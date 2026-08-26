---
otero_id: 26663
otero_key: "UGJPQCKF"
title: "Role of Control in the Model Formulation Process"
authors: "Arun Sen; Ajay Vinze; Shue Feng T. Liou"
year: "1994"
journal: "Information Systems Research"
doi: "10.1287/isre.5.3.219"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.255.6.125] On: 30 September 2016, At: 18:09 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/UGJPQCKF/fulltext/images/0d5197f16a4e73051ee5cac78be3494065f3e9aaeae49841c50a34dbeba20e31.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Role of Control in the Model Formulation Process

Arun Sen, Ajay Vinze, Shue Feng T. Liou,

## To cite this article:

Arun Sen, Ajay Vinze, Shue Feng T. Liou, (1994) Role of Control in the Model Formulation Process. Information Systems Research 5(3):219-248. http://dx.doi.org/10.1287/isre.5.3.219

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1994 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/UGJPQCKF/fulltext/images/8d0d51d2897178047f725445b1c97f9b0730abeceb1d69555e62872823dc5691.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Role of Control in the Model Formulation Process

<table><tr><td>Arun Sen</td><td>Department of Business Analysis and ResearchCBA/GSBTexas A&amp;M UniversityCollege Station, Texas 77843-4217</td></tr><tr><td>Ajay Vinze</td><td>Department of Business Analysis and ResearchCBA/GSBTexas A&amp;M UniversityCollege Station, Texas 77843-4217</td></tr><tr><td>Shue Feng T. Liou</td><td>Department of Business Analysis and ResearchCBA/GSBTexas A&amp;M UniversityCollege Station, Texas 77843-4217</td></tr></table>

Control is being increasingly recognized as having a critical role in the automation of the model formulation process. This paper describes an approach to understanding this role of control by observing experts' behavior and studying their verbalizations during the process of formulating models. Control concerns were noted at two levels: strategic and tactical. At the strategic level, control behavior was found to be opportunistic, i.e., the modelers did not follow a prespecified approach. This paper focuses on the tactical level, where the emphasis was on scheduling the tasks used to construct the model (referred to as formulation tasks). The tactical controls were demonstrated by our AEROBA system implementation.

Model management—Formulation control—Model formulation

## 1. Introduction

problem fundamental to all cognitive processes and intelligent systems involves Lmaintenance of control.Control in intelligent systems can be defined as a mechanism used to regulate the reasoning process being addressed. For example, Hayes-Roth (1985) indicates that to address the control problem, any intelligent system must decide, either implicitly or explicitly, what problems it will attempt to solve, what knowledge it will bring to bear, and what problem-solving methods and strategies to apply. Such a system also must determine how to evaluate the final result and when it should divert its attention to selected problems or subproblems.

Concerns about control are important to most programmed actions, simple or complex. Since intelligent systems typically attempt to mimic human problem solvers, it becomes important to understand the role of control in human problem solving. However, this is not always obvious, because it is not typically made explicit by human problem solvers.

In view of the important role that control plays in developing intelligent systems, these questions need to be addressed: what are control decisions for human problem solvers? and how can they be implemented in an intelligent system? In undertaking our study of control concerns, we selected model formulation activities in the managerial domain as our realm. Several researchers have addressed the importance of automatic model formulation (Binbasioglu and Jarke 1986, Bonczek et al. 1981, Dolk and Konsynski 1984, Dutta and Basu 1984, Fedorowicz and Williams 1986, Krishnan 1990, Ma et al. 1989, Murphy and Stohr 1986, Pabo and Suchanek 1986, Raghunathan 1992, Sivasankaran and Jarke 1985, Vinze and Sen 1991). The model formulation process involves developing mathematical abstractions for a real world problem. Formulating such models effectively is generally recognized as a difficult task even by expert modelers (Krishnan 1990). It is our contention that to provide robust support for this activity it is necessary to determine and implement control decision mechanisms. The process of model formulation, then, can be described as having two parts: model construction and formulation control. Model construction focuses on the “structure" component of the model, while formulation control addresses the “process" of constructing the structure.

The aim of automated model formulation systems is to simplify both the construction and control aspects of this process. In this paper, we will focus our efforts on the control concerns of the formulation process. Our discussion illustrates various tactical control strategies which, since they are based on theory, ensure correct model formulation irrespective of domain.

With this as our focus, we first studied the existing control approaches in automated model formulation systems. Next, we studied control-related concerns as they have been addressed in three domains (formulating algebra word problems, designing engineering objects, cognitive theories of problem solving) where the activity can be seen as analogous to model formulation. In §2, we present a framework of control for model formulation systems based on our findings from the related literature. To further enhance our understanding of control decisions made by human problem solvers, we collected verbal data from 9 modelers and report them in §3. Protocols were extracted from the data and were analyzed to document the control decisions displayed by the selected modelers. Finally, in §4, we develop a knowledge-based system that incorporates the control traits gleaned from the protocol analysis. The system is an illustrative tool to assess the patterns of control strategies and is a good way to simulate them. Concluding remarks are presented in §5.

## 2. A Control Framework for Model Formulation

Although the existing model formulation literature dwells on predefined control strategies (Binbasioglu and Jarke 1986, Bonczek et al. 1981, Dolk and Konsynski 1984, Dutta and Basu 1984, Fedorowicz and Williams 1986, Krishnan 1990, Ma et al, 1989, Murphy and Stohr 1986, Pabo and Suchanek 1986, Raghunathan 1992,

Sivasankaran and Jarke 1985, Vinze and Sen 1991), there is no evidence to suggest that expert modelers actually have used predefined control. Only recently have some studies considered “flexible" control strategies which are categorized as strategic opportunism whereby formulation develops incrementally at various points in the formulation space. Typically, decisions at a given point in the formulation space appear to influence subsequent decisions at both later and earlier points in the temporal sequence and at both higher and lower levels of abstractions (Sen et al. 1992 Vinze et al. 1993). In support of strategic opportunism, Hayes-Roth (1985, p. 252) says:

People do not rely upon pre-determined control programs to guide all of their problem-solving efforts. Instead, they draw upon a repertoire of control knowledge that includes proven control programs and heuristics for dynamically constructing, modifying, and executing control programs during efforts to solve particular domain problems.

Using Simon's (1973) model of problem solving, the process of model formulation is ill-structured because the formulated model cannot be tested to see whether the formulation has been correct unless the model is executed and the results are analyzed; and the formulation space is not defined in a meaningful way to include: (a) all kinds of mathematical structures that the expert modeler has to consider (such as a linear programming model, an integer programming model, a 0–1 integer programming model, nonlinear models, regression, analysis of variance, and forecasting models); (b) all types of application domains (production planning, forecasting, and sales) and their key attributes; (c) all types of problems (transportation, location, allocation, inventory, transhipment, layout, and location-allocation); and (d) varied design styles (like first principles and case based). Formulation of a mathematical model can be described as a guided search through a large, heterogenous, abstract, and interconnected formulation space. This complexity calls for a different approach to model formulation than has been suggested in the literature. We suggest that a better approach recognizes that the formulation acquires a structure slowly, starting from an ill-structured state that can systematically be converted into a well-structured form (Simon 1973).

Given the complexity of the model formulation domain, control concerns are better viewed in more than one layer. We chose two. This division, though arbitrary, allows us to focus on the differing set of concerns each layer entails. At a higher level, which has been labeled the strategic control layer, the focus is on a scheme that governs communication between formulation tasks during the entire formulation episode. At this level, formulation is an assemblage of model components. Therefore. the order in which these tasks are carried out cannot be determined in advance (Muller-Merbach 1979). This kind of flexible sequencing of tasks has also been recommended by Hayes-Roth and Hayes-Roth (1979) in planning errand tasks where the assemblage of planning components is controlled opportunistically

The lower level in the control hierarchy is labeled the tactical control laver. With opportunism as a dominant scheme (the top layer in our framework), modelers use a set of scheduling tactics to help construct different parts of the models. Tactical control, defined as a scheme that directs how the formulation tasks should be scheduled in a formulation episode, plays a very important role in this guidance (Guindon 1990).

TABLE 1  
Controls Observed in Other Areas Related to Formulation

<table><tr><td>Model Formulation Process(Domain/Emphasis)</td><td>Formulation Control Approach Used</td><td>Tactical Control Categories</td><td>Researchers</td></tr><tr><td>Design operations are selected a priori before they are executed (Domain: Designing Engineering Objects/Implemented in Prolog)</td><td>Use of plans</td><td>Formulation Planning</td><td>Gero and Coyne (1987), Kalay et al. (1987)</td></tr><tr><td>An aspect of formulation (Domain: Cognitive Theories of Problem Solving/Conceptual)</td><td>Use of existence of informal decision plans</td><td></td><td>Mintzberg et al. (1976)</td></tr><tr><td>Algebra is created by using earlier examples and methods. Errors occur in the formulation as “buggy variants” of the correct method are used (Domain: Formulating Algebra Word Problem/Cognitive Study)</td><td>Use of stored plans</td><td></td><td>Sleeman (1984)</td></tr><tr><td>Use of stored substantive information to go beyond definitional equations (Domain: Formulating Algebra Word Problem/Cognitive Study)</td><td>Use of stored plans</td><td></td><td>Paige and Simon (1966)</td></tr><tr><td>Employs a specialized goal-driven inferencing called Marple’s Algorithm (Domain: Formulating Algebra Word Problem/Implemented in Prolog)</td><td>Goal driven</td><td>Formulation Goal Setting</td><td>Luger (1981)</td></tr><tr><td>Use of assumption surfacing technique to formulate adversarial problems that are essentially ill-structured (Domain: Cognitive Theories of Problem Solving/Conceptual)</td><td>Assumption based</td><td>Formulation Component Postulating</td><td>Mitroff et al. (1979)</td></tr><tr><td>Assessing the worth of some entity against one’s preferences or external standards (Cognitive Theories of Problem Solving/Conceptual)</td><td>Use of utility assessment and judgement</td><td>Evaluating the Formulation</td><td>Einhorn and Hogarth (1981)</td></tr><tr><td>Original design is decomposed into smaller designs (Domain: Designing Engineering Objects/Conceptual; Implementation in Lisp (Brown and Chandrasekaran 1989))</td><td>Decompose the problem into subproblems</td><td>Problem Decomposition</td><td>Simon (1973), Brown and Chandrasekaran (1989), Maher (1990)</td></tr><tr><td>Formulation can be done by analyzing the “mess” to find its parts (Domain: Cognitive Theories of Problem Solving/Conceptual)</td><td>Decompose the problem</td><td></td><td>Ackoff (1979, 1981), MacCrimmon and Taylor (1976)</td></tr><tr><td>A complex problem can be broken into a set of “fundamental” problem types (Domain: Cognitive Theories of Problem Solving/Conceptual)</td><td>Decompose the problem</td><td></td><td>Smith (1988)</td></tr><tr><td>An aspect of formulation (Domain: Cognitive Theories of Problem Solving/Conceptual)</td><td>Focus on “what is or what is not part of the problem”</td><td>Problem Boundary Determination</td><td>MacCrimmon and Taylor (1976)</td></tr><tr><td>Algebra is created by detailed calculation of the expression, evaluating it by applying algebra rules, and finally by using approximate evaluation (Domain: Formulating Algebra Word Problem/Cognitive Study)</td><td>Determining the referential meaning of algebra</td><td></td><td>Resnick et al. (1987)</td></tr><tr><td>An aspect of formulation (Domain: Cognitive Theories of Problem Solving/Conceptual)</td><td>Undo, switch, and modify the existing plans</td><td>Problem Replanning</td><td>Mintzberg et al. (1976)</td></tr><tr><td>A basic technique for the problem solver is the direction of search (Domain: Cognitive Theories of Problem Solving/Conceptual)</td><td>Work forward and backward</td><td>Reasoning Direction</td><td>MacCrimmon and Taylor (1976)</td></tr></table>

Rule of Control in the Model Formulation Process

<table><tr><td colspan="4">TABLE 1 (cont&#x27;d)</td></tr><tr><td>Model Formulation Process(Domain/Emphasis)</td><td>Formulation Control Approach Used</td><td>Tactical Control Categories</td><td>Researchers</td></tr><tr><td>An aspect of formulation (Domain: Cognitive Theories of Problem Solving/Conceptual)</td><td>Focus on specific aspects</td><td>Formulation Component Focusing</td><td>MacCrimmon and Taylor (1976), Hansmann (1974)</td></tr><tr><td>Use of direct cues including tagging, substitution, decomposition, and transformation (Domain: Formulating Algebra Word Problem/Cognitive Study)</td><td>Sequentially focus each step of formulation</td><td></td><td>Paige and Simon (1966)</td></tr><tr><td>Progressively transforms a Physics problem description using steps: parsing, conversion to internal form, creation of physical model, and creation of geometrical model to its algebraic form (Domain: Formulating Algebra Word Problem/Implemented in Lisp)</td><td>Sequentially focus each step of formulation</td><td></td><td>Novak (1977, 1982)</td></tr><tr><td>Design is looked at as a sequential process of successive refinement (Domain: Designing Engineering Objects/Implemented in Prolog and C(Han et al. 1987); Conceptual (Takeda et al. 1990))</td><td>Sequentially focus each step of formulation</td><td></td><td>Han et al. (1987), Takeda al. (1990)</td></tr></table>

The elements of tactical control assembled from a review of related literature are shown in Table 1, The attempt here is not to present a comprehensive set of tactical control strategies, but rather to identify a set that would cover the common concerns of model formulation. Given that one of the goals of model formulation is to create an algebraic formula from a word description of the problem situation, the literature reviewed focused on prior works that indicated similar activity. We now describe each of the tactical controls in some detail.

The formulation planning (fpl) control describes potential action sequences that the expert modeler intends to take in a formulation process (Gero and Coyne 1987, Kalay 1987, Mintzberg et al. 1976, Paige and Simon 1966, Resnick et al. 1987 Sleeman 1984). This scheme, probably the most widely used cognitive scheme in formulation, focuses on considering the consequences of actions prior to executing those actions. The evidence of widespread use of planning can be seen in algebra word problem formulations, in engineering design problems, and in the cognitive theory of problem solving. In a few of his case studies, Mintzberg et al. (1976) have seen that an “explicit reference is made to decision planning or to the existence of informal decision plans . . ." (Mintzberg et al. 1976, p. 261).

The formulation goal setting (fgs) control assigns tentative goals and subgoals to be pursued during the formulation process and allows the expert modeler to change his or her formulation goals depending on where he or she is in the formulation space (Luger 1981).

The formulation component postulating (fcp) control describes assumptions made during formulation in order to guess other factors not explicit in the problem (Mitroff et al. 1979). It is used when the expert modeler, while formulating the model, makes some kind of assumption about the problem that is not explicit in the problem description. This is called default assumption. The ability to make appropriate default assumptions is one of the most important cognitive traits in humans. Apart from default assumptions, expert modelers can make erroneous assumptions. Fortunately, expert modelers usually recognize mistaken assumptions some time later in the formulation process and “retract" them.

The evaluating the formulation (etf) control makes a judgement about partial formulations. During a formulation process, partial formulations need to be evaluated periodically to make sure that the formulation is proceeding on schedule and on track. It is assumed that a human being does, and should, make decisions by jointly considering his or her expectations as to ultimate decision outcomes and his or her valuation of those outcomes (Einhorn and Hogarth 1981)

The problem decomposition (pdc) control divides a problem into its components or into subproblems (Ackoff 1979, 1981; Brown and Chandrasekaran 1989, MacCrimmon and Taylor 1976, Maher 1990, Simon 1973, Smith 1988). Factoring the problem into subproblems, which in turn can also be factored, is a very common scheme for resolving a wide range of problems. This scheme is used in a number of design (or construction) problems. Breaking up a problem into subproblems is useful only if “there are not too many interrelationships among the subparts, otherwise the coordination problems would clearly outweigh the advantage of decompositions"(Mac-Crimmon and Taylor 1976, p. 1418). Once each subproblem is formulated, the formulations are then recomposed to arrive at the formulation of the original problem.

The problem boundary determination (pbd) control limits the problem space and puts a bound on the formulation attributes being considered. In order to reduce the complexity of a problem, it is necessary to focus on “what is or is not part of the problem" (MacCrimmon and Taylor 1976, p. 1417). The expert modeler determines the characteristics of the out-of-bounds and in-bounds parts of the problem by studying the functions in which the problem lies, by reexamining the problem text to clarify the boundaries, or by analyzing the assumptions underlying the problem.

The formulation replanning (frp) control (Kaebling 1990) switches plans, modifies existing plans, or suspends the current plan and resumes a suspended plan. Decision plans, according to Mintzberg, “typically appear to be informal and flexible, modified and clarified as the decision progresses" (Mintzberg et al. 1976, p. 261).

The formulation component focusing (fcf) control concentrates the formulation knowledge on a specific component of the model (Han et al. 1987, Hansmann 1974, MacCrimmon and Taylor 1976, Novak 1977, 1982; Paige and Simon 1966, Takeda et al. 1990). It is fair to assume that expert modelers concentrate on a single specific aspect of formulation at one time. The focus is changed by the use of strategic opportunism control.

The reasoning direction (rdr) còntrol describes the direction of reasoning that the expert modeler intends to take. The direction of reasoning has been described in almost all expert systems and AI textbooks and does not need elaboration here. The expert modeler has to reason either forward, backward, or in both directions during the course of the formulation process (MacCrimmon and Taylor 1976).

Tactical controls do not actually construct models. Rather, they are used by modelers to schedule the appropriate formulation tasks. It should be noted thát tactical controls as described above are not formulation tasks, i.e., tasks that actually contribute toward model construction. The relationship between tactical control tasks and formulation tasks may be described as a situation wherein the expert modeler may follow the “problem decomposition" control that may schedule any specific formulation task.

## 3. Evidence of Control in Formulation by Expert Modelers

In an attempt to validate our understanding of control, an exploratory study was conducted using a think-aloud technique for data gathering. The study focused on expert modelers and their thought processes as they attempted to formulate models. Researchers studying cognitive processes (Ericsson and Simon 1984) have successfully used the think-aloud technique for a variety of tasks (Bouwman 1983, 1984; Guindon 1990; Schweiger et al. 1985). Verbal behavior is a “type of recordable behavior" and as such can be collected and analyzed.

## 3.1. Empirical Investigation

The experiment was conducted using nine experienced modelers chosen to represent the selected domains: Production Planning, Forecasting, and Auditing. The selection of subjects was based on peer recommendations. Eight of these subjects were professors with degrees of experience ranging from one to fifteen years. One of the subjects in the Auditing field was a practicing professional. Each of the subjects had a Ph.D. degree in the area of specialization.

We recognize that the relatively small number of subjects decreases the power of statistical comparison as well as the generalizability of the results. The results were, however, still deemed useful, based on precedents (Adelson 1981; Bouwman 1983, 1984; Simon 1973) where the number of subjects was as equal or smaller. The primary reason for using only a few subjects in protocol analysis studies is the high cost in transcribing and coding the protocols.

After being introduced to some initial warmup problems, the subjects were given the problems for this experiment. As was done during the warmup exercises, an audio tape recorder was turned on to record the subjects’ verbalizations as they analyzed and formulated the problems assigned to them. At a later time, the recordings were transcribed and the transcripts analyzed using protocol analysis. Prior to the exercise, the solutions to the problems used in this setup were verified by modelers as being appropriate and correct. Subsequent to the completion of the task, the subjects outputs were verified for correctness and completeness. Each of the participants produced acceptable solutions, which eliminated possible effects of inaccuracy.

The experimental setup provided a total of 27 verbalizations (observations). The task assigned to the subjects was generically defined as model formulation. More specifically, the subjects were asked to formulate the problem based on a textual description of the problem rather than to attempt to solve the problem. Using the encoding procedures defined by Ericsson and Simon (1984), we obtained a set of protocols for each of the 27 verbalizations. A complete set of protocols used by one expert for the problem (Appendix 1) is presented in Appendix 2.2

## 3.2. Analysis of the Protocols

Based on our two-layer model, the protocols were analyzed for each type of control, “strategic and tactical." As formulation controł is of two types, the protocols obtained from the above experiment were analyzed for each type. A detailed analysis of the protocols relating to strategic opportunism can be found in Vinze et al. (1993) and will not be repeated. Instead, the focus here will be on observing the tactical controls revealed in the expert's verbalizations.

Observing Tactical Controls. To demonstrate the role of tactical formulation controls in expert verbalization, we present an analysis of the protocols for one specific case using the protocols obtained from an expert modeler. Tactical controls are the mental leaps (Hayes-Roth and Hayes-Roth 1979) that subjects make in formulating a model. In our context of protocol analysis, tactical controls are therefore indications of the intentions of an expert modeler and are implicit rather than explicit in the protocols. Upon closer examination of the protocols, we were able to document and understand these intentions. In an attempt to extract this evidence of tactical controls in the protocols, we performed the following protocol analysis steps:

(1) The protocols of one problem were studied to determine the labeling rules for all tactical control strategies mentioned above;

(2) Using the labeling rules, we labeled the protocols for all 27 cases to illustrate the modelers' use of tactical controls;

(3) The labeled protocols were analyzed to ascertain the extent of use of tactical controls by the expert modelers for each problem.

Labeling Rules for Tactical Controls. The first rule focuses on the tactical control scheme of formulation planning. In formulation planning, the goal was to capture the planning intentions of an expert modeler to do some formulation task. For example, "So call those things product i" (protocol 4) and “So my first constraints are going to be equal to the constraints for demand" (protocol 12) indicate the modeler's intentions of using these factors at a later part of the formulation process.

RuLE 1. If the protocol shows only the planning intention of the modeler, then label the protocol as formulation planning.

In formulation goal setting, the expert modeler's intention is to set up a goal or a subgoal for the formulation process. For example, "I want the amount shipped" (protocol 32) shows the intention of the modeler to set up the current goal of shipping something. The formulation then concentrates on shipping activities as can be seen in the subsequent protocols.

RuLE 2. If the protocol depicts the modeler's intention of setting a formulation goal or subgoal, then label the protocol as formulation goal setting.

Formulation component postulating is needed as a tactical control in the formulation process since the modeler may not find everything about the problem in the problem description. At this time, he or she intends to make reasonable “default" assumptions. For example, in protocol 81, the expert said, "Don't see how I can do that ifI only have one variable. Restrict the parameter. I don't think I can. Think I'm going to have to add another variable."

RuLE 3. If the protocol shows an intention on the part of the expert modeler to assume something, label the protocol as formulation component postulation.

The formulation is continuously monitored to see whether it is going to fail. This is done through a tactical control called evaluating the formulation. The intention of the expert can be seen in certain protocols in Appendix 2. For example, in protocol 19, the expert had just finished the first scan of the problem description and basically understood it. Therefore, he evaluated his gathered data and said, “And you've got requirements and that's all there is to it."

RuLE 4. If the protocol shows an intention of the expert to evaluate the partial formulation, label the protocol as evaluating the formulation.

In problem decomposition, the decomposition can take place at either the problem level, where the original problem can be decomposed into subproblems, or at the problem component level, where the expert is elaborating the components of the problem to be considered for formulation. For example, in Appendix 2 “Oh yeah breakdown 2 different costs" (protocol 41) shows that the modeler had discovered the need to decompose the shipping cost since the problem shows a tonnage discount.

RuLE 5. If the protocol depicts an intention of the modeler to decompose the problem into several subproblems or to“elaborate" the problem components that will be used in the formulation, the protocol is labeled as decomposition

The problem boundary typically provides the meaning and the essential semantics of the problem. The intention to determine the problem boundary forces the expert modeler to classify the problem or to find the important keyword in the problem. In Appendix 2, "That's the only costs I can see" (protocol 20) depicts an effect of the problem boundary determination control.

RuLE 6. If the protocol depicts an intention to classify a problem or to identify a component of the problem, label the protocol as problem boundary determination

When we find evidence that the expert intends to modify the current plan, we say that the protocol demonstrates formulation replanning. This is fairly obvious and can be seen in several protocols. For example, in protocol 28, “Consumer durables and nondurables . . . food producing . . . I'm going to have to address this a little bit differently here" shows that the modeler's earlier plan of creating constraints for demand based upon regions (protocols 6, 10 and 12) needed to be modified to reflect the fact that region C produces consumer durables and nondurables. The constraints therefore should be based on functions and not regions.

RuLE 7. If the protocol shows evidence of a change in current thinking or plan. label the protocol as formulation replanning.

In reasoning direction, the expert shows the direction of his or her reasoning process. It can be seen in the protocols by noticing the phrases like “so . . . ," “if . . then," "becaușe of," and “the reason for . . ." For example, in protocol 15 “So I have an additional constraint relating those 2 sectors" showed a “work forward" control scheme in use.

RuLE 8. If the protocol shows phrases like"so," “if . . . then," "because of," "the reason for . . ." etc., the intention of the expert is to illustrate the direction of reasoning in the formulation process. This protocol must be labeled as reasoning direction.

Finally, in formulation component focusing the expert modeler concentrates on a particular aspect of formulation. For example, in protocol 41, the expert was focusing on “the cost of that shipping given in that table. The distance is going to be . . ." The corresponding labeling rule would be:

RuLE 9. If the protocol shows an intention or evidence of the expert modeler's focusing on a specific aspect of the formulation process, label the protocol as formulation component focusing.

Using the rules developed above as guidelines, twenty-seven sets of protocols were reanalyzed and labeled. An example of the assigning of these labels to protocols is shown in Appendix 2.

The Extent of Use of Tactical Controls. Once the protocols were labeled, we counted the occurrences of each label, in all 27 cases. Counting the number of labels in each set of protocols is useful since each tactical control demonstrates a specific scheduling philosophy in the model formulation process. The protocol labeling and counting was governed by the rules discussed above. The two encoders had been provided the rules before beginning their task. To get an estimate of coder cohesiveness, an inter-rate of reliability (IRR) was computed for the encoders (Kerlinger 1986, p. 503). The index for IRR was the proportion of agreement divided by the total number of possible pairs (Kerlinger 1986). The overall IRR based on this calculation was 66.4% which, according to Kerlinger (1986, p. 503), indicates a substantial degree of cohesiveness. Some interesting trends were noted:

(1) The variation between the coders was largest in the first problem, indicating that learning the application of the rules was occurring. Recalculating the IRR for only problems 2 and 3 IRR showed an increase from 66.4% to 69.8%.

(2) The major contributor to rater disagreement was the category of fcf rule. The fcf rule requires the coder to recognize the expert's change of focus in the modeling process. By removing the fcf count for purposes of calculating IRR for problem 1, the iRR for this problem increased from an initial score of 60% to 81.1%.

(3) Based on observations (1) and (2) above, we concluded that the two negative contributors to the IRR of 66.4% overall were the low IRR for problem 1 and the overall low IR R for fcf across the three problems. Of these two concerns, fcf effect on lowering the IRR is more pronounced. As a result, we recalculated the combined IRR without fcf for the three problems which resulted in an overall IRR of 71%.

To compare the use of tactical controls by different subjects in formulating different problems, the protocol count data were plotted. One such plot for the production planning domain is provided (Figure 1). Each case has been tagged with an expert/ problem pair, such as pe1/pbl indicating expert 1/problem 1 in Production Planning. A close scrutiny suggests a similarity among expert modelers in their use of the tactical controls.

Observations from the protocol count indicated:

(1) Each modeler used tactical controls whose use differs from domain to domain. The average count of the use of tactical controls (per expert per problem) in production planning is 55.44; in forecasting 48.0; and in auditing, 34.56.

(2) Each modeler in production planning put more emphasis in problem boundary determination, problem decomposition, and formulation component focusing than modelers in the other two areas.

(3) There is more evidence of the use of formulation planning and reasoning direction in production planning and forecasting domains.

![](/api/attachments/UGJPQCKF/fulltext/images/2b3ea4ceb4d432feecad11fa49bf21fa61035a7b72c59403d6c32a72b33720ae.jpg)  
FiGURE 1. Protocol Plots for Production Planning Problems.

From the above observations, it is apparent that tactical controls are important to the formulation process. Relative importance for each of the control strategies varies by the domain. There are also differences in approach for the different modelers in each domain, but these differences are somewhat smaller. Surprisingly, the count for the formulation replanning control is quite low in all three problem areas; before the start of the protocol analysis, we expected it to be high. The low count in this category may suggest the subjects' familiarity with similar problems in textbooks. We cannot strongly argue this one way or the other, since the nature of protocol analysis may introduce an underlying bias in counting.

Nevertheless, these counts demonstrate the existence of tactical controls and their importance to the model formulation process. It also shows that modelers vary in their use of the tactical controls depending on the problem faced (see Figure 1).

## 4. Translating Control Decisions into AEROBA

Having demonstrated how human problem solvers use control decisions in the model formulation process, we next attempted to incorporate these findings into an automated model formulation system called AEROBA (MApping Entity-Relationship Model On Blackboard Architecture). AEROBA was developed to simulate the role of the tactical controls in the model formulation process.

Before implementation would begin, we had to determine the order in which the tactical controls were used by modelers. To analyze this, we built a control graph for each protocol set in which the nodes were the tactical control concerns (Figures 2a-2c). The edges of these graphs show the sequence in which the tactical controls were used, indexed by the protocol numbers. These graphs pictorially demonstrate the opportunistic approach followed by the modelers. As can be seen in Figure 2(a), the modeler initially planned for the formulation (fpl control), as is evidenced in protocols 4 and 6, then switched his attention to fcp control (protocol 7) before returning to fpl control. Attention was next directed to rdr control, and the formulation

Sen · Vinze · Liou

![](/api/attachments/UGJPQCKF/fulltext/images/9b324048245f91fbc7c88e5ae522882662c0d2a1355a9c1b5b3e33d5fde8a223.jpg)  
FIGURE 2a. Control Graph for pe1/pb1.

thereafter progressed in an opportunistic manner. It is interesting to note that for the same problem, the other two modelers did not follow the same control sequence (Figures 2b and 2c). Therefore, the conventional expert system approach of forward or backward chaining would not suffice for supporting a model formulation process.

As a result, the blackboard paradigm was adopted to implement the control-oriented design. This paradigm of problem solving has been used as the approach of choice for opportunistic problem-solving applications such as speech understanding image understanding, signal interpretation, and some planning and design problems (Engelmore and Morgan 1988). The blackboard model has been described (Engelmore and Morgan 1988) as analogous to having a group of specialists gathered around a common workspace, with each specialist being able to read and write to this workspace. The blackboard model is usually described as consisting of three components: knowledge sources, blackboard data structure, and control (Engelmore and Morgan 1988).

Presently, AEROBA can formulate LP type problems from general problem descriptions. The system formulates from its own entity-relationship representation of LP-model types. Input from the users during the formulation session allows specialization and fine tuning of the LP-models. As was noted earlier (§2), in prior efforts at automating model formulation decisions the researchers primarily used a predefined control strategy. This approach was more appropriate to automation paradigms like expert systems and various algorithmic approaches. Based on the findings from the protocol analysis in this study, we felt that the classical expert systems/algorithmic approach would be highly restrictive given the complex nature of the controls used by modelers.

![](/api/attachments/UGJPQCKF/fulltext/images/e585846d52d1b4646d040f88bdd238119a49ed5c832b83aea4b8f97725721b57.jpg)  
FIGURE 2b. Control Graph for pe2/pb1.

AEROBA has been developed in Common Lisp on a Sun 3/160 workstation. This system has been described in detail from a software engineering perspective focusing on blackboard related issues in Vinze et al. (1992). We next focus on how the tactical control concerns extracted from the protocol analysis were incorporated in AER-OBA. A sample session (Appendix 4) with AEROBA, using a procurement problem (Appendix 3) is also presented.

## 4.1. An Overview of AEROBA Implementation

Following the blackboard paradigm described above, the components of AEROBA are knowledge sources (ks's) which are formulation tasks that help in constructing the formulated model; the blackboard data structure for executing the formulation tasks (or knowledge sources); and a control for communication monitoring and scheduling the tasks. The control component here refers to the tactical control concerns.

The formulation tasks in AEROBA have been coded such that each knowledge source has a corresponding formulation task. Knowledge sources are, however, more than just coded forms of the formulation task. Each knowledge source is also equipped with a trigger condition, indicating the conditions under which this knowledge source could make a contribution to the formulation process. Knowledge sources may be considered as experts at-large which monitor the process of

Sen • Vinze • Liou

![](/api/attachments/UGJPQCKF/fulltext/images/d11bb854d2bedb08ea28759ec65dfc2e13493d2c74dba00a62ecd13ff2535914.jpg)  
FIGURE 2c. Control Graph for pb1/pe3.

formulation. Once the conditions are suitable for their participation, knowledge sources indicate to the control mechanism their ability to contribute to the process. The scheduling of such knowledge sources is done using tactical controls. A typical knowledge source for the AEROBA system is shown in Figure 3.

The AEROBA architecture, Figure 4, uses three blackboard panels. The focus of the problem panel is on capturing the problem semantics; the solution panel, on the other hand, is structured to accommodate representations of problem solving tools (for example, linear programming, etc.) The structure of these two panels is based on an E-R representation (Lazimi 1987). The knowledge sources that act on the problem and solution panels are labeled “ks." Each of these “ks" have been given an identification number. A separate label, “cks," is used for knowledge sources acting as the control mechanism for AEROBA. The “cks" can therefore be seen on the control panel of the AEROBA architecture.

In an attempt to deal with tactical control issues explicitly, a separate control panel has been setup in AEROBA. This panel monitors the translation of problem semantics (from the problem panel) to an appropriate tool representation on the solution panel. The knowledge sources described above interact with one another through the medium of a blackboard data structure.

## 4.2. Incorporating Tactical Controls in AEROBA

The control panel approach in AEROBA (Figure 4) allows for the incorporation of the tactical control strategies while maintaining the overall strategic control concern of opportunism in the process of formulation. The levels on the control panel do not follow such ER representations as do domain panels but are instead based on “tactical control" considerations. These levels are: general approach, strategy, policy, focus, trigger-record, chosen-record, event.

<table><tr><td>knowledge-source:</td><td>ks05</td></tr><tr><td>name:</td><td>Create-Problem-Entity-Attribute</td></tr><tr><td>stimulus-level:</td><td>P-Entity</td></tr><tr><td>response-level:</td><td>P-Attribute</td></tr><tr><td>rule0501:</td><td>If there is an entity type SUPPLY-LOCATION but no entity type PRODUCT, then add the attribute solution elements SL.NAME, SL.CAP, SL.TOT.SH.QTY and create an associated event.</td></tr><tr><td>rule0502:</td><td>If there is an entity type DEMAND-LOCATION but no entity type PRODUCT, then add the attribute solution elements DL.NAME, DL.REQ, DL.TOT.SH.QTY, and create an associated event.</td></tr><tr><td>rule0503:</td><td>If there is a problem feature (ACTIVITY PROCUREMENT), an entity type SUPPLY-LOCATION, but no entity type PRODUCT, then add several attribute solution elements such as SL.PUR.QTY, SL.PUR.COST, SL.STOCK, SL.TOT.COST, and create an associated event.</td></tr><tr><td>and others</td><td></td></tr></table>

FIGURE 3. A Typical Formulation Knowledge Source.

At the general approach level, decisions are made on whether the current problem is analogous to a problem previously attempted. In the current implementation, prior situations of solving similar cases are not retained in the memory, so each problem attempted by AEROBA is treated as a new problem. The approach to formulation is, therefore, based on “first principles." However, the inclusion of this level in the current implementation was based on some observations from the protocols that indicated situations where modelers equated the present problem to a prior experience and attempted formulation using a case-based approach. Incorporation of the case-based approach to model formulation is seen as a future extension to AEROBA.

The next level of the control panel, strategy, is based on the tactical control feature identified in the earlier section. At this level, the focus of AEROBA is on a subset of the tactical controls such as problem boundary determination, problem decomposition, formulation goal setting, formulation planning, or formulation replanning. It should be noted that each tactical control can potentially involve one or more formulation tasks. The control knowledge sources (such as cks05 in Figure 5) schedule the formulation knowledge sources (ks) which are classified using the tactical control strategies. Problem boundary determination has corresponding formulation knowledge sources ks00, ks01, and ks02.

The policy level on the control panel is activated by the reasoning policy control at the strategy level. There are different categories of reasoning policies available for AEROBA. They are "general-policy," "forward-chaining," “backward-chaining," “knowledge-source-policy," and “rule-policy." These policies are general governing principles for formulation using the blackboard paradigm. For example, a “generalpolicy" used in AEROBA is that a rule may not have multiple firings, i.e., if a rule is used at any time during the execution cycle, it is then flagged out of future contention. An example of the "knowledge-source-policy" is to respond-to-highest-level which enables the system to select a knowledge source that responds to the highest blackboard level. Another policy could be respond-to-lowest-level. An example of the “rule-policy" is to use a rule with-highest-score. Policy decisions remain operative unless they are changed by dynamic formulation situations.

![](/api/attachments/UGJPQCKF/fulltext/images/ba09c1ea7f8c0ead0b9a070d145aa713826d4ce614fd119f59baeb3782f847fc.jpg)  
FIGURE 4. The AEROBA Architecture.

The notion of the formulation component focusing control is implemented through the focus, trigger-record, and chosen-record levels of the control panel. The focus level on the control panel indicates the set of knowledge sources that have been identified as potential contributors to the formulation process. The trigger-record decisions identify all pending knowledge sources, while chosen-record level stores the decisions that identify the knowledge source being scheduled for execution.

![](/api/attachments/UGJPQCKF/fulltext/images/58da231463dc9ac4dc959a176e7097dce07506ea70b0148cb4d289191edcfe42.jpg)  
FIGURE 5. Sample Control Knowledge Source Structures

The intention in AEROBA implementation was not to capture the knowledge of a specific expert and his or her idiosyncracies. Rather, a summarized version of their collective knowledge was encoded. Table 2 shows how the eight control concerns observed from the protocols were incorporated into the AEROBA implementation. Although the formulation process used by AEROBA is not identical to that of a specific expert modeler (in this case expert pe1), the comparison demonstrates that the process used similar criteria to proceed with the formulation. A session with AEROBA is included in Appendix 4. This session shows a partial trace of the control features. The purpose of this trace is to show that AEROBA demonstrates the use of tactical control strategies, an opportunistic sequencing of the control strategies, and interaction with the user as the formulation progresses. The details of AEROBA cycles such as 11-14, 16-21, 23-28 and 30-205 have been suppressed to reduce repetition of the process shown in earlier cycles.

## 5. Conclusions

The problem of control has been studied in a variety of disciplines. In this paper we have developed a framework to study control concerns in the context of model formulation activities. The proposed two-layer framework, strategic and tactical, illustrates differing concerns surrounding control in model formulation. The primary issue for strategic control is the role of opportunism in the process of formulation. Tactical control, on the other hand, addresses scheduling issues for tasks needed to accomplish the formulation. The use of protocol analysis in this study gives further credence to the control concerns identified. Once the issues of control were identified and appropriately classified, they were used in an attempt to automate the process of model formulation. The AEROBA system incorporates the control issues into a blackboard architecture. The utility of the framework is confirmed by demonstrating that the system exhibits dynamic control behavior at both the strategic and the tactical levels, much like an expert modeler.

The emphasis on control presented here and the architecture that flows from it should be useful in designing flexible control-oriented model formulation systems in the future. We think that future efforts in model formulation may extend this work to address large formulation problems that include planning, replanning, and the concerns of reason maintenance. Formulation planning and replanning will become increasingly important parts of tactical control schemes as the control systems become more sophisticated. However, unlike classical planning, most formulation planning seems to be partial, requiring the planner to continually monitor any changes in the formulation process in user inputs and formulated variables that can cause the planner to abandon the current plan. In such cases, the aim may be to salvage parts of the existing plan and go into replanning. We have seen in our protocol analysis some evidence that modelers are concerned about these developments.\*

Sen • Vinze • Liou  
TABLE 2  
Evidencing Tactical Controls in AEROBA Implementation

<table><tr><td>Control Features in the Formulation Process</td><td>Function and Evidence of Control Features from Expert Protocols</td><td>Function of Control Knowledge Sources from AEROBA Execution</td></tr><tr><td>Problem Boundary Determination (pbd)</td><td>categorize explicit problem (none in PE1, Problem 1) and elicit incremental problem (protocols 20, 27, 38, 89, 112)</td><td>activate the selected domain, determine a problem type in the domain, and trace the problem elicitation tree for the problem type</td></tr><tr><td>Problem Decomposition (pdc)</td><td>elaborate problem components (protocols 42, 48)</td><td>activate the entity type and relationship type for the problem</td></tr><tr><td>Formulation Goal Setting (fgs)</td><td>specify tentative goal (protocols 32, 39)</td><td>activate the EER components of the selected tool type</td></tr><tr><td>Formulation Planning (fpl)</td><td>delineate intended actions (protocols 4, 6, 8, 12, 49, 55, 64, 71, 76, 79, 82, 85, 93, 105, 110)</td><td>activate the problem attribute and develop key attributes for solution</td></tr><tr><td>Formulation Replanning (frp)</td><td>switch or modify the plan (protocols 28, 33, 45, 83, 116)</td><td>insert or modify the strategic plan based on some formulation events</td></tr><tr><td>Formulation Component Focusing (fcf)</td><td>concentrate on a specific target (protocols 41, 56, 63, 66, 86, 97)</td><td>initiate, suspend, resume, or interrupt a focus of attention</td></tr><tr><td>Formulation Component Postulating (fcp)</td><td>estimate environmental factors (protocols 7, 43, 81, 87)</td><td>not addressed in the current implementation</td></tr><tr><td>Reasoning Direction (rdr)</td><td>infer actions to be taken (protocols 15, 16, 31, 85, 119)</td><td>adopt different reasoning policy like planning or bookkeeping</td></tr><tr><td>Evaluating the Formulation (etf)</td><td>make a judgement for actions to be taken (protocols 19, 21, 35, 62, 78, 92, 95, 96, 111, 120)</td><td>evaluate active events to decide whether to modify the strategic plan, interrupt the current focus, or do nothing</td></tr></table>

Acknowledgements. The authors would like to acknowledge the assistance of the graduate students of the Spring 1989 Decision Support Systems class in capturing the protocols. Detailed comments from three anonymous referees and the associate editor were most helpful in clarifying the contents of the paper and making it more readable.

\* Robert W. Blanning, Associate Editor. This paper was received on February 10, 1992, and has been with the authors 7 months for 3 revisions.

Appendix 1: A Multiproduct Transportation Problem Appendix 1: A M

An imaginary economy has six distinct geographical locations each having its own specific economic functions, as follows:

<table><tr><td>Region</td><td>Function</td></tr><tr><td>A</td><td>Food Producing</td></tr><tr><td>B</td><td>Manufacturing-Machinery</td></tr><tr><td>C</td><td>Manufacturing-Machinery and consumer durables</td></tr><tr><td>D</td><td>Administrative</td></tr><tr><td>E</td><td>Food-Producing</td></tr><tr><td>F</td><td>Manufacturing-Consumer durables and nondurables</td></tr></table>

The regions also have the following annual requirements (all quantities measured in tons):

<table><tr><td>Region</td><td>Food</td><td>Machinery</td><td>Consumer durables</td><td>Consumer nondurables</td></tr><tr><td>A</td><td>5</td><td>30</td><td>20</td><td>10</td></tr><tr><td>B</td><td>15</td><td>100</td><td>40</td><td>30</td></tr><tr><td>C</td><td>20</td><td>80</td><td>50</td><td>40</td></tr><tr><td>D</td><td>30</td><td>10</td><td>70</td><td>60</td></tr><tr><td>E</td><td>10</td><td>60</td><td>80</td><td>20</td></tr><tr><td>F</td><td>25</td><td>60</td><td>60</td><td>50</td></tr></table>

Using the national railroad; shipping costs are \$1/ton per 100 miles for all hauls over 100 miles. Within 100 miles, all goods are carried by truck at a cost of\$1.25/ton per 100 miles (\$1/ton minimum charge), The distances (in miles) between regions are as follows:

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td></tr><tr><td>A</td><td>—</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B</td><td>500</td><td>—</td><td></td><td></td><td></td><td></td></tr><tr><td>C</td><td>200</td><td>400</td><td>—</td><td></td><td></td><td></td></tr><tr><td>D</td><td>75</td><td>500</td><td>150</td><td>—</td><td></td><td></td></tr><tr><td>E</td><td>600</td><td>125</td><td>350</td><td>550</td><td>—</td><td></td></tr><tr><td>F</td><td>300</td><td>200</td><td>100</td><td>400</td><td>300</td><td>—</td></tr></table>

Assume producing regions can meet all requirements but that, due to government regulation, food production in sector A is restricted to half that of sector E.

Formulate a linear program that will meet the requirements and minimize the total transportation costs in the economy.

Appendix 2: A Complete Verbalization of the Problem in Appendix 1 for Expert PE1

1. Imaginary economy. 6 distinct geographical locations.

2. We've got 6 regions and they all do one thing.

3. The regions also have the following annual requirements. Food, machinery, consumer durables. consumer nondurables.

4. So call those things products i. (fpl)

5. Using the national . . .

6. Call the regions k for now. (fpl)

7. Using the national railroad, shipping costs are 1 ton per 100 miles for all hauls over 100 miles. Within a 100 miles, all goods are carried by truck at a higher cost per 100 miles. One dollar per ton minimum charge. I have no idea what that means. Goods are carried by truck at a cost of a dollar 25 per ton per 100 miles. Dollar per ton minimum charge. Apparently they're getting lower rates over longer distances. I don't know. Distances in miles between regions are given. (fcp)

8. The cost is gonna be a function of the weight with a cut off point of 100 miles, (fpl)

9. 0 to 100 and then within a hundred goods are carried by truck. For hauls over, I'll assume that's greater. 101 or whatever. Greater than a hundred.

10. Assume producing regions can meet all requirements.

11. So demand is met.

12. So my first constraints are going to be equal to the constraints for demand. (fpl)

13. And all demand is met.

14. But due to government regulation, food production is sector A is restricted to half that of sector E.

15. So I have an additional constraint relating those 2 sectors. (rdr)

16. So food was one of items so for i = 1, I'm going to hwe another unique restriction. (rdr)

17. Formulate this as an LP.

19 And vou've got requirements and that's all there is to it. (etf)

20. That's the only costs I can see (pbd)

21. Subiect to. Ok I've got my demand constraints. (etf)

25. Go back up to each region only one does one thing.

27. C does more than one thing. (pbd)

28. Consumer durables and nondurables . . . food producing I'm going to have to address this a little bit differently here. (frp)

31. Regions . . . I could formulated it as a general LP but it's going to really breakdown very quickly because there's not going to be an i of k for each of these things. Pretty restrictive. ok so let's say (rdr)

32. I want the amount shipped (fgs)

33. So its not a function T of annual requirements (frp)

35. That's going to be a very general format because very few k are going to be able to ship function l. Demand is met is the first constraint. That might be it. Using the following annual requirements all demand is met. (etf)

38. The only other restriction is that last one about food production in sector A is half that of sector E. (pbd)

39. Minimize Z is going to be my shipping cost. (fgs)

40. The amount I'm going to ship is X of item i to location k from location l in annual terms.

41. The cost of that shipping given in that table. The distance is going to be (fcf)

42. Oh yeah breakdown 2 different costs. (pdc)

43. That's the tricky part of the problem. (fcp)

45 I'l have to think about that for a while. Get down to the constraints. (frp)

48. Subiect to the restriction that I meet the demand for each one of these I functions in each region, (pdc)

49. X function I region k (fpl)

53. That's the amount of function I shipped to location k from location I

54. I could be = to k.

55. The sum of all that sums over I and should = the demand of function I at location k. (fpl)

56. I'll go to the last constraint. Due to government regulation, food production in sector A is half that of sector E. (fcf)

62. We have X i shipped to location k from / (etf)

63. What I'm concerned with here is location /. (fcf)

64. So I'm going to sum over k. (fpl)

66. And I'm only concerned with these 2 specific ones. (fcf)

67. That's the parameter or variable I want.

71. Food production sector A which / = 1 is restricted to half that of sector E. (fpl)

76. Going to have 2 different costs. (fpl)

78. For some reason, I'm having a tough time remembering how to do that. Less than 100. Some type of restriction. 100 miles. Have to have 2 variables that I can. Going to have to restrict the one variable greater than 100. I got xikl. (etf)

79. I'm going to add to that another variable and restrict xik/ to greater than or equal to 100. Any other one I'll estimate to be = to 100 I guess. I'll have to also include that variable on the other restriction. (fpl)

81. Don't see how I can do that if I only have one variable. Restrict the parameter. I don't think I can. Think I'm going to have to add another variable. (fcp)

82. Fach of those variables to have a different transportation problem. (fpl)

83. Let me modify this. (frp)

85. Come back to that. Subject to I'm gonna have two variables. Gonna have the sum over Ix function I to location k from location I plus the sum over l of y. The sum of those is = to my demand function I at location k. This thing's really going to break down quickly because the combinations of i and k are very limited and /in addition. Then I have something like xikl. That tells me the amount shipped of function I . . . See if these cost (fpl, rdr)

86. Shipping cost . . . (fcf)

87. If shipping cost is given per time, I assume we must be summing all the functions. I guess. (fcp)

89. There's no restriction here on distance. (pbd)

92. So if I just had a distance variable, I would have been alright (etf)

93. I'll add in a capital D which is the distance between per ton per 100 miles (fpl)

95. I see something that makes the problem very easy that I didn't see before. All vou gotta do is look at the distances. There's only one distance on there under 100 miles. So that's the only one that I won't have that shipping cost. So I see. Go back to my original formulation. (etf)

96. That makes it real simple. I was thinking too general. (etf)

97. The cost is just going to be a dollar per ton. (fcf)

105. Gonna have 3 summations in here. (fpl)

110. Add to that another summation for everything else but that linkage. (fpl

1 11. k is gonna be an element of K and / is going to be and element of o 3 capital L. And I'll say capital K = the set of all other combinations. Ok A to B. I'm getting stuck on wording here. I'll say k and / of Z and Z is a set of all the other combinations. Except for the 2 that I just broke out. I'm cheating here. I don't want to go through all of them. (etf)

112. I got the restriction for govt regulation on food production. (pbd)

116. It was all the same transportation costs except the 1 exception. (frp)

119. I'll assume that's all hauls equal to or more than a hundred miles so that I only haye 1 exception. (rdr)

120. So it wasn't as hard a problem as I made it originally. (etf)

## Appendix 3: An Example Procurement Problem

A store chain has an order for 70 display terminals at location D1 and 40 at location D2. It has 2 stores S1 and S2, from which it may ship terminals at costs given below.

<table><tr><td>Shipping Route</td><td>Unit Shipping Cost</td></tr><tr><td>S1-D1</td><td>$20</td></tr><tr><td>S1-D2</td><td>$25</td></tr><tr><td>S2-D1</td><td>$50</td></tr><tr><td>S2-D2</td><td>$55</td></tr></table>

Unfortunately, neither store has sufficient stock to supply the order. Thus more terminals must be purchased. The chain has \$15,000 available for buying new terminals. Each store can buy terminals at cost that varies due to differing distances of the stores from the suppliers, and newly bought units must be shipped to D1 and D2 as needed. Each store buys terminals at a different price. The number of terminals in stock and the cost of buying more terminals are listed in the following table.

<table><tr><td>Store Site Name</td><td>Purchase Price/unit</td><td>Stock Amount</td></tr><tr><td>S1</td><td>$400</td><td>50</td></tr><tr><td>S2</td><td>$350</td><td>20</td></tr></table>

Due to the limit of the truck load, no more than 65 and 45 terminals can be purchased at stores S1 and S2, respectively. Determine how many terminals must be bought by each store and how many should be shipped from each store to each destination in order to minimize the total expense to the chain.

## Appendix 4: An AEROBA Session with Trace of Control Features

The session shows the partial trace of control features. The questions asked by the system are shown by the AEROBA> prompts. The system asks for the user's input by displaying the USER-RESPONSE> prompt. Typical user sessions with the system have system generated information suppressed, as users are not expected to be “blackboard experts." As a result, user sessions with AEROBA show up as AEROBA> and USER-RESPONSE>. To demonstrate the intricacies of the blackboard and the role of control features, we have turned on the blackboard control trace feature of the system. This provides information on the controì panel state for each cycle. These show up in the trace in small font.

The messages, tactical controls, and other prompts by the system, including the session result, i.e., the formulated model, are shown in italics. We have tagged on our explanation for the goings-on in the system in bold.

>(load “aeroba”)

USER-RESPONSE> (FORMULATE)

AEROBA> Which problem area are you working on? Please answer one area name such as PROD-PLAN. AUDITING, or FORECASTING?

Please note the current version of AEROBA only addresses production planning problems

USER-RESPONSE> PRODPLAN

cycle-number 0, Formulation-Component-Focusing

AEROBA starts the formulation process by first focusing on the Problem-Boundary-Determination control task.

cycle-number 1, Problem-Boundary-Determination cycle-number 1, Evaluating-the-Formulation

Trace of execution cycle begins . . .

```ini
cycle-number = 1
triggered-kss = (ks01)
selected-ks = ks01
triggered-rules = (RULE0101)
selected-rule = RULE0101
mission accomplished: (SET THE DOMAIN NAME)
strategic-plan = (Problem-Decomposition Formulation-Goal-Setting Formulation-Planning Problem-Boundary-Determination)
suspended-foci = NIL
focus = (ks01ks02)
interrupted-focus = NIL
interrupted-rs-policy = NIL
reasoning-policy = DESIGNING
resumed? = NIL
event-list = NIL
```

In cycle-number 1, the initial focus is set to ks01 and ks02 (ks refers to formulation knowledge source, refer to Figure 3) which emphasize the tactical control features called the problem boundary determination.

AEROBA> Is this problem related to transforming goods (answer TR), or related to allocating personnel or capital (answer AL)?

USER-RESPONSE> TR

AEROBA> Which type of product transformation is involved in your problem (answer PLACE, TIME, or FORM)?

Information Systems Research 5 : 3

```ini
USER-RESPONSE> PLACE
AEROBA> Is yours a single product situation (answer YES or NO)?
USER-RESPONSE> YES
AEROBA> AEROBA classifies the problem type as SINGLE-PRODUCT-TRANSPORTATION-PROBLEM.
AEROBA will now perform various formulation control tasks, such as Problem-Decomposition, Formulation-Goal-Setting, and Formulation-Planning, depending on the current formulation opportunities.
cycle-number 2, Problem-Boundary-Determination
cycle-number 2, Evaluating-the-Formulation
cycle-number = 2
triggered-kss = (ks02)
selected-ks = ks02
triggered-rules = (RULE0201)
selected-rule = RULE0201
mission accomplished: (DETERMINE PROBLEM TYPE IN PRODPLAN DOMAIN)
strategic-plan = (Problem-Decomposition Formulation-Goal-Setting Formulation-Planning Problem-Boundary-Determination)
suspended-foci = NIL
focus = (ks01 ks02)
interrupted-focus = NIL
interrupted-rs-policy = NIL
reasoning-policy = DESIGNING
resumed? = NIL
event-list = NIL
Rule 0101 of ks01 has been executed in cycle-number 1 and is no longer active. Triggered-ks in cycle-number 2 includes on ks02 and triggered-rules include Rule 0201.
cycle-number 3, Formulation-Component-Focusing
cycle-number = 3
triggered-kss = NIL
strategic-plan = (Problem-Decomposition Formulation-Goal-Setting Formulation-Planning Problem-Boundary-Determination)
suspended-foci = NIL
focus = (ks01 ks02)
interrupted-focus = NIL
interrupted-rs-policy = NIL
reasoning-policy = DESIGNING
resumed? = NIL
event-list = NIL
In cycle-number 3, there is no ks triggered and the system cannot make a contribution to the formulation. Given the opportunistic approach to formulation, the system now refocuses on the next most promising task, which in this case is to resume a suspended focus.
cycle-number 4, Formulation-Component-Focusing
cycle-number = 4
triggered-kss = NIL
strategic-plan = (Problem-Decomposition Formulation-Goal-Setting Formulation-Planning Problem-Boundary-Determination)
suspended-foci = NIL
focus = NIL
interrupted-focus = NIL
```

September 1994

```ini
Sen • Vinze • Liou

interrupted-rs-policy = NIL
reasoning-policy = DESIGNING
resumed? = T
event-list = NIL

The system tries to resume a suspended focus, since there is no suspended focus the system cannot still contribute to the formulation. This lack of contribution causes a refocusing of attention to include a new tactical control strategy.

cycle-number 5, Problem-Decomposition
cycle-number 5, Evaluating-the-Formulation

cycle-number = 5
triggered-kss = (ks03)
selected-ks = ks03
triggered-rules = (RULE0301 RULE0302)
selected-rule = RULE0301
mission accomplished: (ADD ENTITY TYPE SUPPLY-LOC FOR SPTP PROBLEM)
strategic-plan = (Formulation-Goal-Setting Formulation-Planning Problem-Boundary-Determination)
suspended-foci = NIL
focus = (ks03 ks04)
interrupted-focus = NIL
interrupted-rs-policy = NIL
reasoning-policy = DESIGNING
resumed? = NIL
event-list = (P-ENTITY)

To get out of deadlock, in cycle-number 5 a new focus “Problem Decomposition” is established. This focus uses ks03 and ks04.

cycle-number 6, Formulation-Component-Focusing

cycle-number = 6
triggered-kss = (ks04)
selected-ks = ks04
triggered-rules = NIL
strategic-plan = (Formulation-Planning Formulation-Goal-Setting Problem-Boundary-Determination)
suspended-foci = NIL
focus = (ks03 ks04)
interrupted-focus = NIL
interrupted-rs-policy = NIL
reasoning-policy = DESIGNING
resumed? = NIL
event-list = NIL

cycle-number 7, Formulation-Component-Focusing

cycle-number = 7
triggered-kss = NIL
strategic-plan = (Formulation-Planning Formulation-Goal-Setting Problem-Boundary-Determination)
suspended-foci = ((ks03 ks04))
focus = (ks03 ks04)
interrupted-focus = NIL
interrupted-rs-policy = NIL
reasoning-policy = DESIGNING
resumed? = T
event-list = NIL
```

Information Systems Research 5 : 3

```txt
cycle-number 8, Formulation-Planning
cycle-number 8, Evaluating-the-Formulation
cycle-number 8, Formulation-Component-Focusing

cycle-number = 8
triggered-kss = (ks05)
selected-ks = ks05
triggered-rules = (RULE0501)
selected-rule = RULE0501
mission accomplished: (ADD SL. NAME SL. CAP SL. TOT.SH. QTY FOR SUPPLY-LOC)
strategic-plan = (Formulation-Goal-Setting Problem-Boundary-Determination)
suspended-foci = ((ks03 ks04))
focus = (ks05 ks06 ks11 ks25)
interrupted-focus = NIL
interrupted-rs-policy = NIL
reasoning-policy = DESIGNING
resumed? = NIL
event-list = (P-KEY P-DATA P-DERIVED)

AEROBA> Please enter all of the data in letters for SUPPLY-LOCATION-NAMES (separated by a space).

USER-RESPONSE> S1 S2

cycle-number 9, Reasoning-Direction
cycle-number 9, Evaluating-the-Formulation
cycle-number 9, Formulation-Component-Focusing

cycle-number = 9
triggered-kss = (ks08 ks09)
selected-ks = ks08)
triggered-rules = (RULE0801)
selected-rule = RULE0801
mission accomplished: (GET VALUES FOR ENTITY KEY ATTRIBUTE)
strategic-plan = (Formulation-Goal-Setting Problem-Boundary-Determination)
suspended-foci = ((ks03 ks04))
focus = (ks08 ks09)
interrupted-focus = (ks05 ks06 ks11 ks25)
interrupted-rs-policy = DESIGNING
reasoning-policy = BOOKKEEPING
resumed? = NIL
event-list = (P-KEY P-DATA P-DERIVED)

Execution cycle suppressed . . .

cycle-number 11, Formulation-Component-Focusing
cycle-number 12, Problem-Decomposition
cycle-number 12, Evaluating-the-Formulation
cycle-number 12, Formulation-Component-Focusing
cycle-number 14, Formulation-Component-Focusing
cycle-number 15, Formulation-Planning
cycle-number 15, Evaluating-the-Formulation
cycle-number 15, Formulation-Component-Focusing

AEROBA> Please enter all of the data in letters for DEMAND-LOCATION-NAMES (separated by a space).
```

## Sen • Vinze · Liou

## USER-RESPONSE> D1 D2

cycle-number 16, Reasoning-Direction

cycle-number 16, Evaluating-the-Formulation

cycle-number 16, Formulation-Component-Focusing

cycle-number 18, Formulation-Component-Focusing

cycle-number 19, Problem-Decomposition

cycle-number 19, Evaluating-the-Formulation

cycle-number 19, Formulation-Component-Focusing

cycle-number 21, Formulation-Component-Focusing

cycle-number 22, Formulation-Planning

cycle-number 22, Evaluating-the-Formulation

cycle-number 22, Formulation-Component-Focusing

AEROBA> Please enter the data in number for DEMAND-LOCATION-REQUIREMENT of D1.

## USER-RESPONSE> 70

AEROBA> Please describe the constraint for DEMAND-LOCATION-REQUIREMENT of D1. Is it a Maximum-Amount (answer MAX), Exact-Amount (answer EXACT), or Minimum-Amount (answer MIN)?

USER-RESPONSE> EXACT

AEROBA> Please enter the data in number for DEMAND-LOCATION-REQUIREMENT of D2.

## USER-RESPONSE> 40

AEROBA> Please describe the constraint for DEMAND-LOCATION-REQUIREMENT of D2. Is it a Maximum-Amount (answer MAX), Exact-Amount (answer EXACT), or Minimum-Amount (answer MIN)?

## USER-RESPONSE> EXACT

cycle-number 23, Reasoning-Direction

cycle-number 23, Evaluating-the-Formulation

cycle-number 23, Formulation-Component-Focusing

cycle-number 25, Formulation-Component-Focusing

cycle-number 26, Formulation-Component-Focusing

cycle-number 27, Formulation-Component-Focusing

cycle-number 28, Formulation-Component-Focusing

cycle-number 29, Formulation-Goal-Setting

cycle-number 29, Evaluating-the-Formulation

cycle-number 29, Formulation-Component-Focusing

AEROBA> Please enter the datum in number for SUPPLY-LOCATION-CAPACITY of S1.

USER-RESPONSE>

AEROBA> Please enter the datum in number for SUPPLY-LOCATION-CAPACITY of S2

USER-RESPONSE>

The above two questions are asked because the standard Entity-Relationship diagram for Single Product Transportation (SPT) problem includes the data attribute SUPPLY-LOCATION-CAPACITY. However this problem is not a standard (SPT) problem and has no supply capacity data. The user just enters <RTN) when the question is not applicable to the problem. The attribute type SUPPLY-LOCATION-ĊAPACITY will be modified once the system recognizes the problem as a variation of the SPT problem.

AEROBA> State an alternate objective if applicable. Please select answer(s) from the list (separated by a space) (PROFIT-MAX TIME-MIN NEITHER).

USER-RESPONSE> neither

AÉROBA> Are there additional activities in the problem? Please select answer(s) from the list (separated by a space) (PROCUREMENT SUPPLY-LOCATION-SELECTION ROUTÈ-SELEC-TION NONE)

USER-RESPONSE> procurement

cycle-number 162, Formulation-Component-Focusing cycle-number 164, Formulation-Component-Focusing cycle-number 165, Evaluating-the-Formulation cycle-number 165, Formulation-Component-Focusing cycle-number 166, Reasoning-Direction cycle-number 166, Evaluating-the-Formulation cycle-number 166, Formulation-Component-Focusing cycle-number 168, Formulation-Component-Focusing cycle-number 170, Formulation-Component-Focusing cycle-number 171, Evaluating-the-Formulation cycle-number 171, Formulation-Component-Focusing cycle-number 172, Reasoning-Direction cycle-number 172, Evaluating-the-Formulation cycle-number 172, Formulation-Component-Focusing cycle-number 174, Formulation-Component-Focusing cycle-number 176, Formulation-Component-Focusing cycle-number 177, Evaluating-the-Formulation cycle-number 177, Formulation-Component-Focusing cycle-number 178, Reasoning-Direction cycle-number 178, Evaluating-the-Formulation cycle-number 178, Formulation-Component-Focusing cycle-number 180, Formulation-Component-Focusing cycle-number 182, Formulation-Component-Focusing cycle-number 183, Evaluating-the-Formulation cycle-number 183, Formulation-Component-Focusing cycle-number 184, Reasoning-Direction cycle-number 184, Evaluating-the-Formulation cycle-number 184, Formulation-Component-Focusing cycle-number 186, Formulation-Component-Focusing cycle-number 188, Formulation-Component-Focusing cycle-number 189, Evaluating-the-Formulation cycle-number 189, Formulation-Component-Focusing cycle-number 190, Reasoning-Direction cycle-number 190, Evaluating-the-Formulation cycle-number 190, Formulation-Component-Focusing cycle-number 192, Formulation-Component-Focusing cycle-number 194, Formulation-Component-Focusing cycle-number 195, Evaluating-the-Formulation cycle-number 195, Formulation-Component-Focusing cycle-number 196, Reasoning-Direction cycle-number 196, Evaluating-the-Formulation cycle-number 196, Formulation-Component-Focusing cycle-number 198, Formulation-Component-Focusing cycle-number 200, Formulation-Component-Focusing cycle-number 201, Evaluating-the-Formulation cycle-number 202, Formulation-Component-Focusing cycle-number 203, Evaluating-the-Formulation

## Sen • Vinze • Liou

```txt
cycle-number 204, Formulation-Component-Focusing
cycle-number 205, Evaluating-the-Formulation
cycle-number 206, Formulation-Component-Focusing

AEROBA> Formulation Completed
The formulation in algebra format for this problem is:

Objective Function:
Minimize Total Cost =
400*(SL.PUR.QTY .S1) + 350*(SL.PUR.QTY .S2) + 20*(SH.QTY S1 D1) + 25*(SH.QTY S1 D2) + 50*(SH.QTY S2 D1) + 55*(SH.QTY S2 D2)

Subjected to:
1*(SH.QTY S1 D1) + 1*(SH.QTY S2 D1) = 70
1*(SH.QTY S1 D2) + 1*(SH.QTY S2 D2) = 40
-1*(SL.PUR.QTY .S1) + 1*(SH.QTY S1 D1) + 1*(SH.QTY S1 D2) = 50
-1*(SL.PUR.QTY .S2) + 1*(SH.QTY S2 D1) + 1*(SH.QTY S2 D2) = 20
400*(SL.PUR.QTY .S1) + 350*(SL.PUR.QTY .S2)<=15000

(SL.PUR.QTY .S1); integer
(SL.PUR.QTY .S1) <= 65
(SL.PUR.QTY .S2); integer
(SL.PUR.QTY .S2) <= 45
(SH.QTY S1 D1); integer
(SH.QTY S1 D2); integer
(SH.QTY S2 D1): integer
(SH.QTY S2 D2): integer
```

## AEROBA> Control statistics for the run:

total cycles = 207

count of Problem-Boundary-Determination = 7 count of Problem-Decomposition = 3 count of Formulation-Goal-Setting = 7 count of Formulation-Planning = 12 count of Formulation-Replanning = 5 count in Reasoning-Direction = 32 count of Formulation-Component-Focusing = 143 count of Evaluating-the-Formulation = 81

## References

Ackoff, R., “Resurrecting the Future of Operational Research," Journal of the Operational Research Society, 30 (1979), 189–199. So

"The Art and Science of Mess Management," Interfaces, 11, 1 (February 1981), 20–26

Adelson, B., “Problem Solving and the Development of Abstract Categories in Programming Languages," Memory and Cognition. 9 (1981), 422–433. Memory ana

Binbasioglu, M. and M. Jarke, “Domain Specific DSS Tools for Knowledge-Based Model Building," Decision Support Systems, 2 (1986), 213–223.

Bonczek, R. H.. C. W. Holsapple and A. B. Whinston, “A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management," Operations Research, 29, 2 (1981), 263- 281.

Bouwman, M., “Human Diagnostic Reasoning by Computer: An Illustration from Financial Analysis," Management Science, 29, 6 (1983), 653–672.

"Expert vs. Novice Decision Making in Accounting: A Summary," Accounting Organizations and Society, 9 (1984), 325–327.

Brown, C. E. and T. G. Lewis, "HELM: Hierarchical Environment for Linear Modeling," Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, 1989, 449–458.

Brown, D. C. and B. Chandrasekaran, Design Problem Solving: Knowledge Structures and Control Strategies, Morgan Kaufman, San Mateo, CA, 1989.

Dhar, V. and H. E. Pople, "Rule-Based versus Structure-Based Models for Explaining and Generating Expert Behavior," Communications of the ACM, 30, 6 (June 1987), 542–555.

Dolk, D. and B. Konsynski, “Knowledge Representation for Model Management Systems," IEEE Trans actions on Software Engineering, SE-10, 6 (November 1984), 1–8.

Dutta, A. and A. Basu, “An Artificial Intelligence Approach to Model Management in Decision Support Systems," IEEE Computer, 17, 9 (September 1984), 89–97.

Einhorn, H. J. and R. M. Hogarth, "Behavioral Decision Theory: Processes of Judgement and Choice." Annual Review of Psychology, 32 (1981), 53–88.

Engelmore, R. and T. Morgan (Eds.), Blackboard Systems, Addison-Wesley, NY, 1988.

Ericsson, K. A. and H. A. Simon, Protocol Analysis: Verbal Reports as Data, MIT Press, Cambridge, MA. 1984.

Erman, L. D., F. Hayes-Roth, V. R. Lesser and D. R. Reddy, "The Hearsay-II Speech-Understanding System: Integrating Knowledge to Resolve Uncertainty," Computing Survevs. 12. 2 (1980), 213–253

Fedorowicz, J. and G. D. Williams, "Representing Modeling Knowledge in an Intelligent Decision Sup port System," Decision Support Systems, 2, 1 (March 1986), 3–14.

Gero, J. S. and R. D. Coyne, Design Theory for CAD, in “Knowledge Based Planning as a Design Paradigm," in H. Yoshikawa and E. A. Warman (Eds.), Elsevier Science Publishers, North-Holland. 1987. 339-379.

Guindon, R., "Knowledge Exploited by Experts during Software System Design." International Journal of Man-Machine Studies, 33 (1990), 279–304.

Han, G., S. Ohsuga, and H. Yamauchi, “The Application of Knowledge Base Technology to CAD." in J. Gero (Ed.), Expert Systems in Computer-Aided Design, Elsevier Science Publishers, Amsterdam, The Netherlands, 1987, 25–51.

Hansmann, F., Operations Research Techniques for Capital Investment, Huntington, Wiley N.Y., 1974

Hayes-Roth, B., “A Blackboard Architecture for Control," Artificial Intelligence. 26 (1985) 251–321 and F. Haves-Roth. “A Cognitive Model of

Jagnannathan, V., R. Dodhiawala and L. S. Baum, (Eds.), Blackboard Architectures and Applications Academic Press, San Diego, CA, 1989.

Johnson, M. E. and J. P. Poorte, “A Hierarchical Approach to Computer Animation in Simulation Modeling," Simulation, 50, 1 (1988), 30–36

Kaebling, L. P, “An Architecture for Intelligent Reactive Systems," in J. Allen, J. Hendler, and A. Tate (Eds.), Readings in Planning, Morgan Kaufman Publishing, San Mateo, CA. 1990, 713–728.

Kalay, Y. E., "A Knowledge-Based Computable Model of Design," in J. Gero (Ed.), Expert Systems in Computer-Aided Design, 1987, 203–223.

Kerlinger, F. N., Foundations of Behavioral Research, 3rd. Ed., Holt, Rinehart and Winston, New York. 1986.

Kimbrough, S. O. and R. Lee, "Logic Modeling: A Tool for Management Science." Decision Support Systems, 4 (1988), 3–16.

Krishnan, R., “A Logic Modeling Language for Automated Model Construction." Decision Sunport Sys. tems, 6 (1990), 123–152.

Lazimi, R., “A Generic Shell Approach for Knowledge Elicitation and Representation in IDSS." Proceedings of the Eighth International Conference on Information Systems, Pittsburgh, PA, December 1987. 335-351.

Liang, T. P., "Development of a Knowledge-Based Model Management System," Operations Research. 36, 6 (Nov./Dec. 1988), 849–863

Luger, G. F., "Mathematical Model Building in the Solution of Mechanics Problems: Human Protocol and the MECHO Trace," Cognitive Science, 5 (1981), 55–77

Ma, Pai-Chun, F. H. Murphy, and E. A. Stohr, "Computer-assisted Formulation of Linear Programs." IMA Journal of Mathematics in Management, 1 (1987), 147–161.

Ma, P. C., E. A. Stohr, and F. H. Murphy, “Semantic Structures in Linear Programs," Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, Vol, III, Decision Support and Knowledge Based Systems Track, (January 1989), 459–466.

MacCrimmon, K. R. and R. N. Taylor, "Decision Making and Problem Solving," in Ed Marvin and D.

Dunnette (Eds.), Handbook of Industrial and Organizational Psychology, Rand McNally, Chicago, IL, 1976. 1976.

Maher. M. L., “Process Models for Design Synthesis," AI Magazine, 11, 4 (Winter 1990), 49–58. Maher, M. L., “Process Models for Design Synthesis,

Mintzbere H D. Raisinghani and A. Theoret, “The Structure of 'Unstructured' Decision Processes," Administrative Science Quarterly, 21 (1976), 246–275. Administrative Science Quarterly, 21

Mitroff I A J R. Emshoff and R. N. Kilmann, "Assumptional Analysis: A Methodology for Strategic Problem Solving," Management Science, 25, 4 (June 1979), 583–593. Problem Solving,"Management

Muller-Merbach H., "The Modeling Process: Steps Versus Components," Design and Implementation of Computer-Based Information Systems, N. Szyperski and E. Grochla, (Eds.), Sijthoff and Noordhoff, Germantown, MD, 1979. Germantown, MD, 197

Murphy. F. H. and E. A. Stohr, “An Intelligent System for Formulating Linear Programs," Decision Support Systems, 2, 1 (March 1986), 39–47. Support Systems, 2,

Nii. H. P. E. A. Feigenbaum, J. J. Anton and A. J. Rockmore, "Signal-to-Symbol Transformation HASP/SIAP Case Study," AI Magazine, (Spring 1982), 23–35. HASP/SIAP Case Study,

Novak, G. S., Jr., "Representations of Knowledge in a Program for Solving Physics Problems," Proceedings of the Fifth International Joint Conference on Artificial Intelligence, Cambridge, MA, 1977, 286– 291. 291.

“Model Formulation for Physics Problem Solving," Working Paper, Heuristic Programming Project, Stanford University, April 1982. Project, Stanford University, April

Pabo C. O. and E. G. Suchanek, "Computer-Aided Model-Building Strategies for Protein Design," Biochemistry, 25 (1986), 5987–5991.

Paige, J. M. and H. A. Simon, “Cognitive Processes in Solving Algebra Word Problems," in Problem Solving: Research Method, and Theory, B. Kleinmuntz and D. E. Berlyne (Eds.), Wiley, New York, 1966, 51–119.

Raghunathan. S., “Planning Aids: An Intelligent Modeling System for Planning Problems based on Constraint Satisfaction." IEEE Transactions on Knowledge and Data Engineering, 4, 4 (August 1992), 317-335.

Resnick. I. B., E. Cauzinille-Marmeche and J. Mathieu, "Understanding Algebra," in J. A. Sloboda and D Rogers (Fds.), Cognitive Processes in Mathematics, Keele Cognition Seminars: 1, Oxford Science Publications. 1987. Publications, 1987.

Schweiger. D., C. Anderson and E. Locke, “Complex Decision Making: A Longitudinal Study of Process and Performance." Organizational Behavior and Decision Processes, 36 (1985), 245-272.

Sen A., A. Vinze and S. T. Liou, “Construction of a Model Formulation Consultant: The AEROBA Experience." IEEE Transactions on Systems, Man, and Cybernetics, 22, 5 (September/October 1992), 1220-1232. 1220\~1.

Simon, H. A., “The Structure of Ill Structured Problems," Artificial Intelligence, 4 (1973), 145–180. Simon, H. A., "The Structure

Sivasankaran, T, and M. Jarke, "Logic-based Formula Management Strategies in an Actuarial Consulting System," Decision Support System, 1 (1985), 251–262. System," Decision Supporl

Sleeman, D., “An Attempt to Understand Students' Understanding of Basic Algebra," Cognitive Science, 8 (1984), 387–412. (1984), 387–412

Smith, G. F “Towards a Heuristic Theory of Problem Structuring," Management Science, 34, 12 (1988), 1489-1506. 1489-1300.

Takeda, H.. P. Veerkamp, T. Tomiyama, and H. Yoshikawa, "Modeling Design Processes," AI Magazine, 11, 4 (Winter 1990), 37–48. 11, 4 (Winter 1990), 37–48.

Vinze A and A Sen. “Expert Assistance for the Decision Support Process Using Hierarchical Planning," JEEE Transactions on Systems, Man, and Cybernetics, 21, 1 (January 1991), 390–401.

, and S. T. Liou, “AEROBA: A Blackboard Approach to Model Formulation," Proceedings of the Twenty-Fifth Hawaii International Conference on System Sciences, Decision Support and Knowledge-Based Systems Track, January 1992. port and Knlowi

, and "Operationalizing the Opportunistic Behavior in Model Formulation." International Journal of Man-Machine Studies, 38 (1993), 509–540.
