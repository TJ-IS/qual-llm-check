---
otero_id: 18556
otero_key: "79JRXR92"
title: "Impact of prototyping on user information satisfaction during the IS specification phase"
authors: "Juhani Iivari; Mikko Karjalainen"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(89)90053-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of Prototyping on User Information Satisfaction During the IS Specification Phase \*

Juhani Iivari and Mikko Karjalainen
Institute of Information Processing Science, University of Oulu,
90570 Linnanmaa, Oulu, Finland

A study was carried out on an IS development project during the requirements specification of a DB-oriented information system. User Information Satisfaction (UIS) was measured three times during the phase: after the abstract specification of the system, after the interaction prototype, and after the interaction prototype, and after the system prototype. All representations described the identical information system. Assuming that the users' understanding of the system increased during the requirements specification phase, the study is a longitudinal, ex ante assessment of UIS and involves an exploratory analysis of the impact of uncertainty upon the assessment of UIS. The interaction prototype consistently gave the highest mean scores on UIS and the system prototype the lowest. This is consistent with earlier findings that protyping may create unrealistic expectations. The reliability scores of the UIS scales were high and generally increased during the three rounds of the specification process. The variance due to individual differences was considerably greater in the case of the system prototype than in those of the abstract specification and interaction prototype. This maybe explained by the uncertainty effect, which increases the proportion of neutral values.

Keywords: Requirements analysis, Requirements specification, Prototyping, Information system evaluation, Information system assessment, User information satisfaction.

## 1. Introduction

The study involved a real IS development project. The purpose of the system was to assist reporters at the regional studios of a Finnish broadcasting company in Oulu. User Information Satisfaction (UIS) was measured three times during the requirements specification phase using the relevant part of the Bailey-Pearson UIS measure, after abstract specification, consisting of the conceptual schema and interaction description, after the interaction prototype describing the menu-based dialogue technique and related displays, and finally after the system prototype had been constructed with a sample of the real database. These three representations all described the equivalent real IS. Assuming that the users' under-

![](/api/attachments/79JRXR92/fulltext/images/c86f4e8298a8ffa2403234f354189c5e0aad843ac5526889a7a130d22eec1dde.jpg)

![](/api/attachments/79JRXR92/fulltext/images/7ffd382ad9cb98c7a97c3c9767a3e47eb5231ade60e5aae1fff86931a713e791.jpg)  
Juhani Iivari is an Associate Professor of Information Processing Science at the University of Oulu, where he received his M.S. and Ph.D. degrees. His research interests include the comparative analysis of IS design methodologies, the organizational aspects of IS design and implementation, the specification of information systems and IS assessment. He is a member of IFIP Working Group WG8.2.

Mikko Karjalainen received the M.S. degree from the University of Oulu, Finland in 1987. He is currently working as a senior systems analyst in CCC Software Professionals in Oulunsalo, Finland, where he started as a systems analyst in September '88. His earlier employers include Tietohaka, Oulu, where he worked as a programmer in 1984–1986, and the University of Oulu, where he worked as a research assistant in 1986–1987.

standing of the system increased during the three rounds, the study also involves an exploratory analysis of the impact of uncertainty upon the assessment of UIS.

The Bailey–Pearson measure was selected for its correspondence with the Iivari–Koskela construct for UIS ([22,25]). The prototypes were implemented using the Cullinet Inc. prototyping tool: the ADS/OnLine application generator.

We found that the interaction prototype consistently gave the highest mean scores on UIS and the system prototype the lowest. This is congruent with the earlier finding by Alavi that prototyping may create unrealistic expectations [1]. The reliability of the UIS scales was determined using Cronbach's alpha test. The scores turned out to be high in each round of measurement, even though the average scores generally increased during the specification process. Variance analysis of the results revealed that the scale variances due to individual differences were considerably greater in the case of the system prototype than in those of the preceding rounds, while the scale variances after the abstract specification were generally the smallest. This suggests that the first two UIS measurements did not reveal the true individual variation. This is explained by an uncertainty effect according to which increased uncertainty reduces extreme UIS values and favours neutral, close to zero ones. Because these are the results from one project and the size of the user population is small, the study is exploratory.

## 2. Prototypes and User Information Satisfaction

We first review literature on prototyping from the viewpoint of empirical research, focusing particularly upon impacts of prototyping upon IS users. Most of the research has been qualitative, based on individual cases. Although there is no reason to underestimate the value of the practical knowledge obtained in those cases, it is to somewhat anecdotal.

Next we present the UIS measure we applied. It is based on the Bailey-Pearson measure, which was initially developed for the evaluation of total MIS/IS function rather than of individual application IS.

## 2.1. Brief History of Prototyping

There has been considerable interest in prototyping during the last decade, even though the initial enthusiasm has faded. The articles on prototyping, even the most recent, are mainly conceptual, dealing with questions like “What is an IS prototype?”, “What is prototyping as an IS development approach?”, “How is prototyping related to more traditional approaches?”, “What are the types of prototyping?” and “How should one apply prototyping in different contexts? (e.g. [4,9,12,13,15,16,27,28,29,31,33,34,38]). There has also been considerable interest in prototyping environments in the context of both Software Engineering (e.g. [17,39]) and Application Generator/4GLs (e.g. [32]).

Here we assume a prototype to have four characteristics [19]: it is a real system, it corresponds to a certain abstract model for or idea of the intended IS, it is able to exhibit or illustrate the abstract model or idea, and finally it is initially intended to be used only experimentally. The last emphasizes that it is important to realize that a prototype may not be satisfactory from the users' viewpoint and/or that its technical quality will not be adequate for production use. This means that the prototype will be abandoned, but by no means denies the possibility of software reuse for development of the next version. The above characterization also allows a prototype to transition into production use, if it is satisfactory to the users and of acceptable quality.

We are interested in two kinds of prototype: the skeletal interaction prototype, which is able to exhibit only the behaviour of the user interface, and the full-scale system prototype, which normally includes only a partial (sample) data base.

Existing empirical experience of prototyping is almost entirely qualitative, based on individual cases. Due to this, the frequently cited advantages and potential problems involved in it (e.g. [2,4,5,8,12,15,27,28,31,33,40,43]) can still be regarded as anecdotal “folk facts” [8], even though the value of the experience should not be underestimated. To our knowledge, only the comparative study of prototyping and specification by Boehm et al. [7] and of prototyping and traditional life-cycle approach by Alavi [1] form clear exceptions.

Boehm et al. compared the development of a common software item (a version of the COCOMO model, [6]) by seven student teams, three of which applied prototyping and the remaining four more traditional specification. The primary interest of this study lies in Software Engineering issues of SW quality and development productivity rather than in UIS issues. Since the content of the software (i.e. algorithms and tables) was provided, it is clear that they used the term ‘specification’ in a more limited sense, though including user interface specification. They found that prototyping resulted in software with roughly the same performance (functionality, robustness, ease of use and ease of learning) but with about 40% less code and 45% less effort. It also led to a somewhat lower functionality and robustness, but greater ease of use and ease of learning.

Alavi's study identifies five major categories of perceived benefits of prototyping on the basis of a field interview of twelve IS development projects in six organizations: the prototype is real and provides the users with a tangible means of comprehending and evaluating the proposed system, it provides a common reference point for both user and designers, prototyping supports user participation and commitment to a project, it establishes better communication and relationships between users and designers, and it helps to ensure that the nucleus idea of the system is right. The perceived drawbacks are the possibility of overselling prototypes, leading to unrealistic expectations, problems of managing and controlling prototyping, the difficulty of applying it in the case of a large IS, and the problem of maintaining user enthusiasm. She also experimented with the development and use of an IS for investment analysis and planning in an experimental setting consisting of nine user and nine designer groups, all composed of students, randomly matched with each other. Each user/designer group was assigned to follow either the prototyping or the life-cycle approach. The dependent variables were user evaluation of and satisfaction with the system, users' and system designers' attitudes and perceptions of the development approaches, and extent of use of the system. All in all, the prototyping approach performed well. The users' overall evaluation and satisfaction with the system, the accuracy and helpfulness of its output reports, their satisfaction with the level of user participation and perceptions of conflict between users and designers were given a statistically significantly more favourable rating in the case of prototyping. Also the remaining user-defined variables (with the exception of timeliness of output reports, which was rated equally), i.e. ease of communication, user understanding of the project and the extent of use, were ranked higher in the case of prototyping. On the other hand, the designers perceived the management and control of the design process to be more difficult in the case of prototyping and there were more changes in user requirements when using this approach.

To summarize, on the basis of the existing practical and more scientific evidence it is reasonable to assume that prototyping provides considerable advantages over the traditional linear life-cycle approach, although the studies have limitations due to their experimental nature and the small samples used. Our main criticism is that neither analyses or explains how or why prototyping gave the advantages. Both consider prototyping versus a more traditional approach as an independent variable, even though prototyping is a multitude of ideas, e.g.

\- prototyping is an adaptive IS design process in which learning has an important role,

\- prototyping has a non-linear structure, and consequently the process does not proceed strictly sequentially,

\- prototyping includes the idea of alternative designs,

\- prototyping assumes active user participation,

\- prototyping allow "hands-on" experimentation with the system.

The first four are not logically related to prototyping, but they can be applied without prototyping, too [19].

Our basic assumption is that abstract descriptions, interaction prototypes and system prototypes are alternative and complementary means of communicating the idea of the information system to its users. Our interest is in comparing these means, regarding the evolution of UIS as an indicator of the user's understanding of the system.

## 2.2. User Information Satisfaction

The concept of User Information Satisfaction (UIS) has been a subject of lively research during recent years and an increasing number of articles have emerged recently criticising existing UIS research from different perspectives (cf. [11,18,44]). Although we have participated in this criticism, we regard UIS as an important measure of the relationship between the user and the IS [20].

![](/api/attachments/79JRXR92/fulltext/images/957901db4fb99af809026bbb127f6f9f4a666fbe71e46004d171cfa5507ebef7.jpg)  
Fig. 1. A construct for user information satisfaction.

Ives, Olson and Baroudi compared a number of UIS constructs and expressed their preference for the Bailey–Pearson measure ([3,37]) as a candidate for a standard measure for UIS [26]. Even though we are not completely satisfied with its theoretical background, its operational measurement part, based on the semantic differential technique, is the most well-developed and best validated so far. For these reasons we selected the Bailey–Pearson measure for the assessment of UIS in our study, though it has the clear drawback that it is intended for the measurement of total MIS/IS function rather than that of an individual application. In order to overcome this problem we used the Iivari–Koskela construct of UIS [22] to constrain the relevant part of measure. This construct, depicted in Figure 1, was initially developed to support the selection of the conceptual-infological specifications of an information system during IS development. It describes each user's belief or perception regarding how well the information system satisfies his/her ideal information requirements.

Fig. 1 also describes the correspondence between the Iivari–Koskela construct and the Bailey–Pearson measure, leading to the inclusion of the ten scales in this study. For clarity, we have also supplemented the scales with the ordinal numbers from the original Bailey–Pearson measurement instrument.

The translation of the Bailey–Pearson questionnaire into Finnish was validated in an earlier project ([41,42]). The questionnaire used here included the English terms, as well, since most respondents has a fairly good command of English.

## 3. The Action Research Project

During Spring 1985, the Institute of Information Processing Science carried out a graduate student project involving the IS master plan for the Regional Studios of Oy Yleisradio Ab in Oulu. The first author participated in the project as a supervisor and member of the steering committee and the second as a professional IS designer and student. The project produced the idea of developing an IS to support reporters by providing them with background information for radio and TV programmes. This led to a new project. In this, the first author participated as a member of the steering committee and senior researcher and the second as a professional IS designer and junior researcher.

Oy Yleisradio Ab, the state-owned broadcasting company in Finland, has a network of regional studios covering the country. The task of the Oulu studio is to make and broadcast regional radio programmes in the region and to provide both radio and TV news programmes and other daily reports for broadcasting throughout the country. The staff at the studios at the time of the project numbered about 30, about half of whom were reporters. Yleisradio had a centralized Data Administration and EDP Department in Helsinki, with two IBM-4341 mainframes. In addition to IBM system software, the company made extensive use of software products from Cullinet Software, Inc.; e.g. the IDMS database management system and ADS/OnLine application generator.

The background system to be developed was limited to the local governmental areas, or communes, of the Oulu region, and the resultant Communal Database System (CDBS) was to be implemented using the IDMS and ADS/OnLine. The first phase of the project, which started in July 1985, was the organizational analysis and design of the information system, which was carried out in July and August and took about 3 man-months. The phase included analysis of the existing work of reporters, interest groups and actors involved, problem perceptions, likely future factors, goals of the system, and the design and evaluation of organizational alternatives for the system (cf. [21]).

During the analysis, it turned out that the reporters initially had quite different expectations. The problem did not result from the non-existence of information about the local communes, but in its dispersion and inaccessibility. The material can, in principle, be found from different sources, such as telephone directories, brochures, annual reports, official statistics etc.; memorization and informal contacts also play a crucial role in this process. The problem was accentuated, however, by the fact that the reporters were not assigned based on topic or geographical area, but every reporter was responsible for all kinds of programs.

There were three major dimensions in the design of alternatives for the CDBS at the organizational level: organization of the input and output use of the system, inclusion of official statistical information collected by the Central Bureau of

![](/api/attachments/79JRXR92/fulltext/images/9b2b49c60eefa2ff552b50c430acca2a99f9deb52bb2e972ef5f514ae55388b2.jpg)  
Fig. 2. The scope of the Communal Database System (CDBS).

Statistics, and the relationship to the follow-up system for earlier programmes. At the time, it was not possible to hire any extra persons to input data and to “chauffeur” the output use, so the reporters had to take care of it themselves. Use of the system was therefore planned to be voluntary. The official statistics about the local communes were excluded. Since reporters in Oulu unanimously supported the development of the follow-up system, the first decision by the steering committee was to include it in the project. After a couple of weeks it turned out that this effort would have to be cancelled, because of overlapping development in Helsinki. The scope of the CDBS after the first phase of the project is outlined in Fig. 2.

## 3.1. The Abstract Specification

Since the information system to be developed was clearly database-oriented, requirements specification was started by developing its conceptual schema. The design took place according to the normal procedure: defining the user views first and then integrating them. This led to a conceptual schema, part of which is depicted in Fig. 3. Despite the differences in notation (cf. [23]), this schema can be considered an extension of the familiar ER model [10]. Integration was quite straightforward, since, after the initial scoping of the system, user views were highly compatible and relatively close, when one considers the many potential alternatives for restricting the conceptual schema.

![](/api/attachments/79JRXR92/fulltext/images/699d7e9824ab1ece214c1a31d2d27a4e2a68a9b8632a63b683514b1b8817e35d.jpg)  
Fig. 3. Part of the conceptual schema.

The user interface was described by taking account of the conceptual schema as well as the technical implementation environment of the system. Fig. 4 shows some of this interaction. The arrows above the left-hand corners of the parallelograms indicate user inputs while those on the right are system outputs. The parallelograms including vertical lines are not elementary input or output displays, but can be decomposed further (cf. [24]). The implementation environment required the interaction to be structured, based on menus, form-filling and functional keys. As indicated, the interaction pattern followed the structure of the conceptual schema very closely.

Abstract specification started at the beginning of September and was completed in December, 1985. There were several reasons for this long time. As mentioned, a couple of weeks was lost due to the specification of a follow-up system. The project group was also obliged to acquaint itself with the ADS/OnLine application generator, and development of the interaction prototype took place partly in parallel with the abstract specification. The planning and implementation of the UIS questionnaires and interviews also took time. All in all, the abstract specification of the CDBS took about 2.5 man months, a considerable part of which (about 50%) was taken up by the interaction descriptions.

After completing the abstract specification, the integrated conceptual schema and related interaction descriptions were introduced to reporters in a review session of about one hour. Here the conceptual schema and interaction descriptions were supplemented with response time estimates (appr.

![](/api/attachments/79JRXR92/fulltext/images/68c272329e54360e72c7f60b7560bdbb12a821de896b4df0895e60bcdc961443.jpg)  
Fig. 4. Part of the user interface description.

![](/api/attachments/79JRXR92/fulltext/images/9ca7026e6f48cefc68144b59e0a8f97324e25fcfa68ecfaf236efd2b4756f52b.jpg)  
Fig. 5. Part of the displays of the interaction prototype.

1 second) and the displays were explained. The review led to some minor changes, which were made on the spot. After the session the reporters completed the UIS questionnaire. Due to leaves, illness, incomplete answers, etc., only ten acceptable replies were received.

## 3.2. The Interaction Prototype

The interaction prototype was completed at the end of December, 1985. The work took about 2 man-months. The prototype was implemented using ADS/OnLine dialogue prototyping facilities, thereby allowing skeletal simulation of the dialogues and displays (forms) without any actual data. Fig. 5 describes part of the interaction prototype.

The interaction prototype was demonstrated to reporters in review sessions which lasted about 20 minutes. Each of the ten reporters used the prototype under the guidance of the second author; they commented on it, suggested ways of developing it, and finally completed the UIS questionnaire. The new ideas included addition of organizations as entries in the main menu, a faster exit to it (in the worst case the prototype required pushing the “return” key PF15 five times in order to return to the main menu), etc.

## 3.3. The System Prototype

It was decided that the system prototype should be implemented on the basis of the interaction prototype, irrespective of the development suggestions. The database was implemented as a network structure in IDMS, and the processes invoking the database operations were programmed. The system prototype was completed during Spring 1986 and took about 3.5 man-months.

Real data were collected from two communes (of over fifty) for experimentation purposes. It turned out during this process that the set-up cost for the whole system would be considerable, due to the data collection involved. After the sample database was founded the system was evaluated in sessions guided by the second author; the third round of UIS evaluation was completed by ten respondents.

After the specification phase the action research project finished, responsibility for the final completion and technical implementation of the CDBS was transferred to the Department of Data Administration in Helsinki. One year after the completion of the project, the system had still not been implemented at any regional studio. One important reason for this is that it is unrealistic to expect the reporters to take care of initial collection of the data. But after implementation, updating should not be very laborious, since the volatility of the system is relatively low. Also more extensive IS development work is going on, involving implementation of the final CDBS.

## 3.4. Hypotheses

Despite the implementation problems associated with the CDBS, the project provides an interesting case study, since exactly the same system, from the users' viewpoint, was evaluated three times on the basis of three alternative representations. Our conjecture is that the users' understanding of the system increased during the specification process, implying that the UIS evaluations grew successively more “truthful”. Since we do not have any post-implementation UIS evaluations of the system, we are obliged to use the UIS scores obtained after the system prototype as the most reliable estimate. Even though there is certain variation due to individual difference, we shall use the mean scores of UIS as an indicator of the satisfaction. Making the above assumptions, we are led to:

Hypothesis 1. The mean UIS is strictly increasing or decreasing during the specification phase.

Even though our interest here is not in the validity or reliability of the UIS measure, it is interesting to analyse how the users' increased understanding of the system influenced the reliability of the measure. Reliability, as the absence of measurement error, is conventionally assessed using Cronbach's alpha test (e.g. [35]). Our hypothesis is that the reliability increased during the successive rounds of UIS measurement:

Hypothesis 2. The reliability of the successive UIS measurements is strictly increasing.

The following section proceeds to test these hypotheses empirically.

## 4. Results and Discussion

## 4.1. Results

Table 1 shows the mean UIS values in the three rounds of evaluation. Since we are concerned with repeated measurements, only respondents who participated in at least two rounds are included. Differing slightly from the Bailey–Pearson procedure [3], total UIS for each respondent was calculated as the arithmetic average of the ten constituent scales, since omission of the neutral, zero values produces anomalies, as observed by Treacy [44]. We also agree that a neutral response does not mean that it should be dropped.

Table 1
Mean UIS values.

<table><tr><td>Round</td><td>Mean</td><td>t values</td></tr><tr><td>Abstract specification</td><td>0.76 (n = 8)</td><td></td></tr><tr><td>Interaction prototype</td><td>0.96 (n = 9)</td><td> $t_{21} = 0.88$ </td></tr><tr><td>System prototype</td><td>0.56 (n = 9)</td><td> $t_{31} = -0.59$   $t_{32} = -2.08$ </td></tr></table>

Table 4
Average item variances.  
Table 2
Mean UIS scale values.

<table><tr><td>Scale</td><td>Abstract specification</td><td>Interaction prototype</td><td>System prototype</td></tr><tr><td>Completeness</td><td>0.31</td><td>0.53</td><td>-0.29</td></tr><tr><td>Precision</td><td>0.81</td><td>1.19</td><td>0.19</td></tr><tr><td>Currency</td><td>0.57</td><td>0.38</td><td>0.47</td></tr><tr><td>Reliability</td><td>0.93</td><td>1.22</td><td>0.72</td></tr><tr><td>Accuracy</td><td>0.84</td><td>1.22</td><td>0.81</td></tr><tr><td>Convenience</td><td>1.06</td><td>1.17</td><td>0.78</td></tr><tr><td>Response time</td><td>1.17</td><td>1.17</td><td>1.03</td></tr><tr><td>Language</td><td>0.72</td><td>1.14</td><td>0.81</td></tr><tr><td>Format</td><td>0.97</td><td>1.44</td><td>1.00</td></tr><tr><td>Flexibility</td><td>0.32</td><td>0.42</td><td>0.11</td></tr></table>

The results suggest that Hypothesis 1 of the previous section must be rejected. The interaction prototype seemed to produce a higher UIS score than the other two, and the system prototype the lowest, although only the difference between the interaction and system prototypes turned out to be statistically significant at the level 0.05 (one-tailed testing). Downie and Starry remark that the t test can be used for testing means of dependent, paired samples of quite small sample sizes (n = 10) provided that the underlying distribution approaches normality [14]. It is difficult to test the normality in the case of our small sample, of course, but the distribution after the system prototype was much closer to normal than that in the two previous rounds (2 between (-1.5) - (-0.5), 2 between (-0.5) - (+0.5), 3 between (+0.5) - (+1.5) and 2 between (+1.5) - (+2.5). In any case this suggests that it is justifiable to look at the means of the ten constituent scales.

<table><tr><td>Scale</td><td>Abstract specification</td><td>Interaction prototype</td><td>System prototype</td></tr><tr><td>Completeness</td><td>1.67</td><td>0.78</td><td>1.31</td></tr><tr><td>Precision</td><td>0.97</td><td>0.93</td><td>3.26</td></tr><tr><td>Currency</td><td>1.16</td><td>1.23</td><td>1.85</td></tr><tr><td>Reliability</td><td>0.66</td><td>0.76</td><td>1.44</td></tr><tr><td>Accuracy</td><td>0.59</td><td>0.48</td><td>1.59</td></tr><tr><td>Convenience</td><td>1.01</td><td>0.83</td><td>1.93</td></tr><tr><td>Response time</td><td>0.47</td><td>0.80</td><td>2.37</td></tr><tr><td>Language</td><td>1.12</td><td>1.33</td><td>1.95</td></tr><tr><td>Format</td><td>0.89</td><td>1.18</td><td>1.54</td></tr><tr><td>Flexibility</td><td>0.83</td><td>1.80</td><td>2.54</td></tr></table>

The results are given in Table 2, which indicates that the interaction prototype gave consistently higher values than the abstract specification or the system prototype, the only exception being currency. The system prototype gave the lowest value in seven cases out of ten. The differences between the means were not statistically significant. The only exception was completeness, between the interaction and system prototypes.

The scale variances increased during the three rounds of specification (Table 3). This was particularly true in the case of the system prototype. The increase was partly due to the increased item variances (Table 4), but also due to increased inter-item correlations (Table 5).

The correlations lead us to the second hypothesis, which concerned the reliability of the UIS measurements. Cronbach's alpha coefficients, calculated using the formula $kr/(1+(k-1)r)$

Table 3  
Variances of UIS scales.

<table><tr><td>Scale</td><td>Abstract specification</td><td>Interaction prototype</td><td>System prototype</td></tr><tr><td>Completeness</td><td>0.95</td><td>0.51</td><td>1.10</td></tr><tr><td>Precision</td><td>0.71</td><td>0.62</td><td>3.06</td></tr><tr><td>Currency</td><td>0.43</td><td>0.95</td><td>1.57</td></tr><tr><td>Reliability</td><td>0.51</td><td>0.63</td><td>1.35</td></tr><tr><td>Accuracy</td><td>0.37</td><td>0.35</td><td>1.48</td></tr><tr><td>Convenience</td><td>0.83</td><td>0.63</td><td>1.96</td></tr><tr><td>Response time</td><td>0.45</td><td>0.70</td><td>2.46</td></tr><tr><td>Language</td><td>0.72</td><td>0.94</td><td>1.68</td></tr><tr><td>Format</td><td>0.86</td><td>1.04</td><td>1.44</td></tr><tr><td>Flexibility</td><td>0.72</td><td>1.55</td><td>2.43</td></tr><tr><td>Total UIS</td><td>0.20</td><td>0.38</td><td>0.91</td></tr></table>

Table 5  
Average inter-item correlations and the proportion of statistically significant correlations (0.05 level).

<table><tr><td>Scale</td><td>Abstract specification</td><td>Interaction prototype</td><td>System prototype</td></tr><tr><td>Completeness</td><td>0.46 (4/12)</td><td>0.49 (0/12)</td><td>0.69 (6/12)</td></tr><tr><td>Precision</td><td>0.53 (4/12)</td><td>0.64 (2/12)</td><td>0.90 (12/12)</td></tr><tr><td>Currency</td><td>0.16 (2/12)</td><td>0.67 (6/12)</td><td>0.80 (10/12)</td></tr><tr><td>Reliability</td><td>0.77 (6/12)</td><td>0.78 (10/12)</td><td>0.93 (12/12)</td></tr><tr><td>Accuracy</td><td>0.51 (2/12)</td><td>0.67 (4/12)</td><td>0.92 (12/12)</td></tr><tr><td>Convenience</td><td>0.83 (10/12)</td><td>0.74 (8/12)</td><td>0.82 (10/12)</td></tr><tr><td>Response time</td><td>0.87 (12/12)</td><td>0.93 (12/12)</td><td>0.88 (12/12)</td></tr><tr><td>Language</td><td>0.86 (12/12)</td><td>0.68 (8/12)</td><td>0.79 (12/12)</td></tr><tr><td>Format</td><td>0.97 (12/12)</td><td>0.88 (12/12)</td><td>0.94 (12/12)</td></tr><tr><td>Flexibility</td><td>0.83 (8/12)</td><td>0.76 (10/12)</td><td>0.95 (12/12)</td></tr></table>

Table 6 Cronbach's alphas.

<table><tr><td>Scale</td><td>Abstract specification</td><td>Interaction prototype</td><td>System prototype</td></tr><tr><td>Completeness</td><td>0.78</td><td>0.80</td><td>0.90</td></tr><tr><td>Precision</td><td>0.82</td><td>0.88</td><td>0.97</td></tr><tr><td>Currency</td><td>0.44</td><td>0.89</td><td>0.94</td></tr><tr><td>Reliability</td><td>0.93</td><td>0.94</td><td>0.98</td></tr><tr><td>Accuracy</td><td>0.81</td><td>0.89</td><td>0.98</td></tr><tr><td>Convenience</td><td>0.95</td><td>0.92</td><td>0.95</td></tr><tr><td>Response time</td><td>0.96</td><td>0.98</td><td>0.97</td></tr><tr><td>Language</td><td>0.96</td><td>0.89</td><td>0.94</td></tr><tr><td>Format</td><td>0.99</td><td>0.97</td><td>0.99</td></tr><tr><td>Flexibility</td><td>0.95</td><td>0.93</td><td>0.99</td></tr></table>

where k is the number of items and r the average inter-item correlation, are listed in Table 6. In accordance with Hypothesis 2, reliability generally increased during the rounds of UIS evaluation. In six cases out of ten, the abstract specification has the lowest score, and in eight cases out of ten the system prototype is the highest, or at least as high as in the preceding two rounds.

Because we are concerned with an ex ante evaluation, the reliability coefficients are perhaps unrealistically high. With one exception they were 0.78 or more, and all the coefficients were 0.90 or more after the system prototype. Note that Nunally suggests that in applied settings a reliability of 0.90 is the minimum and 0.95 desirable. The high reliability scores are partly due to the fact that, in accordance with the Bailey–Pearson instrument, items forming a scale were grouped together and had the same direction. This practice has been advocated by Nunally, who remarks that the practice of randomly or systematically alternating the polarities “probably is not worth the price that is paid in measurement error”. Our case also has its limitations. It concerned only one system and the number of participants was very limited. Nunally suggests that measurement theory is a “large sample” theory, in which the sampling error arising from the sampling of people is a minor consideration, and he assumes a minimum of 300 persons in his analysis of measurement error. Consequently, we should not pay too much attention to the absolute reliability scores, but in accordance with Hypothesis 2 our main interest lies in the trend in reliability during the three rounds.

Even though the increased reliability of the UIS measures in general terms was to be expected, it is interesting to analyse the reasons for this increase. Cronbach's alpha formula, based on inter-item correlations, emphasizes the internal consistency of UIS scales. Another perspective and interpretation is opened up when the reliability is calculated using the formula $1 - V_{r}/V_{s}$ , where $V_{r}$ is the residual (error) variance and $V_{s}$ the variance because of individual differences between subjects ([30,35]). Table 7 summarizes the results of the two-way variance analysis. There were a few item values missing; these were offset by zero values in the variance analysis. Therefore, the reliability coefficients derivable from the results of Table 7 in some cases differ from those in Table 6. The numbers in parentheses are estimated for variances obtained by dividing the preceding number by the degree of freedom in question. Results indicate a consistent increase in the variation due to subjects. In all ten cases, the system prototype has the highest score on this component, and in most cases it is much higher than the preceding two rounds. Assuming that the system prototype provides the most realistic estimate for the true variation due to individual differences, it is obvious that the preceding two rounds were not able to reveal the true variation between subjects.

Table 7
Variance analysis.

<table><tr><td>Scale/source of variance</td><td>Abstract specification</td><td>Interaction prototype</td><td>System prototype</td></tr><tr><td colspan="4">Completeness</td></tr><tr><td>Total</td><td>56.72</td><td>25.87</td><td>44.00</td></tr><tr><td>Items</td><td>10.10 (3.37)</td><td>4.22 (1.41)</td><td>3.33 (1.11)</td></tr><tr><td>Subjects</td><td>25.97 (3.71)</td><td>13.37 (1.91)</td><td>30.00 (3.75)</td></tr><tr><td>Residual</td><td>20.65 (0.98)</td><td>8.28 (0.39)</td><td>10.67 (0.44)</td></tr><tr><td colspan="4">Precision</td></tr><tr><td>Total</td><td>27.87</td><td>26.22</td><td>106.75</td></tr><tr><td>Items</td><td>0.62 (0.21)</td><td>0.10 (0.03)</td><td>2.31 (0.77)</td></tr><tr><td>Subjects</td><td>16.87 (2.41)</td><td>18.97 (2.71)</td><td>96.00 (12.00)</td></tr><tr><td>Residual</td><td>10.38 (0.49)</td><td>7.15 (0.34)</td><td>8.44 (0.35)</td></tr><tr><td colspan="4">Currency</td></tr><tr><td>Total</td><td>32.86</td><td>37.50</td><td>62.97</td></tr><tr><td>Items</td><td>5.15 (1.72)</td><td>3.00 (1.00)</td><td>3.86 (1.29)</td></tr><tr><td>Subjects</td><td>10.36 (1.73)</td><td>26.50 (3.79)</td><td>50.22 (6.28)</td></tr><tr><td>Residual</td><td>17.35 (0.96)</td><td>8.00 (0.38)</td><td>8.89 (0.37)</td></tr><tr><td colspan="4">Reliability</td></tr><tr><td>Total</td><td>15.86</td><td>21.47</td><td>47.22</td></tr><tr><td>Items</td><td>0.15 (0.05)</td><td>1.35 (0.45)</td><td>1.22 (0.41)</td></tr><tr><td>Subjects</td><td>12.36 (2.06)</td><td>17.72 (2.53)</td><td>43.22 (5.40)</td></tr><tr><td>Residual</td><td>3.35 (0.18)</td><td>2.40 (0.11)</td><td>2.78 (0.12)</td></tr><tr><td colspan="4">Accuracy</td></tr><tr><td>Total</td><td>18.22</td><td>13.47</td><td>51.64</td></tr><tr><td>Items</td><td>1.85 (0.62)</td><td>0.10 (0.03)</td><td>0.97 (0.32)</td></tr><tr><td>Subjects</td><td>10.47 (1.50)</td><td>9.72 (1.39)</td><td>47.39 (5.92)</td></tr><tr><td>Residual</td><td>5.91 (0.28)</td><td>3.65 (0.17)</td><td>3.28 (0.17)</td></tr><tr><td colspan="4">Convenience</td></tr><tr><td>Total</td><td>28.97</td><td>27.00</td><td>62.75</td></tr><tr><td>Items</td><td>1.10 (0.37)</td><td>0.33 (0.11)</td><td>0.97 (0.32)</td></tr><tr><td>Subjects</td><td>23.72 (3.39)</td><td>20.00 (2.50)</td><td>53.50 (6.69)</td></tr><tr><td>Residual</td><td>4.15 (0.20)</td><td>6.67 (0.28)</td><td>8.28 (0.35)</td></tr><tr><td colspan="4">Response time</td></tr><tr><td>Total</td><td>14.72</td><td>26.72</td><td>73.89</td></tr><tr><td>Items</td><td>1.10 (0.37)</td><td>0.85 (0.28)</td><td>0.56 (0.18)</td></tr><tr><td>Subjects</td><td>8.47 (1.21)</td><td>22.47 (3.21)</td><td>65.89 (8.24)</td></tr><tr><td>Residual</td><td>5.15 (0.25)</td><td>3.40 (0.16)</td><td>7.44 (0.31)</td></tr><tr><td colspan="4">Language</td></tr><tr><td>Total</td><td>31.50</td><td>43.00</td><td>63.00</td></tr><tr><td>Items</td><td>0.25 (0.08)</td><td>0.56 (0.19)</td><td>0.56 (0.19)</td></tr><tr><td>Subjects</td><td>25.00 (3.57)</td><td>32.00 (4.00)</td><td>51.50 (6.44)</td></tr><tr><td>Residual</td><td>6.25 (0.30)</td><td>10.44 (0.44)</td><td>10.94 (0.46)</td></tr><tr><td colspan="4">Format</td></tr><tr><td>Total</td><td>24.97</td><td>38.31</td><td>50.00</td></tr><tr><td>Items</td><td>0.10 (0.03)</td><td>0.45 (0.18)</td><td>0.89 (0.30)</td></tr><tr><td>Subjects</td><td>24.22 (3.46)</td><td>31.56 (3.95)</td><td>46.00 (5.75)</td></tr><tr><td>Residual</td><td>0.65 (0.03)</td><td>6.30 (0.26)</td><td>3.11 (0.13)</td></tr><tr><td colspan="4">Flexibility</td></tr><tr><td>Total</td><td>20.11</td><td>56.75</td><td>81.56</td></tr><tr><td>Items</td><td>0.11 (0.04)</td><td>2.52 (0.84)</td><td>0.12 (0.04)</td></tr><tr><td>Subjects</td><td>17.36 (2.89)</td><td>43.50 (5.44)</td><td>77.56 (9.70)</td></tr><tr><td>Residual</td><td>2.64 (0.15)</td><td>10.73 (0.45)</td><td>3.89 (0.16)</td></tr></table>

## 4.2. Discussion

Before going into detailed discussion, it is reasonable to ponder whether there were factors related to the measurement which might explain the results. First of all, we were concerned with an ex ante assessment of UIS among respondents who did not have any previous experience of the on-line use of IS in their work. The lack of user experience may partly explain the results, although we have pointed out that there is no drastic difference between the ex ante and ex post assessment of UIS [20], if UIS is interpreted in the sense of users' beliefs in the capability of the IS to meet their information requirements. Secondly, we should remember that the ex ante assessment did not allow any direct evaluation of the system, but took place indirectly through the three representations of the future system. This leads us to question whether the users assessed the representations rather than the idea of the future system. It is clear that the users did not assess the representations, since some of the scales would have been totally meaningless (e.g., the response time of the abstract specification). Also some of the specific results, such as the score on the completeness dimension after the system prototype, indicate that they were evaluating the idea of the whole system rather than the system prototype itself. Thirdly, since the UIS questionnaires were completed in a real life setting after the review sessions, we think that the answers are at least as reliable as in UIS studies based on mailed questionnaires and answers. Finally, we recognize that our study is, of course, limited to one project, with a small “sample” size and nonrandom selection of respondents; consequently the results are only exploratory in nature.

Although only exploratory, the results support Alavi's observation that prototyping may “oversell” the system by creating unrealistic expectations. This emerged especially in the case of the interaction prototype. It is important to recognize that “overselling” does not necessarily take place intentionally, but due to the fact that the prototype is only a model of the real IS. Its purpose is to illustrate certain ideas of the system; it abstracts away certain features and may also include some features which are not intended in the final system. In our case, the primary purpose of the interaction prototype was to illustrate aspects related to convenience, format of output, and language, and it succeeded relatively well, even though the scores were somewhat higher than after the system prototype. It created excessively optimistic expectations with regard to the completeness and precision dimensions, since no database was implemented, even though the dialogues corresponded very closely to the conceptual schema. Although interaction prototypes often give faster response times than the real system, since there are no database operations, this did not cause any problems.

On the other hand, the system prototype gave a relatively low score on the completeness criterion. This may partly be explained by the incompleteness of the sample database. It was clear to the reporters that the database was only a sample, and in fact the scores on the completeness dimension were not so low that one could conclude that the assessment took place only in terms of the sample database. Anyhow, the above experience suggests that inasfar as the prototype is only a model of the final system, the idea that is being prototyped and the potential limitations and extra features of the prototype should be made clear to the users assessing the idea. Maybe we were not careful enough in that respect. As expected, the reliability of the UIS scores generally increased during the specification process. Variance analysis indicated that this was largely because of the increased variance due to individual differences, particularly after system prototyping. Assuming that the UIS scores after this step provide the most realistic estimate for the true variance, the results imply that the abstract specification and interaction prototype were not able to reveal the “true” variance between individuals. We can put forward three explanations for this:

1. The results are due to real changes in the users' information requirements and satisfaction with the system;

2. The results are due to the representations;

3. The phenomenon was due to an uncertainty effect.

One cannot exclude the first explanation, even through we consider it quite unlikely. To our knowledge, there were no environmental events (e.g., changes in work, etc.) which could have produced such a change. Neither do we believe that the IS design process would have changed users' information requirements, since their participation was limited to interviews and review sessions.

The first association in the second explanation may be that the abstract specification was totally static, whereas the interaction and system prototypes were dynamic. Although the abstract specification exhibited the dynamic behaviour by means of interaction descriptions, it was exactly the same for each user, while experimentation with the prototypes varied to a greater or lesser extent depending on the selected dialogue paths. This may be a valid explanation, but it raises a further problem: how to ensure sufficient coverage of the system features when experimenting with a prototype. The explanation does not seem sufficient, however, since it does not serve to explain the difference in variance after the interaction prototype and system prototype. One should also observe that there was not much qualitative variation in the features and behaviour of the system. The user interface was uniform, and the different dialogue paths in the menu structure were highly comparable. We are prepared to admit, however, that the three representations gave different understanding of the system, and we suggest that the results may be attributed to differences in uncertainty concerning the system.

The third explanation is that the uncertainty of the system and the users' own requirements, eliminate extreme values and increase the proportion of near-neutral values. Assuming that the uncertainty decreased during the three rounds of the specification phase, our experience partly supports an uncertainty effect. In general terms, the average item variances increased, and if the values of the forty items are taken together the proportion of absolute values equal to or greater than 2 was 25% in the case of the abstract specification, 30% after the interaction prototype, and 40% after the system prototype. This effect implies that there is a systematic bias towards small absolute values as uncertainty increases. Consequently, the measurement error is not random and independent of the values of the scale as the standard measurement theory assumes. Even though this systematic bias may reduce the average correlations and consequently decrease coefficient alpha, this is not necessarily the case.

From the theoretical and practical viewpoint, it is important to observe that if we define UIS as a user's belief that the system is able to meet his/her information requirements, the uncertainty is not limited to ex ante assessment of UIS, but concerns ex post evaluation as well. In the case of complex IS there may be considerable uncertainty about a system, its capabilities and the user requirements. Consequently, we suggest that there is a serious need for further research into the potential uncertainty effect suggested above. Surprisingly, we have not encountered any discussion on this in methodological textbooks, and still less in existing empirical UIS research. Nunally [35] discusses different sources of error, the impact of self-knowledge, and Oppenheim [36] recognizes “uncertain” responses due to a lack of awareness, but neither discusses the problem of uncertainty. Referring particularly to the Bailey-Pearson measure, the uncertainty effect may partly be resolved by the procedure of omitting scales with only zero item values. The reason for this procedure is not clearly explained, however, and the procedure leads to other problems [44]. Assuming that the uncertainty effect really exists, we have also the problem of whether different measurement techniques include it equally. The semantic differential technique, for instance, may explain or amplify it, since the bipolarity of items may push answers to the neutral center in the case of uncertainty.

## 5. Final Comments

This study provides some evidence that prototyping may create unrealistic expectations, and more generally emphasizes the need for specifying the idea that is being prototyped, and communicating this idea to the users experimenting with the prototype. But perhaps its most important result is that there may be an uncertainty effect in the measurement of UIS that should be given considerable attention in future research.

The project illustrates the need for careful organizational analysis and design prior to prototyping. The project group failed somewhat in this respect. Our experience was also that the conceptual schema was very useful in the design of the prototypes, whereas the interaction prototype could have been designed without the separate interaction descriptions. The prototypes proved to be highly effective for the early identification of different specification “faults”, although the proposed changes were not taken into account here.

The study was carried out in connection with a real action research project, which lived its life more or less independent of the research plans. This situation naturally requires adaptive research planning, and consequently very intensive involvement of the researchers. In this respect, the project failed to some extent, since the first author, as the senior researcher, was not able to follow the project on a daily basis. The problem was accentuated by the role dilemma affecting the junior researchers; what priority they should give to the role of IS designer and what priority to that of researcher, when the project was falling behind.

## Acknowledgements

The authors are grateful to the whole staff of the Regional Studios of Oy Yleisradio Ab in Oulu, and to Messrs. Olavi Niemelä, Antti Lamppula and Risto Terkki from the Department of Data Administration for their kind cooperation. We are also indebted to Pasi Kuvaja, who acted as project manager, and to Jaakko Kaivosoja, who acted as a second professional IS designer and junior researcher in the project. Finally, we wish to express our gratitude to Mr. Malcom Hicks for editing the English and to Prof. E.H. Sibley for the careful editing of the text.

## References

[1] M. Alavi, “An Assessment of the Prototyping Approach to Information Systems Development”, Communications of the ACM, Vol. 27, No. 6, 1984.

[2] M. Alavi and M.A. Napier, “An Experiment in Applying the Adaptive Design Approach to DSS Development”, Information & Management, Vol. 7, No. 1, 1984.

[3] L.E. Bailey and S.W. Pearson, "Developing a Tool for Measuring and Analyzing Computer User Satisfaction", Management Science, Vol. 29, No. 5, 1983.

[4] L. Bally, J. Brittain and K.H. Wagner, “A Prototype Approach to Information System Design and Development”, Information & Management, Vol. 1, 1977.

[5] S. Belardo and K.R. Karwan, “The Development of a Disaster Management Support System Through Prototyping”, Information & Management, Vol. 10, 1986.

[6] B.W. Boehm, Software Engineering Economics, Prentice-Hall, Englewood Cliffs, New Jersey, 1981.

[7] B.W. Boehm, T.E. Gray and T. Seewaldt, “Prototyping versus Specifying: a multiproject experiment”, IEEE Transactions on Software Engineering, Vol. SE-10, No. 3, 1984.

[8] T.T. Carey and R.E.K. Mason, “Information System Prototyping: techniques, tools and methodologies”, INFOR, Vol. 21, No. 3, 1983.

[9] R.P. Cervany, E.J. Garrity and G.L. Sanders, “The Application of Prototyping to System Development: a rationale and model”, Journal of Management Information Systems, Vol. III, No. 2, 1986.

[10] P.P. Chen, “The Entity-Relationship Model – toward a unified view of data”, ACM Transactions on Database Systems, Vol. 1, No. 1, 1976.

[11] W.G. Chismar, C.H. Kriebel and N.P. Melone, “Criticisms of Information Systems Research Employing ‘User Satisfaction’”, Graduate School of Industrial Administration, Carnegie-Mellon University, WP 24-85-86, October 1985.

[12] D.A. Dearnley and P.J. Mayhew, “In Favour of System Prototypes and Their Integration into the Systems Development Cycle”, The Computer Journal, Vol. 26, No. 1, 1983.

[13] A.R. Dennis, R.N. Burns and R.B. Gallupe, “Phased Design: a mixed methodology for application systems development”, Data Base, Vol. 18, No. 1, 1987.

[14] N.M. Downie and A.R. Starry, Descriptive and Inferential Statistics, Harper & Row, New York, 1977.

[15] K.J. Earl, “Prototype Systems for Accounting Information and Control”, Accounting, Organizations and Society, Vol. 3, No. 2, 1978.

[16] C. Floyd, “A Systematic Look at Prototyping” in Approaches to Prototyping, eds. R. Budde, K. Kuhlenkamp, L. Mathiassen and H. Züllighoven, Springer-Verlag, Berlin, 1984.

[17] R. Goldberg, “Software Engineering: An emerging discipline”, IBM Systems Journal, Vol. 25, No. 3/4, 1986.

[18] D. Goodhue, “IS Attitudes: toward theoretical and definition clarity”, in Proceedings of the Seventh International Conference on Information Systems, eds. L. Maggi, R. Zmud and J. Wetherbe, San Diego, 1986.

[19] J. Iivari, “Prototyping in the Context of Information Systems Design”, in Approaches to Prototyping, eds. R. Budde, K. Kuhlenkamp, L. Mathiassen and H. Züllighoven, Springer-Verlag, Berlin, 1984.

[20] J. Iivari, "User Information Satisfaction (UIS) Reconsidered: an information system as an antecedent of UIS, in Proceedings of the Eight International Conference on Information Systems, eds. J.I. DeGross and C.H. Kriebel, Pittsburgh, 1987.

[21] J. Iivari, “A Methodology for IS Development as An Organizational Change: the IFIP case”, in Report of the Tenth IRIS (Information Systems Research in Scandinavia) Seminar, ed. P. Järvinen, Tampere, Finland, 1987.

[22] J. Iivari and E. Koskela, “Choice and Quality Criteria for Data System Selection”, in Proceedings of the EuroIFIP 79, European Conference on Applied Information Technology, ed. P.A. Samet, North-Holland, Amsterdam, 1979.

[23] J. Iivari and E. Koskela, "An Extended EAR Approach for Information System Specification", in Entity-Relationship Approach to Software Engineering, eds. C.G. Davis, S. Jajodia, P.A. Ng and R.T. Yeh, North-Holland, Amsterdam, 1983.

[24] J. Iivari and E. Koskela, "On Modelling of Human-Computer Interaction as the Interface between the User's Work Activity and the Information System", in Human-Computer Interaction - Interact'84, ed. B. Shackel, North-Holland, Amsterdam, 1985.

[25] J. Iivari and E. Koskela, “The PIOCO Model for IS Design”, MIS Quarterly, Vol. 11, No. 3, 1987.

[26] B. Ives, M.H. Olson and I.J. Baroudi, “The Measurement of User Information Satisfaction”, Communications of the ACM, Vol. 26, No. 10, 1983.

[27] M. Janson, “Applying a Pilot System and Prototyping Approach to Systems Development and Implementation”, Information & Management, Vol. 10, 1986.

[28] M.A. Janson and L.D. Smith, “Prototyping for Systems Development: a critical appraisal”, MIS Quarterly, Vol. 10, No. 4, 1985.

[29] M. Jenkins, “Prototyping: a methodology for the design and development of application systems”, Discussion

paper #227, Division of Research, Graduate School of Business, Indiana University, Bloomington/Indianapolis, 1983.

[30] F.N. Kerlinger, Foundation of Behavioral Research, Third Edition, CBS Publishing Japan Ltd, New York, 1986.

[31] J.M. Kraushaar and L.E. Shirland, “A Prototyping Method for Applications Development by End Users and Information Systems Specialists”, MIS Quarterly, Vol. 10, No. 3, 1985.

[32] J. Martin, Fourth-Generation Languages, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1985.

[33] B. McNurlan, “Developing Systems by Prototyping”, EDP Analyzer, Vol. 19, No. 9, 1981.

[34] J.D. Naumann and A.M. Jenkins, “Prototyping: The new paradigm for systems development”, MIS Quarterly, September 1982.

[35] J.C. Nunally, Psychometric Theory, McGraw-Hill, New York, 1967.

[36] A.N. Oppenheim, Questionnaire Design and Attitude Measurement, Gower, Aldershot, 1986.

[37] S.W. Pearson, Measurement of Computer User Satisfaction, Arizona State University, Tempe, 1977.

[38] N. Pliskin and P. Shoval, “End-user Prototyping: sophisticated users supporting systems development”, Data Base, Vol. 18, No. 4, 1987.

[39] C.V. Ramamoorthy, A. Prakash, W. Tsai and Y. Usuda, "Software Engineering Problems and Perspectives", Computer, October 1984.

[40] M.J. Segall, “The Use of Prototyping to Aid Implementation of an On-line System”, Systems, Objectives, Solutions, Vol. 4, No. 3, 1984.

[41] J. Similä, “Modelling and Analyzing Empirically the Success of ADP Systems Use”, in Report of the Eight Scandinavian Research Seminar on Systemeering, eds. M. Lassen and L. Mathiassen, Aarhus, Denmark, 1985.

[42] J. Similä and R. Nuutinen, “An Operationalized Model for Success in the User Role”, in Human-Computer Interaction - Interact'84, ed. B. Shackel, North-Holland, Amsterdam, 1985.

[43] J.M. Sroka and M.H. Rader; “Prototyping Increases Chance of Systems Acceptance”, Data Management, Vol. 24, No. 3, 1986.

[44] M.E. Treacy, “An Empirical Examination of a Causal Model of User Information Satisfaction”, Center for Information Systems Research, Sloan School of Management, Massachusetts Institute of Technology, 1985.
