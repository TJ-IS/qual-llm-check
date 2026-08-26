---
otero_id: 17212
otero_key: "VBJ673DS"
title: "Uncertainty techniques in expert system software"
authors: "William G.W. Magill; Stewart A. Leech"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90077-o"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Uncertainty techniques in expert system software

William G.W. Magill and Stewart A.

Leech

Department of Accounting and Finance, University of Tasmania, Hobart 7001, Tasmania, Australia

In this paper, approaches for dealing with uncertainty as implemented in two specific expert system tools are analysed with the aim of comparing the theories that underly the two approaches. The comparison undertaken shows that not only are their many conceptual problems that require consideration and understanding before selecting an expert system tool, but also the uncertainty techniques as implemented in two specific tools do not follow strictly the theories on which they are based.

Keywords: Expert systems, Expert system tools, Uncertainty techniques, Bayes' theorem, Certainty factors.

![](/api/attachments/VBJ673DS/fulltext/images/b6f08dce3d83f2204ed467408a6f93e03b85b22c5072972fcfae77241bb6ed7a.jpg)

William G.W. Magill is an Honorary Research Associate in the Department of Economics in the University of Tasmania, Australia. Together with over 20 years teaching and research experience at that university, he has held faculty positions at the Australian National University and the University of Oregon. His main teaching and research interests have been in business statistics, marketing and economics. Currently he is engaged in both private and university research which is principally directed towards marketing and knowledge-based decision support systems. He has been a co-author in articles published in Economics Letters, Economic Record, Economia Internazionale, Journal of Business Finance and Accounting, and The International Journal of Accounting.

![](/api/attachments/VBJ673DS/fulltext/images/e42bf678fd063cf48757f668898cde6a815f2bc412ece42b021d4c44c59dd156.jpg)

Stewart A. Leech is a Reader in the Department of Accounting and Finance in the University of Tasmania, Australia. He has held faculty positions at the University of Melbourne and the University of Sydney, and visiting scholar appointments at U.C.L.A., the University of Minnesota and the City University Business School, London. His primary teaching interest is management information systems. His current research interests include knowledge-based decision

support systems in accounting and auditing. He has published in a range of journals including Abacus, International Journal of Accounting, Journal of Business Finance and Accounting, and Accounting and Business Research. He has co-authored two books: Introduction to Accounting Method (Longman Cheshire 1984) and The TAC System (Longman Cheshire 1985).

## 1. Introduction

Expert systems are a branch of the field of artificial intelligence which seeks to develop computer-based systems that replicate the actions of human beings. Expert systems have been developed for a wide-spectrum of applications in a diverse number of fields. For example, Waterman [14] lists 181 different expert systems from the fields of agriculture, chemistry, computer systems, electronics engineering, geology, information management, law, manufacturing, mathematics, medicine, meteorology, military science, physics, process control and space technology.

There is a growing interest in using expert systems technology for business applications, in particular, for decision-making in economics, marketing, auditing, finance, and accounting. As a result of this surge of interest in expert systems a multitude of expert systems tools (EST's), that arguably can be adapted to a wide range of applications, are available on a variety of computers, including microcomputers. Thus, if we are interested in developing an expert system to assist with making decisions or judgments in fields such as auditing or finance, there are many EST's that could be chosen to build the expert system. Basically, knowledge may be represented in an expert system in a number of ways, the most common being production rules, frames and semantic nets. Production rules tend to dominate in most of the EST's available. In a rule-based system, knowledge is represented by a combination of rules which consists of IF statements (the evidence) and a THEN statement (the hypothesis). If the evidence is satisfied by the facts, the rule is 'fired' and the action specified in the THEN statement is inferred.

An integral feature of any EST is the manner in which it deals with uncertainty with respect to the evidence and the hypothesis, both at the time the expert system is built and at the time the expert system is being used. One of the earliest methods employed was probability theory based upon Bayes' Theorem, but this has limited appeal because of the practical difficulties of assessing the prior and conditional probabilities inherent in the theorem. In addition, strong arguments against the Bayes' approach have been concerned with the possible absence of independence between pieces of evidence on the one hand and between hypotheses on the other. To help overcome these shortcomings, other methods have been adopted using subjective probabilities based purely upon experience, while others have resorted to non-probabilistic methods.

A further technique for dealing with uncertainty has been devised by Shortliffe and Buchanan [10] for the MYCIN system. Their approach adopts estimates provided by experts which reflect the tendency of a piece of evidence to prove or disprove a given hypothesis. These estimates, which measure the increase in either belief or disbelief in some hypothesis as a result of observing the existence of some piece of evidence, are called Certainty Factors, and will be discussed more fully below.

The aim of this paper is to examine aspects of two approaches for dealing with uncertainty as implemented in two specific EST's, in order to compare that implementation with the theory that underlies the two approaches. In the paper an examination of the literature which deals with measures of uncertainty is followed by an analysis of the two specific EST's. The first, Expert Edge [5], employs a Bayesian approach to uncertainty while the second, Personal Consultant [12,13], adopts a certainty factor approach.

## 2. The literature

The problems of dealing with uncertainty in expert systems have been debated widely in the literature. Some expert system tools incorporate a mechanism for dealing with uncertainty that provides a measure of certainty, while others do not. Some argue that conclusions can mislead the user, or at least lead to a false sense of belief in the conclusions; others argue that since most decisions are made with some degree of uncertainty, it is necessary to include reasoning about uncertainty in an expert system that is intended to emulate human decision-making. In the forward to a volume on Uncertainty in Knowledge-Based Systems, which brought together many of the papers presented at the International Conference on Information Processing and Management of Uncertainty in Knowledge-Based Systems in Paris in 1986, Zadeh summed up the current state of affairs when he wrote: ‘...it is evident that the management of uncertainty in knowledge-based systems presents many complex and as yet not fully understood problems’. [15, p iv].

Discussions on the methods of dealing with uncertainty in expert systems are not simply restricted to comparing Bayesian probabilities and certainty factors. However, these two methods are still at the forefront of the debate on reasoning with uncertainty. The work undertaken in the 1970's by Shortliffe and Buchanan [10], Duda, Hart and Nilsson [2], and Shafer [9] was important in establishing the need to investigate, more fully, the methods of dealing with uncertainty in expert systems. Since then the debate has continued, with many articles and conferences on the subject. It is not intended, in this paper, to review each and every known method of reasoning with uncertain knowledge. However, it is worth noting that many methods have been proposed, such as Bayesian probabilities, certainty factors, the Dempster-Shafer theory of evidence, fuzzy set theory and others. These have been reviewed in, and debated by, contributors to Kanal and Lemmer [7] and Bouchon and Yager [1].

## 3. The two expert system tools

The two EST's used in the study are Expert Edge and Personal Consultant. The first uses probabilities based upon Bayes' Theorem for dealing with uncertainty while the second, based upon MYCIN, uses certainty factors. This section will discuss these two tools with particular emphasis on the two methods of dealing with uncertainty.

Both tools allow for the development of an expert system which consists of a number of rules, each being of the type:

$$
\begin{array}{l} \text {IF} \quad \text {‘evidence A’ AND / OR ‘evidence B’} \\ \text {AND / OR ‘...} \end{array}
$$

THEN'hypothesis'.

Not only may there be more than one piece of evidence associated with any one hypothesis, but the hypothesis itself may also become a piece of evidence in any ensuing rule. In addition, a piece of evidence may form a component of the IF statement associated with more than one hypothesis.

## 3.1. Expert Edge

When formulating the rules in an expert system built with Expert Edge, it is necessary to incorporate a number of probabilities associated with each and every rule. The first is the a priori probability of the hypothesis being true. Next, a pair of conditional probabilities must be specified for the first piece of evidence in the IF statement. These are (a) the conditional probability of that piece of evidence being true, given that the relevant hypothesis is also true; and (b) the conditional probability of that piece of evidence being true, given that the relevant hypothesis is false. There will be a pair of such conditional probabilities for each piece of evidence in the IF statement.

Expert Edge uses these probabilities in association with Bayes' Theorem to revise the a priori probability of the hypothesis being true to obtain the posteriori probability for that same hypothesis. For our purposes we shall refer to these two probabilities as the prior and revised probabilities respectively. In rules in which there is more than one piece of evidence it is assumed, prima facie, that such pieces of evidence are independent.

While Expert Edge is designed to revise the probability of each hypothesis being true, it does this only in association with the user. When using the expert system, the user is asked to place a measure on the current likelihood of a piece of evidence being true. If this happens to be 100% in all cases (indicating an answer ‘yes’ the evidence is true), then Bayes’ Theorem is applied directly to revise the prior probability. If the measure were anything other than 100% then the derivation of the revised probability is more complex. For example, an answer of ‘no’ (implying a measure of zero) would necessitate Expert Edge adopting the probabilities of the complements of the conditional events mentioned above, in order to use Bayes’ Theorem to revise the prior probability of the hypothesis. If the answer submitted by the user were anything between ‘no’ and ‘yes’, then Expert Edge uses the resultant measure (something between 0 and 100), to arrive at a revised probability based upon interpolating within the revised probabilities that would result from ‘no’ and ‘yes’ answers respectively.

It should be noted that the two conditional probabilities associated with each piece of evidence are in no way related. However, their relative values are of some significance to the degree to which any given prior probability is revised. The higher is the ratio of the two conditional probabilities the greater will be the increase in the probability of the hypothesis being true in the light of some particular piece of evidence. This aspect, which constitutes a possible connection with certainty factors used by Personal Consultant, has been examined theoretically by Duda et al. [2] who converted the Bayesian conditional probabilities into prior and posterior odds representing ratios as follows:

$$
\mathrm{O} (\mathrm{H}) = \left[ \mathrm{P} (\mathrm{H}) / (1 - \mathrm{P} (\mathrm{H})) \right], \quad \text { and }\tag{1}
$$

$$
\mathrm{O} (\mathrm{H} / \mathrm{E}) = \left[ \mathrm{P} (\mathrm{H} / \mathrm{E}) / (1 - \mathrm{P} (\mathrm{H} / \mathrm{E})) \right],\tag{2}
$$

assuming the evidence is true. Simple algebra based on these two relationships gives the odds-likelihood formulation of Bayes' Theorem:

$$
\mathrm{O} (\mathrm{H} / \mathrm{E}) = \mathrm{x}. \mathrm{O} (\mathrm{H}),\tag{3}
$$

where x is the likelihood ratio defined as

$$
\mathrm{x} = \mathrm{P} (\mathrm{E} / \mathrm{H}) / \mathrm{P} (\mathrm{E} / \text { not } \mathrm{H}).\tag{4}
$$

The likelihood ratio is in effect the ratio of conditional probabilities provided by the expert, given the evidence is true. The higher is this ratio the greater will be the influence of the observation of a true E on the odds of H.

This analysis highlights an important inconsistency in the Bayesian approach to uncertainty in expert systems. As Duda et al. (1976) showed, when updating the odds on H given that E is observed to be false, the following relationship is derived:

$$
\mathrm{O} (\mathrm{H} / \text { not   E }) = \mathrm{y.O} (\mathrm{H}), \quad \text { where }\tag{5}
$$

$$
\mathrm{y} = \mathrm{P} (\text { not   E / H }) / \mathrm{P} (\text { not   E / not   H }),\tag{6}
$$

which is the likelihood ratio associated with the evidence being false.

If the expert provides each conditional probability associated with any rule, the expert is also providing x and y. From the formulas for the two likelihood ratios, it can be seen that if x > 1 then y < 1 and vice versa. On the other hand however, Duda et al. state: 'People who work with rulebased inference systems are commonly told by experts that “The presence of E enhances the odds on H, but the absence of E has no significance”.[2, p. 1077]. This implies that although the expert says that x happens to be greater than unity, y is equal to unity. However, Duda et al. argue that x and y ‘...must be separately provided by the expert’. [2, p.1077]. This means that if y = 1, then x must also equal 1.

## 3.2. Personal Consultant

This tool is based upon MYCIN, which was designed to overcome the problems inherent in formulating the probabilities required by a Bayesian approach to uncertainty. The authors of MYCIN [10] developed concepts which they called 'certainty factors'. These measures, although defined in terms of probabilities, were intended to reflect the degree to which the user's belief or disbelief about a hypothesis being true was increased as a result of observing some piece of evidence. These measures were therefore intuitive reactions rather than values based upon long past experience and were intended (by definition) to be dynamic in a conditional context, (see below).

Unlike Expert Edge where probabilities are incorporated into the rules for all hypotheses and pieces of evidence by the expert, Personal Consultant requires the expert to set a certainty factor for each hypothesis only. However, where relevant, the expert stipulates those pieces of evidence which are such as to enable the user to apply certainty factors to them at the appropriate time. Whenever there is more than one piece of evidence in an IF statement, the system follows certain rules that determine how a revised certainty factor is obtained for the associated hypothesis (see Appendix B).

## 4. A review of the two uncertainty techniques

It is usual for any expert system to include a large number of rules, many of which contain hypotheses dependent upon more than one piece of evidence, and in which there are many instances where a hypothesis in one rule becomes a piece of evidence for another. These characteristics of an expert system make it imperative to understand the features of the uncertainty technique in the EST used for the development of the expert system.

## 4.1. The Bayesian Approach

As pointed out by Duda et al., 'The individual pieces of evidence (the E) and the hypothesis (H) of a rule are propositional statements. Instead of being either absolutely true or false, the truth values of the propositional statements may be uncertain.' [2, p.1075]. As mentioned above, the Bayesian approach attends to this situation by calling upon the expert to provide prior probabilities to all hypotheses as well as a pair of conditional probabilities for all pieces of evidence. Shortliffe and Buchanan state that the use of Bayes' theorem for manipulation of conditional probabilities '...requires either large numbers of valid background data or numerous approximations and assumptions.' [10, p.352]. This situation is compounded when there are rules with more than one piece of evidence, for if an expert system is to be useful when using Bayes' theorem, it is not only necessary to have comprehensive statistical data for the probabilities mentioned above, but it is also important to know something about any interrelationships which may exist between the pieces of evidence within that rule.

In addition to the uncertainty measures provided by the expert, information provided by the user may also be uncertain, and the Bayesian approach attempts to combine these two types of uncertainty. As stated by Duda et al. these attempts tend to lead to ‘...certain kinds of inconsistencies...that seriously jeopardise success’. [2, p. 1076]; and ...‘If the network contains multiple paths linking a given piece of evidence to the same hypothesis, the independence assumption is obviously violated’ [2, p. 1080].

Many of those concerned with uncertainty in EST's tend to consider that the difficulties inherent in setting probabilities are of such a magnitude that they dismiss the Bayesian approach outright. Shortliffe and Buchanan stated: ‘...vast portions of medical experience suffer from having so few data and so much imperfect knowledge that rigorous probabilistic analysis, the ideal standard by which to judge the rationality of a physician's decisions, is not possible’. [10, p. 352]. They qualified this statement, however, by adding that ‘We do not argue against the use of Bayes’ theory in those medical environments in which sufficient data are available to permit adequate use of the theorem'. [2, p. 356].

In summary, the problems inherent in the Bayesian approach to uncertainty in EST's are as follows. First, we have the need for the expert to quantify uncertainty in a probabilistic manner, basing judgments on long past experience and prohibitively large samples. Second, there is the requirement, for simplicity, to assume that two or more pieces of evidence in any rule are independent; and third, the algebraic requirement inherent in the Bayesian technique is contravened by the intuitive beliefs of experts in the field.

## 4.2. The Certainty Factor Approach

Certainty factors as used in MYCIN are, in effect, dynamic approximations to conditional probabilities. When discussing MYCIN, Shortliffe and Buchanan stated that 'Although conceived with medical decision making in mind, it is potentially applicable to any problem area in which real world knowledge must be combined with expertise before an informed opinion can be obtained to explain observations, or to suggest a course of action.' [10, p. 353].

Consider a simple rule in which there is one piece of evidence E in favour of a single hypothesis H. Given this simple model we now outline the development by Shortliffe and Buchanan [10] of the certainty factor concept. The discussion is based directly upon their article. The basic notation is as follows:

MB(H,E) = X means “The measure of increased belief in hypothesis H, based on evidence E, is X”.

MD(H,E) = Y means “The measure of increased disbelief in hypothesis H, based on evidence E, is Y”.

The above two concepts are defined in terms of traditional probabilities. The probability $P(H)$ is regarded as reflecting the expert's belief in H, which directly implies that $[1 - P(H)]$ would be an estimate of his disbelief in the validity of H.

Similarly, P(H/E) reflects the expert's conditional probability of H being true in the light of observing evidence E. When the revised probability P(H/E) is greater than P(H), then it follows that $[1 - \mathrm{P}(\mathrm{H}/\mathrm{E})]$ is less than $[1 - \mathrm{P}(\mathrm{H})]$ . In this case, as Shortliffe and Buchanan claim ‘...the expert’s Disbelief in H has decreased as a result of observing E’. [10, p. 360]. The measure of increased belief is thus defined as the proportionate decrease in disbelief as follows:

$$
\begin{array}{r l} \mathrm{MB(H,E)} & = \frac {[ 1 - \mathrm{P(H)} ] - [ 1 - \mathrm{P(H/E)} ]}{1 - \mathrm{P(H)}} \\ & = \frac {\mathrm{P(H/E)} - \mathrm{P(H)}}{1 - \mathrm{P(H)}}. \end{array}\tag{7}
$$

Similarly, the measure of increased disbelief is defined as the proportionate decrease in belief as follows:

$$
\begin{array}{l} \mathrm{MD(H,E)} = \frac {\mathrm {P(H) - P(H / E)}}{\mathrm{P(H)}}, \\ \text { which   follows   if } \mathrm {P(H / E) <   P(H)}. \end{array}\tag{8}
$$

Both MB(H,E) and MD(H,E) lie between 0 and 1, and since one piece of evidence cannot increase belief and disbelief at the same time, when MB(H,E) > 0, MD(H,E) = 0. Also when MD(H,E) > 0, MB(H,E) = 0. Furthermore, if P(H/E) = P(H), the evidence E is, by definition, independent of the hypothesis H and from equations 7 and 8, it can be seen that MB(H,E) = MD(H,E) = 0.

With these two measures we can now define the certainty factor associated with H given E as

$$
\mathrm{CF} (\mathrm{H}, \mathrm{E}) = \mathrm{MB} (\mathrm{H}, \mathrm{E}) - \mathrm{MD} (\mathrm{H}, \mathrm{E}).\tag{9}
$$

A certainty factor thus combines degrees of belief and disbelief into a single number which ranges between -1 and 1.

There is a number of types of rule structures which also need to be discussed. In the case of ‘parallel combination’ where there are two pieces of evidence E1 and E2 favouring hypothesis H, the two measures of increased belief and disbelief are defined respectively by

$$
\begin{array}{r l} \mathrm{MB(H,E1\&E2)} & = \mathrm{MB(H,E1)} + \mathrm{MB(H,E2)} \\ & \times [ 1 - \mathrm{MB(H,E1)} ], \end{array}\tag{and}
$$

(10)

$$
\begin{array}{r l} \mathrm {MD(H,E1\ & E2) = MD(H,E1) + MD(H,E2)} \\ & \times [ 1 - \mathrm {MD(H,E1)} ]. \end{array}\tag{11}
$$

Both these equations hold only when MD(H,E1 & E2) and MB(H,E1 & E2) respectively are not equal to unity.

Using the fact that $\mathbf{MB}(\mathbf{H},\mathbf{E})\mathbf{MD}(\mathbf{H},\mathbf{E})=0$ , we obtain the following equations for the relevant certainty factors:

$$
\begin{array}{r l} \mathrm{CF(H,E1\&E2)} & = \mathrm{CF(H,E1)} + \mathrm{CF(H,E2)} \\ & - \mathrm{CF(H,E1)CF(H,E2)}, \end{array}\tag{12}
$$

when both CF(H,E1) and CF(H,E2) are non-negative, and

$$
\begin{array}{r l} \mathrm{CF(H,E1\&E2)} & = \mathrm{CF(H,E1)} + \mathrm{CF(H,E2)} \\ & + \mathrm{CF(H,E1)CF(H,E2)}, \end{array}\tag{13}
$$

where both CF(H,E1) and CF(H,E2) are negative. For the case when CF(H,E1) and CF(H,E2) are of opposite signs, see Heckerman [3, p. 169].

In the case of ‘sequential combination’, a situation exists in which the hypothesis in one rule serves as evidence for a hypothesis in another rule. If we have a rule in which $E'$ is evidence for hypothesis E which, in turn, is evidence for hypothesis H in another rule, then the combined certainty factor $\mathrm{CF}(\mathrm{H},\mathrm{E}')$ is given by

$$
\mathrm{CF} (\mathrm{H}, \mathrm{E} ^ {\prime}) = \mathrm{CF} (\mathrm{E}, \mathrm{E} ^ {\prime}) \mathrm{CF} (\mathrm{H}, \mathrm{E}),\tag{14}
$$

where $CF(E,E')$ is non-negative. The definition for the case where $CF(E,E')$ is negative is more complex and will not be considered here (see Heckerman [3, p. 170]).

Two other situations should be mentioned briefly. First, there is the case in which one piece of evidence E bears on more than one hypothesis, say H and H'. Here the measures of belief and disbelief are defined as follows:

$$
\mathrm{MB} (\mathrm{H} \& \mathrm{H} ^ {\prime}, \mathrm{E}) = \min \left[ \mathrm{MB} (\mathrm{H}, \mathrm{E}), \mathrm{MB} (\mathrm{H} ^ {\prime}, \mathrm{E}) \right],\tag{15}
$$

and

$$
\mathrm{MD} (\mathrm{H} \& \mathrm{H} ^ {\prime}, \mathrm{E}) = \max \left[ \mathrm{MD} (\mathrm{H}, \mathrm{E}), \mathrm{MD} (\mathrm{H} ^ {\prime}, \mathrm{E}) \right].\tag{16}
$$

The corresponding CF's can be calculated using equation (9) above.

Second, there is the case where the truth or falsity of a piece of evidence E is not known with certainty, but a certainty factor based upon prior evidence e is known, reflecting the degree of belief in E. In this example, e may be thought of as the current state of information available to an individual, as distinct from some specific piece of evidence which imposes directly on a hypothesis. Then if MB'(H,E) and MD'(H,E) are, respectively, the measures of belief and disbelief in H when E is known to be true with certainty (i.e. they are decision rules acquired from the expert), then the actual measures of belief and disbelief are given by

$$
\mathrm{MB} (\mathrm{H}, \mathrm{E}) = \mathrm{MB} ^ {\prime} (\mathrm{H}, \mathrm{E}) \max [ 0, \mathrm{CF} (\mathrm{E}, \mathrm{e}) ],\tag{17}
$$

$$
\mathrm{MD} (\mathrm{H}, \mathrm{E}) = \mathrm{MD} ^ {\prime} (\mathrm{H}, \mathrm{E}) \max [ 0, \mathrm{CF} (\mathrm{E}, \mathrm{e}) ].\tag{18}
$$

This criterion is similar to the sequential combination mentioned earlier. Once again the relevant certainty factor is obtained simply by applying equation (9) above.

The above discussion on certainty factors is not intended to encompass the entire theory expounded by Shortliffe and Buchanan [10], but is intended rather as a basis for highlighting the disparities between the two approaches to uncertainty.

In general, certainty factors are acquired from an expert who is asked to weight his belief in the parameter of each THEN statement reflecting the degree of certainty he affixes to that conclusion. Regardless of the definition above, such a weighting is not to be interpreted as a conditional probability in the traditional context, for experts tend to contravene the axioms of probability theory concerning complementary events when they are asked to weight their belief in the conclusion not being true given the same premise. Shortliffe and Buchanan claim that ‘...the weights are judgmental measures that reflect a level of belief’ [10, p.358].

It can be shown that, given equation (9) above, $CF(h,e) + CF(\text{not } h,e)$ does not equal 1, which reflects the most significant departure from the Bayesian approach to uncertainty. On the other hand ‘...when the a priori belief in a hypothesis is small, (i.e., $P(h)$ is close to zero), the certainty factor of a hypothesis confirmed by evidence is approximately equal to its conditional probability on that evidence’. [10, p. 363].

Any discussion on techniques for dealing with uncertainty would not be complete without some mention of work by Horvitz and Heckerman [4] and Heckerman [3]. Heckerman (1986) appreciated that a ‘...primary goal in creating the MYCIN certainty factor model was to provide a method for handling uncertainty which avoided the requirement for large amounts of data and the intractability of computation associated with general probabilistic reasoning'. [3, p. 167]. He asserts that the certainty factors discussed in Shortliffe and Buchanan's original work lacked consistency, which in turn lead to confusion when they were used in other applications. This confusion arose from the inappropriate use of certainty factors as measures of absolute belief. The Shortliffe and Buchanan definition clearly shows them to be measures of a change in belief (see equations (7) to (9) above).

Horvitz and Heckerman [4] addressed this problem by outlining a set of properties that they considered adequately defined the concept of an absolute belief on the one hand and the concept of a belief update on the other. Basically they claimed that ‘...an individual’s degree of belief in some proposition or hypothesis H should depend on the particular hypothesis itself…’ and ‘...the current state of information of the individual possessing the belief. Therefore, we will use the term H/e to represent the degree of absolute belief for hypothesis H by an individual with information e’. [4, p. 140]. They go on to consider four other properties which, are virtually axioms of probability theory.

Horvitz and Heckerman [4] define a belief update in terms of a hypothesis H given some specific evidence E and prior information e. In so doing they derive the following odds-likelihood form of Bayes' theorem:

$$
\mathrm{O} (\mathrm{H} / \mathrm{E}, \mathrm{e}) = \mathrm{x} (\mathrm{H}, \mathrm{E}, \mathrm{e}). \mathrm{O} (\mathrm{H} / \mathrm{e}),\tag{19}
$$

where $x(H,E,e)$ is the likelihood ratio that relates the prior odds of H to the posterior odds in the same way as Duda et al. [2] treat the Bayesian approach above. Horvitz and Heckerman [4] assert that experts implicitly assume that a belief update is independent of other information, and so drop e from the analysis. This allows them to state that

$$
\mathrm{x} (\mathrm{H}, \mathrm{E}, \mathrm{e}) = \mathrm{x} (\mathrm{H}, \mathrm{E}).\tag{20}
$$

They further derive a probabilistic interpretation of certainty factors from their axioms by saying that $\mathrm{CF}(\mathrm{H},\mathrm{E})$ is some function F of the likelihood ratio $\mathrm{x}(\mathrm{H},\mathrm{E})$ , where function F maps the range of value from 0 to infinity that the likelihood ratio x assumes, into the interval $[-1, 1]$ . This gives them:

$$
\begin{array}{r l} \mathrm{CF(H,E)} & = \mathrm{F} \left\{\mathrm{x(H,E)} \right\} \\ & = \left\{ \begin{array}{l l} \left\{\mathrm{x(H,E)-1} \right\} / \mathrm{x(H,E)}, & \quad \mathrm{x} \geqslant 1 \\ \mathrm{x(H,E)-1}, & \quad \mathrm{x< 1} \end{array} \right. \end{array}\tag{21}
$$

## 5. A Summary

The above analysis highlights a possible theoretical link between the two approaches to the problem of uncertainty in expert system tools. That link is the likelihood ratio.

Following Duda et al. [2], the likelihood ratio measures the degree to which the odds on a hypothesis H are altered given evidence E [see equation (3)]. In Expert Edge, the likelihood ratio can be derived directly from the relative magnitudes of the conditional probabilities acquired from the expert [equation (4)] and, since the underlying probabilities can be recovered from their odds by the formula

$$
\mathrm{P} (\mathrm{H} / \mathrm{E}) = \left[ \mathrm{O} (\mathrm{H} / \mathrm{E}) / (\mathrm{O} (\mathrm{H} / \mathrm{E}) + 1) \right],\tag{22}
$$

the likelihood ratio also reflects the relationship between the prior and revised probabilities of the hypothesis. That is, the likelihood ratio reflects the functional relationship between P(H) and P(H/E) in Bayes' Theorem. The additional revision of P(H/E) in the light of the user's uncertainty about E is another matter.

On the other hand, the Horvitz and Heckerman (1986) discussion specifies the certainty factor for H given E, in a purely definitional context, as a function of the likelihood ratio. That is, the likelihood ratio is the argument of the function in equation (21) above.

If the two conditional probabilities are known as in Expert Edge, then the two likelihood ratios x and y can be derived directly, and vice versa. On the other hand, if we are given certainty factor CF(H,E), then from equation (21) above, the associated conditional probabilities could be derived using the following relationships:

$$
\mathrm{P} (\mathrm{E} / \mathrm{H}) = [ \mathrm{x} (1 - \mathrm{y}) ] / (\mathrm{x} - \mathrm{y}) \quad \text { and }\tag{23}
$$

$$
\mathrm{P} (\mathrm{E} / \text { not   H }) = (1 - \mathrm{y}) / (\mathrm{x} - \mathrm{y}).\tag{24}
$$

However, this is possible only if both x and y are provided and are non-negative.

While all this might be intuitively appealing in the theoretical context of a simple rule in which there is just one piece of evidence bearing upon a hypothesis, it becomes less appealing when two or more pieces of evidence in an IF statement are considered. In the Bayesian approach the odds on H, given multiple independent evidence, is a function of the product of a set of likelihood ratios (see equation 7 in appendix A). In the certainty factor approach, the likelihood equivalent in the F function (equation 21) is not so readily apparent.

With this rather tenuous and, arguably useful, link between the two approaches to uncertainty in expert systems, let us now turn to the two EST's under consideration.

Expert Edge applies the Bayesian approach to the letter of the law in rules consisting of just one piece of evidence. However, when two or more pieces of evidence arise, Expert Edge does not follow the independence assumption inherent in equations (6) to (9) in Appendix A. Rather, the procedure adopted is as follows.

In a rule in which there are two pieces of evidence E1 and E2 associated with hypothesis H, Expert Edge first considers E1 and, in the light of the user's response, derives a revised probability for H. When Expert Edge considers E2, the revised probability for H in the light of evidence E1 becomes the prior probability of H, and after the user's response regarding E2, revises this already revised probability of H.

In the event that H is a piece of evidence for some other hypothesis, the procedure is very much the same except that Expert Edge uses the (doubly) revised probability of H (the evidence in the second rule) as a surrogate response from the user. The user is not asked for any assessment whatsoever.

As far as Personal Consultant is concerned the certainty factor for the parameter of a hypothesis applied by the expert is a belief update, whereas the certainty factors applied to parameters in the IF statement by the user are absolute beliefs in the evidence given current knowledge. When there are two or more parameters in the IF statement, a simple rule is invoked, as outlined in Appendix B, to determine the CF for the IF statement as a whole. Thus equations (12) and (13) above are not applied. In this case the associated likelihood ratio x could be derived using (21) above, but, in the absence of CF(H/not E), not the likelihood ratio y. For this reason it is not possible to derive the inherent conditional probabilities by means of equations (23) and (24).

When revising the expert's CF for the hypothesis in the light of the user's responses, Personal Consultant continues to deviate from the theory above. Abstracting from the situation in which CF(prev) is non-zero (see Appendix B), Personal Consultant derives a new certainty factor for the hypothesis by simply multiplying the certainty factor for the IF statement by that acquired from the expert for the hypothesis (see equation 1 in Appendix B). There is a case for arguing however, that by applying equation (9) to equations (17) and (18) above, we would derive an expression for CF(new) that reflects the Personal Consultant approach.

## 6. Conclusion

In this paper, the problem of choosing between uncertainty techniques incorporated in expert system tools has been raised. A comparison of uncertainty techniques available in two expert system tools has been undertaken and the differences examined. This comparison has shown that not only are there many conceptual and practical problems, but the techniques as implemented in the two specific tools do not follow strictly the theories on which they are based. These problems require careful consideration and understanding before selecting an EST that is to be used in building expert systems which are to incorporate the use of uncertainty measures.

## Appendix A

Expert Edge and Bayes' Rule

Consider an expert system in which there is one piece of evidence (E1) associated with hypothesis (H). Then if the user responds by saying 'Yes' the evidence (E1) is true, the prior probability P(H) is revised using Bayes' Theorem

$$
\begin{array}{r l} & \mathrm {P(H / E1)} \\ & = \frac {(E 1 / H) P (H)}{P (E 1 / H) P (H) + P (E 1 / n o t H) P (n o t H)}, \end{array}\tag{1}
$$

where (not H) represents the complement of the event (H); that is, the hypothesis is false. If the user's answer to the question about (E1) is 'No', indicating that (E1) is false, then P(H) is revised by means of

$$
\begin{array}{r l} \mathrm {P(H / not E1) = \{P(not E1 / H)P(H)\}} \\ & \times \{\mathrm {P(not E1 / H)P(H)} \\ & + \mathrm {P(not E1 / not H)P(not H)} \} ^ {- 1}, \end{array}\tag{2}
$$

where (not E1) represents the complement of (E1); that is the evidence (E1) is false.

If the user's answer is somewhere between 'Yes' and 'No' and responds by submitting a value 'z', where 'z' lies between 0 and 1, then P(H) is revised by means of

$$
\begin{array}{r l} \mathrm {P(H / E1^ {*}) = P(H/not E1)} & \\ & + z [ \mathrm {P(H / E1) - P(H/not E1)} ], \end{array}\tag{3}
$$

where (E1\*) is evidence (E1) as perceived by the user.

This shows that Expert Edge first revises P(H) for both the 'Yes' and 'No' answers and then generates a value between these two revised probabilities using an interpolation procedure based upon the value given by the user when answering the question about the evidence (E1).

Now consider a situation in which there is a second piece of evidence (E2) bearing upon hypothesis (H). After the user responds with, say, a value of 'r' reflecting the likelihood of (E2) being true, Expert Edge adopts P(H/E1\*) given by equation (3) as the prior probability of hypothesis (H) and proceeds to revise this probability in exactly the same manner as outlined above in the case for (E1). If, for simplicity, we denote P(H/E1\*) by P\*(H), the second revised probability of hypothesis (H) is given by

$\mathrm{P(H / E2^{*})}$

$$
\begin{array}{r l} & = \mathrm{P} ^ {*} (\mathrm{H} / \text {not E2}) \\ & \quad + \mathrm{r} [ \mathrm{P} ^ {*} (\mathrm{H} / \mathrm{E2}) - \mathrm{P} ^ {*} (\mathrm{H} / \text {not E2}) ], \end{array}\tag{4}
$$

where (E2\*) denotes evidence (E2) as perceived by the user. This means that in the light of the user's responses about both (E1) and (E2), the revised probability given by equation (4) is in effect P(H/E1\* & E2\*).

Now assume that hypothesis (H) is evidence in another rule, bearing on some hypothesis (K). If we denote the value of the revised probability derived in equation (4) by 'w', then this value is used by Expert Edge as a measure of the likelihood of the evidence (H) being true. The user is not asked for any response as to the likelihood of (H) being true. The revised probability for (K) is given by

$$
\begin{array}{r l} \mathrm {P(K / H^ {*}) = P(K/notH)} \\ & + \mathrm {w[P(K / H) - P(K/notH)],} \end{array}\tag{5}
$$

where $(\mathrm{H}^{*})$ is evidence (H) as ‘perceived’ by Expert Edge through equation (4).

Much discussion in the literature has been concerned with the assumption that all pieces of evidence in any rule, and therefore all conditional events, are independent. To appreciate the implications of this assumption consider a rule in which n pieces of evidence E1,E2,,,En bear on hypothesis H. Then, given the conditional independence assumption:

$$
\begin{array}{r l} & \mathrm {P(E1,E2,E3,,En / H)} \\ & = \mathrm {P(E1 / H).P(E2 / H).P(E3 / H)...\cdot P(En / H)}, \end{array}\tag{6}
$$

and similarly for the case where H is false. This means that the odds on H are updated by the expression:

$$
\mathrm{O} (\mathrm{H} / \mathrm{E} 1, \mathrm{E} 2, \mathrm{E} 3,,, \mathrm{En}) = \mathrm{Z}. \mathrm{O} (\mathrm{H}),\tag{7}
$$

where Z is the product of the set of n likelihood ratios derived from the conditional probabilities provided by the expert given that all pieces of evidence are true. Using the definition for the odds likelihood form of Bayes Rule, it can be shown that

$$
\mathrm{P} (\mathrm{H} / \mathrm{E} 1, \mathrm{E} 2,,, \mathrm{En}) = \mathrm{Z} / \left[ \left\{1 / \mathrm{O} (\mathrm{H}) \right\} + \mathrm{Z} \right].\tag{8}
$$

Similarly it can be shown that in the case where all pieces of evidence are false

$$
\begin{array}{r l} \mathrm {P(H / not E1,not E2,,,not En)} \\ & = \mathrm{Y} / \left[ \left\{1 / \mathrm{O} (\mathrm{H}) \right\} + \mathrm{Y} \right], \end{array}\tag{9}
$$

where Y is the product of the set of n likelihood ratios derived from the conditional probabilities provided by the expert given that all pieces of evidence are false. Even abstracting from the need to incorporate a potentially large number of user's responses, this differs considerably from the approach adopted by Expert Edge.

## Appendix B

## Personal Consultant

In this expert system tool the expert applies a certainty factor (CF) to the parameters in each of the then statements only. The user may assign CF's to parameter values during consultation where those parameters have been given a certainty-factor range property by the expert. The resultant certainty factor for the IF statement will depend upon whether there is more than one premise in that statement, and whether such premises are combined by AND or OR functions.

For an IF statement to be true, its CF must exceed the default value of 20. (In Personal Consultant the CF's are numbers which lie within the range of -100 and 100). Where the IF statement premises are combined by means of an AND function, each premise must be true in order for the IF statement to be true. The CF of the IF statement is the minimum CF of the premises. Where the premises of the IF statement are combined by means of the OR function, the CF of the IF statement is the maximum CF of the premises.

When the conditions of the IF statement are found to be met, that is, it is true with a CF exceeding 20, the action or actions in the THEN statement are taken and a new CF for the parameter in the THEN statement is calculated. This is achieved by combining the appropriate CF's according to the equations below.

The appropriate CF's are

\- the CF of the IF statement,

\- the CF of the THEN statement provided by the expert,

\- any previously existing CF for the parameter value in the THEN statement.

A previous CF for the parameter exists, except when the parameter being assigned a value either has not had this value assigned to it before, or has a previous value with an associated CF of zero.

Thus, before the THEN statement is performed there may be three CF's. The CF of the IF statement (generated by the user), the CF of the parameter in the THEN statement (acquired from the expert), and CF(prev) of the parameter in the THEN statement obtained on some prior occasion. In the absence of any such CF(prev), the CF acquired from the expert is adjusted to derive the CF(new) for the parameter in the THEN statement by means of the formula

$$
\begin{array}{r l} \mathrm{CF(new)} & = [ \text { CF   of   IF   statement } * \text { CF   of   THEN } \\ & \quad \text { parameter } ] / 1 0 0. \end{array} \tag {7}\tag{1}
$$

If the CF(prev) exists and is of the same sign as CF(new), the CF(new) is further revised to obtain CF(rev) by means of the following formula:

$$
\mathrm{CF} (\text { rev }) = \mathrm{CF} (\text { previous }) + \mathrm{R},\tag{2}
$$

where R is a revision factor and is one of the following:

If CF(prev) and CF(new) are both positive or zero:

$$
\mathrm{R} = \left[ \mathrm{CF} (\text { new }) * (1 0 0 - \mathrm{CF} (\text { prev })) \right] / 1 0 0.\tag{3}
$$

If CF(prev) and CF(new) are both negative:

$$
\mathrm{R} = \left[ \mathrm{CF} (\text { new }) * (1 0 0 + \mathrm{CF} (\text { prev })) \right] / 1 0 0.\tag{4}
$$

Finally we have two cases in which the product of CF(prev) and CF(new) is negative, they are of opposite signs.

If the sum of CF(prev) and CF(new) is positive, then:

$$
\begin{array}{r l} \mathrm{CF} (\text { rev }) & = \left\{\mathrm{CF} (\text { prev }) + \mathrm{CF} (\text { new })\right) * 1 0 0 \\ & \quad + [ 1 0 0 - \mathrm{MIN} ] / 2 \} \\ & / (1 0 0 - \mathrm{MIN}). \end{array}\tag{5}
$$

If the sum of CF(prev) and CF(new) is negative, then:

$$
\begin{array}{r l} \mathrm{CF} (\text { rev }) & = \left\{\mathrm{CF} (\text { prev }) + \mathrm{CF} (\text { new })\right) * 1 0 0 \\ & - [ 1 0 0 - \mathrm{MIN} ] / 2 \} \\ & / (1 0 0 - \mathrm{MIN}), \end{array}\tag{6}
$$

$$
\text { where } \mathrm{MIN} = \min (| \mathrm{CF} (\text { prev }) |, | \mathrm{CF} (\text { new }) |).
$$

## Acknowledgements

This research was supported by research funds from the University of Tasmania. Helpful comments were received from participants in research workshops at the University of Tasmania and the University of Alberta.

## References

[1] B. Bouchon and W.R. Yager (Eds), Uncertainty in Knowledge-based Systems Springer-Verlag, 1987, New York.

[2] R.O. Duda, P.E. Hart and N.J. Nilsson, “Subjective Bayesian Methods for Rulebased Inference Systems” Proceedings, National Computer Conference Vol 45, AFIPS, 1976, pp. 1075–1082.

[3] D. Heckerman, “Probabilistic Interpretations for Mycin’s Certainty Factors” in L.N. Kanal and J.F. Lemmer (Eds) Uncertainty in Artificial Intelligence North-Holland, 1986, pp. 167–196.

[4] E. Horvitz and D. Heckerman, “The Inconsistent use of Measures of Certainty in Artificial Intelligence Research” in L.N. Kanal and J.F. Lemmer (Eds), Uncertainty in Artificial Intelligence 1986, North-Holland, pp. 137–151.

[5] Human Edge Software Corporation, Expert Edge Manual for the IBM Personal Computer, 1985, California.

[6] R.W. Johnson, "Independence and Bayesian Updating Methods" in L.N. Kanal and J.F. Lemmer (Eds) Uncer-

tainty in Artificial Intelligence, 1986, North-Holland, pp. 197–201.

[7] L.N. Kanal and J.F. Lemmer (Eds), Uncertainty in Artificial Intelligence, 1986, North-Holland.

[8] E.P.D. Pednault, S.W. Zucker and L.V. Muresan, “On the Independence Assumption Underlying Subjective Bayesian Updating” Artificial Intelligence Vol 16, 1981, pp. 213–222.

[9] G. Shafer, A Mathematical Theory of Evidence Princeton University Press, 1976, Princeton N.J.

[10] E.H. Shortliffe and B.G. Buchanan, “A Model of Inexact Reasoning in Medicine” Mathematical Biosciences Vol 23, 1975, pp. 351–379.

[11] M. Stefik, J. Atkins, R. Balzer, J. Benoit, L. Birnbaum, F. Hayes-Roth and E. Sacerdoti, “The Architecture of Expert Systems”, being Ch. 4 of F. Hayes-Roth, D.A. Waterman and D.B. Lenat (Eds), Building Expert Systems Addison-Wesley, 1983, Reading Massachusetts.

[12] Texas Instruments, Personal Consultant Reference Guide, 1986, Dallas Texas.

[13] Texas Instruments, Personal Consultant Series Technical Report, 1986, Dallas Texas.

[14] D.A. Waterman, A Guide to Expert Systems Addison-Wesley, 1986, Reading Massachusetts.

[15] L.A. Zadeh, forward to B. Bouchon, and W.R. Yager (Eds) Uncertainty in Knowledge-based Systems, 1987, Springer-Verlag, New York.
