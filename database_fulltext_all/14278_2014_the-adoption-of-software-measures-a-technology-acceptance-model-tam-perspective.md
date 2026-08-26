---
otero_id: 14278
otero_key: "Y4XQBW2T"
title: "The adoption of software measures: A technology acceptance model (TAM) perspective"
authors: "Linda G. Wallace; Steven D. Sheetz"
year: "2014"
journal: "Information & Management"
doi: "10.1016/j.im.2013.12.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The adoption of software measures: A technology acceptance model (TAM) perspective

Linda G. Wallace <sup>a,</sup>\*, Steven D. Sheetz <sup>b</sup>

<sup>a</sup> 3007 Pamplin Hall (0101), Virginia Tech, Blacksburg, VA 24061, United States <sup>b</sup> Virginia Tech, Blacksburg, VA 24061, United States

## A R T I C L E I N F O

Article history: Received 29 March 2012 Received in revised form 25 December 2013 Accepted 31 December 2013 Available online 8 January 2014

Keywords: Software measurement Structural equation modeling Technology acceptance mode

## A B S T R A C T

The use of software measures for project management and software process improvement has been encouraged for many years. However, the low level of acceptance and use of software measures in practice has been a constant concern. In this paper we propose and test a model which explains and predicts the use of software measures. The model is based on the technology acceptance model (TAM) and operationalizes the perceived usefulness construct according to the ‘‘desirable properties of software measures.’’ Our research provides guidance for software engineers in selecting among different software measures and for software metrics coordinators who are planning measurement programs. Published by Elsevier B.V

## 1. Introduction

The concepts underlying quality management have been applied to numerous domains, and in the past several decades they have been used in an attempt to improve software quality. However the assessment of quality requires a certain amount of quantification in order to measure improvement. Quantifying software quality is the focus of research into software measurement. Software measurement techniques promise to improve control of the development process, reduce development time and costs, and produce higher quality software [91]. Software measures have been touted as essential resources for improving quality and controlling cost during software development (e.g. [46,64]). These promises have fueled a great deal of research which, in turn, has led to a proliferation of measures. Thousands of measures have been proposed since the mid 1960s [39]. Zuse [107] notes that over 500 inter-disciplinary references and over 100 different measures exist for the area of software complexity measurement alone.

Despite the large number of available software measures, the adoption and application of these measures by practitioners has been limited [102]. The lack of effective software measurement programs to evaluate and monitor project progress, thus identifying problems before they worsen, provides one possible explanation for the high rate of software project failure [35]. Yet, more than 80% of software measurement initiatives fail within the first 18 months [92]. Explanations of this phenomenon usually center on the argument that the measures are difficult to understand and implement. In addition, some of the measures have limited applicability, have not been thoroughly validated, or their usefulness is not readily apparent [107]. Further complicating the field is a lack of data on measurement programs in organizations. The result is a confusing situation for potential users of software measures in urgent need of techniques to aid in the development of quality software. This paper focuses on the reasons why software developers and project managers may or may not accept a software measure.

In this context, a ‘‘software measure’’ is defined as any tool that provides a quantitative assessment of the degree to which a software product or process possesses a given attribute, such as size, complexity or quality [68]. Understanding why individuals accept new software measures is an important step in increasing the use of measures within organizations and potentially improving the measures themselves. The research question we are attempting to answer is ‘‘What factors influence an individual’s acceptance of a software measure?’’. To address the research question we have developed and tested a model to explain the acceptance of software measures.

We believe the lack of a theoretical foundation for this stream of research has limited the contributions of previous research and prevented organizations from understanding what makes a practical or useful software measure. Understanding the effects of the perceived usefulness and ease of use of software measures is necessary for the development of adoptable measures and the design of practical measurement programs that can lead to higher quality software. Theory-based research on software measurement adoption can provide insights into why existing measures are used (or not used) in practice. It can help software measurement researchers describe how measures address the concerns of potential adopters and help software development practitioners make informed decisions as to what measures to use in their organizations.

This paper creates a theoretical foundation for research in this area by developing a model for explaining and predicting the adoption of software measures. The model is based on the technology acceptance model (TAM) and the factors that prior research suggests are most clearly related to adoption – perceived usefulness and perceived ease of use. The remainder of this paper is organized as follows. The next section briefly reviews the technology acceptance model, the desirable properties of software measures, and presents a research model for assessing the adoption of software measures. The third section describes the instrument development and validation process. The fourth section presents the results. The fifth, sixth, and seventh sections suggest the implications for research and practice as well as limitations with the current research. The last section highlights the overall conclusions drawn.

## 2. Background and theory

Software measurement programs are used by organizations as a means for controlling the cost of software development and the quality of the resulting software [15]. Such programs are usually implemented with the belief that they will improve software development and the management of the development process. This belief is based on the rationale that you cannot improve something without first measuring it [47]. The goal of software measurement programs is to provide feedback that can allow an organization to improve the management of their software development process, thereby improving productivity and quality.

A software measure is a method of quantitatively determining the extent to which a software process, product, or project possesses a certain attribute [31]. By collecting measures related to software development, managers and engineers can make adjustments to development processes and/or products in response to cost, schedule, or other constraints. Previous studies have confirmed the effectiveness of some software measurement programs [36,50,84]. However, many companies either do not have software measurement programs, or the programs eventually fail when the measures stop being used [50,84,14,62]. Given that software measurement programs can help organizations better manage software projects [15], research is needed to identify the factors that can affect measure use. The primary goal of this paper is to determine what properties of a software measure lead to its adoption by software engineers and managers.

## 2.1. The technology acceptance model (TAM)

Adoption theories attempt to explain the process people go through when deciding to perform an activity for the first time [98]. The Theory of Reasoned Action (TRA) [3] suggests that people form intentions to adopt a behavior or technology based on their beliefs about the consequences of adoption. TRA has been used to understand the adoption of behaviors, technologies, or advice. Building on TRA, Davis [32] developed the technology acceptance model (TAM). TAM attempts to explain why individuals choose to adopt or not adopt a particular technology when performing a task. TAM has been expanded and adapted by a number of researchers and has been applied to many different technologies including spreadsheets [73], voice mail [96] and object oriented technologies [52].

There are a large number of studies that have looked at how TAM can explain the acceptance of software development products, but researchers have realized that TAM can also be used to explain the acceptance of software development processes [52]. For example, Chau [24] used TAM to explain CASE tool usage and a few researchers have begun to explore whether TAM can be used to explain acceptance of software measurement programs (e.g. [27,28,100]). However, these earlier studies which used TAM to investigate software measure adoption used correlations and regression analyses [27,28,100], rather than testing the constructs in a nomological net. Our research goes beyond this earlier work by investigating the relationships proposed by TAM through the use of structural equation modeling. Furthermore, we model perceived usefulness as a second order construct with multiple subdimensions in order to better capture its richness and meaning. The following paragraphs describe the theoretical underpinnings of the model that we tested and Sections 3 and 4 describe the methodology and analysis techniques that we used.

According to TAM, two variables impact adoption: perceived usefulness and perceived ease of use. Perceived usefulness refers to the degree to which an individual believes that using a particular technology would enhance his or her job performance [33]. Perceived ease of use refers to the degree to which an individual believes that using a particular technology would be free of physical and mental effort [33]. TAM purports that if a technology or innovation enhances a person’s performance and does not greatly increase the effort required to perform a function, it is considered useful and easy to use, and the person will be more likely to adopt the technology, service, or behavior. The validity and reliability of the perceived usefulness and perceived ease of use variables in TAM have been supported by many studies (e.g. [1,34,58,97]).

TAM can also be applied to the adoption of software measures. Umarji and Seaman [99] have proposed that TAM can be applied to software process improvement initiatives, including software measurement programs. They suggest that the reasons for undertaking new initiatives are similar to the reasons for introducing a new technology (i.e., budget and schedule considerations, changing industry standards, etc.) [99]. As a result, the ‘‘perceived usefulness’’ and ‘‘perceived ease of use’’ constructs would still be relevant when trying to anticipate who will adopt and begin using a software measure. Several other researchers have also investigated the possibility of applying TAM to the adoption of software measures and shown favorable results (e.g. [27,28,75]). Therefore, we feel that TAM is a relevant theory on which to base an examination of software measure adoption.

Specifically, we expect that when individuals involved in systems development believe that using a particular software measure will increase the quality of the software development process or the product (perceived usefulness) they will be more likely to use the measure. Software measures must be perceived as useful, otherwise managers and developers will use them reluctantly and possibly inappropriately [50,48]. This corresponds with existing research which has shown that perceived usefulness can predict user adoption, both with current and future selfreported usage measures [33].

There is growing body of literature which has looked at antecedents of perceived usefulness in the context of TAM [98,2,66,101]. These studies have tried to understand predictors of perceived usefulness as they relate to the adoption of technology and information. However, some researchers suggest perceived usefulness may be multidimensional and may be conceptually too broad to be practically applied [76]. For example, common indicators for perceived usefulness have included the following:

Using the Technology increases my productivity. Using the Technology improves my job performance.

Using the Technology enhances the quality of my work. The advantages of using the Technology outweigh the disadvantages.

Using the Technology makes it easier to do my job.

The Technology is useful in my job.

While powerful in the context of the theory, such items have limited explicative abilities. That is, we do not know why respondents believe they are performing better, being more productive or see the technology as useful. If we cannot understand which characteristics of a technology influence perceived usefulness we cannot determine how to influence perceptions of those characteristics to encourage adoption. Although prior research has emphasized the importance of perceived usefulness, few studies have investigated what makes a technology useful [10,16,95]. Rather, perceived usefulness has been treated as a unidimensional construct that few researchers have attempted to dissect [16,83]. These studies suggest that a deeper understanding of the perceived usefulness construct may be available and further investigation is warranted.

Sub-dimensions of perceived usefulness can be identified for the usefulness of software measures. These dimensions are called the ‘‘desirable properties of software measures’’ and provide a context for extending the theory by increasing applicability to practice. While theoretical purists will object to the loss of parsimony realized by including sub-dimensions of perceived usefulness in TAM, rather than the single construct, we believe this tradeoff can be worthwhile in many contexts if it provides greater practical applicability of the theory to the domain.

Similarly, we believe that if developers perceive that a measure is easy to use (perceived ease of use) they are more likely to adopt it. Not surprisingly, ease of use is a desirable property of software measures.

## 2.2. Desirable properties of software measures

Early in the evolution of software measurement research, the primary concerns were determining what characteristics of software should be measured and how the measures should be derived and validated. Eventually software engineering researchers became concerned with the use of the measures they created. In the literature, this concern is evident in the ‘‘desirable properties’’ of software measures (e.g. [57,69,104]). ‘‘Desirable properties’’ are those characteristics of software measures which increase both their effectiveness and their practical application. The following paragraphs identify four desirable properties which, if possessed by a software measure, should increase its perceived usefulness. We also discuss the desirability of a measure’s ease of use, although in the context of TAM ‘‘ease of use’’ is a construct which is independent of perceived usefulness. Table 1 summarizes the five desirable properties of software measures that are included in our model.

Table 1  
Desirable properties of software measures.

<table><tr><td>Construct</td><td>Definition</td></tr><tr><td>Language independence</td><td>The degree to which computation of the measure does not depend on the programming language used.</td></tr><tr><td>Prescriptiveness</td><td>The ability of the software measure to not only diagnose, but recommend or suggest solutions.</td></tr><tr><td>Validity</td><td>The degree to which the software measure has measurement validity and the degree to which it has been empirically tested and supported.</td></tr><tr><td>Life cycle applicability</td><td>The degree to which the measure can be applied to products and processes throughout the software development life cycle.</td></tr><tr><td>Ease of use</td><td>The degree to which the measure is easy to use.</td></tr></table>

## 2.2.1. Language independence

The degree to which computation of a measure does not depend on the programming language used is referred to as language independence. Lines of code (LOC) was one of the first software measures. However, the emergence of multiple programming languages quickly demonstrated the limitations of counting the lines of code. For example, a lines of code measure will count a line of COBOL the same as a line of assembly language, even though the two languages are very different and the effort required to write the same number of lines of code in each language varies widely [5]. This limitation inhibits comparability across projects implemented in different languages. Furthermore, while individual projects often are written in a single language, many organizations have existing systems written in multiple languages that require maintenance. In the 1970s, language independence provided the impetus for the development of software complexity measures that were not based on lines of code, including pioneering efforts by McCabe [74], Halstead [51], and Albrecht [4]. The need for language independence has rarely been questioned since, as lines of code measures are heavily dependent on the language used for the development efforts. Thus, a measure that can be used and interpreted consistently regardless of programming language would likely be perceived as more useful than a measure that is only applicable to one particular programming language.

## 2.2.2. Prescriptiveness

The Goal-Question Metric [13] was developed to tie the use of software measures to the goals of the organization, thus going beyond evaluations focused on simple characteristics, such as measurement scale. Hall and Fenton [50] assert that software measurement programs that do not relate to the specific goals and outcomes desired by the organization are doomed to fail. Software engineering researchers have embraced these calls with many studies that attempt to establish links between software measures and organizational goals. This stream of research is evidence of the desire for prescriptiveness, i.e., the ability to use the measure to obtain organizational goals.

A measure is considered to be prescriptive if it can not only diagnose problems but suggest solutions. Managers can use some measures to determine if a tool, language, or environment is more productive when compared to others [5,71,90]. Measures can be used to identify unproductive elements of the software development process and monitor scope creep, thereby allowing managers to better diagnose problems and suggest solutions. The more that measurement results provide insights into the development process the more likely the measure will be used [46]. The most significant intended benefit of measures is that they are supposed to provide information to support quantitative managerial decision-making during the systems development life cycle (SDLC) [94]. A measure that has prescriptive properties would be considered to be highly useful, as it identifies resources or processes to be adjusted and predicts how different adjustments will change the measure.

## 2.2.3. Validity

Validity is often mentioned as a necessary property for successful measures (e.g. [57]). A measure is valid if it measures what was intended to be measured. Fenton [37, p. 205], addresses validity more formally as ‘‘Validating a software measure in the assessment sense is equivalent to demonstrating empirically that the representation condition is satisfied for the attribute being measured.’’ Baker [12] said that validity exists if a measure has undergone a ‘‘process of ensuring that the measure is a proper numerical characterization of the claimed attribute’’. In other words, it is important that the measure is a credible representation of what it is intended to measure.

In order to achieve repeatability, the entity (software object) and attribute (property) you want to measure and the unit of measure must be defined. Kitchenham, Pflegger, and Fenton [68] provide an extensive definition of validity consisting of: attribute validity, unit validity, instrument validity and protocol validity. They go on to identify approaches for theoretic and empirical validation. Khoshgoftaar et al. [67] indicate that validation of a measure must show that the measure facilitates improved quality predictions. Measures that depend on subjective estimates rather than objective data have often been criticized [72]. Therefore, validity seems to be a key component of measure usefulness.

## 2.2.4. Life cycle applicability

This property refers to the degree to which a measure can be repeatedly applied throughout the SDLC. It is motivated by the limitations of other measures that can only be calculated after code has been produced. For example, cyclomatic complexity can only be calculated during the implementation and unit testing phases when code has been produced and is available to be analyzed [82]. Limitations of such measures were a motivation for the development of other software measures, such as function points [4]. If a measure can be calculated and used throughout the entire SDLC (e.g., before code exists), then it can be used to improve many different aspects of the software development process. Function points are often estimated early in the SDLC and then recalculated as development continues in order to aid project management [40]. If a measure can be applied throughout the SDLC it would be considered to be a more useful measure than one that could only be applied to a finished system.

## 2.2.5. Ease of use

Ease of use is a well-established construct in TAM. Less complex innovations are easier to understand, easier to implement, and less frustrating to use; thus, all else being equal, the lower the perceived complexity, the more likely the innovation will be adopted. Kafura and Reddy [65] suggest that that it is valuable to have software measures that are intuitively easy to understand. Similarly, previous research has suggested that software measures should be simple and straightforward and easy to use or the software measurement program is more likely to be terminated [50,84,45]. Also, the effort required to collect the information required for the measure should not add significantly to the organizational workload [46]. Thus, our model includes ease of use; and to be consistent with TAM we model it as a separate construct, not as a sub dimension of perceived usefulness. This consistency also supports our use of TAM in a software measures context, as it is accepted that measures that are easier to use are more likely to be adopted [38].

## 2.3. Research model

Our research model (shown in Fig. 1) is a typical TAM model in terms of the relationships between perceived usefulness, perceived ease of use, and use. The desirable property, ease of use, is the same as the perceived ease of use construct found in TAM. However, we have added sub-dimensions of perceived usefulness based on the first four desirable properties for the reasons described above, i.e., higher levels of a desirable property reflect higher levels of usefulness. We are suggesting that the perceived usefulness of a software measure can be assessed by the potential adopter’s perceptions of the sub-dimensions of language independence, prescriptiveness, validity, and life cycle applicability.

![](/api/attachments/Y4XQBW2T/fulltext/images/2deaa7eef905dd63959ba9f0403cf7d3500c9152ce8960cfaba52abf93150ec8.jpg)  
Fig. 1. A TAM-based model of software measure use.

Measures that have higher levels of these properties will be perceived as more useful. The model has the following hypotheses:

H1: Perceived ease of use (PEOU) will have a significant positive impact on perceived usefulness (PU).

H2: Perceived ease of use will have a significant positive impact on Use.

H3: Perceived usefulness will have a significant positive impact on Use.

Similar to other researchers (e.g. [106]) we used ‘‘use’’ and not behavioral intentions as the dependent variable. Behavioral intentions may lack practical value in predicting long-term future use [19]. Since we wanted to predict usage behavior rather than intentions to use we used ‘‘measure use’’ as the dependent variable. Also, like previous research we are hypothesizing that PEOU will influence PU but PU will not influence PEOU. The subdimensions of perceived usefulness are also measures of the perceptions of the potential adopters. Therefore, in Fig. 1 each of the sub-dimensions of PU begins with the word ‘‘perceived’’.

## 3. Instrument development and validation

In order to test the research model we used a web-based survey with both demographic questions and items designed to measure the constructs in the research model. There were no existing measures related to the desirable properties of software since prior research in this area has not been empirical-based. Therefore, in the first stages of the research, both authors wrote items to describe each of the desirable properties of software measures. These items were integrated into a comprehensive list and changes were made until agreement was reached. Then the items were randomly arranged into a document and 20 faculty members who were familiar with software measures were asked to group similar items together. The goal of this step was to provide an initial check into the construct validity and reliability of the categories and item measures. Any items that were not placed with the others in their intended category by at least 70% of the respondents were candidates for revision or deletion. Care was made not to lose content when items were deleted or modified. Ease of use was measured using five items capturing aspects related to complexity and mental effort in using a software measure. The dependent variable was operationalized through a single-item measure which asked the respondent to respond to the statement ‘‘I use this software measure on my projects’’ on a five-point scale ranging from ‘‘never’’ to ‘‘always’’.

Table 2 Final survey items.

<table><tr><td colspan="2">Final survey items.</td></tr><tr><td colspan="2">Perceived Language Independence (LI)</td></tr><tr><td>LI1</td><td>The choice of programming language does not affect the ability to calculate the measure.</td></tr><tr><td>LI2</td><td>The calculation of the measure is not affected by the differences in programming languages.</td></tr><tr><td>LI3</td><td>The measure is programming language independent.</td></tr><tr><td colspan="2">Perceived Prescriptiveness (PS)</td></tr><tr><td>PS1</td><td>The measure improves the ability to identify problems with the software.</td></tr><tr><td>PS2</td><td>The measure makes it easier to identify methods for improving the software.</td></tr><tr><td>PS3</td><td>It is easier to solve problems when using the measure.</td></tr><tr><td colspan="2">Perceived Validity (VA)</td></tr><tr><td>VA1</td><td>The measure has been rigorously tested in the field.</td></tr><tr><td>VA2</td><td>The measure has been extensively empirically validated.</td></tr><tr><td>VA3</td><td>The measure is highly credible.</td></tr><tr><td>VA4</td><td>The purpose of the measure is very clear.</td></tr><tr><td colspan="2">Perceived Life Cycle Applicability (LC)</td></tr><tr><td>LC1</td><td>The measure can readily be used throughout the entire development process.</td></tr><tr><td>LC2</td><td>The measure can easily be used repeatedly throughout a development process.</td></tr><tr><td>LC3</td><td>The measure can support development in both early and later stages.</td></tr><tr><td colspan="2">Perceived Ease of Use (PEOU)</td></tr><tr><td>PEOU1</td><td>I believe the measure is cumbersome to use (reversed).</td></tr><tr><td>PEOU2</td><td>Using the measure requires a lot of mental effort (reversed).</td></tr><tr><td>PEOU3</td><td>Overall, I believe that the measure is easy to use.</td></tr><tr><td>PEOU4</td><td>Learning to operate the measure is easy for me.</td></tr><tr><td>PEOU5</td><td>The measure is easy to understand.</td></tr></table>

In the next phase items were placed onto a web-based survey (see Table 2 for a list of the final items included in the analysis). Respondents were asked to identify software measures that they were familiar with, and then from the list they created they were asked to select the one measure that they were the most familiar with. For the measure that they selected as the most familiar, they were then asked to describe how the measure is used so that a check could be performed to be sure the respondent was knowledgeable enough about measures to include their data in the analysis. Finally, each respondent was asked to assess the measure that they selected according to how much they agreed with statements about the measure on a 5-point Likert-type scale ranging from ‘‘strongly disagree’’ to ‘‘strongly agree’’. They were also asked questions about whether they use the measure in their current job. The survey was pretested with several individuals who had experience with software development and measures. Minor changes were made to the survey items as a result of their feedback.

The final data collection involved using a web-based survey. Our procedures were consistent with the guidelines recommended by Punter et al. [87] and Singer and Vinson [93] for online software engineering surveys. We distributed the web-based survey to potential subjects via Web-based surveys are less costly, more convenient, and provide more control than postal surveys [30]. Moreover, web-based surveys have been shown to be similar to postal surveys in terms of the quality of data gathered [9,26], the number of items answered [9,26], and are useful for reducing social desirability bias [105].

Bryant et al. [22] discuss the validity of web-based experiments. They identify internal validity threats such as increased dropout rates and multiple submissions from the same participant. Consistent with the recommendations of Bryant et al. [22], we included controls to account for some of these potential threats. We encouraged participation in the study by describing the intent of the survey to the participants [70] and by entering them into a drawing for a prize after they completed the survey. Offering financial incentives to participants is a common and effective way to decrease dropout rates in online research and has been shown not to affect participant answers [42,81] or sample characteristics [81]. To control for the internal validity threat of multiple submissions from the same participant, participants were asked to provide their e-mail addresses; we then removed responses with duplicate e-mail addresses from the sample. To reduce item non-response, participants had to answer all questions in one section of the survey before proceeding to the next section.

Data collection involved three groups of subjects who were either current users of, or potential adopters of, software measures. The first group was members of the comp.software.measurement usenet group. An e-mail was posted to the group asking them for assistance in completing a survey and providing a link to a web page containing the survey. From this source we received 13 valid responses. The second source was individuals who are members of the information systems special interest group of the project management institute (PMI-ISSIG). The members of this group were sent an e-mail asking them to participate in the web-based survey. 83 individuals from PMI-ISSIG responded to the survey. In order to obtain additional data for our analysis an e-mail was also sent to a second group of individuals, members of a software measures listserv at a large software development firm. The e-mail directed them to the online survey. 88 individuals from this firm responded to the survey, giving us 184 valid responses to the final survey. Although members of the software measurement Usenet group, the PMI-ISSIG group, and employees of the large software firm were asked to participate in the survey, no one was required to participate. A sample size of 200 is generally recommended for structural equation modeling analysis [53], but our sample size was determined to be sufficient based on similar studies (e.g. [86,88]).

Although some researchers have approached the study of measure adoption from an organizational perspective (e.g. [47]), we chose to focus on individual rather than organizational adoption of software measures for a couple of reasons. First, models of innovation diffusion have noted the importance of individual acceptance of new technologies (e.g. [29]). If an individual is unwilling to adopt a measure then it will be more difficult for organizations to successfully establish a measurement program. Second, other researchers (e.g. [100]) have suggested that the success of a measurement program is dependent on the actions of individual developers and their willingness to provide data from software measures to management and to use the data and its analysis themselves. Therefore, we believe that understanding why individual users’ choose to adopt or not adopt software measures is an important first step in establishing successful organizational measurement initiatives.

## 4. Results

Of the 184 respondents, 66% were male and 34% were female. The mean job experience in the software industry was 18.75 years and the mean respondent age was 43.99 years. In terms of education, 7.6% have a high school diploma, 41.3% have an undergraduate degree, 41.3% have a master’s degree, and 9.2% have a Ph.D. The respondents worked in a variety of industries.

Response bias occurs if there are differences in non-respondents compared to respondents. Ideally we would have contacted some of the members of each of the three groups who did not respond to the survey in order to assess whether response bias was a problem. Unfortunately we were not able to obtain access to those who did not respond. However, non-respondents have been shown to resemble late respondents in previous research [8], so each respondent was categorized by date and time of response in order to distinguish between the early and late respondents. The first 25% of the replies from each user group were considered to be early responders while the last 25% were classified as late responders. Other researchers have used similar methods to check for response bias (e.g. [103]). We used a one-way ANOVA to compare the early and late respondents for each of our two large groups of respondents (n = 83 and n = 88). We found that there were no significant differences in the early and late respondents in terms of their age, years of experience using software measures, job title, and number of years working in the software industry.

Principal components analysis with varimax rotation.

<table><tr><td rowspan="2"></td><td colspan="5">Component</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>LI1</td><td>.035</td><td>.870</td><td>.131</td><td>.140</td><td>.148</td></tr><tr><td>LI2</td><td>.039</td><td>.875</td><td>.116</td><td>.125</td><td>.172</td></tr><tr><td>LI3</td><td>-.006</td><td>.840</td><td>.074</td><td>.215</td><td>.184</td></tr><tr><td>PEOU1</td><td>.728</td><td>.073</td><td>.182</td><td>.016</td><td>-.096</td></tr><tr><td>PEOU2</td><td>.717</td><td>.031</td><td>-.135</td><td>.013</td><td>-.041</td></tr><tr><td>PEOU3</td><td>.860</td><td>.078</td><td>.098</td><td>.126</td><td>.114</td></tr><tr><td>PEOU4</td><td>.761</td><td>-.094</td><td>.065</td><td>.077</td><td>.236</td></tr><tr><td>PEOU5</td><td>.735</td><td>-.012</td><td>.186</td><td>-.025</td><td>.103</td></tr><tr><td>PS1</td><td>.040</td><td>.125</td><td>.113</td><td>.869</td><td>.127</td></tr><tr><td>PS2</td><td>.042</td><td>.160</td><td>.076</td><td>.852</td><td>.076</td></tr><tr><td>PS3</td><td>.094</td><td>.205</td><td>.253</td><td>.691</td><td>.240</td></tr><tr><td>VA1</td><td>.038</td><td>.029</td><td>.802</td><td>.017</td><td>.238</td></tr><tr><td>VA2</td><td>-.056</td><td>.105</td><td>.662</td><td>.126</td><td>.140</td></tr><tr><td>VA3</td><td>.178</td><td>.144</td><td>.742</td><td>.238</td><td>.130</td></tr><tr><td>VA4</td><td>.215</td><td>.067</td><td>.707</td><td>.067</td><td>.032</td></tr><tr><td>LC1</td><td>.030</td><td>.236</td><td>.217</td><td>.140</td><td>.830</td></tr><tr><td>LC2</td><td>.239</td><td>.147</td><td>.188</td><td>.090</td><td>.625</td></tr><tr><td>LC3</td><td>-.007</td><td>.160</td><td>.131</td><td>.193</td><td>.843</td></tr></table>

We performed a principal components factor analysis with varimax rotation to assess the validity of the measurement scales. The Kaiser-Meyer-Olkin (KMO) Measure of Sampling Adequacy was 0.80, which is higher than the minimum recommended value of 0.50. The KMO statistic indicates whether or not the variables should be able to be grouped into a smaller set of underlying factors. The KMO statistic of 0.80 suggests that it was suitable to use principal components analysis on the data. The rotated components matrix is shown in Table 3. Five factors were extracted, explaining 68.5% of the variance. All items loaded highly on their intended factor and had low cross-loadings with other factors, exhibiting good convergent and discriminant validity.

A variance-extracted test can also be used to establish both discriminant and convergent validity [41,79]. This test compares the variance-extracted estimates for two constructs of interest with the square of the correlation of the two constructs. Validity is demonstrated if both variance-extracted estimates are greater than this squared correlation [54]. Table 4 shows the results of this test for the five constructs. The diagonal elements in Table 4 are the variance-extracted estimates for each dimension, and the offdiagonal elements are the squared correlations between constructs. The diagonal elements are all larger than their correspond ing correlation coefficients, which indicate that they exhibit both convergent and discriminant validity [44]. This indicates that each construct shared more variance with its items than it shared with other constructs, thereby demonstrating discriminant validity.

We used a two-step approach using structural equation modeling to test our model. First we tested the measurement model, followed by a test of the structural model. There has been some debate in the academic community regarding whether a measurement model should be analyzed separately, before the analysis of a structural model. Recommendations from researchers in the area have ranged from a single process combining the analysis of the measurement and structural model [56,55] to a two-step process that separates the measurement model and the structural model [6,60], to a four-step process consisting of a factor model, a confirmatory factor model, the proposed structural model, and a more constrained model [63,77,78].

For this research we chose to separate the measurement model from the structural model. This approach is consistent with prior research [23,25,43,89] and was appropriate here because it allowed us to refine our measures before testing the structural model. Amos 21.0.0 was used to perform a confirmatory factor analysis (CFA) to assess the measurement model [7]. CFA can be used to test that indicator variables load highly on predetermined factors, but do not load highly on unrelated factors [54]. The measurement model (see Fig. 2) consisted of five latent variables: Perceived Language Independence, Perceived Prescriptiveness, Perceived Validity, Perceived, Life Cycle Applicability, and Perceived Ease of Use. The covariance matrix of the items comprising these five constructs were used as the input for the analysis and a reference variable for each latent construct was set to one in order to set the scale for the analysis. Each latent variable had between three and five indicator variables (see Table 2). Each indicator variable represented a questionnaire item that was expected to load on only one factor.

Table 4 Variance extracted test.

<table><tr><td></td><td>Perceived Language Independence</td><td>Perceived Prescriptiveness</td><td>Perceived Validity</td><td>Perceived Life Cycle Applicability</td><td>Perceived Ease of Use</td></tr><tr><td>Perc. Language Indep.</td><td> $\mathbf{0.718^a}$ </td><td></td><td></td><td></td><td></td></tr><tr><td>Perc. Prescriptiveness</td><td>0.231</td><td>0.528</td><td></td><td></td><td></td></tr><tr><td>Perc. Validity</td><td>0.118</td><td>0.260</td><td>0.458</td><td></td><td></td></tr><tr><td>Perc. Life Cycle Applic.</td><td>0.237</td><td>0.236</td><td>0.252</td><td>0.592</td><td></td></tr><tr><td>Perc. Ease of Use</td><td>0.018</td><td>0.055</td><td>0.108</td><td>0.045</td><td>0.507</td></tr></table>

<sup>a</sup> Diagonal elements are the Average Variance Extracted. These values should exceed the squared inter-construct correlations (the off diagonal values) for adequate discriminant validity.

![](/api/attachments/Y4XQBW2T/fulltext/images/61e22b8342016c814c9a3e1774b9ccb1a8a20b4fb9014cb88acf549adc46290f.jpg)  
Fig. 2. Measurement model.

The measurement model was estimated and Fig. 2 contains the fit statistics and scale reliabilities that were obtained. The GFI, CFI, NFI and NNFI are all very close to or higher than the recommended minimum values of .90 [17,18,49]. The AGFI is also well above the recommended minimum value of .80, suggesting good model fit. The RMR is .058, which was judged to be an acceptable value [11]. The root mean square error of approximation (RMSEA) is well under the threshold of .80, indicating good model fit after adjusting for sample size [21]. Overall the good fit indices support the construct validity of the individual constructs in the model.

The standardized factor loadings were all significant, with values ranging from .51 to .92. The t-values, representing the significance of the loadings of the indicators on the constructs, indicated that all paths were significant at the p < .001 level. This provides evidence to support the convergent validity and unidimensionality of the indicators [6]. Finally the composite reliability index (see [41]) of each scale was also acceptable with all values in excess of .76, which is above the minimum threshold of .70 for survey research [80]. Overall, the fit measures and item loadings we obtained were found to meet accepted thresholds, thus supporting the reliability and validity of the refined instrument [49,59].

Structural equation modeling using Amos 21.0.0 was selected to evaluate the relationships between indicators and latent constructs, as well as the structural relationships between perceived usefulness, perceived ease of use, and use. Fig. 3 shows the standardized loadings of the items on each latent construct, as well as the path loadings between constructs. The loadings of all four of the desirable properties constructs onto the perceived usefulness construct was significant at p < .001. Both perceived usefulness and perceived ease of use had direct, positive effects on measure use, thereby supporting H2 and H3. Consistent with expectations, perceived ease of use also had a direct, positive effect on perceived usefulness, providing support for H1. All of the path coefficients associated with the relationships between the latent constructs were significant at $p < . 0 0 1$ , with the exception of the path from perceived ease of use to use which was significant at $p < . 0 1$ . The percent of variance explained by the model as it relates to perceived usefulness and use were 13% and 26% respectively.

![](/api/attachments/Y4XQBW2T/fulltext/images/1c097b68865b36f14c12137442bcc085818dd2bd50e3ed3fa179c4a30e4eb672.jpg)  
Fig. 3. SEM analysis results.

The model fit for the structural model was very good with GFI, CFI, NFI, and NNFI values of .91, .97, .89, and .96 respectively. The AGFI was .88 and the normed $\chi ^ { 2 }$ was 1.28. The RMSEA was .039 (with a lower bound of .019 and upper bound of .055) and the standardized RMR was .055.

## 5. Implications for research

The primary purpose of this paper is to provide a direction for future research by developing a theory-based model for the adoption of software measures. Software measures must be perceived as beneficial; otherwise they will be used unenthusiastically, if at all. Managers, developers, and software metrics coordinators may not fully understand the benefits of measures, which may be one cause of low measure adoption and use. Our results suggest that both the perceived ease of use and perceived usefulness of a software measure can increase the likelihood of software measure use. The perceived usefulness of a software measure can be measured by an assessment of the measure’s applicability throughout the life cycle, dependence on a particular programming language, ability to prescribe solutions or actions, and the validity of the software measure. Finally, the perceived ease of use of the software measure can also influence the perceptions of the measure’s usefulness.

Traditionally, the perceived usefulness construct has been conceptualized as unidimensional. However, several researchers have attempted to investigate more deeply what makes a technology useful [10,16,95]. Our finding that perceived usefulness consists of sub-dimensions in the software measures context supports suggestions that a deeper understanding of perceived usefulness may be available. Thus, we contribute to the understanding of this widely applied construct and the applicability of the theory in general. It seems that further investigation into the perceived usefulness construct is warranted. Future researchers that include perceived usefulness in their models may benefit from considering that the construct may be multi-dimensional.

Although the primary focus of this research is the identification of the sub-dimensions of perceived usefulness, we also use a dependent variable (software measure use) in order to provide preliminary validation of the proposed model of software measure adoption. There may be other success variables that would be useful to study in future research (e.g., impact on organizational performance), but for the purposes of this study we were focused on the second order factor structure of the perceived usefulness construct rather than the development of other measures of software measure success.

Similarly, the identification of additional sub-dimensions of perceived ease of use may also be appropriate for future research efforts. It seems reasonable that desirable properties such as intuitiveness, automatability, and calculation ease might be subdimensions of perceived ease of use, which was measured in its classic form for this study, but could be investigated as a multidimensional construct in future studies. We also only selected four desirable properties to tap into the perceived usefulness construct, but there may be other properties which may contribute to perceptions of usefulness. For example, robustness (the degree to which the measure can produce useful information even if some assumptions are violated or the input data is incomplete) and sensitivity (the degree to which the measure is sensitive to changes in the attribute measured) could be additional sub-dimensions of perceived usefulness that future studies could investigate.

## 6. Implications for practice

By understanding why people adopt software measures, measurement programs can be designed to support measure adoption. Our findings suggest that managers should promote both the usefulness and the ease of use, or user friendliness, of software measures to encourage adoption and use of a measure. In order to convince managers and developers to use measures, software metrics coordinators should emphasize how the measures can be used throughout the SDLC, how the measure can be used to improve the product or process, and should promote measures that are valid, can be used regardless of programming language, and are easy to use. Adequate training on the benefits of using software measures may be a vital part of a successful software measurement initiative. Comprehensive education and training programs can help to raise awareness of the benefits of software measures. Software metrics coordinators are particularly well positioned within the organization to fill this role as they can help managers and developers better understand the benefits of software measures and serve as liaisons between managers and developers during software measurement initiatives.

Research on the adoption of software measures has practical implications for the software engineering profession. An instrument for measuring desirable software properties can be used by software engineers to evaluate existing software measures. For example, a potential adopter could ‘‘score’’ the perceived ease of use and usefulness of McCabe’s [74] cyclomatic complexity versus Halstead’s (1977) length, as measured by the desirable properties of the measures. Combined scores across the desirable properties would provide a basis for a high level comparison of the adoptability of software measures while scores for individual properties (prescriptiveness, validity, etc.) would provide a basis for a more detailed comparison. The potential adopter could select a set of measures, based on the results of using such an instrument, that have offsetting strengths and weaknesses to develop a software measurement program.

Future efforts should not only be directed toward education and training, but also toward developing software measures that are perceived as useful and easy to use. The importance of the potential adopters’ perceptions argues for involving practicing professionals in future studies on software measure adoptability. With a few exceptions, the software measures research community has not done enough to involve software engineers in the development of new measures. Future research in this area should determine what the perceived shortcomings of existing software measures are, and thus allow researchers to focus on the issues pertinent to IS managers and software engineers.

## 7. Limitations

For a more thorough investigation of TAM we could have used behavioral intentions in addition to a self-reported use behavior. The value added by intentions is that it would allow managers to predict the potential acceptance of software measure. However, we believed that our research should ultimately be concerned with explaining and predicting potential adopter’s actual behavior rather than their intentions. Also, we only used perceptual selfreported measures of use instead of actual use. So these results must be interpreted with that limitation in mind.

We designed our methodology to make sure that our model was tested and validated for as many software measures as possible.

We did not want to limit its usefulness to one particular measure, such as function points or cyclomatic complexity; i.e., we wanted the model to be generalizable. Therefore, we asked the respondent to identify the measure they were most familiar with, then answer the survey questions as they related to that measure. We wanted to ensure that the respondent fully understood the measure and was therefore able to sufficiently assess its usefulness/ease of use. Future research should consider asking the respondent how long they have been using the particular measure that they choose so it can be used as a control variable. Or, perhaps, the survey could be administered to multiple user groups, with each group focusing on one specific software measure (e.g. function points, cyclomatic complexity, etc.), rather than letting the users identify the measure themselves.

The desirable properties used in this study have not been operationalized in prior research and thus could be construed as somewhat exploratory. Although the fit of the model that we tested was very good, the R-square values were a little low. It is likely that there are other measures that could be investigated in future research, such as other desirable properties or other variables that could be included as control variables, which could improve the predictive power of the model.

A final limitation revolves around the response rate. Although the exact response rate is unknown, as individuals receiving the invitation letter containing the hyperlink to the survey could have passed it along to other individuals, numerous steps were taken to maximize the response rate. First, an invitation letter was included with the link to the survey, which included the intent of the study, the estimated time to complete the survey, and a statement indicating that the respondent was part of a small group chosen to participate in the study [70,85]. Second, to further encourage participation, participants were encouraged to provide their e-mail address, which entered them into a prize drawing [20], and third, the invitation letter stated that anonymity would be assured [61], thereby reducing social desirability bias [105].

## 8. Conclusions

A goal of software measurement is to help improve the quality of software and of the systems development process. Whether software measures can achieve this goal is currently unknown, since they are, as yet, not widely used in industry. If the twentyfirst century is truly to improve software quality, then the software measurement research community must begin to take the problems associated with adoptability seriously. Enlarging the focus of future research to include the adoptability of software measures changes the investigation from primarily an engineering endeavor to one that incorporates a social science perspective. Thus it is fitting that a theoretical base developed in sociology, anthropology, communications, and marketing might prove useful for advancing the study of the adoption of software measures. Our proposed model of software measures adoption builds a bridge between engineering and social science research. We think it can point the way for software measurement researchers to carry their work to fruition.

## References

[11 D.A. Adams. R.R. Nelson, P.A. Todd, Perceived usefulness, ease of use and usage of information technology: a replication, MIS Quarterly 16, 1992, pp. 227–247.

[2] R. Agarwal, J. Prasad, The role of innovation characteristics and perceived voluntariness in the acceptance of information technologies Decision Sciences 38, 1997, pp. 557–582.

[3] I. Ajzen, M. Fishbein, Understanding Attitudes and Predicting Social Behavior, Prentice-Hall, New Jersey, 1980.

[4] A. Albrecht, Measuring application development productivity, in: I.B.M. Press (Ed.), IBM Application Development Symp., 197983–92.

[5] A. Albrecht, J. Gaffney, Software function, source lines of code, and development effort prediction: a software science validation, IEEE Transactions on Software Engineering 1983, pp. 639–648.

[6] J.C. Anderson, D.W. Gerbing, Structural equation modeling in practice: a review and recommended two-step approach, Psychological Bulletin 103, 1988, pp. 411–423.

[7] J.L. Arbuckle, Amos for Windows: Analysis of Moment Structures, Smallwaters, Chicago, IL, 1999.

[8] J.S. Armstrong, T.S. Overton, Estimating nonresponse bias in mail surveys, Journal of Marketing Research 14, 1977, pp. 396–403.

[9] D. Bachmann, J. Elfrink, G. Vanazza, Tracking the progress of e-mail vs. snail-mail, Marketing Research 8, 1996, pp. 30–35.

[10] R. Bagozzi, The legacy of the technology acceptance model and a proposal for a paradigm shift, Journal of the Association for Information Systems 8, 2007, pp. 244–254.

[11] R.P. Bagozzi, Y. Yi, On the evaluation of structural equation models, Journal of the Academy of Marketing Science 16, 1988, pp. 74–94.

[12] A. Baker, J. Bieman, N. Fenton, D. Gustafson, A. Melton, R. Whitty, A philosophy for software measurement, Journal of Systems and Software 12, 1990, pp. 277– 281.

[13] V.R. Basili, H.D. Rombach, The TAME project: towards improvement-oriented software environments, IEEE Transactions on Software Engineering 14, 1988, p 758.

[14] V.R. Basili, F.E. McGarry, R. Pajerski, M.V. Zelkowitz, Lessons learned from 25 years of process improvement: the rise and fall of the NASA software engineering laboratory, in: Proceedings of the 24th International Conference on Software Engineering, 2002. ICSE 2002, 2002, pp. 69–79.

[15] V.R. Basili, M. Lindvall, M. Regardie, C. Seaman, J. Heidrich, J. Munch, D. Rombach A. Trendowicz, Linking software development and business strategy through measurement, Computer 43, 2010, pp. 57–65.

[16] I. Benbasat, H. Barki, T.A.M. Quo Vadis, Journal of the Association for Information Systems 8 2007 pp. 212-218

[18] P.M. Bentler, D.G. Bonett, Significance tests and goodness of fit in the analysis of covariance structures, Psychological Bulletin 88, 1980, pp. 588–606.

[19] F. Bergeron, L. Raymond, S. Rivard, M.F. Gara, Determinants of EIS use: testing a behavioral model, Decision Support Systems 14, 1995

[20] J.P. Birnholtz, D.B. Horn, T.A. Finholt, S.J. Bae, The effects of cash, electronic and paper gift certificates as respondent incentives for a web-based survey of technologically sophisticated respondents, Social Science Computer Review 22, 2004, pp. 355–362.

[21] M.W. Browne, R. Cudeck, Alternative ways of assessing model fit, in: K.A.B.J.S. Long (Ed.), Testing Structural Equation Models, Sage, Newbury Park, CA, 1993, pp. 136–162.

[22] S.M. Bryant, J.E. Hunton, D.N. Stone, Internet-based experiments: prospects and possibilities for behavioral accounting research, Behavioral Research in Accounting 16, 2004, pp. 107–129.

[23] C.L. Carr, A psychometric evaluation of the expectations, perceptions, and difference-scores generated by the IS-adapted SERVQUAL instrument, Decision Sciences 33, 2002, pp. 281–296.

[24] P. Chau, An empirical investigation on factors affecting the acceptance of CASE by systems developers, Information & Management 30, 1996, pp. 269–280.

[25] V.K. Chong, K.M. Chong, Budget goal commitment and informational effects of budget participation on performance: a structural equation modeling approach Behavioral Research in Accounting 14, 2002, pp. 65–86.

[26] G. Coderre, A. Mathieu, N. St-Laurent, Comparison of the quality of quantitative data obtained through telephone, postal and email surveys, International Journal of Market Research 46, 2005, pp. 347-357

[27] N. Condori-Fernandez, O. Pastor, An empirical study on the likelihood of adoption in practice of a size measurement procedure for requirements specification Sixth International Conference on Quality Software (QSIC 2006), Beijing, China, 2006, pp. 133–140.

[28] N. Condori-Ferna´ndez, O. Pastor, Re-assessing the intention to use a measurement procedure based on COSMIC-FFP, International Conference on Software Process and Product Measurement (MENSURA), 2006.

[29] R.B. Cooper, R.W. Zmud, Information technology implementation research: a technological diffusion approach, Management Science 36, 1990, pp. 123–139

[30] M. Couper, Web surveys a review of issues and approaches, Public Opinion Quarterly 64, 2000, pp. 464–494.

[31] M. Daskalantonakis, A practical view of software measurement and implementation experiences within Motorola, IEEE Transactions on Software Engineering 18, 1992, pp. 998–1010.

[32] F.D. Davis, A Technology Acceptance Model for Empirically Testing New End User Information Systems: Theory and Results, Sloan School of Management MIT, Cambridge, MA, 1986.

[33] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13, 1989, pp. 318–340.

[34] W.J. Doll, A. Hendrickson, X. Deng, Using Davis’s perceived usefulness and ease of use instruments for decision making and multi-group invariance analysis, Decision Sciences 29 1998 pp 839–869

[35] K. Ewusi-Mensah, Critical issues in abandoned information systems develop ment projects, Communications of the ACM 40, 1997, pp. 74–80.

[36] S. Fenick, Implementing management metrics: an army program, IEEE Software 1990. pp.65-72

[37] N. Fenton, Software measurement: a necessary scientific basis, IEEE Transactions on Software Engineering 20, 1994, pp. 199–206.

[38] N.E. Fenton, M. Neil, Software metrics: successes, failures and new directions, Journal of Systems and Software 47, 1999, pp. 149–157.

[39] N.E. Fenton, M. Neil, Software metrics: roadmap, International Conference on Software Engineering ACM, Limerick, Ireland, 2000, pp. 357–370.

[40] N.E. Fenton, S.L. Pfleeger, Software Metrics: A Rigorous and Practical Approach, 2nd edition, International Thomson Computer Press, London, 1996.

[41] C. Fornell, D.F. Larcker, Evaluating structural equation models with unobservable variables and measurement error, Journal of Marketing Research 18, 1981, pp. 39–50.

[42] A. Frick, M.T. Bachtiger, U.D. Reips, Financial incentives, personal information, and dropout in online studies, in: U.D. Reips, M. Bosnjak (Eds.), Dimensions of Internet Science, Pabst Science, Lengerich, Germany, 2001, pp. 209–219.

[43] M.T. Frohlich, E-integration in the supply chain: barriers and performance, Decision Sciences 33, 2002, pp. 537–556.

[44] D. Gefen, D. Straub, M. Boudreau, Structural equation modeling and regression: guidelines for research practice, Communications of the Association of Information Systems 4, 2000, pp. 1–79.

[45] A. Gopal, R.P. Bostrom, W.W. Chin, Applying adaptive structuration theory to investigate the process of group support systems use, Journal of Management Information Systems 9, 1992–1993, pp. 46–69.

[46] A. Gopal, M.S. Krishnan, T. Mukhopadhyay, D.R. Goldenson, Measurement programs in software development: determinants of success, IEEE Transactions on Software Engineering 28, 2002, pp. 863–875.

[47] A. Gopal, T. Mukhopadhyay, M.S. Krishnan, The impact of institutional forces on software metrics programs, IEEE Transactions on Software Engineering 31, 2005, pp. 679–694.

[48] R.B. Grady, Practical Software Metrics for Project Management and Process Improvement, Prentice Hall, Upper Saddle River, NJ, 1992.

[49] J.F. Hair Jr., R.E. Anderson, R.L. Tatham, W.C. Black, Multivariate Data Analysis, Third ed. Macmillan New York 1992

[50] T. Hall, N. Fenton, Implementing effective software metrics programs, IEEE Software 1997 pn. 55-65

[51] M.H. Halstead, Elements of Software Science, Elsevier, New York, 1977.

[52] B.C. Hardgrave, R.A. Johnson, Toward an information systems development acceptance model: the case of object-oriented systems development, IEEE Transactions on Engineering Management 50, 2003, pp. 322–336.

[53] M. Harris, SchaubroeckF J., Confirmatory modeling in organizational behavior human resource management: issues and applications, Journal of Management 16, 1990.

[54] L. Hatcher, A Step-by-Step Approach to Using the SAS System for Factor Analysis and Structural Equation Modeling, SAS Institute Inc., Cary, NC, 1994.

[55] L.A. Hayduk, Structural Equation Modeling with LISREL: Essentials and Advances, John Hopkins University Press, Baltimore, 1987.

[56] L. Hayduk, D.N. Glaser, Jiving the four-step, waltzing around factor analysis, and other serious fun, Structural Equation Modeling 7, 2000, pp. 1–35.

[57] B. Henderson-Sellers, Object-Oriented Metrics Measures of Complexity, Prentice-Hall, Upper Saddle, NJ, 1996.

[58] A.R. Hendrickson, P.D. Massey, T.P. Cronan, On the test–retest reliability of perceived usefulness and perceived ease of use, MIS Quarterly 17, 1993, pp. 227–230.

[59] J.W. Henry, R.W. Stone, A structural equation modeling of end-user satisfaction with a computer-based medical information system, Information Resources Management Journal 7, 1994, pp. 21–33.

[60] J.R. Herting, H.L. Costner, Another perspective on the proper number of factors and the appropriate number of steps, Structural Equation Modeling 7, 2001, pp. 92–110.

[61] C. Hewson, P. Yule, D. Laurent, C. Vogel, Internet Research Methods, Sage, London 2003.

[62] J. Iversen, L. Mathiassen, Lessons from implementing a software metrics program, Hawaii International Conference on System Sciences (HICSS-33), 2000.

[63] L.R. James, S.A. Mulaik, J.M. Brett, Causal Analysis: Assumptions, Models, and Data, Sage, Beverly Hills, 1982.

[64] D.R. Jeffrey, I. Vessey, Models, metrics, and management of IS development, Information & Management 3, 1980, pp. 89–93.

[65] D. Kafura, G.R. Reddy, The use of software complexity metrics in software maintenance, IEEE Transactions on Software Engineering 13. 1987, pp. 335–343

[66] E. Karahanna, D. Straub, N.L. Chervany, Information technology adoption across time: a cross-sectional comparison of pre-adoption and post-adoption beliefs MIS Ouarterly 23 1999 pp. 183–213.

[67] T.M. Khoshgoftaar, E.B. Allen, D.L. Lanning, An information theory-based approach to quantifying the contribution of a software metric, Journal of Systems and Software 36, 1997, pp. 103–113.

[68] B. Kitchenham, S.L. Pfleeger, N.E. Fenton, Toward a framework for software measurement validation, IEEE Transactions on Software Engineering 21, 1995, pp. 929–944.

[69] K.B. Lakshmanan, S. Jayaprakash, P.K. Sinha, Properties of control-flow complexity measures, IEEE Transactions on Software Engineering 17, 1991, pp. 1289–1295.

[70] I. Lazar, I. Preece, Designing and implementing web-based surveys, Journal of Computer Information Systems 39, 1999, pp. 63–67.

[71] G.C. Low. D.R. Jeffery. Function points in the estimation and evaluation of the software process, IEEE Transactions on Software Engineering 16, 1990, pp. 64–71.

[72] M.A. Mahmood, K.J. Pettingell, A.I. Shaskevich, Measuring productivity of software projects: a data envelopment analysis approach, Decision Sciences 27, 1996, pp. 57–80.

[73] L. Mathiassen, Management of risks in software development, Data Processing '91 – Congress, Ivvaskyla, Finland, 1991.

[74] T.J. McCabe, A complexity measure, IEEE Transactions on Software Engineering SE-2. 1976, pp. 308–320.

[75] D.L. Moody, Dealing with Complexity: A Practical Method for Representing Large Entity Relationship Models, University of Melbourne, Department of Information Systems, 2001.

[76] G.C. Moore, I. Benbasat, Development of an instrument to measure the perceptions of adopting an information technology innovation, Information Systems Research 2, 1991, pp. 192–222.

[77] S.A. Mulaik, R.E. Millsap, Doing the four-step right, Structural Equation Modeling 7, 2000, pp. 36–73.

[78] S.A. Muliak, Re: Four-step Model, SEMNET Discussion List, 1998.

[79] R.G. Netemeyer, M.W. Johnston, S. Burton, Analysis of role conflict and role ambiguity in a structural equations framework, Journal of Applied Psychology 75, 1990, pp. 148–157.

[80] J.C. Nunnally, I.H. Bernstein, Psychometric Theory, Third ed., McGraw-Hill, New York, 1994.

[81] K. O’Neil, S. Penrod, B. Bornstein, Web-based research methodological variables effects on dropout and sample characteristics, Behavior Research Methods Instruments and Computers 35, 2003, pp. 217–226.

[82] J.S. Osmundson, J.B. Michael, M.J. Machniak, M.A. Grossman, Quality management metrics for software development, Information and Management 40, 2003, pp. 799–812.

[83] S. Petter, D. Straub, A. Rai, Specifying formative constructs in information systems research, MIS Quarterly 31, 2007, pp. 623–656.

[84] S.L. Pfleeger, Lessons learned in building a corporate metrics program, IEEE Software 1993 pp. 67–74

[85] S.R. Porter, M.E. Whitcomb, The impact of lottery incentives on survey response rates, Research in Higher Education 44, 2003, pp. 389–407.

[86] D. Preston, D. Chen, D. Leidner, Examining the antecedents and consequences of CIO strategic decision-making authority: an empirical study, Decision Sciences 39, 2008, pp. 605–642.

[87] T. Punter, M. Ciolkowski, B. Freimut, I. John, Conducting on-line surveys in software engineering, in: Proceedings of the International Symposium on Empirical Software Engineering (ISESE ’03), IEEE Computer Society, Washington, DC, 2003.

[88] A. Rahman, N. Brookes, D. Bennett, The precursors and impacts of BSR on AMT acquisition and implementation, IEEE Transactions on Engineering Management 56, 2009, pp. 285–297.

[89] A. Rai, S.S. Long, R.B. Welker, Assessing the validity of IS success models: an empirical test and theoretical analysis, Information Systems Research 13, 2002, pp. 50–69.

[90] G. Ray, The lines of code alternative, Computerworld 27, 1993, pp. 91–92.

[91] M.A. Rothenberger, Y.-C. Kao, L.N.V. Wassenhove, Total quality in software development: an empirical study of quality drivers and benefits in Indian software projects, Information & Management 47, 2010, pp. 372–379.

[92] H. Rubin, Measuring rigor and putting measurement into action, American Programmer 4, 1991, pp. 9–23

[93] J. Singer, N.G. Vinson, Ethical issues in empirical studies of software engineering, IEEE Transactions on Software Engineering 28, 2002, pp. 1171–1180.

[94] G. Stark, R.C. Durst, C.W. Vowell, Using metrics in management decision making, IEEE Computer September, 1994, pp. 42–49.

[95] D. Straub, A. Burton-Jones, Veni, vedi, vici: breaking the TAM logjam, Journal of the Association for Information Systems 8, 2007, pp. 224–229.

[96] D.W. Straub, M. Limayem, E. Karahanna-Evaristo, Measuring system usage: implications for IS theory testing, Management Science 41. 1995 pp. 1328- 1341

[97] G.H. Subramanian, A replication of perceived usefulness and perceived ease of use measurement, Decision Sciences 25, 1994, pp. 863–874.

[98] S.W. Sussman, W.S. Siegal, Informational influence in organizations: an integrated approach to knowledge adoption, Information Systems Research 14, 2003, pp. 47–65.

[99] M. Umarji, C. Seaman, Predicting acceptance of software process improvement, in: Proceedings of the 2005 Workshop on Human and Social Factors of Software Engineering, ACM, St. Louis, Missouri, 2005, pp. 1–6.

[100] M. Umarji, C. Seaman, H. Emurian, Acceptance issues in metrics program implementation, 11th IEEE International Software Metrics Symposium (METRICS'05). IEEE Computer Society. 2005

[101] V. Venkatesh, F. Davis, A theoretical extension of the technology acceptance model: four longitudinal field studies, Management Science 46, 2000, pp. 186– 204.

[102] L.J.J. Waguespack, S. Badlani, Software complexity assessment: an introduction and annotated bibliography, ACM SIGSOFT Software Engineering Notes 12, 1987, pp. 52–71.

[103] L. Wallace. H. Lin, M.A. Cefaratti, Information security and sarbanes-oxley compliance: an exploratory study, Journal of Information Systems 25, 2011, pp. 185–211.

[104] E.J. Weyuker, Evaluating software complexity measures, IEEE Transactions on Software Engineering 14, 1988, pp. 1357–1365.

[105] B. Whitley, Principles of Research in Behavioral Science, second ed., McGraw-Hill, New York, 2002

[106] H.-d. Yang, Y. Yoo, It’s all about attitude: revisiting the technology acceptance model, Decision Support Systems 38, 2004, pp. 19–31.

[107] H. Zuse, Software Complexity: Measures and Methods, Walter de Gruyter & Co., New York 1990.

Linda Wallace is an Associate Professor and the John & Angela Emery Junior Faculty Fellow in the Department of Accounting and Information Systems at Virginia Tech, where she is also the Director of the Master’s program in ACIS. She obtained her PhD in Computer Information Systems from Georgia State University in 1999. Her research interests include online communities, software project risk, information security, and agile software development. Her research has been accepted for publication in Decision Sciences, Communications of the ACM, Information & Management, IEEE Security & Privacy, Decision Support Systems, Journal of Systems and Software, Journal of Information Systems, and others. She is an AE for Information Systems Journal.

Steven D. Sheetz is an Associate Professor of Accounting and Information Systems at the Pamplin College of Business at Virginia Tech. He received his PhD in Information Systems from the University of Colorado. His research interests include the cognitive complexity of developing information systems, use of social media and web archiving relatedto crises, the understanding of group processes, and affective decision-making. He has published articles in Decision Support Systems, International Journal of Human-Computer Studies, Journal of Management Information Systems, Journal of Systems and Software, Decision Support Systems, Journal of Emerging Technologies in Accounting International Journal of Accounting Information Systems, and Object-Oriented Systems. He also holds a MBA from the University of Northern Colorado and a BS in Computer Science from Texas Tech University. He has substantial industry experience in database design and systems development.
