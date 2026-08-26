---
otero_id: 16108
otero_key: "2H85ZBBE"
title: "Numerical data quality in IS research and the implications for replication"
authors: "James R. Marsden; David E. Pingry"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Numerical data quality in IS research and the implications for replication

![](/api/attachments/2H85ZBBE/fulltext/images/0cee2bc8beb3d7afe2b86f579b65c4430864737f5832223b9dc2d5e386ca3dff.jpg)

James R. Marsden, David E. Pingry

PII: S0167-9236(18)30164-7

DOI: doi:10.1016/j.dss.2018.10.007

Reference: DECSUP 12999

To appear in: Decision Support Systems

Please cite this article as: James R. Marsden, David E. Pingry , Numerical data quality in IS research and the implications for replication. Decsup (2018), doi:10.1016/ j.dss.2018.10.007

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

Research Editorial

# Numerical Data Quality in IS Research and the Implications for Replication

by

James R. Marsden Board of Trustees Distinguished Professor, University of Connecticut Editor-in-Chief, Decision Support Systems

and

David E. Pingry

Professor Emeritus, University of Arizona

Member, Editorial Advisory Board, Decision Support Systems

Numerical Data Quality in IS Research and the Implications for Replication

## ABSTRACT

We argue that there are major, persistent numerical data quality issues in IS academic research. These issues undermine the ability to replicate our research -- a critical element of scientific investigation and analysis. In IS empirical and analytics research articles, the amount of space devoted to the details of data collection, validation, and/or quality pales in comparison to the space devoted to the evaluation and selection of relatively sophisticated model form(s) and estimation technique(s). Yet erudite modeling and estimation can yield no immediate value or be meaningfully replicated without high quality data inputs. The purpose of this paper is: 1) to detail potential quality issues with data types currently used in IS research, and 2) to start a wider and deeper discussion of data quality in IS research. No data type is inherently of low quality and no data type guarantees high quality. As researchers, our empirical research must always address data quality issues and provide the information necessary to determine What, When, Where, How, Who, and Which.

## 1. Introduction

The issue of data quality, where here we use data to refer only to numerical values, is hardly new. What strikes us as new is a growing lack of focus on data quality in IS academic research analyses. In IS research papers, it is not uncommon to find discussion of the data limited to one or two paragraphs that offer little more than a brief summary of the data source along with the ubiquitous indication of the final number of “observations” that are to be used in model estimation. The amount of space devoted to data collection, validation, and/ or quality details pales in comparison to the space devoted to detailing and explaining why a relatively sophisticated model form and estimation technique(s) are employed. Yet erudite modeling and estimation can yield no value without quality data inputs. We frequently hear claims that we are now in the “era of big data,” but big data without good quality does not yield better results. More data of poor quality is not progress. What we need is to move into an era of high quality, big data.

While our focus here is on data quality in the realm of IS research, the data quality problem is, unfortunately, rather widespread. IS research is hardly an isolated island of data concerns. This concern is spread over many academic areas and is often obscured or confounded with terms such as bad experiments, bad analysis, shoddy work, lack of replicability and so forth. Although high quality data does not guarantee high quality experiments, good analysis, or replicability, quality data is a necessary condition for those good outcomes.

The growing concern about the “reproducibility crises” in the physical sciences has led to major discussions in prime outlets including Nature [7], Psychological Science [18], Genes & Diseases [25], Genetics [6], Nature Reviews Drug Discovery [10], Journal of Controversies in Biomedical Research [4], and The Economist [11, 16]. The article “How Science Goes Wrong,” in the October 19, 2013 edition of The Economist [16] stated that:

“Modern scientists are doing too much trusting and not enough verifying – to the detriment of the whole of science, and of humanity. Too many of the findings that fill the academic ether are the result of shoddy experiments or poor analysis.”

In the article “Reproducing results: how big is the problem?” in the January 19, 2016 edition of Times Higher Education [21], Paul Jump, starting with the quote from The Economist above, gives an update on the state of the replication issues and some of the efforts to address them. Some of these efforts by the National Institutes of Health (NIH) are described by Collins and Tabak in Nature [7].

The sciences know the importance of quality data and the problems resulting from poor quality data. Researchers and funding agencies are weighing appropriate data standards and data access to facilitate reproducibility. A general solution or set of solutions may not be at hand, but the spotlight is on the issue.

# ACCEPTED MANUSCRIPT

Our reference disciplines, especially economics, also continue to struggle with data quality. But, in contrast to IS research, in economics, for example, data quality issues have a long history of being openly noted and considered. From Morgenstern’s [29] classic volume, “On the Accuracy of Economic Observations,” to the recent work of Maniadis et al. [26] on enhancing reproducibility in experimental economics, the data quality problem is and has been in the mainstream of the discussion of what it means to do quality research.

Interestingly, another reference discipline for IS research, psychology (the Association for Psychological Science to be precise) has created the Collaborative Replications and Education Project (CREP), whose purpose is stated as: “Through student participation in largescale replication efforts we aim to (1) facilitate student research training and (2) solidify research findings in psychological science.”

Why are we in IS disciplines showing so little concern? Despite some recent positive signs that data quality and replication are being taken seriously, we argue that IS research needs to attack these issues much more proactively. If IS academic research is to be taken seriously by academics and practitioners (who are becoming much more sophisticated about data in this era of analytics), the quality of the data employed by IS academic researchers must set the standard. One purpose of this paper is to start a wider and deeper discussion of data quality in IS and the implications for IS research reproducibility and replication.

After a review in Section 2 of the limited literature on data quality in IS research, Section 3 considers the issues surrounding the setting of data quality thresholds. Section 4 details the various categories or data types currently prominent in IS research, followed in Section 5 by an analysis of the challenges posed for each data type in reaching quality thresholds. Finally, in Section 6 we announce a call for papers to issues related to establishing and implementing data quality levels for different data types that might undergird journal policies that emphasize data quality and reproducibility.

## 2. Data Quality and Replication in IS Research Literature

Your eyes do not deceive – this is a very short literature review section reflecting the very limited attention to data quality and replication in IS. As indicated above, our purposes here are to present a thorough consideration of the current state of data quality in IS and to initiate a wider and deeper discussion of data quality in IS and the implications for IS research reproducibility and replication.

## 2a. Data Quality

IS research is not devoid of efforts in the data quality arena. However, the work to date has tended to focus on issues of data quality management and data quality issues in existing databases (see Wang et al. [37], Wang et al. [38], Wang et al. [39], Wand et al. [36], and Strong et al, [35]) along with the integration of differing data types to strengthen research (Hoffman et al, [14] and [15]). A 2002 article by Fogarty and Blake [9] concentrated on a narrow issue in data quality, incomplete multivariate data. Work in more recent years has tended to center on policies and structures for firms to implement and support the internal collection of quality in the big data era (Kwon et al. [23], Lee et al. [24], Peltier et al. [31]). While data governance in the context of business/corporate decision-making is certainly extremely important, we found little corresponding consideration of data governance or data quality in IS academic research other than comments and discussion on the importance of data quality (see, for example Bapna et al.[3], and Baesens et al. [1].

## 2b. Replication

# ACCEPTED MANUSCRIPT

Replication in IS research has received and continues to receive attention, albeit on a rather limited basis. For example, the year 2015 saw the initial volume of the AIS Transactions on Replication Research, including Dennis and Valacich’s article [8], “A Replication Manifesto.” The authors argued that there were three forms of replication, exact, methodological, and conceptual. They went on to argue that, “All replications are valuable in advancing science.” While there is ongoing debate about the best forms of and strategies in replication, we certainly concur with and commend the authors for their emphasis on the importance of replication and replicability in IS research.

Niederman and March [30], viewing IS as a social rather than physical science, offered their “particular view of replication: why it is important and how various types of replications may coexist.” Again, while we might argue viewpoints, the significant element is that these authors brought the replication issue forward.

In what follows, our emphasis is on data quality and the consideration of the need to address quality thresholds for each data type, a process that must include data collection processes and validation processes. Research replication relies upon the data quality and clear data collection processes of initial analyses. Thus, we center attention on data quality with only occasional reference to research replication. We do note that if the original and replicated work do not have quality data it really doesn’t matter if you do it twice.

## 3. Data Quality Thresholds

The key questions of interest here are:

1) what characteristics determine the “goodness” or “quality” of data? and,

2) how “good” does data have to be to be acceptable for use in IS Research?

We consider each question in turn. In the Encyclopedia of Database Systems, Gupta [10] offers the following definition of data provenance:

“data provenance: The term ‘data provenance’ refers to a record trail that accounts for the origin of a piece of data (in a database, document or repository) together with an explanation of how and why it got to the present place.”

The HOW and WHY of data collection are characteristics of data quality, but alone fall far short of the entire picture. Our view is that the critical data quality (and subsequently research replication) should include all seven W’s - What, When, Where, How, Who, Which, and Why, to wit:

i) What provides an explanation of exactly what is captured in the data;

ii) When refers to the time at which the data is collected;

iii) Where refers to the location (virtual or real) of the data collection;

iv) How describes the precise process(es) of data collection;

v) Who details the individual(s) involved in the data collection and explains individuals or agents were involved in collection;

vi) Which details instruments or artifacts used in collecting the data; and,

vii) Why provides the set of reason or goals for collecting the data.

Of the seven elements, we place the least emphasis on the “Why” since high quality data gathered for one purpose may turn out to have other unanticipated but valuable purposes. We stress that we view the ability to accurately specify the six remaining elements (What, When, Where, How, Who, and Which) as necessary, but not sufficient, conditions for data accuracy, validity, and research reproducibility. The reason for this “necessary but not sufficient” view is that we can certainly construct data gathering processes for which we can specify What, When, Where, How, Who. and Which but where one or more of the six elements are flawed resulting in inaccurate data. Consider a fully specified process where interviewers choosing individuals to complete a survey are allowed to: 1) follow their own selective bias in choosing who to speak with; 2) choose when to do interviews, perhaps only between 1 a.m. and 3 a.m. at a local bar;

and, 3) decide to vary their tone for each different interviewee. While the process may be fully detailed, the data gathered will not meet the quality standards and replicability we seek.

We start by arguing that there is a “top quality level” for data exhibited by at least one type of data, that is, data generated by and gathered from carefully controlled induced-value laboratory experiments that follow the meticulously detailed approach of Vernon Smith (see, in particular Smith [33]; also see Smith [32] and [34]), who won the Nobel Prize for his body of work in this area. Smith’s sufficient conditions for a controlled laboratory microeconomic experiment include the following<sup>1</sup>:

1) “Non-satiation: Given a costless choice be- tween two alternatives, identical (i.e., equivalent) except that the first yields more of a reward medium (for example, U.S. currency) than the second, the first will always be chosen (i.e., preferred) over the second, by an autonomous individual. Hence utility, U (V), is a monotone increasing function of the monetary reward, U' > 0, where V is dollars of currency”;

2) “Saliency: In order that subject rewards in a laboratory experiment have motivational relevance such rewards must be associated indirectly with the message actions of subjects. Individuals are guaranteed the right to claim a reward which is increasing (decreasing) in the goods (bads) outcomes, x', of an experiment; individual property rights in messages, and how messages are to be translated into outcomes are defined by the institution of the experiment”;

3) “Dominance: The reward structure dominates any subjective costs (or values) associated with participation in the activities of an experiment”;

4) “Privacy: Each subject in an experiment is given information only on his/her own payoff alternatives”; and,

5) “Parallelism: Propositions about the behavior of individuals and the performance of institutions that have been tested in laboratory microeconomies apply also to nonlaboratory microeconomies where similar ceteris paribus conditions hold.”

In addition to satisfying Smith’s five precepts, controlled laboratory experiment researchers have

strived to follow Smith’s careful delineation/documentation of all the participant population, recruitment process, actual participants, and each element in the development, testing, controls, conducting, and outcomes of the experiment. With this care, the What, When, Where, How, Who, and Which are clearly detailed and the resulting data provides the intended measures of the messages, actions, and outcomes. Care and controls drive data quality. Data, including all individual actions and transactions and resulting consequences are typically captured in real time during a controlled experiment. There certainly can be (and have been) arguments concerning what implications can be drawn from analysis of the data, including how broad any generalizations can be given a specific subject participant set. But such arguments involve the limits of implications and not data quality or accuracy.

As noted earlier, quality data is a necessary condition for reproducibility/replicability of research. So how do applications of Smith’s controlled laboratory methodology stack up on reproducibility/replicability? In a very significant article that appeared in March 2016 in Science, Camerer et al. [5] completed careful replication of some 18 experimental economics studies that appeared from 2011 to 2014 in the premier economics journals, the American Economic Review and the Quarterly Journal of Economics. Camerer et al. [5] summarized their findings as follows:

“All of these replications followed predefined analysis plans that were made publicly available beforehand, and they all have a statistical power of at least 90% to detect the original effect size at the 5% significance level. We found a significant effect in the same direction as in the original study for 11 replications (61%); on average, the replicated effect size is 66% of the original. The replicability rate varies between 67% and 78% for four additional replicability indicators, including a prediction market measure of peer beliefs.”

While the replication is far from perfect, the work cited suggested that the record for experimental economics is really quite good. More importantly, we note that the because of the research practices of experimental economists, experiments can be replicated. Camerer et al. [5] argued that two important factors help replicability in experimental economics:

“Two methodological research practices in laboratory experimental economics may contribute to relatively high replication success. First, experimental economists have strong norms about motivating subjects with substantial financial incentives and avoiding the use of deception. These norms make subjects more responsive and may reduce variability in how experiments are performed across different research teams, thereby improving replicability. Second, pioneering experimental economists were eager for others to adopt their methods; to this end, they persuaded journals to print instructions and even original data. These editorial practices created norms of transparency and have made replication and reanalysis relatively easy.”

These investigations on replicability buttress the quality of data generated through controlled laboratory experiments. Thus, we view controlled laboratory experiments satisfying Smith’s conditions along with the provision of all details (and instructions) of the experiment and accompany procedures as the “golden fleece”, if you will, or the upper threshold of data quality and precision.

It is, of course, certainly possible that experiments not satisfying Smith’s conditions and procedures may still yield quantitative data at the upper threshold of quality. The difficulty, in our view, is that it is difficult to determine if the data generated in these experiments is of high quality. In fact, laboratory experiments have been frequently employed in IS research, but seldom have the IS experiments satisfied the conditions set out by Smith nor the two methodological research practices emphasized by Camerer et al.[5]. All too often, the laboratory experiments in the IS domain use participants who receive either nothing, a minor addition of points to a course grade, or a chance in a lottery, all of which are independent of their actual performance in the experiment. In addition, there is often a lack of control on message transmissions or collaboration before or during the process. In short, saliency, dominance, and privacy frequently fall by the wayside.

# ACCEPTED MANUSCRIPT

Having set out a “high threshold,” the next question is, “Can we identify and set out a low threshold, a level at or below which data quality is clearly unacceptable for meaningful IS research?” Based on lengthy years of reviewing papers, reading the reviews from colleagues, and making editorial decisions, we do believe there is such a lower level which we term “inferius quod timeamus” (IQT) (or, from rough Latin to rough English, “below which we should fear”). The unfortunately increasingly common examples of IQT or low data quality, are often data gathered from online survey instruments posted at sites such as social networking sites or chat rooms without any controls or ability to actually identify an actual respondent (more importantly, validate the actual characteristics of respondents) or how many times a respondent might have completed a survey (repetitions perhaps intended to achieve more entrants in a prize drawing for those completing a survey?). Even moderate steps to avoid multiple responses, such as checking for duplicate IP addresses, are not utilized. Researchers frequently claim that such surveys may have “qualifying characteristics” such as “only users of mobile banking apps in the last 30 days respondents based on their response, but what the researcher cannot do is tell if the respondent is lying or not. The researcher has no direct ability to check or validate whether any of the respondents actually meet specified conditions or if the proffered responses are accurate or truthful.

Adding to the problem are surprisingly frequent “sampling” approaches used to generate large “sample” sizes, two examples of which are:

1) Snowball Samples: potential survey participants are urged to recruit other potential participants; and,

2) Convenience Samples: The sample is composed of whatever persons can be most easily accessed to fill out the survey.

In either of these sampling processes, the researcher can use qualifying questions, but cannot directly validate the claimed characteristics of those completing the survey instrument. The focus is on increasing N with no apparent concern for the Who or What in data quality. Several years back, King and He [22] note three coverage problems the problems with such sampling:

“In IS research, a common convenience sampling situation occurs when management students or IT students are presumed to represent practicing managers or IT professionals.”

“A second-level of coverage error is introduced when individual respondents, or some subgroup or sample of them, are taken to represent an organization in which they participate. This potential difficulty is often-unremarked-upon in many studies. Because organizations, by definition, cannot respond to any stimulus, it is often assumed that the perceptions of an individual (e.g. the CIO) or the aggregated perceptions of a set of individuals (e.g.: “users”) reflect the organization’s response.”

“Coverage error may be further amplified when a focal individual (e.g. a CIO) is asked to identify others to be respondents (e.g. users). Even when specific directions are given about how the selection is to be made, the likelihood that a nonrepresentative sample is chosen is increased. “

What is disappointing is that such data quality concerns related to convenience sampling remain all too frequent. In fact, the concept of a “focal individual” being asked to identify other respondents has seemed to frequently degenerate into any and all participants being asked to seek out others to go to a website and complete the survey!

We have set out a “first class” of data quality and a “deficient shoddiness” of data quality. As one might expect, most data lies somewhere between the lower and upper quality thresholds. In the next section, we review the common forms of data used in IS research and suggest characteristics that need to be present for the data to surpass the minimum quality threshold.

## 4. Data Types Used in Current IS Research

# ACCEPTED MANUSCRIPT

Below is a list of current numerical data sources/types that are commonly used in IS research, sometimes in straight empirical analysis or model estimation and sometimes in formally testing a model and/or the model’s implication. We constructed the list based on a good deal of time over the years in reading, reviewing, and making editorial decisions on IS research papers. Though we believe the list to be quite thorough, we make no claim as to total comprehensiveness (or, using more technical terms, we do not claim that the list covers the entire space of numerical or quantitative data):

alternative ways to generate numerical data:

i) interviews;

ii) surveys;

iii) field experiments;

iv) quasi-experiments:

v) controlled laboratory experiments;

vi) empirically observed: a) with accuracy control or b) without accuracy control; and,

vii) third party fee-for-service data – purchased (possibly constructed) for specific research.

This list reflects the subjective views of the authors regarding the IS research data types we have observed. The discussion and consideration of different data types is certainly not original with the current authors (in fact, we noted Morgenstern’s classic work [29] appearing in the 1960’s; a colleague in marketing noted work as far back as McGrath [27].

We now, in turn, consider how each of the seven data types listed above fares on the What, When, Where, How, Who, and Which aspects. We stress that we view the six elements as necessary, but not sufficient, conditions for data accuracy, validity, and research reproducibility. As discussed earlier, we can certainly construct data gathering processes for which we can specify What, When, Where, How, Who, and Which where one or more element is flawed, thus resulting in inaccurate data.

# ACCEPTED MANUSCRIPT

i) interviews - researchers using interview data should certainly be able to carefully specify each of the six elements, but the issue of concern is whether subjectivity in interviewing (e.g., - tone, inflection, personal bias) can ever be eliminated - if the subjectivity cannot be eliminated, then the What and How are murky;

ii) surveys - the question with data collected through surveys is whether any of the six elements can be carefully detailed. Even if the survey questions are carefully constructed and the researcher specifies to Who surveys are sent, issues often remain. For example, when surveys are sent to companies, the actual individual, the Who, that completed the survey may not be identified. Concerns then arise regarding whether the actual Who had the necessary knowledge to provide accurate information. Good survey work techniques can reduce these concerns, but there is little a researcher can do to determine if participants are being truthful or actually possess the knowledge required to accurately respond. Surveys posted on-line without controls and validation mechanisms in place lie at the lowest data quality level since much of the What, When, Where, How, Who, Which information cannot be determined;

iii) field experiments - in his 1985 treatise, A. M. Jenkins [20] (see Ch. 6) defined the field experiment approach as follows:

“This methodology guides research that takes place in a “natural setting.” The researcher manipulates the independent variables while trying to control the most important intervening variables. The researcher then measures the effects of the independent variables on the dependent variables by systematic observation of human subjects. The form of “systematic observation” is the basis for distinguishing between various forms of field studies.”

This definition/explanation by Jenkins [20] emphasizes control and manipulation by the researcher and places the field experiment close to the level of a fully controlled laboratory experiment on the hierarchy of the quality of the data generated. The care taken and control exercised by the researcher will determine if the six W’s are clearly identified in any specific field experiment. The details reported need to carefully delineate both of these elements while making sure to fully provide the What, When, Where, How, Who, Which information;

# ACCEPTED MANUSCRIPT

iv) quasi-experiments - here the data gathering involves an “after the fact” attempt to arrange occurrences in ways that closely mimic the process that would have occurred in a controlled field experiment. For example, in propensity score analysis (PSA), comparisons are performed over matched pairs of observations where the goal is to closely match variables except the treatment variable (causal difference making variable, if you will). In this process, the researcher does not have control or manipulative ability, but rather analyzes the available data in an attempt to identify sets of observations that reflect the same characteristics that control would have yielded. That is, paired observations are sought so that, for each pair in the data set, the only difference (as it would be in a controlled experiment) is that one observation has the treatment present and the paired observation does not (see Mithas and Krishnan [28], and Bai et al. [2], for detailed examples of such data and for examples of formal matching processes). If done carefully, with full disclosure of steps and processes, quasi-experiments can certainly provide data that exceeds the quality threshold. This will only occur if the processes can be sufficiently detailed and validated so that the particulars provide the What, When, Where, How, Who, and Which. The process is certainly not clean enough to be equivalent to the experimental economists’ controlled experimentation, but the data may still satisfy the six W’s;

v) controlled laboratory experiments - as discussed earlier, experiments following the careful procedures, including incentives and controls, utilized by experimental economists form one example of the high quality data benchmark. If controlled experiments in IS research follow these guidelines, then the resulting data should exceed the high quality threshold. Too often, unfortunately, controlled experiments in IS research fall short due to failing to utilize sufficient performance base incentive rewards or failure to employ careful experimental controls. These inadequacies can, however, be remedied so that the data from controlled experiments in IS can reach the replicability levels Camerer et al. [5] found in the work of experimental economists;

vi) empirically observed: we divide this data type into two subgroups or categories:

# ACCEPTED MANUSCRIPT

a) empirically observed data in a setting with accuracy control(s): this category includes empirically observed data collected where there are costs or penalties for inaccurate reporting - examples would include tax information required by law to be provided to the government, certified accounting data, actual auction market bids, and certified or legally required performance data. In these cases, it is often the case that the What, When, Where, How, Who, and Which details are clear and detailed; and,

b) empirically observed data in a setting without accuracy control(s) - when controls or requirements are not present and enforced, elements of the What, When, Where, How, Who, and Which will often be unknown or unreliable. Consider data on production performance where the individual performing the analysis is not listed or the precise nature of measurements are not provided. Consider selfreported and non-verified age or income data that resides in a corporate data base.

vii) third party fee-for-service data – purchased (possibly constructed) for specific research - such data will almost always fail the What, When, Where, How, Who, and Which standard because the fee-for-service company will often not openly share the information lest the researchers avoid the middle-man in the future.<sup>2</sup> If our experience in reviewing research is representative, the number of such data gathering fee-for-service companies are expanding rapidly and fee-for-service data growing in prominence. The author still has the responsibility to demonstrate the quality of the data. Simply stating that the third party says the data is of high quality is hardly sufficient for a decision maker to rely upon the results drawn. Data gathering vendors do not share their idiosyncratic knowledge - that is, verifiable details on the actual participants. This is an example of the well-known principal-agent problem. Here, the researcher’s goal should be accurate data while the vendor’s (data provider) goal would seem to be centered on providing sufficient survey responses to satisfy the agreed upon or contracted sample size, N. Without total transparency (perfect monitoring) the researcher has no way to validate that the population from which participants were drawn actually meet any specified criterion, let alone be in a position to check the accuracy of the data provided. The contracts and information flows between the researcher and third party and the contracts between the third party and survey responder are critical in putting a researcher into a position to guarantee the data quality from a third-party source. For example, a contract that pays for completing all questions is problematic.

Each of the seven data types discussed above may include cases or examples that lie high on the data quality spread. But all may also include cases where the data quality is below the low threshold. No data type is inherently of low quality and no data type guarantees high quality, though we have noted problems that we believe are more likely to occur with certain data types. In each setting, in each case, as researchers we must address the data quality issues and provide the information necessary to determine What, When, Where, How, Who, and Which. We suggest that the reader think back on recent IS research papers that they have reviewed or read, and consider the following questions:

i) was data quality addressed as an important issue?

ii) what details of data gathering were included? and,

iii) did the authors provide the information necessary to determine What, When, Where, How, Who, and Which?

Similarly, we ask any reader of recent IS research papers to consider how much emphasis, explanation, and details were provided regarding data quality versus the amount of detail and effort placed on explaining the choice of econometric modeling and estimation? The fact is that SEM modeling or PLS variants or any of the plethora of modeling and estimation processes only take on meaning or value if the data meet quality standards. Issues linked to poor data quality

# ACCEPTED MANUSCRIPT

cannot be overcome by sample size, intricate manipulations or esoteric modeling and/or estimation processes. In short, quality data is the “sine qua non” of meaningful research. This holds true in the sciences and it holds true in IS.

## 5. Can we establish Quality Thresholds for each of the Seven Data Types?

To emphasize how concerned we should be about data quality in IS research, consider the disconcerting examples below of IS survey and third-party data rationale. The “quotes” are edited, merged, and paraphrased from recently published IS articles for illustration purposes.

## Web Surveys and Snowball Techniques

“The statement of the survey purpose and a link to the survey were posted. The snowball technique was used to increase the sample number by requesting participants to share the link. Over 700 responses were collected. Incomplete and questionable questionnaires were excluded after careful examination. We finally obtained 350 valid data points.”

Here, questions abound. Little is known about the data sample and yet, after an unclear data gathering process followed by an undefined exclusion process, the remaining data becomes valid.

## Third Party Data

Researchers have offered justifications for third party data such as “the vendor has access to a broad pool of participants” and “the vendor employs careful screening and validation processes.”

There is typically no documentation of the referenced processes or the verifiable characteristics of the broad pool.

The publishing of articles including such data gathering activities do not seem to have caused a ripple in the IS research community. In contrast, we present the newspaper clamor described below over survey data in the political polling arena. Here, the survey outcomes can have import. To the newspapers, outcomes apparently do matter and there are concerns about data quality. The New York Times offers its set of standards for polling or political surveys at http://www.nytimes.com/packages/pdf/politics/pollingstandards.pdf. e New York Times prescribed standards, problems have occurred. Consider the problems detailed in a Washington Post report [19]:

“A new state election polling collaboration between the New York Times, CBS News and Internet Pollster YouGov has drawn an unusual public rebuke from the leading organization of survey researchers, adding fuel to a fiery debate over what makes a poll "good" or "bad."

The decision to sponsor non-probability Internet polling marks a stark shift in standards for the New York Times. Prior to the collaboration, Times public standards warned of numerous problems with such surveys, including that opt-in surveys often pay respondents to complete polls, that Internet access is not "sufficiently widespread" and access is not evenly distributed across the public. The previous standards stated that for a poll to be "worthy of publication" it "must be representative, that is, based on a random sample of respondents." But the Times' standards changed after their new polling collaboration was published. The revised document indicates that decisions about what polls to publish will be made on a case-by-case basis while new standards are being produced.

AAPOR criticized this decision to adopt a new, piecemeal approach, without an explicit standard justifying their use. "Standards need to be in place at all times precisely to avoid the “we know it when we see it (or worse yet, ‘prefer it’)” approach, which often gives expediency and flash far greater weight than confidence and veracity." (https://www.washingtonpost.com/news/thefix/wp/2014/08/04/how-the-polling-establishment-smacked-down-the-new-york times/)

Here the popular press set forth data quality standards and raised concerns when the standards appeared to have been violated. The surveys have import and this results in concerns about data quality. Where are the comparative standards for IS research-related surveys? Is the lack of concern about data quality a reflection of IS academic research being viewed as of little import? Where are the careful details, the critical information, that answer What, When, Where, How, Who, and Which?

As we argued above, no data type is inherently of low quality and no data type guarantees high quality, though we have noted problems that we believe are more likely to occur with certain data types. It is our view that it is incumbent for researchers to establish data quality thresholds for all data types and, in each use of data, provide the information necessary to determine What, When, Where, How, Who, and Which. To do less risks the credibility of the researchers and the research results. The loss of this credibility will ultimately sever the connection between the body of academic research and society’s decision makers -- a significant potential loss of social welfare.

## 6. Where from here? A Call for Data Quality Forum Contributions

Ok, some may argue that the above was an interesting read (at least we hope it was interesting) from two academics venting their frustration. While we can learn from looking back, our goal must be to deliver high quality research in the future. We need to move onward and upward! We begin “moving on” by offering an opportunity for a forum where others can argue as apologists, using Mirriam-Webster definition of “apologist” as “one who speaks or writes in defense of someone or something” (https://www.merriamwebster.com/dictionary/apologist). An accompanying CFSP (call for Short Papers) requests your submissions either responding to this paper or, more importantly, detailing quality thresholds for any or all of the seven quantitative data types listed above. We also welcome submissions detailing and arguing for journal policies that emphasize data quality and reproducibility.

## ACCEPTED MANUSCRIPT

As in this presentation, the focus must be on quantitative data only. We save discussion of qualitative data for another time. Submissions should be no more than fourteen double-spaced pages including all material. Arguments should be clear and concise. Working with guest reviewers (and possibly an additional guest editor), we will select the clearest, most erudite submissions with a goal of balancing out the discussions of each data type. The selected submissions will appear in an upcoming edition of the journal, either as a special section or a special volume depending on the number and quality of submissions. Fire away!

## References

[1] Baesens, B., Bapna, R., Marsden, J. R., Vanthienen, J., & Zhao, J. L. (2014). Transformational issues of big data and analytics in networked business. MIS Quarterly, 40(4)

[2] Bai, X., Marsden, J. R., Ross Jr. W. T., and Wang, G. (2015). “Relationships among minimum requirements, Facebook likes, and Groupon deal outcomes.” ACM Transactions on Management Information Systems, 6.3: 9

[3] Bapna, R., Goes, P., Gopal, R., and Marsden, J.R., (2006) “Moving from Data-Constrained to Data-Enabled Research: Experiences and Challenges in Collecting, Validating, and Analyzing Large-Scale E-Commerce Data, Statistical Science, 21(2), 116-130

[4] Bauer, Henry Hermann. "How Medical Practice Has Gone Wrong: Causes of the Lack-of-Reproducibility Crisis in Medical Research." Journal of Controversies in Biomedical Research 1.1 (2015): 28-39.

[5] Camerer, C., Dreber, A., Forsell, E. et al. (2016), “Evaluating Replicability of Laboratory Experiments in Economics” Science, 351, 1433–1436.

[6] Churchill, Gary A. (2014) "When are results too good to be true?" Genetics, 1982: 447-448.

[7] Collins, Francis S. and Tabak, Lawrence A. (2014) “Policy: NIH plans to enhance reproducibility, Nature, January 27, 2014

[8] Dennis, A. R., & Valacich, J. S. (2014). “A replication manifesto.” AIS Transactions on Replication Research, 1(1), 1.

[9] Fogarty, D. J., and Blake, J. (2002). "Utilizing recent advancements in techniques for the analysis of incomplete multivariate data to improve the data quality management of current academic research." Quality and Quantity 36.3: 277-289.

[10] Frye, S. V., Arkin, M. R., Arrowsmith, C. H., Conn, P. J., Glicksman, M. A., Hull-Ryde, E. A., & Slusher, B. S. (2015). Tackling reproducibility in academic preclinical drug discovery. Nature Reviews Drug Discovery, 14(11), 733.

[11] Gratzer, W. (2013). Trouble at the lab. Economist, 302 (5911), 774-5.

[12] Groves, R. M. (1987) "Research on survey data quality." The Public Opinion Quarterly. 51: S156-S172.

[13] Gupta, A. (2009). "Data provenance." Encyclopedia of Database Systems. Springer US, 2009. 608-608

[14] Hoffman, E., Marsden, J.R., Jacob, V. S., and Winston, A. (1987). “Development, Use, and Verification of Expert Systems in Modeling Micro-economic Systems.” P. 411–428 in Proceedings of the NATO Advanced Study Institute on Decision Support Systems: Theory and Application, edited by Clyde Holsapple and Andrew B. Whinston. Berlin: Springer. 411-428

[15] Hoffman, E., Marsden, J.R., and Whinston. A., (1990). “Laboratory Experiments and Computer Simulation: An Introduction to the Use of Experimental and Process Model Data in Economic Analysis.” Advances in Behavioral Economics, 2:1–27

[16] https://www.economist.com/leaders/2013/10/21/how-science-goes-wrong

[17] http://www.nytimes.com/packages/pdf/politics/pollingstandards.pdf

[18] https://www.psychologicalscience.org/observer/replication-education

[19] https://www.washingtonpost.com/news/the-fix/wp/2014/08/04/how-the-pollingestablishment-smacked-down-the-new-york-times/

[20] Jenkins, A. M. (1985). "Research methodologies and MIS research." Research Methods in Information Systems. 103-117.

[21] Jump, Paul, “Reproducing results: how big is the problem?,” Times Higher Education (THE), https://www.timeshighereducation.com/features/reproducing-results-how-big-is-theproblem 1/19/2016

[22] King, William R. and He, Jun (2005) "External Validity in IS Survey Research," Communications of the Association for Information Systems, 16:880- 89

[23] Kwon, Ohbyung, Namyeon Lee, and Bongsik Shin. (2014). "Data quality management, data usage experience and acquisition intention of big data analytics." International Journal of Information Management 34.3: 387-394.

[24] Lee, Y., Madnick, S., Wang, R., Wang, F., & Zhang, H. (2014). A Cubic Framework for the Chief Data Officer: Succeeding in a World of Big Data. MIS Quarterly Executive, 13.1

[25] Li, Fei, et al. (2015). "Authentication of experimental materials: A remedy for the reproducibility crisis?" Genes & Diseases 2.4

[26] Maniadis, Zacharias, Fabio Tufano, and John A. List. (2015) "How to make experimental economics research more reproducible: Lessons from other disciplines and a new proposal." Replication in Experimental Economics 215-230.

[27] McGrath, Joseph E. (1982), “Dilemmatics: The Study of Research Choices and Dilemmas,” American Behavioral Scientist, 25 (November/December), 179-210.

[28] Mithas, S., and Krishnan, M.S. (2009). “From association to causation via a potential outcome approach,” Information System Research 20.2: 295-313.

[29] Morgenstern, O. (1963). On the accuracy of economic observations. Princeton University Press.

[30] Niederman, F., and March, S. (2015). “Reflections on Replication.” Transactions on Replication Research, 1 (1 – paper 7): 1-16.

[31] Peltier, James W., Debra Zahay, and Donald R. Lehmann (2013). "Organizational learning and CRM success: a model for linking organizational practices, customer data quality, and performance." Journal of Interactive Marketing 27.1: 1-13.

[32] Smith, V. L. (1976). “Experimental economics: Induced value theory, The American Economic Review, 66(2), 274-279.

[33] Smith, V. L. (1982). “Microeconomic systems as an experimental science,” The American Economic Review, 72(5), 923-955.

[34] Smith, V. L. (1994). “Economics in the laboratory,” Journal of Economic Perspectives, 8(1), 213-131.

[35] Strong, D. M., Lee, Y. M., and Wang. R. Y. (1997) "Data quality in context." Communications of the ACM, 40.5: 103-110.

[36] Wand, Y., and Wang, R. Y. (1996). "Anchoring data quality dimensions in ontological foundations." Communications of the ACM. 39.11: 86-95.

[37] Wang, R. Y., Reddy, M. P., and Kon, H. B. (1995). "Toward quality data: An attributebased approach." Decision Support Systems 13.3: 349-372.

[38] Wang, R. Y. (1998). "A product perspective on total data quality management." Communications of the ACM 41.2: 58-65.

[39] Wang, R. Y., Ziad, M., and Lee, Y. M. (2006). “Data quality”. Vol. 23. Springer Science & Business Media
