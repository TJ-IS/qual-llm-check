---
otero_id: 23154
otero_key: "T7QX8G78"
title: "Assessing the quality of institutional DSS"
authors: "R. Santhanam; T. Guimaraes"
year: "1995"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.1995.19"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Assessing the quality of institutional DSS

R. SANTHANAM $^{1}$ and T. GUIMARAES $^{2}$

$^{1}$ Department of Decision Sciences and Information Systems, College of Business Administration, Florida International University, Miami, FL 33199, USA and $^{2}$ J. E. Owen Chair of Excellence, Information Systems, College of Business Administration, Tennessee Technological University, Cookeville, TN 38505, USA

Effectively assessing decision support systems (DSS) quality has long been a difficult challenge to developers and users. Despite the difficulty, the need to justify substantial investments in DSS projects motivates academics and practitioners alike to attempt continuously to improve quality assessment procedures and methods. Institutional DSS are likely to exacerbate the need for quality assessment because they tend to be larger and more expensive than personal DSS. Institutional DSS, by definition, are used by many people throughout the organization. It is very likely, in such cases, that users will have different perspectives, objectives and expectations from the system. Discussion and comparison of existing methods to assess DSS quality are presented, followed by a proposal for the use of the analytical hierarchy process (AHP) method as a more viable alternative for institutional DSS quality assessment. A case study is used to demonstrate the use of AHP for institutional DSS quality assessment in practice.

## Introduction

In today's competitive environment, quality has become a very important topic for many business organizations. Total quality management and other quality improvement programmes are being applied to enhance customer satisfaction of products and services. The quality of decision making in an organization, despite its obvious importance, has not been addressed effectively by researchers, because of its measurement difficulty. An insurmountable problem is assessment of results from the decision alternatives that were not implemented. For action taken from a particular decision, another major difficulty is the appropriate selection of one or more performance assessment measures from an endless list of possibilities such as short-term versus long-term profitability, shareholders' equity, market share, social responsibility measures (i.e. environment impact and employment) and employee morale. Because of such difficulties in measuring decision-making improvements, researchers have focused primarily on assessing the success of specific interventions such as a process re-engineering project, a quality programme, or an information system in terms of surrogate measures such as the opinions held by decision makers and system users. This paper deals with IS quality assessment, and specifically it focuses on decision support systems (DSS).

The managers of corporations whose efforts have been recognised by awards such as the Malcolm

Baldridge National Quality Award understand that, in general, information systems play a vital role in improving product quality by furnishing data and tools to improve decisions (Alter, 1991). Therefore, developing good-quality IS that meet decision-maker needs becomes a critical theme of information technology management. Few research studies have focused on techniques to enhance software productivity and quality (Swanson et al., 1991). There is very little research that examines ways to improve DSS quality. DSS evaluation studies to date have focused on measuring their impact on decision making, but have not devised ways to measure the extent to which they satisfy the needs of the decision maker (Sharda et al., 1988; Benbasat & Nault, 1990). Under the evolutionary development approach, assessment of system quality from the users' perspective is key to its successful implementation (Keen, 1975; Keen & Scott Morton, 1978). Yet, no formal methods exist to help developers assess users' needs, how well these needs are being met by the particular DSS, or what the DSS should look and behave like to serve those needs.

In the case of a one-user personal DSS, it may be relatively simple to gauge a user's needs by interacting with the user and then adapting the system to meet these needs. However, in the case of a large-scale multi-user DSS, referred to as an institutional DSS (IDSS), a formal quality assessment is probably the only systematic way to improve and evolve the system. The development process for an institutional DSS that serves multiple managers is much more challenging than for the development of personal DSS. Correspondingly, appropriate approaches have to be adopted to assess its quality and address end-users' needs (Meador et al., 1986).

The objectives of this paper are threefold. First and foremost, it examines currently available DSS evaluation methods and identifies their shortcomings. It then presents a DSS quality assessment methodology based on the analytical hierarchy process. Finally, the applicability of this methodology in practice is tested in a case study.

## Theoretical framework

The notion of DSS quality and an appropriate evaluation method have not been adequately addressed in the IS literature. Thus, the first subsection contains a definition of DSS quality and its various dimensions. The second subsection addresses the more widely used DSS evaluation methods, their strengths and weaknesses. The third subsection provides an integrative framework which calls for the combination of two or more methods, depending on the DSS evaluation objectives. The last subsection identifies the need for, and proposes, a more appropriate quality assessment method applicable to personal or institutional DSS alike.

## DSS quality as a construct

As mentioned earlier, quality is a very broad construct with many different perspectives. From an engineering perspective, the quality of a product or service is commonly measured in terms of its fitness for intended use, i.e. it must be adequate for the application the customer has in mind (Dilworth, 1988). According to the American National Standards Institute, quality ‘is the totality of features and characteristics of a product or service that bears on its ability to satisfy given needs’ (ANSI/ASQC, 1978). Quality control activities are undertaken with the objective of designing, developing and tailoring a product to satisfy users’ requirements (Evans & Lindsay, 1980). Enterprises that have attained high levels of quality state that the ultimate yardstick of quality is attaining maximal satisfaction of customers’ needs and expectations (CIO, 1991).

A DSS is developed to support and improve managerial decision making. Different capabilities of the system, such as its ability to analyse information, to model decision strategies and to explore alternatives, are product features that facilitate effective decision making. Unlike management information systems (MIS) that provide for predefined information needs, the DSS philosophy emphasises system capabilities, its ability to satisfy managerial information requirements beyond predefined needs, on an ad hoc basis (Sprague,

1980). Therefore, DSS quality should be viewed as the extent to which these DSS capabilities closely match users' decision-making needs. From the users' perspective, DSS quality will depend on: (1) the extent to which they perceive various DSS capabilities as being useful for decision making, and (2) the extent to which the DSS provides a strong combination of these capabilities. For example, a DSS communication feature is likely to be considered useless by a manager who thinks it unnecessary to share information with other managers. By the same token, a manager who considers data analysis techniques important before making a particular decision will be less inclined to use a system that does not provide this function. In both cases, the system is judged to be of poor quality because it does not cater to users' needs.

Development of a DSS without careful consideration of its important quality dimensions is not likely to promote effective decision making, and managers are likely to avoid such systems. On the other hand, a DSS quality assessment process focused on system capabilities can provide valuable information to the developers on how to modify the system to better suit users' needs and expectations. For example, if user managers state that analysing alternative decision strategies is most important for improving their decision making and if they think their DSS does not have adequate capability to do so, that DSS feature becomes a target for quality improvement. In such a case, more modelling and 'what-if?' functions can be added to the system to ameliorate the problem. This approach is particularly useful since a DSS evolves through several stages, and quality assessment at each stage provides a method to identify managers' needs and develop a system that totally fits their needs. According to Deming (1982), a quality product evolves only by constantly evaluating its performance and improving its features until it completely satisfies the needs of the customer.

In the case of a single-user DSS, quality assessment may be accomplished informally through a prototyping process, with the developer interacting with the user and gathering information to improve the system. This process is more difficult in the case of an institutional DSS (IDSS) because of the large number of users and the variety of decisions it supports. According to Sprague and McNurlin (1986), an IDSS is a large-scale DSS that provides organizational support on a continuing basis. Unlike an ad hoc or 'quick hit' DSS, a characteristic of an IDSS is to provide support for recurring decisions for a large number of decision makers (Donovan & Madnick, 1977). The various decision makers using the IDSS may differ widely in the capabilities they expect from the system. On the other hand, the costs of system enhancements are considerable, making it cost effective to focus development efforts on improvements which are most needed by decision makers. Consequently, assessing the needs and developing a system that satisfies these needs become very difficult. To overcome this problem, a quality assessment method which can evaluate and prioritise user needs is an important undertaking.

## Existing methods to assess DSS quality

## Usage statistics

System usage has generally been used (DeLone & McLean, 1992) as a surrogate measure for system effectiveness. It is a simple method, and is easy to implement by examining the statistics collected from system log files. This method indicates the extent of general use of the system by decision makers, but it usually does not provide a measure of the individual DSS features/functions which are most needed or favoured by the decision makers. Secondly, it does not provide information about features not available in the existing system which are needed by decision makers. In some cases, the extra time spent on the computer may be due to poor skills of the user and not necessarily because it is liked by the user. Further, it has been argued that system usage is often not voluntary; that is, usage is mostly mandated by management (Ives et al., 1983; Srinivasan, 1985; Doll & Torkzadeh, 1988). System usage is considered by many to be a behaviour, determined to a great extent by user attitudes (user satisfaction) towards a new system (Ajzen & Fishbein, 1977; Bailey & Pearson, 1983; Baroudi & Orlikowski, 1988; Guimaraes & Gupta, 1988; Tait & Vessey, 1988; Galletta & Lederer, 1989). On the other hand, a system may not be used frequently owing to reasons other than system quality, such as management problems, poor user motivation, or lack of training. In conclusion, while usage statistics may provide some valuable data for system evaluation, they do not provide much of the information needed to assess, prioritise user needs and tune the existing system to meet changing needs.

## User information satisfaction (UIS)

UIS is a widely used method (DeLone & McLean, 1992) to measure the extent to which users believe the DSS meets their information requirements. This is a very reliable construct that has been rigorously tested and validated by many researchers (Gallagher, 1974; Larcker & Lessig, 1980; Bailey & Pearson, 1983; Ives et al., 1983; Sanders & Courtney, 1985; Jenkins & Ricketts, 1986; Baroudi & Orlikowski, 1988; Guimaraes et al., 1992). Using Likert scales, it collects user perceptions about IS related products and services, such as accuracy of information, timeliness of reports and attitude of IS staff. The focus of UIS instruments is on measuring the results from using a system, i.e. 'its utility in decision making' and not the technical quality of the system (Ives et al., 1983). Therefore, it cannot be applied directly to gauge DSS quality. DSS specific UIS measures, such as those developed by Jenkins and Ricketts (1986), focus on the overall DSS product, such as the input procedures and report content, and do not assess user needs for specific DSS features such as 'what if?' analysis and communications. UIS measures are very useful in assessing whether DSS users are satisfied with their system. Similar to usage statistics, they do not provide information on which features are most needed by users, an essential requirement for improving DSS quality. In summary, at least as used to date, the UIS data collection instruments do not provide developers with the necessary information on how to expand and modify the system to match user expectations.

## Financial analysis methods

In many cases, cost–benefit analysis, return on investment and net present value methods are used in determining the financial impact of an IS. All benefits are converted to dollar values and compared against the costs of developing the system (King & Schrem, 1978). However, as the importance of intangible benefits grows, this method is not considered appropriate for DSS systems because of its focus on measuring tangible benefits. In practice, the perceived benefits of DSS were also found to be most significant in justifying their costs and in evaluating their effectiveness as support tools for the decision-making process (Keen, 1981; Meador et al., 1984; Money et al., 1988). While this method can be employed for justifying investment in a system, it cannot be used for improving the quality of a DSS. It does not provide any information on how to enhance the performance of a DSS.

## Value analysis

Value analysis has been proposed (Keen, 1981) as an alternative to financial analysis approaches to assess the value of and justify investment in a DSS. All qualitative and quantitative benefits of a DSS are identified in its prototype version and its value is established. Benefits of the system, such as its support for planning and its help in solving a business problem, are to be considered in establishing the value of the system. Money et al. (1988) suggest ways to identify and quantify intangible DSS benefits using utility measurements. Value analysis provides a good framework that can be used to decide whether the DSS development effort should be abandoned or continued. However, it does not provide the necessary information for DSS quality improvement.

## Theoretical models for predicting user behaviour: TAM and TPB

Recently, theoretical models have been applied to predict users' intentions to use microcomputer systems based on several independent variables (Igbaria et al., 1995). The technology acceptance model (TAM) considers user perceptions about system usefulness, perceived ease of use, and user attitude towards use as predictors of system usage. The theory of planned behaviour (TPB) includes users' behavioural beliefs and outcome evaluation, normative beliefs and motivation, control beliefs and perceived facilitation, attitude, subjective norms and perceived behavioural control as mediators of users' intentions to use the system. These determinant variables could be manipulated to improve/enhance users' intentions to use the system which, in turn, will affect behaviour in the same direction.

Both TAM and TPB use questionnaires to measure the various determinant variables. The models are applied to derive a measure of users' intentions to use the system. These models have a strong theoretical base and have been shown to have good predictive ability (Davis et al., 1989; Mathieson, 1991). However, these models have limited use in assessing DSS quality because they do not provide ways to determine the detailed capabilities users expect from the system. The only system-dependent variable that these models address is intent to use. If a user's intention to use the system is not strong, developers receive no information regarding how the system could be improved to enhance that user's future intention to use it.

## Quality improvement programmes

Business organizations normally implement quality improvement programmes with the objective of improving the quality of their products. Many large organizations such as AT&T, Xerox, Citicorp and American Airlines have successfully launched quality improvement programmes (CIO, 1991). However, there exists no standard technique or procedure to establish such programmes. Typically, a quality improvement programme starts with a management commitment to quality, a vision and, hopefully, a well thought-out plan on how this will be achieved (Dessler & Farrow, 1990; Walton, 1990). That is followed by a policy statement so that all employees are aware of the organization's commitment and therefore might contribute to improving quality. Changes in organizational procedures, setting up acceptable quality standards and quality monitoring teams, and installing employee reward systems are all part of this programme. The process might include the use of quality circles or quality improvement teams. Originally proposed in Japan, quality circles are teams of employees who meet periodically to develop and discuss strategies to improve the quality of products (Sud & Ingle, 1982). Statistical quality control measures are also an integral part of many quality improvement programmes. Statistical quality control aims to produce defect-free products by inspecting samples of products and ensuring that they meet stringent tolerance limits. Deming (1982) suggested that quality improvement programmes should plan for quality, promote the quality concept among their employees, educate employees about achieving quality in products and processes, and continuously evaluate and monitor opportunities for quality improvement. These programmes are part of the total quality management approach that believes quality can be improved only by continuously striving for and evaluating the product so that it meets customer expectations.

Borgschulte et al. (1992) report on a company that installed a quality improvement programme and found that it had not identified user needs correctly. Florida Power and Light was the first company outside Japan to win the Deming Award, by instituting quality improvement programmes in many of its departments including information systems and services. In the information system and services department, employees were asked to talk to their clients and find out their needs. The department had always assumed that quick system response time was most important to their customers. Instead the department found out that the continuous availability of key systems was of primary importance. Hence, Florida Power and Light had to re-examine client needs and rework systems to match these needs. Quality improvement programmes vary across organizations. As said earlier, there are currently no specific guidelines on how to measure quality, or how to apply the programme for improving a specific product, such as a DSS. These programmes comprise a set of activities, procedures and management orientation whereby quality consciousness is included in decision making, in the allocation of resources and in the manufacture of products. In the context of improving DSS quality, some of the management principles embedded in quality improvement programmes may be applicable. However, these programmes do not currently provide a systematic way for assessing DSS user needs, even though one of the principal components of such programmes is the evaluation of customer needs. The evaluation is usually conducted through customer ratings and interviews. While these informal techniques may provide useful clues of what customers expect from their product, more specific assessment of DSS user needs will be necessary for improving DSS quality.

## An integrative framework for DSS quality evaluation

The discussion above addressed a variety of techniques that can be applied in combination to produce an integrated approach to DSS evaluation and management. The DSS evaluation and management process can be viewed as having four stages. In the first stage, a DSS is proposed and its development is justified. Value analysis can be applied at this stage. In the second stage, user requirements are determined and a product that closely matches these needs is developed, i.e. a quality product is developed. Following the prototyping development approach, several evolutionary versions of the system are produced and tested iteratively until the final product is developed. There exists no specific technique, other than the prototyping process itself, which directly and comprehensively supports this stage of DSS management. Quality improvement programmes help provide a quality consciousness in the development effort. Informal discussions with users might help but do not provide complete information. Quality standards, priorities and goals have to be established to provide a product that fully satisfies the users. In the third stage, the DSS is used and supported. The theory of planned behaviour and the technology acceptance model provide useful ways to identify important variables to foster DSS use. In the fourth stage, the DSS is fully implemented and evaluated. At this stage, the UIS instruments can be applied to evaluate the DSS in the context of the operational environment and IS supporting services. Quality development data collection instruments could also be applied at this stage to monitor and improve the performance of the system.

While, in combination, these various evaluation methods provide a fairly comprehensive DSS assessment framework, there is need for more versatile evaluation methods specifically for stage two of the DSS management process. Further, unlike transaction processing systems, DSS by definition require a higher degree of adaptability (Stabell, 1983; Guimaraes & Saraph, 1991). The related models, variables and capabilities should be expanded and modified easily. As the widely recognised trend towards institutional or group decision support continues, there is a clear need for a more systematic DSS quality assessment method that can integrate information from a variety of users in a form which enables developers to improve the capabilities of the system as it evolves towards new versions of increasingly higher quality and sophistication.

## A quality assessment method for IDSS

Given the relatively large end-user community for many IDSS, and the different perspectives the end-users might have, an IDSS requires a formal development approach by which critical user needs can be evaluated and prioritised systematically (Garnto & Watson, 1985; Meador et al., 1986; Sprague & McNurlin, 1986). More specifically, any IDSS quality assessment procedure useful in practice should first identify the relative importance of the various system capabilities that managers perceive as being useful for their decision making. Then, the extent to which the system supports these capabilities should be measured. From this perspective, IDSS becomes a collection of features or capabilities that managers require to support their decision making. How closely these decision requirements are matched by the system capabilities is a useful measure of the quality of the IDSS. An effective and easy-to-implement quality assessment procedure is needed to identify systematically these system requirements and the extent to which the system satisfies them.

One proven technique to measure the relative importance of multiple attributes (features) is found in the analytical hierarchy process (AHP) method devised by Saaty (1980). One of the distinguishing features of AHP is the use of a hierarchic structuring method to determine the relative contribution of system components (features) towards the overall objective of the system (Saaty, 1980; Saaty & Vargas, 1982). This method is based on three principles: decomposition, comparative judgements and synthesis of priorities. To use this method, the decision problem is first decomposed into a hierarchy of interrelated decision elements. The decomposition of the complex problem into a meaningful hierarchy will depend on the nature of the decision to be made. Generally, the problem is outlined and all the relevant attributes/variables that contribute to the solution are listed. These are then clustered into groups of five to nine attributes so that they can be compared with one another in terms of how they influence the solution to the problem. Elements in each cluster will form the different levels of the hierarchy. The top of the hierarchy must identify the highest level system objective. Then clusters of multiple attributes are listed at various levels such that elements in each level can easily be related to at least some elements in the next highest level. For example, consider a simple decision problem to determine the importance of various factors affecting the purchase of a computer. This problem could be decomposed as shown in Figure 1. System performance, technology level, extent of vendor support and user-friendliness of the system are criteria that influence this decision and are shown at level 1 of the hierarchy. At level 2 are criteria that exert influence on elements in level 1. Here it is seen that user-friendliness of the system is dependent on system documentation, dialogue style and help facilities in the system. In the second stage, judgements of the decision maker are obtained through a series of pairwise comparisons in which each attribute at any given level is compared with every other attribute at the same level of the hierarchy to determine its relative importance to the adjacent upper level element. In this example, decision makers would answer questions such as the following: 'In selecting a computer, is (a) extent of vendor support more important than technology level or is (b) technology level more important than extent of vendor support? Please choose one alternative and indicate how much more it is important'. Respondents choose one alternative and indicate the level of importance on a Likert-type scale ranging from equal importance to absolute importance. In the third stage, relative priority scores for the factors are derived based on normalised eigenvectors of matrices representing answers to these comparisons. In this case, the priority scores will show which of the four factors at level one are most important to the purchase of a computer. For a more in-depth discussion of the principles of AHP and examples on how to decompose problems, the reader is referred to Saaty (1980, 1982).

![](/api/attachments/T7QX8G78/fulltext/images/5fd3b739b727dae582b23bf8d33176704bf03fefc6118f2ea8de92c6d79365d2.jpg)  
Figure 1 Example for complex problem decomposition.

The ability to measure, prioritise and synthesise human judgments in a simple logical manner has made AHP a powerful tool for managerial planning, evaluation and resource allocation decisions. Its effectiveness has been documented in several hundred applications worldwide and is thus proven to be a robust system evaluation methodology. Some of the applications of AHP include capacity planning and evaluation of computer systems (Arbel & Seidmann, 1985), selection of suitable office systems (Beck & Lin, 1981), selection of computer operating systems (Roper-Lowe & Sharp, 1990) and planning for engineering applications (Saaty, 1983). More substantial lists of major AHP applications are provided by Zahedi (1986), Golden et al. (1989) and Shim (1989).

There are several advantages to using AHP instead of a simple rating scheme to determine the relative importance of various capabilities of an IDSS, including: (1) the hierarchic decomposition is said to be one of the most commonly used methods by which decision makers factor a complex problem into manageable sub-problems and hence it matches their ‘cognitive processing’ better (Saaty, 1980); (2) the hierarchy provides a complete view of the decision problem and the decision maker may insert or eliminate elements at each level to sharpen the focus on any part; (3) qualitative criteria (intangibles) can be evaluated along with quantitative criteria; (4) AHP provides a powerful method to derive ‘accurate’ ratio scale priorities from imprecise verbal comparisons, since users find it easier to provide verbal judgements rather than having to quantify their feelings – for example, instead of saying vendor support is three times as important as technology, it is easier to say and justify that it is moderately more important (Dyer & Forman, 1992); (5) AHP allows the decision maker to focus on the comparison of just two features at a time, making the observation as free as possible from extraneous influences; (6) the relative priorities are derived from a complete set of judgements, not one answer, hence priorities are derived in a more meaningful and consistent manner; (7) AHP generates more information since each feature is methodically compared with every other and this extra information is used to ‘average errors’, similar to averaging errors in calculating the population mean (Dyer & Forman, 1992) – thus, if two groups estimated the relative size of objects, they will arrive at the same result irrespective of the fact that one group tended to use stronger words to express itself: in tests involving subjects comparing areas of geometric objects using verbal judgements, the average root mean square of resulting priorities was only 2.4% (Forman, 1990); (8) the scores derived through the AHP method provide a quantitative assessment of how much more/less important a given IDSS feature is, compared with other IDSS features – no two features would receive the same score, so developers can easily focus their effort on those features that are most needed according to users; (9) AHP also provides a way to calculate the consistency of respondents’ judgements: an inconsistency ratio of 0 shows perfect consistency, while a ratio of 1 is equivalent to a set of random judgements – while perfect consistency cannot be expected, higher than 10% or 0.1 ratio can be examined to check whether data entry errors occurred, the respondent did not pay attention in answering the questions, or some other problem occurred; and (10) in a recent empirical study, the accuracies of judgements obtained via five preference elicitation methods were compared. It was found that the verbal pairwise comparison method, as proposed in AHP, obtained the most accurate answers. Direct estimation methods, similar to those used in rating scales, showed the least accurate answers (Millet, 1992).

As mentioned above, the AHP method can be used to determine the relative importance of various DSS capabilities. Managers can be asked to compare various IDSS features that promote effective decision making, such as the capabilities to analyse information, model decision strategies and communicate with other managers. Based on the managers' responses, the various system features can be ranked in terms of their importance. The extent to which the system supports these capabilities is evaluated using a simple questionnaire with Likert scales for managers to rate the extent to which their specific IDSS provides each of these capabilities. Based on this, a separate ranking for the various capabilities provided by the IDSS is determined. In some cases, low scores may reflect user deficiencies (i.e. lack of training) rather than weaknesses in system features. Such exogenous problems need to be identified and accounted for in terms of their effect on the ranking procedures.

A high correlation between the two sets of ranks would indicate a system of good quality. It would mean that the IDSS features which managers consider most important to decision making are being well provided by the IDSS. If many features are rated high on the importance dimension and are poorly supported by the system, the correlation score will be low, thus indicating a poor-quality system. It indicates a system that does not fit well with the users' decision support needs. System developers will then have to analyse the results to see which features are to be added or changed to improve the quality of the system.

The quality assessment methodology presented above can be supplemented with quality standards prescribed by the organization. Acceptable correlation scores between importance ranking and IDSS support ranking can be established. Alternatively, IDSS support ratings could be weighted (multiplied) by the corresponding importance score and combined to obtain an overall quality score for the system. An IDSS receiving higher than the prescribed quality score could be considered to be of good quality. An IDSS not reaching the prescribed quality standards should be reworked and enhanced until it reaches the required quality standard.

## Research design

The nature of the research topic strongly influences the selection of the research methodology (Benbasat, 1984). The main objective of this research was to demonstrate that the proposed quality assessment method for an IDSS can highlight and effectively measure differences between available system features and the needs of decision makers. These differences, in turn, represent a measure of system quality and will indicate where system improvements should take place. A case study methodology provides the ideal vehicle to illustrate the use of the proposed quality assessment technique and should be considered as a most appropriate research design. The information systems departments of several large corporations were contacted to determine whether they were in the process of developing an IDSS. One corporation in Miami, Florida, informed us that they had just started the development of an IDSS (hereafter referred to as SDSS, signifying the specific DSS in this case) and were interested in participating in this research. This was a large business organization in the service industry, well known for providing effective and sophisticated information systems for their managers. Their state-of-the-art computing environment and their effective use of DSS technology, along with the willingness of the managers to co-operate and provide us with the necessary information, made us select this organization for our case study.

## Description of the SDSS system

SDSS was developed to replace a marketing reporting system and to enhance the decision-making processes of the company's marketing managers. Developed by system professionals, SDSS has been termed an IDSS because it supports all levels of decision makers in the marketing and sales department. SDSS was developed using a technique similar to the decision support analysis discussed by Meador et al. (1986), a development technique suitable for IDSS. Based on structured interviews with potential users, system requirements were defined. It was decided at the planning stage that SDSS should provide database querying facilities, a report writer, graphics capabilities and modelling functions, among other capabilities. Using the DSS generator Express, the first version of the system was developed and implemented on a set of personal computers and the company's mainframe computer. After about two months of use, the quality assessment of SDSS based on the AHP technique was undertaken.

## Development of the instrument

In order to develop the AHP-based questionnaire, a structured problem hierarchy was developed. The top level of the hierarchy, denoting the overall objective of the system, was ‘improved decision making’. The lower level of the hierarchy, denoting elements that contribute to the system objective, consisted of its capabilities specified in the system objectives document. Keeping in line with Saaty’s (1982) recommendation, these were limited to the seven most important features required of SDSS. Saaty recommends that the number of elements at any level should not exceed seven to nine, because a larger number will increase the number of pairwise comparisons and could affect the consistency of people’s judgement. The selected list of seven SDSS features were its support for users to:

1. Receive accurate information

2. Make ad hoc requests for information

3. Analyse information

4. Communicate with different personnel

5. Get support for complex decision making

6. Explore alternative decision strategies

7. Make quick decisions.

A questionnaire was developed using the scale and guidelines provided by Saaty (1982) and used to determine the relative importance of these seven SDSS capabilities. Managers were asked to compare two capabilities at a time and indicate which capability contributed more strongly to improving their decision making and by how much. There was a total of twenty one such comparisons. Another questionnaire was developed for the managers to rate the extent of SDSS support for each of these capabilities. The answers were obtained on a five-point Likert scale from (1) no support to (5) great extent of support. One additional feature, namely ‘ability to support standard marketing processes’, was included in this questionnaire. This was a feature specified by top management but the system development managers and the users did not have a clear understanding of this term and hence it was not included in data analysis. The order of the questions was randomised so there were seven different sets of questionnaires.

## Subjects

The first version of the SDSS system was primarily used by fifteen managers and the questionnaires were distributed to these users. Eight completed questionnaires were returned, indicating a 52% response rate. The eight respondents consisted of two senior level managers, three middle level managers and three supervisory managers. One should note that the small sample of responses does not affect the results of the quality assessment procedure. The purpose of this case study was to test the use of AHP methodology to gauge the quality of an institutional DSS, and to test whether the results could be used in practice to improve future performance of the system. The case study was not designed for, and should not be construed as, a comprehensive evaluation of this particular system.

## Quality assessment results

The data from the AHP questionnaire were analysed using Expert Choice software (trademark of Decision Support Software Inc., McLean, Virginia, USA). As mentioned earlier, the AHP method provides for the calculation of an inconsistency ratio that measures whether a subject answered the questions in a purely random manner. It has been recommended that inconsistency ratios higher than 10% should not be accepted because they suggest that the subject may not have paid adequate attention to the questions. The ratio was calculated for each subject and it was found to be higher than 10% for one respondent. That questionnaire was not included in data analysis. The two most common approaches useful to aggregate AHP responses from several respondents are to: (1) calculate the geometric mean of each response and generate a single matrix, or (2) calculate the simple average of weights derived from each individual. Jensen (1986) demonstrated that there is little difference in the results obtained by either procedure. Saaty (1980) recommended using the simple averaging approach if respondents have sufficient knowledge about the decision domain. In this case study, the respondents were managers who knew about the decision domain and the software being used. We followed Saaty's recommendation and adopted the averaging approach to combine individual judgements. The results of the analysis in Table 1 indicate the kind of information that can be obtained from users about the quality of a system. For example, Table 1 shows that SDSS users feel that the ability to receive accurate information is most important to improve decisions. That is followed by the ability to analyse relevant information. The scores on the extent of the system support for these capabilities are also shown in Table 1. Managers felt that SDSS provided great support for analysing information and to make ad hoc requests for information. The Spearman's rank correlation coefficient for user requirements and SDSS features was 0.78 ( $\alpha = 0.05$ ), indicating that the system supported most of the users' requirements.

The weighted scores for each capability were calculated and an overall quality score for the system was developed. As shown in Table 1, this score for SDSS was 3.72. The organization had no quality standards (a benchmark score) to compare these scores against. For the rating scale utilised in this study, the maximum quality score that the system could obtain was 5.00. Scores very much lower than 5.0, i.e. 1.25 or 2.00, would have denoted a poor-quality system. Hence, a score of 3.72 indicates a system of satisfactory quality. The results of the quality assessment were also plotted graphically as shown in Figure 2. The levels of importance of various system capabilities (y-axis) are plotted against their respective ratings (x-axis) and a matrix was created. Those capabilities that fall in the upper left quadrant would be priority areas for im-

![](/api/attachments/T7QX8G78/fulltext/images/d210ec94e2eb976f0217f1639261eaecb4d6d6771ec8e28dd45bb13fa734cb6c.jpg)  
I Quadrant - High importance capabilities implemented poorly  
II Quadrant - High importance capabilities implemented well  
III Quadrant - Low importance capabilities implemented well

IV Quadrant - Low importance capabilities implemented poorly

Figure 2

Table 1 Results of SDSS's quality assessment.

<table><tr><td>Capability</td><td>AHP score</td><td>AHP rank*</td><td>SDSS&#x27;s score</td><td>SDSS&#x27;s rank*</td><td>Quality score</td></tr><tr><td>Ad hoc</td><td>0.119</td><td>4</td><td>4.14</td><td>2</td><td>0.49</td></tr><tr><td>Analyse</td><td>0.193</td><td>2</td><td>4.29</td><td>1</td><td>0.82</td></tr><tr><td>Communicate</td><td>0.088</td><td>6</td><td>3.00</td><td>7</td><td>0.26</td></tr><tr><td>Support</td><td>0.155</td><td>3</td><td>3.57</td><td>4</td><td>0.55</td></tr><tr><td>Explore</td><td>0.096</td><td>5</td><td>3.29</td><td>5</td><td>0.31</td></tr><tr><td>Quick</td><td>0.061</td><td>7</td><td>3.14</td><td>6</td><td>0.19</td></tr><tr><td>Accuracy</td><td>0.287</td><td>1</td><td>3.86</td><td>3</td><td>1.10</td></tr><tr><td colspan="3"></td><td colspan="2">Total quality score</td><td>3.72</td></tr></table>

Ad hoc: ability to make ad hoc requests for information.  
Analyse: ability to analyse the information.  
Communicate: ability to communicate with different personnel.  
Support: ability to support complex decision making.  
Explore: ability to explore alternative strategies.  
Quick: ability to make quick decisions.  
Accuracy: ability to receive accurate and timely information.  
\*Spearman's rank correlation coefficient between AHP rank and SDSS's rank = 0.78 ( $\alpha = 0.05$ ).

provement, because they represent important capabilities that are poorly implemented. In SDSS's case, as seen in Figure 2, most capabilities were well supported, indicating a good-quality system.

Data analysis was followed by interviews with respondents to validate the questionnaire results and to obtain more detailed information. Users stated that SDSS provided them with many different ways to analyse information, including an ad hoc reporting capability. That compares very favourably with the preceding management reporting system which provided only a limited number of standard reports. The system allowed them to view sales totals and forecasts under different categories. Users can also choose between several display formats, such as standard report, graph and pie chart. This flexibility was found to be very useful.

Three features of SDSS that received relatively poor ratings were (in order of decreasing quality): (1) its support for communicating with other managers; (2) its support for making quick decisions; and (3) its support for exploring alternative strategies. When users were questioned, they stated that the system's communication facility was not adequate because they could not share reports, results of analysis or detailed information. The electronic mail facility allowed them to send and receive simple messages only, which was inadequate for sharing tables, reports and other decision analysis. Users felt that SDSS did not support quick decision making because, when managers needed special information that required access to a mainframe database, it took more than thirty minutes to obtain it. Because of this delay, many managers would submit their report requests before they left home for the evening, and hope that answers would be ready the next morning.

The low rating for the SDSS capability to support the exploration of alternative decision strategies was explained by the fact that many of the statistical and forecasting functions were not well supported by the system. The DSS generator in this case (Express) provides many tools to forecast and evaluate alternatives, but these have not been implemented in the current version of the system. Consequently, only users who had very good programming knowledge could use this capability, which frustrated most of the other users. Users did not voice any complaints about the other SDSS capabilities.

The results were also discussed with the systems development manager. He stated that, based on this quality assessment, an effort to enhance the communication feature, i.e. SDSS integration with the company electronic mail facility, to send reports, results of analysis, etc., will be undertaken. He had heard complaints about the long time taken to get information from the main corporate database but had no systematic assessment of the various SDSS components. According to this manager, efforts will be undertaken to enhance the PC to mainframe link performed by the DataServer mechanism. This would speed up the retrieval of information from the corporate database and help managers make decisions more quickly. He also stated that steps were being taken to develop regression and price elasticity models that will help decision makers explore alternative marketing strategies. Furthermore, the manager felt that in SDSS version two, the statistical functions would have to be implemented in a more end-user friendly fashion, perhaps through a menu-driven approach.

Users' ratings of various SDSS capabilities combined with their importance scores provided information to the system development manager on how to target future development work. According to the system development manager, the quality assessment method provides a means to ‘steer the system towards satisfying users’ needs’. The method helped prioritise the development of SDSS functions in various stages, and also helped identify opportunity areas for improving the performance of the system.

## Discussion

It is clear from this study that a quality assessment methodology provides a systematic way to improve IDSS performance and manage its development. In this case, the importance of various system features had to be determined after users interacted with the system, since they had no experience with DSS capabilities in general. In situations where users are very familiar with common DSS features, the importance scores for the features may be determined before the system is developed, and the assessment may be conducted after the system is developed. With the AHP method it is possible to develop a hierarchy that can structure the problem into several levels. Elements at each level of the hierarchy can be used to evaluate IDSS features to a greater degree of detail, such as the colour of the screen, the size of print and the style of reports. Such a detailed assessment will clearly help a much finer tailoring of the system toward satisfying users' needs. In line with the evolutionary DSS development methodology, the quality assessment can be conducted on different versions of the system and at different points in time. At each stage, the AHP methodology provides a systematic way to enhance the IDSS to suit users' expectations. As users become familiar with various generic DSS capabilities, more and more features can be considered in the assessment. The improvement of the system over time can be one way to assess system developers' performance. In situations where several IDSS are developed in an organization, the overall quality score is a way to compare the performance of these systems.

It is interesting to note that the organization independently conducted a value analysis of SDSS at the same time that this AHP quality assessment was undertaken. The value analysis showed that users benefited from the system, but the analysis could not provide any information on how to improve the SDSS towards its version 2. In a similar fashion, the systems development manager felt the SDSS usage statistics provided some information about the extent to which it was being used. However, it could not provide detailed information on each SDSS capability. On the other hand, the AHP assessment provided the systems development manager with the information necessary to enhance the weak capabilities of the system, but it did not provide a financial measure of its value to the company. Needless to say, such information may be vital to ensure funding for subsequent versions of the system.

The proposed method requires the identification of relevant IDSS capabilities/criteria that have to be evaluated. Typically, this is done based on previous knowledge about the problem, group discussions or other sources such as the system documents used in this case study. Lists of DSS capabilities provided in Keen & Scott Morton (1978), Alter (1980), Sprague (1980) and Bennett (1982) could be utilised to identify features for quality assessment. Delphi techniques are sometimes used in identifying criteria for AHP analysis (Khorramshahgol & Moustakis, 1988). The reader should note that criteria can be added or deleted from the AHP hierarchy, and additional judgements can be obtained without repeating the previous judgements; the importance scores can easily be recomputed. A dictionary of hierarchies that represent problems commonly encountered in private and public corporations is also available to assist in the construction of a hierarchy (Saaty, 1990a).

The AHP questionnaire may seem lengthy but the questions are generally ordered in such a manner that they can be answered quickly. For example, the first six questions pertained to the comparison of ‘ability to receive quick and accurate information’ from six other DSS features. The format for each question, as well as for the scales and anchors, is so similar that the user is able to anticipate them after answering three to four questions. After this, the respondent is in a position to answer the remaining questions quickly. Various applications and case studies on the use of AHP highlight the ease and ‘naturalness’ with which answers are obtained (Saaty, 1980).

The advantages of using the AHP method for priority determination are well documented. In recent years, some researchers have questioned the use of AHP in specific cases where adding more elements to the hierarchy affects the interpretation of criterion weights and creates rank reversals (Belton & Gear, 1983; Schoner & Wedley, 1989). Others have stated that it has to be synthesised with the concepts provided in multi-attribute utility theory (Dyer, 1990). However, Harker and Vargas (1987, 1990) and Saaty (1990b) have provided strong justification as to why these issues do not create critical problems in the implementation of AHP, and have demonstrated that AHP has a strong theoretical foundation.

It is important to note that the quality assessment method proposed here evaluates only one aspect of DSS performance, namely the technical quality of the system. A complete evaluation of a DSS, as mentioned earlier, should include, among other things, the extent to which the system led to better decisions. Some laboratory studies (Sharda et al., 1988) have attempted to assess the quality of decisions made using measures such as the time taken to make the decision with and without the DSS, the DSS impact on profits, decision accuracy, and manager confidence with the decision made. However, no methods or guidelines exist as to how this type of evaluation can be conducted in an organizational setting. Given that organizations are very keen to assess the value of investments in their DSS, this will be an important area for future research.

## Summary

Many organizations have programmes to measure and enhance the quality of their products and services. This paper discussed how the quality of an IDSS could be improved. A quality assessment procedure based on AHP was proposed and tested on an IDSS. The assessment procedure was found to be very useful for assessing the quality of the IDSS and for generating information for the builders on how to improve the system. However, managers are cautioned that, while the proposed methodology provides useful information, the actual improvement will depend on whether the effort and resources are devoted to enhancing the quality of the system. The information generated by AHP could be supplemented by the financial information necessary to justify further investment in the system.

While we developed and illustrated the use of an AHP-based method for evaluating an IDSS, it is possible to extend the use of this method for other information systems such as executive information systems and group decision support systems. The unique features that are prioritised would vary across systems but the methodology is equally applicable. In an EIS, for example, the features that could be tested may include ease of dialogue, input procedure and screen design. Because of its versatility, the AHP-based method provides a systematic and reliable means to identify users' needs and assess the quality of systems in multi-user, sophisticated decision support environments. These are essential ingredients in developing and maintaining good-quality DSS.

## References

AJZEN I and FISHBEIN M (1977) Attitudes–behavior relations: a theoretical analysis and review of empirical research. Psychological Bulletin 84(5), 888–918.

ALTER AE (1991) The qualitative difference, interview with winners of Baldridge Quality Award. CIO, International Data Group Publication, August, 20–23.

ALTER SL (1980) Decision Support System, Current Practice and Continuing Challenges. Addison-Wesley, Reading, Massachusetts.

ANSI/ASQC (1978) Quality Systems Terminology. American Society for Quality Control, Milwaukee, Wisconsin.

ARBEL A and SEIDMANN A (1985) Capacity planning, benchmarking and evaluation of small computer systems. European Journal of Operations Research 22(2), 347–358.

BAILEY JE and PEARSON SW (1983) Development of a tool for measuring and analyzing computer user satisfaction. Management Science 29(5), 530–545.

BAROUDI JJ and ORLIKOWSKI WJ (1988) A short-form measure of user information satisfaction. Journal of Management Information Systems 4(4), 44–59.

BECK MP and LIN BW (1981) Selection of automated office systems: a case study. OMEGA 9(3), 169–176.

BELTON V and GEAR T (1983) A note on a short-coming of Saaty's method of analytic hierarchies. OMEGA 11(3), 228–230.

BENSABAT I (1984) An analysis of research methodologies. In Information System Research Challenge (McFarLAN W, Ed.), pp. 47–85. Harvard Business School Press, Boston, Massachusetts.

BENBASAT I and NAULT BR (1990) An evaluation of empirical research in managerial support systems. Decision Support Systems 6(3), 203–226.

BENNETT JL (1982) Building Decision Support Systems. Addison-Wesley, Reading, Massachusetts.

BORGSCHULTE DF, ELAM JJ and SEIN MK (1992) Managing for Quality within the Information Systems and Services Group at Florida Power and Light. Working Paper, Florida International University, Miami.

CHIEF INFORMATION OFFICER (CIO) (1991) The Magazine for Information Executives, Special Issue on Companies Where Quality Counts, August, 1–32.

DAVIS FD, BAGOZZI RP and WARSHAW PR (1989) User acceptance of computer technology: a comparison of two theoretical models. Management Science 35(8), 982–1003.

DELONE WH and McLEAN ER (1992) Information systems success:

the quest for the dependent variable. Information Systems Research 3(1), 60–93.

DEMING WE (1982) Quality, Productivity and Competitive Position. MIT Press, Cambridge, Massachusetts.

DESSLER G and FARROW D (1990) Implementing a successful quality improvement program in a service company: winning the Deming Prize. International Journal of Service Industry Management 1(1), 45–53.

DILWORTH JB (1988) Production and Operations Management, 3rd edn. Random House, New York.

DOLL WJ and TORKZADEH G (1988) The measurement of end-user computing involvement. MIS Quarterly 12(2), 259–274.

DONOVAN J and MADNICK S (1977) Institutional and adhoc DSS and their effective use. Database 8(3), 79–88.

DYER RF (1990) Remarks on the analytic hierarchy process. Management Science 36(3), 249–258.

DYER RF and FORMAN EH (1992) Group decision support with the analytic hierarchy process. Decision Support System 8, 99–124.

EVANS JR and LINDSAY WM (1980) The Management and Control of Quality. West Publishing, St. Paul, Minnesota.

FORMAN EH (1990) Deriving ratio level measures from verbal judgements. In Proceedings of the Washington Consortium Schools of Business, 1990.

GALLAGHER CA (1974) Perceptions of the value of a management information system. Academy of Management Journal 17(1), 46–55.

GALLETTA DF and LEDERER AL (1989) Some cautions on the measurement of user information satisfaction. Decision Sciences 20(3), 419–438.

GARNTO C and WATSON HJ (1985) An investigation of database requirements for institutional and adhoc DSS. Database 16(2), 116–129.

GOLDEN BL, WASIL EA and HARKER PT (1989) The Analytic Hierarchy Process: Applications and Studies. Springer-Verlag, New York.

GUIMARAES T and GUPTA Y (1988) Measuring top management satisfaction with the MIS department. OMEGA 16(1), 17–24.

GUIMARAES T and SARAPH J (1991) The role of prototyping in executive decision systems. Information and Management 21, 257–267.

GUIMARAES T, IGBARIA M and LU M (1992) Determinants of DSS success. Decision Sciences 23(2), March, 409–430.

HARKER PT and VARGAS LG (1987) The theory of ratio scale estimation: Saaty's analytic hierarchy process. Management Science 33(11), 1383–1403.

HARKER PT and VARGAS LG (1990) Reply to remarks on the analytic hierarchy process. Management Science 36(3), 269–273.

IGBARIA M, GUIMARAES T and DAVIS G (1995) Testing the determinants of microcomputer usage via a structural equation model. JMIS 11(4), 87–114.

IVES B, OLSON MH and BAROUDI JJ (1983) The measurement of user information satisfaction. Communications of the ACM 26(10), 785–793.

JENKINS AM and RICKETTS JA (1986) The Development of an MIS Satisfaction Questionnaire: An Instrument for Evaluating User Satisfaction with Turnkey Decision Support Systems. Working Paper 295, Indiana University, Bloomington, Indiana.

JENSEN RE (1986) Comparison of consensus methods for priority ranking problems. Decision Sciences 17(1), 195–211.

KEEN PGW (1975) Computer-based decision aids: the evaluation problem. Sloan Management Review Spring, 17–29.

KEEN PGW (1981) Value analysis: justifying decision support systems. MIS Quarterly 5(1), 1–16.

KEEN PGW and SCOTT MORTON MS (1978) Decision Support Systems: an Organizational Perspective. Addison-Wesley, Reading, Massachusetts.

KHORRAMSHAHGOL R and MOUSTAKIS VS (1988) Delphic hierarchy process: a methodology for priority setting derived from the Delphi method and analytical hierarchy process. European Journal of Operations Research 37(2), 347–354.

KING WR and SCHREM EL (1978) Cost-benefit analysis in information systems development and operation. Computing Surveys 10(1), 20–34.

LARCKER DF and LESSIG VP (1980) Perceived usefulness of information, a psychometric examination. Decision Sciences 11(1), 121–134.

MATHIESON K (1991) Predicting user intentions: comparing the technology acceptance model with the theory of planned behavior. Information Systems Research 2(3), 173–191.

MEADOR CL, GUYOTE MJ and KEEN PGW (1984) Setting priorities for DSS development. MIS Quarterly 8(2), 117–129.

MEADOR CL, GUYOTE MJ and ROSENFELD WL (1986) Decision support planning and analysis: the problems of getting large-scale DSS started. MIS Quarterly 10(2), 159–177.

MILLET I (1992) An empirical comparison of preference elicitation methods. In Proceedings of the 1992 Decision Sciences Annual Meeting, San Francisco, California, pp. 541–543.

MONEY A, TROMP D and WEGNER T (1988) The quantification of decision support benefits within the context of value analysis. MIS Quarterly 12(2), 223–236.

## About the authors

Radhika Santhanam is Associate Professor of MIS at Florida International University. She earned a PhD from the University of Nebraska. Her research interests include human-computer interaction, management of information system investments, and decision support and expert systems. She has published in Information Systems Research, European Journal of Operations Research, International Journal of Man-Machine Studies, Computers and Operations Research, OMEGA, Information and Management, Interfaces, Journal of American Society for Information Science and other journals.

ROPER-LOWE AC and SHARP JA (1990) The analytic hierarchy process and its applications to an information technology decision. Journal of Operational Research Society 4(1), 49–59.

SAATY TL (1980) The Analytic Hierarchy Process. McGraw-Hill, New York.

SAATY TL (1982) Decision Making for Leaders. Wadsworth, Belmont, California.

SAATY TL (1983) Priority setting in complex problems. IEEE Transactions on Engineering Management EM-30, 140–155.

SAATY TL (1990a) How to make a decision: the analytic hierarchy process. European Journal of Operational Research 48(1), 9–26.

SAATY TL (1990b) Exposition of AHP: a reply. Management Science 36(3), 259–268.

SAATY TL and VARGAS LA (1982) The Logic of Priorities. Kluiver-Nijhoff Publications, Boston, Massachusetts.

SANDERS GL and COURTNEY JF (1985) A field study of organizational factors influencing DSS success. MIS Quarterly 9(1), 77–93.

SCHONER B and WEDLEY WC (1989) Ambiguous criteria weights in AHP: consequences and solutions. Decision Sciences 20(3), 462–475.

SHARDA R, BARR SH and McDONNELL JC (1988) Decision support systems effectiveness: a review and an empirical test. Management Science 34(2), 288–296.

SHIM JP (1989) Bibliographical research on the analytic hierarchy process. Socio-Economic Planning Sciences 23(3), 161–167.

SPRAGUE Jr. RH (1980) A framework for the development of decision support systems. MIS Quarterly 4(4), 1–26.

SPRAGUE Jr. RH and McNURLIN BC (1986) Information Systems Management in Practice, pp. 363–382. Prentice-Hall, Englewood Cliffs, New Jersey.

SRINIVASAN A (1985) Alternative measures of system effectiveness: associations and implications. MIS Quarterly 9(3), 243–253.

STABELL CB (1983) A decision-oriented approach to building DSS. In Building Decision Support Systems (BENNETT JL, Ed.). Addison-Wesley, Reading, Massachusetts.

SUD I and INGLE N (1982) Quality Circles in Service Industries: Comprehensive Guidelines for Increasing Productivity and Efficiency. Prentice-Hall, Englewood Hills, New Jersey.

SWANSON K, McCOMB D, SMITH J and McCUBBREY D (1991) The application software factory: applying total quality techniques to system development. MIS Quarterly 15(4), 567–579.

TAIT P and VESSEY I (1988) The effects of user involvement on system success: a contingency approach. MIS Quarterly 12(1), 91–108.

WALTON M (1990) Deming Management at Work. Putnam, New York.

ZAHEDI F (1986) The analytic hierarchy process - a survey of the method and its application. Interfaces 16(4), 96-108.

Tor Guimaraes holds the J.E. Owen Chair of Excellence in IS at Tennessee Technological University. He has a PhD in MIS from the University of Minnesota. He was a professor and chairman of the MIS Department at St. Cloud State University and earlier was an assistant professor at Case Western University. He has spoken at numerous professional meetings and consulted with many leading organizations including TRW, American Greetings, AT&T, IBM and the D.O.D. He has published many articles in Information Systems Research, Communications of the ACM, MIS Quarterly, Decision Sciences, OMEGA, Computers and Operations Research, Information & Management and Data Base.
