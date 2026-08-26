---
otero_id: 4642
otero_key: "FQ9Q58KS"
title: "Using decision tree modelling to support Peircian abduction in IS research: a systematic approach for generating and evaluating hypotheses for systematic theory development"
authors: "Kweku-Muata Osei-Bryson; Ojelanki Ngwenyama"
year: "2011"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.2010.00368.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using decision tree modelling to support Peircian abduction in IS research: a systematic approach for generating and evaluating hypotheses for systematic theory development

Kweku-Muata Osei-Bryson\* & Ojelanki Ngwenyama<sup>†</sup>

\*Information Systems Department, Virginia Commonwealth University, Richmond, Virginia, USA, email: kmuata@isy.vcu.edu, and <sup>†</sup>Institute for Innovation and Technology Management, Ryerson University, Toronto, Canada, email: ojelanki@ryerson.ca

Abstract. Since their early development, computers have had a profound impact on how we conduct modern scientific research. The disciplines of mathematics and operations research are perhaps the earliest to be dramatically transformed by information technology. However, over the years, computing technologies have provided many new opportunities for information processing, problem solving and knowledge creation. In this paper, we explore the potential of data mining technology for providing support for systematic theory testing based on Peirce’s theory of abduction. We propose a data mining approach to abducting and evaluating hypotheses based on Peirce’s scientific method. We believe that this approach could assist scientist to more efficiently explore alternative hypotheses for existing theories. We demonstrate our approach with empirical observations collected using instruments from the well known user performance area of information systems research.

Keywords: abduction, IT support for research, IS research methods, theory testing

## INTRODUCTION

A fundamental tenet of positivist scientific inquiry is the exploration of the limits of existing theories in order to postulate alternatives (Popper, 1957). However, it has been observed that a significant obstacle to such exploration of theories is the difficulty that scientist face in continually generating hypotheses for (rigorous and ruthless) testing (Popper, 1968). In any scientific discipline, testing the limits of existing theories is a difficult, time consuming and costly process. In information systems (IS) these difficulties are further confounded by rapidl changing information technologies (IT) and the emergent nature of the organisations that utilise them. Recent discussions on the state of our discipline suggest that we are facing an enormous challenge in producing knowledge that is rigorous and relevant to existing and emergent problems in the utilisation of IT in organisations and in society (Galliers, 1994; Zmud, 1996; Davenport & Markus, 1999; Benbasat & Zmud, 1999). While no one would deny that systematic testing of our theories and postulating alternative ones is important to advancing of our discipline, there is no clearly articulated approach for conducting such an inquiry. Currently, much of IS theorising is built on theories from other disciplines, and little systematic investigation (as defined by Popper) is conducted to explore the limits of those theories within the context of IS phenomena. According to Popper (1963), systematic testing should involve no only attempts to falsify a theory via repeated observation and experimentation, but to propose alternative hypotheses that would also be subject to falsification. The scientist must reject ad hoc hypotheses that would support the theory in favour of systematically derived ones that offer the potential for new predictions.

Presently, positivist IS theory testing is limited to falsification experiments. The second par of Popper’s prescriptions which is rigorous exploration of the limits of the theory is much more difficult to attain because of limitations on the generation of alternative hypotheses. Such systematic testing of IS theories is even more challenging because of the dynamic nature o the phenomena (organisations and technology) about which the IS discipline is concerned. In this paper, we discuss how data mining technologies could be applied to assist researchers in abducting and evaluating hypotheses for systematic theory testing and development. Using IT to support IS research is not new; we are presently using various IT-based tools such as EQS (Multivariate Softwares, Inc., CA, USA), Amos (SPSS Inc, West Yorkshire, UK), partial least squares (PLS) (and others) for factor analysis and testing of models, Atlas/TI, HyperResearch, NVivo and Leximancer for qualitative data analysis. We believe that the method and computational procedure that we are presenting could improve the efficiency and effectiveness of research, not only in IS, but also in other disciplines. To illustrate our approach, we apply it to the well-known research area of user performance.

## HYPOTHETICO-DEDUCTIVE (H-D) THEORY DEVELOPMENT

The general model of H-D theory development, on which positivist IS research is based, can be described as a cyclical process (cf. Figure 1) of empirical observation, theory formulation, hypotheses generation and hypotheses testing (Grimes, 1990; Chalmers, 1994; Palys, 2003). The scientist first observes some puzzling phenomena in the universe of inquiry (UoI). He or she then attempts to produce general statements that he believes could explain the phenomena. Then, after generating some hypotheses, the scientist then tries to deduce their implications and design experiments to test the logical consequences of the hypotheses. This can be a prediction experiment of the form – ‘if principle P is true, then event E should occur or fac F should be true.’ He/she then carries out the experiments to test the validity of the hypotheses, to see if the predictions prove to be true or false. That is if P is true, does the event E occur or can it be caused to occur. A further test is how reliable is the expectation of the event E occurring when P is true. Note that a single situation of E not occurring when P is true refutes the hypotheses. No amount of testing can ever guarantee the truth value of a theory about phenomena (Brown, 1977; Chalmers, 1994). What is actually attained by using the scientific method is a gradually increasing confirmation of the theory (Carnap, 1953; Lakatos, 1974; Salmon, 1989). Continued cycles through this process over time can lead to the development, acceptance and/or rejection of a scientific theory.

A key limitation of the H-D model is the reliance on human imagination for the hypotheses generation phase (Popper, 1963; Peirce, 1867; cf. CP). However, we believe that a data mining technique known as decision tree (DT) generation can be adapted to support Peirce’s method of hypotheses generation and help overcome this limitation. Data mining technology has already had a profound impact on scientific research in medicine and genetics (Brusic & Zeleznikow, 1999; Lee & Irizarry, 2001). Some of these techniques can enable IS researchers to identify and understand key relationships among empirical observations that can otherwise elude them.

## THEORETICAL FOUNDATIONS OF THE METHOD

Our method focuses on the hypotheses generation phase in Figure 1. What we are proposing is a data mining approach for the abduction and evaluation of hypotheses based on Peirce’s scientific method, and specifically on his theory of abduction. Some scholars (Putnam, 1982; Tursman, 1987; Dipert, 1995; Quine, 1995) consider Peirce a pioneer of the application of deductive and abductive logics to modern scientific inquiry. Other scholars consider him the founding father of modern deductive logic and the first person to systematise abductive inference into a formal method (Hanson, 1961; Harman, 1965; Fann, 1970; Quine, 1995; Hintikka, 1968; 1997; Niiniluoto, 1993; 1999). A fundamental objective of Peirce’s work was the development of a scientific method, ‘laws of development of science. . . . that rests on a sound general theory of logic’. And while his method is similar to the H-D approach, he makes explicit a method for hypotheses generation and evaluation (cf. CP, 1 pp. 492). Our approach is based on Peirce’s method and it targets the phase of theory development and testing, hypotheses generation, that is most difficult for the scientist. Our approach is implemented as a cyclic three-step procedure:

![](/api/attachments/FQ9Q58KS/fulltext/images/ec6ea16de2371d7c4deb997b1f87095f17b2d0dbb7b4550d0475fd4c6974929d.jpg)  
Figure 1. General model of hypothetico-deductive logic.

1 Abduction of a set of alternative hypotheses.

2 The evaluation of the test worthiness of the hypotheses.

3 Selection of an appropriate set of the hypotheses that present an alternative or improved model to explain the evidence.

## Basics concepts for hypothesis abduction

Abduction is an approach to hypotheses generation based on a method of logical inference that was proposed by Charles Sanders Peirce around 1867 (cf. CP). For Peirce, abduction is an approach to ‘studying the facts and devising a theory to explain them’ (CP 5.145); it is an ‘inferential step . . . , [it is] the first stating of a hypothesis and the entertaining of it, whether as a simple interrogation or with any degree of confidence’ (CP 6.525). To understand fully the subtle nuances of abduction, it is important to place it in context with the other forms of inferential logic: induction and deduction. While induction is inference to a rule and deduction inference to a consequence, abduction is inference to a hypothesis (conjecture or theory) that might explain the facts (see Appendix A for an illustration of the three inferential logics). Peirce explains his scientific method as inclusive of the inferential logics: (1) abduction for proposing hypotheses; (2) deduction for deriving the consequences of the hypotheses; and (3) induction for testing and verifying the hypotheses. The key contribution of Peirce’s method to positivist theory testing is that following abductive reasoning, a researcher creates many plausible hypotheses (conjectures) that can be later tested empirically (Fann, 1970; Thagard, 1978; Tursman, 1987; Magnani, 2001). For Peirce, ‘abduction is the process of forming an explanatory hypothesis’ (CP 5.171). The inferential step of abduction is to posit a hypothesis that might explain the empirical observations. This is the inverse of deductive logic; in his Lowell lectures (1866), Peirce states that hypothesis is the inversion of deduction (CP 1:428, 440). Elsewhere, Peirce formally defines abduction as the logical inference of the form: ‘the surprising fact C is observed; but if A were true, C would be a matter of course. Hence, there is a reason to suspect that A is true’ (CP. 5. 189). The general theory of abduction can be expressed in forma logic by the following general formula:

Given the law $( \mathsf { x } ) ( \mathsf { F x } \mathsf { a } \mathsf { G x } )$

From Ga infer Fa.

Later, in his ‘Theory of Probable Inference’ (1883), he asserts a probabilistic version of abduction (CP 2.716–717), which some scholars describe as a subsumption theory of explanation (Hanson, 1961; Hempel, 1965; Day & Kincaid, 1994). Although the general theory of abduction was powerful enough to yield testable hypotheses for most cases, Peirce formulated probabilistic version of it (CP 2.508–516, 2.627). He states:

a has the numerous marks G, G-, G-, etc.

b has the proportion r of the marks $G , G ^ { \prime } , G ^ { \prime \prime } ,$ etc.

Hence, probably and approximately, b has an r-likeness to a.

From the above, we can conclude that r = 1 if a and b are completely similar; this probabilistic formulation of abduction accommodates hypotheses with an appropriate probability/likelihood function. We will discuss this likelihood function in the next section.

## Rules for evaluating the test worthiness of hypotheses

Peirce outlined two main criteria for evaluating the test worthiness of hypotheses generated for the purpose of theory development (CP. 1931–58): (1) the likelihood that the hypothesis will be confirmed in testing, that is, a numeric estimate of the probability that the hypothesis will explain the facts; and (2) the breadth of the hypotheses; as he puts it, ‘twenty skillful hypotheses will ascertain what a million stupid ones will fail to do’. Peirce operationalised his test worthiness criteria for hypotheses using probabilistic reasoning (Peirce, CP, 1931–58). The key to distinguishing among the hypotheses is to find the ones that have a higher likelihood of offering a better explanation of the empirical observations. This approach is commonly called inference to the better explanation (IBE) (cf. Harman, 1965; Hempel, 1965; Day & Kincaid, 1994). The IBE rule suggests that H is preferred when from a set of hypotheses H is a better explanation of the evidence E relative to the background assumptions B. This rule can be defined as follows:

IBE 1.0: Given the evidence E accept the hypothesis H which maximises the likelihood P(E/H&B)

Because we are looking for testable hypotheses, we are not interested in the case in which the hypothesis H is a universal generalisation such that P(E/H&B) = 1. Such a hypothesis would not be falsifiable and as such, would be invalid for the purpose of scientific theory construction and testing. Further, because we are working with evidence collected using instruments based on existing theory, we are unlikely to see the situation in which we have a hypothesis H where P(E/H&B) = 0. This would imply that the empirical observation E is altogether incompatible with the hypothesis H. A solution to these two problems can be formally defined as:

IBE 1.1: Given the evidence E accept the hypothesis H which maximises P(H/E) – P(H)

By specifying this rule, we can ensure that the chosen hypothesis has a high posterior probability and high explanatory power, as we can now set some cut-off point for $P > 0$ that satisfies our interest for exploring the research. This brings us to the final theoretical problem of how to abduct more general hypotheses from lower level ones. A problem commonly referred to as entailment (Hempel, 1965; Hintikka, 1968). Entailment deals with the basic problem of abducting more general hypotheses from lower level hypotheses. For Peirce, if hypothesis H logically includes hypotheses H1 and H2, and H is falsifiable, then H is chosen as the more general hypothesis. Niiniluoto and Tuomela (1973) have argued that the genera IBE rule (IBE 1.1) can be rewritten as: if hypothesis H explains the evidence E better that H1 and H2 combined, H is the more general hypotheses. We can now satisfy the requirements for assessing the posterior probability of our hypotheses by defining the following constraint:

IBE 1.2: Assuming that $\mathsf { P } ( \mathsf { H } ) > 0$ and $\mathsf { P } ( \mathsf { E } ) < 1$ , if H entails E, then $\mathsf { P } ( \mathsf { H } / \mathsf { E } ) > \mathsf { P } ( \mathsf { H } )$

In the following we outline the basic concepts of the data mining technique that we use to operationalise our approach.

## THE DATA MINING TECHNIQUE

We will now explain how a data mining technique known as DT generation (Quinlan, 1986; Kim and Koehler, 1995) can be adapted to implement the logical theory of hypotheses generation and evaluation outlined above. In our methodology, we employed DT generation as a data analysis technique to support:

1 The abduction of hypotheses from the empirical observations.

2 Entailment, the abduction of more general hypotheses from lower level ones.

3 Computing the posterior probabilities and other test statistics for evaluating the test worthiness of the generated hypotheses.

4 The generation of the theoretical model.

A DT is a tree-structured representation of a prediction problem, a model in the form of interpretable and actionable rules (see Figure 2). Each non-leaf node of the DT is associated with one of the independent variables. Each branch from a non-leaf node is associated with a subset of the values of the corresponding independent variable. And each leaf node is associated with a value of the dependent (target) variable. There are two main types of DTs: (1) classification trees and (2) regression trees. For a classification tree, the dependen variable takes its values from a discrete domain, and for each leaf node, the DT associates a frequency, and in some cases a value, for each class of the dependent variable. The class that is assigned to a given leaf node of the classification tree results from a form of majority voting in which the winning class is the one that provides the largest relative frequency. In this paper, we will focus on the classification tree, which is the more commonly used type of DT, and so henceforth in the paper, whenever we use the term ‘decision tree/DT’ we will be referring to a classification tree.

## BASIC CONCEPTS OF DTS

A DT can be described as a model of a prediction problem in the form of interpretable and actionable rules (see Figure 1). Associated with each leaf of the DT is an IF–THEN rule. For a given rule: the condition component (independent variable(s) and their values) of the rule is described by the set of relevant internal nodes and branches from the root to the given leaf; the action part of the rule is described by the relevant leaf which provides the relative frequencies for each class of the dependent variable.

![](/api/attachments/FQ9Q58KS/fulltext/images/73130f4e6511c92b87e5a3987232254d44a4c52e3a8995d354022a2d95b62342.jpg)  
Figure 2. Diagram of a decision tree.

Below, we display the four (4) rules for the DT in Figure 1 where each variable has been discretised into three classes: Low: [1.0, 2.5]; Medium: [2.5, 5.5]; High: [5.5–7.0]. It should be noted that N is the number of cases associated with the condition component of the rule (Table 1).

These rules describe a set of hypotheses that were generated from our analysis; we will discuss them in detail later. Here, we limit our discussion to pointing out key characteristics relevant to understanding their use in our method. As stated earlier, these rules can be interpreted as conditional hypotheses. For example, Rule 1 can be interpreted as: If the independent variable UTILISATION is High (i.e. [5.5–7.0]), then the dependent variable PER-FORMANCE will be High (i.e. [5.5–7.0]) with relative frequency f = 0.200, and 45 cases supporting this rule. Rule 4 can be interpreted as: IF the independent variable UTILISATION is High (i.e. [5.5–7.0]), THEN the dependent variable PERFORMANCE will be High (i.e. [5.5–7.0]) with relative frequency f = 0.896, and 192 cases supporting this rule. On careful analysis the reader will observe that Rules 2 and 3 have a similar structure, they emanate directly from the internal node SYSTEM QUALITY that is itself connected to node Utilisation through the branch UTILISATION = Medium (i.e. [2.5–5.5]). Rules 2 and 3 are called sibling rules, because they involve the entire set of branches from the internal node UTILISATION = Medium (i.e. [2.5–5.5]). We will return to our discussion of sibling rules, as they are importan to the abduction of Sibling Rules Hypotheses.

Table 1. Ruleset of decision tree of figure 1

<table><tr><td>Rule ID</td><td>Condition</td><td>Action: likely resulting performance</td><td>N</td></tr><tr><td>1</td><td>Utilisation = Low</td><td>{High: 20.0%; Med: 55.6%; Low: 24.4%},</td><td>45</td></tr><tr><td>2</td><td>Utilisation = Medium &amp; System_Quality = Low_to_Med</td><td>{High: 31.6%; Med: 65.8%; Low: 2.6%}</td><td>231</td></tr><tr><td>3</td><td>Utilisation = Medium &amp; System_Quality = High</td><td>{High: 64.9%; Med: 35.1%; Low: 0.0%}</td><td>97</td></tr><tr><td>4</td><td>Utilisation = High</td><td>{High: 89.6%; Med: 10.4%; Low: 0.0%}</td><td>192</td></tr></table>

## ABDUCTION AND PRELIMINARY EVALUATION OF HYPOTHESES

We are now concerned with explaining how the theoretical concepts of abduction and evaluation are operationalised in the data mining-based method. The reader will recall that Peirce suggested that any abducted hypothesis should be evaluated for ‘the likelihood that the hypothesis will be confirmed in testing’. For the evaluation, we use traditional statistics-based hypothesis testing (illustrated later). We now focus on illustrating how we operationalise the process of abduction. We consider two types of hypotheses: (1) those derived using a single rule which we will refer to as Single Rule Hypotheses; and (2) those derived using a set of sibling rules, which we will refer to as Sibling Rules Hypotheses. A Sibling Rules Hypothesis could be a global hypothesis or a local hypothesis.

## Global and local hypotheses

A global hypothesis has the form: ‘Variable X has an Impact\_Type impact on the Target Variable Y’, where Impact\_Type ∈ {positive; negative; U-shaped curvilinear; inverted U-shaped curvilinear; None}. It reflects an average pattern that applies across the entire problem space. A local hypothesis has the form: ‘Given a certain Backend Condition Event, then Frontend Condition Variable X has an Impact\_Type impact on the Target Variable Y’. An example of a local hypothesis is: ‘Given Utilisation = Medium, then System\_Quality has a positive impact on Performance’. It reflects an average pattern that applies across a sub-region of the problem space. It is important to note that in some situations, while a global hypothesis might not be supported by empirical data, the local hypothesis might be. Local hypotheses that are supported by the data may be of interest to managers as they can provide guidance for action. Further, together with the associated global hypothesis, local hypotheses can provide a richer picture of the complex relationship between the given predictor variable and the target variable. This strategy provides researchers the ability to develop a detailed understanding of the dynamics of the problem domain that could lead to better (more relevant) predictive theories. It also operationalises a key scientific principle, ‘inference to the better explanation’ (cf. IBE 1.0 in Section 2.1.2). It is important to emphasise that it is unlikely that a researcher would be able to dream up all relevant local hypotheses, consequently without the strategy outlined above, relevant local hypotheses may not be conceptualised and interrogated in later confirmatory data analysis.

## Discretisation of factor scores

An important aspect of our systematic analysis of the hypotheses involves the use of discrete ordinal variables for the factor scores, originally coded on a seven-point Likert scale: (1: Strongly Disagree; 2: Moderately Disagree; 3: Slightly Disagree; 4: Neither Agree nor Disagree; 5, Slightly Agree; 6: Moderately Disagree; and 7: Strongly Agree). Discrete ordinal variables enable the researcher to derive meaningful ranges of values while abducting statistically testable hypotheses about the research problem. There are a variety of legitimate approaches to discretise the factor scores. One legitimate approach that is useful for our purposes, particularly with regard to the abduction of sibling rules hypotheses, is discretisation that involves three categories corresponding to Low, Medium and High values for the given factor. Table 2 displays the qualitative and numeric intervals that we use for each category of the factor scores.

## Sibling rules hypothesis

A Sibling Rules Hypothesis could be directional (e.g. variable X has a positive or negative impact on variable Y) or non-directional (i.e. variable X impacts variable Y). In either case, they are derived using a set of sibling rules (see Appendix D for more details). In our methodology, for any set of sibling rules, we can generate and test a corresponding Sibling Rules Hypothesis. For example, consider the Rules 2 and 3 (recall Table 1) which constitute a full set o sibling rules. Given this pair of rules, we could generate and indirectly test the directional Sibling Rules Hypothesis: ‘Given $U t i l i s a t i o n = M e d i u m$ , then System\_Quality has a positive impact on Performance’. We could indirectly explore the validity of this Sibling Rules Hypothesis by testing the surrogate hypothesis: Given Utilisation = Medium, target event Performance $= H i g h \ i . e$ . [5.5–7.0]) is more likely to occur if System\_Quality = High (i.e. [5.5–7.0]) than if System\_Quality = Low\_Medium (i.e. [1.0–5.5]), i.e. p > p where p , p are the population probabilities associated with the target event $P E R F O R M A N C E = H i g h$ for System\_Quality = High and System\_Quality = Low\_Medium, respectively). Acceptance (i.e. non-rejection) of this surrogate hypothesis would suggest that the given candidate Sibling Rules hypothesis migh be valid and so should be abducted (see Table 3).

Table 2. Illustrative discretisation intervals

<table><tr><td rowspan="2">Category</td><td colspan="2">Intervals: regular coding</td><td colspan="2">Intervals: reverse coding</td></tr><tr><td>Qualitative</td><td>Numeric</td><td>Qualitative</td><td>Numeric</td></tr><tr><td rowspan="2">Low (L)</td><td>Strongly Disagree</td><td>[1.0, 2.5]</td><td>Moderately Agree</td><td>[5.5, 7.0]</td></tr><tr><td>Moderately Disagree</td><td></td><td>Strongly Agree</td><td></td></tr><tr><td rowspan="3">Medium (M)</td><td>Slightly Disagree</td><td>[2.5, 5.5]</td><td>Slightly Disagree</td><td>[2.5, 5.5]</td></tr><tr><td>Neither Disagree nor Agree</td><td></td><td>Neither Disagree nor Agree</td><td></td></tr><tr><td>Slightly Agree</td><td></td><td>Slightly Agree</td><td></td></tr><tr><td rowspan="2">High (H)</td><td>Moderately Agree</td><td>[5.5, 7.0]</td><td>Strongly Disagree</td><td>[1.0, 2.5]</td></tr><tr><td>Strongly Agree</td><td></td><td>Moderately Disagree</td><td></td></tr></table>

## Single rules hypothesis

A Single Rule Hypothesis would have the form: If Condition (e.g. Utilisation is High) applies then the probability of target event (e.g. User Performance is High) is Strong $( \mathfrak { i } . \mathfrak { e } . \ p _ { 0 } \geq \tau _ { 0 } )$ . It is important to note here that a Condition could consist of a single condition event (e.g. Utilisation = High) or a conjunction of condition events (e.g. Utilisation = Medium & System\_Quality = High) in the given rule. For our purposes, we are only interested in Single Rule hypotheses for which the value of $p _ { 0 }$ satisfies the test worthiness specification (constraint IBE 1.1, Section 2.1.2) of the researcher $( \mathsf { i } . \mathsf { e } . , p _ { 0 } \geq \tau _ { 0 } )$ . Therefore, for each set of sibling rules, a given rule is considered to be a strong rule only if statistical testing supports the hypothesis: $p _ { 0 } \ge \tau _ { 0 }$ . Only strong rules are used to generate Single Rule Hypotheses; therefore, the first step involves identifying the strong rules in a given set of sibling rules. However, it is possible that each rule in a set of siblings could be strong, which would suggest that the discriminating variable for the given set of sibling rules would not be a useful predictor within the context of a Strong Single Rule hypothesis. Therefore, we only use those strong rules that are statistically different from at least one of their sibling rules to form Strong Single Rule Hypotheses.

## THE ENTAILMENT PROCEDURE

The reader will recall that entailment is the abduction of more general hypotheses from lower level ones. The basic logic of entailment outlined by Peirce and Popper posits (cf. IBE 1.2 in Section 2.1.2 above) that if hypothesis H logically includes hypotheses H1 and H2, and H is falsifiable, then H is chosen as the more general hypothesis. Our data mining-based method implements entailment via a strategy of merging child nodes of an internal node to form a new sub-tree. For example, if the nodes associated with Rules 2 and 3 were merged then we would obtain a new sub-tree (see Figure 3 and Table 1) with the more general rule:

Table 3. Corresponding candidate sibling rules hypotheses for DT of figure 1

<table><tr><td rowspan="2">ID</td><td colspan="2">Condition events</td><td rowspan="2">N</td><td rowspan="2">Rel. freq (f)</td><td colspan="3">Surrogate hypotheses</td><td rowspan="2">Abduct?</td><td rowspan="2">Candidate sibling rules hypothesis</td></tr><tr><td>Backend</td><td>Frontend</td><td>Hyp.</td><td>t-stat</td><td>Dec</td></tr><tr><td rowspan="3">1</td><td></td><td>Util = L</td><td>45</td><td>0.200</td><td> $p_{M}>p_{L}$ </td><td>2.77</td><td>A</td><td>YES</td><td>Util has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>Util = M</td><td>328</td><td>0.415</td><td> $p_{H}>p_{M}$ </td><td>10.77</td><td>A</td><td></td><td></td></tr><tr><td></td><td>Util = H</td><td>192</td><td>0.896</td><td></td><td></td><td></td><td></td><td></td></tr></table>

H, high; M, medium; L\_M, low-to-medium; L, low; (For the column ‘Dec’ (Decision): A = Accept; R = Reject).

![](/api/attachments/FQ9Q58KS/fulltext/images/5410ccbca31c7abe569bb0040f42113aee7c09b9adedabafe4363a12f2f40940.jpg)  
Figure 3. Diagram of DT with rules 2 and 3 combined.

Rule 2–3: IF Utilisation is Medium THEN Performance = {High: 41.5%; Medium: 56.7%; Low: 1.8%}%}, where N = 328.

The reader may observe that this DT involves a partitioning of the dataset based on the Utilisation variable, but in which the partitioning is determined by the DT generation procedure. The set of sibling rules that is associated with this DT allows us to explore the impact of Utilisation on our performance variable Performance. However, every general rule entailed from sibling rules must be tested to ascertain if it satisfies the test worthiness criterion. It is important to note here that commercial data mining (DM) softwares such as SAS Enterprise Miner routinely provide the class distribution for each DT node, which can also be used for abducting higher hypotheses (entailment).

## THE PROCEDURE FOR ABDUCTING A THEORETICAL MODEL

Having illustrated the strategy for abducting and evaluating individual hypotheses, we will now present our data mining methodology as a five-step procedure for abducting a theoretica model, in which Step 1 is done by the researchers and Steps 2–5 are automatic. We will first outline the procedure then provide an illustrative example of the process (detailed step by step instructions for replication are provided in Appendix C). Step 1 of the process is the preparation phase (activities ‘a’ to ‘e’ in Appendix C). In this phase, the researcher: (a) identifies the dependent variables (or target variables in the language of data mining); (b) identifies any possible mediator variables; (c) defines and applies the Discretisation Method such as that described in Table 2; (d) specifies data mining parameter values (e.g. splitting methods, and minimum observations per leaf; (e) specifies the test worthiness threshold, t for Single Rule Hypotheses to be generated and a, the significance level for statistical testing of the hypotheses; and (f) the researcher specifies the Set of Selection Rules for Formulating and Evaluating Candidate Sibling Rules Hypotheses (for details see Appendix D).

In Step 2 of the process, the data mining software then generates the DT rules using the data mining parameters defined by the researcher in Step 1. From the set of generated DT rules, all the sets of sibling rules are automatically identified for further analysis. For each set of sibling rules discovered for which the relationships between the relevant frequencies are included in the Set of Selection Rules for Formulating and Evaluating Candidate Sibling Rules Hypothesis (see Appendix D), a candidate Sibling Rules Hypothesis is automatically selected and indirectly tested using statistical difference of proportions tests to determine if it is likely to be supported by the data. The candidate Sibling Rules hypotheses that satisfy the relevant difference of proportions tests are automatically abducted. In the second part of Step 2, Single Rules Hypotheses are automatically abducted and each is indirectly tested to determine if it is likely to be supported by the data.

In Step 3, the software examines the set of abducted hypotheses to identify those potential mediator variables that are included in at least one abducted hypothesis for the dependent variable. For each such mediator variable, Step 4, which is analogous to Step 2 for the dependent variables, is executed. Finally, in Step 5, the theoretical model is generated by integrating the set of causal links between the predictor and dependent variables that were identified in the sets of abducted Sibling Rules Hypotheses and Single Rule Hypotheses. On the completion of this process, the researcher(s) should provide justification for the existence of each causal link of the integrated theoretical model, and links that they cannot justify should be removed.

## BACKGROUND ON THE ILLUSTRATIVE PROBLEM

A number of studies have focused on end-user performance when using IS; in this section, we review some of this work that is relevant to our illustrative example. The body of research upon which we draw to illustrate our hypothesis generation methodology can be divided into two types of inquiry (a) task-technology fit studies; and (b) user satisfaction studies, each category approaching the study of end-user performance from a different perspective. The task-technology fit approach postulates that when the user’s task and the technology are congruent, user Performance will be High (Goodhue, 1995; Goodhue & Thompson, 1995; Mathieson & Keil, 1998; Dishaw & Strong, 1999). Consequently, studies falling under this approach try to define task and technology characteristics and the ‘goodness of fit’ between specific technologies and end-user tasks (Mathieson & Keil, 1998; Dishaw & Strong, 1999; Goodhue et al. 2000). On the other hand, user satisfaction studies investigate the extent to which certain IS properties such as system quality, information quality, system use and user satisfaction influence user performance (Doll & Torkzadeh, 1988: Bailey & Pearson. 1993). Numerous user satisfaction studies have been conducted in the last decade attempting to identify factors of the IS that lead to high user performance (Torkzadeh & Doll, 1991; DeLone & McLean, 1992; Doll et al., 1994). Our illustrative problem is situated within this second category of studies that attempt to define factors influencing end-user performance. In this regard, we will focus our review of relevan research in this area.

Much of the research on identifying factors influencing end-user performance have focused on identifying factors and designing and testing instruments for use in assessing enduser satisfaction (Doll & Torkzadeh, 1988; DeLone & McLean, 1992). For example, Bailey & Pearson (1993) conducted a literature review to identify influencing factors, and developed and tested a questionnaire for investigating user satisfaction. Doll & Torkzadeh (1988) developed an instrument to measure end-user computing satisfaction as a proxy for IS success. Etezadi-Amoli & Farhoomand (1996) developed a questionnaire instrument to measure end-user satisfaction, and empirically tested the relationship between end-user satisfaction and user performance. Igbaria & Tan (1997) studied the relationship among user satisfaction, system usage and individual impact. DeLone & McLean (1992) have validated that four factors – system quality, information quality, use, and user satisfaction – impact individual and organisational performance. Taken together, these studies have led to a list factors and various models for investigating end-user performance and an inventory of instruments for eliciting data from end-users. These studies also provide a list of variables/factors that have been investigated (cf. Appendix B).

## DATA COLLECTION AND FACTOR ANALYSIS

The data used to illustrate our methodology was collected from 20 organisations in two countries using well-known instruments that were validated by previous research. We integrated and used three questionnaires: (1) Goodhue and Thompson’s (1995) task-technology fit instrument; (2) Etezadi-Amoli & Farhoomand’s (1996) end-user computing satisfaction instrument (EUCS); and (3) Doll & Torkzadeh’s (1988) EUCS instrument. In integrating the three questionnaires, we removed overlapping items and added some items to capture geographic, industry and demographic characteristics, and validated the final instrument. The additional questions helped us access the industry of the respondents’ organisations and the level of the respondents’ knowledge of their organisation and their familiarity with the IS. In collecting the data, we used two different media: in the United States, we used an online internet survey, and in Thailand we used the more traditional method. Both the online and paper questionnaires used a seven-point Likert scale. Of the 25 organisations that participated in the study, 15 were from the United States and 10 were from Thailand. The response rate for the data collection was 84%. A total of 690 questionnaires were collected, 349 usable ones from the US organisations and 304 usable ones from Thai organisations; 36 questionnaires were discarded for incompleteness. In Appendix B we list the variables and their definitions. Following factor analysis, factor scores were also generated<sup>4</sup>. Using the discretisation transformations described in Table 2, for each observation, each corresponding factor score was then categorised as High, Medium or Low.

## APPLICATION OF ABDUCTION PROCEDURE TO THE ILLUSTRATIVE PROBLEM

The reader may recall that following factor analysis, our dataset included factor scores that were categorised as Low (L), Medium (M) or High (H) using the discretisation rules described in Table 2. For all of our analysis, we specified that the minimum number of cases (observations) for each DT rule should be 30; set the significance level for statistical testing at $\alpha = 0 . 0 5 ;$ and set the threshold of our test worthiness for the Single Rule Hypotheses as $\tau _ { 0 } = 0 . 8 0$ . The last threshold implies that we only consider a rule to be strong if $p _ { 0 } > \tau _ { 0 } = 0 . 8 0$ , and will only use these ‘strong’ rules to form single rule hypotheses. However, it should be noted that other rules may be generated during DT generation, but we will not use them to form single rule hypotheses. The Set of Selection Rules for Formulating and Evaluating Candidate Sibling Rules Hypothesis is the same as that provided in Appendix D. We used the SAS Data Mining software, Enterprise Miner, to generate and analyse the DTs.

## Abducting hypotheses for the dependent variable

For our dependent variable, Performance, the selected target event is High Performance (H). We generated multiple DTs by means of a strategy that ensured that each variable was selected as the first split for at least one of these DTs, while having the lower level splits to be automatically determined by the splitting algorithm. For each potential predictor variable X (i.e. System Quality, Ease of Use, Reliability, Authorisation, Documentation, Utilisation), this allowed us to indirectly test the global hypothesis:

Variable X has a Impact\_Type impact on Performance where Impact\_Type ∈ {NO; Posi tive; Negative; U-shaped symmetric curvilinear; inverted U-shaped symmetric curvilinear}.

For each generated DT, the lower-level sets of sibling rules allowed for the selection and testing of candidate Sibling Rules Hypotheses. A complete description and analysis of the rule-sets of all the generated DTs would result in an overly lengthy paper that would be tiring for the reader. Therefore, we will limit our analysis and discussion to the rule-sets of DT A1E (Table 4a) and show the results of the analysis of all the DTs for the dependent variable (Performance) in Appendix E.

The candidate Sibling Rules Hypotheses for A1E were automatically selected based on the Set of Selection Rules for Formulating and Evaluating Candidate Sibling Rules Hypotheses in Appendix D. Each hypothesis was then indirectly tested for validity using statistical difference of proportions tests. Only those candidate Sibling Rules Hypotheses that passed the validity tests were abducted (see Table 4a).

The next step in our procedure is the generation of the set of Single Rule Hypotheses fo the dependent variable. For each rule in a set of sibling rules that is statistically different from each of its siblings at significance level $\alpha = 0 . 0 5$ , we test the surrogate hypothesis $p _ { 0 }$ $\geq \tau _ { 0 }$ at significance level of $\alpha = 0 . 0 5$ , where $\tau _ { 0 } = 0 . 8 0$ . A single rule hypothesis is abducted only if the corresponding surrogate hypothesis is accepted (i.e. not rejected). In Table 4b below, we display all of the accepted Strong Single Rule Hypotheses and some of the rejected Single Rule hypotheses. It should be noted that the target event is High Performance.

Table 4a. The A1E rule set: sibling rules hypotheses

<table><tr><td rowspan="2">Set ID</td><td colspan="2">Condition event</td><td rowspan="2">N</td><td rowspan="2">Rel. freq (f)</td><td colspan="3">Surrogate hypotheses</td><td rowspan="2">Abduct?</td><td rowspan="2">Candidate sibling rules hypothesis</td></tr><tr><td>Backend</td><td>Frontend</td><td>Hyp.</td><td>t-stat</td><td>Dec</td></tr><tr><td rowspan="3">1</td><td></td><td>Util = L</td><td>45</td><td>0.200</td><td> $p_M > p_L$ </td><td>2.77</td><td>A</td><td>YES</td><td>Util has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>Util = M</td><td>328</td><td>0.415</td><td> $p_H > p_M$ </td><td>10.77</td><td>A</td><td></td><td></td></tr><tr><td></td><td>Util = H</td><td>192</td><td>0.896</td><td> $p_H > p_L$ </td><td>9.89</td><td>A</td><td></td><td></td></tr><tr><td rowspan="2">2</td><td>Util = H</td><td>SysQI = L_M</td><td>59</td><td>0.678</td><td> $p_H > p_{L\_M}$ </td><td>6.56</td><td>A</td><td>YES</td><td>GIVEN Util = H THEN</td></tr><tr><td></td><td>SysQI = H</td><td>133</td><td>0.992</td><td></td><td></td><td></td><td></td><td>SysQI has a positive impact on PERFORMANCE</td></tr><tr><td rowspan="2">3</td><td>Util = H &amp; SysQI = H</td><td>EOU = L_M</td><td>47</td><td>0.979</td><td> $p_H > p_{L\_M}$ </td><td>1.34</td><td>R</td><td>NO</td><td>GIVEN Util = H &amp; SysQI = H THEN</td></tr><tr><td></td><td>EOU = H</td><td>85</td><td>1.000</td><td></td><td></td><td></td><td></td><td>EOU has a positive impact on PERFORMANCE</td></tr><tr><td rowspan="2">4</td><td>Util = M</td><td>SysQI = L_M</td><td>231</td><td>0.316</td><td> $p_H > p_{L\_M}$ </td><td>5.59</td><td>A</td><td>YES</td><td>GIVEN Util = M THEN</td></tr><tr><td>Util = M</td><td>SysQI = H</td><td>97</td><td>0.649</td><td></td><td></td><td></td><td></td><td>SysQI has a positive impact on PERFORMANCE</td></tr><tr><td rowspan="2">5</td><td>Util = M &amp; SysQI = L_M</td><td>Auth = L</td><td>44</td><td>0.394</td><td> $p_L > p_M$ </td><td>1.80</td><td>A</td><td>YES</td><td>GIVEN Util = M &amp; SysQI = L_M THEN</td></tr><tr><td></td><td>Auth = M</td><td>157</td><td>0.255</td><td> $p_H > p_M$ </td><td>2.89</td><td>A</td><td></td><td>Auth has a U-shaped curvilinear impact on PERFORMANCE</td></tr></table>

(For the column ‘Dec’ (Decision): A = Accept; R = Reject).

Table 4b. Abducted single rule hypotheses for performance

<table><tr><td>DT</td><td>Condition Event</td><td>N</td><td>f</td><td>t-stat</td><td>P&gt;0.80</td></tr><tr><td>A1E</td><td>Util = H</td><td>192</td><td>0.896</td><td>3.317</td><td>Accept</td></tr><tr><td>A1E</td><td>Util = H &amp; SysQI = H</td><td>139</td><td>0.992</td><td>5.639</td><td>Accept</td></tr><tr><td>A1E</td><td>Util = H &amp; SysQI = H &amp; EOU = L_M</td><td>47</td><td>0.979</td><td>3.035</td><td>Accept</td></tr><tr><td>A1E</td><td>Util = H &amp; SysQI = H &amp; EOU = H</td><td>85</td><td>1.000</td><td>4.583</td><td>Accept</td></tr><tr><td>B1G</td><td>SysQI = H</td><td>236</td><td>0.835</td><td>1.341</td><td>Reject</td></tr><tr><td>B1G</td><td>SysQI = H &amp; Auth = H</td><td>98</td><td>0.890</td><td>2.216</td><td>Accept</td></tr><tr><td>B1G</td><td>SysQI = H &amp; Doc = H</td><td>77</td><td>0.900</td><td>2.179</td><td>Accept</td></tr><tr><td>B1E</td><td>EOU = H</td><td>158</td><td>0.842</td><td>1.316</td><td>Reject</td></tr><tr><td>B1E</td><td>EOU = H &amp; SysRI = H</td><td>77</td><td>0.900</td><td>2.179</td><td>Accept</td></tr><tr><td>B1E</td><td>EOU = H &amp; SysQI = H &amp; SysRI = H</td><td>62</td><td>0.935</td><td>2.636</td><td>Accept</td></tr><tr><td>T1G1</td><td>Auth = H &amp; SysQI = H</td><td>99</td><td>0.890</td><td>2.227</td><td>Accept</td></tr><tr><td>T1G1</td><td>Auth = M &amp; SysQI = H &amp; EOU = H</td><td>51</td><td>0.880</td><td>1.414</td><td>Reject</td></tr><tr><td>T1G2</td><td>Doc = H</td><td>103</td><td>0.835</td><td>0.884</td><td>Reject</td></tr><tr><td>T1G2</td><td>Doc = H &amp; Auth = H</td><td>38</td><td>0.970</td><td>2.585</td><td>Accept</td></tr><tr><td>T1G3</td><td>SysRI = H &amp; SysQI = H</td><td>13</td><td>0.880</td><td>0.693</td><td>Reject</td></tr></table>

## Abducting hypotheses for the mediator variable

The first step in this phase of the process is to identify mediator variables. This involves determining if the potential mediator variable (i.e. Utilisation) is included in any of the abducted hypotheses for the dependent variable (i.e. Performance). For example, if we examine the abducted Sibling Rules Hypotheses (see Table $_ { 4 \mathsf { a } ) }$ that were derived using $A 1 E ,$ , we observe that Utilisation (Util) is included in every abducted hypothesis. This suggests that Utilisation is a mediator variable. Our next step is to therefore generate DTs that can be used to derive candidate hypotheses that involve Utilisation as the target variable. Similar to the approach used for the dependent variable, candidate Sibling Rule Hypotheses were automatically selected and indirectly tested for the mediator variable. We present the results for one of the DTs (i.e. A2E) in Table 5a. The results of the analysis of all the DTs for the mediator variable are displayed in Appendix F.

Similar to the approach used for the dependent variable, candidate Single Rule Hypotheses for the mediator variable were automatically selected and indirectly tested. For Utilisation, all of the corresponding surrogate hypotheses were rejected and therefore, no corresponding Strong Single Rule Hypothesis was generated (see Table 5b).

Table 5a. Decision tree A2E: sibling rules hypotheses

<table><tr><td rowspan="2">Set ID</td><td colspan="2">Condition event</td><td rowspan="2">N</td><td rowspan="2">Rel. freq (f)</td><td colspan="3">Surrogate hypotheses</td><td rowspan="2">Abduct?</td><td rowspan="2">Candidate sibling rules hypothesis</td></tr><tr><td>Backend</td><td>Frontend</td><td>Hyp.</td><td>t-stat</td><td>Dec</td></tr><tr><td rowspan="3">1</td><td></td><td>EOU = L</td><td>48</td><td>0.063</td><td> $p_M > p_L$ </td><td>2.90</td><td>A</td><td>YES</td><td rowspan="3">EOU has a positive impact on Utilisation</td></tr><tr><td></td><td>EOU = M</td><td>360</td><td>0.250</td><td> $p_H > p_M$ </td><td>8.13</td><td>A</td><td></td></tr><tr><td></td><td>EOU = H</td><td>157</td><td>0.624</td><td> $p_H > p_L$ </td><td>6.80</td><td>A</td><td></td></tr><tr><td rowspan="2">2</td><td>EOU = H</td><td>SysQI = L_M</td><td>35</td><td>0.400</td><td> $p_H > p_{L\_M}$ </td><td>3.11</td><td>A</td><td>YES</td><td rowspan="2">GIVEN EOU = H THEN SysQI has a positive impact on Utilisation</td></tr><tr><td></td><td>SysQI = H</td><td>122</td><td>0.689</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">3</td><td>EOU = M</td><td>SysQI = L_M</td><td>250</td><td>0.176</td><td> $p_H > p_{L\_M}$ </td><td>4.88</td><td>A</td><td>YES</td><td rowspan="2">GIVEN EOU = M THEN SysQI has a positive impact on Utilisation</td></tr><tr><td></td><td>SysQI = H</td><td>110</td><td>0.418</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">4</td><td>EOU = M &amp; SysQI = H</td><td>Auth = L_M</td><td>75</td><td>0.395</td><td> $p_H > p_{L\_M}$ </td><td>0.75</td><td>R</td><td>NO</td><td rowspan="2">GIVEN EOU = M &amp; SysQI = H THEN Auth has a positive impact on Utilisation</td></tr><tr><td></td><td>Auth = H</td><td>34</td><td>0.471</td><td></td><td></td><td></td><td></td></tr></table>

Legend for the column: Dec (Decision): A = Accept: R = Reject.

Table 5b. Sample of tested single rule hypotheses for utilisation

<table><tr><td>DT</td><td>Condition event</td><td>Target event</td><td>N</td><td>F</td><td>t-stat</td><td>P&gt;0.80</td></tr><tr><td>A2E</td><td>EOU = H</td><td>UTIL = H</td><td>157</td><td>0.624</td><td>-5.4956</td><td>Reject</td></tr><tr><td>A2E</td><td>EOU = H &amp; SysQI = H:</td><td>UTIL = H</td><td>122</td><td>0.689</td><td>-3.0525</td><td>Reject</td></tr><tr><td>T2G4</td><td>SysQI = H</td><td>UTIL = H</td><td>236</td><td>0.555</td><td>-9.3894</td><td>Reject</td></tr><tr><td>T2G4</td><td>SysQI = H &amp; Auth = H</td><td>UTIL = H</td><td>98</td><td>0.663</td><td>-3.3732</td><td>Reject</td></tr></table>

## Abduction of theoretical model

At this stage, a theoretical model can be automatically generated by integrating the set of causal links that are associated with the abducted Sibling Rules Hypotheses (see Appendices E and F) and Strong Single Rule Hypotheses. This theoretical model describes the independent, mediator and dependent variables, and the newly hypothesised relationships. Having followed the approach systematically analysing the data and abducting and evaluating alternative hypotheses, we conjecture that this is a better explanation of the data than existing explanations of the data. Our conjecture can be empirically tested in future investigations. Below, we display our new theoretical model with causal links and associated supporting hypotheses in Table 6.

## CONCLUDING REMARKS

In this paper, we developed and illustrated a new approach to systematic theory developmen and testing based on Peirce’s scientific method. Our approach is unique in that it uses modern data mining technology for abduction of hypotheses and the theoretical model from empirica data. This data mining technology is itself built on the principles of abductive inference outlined by Peirce (CP. 1931–58; see also Fann, 1970; Shanahan, 1989; Pagnucco, 1996; Flach, 2000; Flach & Kakas, 2000). Our approach provides significant support for the researcher who would otherwise have to ‘dream up’ large numbers of relevant and testable hypotheses from an almost infinite domain. We believe that this approach can contribute significantly to the advancement of the discipline of IS and many others. We will now consider some questions that might concern the reader about our DT-based approach:

Table 6. Summary of abducted hypotheses

<table><tr><td>Causal link</td><td>Supporting abducted hypotheses</td></tr><tr><td>Auth ⇒ Perf</td><td>Auth has a symmetric U-shaped curvilinear impact on PERFORMANCEGIVEN Util = M &amp; SysQI = L_M THEN Auth has a symmetric U-shaped curvilinear impact on PERFORMANCEGIVEN SysQI = L_M &amp; EOU = M THEN Auth has a positive impact on PERFORMANCEGIVEN Doc = M THEN Auth has a symmetric U-shaped curvilinear impact on PERFORMANCEGIVEN Doc = H &amp; Auth = H THEN PERFORMANCE = H with High ProbabilityGIVEN SysQI = H &amp; Auth = H THEN PERFORMANCE = H with High ProbabilityGIVEN Auth = H &amp; SysQI = H THEN PERFORMANCE = H with High Probability</td></tr><tr><td>Doc ⇒ Perf</td><td>Doc has a positive impact on PERFORMANCEGIVEN SysQI = H &amp; Doc = H THE PERFORMANCE = H with High ProbabilityGIVEN Doc = H &amp; Auth = H THEN PERFORMANCE = H with High Probability</td></tr><tr><td>EOU ⇒ Perf</td><td>EOU has a positive impact on PERFORMANCEGIVEN SysRI = H &amp; SysQI = H THEN EOU has a positive impact on PERFORMANCEGIVEN EOU = H &amp; SysRI = H THEN PERFORMANCE = H with High ProbabilityGIVEN EOU = H &amp; SysQI = H &amp; SysRI = H THEN PERFORMANCE = H with High Probability</td></tr><tr><td>SysQI ⇒ Perf</td><td>SysQI has a positive impact on PERFORMANCEGIVEN Util = H THEN SysQI has a positive impact on PERFORMANCEGIVEN Util = M THEN SysQI has a positive impact on PERFORMANCEGIVEN EOU = M THEN SysQI has a positive impact on PERFORMANCEGIVEN Auth = M THEN SysQI has a positive impact on PERFORMANCEGIVEN Auth = H THEN SysQI has a positive impact on PERFORMANCEGIVEN SysRI = H THEN SysQI has a positive impact on PERFORMANCEGIVEN SysRI = L_M THEN SysQI has a positive impact on PERFORMANCEGIVEN SysQI = H &amp; Auth = H THEN PERFORMANCE = H with High ProbabilityGIVEN SysQI = H &amp; Doc = H THEN PERFORMANCE = H with High ProbabilityGIVEN EOU = H &amp; SysQI = H &amp; SysRI = H THEN PERFORMANCE = H with High Probability</td></tr><tr><td>SysRI ⇒ Perf</td><td>SysRI has a positive impact on PERFORMANCEGIVEN EOU = H &amp; SysRI = H THEN PERFORMANCE = H with High ProbabilityGIVEN EOU = H &amp; SysQI = H &amp; SysRI = H THEN PERFORMANCE = H with High Probability</td></tr><tr><td>Util ⇒ Perf</td><td>Util has a positive impact on PERFORMANCEGIVEN Util = H THEN PERFORMANCE = H with High ProbabilityGIVEN Util = H &amp; SysQI = H THEN PERFORMANCE = H with High ProbabilityGIVEN Util = H &amp; SysQI = H &amp; EOU = L_M THEN PERFORMANCE = H with High ProbabilityGIVEN Util = H &amp; SysQI = H &amp; EOU = H THEN PERFORMANCE = H with High Probability</td></tr><tr><td>Auth ⇒ Util</td><td>GIVEN Doc = H THEN Auth has a positive impact on Utilisation</td></tr><tr><td>Doc ⇒ Util</td><td>Doc has a positive impact on UtilisationGIVEN Auth = H &amp; EOU = H THEN Doc has NO impact on Utilisation</td></tr><tr><td>EOU ⇒ Util</td><td>EOU has a positive impact on UtilisationGIVEN SysQI = H THEN EOU has a positive impact on UtilisationGIVEN SysQI = L_M THEN EOU has a positive impact on UtilisationGIVEN Auth = H THEN EOU has a positive impact on UtilisationGIVEN Doc = M THENEOU has a positive impact on UtilisationGIVEN SysRI = H THEN EOU has a positive impact on Utilisation</td></tr></table>

Table 6. cont.

<table><tr><td>Causal link</td><td>Supporting abducted hypotheses</td></tr><tr><td>SysQI ⇒ Util</td><td>GIVEN EOU = H THEN SysQI has a positive impact on UtilisationGIVEN EOU = M THEN SysQI has a positive impact on UtilisationGIVEN SysRI = L THEN SysQI has a positive impact on UtilisationGIVEN SysRI = M THEN SysQI has a positive impact on UtilisationGIVENAuth = M THEN SysQI has a positive impact on UtilisationSysQI has a positive impact on Utilisation</td></tr></table>

High probability: P > t = 0.80.

## 1. Is this DT-based approach defensible from a statistical analysis perspective?

Our DT-based approach generates two types of hypotheses, single rule hypotheses and sibling rules hypotheses, and explanatory models. Hypotheses of these types can be subjected to traditional statistical hypothesis testing procedures. The main differences between these types of hypotheses and those that are typically used in IS studies is that they are derived from and grounded in empirical data, while the traditional ones are typically derived from existing theory and/or the researcher’s imagination.

## 2. Are the hypotheses generated any good and could they be generated by the researcher without this method?

Several of the hypotheses generated by our approach meet the standards set out by Peirce: (1) They identify some connection or relationship in the data that was previously unidentified or over looked. (2) They lead to predictions of phenomena, which until now have not been theorised about and independently investigated. (3) They have been evaluated to ensure their test worthiness. They all satisfy the Peircean posterior probability test that demonstrates that they are likely to be confirmed in empirical testing. The same cannot be said of hypotheses imagined by the researcher. While some of the hypotheses generated by our DT method migh easily be imagined by the researcher, there are several others that are unlikely for a researcher to imagine. For example, hypotheses such as: ‘Authorisation (Auth) has a U-shaped curvilinear impact on Performance’, and ‘Given Authorisation = High and Ease\_of\_Use = High then

Documentation has NO impact on Utilisation’. On close examination, the reader will notice these two hypotheses are relevant to theorising about the phenomena, and can offer advice to managers in organisational situations.

## 3. Does the proposed method offer an important novel contribution?

While it is true that some data mining techniques support hypotheses generation, it does not follow the application of data mining in our paper for the systematic testing of IS theories is not novel. The central contribution of our paper is a general method for exploring the limits of IS theories based on Peirce’s scientific method. Our approach for generating hypotheses involves the use of DT partitioning of the dataset to generate two types of hypotheses: 1) those based on ‘Strong’ rules; and 2) those based on Sibling Rules. To date no previous published work by other authors have used sibling rules to generate hypotheses. Further, we have presented not only a novel method for generating hypotheses but also a procedure for abducting a theoretical model from data.

## 4. Is the proposed method not just simply about data dredging in order to find correlations?

The charge of data dredging is sometimes mistakenly levelled against data mining and exploratory factor analysis. However, this may come from a limited understanding of a class of statistical data analysis methods. In this paper, we use data mining technology to partition the dataset in subsets after which we do traditional statistics-based hypothesis test on the generated rules in order to abduct hypotheses. In this paper, the application of our method in each subset of the dataset consists of at least 30 observations. It should be noted that severa published empirical studies in leading IS journals have involved datasets with barely more observations than we have for our smallest subsets.

## 5. Why use DT’s instead of association rules, neural networks, knowledge maps, etc. for representing hypotheses?

We did experiment with association rules (AR) to generate hypotheses but decided against this course of action for several reasons including: 1) the necessity of doing additional preprocessing; 2) the need to do pruning of the generated set of ARs; 3) the additional processing cost of organising the ARs into sets of sibling rules. In general we found that the DT approach was more cost efficient but equally effective for hypotheses and model generation for IS (and other organisation science) research. We do not claim that DT generation is the only approach for generating hypotheses. It is, however, a convenient approach for generating hypotheses. It is more intuitive for researchers to think of hypotheses in DT; further, it offers a hierarchical structuring of the rule-set, which facilitates easy identification of sets of sibling rules. Concep tually and pragmatically, DTs offered a structure upon which we were able to build a novel and effective methodology for generating hypotheses and a procedure for abducting theoretica models from data based on the Peircian epistemological principles.

## 6. Given that the proposed method involves data mining of a single set of already predefined independent and dependent, is it not more inductive than abductive, and also more deductive than abductive?

If the proposed method was simply about DT generation then the answer to this question would be ‘Yes’. But we have successfully developed an approach to operationlising Peirce’s scientific methodology. Further, our use of DT rules to generate hypotheses follows Peircian abduction. Consider a Sibling Rules Hypothesis, in order to generate one we do traditional hypothesis testing of a set of associated surrogate hypotheses, each of which is based on a pair of sibling rules from the given rule-set. Only if all of the given surrogate hypotheses are accepted do we generate the given Sibling Rules Hypothesis because the evidence suggests that it is likely to be valid. It should be noted that we do not say that the given hypothesis is valid because its associated surrogate rules are valid. That would be deduction. Our approach appropriatel confirms to the abductive inference outlined by Peirce (CP. 1931–58; see also Fann, 1970).

## 7. Data mining is typically applied to data sets, which were developed for a different purpose than that of constructing inferential statements. Is it really appropriate to apply data mining to survey data?

The idea that inferential statements should be limited to some special class of empirica observations of any phenomena is an ideological misrepresentation of basic principles of scientific inquiry. As Popper pointed out in The Aim of Science (Popper, 1957), the objective is to render theoretical explanations about empirical observations of relevance in our world (see also Hempel, 1965; Hintikka, 1968; Tuomela, 1985). It should also be noted that the data in organisational databases (commercial, economic, medical, environmental, etc.) upon which we now routinely apply data mining to make plans and decisions were not in all cases initially collected with the objective that such data could be subjected to data mining exploration. Rather it is the availability of both data and data mining technology that provides the opportunity for data mining exploration, which has advanced our scientific knowledge in many branches of science, from predicting natural disasters to developing new understandings of old diseases in new ways.

## 8. Can the average IS researcher use this method and will it make scientific work more productive?

Our method is general and applicable to any type of positivist theory development in IS research. It can be implemented using many data mining software packages (e.g. C5.0, SAS Enterprise Miner, IBM Intelligent Miner), which provide facilities for the generation of DTs a relatively easy task. Given this fact, a major decision to be made by the researcher is the determination of target events (e.g. Performance is in the [5.5–7.0] interval) that are of interest Once this decision has been made, many DM software provide convenient facilities for discretising the variables. Alternately, the discretisation could be done using readily available data analysis tools such as in Excel. Further, all of the statistical testing for evaluating the generated hypotheses can be done automatically within the data mining software, if the researcher specifies the necessary tests and appropriate parameters.

To summarise, our objective in this research was to develop a method of hypotheses generation and evaluation based on Peircian epistemology. We wanted to help overcome the problem of the paucity of hypotheses for theory development in the positivist approach pointed by Popper and others. In this regard, we have developed a methodology based on Pierce’s theory of abduction and implemented it using DT generation technology. Our DT-based approach provides the researcher with a decision support environment in which he/she can automatically generate and evaluate a very large number of hypotheses in a relatively small amount of time. The approach promises significant savings in terms of the time and cost of conducting systematic theory testing and development. In addition to generating meaningful hypotheses that are likely to be valid in future empirical testing, another important contribution of our approach is the ability to understand the functional form of causal relationships. This understanding would assist the researcher in making appropriate choices of statistical methods for testing hypotheses. For example, if the researcher comes to understand from using our method that certain causal relationships are non-linear, then he/she she would know that linear data analytic methods (such as PLS approaches) are not adequate for interrogating them. It has already been shown that when linearity is incorrectly assumed for theoretica model relationships, empirical findings are often contradictory, confounding or incorrect (Ko & Osei-Bryson, 2004a; b). But the general practice of most positivist IS research is to assume that all relationships in theoretical models are linear and unconditional. Our approach could assist the researcher in discovering the correct functional form of the relationships, and as a consequence, make appropriate choices of statistical methods for testing the hypothetical models. Finally, our approach could be used in a complementary manner with the current dominant approach to confirmatory analysis. For example, given a dataset that has been previously used by a researcher for confirmatory data analysis, our DT-based approach could be used to abduct new hypotheses that would be used in future research using new datasets. In this regard, our research offers a robust methodology which helps to advance the development of scientific theories and knowledge reproduction in our field.

## ACKNOWLEDGEMENTS

This research project from which this work derives was started in 2000 when both researchers were employed in the Information Systems Department, School of Business, Virginia Commonwealth University which provided summer Research Grants in 2001, 2002, 2007 and 2010. The research also benefited from grants (2005, 2006, 2008) from the Associate Dean for Research, Ted Rogers School of Management, Ryerson University.

## REFERENCES

Bailey, J.E. & Pearson, S.W. (1993) Development of a too for measuring and analyzing computer user satisfaction. Management Science, 29, 530–545.

Benbasat, I. & Zmud, R. (1999) Empirical research in information systems: the practice of relevance. MIS Quarterly, 1, 3–16.

Brusic, V. & Zeleznikow, J. (1999) Knowledge discovery and data mining in biological databases. Knowledge Engineering Review, 14, 257–277.

Carnap, R. (1953) Testability and Meaning. In: Readings in the Philosophy of Science, Feigel H. & Broddeck M. (eds.), pp. 47–92. Appleton-Century-Crofts, New York, NY, USA.

Chalmers, A.F. (1994) What Is This Thing Called Science? 3rd edn. Hackett Publishing Company, Indianapolis, IN, USA.

Davenport, T. & Markus, L. (1999) Rigor and relevance revisited: a response to Benbasat and Zmud. MIS Quarterly, 23, 19–23.

Day, T. & Kincaid, H. (1994) Putting inference to the best explanation in its place. Synthese, International Journa for Epistemology, Methodology and Philosophy of Science, 98, 271–295.

DeLone, W.H. & McLean, E.R. (1992) Information systems success: the quest for the dependent variable. Information Systems Research, 3, 60–95.

Dipert, R. (1995) Peirce’s underestimated role in the history of logic. In: Peirce and Contemporary Thought, Ketner, K. (ed.), pp. 32–58. Fordham University Press, New York, NY, USA.

Dishaw, M.T. & Strong, D.M. (1999) Extending the technology acceptance model with task-technology fit constructs. Information & Management, 36, 9–21

Doll, W.J. & Torkzadeh, G. (1988) The measurement of end-user computing satisfaction. MIS Quarterly, 12, 259–274.

Doll, W.J., Xia, W. & Torkzadeh, G. (1994) A confirmatory factor analysis of the end-user computing satisfaction instrument. MIS Quarterly, 18, 453–461.

Etezadi-Amoli, J. & Farhoomand, A.F. (1996) A structura model of end user computing satisfaction and user performance. Information & Management, 30. 65–73

Fann, K.T. (1970) Peirce’s Theory of Abduction. Martinu Nijhoff, Amsterdam, The Netherlands.

Flach, P.A. (2000) On the logic of hypothesis generation. In: Abduction and Induction: Essays on Their Relation and Integration, Flach, P.A. & Kakas, A.C.

(eds.), pp. 89–106. Kluwer Academic Publishers, The Netherlands.

Flach, P.A. & Kakas, A.C. (eds.) (2000) Abduction and Induction: Essays on Their Relation and Integration. Kluwer Academic Publishers, The Netherlands

Goodhue, D.L. (1995) Understanding user evaluations of information systems. Management Science, 41, 1827– 1844.

Goodhue, D.L. & Thompson, R.L. (1995) Task-technology fit and individual performance. MIS Quarterly, 19, 213– 236.

Grimes, T.R. (1990) Truth, content, and the Hypothetico Deductive method. Philosophy of Science, 57, 514–522.

Hanson, N.R. (1961) Is there a logic of discovery. In: Current Issues in The Philosophy of Science, Feigle, H. & Maxwell, G. (eds.), pp. 20–35. Holt, Rinehart and Winston. Austin. TX. USA

Harman, G. (1965) Inference to the best explanation. The Philosophical Review, 74, 88–95.

Hempel, C.G. (1965) Aspects of Scientific Explanation. The Free Press, NY, USA.

Hintikka, J. (1968) The varieties of information and scien tific explanation. In: Logic, Methodology and Philosophy of Science III, van Rootselaar, B. & Staal, J.F. (eds.), pp. 151–171. North-Holland Publishing Co., Amsterdam.

Hintikka, J. (1997) The place of C.S. Peirce in the history o logical theory. In: Lingua Universalis Vs. Calculus Ratio cinator, Selected Papers 2, pp. 140–161. Kluwer Aca demic Publishers, The Netherlands.

Igbaria, M. & Tan, M. (1997) The consequences of infor mation technology acceptance on subsequent individua performance. Information & Management, 32, 113–121.

Kim, H. & Koehler, G. (1995) Theory and practice of deci sion tree induction. Omega, 23, 637–652.

Ko, M. & Osei-Bryson, K.M. (2004a) Exploring the relation ship between information technology investments and firm performance productivity using regression splines analysis. Information & Management, 42, 1–13

Ko, M. & Osei-Bryson, K.M. (2004b) Using regression splines to assess the impact of information technology investments on productivity in the health care industry. Information Systems Journal. 14. 43–63

Lakatos, I. (1974) Falsification and the methodology of scientific research programs. In: Criticism and The Growth of Knowledge, Lakatos I. & Musgrave A. (eds.), pp. 91–195. Cambridge University Press, Cambridge, UK.

Lee, C. & Irizarry, K. (2001) The gene mine system for genome/proteome annotation and collaborative data mining. IBM Systems Journal, 40, 592–603.

Magnani, L. (2001) Abduction, Reason, and Science: Processes of Discovery and Explanation, Springer, New York, USA.

Mathieson, K. & Keil, M. (1998) Beyond the interface: ease of use and task/technology fit. Information & Management, 34, 221–230.

Niiniluoto, I. (1993) Peirce’s theory of statistical explanation. In: Charles S. Peirce and the Philosophy of Science, Moore, E.C. (ed.), pp. 186–207. The University of Alabama Press, Tuscaloosa, AL, USA and London, UK.

Niiniluoto, I. (1999) Defending abduction. Proceedings of Philosophy of Science, 66, S436–S451.

Niiniluoto, I., & Tuomela, R. (1973) Theoretical Concepts and Hypothetico-Inductive Inference, D. Reidel Pub. Co. Boston, USA.

Pagnucco, M. (1996) The role of abductive reasoning in the process of belief revision. Ph.D. Dissertation, University of Sidney, Australia.

Palys, T.S. (2003) Research Decisions: Quantitative and Qualitative Perspectives, 3rd edn. Nelson, Scarborough, UK.

Peirce, C.S. (1931–1958) Collected Papers of Charles Sanders Peirce, Vol. 1–8, Hartshorne, C., Weiss, P. & Burks, A. (eds.), Harvard University Press, Harvard, USA.

Popper, K.R. (1957) The aim of science. Ratio, 1, 24–35.

Popper, K. (1963) Conjectures and Refutations: The Growth of Scientific Knowledge, Routledge and Kegan Paul, London, UK.

Popper, K.R. (1968) The Logic of Scientific Discovery Harper Torch Books, New York, NY, USA.

Putnam, H. (1982) Peirce the logician. Historia Mathematica, 9, 290–301.

Salmon, W.C. (1989) Four Decades of Scientific Explanation, University of Minnesota Press, Minneapolis.

Quine, W.V. (1995) Peirce’s logic. In: Peirce and Contemporary Thought, Ketner, K.L. (ed.), pp. 23–31. Fordham, New York. NY. USA

Quinlan, J.R. (1986) Induction of decision trees. Machine Learning, 1, 81–106.

Shanahan, M. (1989) Prediction is deduction but explanation is abduction. Proceedings of the 11th International Joint Conference on Artificial Intelligence, Detroit, pp. 1055–1060.

Thagard, R. (1978) The best explanation: criteria for theor choice. Journal of Philosophy, 65, 76–92.

Torkzadeh, G. & Doll, W.J. (1991) Test-retest reliability of the end-user computing satisfaction instrument. Decision Sciences, 22, 26–37.

Tuomela, R. (1985) Truth and best explanation. Erkennt nis, 22, 271–299.

Tursman, R. (1987) Peirce’s Theory of Scientific Discov ery. Indiana University Press, Bloomington, IN, USA.

Zmud, R. (1996) Editors comments: on rigor and rel evance. MIS Quarterly, 20, xxxvii–xxxviii

## Biographies

Kweku-Muata Osei-Bryson is Professor of Informatior Systems at Virginia Commonwealth University in Richmond, VA where he also served as PhD Program Coordi nator from 2001–2003. Previously, he was Professor of Information Systems & Decision Sciences at Howard University in Washington, DC. He holds a Ph.D. in Applied Mathematics (Management Science & Information Systems) from the University of Maryland at College Park. He has published in various leading journals including: Information Systems Journal, Information Sciences, Infor mation & Management. Journal of the Association for Information Systems, European Journal of Information Systems, Expert Systems with Applications, Information Systems Frontiers, Journal of Database Management, Data & Knowledge Engineering, Decision Support Systems, Expert Systems with Applications, Computers & Operations Research and the European Journal of Operational Research. He serves as an Associate Editor of the INFORMS Journal on Computing, on the Editorial Board of the Computers & Operations Research Journal and the International Advisory Board of the Journal of the Operational Research Society.

Ojelanki Ngwenyama is Director of the Institute fo Innovation and Technology Management, Ted Rogers School of Management, Ryerson University. He holds an MSc. from Roosevelt University; MBA from Martin J. Withman School of Management, Syracuse University; a Ph.D. from Thomas J. Watson School of Engineering, State University of New York; and a D.Phil (honoris causa, 2009) from the Faculty of Engineering, University of Pretoria, South Africa. His papers have appeared in a range of international scholarly journals. He is a member of the Editorial Boards of the Scandinavian Journal of Information System, Journal of Information Technology for Development and Information Systems Journal. Ojelanki has been a member of IFIP Working Group 8.2 (Organization and Societal Implications of Information Systems) since 1986. ojelanki@ryerson.ca.

## APPENDIX A

## The three inferential logics Peirce illustrated with the Barbara syllogism:

In his Lowell Lectures Peirce (1866) used the Barbara syllogism to illustrate the differences among the three inferential logics. In his view all three are necessary for systematic scientific inquiry (abduction for proposing hypotheses; deduction for deriving the consequences of the hypotheses; and induction for testing and verification of the hypotheses). He illustrated the three inferential logics as follows:

A1. Deduction is the inference of a result from a rule and a case:

Rule – All beans from this bag are white

Case – These beans are from this bag

Result – These beans are white

A2. Induction is the inference of a rule from the result and case:

Result – These beans are white

Case – These beans are from this bag

Rule – All beans from this bag are white

A3. Abduction is the inference of the case from the rule and the result:

Rule – All beans from this bag are white.

Result – These beans are white.

Case – These beans are from this bag.

## APPENDIX B

## Definition of questionnaire variables

(1) CASEID – is a unique number for each case/record.

(2) COUNTRY – (1) USA (2) Thailand

(5) CURR – The data provide by the system is up-to-date enough for my purposes.

(6) RDATA – The system available to me is missing critical data that are very useful to me in my job.

(7) RDETAIL – The system maintains data at an appropriate level of detail for my group’s tasks.

(8) MEAN – The exact definition of data fields relating to my tasks is easy to find out.

(9) AUTH1 – Data that would be useful to me are unavailable because I don’t have the righ authorisation.

(10) AUTH2 – Getting authorisation to access data that would be useful in my job is time consuming and difficult.

(11) RELIA1 – The system I use is subjected to unexpected or inconvenient down times which makes it harder to do my work.

(12) RELIA2 – The system I use is subject to frequent system problems and crashes.

(13) EOU1T – It is easy to learn how to use the system.

(14) EOU2T – The system I use is convenient and easy to use.

(15) TRAIN – There is not enough training for me or my staff on how to find, understand, access or use the system.

User satisfaction instrument (1)

(16) CONT1 – The system provides the precise information I need.

(17) CONT2 – The information contents provided by the system meet my needs.

(18) CONT3 – The system provides reports that seem to be exactly what I need.

(19) CONT4 – The system provides sufficient information to my needs.

(20) ACCU1 – The system is accurate.

(21) ACCU2 – I am satisfied with the accuracy of the system.

(22) FOR1 – The output is presented in a useful format.

(23) FOR2 – The information is clear.

(24) TIME – The system provides me the information I need in a timely manner.

User satisfaction instrument (2)

(25) DOC1 – The content of the user manual is useful.

(26) DOC2 – The index of the user manual is useful.

(27) DOC3 – The user manual is current (i.e. up-to-date).

(28) DOC4 – The user manual is complete.

(29) DOC5 – The user manual is easy to understand and follow.

(30) EOU1U – The description of the functions/ commands displayed on screen is clear to me.

(31) EOU2U – The function/command names are easy to remember.

(32) FUNC1 – The system provides complete features I need.

(33) FUNC2 – I am satisfied with the speed of interacting with the system.

(34) FUNC3 – It is easy to detect possible errors in the systems.

(35) FUNC4 – It is easy to correct errors that happen in the systems.

(36) FUNC5 – It is easy to change the output format.

(37) SUPP1 – I am satisfied with the amount of support provided by vendor or other sources.

(38) SUPP2 – I am satisfied with the availability of information systems staff for consultation.

## Utilisation

(39) UTIL1 – Currently, I cannot accomplish my tasks without the systems.

(40) UTIL2 – If I have a choice to use any systems to perform my tasks, I still prefer to use the current system

Performance

(41) PERFO1 – The system helps me to be more effective

(42) PERFO2 – The system has a positive impact on my productivity in my job

(43) PERFO3 – The system is an important aid to me in the performance of my job.

Demographic and support information

(44) INDUS – industry that the organisations are in

(45) EDUC – Education level

(46) LWCOMP – Years work in the company

(47) LWJOB – Years work in the current job

(48) LWSYS – years work with the system in consideration

(49) MGRLEVEL – management level

(50) SYSTEM – similar to ID but more detail in that non- are decomposed into software package, in-house system, and customise package

(51) MODULE – the system module that participants use the most

## APPENDIX C

## Procedure for implementing the methodology

Step 1: Preparation (Researcher):

a. Identify Dependent variables: Identify dependent variables (e.g. Performance)

b. Identify Possible Mediator variables: Identify possible mediator variables (e.g. Utilisation).

c. Specify the Discretisation Method. An example of such a method is presented in Table 2.

d. Identify the Target Events for the Dependent & Mediator Variables: For each dependent variable, identify target events (e.g. Performance is High ≡ the value of Performance is in the [5.5–7] interval) that may be of interest. Do similarly for the Mediator variable(s).

e. Discretise All Ordinal Variables: For each ordinal variable, discretise the given variable using the specified Discretisation Method.

f. Specify DT Generation Parameters: Specify relevant values for data partitioning parameters (e.g. distribution of cases in training, validation and test datasets; stratification variables), DT induction parameters (e.g. splitting method options, minimum observations per leaf).

g. Specify Thresholds: Specify a, the significance level for statistical testing of the hypotheses, and $\tau _ { 0 } ,$ the threshold for $p _ { 0 } .$ . A Strong Single Rule Hypothesis will not be generated for any rule for which the highest $p _ { 0 }$ that is supported by the data is below $\tau _ { 0 } .$

h. Specify the Set of Selection Rules for Abducting and Evaluating Sibling Rules Hypotheses: A candidate sibling rules hypothesis is formulated based on the relative frequency distribution of the target event for the set of sibling rules that are associated with the predictor variable. Appendix D provides example of a Set of Selection Rules for Formulating and Evaluating Candidate Sibling Rules Hypotheses.

## Step 2: Hypotheses generation for dependent variables (automatic):

For each dependent variable:

Substep 2a: Generate DTs for Dependent Variables: Generate a set of DTs using the discretised dataset and the combination of DT generation parameter values that were specified in Step 1.

Substep 2b: Abduct and Evaluate Sibling Rules Hypotheses for Dependent Variables: In this substep, for each DT a sibling rules hypothesis will be abducted for each set of sibling rules if the relationship between the associated relative frequencies is included in the Set of Selection Rules for Formulating and Evaluating Candidate Sibling Rules Hypotheses. Each such abducted Sibling Rules Hypothesis is indirectly evaluated by subjecting the associated set of surrogate hypotheses to statistical testing. If they are all accepted then there is good reason to believe that the Sibling Rules Hypothesis will not be rejected, and so it is not rejected.

Substep 2c: Abduct Strong Single Rule Hypotheses for Dependent Variables: For each sibling rule that is statistically different from each of its other sibling rules at significance level $\mathbf { \alpha } _ { \mathbf { 0 } } ,$ determine if it is a strong rule by testing the surrogate hypothesis: $p _ { 0 } \geq \tau _ { 0 } .$ For each such surrogate hypothesis that is accepted, use the given rule to abduct a corresponding Strong Single Rule Hypothesis.

## Step 3: Identify mediator variables (automatic)

Examine the set of supported hypotheses from Step 2 to determine if any potential mediator variable is included at least one of the abducted hypotheses for one of the dependent variables.

## Step 4: Generate hypotheses for mediator variables (automatic)

Step 4 is executed for each mediator variable that was included in a condition event of a hypothesis for one of the dependent variables. If there is no such mediator variable then this step is bypassed.

For each mediator variable:

Substep 4a: Generate DTs for Predicting Mediator Variables. Similar to Substep 2a.

• Substep 4b: Abduct Sibling Rules Hypotheses for Mediator Variables. Similar to Substep 2b.

Substep 4c: Abduct Strong Single Rule Hypotheses for Mediator Variables. Similar to Substep 2c.

## Step 5: Abduction of theoretical model (automatic):

Generate a theoretical model by integrating the set of causal links between predictor and target variables that are associated with the abducted directional and Single Rule Hypotheses.

## APPENDIX D

Examples of decision rules for formulating and evaluating candidate sibling rules hypotheses

Assuming a discretised target variable with 3 bins, Table D1 below could be used to formulate and test a candidate sibling rules hypothesis of the form: Predictor variable X has {Impact Type} on Target variable Y.

Table D1. Example of decision rules for formulating candidate sibling rules hypotheses

<table><tr><td>Impact type</td><td>Relationships between relative frequencies</td><td>Set of surrogate hypotheses that must each be accepted</td></tr><tr><td>a Positive Impact</td><td> $f_{H} > f_{M} > f_{L}$ </td><td> $(p_{H} > p_{M}) \& (p_{M} > p_{L})$ </td></tr><tr><td>a Positive Impact</td><td> $f_{H} > f_{L\_M}$ </td><td> $p_{H} > p_{L\_M}$ </td></tr><tr><td>a Negative Impact</td><td> $f_{H} < f_{M} < f_{L}$ </td><td> $(p_{H} < p_{M}) \& (p_{M} < p_{L})$ </td></tr><tr><td>a Negative Impact</td><td> $f_{H} < f_{L\_M}$ </td><td> $p_{H} > p_{L\_M}$ </td></tr><tr><td>U-shaped symmetric curvilinear impact</td><td> $(f_{L} > f_{M}) \& (f_{H} > f_{M})$ </td><td> $(p_{L} > p_{M}) \& (p_{H} > p_{M})$ </td></tr><tr><td>Inverted U-shaped symmetric curvilinear impact</td><td> $(f_{L} < f_{M}) \& (f_{H} < f_{M})$ </td><td> $(p_{L} > p_{M}) \& (p_{H} > p_{M})$ </td></tr><tr><td>No impact</td><td></td><td> $(p_{L} \approx p_{M}) \& (p_{M} \approx p_{H})$ </td></tr><tr><td>No impact</td><td></td><td> $p_{H} \approx p_{L\_M}$ </td></tr></table>

## APPENDIX E

## Evaluated candidate sibling rules hypotheses for dependent variable

Table E1. Performance – candidate sibling rules hypotheses

<table><tr><td rowspan="2">DT</td><td colspan="2">Condition events</td><td rowspan="2">N</td><td rowspan="2">Rel. freq (f)</td><td colspan="3">Surrogate hypotheses</td><td rowspan="2">Abduct?</td><td rowspan="2">Candidate sibling rules hypothesis</td></tr><tr><td>Backend</td><td>Frontend</td><td>Hyp</td><td>t-stat</td><td>Dec</td></tr><tr><td rowspan="3">A1E</td><td></td><td>Util = L</td><td>45</td><td>0.200</td><td> $p_{M} > p_{L}$ </td><td>2.77</td><td>A</td><td rowspan="3">YES</td><td rowspan="3">Util has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>Util = M</td><td>328</td><td>0.415</td><td> $p_{H} > p_{M}$ </td><td>10.77</td><td>A</td></tr><tr><td></td><td>Util = H</td><td>192</td><td>0.896</td><td> $p_{H} > p_{L}$ </td><td>9.89</td><td>A</td></tr><tr><td rowspan="2">A1E</td><td>Util = H</td><td>SysQI = L_M</td><td>59</td><td>0.678</td><td> $p_{H} > p_{L\_M}$ </td><td>6.56</td><td>A</td><td rowspan="2">YES</td><td rowspan="2">GIVEN Util = H THEN SysQI has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>SysQI = H</td><td>133</td><td>0.992</td><td></td><td></td><td></td></tr><tr><td rowspan="2">A1E</td><td>Util = H &amp; SysQI = H</td><td>EOU = L_M</td><td>47</td><td>0.979</td><td> $p_{H} > p_{L\_M}$ </td><td>1.34</td><td>R</td><td rowspan="2">NO</td><td rowspan="2">GIVEN Util = H &amp; SysQI = H THEN EOU has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>EOU = H</td><td>85</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td rowspan="2">A1E</td><td>Util = M</td><td>SysQI = L_M</td><td>231</td><td>0.316</td><td> $p_{H} > p_{L\_M}$ </td><td>5.59</td><td>A</td><td rowspan="2">YES</td><td rowspan="2">GIVEN Util = M THEN SysQI has a positive impact on PERFORMANCE</td></tr><tr><td>Util = M</td><td>SysQI = H</td><td>97</td><td>0.649</td><td></td><td></td><td></td></tr></table>

Table E1. cont.

<table><tr><td rowspan="2">DT</td><td colspan="2">Condition events</td><td rowspan="2">N</td><td rowspan="2">Rel. freq (f)</td><td colspan="3">Surrogate hypotheses</td><td rowspan="2">Abduct?</td><td rowspan="2">Candidate sibling rules hypothesis</td></tr><tr><td>Backend</td><td>Frontend</td><td>Hyp</td><td>t-stat</td><td>Dec</td></tr><tr><td rowspan="3">A1E</td><td rowspan="3">Util = M &amp; SysQI = L_M</td><td>Auth = L</td><td>44</td><td>0.394</td><td> $p_{L}>p_{M}$ </td><td>1.80</td><td>A</td><td>YES</td><td>GIVEN Util = M &amp; SysQI = L_M THEN</td></tr><tr><td>Auth = M</td><td>157</td><td>0.255</td><td> $p_{H}>p_{M}$ </td><td>2.89</td><td>A</td><td></td><td rowspan="2">Auth has a U-shaped curvilinear impact on PERFORMANCE</td></tr><tr><td>Auth = H</td><td>41</td><td>0.488</td><td> $p_{H}=p_{L}$ </td><td>0.87</td><td>A</td><td></td></tr><tr><td rowspan="2">B1G</td><td rowspan="2"></td><td>SysQI = L_M</td><td>329</td><td>0.365</td><td> $p_{H}>p_{L\_M}$ </td><td>11.10</td><td>A</td><td>YES</td><td rowspan="2">SysQI has a positive impact on PERFORMANCE</td></tr><tr><td>SysQI = H</td><td>236</td><td>0.835</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">B1G</td><td rowspan="3">SysQI = L_M</td><td>EOU = L</td><td>44</td><td>0.250</td><td> $p_{M}>p_{L}$ </td><td>1.22</td><td>R</td><td>NO</td><td rowspan="3">GIVEN SysQI = L_M THEN EOU has a positive impact on PERFORMANCE</td></tr><tr><td>EOU = M</td><td>250</td><td>0.344</td><td> $p_{H}>p_{M}$ </td><td>3.57</td><td>A</td><td></td></tr><tr><td>EOU = H</td><td>35</td><td>0.657</td><td> $p_{H}>p_{L}$ </td><td>3.63</td><td>A</td><td></td></tr><tr><td rowspan="3">B1G</td><td rowspan="3">SysQI = L_M &amp; EOU = M</td><td>Auth = L_M</td><td>199</td><td>0.302</td><td> $p_{H}>p_{L\_M}$ </td><td>2.79</td><td>A</td><td>YES</td><td rowspan="3">GIVEN SysQI = L_M &amp; EOU = M THEN</td></tr><tr><td>Auth = H</td><td>51</td><td>0.510</td><td></td><td></td><td></td><td></td></tr><tr><td>Auth = H</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">B1E</td><td rowspan="3"></td><td>EOU = L</td><td>48</td><td>0.250</td><td> $p_{M}>p_{L}$ </td><td>2.92</td><td>A</td><td>YES</td><td rowspan="3">Auth has a positive impact on PERFORMANCE</td></tr><tr><td>EOU = M</td><td>359</td><td>0.473</td><td> $p_{H}>p_{M}$ </td><td>7.85</td><td>A</td><td></td></tr><tr><td>EOU = H</td><td>158</td><td>0.842</td><td> $p_{H}>p_{L}$ </td><td>7.87</td><td>A</td><td></td></tr><tr><td rowspan="5">B1E</td><td rowspan="5">EOU = M</td><td>SysQI = L_M</td><td>250</td><td>0.344</td><td> $p_{H}>p_{L\_M}$ </td><td>7.76</td><td>A</td><td>YES</td><td rowspan="2">GIVEN EOU = M THEN</td></tr><tr><td>SysQI = H</td><td>109</td><td>0.789</td><td></td><td></td><td></td><td></td></tr><tr><td>Auth = L</td><td>65</td><td>0.620</td><td> $p_{M}>p_{L}$ </td><td>-2.21</td><td>R</td><td>NO</td><td rowspan="3">Auth has a positive impact on PERFORMANCE</td></tr><tr><td>Auth = M</td><td>332</td><td>0.470</td><td> $p_{H}>p_{M}$ </td><td>5.53</td><td>A</td><td></td></tr><tr><td>Auth = H</td><td>168</td><td>0.730</td><td> $p_{H}>p_{L}$ </td><td>1.64</td><td>R</td><td></td></tr><tr><td rowspan="3">T1G1</td><td rowspan="3"></td><td>Auth = L</td><td>65</td><td>0.620</td><td> $p_{L}>p_{M}$ </td><td>2.21</td><td>A</td><td>YES</td><td rowspan="3">Auth has a symmetric U-shaped curvilinear impact on PERFORMANCE</td></tr><tr><td>Auth = M</td><td>332</td><td>0.470</td><td> $p_{H}>p_{M}$ </td><td>5.53</td><td>A</td><td></td></tr><tr><td>Auth = H</td><td>168</td><td>0.730</td><td> $p_{H}=p_{L}$ </td><td>1.64</td><td>A</td><td></td></tr><tr><td rowspan="4">T1G1</td><td rowspan="4">Auth = M</td><td>SysQI = L_M</td><td>217</td><td>0.300</td><td> $p_{H}>p_{L\_M}$ </td><td>8.34</td><td>A</td><td>YES</td><td rowspan="2">GIVEN Auth = M THEN</td></tr><tr><td>SysQI = H</td><td>115</td><td>0.780</td><td></td><td></td><td></td><td></td></tr><tr><td>Auth = H</td><td>69</td><td>0.490</td><td> $p_{H}>p_{L\_M}$ </td><td>5.72</td><td>A</td><td>YES</td><td rowspan="2">GIVEN Auth = H THEN</td></tr><tr><td>SysQI = H</td><td>99</td><td>0.890</td><td></td><td></td><td></td><td></td></tr></table>

Table E1. cont.

<table><tr><td rowspan="2">DT</td><td colspan="2">Condition events</td><td rowspan="2">N</td><td rowspan="2">Rel. freq (f)</td><td colspan="3">Surrogate hypotheses</td><td rowspan="2">Abduct?</td><td rowspan="2">Candidate sibling rules hypothesis</td></tr><tr><td>Backend</td><td>Frontend</td><td>Hyp</td><td>t-stat</td><td>Dec</td></tr><tr><td rowspan="3">T1G2</td><td></td><td>Doc = L</td><td>49</td><td>0.306</td><td> $p_M > p_L$ </td><td>2.87</td><td>A</td><td rowspan="3">YES</td><td rowspan="3">Doc has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>Doc = M</td><td>413</td><td>0.523</td><td> $p_H > p_M$ </td><td>5.75</td><td>A</td></tr><tr><td></td><td>Doc = H</td><td>103</td><td>0.835</td><td> $p_H > p_L$ </td><td>6.46</td><td>A</td></tr><tr><td rowspan="3">T1G2</td><td>Doc = M</td><td>Auth = L</td><td>51</td><td>0.627</td><td> $p_L > p_M$ </td><td>2.55</td><td>A</td><td rowspan="3">YES</td><td>GIVEN Doc = M THEN</td></tr><tr><td></td><td>Auth = M</td><td>246</td><td>0.431</td><td> $p_H > p_M$ </td><td>4.28</td><td>A</td><td rowspan="2">Auth has a symmetric U-shaped curvilinear impact on PERFORMANCE</td></tr><tr><td></td><td>Auth = H</td><td>116</td><td>0.672</td><td> $p_H = p_L$ </td><td>0.56</td><td>A</td></tr><tr><td rowspan="2">T1G3</td><td></td><td>SysRI = L_M</td><td>383</td><td>0.500</td><td> $p_H > p_{L\_M}$ </td><td>4.25</td><td>A</td><td rowspan="2">YES</td><td rowspan="2">SysRI has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>SysRI = H</td><td>182</td><td>0.690</td><td></td><td></td><td></td></tr><tr><td rowspan="2">T1G3</td><td>SysRI = H</td><td>SysQI = L_M</td><td>79</td><td>0.440</td><td> $p_H > p_{L\_M}$ </td><td>6.36</td><td>A</td><td rowspan="2">YES</td><td rowspan="2">GIVEN SysRI = H THEN SysQI has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>SysQI = H</td><td>103</td><td>0.880</td><td></td><td></td><td></td></tr><tr><td rowspan="2">T1G3</td><td>SysRI = L_M</td><td>SysQI = L_M</td><td>250</td><td>0.340</td><td> $p_H > p_{L\_M}$ </td><td>8.57</td><td>A</td><td rowspan="2">YES</td><td rowspan="2">GIVEN SysRI = L_M THEN SysQI has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>SysQI = H</td><td>133</td><td>0.800</td><td></td><td></td><td></td></tr><tr><td rowspan="2">T1G3</td><td>SysRI = H &amp; SysQI = H</td><td>EOU = L_M</td><td>41</td><td>0.800</td><td> $p_H > p_{L\_M}$ </td><td>2.17</td><td>A</td><td rowspan="2">YES</td><td rowspan="2">GIVEN SysRI = H &amp; SysQI = H THEN EOU has a positive impact on PERFORMANCE</td></tr><tr><td></td><td>EOU = H</td><td>62</td><td>0.940</td><td></td><td></td><td></td></tr></table>

(For the column ‘Dec’ (Decision): A = Accept; R = Reject).

## APPENDIX F

## Evaluated candidate sibling rules hypotheses for mediator variable

Table F1. Utilisation – candidate sibling rules hypotheses

<table><tr><td rowspan="2">DT</td><td colspan="2">Condition events</td><td rowspan="2">N</td><td rowspan="2">Rel. freq (f)</td><td colspan="3">Surrogate hypotheses</td><td rowspan="2">Abduct?</td><td rowspan="2">Candidate sibling rules hypothesis</td></tr><tr><td>Backend</td><td>Frontend</td><td>Hyp.</td><td>t-stat</td><td>Dec</td></tr><tr><td rowspan="3">A2E</td><td></td><td>EOU = L</td><td>48</td><td>0.063</td><td> $p_M > p_L$ </td><td>2.90</td><td>A</td><td>YES</td><td rowspan="3">EOU has a positive impact on Utilisation</td></tr><tr><td></td><td>EOU = M</td><td>360</td><td>0.250</td><td> $p_H > p_M$ </td><td>8.13</td><td>A</td><td></td></tr><tr><td></td><td>EOU = H</td><td>157</td><td>0.624</td><td> $p_H > p_L$ </td><td>6.80</td><td>A</td><td></td></tr><tr><td rowspan="2">A2E</td><td>EOU = H</td><td>SysQI = L_M</td><td>35</td><td>0.400</td><td> $p_H > p_{L\_M}$ </td><td>3.11</td><td>A</td><td>YES</td><td>GIVEN EOU = H THEN</td></tr><tr><td></td><td>SysQI = H</td><td>122</td><td>0.689</td><td></td><td></td><td></td><td></td><td>SysQI has a positive impact on Utilisation</td></tr><tr><td rowspan="2">A2E</td><td>EOU = M</td><td>SysQI = L_M</td><td>250</td><td>0.176</td><td> $p_H > p_{L\_M}$ </td><td>4.88</td><td>A</td><td>YES</td><td>GIVEN EOU = M THEN</td></tr><tr><td></td><td>SysQI = H</td><td>110</td><td>0.418</td><td></td><td></td><td></td><td></td><td>SysQI has a positive impact on Utilisation</td></tr><tr><td rowspan="4">A2E</td><td>EOU = M &amp; SysQI = H</td><td>Auth = L_M</td><td>75</td><td>0.395</td><td> $p_H > p_{L\_M}$ </td><td>0.75</td><td>R</td><td>NO</td><td rowspan="2">GIVEN EOU = M &amp; SysQI = H THEN</td></tr><tr><td></td><td>Auth = H</td><td>34</td><td>0.471</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>SysRI = M</td><td>195</td><td>0.154</td><td> $p_H > p_M$ </td><td>2.88</td><td>A</td><td></td><td rowspan="2">Auth has a positive impact on Utilisation</td></tr><tr><td></td><td>SysRI = H</td><td>78</td><td>0.308</td><td> $p_H > p_L$ </td><td>2.75</td><td>A</td><td></td></tr><tr><td rowspan="3">T2G1</td><td></td><td>Auth = L</td><td>65</td><td>0.290</td><td> $p_M > p_L$ </td><td>-0.33</td><td>R</td><td>NO</td><td rowspan="3">Auth has a positive impact on Utilisation</td></tr><tr><td></td><td>Auth = M</td><td>333</td><td>0.270</td><td> $p_H > p_M$ </td><td>5.10</td><td>A</td><td></td></tr><tr><td></td><td>Auth = H</td><td>167</td><td>0.500</td><td> $p_H > p_L$ </td><td>2.89</td><td>A</td><td></td></tr><tr><td rowspan="3">T2G1</td><td></td><td>Auth = L</td><td>65</td><td>0.290</td><td> $p_L > p_M$ </td><td>0.33</td><td>R</td><td>NO</td><td rowspan="3">Auth has a U-shaped symmetric curvilinear impact on Utilisation</td></tr><tr><td></td><td>Auth = M</td><td>333</td><td>0.270</td><td> $p_H > p_M$ </td><td>5.10</td><td>A</td><td></td></tr><tr><td></td><td>Auth = H</td><td>167</td><td>0.500</td><td> $p_H = p_L$ </td><td>2.89</td><td>A</td><td></td></tr><tr><td rowspan="2">T2G1</td><td>Auth = M</td><td>SysQI = L_M</td><td>218</td><td>0.170</td><td> $p_H > p_{L\_M}$ </td><td>5.67</td><td>A</td><td>YES</td><td>GIVEN Auth = M THEN</td></tr><tr><td></td><td>SysQI = H</td><td>115</td><td>0.460</td><td></td><td></td><td></td><td></td><td>SysQI has a positive impact on Utilisation</td></tr><tr><td rowspan="2">T2G1</td><td>Auth = H</td><td>EOU = L_M</td><td>95</td><td>0.290</td><td> $p_H > p_{L\_M}$ </td><td>6.02</td><td>A</td><td>YES</td><td>GIVEN Auth = H THEN</td></tr><tr><td></td><td>EOU = H</td><td>72</td><td>0.760</td><td></td><td></td><td></td><td></td><td>EOU has a positive impact on Utilisation</td></tr><tr><td rowspan="2">T2G1</td><td>Auth = H &amp; EOU = H</td><td>Doc = L_M</td><td>40</td><td>0.790</td><td> $p_H > p_{L\_M}$ </td><td>-0.40</td><td>R</td><td>NO</td><td>GIVEN Auth = H &amp; EOU = H THEN</td></tr><tr><td></td><td>Doc = H</td><td>32</td><td>0.750</td><td></td><td></td><td></td><td></td><td>Doc has a positive impact on Utilisation</td></tr><tr><td rowspan="3">T2G2</td><td></td><td>Doc = L</td><td>49</td><td>0.180</td><td> $p_M > p_L$ </td><td>1.88</td><td>A</td><td>YES</td><td rowspan="3">Doc has a positive impact on Utilisation</td></tr><tr><td></td><td>Doc = M</td><td>414</td><td>0.310</td><td> $p_H > p_M$ </td><td>4.35</td><td>A</td><td></td></tr><tr><td></td><td>Doc = H</td><td>102</td><td>0.540</td><td> $p_H > p_L$ </td><td>4.19</td><td>A</td><td></td></tr><tr><td rowspan="2">T2G2</td><td>Doc = M</td><td>EOU = L_M</td><td>328</td><td>0.220</td><td> $p_H > p_{L\_M}$ </td><td>7.68</td><td>A</td><td>YES</td><td>GIVEN Doc = M THEN</td></tr><tr><td></td><td>EOU = H</td><td>86</td><td>0.650</td><td></td><td></td><td></td><td></td><td>EOU has a positive impact on Utilisation</td></tr><tr><td rowspan="2">T2G2</td><td>Doc = H</td><td>Auth = L_M</td><td>65</td><td>0.430</td><td> $p_H > p_{L\_M}$ </td><td>2.92</td><td>A</td><td>YES</td><td>GIVEN Doc = H THEN</td></tr><tr><td></td><td>Auth = H</td><td>37</td><td>0.730</td><td></td><td></td><td></td><td></td><td>Auth has a positive impact on Utilisation</td></tr></table>

Table F1. cont.

<table><tr><td rowspan="2">DT</td><td colspan="2">Condition events</td><td rowspan="2">N</td><td rowspan="2">Rel. freq (f)</td><td colspan="3">Surrogate hypotheses</td><td rowspan="2">Abduct?</td><td rowspan="2">Candidate sibling rules hypothesis</td></tr><tr><td>Backend</td><td>Frontend</td><td>Hyp.</td><td>t-stat</td><td>Dec</td></tr><tr><td rowspan="3">T2G3</td><td></td><td>SysRI = L</td><td>86</td><td>0.230</td><td> $p_M > p_L$ </td><td>0.74</td><td>R</td><td>NO</td><td rowspan="3">SysRI has a positive impact on Utilisation</td></tr><tr><td></td><td>SysRI = M</td><td>298</td><td>0.270</td><td> $p_H > p_M$ </td><td>5.09</td><td>A</td><td></td></tr><tr><td></td><td>SysRI = H</td><td>181</td><td>0.500</td><td> $p_H > p_L$ </td><td>4.19</td><td>A</td><td></td></tr><tr><td rowspan="2">T2G3</td><td>SysRI = H</td><td>EOU = L_M</td><td>105</td><td>0.340</td><td> $p_H > p_{L\_M}$ </td><td>4.91</td><td>A</td><td>YES</td><td>GIVEN SysRI = H THEN</td></tr><tr><td></td><td>EOU = H</td><td>76</td><td>0.710</td><td></td><td></td><td></td><td></td><td>EOU has a positive impact on Utilisation</td></tr><tr><td rowspan="2">T2G3</td><td>SysRI = M</td><td>SysQI = L_M</td><td>195</td><td>0.150</td><td> $p_H > p_{L\_M}$ </td><td>6.46</td><td>A</td><td>YES</td><td>GIVEN SysRI = M THEN</td></tr><tr><td></td><td>SysQI = H</td><td>103</td><td>0.500</td><td></td><td></td><td></td><td></td><td>SysQI has a positive impact on Utilisation</td></tr><tr><td rowspan="2">T2G3</td><td>SysRI = L</td><td>SysQI = L_M</td><td>56</td><td>0.110</td><td> $p_H > p_{L\_M}$ </td><td>3.75</td><td>A</td><td>YES</td><td>GIVEN SysRI = L THEN</td></tr><tr><td></td><td>SysQI = H</td><td>30</td><td>0.470</td><td></td><td></td><td></td><td></td><td>SysQI has a positive impact on Utilisation</td></tr><tr><td rowspan="2">T2G3</td><td>SysRI = H &amp; EOU = H</td><td>Doc = L_M</td><td>42</td><td>0.740</td><td> $p_H > p_{L\_M}$ </td><td>0.58</td><td>R</td><td>NO</td><td>GIVEN SysRI = H &amp; EOU = H THEN</td></tr><tr><td></td><td>Doc = H</td><td>34</td><td>0.680</td><td></td><td></td><td></td><td></td><td>Doc has an impact on Utilisation</td></tr><tr><td rowspan="2">T2G4</td><td></td><td>SysQI = L_M</td><td>329</td><td>0.180</td><td> $p_H > p_{L\_M}$ </td><td>9.41</td><td>A</td><td>YES</td><td rowspan="2">SysQI has a positive impact on Utilisation</td></tr><tr><td></td><td>SysQI = H</td><td>236</td><td>0.560</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">T2G4</td><td>SysQI = H</td><td>EOU = L_M</td><td>114</td><td>0.410</td><td> $p_H > p_{L\_M}$ </td><td>4.32</td><td>A</td><td>YES</td><td>GIVEN SysQI = H THEN</td></tr><tr><td></td><td>EOU = H</td><td>122</td><td>0.690</td><td></td><td></td><td></td><td></td><td>EOU has a positive impact on Utilisation</td></tr><tr><td rowspan="3">T2G4</td><td>SysQI = L_M</td><td>EOU = L</td><td>44</td><td>0.050</td><td> $p_M > p_L$ </td><td>2.17</td><td>A</td><td>YES</td><td>GIVEN SysQI = L_M THEN</td></tr><tr><td></td><td>EOU = M</td><td>250</td><td>0.180</td><td> $p_H > p_M$ </td><td>3.01</td><td>A</td><td></td><td rowspan="2">EOU has a positive impact on Utilisation</td></tr><tr><td></td><td>EOU = H</td><td>35</td><td>0.400</td><td> $p_H > p_L$ </td><td>3.83</td><td>A</td><td></td></tr></table>

For the column ‘Dec’ (Decision): A = Accept; R = Reject
