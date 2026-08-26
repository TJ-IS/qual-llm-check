---
otero_id: 17375
otero_key: "DHH9HFPW"
title: "Model management"
authors: "Hemant K. Bhargava; Steven O. Kimbrough"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90064-a"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model management An embedded languages approach \*

Hemant K. Bhargava

Naval Postgraduate School, Monterey CA, USA

Steven O. Kimbrough

University of Pennsylvania, Philadelphia PA, USA

November 29, 1991

Model management is an important component of decision support. Executable modeling languages (EMLs) have been employed quite successfully in designing useful modeling systems. In this paper, we present a technique, called embedded languages, which is a generalization of the EML approach, we believe that this technique can prove extremely useful in implementing desirable features not usually found in existing systems. The approach is discussed with reference to such a system, TEFA, which has been developed, and is being improved, on the basis of this technique.

Keywords: Decision support systems; Model management; Logic; Artificial intelligence; Formal languages

## 1. Introduction

There is – at a high level of generality – broad agreement among information systems researchers regarding the goals and purposes of model management systems. These systems should, insofar as possible, support modeling activities throughout the modeling life cycle $[15,2,13,25]$ . They should provide material help both to users and builders of decision support systems in creating, validating, executing, manipulating, revising, and explaining models. There is not, however, broad agreement regarding how model management systems should be designed and built, that is, what their architectures should be. Even so, there is a substantial literature in which general agreement obtains that model management can be effect with an executable modeling language, or EML (see, e.g., $[7,12,17]$ ). What pervades the various approaches and systems described in the EML model management literature is the aim of representing mathematical models with “a declarative language that is formal in the sense that it has an unambiguous syntax and semantics” $[9]$ , which language can be used in executing models represented in it, and in providing various other model management features.

The purpose of this paper is to present and discuss a technique - which we call embedded languages – that we have developed and successfully employed to design and implement a model management system. This technique is a variant, indeed a generalization, of the EML approach to model management. Our model management system, called TEFA (“The Eileen Ford Agency”, since model management is such a fashionable topic) is currently being used by the US Coast Guard and has been partially described elsewhere $[1,2,4,6,20,21]$ . Further, it is currently being extended (e.g. $[3]$ ). This paper is about certain of the design principles used for TEFA (i.e., is about embedded languages), which we believe should be broadly interesting to the model management community. The paper is not primarily about the specific details of TEFA.

![](/api/attachments/DHH9HFPW/fulltext/images/26af46098b3a2977cd1a85cb3b4d5105d0014553b52fc6e54ab403e8c08bc793.jpg)

The central ideas of our research on embedded languages for model management can be summarized as follows. The EML approach has proved useful for developing model representations, and for manipulating these representations in ways that are useful for the purposes of model management (see the references). In addition, we claim it is highly useful to embed languages for performing specific model management tasks within a more general model management language. The benefits we have found in doing this include flexibility, expressive power, naturalness of expression, and clean modularity in the resulting code. More significantly, in our view, is the fact that the technique allows us to represent – both formally and computationally – information about expressions in a language that cannot (or cannot easily) be expressed in the language. This feature has been largely absent in the various existing executable modeling languages.

A small framework will be useful in explaining our position. Consider three related languages, called $L_{\downarrow}^{*}$ , $L_{\downarrow}$ , and $L^{\uparrow}$ . $L^{\uparrow}$ is the embedding language; it is completely formalized. TEFA – the model management language we have developed, are continuing to develop and will describe in part here – is an example of a particular embedding language. $L_{\downarrow}$ is the embedded language. It, too, is completely formalized and has a full interpretation as an independent (of $L^{\uparrow}$ ) language. The purpose of an $L_{\downarrow}$ language is (normally) to partially formalize and represent the target language, $L_{\downarrow}^{*}$ , which is normally not fully formalized, but typically contains significant natural language elements.

![](/api/attachments/DHH9HFPW/fulltext/images/3de3801a8baeffa25aea0cb05f0a26b4ee6814e49703a2f9b26e37cc1fc2a443.jpg)

In the context of applying this technique to model management, the embedded language might be an EML such as AMPL $[12]$ or SML $[17]$ , with the target language being the (natural and man-made) language we use to represent, discuss, and reason about mathematical programming models. In general, the target language is often some variety of natural language, is usually quite complex, and may be formalized in part. The technique does not require the target language to be fully formal. The embedded language (or languages, since there can be more than one) models (model) parts of the target language(s).

The idea behind the (standard) EML approach is to develop an appropriate $L_{\downarrow}$ , i.e., a fully formal language that is itself a model of the language ( $L_{\downarrow}^{*}$ , a combination of natural language and mathematics) we would otherwise use to represent and reason about mathematical models. The motivating idea behind our embedded languages approach is to embed one or more $L_{\downarrow}$ languages in an $L^{\uparrow}$ language, which is itself executable. Further, $L^{\uparrow}$ can be used to represent information about expressions (formulas and terms) in an $L_{\downarrow}$ language, including, e.g., rules of formation of expressions, and rules for translating one embedded EML (call it $L_{\downarrow}^{i}$ ) into another (call it $L_{\downarrow}^{j}$ ). We shall make extensive use of this framework in what follows. We hope to present with some clarity and depth the idea of the embedded languages approach to model management, as well as some of the reasons why we believe this is a promising and useful technique (not the least of which is our experience with the implementation of TEFA).

The strategy underlying our development of the embedded languages approach to model management is best described as follows. We recognize that the model management community has produced excellent work in developing particular modeling languages. These languages have competing strengths and weakness, and are often aimed at different purposes, e.g., some are strong for mathematical programming models in general, others work only for linear programming models, still others support only simulation models. Instead of aiming to design a universal modeling language, we have sought to develop techniques for exploiting particular modeling languages (particular $L_{\downarrow}$ languages) and for combining them in a common modeling system. $^{1}$

In what follows, we shall illustrate the embedded languages technique in some detail, but on a very simple language, sentence logic. That is the subject of section 3. In section 4, we discuss how this technique is applied to model management by embedding an EML in our model management language. This allows us to represent formally, flexibly, and generally, models and information about them and to define useful functions for a model management system. We discuss the usefulness of this approach in developing our model management system, TEFA. We conclude, in section 5, with some interpretive remarks about the method of embedded languages as it applies to model management. First, however, we shall present briefly, in section 2, the essentials of our concept of model management, provide motivation for the need for the embedded languages approach, and present an example, to which we shall advert in section 4.

## 2. Concept and motivation

The objective of a model management system is to provide automated support to modelers for activities performed during the major modeling life-cycle phases. These phases include:

\- Identification of the problem;

\- formulation and specification of the model in some appropriate formalism (e.g., an algebraic statement);

\- implementation and validation of the model;

\- interpretation and communication of the model;

\- data collection and analysis, pertinent to the particular problem at hand; determination of parameter values;

\- solver selection and model solution;

\- interpretation and analysis of the solution;

\- evaluation and modification of the model.

Although the purposes of this paper do not require a detailed discussion of these phases and the role of model management systems in supporting them, we make two observations. One, the solution phase usually comprises less than 10% of the modeling effort and time (see e.g., [13]), and essentially relies only on the mathematical structure of the model, which is very well represented in a standard EML. Two, to provide support for the remaining phases, such mathematical information is not enough – one must generally draw upon a variety of quantitative as well as qualitative information about models, variables, and data scenarios. Such information includes the mathematical structure of a model, assumptions underlying it, references and documentation of the model, dimensions and units of variables [9,4], source and reliability of data, quality of results under different conditions, computational experience with the model, user comments, and so on. We believe that what can be achieved with model management must rely on a rigorous and flexible representation of (a) models; and (b) information about them that is required to perform the above functions.

For the sake of precision, let us consider one specific example for our second observation above. This concerns the problem of unique names violations in model integration, discussed in [4]. Consider the situation where two or more models are built independently, and later need to be integrated. It is quite likely, since they were developed independently, that different variable names are used in these models for what should be identical variables. Since the variable names are different, it is also quite likely that these variables (really, the same variable) will have different values in the same scenario. (This could happen for various reasons, such as different measurement devices.) In the integrated model, such a state of affairs is clearly inconsistent. What can a model management system do to provide support for resolving unique names violations? A reasonable starting point is, wherever possible, to detect such violations automatically. But how is the system to know that two different variables were actually intended to represent the same object? Clearly one (a modeler or the machine) needs more information to make such inferences. The solution proposed in [4] illustrates the general principle that has guided the design of our model management language: Predicate information about modeling elements (here, variables), and use this information in making materially useful inferences. In this case, we must capture information about what it is that a variable essentially represents – its quiddity (and its dimension) – and compare the quiddites of pairs of variables to see if they possibly represent the same object. The larger lesson here, we believe, is that embedded languages is a technique that facilitates the addition and exploitation in this way of information that was not anticipated when the modeling system was originally designed and built.

Finally, for present purposes we will assume that model management functions are most appropriately implemented in executable modeling languages for model management. Existing ELMs (e.g., [12]) focus primarily on translation to and from one or more solvers, although some (e.g., [15]) successfully exploit the model representations for display purposes. Briefly, existing EMLs provide a formal representation for the models, (a, above), but do little to provide for representation and exploitation of information about the models, (b). It is information of this latter sort that, we believe, is key to developing advanced, general-purpose model management systems. This belief is supported by other researchers attempting to develop advanced modeling environments (e.g., [8]). In the sequel, we shall attempt to provide some details on our reasons for this belief.

In order to see our motivation for using the embedded languages approach to model management, consider the following simple example, which may be taken to represent a model in $L_{\downarrow}^{*}$ , the ordinary language of human modelers. The representation includes mathematical expressions comprising the model, and certain other information as seen below.

Example 1. A simple-lot-size EOQ model This model is one of the simplest models used to determine optimal reorder quantities and reorder points for a single item, with the objective of minimizing total costs and ensuring sufficient inventory to meet the demand for that item, under a set of assumptions stated below. The total cost (not including the purchase cost of the item), and the number of orders per period, are defined by the following equations (the order quantity is the same for each order, and the inter-order time is constant).

$$
\mathrm{TC} = \frac {a d}{q} + h q _ {\text { ave }},\tag{1}
$$

$$
n \stackrel {\text { def }} {=} \frac {d}{q}.\tag{2}
$$

The optimal cost is determined by selecting q so as to minimize TC.

$$
\mathrm{TC} ^ {*} \stackrel {\text { def }} {=} \min _ {q} (\mathrm{TC}).\tag{3}
$$

This cost is minimized when q is given by the following equation.

$$
q ^ {*} \stackrel {\mathrm{def}} {=} \sqrt {\frac {(2 a d)}{h}}.\tag{4}
$$

The EOQ model, given by the above equations, is developed and explained in Analysis of Inventory Systems, by G. Hadley and T. Whitin. The model contains the following variables: TC (total cost, in dollars), $q^{*}$ (optimal reorder quantity, in itemunits), $q_{ave}$ (average inventory between orders, in item-units), a (setup cost, in dollars), d (demand for the period, in item-units), h (holding cost, in dollars per item-units), and n (number of orders). It is assumed that the demand is deterministic and known, the holding cost is linear, the setup cost is constant, and there is no lead time.

As simple as this example is, there are several interesting things to notice, things that motivate our approach. First, although the mathematical expression of the model (as equations) is essential to solving it – and to understanding it – the mathematics certainly do not capture the essential information in the accompanying paragraph. Second, the accompanying paragraph provides information about the model. This, from the point of view of formal logic, naturally suggests using a referring expression (name or function) to represent the model, and expressing information about the model by predicating that information on the referring expression. Third, as seen in the accompanying paragraph, the model contains variables, which we want to mention (when we say things about them) and which we want to use (as variables, when we execute the model). This naturally suggests finding a way to have a dual interpretation for certain symbols. Fourth, our eyes and experience tell us that the equations are well formed. We want, however, to rely as much as possible on the model management system to make this determination, and if it is to do so, it must not only represent the mathematical expressions, but also have knowledge about the valid formation conditions for the expressions. Normally, it is impossible to express in a language its own expression formation rules. These points strongly suggest to us the utility of building a language for expressing knowledge about (and for manipulating) expressions in a modeling language. That is how we built TEFA.

Having indicated some of the motivation for the embedded languages approach, we shall now explain the essential details of how such a language for working with and reasoning about other languages can be constructed, and what can be done with it. Because the story is complex, we shall begin in section 3 with a simple example, pursued in some depth. Following that, in section 4, we will lay out our version of the embedded languages approach for model management. We will use the example presented above to illustrate our point.

## 3. The technique illustrated: Sentence logic

There is something paradoxical about the idea of embedding one language, call it $L_{\downarrow}$ , within another language, call it $L^{\uparrow}$ . It is our intention that formulas – either in $L_{\downarrow}$ or in $L^{\uparrow}$ – are to be interpreted propositionally. These formulas have truth values. It is also our intention that $L^{\uparrow}$ be a language of first-order logic (FOL), yet on any straightforward view, first-order logic does not permit predication applied to truth-bearing formulas. For example, $F(a)$ – where a stands for “Bob” and $F(x)$ stands for “x is tall” – is a well-formed formula in FOL, with a an individual constant and F a predicate of arity 1. But, $G(F(a))$ , where G is any predicate at all, is not a legal expression in FOL. How then is this sort of embedding to be done? The purpose of this section is to answer this question precisely, using sentence logic as the embedded language.

In section 3.1, we lay out our basic framework for talking about embedded languages and we describe in some detail how sentence logic may be embedded in another language family, here first-order logic which we also use as the embedding language family for our model management system. Sentence logic is a particularly apt language to use for this example, in part because of its simplicity. Few formal languages of interest – and even fewer in case of model management – are as simple and easily understood as sentence logic. Then, in section 3.2, we discuss the significance of performing the embedding. We shall make some general remarks regarding why it is worth doing and what can be gained from it. This will set the stage for our discussion, in section 4, of our embedded language approach to model management proper.

## 3.1. Embedding sentence logic

To begin, we need to consider three languages: $L^{\uparrow}$ , the embedding language; $L_{\downarrow}$ , the embedded language; and $L_{\downarrow}^{*}$ , the language - called the target language - modeled by the embedding. Here, $L_{\downarrow}^{*}$ will be our ordinary language for expressing propositions and for reasoning about them. $L_{\downarrow}$ will be ordinary sentence logic. Finally, $L^{\uparrow}$ will be an FOL language that embeds $L_{\downarrow}$ and that can also represent information useful for reasoning about propositional expressions, information that is not expressible in sentence logic ( $L_{\downarrow}$ ).

To illustrate the basic ideas, consider a very simple inference in sentence logic. In $L_{\downarrow}^{*}$ we have as axioms:

\- if Cynthia is home, then the phone rings four times before the answering machine kicks in;

\- the answering machine has kicked in on two rings.

from which it follows that Cynthia is not home. Our symbolization scheme for translating into $L_{\downarrow}$ is: p :: “Cynthia is home”; q :: “The phone rings four times before the answering machine kicks in”. This results in the following symbolization of the above sentences into $L_{\downarrow}$ :

$$
\bullet \quad p \rightarrow q,
$$

$$
\bullet \neg q,
$$

from which it follows - using standard inference procedures in sentence logic - that $\neg p$ . (Notice that our representation in $L_{\downarrow}$ does not fully express the original meaning of the sentences in $L_{\downarrow}^{*}$ , but is good enough for present purposes. This is the normal situation with formal modeling languages; they represent a portion of the information at hand, but (one hopes) a portion sufficient for the purposes at hand.)

As we shall see, we may embed the above $L_{\downarrow}$ expressions in $L^{\uparrow}$ (a first-order logic language) as follows.

$$
\begin{array}{r l} & {\bullet S (i ^ {f} (p, q)),} \\ & {\bullet S (n ^ {f} (q)),} \end{array}
$$

from which it will follow that $S(n^{f}(p))$ (given the addition of certain axioms, discussed in the sequel). The correspondence, in this case, between expressions in $L_{\downarrow}$ and expressions in $L^{\uparrow}$ should be fairly transparent. Here, the $L_{\downarrow}$ expression $\neg q$ has been re-expressed as $n^{f}(q)$ and placed into the argument slot of the S predicate, producing $S(n^{f}(q))$ . Similarly, $p \to q$ has been re-expressed as $i^{f}(p, q)$ and embedded as $S(i^{f}(p, q))$ .

There are two important points to notice about this embedding example. First, in $L_{\downarrow}^{*}$ it is possible to say things about the sentences in question. For example, we might know that if Cynthia is home, then the phone rings four times before the answering machine kicks in because Cynthia told us. This information is easy to express in $L_{\downarrow}^{*}$ , i.e., in natural language, but it cannot – or cannot adequately – be expressed in sentence logic. In sentence logic we simply have declarative sentences and Boolean combinations of such sentences; we cannot refer to one sentence with another. The situation is quite different in $L^{\uparrow}$ . Here we simply need to declare a predicate – e.g., ‘Source’ $_{p}(x, y)$ : “The source of the information that x is y” – and use it: ‘Source’ $_{p}(i^{f}(p, q), Cynthia)$ .

The second important point to notice about this example is that when the $L_{\downarrow}$ formulas ( $p \rightarrow q$ , $\neg q$ ) are re-expressed (producing $i^{f}(p, q)$ and $n^{f}(q)$ ), the resulting expressions are terms in $L^{\uparrow}$ . Specifically, the analog in $L^{\uparrow}$ of the $L_{\downarrow}$ logical connective $\rightarrow$ is a two-argument function constant, $i^{f}$ (for “implication”). Similarly, $\neg$ is a sentence operator in $L_{\downarrow}$ and its analog in $L^{\uparrow}$ is the one-argument function constant, $n^{f}$ (for “negation”). The embedding works – here and in general – by re-expressing formulas (truth-bearing expressions) in the $L_{\downarrow}$ language as terms (expressions that refer to individuals) in the $L^{\uparrow}$ language.

Finally, before discussing the technical details of embedding sentence logic, and of embedding in general, it is instructive to recall our earlier example, the EOQ model in section 2. The example should be thought of as presented in $L_{\downarrow}^{*}$ , a mixture of ordinary English and algebra. Part of the information in the example – the algebraic model – could easily be represented in a fully-formalized $L_{\downarrow}$ language (and we do just that in the sequel). Doing this, however, would leave out a great deal of the (largely qualitative) information in the example. Just as “Cynthia told me that if she is home, then the phone rings four times before the answering machine kicks in” cannot be adequately represented in sentence logic, so “It is assumed that the demand is deterministic and known, the holding cost is linear, the setup cost is constant, and there is no lead time” cannot be adequately expressed in the language of equational algebra. It is, or course, always possible to extend the languages of sentence logic and equational algebra in order to be able to represent such additional information. The embedded languages technique may be thought of as a general, principled way of doing this, without at the same time effectively abandoning the original $L_{\downarrow}$ languages. We shall discuss the advantages of the embedded languages technique in the sequel. For the present we turn to a more careful and thorough discussion of what the technique is. We shall focus on how it may be applied to sentence logic because sentence logic is clear and simple and because it is possible to perform the embedding completely.

First, we specify the alphabet and rules of formation for our $L_{\downarrow}$ language, sentence logic.

(1) The alphabet for our $L_{\downarrow}$ language, sentence logic, is as follows:

(a) Countably many sentence letters: $a$ , $b, \ldots, z$ , $a_1, a_2, \ldots, b_1, \ldots$ ,

(b) left and right parentheses: ( , ),

(c) logical constants: $\wedge, \vee, \neg, \rightarrow, \leftrightarrow$ ,

(d) nothing else not in the above enumeration is in the alphabet of sentence logic;

(2) The well-formed formulas (wffs) for $L_{\downarrow}$ are as follows:

(a) Any sentence letter is a well-formed formula (wff);

(b) $\neg \phi$ is a wff if $\phi$ is a wff;

(c) $(\phi \wedge \psi)$ is a wff if both $\phi$ and $\psi$ are wffs; (d) $(\phi \vee \psi)$ is a wff if both $\phi$ and $\psi$ are wffs;

(e) $(\phi \rightarrow \psi)$ is a wff if both $\phi$ and $\psi$ are wffs;

(f) $(\phi \leftrightarrow \psi)$ is a wff if both $\phi$ and $\psi$ are wffs;

(g) nothing else, not required by the above, is a wff.

Next, we specify the alphabet and rules of formation four our $L^{\uparrow}$ language, first-order logic (FOL).

(1) The alphabet for our $\mathbf{L}^{\uparrow}$ language, FOL, is as follows:

(a) countably many predicate letters or constants: $\bot$ , $A, B, \ldots, Z$ , $A_1, A_2, \ldots, B_1, \ldots$ , plus any alphanumeric string enclosed in single quotes and subscripted with a $p$ , with each predicate constant having an associated arity (number of arguments), an integer greater than or equal to zero (the special predicate constant $\bot$ has an arity of zero). (b) Countably many individual constants: $a, b, \ldots, z$ , $a_1, a_2, \ldots, b_1, \ldots$ , plus any alphanumeric string enclosed in single quotes and not subscripted or superscripted,

(c) Countably many function constants: $a^{f}$ , $b^{f},\ldots,z^{f}$ , $a_{1}^{f}$ , $a_{2}^{f},\ldots,b_{1}^{f},\ldots$ , with each function constant having an associated arity (number of arguments), an integer greater than or equal to one,

(d) Countably many individual variables: $a^v$ , $b^v, \ldots, z^v, a_1^v, a_2^v, \ldots, b_1^v, \ldots,$

(e) Left and right parentheses: ( , ),

(f) Logical constants: $\wedge, \vee, \neg, \rightarrow, \leftrightarrow, \exists, \forall$ ,

(g) A special logical predicate constant: =,

(h) Nothing else not in the above enumeration is in the alphabet of FOL;

(2) The (well-formed) terms of FOL are as follows:

(a) any individual constant is a term,

(b) any individual variable is a term,

(c) if $\rho$ is a function constant of arity $n$ , the $\rho(\tau_1, \tau_2, \ldots, \tau_n)$ is a term if all of $\tau_1, \tau_2, \ldots, \tau_n$ are terms,

(d) nothing else, not required by the above, is a (well-formed) term;

(3) The well-formed formulas (wffs) for FOL are as follows:

(a) If $\phi$ is a predicate constant of arity $n$ and if all of $\tau_{1}, \tau_{2}, \ldots, \tau_{n}$ are terms, then $\phi(\tau_{1}, \tau_{2}, \ldots, \tau_{n})$ is a wff,

(b) $\neg \phi$ is a wff if $\phi$ is a wff,

(c) $(\phi \wedge \psi)$ is a wff if both $\phi$ and $\psi$ are wffs, (d) $(\phi \vee \psi)$ is a wff if both $\phi$ and $\psi$ are wffs,

(e) $(\phi \to \psi)$ is a wff if both $\phi$ and $\psi$ are wffs,

(f) $(\phi \leftrightarrow \psi)$ is a wff if both $\phi$ and $\psi$ are wffs,

(g) $\forall \chi \phi$ is a wff if $\phi$ is a wff and $\chi$ is an individual variable,

(h) $\exists \chi \phi$ is a wff if $\phi$ is a wff and $\chi$ is an individual variable,

(i) Nothing else, not required by the above, is a wff.

Now, using these two specific languages as a running example, we shall define the key concepts associated with the embedded languages idea. There are four. First, an embedding (of $L_{\downarrow}$ in $L^{\uparrow}$ ) is a triple, $\langle J, F, \Delta \rangle$ , where:

(1) $\mathcal{I}$ , called the image function, uniquely maps all expressions (terms and formulas) in $L_{\downarrow}$ into terms in $L^{\uparrow}$ . We require $\mathcal{I}$ be invertible, i.e., that $\mathcal{I}^{-1}(\mathcal{I}(\phi)) = \phi$ , for all expressions, $\phi$ , in $L_{\downarrow}$ .

(2) $\mathcal{F}$ , called the translation function, uniquely maps the images of all formulas in $L_{\downarrow}$ (which are terms in $L^{\uparrow}$ ) into formulas in $L^{\uparrow}$ . We require that $F$ be invertible, i.e., that $\mathcal{F}^{-1}(\mathcal{F}(\mathcal{I}(\phi))) = \mathcal{I}(\phi)$ .

(3) $\Delta$ is a (possibly empty) collection of $L^{\uparrow}$ formulas for representing the rules of inference and transformation of $L_{\downarrow}$ .

Second, we say that a collection of formulas, $\Phi$ , from $L_{\downarrow}$ is embedded as a collection of formulas, $\Psi$ , in $L^{\uparrow}$ for a particular embedding, E if $\Psi$ comes from $\Phi$ by applying the embedding, $\mathcal{E}$ to $\Phi$ . More formally, we require that if $\mathcal{E} = \langle \mathcal{I}, \mathcal{F}, \Delta \rangle$ , then

$$
\Psi = \Delta \cup \bigcup_ {\phi \in \Phi} \mathcal {F} (\mathcal {I} (\phi))
$$

As our third key concept associated with the embedded languages idea, we say that an embedding is correct if, when $\Phi$ is embedded as $\Psi$ , then what can be derived in $L^{\uparrow}$ from $\Psi$ is "the same as" what can be derived from $\Psi$ in $L_{\downarrow}$ . More formally, we say that an embedding is correct if, for all $\Gamma$ , $\phi$ in the $L_{\downarrow}$ embedded set, $\Phi$ , if $\Delta$ , $\mathcal{F}(\mathcal{I}(\Gamma)) \vdash_{L^{\uparrow}} \mathcal{F}(\mathcal{I}(\phi))$ ,

then

$$
\Gamma \vdash_ {L _ {\downarrow}} \phi .
$$

Fourth, and finally, we say that an embedding is complete (for a set of $L_{\downarrow}$ sentences, $\Phi$ ) if, for all $\Gamma, \phi$ in the $L_{\downarrow}$ embedded set, $\Phi$ , if

$$
\Gamma \vdash_ {L _ {\perp}} \phi ,
$$

then

$$
\Delta , \mathcal {F} (\mathcal {I} (\Gamma)) \vdash_ {L ^ {\uparrow}} \mathcal {F} (\mathcal {I} (\phi)).
$$

What remains to be done in this section is to define a particular embedding of sentence logic in FOL, to show that the puted embedding actually is an embedding, and to show that the embedding is correct and complete.

In defining our embedding, $\langle I, F, \Delta \rangle$ , of sentence logic (our current $L_{\downarrow}$ language) into predicate logic (our current $L^{\uparrow}$ language), we shall proceed element by element.

(1) For any well-formed formula in sentence logic, $\phi$ , $\mathcal{I}(\phi)$ is defined as follows (see the definition above of the wffs of $L_{\downarrow}$ ): (a) if $\phi$ is a sentence letter of $L_{\downarrow}$ , then $\mathcal{I}(\phi) = \phi$ . (note the - useful but unnecessary - pun here; $\phi$ is a setence letter in $L_{\downarrow}$ and an individual constant in $L^{\uparrow}$ ; it is convenient but unnecessary that the same symbol be used for both purposes); (b) if $\neg \phi$ is a wff of $L_{\downarrow}$ , then $\mathcal{I}(\neg \phi) = n^{f}(\mathcal{I}(\phi))$ (note here that the logical constant, $\neg$ , in $L_{\downarrow}$ has been transformed by the embedding into a particular function constant, $n^{f}$ , in $L^{\uparrow}$ ); (c) if $(\phi \wedge \psi)$ is a wff in $L_{\downarrow}$ , then $\mathcal{I}((\phi \wedge \psi)) = c^{f}(\mathcal{I}(\phi), \mathcal{I}(\psi))$ ( $c^{f}$ is a function constant for conjunction):

(d) if $(\phi \vee \psi)$ is a wff in $L_{\downarrow}$ , then $\mathcal{I}((\phi \vee \psi)) = d^{f}(\mathcal{I}(\phi), \mathcal{I}(\psi))(d^{f}$ is a function constant for disjunction);  
(e) if $(\phi \to \psi)$ is a wff in $L_{\downarrow}$ , then $\mathcal{I}((\phi \to \psi)) = i^{f}(\mathcal{I}(\phi), \mathcal{I}(\psi))(i^{f}$ is a function constant for material implication);  
(f) if $(\phi \leftrightarrow \psi)$ is a wff in $L_{\downarrow}$ , then $\mathcal{I}((\phi \leftrightarrow \psi)) = b^{f}(\mathcal{I}(\phi), \mathcal{I}(\psi))(b^{f}$ is a function constant for biconditional);

(g) nothing else, not required by the above, is mapped by $\mathcal{I}$ (note that every wff in $L_{\downarrow}$ is transformed by $\mathcal{I}$ to a term in $L^{\uparrow}$ , that these terms contain only individual constants and function constants, and that - by inspection - this transformation satisfied the invertibility requirement on $\mathcal{I}$ .)

(2) If $\phi$ is a wff in $L_{\downarrow}$ and $\mathcal{I}(\phi) = \psi$ , then $\mathcal{F}(\psi) = S(\psi)$ . (Note that $\mathcal{F}$ is here very simple. Complicating generalizations are certainly possible and may well be useful. For example, if we were embedding many $L_{\downarrow}$ languages we might have $\mathcal{F}(\psi) = S(\psi, \text{'sentence-logic'})$ in order to identify the source $L_{\downarrow}$ language. Note as well that $\mathcal{F}$ is invertible.)

$\Delta$ consists of ten "non-logical" formulae:  
(a) $\forall x(S(n^{f}(n^{f}(x))) \to S(x));$ (b) $\forall x \forall y(S(c^{f}(x, y)) \to (S(x) \land S(y)));$ (c) $\forall x \forall y(S(n^{f}(c^{f}(x, y))) \to (S(n^{f}(x)) \lor S(n^{f}(y)));$ (d) $\forall x \forall y(S(d^{f}(x, y)) \to (S(x) \lor S(y)));$ (e) $\forall x \forall y(S(n^{f}(d^{f}(x, y))) \to (S(n^{f}(x)) \land S(n^{f}(y)));$ (f) $\forall x \forall y(S(i^{f}(x, y)) \to (S(n^{f}(x)) \lor S(y)));$ (g) $\forall x \forall y(S(n^{f}(i^{f}(x, y))) \to (S(x) \land S(n^{f}(y)));$ (h) $\forall x \forall y(S(b^{f}(x, y)) \to ((S(x) \land S(y))) \lor (S(n^{f}(x)) \land S(n^{f}(y)));$ (i) $\forall x \forall y(S(n^{f}(b^{f}(x, y))) \to ((S(x) \land S(n^{f}(y)))) \lor (S(n^{f}(x)) \land S(y)));$ (j) $\forall x(S(n^{f}(x)) \to \neg S(x)).$

Some comments are in order regarding $\Delta$ . The nine items, $\Delta_{a} \ldots \Delta_{i}$ , correspond precisely to the rules of inference for a standard (complete and consistent) form of sentence logic, [19]. For example, in $L_{\downarrow}$ we have a rule of inference - expressed in the metalanguage for $L_{\downarrow}$ - that says: if $\neg \neg \phi$ is derivable, then $\phi$ is derivable. Rule $\Delta_{a}$ , above, says just this, and it says it in $L^{\uparrow}$ about expressions in $L_{\downarrow}$ , as embedded in $L^{\uparrow}$ . With $\Delta$ we have succeeded in formalizing part of the metalanguage for $L_{\downarrow}$ . The tenth item in $\Delta$ may be thought of as a rule that bridges between $L_{\downarrow}$ and $L^{\uparrow}$ ; it links $n^{f}$ with $\neg$ .

Note, most importantly, that each of the members of $\Delta$ is – when universally instantiated and translated back to $L_{\downarrow}$ – a tautology. For example, from $\Delta_{a}$ we get (in $L^{\uparrow}$ ) $S(n^{f}(n^{f}(p))) \to S(p)$ by universally instantiating p for x. But, when we invert this expression to get a formula in $L_{\downarrow}$ , we get $\neg \neg p \to p$ , which is a tautology. The story for the rest of the elements of $\Delta$ is the same. In short, the $\Delta$ axioms are “non-logical” from the point of view of $L^{\uparrow}$ ; from the point of view of $L_{\downarrow}$ they are all logical truths.

Having defined the embedding, it remains to show that it is correct and complete. We will merely sketch the proof, since it is rather direct and simple in concept. Regarding completeness, it is easy to see that any proof carried out in $L_{\downarrow}$ can also be carried out in the $L^{\uparrow}$ embedded version. Briefly, every transformation permitted by a rule of inference in $L_{\downarrow}$ is also allowed in $L^{\uparrow}$ . Reverting to our running example, if in $L_{\downarrow}$ we are able to derive a formula of the form $\neg\neg\phi$ , then we are allowed (by an $L_{\downarrow}$ rule of inference) to derive $\phi$ . Correspondingly, if in $L^{\uparrow}$ we can derive $S(n^{f}(n^{f}(\mathcal{I}(\phi))))$ (the translation of $\neg\neg\phi$ ), then – using $\Delta_{a}$ and modus ponens – we can derive $S(\mathcal{I}(\phi))$ (the translation of $\phi$ ). The point holds in general. Finally, using the truth-tree method [19], we must locate contradictions to perform proofs. Suppose that in $L_{\downarrow}$ we have derived both $\phi$ and $\neg\phi$ , then in $L^{\uparrow}$ we can derive both $S(\mathcal{I}(\phi))$ and $S(n^{f}(\mathcal{I}(\phi)))$ . Using $\Delta_{j}$ and modus ponens, we can then derive $\neg S(\mathcal{I}(\phi))$ , and we have our contradiction in $L^{\uparrow}$ . It should be plain that our embedding is complete.

What makes our embedding correct is the required restriction that there are no expressions involving the predicate S in $L^{\uparrow}$ except as provided for by the embedding (i.e., either in the embedding or derivable from it). We are not, for example, allowed to add $\forall x(S(n^{f}(n^{f}(x))) \to S(n^{f}(x)))$ to $L^{\uparrow}$ , since this does not correspond to a tautology in $L_{\downarrow}$ . Thus, restricting $\Delta$ as above (to tautologies in $L_{\downarrow}$ ) is to ensure that only logically correct inferences will be drawn in the embedding.

We have now fully embedded $L_{\downarrow}$ in $L^{\uparrow}$ . This has been possible in part because of the simplicity of sentence logic. In general, i.e., when moving beyond sentence logic, it may not always be either possible or desirable to implement a full embedding. We will almost always demand correctness, but not require or obtain completeness.

## 3.2. Discussion: Significance of the embedding

Where are we now and what have we gained? First, a discussion of where we are. Think of it this way. We want to reason with, to perform inferences with, statements in $L_{\downarrow}^{*}$ , but $L_{\downarrow}^{*}$ is (typically) not completely formalized, so we model part of $L_{\downarrow}^{*}$ with a fully formal language, $L_{\downarrow}$ . Now, given $L_{\downarrow}$ it would certainly be possible to develop procedures (we can think of them as inference engines) that manipulate a collection of expressions in $L_{\downarrow}$ (think of these as declarations in a knowledge base). Instead – or so we are advocating – we embed $L_{\downarrow}$ expressions in another formal language, $L^{\uparrow}$ , then we treat these expressions as declarations in a knowledge base and we write inference engines for them. Further, we illustrated this idea in section 3.1 with sentence logic. The idea is that $L^{\uparrow}$ is a logical language for which there is a standard proof procedure (not discussed in section 3.1). $L_{\downarrow}$ , however, also had an implicit and standard proof procedure. Note that the inferential procedure for $L_{\downarrow}$ (what one does, e.g., to prove a theorem in $L_{\downarrow}$ ) cannot be represented in $L_{\downarrow}$ ; nor can the inferential procedure for $L^{\uparrow}$ be represented in $L^{\uparrow}$ . When we embedded $L_{\downarrow}$ , however, we represented statements from $L_{\downarrow}$ in $L^{\uparrow}$ and we represented the proof procedure for $L_{\downarrow}$ in $L^{\uparrow}$ . That is the role of the “non-logical” axioms, $\Delta$ , above.

To illustrate the point, recall a very simple inference in sentence logic. In $L_{\downarrow}^{*}$ we have as axioms

\- if Cynthia is home, then the phone rings four times before the answering machine kicks in;

\- the answering machine has kicked in on two rings;

from which it follows that Cynthia is not home. Our symbolization scheme for translating into $L_{\downarrow}$ is: p:: “Cynthia is home”; q:: “The phone rings four times before the answering machine kicks in". This results in the following symbolization of the above sentences into $L_{\downarrow}$ .

$$
\bullet \mathrm{p} \rightarrow \mathrm{q},
$$

$$
\bullet \neg q,
$$

from which it follows - using standard inference procedures in sentence logic - that $\neg p$ . To prove this, we add the denial of the conclusion to the premises and derive a contradiction.

(1) $p \to q$ (first premise);

(2) $\neg q$ (second premise);

(3) $\neg \neg p$ (denial of the conclusion);

(4) $p$ (from $\neg \neg p$ using the inference rule for double negation);

(5) $q$ (from $p$ and $p \to q$ using the inference rule of modus ponens);

(6) Done. (both q and $\neg q$ have been derived, the argument is shown to be valid via a proof by contradiction).

We embed the above $L_{\downarrow}$ expressions in $L^{\uparrow}$ as follows

\- $S(i^{f}(p,q))$ ,

• $S(n^{f}(q))$ ,

from which it will follow that $S(n^{f}(p))$ . To prove this, we add the denial of the conclusion to the premise and derive a contradiction.

(1) $S(i^{f}(p,q))$ (first premise);

(2) $S(n^{f}(q))$ (second premise);

(3) $S(n^{f}(n^{f}(p)))$ (denial of the conclusion);

(4) $\forall x(S(n^{f}(n^{f}(x)))\to S(x))$ (axiom $\Delta_{a}$ );

(5) $S(p)$ (from the previous two lines and modus ponens);

(6) $\forall x\forall y(S(i^{f}(x,y))\to (S(n^{f}(x))\lor S(y)))$ (axiom $\Delta_f$ );

(7) $(\dot{S}(n^{f}(p))\vee S(q))$ (first premise, $\Delta_f$ , universal instantiation, and modus ponens);

(8) $\forall x(S(n^f(x))\to \neg S(x))$ (axiom $\Delta_{j}$ );

(9) $\neg S(q)$ (second premise and $\Delta_{j}$ );

(10) $(\neg S(p)) \vee S(q)) ((S(n^f(p)) \vee S(q))$ and $\Delta_j)$ ;

(11) Done. $(S(p), \neg S(q)$ , and $(\neg S(p)) \vee S(q))$ are contradictory in $L^{\uparrow}$ .

The point may be summarized this way. What is achieved by embedding an $L_{\downarrow}$ in an $L^{\uparrow}$ is not merely that expressions in $L_{\downarrow}$ (in sentence logic for our current example) get represented in $L^{\uparrow}$ .

In addition, the procedures, the inference engines, for reasoning with expressions in $L_{\downarrow}$ also get represented in $L^{\uparrow}$ . That, in brief, is where we are. What, then, does it buy us?

There are, we believe, three main categories of benefits associated with embedded languages. First, and perhaps most important for model management, is that once an $L_{\downarrow}$ language is embedded in an $L^{\uparrow}$ language it becomes rather straightforward to express knowledge about expressions in the embedded language. Normally, it is impossible to express such knowledge in the $L_{\downarrow}$ language itself. Recalling the last example we have it in $L_{\downarrow}$ that $p \rightarrow q$ . What is the source of that information? Impossible to say in $L_{\downarrow}$ and easy to say in $L^{\uparrow}$ . We simply add an appropriate predicate to $L^{\uparrow}$ and make the necessary reference, as described in section 3.1: e.g., 'Source' $_{p}$ ( $i^{f}(p,q)$ , 'Cynthia'). Clearly, the deductive inference engine – the "non-logical" axioms, $\Delta$ – cannot exploit this new information in any way, but nothing prevents us from adding another inference engine in $L^{\uparrow}$ for reasoning about sources of information. To see the connection with model management (or at least with management of mathematical models, since the current examples are in fact discussing management of models, too: Logic models), recall the EOQ example in section 2. The mathematical equations constituting the EOQ model were represented algebraically. This language simply cannot express the qualitative information in the paragraph following the equations. In section 4, we will show how embedding techniques can be used to represent both the equations and the qualitative information of the EOQ example in a single embedding language, i.e., in a common $L^{\uparrow}$ .

A second benefit of employing embedded languages is closely related to the first benefit. With embedded languages it becomes straightforward to embed multiple, distinct $L_{\downarrow}$ languages in a common $L^{\uparrow}$ language. We might, for example, embed sentence logic, a language for mathematical modeling and a language for qualitative reasoning, all within a common $L^{\uparrow}$ . These multiple embedded languages may then be integrated with each other via expressions in $L^{\uparrow}$ . We have used two kinds of integration. First, expressions in one embedded language may refer to expressions in another embedded language. ‘Source’ $_{p}(i^{f}(p,q),$ ‘Cynthia’) is an example of this sort of integration. Second, expressions in one embedded language may be translated into expressions in another language. In TEFA we have, for example, a program that translates TEFA expressions into GAMS expressions, writes a file to record the result, which file can then be executed under GAMS. Also, we have developed a useful approach to model validation by writing a program for translating TEFA expressions into $T_{E}X$ , compiling the $T_{E}X$ file, presenting the model builder with the printed result, and asking: Is this the mathematical model you intended to put into the system? We note, but it goes without saying, that statements used to integrate two different languages simply cannot be made in either of the two languages. It is difficult to see how such linguistic integration could be done without an embedded languages approach.

The third category of benefit of the embedded languages approach is its natural fit with meta-level inferencing techniques, which have generated much excitement and shown great promise, e.g., [14,18,22,26]. Meta-level systems generalize the familiar inference-engine-and-knowledge-base architecture of standard expert systems. The following is a particularly clear statement of the concept of meta-level systems: “The essential characteristics of meta-level architectures is of course that they consists of two levels, the object-level and the meta-level. Each layer can be seen as an individual system with a representation language and an interpreter for expressions in that language. The purpose of the object level is to perform reasoning in the application domain of the system, while the goal of the meta level is to control the behavior of the object level” [18, pp. 14–15]. A number of advantages have been claimed in the literature for meta-level systems (e.g., [18, pp. 13–14]), including:

(1) great modularity, permitting easier and faster development and maintenance;

(2) ease with which particular domain knowledge can be used for multiple purposes;

(3) ease with which the system may produce explanations of its own behavior.

These are all benefits to which we would attest from our experience in developing TEFA. In addition, an impressive number of powerfully performing systems have been developed using meta-level architectures (e.g., see references in [14,18,22,26]).

In developing our concept of embedded languages and in implementing TEFA we were especially influenced by the impressive performance reported for PRESS [26], a PRolog Equation Solving System, which makes extensive use of meta-level inferencing. The following passage eloquently describes the flow of control (at the meta-level) for PRESS, and provides a strong intuitive sense for why such techniques work well, i.e., for why they can greatly reduce the search space: "We (...) use the term heuristic waterfall to describe the control flow of PRESS. The waterfall consists of a number of methods [object-level interpreters]. At the top of the waterfall, PRESS checks to see if the equation is already solved. If it is, PRESS returns the answer and the equation is removed from the waterfall. Otherwise, the equation is passed over the waterfall. On the way down, the PRESS methods try to transform the equation. If a method succeeds in transforming the equation, the new equation is sent to the top of the waterfall and the process is repeated. If a method such as change of unknown creates more than one equation, all such equations are sent to the top. If a method fails to transform the equation, the equation falls to the next level where the next method is tried. The process terminates with success when there are no more equations to be processed. If an equation falls right through the waterfall, i.e. no method can transform the equation, PRESS backtracks. (...) Finally, if all possibilities have been tried, and equations still remains in the waterfall, the process terminates with failure, i.e. PRESS fails to solve the equation.

“PRESS tries the methods in the order isolation, factorization, polynomial methods, change of unknown, collection, attraction, trigonometric methods, logarithmic methods, homogenization and nasty function methods” [26, pp. 29–30].

If meta-level architectures are good things, then how do embedded languages fit in and what do they contribute to building such systems? The fit is natural. Expressions in an $L_{\downarrow}$ language (recall our example of sentence logic) constitute, in effect, statements in an object-level knowledge base. In our sentence logic example, the “non-logical” axioms together constitute an object-level interpreter for expressions in the object-level knowledge base. As we saw, both the statements in the object-level knowledge base (the sentence logic axioms) an the statements in the object-level interpreter (the “non-logical” axioms) are embedded in the $L^{\uparrow}$ language. In effect, they become constituents of statements in a meta-level knowledge base, which statements are then interpreted by a meta-level interpreter. Thus, the correspondence between meta-level architectures and embedded languages is apt. What then does it do for us?

Given that we wish to work with a meta-level architecture, embedded languages offers us a principled, modular lingua franca, a way to generalize meta-level inference across multiple $L_{\downarrow}$ languages (e.g., statements in algebra and statements about algebraic models). Not only may meta-level inference be used to control the application of object-level interpreters, but the object-level knowledge bases may span multiple $(L_{\downarrow})$ languages. Thus, not only may we embed and use multiple $L_{\downarrow}$ languages in a common system (benefit category two, above), but we can also reason at the meta-level about the object-level interpreters (aka: Methods) for these disparate languages. All this works because the embedding effects a translation into the common $L^{\uparrow}$ language. In a sense we have our cake (one common language) and we eat it, too (we also have multiple, very different languages).

This concludes our detailed general discussion of the embedded languages idea. By focusing on a particularly simple example - embedding of sentence logic into an $L^{\uparrow}$ language - we have been able both to see in detail how the embedding works and to see broadly what the consequences and benefits of such an approach are. We shall now focus the discussion on illustrating how we have used embedded languages in the context of model management for equational models. Of the three categories of benefits we have discussed: (1) expression of knowledge about statements in an embedded language; (2) representation and use of multiple languages in a common system; and (3) facilitation and generalization of meta-level reasoning - what we say in the sequel will concentrate mainly on the first. The benefit of being able to represent both models and arbitrary information about models, and to do so in a principled and general way, is perhaps the most obviously useful benefit of embedded languages for model management. How that may be achieved (and is achieved in TEFA) is the main theme of what follows.

## 4. Model management

In this section we describe and discuss a fragment of our embedding language for model management. While we will not present the entire language here, the principles discussed apply as well to the portions of the language not discussed. (The languages discussed here are described in much detail in [1].) For the purposes of this section, $L_{\downarrow}^{*}$ , $L_{\downarrow}$ , and $L^{\uparrow}$ will denote the target, embedded, and embedding languages, respectively, specific to model management. We begin, in section 4.1, by describing our target language and clarifying our conceptual framework for modeling. Next, we present a generic EML (section 4.2), develop an embedding language for model management (section 4.3), and embed our generic EML in this embedding language (section 4.3.6). (Note: This embedding could as well have been done with a specific existing EML such as AMPL.) Finally, in section 4.4 we discuss certain advantages of this approach.

## 4.1. The target language for model management

Our target language is the natural and man-made language we use to represent, describe, and reason about models. It combines several kinds of representations, including sentences in a natural language (such as English), mathematical symbols, graphs, plots, diagrams, tables, and matrices, and employs several informal conventions. Since the target language is very complex and inherently semi-formal, we cannot hope to either describe or formalize it fully. Hence we will only discuss significant parts of it that are critical in developing a formal modeling language using the following example, drawn from $[3, 1]$ , to illustrate the representation of an optimization model in the target language.

Example 2. A steel production planning model Weekly production needs to be planned at a mill for two products, rolled steel and stainless steel, produced at the mill. The mill has two furnaces – one employs the conventional open hearth process, the other uses the basic oxygen furnace process. Each furnace can process a fixed amount of raw materials per day. Two types of coal, bituminous and brown coal, are the principal raw-materials, and are purchased at the mill. The purchase level of coal, and the amount of steel production that maximize the total profit have to be determined.

Given that the problem requires an optimal solution and assuming that the processes in the problem are linear, we have the following linear programming formulation:

\- furnace set of furnaces in the mill {open hearth, basic oxygen},

\- coal set of types of coal used as raw material {bituminous coal, brown coal};

\- steel set of types of steel produced {stainless steel, rolled steel};

\- $x_{i}$ amount of steel of type $i$ produced (tons), $i \in \text{steel}, x_{i} \geqslant 0$ ;

\- $u_{ij}$ utilization rate of furnace $j$ for steel type $i, j \in \text{furnace}, u_j > 0$ ;

\- $c_j$ capacity of furnace $j$ (tons/day), $j \in$ furnace, $c_j > 0$ ;

\- $a_{ik}$ utilization rate of coal type $k$ for steel type $i$ , $k \in coal$ , $i \in steel$ , $a_{ik} > 0$ ;

\- $p_k$ purchase level for coal type $k$ (tons), $k \in coal$ , $p_k \geqslant 0$ ;

\- pc $_{k}$ purchase cost of coal type k \$/ton), k ∈ coal, p $_{k}$ > 0;

\- $u_i$ unit-profit for steel type i (\$/ton), $i \in steel$ ;

• z total profit (\$).

Given $u_{ij}, c_j, a_{ik}, \mathrm{pc}_k, u_i$ , determine $x_i, p_k$ such that

$$
\begin{array}{l l} z \stackrel {{\text { def }}} {{=}} \max & \left[ \sum_ {i \in s t e e l} u _ {i} x _ {i} - \sum_ {k \in c o a l} p _ {k} \mathrm{pc} _ {k} \right]; \\ \text { s.t. } & \sum_ {i \in s t e e l} a _ {i k} x _ {i} \leqslant p _ {k} \quad \forall k, \\ & \sum_ {i \in s t e e l} u _ {i j} x _ {i} \leqslant c _ {j} \quad \forall j, \\ & x _ {i} \geqslant 0 \quad \forall i, \\ & p _ {k} \geqslant 0 \quad \forall k. \end{array}
$$

In a simple framework for modeling [25], and as the modeling example presented in section 2 suggests, model development can be viewed as the identification of the variables relevant to the model and a specification of the relationships between them and other modeling elements. From the example presented above we draw certain observations to extend this simple modeling framework. We note that modelers often use indexed variables (such as $a_{ik}$ ), by employing indices (such as i, j) that range over index sets (such as steel, coal). The indices are dummy in the sense that one may either change the index throughout the expression without affecting the semantics of the model, or use the same index to range over different sets in different expressions. The objective function and constraints are specified mathematically, using functional expressions and conditional expressions, respectively, that combine constants, mathematical variables, mathematical functions (that express mathematical relationships), and relations or predicates (that express qualitative relationships). By providing a formal representation for these model components, an EML aims to represent unambiguously some of the modeling information expressed less formally in the target language.

An executable modeling language aims to represent these features of the target language unambiguously, by providing a formal representation for the various components of a model.

4.2. An executable modeling language for model management

Recent research in modeling has led to the development of several executable modeling languages for model representation in modeling systems. These languages include AMPL [12], SML [17], and the languages in GAMS [7] and the $L_{\downarrow}$ portion of TEFA. In what follows, we describe a significant part of a generic executable modeling language $L_{\downarrow}$ in order to explain the embedding of this language in $L^{\uparrow}$ . We being by discussing the vocabulary and rules of formation for $L_{\downarrow}$ .² (In example 4, in appendix A, we illustrate $L_{\downarrow}$ by representing the steel production model of example 2 in $L_{\downarrow}$ , and we encourage readers unfamiliar with EMLs to examine the example.)

4.2.1. The symbols in $L_{\downarrow}$

\- $L_{\downarrow}$ has the following constant symbols:

(1) countably many individual constants: These include numbers, and other constants such as stainless-steel, brown-coal;

(2) countably many function constants: These include arithmetic operators $(+, -, *, /, \hat{)}$ , trignometric functions (e.g., sin, cos, atan), logarithmic functions (e.g., ln, exp), combinatorial functions (e.g., comb, perm), special functions (e.g., gamma, beta) and operators such as min, max, $\Sigma$ and $\Pi$ ;

(3) countably many relation constants: These include the equality and inequality relations (e.g., $\leqslant$ ), set operators (e.g., $\in$ ), and other predicates such as Divides, where Divides(x, y) is true if x divides y.

\- $L_{\downarrow}$ has a countable number of variable symbols, denoted by the letters $x, y, z, \ldots$

The language also contains the usual logical constants (which we denote by the symbols n, c, and d, as before), a universal quantifier (forall), as well as non-logical symbols ('','), and ';').

## 4.2.2. Well-formed expressions in $L_{\downarrow}$

Functional expressions in $L_{\downarrow}$ are arithmetic or symbolic mathematical expressions that result in a single value when evaluated in some scenario. For example, if x and y are variables, having values 10 and 15 in a particular scenario, respectively, then the functional expression $x + y$ will evaluate to 25 in that scenario. The class of functional expressions allowed in $L_{\downarrow}$ is defined recursively below:

(1) All constants and variables are functional expressions.

(2) If $\phi$ and $\psi$ are functional expressions, and if $\rho$ is a conditional expression (see below), then the following are functional expressions:

(a) $+\phi, -\phi, \phi + \psi, \phi - \psi, \phi * \psi, \phi / \psi,$ $\phi^{\wedge}\psi;$

(b) If $F$ is a function constant in $L_{\downarrow}$ , of arity $n$ , and if $\phi_1, \ldots, \phi_n$ are functional expressions, then so is $F(\phi_1, \ldots, \phi_n)$ . For example, an expression of the form $\mathbf{Sin}(\phi)$ is an $L_{\downarrow}$ functional expression, whenever $\phi$ is; (c) $\Sigma(\alpha \in \Delta, \phi)$ (a similar rule holds for $\Pi$ ), where $\alpha$ is a dummy index occurring in $\phi$ , and $\Delta$ is a set; the expression denotes the summation of $\phi$ with $\alpha$ ranging over this set;

(d) $\min(x_{s}, \phi)$ and $\min(x_{s}, \phi | \rho)$ (a similar rule holds for max), where $x_{s}$ is a list of variables that the expression $\phi$ is to be optimized over, subject to constraints $\rho$ , if any.

A conditional expression describes a testable condition, and is a generalization of the constraints that occur in a mathematical program. A conditional expression can be tested for being true or false in a given scenario after instantiating the free variables in the expression with their values in that scenario. For example, the conditional expression x > y is false in a scenario in which x and y have values 10 and 15, respectively. The class of conditional expressions allowed in $L_{\downarrow}$ is defined recursively below.

If $\phi$ and $\psi$ are functional expressions, and if $\rho$ and $\delta$ are conditional expressions, then the following are conditional expressions:

(1) $\phi = \psi, \phi > \psi, \phi \geqslant \psi, \phi < \psi, \phi \leqslant \psi;$

(2) $\phi \in \Delta, \Delta \subset \Gamma, \Delta \supset \Gamma, \Delta \subseteq \Gamma, \Delta \supseteq \Gamma$ , where $\Delta, \Gamma$ are sets or set expressions;

(3) if R is a relation constant in $L_{\downarrow}$ , of arity n, and if $\phi_{1},\ldots,\phi_{n}$ are functional expressions, then $R(\phi_{1},\ldots,\phi_{n})$ is a conditional expression. For example, expressions of the form $\text{integer}(\phi)$ , or $\text{divides}(\phi,\psi)$ , are conditional expressions if $\phi$ and $\psi$ are functional expressions;

(4) $n(\rho), c(\rho, \delta), d(\rho, \delta)$ ;

(5) forall $(\alpha \in \Delta, \rho)$ , where $\alpha$ is a dummy index occurring in $\rho$ and $\Delta$ is a set or set expression.

A definitional expression defines a variable in terms of others, and the definition holds in all scenarios. For example, $y = x^{2}$ defines y, in any scenario, as the square of the value of x in that scenario. In general, if $\phi$ is a functional expression, $\rho$ is a conditional expression and Y is a modeling variable, then $Y = \phi$ is a definitional expression.

4.3. The embedding language for model management

Now we explain how the embedded languages technique is operationalized in the case of model management. $L^{\uparrow}$ , our embedding model management language, is an FOL language used to specify and manipulate sublanguages, chiefly the $L_{\downarrow}$ executable modeling language discussed above. We will discuss a vocabulary and rules of formation for this language, and explain the embedding in terms of the triple $\langle S, F, \Delta \rangle$ . In particular, we will require that for all expressions $\phi$ in $L_{\downarrow}$ , $\mathcal{I}(\phi)$ be a term in $L^{\uparrow}$ , and for all such $\phi$ that are formulas in $L_{\downarrow}$ , $\mathcal{F}(\mathcal{I}(\phi))$ be a formula in $L^{\uparrow}$ . We being by defining the vocabulary of $L^{\uparrow}$ . (At various points in this section, the reader may find it useful to turn to example 5 in the appendix, where we illustrate $L^{\uparrow}$ by representing the steel production planning model of example 4 in $L^{\uparrow}$ .)

## 4.3.1. Individual constants, $\mathcal{C}$

With a view towards embedding $L_{\downarrow}$ in $L^{\uparrow}$ , we seek to treat models, variables, and other modeling elements as constants in $L^{\uparrow}$ . Let $\Lambda$ , $\Delta_{M}$ , and $\Delta_{S}$ denote the sets of sets, models, and scenarios, respectively, that occur in the modeling domain. Further, let $\Delta C$ , $\Delta_{F}$ , $\Delta_{R}$ and $\Delta_{V}$ denote respectively, the sets of individual constants, function constants, relation constants, and variables in $L_{\downarrow}$ . Then we require that the set of $L^{\uparrow}$ constants

$$
\mathscr {C} \supset \Delta_ {C} \cup \Delta_ {R} \cup \Delta_ {F} \cup \Delta_ {V} \cup \Delta_ {M} \cup \Delta_ {S} \cup \Lambda
$$

and that for all elements x of these sets, $\mathcal{S}(\phi) = \phi$ . (This pun, noted in section 3.1, is useful but hardly required for the method.) Examples include: 18.71, $+\downarrow$ , sum, $= _{\downarrow}$ , $x_{i}$ , steel, steel-production-planning. Note that we now write $+ _{\downarrow}$ to distinguish the symbol for addition in $L_{\downarrow}$ from the function constant + in $L^{\uparrow}$ , to which it is related by rules of translation. However, for the sake of readability we will not do the same for other symbols. (Strictly speaking, the two symbols are distinct, but they have the same interpretation in the domain of discourse, $L^{*}_{\downarrow}$ . The rules of translation ensure the correctness of the inferences made in $L^{\uparrow}$ with respect to $L_{\downarrow}$ and $L^{*}_{\downarrow}$ .) This scheme allows us to predicate (using $L^{\uparrow}$ relation constants, to be discussed below) arbitrary information, in $L^{\uparrow}$ , about any of these modeling elements. For example, we could predicate information about the computational complexity of a matrix inversion function used in $L_{\downarrow}$ .

## 4.3.2. Function constants, $\mathcal{H}$

We will construct the set $\mathcal{H}$ in a manner that facilitates the embedding of $L_{\downarrow}$ in $L^{\uparrow}$ . We require $\mathcal{H}$ to have at least the following kinds of elements. One, it must contain function constants corresponding to the mathematical functions in $L_{\downarrow}$ , such as for arithmetic operators and trigonometric functions. For example, there is an addition function $+\uparrow$ corresponding to the addition function in $L_{\downarrow}$ . (In what follows however, we will omit the superscript for the sake of simplicity of notation, unless there is scope for confusion.) In general, for every $n$ -ary function constant $f_{\downarrow}$ in $L_{\downarrow}$ , there is an $n$ -ary function constant $f^{\uparrow}$ in $L^{\uparrow}$ , such that

$$
\mathcal {I} \left(f _ {\downarrow} \left(\phi_ {1}, \dots , \phi_ {n}\right)\right) = f ^ {\uparrow} \left(\mathcal {I} \left(\phi_ {1}\right), \dots , \mathcal {I} \left(\phi_ {n}\right)\right),\tag{5}
$$

is a term in $L^{\uparrow}$ , for all terms $\phi_{i}$ in $L_{\downarrow}$ .

Second, since we require that there be well-formed terms in $L^{\uparrow}$ corresponding to well-formed formulas in $L_{\downarrow}$ , H must contain elements n, c, d, for all which are the logical constants in $L_{\downarrow}$ . We will require that for all formulas $\phi$ and $\psi$ in $L_{\downarrow}$ ,

$$
\mathcal {I} (n (\phi)) = n (\mathcal {I} (\phi)),\tag{6}
$$

$$
\mathcal {I} \big (c (\phi , \psi) \big) = c \big (\mathcal {I} (\phi), \mathcal {I} (\psi) \big),\tag{7}
$$

$$
\mathcal {I} \big (d (\phi , \psi) \big) = d \big (\mathcal {I} (\phi), \mathcal {I} (\psi) \big),\tag{8}
$$

$$
\mathcal {I} (f o r a l l (x, \psi)) = f o r a l l (\mathcal {I} (x), \mathcal {I} (\psi)),\tag{9}
$$

so that the right-hand side expressions are terms in $L^{\uparrow}$ .

Third, also from our requirement that there be well-formed terms in $L^{\uparrow}$ corresponding to well-formed formulas in $L_{\downarrow}$ , it follows that H must contain functions corresponding to the relation constants in $L_{\downarrow}$ . For example, the wff x > y in $L_{\downarrow}$ would be mapped to a term $\mathcal{I}(x) > ^{\uparrow}(y)$ in $L^{\uparrow}$ . In general, for every n-ary relation constant $r_{\downarrow}$ in $L_{\downarrow}$ , there is an n-ary function constant $r^{\uparrow}$ in $L^{\uparrow}$ , such that

$$
\mathcal {I} \left(r _ {\downarrow} \left(\phi_ {1}, \dots , \phi_ {n}\right)\right) = r ^ {\uparrow} \left(\mathcal {I} \left(\phi_ {1}\right), \dots , \mathcal {I} \left(\phi_ {n}\right)\right),\tag{10}
$$

is a term in $L^{\uparrow}$ , for all terms $\phi_{i}$ in $L_{\downarrow}$ .

Fourth, since $L^{\uparrow}$ is our language for model management, it must contain model management functions (see section 2) such as evaluate, formulate, and describe. The role of these functions will be clear when we discuss the axiom set $\Delta$ .

Thus, essential for our purposes is that $\mathcal{H}$ include at least the following function constants: $\bullet +, -, *, /, ^{\wedge}$ , sqrt, sin, tan, ln, gamma, comb, max, sum;

• n, c, d, forall, exists, ← ;

$>\uparrow, <\uparrow, =\uparrow, \leqslant\uparrow, \geqslant\uparrow, in, contains;$

\- evaluate, formulate, describe, select, integrate, evaluate, explain, analyze.

## 4.3.3. Relation Constants, $\mathcal{R}$

We stated above that we seek to treat models, variables, and other modeling elements as constants in $L^{\uparrow}$ . That some constant X in $L^{\uparrow}$ is to be interpreted as a variable (or as a constant or model, etc.) in $L_{\downarrow}$ , is declared by making assertions in $L^{\uparrow}$ of the form $\text{variable}(x)$ . Thus the set R must contain predicates such as constant, variable, and model that allow us to distinguish among constants in $L^{\uparrow}$ . Next, it also must contain predicates to represent $L_{\downarrow}$ formulas such as conditional expressions that are in $L_{\downarrow}$ . In other words, for any wff $\phi$ in $L_{\downarrow}$ , there is a predicate p that is used to embed the $L^{\uparrow}$ term, $\mathcal{I}(\phi)$ , corresponding to $\phi$ , such that

$$
\mathcal {F} (\mathcal {I} (\phi)) = p \big (\mathcal {I} (\phi , \Psi) \big),\tag{11}
$$

is a formula in $L^{\uparrow}$ , where $p(\mathcal{I}(\phi, \Psi))$ denotes a predicate one of whose arguments is $\mathcal{I}(\phi)$ , and $\Psi$ is additional information (not confined to a single argument) related to $\phi$ in $L_{\downarrow}^{*}$ . (Recall the $S(\psi, \text{'sentence-logic'})$ example in section 3.1.) For example, the $L_{\downarrow}$ wff $q^{*} = \sqrt{(2ad)/h}$ (expression 4 in the EOQ model, example 1) is embedded in the $L^{\uparrow}$ predicate defE as shown below.

\- defE(eoq, 1.4, 'The optimal order quantity as a function of $a$ , $d$ , and $h$ :',

$$
\operatorname{opt} (q) \stackrel {\text { def }} {=} \operatorname{sqrt} (2 * a * d / h)).
$$

Similarly, $L^{\uparrow}$ must also must contain predicates to represent some of the qualitative information (such as the assumptions, or source, of a model) expressed in $L_{\downarrow}^{*}$ (which is not captured in $L_{\downarrow}$ ). For example, the assumption in example 1 that “demand is deterministic and known, the holding cost is linear, the setup cost is constant, and there is no lead time” is embedded in the $L^{\uparrow}$ predicate assume as shown below.

\- assume(eoq, 'Known demand, lead time = 0, da/dq = 0,

$\mathrm{d}^2 H(Q) / \mathrm{d}Q^2 = 0$ ( $H$ is holding cost,

$Q$ is quantity in stock)')

Finally, $L^{\uparrow}$ must contain predicates for arithmetic comparisons and set-containment operations. Hence R includes at least the following predicates (for our present purpose – that of explaining the embedding – it is not necessary to explain the precise interpretation of these predicates or to discuss the other predicates in $L^{\uparrow}$ ):

\- constant, function, relation, variable, set, model, scenario,

\- defE, conE, funE, funDef, setDef, datum;

\- modelSource, units-of-measurement, assume, quiddity;

\- Integer, binary, positive;

$$
= , <  , >, \geqslant , \leqslant , \in , \subset , \supset , \subseteq , \supseteq .
$$

## 4.3.4. Terms in $L^{\uparrow}$

A well-formed term in $L^{\uparrow}$ is defined recursively to include the following:

(1) Any individual constant (any element of $\mathcal{C}$ ) or a variable is a term;

(2) if $\rho$ is a function constant of arity n, then $\rho(\tau_{1},\ldots,\tau_{n})$ is a term iff all of $\tau_{1},\ldots,\tau_{n}$ are terms.

These, of course, are the rules of formation for terms in a standard FOL language (see section 3.1). Due to our choice of symbols in the sets C and H, they ensure that all terms and formulas of $L_{\downarrow}$ are interpretable in $L^{\uparrow}$ (i.e., there images are terms in $L^{\uparrow}$ ). However, since $L^{\uparrow}$ is to be a specialized language for model management, not all terms obtained by these rules will be meaningful for our purposes. In particular, not all terms of $L^{\uparrow}$ will have any interpretation in $L_{\downarrow}$ . We isolate such terms with axioms, which we state in section 4.3.7, that define the class of terms that are well-formed in $L_{\downarrow}$ .

## 4.3.5. Well-formed formulas in $L^{\uparrow}$

A well-formed formula in $L^{\uparrow}$ is defined recursively to include the following:

(1) if $\rho$ is a relation constant $(\rho \in \mathcal{R})$ of arity $n$ , then $\rho(\tau_1, \ldots, \tau_n)$ is a wff iff all of $\tau_1, \ldots, \tau_n$ are terms;

(2) if $\phi$ and $\psi$ are wffs then so are: $\neg \phi$ , $\phi \wedge \psi$ , $\phi \to \psi$ ;

(3) if $\phi$ is a wff then so is $(\forall \nu \phi)$ , where $\nu$ is a variable.

For example, the relation constant defE is used as follows. If, in $L_{\downarrow}$ , there is a definitional expression $\phi$ in a model M, then $L^{\uparrow}$ has the wff, defE(M, Exp-Id, Description, $\phi$ ), which asserts and embeds the $L_{\downarrow}$ thesis, that the model M has a definitional expression $\phi$ identified with Exp-Id and described with Description. Given our choice of symbols in $L^{\uparrow}$ , and the definitions of S and F, it is easy to verify that every formula $\phi$ in $L_{\downarrow}$ can be embedded in an appropriate predicate in $L^{\uparrow}$ .

4.3.6. Embedding an $L_{\downarrow}$ executable modeling language in $L^{\uparrow}$

Does our specification on $L^{\uparrow}$ meet the requirements for an embedding, i.e., does $L^{\uparrow}$ embed our executable modeling language $L_{\downarrow}$ ? It is easy to verify that, given our construction of $L^{\uparrow}$ , the image function (S) and the translation function (F) are, taken together, able to transform any wff in $L_{\downarrow}$ into a wff in $L^{\uparrow}$ . Given the vocabulary and rules of formation for $L^{\uparrow}$ , the images of all $L_{\downarrow}$ terms and formulas are terms in $L^{\uparrow}$ , and all $L_{\downarrow}$ formulas can be embedded in a suitable $L^{\uparrow}$ formula. It remains for us to discuss the axiom set $\Delta$ and to show that our construction of $L^{\uparrow}$ is such that all the inferences that can be made in $L_{\downarrow}$ can be made in $L^{\uparrow}$ as well. Although we will not offer a complete treatment of these two issues here, we will illustrate them by using the evaluation operation, and by applying it to our EOQ model of example 1.

First, we define two $L^{\uparrow}$ predicates mentioned earlier: datum, and calls. The formula $\text{datum}(y, s, \alpha)$ states that the value of the variable y in scenario s is exogenously specified to be $\alpha$ . Similarly, $\text{calls}(m_{1}, y_{1}, m_{2}, y_{2})$ means that the variable $y_{1}$ in model $m_{1}$ evaluates to the value of the variable $y_{2}$ computed using model $m_{2}$ . (For example, in the EOQ model, the demand d may be obtained by specifying it as the output of one of several demand forecasting models.)

Second, let us examine some axioms that specify a simple model selection function (given a set declarations made by the modeler). Given a variable y in a model m the function select(m, y) returns a pair $(m', \phi)$ such that model $m'$ is called to evaluate the expression $\phi$ when y is to evaluated using the model m. Two axioms that constitute of the definition of this function are:

$$
\begin{array}{l}\forall m \forall y \forall \phi \left(d e f E (m, *, *, y \stackrel {{\text { def }}} {{=}} \phi) \right.\\\rightarrow s e l e c t (m, y) = (m, \phi)\left. \right),\end{array}\tag{12}
$$

$$
\begin{array}{r l}&{\forall m \forall y \forall m ^ {\prime} \forall y ^ {\prime} \forall m ^ {\prime \prime} \forall y ^ {\prime \prime}}\\&{\qquad \times (c a l l s (m, y, m ^ {\prime}, y ^ {\prime}) \wedge s e l e c t (m ^ {\prime}, y ^ {\prime})}\\&{\qquad = (m ^ {\prime \prime}, \phi) \rightarrow (s e l e c t (m, y)}\\&{\qquad \qquad = (m ^ {\prime \prime}, \phi)).}\end{array}\tag{13}
$$

Third, let us examine a small subset of the axioms corresponding to the evaluate function. (evalute(y, m, s) = $\alpha$ means that the value of the variable y in scenario s evaluated using the model m is $\alpha$ .) The ones we need to illustrate our point are the following. $^{3}$

$$
\forall m \forall y \forall m ^ {\prime} \forall y ^ {\prime} \forall s
$$

$$
\begin{array}{r l}\times (\text { variable } (y) \wedge (\text { select } (m, y) = (m ^ {\prime}, \phi))\\&\rightarrow (\text { evaluate } (y, m, s)\\&= \text { evaluate } (\phi , m ^ {\prime}, s))),\end{array}\tag {1}\tag{14}
$$

$$
\begin{array}{r l} \forall m \forall \phi \forall s & \left(e v a l u a t e (\sqrt {\phi}, m, s) \right. \\ & = \sqrt {e v a l u a t e (\phi , m , s)}), \end{array}\tag{15}
$$

$$
\begin{array}{l} \forall m \forall \phi \forall \psi \forall s (e v a l u a t e (\phi * \psi , m, s) \\ = e v a l u a t e (\phi , m, s) * e v a l u a t e (\psi , m, s)), \end{array}\tag{16}
$$

$$
\begin{array}{l} \forall m \forall \phi \forall \psi \forall s (e v a l u a t e (\phi / \psi , m, s) \\ = e v a l u a t e (\phi , m, s) / e v a l u a t e (\psi , m, s)), \end{array}\tag{17}
$$

$$
\begin{array}{l}\forall m \forall y \forall \alpha \forall s d a t u m (y, s, \alpha)\\\rightarrow (e v a l u a t e (y, m, s) = \alpha).\end{array}\tag{18}
$$

Fourth, consider the following set of $L_{\downarrow}$ statements about the EOQ model, and about data in some scenario-call it k.

$$
\bullet \quad \{\mathrm{q} ^ {*} = \sqrt {2 a d / h}, \mathrm{a} = 5, \mathrm{d} = 1 2 0, \mathrm{h} = 1 2 \}.
$$

Denote the collection of these sentences by $\Gamma_{\downarrow}$ . It follows, using the standard laws of evaluation pertaining to an EML, that in the given scenario, $q^{*}$ evaluates to 10, i.e.,

$$
\Gamma_ {\downarrow} \vdash (q ^ {*} = 1 0).\tag{19}
$$

Fifth, consider the set $\Gamma^{\uparrow} (= \mathcal{F}(\mathcal{I}(\Gamma_{\downarrow})))$ of the embedding statements in $\mathrm{L}^{\uparrow}$ corresponding to the statements in $\Gamma_{\downarrow}$ . It contains the following formulas:

$$
\operatorname{def} E \left(e o q, 1. 4, ^ {\prime} \text { Optimal   order } \dots^ {\prime}, \operatorname{opt} (q) \right.
$$

$$
\stackrel {\text { def }} {=} \operatorname{sqrt} (2 * a * d / h)),\tag{20}
$$

$$
d a t u m (a, k, 5),\tag{21}
$$

$$
\operatorname{datum} (d, k, 1 2 0),\tag{22}
$$

$$
\operatorname{datum} (h, k, 1 2),\tag{23}
$$

$$
\text { scenario } (k).\tag{24}
$$

Now, in $L^{\uparrow}$ , we must be able to prove the equivalent of the statement that “ $q^{*}$ evaluates to 10 in scenario k using the EOQ model”, i.e., we require that

$$
\{\Delta , \Gamma^ {\uparrow} \} \vdash (e v a l u a t e (o p t (q), e o q, k) = 1 0).\tag{25}
$$

It is easy to see that that is indeed the case. Axiom 18 and formulas 21, 22, and 23, respectively imply that

evaluate(a, eoq, k) = 5,

evaluate(d, eoq, k) = 120,

evaluate(h, eoq, k) = 12.

Axiom 12 and formula 20 imply that

$$
\operatorname{select} (e o q, \operatorname{opt} (q)) = (e o q, \operatorname{sqrt} (2 * a * d / h)),\tag{26}
$$

which combined with axiom 14 implies that

$$
e v a l u a t e (o p t (q), e o q, k)
$$

$$
= \text { evaluate } (s q r t (2 * a * d / h), e o q, k),\tag{27}
$$

and a recursive application of axioms 15, 16 and 17 results in the desired conclusion.

4.3.7. Formalizing rules of formation for $L_{\downarrow}$ expressions

We now illustrate how $L^{\uparrow}$ formalizes the met-alanguage for $L_{\downarrow}$ (the language used to describe $L_{\downarrow}$ in section 4.2.2) via axioms that formally state the rules of formation for $L_{\downarrow}$ functional expressions, conditional expressions, and definitional expressions, in that order. Again, it is sufficient for this purpose to state only an illustrative subset of these axioms. The rules of formation state below have another purpose – they are the rules for checking validity of $L_{\downarrow}$ expressions. This illustrates one benefit of using the embedded languages technique, namely the ability to ensure valid formation of expressions that declare modeling knowledge within the language itself. We use the following notation to denote if an expression is a functional expression, or a conditional expression, or a definitional expression:

$$
\bullet \text { funE } (\phi) \equiv \phi \text {   is   a   functional   expression   in   } L _ {\downarrow};
$$

$$
\bullet \operatorname{conE} (\phi) \equiv \phi \text {   is   a   conditional   expression   in   } L _ {\downarrow};
$$

$$
\bullet \quad \operatorname{defE} (\phi) \equiv \phi \text {   is   a   definitional   expression   in   } L _ {\downarrow}.
$$

We begin with axioms that formalize the rules of formation for functional expressions in $L_{\downarrow}$ . For the most part (e.g., for trignometric functions), we will state only some of the axioms since the rest follow quite similarly.

$$
\forall X \quad (X \in \Delta_ {C} \rightarrow f u n E (X)),
$$

$$
\forall X \quad (X \in \Delta_ {V} \rightarrow f u n E (X)).
$$

These axioms correspond to part (1) of the definition of functional expressions in section 4.2.2.

$$
\forall \phi \quad (f u n E (\phi) \rightarrow f u n E (+ \phi)),
$$

$$
\forall \phi \quad (f u n E (\phi) \rightarrow f u n E (- \phi)),
$$

$$
\forall \phi \forall \psi \quad (f u n E (\phi) \wedge f u n E (\psi) \rightarrow f u n E (\phi + \psi)),
$$

$$
\forall \phi \forall \psi (f u n E (\phi) \wedge f u n E (\psi) \rightarrow f u n E (\phi - \psi)),
$$

$$
\forall \phi \forall \psi \quad (f u n E (\phi) \wedge f u n E (\psi) \rightarrow f u n E (\phi * \psi)),
$$

$$
\forall \phi \forall \psi \quad (f u n E (\phi) \wedge f u n E (\psi) \rightarrow f u n E (\phi / \psi)),
$$

$$
\forall \phi \forall \psi \quad (f u n E (\phi) \wedge f u n E (\psi) \rightarrow f u n E (\phi^ {\wedge} \psi)).
$$

These axioms correspond to part 2(a) of the definition of functional expressions in section 4.2.2.

$$
\forall \phi \quad (f u n E (\phi) \rightarrow f u n E (S q r t (\phi))),
$$

$$
\forall \phi \quad (f u n E (\phi) \rightarrow f u n E (l n (\phi))),
$$

$$
\forall \phi \quad (f u n E (\phi) \rightarrow f u n E (E x p (\phi))),
$$

$$
\forall \phi \quad (f u n E (\phi) \rightarrow f u n E (S i n (\phi))),
$$

$$
\forall \phi \quad (f u n E (\phi) \rightarrow f u n E (G a m m a (\phi))).
$$

These axioms correspond to a subset of the functions mentioned in part 2(b) of the definition of functional expressions in section 4.2.2.

$$
\begin{array}{r l}\forall \phi \forall X \forall S&(f u n E (\phi) \wedge i n d e x (X) \wedge s e t E (S)\\&\rightarrow f u n E (\Sigma (X \in S, \phi))),\end{array}
$$

$$
\begin{array}{r l}\forall X s \forall \phi \forall \rho&(i n d e x l i s t (X s) \wedge f u n E (\phi) \wedge c o n E (\rho)\\&\rightarrow f u n E (M a x (X s, \phi | \rho))).\end{array}
$$

These axioms correspond to parts 2(c) and 2(d) of the definition of functional expressions in section 4.2.2.

Finally, we formalize some of the rules of formation for conditional expressions and definitional expressions in $L_{\downarrow}$ , stated in section 4.2.2, with the following axioms.

$$
\begin{array}{l l l} \forall \phi \forall \psi & (f u n E (\phi) \wedge f u n E (\psi) & \to c o n E (\phi = \psi)), \\ \forall \phi \forall \psi & (f u n E (\phi) \wedge f u n E (\psi) & \to c o n E (\phi <   \psi)), \\ \forall \phi \forall \Delta & (f u n E (\phi) \wedge s e t E (\Delta) & \to c o n E (\phi \in \Delta)), \\ \forall \Gamma \forall \Delta & (s e t E (\Gamma) \wedge s e t E (\Delta) & \to c o n E (\Gamma \subset \Delta)), \\ \forall \phi & (f u n E (\phi) & \to c o n E (i n t e g e r \\ & & (\phi))), \\ \forall \rho & (c o n E (\rho) & \to c o n E (n (\phi))), \\ \forall \alpha , \forall \Gamma , \forall \phi & (\alpha \in \Delta \wedge s e t E (\Gamma) \wedge f u n E (\phi) & \to c o n E (f o r a l l \\ & & (\alpha \in \Delta , \phi))), \\ \forall Y \forall \phi & Y \in \Delta_ {V} \wedge (f u n E (\phi) & \to d e f E (Y = \stackrel {{\text {def}}} {{=}} \phi)) \Big) \end{array}
$$

These axioms illustrate how the metalanguage for any $L_{\downarrow}$ language may be formalized in the embedding language, $L^{\uparrow}$ . We turn now to discuss the significance of the embedded languages technique.

## 4.4. Discussion

We have sketched how the embedded languages technique is applied to model management. Recalling the three categories of benefits of embedding languages (cf. section 3.2), the specific advantages that we have demonstrated for model management are the following:

(1) embedded languages allows us to represent in a rigorous, and completely flexible and general manner, a rich variety of qualitative knowledge about models (that is, the first category of benefit is realized);

(2) this knowledge can be used in defining materially useful inferences, e.g., as in the case of the unique names violation problem (this is a specific case of the first category of benefit);

(3) embedded languages allows us to represent rules of formation of expressions in the modeling language, and to examine the validity of model declarations (again, this is a case of exploiting information about models, information that cannot be expressed in, e.g., algebra);

(4) multiple languages - distinct but related - can be embedded and effectively integrated within $L^{\uparrow}$ . These languages may be used (benefit category 2) and their interpreters reasoned about (benefit category 3) in $L^{\uparrow}$ .

Recall now the EOQ example (example 1) for illustrating the points made in this section, in particular the relationship between $L^{\uparrow}$ and $L_{\downarrow}$ . From the embedded languages point of view, information about this model was described in $L_{\downarrow}^{*}$ , which is the semi-formal target language that we need to model with the embedding. In representing this model using the embedded languages approach, we require that the $L_{\downarrow}$ expressions that we obtain for it be terms in $L^{\uparrow}$ . Further, we must not only express the mathematical structure of the model, but the qualitative information in the accompanying paragraph, such as the dimensions of the variables in the model, as well. We do so with predicates such as the defE predicate in $L^{\uparrow}$ , by using the model name eoq as the referring expression and predicating information about it. Finally, we also need to have knowledge about the valid formulation conditions for these expressions, but those are already available in $L^{\uparrow}$ .

## Example 3. The EOQ model, in $L^{\uparrow}$

\- model(eoq, ‘This is the simple lot size EOQ model...’)

\- objective(eoq, ‘Determine reorder quantities and reorder points for a single item, minimizing total costs and ensuring sufficient inventory to meet the demand for the item.’)

\- assume(eoq, ‘Known demand, lead time = 0, $d_{a}/d_{q} = 0$ , $\mathrm{d}^{2}H(Q)/\mathrm{d}Q^{2} = 0$ (H is holding cost, Q is quantity in stock)’)

\- defE(eoq, 1.1, 'Total cost is …', $TC^{def} = (a * d / q) + h * q_{ave}$ )

\- defE(eoq, 1.2, ‘Optimal cost is …’, opt(TC) $^{def}$ = min(q, TC))

\- defE(eoq, 1.3, 'Number of orders is …', $n \stackrel{\text{def}}{=} d/q$ )

\- defE(eoq, 1.4, 'Optimal reorder quantity is ...', opt(q) = sqrt(2 \* a \* d/h))

• variable(q, 'Reorder quantity.')

\- variable( $q_{ave}$ , 'Average inventory.')

\- variable(n, 'Number of orders placed in each period.')

\- variable(a, 'Setup cost for each order.')

• variable(h, 'Unit holding cost.')

\- variable(d, 'Total demand for the period.')

• variable(TC, 'Total cost.')

\- quiddity(q, item-units/ period, amount(reorder(item)))

\- quiddity( $q_{ave}$ , item-units, average(quantity (item))

We have the following interpretations for the above statements. In $L^{\uparrow}$ , we have the predicate $defE \in \mathcal{R}$ , and constant symbols $eoq \in \mathcal{C}$ , $q \in \mathcal{C}$ , $a \in \mathcal{C}$ , etc. For the same symbols (except $defE$ ) in $L_{\downarrow}$ we have $sqrt \in \Delta_F$ , $eoq \in \Delta_M$ , $q \in \Delta_V$ , $a \in \Delta_V$ . If we now wish to add additional information, such as the source of the model, we can do so by creating an appropriate relation in $L_{\downarrow}$ using the predicate symbol relation in $L^{\uparrow}$ , and b) asserting this information as a formula in $L_{\downarrow}$ .

\- relation(modelSource,[model,source])

\- $L_{\downarrow}$ (modelSource(eoq, 'Analysis of Inventory Systems, G. Hadley and T. Whitin'))

We note that we could have directly expressed this information as an $L^{\uparrow}$ formula (by including the predicate modelSource in R in $L^{\uparrow}$ ), moving directly from $L_{\downarrow}^{*}$ to $L^{\uparrow}$ , saving us the cost of transformation from $L_{\downarrow}$ to $L^{\uparrow}$ . However, such a strategy requires us to know in advance all the predicates that the set R must contain. By using the predicate relation we are able to enrich $L_{\downarrow}$ so that it can represent any new kinds of information that may be expressed in our semi-formal target language.

## 5. Conclusion

We have sought to introduce the concept of, motivation for, principles of, and chief benefits of embedded languages, especially as applied to model management. Further, we have illustrated the employment of the concept for sentence logic models, for algebraic models, and for languages that describe expressions in these two sorts of models.

In addition to the general advantages of the embedded languages approach, discussed mainly in section 3.2 and section 4.4, we want to make the following high-level observations about the approach.

(1) Our fundamental strategy in designing, building, and fielding TEFA has been to develop a general architecture for model management, one that is strong with regard to expressive power, flexibility, and functionality. Our strategy has not been the conventional one of attempting to determine, once and for all, the requirements for a model management system and then to implement them using a well-suited architecture. Instead, we have sought to develop an architectural approach that supports known requirements and that can, in a principled and systematic fashion, accommodate new features and functionality as they become requirements. In brief, an embedding language is not just another EML; rather one should think of it as an executable language for making more effective use of other executable modeling languages.

(2) The embedded languages approach is well-suited to encourage the use of multiple modeling languages within a common modeling system, including and model management languages developed independently of our particular implementation. Such modeling languages are – from the point of view of our embedding language, $L^{\uparrow}$ – simply particular $L_{\downarrow}$ languages, which may be exploited once embedding translators (to and from $L^{\uparrow}$ ) are written. Although we have not presented an example of this in the present paper, we hope it is obvious to the reader (as it is to us) that doing this is a comparatively straightforward task. We are happy to note that this exercise has been carried out for a logic-based language for structured modeling [10], and we hope to see other such examples in the future.

(3) The embedded languages approach can improve the usefulness of existing modeling languages (particular $L_{\downarrow}$ languages) in at least two ways. First, we can express information in $L^{\uparrow}$ about particular $L_{\downarrow}$ languages and expressions in them, information that cannot be easily expressed in the particular $L_{\downarrow}$ languages themselves. This holds even when the embedded language can, e.g., express both a mathematical model and certain information about the model. It is, for example, straightforward to say in $L^{\uparrow}$ what the expressive limitations are of the $L_{\downarrow}$ language in question, while this would not be possible in the $L_{\downarrow}$ language itself. Second, by facilitating the integration of multiple $(L_{\downarrow})$ specialized modeling languages, as noted above, the embedded languages approach can improve the usefulness of the individual languages. For example, using embedded languages would facilitate the development of a model that combined a mathematical programming model (represented in a mathematical programming language) with a queueing model (represented in a queueing-theoretic language) whose output values serve as the parameter values for the mathematical programming model.

(4) The embedded languages approach does nothing to alter the computational, mathematical, expressive, or semantic properties of an embedded language. Nor does the approach provide material help in designing and developing particular $L_{\downarrow}$ modeling languages. The virtues of the embedded languages method lie elsewhere, as discussed above.

Having surfaced the idea and demonstrated its plausibility, much remains to be done by way of exploring and exploiting the concept of embedded languages for model management. Computational costs need to be examined. Meta-level control techniques in the face of undecidability need investigation. Principles of efficient translation between useful modeling languages, say AMPL and SML, would bear investigation. Principles of integrating modeling languages and systems, say GAMS and Macsyma, focused on different sorts of models are well worth looking in to.

There is much more. We believe that we have only begun to understand what can be done with this technique. Furthering that understanding is something we aim to pursue. We hope others will as well.

## Appendix A: Examples

Example A.1. Steel production planning model, in $L_{\downarrow}$

## SETS

set furnace = {open-hearth, basic-oxgen}; A set of furnaces

set steel = {stainless-steel, rolled-steel}; Types of steel produced at the mill

set coal = {bituminous-coal, brown-coal};
Types of coal used as raw material

VARIABLES

$x_{i}$ : $i \in steel x_{i} \geqslant 0$ ; amount of steel of type i produced (tons)

$u_{[i,j]}$ : $j \in furnace$ , $u_{j} > 0$ ; utilication rate of furnace j for steel type i,

$\mathbf{c}_j$ : $\mathbf{j} \in \mathbf{furnace}$ , $\mathbf{c}_j > 0$ ; capacity of furnace j (tons/day)

$\mathbf{a}_{[i,k]}$ : $\mathbf{k} \in \text{coal}$ , $\mathbf{i} \in \text{steel}$ , $\mathbf{a}_{[i,k]} > 0$ ; utilization rate of coal type $\mathbf{k}$ for steel type $\mathbf{i}$

$p_{k}$ : $k \in coal$ , $p_{k} \geqslant 0$ ; purchase level for coal type k (tons)

$pc_{k}$ : $k \in coal$ , $p_{k}^{c} > 0$ ; purchase cost of coal type $k$ (\$/ton)

$\mathbf{u}_{i}$ : i ∈ steel; unit revenue for steel type i (\$/ton)

z; total profit (\$)

DEFINITIONAL EXPRESSION

$$
\mathbf {z} = \max ([ \mathbf {x} _ {i}, \mathbf {p} _ {k} ],
$$

FUNCTIONAL EXPRESSION (OBJECTIVE FUNCTION)

$\Sigma(i \in \text{steel}, \mathbf{u}_i * \mathbf{x}_i) - \Sigma(k \in \text{coal}, \mathbf{p}_k * \mathbf{pc}_k));$ maximize total profit, s.t.

CONDITIONAL EXPRESSIONS (CONSTRAINTS)

forall(k, $\Sigma (i\in$ steel, $\mathbf{a}_{[i,k]}*\mathbf{x}_i)\leqslant \mathbf{p}_k$ ); coal consumption less than purchase

forall(j, $\Sigma (i\in$ steel, $\mathbf{u}_{[i,j]}*\mathbf{x}_i)\leqslant \mathbf{c}_j$ ); furnace capacity constraint

forall(i ∈ steel, x\_i ≥ 0);

forall $(k\in \mathbf{coal},\mathbf{p}_k\geqslant 0)$

Example A.2. Steel production planning model, in $L^{\uparrow}$

\- model(steel-prod-plan, ‘Weekly production needs to be planned…’)

\- modelSource(steel-prod-plan, 'H.K. Bhargava and R. Krishnan, A Formal Approach to Model Formulation, Proceedings of HICSS, 1990.')

• model-class(steel-prod-plan, PDI)

\- set(fur-type, 'Types of furnaces that can be used to produce steel.')

\- set(steel-type, 'Types of steel produced at the mill.')

\- set(coal-type, 'Types of coal used as raw material.')

\- solver(steel-prod-plan,LINDO)

\- solver-output(steel-prod-plan, LINDO, z)

\- solver-output(steel-prod-plan, LINDO, $x_{i}$ )

\- solver-output(steel-prod-plan, LINDO, $p_{k}$ )

\- indexvar(i,steel-prod-plan,'Type of steel',[i in steel-type])

\- indexvar(j,steel-prod-plan,'Type of furnace',[j in fur-type])

- indexvar(k,steel-prod-plan,'Type of coal',[k in coal-type])

\- variable( $x_{i}$ ,['Amount of steel produced of type',i])

\- variable( $u_{i,j}$ ,['Utilization rate of furnace', j, 'for steel of type', i])

\- variable( $c_{j}$ ,['Capacity of furnace',j])

\- variable( $a_{i,k}$ ,['Utilization rate of coal type',k,'for steel type',i])

\- variable $(p_k, [\text{‘Purchase level for coal type’, k])$

\- variable $(pc_k, ['Purchase cost of coal type', k])$

\- variable( $u_{i}$ ,['Unit revenue for steel type',i])

• variable(z,'Total profit')

\- defE(steel-prod-plan,1.1.'Total profit = revenue-costs', z = sum(i in steel-type, $u_i * x_i$ )-sum(k in coal, $p_k * pc_k$ ))

\- defE(steel-prod-plan,1.2,'Maximize total profit',opt(z) $^{def}$ = max([ $x_{i},p_{k}$ ],z)

\- conE(steel-prod-plan,1.3,'Coal capacity constraint',forall(k in coal-type,sum(i in steel-type, $a_{i,k} * x_i \leqslant p_k$ ))

\- conE(steel-prod-plan,1.4,'Furnace capacity constraint',forall(j in furtype,sum(i in steel-type, $u_{i,j} * x_i \leqslant c_j$ ))

\- conE(steel-prod-plan,1.5,'Non-negative production',forall(i in steeltype, $x_{i}\geqslant 0$ ))

\- conE(steel-prod-plan,1.6,'Non-negative purchase level',forall(k in coaltype, $p_{k} \geqslant 0$ ))

\- quiddity( $x_{i}$ , tons, amount(produced(steel)))

\- quiddity $(u_{i,j},\text{nil,util-rate(steel,furnace)})$

\- quiddity( $c_{i}$ , tons/day, capacity(furnace))

\- quiddity $(a_{i,k},\text{nil,util-rate(steel,coal)})$

\- quiddity $(p_k, \text{tons}, \text{amount}(\text{purchased}(\text{coal}))$

\- quiddity $(pc_k, \text{dollars/tons}, \text{cost(purchase(coal))}$

\- quiddity $(u_{i},$ dollars/tons, profit(steel))

\- quiddity(z, dollars, total(profit(steel)))

\- assume(steel-prod-plan, indep-of(( $pc_k, p_k$ ))

\- assume(steel-prod-plan, upper-limit $(p_k) = \inf$ )

\- model-application(steel-prod-plan, 'This model was used previously …')

## References

[1] Hemant K. Bhargava, A Logic Model for Model Management: An Embedded Languages Approach, Ph.D. thesis, University of Pennsylvania, Department of Decision Sciences, 1990.

[2] Hemant Bhargava, Michael Bieber and Steven O. Kimbrough, Oona, Max, and the WYWWYWI Principle: Generalized Hypertext and Model Management in a

Symbolic Programming Environment, in: Janice I. De-Gross and Margrethe H. Olson, Eds., Proceedings of the Ninth International Conference on Information Systems, (November 30–December 3, 1988) 179–191.

[3] Hemant K. Bhargava and Ramayya Krishnan, A Formal Approach for Model Formulation in a Model Management System, in: Jay F. Nunamaker, Jr., Ed., Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, Vol. III (IEEE Computer Society Press, Los Alamitos, CA, January 1990) 453–462.

[4] Hemant K. Bhargava, Steven O. Kimbrough and Ramayya Krishnan, Unique Names Violations, a Problem for Model Integration or You Say Tomato, I Say Tomato, ORSA Journal on Computing 3, No. 2 (Spring 1991) 107–120.

[5] Michael P. Bieber and Steven O. Kimbrough, On the Concept of Generalized Hypertext, MIS Quarterly 16, no. 1 (March 1990).

[6] Michael P. Bieber and Steven O. Kimbrough, Towards a Logic Model of Generalized Hypertext, in: Jay F. Nunamaker, Jr., Ed., Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, Vol. III (IEEE Computer Society Press, Los Alamitos CA, January 1990) 506–519.

[7] J. Bisschop and A. Meeraus, On the Development of a General Algebraic Modeling System in a strategic planning environment, Mathematical Programming Study 20 (1982).

[8] G. Bradley, Mathematical Programming Modeling Project, Proceedings of the Conference on the Impact of Recent Computer Advances on Operations Research, Williamsburg, VA, January 1989.

[9] Gordon H. Bradley and Robert D. Clemence, Jr., Model Integration with a Typed Executable Modeling Language, in: Benn R. Konsynski, Ed., Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences, Vol. III, Decision Support and Knowledge Based Systems Track (January 1988) 403–410.

[10] S. Chari and R. Krishnan, Towards a Logical Reconstruction of Structured Modeling, in: Jay F. Nunamaker, Jr., Ed., Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, Vol. III (IEEE Computer Society Press, Los Alamitos CA, January 1990) 524–533.

[11] R. Fourer, Modeling Languages versus Matrix Generators for Linear Programming, ACM Transactions on Mathematical Software 9, No. 2 (1983).

[12] R. Fourer, David Gay and Brian W. Kernighan, A Mathematical Programming Language, Management Science 36, No. 5 (May 1990).

[13] S. Gass, Managing the Modeling Process: A Personal Reflection, European Journal of Operations Research 31 (1987).

[14] M. Genessereth and N. Nilsson, Logical Foundations of Artificial Intelligence (Morgan Kaufman Publishers, New York, 1987).

[15] Arthur M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987).

[16] Arthur M. Geoffrion, Computer-based Modeling Environments, European Journal of Operational Research 41, No. 1 (1989).

[17] Arthur M. Geoffrion, The SML Language for Structured Modeling, Working Paper No. 378, Western Management Science Institute, UCLA, 1990. (Two-part extract forthcoming in Operations Research.)

[18] Peter Jackson, Han Reichgelt and Frank van Harmelen, Eds., Logic-Based Knowledge Representation (The MIT Press, Cambridge, MA, 1989).

[19] Richard Jeffrey, Formal Logic: Its Scope and Limits, Third Edition, (McGraw-Hill, Inc., NY, New York, 1991).

[20] Steven O Kimbrough, Clark Pritchett, Michael Bieber and Hemant K. Bhargava, An Overview of the Coast Guard's KSS Project: DSS Concepts and Technology, in: Linda Volonino, Ed., DSS-90 Transactions: Tenth International Conference on Decision Support Systems (Boston, May 1990) 63–77.

[21] Steven O Kimbrough, Clark Pritchett, Michael Bieber and Hemant K. Bhargava, The Coast Guard's KSS Project, Interfaces 20, No. 6 (November–December 1990) 5–16.

[22] P. Maes and D. Nardi, Eds., Meta-Level Architectures and Reflection (north-Holland, New York, NY, 1988)

[23] Alexander Meeraus, An Algebraic Approach to Modeling, Journal of Economic Dynamics and Control 5 (1983) 81–108.

[24] Gerhard Rayna, Reduce: Software for Algebraic Computation (Springer-Verlag, New York, NY, 1987).

[25] T. Saaty and J. Alexander, Thinking with Models: Mathematical Models in the Physical, Biological, and Social Sciences (Pergamon Press, New York, NY, 1981).

[26] B. Silver, Meta-Level Inference (North-Holland, Amsterdam, Holland, 1986).

[27] Leon Sterling and Ehud Shapiro, The Art of Prolog: Advanced Programming Techniques (The MIT Press, Cambridge, MA, 1986).

[28] Stephen Wolfram, Mathematica: A System for Doing Mathematics by Computer (Addison-Wesley Publishing Company, Reading, MA, 1988).
