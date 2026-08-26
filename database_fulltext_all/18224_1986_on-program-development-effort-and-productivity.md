---
otero_id: 18224
otero_key: "GH4WEP5E"
title: "On program development effort and productivity"
authors: "Iris Vessey"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90028-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On Program Development Effort and Productivity

Iris Vessey

University of Pittsburgh, Graduate School of Business,
Mervis Hall, Pittsburg, PA 15260, USA

Many claims are made in the literature concerning large productivity increases as a result of the introduction of various new programming tools and techniques. Seldom do the researchers substantiate these claims, however. Further, many of the reported studies have been unsuccessful because much of the existing research is methodologically flawed and poorly grounded in theory. This paper investigates the methodological problems of previous studies and reports the results of a field study conducted to assess the feasibility of conducting controlled studies of the programming process. A field study of COBOL programs from three commercial organizations investigated the effects of programming style (i.e., structured programming) and programmer skill on (i) the effort required to develop programs and (ii) programming productivity; program size was used as a control variable. The results of the study support the underlying concept: that use of disciplined approaches and well-defined variables leads to more readily interpretable and more conclusive results.

Keywords: Program development, programming productivity, program size, structured programming, programmer skill, program complexity.

![](/api/attachments/GH4WEP5E/fulltext/images/a1724fd4c25d65b9024f12e581ebc1479e93d7b18a1574c4bacb2b1373e67eb5.jpg)

Iris Vessey is Associate Professor in information systems at the Graduate School of Business, University of Pittsburgh. She was previously on the faculty of the University of Queensland, Australia. She received the Ph.D. degree from the University of Queensland in 1984. Her research interests focus on human factors in software engineering.

Acknowledgement: The author is indebted to Ron Weber and Ross Jeffery for comments on a previous version of the paper, and to the editor for his comments.

## 1. Introduction

This paper reports a field study that investigated, across organizations, certain factors commonly held to affect program development effort and programmer productivity. From a practical viewpoint, research on such factors is important for two reasons: first, to estimate the effort (and therefore cost) to develop a system; and second, to set performance standards for programmers, and ultimately, therefore, to increase programmer efficiency.

There have been several different types of attempts to estimate the cost of systems development. For a review, see [7]. Some approaches adopt a bottom-up or micro strategy, while others adopt a top-down or macro strategy. Examples of the top-down approach to cost estimating are those of Putnam [47] and Parr [45] who have developed predictive models for software cost estimating. These models forecast manpower requirements for large software engineering projects given specified development times. They also predict the minimum system development time; i.e., for development times shorter than the minimum, cost and time overruns are inevitable. Putnam [48] has, however, extended his work to include systems with as low as 15,000 expected lines of code, 24 man-months of effort, and development time of 6 months. Boehm [8] also uses a top-down approach to estimating software costs. His approach is more flexible, however, in that it provides three levels of decomposition and therefore also permits estimation of costs for individual phases.

Predictive models, such as those discussed above, describe an outcome and are, therefore, paramorphic in nature. Thus, the level of abstraction of a predictive model is too high to describe the underlying associations. Here, descriptive or isomorphic models are needed: models that establish a cause-effect relationship so that manipulation of certain input variables will cause certain output variables to be influenced in a desired manner. $^{1}$ Bottom-up approaches to cost estimating and establishing performance standards require detailed understanding of the factors underlying the programming process.

The factors that may play a role in determining the effectiveness of the programming process are many and varied. $^{2}$ In addition, the environment is continually changing. Much has been written in the literature about the effectiveness of a variety of new tools and techniques in aiding the systems development process. However, while many of these approaches may seem intuitively appealing and while the practical achievements claimed for them appear convincing, their use in an ongoing practical environment often has not been justified empirically. (For reviews of the studies conducted, see [46,50,59]).

Further, many of the attempts that have been made to assess the effectiveness of new programming tools and techniques have been unsuccessful. There are two reasons:

1. Many of the studies have been methodologically flawed.

2. Little attempt has been made to base the research on established theory.

In the absence of theory, empirical research can only be based on the evidence of previous studies. If those studies are methodologically unsound, then we have no basis for future research.

The objective of this paper is to highlight some of the methodological problems of previous studies and to indicate ways of overcoming those problems. The paper presents the results of testing some of the possible descriptive relationships influencing development effort and productivity. The factors tested in this study to determine their effects on development effort and productivity were programming style, and programmer skill, with program size as a control variable.

## 2. Previous Research

The state of the art in research on factors affecting program development has been discussed by Chrysler [15] and Jeffery and Lawrence [28,29,30]. Much of the research takes the form of field studies.

The research undertaken is meagre. Frequently, the studies cited have evaluated numerous factors across diverse programming environments (see, for example, [23,41,60]). There are three major problems with this type of approach. First, the study of numerous independent variables means many of them will frequently be correlated [15]. Correlation among variables complicates both the statistical analysis and the interpretation of the results. A more effective approach would be to factor analyze the variables under consideration to determine the orthogonal factors underlying them, and to use those factors in further analysis. Alternatively, global variables could be used. This would obviate the necessity for factor analysis.

Second, field studies do not lend themselves to control of extraneous variables [6]. Rather, the approach is to collect a large volume of data and assume that other variables not under study will be randomly distributed across the ranges of variables under investigation, so that there will be no biases or confoundings in the results. Any variables that are not randomly distributed should be included as variables for investigation in the study.

As an example of bias or confounding, the New York Time Project is reported as achieving high productivity rates due to the use of the chief programmer team approach $[4,5]$ . However, the project also used structured programming. The point is that it is not possible to attribute the high productivity rates achieved to either of these factors, as both changed at the same time, i.e., there was no control study that used structured programming but not the chief programmer team approach or vice versa. Moreover, the use of a development support library or a superprogrammer may also have contributed to the reported results. As a further example, Walston and Felix $[60]$ report that their data base contained data on 60 projects, ranging in size from 4000 to 467000 source lines of code, which took from 12 to 11758 man months to develop, in 28 different high-level languages, on 66 different computers. The data included a wide range of applications, personnel, and experience. In this study, the data base may not have been sufficiently large to justify the assumption that the myriads of variables were distributed randomly across all projects.

A third problem with much of the early research conducted into factors affecting program development is that there was no empirical testing of the models proposed either within the same organization or across organizations. Hence, the generality of the proposed models was suspect. Interestingly, most authors recognized the limitation of their models when they recommended that organizations keep their own data banks to analyze their own unique in-house environment so they could estimate programming effort, costs, and productivity at some time in the future $[15,28]$ . More recently, however, Lawrence and Jeffery $[34]$ and Jeffery and Lawrence $[30]$ have conducted both cross-sectional and longitudinal studies.

Many of the variables assessed for their effects on development effort and/or productivity fall into two categories: those that attempt to measure program size or program complexity, and those that attempt to measure programmer experience. $^{3}$ Some attention has also been paid to the impact of programming mode (i.e., batch or on-line environment), organizational factors, different programming languages, and different hardware configurations, on program development effort and/or productivity [30,49,60].

## 3. The Research Study

This study assessed the effects of a limited number of selected variables on development effort and productivity.

## 3.1. Variables

The variables tested were program size, programming style, and programmer skill. These variables were selected for the following reasons:

1. There is considerable support for their relevance in determining both development effort and productivity in previous research and literature, though the results are often inconsistent. (See [13,50,59]).

2. The variables are global in nature; examination of a number of detailed variables introduces uncertainty about the existence and direction of effects. Subsequently, if the global factors investigated in this study are found to be significant, further research can investigate the important determinants of these factors.

3. The variables chosen are likely to be orthogonal (i.e., they are unlikely to be correlated with each other) so that the effect of each can be assessed unambiguously with regard to the others [58].

## 3.1.1. Effect of Program Size

Recently, there has been considerable interest in the relationship between development effort and program size, measured as lines of code. Jeffery and Lawrence [28] proposed that the relationship is linear, based on results obtained on 103 programs ranging in size from 100 to 4500 lines of code across 3 organizations. Walston and Felix [60] and Basili et al. [6] have observed almost linear relationships for larger scale projects. The latter authors conclude (p. 56) that “(w)hether the relationship between effort and lines of code is modeled by a linear equation … or an exponential equation …, it is closer to linear than one might expect”.

Few studies report effects of program size on productivity. Jeffery and Lawrence, however, observe a positive relationship of size to productivity in two studies, i.e., longer programs are written with higher productivity than shorter programs [28,30].

Table 1
Propositions Tested in this Study

H1(a): Shorter programs are developed more quickly than longer programs;

H1(b): Longer programs show higher rates of productivity than shorter programs;

H2(a): Structured programs require less time for development than unstructured programs;

H2(b): Structured programs show higher rates of productivity than unstructured programs;

H3(a): Less skilled programmers take longer to develop programs than highly skilled programmers;

H3(b): Less skilled programmers have lower productivity rates than more skilled programmers.

## 3.1.2. Effect of Programming Style

The basis for structured programming is rooted in the chunking concept of cognitive psychology $[22,38,55]$ and in the notion that complex matter is best handled by creating hierarchical subunits that are strongly cohesive and loosely coupled $[52]$ . Many claims of greatly increased productivity have been made by advocates of structured programming techniques. It is not unusual to read reports about an organization, for example, that was producing code at the rate of 2,000 lines per year but on changing to a “more structured approach … boosted productivity to 5,000 lines per year”, and another which expects to achieve “an average of 10,000 lines of tested code per programmer per year” $[19]$ . To date, however, quantitative figures on the success of these techniques come from projects where other variables were not controlled $[4,5,25,26]$ or the sources of the claims are not referenced. Vessey and Weber $[59]$ review the empirical studies published in the literature and conclude they provide weak support for the adoption of structured programming.

## 3.1.3. Effect of Programmer Skill

It is generally accepted that certain programmers are more proficient than others, culminating in the efforts of those who are purported to be superprogrammers $[62]$ . Previous studies have recognized that the programmer may be a factor in the determination of both program development effort and productivity and have introduced such variables as years of programming experience $[28]$ , months of experience programming with COBOL at the given installation, and even age $[15]$ , into their models. However, the results, at best, have been mixed, some finding experience to be a significant factor $[15,23,49]$ , others not $[28,60]$ . Moher and Schneider $[39]$ , on the basis of laboratory experiments, conclude that both aptitude and experience influence student programming performance, while experience alone is related to professional programming performance. Lawrence $[33]$ and Jeffery et al. $[30]$ observe that programmer experience has no effect on productivity after the first year.

It is contended here that the variable of importance is not programmer experience but the level of programmer skill. Clearly there is a learning curve associated with the effective and efficient accomplishment of a certain task (the acquisition of skills), but after some time (i.e., experience), the quality of the agent is determined not by time on the job but by a combination of innate ability and different types of learning experiences.

The assessment of programmer skill has been of concern throughout the history of information processing. Historically, interest focussed first on the development of programmer rating instruments, and then on factors that influence the programming process. The major outcome of the research into programmer assessment was the recognition that instruments frequently captured those variables that related to success in training courses but not those that related to performance on the job [36]. Despite this evidence of the complex nature of expert programming skill, researchers in computer science embarked on numerous studies that attempted to measure the effects of various programming factors on the ease of programming. Not surprisingly, the results of those studies were mixed [46,50]. Frequently, the variability among programmers was greater than between the levels of the experimental variables, suggesting yet again the need to control for some element of programmer skill.

## 3.2. Measures

The following metrics were used for the variables under examination:

## 3.2.1. Program Development Effort

The first dependent variable examined was program development effort (measured in hours). The time recorded included that to design, code, and unit test a particular program, but not the time involved in documentation or systems testing. (See for example [28,34]).

## 3.2.2. Productivity

The second dependent variable, productivity, was measured as the ratio of the number of PROCEDURE DIVISION lines of code in a program to program development effort as defined above. The DATA DIVISIONs of the COBOL programs were not included as they are generally copied from existing definitions. (See [3,15,28,30,33,60].)

## 3.2.3. Program Size

The number of PROCEDURE DIVISION lines of code was the measure of program size used in this study. This follows the approach taken by Jeffery et al. [28,30], Lawrence [33], and Lawrence and Jeffery [34].

## 3.2.4. Programming Style

For the purpose of this study, programs were classified as either structured or unstructured on the basis of how they were designed and the extent to which they used the GO TO statement. If a program was organized into functional units that were linked by means of PERFORM statements, and if the GO TO statements were used judiciously – for example, in order to jump to an EXIT paragraph – then the program would be designated as “structured”. Even if a program appeared to be modularized, non-judicious use of the GO TO statement as, for example, in creating backward jumps, or simply the existence of too many jump statements, resulted in the program being classified as unstructured [58].

## 3.2.5. Programmer Skill

Managers in the organizations participating in the program were asked to assess the skill levels of the programmers who developed and implemented the programs studied. Ranking was undertaken using a 7-point Likert scale. The managers were requested to assess the skill of the programmers rather than their experience. They indicated changes in skill over time by rating programmers at the date of individual program development. Programmer skill ratings were provided for organization A by a group of top managers, for organization B by the project leader in charge of the team concerned, and for organization C by the supervisors of the programmers involved. The programmer skill ratings obtained from the organizations then were collapsed to allocate programmers to two categories: less skilled and more highly skilled. $^{4}$ The two categories contained approximately equal numbers.

## 3.3. Model

Since the relationship between program size and programming effort is by now well-established, program size was used as a control variable to better assess the effects of programming style and programmer skill on effort. The same model was also used to test the effects of the variables on programming productivity.

## 4. Data analysis

In order to test the hypotheses, a field study was conducted in which data was collected from three business organizations. More than one organization was chosen so that the generality of the results could be assessed. Data on COBOL programs, only, was collected in order to simplify the research design. The total sample size was 353 programs: 103, 191, and 59 respectively from each of the three organizations (referred to hereafter as organizations A, B, and C).

Organization A was a large retail firm, while organizations B and C were large insurance firms. The programs sampled from organizations A and C were selected from the whole range of systems available. Those from organization B were all part of the same system; these were the only programs at that time recorded on a suitable effort tracking system. Unfortunately, the programs in organization B were all classified as structured so that hypothesis 2 could be tested for organizations A and C only. The data collected included the number of PROCEDURE DIVISION lines of code, the number of DATA DIVISION entries, the total number of lines of code, and the number of IF statements, as well as the effort required to complete the program. Tables 2(a), (b), and (c) present information on the characteristics of the programs developed by each organization.

Plots of development effort by the number of logic tests and the number of different types of lines of code for each firm showed high variability. Two facts lead to significant variations from the “norm”:

1. Some development efforts appeared to be in-ordinately long, no matter what program characteristics they were measured against.

2. At the other end of the scale, some programs were completed with high productivity rates, e.g., organization A's highest rate was 86 PROCEDURE DIVISION lines of code per hour, that of organization B was 98, while organization C achieved a maximum of 51. These seemingly superhuman efforts are due to the fact that these programs are largely copied from other similar programs. In the words of one programmer, “nothing is new anymore”.

These observations may be regarded as outliers. Outliers may be caused by inaccurate recording,

PROCEDURE DIVISION lines of code for the Programs Studied

<table><tr><td rowspan="2"></td><td colspan="2">Programmer</td></tr><tr><td>Expert</td><td>Novice</td></tr><tr><td colspan="3">ORGANIZATION A</td></tr><tr><td>Modular</td><td>573.115(553.476)</td><td>667.143(575.488)</td></tr><tr><td>Structured</td><td>484.000(368.341)</td><td>545.333(505.968)</td></tr><tr><td colspan="3">ORGANIZATION B</td></tr><tr><td>Structured</td><td>142.545(161.977)</td><td>187.078(214.746)</td></tr><tr><td colspan="3">ORGANIZATION C</td></tr><tr><td>Modular</td><td>181.875(120.726)</td><td>283.333(170.509)</td></tr><tr><td>Structured</td><td>141.444(92.079)</td><td>165.619(111.310)</td></tr></table>

The first figure in each entry is the mean and the second the standard of the mean.

Programming Effort (hours) for the Programs Studied

<table><tr><td rowspan="2"></td><td colspan="2">Programmer</td></tr><tr><td>Expert</td><td>Novice</td></tr><tr><td colspan="3">ORGANIZATION A</td></tr><tr><td>Modular</td><td>44.031(29.027)</td><td>54.786(46.175)</td></tr><tr><td>Structured</td><td>56.679(39.259)</td><td>38.578(28.162)</td></tr><tr><td colspan="3">ORGANIZATION B</td></tr><tr><td>Structured</td><td>2.804(3.739)</td><td>2.911(3.871)</td></tr><tr><td colspan="3">ORGANIZATION C</td></tr><tr><td>Modular</td><td>85.938(84.691)</td><td>59.500(63.574)</td></tr><tr><td>Structured</td><td>55.792(43.545)</td><td>37.274(38.159)</td></tr></table>

Table 2(c)  
Programming Productivity for the Programs studied

<table><tr><td rowspan="2"></td><td colspan="2">Programmer</td></tr><tr><td>Expert</td><td>Novice</td></tr><tr><td colspan="3">ORGANIZATION A</td></tr><tr><td>Modular</td><td>15.252(13.586)</td><td>14.473(11.379)</td></tr><tr><td>Structured</td><td>9.970(6.198)</td><td>18.185(25.726)</td></tr><tr><td colspan="3">ORGANIZATION B</td></tr><tr><td>Structured</td><td>88.680(98.140)</td><td>115.456(110.947)</td></tr><tr><td colspan="3">ORGANIZATION C</td></tr><tr><td>Modular</td><td>5.623(7.837)</td><td>10.555(13.786)</td></tr><tr><td>Structured</td><td>4.145(4.437)</td><td>5.507(3.193)</td></tr></table>

misspecification of the model, or rare deviations from expectation [2]. During data collection, all recording was double-checked, though no check could be made on the initial data capture. For the very short development efforts, the model is incomplete; it should include a term to reflect the proportion of a program actually developed during the associated development period. Therefore, in the absence of a consistent explanation for the first observation and since the data required to incorporate the second into the model was not readily obtainable, the full data set was used in the analysis [2].

An analysis of covariance model (ANCOVA) [42] was used to test the six hypotheses. The dependent variables were development effort and productivity; the covariate was program size (the number of PROCEDURE DIVISION lines of code); and there were two factors: programming style measured at two levels, and programmer skill measured at two levels. The results for development effort are presented first followed by those for productivity. A similar procedure was followed in both cases.

## 4.1. Development Effort

Since the numbers of observations for each treatment of the factorial design were unequal (nonorthogonal factorial design), there could be no unique decomposition of the total sum of squares. The covariate was estimated first, followed by the main factor effects; the interaction effects were estimated after adjustment for the covariate and the main effects [42]. To meet the requirements of the ANCOVA model, the dependent variable was transformed using the formula $\log_{10}X$ . Further, 13 programs written by one programmer in organization B were dropped from the sample (i.e., they were outliers) before the assumptions underlying the model were met.

Table 3 shows the results of the ANCOVA model using the logarithm of development effort for the three organizations. The ANCOVA results show that the covariate – program size – is significant in all organizations at the 0.001 level; the relationship between effort and size is positive; thus, there is support for hypothesis 1(a). The only significant factor resulting from the analysis is programmer skill in organization C (p < 0.05). Less skilled programmers took longer to develop programs than more skilled programmers. Hence, hypothesis 3(a) is supported in only one organization from three. This model accounted for 30.5, 33.1, and 25.3 percent of the variation in program development effort for organizations A, B, and C respectively.

## 4.2. Productivity

The analysis for the dependent variable, productivity, followed the same procedure as that for development effort. Again, the dependent variable was transformed logarithmically to test the ANCOVA model. Organization B's data was analyzed throughout using the reduced sample of 178 programs.

Analysis of Covariance for Logarithm of Program Development Effort

<table><tr><td rowspan="2">SOURCE OF VARIATION</td><td colspan="3">p</td></tr><tr><td>ORG. A</td><td>ORG. B</td><td>ORG. C</td></tr><tr><td>COVARIATEPROCEDURE DIVISIONlines of code</td><td>0.000</td><td>0.000</td><td>0.001</td></tr><tr><td>MAIN EFFECTSProgramming Style</td><td>0.626</td><td>-</td><td>0.841</td></tr><tr><td>Programmer Skill</td><td>0.407</td><td>0.114</td><td>0.017</td></tr><tr><td>2-WAY INTERACTIONStyle Skill</td><td>0.164</td><td>-</td><td>0.444</td></tr><tr><td>EXPLAINED</td><td>0.000</td><td>0.000</td><td>0.002</td></tr><tr><td> $R^2$ </td><td>0.305</td><td>0.331</td><td>0.253</td></tr></table>

Analysis of Covariance for Logarithm of Productivity

<table><tr><td rowspan="2">SOURCE OF VARIATION</td><td colspan="3">p</td></tr><tr><td>ORG. A</td><td>ORG. B</td><td>ORG. C</td></tr><tr><td>COVARIATEPROCEDURE DIVISIONlines of code</td><td>0.000</td><td>0.051</td><td>0.009</td></tr><tr><td>MAIN EFFECTSProgramming Style</td><td>0.331</td><td>-</td><td>0.962</td></tr><tr><td>Programmer Skill</td><td>0.595</td><td>0.004</td><td>0.023</td></tr><tr><td>2-WAY INTERACTIONStyle Skill</td><td>0.289</td><td>-</td><td>0.513</td></tr><tr><td>EXPLAINED</td><td>0.000</td><td>0.003</td><td>0.017</td></tr><tr><td> $R^2$ </td><td>0.240</td><td>0.066</td><td>0.190</td></tr></table>

The results of the ANCOVA model are shown in Table 4. The covariate, program size, is highly significant in organizations A and C (p < 0.01), while it borders on significance in organization B (p = 0.051); the relationship between productivity and size is positive; hence, hypothesis 1(b) is supported. Programmer skill is significant in both organizations B and C. In both organizations, more skilled programmers exhibited higher rates of productivity than lower skilled programmers. Hence, hypothesis 3(b) is supported in 2 of the 3 organizations studied. The model accounted for 24.0, 6.6, and 19.0 percent of the variation in productivity for organizations A, B, and C, respectively.

## 5. Discussion

The model used in this study accounts for between 25 and 33 percent of the observed variation in program development effort, and between 7 and 24 percent of the variation in programming productivity. That the full sample set – with the exception of the programs written by one programmer – was used in the analysis should be kept in mind when assessing the results.

## 5.1. Program Size

Clearly, the principal determinant of both program development effort and productivity in this study is the number of PROCEDURE DIVISION lines of code. The result is highly significant for development effort in all three organizations and only slightly less significant for productivity.

Let us examine, further, the result for development effort. The use of the variable program size does not contribute to our knowledge of the programming process (it was, in fact, used in this study as a control variable). It merely tells us there is an ex post relationship between the size of the program produced and the length of time taken to produce it. It says nothing about the nature of the task performed by the programmer, since program size may be the same for tasks of differing complexity. As an example, suppose two programmers each wrote programs to accomplish the same task; if the two programs were of different size, we would not be surprised if the longer one required more effort to write. However, the difference in effort, masquerading as a difference in size, masks the programmer skill effect.

Nor would the use of presently available complexity measures, such as those developed by Halstead [24] and McCabe [37] resolve the problem. These methods generally do not include an objective assessment of the complexity of the task before programming commences. They are, in any case, quite highly correlated with program size (see, for example, [17]). Further, Halstead's metrics do not appear to be effective in structured environments [18].

There are two further problems associated with metrics of this nature. First, though based on elementary syntactic structures, Halstead's metrics also rely on the use of Miller's magical number 7 [38] and Stroud's 18 discriminations per second [55]. These parameters were developed using simple tasks in artificial environments and hence may not apply to complex cognitive tasks such as programming [11,50]. Second, the complexity metrics are essentially predictive in nature and therefore do not provide any insight into the information processing of programmers. What we need to know are those factors that render tasks psychologically complex for programmers. Curtis [16] discusses various aspects of psychological complexity.

The result for productivity is in accord with the observations of Jeffery and Lawrence [28,30] that productivity increases as program size increases. It suggests that there are fixed overheads associated with program development that result in the lower productivity of shorter programs.

## 5.2. Structured Programming

In no organization did structured programming have an influence on the effort required to develop programs or on productivity. There may be several reasons for this result.

1. The time involved to code and debug structured programs may be less than the time required for unstructured programs, but the design phase may be more time consuming [3,25,26,33].

2. The important factor affecting development effort may not be structured programming per se but the particular type of modularity created by the design process used. This raises the question of what the unit of decomposition “should” be. (See [46].)

3. The benefits of structured programming may lie not in the development phase but in the modification and maintenance phases where better documentation and better program structure increase the comprehensibility of the programs to programmers who were not the authors.

4. Lawrence [33] suggests that programmers are so familiar with the tasks with which they are confronted that they retrieve an appropriate knowledge structure from long-term semantic memory and tailor it to suit their needs; it does not matter whether the template is structured or unstructured.

5. The programs tested may not have been sufficiently complex to reveal the positive effects of the use of structured programming. Brooks [14], in his reanalysis of the Walston-Felix data, suggests that there is a program complexity-programmer style interaction. He found productivity gains of 200 to 600 percent when structured rather than unstructured programming was used for highly complex projects. This effect is not apparent for systems of the size and complexity tested in this study, but should be kept in mind for studies involving systems of increased complexity.

Two of these factors warrant consideration in further detail. They are the unit of decomposition and the retrieval of known solutions.

## 5.2.1. Unit of Decomposition

The type of decomposition used by all three organizations in this study was the Yourdon-Constantine approach [40,44,54,63]. This method is based on processes that transform data flows and produces a program design that foregrounds control flow. Sample data for other approaches to decomposition could not be obtained, so this study examined specifically the effect of producing unstructured code versus code derived by the structured design approach.

The major alternative to structured design is the data structure approach of Jackson [27] and Warnier-Orr [43,61]. The data structure approach first determines all the data structures, explicit or implicit, in the program being developed. Then, it specifies a processing structure for each data structure. Hence, it takes a completely opposite view of the design process to structured design. The data structure approach is similar in many respects to object-oriented design [10], a design methodology that parallels object-oriented programming. There appears to be a trend in the literature towards object-oriented programming. The best known of such programming language is, of course, Ada [1].

These alternative approaches to decomposition should be investigated to determine whether they have a positive influence on program development effort and/or productivity.

## 5.2.2. Retrieval of Known Solutions

Whether the structuring of programmers' retrieved knowledge has an effect on programmer efficiency is an interesting question. The inconsistent results of many programming factors studies have led researchers to conclude that individuals possess large and extremely diverse knowledge bases [12,13,46,50]; for example, Brooks [12] estimates that a programmer's knowledge base consists of 50,000–100,000 chunks. Hence, given that programmers retrieve stored knowledge structures, there is ample evidence to suggest that some of those knowledge structures may be more effective than others. The diffusion of structured techniques in the information systems community over the past decade or so suggests there are advantages associated with their use. Certainly, however, much more research needs to be conducted into the effectiveness of certain types of structuring and the situations in which they are applicable [46,59].

## 5.3. Programmer Skill

The results relating to programmer skill are somewhat mixed. First, programmer skill does not appear to affect development effort in organization A. Second, in organization B, a programmer effect of sorts existed in that the programs written by one particular programmer were dropped from the sample so the sample population characteristics met the requirements of the ANCOVA model. Once the data for this programmer was removed, no programmer skill effect was observed for development effort. There was, however, a programmer effect in the expected direction for effort in organization C. Programmer skill is related to productivity in 2 of the 3 organizations studied. More highly skilled programmers in organizations B and C exhibit increased rates of productivity compared with less skilled programmers.

There are several possible explanations for the lack of a consistent programmer skill effect.

1. Note that the skill ratings of managers in organization A did not result in any significant programmer effects; those of the project leader in organization B resulted in a significant effect for productivity; those of supervisors in organization C resulted in significant effects for both effort and productivity. These results suggest that managers may be too far removed from the work environment to differentiate the skills of their programmers. Vessey [57] found support for this notion.

2. Management assigns better programmers to harder programs; however, little evidence was found to support this possibility.

3. Management does not ask any more of highly skilled than less skilled programmers so that Parkinson's Law applies; i.e., "work expands to fill the time available". A related perspective is that (indirect) peer pressure reduced the performance of the more skilled programmers.

4. Management employs its better programmers as lead programmers so that the difference in quality of those programmers writing the programs is insufficient to reveal expected differences.

5. Another contributing factor may be that better programmers are more aware of the complexities involved and hence spend more time testing their programs than poorer programmers. Vessey and Weber [58] found some support for the latter suggestion; they reported almost no difference in observed error rates between moderately complex and highly complex programs $^{5}$ .

6. A metric is required that more accurately represents programmer skill. Previous mention has been made of the inconsistent results deriving from programming factors research. As a result of this research, several authors now believe that the diversity of programmers' processes or knowledge structures frequently result in larger within-group than between-group differences. Vessey [57] derived a measure of expertise in debugging programs that used the chunking process as the criterion for distinguishing between more and less skilled programmers.

## 6. Limitations of the Research

A possible limitation of this study is that it did not control for factors that may affect the program development process such as quality of the design specifications and the systems support available to programmers during development. Large organizations with well-developed information systems generally institute a set of internal standards to which designers must adhere. This approach limits the variation in specifications that might otherwise occur. Hence, in a study that analyses data on an organizational basis, this factor is not considered important. Similarly, the program development environment is common to all programs from one organization. The same tools and techniques are therefore available to all programmers. The only way in which such factors may bias the results is if a change in either occurs at the same time as a change in one of the factors under study. Program size would not change with either of these factors (since data was collected on COBOL programs only) and neither should programmer skill. Programming style could well change at the same time as programming standards and/or programming mode. One would expect, however, that the results then would be biased in favour of the new state. Since no positive effect of programming style was identified, it would seem that there is no benefit to any possible concurrent change in the two factors concerned.

This study, and other similar studies, did not directly assess the resultant program quality. From the viewpoint of program quality, program development can be considered as a production process; any process resulting in a physical product would be tested to ensure that the product met prespecified standards. Similar standards should be set for programming products. Hence, the extent to which the programs meet management's requirements of maintainability, robustness, clarity, performance, cost, portability, and useability, etc. [62], should be included in the model. However, there is as yet little formal use of program quality metrics. Perhaps the 11 quality characteristics, the associated 151 metrics cited by Boehm et al. [9], and the lack of a theory to relate them to meaningful independent variables is sufficient to deter practitioners from adopting them. This study (and all others), therefore, makes the implicit assumption that all programs satisfy management's requirements to the same degree! To the extent that this is not so, with a reasonable sample size and random selection of programs, there is no reason to suspect bias in the results.

## 7. Conclusion

In this paper we have briefly reviewed research on factors affecting the program development process with an emphasis on the methodological problems that have rendered their results questionable. We have also presented the results of our own study of factors affecting program development effort and productivity.

This study raises another major problem when investigating factors underlying the programming process, namely, how research in this area should be conducted. This paper presents the results of a field study, carried out by collecting data on program development efforts from operational environments. This method has the advantage of addressing “real world” occurrences; it has the disadvantages associated with poor, or inadequate record-keeping, or none at all, and the difficulty of ensuring that there is no bias in other variables not under investigation. Another approach is the laboratory experiment. Its principal advantage lies in control over variables not under investigation that may otherwise influence the results. On the other hand, the artificial situation created may render the application of any findings to a practical environment suspect. This problem must be resolved if we are to test empirically the claims that are being made about an ever increasing number of programming tools and techniques.

## References

[1] Ada: “Requirements for High Order Programming Languages, IRONMAN”, Department of Defense, January 14, 1977.

[2] Anscombe, F.J., "Outliers", in D.L. Stills, ed., International Encyclopedia of the Social Sciences, Vol. 15, The Macmillan Company and the Free Press, 1968, pp. 178–182.

[3] Bailey, J.W. and Basili, V.R., "A Meta-Model for Software Resource Expenditures", Proc. 5th Int. Conf. on Software Eng., 1981.

[4] Baker, F.T., “Chief Programmer Team Management of Production Programming”, IBM Systems Journal, 11 (1), pp. 56–73, 1972.

[5] Baker, F.T. and Mills, H.D., “Chief Programmer Teams”, Datamation, December 1973, pp. 58–61.

[6] Basili, V.R. and Freburger, K., “Programming Measurement and Estimation in the Software Engineering Laboratory”, J. of Systs. and Software, 2, pp. 47–57, 1981.

[7] Benbasat, I. and Vessey, I., “Programmer and Analyst Time/Cost Estimation”, MIS Quarterly, Vol. 4, No. 2, pp. 31–43, 1980.

[8] Boehm, B.W., Software Engineering Economics, Prentice-Hall, Inc., Englewood Cliffs, N.J., 1981.

[9] Boehm, B.W., Brown, J.R., Kaspar, H., Lipow, M., Macleod, G.J., and Merit, M.J., Characteristics of Software Quality, North-Holland, Amsterdam, 1978.

[10] Booch, G., Software Engineering with Ada, The Benjamin/Cummings Publishing Company, Inc., Reading, Mass., 1983.

[11] Broadbent, D.E., “The Magic Number Seven after Fifteen Years”, in A. Kennedy and A. Wilkes (eds.), Studies in Long Term Memory, New York: Wiley, 1975.

[12] Brooks, R.E., “Towards a Theory of the Cognitive Processes in Computer Programming”, Int. J. Man-Machine Studies, 9, pp. 737–751, 1977.

[13] Brooks, R.E., “Studying Programmer Behavior Experimentally: The Problems of Proper Methodology”, Comms. of the ACM, 23, pp. 207–213, 1980.

[14] Brooks, W.D., "Software Technology Payoff: Some Statistical Evidence", Journal of Systems and Software, 2, pp. 3-9, 1981.

[15] Chrysler, E., “Some Basic Determinants of Computer Programming Productivity”, Comms. of the ACM, Vol. 21, 1978, pp. 472–483.

[16] Curtis, B., "In Search of Software Complexity", Procs. of the Workshop on Quantitative Software Models for Reliability, Complexity and Cost, IEEE, New York, 1980.

[17] Curtis, B., Sheppard, S.B., and Milliman, P., "Third Time

Charm: Stronger Prediction of Programmer Performance by Software Complexity Metrics". In Proceedings of the Fourth International Conference on Software Engineering, IEEE, New York, pp. 356–360.

[18] Curtis, B., Sheppard, S.B., Milliman, P., Borst, M.A., and Love, T., “Measuring the Psychological Complexity of Software Maintenance Tasks with the Halstead and McCabe Metrics”, IEEE Trans. on Software Eng., SE-5 (2), pp. 96–104, 1979.

[19] Davis, G.B., Computers and Information Processing, McGraw-Hill Inc., N.Y. 1978.

[20] Davis, J.S.; "An Investigation of Chunk Based Complexity Measures", Working Paper, Army Institute for Research in Management Information and Computer Science, Georgia Institute of Technology, 1984.

[21] Farquhar, J.A., “A Preliminary Inquiry into the Software Estimation Process”, RM-6272-PR, The Rand Corp, Santa Monica, CA, 1970.

[22] Frost, D., “Psychology and Program Design”, Datamation, 21 (May), pp. 137–138, 1975.

[23] Gayle, J.B., “Multiple Regression Techniques for Estimating Computer Programming Costs”, Journal of Systems Management, February 1971, pp. 13–16.

[24] Halstead, M.H., Elements of Software Science, New York-Elsevier, 1977.

[25] Holton, J.B., “Are the New Programming Techniques Being Used?”, Datamation, July 1977, pp. 97–103.

[26] Hugo, I. St. J., “A Survey of Structured Programming Practice”, AFIPS Conference Proceedings, 1977, pp. 741–752.

[27] Jackson, M., Principles of Program Design, Academic Press, New York, 1975.

[28] Jeffery, D.R. and Lawrence, M.J., "An Interorganizational Comparison of Programming Productivity", Proc. 4th International Conference on Software Engineering, Munich, ACM and IEEE (1979), pp. 369–377.

[29] Jeffery, D.R. and Lawrence, M.J., “Some Issues in the Measurement and Control of Programming Productivity”, Information and Management, 4, 1981, pp. 169–176.

[30] Jeffery, D.R. and Lawrence, M.J., “Managing Programming Productivity”, J. of Systems and Software, 5, pp. 49–58, 1985.

[31] Jeffery, D.R. and Vessey, I., “Models, Metrics and Management of Information System Development”, Information and Management, 3, (1980), pp. 89–93.

[32] Jeffries, R., Turner, A.A., Polson, P.G., and Atwood, M.E., “The Processes Involved in Designing Software”. In J.R. Anderson (ed.), Cognitive Skills and Their Acquisition, Erlbaum Assocs., Hillsdate, N.J., 1980.

[33] Lawrence, M.J., “Programming Methodology, Organizational Environment, and Programming Productivity”, Journal of Systems and Software, 2, pp. 257–269, 1981.

[34] Lawrence, M.J. and Jeffery, D.R., “Commercial Programming Productivity – An Empirical Look at Intuition”, The Australian Computer Journal, 15, (1983), pp. 28–32.

[35] Malhotra, A., Thomas, J.C., Carroll, J.M., and Miller, L.A., “Cognitive Processes in Design”, Inter. J. of Man-Machine Studies, 12, pp. 119–140, 1980.

[36] Mayer, D.B. and Stalnaker, A.W., “Selection and Evaluation of Computer Personnel – the Research History of SIG/CPR”, Proceedings of the 23rd ACM National Conference, 1968, 657–670.

[37] McCabe, T.J., "A Complexity Measure", IEEE Transactions on Software Engineering, Vol. SE-2, 4 (Dec. 1976), pp. 308–320.

[38] Miller, G.A., “The Magical Number Seven Plus or Minus Two: Some Limits on Our Capacity for Processing Information, Psychol. Rev., 63, pp. 81–97, 1956,

[39] Moher, T. and Schneider, G.M., "Methods for Improving Controlled Experimentation in Software Engineering", International Conference on Software Engineering, IEEE, 1981, pp. 224–233.

[40] Myers, G.J., Composite/Structured Design, Van Nostrand Reinhold, New York, 1978.

[41] Nelson, E.A., Management Handbook for the Estimation of Computer Programming Costs, System Development Corp., Santa Monica, Calif., March 1967.

[42] Neter, J. and Wasserman, W., Applied Linear Statistical Models, Irwin, Homewood, Ill., 1974.

[43] Orr, K.T., Structured Systems Development, Yourdon Press, New York, 1977.

[44] Page-Jones, M., The Practical Guide to Structured Systems Design, Yourdon Press, New York, 1980.

[45] Parr, F.N., "An Alternative to the Rayleigh Curve Model for Software Development Effort", IEEE Trans. on Software Eng., SE-6 (3), pp. 291–296, 1980.

[46] Pennington, N., “Cognitive Components of Expertise in Computer Programming: A Review of the Literature”, Technical Report No. 46, University of Michigan, 1982.

[47] Putnam, L.H., “A General Empirical Solution to the Macro Software Sizing and Estimating Problem”, IEEE Transactions on Software Engineering, Vol. SE-4, 4 (July 1978), pp. 345–361.

[48] Putnam, L.H., “SLIM System Description”, Quantitative Software Management, Inc., McLean, VA, 1980.

[49] Sackman, H., Erikson, W.J., and Grant, E.E., “Exploratory Experimental Studies Comparing Online and Offline Programming Performance”, Communications of the ACM, Vol. 11, No. 1 (Jan. 1968), pp. 3–11.

[50] Sheil, B.A., “The Psychological Study of Programming”, Comput. Surveys, 13 (Mar.), pp. 101–120, 1981.

[51] Shneiderman, B., Software Psychology: Human Factors in Computer and Information Systems, Winthrop, Cambridge, Mass., 1980.

[52] Simon, H.A., “The Architecture of Complexity”, Proc. Amer. Philosoph. Soc., 106 (Dec.), pp. 467–482, 1962.

[53] Simon, H.A., “How Big is a Chunk?”. In Models of Thought, Chap. 2.2, 1979.

[54] Stevens, W.P., Using Structured Design, John Wiley & Sons, New York, 1981.

[55] Stroud, J.M., “The Fine Structure of Psychological Time”, Annals of the New York Academy of Sciences, pp. 623–631, 1966.

[56] Tracz, W.J., “Computer Programming and the Human Thought Process”, Software-Practice and Experience, 9, pp. 127–137, 1979.

[57] Vessey, I., “The Psychological Processes Underlying the Debugging of Computer Programs”, Unpublished Doctoral Dissertation, University of Queensland, 1984.

[58] Vessey, I. and Weber, R.A., “Some Factors Affecting Program Repair Maintenance: An Empirical Study”, Communications of the ACM, Vol. 26, No. 2, Feb. 1983, pp. 128–134.

[59] Vessey, I. and Weber, R.A., “Research on Structured Programming: An Empiricist’s Evaluation”, IEEE Trans. on Software Eng., SE-10 (4), pp. 397–407, 1984.

[60] Walston, C.E. and Felix, C.P., "A Method of Programming Measurement and Estimation", IBM Systems Journal, 16, 1977, pp. 54–73.

[61] Warnier, J.D., Logical Construction of Programs (L.C.P.), H.E. Stenfert Kroese B.V., Leiden, 1974.

[62] Wulf, W.A., “Programming Methodology”, Proceedings of a Symposium on the High Cost of Software, J. Goldberg (ed.), Stanford Research Institute, Sept., 1973.

[63] Yourdon, E. and Constantine, L.L., Structured Design, Prentice-Hall, Inc., Englewood Cliffs, N.J., 1979.
