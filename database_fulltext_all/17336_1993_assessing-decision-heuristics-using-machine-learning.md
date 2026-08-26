---
otero_id: 17336
otero_key: "48DYCQJH"
title: "Assessing decision heuristics using machine learning"
authors: "Michael Lewis"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90038-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Assessing decision heuristics using machine learning \*

Michael Lewis

University of Pittsburgh, Pittsburgh PA, USA

In decision making, automatization associated with 'skill' contributes to the discrepancies often found between actual and reported use of information. Designing decision support systems (DSS) to assist skilled decision making is complicated by this lack of accessible models. This paper proposes a model of skilled decision making in which tacit heuristics define simplified situations within which skilled decisions are made. Heuristics employed in decision making are identified from qualitative representations of past decisions using machine learning. These heuristics can then be matched with performance criteria to identify conditions under which the user may need supplemental aiding. This use of machine learning to identify 'buggy' models of human performance has proved very difficult even for simple tasks such as subtraction. We argue that skilled interaction with real-time systems provides a special case in which the learning problem can he simplified sufficiently to allow user modelling of adequate quality for decision support. Our approach is illustrated in assessments of decision heuristics used by pilots in avoiding intruding aircraft and for operators of a simulated process plant. The ability to adapt decision support functions to complement the decision making processes of skilled users is argued to he essential to providing them effective support Attribute-based machine learning methods are proposed as a feasible mechanism for achieving this goal.

Keywords: Empirical learning; Cognitive modeling; Skilled decisions.

## 1. Introduction

Assessing heuristics used in skilled decision making is difficult because of the high level of automaticity which develops. The tacit knowledge and implicit learning $[27]$ it reflects are neither accessible to introspection nor explained by conscious knowledge. The relatively minor influences of training curricula and absence of relation between verbalizable knowledge and decisions is a common finding in this area $[22]$ . Using outcome as the sole criterion for assessing skilled decisions has its own pitfalls because comparable results may be produced by widely varying sequences of decisions $[16]$ . Despite this impenetrability, society relies heavily on skilled decision making for functions ranging from medical diagnosis to air traffic control. While decisions made by these practitioners are critical, they are difficult to support because no external model of the decision process is available.

Consider the complexity of decisions necessary to drive a car. A failure in planning (forgetting an exit) may combine with a poor decision to change lanes to produce a near collision which is then avoided due to skill in steering.

If asked about the near accident the driver would probably mention preoccupation, almost missing the exit, and not seeing the other car. If the interview went further we would probably find that the driver was aware of the blind spot and usually made a practice of checking in the rear view mirror as he drove to stay aware of his current situation. This example illustrates how measures of knowledge and success may be insufficient to fully characterize an individual's decision making and its need of support. We could only identify this driver's potentially fatal flaw, "making lane change decisions without explicitly re-checking the blind spot" by examining his decisions directly.

![](/api/attachments/48DYCQJH/fulltext/images/f95a683117eef5f4945490776e7839c74c27aeef844c6bf661ac170157bc0ce7.jpg)

Many routinized real-time decisions in uncertain environments are of exactly this sort. Nuclear power plant operators, commercial pilots, medical personnel, and financial officers all routinely make complex, high consequence decisions. The usual effectiveness of their heuristics, however, cannot preclude the existence of blind spots, which under the wrong conditions might lead to catastrophe. To support real-time, high consequence decision making, therefore, an intelligent decision support system should be able to model its user's decision making heuristics to identify when additional support is needed.

One solution is to construct a strong domain theory and use it as the basis for learning and aiding. This explanation-based learning (EBL) approach is being used in the Pilot's Associate program [15] to learn new pilot strategies. Although EBL can provide a richer and more detailed account of human behavior than empirical learning methods, success depends on the adequacy of its domain theory. EBL cannot solve our problem, however, because our objective is to provide support to “skilled decisions for which no external model of the decision process is available” and more particularly, to identify flaws (inconsistency with respect to a domain model) in this process.

Our approach to assessing decision heuristics lies in analyzing past decisions directly. We make the “common determination” assumption that the same decision heuristics account for both good and bad decisions. By identifying the relations between situations and decisions which were made, without regard to their consequences, it is possible to characterize these heuristics, themselves. A more comprehensive discussion of this approach to modeling decision processes is presented in [28]. Evaluations of this sort frequently occur informally through coaching in settings such as driver's training or flight instruction. A driver's training instructor, for example, would be likely to notice and point out the "mirror error" even though it might not be evident from the trainee's driving record.

This coaching function is difficult to objectify because it does not involve observed outcomes. It requires, instead, observing a decision, without regard to its consequences, and evaluating it within the context of the wider class of situations in which that alternative might he chosen. For an intelligent decision support system a coaching function might involve maintaining records of routinely requested/used information. Highly deviant values of neglected information could then be recognized and brought to the users attention.

A basic premise of our approach is that heuristic simplifications are made in terms of the semantics of situations rather than continuous values defining them. A heuristic simplification used in buying a car, for example, might classify prices as affordable or not affordable and style as mid-size and four door or not. The decision involving continuous values of price, size and style would then he made within this restriction. Problems arise when the restriction is either too broad or too narrow. This car buying simplification, for example, ignores color (perhaps too broad) and excludes larger cars even if affordable (perhaps too narrow). Decision heuristics of this sort are essential to skilled decision making because they substantially narrow the range of alternatives which must be considered. Heuristic simplifications of this form can be identified by examining qualitative versions of past decisions. If the car buyer repeatedly bought affordable, mid size, four door cars of varying color and make, we might infer the presence of such a restriction.

This view of the semantics of situations parallels that of researchers in qualitative reasoning $[1]$ . In these approaches, continuous values are replaced by a discrete number of ranges defined by qualitative changes in states. The boundaries at which transitions occur are termed landmarks $[12]$ . Non-transitional changes are represented through qualitative derivatives (decrease, no change, increase). A closed container of water heated by a flame $[8]$ , for example, would define pressure at two values, enough-to-burst container and not-enough-to-burst container and at three discrete rates of change $(-, 0, +)$ . This simplified representation characterizes the semantics of the system. It is either cooling and unburst (and will stay unburst), heating and unburst (and will eventually burst), constant and unburst (and will stay unburst), or heating, cooling, or constant and burst (and will stay burst).

The value to DSS of a model of routine, high consequence decision making as a decision process occurring within heuristic restrictions is that it offers the possibility of adapting decision support functions to individual users' decision processes. Decision makers entrusted with routine high consequence decisions in uncertain environments are (by natural selection) almost always skilled in making such decisions. As we have argued above, a major component of this skill lies in the decision heuristics they have developed. A DSS which disregards this fact by providing advice or predictions (which are likely to be no better than the user's own in uncertain environments) is almost certain to encounter problems with user acceptance and is unlikely to improve the quality of decisions. An expert system, KARL, used as a decision aid for the process control task described later in this paper was universally disliked by users [11]. Subjects complained that it 'nagged' them, turned the DSS off when they were allowed, and failed to heed advice when it was provided. Limiting decision support functions to display and analysis of information, however, disregards exactly those aspects of skilled decision making most in need of support, the blind spots.

Although using machine learning to model human heuristics in order to detect their flaws has obvious and intuitive appeal, the value of the approach depends on the quality of results which can be obtained from real subjects performing realistic tasks. The inherent variability of human performance and its unfortunate relation to the weaknesses of empirical machine learning make this difficult. Surprisingly little data actually exist on the validity of empirically learned models of human performance.

The study of children's ‘bugs’ in subtraction [3,13,32] forms the most substantial corpus of research in the area. Although DEBUGGY [3] used a bug library, its natural evolution was to acquire bugs directly using machine learning. This final step from matching noisy human data with predefined templates to learning the templates themselves has remained elusive.

The major obstacles to modeling human performance are noise, weak sequential dependency, and bias. Noise refers to examples which contradict the ‘concept’ being learned and is pervasive in behavioral data due to human variability. Problems of sequential dependency arise because many human activities are partially rather than completely sequential. If, for example, I start the car on one occasion before turning on the lights and on another occasion I turn the lights on first, the program is presented with a contradiction and cannot learn about either activity. Bias refers to the space of possible ‘concepts’ learnable by a program from a representation. If a bias is restrictive (the space is small) fewer examples are needed to produce a description which is probably approximately correct [9]. An overly restrictive bias, however, may exclude the very forms of expression needed to model the performance.

In concert, these characteristics present severe problems to empirical machine learning. If examples are neither independent (in which case they would meet the assumptions of weak machine learning methods) nor completely dependent (in which case they could he made independent by appending a token indicating the previous activity) then strong domain models of the partial sequential dependencies are needed. Detailed representations of this sort, however, are not amenable to efficient attribute based methods which require a uniform learning space. As a consequence, modeling is forced into strong methods such as complete searches of large graphs or the use of templates. Eliminating the noise of human data and using problem/answer pairs as examples Langley and Ohlsson [13] report that their automated cognitive modeler (ACM) could successfully learn production rule conditions for VanLehn's bugs "given idealized behavior on a set of 20 representative test problems." VanLehn and Garlick [32] report success at the complementary problem of learning partial sequential dependencies (plans), given the 'production rules', by analyzing subtraction protocols (what the child did) using ID3. What appears unobtainable even for this apparently simple task is the simultaneous identification of production rules and control structure from noisy human performance data. This is precisely what must he done to identify the inaccessible models involved in skilled decision making for use in decision support.

Although any deterministic machine learning algorithm will produce ‘rules’, examples which are partially sequentially dependent and sometimes incorrect, will reflect idiosyncrasies of the training examples and be useless as a basis for aiding. Langely and Ohlson refer to this as the problem of identifying “consistent and psychologically plausible” rules. Consistency and psychological plausibility go hand in hand in determining the validity of the learned model because a model of human performance which is not psychologically plausible, is unlikely to describe additional examples and therefore unlikely to be truly (in the population of examples) consistent.

We report two successful applications of empirical machine learning methods to modeling human performance at skilled decision tasks. This success does not result from any advance in machine learning but rather from identifying a restricted class of problems for which empirical learning can work. Skilled decisions involving human-machine interaction provide this very special case in which human performance closely approximates the requirements of empirical learning methods. Skilled behavior is largely automatic and therefore highly consistent and relatively noise free. To the extent that decisions are made in response to a currently displayed state, the difficulties associated with partial dependencies among actions are also minimized. Despite these nearly ideal conditions, pre and post-processing were still required to compensate for noise and sequential dependencies. In one data set, learning was performed using both full and reduced (deleted attributes) training examples and the $\tau_{b}$ statistic used in post-processing to select the 'best' rules. In the other, a bootstrapping method was used in which rules were repeatedly learned from subsets of examples and compared with the full sample for selection or rejection. In all cases the description of human performance provided by the learned model is shown to be both psychologically plausible and statistically robust. The significance of this research to the use of machine learning in decision support systems lies in its demonstration that for at least this restricted class of problems it is possible to identify reliable human performance descriptions using empirical learning methods. Although machine learning may have other applications in acquiring knowledge about the domain, this research demonstrates in ways others have not, that it is possible to learn useful user models from actual human performance data.

Decision heuristics found for skilled pilots and well-practiced process control subjects are presented in this paper. Individuals who might have benefited from heuristic-sensitive aiding are present in both groups. Nearly half the pilots chose evasive maneuvers which brought them nearer intruding aircraft under conditions predictable from identified heuristics. Decisions and performance of practiced process control subjects were found to be much better characterized by their decision heuristics than differences in training or tested proficiency (e.g., familiarity with a normative model). Such results suggest that intelligent decision support adapted to individual decision making strategies may be a viable approach to supporting skilled decision makers.

## 2. Machine learning methods

Decision heuristics from two problem domains identified, using three distinct machine learning methods are presented in this paper. Our purpose is to illustrate the potential of empirical machine learning for identifying decision heuristics used in skilled decision making rather than to advocate particular methods. In fact, highly similar descriptions were found when very different approaches, AQ and a genetic classifier, were used to assess the same decisions.

The machine learning methods used are all forms of concept learning in which data were presented as examples consisting of a described condition and the action chosen under that condition. All three methods learn conjunctive expressions which are consistent generalizations of the conditions under which a particular action was observed. These generalizations are production rules which serve to predict the decision maker's choice of alternatives.

Two of the machine learning methods, AQ [20], and INDUCE [10] were used to find minimal discriminant descriptions. Minimal discriminant descriptions are the most general description of a set of examples which excludes all examples for which a particular alternative was not chosen and includes all examples for which it was chosen. Both methods form these descriptions as a disjunction of conjunctive expressions which we interpret individually as production rules. Because all expressions are conjunctive, the connections between bracketed conditions are dropped. The attribute based rule learned by the AQ method from the examples:

```ini
[temperature = warm][weather = sunny]
```

```toml
[temperature = cold][weather = cloudy]
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
[temperature = warm][weather = rain]
 $\Rightarrow \neg go\_to\_park$
</div>

would be:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
[weather = sunny or cloudy] $\Rightarrow$ go_to_park
</div>

This example illustrates the algorithm's two generalization methods:

\- dropping attributes (temperature) which do not discriminate between positive and negative instances of going\_to\_park;

\- forming disjunctions of attribute values (for non-negative instances) which are involved in the discrimination.

The existential conjunctive rule learned by the INDUCE method from the examples:

```ini
[open_valves(column-1, column-2) = 2]
[open_valves(column-2, column-3) = 3]
⇒ do_nothing
```

```txt
[open_valves(column-1,column-2) = 2]
[open_valves(column-2,column-3) = 2]
⇒ do_nothing
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
[open_valves(column-1,column-2) = 1]
[open_valves(column-2,column-3) = 2]
$\Rightarrow \neg$ do nothing
</div>

would be:

```ini
[open_valves(column-x, column-y) = 2 or 3]
[open_valves(column-y, column-z) = 2 or 3]
⇒ do_nothing
```

In this instance the positive examples of doing nothing are discriminated from the negative example by not having an “open\_valves” value of 1. INDUCE examples and rules can grow quite complicated because of the patterns of quantification they allow. In the reported analyses both attribute-based and existential conjunctive generalizations were generated using the INDUCE program. We refer to the learning method as AQ when only the star generation algorithm was used and as INDUCE when the program was used to generalize existential conjunctive concepts.

The genetic classifier [2] used to assess heuristics learned maximally specific characteristic descriptions. In contrast to the discriminant methods, characteristic methods do not consider negative examples in generalization. The genetic classifier learned attribute based descriptions similar to those of AQ. Heuristics were found by progressively removing matched examples and relaxing the specificity restriction (penalty on deleting attributes). Dropping attributes was the only generalization method available to the classifier. In the go-to-park example it could learn nothing because no expression in 2 or 1 attribute values describes more examples than these examples themselves.

Each method has its advantages and disadvantages. The logical methods are not error tolerant and require pre and post-processing to accommodate noise. Attribute-based concepts can be learned very efficiently but are limited to decision situations which can be described without variables. Existential concepts are inefficient to learn and limited to situations involving a fixed set of variables but provide a much richer description.

## 3. Pilot decision heuristics

Data from an experiment reported in $[24]$ are used in this example. A more detailed account of this application of machine learning is provided in $[17]$ . These CDTI (cockpit display of traffic information) experiments provide a test of our claim that psychologically plausible descriptions of human performance can be obtained from real data using machine learning. Although the simulator avoidance task is somewhat artificial it resembles flight tasks these pilots performed regularly. The learning problem is simplified because only a single maneuver is performed, eliminating difficulties associated with sequential dependencies among actions. The task itself is of precisely the sort we predict should be describable by machine learning. It involves skilled behavior in response to changes in a displayed situation.

Palmer's experiment investigated the effects of information quality and intruder characteristics on the use of a cockpit display of traffic information (CDTI) shown in fig. 1. In this experiment, sixteen experienced pilots ‘flew’ sixteen programmed encounters under three display conditions. Pilots were instructed to maintain a steady course, using the autopilot unless they received a threat advisory. In response to the threat they were told to maneuver to maintain a horizontal separation of greater than 1.5 nautical miles and a vertical separation in excess of 500 ft while staying as near as possible to their programmed flight path. The three display conditions were:

![](/api/attachments/48DYCQJH/fulltext/images/c3b1393abd53178e37df25d0c0ecd3bbf7c45a46e146d9a2f5609354de17fce5.jpg)  
Fig. 1. CDTI predictor display.

(1) in the least informative condition the CDTI portrayed the relative positions of the ownership (that being piloted) and the intruder along with tags showing their altitudes;

(2) the predictive CDTI provided ground referenced predictors showing predicted positions of the ownership and intruder as well as an additional tag showing the intruders projected altitude at time of closest approach;

(3) in the third condition noise was introduced into the predictive CDTI.

Researchers investigating pilot use of cockpit displays of traffic information $[26,30]$ have found maneuver decisions to depend upon encounter, display characteristics and individual differences. In the development of the CDTI, therefore, it is important that both generalized decision making strategies shared by most pilots and idiosyncratic decisions of the few be understood. Plans call for the CDTI to be used in conjunction with a second advisory decision support system, the collision avoidance system (CAS). To integrate these decision support functions it is important to gauge the influence of the display on pilot maneuvers so that advisories can he formed which are both consonant with pilot decisions and which avoid conflicts among decisions made by multiple pilots. Radar assisted collisions discussed by Curry [5] demonstrate the danger of introducing decision support technology without considering possible interactions.

Encounters were re-represented in qualitative form in order to identify heuristics underlying the pilots' decisions, Encounters were characterized by the attributes: horizontal passing position (behind, intercept, or infront), vertically crossing trajectories (no, yes), intruder vertical velocity (zero or non-zero), projected horizontal separation at point of closest approach (very near, 0–0.24 nm, near, 0.24–1 nm, far, >1 nm), and projected vertical separation at point of closest approach (very near, 0–140', near, 140–350', far, >350').

Pilots' responses were represented by maneuvers toward or away from the intruder along a dominant axis. The dominant axis was determined by comparing the horizontal and vertical magnitudes of a maneuver to the respective tolerances which the pilots had been instructed to maintain. Five maneuvers result: No action, vertical-toward, vertical-away, horizontal-toward, and horizontal-away.

## 3.1. Pilot strategies

Within the range of encounters examined, the vertical movement of the intruder appears the most crucial factor in determining the pilot's dominant response. Under conditions in which the intruder approached at a constant altitude pilots under all displays, with few individual differences, and with little regard to the degree of threat, maneuvered vertically away. This heuristic follows the principle of least effort in limiting the decision to a single dimension (vertical velocity) and producing a response which increases separation at point of closest approach under all conditions. While ensuring success at the pilots' primary task of avoidance, this strategy may run counter to the secondary task of maintaining course in the face of non-threatening encounters. This shortcoming is highlighted by noting that of 48 occasions on which the pilot did not maneuver only one occurred under these conditions.

![](/api/attachments/48DYCQJH/fulltext/images/5f2ea0f08cf1e5f746fae9b2ee6113b1f6ad682a0c64a57306204e93003ed6f1.jpg)  
Fig. 2. Encounter geometry.

When the intruder was changing altitude the vertical response dimension was largely ignored accounting for the dominant response on only 24% of such occasions.

As in previous studies investigating decisions made using the CDTI system $[7,25,30]$ , horizontal-toward were preferred to horizontal-away maneuvers. Fig. 2 illustrates the geometry of the horizontal component of encounters. Turning toward an intruder which would have passed in front increases separation, while turning toward an intruder which would have passed behind decreases separation. The tendency of some pilots to turn toward an intruder which would have passed behind has been attributed to their desire to maintain visual contact with the intruder $[26]$ . On the other hand, $[7]$ suggests that the pilots desire, instead, to minimize the time to resolution of the conflict by passing behind the intruder. Additional light on this preference is provided in $[30]$ , which found that encounters rated as less threatening showed a stronger turning-toward tendency. AQ heuristics identified for the horizontal-toward decision support this view by showing a general preference for the horizontal-toward response while using predictor displays (which allowed a clear view of conflict resolution), but limiting the response to the more conservative recommended strategy when the display lacked predictors. Heuristics identified using the genetic algorithm were insensitive to display type.

This discrepancy is likely due to differences in the representational biases and learning criteria of the methods. The genetic classifier, lacking the ability to represent disjunctions of attribute values, dropped the display attribute as one the least characteristic (being evenly distributed across the response alternatives) of the attributes. The differences among responses, the availability of disjunctive values, and the discriminant learning criterion of AQ, by contrast, forced the generation of rules describing the difference.

As found in earlier studies [7,26,30] large individual differences were noted among pilot's decisions. The most nearly universal decision was the choice of the vertical-away maneuver under conditions in which it unambiguously increased separation.

The heuristics identified suggest that vertical information may not be presented in the most useful manner by the decision support system. The identified decision heuristics exclude vertical separation although it contributes as much to achieved separation and collision avoidance as the horizontal dimension. This neglect is further reflected in the pilots' overall preference for horizontal maneuvers. In [30] it is suggested that the preference for horizontal responses may be due to FAA regulations, comfort, safety or fuel conservation but the absence of vertical information from decision heuristics suggest the bias may more likely he due to the superior display of horizontal traffic information by the decision support system.

The finding that pilots using predictive CDTI displays were more likely to proceed with conflict resolution by turning toward the intruder than following the recommended strategy reinforces concerns aired in $[14,25]$ and elsewhere that CDTI in some instances may actually make collisions more likely.

Earlier analysis of this data $[24]$ indicates that the noiseless predictor display led to fewer positive CAS advisories and smaller maneuver magnitudes while the predictorless display resulted in smaller achieved separations and less frequent agreement with the recommended strategy. The present investigation suggests that the superiority in performance on the predictor displays results from improvements in execution rather than fundamental shifts in decision heuristics. For one group of pilots, in fact, consistent violation of the recommended strategy was linked with the use of the noiseless predictor display. While the most widely employed strategy observed was the vertical away response to a constant altitude intruder, vertical responses were generally avoided under other conditions. Since projected altitudes at closest point of approach provide information unavailable from rapidly updating data tags, the failure to find a related consistency in pilots' responses suggests some difficulty in abstracting or using this more detailed altitude information in the form it was presented.

![](/api/attachments/48DYCQJH/fulltext/images/f876450a26a604205545fc76090acd63f5b35fc170decf9cc5677e50f593bfcd.jpg)  
Fig. 3. Pilot decision sequence.

A convergent picture of the pilots' maneuvers as a heuristic decision sequence emerges from both the AQ and genetic algorithm descriptions. Apart from distinctions among pilots with respect to the ranges (very near = 0–0.24 nm vs very near or near = 0.24–1 nm) of values over which a strategy was employed the identified rules can be collapsed into four decision heuristics portrayed in fig. 3.

(1) If the intruder is approaching at a constant altitude a vertical-away response is chosen. This decision requires minimal effort since it will always agree with the instructions to increase separation in the same orientation as would have occurred in the absence of a maneuver.

(2) A subgroup of pilots chose not to maneuver in non-threatening encounters in accordance with their second instruction of maintaining a constant course. This decision comes second since it was restricted to encounters in which the constant altitude condition was not present.

(3) A second subgroup of pilots consistently chose a horizontal-toward response for horizontally near intruders in conflict with separation instructions for intruders which would have passed behind.

(4) The horizontal-toward decision common across pilots introduced the additional stipulation that the intruder would pass in front bringing the decision into agreement with instructions.

This sequence portrayed in fig. 3 illustrates a series of heuristic simplifications in which pilots chose the simplest decision (turning away from a constant altitude intruder) if possible before considering the potential threat of the intruder. In the incorrect variant of the horizontal-toward choice a subset of pilots again simplified their decision by restricting consideration to proximity information, ignoring the more complicated encounter geometry.

This example demonstrates that simple representations and simple empirical machine learning methods were sufficient to identify psychologically plausible and consistent models from human data. The tendencies identified, preference for horizontal maneuvers and turning toward intruders, are the same ones described anecdotally elsewhere in the literature. The predictive information already needed to drive the CDTI and simple expressions of the “avoid unnecessary maneuvers” and “choose direction which increases separation” criteria would have provided the information needed for adaptive aiding. Without resort to a domain theory, a machine learning method which identified these heuristics, could supply them to an aiding module. By matching conditions with those on the display, the aid could detect precisely those conditions under which advisories were needed for particular pilots. Those not exhibiting blind spots in their maneuvers could be left without distraction to perform their other tasks.

## 4. Decision heuristics in process control

Our second example extends this approach to skilled subjects controlling a simulated industrial process. Unlike the pilots who performed a discrete maneuver under identifiable conditions, process control operators perform a continuous control task requiring planning. These experiments provide a test of the effectiveness of simple methods for representing qualitative derivatives and approximating current goals which allow the identification of heuristics from behavioral data under sequentially dependent conditions. The task is representative of the class of problems we argued in the introduction might be most appropriate for aiding based on machine learning. It has no strong domain theory, relies on unarticulated skilled behavior, and was found in $[11]$ to be resistant to aiding by a conventional expert system. The task is typical of many found in process industries. Although its high level goal, “pump as much feedstock through as possible” is clear, there are many alternate styles and strategies for achieving it.

PLANT (production levels and network troubleshooting) is a simulation of an industrial process in which feedstock is pumped in at one end and finished product pumped out at the other. A detailed description of the simulation and a summary of experiments involving PLANT are presented in [23]. PLANT consists of a series of tanks interconnected by valves. Tanks are arranged in columns. Each tank is connected by valves to each of the tanks in the adjacent columns. Each tank has a pump which may be either operational or failed. Pumps at the input and output side of the system supply feedstock or remove product from banks of tanks. The operator controls valve position (opened or closed) and pumping rates for feedstock and product.

## 4.1. Plant dynamics

Dynamics are based on differential equations which model fluid flow through piping. When a valve is opened a surge of fluid is forced through the pipe leading to are oscillation in flow. Over time this oscillation dampens but does not completely disappear. The amplitude of this surge is dependent on the height difference between the tanks.

These dynamics result in a system which behaves in ways characteristic of actual industrial processes. The effects of a control action are noticeable only after a lag. Even then, the result is not clearly evident until the transient settles out of the system. The nature of this response is additionally dependent on relative tank heights and the number of valves open from the tank. These dynamics result in a difficult decision task. Additional verisimilitude is provided by safety systems which trip valves closed when flow through a pipe exceeds a setpoint.

![](/api/attachments/48DYCQJH/fulltext/images/03aa70b46ca035d54fd104b837673a622219b34749e4428801f79c8c7264887b.jpg)  
Fig. 4. PLANT display.

## 4.2. Interface

The operator's primary display is a graphic depicting the network of tanks, shown in fig. 4. Tank level is displayed numerically as percentage of capacity and in analog by shading the tank icon proportionately. Open valve position is represented by lines between tanks.

An ancillary display contains a short history of command lines, responses to test flow and repair requests, and production records. Commands are entered through a keyboard. The simulation is self-paced, updating after each command. Data is collected at each iteration including: tank levels, valve positions, and pumping rates. Because the object of the task is to produce product, high level strategy is fairly simple. All valves should be open to provide maximum flow between the input and output. Pumping levels should be set as high as possible without introducing instabilities.

## 4.3. Procedure

PLANT logs from an experiment described in [21] which recorded a complete record of the plant's state at each iteration were used to provide examples for learning rules to characterize the subjects' heuristics. The 9-tank, 18-valve, 2-pumping-rate state of the plant was augmented with qualitative derivatives and a token reflecting the currently appropriate control goal to form examples. Subsets of examples were repeatedly generalized using INDUCE in a bootstrapping procedure intended to compensate for noise in the data. Sets of rules for opening valves, skip and flow checking, and commands for increasing feedstock pumping rate were found for all subjects. An average of 8.8 rules accounting for 70% of the approximately 1000 responses with 1% errors were found for each subject. Comparable performance was observed in independent validation samples of 500 observations where these rules accounted for 74% of the responses with 2% errors.

Intuitively, subjects with similar heuristics might be described as subjects who do the same thing under the same conditions. Description of their performance in the form of condition-action rules allows us to formalize this definition of similarity. We define the intersection of two rule sets to be the set of states matching the conditions of both (both subjects make the same response) and the union to be the set of states matching the rule sets of either subject.

A distance measure, D, was defined on the subjects' rule sets: Using PLANT states present in the data to estimate relative cardinalities of these intersections and unions.

$$
D = \frac {\left| R _ {1} \cap R _ {2} \right|}{\left| R _ {1} \cup R _ {2} \right|}.\tag{1}
$$

D is similar to a correlation in ranging from 1, for identical rule sets, to 0 for rule sets with disjoint conditions. It behaves as a similarity measure across its range classifying both rule sets with wide coverage and relatively little overlap and rule sets differing in extent of coverage as dissimilar.

Distance matrices based on D were generated for valve opening, skip/flow, rate increase, and a combination of the three commands for the subjects' rule sets. An additive tree clustering procedure [4] was then used to group subjects according to these similarities. The groups defined by the clusters were compared on performance measures using one-way analysis of variance and identified effects interpreted by examining rule sets of the clusters. Reported clusterings all account for more than 95% of the variance in the distance measure.

## 4.4. Results

Table 1 compares the variance in performance measures explained by grouping subjects in accordance with similarities among their rule sets with the effects of training manipulations for the same data (above the double line) and for the larger set of data examined by [21]. As might be expected, similarities in what subjects do appear to be a much stronger determinant of their performance on criterion measures then similarity in what they have been told or trained to do. The strength of this relation confirms our earlier assumption of common determination: The aspects of the subjects' responses being captured in our descriptions are also those determining performance on criterion measures.

Explained variance in summary measures $(\omega^2)^{\mathrm{a}}$

<table><tr><td></td><td>production</td><td>trips</td><td>open valves</td><td>it-to-repair</td></tr><tr><td>Grouped by rules</td><td>0.52</td><td>0.74</td><td>(0.63)</td><td>0.29</td></tr><tr><td>Grouped by training</td><td>(0.004)</td><td>(0.13)</td><td>(0.24)</td><td>0</td></tr><tr><td colspan="5">Morris 1983 full experiment</td></tr><tr><td>procedures</td><td>0</td><td>0.12</td><td>0.20</td><td>-</td></tr><tr><td>principles</td><td>0</td><td>0</td><td>0</td><td>-</td></tr></table>

$^{a}$ Values inclosed in parentheses are not significant at the p < 0.05 level but are included for comparison. Tests for subjects grouped by rules are based on full permutation distributions of their F statistics.

Descriptions of decision heuristics for opening valves illustrate the power of this approach in characterizing decision processes. The clusters defined in fig. 5 provide a precise view of differences among subjects in the decision to open valves. Decision heuristics for opening valves can be classified as either strong or weak, where strong means applicable in situations having any closed valves, and weak applicable only in situations having multiple closed valves. A strong heuristic can be identified by the presence of the expression $[vlv(c1,c2)\#3]$ (all valves are not open between two columns) in its description. Weak heuristics, by contrast, may contain expressions such as, $[vlv(c1,c2)=1]$ (more than 2 valves are closed between two columns) or $[vlv(c1,c2)\#2]$ (it is not the case that one valve is closed between column 1 and column 2).

Subjects employing the strong heuristic place a high priority on keeping all valves open (a good heuristic for controlling PLANT) while subjects using the weak heuristic give less weight to the choice of opening valves.

![](/api/attachments/48DYCQJH/fulltext/images/0f1f1f79895905ee4794df3c6b1e5d6044894a9879e21111c3c52f61fbdfade4.jpg)  
Fig. 5. Clustering for decision to open valves.

Four clusters and one idiosyncratic subject were identified by distinct value opening strategies. This grouping of subjects accounts for $\omega^{2}=0.52\ (p<0.05)$ of the variance in production and $\omega^{2}=0.63\ (p<0.05)$ of the variance in average number of open valves. The clusters may be characterized in the following way.

Cluster 1 (bak, jcs, lxs, pjg, wdn, wtl) Subjects with strong heuristics for opening closed valves which are augmented to take into account adjustments in compensating for large within column differences in tank heights.

Cluster 2 (rjc, shl) Subjects with strong heuristics for opening closed valves which are augmented to allow adjusting valve closure in compensating for imbalances between input and output columns.

Cluster 3 (djr, hmb, jrp, tdd) Subjects with strong heuristics for opening closed valves but without heuristics for manipulating valves to adjust tank levels.

Cluster 4 (chw, cms) Subjects with weak heuristics for opening closed valves and without heuristics for manipulating valves to adjust tank levels.

The description of heuristics found for pjg provide an example of cluster 1 subjects.

$$
\begin{array}{c} \text {[dcm = wci][difc(c1,c2) = 2,3][ddif(c1,c2) = 3]} \\ \text {[pio(p1)\#2]} \\ \text {[tpt(p1)\#1][vlv(c1,c2)\#3](maxw(c2) = 2,3]} \end{array}
$$

There is a within column imbalance and the difference in tank levels between the imbalanced column and the column to its left is moderate or large and increasing and a pumping rate has been changed but not in the last three iterations (valves need to be opened to compensate for the increasing between column imbalance whether or not they had been previously closed to adjust within column levels).

$$
[ \text { forall - cs(maxw } = 2) ] [ \text { vlv } (c 1, c 2) \# 3 ].
$$

Within column tank level differences are all within a normal range and a valve is closed.

$$
[ \operatorname{vlv} (c 1, c 2) = 1 ].
$$

If two or more valves are closed between two columns, a valve is opened.

The first heuristic describes conditions under which a tank level adjustment strategy should be overridden by opening valves. The second heuristic prescribes opening any closed valve if tank levels are balanced. The third heuristic calls for opening valves any time a large number of valves are closed between columns regardless of other strategic considerations.

The correspondence between these decision heuristics and the task demands of maintaining stability and flow of product directly mirror the quality of the subjects' decisions. Differences in performance on all four measures have the same order (1–4) as these clusters.

Although subjects who developed similar heuristics also tended to be similar in performance, there were some large differences among subjects with very similar criterion performance. These are differences in decision making which are hidden from conventional approaches to performance assessment. Two of the best performing subjects in this sample came from the group receiving minimal instructions. Subject, BAK, adopted the normative heuristics common to the best performing subjects receiving explicit training. For all decision alternatives examined, BAK is grouped with these same subjects (LXS, PJG, and WTL). This group followed the strategy of maintaining stability in the plant, keeping valves open, and maintaining stable pumping rates. Although AKS performed only slightly less well than BAK the pattern of responses was highly idiosyncratic falling into an individual cluster for the combined, open valve, and no action response categories. An examination of heuristics identified for AKS reveals that this performance was achieved despite a pattern of responding that risked instability.

An examination of described heuristics shows that AKS had developed an effective decision-making strategy that was completely different from the one advocated in PLANT training. Rather than relying on stability to achieve production over an extended period, AKS employed high pumping rates as long as they could be maintained and then lowered them just as instability approached. The effectiveness of these heuristics is seen both in performance (AKS has one of the lowest rates for tripped valves as well as high production) and the decision heuristics, most of which addressed the adjustments needed to tune this produce-and-stabilize strategy.

For these data empirical machine learning methods again produced psychologically plausible and highly predictive descriptions of the process control subjects' behavior. Decision aiding for tasks of this sort, however, cannot take the form of advisories as in the CDTI encounters because clear performance criteria are unavailable. The undesirability of close monitoring under these relatively relaxed conditions is emphasized by the hostile reactions aroused by the didactic style of an expert system used as an aid [11]. Under these conditions a coaching function might provide the most effective form of aiding. Learned heuristics could be stored off-line for later use by operators desiring to improve their productivity. Although the record would not be prescriptive it could provide an operator with clear indications of conditions under which important considerations such as balancing columns were being ignored.

## 5. Discussion

These examples demonstrate that useful descriptions of the decision heuristics of pilots and process control subjects could be found using machine learning. In both cases these heuristics accounted for individual differences in performance and identified conditions under which individual decision makers were prone to error. The development of a successful idiosyncratic decision making style by subject, BAK, highlights the fallacy of presuming that complex, sequential decisions must have uniquely preferred solutions.

Providing support for decision makers following a variety of idiosyncratic strategies and simplifications is a daunting task. The temptation to construct and support a “normative” model whether through EBL or an expert system is strong. Such an approach succeeds, however, only to the extent that users can be induced to follow a single normative sequence of decisions. The PLANT data suggest that that this may be an unrealistic expectation in complex domains where outcomes depend on the interaction of many sequential decisions. Neither training users in a normative model (the training manipulation) nor aiding users in accordance with that normative model (the expert system) improved performance. The alternative is to adapt the DSS to the decision processes which are actually occurring rather than supporting an “ideal” decision process which is not.

The form of these adaptive decision support functions depends on the tasks they must support. Complex, real-time decisions of the sort addressed in this paper typically involve long sequences of rapid decisions made in the presence of massive amounts of information. A reactor operator, for example, will have in excess of 2000 displays on which to base his decisions. A physician may receive reports of more than 50 tests from a single blood sample. Human decision makers are required to perform these ‘impossible’ decision tasks, precisely because of their criticality and human abilities to develop skill (e.g., heuristic simplifications) for making them. In this paper we have shown that for two tasks of this sort the heuristic simplifications needed to allow skilled decisions could be approximated using empirical machine learning methods. Decision aiding strategies which attempt to ‘compensate’ for the simplifications which constitute their user’s skill only exacerbate the problem. In domains ranging from nuclear power plants [19], to network management [31], to hospital operating rooms [6] the major problem lies in an excess of ‘decision support’ in the form of advisories and warnings not in its absence.

Once the ‘sub-optimal’ simplifications of skilled human decision makers are accepted as a positive rather than negative feature of their decisions, the problem of protecting these users from their own ‘skill’ is raised. As we pointed out in the introduction, even very good heuristics may harbor blind spots, peculiar conditions under which normally effective simplifications lead to decisions with unacceptable outcomes. What these conditions are will depend on the individual decision maker. The choice of a human decision maker paired with a DSS to perform a task constitutes an a priori admission that human decision making skills are needed. An intelligent DSS, therefore, must not regularly ‘second guess’ (e.g., nag) its user but should be able to identify and intervene on those occasions where its help is truly needed. Unfortunately, these occasions, cannot be anticipated by either the DSS designer or its user.

One solution to this problem lies in incorporating machine learning capabilities within the DSS which allow it to model its user's heuristics. For tasks with clear performance criteria a model of user heuristics together with a database defining system performance criteria could be used to provide as-needed support for skilled decision making. For tasks lacking clear performance criteria decision aiding will be difficult in any case, and machine learned models may help clarify what the criteria should be for a particular user and skilled decision making style. For environments in which data are accessed and decisions rendered through a computer such adaptive decision support may be feasible in the near term. A flight computer aware of one pilot's habit of turning toward approaching aircraft could issue an advisory when this decision could decrease separation unacceptably while remaining silent under other conditions and for other pilots. This silence, itself, is a form of decision support in that it decreases the quantity of information which must be assimilated, freeing mental resources for other demanding decisions. A medical record keeping system might track test results and treatments, not to supplant the physician's diagnostic judgement, but to bring to his attention normally unheeded results on those rare occasions where customary forms of treatment might be inappropriate. The premise behind this approach to decision support is not that the decision makers are unaware of the significance of unheeded information but rather that this information is normally unimportant to the success of their decisions.

The potential of machine learning for adaptive decision support depends on several factors. The approach is best suited to tasks involving complex routine decisions. Although the descriptive power of structural learning methods such as INDUCE are attractive, they are inefficient and require many examples to approximate ‘correctness’ [9]. Attribute-based representations, by contrast, are efficient to learn, require relatively few examples, and can be evaluated for accuracy [18]. The heuristic simplifications involving excluded categories and ignored distinctions which attribute-based methods learn are also those easiest to remedy through decision support. As Lewis and Heidorn [17] demonstrate, the quality of attribute-based descriptions of heuristics appears to be largely independent of the choice of machine learning method. The existence of a variety of efficient, robust learning methods for attribute-based representations such as ID3, AQ, and genetic classifiers argues for the early incorporation of adaptive support functions into intelligent DSS.

## References

[1] D. Bobrow, Qualitative reasoning about physical systems (MIT Press, 1985).

[2] L.B. Booker, D.E. Goldberg, and J.H. Holland, Classifier systems and genetic algorithms, Artificial Intelligence 40 (1989) 235–282.

[3] J.S. Brown and K. VanLehn, Repair theory: A generative theory of bugs in procedural skills, Cognitive Science 2 (1980) 155–192.

[4] J. Corter, ADDTREE/P: A PASCAL program for fitting additive trees based on Sattath and Tversky's AD-DTREE program, Behavior Research Methods and Instrumentation 14 (1982) 353–354.

[5] R.E. Curry, Will the ATSD precipitate display-assisted collisions?, in: H.G. Weiss and R.W. Bush, Eds., The Role of an Airborne Traffic Situation Display in an Evolving ATC Environment (PB-215-714) (MIT, Cambridge, MA, 1972).

[6] L.G. Deneault, C.M. Lewis, A. Debons and K.L. Stein, An integrated display for patient monitoring, 1990 International Conference on Systems, Man, and Cybernetics (1990).

[7] S.R. Ellis and E.A. Palmer, Threat perception while viewing single conflicts on a cockpit display of traffic

information (Report No. 81341) Moffett Field, NASA-Ames Research Center, CA (1982).

[8] K.D. Forbus, Qualitative process theory, In: Bobrow, Ed., Qualitative reasoning about physical systems (MIT Press) 85–168.

[9] D. Haussler, Learning conjunctive concepts in structural domains (Report No. USC-CPL-87-1) UCSC, Santa Cruz, CA.

[10] W.A. Hoff, R.S. Michalski and R.E. Stepp, INDUCE 3: a program for learning structural descriptions from examples, Department of Computer Science, University of Illinois at Urbana-Champaign.

[11] A.E. Knaeuper and N.M. Morris, A model-based approach to training and aiding in process control, Procedures 1984 IEEE International Conference on Systems, Man, and Cybernetics (1984) 173–177.

[12] B. Kuipers, The limits of qualitative simulation, Proceedings at the 9th IJCAI, Los Angeles, CA, Vol. 1 (1985) 128–136.

[13] P. Langley and S. Ohlsson, Automated cognitive modeling, Proceedings of the Fourth National Conference on Artificial Intelligence, Austin, TX (1984) 193–197.

[14] P.T. Lester and E.E. Quan, The cockpit display of traffic information and the threat alert and collision avoidance system integration: A review, Proceedings of the Second Symposium on Aviation Psychology, Aviation Psychology Laboratory, Ohio State University, Columbus, OH (1983).

[15] K.R. Levi, V.L. Shalin and D.L. Perschbacher, Identifying knowledge base deficiencies by observering user behavior. Proceedings of the Sixth International Workshop on Machine learning, Ithaca, NY (1989) 296–301.

[16] C.M. Lewis, Modeling individual differences at a process control task. Proceedings of the Human Factors Society 34th Annual Meeting, Orlando, FL (1990) 917–921.

[17] C.M. Lewis and P.B. Heidorn, Identifying tacit strategies in aircraft maneuvers, IEEE Transactions on Systems, Man, and Cybernetics SMC-21, No. 6 (1991) 1560–1571.

[18] C.M. Lewis and J.M. Hammer, Significance testing of rules in rule-based models of human problem solving. IEEE Transactions on Systems, Man, and Cybernetics, vol SMC-16, no. 1 (1986) 154–157.

[19] Mason, The technical blow-by-blow (the accident that shouldn't have happened) IEEE Spectrum (1979) 33–42.

[20] R.S. Michalski, Synthesis of optimal and quasi-optimal

variable valued logic formulas. Proceedings of the 1975 International Symposium on Multiple-Valued Logic, Bloomington, IN (1975) 76–87.

[21] N.M. Morris, Human problem solving in process control (Report No. 83–2) ISYE, Georgia Institute of Technology Atlanta, GA (1983).

[22] N.M. Morris and W.B. Rouse, The effects of type of knowledge upon human problem solving in a process control task. IEEE Transactions on Systems, Man, and Cybernetics (1985) 698–707.

[23] N.M. Morris, W.B. Rouse and J.L. Fath, PLANT: An experimental task for the study of human problem solving in process control. IEEE Transactions on Systems, Man, and Cybernetics 14 (1985) 792–798.

[24] E. Palmer, Conflict resolution maneuvers during near-miss encounters with cockpit traffic displays, Proceedings of the Human Factors Society-27th Annual Meeting, Human Factors Society, Santa Monica, CA (1983) 757–761.

[25] E. Palmer, S. Jago and M. DuBord, Horizontal conflict maneuvers with a cockpit display of traffic information, Proceedings of the Seventeenth Annual Conference on Manual Control, UCLA, Los Angeles, CA (1981).

[26] E. Palmer, S. Jago, D. Baty and S. O'Conner, Perception of horizontal aircraft separation. On a cockpit display of traffic information, Human factors 22 (1980) 605–620.

[27] A.S. Reber, Implicit learning and tacit knowledge. Journal of Experimental Psychology: General, 118:3 (1989) 219–235.

[28] W.B. Rouse, J.M. Hammer and C.M. Lewis, Algorithmic approaches to knowledge engineering, IEEE Transactions on Systems, Man, and Cybernetics 19 (1989) 558–573.

[29] S. Sattath and A. Tversky, Additive similarity trees. Psychometrika 42 (1979) 319–345.

[30] J.D. Smith, S.R. Ellis and C.E. Lee, Perceived threat and avoidance maneuvers in response to cockpit traffic displays, Human Factors 26 (1984) 33–48.

[31] S. Taylor, Is integrated net management possible? TPT/Networking Management (Jan, (1989) 45–50.

[32] K. VanLehn and S. Garlick, Cirrus: An automated protocol analysis tool. Proceedings of the Fourth International Workshop on Machine Learning, Irvine, CA (1987) 205-217.
