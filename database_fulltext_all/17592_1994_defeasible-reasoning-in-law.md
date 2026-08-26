---
otero_id: 17592
otero_key: "NXX8PBC8"
title: "Defeasible reasoning in law"
authors: "Sandra K. Dewitz; Young Ryu; Ronald M. Lee"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90029-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Defeasible reasoning in law

Sandra K. Dewitz

College of Business, San Jose State University, San Jose, CA, USA

Young Ryu and Ronald M. Lee

Graduate School of Business, The University of Texas at Austin, Austin, TX, USA

Numerous legal scholars have asserted that legal reasoning is largely a deductive process in which legal rules are applied to the facts of a case in order to derive a conclusion. Though some might contest this assertion, it seems that what we know as law is largely a system of rules. However, these rules are not immutable and fully consistent; in many cases, multiple rules can be applied to the facts of a case, the conclusion derived from one rule conflicting with and potentially defeating that derived from another rule. In this paper, we discuss legal reasoning as defeasible reasoning and present a prototype of a computer-based legal reasoning system to illustrate the advantages of our approach. Defeasible reasoning is an appropriate foundation for the development of legal support systems because it not only can support the non-monotonicity of legal rules but also can resolve many of the conflicts that arise in applying these rules.

Keywords: Defeasible reasoning; Legal reasoning; Logic modeling

![](/api/attachments/NXX8PBC8/fulltext/images/ef88303afecb324b8b3075b67d6f03db2f69b30a075f613d006971e6da6b7eb4.jpg)

Sandra Dewitz is an Associate Professor in Management Information Systems at San Jose State University. She completed her PhD in 1992 at the University of Texas at Austin. Her research interests include investigating the design requirements of legal reasoning systems and developing rule-based systems to facilitate inter-firm procedures.

![](/api/attachments/NXX8PBC8/fulltext/images/70ccfa1a80fd9f98b37267cd95d1ecea8b99016c02c8d4207feee24c56d2576f.jpg)  
Young U. Ryu is currently Assistant Professor of Information Systems at the University of Texas, Dallas. He completed his PhD in 1992 at the University of Texas at Austin in Information Systems. His current research interests include the use of logic for law and business applications, business expert systems, and database approaches to the design of information systems.

![](/api/attachments/NXX8PBC8/fulltext/images/769532f856df0ca4c83f5b81c66e309ea9a64547d272a972dcfa67a1454a2aa6.jpg)

Ronald M. Lee is currently Director of the Erasmus University Research Institute for Decision and Information Systems (EURIDIS) in Rotterdam, the Netherlands. Formerly, he was Associate Professor of Information Systems at the Management Science and Information Systems Department at the University of Texas at Austin. He has a PhD in Decision Sciences (Wharton, 1980), and has previously served as a research scholar at the International Institute for Applied Systems Analysis in Vienna, Austria, and as Visiting Professor of Management at the Universidade Nova de Lisboa, in Lisbon, Portugal. Current research focuses on applications of artificial intelligence to business; special focus is 'logic modeling', the use of formal logic representations for management science applications; current projects involve the use of logic modeling to represent and manage formal business communications systems focusing on (a.) bureaucratic systems (formalized communications within institutions) and (b.) electronic contracting systems (formalized communications between enterprises). Theoretical aspects include the role of deontic and illocutionary logic in representing formal business conversations. Practical value is the reduction of bureaucratic and legalistic red tape. This work also includes multilingual business communications, communications between parties with different native languages.

supporting structured communications between parties with different native languages.

Correspondence to: S.K. Dewitz, Department of Marketing and Quantitative Studies, College of Business, San Jose State University, San Jose, CA 95192, USA.

## 1. Introduction

The application of artificial intelligence (AI) to legal reasoning, though one of the more active research areas, has been largely unsuccessful (Leith, 1986; Reed, 1989; Stamper, 1988 and Susskind, 1986, 1987). Although the many projects aimed at developing legal reasoning systems have proven the feasibility of this endeavor, none has produced a system of use to lawyers (Susskind, 1986). Susskind (1987) attributes this failure to the fact that almost all $^{1}$ current legal reasoning systems ignore the jurisprudential theory on which legal reasoning is based. Without this jurisprudential grounding, AI researchers are likely to be misled by what most attracts them to this domain: its “rule-like surface veneer” (Rissland, 1985, p. 1254). The surface structure of law fosters the “naive notion (for some) that because a body of rules and regulations exists, all one has to do is translate them into executable code to create a program for performing complex legal reasoning”; in fact, the existing body of rules and regulations is only “semi-formalized”, in that many of the rules are “contradictory, incomplete, and even deliberately ambiguous” (Waterman, Paul and Peterson, 1986, p. 214). Thus, correctly and fully specifying the legal rules of even a very restricted legal domain is difficult, some have said impossibly so $^{2}$ (see e.g., Leith, 1986a, 1986b; Stamper, 1988).

Existing computer-based legal reasoning systems have tried to represent legal rules as production rules (see e.g., Sprowl, 1979, Waterman, Paul and Peterson, 1986) or as Horn clauses (see e.g., Hustler, 1982, Sergot et al, 1986, Stamper, 1980, Sherman, 1987). Limitations identified in these systems include failing to support temporal reasoning, to document the source of a conclusion (e.g., statutory rule or case), and, most importantly, to recognize the hierarchical structure of the rules in a particular legal domain. Production rules and Horn clause logic support only material implication in which a conclusion always follows deductively from the satisfaction of its premises: e.g.,

All humans are mortal. Rule
Socrates is a human. Fact
Therefore Socrates is mortal. Conclusion

Material implication is sufficient to represent and to manipulate legal rules whose conclusions always hold when their premises are satisfied, but it is too strong and too inflexible to represent legal rules whose “status (is) more like that of heuristics than of theorems, in the sense that the joining of antecedents and conclusions is not ironclad” (Rissland, 1988, p. 46). Furthermore, using material implication to represent legal rules suggests that law is immutable, that a conclusion once drawn cannot be altered. But legal rules are neither ironclad nor immutable; legal reasoning is more appropriately described as a “rule-guided activity” than as a “rule-governed” one (emphasis added; Gardner, 1985, p. 249).

Recent advances in the formulation of non-standard logics have presented a means of representing the relative strengths of rules and of reasoning with “weak” rules. Non-monotonic or default logic, (see e.g., Reiter, 1980) allows not only material implication but also weaker forms of implication. A specific branch of default logic, defeasible reasoning, allows both absolute rules and defeasible rules, whose conclusions can be defeated by other rules. $^{3}$ We use defeasible reasoning as a basis for modeling legal reasoning and show how our approach can remedy some problems identified in previous legal reasoning systems. The legal domain addressed here is secured transactions as defined in the Uniform Commercial Code (UCC), Article 9. $^{4}$

An assumption underlying our view of computer-based legal reasoning systems is that their primary purpose is to support the argumentation and justification processes of lawyers and judges. $^{5}$ Thus, we believe that developers of these systems can focus on what the lawyer and judge must focus on: existing statutes, previously decided cases, and secondary legal sources (e.g., in the domain of commercial sales contracts, The Restatement of Contracts and the Official Comments to the Uniform Commercial Code). This reliance on existing rules may produce no original insights or ground-breaking arguments, but we hope that most of the time it will approximate the expertise of a reasonably competent attorney – which is what one would expect a computer-based legal reasoning system to do.

Before presenting our conceptual model and the prototype that illustrates it, we (1) discuss the nature of legal reasoning, (2) define what a legal rule is and describe a procedure for representing statutes and precedents as computable rules, and (3) discuss defeasible reasoning and its applicability to legal reasoning.

## 2. Legal reasoning and defeasibility

## 2.1. The defeasibility of legal rules

The assumption that there are legal rules that must be applied to decide a case does not obviate the fact that legal rules can be incomplete or can point to contradictory outcomes. In fact, most legal systems are structured in such a way that multiple, sometimes conflicting rules may be relevant to a case. Here the reasoning task involves weighing the rules to determine which hold and which are defeated. Unlike the case when reasoning from a static, fully consistent knowledge base, “legal conclusions that appear to follow deductively are in fact defeasible. That is, given the legal rule $[IF Px THEN Qx]$ and the fact Pa, the conclusion Qa is only a default conclusion” (Gardner, 1987, 3.1–3.3).

Most legal systems have a well-defined hierarchy and segmentation of authority, many aspects of which are stipulated explicitly by the system's legislative body. For example, the U.S. Supreme Court's jurisdiction is stipulated in Article III of the Constitution. Cases involving constitutional issues are under the original jurisdiction of the Supreme Court; other cases, e.g., federal cases tried by one of the U.S. District Courts or appealed to one of the U.S. Courts of Appeals, may be appealed before the Supreme Court if they meet the criteria for direct review. The same kind of hierarchy and division of powers is evident in the legislative branch of the American legal system. Thus, the city council of Smalltown, U.S.A. is vested with different powers and holds a different place in the hierarchy than does its State Legislature or the U.S. Senate.

One effect of this hierarchy and segmentation is that multiple, conflicting rules may arise from the decisions issued by these various courts and from the statutes enacted by these legislative bodies. For example, one legal rule may state “If facts A&B&C, then outcome O” whereas another may state “If facts A&B&C, then not outcome O.” Cueto-Rua (1981) labels this an instance of “total incompatibility” which is usually resolved by applying one or more legal principles. One legal principle, lex superior derogat legi inferiori, stipulates that a legal rule issued by a higher authority overrules one issued by a lower authority, thus establishing a hierarchy of norm-enacting bodies in which e.g., federal laws of a particular type may supersede state laws of that same type. Another legal principle, lex posterior derogat legi priori, resolves conflicts in legal rules issued by the same level of the hierarchy by favoring the rule enacted at a later date; e.g., the Eighteenth Amendment to the U.S. Constitution, which prohibited the manufacture, sale and consumption of intoxicating beverages, is defeated by the Twenty-first Amendment, which was enacted at a later date and which permits such activities.

Another conflict-resolving guideline involves the jurisdiction or scope of a legal rule, i.e., its area of authority. For example, the Uniform Commercial Code (UCC) has been ratified and adopted by 49 of the 50 state legislatures; Louisiana, the exception, has adopted only parts of the Code. Thus, the Code gives authoritative legal rules governing commercial transactions in most of the U.S, but its rules may have no implicit authority in transactions between parties in Texas and Louisiana or between parties in Texas and Japan, unless these parties explicitly specify the Code as the law governing their transactions. Furthermore, the UCC is applicable only to transactions involving personal property; real estate transactions are outside its scope. If a rule in the UCC conflicts with a rule in another legal text, that conflict can likely be resolved by examining the jurisdictions of the conflicting rules.

Where none of these principles applies, it may be that the conflict can be resolved only by interpreting one rule as an exception to the other. For example, the second rule in the example above might be interpreted as “If facts A&B&C&D, then not outcome O” – thereby making the second rule an exception to the first and thus capable of defeating the first, more general rule. In fact, the legal rules stated in a statute are often represented in defeasible form to help individuate the rules and to make them memorable (Gordon, 1987). Typically a statute states a general rule and presents its exceptions as separate rules. As a result, several rules may seem applicable to a given situation, each rule potentially yielding a different conclusion. This phenomenon is illustrated by the following set of rules:

If facts A & B then outcome O.

If facts A&B&C then not outcome O.

If facts A&B&D then outcome Q.

For example, under the Uniform Commercial Code, Article 9, the general rule determining priorities among conflicting security interests in collateral is that, when both security interests are perfected $^{6}$ , the first to file or perfect has priority (UCC 9-312(5a)). However, another rule stipulates that, regardless of time of filing or perfecting, a purchase money security interest may have priority over a regular security interest if certain requirements are met (UCC 9-312(4)). Yet additional exceptions to the general rule may protect neither party's claim, instead protecting the rights of innocent third parties (e.g., UCC 9-307, 9-308, and 9-309). Resolving these conflicts requires another legal principle, lex specialis derogat legi generali, which stipulates that a more specific law defeats a more general one; that is, a rule that covers more facts of the case defeats a general rule. Resolving conflicts by examining the specificity of the applicable legal rules is the focus of our research.

## 2.2. The applicability of defeasible reasoning to law

Because legal rules are defeasible, the classic inference rule – modus ponens – may not always apply in legal reasoning. Thus classical first-order predicate logic may be an insufficient tool for reasoning in domains where knowledge is incomplete or uncertain; what is needed is “an inference rule that permits us to make somewhat temporary, or default, assumptions that can later be revised when additional qualifications become important” (Genesereth and Nilsson, 1987, p. 117). Defeasible reasoning, a form of non-monotonic logic, provides such inference mechanisms. By using defeasible reasoning as the inference engine of a legal reasoning system, we can represent the varying strength of legal rules. For example, well-established rules that are fixed by statute or legislative enactment and whose meaning has not been questioned can be represented as absolute rules, subject to the material implication of classical logic. Less well-established rules that may be defeated by competing rules can be represented as defeasible rules subject to a weaker form of implication.

Legal principles, the general statements of the values underlying legal rules – e.g., that no one should profit from his own wrong-doing, $^{7}$ are logically different from legal rules in that legal rules “are applicable in an all-or-nothing fashion”; in contrast, a legal principle does not “set out antecedents that make its application necessary. Rather it states a reason that argues in one direction, but does not necessitate a particular decision” (Dworkin, 1977, pp. 45–47). Functioning in a similar capacity in a legal system as defeaters do in defeasible reasoning, “principles … incline a decision one way, though not conclusively, and they survive intact when they do not prevail” (Dworkin, 1977, p. 56). Legal principles, especially basic assumptions about the “absence of vitiating factors such as fraud, duress, mistake, and so on” (MacCormick, 1974, p. 126), might be represented as defeaters that make it impossible to predict what conclusion a judge will reach. Legal rules, a method of representing them in computable form, and a defeasible reasoning formalism for determining their applicability to a case are the focus of the rest of this paper.

## 3. Representing legal rules

Legal rules generally fall into one of two categories: (1) normative rules that guide human behavior in society or (2) definitional rules that define the criteria for bringing about certain legal states. Both types of legal rules can be represented as conditional IF $\langle$ antecedent $\rangle$ THEN $\langle$ consequent $\rangle$ statements (Twining and Miers, 1982). For example,

IF debtor D gives creditor C a security interest in collateral Z

AND debtor D defaults on his loan

(normative rule)

THEN creditor C has the right to repossess collateral Z.

IF creditor C has a security interest in collateral Z of debtor D

AND collateral Z is a tangible good

(definitional rule)

AND creditor C files a financing statement

THEN creditor C has a perfected security interest in collateral Z.

The antecedent of a legal rule gives the conditions under which the rule applies, i.e., the acts that must have occurred or the criteria that must be met in order for the consequent to be true. The consequent gives the legal consequences of performing the actions or the legal state achieved by satisfying the criteria.

Legal rules can be represented in predicate logic, in which a rule is a syntactic structure that allows one to deduce from some set of predicates in the antecedent that another predicate (or predicates) in the consequent is true. If the interpretation of the symbols used to represent these predicates is correct, then this deduction may be made mechanically. To represent legal rules in our prototype, we use a restricted predicate logic that supports defeasible reasoning. For example, the legal rule defining collateral as a consumer good ${}^{8}$ can be represented in the following predicate logic notation:

IF good(Collateral)

AND bought(Debtor, Collateral, for \_personal \_use)

THEN consumer\_good(Collateral).

Representing legal rules as predicate logic statements involves identifying the basic individuals, properties, and relations expressed in the legal rules. Individuals are expressed as variables (e.g., Debtor, Collateral) or individual constants (e.g., instantiating the variable Debtor with 'John Smith'). Properties are expressed as one-place predicates, e.g., consumer\_good(Collateral), which states that the Collateral has the property of being a consumer good. Relationships between individuals are expressed as relations, e.g., bought(Debtor, Collateral, for \_personal \_use), which states that the debtor bought the collateral for his own personal use. In our implementation, the closed vocabulary is presented in all capital letters, e.g., IF, THEN, AND. Open vocabulary predicate constants are presented in lower case, e.g., good, bought, consumer\_good. Variables can be represented as single upper case letters, e.g., X, Y, Z, or as words in mixed case, e.g., Debtor, Collateral.

## 4. Defeasible reasoning

## 4.1. General characteristics

Systems of defeasible reasoning (See e.g., Belzer, 1986, 1987; Belzer and Loewer, 1988; Causey (see article in this issue); Gordon, 1987; Nute, 1985, 1988, 1989a, 1989b) have several features in common, although each system formalizes these concepts in different ways. For example, most systems of defeasible reasoning support not only the traditional form of material implication represented by

IF <antecedent>

THEN $\langle$ consequent $\rangle$ .

but also a weak form, which can be represented by

IF〈antecedent〉

PRESUMABLY $\langle$ consequent $\rangle$ .

The first is variously called “an absolute rule” (Nute, 1989a), “a nondefeasible rule” (Causey, this issue), a “beyond reasonable doubt” rule (Belzer and Loewer, 1988), or “an all-things-considered norm” (Belzer, 1987). The second is variously called “a defeasible rule” (Causey, this issue; Nute, 1989a), a “favored” proposition (Belzer and Loewer, 1988), or “a prima facie norm” (Belzer, 1987). Whatever the name given these concepts, all systems recognize the need for a weaker form of implication whose conclusions can be retracted as more information becomes available. Thus, one problem addressed by defeasible reasoning is the real-world necessity of reasoning with incomplete, dynamic information.

Another feature of defeasible reasoning formalisms is a mechanism for ranking rules. Again, this ranking is performed under different guises. For example, Gordon (1987) assigns rules to types and explicitly states the rank order among types. In contrast, Nute (1989a) uses “specificity” to implicitly order rules by recognizing that a more specific rule can defeat a more general rule; Rule A is “more specific” than Rule B if the conditions in the antecedent of Rule B are a subset of those in the antecedent of Rule A. Typically, this ranking of rules yields a partial order, which fits our intuitive notion that, although rules vary in their strength, we cannot always rank one as higher or lower in the order than another one. For example, consider three rules about the situation of driving to work:

IF approaching\_ intersection AND flashing\_yellow\_light THEN proceed\_with\_caution.

IF approaching intersection

AND flashing\_yellow\_light

AND greyhound\_bus\_approaching\_at\_high\_speed

THEN stop.

IF late\_for\_work
THEN take\_shortcut.

Although the first and second rules yield opposite conclusions, we can resolve this conflict by explicitly or implicitly ranking the second rule higher than the first rule. The added condition of the second rule causes it to defeat the more general rule, so we stop at the intersection. But the third rule is neither obviously superior to nor inferior to the other two rules. However, this is not a problem in that the third rule does not compete with the first two.

In this section, we discuss these features of defeasible reasoning in more detail and introduce a prototype legal reasoning system implemented in a modified version $^{9}$ of d-Prolog (Nute and Lewis, 1985), a programming language designed to support the heuristics of defeasible reasoning (Nute, 1985a). To avoid the confusion inherent in discussing the specific features of several defeasible reasoning formalisms and to ensure that this discussion coheres with the d-Prolog implementation, we focus on Nute's Defeasible Logic $^{10}$ (Nute, 1985, 1989a, 1989b). However, it is important to note that all the defeasible reasoning systems mentioned here can resolve conflicts between competing rules by supporting the legal principle lex specialis derogat legi generali. $^{11}$

Recognizing the importance of temporal reasoning in most legal domains, we have extended d-Prolog to support operations on Julian calendar dates, thus providing certain temporal reasoning capabilities such as (1) comparing dates to determine precedence and (2) adding and subtracting an integer number of days or months from one date to determine a second date, e.g. a date 30 days or 3 months from the current date. The operators supported are as follows $^{12}$ :

equality . = .
temporal precedence . < .
. < = .
temporal succession . > .
. > = .
inequality . < > .

temporal addition +.

temporal subtraction .-.

## 4.2. Non-monotonicity: Reasoning with a dynamic knowledge base

Nute's Defeasible Logic (1985, 1989a, 1989b) is a proof-theoretic form of non-monotonic reasoning based on conditional logic. Compared to monotonic reasoning based on classical first-order logic, non-monotonic reasoning is characterized as follows:

Say that F and G are sets of first-order logic formulas and f is a first-order logic formula. Monotonicity states that if F is a subset of G, whenever f is inferable from F, f will also be inferable from G. Non-monotonicity states that when F is a subset of G, even though f is inferable from F, f may not be inferable from G.

Intuitively, a non-monotonic system is one in which the conclusions drawn from existing knowledge may change when certain new knowledge is added. For example, assume that the following fact is observed:

F1: John has made a contract.

Also assume the following rules (See e.g., Calamari and Perillo, 1987, § 8-4):

R1: A contract is enforceable.

R2: A contract made by a minor can be disaffirmed at the minor's option, i.e., may not be enforceable.
R3: A minor's contract to repay an educational loan is enforceable.

From the above knowledge, one can infer, by applying R1, that “John’s contract is enforceable.” However, assume that the following facts are also observed:

F2: John is a minor.

F3: John has disaffirmed his contract.

With the additional knowledge, one concludes, from R2, that “John’s contract is not enforceable.” This conclusion contradicts the previous conclusion. However, since R2 describes a special case – in essence, an exception to R1, the conclusion drawn from R1 is defeated. Say that the following fact is further observed:

F4: John's contract involves repaying an educational loan.

Then, R3 is most applicable, and we must deny the previous conclusion, again stating that “John’s contract is enforceable.” In a non-monotonic system, additional knowledge (i.e., facts and rules) may deny conclusions drawn without that knowledge.

Defeasible reasoning provides an expressively powerful system to automate reasoning with incomplete and dynamic knowledge and to resolve conflicts between conflicting rules. Knowledge consists of facts and rules. Facts are expressions of actual situations that are observed or known. In our implementation a fact is represented by the operator FACT followed by a (ground) $^{13}$ predicate expression consisting of a predicate symbol followed by n constants. For example, the one-place predicate minor('John') following the operator FACT means that "John is a minor." The binary predicate party(contract1, 'John') following the operator FACT indicates that "John is a party to contract1." We also represent a weaker form of fact, a presumption, using the operator PRESUMPTION. For example, PRESUMPTION innocent('John') indicates that, until we receive evidence to the contrary, we must presume that John is innocent.

In Defeasible Logic (Nute, 1989a, 1989b), the operator NEG is used for explicit negation. For example, if both enforceable(X) and NEG enforceable(X) are derived from the same set of facts, the situation described by the facts is contradictory. In defeasible reasoning, negation is interpreted as contrary; thus, defeasible reasoning allows clauses with negative conclusions. A negative conclusion, NEG P, is drawn when a clause having NEG P as its conclusion or a clause having a contrary of P as its conclusion is applicable without being defeated. For example, the conclusion NEG P is drawn in two situations:

1. when IF P1 AND P2 PRESUMABLY NEG P is applicable without being defeated, or

2. when IF Q1 AND Q2 PRESUMABLY Q is applicable without being defeated and incompatible(P,Q) is declared as the relationship between P and Q.

In classical first-order logic, a rule may be represented by the logical implication IF...THEN. Due to the monotonicity of classical first-order logic, such rules are absolute and truth-preserving. For example, if we have a rule IF P THEN Q, when P is given, we conclude Q by modus ponens. However, in defeasible reasoning, we have a weaker version of implication, which we indicate by IF $\langle$ antecedent $\rangle$ PRESUMABLY $\langle$ consequent $\rangle$ . A rule with this connective is called a defeasible rule. A defeater, expressed using the connective IF $\langle$ antecedent $\rangle$ MAYBE $\langle$ consequent $\rangle$ , is another kind of rule that expresses a presumption or possibility but does not force a particular conclusion. For example, when the two rules

IF P1
PRESUMABLY Q.

IF P1
AND P2
MAYBE NEG Q.

are given with the facts P1 and P2, the second rule, which is a defeater, defeats the first rule so that we may not conclude Q. However, we may not conclude NEG Q, either. In other words, the defeater prevents us from drawing a conclusion that is contrary to the consequent of the defeater. An example of a defeater in our contracting scenario is provided by the legal doctrine of unconscionability. According to this doctrine, a court may refuse to enforce a contract whose terms are oppressively unfavorable to one of the parties (UCC 2-302). If a contract is unconscionable, one cannot presume that it is either enforceable or not enforceable; all one can presume is that it might not be enforceable. This defeater can be expressed in the following notation:

IF contract(X)
AND unconscionable(X)
MAYBE NEG enforceable(X).

The above example of contracting with a minor can be represented by the following rules:

IF contract(X)
PRESUMABLY enforceable(X).

(R1)

IF contract(X)
AND party(X, Y)
AND minor(Y)
PRESUMABLY NEG enforceable(X).

(R2)

IF contract(X)
AND party(X, Y)
AND minor(Y)
AND educational\_loan\_repayment(X)
PRESUMABLY enforceable(X).

and the following facts:

<table><tr><td>FACT contract(contract1).</td><td>(F1)</td></tr><tr><td>FACT party(contract1, ‘John’)</td><td>(F2)</td></tr><tr><td>FACT minor(‘John’).</td><td>(F3)</td></tr><tr><td>FACT disaffirmed(‘John’, contract1).</td><td></td></tr><tr><td>FACT educational_loan_repayment(contract1).</td><td>(F5)</td></tr></table>

## 4.3. Specificity: Resolving conflicts between rules

The central idea of a defeasible reasoning system is resolving conflicts among rules by determining which rule is “more applicable.” Being able to evaluate the applicability of a rule is an asset in a legal reasoning system because often more than one rule will be relevant to the case under consideration. Where conflicting rules can be applied to the same set of facts, defeasible reasoning attempts to resolve the conflict by determining whether one rule is superior to the other. The superiority of a rule is determined by the following guidelines, which we believe exhaust all possible situations in which one rule might compete with another:

1. When both are absolute rules, neither is superior. Therefore, the result is contradiction.

2. When one is an absolute rule and the other is either a defeasible rule or a defeater, the absolute rule is superior, and its consequent is deduced.

3. When one is a defeasible rule and the other is a defeasible rule, if the antecedent of the first defeasible rule is derivable from the antecedent of the second defeasible rule, the second is superior to the first, and the conclusion drawn is the consequent of the second rule.

4. When one is a defeasible rule and the other is a defeater, if the antecedent of the defeasible rule is derivable from the antecedent of the defeater, the defeater is superior. Since a defeater does not allow us to make any conclusion, the result is no conclusion.

5. When both are defeasible rules or both are defeaters or when one is a defeasible rule and the other is a defeater, if no derivability is obtained between the antecedent of the rules, neither is superior. Therefore, the result is contradiction.

6. When both are defeaters, if the antecedent of one is derivable from the antecedent of the other, the latter is superior. However, since the defeater does not allow us to make any conclusion, the result is no conclusion.

The derivability of the antecedent of one rule from the antecedent of another rule is called specificity. Specificity determines whether a defeasible rule may be defeated or denied by a rule that is “more informative” $^{14}$ about the situation. For example, say that we are given two defeasible rules:

R1: IF strike(match)

PRESUMABLY light(match).

R2: IF strike(match)
AND wet(match)
PRESUMABLY NEG light(match)

$^{14}$ Both this term and the following example are from (Covington, Nute and Vellino, 1988, p. 342).

and the facts strike(match) and wet(match). From the first rule, one may conclude that the match lights; from the second rule, that the match does not light. Since the second rule covers or provides more information about the actual situation, it defeats the first rule, and we have only one conclusion: that the match does not light. Similarly, in our contracting example, specificity determines that R3 is more informative than R2; that is, the antecedent of R2 is derivable from the antecedent of R3. Therefore, R3 defeats R2, so we conclude that the contract is enforceable.

Under the laws of contracting, contracts are of one of four types: enforceable, voidable, void, and unenforceable (Calamari and Perillo, 1987, § 1-11). An enforceable contract is one that, if breached, entitles the offended party to sue for damages or performance. A voidable contract is an enforceable contract unless one or both parties, having the option to void the contract, explicitly do void the contract. A void contract is not a contract at all in that it creates no legal obligations and is not legally enforceable. An unenforceable contract is one that may have legal effect but that cannot be enforced for damages or performance because it fails to meet e.g., the statute of limitations or the Statute of Fraud requirement of a signed writing. $^{15}$ As this discussion shows, the predicate NEG enforceable(X), therefore, includes two cases: void(X) and unenforceable(X).

In a domain such as contract law, where we need to represent states that are not just binary – e.g., on, off; P, not P – contrary states must be expressed explicitly. To handle this domain constraint, defeasible reasoning uses the relation incompatible. For example, incompatible(enforceable(X), void(X)) states that we may not conclude that a contract is both enforceable and void. Similarly, the relation incompatible(enforceable(X), unenforceable(X)) states that we may not conclude that a contract is both enforceable and unenforceable. Using the four types of contracts and the INCOMPATIBLE relation, we can re-represent the rules of our contracting scenario as follows:

IF contract(X)
PRESUMABLY enforceable(X).

IF contract(X)
AND party(X, Y)
AND minor(Y)
PRESUMABLY voidable(X).

(R1')

IF contract(X)
AND party(X, Y)
AND minor(Y)
AND disaffirm(Y, X)
PRESUMABLY void(X).

(R2'a)

(R2'b)

IF contract(X)
AND party(X, Y)
AND minor(Y)
AND disaffirm(Y, X)
AND educational\_loan\_repayment(X)
PRESUMABLY enforceable(X).

(R3')

together with two contrary declarations:

incompatible(enforceable(X), void(X)).
incompatible(enforceable(X), unenforceable(X)).

It should be noted that in this revision of the rules, both R1' and R2'a could be applicable to a situation but that there is no intrinsic contradiction between their results: a voidable contract is enforceable unless and until the party with the ability to void the contract does so.

## 5. An example of defeasible reasoning in law

The domain we have chosen to illustrate the effectiveness of defeasible reasoning in law is the priority of conflicting security interests under the Uniform Commercial Code (UCC), Article 9. Article 9 can be viewed as a set of rules governing secured credit commercial transactions. The Official Comments to UCC 9-101 state that

The aim of this Article is to provide a simple and unified structure within which the immense variety of present-day secured financing transactions can go forward with less cost and with greater certainty.

Given that the law of secured transactions is one of the more settled subsystems of law and that the drafters' purpose in Article 9 was to clearly and systematically detail the procedures for creating and enforcing security interests, this domain seems to be amenable to rule-based legal reasoning. Secured transactions represent a large percentage of major business and consumer purchases, making this a domain whose recurrent problems could benefit from an automated legal reasoning system.

Article 9 governs the creation (or in legal terms, the attachment) of a security interest, a creditor's interest in the collateral used to secure a loan or to secure the purchase of the collateral itself. For example, Joe Smith, owner of Joe's Sporting Goods (the debtor), needs \$10,000 to buy inventory for his store. In exchange for a security interest in his inventory (the collateral) and his promise to repay, First National Bank (the secured party or creditor) lends Joe the money he needs and requires Joe to sign a security agreement stating the facts of their contract. The security interest in this example is commonly called a purchase money security interest because the creditor loans money to enable the debtor to purchase the item used as collateral for the loan.

Article 9 also governs the perfection of a security interest in collateral. Perfection is a legal act whereby the creditor takes possession of the collateral or files a financing agreement (usually with the Secretary of State) to assert his rights to the collateral. The rules for perfecting a security interest are in themselves fairly straightforward. Of greater complexity and interest are the rules governing the priorities among conflicting security interests, that is, among multiple creditors claiming a security interest in the same collateral. The following section discusses some of these rules and presents excerpts of our rulebase.

## 5.1. The hierarchy of rules governing priorities among creditors

The most fundamental rules governing priority of security interests are (1) that a perfected security interest has priority over an unperfected one ${}^{16}$ ; (2) that, if both security interests are perfected, then the first to file has priority; and (3) that, if neither security interest is perfected, then the first to attach a security interest has priority ${}^{17}$ :

## Rule 1:

IF attached\_security\_interest(Creditor1, Debtor, Collateral, ADate1)
AND attached\_security\_interest(Creditor2, Debtor, Collateral, ADate2)
AND perfected\_interest(Creditor1, Debtor, Collateral, Date1),

$^{16}$ No section of the UCC explicitly states that a perfected security interest has priority over an unperfected one, but this rule can be inferred from the sections cited here. See also Bloom v. Hilty 427 Pa. 463, 234 A.2d 860 (1967).

$^{17}$ The final argument of the “priority” predicate indicates the section of the UCC in which the rule is stated.

AND NEG perfected\_interest(Creditor2, Debtor, Collateral, Date2)

AND NEG real\_estate\_interest(Creditor1, Real\_property)

AND NEG real\_estate\_interest(Creditor2, Real\_property)

PRESUMABLY priority(Creditor1, Creditor2, Debtor, Collateral, '9-312(5)/9-301(1a)').

## Rule 2:

IF perfected interest(Creditor1, Debtor, Collateral, Date1)

AND perfected\_interest(Creditor2, Debtor, Collateral, Date2)

AND NEG real\_estate\_interest(Creditor1, Real\_property)

AND NEG real\_estate\_interest(Creditor2, Real\_property)

AND Date 1. <. Date2

PRESUMABLY priority(Creditor1, Creditor2, Debtor, Collateral, '9-312(5a)').

## Rule 3:

IF NEG perfected interest(Creditor1, Debtor, Collateral, PDate1)

AND NEG perfected\_interest(Creditor2, Debtor, Collateral, PDate2)

AND attached\_security\_interest(Creditor1, Debtor, Collateral, Date1)

AND attached\_security\_interest(Creditor2, Debtor, Collateral, Date2)

AND NEG real\_estate\_interest(Creditor1, Real\_property)

AND NEG real\_estate\_interest(Creditor2, Real\_property)

AND Date1.<.Date2

PRESUMABLY priority(Creditor1, Creditor2, Debtor, Collateral, '9-312(5b)').

However, these general rules are defeasible rules, applicable only in situations where more specific rules do not apply. An example of a more specific rule that may defeat the “first-to-file” priority rule (Rule 2) is the rule governing a purchase money security interest (pmsi) in inventory:

## Rule 4:

IF inventory(Collateral, Creditor, Debtor)

AND perfected\_interest(Creditor1, Debtor, Collateral, Date1) \*

AND perfected\_interest(Creditor2, Debtor, Collateral, Date2) \*

AND Date1 . < . Date2

AND pmsi(Creditor2, Debtor, Collateral)

AND received possession(Debtor, Collateral, RPDate)

AND Date2 . < . RPDate

AND gave\_notice\_in\_writing(Creditor2, Creditor1, NDate)

AND NDate . < . Date2

AND received\_notice(Creditor1, RNDate)

AND RNDate. $< = .$ RPDate + 5 years

PRESUMABLY priority(Creditor2, Creditor1, Debtor, Collateral, '9-312(3)').

Note: The starred predicates in Rule 4 are the same predicates as Rule 2.

By the rules of specificity (see the third guideline for determining superiority listed in Section 4.3), because Rule 2 is derivable from Rule 4, Rule 4 can defeat Rule 2. According to Rule 4, when collateral subject to a purchase money security interest in inventory is also covered by an earlier creditor's "after-acquired property" clause, the purchase money creditor will have priority if the conditions stated in the rule are met.

For example, assume that on July 5, Joe Smith, owner of Joe's Sporting Goods, signs a security agreement with Bank One, which includes a clause giving Bank One a security interest in all property acquired by Joe during the time that his loan with Bank One is outstanding. Bank One files to perfect its interest on July 13. On November 17, Joe borrows \$10,000 from First National Bank and gives First National a security interest in the inventory he purchases with the loan, thus creating a purchase money security interest, which First National files to perfect on November 21. Now both Bank One and First National have perfected security interests in Joe's inventory. If First National both (1) gives Bank One the required notice before Joe receives possession of the inventory and (2) files to perfect its interest before, or within 10 days after, Joe receives possession of the inventory, First National will have priority. In a similar situation involving goods other than inventory, the rule giving the purchase money secured creditor priority (See UCC 9-312(4)) is somewhat simpler:

## Rule 5:

IF perfected\_interest(Creditor1, Debtor, Collateral, Date1)

AND perfected\_interest(Creditor2, Debtor, Collateral, Date2) \*

AND Date1 . < . Date2

AND NEG inventory(Collateral, Creditor, Debtor)

AND pmsi(Creditor2, Debtor, Collateral)

AND received possession(Debtor, Collateral, RPDate)

AND Date 1. <= .RPDate .+. 10 days

PRESUMABLY priority(Creditor2, Creditor1, Debtor, Collateral, '9-312(4)').

Again, starred predicates are the same as those of Rule 2.

Another set of rules (UCC 9-313) governs situations in which two parties have conflicting interests in collateral that has become a fixture (e.g., a central heating or cooling system, a water heater or other appliance attached to and not easily removed from real estate). The parties in this situation are usually a creditor who holds a security interest in the fixture as personal property and one who owns or holds an interest in the real estate to which the fixture is attached. For example, assume that Joe Smith, the proprietor of Joe's Sporting Goods used in our earlier example, rents space in a building owned by Larry Landlord, who has given CreditBanc a mortgage on the building. On August 28, Joe buys an air conditioning system from Prime Systems, using Prime's repayment plan and giving Prime a security interest in the air conditioning system. The system is installed in Joe's business on August 30. Prime files to perfect its security interest on September 3.

In this hypothetical, both CreditBanc and Prime Systems have an interest in Joe's air conditioning system: CreditBanc by virtue of its mortgage on the real estate on which the system has been installed and Prime Systems by virtue of its purchase money security interest. If Joe defaults on his loan with Prime or if Larry defaults on his mortgage with CreditBanc, a court may have to decide which creditor has priority in claiming its interest in the air conditioning system. Two of the several rules governing interests in fixtures are the following:

## Rule 6:

IF fixture\_in(Collateral, Real\_property)
AND real\_estate\_interest(Creditor2, Real\_property)
AND owner(Owner, Real\_property)
AND attached\_security\_interest(Creditor1, Debtor, Collateral, ADate1)
AND attached\_interest(Creditor2, Owner, Real\_property, ADate2)
PRESUMABLY priority(Creditor2, Creditor1, Debtor, Collateral, '9-313(7)').

![](/api/attachments/NXX8PBC8/fulltext/images/acba14a03e4ba16d5c61f5ff7f3166001d9529ebfb4db26d274cb9ee214a3cb9.jpg)  
Fig. 1. Partial ordering of priority rules.

## Rule 7:

IF fixture\_in(Collateral, Real\_property) \*

AND real\_estate\_interest(Creditor2, Real\_property) \*

AND owner(Owner, Real\_property) \*

AND attached\_security\_interest(Creditor1, Debtor, Collateral, ADate1) \*

AND attached\_interest(Creditor2, Owner, Real\_property, ADate2)

AND became\_fixture(Collateral, Install\_Date)

AND pmsi(Creditor1, Debtor, Collateral)

AND ADate2 . < . Install\_Date

AND filed\_financing\_statement(Creditor1, Debtor, Collateral,

real\_estate\_recorder, FDate)

AND FDate .<=. Install\_Date .+. 10 days

AND has\_interest\_in(Debtor, Real\_property)

PRESUMABLY priority(Creditor1, Creditor2, Debtor, Collateral, '9-313(4a)').

Again, notice that the starred predicates in the antecedent of Rule 7 are the same as those in the antecedent of Rule 6.

Rule 6 is the most general rule governing conflicts among interests in fixtures. According to this rule, the creditor that financed the owner's purchase of the real property to which the fixture is attached (e.g., CreditBanc) has priority over the creditor that financed the debtor's purchase of the good that has become a fixture (e.g., Prime Systems). Rule 7 gives an exception to this general rule, stating that, if the fixture financer “fixture filed” $^{18}$ before the good became a fixture and after the real estate financer took an interest in the real property, then the fixture financer will have priority. In our hypothetical, according to Rule 6 CreditBanc has priority. But Rule 6 covers only the general case; if a more specific rule is applicable to the situation, that rule should be used to determine priority. Rule 7, which is more specific, defeats Rule 6, so we conclude that Prime Systems has priority because it holds a purchase money security interest and it perfected within 10 days of installing the air conditioning system.

These statements of some of the rules governing priority illustrate the hierarchy of rules in this domain. As the scenarios show, this system of rules is partially ordered: the most general rules being 9-312(5a)/9-301, 9-312(5a), 9-312(5b), and 9-313(7), as shown in Figure 1.

## 5.2. A hypothetical to test the system

To illustrate the workings of our prototype legal reasoning system, we have represented the rules and facts related to a hypothetical. $^{19}$ This hypothetical involves the conflicting interests of secured creditors who have an interest in goods that had become fixtures. As of January 1, 1988, the first creditor, Friendly Financial, holds a mortgage on the apartment complex, Town Lake Apartments, owner by landlord. First Financial has filed in the Town Clerk's office (real\_estate\_recorder) as required by real estate law. The second creditor, Anderson Appliances, executed a conditional sales contract (i.e., a contract for sale and a security agreement) with Miss Julia on January 2, 1989, taking a security interest in the oven, which was installed on January 10 (i.e., we assume it became a fixture on that date). Although, as a purchase money security interest (pmsi), Anderson's security interest in the oven (a consumer good under UCC 9-109(1)) was automatically perfected (UCC 9-302(1d)), Anderson Appliances filed a financing statement in the Town Clerk's office on January 8 as required to retain priority in a fixture (UCC 9-313(1b) and 9-313(4a)).

```txt
?- @has _perfected _interest(Creditor, Debtor, Collateral, Date, Rule).
Creditor = 'Anderson Appliances', Debtor = 'Miss Julia', Collateral = oven,
Date = 1/2/89,
Rule = '9-302(1d)';
```

A full listing of the rulebase used in this hypothetical is given in Appendix 1. The stated facts and ancillary facts are listed below:

FACT consumer\_good(oven, 'Anderson Appliances', 'Miss Julia').

FACT fixture\_in(oven, 'Town Lake Apts').

FACT became \_fixture(oven, 1/10/89).

FACT signed\_security\_agreement('Miss Julia', 'Anderson Appliances', oven, 1/2/89).

FACT gave\_value('Anderson Appliances', 'Miss Julia').

FACT has\_rights\_in('Miss Julia', oven, 1/2/89).

```txt
FACT filed_financing_statement('Anderson Appliances', 'Miss Julia',
```

oven, real\_estate\_recorder, 1/8/89).

FACT attached\_interest('Friendly Finance', landlord, 'Town Lake Apts', 1/1/88).

FACT pmsi('Anderson Appliances', 'Miss Julia', oven).

FACT owner(landlord, 'Town Lake Apts').

FACT has\_interest\_in('Miss Julia', 'Town Lake Apts').

FACT real\_estate\_interest('Friendly Finance', 'Town Lake Apts').

Based on these facts we can query the system, asking the following questions:

1. Which creditor(s) has/have attached a security interest to the collateral of a debtor?

2. Which creditor(s) has/have perfected an interest in a debtor's collateral and by what rule?

3. If two or more creditors have a security interest in the collateral of a debtor, who are they, what is the priority between them, and which rule determines this priority?

The results of these queries are shown below, where the bold-faced type indicates the user's query and where 'no' indicates that no answer is derivable or that there are no more answers.

```txt
?- @attached_security_interest(Creditor, Debtor, Collateral, Date).
Creditor = 'Anderson Appliances', Debtor = 'Miss Julia', Collateral = oven,
Date = 1/2/89;
no
```

?- @priority(Creditor1, Creditor2, Debtor, Collateral, Rule).
    Creditor1 = 'Anderson Appliances', Creditor2 = 'Friendly Finance',
    Debtor = 'Miss Julia', Collateral = oven, Rule = '9-313(4a)'';
no

The responses to @has\_perfected\_interest(Creditor, Debtor, Collateral, Date, Rule) indicate that Anderson Appliances has a perfected security interest in Miss Julia's oven as of January 2 by virtue of its automatic perfection of a purchase money security interest in consumer goods (UCC 9-302(1d)) and as of January 8 by virtue of its filing a finance statement regarding the fixture (UCC 9-313(1b)) with the "real\_estate\_recorder." Of most interest in terms of the system's defeasible reasoning capability is the answer to the priority question. Although the conditions in both Rule 6 – whose conclusion gives Friendly Finance priority – and Rule 7 – which gives Anderson Appliances priority – are satisfied by the facts presented, Rule 7, being more specific, defeats Rule 6, causing the system to conclude that Anderson Appliances has priority by virtue of UCC 9-313(4a).

If we modify the facts, changing the current filed\_financing\_statement fact to

FACT filed\_financing\_statement('Anderson Appliances', 'Miss Julia', oven, sec\_of\_state, 1/8/89).

the system provides different answers:

?- @has \_perfected \_interest(Creditor, Debtor, Collateral, Date, Rule).
    Creditor = 'Anderson Appliances', Debtor = 'Miss Julia', Collateral = oven,
    Date = 1/2/89,
    Rule = '9-302(1d)';
no

```txt
?- @priority(Creditor1, Creditor2, Debtor, Collateral, Rule).
    Creditor1 = 'Friendly Finance', Creditor2 = 'Anderson Appliances',
    Debtor = 'Miss Julia', Collateral = oven, Rule = '9-313(7)';
no
```

Because Anderson Appliances filed its financing statement in the wrong office (that is, with the sec\_of\_state – Secretary of State – instead of with the real\_estate\_recorder), Anderson has a perfected security interest only by virtue of the automatic perfection of a purchase money security interest in consumer goods; more importantly, Anderson Appliances has lost its special priority. Now the more general rule, UCC 9-313(7), gives Friendly Finance a priority interest in Miss Julia's oven. However, if we alter our fact base once more, adding the following:

PRESUMPTION fraud('Friendly Finance')

and ask the priority question again,

## ?- @priority(Creditor1, Creditor2, Debtor, Collateral, Rule). no

the system is unable to draw any conclusion. Normally, because Anderson Appliances filed incorrectly, Friendly Finance would have priority as stated above, but where the priority party is presumed to have committed fraud, the defeater

IF fraud(Creditor1)
MAYBE NEG priority(Creditor1, Creditor2, Debtor, Collateral, Rule).

defeats the general rule (i.e., UCC 9-313(7)) that would have given Creditor1 (i.e., Friendly Finance) priority. Nor can we conclude that Anderson Appliances has priority. Thus, the system responds “no” – indicating that no conclusion is derivable.

## 6. Conclusions and future research

Defeasible reasoning seems to be an expressive, flexible formalism for representing and reasoning about incomplete, dynamic facts and competing rules. The concept of a defeater, as implemented in Nute's Defeasible Logic, provides capabilities not supported by earlier logics, e.g. non-monotonic logic (McDermott and Doyle, 1980) and default logic (Reiter, 1978). Using this concept to prevent the drawing of a contrary conclusion effectively mirrors the open-endedness of legal reasoning in which one cannot always predict the outcome of a case. Furthermore, the ordering of rules supported by all the defeasible reasoning formalisms discussed in this paper helps to resolve conflicts by stipulating that more specific rules can defeat general rules. Although not sufficient in themselves to cover all problems in legal reasoning, $^{20}$ the concept of a defeater and the partial ordering of rules seem to be necessary features in a formalism to support legal reasoning.

A defeasible reasoning approach to legal reasoning may overcome two limitations of systems using a standard Horn clause logic programming approach. First, in Horn clause logic programming, negative information is inferred by the negation as failure rule (Clark, 1978): if fail to infer P, infer not P. As shown in Apt (1988), negation as failure is a restricted form of the closed world assumption (Reiter, 1978) in which whatever is unknown is assumed to be false. $^{21}$ Therefore, negation as failure can be used appropriately only when the closed world assumption is acceptable. In legal reasoning, however, this assumption does not hold. $^{22}$

A second limitation of standard Horn clause logic is that its negation as failure allows only a limited form of non-monotonic reasoning. Sergot et al. (1986) used only negation as failure to handle the non-monotonicity inherent in legal reasoning and were unable to derive negative conclusions. In contrast, defeasible logic uses explicit negation and specificity, not only supporting non-monotonicity but also implicitly ordering competing rules, thereby resolving conflicts that Sergot et al.'s standard Horn clause logic approach could not address. Compared to standard Horn clause predicate logic, defeasible logic seems to be a more flexible, powerful, and expressive formalism that can handle negative, incomplete, and contradictory information in a more natural manner.

Nonetheless, the legal reasoning system described here has limitations of its own. One limitation is the absence of an explanation facility in our prototype. Ideally, a legal reasoning system should provide all of the richness of EVID's (Causey, this issue) justification procedure, allowing the user to query the system to inquire how (i.e., absolutely or defeasibly) and why (i.e., by what rules) a conclusion holds and how a particular conclusion can be defeated. These features, especially the second one, would be very useful to a lawyer preparing arguments to defeat an opponent's case. Without such a facility, a legal reasoning system provides little support for the jurist's argumentation and justification processes, though it may be a useful tool in identifying the rule that most impacts the case.

A second limitation of the current system is that it requires that the user do the really “hard work.” The most difficult task in legal reasoning is determining what facts are important to a case (Burton, 1985). Here we assume that the facts are given; a more useful system would prompt the user to elicit the facts, perhaps providing tentative conclusions as the facts are gathered. For example, the fact-gathering process might begin by soliciting values from the user to instantiate the predicates of a general rule, either rejecting the rule and moving to a different line of reasoning if a predicate in the general rule cannot be satisfied, or accepting the rule and proceeding to a more detailed rule (i.e., an exception) if all the predicates are satisfied. Supporting this “determination” process would require that the heuristics used by legal experts be implemented as procedures in the system.

Other limitations, though present in our prototype, are inherent in legal reasoning itself. For example, defeasible reasoning can only indirectly address the vagueness of many legal rules. To derive sound conclusions from facts and rules, the system must be able to determine that some set of facts is or is not covered by a particular legal rule. H.L.A. Hart used the term “open texture” to describe this feature of legal rules and illustrated its effect on legal reasoning with his “vehicles in the park” scenario:

A legal rule forbids you to take a vehicle into the public park. Plainly this forbids an automobile, but what about bicycles, roller skates, toy automobiles? What about airplanes? Are these, as we say, to be called “vehicles” for the purpose of the rule or not? ... The toy automobile cannot speak up and say, “I am a vehicle for the purpose of this legal rule,” nor can the roller skates chorus, “We are not a vehicle.” Fact situations do not await us neatly labeled, creased, and folded, nor is their legal classification written on them to be simply read off by the judge. Instead, in applying legal rules, someone must take the responsibility of deciding that words do or do not cover some case in hand [Hart 1958, p. 607].

Giving a reasonably certain answer to questions regarding the applicability of a general rule to a specific case is difficult. Equally difficult is determining the meaning of legal conditions, such as the debtor's "having rights in" the collateral, for which no definition – no matter how vague or ambiguous – has been stipulated. Although closing open texture is a major challenge, meeting this challenge is a requirement of a useful and reasonably sound legal reasoning system.

Finally, defeasible reasoning, being a form of deductive reasoning, addresses only a restricted segment of the legal reasoning spectrum. We have assumed that the knowledge base consists only of rules, i.e., that both statutes and the decisions of precedent-setting cases have been transformed into computable rules. In practice, lawyers and judges frequently examine the specifics of a precedent case, comparing its parties, acts, and context to those of the case at hand in order to argue that the similarities (differences) justify a similar (different) decision in the current case. Thus, a fully implemented legal reasoning system should support not only deductive but also analogical reasoning and should provide a framework for representing the details of a case (see, e.g., Ashley, 1989; Branting, 1989 for a discussion of reasoning about precedents).

## Acknowledgement

This research was supported in part by the National Science Foundation, under grant IRI-8715297. The authors wish to thank the editor and the anonymous reviewers for their insightful comments and suggestions on an earlier version of this article.

## References

Ashley, K.D., Toward a Computational Theory of Arguing with Precedents, Proceedings of the Second International Conference on Artificial Intelligence and Law, ACM Press, 1989.

Belzer, M., Legal Reasoning in 3-D, Proceedings of the First International Conference on Artificial Intelligence and Law, ACM Press, 1987.

Belzer, M., Reasoning with Defeasible Principles, 66 Synthese (1986), 1–24.

Belzer, M. and Loewer, B., A Conditional Logic for Defeasible Beliefs, 4 Decision Support Systems (1988), 129–142.

Branting, L.K., Representing and Reusing Explanations of Legal Precedents, Proceedings of the Second International Conference on Artificial Intelligence and Law, ACM Press, 1989.

Burton, S.J., An Introduction to Law and Legal Reasoning, Little, Brown and Company, 1985.

Calamari, J.D., and Perillo, J.M., Contracts, (3rd ed.). St. Paul: West Publishing, 1987.

Causey, R.L., EVID: A System for Interactive Defeasible Reasoning, In this issue.

Clark, K.L., Negation as Failure, In H. Gallaire and J. Minker (Eds.), Logic and Data Bases, New York: Plenum Press, 1978.

Countryman, V., Kaufman, A., and Wiseman, Z., Commercial Law: Cases and Materials, 3rd Edition, forthcoming.

Covington, M., Nute, D., and Vellino, A., Prolog Programming in Depth, Scott Foresman, 1988.

Cueto-Rua, J.C., Judicial Methods of Interpretation of the Law, The Publications Institute, Paul M. Hebert Law Center, Louisiana State University, 1981.

Dworkin, R.M., Is Law a System of Rules?, In The Philosophy of Law, London: Oxford University Press, 1977.

Gardner, A. von der Lieth., An Artificial Intelligence Approach to Legal Reasoning, Cambridge, MA: MIT Press, 1987.

Gardner, A. von der Lieth., Overview of an Artificial Intelligence Approach to Legal Reasoning, In C. Walter (Ed.), Computer Power and Legal Reasoning, St. Paul: West Publishing, 1985.

Genesereth, M.R. and Nilsson, N.J. Logical Foundations of AI, Morgan Kaufman, 1987, Chapter 6.

Gordon, T.F., Object-Oriented Predicate Logic and Its Role in Representing Legal Knowledge, In C. Walter (Ed.), Computing Power and Legal Reasoning, St. Paul: West Publishing, 1985.

Gordon, T.F., Oblog-2: A Hybrid Knowledge Representation System for Defeasible Reasoning, Proceedings of the First International Conference on Artificial Intelligence and Law, ACM Press, 1987.

Hanks, S. and McDermott, D., Nonmonotonic Logic and Termporal Projection, 33 Artificial Intelligence (1987), 379–412.

Hart, H.L.A., The Concept of Law, London: Oxford University Press, 1961.

Hart, H.L.A., Positivism and the Separation of Law and Morals, 71 Harvard Law Review (1958), 593–629.

Hustler, A., Programming Law in Logic, University of Waterloo Department of Computer Science, Research Report CS-82-13, 1982.

Kimbrough, S.O. and Adams, F., Why Nonmonotonic Logic?, 4 Decision Support Systems (1988), 111–127.

Kimbrough, S.O. and Hua Hua., On Modeling Nonmonotonic Reasoning with the Method of Sweeping Presumptions, forthcoming in Minds and Machines, November 1991.

Lee, R.M., Coelho, H., and Cotta, J.C., Temporal Inferencing on Administrative Databases, 10 Information Systems (1985), 197–206.

Leith, P., Clear Rules and Legal Expert Systems, In A.A. Martino and R. Socci Natali (Eds.), Automated Analysis of Legal Texts, Elsevier Science Publishers, 1986a, 661–679.

Leith, P., Legal Expert Systems: Misunderstanding the Legal Process, 49 Computers and Law (1986b), 26–31.

Leith, P., Logic, Formal Models and Legal Reasoning, 24 Jurimetrics Journal (1984), 334–356.

Lucash, R.M., Legal Liability for Malfunction and Misuse of Expert Systems, 18 SIGCHI Bulletin, July 1986, 35–43.

MacCormick, D.N., Law as Institutional Fact, 90 The Law Quarterly Review (1974), 102–129.

McDermott, D. and Doyle, J., Non-monotonic Logic I, 13 Artificial Intelligence (1980), 41–72.

Nute, D., Defeasible Reasoning and Decision Support Systems, 4 Decision Support Systems (1988), 97–110.

Nute, D., Defeasible Reasoning and Temporal Projection, In Proceedings of the 22nd Hawaii International Conference on Systems Science, 1989a.

Nute, D., General and Special Defeasible Logic, In Proceedings of the Tubingen Workshop on Semantic Nets and Non-monotonic Reasoning, 1989b.

Nute, D., A Non-monotonic Logic Based on Conditional Logic, Advanced Computational Methods Center Research Report 01-007, University of Georgia, 1985.

Nute, D., Billington, D., and De Coster, K., Inheritance Nets Are Specialized Defeasible Theories, In Proceedings of the Tubingen Workshop on Semantic Nets and Non-monotonic Reasoning, 1989.

Nute, D. and Lewis, M., d-Prolog: A User's Manual, ACMC Research Report 01-0017, Advanced Computational Methods Center, Univ. of Georgia, 1985.

Polley, M.S., Computer-Assisted Legal Analysis: Minimizing the Risks for the Consumer, American Bar Association Center for Professional Responsibility, 1985.

Reed, C., Expert Systems and Legal Expertise, 5 Computer Law and Practice (1989), 122–125.

Reiter, R., A Logic for Default Reasoning, 13 Artificial Intelligence (1980), 81–132.

Reiter, R., On Closed World Data Bases, in Logic and Data Bases, H. Gallaire and J. Minker (Eds.), Plenum Press, New York, 1978.

Rissland, E.L., Artificial Intelligence and Legal Reasoning: A Discussion of the Field and Gardner's Book, AI Magazine (Fall 1988), 45–55.

Sergot, M.J., Sadri, R., Kowalski, R.A., Kriwaczek, F., Hammond, P. and Cory, H.T., The British Nationality Act as a Logic Program, 29 Communications of the ACM (May 1986), 370–386.

Sherman, D.M., A Prolog Model of the Income Tax Act of Canada, Proceedings of the First International Conference on Artificial Intelligence and Law, ACM Press, 1987.

Sprowl, J.A., Automating the Legal Reasoning Process: A Computer That Uses Regulations and Statutes to Draft Legal Documents, 1 American Bar Foundation Research Journal (1979).

Stamper, R., The Dangers of AI in Information Systems as Exposed by the Field of Computers and Law, 3 Journal of Information Technology (1988), 6–8.

Stamper, R., LEGOL: Modelling Legal Rules by Computer, In B. Niblett (Ed.), Advanced Workshop on Computer Science and Law, Cambridge University Press, 1980.

Susskind, R.E., Expert Systems in Law, Proceedings of the First International Conference on Artificial Intelligence and Law, ACM Press, 1987.

Susskind, R.E., Expert Systems in Law: A Jurisprudential Approach to Artificial Intelligence and Legal Reasoning, 49 The Modern Law Review (1986), 168–194.

Susskind, R.E., Expert Systems in Law: A Jurisprudential Inquiry, Oxford: Clarendon Press, 1987.

Twining, W. and Miers, D., How To Do Things with Rules (2nd ed.), London: Weidenfeld and Nicolson, 1982.

Waterman, D.A., Paul, J., and Peterson, M., Expert Systems for Legal Decision Making, 3 Expert Systems (October 1986), 212–226.

## Appendix 1: Listing of rules

/\* PRIORITY RULES \*/

IF attached\_security\_interest(Creditor1, Debtor, Collateral, ADate1)
AND attached\_security\_interest(Creditor2, Debtor, Collateral, ADate2)
AND perfected\_interest(Creditor1, Debtor, Collateral, Date1),
AND NEG perfected\_interest(Creditor2, Debtor, Collateral, Date2)
AND NEG real\_estate\_interest(Creditor1, Real\_property)
AND NEG real\_estate\_interest(Creditor2, Real\_property)
PRESUMABLY priority(Creditor1, Creditor2, Debtor, Collateral, '9-312(5)/9-301(1a)').

IF perfected\_interest(Creditor1, Debtor, Collateral, Date1)
AND perfected\_interest(Creditor2, Debtor, Collateral, Date2)
AND NEG real\_estate\_interest(Creditor1, Real\_property)
AND NEG real\_estate\_interest(Creditor2, Real\_property)
AND Date1 . <. Date2
PRESUMABLY priority(Creditor1, Creditor2, Debtor, Collateral, '9-312(5a)').

IF NEG perfected\_interest(Creditor1, Debtor, Collateral, PDate1)
AND NEG perfected\_interest(Creditor2, Debtor, Collateral, PDate2)
AND attached\_security\_interest(Creditor1, Debtor, Collateral, Date1)
AND attached\_security\_interest(Creditor2, Debtor, Collateral, Date2)
AND NEG real\_estate\_interest(Creditor1, Real\_property)
AND NEG real\_estate\_interest(Creditor2, Real\_property)
AND Date1. <.Date 2
PRESUMABLY priority(Creditor1, Creditor2, Debtor, Collateral, '9-312(5b)').

IF inventory(Collateral, Creditor, Debtor)
AND perfected\_interest(Creditor1, Debtor, Collateral, Date1)
AND perfected\_interest(Creditor2, Debtor, Collateral, Date2)
AND Date1 . < . Date2
AND pmsi(Creditor2, Debtor, Collateral)
AND received possession(Debtor, Collateral, RPDate)
AND Date2 . < . RPDate
AND gave notice in writing(Creditor2, Creditor1, NDate)
AND NDate . < . Date2
AND received notice(Creditor1, RNDate)
AND RNDate . < = . RPDate + 5 years
PRESUMABLY priority(Creditor2, Creditor1, Debtor, Collateral, '9-312(3)').

IF NEG inventory(Collateral, Creditor, Debtor)
AND perfected \_ interest(Creditor1, Debtor, Collateral, Date1)
AND perfected \_ interest(Creditor2, Debtor, Collateral, Date2)
AND Date1 . < . Date2

AND pmsi(Creditor2, Debtor, Collateral)
AND received possession(Debtor, Collateral, RPDate)
AND Date1 . <= . RPDate . + . 10 days
PRESUMABLY priority(Creditor2, Creditor1, Debtor, Collateral, '9-312(4)').

IF fixture\_in(Collateral, Real\_property)
AND real\_estate\_interest(Creditor2, Real\_property)
AND owner(Owner, Real\_property)
AND attached\_security\_interest(Creditor1, Debtor, Collateral, \_)
AND attached\_interest(Creditor2, Owner, Real\_property, \_)
PRESUMABLY priority(Creditor2, Creditor1, Debtor, Collateral, '9-313(7)').

IF fixture\_in(Collateral, Real\_property)
AND real\_estate\_interest(Creditor2, Real\_property)
AND owner(Owner, Real\_property)
AND attached\_security\_interest(Creditor1, Debtor, Collateral, \_)
AND attached\_interest(Creditor2, Owner, Real\_property, Attach\_Date)
AND became\_fixture(Collateral, Install\_Date)
AND pmsi(Creditor1, Debtor, Collateral)
AND Attach\_Date. <.Install\_Date
AND filed\_financing\_statement(Creditor1, Debtor, Collateral,
real\_estate\_recorder, FDate)
AND FDate. <= . Install\_Date . + . 10 days
AND has\_interest\_in(Debtor, Real\_property)
PRESUMABLY priority(Creditor1, Creditor2, Debtor, Collateral, '9-313(4a')).

/\* DEFEATER \*/

IF fraud(A)
MAYBE NEG priority(A,\_,\_,\_,\_).

/\* CONTRARY STATEMENT \*/

incompatible(priority(C1, C2, D, C, \_), priority(C2, C1, D, C, \_)).

/\* OTHER RULES \*/

PRESUMPTION neg real\_estate\_interest(\_, \_).
PRESUMPTION neg perfected\_interest(\_, \_, \_, \_).
PRESUMPTION neg has\_perfected\_interest(\_, \_, \_, \_, \_).
PRESUMPTION neg has\_rights\_in(\_, \_, \_).
PRESUMPTION neg attached\_security\_interest(\_, \_, \_, \_).

IF signed\_security\_agreement(Debtor, Creditor, Collateral, Date)
AND gave\_value(Creditor, Debtor)
AND has\_rights\_in(Debtor, Collateral, RDate)
AND RDate. <= . Date
THEN attached\_security\_interest(Creditor, Debtor, Collateral, Date).

IF after\_acquired\_property(Collateral, Creditor, Debtor)
AND signed\_security\_agreement(Debtor, Creditor, Collateral, Date)
AND gave\_value(Creditor, Debtor)
AND has\_rights\_in(Debtor, Collateral, Date1)
AND Date .<. Date1
THEN attached\_security\_interest(Creditor, Debtor, Collateral, Date).

IF has\_perfected\_interest(Creditor, Debtor, Collateral, Date, Rule)
THEN perfected\_interest(Creditor, Debtor, Collateral, Date).

IF personal\_property(Collateral, Creditor, Debtor)
AND filed\_financing\_statement(Creditor, Debtor, Collateral, sec\_of\_state, Date1)
AND attached\_security\_interest(Creditor, Debtor, Collateral, Date2)
AND Date2 <= .Date1
THEN has\_perfected\_interest(Creditor, Debtor, Collateral, Date1, '9-303.1').

IF after \_ acquired \_ property(Collateral, Creditor, Debtor)
AND personal \_ property(Collateral, Creditor, Debtor)
AND filed \_ financing \_ statement(Creditor, Debtor, Collateral, sec \_ of \_ state, Date1)
AND attached \_ security \_ interest(Creditor, Debtor, Collateral, Date2)
AND Date2 . < . Date1

THEN has \_ perfected \_ interest(Creditor, Debtor, Collateral, Date1, '9-303.2').

IF personal\_property(Collateral, Creditor, Debtor)
AND filed\_financing\_statement(Creditor, Debtor, Collateral, sec\_of\_state, Date1)
AND attached\_security\_interest(Creditor, Debtor, Collateral, Date2)
AND Date2.<.Date1
THEN has\_perfected\_interest(Creditor, Debtor, Collateral, Date1, '9-303.3').

IF consumer\_good(Collateral, Creditor, Debtor)
AND attached\_security\_interest(Creditor, Debtor, Collateral, Date)
AND pmsi(Creditor, Debtor, Collateral)
THEN has\_effected\_interest(Creditor, Debtor, Collateral, Date, '9-302(1d)').

IF fixture\_in(Collateral, Real\_property)
AND attached\_security\_interest(Creditor, Debtor, Collateral, Date1)
AND filed\_financing\_statement(Creditor, Debtor, Collateral, real\_estate\_recorder, Date)
THEN has\_perfected\_interest(Creditor, Debtor, Collateral, Date, '9-313(1b)').

## /\* FACTS \*/

FACT consumer\_good(oven, 'Anderson Appliances', 'Miss Julia').  
FACT fixture\_in(oven, 'Town Lake Apts').  
FACT became\_fixture(oven, 1/10/89).  
FACT signed\_security\_agreement('Miss Julia', 'Anderson Appliances', oven, 1/2/89).  
FACT gave\_value('Anderson Appliances', 'Miss Julia').  
PRESUMPTION has\_rights\_in('Miss Julia', oven, 1/2/89).  
FACT filed\_financing\_statement('Anderson Appliances', 'Miss Julia', oven, real\_estate\_recorder, 1/13/89).

FACT attached\_interest('Friendly Finance', landlord, 'Town Lake Apts', 1/1/89).
FACT pmsi('Anderson Appliances', 'Miss Julia', oven).
FACT owner(landlord, 'Town Lake Apts').
PRESUMPTION has\_interest\_in('Miss Julia', 'Town Lake Apts').
FACT real\_estate\_interest('Friendly Finance', 'Town Lake Apts').

/\* The following are facts added to the above data set in subsequent queries \*/
/\*
PRESUMPTION fraud('Friendly Finance').

PRESUMPTION readily\_removable(oven, 'Town Lake Apts'). FACT replacement(oven). PRESUMPTION domestic\_appliance(oven).

FACT signed\_security\_agreement('Miss Julia', 'City Bank', oven, 10/21/89).
FACT gave\_value('City Bank', 'Miss Julia').
FACT filed\_financing\_statement('City Bank', 'Miss Julia', oven, real\_estate\_recorder, 10/23/89).
\*/
