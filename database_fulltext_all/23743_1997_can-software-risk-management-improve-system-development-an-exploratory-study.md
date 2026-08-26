---
otero_id: 23743
otero_key: "K3NAJK3C"
title: "Can software risk management improve system development: an exploratory study"
authors: "J Ropponen; K Lyytinen"
year: "1997"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000253"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Can software risk management improve system development: an exploratory study

J Ropponen<sup>1</sup> and K Lyytinen<sup>2,3</sup>

<sup>1</sup>Nokia Telecommunications Ltd, Network Management Systems, Hatanpa¨a¨nkatu 3, PO Box 759, 33101 Tampere, Finland; <sup>2</sup>University of Jyva¨skyla¨ , Department of Computer Science and Information Systems, Seminaarinkatu 15, P.O. Box 35, 40351 Jyva¨ skyla¨, Finland; and <sup>3</sup>Georgia State University, GA, USA

Software risk management can be defined as an attempt to formalise risk oriented correlates of development success into a readily applicable set of principles and practices. Earlier research suggests that it can reduce the likelihood of a system failure. Using a survey instrument we investigate this claim further. The investigation addresses the following questions: (1) which characteristics of risk management practices; and (2) which other environmental and process factors (such as development methods, manager’s experience) relate to improved performance in managing software risks? Our findings support in general the claim that the use of risk management methods improves system development performance. Yet, little support was found for the claim that specific risk management methods are instrumental in attacking specific software risks. Overall, risks are better managed with combined measures of having experienced project managers, selecting a correct project size, and investing in and obtaining experience in risk management deliberations.

## Introduction

It costs too much, is always late and comes incomplete.

The literature on software development is replete with similar statements from the seventies (Brooks, 1974), the eighties (Lyytinen, 1987; Lyytinen & Hirschheim, 1987), and more recent times (Barki et al, 1993). Software development seems to be chronically suffering from difficulties of cost overruns, project delays, unmet user needs and unused systems. This also continues despite huge advances in development techniques, tools and software technologies. Since the early eighties (McFarlan, 1982; Boehm, 1989) these difficulties have been addressed more rigorously through software risk management.

Software risk management can be defined as an attempt to formalise risk oriented correlates of development success into a readily applicable set of principles and practices (Boehm, 1991). It embraces techniques and guidelines to identify, analyse and tackle software risks items. A risk item denotes a particular aspect or property of a development task, process or environment, which, if ignored, will increase the likelihood of a project failure, e.g. threats to successful software operation, major sources of software rework, implementation difficulty or delay (Lyytinen et al, 1996b, pp 5–6). Overall, software risk management has raised considerable hopes for improving system development (Alter & Ginzberg,

1978; Boehm, 1989, 1991; Boehm & Ross, 1989; Charette, 1989; Mathiassen et al, 1995).

Even though guidelines suggested by proponents of software risk management have been followed increasingly by practitioners and researchers alike, our knowledge of software risk management and its impacts has been sparse and anecdotal. In this paper our goal is to improve the knowledge in this area by investigating whether the software risk management as currently practised can, indeed, improve system development. In doing so we draw upon Boehm’s (1989, 1991) studies on software risk items and risk management methods. We seek answers to the following questions: (1) what risk management practices; and (2) other environmental and process factors (such as development methods, manager’s experience) affect project managers’ performance in managing software risks.

The paper is organized as follows. First, we discuss related research and formulate our research problem and explain the research method. Next, we examine how risk management practices correlate with improved performance in handling software risks. We continue by analysing how risk management performance is influenced by environmental contingencies. We conclude by discussing conditions for the success of software risk management.

## Research problem and method

## Research problem

The effect of software risk management has not been intensively researched. Instead, the majority of risk management studies have dealt with normative techniques of effective risk management (McFarlan, 1982; Boehm, 1989, 1991; Boehm & Ross, 1989; Charette, 1989), but available empirical evidence of their effectiveness is sparse. Available empirical studies have mostly classified and ranked software risk items (Boehm, 1989; Bark et al, 1993; Ropponen & Lyytinen, 1996). These studies are useful in obtaining reliable figures of common software risks and considering them along various dimensions. Empirical studies that seek to understand how one can manage software risks more effectively are few.

A few studies discuss real life cases in which risk management principles were (or were not) followed and try to learn of their use (or non-use). These studies have been either single site case studies (Boehm & Ross, 1989; Markus & Keil, 1994; Neo & Kwong, 1994), or multiple site case studies (Willcocks & Margetts, 1994). From these studies it is difficult to deduce to what extent the risk management deliberations were purposefully crafted and what their true impacts were. A few published studies have gone further and sought to establish systematic impact models of risk management. They have all come to a conclusion that risk management efforts reduce the exposure to software risks, increase software quality and improve the quality of the systems development process (Boehm, 1989; Charette, 1989; van Genuchten, 1991; van Swede & van Vliet, 1994; Mathiassen et al, 1995). These studies have been either small scale laboratory experiments with student subjects, their sample size was small, or their methodological rigor was questionable in measuring risk management improvement.

Some studies have focused on specific aspects of the development process such as project delays (van Genuchten, 1991), or dealt only indirectly with risk management issues (van Swede & van Vliet, 1994). Overall the causal connection between the use of risk management methods and the development improvement has remained unsubstantiated, and more research is needed to establish this relationship.

## Research model and method of inquiry

We investigate in this study the impact of software risk management practices on the system development process. The study is exploratory in nature and focuses on ‘hypotheses generation’ rather than ‘hypotheses testing’. It is hoped that recognised interactions can be extended in future studies to systematic theory development and more rigorous testing.

In more specific terms we shall examine the following questions: (1) Does risk management improve developers’ performance in handling software risks?; and (2) What other factors in the development process and environment correlate significantly with improved risk management performance? Figure 1 summarises the postulated interactions between the model components (as depicted by the arrows), and the classes of variables covered.

![](/api/attachments/K3NAJK3C/fulltext/images/dcb75e25946fa50f9c8061f47c18469d0816b9c2810ea23bc450eb9a8f988fc0.jpg)  
Figure 1 The research model.

We examined the postulated interactions in our research model by using a survey instrument<sup>1</sup> where experienced project managers provided data on their system development performance. This research method was selected because we did not have access to project level performance data, and such data is extremely difficult or costly to obtain. Due to the exploratory nature of our study we identified major model components and their interactions before proceeding to the detailed theory development and confirmatory hypothesis testing. Therefore only causal positive impacts were seached for. The components of the research model, their selection, and their operationalisation in the questionnaire are discussed next.

## Model components and their operationalisation

## Performance in managing software risk

Risks were above defined as particular aspects or properties of a development task, process or environment, which, if ignored, will increase the likelihood of a project failure. This suggests a pragmatic way to evaluate the influence of risk management practices on software development. As the measurement of a development success is rife with both conceptual and instrumental problems (Haga & Zviran, 1994) we sought to measure the success of managing typical risk items that normally represent general major pitfalls in software development. For this purpose we selected the top-ten risk list provided by Boehm (1989).

Boehm’s list looked appropriate because it has been compiled by probing a large number of software projects and their common risk items. Moreover, it is quite extensive in terms of possible sources of risks (Lyytinen et al, 1996b) and reflects faithfully a project managers’ perspective on software risks by addressing critical concerns and objectives of different stakeholders (see Appendix 1). This list is also the most well-known and has been widely applied in practice to orchestrate risk management plans with some success (Boehm & Ross,

1989; Boehm, 1991). Despite its limitations,<sup>2</sup> it reflects adequately the focus of our study.

Using Boehm’s top-ten list we derived a number of statements which represent claims how well these risks are being managed. We extended this list with some new risk considerations such as project cancellation, and the uneven distribution of work (due to the ‘deadline effect’). Then we operationalised these claims into 20 Likert scale items that formed the performance assessment part of our questionnaire<sup>3</sup> (see Appendix 2).

## Risk management methods and their use

Exploring the use of the methods was deemed necessary in finding out whether software risk management has an impact on the performance of managing risks; and if it has, what these impacts are. Investigating the use of risk management methods we utilised Boehm’s (1989) classification. <sup>4</sup> In addition, we inquired about respondents’ commitment to risk management in general. We also asked how long and extensively risk management methods had been used, whether the use was voluntary, and what were the experiences of using methods. These were included because we assumed that organizations with wider experience and use figures will learn to apply risk management methods more effectively because they can share experiences, improve practices and create culture that fosters risk awareness and frames development issues in risk oriented terms. We also investigated resources used for managing risks, assuming that an allocation of sufficient resources is a good indicator of a true management commitment.

## Environmental contingencies

Based on earlier studies we postulated that the capability to handle risks is also contingent upon a number of external factors including (see also Boehm & Ross, 1989; Lyytinen et al, 1996a): (1) environmental factors; (2) technology factors; and (3) individual characteristics. Environmental factors cover items like organizational size, industry, the size of the software organization, type of system being developed (business systems/embedded systems) as well as contractual arrangements (Beath, 1983, 1987).

We assume that technological factors such as newness of technology, the complexity and the novelty of the required technological solutions (McFarlan, 1982; Charette, 1989; Willcocks & Margetts, 1994) can relate to risk management performance (Boehm, 1989; Charette, 1989; Willcocks & Margetts, 1994). We measured these with such items as selection of hardware architecture, the type of application (batch/interactive), the novelty of the programming environment, and the use of original and complex technologies (data communications, multimedia, or knowledge engineering). We also assumed that process technologies like development tools and methods affect ability to manage risks (see Humphrey,

1989; van de Swede & van Vliet, 1994). We therefore measured their use and organizational status (voluntary/obligatory) of design and analysis methods, the CASE tools, and project management tools.

Project managers’ individual characteristics, personal skills and experiences (projects with different size and complexity), can be one of the most important predictors of success in managing risks (Kerzner, 1987; van de Swede & van Vliet, 1994). Similarly software developers’ education, both in computing, in general, and in the project and risk management may, in particular, affect the capability to deal with software risks.

## Analysis of the research data

We obtained the data for our study by mailing the questionnaire to 248 randomly selected members of the Finnish Information Processing Association (1991) whose affiliation was project manager, or similar. The final sample consisted of 83 project managers (response rate = 33.5%). The earlier literature suggests that project managers’ responsibilities include risk management tasks such as keeping the project on time and within budget (Boehm, 1989), and therefore we purposefully selected project managers as research subjects. The response rate was satisfactory and above average.

We applied ANOVA<sup>5</sup> to examine the influence of risk management practices and environmental contingencies on risk management performance. The basic requirements of using variance analysis (Cody & Smith, 1987) – the independence of test groups, the homogeneity of variances ( = 0.01), and normal distributions – were all tested and were met with the data. In most tests (if not otherwise described) we used a conservative statistical significance level of  = 0.01. The steps to assess the validity and reliability of the data set and the likelihood of sampling bias are explained in Appendix 3.

## The impact of risk management practices

Our study showed that a large portion of project managers studied were engaged in some type of risk management activity. Yet, risk concepts were understood and utilised only by 25% of respondents. This is in line with earlier claims that project managers do not know the terms ‘risk identification’ and ‘risk assessment’ despite what they actually do (Boehm, 1989). Overall, the respondents believed that risk management methods had a positive impact both on the development process and its outcomes (for details see Ropponen, 1996).

The prominent interactions between risk management performance and risk management practices were resolved using one-way ANOVA. We found four risk management aspects that significantly influence risk management performance. These are illustrated in Table 1 and they are: (1) the number of projects where risk management methods have been applied; (2) resource demands in using risk management methods; (3) using decomposition analysis of poorly defined project parts; and (4) using the analysis of key decisions. The risk items affected are: failures in size estimations, failures in correct resource allocation, failures in handling the project complexity, failures in monitoring requirements changes, and failures in specifying satisfactory user interfaces.

Table 1 The impact of risk management methods on risk management

<table><tr><td>Performance in managing the risk item</td><td>Risk management aspect</td><td>F</td><td>P</td><td>N</td><td> $R^2$ %</td></tr><tr><td>Wrong size estimates</td><td>The number of projects where risk management methods have been applied</td><td>12.38</td><td>0.0005</td><td>20</td><td>59</td></tr><tr><td>Steady consumption of time</td><td>Resources spent on the risk management method</td><td>11.85</td><td>0.0031</td><td>19</td><td>41</td></tr><tr><td>Complexity easy to handle</td><td>Resources spent on the risk management method</td><td>8.35</td><td>0.0102</td><td>19</td><td>33</td></tr><tr><td>Requirements changes</td><td>Decomposition analysis of poorly defined project parts</td><td>6.83</td><td>0.0019</td><td>81</td><td>15</td></tr><tr><td>Satisfaction with the user interface</td><td>The analysis of key decisions</td><td>16.23</td><td>0.0001</td><td>77</td><td>18</td></tr></table>

The results suggest that two features of risk management are highly related to improved performance in managing software risk. These are: cumulated experience in using methods, and the amount of resources spent. The study also reveals that the longer experience in using risk management methods, the better the project manager’s performance in estimating the project size, and decreasing the chances of project delay. This dependency is also quite strong as pointed out by the high R<sup>2</sup> value. A more detailed break-down of the data shows that respondents with the least experience (1– 4 projects) clearly performed worse in size estimation. Learning to use size estimation methods efficiently thus requires time.

Another finding is that a moderate allocation of resources (2–8% of the project’s time) to manage risks can help considerably to maintain a stable and correct resource allocation, and to manage complexity. This comes as no surprise, as these two risk items are closely related – a fact which has been well known since Brooks’ eloquent discussion in his Mythical Man–Month (1974). Our analysis reveals, however, that too little risk management (less than 2%) or too much (over 8%) can result in a considerably lower performance. A reasonable time slot allocated (2–8% of the project’s time) also improves the chances of coping with project complexity. The fundamental lesson here is: garner experiences in using the risk management methods, and reserve adequate resources to do it properly.<sup>6</sup> These two management aspects seem to be more important in managing software risks than choosing ‘the correct’ risk management method.

To our surprise we found that only two risk management methods relate significantly to managing specific risk items. These two methods were: decomposing poorly defined project parts, and the analysis of key decisions. We did not find the multitude of cause–effect relationships across top-ten risks and risk management methods as suggested by Boehm’s risk management approach (1989). Instead, we found two new dependencies. The first one suggests that the decomposition of poorly defined project parts increases the ability to control the continuing stream of requirements changes. This finding is interesting in two ways. First, this risk management technique tackles a risk item that has been reported to be one of the most critical ones (Davis, 1982; Curtis et al, 1988; Lyytinen, 1988; Ropponen & Lyytinen, 1996). Second, this relation was not suggested by Boehm.<sup>7</sup> The detected causal relation can, moreover, be interpreted in a straight-forward manner: those project areas that are ignored in early phases tend to show up later causing surprises to project managers and thereby leading to late and uncontrolled requirements changes. In contrast, simple decomposition of system and project components and functions will lead to early recognition of missing parts and thereby to avoid hazardous requirement changes.

Second, we observed that the analysis of key decisions (i.e. decisions on hardware, subcontractors, timetables and budgets) relates significantly to designing a correct user interface. This can be explained by the fact that many key decisions are made separately from thinking about the use of the software. Selecting hardware, picking up subcontractors, and setting timetables and budgets are rarely conducted by the system users, but are instead agreed and carried out at managerial level discussions. Despite this these decisions can have tremendous effects on the capability to develop user friendly systems. This is often the most time-consuming enterprise in software development requiring skill and dedication. With this explanation it is easy to understand that paying attention to key decisions has an effect on the usability of the produced system.

## The impact of environmental contingencies

Overall, the environment faced by the project managers in our sample included both in-house IS departments and software houses of varying size. The respondents in our sample reported experiences of nearly 1100 software projects. MIS applications covered c.a. 76% of all projects included in the sample. By US standards the majority of the development projects were small. The largest reported project was 672 man months. The average size of the last completed project was 15.24 (std = 11.14; N = 75).

The results of analysing the dependence of risk management performance on environmental contingencies are shown in Table 2. Using one-way ANOVA we found altogether seven environmental factors that explain the risk management performance. These were: the type of project’s client, project size, project length, selection of hardware architecture, the nature of used development methods, project manager’s experience, and the amount of project management training. These influenced the management of the following risks: project delays, the dead-line effect, stable consumption of time, project complexity, gold plating, and changes in timetable. Results vividly illustrate the importance of understanding environmental contingencies in system development. These are: experience in managing projects, the size of the last project, and the status of the development methods. The analysis suggests that the ability to keep a project on time is improved by the project manager’s experience (projects of 36–84 man months), the size of the project, and working for an external client. In addition, respondents with experience from only one project, scored much lower than those who had managed two or more projects. Moreover, we also found that success in avoiding a deadline-effect<sup>8</sup> relates significantly with the experience with large projects (over 180 man months). Those respondents who had managed two or more projects of this size scored much better than those who had completed only one project. Furthermore, the analysis suggests that a larger experience in managing projects increases the ability to handle project complexity. Respondents who had managed only one project performed worse than those having experience with two or more projects.

Interestingly, our study shows that the size of the last completed system project is inversely related to the ability to manage risks (cf. McFarlan, 1982) in that the smaller the size the better the ability to complete the project on time. This is in line with earlier studies that smaller projects have fewer communication links, and therefore have a higher likelihood of an early problem recognition (Brooks, 1974), and they are therefore easier to estimate. This can be formulated as a risk management strategy: keep the project size small. In a similar vein, keeping the project size small helps in achieving a better resource allocation. Overall, middle sized projects (11–50 man months) scored significantly better than larger ones. Moreover, we found a similar relationship in avoiding schedule changes. When measured by three variables (duration, man months and actual costs) the results show that a larger project is more likely to run into difficulties with schedule changes.

Table 2 The effects of environmental characteristics on managing risks

<table><tr><td>Performance in managing risk item</td><td>Environmental variable</td><td>F</td><td>P</td><td>N</td><td> $R^2$ %</td></tr><tr><td rowspan="4">Problems in timetable</td><td>A project&#x27;s client</td><td>7.49</td><td>0.0076</td><td>83</td><td>8</td></tr><tr><td>Experience with projects having size of 36–84 man months</td><td>8.18</td><td>0.0060</td><td>56</td><td>13</td></tr><tr><td>The size of the last project (man months)</td><td>6.96</td><td>0.0018</td><td>72</td><td>17</td></tr><tr><td>The size of the last project (actual costs)</td><td>5.51</td><td>0.0070</td><td>51</td><td>19</td></tr><tr><td>Resource usage and deadline</td><td>Experience with projects over 15 man years</td><td>9.38</td><td>0.0120</td><td>12</td><td>48</td></tr><tr><td rowspan="2">Steady consumption of time</td><td>The size of the last project (man months)</td><td>5.43</td><td>0.0065</td><td>72</td><td>14</td></tr><tr><td>The status of the development methods</td><td>4.81</td><td>0.0040</td><td>82</td><td>16</td></tr><tr><td>Complexity easy to handle</td><td>Experience with projects under six man months</td><td>11.61</td><td>0.0013</td><td>52</td><td>19</td></tr><tr><td rowspan="2">Gold plating</td><td>Project management training</td><td>4.67</td><td>0.0121</td><td>83</td><td>10</td></tr><tr><td>Selection of hardware architecture</td><td>6.57</td><td>0.0124</td><td>74</td><td>8</td></tr><tr><td rowspan="3">Changes in time table</td><td>The duration of the last project (months)</td><td>7.96</td><td>0.0008</td><td>75</td><td>18</td></tr><tr><td>The size of the last project (man months)</td><td>8.40</td><td>0.0005</td><td>72</td><td>20</td></tr><tr><td>The size of the last project (actual cost)</td><td>8.39</td><td>0.0007</td><td>51</td><td>26</td></tr></table>

The analysis also reveals that variation in such factors as the type of the project client, the status of development methods, volume of project management training, and selection of hardware architecture can affect risk management performance. Projects with external clients handle schedule constraints more successfully than projects with an in-house client. This can be explained by differences in incentive structures and heavy penalties associated with the late delivery times in external projects. It also lends support to the popular argument that outsourcing improves development control. Organizations preferring obligatory use of development methods scored significantly better in achieving stable resource consumption than organizations relying on voluntary use. This finding is in line with Humphrey’s (1989) theory in that a disciplined systems development environment leads to better control of the development process. The extent of project management training and applied hardware architecture both reduced the negative effect of gold plating. Well trained project managers succeeded significantly better in that they could focus on essential aspects of the design. Finally, project managers working with centralised architectures avoided gold plating significantly better than those developing systems with distributed architectures. This can be explained by two salient features of distributed systems. For one thing, they offer more ‘bells and whistles’ to develop fancy user interfaces than the earlier text based centralised solutions. Second, less managerial control can be exercised in distributed environments.

## Discussion and conclusions

This paper sought answers to four questions concerning the impacts of software risk management. In this section we summarise our findings and discuss their implications for IS management.

(1) Does risk management improve developers’ performance in handling software risks? Some significant interactions were observed between the use of risk management methods and risk management performance.

The most important insight is that the time and effort spent on risk management deliberations have a positive impact on process related risks (the timely delivery of software and the correct estimation of resource needs). In particular, the number of projects where risk management methods have been used and the extent of their usage were found to be good predictors of improved risk management performance. Effects in using risk management methods were observed with getting the requirements right, and with managing development tasks. Overall our findings are promising in that several features of risk management could be brought to bear on how risks are effectively managed. In addition, these benefits tend to grow with experience. Hence, the value of risk management is not only a fiction, and IS shops should carefully consider its use especially if they continually face problems in project timing, resource usage, and management of complexity. Moreover, performance in managing risks seems to be a function of better managerial cognition, commitment, and the use of a proactive management style, rather than using a specific risk management technique.

(2) What factors in the development process and environment correlate significantly with the improved risk management performance? We observed that risk management performance depends on several environmental contingencies. These include the size of the IS department, the project size, project management training, project managers’ experience, and the use of systems development methods. This suggests that risk management performance can be improved by leveraging on the experience of the project managers, by improving management training, by disciplining the development process, by minimising the project size, and by standardising and controlling essential components in the application development (such as user interfaces).

Our findings need to be interpreted with caution because the study suffers from a number of limitations. First, Boehm’s ‘top-ten’ list of software risks may ignore some software risk items that are important for managers, or end users. It is important to remember that Boehm’s studies focused exclusively on project managers’ perceptions of software development (Lyytinen et al, 1996b). Another problem stemming from Boehm’s list is that it is to a large extent inductive and lacks an integrating conceptual foundation. Therefore advances in reliably measuring software risks can only be made after developing a more systematic and coherent classification of risk items and their sources (Barki et al, 1993; Lyytinen et al, 1996b). The third problem is that the measurement of risk management performance was based solely on the project managers’ self-reports. In future, we need to supplement these measures with more objective behavioural and economic measures. The fourth problem is a possible sampling bias in using project managers from one country, despite the fact that our sample was quite representative in terms of industries covered and types of systems developed. Finally, our study shares the limitations of all survey studies in establishing causal inference – it was a single period study without a control group (Haga & Zviran, 1994). Therefore obtained results are only indicative of possible causal connections. The validity of our findings can be improved in future by using designs that remove some of the limitations of the current study. We need to improve the instrumentation, use several measurement points (before and after application of risk management methods), extend the study to other countries, and introduce quasi experimental research designs (by controlling environmental variation).

## Notes

1. We are indebted to several experienced project managers who helped to design and validate the instrument.

2. For example, there is some lack of rigor in deriving the list. Boehm only mentions that the list is ‘based on a survey of several experienced project managers’ (Boehm, 1991, p 35). The list was derived from interview data and available project data base (Boehm, 1995). Yet, the ranking procedure is not systematic. The limitations also include that it covers only a software production oriented part of software development and ignores implementation and political risks that were emphasized by some project managers participating in our interviews (see also Schmidt et al, 1996). Therefore the ranking of Boehm’s top-ten risk items should not be understood as a complete ranking of all potential risk items but of those that Boehm found in his studies. There may also exist a possible bias in the selection of risk items due to the emphasis on large software projects.

3. The questionnaire did not give us a good mechanism to control the impact and time of historical incidents (both the personal history and a project phase) on which the respondents based their responses of their performance. Therefore, connecting respondents’ development practices to their evaluations can be biased. Risk management outcomes change slowly, however, over longer time periods. Therefore, we believe that we obtained sufficient reliable measures of risk management performance by analysing these statements. Statistical validity measures also suggest this. Although we cannot directly connect respondents’ evaluations to certain project phases, their responses are likely to reflect their perceptions of their overall success in managing software risks.

4. Altogether we derived 14 questions from this list. These were selected to cover essential methods in Boehm’s list.

5. Chi-square test was not applicable because the cell frequencies were not at an acceptable level (Mills, 1965).

6. This basically reflects a true commitment to engage actively in risk management.

7. Instead, Boehm mentions high change threshold, information hiding, and incremental development by deferring changes to later increments.

8. This means uncontrolled resource consumption just before a project deadline.

9. Stakeholder groups by Boehm and Ross, 1989; subordinates and bosses denote those of a project manager.

Acknowledgements – We are grateful to Roy Schmidt, Lars Mathiassen, Esko Leskinen, and anonymous reviewers for comments and constructive criticism.

## References

<sup>Alter</sup> <sup>S</sup> and <sup>Ginzberg</sup> <sup>M</sup> (1978) Managing uncertainty in MIS implementation. Sloan Management Review, Fall, 23–31.

<sup>Barki</sup> <sup>H,</sup> <sup>Rivard</sup> <sup>S</sup> and <sup>Talbot</sup> <sup>J</sup> (1993) Toward an assessment of software development risk. Journal of Management Information Systems 10 (2), Fall, 203–225.

<sup>Beath</sup> <sup>CM</sup> (1987) Strategies for managing MIS projects: a transaction cost approach. In Proceedings of the 4th International Conference on Information Systems, Texas, Houston, 15–17 Dec, pp 133–147.

<sup>Beath</sup> <sup>CM</sup> (1987) Managing the user relationship in information systems development projects: a transaction governance approach. In Proceedings of the 8th International Conference on Information Systems, Pittsburgh, 12–14 Dec, pp 415–427.

<sup>Boehm</sup> <sup>BW</sup> (1989) Software Risk Management, tutorial. IEEE Computer Society Press.

<sup>Boehm</sup> <sup>BW</sup> (1991) Software risk management: principles and practices. IEEE Software January, pp 32– 41.

<sup>Boehm BW</sup> (1995) Personal communication. Helsinki University of Technology, 20 June.

<sup>Boehm</sup> <sup>BW</sup> and <sup>Ross</sup> <sup>R</sup> (1989) Theory-W software project management: principles and examples. IEEE Transactions on Software Engineering 15(7), 902–916.

<sup>Brooks</sup> <sup>F</sup> (1974) The Mythical Man-Month: Essays on Software Engineering. Addison-Wesley London, Prentice-Hall.

<sup>Charette</sup> <sup>RN</sup> (1989) Software Engineering Risk Analysis and Management. Intertext Publications McGraw-Hill Book Company.

<sup>Cronbach LJ</sup> (1951) Coefficient alpha and the internal structure of tests. Psychometrika 16(3), 297–334.

<sup>Curtis B, Krasner H</sup> and <sup>Iscoe N</sup> (1988) A field study of the software design process or large systems. Communications of the ACM 31(11), 68–87.

<sup>Cody</sup> <sup>RP</sup> and <sup>Smith</sup> <sup>JK</sup> (1987) Applied Statistics and the SAS Programming Language. 2nd ed. Elsevier Science Publishing Co, Inc.

<sup>Davis</sup> <sup>GB</sup> (1982) Strategies for information rquirements determination. IBM Systems Journal 21(1), 4–30.

<sup>F</sup>innish Information Processing Association (1991) Individual Business Members. In Buyer’s guide 1991. Infoline Oy/Insino¨o¨rilehdet Oy, Kustannusosakeyhtio¨ Otava, Keuruu.

<sup>Genuchten</sup> <sup>M</sup> <sup>van</sup> (1991) Why is software late? An empirical study of reasons for delay in software development. IEEE Transactions on SE 17(6), 582–590.

<sup>Haga W</sup> and <sup>Zviran M</sup> (1994) Information systems effectiveness: research design for causal inference. Information Systems Journal 4(2), 141–166.

<sup>Humphrey</sup> <sup>WS</sup> (1989) Managing the Software Process, Software Engineering Institute. The SEI Series in Software Engineering. Addison-Wesley Publishing Company Inc.

<sup>Kerzner</sup> <sup>H</sup> (1987) In search of excellence in project management. Journal of Systems Management 38(2), 30–39.

<sup>Lyytinen</sup> <sup>K</sup> (1987) Different perpectives on information systems: problems and their solutions. ACM Computing Surveys 19(1), 5–44.

<sup>Lyytinen</sup> <sup>K</sup> (1988) Expectation failure concept and systems analyst’s view of information system failures: results of an exploratory study. Information & Management 14(1), 45–56.

<sup>Lyytinen</sup> <sup>K</sup> and <sup>Hirschheim</sup> <sup>R</sup> (1987) Information systems failures: a survey and classification of the empirical literature. Oxford Surveys in Information Technology. Oxford University Press, Vol. 4, pp 257–309.

Lyytinen K, Mathiassen L <sub>and</sub> Ropponen J <sub>(1996a)</sub> <sub>A</sub> <sub>framework</sub> for software risk management. Journal of Information Technology 11, 278–285.

Lyytinen K, Mathiassen L <sub>and</sub> Ropponen J <sub>(1996b)</sub> <sub>Attention</sub> <sub>shap-</sub> ing and software risk: a categorical analysis of four classical approaches. University of Jyva¨skyla¨, Finland, unpublished working paper.

<sup>Markus L</sup> and <sup>Keil M</sup> (1994) If we build it, they will come: designing information systems that users want to use. Sloan Management Review 35(4), 11–25.

Mathiassen L, Seewaldt T <sub>and</sub> Stage J <sub>(1995) Prototyping and</sub> specifying: principles and practices of a mixed approach. Scandinavian Journal of Information Systems 7(1), 55–72.

<sup>McFarlan</sup> <sup>W</sup> (1982) Portfolio approach to information systems. Journal of Systems Management January, 12–19.

## Appendix 1

Boehm’s top-ten risk list and stakeholder perspectives concerned

Name of the Description Stakeholder risk item concerned<sup>9</sup> Personnel Lack of qualified Customer, users, shortfalls personnel and their subordinates, change maintainers, bosses, project manager Unrealistic Development time Customers, bosses, schedules and and budget estimated project manager budgets incorrectly (too low) Developing wrong Development of User, project software functions software functions manager that are not needed or are wrongly specified Developing wrong Inadequate or User, project user interface difficult user manager interface Gold plating Adding unnecessary Subordinates, users, features (‘whistles project manager and bells’) to software because of professional interest or pride or user’s demands Continuing stream Uncontrolled and Subordinates, user, of requirement unpredictable change project manager changes of system functions and features Shortfalls in Poor quality of Customers, bosses, externally system components project manager furnished that have been components delivered externally Shortfalls in Poor quality or Customers, bosses, externally unpredictable project manager performed tasks accomplishment of tasks that are performed outside the organisation

<sup>Mills FC</sup> (1965) Statistical Methods 3rd edn, Sir Isaac Pitman and Sons Ltd.

<sup>Neo</sup> <sup>BS</sup> and <sup>Kwong</sup> <sup>SL</sup> (1994) Managing risks in information technology projects: a case study of trade net. Journal of Information Technology Management May.

<sup>Nunnally</sup> <sup>JC</sup> (1978) Psychometric theory. McGraw-Hill, New York, NY.

<sup>Ropponen</sup> <sup>J</sup> (1993) Risk management in information system development, technical reports TR-3. Department of Computer Science and Information Systems, University of Jyva¨skyla¨, Finland.

<sup>Ropponen</sup> <sup>J</sup> (1997) Software Development Risks and Management Practices — a project manager survey. In Beyond the IT Productivity Paradox: Assessment Issues (<sup>Willcocks</sup> <sup>L</sup> and <sup>Lester</sup> S, Eds), McGraw-Hill Inc, forthcoming in September.

<sup>Schmidt</sup> <sup>R</sup> et al (1996) Identifying software project risks: an international Delphi study, Hong Kong University of Science and Technology, unpublished working paper.

<sup>Straub DW</sup> (1989) Validating instruments in MIS research. MIS Quarterly June, 147–165.

<sup>Swede</sup> <sup>van</sup> <sup>V</sup> and <sup>Vlient</sup> <sup>van</sup> <sup>J</sup> (1994) Consistent development: results of a first empirical study on the relation between project scenario and success. In Wijers G., Brinkkemper S (eds), Proceedings of the 6th CAiSE Conference, Springer-Verlag.

<sup>Willcocks L</sup> and <sup>Margetts H</sup> (1994) Risk assessment and information systems. European Journal of Information Systems 3(2), 127–138.

Straining computer Inability to Subordinates, users, science capabilities implement the system customers, project because of lacking manager technical solutions and computing power

## Appendix 2

## Measurement for risk management performance

In the following we present a list of statements describing your projects. Mark an appropriate alternative for each statement based on your experience. Choose one alternative based on how often the described situation occurs.

<table><tr><td></td><td>Hardly ever</td><td>Rather seldom</td><td>Half</td><td>Rather often</td><td>Almost always</td></tr><tr><td>Your project has considerable problems due to personnel shortfalls</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Your project is completed according to the timetable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Resource consumption reaches its top when you finish the project</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Actual project costs and estimated costs in your projects are close to one another</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Your project is cancelled before completing it</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>A failure to estimate software size interferes with the system implementation</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Demand of personnel in your project is constant</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Time consumption of your project is constant</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Personnel in your project has insufficient expertise in methods, software, and equipment</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>The project complexity of your project and its effects are easy to manage</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Developed software functions and properties meet with users' demands</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Developed software includes complex, but only marginally useful properties</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Software requirements are continuously changed</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Your project timetable is changed continually</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Users are not satisfied with the user interface</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Purchased components and equipment in your project meet the expectations</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>You have unrealistic expectations of the project members' skills</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Real-time performance requirements are estimated incorrectly</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Subcontracted tasks in the project are performed as expected</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Software and hardware functionality is estimated incorrectly</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr></table>

## Appendix 3

## Validation of the survey instrument and control of sampling bias

Great care was taken to improve the instrument validity. Using Straub’s (1989) list of questions we describe how the instrument was validated.

## Content validity

This question addresses whether instrument measures are drawn from all possible measures of the properties under investigation, i.e. are its questions drawn from a representative universal pool. Because software risk measurement and software risk management performance are not well understood areas the issue of content validity is a serious one. We took several steps to improve content validity by examining available lists of software risk items and soliciting our questions from a representative sample. Based on their popularity and extensive empirical basis we decided to apply Boehm’s lists as a starting point (see e.g. Lyytinen et al, 1996b). It had also been compiled with a similar sample as we used in our study. We also discussed with experienced project managers and other qualified researchers how representative our set of questions was until we deemed it to be sufficient. This led to adding some measures to the risk performance measurement. Most of them related to managing process aspects such as completion in time, schedule changes, project cancellation and the deadline effect. These aspects were not seen to be captured by Boehm’s notion of ‘unrealistic schedules and budgets’.

## Construct validity

This question addresses whether the measures show stability across methodologies, i.e. that the data is a reflection of true scores of artefacts of the kind of instrument chosen. We sought to improve construct validity with several measures. First, we compared the data from our project manager interviews to the questionnaire data to resolve possible bias (see Ropponen, 1993). Second we conducted pilot-tests which led to modifications in the questionnaire which improved both the content and construct validity. In particular, we tested carefully that all interviewees could understand the questionnaire items so that they could provide an unambiguous answer to each question. To improve this we added to the questionnaire a list of items that described each technical term used (such as gold plating). During pilot testing we moreover asked the respondents to make suggestions to improve the questionnaire, e.g. by removing some items and adding new ones. This step introduced some amendments. We also analysed the possible discrepancies or variations in answers but found none.

## Reliability

This question shows the measures’ stability across the units of the observation, i.e. that the same questions are answered exactly or approximately in the same manner. The idea in improving reliability is to decrease the possibility that the measure is due to misunderstanding, error or mistake but instead reveals the true score. Usually high correlations between alternative measures or large Cronbach alphas are usually signs that measures are reliable (Cronbach, 1951). In order to address this question we used data reliability tests. We computed Cronbach alphas for the dependent variable of our study – the risk management performance items – because these items could be subject to bias. The results of this analysis are shown in Table 3. The overall Cronbach alpha was 0.79 for the standardised 20 variables which is acceptable. Sufficiently high correlations apply for all the items and they meet the level 0.70 suggested by Nunnally (1978) as adequate for exploratory research. Hence the reliability of the measures can be regarded sufficient.

Table 3 Cronbach coefficient alphas

<table><tr><td colspan="3">Cronbach coefficient alpha</td></tr><tr><td>Deleted variable</td><td>Correlation with Total</td><td>Alpha</td></tr><tr><td>Personnel shortfalls</td><td>0.119</td><td>0.795</td></tr><tr><td>Problems in timetable</td><td>0.424</td><td>0.777</td></tr><tr><td>Resource usage and deadline</td><td>0.116</td><td>0.796</td></tr><tr><td>Actual costs vs estimated costs</td><td>0.255</td><td>0.787</td></tr><tr><td>Cancelling of the project</td><td>0.119</td><td>0.795</td></tr><tr><td>Wrong size estimates</td><td>0.534</td><td>0.770</td></tr><tr><td>Estimates for personnel need</td><td>0.550</td><td>0.769</td></tr><tr><td>Steady consumption of time</td><td>0.344</td><td>0.782</td></tr><tr><td>Insufficient expertise</td><td>0.357</td><td>0.784</td></tr><tr><td>Complexity easy to handle</td><td>0.564</td><td>0.768</td></tr><tr><td>Functions and properties correct</td><td>0.296</td><td>0.783</td></tr><tr><td>Gold plating</td><td>0.332</td><td>0.783</td></tr><tr><td>Requirement changes</td><td>0.419</td><td>0.777</td></tr><tr><td>Changes in timetable</td><td>0.392</td><td>0.779</td></tr><tr><td>Satisfaction with the user interface</td><td>0.319</td><td>0.783</td></tr><tr><td>Shortfalls in externally furnished components</td><td>0.374</td><td>0.780</td></tr><tr><td>Evaluation of performance requirements</td><td>0.423</td><td>0.777</td></tr><tr><td>Unrealistic expectation of the personnel&#x27;s abilities</td><td>0.351</td><td>0.781</td></tr><tr><td>Success in externally performed tasks</td><td>0.300</td><td>0.785</td></tr><tr><td>Estimation of hardware and software functionality</td><td>0.489</td><td>0.773</td></tr></table>

## About the authors

Janne Ropponen holds a masters degree in computer science and information systems (1992) and a licentiate degree in economic sciences (1995) from the University of Jyva¨skyla¨, Finland. His research activities include the management of information technology projects and especially software development risks and their management. These are investigated in detail in his dissertation being prepared. Related to his PhD project he has written and co-authored a number of publications concerning software risk management which has been accepted e.g. in the Journal of Information Technology. He is currently working as a senior process development engineer at the Nokia Telecommunications Ltd where he is responsible for improving requirements and risk management practices.

The measures were also tested for their variance and normal distribution which were all met. This shows that no ‘floor’ or ‘ceiling’ effects were observed due to misunderstanding or measurement reactivity. We also tested for the possible personal bias in reporting performance by correlating all performance responses to an item which reported the percentage of own projects that had succeeded. The correlation was negative $( r _ { \mathrm { { S } } } = - 0 . 3 8 9 9 8$ $P = 0 . 0 0 0 3 , n = 8 3 )$ which suggests that the higher the reported success percentage in their own projects the worse they were actually managing risks. In this sense the measures obtained in managing risks seem to be highly reliable. Moreover, we reduced potential misunderstanding by paraphrasing the questions concerning the use of specific risk management methods in a manner where a respondent did not know that he is being asked the use of a risk management method. This was done purposefully, because many project managers do not necessarily know the technical terms of ‘risk identification, risk assessment’.

## Sampling bias

We also investigated carefully reasons for not responding by calling 24 persons who had not replied. No bias in reasons to not respond was revealed. In fact, more bias would have been generated in our study, as three of the non-respondents did not have any experience in project management. Too little time and offices the rule of not responding to any surveys accounted for over 50% of the reasons. This suggests that our results in some sense can be biased to convey an overly positive description of the situation.

Kalle Lyytinen is a full professor in Information Systems at the University of Jyva¨skyla¨, Finland and currently a visiting professor at Georgia State University. He currently serves on the editorial boards of Information Systems Journal, European Journal of Information Systems, Accounting, Management and Information Technology, MIS Quarterly, Information Systems Research, Information Technology & People, Requirements Engineering Journal and Journal of Strategic Information Systems. He has published over 70 articles and edited or written six books. His research interests include information system theories, system design methods and tools, system failures and risk assessment, electronic commerce, computer supported cooperative work, decision making theories, and diffusion of complex standardised technologies.
