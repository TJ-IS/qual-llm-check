---
otero_id: 19240
otero_key: "ZDT6PB76"
title: "Using interdependence as a predictor of data standards. Theoretical and measurement issues"
authors: "Michael D. Wybo; Dale L. Goodhue"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00034-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Using interdependence as a predictor of data standards Theoretical and measurement issues

Michael D. Wybo $^{a,*}$ , Dale L. Goodhue $^{b}$

$^{a}$ Faculty of Management, McGill University, 1001 Sherbrooke Street West, Montréal Que H3A 1G5, Canada $^{h}$ Information and Decision Sciences, Carlson School of Management, University of Minnesota, 271 19th Avenue South, Minneapolis MN 55455, USA

## Abstract

The standardization of data semantics (definitions, names, identifiers, domains, and constraints) across organizational units and systems is one means of coordinating the activities of these units. Since the need for subunit coordination is considered a function of the level of interdependence among subunits, many authors have hypothesized a positive relationship between subunit interdependence and the use of semantic standards. Empirically testing this relationship revealed two surprising results. First, commonly used operational definitions of interdependence from previous research were found to measure different dimensions and hence could not be used interchangeably. Second, no relationship between any of the operational definitions of subunit interdependence and the use of data standards was found. These findings lead us to believe that more precise conceptualizations of interdependence and better models of the tradeoffs between standardization and alternative means of dealing with inconsistent data semantics are required to better understand how investments in standardized data impact organizational outcomes.

Keywords: Data standards; Interdependence; Organization-wide information systems; Heterogeneous database; Measurement; Survey

## 1. Introduction

Inconsistent data semantics plague many organizations. A holding company cannot directly compare the performance of its various units because of different definitions used for Return on Capital. A global distributor cannot coordinate inventories across regions because of inconsistent product coding schemes. A manufacturer cannot determine total purchases by vendor because of incompatible vendor purchase data across divisions.

Semantic inconsistencies are differences in the definitions, names, identifiers, domains, and constraints imposed on data elements across systems and subunits $^{1}$ . In general, techniques for managing these kinds of problems involve developing organizational standards to force semantic consistency or implementing automated mapping or translation mechanisms across semantically inconsistent databases. Several authors have proposed that when organizational subunits are highly interdependent there is a greater need for and benefits from semantic standards [14,17]. There is an implicit assumption that coordinating subunit activities is much more efficient and effective if all units speak the same language. The argument linking standards with interdependence is that 1) semantic inconsistencies hinder data sharing and therefore reduce communication and coordination and 2) the need for coordination is driven by interdependence [6,19].

Yet in spite of the strong theoretical foundations for this relationship, many firms that have attempted standardization have failed or experienced major difficulties. There is no normative principle specifying that standardization is a preferred approach to managing semantically inconsistent data. There are significant problems associated with standards for data semantics that may make them an inappropriate choice even when subunits are highly interdependent. These include keeping individual units aligned with their particular environments when environmental changes are localized and the difficulty of arriving at standards acceptable to all parties involved. There is therefore reason to question the presumed interdependence – standardization relationship. This paper presents an empirical test of that relationship.

## 2. Theoretical foundations

The theoretical basis for a positive interdependence – data standards relationship is found in Organizational Information Processing theory [4]. This theory posits that uncertainty, or the absence of specific, needed information, is a principal force driving the need for organizational information processing. Three sources of uncertainty at the organizational subunit level are 1) complex or non-routine subunit tasks, 2) unstable task environments, and 3) interdependence [20]. For example, a manufacturing unit using newly developed thin film manufacturing technology might face uncertainty in its operations (complex task), from constantly changing customer demands (unstable environment), and in dealing with a procurement office that does not always understand the urgency or nature of its requests (interdependence).

Where uncertainty comes mainly from interdependence (a manufacturing unit that must deal with a procurement unit to purchase materials), data standards could have significant positive impacts. Data whose meaning and codes have been standardized across these units provides a formalized language that facilitates communication and coordination. However, when uncertainty comes mainly from task complexity or environmental instability unique to individual subunits (the variable manufacturing process and changing demand faced by the thin film unit and not faced by the metal stamping unit), semantic standards can reduce the flexibility of an individual subunit to redesign its systems to best meet its unique information requirements. Hence a high level of standardization could have negative performance impacts. The potentially conflicting characteristics of standardization in general, enabling interchangeability and restricting innovation, are well recognized (e.g. [5]). Case study evidence supporting these effects in the case of data standards is found in [10].

In light of the fact that standardized data semantics can be restrictive to individual subunits, it is most likely that they will be employed in situations where the benefits of being able to exchange data unambiguously and efficiently between subunits are high. Information processing theory indicates that such benefits will exist among interdependent subunits. This theoretical perspective leads to the following hypothesis:

As the level of interdependence between subunits increases, the use of standardized data semantics among these same subunits will also increase.

## 3. Construct definition

## 3.1. Semantic data standards

Conceptually, semantic data standards are defined as consistent definitions, names, identifiers, domains, and constraints for data elements across systems and subunits. Several operational definitions are possible. Perhaps the most effective means of standardizing is to eliminate the possibility for violations of the standard by implementing a single, shared source for data. This could be done either through the use of a common system and associated files or databases or through centralized subject area data files or databases [9] accessible to various individual systems

A second approach is to distribute related data across different physical data sources while maintaining “logical centralization” [13] through the use and enforcement of a single conceptual schema. This scenario describes many distributed database systems where data is decentralized and partitioned in different ways to optimize local processing needs but over which a single logical schema is enforced.

A third approach is to document structural and semantic standards as rules for systems development and data use. These standards may exist as paper documentation or be stored in an on-line data dictionary or repository. Standards may be enforced to varying degrees by different CASE environments. There is evidence, however, that standards implemented in this way are relatively easy to circumvent $^{2}$ and that this approach may not be effective in ensuring consistency across independently developed data sources [7,8].

Because of the relative weakness of the documentation approach, the use of semantic standards has been defined in this study as the use of common systems, common data sources, or shared record structures across physically distributed data stores. This operational definition was reviewed by data management personnel in several organizations before being distributed to the firms making up our sample. These reviewers were able to distinguish between the different integration mechanisms on the questionnaire and to identify situations in their own organizations that fit each of them. Thus we were confident that the measure had sufficient face validity for use in the study.

Our measure focuses on the use of semantic standards at the individual subunit level. Standardization implies at least two subunits and is a characteristic of the relationship between these subunits rather than a property of the subunits themselves. Although many subunits may be involved, we have focused on pairs of subunits in order to make the analysis more tractable $^{3}$ .

![](/api/attachments/ZDT6PB76/fulltext/images/f56624f5bb8b9522c14b7054da53aea36685b9933e4d1cfa64843b5a15dab9bc.jpg)  
Fig. 1. Asymmetric standardization between two subunits.

Because the hypothesis states that the use of semantic standards will increase with more interdependence, this operational definition must reflect some notion of “how much”. It must provide some means of measuring the extent to which data is subject to common systems, shared databases, or common record structures. We have operationalized the “amount” of standardization as the proportion or percentage of a subunit’s data that is subject to these mechanisms. This is more meaningful than using an absolute number of standardized data elements as it accounts for the relative size of the data set needed by each subunit. Take, for example, the case of a marketing unit and a production unit in one of the participating companies, depicted graphically in Fig. 1. The number of standardized data elements represents a large proportion of the marketing group’s data but a much smaller proportion of the production group’s data.

Because of this asymmetry it is more accurate to measure the use of semantic standards as a characteristic of one subunit's relationship with a specified other unit. This allows for different “amounts” of standardization for each subunit in the relationship. We therefore would generate one value of the level of standardization for each subunit vis a vis each other subunit (marketing vis a vis production and production vis a vis marketing). We refer to the unit of analysis as the asymmetric subunit pair because it captures the asymmetric nature of the amount of standardization and focuses on pairs of subunits. We operationally define the level of semantic standardization as the percentage of that data required by a subunit to successfully perform its function that is subject to common systems, data sources, or record structures used or adhered to by a specified other unit in the firm. This percentage was measured using a questionnaire administered to members of the subunit's data processing staff.

## 3.2. Subunit interdependence

The concept of the amount of subunit interdependence is defined as the degree to which the actions and outcomes of one unit are controlled by or contingent upon the actions of another unit. This is consistent with the use of the term in the organizational literature (e.g. [15]). However, a direct operationalization of this definition requires close monitoring of all the actions taken in an organization. This is a difficult task, complicated by the fact that the effects of specific actions may not be direct and may only be visible over time. In order to overcome this problem researchers have traditionally operationalized subunit interdependence in terms of the pattern of work flows and the characteristics of resource exchanges between units. An additional third operational definition based on the perceptions of subunit members was developed for this study.

Patterns of work flow between subunits have been used to operationalize different levels of interdependence suggested by $[19]$ . Different patterns reflect increasing levels of “mutual adjustment” that subunits must make to one another’s actions during task execution. In pooled interdependence, subunits do not adjust their actions based on those of another unit, as work does not flow between them. In sequential interdependence, work flows in one direction from one unit to another. Only the receiving unit is required to adjust. Reciprocal interdependence arises from truly “mutual” adjustments made when “each unit’s inputs are its own outputs, recycled through other units” $[23]$ . In team interdependence $[21]$ , subunits work on a task at the same time and make immediate adjustments to the other subunit’s actions.

Characteristics of resource exchanges have been used as surrogates for the specific actions of subunits [1]. Interdependence is operationalized as the degree to which the actions and outcomes of one unit are controlled by or contingent on the receipt of resources from another. The nature of transacted resources varies and may include funds, physical products, support services, or information critical for unit performance [16]. Increased perceived importance of the resources and increased frequency of exchanges are two indicators of increased interdependence.

Perceptions of interdependence represents a third approach to measuring the construct. A measure of perceived interdependence was developed for this study. It measures the extent to which subunit personnel perceive the actions or decisions of their unit to be controlled by or contingent upon the actions of another unit. This approach directly operationalizes the conceptual definition of interdependence in terms of the perceptions of subunit personnel.

Questionnaire items were developed to measure the pattern of work flows, characteristics of resource exchanges, and perceived interdependence among subunits. It should be noted that work flow patterns and characteristics of information exchanges were not directly measured. By using informants to gather this data, these measures are based on informant perceptions.

We also note that the same issues of asymmetry arise for the interdependence construct; two actors may be differentially interdependent in regard to one another, that is the outcomes of unit A may be more contingent on the actions of unit B than B's outcomes are on A's actions. This asymmetry is in fact built into notions of sequential interdependence. Subunits further down the chain of work flows are increasingly dependent on units further up the chain.

## 4. Research design

This research was conducted as a field study as our goal was to investigate the hypothesized relationship in real organizations. In order to perform a quantitative test of the hypotheses, and given the difficulty of manipulating the independent variables in real organizations, we adopted a cross-sectional survey approach using questionnaires for data collection.

## 4.1. Sites and participants

The study was conducted in manufacturing firms. We focused on one type of activity to reduce the influence of industry factors on the analysis. We selected firms of similar size, type of operations, and experience with data management. Participation was solicited from member firms of a local information management professional organization. All who expressed an interest in the project were invited to participate. Participating firms are nationally known manufacturers of food products, electrical machinery, filtration equipment, and measurement instruments. We targeted the Product Engineering, Production, Sales/Marketing, Procurement, and Administrative units of each organization. The basis for this choice was to have a generic and comparable set of functions across firms. After identifying individual participants, each was sent a brief description of the project and a questionnaire.

## 4.2. Data collection

In order to get data from the best informed individuals we used different groups of informants for independent and dependent variables. Data on the level of interdependence was collected from a representative of each unit having significant responsibilities for their unit's relationships with other units. Data concerning the extent of data integration was collected from information systems (IS) professionals having responsibility for the data used by the corresponding subunit. These personnel were extremely knowledgeable concerning the data used by subunit personnel and how that particular data was managed. The majority reported directly to the subunit's manager and worked on a daily basis with subunit personnel.

This approach required the participation of a maximum of 10 individuals per firm, 1 from each of five functional subunits and 5 from the organization's IS function. Selecting informants based on their qualifications to assess a certain construct improves the quality of the data as well as reduces the potential for some obvious methods bias (respondents rating both interdependence and data integration may seek to give what they believe to be internally consistent responses). The principal disadvantage of this approach is the need to enlist the participation of a large number of informants per firm and the significant loss of information from the failure of one informant to correctly respond to their set of questionnaire items. The failure of one individual to participate correctly and completely has the potential effect of reducing the size of the sample by up to four observations $^{4}$ . We considered this to be an acceptable risk when weighed against the prospects for getting higher quality data.

Table I  
Statistical power calculations

<table><tr><td></td><td colspan="3">Power = 0.8 alpha = 0.05</td></tr><tr><td>Estimated effect size (R2)</td><td>0.1</td><td>0.15</td><td>0.2</td></tr><tr><td>Required number of asymmetric subunit pairs</td><td>71</td><td>45</td><td>33</td></tr></table>

## 4.3. Statistical power and sample size

Determination of the appropriate sample size for this study was made on the basis of assuring sufficient statistical power for estimated effect sizes and the analytical technique employed. We used Cohen's [3] procedure to calculate sample size for regression analysis. Conventional levels of statistical power (0.8) and alpha (0.05) were used. We calculated sample sizes for a simple regression analysis at three potential effect sizes corresponding to Cohen's values for "small", "medium", and "large" effects. The resulting sample sizes are shown in Table 1. Using a conservative estimate of effect size (0.1) requires 71 observations to attain the desired level of statistical power. We administered questionnaires for 113 asymmetric subunit pairs. Of these, 14 observations were lost due to unreturned questionnaires by one of the two parties needed to form a complete observation. Another 14 were eliminated due to irreconcilable errors in the responses, such as stating that no data was exchanged between one unit and another and later in the questionnaire stating that this exchange was important. The remaining 85 usable observations represent an effective response rate of 75%.

Table 2  
Single factoredness: inter-item correlations

<table><tr><td>Critical</td><td>Critical</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Coordinate</td><td> $0.90^d$ </td><td>Coordinate</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Implications</td><td> $0.93^d$ </td><td> $0.90^d$ </td><td>Implications</td><td></td><td></td><td></td><td></td></tr><tr><td>Depend</td><td> $0.48^d$ </td><td> $0.59^d$ </td><td> $0.55^d$ </td><td>Depend</td><td></td><td></td><td></td></tr><tr><td>Important</td><td> $0.39^c$ </td><td> $0.44^d$ </td><td> $0.34^b$ </td><td> $0.82^d$ </td><td>Important</td><td></td><td></td></tr><tr><td>Delay</td><td>-0.21</td><td>-0.06</td><td>-0.12</td><td> $0.33^b$ </td><td> $0.25^a$ </td><td>Delay</td><td></td></tr><tr><td>Frequency</td><td>0.18</td><td>0.21</td><td> $0.22^a$ </td><td> $0.53^d$ </td><td> $0.36^c$ </td><td> $0.54^d$ </td><td>Frequency</td></tr><tr><td>Pattern</td><td>0.02</td><td>0.17</td><td>0.14</td><td> $0.44^d$ </td><td>0.19</td><td> $0.31^b$ </td><td> $0.33^b$ </td></tr></table>

$^{a}$ p < = .05.  
$^{b}$ p < = .01  
$^{c}$ p < = .001  
p < = .0001

## 5. Empirical results

As part of our study we pre-tested and validated our measurement instruments within a rigorous validation framework employing both conceptual and empirical criteria $[2]$ . The first set of empirical results we present relate to the validity of the interdependence construct as employed in the organizational literature. The second concerns the statistical relationship between subunit interdependence and the extent of data integration.

5.1. Single factoredness of the subunit interdependence construct

As noted above, the organizational literature contains multiple operational definitions of subunit interdependence. This gives rise to the question of whether these definitions can be used interchangeably and whether items based on these definitions can be combined into a single measure of interdependence.

Conceptually, there is little reason to believe that such combination is meaningful. Resources considered to be important by the receiving unit need not be frequently exchanged. Likewise, frequent exchange need not imply importance. The pattern of information exchanges need not reflect either frequency or importance. Reports or updated files may be sent regularly to a number of subunits but only be useful to a few, if any. To the extent that bureaucratic procedures exist that are not required for the functioning of the unit, neither frequency nor pattern based measures are likely to measure interdependence as it is conceptually defined. These operational definitions implicitly assume that existing information flows address real information needs and do not include additional, non-essential information exchanges. We make this assumption explicit in our empirical analyses.

Table 3  
Common Factor Analysis/Oblique Rotation

<table><tr><td></td><td>F1</td><td>F2</td><td>F1</td><td>F2</td><td>F3</td></tr><tr><td>Critical</td><td>0.98410</td><td>0.18177</td><td>0.97752</td><td>0.39878</td><td>0.01820</td></tr><tr><td>Coordinate</td><td>0.91461</td><td>0.24495</td><td>0.91007</td><td>0.41035</td><td>0.09753</td></tr><tr><td>Implications</td><td>0.90743</td><td>0.20747</td><td>0.93955</td><td>0.32817</td><td>0.10288</td></tr><tr><td>Depend</td><td>0.47534</td><td>0.85236</td><td>0.43225</td><td>0.86143</td><td>0.64297</td></tr><tr><td>Important</td><td>0.38766</td><td>0.63421</td><td>0.34125</td><td>0.93336</td><td>0.42120</td></tr><tr><td>Delay</td><td>-0.15859</td><td>0.54289</td><td>-0.15047</td><td>0.23894</td><td>0.63188</td></tr><tr><td>Frequency</td><td>0.16096</td><td>0.75220</td><td>0.17781</td><td>0.45717</td><td>0.84432</td></tr><tr><td>Pattern</td><td>0.06454</td><td>0.48968</td><td>0.07231</td><td>0.28524</td><td>0.51143</td></tr><tr><td colspan="6">Inter-Factor Correlations</td></tr><tr><td></td><td>F1</td><td>F2</td><td>F1</td><td>F2</td><td>F3</td></tr><tr><td>F1</td><td>1.00000</td><td></td><td>F1</td><td>1.00000</td><td></td></tr><tr><td>F2</td><td>0.25541</td><td>1.00000</td><td>F2</td><td>0.40739</td><td>1.00000</td></tr><tr><td></td><td></td><td></td><td>F3</td><td>0.09293</td><td>0.50461</td></tr></table>

Table 4  
Total variance accounted for by each factor

<table><tr><td></td><td>F1</td><td>F2</td><td>F3</td><td>F4</td><td>F5</td><td>F6</td><td>F7</td><td>F8</td></tr><tr><td>Eigenvalue</td><td>3.5188</td><td>2.1947</td><td>0.8207</td><td>0.6873</td><td>0.3960</td><td>0.1723</td><td>0.1366</td><td>0.0733</td></tr><tr><td>Proportion</td><td>0.439</td><td>0.274</td><td>0.102</td><td>0.085</td><td>0.049</td><td>0.021</td><td>0.017</td><td>0.009</td></tr><tr><td>Cumulative</td><td>0.439</td><td>0.714</td><td>0.816</td><td>0.902</td><td>0.952</td><td>0.973</td><td>0.990</td><td>1.000</td></tr></table>

To test the single factoredness of these operational definitions, we first examined the matrix of correlations among the subunit interdependence items shown in Table 2 for patterns that might indicate different underlying dimensions of the construct. If all items measure the same dimension, they should be significantly correlated at approximately the same level. The inter-item correlation matrix indicates two general groupings of items corresponding to 1) the importance of received information and the perceived interdependence items and 2) the frequency of exchange and pattern items. Furthermore, the items DEPEND and IMPORT correlate highly and significantly with almost all other items. The text of each item appears in the appendix.

To further investigate the single factoredness of these items we performed an exploratory factor analysis. Since our objective is to identify possible latent dimensions underlying these variables and we have no a priori knowledge of how the variance of each variable is divided among common, unique, and error variance, we employed a common factor model [12]. This eliminates unique and error variance and derives a solution based only on the common variance among the variables. We used an oblique rotation in arriving at the factor solution. Such rotation permits correlated factors, which is consistent with the assumption that the different operational definitions measure dimensions of the same construct and not different, unrelated constructs. Table 3 reports the factor structure matrix resulting from two and three factor solutions. Elements of this matrix are correlation coefficients of the variable with the underlying factor and are indicators of the grouping of variables with factors. Table 3 also reports inter-factor correlations.

(Table 4)

Using the conventional eigenvalue of 1 or greater for admitting factors resulted in the two factor solution. In this solution there is a clear grouping of the first three items on factor 1 and the last three items on factor 2. The DEPEND and IMPORTANT items loaded on both factors. This is consistent with the pattern observed in the inter-item correlation matrix. We forced a three factor solution to see if a general interdependence factor based on the items DEPEND and IMPORTANT would emerge. This is indeed the case. All variables load at least moderately on this third factor and factors F1 and F2 show a cleaner separation with the three factor solution. We note that the grouping of items in the three factor solution does not map directly to the three operational definitions of interdependence presented earlier. Most notably, the items representing the pattern and characteristics of exchanged resources load heavily on the same factor and a third factor, which we label here as “general interdependence”, emerges.

Table 5  
Single factoredness - internal consistency reliability

<table><tr><td>Scale</td><td>Perceptions of Interdependence</td><td>Patterns and Characteristics of Exchanged Resources</td><td>General Interdependence</td></tr><tr><td>Std. Alpha</td><td>0.966</td><td>0.707</td><td>0.899</td></tr><tr><td>Scale Items</td><td>Implications, Coordinate, Critical</td><td>Delay, Frequency, Pattern</td><td>Depend, Important</td></tr></table>

Table 6  
Regression results (Dependent variable = extent of semantic standardization)

<table><tr><td></td><td>Independent Variable</td><td>Standardized Regression Coefficient</td><td>Adjusted R-square</td><td>p-value of overall F-test</td><td>n</td><td>Statistical Powera</td></tr><tr><td>H1:</td><td>General Interdependence</td><td>0.073</td><td>-0.0085</td><td>0.5357</td><td>74</td><td>0.8</td></tr><tr><td>H2:</td><td>Perceived interdependence</td><td>0.081</td><td>0.0074</td><td>0.4948</td><td>73</td><td>0.8</td></tr><tr><td>H3:</td><td>Exchanged Resources</td><td>0.140</td><td>0.0055</td><td>0.2430</td><td>71</td><td>0.8</td></tr></table>

$^{a}$ Statistical power estimates band on small effect size and defined in Table I

As a final step we assessed the internal consistency reliability of the sets of variables identified in the factor analysis. These results appear in Table 5. The metric for evaluating internal consistency reliability is coefficient alpha (Cronbach's alpha). The importance/perceptions scale shows a very high internal consistency reliability. The time sensitivity scale's reliability is slightly lower than the 0.8 convention but acceptable for a measure under development.

The conclusion we draw from this first part of our empirical analysis is that the subunit interdependence construct is not uni-dimensional and that different operational definitions of the construct may measure different dimensions. Hence future research employing the interdependence construct should not use these alternative operationalizations interchangeably. More importantly, researchers should specify which of these operational definitions they are using and the theoretical justification for using that particular definition $^{5}$ .

## 5.2. The interdependence - semantic standards relationship

Table 6 shows the results of the regression analysis of the relationship between subunit interdependence and the use of semantic standards. Due to missing values for some individual questionnaire items, individual analyses may have fewer than 85 observations. The number of observations and statistical power is reported for each regression. As the literature provides no a priori theoretical basis for choosing among the three different identified dimensions we performed the test using each. None of the interdependence measures showed a significant statistical relationship with the level of use of semantic standards. Even though we designed our study to have sufficient statistical power to detect a “small” effect size we did not detect a statistically significant effect. If the principal benefits of data standards stem from subunit interdependence we believe we should see a managerially significant effect size and that the conservative estimate of 0.1 used in the sample size calculations is not unreasonable. We must therefore conclude that either 1) the hypothesized relationship does not exist, 2) it is smaller than “small” and not managerially significant, or 3) the findings are the result of some other factor we have not heretofore considered.

## 6. Discussion

The results obtained and presented above are clearly inconsistent with the interdependence – integration relationship proposed in the information systems literature. The hypothesized relationship between interdependence and data standards is built upon a well accepted theoretical foundation. Rather than dismissing this relationship as non existent, we examine three alternative explanations for our findings:

Measurement problems.

Decision makers may not have perceived or acted on the link.

Data standards are not the only solution.

## 6.1. Measurement problems

A current view of measurement is that it comprises both conceptual and empirical activities that provide meaning to the theoretical variables and hence cannot be divorced from the broader theoretical network [22].

Our measures of subunit interdependence are valid from an empirical point of view. They demonstrate the desirable characteristics of being unidimensional and internally consistent. They also point to the fact that subunit interdependence is a complex construct. As such, some conceptualizations may be better in some theories than in others. It may be that the essence of the construct, as operationally defined in the organizational literature, is lost when using surrogates based on workflows and exchanged resources. These conceptualizations may be inappropriate to the case of semantic data standards.

In terms of our measure of the extent of use of semantic standards we believe that we have a valid conceptual definition, clearly distinguishing between standards and alternative mechanisms for addressing semantic inconsistencies. The definition also distinguishes between “strong” semantic standardization mechanisms, such as common systems, data sources, and record structures and much weaker mechanisms such as documented data definitions. It will, of course, be desirable to develop more rigorously validated measures of semantic standardization, as well as other techniques for managing data semantics. However, we believe this measure is a good first cut at operationalizing an important concept that has until now been dealt with solely on a conceptual level.

## 6.2. Decision makers may not have perceived or acted upon the link

A second potential explanation for our findings is that even though there is a link between interdependence and the benefits of semantic standards, IS decision makers have not recognized it in the past and have not acted on it. Standards for data semantics have traditionally been proposed as a general approach for managing organizational data rather than as a means of targeting specific areas of interdependence (i.e. selective or partial standardization at the level of individual data elements of groups of subunits). Proponents of standardized semantics have tended to push for large scope rather than focus. Thus our results could be interpreted as suggesting that standardization efforts have not been well targeted, at least in our sample firms.

It might also be the case that the business processes in the participating organizations are inefficient in that information exchanges do not reflect real information needs. We have no evidence on which to question the assumption that the business processes in these firms are not in need of serious re-engineering and that information exchanges do indeed reflect required information exchanges. It is, however, possible that business processes are not as efficient as they might be.

## 6.3. Data standards not the only solution

A third possible explanation for our results is that standards are not the only and may not be the least expensive means of responding to the coordination needs of interdependent actors. Even where actors are interdependent and the impact of coordination on tangible benefits clear, alternative mechanisms may be more appropriate.

It is possible to resolve some simple semantic inconsistencies through mapping or translation between databases. These inconsistencies include some data element naming conflicts, conflicting data types, or differences in data element legal values. Many of these mapping approaches operate in an uncoupled mode and the resulting integrated data is usually non-updatable. Hence, in certain cases, mapping is an appropriate and much simpler response to sharing data to meet coordination needs than the use of semantic standards.

In some cases organizations avoid automated solutions, placing responsibility for resolving semantic inconsistencies in the hands of a human actor. This solution is sometimes used when the number and complexity of inconsistencies is low or when the resolution of inconsistencies need only be done once, to answer a specific question for example.

To the extent that the problems caused by semantically inconsistent data are smaller than presumed, there will be less pressure to implement standards, or any other mechanism for managing inconsistent data, as a means of coordinating subunit activities. Thus it is important to directly address the question of the business impacts of inconsistent semantics as well as the costs and effectiveness of alternative mechanisms for managing different types of data inconsistencies.

## 7. Conclusions

We draw the following conclusions based on the conceptual and empirical analyses reported above. First, the conceptualization and operationalization of data standards construct we have presented provides an adequate means of assessing levels of data standards in organizations. The definitions are consistent with concepts of schema integration and bring an organizational perspective to schema integration research.

Second, widely used conceptual and operational definitions of subunit interdependence may not be interchangeable and may indeed reflect different conceptual definitions of interdependence. The distinctions between these definitions may have important implications for the use of the construct in theory building. Conceptual and operational clarification of the interdependence construct deserves further detailed study. Explicit conceptual and operational definitions and validation data should be presented when using the construct in empirical research. Alternative conceptual definitions of interdependence may be required to better fit the concept into a larger theoretical network of data management.

Finally, there is a strong theoretical basis for presuming a relationship between subunit interdependence and benefits from semantic standards. This presumed relationship is an important one. Standardization would seem to be a logical means of addressing the coordination needs generated by interdependence. Since we found little evidence of this relationship here, we have carefully laid out the research design and measurement approaches we took, to enlighten future efforts at testing this relationship. Certainly, if no evidence for its existence can be found by a number of careful studies, some re-theorizing is in order. We do not believe we have yet reached that point.

## Acknowledgements

This research was partially funded by an FCAR grant to the first author.

## Appendix A. Questionnaire items

## A.1. Definitions of Alternative Standardization Mechanisms

SHARED SYSTEMS OR DATABASES are information systems or databases shared by more than one functional unit. A single order entry system shared by different product lines is an example of a shared system. Master files or databases of customers, parts, or products are examples of shared databases.

STANDARD RECORD STRUCTURES are rules that control how individual data elements are assembled into records. Standard record structures can apply to the data stored on multiple systems and databases yet the data itself may not be shared.

STANDARD FIELD DEFINITIONS are rules that define the meaning of individual data elements. For example, a standard field definition for PARTS-STATUS may be defined to mean whether a particular part is scheduled for production in the next 60 days. Standard field definitions are often stored in a data dictionary or repository.

NO CROSS FUNCTIONAL STANDARDS refers to data used by UnitOne that does not come from systems or databases shared with other units and which is not controlled by record or field level standards used across more than one functional unit in the your company.

## A.2. Questionnaire item used to collect level of data standardization

## DATA STANDARDS SHARED WITH UNITWO

Classify $100\%$ of UnitOne's data according to the types of data standards mechanisms that link it with UnitTwo.

—% Percentage of UNITONE's critical data stored on systems or databases shared with UNITTWO.

—% Percentage of UNITONE's critical data that are not on shared systems, but which are subject to standard record structures which also apply to UNITTWO.

—% Percentage of UNITONE's critical data that are not on shared systems, and are not subject to standard record structures, but which conform to standard field definitions which also apply to UNITTWO.

—% Percentage of UNITONE's critical data that are not subject to any data standards which also apply to UNITTWO.

A.3. Questionnaire item used to collect data on level of interdependence. Variable name from tables in text associated with each item is given as [VARIABLE]

<table><tr><td></td><td>Not Applicable</td><td>One Qtr. or Longer</td><td>One Month</td><td>Two Weeks</td><td>One Week</td><td>One Day</td><td>One Hour</td><td>One Minute</td></tr><tr><td rowspan="3">[DELAY]</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="8">5. How long can information coming from this other unit be delayed before the operations of UnitOne are negatively affected?</td></tr><tr><td>Not Applicable</td><td>Strongly Disagree</td><td>Disagree</td><td>Somewhat Disagree</td><td>No Opinion</td><td>Somewhat Agree</td><td>Agree</td><td>Strongly Agree</td></tr><tr><td>[COORDINATE]</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>[IMPLICATIONS]</td><td colspan="8">7. Close coordination with this unit is essential for UnitOne to successfully do its job.</td></tr><tr><td rowspan="3">[CRITICAL]</td><td colspan="8">8. The actions or decisions of this other unit have important implications for the operations of UnitOne.</td></tr><tr><td colspan="8">9. Information provided by this other unit is critical to the performance of UnitOne.</td></tr><tr><td>Not Applicable</td><td>Once/Qtr. or Less</td><td>Once a Month</td><td>Every Two Weeks</td><td>Once a Week</td><td>Once a Day</td><td>Once an Hour</td><td>Once a Minute</td></tr><tr><td rowspan="2">[FREQUENCY]</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td colspan="8">10. How frequently does UnitOne send or receive information to or from this other unit?</td></tr></table>

<table><tr><td colspan="5">11. How important is the information you receive from this other unit?</td><td>a__Unit Two</td></tr><tr><td rowspan="2">Impossible to function effectively without it</td><td rowspan="2" colspan="2">Difficult, but possible,to function effectively without it</td><td colspan="3">A minor inconvenience toNone receivedb__Unit Threec__Unit Four</td></tr><tr><td>do without it</td><td colspan="2">from this unit</td></tr><tr><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td colspan="6">13. In general, how dependent on these other units is your unit?</td></tr><tr><td>Extremely</td><td>To a great extent</td><td>Moderately</td><td>To some extent</td><td>Not at all</td><td rowspan="2">a__UnitTwob__UnitThreec__UnitFourd__UnitFive</td></tr><tr><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td></tr></table>

A.4. Questionnaire item used to collect data on [pattern] of information exchanges

<table><tr><td></td><td>UNITTWO</td><td>UNITTHREE</td></tr><tr><td>Each column must sum to 100% of the Work Objects or Information exchanged with this other unit.</td><td>Classify 100% of information exchanged with this unit into these four patterns?</td><td>Classify 100% of Information exchanged with this unit into these four patterns?</td></tr><tr><td>Percent passed in one direction from this other unit to your unit.</td><td>%</td><td>%</td></tr><tr><td>Percent passed in one direction from your unit to this other unit.</td><td>%</td><td>%</td></tr><tr><td>Percent passed back and forth between your unit and this other unit over time.</td><td>%</td><td>%</td></tr><tr><td>Percent used or worked on at the same time by your unit and this other unit.</td><td>%</td><td>%</td></tr><tr><td></td><td>100 %</td><td>100 %</td></tr></table>

## References

[1] Aiken, M. and J. Hage (1968), “Organizational Interdependence and Intra-Organizational Structure”, American Sociological Review, 33(6), pp. 912–930.

[2] Bagozzi, R.P. (1980), Causal Models in Marketing, New York, Wiley and Sons.

[3] Cohen, J. (1988), Statistical Power Analysis for the Behavioral Sciences, Hillsdale, NJ, Lawrence Erlbaum Associates.

[4] Daft, R.L. and R.H. Lengel (1986), “Organizational Information Requirements, Media Richness, and Structural Design”, Management Science, 32(5), pp. 554–571.

[5] Fry, J.P. and E.H. Sibley (1976), “Evolution of Data-Base Management systems”, Computing Surveys, 8(1), pp. 7–36.

[6] Galbraith, J.R. (1973), “Designing Complex Organizations”, Reading, MA, Addison – Wessley.

[7] Gillenson, M.L. (1982), “The State of Practice of Data Administration – 1981”, Communications of the ACM, 25(10), pp. 699–706.

[8] Goodhue, D.L., L.J. Kirsch, J.A. Quillard, and M.D. Wybo (1992), “Strategic Data Planning: Lessons From the Field”, MIS Quarterly, 16(1), pp. 11–34.

[9] Goodhue, D.L., J.A. Quillard, and J.F. Rockart (1988), “Managing the Data Resource: A Contingency Perspective, MIS Quarterly, 12(3), pp. 373–392.

[10] Goodhue, D.L., M.D. Wybo, and L.A. Kirsch (1992), “The Impact of Data Integration on the Costs and Benefits of Information Systems”, MIS Quarterly, 16(3), pp. 293–311.

[11] GUIDE (1991), “The Definition of Data Administration and The Support Role of CASE Tools”, Guide International Corporation, Application Enabling Environment Division, GPP - 256

[12] Hair, J.F., R.E. Anderson, R.L. Tatham, and W.C. Black (1992), Multivariate Data Analysis, Third ed., New York, Macmillan.

[13] Heimbigner, D. and D. McLeod (1985), “A Federated Architecture for Information Management”, ACM Transactions on Office Information Systems, 3(3), pp. 253–278.

[14] Lee, S. and R.P. Leifer (1992), “A Framework for Linking the Structure of Information Systems with Organizational Requirements for Information Sharing”, Journal of MIS, 8(4), pp. 27–44.

[15] McCann, J. and J.R. Galbraith (1981), “Interdepartmental Relations”, in: Handbook of Organizational Design, Oxford University Press, pp. 60–84.

[16] McCann, J.E. and D.L. Ferry (1979), “An Approach for Assessing and Managing Inter-Unit Interdependence”, Academy of Management Review, 4(1), pp. 113–119.

[17] Rockart, J.F. and J.E. Short (1989), “IT in the 1990’s: Managing Organizational Interdependence”, Sloan Management Review, pp. 7–17.

[18] Sheth, A.P. (1991), “Semantic Issues in Multidatabase Systems”, SIGMOD Record, 20(4), pp. 5–9.

[19] Thompson, J.D. (1967), “Organizations in Action: Social Science Bases of Administrative Theory”, New York, NY, McGraw-Hill.

[20] Tushman, M.L. and D.A. Nadler (1978), “Information Processing as an Integrating Concept in Organizational Design”, Academy of Management Review, 3, pp. 613–624.

[21] Van de Ven, A.H., A.L. Delbecq, and R. Koenig, Jr., (1976), "Determinants of Coordination Modes Within Organizations", American Sociological Review, 41(2), pp. 322–338.

[22] Venkatraman (1989), “The Concept of Fit in Strategy Research: Toward Verbal and Statistical Correspondence”, Academy of Management Review, 14(3), pp. 423–444.

[23] Victor, B. and R.S. Blackburn (1987), “Interdependence: An Alternative Conceptualization”, Academy of Management Review, 12(3), pp. 486–498.

![](/api/attachments/ZDT6PB76/fulltext/images/e38b94c0c12558c40ae74ec5db7d5e1df04f3ac0d6b31c26f80e08d4a18c4a28.jpg)  
Michael D. Wybo is an assistant professor of Information Systems at the Faculty of Management of McGill University. He received his Ph.D. in MIS from the University of Minnesota. His research is in assessing the impact of alternative data management strategies.

![](/api/attachments/ZDT6PB76/fulltext/images/536f03e443e83ac5ae2c0a48de7b2211f4346d634656df310cfa7deb3f63e7e7.jpg)  
other IS infrastructure/resources.  
Dale L. Goodhue is an assistant professor of MIS at the University of Minnesota's Carlson School of Management. He received his Ph.D. in MIS from MIT, and has published in MIS Quarterly, Database, Information and Management, and has a forthcoming article in Management Science. His research interests include measuring the impact of information systems, the impact of task – technology fit on performance, and the management of data and
