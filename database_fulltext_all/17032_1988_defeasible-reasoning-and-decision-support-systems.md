---
otero_id: 17032
otero_key: "H4UP2M9P"
title: "Defeasible reasoning and decision support systems"
authors: "Donald Nute"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90100-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Defeasible Reasoning and Decision Support Systems $^{1}$

Donald NUTE

Department of Philosophy, Advanced Computational Methods Center, University of Georgia, Athens, GA 30602, USA

![](/api/attachments/H4UP2M9P/fulltext/images/2de311fac1a3b106afd81dad4fa64ac26dd6ed6ba182f3a0359d676dbbe1302d.jpg)

Donald Nute is professor of philosophy and director of the MS program in artificial intelligence at the University of Georgia. He received a B.A. in philosophy and mathematics from the University of Kentucky in 1969, and a Ph.D. in philosophy from Indiana University in 1974. His research interests lie in logic, logic programming, automated reasoning, natural language understanding, and expert systems.

$^{1}$ This paper is a revision and an extension of Nute [1987]. If owe thanks to many people for helpful discussions and comments, but especially to Marvin Belzer, Michael Covington, Dov Gabbav, Michael Lewis, and Franz Guenther. The research reported here was supported by NSF Grant #IST-8505586 and by the Research Center for Natural Language Systems (FNS), Universität Tübingen.

## 1. Introduction

Our reasoning often leads to conclusions that are later ‘defeated’ by new information. We can often provide reasons for our defeasible conclusions in the form of simply stated rules-of-thumb. These rules apply to normal or typical cases, but they may be defeated by evidence that the case before us is not typical. In this paper, we will examine this kind of defeasible reasoning and look at ways to implement it in an automated reasoning system.

Perhaps the two methods that have been used most often to try to capture the kind of reasoning we will investigate are probabilistic approaches and approaches that require us to explicitly list all exceptions as conditions for a rule. Neither of these approaches, I shall argue, give us a natural representation of many simple and ordinary patterns of defeasible reasoning. A better method is needed.

To get a better understanding of what a proper account of defeasible reasoning requires, we will look at how we resolve conflicts involving rules-of-thumb that give us contradictory advice. Some promising formal systems look like they may offer ways to represent these defeasible rules. These include certain conditional logics, default logics, belief revision systems and nonomonotonic logics that have been described in the literature. In the end, none of these gives us the results that our investigation of conflicts between competing rules-of-thumb leads us to expect.

In the rest of the paper I will develop a new logic for defeasible reasoning, a semantics for this logic, and an extension of the logic programming language Prolog based on an extension of this logic. This new logic distinguishes between facts and presumptions, and between absolute rules and defeasible rules. It also introduces another special kind of very weak rule called a defeater. The semantics for this logic provides compliance conditions for sets of rules, where a compliance condition for a set of inference rules determines the belief states a system (a person or a computing system) that accepts all the rules in the set could be in.

I develop a sentential logic for the sake of simplicity. A quantified extension of this logic has been incorporated into an extension of Prolog. This Prolog extension is described, together with prototype expert systems under development in it.

## 2. Defeasible Reasoning

We can be certain about many things. When we look at an apple and see its color, we are certain that it is red or yellow or green. When we taste it, we know that it is sweet or tart. We can be sure that all penguins are birds, that no bachelor is married, and that oxygen is consumed when a match is burned. What we consider to be certain knowledge includes both particular facts that we observe and general rules that we are confident have no exceptions. But much that we believe or even claim to know is less than certain. Often we accept something on the basis of good evidence full well knowing that the evidence we have is less than conclusive. Whenever we do this, we take a risk that new evidence might be uncovered that will force us to revise our beliefs or expectations.

When some new fact causes us to reject a prior conclusion, we will say that the conclusion together with the reasoning that gave rise to it are defeated. Any bit of reasoning that could in principle be defeated by further information we will call defeasible reasoning.

Very often when we arrive at a risky conclusion based on available evidence, we can provide justification in the form of a warrant or rule for accepting the conclusion. A physician may say that penicillin is effective in treating pneumonia, but she will not give penicillin to a patient who is allergic to it. A financial advisor might say that an IRA offers a good way to shelter income from taxes, but he will not recommend contributing to an IRA if the investor will need to withdraw the funds after a short period of time and before retirement. On a mundane level, we expect the bread to toast when we put it in the toaster, we expect the morning drive to work to take a certain amount of time, and we expect our friends to keep their luncheon engagements, but we know that power outages interfere with toasters, that flat tires make us late to work, and that personal emergencies prevent friends from keeping their luncheon dates. Each of these rules-of-thumb that guide our decisions can be defeated by special circumstances. Consequently, we can call these principles defeasible rules.

Human beings, whether laymen or experts, normally base their opinions on best evidence even when they would admit that their evidence is not conclusive. But this is not a mistake, or at least it is not always a mistake. Defeasible reasoning is not something to be corrected or eliminated. We should certainly seek conclusive evidence when the matter at hand is important enough and conclusive evidence can easily be had. But sometimes it is impossible to get conclusive evidence. In other cases where conclusive evidence is possible, the cost and effort involved in getting it are not justified by the importance of the matter under consideration. Even when conclusive evidence can be had and we can justify the expense and effort required to obtain it, we sometimes find ourselves in a situation where we must act before the conclusive evidence can be obtained. But perhaps even more common than any of these cases is the case where we unconsciously follow the rule-of-thumb for the typical case without even considering that the case we face may not be typical. These rules-of-thumb make up much of what we call common knowledge or common sense. Our reliance on various defeasible principles is in fact so very common I am tempted to claim that defeasible reasoning is the rule rather than the exception.

Expert systems and other decision support systems must operate under the same restrictions as do human experts. If they are to perform as well as human experts, they must be able to reason defeasibly. When conclusive data is not available for whatever reason, we will still want these systems to deliver whatever conclusions the evidence justifies, even if these conclusions are risky. Furthermore, we want our systems to revise their conclusions if additional relevant information becomes available just as human experts do.

There is no doubt that defeasible reasoning has been built into existing decision support systems to satisfy specific requirements peculiar to the domains of particular systems. What we need, though, is a general account of defeasible reasoning and an implementation that is not domain specific.

## 3. Probabilistic Reasoning

One kind of defeasible reasoning is probabilistic reasoning. The probability that a pair of dice will come up a seven on a particular throw is normally figured at about 0.167. But the probability that a pair of dice loaded in a certain way will come up a seven on a particular throw might be much higher, let us say 0.75. If we are told only that some pair of dice or other has been thrown and we are required to act in different ways depending on whether or not the dice came up a seven, our best course of action is to presume that the dice did not come up a seven. But we should presume just the opposite if we are told that the dice were loaded in the appropriate way. In either case, we are acting just as we would if we believed that the dice did or did not come up a seven, and our behavior or ‘tentative belief’ is predicated on the inconclusive evidence we have available.

In some expert or decision support systems, probabilistic reasoning is used to represent various kinds of defeasible reasoning. In these systems, a numerical measure of probability or 'degree of certainty' must be assigned to each rule and perhaps even to each fact in the knowledge base. These probability measures might take the form of single values between 0 and 1, of ranges of values, or even of so-called 'fuzzy' numbers. When competing lines of reasoning led to contradictory conclusions, the probability measures of the rules (and 'facts') used may be combined in some way to determine which line of reasoning is to be trusted. The methods used to combine these degrees of certainty usually do not satisfy the restrictions of mathematical probability theory.

Probabilistic reasoning may be appropriate in some circumstances, but this should not be our only model for defeasible reasoning for at least two reasons. First, much of our defeasible reasoning does not seem to fit this model. When I choose between using the competing rules 'Matches burn when struck' and 'Wet matches don't', I do not base my decision on what I take to be the probabilities that matches in general and wet matches in particular burn when struck. Probabilistic reasoning simply does not fit our observations about the way we ourselves use such general principles. Second, systems of this sort are difficult to maintain and to expand. No matter how many rules are in a probabilistic system and no matter how successful the system is in adjudicating between competing lines of reasoning, we must always be concerned that if we add new rules to the system, we will not get correct results in all cases unless we also revise the probabilities assigned to the old rules. Our probabilities must be reevaluated again and again as the system grows.

## 4. Listing All Exceptions

Another possibility is to expand our rules to include all possible exceptions. Something of this sort can also be done with decision tables or other decision support mechanisms. Thus we have 'Dry matches burn when struck' and 'Wet matches don't'. The same match will never satisfy both conditions on a single occasion. But then what of wet water-proofed matches? To take these into consideration, we will at least need to rewrite our second rule (or revise our decision table, etc.).

But there is a more serious problem for the strategy of explicitly listing all exceptions to a rule. If we do this, we can never make any tentative conclusions. For example, if we use the rules 'Dry matches burn when struck' and 'Wet matches don't', we can draw no conclusion, not even a tentative one, until we know whether the match in question is dry or wet. If we must draw a conclusion on just the information that a match has been struck, we are out of luck. Of course, people usually try to keep their matches dry, so we might just presume that the match is dry unless we learn otherwise. But this just pushes the need for a defeasible rule back one step.

There is another problem with representing competing rules using exceptions. Suppose we accept two principles concerning some future election: Smith will win if Jones doesn't, and if by some chance neither Smith nor Jones wins, then Brown will win. How would we represent these rules using exceptions? We might represent them as 'If Jones doesn't win, then Smith will win', and 'If neither Jones nor Smith wins, then Brown will win'. Now what happens if Brown wins? Then Jones doesn't, and the first rule forces us to conclude that Smith wins. This contradictory result is inescapable if neither rule is defeasible. But suppose we change the first rule by adding another exception: 'If neither Jones nor Brown wins, then Smith will win'. This avoids the contradiction, but now our two rules look just alike except that Smith and Brown are interchanged. They no longer reflect the preference we originally gave to Smith over Brown. In general, we cannot represent defeasible reasoning properly by listing exceptions to absolute, nondefeasible rules.

## 5. Competing Principles: An Example

If we don't use probabilities or explicitly list exceptions, how do we decide between competing lines of reasoning? To answer this question, we need to look at some examples of correct defeasible reasoning. Our starting point is the simplest kind of case where only two rules are involved. Consider an aquarist who accepts the following rules about certain kinds of tropical fish:

(1) If a fish is a chromide, it comes from brackish water.

(2) If a fish is a cichlid, it comes from fresh (not brackish) water.

Assume as well that our aquarist knows no other facts or rules relevant to our example. We will suppose that our aquarist has received a new specimen. Naturally, she wishes to provide it with a suitable environment, including water conditions similar to those of its native habitat. Suppose she knows that

(3) The new fish is a cichlid.

She concludes that

(4) The new fish comes from fresh water.

But now she learns that

(5) The new fish is also a chromide.

She does not know what to do. The antecedent conditions for (1) and (2) are both satisfied, but the results of applying the two rules are contradictory. She now knows that at least one of these two rules is defeasible even though she may previously have believed them both to be absolute.

Our aquarist is in a real quandary. Having gone to some trouble to acquire her specimen, it is important to her that she make the right decision. It is also of some importance to the fish. She might try to resolve the question by tasting the water that the fish has been delivered in, but some aquarists object to tasting water after a fish has lived in it at close quarters for a few days. She might try to avoid the issue altogether and simply not put the fish in any kind of water. Many aquarium fish have tried this alternative on their own initiative; few have found the results satisfactory.

Our aquarist does some research and discovers that

(6) If a fish is a chromide, it is a cichlid.

Now she can decide between the contradictory advise of (1) and (2). (1) requires more specific information than (2), so she uses it and provides her new specimen with brackish water.

This single example demonstrates the simple and elegant method we use to resolve many of the conflicts that arise in defeasible reasoning. However, the unfamiliarity of the situation may have prevented the reader from seeing how (6) resolves the issue. Look again at rules (1) and (2). We can think of defeasible rules as telling us what to expect in the normal or typical case. Rule (1) says that chromides typically come from brackish water and rule (2) tells us that cichlids typically come from fresh water. Is the new specimen a typical chromide or a typical cichlid? (6) tells us that a chromide is a special kind of cichlid, but we have no information that the fish is a special kind of chromide. The condition for (1), that the fish is a chromide, implies together with (6) all the information required for the condition of (2), that the fish is a cichlid. But the converse is not true. We do not know that a fish is a chromide when we learn that it is a cichlid. If we did, then we would truly be in a contradictory situation and might suspect that either (1) or (2) was downright false rather than just defeasible.

This example also shows why we are sometimes unable to resolve dilemmas involving contradictory defeasible rules. Without (6), we can't tell whether (1) or (2) accounts for more of the available evidence, and we can't tell whether we are dealing with an atypical chromide or an atypical cichlid. Unless we can tell this, we can't decide which rule to use. This is not a flaw in our reasoning; it is a flaw in our information. Note also that (6) is an absolute rule of taxonomy. We only use absolute rules in comparing the amount of information embodied in the conditions of competing rules. Other examples of rules we might take as absolute are rules like 'No bachelor is married' that are based on definitions, lawlike statements of science like 'Oxygen is consumed when a match burns', mathematical rules, and geographical regularities like ‘Anything in Honolulu is on Oahu’. 2

## 6. Conditional Logics

Within the last twenty years, logics have been developed for so-called ‘counterfactual’ conditionals. (Stalnaker (1968), Lewis (1973), Nute (1975); see Nute (1985) for a review of the literature.) These differ from classical logics in ways that suggest that they might be useful in explaining defeasible reasoning. A typical conditional logic is the system VW developed by David Lewis. Using → to represent the ordinary material conditional and > to represent the counterfactual conditional, we can axiomatize VW as follows.

AX1. $p > p$ .

AX2. $\left[p > (q\rightarrow r)\right]\to \left[(p > q)\rightarrow (p > r)\right].$

AX3. $(p > q) \to (p \to q)$ .

AX4. $(\sim p > p) \to (q > p)$ .

AX5. $\left[(p > q) \& \sim (p > \sim r)\right] \to \left[(p \& r) > q\right]$ .

AX6. $\left[(p\& q) > r\right] \to \left[p > (q \to r)\right]$ .

AX7. $\left[(p > q) \& (q > p)\right] \to \left[(p > r) \equiv (q > r)\right]$ .

Rule 1. From $p$ and $p \to q$ to infer $q$ .

Rule 2. From $(p_1\& \ldots \& p_n)\to q,r > p_1,\ldots ,$

and $r > p_n$ , to infer $r > q$ (where $n \leq 0$ ).

In VW, the counterfactual conditional differs from the classical material conditional in a number of ways that impinge upon our present concerns. Perhaps most importantly, the material conditional $p \rightarrow q$ entails the material conditional ( $p \& r$ ) $\rightarrow q$ , while the counterfactual conditional p > q may be true even though the counterfactual conditional ( $p \& r$ ) > q is false. This corresponds to the fact about defeasible rules that a rule like ‘Matches burn when struck’ is accepted while ‘Wet matches burn when struck’ is rejected.

Another difference between material and counterfactual conditionals is that counterfactual conditionals are not transitive. While $p \rightarrow q$ and $r \rightarrow p$ entail $r \rightarrow q$ , the two conditionals p > q and r > p do not entail r > q. This also happens with defeasible rules as in the following example.

(7) Presumably the weakened bridge would collapse if traffic were allowed on it.

(8) Presumably traffic would be allowed on the weakened bridged if it were repaired.

(9) But the weakened bridge would not collapse if it were repaired.

These and other features of counterfactual conditionals match features of the rules we use in defeasible reasoning. Nevertheless, we cannot use VW or any of its relatives to represent defeasible reasoning. AX3 and Rule 1 cause the problem. Together they imply that p and p > q entail q. But the very essence of a defeasible rule is that it may be a mistake to detach its consequent even in a case where its antecedent condition is satisfied. It is not enough that we cannot infer the rule ‘Wet matches burn when struck’ from the rule ‘Matches burn when struck’. We also do not want to accept the conclusion that a match burns when we learn that it was wet and it was struck. What we need, then, is a restricted procedure for detaching the consequent of a defeasible rule, and nothing of the sort is offered by conditional logics.

## 7. Other Approaches

Glymour and Thomason (1984) develop a system for revising theories as new information is acquired. Their view is a common one, that p, q, p > r and $q > \sim r$ comprise an inconsistent set of statements. Their solution to the dilemma is to reject some member of the set. If we are sure about p and q, then one of our rules is false and must be rejected. However, they do not simply defeat one of the conditionals; they eliminate it totally. This raises problems when the affected rules are actually generalizations that we may still want to use in other cases.

The criterion Glymour and Thomason use in deciding which conditional to reject is quite different from the test we uncovered in our fish example. Their method requires that when we learn that the antecedent of a conditional is satisfied, then that conditional and its consequent is preferred over any fact or conditional accepted at some earlier time. In the case of our aquarist, this means that she would provide her new specimen with fresh water if she learned that it was a cichlid after she learned that it was a chromide. But this is counterintuitive.

Raymond Reiter (1980) has developed a logic for defaults that is intended to handle examples of the sort we are considering. But Reiter's default logic runs into this same problem. The order in which the antecedents of rules are learned is not important since default logic takes a static system as its paradigm rather than the dynamic revision of a theory over time. However, the order in which rules are applied still makes a difference in the outcome of our deliberation. Here, the rule used first has priority and may prevent another rule from being used. The rules are not rejected as in the Glymour and Thomason system, nor are they defeated as in our examples. Instead, system-wide consistency conditions are explicitly listed in the antecedents of Reiter's default rules. By detaching the consequent of one rule, we may ensure that the condition of another rule is not satisfied. The second rule is not defeated since its antecedent is never satisfied.

McDermott and Doyle (1980) develop what they call nonmonotonic logic. In some ways their system resembles Reiter's default logic. $^{3}$ Again, system-wide consistency conditions are incorporated into the antecedents of rules. But unlike Reiter, McDermott and Doyle do not allow us to choose the order in which we apply the rules, a procedure that gives different results for different orders of application. What they propose instead is, roughly, that we should accept only those conclusions that show up no matter what order we apply the rules. This approach prevents the possibility that our aquarist might make the mistake of providing her new specimen with fresh water, but it prevents much more. In nonomonotic logic, the aquarist cannot decide between fresh and brackish water even after she learns that all chromides are cichlids. I think McDermott and Doyle are right in thinking that the order we apply the rules should not affect the conclusions we reach, but their nonmonotonic logic still does not behave as we want in our sample cases. Getting no answer when the question is intuitively decidable is as serious a defect as getting the wrong answer.

This discussion of the views of Glymour and Thomason, of Reiter, and of McDermott and Doyle is oversimplified. Their work deserves far more attention than we can give it here. There are many other accounts that could also be included in our discussion, such as McCarthy's work on circumscription (1980) and work by Etherington and Reiter on inheritance hierarchies (1984), but these must await another occasion.

## 8. The Formal System LDR

For simplicity's sake, I will develop a sentential logic for defeasible reasoning in this paper. I will call this system LDR. We will assume that we have a countable set of sentence constants $p$ , $q$ , $r$ , ... from which to construct the sentences and rules of LDR. A literal is either a sentence constant $p$ or the negation of some sentence constant $p$ (written $\sim p$ ). If $p$ is a sentence constant, then the complement of $p$ is $\sim p$ and the complement of $\sim p$ is $p$ . For any literal $p$ , we write the complement of $p$ as $\neg p$ . All literals are sentences of LDR, and if $p$ is a literal then $Ep$ is a sentence of LDR. We read $Ep$ as 'Evidently, $p'$ or as 'The evidence best supports the view that $p'$ . Intuitively, $E$ -sentences will mark the risky conclusions we draw using defeasible rules.

We represent rules in LDR using three dyadic operators: $\rightarrow$ , $\Rightarrow$ , and ? $\rightarrow$ . Where $S$ is a finite set of literals and $p$ is a literal, $S \rightarrow p$ is an absolute rule, $S \Rightarrow p$ is a defeasible rule, and $S? \rightarrow p$ is a defeater which we read as 'If everything in $S$ were satisfied, then maybe $p$ . A defeater never entitles us to reach a new conclusion; its only function is to interfere with inferences we might otherwise make using some defeasible rule. We will require that the antecedent set $S$ be non-empty in the cases of absolute rules and defeaters. In the case of defeasible rules it is useful to allow $S$ to be empty. A defeasible rule with an empty antecedent is called a presumption. For example, the statement 'Presumably the Republicans will nominate Bush for the Presidency in 1988' is represented in the language of LDR by a defeasible rule of the form {} $\Rightarrow p$ , where {} is the empty set.

An LDR theory is a pair $\langle R, K \rangle$ where R is a set of rules and K is a set of literals. Notice that E-sentences cannot appear in theories. We may wish to include some uncertain ‘facts’ in a theory, but we do this by putting the corresponding presumption in the rule set of the theory. This will allow us to reach the corresponding E-sentence as a conclusion unless the presumption is defeated. However, were we to allow an E-sentence in our initial theory we could never reject or defeat it. Presumptions represent uncertain initial assumptions that we might be persuaded to reject, while E-sentences represent the risky conclusions we reach through defeasible rules, including presumptions.

An absolute proof of a literal p from a theory $\langle R, K \rangle$ is a list $\sigma$ of literals whose last member is p, such that for every member $\sigma_{i}$ of $\sigma$ , one of the following conditions holds:

(AP1) $\sigma_{i}\in K$ , or

(AP2) for some absolute rule $S \to \sigma_i$ in $K$ , every member of $S$ is an earlier line of $\sigma$ .

We say $p$ is absolutely derivable from $\langle R, K \rangle$ (in symbols, $\langle R, K \rangle \vdash p$ ) if there is an absolute proof of $p$ from $\langle R, K \rangle$ . We write $\langle R, K \rangle \vdash S$ if $\langle R, K \rangle \vdash p$ for every $p \in S$ .

Theorem 1. If $\langle R, K \rangle \vdash p$ , $Q$ is a set of rules containing $R$ , and $L$ is a set of literals containing $K$ , then $\langle Q, L \rangle \vdash p$ .

Theorem 2. If $S \to p$ is in $R$ and $\langle R, K \rangle \vdash S$ , then $\langle R, K \rangle \vdash p$ .

The various results in this paper are listed together with their proofs in the appendix.

A proof of a sentence p from a theory $\langle R, K \rangle$ is a list $\sigma$ of sentences whose last member is p, such that for every member $\sigma_{i}$ of $\sigma$ , one of the following conditions holds:

(P1) $\langle R, K \rangle \vdash \sigma_{i}$ ,

(P2) $\sigma_{i} = Eq$ for some literal $q$ , and $q$ is an earlier member of $\sigma$ ,

(P3) $S \to q \in R$ , not $\langle R, K \rangle \vdash \neg q$ , $\sigma_i = Eq$ , and $Er$ is an earlier member of $\sigma$ for every $r \in S$ , or

(P4) $S \Rightarrow q \in R$ , not $\langle R, K \rangle \vdash \neg q$ , $\sigma_i = Eq$ , $Er$ is an earlier member of $\sigma$ for every $r \in S$ , and for every set $T$ of literals, if either $T \Rightarrow \neg q \in R$ or $T? \rightarrow \neg q \in R$ , and $\langle R, K \rangle \vdash T$ , then $\langle R, S \rangle \vdash T$ but not $\langle R, T \rangle \vdash S$ .

(P2) says that q is evident if it can be proved using only absolute rules. (P3) says that q is evident if it follows from absolute rules and other evident literals. The only way to defeat such an inference is to show that the conclusion can be proven false using only absolute rules and facts. (P4) is a complex rule incorporating the mechanism for comparing the antecedent sets of competing defeasible rules and defeaters.

We say $p$ is defeasibly derivable from $\langle R, K \rangle$ (in symbols, $\langle R, K \rangle \Vdash p$ ) if there is a proof of $p$ from $\langle R, K \rangle$ . We write $\langle R, K \rangle \Vdash S$ if $\langle R, K \rangle \Vdash p$ for every $p \in S$ .

## 9. A Semantics for LDR

A semantics for LDR must tell us what a defeasible rule means or what is required to understand a defeasible rule. Defeasible rules are expressed in English by generalizations like 'Birds fly' or by explicit conditionals like 'If you strike a match, it will burn'. The usual method in formal semantics is to explain the meaning of such declarative sentences by giving truth conditions for them. We understand a sentence when we know what circumstances would make it true and what circumstances would make it false.

There is another way to think about the meaning of a defeasible rule. The sentence ‘Birds fly’ tells us something about the world, but when thought of as a rule it does something else. It tells us to draw a certain conclusion under certain circumstances. Viewed as a rule, it is an imperative rather than a declarative sentence. It tells us to infer that a thing flies, other things being equal, if we know that it is a bird. The ceteris paribus or ‘other things being equal’ clause is what distinguishes it from an absolute rule.

As a rule rather than a description of the world, we can and must give the sentence ‘Birds fly’ a different kind of analysis since it makes no sense to ask when an imperative is true or false. To see this more clearly, consider the rules of chess. They certainly are not true or false. What does it mean, then, to say that we understand the rules of chess? I suggest that we understand the rules of chess, we know what they mean, when we know how to follow them or comply with them. Instead of truth conditions, this suggests that we can explain what a rule means by specifying compliance conditions for it. This is the basic idea behind the semantics for LDR that I will develop.

We can think of the rules of LDR as policies for belief revision. $^{5}$ Both absolute and defeasible rules tell us how we should change our overall beliefs when we learn something new. If I learn that something is a bird, I also come to believe, at least tentatively, that it flies. If I don't, then I do not comply with the rule 'Birds fly'. Only certain belief states are available to me if I accept a particular set of rules. In this case, no belief state is available to me in which I believe that Tweety is a bird, believe nothing that indicates Tweety doesn't fly, but still do not believe that Tweety flies. I am violating the rule 'Birds fly' if I am in a belief state like this.

The rules of chess determine a set of playable games. Leave something out of this set or add something to it and you no longer have chess. In a similar way, a set S of LDR rules determines a set of possible belief states. Leave something out or add something and you no longer have compliance with S. I will offer an account of the set of possible belief states a person could be in who accepts a particular set of LDR rules. This approach makes particularly good sense if our goal is to implement LDR in an automated reasoning system, for the system must accept the rules it is given and has no means to determine if they are justified. What we want to know is how this acceptance should effect the total set of ‘beliefs’ of the system.

We begin by defining a belief state as a pair $\langle M, N \rangle$ where N is a set of literals and M is a subset of N. Intuitively, we want M to represent those literals to which there is strong epistemic commitment, and N to represent those literals to which there is at least tentative epistemic commitment. Roughly speaking, M is the set of literals which an agent would claim to know and N is the set of literals which the agent would assert at least tentatively, perhaps using 'I think', 'I believe', or 'I expect'.

Where R is a set of rules and defeaters, let $R_{abs}$ be the set of all belief states $\langle M, N \rangle$ such that for every

$$
S \rightarrow p \in R,
$$

(A1) if $S$ is a subset of $M$ , then $p \in M$ ; and (A2) if $S$ is a subset of $N$ , then either $\neg p \in M$ or $p \in N$ .

$R_{abs}$ represents the set of all belief states that a person who accepts all the absolute rules in R could be in. For the literal p, we will represent the set of all belief states $\langle M, N \rangle$ in $R_{abs}$ such that $p \in M$ by $R[p]$ . Where S is a set of literals, $R[S]$ is the set of all belief states $\langle M, N \rangle$ in $R_{abs}$ such that S is a subset of M.

Theorem 3. $\langle R, K \rangle \vdash p$ iff $R[K]$ is contained in $R[p]$ .

Theorem 4. $\langle R, K \rangle \vdash L$ iff $R[K]$ is contained in $R[L]$ .

For any set R of rules and defeaters, we will let $R_{comp}$ be the set of all belief states that are possible for an agent who accepts all the members of R. We call $R_{comp}$ the complete R observing belief space. Formally, $R_{comp}$ must be represented by some subset of $R_{abs}$ . A member $\langle M, N \rangle$ of $R_{abs}$ is in $R_{comp}$ provided it satisfies the following condition for every subset S of N and every literal p:

(A3) if $S$ is a subset of $N$ , $S \Rightarrow p \in R$ , and $R[S]$ is a proper subset of $R[T]$ for every subset $T$ of $M$ such that either $T \Rightarrow \neg p \in R$ or $T? \rightarrow \neg p \in R$ , then $\neg p \in M$ or $p \in N$ .

Consider a person who strongly believes all and only the literals in some set M and who accepts all and only the rules and defeaters in some set R. This person's belief state should be in $R_{comp}$ , that is, $\langle M, N \rangle$ should be a member of $R_{comp}$ where N is the set of all and only those literals which the person accepts at least tentatively. But N might contain literals that are not justified by belief in the members of M and acceptance of the members of R. There might be a proper subset Q of N such that $\langle M, Q \rangle$ is also in $R_{comp}$ . If this is not the case, we will say that the person's belief state is an R-minimal belief state.

Theorem 5 (Soundness). If $K$ is a set of literals, $R$ is a set of rules and defeaters, $M = \{p: \langle R, K \rangle \vdash p\}$ , $\langle M, N \rangle$ is an $R$ -minimal belief state and $\langle R, K \rangle \Vdash Eq$ , then $q \in N$ .

Theorem 6. If R is a set of rules and defeaters, K is a set of literals, and $M = \{ p: \langle R, K \rangle \vdash p \}$ , then there is exactly one set N of literals such that $\langle M, N \rangle$ is an R-minimal belief state.

We will call the set N that satisfies the condition in Theorem 6 the conservative R-revision of K.

Theorem 7 (Completeness). $\langle R, K \rangle \Vdash Ep$ iff $p$ is in the conservative $R$ -revision of $K$ .

$R_{comp}$ gives the compliance condition for the set R of LDR rules. It is more difficult to give the compliance condition for a single defeasible rule or defeater because of the way the rules interact. The meaning of a single rule can only be given by showing the results of adding that rule to any set of LDR rules that doesn't already contain it. Suppose $r$ is a particular LDR rule and $R$ is a set of LDR rules that doesn't contain $r$ . Then $R_{\text{comp}}$ is the compliance condition for $R$ and $(R \cup \{r\})_{\text{comp}}$ is the compliance condition for $R \cup \{r\}$ . This pair of belief spaces represent what happens when a person who already accepts all the rules in $R$ adds $r$ to his policies for belief revision. Now we need to collect all such pairs for every initial set $R$ of LDR rules that a person might accept. The compliance condition of a single LDR rule $r$ is given by the set of pairs of belief spaces $\{\langle R_{\text{complete}}, (R \cup \{r\})_{\text{comp}} \rangle: R \text{ is a set of LDR rules and } r \text{ is not a member of } R \}$ .

## 10. Implementation

An extension of the inference engine of the popular logic programming language Prolog has been constructed that implements a quantified version of LDR. This extension is a Prolog program called d-Prolog (for defeasible Prolog). I will describe d-Prolog briefly and discuss some current d-Prolog applications projects.

In Prolog, we represent an atomic sentence as a predicate together with some arguments. For example, 'Tweety flies' is represented as

flies(tweety).

d-Prolog adds to Prolog syntax a negation operator neg. $^{6}$ The negative literal ‘Tweety does not fly’ becomes

neg flies(tweety).

In Prolog, rules are written with the conclusion coming before the condition, and I have adopted the same convention for d-Prolog. Only absolute rules can be represented in Prolog. The absolute rule $\{p, q, r\} \rightarrow s$ is written

$$
s: - p, q, r.
$$

The operator :- is read 'if', and the literals in the condition are connected by commas which we read 'and'. We add two additional operators := and : in d-Prolog, one for defeasible rules and the other for defeaters. { p, q, r } ⇒ s is written s := p, q, r.

And $\{p, q, r\} ? \to s$ is written

$$
s \colon \hat {\textbf {\textit {p}}}, q, r.
$$

Prolog provides a nullary predicate true that always succeeds. We can use this predicate in d-Prolog to represent presumptions. 'Presumably, $p$ ', represented in LDR as $\{\} \Rightarrow p$ , is written in d-Prolog as

p := true.

Prolog computation begins when the system is given a query. It treats this query as a theorem to be proven from the facts and rules in the database. A Prolog query has the form

$$
? - p.
$$

which can be read 'Can you prove p?' Prolog responds yes or no. Of course, Prolog does not recognize defeasible rules, defeaters or presumptions. It must be told what these are and how they are to be used. This is what the program d-Prolog does. It tells Prolog how to reason defeasibly. To invoke the d-Prolog inference engine, we must phrase our query in a way that tells d-Prolog to use the defeasible rules, etc., in its database. Our query takes the form

$$
? - @ p.
$$

which can be read 'Can you prove p defeasibly?'

Prolog rules can include variable expressions that become bound to various values during the attempt to prove some query. It is these bindings that provide the solutions to various problems. Variables are represented by a simple expression beginning with a capital letter. For example, the defeasible rules 'Birds fly' and 'Penguins don't fly', the defeater 'Sick birds might not fly', and the absolute rule 'Penguins are birds' could be written

in d-Prolog as

flies(X) := bird(X).

neg flies(X) := penguin(X).

neg flies(X):^sick(X), bird(X).

bird(X) :- penguin(X).

If our d-Prolog database includes only these four rules and the fact

bird(Tweety).

then the d-Prolog query

? - @ flies(X).

will succeed, producing the response

If we add either

sick(tweety).

or

penguin(tweety).

to our database, then the same d-Prolog query ? - @ flies(X).

will fail. But there is an important difference in these two cases. If we add

sick(tweety).

then the query

? - @ neg flies(X).

will also fail. But if we add

penguin(tweety).

then the query

? - @ neg flies(X).

will succeed with the solution

$X =$ tweety.

The defeater only prevents us from concluding that Tweety flies, but the competing defeasible rule allows us to reach the contradictory conclusion. The absolute rule ‘Penguins are birds’ is used in comparing the competing defeasible rules.

Various d-Prolog knowledge bases have been developed to test and demonstrate the features of this systems. One is a toy medical diagnostic system that uses defeasible metarules to control the prescription of medication. This system uses the following four rules for prescribing medication.

(1) Normally, prescribe a medication for an ailment if that ailment has been diagnosed and the medication is effective in treating the ailment.

(2) Normally, don't prescribe a medication if the medication is counterindicated (allergy, high blood pressure, etc.).

(3) Normally, prescribe a medication for an ailment if that ailment has been diagnosed, if the medication is effective in treating the ailment, and if the patient's condition is critical (death is likely without treatment), even if the medication is counterindicated.

(4) Never prescribe a medication for an ailment if the medication is counterindicated and there is another medication indicated for the ailment that is not also counterindicated.

These four rules are easily represented in d-Prolog as

prescribe(Medication,Ailment) := diagnosed(Ailment), effective-in-treating(Medication,Ailment).

neg prescribe(Medication,Ailment) := counterindicated(Medication).

prescribe(Medication,Ailment) := diagnosed(Ailment), effective-in-treating(Medication,Ailment), counterindicated(Medication), condition-of-patient(critical).

neg prescribe(Medication, Ailment) := counterindicated(Medication), effective-in-treating(AlternateMedication, Ailment),

neg counterindicated(AlternateMedication).

Supplied with information about which medications are effective in treating which ailments and about the allergies, etc., of the patient, this system makes highly plausible prescriptions.

Two prototype expert systems using d-Prolog are now under development. The first helps the user select a business forecasting method. $^{7}$ The second helps the user estimate the economic importance of kaolin deposits. $^{8}$ Both are intended for field use when they are completed.

The development of d-Prolog and various implementation issues are discussed in Nute (1984, 1985a), Nute and Lewis (1986), Covington and Nute (1986), and Chapter 11 of Covington, Nute and Vellino (1987). $^{9}$

## 11. Summary and Conclusions

Defeasible reasoning is a widespread phenomenon that cannot be ignored in the development of expert systems and decision support systems. In the end, we want more than piecemeal solutions cobbled together for a particular application in a particular domain. What we want is a general account of defeasible reasoning, an account that provides a foundation for implementation. It should provide suitable methods for knowledge representation and an intuitively correct inference engine. It is important that the knowledge representation be natural and easy to understand, and that the inference engine be based on principles we understand and approve.

Probabilistic methods are difficult to use and can hardly be called natural. Such methods have been widely used in applications since nothing else has been available. But the general opinion seems to be that such systems are difficult to build, are even more difficult to expand, and are unpredictable.

A simpler approach would seem to be to include all exceptions in each rule we add to a system. This results in extremely complicated rules and still does not allow us to express simple hierarchies of rules without contradiction.

Conditional logics are initially promising, but general rules are falsified by individual counterexamples when what we really want is to defeat the general rule for each exception while continuing to follow it for other cases. A method of belief revision due to Glymour and Thomason inherits this difficulty from conditional logics.

Reiter's default logic and McDermott's and Doyle's nonmonotonic logic avoid many of the problems of the other methods we considered, but they are ultimately unable to resolve conflicts between competing rules in cases where intuitively resolution is possible.

LDR and its quantificational extension provide an alternative to these approaches. No numerical probabilities or confidence factors are involved. A basic rule can be expressed simply, and its exceptions can be added in separate rules as they are learned. This makes it easy to read and understand the rules. Tentative conclusions are marked so we know which conclusions are at risk. By distinguishing between absolute and defeasible rules, we are able to resolve conflicts between competing defeasible rules that other systems cannot resolve. The basic principle for resolving these conflicts is easy to explain using simple examples involving ordinary cases. And the notion of a defeater provides additional resources for knowledge representation not found in other systems.

Another advantage of this approach is that it has been implemented as an extension of a widely available programming language. This makes further experimentation and testing possible. Practically speaking, the ultimate experiment or test is whether the approach can prove itself in real applications. We have now begun to develop such applications. In the near future, we will report the first results of these efforts.

## Appendix

All the results cited in this paper, together with their proofs, are collected here for the convenience of the reader.

Theorem 1. If $\langle R, K \rangle \vdash p$ , $Q$ is a set of rules containing $R$ , and $L$ is a set of literals containing $K$ , then $\langle Q, L \rangle \vdash p$ .

Proof. Assume the hypothesis. Let $\sigma$ be an absolute proof of $p$ from $\langle R, K \rangle$ . Then the last member of $\sigma$ is $p$ and for each member $\sigma_i$ of $\sigma$ , either $\sigma_i$ is a member of $K$ or there is an absolute rule $S \to \sigma_i$ in $R$ such that every member of $S$ is an earlier line of $\sigma$ . If $\sigma_i$ is in $K$ , then $\sigma_i$ is in $L$ ; and if $S \to \sigma_i$ is $R$ , then $S \to \sigma_i$ is in $Q$ . So the last member of $\sigma$ is $p$ , and for each member $\sigma_i$ of $\sigma$ , either $\sigma_i$ is in $L$ or there is an absolute rule $S \to \sigma_i$ in $R$ such that every member of $S$ is an earlier line of $\sigma$ . Thus, $\sigma$ is an absolute proof of $p$ from $\langle Q, L \rangle$ , and $\langle Q, L \rangle \vdash p$ .

Theorem 2. If $S \to p$ is in $R$ and $\langle R, K \rangle \vdash S$ , then $\langle R, K \rangle \vdash p$ .

Proof. Assume the hypothesis. Since $S \to p$ is an absolute rule, $S$ is finite. Let $S = \{s_1, \ldots, s_n\}$ . Since $\langle R, K \rangle \vdash S$ , there is an absolute proof of each $s_i$ from $\langle R, K \rangle$ . For each $s_i$ , let $\sigma^i$ be an absolute proof of $s_i$ from $\langle R, K \rangle$ . Let $\sigma = \sigma^1 * \ldots * \sigma^n * \langle p \rangle$ , where $*$ is the concatenation operator for sequences. The last member of $\sigma$ is $p$ , and for every member $\sigma_j$ of $\sigma$ except the last, $\sigma_j$ is a member of one of the $\sigma^i$ 's and hence is either a member of $K$ or is the consequent of some absolute rule $T \to \sigma_j$ in $R$ such that each member of $T$ is an earlier line in $\sigma$ . But the last member of $\sigma$ also satisfies this condition since $S \to p \in R$ and for each $s_i \in S$ , $s_i$ is the last member of $\sigma^i$ and hence an earlier member of $\sigma$ . So $\sigma$ is an absolute proof of $p$ from $\langle R, K \rangle$ , and $\langle R, K \rangle \vdash p$ .

Theorem 3. $\langle R, K \rangle \vdash p$ iff $R[K]$ is contained in $R[p]$ .

Proof. Suppose $\langle R, K \rangle \vdash p$ and $\langle M, N \rangle \in R[K]$ . Then $K$ is contained in $M$ , and we can let $\sigma$ be an absolute proof of $p$ from $\langle R, K \rangle$ . Let $n$ be any integer less than the length of $\sigma$ and suppose that for all $i \leq n$ , $\sigma_i \in M$ . This will be vacuously true for $\sigma_1$ since there are no earlier members of $\sigma$ . By definition, $\sigma_n \in K$ or there is an absolute rule $S \to \sigma_n \in R$ such that every member of $S$ is an earlier member of $\sigma$ . If $\sigma_n \in K$ , then $\sigma_n \in M$ since $M$ contains $K$ . If $S \to \sigma_n \in R$ and each member of $S$ is an earlier member of $\sigma$ , then

S is contained in M by our inductive hypothesis. But $\langle M, N \rangle \in R_{abs}$ , so by (A1), $\sigma_{n} \in M$ . By mathematical induction, every member of $\sigma$ is a member of M. But $\sigma$ is an absolute proof of p from $\langle R, K \rangle$ , so the last member of $\sigma$ is p. Thus, $p \in M$ and $\langle M, N \rangle \in R[p]$ . It follows that R[K] is contained in R[p].

Suppose conversely that $R[K]$ is contained in $R[p]$ . Let $M = \{q: \langle R, K \rangle \vdash q\}$ . We will show that $\langle M, M \rangle \in R[K]$ . Clearly $\langle M, M \rangle$ is a belief state. Suppose $S \to q \in R$ and $S$ is a subset of $M$ . Then $\langle R, K \rangle \vdash S$ , and $\langle R, K \rangle \vdash q$ by Theorem 2. But then $q \in M$ . Therefore $\langle M, M \rangle$ satisfies (A1) and (A2), and $\langle M, M \rangle \in R_{\mathrm{abs}}$ . By our hypothesis, $R[K]$ is contained in $R[p]$ ; so $\langle M, M \rangle \in R[p]$ , $p \in M$ , and $\langle R, K \rangle \vdash p$ by the definition of $M$ .

Theorem 4. $\langle R, K \rangle \vdash L$ iff $R[K]$ is contained in $R[L]$ .

This Theorem is an obvious extension of Theorem 3.

Theorem 5 (Soundness). If $K$ is a set of literals, $R$ is a set of rules and defeaters, $M = \{p: \langle R, K \rangle \vdash p\}$ , $\langle M, N \rangle$ is an $R$ -minimal belief state and $\langle R, K \rangle \Vdash Eq$ , then $q \in N$ .

Proof. Assume the hypothesis. Let $\sigma$ be a proof of Eq. Let $\sigma_{i}$ be any member of $\sigma$ and suppose that for every earlier member $\sigma_{j}$ of $\sigma$ , either $\sigma_{j} \in N$ if $\sigma_{j}$ is a literal, or $\sigma_{j} = Er$ for some $r \in N$ if $\sigma_{j}$ is not a literal. $\sigma_{1}$ satisfies this condition vacuously since there are no earlier members of $\sigma$ . We will show that $\sigma_{i}$ satisfies this same condition, and hence by mathematical induction, every member of $\sigma$ satisfies this condition. Since Eq is the last member of $\sigma$ , it follows immediately that $q \in N$ .

$\sigma_{i}$ must satisfy one of the conditions (P1)-(P4). We will consider each of these cases separately.

Case 1: $\langle R, K \rangle \vdash \sigma_i$ . Then by the definition of $M$ , $\sigma_i \in M$ . But by the definition of a belief state, $M$ is contained in $N$ . So $\sigma_i \in N$ .

Case 2: $\sigma_{i} = Er$ and $r$ is an earlier line of $\sigma$ . But then by our inductive hypothesis, $r \in N$ .

Case 3: $S \to r \in R$ , not $\langle R, K \rangle \vdash \neg r$ , $\sigma_i = Er$ , and $Es$ is an earlier member of $\sigma$ for every $s \in S$ . By our inductive hypothesis, $S$ must be a subset of $N$ . But $\langle M, N \rangle \in R_{\mathrm{abs}}$ and thus satisfies (A2). So $\neg r \in M$ or $r \in N$ . But by the definition of $M$ , and since not $\langle R, K \rangle \vdash \neg r, \neg r$ is not a member of M. So $r \in N$ .

Case 4: $S \Rightarrow r \in R$ , not $\langle R, K \rangle \vdash \neg r$ , $Es$ is an earlier member of $\sigma$ for every $s \in S$ , and for every set $T$ of literals, if either $T \Rightarrow \neg r \in R$ or $T? \to \neg r \in R$ , and $\langle R, K \rangle \vdash T$ , then $\langle R, S \rangle \vdash T$ but not $\langle R, T \rangle \vdash S$ . Suppose $T \Rightarrow \neg r \in R$ or $T? \to \neg r \in R$ , and that $\langle R, K \rangle \vdash T$ . Then $R[S]$ is a subset of $R[T]$ by Theorem 4 since $\langle R, S \rangle \vdash T$ ; but $R[T]$ is not contained in $R[S]$ , also by Theorem 4, since not $\langle R, T \rangle \vdash S$ . So $R[S]$ is a proper subset of $R[T]$ . But $\langle M, N \rangle \in R_{\text{comp}}$ and thus satisfies (A3). It follows that $\neg r \in M$ or $r \in N$ . But by the definition of $M$ , and since not $\langle R, K \rangle \vdash \neg r$ , $\neg r$ is not a member of $M$ . So $r \in N$ .

Theorem 6. If $R$ is a set of rules and defeaters, $K$ is a set of literals, and $M = \{p: \langle R, K \rangle \vdash p\}$ , then there is exactly one set $N$ of literals such that $\langle M, N \rangle$ is an $R$ -minimal belief state.

Proof. Assume the hypothesis. Let $N = \{p: \langle R, K \rangle \Vdash Ep\}$ . We begin by showing that $\langle M, N \rangle \in R_{\mathrm{comp}}$ .

$\langle M, N \rangle$ satisfies (A1) by Theorem 2.

Suppose $S \to q \in R$ , $S$ is a subset of $N$ , and $\neg q$ is not a member of $M$ . Since $S$ is finite, we can let $S = \{s_1, \ldots, s_n\}$ . For each $s_i \in S$ , we let $\sigma_i$ be a proof of $Es_i$ from $\langle R, K \rangle$ . We can do this since for each $s_i$ , $\langle R, K \rangle \Vdash Es_i$ . Let $\sigma = \sigma_1 * \ldots * \sigma_n * \langle Eq \rangle$ . Since $\neg q$ is not in $M$ , not $\langle R, K \rangle \vdash \neg q$ . Then by the definition of a proof, and by (P3) in particular for the last member of $\sigma$ , $\sigma$ is a proof of $Eq$ from $\langle R, K \rangle$ , and $q \in N$ . So $\langle M, N \rangle$ satisfies (A2) and $\langle M, N \rangle \in R_{\text{abs}}$ .

Suppose $S$ is a subset of $N$ , $S \Rightarrow q \in R$ , $R[S]$ is a proper subset of $R[T]$ for every subset $T$ of $M$ such that either $T \Rightarrow \neg q \in R$ or $T? \rightarrow \neg q \in R$ , and not $\neg q \in M$ . Since $S$ is finite, we can let $S = \{s_1, \ldots, s_n\}$ . By the definition of $N$ , we let $\sigma_i$ be a proof of $Es_i$ from $\langle R, K \rangle$ for each $s_i \in S$ . Finally, we let $\sigma = \sigma_1 * \ldots * \sigma_n * \langle Eq \rangle$ . We know that the last member of $\sigma$ is $Eq$ and that every member of $\sigma$ except possibly the last satisfies one of (P1)-(P4). Since $\neg q$ is not in $M$ , not $\langle R, K \rangle \vdash \neg q$ . Furthermore, $S \Rightarrow q \in R$ and for each $s_i \in S$ , $Es_i$ is an earlier member of $\sigma$ . Suppose $T$ is a set of literals such that $\langle R, K \rangle \vdash T$ and either $T \Rightarrow \neg q \in R$ or $T? \rightarrow \neg q \in R$ . Then by our hypothesis, $R[S]$ is a proper subset of $R[T]$ . It follows from Theorem 4 that $\langle R, S \rangle \vdash T$ but not $\langle R, T \rangle \vdash S$ . Thus, the last member of $\sigma$ satisfies (P4). This establishes that $\sigma$ is a proof of $Eq$ from $\langle R, K \rangle$ , that $\langle R, K \rangle \Vdash Eq$ , and that $q \in N$ . So $\langle M, N \rangle$ satisfies (A3), and $\langle M, N \rangle \in R_{\mathrm{comp}}$ .

Now let $\langle M, Q \rangle$ be any R-minimal belief state. By Theorem 5, N is contained in Q. Then since $\langle M, Q \rangle$ is R-minimal, N = Q. So $\langle M, N \rangle$ is the required unique R-minimal belief state.

Theorem 7 (Completeness). $\langle R, K \rangle \Vdash Ep$ iff $p$ is in the conservative $R$ -revision of $K$ .

Theorem 7 follows immediately from the construction of the conservative R-revision of K in the proof of Theorem 6.

## References

Covington, Michael and Donald Nute, Implicature, Disjunction, and Non-monotonic Logic, ACMC Research Report 01-0015 (University of Georgia, Athens, GA, 1986).

Covington, Michael, Donald Nute and Andre Vellino, Prolog Programming in Depth (Scott, Foresman, and Company, Glenview, IL, 1988).

Etherington, David W. and Raymond Reiter, On Inheritance Hierarchies with Exceptions, Proc. AAAI-83 (William Kaufmann, Los Altos, CA).

Glymour, Clark and Richmond Thomason, 1984, Default Reasoning and the Logic of Theory Perturbation, Proceedings of the AAAI Workshop on Non-monotonic Reasoning (New Paltz, New York, October 17–19, 1984).

Lewis, David, Counterfactuals (Harvard University Press, Cambridge, MA, 1973).

McCarthy, John, Circumscription - A Form of Non-monotonic Reasoning, Artificial Intelligence 13 (1980) 27-39.

McDermott, Drew and Jon Doyle, Non-monotonic Logic I, Artificial Intelligence 13 (1980) 41–72.

Nute, Donald, Counterfactuals and the Similarity of Worlds, Journal of Philosophy 72 (1975) 773–778.

Nute, Donald, Topics in Conditional Logic (Reidel, Dordrecht, 1980).

Nute, Donald, Non-monotonic Reasoning and Conditionals, ACMC Research Report 01-0002 (University of Georgia, Athens, GA, 1984).

Nute, Donald, Conditional Logic, in: D. Gabbay and F. Guenther, eds., Handbook of Philosophical Logic II (Reidel, Dordrecht, 1985).

Nute, Donald, Non-monotonic Logic Based on Conditional Logic, ACMC Research Report 01-0007 (University of Georgia, Athens, GA, 1985a).

Nute, Donald, Defeasible Reasoning, Proceedings of the 20th Hawaii International Conference on System Science (University of Hawaii, Honolulu, 1987).

Nute, Donald and Michael Lewis, A User's Manual for d-Prolog, ACMC Research Report (University of Georgia, Athens, GA, 1986).

Nute, Donald, Robert Mann and Betty Brewer, Using Defeasible Logic to Control Selection of a Business Forecasing Method. Proceedings of the 21st Hawaii International Conference on System Science (IEEE Computer Society Press, Washington, DC, 1988).

Reiter, Raymond, A Logic for Default Reasoning, Artificial Intelligence 13 (1980) 81–132.

Stalnaker, Robert, A Theory of Conditionals, in: N. Rescher, ed., Philosophical Quarterly Monograph series 2 (Blackwell, Oxford, 1968).

Stalnaker, Robert, Inquiry (MIT, Cambridge, 1984).
