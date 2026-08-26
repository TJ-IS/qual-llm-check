---
otero_id: 12626
otero_key: "JZB8B9J7"
title: "Supporting Creative Problem Solving with a Case-Based Reasoning System"
authors: "Niek Althuizen; Berend Wierenga"
year: "2014"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222310112"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting Creative Problem Solving with a Case-Based Reasoning System

Niek Althuizen & Berend Wierenga

To cite this article: Niek Althuizen & Berend Wierenga (2014) Supporting Creative Problem Solving with a Case-Based Reasoning System, Journal of Management Information Systems, 31:1, 309-340

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222310112

![](/api/attachments/JZB8B9J7/fulltext/images/07e0911b43088204fe7f52878f2139cd3ce5932eb8d9f3900bf6046961d9fe65.jpg)

Published online: 05 Dec 2014.

![](/api/attachments/JZB8B9J7/fulltext/images/21cb9f3412a18df3a571e22814df7e6ef865f5445c15033b665879b797ee1549.jpg)

Submit your article to this journal

![](/api/attachments/JZB8B9J7/fulltext/images/e60b111365c4e0c3455faf49a34c9fe2612abdae4e418fe87f84d5662a550622.jpg)

Article views: 36

![](/api/attachments/JZB8B9J7/fulltext/images/7a7bb35493166a8ddcc0caf8bd0c3b6497a79bde0168a5c17c9608ed9c89ee4b.jpg)

View related articles

![](/api/attachments/JZB8B9J7/fulltext/images/b77bb77789a778823232646a1034909107d29e156137fbf001e9fd6a40835ffb.jpg)

View Crossmark data

# Supporting Creative Problem Solving with a Case-Based Reasoning System

Nie k Althuizen and Be rend Wie ren ga

Niek Althuizen is an associate professor in the Department of Marketing, ESSEC Business School, Paris. He obtained his M.S. in agricultural economics from Wageningen University (Netherlands) and his Ph.D. in marketing from the Rotterdam School of Management, Erasmus University. His research interests focus on marketing decision making and decision support, with a special interest in creativity support systems. His work has been published in Decision Support Systems and Electronic Commerce, American Sociological Review, Marketing Letters, Psychology & Marketing, and Creativity Research Journal.

Beren d Wieren ga is Professor Emeritus of Marketing at the Rotterdam School of Management (RSM), Erasmus University. Before joining RSM, he served as a faculty member at Wageningen University, where he also obtained his Ph.D. Dr. Wierenga held visiting positions at the Stanford Graduate School of Business, INSEAD, and the Wharton School of the University of Pennsylvania. His research interests focus on marketing models, marketing decision making, and marketing management support systems. He has published widely on these topics in journals such as Journal of Marketing and Management Science. He has also written several books, most recently, Marketing Management Support Systems: Principles, Tools, and Implementation. He is the editor of the Handbook of Marketing Decision Models, which appeared in the International Series in Operational Research and Management Science.

Ab stra ct: Attention for the division of work between computers and humans is growing due to ever-increasing computer capabilities. Over the past decades, creativity support systems (CSSs) have gained ground as a means to enhance individual, group, and organizational creativity. Whereas prior research has focused primarily on the main effects of CSSs, we explore the interaction effects with the creative ability of the individual. In this paper, we investigate the use of the case-based reasoning (CBR) technology, which is based on the principle of analogical reasoning, to aid individuals in solving business problems creatively. The expectations as to why the CBR technology should enhance individual creativity, and under what conditions (i.e., the type and number of cases that are made available), are derived from creative cognition theory, and are tested empirically. In a series of studies, a CBR system loaded with a diverse set of cases was found to enhance the performance of individuals with lower creative ability, but it did not help the most creative individuals. Although the literature suggests that cases from remote problem domains should lead to more novel solutions, loading the CBR system only with cases closely related to the problem domain proved more effective than remote cases only. Finally, loading the CBR system with a larger set of diverse cases was found to positively influence the creativity of the solutions. These findings have the following implications for CSSs and creative cognition theory: (1) when considering the effectiveness of CSSs it is important to take into account the creative ability of the individual (i.e., “one size does not fit all”), (2) making a sufficiently large and diverse set of cases available is better for stimulating creativity, and (3) providing cases that are too remote may be counterproductive. On a practical note, organizations seeking to redesign their division of labor between individuals and machines can easily follow the CBR approach presented here using their own set of cases.

Key w ords an d phra ses: case-based reasoning, creative problem solving, creativity support systems, creative cognition theory, domain knowledge, marketing campaigns.

New decision support a pproa ches (e.g., [12, 25, 42, 81]) are often quantitative and geared toward econometrics and operations research (OR), and hence are best suited to support managerial decision making for business problems that are relatively structured. However, as Simon argued, OR-oriented approaches are

limited to making choices among a set of alternatives that are given, explicitly or implicitly, in advance. . . . But a great deal of real-world decision making— perhaps most of it—is concerned with creating alternatives among which choices can be made. The activities that create new alternatives are usually called design activities. [69, p. 14]

Design problems in management, such as the design of new products, marketing campaigns, and strategic plans, are typically weakly structured, they come with a vast solution space, and often require creative solutions. This renders the use of OR-oriented decision support approaches largely ineffective, as the generation of creative ideas is difficult to capture in a quantitative model.

The production of creative ideas constitutes the core of an organization’s capacity to innovate and, as such, is quintessential for survival in highly competitive environments [6, 50, 80]. Over the past two decades, the information systems (IS) discipline has increasingly paid attention to the topic of creativity, crystallizing into a distinct stream of research on creativity support systems (CSSs) (see [18, 27, 28]). CSSs can be defined as information technology (IT)–enabled tools that intend to enhance the creative output of individuals (e.g., [24, 29]) or groups of individuals [17, 39, 64]. They range from electronic brainstorming techniques to more exotic approaches, such as guided fantasy and force field analysis (see [18, 27, 28]). Given the importance of creativity for all corners of business [40], surprisingly few companies actually provide their employees with formal creativity training or support, that is, beyond putting in place (financial) incentives [13]. One of the reasons for the underutilization of CSSs in practice may be the belief that creativity cannot be supported because of its inherently ill-structured nature [66].

According to Sternberg, “few psychological issues are more interesting, but more intractable, than the issue of creativity” [72, p. vii], which is commonly defined as the ability to produce work that is both novel (i.e., original, unexpected) and appropriate (i.e., useful, adaptive concerning task constraints) (see [5, 13, 20]). Although our understanding of the multitude of factors that influence creativity [38] has improved significantly, even renowned scholars admit that there is still much we do not know about creativity and how it works exactly [73]. Fortunately, this has not discouraged researchers from attempting to simulate creativity with computer programs (e.g., [11]). Most prior CSS research has focused on design issues, that is, how to incorporate IT into the creative process (e.g., [58]), or on their effectiveness, that is, whether or not CSSs, on average, enhance creativity (e.g., [17, 24, 29, 39, 55, 64]). However, it is unlikely that CSSs are equally effective for everyone [44] because of individual differences in creative ability, personality, and motivation.

The question as to “who benefits most” from CSSs is relevant from both a theoretical and managerial perspective. We deploy the case-based reasoning (CBR) technology, which has been developed in the field of artificial intelligence [1, 45, 62], to investigate this issue. CBR is based on the principle of analogical reasoning (e.g., [32]), as it makes knowledge about previous problem-solving episodes available in the form of cases that are similar or analogous to the problem at hand. The knowledge base of a CBR system thus consists of a collection of cases from the domain under study and a set of search criteria for retrieving cases that are similar to the target problem. The cases share a general structure (e.g., problem, solution, and outcomes) and may contain words, numbers, or pictures.

Applications of the CBR technology can be found, for example, in architecture, engineering, law, and medicine [45, 48, 51]. A physician may benefit from the use of a CBR system that provides access to cases of treated patients with symptoms similar to those of a new patient. That managers also use analogies routinely, by recalling similar past business situations in order to solve new problems, has been documented, for example, in strategy (see [31]), finance (see [37]), and marketing (see [36]). As analogical reasoning is often associated with creativity (e.g., [18, 19, 39]), it seems worthwhile to investigate the effectiveness of using CBR systems for solving business problems creatively. CBR systems incorporate features that are said to be quintessential for supporting creativity [68], such as (1) making previous examples or cases available as a source of inspiration, and (2) providing advanced search facilities to retrieve these previous examples. Hence, researchers in areas other than business have started to explore the potential of CBR systems for enhancing creativity (e.g., [34, 46, 54]).

The remainder of this paper is organized as follows. We first discuss our CBR approach in more detail and argue why we expect it to stimulate creativity. We then empirically assess the effectiveness of CBR systems in three laboratory studies by addressing the following questions: (1) does a CBR system help individuals to produce more creative solutions, and (2) under what conditions? The first condition pertains to the creative ability of the individual (Study 1), that is, who benefits most: creative or noncreative individuals? The other conditions concern design characteristics of the CBR system, that is, the type of cases (Study 2) and the number of cases (Study 3) stored in the CBR system.

## Theoretical Background and Hypotheses

## Domain Knowledge and Case-Based Reasoning

Beca use of the human min d’s excellen t ca pa city to make novel associations and to combine existing knowledge elements into new solutions, it is well suited to perform creative tasks. Although this capacity is difficult to mimic, CSSs may still be useful for stimulating such mental association and combinatory processes [50]. Whereas quantitative decision support approaches typically help to narrow down the number of decision alternatives until only the best alternative is left, creativity support tools should help to enlarge the set of decision alternatives. Unaided individuals have a tendency to take a “path of least resistance” [77] or may suffer from “cognitive inertia” [47, 64], meaning that they search for solutions within highly accessible but bounded areas of their memory, which limits their exploration of the vast solution space and is not likely to produce the most creative solutions [63, 64, 77].

How may a CBR system filled with old cases help to generate more creative solutions? The use of existing knowledge seems counterproductive when the goal is to produce something new. However, as Ward argues, “creative ideas do not appear, ex nihilo, full-blown in the mind of their originators, but rather must be crafted from the person’s existing knowledge” [79, p. 176]. Descriptions of the creative process, such as “using old solutions in novel ways” [46, p. 19] and “novel combinations of old ideas” [11, p. 75], stress that creative ideas are often rooted in existing knowledge. Some even suggest that profound knowledge of a domain is crucial for producing solutions that are not only novel but also useful (e.g., [70]).

However, the use of a CBR system may also have adverse effects, as the provision of previous cases could induce fixation effects that inhibit “out-of-the-box” thinking. In other words, the knowledge structures that the provided cases activate in the person’s mind may impede access to other areas of the solution space. In general, the ease with which knowledge can be accessed and retrieved from long-term memory largely depends on the frequency of use, that is, “frequent use of particular cognitive structures enhances the chronic accessibility of these structures” [63, p. 935]. This explains the tendency of individuals, when unaided, to think primarily within highly accessible areas of their memory, since it requires less effort [64, 77]. To boost creativity, people thus need to be stimulated to explore the solution space more thoroughly. This is exactly what most current techniques, such as brainstorming and guided fantasy [18], try to accomplish. Nonetheless, retrieving relevant knowledge from less accessible parts of memory can be difficult for people [33]. A CBR system facilitates easy and unbiased access to relevant knowledge stored in an external case base (or organizational memory) [71].

## Creative Ability

The creative problem-solving process typically involves iterative phases of problem formulation, preparation, idea generation, evaluation, and selection [5]. This requires not only generative cognitive processes to produce a diverse set of candidate solutions but also exploratory cognitive processes to select and refine the most promising ones [26]. A creative person should thus be good at divergent as well as convergent thinking [44]. Divergent thinking is the ability to generate many diverse ideas in response to an open-ended problem and comprises the cognitive subskills of “fluency” (number of ideas), “flexibility” (diversity of ideas), and “originality” (rarity of ideas). Divergent thinking is essential for creativity, but convergent thinking is needed to select and work out the most promising idea(s) [60]. In business, it is eventually the quality of the best idea that counts more than the sheer number of ideas.

In a comprehensive review of applied creativity in business, Kabanoff and Rossiter [43] concluded that, when the task is unstructured, the largest contributing factor to creative performance is the creative ability of the individual. However, contextual factors, such as training, incentives, and the use of CSSs, are likely to moderate the ability of the individual to perform creatively [80]. Whereas earlier work has focused predominantly on the main effects of using CSSs (notable exceptions are [44, 53]), we explicitly examine interaction effects between the use of a CBR system and the creative ability of the individual.

## The Effects of the Use of a CBR System on Creativity

Thus far we have argued that a CBR system loaded with domain knowledge in the form of cases can open up the solution space by enlarging a person’s “network of possible wanderings” [59, p. 82], which may help to produce more creative solutions. But if these solutions are crafted from existing knowledge, then where exactly does their novelty come from? Based on contemporary creative cognition research (e.g., [21, 26, 63, 64]), we propose two routes through which the provision of domain knowledge can enhance novelty: by increasing (1) the depth of exploration of the solution space and (2) the breadth of exploration of the solution space. The rationale is that the first ideas that people generate are usually the most obvious ones based on highly accessible knowledge structures [63, 64, 77]. If the cognitive effort to produce additional ideas within a particular category becomes too high, people may switch to a different category of ideas or stop generating ideas altogether. But when they are stimulated to explore the solution space more thoroughly, more original solutions may emerge.

To increase the depth of exploration of the solution space, it may be useful to activate easily accessible knowledge prior to the creative task (see [63]). Rietzschel et al. [63] found that such a preactivation of highly accessible knowledge (and the spreading of activation in memory; see [64]) stimulated individuals to explore the activated idea categories more deeply, resulting in the production of more novel ideas. To increase the breadth of exploration of the solution space, less accessible, more remote knowledge could be activated prior to the creative task. This is also why cross-functional teams are said to be more creative (e.g., [22, 74]), since each member brings a unique set of perspectives, experiences, and knowledge to bear on the creative task. This will broaden the exploration of the solution space, resulting in the generation of more novel ideas. Hence, we expect that a CBR system filled with a diverse set of cases, that is, close cases can stimulate a deeper exploration, whereas remote cases can stimulate a broader exploration of the solution space.

Although the manner in which Rietzschel et al. [63] activated domain knowledge (prior to the task) had a positive effect on the novelty of the generated ideas, it did not improve the usefulness of these ideas. In their study, increases in novelty came basically at the expense of the practicality of the ideas. The provision of domain knowledge in the form of (successful) past cases has the advantage that it can also enhance the usefulness of the generated ideas [30, 44]. Moreover, individuals do not have to rely solely on their own, biased memory, as they have an external knowledge base at their disposal. To summarize, we expect that a CBR system loaded with a diverse set of cases has the potential to stimulate both divergent and convergent thinking processes [44], which is considered to be crucial for CSSs in order to enhance the novelty as well as the usefulness of the solutions effectively [58].

Hypothesis 1: Individuals who use a CBR system loaded with diverse cases will produce more novel, more useful, and overall more creative solutions than individuals who do not use such a CBR system.

## The Interaction Between CBR System and Creative Ability

It has been argued that “creative thinking techniques are not a one-size-fits-all proposition” [44, p. 307], because each individual “brings to the creative thinking process different kinds of abilities and knowledge that need to be taken into account in order to identify the creative thinking techniques that are most useful to them” [44, p. 299]. However, most prior CSS studies have not explored this issue, but have treated the creative ability of the individual as randomly distributed across experimental groups or conditions (e.g., [65]) or as one of the covariates in the analyses (e.g., [39, 55]). The few studies that investigated interaction effects between the individual and the CSS are inconclusive as to who benefits most, that is, creative or noncreative individuals. MacCrimmon and Wagner [53] found that the use of a CSS enhanced the performance of highly creative individuals most, suggesting a reinforcement effect of the CSS. However, Cheung et al. [15] reported a decrease in the performance of highly creative individuals when they used a CSS.

Empirical evidence in the broader decision support systems literature seems in favor of a compensatory effect. That is, for relatively structured problems that require analytical problem solving, the use of analytical decision support systems has been shown to be more beneficial for nonanalytical individuals than for analytical individuals (e.g., [8, 76]). Extrapolating this finding to the realm of CSSs suggests that noncreative individuals may benefit more than creative individuals. Such a compensatory effect of the use of CSSs would also be congruent with creative cognition theories that advocate the use of examples or templates (e.g., [26, 67]). Providing people with examples, as a CBR system does in the form of cases, has been shown to influence positively the number of generated solutions [55] and the creativity of the solutions [67]. The ability to generate many diverse ideas (i.e., fluency and flexibility), including novel ones (originality), is what people with a low creative ability lack. Hence, we may expect them to benefit more from the use of a CBR system. Given the scarce and mixed evidence so far, we will address the question as to who benefits most empirically.

RQ1: To what extent do the effects of a CBR system loaded with diverse cases depend on the creative ability of the individual?

The domain of our empirical studies, which are discussed next, is the design of creative sales promotion campaigns. Sales promotions are direct, short-term inducements to buy a product or service now, such as price discounts, coupons, free samples, sweepstakes, contests, and giveaways [10]. Such campaigns are organized with a relatively high frequency and are often the responsibility of a single person, typically the brand or product manager. This will be the setting in which we test the effectiveness of our CBR approach for enhancing individual creativity, which eventually may benefit the organization as a whole.

## Study 1

## Design and Participants

To test H1, w e devised a b etw een -sub jects experimen t in which one group of participants (n = 20) was given a CBR system filled with a diverse set of cases, plus a sales promotion technique inventory on paper (more details are given in the Treatments subsection). The other group of participants (n = 20) received only the sales promotion technique inventory on paper. Forty marketing students from a Dutch university participated in this study.<sup>1</sup> The participants were randomly assigned to one of the two groups. Gender and education level were found to be proportionally distributed over the two groups (gender: 65 percent male; education level: 70 percent master’s degree and 30 percent bachelor’s degree).

## Task and Procedure

In order to create a motivation for maximum performance, the study was announced as a sales promotion campaign design contest. The study took place in the university’s behavioral laboratory. We organized eight three-hour sessions with an average of five students per session, who worked on the task individually in isolated cubicles. At the beginning of each session, they collectively took a 15-minute creative ability test (more details can be found in the Measures subsection). Next, the participants were asked to read the task description and a short document on how to use the available support.<sup>2</sup> The lead researcher had to clarify or answer about five (technical) questions per session. When ready, the participants were told to save their campaign proposal on the computer and were given a survey containing a number of process measures (see the Post H oc Analyses section). After completing the survey, the participants received compensation of 30 euros.

A Dutch beer brewery gave permission to use one of their campaign briefs in our study. The participant’s task was to write a proposal for a campaign that had to boost brand loyalty and enhance the image of the brand. The campaign had to be targeted at the “heavy-user” segment with “live music” as the main theme. The brief included a number of practical constraints: (1) the promotion had to apply to crates (containing 30 cl [centiliter] or 45 cl bottles), (2) promotional items should not be attached to the sides of the crates, and (3) the value of the promotional offer should not exceed 5 euros per crate. The campaign proposal had to contain a brief description of (1) the basic idea, (2) the sales promotion technique, (3) supporting activities, and (4) a rough cost estimation. The task thus involved all the phases of the creative process, including a divergent (generating ideas) and a convergent phase (selecting and working out the best idea) [5]. The participants were instructed not to copy one of the brand’s previous campaigns (see [67]). They were also told that experts would rate their campaign proposal on novelty and usefulness (see [10]).

## Treatments

To fill the case-base of the CBR system, we collected descriptions of 100 award-winning campaigns in Europe from the 1980s and the first half of the 1990s. The cases were taken from two books: Scoren [56] and European Sales Promotion: Great Campaigns in Action [75]. Examples of how these cases were stored in the CBR system, which we called LEAPS,<sup>3</sup> are given in Appendix A (close case) and Appendix B (remote case).

The search structure of the CBR system consisted of the following components: (1) general information about the case; (2) problem situation, including market situation, campaign objectives, and constraints; (3) solution, including campaign design and campaign execution; and (4) outcomes. This search structure contained 60 different variables. Users could search for cases by specifying the parameters they deemed relevant given the problem situation. The search values were mostly qualitative in nature, such as “introduction,” “growth,” “maturity,” and “decline” for the variable “product life cycle phase.” Users could also attach importance weights to the search variables (ranging from “very low” to “very high”). The importance weights could be inferred from the campaign brief. To prevent information overload, the CBR system displayed only the ten most similar past cases. The similarity between the search query and the cases in the CBR system was calculated using a distance-based measure (ranging from 0 = “no similarity” to 1 = “perfect similarity”).<sup>4</sup> Users were free to run multiple search queries.

The large number of search variables, the qualitative nature of the search values, the option to assign importance weights, the possibility of running multiple search queries, and the display of multiple cases that differ in their degree of similarity to the target problem ensure sufficient freedom to wander through the solution space and discover unexpected but relevant knowledge that may stimulate creativity (see [7]). Instead of manipulating the search structure or the search process, we focused on the role of the content of the case base, that is, the type and number of cases stored in the CBR system (see Studies 2 and 3).

Participants in the “no CBR system” control condition received only a sales promotion technique inventory on paper. It should be noted that this paper document was also made available to the participants in the CBR system condition. The inventory contained a basic description of sales promotion techniques (such as sampling or organizing a contest) together with the most salient pros and cons of each technique (such as aptitude for inducing trial, implementation times, and predictability of the costs). The descriptions were taken from textbooks and verified by experts (who also verified the CBR system’s search structure). All the participants were told that they could use the available support as well as their imagination.

## Measures

Creative Ability. To measure the creative ability of the participants, we used the Abbreviated Torrance Test for Adults (AT A) developed and validated by Goff and Torrance [35] (see also [4]). This test is a brief 15-minute version of the Torrance Tests of Creative Thinking and measures the following cognitive subskills of creative thinking: fluency (number of ideas), flexibility (diversity of ideas), originality (rarity of ideas), and elaboration (embellishment of ideas with details), together with 15 other creativity indicators, such as “richness and colorfulness of imagery” and “humor: conceptual incongruity.” The AT A test consists of one verbal and two figural response tasks. Two independent, trained raters scored the responses to the tasks. With raters considered in agreement whenever their scores differed no more than one point on a seven-point scale $( 1 = \mathrm { \ddot { ~ } m i n i m a l \dot { ~ } } ^ { , }$ to $7 = \mathrm { \ddot { \ s u b s t a n t i a l } { \Sigma ^ { \circ } } ) }$ (see [23, 63]), there was agreement in 100 percent of the cases. We also calculated the $r _ { w g }$ coefficient as an index of within-group interrater agreement [41]. The mean $r _ { w g }$ for the creative ability scores was 0.97 (range: 0.85–1.00), indicating strong agreement [52].<sup>5</sup> Hence, we combined the scores of the raters. The mean creative ability level was 4.7 (SD [standard deviation] = 1.3) with no significant difference between the two groups $( t ( 3 8 ) = 0 . 4 2 2 , p = 0 . 6 7 5 )$

Dependent Variables: Novelty, Usefulness, and Overall Creativity. For measuring the novelty of the solution, we selected three items (i.e., originality, surprise, and uniqueness) from Besemer and O’Quin’s [9] Creative Product Semantic Scale, which is a well-known instrument for evaluating creative products [60]. For measuring usefulness, we selected four items from the same scale. We slightly adapted the items to fit the objectives stated in the campaign brief. The four items were effectiveness for increasing the loyalty of heavy users, fit with the brand values, attractiveness for heavy users, and the overall usefulness of the campaign. All seven items were measured on a scale from 0 (very poor) to 10 (excellent).

Following Amabile [5], we asked three experts to rate independently all of the campaign proposals. Two of the experts were creative directors of renowned Dutch marketing agencies. The other expert was the beer brewery’s senior marketing manager in charge of the original campaign. Two of the experts had also served as chairmen of the annual Dutch Sales Promotion Campaign Awards. The experts were blind to the study design. All the proposals were given an identical layout and were sent to the experts in randomized batches of 20 proposals. There were no order or batch effects. It took about four hours to rate all 40 proposals.

The novelty items and the usefulness items showed high internal consistency for all experts (Cronbach $\alpha \mathrm { s } > 0 . 8 6 )$ . Thus, we averaged the individual item scores to obtain a single “novelty” score and a single “usefulness” score per expert. To obtain an “overall creativity” score for each expert, we averaged these novelty and usefulness scores (see [13, 55]). In terms of interrater agreement, the experts’ scores differed by no more than two points on an 11-point scale in 93 percent of the cases for novelty, 93 percent for usefulness, and 92 percent for overall creativity. We also calculated the multiple-item $r _ { w g ( j ) }$ coefficients [41]. The mean $r _ { w g ( j ) }$ coefficients were 0.90 for novelty (range: $0 . 0 0 { - } 1 . 0 0 $ ; with 92.5 percent $> 0 . 7 0 )$ , 0.91 for usefulness (range: 0.00–1.00; with 95 percent > 0.70 ), and 0.91 for overall creativity (range: 0.07–0.99; with 92.5 $\mathrm { p e r c e n t } > 0 . 7 0 )$ . Hence, we combined the novelty, usefulness, and overall creativity scores across experts $( \mathrm { M } = 6 . 3 , \mathrm { S D } = 0 . 7 5$ for novelty; $\mathrm { M } = 5 . 9 , \mathrm { S D } = 0 . 8 0$ for usefulness; and $\mathrm { M } = 6 . 1 , \mathrm { S D } = 0 . 7 2$ for overall creativity).

Covariates. We included two covariates commonly used in creativity research, namely gender and education level. The length of the proposal was also taken into account, as the sheer number of words has been shown to influence expert ratings of solution quality [52].

## Results and Discussion

Because of the continuous nature of the creative ability measure, we performed a series of moderated regression analyses following the procedure outlined by Aiken and West [2]. We regressed the dependent variables (novelty, usefulness, and overall creativity) on the (mean-centered) independent variables: a dummy variable for the CBR system loaded with 100 diverse cases, the participants’ creative ability, a multiplicative term of these two variables, and the covariates (gender, education level, and length of the proposal). Table 1 gives the standardized regression coefficients, the standard errors, and the increase in $R ^ { 2 }$ due to the inclusion of the interaction term.

The results show a positive effect of the CBR system with 100 diverse cases on the usefulness of the solutions (β = 0.26, t = 1.983, p = 0.028; right-tailed), but the effect on novelty is not significant (β = 0.17, t = 1.125, p = 0.135; right-tailed). We also find a positive main effect of the CBR system with 100 diverse cases on the overall creativity of the solutions (β = 0.23, t = 1.695, p = 0.050; right-tailed), which is in line with H1. The main effects are, however, qualified by a significant CBR system × creative ability interaction for novelty (β = –0.41, t = –2.769, p = 0.009), usefulness $( \beta = - 0 . 4 5$ $t = - 3 . 4 0 6 , p = 0 . 0 0 2 )$ , and overall creativity $( \beta = - 0 . 4 7 , t = - 3 . 3 7 6 , p = 0 . 0 0 2 )$ .

Following the recommendations of Aiken and West [2], we investigated the nature of these interaction effects by calculating the simple effects of the CBR system at one standard deviation above and below the mean of creative ability. The results revealed a positive effect of the use of the CBR system with 100 diverse cases on the overall creativity of the solutions for individuals with a low creative ability $( \beta = 0 . 7 0$ $t = 3 . 6 1 0 , p < 0 . 0 0 1 )$ ), but not for highly creative individuals $( \beta = - 0 . 2 4 , t = - 1 . 2 1 8 .$ $p = 0 . 2 3 2 ) .$ .<sup>6</sup> The nature of the interaction effect for overall creativity is displayed in Figure 1 (note that the results were similar for novelty and usefulness). Thus, we may conclude that the positive effect of the CBR system with diverse cases on the novelty, usefulness, and overall creativity of the solutions was stronger for individuals with a low creative ability than for highly creative individuals, who did not benefit from the CBR system with diverse cases.

Table 1. The Effects of a CBR System with Diverse Cases on Creativity (Study 1)

<table><tr><td>Variables</td><td>Novelty</td><td>Usefulness</td><td>Overall creativity</td></tr><tr><td>CBR system (100 diverse cases)</td><td>0.17(0.22)</td><td>0.26*(0.21)</td><td>0.23*(0.20)</td></tr><tr><td>Creative ability</td><td>0.25(0.09)</td><td>0.10(0.09)</td><td>0.18(0.08)</td></tr><tr><td>CBR system (100 diverse cases) × creative ability</td><td>-0.41**(0.17)</td><td>-0.45**(0.17)</td><td>-0.47**(0.15)</td></tr><tr><td>Covariates</td><td></td><td></td><td></td></tr><tr><td>Gender</td><td>-0.13(0.24)</td><td>-0.26†(0.23)</td><td>-0.21(0.22)</td></tr><tr><td>Education level</td><td>0.04(0.24)</td><td>0.28*(0.23)</td><td>0.18(0.21)</td></tr><tr><td>Length of proposal</td><td>0.13(0.00)</td><td>0.05(0.00)</td><td>0.10(0.00)</td></tr><tr><td> $R^2$ </td><td>0.29</td><td>0.43</td><td>0.38</td></tr><tr><td>F</td><td>2.27†</td><td>4.15**</td><td>3.44**</td></tr><tr><td>Δ $R^2$ (due to the inclusion of the interaction term)</td><td>0.17</td><td>0.20</td><td>0.21</td></tr><tr><td>F for Δ $R^2$ </td><td>7.90**</td><td>11.96**</td><td>11.74**</td></tr></table>

Notes: $n = 4 0 .$ . All the independent variables are mean-centered, following Aiken and West [2]. The standardized regression coefficients are reported, with standard errors in parentheses. The baseline condition involves no CBR system. Covariates: Master’s-degree students produced more usefu solutions than bachelor’s-degree students. Men tended to produce more useful solutions than women. $^ { \dag } p \leq 0 . 1 0 ; ^ { \ast } p \leq 0 . 0 5 ; ^ { \ast \ast } p \leq 0 . 0 1$

In Study 1, the CBR system contained a broad variety of cases, ranging from campaigns for beer brands (the same product category) to campaigns for insurance products (a very different product category). This begs the question whether the type of cases stored in the CBR system influences the creativity of the solutions. Dahl and Moreau [19], for example, argued that analogies coming from very different problem domains should lead to more novel solutions than analogies coming from basically the same problem domain. Given the stark differences between individuals with a low and high creative ability in Study 1, the question of “who benefits most from which type of cases” also seems pertinent. To address these questions, we manipulated the type of cases stored in the CBR system in Study 2.

![](/api/attachments/JZB8B9J7/fulltext/images/93a095d8536474c9a23d9e4b657eab8025179b5b74f92a1e34cdaa51d3becfa6.jpg)  
Figure 1. Study 1: Interaction Between Creative Ability and the Use of a CBR System

## Study 2

The Effects of the CBR System’s Content: Close Versus Remote Cases

With rega rd to the type of ca ses, a distinction can be made between close cases, which come from basically the same problem domain, and remote cases, which come from more distant or even “wildly discrepant” problem domains [16, 78, 79]. For example, when a marketer has to design a creative campaign for a beer brand, he or she may find inspiration in previous campaigns organized by the same or other beer brands (close cases), but also in campaigns organized for cars or insurance products (remote cases). Earlier we argued that the use of a CBR system might help to increase the depth and breadth of exploration of the solution space [63]. More specifically, close cases are expected to enhance the depth of exploration of the solution space, whereas remote cases are expected to enhance the breadth of exploration. Both types of exploration may lead to novel solutions, but prior research suggests that remote cases will enhance novelty more than close cases (e.g., [19]). The rationale is that using remote cases requires more cognitive effort, because the similarities with the target problem exist at an abstract level only [32]. Simply put, the use of remote cases requires “mental leaps,” whereas the use of close cases only requires “mental hops” [78]. Due to the greater conceptual distance between the base and the target problem, solutions based on remote cases may be less obvious and thus more novel. However, this greater distance is also likely to produce less useful solutions than those based on close cases.

Hypothesis 2: Individuals who use a CBR system loaded with remote cases only will produce more novel but less useful solutions than individuals who use a CBR system loaded with close cases only.

In Study 1, individuals with a low creative ability were helped more by a CBR system with 100 diverse cases than individuals with a high creative ability. But what if the CBR system contains only remote cases? Since highly creative individuals, by definition, are more flexible in their thinking, it might be easier for them to work with cases that are remote from the target problem than for individuals with a low creative ability (for whom the use of such cases could be too demanding). The latter probably benefit more from close cases, as these cases require only “mental hops.” Nonetheless, close cases can still stimulate a deeper exploration of the solution space and, hence, may lead to more novel solutions, but less so than remote cases that are expected to stimulate a broader exploration of the solution space.

RQ2: To what extent do the effects of a CBR system loaded with remote cases only depend on the creative ability of the individual?

## Design and Participants

Study 2 was identical to Study 1, except for the experimental treatments. Of the CBR system with 100 diverse cases used in Study 1, 50 cases were classified as “close” and 50 as “remote” based on the product category (see [16]). Campaigns for consumerpackaged goods (cpg), such as beer and soft drinks, are quite different from campaigns for consumer durables or services (non-cpg), such as cars or insurance products. Since beer is a consumer-packaged good, we classified all cpg cases as “close” and all non-cpg cases as “remote.”

To test H2, we devised a between-subjects study in which one group of participants (n = 20) was given a CBR system with remote cases only, while the other group (n = 20) received a CBR system with close cases only. Forty marketing students from the same university as in Study 1 were randomly assigned to one of the two groups. Gender and education level were again found to be proportionally distributed over the two groups (gender: 73 percent male; education level: 70 percent master’s degree, 30 percent bachelor’s degree).

## Measures

The same raters as in Study 1 scored the participants’ responses to the AT A test. Their scores differed by no more than one point (on a seven-point scale) in 100 percent of the cases. We also calculated the mean $r _ { w g }$ coefficient, which was a high 0.97 (range: 0.85– 1.00). Thus, we combined the scores of the two raters. The mean creative ability level was 4.9 (SD = 1.4), with no significant difference between the two groups $( t ( 3 8 ) = 0 . 5 6 1$ $p = 0 . 5 7 8 )$ . The same experts as in Study 1 agreed to evaluate the campaign proposals. As for interrater agreement, their scores differed by no more than two points (on an 11-point scale) in 98 percent of the cases for novelty, 97 percent for usefulness, and 98 percent for overall creativity. The mean $r _ { w g ( j ) }$ coefficients were 0.97 for novelty (range: 0.84–1.00), 0.93 for usefulness (range: 0.25–1.00; with 97.5 percent > 0.70), and 0.96 for overall creativity (range: 0.76–1.00). Hence, we combined the novelty, usefulness, and overall creativity scores across experts (M = 6.2, SD = 0.64 for novelty; M = 5.7, $\mathrm { S D } = 0 . 6 5$ for usefulness; and M = 5.9, SD = 0.57 for overall creativity).

Table 2. The Effects of the Type of Cases Stored in the CBR System (Study 2)

<table><tr><td>Variables</td><td>Novelty</td><td>Usefulness</td><td>Overall creativity</td></tr><tr><td>CBR system (50 remote cases)</td><td>-0.25(0.20)</td><td>-0.21(0.21)</td><td>-0.26*(0.17)</td></tr><tr><td>Creative ability</td><td>-0.21(0.07)</td><td>0.07(0.08)</td><td>-0.08(0.06)</td></tr><tr><td>CBR system (50 remote cases) × creative ability</td><td>-0.24(0.13)</td><td>-0.31*(0.14)</td><td>-0.31*(0.12)</td></tr><tr><td>Covariates</td><td></td><td></td><td></td></tr><tr><td>Gender</td><td>-0.01(0.24)</td><td>-0.29(0.26)</td><td>-0.17(0.22)</td></tr><tr><td>Education level</td><td>0.26(0.23)</td><td> $0.30^†$ (0.24)</td><td> $0.32^†$ (0.20)</td></tr><tr><td>Length of proposal</td><td>0.38*(0.00)</td><td>0.08(0.00)</td><td> $0.26^†$ (0.00)</td></tr><tr><td> $R^2$ </td><td>0.36</td><td>0.32</td><td>0.38</td></tr><tr><td>F</td><td>3.15*</td><td>2.55*</td><td>3.32*</td></tr><tr><td>Δ $R^2$  (due to the inclusion of the interaction term)</td><td>0.05</td><td>0.09</td><td>0.08</td></tr><tr><td>F for Δ $R^2$ </td><td> $2.86^†$ </td><td>4.56*</td><td>5.03*</td></tr></table>

Notes: $n = 4 0 .$ . All the independent variables are mean-centered, following Aiken and West [2]. The standardized regression coefficients are reported, with standard errors in parentheses. The baseline condition involves the CBR system loaded with 50 close cases. Covariates: Master’s-degree students tended to produce more novel, and overall more creative solutions than bachelor’s-degree students. The length of the proposal (number of words) was positively related to the novelty and overall creativity of the solutions. $^ { \prime } p \leq 0 . 1 0 ; ^ { \ast } p \leq 0 . 0 5 ; ^ { \ast \ast } p \leq 0 . 0 1$

## Results and Discussion

As in Study 1, we regressed the dependent variables (novelty, usefulness, and overall creativity) on the (mean-centered) independent variables: a dummy variable for the CBR system loaded with remote cases only, the participants’ creative ability, a multiplicative term of these two variables, and the same covariates. The results are presented in Table 2.

Contrary to our expectations (H2), the use of a CBR system loaded with remote cases only, as compared with a CBR system loaded with close cases only, neither positively influenced the novelty of the solutions $( \beta = - 0 . 2 5 , t = - 1 . 6 2 5 , p = 0 . 9 4 3$ right-tailed), nor did it significantly affect the usefulness of the solutions $( \beta = - 0 . 2 1$ t = –1.287, $p = 0 . 1 0 4 $ ; left-tailed). Thus, we may conclude that a CBR system with remote cases only does not lead to more novel, but less useful, solutions than a CBR system with close cases only.

However, there was a marginally significant negative effect of the CBR system loaded with remote cases only on the overall creativity of the solutions $( \beta = - 0 . 2 6 , t = - 1 . 6 9 5$ $p = 0 . 0 9 8 )$ . In addition, the interaction effect between the CBR system loaded with remote cases only and creative ability was significant for overall creativity $( \beta = - 0 . 3 1$ $t = - 2 . 2 0 8 , p = 0 . 0 3 4 )$ and for usefulness $( \beta = - 0 . 3 1 , t = - 2 . 1 0 2 , p = 0 . 0 4 3 )$ , but not for novelty $( \ B = - 0 . 2 4 , t = - 1 . 6 6 6 , p = 0 . 1 0 5 )$ . A closer investigation of this interaction effect for overall creativity revealed that the CBR system loaded with remote cases only had a negative impact for individuals with a high creative ability $( \beta = - 0 . 5 8 ,$ $t = - 2 . 8 1 0 , p = . 0 0 8 )$ , but there was no significant effect for individuals with a low creative ability $( \beta = 0 . 0 6 , t = 0 . 2 6 , p = . 7 9 0 )$ . The nature of this interaction effect is displayed in Figure 2 (note that the results were similar for usefulness). Thus, we may conclude that the use of a CBR system with remote cases only decreased the usefulness and overall creativity of the solutions proposed by highly creative individuals. This negative effect is intriguing and may explain why highly creative individuals did not perform better in Study 1. For them, remote cases seem to work as distractors rather than facilitators. We come back to this issue in the Post H oc Analyses section.

![](/api/attachments/JZB8B9J7/fulltext/images/e4928bcb8a26a9997808871cf95b336f2c5de9432cbd1c441886417113bdee0e.jpg)  
Figure 2. Study 2: Interaction Between Creative Ability and Type of Cases in the CBR System

So far, we have investigated the effectiveness of a CBR system loaded with a diverse set of cases for enhancing the creativity of individuals with different levels of creative ability (Study 1) and explored the role of the type of cases stored in the CBR system (Study 2). Because we had only 50 close cases and 50 remote cases at our disposal, the CBR systems inevitably contained different numbers of cases (i.e., 100 in Study 1 versus 50 in Study 2). In Study 3, we therefore investigate the role of the number of cases stored in the CBR system.

## Study 3

## The Effects of the Content of the CBR System: More Versus Fewer Cases

In the litera ture n ot on ly the diversity of kn ow ledge is argued to positively influence creativity but the amount of available knowledge may also play a role [57]. Moorman and Miner [57] found that the amount of knowledge made available to employees in organizations was positively related to the financial performance of their new products (cf. usefulness), although they did not find a significant impact on the creativity of these products. Accordingly, we expect that the number of cases stored in the CBR system may positively influence the usefulness of the solutions. The rationale is that having more cases stored in the CBR system increases the likelihood of retrieving cases that are relevant to the problem at hand. More relevant cases are likely to lead to more useful solutions. Since any case may activate knowledge in a person’s mind and, hence, stimulate a deeper or broader exploration of the solution space, we do not expect an effect of the number of cases stored in the CBR system on the novelty of the solutions.

Hypothesis 3: Individuals who use a CBR system loaded with more diverse cases will produce more useful solutions than individuals who use a CBR system loaded with fewer diverse cases.

Based on the results of Study 1, we also expect that individuals with a low creative ability will benefit more from a CBR system with a larger number of cases than highly creative individuals. Thus, we formulate the following research question:

RQ3: To what extent do the effects of a CBR system loaded with more diverse cases depend on the creative ability of the individual?

## Design and Participants

Study 3 was identical to the previous ones, except for the experimental treatments. We compared the group of participants (n = 20) of Study 1 who used the CBR system loaded with 100 diverse cases with a new group of participants (n = 20) who were given a CBR system loaded with 50 diverse cases (randomly selected out of the 100 cases). Both CBR systems contained a 50/50 mix of close and remote cases. Twenty marketing students from the same university were recruited to use the CBR system loaded with 50 diverse cases. Gender and education level were again found to be proportionally distributed over the two groups (gender: 65 percent male; education level: 80 percent master’s degree and 20 percent bachelor’s degree).

## Measures

Again, the same two trained raters scored the responses to the AT A test. Their scores differed by no more than one point (on a seven-point scale) in 100 percent of the cases. We also calculated the mean $r _ { w g }$ coefficient, which was a high 0.97 (range: 0.85–1.00). Hence, we combined the scores of the two raters. The mean creative ability level was 4.8 (SD = 1.3) with no significant difference between the two groups $( t ( 3 8 ) = 0 . 2 9 6 , p = 0 . 7 6 9 )$ . The new campaign proposals were rated by the same experts. As for interrater agreement, their scores differed by no more than two points (on an 11-point scale) in 92 percent of the cases for novelty, 91 percent for usefulness, and 92 percent for overall creativity. The mean $r _ { w g ( j ) }$ coefficients were 0.90 for novelty (range: 0.00–1.00; with 90 percent > 0.70), 0.90 for usefulness (range: 0.00–1.00; with 92.5 percent > 0.70), and 0.95 for overall creativity (range: 0.47–1.00; with 97.5 percent > 0.70). Hence, we averaged the novelty, usefulness, and overall creativity scores across experts (M = 6.3, SD = 0.65 for novelty; M = 5.9, SD = 0.83 for usefulness; and M = 6.1, SD = 0.68 for overall creativity).

Table 3. The Effects of the Number of Cases Stored in the CBR System (Study 3)

<table><tr><td>Variables</td><td>Novelty</td><td>Usefulness</td><td>Overall creativity</td></tr><tr><td>CBR system (100 diverse cases)</td><td>0.24(0.20)</td><td>0.33*(0.22)</td><td>0.31*(0.18)</td></tr><tr><td>Creative ability</td><td>0.09(0.08)</td><td>-0.02(0.08)</td><td>0.03(0.07)</td></tr><tr><td>CBR system (100 diverse cases) × creative ability</td><td>-0.22(0.15)</td><td>-0.34*(0.16)</td><td>-0.32*(0.13)</td></tr><tr><td>Covariates</td><td></td><td></td><td></td></tr><tr><td>Gender</td><td>-0.19(0.21)</td><td>-0.15(0.23)</td><td>-0.19(0.19)</td></tr><tr><td>Education level</td><td>0.38*(0.25)</td><td>0.51**(0.27)</td><td>0.50**(0.22)</td></tr><tr><td>Length of proposal</td><td>0.08(0.00)</td><td>0.00(0.00)</td><td>0.04(0.00)</td></tr><tr><td> $R^2$ </td><td>0.31</td><td>0.48</td><td>0.47</td></tr><tr><td>F</td><td>2.45*</td><td>5.13**</td><td>4.93**</td></tr><tr><td>Δ $R^2$ (compared to main effects model)</td><td>0.05</td><td>0.11</td><td>0.10</td></tr><tr><td>F for Δ $R^2$ </td><td>2.31</td><td>7.40*</td><td>6.23*</td></tr></table>

Notes: $n = 4 0 .$ . All the independent variables are mean-centered, following Aiken and West [2]. The standardized regression coefficients are reported, with standard errors in parentheses. The baseline condition involves the CBR system loaded with 50 diverse cases. Covariates: Master’s-degree students outperformed bachelor’s-degree students in terms of the novelty, usefulness, and overall creativity of their solutions. <sup>†</sup> p ≤ 0.10; \* $p \leq 0 . 0 5 ;$ \*\* $p \leq 0 . 0 1$

## Results and Discussion

We regressed the dependent variables (novelty, usefulness, and overall creativity) on the (mean-centered) independent variables: a dummy variable for the CBR system loaded with 100 diverse cases, the participants’ creative ability, a multiplicative term of these two variables, and the same covariates. The results are presented in Table 3. In agreement with H3, we found a positive effect of the CBR system loaded with 100 diverse cases (versus 50 diverse cases) on the usefulness of the solutions (β = 0.33, t = 2.457, p = 0.010; right-tailed). We also found a positive main effect of the CBR system loaded with 100 diverse cases on the overall creativity of the solutions $( \beta = 0 . 3 1$ $t = 2 . 3 3 8 , p = 0 . 0 2 6 )$ . These main effects were qualified by a significantly negative interaction effect with creative ability for overall creativity $( \beta = - 0 . 3 2 , t = - 2 . 4 5 9 ,$ $p = 0 . 0 1 9 )$ and for usefulness $( \beta = - 0 . 3 4 , t = - 2 . 6 8 1 , p = 0 . 0 1 1 )$ . A closer investigation of the interaction effect for overall creativity revealed a significantly positive effect of the CBR system loaded with 100 diverse cases for individuals with a low creative ability $( \beta = 0 . 6 3 , t = 3 . 4 0 5 , p = 0 . 0 0 2 )$ , but not for highly creative individuals $( \beta = - 0 . 0 1$ ， $t = - 0 . 0 3 3 , p = 0 . 9 7 4 )$ . Figure 3 shows the nature of this interaction effect for overall creativity (note that the results were similar for usefulness).

![](/api/attachments/JZB8B9J7/fulltext/images/fa565983fbf8713c88a2c24328977b2270a48cc6f6505315c6fca38b90b0b0d0.jpg)  
Figure 3. Study 3: Interaction Between Creative Ability and Number of Cases in the CBR System

## Post Hoc Analyses

Tw o in triguin g question s a risin g from the results deserve a tten tion : (1) Why did remote cases not have a positive effect on novelty? and (2) Why did highly creative individuals not benefit from a CBR system, and the one with remote cases in particular? To address these questions, we performed a number of post hoc analyses on the process data that we collected at the end of each study. The participants were asked to report the cases that they had read (“cases read”) and the cases that had inspired them or from which they had taken elements (“cases used”). They could look up the cases, if necessary. Out of the 100 cases, 83 different cases were read and 35 different cases were actually used by the participants. Following the campaign brief, campaigns organized for alcoholic beverages and campaigns with music as the main theme were among the most frequently read and used cases. The participants also reported the time that they worked with the available support (in minutes), the time needed for completing the task (in minutes), and whether the time allotted to the task was sufficient (on a seven-point scale from 1 = “far too little” to 7 = “far too much”). These process data are presented in Table 4.

Why did remote cases not enhance novelty? The first two rows of Table 4 show that participants in Study 2 (close versus remote cases) read, on average, about the same number of cases $( \mathbf { M } = 4 . 3$ versus $\mathbf { M } = 4 . 6 , p = 0 . 6 6 8 )$ . However, Table 4 also reveals that participants in the “remote cases” condition, on average, used fewer cases than participants in the “close cases” condition $( \mathbf { M } = 0 . 6 0$ versus $\mathbf { M } = 1 . 2 5 , p = 0 . 0 4 3 )$

M<sup>eans</sup> <sup>of</sup> <sup>the</sup> <sup>Process</sup> <sup>Data</sup> <sup>per</sup> <sup>C</sup>

<table><tr><td>CBR system</td><td>Number of cases read</td><td>Number of cases used</td><td>Close cases read</td><td>Remote cases read</td><td>Close cases used</td><td>Remote cases used</td><td>System usage time</td><td>Total time</td><td>Sufficient time</td></tr><tr><td>Remote cases (50)</td><td>4.30</td><td>0.60</td><td>—</td><td>4.30</td><td>—</td><td>0.60</td><td>46.0</td><td>132.8</td><td>4.5</td></tr><tr><td>Close cases (50)</td><td>4.60</td><td>1.25</td><td>4.60</td><td>—</td><td>1.25</td><td>—</td><td>48.8</td><td>115.5</td><td>4.9</td></tr><tr><td>Diverse cases (100)</td><td>3.30</td><td>0.95</td><td>2.35</td><td>0.95</td><td>0.85</td><td>0.10</td><td>34.5</td><td>127.6</td><td>4.7</td></tr><tr><td>Diverse cases (50)</td><td>4.40</td><td>1.00</td><td>2.75</td><td>1.65</td><td>0.80</td><td>0.20</td><td>38.4</td><td>132.8</td><td>5.1</td></tr><tr><td>Mean</td><td>4.15</td><td>0.95</td><td>3.23</td><td>2.30</td><td>0.97</td><td>0.30</td><td>41.9</td><td>127.2</td><td>4.8</td></tr><tr><td colspan="10">Notes: n = 80. Master&#x27;s-degree students read more close cases (r = 0.30, p = 0.007), but also more remote cases (r = 0.21, p = 0.066) than bachelor&#x27;s-degree students. Creative ability and gender are not significantly related to any of the process variables.</td></tr></table>

The inclination to use close cases rather than remote cases can also be observed in the conditions where participants had both types of cases available (Study 3: see rows 3 and 4 of Table 4). In these conditions, participants read and used significantly more close cases than remote cases $( \mathrm { M } = 2 . 3 5 $ versus M = 0.95, $p = 0 . 0 0 4$ for “cases read”; $\mathbf { M } = 0 . 8 5$ versus $\mathbf { M } = 0 . 1 0 , p = 0 . 0 0 5$ for “cases used”). Thus, there appears to be a (cognitive) hurdle for using remote cases.

To enhance novelty via a deeper exploration of the solution space, Rietzschel et al. [63] argued that a certain degree of homogeneity of the provided stimuli is necessary. The cases provided by the CBR system loaded with remote cases (containing cases for a wide variety of product categories) are arguably more heterogeneous than the cases provided by the CBR system loaded with close cases (containing only consumer-packaged goods cases), which may thus have inhibited a deeper exploration of the solution space. Nonetheless, a CBR system filled with remote cases should still be able to stimulate a broader exploration of the solution space, but apparently it failed to do so in our study. A possible explanation could be that participants had difficulty seeing the relevance of the retrieved remote cases for solving the problem at hand, as it involves the identification of similarities at a higher level of abstraction than for close cases and thus requires more effort. This is illustrated by the fact that the participants in the “remote cases” condition used fewer cases but, at the same time, they tended to take more time to come up with a solution than the participants in the “close cases” condition $( \mathbf { M } = 1 3 2 . 8$ versus $\mathbf { M } = 1 1 5 . 5 , p = 0 . 0 5 8 )$ .

Interestingly, a number of participants who had the choice between close and remote cases managed to overcome this hurdle and actually used remote cases. When the proportion of “remote cases used” is included as an explanatory variable in the regression analysis of Study 3, we find a positive relationship with novelty $( \beta = 0 . 3 3 , p = 0 . 0 5 0 )$ (note that the inclusion of this variable did not substantially alter the coefficients shown in Table 3). Also, the solution with the highest overall creativity score (7.31) was actually produced by a participant (with an average creative ability) who used a remote case. Hence, we should not discard remote cases too quickly. The challenge is to get people to use remote cases, but using a system loaded with remote cases only proved largely ineffective. A comparison of the right-hand side of Figure 1 (mix of close and remote cases) with Figure 2 (either close cases or remote cases) suggests that providing a mix of close and remote cases is more effective.

Why did a CBR system not help highly creative individuals? Highly creative individuals are said to be high on self-sufficiency [14], so they may have ignored the CBR system. This is not the case in our studies. Highly creative individuals did not differ in terms of the number of cases they read and used, the time they worked with the CBR system, and the total time they needed to complete the task. However, there are some significant differences with regard to the use of the CBR system loaded with remote cases only. Highly creative individuals used this CBR system much longer than individuals with a low creative ability $( \mathbf { M } = 5 1 . 5 $ versus $\mathbf { M } = 2 0 . 0 , p = 0 . 0 1 5 )$ . They also used remote cases for constructing a solution to a greater extent than individuals with a low creative ability, who abstained from using them $( \mathbf { M } = 0 . 9 0$ versus ${ \bf M } = 0 . 0 0$ $p { = } 0 . 0 5 4 )$ . The story here is that individuals with a low creative ability tend to dismiss remote cases more quickly, while highly creative individuals go the extra mile, but it does not help them to produce more creative solutions.

## Discussion

## Implications for Research

Tab le 5 provides an overview of our fin din gs. Study 1 showed that a CBR system loaded with a diverse set of 100 (successful) past cases effectively enhanced the creative performance of individuals with lower creative ability, but it did not help highly creative individuals. Study 2 revealed that the strategy to enhance the novelty of the solutions by loading the CBR system with remote cases only was largely ineffective. The process data suggest that participants were less inclined to use remote cases, arguably because they had difficulty seeing their relevance and applicability. Nonetheless, when given the choice between close and remote cases, participants who actually used remote cases tended to produce more novel solutions. These findings provide a more nuanced view on the benefits of using remote cases (or far analogies) for enhancing novelty, as reported by Dahl and Moreau [19], De L uca and Atuahene-Gima [22], Moorman and Miner [57], and Tiwana and McLean [74]. There might be an optimal level of remoteness beyond which the use of remote knowledge becomes counterproductive (inverted U‑ shape).

Study 3 demonstrated that a CBR system loaded with 100 diverse cases (instead of 50) proved more effective, but not for highly creative individuals. Although participants, on average, read about four different cases and used only one of these cases for constructing a solution, storing more cases in the CBR system seems better for enhancing the usefulness and overall creativity of the solutions. We compared only two situations here: 50 versus 100 diverse cases. It would be interesting to investigate whether our findings also apply to larger case bases. For example, would it be worthwhile to create vast knowledge bases that contain thousands of cases? Or is there perhaps also an inverse U‑ shaped relationship with the creativity of the solutions when it comes to the number of cases stored in the CBR system?

The participants in our studies were marketing students. Marketing students are prospective brand managers in charge of sales promotion activities and it is not unlikely that, through their student jobs and internships, many of them already had some experience with designing marketing campaigns. Although students have been found to be reasonable substitutes for managers in experimental studies (e.g., [61]), it would be interesting to conduct a study with brand managers or employees of marketing agencies who arguably possess more practical domain knowledge. Furthermore, participants worked on the task individually, but in practice creativity is often the result of teamwork. Professionals and teams may also be better able to use remote cases. Further research should therefore investigate whether our findings also hold in team settings. We did conduct a pilot study with small teams and found similar positive effects of a CBR system loaded with 100 diverse cases on creativity.

In our studies remote cases appeared less effective for enhancing creativity than close cases, which runs counter to the findings of other studies (e.g., [19]). A possible explanation could be that the provided cases were too remote (or too diverse). This calls for more research on (1) the optimal level of “remoteness,” that is, how distant should cases be from the target problem in order to effectively stimulate creativity, or (2) research on how people can be assisted in overcoming the (cognitive) hurdle for using remote cases, for instance, by making the similarity or applicability of the remote cases more salient. Special attention needs to be paid here to highly creative individuals, whom we expected to be better able to use remote cases and make the necessary mental leaps. However, they did not benefit from the use of a CBR system, and the one loaded with remote cases only appeared even detrimental (see Figures 1 and 2). Should these people be left alone or are there other techniques that could enhance their performance? We need to dig deeper into the process and the differences between individuals with a high and low creative ability, so that we can support them with the right type of CSSs.

<table><tr><td colspan="2">Explanatory variables</td><td colspan="3">Results</td><td rowspan="2">Substantive conclusions and additional findings</td></tr><tr><td>Type of CBR system</td><td>Type of effect</td><td>Novelty</td><td>Usefulness</td><td>Overall creativity</td></tr><tr><td rowspan="4">CBR system with 100 diverse cases (versus no CBR system)</td><td>Main effect (H1)</td><td>Hypothesized (+), but not significant</td><td>+ (supported)</td><td>+ (supported)</td><td>The use of a CBR system with 100 diverse cases results in more useful and overall more creative solutions (as hypothesized), but it has no significant impact on the novelty of the solutions (contrary to what was hypothesized).</td></tr><tr><td>Interaction with creative ability (R1)</td><td>-</td><td>-</td><td>-</td><td rowspan="3">The use of a CBR system with 100 diverse cases leads to more novel, more useful, and overall more creative solutions for individuals with a low creative ability, but it has no significant impact for individuals with a high creative ability.</td></tr><tr><td>- Low creative ability</td><td>+</td><td>+</td><td>+</td></tr><tr><td>- High creative ability</td><td>Not significant</td><td>Not significant</td><td>Not significant</td></tr><tr><td>CBR system with 50 remote cases (versus 50 close cases)</td><td>Main effect (H2)</td><td>Hypothesized (+), but not significant</td><td>Hypothesized (-), but not significant</td><td>- (not hypothesized)</td><td>The use of a CBR system with remote cases only does not result in more novel, but less useful solutions than the use of a CBR system with close cases (contrary to what was hypothesized), but it does tend to result in overall less creative solutions than the use of a CBR system with close cases only (not hypothesized).</td></tr></table>

<table><tr><td rowspan="3"></td><td>Interaction with creative ability (R2)</td><td>Not significant</td><td>-</td><td>-</td><td rowspan="3">The use of a CBR system with remote cases only leads to less useful and overall less creative solutions for highly creative individuals, but it has no significant impact for individuals with a low creative ability.</td></tr><tr><td>- Low creative ability</td><td></td><td>Not significant</td><td>Not significant</td></tr><tr><td>- High creative ability</td><td></td><td>-</td><td>-</td></tr><tr><td rowspan="4">CBR system with 100 diverse cases (versus 50 diverse cases)</td><td>Main effect (H3)</td><td>Not hypothesized, and not significant</td><td>+ (supported)</td><td>+ (not hypothesized)</td><td>The use of a CBR system with 100 diverse cases results in more useful solutions than the use of a CBR system with 50 diverse cases (as hypothesized), and also in overall more creative solutions (not hypothesized).</td></tr><tr><td>Interaction with creative ability (R3)</td><td>Not significant</td><td>-</td><td>-</td><td rowspan="3">The use of a CBR system with 100 diverse cases leads to more useful and overall more creative solutions for individuals with a low creative ability, but it has no significant impact for individuals with a high creative ability.</td></tr><tr><td>- Low creative ability</td><td></td><td>+</td><td>+</td></tr><tr><td>- High creative ability</td><td></td><td>Not significant</td><td>Not significant</td></tr></table>

## Implications for Practice

Hiring highly creative individuals is one option to enhance the creative output of an organization [3]. However, with the help of a CBR system with 100 diverse cases, individuals with a low creative ability were able to match, or even surpass, the performance of highly creative individuals (see Figure 1). Thus, organizations do not necessarily have to rely on creative individuals, as they can easily set up a CBR system and fill it with cases. An organization’s own cases constitute an invaluable source of proprietary domain knowledge. Based on our findings, it seems best to build a sufficiently large case base that contains a mix of close cases and remote cases.

A recent example of the approach outlined in this paper is the beer bottle design contest that Heineken organized to celebrate its 140th anniversary (Heineken Future Bottle Design Contest 2013). This contest invited people from all over the world to submit a creative design for Heineken’s future beer bottle. Participants were explicitly asked to look for inspiration in the Heineken archives, which include 250 items ranging from pictures of previous bottle designs (close cases) to pictures of nature and art objects (remote cases), and to “remix” these items into a new bottle design. Participants could also view the designs submitted by other contestants (as well as the number of views for each submission).

## Conclusions

Atten tion to the division of w ork b etw een computers an d human s is growing due to ever-increasing computer capabilities. Over the past two decades, CSSs have gained ground as a means to enhance individual, group, and organizational creativity. In three studies, we investigated the effectiveness of a knowledge-based CBR system for enhancing the creativity of sales promotion campaigns. The CBR technology is based on the principle of analogical reasoning and makes relevant domain knowledge available in the form of cases. Because analogical reasoning and the provision of domain knowledge have been argued to be conducive to creativity, we investigated whether the use of a CBR system enhances creativity and under what conditions. These conditions pertained to the creative ability of the individual and two system design characteristics, namely the type and number of cases stored in the CBR system. Our findings have the following implications for CSSs and creative cognition theory: (1) when considering the effectiveness of CSSs it is important to take into account the creative ability of the individual (i.e., “one size does not fit all”), (2) making a sufficiently large and diverse set of cases available is better for stimulating creativity, and (3) providing cases that are too remote may be counterproductive.

Organizations seeking to redesign their division of labor between individuals and machines can easily follow the CBR approach presented in this paper, using their own set of cases, in order to boost the creativity of individuals with lower creative ability. There are many examples of creative design problems in business that are comparable to the problem of designing sales promotion campaigns, such as the design of advertising campaigns, new products, packaging, logos, or even strategic plans. Such weakly structured problems, for which cases of previous problemsolving episodes are available, may benefit greatly from collecting, indexing, and storing cases in a CBR system and putting them into action for creative problem solving. However, organizations with highly creative employees, such as advertising agencies, are not likely to benefit much from making a CBR system available to their employees.

## Notes

## Referen ces

1. Aamodt, A., and Plaza, E. Case-based reasoning: Foundational issues, methodological variations, and system approaches. AI Communications, 7, 1 (1994), 39–59.

2. Aiken, L.S., and West, S.G. Multiple Regression: Testing and Interpreting Interactions. Newbury Park, CA: Sage, 1991.

3. Althuizen, N. The relative performance of different methods for selecting creative marketing personnel. Marketing Letters, 23, 4 (2012), 973–985.

4. Althuizen, N.; Wierenga, B.; and Rossiter, J.R. The validity of two brief measures of creative ability. Creativity Research Journal, 22, 1 (2010), 53–61.

5. Amabile, T.M. The Social Psychology of Creativity. New York: Springer, 1983.

6. Amabile, T.M. Creativity in Context. Boulder, CO: Westview Press, 1996.

7. Austin, R.D.; Devin, L.; and Sullivan, E.E. Accidental innovation: Supporting valuable unpredictability in the creative process. Organization Science, 25, 3 (2012), 1505–1522.

8. Benbasat, I., and Dexter, A.S. An experimental evaluation of graphical and color enhanced information presentation. Management Science, 31, 11 (1985), 1348–1364.

9. Besemer, S., and O’Quin, K. Analyzing creative products: Refinement and test of a judging instrument. Journal of Creative Behavior, 20, 2 (1986), 115–125.

10. Blattberg, R.C., and Neslin, S.A. Sales Promotion: Concepts, Methods and Strategies. Englewood Cliffs, NJ: Prentice Hall, 1990.

11. Boden, M.A. What is creativity? In M.A. Boden (ed.), Dimensions of Creativity. Cambridge: MIT Press, 1994, pp. 75–117.

12. Brodsky, A.; Egge, N.E.; and Wang, X.S. Supporting agile organizations with a decision guidance query language. Journal of Management Information Systems, 28, 4 (Spring 2012), 39–68.

13. Burroughs, J.E.; Dahl, D.W.; Moreau, C.P.; Chattopadhyay, A.; and Gorn, G.J. Facilitating and rewarding creativity during new product development. Journal of Marketing, 75, 4 (2011), 53–67.

14. Cattell, R.B.; Eber, H.W.; and Tatsuoka, M.M. Handbook for the Sixteen Personality Factor Questionnaire. Champaign, IL: Institute for Personality and Ability Testing, 1970.

15. Cheung, P.-K.; Chau, P.Y.K.; and Au, A.K.K. Does knowledge reuse make a creative person more creative? Decision Support Systems, 45, 2 (2008), 219–227.

16. Christensen, B.T., and Schunn, C.D. The relationship of analogical distance to analogical function and preinventive structure: The case of engineering design. Memory & Cognition, 35, 1 (2007), 29–38.

17. Connolly, T.L.; Jessup, M.; and Valacich, J.S. Effects of anonymity and evaluative tone on idea generation in computer-mediated groups. Management Science, 36, 6 (1990), 698–703.

18. Couger, J.D.; Higgins, L.F.; and McIntyre, S.C. (Un)structured creativity in information systems organizations. MIS Quarterly, 17, 4 (1993), 375–397.

19. Dahl, D.W., and Moreau, C.P. The influence and value of analogical thinking during new product ideation. Journal of Marketing Research, 39, 1 (2002), 47–60.

20. Dean, D.L.; Hender, J.M.; Rodgers, T.L.; and Santanen, E.L. Identifying quality, novelty, and creative ideas: Constructs and scales for idea evaluation. Journal of the Association for Information Systems, 7, 10 (2006), 646–699.

21. De Dreu, C.K.W.; Baas, M.; and Nijstad, B.A. Hedonic tone and activation level in the mood–creativity link: Toward a dual pathway to creativity model. Journal of Personality and Social Psychology, 94 (2008), 739–756.

22. De Luca, L.M., and Atuahene-Gima, K. Marketing knowledge dimensions and crossfunctional collaboration: Examining the different routes to product innovation performance. Journal of Marketing, 71, 1 (2007), 95–112.

23. Diehl, M., and Stroebe, W. Productivity loss in brainstorming groups: Toward the solution of a riddle. Journal of Personality and Social Psychology, 53, 3 (1987), 497–509.

24. Elam, J.J., and Mead, M. 1990. Can software influence creativity? Information Systems Research, 1, 1 (1990), 1–22.

25. Fang, X.; Hu, P.J.; Chau, M.; Hu, H.; Yang, Z.; and Sheng, O.R.L. A data-driven approach to measure Web site navigability. Journal of Management Information Systems, 29, 2 (Fall 2012), 173–212.

26. Finke, R.A.; Ward, T.B.; and Smith, S.M. Creative Cognition: Theory, Research, and Applications. Cambridge: MIT Press, 1992.

27. Fjermestad, J., and Hiltz, S.R. An assessment of group support systems experimental research: Methodology and results. Journal of Management Information Systems, 15, 3 (Winter 1998–99), 7–149.

28. Garfield, M.J. Creativity support systems. In F. Burnstein and C.W. Holsapple (eds.), Handbook on Decision Support Systems 2: Variations. Heidelberg: Springer, 2008, pp. 745–758.

29. Garfield, M.J.; Taylor, N.J.; Dennis, A.R.; and Satzinger, J.W. Research report: Modifying paradigms—Individual differences, creativity techniques, and exposure to ideas in group idea generation. Information Systems Research, 12, 3 (2001), 322–333.

30. Gassmann, O., and Zeschky, M. Opening up the solution space: The role of analogical thinking for breakthrough product innovation. Creativity and Innovation Management, 27, 2 (2008), 97–106.

31. Gavetti, G., and Rivkin, J.W. 2005. How strategists really think: Tapping the power of analogy. Harvard Business Review, 83, 4 (2005), 54–63.

32. Gentner, D. Structure-mapping: A theoretical framework for analogy. Cognitive Science, 7, 2 (1983), 155–170.

33. Gick, M.L., and Holyoak, K.J. Analogical problem solving. Cognitive Psychology, 12, 3 (1980), 306–355.

34. Goel, A.K. Design, analogy, and creativity. IEEE Expert, 12, 3 (1997), 62–70.

35. Goff, K., and Torrance, E.P. Abbreviated Torrance Test for Adults Manual. Bensenville, IL: Scholastic Testing Service, 2002.

36. Goldstein, D.K. Product managers’ use of scanner data: A story of organizational learning. In R. Deshpande (ed.), Using Market Knowledge. Thousand Oaks, CA: Sage, 2001, pp. 164–191.

37. Gregan-Paxton, J., and Cote, J. How do investors make predictions? Insights from analogical reasoning research. Journal of Behavioral Decision Making, 13, 3 (2000), 307–327.

38. Guilford, J.P. Creativity. American Psychologist, 5, 9 (1950), 444–454.

39. Hender, J.M.; Dean, D.L.; Rodgers, T.L.; and Nunamaker, J.F., Jr. An examination of the impact of stimuli type and GSS structure on creativity: Brainstorming versus non-brainstorming techniques in a GSS environment. Journal of Management Information Systems, 18, 4 (Spring 2002), 59–85.

40. IBM. Capitalizing on Complexity: Insights from the Global Chief Executive Officer Study. Somers, NY: IBM Global Business Services, 2010.

41. James, L.R.; Demaree, R.G.; and Wolf, G. Estimating within-group interrater reliability with and without response bias. Journal of Applied Psychology, 69, 1 (1984), 85–98.

42. Jensen, M.L.; Lowry, P.B.; and Jenkins, J.L. Effects of automated and participative decision support in computer-aided credibility assessment. Journal of Management Information Systems, 28, 1 (2011), 201–233.

43. Kabanoff, B., and Rossiter, J.R. Recent developments in applied creativity. In C.L. Cooper and I.T. R obertson (eds.), International Review of Industrial and Organizational Psychology. London: Wiley, 1994, pp. 283–324.

44. Kilgour, M., and Koslow, S. 2009. Why and how do creative thinking techniques work? Trading off originality and appropriateness to make more creative advertising. Journal of the Academy of Marketing Science, 37 (2009), 298–309.

45. Kolodner, J.L. Case-Based Reasoning. San Mateo, CA: Morgan Kaufmann, 1993.

46. Kolodner, J.L., and Wills, L.M. Paying attention to the right thing: Issues of focus in case-based creative design. In D. L eake (ed.), Proceedings of the AAAI Case-Based Reasoning Workshop. Menlo Park, CA: AAAI Press, 1993, pp. 19–25.

47. Lamm, H., and Trommsdorff, G. Group versus individual performance on tasks requiring ideational proficiency (brainstorming): A review. European Journal of Social Psychology, 3, 4 (1973), 361–388.

48. Leake, D.B. CBR in context: The present and future. In D.B. Leake (ed.), Case-Based Reasoning: Experiences, Lessons, and Future Directions. Menlo Park, CA: AAAI Press, 1996, pp. 1–35.

49. LeBreton, J.M., and Senter, J.L. Answers to 20 questions about interrater reliability and interrater agreement. Organizational Research Methods, 11, 4 (2008), 815–852.

50. Lee, H., and Choi, B. Knowledge management enablers, processes, and organizational performance: An integrative view and empirical examination. Journal of Management Information Systems, 20, 1 (Summer 2003), 179–228.

51. Liang, T.-P., and Turban, E. Case-based reasoning and its applications. Expert Systems with Applications, 6, 1 (1993), 1–2.

52. Lilien, G.L.; Van Bruggen, G.H.; Rangaswamy, A.; and Starke, K. DSS effectiveness in marketing resource allocation decisions: Reality vs. perception. Information Systems Research, 15, 3 (2004), 216–235.

53. MacCrimmon, K.R., and Wagner, C. Stimulating ideas through creativity software. Management Science, 40, 11 (1994), 1514–1532.

54. Maher, M.L.; Balachandran, M.B.; and Zhang, D.M. Case-Based Reasoning in Design. Hillsdale, NJ: Lawrence Erlbaum, 1995.

55. Massetti, B. An empirical examination of the value of creativity support systems on idea generation. MIS Quarterly, 20, 1 (1996), 83–97.

56. Meetlatcomité Nederland. Scoren boven op of onder de lijn: Succesvolle promotion cases [Scoring Above, On or Under the Line; Successful Promotion Cases]. Breukelen: Van Lindonk, 1994.

57. Moorman, C., and Miner, A.S. The impact of organizational memory on new product performance and creativity. Journal of Marketing Research, 34, 1 (1997), 91–106.

58. Müller-Wienbergen, F.; Müller, O.; Seidel, S.; and Becker, J. Leaving the beaten tracks in creative work—A design theory for systems that support convergent and divergent thinking. Journal of the Association for Information Systems, 12, 11 (2011), article 2.

59. Newell, A., and Simon, H. Human Problem Solving. Englewood Cliffs, NJ: Prentice Hall, 1972.

60. Plucker, J.A., and Renzulli, J.S. Psychometric approaches to the study of human creativity. In R.J. Sternberg (ed.), Handbook of Creativity. Cambridge: Cambridge University Press, 1999, pp. 35–61.

61. Remus, W. Graduate students as surrogates for managers in experiments on business decision making. Journal of Business Research, 14, 1 (1986), 19–25.

62. Riesbeck, C.K., and Schank, R.C. Inside Case-Based Reasoning. Hillsdale, NJ: Lawrence Erlbaum Associates, 1989.

63. Rietzschel, E.F.; Nijstad, B.A.; and Stroebe, W. Relative accessibility of domain knowledge and creativity: The effects of knowledge activation on the quantity and originality of generated ideas. Journal of Experimental Social Psychology, 43, 6 (2007), 933–946.

64. Santanen, E.L.; Briggs, R.O.; and De Vreede, G.-J. Causal relationships in creative problem solving: Comparing facilitation interventions for ideation. Journal of Management Information Systems, 20, 4 (Spring 2004), 167–197.

65. Satzinger, J.W.; Garfield, M.J.; and Nagasundaram, M. The creative process: The effects of group memory on individual idea generation. Journal of Management Information Systems, 15, 4 (Spring 1999), 143–160.

66. Seidel, S.; Müller-Wienbergen, F.; and Becker, J. The concept of creativity in the information systems discipline: Past, present, and prospects. Communications of the Association for Information Systems, 27, 14 (2010), 217–242.

67. Shalley, C.E., and Perry-Smith, J.E. Effects of social-psychological factors on creative performance: The role of informational and controlling expected evaluation and modeling experience. Organizational Behavior and Human Decision Processes, 84, 1 (2001), 1–22.

68. Shneiderman, B. Creativity support tools: Accelerating discovery and innovation. Communications of the ACM, 50, 12 (2007), 20–32.

69. Simon, H.A. Two heads are better than one: The collaboration between AI and OR. Interfaces, 17, 4 (1987), 8–15.

70. Simonton, D.K. Scientific creativity as constrained stochastic behavior: The integration of product, person, and process perspectives. Psychological Bulletin, 129, 4 (2003), 475–494.

71. Stein, E.W., and Zwass, V. Actualizing organizational memory with information systems. Information Systems Research, 6, 2 (1995), 85–117.

72. Sternberg, R.J. Preface. In R.J. Sternberg (ed.), The Nature of Creativity: Contemporary Psychological Perspectives. Cambridge: Cambridge University Press, 1988, p. vii.

73. Sternberg, R.J., and Dress, N.K. Creativity for the new millennium. American Psychologist, 56 (2001), 332.

74. Tiwana, A., and McLean, E. Expertise integration and creativity in information systems development. Journal of Management Information Systems, 22, 1 (Summer 2005), 13–43.

75. Toop, A. European Sales Promotion: Great Campaigns in Action. London: Kogan Page, 1992.

76. Van Bruggen, G.H.; Smidts, A.; and Wierenga, B. Improving decision making by means of a marketing decision support system. Management Science, 44, 5 (1998), 645–658.

77. Ward, T.B. Structured imagination: The role of category structure in exemplar generation. Cognitive Psychology, 27, 1 (1994), 1–40.

78. Ward, T.B. Analogical distance and purpose in creative thought: Mental leaps versus mental hops. In K.J. H olyoak, D. G entner, and B.N. Kokinov (eds.), Advances in Analogy Research. Sofia: New Bulgarian University Press, 1998, pp. 221–230.

79. Ward, T.B. Cognition, creativity, and entrepreneurship. Journal of Business Venturing, 19, 2 (2004), 173–188.

80. Woodman, R.W.; Sawyer, J.E.; and Griffin, R.W. Toward a theory of organizational creativity. Academy of Management Review, 18, 2 (1993), 293–321.

81. Yang, Y.; Singhal, S.; and Xu, Y.C. Alternate strategies for a win-win seeking agent in agent–human negotiations. Journal of Management Information Systems, 29, 3 (Winter 2012–13), 223–256.

## Appendix A: Example of a Close Case Stored in the CBR System

In the ea rly 1990s, con sumers w ere b ecomin g less an d less loya l. Hence, promotions were increasingly important to persuade customers to switch brands, stimulate repeat purchases, and increase (behavioral) loyalty. A few beer brands offered deep price discounts, sacrificing profit margins. Amstel beer—produced by Heineken— developed a promotion inspired by the popular game “Bingo.” Underneath the crown cap of Amstel beer bottles, the consumer could find a number, which had to be put on a bingo card. If the consumer had a full card (“Bingo”), he or she could win 454 euros. However, the consumer also had to come up with a slogan. The best slogans were rewarded with 450 euros. In total, the prize money was 113,445 euros. In a period of nine weeks, Amstel received a total of 240,000 complete Bingo cards. Results after nine weeks (three rounds of three weeks): increased traffic in stores, increased sales, Amstel’s market share rose 6.4 percent (to 27 percent). The campaign was supported by brochures (at retail outlets), television and radio commercials, outdoor advertisements, regular advertisements, point of sales material, and crate covers. In 1993, the campaign was repeated.

## 1. G eneral Information:

001 Campaign Title: ‘Amstel Bingo

002 Start Date: June 1, 1992

003 End Date: August 31, 1992

004 Short Case Description: “double click here”

005 Full Case Description: ‘see casebook: nr. 45

2. Market Situation:

2.1 Product Category Situation:

006 Product Category Name (broad): #‘alcoholic beverages’

007 Product Category Name (narrow): ‘regular beer

008 Category Life Cycle Phase: #maturity 009 Price Level: {5-49 euros} 010 Involvement: #medium 011 Loyalty: #high 012 Purchase Motivation: #transformational 013 Promotion Intensity: #high 2.2 Product/Brand Situation: 014 Product/Brand Name: ‘Amstel Beer’ 015 Product/Brand Life Cycle Phase: #maturit 016 Relative Price: #average 017 Distinctiveness: #low 021 Seasonality: #medium 2.3 T argeted Customers: 022 Country/Region: #‘the netherlands’ 025 Socioeconomic Class: {middle, lower} 2.4 Competitive Environment: 028 Company Name: ‘Heineken 029 Market Leadership: true 030 Competition Intensity: #high 031 Market Turbulence: #low 3. Campaign Objectives: 032 Main Objective(s): {increase repeat purchase, increase trial purchase, support/reinforce product/brand image} 4. Constraints: 033 Budget: #high 035 Campaign Duration: #‘medium-term (several months) 036 Campaign Frequency: #‘repeated campaign 5. Campaign Design: 038 SP Theme: {family & friends, sports & entertainment} 039 SP Technique: {contest/competition} 040 SP Slogan: ‘Amstel Bingo 041 SP Support: {in-store/POS promotion material, outdoor advertising, promotion packaging, radio/tv commercial} 042 SP Offer Value (in Euros): {50 - 999 euros} 043 SP Distribution/Handling Channel: {postal, retail} 6. Campaign Execution: 045 Executive Agency Name: ‘Bartels/Verdonk Impuls’ 047 Planned Running Time: #‘1 month - 3 months 7. Outcomes: 059 Repeat Intention: true 058 Actual Running Time: #‘as planned 065 Product/Brand Market Share: #‘major increase 056 SP Offer Attractiveness: #high 063 Product/Brand Image Support: #‘positive

064 Product/Brand Sales: #‘major increase

054 Customer Information: true

049 Total Number of Respondents: 240000

060 Main Objective(s) Attainment: true

## Appendix B: Example of a Remote Case Stored in the CBR System

Fren ch Ra ilwa ys ha d tw o ra il ca rds design ed for 12–26 year olds (Carte Jeune and Carré Jeune) that offer free travel during the summer. Peak sales occur in May, when summer travel plans are made. Younger customers represent prospective fullfare-paying passengers. It was important to demonstrate to young people that rail travel is economical, so OK! French Railways teamed up with the rock group A-ha. Regional activities centered on A-ha’s concert tour (15 cities): hostesses drove to places where young people gather, distributing 700,000 game cards that had to be inserted in a machine at the railway station to win A-ha prizes. Next to the machine was a booth selling the Carte Jeune and Carré Jeune. At the national level, a mail-in competition was held, for which entry forms could be obtained at railway stations. The contestants answered questions related to both A-ha and the rail cards in order to win a USA-rock-capitals tour for two weeks (and other prizes). At the end of the promotion, an additional A-ha concert was held near Paris, offering 16,000 free seats. Results: almost one-third of the ±8.5 million young French people in the target age group were reached, 8.28 percent of the game cards had been inserted in the machines, 2.64 percent of the national entry forms were completed and returned. Carré Jeune sales increased 13 percent and Carte Jeune 20 percent.

1. G eneral Information:

001 Campaign Title: ‘French Railways Get into Rock

002 Start Date: May 1, 1988

003 End Date: June 10, 1988

004 Short Case Description: “double click here”

005 Full Case Description: ‘see European Sales Promotion: pp 112-116

2. Market Situation:

2.1 Product Category Situation:

006 Product Category Name (broad): #‘travel & leisure

007 Product Category Name (narrow): ‘rail tickets

008 Category Life-Cycle Phase: #maturity

009 Price Level: {5-49 euros}

010 Involvement: #low

011 Loyalty: #low

012 Purchase Motivation: #informational

013 Promotion Intensity: #low

2.2 Product/Brand Situation:

014 Product/Brand Name: ‘rail cards

015 Product/Brand Life-Cycle Phase: #maturity

016 Relative Price: #‘below average’ 017 Distinctiveness: #medium 021 Seasonality: #high

2.3 Targeted Customers: 022 Country/Region: #france 023 Age Category: {teenagers, adolescents} 027 B-to-B: false

2.4 Competitive Environment: 028 Company Name: ‘French Railways’ 029 Market Leadership: true 030 Competition Intensity: #low 031 Market Turbulence: #low

3. Campaign Objectives: 032 Main Objective(s): {attract new customers, support/reinforce product/ brand image}

4. Constraints: 033 Budget: #high 035 Campaign Duration: #‘medium-term (several months)’ 036 Campaign Frequency: #‘single campaign’

5. Campaign Design: 037 Total Number of Targeted Customers: 8500000 038 SP Theme: {music, travel & leisure} 039 SP Technique: {character/celebrity promotion, contest/competition, sweepstakes/lottery} 041 SP Support: {display, festivity, outdoor advertising, radio/tv commercial} 042 SP Offer Value (in Euros): {5-49 euros, 50-999 euros} 043 SP Distribution/Handling Channel: {own company}

6. Campaign Execution: 045 Executive Agency Name: ‘Marco Polo’ 046 Endorsement: {other...} 047 Planned Running Time: #‘1 month-3 months

7. Outcomes: 049 Total Number of Respondents: 2800000 050 Response Rate (in %): 33.0 054 Customer Information: true 056 SP Offer Attractiveness: #high 058 Actual Running Time: #‘as planned 060 Main Objective(s) Attainment: true 063 Product/Brand Image Support: #‘positive 064 Product/Brand Sales: #‘minor increase’
