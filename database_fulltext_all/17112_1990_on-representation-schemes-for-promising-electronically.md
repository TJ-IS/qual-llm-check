---
otero_id: 17112
otero_key: "QXAHQ2NK"
title: "On representation schemes for promising electronically"
authors: "Steven O Kimbrough"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90003-a"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On Representation Schemes for Promising Electronically $^{1}$

Steven O. KIMBROUGH

University of Pennsylvania, The Wharton School, Department of Decision Sciences, Philadelphia, PA 19104-6366, USA

This paper proposes and discusses a series of representational techniques for expressing promises in first-order logic. It is argued that the proposed representations have properties that cohere well with our pre-theoretic concept of promising, including creation of intensional contexts. Also, representations of promises in other formal languages, and inferences with them, may be validated by translating the expressions into the first-order formalism proposed here. Finally, a brief discussion is given to indicate that the proposed representational techniques may be applied generally to other illocutionary forces (or propositional attitudes).

Keywords: Promise; Speech Acts; Electronic Contracting; Electronic Data Interchange; Propositional Attitudes.

The concept of a promise is obscure. This is why it challenges philosophic reflection. And this is why the philosopher is to some extent free to shape the concept so that its logical features and relations to other concepts become clear. Nothing more will here be said about the justification of our procedure [von Wright (1962)].

[M]utually self-imposed promissory obligation ... is the very life of contract [Fried (1981, p. 63)].

## 1. Introduction

Promising is fundamental to doing business. Issuing a check is issuing a promise to pay, as issuing a ticket is issuing a promise to provide service. An offer to contract is a promise to do something, conditioned on acceptance of the offer, and accepting an offer includes promising to meet the conditions of the offer. Promising pervades business communications [Kimbrough, Lee and Ness (1984)].

The purpose of this paper is to sketch a theory of how promises may be expressed in a machine-readable language. As has been noted [Kimbrough and Lee (1986)], although promises have long been usefully communicated electronically, they are generally expressed either in natural language – which is not machine-readable – or in specially-developed protocols – which are lacking in flexibility and expressive power. There remains the intriguing possibility of developing a machine-readable language for expressing promises. We may begin to explore this possibility by using some simple notation, which I shall modify subsequently. Let

$$
\text { Promise } (\alpha , \beta) (\Phi)\tag{1.1}
$$

represent 'Speaker $\alpha$ promises hearer $\beta$ that $\Phi$ ', where $\Phi$ may be an arbitrarily complex truth-bearing expression and $\alpha$ and $\beta$ are individual terms. Expression (1.1) may, of course, be made machine readable, but the problem at hand is not (primarily) one of notation. Rather, it is one of underlying logic. Do we have, for example, the following entailment?

![](/api/attachments/QXAHQ2NK/fulltext/images/f48f52aa9ba92e22183e2b6ede406b0dbdd3712723464ae6fb97e26ca31b2de0.jpg)

$$
\begin{array}{l} \text { Promise } (\alpha , \beta) (\Phi \wedge \Psi) \\ \quad \vDash \text { Promise } (\alpha , \beta) (\Phi) \wedge \text { Promise } (\alpha , \beta) (\Psi). \end{array}\tag{1.2}
$$

Notation alone will not tell us. The problem at hand is the broadly logical one of developing or using a formal language that can be proved to behave in a way that mirrors what it is we are trying to model. If, pre-theoretically, we are certain that promising both $\Phi$ and $\Psi$ implies both promising that $\Phi$ and promising that $\Psi$ (as is stated in (1.2)), then our logical theory, our formal language for representing promising, had better reflect this fact. $^{2}$

What, then, shall be our formal language for representing promises? The illocutionary logic of Searle and Vanderveken (1985) has been explored for this and related purposes [Kimbrough and Lee (1986), Winograd (1986), Winograd and Flores (1986), Lyytinen (1986, 1987) and indirectly by Crowston et al. (1986), Malone et al. (April 1987), Malone et al. (May 1987)]. A problem with the approach is that illocutionary logic is not well-developed theoretically. Moreover, it is highly non-standard and presently lacks any quantification theory, so that were it possible to use a more standard logic (with, e.g., a well-understood semantics), then it would be desirable to do so.

If a more standard logic were to be used for representing promises, some variety of modal (particularly some variety of deontic) logic would be a natural choice. A main reason for this is that modal logic, like promising, is not truth functional. The truth of 'It is necessary that $\Phi$ ' is undetermined given only that $\Phi$ is true, and the truth of 'It is possible that $\Phi$ ' is undetermined given only that $\Phi$ is false. Promising is arguably less truth functional than necessity. $\Phi$ is neither necessary nor sufficient for promising that $\Phi$ ; the one is left completely undetermined by the other.

A further complication is that promising – like modality – generates intensional contexts. $^{3}$ In particular, suppose that $\Phi$ is equivalent to $\Psi$ . Is ‘I promise you that $\Phi$ ’ equivalent to ‘I promise you that $\Psi$ ’? The reigning consensus, with which I agree, holds that it is not. Suppose, for example, that I promise to buy 100 widgets from you, but it happens that the only way I can buy those widgets is by firing my employee Lane, who simply refuses to buy anything from your company. In promising to buy the widgets have I also promised to fire Lane? Arguably not, for (roughly) what I promised I promised to do no matter what, while if

Lane had relented I could have kept my promise without firing her.

I claim that standard first-order predicate logic (FOL) can be used to express what needs to be said in making commercial promises. Given that promising is not truth functional and that it generates intensional contexts, the claim is perhaps surprising. But if the claim is correct this is happy news, for FOL is a well-developed and well-understood language, which can be expressed in machine-readable form. Further, certain fragments of predicate logic have quite attractive computational properties. I do not hope, in what follows, to present definitive support for the claim that commercial promising can be expressed in first-order logic. Instead, I shall discuss representational methods for expressing the sorts of things that need to be expressed in promising. The resulting formulae will not be identical in meaning with any such English statement as 'I promise to meet you for lunch tomorrow' and will certainly not be identical with any act of promising. Moreover, the resulting formulae do not constitute a full theory of representation for promising. This is a modeling effort and like other such efforts it aims only to capture what is essential and useful in the system – here, certain patterns of speech and behavior associated with business activities – that is being modeled.

The basic strategy I shall follow in the paper is as follows. First, I give an FOL representation of promising in a rough and approximate sense and I discuss the properties of the representation. The representation will be based upon claims (and theory) regarding the meaning of expressions uttered when promises are made. Second, I give an algorithm for translating expressions such as (1.1) into the FOL representation for promising. Then, I repeat this process through several iterations in which the senses of promising employed are progressively less rough and approximate. In the end a pattern will emerge. This pattern – a broad strategy for representing promises – and its properties constitute the main results to be presented here.

In section 2, I begin by discussing, and I hope clarifying, the relation between the expression of a promise and the making of the promise itself. First, however, I want to state and explain an assumption. It is not my intention that first-order logic actually be used in any real system as a machine-readable language for expressing promises (and other speech acts). Instead, I assume that an actual implementation will employ a specialized language and notation, designed for the application. I call this the working language. Expressions in such a working language might well look like (1.1). Given the theory, discussed below, of how to represent promises in first-order logic, it will be possible to develop rigorous translations from working language expressions to expressions in first-order logic. The working language may then be validated by examination of the first-order formula produced by the translation. In what follows, I illustrate translation from working language expressions – such as (1.1) – to first-order logic, but my focus is on the first-order expressions.

## 2. Contexts for Representation

To make a promise is to take a certain kind of action, a kind that involves a large element of convention. Part of making, or uttering, a promise is signalling that the promise is made. (For an early, and insightful, discussion of these points, see [Hume (1888, pp. 516–525) 'Of the Obligation of Promises'). Signals allowed for indicating a promise are determined by convention, explicit or implicit. They may include straightforward linguistic expressions, as in 'I promise to pay you for the widgets by Friday'. They may also include signs that cannot directly be taken as expressions in a language, in which case the sign may be understood to refer to a linguistic expression. One may, for example, make a promise by nodding or by giving a 'thumbs up' sign on the floor of a stock exchange or by putting a certain bit pattern in a packet sent on a telecommunications network. In the case of promising by nodding, the nod is a sign referring to the expression 'I promise that $\Phi$ where $\Phi$ is determined by the context. The act of giving the nod is, by convention, the act of uttering the expression that is its referent. Similar analyses can be given of the other cases, and generally.

There is an important difference, then, between the making of a promise and the vehicle for expressing a promise. I make a promise, e.g., by going up to you, looking at you, ascertaining that you are listening to what I say, and then saying 'I promise to deliver the 100 widgets to you before this Friday'. The main goal of this paper is to show how to express a promise, to make the saying of the promise, with the language of predicate logic as the vehicle. To do this, we must begin by laying out carefully distinctions made in this and the previous paragraph. Following that, I will sketch the contexts and associated conventions I have in mind for the application of the representation schemes for promising, which I will take up in section 3.

When a promise is made it is possible to distinguish four aspects of the promise:

1. the uttering of the promise (an act creating the promise);

2. the content of the promise;

3. the expression of the utterance of the promise;

4. the sign used to make the promise.

In the example of promising with a nod, the act (1) of nodding (in the appropriate circumstances) constitutes the uttering of the promise and the nod is the sign (4) used to make the promise. The sign, as I have said, refers to the expression (3), 'I promise that $\Phi'$ , and $\Phi$ is the content (2) of the promise.

As noted above, actions taken in certain circumstances, determined by implicit or explicit convention, count as promises. I call such an action the uttering of a promise, when it succeeds in creating a promise, and the attempted uttering of a promise, when it fails to create a promise. Such an utterance may be signified in a variety of ways (including carefully-worded written documents, verbal expressions, and simple hand signals), depending upon the ambient conventions. The uttering (successful or merely attempted) is not something that can be true or false. Making a contract, promising, running to first base, going out for a cup of coffee are alike in being actions and in not bearing truth values. That a contract exists, that a promise has been made, that Maciejewski became a lawyer in LaCrosse, that Colelli went back to New York are all, of course, either true or false, depending on whether the actions described occurred or not.

Grammatically, the utterance (or uttering) of a promise is – in virtue of being an action – a noun, and from a logical point of view is to be represented by a logical term [cf., van Fraassen (1971, pp. 26–7)]. Grammatically, the expression of a promise is clearly a sentence, as in 'I promise to deliver the 100 widgets to you before this Friday'. Such sentences bear truth values, as do the signs referring to them, in virtue of a translation scheme from the signs to the sentence expressions. The problem of developing a formal representation scheme for promising is the problem of developing a system of signs such that the signs (a) can be translated to their corresponding expressions, and (b) can be manipulated formally in a manner that correctly represents the formal manipulations that apply to their corresponding expressions.

Reverting to (1.1) again, the expression,

$$
\text { Promise } (\alpha , \beta) (\Phi)\tag{1.1}
$$

is to serve as our formal shorthand for the third-person assertion that $\alpha$ promises $\beta$ that $\Phi$ .⁴ Think of this expression as a possible sign of a promise that $\Phi$ . In what follows, I shall give a translation and analysis of this expression in first-order logic. For now, (1.1) may serve as a convenient shorthand in our discussion of the associated conventions and contexts.

The contexts I have primarily in mind are transactions under the Uniform Commercial Code, which governs routine buying and selling of goods among firms, and electronic mail communications in office environments [Kimbrough and Thornburg (1989)], either intra- or inter-organizational. In either case, a supporting telecommunications network is required. Given such a network, the convention characterizing the utterance of a promise over the network is simple:

Individual $\alpha$ promises individual $\beta$ that $\Phi$ on the network by putting a message (sign) onto the network of the form Promise- $(\alpha, \beta)(\Phi)$ ,

where $\text{Promise}(\alpha, \beta)(\Phi)$ bears a truth value and is analyzed below. $^{5}$ Roughly, the act of promising consists - under this convention - of uttering a certain truth-bearing sentence in an appropriate context, where the truth-bearing sentence says of the speaker that the speaker has made the promise. The sentence, 'I have promised to pay you \$100 for one widget', has a truth value and is not an action, let alone a promise. The underlying idea in the convention is that what counts as s promising h that s will pay h \$100 for one widget is that - under the right conditions - s says 's has promised to pay h \$100 for one widget'.

Two main things are needed for this convention to work. First, an adequate scheme for authenticating messages is required; the sender of the message must always be identifiable. Were this not the case, it would be possible for an individual other than $\alpha$ to send the $\text{Promise}(\alpha, \beta)(\Phi)$ message, which would defeat the convention and the system relying on it. One should not be able to issue the expression of a promise for someone else; otherwise, real promises cannot be distinguished from pseudo-promises.

The second main requirement for the success of this convention is that the message used to express the utterance have the right properties. It must be clear, unambiguous, readable and processable by a machine. All that can be achieved by a well-defined protocol for record passing. We want more. We require that the messages sent have significant expressive power; they should be interpretable as expressions in an open-ended and flexible language; the messages should be useful for performing inferences relevant to the promise in question; and the meaning of the messages should be acceptably close to the natural language root expressions they are modeling. In particular, the messages should be able to express attitudes towards statements, which statements in turn may express attitudes towards other statements (and on indefinitely). For example, in $\text{Promise}(\alpha, \beta)(\Phi)$ the expressed attitude is that of a promise. This propositional attitude is taken with regard to $\Phi$ , which itself may contain attitudinal expressions.

Showing how these requirements can be met is the main aim of this paper. If the message used to express a promise can be expressed in first-order predicate logic (FOL), then there is good reason to optimistic that these requirements can be met. In the next section I begin the discussion of just how messages of the form $Promise(\alpha, \beta)(\Phi)$ may successfully be represented in predicate logic.

## 3. Representation Schemes for Promising: First Pass

I shall begin discussion of the representation schemes with a brief digression. The purpose of the digression (in section 3.1) is to illustrate an important representation technique, which I shall use extensively in the sequel. Then (in section 3.2), I shall present and briefly discuss a simple representation scheme, in FOL, for promising. I elaborate upon this basic scheme in section 4.

## 3.1. Illustrative Digression

For the purpose of understanding more clearly what follows about promises, let us begin with an old philosophical chestnut that goes like this [cf., Ellis, (1979, p. 61)]. Consider the following three statements:

(a) If you live in Chicago, then you live in Illinois.
(b) If you live in Chicago, then you live in Wisconsin.

(c) If you live in Milwaukee, then you live in Illinois.

Symbolized in the usual manner, these statements yield:

$$
\begin{array}{l}\left(\mathbf {a} ^ {\prime}\right) \mathrm{C} \rightarrow \mathrm{I},\\\left(\mathbf {b} ^ {\prime}\right) \mathrm{C} \rightarrow \mathrm{W},\\\left(\mathbf {c} ^ {\prime}\right) \mathrm{M} \rightarrow \mathrm{I},\end{array}
$$

given the interpretation:

Now, if we think that $(a')$ is true and that both $(b')$ and $(c')$ are false, then we are agreeing that the following three statements are each and all true:

$$
\begin{array}{l}\left(\mathbf {a} ^ {\prime}\right) \mathrm{C} \rightarrow \mathrm{I},\\\left(\mathbf {b} ^ {\prime \prime}\right) \neg (\mathrm{C} \rightarrow \mathrm{W}),\\\left(\mathbf {c} ^ {\prime \prime}\right) \neg (\mathrm{M} \rightarrow \mathrm{I}),\end{array}
$$

using the unexceptionable principle that if something is false, then its denial is true. We have a problem, however, for (a'), (b''), and (c'') are jointly inconsistent. (b'') is equivalent to (C ∧ ¬W) and (c'') is equivalent to (M ∧ ¬I), together yielding $(C \wedge \neg I)$ , which is equivalent to the denial of $(\mathbf{a}')$ .

Most would, I hope, agree that (a) is true and that both (b) and (c) are false. We have a representation problem, then, and must conclude that somehow (a), not (b), and not (c) are not adequately represented by (a'), (b''), and (c''). One way (there are others) of handling this representation problem is to take (a), (b), and (c) as asserting something stronger than a material conditional $(\rightarrow)$ between the statements within (a), (b), and (c). We might well reason that somehow (a) must be true and that in denying (b) and (c) we are then denying that they must be true. If we reason this way, we are taking a modal point of view (reasoning about possibility and necessity, of whatever sort). On this view, (a) is asserting that necessarily (for some appropriate, but unspecified, kind of necessity) if you live in Chicago, then you live in Illinois. Using L as our symbol for 'It is necessarily the case that ...' and M for 'It is possibly the case that ...' we can symbolize (a), (b), and (c) as:

(d) $\mathbf{L}(C\to I)$

(e) $\mathbf{L}(C \to W)$ ,

(f) $\mathbf{L}(M \to I)$ .

Denying (e) and (f) and assuming that $L\Phi = \neg M \neg \Phi$ for any well-formed formula, $\Phi$ , gives us our analogs to $(a')$ , $(b'')$ , and $(c'')$ :

(d) $\mathbf{L}(C \rightarrow I)$ ,

$(e')\mathbf{M}_{\neg}(C \rightarrow W),$

$$
(\mathbf {f} ^ {\prime}) \mathbf {M} _ {\neg} (M \rightarrow I).
$$

This collection of statements is consistent, $^{6}$ so (d), (e), and (f) can, at least provisionally, be accepted as adequate representations of (a), (b), and (c). Unfortunately, with this representation we have moved beyond the familiar confines of FOL, contrary to the announced intention in section 1. We should like to return, and we shall. Showing how this is to be done is the main reason for this digression. As noted in section 1, both modality and promising are not truth-functional. Here, in the digression, my purpose is to treat of modality with the same techniques – conditioning and relativization, below – I shall later apply to promising (as well as other speech acts and propositional attitudes). This parallel application of the techniques serves, I believe, to illuminate their meaning.

L and M are operators whose intended interpretation (semantics) is modal (necessity and possibility). Under the standard semantics of modal logic [e.g., [Chellas, (1980), Forbes (1985), Hughes and Cresswell (1968)], the universe is (very roughly) conceived of as consisting of indefinitely many possible worlds, only one of which is the actual world (the one we live in). Although it is impossible to travel from one possible world to another, different possible worlds in a model may be described as being accessible (or inaccessible) to one another. Then, LΦ or 'It is necessarily the case that Φ' is interpreted as 'In every possible world accessible from the actual world, Φ is the case'. Similarly, MΦ, or 'It is possible that Φ', is to be understood as 'In at least one possible world accessible from the actual world, Φ is the case'.

To illustrate the intuition behind the accessibility relation, imagine you are deciding whom to vote for in a primary election. You would like to vote for Herman, Wahl, and Roubillard, who are running for different offices. Let:

H::You have voted for Herman.

R :: You have voted for Roubillard.

W:: You have voted for Wahl.

There are eight possibilities, each describing a distinct possible world:

Worlds Table 1.

<table><tr><td>world</td><td>H</td><td>W</td><td>R</td><td>direct access to</td></tr><tr><td>1</td><td> $\top$ </td><td> $\top$ </td><td> $\top$ </td><td>out</td></tr><tr><td>2</td><td> $\top$ </td><td> $\top$ </td><td> $\bot$ </td><td>nil</td></tr><tr><td>3</td><td> $\top$ </td><td> $\bot$ </td><td> $\top$ </td><td>nil</td></tr><tr><td>4</td><td> $\top$ </td><td> $\bot$ </td><td> $\bot$ </td><td>3, 2</td></tr><tr><td>5</td><td> $\bot$ </td><td> $\top$ </td><td> $\top$ </td><td>out</td></tr><tr><td>6</td><td> $\bot$ </td><td> $\top$ </td><td> $\bot$ </td><td>2</td></tr><tr><td>7</td><td> $\bot$ </td><td> $\bot$ </td><td> $\top$ </td><td>3</td></tr><tr><td>8</td><td> $\bot$ </td><td> $\bot$ </td><td> $\bot$ </td><td>7, 6, 4</td></tr></table>

There is a problem, however, in that not all logical possibilities are legal possibilities. You live in a state requiring that all the people you vote for in a primarily election be running for office under the same party. Roubillard is running in the Socialist primary, Wahl in the Democratic primary. By special arrangement Herman and all her opponents are running both in the Democratic and the Socialist primaries, and the two parties have agreed to nominate whoever gets the largest total vote in their two primaries taken together.

We can model the temporal unfolding of your options by using the accessibility relation. From Worlds Table 1, we note that two of the logically possible worlds (1 and 5) are not legally possible at all; we cannot assign $a^*$ (the actual world) to either one, so we will leave both out. Further, we can say that certain worlds are (directly) accessible from others, as noted in Worlds Table 1. So, e.g., if you are at world 8 (you haven't voted at all), then you have direct access to worlds 4, 6 and 7 (since you can only vote for one person at a time). We should add that, here, the accessibility relation is reflexive (you always have the option of voting for no one else) and transitive, but not symmetric (having voted, you cannot unvote).

Given all this, the resulting logic model behaves sensibly; what you can do depends upon what you have already done. If, e.g., $a^* =$ world 8, then it is possible for you to vote for Roubillard, since worlds 3 and 7 are accessible to you. If, on the other hand, $a^* =$ world 6, then it is necessary that you do not vote for Roubillard, for in all worlds accessible to you (6 and 2) you do not vote for Roubillard. (See Appendix 2 - to be read after Appendix 1 - for a proof-theoretic discussion of this simple model.)

Without going into a lengthy discussion of this way of thinking about possibility and necessity, it is worth noting that the English translations of (d), (e'), and (f') make good sense, remain consistent, and are arguably acceptable stylistic variants on (a), not (b), and not (c):

(d'') In every possible world it is true that if you live in Chicago, then you live in Illinois.

(e") There is some possible world in which you live in Chicago and you do not live in Wisconsin.

(f'') There is some possible world in which you live in Milwaukee and you do not live in Illinois.

(Again, I am leaving unspecified the sort of necessity being appealed to.)

To return to predicate logic, we need a translation scheme for converting a formula in the language of modal logic to a formula in an FOL (first-order predicate logic) language. I propose to do so by relativizing expressions in the modal language to the actual world. Letting $a^{*}$ be a logical constant term standing for the actual world, we may say that the translation of a modal formula, $\Phi$ , is the relativization of the formula to $a^{*}$ , or in symbols:

$$
\operatorname{Trans} (\Phi) = \operatorname{Rel} (\Phi , a ^ {*})\tag{3.1.1}
$$

Rel is given by an algorithm, which is discussed in Appendix 1 and developed in the sequel. The FOL language used there (and modified in the sequel) has two sorts of individuals: possible worlds and everything else. I will use u, v, w (possibly with subscripts) as possible world variables, and x, y, z (possibly with subscripts) as variables for anything but possible worlds. (Later, I will use, r, s, t (possibly with subscripts) as temporal variables.) The sorts applying to individual constants and functions should be clear from the context. Further, let:

$A(\alpha, \beta) ::$ World $\beta$ is accessible from world $\alpha$ .

Given this, $\mathbf{Trans}((\mathbf{d})) = (\mathbf{g})$ , $\mathbf{Trans}((\mathbf{e}^{\prime})) = (\mathbf{h})$ , and $\mathbf{Trans}((\mathbf{f}^{\prime})) = (\mathbf{i})$ , where:

$$
(\mathbf {g}):: (\forall w) (A (a ^ {*}, w) \rightarrow (C (w) \rightarrow I (w))),
$$

$$
(\mathbf {h}):: (\exists w) \neg (A (a ^ {*}, w) \rightarrow (C (w) \rightarrow W (w))),
$$

$$
(\mathrm{i}):: (\exists w) \neg (A (a ^ {*}, w) \rightarrow (M (w) \rightarrow I (w))),
$$

and

$C(w)$ :: At world w, you live in Chicago.

$I(w) :: \text{At world } w, \text{ you live in Illinois.}$

$W(w)$ : At world $w$ , you live in Wisconsin.

$M(w)$ :: At world w, you live in Milwaukee.

Rather transparently, (d''), (e''), and (f'') are English translations of (g), (h), and (i), and these latter expressions are mutually consistent. $^{7}$ It is worth noting that we can get expressions equivalent to (g), (h), and (i) in a single-sorted logic by introducing

$W_{1}(w)$ :: $w$ is a possible world.

and conditioning on it:

$$
\begin{array}{c}(\mathrm{g} ^ {\prime}):: (\forall w) (W _ {1} (w) \rightarrow (A (a ^ {*}, w) \rightarrow (C (w) \rightarrow\\I (w))))\end{array}
$$

$$
\begin{array}{c}(\mathrm{h} ^ {\prime}):: (\exists w) _ {\neg} (W _ {1} (w) \rightarrow (A (a ^ {*}, w) \rightarrow (C (w) \rightarrow\\W (x)))),\end{array}
$$

$$
\begin{array}{c}(\mathrm{i} ^ {\prime}):: (\exists w) \neg (W _ {1} (w) \rightarrow (A (a ^ {*}, w) \rightarrow (M (w) \rightarrow\\I (x)))).\end{array}
$$

Having said how translations into FOL can be given for (a), (b), (c), I now return to the problem of translating expressions such as (1.1) into FOL. We shall see that the main moves just made – providing a translation scheme, relativizing to possible worlds, and conditioning on possible worlds – will be made to work again. (Note: I am ignoring certain questions pertaining to transworld identity that have loomed large in the literature on modal logic [cf., Lewis (1968), Forbes (1985)]. Suffice it to say that I claim that once you fix your philosophy on the matter, the representation schemes I offer may either be retained or adjusted in unproblematic ways.)

## 3.2. Promising

With the foregoing in place, it is now possible succinctly to present a series of representation schemes in FOL for promising. I shall begin, in this section, with two elementary cases, which I shall abstract upon and generalize in the sequel.

Our problem is to provide a translation into FOL of

$$
\text { Promise } (\alpha , \beta) (\Phi),\tag{1.1}
$$

where the translation has a meaning acceptably close to 'Speaker $\alpha$ promises hearer $\beta$ that $\Phi$ . A simple intuition underlies the representation forms I shall propose. Suppose that $s$ promises $h$ that $P$ . The possible worlds can then be divided into two categories: those in which $s$ keeps his promise and those in which $s$ does not keep his promise. Thus, if $s$ has promised $h$ that $P$ , $P$ must be true in all those worlds in which $s$ keeps the promise, and $P$ may or may not be true in those worlds in which $s$ fails to keep his promise. This is a metaphysical point, not an epistemological one. We may or may not know whether our world, the one and only actual world, is a world in which $s$ keeps his promise that $P$ ; nonetheless that $s$ does so carries a truth value.

This simple intuition suggests - nearly mandates - the following representation for Promise $(\alpha, \beta)(\Phi)$ :

$$
(\forall w) \big (A (a ^ {*}, w) \rightarrow \big (C (w, \alpha , \beta) \rightarrow \operatorname{Rel} (\Phi , w) \big) \big),\tag{3.2.1}
$$

where:

$C(w, x, y):: w$ is a possible world in which $x$ keeps $x$ 's promises to $y$ ,

$A(u,v)$ ::World $v$ is accessible from world $u$ ,

which is translated into English as ‘Φ is true in every possible world (accessible from the actual world) in which α keeps his promises to β’. In other words, Trans((1.1)) = Rel((1.1), a\*) = (3.2.1), and we may (provisionally) add this as a rule to the relativization algorithm in Appendix 1. We shall also need to assume something about the accessibility relation, if (3.2.1) is to work as intended. In particular, I shall postulate that the actual world is accessible to itself:

$$
A (a ^ {*}, a ^ {*}).\tag{3.2.2}
$$

This is a weaker assumption than the T axiom (see Appendix 1).

To illustrate, let:

$$
\text { Promise } (s, h) (P),\tag{3.2.3}
$$

then:

$$
\begin{array}{r l}\text { Trans } ((3. 2. 3))&= (\forall w) (A (a ^ {*}, w) \rightarrow (C (w, s, h) \rightarrow P (w))),\\&\tag {3.2.4}\end{array}
$$

where:

$P(w) :: P \text{ is true at world } w.$

The main test, of whether an expression such as (3.2.1) is a good representation, consists of examining its behavior. Does what it implies, and is implied by, cohere with its purported English translation? The question has a long answer. Notice, first, that denying (3.2.1) yields a sensible result: if it is false that 'Speaker $s$ promises hearer $h$ that $P'$ then there is at least one world (accessible from the actual world) in which $s$ keeps his promises and $P$ is false. Also, 'Speaker $s$ promises hearer $h$ that $\neg P'$ has a sensible representation, so that the distinction between not promising and promising not is correctly maintained.

(1.1), as translated by (3.2.1), is not truth functional; neither promising nor not promising $\Phi$ follows from either $\Phi$ or $\neg\Phi$ . Further, given (3.2.1) as $\text{Trans}(\text{Promise}(s, h)(P))$ , and $P \to Q$ , it does not follow that $\text{Promise}(s, h)(Q)$ . Our representation for promising generates intensional contexts. If, however, $s$ promises $h$ that $P$ and $\mathbf{L}(P \to Q)$ , then it follows, on our representation, that $s$ promises $h$ that $Q$ .

Under what conditions does one break a promise? Intuitively, if s promises h that P and P is false, then s has broken his promise. Given our representation, and that if one breaks a promise one fails to keep it, we can represent breaking a promise (in world b) as

$$
\neg C (b, s, h).\tag{3.2.5}
$$

Now, if $\neg P(b)$ (P is false at world b), and (from (3.2.1)) s has promised h that P, then it follows that

$$
\neg (A (a ^ {*}, b) \wedge C (b, s, h)),\tag{3.2.6}
$$

i.e., that either $b$ is not accessible from $a^*$ or $b$ is not a world in which $s$ keeps his promise to $h$ . Assume now that $A(a^*, a^*)$ (or more broadly that accessibility is reflexive: $(\forall w)A(w, w)$ ), then if $P$ has been promised and is actually false (i.e., $\neg P(a^*)$ ) then the actual world is not a world in which $s$ keeps his promise to $h$ . This is exactly what we want and expect of any representation of promising.

I hold that 'Speaker $\alpha$ promises hearer $\beta$ that $\Phi'$ has essentially $^{8}$ the same meaning as 'In every possible world accessible from the actual world, if $\alpha$ keeps his promise to $\beta$ then $\alpha$ causes it to be the case that $\Phi'$ , which in English implies that 'In every possible world accessible from the actual world, if $\alpha$ keeps his promise to $\beta$ then $\Phi'$ . It is the latter expression that is represented by (3.2.1). To see the difference, imagine that Wahl promised to pay Herman \$100 in exchange for Herman's promise to deliver Wahl some widgets, but Wahl instructed her accounting department not to pay Herman the \$100. Nevertheless, because of a freak accident Herman is in fact paid \$100 by Wahl. Clearly, Wahl did not cause the \$100 payment. In spite of the fact that what Wahl promised – the \$100 payment – occurred, I believe that we should regard Wahl as having reneged on her promise. The difference, however, is not much of a difference (we shall see later a case in which perhaps it matters) and causation is difficult to model, so I think it best to use the latter expression (implied by the former) as the object of our representation efforts. Here, as in every case of modeling, compromises between accuracy and tractability are required.

A limitation of practical import in (3.2.1) is that promises are not individuated. We have with it no way of saying that in some world $\alpha$ keeps certain promises and breaks others. This limitation is easily remedied by indexing each promise with a unique name. We replace (1.1) with (3.2.7):

$$
\text { Promise } (\alpha , \beta , \nu) (\Phi),\tag{3.2.7}
$$

where $\nu$ is required to be a unique name, and we replace (3.2.1) with (3.2.8):

$$
\begin{array}{l}(\forall w) \big (A (a ^ {*}, w)\\\rightarrow \big (C (w, \alpha , \beta , \nu) \rightarrow \mathbf {R e l} (\Phi , w) \big) \big),\end{array}\tag{3.2.8}
$$

where:

$C(w, x, y, \nu):: w$ is a possible world in which $x$ keeps $x$ 's promise, $\nu$ , to $y$ .

An interesting question is whether, in (3.2.8), $\Phi$ should also be indexed with v. If so, then we need to define an indexing function, $\text{Index}(\Phi, v)$ , that adds another argument to each predicate in $\Phi$ and puts v into it. Index is defined in Appendix 3. Given this function, an alternative to (3.2.8) as a translation of (3.2.7) is (3.2.9):

$$
\begin{array}{l}(\forall w) \big (A (a ^ {*}, w)\\\rightarrow \big (C (w, \alpha , \beta , \nu) \rightarrow \operatorname{Rel} (\operatorname{Index} (\Phi , \nu), w) \big) \big),\end{array}\tag{3.2.9}
$$

(3.2.9) would be preferred to (3.2.8) in situations in which it is possible that otherwise a single state of affairs would satisfy more than one promise. For example, suppose Maciejewski sells Colelli \$100 worth of widgets and \$100 worth of smidgets. Colelli makes exactly one payment of \$100. Under (3.2.8), we would have to record both that a payment was made and that a payment was not made, a contradiction. Under (3.2.9) the logic allows us to distinguish the payment that has been made from the one that has not been made, and no contradiction results.

This completes my sketch of the basic theory for representing promises in FOL. Before elaborating upon the theory, it is worth commenting on how it might be applied. My claim is that, given appropriate conventions and expressed in the right circumstances, (3.2.9)-type expressions can serve as good representations for the expressions used in making the utterance of a promise (recall section 2). The idea is this. Participants on the network agree (by convention, as it were) that putting an expression of the form (3.2.9) on the network constitutes making a promise (with content $\Phi$ ). In addition, physical arrangements are made so that only the initiator of the action (of putting such an expression on the network) can be named by $\alpha$ . Thus, the promisor is one and the same as the speaker; one cannot utter promising expressions for someone else. $^{9}$ Finally, each expression put on the network is indexed by a unique token, $\nu$ (e.g., a concatenation of the speaker's name and the time of the speech act). Then, given proper means of authentication, expressions of the form (3.2.9) will be on the network if only if $\alpha$ has promised $\beta$ that $\Phi$ and $\alpha$ has abided by the network's conventions for making promises.

## 4. Promising and Time

My purpose in this section is to elaborate upon (3.2.1) and (3.2.9), and the previous discussion pertaining to them, by bringing in temporal considerations. We shall see that the moves taken here to accommodate time generalize to other conditions as well.

Promises are actions, events that occur in time. It is normally thought that one cannot promise to do something in the past [e.g., von Wright (1962)]. Using the vocabulary developed above, we can say that a validity condition for promising is that the time of the utterance be before the first time at which the content of the promise is to become true. Using notation whose FOL translation is given in Appendix 4, let:

$$
T _ {-} a t (\Phi , \tau)\tag{4.1}
$$

symbolize ‘Φ is true at time τ’, where Φ is (as usual) a statement and τ a time. (We now change the underlying FOL language from having two sorts – possible worlds and everything else – to having three sorts – possible worlds, times, and everything else.) Likewise, we change (3.2.7) to (4.2):

$$
\text { Promise } (\alpha , \beta , \nu , \tau_ {0}) (T _ {-} a t (\Phi , \tau)).\tag{4.2}
$$

Suppose an expression of the form (4.2) is uttered, but $\tau_{0}$ is after $\tau$ , what are we to make of this? One option is simply to prohibit such expressions from being sent to the hearer. An honest post office could perform this and other validity checks. Invalid messages could be returned to the sender. A second option would be to add a universal axiom, available to all, much as a basic lexicon would be. The axiom (scheme) would say that, in promise expressions of the form of (4.2), $\tau$ is after $\tau_{0}$ :

$$
\begin{array}{l} (\forall \Phi) (\forall x) (\forall y) (\forall z) (\forall s) (\forall t) \\ \big (P r o m i s e (x, y, z, s) (T _ {-} a t (\Phi , t)) \to s <   t \big). \end{array}\tag{4.3}
$$

A significant disadvantage with (4.3) is that the expression used in making a promise (or attempting to do so) is (in conjunction with (4.3)) inconsistent, if in fact the time of the promise if after the promise time. This defeats the network access convention, which needs to assure the participants that nothing false gets put onto the network.

A third option for handling this temporal validity condition is to treat it literally as another condition on the promised content. In this case a (partial) translation of $(4.2)$ would be

$$
\begin{array}{r l} & {(\forall w) \big (A (a ^ {*}, w) \to \big (C (w, \alpha , \beta , \nu , \tau_ {0})} \\ & {\qquad \to \big (\tau_ {0} <   _ {t} (w) \tau} \\ & {\qquad \to \operatorname{Rel} \big (\operatorname{Index} (\operatorname{Index} (\Phi , \nu), \tau), \mathrm{w}) \big) \big),} \end{array}\tag{4.4}
$$

which is equivalent to

$$
\begin{array}{r l}&{(\forall w) \big ((A (a ^ {*}, w)}\\&{\qquad \wedge C (w, \alpha , \beta , \nu , \tau_ {0}) \wedge \tau_ {0} <   _ {t} (w) \tau \big)}\\&{\rightarrow \operatorname{Rel} (\operatorname{Index} (\operatorname{Index} (\Phi , \nu), \tau), w) \big),}\end{array}\tag{4.5}
$$

where $s < _t(w)t$ is interpreted as 'At world $w$ , time $s$ is before time $t$ '.

Comparing (4.4) and (4.5) with (3.2.9), we see that, abstractly, the FOL representation of a basic promise expression (3.2.9) is $(\Psi \rightarrow \Phi)$ , where $\Phi$ is the content of the promise (what it is that is promised) and $\Psi$ indicates that something is being promised (it indicates an illocutionary force). By adding a temporal validity condition we have a less basic promise expression (4.5), having the form $(\Psi \wedge \Gamma \rightarrow \Phi)$ .

The key to the use of (4.5) is that the truth of $s <_{t}(w)t$ can be determined independently by all network participants. One may not know what time an action occurred, but one always does know that April comes after May in any given year. To illustrate, suppose that s sends h the message

$$
\begin{array}{r l}&{(\forall w) \big ((A (a ^ {*}, w)}\\&{\qquad \wedge C (w, s, h, n, t _ {0}) \wedge t _ {0} <   _ {t} (w) t _ {d} \big)}\\&{\qquad \rightarrow \operatorname{Rel} \big (\operatorname{Index} \big (\operatorname{Index} (\Phi , n), t _ {d} \big), w \big) \big)}\end{array}\tag{4.6}
$$

but $\neg t_0 <_t(w)t_d$ and $h$ is able to deduce this (an elementary operation), then $\neg \mathbf{Rel}(\mathbf{Index}(\mathbf{Index}(\Phi, n), t_d), a^*)$ does not imply $\neg C(w, s, h, n, t_0)$ . Since $\neg \Phi$ does not imply that $s$ breaks her promise, then $\Phi$ cannot have been promised by $s$ . $h$ will be able to deduce this and act accordingly. (Notice that if $t_0 <_t(w)t_d$ , then (4.6) implies $\mathbf{Trans}((3.2.7))$ , given the obvious substitutions.)

This third strategy for handling temporal conditions works well, I believe, and generalizes to other conditions or qualifications on promising. Falsehood of the condition ( $\Gamma$ in the abstraction above) will not generate any inconsistency.

There is a fourth strategy, which can also be generalized beyond management of temporal validity conditions, but which I shall not discuss in any depth here. $^{10}$ In pursuing this strategy, called embedded languages, one expresses the formulae of one formal language, called $L_{\downarrow}$ , within another, called $L^{\uparrow}$ . Further, information about expressions in $L_{\downarrow}$ – including validity conditions – can be expressed in $L^{\uparrow}$ and used for inferencing and action. The essential idea is to formalize the metalanguage for the object language of interest, here a formal language for business communications. Although the technical details are lengthy, the principle is simple and the strategy sound theoretically.

## 5. Discussion

There is no fully agreed upon analysis of promising, either in the philosophical literature or in the jurisprudence literature. Nor is it obvious that a single analysis of promising can be had. There may well be several different, albeit related, notions of promising, each appropriate in certain contexts. Thus, testing the adequacy of a proposed representation (or representation scheme) for promising must involve considered judgments about the contexts of intended use of the representation, about various competing analyses of promising, and about tradeoffs between the accuracy and the complexity of the representations.

My comments in this section are aimed at such testing of the proposed representation (forms) for promising. In section 5.1, I prove certain properties of the representation scheme I have proposed. An important - but I think unproblematic - assumption in the proofs I offer is that if $\text{Trans}(\Phi) = \Psi$ , then $\Phi$ and $\Psi$ have the same truth value. In section 5.2, I address three questions: (1) What happens when someone promises something that cannot be done? (2) What obligations are incurred by promising? and (3) What must one intend for one's promise to be valid? The findings of these three subsections constitute, I maintain, strong reasons for accepting the representation scheme I have proposed.

A word on notation. I have augmented

$$
\text { Promise } (\alpha , \beta) (\Phi),\tag{1.1}
$$

in a variety of ways and provided a translation in each case. In some of these cases we have an operator on $\Phi$ , which may be subject to quantification (e.g., $T\_at(\Phi, \tau)$ in (4.2) and (4.5)). For the sake of perspicacity in stating the theorems that follow, I shall abbreviate (1.1) and all its extensions as

$$
\operatorname{Prom} (\Phi),\tag{5.1}
$$

but shall carry out the proofs in a generalization of (4.5):

$$
\begin{array}{r l}(\forall w) (\forall \nu) (\forall \overline {{\eta}})&\big ((A (a ^ {*}, w)\\&\wedge C (w, \alpha , \beta , \nu , \overline {{\eta}}) \wedge \Gamma (\overline {{\eta}})\\&\rightarrow \operatorname{ReL} \big (\Omega (\operatorname{Index} (\Phi , \nu), \overline {{\eta}}), w \big) \big),\end{array}\tag {1}\tag{5.2}
$$

where $\bar{\eta}$ is a vector of (individual) terms, $\Gamma(\bar{\eta})$ an arbitrary predicate (used for conditioning and qualification), and $\Omega$ an arbitrary operator on formulas ( $\Phi$ ), taking parameters from $\bar{\eta}$ . Finally, if promising that $\Phi$ is represented by (5.1), then

$$
\text { Reneg } e (\Phi) \stackrel {\text { def }} {=} \text { Prom } (\Phi) \wedge \neg \Phi .\tag{5.3}
$$

The idea is that if one has promised that $\Phi$ but $\Phi$ is false, then one has broken, or reneged on, one's promise.

## 5.1. Basic Laws of Promising

Intensionality Theorem. $Prom(\Phi), \Phi \leftrightarrow \Psi \nvdash Prom(\Psi).$

Proof. Translating these expressions into FOL yields an invalid sequent. (Note: Quantificational generalizations are straightforward.)

Laws of Negation for Promising. $Prom(\neg\Phi)\nvdash\neg Prom(\Phi)$ , $\neg Prom(\Phi)\nvdash Prom(\neg\Phi)$ .

Proof. Trans(Prom(¬Φ)) and Trans(¬Prom(Φ)) are expressions in FOL, neither of which implies the other.

Law of Conjunction Distribution for Promising. $\text{Prom}(\Phi \wedge \Psi) \leftrightarrow \text{Prom}(\Phi) \wedge \text{Prom}(\Psi)$ .

Proof. Trans(Prom(Φ ∧ Ψ)) is equivalent in FOL to Trans(Prom(Φ) ∧ Prom(Ψ)). (Note: Prom does not distribute across ∨ or →. This is, I claim, intuitively correct. One can promise that P or Q, without promising that P or promising that Q. Still, if neither P or Q come true, one has reneged and that does follow in the representation scheme. Since the conditional is a variant of the disjunction, nothing new would be added by discussing it.)

Law of Biconditional Distribution for Promising. $\text{Prom}(\Phi \leftrightarrow \Psi) \rightarrow (\text{Prom}(\Phi) \leftrightarrow \text{Prom}(\Psi))$ .

Proof. Translating these expressions into FOL yields a valid sequent. (Note: this accords with intuition. If I promise that I will sell you widgets if and only if I will sell you gadgets, and if I promise to sell you widgets, then I have promised to sell you gadgets. The converse to this law is not true, either intuitively or logically in this representation. From the fact that I promise to sell you widgets if and only if I promise to sell you gadgets, it should not follow that I promise to sell you widgets if and only if I sell you gadgets, since I may not have made any promise at all. Again, the behavior of the representation accords with intuition upon reflection.)

Conditioning Theorem. Prom(Φ → Ψ), Φ ⊢ ¬Ψ → Renegé(Φ → Ψ).

Proof. Translating these expressions into FOL yields a valid sequent. (Note: $P$ , $P \to Prom(\Phi) \vdash Prom(\Phi)$ , but $P$ , $Prom(\Phi \to \Psi) \not\vdash Prom(\Psi)$ .)

The behavior, with respect to these laws of promising, of the representational schemes under consideration is a good test of their adequacy. The same test should be applied to any alternate representation scheme for promising. If the logical behavior of the scheme proposed here is correct – as I think it is – then the logical turn, the move to a formal language expressed in FOL, has paid off handsomely, for the representation supports inferencing and does so validly. Moreover, the representation is tied to an explicit theory of promising. These are advantages that it would be hoped a formal language for business communication (FLBC), rather than a protocol, would provide.

## 5.2. Three Questions

Let us now turn to the three questions that I raised in the first paragraph of section 5.

First, what happens when someone promises the impossible? Suppose Lane promises (or, not to beg the question, attempts to promise) Klabundi that $\Phi$ but $\Phi$ is (in some sense of the word) impossible. Then it is impossible for Lane to keep her promise. More generally, we have the following:

Promising Impossibility Theorem. Prom(Φ), L¬Φ
← Renegé(Φ).

Proof. Translating these expressions into FOL yields a valid sequent. (Note: a stronger conclusion is possible. Not only do you renege, you must renege. Using (5.2), the conclusion of the above theorem can be strengthened to $(\forall w)(A(a^{*}, w) \rightarrow \neg C(w, \alpha, \beta, \nu, \bar{\eta}))$ . If you promise the impossible you necessarily break your promise.)

## Promising Necessity Theorem. $Prom(\Phi), L\Phi \vdash \Phi.$

Proof. Translating these expressions into FOL yields a valid sequent. (Note (1): Here we are using the assumption that the actual world is accessible to itself. Note (2): As in the previous theorem, the conclusion can be strengthened to $(\forall w)(A(a^{*}, w) \rightarrow C(w, \alpha, \beta, \nu, \bar{\eta}))$ . If you promise the necessary, you necessarily keep your promise.)

The second question concerns the obligations incurred in promising. Reverting to our example, there are some [cf., Searle and Vanderveken (1985)] who would argue that Lane has failed to promise that $\Phi$ ; the (attempted) promise is invalid and should be considered null, for the act that resembled a promise did not succeed. An argument in favor of this view is as follows [von Wright (1962)]. Promises create obligations, but one is never obliged to do what cannot be done, hence one cannot promise what is (in the operant sense of the word) is impossible. This presents a problem, for there is nothing about the representation schemes for $Prom(\Phi)$ that requires $\Phi$ to be possible.

I prefer a different analysis (of promising and obligation) and dispute the claim that in all cases if one promises that $\Phi$ then one is obliged to see to it that $\Phi$ . The intuition is that it is one thing to make a promise and another to be obliged to keep the promise, for often times one is obliged upon promising only if certain other conditions are met. Usually, we are obliged to keep our promises, but not always. Sometimes we are excused. For example, if Lane promises to meet someone for lunch at noon, but is late because of an unanticipated traffic jam, she will likely not be accused of breaking her promise. Similarly, if Roubillard makes an extravagant offer, but is later held to be insane, it may well be that the courts will release her from any obligation to make good on the offer. Ordinary language reflects this point of view, as when we say “And there’s no excuse for it” in heaping scorn on someone who has broken a promise. In short, promises create obligations, but defeasibly so. What may defeat an obligation from a promise? The content of the promise being impossible – and the promisor being unaware of that fact at the time of the promise – is, I think, a clear case in point. $^{11}$

There is an important practical advantage in permitting promises whose content is impossible. Under the scheme envisioned here, $Prom(\Phi)$ has a truth value. If promising the impossible is not permitted, however, the expression $Prom(\Phi)$ could turn out to be meaningless, neither true nor false, complicating things greatly. I think it is better to say that if one promises the impossible, then one necessarily breaks one's promise (and if one promises the necessary, one necessarily keeps the promise). In fact, the representation scheme proposed here supports there inferences.

Even so, there will be many cases in which we want to have it implied that a promise creates an obligation. This requirement can be handled by adding a simple law, which may be varied and elaborated in many ways:

$$
\begin{array}{c} (\forall w) (\forall x) (\forall y) (\forall z) \\ \bigl (\neg C (w, x, y, z) \to I (w, x, y) \bigr), \end{array}\tag{5.2.1}
$$

where $I(w, x, y)$ is to be interpreted as 'In world $w, x$ has acted forbiddenly (i.e., illegally, immorally, etc.) towards $y'$ . Note that - both in ordinary language and in this formal language - if $s$ promises that $P$ , then if $s$ is not to act forbiddenly, then $P$ must be true. Thus, while I have not presented a full theory of representing the obligations of promises, I believe that there are no fundamental obstacles to doing so with the representation schemes for promising I am proposing.

Finally, there is our third question, regarding intentions and promising. Searle and Vanderveken (1985) hold that if one promises that $\Phi$ , then one must intend that $\Phi$ . In support of this claim, they point out that expressions such as 'I promise to meet you for lunch tomorrow, but I do not intend to meet you for lunch tomorrow' are paradoxical and, they claim, incoherent. I disagree. It is odd, surely, to promise and to announce your intention to break the promise – all in one breath – but it is not incoherent; it is not nonsense. My view, in brief, $^{12}$ is that to promise one must intend that the expression of the promise be understood as just that. Actors on stage who say 'I promise…', and tyros at auctions who mistakenly make the hand signal of a bid, have not promised anything because they did not intend that the promising expression they issued should count as a promising expression. Not so with those who would deceive others. A false promise is, on this view, a promise nonetheless. An important practical advantage of this view is that the network access conditions can in principle be arranged so that no one issuing a promise expression on the network can plausibly deny an intention to do so, hence neither can the intention that the expression be taken as indicating a promise be plausibly denied. It is difficult to see how – even in principle – a communications network could be designed so that only those intending to do $\Phi$ could (on the network) issue a promise expression to do $\Phi$ .

## 6. Problems

Nothing is flawless, including the representation scheme developed here. In this section I shall discuss two problems with the representation scheme. I shall argue that these problems, although unwanted, are not debilitatingly serious.

The first problem arises through reflecting upon the following theorem.

Promising Paradox of Necessity. $\mathbf{L}\Phi \vdash Prom(\Phi)$ .

Proof. Translating these expressions into FOL yields a valid sequent.

The mist of paradox lifts somewhat if we reflect on the meaning of the translation of $Prom(\Phi)$ , on our theory of what it means to promise. It is surely correct to say that, if for all possible worlds accessible to the actual world (including those in which one keep's one's promises), $\Phi$ , then $\Psi \to \Phi$ is true at every accessible world. We can think of the present paradox as an analog of the paradox of material implication: $\Phi \vdash (\Psi \to \Phi)$ . We must live with both.

The second problem has to do with saying that a promise has been kept. It is easy to say, in FOL, that a promise has been kept. Using (4.5), we can say that promise $\tau_{0}$ has been kept in the actual world with: $C(a^{*}, \alpha, \beta, \nu, \tau_{0})$ . We get into trouble, however, if we try to provide a rule for deducing that a promise has been kept. It is tempting to define keeping a promise as:

$$
\operatorname{Prom} (\Phi) \wedge \Phi \rightarrow \operatorname {K e e p \_ p r o m} (\Phi).\tag{6.1}
$$

This may be intuitively appealing and apparently innocuous, but it isn't. Let:

Trans(Prom(Φ)) = (∀w)(A(a\*, w) ∧ C(w, α, β) → Rel(Φ, w)) and

$\operatorname{Trans}(\Phi) = \operatorname{Rel}(\Phi, a^*)$ . This yields

$$
\begin{array}{r l} & {(\forall w) (A (a ^ {*}, w) \land C (w, \alpha , \beta) \to \mathbf {R e l} (\Phi , w))} \\ & {\quad \land \mathbf {R e l} (\Phi , a ^ {*}) \to C (a ^ {*}, \alpha , \beta),} \end{array} \tag {6}\tag{6.2}
$$

as an axiom scheme in FOL for (6.1). Consider the following.

Arg(1):

1. $(\forall w)(A(a^{*},w)\land C(w,s,h)\to P(w)).$ (Assumption: $P$ has been promised by $s$ to $h$ .)

2. $Q(a^{*})$

(Assumption: $Q$ is true in the actual world.)

4. $(\forall w)(A(a^{*},w)\land C(w,s,h)\to (P(w)\lor Q(w)).$ (From 1 by FOL)

4. $(Q(a^{*})\vee P(a^{*}))$

5. $C(a^{*}, s, h)$ .

(From 4, 3 and (6.2) by FOL.)

6. $\neg P(a^{*})$ .

(Assumption: P is false in the actual world.)

7. $\neg C(a^{*}, s, h)$ . (From 1 and 6 by FOL.)

Thus, given a promise (line 1) and any fact true in the actual world (line 2), it follows that the promise is kept (line 5). Further, if what was originally promised (P) comes out false, then a contradiction results (lines 5 and 7). This looks like disaster.

The only option I see with regard to (6.2) is to reject it. This is not a particularly happy alternative. Neither is it especially bad. I adduce three reasons.

First, as already noted, the representation scheme does allow us to say that a promise is kept. This is no small consolation. Further, what should follow from a promise and the fact that the promise is kept does follow. From $Prom(P)$ and $C(a^{*}, s, h, n)$ it follows that $P(a^{*})$ . There is, however, no way without (6.2) or something like it to deduce that a promise has been kept.

A second reason to reject (6.2) is that the motivation for it may be mistaken. The intuition that led to (6.2) is appealing. That does not make it correct. I have by doubts. Suppose one promises to do something, sets out not to do it, but ends up doing it after all. Perhaps one has not broken the promise. Has it been kept? What the right answer is is not obvious to me and I leave it as a matter for future research. Recall Satre's short story, 'The Wall', in which the narrator is a partisan who gives his tormentors directions to the local commander's hideout, intending to mislead them. It turns out the directions are correct. Has the narrator kept his promise to inform on his commander? If not, perhaps we can reject (6.2) and the intuition behind it, and do so with equanimity. The idea is that, while one may promise without intending to keep the promise, keeping the promise implies intending what is promised. If so, then if (6.2) is right $Prom(P)$ and P implies intending that P, and for reasons given earlier I think that incorrect. Finally, I note that those who like (6.2) may be wont to like affirming the consequent. Perhaps both are equally mistaken.

Even if the first two points were not convincing, there remains the question of whether a practical need exists, in the application envisioned here (inter- and intra-organizational business communications) to do more than express the notion that a particular promise has been kept. A case can be made that any such need is small. What does one learn in hearing that $Prom(\Phi)$ and $\Phi$ ? If someone has promised to send me widgets, then my direct concern is whether the widgets have arrived (It is true that $\Phi$ ?) and if not, who is to be blamed (Has a promise been broken and if so, whose promise?). Both of these questions are answerable in the representations proposed here.

## 7. Extensions: Other illocutionary Forces

The technique of combining relativization, conditioning, and indexing, much in evidence above, can fruitfully be used to model types of expression other than promises. According to Searle's theory of speech acts [Searle (1975), Searle and Vanderveken (1985) and Kimbrough and Lee (1986) for a brief review] there are but five fundamental illocutionary forces: assertives, commissives (promises are a type of commissive), directives, declaratives, and expressives. According to the theory, every expression in every language is at bottom one of these, or a combination of them, properly qualified. I believe that the representation schemes for promising can be modified and used for representing the other four illocutionary forces. I shall now sketch an account of how these four might be represented.

## 7.1. Representing Assertives

The point of an assertive is to say that something is the case. Thus, $\text{Assert}(\alpha, \beta)(\Phi)$ (by analogy with (1.1)) is to represent that $\alpha$ asserts to $\beta$ that $\Phi$ is true. Let:

$T(w, x, y) :: \text{In world } w, \text{ speaker } x \text{ tells the truth to hearer } y.$

$$
\begin{array}{l}\text { Then } \operatorname{Trans} (A s s e r t (\alpha , \beta) (\Phi)) =\\(\forall w) (A (a ^ {*}, w) \wedge T (w, \alpha , \beta) \rightarrow \operatorname{Rel} (\Phi , w)).\end{array}\tag {7.1.1}
$$

Clearly, (7.1.1) could be generalized and extended in a manner similar to (1.1).

## 7.2. Representing Directives

Directives are commands, orders. Their point is to get someone to do something. Letting $\text{Direct}(\alpha, \beta)(\Phi)$ represent that $\alpha$ commands $\beta$ that $\Phi$ , and letting

$D(w, x, y) :: \text{In world } w, \text{ speaker } x's \text{ directive to } y \text{ succeeds.}$

$$
\begin{array}{r l}&\text { Then } \operatorname{Trans} (D i r e c t (\alpha , \beta) (\Phi)) =\\&\quad (\forall w) (A (a ^ {*}, w) \wedge D (w, \alpha , \beta) \rightarrow \operatorname{Rel} (\Phi , w)).\end{array}\tag {7.1.2}
$$

Clearly, (7.1.2) could be generalized and extended in a manner similar to (1.1).

## 7.3. Representing Declaratives

A successful declarative brings into being the fact its content describes. Thus, for a successful declarative, saying so makes it so. Examples are 'You're out?' From an umpire, 'Your name is Margaret Lane' from the parents at a naming ceremony, and perhaps (but contrary to Winograd and Flores (1986, p. 59) and Searle and Vanderveken (1985), p. 21)) 'I apologize'. Declaratives are also frequently uttered non-verbally.

There must be two elements in a successful declarative. First, the speaker must have the authority to make the declaration. Only the umpire can call you out. Only you can really endorse your checks, all other signatures being forged or merely apparent endorsements. Second, the speaker must utter an appropriate expression. For that expression, let

$Auth(w, x, y, z)::$ In world w, speaker x has authority of type z with respect to y.

Then $\operatorname{Trans}(\text{Declare}(\alpha, \beta, \nu)(\Phi)) =$

$$
\begin{array}{l}(\forall w) \big (A (a ^ {*}, w) \wedge A u t h (w, \alpha , \beta , \nu)\\\rightarrow \operatorname{Rel} (\operatorname{Index} (\Phi , \nu), w) \big).\end{array}\tag{7.3.1}
$$

But something more is needed if the utterance of (7.3.1) is to result in $\Phi$ . What needs to be stated (or implied) is that the speaker has the authority, i.e., that

$$
\operatorname{Auth} \left(a ^ {*}, \alpha , \beta , \nu\right).\tag{7.3.2}
$$

Something like this might be had by adding a system-wide axiom to the effect that anyone who owns something may transfer it to anyone else:

$$
\begin{array}{r l}&O w n s (a ^ {*}, \alpha , \gamma)\\&\rightarrow (\forall w) (A (a ^ {*}, w) \wedge A u t h (w, \alpha , \beta , \nu)\\&\rightarrow T r a n s f e r (w, \alpha , \gamma , \beta , \nu))\\&\rightarrow T r a n s f e r (a ^ {*}, \alpha , \gamma , \beta , \nu),\end{array}\tag{7.3.3}
$$

where:

$$
\begin{array}{l} \text { Owns } (w, x, y):: \text { In   world } w, x \text { owns } y. \\ \text { Transfer } (w, x, z, y, z _ {1}) \end{array}
$$

:: In world w, x transfers z to y with respect to action $z_{1}$ .

Then, for example, if the speaker, Maciejewski, declares to Wahl that the object is transferred to Wahl and Maciejewski actually owns the object (at the time of the utterance) then the object is actually transferred to Wahl. $^{13}$ Further, if Maciejewski declares to Wahl that the object is transferred to Wahl and that she (Maciejewski) actually owns the object (at the time of the utterance) then the object is actually transferred to Wahl or Maciejewski is a liar (i.e., it follows that $\neg T(a, Maciejewski, Wahl)$ ).

## 7.4. Representing Expressives

The point of an expressive, $Express(\alpha, \beta)(\Phi)$ , is to 'express the speaker's attitude about the state of affairs that $P'$ [Searle and Venderveken (1986, p. 58)]. Attitudes that may be expressed include approving, deploring, and welcoming. Let:

Express(w, x, y, z):: In world w, speaker x's expressive to y of type z succeeds.

approval

$$
\begin{array}{r l}&\text { Then }\\&(\forall w) (A (a ^ {*}, w) \land E x p r e s s (w, \alpha , \beta , a p p r o v a l)\\&\qquad \rightarrow \mathbf {R e l} (\Phi , w)),\end{array}\tag {7.4.1}
$$

says that $\alpha$ express approval of $\Phi$ to $\beta$ . Clearly, (7.4.1) could be generalized and extended in a manner similar to (1.1).

## 7.5. Iteration of Attitudes, Third-Party Attitudes

The various illocutionary forces are examples of what are called propositional attitudes. Promising and asserting are two different attitudes that might be taken by the same person towards the same proposition, $\Phi$ , producing quite different statements. To promise that it will rain is very different than asserting that it will rain. By using conditioning, indexing, and relativization, we have been able to achieve representation of five different, basic propositional attitudes, and by continuing in this fashion could represent other attitudes as well. But there is more.

Attitudes may be iterated, just as modal operators may be iterated (see Appendix 2). For example, Janet may promise Joy to tell Gloria that there is beer in the refrigerator. Adverting to our (sketched) working language, we might then have:

$$
\text { Prom } (J a n e t, J o y)
$$

$$
(A s s e r t (J a n e t, G l o r i a) (B e e r i s i n t h e f r i g)).
$$

Here, promising and asserting are iterated attitudes. There is no particular reason to stop with two iterations; any finite combination could in principle be permitted. Happily, our translation rules are fully recursive. They implicitly specify arbitrary iterations of the attitudes they cover.

A second category of complexity may be described as third-party attitudes. Normally, the speaker takes an attitude towards a proposition that directly involves the hearer. For example, 'I promise to meet you for lunch' is a stylistic variant of 'I promise you that I will meet you for lunch', but it is quite possible to make a different promise: 'I promise you that I will meet Milan for lunch', where you and Milan are different. Milan is the third party. Promises of this sort are much-discussed in the theory of contract law and may be characterized as follows.

In these cases A promises B (let us assume for good consideration) that A will render a benefit to C. [Fried (1981, p. 44)].

Clearly, the representation schemes offered here need no stretching to accommodate third-party attitudes.

The expressive power of these schemes is indeed ample.

## 8. Conclusion

Much remains to be learned about the problem of formal representations for promising. Even assuming that asserting, declaring, directing, and expressing (plus promising or committing) span the set of illocutionary points, still more remains to be learned about how to represent them. Much remains to be learned about the (possible world) accessibility relations appropriate for promising and other attitudes. It is far from clear what these relations should be, or even whether they are common or distinct among attitudes. Further, while I have sketched an approach (cf. (5.2)) for handling validity conditions – How do we enforce that promises must be made only for future conditions? etc. – much remains to be learned about what these validity conditions are. I suggest that a good way of proceeding from here would be to develop models and test prototypes for actual problem domains. Electronic contracting under the Uniform Commercial Code and enhanced electronic mail services are, if I may say so, especially promising application areas.

Before closing, I want to address one more theoretical issue, the need for defeasible or non-monotonic reasoning in these applications.

McCarthy (1982) seems to have been the first to publish the idea of developing a language, rather than a protocol, for business communications. In commenting on his proposals, he has written [McCarthy (1986)] that:

To me the most problematic aspects of the problem (of developing a machine-readable language for business communications) were associated with the non-monotonic aspects of communication, especially business communication. Much is inferred from what is left out of a message, and these non-monotonic inferences have even legal force. For example, if the means of delivery isn't specified, then any standard method will do.

How should we handle under-specified promises? What shall our defaults be and under what conditions should they be invoked? If we are to invoke defaults, then we must have a way of revoking (or defeating) them. We need nonmonotonic reasoning of some sort. I argued above that the connection between promising that $\Phi$ and being obliged that $\Phi$ is also defeasible (and hence nonmonotonic). Should the defeasible reasoning process for obligation be the same as that for, e.g., under-specified promises? These are important and unsolved problems, both generally and for the specific application problem of developing a formal language for business communication. And they are problems beyond the scope of this paper. Nonetheless there are two points worth making.

First, the need for nonmonotonic reasoning in the envisioned applications may not be overriding and perhaps can be circumvented. Unstructured situations, such as conversation in natural language or under-specified promises, are one source of the need for nonmonotonic reasoning, but it may well be that the intended contexts – certain inter- and intra-organizational business communications – can be made sufficiently structured that the need for default reasoning is minimized or eliminated. This is a live possibility, which future research will have to explore. The other present source of need for nonmonotonic reasoning, defeasible connections between promising and obligations, may be circumventable. Under the representation schemes I have proposed, it is possible to infer (and correctly so) such things as whether a given promise has been broken, whether not doing $\Phi$ will result in breaking a promise, and so on. It is, I say, very useful to have a machine that is able to reason about promises, whether or not it can also reason about the obligations entailed by those promises. Half a loaf may be plenty.

Second, even if we must face the full force of the problem of nonmonotonic reasoning, the representation schemes presented here are unlikely to be vitiated as a consequence. It is one thing to make a promise and another to reason about the fact that it normally entails a certain obligation. This paper is mainly about the former. That the representations proposed allow the propositional contents of promises to be extracted in predicate logic form can only be an advantage when developing a method of reasoning nonmonotonically about the promises.

In conclusion, the exciting prospect of developing a machine-readable language for business communications presents a series of difficult problems. Important benefits would be had if the language were expressible in first-order logic. I have proposed a series of representation schemes for promising – and have suggested schemes for asserting, declaring, directing, and expressing – that have unequivocal translations into FOL. These representation schemes are motivated by theory and have felicitous formal properties, but investigation of the schemes cannot be said to be complete and must be the subject of future research.

## Appendix 1: Relativization and Possible Worlds

We are after an algorithm for translating an arbitrary formula in a particular source language, $l_{s}$ , to a particular target language, $l_{t}$ . All the target languages I shall discuss here are languages of FOL, each of which contains two predicates and a term constant, all assumed not to be present in the source languages:

$A(u,v)$ :: World $v$ is accessible from world $u$ .

$In(x, w)::$ Individual x exists in world w.

$a^{*}$ :: The actual world.

(Further, the target language adds a sort - possible worlds - so the sorts in the source language, although this is not strictly required.) The idea is that if $\Phi$ is a formula in the source language, then $\operatorname{Trans}(\Phi)$ is a formula with the same truth value but in the target language (i.e., in FOL). Further, we say:

$$
\operatorname{Trans} (\Phi) = \operatorname{Rel} (\Phi , a ^ {*}),\tag{A1.1}
$$

and call the right-hand side the relativization of $\Phi$ with respect to $a^{*}$ . Thus, giving an algorithm for Rel is giving an algorithm for Trans, and this is what I shall do. The algorithm I shall give is a generalization and extension of that given in Forbes (1985) for modal system S5 (and limited to S5). As we shall see below, the relativization algorithm given here can be used for a variety of modal systems - including S5 - and for other purposes as well, viz. translating promise expressions into FOL.

Two further points before specifying Rel. The first point is a technical matter of some theoretical importance. It is an open question (at least to me)

whether the translation we employ should encompass counterpart theory [Lewis (1968, 1983)]. The Rel as I am giving it does not produce counterpart-theoretic statements in FOL, but the modification required to do so is trivial and does not affect the basic results I have presented. This fact, and that the representation without counterpart theory is somewhat simpler, seems to me sufficient reason to present Rel without counterpart theory. No generality is lost.

The second point is a matter of notation. I will use lower case Greek letters as metalinguistic variables ranging over individual terms and upper case Greek letters as metalinguistic variables ranging over predicates. Distinct metalinguistic variables are to be instantiated by distinct object language terms or predicates to obtain well-formed formulas in the object language.

The definition of relativization is recursive and goes as follows:

1. If $\Phi(\tau_1, \ldots, \tau_n)$ with $n \geqslant 0$ , is an atomic formula (with $\tau_i$ either a free variable or a constant), then $\operatorname{Rel}(\Phi(\tau_1, \ldots, \tau_n), \xi) = \Phi(\tau_1, \ldots, \tau_n, \xi)$ .

2. $\operatorname{Rel}(\Phi \wedge \Psi, \xi) = \operatorname{Rel}(\Phi, \xi) \wedge \operatorname{Rel}(\Psi, \xi)$ .

3. $\mathbf{Rel}(\Phi \vee \Psi, \xi) = \mathbf{Rel}(\Phi, \xi) \vee \mathbf{Rel}(\Psi, \xi)$ .

4. $\operatorname{Rel}(\Phi \to \Psi, \xi) = \operatorname{Rel}(\Phi, \xi) \to \operatorname{Rel}(\Psi, \xi)$ .

5. $\operatorname{Rel}(\Phi \leftrightarrow \Psi, \xi) = \operatorname{Rel}(\Phi, \xi) \leftrightarrow \operatorname{Rel}(\Psi, \xi)$ .

6. $\mathbf{Rel}(\neg \Phi, \xi) = \neg \mathbf{Rel}(\Phi, \xi)$ .

7. $\operatorname{Rel}(\mathbf{L}\Phi, \xi) = (\forall \sigma)(\mathbf{A}(\xi, \sigma) \to \operatorname{Rel}(\Phi, \sigma)).$

8. $\operatorname{Rel}(\mathbf{M}\Phi, \xi) = (\exists \sigma)(\mathrm{A}(\xi, \sigma) \wedge \operatorname{Rel}(\Phi, \sigma))$ .

9. $\operatorname{Rel}(\tau_i = \tau_j, \xi) = (\tau_i = \tau_j)$ .

10. $\mathbf{Rel}((\forall \tau)\bar{\Phi} (\tau),\xi) = (\forall \tau)(In(\tau ,\xi)\to$ $\mathbf{Rel}(\varPhi (\tau),\xi)).$

11. $\operatorname{Rel}((\exists \tau)\Phi (\tau),\xi) = (\exists \tau)(In(\tau ,\xi)\wedge$ $\operatorname {Rel}(\Phi (\tau),\xi)).$

Given this translation algorithm, via relativization, we can represent systems of modal logic in FOL. I shall now discuss five of them.

## System K

Modal system K (for sentence logic) contains one axiom and one rule of inference, beyond those needed for PC. The axiom is:

$$
\mathbf {L} (\Phi \rightarrow \Psi) \rightarrow (\mathbf {L} \Phi \rightarrow \mathbf {L} \Psi).\tag{K}
$$

If we relativize (K) we get:

$$
\begin{array}{r l} & {(\forall w) \big (A (a ^ {*}, w) \to (\Phi (w) \to \Psi (w))} \\ & {\qquad \to ((A (u) (A (a ^ {*}, u) \to \Phi (u))} \\ & {\qquad \to (A (v) (A (a ^ {*}, v) \to \Psi (v))).} \end{array}\tag{K-rel}
$$

It is easy to prove that (K-rel) is a tautology in FOL.

The added rule of inference in system K is called the rule of necessitation:

Rule of necessitation. If $\vdash\Phi$ , then $\vdash L\Phi$ . (In words, if $\Phi$ is a tautology, then so is $L\Phi$ .)

The rule of necessitation is a frequent source of confusion. It appears to be validating the formula, $\Phi \to \mathbf{L}\Phi$ , but it is not. An advantage of the FOL translation is that in the translation it is easy to see that the rule is correct. In fact, it reduces to a tautology in FOL and hence can be dropped. To see this, note that if $\Phi$ is a tautology (i.e., if $\vdash \Phi$ ) then so is $\operatorname{Rel}(\Phi, w)$ for all $w$ . But, then so is $\operatorname{Rel}(\mathbf{L}\Phi, a^{*}) = (\forall w)(A(a^{*}, w) \to \operatorname{Rel}(\Phi, w))$ . In sum, the translation scheme given above produces an FOL equivalent of modal system K.

## System T

Modal system T is K plus the T axiom:

$$
\mathbf {L} \Phi \rightarrow \Phi .\tag{T}
$$

In the semantics for system T, the accessibility relation is reflexive, but non-transitive and nonsymmetric. It is easy to show that if we add

$$
(\forall w) A (w, w),\tag{TA}
$$

as a premise, then Trans((T)) can be proved in FOL. Conversely, (T) implies reflexivity of the accessibility relation, for if we have (T) and we assume that the accessibility relation is not transitive, then it is possible to specify a model that gives inconsistent evaluations. For example, suppose that our (modal sentence logic) model has two worlds, $a$ and $b$ , with $\neg P$ true at $a$ and $P$ true at $b$ . Further, the specified accessibility relation is that $b$ is accessible from $a$ and from itself. Thus, there is one world, $a$ , that is not accessible to itself, i.e., not all worlds are accessible to themselves. Assume (T) as an axiom. What is true in this model? Note that the value of $\neg P$ at $a$ is $\top$ (i.e., $\mathbf{Value}(\neg P, a) = \top$ ), since $\neg P$ is true at world $a$ . Further, note that $\mathbf{Value}(\mathbf{L}P, a) = \top$ , since the value of $P$ is $\top$ in every world accessible from $a$ (i.e., in $b$ ). But, by (T) and LP we have it that the value of $P$ is $\top$ in $a$ , and hence we have a contradiction.

System S4

Modal system S4 is T plus the S4 axiom:

$$
\mathbf {L} \Phi \rightarrow \mathbf {L L} \Phi .\tag{S4}
$$

In the semantics for system S4, the accessibility relation is reflexive and transitive, but non-symmetric. It is easy to show that if we add

$$
\begin{array}{r l}&(\forall w) (A (w, w)), \quad \text {(TA)}\\&(\forall u) (\forall v) (\forall w) (A (u, v) \land A (v, w) \rightarrow A (u, w)), \quad \text {(S4A)}\end{array}
$$

as premises, then Trans((S4)) can be proved in FOL.

Conversely, (T) and (S4) imply reflexivity and transitivity of the accessibility relation, for if we have (T) and (S4) and we assume that the accessibility relation is reflexive but not transitive, then it is possible to specify a model that gives inconsistent evaluations. For example, suppose that our (modal sentence logic) model has three worlds, $a$ , $b$ , and $c$ , with $P$ true at $a$ and $P$ true at $b$ , and $\neg P$ true at $c$ . Further, the specified accessibility relation is that $b$ is accessible from $a$ , $c$ is accessible from $b$ , and every worlds is accessible from itself. Thus, there is one world, $c$ , that is not accessible to $a$ , i.a., not all worlds are in a transitive accessibility relation. Assume (T) and (S4) as axioms. What is true in this model? Note that the value of $P$ at $a$ is $\top$ (i.e., $\text{Value}(P, a) = \top$ ), since $P$ is true at world $a$ . Repeating and continuing, note that:

1. Value $(P, a) = \top$ . ( $P$ is true at $a$ .)

2. Value $(P, b) = \top$ . ( $P$ is true at $b$ .)

3. Value $(P, c) = \bot$ . ( $P$ is false at $c$ .)

5. Value(LP, b) = $\bot$ .
(P is not true in some world accessible from
b.)

6. Value(LLP, a) = ⊥.
(Value(LP, b) = ⊥ and b is accessible from a.)

7. Value(LLP, a) = T.
(By 4 and (S4).)

## System B

Modal system B is T plus the B axiom:

$$
\Phi \rightarrow \mathbf {L M} \Phi .\tag{B}
$$

In the semantics for system B, the accessibility relation is reflexive and symmetric, but non-transitive. It is easy to show that if we add

$$
(\forall w) (A (w, w)),\tag{TA}
$$

$$
(\forall u) (\forall v) (A (u, v) \leftrightarrow A (v, u)),\tag{BA}
$$

as premises, then Trans((B)) can be proved in FOL.

Conversely, (T) and (B) imply reflexivity and symmetry of the accessibility relation, for if we have (T) and (B) and we assume that the accessibility relation is reflexive but not symmetric, then it is possible to specify a model that gives inconsistent evaluations. For example, suppose that our (modal sentence logic) model has two worlds, $a$ and $b$ , with $P$ true at $a$ and $\neg P$ true at $b$ . Further, the specified accessibility relation is that $b$ is accessible from $a$ , and every world is accessible from itself. Thus, there is one world, $a$ , that violates the symmetric accessibility relation. Assume (T) and (B) as axioms. What is true in this model? Note that the value of $P$ at $a$ is $\top$ (i.e., $\text{Value}(P, a) = \top$ ), since $P$ is true at world $a$ . Repeating and continuing, note that:

1. Value $(P, a) = \top$ .

$(P$ is true at $a$ .)

2. Value $(P, b) = \bot$ .

(P is false at b.)

3. Value(MP, b) = ⊥.

(P is false at every world accessible from b.)

4. Value(LMP, a) = $\perp$ .

(MP is false at some world accessible from a.)

5. Value(LMP, a) = T.

(By Value(P, a) = T and (B).)

## System S5

Modal system S5 is T plus the S5 axiom:

$$
\mathbf {M} \Phi \rightarrow \mathbf {L M} \Phi .\tag{S5}
$$

In the semantics for system S5, the accessibility relation is reflexive, symmetric and transitive. It is easy to show that if we add

$$
(\forall w) (A (w, w)),
$$

$$
(\forall u) (\forall v) (A (u, v) \leftrightarrow A (v, u)),\tag{TA}
$$

$$
(\forall u) (\forall v) (\forall w)\tag{BA}
$$

$$
\big (A (u, v) \wedge A (v, w) \rightarrow A (u, w) \big),\tag{S4A}
$$

as premises, then Trans((S5)) can be proved in FOL.

Conversely, (T) and (S5) imply reflexivity, symmetry, and transitivity of the accessibility relation. Showing that (T) and (S5) imply (B) is trivial. Further, if we have (T) and (S5) and we assume that the accessibility relation is reflexive and symmetric, but not transitive, then it is possible to specify a model that gives inconsistent evaluations. For example, suppose that our (modal sentence logic) model has three worlds, $a$ , $b$ and $c$ , with $P$ false at $a$ and $b$ , and $P$ true at $c$ . Further, the specified accessibility relation is that $b$ is accessible from $a$ , $c$ is accessible from $a$ , accessibility is symmetric and every world is accessible from itself. The accessibility relation is not transitive, since $a$ is accessible from $b$ and $c$ is accessible from $a$ , but $c$ is not accessible from $b$ . Assume (T) and (S5) as axioms. What is true in this model? Note that the value of $P$ at $a$ is $\perp$ (i.e., $\text{Value}(P, a) = \perp$ ), since $\neg P$ is true at world $a$ . Repeating and continuing, note that:

1. Value $(P, a) = \bot$ .

$(P$ is false at $a$ .)

2. Value $(P, b) = \bot$ .

3. Value $(P, c) = \top$ .

$(P$ is true at $c$ .)

4. Value(MP, a) = T.

(P is true at some world accessible to a, i.e., c.)

5. Value(LM P, a) = ⊥.

(MP is false at some world accessible to a, i.e., b.)

6. Value(LM $p, a) = \top$ .

(By 4 and (S5).)

## Appendix 2: Proof of Theoretic Equivalents of Worlds Table 1

A collection of modal axioms for which Worlds Table 1

Worlds Table 1

<table><tr><td>world</td><td>H</td><td>W</td><td>R</td><td>direct access to</td></tr><tr><td>1</td><td> $\top$ </td><td> $\top$ </td><td> $\top$ </td><td>out</td></tr><tr><td>2</td><td> $\top$ </td><td> $\top$ </td><td> $\bot$ </td><td>nil</td></tr><tr><td>3</td><td> $\top$ </td><td> $\bot$ </td><td> $\top$ </td><td>nil</td></tr><tr><td>4</td><td> $\top$ </td><td> $\bot$ </td><td> $\bot$ </td><td>3, 2</td></tr><tr><td>5</td><td> $\bot$ </td><td> $\top$ </td><td> $\top$ </td><td>out</td></tr><tr><td>6</td><td> $\bot$ </td><td> $\top$ </td><td> $\bot$ </td><td>2</td></tr><tr><td>7</td><td> $\bot$ </td><td> $\bot$ </td><td> $\top$ </td><td>3</td></tr><tr><td>8</td><td> $\bot$ </td><td> $\bot$ </td><td> $\bot$ </td><td>7, 6, 4</td></tr></table>

serves as a model is as follows, with A1 describing the actual world for this model.

A1. $(\neg W \land \neg H \land \neg R)$ .  
A2. $(\neg W \land \neg H \land \neg R) \to \mathbf{M}(\neg W \land \neg H \land R)$ .  
A3. $(\neg W \land \neg H \land \neg R) \to \mathbf{M}(\neg W \land H \land \neg R)$ .  
A4. $(\neg W \land \neg H \land \neg R) \to \mathbf{M}(W \land \neg H \land \neg R)$ .  
A5. $\mathbf{M}(W \land \neg H \land \neg R) \to \mathbf{MM}(W \land H \land \neg R)$ .  
A6. $\mathbf{M}(\neg W \land H \land \neg R) \to \mathbf{MM}(W \land H \land \neg R)$ .  
A7. $\mathbf{M}(\neg W \land H \land \neg R) \to \mathbf{MM}(\neg W \land H \land R)$ .  
A8. $\mathbf{M}(\neg W \land \neg H \land R) \to \mathbf{MM}(\neg W \land H \land R)$ .  
A9. $\mathbf{L}(W \to \mathbf{L}W)$ .  
A10. $\mathbf{L}(H \to \mathbf{L}H)$ .  
A11. $\mathbf{L}(R \to \mathbf{L}R)$ .

Briefly, the meaning of these axioms is as follows. A1 designates the actual world, world 8. Axioms A2–4 state that worlds 7, 4, and 6 are directly accessible to 8. World 2 is accessible (is possible) from world 6, but world 6 – being one arc away from the actual world – is at best possible, thus world 2 is possibly possible from world 8. That is what A5 says; similarly for A6–8. A9 says, roughly, that once you have W you are stuck with it; similarly for A10–11. Note that

Trans(A9)

$$
\begin{array}{r l}&= (\forall u) \big (A (a ^ {*}, u)\\&\quad \rightarrow (W u \rightarrow (\forall v) (A (u, v) \rightarrow W v)) \big),\end{array}\tag{A2.1}
$$

which has a meaning that is much clearer.

We want the accessibility relation to be both reflexive and transitive, but not symmetric. (For example, world 2 should be possible from world 8, but not vice versa.) These conditions describe modal system S4, as noted in Appendix 1. In carrying out proofs – e.g., that world 2 is accessible from world 8 – either in S4 or the FOL translation of it, the reader will easily see that the reflexivity and transitivity assumptions are used essentially.

Next, let us consider the case with world 6 actual. The revised axioms are as follows.

A21. $(W \land \neg H \land \neg R)$ .
A22. $\mathbf{M}(\neg W \land \neg H \land \neg R) \rightarrow \mathbf{MM}(\neg W \land \neg H \land R)$ .
A23. $\mathbf{M}(\neg W \land \neg H \land \neg R) \rightarrow \mathbf{MM}(\neg W \land H \land \neg R)$ .
A24. $\mathbf{LM}(W \land \neg H \land \neg R) \rightarrow \mathbf{M}(\neg W \land \neg H \land \neg R)$ .
A25. $(W \land \neg H \land \neg R) \rightarrow \mathbf{M}(W \land H \land \neg R)$ .
A26. $\mathbf{MM}(\neg W \land H \land \neg R) \rightarrow \mathbf{MMM}(W \land H \land \neg R)$ .
A27. $\mathbf{MM}(\neg W \land H \land \neg R) \rightarrow \mathbf{MMM}(\neg W \land H \land R)$ .
A28. $\mathbf{MM}(\neg W \land \neg H \land R) \rightarrow \mathbf{MMM}(\neg W \land H \land R)$ .
A29. $L(W \rightarrow LW)$ .
A30. $L(H \rightarrow LH)$ .
A31. $L(R \rightarrow LR)$ .

It is easy to see - either in S4 or the FOL translation - that this system behaves well. $W$ is here necessary, since it is true in all worlds accessible from the actual world (6 and 2). Given A21 and A29, LW follows easily, but if the accessibility relation were symmetric (e.g., if we used S5 instead of S4), then A21-31 would result in an inconsistency. As it is, with S4 (or the translation of all this) no inconsistency obtains.

Finally, a word about providing axioms for worlds tables. We can think of such a table as specifying a directed graph, with worlds as nodes and (direct) accessibility represented by arcs between nodes. Since world 7 is directly accessible from world 8 (in Worlds Table 1), there is an arc from 8 to 7. Define the distance of a world, w, from $a^{*}$ as follows. Ignoring the direction of the arcs, $d(a^{*}, w) = \text{the minimum number of arcs that need to be traversed in going from } a^{*} \text{ to } w$ . (Distance is undefined for worlds not connected to $a^{*}$ .) Then, for every from-node, $N_{f}$ , for which its to-node, $N_{t}$ , is not on a shortest path from $a^{*}$ to $N_{f}$ , add an axiom of the form:

$$
\mathbf {M} _ {d (a ^ {*}, N _ {f})} \left(c (N _ {f})\right)\rightarrow \mathbf {M} _ {d (a ^ {*}, N _ {f}) + 1} \left(c (N _ {t})\right),\tag{*}
$$

where $c(\nu)$ is the content of node $\nu$ (e.g., $c(2)$ is $(W \wedge H \wedge \neg R))$ and $\mathbf{M}_{\delta}$ is $\delta$ iterated $\mathbf{Ms}$ (e.g., $\mathbf{M}_{3}R = \mathbf{MMM}R$ ).

If the to-node is on every shortest path to $N_{f}$ (and hence the arc points back towards $a^{*}$ ), add

an axiom of the form:

$$
\mathbf {L M} _ {d (a ^ {*}, N _ {f})} \big (c (N _ {t}) \big) \rightarrow \mathbf {M} _ {d (a ^ {*}, N _ {f})} \big (c (N _ {f}) \big). \quad (* *)
$$

Slight reflection on the Browerian axiom (B, in Appendix 1) will show that this procedure for handling incoming arcs is correct.

## Appendix 3: Definition of the Index Function

The purpose of the index function is simply to add an argument to each predicate in a source language formula. The definition of the index function is recursive and goes as follows:

1. If $\Phi(\tau_1, \ldots, \tau_n)$ with $n \geqslant 0$ , is an atomic formula (each $\tau_i$ a term), then $\mathbf{Index}(\Phi(\tau_1, \ldots, \tau_n), \iota) = \Phi(\tau_1, \ldots, \tau_n, \iota)$ .

2. $\operatorname{Index}(\Phi \wedge \Psi, \iota) = \operatorname{Index}(\Phi, \iota) \wedge \operatorname{Index}(\Psi, \iota)$ .

3. $\operatorname{Index}(\Phi \vee \Psi, \iota) = \operatorname{Index}(\Phi, \iota) \vee \operatorname{Index}(\Psi, \iota)$ .

4. $\operatorname{Index}(\Phi \to \Psi, \iota) = \operatorname{Index}(\Phi, \iota) \to \operatorname{Index}(\Psi, \iota)$ .

5. $\operatorname{Index}(\Phi \leftrightarrow \Psi, \iota) = \operatorname{Index}(\Phi, \iota) \leftrightarrow \operatorname{Index}(\Psi, \iota)$ .

6. $\operatorname{Index}(\neg \Phi, \iota) = \neg \operatorname{Index}(\Phi, \iota)$ .

$$
\operatorname{Index} (\mathbf {L} \Phi , \iota) = \mathbf {L} (\operatorname{Index} (\Phi , \iota)).
$$

8. Index(MΦ, ι) = M(Index(Φ, ι)).

9. Index $(\tau_{i} = \tau_{j},\iota) = (\tau_{i} = \tau_{j})$

10. $\mathbf{Index}((\forall \tau)\Phi (\tau),\iota) = (\forall \tau)(\mathbf{Index}(\Phi (\tau),\iota)).$

11. $\operatorname{Index}((\exists \tau)\Phi (\tau),\iota) = (\exists \tau)(\operatorname{Index}(\Phi (\tau),\iota)).$

## Appendix 4: Translation Algorithm for Temporal Operators

For present purposes, I will limit the discussion to three temporal operators:

$T_{-}at(\Phi, \tau)$ :: $\Phi$ is true at time $\tau$ .

$T\_before(\Phi, \tau) :: \Phi \text{ is true at or before time } \tau.$

$T\_after(\Phi, \tau)$ :: $\Phi$ is true at or after time $\tau$ .

The translation scheme is as follows:

1. $\operatorname{Trans}(T\_ at(\Phi, \tau)) = \operatorname{Index}(\Phi, \tau)$ .

2. $\operatorname{Trans}(T_{-}before(\Phi, \tau_0)) = (\exists \tau)(\operatorname{Index}(\Phi, \tau) \wedge \tau \leqslant \tau_0)$ .

3. Trans $(T_{-}after(\Phi, \tau_0)) = (\exists \tau)(\text{Index}(\Phi, \tau) \wedge \tau \geqslant \tau_0)$ .

## References

Bhargava, Hemant K. and Steven O. Kimbrough, On Embedded Languages for Model Management, Proceedings of the 23rd Hawaii International Conference on System Sciences (1990).

Chellas, Brian F., Modal Logic: An Introduction (Cambridge University Press, Cambridge, 1980).

Crowston, Kevin, Thomas W. Malone and Felix Lin, Cognitive Science and Organizational Design: A Case Study of Computer Conferencing, Working Paper No. 144 (Massachusetts Institute of Technology, Center for Information Systems Research, November 1986).

Dennett, Daniel C., The Intentional Stance, A Bradford Book (MIT Press, Cambridge, MA, 1987).

Dretske, Fred I., Knowledge and the Flow of Information, A Bradford Book (MIT Press, Cambridge, MA, 1981).

Ellis, Brian, Rational Belief Systems (Blackwell, Oxford, 1979).

Flanagan, Owen J., Jr., The Science of the Mind, A Bradford Book (MIT Press, Cambridge, MA, 1984).

Fodor, Jerry A., Psychosemantics: The Problem of Meaning in the Philosophy of Mind, A Bradford Book (MIT Press, Cambridge, MA, 1987).

Forbes, Graeme, The Metaphysics of Modality (Clarendon Press, Oxford, 1985).

Fried, Charles, Contract as Promise: A Theory of Contractual Obligation (Harvard University press, Cambridge, MA, 1981).

Hughes, G.E. and M.J. Cresswell, An Introduction to Modal Logic (Methuen, London, 1968).

Hume, David, A Treatise of Human Nature (Clarendon Press, Oxford, 18888 (reprinted 1968)).

Kimbrough, Steven O., Ronald M. Lee and David Ness, Performative, Informative, and Emotive Systems: The First Piece of the PIE, in: Leslie Maggie, ed., Proceedings of the Fifth International Conference on Information Systems (1984) 141–148.

Kimbrough, Steven O. and Ronald M. Lee, On Illocutionary Logic as a Telecommunications Language, in: Leslie Maggie, Robert Zmud, and James Wetherbe, eds., Proceedings of the Seventh International Conference on Information Systems (1986).

Kimbrough, Steven O. and Fred Adams, Why Nonmonotonic Logic?, Decision Support Systems 4 (1988) 111–27.

Kimbrough, Steven O. and Michael B. Thornburg, On Semantically-Accessible Messaging in an Office Environment, Proceedings of the Twenty-Second Hawaii International Conference on System Sciences (1989).

Lewis, David, Counterpart Theory and Quantified Modal Logic, Journal of Philosophy, 65 (1968) 113–126; reprinted in David Lewis, Philosophical Papers, Vol. I (Oxford University Press, Oxford, 1983).

Lyytinen, Kalle, SAMPO Project Final Report: 1983–1985 (Department of Computer Science, University of Jyvaskyla, SF-40 100 Jyvaskyla, Finland, 1986).

Lyytinen, Kalle, Different Perspectives on Information Systems: Problems and Solutions, ACM Computing Surveys 19, No. 1 (March 1987) 5–46.

Mackie, J.L., Problems of Intentionality, in: Joan Mackie and Penelope Mackie, eds., Logic and Knowledge, Selected Papers, Vol. I (Clarendon Press, Oxford, 1985).

Malone, Thomas W., Kenneth R. Grant, Kum-Yew Lai, Ramana Rao and David Rosenblitt, Semistructured Messages Are Surprisingly Useful for Computer-Supported Coordination, ACM Transactions on Office Information Systems 5, No. 2 (April 1987).

Malone, Thomas W., Kenneth R. Grant, Franklyn A. Turbak, Stephen A. Brobst and Michael D. Cohen, Intelligent Information-Sharing Systems, Communications of the ACM 30, no. 5 (May 1987) 390–402.

McCarthy, John, The Common Business Communication Language, in: Albert Endres and Jürgen Reetz, eds. Textverarbeitung und Bürosysteme (R. Oldenbourg Verlag, Munich and Vienna, 1982).

McCarthy, John, personal communication (December 17, 1986).

Moore, Robert C., The Role of Logic in Artificial Intelligence, Working Paper, Report No. CSLI-85-33 (Center for the Study of Language and Information, September 1985).

Putnam, Hilary, The Many Faces of Realism (Open Court, LaSalle, IL, 1987).

Quine, V.W., Word and Object (MIT Press, Cambridge, MA, 1960).

Searle, John R., A Taxonomy of Illocutionary Acts, in: Keith Gunderson, ed., Language, Mind, and Knowledge, Minnesota Studies in the Philosophy of Science, Vol. III (Uni-

versity of Minnesota Press, Minneapolis, MN, 1975); reprinted in John R. Searle, Expression and Meaning, Studies in the Theory of Speech Acts (Cambridge University Press, Cambridge, 1979).

Searle, John R., Intentionality: An Essay in the Philosophy of Mind (Cambridge University Press, Cambridge, 1983).

Searle, John R. and Daniel Vanderveken, Foundations of Illocutionary Logic (Cambridge University Press, Cambridge, 1985).

Tiersma, Peter M., The Language of Offer and Acceptance: Speech Acts and the Question of Intent, California Law Review 74 (1986) 189–232.

van Fraasen, Bas, Formal Semantics and Logic (Macmillan, New York, 1971).

Von der Lieth Gardner, An Artificial Intelligence Approach to Legal Reasoning (MIT Press, Cambridge, MA, 1987).

Von Wright, G.H., On Promises, Theoria 28 (1962) 276–97; reprinted in von Wright, G.H., Practical Reason, Philosophical Papers, Vol. I (Cornell University Press, Ithaca, NY, 1983).

Winograd, Terry, A Language/Action Perspective on the Design of Cooperative Work, Proceedings of the Conference on Computer Supported Cooperative Work (Austin, TX, December 3–5, 1986) 203–220.

Winograd, Terry and Fernando Flores, Understanding Computers and Cognition: A New Foundation for Design (Ablex Publishing Company, Norwood, NJ, 1986).
