---
otero_id: 21788
otero_key: "CCE8MFBQ"
title: "Unexpectedness as a measure of interestingness in knowledge discovery"
authors: "Balaji Padmanabhan; Alexander Tuzhilin"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00053-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Unexpectedness as a measure of interestingness in knowledge discovery

Balaji Padmanabhan <sup>a,)</sup>, Alexander Tuzhilin <sup>b,1</sup>

<sup>a</sup> Operations and Information Management Department, The Wharton School, UniÕersity of PennsylÕania, PennsylÕania, PA, USA <sup>b</sup> Information Systems Department, Stern School of Business, New York UniÕersity, New York, NY, USA

## Abstract

Organizations are taking advantage of ‘‘data-mining’’ techniques to leverage the vast amounts of data captured as they process routine transactions. Data mining is the process of discovering hidden structure or patterns in data. However, several of the pattern discovery methods in data-mining systems have the drawbacks that they discover too many obvious or irrelevant patterns and that they do not leverage to a full extent valuable prior domain knowledge that managers have. This research addresses these drawbacks by developing ways to generate interesting patterns by incorporating managers’ prior knowledge in the process of searching for patterns in data. Specifically, we focus on providing methods that generate unexpected patterns with respect to managerial intuition by eliciting managers’ beliefs about the domain and using these beliefs to seed the search for unexpected patterns in data. Our approach should lead to the development of decision-support systems that provide managers with more relevant patterns from data and aid in effective decision making. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Interestingness of patterns; Unexpectedness; Beliefs; Belief-driven rule discovery

If you do not expect it, you will not find the unexpected, for it is hard to find and difficult.

Heraclitus of Ephesus, 544–484 BC

## 1. Background and research motives

Technological and organizational trends are increasingly leading to knowledge-intensive work environments. The Work of Nations <sup>w</sup> <sup>x</sup> 14 identifies a fundamental stream of work that involves the production of information goods, rather than physical goods. The manager–analyst in these environments is more of a knowledge worker who routinely deals with information to produce value-added information products.

Technological trends have resulted in organizations accumulating enormous amounts of data on several facets of their operations. For example, many organizations such as credit card companies or retailing outlets record every single transaction a customer performs. It has been estimated 12 that businesses<sup>w</sup> <sup>x</sup> generate gigabytes of data every year and that the total quantity of data tracked doubles approximately every 2 years.

Organizations may proactively build a technological infrastructure to capture and store such data. Firms build data warehouses to support various kinds of decision-making tasks such as planning marketing promotions using scanner data on sales. In other cases, the legal environment in many economies may require that organizations collect and maintain operational data such as telephone conversations withŽ clients or credit card transactions that could grow to . enormous proportions. In either case, the data exists and organizations should leverage the data for competitive advantage by distilling potentially valuable ‘‘nuggets’’ of information. A role of intelligent systems in such an environment is to provide an infrastructure that identifies hidden patterns in the gathered data and thereby empower managers to make more effective decisions.

Data mining is the process of discovering hidden structure or patterns in data. There have been many successful data-mining applications 7 in areas such <sup>w</sup> <sup>x</sup> as customer profiling, fraud detection, telecommunications network monitoring and market-basket analysis. These applications are driven by methods that discoÕer patterns in data. Several of these methods such as association rule algorithms 1 are rule-dis-<sup>w</sup> <sup>x</sup> covery methods that discover patterns in the form of IF–THEN rules. <sup>2</sup> In a supermarket transactions data set, for example, rules may indicate patterns such as ‘‘shoppers who buy diapers on Friday tend to buy beer too’’ Ž . IF diaper, friday THEN beer . The discovered rule in this case could be used to plan shelving arrangements — placing beer near diaper shelves may increase sales of beer. In a credit card transactions data set, finding rules of the form IF ² : ² : condition THEN fraudulent\_transaction is valuable, since these rules indicate conditions that result in a fraudulent transaction. There are several commercial data-mining tools 10 that incorporate <sup>w</sup> <sup>x</sup> methods for rule-discovery and these tools are used in as diverse areas such as fraud detection and medical research 10 . In this research, we focus on<sup>w</sup> <sup>x</sup> improving the data-mining task of discovering rules in business data sets.

Data-mining and data-warehousing tools provide an infrastructure in knowledge-intensive work environments that could potentially informate skilled manager analysts. However, several rule discovery approaches proposed in the literature have the following drawbacks.

Ž . 1 These methods often generate a very large number of rules, most of which obvious or irrelevant, that result in a data-mining problem of the second order — the interpretation and evaluation of the discovered rules could be a highly resource-consuming exercise. Recently, researchers from Stanford University 6 applied an association rule generating algorithm to a subset of census data containing about 30,000 records. Their algorithm generated over 20,000 rules from the census data. In their conclusions, they remark 6 :<sup>w</sup> <sup>x</sup>

Looking over the implication rules generated on census data was educational. First, it was educational because most of the rules themselves were not. The rules that came out at the top, were things that were obvious.

Ž . 2 An important objective of data mining is to discover interesting patterns in data. Most of the existing approaches in the literature on knowledge discovery and data mining use objectiÕe measures of interestingness, such as confidence and support 1 ,<sup>w</sup> <sup>x</sup> for the evaluation of the discovered patterns. These objective measures capture the statistical strength of a pattern. It has been argued in Refs. 8,12,16,17<sup>w</sup> <sup>x</sup> that besides objective measures of interestingness, subjectiÕe measures are equally important. These subjective measures, such as unexpectedness <sup>w x</sup> <sup>w</sup> <sup>x</sup> 8,16,17 and actionability 3,12,16,17 , assume that the interestingness of a pattern depends on the decision maker and does not solely depend on the statistical strength of the pattern. Consider the following two patterns in a supermarket transactions data set:

<sup>Ø</sup> The shopping volume on Saturday is greater than the volume on any other day of the week ŽTrue for 98% of the weeks in the data ..

<sup>Ø</sup> When store coupons are available on Friday, these coupons are not used ŽTrue for 60% of the weeks in the data ..

Using the strength objective criteria as the selec- Ž . tion criterion for the interestingness of the rules will result in the first pattern being chosen as ‘‘more interesting’’, since the pattern is true for 98% of the weeks. However, this pattern may be obvious to any domain expert and hence represents little added value.

The Data as a

In contrast, the second pattern is true for only 60% of the weeks, but is unexpected, since it challenges conventional wisdom that a majority of shoppers tend to use coupons at a store if they are available. A subjective criterion such as unexpectedness would, therefore, rate the second pattern as ‘‘more interesting’’ than the first.

Ž .3 Most of the existing algorithms such as CART <sup>w x</sup> <sup>w x</sup> <sup>w</sup> <sup>x</sup> 5 , Apriori 2 , C4.5 13 are primarily data-driven and do not fully exploit domain knowledge and intuition that managers in a business environment have. Managerial intuition develops over several years of experience and could be an invaluable input to any knowledge-discovery process.

These drawbacks are serious concerns given that the users of these systems need to understand and act on the data in ever shorter amounts of time. In this paper, we propose new methods of discovery that address these drawbacks by discovering unexpected patterns that take into consideration prior background knowledge of managers. This prior knowledge constitutes a set of expectations or beliefs that managers have about the problem domain. We use these beliefs to seed the search for patterns in data that contradict the beliefs. Patterns contradictory to prior knowledge are by definition unexpected.

Methods that discover unexpected patterns with respect to prior knowledge are consistent with the general nature of scientific inquiry. The philosopher Karl Popper stresses the importance of falsification <sup>w</sup> <sup>x</sup> 4 for scientific inquiry. It is important to develop strong theories about a domain, but the rules of science demand that we also formulate the exact circumstances under which these theories can be falsified 4 . Moreover, the discovery of unexpected <sup>w</sup> <sup>x</sup> patterns addresses the drawbacks mentioned above.

<sup>Ø</sup> Since the search is focused on finding potentially interesting patterns, the problem of generating too many obvious or irrelevant patterns is avoided.

<sup>Ø</sup> The search uses subjective criteria for interestingness by leveraging prior domain knowledge Žwhich constitute a manager’s subjectiÕe input into the discovery process . Managers are potentially in- . valuable sources of intuition that may be specific to the task at hand. When such intuition forms the basis for an initial set of expectations, finding unexpected patterns in data attains significance, since they potentially test the robustness of managerial intuition.

## 1.1. An approach to pattern discoÕery

Our approach to pattern discovery begins with a set of beliefs that represent a decision maker’s prior domain knowledge. These beliefs can either be elicited from the decision maker initially or ‘‘learned’’ from the data using machine learning methods and shown to the decision maker for his or her approval. Our approach has two complementary facets:

1. Discovery of unexpected patterns in data

2. Knowledge refinement based on the discovery of unexpected patterns

The discovery of patterns in data that contradict prior knowledge can be used in building theories about the domain. There could be several reasons why prior intuition and patterns from data may conflict. For example, managerial intuition may have developed over years of prior experience and the data might reflect patterns on current environmental conditions distinctly different from previous conditions. Whatever the reasons, resolving such contradictions is important and could lead to a deeper understanding of the domain. Deming refers to knowledge developed through iterative theory building and refinement as ‘‘profound knowledge’’. The discovery of unexpected patterns with respect to specific intuitions could therefore lead to learning and the refinement of prior knowledge. In this sense, the discoÕery of unexpected patterns and refinement of prior knowledge form two sides of the same coin Ž . as illustrated in Fig. 1 .

In this paper, we focus only on the discovery of unexpected patterns given an initial set of beliefs.

![](/api/attachments/CCE8MFBQ/fulltext/images/31f58e008dcd69845a9f644828e7f71521d78b4ae37fca8f1b9713fa6046b381.jpg)  
Knowledge Repository

Fig. 1. Complementary nature of the discovery of unexpected patterns and knowledge refinement.

We do not address the issue of how to build a ‘‘good’’ set of beliefs. We assume that it can be generated using methods described in Ref. 17 , such<sup>w</sup> <sup>x</sup> as elicitation of beliefs from the domain expert, learning them from data and refinement of existing beliefs using newly discovered patterns. A similar issue of how to specify an initial set of beliefs has also been addressed in Ref. 9 . The rest of the paper<sup>w</sup> <sup>x</sup> is organized as follows. In Section 2, we discuss unexpectedness and present a definition for the unexpectedness of a rule. After briefly presenting some preliminaries of association rules in Section 3, we describe an algorithm for the discovery of unexpected rules in Sections 4 and 5. In Section 6, we present results from applying our method and a standard association rule generating algorithm on consumer purchase data and present conclusions in Section 7.

## 2. Unexpectedness of a rule

Unexpectedness of a rule has been considered before in Refs. 8,15–17 . However, Refs. 8,15–17<sup>w x</sup> <sup>w x</sup> present different approaches to defining this concept.

The approach presented in Ref. 8 captures a <sup>w</sup> <sup>x</sup> measure of rule ‘‘distance’’, but not ‘‘unexpectedness’’ for the following reason. The approach is based on a syntactic comparison between a rule and a belief. In Ref. 8 , a rule and a belief are ‘‘different’’ if either the consequents of the rule and the belief are ‘‘similar’’, but the antecedents are ‘‘far apart’’ or the consequents are ‘‘far apart’’, but the antecedents are ‘‘similar’’, where ‘‘similarity’’ and ‘‘difference’’ are defined syntactically based exclusively on the structure of the rules. For example, consider a belief man X( ) ( ) human X and a rule is woman X( ) ( ) human X . According to Ref. 8 , this<sup>w</sup> <sup>x</sup> rule has an ‘‘unanticipated condition’’ Žwoman X( ). and thus the rule is ‘‘different’’ from the belief. However, Ref. 8 stops short from declaring this<sup>w</sup> <sup>x</sup> rule to be ‘‘unexpected’’ relative to the belief. In deed, this rule, though different from the belief, is not unexpected, since one does not contradict the other in any way.

In Refs. 16,17 , a rule is considered to be unex-<sup>w</sup> <sup>x</sup> pected if it, intuitively, ‘‘shakes’’ the system of beliefs, including changes to the degrees of these beliefs. Our approach differs from Refs. 16,17 , in<sup>w</sup> <sup>x</sup> that we consider logical contradiction of a rule with a belief, whereas Refs. 16,17 define unexpected-<sup>w</sup> <sup>x</sup> ness in probabilistic terms of how much the degree of belief is affected by a rule. We believe that our definition of unexpectedness is simpler and more operational.

An alternative approach is presented in Ref. 15<sup>w</sup> <sup>x</sup> that discovers ‘‘exception rules’’ in the form of rule-pairs, but does not begin with prior background knowledge. The approach in Ref. 15 discovers pairs<sup>w</sup> <sup>x</sup> of association rules A B and their corresponding exceptions A, C B , where A and C are conjunc-² :  tions of attribute, value pairs and B and B are ² : attribute, value pairs corresponding to the same attribute, but with different values. Further, the unexpectedness of the exception rule in Ref. 15 is <sup>w</sup> <sup>x</sup> defined by an additional constraint that the ‘‘reference rule’’ C B has low confidence. Ref. 15 <sup>w</sup> <sup>x</sup> argues that if the reference rule has high confidence, then the exception rule A, C<sup>ª</sup>B will not be unexpected.

The approach presented in Ref. 15 is based on<sup>w</sup> <sup>x</sup> an interesting probabilistic approach and has the advantage that it does not depend on prior domain knowledge. However, it has been argued 16,17 that<sup>w</sup> <sup>x</sup> unexpectedness is inherently subjective and that prior beliefs of the user are, therefore, an important component of unexpectedness. Further, unexpectedness as defined in Ref. 15 can be restrictive, since it<sup>w</sup> <sup>x</sup> does not capture some exceptions that are unexpected in the sense defined below.

In the rest of this section, we present a new definition of unexpectedness of a rule. In order to define the concept of unexpectedness, we first present some preliminaries including definitions of rules and beliefs. We consider rules of the form X A, where X and A are conjunctions of literals i.e., Ž either atomic formulas of first-order logic or negations of atomic formulas . We also associate with the. rule some measure of its statistical ‘‘strength’’ 11 ,<sup>w</sup> <sup>x</sup> such as ‘‘confidence’’ and ‘‘support’’ 1 . We say <sup>w</sup> <sup>x</sup> that a rule holds on a data set D if the confidence of the rule is greater than 50% the threshold confi-Ž dence can also be chosen to be any value greater than 0.5 ..

We define a belief as a statement of the form Y B, where Y and B are defined as for the rule.

Associated with a belief is its degree <sup>w</sup> <sup>x</sup> 16,17 . Degrees of beliefs are subjective in the sense that they are defined by the user and are revised according to some belief revision procedure 16,17 .<sup>w</sup> <sup>x</sup>

The approach in Ref. 8 considers beliefs that<sup>w</sup> <sup>x</sup> incorporate fuzzy linguistic modifiers such as Ž ‘‘low’’, ‘‘high’’, ‘‘small’’, etc. . An example of such. a belief is ‘‘if temperature is high then heart\_rate is low’’. An advantage of this approach is that it permits the user to specify beliefs without drawing hard artificial boundaries around continuous variables. In this paper, however, we do not consider beliefs that incorporate fuzzy modifiers, since we focus our studies on pattern discovery in discrete data. We plan, however, to incorporate fuzziness into the representation of user beliefs in our subsequent work when we consider continuous variables as well.

We also make an assumption of monotonicity of beliefs. In particular, if we have a belief $Y  B$ which we expect to hold on a data set D with degree d, then the belief will also be expected to hold on any ‘‘statistically large’’ <sup>3</sup> subset of D with degree $d _ { 1 }$ that is greater than 0.5. We believe that this is a reasonable assumption for the following reason. Assume that we have two nonmonotonic beliefs $\ ^ { \cdot \cdot } b i r d ( X ) \to f l i e s ( X ) ^ { \prime } ^ { \prime }$ ( ) ( )  and ‘‘bird X , penguin X <sup>ª</sup> $\neg f l i e s ( X ) ^ { \prime } $ . Hence, in the current form, it appears that we expect the belief that birds fly to hold in general for the entire class of birds, but we do not expect it to hold for a subset that consists of penguins. However, these can be transformed into the following pair of monotonic beliefs ‘‘bird X ,( ) <sup>!</sup> penguin X( ) ( ) ( ) ( )<sup>ª</sup>flies X ’’ and ‘‘bird X , penguin X $ \neg f l i e s ( X ) ^ { \gtrless }$ . In general, if we have a nonmonotonic belief that we expect Ž not to hold for some subset of the data , we incorporate our knowledge of. why we do not expect the belief to hold on the subset into the belief, thereby making the belief more specific. We can do this iteratively until we have a set of monotonic beliefs. <sup>4</sup>

Given these preliminary concepts, we are ready to define unexpectedness of a rule.

Definition. The rule A<sup>ª</sup>B is unexpected with respect to the belief X<sup>ª</sup>Y on the data set D if the following conditions hold:

Ž .a B AND Y <sup><s</sup>FALSE. This condition imposes the constraint that B and Y logically contradict each other.

Ž . Ž <sup>3</sup> b A AND X holds on a statistically large . subset of tuples in D. We use the term ‘‘intersection of a rule with respect to a belief ’’ to refer to this subset. This intersection defines the subset of tuples in D in which the belief and the rule are both ‘‘applicable’’ in the sense that the antecedents of the belief and the rule are both true on all the tuples in this subset.

Ž . Ž . c The rule A, X<sup>ª</sup>B holds. Since condition a constrains B and Y to logically contradict each other, it logically follows that the rule A, $X  \neg Y$ holds.

We believe that this definition captures the spirit of ‘‘unexpectedness’’ for the following reasons.

Ž . 1 The heads of the rule and the belief are such that they logically contradict each other. Therefore, in any tuple where the belief and the rule are both ‘‘applicable’’, if the rule holds on this tuple, the belief cannot hold and vice versa.

Ž .2 Since both a rule and a belief hold statistically, it is inappropriate to label a rule ‘‘unexpected’’ if the intersection of the contradicting rule and the belief is very small. Hence, we impose the condition that the intersection of the belief and the rule should be statistically large. Within this statistically large intersection, we would expect our belief to hold because of the monotonicity assumption. However, if the rule holds in this intersection, the belief cannot hold because the heads of the rule and belief logically contradict each other. Hence, the expectation that the belief should hold on this statistically large subset is contradicted.

Our method of representation of beliefs can also be used to represent beliefs in which the expected confidence is less than 50% by converting the beliefs into those that have expected confidence greater than 50%. For example, consider the belief that Y is true

1% of the cases in which X is true. This is equivalent to the belief that NOTŽ .Y should be true 99% of the cases in which X is true.

The approach presented in this paper differs from that in Ref. 15 in the following aspects.<sup>w</sup> <sup>x</sup>

<sup>Ø</sup> The approach presented in Ref. 15 does not<sup>w</sup> <sup>x</sup> depend on prior beliefs, but discovers pairs of rules Ž . that can be considered as beliefs and their exceptions simultaneously. The approach presented in this paper begins with a system of beliefs.

<sup>Ø</sup> The approaches consider different types of unexpectedness. The approach presented in this paper is based on the monotonicity of beliefs, while exceptions in Ref. 15 are based on the structure of <sup>w</sup> <sup>x</sup> the rule-pair discovered and additional probabilistic constraints.

<sup>Ø</sup> The approach in Ref. 15 discovers only cer- <sup>w</sup> <sup>x</sup> tain refinements to rules as exceptions, while the approach presented in this paper discovers all refinements that are unexpected and also unexpected generalizations as well.

We presented a general definition of unexpectedness in this section. We next present an algorithm for finding unexpected rules. Since association rules are popular in the data mining literature with many efficient discovery algorithms developed for them, we focus in the rest of the paper on the discovery of unexpected association rules.

One way to generate unexpected association rules would be to follow the approach proposed in Ref. <sup>w</sup> <sup>x</sup> 8 : run standard association rule discovery algorithms 2 and then select unexpected rules using the<sup>w</sup> <sup>x</sup> definition of unexpectedness introduced in this section. The main problem with this approach is that of efficiency. It may turn out that there are few unexpected patterns and it would, therefore, not be efficient to generate a large number of patterns before selecting the unexpected ones. <sup>5</sup>

## 3. Association rule preliminaries

In this section, we provide an overview of associ ation rules and sketch the algorithms for discovering association rules proposed in Ref. 2 . Let<sup>w</sup> <sup>x</sup> I<sup>s</sup> $\{ i _ { 1 } , i _ { 2 } , \ldots , i _ { m } \}$ be a set of discrete attributes alsoŽ called ‘‘items’’ 1 . Let an<sup>w</sup> <sup>x</sup>. atomic condition be defined as a proposition of the form ‘‘attribute<sup>s</sup> value’’, where the attribute can take on a discrete set of mutually exclusive values. An itemset is a conjunction of atomic conditions. Let D <sup>s</sup> $\{ T _ { 1 } , T _ { 2 } , \dots , T _ { N } \}$ be a relation consisting on N transactions $[ 2 ] \quad T _ { 1 } , \ldots , T _ { N }$ over the relation schema $\{ i _ { 1 } , i _ { 2 } , \ldots , i _ { m } \}$ . A transaction $T _ { i }$ is said to ‘‘contain’’ an itemset if the itemset holds on $T _ { i } .$

An association rule is an implication of the form body<sup>ª</sup>head where ‘‘body’’ is an itemset and ‘‘head’’ is an itemset that contains only a single atomic condition. The rule holds in D with confidence c if c% of the transactions that contain body also contain head. The rule has support s in D if s% of the transactions in D contain both body and head. The search for association rules is usually constrained to rules that satisfy minimum specified support and confidence requirements. An itemset is said to be large if the percentage of transactions that contain it exceeds the minimum specified support level.

Various efficient algorithms for finding all association rules in transactions databases have been proposed in Ref. 2 . These algorithms operate in two <sup>w</sup> <sup>x</sup> phases. In the first phase, all large itemsets are generated. This phase utilizes the observation that all subsets of a large itemset are large. Candidate itemsets of length k are generated from the set of large itemsets of length Ž . k<sup>y</sup>1 by imposing the constraint that all subsets of length Ž . k <sup>y</sup> 1 of any candidate itemset must be present in the set of large itemsets of length Ž . k<sup>y</sup>1 . The second phase of the algorithm generates rules from the set of all large itemsets. For example, let $I _ { 1 } = \mathrm { \{ a g e = h i g h } $ 4 , income<sup>s</sup>high and $I _ { 2 } = \mathrm { \{ a g e = h i g h \} }$ . From the supports of these two itemsets, the confidence, $^ { c , }$ of the rule ‘‘if age ( <sup>s</sup> high then) $( i n c o m e = h i g h ) ^ { \prime } $ can be calculated as $c = s u p p o r t ( i a g e = h i g h ,$ incom $e = h i g h \ j ) _ { \mathit { h } } $ $s u p p o r t ( \it { i } a g e = h i g h \it { j } )$ . Hence, in this phase, given the set of all large itemsets, significant rules involving these itemsets are generated.

## 4. Discovery of unexpected association rules

In this section, we present an extension to the algorithm of Ref. 2 that takes a set of beliefs, <sup>w</sup> <sup>x</sup> B, and discovers unexpected association rules. In this paper, we restrict our attention to beliefs that have the same syntax as association rules and where the head of the belief involves a binary attribute. <sup>6</sup>

## 4.1. OÕerÕiew of the discoÕery strategy

Consider a belief X Y and a rule $A  B ,$ , where both the itemsets X and A are conjunctions of atomic conditions and both Y and B are single atomic conditions involving binary attributes. It follows from the definition of unexpectedness in Section 2 that if an association rule $A  B$ is ‘‘unexpected’’ with respect to the belief X<sup>ª</sup>Y, then the following must hold:

$$
B = \neg Y.
$$

## 2. The rule X, A<sup>ª</sup>B holds.

Hence, for every unexpected rule of the form $A  B ,$ it has to be the case that the rule X, A<sup>ª</sup>B also holds.

We propose the discovery algorithm ZoomUAR Ž . ‘‘Unexpected Association Rules’’ that consists of two parts: ZoominUAR and ZoomoutUAR. Given a belief X <sup>ª</sup> Y, the strategy that the algorithm ZoomUAR adopts is to first discover in AlgorithmŽ ZoominUAR. all significant rules of the form X, $A  \neg Y$ and then consider in AlgorithmŽ ZoomoutUAR. other more general and potentially unexpected rules of the form X , $A \to \lnot Y ,$ , where $X ^ { \prime } \subset X$ The rules that ZoominUAR discovers are ‘‘refinements’’ to the beliefs such that the beliefs are contradicted. The rules that ZoomoutUAR discovers are not refinements, but more general rules that satisfy the conditions of unexpectedness. For example, if a belief is that ‘‘professional weekend’’ Žprofessionals tend to shop more on weekends than on weekdays ,. ZoominUAR may discover a refinement such as ‘‘professional, december weekday’’ Žin December, professionals tend to shop more on weekdays than on weekends .. ZoomoutUAR may then discover a more general rule ‘‘december weekday’’, which is totally different from the initial belief ‘‘professional weekend’’.

## 4.2. Algorithm ZoominUAR

The inputs to this algorithm are a set of beliefs, B, and the data set D. For each belief $X  Y ,$ ZoominUAR finds all unexpected association rules of the form X, $A \to \lnot Y .$ . It is important to note that our approach differs from other association rule algorithms mainly in how we generate candidate itemsets that need to be checked for support and not in the actual process of checking the transactions in the data set to determine the supports for these itemsets. In Ref. 2 , different algorithms that calculate sup- <sup>w</sup> <sup>x</sup> ports for itemsets efficiently are presented. Our method can be easily integrated into any such efficient association rule algorithm. For simplicity, in this paper, we use the ‘‘shell’’ of the Apriori algorithm proposed in Ref. 2 . ZoominUAR is presented <sup>w</sup> <sup>x</sup> in Fig. 2.

For each belief, B, ZoominUAR first generates incrementally all large itemsets that may potentially generate unexpected rules. For example, if a belief is $X  Y$ then the search is initially for large itemsets that contain X and <sup>!</sup>Y, since the set of unexpected rules generated by this algorithm is of the form X, $A  \neg Y .$ The confidence of this rule is given by supportŽ . Ž . X, A,<sup>!</sup>Y <sup>r</sup>support X, A . Hence, each time the algorithm generates a candidate itemset $I _ { 1 }$ containing the negation of the head of the belief, the algorithm should also generate a corresponding candidate itemset $I _ { 1 } ^ { \prime }$ that contains all conditions in $I _ { 1 }$ except the negation of the head of the belief. In Fig. 2, the notation $C _ { k }$ refers to a set of candidate itemsets that contain the negation of the head of the belief and $C _ { k } ^ { \prime }$ refers to the corresponding set of candidate itemsets that do not contain the negation of the head of the belief. For example, for the belief $X  Y .$ , for every itemset of the form $\{ X , A , \lnot Y \}$ in $C _ { k }$ , there will be a corresponding itemset  4 X, A in $C _ { k } ^ { \prime }$

The first candidate itemsets generated step 2 in Ž Fig. 2 in this case is just . $\{ X , \lnot Y \}$  4 and X . Once candidate itemsets are generated, steps 4 and 5 determine the support counts in data set D for all the candidate itemsets currently being considered and selects the large itemsets in this set. Hence, in the initial pass, if both $\{ X , \lnot Y \}$  4 and X are found to be ‘‘large’’, then $L _ { 0 } = \{ \{ X , \neg Y \} , \{ X \} \}$

```txt
Inputs: Beliefs Bel_Set, Dataset D, Thresholds min_support and min_conf
Outputs: For each belief, B, itemsets Items_In_UnexpRule$_B

1 forall beliefs B ∈ Bel_Set {
2    C$_0$ = {{¬head(B),body(B)}}; C$_0'$ = {{body(B)}}; k=0;
3    while (C$_k$ != ∅ ) do {
4    forall candidates c ∈ C$_k$ ∪ C$_k'$, compute support(c)
5    L$_k$ = {x | x ∈ C$_k$ ∪ C$_k'$, support(x) ≥ min_support }
6    k++
7    C$_k$ = generate_new_candidates(L$_{k-1}$, B);
8    C$_{k'}$ = generate_bodies(C$_k$, B);
9    }
10 Let X = {x | x ∈ ∪L$_i$, x ≧ ¬head(B) }
11 Items_In_UnexpRule$_B$ = ∅
12 forall (x ∈ X) {
13    rule_conf = support(x)/support(x - ¬head(B))
14    if (rule_conf > min_conf) {
15    Items_In_UnexpRule$_B$ = Items_In_UnexpRule$_B$ ∪ {x}
16    Output Rule " x - ¬head(B) → ¬head(B) "
17    }
18    }
19 }
```  
Fig. 2. Algorithm ZoominUAR.

In step 7, the function generate\_new\_ candidates $\mathit { ^ { \prime } L _ { k - I } } , \mathit { B } )$ generates the set $C _ { k }$ of new candidate itemsets to be considered in the next pass from the previously determined set of large itemsets, $L _ { k - 1 }$ , with respect to the belief $B \ ( ^ { \ast \ast } x  y ^ { \ast } )$ in the following manner:

Ž . Ž . 1 Initial condition when k<sup>s</sup>1 : To explain this step, consider the following example. Assume that for the belief $x  y , \ L _ { 0 } = \{ \{ x , \lnot \ y \} , \{ x \} \}$ , i.e., both the initial candidates were found to be large. Further assume that $\ " p \ "$ and $\ " q \ "$ are the only other attributes in the domain that are not already present in any of the conditions in x or y and that $" p '$ and $\cdots _ { q } , ,$ are both binary attributes. The next set of candidates to be considered would be $C _ { 1 } =$ $\{ \{ x , \ l \} , \{ y , p \} , \{ x , \lnot y , \lnot p \} , \{ x , \lnot y , q \} , \{ x , \lnot y , \lnot q \} \}$ and $C _ { 1 } ^ { \prime } = \{ \{ x , p \} , \{ x , \lnot p \} , \{ x , q \} , \{ x , \lnot q \} \}$

In general, for the belief B, the initial candidate itemset $C _ { 0 }$ contains the single element body Ž . B , <sup>!</sup>headŽ . B 4. If this itemset is large, then the next set of candidate itemsets would be the sets $C _ { 1 } =$ bodyŽ . Ž . B , <sup>!</sup>head B , X 44, where X is any atomic condition involving an attribute not present in either Ž . Ž .4 body B or <sup>!</sup>head B and $C _ { 1 } ^ { \prime } = \{ \{ \mathrm { b o d y } ( B ) , ~ X \} \}$ where X is any atomic condition involving an attribute not present in either bodyŽ . Ž . B or <sup>!</sup>head B 4. The algorithm precomputes all the unique values for each attribute in the data set and uses these values to generate all possible attribute–value combinations that can be considered for X.

Ž . 2 Incremental generation of $C _ { k }$ from $L _ { k - 1 }$ when $k > 1$ : This function is very similar to the apriori-gen function described in Ref. 2 . For example, assume <sup>w</sup> <sup>x</sup> that for the belief $x  y , \quad L _ { 1 } = \{ \{ x , \lnot y , p \} $ $\{ x , \neg y , q \} , \{ x , p \} , \{ x , q \} \}$ . Similar to the Apriori algorithm, the next set of candidate itemsets that contain x and <sup>!</sup> y is $C _ { 2 } = \{ \{ x , \lnot \ y , p , q \} \}$ , since this is the only itemset such that all its subsets of one less cardinality that contain x and $\lnot \ y$ are in $L _ { 1 }$ . We would also need the support of the itemset $\{ x , p , q \}$ to Ž . eventually determine the confidence of the rule x, p, q  <sup>!</sup> y. Hence, the function generate\_ bodies $\mathbf { \bar { \Gamma } } _ { C _ { 2 } , B } )$ generates $C _ { 2 } ^ { \prime } = \{ \{ x , p , q \} \}$

In general, an itemset X is in $C _ { k }$ if and only if for the belief B, X contains <sup>!</sup>headŽ . Ž . B and body B and all subsets of X with one less cardinality, containing <sup>!</sup>headŽ . Ž . B and body B , are in $L _ { k - 1 } .$ The condition that X contains the negation of the head of the belief B is just an artifact of the fact that for every itemset of the form A,body B , ( ) ( ) <sup>!</sup> head B in $L _ { k - 1 } ,$ there will be a corresponding itemset A,body B( ) that will also be in $L _ { k - 1 }$ . Once $C _ { k }$ is generated as described above, the function generate\_bodies $\mathbf { \bar { \Lambda } } _ { C _ { k } , B } )$ generates the set $C _ { k } ^ { \prime }$ by considering each itemset in $C _ { k }$ and dropping <sup>!</sup>headŽ . B from the itemset.

Once all such large itemsets have been generated, steps 10 through 16 of the algorithm generate unexpected rules of the form $( x , A \to \neg y )$ , where $\{ x , \lnot \ y , A \}$  4 and x, A are large itemsets generated.

## 4.3. An example of ZoominUAR

Consider the following example. Assume that we have a data set of purchases at a supermarket Fig.Ž 3a containing the following four binary attributes:. Ž . Ž . Ž . 1 day of shopping weekend<sup>r</sup>weekday , 2 whether the shopper is employed, 3 whether diapers were Ž . purchased, and 4 whether beer was purchased. Ž . Further assume that we have a belief that shoppers who buy diapers tend to buy beer Ž . diaper beer . Fig. 3b illustrates the iterations of ZoominUAR and the unexpected rules generated given the constraints that any itemset in a rule should have a support of at least three transactions and that the minimum confidence of a rule should be 60%.

Our approach differs from Apriori in that in the first iteration, we start with itemsets that are derived from the belief since ZoominUAR focuses on dis- Ž covering rules of the form diaper, X beer.. We observe from the data that the belief is true in general confidence of the ruleŽ diaper beer is $5 / 8 )$ . However, in the second iteration, we discover two interesting rules that during weekdays or when the shopper is not employed, then the purchase of diapers implies that beer is not purchased. Further refinement third iteration results in a stronger ruleŽ . Ž . conf. 100% that when a shopper who is not employed shops on weekdays and buys diapers, then the shopper does not buy beer. Observe that:

![](/api/attachments/CCE8MFBQ/fulltext/images/ebf132130677cced3a17163a4e5c0f7ada3bc64228e638e33ce415bcd317bc1c.jpg)

<table><tr><td>Iteration #</td><td>Itemsets To Check</td><td>Sup</td><td>Large Itemset? (sup. &gt; 3)</td><td>Rules Generated (confidence &gt; 0.6)</td></tr><tr><td rowspan="2">1</td><td>{diaper, not_beer}</td><td>3</td><td>√</td><td>None - confidence (3/8) of</td></tr><tr><td>{diaper}</td><td>8</td><td>√</td><td>diap. → not_beer is &lt; 0.6</td></tr><tr><td rowspan="8">2</td><td>{diaper, not_beer, weekend}</td><td>0</td><td>×</td><td>None</td></tr><tr><td>{diaper, weekend}</td><td>4</td><td>√</td><td></td></tr><tr><td>{diaper, not_beer, not_weekend}</td><td>3</td><td>√</td><td rowspan="2">diap., weekday → not_beer (conf. = 3/4 = 0.75)</td></tr><tr><td>{diaper, not_weekend}</td><td>4</td><td>√</td></tr><tr><td>{diaper, not_beer, employed}</td><td>0</td><td>×</td><td>None</td></tr><tr><td>{diaper, employed}</td><td>3</td><td>√</td><td></td></tr><tr><td>{diaper, not_beer, not_employed}</td><td>3</td><td>√</td><td rowspan="2">diaper, not_employed. → not_beer (conf. = 3/5)</td></tr><tr><td>{diaper, not_employed}</td><td>5</td><td>√</td></tr><tr><td rowspan="2">3</td><td>{diaper, not_beer, not_weekend, not_employed}</td><td>3</td><td>√</td><td rowspan="2">diaper, not_employed, weekday → not_beer (conf. = 3/3)</td></tr><tr><td>{diaper, not_weekend, not_employed}</td><td>3</td><td>√</td></tr></table>

Fig. 3. a Left Example data containing nine transactions, each consisting of four fields. b Right Iterations of ZoominUAR right table Ž . Ž . Ž . Ž . Ž . corresponding to the belief ‘‘diapers<sup>ª</sup>beer’’.

```awk
Inputs: Beliefs Bel_Set, Dataset D, Thresholds min_support' and min_conf, For each belief, B, itemsets Items_In_UnexpRule$_B

1 forall beliefs B {
2    new_candidates = ∅
3    forall (x ∈ Items_In_UnexpRule$_B$) {
4    Let K = {k | k ⊂ x, k ⊃ x-body(B)}
5    Let K' = {k | k ⊂ x - ¬head(B), k ⊃ x-body(B)}
6    new_candidates = new_candidates ∪ K ∪ K'
7    }
8    find_support(new_candidates)
9    Let X = {x | x ∈ new_candidates, x ⊃ ¬head(B)}
10    forall (x ∈ X) {
11    rule_conf = support(x)/support(x - ¬head(B))
12    if (rule_conf > min_conf) {
13    Items_In_UnexpRule$_B$ = Items_In_UnexpRule$_B$ ∪ {x}
14    Output Rule "x - ¬head(B) → ¬head(B)"
15    }
16    }
17 }
```  
Fig. 4. Algorithm ZoomoutUAR.

Ž . 1 To compute the confidence of the rule diaper, X<sup>ª</sup>not\_beer, we need the supports of both the itemsets diaper, 4  4 X, not\_beer and diaper, X .

Ž . 2 In each iteration, we consider itemsets containing one more condition and the corresponding rules generated are therefore more specific ‘‘Ž zooming in’’ ..

Ž . 3 In the third iteration for example, we do not even consider the itemset diaper, not \_beer, weekend, unemployed , since a subset of this itemset, 4  4 diaper, not\_beer, weekend , did not have minimum support the first itemset considered in iteration Ž . a2 . If any subset of an itemset does not have enough support, then the itemset in consideration also cannot have minimum support 2 .<sup>w</sup> <sup>x</sup>

## 4.4. Algorithm ZoomoutUAR

ZoomoutUAR considers each unexpected rule generated by ZoominUAR and tries to determine all the other more general rules that may be unexpected. Given a belief X<sup>ª</sup>Y and an unexpected rule X, $A \to \lnot Y$ , ZoomoutUAR tries to find more general association rules of the form X , A <sup>!</sup>Y, where $X ^ { \prime } \subset X$ , and check if they satisfy minimum confidence requirements. Such rules satisfy the following properties.

<sup>Ø</sup> They are unexpected, since the intersection <sup>7</sup> of this rule with the belief results in the rule X, A <sup>ª</sup> <sup>!</sup>Y, which is already known to hold.

<sup>Ø</sup> These rules are more general in the sense that they have at least as much support as the rule X, $A  \neg Y .$

<sup>Ø</sup> The itemsets $\{ X ^ { \prime } , A \}$ and $\{ X ^ { \prime } , A , \lnot Y \}$ are guaranteed to satisfy the minimum support requirement Žthough we still have to determine their exact support in D., since the itemsets  4X, A and $\{ X , A , \lnot Y \}$ are already known to satisfy the minimum support requirement.

The algorithm ZoomoutUAR is presented in Fig. 4. For each belief, B, from the previous algorithm ZoominUAR, we have the set of all large itemsets that contain both <sup>!</sup>headŽ . Ž . B and body B . The general idea is to take each such large itemset, I, and find the supports for all the subsets of I that are obtained by dropping from I one or more attributes that are in bodyŽ . B . From the supports of all such new itemsets <sup>8</sup> considered here, ZoomoutUAR derives the rest of the more general unexpected rules. Step 4 of the algorithm creates candidate itemsets from the set of all large itemsets that contains the head of the unexpected rule being considered. As explained previously, for every itemset created in step 4, step 5 creates a corresponding new itemset that does not contain the head of the unexpected rule considered. Hence, in steps 3 through 6, the algorithm generates all the new candidate itemsets for which supports have to be calculated. In one pass over D, step 8 determines the supports for all these candidate itemsets. Once all the new large itemsets have been determined, steps 9 through 14 of the algorithm generates unexpected rules in a similar manner as the latter part steps 10 through 16 of theŽ . previous algorithm ZoominUAR.

## 4.5. Completeness of ZoomUAR

In this section, we present the theorem that ZoomUAR discovers all unexpected rules and provide a sketch of the proof.

Theorem. For any belief A B, ZoomUAR discoÕ- ers all unexpected rules of the form X Y, where X and A are conjunctions of atomic conditions and Y and B are single atomic conditions inÕolÕing binary attributes.

Sketch of the Proof. Consider the belief $A  B$ and any unexpected rule X Y Žwith support and confidence values greater than the specified threshold values where both the itemsets. X and A are conjunctions of atomic conditions and both Y and B are single atomic conditions involving binary attributes. From the definition of unexpectedness Section 2 , itŽ . follows that:

$$
1. Y = \neg B.
$$

2. The rule X, $A  \lnot B$ holds.

Therefore, the rule X, $A  \lnot B$ has support and confidence values greater than the specified threshold values. More specifically, the itemset $\{ X , A , \lnot B \}$ has adequate support. To prove the theorem, we will first show that ZoominUAR: a generates the itemset Ž . $\{ X , A , \lnot B \}$ and b derives the ruleŽ . X, $A  \lnot B$ from the itemset $\{ X , A , \lnot B \}$

If A is a subset of X, this completes the proof, <sup>9</sup> since the rule X, $A  \lnot B$ is equivalent to the rule $X  Y$ given that $Y = \lnot B .$ If A is not a subset of X, we will show that ZoomoutUAR: c generates theŽ . itemset $\{ X , \lnot B \}$ and d derives the ruleŽ . $X  \neg B$ from the itemset $\{ X , \lnot B \}$ . Since $Y = \lnot B .$ , this rule is the unexpected rule $X  Y .$

Since X is a conjunction of atomic conditions, assume that $X = \{ X _ { 1 } , X _ { 2 } , \ldots , X _ { N } \}$ . Since the itemset $\{ X , A , \lnot B \}$ is guaranteed to have adequate support, all subsets of $\{ X , A , \lnot B \}$ will also have adequate support. First, since we start with the belief $A  B ,$ step 2 of ZoominUAR Ž . Fig. 2 generates the itemset $\{ A , \lnot B \}$ . In the first iteration of ZoominUAR $( k =$ 0 , the itemset. $\{ A , \lnot B \}$ will be determined to have adequate support. Further, in this iteration, step 7 of ZoominUAR generates all candidate itemsets $\{ P , A , \lnot B \}$ where P is a single atomic condition. Hence, this candidate set also contains $\{ X _ { i } , A , \lnot \ B \}$ for i<sup>s</sup>1 to N. In the next iteration $\left( k = 1 \right)$ , all the itemsets $\{ X _ { i } , A , \lnot \ B \}$ will be determined to have adequate support in step 4. The next set of candidate itemsets generated byŽ .generate\_new\_candidates will contain itemsets of the form $\{ P , Q , A , \lnot B \}$ such that all subsets of this itemset that contain $\{ A , \lnot B \}$ have been determined to be large in the previous iteration. All itemsets of the form $\{ X _ { i } , X _ { j } , A , \lnot \ B \}$ will be generated as candidates, since the subsets $\{ X _ { i } , A , \lnot \ B \}$ and $\{ X _ { i } , A , \lnot B \}$ are known to be large from the previous iteration. Extending the same argument in subsequent iterations, it can be shown that ZoominUAR generates the itemset $\{ X _ { 1 } , X _ { 2 } , \ldots ,$ $X _ { N } , A , \lnot \ B \}$ in the iteration in the N th iteration. Since this itemset has adequate support, $\{ X , A , \lnot B \}$ will be an element in the set Items\_In\_UnexpRule.

Since ZoominUAR determines the set $\{ X , A , \lnot B \}$ to be large, step 13 of ZoominUAR considers the rule X, $A  \lnot B$ and determines that the rule holds. If A is a subset of X, this completes the proof, since the rule X, $A  \lnot B$ is equivalent to the rule $X \to Y$ given that $Y = \lnot B .$

If A is not a subset of X, since $\{ X , A , \lnot B \}$ is an element in the set Items\_In\_UnexpRule, step 4 of ZoomoutUAR Ž .Fig. 3 generates the itemset $\{ X , \lnot B \}$ by dropping one or more attributes from the body Ž .A of the belief $A  B ,$ . Step 5 similarly generates the itemset  4  4X . The itemsets X and $\{ X , \lnot B \}$ are, therefore, elements in the set new\_candidates generated in step 6 of ZoomoutUAR. Since these are guaranteed to have adequate support, step 14 of ZoomoutUAR generates the rule $X  \lnot B .$ . From the observation that $Y = \lnot B ,$ it follows that ZoomoutUAR generates the rule $X  Y .$

The theorem presented in this section states that ZoomUAR discovers all unexpected rules. Moreover, it is clear that ZoomUAR discovers only unexpected rules and no other rules. Therefore, ZoomUAR discovers a rule if and only if it is unexpected.

## 5. Handling multiple beliefs efficiently in Zoomin-UAR

Algorithm ZoominUAR shown in Fig. 2 discovers unexpected rules for each belief independently. In this section, we present extensions to ZoomUAR to exploit efficiency issues when dealing with multiple beliefs in parallel.

Consider the following example. Assume that the only conditions in a domain are A, B, C, D and their logical negations. Consider two beliefs, A B and $C  B .$ When the algorithm attempts discovers unexpected rules for each belief independently, Fig. 5 lists the itemsets considered by ZoominUAR in a hypothetical case the underlined itemsets in theseŽ tables are assumed to represent the ‘‘large’’ itemsets in that specific iteration ..

Observe that: a In the second iteration, the sameŽ . itemset $\{ A , \lnot B , C \}$ is considered twice: once each when itemsets are generated for the two beliefs, $A  B$ and $C  B .$ This could result in discovering the same rule e.g.,Ž A, $C \to \lnot B )$ by starting from two different beliefs. b When itemsets are consid-Ž . ered for the belief $A  B ,$ , the third iteration considers only the itemset $\left\{ A , \lnot \ B , C , \lnot \ D \right\}$ for support, since this is the only itemset that satisfies the condition that all its subsets containing $\{ A , \lnot B \}$ are $" \mathrm { l a r g e } ^ { \mathrm { , } \mathrm { , } }$ the underlined itemsets in the previousŽ iteration . However, one of its subsets. $\{ \lnot B , C , \lnot D \}$ does not have support as determined in the second iteration for the other belief $C  B .$ . Hence, the itemset $\{ A , \lnot B , C , \lnot D \}$ is guaranteed not to have the minimum support and therefore does not even need to be considered for checking its support.

In Fig. 6, we present the modified candidate building phase of ZoominUAR. The rest of the algorithm is the same as shown in Fig. 2.

## 6. Experiments

We tested our algorithm on consumer purchase data from a major market research firm. We preprocessed these data by combining different data sets, made available to us by this firm, into one table containing 36 different attributes. These attributes pertain to the item purchased by a shopper at a store, together with certain characteristics of the store and the demographic data about the shopper and his or her family. <sup>10</sup> Some demographic attributes include age and sex of the shopper, occupation, income and marital status of the household head and the presence of children in the family and the size of the household. Some transaction-specific attributes include type of item purchased, coupon usage whether theŽ shopper used any coupons to get a lower price or not , the availability of store coupons or manufac- . turer’s coupons and presence of advertisements for the product purchased in the store.

<table><tr><td>Iteration</td><td>Itemsets Considered for the belief A → B</td><td>Itemsets Considered for the belief C → B</td></tr><tr><td>1</td><td>{A, ¬B}</td><td>{C, ¬B}</td></tr><tr><td>2</td><td>{A, ¬B, C}, {A, ¬B, ¬C}, {A, ¬B, D}, {A, ¬B, ¬D}</td><td>{C, ¬B, A}, {C, ¬B, ¬A}, {C, ¬B, D}, {C, ¬B, ¬D}</td></tr><tr><td>3</td><td>{A, ¬B, C, ¬D}</td><td>{C, ¬B, A, D}</td></tr></table>

Fig. 5. Example itemsets considered by ZoominUAR for the two beliefs A<sup>ª</sup>B and $C  B .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs: Beliefs Bel_Set, Dataset D, Threshold min_support,
Outputs: The set of large itemsets used by the rest of ZoominUAR to
generate the itemsets Items_In_UnexpRule$_{B}$ (as in Fig. 4.1)

1    forall beliefs B$_{i}$ ∈ Bel_Set {
2    C$_{0}$[i] = {{-head(B$_{i}$),body(B$_{i}$)}}; C$_{0}'$[i] = {{body(B$_{i}$)}};
3    }
4    k = 0;
5    while (∃i : C$_{k}$[i] != ∅ ) do {
6    for (j = 1 to numbeliefs) {
7    forall candidates c ∈ C$_{k}$[j] ∪ C$_{k'}$[j], get
support(c)
8    L$_{k}$[j]={x | x ∈ C$_{k}$[j] ∪ C$_{k'}$[j],support(x) ≥
min_support}
9    }
10    k++
11    for (j = 1 to numbeliefs) {
12    C$_{k}$[j] = generate_new_candidates(L$_{k-1}$[], B);
13    C$_{k'}$[j] = generate_bodies(C$_{k}$[j], B);
14    }
15    }

Fig. 6. Extension to the candidate building phase of algorithm ZoominUAR.
</div>

While we generated this combined data set, we also restricted the purchasing records only to the class of carbonated beverages, i.e., each record in this data set refers to a purchase of some carbonated beverage by a shopper. The resulting data set had 87,437 records, each consisting of 36 discrete fields. The levels of discrete attributes range from 2 to 12 distinct values.

## 6.1. DiscoÕering unexpected patterns

We compiled 15 beliefs about the data in this domain which fall into three groups: 1 Usage ofŽ . coupons, e.g., ‘‘ young shoppers with high income tend not to use coupons’’. 2 Purchase of diet vs.Ž . regular drinks, e.g., ‘‘shoppers in households with children tend to purchase regular beÕerages more than diet’’. 3 Day of shopping, e.g., Ž . ‘‘ professionals tend to shop more on weekends than on weekdays’’. Some of these beliefs were solicited from experts and others were based on prior analyses of data. These beliefs were certainly not exhaustive about such a complex application in the sense that they do not contain all possible beliefs that a person may have about consumer purchase data. The set of beliefs that we used were selected just for illustrative purposes. In general, a much more complete set of beliefs can be obtained by learning them from the data as discussed in Ref. 18 .<sup>w</sup> <sup>x</sup>

Fig. 7 illustrates some of the unexpected rules discovered using our algorithm. The first rule in Fig. 7 is that shoppers who are retired do not use coupons, which is a direct contradiction of our belief. More subtle cases are when the unexpected rules do not directly contradict our beliefs. For example, we believed that professionals shop more on weekends than on weekdays belief Ž . a2 in Fig. 7 . Though the belief holds on the data, we find that, during December or when the household size is large, the belief is contradicted: professionals tend to shop more on weekdays in these cases. Though unexpected, ex post these rules seem to make sense given that there are usually more holidays in December or that large households may require the shopper to shop more often on demand than at convenient times. We also believed that households that had children tend to buy more of regular than diet beverages beliefŽ . a3 . Though this did seem to hold on the data, we found that when there are large advertisements in the store, they bought more diet than regular drinks.

<table><tr><td>#</td><td>Belief</td><td>Some Unexpected Rules for these Beliefs</td></tr><tr><td>1</td><td>occupation = retired → coupon_usage = yes</td><td>occupation = retired → coupon_usage = no[c = 0.9, s = 11%]</td></tr><tr><td>2</td><td>occupation = professional → day = weekend</td><td>occupation = professional, household_size = large → day = weekday[c = 0.6, s = 1%]occupation = professional, month = december → day = weekday [c = 0.6, s = 1%]</td></tr><tr><td>3</td><td>children = yes → drink = regular</td><td>children = yes, store_advertisement = large → drink = diet [c = 0.64, s = 1%]</td></tr></table>

Fig. 7. Some unexpected rules derived from consumer purchase data.

## 6.2. Comparison with Apriori

In addition to our belief-driven algorithm ZoomUAR, we tested a standard association rulegenerating algorithm, Apriori 2 on the consumer<sup>w</sup> <sup>x</sup> purchase data. ZoomUAR generated about 600 unexpected rules, while Apriori generated over 40,000 rules. To compare the interestingness of the rules generated, for illustrative purposes, we list a few rules generated by each method in Fig. 8. For Apriori, we selected some of the strongest rules all withŽ almost a 100% confidence! and for ZoomUAR, we. manually selected some rules, since we are dealing with a much smaller set of rules.

The rules generated from ZoomUAR Fig. 8 areŽ . not statistically very strong, but are interesting, since they were unexpected with respect to some of our expectations. In contrast, some of the top few rules generated by Apriori were extremely strong in the statistical sense close to a 100% rule confidence! . Ž . However, these rules, as they turned out, were an artifact of the data — for all the records in the data, there were no product displays in the lobby of the store during the purchase. Hence, trivially, any rule X no\_display\_in\_lobby would have a 100% confidence.

<table><tr><td>Rules from ZoomUAR</td><td>Rules from Apriori</td></tr><tr><td>1. professional, december → weekday (0.6)2. professional, large_household → weekday (0.6)3. children, store_advertisement → diet (0.6)4. male, young → diet (0.7)5. retired → no_coupon_usage (0.9)6. old, low_income → no_coupon_usage (0.9)</td><td>1. weekday → no_display_in_lobby (1.0)2. weekend → no_display_in_lobby (1.0)3. january → no_display_in_lobby (1.0)4. february → no_display_in_lobby (1.0)5. march → no_display_in_lobby (1.0)6. april → no_display_in_lobby (1.0)</td></tr></table>

Fig. 8. Comparison of rules generated from ZoomUAR and Apriori.

## 6.3. Discussion

As shown in the theorem in Section 4.5, for any belief, A<sup>ª</sup>B, ZoomUAR discovers all unexpected rules of the form X Y, where X and A are conjunctions of atomic conditions and Y and B are single atomic conditions involving binary attributes. Apriori extended for discrete attributes , on theŽ . other hand, discovers all association rules. The rules that ZoomUAR discovers are therefore a subset of the rules that Apriori discovers. This subset consists of the set of all unexpected rules, and is the most interesting subset of rules if unexpectedness is used as the measure of interestingness. Are there some patterns that Apriori discovers and that ZoomUAR does not that could be ‘‘interesting’’? Inasmuch as unexpectedness is the single measure of interestingness, this can never be the case based on theŽ theorem in Section 4.5 . However, from a more. general perspective, there may be other subjective measures of interestingness such as actionabilityŽ <sup>w</sup> <sup>x</sup> 3,12,16,17 that could result in ZoomUAR ‘‘mis-. sing’’ some of the ‘‘interesting’’ rules. We would like to make three observations in this regard. First, ZoomUAR is not intended to discover all ‘‘interesting’’ rules. Rather, it is an algorithm that discovers all unexpected rules. Hence, ZoomUAR by design, discovers only the subset of interesting rules that satisfy unexpectedness. Second, even for another subjective measure such as ‘‘actionability’’, the only ‘‘missing’’ rules are actionable, but expected rules. It has been conjectured 16–18 that most actionable rules are unexpected and hence this subset is small. Third, inasmuch as it is possible to explicitly charac terize all facets of interestingness, it may be possible to develop methods that discover all interesting patterns. Our work is just a step in this direction. Characterizing all the facets of interestingness and developing methods to discover all interesting patterns are important areas of future research in data mining.

## 7. Conclusions

In this paper, we proposed a new definition of unexpectedness of a rule with respect to a belief and presented an algorithm that finds unexpected association rules from data using this measure. We tested our methods on consumer purchase data from a market research firm and found some unexpected patterns with respect to our belief set. We also compared our approach with a standard association rule generating algorithm Apriori across the two Ž . dimensions: interestingness of rules and number of rules generated. We conclude that our method discovers, generally, fewer rules and avoids discovering many obvious or irrelevant rules as Apriori does. This means that our approach provides more focused and, therefore, more efficient search for interesting rules than Apriori.

In future work, we plan to extend our algorithm to discover unexpected patterns of a more general nature than association rules. We also plan to apply our method in the context of knowledge refinement based on the discovery of unexpected patterns. More generally, the contribution of this research will be procedures for making data mining more intelligent and useful for the decision maker. Our approach should lead to the development of decision-support systems that provide more relevant patterns in the data to the user, patterns that confirm or challenge the user’s beliefs and domain knowledge. We believe that such a breakthrough is required if data mining is to achieve its potential in business applications.

## References

<sup>w</sup> <sup>x</sup> 1 R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, in: Proc. of the ACM SIGMOD Conference on Management of Data, 1993, pp. 207–216.

<sup>w</sup> <sup>x</sup> 2 R. Agrawal, H. Mannila, R. Srikant, H. Toivonen, A.I. Verkamo, Fast discovery of association rules, in: U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy Ž . Eds. , Advances in Knowledge Discovery and Data Mining, AAAI Press, 1995.

<sup>w</sup> <sup>x</sup> 3 G. Adomavicius, A. Tuzhilin, Discovery of actionable patterns in databases: the action hierarchy approach, in: Proc. of the Third International Conference on Knowledge Discovery and Data Mining, 1997.

<sup>w</sup> <sup>x</sup> 4 P. Adriaans, D. Zantinge, Data Mining, Addison Wesley, Longman, 1996.

<sup>w</sup> <sup>x</sup> 5 L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classification and Regression Trees, Wadsworth International Group, 1984.

<sup>w</sup> <sup>x</sup> 6 S. Brin, R. Motwani, J.D. Ullman, S. Tsur, Dynamic itemset

counting and implication rules for market basket data, in: Procs. ACM SIGMOD Int. Conf. on Mgmt. of Data, 1997, pp. 255–264.

<sup>w</sup> <sup>x</sup> 7 U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, From data mining to knowledge discovery: an overview, in: U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy Ž . Eds. , Advances in Knowledge Discovery and Data Mining, AAAI<sup>r</sup>MIT Press, 1996.

<sup>w</sup> <sup>x</sup> 8 B. Liu, W. Hsu, Post-analysis of learned rules, in: Proc. of the Thirteenth National Conference on Artificial Intelligence Ž . AAAI ’96 , 1996, pp. 828–834.

<sup>w</sup> <sup>x</sup> 9 B. Liu, W. Hsu, S., Chen, Using general impressions to analyze discovered classification rules, in: Proc. of the Third International Conference on Knowledge Discovery and Data Mining KDD 97 , 1997, pp. 31–36.Ž .

<sup>w</sup> <sup>x</sup> 10 T.V. Merckt, 1997. http:<sup>rr</sup>www.cs.su.oz.au<sup>r ;</sup> thierry<sup>r</sup> ckdd.html

<sup>w</sup> <sup>x</sup> 11 G. Piatetsky-Shapiro, Discovery, analysis and presentation of strong rules, in: G. Piatetsky-Shapiro, W.J. Frawley Eds. , Ž . Knowledge Discovery in Databases, AAAI<sup>r</sup>MIT Press, 1991.

<sup>w</sup> <sup>x</sup> 12 G. Piatetsky-Shapiro, C.J. Matheus, The interestingness of deviations, in: Procs. of the AAAI-94 Workshop on Knowledge Discovery in Databases, 1994, pp. 25–36.

<sup>w</sup> <sup>x</sup> 13 J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993.

<sup>w</sup> <sup>x</sup> 14 R.B. Reich, The Work of Nations: Preparing Ourselves for 21st Century Capitalism, Alfred A. Knopf, New York, 1992.

<sup>w</sup> <sup>x</sup> 15 E. Suzuki, Autonomous discovery of reliable exception rules, in: Proc. of the Third International Conference on Knowledge Discovery and Data Mining, 1997, pp. 259–262.

<sup>w</sup> <sup>x</sup> 16 A. Silberschatz, A. Tuzhilin, On subjective measures of interestingness in knowledge discovery, in: Proc. of the First International Conference on Knowledge Discovery and Data Mining, 1995, pp. 275–281.

<sup>w</sup> <sup>x</sup> 17 A. Silberschatz, A. Tuzhilin, What makes patterns interesting in knowledge discovery systems, IEEE Transactions on

Knowledge and Data Engineering 5 6 1996 970–974, Ž . Ž . Special Issue on Data Mining.

<sup>w</sup> <sup>x</sup> 18 A. Tuzhilin, A. Silberschatz, A belief-driven discovery framework based on data monitoring and triggering, Working Paper aIS-96-26, Dept. of Information Systems, Leonard N. Stern School of Business, NYU, 1996.

Balaji Padmanabhan is an assistant professor of Operations and Information Management at The Wharton School, University of Pennsylvania. His research interests are in the areas of knowledge discovery in databases, design of Web-based systems and marketing on the Web. His current research focuses on building effective tools for the discovery of interesting patterns in data by combining prior intuition and organizational knowledge about problems with the power of automated search. His work has been published in the International Conference on Knowledge Discovery and Data Mining KDD , International Conference on information SystemsŽ . Ž . ICIS , Workshop on Information Technology and Systems Ž . Ž .WITS , America’s Conference on Information Systems AIS and the European Journal of Marketing.

Alexander Tuzhilin is an associate professor of Information Systems at Stern School of Business, New York University. He holds a PhD in Computer Science from the Courant Institute of Mathematical Sciences, NYU. His research interests include knowledge discovery in databases, temporal databases, marketing information systems, query-driven simulations and conceptual modeling of information systems. His papers have been published in ACM Transactions on Database Systems, ACM Transactions on Information Systems, ACM Transactions on Modeling and Computer Simulation, IEEE Transactions on Knowledge and Data Engineering, Acta Informatica, Information Systems, Information Systems Research, DSS, and marketing and OR journals. He serves on the Editorial Boards of the Data Mining and Knowledge Discovery Journal and the Journal of AIS.
