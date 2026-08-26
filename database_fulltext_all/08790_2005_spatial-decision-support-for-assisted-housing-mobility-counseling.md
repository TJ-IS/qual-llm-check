---
otero_id: 8790
otero_key: "WQDB638M"
title: "Spatial decision support for assisted housing mobility counseling"
authors: "Michael P. Johnson"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.08.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Spatial decision support for assisted housing mobility counseling

Michael P. Johnson

H. John Heinz III School of Public Policy and Management, Carnegie Mellon University, 5000 Forbes Ave., Pittsburgh, PA 15213-3890, USA

Received 28 May 2003; received in revised form 5 February 2004; accepted 16 August 2004 Available online 25 September 2004

## Abstract

This paper presents a prototype spatial decision support system (SDSS) that enables clients in the Housing Choice Voucher Program to make better decisions about neighborhoods in which to search for housing and specific units to evaluate for occupancy. Application requirements are based on field research establishing limitations of housing counselors to provide detailed assistance to clients, and the capability of clients to use a spatial decision support system. Decision opportunities are identified using value-focused thinking and spatial analysis. Specific destination alternatives are ranked using a destination choice algorithm based on multicriteria decision models that incorporates alternative relocation strategies. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Subsidized housing; Housing mobility; Geographic information systems; Spatial decision support systems

## 1. Introduction

Subsidized housing policy in the United States has undergone a fundamental transformation in the past twenty years. Housing mobility and deconcentration of poverty have supplanted provision of adequate-quality shelter to the most-needy as key missions of American public housing authorities (PHAs) [27]. This paper is an effort to demonstrate the potential contributions of information technology to housing mobility and poverty deconcentration through a prototype spatial decision support system (SDSS).

Poverty deconcentration is a policy goal whereby poor families are more evenly distributed across communities within urbanized areas in such a way as to reduce the incidence of high-poverty neighborhoods, traditionally defined as those communities with poverty rates exceeding 40% [15]. Housing mobility programs, which enable low-income families to relocate from high-poverty areas to more advantaged and less racially segregated communities using tenant-based housing subsidies [36], are one means to this goal; others include inclusive zoning [3], low-income tax credit financing for construction of affordable housing [7], fair housing initiatives to reduce barriers to housing choice among members of certain legally defined <sup>b</sup>protected classes<sup>Q</sup> [44] and federally subsidized redevelopment of high-poverty public housing communities into attractive, mixedincome neighborhoods [31].

The Federal Housing Choice Voucher Program (HCVP, also known as <sup>b</sup>Section 8<sup>Q</sup>) enables lowincome families to select private-market rental housing with the help of rental subsidies. HCVP has surpassed public housing as the most popular single program for provision of subsidized housing in the U.S. [39]. Because HCVP has been shown to enable low-income families to relocate to neighborhoods that are more advantaged than those in which public housing is located [41], and because HCVP is central to the operation of two highly visible and successful housing mobility programs, the Gautreaux Assisted Housing Program in the Chicago metropolitan area [28] and the national Moving to Opportunity for Fair Housing demonstration [18], this paper focuses on decision support for housing mobility programs using HCVP.

Central to the success of HCVP and the housing mobility programs that use it is the role of housing counseling and supportive services that enable clients to navigate the private rental housing market successfully. However, little is known about how housing counseling can help low-income families make better relocation decisions. The main value added of housing counselors in the Gautreaux Program has appeared to be their ability to identify particular candidate rental units [8]. In contrast, housing counseling in the Moving to Opportunity demonstration program has appeared to provide more opportunities for clients to search for rental housing on their own [32,40].

While an extensive literature in the area of household mobility provides models of the processes by which families make relocation and tenure choice decisions [4,33], there is little evidence regarding the relocation decision processes of low-income families and the specific role that tenant-based housing subsidies play in this process.

Finally, in efforts to increase the <sup>b</sup>lease-up<sup>Q</sup> rate of clients, PHAs often focus on landlord recruitment in order to expand the pool of available units for HCVP clients. Current research [42] indicates that, controlling for various factors, quality of landlord outreach efforts is a statistically significant predictor of the success of HCVP clients in securing private-market housing. However, there is little evidence as to the effect of landlord outreach specifically in enabling low-income families to relocate to lower-poverty neighborhoods, nor the relative contributions of landlord outreach and housing counseling towards housing mobility and poverty deconcentration.

In reaction to this <sup>b</sup>black box<sup>Q</sup> of housing search processes, housing counseling and landlord outreach, preliminary research has proposed a decision support system integrating geographic information systems, relational databases and multicriteria decision models to provide specific, structured guidance to HCVP clients for housing search to meet the policy goals of poverty deconcentration via individual choice of neighborhoods and housing units [1,16]. The present paper extends this initial effort by developing a prototype SDSS called the Pittsburgh Housing eCounselor, in reference to the Housing Authority of the City of Pittsburgh (HACP), the PHA that has served as the primary field collaborator for this research effort. This system provides services to three types of end-users: PHA clients, PHA counselors and private-market landlords. This development effort is intended to demonstrate that (a) the system is responsive to the needs of end-users, (b) the system is technically feasible given current technologies and (c) that end-users recognize the system’s potential contributions.

For HCVP clients and counselors, the application provides Web-based information on housing search strategies and real-time access to data on neighborhood characteristics and specific housing units; for landlords, the application provides Web-based administrative information on HCVP and the ability to manage an online portfolio of rental units. In addition, this application enables clients to select neighborhoods with characteristics consistent with their preferences and to rank them according to particular attributes.

This paper makes multiple contributions to research in housing policy and decision support systems. First, the application is based on field research that has established the limitations of housing counselors to provide detailed housing search assistance to clients, and the substantial capability of clients to productively use a spatial decision support system. Second, the application enables users to identify potential destinations that meet multiple criteria using principles of value-focused thinking and spatial analysis. Third, the application introduces a destination choice algorithm based on multicriteria decision models that incorporates alternative relocation strategies and accommodates the desire of PHAs to leverage data on known HCVP housing opportunities. Finally, the application provides a basis for counseling decision support in other housing domains where such methods are not used at present: homeownership, affordable housing and fair housing. The Pittsburgh Housing eCounselor forms the basis for a longer-term project to develop an integrated, professional-quality, fully Web-enabled spatial decision support system that will support a variety of outcome analyses.

The next section of this paper contains assessments of Section 8 program administration, spatial data analysis and results of interviews with HCVP clients and housing counselors that frame this research effort and provide specific guidance in application design. Details are then given of the design of the SDSS. The next section describes the actual implementation of the Pittsburgh Housing eCounselor to date, followed by preliminary user reactions to the prototype application. The final section concludes and identifies research extensions.

## 2. Housing policy and data analysis

This section reviews housing policy research and presents data on subsidized housing in Pittsburgh in order to identify key application design issues.

## 2.1. Housing choice voucher program policy

A study on Section 8 voucher success rates using national data on individual HCVP clients [42] indicates that, controlling for various factors, only tightness of the housing market, landlord outreach, size of tenant briefing sessions and type of voucher (<sup>b</sup>Welfare-to-Work<sup>Q</sup> versus turnover vouchers) are statistically significant in explaining HCVP client success rates. These results reinforce a common perception among HCVP management that landlord outreach is crucial for client success (a <sup>b</sup>supply-side<sup>Q</sup> perspective). On the other hand, since housing markets cross jurisdictional lines, it is not always reasonable to expect that Section 8 clients will limit their search for desirable communities to the jurisdiction of the PHA, which has provided the voucher. A policy of metropolitan area-wide administration of the Section 8 program has been proposed [19] that would enable clients to search for housing across a large region, including areas in which affordable rental housing is available, even if landlords have not made the availability of their units known to PHAs (a <sup>b</sup>demand-side<sup>Q</sup> perspective).

These results provide support for two application design imperatives: first, that the application enable landlords to register available units online and more generally, market the Section 8 program to landlords and, second, that SDSS-based counseling explicitly address restrictions in available rental units along with neighborhood-level attributes while enabling housing search across a metropolitan area.

## 2.2. Spatial distribution of Section 8 housing and neighborhood characteristics

Another way to address the <sup>b</sup>supply-side<sup>Q</sup> versus <sup>b</sup>demand-side<sup>Q</sup> arguments that assisted housing practitioners and researchers confront is to examine data on the distribution of current Section 8 families as compared with the distribution of known Section 8 housing opportunities. Analysis of data for the city of Pittsburgh provided by HACP [13] and Census 2000 tabulations [37] indicates that of the top 10 Pittsburgh neighborhoods by number of active Section 8 clients (about 39% of the total), six also appear on the list of top 10 Pittsburgh neighborhoods by number of available Section 8 units known to HACP (about 50% of the total). As a result, it is likely that current landlord outreach results in vacancies that are concentrated in areas that already contain significant numbers of Section 8 families.

In addition, available Section 8 units known to HACP are disproportionately concentrated in neighborhoods with large black populations. About 71% of all Section 8 clients in the city of Pittsburgh are African–American; about 27% of Pittsburgh’s population is African–American. Tracts that have Section 8 families are about 32% black, whereas tracts that have available Section 8 units are about 50% black. Finally, Pittsburgh data indicate that tracts containing Section 8 units advertised to HACP have an average poverty rate of 25%, as compared to 20% for the city as a whole (and 21% for occupied Section 8 units).

These facts support a hypothesis that an institutional focus on landlord outreach that does not address the significant spatial bias in known Section 8 housing opportunities could push families to disproportionately consider neighborhoods with higher concentrations of African Americans and Section 8 recipients and measures of social disadvantage than for neighborhoods overall.

## 2.3. Interviews with potential users

Interviews with housing specialists at HACP (detailed in Ref. [1]) indicated that these employees see themselves primarily as case managers and not as relocation counselors. Indeed, their high caseloads, substantial administrative responsibility and limited training in housing policy or data analysis reinforce a <sup>b</sup>supply-side<sup>Q</sup> perspective on housing opportunity: they expressed a general belief that a limited supply of affordable units in Pittsburgh required HACP to direct limited resources to landlord recruitment and education. These results indicate that technical training and workflow analysis will be necessary for housing specialists to provide assistance to clients in the use of the housing counseling SDSS, and that a caseload management component will be critical if the SDSS were to be used on a daily basis by housing specialists.

Interviews with current Section 8 voucher holders provide another perspective on application design requirements. Twenty-eight interviews were performed with HACP clients between May and September 2002 based on a stratified random sample of families who, as of May 2002, were either looking for Section 8 housing (<sup>b</sup>searching<sup>Q</sup>), had already found Section 8 housing in the past six months (<sup>b</sup>active<sup>Q</sup>), or were unable to exercise their vouchers within the 90- day limit imposed by HACP (<sup>b</sup>inactive<sup>Q</sup>). Because the focus of our analysis is on the housing search process, <sup>b</sup>active<sup>Q</sup> Section 8 clients were oversampled. Representative descriptive statistics (Table 1) indicate that respondents are older, less likely to have children, more likely to be African–American and less likely to be female than the Section 8 population overall.

In addition, nearly half of respondents had some post-high school education; most respondents were either seeking employment or out of the job market, and nearly half were attempting to relocate, or had relocated, because of dissatisfaction with housing unit quality. Additional analysis indicated that, compared to the overall Section 8 population and the city of Pittsburgh, families in the Section 8 sample lived in higher-poverty neighborhoods (51.16% versus 21.38% and 20.38%, respectively) and neighborhoods that higher concentrations of single-female headed households (33.32% versus 18.86% and 8.95%, respectively), but neighborhoods with somewhat lower concentrations of African–American families (24.63% versus 32.17% and 26.76%, respectively).

Table 1  
HACP Section 8 client interview results—descriptive statistics

<table><tr><td rowspan="2">Respondent attributes</td><td colspan="2">Sample</td><td colspan="2">All S8</td></tr><tr><td>Number</td><td>Percent</td><td>Number</td><td>Percent</td></tr><tr><td colspan="5">Program status</td></tr><tr><td>Active</td><td>8</td><td>28.57</td><td>2540</td><td>85.93</td></tr><tr><td>Searching</td><td>19</td><td>67.86</td><td>404</td><td>13.67</td></tr><tr><td>Inactive</td><td>1</td><td>3.57</td><td>12</td><td>0.41</td></tr><tr><td colspan="5">Race/ethnicity</td></tr><tr><td>White</td><td>3</td><td>10.71</td><td>767</td><td>25.95</td></tr><tr><td>Black</td><td>25</td><td>89.29</td><td>2163</td><td>73.17</td></tr><tr><td>Other</td><td>0</td><td>0.00</td><td>26</td><td>0.88</td></tr><tr><td colspan="5">Gender</td></tr><tr><td>Male</td><td>8</td><td>28.57</td><td>413</td><td>13.99</td></tr><tr><td>Female</td><td>20</td><td>71.43</td><td>2540</td><td>86.01</td></tr><tr><td colspan="5">Household composition</td></tr><tr><td>Without children</td><td>16</td><td>57.14</td><td>910</td><td>30.78</td></tr><tr><td>With children</td><td>12</td><td>42.86</td><td>2046</td><td>69.22</td></tr><tr><td colspan="5">Age</td></tr><tr><td>18–24</td><td>1</td><td>3.57</td><td>502</td><td>16.98</td></tr><tr><td>25–29</td><td>2</td><td>7.14</td><td>403</td><td>13.63</td></tr><tr><td>30–34</td><td>1</td><td>3.57</td><td>391</td><td>13.23</td></tr><tr><td>35–44</td><td>8</td><td>28.57</td><td>734</td><td>24.83</td></tr><tr><td>45–49</td><td>4</td><td>14.29</td><td>253</td><td>8.56</td></tr><tr><td>50–64</td><td>10</td><td>35.71</td><td>410</td><td>13.87</td></tr><tr><td>&gt;65</td><td>2</td><td>7.14</td><td>263</td><td>8.90</td></tr><tr><td>Total all types</td><td>28</td><td>100.00</td><td>2956</td><td>100.00</td></tr></table>

Source: interviews by author.

A portion of the interview consisted of eliciting strength-of-preference responses for a variety of neighborhood- and housing unit-level characteristics, both for the origin neighborhood and housing unit, and, if the respondent had successfully relocated using a Section 8 voucher, the destination neighborhood and housing unit. In addition, interviews elicited preferences for characteristics of an <sup>b</sup>ideal<sup>Q</sup> neighborhood and housing unit. Results indicated, generally, that families had well-defined preferences that varied depending on their search status and household composition.

For example, Fig. 1 indicates that 19 respondents who are currently searching for Section 8 housing (labeled <sup>b</sup>current: searching<sup>Q</sup>) feel less strongly about the importance of characteristics such as local amenities, transportation, cost of living, health services and environmental status of neighborhoods in which they currently live than do 9 respondents (<sup>b</sup>searching<sup>Q</sup>, <sup>b</sup>active<sup>Q</sup> and <sup>b</sup>inactive<sup>Q</sup>; labeled <sup>b</sup>ideal: searching<sup>Q</sup>) who considered an <sup>b</sup>ideal<sup>Q</sup> neighborhood. Eight respondents who have successfully completed the search process (labeled <sup>b</sup>current: active<sup>Q</sup>) have stronger preferences regarding cultural amenities of the neighborhoods they have actually chosen, and weaker preferences regarding local work and employment opportunities than those in the two other groups.

Analysis of open-ended responses indicated that respondents reported difficulty finding good-quality housing in acceptable neighborhoods and were generally dissatisfied with the quality and quantity of housing search assistance provided by HACP. In particular, respondents were familiar with lists of available Section 8 housing units made available online by the HACP and criticized these lists for being incomplete, misleading or out of date. In addition, respondents were roughly evenly split between those that used neighborhood characteristics as the primary tool for initiating a housing search (e.g., seeking lowcrime neighborhoods) and those that relied on knowledge of housing unit characteristics (e.g., seeking housing units that met their specific shelter needs).

A substantial portion of the survey focused on familiarity with information technology and skills in tabular and spatial data analysis. Sixty-four percent of interview participants considered themselves <sup>b</sup>computer literate<sup>Q</sup>, the same percentage had Internet access, either at work, home or a public facility, and 82% felt that an information system could help them use their Section 8 vouchers more effectively.

Interview participants were asked to analyze a map of the city of Pittsburgh color-coded by crime rates at the neighborhood level and did so without substantial difficulty: most participants successfully identified: highest-crime neighborhoods (71.43%), lowest-crime neighborhoods (67.86%) and the neighborhood closest to the one in which they currently lived (64.29%). However, only 39.29% of participants were able to correctly estimate the crime rate of the neighborhood in which they lived.

Finally, interview participants were asked to analyze tabular data representing attributes associated with a hypothetical set of neighborhoods and again did so without substantial difficulty: most participants were able to successfully identify neighborhoods that performed best on individual attributes such as transit (60.71%) and education quality (82.14%), and to identify neighborhoods that were most-preferred (78.57%) and least-preferred (89.29%) according to attribute values.

![](/api/attachments/WQDB638M/fulltext/images/f8886b1068c5a2e6a96f8ce93d6a5473fea8e0db9f0e048b5e7eb02c30a6884b.jpg)  
Fig. 1. Strength of preference for neighborhood characteristics as a function of search status.

These Section 8 client results indicate that clients do not appear to be <sup>b</sup>anchored<sup>Q</sup> to the notion of restricting their search to neighborhoods with which they are already aware, or framing their search only in terms of housing units known to be available via the PHA. Second, clients desire more personalized, intensive housing counseling than is generally currently available from the local PHA. Third, respondents have clearly defined yet variegated preferences for neighborhood and housing unit attributes that could be used in a multicriteria decision model for ranking destination alternatives. Finally, and most importantly, respondents appear to have the cognitive skills to make productive use of tabular and spatial data of the kind that would be contained in a spatial decision support system.

The results in this section strongly support the vision of a spatial decision support system whose primary goal is increased capability of clients to make detailed, affirmative choices regarding housing alternatives. In addition, these results support secondary goals of increased participation in HCVP by landlords and increased quality of counseling support provided by housing specialists. This vision may be summarized as one aimed at developing a SDSS that is client-focused, counselor-facilitated and landlord-supported.

## 3. Application design

This section provides details on the Pittsburgh Housing eCounselor’s high-level functionality, as well as design choices application components: website, relational database, spatial database and housing search algorithm. A comprehensive presentation of application functionality is contained in Ref. [17].

## 3.1. High-level functionality

The Pittsburgh Housing eCounselor is intended to be a Web-enabled spatial decision support system for housing provision and search under the Housing Choice Voucher Program. As such, it appeals to three distinct user groups: Section 8 clients, who seek clear, well-structured guidance on searching for neighborhoods and housing units that meet their needs; housing authority housing specialists, who provide assistance to clients in their search, as well as manage a collection of client cases, and landlords, who wish to make information on vacant rental units available to the widest possible audience of potential renters.

A schematic description of the application architecture, based on standard design principles [35], is contained in Fig. 2, below.

Research in another domain of DSS pursued by this author, generation of practice reminders for primary care physicians, has made clear that the relational database and presentation system components of a DSS must include caseload management components to ensure that the application can be fully integrated into the organization’s daily workflow [45]. Though the current version of the eCounselor does not include such functionality, work to do so is ongoing, based on development of a Web-based caseload management application for another housing counseling client [5].

![](/api/attachments/WQDB638M/fulltext/images/b207379cbc6fb2e39360d1b7eebb33e5c3cb1b311cb91e688da7e3b2f6a4dd44.jpg)  
Fig. 2. High-level architecture.

## 3.2. Website

As argued in Ref. [16], an SDSS for assisted housing counseling should be entirely Web-enabled for ease of application distribution and access. To gain insight into relevant practice of Web-based assisted housing counseling, we examined two service models: apartmentsinpittsburgh.net, developed by the Housing Authority of the City of Pittsburgh [12], and HousingConnections.org, developed by the City of Portland Department of Housing and Community Development [6]. The HACP website provides current listings of assisted housing units in HACP’s inventory, including available Section 8 rental units. The site also allows landlords to register their own housing units. The data on this website is static: users cannot sort or filter the lists of housing according to their own needs, nor can users manage, in real time, a portfolio of housing units. The City of Portland site has a more sophisticated design that enables users to search housing units by a variety of criteria. However, the site does not enable users to learn about neighborhood characteristics before searching for specific housing units.

The Pittsburgh Housing eCounselor is designed to use both static data and dynamic data. Examples of client-focused static data are administrative information about the Housing Choice Voucher Program, tips on identifying selecting appropriate neighborhoods in which to search for specific housing units and tips on evaluating specific housing units according to characteristics such as kitchens, bedrooms and safety considerations.

Dynamic client-focused data include a search engine for available rental units and a wide variety of spatial data that may be examined at different levels. These data are used in the housing destination search algorithm, which allows users to identify housing opportunities by exploring characteristics of neighborhoods, or, alternatively by exploring characteristics of rental units registered by landlords with the PHA.

Examples of landlord-focused static data are administrative information about HCVP especially relevant to landlords, and a direct appeal for landlord participation in HCVP based on business benefits and links to online resources for provision and management of affordable housing. Dynamic landlordfocused data include landlord registration and online property portfolio management.

## 3.3. Relational database

Data stored in the eCounselor’s relational database are of three types: case-related data, property-related data and neighborhood-related data.

Case-related data include data on housing specialists, the cases they manage, and the families associated with each case. Property-related data include data on landlords, and buildings and individual units that are marketed to and occupied by Section 8 clients. Neighborhood-related data include data on small, well-defined components of the service area of the housing authority called <sup>b</sup>neighborhoods<sup>Q</sup> that are assumed to consist of Census tracts which contain a variety of <sup>b</sup>amenities<sup>Q</sup> such as schools, stores and cultural resources.

## 3.4. Spatial data

Two classes of spatial data are used in the application are referred to here as aggregate data, at the level of spatial units such as Census tracts, city neighborhoods, Zip codes and so on, and amenity data, at the level of <sup>b</sup>point<sup>Q</sup>- or <sup>b</sup>line<sup>Q</sup>-type spatial units. This discussion is based on the framework of data needs for housing relocation counseling developed in Ref. [16].

Aggregate data are intended to provide users with insight into characteristics that distinguish neighborhoods, Census tracts or other relevant spatial units from each other. This information, in turn, enables users to identify acceptable neighborhoods through thresholds associated with specific neighborhood characteristics. Examples of aggregate data include: total number of vacant housing units, crime rate, fair housing complaints and education quality.

Amenity data provide information on specific neighborhood characteristics, for example the location of churches, day care centers, hospitals and property parcels within a given community. Knowledge of amenity data might enable a user to decide whether a neighborhood that appears desirable in terms of aggregate characteristics remains desirable when the physical configuration of local amenities, such as streets, property parcels, mass transit lines, recreation centers and so on, are visible.

## 3.5. Housing search algorithm

The specific means by which a Housing Choice Voucher Program client receives housing search guidance—the housing or destination search algorithm—is at the core of the Pittsburgh Housing eCounselor. This process consists of two steps: values clarification and identification/ ranking of housing search alternatives.

The values clarification step is inspired by valuefocused thinking methodology [20] and follows a discussion of the application of this methodology to housing search [16]. An interactive discussion regarding the client’s values in the housing search process can be motivated by open-ended questions from the housing specialist, e.g., <sup>b</sup>What are you looking for in a new neighborhood?<sup>Q</sup> or <sup>b</sup>What kind of housing unit is important to you?<sup>Q</sup> Such a discussion enables the client and the housing specialist to identify means objectives, i.e., the goals that can be measured using the type of data presented in the <sup>b</sup>spatial data<sup>Q</sup> subsection above, and contrast these with ends objectives, i.e., fundamental goals that may or may not correspond to particular data elements.

Moreover, identifying means and ends objectives can be facilitated by browsing available spatial data. So, for example, if a client asserts that the quality of education received by her young children is very important to her, upon browsing available data regarding education quality across suburban school districts or city neighborhoods, she may conclude that certain city neighborhoods or suburban school districts are more desirable along this dimension than others.

Identification and ranking of housing search alternatives is based on the notion, developed in the previous section, that some families are most comfortable framing their housing search process in terms of neighborhoods that meet their needs, while other families are most comfortable choosing between alternative housing units, with less concern for neighborhoods in which the units are located. Fig. 3 presents a schematic description of the destination search algorithm.

![](/api/attachments/WQDB638M/fulltext/images/06f0fa75a9f1b9e486f92403ea676dd9f0ba949df81238612ebde9ef777935f7.jpg)  
Fig. 3. Destination search algorithm.

This algorithm assumes that alternatives—neighborhoods or housing units—can be selected through value focused thinking and queries of relevant databases. These alternatives could, if the user desires, be ranked using multicriteria decision models. At this point, if the user has focused initially on neighborhoods, she may wish to incorporate data on available rental units known to the housing authority in order to select those available housing units in only neighborhoods previously deemed desirable. Alternatively, if the user has initially focused on housing units, she may wish to incorporate data on neighborhoods in order to restrict her search to housing units in desirable neighborhoods. In either case, the user may then rank housing units in desirable neighborhoods according to housing unit-level attributes, as well as a measure of neighborhood desirability derived from an MCDM. At various points in this algorithm, the user may choose to print current results and end the process or continue.

## 3.6. Alternatives ranking

There is a wide variety of multicriteria decision models from which to choose one or more for the alternatives ranking phase of the housing search algorithm. Based on Section 8 housing specialist interview results in the previous section, staff in typical PHAs are not likely to have much time to train themselves on the application or guide clients. However, Section 8 client interview results in the previous section provided support for the notion that clients have the capacity to analyze spatial data and rank alternatives relatively accurately and quickly. Therefore, it seems reasonable to propose two types of MCDMs for use in ranking destination alternatives: a <sup>b</sup>simple<sup>Q</sup> MCDM that can be used quickly by all, but at a potential cost of accuracy in translating user preferences to alternative rankings, and an <sup>b</sup>advanced<sup>Q</sup> MCDM that might require somewhat more time to use but generate rankings more consistent with user preferences (see Ref. [1] for details regarding the two-track MCDM design and detailed justification for the choice of specific MCDMs).

We propose <sup>b</sup>elimination by aspects<sup>Q</sup> (simple ranking) [35] as the <sup>b</sup>simple<sup>Q</sup> MCDM and the PROMETHEE outranking method [2] as the <sup>b</sup>advanced<sup>Q</sup> MCDM. The choice of elimination by aspects is straightforward: it is simple to use and consistent with most people’s understanding of alternatives ranking, i.e., <sup>b</sup>breaking ties<sup>Q</sup>. Of course, the inability of this method to allow any tradeoffs between attributes makes it less useful for users who may weight two or more alternatives reasonably closely. The choice of the advanced MCDM is based on an examination in Ref. [1] of four advanced MCDMs: multi-attribute utility theory [43], Analytic Hierarchy Process [30], PROMETHEE and ELECTRE [29]. We concluded that commercially available implementations of MAUT and AHP are much more difficult to use than PROMETHEE (and somewhat more difficult to use than ELECTRE), and that results of MAUT are likely to be less consistent with users’ underlying preferences than those of AHP, ELECTRE and PROMETHEE. As a result, PROMETHEE is proposed here as a best-compromise solution for <sup>b</sup>advanced<sup>Q</sup> MCDM in the destination search algorithm of the eCounselor. Details of the PROMETHEE algorithm are contained in Ref.

Table 2  
Application spatial data sources and descriptions

<table><tr><td>Type</td><td>Description</td><td>Source</td></tr><tr><td>Aggregate</td><td>Fair housing complaints, by Zip code, city of Pittsburgh neighborhood and suburban Allegheny County municipalityType I and type II crime rates by city of Pittsburgh neighborhood and suburban Allegheny County municipalityCensus 2000 demographic data by city of Pittsburgh neighborhood and suburban Allegheny County municipality:Race/ethnicityPovertyPopulationRental, owner-occupied and vacant housingEstablishment counts by sector and Zip codeEducational outcomes, Pennsylvania SSA, by grade, subject, city of Pittsburgh neighborhood and suburban Allegheny County municipality</td><td>Analysis of impediments to fair housing, Pittsburgh [22] and suburban Allegheny County [21]The Pittsburgh Post-Gazette [24,25], Pennsylvania Uniform Crime Reporting System [23]U.S. Census Bureau [37]</td></tr><tr><td>Amenity</td><td>Current and vacant Section 8 unitsChurchesParksDay care centersTransit accessibility regionsRoads and mass transit routes</td><td>U.S. Census Bureau [38]Education Policy Issues Center [9]Housing Authority of the City of Pittsburgh [13] Pittsburgh Foundation&#x27;s Getting to Work Project [34]Port Authority of Allegheny County [26]</td></tr></table>

[2]. Field research to validate these judgments is ongoing.

The consideration of multiple aspects of design of a spatial decision support system for housing search has then led us to propose an information technology application that:

<sup>!</sup> Targets Section 8 clients, housing specialists and landlords;

<sup>!</sup> Is Web-based;

<sup>!</sup> Integrates spatial and relational data;

<sup>!</sup> Incorporates a destination search algorithm that addresses alternative client search strategies and alternative client preferences for MCDMs to rank alternatives; and

<sup>!</sup> Uses a particular <sup>b</sup>advanced<sup>Q</sup> MCDM, PROME-THEE, which may be easier to use effectively in real time than competing MCDMs.

![](/api/attachments/WQDB638M/fulltext/images/0cb52a98924bc0868962b0854f6a2e8f6815599f43f1f97a9d8b504037c91541.jpg)  
Map:1355703,33,37811291-Image:525,420-ScaleFactor.284.5446356682714 Source: Pittsburgh Housing eCounselor, http://www.housing-ecounselor.org

Fig. 4. Search Pittsburgh neighborhoods—fair housing complaints.

## 4. Implementation of the Pittsburgh Housing eCounselor

This section discusses implementation of a spatial decision support system based on the design presented in the previous section: sources for spatial data, development platforms and a description of the final application.

## 4.1. Data sources

This SDSS requires a substantial volume of data to provide guidance to clients and to enable landlords to view and modify their portfolios of rental units available for consideration by Section 8 clients. Ref. [16] identifies a large set of objective community indicators that enable community residents to evaluate the health and quality of their neighborhoods. These data, listed in Table 2, represent a subset of that list that were feasible to include in the current application, and include fair housing, subsidized housing, neighborhood amenities, transportation, employment, education and a wide variety of Census-defined demographic characteristics.

Aggregate data are displayed using standard boundary files for Census tracts, Zip codes, city of Pittsburgh neighborhoods, and suburban Allegheny County municipalities and school districts [9,14,37]. A complete list of spatial data tables and details on the spatial data at the Census tract, Pittsburgh neighborhood/suburban Allegheny County municipality and Pittsburgh neighborhood/suburban Allegheny County school district is contained in the appendix to Ref. [17].

## 4.2. Development platforms and implementation

Limited resources have reduced the scope of the Pittsburgh Housing eCounselor to a prototype

![](/api/attachments/WQDB638M/fulltext/images/7ffe447a0460cc70cde868d77719bffc995abab30a7024ca134e865e8b9f5d81.jpg)  
Source: Pittsburgh Housing eCounselor, http://www.housing-ecounselor.org

Fig. 5. Search Pittsburgh neighborhoods—property parcels, east liberty neighborhood of Pittsburgh.

consisting of two components: a website, http:// www.housing-ecounselor.org, and a PC-based application. The website contains all client- and landlordside static data, landlord-side dynamic data and the following client-side dynamic data components: a GIS-enabled browser to view the spatial dataset and real-time database connectivity to a sample dataset of available Section 8 rentals. Static data are developed using HTML and JavaScript. Relational database connectivity is implemented using Microsoft Active Server Pages and JavaScript to manage connections with a Microsoft Access 2002 database. Spatial data display is implemented with ArcIMS 4.0 [11].

Figs. 4 and 5 present regional and local views of the spatial dataset. The former view might assist a client in choosing particular neighborhoods for consideration as part of the housing search process; the latter view might assist a client in determining if a particular neighborhood’s local amenities meet the client’s preferences.

Fig. 6 presents functionality that allows a client to choose from among the complete set of available Section 8 units known to the housing authority that subset which meets the client’s personal criteria.

The eCounselor also allows a landlord or property owner to manage a portfolio of rental units online: registering new rental units, viewing the complete portfolio of currently vacant housing units, displaying detailed housing unit attributes for one of the landlord’s vacant rental units, modifying attributes of currently vacant units or removing a just-rented unit from the online portfolio.

The PC-based application is composed of two parts. The first, developed using ArcView 3.2 and the

![](/api/attachments/WQDB638M/fulltext/images/bcb5c410a7688973fd16af948a9b09d055d718e8d325c80c1402f2d0bc2e6404.jpg)  
Source: Pittsburgh Housing eCounselor, http://www.housing-ecounselor.org

Fig. 6. Search registered housing units.

Avenue scripting language [10], enables users to select neighborhoods in Allegheny County according to criteria defined at a variety of spatial levels (Zip code, Census tract, Pittsburgh neighborhood/suburban Allegheny County municipality and Pittsburgh neighborhood/suburban Allegheny County school district). The second part of the application features an implementation, using Java and HTML, of the PROMETHEE algorithm and of a simple sort routine. Thus, we have implemented a portion of the <sup>b</sup>neighborhood-first<sup>Q</sup> portion of the destination search algorithm presented in Fig. 3 represented by the first two function boxes.

Fig. 7 shows how a user might select neighborhoods and municipalities according to a single criterion: the percentage of students in each neighborhood or school district scoring in the top quartile of the 8th grade Pennsylvania System of School Assessment Math exam is at least 40%.

The dialog box at the center of the figure containing the range of values for this district-level attribute indicates that this is a stringent criterion.

Fig. 8 shows how a subset of four suburban municipalities that meet this requirement might be ranked according to the <sup>b</sup>advanced<sup>Q</sup> PROMETHEE MCDM by five fixed criteria: total number of Section 8 units, crime rate, percent of population that is black, number of vacant units and total number of fair housing complaints. Efforts to enable selected neighborhoods to be ranked by the same criteria by which they were selected, even if the selection at one spatial level, e.g., Zip code, results in a municipality having two or more distinct values, are ongoing.

The user is prompted first for the direction of preference for each attribute, and then to select between two <sup>b</sup>strength of preference<sup>Q</sup> functions: the <sup>b</sup>type II<sup>Q</sup> (<sup>b</sup>U-shaped<sup>Q</sup>) and <sup>b</sup>type III<sup>Q</sup> (<sup>b</sup>V-shaped<sup>Q</sup>) functions (see Ref. [2]). For the preference function

![](/api/attachments/WQDB638M/fulltext/images/9a9b3df96938aad73208060f2dbf3f5205b7209dcd8a70f4f94615f40519607c.jpg)  
Source: Pittsburgh Housing eCounselor, Desktop ArcView 3.2/Avenue application

Fig. 7. Select acceptable neighborhoods—minimum education quality threshold.

M.P. Johnson / Decision Support Systems 41 (2005) 296–312  
![](/api/attachments/WQDB638M/fulltext/images/b93e0287f9ecadef4c2190b77fc64e98a38b1bd11829ab3b80f09d954dd011bd.jpg)  
Source: Pittsburgh Housing eCounselor, Desktop Java/HTML application  
Fig. 8. Rank neighborhoods using PROMETHEE.

chosen, the user is asked for a single parameter representing the extent of indifference modeled by the function. Implementation of all six strength of preference functions is a subject of ongoing development.

At this point, we have achieved only a partial implementation of the Pittsburgh Housing eCounselor. Development of a fully-integrated version, including the full destination search algorithm is ongoing.

## 5. Evaluation of the Pittsburgh Housing eCounselor

The Pittsburgh Housing eCounselor has been presented to managers in the Housing Authority of the City of Pittsburgh’s Section 8 program and to Section 8 housing specialists. Section 8 managers see the SDSS as consistent with their PHA’s goals of maximizing lease-up rate, maximizing landlord satisfaction, minimizing neighborhood opposition and maximizing beneficial client outcomes. They view the eCounselor as a means to secure competitive advantage for their organization. In addition, they believe that the eCounselor could be installed in kiosks near the Section 8 offices, enabling clients to familiarize themselves with program requirements and regional data, thus making their limited time with housing specialists more productive.

HACP Section 8 housing specialists are more skeptical of the potential of the eCounselor to add value to their work, however. While agreeing that clients would likely benefit from an application such as the eCounselor, housing specialists are concerned about adding software training to their already high caseloads, and believe that a case management system would be of more immediate use to them. In addition, housing specialists are concerned that clients might use the tool inappropriately, e.g., to choose destination communities that may be desirable along a number of dimensions yet lack affordable rental housing, increasing the risk of unsuccessful searches. Housing specialists were also concerned that clients might use the eCounselor to leave the city of Pittsburgh for the suburbs (a jurisdictional concern that appears irrelevant to family outcomes). The housing specialists agree that if some measure of housing availability were included in every neighborhood selection/ranking process, and if there were a way to visualize tradeoffs between alternatives on the basis of varying bundles of attributes, clients might indeed have increased information with which to make relocation decisions.

Section 8 managers and housing specialists are supportive of another evaluation mechanism, a scripted counseling session between clients and housing specialists mediated by the eCounselor. Work on this evaluation scheme is ongoing.

## 6. Conclusion and next steps

The Pittsburgh Housing eCounselor is a prototype spatial decision support system to assist families receiving housing assistance under the Housing Choice Voucher Program to choose neighborhoods and housing units that best suit their preferences and which provide the greatest likelihood of beneficial outcomes. The eCounselor also enables landlords to manage, online, portfolios of available rental units of interest to HCVP clients. The prototype application presented in this paper is a first step towards a fully integrated, professional-quality Web-enabled SDSS that will provide value to clients, housing specialists and landlords, and which will enable a comprehensive and rigorous outcomes evaluation of IT-assisted housing counseling.

The Pittsburgh Housing eCounselor is based on social science results in household mobility, housing mobility programs and fair housing. The application’s functional requirements are based on field research with public housing authority housing specialists and assisted housing clients. The eCounselor represents an advance in housing counseling practice and in the integration of information technology and management science into publicsector service delivery. Initial reactions to the application from staff of the client organization are encouraging and more evaluations of the prototype are under consideration.

However, a substantial amount of research and development is necessary in order for the eCounselor to be used on an evaluation basis by housing specialists. Additional field research must provide insight into: categories of data that are of greatest importance to assisted housing clients; specific measures for data elements that convey the greatest meaning to clients; alternative MCDMs that enable users to rank alternatives quickly and effectively, and an interface design that is consistent with the needs and expectations of users. The eCounselor, if redeveloped into a professional-quality application, will provide the means for outcomes evaluation addressing user satisfaction, client location choices and family outcomes.

## Acknowledgements

This work was funded by the U.S. Department of Housing and Urban Development Urban Scholars Postdoctoral Fellowship. Thanks to the following collaborators: Systems Synthesis project team (Miroslava Angelova, Iris Bond, Arthdale Brown, Irina Guretskaya, Xiaoyan Li, Imran Moin, Russell O’Lare, Dan Silitonga, Hsin-Yi Teng and Nicole Williams), Heinz School research assistants (Olutayo Fabusuyi, Min Huo, Lei Lai, David Poku, Clara Pratte and Refeng Wu) and the Housing Authority of the City of Pittsburgh (Chris Shea, Mark Patterson, Robert Zak, Kevin Bartko, Markas Adams, Barbara Brown, Shannon Copeland, Chris Linderman and Pam Norr). Special thanks to Marjorie Austin Turner and Wilpen Gorr for guidance during my HUD Urban Scholars Postdoctoral Fellowship.

## References

[1] M. Angelova, I. Bond, A. Brown, I. Guretskaya, X. Li, I. Moin, R. O’Lare, D. Silitonga, H.-Y. Teng, N. Williams, M.P. Johnson, Low-income housing search assistance on the Web: the Pittsburgh Housing eCounselor, Systems Synthesis final report, Carnegie Mellon University, H. John Heinz III School of Public Policy and Management (2002 May).

[2] J.P. Brans, P. Vincke, A preference ranking organisation method (The PROMETHEE Method for Multiple Criteria Decision Making), Management Science 31 (6) (1985 June) 647– 656.

[3] K.D. Brown, Expanding Affordable Housing Through Inclusionary Zoning: Lessons from the Washington Metropolitan Area, The Brookings Institution, Center on Urban and Metropolitan Policy, Washington, D.C., 2001.

[4] M. Cadwallader, Migration and Residential Mobility, The University of Wisconsin Press, Madison, WI, 1992.

[5] C.W. Choe, K. Kalloo, M. Klug, K. Mason, Y. Sugita, M.P. Johnson, Client counseling tracking system-CCTS, Information Systems Project final report, Carnegie Mellon University, H. John Heinz III School of Public Policy and Management (2003 Aug.).

[6] City of Portland Department of Housing and Community Development, HousingConnections.org, World Wide Web page <sup>b</sup>http://www.housingconnections.org/<sup>N</sup>, accessed July 22, 2002 (2002).

[7] J.L. Cummings, D. DiPasquale, The low-income housing tax credit: an analysis of the first ten years, Housing Policy Debate 10 (2) (1999) 251– 308.

[8] S. DeLuca, J.E. Rosenbaum, If Low Income Blacks are Given a Chance to Live in White Suburbs, Will They Stay? Testing Mobility Patterns with Quasi-Experimental Data, Northwestern University, Evanston, Ill, 2002 May.

[9] Education Policy & Issues Center, Dataset of Student Achievement on the Pennsylvania System of School Assessment, Pittsburgh, 2000.

[10] Environmental Sciences Research Institute, ArcView Version 3.2, Redlands, Calif. (2001).

[11] Environmental Sciences Research Institute. ArcIMS Version 4.0, Redlands, Calif. (2002).

[12] Housing Authority of the City of Pittsburgh, ApartmentsInPittsburgh.net, World Wide Web page <sup>b</sup>http://www. apartmentsinpittsburgh.net/<sup>N</sup>, accessed July 22, 2002. (2002).

[13] Housing Authority of the City of Pittsburgh, Dataset of Section 8 Units, 2002.

[14] Housing Authority of the City of Pittsburgh, Dataset of Pittsburgh shapefiles, 2002.

[15] P.A. Jargowsky, Poverty and Place: Ghettos, Barrios and the American City, Russell Sage Foundation, New York, 1997.

[16] M.P. Johnson, Decision support for family relocation decisions under the section 8 housing assistance program using GIS and the analytic hierarchy process, Journal of Housing Research 12 (2) (2001) 277– 306.

[17] M.P. Johnson, The Pittsburgh Housing eCounselor: Using Information Technology and Management Science to Help Housing Choice Voucher Program Participants Choose Better Homes and Communities, Heinz School Working Paper 2002- 41 (2002 Dec.).

[18] M.P. Johnson, H.F. Ladd, J. Ludwig, The benefits and costs of residential-mobility programs for the poor, Housing Studies 17 (1) (2002 Jan.) 125– 138.

[19] B.J. Katz, M.A. Turner, Who should run the housing voucher program? A Reform Proposal, Housing Policy Debate 12 (2) (2001) 239–262.

[20] R.L. Keeney, Value-Focused Thinking: A Path to Creative Decision Making, Harvard University Press, Cambridge, MA, 1992.

[21] C.A. Martin, M.P. Johnson, Analysis of Impediments to Fair Housing Choice in Allegheny County, Pennsylvania: Excluding the City of Pittsburgh, the City of McKeesport, and the Municipality of Penn Hills, The Allegheny County Department of Economic Development, The Fair Housing Partnership of Greater Pittsburgh (1999 Dec.).

[22] C.A. Martin, M.P. Johnson, A. Williams Foster, Analysis of impediments to fair housing choice in the city of Pittsburgh, Pennsylvania, The City of Pittsburgh Department of City Planning (2000 Oct.).

[23] Pennsylvania Uniform Crime Reporting System, PA UCR Reports, World Wide Web page <sup>b</sup>http://ucrreport.psp.state. pa.us/UCR/Reporting/RptMain.asp<sup>N</sup>, accessed December 17, 2002 (2002).

[24] Pittsburgh Post-Gazette, Neighborhoods: Reported Part 1 Crimes per 100, World Wide Web page <sup>b</sup>http://www. post-gazette.com/neigh<sup>\_</sup>city/20020224citypart1stat9p9.asp<sup>N</sup>, accessed May 28, 2003 (February 24, 2002).

[25] Pittsburgh Post-Gazette, Neighborhoods: Reported Part 2 Crimes per 100, World Wide Web page <sup>b</sup>http://www.postgazette.com/neigh<sup>\_</sup>city/20020224citypart2stat9p9.asp<sup>N</sup>, accessed May 28, 2003 (February 24, 2002).

[26] Port Authority of Allegheny County, Dataset of mass transit routes in Allegheny County (2002).

[27] R.G. Quercia, G.C. Galster, The challenges facing public housing authorities in a brave new world, Housing Policy Debate 8 (3) (1997) 535– 569.

[28] J.E. Rosenbaum, Changing the geography of opportunity by expanding residential choice: lessons from the Gautreaux Program, Housing Policy Debate 6 (1) (1995) 231 – 267.

[29] B. Roy, The Outranking Approach and the Foundations of ELECTRE Methods, Theory and Decision 31 (1991 July) 49 – 73.

[30] T.L. Saaty, How to make a decision: the analytic hierarchy process, European Journal of Operational Research 48 (1) (1990 Sept.) 9 –26.

[31] J.J. Salama, The redevelopment of distressed public housing: early results from HOPE VI projects in Atlanta, Chicago, and San Antonio, Housing Policy Debate 10 (1) (1999) 95 – 142.

[32] M. Schroder, Locational constraint, housing counseling, and successful lease-up in a randomized housing voucher experiment, Journal of Urban Economics 51 (2) (2002 Mar.) 315– 338.

[33] A. Speare Jr., S. Goldstein, W.H. Frey, Residential Mobility, Migration and Metropolitan Change, Ballinger, Cambridge, MA, 1975.

[34] The Pittsburgh Foundation, Getting to Work: A GIS Transportation Project for Allegheny County [CD-ROM] (1999).

[35] E. Turban, J.E. Aronson, Decision Support Systems and Intelligent Systems, Sixth ed., Prentice Hall, Upper Saddle River, N.J., 2001.

[36] M.A. Turner, Moving out of poverty: expanding mobility and choice through tenant-based housing assistance, Housing Policy Debate 9 (2) (1998) 373– 394.

[37] U.S. Census Bureau, 2000 Census Tracts: Cartographic Boundary Files, Washington, D.C., World Wide Web page <sup>b</sup>http://www.census.gov/geo/www/cob/tr2000.html<sup>N</sup>, accessed May 28, 2003 (2001).

[38] U.S. Census Bureau, Economic Census-1997, Washington, D.C., World Wide Web page <sup>b</sup>http://www.census.gov/epcd www/econ97.html<sup>N</sup>, accessed May 28, 2003 (2003).

[39] U.S. Department of Housing and Urban Development, Office of Policy Development and Research, A Picture of Subsidized Households-1998, Washington, D.C., World Wide Web page <sup>b</sup>http://www.huduser.org/datasets/assthsg/statedata98/index. html<sup>N</sup>, accessed May 28, 2003 (1998).

[40] U.S. Department of Housing and Urban Development, Office of Policy Development and Research, Moving to Opportunity for Fair Housing Demonstration Program: Current Status and Initial Findings (Washington, D.C., 1999).

[41] U.S. Department of Housing and Urban Development, Office of Policy Development and Research, Voucher Recipients Enjoy Much Greater Choice About Where to Live than Residents of Public Housing and Are Less Likely to be Concentrated in Distressed Neighborhoods, Issue Brief No. 1 (Washington, D.C., 2000).

[42] U.S. Department of Housing and Urban Development, Office of Policy Development and Research, Study on Section 8 Voucher Success Rates—Volume I: Quantitative Study of Success Rates in Metropolitan Areas, prepared by Meryl Finkel and Larry Buron, Abt Associates (Washington, D.C., 2001).

[43] D. von Winterfeldt, W. Edwards, Decision Analysis and Behavioral Research, Cambridge University Press, Cambridge, UK, 1986.

[44] J. Yinger, Closed Doors, Opportunities Lost: The Continuing Costs of Housing Discrimination, Russell Sage Foundation, New York, 1995.

[45] K. Zheng, R. Padman, M.P. Johnson, J. Engberg, H.M. Diamond, <sup>b</sup>An adoption study of a clinical reminder system in ambulatory care using a developmental trajectory approach,<sup>Q</sup> for presentation at the International Medical Informatics Association Triennial Meeting, September 7–11, 2004 (2003 Nov.).

![](/api/attachments/WQDB638M/fulltext/images/420ad5196b773f6ea3784aab30335fca25f4b15986537d816c2bdba8c4b95a4b.jpg)

Dr. Michael P. Johnson is an Assistant Professor of Management Science and Urban Affairs in the H. John Heinz III School of Public Policy and Management at Carnegie Mellon University, Pittsburgh, PA. His research interests lie primarily in operations research/management science planning models for public-sector facility location and service delivery, with applications to location of subsidized housing, home-delivered meals to the elderly/infirm

and community corrections centers. Dr. Johnson also uses cost– benefit analysis to estimate impacts of proposed policies and information technology to design decision support systems. Dr. Johnson received his PhD in operations research from Northwestern University in 1997 and BS from Morehouse College in 1987. His work has appeared in a variety of journals, including Annals of Operations Research, Environment and Planning A, Housing Studies, Journal of Geographic Systems, Journal of Housing Research, Location Science, Management Science, Papers of the Regional Science Association and Socio-Economic Planning Sciences. Dr. Johnson is a member of a number of professional societies, including the Institute for Operations Research and the Management Sciences and the Regional Science Association. He is a recipient of the National Science Foundation’s CAREER Postdoctoral Fellowship and former U.S. Department of Housing and Urban Development Urban Scholars Postdoctoral Fellow.
