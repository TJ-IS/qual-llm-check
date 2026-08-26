---
otero_id: 22118
otero_key: "9UF5224Z"
title: "AIMQ: a methodology for information quality assessment"
authors: "Yang W. Lee; Diane M. Strong; Beverly K. Kahn; Richard Y. Wang"
year: "2002"
journal: "Information & Management"
doi: "10.1016/s0378-7206(02)00043-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# AIMQ: a methodology for information quality assessment

Yang W. Lee<sup>a</sup>, Diane M. Strong<sup>b</sup>, Beverly K. Kahn<sup>c</sup>, Richard Y. Wang d,\*

<sup>a</sup>College of Business Administration, Northeastern University, Boston, MA, USA

<sup>b</sup>Worcester Polytechnic Institute, Management Department, Worcester, MA, USA

<sup>c</sup>Sawyer School of Management, Suffolk University, Suffolk, VA, USA

<sup>d</sup>MIT, UC, Berkerley and Boston University, Boston, MA, USA

Received 16 July 1999; received in revised form 28 May 2001; accepted 8 November 2001

## Abstract

Information quality (IQ) is critical in organizations. Yet, despite a decade of active research and practice, the field lacks comprehensive methodologies for its assessment and improvement. Here, we develop such a methodology, which we call AIM quality (AIMQ) to form a basis for IQ assessment and benchmarking. The methodology is illustrated through its application to five major organizations. The methodology encompasses a model of IQ, a questionnaire to measure IQ, and analysis techniques for interpreting the IQ measures. We develop and validate the questionnaire and use it to collect data on the status of organizational IQ. These data are used to assess and benchmark IQ for four quadrants of the model. These analysis techniques are applied to analyze the gap between an organization and best practices. They are also applied to analyze gaps between IS professionals and information consumers. The results of the techniques are useful for determining the best area for IQ improvement activities. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Information quality; Information quality assessment; Information quality benchmarking; Information quality analysis; Information quality improvement; Total Data Quality Management (TDQM)

## 1. Introduction

Information quality (IQ) has become a critical concern of organizations and an active area of Management Information Systems (MIS) research. The growth of data warehouses and the direct access of information from various sources by managers and information users have increased the need for, and awareness of, highquality information in organizations. MIS researchers have always considered the quality of information to be important. A survey of the variables used to measure IS success reported IQ as one of the six categories commonly employed in MIS research [11]. Over the last decade, IQ research activities have increased significantly to meet the needs of organizations attempting to measure and improve the quality of information [4–7,9,15,19,21,22,34–36,38,39]. In industry, IQ has been rated regularly as a top concern in data warehousing projects [8,12,27,32].

Despite a decade of research and practice, only piece-meal, ad hoc techniques are available for measuring, analyzing, and improving IQ in organizations. As a result, organizations are unable to develop comprehensive measures of the quality of their information and to benchmark their efforts against that of other organizations. Without the ability to assess the quality of their information, organizations cannot assess the status of their organizational IQ and monitor its improvement. The research challenge is to develop an overall model with an accompanying assessment instrument for measuring IQ. Furthermore, techniques must be developed to compare the assessment results against benchmarks and across stakeholders. Such techniques are necessary for prioritizing IQ improvement efforts.

Our research was designed to meet these challenges. We developed a methodology called AIM quality (AIMQ) that provided a rigorous and pragmatic basis for IQ assessments and benchmarks. Its first component is a $2 \times 2$ model or framework of what IQ means to information consumers and managers [18]. This model has four quadrants, depending on whether information is considered to be a product or a service, and on whether the improvements can be assessed against a formal specification or customer expectation.

The second component is a questionnaire for measuring IQ along the dimensions of IQ important to information consumers and managers. Several of these dimensions together measure IQ for each quadrant of the 2 - 2 model. This instrument can be applied to assess the quality of information in organizations.

The third component of AIMQ consists of two analysis techniques for interpreting the assessments captured by the questionnaire. These two techniques help organizations focus their IQ improvement efforts on the analysis of their IQ assessments. The first technique compares an organization’s IQ to a benchmark from a best-practices organization. The second technique measures the distances between the assessments of different stakeholders of an information production system.

Each component of the AIMQ methodology has merit in itself. For example, IQ can be assessed using the validated questionnaire and, therefore, it furthers research in IS success. The key contribution of the overall research, however, stems from the integration and synthesis of these components. Properly applied, together they form an effective methodology for assessing IQ in various organizational settings where decisions must be made to prioritize tasks and allocate resources for IQ improvement.

Table 1  
The academics’ view of information quality

<table><tr><td></td><td>Intrinsic IQ</td><td>Contextual IQ</td><td>Representational IQ</td><td>Accessibility IQ</td></tr><tr><td>Wang and Strong [39]</td><td>Accuracy, believability, reputation, objectivity</td><td>Value-added, relevance, completeness, timeliness, appropriate amount</td><td>Understandability, interpretability, concise representation, consistent representation</td><td>Accessibility, ease of operations, security</td></tr><tr><td>Zmud [41]</td><td>Accurate, factual</td><td>Quantity, reliable/timely</td><td>Arrangement, readable, reasonable</td><td></td></tr><tr><td>Jarke and Vassiliou [16]</td><td>Believability, accuracy, credibility, consistency, completeness</td><td>Relevance, usage, timeliness, source currency, data warehouse currency, non-volatility</td><td>Interpretability, syntax, version control, semantics, aliases, origin</td><td>Accessibility, system availability, transaction availability, privileges</td></tr><tr><td>Delone and McLean [11]</td><td>Accuracy, precision, reliability, freedom from bias</td><td>Importance, relevance, usefulness, informativeness, content, sufficiency, completeness, currency, timeliness</td><td>Understandability, readability, clarity, format, appearance, conciseness, uniqueness, comparability</td><td>Usableness, quantitativeness,  $convenience\ of\ access^a$ </td></tr><tr><td>Goodhue [14]</td><td>Accuracy, reliability</td><td>Currency, level of detail</td><td>Compatibility, meaning, presentation, lack of confusion</td><td>Accessibility, assistance, ease of use (of h/w, s/w), locatability</td></tr><tr><td>Ballou and Pazer [4]</td><td>Accuracy, consistency</td><td>Completeness, timeliness</td><td></td><td></td></tr><tr><td>Wand and Wang [37]</td><td>Correctness, unambiguous</td><td>Completeness</td><td>Meaningfulness</td><td></td></tr></table>

<sup>a</sup>Classified as system quality rather than information quality by Delone and McLean.

## 2. Dimensions of IQ

In our earlier research, we empirically derived the IQ dimensions that are important to information consumers (people who use information), using methods traditionally employed in market research. These formed a foundation for our current research. Specifically, our questionnaire includes items to measure IQ as derived in that earlier research (Table 1).

We also grouped the IQ dimensions into four IQ categories, intrinsic IQ, contextual IQ, representational IQ, and accessibility IQ (Table 1). Intrinsic IQ implies that information has quality in its own right. Contextual IQ highlights the requirement that IQ must be considered within the context of the task at hand; it must be relevant, timely, complete, and appropriate in terms of amount, so as to add value. Representational and accessibility IQ emphasize the importance of computer systems that store and provide access to information; that is, the system must present information in such a way that it is interpretable, easy to understand, easy to manipulate, and is represented concisely and consistently; also, the system must be accessible but secure.

Our follow-up research has provided further evidence that these dimensions provide comprehensive coverage of the multi-dimensional IQ construct. For example, a follow-on qualitative study of IQ improvement projects in organizations used these dimensions as the codes in content analysis of the organizational attention to different aspects of IQ during improvement projects. All IQ aspects in the projects were covered by the IQ dimensions.

## 2.1. Academics’ view of IQ dimensions

Table 1 summarizes academic research on the multiple dimensions of IQ. The first row is our study, which takes an empirical, market research approach of collecting data from information consumers to determine the dimensions of importance to them. The second row of Table 1 list the dimensions uncovered in Zmud’s pioneering IQ research study [41], which considers the dimensions of information important to users of hard-copy reports. Because of the focus on reports, information accessibility dimensions, which are critical with on-line information, were not relevant.

In contrast to these empirically developed dimensions, the next three studies developed their IQ dimensions from existing literature. The Jarke and Vassiliou [16] study modified the Wang–Strong dimensions in their study of data warehouse quality. The first dimension in each of the four categories is their overall label for that category. Delone and McLean’s review of the MIS literature during the 1980s reports 23 IQ measures from nine previous studies. Four of these studies include only one measure of IQ, either importance or usefulness. Two studies, one of which is the wellknown user satisfaction study by Bailey and Pearson [3], include nine measures. Goodhue’s dimensions [14] are developed from a literature review to find the characteristics of information that are important to managers who use quantitative data stored in computer systems. In Goodhue’s study, the importance of the dimensions in the accessibility IQ category is apparent.

The last two rows present two studies that focus on a few dimensions that can be measured objectively, rather than a comprehensive list of dimensions important to information consumers. Ballou and Pazer’s study focuses primarily on intrinsic dimensions that can be measured objectively. They use four dimensions that frequently appear in IQ studies: accuracy, consistency, completeness, and timeliness. While they acknowledge the gap between user expectations for IQ and performance of the IS group in delivering IQ, their research does not specifically address the contextual and more subjective IQ dimensions. The Wand and Wang [37] study takes an ontological approach and formally defines four IQ dimensions: correctness, unambiguous, completeness, and meaningfulness. The quality along these four dimensions can be assessed by comparing values in a system to their true real world values.

In comparing these studies two differences are apparent. One is whether the viewpoint of information consumers is considered, which necessarily requires the inclusion of some subjective dimensions. The other is the difficulty in classifying dimensions, for example, completeness, and timeliness. In some cases, such as in the Ballou and Pazer study, the completeness and timeliness dimensions fall into the intrinsic IQ category, whereas in the Wang and Strong study, these dimensions fall into the contextual IQ category. As an intrinsic dimension, completeness is defined in terms of any missing value. As a contextual dimension, completeness is also defined in terms of missing values, but only for those values used or needed by information consumers.

In summary, the academic research included several types of studies. One provided overall coverage for the IQ construct by empirically developing the dimensions from information consumers, such as in the Wang and Strong study. Zmud’s study was an early empirical effort based on hard-copy reports. Another type developed their dimensions from literature reviews, i.e. the Delone and McLean, Goodhue, and Jarke and Vassiliou studies. By grouping all measures from other authors together, they hoped to cover all aspects of the IQ construct. The third type of study focused on a few dimensions that can be objectively defined, e.g. Ballou and Pazer, and Wand and Wang.

## 2.2. Practitioners’ view of IQ dimensions

Practitioners have reported the dimensions and measures they use within organizations. The approach is generally not rigorous from a research viewpoint, but it provides some insight into their views. IQ practitioners include specialists within organizations, outside consultants, and vendors of products. Because they focus on specific organizational problems, coverage of all IQ properties is not their primary intent.

Table 2 presents a sampling of practitioner IQ research. The Department of Defense (DoD) Guideline for data quality adopts define, measure, analyze, and improve as the four phases in a continuous life cycle, as advocated by the MIT Total Data Quality Management (TDQM) Program. In this effort, the DoD program focuses on the accuracy, completeness, consistency, validity, timeliness, and uniqueness dimensions of IQ.

Mitre has an active IQ improvement effort, based on the IQ dimensions [39]. One of their recent studies [25] reported that 35% of user concerns about IQ are accessibility issues, 27% intrinsic issues, 24% contextual issues, and 14% representational issues.

The practitioners’ view of information quality

<table><tr><td></td><td>Intrinsic IQ</td><td>Contextual IQ</td><td>Representational IQ</td><td>Accessibility IQ</td></tr><tr><td>DoD [10]</td><td>Accuracy, completeness, consistency, validity</td><td>Timeliness</td><td>Uniqueness</td><td></td></tr><tr><td>MITRE [25]</td><td>Same as [39]</td><td>Same as [39]</td><td>Same as [39]</td><td>Same as [39]</td></tr><tr><td>IRI [20]</td><td>Accuracy</td><td>Timeliness</td><td></td><td>Reliability (of delivery)</td></tr><tr><td>Unitech [23]</td><td>Accuracy, consistency, reliability</td><td>Completeness, timeliness</td><td></td><td>Security, privacy</td></tr><tr><td>Diamond Technology Partners [24]</td><td>Accuracy</td><td></td><td></td><td>Accessibility</td></tr><tr><td>HSBC Asset Management [13]</td><td>Correctness</td><td>Completeness, currency</td><td>Consistency</td><td>Accessibility</td></tr><tr><td>AT&amp;T and Redman [29]</td><td>Accuracy, consistency</td><td>Completeness, relevance, comprehensiveness, essentialness, attribute granularity, currency/cycle time</td><td>Clarity of definition, precision of domains, naturalness, homogeneity, identifiability, minimum unnecessary redundancy, semantic consistency, structural consistency, appropriate representation, interpretability, portability, format precision, format flexibility, ability to represent null values, efficient use of storage, representation consistency</td><td>Obtainability, flexibility, robustness</td></tr><tr><td>Vality [8]</td><td></td><td></td><td>Metadata characteristics</td><td></td></tr></table>

Table 3

Of the accessibility issues, 43% of the problems were due to ease of operations. This supports our findings that accessibility is an increasingly important component.

Information Resources Inc., a supplier of information to other organizations, is concerned about ensuring the quality of the information it delivers as well as the reliability of the delivery, since that is the source of their value [20]. They have developed their TRAQ (timeliness þ reliability þ accuracy ¼ quality) model to focus attention on IQ. Unitech, a company that sells IQ software tools, prefers to use the term: information integrity. They employ three key attributes that are intrinsic to the concept of information integrity: accuracy, consistency, and reliability. They argue that these capture the essential characteristics of other attributes, such as completeness, timeliness, security, and privacy [23].

Diamond Technology Partners, a consulting company that builds data warehouses, focuses on accuracy and accessibility as the IQ dimensions against which they assess the quality of information in their data warehouses [24]. Another data warehouse company focuses on attributes of IQ that are important to users, including correctness, completeness, consistency, currency, and accessibility [13].

Based on work at AT&T, Redman [29] provided a comprehensive list of IQ attributes. It includes many representational attributes, e.g. naturalness of the representation. Much of his work has involved large databases that must work together consistently, thus, concerns about data representation are important. As a result, fewer of his attributes focus on concerns of end users. Vality also focuses on representational attributes for scrubbing and combining data across multiple sources for input into data warehouses.

The IQ dimensions employed by practitioners are driven by the context in which they are delivering IQ—more than does the research of academics. In the sample of studies in Table 2, the contexts include: data warehouse development, IQ tools for improving the quality of data input to databases, environments with multiple incompatible databases, and environments in which timely delivery of information is critical. The context influences the dimensions selected. For example, in a context of multiple incompatible databases, representational dimensions are more important.

## 3. The PSP/IQ model

The foundation of the AIMQ methodology is a model and a set of IQ dimensions that cover aspects of IQ that are important to information consumers. The PSP/IQ model organizes the key IQ dimensions so that meaningful decisions can be made about improving IQ. More importantly, these dimensions are developed from the perspective of information consumers and, therefore, are a logical choice.

The AIMQ methodology consists of the following three components:

 the PSP/IQ model;

 the IQA instrument;

 the IQ Gap Analysis techniques.

The PSP/IQ model consolidates the dimensions into four quadrants: sound, dependable, useful, and usable information (Table 3). These four quadrants represent IQ aspects that are relevant to IQ improvement decisions. The IQA instrument measures IQ for each of the IQ dimensions. These measures are averaged to form measures for the four quadrants. The IQ Gap Analysis techniques assess the quality of an organization’s information for each of the four quadrants. These gap assessments are the basis for focusing IQ improvement efforts.

For defining the concept of IQ, the four categories (intrinsic, contextual, representational, and accessibility) are useful in ensuring complete coverage of the concept of IQ. These four, however, are not as useful for deciding what to do to improve IQ. The PSP/IQ model’s focus on product or service delivery and on how quality can be assessed by specifications or customer expectations employs quality aspects that are relevant to delivering better quality information. These concepts are consistent with the basic Total Quality Management (TQM) tenets known to IS managers [28,30]. Further details of the PSP/IQ model and its development process can be found in [17,18].

The PSP/IQ model

<table><tr><td></td><td>Conforms to specifications</td><td>Meets or exceeds consumer expectations</td></tr><tr><td rowspan="7">Product Quality</td><td>Sound information</td><td>Useful information</td></tr><tr><td>IQ dimensions</td><td>IQ dimensions</td></tr><tr><td>Free-of-error</td><td>Appropriate amount</td></tr><tr><td>Concise representation</td><td>Relevancy</td></tr><tr><td>Completeness</td><td>Understandability</td></tr><tr><td>Consistent representation</td><td>Interpretability</td></tr><tr><td></td><td>Objectivity</td></tr><tr><td rowspan="6">Service Quality</td><td>Dependable information</td><td>Usable information</td></tr><tr><td>IQ dimensions</td><td>IQ dimensions</td></tr><tr><td>Timeliness</td><td>Believability</td></tr><tr><td>Security</td><td>Accessibility</td></tr><tr><td></td><td>Ease of operation</td></tr><tr><td></td><td>Reputation</td></tr></table>

## 4. IQA instrument development and administration

The development of the IQA instrument followed standard methods for questionnaire development and testing, see for example [26,31].

## 4.1. Item development

The first step was the development of 12–20 items for each of the IQ dimensions. Since these were derived originally from a factor analysis of IQ attributes or phrases, the underlying attributes for each dimension were used in developing them. Most items were of the general form: ‘‘this information is (attribute or phrase).’’ For example, ‘‘this information is presented consistently’’ and ‘‘this information is relevant to our work.’

These items were reviewed by IQ researchers to check that they covered the dimension and did not include ones that overlapped. The items for each dimension were also reviewed by users to check that they are meaningful to information consumers who would be completing the survey. As a result of these reviews, items were added, deleted, and revised. This process of reviewing and editing was repeated until agreement was reached on an initial set of eight items per IQ dimension.

## 4.2. Pilot study

The purpose of the pilot study was to provide an initial assessment of the reliability of the items for each of the dimensions and to use this to reduce the number of items per dimension. Reducing the number of items is important, because the eight items for each dimension, resulting from item development, are too many for practical use. In studies focusing on IQ, several independent variables will also need to be measured. For information systems success studies, IQ is only one component of measuring success.

For the pilot survey, the 120 IQA items were randomly mixed across four pages. The scale used in assessing each item ranged from 0 to 10 where 0 was labeled ‘‘not at all’’ and 10 is labeled ‘‘completely’’. The use of an 11-point scale is based on previous experience with IQ assessment. Results of a previous questionnaire, which used a 1–9 scale, indicate that respondents preferred to use the upper half of the scale. This was confirmed in our interviews of information collectors, information consumers, and IS professionals who preferred to assess their IQ as average or above.

The pilot IQA instrument also included two pages of demographic information. One item of particular interest was the survey respondent’s role in the information production system as a collector of information, a consumer of it in tasks, or as an IS professional. The pilot IQA instrument was printed as an eight-page booklet, six pages of questions, one page for comments and suggestions on the survey, and a final blank page.

The 52 respondents to the pilot Instrument were information collectors, information consumers, and IS professionals in six companies. These are from the financial, healthcare, and manufacturing sectors. In each company, respondents answered the questions for a particular set of information, e.g. their patient information or their production information.

To assess the items for measuring each construct, Cronbach alphas were computed and factor analysis was performed. The results were used to eliminate items that did not add to the reliability of the scale or did not measure the same construct. This resulted in 4– 5 items per dimension, for a total of 65 items to assess IQ along all dimensions.

## 4.3. Full study

The full study used the final questionnaire to assess IQ in organizations. The 65 IQA items formed two pages in the final questionnaire. With shortened demographic questions and space for comments, the IQA instrument was printed as a booklet of four pages. The

T<sub>a</sub>bl<sub>e</sub> 4 Di<sub>mens</sub>i<sub>on</sub>-l<sub>eve</sub>l <sub>corre</sub>l<sub>a</sub>ti<sub>ons</sub>

<table><tr><td colspan="2"></td><td>Mean</td><td>S.D.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>1</td><td>Accessibility</td><td>4.75</td><td>2.36</td><td>(0.92)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Appropriate amount</td><td>5.07</td><td>1.96</td><td>0.68**</td><td>(0.76)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Believability</td><td>4.87</td><td>2.25</td><td>0.64**</td><td>0.64**</td><td>(0.89)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>Completeness</td><td>4.82</td><td>2.05</td><td>0.77**</td><td>0.77**</td><td>0.76**</td><td>(0.87)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Concise representation</td><td>4.71</td><td>2.07</td><td>0.75**</td><td>0.59**</td><td>0.71**</td><td>0.74**</td><td>(0.88)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>Consistent representation</td><td>5.27</td><td>2.16</td><td>0.71**</td><td>0.62**</td><td>0.72**</td><td>0.72**</td><td>0.75**</td><td>(0.83)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>Ease of operation</td><td>4.78</td><td>0.95</td><td>0.48**</td><td>0.22**</td><td>0.32**</td><td>0.43**</td><td>0.44**</td><td>0.31**</td><td>(0.85)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>Free-of-error</td><td>4.98</td><td>2.28</td><td>0.63**</td><td>0.64**</td><td>0.91**</td><td>0.75**</td><td>0.66**</td><td>0.69**</td><td>0.32**</td><td>(0.91)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td>Interpretability</td><td>5.05</td><td>1.87</td><td>0.72**</td><td>0.59**</td><td>0.68**</td><td>0.68**</td><td>0.73**</td><td>0.70**</td><td>0.30**</td><td>0.67**</td><td>(0.77)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>Objectivity</td><td>5.88</td><td>2.04</td><td>0.49**</td><td>0.44**</td><td>0.64**</td><td>0.60**</td><td>0.53**</td><td>0.55**</td><td>0.31**</td><td>0.63**</td><td>0.57**</td><td>(0.72)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11</td><td>Relevancy</td><td>6.58</td><td>2.18</td><td>0.51**</td><td>0.47**</td><td>0.56**</td><td>0.61**</td><td>0.50**</td><td>0.53**</td><td>0.29**</td><td>0.55**</td><td>0.53**</td><td>0.66**</td><td>(0.94)</td><td></td><td></td><td></td><td></td></tr><tr><td>12</td><td>Reputation</td><td>4.49</td><td>2.21</td><td>0.61**</td><td>0.58**</td><td>0.86**</td><td>0.72**</td><td>0.70**</td><td>0.67**</td><td>0.29**</td><td>0.79**</td><td>0.67**</td><td>0.60**</td><td>0.50**</td><td>(0.85)</td><td></td><td></td><td></td></tr><tr><td>13</td><td>Security</td><td>5.65</td><td>2.21</td><td>0.30**</td><td>0.40**</td><td>0.44**</td><td>0.41**</td><td>0.32**</td><td>0.40**</td><td>0.14*</td><td>0.41**</td><td>0.36**</td><td>0.42**</td><td>0.34**</td><td>0.35**</td><td>(0.81)</td><td></td><td></td></tr><tr><td>14</td><td>Timeliness</td><td>4.93</td><td>2.18</td><td>0.69**</td><td>0.68**</td><td>0.73**</td><td>0.71**</td><td>0.66**</td><td>0.64**</td><td>0.29**</td><td>0.72**</td><td>0.63**</td><td>0.56**</td><td>0.50**</td><td>0.70**</td><td>0.34**</td><td>(0.88)</td><td></td></tr><tr><td>15</td><td>Understandability</td><td>5.23</td><td>2.14</td><td>0.72**</td><td>0.58**</td><td>0.70**</td><td>0.68**</td><td>0.77**</td><td>0.73**</td><td>0.37**</td><td>0.66**</td><td>0.87**</td><td>0.62**</td><td>0.55**</td><td>0.69**</td><td>0.38**</td><td>0.64**</td><td>(0.90)</td></tr></table>

C<sub>ron</sub>b<sub>ac</sub>h <sub>a</sub>l<sub>p</sub>h<sub>as</sub> <sub>on</sub> th<sub>e</sub> di<sub>agona</sub>l<sub>s</sub>

<sup>\*</sup> P < 0 : 05 .

<sup>\* \*</sup> P < 0 : 0 1 .

Table 5  
Quadrant-level correlations

<table><tr><td></td><td>Mean</td><td>S.D.</td><td>Soundness</td><td>Dependability</td><td>Usefulness</td><td>Usability</td></tr><tr><td>Soundness</td><td>4.94</td><td>1.90</td><td>(0.94)</td><td></td><td></td><td></td></tr><tr><td>Dependability</td><td>5.29</td><td>1.80</td><td>0.730**</td><td>(0.83)</td><td></td><td></td></tr><tr><td>Usefulness</td><td>5.56</td><td>1.67</td><td>0.871**</td><td>0.728**</td><td>(0.93)</td><td></td></tr><tr><td>Usability</td><td>4.72</td><td>1.64</td><td>0.925**</td><td>0.710**</td><td>0.841**</td><td>(0.94)</td></tr></table>

Cronbach alphas on the diagonals.  
<sup>\*\*</sup> P < 0:01.

only change to the scale was to label the mid-point of the scale, 5, as ‘‘average.’’ The actual questionnaire items are included in the Appendix.

The IQA instrument reliability statistics are from completed surveys from 261 respondents in five organizations. In each organization, there were respondents representing all the information production roles, i.e. information collectors, information consumers, and IS professionals. Each respondent focused his or her answers on one set of information of importance to the organization, e.g. patient information in healthcare organizations.

Statistical analyses were performed using SPSS for Windows. Construct reliability of the IQ dimensions was tested using the Cronbach alpha. The values, which range from 0.94 to 0.72, indicate that the measures of each dimension are reliable. The correlations among the dimensions are reported in Tables 4 and 5, with the Cronbach alpha values on the diagonals.

IQ, although multi-dimensional, is a single phenomenon. As a result, the dimensions are not inherently independent. This dependence among the dimensions eliminates the applicability of path analysis in the validation of the survey. This was confirmed with path analysis using AMOS [2]. Path analysis produced some inadmissible solutions due to high correlations among the dimensions. While these problems can be eliminated by combining dimensions, such a data-driven approach is unacceptable. Thus, the standard Cronbach alpha was used to assess reliability.

## 5. IQ Gap Analysis techniques

The IQA instrument allowed us to assess IQ at the dimension level. For this analysis, we aggregated the dimensions into the PSP/IQ quadrants. Values for each quadrant were computed as the mean of the values of its constituent dimensions. A weighted-average model, using the importance ratings of each dimension, was also investigated. The importance ratings are from a separate survey of information consumers. The weighted model produced the same results as the nonweighted model, since the range of importance weights for the quadrants was 0.232–0.265, which differ little from an equal weighting of 0.25. Thus, the simpler equal-weighted model was used in our analysis.

The Gap Analysis techniques used these quadrant IQ values as their input. These techniques are a set of algorithms for analyzing and comparing the IQAs from the IQA instrument and the PSP/IQ model. They are used to benchmark the quality of an organization’s IQ and to focus improvement activities.

Two analysis techniques, IQ Benchmark Gaps and IQ Role Gaps, are used to identify IQ problem areas. Analysis begins by analyzing a specific quadrant of the PSP/IQ model, such as usability. This continues for the other quadrants. After all four quadrants have been individually analyzed, the four quadrants can be compared to detect common patterns or to focus on the quadrant that most needs to be improved.

## 5.1. Benchmarking Gap Analysis

A common concern in organizations is how well they are doing relative to others. Benchmarking addresses this concern. It is defined as ‘‘a continuous, systematic process for evaluating the products, services, and work processes of organizations that are recognized as representing best practices for the purposes of organizational improvement’’ [33].

Benchmarking is a measurement of products, services, or business practices against tough competitors, industry leaders, or other sources of best practices.

![](/api/attachments/9UF5224Z/fulltext/images/417e2ce5da33b8f352a2330b3aed4216443f0ca6d1cd0890ed616795037e6e06.jpg)  
Fig. 1. An example of the IQ Benchmark Gap.

These best practices form the benchmark against which performance is measured [1,40].

The IQA instrument provides a method of establishing the state of IQ in an organization at a given time. For best-practice organizations, the IQA measurement represents a benchmark against which other organizations can assess their IQ.

The first technique, IQ Benchmark Gaps, assesses an organization’s IQ against a benchmark. This is the IQ assessment of a best-practice organization. Fig. 1 shows an example IQ Benchmark Gap diagram for the usability quadrant using the data from the full study. The y-axis is the level of quality, which can range from 0 to 10. The x-axis is the percentage of respondents, e.g. the level of IQ reported by the bottom 10% of the respondents.

When analyzing IQ Benchmark Gaps, three indicators should be considered:

 size of the gap area;

 location of the gap;

 different size gaps over the x-axis.

There is a substantial gap between the best-practices organization and the four other organizations. Thus, there is room for much improvement in usability IQ for all four organizations. The location of the gap refers to its placement on the y-axis. For example, at 10% the gap is located between 2 and 5.5, whereas at 60%, the gap is located between 4.5 and 7.6. In this case, the size of the gap does not change much for different values of the x-axis. For company 3, however, the size of the gap is smaller after the seventieth percentile. To analyze quadrant differences, we would need similar graphs for the other three quadrants.

## 5.2. Role Gap Analysis techniques

IQ Role Gaps compare the IQ assessments from respondents in different organizational roles, IS professionals, and information consumers. IQ Role Gaps is a useful diagnostic technique for determining whether differences between roles is a source of a Benchmark Gap. The IQ assessment and comparison across roles serves to identify IQ problems and lays the foundation for IQ improvement.

Fig. 2 is an example of the Role Gap for the usability quadrant using the data from the full study. The x-axis is the five organizations, with number one as the best-practices organization. The numbers for the organizations are the same as those used in the Benchmark Gap Analysis. The y-axis is the level of quality, as in the IQ Benchmark Gap. The points in the graph are the mean level of IQ reported by information consumers (diamonds) and the mean level reported by IS professionals (squares). The line between the diamond and the square for a particular organization represented the size of the IQ Role Gap for usability.

![](/api/attachments/9UF5224Z/fulltext/images/bca91128fe59c90bd4d86d7549ab895f6e37e789034092529bf49d272c0ca1cb.jpg)  
Fig. 2. An example of the IQ Role Gap.

When analyzing IQ Role Gaps, three indicators should be considered:

 size of the gap area;

 location of the gap;

 direction of the gap (positive versus negative).

The size of the IQ Role Gap is much greater in organizations two and five, which means that information consumers and IS professionals do not agree about the level of IQ for usability. The location of the gap for the best-practices organization (number one) is around an IQ level of seven, which is quite good; whereas the location of the gap for organization three, which is also small, is around 4.5. Thus, although their size was similar, organization one had much better IQ than organization three. The direction of the gap is defined to be positive when IS professionals assess the level of IQ to be higher than information consumers. Thus, organization five had a large positive gap. The bestpractices organization had a small negative gap.

A large positive gap means that IS professionals are not aware of problems that information consumers are experiencing. In general, organizations with a large positive gap should focus on reducing the problem by gaining consensus between IS professionals and information consumers. If the size of the gap is small, organizations are positioned to improve the quality of their information, since they have consensus about its level. If the size of the gap is small, then the location of the gap should be examined. If the location is high, indicating high IQ, incremental improvements are most appropriate, whereas if the location is low, major improvement efforts have the potential for significant quality improvement.

## 6. Conclusion

We have developed the AIMQ methodology for assessing and benchmarking IQ in organizations. This encompasses three major components: the PSP/IQ model, the IQA instrument, and the Gap Analysis techniques.

Each component of the AIMQ has merit in itself and, therefore, makes a contribution on its own. The PSP/IQ model assesses IQ in terms of conformance to specifications and as exceeding consumer expectations on the one axis and IQ as a product and as a service on the other. It is a management tool for conceptualizing and assessing IQ in business terms. Furthermore, it serves as a theoretical foundation for performing gap analyses.

The IQA instrument provides the measurements underpinning the PSP/IQ model and the gap analyses.

It collects data to assess IQ status along the key IQ dimensions. Valid measures of IQ are critical for further research progress in IQ. The data collected from the IQA are the prerequisite for PSP/IQ modeling and gap analyses.

The gap analysis techniques provide the tools by which organizations can understand their IQ deficiencies as compared to other organizations and to different stakeholders within one organization. Using these analysis techniques, organizations can benchmark their IQ and determine appropriate areas to focus improvement efforts.

The key contribution of the overall research, however, stems from the integration and synthesis of these components. The AIMQ methodology as a whole provides a practical IQ tool to organizations. It has been applied in various organizational settings, such as the financial, healthcare, and manufacturing industries. The methodology is useful in identifying IQ problems, prioritizing areas for IQ improvement, and monitoring IQ improvements over time.

## Appendix A. The measures

All items are measured on a 0 to 10 scale where 0 is not at all and 10 is completely. Items labels with ‘‘(R)’’ are reverse coded.

Accessibility. (4 items, Cronbach’s Alpha ¼ .92) This information is easily retrievable. This information is easily accessible. This information is easily obtainable. This information is quickly accessible when needed. Appropriate Amount. (4 items, Cronbach’s Alpha ¼ .76) This information is of sufficient volume for our needs. The amount of information does not match our needs. (R) The amount of information is not sufficient for our needs. (R) The amount of information is neither too much nor too little. Believability. (4 items, Cronbach’s Alpha ¼ .89) This information is believable. This information is of doubtful credibility. (R)

## Appendix A. (Continued )

This information is trustworthy. This information is credible. Completeness. (6 items, Cronbach’s Alpha ¼ .87) This information includes all necessary values. This information is incomplete. (R) This information is complete. This information is sufficiently complete for our needs. This information covers the needs of our tasks. This information has sufficient breadth and depth for our task. Concise Representation. (4 items, Cronbach’s Alpha ¼ .88) This information is formatted compactly. This information is presented concisely. This information is presented in a compact form. The representation of this information is compact and concise. Consistent Representation. (4 items, Cronbach’s Alpha ¼ .83) This information is consistently presented in the same format. This information is not presented consistently. (R) This information is presented consistently. This information is represented in a consistent format. Ease of Operation. (5 items, Cronbach’s Alpha ¼ .85) This information is easy to manipulate to meet our needs. This information is easy to aggregate. This information is difficult to manipulate to meet our needs. (R) This information is difficult to aggregate. (R) This information is easy to combine with other information. Free of Error. (4 items, Cronbach’s Alpha ¼ .91) This information is correct. This information is incorrect. (R) This information is accurate. This information is reliable. Interpretability. (5 items, Cronbach’s Alpha ¼ .77) It is easy to interpret what this information means. This information is difficult to interpret. (R)

Appendix A. (Continued )

It is difficult to interpret the coded information. (R) This information is easily interpretable. The measurement units for this information are clear.

Objectivity. (4 items, Cronbach’s Alpha ¼ .72) This information was objectively collected. This information is based on facts. This information is objective. This information presents an impartial view.

Relevancy. (4 items, Cronbach’s Alpha ¼ .94) This information is useful to our work. This information is relevant to our work. This information is appropriate for our work. This information is applicable to our work.

Reputation. (4 items, Cronbach’s Alpha ¼ .85) This information has a poor reputation for quality. (R) This information has a good reputation. This information has a reputation for quality. This information comes from good sources.

Security. (4 items, Cronbach’s Alpha ¼ .81) This information is protected against unauthorized access. This information is not protected with adequate security. (R) Access to this information is sufficiently restricted. This information can only be accessed by people who should see it.

Timeliness. (5 items, Cronbach’s Alpha ¼ .88) This information is sufficiently current for our work. This information is not sufficiently timely. (R) This information is not sufficiently current for our work. (R) This information is sufficiently timely. This information is sufficiently up-to-date for our work.

Understandability. (4 items, Cronbach’s Alpha ¼ .90) This information is easy to understand.

## References

[1] S.L. Ahire, D.Y. Golhar, M.A. Waller, Development and validation of TQM implementation constructs, Decision Sciences 27 (1), 1996, pp. 23–51.

[2] J.L. Arbuckle, Amos Users’ Guide, Version 3.6, SmallWaters Corporation, Chicago, IL, 1997.

[3] J.E. Bailey, S.W. Pearson, Development of a tool for measuring and analyzing computer user satisfaction, Management Science 29 (5), 1983, pp. 530–545.

[4] D.P. Ballou, H.L. Pazer, Modeling data and process quality in multi-input, multi-output information systems, Management Science 31 (2), 1985, pp. 150–162.

[5] D.P. Ballou, H.L. Pazer, Designing information systems to optimize the accuracy–timeliness trade off, Information Systems Research 6 (1), 1995, pp. 51–72.

[6] D.P. Ballou, G.K. Tayi, Methodology for allocating resources for data quality enhancement, Communications of the ACM 32 (3), 1989, pp. 320–329.

[7] D.P. Ballou, R.Y. Wang, H. Pazer, G.K. Tayi, Modeling information manufacturing systems to determine information product quality, Management Science 44 (4), 1998, pp. 462– 484.

[8] S.M. Brown, Preparing data for the data warehouse, Proceedings of the Conference on Information Quality, Cambridge, MA, 1997, pp. 291–298.

[9] I. Chengalur-Smith, L.L. Pipino, Proceedings of the Conference on Information Quality, Cambridge, MA, 1998.

[10] P. Cykana, A. Paul, M. Stern, DoD guidelines on data quality management, Proceedings of the Conference on Information Quality, Cambridge, MA, 1996, pp. 154–171.

[11] W.H. Delone, E.R. McLean, Information systems success: the quest for the dependent variable, Information systems research 3 (1), 1992, pp. 60–95.

[12] C.P. Firth, R.Y. Wang, Data Quality Systems: Evaluation and Implementation, Cambridge Market Intelligence Ltd., London, 1996.

[13] E. Gardyn, A Data Quality Handbook For A Data Warehouse, Proceedings of the Conference on Information Quality, Cambridge, MA, 1997, pp. 267–290.

[14] D.L. Goodhue, Understanding user evaluations of information systems, Management Science 41 (12), 1995, pp. 1827– 1844.

[15] K. Huang, Y. Lee, R. Wang, Quality Information and Knowledge, Prentice Hall, Upper Saddle River, NJ, 1999.

[16] M. Jarke, Y. Vassiliou, Data warehouse quality: a review of the DWQ project, Proceedings of the Conference on Information Quality, Cambridge, MA, 1997, pp. 299–313.

[17] B.K. Kahn, D.M. Strong, Product and service performance model for information quality: an update, Proceedings of the Conference on Information Quality, Cambridge, MA, 1998, pp. 102–115.

[18] B.K. Kahn, D.M. Strong, R.Y. Wang. Information quality benchmarks: product and service performance, Communications of the ACM 45 (4ve), April 2002, pp. 184–192.

[19] B. Klein, D. Rossin (Eds.), Proceedings of the 1999 Conference on Information Quality, Cambridge, MA, 2000.

[20] R. Kovac, Y.W. Lee, L.L. Pipino, Total Data Quality Management: the case of IRI, Proceedings of the Conference on Information Quality, Cambridge, MA, 1997, pp. 63–79.

[21] Y.W. Lee, G.K. Tayi (Eds.), Proceedings of the Conference on Information Quality, Cambridge, MA, 1999.

[22] S. Madnick, R.Y. Wang, Introduction to Total Data Quality Management (TDQM) Research Program, No. TDQM-92-01, Total Data Quality Management Program, MIT Sloan School of Management, Sloan, 1992.

[23] V.V. Mandke, M.K. Nayar, Information integrity–a structure for its definition, Proceedings of the Conference on Information Quality, Cambridge, MA, 1997, pp. 314–338.

[24] A Matsumura, N. Shouraboura, Competing with Quality Information, Proceedings of the Conference on Information Quality, Cambridge, MA, 1996, pp. 72–86.

[25] D.M. Meyen, M.J. Willshire, A data quality engineering framework, Proceedings of the Conference on Information Quality, Cambridge, MA, 1997, pp. 95–116.

[26] G.C. Moore, I. Benbasat, Development of an instrument to measure the perceptions of adopting an information technol ogy innovation, Information Systems Research 2 (3), 1991, pp. 192–222.

[27] K. Orr, Data quality and systems theory, Communications of the ACM 41 (2), 1998, pp. 66–71.

[28] J.M. Pearson, C.S. McCahon, R.T. Hightower, Total Quality Management: are information systems managers ready? Information and Management 29 (5), 1995, pp. 251– 263.

[29] T.C. Redman, Data Quality: Management and Technology, Bantam Books, New York, NY, 1992.

[30] C.A. Reeves, D.E. Bednar, Defining quality: alternatives and implications, AMR 19 (3), 1994, pp. 419–445.

[31] J. Saraph, G. Benson, R. Schroeder, An instrument for measuring the critical factors of quality management, Decision Sciences 20 (4), 1989, pp. 810–829.

[32] G. Schusell, Data quality the top problem, DW for Data Warehousing Management, Digital Consulting Institute (DCI), October 1997, p. S5.

[33] M.J. Spendolini, The Benchmarking Book, AMACOM, New York, NY, 1992.

[34] D.M. Strong, IT process designs for improving information quality and reducing exception handling: a simulation experiment, Information and Management 31 (5), 1997, pp. 251–263.

[35] D.M. Strong, B.K. Kahn (Eds.), Proceedings of the Conference on Information Quality, Total Data Quality Management Program, Cambridge, MA, 1997, 372 pp.

[36] D.M. Strong, Y.W. Lee, R.Y. Wang, Data quality in context, Communications of the ACM 40 (5), 1997, pp. 103–110.

[37] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological foundations, Communications of the ACM 39 (11), 1996, pp. 86–95.

[38] R.Y. Wang (Ed.), Proceedings of the Conference on Information Quality, Total Data Quality Management Program, Cambridge, MA, 1996.

[39] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4), 1996, pp. 5–34.

[40] M. Zairi, Benchmarking for Best Practice, Butterworths, Oxford, 1996.

[41] R. Zmud, Concepts, theories and techniques: an empirical investigation of the dimensionality of the concept of information, Decision Sciences 9 (2), 1978, pp. 187–195.

![](/api/attachments/9UF5224Z/fulltext/images/f2ce242d8e9450f433acb397f93c90789a9963f01a178397920d6bb96d35ab65.jpg)

Yang W. Lee is Assistant Professor and Joseph G. Reisman Research Professor in the College of Business Administration at Northeastern University. She received her PhD from MIT. Prof. Lee’s publications have appeared in leading journals such as Communications of the ACM, Sloan Management Review, and IEEE Computer. She also coauthored Quality Information and Knowledge (Prentice Hall, 1999), Data

Quality (Kluwer Acadmic Publishers, 2000) and Journey to Data Quality (MIT Press, forthcoming). Her current research interests include data quality, IT-facilitated institutional learning, and systems integration. In the academic year 2000, she was also a Visiting Professor at MIT Sloan School of Management, where she taught E-systems integration and conducted research on data quality.

![](/api/attachments/9UF5224Z/fulltext/images/54b60d6b96e14636bb3728360fe8cb03cb54c6a02bba4050f54472896fe32228.jpg)

Diane M. Strong is Associate Professor in the Management Department at Worcester Polytechnic Institute. She received her PhD in Information Systems from Carnegie Mellon University. Dr. Strong’s research centers on data and information quality and on MIS application systems, especially ERP systems. Her publications have appeared in leading journals such as Communications of the ACM, ACM Transactions on Infor-

mation Systems, Journal of Systems and Software, Journal of Management Information Systems, and Information & Management.

![](/api/attachments/9UF5224Z/fulltext/images/3548cc3702cb992fb3270f80c347c488a40552770db37eadabc8c68488d46fa0.jpg)

Beverly K. Kahn is Chair and Associate Professor of Computer Information Systems in the Sawyer School of Management at Suffolk University. Dr. Kahn’s research concentrates on information quality, information resource management, database design and data warehousing. Her publications have appeared in leading journals such as MIS Quarterly, Journal of Management Information Systems, Communications of the

ACM and Database. Her methodologies have been applied in organizations such as AT&T, Bell Atlantic, Fleet Financial and US Department of Defense.

![](/api/attachments/9UF5224Z/fulltext/images/2aa9788fbd2f4dd632526f1326e9552be3bf56cb0dca652af93c507378274311.jpg)

Richard Y. Wang is a Pioneer and internationally known Leader in the data quality field. He is Co-director for the TDQM Program at Massachusetts Institute of Technology, where he has been a Professor for a decade prior to joining the Faculty of Boston University. Prof. Wang has also served on the Faculty of the University of Arizona, Tucson, prior to joining the Faculty of MIT. He is a Visiting Professor at the University of California, Berkeley in academic year 2002. Prof. Wang received his PhD degree from the Massachusetts Institute of Technology.
