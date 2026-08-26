---
otero_id: 18883
otero_key: "6EWQ9294"
title: "A framework for effective data collection, usage and maintenance of DSS"
authors: "Bay Arinze; Snehamay Banerjee"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90073-o"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A framework for effective data collection, usage and maintenance of DSS \*

Bay Arinze and Snehamay Banerjee

Department of Management, Drexel University, Philadelphia, PA, USA

The need for proper, reliable, and accurate data for any DSS is universally accepted. However, in real life, developers and users face ill-structured problems in noisy and difficult environments. While a wide variety of hardware and software exists for data storage, communication, and presentation (e.g., specialized hardware, DBMS's, and query languages), much less effort has gone into developing methodologies for DSS data capture in less tractable decision environments. Insufficient understanding of potential problems with DSS data and of available methods for dealing with these problems will

![](/api/attachments/6EWQ9294/fulltext/images/9f40fb300529e54a41c4037372e7c5d693a935b402bb3323faff08411208e024.jpg)

Bay Arinze is an Assistant Professor of Management Information Systems in the Department of Management at Drexel University. He holds a B.Sc. in Computer Science from the University of Lagos and an M.Sc. and Ph.D. in Systems Analysis from the London School of Economics and Political Science. His current research interests include DSS design methodologies and applications and knowledge-based systems and their uses in operations management. He has published articles in Journal of Management Information Systems, IEEE Transactions in Engineering Management, Computers and Industrial Engineering, Industrial Marketing Management and ACM Sigart Special Issue on Knowledge Acquisition.

![](/api/attachments/6EWQ9294/fulltext/images/1caef026bfb81c879d69f73fd001b9daa76533c77d141f495513d38f8a7976fa.jpg)

Snehamay Banerjee is an Assistant Professor of Management Information Systems in the Department of Management at Drexel University. He holds B. Tech. and M. Tech. in Engineering from India, an M.S. from Case Western Reserve University and Ph.D. in Information Systems and Management Science from University of Maryland at College Park. His current research interests include knowledge-based systems and their uses in management science, model management and Electronic Data Interchange.

Correspondence to: Bay Arinze, Department of Management, Drexel University, Philadelphia, PA 19104, USA, tel.: (215) 8951798, E-mail: Arinzeob@duvm.

\* An earlier version of the paper appeared in the 1991 HICSS conference proceedings.

serve to limit the effectiveness of even sophisticated technologies in DSS development and use. This paper addresses the issue of data collection for DSS in noisy environments, and presents a framework for detecting, preventing, and correcting errors in data collected for DSS use. It employs the metaphor of data communications, and uses analogies from that field in constructing the framework. The approach is illustrated using an actual case study from industrial marketing.

Keywords: Decision support systems, Data collection, Data quality, DSS databases, Data communications, Industrial marketing.

## 1. Introduction

A Decision Support System (DSS) is an effective combination of many components (e.g., hardware, software, a data and/or a knowledge base), created to aid decision makers. DSS are used in the solution of ill-structured problems faced by managers in various organizations, and their use is typically accompanied by an emphasis on support of decision-making, an adaptive model-based approach, system flexibility, and high-level user interfaces $[2,10]$ .

The capabilities to be expected from a DSS however, are significantly dependent on the availability and quality of data to solve the problem. Much of the DSS research literature has focused on problem modeling and model execution, leaving much to be done in the other critical area i.e., DSS data requirements. For developing effective DSS, there is a need to focus on analyzing appropriate data requirements, obtaining and validating such data, and making the data easily accessible.

While the majority of the DSS development approaches are process-driven [e.g., 7], the question of data requirements analysis is recognized as critical to the DSS development process [17].

In fact, Little and Cassetari [14] say that a DSS may live or die by the quality of the data contained in its database. With the more structured Management Information Systems (MIS), sources of data for the organizational database are typically stable, static, and primarily internal or organizational. However, in creating the DSS database, data sources are unstable, volatile and usually a mix of the internal and external.

For many ad hoc DSS in particular (i.e., DSS created for special projects and of limited duration), data collection is often performed haphazardly and unsystematically, resulting in unacceptable and inaccurate DSS output $[1,5]$ . One reason is that few frameworks have been developed to enable the DSS developer understand and analyze the sources of errors in DSS data, their impact on DSS effectiveness, methods for detecting and preventing errors in the acquired data, and correcting them when they occur.

While the DSS paradigm has greatly matured over the years, data collection and validation is a continuing concern. Data collection may be viewed as moving data from various sources into the DSS. It is conceivable therefore, that the theories associated with data communications may significantly help in understanding the issues associated with DSS data collection. The utility of the communications analogy is the provision of greater insights into the typology of potential problems in capturing DSS data, and analogous methods for handling such problems.

Our model employs concepts from data communications as an analogous framework for error avoidance, detection, and correction of data extracted from internal and external sources into a DSS database. This framework will help a DSS developer anticipate potential problems with data and take corrective action to solve them. Benefits of this approach include a more systematic method for data collection, leading to better-quality, and more effective DSS.

## 2. DSS requirements analysis

The DSS problem solving dimension is well-advanced, with an abundance of options for the

![](/api/attachments/6EWQ9294/fulltext/images/ede4471fe8fa664ecea20a353ae3e8eddddad47fd7a0d7dfbe4ecdf1cf8c0ae8.jpg)  
Fig. 1. Sprague and Carlsons' DSS model.

DSS builder. A useful classification has been outlined by Sprague and Carlson [19], who envisage DSS artifacts as existing on three levels (see Figure 1), namely:

(a) A Dialogue Management Subsystem (DGMS).  
(b) A Model Base Management Subsystem (MBMS).

(c) A Data Base Management Subsystem (DBMS).

These subsystems can be further subdivided. The DGMS should have a knowledge based component to facilitate communication with users. The MBMS should have wide ranging capabilities that include selection, integration, creation, modification, and execution of models originating from a wide range of quantitative techniques. Database technologies are also well-advanced, with respect to hardware (e.g., fast-access and large capacity storage), software (i.e., powerful multi-user operating systems, object-oriented DBMS's, specialized DSS modeling languages like IFPS, and fourth generation languages [16,25]), and contemporary information system configurations (such as distributed database options [9,24]).

Figure 2 depicts a general form of DSS methodology, paralleling others cited authors. It further illustrates the role of both the technological and modeling options available to the DSS developer, and indicates their use in the Design phase of the DSS development life cycle. However, prior to the use of these methods and technology, specifically, in the DSS requirements analysis phase, data collection is required to calibrate the DSS.

Validating and checking the quality of data for DSS in data requirements analysis has not received a great deal of attention in the DSS literature. Keen and Scott Morton [11], in their seminal work on DSS, referred to the issue of DSS data as posing several problems, including the difficulty of collecting and validating the data, and its subsequent maintenance. In fact, one heuristic they make mention of states: “Assume the data you want doesn’t exist, no matter what people tell you.”

![](/api/attachments/6EWQ9294/fulltext/images/f984495add929ae9f296c928ec2873cb17fdde576bb7f03208c451b9b49acc7a.jpg)  
Fig. 2. The role of data collection methods in the DSS development cycle.

In Figure 1, the ROMC approach (Representations, Operators, Memory Aids, and Control) embodies a contemporary and comprehensive DSS methodology (see [26] for an updated version). In addition to specifying the ROMC elements, a means is developed to transform these elements into an operational DSS. The ROMC approach deals with several required capabilities for a DSS data extraction subsystem. These capabilities include data aggregation (and occasionally, disaggregation), subsetting, data presentation and data description. In addition, internal and external sources of DSS data are identified. While the taxonomy of potential problems with collected data apply to data from both sources, such problems are potentially more acute with externally collected data where the controls are poor.

Sol [18] and Stecher and Hellemaa [23] consider other aspects of the aggregation of data by DSS, with regard to potential inaccuracies introduced into global decisions; and the applicability of knowledge based methods to the aggregation process.

Furthermore, some authors $[4,5]$ have examined the differing requirements of institutional and ad hoc DSS, with the latter authors focusing particularly on database requirements. Using anecdotal comparisons, they found that institutional DSS make use of more internal data, larger data amounts, more sophisticated data organization and random access, but more limited manipulation than DSS of the ad hoc variety. In addition, in $[8]$ two types of DSS databases are envisaged, namely operational and planning types. These map broadly onto the institutional/ad hoc DSS types discussed previously, although cross-mappings may be created.

These efforts may be seen as setting the stage for a framework and procedure for data capture into a DSS database. While the first strand of research discussed sets out the required DSS capabilities, the second delineates the different classes of DSS, to enable a more focused analysis of the requirements for each class.

## 3. A framework for DSS data collection

The framework now described provides ways to identify potential sources of error in data collection and DSS calibration, the impact of these errors on DSS effectiveness, and prevention, detection and correction methods that are applicable. Analogies from the area of data communications are employed to develop these functions. The intention in this paper is not to document an exhaustive list of potential data collection errors, but to provide a useful methodology for the DSS developer to handle data collection effectively.

The framework however, does not employ the rigid algorithmic methods of error handling used in data communication because the complexities of DSS data validation will not support it. Therefore, at every stage, the user interface remains a vital input; thus user subjective judgments play an important role.

## 3.1 Error sources in DSS data collection

Consideration of the sources of error in the data communications context highlights several classes of potential error. They include: noise (white noise, impulse noise, and interference), jitter (variation in phase or magnitude), attention, (weakening of data signals over distance) and delay distortion (which occurs when signal amplifiers are used [21,22]). The equivalent DSS types of potential error are:

## Noise

In data communications, white noise is a disturbance present in all data transmission; it is introduced by the environment. In a DSS environment, errors are introduced while capturing data from the environment. For example, obtaining data from a sample instead of the population introduces potential errors. A tool used to collect data may often serve to introduce errors into the body of collected data, e.g., incorporating data from previous (flawed) analyses. It is difficult to eliminate white noise.

Impulse noise is characterized by signal spikes, momentary and acute changes in the noise level, caused by external agents e.g., lightning. Although a certain amount of noise accompanies every DSS dataset, the analogy envisages situations in which there is temporary volatility in the collected data such as war, strikes etc., which can momentarily, but significantly, alter the data set. Such sudden variations of data, if unnoticed, may cause significant errors.

Interference or cross talk occurs due to unplanned merging of two or more signals from different channels. The interference effect on DSS data may occur if there are confounding factors that inadvertently impact the usability of data collected for the intended purpose. For example, data may have been collected from diverse sources, and it may be difficult to nullify or erase the effects of several of these sources.

## Data synchronization (jitter)

Jitter signifies a phase variation in a continuous signal. In the realm of DSS we expect jitter only if the data have a seasonal or cyclical factor; e.g., for a DSS where the data collected from one environment is used to predict the behavior in another and the expected behavior of the environments are identical save for a phase lag. As an example, if American and Australian markets are expected to demonstrate the same type of consumer behavior for winter garments, and if data are available for America but not for Australia, then we may use the data from the American market to predict the behavior of the Australian market. However, analysts could be caught off guard if the data are used directly i.e., the high months of America correspond to the low months in Australia (as winter in US is summer in Australia). So, although the markets exhibit the same behavior, a phase lag is involved. This error can be introduced inadvertently if the analysts are not familiar with environments under which data have been collected and/or where the DSS is to be used.

## Attenuation / delay distortion

There is a direct parallel of attenuation and delay distortion in the context of DSS data extraction and analysis. Attenuation signifies a weakening of the signal due to the distance traveled by the data; this translates to distortions introduced when data are gathered second or third-hand from an external source. The data loses accuracy on its way to the DSS database. To transform the data back to its original form, the DSS may employ 'filters' to compensate for these effects, but it is often difficult to unearth the nature of the previous data distortion.

Filters placed to clean the data may introduce further errors, some of which include computational overhead and possible over- or undercompensation for encountered distortion.

## 3.2. The impact of errors on DSS effectiveness

It has been suggested that DSS outputs are only as good as the data with which the DSS is supplied $[14]$ . The above types of errors will affect both model building and the calibration of the DSS database.

First, the designed model may form an inaccurate representation of the realworld phenomenon it is supposed to depict. For instance, a market analysis model may be “hard-wired” with inaccurate data relating to the market segments, sizes, constituents etc.; it would produce correspondingly unreliable analyses of the market.

Second, incorrect calibration of the DSS database will result in retrieval of erroneous factual information concerning various aspects of the modeled reality, and inaccurate modeling results.

Alter [1] has described the need for “bomb-proofing” by builders of computerized DSS, citing the sharp decline in confidence by users of a DSS that is subject to unreliability e.g., errors that are obvious to the DSS user. An important component of a system’s reliability is its ability to degrade gracefully, rather than sharply. The robustness of a DSS and its reliability depend centrally upon the prevention, detection and correction of errors in collected data.

## 3.3. Methods of error prevention

In the realm of data communications, there are a body of methods which may be used for error prevention $[22]$ . These methods include measures for increasing the robustness of the communications network (using line conditioning, shielding, and improved hardware etc.), and decreasing the requirements made on it (e.g., lower transmission speeds). In the same way, it is possible to envisage equivalent methods for dealing with potential problems in collection and transmission of data required for DSS. Three potential processes (and any combination therein) can be used to prevent propagation of error

First, DSS ‘filters’ may be used to clean up incoming data in the form of analytical and statistical tools. Examples of filters placed over data include those that screen out inaccurate or incomplete observations (using expectations of domains and ranges) from a data sample; and those that perform extraction and possibly extrapolation (using trend analysis, regression etc.) of required data from a wider data pool, e.g., departmental data from a wider organizational transaction database, or forecasts from historical data. Analytical and statistical tools may be used to reorient the collected DSS data or determine the extent of its validity. Reorienting the data for DSS use involves techniques such as trend smoothing to counter the effects of potentially abnormal observations. This may also remove real outliers that should not be counted e.g., the effect on the agricultural area of a sudden flood or local drought. Validity testing for existing data will include determined levels of confidence expressed about data interrelationships, statistical measures such as standard deviations and correlations, and the results of various sensitivity and risk analyses performed on the data.

Second, there may be a lessening of the requirements and expectations from the collected DSS data. This may range from the inclusion of reliability caveats accompanying its use; to restricting it to certain models, e.g., requiring that data be used in only one-year forecasts. In addition, DSS outputs may be supplemented with data from other information systems.

Third, organizational procedures for collecting data and data compatibility must be reviewed to ensure that collected data are accurate, timely, and complete. The organizational procedures include those for information collection, analysis, and dissemination and may be outdated, inefficient, or even serve to introduce noise into the dataset. The review of data compatibility, on the other hand, should be carried at the levels of hardware, software, data, procedures and people.

## 3.4. Methods for error detection

In the realm of data communications, there are methods used to detect errors in transmitted data; vertical (parity), longitudinal, and cyclic redundancy checking. The latter is the most complicated and involves the use of a generator polynomial to create and compare the added code at both source and destination. Unequal CRCs signify errors in the data. Error detection may be carried out by the host computer, but increasingly, by communications control devices, such as modems, using recently-developed protocols [13].

Since the problems of data communication and DSS data collection are not exactly the same, it is impossible to have an exact analogy but similar methods exist in the literature for the detection of errors, inaccuracies and incompleteness in data when they occur. Methods that are used to detect unreliability in data usually involve validation against its expected form and include a broad range of testing and validation methods $[12,20]$ , such as;

1. Completeness tests: to verify that all the required data for a set of models has been provided and that it is at the required level of aggregation.

2. Face Validity: involves testing the fit between the model's outputs and the decision maker's expectations of the form of the output.

3. Replication of Reference Models: this compares the results (and implied behavior) of the model with a well-understood reference model to see if it is faithfully reproduced (e.g., diminishing returns on advertising expenditure in a marketing-mix model). While it is unlikely that reference models will be totally applicable in a DSS context with a poorly-understood problem, reference models may be useful in illustrating general (e.g., economic) behavior, depicting a part of the overall problem, or providing a helpful though indirect analogy.

4. Testing for Extreme Conditions: the collected data may be tested to ensure that it is does not exceed upper and/or lower limits. These might pertain to the characteristics of the data itself, such as length and type of the field or to its content; e.g., a person's age being less than 100. In DSS use, these 'outliers' should be flagged for the user's attention, as they may signal environmental changes (e.g., workers over 65 years of age or loss of agricultural production in areas now used for homes).

## 3.5 Methods of error correction

Drawing from the data communications context, certain methods are directly transferable into that of DSS data collection. These include: data retransmission (up to a specified retry limit), data modification, and rerouting. In synchronous data transmission for example, where data are transmitted one block at a time, the detection of an error would typically result in an 'automatic request for retransmission' or ARQ message to the sender. The sender then retransmits the individual block up to a specified retry limit (anywhere between 3 and 100), and if still unsuccessful, will cease data transmission temporarily. Only if an error-correcting code is included (a relatively rare practice) will data modification be attempted.

Retransmission in the context of DSS data collection will involve collection of a new dataset if the existing dataset is found to be unreliable. This may be primary data, in which case a further survey may be required, or secondary data in which case the data may be obtained from another source. Interestingly enough, in the DSS context, primary data collection may often prove to be prohibitively expensive. Data triangulation, a method used to create a composite picture of a phenomenon under study, is often employed to generate a higher level of confidence in the final dataset than in its constituent parts [12].

Modification of the collected data are the second method of correcting errors detected in the body of data. These methods would include using the data filters, as previously mentioned, to improve the quality of the data and ensure that it meets the specifications of the DSS models. An example of this procedure includes the use of statistical techniques to flag, and if necessary, remove freak observations (e.g., those resulting from one-off events, such as a labor strike, catastrophe, etc.), and compensating for skewness in a data distribution. This is often used, particularly for primary data, as the cost of further collection may be prohibitive.

Modification may also be needed, not to correct intrinsic accuracies in the dataset, but to transform it into a required format. An example of this is the deseasonalization of data characterized by seasonal or cyclical effects. Deseasonalization might be carried out as part of a forecasting method, as with time series decomposition, or performed prior to the use of other forecasting methods, such as exponential smoothing etc. [15]. Seasonally adjusted data should always clearly be indicated as such.

![](/api/attachments/6EWQ9294/fulltext/images/d024bf4063f488789159fcb73d49d9f57b4b9b3d4648acddca82cd32f67139c9.jpg)  
Fig. 3. Extended DSS configuration.

Forecasting methods themselves are also a form of data modification, used when the dataset is accurate but out of date. If current data are unavailable then a forecast may be made to create a more accurate dataset. Sales and population estimates are good examples of the use of forecasting techniques to improve a dataset. Again, forecasted data should clearly be labeled as such, and accompanied by an indication of the assumptions used in making the forecast, and the forecasting method used.

The final technique of rerouting involves the collection of data from another source. Little and Cassetari [14] point out that data supplied by say, AC Nielson may be unusable for showing very recent changes in sales. In this case, the required data may be obtained from another organization (e.g., SAMI), whose data show up sales trends quicker.

## 4. A DSS model with extensions for data capture

DSS have undergone extensive use in ill-structured and 'tough' managerial problems that had resisted earlier information system approaches, such as traditional Data Processing and MIS. These model-based systems have been required to be more flexible and adaptable, and to use information from a wider variety of sources to support managerial decision-making, usually at higher organizational levels. DSS, which focus on more strategic-oriented activities, tend to be more 'extroverted' in outlook than conventional MIS in their interaction with external systems and the associated collection and transformation of data for the DSS database.

Figure 3 illustrates the various DSS components required to capture and maintain DSS data effectively. Internal and external data sources are shown to be susceptible to certain types of error during data capture. This data capture is performed by the data extraction facility, which subsequently transforms the data into a format compatible with the DSS database. Functions for the prevention, detection, and correction of errors in the data are shown as integral components of the DSS data extraction system.

A procedure for employing the framework of data-related problems and the taxonomy of solutions is also required, to enable both the DSS developer and user to anticipate, assess, and adequately handle encountered problems with poor-quality data. Using a tabular representation as an analysis tool, a seven step procedure is presented below. This has been used in an actual case study.

1. Set up in a tabular format, for all the datasets involved, the error types, and the methods for error handling (prevention, detection and correction).

2. Examine the initial dataset to see if data retransmission, new data collection, and/or data triangulation is required, due to unreliability, incompleteness etc.

3. If required, collect data from other sources for data triangulation.

4. Recreate the table of datasets from Step (1), noting the remaining problems and associated methods for error handling.

5. Examine and select error handling techniques based on cost/effectiveness criteria.

6. Apply error-handling techniques.

7. If the results are still unsatisfactory, reiterate through Step (2).

Use of this procedure is now demonstrated by means of an example from the context of industrial marketing.

## 5. A case study

The case study described in this section is based on a problem, involving a company in Great Britain (under the acronym, HLX) engaged in developing and selling specialized software. This software may be viewed as an industrial or business product purchased primarily by other organizations for use in value-added products. The market was dominated by a small set of major competitors, about whom initial sales figures were only available from press reports and statements made in the trade literature. The product manager suspected that these data were exaggerated, and two market surveys failed to dispel his disquiet or provide a fit to his perceptions of the market.

Table 1  
Initial estimates of competitor market share

<table><tr><td>Firm</td><td>Units Sold</td><td>List Price ($)</td><td>Revenue ($)</td><td>Market Share</td></tr><tr><td>EXP</td><td>800</td><td>1,838</td><td>1,470,000</td><td>42.9%</td></tr><tr><td>ESI</td><td>1,000</td><td>882</td><td>882,000</td><td>25.7%</td></tr><tr><td>ISI</td><td>150</td><td>4,410</td><td>661,500</td><td>19.3%</td></tr><tr><td>HLX</td><td>100</td><td>2,039</td><td>203,900</td><td>5.9%</td></tr><tr><td>IEV</td><td>100</td><td>1,022</td><td>102,200</td><td>3.0%</td></tr><tr><td>Others</td><td>150</td><td>735</td><td>110.250</td><td>3.2%</td></tr></table>

While three of the major competitors had been in this market for several years, one competitor was a recent addition to the field (in the previous 3 months). The results of an initial market investigation by the authors using immediately available data sources is shown in Table 1. This was based entirely on the trade literature and market surveys and defines five market leaders, plus a Sixth category, aggregating the smaller players. The sales estimates for each firm ranged from approximately \$1.47 million on sales of 800 units for the market leader, to \$102,200 on sales of 100 units, for the smallest of the market leaders. HLX placed fourth in sales revenues, with \$203,900 in sales, and an estimated 5.9% market share (see Table 1).

The first-cut dataset was received skeptically by the product manager and the DSS developer, who felt that the sales figures reported by HLX's competitors were exaggerated. In this new market, the sales figures were suspected of being subject to intentional distortion, with no attention paid to their verification by either the trade press or the market surveys. In addition, the product manager felt that sales of the company's package were distinctly seasonal in nature, paralleling the regional software sales pattern. The first iteration of the procedure used techniques shown in Table 2.

Table 2  
The initial dataset

<table><tr><td rowspan="2">Error Type</td><td rowspan="2">Initial Sales Data Set</td><td colspan="3">Error Handling Methods</td></tr><tr><td>Prevention</td><td>Detection</td><td>Correction</td></tr><tr><td rowspan="3">Noise</td><td>Competitive sales subject to suspected inflation</td><td></td><td></td><td rowspan="2">Collect new Dataset</td></tr><tr><td>Response functions for marketing mix model</td><td></td><td></td></tr><tr><td>Difficulty In verifying figures from the trate literature</td><td></td><td></td><td>Collect New Dataset</td></tr><tr><td>Delay/ Distortion</td><td>Second-hand survey data</td><td></td><td></td><td>Collect New Dataset</td></tr></table>

Table 3  
Second-cut data analysis

<table><tr><td rowspan="2">Error Type</td><td rowspan="2">Initial Sales Data Set</td><td colspan="3">Error Handling Methods</td></tr><tr><td>Prevention</td><td>Detection</td><td>Correction</td></tr><tr><td rowspan="4">Noise</td><td>Enhanced sales figures</td><td></td><td></td><td></td></tr><tr><td>Uncertainty reduced by data triangulation</td><td></td><td></td><td></td></tr><tr><td>Outdated sales data</td><td></td><td></td><td>Forecasting</td></tr><tr><td>Response function for marketing mix model</td><td></td><td>Replication of reference modelsFace validityDelphi methods</td><td></td></tr><tr><td>Data Synchronization</td><td>Seasonal sales factor</td><td></td><td></td><td>Modification (Forecasting)</td></tr><tr><td>Delay/Distortion</td><td>Second-hand survey enhanced by primary Data collection</td><td></td><td></td><td></td></tr></table>

Based on the initial statement of error types, the DSS developer (i.e., one of the authors) chose to collect new datasets from different sources (data retransmission and triangulation), due to the high level of unreliability perceived in the initial market data. The developer also elected to make direct enquiries to the competitor sales departments to elicit information relating to their products and sales figures. In addition, public domain documentation relating to the competitors was also collected (e.g., annual financial statements) and analyzed to match reported sales in the trade literature and extrapolated sales from the statements. These datasets were then used to create an improved, composite picture of sales data for the competing firms.

This first iteration resulted in substantial reductions in sales estimates for the competing firms, as triangulation of the additional data sources indicated they were much lower (from the direct enquiries to sales departments), and limits on maximum achievable sales, inferred from annual financial statements. Additionally, individual revenues for three of the competitors were further revised downwards when it was found that substantial, but unadvertised, discounting from list price was practiced.

Following the creation of the more reliable dataset, further problems were handled, as shown in Table 3. The seasonal sales effect was used to modify sales data following their capture. In addition, it was realized that the marketing-mix model required a sales forecast for the succeeding year, so a forecasting method was used to 'correct' (using extrapolation) the sales figures, taking into account the startup competitor, for whom sales figures existed for only a part of the year.

For the calibration of response functions in the marketing-mix model, the DSS developer used a judgmental forecasting technique, namely the jury of executive opinion, via the manager and salespersons; and validation techniques (e.g., face validity, reference models) to ensure accurate model calibration. The jury of executive opinion and Delphi methods are often useful in the absence of hard data, providing a consensus of expert opinion [6]. Alternatively, particularly for the single user, more rigorous methods for model calibration include conjoint analysis, analytical hierarchical process (AHP), and repertory grid analysis [12].

Following the second iteration, the final dataset for use by the DSS is shown in Table 4. This table shows the five major competitors and a composite grouping of the market's minor players. However, the adjustments made during the use of the procedure changed the perceived size of the market and competitor rankings dramatically. The overall size of the market was assessed to be about $60\%$ less than originally estimated (i.e., \$1.37 million), and HLX moved up one place in the competitive rankings (its exact revenues and sales being available in the first iteration). The market share for HLX was also adjusted, from $5.9\%$ to $14.9\%$ . The data shown in Table 4, resulting from the use of the advanced procedure, were then used by the DSS to test the effects of market actions, and to indicate effective marketing strategies [see 3]. While proper validation of a framework requires a substantial number of successful implementations, the high degree of satisfaction expressed by management in this case provides some indication, though anecdotal only, of the viability of our approach.

A marketing-mix decision, of the type discussed here, will rarely be of the one-off variety, but a recurring one, to be continually monitored and adjusted. This factor might lend itself to the use of a knowledge based system which would be able to lead the product manager through the procedure and show the different methods available.

Table 4  
Final estimates of competitor market share

<table><tr><td>Firm</td><td>Units Sold</td><td>Discounted Price ($)</td><td>Revenues ($)</td><td>Market Share</td></tr><tr><td>EXP</td><td>480</td><td>1,020</td><td>489,686</td><td>35.7%</td></tr><tr><td>ISI</td><td>100</td><td>3,307</td><td>330,750</td><td>24.1%</td></tr><tr><td>HLX</td><td>100</td><td>2,309</td><td>203,900</td><td>14.9%</td></tr><tr><td>ESI</td><td>250</td><td>662</td><td>165,375</td><td>12.1%</td></tr><tr><td>IEV</td><td>70</td><td>1,022</td><td>71,540</td><td>5.2%</td></tr><tr><td>Others</td><td>150</td><td>735</td><td>110,250</td><td>8.0%</td></tr></table>

## 5.1. Implementation considerations

Although this framework was tested by one of the authors in a real world setting, an effective implementation of the framework needs work beyond what has been presented here. The problem of dealing with noisy or corrupted data is not well defined or structured, and the problem description varies in every situation. User input at every stage of the framework is correspondingly very critical, therefore it will be unwise to try to automate the whole process. The implementation of the framework should rather look at providing the users with maximum guidance on error detection and error correction procedures. Another complicating factor is the cost of cleaning the corrupt data. It is difficult to do traditional cost benefit analysis to find out the benefit of cleaning data or what is the optimal level of noise in a DSS dataset given all constraints.

Time is another important dimension in this process. As the value of data recedes with time, the consequent effectiveness of decisions based the data diminishes. As a result, a trade-off exists between making a quick decision with noisy data or a delayed decision (presumably more accurate) with better data. Some circumstances may not give the DSS developer a chance to filter the noisy data.

The environment is another critical factor in this implementation process. Environments may be categorized as internal or external. internal factors include top management support for this procedure. External factors include the volatility of the industry or marketplace. The more volatile the environment, the more difficult it is to clean the noisy data. A related factor is the robustness or sensitivity of the DSS to variations in data. If the model is insensitive to data variation within a certain range, then it provides an indication of the level of noise that can be tolerated without compromising the DSS final output.

One potential difficulty in implementing this framework is the problem of assuring that correct data are not termed as corrupted, and at the same time, noisy data are not treated as correct (these may be termed type I and type II errors). Controlling one error increases the likelihood of the other type. Some established guidelines are needed to control these two errors and to understand the impact of these errors for every problem.

With regard to modeling requirements, capabilities over and above those utilized by most DSS DBMS's will be required. Data analysis tools will be needed to detect inaccuracies and incompleteness in collected data, and other models, such as forecasting, sensitivity analysis, trend-smoothing, and descriptive statistical models employed to assess data quality. The validation techniques above are useful for testing the quality of data used for model calibration.

The benefits offered by this approach are in the form of a procedure that enables developers and users to anticipate and handle data-related problems in DSS calibration. This is expected to lead to improvements in data quality and to measurable performance benefits. As the case study (which is based on an actual setting) illustrates, a radically different and more accurate understanding of a market or other phenomenon may be produced using this procedure. Since even minimal improvements to forecasting accuracy may yield large benefits to a firm, identical benefits may be produced by the use of this and similar procedures for DSS data requirements analysis.

## 6. Conclusions

Many DSS developers are fortunate enough to develop DSS in environments characterized by a wealth of reliable data sources. Examples include DSS for consumer marketing applications, and DSS employing primarily organizational data. The latter type include institutionalized DSS, which often have available, good-quality, and verifiable organizational data. In these cases, the developer's energies may be focused on developing other system features, namely data management, modeling capabilities, and the user interface.

This paper has presented a framework and procedure for developing DSS in less tractable and noisy environments, in which data collection for the DSS database is correspondingly more difficult. Using analogies of methods employed in the data communications realm, a framework for anticipating and handling errors in DSS data collection was outlined. The framework and associated procedure may be used by the developer to realize improvements in the quality of data captured in the DSS database.

The method described for improving the quality of DSS data may, additionally, be incorporated within the DSS itself. Roles that the DSS may play in data collection will range from the identification of data-related problems, to the proposal of alternative techniques to improve data collection. Both of these roles may be served by a knowledge based subsystem which will produce the diagnostics. Developing such capabilities represents one aspect of continuing research. Further research directions involve refining the presented framework, applying it to a wider range of DSS applications, and testing and measuring its effectiveness.

Acknowledgements: We are thankful to Dr. E.H. Sibley and the two anonymous reviewers for their assistance in improving the quality of the manuscript.

## References

[1] Alter, S.L., Decision Support Systems: Current Practice and Continuing Challenges, Addison Wesley, Reading, MA, 1980.

[2] Ariav, G. and Ginzberg, M.J., “DSS Design: A Systemic View of Decision Support”, Communications of the ACM, Vol. 28, No. 10, October 1985, pp. 1045–1053.

[3] Arinze, O.B. “Market Planning with Computer Models: A Case Study in the Software Industry”, Industrial Marketing Management, Vol. 19, May 1990, pp. 117–129.

[4] Donovan, J.J. and Madnick, S.E. “Institutional and Ad Hoc DSS and their Effective Use”, Data Base, Vol. 8, No. 3, Winter 1977, pp. 79–88.

[5] Garnto, C. and Watson, H.J. An Investigation of Database Requirements for Institutional and Ad-Hoc DSS, In: Sprague, R.H. and Watson, H.J., eds., Decision Support Systems: Putting Theory into Practice, Prentice Hall, Englewood Cliffs, NJ, 1986.

[6] Georgoff, D.M. and Murdick, R.G., “Manager’s Guide to Forecasting”, Harvard Business Review, January–February 1986, pp. 110–120.

[7] Gerrity, Jr., T.P. "Design of Man-Machine Systems: An Application to Portfolio Management", Sloan Management Review, Vol. 14, Winter 1971, pp. 59–75.

[8] Hirouchi, T. and Kosaka, T. “An Effective Database Formation for Decision Support Systems”, Information and Management, Vol. 7, 1984, pp. 183–195.

[9] Jerrell, E.M. and Morgan, J.N., “Communications Cost under Alternative Distributed Database Configurations”, Information and Management, Vol. 16, 1989, pp. 19–29.

[10] Keen, P.G.W., “Adaptive Design for Decision Support Systems”, Data Base, Vol. 12, No 1–2, 1980, pp. 15–28.

[11] Keen, P.G.W. and Scott Morton, M. Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[12] Lilien, G.L. and Kotler, P. Marketing Decision Making: A Model-Building Approach, Harper and Row, New York, 1983.

[13] Lindsay, G., “Lining up for Error-Free Data”, Systems International, Vol. 17, No. 5, May 1989, pp. 53–58.

[14] Little, J.D. and Cassettiari, M.N. Decision Support Systems for Marketing Managers, AMA management briefing, Management Decision Systems, Place?, 1984.

[15] Makridakis, S., Andersen, A., Carbone, R., Fildes, R., Hibon, M., Lewandowski, R., Newton, J., Parzen, E. and Winkler, R. “The Accuracy of Extrapolation (Time Series) Methods: Results of a Forecasting Competition”, Journal of Forecasting, Vol. 1, pp. 111–153, 1982.

[16] Reimann, B.C. and Waren, A.D. "User-Oriented Criteria for the Selection for the Selection of DSS Software", Communications of the ACM, Vol. 28, No. 2, February 1985, pp. 166–179.

[17] Sage, A., Galing, B. and Lagomasino, A. “Methodologies for Determination of Information Requirements for Decision Support Systems”, Large Scale Systems, Vol. 5, 1983.

[18] Sol, H.G. “Aggregating Data for Decision Support”, Decision Support Systems, Vol. 1, 1985, pp. 111–121.

[19] Sprague, R.H. and Carlson, E.D. Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[20] Stabell, C.B., A Decision-Oriented Approach to Building DSS, in: Bennet, J.L., ed., Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983.

[21] Stallings, W. “Local Networks”, Computing Surveys, Vol. 16, No. 1, March 1984, pp. 3–41.

[22] Stamper, D.A. Business Data Communications, Benjamin/Cummings, Redwood City, CA, 1989.

[23] Stecher, P. and Hellemaa, P. “An ‘Intelligent’ Extraction and Aggregation Tool for Company Data Bases”, Decision Support Systems, Vol. 2, 1986, pp. 145–158.

[24] Summers, R.C. “Local Area Distributed Systems”, IBM Systems Journal, Vol. 28, No. 2, 1989, pp. 227–240.

[25] Turban, E. Decision Support and Expert Systems, Macmillan, NY, 1990.

[26] Young, L.F. Decision Support and Idea Processing Systems, Brown, Dubuque, IA, 1989.
