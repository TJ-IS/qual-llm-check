---
otero_id: 11124
otero_key: "43HKQVDG"
title: "A logical framework for identifying quality knowledge from different data sources"
authors: "Kaile Su; Huijing Huang; Xindong Wu; Shichao Zhang"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.02.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 1673– 1683

www.elsevier.com/locate/dss

# A logical framework for identifying quality knowledge from different data sources ☆

Kaile Su <sup>a</sup>, Huijing Huang <sup>b</sup>, Xindong Wu <sup>c</sup>, Shichao Zhang <sup>d,e,⁎</sup>

<sup>a</sup> Faculty of Computer Science, Zhongshan University, China

<sup>b</sup> Bureau of Personnel and Education, Chinese Academy of Sciences, China

<sup>c</sup> Department of Computer Science, University of Vermont, Burlington, Vermont 05405, USA d Guangxi Normal University, Guilin, China

<sup>e</sup> Faculty of Information Technology, University of Technology Sydney, PO Box 123, Broadway NSW 2007, Australia

Received 9 February 2005; received in revised form 16 February 2006; accepted 20 February 2006 Available online 19 April 2006

## Abstract

As the Web has emerged as a large distributed data repository, individuals and organizations have been able to utilize the lowcost information and knowledge on the Internet when making business decisions. Because data in different data sources may be conflictive or untrue, researchers and practitioners must intensify efforts to develop appropriate techniques for its efficient use and management. In this paper, a logical framework is designed for identifying quality knowledge from different data sources, thus working towards the development of an agreed ontology. Our experimental results have demonstrated that the approach is promising, and that a minor data enhancement adjustment could bring higher effectiveness. © 2006 Elsevier B.V. All rights reserved.

Keywords: Knowledge; Data source; Logic

## 1. Introduction

The vast amount of information available on the Web provides great potential for people to improve the quality of decision-making by enhancing results mined from databases [9]. If a company has an internal dataset D to be mined, high-profit pressures generate an urgent need for the collection of extra information from external data sources, referred to here as $D _ { 1 } , D _ { 2 } , . . . , D _ { n } ,$ , when mining D. As such, knowledge discovery from different data sources (K3D) has been recognized recently as an important research topic in the data mining community. Here, the knowledge from D is referred to as ‘internal knowledge’, whereas the knowledge from $D _ { 1 } , D _ { 2 } , . . . , D _ { n }$ is ‘external knowledge’.

There are essential differences between mono- and multi-database mining. Both data and patterns in multidatabases present more challenges than those in monodatabases. For example, unlike in mono-databases, data items in multi-databases may have different names, formats and structures. They may also conflict with one another, or be untrue [23]. Therefore, an agreed ontology must be developed for mining quality knowledge from multiple data sources, where quality knowledge is reliable and not contradictory.

Liu et al. have proposed a means of searching for interesting knowledge in multiple databases according to a user query [11]. Zhong et al. have proposed a method of mining peculiarity rules from multiple databases [26]. Aronis et al. have introduced a system called WoRLD that uses spreading activation to enable inductive learning from multiple tables in multiple databases spread across the network [1]. These research efforts provide a good insight into knowledge discovery from multiple data sources.

The authors of this paper have also contributed research towards mining multiple data sources. For example, Wu and Zhang [20] advocated an approach for identifying patterns in multiple databases by weighting; Zhang et al. [23] designed a local pattern analysis for mining multiple databases; Wu et al. [22] proposed a database classification for mining multiple databases; and Zhang et al. [24] systematically studied various strategies for mining multiple databases.

However, all of the above techniques are based only on quality data. That is, researchers have assumed that the input to mining algorithms conforms to well-defined data distribution, containing no missing, inconsistent, or incorrect values [25]. This leaves a large gap between the use of available data and the machinery available to process that data. Because real-world data might be incomplete, noisy, or inconsistent, thus disguising useful patterns, researchers and practitioners must intensify efforts to develop appropriate techniques for efficiently using and managing data. Although data enhancement, which straddles data preprocessing and K3D, often presents itself as less glamorous, it is, in fact, a more critical step than other steps in K3D applications; as minor data enhancement adjustments have the potential to bring about higher effectiveness. Therefore, we see data enhancement as a crucial research topic in K3D applications.

In this paper, breaking fresh ground from traditional data mining strategies, we take a data source as a knowledge base and design a logic framework for identifying trustworthy knowledge from various data sources, thus working toward the development of an agreed ontology.

The rest of this paper is organized as follows. Some basic concepts are recalled in Section 2. In Section 3 we present a logic and its semantics for K3D. Section 4 constructs the proof theory. Section 5 discusses how the proposed methodology can be used to enhance nonmonotonic reasoning. Section 6 illustrates the use of our framework. Our research contributions are summarized in the last section.

## 2. Needed concepts

The aim of our research in this paper can be formulated as follows:

Given a mining task for a company that has data source $\mathrm { D S } _ { 1 } ,$ and assuming DS<sub>2</sub>, $\mathrm { D S } _ { 3 } , . . . , \mathrm { D S } _ { n }$ are $n - 1$ external data sources that have been collected for the mining task, we will construct a logic framework for identifying trustworthy knowledge from external data sources.

Because privacy is a very sensitive issue, and safeguarding its protection in a data source is of extreme importance, sharing knowledge (rather than simply using the original raw data) presents a feasible way to deal with different data source problems [20]. Accordingly, we assume here that a data source is taken as a knowledge base<sup>1</sup>; a company is viewed as a data source; and a rule has two values in a data source: true (the data source supports the rule) and false (otherwise).

The collected knowledge from external data sources may be subject to noise. Thus, if a data source wants to create its own knowledge for data mining applications, the data source needs the ability to refine the knowledge it has collected. That is, the data source has to determine which set of knowledge to believe according to its own knowledge. To do this, we advocate a logic framework that pursues the following principle, based on work in [16], as follows.

If a data source i believes that another data source j is veridical, in terms of a standard multi-modal language, $K _ { i } ( K _ { j } \alpha \Rightarrow \alpha )$ for all formulas $\alpha ,$ then data source i inherits and accepts the knowledge in data source j. Otherwise, the knowledge in data-resource j must be preprocessed before it is applied.

In the above stipulation, the knowledge in data source i is referred to as ‘internal knowledge’ and the knowledge in data source j is referred to as ‘external knowledge’.

For example, let $D _ { 1 }$ be a data source with a rule set $\{ a _ { 1 }  b _ { 1 } \} , D _ { 2 }$ be an external data source with a rule set $\{ a _ { 2 }  b _ { 2 } , a _ { 3 }  b _ { 3 } \}$ , and data source $D _ { 1 }$ believes that the external data source $D _ { 2 }$ is veridical. Then the data source $D _ { 1 }$ inherits and accepts the knowledge in $D _ { 2 }$ This means that $D _ { 1 }$ has a rule set $\{ a _ { 1 }  b _ { 1 } , \ a _ { 2 }  b _ { 2 } ,$ $a _ { 3 }  b _ { 3 } \}$ after collecting knowledge from $D _ { 2 }$

Our logic framework focuses on the following epistemic properties:

• Veridicality. Knowledge is true.

• Introspection. A data source is aware of what it supports and of what it does not support.

• Consistency. A data source's knowledge is noncontradictory.

The well-known modal logics S5, K, T, K45 and KD45 have already been constructed by Turner [18] and Wooldridge [19] using different combinations among the above properties. In this paper we will build a new model logic for K3D, in which the veridicality and introspection of knowledge are taken into account. We allow the explicit mention of introspection and veridicality of a data-resource according to its own knowledge so that the formulas in our language indicate which one of K, T, S5, or K45 can be used by a dataresource.

The language of those logics is a propositional logic augmented by the modal operators $K _ { 1 } , K _ { 2 } , . . . , K _ { n } ,$ where $K _ { i } \phi$ reads “data source i supports $\phi ^ { , , }$ .

We denote this language by $L _ { n } .$ For convenience, we define true as an abbreviation for a fixed valid propositional formula, say $p \lor \lnot p .$ , where $p$ is a primitive proposition. We abbreviate ¬true by false.

According to Halpren and Mosses [5], the semantics of logic formulas can be given by means of Kripke structures [7], which formalize the intuition behind possible worlds. A Kripke structure is a tuple $( W , \pi , K _ { 1 } ,$ $. . . , K _ { n } )$ , where $W$ is a set of worlds, π associates with each world a truth assignment to the primitive propositions so that $\pi ( w ) ( p ) \in \{ \mathrm { t r u e } .$ , false} for each world w, and primitive proposition $p ,$ and $K _ { 1 } , . . . , K _ { n }$ are binary accessibility relations. By convention, $K _ { i } ^ { M }$ and $\pi ^ { M }$ are used to refer to the $K _ { i }$ relation and the π function in the Kripke structure $M ,$ respectively. We omit the superscript M if it is obvious from the context. Finally, we define

$$
K _ {i} (w) = \{w ^ {\prime} | \forall \phi \in w ^ {\prime} (K _ {i} \phi) \}
$$

That is, $K _ { i } ( w )$ is the set of worlds that data source i considers possible in each w.

A situation is a pair (M, w) consisting of a Kripke structure M and a world w in M. By using situations, we can inductively give semantics to formulas as follows. For primitive propositions $p ,$

$$
(M, w) \models p \text {   iff   } \pi^ {M} (w) (p) = \text { true }
$$

Conjunctions and negations are dealt with in the standard way. Finally,

$$
(M, w) \models K _ {i} \alpha \text {   iff   for   all   } w ^ {\prime} \in K _ {i} ^ {M} (w), (M, w ^ {\prime}) \models \alpha
$$

Thus, a data source i supports α if α is true in all situations that the data source considers possible.

Note that the Kripke structure M is fixed in the above inductive interpretation. However, as we will see in the next section, our interpretation differs from the above case.

## 3. Formal semantics

The language we define in this section is $L _ { n } ,$ augmented by two classes of special proposition constants: $I _ { i }$ and $V _ { i }$ $( 1 \leq i \leq n )$ . These are denoted by $L _ { n } ( V I )$ , where $I _ { i }$ and $V _ { i }$ $( 1 \leq i \leq n )$ correspond to the epistemic properties, introspection and veridicality respectively. In formula $I _ { i }$ data source i has the ability to respect its knowledge, and formula $V _ { i }$ indicates that data source i supports true knowledge only.

The language $L _ { n } ( V I )$ is tailored to represent and tackle the relationship between internal and external knowledge faced by the data sources. When identifying trustworthy knowledge from external data sources, the most important merit of this logic is that it distinguishes the internal knowledge from the external knowledge of a data source.

We now present the interpretation of $L _ { n } ( V I )$ . By way of description, in this section we use standard Kripke structures and situations in a non-standard way. The key point is that the accessibility relation $K _ { i }$ in the Kripke structures is no longer related to data source i's knowledge. In each situation $( M , w )$ the syntactic counterpart is $( M , w ^ { \prime } )$ , where, $w ^ { \prime } \in K _ { i } ( w )$ is what the information that data source i has collected rather than its own knowledge. Nonetheless, the relation $K _ { i } ,$ together with the actual world w, uniquely determines data source $i \mathrm { { ^ { \circ } s } }$ knowledge in some implicit way.

Let $\models _ { N }$ be the satisfaction relation we are going to define. The most subtle case is that of dealing with formulas of the form $K _ { i } \alpha$ . One might tend to let

$$
(M, w) \models_ {N} K _ {i} \alpha
$$

iff for all

$$
w ^ {\prime} \in K _ {i} (w), (M, w ^ {\prime}) \models_ {N} \alpha
$$

This would be completely true if the $( M , w ^ { \prime } ) \mathbf { \dot { s } }$ $( w ^ { \prime } \in K _ { i } ( w ) )$ were exactly those situations that are thought possible from the standpoint of data source $i \mathbf { \ ' } _ { \mathbf { S } }$ knowledge. Unfortunately, these $( M , w ^ { \prime } ) \mathrm { s }$ are thought possible only from the standpoint of what the information that data source i has collected. Indeed, if we did it in this way, we would get nothing but the well-known modal logic $K _ { n } .$ . Thus, it is crucial to ask in what situations should data source i think it possible from the standpoint of what it actually supports, after checking and cogitating on the external knowledge. Let $S _ { i } ( M , w )$ be the set of all such possible situations for the given situation $( M , w )$ , then we interpret formulas of the form $K _ { i } \alpha$ as,

$$
(M, w) \models_ {N} K _ {i} \alpha
$$

iff

$$
\forall (M ^ {\prime}, w ^ {\prime}) \in S _ {i} (M, w), (M ^ {\prime}, w ^ {\prime}) \models_ {N} \alpha
$$

We can now figure out what $S _ { i } ( M , w )$ should be. There are four cases according to the logic style of data source i in the situation $( M , w )$ . Firstly, if the logic style is K, i.e. the value of $\pi ( \boldsymbol { w } )$ is false at both $I _ { i }$ and $V _ { i } ,$ then data source i is unable to distinguish its knowledge from what has been collected, and hence the situations in $S _ { i } ( M , w )$ are exactly the same as $( M , w ^ { \prime } ) \dag \mathrm { s } .$ , where $w ^ { \prime } \in K _ { i } ( w )$

Secondly, assume the logic style is T. That is,

$$
\pi (w) \left(I _ {i}\right) = \text { false   and } \pi (w) \left(V _ {i}\right) = \text { true }
$$

Then, we get $S _ { i } ( M , w )$ by adding the actual world w to each $( M , w ^ { \prime } )$ , where $w ^ { \prime } \in K _ { i } ( w )$ . This enables data source i to delete the false part from the collected knowledge.

Thirdly, suppose the logic style is K45. That is:

$$
\pi (w) \left(I _ {i}\right) = \text { true   and } \pi (w) \left(V _ {i}\right) = \text { false }
$$

Assuming, from its internal knowledge, that data source i thinks the situations $( M ^ { \prime } , w ^ { \prime } )$ are possible, we have, by the introspection of data source $i ,$ that data source $i \mathbf { \ ' } _ { \mathbf { S } }$ external knowledge in each of those situations $( M ^ { \prime } , w ^ { \prime } )$ is exactly the same as that in the actual situation $( M , w )$ . This is semantically represented as

$$
K _ {i} ^ {M ^ {\prime}} (w ^ {\prime}) = K _ {i} ^ {M} (w)
$$

On the other hand, the knowledge of the introspection property $I _ { i }$ is such that if it holds, then data source i must support it, no matter what information data source i has collected. Thus, in each of those situations $( M ^ { \prime } , w ^ { \prime } )$ $I _ { i }$ must hold. Hence,

$$
\pi^ {\mathrm{M} ^ {\prime}} (w ^ {\prime}) (I _ {i}) = \text { true }
$$

Based on the above discussions, we define $S _ { i } ( M , w )$ as a set of those situations $( M ^ { \prime } , w ^ { \prime } )$ , where $w ^ { \prime } { \in } K _ { i } ^ { M } ( w )$ and $M ^ { \prime }$ coincides with M, and,

$$
K _ {i} ^ {M ^ {\prime}} (w ^ {\prime}) = K _ {i} ^ {M} (w) \text { and } \pi^ {M ^ {\prime}} (w ^ {\prime}) (I _ {i}) = \text { true }
$$

For convenience, we denote the above M′ Kripke structures by

$$
M \left[ \frac {K _ {i} (w ^ {\prime})}{K _ {i} (w)}; \frac {\pi (w ^ {\prime}) (I _ {i})}{\text { true }} \right]
$$

Finally, let the logic style be S5. Then, by considering the veridicality, we should put the actual world w into the set $K _ { i } ^ { M } ( w )$ , and conclude that $K _ { i } ^ { M } ( w ) \cup \{ w \}$ } was the set of worlds possible from the standpoint of data source $i \mathbf { \ ' } _ { \mathbf { S } }$ external knowledge. By considering the introspection, we define $S _ { i } ( M , w )$ in the same way as in the case of K45. Now, $K _ { i } ^ { M } \left( \boldsymbol { w } \right)$ , the set of worlds possible from the standpoint of data source $i \mathrm { \ ' } _ { \mathrm { S } }$ external knowledge, is replaced by $K _ { i } ^ { M } \left( w \right) \cup \left\{ w \right\}$ . In other words, we define $S _ { i } ( M , w )$ as the set of those situations $( M ^ { \prime } , w ^ { \prime } )$ , where $w ^ { \prime } { \in } K _ { i } ^ { M }$ $( w ) \cup \{ w \}$ , and $M ^ { \prime }$ coincide with M, and

$$
K _ {i} ^ {M ^ {\prime}} (w ^ {\prime}) = K _ {i} ^ {M} (w) \cup \{w \} \text {   and   } \pi^ {M ^ {\prime}} (w ^ {\prime}) (I _ {i}) = \text { true }
$$

For convenience, we denote the M′ Kripke structures by

$$
M \left[ \frac {K _ {i} (w ^ {\prime})}{K _ {i} (w) \cup \{w \}}; \frac {\pi (w ^ {\prime}) (I _ {i})}{\text { true }} \right]
$$

As we have seen, $S _ { i } ( M , w )$ is equal to

(1) $\{ ( M , w ^ { \prime } ) | w ^ { \prime } { \in } K _ { i } ^ { M } ( w ) \}$

$$
\text { if   } \pi (w) (I _ {i}) = \text { false   and   } \pi (w) (V _ {i}) = \text { false };
$$

(2) $\{ ( M , w ^ { \prime } ) | w ^ { \prime } { \in } K _ { i } ^ { M } ( w ) \} \cup \{ ( M , w ) \}$ ,

$$
\text { if   } \pi (w) (I _ {i}) = \text { false   and   } \pi (w) (V _ {i}) = \text { true; }
$$

$$
(3) \left\{\left(M \left[ \frac {K _ {i} (w ^ {\prime})}{K _ {i} (w)}; \frac {\pi (w ^ {\prime}) (I _ {i})}{\text { true }} \right], w ^ {\prime}\right) \mid w ^ {\prime} \in K _ {i} ^ {M} (w) \right\},
$$

$$
\text { if } \pi (w) (I _ {i}) = \text { true   and } \pi (w) (V _ {i}) = \text { false };
$$

$$
\begin{array}{l} (4) \left\{\left(M \left[ \frac {K _ {i} w ^ {\prime}}{K _ {i} w \cup \{w \}}; \frac {\pi (w ^ {\prime}) (I _ {i})}{\text { true }} \right], w ^ {\prime}\right) \mid w \in K _ {i} ^ {M} (w) \cup \{w \} \right\}, \\ \text { if } \pi (w) (I _ {i}) = \text { true   and } \pi (w) (V _ {i}) = \text { true } \end{array}
$$

From the above, we can get the following properties of $S _ { i } .$ .

Proposition 1. For all situations $( M , w )$

(1) $i f \pi ^ { M } ( w ) ( V _ { i } ) { = } t r u e a n d \pi ^ { M } ( w ) ( I _ { i } ) { = } f a l s e ,$

then $( \mathrm { M } , w ) { \in } S _ { i } ( { \cal M } , w ) ;$

$$
i f \pi^ {M} (w) \left(V _ {i}\right) = t r u e a n d \pi^ {M} (w) \left(I _ {i}\right) = t r u e,
$$

then $\left( M \left[ \frac { K _ { i } ( w ) } { K _ { i } ( w ) \cup \{ w \} } \right] , w \right) { \in } S _ { i } ( M , w ) ;$

(3) $i f \pi ^ { M } \dot { ( w ) } ( I _ { i } ) = t r u e ,$

$$
\text { then,   for   all   situations } (M ^ {\prime}, w ^ {\prime}) \text { in } S _ {i} (M, w),
$$

$$
\pi^ {M ^ {\prime}} (w ^ {\prime}) (I _ {i}) = \text { true   and } S _ {i} (M ^ {\prime}, w ^ {\prime}) = S _ {i} (M, w)
$$

The properties can be proven by the above definitions and deliberations.

We now formally present our semantic framework by defining inductively the satisfaction relation $\models _ { N }$ between a situation and a formula as follows.

(1) $( M , w ) \vdash _ { N } p \mathrm { i f f } \pi ( w ) ( p ) = \mathrm { t r u e } ,$ , for a primitive proposition $p .$

(2) $( M , w ) \vdash _ { N } \lnot \alpha$ iff not $( M , w ) \mathop { = } _ { N } \alpha _ { : }$ , and $( M , w ) \vdash _ { N }$

α ∧ β iff $( M , w ) \mathop { = } _ { N } \alpha$ and $( M , w ) \mathop { \vartriangle } { = } \ l _ { N } \beta .$

(3) $( M , w ) \mathsf { l } = _ { N } K _ { i } \alpha$ iff $( M ^ { \prime } , w ^ { \prime } ) \vdash _ { N } \alpha$ for all $( M ^ { \prime } , w ^ { \prime } ) { \in } S _ { i }$ (M, w).

We remark that, according to this semantic framework, a veridical data source takes the knowledge that has been collected and adds the current world to the set of possibilities in order to obtain its own knowledge. However, it is difficult for data sources to construct such a knowledge-sharing environment. This is because a data source typically does not support what is current world and it is impossible for a data source to perform the operation of adding current world. Nevertheless, this does not imply that this semantic framework is counterintuitive and suspect. There might be no veridical data source in the real world, but there are data sources that do have veridicality properties from the viewpoints of other data sources. For example, if data source $j$ thinks that data source i is veridical, then, from data source $j ^ { \circ } \mathbf { s }$ viewpoint, data source i does not yet support the current world, but data source j supports (or believes) that the current world is one of data source $j ^ { \circ } \mathbf { s }$ possible worlds. Thus, if data source $j$ supposes that the current world is w and data source $i \mathbf { \ ' } _ { \mathbf { S } }$ set of possible worlds (corresponding to its external knowledge) is $W ,$ then data source $j$ thinks that data source $i \mathrm { \ ' } _ { \mathrm { S } }$ knowledge is determined by the set $W ,$ plus the supposed current world w.

The following propositions helps to prove the validity of axioms in the next section.

Proposition 2. For all formulas $\phi , i f$

$$
\pi^ {\mathrm{M}} (w) \left(V _ {i}\right) = \text { true   and } \pi^ {\mathrm{M}} (w) \left(I _ {i}\right) = \text { true }
$$

then, for each world $w ^ { \prime } ,$

$$
\left(M \left[ \frac {K _ {i} (w)}{K _ {i} (w) \cup \{w \}} \right], w ^ {\prime}\right) \models_ {N} \phi \text {   iff   } (M, w ^ {\prime}) \models_ {N} \phi
$$

Proof. The proof of this proposition is accomplished by somewhat tedious induction on the structure of $\phi$ . More precisely, assuming, for all sub-formulae of $\phi _ { ; }$ , that this claim holds for all $M , i ,$ w and $w ^ { \prime }$ , we will show that it holds also for $\phi .$ . Suppose

$$
\pi^ {\mathrm{M}} (w) \left(V _ {i}\right) = \text { true   and } \pi^ {\mathrm{M}} (w) \left(I _ {i}\right) = \text { true }
$$

If $\phi$ is a primitive proposition $p ,$ it is immediately derived from the fact that assignment function π is the same in both the Kripke structures $M$ and $\begin{array} { r } { M \left\lceil \frac { K _ { i } ( w ) } { K _ { i } ( w ) \cup \{ w \} } \right\rceil } \end{array}$ The cases where $\phi$ <sup>ð Þ[f g</sup>is a conjunction or a negation follow from the definition of $\models _ { N }$ above.

If $\phi$ is of the form $K _ { i } \psi ,$ , then, in the case of $\ { \mathrm { \Delta } } _ { W } = w ^ { \prime } { \mathrm { \Delta } } _ { \mathrm { \Omega } }$ , the claim holds, since it is easy to check that

$$
S _ {i} (M, w) = S _ {i} \left(M \left[ \frac {K _ {i} \left(w ^ {\prime}\right)}{K _ {i} (w) \cup \{w \}} \right], w\right)
$$

Thus, we can assume $w \ne w ^ { \prime }$ . There are four subcases as follows:

$$
(1) \pi^ {M} (w ^ {\prime}) (V _ {i}) = \text { false   and } \pi^ {M} (w ^ {\prime}) (I _ {i}) = \text { false },
$$

$$
(2) \pi^ {M} (w ^ {\prime}) (V _ {i}) = \text { true   and } \pi^ {M} (w ^ {\prime}) (I _ {i}) = \text { false },
$$

$$
(3) \pi^ {M} (w ^ {\prime}) (V _ {i}) = \text { false   and } \pi^ {M} (w ^ {\prime}) (I _ {i}) = \text { true },
$$

$$
(4) \pi^ {M} (w ^ {\prime}) (V _ {i}) = \text { true   and } \pi^ {M} (w ^ {\prime}) (I _ {i}) = \text { true. }
$$

Subcases 1 and 2 can be immediately obtained by the definition of $\models _ { N } ,$ and the inductive assumption. For subcase 3, we firstly note that, by $w \ne w ^ { \prime }$

$$
K _ {i} ^ {M} (w ^ {\prime}) = K _ {i} ^ {M \left[ \frac {K _ {i} (w)}{K _ {i} (w) \cup \{w \}} \right]} (w ^ {\prime})
$$

Accordingly, by the definition of $\models _ { N } ,$ it suffices to show, for each $w ^ { \prime \prime } { \in } K _ { i } ^ { M } ( w ^ { \prime } )$ ,that

$$
\left(M \left[ \frac {K _ {i} (w)}{K _ {i} (w) \cup \{w \}} \right] \left[ \frac {K _ {i} (w ^ {\prime \prime})}{K _ {i} (w ^ {\prime})}; \frac {\pi (\mathrm{w} ^ {\prime \prime}) (I _ {i})}{\text { true }} \right], w ^ {\prime \prime}\right) \models_ {N} \psi
$$

iff

$$
\left(M \left[ \frac {K _ {i} (w ^ {\prime \prime})}{K _ {i} (w ^ {\prime})}; \frac {\pi (w ^ {\prime \prime}) (I _ {i})}{\text { true }} \right], w ^ {\prime \prime}\right) \models_ {N} \psi
$$

Note that the assertion above holds if $w ^ { \prime \prime } { = } w ,$ , because

$$
M \left[ \frac {K _ {i} (w)}{K _ {i} (w) \cup \{w \}} \right] \left[ \frac {K _ {i} (w)}{K _ {i} (w ^ {\prime})}; \frac {\pi (w) (I _ {i})}{\text { true }} \right]
$$

T.

equal

$$
M \left[ \frac {K _ {i} (w)}{K _ {i} (w ^ {\prime})}; \frac {\pi (w) (I _ {i})}{\text { true }} \right]
$$

And if $w ^ { \prime \prime } \ne w ,$ then this assertion holds also by the inductive assumption. Subcase 4 can be proved in the same way.

Finally, suppose that $\phi$ is of the form $K _ { j } \psi$ for $j \neq i .$ . This case is also divided into four subcases depending on the values of π $^ M ( w )$ at $V _ { j }$ and $I _ { j } .$ We prove the claim only in the case where data source i's logic style is S5. That is:

$$
\pi^ {\mathrm{M}} (w ^ {\prime}) (V _ {i}) = \text { true   and } \pi^ {\mathrm{M}} (w ^ {\prime}) (I _ {i}) = \text { true }
$$

since other cases are simpler, or can be handled in the same way. In this subcase, by the definition of $\models _ { N } ,$ it suffices to show, for every $w ^ { \prime \prime } { \in } K _ { j } ( w ^ { \prime } ) \cup \{ w ^ { \prime } \}$ , that

$$
\left(M \left[ \frac {K _ {i} (w)}{K _ {i} (w) \cup \{w \}} \right] \left[ \frac {K _ {i} (w ^ {\prime \prime})}{K _ {i} (w ^ {\prime}) \cup w ^ {\prime}}; \frac {\pi (w ^ {\prime \prime}) (I _ {i})}{\text { true }} \right], w ^ {\prime \prime}\right) \models_ {N} \psi
$$

iff

$$
\left(M \left[ \frac {K _ {i} (w ^ {\prime \prime})}{K _ {i} (w ^ {\prime}) \cup \{w ^ {\prime} \}}; \frac {\pi (w ^ {\prime \prime}) (I _ {i})}{\text { true }} \right], w ^ {\prime \prime}\right) \models_ {N} \psi
$$

But this can be obtained in a straightforward way by the inductive assumption. Because even if $w ^ { \prime \prime } { = } w ,$ in the Kripke structure

$$
M \left[ \frac {K _ {i} (w ^ {\prime \prime})}{K _ {i} (w ^ {\prime}) \cup \{w ^ {\prime} \}}; \frac {\pi (w ^ {\prime \prime}) (I _ {i})}{\text { true }} \right]
$$

the data source i's logic style in world w remains S5. That is,

$$
\pi^ {\mathrm{M}} (w ^ {\prime}) (V _ {i}) = \text { true   and } \pi^ {\mathrm{M}} (w ^ {\prime}) (I _ {i}) = \text { true }
$$

Hence, the inductive assumption can be applied.

The following proposition reflects some of the formal properties of $\models _ { N }$

Proposition 3. For all formulas α, $\beta \in L _ { n } ( V I )$ , and situations (M, w):

$$
\begin{array}{l} (1) (M, w) \vDash_ {N} (K _ {i} \alpha \wedge K _ {i} (\alpha \Rightarrow \beta)) \Rightarrow K _ {i} \beta ; \\ (2) (M, w) \vDash_ {N} V _ {i} \Rightarrow (K _ {i} \alpha \Rightarrow \alpha); \\ (3) (M, w) \vDash_ {N} I _ {i} \Rightarrow (K _ {i} I _ {i} \wedge (K _ {i} \alpha \Rightarrow K _ {i} K _ {i} \alpha) \\ \quad \wedge (\neg K _ {i} \alpha \Rightarrow K _ {i} \neg K _ {i} \alpha)). \end{array}
$$

Proof. To prove part (1), assuming $( M , w ) \mathop { = } _ { N } K _ { i } \alpha \wedge K _ { i }$ $( \alpha \Rightarrow \beta )$ , we must show $( M , w ) \mathop { \vartriangle } { = } \ l _ { N } \beta .$ But, by the assumption, we have, for each $( M ^ { \prime } , w ^ { \prime } ) { \in } S _ { i } ( M , w ) , ( M ^ { \prime } ,$ $w ^ { \prime } ) { \sf = } _ { N } \alpha$ and $( M ^ { \prime } , w ^ { \prime } ) \vdash _ { N } \alpha \Rightarrow \beta .$ It follows that $( M ^ { \prime } , w ^ { \prime } )$ $\models _ { N } \beta$ for all such $( M ^ { \prime } , w ^ { \prime } )$ , and therefore, $( M , w ) \mathop { \vartriangle } { = \ v { N } } \beta .$ Parts (2) and (3) can immediately be obtained from Proposition 1 (1) and Proposition 1 (2), respectively.

## 4. Proof theory

With respect to the semantic framework in the previous section, we present a sound and complete proof theory below. For any data source i:

P. All instances of axioms of propositional logic

$$
\text { K45. } \quad I _ {i} \Rightarrow (K _ {i} I _ {i} \land (K _ {i} \alpha \Rightarrow K _ {i} K _ {i} \alpha) \land (\lnot K _ {i} \alpha \Rightarrow K _ {i} \lnot K _ {i} \alpha))
$$

and the rules of inference are:

$$
\begin{array}{l l} \text { R1. } & \text { From   } \alpha \text {   and   } \alpha \Rightarrow \beta \text {   infer   } \beta \\ \text { R2. } & \text { From   } \alpha \text {   infer   } K _ {i} \alpha . \end{array}
$$

Axioms P and K, and the inference rules R1 and R2, consist of the well-known modal logic system $K _ { n } .$ Axioms T and K45 capture the aforementioned meanings of the constants: $I _ { i }$ and $V _ { i } ,$ respectively. For convenience, we denote this system by $\dot { K } _ { n } ^ { V I }$ . Two main results of our logic are the soundness and completeness of the proof system $K _ { n } ^ { V I }$ . The soundness is easy to check. Nevertheless, we need Proposition 2 to prove the validity of Axiom T, as shown in the proof of Proposition 3. Completeness is proved by the standard techniques originally due to Kaplan [6] that show close correspondence between the axioms and a particular Kripke structure known as the canonical structure.

Theorem 1. For the language $L _ { n } ( V I )$ , the system $K _ { n } ^ { V I }$ is a sound and complete axiomatization with respect to the semantics presented in the previous section.

Proof. Soundness: the validity of axiom P and rule R1 follows immediately from the fact that the interpretation of ∧ and ¬ in the definition of $\models _ { N }$ is the same in the propositional calculus. The validity of axioms $\mathrm { K , T , }$ and 45 are simply Proposition 3. For rule R2, if $( M , w ) \mathop { = } _ { N } \alpha$ for all situations (M, w), then, for any fixed situation $( M ^ { \prime } , w ^ { \prime } )$ , it follows that $( M , w ) \mathop { = } _ { N } \alpha$ for all situations $( M , w ) { \in } S _ { i } ( M ^ { \prime } , w ^ { \prime } )$ . Thus, $( M ^ { \prime } , w ^ { \prime } ) \vdash _ { N } K _ { i } \alpha$ for all situations $( M ^ { \prime } , w ^ { \prime } )$

Completeness: it suffices to prove that every consistent formula is satisfied by some situation. We construct a special Kripke structure $M ^ { \mathrm { c } }$ , known as canonical Kripke structure as follows. Given a set w of formulas, define $w / K _ { i } { = } \{ \phi \colon K _ { i } \phi { \in } V \}$ . Let $M ^ { \mathrm { c } } ( W , \pi , K _ { 1 } , . . . , K _ { n } )$ where

$W = \{ w : w$ is a maximal consistent set

$$
\pi (w) (p) = \left\{ \begin{array}{l} \text {true if p\in w} \\ \text {false if p\notin w} \end{array} \right.
$$

$$
K _ {i} = \{(w, w ^ {\prime}): w / K _ {i} \subseteq w ^ {\prime} \}.
$$

We first show that for each $w \in W , S _ { i } ( M ^ { \mathrm { c } } , w ) = \{ ( M ^ { \mathrm { c } }$ 9 $w ^ { \prime } ) \colon w ^ { \prime } \in { \mathbf { K } } _ { i } ( w ) \}$ , we have

$$
(M ^ {\mathrm{c}}, w) \models_ {N} K _ {i} \phi
$$

iff

$$
(M ^ {\mathrm{c}}, w ^ {\prime}) \models_ {N} \phi \text {   for   all   } w ^ {\prime} \in K _ {i} (w)\tag{\( \left( *\right) \}
$$

which is referred to a fact (⁎).

Firstly, if the logic style of data source i is $\mathrm { ~ K ~ } ( \mathrm { i . e . }$ $\pi ( w ) ( I _ { i } ) =$ false and $\pi ( w ) ( V _ { i } ) { = } \mathrm { f a l s e } )$ then, by the definition of $S _ { i } ,$ this claim is trivially true.

Secondly, if the logic style of data source i is T $( \mathrm { i . e . , ~ } \pi ( w ) ( I _ { i } ) =$ false and $\pi ( w ) ( V _ { i } ) { = } \mathrm { t r u e } )$ then, by the definition,

$$
S _ {i} (M ^ {\mathrm{c}}, w) = \left\{\left(M ^ {c}, w ^ {\prime}\right): w ^ {\prime} \in K _ {i} (w) \right\} \cup \left\{\left(M ^ {c}, w\right) \right\}
$$

But, by Axiom T and the maximality of w, we have $w / K _ { i } \subseteq w .$ It follows then that $w \in K _ { i } ( w )$ , and hence

$$
S _ {i} (M ^ {c}, w) = \left\{\left(M ^ {\mathrm{c}}, w ^ {\prime}\right): w ^ {\prime} \in K _ {i} (w) \right\}
$$

Thirdly, we suppose the logic style of data source i is K45, or

$$
\pi (w) \left(I _ {i}\right) = \text { true   and } \pi (w) \left(V _ {i}\right) = \text { false }
$$

By the definition, it suffices to show that

$$
\forall w ^ {\prime} \in K _ {i} (w), \left(M ^ {\mathrm{c}} \left[ \frac {K _ {i} (w ^ {\prime})}{K _ {i} (w)}; \frac {\pi (w ^ {\prime}) (I _ {i})}{\text { true }} \right], w ^ {\prime}\right) = (M ^ {\mathrm{c}}, w ^ {\prime})
$$

That is, $K _ { i } ( w ^ { \prime } ) { = } K _ { i } ( w )$ and $\pi ( w ^ { \prime } ) ( I _ { i } ) { = } \mathrm { t r u e }$ . By Axiom 45 and the fact that $\pi ( w ) ( I _ { i } ) { = } \mathrm { t r u e } \ ( \mathrm { i . e . } \ I _ { i } \in w )$ , we have $K _ { i } I _ { i } \in w .$ Hence $I _ { i } { \in } w ^ { \prime }$ and therefore, $\pi ( w ^ { \prime } ) ( I _ { i } ) { = } \mathrm { t r u e }$ . To show $K _ { i } ( w ^ { \prime } ) { = } K _ { i } ( w )$ , given an arbitrary $w ^ { \prime \prime } \in W ,$ we must prove that $\nu / K _ { i } \subseteq \nu ^ { \prime \prime }$ iff $w ^ { \prime } / K _ { i } \subseteq w ^ { \prime }$ . Assuming w/ $K _ { i } \subseteq { w ^ { \prime \prime } }$ and $\phi \in \boldsymbol { w } ^ { \prime } / K _ { i } ,$ we want to show $\phi \in \boldsymbol { w } ^ { \prime \prime }$ . If not, then $K _ { i } \phi \notin \boldsymbol { w } ,$ , and hence $\lnot K _ { i } \phi \in _ { \ l } w .$ . Thus, by Axiom 45, we would have $K _ { i } { \neg } K _ { i } \phi \in w ,$ , whence $\lnot K _ { i } \phi \in \ l w ^ { \prime }$ , contradicting the assumption that $\phi \in \boldsymbol { w } ^ { \prime } / K _ { i }$

On the other hand, assuming $w ^ { \prime } / K _ { i } \subseteq w ^ { \prime \prime }$ and $\phi \in w /$ $K _ { i } ,$ we have $K _ { i } \phi \in \boldsymbol { w } ,$ and hence by Axiom 45, $K _ { i } K _ { i } \phi \in _ { \textstyle w _ { \cdot } }$ Thus

$$
K _ {i} \phi \in w ^ {\prime} (\text { by } w / K _ {i} \subseteq w ^ {\prime})
$$

and

$$
\phi \in w ^ {\prime \prime} (w ^ {\prime} / K _ {i} \subseteq w ^ {\prime \prime})
$$

Finally, for the case where the logic style of data source i is ${ \mathrm { S } } 5 ( i . e . , \pi ( w ) ( I _ { i } )$ =true and $\pi ( w ) ( V _ { i } ) { = } \mathrm { t r u e } )$ by the same argument as above, it suffices to show that $w \in K _ { i } ( w ) , K _ { i }$ $( w ^ { \prime } ) { = } K _ { i } ( w )$ and $\pi ( w ^ { \prime } ) ( I _ { i } ) { = } \mathrm { t r u e }$ . But, as we have shown, the first follows from π(w)(V ) = true and Axiom ${ \mathrm { T } } ,$ and the last two from $\pi ( w ) ( I _ { i } ) { = } \mathrm { t r u e }$ and Axiom 45.

We now show, by induction on the structure of ${ \dot { } } \phi ,$ , that for every w we have

$$
(M ^ {\mathrm{c}}, w) \models_ {N} \phi \text {   iff   } \phi \in w\tag{**}
$$

More precisely, assuming that the claim holds for all sub-formulas of $\phi ,$ we will also show that it holds for $\phi .$ If ϕ is a primitive proposition $p ,$ this comes immediately from the definition of π(w) above. The case where $\phi$ is a conjunction of a negation follows easily from the definition of $\models _ { N }$ and some basic properties of a maximal consistent set of formulas.

Finally, suppose ϕ is of the form $K _ { i } \psi$ and $\psi \in w ,$ then $\psi \in w / K _ { i } .$ . Thus, by the definition of $K _ { i } ,$ for each $w ^ { \prime } \in K _ { i }$ (w), $\psi \in w ^ { \prime } ;$ , and hence, by the inductive hypothesis, $( M ^ { \mathrm { c } } , w ^ { \prime } ) { \models } _ { N } \psi$ . Thus, by fact ( ), it follows that $( M ^ { \mathrm { c } } , w ) \vdash$ ${ } _ { N } K _ { i } \psi$

For the other direction, assuming $( M ^ { \mathrm { c } } , w ) \vdash _ { N } K _ { i } \psi .$ , we must prove $K _ { i } \psi \in _ { w }$ . We first show that $w / K _ { i } \cup \{ \psi \}$ is inconsistent. If this is not the case, then it must have a maximal consistent extension $w ^ { \prime } ,$ and by construction we have $w ^ { \prime } \in K _ { i } ( w )$ . By the inductive hypothesis, we would have $( M ^ { \mathrm { c } } , w ^ { \prime } ) \vdash _ { N } \lnot \psi$ , and so $( M ^ { \mathrm { c } } , w ) \vdash _ { N } K _ { i } \psi$ by fact ( ), contradicting our previous assumption.

Since $w / K _ { i } \cup \{ \psi \}$ is inconsistent, some finite subset, say, $\{ \phi _ { 1 } , . . . , \phi _ { k } , \neg \psi \}$ , must also be inconsistent. Thus, by propositional reasoning, we have

$$
\vdash \phi_ {1} {\Rightarrow} (\phi_ {2} {\Rightarrow} (\cdot \cdot \cdot (\phi_ {k} {\Rightarrow} \psi) \cdot \cdot \cdot))
$$

And, by R2, we have

$$
K _ {i} \vdash \phi_ {1} \Rightarrow (\phi_ {2} \Rightarrow (\cdot \cdot \cdot (\phi_ {k} \Rightarrow \psi) \cdot \cdot \cdot))
$$

Therefore, by iterated applications of Axiom K and propositional reasoning, we get

$$
K _ {i} \phi_ {1}, K _ {i} \phi_ {2}, \dots K _ {i} \phi_ {k} \vdash K _ {i} \psi
$$

Since $\phi _ { 1 } , ~ . . . ~ \phi _ { k } { \in } w / K _ { i } ,$ we must have $K _ { i } \phi _ { 1 } , \ldots$ $K _ { i } \phi _ { k } { \in } w .$ . Since w is a maximally consistent set of formulas, it must be closed under ⊢. Therefore, $K _ { i } \psi \in _ { \cal { W } }$ □

## 5. Circumscription

Viewing each modal operator $T _ { i }$ (see Section 2) as a predicate, we may circumscribe $T _ { i }$ to a theory T in order to enhance the mechanism of nonmonotonic reasoning, in the same way as in the circumscription of [12]. The intuition behind this circumscription is that, if T holds, data source i can be collected as little as possible. In other words, what has been collected from data source i is, in some sense, derivable from T.

Similar to Reiter's default logic [14], which has been widely investigated in the AI community [15], we capture our intuition also by the default theory $( \mathrm { T } , D _ { i } )$ , where $D _ { i }$ consists of those free normal defaults $\frac { : \dot { \neg } T _ { i } \phi } { \neg T _ { i } \phi }$ for arbitrary formulas $\phi .$ . Interestingly, we can get the notion of circumscribing external knowledge about some subject straightforward by restricting formulas $\phi$ in defaults $\frac { \mathrel { \mathop : } \lnot T _ { i } \phi } { \lnot T _ { i } \phi }$ to those that concern the subject. This notion appears useful, because we are often interested only in what has collected from a data source about a specific subject, instead of all that has been collected from it.

The semantic counterpart of the above is as follows. Just as for the HM notion of only knowing [4], we need some appropriate notion of possibility. Here we adopt the ω-tree ([2,3,17]). Let $T _ { M , w }$ be the ω-tree corresponding to the situation $( M , w )$ , and $\mathrm { P o s s } _ { i } \left( M , w \right)$ the set $\{ T _ { M , w ^ { \prime } } | w ^ { \prime } \in K _ { i } ( w ) \}$ . We have the following:

Theorem 2. For each situation (M,w) and each theory $T o f L _ { n } ^ { T } ( W I )$ , there is an extension E of the default theory $( T , D _ { i } )$ such that $( M , w ) \mathop { \vartriangle } { = \ v { N } } E ,$ , iff (M, w) ⊨<sub>N</sub> T, and for all $( M ^ { \prime } , w ^ { \prime } ) , P o s s _ { i } ( M ,$ w) is not a proper subset of Poss (M′, $w ^ { \prime } )$ whenever $( M ^ { \prime } , w ^ { \prime } ) \vdash _ { N } T .$

We note that it is unreasonable for us to exactly the same for knowledge modalities $K _ { i } \mathbf { s }$ . In the presence of introspection, $, \neg K _ { i } \neg K _ { i } p$ is equivalent to $K _ { i } p$ . Thus the default $\frac { : \neg K _ { i } \neg K _ { i } p } { \neg K _ { i } \neg K _ { i } p }$ essentially says that data source i knows $p$ whenever possible, contradicting the intuition of the circumscribing knowledge of data source i. We thus should restrict our attention to only those formulas that are, in some sense, objective $f o r$ data source i, and the resulting notion of only knowing is essentially the only knowing about objective formulas. Nevertheless, in the presence of veridicality, it is rather subtle for standard modal logics to figure out such formulas, and some additional complicated operators, such as the $Q _ { i } ^ { \xi } , \mathrm { s }$ in [3], may be needed.

Interestingly, our methodology can reasonably lead to the notion of only knowing about some subject by limiting the formulas $\phi$ in the defaults $\textstyle { \frac { \neg K _ { i } \phi } { \neg K _ { i } \phi } }$ to those that concern the subject. This is beneficial, since we are usually more interested in what a data source knows about a particular subject. This approach to onlyknowing-about differs from that in [8], where two special kinds of subject are discussed for the logic KD45. The first kind of subjects, using default theories, can uniformly address arbitrary and interesting subjects, such as those regarding some data sources as knowledge about the actual world, provided that it is clear what formulas concern those subjects.

Our notion of only-knowing-about, however, is given as a special case of circumscribing external knowledge. Assuming $O _ { \ i } ^ { * } \alpha$ denotes what data source i knows is α, we define it semantically as follows. Given a situation (M, w), $( M , w ) { \sf t } _ { N } O _ { \imath } ^ { * } \alpha$ iff $( M , w ) \mathop { \vartriangle } { = \ v { N } } K _ { i } \alpha$ and for each $( M ^ { \prime } , w ^ { \prime } )$ , Poss (M, w) is not a proper subset of $\mathrm { P o s s } _ { i } ( M ^ { \prime } , w ^ { \prime } )$ whenever $( M ^ { \prime } , w ^ { \prime } ) \vdash _ { N } K _ { i } \alpha$ . Thus, by Theorem 2, $( M , w ) \mathop { \vartriangle } { = } _ { N } \mathrm { O } _ { t } ^ { * } \alpha$ iff $( M , w ) \mathop { = } _ { N } E$ , for some extension E of the default theory $( K _ { i } \alpha , D _ { i } )$

It is worth pointing out that O<sup>⁎</sup>α is satisfiable for any arbitrary $\alpha .$ Our notion thus differs from that in [10], which is closely related to that of a stable expansion in [13]. As shown by Example 5.4 of [10], it is impossible to know only the fact of knowing some falsifiable objective sentence, though possible to only know any objective sentence. Despite the reasons demonstrated in [10], this seems to contradict our intuition, that if knowing some thing is logically equivalent to knowing some other thing, then only knowing one of them should be equivalent to only knowing the other.

We say T is i-determinate if the default theory (T, $D _ { i } )$ has a unique extension, and a formula α is honest if $K _ { i } \alpha$ is determinate. In comparison with the HM notion of only knowing [4], we also characterize the notion of honest for special logics as follows.

To present the notion of ${ \mathrm { S } } 5 _ { n ^ { - } } i { - } h o n e s t ,$ we limit our attention to so-called S5-situations, where for all worlds $w ^ { \prime }$ and all data source $j \mathrm { s } ,$ $\pi ( w ^ { \prime } ) ( J j )$ = true and $\pi ( w ^ { \prime } ) ( V _ { j } ) { = } \mathrm { t r u e }$ . We say α is ${ \mathrm { S } } 5 _ { n ^ { - } } i { - } h o n e s t ,$ if there is an S5-situation (M, w), called S5-i-maximum situation for $\alpha ,$ , such that $( M , w ) \mathsf { l } = _ { N } K _ { i } \alpha$ , and for each S5-situation $( M ^ { \prime } , w ^ { \prime } )$ , we have $\mathrm { P o s s } _ { i } ( M ^ { \prime } , w ^ { \prime } ) \subseteq \mathrm { P o s s } _ { i } ( M , w )$ whenever $( M ^ { \prime } , w ^ { \prime } ) \vdash _ { N } K _ { i } \alpha$ . Similar notions can be obtained for logics $K _ { n } , T _ { n }$ and $\mathrm { K } 4 5 _ { n }$

The above notions are reasonable. In fact, we can prove that, for $\mathrm { K } _ { n } , \ \mathrm { T } _ { n } ,$ and $\mathrm { K } 4 5 _ { n } ,$ and also for ${ \mathrm { S } } 5 _ { n } ,$ they coincide with those in [3]. The essential point of our approach to only-knowing-about is that the circumscription of knowledge usually results from that of external knowledge. The less that is collected, the less is known. This only-knowing-about approach has many potential applications in non-monotonic reasoning environments, and can be used as a qualifier in answering systems.

## 6. Evaluation

As we have seen, the above framework provides a formal description for considering external knowledge under two epistemic properties: introspection and veridicality. It can be taken as a basis for K3D. This section evaluates the logic framework.

## 6.1. Examples

Our logic framework is taken as the first step in mining multiple data sources. The use of the logic framework is illustrated as follows:

Let $\mathrm { D S } _ { 1 } { = } \{ a _ { 1 } { \longrightarrow } b _ { 1 } \}$ be an internal data source, $\mathrm { D S } _ { 2 } = \{ a _ { 2 } \{  b _ { 2 } , a _ { 3 }  b _ { 3 } , a _ { 4 }  b _ { 4 } \}$ and $\mathrm { D S } _ { 3 } = \{ a _ { 2 }  b _ { 2 }$ 4 $a _ { 5 }  b _ { 4 } \}$ be two external data sources. Then $\mathrm { D S } _ { 1 }$ can form its own knowledge set, Ruleset1, by collecting quality knowledge from $\mathrm { D S } _ { 2 }$ and $\mathrm { D S } _ { 3 }$

(1) When $I _ { 1 } , \mathrm { D S } _ { 1 }$ has the ability to select true rules in $\mathrm { D S } _ { 2 } \cup \mathrm { D S } _ { 3 }$ and add them to Ruleset1. When not $\left( I _ { 1 } \right)$ , Ruleset1 is formed dependent on $K _ { 1 } ( I _ { 2 } ) , K _ { 1 }$ $( I _ { 3 } ) , K _ { 1 } ( V _ { 2 } )$ and $K _ { 1 } ( V _ { 3 } )$

(2) When not $( V _ { 1 } )$ , Ruleset $1 = \phi$ . When $V _ { 1 }$ , Ruleset1 is formed dependent on $K _ { 1 } ( I _ { 2 } ) , K _ { 1 } ( I _ { 3 } ) , K _ { 1 } ( V _ { 2 } )$ and $K _ { 1 } ( V _ { 3 } )$

(3) When $K _ { 1 } ( I _ { 2 } )$ , Ruleset $\mathbf { 1 } = \mathbf { D S } _ { 1 } \cup \mathbf { D S } _ { 2 }$ . When $K _ { 1 } ( I _ { 3 } ) _ { : }$ Ruleset $\mathsf { l } = \mathsf { D } \mathsf { S } _ { 1 } \cup \mathsf { D } \mathsf { S } _ { 3 }$ . When $K _ { 1 } ( I _ { 2 } )$ and $K _ { 1 } ( \mathrm { I } 3 )$ Ruleset $\mathbf { \tau } = \mathbf { D } \mathbf { S } _ { 1 } \cup \mathbf { D } \mathbf { S } _ { 2 } \cup \mathbf { D } \mathbf { S } _ { 3 }$

(4) When $K _ { 1 } ( V _ { 2 } )$ , true rules in $\mathrm { D S } _ { 2 }$ are added to Ruleset1. When $K _ { 1 } ( V _ { 3 } )$ , true rules in $\mathrm { D S } _ { 3 }$ are added to Ruleset1.

(5) When $K _ { 1 } ( V _ { 2 } )$ and $K _ { 1 } ( V _ { 3 } )$ , true rules in $\mathrm { D S } _ { 2 } \cup \mathrm { D S } _ { 3 }$ are added to Ruleset1. When $K _ { 1 } ( V _ { 2 } )$ or $K _ { 1 } ( V _ { 3 } )$ , if the rule $a _ { 2 } \to b _ { 2 }$ in $\mathrm { D S } _ { 2 } \cap \mathrm { D S } _ { 3 }$ is true, $a _ { 2 } \to b _ { 2 }$ are added to Ruleset1.

In the above examples, $K _ { 1 } ( I _ { i } )$ means that data source $\mathrm { D S } _ { 1 }$ believes that data source $\mathrm { D } \mathrm { S } _ { i }$ has introspection ability. $K _ { 1 } ( V _ { i } )$ means that data source $\mathrm { D S } _ { 1 }$ believes that data source $\mathrm { D S } _ { i }$ is veridical.

The values of $\dot { T } _ { 1 }$ and $V _ { 1 }$ are determined by the domain knowledge in $\mathrm { D S } _ { 1 }$ . Whereas the values of $K _ { 1 } ( I _ { 2 } ) , K _ { 1 } ( I _ { 3 } ) .$ $K _ { 1 } ( V _ { 2 } )$ and $K _ { 1 } ( V _ { 3 } )$ are determined by both domain knowledge and experienced knowledge in $\mathrm { D S } _ { 1 }$ . Domain knowledge can be a set of constraints. For example, ‘the salary of a regular employee is not over $\$ 10,0000.00$ per week’. Experience knowledge can be a set of rules extracted from historical data in data sources. For example, customers who ‘think that the supermarket Safeway is credible’.

## 6.2. Experiments

To evaluate the effectiveness of the proposed framework, we have carried out some experiments using Java on a DELL machine. Our experiments are designed to test the proposed approach from the veridicality of data sources.

![](/api/attachments/43HKQVDG/fulltext/images/87914d49ba88339385372efe4afe3a35b6856d396d6533ed2634c3f7a8791f2d.jpg)  
Fig. 1. Success ratios of TD and NOTD.

To obtain a group of data sources relevant and uncontradictable to a given dataset, we vertically partition a transaction database into a number of sub-sets, each containing a certain number of attributes. Also, we modify some of the data in some subsets so that the modified subsets are contradictory to the given dataset. We do this to test inconsistencies in data sources. In these experiments, multiple subsets were generated using databases from the Synthetic Classification Data Sets on the Internet (http://www.kdnuggets.com/).

We now carried out two sets of experiments on four classes of applications from a data source DS. One set assumes that DS uses rules only from trustworthy data sources. This set we call TD. The other we call NOTD, in which case DS randomly borrows external rules from other data sources.

We select 10 data sources and each has a set of rules. Eight are trustworthy, and two contain rules contradictory to DS, where those rules always cause failed applications. Note that association rules (including negative association rules) from a dataset are taken as patterns of the dataset for uncontradictability. A negative association rule (see Ref. [21]) $A \Rightarrow \neg B$ is defined as

(1) $\mathrm { A } \cap \mathrm { B } = \phi ;$

(2) supp(A)≥minsupp, supp(B)≥minsupp, and supp $( A \cup \lnot B ) _ { = }$ minsupp;

(3) supp( $A \cup \neg B ) / \operatorname { s u p p } ( A ) \geq \operatorname* { m i n c o n f } .$

Where minsupp and minconf are the minimum support and minimum confidence given by the user.

For the four classes of applications, each consists of ten reasoning tasks. The first class of application requires rules from 2 data sources. The second class of application requires rules from 3 data sources. The third class of application requires rules from 5 data sources. The fourth class of application requires rules from 6 data sources. The success ratios of TD and NOTD are depicted in Fig. 1.

In Fig. 1, the TD model received a 100% successratio because (1) the proposed technique has been utilized and (2) the given reasoning tasks can be finished by calling in trustworthy data sources. The NOTD model obtained a low success-ratio, decreasing according to the amount of fraudulent rules in untrustworthy data sources that were used.

## 7. Conclusions

Existing mining techniques may not always be helpful for identifying patterns from different data sources. This is because knowledge from external data sources may be untrustworthy, or even conflictive, and can disguise realistic patterns that might be useful to real-world applications. For this reason, we have proposed a framework for K3D, which aims to identify trustworthy knowledge in veridical data sources. The proposed approach is different from traditional data mining techniques because

(1) we distinguish internal knowledge from external knowledge;

(2) we have designed a logic framework for identifying trustworthy knowledge from various data sources; and

(3) untrustworthy and fraudulent knowledge have been eliminated by veridicality and introspection analysis.

Future work will involve the design of logic frameworks for resolving conflict, as we move towards the development of an agreed ontology for mining multiple data sources.

## References

[1] J. Aronis, et al., The WoRLD: knowledge discovery from multiple distributed databases, Proceedings of 10th International Florida AI Research Symposium, 1997, pp. 337–341.

[2] J.Y. Halpern, Reasoning with only knowing with many agents, Proc. of AAAI '93, 1993, pp. 655–661.

[3] J.Y. Halpern, A theory of knowledge and ignorance for many agents, Journal of Logic and Computation 7 (1997) 79–108.

[4] J.Y. Halpern, Y. Moses, Towards a theory of knowledge and ignorance, Proc. of AAAI Workshop on Non-Monotonic Logic, 1984, pp. 125–143.

[5] J. Halpern, Y. Moses, A guide to completeness and complexity for modal logics of knowledge and belief, Artificial Intelligence 54 (1992) 319–379.

[6] D. Kaplan, Review of “A semantical analysis of modal logic. I: normal modal propositional calculi”, Journal of Symbolic Logic 31 (1966) 120–122.

[7] S. Kripke, A semantical analysis of modal logic. I: Normal modal propositional calculi, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 9 (1963) 67–96.

[8] G. Lakemeyer, All they know about, Proc. of AAA'93, 1993, pp. 662–667.

[9] V. Lesser, B. Horling, F. Klassner, A. Raja, T. Wagner, S. Zhang, BIG: an agent for resource-bounded information gathering and decision making, Artificial Intelligence Journal, vol. 118, 1–2, 2000, pp. 197–244.

[10] J. Levesque, All I know: a study in autoepistemic logic, Artificial Intelligence 42 (1990) 263–309.

[11] H. Liu, H. Lu, J. Yao, Identifying relevant databases for multidatabase mining, Proceedings of PAKDD '98, 1998, pp. 210–221.

[12] J. McCarthy, Circumscription: a form of nonmonotonic reasoning, Artificial Intelligence 13 (1980) 27–39.

[13] R.C. Moore, Semantical considerations on nonmonotonic logic, Artificial Intelligence 25 (1985) 75–94

[14] R. Reiter, A logic for default reasoning, Artificial Intelligence 13 (1980) 81–132.

[15] K. Su, W. Li, Computation of seminormal default theories, Fundamental Informaticae 40 (1999) 79–102.

[16] K. Su, X. Luo, H. Wang, Chengqi Zhang, S. Zhang, Q. Chen, A logical framework for knowledge sharing in multi-agent systems, Proceedings of COCOON'01, August 2001.

[17] K. Su, H. Chen, D. Ding, Two alternative notions of possibility, Journal of Logic and Computation, 10 (2) (2000).

[18] R. Turner, Truth and Modality for Knowledge Representation, Pitman Publishing, London, 1990.

[19] M. Wooldridge, The logical modelling of computational multi-agent systems, Ph.D. thesis, University of Manchester, 1992.

[20] X. Wu, S. Zhang, Synthesizing high-frequency rules from different data sources, IEEE Transactions on Knowledge and Data Engineering 15 (2) (March/April 2003) 353–367.

[21] Xindong Wu, Chengqi Zhang, Shichao Zhang, Mining both positive and negative association rules, Proceedings of 19th International Conference on Machine Learning, Sydney, Australia, July 2002, pp. 658–665.

[22] Xindong Wu, Chengqi Zhang, Shichao Zhang, Database classification for multi-database mining, Information Systems 30 (2005) 71–88.

[23] Shichao Zhang, Xindong Wu, Chengqi Zhang, Multi-Database Mining, IEEE Computational Intelligence Bulletin 2 (1) (June 2003) 5–13.

[24] Shichao Zhang, Chengqi Zhang, Xindong Wu, Knowledge Discovery in Multiple Databases, Springer, ISBN: 1-85233-703-6, 2004, p. 233.

[25] Shichao Zhang, Chengqi Zhang, Qiang Yang, Information enhancement for data mining, IEEE Intelligent Systems (Mar./ Apr. 2004).

[26] N. Zhong, Y. Yao, S. Ohsuga, Peculiarity oriented multi-database mining, Principles of Data Mining and Knowledge Discovery, 1999, pp. 136–146.

![](/api/attachments/43HKQVDG/fulltext/images/2668c57d50f77bed8d96f210ac5ed05da511bd5249a90bfb678cbf40cf021dc6.jpg)

Kaili Su is a professor at the Sun Yatsen University and a Research Fellow at the Griffith University. He received his PhD degree in computer science from Nanjing University in 1995. He was a Visiting Research Fellow at the University of NSW from 2001 to 2002. His research interests include logic-based knowledge representation, verification of security protocols, model checking, multi-agent systems, and modal logic. He has published 68 papers,

including full papers published in top international conferences AAAI-04, AAAI-05, KR-04, and AAMAS-05; and papers in journals such as Information and Computation, Journal of Logic and Computation and Fundamenta Informaticae. He (with Meyden and Engelhardt) won the best paper award in AiML 2002.

![](/api/attachments/43HKQVDG/fulltext/images/8400558d1284ac244bd5f83554b9548542576c867983eac12b029d741b7c7e52.jpg)

Hui-jing Huang received his BS degree from Peking University in 1996 and has been awarded an MS degree in 2005 by the Institute of Computing Technology, Chinese Academy of Sciences. He is currently an engineer and a project manager at the Bureau of Personnel and Education, Chinese Academy of Sciences, Beijing, China. His research interests include network administration, data mining, ERP and software engineering.

![](/api/attachments/43HKQVDG/fulltext/images/05de4c8d89e2d2ec45c772fd6de878df6815fd97729434845f4f08e2c703fc09.jpg)

Xindong Wu is a Professor and the Chair of the Department of Computer Science at the University of Vermont. He holds a PhD in Artificial Intelligence from the University of Edinburgh, Britain. His research interests include data mining, knowledge-based systems, and Web information exploration. He has published extensively in these areas in various journals and conferences, including IEEE TKDE, TPAMI, ACM TOIS, IJCAI, AAAI, ICML, KDD, ICDM, and WWW, as

well as 12 books and conference proceedings. Dr. Wu is the Editor-in-Chief of the IEEE Transactions on Knowledge and Data Engineering (by the IEEE Computer Society), the founder and current Steering Committee Chair of the IEEE International Conference on Data Mining (ICDM), an Honorary Editor-in-Chief of Knowledge and Information Systems (by Springer), and a Series Editor of the Springer Book Series on Advanced Information and Knowledge Processing (AI&KP). He is the 2004 ACM SIGKDD Service Award winner.

![](/api/attachments/43HKQVDG/fulltext/images/9a3bc1d1d19dde2154226d4c2326dad1f054a5438f0ceeb37b90a7990d726bab.jpg)

Shichao Zhang is a senior research fellow in the Faculty of Information Technology at the University of Technology, Sydney, and a professor at the Guangxi Normal University. He received his PhD degree in computer science from Deakin University, Australia. His research interests include data analysis and smart pattern discovery. He has published over 30 international journal papers (including 6 in IEEE/ACM Transactions, 2 in Information Systems, 6

in IEEE magazines) and over 30 international conference papers (including 2 ICML papers and 3 FUZZ-IEEE/AAMAS papers). He has won 4 China NSF/863 grants, 3 Australian large ARC grants and 2 Australian small ARC grants. He is a senior member of the IEEE, a member of the ACM, and serving as an associate editor for Knowledge and Information Systems and The IEEE Intelligent Informatics Bulletin.
