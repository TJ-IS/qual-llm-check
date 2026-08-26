---
otero_id: 24452
otero_key: "Q6X432UK"
title: "The Effect of Human–Computer Interchange Protocol on Decision Performance"
authors: "David P. Hale; George M. Kasper"
year: "1989"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1989.11517846"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Effect of Human-Computer Interchange Protocol on Decision Performance

David P. Hale & George M. Kasper

To cite this article: David P. Hale & George M. Kasper (1989) The Effect of Human–Computer Interchange Protocol on Decision Performance, Journal of Management Information Systems, 6:1, 5-20, DOI: 10.1080/07421222.1989.11517846

To link to this article: https://doi.org/10.1080/07421222.1989.11517846

![](/api/attachments/Q6X432UK/fulltext/images/cc6931ab78a785868c91b506fedae4be563f33d55f061d09b1da4129048c17c5.jpg)

Published online: 22 Dec 2015.

![](/api/attachments/Q6X432UK/fulltext/images/461509036ca954ca40785b62f0c189670cabd13d94729aba66d288f45315e7de.jpg)

Submit your article to this journal ↗

![](/api/attachments/Q6X432UK/fulltext/images/f7774e748d4223a2f6010db0b14b4404da1c6c9b5f7e3429b187ab8e8dd9733c.jpg)

View related articles ↗

![](/api/attachments/Q6X432UK/fulltext/images/036d7bf84bca1781cfed70809e30858606b6a2aff0528aab5413be5befccce39.jpg)

Citing articles: 10 View citing articles ↗

The Effect of

# Human-Computer Interchange Protocol on Decision Performance

DAVID P. HALE and GEORGE M. KASPER

DAVID P. HALE is Assistant Professor of Information Systems and Quantitative Sciences at Texas Tech University College of Business Administration. He received his Ph.D. in Management Information Systems from the University of Wisconsin-Milwaukee in 1986. His research interests include collaborative problem-solving systems and software maintenance. His papers on joint human-computer problem-solving systems, database management system design, decision-group connectivity, and software maintenance have appeared in Management Information Systems Quarterly and several conference proceedings. He has been honored by the Society for Information Management for his work in decision-group connectivity.

GEORGE M. KASPER is Associate Professor of Information Systems and Quantitative Sciences at Texas Tech University College of Business Administration. He received his Ph.D. in 1983 from the State University of New York at Buffalo. His primary research interests are decision support systems and expert system-aided decision making. His research has been published in such journals as Decision Support Systems, Journal of Management Information Systems, Information and Management, Decision Sciences, and others. Dr. Kasper has also served as a visiting member of the Faculty of Informatics, Delft University of Technology, the Netherlands, and has worked and consulted for both government and private industry.

ABSTRACT: The concept of a collaborative human-computer interchange was proposed almost thirty years ago. The goal of this paradigm is to design human-computer decision-making systems that think and process information at a level exceeding that of either the human or the computer alone. Technological and conceptual developments have made this holistic partnership increasingly possible. Moreover, recent discussions of human-computer collaborative work have highlighted the system performance advantages of this interchange.

In this paper, the notion of human-computer interchange protocols is developed and the importance of these protocols to human-computer collaboration and system performance is argued. Based on data collected in a laboratory setting, empirical support for the proposed holistic effect of human-computer interchange protocols on system performance is provided. Decision performance is significantly improved by interchange protocols that encourage human-computer interaction during the problem-solving process.

KEY WORDS AND PHRASES: Human-computer interchange protocols, collaborative human-computer systems, cooperative human-computer systems, human-computer interaction, human-computer interface design, decision performance, decision support systems.

## 1. Introduction

ALMOST THIRTY YEARS AGO, Licklider [15] proposed a holistic human-computer partnership that would think and process information at a level not approached by either the human or the computer alone. "To think in interaction with a computer in the same way that you think with a colleague whose competence supplements your own will require much tighter coupling between man and machine than is . . . possible today" [15, p. 5]. Despite this often cited quote, Peace and Easterby [20], Woods [28, 29], Henderson [8], and others have at varying times lamented the lack of progress and called for renewed efforts to develop such human-computer collaborative decision-making systems. Collaborative decision making can be defined as the process by which participants jointly contribute knowledge that incrementally moves the whole toward a goal state. In this way, participants, whether human or machine, interact by adding knowledge to a current state that moves the whole toward a goal. The rules governing this interchange are critical to the effectiveness of this process.

While progress has been made, much work remains before the level of human-computer interchange needed to produce the holistic performance envisioned by Licklider is realized. As currently designed, the decision performance of either decision support systems (DSS) or expert systems (ES) is limited to the knowledge of the controlling component of the system. For DSS, the human is in control and decision performance is primarily a function of the human's knowledge; for ES, the system is in control and the primary limitation to performance is its knowledge [26]. While this perspective neglects the human's ultimate control over the process, and may only reflect ES and DSS at the extremes, it is clear that neither of these designs takes full advantage of the joint problem-solving potential of the whole system [16]. Holistic problem solving requires the design of a human-computer interchange that effectively integrates the knowledge and capabilities of the human and the computer application. The nature of this interchange ranges from query/response transactions (controlled by either party) to a point where both the computer application and the human are collaboratively involved in the problem-solving process.

The purpose of this paper is to investigate the effect of different forms of human-computer collaboration on system performance. To facilitate collaboration, the concept of human-computer interchange protocols is proposed and the results of a laboratory study supporting this proposition are reported. Specifically, the decision performance of interchange protocols that vary the sequencing of human and computer application interaction during the problem-solving process are compared.

The literature suggesting the need to combine the capabilities of computer applications and the abilities of the human to produce a holistic problem-solving system is reviewed in the next section. The notion of collaborative human-computer interchange protocols and their relation to holistic system performance is then developed. Based on this, a discussion of the experiment and its hypotheses, design, and methodology follow. Data analysis and the results are then reported. Finally, the empirical results are summarized, and the implications of the study and conclusions of the research are presented.

## 2. Background

THE EFFECTIVE INTERCHANGE OF HUMAN ABILITIES and computer capabilities is fundamental to the development of holistic problem-solving systems. The conceptual foundation of these systems is based on the work of human factors engineers $[15, 20]$ , decision theorists $[11, 27]$ , knowledge engineers $[9, 28, 29]$ , decision support system designers $[8, 16, 26]$ , and others. The breadth of support and convergence of thought from these fields suggests a conceptually well-founded, yet practical, paradigm on which to develop these systems.

Commenting on the need to integrate human abilities and computer capabilities, Ginzberg and Stohr [7, p. 22] contend that the application of computer-based models must be tempered by knowledge of the specific setting. Keen and Scott Morton [13] have also argued for combining computer-based support and the human's descriptive realism. The most effective decision support "lies in meshing the machine's efficiency . . . with the individual's judgement" [13, p. 68]. Research on the "mutual symbiosis of mind and computer can be immensely valuable" to the development of DSS [13, p. 68]. The structure of this interchange is critical to effective human-computer problem-solving.

Expert system knowledge engineers also suggest that effective decision support is best met by integrating human and artificial intelligence $[28, 29]$ . This integration requires the design of effective human–computer interchange strategies. Woods $[28, 29]$ proposes two strategies for designing effective human–computer problem-solving systems. The first uses a redundant design in which the human or the computer critiques the other's plan or solution. The second interchange strategy requires a “...man-in-the-control-loop (or decision loop) architecture...” $[28, p. 157]$ in which the human and computer application confer at intermediate steps during the problem-solving process. Both human–computer interchange strategies suggest vehicles for effectively integrating the human and computer application into a collaborative holistic decision-making system. The development of effective rules governing the interchange between the human and the computer application will require much work; the balance of this paper attempts a beginning toward this end.

## 3. Development of Collaborative Interchange Protocols

THE RULES GOVERNING THE EXCHANGE OF KNOWLEDGE between collaborating entities are critical to the effectiveness of these systems. Within the data communications literature, a set of rules governing the exchange of information between two entities is known as a protocol [23, p. 372], which is equivalent to conversational structure in the human communications literature [6, ch. 10]. Key elements of both conversational structure and protocol are syntax, semantics, and timing. $^{1}$

The role of syntax and semantics in human-computer interface design has been the topic of much research. In fact, a syntactic/semantic model of user behavior has been proposed by Shneiderman [21, ch. 2]. His model treats syntactic knowledge as somewhat arbitrary and system dependent, but divides semantic knowledge into knowledge about task concepts and computer concepts. $^{2}$ Because his syntactic/semantic model identifies the types of knowledge needed by a computer user, Shneiderman [21] suggests that it serves as an aid to both the designer and researcher of human-computer interfaces. Syntax and semantics have also been the topic of much natural language interface (NLI) research; however, rather than leading to more human-computer collaborative problem-solving, a NLI may actually increase the human's processing load [21, p. 168; 14]. Furthermore, syntax and semantics in the form of mode of presentation have received much attention by management information systems (MIS) researchers. Collectively, the evidence suggests that the effect of presentation syntax and semantics on decision quality (decision performance, decision time, etc.) depends upon the complexity of the problem [4]. Detailed reviews of the syntax and semantics of human-computer interaction can be found in Montazemi and Wang [18] and DeSanctis [3].

Timing, the third key element of protocol, includes both the speed and the sequencing of the interchange [23, p. 372]. Speed consists of system response time (the time it takes for the system to begin displaying information in response to a user query) and display rate (the rate at which characters are displayed) [21, pp. 106–7]. $^{3}$ Sequencing includes flow management, error management, and exchange coordination; or more generally, interchange management [23, pp. 380, 4–5].

Characteristics of human-computer interchange sequencing include the initiating entity, the controlling entity, and the amount of information (knowledge) contributed before surrendering control. The problem-solving process can be initiated [2, 19] or controlled by either the human or the computer application [26]. At the extremes, sequencing of the human-computer interchange can follow either a simple batch approach or a problem-sharing protocol. That is, either the human or the computer application can solve the problem, which is then reviewed and critiqued by the other entity; or shares of the problem-solving effort can be naively apportioned to the human and computer independent of the nature of the problem, the problem-solving process, and the unit of exchange. Between these extremes, an interchange protocol exists that maximizes human-computer collaboration and system performance by sequencing the interchange of knowledge in a way consistent with the nature of the problem-solving process and the specific problem. Problem decomposition, as argued by Simon [22], may provide a means of identifying points during the process of solving a specific problem where human-computer interchanges would result in improved decision performance.

Consistent with the MIS paradigm [12], factors other than the protocol governing the human-computer interchange also affect decision performance. These include individual characteristics and problem complexity [18]. Individual characteristics pertain to both the human and the computer. For example, both the human's and the computer application's problem-solving style have been suggested as important determinants of system performance [10]. While task is already recognized as an important determinant of interface design [21, p. 55], the characteristics of the problem take on added importance in the design of a collaborative human-computer system. The degree to which a problem can be decomposed, the complexity of the subproblems, etc., are expected to affect both the performance and the design of collaborative human-computer problem-solving systems.

## 4. Empirical Support

THE DEVELOPMENT OF INTERCHANGE PROTOCOLS that maximize human-computer decision performance is the ultimate goal of this line of research. Assessment of differences in human-computer system interchange protocols is fundamental to the achievement of this goal. Based on Woods' [28] proposed strategies and the conceptual development of collaborative protocols, the effect of human-computer interchange sequencing on system performance is investigated. Specifically, differences in performance are compared for system sequencing strategies in which the human critiques and alters a heuristically based application's proposed solution and two cooperative (human-in-the-control-loop) protocols in which a heuristically based application and the human confer at various points during the problem-solving process. Factors other than the sequencing of the human-computer interchange (such as syntax, semantics, speed, and the underlying decision aid) are held constant.

## 4.1. Experimental Design

To isolate individual differences, a blocked design in which each subject received all treatments is used. Each block consists of a non-repeating combination of the four treatments. To prevent any carryover effect from confounding the results, each of the twenty-four possible treatment orderings appears once in the experimental design. The four treatments are a control in which no sequence is imposed on the human-computer interchange, a critique protocol in which the human critiques and alters the computer application's proposed solution, and two cooperative protocols in which the human-in-the-control-loop strategy is achieved by altering the sequence by which the application and the human confer during the problem-solving process. Each treatment is discussed in detail below.

## 4.2. Decision Setting

Simon [22] and Ginzberg and Stohr [7] argue that decomposition and the imposition of structure are essential contributions of the problem-solving capabilities of their respective decision-aiding approaches. For collaborative human-computer systems, this requires, at a minimum, that both the computer application and the human have some knowledge to contribute to the problem-solving effort, and that they have an opportunity to make their contribution(s). The latter necessitates the identification of points within the problem-solving process where both entities can confer. To meet these requirements, network routing problems, in the form of the “traveling salesman problem,” were selected as the decision setting for this study. Four characteristics of this decision setting make these problems particularly appropriate because they are (1) multiple-step problems in which the nodes offer distinct conferring points; (2) known and represent familiar situations encountered by the subjects on a daily basis;

and (3) problems for which computer-based heuristics are available; however, (4) short of enumerating all possible routes (which is impractical for all but small problems), neither the computer nor the human can guarantee a real-time optimal solution, but an optimal solution can be found. From a research perspective, this last characteristic provided a challenging problem-solving environment with an absolute measure of performance.

The decision setting consisted of a microcomputer-driven screen displaying a cost matrix, labeled points representing the nodes of the domain, and questions from the interface software or suggestions from the underlying decision aid. Points labeled A, B, C, etc. were printed on the right half of the display. By identifying two labeled points, line segments were added or deleted, which the software then drew or erased accordingly. By design, the placement of the labeled points did not reflect the cost matrix data. Participants were told to use the software and cost matrix to make their decisions, and that the labeled points were only intended to provide a scratch pad for their work.

## 4.3. Subjects

Consistent with the experimental design, a total of twenty-four subjects participated in the study. The sample consisted of students enrolled in a graduate MIS data communications course. To encourage participation and to motivate performance, subjects were given extra credit points toward their course grade and a total of S80 in performance incentive money. The subject with the highest average treatment performance received \$50; and the second highest, \$30.

Demographically, the subjects reported a median age of 25 years, and 60 percent indicated full-time work experience of, on average, 3 years. The overwhelming majority of the subjects had undergraduate degrees in computer science/MIS or a quantitative field, and all had some exposure to network routing heuristics. Moreover, the frequency with which network routing problems occur in daily life makes task performance somewhat independent of formal experience and background. This is supported by the pilot study results discussed below.

## 4.4. Treatments

Each subject completed all four treatments. All treatments included identical syntax, semantics, and decision aid; however, the sequencing of problem-solving interchange between the human and computer application was varied. One treatment consisted of a control in which no specific problem-solving sequence was imposed on the human-computer interchange. While supported by information from the decision aid, in the control treatment the human made all network node connection decisions (i.e., adding and deleting arcs). Based on the conceptual development of collaborative protocols, and consistent with Woods' [28] discussion, each of the remaining treatments attempted to impose a different human-computer interchange strategy on the joint problem-solving process by varying the sequence in which the human and the computer application made network node connection decisions. The critique treatment allowed the subject to critique and modify the heuristic-based application's completed network routing answer.

Two cooperative treatments were developed to investigate the performance of human-in-the-control-loop strategies. The alternate cooperative treatment required the human and the computer to alternate making decisions at each node in the network. The last treatment—dichotomous cooperative—allowed the human to request that the computer application finish the network once the human had proposed a route connecting a minimum of fifty percent of the network. In this way, both the alternating and the dichotomous cooperative treatments provided the same amount of decision aid support; the only difference was in the timing of this support. Within the confines of all four treatments, subjects were free to add and delete arcs at any time, and upon completion of a route, to investigate any number of alternatives.

Pilot study results and debriefings indicated that the arc selection behavior of a majority of subjects was consistent with that of the best-first $^{4}$ heuristic when no support was provided nor problem-solving sequence imposed. This result highlighted the need, as suggested by Licklider [15, p. 5], to provide the human “with a colleague whose competence supplements” his or her own. Rather than supplement, the pilot study results indicated that the best-first network routing heuristic merely mimicked the subjects’ approach.

To provide a computer-based colleague whose competence supplements that of the human requires an algorithm more accurate than the subject's best-first heuristic. A random perturbation heuristic [24, p. 69] was chosen as the computer application's decision algorithm because it differs so much from the systematic procedure of best-first, its accuracy is inversely related to the number of nodes remaining in the network, and it is easily implemented and applied to subsets of a larger problem. The random generation of possible solutions, so very compatible with computer application capabilities, is all but impossible for the human. Yet this problem-solving difference was a primary reason for believing that the random perturbation heuristic would supplement the human's best-first approach.

To ensure the need for an exchange of information between the human and the computer application, and a response rate commensurate with online problem solving, the random perturbation algorithm was restricted to two thousand perturbations. In practice this meant that as the number of unconnected nodes in the network decreased, performance of the computer application increased. For each arc decision, the minimum arc of the best performing of either the best-first or the random perturbation algorithm was provided as the computer application's selection for all four treatments.

It should be noted that our intention was not to provide a computer-based colleague that always found the optimal solution; if a computer application can solve the problem alone, there is no need to have a human colleague. Conversely, there is no incentive to seek the computer colleague's help if some of its suggested decisions are no better than the human's alone. In practice, the decision setting would be expected to be much more complex and the heuristic algorithm (expert system) to be much more sophisticated than was used in this research. However, given the relative simplicity of the setting, support for the hypothesized improvement in decision performance should understate the “real world” potential effect of the sequence of human-computer interchange on problem-solving performance.

## 4.5. Hypotheses

Basic to the development of collaborative human-computer problem-solving systems is the expected holistic performance of such systems. Therefore, the primary intent of the empirical study is to investigate the effect of varying forms of human-computer collaboration on system performance. Specifically, the decision performance of the critique and two cooperative problem-solving treatments are compared with that of the human (control treatment) and the computer-based heuristic's performance alone. Stated in the null form, hypothesis one is

H 1.0: No difference in decision performance exists between any of the three human-computer collaboration treatments (critique, alternating, and dichotomous) and either the human's (control) or the computer-based heuristic's performance alone.

In the presence of collaborative human-computer performance significantly greater than that of either the human or the computer alone, an examination of the other treatment contrasts is required to determine the effectiveness of the different human-computer problem-solving strategies. Specifically, the contrast hypothesis compares the performance of the critique and the two cooperative treatments.

H 2.0: No difference in decision performance exists between critique, dichotomous cooperative, and alternating cooperative human-computer problem-solving interchange treatments.

While problem complexity is recognized as an important determinant of system performance [18], its interaction with the protocol governing human-computer interchange is likely to take on added importance in a collaborative problem-solving system. As in any system designed to maximize decision performance, a collaborative effort among components is only required when the problem cannot be effectively solved by any single component of the system; that is, help from a colleague is only needed when the problem is beyond one's own capabilities. This is true, whether the colleague is a computer-based heuristic or a human. Therefore, one expects more collaboration among colleagues to solve complex problems than to solve easy problems. Consistent with this reasoning, the last hypothesis is

H 3.0: No difference in decision performance exists due to the interaction of problem complexity and the treatments governing the human-computer interchange.

To estimate the interaction effect of problem complexity and the protocols governing the human-computer interchange, problem complexity was defined as follows. Both optimal $^{5}$ and best-first heuristic solutions were computed for 100 randomly developed eleven-node network problems. Because the objective was to identify problems that might be more effectively solved by a human-computer interchange, network routing problems for which the best-first heuristic found the optimal solution were discarded. To be consistent with the number of treatments, the remaining 77 problems were divided into 4 groups that were relatively equal in size, and one problem was selected from each group. For the selected problems, the best-first heuristic's performance error was 6, 12, 18, and 24 percent of the optimal solution. These deviations from optimal performance defined four levels of problem complexity, and their respective eleven-node network problems served as the specific decision setting for this study.

Both the selection of eleven-node networks and the definition of problem complexity as the percent error of the best-first heuristic were based on the results and observations of two pilot studies. These studies revealed that problems of eleven nodes provided the subjects with a challenging domain that encouraged the use of the decision aid. Moreover, as previously mentioned, when no decision aid or human-computer interchange protocol was imposed, subject debriefings and analysis of the pilot study data indicated that the behavior of the vast majority of participants was consistent with that of the best-first heuristic. For this reason, deviation from the best-first heuristic result was used as an indication of problem complexity.

## 4.6. Research Model

Mathematically, the research model can be summarized as

$$
y (i j k) = u + a (i) + b (j) + c (k) + b (j) c (k) + e (i j k)
$$

where $y(ijk)$ is the dependent variable, decision performance; u is the grand mean of $y(ijk)$ and is an unknown constant; $a(i)$ is the effect due to the i-th decision maker ( $i = 1, \ldots, 24$ ); $b(j)$ is the effect due to the j-th treatment ( $j = 1, \ldots, 4$ ); $c(k)$ is the effect due to problem complexity ( $k = 1, \ldots, 4$ ); $b(j)c(k)$ is the treatment by problem complexity interaction; and $e(ijk)$ is the random error associated with each of the 96 problem/treatment pairings.

In terms of the experimental design, each subject block included all treatments and levels of problem complexity. The 24 possible problem complexity orderings were paired with the 24 treatment orderings to produce an almost completely balanced design with respect to the main effects and interaction. The final design was completely ordered and balanced with regard to both treatment and problem complexity, and the interaction of these main effects resulted in deviations from the ideal of no more than one observation. A complete listing of the combinations is presented in the appendix.

## 4.7. Procedures

All treatments were applied in a single setting. Subjects began by completing a brief background questionnaire designed to collect demographic data. They were told that the performance objective was network route cost minimization (i.e., the traveling salesman problem) as well as the treatment characteristics and procedures to be followed during the experiment. Next they were randomly assigned to a microcomputer workstation that was programmed to execute one set of the 24 treatment/problem pairings. During each treatment, decision performance was automatically recorded. After the last treatment, exit interviews were held with each subject.

During the semester, students participated in two practice sessions using software and solving problems similar to those of the study. These practice sessions resulted in subjects who were very familiar with the keystrokes needed to add and delete line segments, and the general characteristics of the software. However, neither the final form of any one of the treatments nor the eleven-node problems of the study were ever introduced during these practice sessions. Nevertheless, the subjects were familiar with the objective, the treatment interfaces, and the procedures of the study before the actual collection of the data. These procedures may have resulted in improved human-only (control treatment) performance, thereby potentially underestimating treatment differences.

## 5. Analysis and Results

FIGURE 1 SHOWS THE MEAN DECISION PERFORMANCE SCORES by treatment. The stack bar chart compares the decision performance levels of subjects without an imposed problem-solving sequence (human), the underlying performance of the computer-based heuristic without human intervention (computer), and the performance of the imposed human-computer collaborative sequences (collaboration). Because the task objective is cost minimization of the route, the mean cost performance axis is inverted.

Figure 1 shows that the mean performance of both the dichotomous and the alternating cooperative treatments exceeds that of either the control or the critique treatments. Furthermore, the dichotomous and the alternating treatments' cooperative performance is significantly greater than that of the underlying computer-based heuristic decision aid (dichotomous, t = 2.47, p < .03; alternating, t = 3.04, p < .01). These results reflect a high level of participation on the part of the subjects. In 95 of the 96 treatment/problem pairings, subjects attempted to improve their performance by modifying their initial routing solution; this was in addition to their involvement in the development of these solutions.

To estimate the main effects and interaction term of the research model, a mixed general linear model was used. The treatments and problem complexity were both modeled as fixed effects, and the subject as a random effect. Estimates of the parameters of this model for the dependent variable decision performance are summarized in Table 1. Also shown are the type III sum-of-squares results for the main effects and interaction term.

These results show that once the variance explained by the user block and problem complexity effect is allocated, the treatments have a significant effect $p\text{-value} < .05$ on system performance. Based on this result, all pairwise treatment contrasts were computed. The mean differences and the 95 percent simultaneous Bonferroni confidence intervals for all six decision performance pairwise comparisons are presented in Table 2.

TREATMENTS

![](/api/attachments/Q6X432UK/fulltext/images/97be2c3812cf2f3279022ceb7608958a4ac921522b6710b238548df2a870cfd0.jpg)  
Figure 1. Mean Decision Performance by Treatment

The results of the treatment contrasts show the nature of the significant treatment effect. Specifically, the data show that both the dichotomous cooperative and the alternating cooperative treatments performed significantly better (i.e., a lower average route cost) than the control (human) treatment. However, no significant difference in decision performance was found between the control and the critique treatment. Collectively, the analysis of variance results, pairwise treatment contrasts, and the significant improvement in performance of the dichotomous and the alternating treatments over the underlying computer-based decision aid combine to reject hypothesis H 1.0. That is, human-computer collaboration, in the form of the alternating or the dichotomous treatment, performed significantly better than either the human (control) or the computer-based heuristic alone.

The pairwise contrasts also show that the difference in decision performance between either cooperative protocol (dichotomous and alternating treatments) and the critique treatment is significant. Because neither of these confidence intervals includes zero, H 2.0 can be rejected and we can conclude that decision performance using either the dichotomous or alternating cooperative treatment protocols is superior to that attained using the critique treatment.

Table 1 ANOVA for Decision Performance Effects

<table><tr><td>source</td><td>df</td><td>sum of squares</td><td>mean square</td><td>F-value</td><td>p&gt;F</td></tr><tr><td>Model</td><td>38</td><td>247,759.22</td><td>6,519.98</td><td>10.05</td><td>0.001</td></tr><tr><td>Error</td><td>57</td><td>36,992.28</td><td>648.99</td><td></td><td></td></tr><tr><td>Corrected Total</td><td>95</td><td>284,751.50</td><td></td><td></td><td></td></tr><tr><td>R-square</td><td></td><td>0.87</td><td></td><td></td><td></td></tr><tr><td>Coefficient of variation</td><td></td><td>4.52</td><td></td><td></td><td></td></tr><tr><td>Root mean square error</td><td></td><td>25.48</td><td></td><td></td><td></td></tr><tr><td>Source</td><td>df</td><td>Type III sum of squares</td><td></td><td>F-value</td><td>p&gt;F</td></tr><tr><td>User</td><td>23</td><td>23,508.91</td><td></td><td>1.57</td><td>0.084</td></tr><tr><td>Treatments</td><td>3</td><td>10,305.68</td><td></td><td>5.29</td><td>0.003</td></tr><tr><td>Problem complexity</td><td>3</td><td>201,097.25</td><td></td><td>103.29</td><td>0.001</td></tr><tr><td>Treatment * Problem</td><td>9</td><td>4,171.71</td><td></td><td>0.71</td><td>0.694</td></tr></table>

In addition, the results in Table 1 show no evidence of the hypothesized problem complexity by treatment interaction. Therefore, hypothesis H 3.0 cannot be rejected; problem complexity did not significantly affect the treatment's performance ranking. Across significantly different levels of problem complexity, the decision performance of the cooperative treatments (dichotomous and alternating) exceeded that of the critique and control treatments. Because differences in decision time might have contributed to this result, analysis of secondary data recorded during the study showed that decision time remained relatively constant across treatments and levels of problem complexity. Other reasons for this finding are discussed below.

## 6. Summary and Conclusions

BASED ON THE NOTION OF HUMAN-COMPUTER interchange protocols, the results of this study show that differences in the sequencing of the human-computer interchange affect decision performance. Specifically, the treatments that encouraged cooperation (dichotomous and alternating) performed significantly better than did either the control or the critique treatments. Within the limited domain of this study, when the human and the computer are encouraged to interact during the problem-solving process, their decision performance is better than that of either the computer application generating a solution that the human critiques and attempts to improve upon, or the human's solution unaided by the imposition of a specific interchange sequence with the computer-based support.

As with any empirical study, these results are limited to the range of the observations. The artificial nature of the setting, the student subjects' familiarity with both the treatments and the general class of problems to be solved, and the specifics of the decision setting and treatments must be evaluated in assessing the significance of these results. By design, the decision setting was restricted to eleven-node network routing problems, and decision making was limited to the generation, evaluation, and selection of alternative solutions. Problem complexity may also have been varied over too narrow a range for the data to show the anticipated effect on decision performance due to the interaction of the human-computer interchange protocols and problem complexity. $^{6}$ Moreover, as implemented in this study, the critique treatment required the human to review the computer application's suggested route, rather than the computer application evaluating the human's plan. The level of human-computer collaboration suggested by discussions of critique designs [14] is much greater than that implemented in this study. Despite these limitations, the results of this research suggest a number of recommendations.

Table 2 Pairwise Contrasts of Treatments within the Decision Performance Model

<table><tr><td rowspan="2">treatment contrast</td><td colspan="3">95% simultaneous Bonferroni confidence interval</td></tr><tr><td>lower limit</td><td>upper limit</td><td>difference between means</td></tr><tr><td>Control-Critique</td><td>-21.35</td><td>18.85</td><td>-1.25</td></tr><tr><td>Control-Dichotomous</td><td>3.23</td><td>43.44</td><td>23.33</td></tr><tr><td>Control-Alternating</td><td>6.46</td><td>46.67</td><td>26.56</td></tr><tr><td>Critique-Dichotomous</td><td>4.48</td><td>44.69</td><td>24.58</td></tr><tr><td>Critique-Alternating</td><td>7.71</td><td>47.92</td><td>27.81</td></tr><tr><td>Alternating-Dichotomous</td><td>-23.33</td><td>16.87</td><td>-3.23</td></tr></table>

The critical value for these confidence intervals is t = 2.73, with 57 degrees of freedom, a mean square error of 648.99, and a minimum significant difference between means of 20.10.  
Because the decision performance criterion is cost minimization, a positive difference between means indicates that the negative weighted treatment in the contrast vector outperformed (had a lower mean) the positive weighted treatment.

While it is too early to make specific design suggestions to the practitioner, it is clear that the sequence of interchange between the human and the computer application can significantly affect decision performance. Therefore, in addition to the interface display issues usually considered when designing decision-aiding systems, the human-computer interchange sequence must also be carefully evaluated. However, because neither the nature nor the full extent of this effect is known, more definitive design suggestions will require further investigation.

For the research community, this study raises several important issues. Chief among these is the identification of factors that significantly affect human-computer interchange and the holistic performance of the system. The degree to which the results of this study extend to other problems and types of inquiring systems also remains to be investigated. Questions include how do different types of inquiring systems [17] combine with human-computer interchange protocols to improve performance, and what are the characteristics of problems that make them amenable to human-computer joint problem-solving efforts? The imposition of structure by decomposing what otherwise are ill- or semi-structured problems has been discussed [22], and in light of the findings of this study more attention to this topic by MIS researchers seems warranted.

In closing, Licklider's concept of human-computer symbiosis requires combining the capabilities of the computer and the abilities of the human to produce a collaborative decision-making system. To encourage this collaboration, the notion of human-computer interchange protocols and their importance to system performance was proposed and developed. Based on the findings of this laboratory study, decision performance can be significantly improved by interchange sequences that encourage human-computer interaction during the problem-solving process.

## APPENDIX

<table><tr><td colspan="5">Order of Treatments and Problem Complexity in Experimental Design</td></tr><tr><td>Subject</td><td>Position 1</td><td>Position 2</td><td>Position 3</td><td>Position 4</td></tr><tr><td>1</td><td>Alternating,.06</td><td>Control,.12</td><td>Dichotomous,.18</td><td>Critique,.24</td></tr><tr><td>2</td><td>Alternating,.12</td><td>Control,.06</td><td>Critique,.18</td><td>Dichotomous,.24</td></tr><tr><td>3</td><td>Alternating,.18</td><td>Dichotomous,.06</td><td>Control,.24</td><td>Critique,.12</td></tr><tr><td>4</td><td>Alternating,.24</td><td>Dichotomous,.18</td><td>Critique,.12</td><td>Control,.06</td></tr><tr><td>5</td><td>Alternating,.24</td><td>Critique,.06</td><td>Control,.18</td><td>Dichotomous,.12</td></tr><tr><td>6</td><td>Alternating,.06</td><td>Critique,.24</td><td>Dichotomous,.12</td><td>Control,.18</td></tr><tr><td>7</td><td>Control,.06</td><td>Alternating,.12</td><td>Dichotomous,.24</td><td>Critique,.18</td></tr><tr><td>8</td><td>Control,.12</td><td>Alternating,.18</td><td>Critique,.06</td><td>Dichotomous,.24</td></tr><tr><td>9</td><td>Control,.18</td><td>Dichotomous,.24</td><td>Alternating,.12</td><td>Critique,.06</td></tr><tr><td>10</td><td>Control,.24</td><td>Dichotomous,.18</td><td>Critique,.06</td><td>Alternating,.12</td></tr><tr><td>11</td><td>Control,.18</td><td>Critique,.12</td><td>Alternating,.24</td><td>Dichotomous,.06</td></tr><tr><td>12</td><td>Control,.18</td><td>Critique,.24</td><td>Dichotomous,.06</td><td>Alternating,.12</td></tr><tr><td>13</td><td>Dichotomous,.06</td><td>Alternating,.18</td><td>Control,.12</td><td>Critique,.24</td></tr><tr><td>14</td><td>Dichotomous,.12</td><td>Alternating,.24</td><td>Critique,.06</td><td>Control,.18</td></tr><tr><td>15</td><td>Dichotomous,.12</td><td>Control,.06</td><td>Alternating,.24</td><td>Critique,.18</td></tr><tr><td>16</td><td>Dichotomous,.24</td><td>Control,.12</td><td>Critique,.18</td><td>Alternating,.06</td></tr><tr><td>17</td><td>Dichotomous,.18</td><td>Critique,.12</td><td>Alternating,.06</td><td>Control,.24</td></tr><tr><td>18</td><td>Dichotomous,.12</td><td>Critique,.18</td><td>Control,.24</td><td>Alternating,.06</td></tr><tr><td>19</td><td>Critique,.06</td><td>Alternating,.18</td><td>Control,.24</td><td>Dichotomous,.12</td></tr><tr><td>20</td><td>Critique,.12</td><td>Alternating,.24</td><td>Dichotomous,.18</td><td>Control,.06</td></tr><tr><td>21</td><td>Critique,.18</td><td>Control,.06</td><td>Alternating,.12</td><td>Dichotomous,.24</td></tr><tr><td>22</td><td>Critique,.24</td><td>Control,.12</td><td>Dichotomous,.06</td><td>Alternating,.18</td></tr><tr><td>23</td><td>Critique,.06</td><td>Dichotomous,.24</td><td>Alternating,.18</td><td>Control,.12</td></tr><tr><td>24</td><td>Critique,.24</td><td>Dichotomous,.06</td><td>Control,.12</td><td>Alternating .18</td></tr></table>

## NOTES

3. The evidence suggests that “modest variations in response time (plus or minus 50 percent of the mean) appear to be tolerable and have little impact on user performance” [21, pp. 302–3]. According to Shneiderman [21, p. 304], the effect of display rate seems to depend upon whether or not the material being printed must be read. If the full text must be read, display rates that are faster than reading speed may be counterproductive, unless the entire screen can be filled virtually instantaneously. However, if reading the full text is not required, fast display rates may speed task completion but lead to more errors.

4. Best-first, also known as shortest-path, is derived from Dijkstra's [5] minimum spanning tree algorithms.

5. An eleven-node network routing problem requires of order 11! iterations to examine all possible solutions.

6. One may argue that our implementation of problem complexity was closer to the concept of problem difficulty; however, the empirical literature does not seem to make a distinction between these two [4]. A comprehensive review and analysis of task complexity can be found in Campbell [1].

## REFERENCES

1. Campbell, D. J. Task complexity: a review and analysis. Academy of Management Review, 13, 1 (1988), pp. 40–52.

2. Courtney, Jr., J. F.; Paradice, D. B.; and Ata Mohammed, N. H. A knowledge-based DSS for managerial problem diagnosis. Decision Sciences, 18, 3 (1987), pp. 373–399.

3. DeSanctis, G. Computer graphics as decision aids: directions for research. Decision Sciences, 15, 4 (1984), pp. 463–487.

4. Dickson, G. W.; DeSanctis, G.; and McBride, D. J. Understanding the effectiveness of computer graphics for decision support: a cumulative experimental approach. Communications of the ACM, 29, 1 (1986), pp. 40–47.

5. Dijkstra, E. W. A note on two problems in connexion with graphs. Numerische Mathematik, 1 (1959), pp. 269–271.

6. Ellis, A., and Beattie, G. The Psychology of Language and Communication. New York: Guilford Press, 1986.

7. Ginzberg, M. J., and Stohr, E. A. Decision support systems: issues and perspectives. In Ginzberg, M. J.; Reitman, W. R.; and Stohr, E. A. (eds.), Decision Support Systems. Amsterdam: North-Holland, 1982, pp. 9–31.

8. Henderson, J. C. Finding synergy between decision support systems and expert systems research. Decision Sciences, 18, 3 (1987), pp. 333–349.

9. Hollnagel, E.; Mancini, G.; and Woods, D. D. Intelligent Decision Support in Process Environments. NATO ASI Series. Berlin: Springer-Verlag, 1986.

10. Hollnagel, E., and Woods, D. D. Cognitive systems engineering: new wine in new bottles. International Journal of Man-Machine Studies, 18, 6 (1983), pp. 583–600.

11. Howard, R. A. Decision analysis: practice and promise. Management Science, 34, 6 (1988), pp. 679–695.

12. Ives, B.; Hamilton, S.; and Davis, G. A framework for research in computer-based management information systems. Management Science, 26, 9 (1980), pp. 910–933.

13. Keen, P. G. W., and Scott Morton, M. S. Decision Support Systems: An Organizational Perspective. Reading, MA: Addison-Wesley, 1978.

14. Langlotz, C. P., and Shortliffe, E. H. Adapting a consultation system to critique user plans. International Journal of Man-Machine Studies, 19, 5 (1983), pp. 479–496.

15. Licklider, J. C. R. Man-computer symbiosis. IRE Transactions on Human Factors in Electronics, Vol. HFE-1, No. 1 (1960), pp. 4–11.

16. Luconi, F. L.; Malone, T. W.; and Scott Morton, M. S. Expert systems: the next challenge for managers. Sloan Management Review, 27, 4 (1986), pp. 3–14.

17. Mason, R. O., and Mitroff, I. I. A program for research on management information systems. Management Science, 19, 5 (1973), pp. 475–487.

18. Montazemi, A. R., and Wang, S. The effects of modes of information presentation on decision making: a review and meta-analysis. Journal of Management Information Systems, 5, 3 (1989), pp. 100–127.

19. Paradice, D. B., and Courtney, Jr., J. F. Controlling bias in user assertions in expert decision support systems for problem formulation. Journal of Management Information Systems, 3, 1 (1986), pp. 52–64.

20. Peace, D. M. S., and Easterby, R. S. The evaluation of user interaction with computer-based management information systems. Human Factors, 15, 2 (1973), pp. 163–177.

21. Shneiderman, B. Designing the User Interface: Strategies for Effective Human-Computer Interaction. Reading, MA: Addison-Wesley, 1987.

22. Simon, H. A. The structure of ill structured problems. Artificial Intelligence 4 (1973), pp. 181–201.

25. Targowski, A. S., and Bowman, J. L. The layer-based, pragmatic model of the communication process. The Journal of Business Communication, 25, 1 (1988), pp. 5–24.

26. Turban, E., and Watkins, P. R. Integrating expert systems and decision support systems. MIS Quarterly, 10, 2 (1986), pp. 121–136.

27. Wisudha, A. D. Design of decision-aiding systems. In Wright, G. (ed.), Behavioral Decision Making. London: Plenum Press, 1985, pp. 235–256.

28. Woods, D. D. Paradigms for intelligent decision support. In Hollnagel, E.; Mancini, G.; and Woods, D. D. (eds.), Intelligent Decision Support in Process Environments. NATO ASI Series. Berlin: Springer-Verlag, 1986, pp. 153–173.

29. Woods, D. D. Cognitive technologies: the design of joint human-machine cognitive systems. The AI Magazine, 4, 4 (Winter 1986), pp. 86–92.
