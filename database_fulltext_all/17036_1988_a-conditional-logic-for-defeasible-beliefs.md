---
otero_id: 17036
otero_key: "PT2GUNMZ"
title: "A conditional logic for defeasible beliefs"
authors: "M Belzer"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90102-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Conditional Logic for Defeasible Beliefs

Marvin BELZER \* and Barry LOEWER \*\*

\* Advanced Computational Methods Center, University of Georgia, Athens, GA 30602, USA

\*\* Department of Philosophy, University of South Carolina, Columbia, SC 29208, USA

This paper provides a framework for representing beliefs by distinguishing between (i) the defeasible principles of a belief system, (ii) the propositions that are beyond reasonable doubt in a belief state, and (iii) the propositions 'favored' on the basis of defeasible principles and those propositions that are beyond reasonable doubt. Defeasible principles are interpreted semantically by means of a Lewis-style ranking of worlds (without the assumption that the actual world is among the 'innermost', or most highly ranked, worlds). The 'favored closure' (F-closure) of a set of defeasible principles and reasonable propositions is non-monotonic. Yet, given the concept of 'pruning' the default ranking relative to a set of worlds (determined by what is beyond reasonable doubt in a particular belief state) we provide a formal characterization of the conditions under which in inference to a favored conclusion on the basis of defeasible rules and reasonable propositions, is warranted. The adequacy of our representation of defeasible principles can be tested by considering a number of valid formulas that we list. We show that our concept of defeasible principle parallels but is not identical to the concept of 'relatively high conditional probability'. An example of application of the formal language and semantics is given, and the final parts of the paper contain discussion of a computational implementation of the theory.

![](/api/attachments/PT2GUNMZ/fulltext/images/c11899e1efd1cddd7631792d703105206a6f85f78b9ce7d4d0dc58f98da04afd.jpg)

Marvin Belzer is a CDC Pacer Postdoctoral Fellow in the Advanced Computational Methods Center of the University of Georgia. He received a B.A. from Northwest Nazarene College in 1974 and a Ph.D. in philosophy from Duke University in 1984. A former Fulbright scholar, his research interests lie in normative systems, logic, and automated reasoning.

## 1. Introduction

Reasoning is a change in beliefs, preferences, and plans with a view towards improving their coherence. A system of logic characterizes some notion of validity and lays down rules so that reasoning can be evaluated. There is reasoning to form beliefs in which as we accumulate evidence we may withdraw a proposition formerly believed. Even among propositions not believed some may be more reasonably accepted than others, and as new things are learned a proposition may become more or less reasonable. Similarly as we accumulate evidence our plans may change. As is illustrated below, some types of reasoning involve defeasible principles and are non-monotonic. Here we investigate a logic for belief systems that contain defeasible principles. Our aims are (i) to describe a framework for representing and appraising beliefs, (ii) introduce principles of inference, and (iii) characterize a notion of validity.

## 2. 'Beyond Reasonable Doubt', 'Favored', and Defeasible Principles

As Chisholm has pointed out, there are three perspectives that may be taken towards a given proposition at any particular time (so far as belief is concerned):

(1) one may believe (or accept) the proposition; (2) one may disbelieve the proposition, and this is the same thing as accepting its negation; or (3) one may withhold or suspend belief – that is to say, one may refrain from believing and from disbelieving the proposition. $^{1}$

To say that Sally accepts (or believes) that Fred is in Tanzania is to formulate a description of Sally. On the other hand we sometimes use evaluative terms in comparing different beliefs (or potential beliefs) 'with respect to reasonableness':

Thus we may say that one belief is more reasonable than another, or, more exactly, that one belief is more reasonable for a given person at a given time than is another belief. As alternatives to 'more reasonable than', we might also use 'epistemically better than' or 'epistemically preferable to'. $^{2}$

One such evaluative term is ‘beyond reasonable doubt’. Even if Sally actually does not believe that Esther is in Somalia, the proposition that Esther is in Somalia may be beyond reasonable doubt for her (at a certain time); if so, it is something she could believe without being unreasonable and perhaps would believe were she ideally rational. Chisholm’s definition of ‘beyond reasonable doubt’ is as follows:

p is beyond reasonable doubt for $S =_{df}$ Accepting p is more reasonable for S than withholding p. $^{3}$

This means that $p$ is beyond reasonable doubt for $S$ just in case accepting $p$ is more reasonable for $S$ than neither accepting $p$ nor accepting $\tilde{p}$ .

A second evaluative term, ‘favored’, is weaker than ‘beyond reasonable doubt’ in that any proposition that is beyond reasonable doubt will be favored, but not conversely (some favored propositions are not beyond reasonable doubt). Even if the proposition that Daphne is in Ruanda is neither accepted by, nor beyond reasonable doubt for, Sally (at a certain time) it may be that accepting that proposition would be more reasonable for her than accepting its negation (if she had to choose). In that case we will say the proposition is favored for her (at that time).

p is favored for $S =_{df}$ Accepting p is more reasonable for S than accepting $\tilde{p}$ .

This concept is important because often one must act in situations in which one's information is incomplete (neither $p$ nor $\tilde{p}$ is beyond reasonable doubt) and yet one's decisions may be dependent upon the assumptions that are made concerning $p$ . In such situations it is useful to know that $p$ is favored (i.e., that accepting $p$ would be more reasonable than accepting $\tilde{p}$ ). Useful as the category may be, we are expressing 'only faint epistemic praise' when we say that a proposition falls within this category, as Chisholm points out:

in saying that believing is more reasonable than disbelieving we may be saying only that the former is the lesser evil, epistemically. Consider, for example, the proposition that the Pope will be in Rome on the third Tuesday in October five years from now. Believing it, given the information we have now, is more reasonable than disbelieving it, i.e., it is more reasonable to believe that the Pope will be in Rome at that time than it is to believe that he will not be there. But withholding the proposition, surely, is more reasonable still. $^{6}$

The favorability of a proposition often can be established by a type of reasoning that depends upon defeasible principles (also known as ‘rules of thumb’ or defaults), e.g., ‘Normally the pope is in Rome’. A defeasible principle may be accepted and used legitimately even when it is known that there are possible situations in which the principle should not be used. $^{7}$ Suppose for instance that Sally believes that

(1) Quincy, who does not get along well with Penrose, tends not to go to parties that Penrose goes to;

and she also believes that

(2) Quincy tends to go to parties that Rachel goes to (even if Penrose also is in attendance).

Now if the proposition $p$ (Penrose is going to a certain party) is beyond reasonable doubt for Sally at a time $t$ at which $r$ (Rachel is going to the party) is not beyond reasonable doubt, then (given no further relevant information) the proposition $\tilde{q}$ , that Quincy will not go to the party, is favored because of the defeasible principle (1). This does not mean, of course, that $\tilde{q}$ is beyond reasonable doubt; it means only that accepting $\tilde{q}$ would be more reasonable for Sally than accepting $q$ . If Sally were to have to act on either the assumption that $q$ or the assumption that $\tilde{q}$ , it would be more reasonable for her at $t$ to act on the assumption that $\tilde{q}$ . However at a later time $t^*$ when both $p$ and $r$ are beyond reasonable doubt for Sally, then $q$ is favored and $\tilde{q}$ is not, due to principle (2) which intuitively has greater 'weight' than (1).

## 3. Semantics

We want now to provide a logic, 'General Doxastic Logic' (GDL), for these concepts. To the language of propositional logic we add the one-place modal operators S and L, and the dyadic operator → read as follows:

Sp: p is beyond reasonable doubt.

$Lp: p$ is favored.

$p \to q$ : if $p$ then (defeasibly) $q$ .

We also add a dyadic operator $V(-,-)$ to form expressions $V(q,p)$ used in detaching conclusions about what is favored. The central semantical ideas for interpreting these expressions are a function F which assigns to persons $^{9}k$ (at a given time) and propositions p a set of propositions $F_{k}(p)$ and a function R that assigns to a belief state k the set of propositions that are beyond reasonable doubt for k. We will suppose that $R(k)$ is closed under the usual Boolean operations. $F_{k}(p)$ is the set of propositions that p tends to confirm for k. We will, for the moment, suppose that F need not be defined for all propositions and place no restrictions on F with the exception that it be defined for the tautological proposition. The expressions in the language are evaluated relative to k (at a given time). The key truth clauses read as follows: $^{10}$

(i) $p \to q$ is True at $k$ iff $q \in F_k(p)$ , (ii) $Sp$ is True at $k$ iff $p \in R(k)$ , (iii) $V(q, p)$ is True at $k$ iff for all $r \in R(k)$ for which $F_k(p \& r)$ is defined, $q \in F_k(p \& r)$ ,

(iv) Lq is True at k iff there is a $p \in R(k)$ such that $p \to q$ , Sp, and $V(q, p)$ are true at k.

GDL is a comprehensive formal system for representing reasoning in belief systems. $p \rightarrow q$ is ‘defeasible’ because of the invalidity of

(augmentation) $p \to q \supset (p \& r) \to q$ .

Two additional invalidities are

(transportation) $p \rightarrow q \supset \tilde{q} \rightarrow \tilde{p}$ ,

and

(chaining) $p \to q \& q \to r \supset p \to r$ .

As we will see $\rightarrow$ also can be used to express the idea that one defeasible rule overrides (or ‘defeats’) another.

## 4. Detachment

In GDL defeasible rules are formulated by conditionals $p \rightarrow q$ which say that p provides a reason, other things being equal, for favoring q (even if q is not beyond reasonable doubt). The fundamental idea is that in determining what is favored for k one needs to look at the defeasible principles and reasonable propositions for k. On our account Lq holds at k iff there is a p beyond reasonable doubt at k for which $p \rightarrow q$ holds relative to k and is not overridden. Consider how GDL represents conflicts between defeasible principles and reasoning with conflicts. In the example involving Quincy, $F_{k}(p) = \{\tilde{q}\}$ and $F_{k}(p \& r) = \{q\}$ and $R(k) = \{p, r, \ldots\}$ . So (given F defined for no other propositions) we also have Lq. Given suitable definitions of validity the following inference scheme is valid:

$$
\begin{array}{l l} \text {(Key)} & p \to q \\ & S p, \\ & V (q, p), \\ \text {So} & L q. \end{array}
$$

Key connects statements that say that one has some reason to expect a certain state of affairs with conclusions about what one ought to favor all things considered. The third premise of course is crucial because the sentence

$$
(\mathbf {d} - \mathbf {m p}) p \rightarrow q \&S p \supset L q
$$

is not valid in the semantics. Nonetheless, as the example shows, there are belief states in which the presence of $p \to q$ and $Sp$ can warrant an inference to $Lq$ . The 'warranting conditions' are spelt out by the truth condition for $V(q, p)$ - the inference is warranted at $k$ just so long as there is no proposition $c$ such that both $\tilde{[}(q\&c) \to q]$ and $Sc$ are true relative to $k$ . Thus in the example (which contains both $Sp$ and $Sr$ ) the inference to $Lq$ on the basis of $p \to q$ and $Sp$ is not warranted because of the falsity of $(p\&r) \to q$ . It is natural to say in that case that the rule $p \to q$ is 'defeated' in the example. In general,

$p \to q$ is defeated at $k$ just in case there there is some proposition $c$ such that both $Sc$ and $\tilde{[}(p \& c) \to q]$ are true at $k$ .

If a rule is defeated in a belief state, then inferences based on that rule will not be warranted. $^{12}$

Defeasible rules can be defeated because the various defeasible rules of a system may be of unequal importance. The relative importance, or 'relative weight', of two rules can be determined as follows:

$p \rightarrow q$ has greater relative weight in a system k than $r \rightarrow s$ if, and only if, $p \& r \& ^{(q \equiv s)} \rightarrow q$ is true relative to k and $p \& r \& ^{(q \equiv s)} \rightarrow s$ is not true relative to k. $^{13}$

Suppose for instance that we add to our example the defeasible principles that Sophie tends to go to parties that Rachel goes to, and also Thomas tends to accompany Utne,

$$
r \rightarrow s,
$$

$$
u \rightarrow t.
$$

And suppose that one is in a belief state in which both $r$ and $u$ are reasonable, $Sr$ and $Su$ , as is the proposition that one but not both of Sophie and Thomas will come to the party, $S^{\sim}(t \equiv s)$ . Now if $u \to t$ has greater relative weight than $r \to s$ , which by our definition means

$$
r \&u \&^ {\sim} (t \equiv s) \rightarrow t,
$$

then in this situation one would be warranted in concluding Lt (assuming that no other reasonable propositions or rules are relevant).

## 5. Non-monotonicity of F-closure

Let the ‘favored closure’ (‘F-closure’) of a set x of defeasible rules and reasonable propositions be the set of (favored) propositions that are entailed by s. F-closure is non-monotonic in the sense that a set x may be included in a set x even though the F-closure of x is not included in the F-closure of $x^{*}$ . For instance let x be the deductive closure of the set of defeasible rules in the Quincy example $\{p \rightarrow \sim q, (p \& r) \rightarrow q\}$ together with the closure of $\{Sp\}$ ; and let $x^{*}$ include x as well as the deductive closure of $\{Sp, Sr\}$ . The sentence $L^{\sim}q$ is contained in the F-closure of x, but it is not contained in the F-closure of $x^{*}$ . The non-monotonicity of F-closure reflects the fact that as evidence accumulates, conclusions favored on earlier evidence may have to be relinquished. An inference to Lq may also be said to be ‘non-monotonic’, if by this we mean that an inference to Lq may be valid relative to a set x (as in the example just described) even though it is not valid relative to a superset set $x^{*}$ of s.

## 6. The Weakness of GDL

The logic of $\rightarrow$ contains only the following two rules concerning substitution

RCOEA.

RCOEC.

$$
\begin{array}{l}\frac {P \equiv P ^ {\prime}}{P \rightarrow Q} \equiv P ^ {\prime} \rightarrow Q,\\\frac {Q \equiv Q ^ {\prime}}{P \rightarrow Q} \equiv P \rightarrow Q ^ {\prime}.\end{array}
$$

GDL is based on an austere conditional logic $^{14}$ that not only fails to validate ‘agglomeration’, ‘transposition’, ‘chaining’, and ‘d-modus ponens’ (mentioned above) but also validates none of the following schemas concerning → :

$$
\begin{array}{l} T \to T, \qquad (T \text {representing tautologies}) \\ p \to T, \\ p \to p, \\ p \to (q \supset r). \supset (p \to q) \supset (p \to r), \\ p \to q \& T \to p. \supset T \to q, \qquad (\mathrm{d-detachment}) \\ p \to q \supset^ {\sim} (p \to^ {\sim} q), \\ ^ {\sim} (p \to^ {\sim} T), \end{array}
$$

$$
\begin{array}{l}p \rightarrow q \&p \rightarrow r. \supset p \rightarrow (q \&r), \quad (\text {agglomeration})\\p \rightarrow (q \&r). \supset p \rightarrow q \&p \rightarrow r, \quad (\text {decomposition})\\p \rightarrow q \&r \rightarrow q \supset (p \vee r) \rightarrow q,\\(p \vee r) \rightarrow q \supset p \rightarrow q \vee r \rightarrow q,\\p \rightarrow q \&^ {\sim} (p \rightarrow^ {\sim} r) \supset (p \&r) \rightarrow q, \quad (\text {str} ^ {*})\end{array}
$$

Although GDL can be used to represent basic defeasible reasoning, it is so weak that there are important types of reasoning that cannot be represented. In fact we would like to suggest that each of the schemas in the above list would be accepted in a logic that provides both a useful conception of consistency in belief systems as well as standards for evaluating defeasible reasoning. Various conditions can be placed on the function F to validate these schemas. To validate all of them in one fell swoop we introduce the following semantical framework.

## 7. The Lewis-based Semantics 3Db.

The core of the new semantics is the idea that a belief system induces a ranking on possible worlds according to ‘normality’ relative to the defeasible principles of the belief system. The semantics is modelled on the semantics developed by David Lewis for subjunctive conditionals in [7]. We assume that there is associated with any belief system k a weak ordering $S_{k}$ of worlds we call the default field of normality for k. Defeasible principles are evaluated relative to belief systems, as follows:

$p \to q$ is true relative to a belief system $k$ just in case there is some $(p \& q)$ -world in $S_k$ ranked more highly than any $(p \& \tilde{q})$ -world.

This means that $p \rightarrow q$ is true relative to k just in case all of the ‘most normal’ worlds (relative to the default assumptions of the belief system i) at which p is true are worlds at which q is true.

Lewis suggested we think of the ranking of worlds in $S_{k}$ as a system of embedded spheres. In our application the innermost sphere in $S_{k}$ is the set of 'most normal' worlds relative to the belief system $k$ . It is important to see that the actual world need not be included in this set – for the actual world can be surprising. The divergence between default assumptions and facts explains

the invalidity of

$$
(* \mathbf {M P}) (A \rightarrow B) \supset (A \supset B),
$$

and it is the invalidity of \*MP that distinguishes default assumptions $A \rightarrow B$ from ordinary subjunctive conditionals A > B, for which it is usually assumed that

$$
(\mathbf {M P}) \quad A > B \supset (A \supset B).
$$

This difference is represented semantically by rejecting a condition on systems of spheres that the actual world always is at least one of the innermost worlds. $^{15}$ The logic of defeasible principles expressed by rules of the form $p \rightarrow q$ and $p + q$ is Lewis' conditional logic VTA. $^{16}$ In the following section of this paper we consider some theorems of VTA that can be used to test our claim that this logic is the correct logic for defeasible rules.

Now let us consider the propositions beyond reasonable doubt for k. In our possible worlds semantics we assume there is a set of worlds – the ‘range of accessibility for k’ – that are compatible with what is beyond reasonable doubt for k. We can use the accessible set for k to provide a truth condition for expressions of the form Sp, relative to k:

$^{15}$ Both of the Lewis conditions 'centering' (the actual world is the only world in the innermost sphere) and 'weak centering' (the actual world is among the worlds in the innermost sphere) therefore must be rejected in our application of the Lewis semantics to belief systems; but at least one of them typically is accepted in applications to subjunctive conditionals. However this is the only difference in the two applications. Lewis points out that rejection of the centering and weak centering conditions is appropriate for deontic (normative) systems which is this respect are similar to belief systems. The theory of defeasible reasoning that we are presenting in this paper is based partly on other papers in which we formulated a logic for defeasible reasoning in normative systems, cf. [3,4,12,13].

$^{16}$ cf. [10], p. 130–132. Lewis' preferred logic for subjunctive conditionals is VW, which does validate (MP). In discussing the suitability of conditional logics in a theory of defeasible reasoning, Nute claims that 'we cannot use VW or any of its close relatives to represent defeasible reasoning' [16], p. 473. It is true that any conditional logic that, like VW, validates (MP) will fail to represent defeasible reasoning correctly; but VTA does not validate (MP) and as we argue here is otherwise suitable for the task. But we agree with Nute's claim that we need 'a restricted procedure for detaching the consequent of a defeasible rule, and nothing of the sort is offered by conditional logics', p. 473. It is for this reason that we extend VTA with the introduction of the additional modal operators S, L, and V and additional inference principles including 'key' from section 4.

Sp is true relative k just in case p is true at each of the worlds in the accessible set for k.

This means that Sp is true at k just in case p is a member of the set of logical consequences of what is beyond reasonable doubt for k. $^{17}$ Because falsehoods may sometimes be beyond reasonable doubt, $^{18}$ we cannot assume that the actual world is included in the accessible set for k and therefore

$$
(\mathbf {R}) \quad S p \supset p
$$

is not valid. If however we assume that for any (coherent) belief state k there is a non-empty range of accessibility for k, then we validate

$$
\left(\mathbf {R} ^ {\prime}\right) \quad S p \supset^ {\sim} S ^ {\sim} p.
$$

The logic of S (considered alone) is Chellas' logic KD. $^{19}$

We turn now to what is favored for k. The following idea lies at the heart of our semantics. Let the ‘favored field of normality for k’ be the ranking of worlds that results when the default field $S_{k}$ for k is pruned by removing from $S_{k}$ each world that is not in the range of accessibility for k. Let the set of ‘favored worlds’ for k be the set of most highly ranked worlds in the favored field for k. This set is used to provide truth conditions for L, relative to k, as follows:

Lp is true at k just in case p is true at each of the favored worlds for k.

Since the favored field for k is determined completely by the default field for k and the range of accessibility for k, the favored conclusions for k are determined completely by the defeasible rules of the system k together with what is beyond reasonable doubt for k. The operator L is similar to S in that the actual world may not be favored for k, so that

$$
(\mathbf {r}) \quad L p \supset p
$$

fails; but it is reasonable to assume that there will be a non-empty set of favored worlds for any coherent state in any belief system, so

$$
\left(\mathbf {r} ^ {\prime}\right) \quad L p \supset - L - p
$$

should be valid. The logic of L also is KD. The 'key' inference schema from section 4 remains valid in the new semantics. (See the appendix of this paper for a more formal treatment of the semantics of 3Db.)

## 8. Theorems and Features of Defeasible Principles

There are a number of features of our formalization of the concept of 'defeasible principle' that can be used to test its adequacy. None of the following schemas is valid in the semantics

(mp)

$$
p \rightarrow q \&p \supset q.\tag{str}
$$

$$
p \rightarrow q \supset (p \&r) \rightarrow q,\tag{trans}
$$

$$
p \rightarrow q \supset^ {\sim} q \rightarrow^ {\sim} p,\tag{ch}
$$

$$
p \rightarrow q \&q \rightarrow r \supset p \rightarrow r.
$$

On the other hand of the following is valid:

$$
\begin{array}{l l}\left(\operatorname{str} ^ {*}\right)&p \rightarrow q \&p + r \supset (p \&r) \rightarrow q,\\\left(\operatorname{trans} ^ {*}\right)&p \rightarrow q \&T + \tilde {\sim} q \supset \tilde {\sim} q \rightarrow \tilde {\sim} p,\\\left(\operatorname{ch} ^ {*}\right)&p \rightarrow q \&q \rightarrow r \&T + p \supset p \rightarrow r.\end{array}
$$

The suitability of interpreting defeasible default principles by means of the Lewis ranking of worlds can be tested by examining whether these schemas should always hold in applications to actual reasoning systems that contain defeasible rules. Consider for instance (str\*). It tells us that if we assume as a rule of thumb, for instance, 'red sky at night, sailor's delight',

$$
r \rightarrow d,
$$

and if we do not have a rule, say, 'red sky at night, the mosquitoes will not bite', $\tilde{(r \to \tilde{b})}$ , that is,

$$
r + b,
$$

then it follows 'red sky at night and the mosquitoes bite, sailor's delight':

$$
(r \&b) \rightarrow d.
$$

This may seem like a counterexample to (str\*), because the premises seem acceptable (so we have heard) whereas the conclusion is unacceptable. However, we must consider whether $r + b$ , that is $\tilde{(r \to \tilde{b})}$ , actually would be acceptable relative to a belief system that contains $r \to d$ and to which the application is being made. Could there be any 'most normal' $r$ -worlds for that system at which mosquitoes bite? On the contrary, it would seem that mosquitoes would not be a problem in the relevant r worlds (the 'normal' ones); after all, a sailor typically being at sea, normal red skies are viewed far from mosquito-infested swamps, $r \rightarrow \sim s$ . No matter what color the sky may be sailors do not expect to encounter mosquitoes: $T \rightarrow \sim b$ , likewise even if the sky happens to be red, $r \rightarrow \sim b$ . And of course 'red sky at night and near a mosquito infested swamp, sailor's nightmare'

$$
(r \&s) \rightarrow^ {\sim} d,
$$

is perfectly consistent with $r \to d$ . However, we cannot settle these nautical matters here. The example does not convince us of the intuitive invalidity of str\* because the second premise is not clearly acceptable; and yet if it were regarded as acceptable then that would seem to be adequate grounds for rejecting the first premise $r \to d$ (folklore notwithstanding) since, after all, in that case even given $r$ it might be that $b$ , in which case $\tilde{~d}$ .

## 9. Defeasible Rules and Probabilities

It may be tempting to think of a default rule $p \to q$ as expressing a probabilistic relationship between $p$ and $q$ , the probability that $q$ given $p$ is high' which can be represented as

$$
P r (q / p) > n,
$$

for a suitably large $n$ (perhaps .5). What is the relationship between the expressions $\Pr(q/p) > n$ and $p \to q$ ? In this section we will explore the hypotheses that $p \to q$ can be identified with $\Pr(q/p) > n$ for some suitable $n$ .

The two notions are not identical, but there are some parallels. The probabilistic counterparts of the invalid formulas str, ch, and trans also fail:

$$
\begin{array}{l l} \text {(str +)} & \operatorname * {P r} (q / p) > n \supset \operatorname * {P r} (q / p \& r) > n, \\ \text {(ch +)} & \operatorname * {P r} (q / p) > n \& \operatorname * {P r} (r / q) > n \supset \\ & \operatorname * {P r} (r / p) > n, \\ \text {(trans +)} & \operatorname * {P r} (q / p) > n \supset \operatorname * {P r} (\tilde {\sim} p / \tilde {\sim} q) > n. \end{array}
$$

Also if $q$ entails $r$ , then

$$
\operatorname * {P r} (q / p) > n \supset \operatorname * {P r} (r / p) > n,
$$

and

$$
\operatorname * {P r} (p / r) > n \supset \operatorname * {P r} (p / q) > n,
$$

both hold universally, as do the corresponding

relationships between default rules:

$$
p \rightarrow q \supset p \rightarrow r,
$$

and

$$
r \rightarrow p \supset q \rightarrow p.
$$

But there also are significant differences between defeasible rules and the expressions of probability. The probabilistic analog to our valid (str\*), namely

$$
\begin{array}{r l} & (\mathrm{str} ^ {*} +) \mathrm{Pr} (q / p) > n \& \tilde {} [ \mathrm{Pr} (\tilde {r} / p) > n ] \\ & \supset \mathrm{Pr} (q / p \& r) > n \end{array}
$$

fails as do also the analogs to (ch\*) and (trans\*). The schema

$$
p \rightarrow q \&r \rightarrow q \supset (p v r) \rightarrow q
$$

is valid in the Lewis weak ordering semantics, but its probabilistic analog

$$
\begin{array}{l} \operatorname * {P r} (q / p) > n \& \operatorname * {P r} (q / r) > n \supset \operatorname * {P r} (q / p v r) > n \\ \text { fails. } \end{array}
$$

As noted above, default rules can be compared with respect to their 'weight' (or importance) in a system of default assumptions (in 3Db, $p \to q$ has greater relative weight than $r \to s$ in a system $k$ just in case $(p \& q \& (r = s)) \to r$ is true in $i$ ). A corresponding probabilistic notion,

$$
\begin{array}{r l} \operatorname * {P r} (q / p) & > \operatorname * {P r} (s / r) \text {   iff   } \operatorname * {P r} (q / p \& r \& ^ {\sim} (s \equiv q)) \\ & > \operatorname * {P r} (s / p \& r \& ^ {\sim} (s \equiv q)) \end{array}
$$

does not hold. $^{20}$ However the probabilistic analog to the definition of relative weight for default assumptions whose antecedent is T does hold (recall that in 3Db, $T \rightarrow p$ has greater relative weight than $T \rightarrow q$ just in case $\tilde{(p \equiv q) \rightarrow p}$ ):

$$
\begin{array}{r l} \operatorname * {P r} (p) & > \operatorname * {P r} (q) \text {   iff   } \operatorname * {P r} \bigl (p / ^ {\sim} (p \equiv q) \bigr) \\ & > \operatorname * {P r} \bigl (q / ^ {\sim} (p \equiv q) \bigr). ^ {2 1} \end{array}
$$

We conclude that $p \rightarrow q$ is not the same notion as $\Pr(q/p) > n$ , for suitably high n, even though there are some interesting parallels between the two notions. $^{22}$

## 10. An example

To consider a simple example (adapted from [17]), suppose that before a certain election you assume as a default that Wilson will win the election,

$$
T \rightarrow w,
$$

that Thorpe will win if Wilson does not win,

$$
\tilde {w} \rightarrow t,
$$

that Heath will win if neither Wilson nor Thorpe does so,

$$
\tilde {w} \&\tilde {t} \rightarrow h,
$$

and that there is going to be one and only one winner. To determine the default field of normality consider first these eight types of worlds:

<table><tr><td>1</td><td>w</td><td>t</td><td>h</td></tr><tr><td>2</td><td>w</td><td>t</td><td> $\tilde{h}$ </td></tr><tr><td>3</td><td>w</td><td> $\tilde{t}$ </td><td>h</td></tr><tr><td>4</td><td>w</td><td> $\tilde{t}$ </td><td> $\tilde{h}$ </td></tr><tr><td>5</td><td> $\tilde{w}$ </td><td>t</td><td>h</td></tr><tr><td>6</td><td> $\tilde{w}$ </td><td>t</td><td> $\tilde{h}$ </td></tr><tr><td>7</td><td> $\tilde{w}$ </td><td> $\tilde{t}$ </td><td>h</td></tr><tr><td>8</td><td> $\tilde{w}$ </td><td> $\tilde{t}$ </td><td> $\tilde{h}$ </td></tr></table>

In the default field we can rank worlds by their type. Because it is assumed that there will be one and only one winner worlds of types 1, 2, 3, 5, and 8 can be ranked equally at the bottom of the field; and the appropriate ranking is:

$$
(f 1) \quad 4 <   6 <   7 <   (1, 2, 3, 5, 8).
$$

If in state k1 there are no relevant propositions beyond doubt (so that worlds of each of the eight types are in the range of accessibility), then this field also serves as the favored field, and the 'favored worlds' are the accessible worlds of type 4. Thus $Lw$ , $L^{\sim}t$ , and $L^{\sim}h$ are true relative to k1.

Suppose now that you arrive home to catch the tail end of Thorpe's concession speech, but you do not hear to whom he has conceded. It now is beyond reasonable doubt that $\tilde{t}$ , Thorpe is not going to win. $S\tilde{t}$ holds relative to the new belief state k2; $\tilde{t}$ is true at each world in the range of accessibility for k2. We prune f1 by eliminating each world type that no longer is accessible (that is, by eliminating the world types from f1 that make t true):

$$
(f 2) \quad 4 <   7 <   (3, 8).
$$

This change does not alter any unconditional expectations, as $Lw$ , $L^{\sim}t$ , and $L^{\sim}h$ remain true. It does however alter a conditional expectation since $L(t\&\tilde{h}/\tilde{w})$ was true relative to the favored field for k1 (field f1) whereas $L(h\&\tilde{t}/\tilde{w})$ is true relative to the favored field (f2) for k2. $^{23}$ However it is reasonable to suggest that even though $L(h\&\tilde{t}/\tilde{w})$ is true after $\tilde{t}$ was accepted, nevertheless it would be appropriate to hold the 'counterfactual' expressed by $L(\tilde{w}>t\&\tilde{h})$ . The reasoning is as follows: one still expects Wilson to win, and while one now expects Heath to win if Wilson loses, it still would be reasonable to believe that if Wilson had not been (going to be) the winner, then you wouldn't have heard Thorpe's concession speech (because Thorpe would have won). This belief is reasonable precisely because of the nature of the default field f1. Thus our semantics provides a formal representation, as well as an account, of Stalnaker's distinction in [17] between a 'conditional belief', $L(h\&\tilde{t}/\tilde{w})$ , and a 'belief in a conditional', $L(\tilde{w}>t\&\tilde{h})$ .

To consider an alternative version of the story, suppose that you arrive home to near Wilson conceding, but do not hear to whom he has conceded. We prune f1 by eliminating all the world types that make w true, and the field f3 results:

$$
(f 3) \quad 6 <   7 <   (5, 8).
$$

Given the new evidence, both $Lw$ and $L^t t$ are rejected; and both $L^w w$ and $Lt$ become true. If to your surprise you learn that Thorpe also lost, then f3 itself is pruned by eliminating world types at which Thorpe wins:

$$
(f 4) \quad 7 <   8
$$

is the resulting field, according to which Lh. (In this simple example, the non-monotonicity of F-closure is illustrated several times.)

## 11. Computational Prototype

An extension of the 3Db based theory of defeasible reasoning to a quantified language has been implemented as part of a PROLOG practical reasoning system called 3dpr. Defeasible rules $p \to q$ and $p + q$ of the 'belief' component are represented by means of a dyadic PROLOG predicates $b(q, p)$ and $c(q, p)$ respectively. The ordinary PROLOG 'facts' ( $p$ ) and 'rules' ( $q: -p$ ) represent reasonable propositions $Sp$ and $S(p \supset q)$ respectively. Finally favored propositions $Lp$ are represented by a monadic predicate $l(p)$ . $^{24}$

The belief component of 3dpr has two main parts: the first part 'fills gaps' in a 'belief code' and the second contains rules that govern reasoning with the 'filled in' code. Although we can give only a general overview of the program here, each of these parts will be discussed briefly in turn.

## 12. Gaps

A ‘belief code’s is defined to be a set of sentences of the form $b(-,-)$ and $c(-,-)$ . Given a finite belief code

$$
B = \left\{x 1, x 2, \dots , x n \right\},
$$

there are two separate problems falling under the heading 'filling in gaps': (i) some 3Db consequences of B will not be included in B and yet should be available for reasoning, and (ii) there are norms that are not 3Db consequences of B but nevertheless should be used in reasoning that is based on B. Expressed in terms of the 3Db semantics, the two problems are (i) to be able to use defeasible rules that are true in any ranking of worlds that makes true each of the members of B, and (ii) to be able to use defeasible rules that, while not true relative to all of the rankings that satisfy B, are nonetheless true in the ranking (or in each of the rankings) than can be selected as satisfying B more successfully than do any of the other rankings that satisfy B.

Consider for instance the simple belief code $B^{*}=\{b(q,p),b(r,p)\}$ . To interpret the two rules semantically it is sufficient to consider the following eight types of worlds:

<table><tr><td>1</td><td>p</td><td>q</td><td>r</td><td>, r</td><td>r</td><td>r</td><td>, r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>p</td><td>q</td><td>, q</td><td>r</td><td>r</td><td>p</td><td>q</td><td>r</td><td>r</td><td>r</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>p</td><td>q</td><td>, q</td><td>r</td><td>r</td><td>p</td><td>q</td><td>q</td><td>r</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>p</td><td>q</td><td>, q</td><td>r</td><td>r</td><td>p</td><td>q</td><td>q</td><td>r</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>p</td><td>q</td><td>, q</td><td>r</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td>t</td><td></td></tr><tr><td>6</td><td>p</td><td>q</td><td>, q</td><td>r</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>p</td><td>q</td><td>, q</td><td>r</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>p</td><td>q</td><td>, q</td><td>r</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>r</td><td>p</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td>q</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Given the 3Db truth condition, the rule $p \to q$ will hold relative to any ranking of these eight world-types that ranks either 1 or 2 more highly than both 3 and 4, whereas $p \to r$ will hold relative to any ranking that ranks 1 or 3 more highly both 2 and 4. Thus $B^*$ is satisfied by any ranking that meets both of these conditions. The rule $p \to (q \& r)$ also will hold relative to any such ranking, but it is not included in $B^*$ - hence the first problem of gap filling.

For the second type of gap, consider $T \rightarrow p$ which is true in some of the rankings that satisfy $B^{*}$ , for instance

$$
1 <   (2 - 8).
$$

But it is false relative to other rankings that satisfy $B^{*}$ , for instance

$$
(1, 8) <   (2 - 7)
$$

which makes $T \to p$ false since some most highly ranked worlds (those of type 8) are $\tilde{p}$ worlds. Now if it can be shown that some of the rankings that satisfy $B^*$ do so more successfully than others, then it may turn out that certain defeasible rules are true in each of those most successful rankings for $B^*$ even though they are not true in all of the rankings that satisfy $B^*$ . We will suggest below that this is indeed the case – some principle which will be proposed have the consequence that, for instance, in none of the preferred rankings for $B^*$ is $T \to p$ true.

Each of these gap-filling problems receives a partial solution in the program 3dpr (which also offers parallel solutions to parallel problems for codes containing defeasible norms).

(i) The first problem is tackled directly by a procedure 'sweep' and indirectly by the 3Db-based inference rules in the program. The rule 'sweep' invokes a number of procedures that add new defeasible principles to the database (before reasoning with the code commences; reasoning subsequently takes place relative to the 'swept' code). For instance, if $B$ contains both $b(q, p)$ and $b(\tilde{q}, (p, r))^{25}$ the rule 'extend-str' ensures that the sept code also contains $o(\tilde{r}, p)$ in accord with the following 3Db validity:

$$
\left(\operatorname{str} ^ {\wedge}\right) \quad p \rightarrow q \&(p \&r) \rightarrow^ {\sim} q \supset p \rightarrow^ {\sim} r.
$$

The defeasible rules added to the database in this manner can be important insofar as they make possible derivations that are valid (relative to the 3Db) which otherwise would fail. To continue the example, if $B$ contains only $b(q, p)$ and $b(\tilde{q}, (p, r))$ , and if the only 'fact' derivable in the database is $p$ , then we can derive 'l( $^{r}$ )' after the code has been swept (but not before). Other procedures add rules in accordance with the theorems ch\* and str\* listed above, as well as

$$
\left(\mathrm{eq}\right) \quad p \rightarrow q \&q \rightarrow p \supset [ p \rightarrow r \equiv q \rightarrow r ].
$$

After sweeping the original code B with the resulting swept code B1, the code B1 itself can be swept with the result B2. Of course B2 also can be swept, and so on. To limit this process the number of iterated sweepings can be specified as is deemed useful.

(ii) The second gap-filling problem exists only if it is true that, of all the rankings that are compatible with each of the defeasible rules in B, one (or some) of the rankings more successfully satisfies B than do others. The suggestion that this is indeed the case is based on a number of default assumptions. The first is the ‘libertine’ assumption:

## Libertine

$c(q, p)$ is true relative to any code $B$ unless $\tilde{c}(q/p)$ , that is, $b(\tilde{q}, p)$ , is entailed by $B$ .

Given the libertine assumption it is possible to select, for any code B, a ‘unique’ ranking for B that satisfies the defeasible rules in B more successfully than any other ranking. Let SB be the set of rankings that satisfy B. The ‘unique’ ranking <B for a code B is the ranking x in SB that meets the following condition:

for each possible history h, h is ranked as highly in x as in any ranking y in SB.

This means that the unique ranking $< B$ for $B$ will rank each world as highly as is logically compatible with the defeasible rules in $B$ . $^{26}$

The libertine assumption taken alone has the consequence that $b(r, p)$ holds relative to a code B only if $b(r, p)$ is true in each of the weak orderings that are compatible with all of the elements of B. For this reason the libertine assumption is too permissive. Suppose for instance $B = \{b(s, p), b(q, r)\}$ where the propositions s, p, q, and r are logically independent. There will be rankings of worlds that satisfy both of the beliefs in B but fail to satisfy $b(s, (p \& r))$ . Hence, according to the libertine assumption, $\tilde{b}(s, (p \& r))$ . This is a counterintuitive result, for B contains a defeasible rule, $b(s, p)$ , that tends to confirm s given p; and it contains no additional rule that undermines this rule. Also needed therefore is the assumption of ‘inertia’:

## Inertia

if $b(q, p)$ is in $B$ then $b(q, (p \& r))$ also holds relative to $B$ , for all propositions $r$ ,

where this principle has priority over the libertine assumption. The idea is that a principle $b(s, p)$ has ‘inertia’ (relative to a code B of which it is a member) in the sense that in any situation in which p is beyond reasonable doubt, s will be favored for B. Of course, there also are exceptions to the principle of inertia since $b(s, p)$ is defeasible and B may contain rules that conflict and override $b(s, p)$ . The assumption of 'inertia' is (like 'libertine') merely a default assumption, for there are circumstances in which it should not be applied - for instance, if $b(q, p)$ is in $B$ and $B$ also contains $b(\tilde{q}, (p \& r))$ then $b(q, (p \& r))$ should not be added. The principle of inertia is limited in its applicability because of the possibility of conflicting rules, and in what follows we consider precisely under what conditions inertia should be invoked.

Let there be a ‘potential conflict’ between two rules just in case their consequents are logical contraries. $^{27}$ (For certain applications it may be useful to define potential conflicts in terms of ‘physical’ contraries.) There is for instance a potential conflict between $b(\sim q, p)$ and $b((q \& r), s)$ . Let there be ‘convergence’ between two rules just in case the antecedent of one of the rules is entailed by the antecedent of the other rule. There is convergence then between $b(q, p)$ and $b(r/(p \& q))$ . Suppose that there is a potential conflict between two ‘b’ rules in a code B. There are two different types of cases to consider, depending on whether or not there is convergence between the potentially conflicting rules.

In case (a) there is a potential conflict between $b(q, p)$ and $b(s, r)$ , i.e., q and s are contraries, but no convergence, i.e., p does not entail r and r does not entail p. In this case it is plausible to suggest that the inertia of each of the beliefs is limited by the other – they are mutually defeating in the sense that p defeats $b(s, r)$ and r defeats $b(q, p)$ . $^{28}$

In case (b) there is a potential conflict between $b(q, p)$ and $b(s, r)$ but either (bi) entails $r$ and $r$ does not entail $p$ , or (bii) $r$ entails $p$ and $p$ does not entail $r$ . $^{29}$ In case (bi), the truth of $r$ should not defeat $b(q, p)$ because any weak ordering that satisfies $b(q, p)$ also will satisfy $b(q, p \& r)$ and also $b(q, (p \& r \& ^{\sim}(q = s)) -$ which means that $b(q, p)$ has greater relative weight than $b(s, r)$ and hence should prevail when the two rules conflict. Similarly in case (bii) p should not defeat $b(s, r)$ , since $b(s, r)$ then has greater relative weight than $b(q, p)$ and $b(q, p)$ should be defeated by r.

If there is a potential conflict between a 'b' rule $b(q, p)$ and a 'c' rule $c(s, r)$ , then again there are two cases: there is either (c) no convergence or (d) convergence where either (di) p entails r or (dii) r entails p.

In case (c) it seems reasonable to restrict the inertia of $b(q, p)$ by regarding the acceptability of r as a defeating condition for $b(q, p)$ . But $c(s, r)$ should not be restricted: given the libertine assumption, the explicit presence of $c(s, r)$ gives it a priority over rules with which there is potential conflict but no convergence (for otherwise there would be no point in explicitly including it at all).

In case (dii) clearly $b(q, p)$ should be restricted, due to considerations of relative weight like those referred to above in regards case (bi). In case (di) $c(s, r)$ , but not $b(q, p)$ , should be restricted.

Thus far we have discussed the libertine principle and the principle of inertia modified by the considerations on potential conflicts. Whether or not these principles can be shown to determine a unique ranking for B remains an open question, but it is clear that the principles can be used to show that some rankings that satisfy all of the beliefs of B nevertheless are less successful than other rankings in reflecting the content of B. $^{30}$

The libertine principle and the modified inertia principles are implemented in 3dpr by means of the 'process' procedure which compares each belief $b(q, p)$ in the swept code with each other belief to see whether there is a potential conflict. Suppose that 'process' is examining $b(q, p)$ relative to $b(s, r)$ or $c(s, r)$ . If there is no potential conflict, nothing is added to the knowledge base. If there is a potential conflict, then in cases (a), (bii), (c), and (dii) the following clause is added to the database

defeated(b(q, p)): -r.

In cases (b) and (di) nothing is added.

30 Recall for instance the 'libertine' ranking determined on the basis of the libertine principle alone: given two independent rules $b(q, p)$ and $b(s, r)$ , the libertine ranking, in which each history is ranked highly as in any ranking that satisfies the code, will be less acceptable than others (as was pointed out in showing the need for the principle of inertia).

## 13. Reasoning

The ‘defeated’ clauses play an essential role in the defeasible reasoning to favored conclusions ‘ $l(q)$ ’ as for instance in the following rule that implements the ‘Key’ detachment schema:

$$
\begin{array}{c} 1 (Y): - b (Y, X), \\ X, \\ \text { not   defeated } (b (Y, X)). \end{array}
$$

In the Wilson et al. example where the original belief code is $\{b(w), b(t, \tilde{w}), b(h, (\tilde{w}, \tilde{t}))\}$ sweeping will supplement the code with $b(w, \text{true})$ , together with other rules entailed by the code, and the ‘defeated’ clauses introduced in processing will include

$$
\text { defeated } (b (w, \text { true })): - \tilde {w}.
$$

$$
\operatorname{defeated} \bigl (b (t, \tilde {w}) \bigr): - \tilde {t}.
$$

Relative to the empty set of reasonable propositions we can detach the presumption expressed by $l(w)$ using this instantiation of the ‘key’ rule:

$$
\begin{array}{l} l (w): - b (w, \text { true }), \\ \quad \text { true }, \\ \quad \text { not   defeated } (b (w, \text { true })). \end{array}
$$

However when it turns out that $\tilde{w}$ is beyond reasonable doubt (that is, $\tilde{w}$ is added as a PROLOG fact to the knowledge base) the third conjunct of the body of this rule, namely

not defeated $(b(w, \text{true}))$

no longer succeeds; and there is no way to derive $l(q)$ . We can however derive $l(t)$ by means of the following instantiation of the 'key' rule:

$$
\begin{array}{c} l (t): - b \big (t, \tilde {\sim} w \big), \\ \tilde {\sim} w, \\ \text { not   defeated } \big (b \big (t, \tilde {\sim} w \big) \big). \end{array}
$$

Of course when $\tilde{t}$ also is asserted, this derivation fails because 'defeated $(b(t, \tilde{w}))'$ succeeds. But we can derive $l(h)$ by means of

$$
\begin{array}{l} l (h): - b \big (h, (\tilde {\sim} w, \tilde {\sim} t) \big), \\ \qquad (\tilde {\sim} w, \tilde {\sim} t), \\ \qquad \text { not   defeated } \big (b (h, (\tilde {\sim} w, \tilde {\sim} t)) \big). \end{array}
$$

## 14. Summary

A theory of reasoning with defeasible rules in belief systems needs to be able to represent the distinction between (i) the propositions reasonably believed by the system and (ii) those propositions that are not beyond reasonable doubt but nevertheless are more reasonable, given the defeasible rules, than their negations. We have presented a language to express these different components of belief systems, and we have provided a possible worlds semantics that characterizes these notions formally. The semantics for defeasible rules is based on Lewis' semantics for conditional logic (without the condition that the actual world always is among the 'innermost' worlds in the system of spheres). The 'favored closure' (F-closure) of a set of defeasible default rules and reasonable propositions is non-monotonic. Yet, as we showed, it is possible to state precisely the conditions under which an inference to a favored conclusion, on the basis of defeasible rules and reasonable propositions, is warranted. We pointed out some rather strong consequences of the theory of defeasible rules and implicitly challenged the reader to construct counterexamples. We showed that there are significant differences between our defeasible rules and expressions of probability. Finally we discussed the main features of a computational prototype of the theory of defeasible reasoning. $^{31}$

## Appendix

This appendix contains a formalization of the semantics of section 7. Let the language of 3Db be a propositional language containing T and F, two dyadic modal operators $\rightarrow$ and $L(-/-)$ , and a monadic modal operator S. For tautology T, let $Lq =_{\mathrm{df}} L(q/T)$ and $Bq =_{\mathrm{df}} T \rightarrow q$ .

A 3Db model structure is a 6-tuple $\langle W, T, H, K, S, G \rangle$ where $W$ is a set of momentary world stages, T is the set of natural numbers (the set of times), H is a subset of the set of functions from T into W (these functions are possible histories), K is a set of belief systems, S is a function from $T \times H \times K$ into the set of weak orderings on H, and G is function from $T \times H \times K$ into H. For a temporal belief state $k = \langle t, h, i \rangle$ for $t \in T$ , $h \in H$ , and $i \in K$ , $S_k$ is the default field of normality for k and $G_k$ is the range of accessibility for k.

Given an ordering x on H and a subset y of H let the restriction of x to y be the ordering z that results by removing from x (i.e., ‘pruning x by removing’) each element of H not in y. $S_{k}^{*}$ is defined to be the restriction of $S_{k}$ to $G_{k}$ and is called the favored field for k.

An interpretation [] on a 3Db model structure is defined as follows: [] assigns to each propositional variable a subset of $T \times H \times K$ where we stipulate that for non-modal propositions the time and system indices are irrelevant (i.e., non-modal propositions are evaluated relative to histories alone). Recursion clauses for the truth-functional connectives are as usual. Now let $[q/p]$ be the class of weak orderings $\leq$ on $H$ such that

$$
E j \left(j \in [ p \& q ] \& (k) \left(k \in [ p \& ^ {\sim} q ] \supset^ {\sim} (k \leq j)\right)\right).
$$

That is, $[q/p]$ is the class of weak orderings on $H$ in which some $p\& q$ history is ranked more highly than any $p\& \tilde{q}$ history. For $k = \langle t, h, i \rangle$ and for $j, k \in H$ :

$$
\begin{array}{l} k \in [ p \to q ] \quad \text { iff } S _ {k} \in [ q / p ]. \\ k \in [ L (q / p) ] \quad \text { iff } S _ {k} ^ {*} \in [ q / p ]. \\ k \in [ S q ] \quad \text { iff } G _ {k} \in [ q ]. \end{array}
$$

For $V(q, p)$ first let us say that for $x \subseteq H$ , $g(k, x)$ is the set of most highly ranked histories in the set $x$ according to $S_k$ . Also for $x, y \subseteq H$ , let

$$
x = _ {p} Y
$$

say

$$
x \subset [ p ] \quad \text { iff } y \subset [ p ]
$$

and $x \cap [p] \neq \wedge$ iff $y \cap [p] \neq \wedge$ .

The recursion clause for $V(q, p)$ is

$$
\begin{array}{r l} & k \in [ V (q, p) ] \\ & \quad \text { iff } (x) (x \subseteq H \& G _ {k} \subseteq \times g (k, [ p ] \cap x) \\ & \quad = _ {q} g (k, [ p ]). \end{array}
$$

## References

[1] Belzer, M., Normative Kinematics (I): A Solution to a Problem about Permission, Law and Philosophy 4 (1985a) 257–287.

[2] Belzer, M., Normative Kinematics (II): The Introduction of Imperatives, Law and Philosophy 4 (1985b) 377–403.

[3] Belzer, M., Reasoning with Defeasible Principles, Synthese 66 (1986a) 135–158.

[4] Belzer, M., A Logic of Deliberation, Proc. Fifth National Conference on Artificial Intelligence 1 (1986b) 38–43.

[5] Belzer, M., Legal Reasoning in 3-D, Proc. First International Conference on Artificial Intelligence and Law (ACM Press, 1987) 155–163.

[6] Chellas, B., Modal Logic (Cambridge University Press, Cambridge, 1984).

[7] Chisholm, R., Theory of Knowledge (Prentice-Hall, Englewood Cliffs, NJ, 1977).

[8] Doyle, J., Some Theories of Reasoned Assumptions, Department of Computer Science, Carnegie-Mellon University, Pittsburgh (1983).

[9] Levesque, H.J., A Logic of Implicit and Explicit Belief,

Proc. National Conference on Artificial Intelligence (1984) 198–202.

[10] Lewis, D., Counterfactuals (Basil Blackwell, Oxford, 1973).

[11] Lewis, D., A problem about Permission, in: E. Saarinen, R. Hilpinen, I. Niiniluoto, and M.B. Provence Hintikka, eds., Essays in Honour of Jaakko Hintikka (Reidel, Dordrecht, 1979).

[12] Loewer, B. and M. Belzer, Dyadic Deontic Detachment, Synthese 54 (1983) 295–319.

[13] Loewer, B. and M. Belzer, Help for the Good Samaritan Paradox, Philosophical Studies 50 (1986) 117–127.

[14] Loewer, B. and M. Belzer, Default Rules, Acceptance, and Expectation in Belief Systems, Proc. Twentieth Annual Hawaii International Conference or System Sciences 3 (1978) 445–454.

[15] Loewer, B. and M. Belzer, Prima Facie Obligation: Its Deconstruction and Reconstruction, forthcoming in a Festschrift in honor of John Searle (1987b).

[16] Nute, D., Defeasible Reasoning, Proc. Twentieth Annual Hawaii International Conference on System Sciences 3 (1987) 470–477.

[17] Stalnaker, R., Inquiry (MIT Press, Cambridge, 1984).
