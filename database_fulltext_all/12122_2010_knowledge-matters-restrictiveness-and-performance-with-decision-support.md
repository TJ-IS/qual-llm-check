---
otero_id: 12122
otero_key: "CZWXA6KS"
title: "Knowledge matters: Restrictiveness and performance with decision support"
authors: "Michael J. Davern; Arnold Kamis"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.04.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge matters: Restrictiveness and performance with decision support

Michael J. Davern <sup>a,</sup>⁎, Arnold Kamis <sup>b</sup>

<sup>a</sup> Department of Accounting and Business Information Systems, The University of Melbourne, Victoria 3010, Australia

<sup>b</sup> Department of Information Systems and Operations Management, Suffolk University, Boston, MA 02108, USA

## a r t i c l e i n f o

Article history: Received 16 October 2008 Received in revised form 19 March 2010 Accepted 4 April 2010 Available online 9 April 2010

Keywords: User knowledge System restrictiveness Effort/accuracy Data Envelopment Analysis

## a b s t r a c t

We study 56 subjects of varying knowledge in a preferential choice task, aided by one of two Decision Support Systems (DSS) of different restrictiveness: an eliminative tool (ELIM) and a parametric search tool (PS). Using a novel measure for performance based on Data Envelopment Analysis (DEA), we <sup>fi</sup>nd that the gains due to effort are greater with the less restrictive DSS. Surprisingly knowledge has a negative effect on performance, an effect exacerbated with the less restrictive DSS. We interpret our results in terms of knowledge-effort substitution and the nature of knowledge relative to the restrictiveness of the DSS.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Decision support tools are ubiquitous. They are commonly found both as stand-alone applications and as embedded tools in larger systems. They have been applied across a wide range of domains including consumer purchases in e-commerce [32], production planning (e.g., [22,23]), revenue yield management (e.g., [20,21,57]) and corporate recovery [3]. Experimental research into the behavioral aspects of effective decision support has a long tradition, from the wellknown Minnesota experiments [24] to the studies by Todd and Benbasat [7,62–65]. Yet, important gaps in the literature remain.

Much of the prior research has adopted a behavioral decision theory perspective focusing on factors such as effort and accuracy [48], economic incentives [65], perceived usefulness [22,23], decisional guidance [55], naturalness [35], forms of feedback [37,51] and descriptions of the decision tool and its prior performance [22]. Performance however is a function of both individual user characteristics and technology design in the context of a speci<sup>fi</sup>c task [19]. In comparing technology designs, a key factor is the range of decision strategies supported, which is well re<sup>fl</sup>ected in the relative degree of system restrictiveness (i.e., a more restrictive system supports fewer strategies). Almost axiomatically, user domain knowledge is a critical individual characteristic in exploring performance with a DSS. Despite the volume of research in decision support, rather surprisingly, user domain knowledge has not commonly been explicitly featured as a central construct (for exceptions see [5,39,61]). Only in the comparisons of expert versus novice behavior in expert systems research does user domain knowledge take the centre stage [3,41]. This is often by necessity, since many of the tasks in the expert systems context are nonnormative – there is no objective correct decision even ex post – and thus the focus is on decision processes and expertise. In contrast, knowledge has been less central in the multi-alternative, multi-attribute preferential choice problems that have dominated the behavioral decision theory perspective on decision support research (e.g., [65]).

That user domain knowledge affects performance seems intuitive — even in the context of preferential choice tasks where knowledge has not been a primary variable of study. However the nature of the effect of user domain knowledge is very much an empirical question. For example, knowledge could be very helpful, improving the problem solving performance obtained for a given level of effort [42], even without decision support. Alternatively the domain knowledgeable user may be less mindful [36], or more complacent and thereby fail to take full and effective advantage of the functionality offered by a decision tool. The knowledgeable user may be better equipped to leverage the power of a decision tool, or alternatively, as is the case in knowledgebased systems, the user may be less likely to incorporate the tool into their established decision processes [40,41].

Silver [54 p.52] de<sup>fi</sup>ned system restrictiveness as: “… the degree to which and the manner in which a Decision Support System limits its users' decision making processes to a subset of all possible processes”. A system that is more restrictive provides support for a smaller set of possible decision processes than a less restrictive system. System restrictiveness thus captures the extent to which a decision support system enables and constrains user behavior. The effects of system restrictiveness are however an open empirical question. A more restrictive system may yield greater performance as it provides a more rigid structure to the decision process, potentially reducing error. Alternatively, a less restrictive system offers greater support to the user in carrying out the task in the manner they see appropriate. Intuitively, user domain knowledge is likely to interact with system restrictiveness. For example, a more restrictive system in limiting behaviors may be bene<sup>fi</sup>cial to the less knowledgeable user but constraining and insuf<sup>fi</sup>ciently <sup>fl</sup>exible for the more knowledgeable user.

The purpose of this study is to empirically explore the potentially divergent effects of user domain knowledge and system restrictiveness. Furthermore, we build on the cumulative research tradition that exists within the effort/accuracy framework (e.g., [65]) that has dominated the behavioral decision theory perspective on decision support research. Consistent with prior research we conduct our study in the context of a preferential choice task. Speci<sup>fi</sup>cally this research asks the question:

In a preferential choice task, what is the effect of domain knowledge and effort on performance with decision tools of varying system restrictiveness?

The paper is structured as follows. In the next section we review the key constructs and develop our theoretical perspectives on the effect of effort and knowledge on performance with decision tools of different degrees of restrictiveness. In the third section we present our research method. The results of our experimental study are presented in the fourth section, followed by a discussion and review of the limitations. We conclude with implications for research and practice.

## 2. Theory development

## 2.1. The effort-accuracy trade-off

Preferential choice tasks entail selecting among competing alternatives based on one's likes and dislikes. There is often no universal best choice, but optimality can be determined for a given set of preferences. The complexity of a preferential choice task is derived from the number of competing alternatives, the number attributes describing the alternatives and the range of values the attributes may take. Within a preferential choice task, a range of decision strategies of varying degrees of effort and accuracy have been observed and described in the behavioral decision theory literature [30,34]. For example, low effort, low accuracy strategies include Random Choice, Satis<sup>fi</sup>cing, the Lexicographic Strategy and Elimination by Aspects [48]. These strategies are non-compensatory strategies; that is, they do not directly involve balancing competing preferences for different attributes. In contrast, compensatory strategies attempt to explicitly balance competing preferences for the different attributes of the alternatives and include most notably the high effort, high accuracy Weighted Additive strategy. In the Weighted Additive strategy, each attribute dimension is weighted relative to its importance, and the weighted values of each alternative are summed to determine the best alternative. In choosing a decision strategy, a decision maker has to balance the trade-off between effort and accuracy.

Accuracy is a measure of the degree to which the selected alternative satis<sup>fi</sup>es a decision maker's competing preferences, relative to some benchmark. The Weighted Additive strategy is often used as a benchmark because it is fully compensatory and decision makers typically agree that it is a good strategy to use, whether they follow it or not [48]. This benchmark however is confounded by the constructive nature of preferences [46,47], an issue we explore further below when we introduce a benchmark based on Data Envelopment Analysis (DEA).

Effort is the cognitive effort employed in making trade-offs or evaluating alternatives or attributes. At a micro-level, effort can be measured by counting the Elementary Information Processing operators (e.g., compare, add, and read) required by a decision maker's chosen strategy [43,48]. Alternatively effort can be measured more holistically as time to execute the strategy [48].

Decision makers recognize the trade-offs between effort and accuracy and select an appropriate strategy as an adaptive response to the goals and constraints they face (e.g., incentives for accuracy versus limited available time for strategy execution). Extending the Effort-Accuracy research, Todd and Benbasat found that decision tools can add value to the user by decreasing effort given a desired level of accuracy [62] or increasing the accuracy achieved given a certain level of effort [65]. The twin objectives, accuracy maximization and effort minimization, generate value to a user as he or she makes trade-offs with a decision support tool, although effort minimization tends to take precedence over accuracy maximization [7,64]. The most important goal for decision support tools in this context is to reduce the effort required to execute a given strategy. In so doing, they make a more accurate strategy available to the user for less effort; enabling improved performance by changing the effort-accuracy trade-off.

## 2.2. Knowledge, effort and performance

The Effort-Accuracy work does not directly consider the role of the user's knowledge of the task domain (i.e., the knowledge the user would employ in carrying out the task in the absence of decision support). In the preferential choice task context, user domain knowledge may include knowledge of attribute ranges, attribute trade-offs or attribute diagnosticity, i.e., the attribute that best distinguishes between alternatives [66]. Domain knowledge may also be a speci<sup>fi</sup>cation of a stereotypical ideal [27,60], for example, in a computer purchasing context a user's knowledge may be of the attribute values for their “dream” computer. Knowledge can substitute for effort, i.e., an exchange of preparation for deliberation [42]. As substitutes, a decision maker can compensate for a lack of knowledge with additional effort, and still achieve a given level of performance. Conversely, a knowledgeable decision maker can achieve a given level of performance with less effort than a less knowledgeable individual. Newell [42] elegantly characterizes this as a trade-off between knowledge and effort in terms of “equi-performance isobars” (see Fig. 1, below). Thus any consideration of knowledge effects is potentially confounded if it does not also consider effort effects. Similarly, any study of effort is potentially confounded if it does not consider or appropriately control for knowledge.

In the consumer purchase decision (a preferential choice task) we explore here, domain knowledge pertains to the decision maker's knowledge of the product space (e.g., ranges of attribute values and appropriate trade-offs between different attributes). Effort relates to the decision maker's work in searching the product space to acquire domain knowledge about the products, attribute trade-offs and in making the ultimate selection of a product consistent with his or her preferences [59]. Indeed, in Newell's original <sup>fi</sup>gure, from which Fig. 1 is adapted, he labels the axes as “Immediate Knowledge (preparation) and Search

![](/api/attachments/CZWXA6KS/fulltext/images/91db51eada6af589b7e8658e189f495f3f6862c013a9efb8e0e353415c99082b.jpg)  
Fig. 1. Performance and the knowledge-effort relationship. (Adapted from [42 Fig. 2–19]).

Knowledge (deliberation)”, which in the present context translates to a priori domain knowledge and search effort.

As per Fig. 1, there are a range of possible means of achieving a given level of performance from high knowledge and low effort to high effort and low knowledge. Not surprisingly, there are diminishing marginal returns in terms of performance for increasing reliance on either factor without a concomitant increase in the complementary factor. Thus the equi-performance isobars are convex, in a similar manner to the convexity commonly observed with indifference curves in utility analysis. To the extent that the isobars are convex, knowledge and effort can also act as complements and operate synergistically, with higher levels of performance being obtained when they work in combination rather than in isolation.

While our interest here is in domain knowledge, it should be recognized that users may have other sorts of knowledge that are relevant to task performance. For example, there is meta-knowledge: knowledge of how to make a decision (e.g. of decision strategies, such as those discussed by Payne et al. [48], or knowledge about how to use speci<sup>fi</sup>c decision support tools). For example, McKay and Elam [39] <sup>fi</sup>nd that a lack of knowledge of how to use a decision support tool restricts the performance bene<sup>fi</sup>ts that would otherwise be obtained from superior domain knowledge. Importantly, as a matter of context and scope our concern here is with domain knowledge, not expertise or the associated expert versus novice distinctions. Domain knowledge is a necessary, but not suf<sup>fi</sup>cient, condition for expertise [52], and thus care should be taken in generalizing our <sup>fi</sup>ndings beyond matters of knowledge to those of expertise. For brevity we use the term knowledge hereafter to refer exclusively to domain knowledge.

In summary, the foregoing suggests that for a given level of effort, users with greater knowledge will achieve greater accuracy (i.e., a higher equiperformance isobar in Fig. 1). Similarly, for a given level of knowledge, users who exert greater effort will achieve greater accuracy. This is consistent with prior effort-accuracy research, while controlling for any potential effort-knowledge substitution effect (per Fig. 1). We next consider the issue of system restrictiveness and how it may in<sup>fl</sup>uence the interrelationships between knowledge, effort and accuracy.

## 2.3. Decision support tools and restrictiveness

Following Silver [53,54] we assess system restrictiveness in terms of the processes that the system supports (what Chu and Elam [14] refer to as Physical System Restrictiveness). Simplistically, a less restrictive system is one that supports a greater range of processes. The de<sup>fi</sup>nition and measurement of restrictiveness is thus relative rather than absolute. The degree of restrictiveness of a system can only be measured relative to another system, and even then the set of processes provided by the more restrictive system must be completely subsumed by the less restrictive system to make a de<sup>fi</sup>nitive measurement (lest measurement require comparisons of the restrictiveness of the different processes themselves).

In the context of the effort/accuracy framework system restrictiveness is re<sup>fl</sup>ected in the provision of support for different decision strategies, with the more restrictive system supporting fewer decision strategies than the less restrictive system. For ease of exposition and understanding we explore a theory in this regard in terms of the speci<sup>fi</sup>c tools that we developed to operationalize restrictiveness with differing decision strategies. This is particularly pertinent because restrictiveness is a relative concept. Thus we focus our attention on a tool that is relatively less restrictive than a benchmark tool. However we believe our theory and hypotheses apply more broadly to any comparison of decision tools that support differing decision strategies where one set of supported strategies is a complete subset of the strategies supported by the less restrictive tool.

We developed two tools: ELIM and PS. The eliminative strategy on which ELIM is based is a commonly used decision strategy and the parametric search tools on which PS is based are commonplace in decision support. The decision strategy in ELIM allows search focusing on only one criterion at a time, whereas a parametric search such as implemented in PS allows simultaneous consideration of one or more criteria. As a result ELIM is a more restrictive tool than PS. Put simply; PS can do everything ELIM can, and more. ELIM thus provides the benchmark for understanding performance with the relatively less restrictive tool PS.

The ELIM tool we developed permits a user to select each attribute in turn (from most important to least important) sorting on the given attribute and <sup>fi</sup>ltering out all the alternatives which are above (for an attribute to be maximized) or below (for an attribute to be minimized) a criterion value for that attribute, until a single alternative or trivially small set of alternatives remain. To enhance ease of use, users are provided with a base or all inclusive criterion value for each attribute. For example, in the case of price, this is the maximum price in the product space, since price is an attribute whose value is to be minimized. (See Fig. 2a and b for sample screenshots of the ELIM tool).

The PS tool we developed permits a user to specify ranges (maximum and minimum thresholds) for each attribute and returns a consideration set comprising all products with attribute values in the speci<sup>fi</sup>ed ranges. To enhance ease of use, for each attribute, users are provided with the maximum and minimum values present in the product space. Unlike ELIM, iterative use of PS always applies the threshold ranges to the entire product space, rather than just the interim result space. However, it is possible to perfectly mimic ELIM with PS, by restricting only one attribute threshold at a time successively. Since ELIM provides a subset of the functionality of PS, it is by de<sup>fi</sup>nition a more restrictive tool. (See Fig. 3 for a sample screenshot of the PS tool).

The effect of differing levels of system restrictiveness on accuracy is open to debate. Restrictiveness, like any constraint, is both a limiter and an enabler of behavior [44]. In other words, by constraining behavior a restrictive system may direct the decision maker towards a more accurate decision strategy, whereas the less restrictive system can confuse the user by virtue of the greater <sup>fl</sup>exibility it provides. Alternatively a less restrictive system provides greater functionality and also is more likely to support the decision processes that are natural [35] to the user — a <sup>fi</sup>t argument [18,19]. Thus in the abstract it is not possible to say whether greater restrictiveness is good or bad in terms of performance outcomes. Contextualizing this into a decision support context, the relative merits of restrictiveness depend on the speci<sup>fi</sup>c decision strategies that are supported by the different systems. For example, suppose system A supports decision strategies D1 and D2, whereas system B supports only D1 (i.e., system B is more restrictive). The relative performance outcomes of restrictiveness in this context are not due simply to the restrictiveness but rather which decision strategy is better. For example, if D2 is a superior decision strategy to D1, then system A dominates. Conversely if D1 is the superior strategy then it is possible that the same performance outcomes may result or that indeed system B may dominate (the critical factor in this case is the effect of the additional complexity and confusion, if any, created by allowing the user greater choice of strategy in System A).

Following the above logic our comparison of PS and ELIM is a situation where the less restrictive system (PS) provides support for a more accurate decision strategy. Speci<sup>fi</sup>cally, it permits simultaneous rather than sequential consideration of attributes, and it allows for consideration of both upper and lower thresholds for attribute values. We particularly framed our tools and the strategies they support in this way because it is more re<sup>fl</sup>ective of the structures of different DSS in practice. Furthermore, we see relatively little merit in developing a decision support tool that expands the available decision strategies to include less optimal strategies than that which are available in a more restrictive tool (although a <sup>fi</sup>t argument may suggest inclusion of a less optimal strategy, the more rational approach to address problems of <sup>fi</sup>t would be to train the user to improve the <sup>fi</sup>t with the more optimal strategies).

![](/api/attachments/CZWXA6KS/fulltext/images/6662279381f76454d0b30976df5dddb07fd359f6effa2b63df9fa880aafd5423.jpg)

![](/api/attachments/CZWXA6KS/fulltext/images/2d487e141d85534741410d1efc7bc8c8d617e1c216c4f86349906c2dd1fe269e.jpg)  
Fig. 2. a: ELIM sample screenshot (<sup>fi</sup>rst screen). b: ELIM sample screenshot (subsequent screen)

![](/api/attachments/CZWXA6KS/fulltext/images/a97315411d54e430b38b490a795cc40157f1356ef033b2fcc3e4f55a0d43753c.jpg)  
Fig. 3. PS sample screenshot.

## 2.4. Hypotheses

Building on the above theory we develop hypotheses surrounding our three independent variables (effort, knowledge and restrictiveness) and their effects on the dependent variable (accuracy). More speci<sup>fi</sup>cally our hypotheses are broken into groupings, as follows: effort effects (H1 and H2), knowledge effects (H3 and H4) and interaction effects (H5 and H6). In each case we examine two hypotheses one for the less restrictive tool (PS), and one for the less restrictive tool (PS) relative to the more restrictive tool (ELIM). In experimental terms the ELIM tool is our control condition, with PS providing the treatment for the relaxing of restrictiveness. We describe the logic for this design as follows. By de<sup>fi</sup>nition a highly restrictive tool provides little <sup>fl</sup>exibility and choice in how it is used. In the present context, the ELIM tool is by design highly restrictive relative to PS, and so provides less choice on how it is to be used. By de<sup>fi</sup>nition a more restrictive decision tool provides a more tightly structured decision process; it permits the use of fewer options in terms of decision strategy and consequently effort. Thus with use more constrained by the ELIM tool, the opportunity to leverage additional effort or knowledge is similarly constrained with ELIM. We therefore do not expect substantial effects for knowledge and effort with the ELIM tool, and make no hypotheses in this regard. Moreover, given that our interest is in the effects of restrictiveness, and that restrictiveness is in essence a relative measure, empirically we employ the ELIM tool as a benchmark for comparing performance with the less restrictive PS tool.

## 2.4.1. Effort effects — less restrictive tool

H1. For a given level of knowledge, users who exert greater effort will achieve greater accuracy with the PS tool.

This is consistent with prior effort-accuracy research, while controlling for any effort-knowledge substitution effect.

## 2.4.2. Effort effects — less restrictive vs. more restrictive tool

H2. For a given level of knowledge, effort will have a greater effect on accuracy for users of the PS tool than for users of the ELIM tool.

The greater <sup>fl</sup>exibility of the less restrictive tool provides greater opportunity for performance improvement through greater effort.

## 2.4.3. Knowledge effects — less restrictive tool

H3. For a given level of effort, users of the PS tool who have greater knowledge will achieve greater accuracy.

For a given level of effort, the user is able to reach a higher equiperformance isobar through greater knowledge (per Fig. 1).

## 2.4.4. Knowledge effects — less restrictive vs. more restrictive tool

H4. For a given level of effort, greater knowledge will have a greater positive effect on accuracy for users of the PS tool than for users of the ELIM tool.

The greater <sup>fl</sup>exibility of the less restrictive tool provides a greater opportunity to leverage knowledge for performance gain.

## 2.4.5. Interaction of effort and knowledge — less restrictive tool

H5. For users of the PS tool, the interaction of knowledge and effort will positively affect accuracy.

That knowledge and effort together offer synergistic gains in accuracy is indicated by the convexity of the equi-performance isobars in Fig. 1.

2.4.6. Interaction of effort and knowledge — less restrictive vs. more restrictive tool

H6. The effect of the interaction of knowledge and effort on accuracy will be greater for users of the PS tool than for users of the ELIM tool.

Consistent with the arguments for H2 and H4, the less restrictive tool offers greater opportunity to leverage both knowledge and additional effort synergistically for greater performance gain.

## 3. Research design

## 3.1. Operationalization of constructs

## 3.1.1. Accuracy

Measuring accuracy in a preferential choice task can be somewhat problematic. Prior research has often used the results of a Weighted Additive decision strategy as a benchmark for performance. However, a Weighted Additive benchmark is confounded as it is well established that preferences (which determine the weights in the Weighted Additive model) are constructive. In other words, they are not held resident in memory, but are rather generated dynamically in response to stimuli. Thus preferences are often not stable and are affected by the timing and method of elicitation [9,46,47]. As a consequence the Weighted Additive benchmark itself would be unstable and it becomes impossible to separate out genuine effects from effects due to instability in the benchmark. To overcome this problem we employ a more objective approach, using Data Envelopment Analysis (DEA) [4,12,28]. Importantly, our approach considers only revealed preferences (i.e., actual choices) in assessing accuracy, rather than separately elicited weights or attribute preferences.

DEA is an optimization method, based on linear programming, that can be used to identify dominated (suboptimal) or dominant (optimal) items in a set. Traditionally, DEA has been used to simultaneously analyze multiple inputs and outputs of similar production facilities, such as factories, bank branches, or fast-food franchises, to compute their relative production ef<sup>fi</sup>ciency. (For example applications of DEA see: [15,25,31,45,67]). The concept and technique apply more broadly, however. Dominance (also called ef<sup>fi</sup>ciency) is a way of capturing optimality in any multi-dimensional decision context. In essence, DEA enables the construction of an ef<sup>fi</sup>cient frontier in multi-dimensional space — representing the optimal output across the full range of the different input dimensions.

In the present consumer purchase context, the DEA ef<sup>fi</sup>cient frontier comprises the set of dominant products. This is more subtle than simply including one product that is dominant on each attribute (e.g., the cheapest price, biggest size, etc.). The DEA technique empirically derives the trade-offs among attributes and thus also includes dominant combinations of attributes. The DEA frontier is preference-independent. It is derived from the range of products itself, not from the preferences of any given individual. Given a suf<sup>fi</sup>ciently comprehensive and evenly distributed product space, there will exist a product on the frontier that is dominant for any given set of rational preferences. In such a situation, an individual will always prefer a product on the frontier than one not on the frontier.

Fig. 4, shows an evenly distributed and comprehensive product space containing nine products with two attributes. Irrespective of an individual's preference weightings for each attribute, the dominant choice is on the DEA frontier which comprises Products A–C. For example, if an individual's preferences strongly favor Attribute 1, Product C dominates. Alternatively, if the individual is indifferent between the attributes, Product B dominates. Thus the frontier provides an objective accuracy benchmark that can be used to generate an appropriate dominant product for any given set of preferences (given the evenly distributed and comprehensive product space). The exact benchmark product is determined by the product on the frontier that is nearest product to the individual's <sup>fi</sup>nal choice (or their <sup>fi</sup>nal choice if that is itself on the frontier). In this way, while the frontier is objective and preference independent, the actual benchmark product is determined by the individual's revealed preferences (i.e., their <sup>fi</sup>nal choice). Assuming that an individual does not behave perversely (i.e., against their own preferences) the structure of our product space ensures that a product on the frontier will always dominate an off-frontier choice. Furthermore, given any choice not on the frontier, a move to the nearest product on the frontier will result in an improvement in the attribute values of at least one dimension, without any sacri<sup>fi</sup>ce in the other dimensions (i.e. without trade-off). We describe how we constructed such a comprehensive and evenly distributed product space in Section 3.2 below.

![](/api/attachments/CZWXA6KS/fulltext/images/b2218db09edbb1fc97d1707d20c0ef9b7622898756f8578af135f6716e6fb015.jpg)  
Fig. 4. The DEA frontier in an evenly distributed and comprehensive product space

Using the DEA frontier as a benchmark, we operationalize accuracy as the degree of dominance of the chosen product, ranging from 0 (dominant, i.e., on the frontier) to 9 (completely dominated, i.e., the farthest distance possible from the frontier). Degree of dominance is de<sup>fi</sup>ned as the distance from an alterative to the DEA ef<sup>fi</sup>cient or dominant frontier, in a multi-dimensional space [31]. To simplify the data analysis, we subsequently reversed the scores to yield a measure for accuracy, such that a larger value indicated a more accurate selection. Rarely has DEA been used to measure the degree of dominance and never to our knowledge has it been previously applied as a benchmark in experimental decision support systems research. The DEA frontier avoids the problem of preference instability of the Weighted Additive benchmark. Yet, it provides a benchmark sensitive to the revealed preferences of the individual decision maker; with an evenly distributed and comprehensive product space, the frontier will provide a dominant choice for any possible set of rational preferences. The accuracy measure is determined by reference to the objective DEA frontier and the revealed preferences (i.e., the <sup>fi</sup>nal product choice) of the user.

## 3.1.2. Effort

A range of approaches exist for measuring cognitive effort and like constructs. For example at the most sophisticated end, Smith [56] looked at electrocardiograph information of his subjects in a <sup>fi</sup>nancial trading decision making experiment. Concurrent verbal protocols can also be used to assess effort, assuming the think-aloud commentary is veridical [16,62,64]. Other research has employed counts of the elementary information processing units discussed earlier [8,13,38,49,63]. However, this counting approach is not readily applicable in all task situations. In particular it does not apply well to the ELIM and PS tools we use in this study. The decision support tools in this study are holistic, non-decomposable tools, rather than a set of independent operators. Our approach contrasts with Todd and Benbasat [63] who provide a suite of operators that implement elementary information processing functions. Given that we wanted to manipulate restrictiveness with respect to the decision strategies supporting a suite of elementary information processing operators would have provided far too great a <sup>fl</sup>exibility to effectively manipulate restrictiveness. Hence we employed holistic decision tools as opposed to a suite of operators and consequently sought alternative measures to counts of elementary information processes. Following prior research [26,29], we measure effort as time engaged in the preferential choice task, i.e., excluding time spent reading experimental instructions or training.

## 3.1.3. Knowledge

Since our preferential choice task is a consumer purchase decision, we employ an established subjective measure of knowledge from the marketing literature. Speci<sup>fi</sup>cally, we use the construct of product category knowledge [6,50]. We use a three item scale based on the instrument employed by Brucks [11]. We control for other forms of knowledge by using very easy to use decision support tools and by training subjects in the use of the tools.

We explicitly chose to use a subjective measure of domain knowledge, for both theoretical and pragmatic reasons. Theoretically, this avoided problems of bias in objective tests of knowledge (e.g., a pre-test may bias behaviors by highlighting factors of importance in the task, a post-test would suffer from a circularity: those with high knowledge are by de<sup>fi</sup>nition those who perform the task competently). More pragmatically, in the consumer purchase context a subjective measure of knowledge already exists in the literature [11]. While some contexts provide certi<sup>fi</sup>cations that can be employed to distinguish between high and low knowledge subjects (e.g., see [40]), there is no applicable measure in our context. In any event professionally experienced subjects have on occasion been found to perform worse than novices on objective tests of knowledge [5]. Of more relevance to the present context, there is evidence in the marketing literature that subjective measures of knowledge are highly correlated with objective measures [17], but that the correlation can breakdown when an individual does not have good insight into “how much or how little she knows”[10]. This literature supports our use of a subjective measure. We had strong reasons to believe our subjects (undergraduate information systems students) would be well calibrated in their perceptions of knowledge in the domain of our task: computer products.

## 3.2. Experimental study

## 3.2.1. Task environment

For our preferential choice task we examined a simulated consumer purchase for two items: a printer and a computer. The printer shopping task was used as a practice or training task prior to the real task of shopping for a computer. We constructed a comprehensive and evenly distributed product database of 243 unbranded instances of each product, by varying each product attribute across three different levels (low, medium, high) using attribute values derived from market offerings current at the time of the experiment. Each product was described in terms of <sup>fi</sup>ve attributes (printer: resolution, paper tray capacity, speed, footprint, and price; computer: processor speed, RAM, hard disk size, monitor size, and price). Consequently, this initial product space was comprehensive: 5 attributes, 3 values each = 243 possible combinations.

For each product we applied DEA to the measures of the <sup>fi</sup>ve attributes. An ef<sup>fi</sup>cient frontier for each product category was readily determined as optimality can be determined directly from the attributes. For example, ceteris paribus, a computer with more RAM is preferable to one with less RAM; a computer with lower price dominates one with a higher price, assuming rational preferences. This relies on an objective ordering of attribute values. Consequently, we excluded any attributes where an objective ordering was not possible (e.g., color, brand, etc.).

Table 1 Descriptive statistics.

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td><td>Actual range</td><td>Theoretical range</td></tr><tr><td>Knowledge</td><td>3.363</td><td>1.387</td><td>1.00–6.0</td><td>1.0–7.0</td></tr><tr><td>Effort $^a$ </td><td>148.0</td><td>79.2</td><td>47.0–405.0</td><td>0–infinite</td></tr><tr><td>Accuracy</td><td>8.339</td><td>1.116</td><td>5.0–9.0</td><td>1.0–9.0</td></tr></table>

<sup>a</sup> Effort is measured as the number of seconds actually engaged in the decision making task (i.e., excluding reading instructions, training etc.).

Using DEA we identi<sup>fi</sup>ed dominant products in each category (printer or computer) and removed the six most dominant products to yield a product space of 237 items with 11 (4.6%) dominant products per category. With products described by <sup>fi</sup>ve attributes, the <sup>fi</sup>rst <sup>fi</sup>ve most dominant products would be trivially identi<sup>fi</sup>ed by in turn, choosing to optimize individual on each of the <sup>fi</sup>ve attributes. To avoid this possibility we removed these “obvious” dominant alternatives. The resulting product database had slightly more than twice the number of dominant products as there were attributes. This was consistent with prior research in an e-commerce context, providing a substantial product space, and a small but non-trivial number of dominant products [29]. Importantly, the product space was sizable enough to require effective use of the tools, while not being unrealistically large. The product space and frontier was preference indifferent (i.e., not skewed in favor of any particular attribute) and suf<sup>fi</sup>ciently comprehensive and evenly distributed to ensure that for any given rational preferences a dominant product existed on the frontier. Finally, it was consistent with current market offerings at the time of the experiment. The DEA frontier of 11 products was the basis for assessing accuracy, measured as the distance from the selected product to the DEA frontier.

Subjects were provided access to the product database via a web interface that implemented either the ELIM or PS tool described above. The ELIM and PS tools were speci<sup>fi</sup>cally developed for this experiment as part of a web shopping simulation. This web-based environment controlled the interface, preventing users from accessing sites outside the controlled experimental environment. The implementation of the two decision tools contained no extraneous links or images, reducing clutter and emphasizing the functionality of the tool.

## 3.2.2. Experimental design and method

We employed a between-subjects design manipulating the decision tool provided to the subjects, with half receiving ELIM and half receiving PS. Effort is clearly a discretionary decision of the subject. Consequently, we measured effort but did not attempt to directly manipulate it. Similarly, knowledge was measured but not manipulated. We did not attempt to allocate subjects to experimental condition on the basis of knowledge as we were interested in the effects of the full spectrum of knowledge levels with the two different tools: ELIM and PS.

Relevant questionnaire instruments were automatically administered at appropriate stages in the user interaction. Prior pilot tests were conducted to ensure that the web simulation was error-free, that the instructions were clear, and that shopping with the tools was neither trivially easy nor frustratingly dif<sup>fi</sup>cult.

Subjects were 56 college students drawn from a volunteer pool from an introductory undergraduate information systems subject. Subjects were motivated by a performance-linked incentive: \$200 for <sup>fi</sup>rst place, \$100 for second place and \$50 for third place performers. Subjects were instructed that their goal was to obtain the most suitable product for provision by the university to incoming freshman, and that in the event of a ties, the quickest decision maker would win. Operationally, performance was calculated using the DEA-calculated accuracy measure, with effort (lowest time taken) used to break any ties. The incentive ensured engagement in the task and was consistent with the effort-accuracy trade-off. Note however, we did not use the term “accuracy” anywhere in the instructions, lest the subject erroneously interpret this to mean there was a single optimal choice irrespective of preferences.

On arrival, subjects received brief instructions on the tasks and then began the printer shopping task to familiarize themselves with the decision tool. No incentives were applied in this training task to allow subjects the full opportunity to explore the capabilities and use of the tool provided.

## 4. Results

Demographic data revealed the subjects to be relatively homogenous; consequently, it is not reported here in the interests of brevity (the subjects were nearly exclusively freshman, and all were studying an undergraduate information systems subject). Descriptive statistics for three quantitative variables are shown in Table 1.

The results of the tests of the hypotheses were obtained by regressing accuracy on the independent variables based on the following general model:

$$
\begin{array}{r l} \text { Accuracy } & = \beta_ {0} + \beta_ {1} P S + \beta_ {2} \text { Effort } + \beta_ {3} \text { Effort } \times P S + \beta_ {4} K + \beta_ {5} K \times P S \\ & + \beta_ {6} \text { Effort } \times K + \beta_ {7} \text { Effort } \times K \times P S \end{array} \tag {1}
$$

where

PS is a dummy variable for the decision tool

(PS=1 for the less restrictive parametric search and

K is the measure of product category knowledge

Effort is the time spent interacting with the tool.

The use of a dummy variable in this way permits us to simultaneously estimate two equations, one for ELIM (i.e., PS=0) and one for PS (PS=1). Substituting in the respective values we can see the above equation decomposed into two equations as follows:

PS=0 (ELIM tool)

$$
A c c u r a c y = \beta_ {0} + \beta_ {2} E f f o r t + \beta_ {4} K + \beta_ {6} E f f o r t \times K\tag{2}
$$

PS= 1 (PS tool)

$$
\begin{array}{c} A c c u r a c y = (\beta_ {0} + \beta_ {1}) + (\beta_ {2} + \beta_ {3}) E f f o r t + (\beta_ {4} + \beta_ {5}) K \\ + (\beta_ {6} + \beta_ {7}) E f f o r t \times K \end{array}\tag{3}
$$

The results of the analysis are summarized in Table 2. Hypotheses H1 and H2 are fully supported, effort positively in<sup>fl</sup>uences accuracy $( p = 0 . 0 0 8 )$ , and this in<sup>fl</sup>uence is stronger for PS $( p = 0 . 0 0 9 )$ . The test of Hypothesis H3 interestingly shows knowledge to have a signi<sup>fi</sup>cant negative effect on accuracy with PS (pb0.0001). While the effect of knowledge was signi<sup>fi</sup>cantly greater for PS $( p = 0 . 0 3 1 )$ , the effect was negative, counter to H4. Hypothesis H5 is marginally supported; the interaction of knowledge and effort appears to positively in<sup>fl</sup>uence accuracy with PS $( p = 0 . 0 7 1 )$ . This effect is not signi<sup>fi</sup>cantly different between PS and the ELIM control group, with Hypothesis H6 not quite obtaining marginal support (p=0.114).

Table 3  
Table 2  
Regression results.

<table><tr><td>Predictor</td><td>Coeff.</td><td>Standard error</td><td>T</td><td>P</td><td>Relevant hypothesis</td></tr><tr><td>Intercept (ELIM)  $\beta_0$ </td><td>9.34</td><td>0.5565</td><td>16.79</td><td>0.000</td><td></td></tr><tr><td> $\Delta$ Intercept (PS vs ELIM)  $\beta_1$ </td><td>-1.1658</td><td>0.8961</td><td>-1.30</td><td>0.199</td><td></td></tr><tr><td>Effort (ELIM)  $\beta_2$ </td><td>-0.0007</td><td>0.0018</td><td>-0.39</td><td>0.700</td><td></td></tr><tr><td>Effort (PS)  $\beta_2 + \beta_3$ </td><td>0.0127</td><td>0.0046</td><td>2.78</td><td>0.008</td><td>H1 supported</td></tr><tr><td> $\Delta$ Effort (PS vs. ELIM)  $\beta_3$ </td><td>0.0134</td><td>0.0049</td><td>2.73</td><td>0.009</td><td>H2 supported</td></tr><tr><td>K (ELIM)  $\beta_4$ </td><td>-0.1497</td><td>0.1274</td><td>-1.18</td><td>0.246</td><td></td></tr><tr><td>K (PS)  $\beta_4 + \beta_5$ </td><td>-0.5466</td><td>0.1249</td><td>-4.38</td><td>0.000</td><td>H3 unsupported Significant effect opposite to H3</td></tr><tr><td> $\Delta K$  (PS vs. ELIM)  $\beta_5$ </td><td>-0.3969</td><td>0.1784</td><td>-2.22</td><td>0.031</td><td>H4 unsupported Significant effect opposite to H4</td></tr><tr><td>Effort×K (ELIM)  $\beta_6$ </td><td>0.0004</td><td>0.0016</td><td>0.22</td><td>0.824</td><td></td></tr><tr><td>Effort×K (PS)  $\beta_6 + \beta_7$ </td><td>0.0068</td><td>0.0037</td><td>1.85</td><td>0.071</td><td>H5 marginally supported</td></tr><tr><td> $\Delta$  Effort×K (PS vs ELIM)  $\beta_7$ </td><td>0.0064</td><td>0.0040</td><td>1.61</td><td>0.114</td><td>H6 unsupported</td></tr></table>

Adjusted R-squared=42%. Note: The above results are drawn from running regressions both with and without interactions. The values shown for the main effects of knowledge and effort were derived from regressions without the knowledge-effort interaction terms to avoid multi-collinearity problems in the interpretation of main effects in the presence of interactions [2,58]. The adjusted R-squared was taken from the full equation (including interaction terms).

## 5. Discussion and limitations

## 5.1. Discussion

## 5.1.1. Effort and restrictiveness effects

Overall, the results support the hypotheses relating to effort. Greater effort results in greater accuracy with the less restrictive (PS) tool, effectively con<sup>fi</sup>rming prior effort/accuracy research. More importantly, effort has signi<sup>fi</sup>cantly greater effect on accuracy with the less restrictive tool (PS versus ELIM). This is consistent with the notion that the less restrictive tool provides greater <sup>fl</sup>exibility and thus opportunity to bene<sup>fi</sup>t from increased effort.

The results also clearly demonstrate that system restrictiveness (as operationalized here) matters. Consistent with theory and intuition, effort provides greater performance returns with a less restrictive system. In addition, as expected, we found no evidence of a knowledge effect with the more restrictive tool. However a less restrictive tool actually seems to be dangerous in the hands of more knowledgeable users; greater knowledge resulted in signi<sup>fi</sup>cantly worse performance for users of the less restrictive tool. This counter-intuitive and contrary to hypothesis result is arguably even more surprising given the way system restrictiveness was operationalized here. Speci<sup>fi</sup>cally, the less restrictive tool provided support for a superior decision strategy (i.e., simultaneous consideration of alternatives versus sequential consideration of alternatives), so a priori it should have been even more likely to yield greater performance outcomes — yet the results reveal the opposite for the more knowledgeable subjects.

## 5.1.2. Knowledge effects

The results for the hypotheses relating to knowledge thus require further investigation. We considered several possible explanations for the anomalous effects of knowledge in users of the less restrictive tool:

1. Subjects with greater knowledge may have been less mindful [36] or more complacent, and thus did not exercise as much care or effort.

• This explanation is ruled out. We observe the negative effect for knowledge in a model which includes a variable for effort.

2. More knowledgeable subjects may have been unable to <sup>fi</sup>t the functionality of the tool into their established patterns of decision making [18,19,40,41].

• This explanation is also ruled out. We observe the negative effect for knowledge to be signi<sup>fi</sup>cantly greater with the more <sup>fl</sup>exible (less restrictive) tool (PS).

3. High knowledge subjects may have conducted less comprehensive or thorough searches. Prior research in marketing suggests that greater knowledge of speci<sup>fi</sup>c products leads to the perception of fewer bene<sup>fi</sup>ts to search [1], which leads to less search [50]. Thus, if the high knowledge users had knowledge of speci<sup>fi</sup>c products, perhaps they conducted fewer searches.

• This explanation is also ruled out. A less comprehensive search equates to less effort, yet the negative effect of knowledge was observed even after controlling for effort effects.

4. High knowledge subjects may have employed a markedly different search process, for example narrowing too quickly to a few alternatives but then exerting concentrated effort. Such a process could lead to worse choices, without signi<sup>fi</sup>cant differences in effort — the effort is simply applied at a different stage in the process. Thus, an effect could be observed even after controlling for effort.

• Exploring this possibility requires a consideration of process data. In what follows we present such a discussion and analysis.

To examine the process, we considered the number of iterative applications of the tool employed by each subject. As shown in Table 3 this analysis provides support for differences in the search process.

Several notable <sup>fi</sup>ndings are evident in Table 3. Subjects using ELIM went through considerably more iterations with the tool. This result is not surprising given that ELIM only permits sequential rather than simultaneous evaluation of attributes. Therefore, it is also not surprising to <sup>fi</sup>nd Effort positively correlated with the use of the ELIM tool. Of note, however, is the relatively lower number of iterations for users of PS, and the marginally signi<sup>fi</sup>cant negative correlation between knowledge and number of iterations with PS. The more knowledgeable subjects ran fewer iterations of the PS tool. Such an outcome would be consistent with a knowledge-effort substitution, which would be evidenced by a negative correlation between knowledge and effort for the PS tool. In fact, Effort and Knowledge show no signi<sup>fi</sup>cant correlation for either tool (corr = 0.177, p=0.377 for PS, corr=0.157, p=0.416 for ELIM).

What could lead higher knowledge users of the less restrictive (PS) tool to conduct fewer iterations, exert comparable effort levels, and yet perform worse than low knowledge users? Perhaps high knowledge subjects executed their search differently. If knowledgeable users held their knowledge in the form of a stereotypical ideal [27,60] then their search would have been for a near match to their stereotypical ideal. Such a search would be quite different from a search based on knowledge such as attribute trade-offs or diagnosticity.

Iteration analysis by treatment.

<table><tr><td rowspan="2">Treatment</td><td colspan="2">Number of Iterations</td><td colspan="2">Iterations correlated with</td></tr><tr><td>Mean</td><td>St. Dev.</td><td>Knowledge</td><td>Effort</td></tr><tr><td>PS</td><td>1.407</td><td>1.118</td><td>-0.358 (p=0.067)</td><td>0.141 (p=0.485)</td></tr><tr><td>ELIM</td><td>4.862</td><td>0.915</td><td>-0.169 (p=0.379)</td><td>0.321 (p=0.090)</td></tr></table>

Search based on knowledge of a stereotypical ideal explains why a negative knowledge effect may be observed even after controlling for effort. Given our comprehensive and evenly distributed product space, there are arguably more dominant products than there would be near matches to the stereotypical idea. Consequently, a search for a stereotypical ideal could potentially take longer than a search for any dominant product, thereby negating any effort reduction due to the knowledge-effort substitution effect proposed by Newell [42]. Lower performance may result in the end, as the stereotypical ideal may itself be dominated in our product space. This is especially likely with the computers product category, given the fast pace of change in technology and the rapid dating of knowledge of what constitutes state-of-the-art.

Clearly, the question of knowledge effects is not simply a matter of how much, but also of what form. A highly knowledgeable subject may, for example, have a well developed stereotypical ideal, or alternatively a comprehensive understanding of attribute trade-offs in the product space. The implications for performance with decision support tools appear quite different depending on the speci<sup>fi</sup>c form or content of knowledge rather than simply a matter of degree.

More broadly, the stereotypical ideal explanation is akin to a decision maker searching for an a priori preferred solution and thereby failing to identify better alternatives available in the given situation. Such behavior has already been evidenced in the literature with Kachelmeier and Messier [33] evidencing users of a decision aid working backwards to get the aid to generate the result they wanted. In terms of the question of knowledge, it is a matter of knowledge of solutions versus knowledge about how to process information to obtain a solution.

## 5.1.3. Summary

Examining knowledge, effort and restrictiveness together reveals performance with decision support to be complex, even more so than we had originally theorized. While a knowledge-effort substitution effect is not clearly apparent in our results, we do <sup>fi</sup>nd evidence, consistent with the theory, that knowledge and effort synergistically improve accuracy. Subjects with greater knowledge who exert greater effort appear to be able to move to a higher equi-performance isobar. That this result is only marginally signi<sup>fi</sup>cant may be a re<sup>fl</sup>ection of the noise due to the form and content of the knowledge issue alluded to above.

## 5.2. Limitations

As with any experimental study, high internal validity is achieved with some loss of external validity. Whether our results will generalize to other preferential choice tasks, decision tools and decision making contexts is a matter to be assessed by replications and future research. We are comforted in this regard by the realism of our task. Speci<sup>fi</sup>cally, the use of a salient monetary reward, a product database of substantial size derived from market offerings, and decision tools (PS and ELIM) that are commonplace.

While our measure of effort is consistent with prior research we recognize that effort may be multi-faceted. For example, there is the effort entailed in translating one's preferred decision process to “<sup>fi</sup>t” a process permitted by the tool [18,19]. Decomposing effort in this regard is beyond the scope of the present study. In any event, such issues are likely to be more signi<sup>fi</sup>cant in more restrictive tools which by de<sup>fi</sup>nition support only a subset of processes. Empirically we minimize this problem by our focus on the less restrictive PS and the use of the restrictive ELIM only as a benchmark or experimental control.

Our measure of knowledge is a perceptual measure. Our use of a subjective measure was motivated by concerns about the ability of an objective measure to correctly capture the underlying construct of interest as described earlier (see also [5]). Nonetheless the potential for bias in subjective measures raises the question as to whether similar results would have been found had an appropriate objective measure of knowledge been available. We have no reason to expect miscalibration in the knowledge perceptions of our subjects. Indeed, given their demographics and recent exposure to an introductory information systems subject, which included curriculum on computer hardware, we expect they have had ample opportunity in the real world to receive feedback to calibrate their knowledge perceptions in the computer product category. In any event the main effect for knowledge would not be explained by miscalibration, but only by perverse calibration (i.e., perceptions of knowledge strongly negatively correlated to objective knowledge).

## 6. Implications and conclusions

Our results demonstrate quite powerfully that domain knowledge matters in understanding the impact of effort, and decision tool design (speci<sup>fi</sup>cally restrictiveness) on performance. Surprisingly, a more <sup>fl</sup>exible tool can actually yield worse outcomes for more knowledgeable subjects, even in the presence of incentives.

From a research perspective, this study raises substantial issues in our understanding of the role of user domain knowledge in performance with decision support tools. Clearly future research can no longer restrict itself to effort-accuracy considerations without also capturing knowledge effects. More speci<sup>fi</sup>cally, it appears that form or content of knowledge must be assessed, as opposed to applying a unidimensional assessment of “more versus less” knowledge. For example, in the context of a preferential choice task does the knowledge capture attribute values, ranges and trade-offs, or is it a stereotypical ideal product. We suspect that decision tools that provide a better “<sup>fi</sup>t” with the form or content of user domain knowledge will enhance task performance [18,19]. In a similar vein, a greater exploration of the form of effort is likely to be informative.

Theory suggested that knowledge and effort are potential substitutes, and that combined together, they may have synergistic bene<sup>fi</sup>ts. Our results reveal that any knowledge-effort substitution may be, in practice, more complex — requiring consideration of form or content of the knowledge (e.g., stereotypical ideal product, or attribute trade-offs). Nonetheless synergistic bene<sup>fi</sup>ts are available, when the decision tool provides the potential for such bene<sup>fi</sup>ts to be applied.

Future research also needs to consider further the interplay between knowledge, effort and system restrictiveness. Restrictiveness appears to play an important role in enabling or limiting, as the case may be, the opportunity to exploit knowledge and effort to improve performance. While additional effort with a less restrictive tool yields improved performance, greater levels of knowledge actually hurt performance with a less restrictive tool. Pragmatically this suggests that where there is opportunity to exert effort, greater <sup>fl</sup>exibility (less restrictiveness) can be bene<sup>fi</sup>cial, but that surprisingly more knowledgeable individuals may not be better off with greater <sup>fl</sup>exibility. From a research perspective it is clear that the impact of restrictiveness cannot be studied without consideration of effort and knowledge.

Methodologically, this study makes an additional contribution by demonstrating the application of DEA to the assessment of accuracy in a preferential choice task. This overcomes a limitation of prior studies that have relied on a Weighted Additive model as the benchmark for accuracy, which is vulnerable to the constructive nature of preferences. Our DEA accuracy measure depends on the characteristics of the product space and subjects' revealed preferences (i.e., choice) rather than on unstable solicited weightings for attributes.

From a practical perspective, our research casts concern over the widespread use of parametric search tools. It also brings into question the role of such powerful tools in the performance of more knowledgeable decision makers. Pragmatically, it highlights the importance of considering, in detail, the domain knowledge of the target users of a decision support tool. The design of a decision support tool can signi<sup>fi</sup>cantly constrain or enable effective performance, and any effect on performance is contingent on both the effort and the form or content of the domain knowledge of the user. Design choices about how restrictive to make decision tools thus need to be informed by a detailed assessment of the domain knowledge of target users. Only then can we hope to build decision tools that provide an appropriate balance between the knowledge of the user and the power and intelligence embedded in the decision tool. In short, our results suggest that better tools do not necessarily lead to better outcomes in the hands of domain knowledgeable users. Designers need to consider what users know about the domain and how this will affect their behavior with the tools they are provided in the speci<sup>fi</sup>c task context. Moreover, more restrictive, less powerful, tools may yield superior performance as they provide less scope for inappropriate action by users.

## References

[1] J.W. Alba, J.W. Hutchinson, J. Lynch, Memory and decision making, in: T. Robertson, H. Kassarjian (Eds.), Handbook of Consumer Behavior, Prentice-Hall, Englewood Cliffs, NJ, 1991, pp. 1–49

[2] P.D. Allison, Testing for interaction in multiple regression, American Journal of Sociology 83 (1) (1977) 144–153.

[3] V. Arnold, P.A. Collier, S.A. Leech, S.G. Sutton, Impact of intelligent decision aids on expert and novice decision-makers' judgments, Accounting & Finance 44 (1) (2004) 1–26.

[4] R.D. Banker, A. Charnes, W.W. Cooper, Some models for estimating technical and scale inef<sup>fi</sup>ciencies in data envelopment analysis, Management Science 30 (9) (1984).1078-1092

[5] J.A. Barrick, B.C. Spilker, The relations between knowledge, search strategy, and performance in unaided and aided information search, Organizational Behavior and Human Decision Processes 90 (1) (2003) 1–19.

[6] S.E. Beatty, S.M. Smith, External search effort: an investigation across several product categories, Journal of Consumer Research 14 (Jun 1 1987) 83–95.

[7] I. Benbasat, P. Todd, The effects of decision support and task contingencies on model formulation: a cognitive perspective, Decision Support Systems 17 (4) (1996) 241–252.

[8] J.R. Bettman, E.J. Johnson, J.W. Payne, A componential analysis of cognitive effort in choice Organizational Behavior and Human Decision Processes 45 (Feb 1.1990) 111-139.

[9] J.R. Bettman, M.F. Luce, J.W. Payne, Constructive consumer choice processes, Journal of Consumer Research 25 (3) (1998) 187–217.

[10] K. Braunsberger, R.B. Buckler, M. Luckett, Dimensions of total product knowledge in a service environment, The Journal of Service Marketing 22 (7) (2008) 505.

[11] M. Brucks, The effects of product class knowledge on information search behavior, Journal of Consumer Research 12 (1) (1985) 1–16.

[12] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 2 (6) (1978) 429–444.

[13] P.C. Chu, E.E. Spires, The joint effects of effort and quality on decision strategy choice with computerized decision aids, Decision Sciences 31 (2) (2000) 259–292.

[14] P.C. Chu, J.J. Elam, Induced system restrictiveness: an experimental demonstration, IEEE Transactions on Systems Man and Cybernetics 20 (1) (1990) 195–201.

[15] A. Cielen, L. Peeters, K. Vanhoof, Bankruptcy prediction using a data envelopment analysis, European Journal of Operational Research 154 (2) (2004).

[16] E. Coupey, Restructuring: constructive processing of information displays in consumer choice, Journal of Consumer Research 21 (June 1 1994) 83–99.

[17] E. Cowley, A.A. Mitchell, The moderating effect of product knowledge on the learning and organization of product information, Journal of Consumer Research 30 (3) (2003) 443.

[18] M.J. Davern, When good <sup>fi</sup>t is bad: the dynamics of perceived <sup>fi</sup>t, Proceedings of the Seventeenth International Conference on Information Systems, Cleveland, OH, Association for Computing Machinery (1996) 112–121.

[19] M.J. Davern, Towards a uni<sup>fi</sup>ed theory of <sup>fi</sup>t: task, technology and individual, in: D. Hart, S. Gregor (Eds.), Information Systems Foundations: Theory Representation and Reality, Canberra ACT, ANU E-Press, 2007, pp. 49–69.

[20] M.J. Davern, R.J. Kauffman, Discovering potential and realizing value from information technology investments, Journal of Management Information Systems 16 (4) (2000) 121–143.

[21] M.J. Davern, R. Mantena, E. Stohr, Diagnosing decision quality, Decision Support Systems 45 (2008) 123–139.

[22] F.D. Davis, J.E. Kottemann, User perceptions of decision support effectiveness: two production planning experiments, Decision Sciences 25 (1) (1994) 57–78.

[23] F.D. Davis, J.E. Kottemann, Determinants of decision rule use in a production planning task, Organizational Behavior and Human Decision Processes 63 (2) (1995) 145–157.

[24] G.W. Dickson, J.A. Senn, N.L. Chervany, Research in management information systems: the minnesota experiments, Management Science 23 (9) (1977) 913–923.

[25] M.K. Epstein, J.C. Henderson, Data envelopment analysis for managerial control and diagnosis, Decision Sciences 20 (1) (1989) 90–119.

[26] G.W. Fischer, Z. Carmon, D. Ariely, G. Zauberman, Goal-based construction of preferences: task goals and the prominence effect, Management Science 45 (Aug 8 1999) 1057–1075.

[27] S.T. Fiske, M.A. Pavelchak, Category-based versus piecemeal-based affective responses: developments in schema-triggered affect, in: R.M. Sorrentino, E.T. Higgins (Eds.), The Handbook of Motivation and Cognition: Foundations of Social Behavior, Guilford, New York, 1986, pp. 167–203.

[28] M. Halme, T. Joro, P. Korhonen, S. Salo, J. Wallenius, A value ef<sup>fi</sup>ciency approach to incorporating preference information in data envelopment analysis, Management Science 45 (1) (1999) 103–115

[29] G. Haubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Marketing Science 19 (1) (2000) 4–21.

[30] E.J. Johnson, J.W. Payne, Effort and accuracy in choice, Management Science 31 (4) (1985) 395-414.

[31] S.A. Johnson, J. Zhu, Identifying “best” applicants in recruiting using data envelopment analysis, Socio-Economic Planning Sciences 37 (2) (2003) 125–139.

[32] A. Kamis, M. Koufaris, T. Stern, Using an attribute-based decision support system for user-customized products online: an experimental investigation, MIS Quarterly 32 (1) (2008) 159–177.

[33] S.J. Kachelmeier, W.F. Messier, An investigation of the in<sup>fl</sup>uence of a nonstatistical decision aid on auditor sample size decisions, The Accounting Review 65 (1) (1990) 209–226.

[34] N.M. Klein, M.S. Yadav, Context effects on effort and accuracy in choice — an inquiry into adaptive decision-making, Journal of Consumer Research 15 (Mar 4 1989) 411–421.

[35] J.E. Kottemann, W.E. Remus, A study of the relationship between decision model naturalness and performance, MIS Quarterly 13 (2) (1989) 170–181.

[36] E.J. Langer, Mindfulness, Addison Wesley Publishing Company, 1989.

[37] F.J. Lerch, D.E. Harter, Cognitive support for real-time dynamic decision making, Information Systems Research 12 (1) (2001) 63–82.

[38] G.L. Lohse, E.J. Johnson, A comparison of two process tracing methods for choice tasks, Organizational Behavior and Human Decision Processes 68 (Oct 1 1996) 28–43.

[39] J. Mckay, J. Elam, A comparative study of how experts and novices use a decision aid to solve problems in a complex knowledge domain, Information Systems Research 3 (2) (1992) 150–172

[40] J. Mao, I. Benbasat, The use of explanations in knowledge-based systems: cognitive perspectives and a process-tracing analysis, Journal of Management Information Systems 17 (1) (2000) 155–181.

[41] F. Nah, I. Benbasat, Knowledge-based support in a group decision making context: an expert-novice comparison, Journal of the Association for Information Systems 5 (3) (2004) 125–150.

[42] A. Newell, Uni<sup>fi</sup>ed Theories of Cognition, Cambridge, MA, Harvard University Press (1990) 42–110.

[43] A. Newell, H.A. Simon, Human Problem Solving, Englewood Cliffs, N.J., Prentice-Hall, 1972.

[44] E.L. Newport, Maturational constraints on language learning, Cognitive Science 14 (1) (1990) 11–28.

[45] J.H. Park, S.C. Park, Agent-based merchandise management in business-tobusiness electronic commerce, Decision Support Systems 35 (3) (2003) 311–333.

[46] J.W. Payne, J.R. Bettman, E. Coupey, E.J. Johnson, A constructive process view of decision-making — multiple strategies in judgment and choice, Acta Psychologica 80 (Aug 1–3 1992) 107–141.

[47] J.W. Payne, J.R. Bettman, E.J. Johnson, Behavioral decision research: a constructive processing perspective, Annual Review of Psychology 43 (1992) 87–131.

[48] J.W. Payne, E.J. Johnson, J.R. Bettman, The Adaptive Decision Maker, Cambridge University Press, Cambridge, 1993.

[49] J.W. Payne, J.R. Bettman, M.F. Luce, When time is money: decision behavior under opportunity-cost time pressure, Organizational Behavior and Human Decision Processes 66 (2) (1996) 131–152.

[50] G.N. Punj, R. Staelin, A model of consumer information search behavior for new automobiles, Journal of Consumer Research 9 (March 4 1983) 366–380.

[51] K. Sengupta, T.K. Abdel-Hamid, Alternative conceptions of feedback in dynamic decision environments: an experimental investigation, Management Science 39 (4) (1993) 411–428.

[52] J. Shanteau, Competence in experts: the role of task characteristics, Organizational Behavior and Human Decision Processes 53 (1992) 252–266.

[53] M.S. Silver, User perceptions of decision support system restrictiveness: an experiment, Journal of Management Information Systems 5 (1) (1988) 51–65.

[54] M. Silver, Decision support systems: directed and nondirected change, Information Systems Research 1 (1) (1990) 47–70

[55] M. Silver, Systems that Support Decision Makers: Description and Analysis, Wiley, Chichester; New York, 1991.

[56] K. Smith, Decision-making in rapidly changing environments: trading in the spot currency markets, PhD Dissertation, University of Minnesota (UMI/Proquest Dissertations publication number AAT9621914) 1996

[57] B.C. Smith, J.F. Leimkuhler, R.M. Darrow, Yield management at American airlines, Interfaces 22 (1) (1992) 8–31.

[58] K.E. Southwood, Substantive theory and statistical interaction: <sup>fi</sup>ve models, American Journal of Sociology 83 (5) (1978) 1154–1203.

[59] N. Srinivasan, B.T. Ratchford, An empirical test of a model of external search for automobiles, Journal of Consumer Research 18 (2) (1991).

[60] M. Sujan, Consumer knowledge: effects on evaluation strategies mediating consumer judgments, Journal of Consumer Research 12 (June 1985) 31–46.

[61] V. Swaminathan, The impact of recommendation agents on consumer evaluation and choice: the moderating role of category risk, product complexity, and consumer knowledge, Journal of Consumer Psychology 13 (1/2) (2003) 93–102.

[62] P. Todd, I. Benbasat, The use of information in decision making: an experimental investigation of the impact of computer-based decision aids, MIS Quarterly 16 (3) (1992) 373–393.

[63] P. Todd, I. Benbasat, An experimental investigation of the relationship between decision makers, decision aids and decision making effort, INFOR 31 (2) (1993) 80–100.

[64] P. Todd, I. Benbasat, The in<sup>fl</sup>uence of decision aids on choice strategies: an experimental analysis of the role of cognitive effort, Organizational Behavior and Human Decision Processes 60 (Oct 1 1994) 36–74

[65] P. Todd, I. Benbasat, Evaluating the impact of DSS, cognitive effort, and incentives on strategy selection, Information Systems Research 10 (4) (1999) 356–374.

[66] L. Van Wallendael, Y. Guignard, Diagnosticity, con<sup>fi</sup>dence, and the need for information, Journal of Behavioral Decision Making 5 (1992) 25–37.

[67] C.V. Zenios, S.A. Zenios, Benchmarks of the ef<sup>fi</sup>ciency of bank branches, Interfaces 29 (3) (1999) 37–51.

Michael Davern is Associate Professor in Accounting and Business Information Systems, and Director of the Master of Business and IT program at the University of Melbourne. He obtained his Ph.D. from the University of Minnesota and previously was on the faculty at New York University. Using behavioral and business process perspectives his research in information systems focuses on the value of IT, managerial decision making and control, appropriation, and enterprise risk management. His research is supported by both the corporate sector and the Australian Research Council (LP0774949, LP100100068) and has been published in the Journal of Management Information Systems, Decision Support Systems, Communications of the ACM, Information Technology & People, and DATA BASE, among others. He currently serves as an associate editor for the journal AIS Transactions on HCI.

Arnold Kamis is an Associate Professor of Information Systems and Operations Management at Suffolk University. He received his Ph.D. in Information Systems from the Stern School of Business of New York University and his B.S. in Applied Mathematics (Computer Science) from Carnegie Mellon University. Arnold's research interests are in human–computer interaction and decision support systems in the domains of ecommerce and e-healthcare. His publications appear in MIS Quarterly, The American Statistician, Information & Management, International Journal of Electronic Commerce, Communications of the ACM, among others. He serves as chair for the HICSS Minitrack on Electronic Marketing and is the Web Site Editor for the Journal of Management Information Systems.
