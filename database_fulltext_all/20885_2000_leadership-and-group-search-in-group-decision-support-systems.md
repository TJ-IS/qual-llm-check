---
otero_id: 20885
otero_key: "Y2XZRA2E"
title: "Leadership and group search in group decision support systems"
authors: "Jackie Rees; Gary J Koehler"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00090-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Leadership and group search in group decision support systems

Jackie Rees <sup>a,)</sup>, Gary J. Koehler <sup>b,1</sup>

Krannert Graduate School of Management, Purdue UniÕersity, West Lafayette, IN 47907-1310, USA <sup>b</sup> Department of Decision and Information Sciences, Warrington College of Business Administration, UniÕersity of Florida, 351 Stuzin Hall, GainesÕille, FL 32611, USA

Received 1 January 2000; accepted 1 April 2000

## Abstract

Groups using group decision support systems GDSS for addressing organizational problems is an evolutionary process.Ž . An analytical model incorporating evolutionary processes exists, capturing this adaptation in the group decision-making process. This model is based on the genetic algorithm GA and can be used to estimate GA parameter values fromŽ . experimental data. This research effort examines possible relationships between the GA crossover and mutation parameters and the group context variables of leadership. Both the presence of and the activity level of group leaders are considered. Particular attention is paid to model implementation for a specific instance of GDSS use. The results of this effort are generally encouraging, hinting at the need to conduct further research in this area. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: GDSS; Genetic algorithms; Leadership; Computational model

## 1. Introduction

The organizations of today face many challenges in an increasingly complex and global business environment. To meet these challenges, the combination and coordination of the talents and energies of many members of the organizations are needed. Group meetings are the obvious outcome of the need to meet this challenge. However, group meetings are frequently maligned, often rightly so. According to one estimate, senior-level managers spend from 58% to 70% of their work time in meetings 5 . Of<sup>w</sup> <sup>x</sup> particular interest are group meetings supported by computer technology. One implementation of computer-supported group work for decision making is group decision support systems GDSS . GDSS are aŽ . specific combination of technologies aimed at improving the outcomes of group meetings. The purpose of GDSS is A . . . to support the exchange of ideas, opinions, and preferences within the groupB <sup>w</sup> <sup>x</sup> 8 p. 278 . Many researchers have found that the Ž . introduction of technology strongly impacts meeting outcomes 22 . However, the strength and direction<sup>w</sup> <sup>x</sup> Ž . improved vs. diminished decision quality of this impact is variable across studies and is poorly understood. Therefore, a model that provides better insights and eventually predictive capabilities would be highly desirable to researchers and practitioners alike.

Within the GDSS context, group meetings to address and solve organizational issues and problems can be considered an evolutionary process 13 . A<sup>w</sup> <sup>x</sup> model for GDSS, incorporating such evolutionary processes, was proposed by Rees and Koehler 26 .<sup>w</sup> <sup>x</sup> This model utilized a genetic algorithm GA as anŽ . analogy for the decision-making process undertaken by the groups. The model is based on the premise that groups using GDSS are undertaking a search process 9,27 and exhibit search strategies similar to <sup>w</sup> <sup>x</sup> those found in GA search strategies.

A group generates ideas, proposals, and solutions to a given problem and reacts to the current slate of proposed solutions to generate new ones. Often the new proposals are adaptations of current ones. This adaptive capability captures one of the basic principles of group decision making put forth by Hirokawa and Johnson 13 that <sup>w</sup> <sup>x</sup> Agroup decision making is an evolutionary process.B Other times proposed solutions are completely unexpected and cause the group to explore whole new areas of the problem’s decision space. Gavish and Kalvenes 9 call this a<sup>w</sup> <sup>x</sup> trigger phenomenon.

GAs appear to operate similarly. Current solutions provide the seeds for the next population of proposed solutions through recombination operators. GAs also exhibit punctuated equilibria where a seemingly stable system suddenly evolves new genetic material, mainly through mutation operators.

Provided that a group decision process can be adequately mimicked by a GA, there exist several potential advantages and implications. For example, GAs are known to have an exact expected behavior described by a Markov chain MC 30 . In principle,Ž . <sup>w</sup> <sup>x</sup> one can compute many properties from an MC, such as the expected first passage times from a set of states to a target set of states and the probabilities of various outcomes. Interpreted in a GDSS setting, such calculations can tell us the expected time till an optimal solution is generated, the expected time for consensus to appear, the expected number of new ideas, the probability of novel Aleft fieldB ideas, and more. To the extent the GA captures the dynamics of the actual GDSS process, these same values would represent the group s performance.

Another implication is that of the Astand inB GA incorporated into GDSS software. The Astand inB GA can be used in parallel while the group is solving a problem, possibly supplying and being supplied Ž . solutions to by the group. It can be used to con- Ž . tinue and refine a search process started by the actual group. It could be used as a complete replacement for the group.

The GA parameters of crossover and mutation influence the course of the search by focusing the search in particular regions of the search space and by providing random AjumpsB to other regions that possibly contain potential solutions but have not been actively explored.

Although a priori GA parameters were not linked to specific GDSS context variables such as leadership, one may be able to relate such factors and different environmental pressures thought to influence the process to GA parameters a posteriori. Then, knowing how GA parameters influence various performance measures from formal GA theory, one could optimize these by altering the GDSS design and usage. Even if one could not directly optimize these performance measures, there exists a large body of heuristic knowledge available in the GA community for the GA to improve its search capabilities, which could be used indirectly to set GDSS design and usage through these GDSS–GA parameter relations.

Hence, one question of interest is: do relationships exist between GA search parameters and GDSS context variables? Many research studies have examined the effect of GDSS variables, for example leadership 11,16,28 , anonymity 14,15 and group <sup>w</sup> <sup>x</sup> <sup>w x</sup> size 7 on GDSS outcomes. As the GA search parameter values have various effects on the outcomes of GA search, it would be most useful to determine the existence and extent of possible relationships between GA parameter values and GDSS context variables. If these relationships do exist, more could be learned about appropriate computersupported group configurations in order to achieve desired decision outcomes.

Leadership has been identified as an important contextual variable by GDSS researchers. The presence of a leader has been hypothesized to increase the consensus among groups using GDSS 11 . Stud-<sup>w</sup> <sup>x</sup> ies of non-GDSS supported groups have found that small groups with leaders are less likely of split into factions or subgroups 6 and leaders are useful in<sup>w</sup> <sup>x</sup> order to achieve task-oriented goals 3 . As leader-<sup>w</sup> <sup>x</sup> ship appears to have an impact on the outcomes of GDSS use, it seems likely that leadership influences the search process undertaken by groups using GDSS.

The goal of this research is to examine the possible link between leadership presence and participation in GDSS and the GA parameters of crossover and mutation rates within the context of the evolutionary model. Section 2 provides a look into the study of leadership within the GDSS context and also relevant literature pertaining to the GA parameters under consideration. Section 3 highlights the evolutionary model providing the context for the study. Section 4 puts forth several research questions examining the relationships among GDSS leadership from two angles, the ApresenceB of a designated leader and the actual interaction of the leaders with the other group members. Methodological details are provided in Section 5. Results are discussed in Section 6. Sections 7 and 8 present conclusions and future research directions, respectively.

## 2. Background

The following section provides a brief background on the role of leadership in GDSS. The simple GA will also be discussed in detail in order to provide perspective on the potential relationships between leadership in GDSS and GA parameters.

## 2.1. Leadership in GDSS

Leadership has been extensively studied in the small group literature 2 . Several studies have exam- <sup>w</sup> <sup>x</sup> ined the role of leadership in GDSS 1,11,17 . Addi- <sup>w</sup> <sup>x</sup> tionally, several GDSS studies have examined the impacts of not only the presence or absence of leadership on GDSS group outcomes but also the impacts of leadership style on GDSS outcomes <sup>w</sup> <sup>x</sup> 16,28 . Leadership style is very difficult to describe or classify and certainly difficult to effectively measure, due to it’s multidimensional characteristics. Moreover, leaders can exhibit different leadership styles at various times 2 . However, leadership style <sup>w</sup> <sup>x</sup> and its appropriateness to the particular scenario involved can leave a deep imprint on the effectiveness of the GDSS group outcome.

Also important is the context within which GDSS processes are examined. There are several useful models in the literature. Several of these models are descriptive models, including the contingency model <sup>w x</sup> <sup>w x</sup> 25 , the theory of Adaptive Structuration 24 and the input–process–output model 23 . In addition, <sup>w</sup> <sup>x</sup> several analytical models have been proposed. These models include the brainstorming model 29 and the <sup>w</sup> <sup>x</sup> economic model 9 . These models are the precursors<sup>w</sup> <sup>x</sup> to the evolutionary model, based on the simple GA discussed below 26 .<sup>w</sup> <sup>x</sup>

## 2.2. GAs

GAs are derived from the principles of Darwinian natural selection and evolution. Rather than searching point by point, GAs operate in parallel, searching by groups or populations of points or agents. Such agents, called strings or chromosomes, conduct a search by means of three basic operations. These three operations are selection, crossover and mutation. Selection, or reproduction, stochastically collects the AfittestB members of the population according to a pre-defined objective function for use in the next population or generation. Crossover pairs off the members of the new generation and exchanges genetic material between member pairs. Finally, mutation randomly alters information contained in the population members adding diversity back into the population 10 .<sup>w</sup> <sup>x</sup>

The GA crossover and mutation operations play a guiding role in genetic search. The crossover rate, , is a AfocusingB factor in the search process. Two selected strings are AcrossedB with probability . Every pair of strings that are crossed-over have been selected according to its AfitnessB. On average, the crossover operator combines two very good solutions into potentially even better solutions. In a search space with global optima, the better solutions are likely to be proximately located. The crossover operation attempts to focus search and move even closer to an optimal point. For this reason, the crossover parameter is often termed the AexploitationB operator.

On the other hand, the mutation rate, , plays a AdiversifyingB role in genetic search. Mutation operates on each bit in the string. A given bit is mutated with probability . The mutation rate is usually set to be very low, for example, 0.1% of all bits in all of the strings might be subject to mutation. If a particular bit is mutated the value of the bit would be altered, from a zero to a one or vice versa. The purpose of the mutation operation is to add either strings that were Aselected outB of the population back or to introduce new strings. Mutation serves to direct the search away from local minima or maxima. For this reason, the mutation operator is often termed the AexplorationB operator.

Nix and Vose 21 developed an MC model for<sup>w</sup> <sup>x</sup> the simple GA. Each state of the MC represents a population of the GA, providing an exact representation for the expected populations of a GA over time. This model forms the basis for the evolutionary model for GDSS.

## 3. Evolutionary model for GDSS

Several research projects have examined the evolutionary characteristics of systems by creating a simulation environment where a GA is used to mimic the behavior of some agent or group of agents. For example, organizational evolution was modeled using the simple GA 4 . Also, market behavior was<sup>w</sup> <sup>x</sup> studied through GA simulation 18 .<sup>w</sup> <sup>x</sup>

The evolutionary model for group problem solving, when supported by GDSS, can be modeled by a simple GA, utilizing selection, crossover and mutation 26 . The essence of the model is to capture the<sup>w</sup> <sup>x</sup> adaptive search process undertaken by each group as it uses the GDSS for decision-making. The mechanics of the model are discussed below.

The group’s collection of the proposed ideas or solutions is represented by a population of strings; each string in the population at time step t represents a current proposed solution at time t. The sizes of these populations are variable and are a function of the interaction between group members. The fitness of proposed ideas can be determined through the use of incentive schemes or through the results of any polling of voting procedures which may be a function of the particular GDSS software used. Selection, crossover and mutation operate as described above. As the generations evolve, the GA finds either the best or at least a very good solution with high Ž probability . GDSS supported groups can be viewed . as generating solutions using a mechanism that can be modeled in this way.

The purpose of the selection operator is to identify better or AfitterB solutions in accordance with the fitness function and insert these strings into the next generation. Ensuring the Asurvival of the fittestB is the role of the selection operator. The specific implementation of selection may vary from application to application and from task to task . However, rankŽ . selection appears to be a generally robust selection operation. Rank selection, considered a non-parametric procedure, sorts the strings in the population according to fitness value. Copies of individual strings are inserted into the next generation according to a function of the original ranking. Essentially, the higher-ranked the idea, the more likely it will influence subsequent generations.

The crossover and mutation operators are implemented as follows: for crossover, two strings are mated with probability  Ž . the crossover rate . Uniform crossover appears to be a fairly good implementation choice for the evolutionary model for GDSS 26 . Uniform crossover works by moving <sup>w</sup> <sup>x</sup> bit-wise down the pair of strings, exchanging bits with probability . The appeal of uniform crossover is the ability to exchange a variable number of information segments between the string pairs, which is a more dynamic approach than either single-point or multi-point crossover 10 . Uniform mutation is<sup>w</sup> <sup>x</sup> the implementation of the mutation operator 26 . <sup>w</sup> <sup>x</sup> Under uniform mutation, mutation is applied with a fixed, pre-determined probability to each gene eachŽ bit in every solution string. The mutation rate is. kept very low, usually between 0.001 and 0.5 to prevent the search from diversifying too rapidly.

One of the attractive features of using a GA for the analysis of computer-supported group decisionmaking is a body of formal, mathematical theory has been developed to describe the expected behavior of the simple GA. By modeling groups using GDSS for particular tasks as a GA, this theory provides numerous insights into the group decision-making process. Variables and different environmental pressures thought to influence the process could be related to GA parameters and then factors such as the expected behavior of the system could be determined or optimized.

This model differs from the previous examples of using a GA to study systems in that rather than simulate the groups used in Barkhi’s study 1 , the<sup>w</sup> <sup>x</sup> historical data was used to find a best-fit GA. The MC model used was derived from the model proposed by Vose 30 that gives transition probabilities to determine a likelihood function for the probabilities of each group’s particular path through the solution space. The maximum likelihood estimates Ž . MLEs for these paths were calculated over all possible values of mutation 0, 0.5 and crossover 0, Ž . Ž 1.0 with 3-digit precision. Therefore, a best-fit mu- . tation and crossover rate for each group was estimated, given the assumption that each group acted like a simple GA.

## 4. Research questions

The idea that groups using GDSS behave similarly to those using GA was discussed extensively by Rees and Koehler 26 . Therefore, the research ques-<sup>w</sup> <sup>x</sup> tions posed in this section assume a simple GA model as the basis of group dynamics. The questions posed in this section try to explore the possible relationship between the GA parameters  and $\mu ,$ and two dimensions GDSS context variables of leadership presence and style.

In this research, we use the same conceptual base of leadership as used previously 17,1 , that of leader influence and group cohesion. Groups with a designated leader will tend to produce solutions deemed as potentially acceptable to the leader. Therefore, less exploration of alternative solutions will likely take place. Hiltz et al. 11 hypothesized that the <sup>w</sup> <sup>x</sup> presence of a leader increases the consensus among groups using GDSS. Studies of non-GDSS supported groups have found that small groups with leaders are less likely of split into factions or subgroups 6 and<sup>w</sup> <sup>x</sup> that leaders are useful in order to achieve task-oriented goals 3 . Conversely, democratic groups <sup>w</sup> <sup>x</sup> Ž . groups without a leader will tend to explore the solution space more actively since it might seem easier to convince another manager of an alternative solution than a superior. This gives us,

Hypothesis 1 Ž . H1a . Autocratic groups will propose less explorative solutions than democratic groups as measured by the maximum likelihood of each group’s mutation rate.

We test H1a by comparing the best-fit mutation rate $\mu$ between the autocratic groups and democratic groups. We believe $\mu$ will be smaller for autocratic groups than for democratic groups because the autocratic groups are less likely to actively explore various regions of the solution space, due to the less exhaustive search undertaken, than democratic groups.

Using the mutation rate, , as a measure of exploration, we would expect that autocratic groups would tend to refine solutions deemed acceptable to the leader, rather than propose radically different alternatives. The group members all had access to decision tools discussed below which provided in- Ž . stant feedback to the increased revenue or cost of a proposed solution. This instant feedback ensures that all solutions proposed are feasible according to the problem constraints. However, the search space is still large enough to allow for considerable differences among proposed solutions. These differences can be measured by their so-called AdiversityB. GA research has concerned itself extensively with the concept of Hamming distance 10 . Mitchell 20<sup>w x</sup> <sup>w x</sup> defines Hamming distance as the number of locations or genes at which the corresponding values or bits differ. Other such distance measures are possible, however Hamming distance represents the simplest and most widely used distance measure for complex search spaces in GA literature. This leads to,

HYPOTHESIS 1 Ž . H1b . Autocratic groups will have lower solution diversity than democratic groups as measured by each group’s average Hamming distance.

We measure solution diversity, , as the distance between the solutions, or points, in the solution space. We compute the average Hamming distance for each group’s solutions by computing the Hamming distance between every pair of solutions in the group and summing up all of the distances. This sum is then divided by the number of solution pairs in the group to create an average diversity level for each group. As $\varDelta$ becomes small, the best fit $\chi$ should also become small. As there is less diversity within the group, the crossover rate, or the rate at which ApartsB of proposals or ideas are exchanged, will become small, as most of the proposals are already identical. As autocratic groups experience less diversity, there should be a lower rate of exchange of proposals, or at least components of proposals. Correspondingly, and should both be larger for democratic groups. This leads to,

HYPOTHESIS 1 Ž . H1c . If there is little or no diversity within the groups, autocratic groups will experience a lower rate of exchange of ideas or proposals than democratic groups as measured by the maximum likelihood estimate of each group’s crossover rate.

We test this hypothesis by comparing  between autocratic and democratic groups. Assuming that diversity is lower for autocratic groups as proposed in H1b,  should be lower for autocratic groups than for democratic groups.

To further study the effect of leadership on GA parameters, we examined the level interaction of the leaders with the other group members. By examining leader interaction we can gain insights into the leadership style of the group leaders. As mentioned previously, leadership style is difficult to describe or measure, due to its inherent multidimensionality. For our purposes, we classified leadership style into two broad categories: directive Active and passive In-Ž . Ž active . The experimental groups were partitioned. into the two categories by using an equality measure similar to the equality of participation measure proposed in Hiltz et al. 12 . The number of ideas <sup>w</sup> <sup>x</sup> proposed by the leaders was compared to the number of ideas proposed by rest of the group members. If all group members, including the leader, are participating equally each group member should contribute roughly one-fourth 25% of the ideas generated.Ž . However, the leader’s role is different from the roles of the other functional managers, specifically the leader’s role is to maximize the welfare of the organization while the other managers’ role is to maximize the welfare of their individual departments, within the organization. Therefore, leaders might not contribute an equal number of solutions to the entire ApoolB. Some leaders will take on an active level of participation whereas others will assume an inactive participation level. Using data from Barkhi 1 , approximately one half of the groups had<sup>w</sup> <sup>x</sup> leaders that contributed less than one quarter of the ideas and one half of the leaders contributed one quarter of the ideas or more. We designated the lower participation leaders as Inactive leaders and the higher output leaders as Active leaders. This information is provided in Table 1. In accordance with H1a, the Active leaders will act to narrow the direction of the search for a solution. However, this active approach should also act to encourage a thorough search in hopes of finding the optimal solution for the organization. Therefore we believe,

Leader classification according to idea contribution percentage by group

<table><tr><td>Leader ideas</td><td>Total group ideas</td><td>Leader (%)</td><td>Leader style</td></tr><tr><td>12</td><td>26</td><td>0.461</td><td>Active</td></tr><tr><td>4</td><td>19</td><td>0.211</td><td>Inactive</td></tr><tr><td>2</td><td>25</td><td>0.080</td><td>Inactive</td></tr><tr><td>3</td><td>11</td><td>0.273</td><td>Active</td></tr><tr><td>9</td><td>24</td><td>0.375</td><td>Active</td></tr><tr><td>5</td><td>16</td><td>0.313</td><td>Active</td></tr><tr><td>2</td><td>11</td><td>0.182</td><td>Inactive</td></tr><tr><td>4</td><td>18</td><td>0.222</td><td>Inactive</td></tr><tr><td>6</td><td>18</td><td>0.333</td><td>Active</td></tr><tr><td>1</td><td>11</td><td>0.091</td><td>Inactive</td></tr><tr><td>1</td><td>10</td><td>0.100</td><td>Inactive</td></tr><tr><td>2</td><td>17</td><td>0.118</td><td>Inactive</td></tr><tr><td>6</td><td>14</td><td>0.429</td><td>Active</td></tr><tr><td>8</td><td>18</td><td>0.444</td><td>Active</td></tr><tr><td>7</td><td>18</td><td>0.389</td><td>Active</td></tr><tr><td>3</td><td>12</td><td>0.250</td><td>Inactive</td></tr><tr><td>3</td><td>18</td><td>0.167</td><td>Inactive</td></tr><tr><td>3</td><td>15</td><td>0.200</td><td>Inactive</td></tr><tr><td>15</td><td>26</td><td>0.577</td><td>Active</td></tr><tr><td>5</td><td>19</td><td>0.263</td><td>Active</td></tr><tr><td>2</td><td>17</td><td>0.118</td><td>Inactive</td></tr><tr><td>5</td><td>15</td><td>0.333</td><td>Active</td></tr><tr><td>4</td><td>12</td><td>0.333</td><td>Active</td></tr></table>

HYPOTHESIS 2 Ž . H2a . Groups with Active leaders will propose more explorative solutions than groups with Inactive leaders as measured by the maximum likelihood estimate of each group’s mutation rate.

This hypothesis will be tested by comparing the best-fit mutation rate between the two leadership-type groups. Similarly, the level of solution diversity should be higher for the Active leaders than the Inactive leaders. This leads to,

HYPOTHESIS 2 Ž . H2b . Groups with leaders classified as Active will have a higher solution diversity than groups with leaders classified as Inactive as measured by each group’s average Hamming distance.

The level of diversity, , therefore should be lower for Inactive groups than Active groups. As previously mentioned, as  becomes small,  should also become small for Inactive leader groups. Correspondingly,  and  should both be larger for Active leader groups. This leads to,

HYPOTHESIS 2 Ž . H2c . If there is little or no diversity within the groups, Active-leader groups will experience a higher rate of exchange of ideas or proposals than Inactive-leader groups as measured by the maximum likelihood estimate of each group’s crossover rate.

## 5. Model details

In order to address the research questions, experimental data from actual computer-supported group decision-making was required. The experimental data was provided by Barkhi 1 where groups were faced<sup>w</sup> <sup>x</sup> with a mixed-motive task 19 by which group mem-<sup>w</sup> <sup>x</sup> bers had to coordinate the final solution in the face of conflicting pay-off information. In that study, incentive structure, leadership presence and communications channel were varied. Groups were constructed such that each member represented a different department within a simulated manufacturing environment, the departments being labeled as production, purchasing and marketing. Some of the groups in the study were comprised of the three members labeled as above and the others were comprised of four members the previous three plus a Ž designated AleaderB who had override power on all decisions made within the group . The group was . assigned a combinatorial problem with a calculated payoff for each member.

In order to examine the effects of leadership presence and leadership style, the crossover and mutation rates had to be estimated from the data using the MC model for GAs 21 . In order to use the<sup>w</sup> <sup>x</sup> model, the problem and data from group experiments was encoded as follows. Each string in the population represented a set of orders to be filled as proposed by a manager or the leader in a specific generation. Each string was composed of twenty binary digits, each representing the inclusion or Ž exclusion of a customer order by a one or zero .. Ž .

A population consists of a number of solutions. The number will vary from episode to episode, but there is no AnaturalB demarcation for computer-supported groups. Such groups can be modeled as having a dynamic population size. Four different schemes were originally examined for modeling the populations 26 .<sup>w</sup> <sup>x</sup>

For this study, the Peer-Influenced population scheme was utilized. The scheme treats the inputs of all users equally, due to the unknown levels of influence the leaders might have over other group members. The scheme is implemented as follows. The GA population size expands or contracts de-Ž . pending upon the frequency of group member interaction. Each generation is delineated by the proposal of a solution from a different user. For example, in a group of size four, the marketing manager might propose a solution. After some thought and no input from other participants, the marketing manager proposes a slightly altered solution. The production manager then adds his solution. This suggestion marks the entirety of the population and its size is three. If the purchasing manager then suggests a solution, followed by another solution from the production manager, that population size is two. It is worthwhile to note that this strategy relies not on the timing of the solutions but on the interaction of the different group member’s solutions ideas . Theoreti-Ž . cally, it might be preferable to close each generation after input has been made by all four participants. However, due to group interaction dynamics, it is possible that one or more managers might engage in freeloading behaviors and artificially influence the creation and sizing of generations.

## 6. Results

Hypothesis H1a stated that autocratic groups are likely to propose a less explorative search than democratic groups. To test this hypothesis, we compared the best-fit mutation rates between autocratic and democratic groups. In order to not reject this hypothesis, autocratic groups must have a smaller $\mu$ than democratic groups. This difference was weakly significant at $\alpha = 0 . 1 0 \textrm { } \left( p = 0 . 0 7 2 \right)$ . These results are reported in Table 2.

Hypothesis H1b states that autocratic groups are likely to have lower solution diversity than democratic groups, where solution diversity is measured by . This hypothesis was not rejected at $\alpha = 0 . 0 5$

Hypothesis H1c examines the relationship between the crossover rates of the two groups. H1c states if is close to zero, meaning there is little diversity within the groups, autocratic groups are likely to experience a lower rate of exchange of ideas or proposals than democratic groups. In order to not reject this hypothesis, autocratic groups must have a lower best-fit crossover rate than democratic groups. This difference was significant at $\alpha = 0 . 1 0$ but again not strongly so $( \boldsymbol { p } = 0 . 0 5 8 )$

Hypothesis H2a examined a specific aspect of leadership style as described above on the GA parameter mutation. H2a stated that groups with leaders classified as Active are likely to propose a more explorative search than groups with leaders classified as Inactive. We do not reject this hypothesis at $\alpha = 0 . 1 0$ but was not strongly significant $( p =$ 0.081 . The results are presented in Table 3..

Hypothesis H2b stated Active leader groups would have a higher  than Inactive leader groups. This hypothesis was not supported. In fact,  was higher for Inactive leader groups than Active leader groups. Active leader groups had a much lower then Inactive Leader groups. The results are listed in Table 3.

Hypothesis H2c stated that if diversity is low within the groups, Inactive leader groups should have a lower  than Active leader groups. This hypothesis was not rejected and was significant at $\alpha = 0 . 1 0$ but not strongly so $( \boldsymbol { p } = 0 . 0 5 1 )$ .

Table 2  
Results of statistical tests on leadership hypotheses

<table><tr><td>Hypothesis</td><td>Autocratic mean</td><td>Democratic mean</td><td>Results</td></tr><tr><td>H1a</td><td>0.018</td><td>0.028</td><td>0.072; do not reject H1a</td></tr><tr><td>H1b</td><td>0.807</td><td>1.258</td><td>0.017; do not reject H1b</td></tr><tr><td>H1c</td><td>0.092</td><td>0.223</td><td>0.058; do not reject H1c</td></tr></table>

Table 3  
Results of statistical tests on leadership style hypotheses

<table><tr><td>Hypothesis</td><td>Active mean</td><td>Inactive mean</td><td>Results</td></tr><tr><td>H2a</td><td>0.023</td><td>0.011</td><td>0.081; do not reject H2a</td></tr><tr><td>H2b</td><td>0.690</td><td>0.960</td><td>0.035; reject H2b(Active &lt; Inactive)</td></tr><tr><td>H2c</td><td>0.149</td><td>0.017</td><td>0.051; do not reject H2c</td></tr></table>

## 7. Conclusions

Several conclusions can be drawn from the above results. Our experiments found significant results at the $\alpha = 0 . 1 0$ level for the effect of leadership presence on the GA parameters of mutation and crossover as well as solution diversity. Thus, we have tentatively established a link between the presence of leadership and the exploration of the search space as measured by the GA parameters.

By further breaking down leadership into two leadership participation levels, the outcomes were somewhat confused. We hypothesized that Active leader groups would encourage a broader search than Inactive leader groups. This hypothesis was supported. However, the average diversity of the solutions was lower for Active leader groups. This seems to contradict the finding of higher levels of exploitation found within Active leader groups. Obviously, much more work needs to be performed to fully understand the relationships between leadership approach and the GA parameters examined here.

The important implication of this study is that there does appear to be differences in the searches performed by democratic and autocratic groups, as measured by the estimated crossover and mutation rates. Search differences also appear between types of autocratic groups, for both Active and Inactive leaders. By understanding how these different groups explore and exploit the solution space, adjustments can be made to the technology and perhaps the group itself to facilitate the groups’ search for the optimal solution.

There are several limitations to this study. First, the current study is subject to the limitations of the underlying model and by the limitations of the study used in examining the research questions. The task used in the underlying study was much more highly constrained than many GDSS tasks, reducing the number of feasible solutions available to the group members. Thus, the exploitation of the search space, therefore the crossover rates are much lower than would be seen in a less constrained task. Obviously, more data sets from various GDSS configurations and environments need to be examined within the model. Second, we need to further enhance the model to better capture the GDSS processes. There are many different GAs with many variations on selection, crossover and mutation operators, as well as other operators available. Re-running our experiments with different GAs in the model might well provide more insightful results. Finally, more research needs to be performed with respect to leadership style within the GDSS context. Leadership is multi-dimensional and very difficult to measure. Our division into Active<sup>r</sup>Inactive groups was a simplistic approach to this complex domain, yet serves to encourage more research into this facet of GDSS use.

## 8. Future research

There are numerous opportunities for future research in this area. As mentioned in the above section, much more experimental data is required for further validation of the model and to better understand the possible relationships between GA parameters and the context variables of the group. Also, the GA model itself needs to be fine-tuned to better capture the underlying GDSS processes. For example, elitist selection might provide additional insights into GDSS use. More complex variations of crossover and mutation operators are available as well.

Another possibility is to use the concept of GA masks 30 that allow the best crossover and muta-<sup>w</sup> <sup>x</sup> tion schemes to be discovered from the data itself. Theoretically, the use of crossover and mutation masks would free researchers from discovering the best crossover and mutation implementations whichŽ could vary from GDSS setting to setting and even from group to group! . However, the use of crossover. and mutation masks poses a very computationally difficult challenge, even in the realm of today’s high-speed processors.

Finally, this research could be extended beyond GDSS groups into group meetings that not supported by technology, time-series meetings and even virtual organizations. The ideas that underlie this particular study should apply to the above group activities. Eventually, the use of a model like the one described in this paper will provide deep insights into group activities, which in turn will lead to better outcomes for researchers and practitioners alike.

## References

<sup>w</sup> <sup>x</sup> 1 Barkhi, R., 1995 . An empirical study of the impact of Ž . proximity, leader and incentives on negotiation process and outcomes in a group decision support setting. Doctoral dissertation, The Ohio State University.

<sup>w</sup> <sup>x</sup> 2 B.M. Bass, Bass and Stogdill’s handbook of leadership: theory, research and managerial applications, Free Press, New York, 1990.

<sup>w</sup> <sup>x</sup> 3 E.F. Borgatta, R.F. Bales, Some findings relevant to the great man theory of leadership, American Sociological Review 19 Ž . 1954 .

<sup>w</sup> <sup>x</sup> 4 E. Bruderer, J.V. Singh, Organizational evolution, learning, and selection: a genetic-algorithm-based model, Academy of Management Journal 39 5 1996 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 L.H. Chaney, J.A. Lyden, Managing meetings to manage your image, Supervision 59 5 1998 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 J.R.P. French Jr., The disruption and cohesion of groups, Journal of Abnormal and Social Psychology 36 1941 . Ž .

<sup>w</sup> <sup>x</sup> 7 R.B. Gallupe, A.R. Dennis, W.H. Cooper, J.S. Valacich, L.M. Bastianutti, J.F. Nunamaker, Electronic brainstorming and group size, Academy of Management Journal 35 2Ž . Ž .1992 .

<sup>w</sup> <sup>x</sup> 8 R.B. Gallupe, G. DeSanctis, Computer-based support for group problem-finding: an experimental investigation, MIS Quarterly 12 2 1988 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 B. Gavish, J. Kalvenes, Economic issues in group decision support systems, in: H. Pirkul, M. Shaw Eds. , ProceedingsŽ . of the first INFORMS conference on information systems and technology, INFORMS, Washington, DC, 1996.

<sup>w</sup> <sup>x</sup> 10 D.E. Goldberg, Genetic algorithms in search, optimization, and machine learning, Addison Wesley, Reading, MA, 1989.

<sup>w</sup> <sup>x</sup> 11 S.R. Hiltz, K. Johnson, M. Turoff, Group decision support: the effects of designated human leaders and statistical feedback in computerized conferences, Journal of Management Information Systems 8 2 1991 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 S.R. Hiltz, M. Turoff, K. Johnson, Experiments in group decision making, 3: Disinhibition, deindividuation and group process in pen name and real name computer conferences, Decision Support Systems 5 1989 .Ž .

<sup>w</sup> <sup>x</sup> 13 R. Hirokawa, D. Johnson, Toward a general theory of group

decision making development of an integrated model, Small Group Behavior 20 4 1989 .Ž . Ž .

14 L.M. Jessup, T. Connolly, J. Galegher, The effects of anonymity on GDSS group process with an idea generating task, MIS Quarterly 14 3 1990 .Ž . Ž .

15 L.M. Jessup, D.A. Tansik, Decision making in an automated environment: the effects of anonymity and proximity with a group decision support system, Decision Sciences 22 2Ž . Ž . 1991 .

<sup>w</sup> <sup>x</sup> 16 S.S. Kahai, J.J. Sosik, B.J. Avolio, Effects of leadership style and problem structure on work group process and outcomes in an electronic meeting system environment, Personnel Psychology 50 1 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 L.-H. Lim, K.S. Raman, K.-K. Wei, Interacting effects of GDSS and leadership, Decision Support Systems 12 1994 .Ž .

<sup>w</sup> <sup>x</sup> 18 R.E. Marks, D.F. Midgley, L.G. Cooper, Adaptive behaviour in an oligopoly, in: J. Biethahn, V. Nissen Eds. , Evolution- Ž . ary algorithms in management applications, Springer-Verlag, New York, 1995.

<sup>w</sup> <sup>x</sup> 19 J.E. McGrath, A.B. Hollingshead, Putting the ‘group’ back in group support systems: some theoretical issues about dynamic processes in groups with technological enhancements, in: L.M. Jessup, J. Valacich Eds. , Group support systems Ž . new perspectives, Macmillan, New York, 1993.

<sup>w</sup> <sup>x</sup> 20 M. Mitchell, An introduction to genetic algorithms, MIT Press, Cambridge, MA, 1996.

<sup>w</sup> <sup>x</sup> 21 M.A. Nix, M.D. Vose, Modeling genetic algorithms with Markov chains, Annals of Mathematics and Artificial Intelligence 5 1992 .Ž .

<sup>w</sup> <sup>x</sup> 22 J.F. Nunamaker, R.O. Briggs, D.D. Mittleman, D.R. Vogel, P.A. Balthazard, Lessons from a dozen years of group support systems research: A discussion of lab. and field findings, Journal of Management Information Systems 13 3 1997 . Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 J.F. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34 7 1991 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 M.S. Poole, G. DeSanctis, Understanding the use of group decision support systems: the theory of adaptive structuration, in: C.W. Steinfeld, J. Fulk Eds. , Organizations andŽ . communication technology, Sage Press, Newbury Park, CA, 1990.

<sup>w</sup> <sup>x</sup> 25 V.S. Rao, S.L. Jarvenpaa, Computer support of groups: Theory-based models for GDSS research, Management Science 37 10 1991 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 26 J. Rees, G.K. Koehler, A new direction in group support system theory: an evolutionary approach to group decisionmaking, 1999, in review.

<sup>w</sup> <sup>x</sup> 27 H.A. Simon, The new science of management decision, Prentice-Hall, Englewood Cliffs, NJ, 1977.

<sup>w</sup> <sup>x</sup> 28 J.J. Sosik, Effect of transformational leadership and anonymity on idea generation in computer-mediated groups, Group and Organization Management 22 4 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 J.S. Valacich, A.R. Dennis, A mathematical model of performance of computer-mediated groups during idea generation, Journal of Management Information Systems 11 1 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 M.D. Vose, The simple genetic algorithm: foundations and theory, MIT Press, Cambridge, MA, 1999.

![](/api/attachments/Y2XZRA2E/fulltext/images/a453e7457c592d05e0be3bafc541d1f1434afc9c9ad4b2d997103dea8e6e4d2a.jpg)

Jackie Rees is an assistant professor in the Krannert Graduate School of Management at Purdue University. She earned her doctorate at the University of Florida in 1998. She is a member of INFORMS and DSI. Her current research interests are in the areas of group decision-making, genetic algorithm, machine learning and information security.

![](/api/attachments/Y2XZRA2E/fulltext/images/abf2a4a66c6dfab8c28a53550412a2428549d1f0869d7bdd10877ccf6482b873.jpg)

Gary J. Koehler is the John B. Higdon Eminent Scholar and Professor of Decision and Information Sciences in the Warrington School of Business at the University of Florida. He has published in Decision Support Systems, Operations Research, Management Science, ORSA Journal on Computing, Evolutionary Computations, SIAM Journal on Control and Optimization, Annals of Operations Research, European Journal of Operational Research, Decision Sci-

ences, Annals of Mathematics and Artificial Intelligence, Computers and Operations Research, Complex Systems, Neural Networks, IEEE Transactions on Engineering Management, Managerial and Decision Economics, Naval Research Logistics Quarterly, Discrete Applied Mathematics, Journal of Finance and others. His current research interests are in e-commerce related areas.
