---
otero_id: 1164
otero_key: "DAXEBM8E"
title: "A user-centred corporate acquisition system: a dynamic fuzzy membership functions approach"
authors: "Anthony McCloskey; Ronan McIvor; Liam Maguire; Paul Humphreys; Tina O'Donnell"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.11.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A user-centred corporate acquisition system: a dynamic fuzzy membership functions approach

Anthony McCloskey <sup>a</sup>, Ronan McIvor <sup>a,\*</sup>, Liam Maguire <sup>b</sup>, Paul Humphreys <sup>a</sup>, Tina O’Donnell <sup>a</sup>

<sup>a</sup>University of Ulster, Faculty of Business and Management, School of International Business, Magee Campus, Northern Ireland, United Kingdom

<sup>b</sup>University of Ulster, Faculty of Engineering, School of Computing and Intelligent Systems, Magee Campus, Northern Ireland, United Kingdom

Available online 4 January 2005

## Abstract

A user-centred hierarchical system employing scalable fuzzy membership functions, which supports decision making in corporate acquisition process, is presented. The system attempts to simulate the human precedence given to particular financial statistics by using an interchangeable priority system and fuzzy membership scaling. The system receives financial statistics from multiple aspects of a company’s characteristics and makes generalised decisions based on the objectives set out by the focal organisation. The hierarchical structure and the membership scaling of the system are directly linked to the focal organisation’s profile and their acquisition objectives. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Corporate acquisition; Decision making; User-centred; Hierarchical systems; Scalable fuzzy membership functions

## 1. Introduction

Changes in the global environment of many industries have impacted upon how individual firms in those sectors must compete to survive [8]. A strategy that companies have adopted to meet the international challenge has been international expansion via acquisitions [14]. Identifying suitable companies in the vastly diverse and escalating markets requires considerable research effort from the company’s financial experts, whose time represents a considerable investment by the focal organisation [4]. Conversely, in the last decade, advances in computer hardware and software, coupled with the electronic distribution of financial databases such as Value Line, FAME, and Compustat, have provided more readily accessible sources of corporate information.

Recent technologies available for data analysis include: machine learning [13], including induction, data mining, statistical, and conceptual clustering;

neural networks [6]; and genetic algorithms [30]. The objective of this paper is to show how Fuzzy systems [1] can assist in the evaluation of corporate acquisitions. This paper considers the diversity of companies and their immediate objectives in the corporate acquisition process. Consequently, this paper proposes a user-centred system [12] to reflect the position of the focal organisation and the objectives of their acquisition. The proposed system employs a hierarchical fuzzy system [26] with scalable fuzzy membership functions [19,25] to support decision making in the acquisition process. Based on the objectives of the company, financial information will be prioritised, based on its importance from the focal organisation’s perspective. This can be illustrated by the following: if a focal organisation wishes to acquire a company that will increase its market share, it does not necessarily wish to acquire the company with the largest market share. Ideally, they will wish to acquire a company with a smaller or similar market share as their own company. The system attempts to emulate the general rules adhered to by a company’s financial experts, except on a larger scale and in a timeeffective manner. This system enables an extensive database of companies to be considered for possible corporate acquisition while taking account of the personal position and objectives of the focal organisation. This enables financial experts’ access to a tailored system to analyse a greater number of perspective acquisition companies. Particular attention is given to how the system can identify potential acquisition targets through the extraction and analysis of financial information from on-line databases.

![](/api/attachments/DAXEBM8E/fulltext/images/6aac85ec19dfcb8f254df753267698e7720255b9f869c4e7536b01cc70592f81.jpg)  
Fig. 1. The acquisition model.

This paper illustrates the potential benefits of the system by providing results obtained for different real companies from the same on-line database of companies. The system discussed serves as a basis for discussion and future research.

## 2. The acquisition process

One strategy that firms must consider when looking for ways to address the challenge of globalisation in many industries is international expansion via acquisitions [18]. International expansion can provide the firm with an external environment where: new markets exist; labour costs are cheaper; transportation costs are less expensive; and/or the taxes are less. In theory, the organisation decides its objectives and how acquisitions will be part of the strategy to achieve these objectives. It will then proceed to buy a company that meets the required criteria. Once the objectives and criteria of the acquisition are established, the focal organisation must identify companies that meet these objectives; this is the focus of this paper. Clearly, in an international context, there may be thousands of firms representing dozens of industries that may be suitable. In the past, searching for suitable acquisition candidates would involve a considerable amount of research time, examining the relevant financial information of potential companies across different industries and countries. Such effort requires a considerable investment of the acquiring firm’s technical personnel skills and talents. In the last decade, advances in computer hardware and software, coupled with the electronic distribution of financial databases such as Value Line, FAME, and Compustat, have provided more readily accessible sources of corporate information. This provides opportunities for companies to identify or eliminate possible acquisition candidates on-line that may fulfil or not fulfil their initial acquisition criteria without having to carry out extensive desk research. The corporate acquisition model described in this paper attempts to overcome some of the problems associated with the acquisition process, and act as a decision aid for an organisation. However, it must be emphasised that the model is not a panacea for all of the problems associated with corporate acquisition analysis. The model illustrates how the process of evaluating potential acquisitions can be assisted with the aid of a fuzzy system to take advantage of advances in the electronic distribution of on-line corporate databases. The stages involved in this corporate acquisition model are illustrated on a decision tree in Fig. 1. A full description of the stages involved in the model will be presented in Section 3.3. This is followed by a detailed explanation of Stage 3: the hierarchical fuzzy system.

## 3. The development of the acquisition system

## 3.1. Problem definition

The proposed system is concerned with providing a focal organisation with a structure to follow in the corporate acquisition decision-making process. The system aims to assist the focal organisation to correctly identify companies that are of particular relevance to their organisation. The system sets out to address the following aspects of the acquisition process:

To allow the focal organisation to set out the motivation they have in considering the acquisition of another company. What are the set objectives the focal organisation has for the acquisition of a new company (e.g., Is the purpose to increase market share, or obtain access to a particular market?)?

What criteria should be considered when analysing a potential company’s financial situation? Different focal organisation motivations will influence how important different financial statistics are in the acquisition process even to the extent of determining what financial information should be considered.

What qualitative factors should be considered when making the acquisition decision (the quality of product produced by the company, the management quality, and the quality of machinery in the company)?

## 3.2. The selection of development tools

The development tools selected for use in this application are Visual Basic (VB) developed by Microsoft and Matlab (matrix laboratory) developed by The MathWorks. VB is used to acquire data directly from the user, through a series of graphic user interfaces (GUIs), while Matlab is used to implement the mathematical calculations used in the system.

VB provides a development tool for the main development environment, as it enables sharing of data across applications, lower development costs, and user familiarity as most users will be familiar with other Microsoft Office applications. Matlab provides an interactive software system for numerical computations and graphics. It offers matrix-based programming, advanced mathematical functions, and a simplified flexible language. In addition, Matlab has introduced add-on tools specifically for financial professionals such as analysts, which provides a comprehensive set of financial function add-ins for Microsoft Excel and Applix.

## 3.3. The five stages of acquisition

The system is structured around the acquisitions model, as shown in Fig. 1. The model represents the basic hierarchical nature of the decision-making process for corporate acquisition. The fundamental basis of the system is that the user has a clearly defined objective for the corporate acquisition. Therefore, it is essential that a team from various functions of the business should be formed to effectively lay out the focal organisation objectives. An outline of the different stages in the model identifies what is required both of the user and the system at each stage of the acquisition process. An overview of the system as it has been implemented is shown in Fig. 2.

## 3.3.1. Stage 1—set acquisition criteria and objectives

This stage is carried out by the corporate acquisition team. The initial impetus for an acquisition may come from the corporate level of the focal organisation. The corporate acquisition team may decide to pursue an acquisition strategy for a number of reasons such as: for regional diversification; to eliminate competition; as a defensive measure; to gain access to cash; or to increase market share. It will then be the responsibility of the lower levels of management to seek and analyse potential companies that meet the objectives of the corporate acquisition team. The objective of this system is to replace or partly replace the responsibility of the lower levels of management, in that it will seek and analyse potential companies that meet the objectives of the corporate acquisition team. The practical objective of the system at this stage is to capture as much knowledge from the acquisition team as possible so that it can use this knowledge in its identification process. The system will rely a great deal on this initial information in the following stages to identify the correct company for acquisition. Therefore, it is important that the system arrives at definite conclusions from the vague, ambiguous, or imprecise information provided by the acquisition team at this stage.

The initial stage of the process is divided into two sections: the first section deals with the organisation and setting up a profile for the focal organisation. This profile allows the system to know from what perspective the focal organisation is viewing the acquisition process. The perspective of the focal organisation can be of utmost importance in identifying the correct company for acquisition. For example, if the focal organisation wishes to acquire a company to improve its market share, then the profile will identify what market the focal organisation is in and what share of the market it currently holds. This will help identify companies that are of smaller or similar market share to the focal organisation as it is highly unlikely that it wishes to buy out a much larger company that holds a much greater market share. This information, along with other information in the focal organisation profile, helps to personalise the acquisition process and identify more relevant companies for acquisition. The profile of the focal organisation needs only be entered once and then can be updated further as necessary. The focal organisation profile is entered on the system through a VB GUI and stored for use in all future processes on the system.

The second element of Stage 1 is identifying what the motivations and objectives of the focal organisation are in the acquisition process. This is again achieved by using a VB GUI. The GUI allows the user to select their motivation for the acquisition of another company and to set the criteria an acquired company should meet to enable the focal organisation to meet their objectives. This completes the initial information required from the user to enable the system to build up the context in which it is working. Rules based on the knowledge of a financial expert look at the situation that is defined by the user, identifying the perspective of the user and the motivation and objectives for the acquisition. Based on the expert rules and the described context, the system defines the financial categories and the financial ratios that are important to the user, attaching priorities to each of the financial ratios within each category and to each category within the whole system to create a system structure. This structure, along with the identified financial categories and financial ratios with their priorities, is presented to the user and the user is requested to confirm that the structure is representative of their priorities, or to make adjustments so that it is representative.

![](/api/attachments/DAXEBM8E/fulltext/images/1961ff28d748ed1a0ecfe1f3a83daaf9bdd234b3bcdd5430cb99c03075d652e0.jpg)  
Fig. 2. Overview of acquisition system.

## 3.3.2. Stage 2—preliminary identification of potential companies

An extensive list of possible companies for acquisition can be generated. The relevance of a potential company to the focal organisation can be greatly reduced by three decisive factors: the country or region, the industrial sector, and the company size. Utilising the information obtained through the focal organisation profile, motivation, and objectives, the system can identify on-line databases to search and provide the preliminary companies for consideration.

The companies identified can be from an individual on-line database or a combination of on-line databases. The user is free to review and change the on-line databases selected by the system and to alter the selection criteria. Once potential companies have been identified, the information on the companies will be downloaded and stored on the system and can be accessed or updated for future acquisition processes. For the purposes of a demonstration of the system, the FAME database was used as the data source for extracting and analysing the financial profiles of a sample of companies. The FAME database is one of many on-line databases containing financial figures on companies from a range of industry sectors. For purposes of this analysis, the region was set to the UK, and the industrial sector set to Computing. This identified a set of 50 companies as potential acquisition companies. A file was then created containing all the financial results and other details concerning the performance of each company.

## 3.3.3. Stage 3—financial analysis of potential companies

Once a grouping of potential companies for acquisition has been identified through Stage 2, a further analysis is required. This financial analysis will deal with a large number of companies as the identification of potential companies in Stage 2 is expected to return a substantial number of companies. This analysis considers the financial data available from the on-line database and the financial priority settings defined by the expert rules in Stage 1. The system uses the financial categories identified in Stage 1 of the process as the building blocks of the fuzzy hierarchical system. A fuzzy system is created for each of the categories with the relevant financial ratios as the inputs; this forms the bottom layer of the fuzzy hierarchical system.

Subsequently, the output from each category fuzzy system forms an input to another fuzzy system that accumulates the categories, which is on the second layer of the fuzzy hierarchical system. In essence, Stage 1 of the process provides Stage 3 with information to create the building blocks and structure of the system, while Stage 2 provides the data for Stage 3 to process. The output from Stage 3 is a descending list of companies with the most suitable company for corporate acquisition listed first; the user is then free to select the top five, or a user-determined number, for further analysis in Stage 4. Stage 3 of the process is explained in detail in Section 3.3.4.

## 3.3.4. Stage 4— analysis of selected companies (internal and external)

Stage 4 is not within the scope of this paper. However, a brief description will be given to identify how the entire system will work. The objective at this stage is to determine the compatibility of the potential takeover companies to the motivation and objectives of the focal organisation set out in Stage 1. Multiattribute analysis (MAA) is applied to the analysis of these categories. MAA is capable of selecting or identifying optimum choice in respect of the same objectives where the decision alternatives are predetermined [10]. Dean and Schniederjans [5] found that employing simple ranking methods does not allow for the interactive effects of multiple criteria. The relative importance of differing criteria may not be adequately weighted in the final analysis because ranking is assessed based on a single criterion, rather than the ranking of importance of multiple conflicting criteria. The advantages of MAA are primarily that it facilitates decision making despite the presence of multiple conflicting criteria. Hence, it is suitable for the multicriteria/multialternative nature of this stage (i.e., the evaluation and selection of a suitable company for acquisition). It is not within the scope of this article to describe the application of MAA.

## 3.3.5. Stage 5—establish acquisition program

Having identified a target company and established as much about it as possible from published and other third-party sources, the next stage is to establish an acquisition program and complete the acquisition. Key issues to be addressed are: organising for acquisition, making the approach, handling negotiations, valuation, managing currency risk if appropriate, management issues, handling industrial relations, and necessary commitment [9]. This is not an exhaustive list of the factors involved in the analysis. However, it highlights and demonstrates the complexity and ramifications of making an effective acquisition. Each case will be different; but in every case, considerable commitment is required by the focal organisation and a thorough analysis is necessary for each factor.

## 4. Hierarchical fuzzy system with scalable fuzzy membership functions

This section provides a more detailed look at Stage 3 of the acquisition process. Stage 3 is a hierarchical fuzzy system that uses scaling to prioritise the inputs to the fuzzy system. Fuzzy systems were developed due to the understanding that measurements, process modelling, and control can never be exact for real and complex processes. Also, there are uncertainties such as incompleteness, randomness, and ignorance of data in the process model. The seminal work by Zadeh [27–29] introduced the concept of fuzzy logic to model human reasoning from imprecise and incomplete information by providing a computational framework for vague information. Fuzzy logic can incorporate human experiential knowledge and give it an engineering meaning to control ill-defined systems with nonlinearity. There are many interpretations of fuzzy modelling. For instance, a fuzzy set is a fuzzy model of human concept. In this study, a fuzzy model is understood as an approach to form a system model using a descriptive language based on fuzzy logic with fuzzy predicates. Fuzzy models consist of linguistic explanations about the system behaviour. Apart from fuzzy control, there are many studies on fuzzy modelling. Those are divided into two groups: the first group deals with fuzzy model of the system itself or a fuzzy model for simulation [7,15,24]; and the second group deals with fuzzy modelling of a plant for control [3,23]. In this system, we are using linguistic terms to define how import particular financial categories and ratios are in the acquisition process.

In the proposed system, the structure of the system is taken from Stage 1 of the process by the number of different financial categories required by the user and how the different categories are accumulated. Each category identified by the user forms a fuzzy system and the outputs are accumulated to form the system output. The inputs to each fuzzy system are scaled according to priorities set in Stage 1 of the acquisition system. This structure is defined by the priorities that are represented by a set of expert rules that define the most suitable priorities according to the objectives and criteria set out by the focal organisation in Stage 1. These priorities can be viewed and altered by the user at the beginning of Stage 3. In this paper, a two-level hierarchical system is illustrated; however, this can be easily expanded to three levels to accommodate more complex priority settings. The additional levels allow the merging of financial categories at different levels within the hierarchical system, therefore accommodating more complex priority settings. A model of the structure of a three-level hierarchical system is illustrated in Fig. 3.

The number of financial categories, their priorities, and where they fit in the hierarchy determine the structure of the system. For the purposes of this paper, four categories have been identified: profitability, liquidity, efficiency, and, finally, financial strength and gearing and a two-level system with one accumulator fuzzy system. The user is not limited to a set number of categories or financial ratios within each category; the selections made are for demonstration only. Within each category, important financial ratios that are considered to offer the best information about that particular category are selected. The financial categories and ratios selected are shown in Appendix A. Different companies may choose alternative categories or add more categories with alternative combinations of financial ratios that better reflect what they consider relevant in their acquisition process.

![](/api/attachments/DAXEBM8E/fulltext/images/df6b8eb298fdc963160795d837acd5b647354888e1e46af7513fd7c78cdc1158.jpg)  
Fig. 3. Hierarchical fuzzy systems.

## 4.1. Fuzzy inference method

The fuzzy inference method used in this system is the Takagi–Sugeno–Kang (TSK) method, which was introduced in 1985 [20–22]. The TSK method was selected rather than the fuzzy inference method of Mamdani and Assilian [11], as it is more computationally efficient and it works well with optimisation and adaptive techniques [2]. A zero-order TSK fuzzy model is used in this paper but it is proposed to use a first-order TSK fuzzy model in future work as the system evolves.

## 4.2. Input membership function

Once the basic structure of the system has been established, the next stage is to determine the membership functions for the inputs to each fuzzy system. Heuristic selections of parameters of membership functions are widely used and practiced in fuzzy modelling and applications. Other techniques that reflect the actual data distribution by using learning algorithms where some input/output data are available have also been proposed. There are different approaches to construct membership functions such as:

n Heuristic selection

n Clustering approach

n C-means clustering approach

n Adaptive vector quantization

n Self-organising map.

Detailed descriptions of these approaches can be found in Ref. [3]. In this paper, three major factors are considered when determining the membership functions for each input:

The first is the total range of all membership functions: the universe of discourse. As the system must determine how each company in the database performs in relation to the strongest and weakest benchmarks for each financial ratio, therefore the strongest and weakest companies are used to determine the total membership range of all the membership functions.

n The second factor is how the data are dispersed between the strongest and weakest benchmarks. If data are evenly dispersed, then membership functions with equal width would be suitable; however, if data are concentrated in a particular range, then membership functions with unequal widths would be more appropriate. Therefore, the widths of membership functions will be determined by the dispersion of the data within the membership range.

n The last is the priority level given to the input in the system; this will determine the maximum degree of membership possible for each membership function.

## 4.3. Membership range

The range of the membership functions in any financial ratio is determined by the strongest and weakest values retrieved in the input data. All the input data are normalised with the strongest input value set as 1 (x-axis) and the weakest value set as 0 (x-axis). This sets the extremes that the fuzzy membership functions must cover. The authors have arbitrarily selected five membership functions across each universe of discourse for illustration purposes. Increasing the number of membership functions may improve the model accuracy but will increase computational demands. The five membership functions have been termed: <sup>b</sup>very poor,<sup>Q</sup> <sup>b</sup>poor,<sup>Q</sup> <sup>b</sup>average,<sup>Q</sup> <sup>b</sup>good,<sup>Q</sup> and <sup>b</sup>very good.<sup>Q</sup> Assuming that the input is equally dispersed, the membership functions were evenly divided across the range. For example, in the Profitability category, one of the three input ratings is net profit margin; the strongest value in the industry was 46% and the weakest value was 3%, if the data were evenly dispersed across the range of the membership functions shown in Fig. 4.

Using these membership functions, each company in the sector under analysis is assigned a membership function based upon its position in the range. In the example shown in Fig. 4, a company with a net profit margin of 25% would be normalised to 0.58 and so would be a part of the mf3 (<sup>b</sup>average<sup>Q</sup>) and mf4 (<sup>b</sup>good<sup>Q</sup>). The degree of membership of each function would relate to the shape of the membership function used; in this case, a triangular shape [16,17]. The triangular curve is a function of a vector x, and depends on three scalar parameters a, b, and c as given by:

$$
f (x; a, b, c) = \left\{ \begin{array}{l l} 0, & x \leq a \\ \frac {x - a}{b - a}, & a \leq x \leq b \\ \frac {c - x}{c - b}, & b \leq x \leq c \\ 0, & c \leq x \end{array} \right.\tag{1}
$$

The parameters a and c locate the feet of the triangle and parameter b locates the peak as illustrated for mf2 in Fig. 4. The degree of membership of mf3 (<sup>b</sup>average<sup>Q</sup>) would be in the region of 0.5 and the degree of membership of mf4 (<sup>b</sup>good<sup>Q</sup>) would be in the region of 0.1, with 1.0 representing full membership. This process is carried out for each company in each financial ratio and for each financial category.

4.4. Width of individual membership functions to cover data dispersion

If data are dispersed evenly across the membership range, then the fuzzy membership functions are divided evenly over the range with partition of unity as illustrated in Fig. 4. The even division of the membership function over the range enables the membership functions to have partition of unity. However, from analysis of the data, it was apparent that a small number of companies were present at the extremes of the membership range and that the data were not evenly dispersed across the membership range. In these circumstances, the fuzzy membership functions are altered. In the range were data are concentrated, the width of the fuzzy membership functions is narrowed, and in the areas of sparse data, the width of the membership function is widened. This widening and narrowing of the membership functions attempt to create an even distribution of companies in each membership function. In order to mathematical calculate how the membership functions are narrowed or widened for each membership function, three points are found in the range. The three points correspond to the b parameter or the peaks of mf2, mf3, and mf4. The b parameter of mf1 and mf5 is set to 0 and 1, respectively. The other three b parameters or peaks are calculated using the following formulas:

![](/api/attachments/DAXEBM8E/fulltext/images/feb4215337dfbc2e552eb0b2a9067b7b22ffc04b30a31ab3b1956e4519b362e7.jpg)  
Fig. 4. Example of fuzzification scheme.

$$
m f 2 (b) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{2 (n)}\tag{2}
$$

$$
m f 3 (b) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}\tag{3}
$$

$$
m f 4 (b) = \left(\frac {1 - \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}}{2}\right) + \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}\tag{4}
$$

where n=number of inputs for x.

The important factor in this calculation is that partition of unity must be maintained; therefore, once the peaks of the five membership functions have been calculated, points a and c of the feet of the membership functions are routinely defined. Partition of unity ensures that at any point in the range, the degree of membership combines to produce 1; this may be 0.2 of mf1 and 0.8 of mf2, or simply 0.5 of each or a complete 1 of either and 0 of the other. An example of how the membership functions would change to account for the unevenly dispersed data across the membership functions is illustrated in Fig. 5. The data represented are more concentrated in the lower end of the membership range; therefore, the membership widths of the lower membership functions are smaller to more evenly divide the data between membership functions.

## 4.5. Priority levels and scaling

To identify the aim of the acquisition team, the system translates the motivation and objectives of the focal organisation into fuzzy priorities. These priorities are set within the financial categories and the financial ratios within each financial category. The translation is based on a financial expert’s rules for financial priorities, given the motivation and objectives of a focal organisation in the corporate acquisition process. These rules give priority to one financial category over the other and priority to one financial ratio over the other within each financial category; the rules contain five general levels of priority:

![](/api/attachments/DAXEBM8E/fulltext/images/ab4ac8f0bfc8b9e8b91f323dda3d29dc99fa1ed7769a81e9c45c20256a0b6da5.jpg)  
Fig. 5. Unevenly dispersed data in membership range.

! <sub>Very</sub> <sub>high</sub> <sub>priority</sub>

! <sub>High</sub> <sub>priority</sub>

! <sub>Medium priority</sub>

! <sub>Low</sub> <sub>priority</sub>

! <sub>Very</sub> <sub>low</sub> <sub>priority.</sub>

The four financial categories: Profitability, Efficiency. Liquidity, and Financial Strength and Gearing are arranged into priorities based on the focal organisation’s motivation and objectives through the expert rules in Stage 1. The user is permitted to view these priorities and accept or adjust them if they wish. Within each financial category, the financial ratios are also prioritised into the same five priority levels. Again the priorities are based on an expert’s rules, and the motivation and objectives set out by the acquisition team. Like the financial categories, these priority levels can be accepted or adjusted by the Acquisition team. To incorporate the priority levels set out in Stage 1, the fuzzy membership functions are adjusted to reflect the priority level given to the individual category or financial ratio. The standard membership function allows a degree of membership from 0 to 1; this has been illustrated previously in Figs. 4 and 5 as each membership function rises to 1 on the y-axis. The proposed scaling of the membership functions replaces this membership function for each input with a scaled membership function. This scaling changes the membership functions in accordance to the priority level given to the input:

<table><tr><td>Very high priority</td><td>0-1.0</td></tr><tr><td>High priority</td><td>0-0.8</td></tr><tr><td>Medium priority</td><td>0-0.6</td></tr><tr><td>Low priority</td><td>0-0.4</td></tr><tr><td>Very low priority</td><td>0-0.2</td></tr></table>

The triangular function define in Eq. (1) is altered to enable the degree of membership of a function to be changed. The triangular curve is still a function of the vector x, but now depends on four scalar parameters a, b, c, and d. The d parameter determines the maximum degree of membership for the membership function. The triangular function is given by:

$$
f (x; a, b, c) = \left\{ \begin{array}{l l} 0, \quad x \leq a \\ \frac {(x - a) d}{b - a}, & a \leq x \leq b \\ \frac {(c - x) d}{c - b}, & b \leq x \leq c \\ 0, \quad c \leq x \end{array} \right.\tag{5}
$$

The five membership functions for the five priority levels—very high priority, high priority, medium priority, low priority, and very low priority—are illustrated in Fig. 6.

This scaling determines how influential a particular input can be; as the degree of membership for the input is limited, this limiting factor determines how influential the input is on the output of the system. This scaling determines the influential levels of the financial ratio within each financial categories and how influential each financial category is in determining the final companies identified as being suitable for further analysis.

## 4.6. Rules for the fuzzy systems

Each fuzzy system produces an output from their respective inputs. This output is determined by the rules employed by the fuzzy system. The combination of rules that are fired and the firing strength of the rule determine the output from the fuzzy system. The number of rules defined in this system is a product of the number of membership functions in each input. For example, the profitability category has three inputs (net profit, gross profit, and profit per employee), each with five membership functions (very poor, poor, average, good, and very good). Therefore:

The number of rules for the profitability category

$$
= p ^ {n}\tag{6}
$$

where p=number of sets; n=number of inputs.

The set of if–then statements used to formulate the conditional statements that comprise fuzzy logic in this system uses the <sup>b</sup>OR<sup>Q</sup> operator. This gives an output to each rule, each time any input in the rule is firing. The <sup>b</sup>OR<sup>Q</sup> operator uses the maximum function, which maintains the creditability of the scaling of the degree of membership for each input. Using an <sup>b</sup>AND<sup>Q</sup> operator or the minimum function negates the creditability of the scaling of the degree of membership for each input. The rules set on the system do not require expert knowledge and will grow or reduce depending on the number of inputs to the system and the number of membership functions. The rules account for every possible combination of inputs. They are set, but what rules are fired and the strength of the firing are determined by the inputs to the system, which is determined by the input data of the each company. The maximum aggregation method is used in the aggregation of the rules in this system and an aggregate output fuzzy set is formed. The defuzzification method used in each fuzzy system is weighted average. The fuzzy output produces a crisp output. That is used as an input to the next level of the hierarchy, which combines the outputs of the four financial categories to form the final output. The output of this fuzzy system will determine what companies are to be considered for further analysis.

## 5. Results

This section reviews the results achieved in Stage 3 of the acquisition system and the merits of the results. The merits of the acquisition system are illustrated in the processing of two focal organisations seeking companies for corporate acquisition. The financial categories and financial ratios used in both companies are the same, and the same two-level hierarchical structures are used. The focal organisation’s profile and aims and objectives are different, which results in different priority settings being identified for the two focal organisations. The difference in the priority settings will cause the system to identify different companies for acquisition for the two focal organisations. Focal organisation A has been set with no financial priorities. Focal organisation B has a range of priorities within each financial category and for the overall system. The financial priorities for each company are defined in Appendix A. The data used in the results are real data that have been downloaded from the FAME on-line database; the individual company names have been replaced to protect their identity.

## 5.1. Database of companies’ normalised data

The database of companies used for the demonstration of the acquisition system consists of 50 companies, which are real companies but have been given the names Companies 1–50. The relevant financial ratios for each financial category have been normalised to produce a value between 0 and 1 for each ratio. These data have been plotted in graphical form to show the varying strengths and weaknesses of each company as shown in Fig. 7.

![](/api/attachments/DAXEBM8E/fulltext/images/b7dc7d538bf9dd767a46c315ed26895c2aee228521fbc6f65560ca3e2d49d1cc.jpg)

![](/api/attachments/DAXEBM8E/fulltext/images/3c69e4ce56c8fbd29c5ccde9fcf8199eb77c84a34ace178258307f604ce609cf.jpg)

![](/api/attachments/DAXEBM8E/fulltext/images/d4059b8708b104db264389683c5935acfd39d39cff686128042cf33751f72c29.jpg)

![](/api/attachments/DAXEBM8E/fulltext/images/0b729eca3512d54afc274f10708868467d9c0274c3401d3a32de666d2b2adb67.jpg)

![](/api/attachments/DAXEBM8E/fulltext/images/df2013db4eacb098baba6058d5fc918a3249a6973ab116216124bfadc8ccbf06.jpg)  
Fig. 6. Fuzzy membership functions—priority scaling.

Fig. 7a shows the Profitability Category, which contains three financial ratios: net profit percentage, gross profit percentage, and profit per employee. As can be seen in the graph, the strongest company in the net profit percentage is Company 42 while the weakest is Company 40; in the gross profit percentage, the strongest company is Company 33

(b)

(d)  
(a)  
![](/api/attachments/DAXEBM8E/fulltext/images/33daf75391df8dec99fddabc86acd2a1b0f115fa87a1996ee763fca3cdfac046.jpg)

![](/api/attachments/DAXEBM8E/fulltext/images/12a390efd1b2333a8a79f77c625bff5c40deaab5157fa14ed11876b3a3000275.jpg)

(c)  
![](/api/attachments/DAXEBM8E/fulltext/images/17ce1227d528b42cd7fdd3077b7d9a80cac2327d28d8df52ae8b702668435ef5.jpg)

![](/api/attachments/DAXEBM8E/fulltext/images/59c70133a1b349ddd84ab163024bd263b006d630f31a626f2a766adfb4f9b01b.jpg)  
Fig. 7. Normalized input values for selected financial categories.

while the weakest is Company 3; and in the profitper-employee ratio, the strongest company can be seen to be Company 11 while the weakest company is Company 41.

Fig. 7b shows the Efficiency Category, which contains three financial ratios: net asset turnover, fixed asset turnover, and return on capital employed. In the graph, it can be seen that in the net asset turnover, the strongest company is Company 11 while Company 40 is the weakest; in the fixed asset turnover, Company 20 is the strongest while Company 40 is the weakest again; and in the return on capital employed, Company 50 is the strongest while Company 5 is the weakest.

Fig. 7c shows the Liquidity Category, which contains two financial ratios: liquidity ratio and current asset ratio. As can be seen in the graph,

Company 27 is the strongest company both in liquidity ratio and current asset ratio; while Company 50 is the weakest in the liquidity ratio and Company 30 is the weakest in current asset ratio.

Fig. 7d shows the Gearing Category, which contains three financial ratios: gearing ratio, solvency ratio, and return on shareholders Fund. As shown in the graph, the strongest company in the gearing ratio is Company 17 while the weakest is Company 11; in the solvency ratio, Company 31 is the strongest while Company 44 is the weakest; and in the return on shareholders fund, the strongest company is Company 11 while Company 12 is the weakest. The graphs shown clearly illustrated the relative strengths and weaknesses of the companies that have been processed in this database.

## 5.2. Acquisition system results per fuzzy system

The fuzzy systems used to process the financial categories are represented in Fig. 8. The scaled financial ratios are used as inputs to the fuzzy system and the output is a single crisp number that represents the aggregation and defuzzification of the inputs. The fuzzy system calculates a single crisp output for each of the companies in the database.

The results presented are for focal organisation A, which has no set priorities, and for focal organisation B, which has priorities as defined in Appendix B. The results show the output from the four fuzzy systems that account for the four financial categories chosen for this demonstration: Profitability, Efficiency, Liquidity, and Gearing. The results are shown in graphical form so comparison of results can be easily achieved. Due to the nature of the membership functions, the important fact is not in what position a company achieves, although this is a good indicator; it is the magnitude of difference that is achieved in comparison to the other companies and the position in relation to the average of all the companies. The average is used to determine the position of the all the membership functions; therefore, a company’s position in relation to the average ratio will determine which membership functions it will fall under. This can be illustrated in a simple example. If five inputs have the values 0.4, 0.5, 0.3, 0.1, and 0.7, the average is 0.4 and any value from 0.4 down will be considered <sup>b</sup>average,<sup>Q</sup> <sup>b</sup>poor,<sup>Q</sup> or <sup>b</sup>very poor<sup>Q</sup>; however, if the input values have values 0.8, 0.9, 1.0, 0.8, and 0.5, the average is 0.8 and anything from 0.8 down will be considered <sup>b</sup>average,<sup>Q b</sup>poor,<sup>Q</sup> or <sup>b</sup>very poor.<sup>Q</sup> Therefore, a company that achieves a value of 0.5 may, in the first instance, be part of the membership functions <sup>b</sup>average<sup>Q</sup> and <sup>b</sup>good,<sup>Q</sup> while in the second instance be part of the membership functions <sup>b</sup>average<sup>Q</sup> and <sup>b</sup>poor.<sup>Q</sup>

![](/api/attachments/DAXEBM8E/fulltext/images/4ef2b2da4836338ad8e52fa8019e663e12209551fe31ed82706258c34c5786cb.jpg)  
Fig. 8. Fuzzy inference system—financial category.

The results from the profitability fuzzy system will be analysed in detail in this paper, while the results from the other fuzzy system are presented in Appendices C D E. The output results from the profitability fuzzy system are shown in Fig. 9.

Table 1 identifies the order of the companies from the profitability fuzzy system for both focal organisations A and B. As can be seen in the table, the general suitability of companies for the two acquiring companies is different. This is due to the changed priorities within the system. The system enables ratios of higher importance to have greater influence over the output but not to the extent that a high priority ratio can fully determine the output.

The strongest prospect for acquisition for both focal organisations is Company 42, but it is a more emphatic prospect for focal organisation B. This is due to the fact that net profit is given a very high priority in focal organisation B and Company 42 is the best company in this financial ratio by a strong margin.

Company 11, which is returned in second position for both focal organisations, is in 39th position in the net profit ratio but still holds second position when net profit is given a very high priority. This is due to the fact that although net profit is a very high priority, it is not the only determiner and because Company 11 has done well in the other financial ratios: second in gross profit ratio, and first in the profit-per-employee ratio.

Company 16, which obtained third position for focal organisation B, is in the 14th position for focal organisation A. It achieves this rise in position due to the fact that the net profit ratio for Company 16 is in fifth position and has a value of 0.6734, well above the average of 0.493. Company 16 does not do as well in the other two categories as can be seen in Table 2, but as they are of a lower priority as they have less influence. The fact that Company 16 has done better than other companies that are above it in the net profit ratio, such as Companies 44, 27 and 15, shows how it secures the third position for focal organisation B. This illustrated how doing well in a high priority financial ratio will heavily influence a company’s case for acquisition but will not be the only determining factor. As in the case with Company 11, the combination of doing well in a number of the lower priority financial ratios also heavily influenced the company’s case for acquisition. This system achieves a balance that enables a financial

![](/api/attachments/DAXEBM8E/fulltext/images/706f9182020bc8972bf8809bf910191909a45849baf3676bfd2143282e7d8696.jpg)  
Fig. 9. Profitability output for focal organisations A and B.

Table 1  
Top half of companies in the profitability category

<table><tr><td colspan="5">Profitability</td></tr><tr><td>Position</td><td colspan="2">Focal organisation A</td><td colspan="2">Focal organisation B</td></tr><tr><td>1st</td><td>Company 42</td><td>0.567</td><td>Company 42</td><td>0.6051</td></tr><tr><td>2nd</td><td>Company 11</td><td>0.5636</td><td>Company 11</td><td>0.5249</td></tr><tr><td>3rd</td><td>Company 19</td><td>0.531</td><td>Company 16</td><td>0.5227</td></tr><tr><td>4th</td><td>Company 17</td><td>0.5221</td><td>Company 27</td><td>0.5207</td></tr><tr><td>5th</td><td>Company 28</td><td>0.5169</td><td>Company 49</td><td>0.5139</td></tr><tr><td>6th</td><td>Company 49</td><td>0.5148</td><td>Company 33</td><td>0.5136</td></tr><tr><td>7th</td><td>Company 33</td><td>0.5121</td><td>Company 19</td><td>0.5124</td></tr><tr><td>8th</td><td>Company 14</td><td>0.5116</td><td>Company 44</td><td>0.5105</td></tr><tr><td>9th</td><td>Company 10</td><td>0.5089</td><td>Company 15</td><td>0.5095</td></tr><tr><td>10th</td><td>Company 26</td><td>0.5075</td><td>Company 17</td><td>0.5085</td></tr><tr><td>11th</td><td>Company 1</td><td>0.507</td><td>Company 28</td><td>0.5073</td></tr><tr><td>12th</td><td>Company 20</td><td>0.505</td><td>Company 45</td><td>0.5072</td></tr><tr><td>13th</td><td>Company 47</td><td>0.5049</td><td>Company 2</td><td>0.504</td></tr><tr><td>14th</td><td>Company 16</td><td>0.5025</td><td>Company 47</td><td>0.5035</td></tr><tr><td>15th</td><td>Company 46</td><td>0.5</td><td>Company 20</td><td>0.5025</td></tr><tr><td>16th</td><td>Company 45</td><td>0.4972</td><td>Company 26</td><td>0.5005</td></tr><tr><td>17th</td><td>Company 35</td><td>0.4967</td><td>Company 10</td><td>0.5001</td></tr><tr><td>18th</td><td>Company 27</td><td>0.4934</td><td>Company 9</td><td>0.4992</td></tr><tr><td>19th</td><td>Company 18</td><td>0.4903</td><td>Company 14</td><td>0.4988</td></tr><tr><td>20th</td><td>Company 6</td><td>0.4889</td><td>Company 38</td><td>0.4985</td></tr><tr><td>21st</td><td>Company 5</td><td>0.4879</td><td>Company 22</td><td>0.4984</td></tr><tr><td>22nd</td><td>Company 22</td><td>0.4863</td><td>Company 39</td><td>0.4982</td></tr><tr><td>23rd</td><td>Company 2</td><td>0.4849</td><td>Company 36</td><td>0.4976</td></tr><tr><td>24th</td><td>Company 48</td><td>0.4843</td><td>Company 18</td><td>0.4965</td></tr><tr><td>25th</td><td>Company 38</td><td>0.4814</td><td>Company 37</td><td>0.4958</td></tr></table>

ratio to be more influential but without complete control. This enables a simulated human reasoning where one aspect may influence a decision more but not to the extent that it negates the influence of other aspects. Other category results are presented in Appendices C, D and E.

## 5.3. Acquisition system output fuzzy system

The final stage of the fuzzy hierarchy is the output fuzzy system, which summates the outputs from all the financial category fuzzy systems. The inputs to the output fuzzy system are also scaled membership function, with the scaling depending on the priority level given to each individual financial category in the context of the entire system. An overview of the output fuzzy system has been illustrated in Fig. 10. The results obtained from the output fuzzy system provide a rating for each company, which indicated how suitable it would be for corporate acquisition for a particular focal organisation. The system or user can then select a number of the top companies identified for further analysis.

For focal organisations A and B, the companies identified for corporate acquisition are presented in Fig. 11. The company with the highest output value is considered to be the most suitable company for acquisition for the particular focal organisation. As illustrated in the graph for focal organisation A, the most suitable company for acquisition is Company 27 followed by Company 42 and then Company 14. The top three companies for focal organisation B are Company 42 followed by Company 14 and then Company 10. The change in order identified for each focal organisation can be attributed to two issues: the first is the change in companies identified as the strongest in each financial category due to the change in the priorities of the financial ratios, and the second is the change due to the priorities given to the financial categories. This can be seen with Company 42, which has risen to top position for focal organisation B as it holds the top position in the profitability category for focal organisation B by a significant margin but also because it is around average in the efficiency category, high in the liquidity category, and above average in the gearing category. Company 27, which is identified as the best company for focal organisation A, has its real strength in liquidity in which it is top by a good margin, but for focal organisation B, liquidity is of a very low priority; therefore, Company 27Vs real strength is not of any benefit to focal organisation B and so it drops out

Table 2  
Top ten companies system output

<table><tr><td colspan="5">System output</td></tr><tr><td>Position</td><td colspan="2">Focal organisation A</td><td colspan="2">Focal organisation B</td></tr><tr><td>1st</td><td>Company 27</td><td>0.544</td><td>Company 42</td><td>0.5425</td></tr><tr><td>2nd</td><td>Company 42</td><td>0.5394</td><td>Company 14</td><td>0.5401</td></tr><tr><td>3rd</td><td>Company 14</td><td>0.5389</td><td>Company 10</td><td>0.5378</td></tr><tr><td>4th</td><td>Company 11</td><td>0.5374</td><td>Company 28</td><td>0.5377</td></tr><tr><td>5th</td><td>Company 28</td><td>0.5374</td><td>Company 17</td><td>0.5376</td></tr><tr><td>6th</td><td>Company 19</td><td>0.5365</td><td>Company 35</td><td>0.5375</td></tr><tr><td>7th</td><td>Company 44</td><td>0.5365</td><td>Company 18</td><td>0.5372</td></tr><tr><td>8th</td><td>Company 17</td><td>0.5363</td><td>Company 37</td><td>0.5372</td></tr><tr><td>9th</td><td>Company 47</td><td>0.5362</td><td>Company 33</td><td>0.5371</td></tr><tr><td>10th</td><td>Company 46</td><td>0.5361</td><td>Company 32</td><td>0.537</td></tr></table>

![](/api/attachments/DAXEBM8E/fulltext/images/ef30da5268405b144e92346dc60de2db39536abf55ff7ad44d14028dd15efaed.jpg)  
Fig. 10. Fuzzy inference system—accumulated categories.

of the top 10. The graphical representation of the results illustrates how close each company is in its suitability for acquisition; a large drop on the y-axis equates to a large drop in the suitability of the company for acquisition.

The results presented illustrate the levels of influence that can be obtained through the use of a fuzzy hierarchical system with scalable fuzzy membership functions. The results show how natural priorities are implemented to influence the results to varying degrees without completely controlling the final result.

![](/api/attachments/DAXEBM8E/fulltext/images/069cb9040a683d025be28f242a735d9a0e4d2c59c50d0e2028312f9a32d6a823.jpg)  
Fig. 11. Comparing company output ratings for acquiring companies A and B.

## 6. Conclusions and future research

An acquisition system that provides a system that assists in the evaluation of corporate acquisitions has been presented in this paper. A user-centred approach that adequately reflects the position of any focal organisation and the objectives of their acquisition has been achieved. The major benefit of this system is that in a computationally inexpensive manner, the acquisition system is capable of implementing a range of user priorities that influence to varying degrees the system output. The priorities of financial data within the system have been deduced using expert rules utilising the focal organisation’s profile and their acquisition objectives. The expert rules prioritise financial information, based on its importance from the focal organisation’s perspective. These expert rules define what can be assumed to be financial priorities given a set of circumstances and an environment. The system presents its representation of the financial priorities to the user and allows the user to adjust or disregard these priorities if required, enabling full control to remain with the actual user. The hierarchical fuzzy system with scalable fuzzy membership function employed imparts user priorities onto the system that can gently or strongly influence the company selection process. This provides a computationally inexpensive manner of applying the prioritised influences involved in the human decision-making process. The system attempts to emulate the financial influences and priorities adhered to by a company’s own financial experts, but on a larger scale and in a more timely and costeffective manner. The proposed approach has been implemented and tested on real companies and financial ratios from the on-line financial database, FAME. The results presented in this paper illustrate the varying degrees of influence that have been exerted on the system and how the system has successfully emulated the acquisition process adhered to by financial experts. The results demonstrate an accurate reflection of suitable companies for acquisition for individual focal organisations. In comparison to a financial expert assessment of the identified companies based on similar focal organisation priorities, the same principal companies have been identified as possible acquisition targets. Judging by the results obtained and the feedback received, it can be concluded that the approach is of significant use to the financial expert and can be of considerable help in the real world acquisition process.

The authors are currently working on developing two areas:

Learning scaling factors: The constant scaling employed in this paper is effective, but a future development would attempt to encompass more understanding of the user priority meaning. This understanding would negotiate the beliefs of the user in the context of the priority settings, negotiating the value of the priority settings in a uniform or nonuniform manner. It is purposed that several methods of computational intelligence will be investigated, including fuzzy logic, neural networks, and Evolutionary computing, or a hybrid combination of these computational techniques.

Learning hierarchical structures and level groupings: A simple hierarchical system has been illustrated in this paper, but as the complexity of the focal organisations objectives grow and the complexity of financial data being analysed expands, then the hierarchical structure will become more complex. The correct grouping of financial inputs into different levels and sublevels within each financial category and within the whole system requires an intelligent system. The intelligent system will determine the number of levels required in the hierarchy and the interconnections of the hierarchy. The intelligent system will also balance the advantage of creating numerous levels within the hierarchy against the computational and financial costs of creating additional fuzzy systems. This system will also employ intelligent techniques.

Future investigation will develop a means to efficiently obtain knowledge from the user on an ongoing basis so that the system is continually adapting to the changes in the financial environment and the changes in the users. This adaptive knowledge will be applied in appropriate form to both the scaling and hierarchical systems. The possible use of a reinforcement learning system will be investigated to enable continual learning from both positive and negative knowledge acquired through the identification of correct and incorrect companies for acquisition. This will realise an evolvable system that develops with the user.

## Appendix A. Financial categories and financial ratios

Category 1: Profitability Financial ratio 1: gross profit percentage Financial ratio 2: net profit percentage Financial ratio 3: profit per employee

Category 2: Efficiency Financial ratio 1: return on capital employed Financial ratio 2: net asset turnover Financial ratio 3: fixed asset turnover

Category 3: Liquidity Financial ratio 1: liquidity ratio Financial ratio 2: current asset ratio

Category 4: Financial strength and gearing Financial ratio 1: return on shareholders funds Financial ratio 2: gearing Financial ratio 3: solvency ratio.

Appendix B. Financial priorities of focal organisations

<table><tr><td colspan="2"></td><td>Acquiring company A</td><td>Acquiring company B</td></tr><tr><td rowspan="4">Category</td><td>Profitability</td><td>Very high priority</td><td>Very high priority</td></tr><tr><td>Efficiency</td><td>Very high priority</td><td>Medium priority</td></tr><tr><td>Liquidity</td><td>Very high priority</td><td>Very low priority</td></tr><tr><td>Gearing</td><td>Very high priority</td><td>Very low priority</td></tr><tr><td rowspan="3">Profitability</td><td>Net profit ratio</td><td>Very high priority</td><td>Very high priority</td></tr><tr><td>Gross profit ratio</td><td>Very high priority</td><td>Medium priority</td></tr><tr><td>Profit/employee</td><td>Very high priority</td><td>Very low priority</td></tr><tr><td rowspan="3">Efficiency</td><td>Net asset turnover</td><td>Very high priority</td><td>Very high priority</td></tr><tr><td>Fixed asset turnover</td><td>Very high priority</td><td>Medium priority</td></tr><tr><td>Return on capital</td><td>Very high priority</td><td>Very low priority</td></tr><tr><td rowspan="2">Liquidity</td><td>Liquidity ratio</td><td>Very high priority</td><td>Very high priority</td></tr><tr><td>Current asset ratio</td><td>Very high priority</td><td>Very low priority</td></tr><tr><td rowspan="3">Gearing</td><td>Gearing</td><td>Very high priority</td><td>Very high priority</td></tr><tr><td>Solvency ratio</td><td>Very high priority</td><td>Medium priority</td></tr><tr><td>Return on shareholder fund</td><td>Very high priority</td><td>Very low priority</td></tr></table>

Appendix C. Top 10 companies’ efficiency category for focal organisations A and B

<table><tr><td colspan="5">Efficiency</td></tr><tr><td>Position</td><td colspan="2">Focal Organisation A</td><td colspan="2">Focal Organisation B</td></tr><tr><td>1st</td><td>Company 20</td><td>0.5701</td><td>Company 11</td><td>0.5968</td></tr><tr><td>2nd</td><td>Company 11</td><td>0.5621</td><td>Company 20</td><td>0.562</td></tr><tr><td>3rd</td><td>Company 14</td><td>0.5342</td><td>Company 14</td><td>0.5231</td></tr><tr><td>4th</td><td>Company 28</td><td>0.5314</td><td>Company 28</td><td>0.5219</td></tr><tr><td>5th</td><td>Company 50</td><td>0.5176</td><td>Company 35</td><td>0.5028</td></tr><tr><td>6th</td><td>Company 35</td><td>0.5043</td><td>Company 31</td><td>0.4991</td></tr><tr><td>7th</td><td>Company 31</td><td>0.4954</td><td>Company 5</td><td>0.4983</td></tr><tr><td>8th</td><td>Company 1</td><td>0.4942</td><td>Company 49</td><td>0.4855</td></tr><tr><td>9th</td><td>Company 37</td><td>0.4862</td><td>Company 1</td><td>0.4851</td></tr><tr><td>10th</td><td>Company 17</td><td>0.4861</td><td>Company 50</td><td>0.4803</td></tr></table>

![](/api/attachments/DAXEBM8E/fulltext/images/3655d36aac162943b48c31b01175d93da2ffad7886d17cd56e15b9fb1af31adc.jpg)

<table><tr><td colspan="5">Liquidity</td></tr><tr><td>Position</td><td colspan="2">Focal Organisation A</td><td colspan="2">Focal Organisation B</td></tr><tr><td>1st</td><td>Company 27</td><td>0.7778</td><td>Company 27</td><td>0.7931</td></tr><tr><td>2nd</td><td>Company 44</td><td>0.6759</td><td>Company 44</td><td>0.6803</td></tr><tr><td>3rd</td><td>Company 42</td><td>0.6044</td><td>Company 42</td><td>0.6157</td></tr><tr><td>4th</td><td>Company 16</td><td>0.5982</td><td>Company 16</td><td>0.6076</td></tr><tr><td>5th</td><td>Company 9</td><td>0.5975</td><td>Company 9</td><td>0.6065</td></tr><tr><td>6th</td><td>Company 14</td><td>0.5947</td><td>Company 14</td><td>0.603</td></tr><tr><td>7th</td><td>Company 19</td><td>0.5761</td><td>Company 19</td><td>0.5772</td></tr><tr><td>8th</td><td>Company 46</td><td>0.571</td><td>Company 46</td><td>0.5683</td></tr><tr><td>9th</td><td>Company 21</td><td>0.5681</td><td>Company 21</td><td>0.5666</td></tr><tr><td>10th</td><td>Company 15</td><td>0.5651</td><td>Company 47</td><td>0.5629</td></tr></table>

![](/api/attachments/DAXEBM8E/fulltext/images/5aae193ec6ce44eeee87d897e3170eefbd908d6e804faf4655621f923f2cb1bb.jpg)

<table><tr><td colspan="5">Gearing</td></tr><tr><td>Position</td><td colspan="2">Focal Organisation A</td><td colspan="2">Focal Organisation B</td></tr><tr><td>1st</td><td>Company 14</td><td>0.5591</td><td>Company 14</td><td>0.5967</td></tr><tr><td>2nd</td><td>Company 30</td><td>0.5483</td><td>Company 30</td><td>0.5878</td></tr><tr><td>3rd</td><td>Company 38</td><td>0.5451</td><td>Company 10</td><td>0.5857</td></tr><tr><td>4th</td><td>Company 39</td><td>0.5451</td><td>Company 32</td><td>0.5847</td></tr><tr><td>5th</td><td>Company 46</td><td>0.5411</td><td>Company 18</td><td>0.5838</td></tr><tr><td>6th</td><td>Company 35</td><td>0.5391</td><td>Company 38</td><td>0.5836</td></tr><tr><td>7th</td><td>Company 18</td><td>0.5384</td><td>Company 39</td><td>0.5835</td></tr><tr><td>8th</td><td>Company 32</td><td>0.5379</td><td>Company 17</td><td>0.5797</td></tr><tr><td>9th</td><td>Company 10</td><td>0.5369</td><td>Company 46</td><td>0.5781</td></tr><tr><td>10th</td><td>Company 31</td><td>0.5369</td><td>Company 29</td><td>0.5762</td></tr></table>

![](/api/attachments/DAXEBM8E/fulltext/images/d20262299f240fa94c027b59b50cc880a5ca63f9529b664d23e439db420a7622.jpg)

## References

[1] R.E. Bellman, L.A. Zadeh, Decision-making in a fuzzy environment, Management Science 17 (4) (1970) 141– 164.

[2] V. Cherkassky, Fuzzy inference systems: a critical review, in: O. Kayak, et al., (Eds.), Computational Intelligence: Soft Computing and Fuzzy-Neuro Integration with Applications, Springer-Verlag, Germany, 1998, pp. 177–197.

[3] Z. Chi, H. Yan, ID3-derived fuzzy rules and optimized defuzzification for handwritten numeral recognition, IEEE Transactions on Fuzzy Systems 4 (1) (1996) 24– 31.

[4] A. Colyer, Financing as a driver for mergers and acquisitions, Nature Biotechnology 17 (1999) BE13, Supplement.

[5] B.V. Dean, M.J. Schniederjans, A multiple objective selection methodology for strategic industry selection analysis, IEEE Transactions on Engineering Management 38 (1) (1991 February) 53– 62

[6] S. Dreiseitl, L. Ohno-Machado, Logistic regression and artificial neural network classification models: a methodology review, Journal of Biomedical Informatics 35 (5/6) (2002 October) 352– 359.

[7] D. Filev, Fuzzy modelling of complex systems, International Journal of Approximate Reasoning 5 (1991) 281– 290.

[8] B. Harrison, Lean and Mean: The Changing Landscape of Corporate Power in the Age of Flexibility, Basic Books, New York, 1994.

[9] Hill Samuel Bank, Mergers, Acquisitions and Alternative Corporate Strategies, Mercury Books, 1992.

[10] G.D. Holt, P.O. Olomolaiye, F.C. Harris, Applying multiattribute analysis to contractor selection decisions, European Journal of Purchasing and Supply Management 1 (3) (1994) 139– 148.

[11] E.H. Mamdani, S. Assilian, An experiment in linguistic synthesis with a fuzzy logic controller, International Journal of Man–Machine Studies 7 (1) (1975) 1– 13.

[12] C. Marsala, B. Bouchon-Meunier, An adaptable system to construct fuzzy decision trees, Proceedings of NAFIPSV99, New York, USA, 1999 (June), pp. 223 – 227.

[13] M. Murata, O. Ma, H. Isahara, Comparison of three machine– learning methods for Thai part-of-speech tagging, ACM Transactions on Asian Language Information Processing (TALIP) 1 (2) (2002 June) 145– 158.

[14] J.K. Newton, Acquisitions: a directional policy matrix approach, Long Range Planning 14 (6) (1981) 51– 57.

[15] W. Pedrycz, An identification algorithm in fuzzy relational systems, Fuzzy Sets and Systems 13 (1984) 153–167.

[16] W. Pedrycz, Why triangular membership functions? Fuzzy Sets and Systems 64 (1994) 21– 30.

[17] W. Pedrycz, J. Valente de Oliveria, Optimization of fuzzy models, IEEE Transactions on Systems, Man and Cybernetics. Part B. Cybernetics 25 (1996) 627–636.

[18] M.J. Schniederjans, J. Hoffman, Multinational acquisition analysis: a zero-one goal programming model, European Journal of Operational Research 62 (2) (1992) 175– 185.

[19] S.K. Sharma, M.O. Tokhi, Genetic evolution: a dynamic fuzzy approach, Proceedings of FUZZ IEEE 2000, IEEE Interna-

tional Conference on Fuzzy Systems, Texas, USA, vol. 2, 2000 (May), pp. 748 – 752.

[20] M. Sugeno, Industrial Applications of Fuzzy Control, Elsevier, 1985.

[21] M. Sugeno, G.T. Kang, Structure identification of fuzzy model, Fuzzy Sets and Systems 28 (1988) 15 – 33.

[22] M. Sugeno, T. Yasukawa, A fuzzy-logic-based approach to qualitative modelling, IEEE Transactions on Fuzzy Systems 1 (1993) 7 – 31.

[23] T. Takagi, M. Sugeno, Fuzzy identification of systems and its application to modelling and control, IEEE Transactions on Systems, Man and Cybernetics 15 (1985) 116– 132.

[24] R.M. Tong, The evaluation of fuzzy models derived from experimental data, Fuzzy Sets and Systems 4 (1980) 1– 12.

[25] K. Warne, G. Prasad, N.H. Siddique, L. Maguire, A novel intelligent approach to anchorage measurement using electron microscopy, IEEE International Conference on Systems, Man and Cybernetics, Washington, DC, 2003 (October), pp. 3810– 3815.

[26] C. Wei, L. Wang, A note on universal approximation by hierarchical fuzzy systems, Information Sciences 123 (2000) 241– 248.

[27] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338– 353.

[28] L.A. Zadeh, Fuzzy algorithms, Information and Control 12 (1968) 94– 102.

[29] L.A. Zadeh, Outline of a new approach to the analysis of complex systems and decision process, IEEE Transactions on Systems, Man and Cybernetics 3 (1973) 28– 44.

[30] A. Zomava, F. Ercal, S. Olariu, Solutions to Parallel and Distributed Computing Problems, Lessons from Biological Sciences, Book, John Wiley & Sons, 2000 (September).
