---
otero_id: 17487
otero_key: "MAFSJQJN"
title: "Market share analysis and prognosis using qualitative reasoning"
authors: "Paul Alpar; Werner Dilger"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00032-n"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Market share analysis and prognosis using qualitative reasoning

Paul Alpar $^{a,*}$ , Werner Dilger $^{b}$

$^{a}$ Philipps-University Marburg, Universitätsstr. 24, 35032 Marburg, Germany $^{b}$ University of Technology, Postfach 964, 09009 Chemnitz, Germany

## Abstract

Today, extensive quantitative modelling of the performance of marketing activities is possible due to the availability of rich data sets on product sales and related marketing actions. However, there are a number of product categories for which only inaccurate sales figures or data about marketing efforts exist (e.g., because a significant part of the sales is realized in stores without scanners or which do not make the data available to firm outsiders). In such cases, reliable quantitative findings about the impact of marketing-mix variables on sales may not be achievable but qualitative reasoning may, at least, indicate likely implications of past or planned marketing activities in terms of directions of change. Even in markets with good data qualitative reasoning may be a worthwhile first modelling approach when market conditions change so significantly that a previously used model is deemed unsatisfactory and not enough data exist yet for a specification of a revised quantitative model. We show specifically how qualitative reasoning can be used to diagnose and predict market share changes. The diagnostic part represents a combination of qualitative reasoning and extensions of a previously published rule-based expert system for that task while the prognostic part is solely based on qualitative process theory and order of magnitude reasoning.

Keywords: Qualitative reasoning; Artificial intelligence; Market share analysis; Marketing

## 1. Introduction

People make many, if not most, decisions based on a mainly qualitative thought process. This is also true for situations in which quantitative modelling is possible in principle. For example, most people make their investment decisions by ‘playing’ through different scenarios rather than employing a quantitative model. They reason qualitatively: ‘If interest rates go down, the construction activity will rise, the earnings of construction companies will improve ...’

In marketing, many quantitative models have been built to support decision making $[10]$ . For example, a fairly good understanding of the influence of one or a few marketing-mix variables on sales or market share has been developed. Reports of successful use of fairly complex market share attraction models exist $[3]$ . However, even these models often do not incorporate all marketing-mix and other potentially relevant variables (e.g., demographic variables). In addition, the functional choices, especially for the interaction of independent variables, are often driven by convenience within certain plausibility constraints. The lack of theory about the functional form of interactions of the variables is one of the main reasons for the difficulties and the complexity of the modelling task. Capturing qualitative knowledge of experts used in such situations and applying the method of qualitative reasoning may help to gain, at least, qualitative results (e.g., direction of change in sales) about the behaviour of a complex market system.

A similar situation in which qualitative reasoning may help is when disagreement exists on how to incorporate a variable in a model. For example, in diffusion modelling, it is accepted that advertising is likely to influence the diffusion process. However, researchers suggested different ways to account for that. Advertising was either included to influence the number of adopters due to internal communication $[14]$ or the number of adopters due to external communication $[7]$ . In both cases the effect will be an increased number of total adopters. In qualitative reasoning one can simply say that advertising positively and monotonically influences the number of total adopters without need for an exact quantitative specification of that relationship. Of course, if firm knowledge about the quantitative relationship exists then it should be used. But if there are doubts about the plausibility of model assumptions or the quality of data on which the quantitative specification was based, a qualitative model may be preferable since it is not sensitive to the functional form or the values of parameters of the relationship $[8]$ .

The paper is structured as follows. A brief introduction to concepts of qualitative reasoning relevant to our work is given in the next section. In Section 3, we reformulate a rule-based expert system for market share analysis in terms of qualitative reasoning. In Section 4 we show based on this formulation how interactions between marketing actions in different markets can be modeled. The prognosis of market share changes after specific marketing actions is modeled in Section 5. The last section reports on the state of our implementation and model evaluation efforts.

## 2. Basic concepts of qualitative reasoning

Qualitative reasoning (QR) is a means for reasoning on dynamic systems. Different approaches have been developed, the most important ones are the Qualitative Physics based on Confluences [4], the Qualitative Process Theory [6], and the Qualitative Simulation Algorithm [9]. All three approaches were aimed for the modelling of technical systems but can be applied to other types of dynamic systems. Such a system is described by two aspects: its structure and its behaviour. In QR the focus of attention is on behaviour. The concepts used in our application will be defined below.

The description of behaviour is based on variables that may change their values over time. That means, variables are considered as functions over time. Each variable v has two types of values:

A - value('amount'), denoted A(v)

D - value('derivative'), denoted D(v)

A(v) is the normal value of v and D(v) is the derivative of v over time. If we want to refer to a value of a variable at some time point t, we denote it by A(v,t), correspondingly for the D-value.

For each type of value a Qualitative Value Domain (QVD) is defined. For the A-value we assume that it has a ‘natural’ lower and upper bound. The interval between these bounds is subdivided into several smaller intervals according to application dependent considerations. Thus the QVD of the A-value is this set of subintervals, possibly augmented by some or all of the points between the intervals. For the D-value the usual QVD is the set $\{-,0,+$ , where 0 is a point and - and + represent intervals. The meaning of the D-value of a variable is to show the direction of possible change of the A-value of that variable. More precisely, if a variable v has the QCD $\{X_{1},...,X_{i-1},X_{i},X_{i+1},...$ and $A(v)=X_{i}$ , then if $D(v)=+,A(v)$ will eventually become $X_{i+1}$ , if $D(v)=-,A(v)$ will eventually become $X_{i-1}$ , if $D(v)=0,A(v)$ will not change in the next period of time.

The set $\{-,0,+$ of D-values must be extended by a further item, which may be denoted by ‘na’ or by the set itself, hence the QVD is $\{-,0,+,na\}$ or $\{-,0,+,\{-,0,+\}\}$ . The fourth value is needed to make a semigroup of the set with respect to the operation $\oplus$ as a special version of the usual addition. It is defined in Table 1.

Table 1  
Definition of the operator $\oplus$

<table><tr><td> $\oplus$ </td><td>-</td><td>0</td><td>+</td></tr><tr><td>-</td><td>-</td><td>-</td><td> $\{ -,0, +\}$ </td></tr><tr><td>0</td><td>-</td><td>0</td><td>+</td></tr><tr><td>+</td><td> $\{ -,0, +\}$ </td><td>+</td><td>+</td></tr></table>

$\oplus$ can be extended on the set $\{-,0,+,\{-,0,+ \}$ by defining $\{-,0,+ \} \oplus z=\{-,0,+ \}$ for all $z\in\{-,0,+ \}$ . This is undoubtedly the only meaningful extension of $\oplus$ , however it reveals the basic problem of the QR approach: The more inference steps are made in a QR model, i.e., the more applications of the operation $\oplus$ are made, the more likely is the undetermined D-value $\{-,0,+ \}$ as a result.

Other operations on qualitative values can also be defined. For instance, some authors define a qualitative counterpart to multiplication (the definition is quite natural). However, as $[15]$ points out, qualitative multiplication raises a number of serious problems. This may be the reason why qualitative multiplication is seldom used. Some authors (e.g., $[13]$ ) analyse dynamic systems described through non-linear differential equations by piecewise linear approximation. The domain of the underlying function is subdivided into several regions. Within the regions the function can be analysed using qualitative operations, in particular the qualitative version of addition. In marketing applications, systems are usually not described by differential equations. However, the idea of analysing such a system within certain regions may also be applied. Such regions must be defined pragmatically.

In order to avoid the growing uncertainty mentioned before one can make use of additional information if it is at hand. In fact, this happens to be within practical applications. Experts can sometimes estimate the strength of the change of a variable v, that means in the terms of QR something like the 'amount' of D(v). To avoid confusion with the A-values of variables we will call this the strength of D-values. It will be denoted by STR(D(v)). The value of STR(D(v)) is not specified, we only claim that STR(0) = 0 and STR(-) and STR(+) are arbitrarily chosen positive real numbers. By means of the STR-notation it is possible to compare the D-values of different variables. If v and w are variables, their STR-values may be different, even if their D-values are equal. For instance let D(v) = D(w) = + and STR(D(v)) < STR(D(w)), then D(w) is stronger than D(v). If STR(D(v)) is very small, D(v) is said to be neglectable. Notice that D(v) is neglectable if D(v) = 0. These are the basic concepts of the so called order of magnitude reasoning [12] which should be regarded as an important subarea of QR.

An important consequence of the definitions of strength and neglectability is the following property. Assume $D(v) = -$ and $D(w) = +$ for some variables v and w. If $\text{STR}(D(v)) = \text{STR}(D(w))$ , then $D(v) \oplus D(w) = 0$ , in contrast to the usual definition of $\oplus$ . However, it will be a rare case when it is known that the equation $\text{STR}(D(v)) = \text{STR}(D(w))$ holds. More often it may be known that $\text{STR}(D(v))$ is almost equal to $\text{STR}(D(w))$ . This relation will be denoted by $\text{STR}(D(v)) \approx \text{STR}(D(w))$ and we will define the obvious relationship

$$
\text { If } \mathrm{D} (\mathrm{v}) = - \text { and } \mathrm{D} (\mathrm{w}) = +
$$

for any variables v and w, then

$$
\operatorname{STR} (\mathrm{D} (\mathrm{v})) \approx \operatorname{STR} (\mathrm{D} (\mathrm{w})) \text {   if   and   only   if   }
$$

$D(v) \oplus D(w)$ is negligible.

It turns out that the notion of strength is closely related to the operation $\oplus$ .

An important concept of QR is causality. In some QR calculi it comes in by interpretation of any relations between variables, in others it is expressed directly as a special relation between variables. Following the lines of the Qualitative Process Theory, causality is expressed in two ways: Firstly, by a binary relation between variables, the directed proportionality, denoted by $\sim >^{+}$ and $\sim >^{-}$ . If v and w are variables, then $v \sim >^{+} w$ means that v has a positive influence on w, correspondingly for $v \sim >^{-} w$ ; secondly, by claiming that processes in general are the cause of changes, which is described through direct influences of processes on variables.

As [6] points out, there is a difference between the two notions of causality. If a variable is influenced by several processes, these influences can be summed up using the operation $\oplus$ . The directed proportionality, however, is the qualitative representation of a functional relationship between two variables, therefore in general we cannot compute the result of multiple influences by the directed proportionality using the operation $\oplus$ . Nevertheless, in the rest of this paper we will interpret the directed proportionality by means of $\oplus$ . If we use this interpretation only within narrow bounds of the variables, we can take it as an approximation to the underlying functional relation. Thus, $v \sim >^{+} w$ means that $D(v)$ must be added to $D(w)$ , whereas $v \sim >^{-} w$ means that $-1 * D(v)$ must be added to $D(w)$ .

According to the Qualitative Process QP Theory all changes in a dynamic system are triggered by processes. A process is a means to describe the dynamics of a system. Basically it consists of conditions and actions, like a rule in a rule system. However, there is a new aspect in the processes beyond the rules, namely the aspect of time. A process is something that starts at some time, is active for some period of time, and stops at another time. A rule may fire if its conditions are satisfied. A process is active as long as its conditions are satisfied. A rule is fired only if the rule interpreter chooses it, a process becomes active as soon as its conditions are satisfied, no interpreter or control system is required to start it.

One has to distinguish between process classes and process instances. What is defined in the Qualitative Process Theory are process classes, what is running in reality are process instances. The only things that are required to describe a process instance are a unique name and the name of the process class of which it is an instance. The process instance is completely determined by the process class to which it belongs. Because we are dealing mainly with process classes in the rest of the paper, we use process as a shorthand for process class if no confusion can arise.

A process is defined as a frame with three main slots: Conditions, constraints, and effects. Usually, a list of variables and a list of constants occurring in the process are added. A process may be a specialization of another process and, on the other hand, may have subprocesses that are specializations of it. The information about existing super-and subprocesses is added to the process definition by special slots. A process may be composed of other processes and is then called an aggregated process. The parts of the aggregated process need not be (and usually are not) subprocesses of that process, they may be of any other type. An aggregated process consists not only of a list of parts, rather the way how the parts are composed should also be described. This is usually done by defining influences between variables of different parts. Finally, each process gets an individual name. If one of the slots has an empty value, it is omitted. Thus the general structure of a process definition is as follows:

process process name

supers list of processes

subs list of processes

has-as-parts list of processes

links list of expressions characterizing relations between the processes mentioned in the has\_as\_part slot

variables list of variables occurring in the process

constants list of constants occurring in the process

preconditions list of expressions describing
    preconditions for the process
    activity

conditions list of activity conditions

constraints list of constraints

effects list of expressions characterizing the influence of the process on any variables

The supers and subs slots allow for the definition of is-a-hierarchies of processes. Thus classes of processes with general features can be defined and subsequently be refined to subclasses on different levels. An arbitrary number of instances which represent real processes can be created of each class. If a process is composed of other processes, these processes are listed in the has-as-parts slot, which allows for building part-of-hierarchies that are orthogonal to the is-a-hierarchies. The links are usually defined by proportionality relations between variables of the part processes. The preconditions slot contains statements that describe certain conditions for the activity of the process which cannot be expressed within the Qualitative Process Theory, cf. [6]. The conditions are relations over some of the variables and constants in the corresponding lists. Whenever all of the conditions are satisfied, the process is regarded as active, that means, the conditions and constraints hold. The constraints are relations over some of the variables like the conditions, but they are not regarded as conditions for the process activity, rather as consequences of the activity. A particularly important type of constraints are the proportionality expressions. The effect of the process on certain variables, i.e., a possible change of their D-value and consequently their A-value, can be described by the effects slot. Usually, these variables are used in the activity conditions of the actual or other processes. This guarantees that an active process may become inactive at a later time and an inactive process may become active.

We choose frames to capture the relevant knowledge since they are perfectly suited for the representation of taxonomic knowledge inherent in economic market structures. Further, frames offer an easy way to define conditions for triggering processes as we do it in the preconditions slot.

## 3. A first QR formulation of a market share analysis model

Our study of related work in marketing revealed that a model that attempted to capture some ‘first principles’ of market share analysis as it is performed by marketing managers at a manufacturer of packaged consumer goods has already been built [1,2]. Although no reference was made to QR, the developed system is clearly based on a causal model that relates changes in market share to changes in two marketing-mix factors using only values from the QVD described in Section 2. In fact, this model was termed by other researchers a 'direction of causality model' [11], a further implicit indication of similarity with the way causality is expressed in QP Theory. The resulting system, called SHANEX, was built as a rule-based expert system in PROLOG. More or less similar expert systems have been built for other marketing problems and some of them have found their way into commercial products. We chose SHANEX as a natural starting point for our work. First, we reformulate its knowledge using a QR representation and then we demonstrate possible extensions of the model. We first show how to improve its ability to diagnose market share changes, the task it was built for. Then, we develop a system that can also predict market share changes, a related but new task.

The SHANEX market model is based on three types of variables: (relative) price, market share, and featuring (share). Featuring refers to such marketing actions as fliers attached to newspapers in which a retail store or chain advertises specific brands. Some of the featuring costs may be borne by manufacturers of featured goods. Variables of type price, market share, and featuring can be regarded as functions of organizational units where sales take place (geographic areas or national retail accounts, i.e., large retail chains) and of time. Their values can be assumed to be numerical, though nothing is said about them and the focus of attention is not on their actual amount, rather on their change. Thus, it seems reasonable to define them as qualitative variables where the A-value is some non-negative number and the D-value is defined as in Section 2. The units are used to specify processes, i.e. for each unit a process describing a market is defined. By market we mean a 'market and competitive structure' as [3], i.e., a group of brands that are believed by marketing experts to compete with each other but not with other brands. This belief may be based on extensive market research and it may be more or less close to perceptions of consumers who actually buy the products.

There is one general process class that characterizes the events occurring in the market share analysis, the process Market. Essentially it states that the price has a negative influence and that featuring has a positive influence on the market share respectively. Typically it is always active, thus its activity condition is defined as TRUE. The process Market may have subprocesses for different units which in turn may have subprocesses for different brands etc. which results in the process hierarchy denoted below. All subprocesses have the general properties defined for the process Market.

<table><tr><td>process</td><td>Market</td></tr><tr><td>subs</td><td>Unit1 Unit2 ...</td></tr><tr><td rowspan="3">variables</td><td>p is a price</td></tr><tr><td>f is a featuring</td></tr><tr><td>m is a market_share</td></tr><tr><td>conditions</td><td>TRUE</td></tr><tr><td rowspan="2">constraints</td><td>p ~ &gt;- m</td></tr><tr><td>f ~ &gt;+ m</td></tr><tr><td>process</td><td>Unit1</td></tr><tr><td>supers</td><td>Market</td></tr><tr><td>subs</td><td>Brand1 Brand2 ...</td></tr><tr><td>process</td><td>Brand1</td></tr><tr><td>supers</td><td>Unit1</td></tr><tr><td>subs</td><td>Product_form1 Product_form2 ...</td></tr><tr><td>process</td><td>Product_form1</td></tr><tr><td>supers</td><td>Brand1</td></tr><tr><td>subs</td><td>Size1 Size2 ...</td></tr><tr><td>process</td><td>Size1</td></tr><tr><td>supers</td><td>Product_form1</td></tr></table>

By inheritance the subprocesses Unit $_i$ and Brand $_i$ get all slots of the process Market, thus these slots need not be repeated in the definition of the subprocesses. The domain of the variables is subsequently restricted from one process to its subprocesses. Which process instances will actually carry values in their variables depends on the desired level of aggregation. For example, if differentiation by size is not considered important then no size processes need to be defined and information on price, featuring, and market share will be stored in processes of type product\_form.

Notice that the process Market has no explicit effect, rather it has indirect influences on the market share which are stated by the constraints. A change of price or featuring, caused by any process, may lead to a change of the market share. More precisely: If t and $t'$ are times such that $t'$ is later than t then $D(m,t') = D(m,t) \oplus -1 * D(p,t)$ and $D(m,t') = D(m,t) \oplus D(f,t)$ . If we assume that the market is a closed world, i.e. there are no other influences on the variables than the ones stated in the process definitions, we can compute the value of $D(m,t')$ from the above equations. The sums in the equations are well defined if at least one part is zero, e.g., if $D(p,t)$ and $D(f,t)$ are zero, i.e., the A-values of p and f do not change at time t. If, however, at least one of them is not zero, we may get problems, according to the addition table for $\oplus$ , cf. Section 2. Problems arise if and only if $D(m,t) = D(p,t) \neq 0$ or $D(m,t) = -1 * D(f,t) \neq 0$ . In both cases the sum can take on one of the three values -, 0, and +. That means the result is undetermined.

This consideration corresponds to the reality of the market, where values are often not precise and consequently the results of computations or inferences are ambiguous. A computational model of the market cannot be more precise than the reality. However, in the market share analysis according to SHANEX there is additional information available that can be used in the sense of order of magnitude reasoning, cf. Section 2. It allows for making the results of the computation unambiguous in some cases.

Information of this kind is for instance contained in the rule that states when a change of a variable will be regarded as a move apart from its previous value [[2],p.10]. The condition for moving up is A(v,t') \* 100/A(v,t) > 106 (6% as a significance limit is just an arbitrary example), where v is a variable, t' is the actual time and t some time previous to t'. Similarly one could define a condition for moving down by A(v,t') \* 100/A(v,t) < 94. In the terms of Order of Magnitude Reasoning this means: A(v,t') > A(v,t) if and only if D(v,t) = +, but STR(D(v,t)) is neglectable if A(v,t') \* 100/A(v,t) ≤ 106, correspondingly for the case A(v,t') < A(v,t).

SHANEX is essentially a diagnostic system.

The result of its diagnosis is referred to as a pattern. A pattern is derived for each unit (area or account) and then the dominating pattern is computed by accumulation of weights for the unit patterns. The weights in SHANEX are calculated on the basis of manufacturer to retail shipments but other derivations are possible too. The dominating pattern (if it exists) is called the overall pattern. The diagnostic knowledge incorporated in the SHANEX system interprets situations occurring in the market. Because the basic knowledge about the market is represented here by the processes defined above, the diagnostic knowledge must be rewritten. An example of this kind of knowledge is the rule that attributes market share changes to the featuring activity [[2],p.11]. It can be reformulated in the following way:

(1) IF $\mathrm{D}(\mathfrak{m})\neq 0$ and

$D(f) = D(m) \text{ and } D(p) \text{ is neglectable}$

THEN market share was influenced by featuring

This rule describes by its condition the situation when the market share variable m and the featuring variable f move substantially in the same direction, whereas the price variable p does not change or its change is negligible. Similarly a rule can be defined for the influence of the price on the market share:

(2) IF $\mathrm{D}(\mathfrak{m})\neq 0$ and $\mathrm{D(p)} = -1*\mathrm{D(m)}$

and $\mathbf{D}(\mathbf{f})$ is negligible

THEN market share was influenced by price

Notice that these rules only apply to real situations, and these are represented by process instances. In addition, both rules are related to single units. Hence the rules interpret processes of the type Unit $_{i}$ . Other cases, indicated in [2] but not explicitly shown in form of rules can be represented as follows:

(3) IF $\mathrm{D}(\mathrm{m}) \neq 0$ and $\mathrm{D}(\mathrm{f}) = \mathrm{D}(\mathrm{m})$

and $\mathrm{D(p) = -1*D(m)}$

THEN market share was influenced by featuring or by price

Clearly, the content of this information is not as high as in the rules 1 and 2, but the rule at least states that all three variables have moved and the influencing variables moved in such a way that both may be the cause for the moving of the market share. The next rule alerts marketing managers to an unexpected situation:

(4) IF $\mathrm{D}(\mathrm{m})$ is negligible and $\mathrm{D}(\mathrm{f}) = +$ and

$\mathrm{D(p)}$ is negligible

THEN market share was not influenced by

featuring though this could be expected

The rule states that there is an obvious contradiction between the observed situation and the constraints in the Market process. Because we presuppose that there are no other influences on variables than the ones defined in the Market process, the reason for this phenomenon must be that the change of featuring was not strong enough to cause a substantial change of the market share.

As mentioned above, SHANEX not only derives conclusions about market share changes in units(unit patterns) but also a diagnosis for the whole country (overall pattern). A unit pattern is determined as the overall pattern if it is the prevalent pattern over the whole set of units. It can be taken as a snapshot of the market situation on the national level. That means, an overall pattern is no longer related to units, but it is still related to a certain brand. The rule for determining an overall pattern refers to a process of the type National\_Market in the terminology of processes. However, this process should include in some sense the processes of type Unit $_{i}$ that contribute to the overall pattern. In fact, such a process could be conceived as describing the market on the national level. The appropriate definition for the process is by composition.

$$
\begin{array}{l l} \text {process} & \text {National\_Market} \\ \text {supers} & \text {Market} \\ \text {has\_as\_parts} & \text {Unit1 Unit2 ...} \end{array}
$$

So far the process has no links slot because no knowledge about relationships between the parts has been defined in SHANEX. The SHANEX diagnostic knowledge [[2],pp.11,12] evaluates the situations of the processes of type Unit $_i$ that are parts of the National\_Market process. The evaluation can best be realized as an algorithm running on the part processes. It takes into account the weights of the units for the patterns and it uses the rules for the interpretation of the part processes. Its structure is as follows:

```txt
PROCS ← list of part processes
w1 ← 0
w2 ← 0
repeat
    select one element of PROCS as the actual process, say pr
    delete pr from PROCS
    if D(m) ≠ 0 and D(f) = D(m) and D(p) is neglectable
    then w1 ← w1 + weight(pr)
    end if
    if D(m) ≠ 0 and D(p) = -1 * D(m) and D(f) is neglectable
    then w2 ← w2 + weight(pr)
    end if
until PROCS is empty
if    w1 > upper_limit
then    ‘market share was influenced by featuring’ is the overall pattern
else if    w2 > upper_limit
then    ‘market share was influenced by price’ is the overall pattern
else    no overall pattern
```

The parameter upper\_limit is set by marketing experts based on several criteria.

## 4. Extensions to the market share analysis model

The SHANEX model contains several simplifications of the real world situations. According to [2], this simplified model was capable of correctly diagnosing most of the cases in the observed time period (in the sense of matching both a human analysts' and a statistical model's diagnosis). However, when the model is used over a longer time period and for various brands more exceptions, i.e., cases that cannot be handled by the model will occur. One would clearly like to improve the model by removing some of the simplifications. In a rule-based system this often leads not only to new rules but also to a change of existing rules. The latter case may mean that the number of premises must be increased which is equal to an increase in potential cases that need to be covered by rules. This may further lead to an explosion of the number of rules and/or much more complicated rules. In the outlined QR approach extensions to the basic model are easier to perform.

One of the simplifications in SHANEX is the assumption of no interaction between the marketing actions in different units. Remember, a unit is either a geographic area or a national account. In the latter case, it is quite likely that actions related to one brand will not only influence other brands in the same product category and unit but also brands in other, usually competing, units. In our further discussion, we assume that a market process simulates a national account. Then, one could assume, for example, that featuring a brand in one market has a beneficial effect on the market share of this brand in another market as well because consumers are generally induced to pay more attention to that brand. Another assumption may be that the price change of one brand in one market inversely influences the market share of this brand in another market. The reason for such behaviour may be that loyal consumers are more likely to switch the shop where they purchase an expensive brand than to switch the brand. For example, a price decrease of such a brand in one chain may attract usual buyers of this brand away from other chains while loyal buyers of competitive brands continue to shop their preferred brands in the usual locations and in usual quantities. Thus, the market share of the analysed brand would decrease in chains where price decreases did not occur.

The proposed assumptions can be easily implemented in our approach via links. Note that the use of links would have also been necessary if we would have represented each competing brand explicitly, i.e., with its own market share, price, and featuring share. A quantitative modeller would then see nothing special in that since a full-fledged attraction model explicitly considers all relevant brands and differential effects of the marketing efforts related to each brand. The point we want to make here is that we are now modelling interactions between markets which is seldom done in attraction models due to the further complexity it creates. Considering interactions between markets is necessary in many situations, e.g., in cases of product substitution or complementarity (see $[5]$ for an economic QR analysis at product category level). In the context of market share analysis this is especially necessary when the modeled relationship affects the brands differently. For example, an aggressive push of a pancake mix may have a more significant impact on the same name syrup than on other syrup brands that are all complementary to the pancake mix. Or, the positioning of a cereal towards a snack will have a differential effect on specific snack groups and brands within these groups. In general, due to the great variety within many product categories (e.g., there are almost 2000 different cracker products in terms of different UPCs) we often have to define markets based on subgroups of a product category thus creating likely interactions between markets.

We demonstrate the use of links using the above mentioned assumption that the price of a brand in one unit inversely influences the market share of this brand in another unit. When more than one process is considered, the variables occurring in the processes must be distinguished. This is done here by prefixing them with the process name. On the basis of this model the rules of the diagnostic knowledge should also be revised. Instead of single rules we get rule schemata for the processes of type Unit $_{i}$ . Such a rule schema is the following one:

$$
\begin{array}{l l} \text {IF} & D (U n i t _ {i}. m) \neq 0 \\ & \text {and} D (U n i t _ {i}. f) = D (U n i t _ {i}. m) \\ & \text {and} D (U n i t _ {i}. p) \text {is neglectable} \\ & \text {and} D (U n i t _ {j}. p) \text {is neglectable} \\ \text {THEN} & \text {market share was influenced by featuring} \end{array}\tag{5}
$$

This schema can be instantiated for different units. It corresponds to rule 1. The two rule schemata corresponding to rule 2 are developed in a similar way:

$$
\mathrm{D} (\text { Unit } _ {i}. \mathrm{m}) \neq 0\tag{6}
$$

$$
\mathrm{D} \left(\text {Unit} _ {\mathrm{i}}. \mathrm{p}\right) = - 1 * \mathrm{D} \left(\text {Unit} _ {\mathrm{i}}. \mathrm{m}\right)
$$

$$
\mathrm{D} (\text { Unit } _ {i}. f)
$$

$$
\mathrm{D} (\text { Unit } _ {j}. \mathrm{p})\tag{7}
$$

$$
\begin{array}{l l} \text {IF} & D (U n i t _ {i}. m) \neq 0 \\ & \text {and} D (U n i t _ {j}. p) = - 1 * D (U n i t _ {i}. m) \\ & \text {and} D (U n i t _ {i}. f) \text {is neglectable} \\ & \text {and} D (U n i t _ {i}. p) \text {is neglectable} \\ \text {THEN} & \text {market share was influenced by the price in Unit} _ {j}. \end{array}
$$

Assuming that the Unit $_{i}$ process for any i contains more than two competing brands and looking at the rules 3 and 4, it becomes obvious that the rules should be replaced with small algorithms running over the set of units and checking all possible situations. They have a similar structure as the algorithm of Section 3 and can be incorporated in that algorithm to produce a larger one for computation of the overall patterns.

## 5. A market share prognosis model

Now, we turn to the task of prognosis. QR is here of particular interest when we try to predict effects of planned actions which were not executed before. The same is true for competitors' actions that just started but not enough data on the effects of the action are available. In cases where no dramatic changes in the structure of competition are expected extrapolation via quantitative models is still the preferable approach.

In this section we model a situation which contains markets that function according to the original SHANEX model as described in Section 3. In addition, we model interactions among three markets each representing a group of brands where each brand normally does not compete against specific brands from the other groups. However, due to specific actions we expect that the market share of a brand in one market inversely influences market shares of specific brands in other markets. This means that an increase in sales and market share of one brand within its group leads to a decrease of sales in another group and especially so for one brand within that group. For example, marketing activities to back up sales of a brand of iced tea may not only increase its market share in its product group (i.e., market) but also hurt the group of carbonated drinks and especially the lemon-flavoured brands.

Our market definition includes only brands which normally compete with each other. Now, we need to define a process which contains several markets to be able to define relationships among brands (which will be abbreviated by B) from different markets. We call this process Expanded\_Market and list as its parts all brands from the original markets. In the example we consider three brands from three markets.

<table><tr><td>process</td><td>Expanded_Market</td></tr><tr><td>supers</td><td>Market</td></tr><tr><td>has_as_parts</td><td>B1 B2 B3</td></tr><tr><td>links</td><td>B1.m ~ &gt; $^{-}$  B2.m</td></tr><tr><td></td><td>B1.m ~ &gt; $^{-}$  B3.m</td></tr><tr><td></td><td>B2.m ~ &gt; $^{-}$  B1.m</td></tr><tr><td></td><td>B2.m ~ &gt; $^{-}$  B3.m</td></tr><tr><td></td><td>B3.m ~ &gt; $^{-}$  B1.m</td></tr><tr><td></td><td>B3.m ~ &gt; $^{-}$  B2.m</td></tr></table>

The definition of the Brand process that will be used here is an extended version of that given in Section 3. The main difference is that now the Brand process has specified preconditions and effects. This allows for describing the activity of a company concerning a certain brand. The company decides to take actions that influence the market share of the brand. This is denoted in the preconditions slot. The market share can be influenced by changing the price or featuring, which is denoted in the effects slot. Thus, the general definition of the Brand process Bi is

process Bi
supers Unit1
is\_part\_of Expanded\_Market
variables p is a price of brand;
in unit1
f is a featuring of brand; in unit1
m is a market\_share of brand;

For a particular Brand process, say B1, the preconditions and effects could be defined as follows:

preconditions Take action that influences the market share of B1
effects D(B1.f) = +

That means, featuring is increased but the price is left unchanged. For the processes B2 and B3 the preconditions and effects are defined analogously by

process B2

process B3

The last precondition means that process B3 will not become active.

By inheritance for each process Bi the constraints $p \sim >^{-} m$ and $f \sim >^{+} m$ hold, or more precisely:

Altogether there are 12 directed proportionalities in the Expanded\_Market process. We will reformulate these relations as a directed graph with the Bi.v as nodes and the edges labelled by + or -. This is shown in Fig. 1.

This graph allows for the propagation of D-values along the edges. Assume that $t_{0}$ , $t_{1}$ , $t_{2}$ , and $t_{3}$ are points on the time axis ordered in this sequence, i.e. $t_{0} < t_{1} < t_{2} < t_{3}$ . At these times, snapshots of the set of processes are taken, and we assume that between two subsequent times one propagation step between adjacent nodes occurs. The distances between subsequent points are left unspecified. According to the definition of the effect slots of B1, B2, and B3 we have the following situation:

$$
\begin{array}{l l} D (B 1. p, t _ {0}) = 0 & D (B 1. f, t _ {0}) = + \\ D (B 2. p, t _ {0}) = + & D (B 2. f, t _ {0}) = 0 \\ D (B 3. p, t _ {0}) = 0 & D (B 3. f, t _ {0}) = 0 \end{array}
$$

In addition, we assume that

$$
\begin{array}{l} \mathrm {D(B1.m, t_ {0}) = 0} \\ \mathrm {D(B2.m, t_ {0}) = 0} \\ \mathrm {D(B3.m, t_ {0}) = 0} \end{array}
$$

At each time $t_j, j \geq 1$ , the value of D(Bi.m, $t_j$ ) (i = 1,2,3) is computed as the sum of D(Bi.m, $t_{j-1}$ ) and all D(v, $t_{j-1}$ ) for which there is an arrow from D(v, $t_{j-1}$ ) to D(Bi.m, $t_j$ ) in the graph. Each D(v, $t_{j-1}$ ) is multiplied with -1 if the label of the arrow leading to D(Bi.m, $t_j$ ) is -. For example, at time $t_1$ the value of D(B1.m, $t_1$ ) is

$$
\begin{array}{l} \mathrm {D(B1.m, t _ {1}) = D(B1.m, t _ {0})} \\ \oplus - 1 * \mathrm {D(B1.p, t _ {0})\oplus D(B1.f, t _ {0})} \\ \oplus - 1 * \mathrm {D(B2.m, t _ {0})\oplus - 1*D(B3.m, t _ {0})} \\ = 0 \oplus 0 \oplus + \oplus 0 \oplus 0 \\ = + \end{array}
$$

In order to compute the sums at each time $t_{j}$ values for the $D(Bi.p,t_{j})$ and $D(Bi.f,t_{j})$ must be established. That means, the set of active Brand processes and hence the kind of influences on the market share of the brands may change from time $t_{j}$ to time $t_{j+1}$ . In fact, the distinction between different times is mainly determined by such changes. Applying this computation scheme to all $D(Bi.m,t_{j})$ (i = 1,2,3; j = 0,1,2,3) results in Table 2.

It is easy to see that for arbitrary values of the $D(Bi.p,t_{2})$ and $D(Bi.f,t_{2})$ all $D(Bi.m,t_{3})$ get the undetermined value $\{-,0,+$ . If, however, additional information about the strength of the D-values is available, the result at least at time $t_{3}$ could be more precise. Assume the experts know that in general the influences of featuring and price on the market share of a commodity are stronger than the influences of the market shares of other commodities. This means in the terms of order of magnitude reasoning:

![](/api/attachments/MAFSJQJN/fulltext/images/8f4f1d0390659dbaef97019238f100193df4de6365892792091b409e91a37ea9.jpg)  
Fig. 1. Influence diagram with three brands.

$$
\begin{array}{l} \operatorname{STR} \bigl (\mathrm{D} \bigl (\mathrm{Bi}. \mathrm{p}, \mathrm{t} _ {\mathrm{j}} \bigr) \bigr) > \operatorname{STR} \bigl (\mathrm{D} \bigl (\mathrm{Bk}. \mathrm{m}, \mathrm{t} _ {\mathrm{j}} \bigr) \bigr) \\ \quad (\mathrm{i} = 1, 2, 3; \mathrm{k} \neq \mathrm{i}) \text {and} \\ \operatorname{STR} \bigl (\mathrm{D} \bigl (\mathrm{Bi}. \mathrm{f}, \mathrm{t} _ {\mathrm{j}} \bigr) \bigr) > \operatorname{STR} \bigl (\mathrm{D} \bigl (\mathrm{Bk}. \mathrm{m}, \mathrm{t} _ {\mathrm{j}} \bigr) \bigr) \\ \quad (\mathrm{i} = 1, 2, 3; \mathrm{k} \neq \mathrm{i}) \end{array}
$$

Qualitative propagation of changes

<table><tr><td></td><td> $t_0$ </td><td> $t_1$ </td><td> $t_2$ </td><td> $t_3$ </td></tr><tr><td>D(B1.p,  $t_i$ )</td><td>0</td><td>0</td><td>arbitrary</td><td></td></tr><tr><td>D(B1.f,  $t_i$ )</td><td>+</td><td>0</td><td>arbitrary</td><td></td></tr><tr><td>D(B2.p,  $t_i$ )</td><td>+</td><td>0</td><td>arbitrary</td><td></td></tr><tr><td>D(B2.f,  $t_i$ )</td><td>0</td><td>+</td><td>arbitrary</td><td></td></tr><tr><td>D(B3.p,  $t_i$ )</td><td>0</td><td>-</td><td>arbitrary</td><td></td></tr><tr><td>D(B3.f,  $t_i$ )</td><td>0</td><td>0</td><td>arbitrary</td><td></td></tr><tr><td>D(B1.m,  $t_i$ )</td><td>0</td><td>+</td><td>+</td><td> $\{ -, 0, + \}$ </td></tr><tr><td>D(B2.m,  $t_i$ )</td><td>0</td><td>-</td><td> $\{ -, 0, + \}$ </td><td> $\{ -, 0, + \}$ </td></tr><tr><td>D(B3.m,  $t_i$ )</td><td>0</td><td>0</td><td> $\{ -, 0, + \}$ </td><td> $\{ -, 0, + \}$ </td></tr></table>

With these relations, the computation of $D(B3.m,t_{2})$ is as follows:

$$
\mathrm{D} (\mathrm{B3.m}, \mathrm{t} _ {2}) = \mathrm{D} (\mathrm{B3.m}, \mathrm{t} _ {1})
$$

$$
\oplus - 1 * \mathrm{D} (\mathrm{B3.p}, t _ {1}) \oplus \mathrm{D} (\mathrm{B3.f}, t _ {1})
$$

$$
\oplus - 1 * \mathrm{D} (\mathrm{B} 1. \mathrm{m}, \mathrm{t} _ {1}) \oplus - 1 * \mathrm{D} (\mathrm{B} 2. \mathrm{m}, \mathrm{t} _ {1})
$$

$$
= 0 \oplus + \oplus 0 \oplus - \oplus +
$$

Now because $\mathrm{STR}(\mathrm{D}(\mathrm{B3.p},\mathrm{t}_1)) > \mathrm{STR}(\mathrm{D}(\mathrm{B1.m},\mathrm{t}_1)), - 1*\mathrm{D}(\mathrm{B3.p},\mathrm{t}_1)\oplus -$ $1*\mathrm{D}(\mathrm{B1.m},\mathrm{t}_1) = -1*\mathrm{D}(\mathrm{B3.p},\mathrm{t}_1)$ , hence $\mathrm{D(B3.m,t_2)} = +.$ For $\mathrm{D(B2.m,t_2)}$ a similar result cannot be computed:

$$
\mathrm{D} (\mathrm{B2.m}, \mathrm{t} _ {2}) = \mathrm{D} (\mathrm{B2.m}, \mathrm{t} _ {1})
$$

$$
\oplus - 1 * \mathrm{D} (\mathrm{B2.p}, t _ {1}) \oplus \mathrm{D} (\mathrm{B2.f}, t _ {1})
$$

$$
\oplus - 1 * \mathrm{D} (\mathrm{B} 1. \mathrm{m}, \mathrm{t} _ {1}) \oplus - 1 * \mathrm{D} (\mathrm{B} 3. \mathrm{m}, \mathrm{t} _ {1})
$$

$$
= - \oplus 0 \oplus + \oplus - \oplus 0
$$

The uncertainty comes in by the values of $D(B2.m,t_{1})$ and $D(B2.f,t_{1})$ for which nothing is known about their strength, thus the result is still $\{-,0,+$ . Altogether with appropriate D-values for the other variables at $t_{2}$ we get the modified Table 3.

$D(B2.m,t_{2})$ propagates its value to $D(B1.m,t_{3})$ because nothing is known about the relation between the strength of $D(B1.m,t_{2})$ and $D(B2.m,t_{2})$ , therefore the usual rule for the addition is applied. On the other hand, $D(B3.f,t_{2})$ overrides the value of $D(B2.m,t_{2})$ , thus the result at $t_{3}$ is unique.

The example shows that by introducing knowledge about the strength of influences, which is sometimes at hand, the amount of uncertainty that arises in a deduction can be reduced. There could be other knowledge of this type, for instance about the relations between $D(\mathrm{Bi.m},\mathrm{t}_{j-1})$ and $D(\mathrm{Bi.p},\mathrm{t}_{j-1})$ as well as $D(\mathrm{Bi.f},\mathrm{t}_{j-1})$ , which would further reduce the uncertainty.

Qualitative propagation of changes with knowledge of strength of changes

<table><tr><td></td><td> $t_0$ </td><td> $t_1$ </td><td> $t_2$ </td><td> $t_3$ </td></tr><tr><td>D(B1.p,  $t_i$ )</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>D(B1.f,  $t_i$ )</td><td>+</td><td>0</td><td>0</td><td></td></tr><tr><td>D(B2.p,  $t_i$ )</td><td>+</td><td>0</td><td>0</td><td></td></tr><tr><td>D(B2.f,  $t_i$ )</td><td>0</td><td>+</td><td>+</td><td></td></tr><tr><td>D(B3.p,  $t_i$ )</td><td>0</td><td>-</td><td>0</td><td></td></tr><tr><td>D(B3.f,  $t_i$ )</td><td>0</td><td>0</td><td>+</td><td></td></tr><tr><td>D(B1.m,  $t_i$ )</td><td>0</td><td>+</td><td>+</td><td>{ -,0,+}</td></tr><tr><td>D(B2.m,  $t_i$ )</td><td>0</td><td>-</td><td>{ -,0,+}</td><td>{ -,0,+}</td></tr><tr><td>D(B3.m,  $t_i$ )</td><td>0</td><td>0</td><td>+</td><td>+</td></tr></table>

So far we have assumed that from one time to the next just one propagation step between each pair of adjacent nodes takes place. If we drop this restriction we get to a generalized model. We assume that information about the ratio between the duration of different propagation steps is given. This establishes a relation on the set of influences expressing the relative speed of the influences. For instance, if v \~ > x and w \~ > x are influences, D(v) and D(w) change from 0 to either + or -, and the change of D(w) needs double the time of D(v) to have an impact on D(x), then we say that v \~ > x is twice as fast as w \~ > x. This relation will be denoted by

$$
\mathrm{RS} \left(\text { infl } _ {1}, \text { infl } _ {2}, n\right)
$$

RS means relative speed. The expression states that $infl_{1}$ is n times faster than $infl_{2}$ . RS is reflexive and transitive in the first two arguments with appropriate values for the third one. Thus if $RS(infl_{1},infl_{2},n)$ then $RS(infl_{2},infl_{1},1/n)$ , and if $RS(infl_{1},infl_{2},n)$ and $RS(infl_{2},infl_{3},m)$ then $RS(infl_{1},infl_{3},n\cdot m)$ . In addition, from $RS(infl_{1},infl_{3},n)$ and $RS(infl_{2},infl_{3},n)$ it follows that $RS(infl_{1},infl_{2},1)$ . These properties allow for the propagation of speeds in a set of influences. Assume the following relations are given:

$$
\mathrm{RS} (\mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, \mathrm{B1.m} \sim > ^ {-} \mathrm{B2.m}, 2)
$$

$$
\mathrm{RS} (\mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, \mathrm{B1.m} \sim > ^ {-} \mathrm{B3.m}, 3)
$$

$$
\mathrm{RS} (\mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, \mathrm{B2.m} \sim > ^ {-} \mathrm{B1.m}, 2)
$$

$$
\mathrm{RS} (\mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, \mathrm{B2.m} \sim > ^ {-} \mathrm{B3.m}, 3)
$$

$$
\mathrm{RS} (\mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, \mathrm{B3.m} \sim > ^ {-} \mathrm{B1.m}, 2)
$$

$$
\mathrm{RS} (\mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, \mathrm{B3.m} \sim > ^ {-} \mathrm{B2.m}, 2)
$$

$$
\mathrm{RS} (\mathrm{B1.f} \sim > ^ {+} \mathrm{B1.m}, \mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, 1)
$$

$$
\mathrm{RS} (\mathrm{B2.p} \sim > ^ {-} \mathrm{B2.m}, \mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, 1)
$$

$$
\mathrm{RS} (\mathrm{B2.f} \sim > ^ {+} \mathrm{B2.m}, \mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, 1)
$$

$$
\mathrm{RS} (\mathrm{B3.p} \sim > ^ {-} \mathrm{B3.m}, \mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, 1)
$$

$$
\mathrm{RS} (\mathrm{B3.f} \sim > ^ {+} \mathrm{B3.m}, \mathrm{B1.p} \sim > ^ {-} \mathrm{B1.m}, 1)
$$

From these relations others can be derived using the properties of RS. For instance, RS(B3.p $\sim >^{-}$ B3.m, B2.m $\sim >^{-}$ B3.m, 3) holds by transitivity because RS(B3.p $\sim >^{-}$ B3.m, B1.p $\sim >^{-}$ B1.m, 1) and RS(B1.p $\sim >^{-}$ B1.m, B2.m $\sim >^{-}$ B3.m, 3). From RS(B1.p $\sim >^{-}$ B1.m, B1.m $\sim >^{-}$ B2.m, 2) we get by reflexivity RS(B1.m $\sim >^{-}$ B2.m, B1.p $\sim >^{-}$ B1.m, 1/2). Together with RS(B1.p $\sim >^{-}$ B1.m, B2.m $\sim >^{-}$ B3.m, 3) it follows that RS(B1.m $\sim >^{-}$ B2.m, B2.m $\sim >^{-}$ B3.m, 3/2). Fig. 2 illustrates the relations by arc labels augmented by those ratios that are different from 1.

The relative speeds of the influences describe various delays of their impacts. A marketing example where modelling of delays is needed is an incentive given to retailers by manufacturers where consequences show up in sales to consumers in a later period. Another example is consecutive sales of a brand complementary to another brand. A concrete example is a rise in market share of an inkjet printer followed by a rise in market share of the same manufacturer's printer ink. The delays can be projected on the time axis yielding points where the D-values of variables may change. In the above example we get the equidistant points $t_{0}$ , $t_{1}$ , $t_{2}$ , and $t_{3}$ . The computation of the D-values for these times yields results shown in Table 4. The activity of the different Brand processes at the times is obvious. Notice that these results have been achieved without any assumptions on the strength of the influences.

![](/api/attachments/MAFSJQJN/fulltext/images/cde33d1188cb006969c1590ad42cd45d764a1af9f409d83818b2c8e19495a27c.jpg)  
Fig. 2. Influence diagram with three brands and delayed influences.

Table 4  
Qualitative propagation of changes with delays

<table><tr><td></td><td> $t_0$ </td><td> $t_1$ </td><td> $t_2$ </td><td> $t_3$ </td></tr><tr><td>D(B1.p,  $t_i$ )</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>D(B1.f,  $t_i$ )</td><td>+</td><td>0</td><td>0</td><td></td></tr><tr><td>D(B2.p,  $t_i$ )</td><td>+</td><td>0</td><td>0</td><td></td></tr><tr><td>D(B2.f,  $t_i$ )</td><td>0</td><td>+</td><td>+</td><td></td></tr><tr><td>D(B3.p,  $t_i$ )</td><td>0</td><td>-</td><td>0</td><td></td></tr><tr><td>D(B3.f,  $t_i$ )</td><td>0</td><td>0</td><td>+</td><td></td></tr><tr><td>D(B1.m,  $t_i$ )</td><td>0</td><td>+</td><td>+</td><td>+</td></tr><tr><td>D(B2.m,  $t_i$ )</td><td>0</td><td>-</td><td>{ -,0,+}</td><td>{ -,0,+}</td></tr><tr><td>D(B3.m,  $t_i$ )</td><td>0</td><td>0</td><td>+</td><td>+</td></tr></table>

## 6. Implementation and future work

Currently we have built an interpreter that performs the evaluation of the directed proportionalities by propagation of the D-values. It makes use of the information about the relative strength of influences, which should be denoted under the constraints slot, to compute the sums according to the operation $\oplus$ . Model validity was tested with historical data used in the evaluation of SHANEX since for these data a human analysis, a statistical model, and a rule-based analysis exist. The tests revealed the following: The model described in Section 3 yielded the same results as SHANEX. This is of no surprise as the model is just a rewritten version of SHANEX. The extended model described in Section 4 was capable of correctly diagnosing some particular cases that SHANEX could not. These were the cases where the additional knowledge was crucial to explain the market share changes. However, these were just a few cases and it is not clear on that basis whether the extension really pays off. Therefore, a test on a larger data set is needed. This is also true for the model described in Section 5 which also needs further refinements. The current implementations are written in Scheme but we plan to move them to CLOS.

In addition, we are working on developing an editor and a presentation component. A new model consisting of a set of processes can be entered into the computer or an existing model can be modified using this editor. The editor presents the process frame in a partly graphical form with all slots that are required or that already exist. The user only has to fill in the slot values. The presentation component yields the result of a computation as a table. It also can produce a directed graph from the process definitions which sometimes is a more convenient representation of a system of processes than the textual one.

matical Bases for Qualitative Reasoning, IEEE Expert, April 1991, 11–19.

[9] B. Kuipers, Commonsense Reasoning about Causality: Deriving Behaviour from Structure, 169–203.

[10] G.L. Lilien, Ph. Kotler and K.S. Moorthy, Marketing Models (Prentice-Hall, Englewood Cliffs, N.J., 1992).

[11] J.M. McCann and J.P. Gallagher, Expert Systems for Scanner Data Environments (Kluwer, Boston, 1990).

[12] O. Raiman, Order of Magnitude Reasoning, in Proceedings of AAAI-88, 1988, 100–104.

[13] E. Sacks, Piecewise Linear Reasoning, in Proceedings of AAAI-87, 1987, 655–659.

[14] H. Simon and K.-H. Sebastian, Diffusion and Advertising: The German Telephone Company, Management Science 33, April 1987, 451–466.

[15] P. Struss, Problems of Interval-Based Qualitative Reasoning, in Weld/de Kleer (eds.), Qualitative Reasoning about Physical Systems (Morgan-Kaufmann, San Mateo, CA, 1990).

[16] L. Travé-Massuyès, Qualitative Reasoning from Different Aspects and Potential Applications to Decision Support Systems, in M.G. Singh, L. Travé-Massuyès, Decision Support Systems and Qualitative Reasoning, Proceedings of the IMACS International Workshop on Decision Support Systems and Qualitative Reasoning, Toulouse, 1991, 29-42.

## 7. For further reading

[16]

## References

[1] P. Alpar, Expert Systems in Marketing, Working Paper 86-16 of the College of Business Administration, University of Illinois at Chicago, 1986.

[2] P. Alpar, Knowledge-Based Modelling of Marketing Managers' Problem Solving Behaviour, Int. Journal of Research in Marketing 8, 1991, 5–16.

[3] L.G. Cooper and M. Nakanishi, Market-Share Analysis (Kluwer, Boston, 1988).

[4] J. de Kleer and J.S. Brown, A Qualitative Physics Based on Confluences, Artificial Intelligence 24 (1-3) 1984, 7–83.

[5] A.M. Farley and K.-P. Lin, Qualitative reasoning in Microeconomics: An Example, in M.G. Singh, L. Travé-Massuyès, Decision Support Systems and Qualitative Reasoning, Proceedings of the IMACS International Workshop on Decision Support Systems and Qualitative Reasoning, Toulouse, 1991, 303–306.

[6] K.D. Forbus, Qualitative Process Theory, Artificial Intelligence 24 (1-3) 1984, 85–168.

[7] D. Horsky and L.S. Simon, Advertising and the Diffusion of New Products, Marketing Science 1 (Winter 1983), 1–18.

[8] J. Kalagnanam, H.A. Simon and Y. Iwasaki, The Mathe-

![](/api/attachments/MAFSJQJN/fulltext/images/0db694d6ddf1635ff834b6240058613e520f296fce499d0a51860e53d432058e.jpg)

Paul Alpar is a Professor of Business Administration and Information Systems at Philipps-University, Marburg, Germany. Prior to that he was on the faculty of the Dep. of Information and Decision Sciences at University of Illinois at Chicago and held visiting positions at the universities of New Mexico, Albuquerque, Tel-Aviv, Israel, and Goethe, Frankfurt, Germany. He received his Ph.D. in Business Administration (specialization in

MIS) from Goethe-University, Frankfurt, Germany. His current research interests include application of artificial intelligence techniques to business problems (esp. in marketing) and economics of information technology use. He is member of TIMS and ACM.

![](/api/attachments/MAFSJQJN/fulltext/images/03cc48ebf2d3b56bf7324c3d3ec8b52ba1a3d03bd690c71f3d05e176adf24c98.jpg)

Werner Dilger is a Professor of Artificial Intelligence at Chemnitz-University of Technology, Chemnitz, Germany. He received his M.Sc. in Computer Science from the University of Karlsruhe, Germany, in 1974 and his Ph.D. in Computer Science from the University of Kaiserslautern, Germany, in 1982. He held research positions at the Universities of Konstanz and Kaiserslautern, at the Institute for German Language in Mannheim,

and at the Fraunhofer-Institute for Information and Data Processing in Karlsruhe. From 1989 to 1993 he was a Professor for Computer Science at the European Business School, Schloss Reichartshausen. He is a member of GI.
