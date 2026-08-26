---
otero_id: 9880
otero_key: "245CZVP9"
title: "Philosophy of science underpinnings of prototype validation: Popper vs. Quine"
authors: "wendy"
year: "2007"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.2006.00239.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Philosophy of science underpinnings of prototype validation: Popper vs. Quine

Esther E Klein\* & Paul J Herskovitz<sup>†</sup>

\*Department of Business Computer Information Systems/Quantitative Methods, Zarb School of Business, Hofstra University, 211 Weller Hall, Hempstead, NY 11549, USA, email: eklein9@aol.com, and <sup>†</sup>Department of Business (Law), College of Staten Island, City University of New York, 2800 Victory Boulevard, Room #3 N-206, Staten Island, NY 10314, USA, email: pjhersko@aol.com, herskovitz@mail.csi.cuny.edu

Abstract. In this paper, we aim to provide prototype validation in both custom and packaged software development with a theoretical framework located within the philosophy of science. Towards that end, we consider Popperian and Quinean accounts of scientific knowledge and argue that the theoretical underpinning of prototype validation is Quine’s holistic philosophy of science, whose cornerstone principle is that all beliefs are revisable. Specifically, our thesis is that the systems developer and software consumer (user or customer) join forces – not as Popperian falsifiers, who make a decision rule to reject the prototype on account of any divergence, major or minor, from the software consumer’s mental model, but – as Quinean revisers, with the objective of fine-tuning the prototype (or the software consumer’s mental model) so that the prototype and the software consumer’s mental model are congruent with each other. This paper suggests that prototype revisions are belief revisions, and, as such, should be guided – and are guided – by pragmatic norms, such as conservatism, simplicity and generality, and are influenced by social, or sociological, factors as well. Finally, we discuss the relevance, value and pragmatic implications of a Quinean philosophy of science framework for research and practice.

Keywords: software development, epistemology, falsificationism, holism, philosophy of science, prototype validation

## INTRODUCTION

The past decade, bracketed by the waning years of the second millennium and the opening years of the third, has been witness to a growing, robust and richly textured literature on the philosophical foundations and dimensions of information systems (IS) in general and information systems development (ISD) in particular (e.g. see Hirschheim et al., 1995; Winder et al.,

1997; Klein, 2004; Monod, 2004; Taylor, 2005). The aim of this paper is to contribute to these efforts by providing prototype validation in both custom and packaged software development with a theoretical framework located within the philosophy of science.

In contrast to computer science (CS) and software engineering (SE), which are predominantly technical disciplines, IS ‘in essence is an applied social science pertaining to the use and impact of technology’ (Elliot & Avison, 2004, p. 5). IS, then, can be viewed as ‘social systems that are technically implemented’ (Hirschheim et al., 1995, p. 1). As philosophy of science perspectives have historically enriched the various sciences, including IS (e.g. see Floridi, 2002), by ‘illuminating the character of the scientific enterprise’ (Nagel, 1960, p. 13) and reflecting upon the scientific method involved in a particular discipline’s activities (Kemeny, 1959), it is a goal of this paper to shed light on prototype validation research and practice through the prism of philosophy of science.

Prototyping is a flexible ‘[ISD] methodology based on building and using a model of a system for designing, implementing, testing, and installing the system’ (Lantz, 1987, p. 1). Under such an approach, ‘[information] systems are developed through an iterative rather than a systematic process’, whereby ‘[systems] developers and [software consumers] are . . . interacting, revising, and testing the prototype system until it evolves into an acceptable application’ (Oz, 2004, p. 599).

The term ‘user(s)’, as employed in this paper, refers to the end user(s) of custom software and encompass situations where the end user is an individual or a team. The term ‘customer(s) refers to the consumer(s) of packaged software. The term ‘software consumer’ subsumes both end user(s) of custom software and customer(s) of packaged software. In using the above terminology, we have adapted the nomenclature suggested by Keil & Carmel (1995, p. 34).

For Naumann & Jenkins (1982, p. 37), the activity of prototyping typically involves prototype revision: ‘The prototype builder constructs successive versions of the system, compromising and resolving conflicts between the context (i.e. user [or customer] needs and desires) and the form as constrained by technology and economics.’ Accordingly, a prototype is built with the expectation that it will be tested against the user’s or customer’s mental model, and if necessary – which is usually the case – revised.

Prototyping and thus prototype validation take place in two domains or contexts: custom software development and packaged software development. Custom software, also known as customer-specific, made-to-order and bespoke software, is built for particular users by ‘an organization’s internal IS staff or by direct subcontract to a software house’ (Sawyer, 2000, p. 47). By contrast, packaged software, also referred to as commercial off-the-shelf (COTS), shrink-wrapped, market-driven and commercial software, is developed for a mass or niche market by a vendor (Murphy & Seddon, 2003) and is generally ‘licensed for use, not sold’ (Sawyer, 2000, p. 47). Murphy & Seddon (2003, p. 1) have observed that, although ‘organizations are increasingly using packaged [rather than custom] software to satisfy their software needs’, it is only relatively recently that packaged software has been subjected to increasing scholarly treatment.

Packaged software development ‘differs from custom software development . . . most fundamental[ly] [in] the role of . . . user or customer involvement’ (Mäntyniemi et al., 2004, p. 37).

Specifically, such ‘[software consumer] involvement, a central belief of custom IS development, is not common in packaged software development’ (Sawyer, 2000, p. 47). In light of ‘the literature suggest[ing] that user involvement has positive effects, especially on user satisfaction . . . [and as] an effective means of requirements capture’ (Kujala, 2003, p. 1), there have been efforts in packaged software development for customer feedback, input and participation (see Mäntyniemi et al., 2004, pp. 50–51).

Prototype validation in both custom and packaged software development centres on ascertaining whether the prototype matches the consumer’s mental model. By custom software development, the prototype is presented to the user, who makes the determination whether the prototype conforms to the user’s mental model. In packaged software development, prototype validation often includes alpha (internal) and beta (external) testing, a two-pronged process comparing the prototype to the customer’s mental model. Specifically, alpha testing occurs within the specialized software vendor company usually by an independent team, that is, a team other than the project team that developed the software. If the prototype is determined to be consistent with the software customer’s mental model as understood by the vendor’s project team, then the prototype goes through beta testing, in which a number of select customers assess whether the prototype conforms to the select customer’s mental model (e.g. see Mäntyniemi et al., 2004, pp. 37–52).

As is true with many disciplines that have a pragmatic component, theory in IS has not kept pace with practice. An aim of this paper is to redress this imbalance with respect to prototype validation. Specifically, in our quest to provide a theory for prototype validation, we will consider two seminal and well-developed philosophies of science as theoretical frameworks – Popper’s falsificationism and Quine’s holism – and we will argue that it is Quinean holism that is the appropriate theory for prototype validation. In the course of our argument, we will contrast Quinean holism to Popperian falsificationism because the latter is held to be by many researchers to be the gold standard of scientific methodology and theory evaluation. Moreover, a Popperian perspective serves as a powerful foil to the Quinean approach, whose terrain is best explored in stark juxtaposition to that of Popper. Indeed, an appreciation of Popper’s thought is helpful in understanding Quinean philosophy because, as will be discussed below, Quine has agreed with Popper’s scepticism towards verifications but, unlike Popper, Quine has extended this doubting stance to falsifications as well.

According to Okasha (2002, p. 12), ‘[t]he principal task of philosophy of science is to analyse the methods of enquiry used in the various sciences.’ As prototype validation involves an evidentiary assessment whether the prototype conforms to the user’s or customer’s mental model, the focus of this paper is the epistemology of science, the branch of philosophy of science that deals with issues pertaining to how claims to scientific knowledge are justified and what constitutes evidential support for scientific statements, hypotheses and theories.

Although currently not dominant schools of thought, the philosophies of science of Popper and Quine have been exceptionally influential – Popper among scientists (Boyd, 1991, p. 11) and social scientists (Skinner, 1985, p. 5) and Quine among philosophers (Hookway, 1988, p. 1) – and, we suggest, may be useful in understanding discrete scientific activities within a larger discipline. According to Webb (1995, p. 87), in the social sciences, ‘we use theories to highlight aspects of reality that are deemed important with respect to a particular phenomenon.’ In that spirit, recently, Klein & Herskovitz (2005) have analysed Popperian falsificationism, Quinean holism and early Putnamean scientific realism with respect to computer simulation validation, and have concluded that a Popperian perspective is the appropriate stance there. Similarly, here, we will consider Popperian falsificationism and Quinean holism not as overarching or grand theories for IS but merely as frameworks limited to exploring one aspect of IS: prototype validation. Such an approach is consistent with the view that although IS is ‘a field in its own right . . . a common overarching theory does not [and need not] exist’ (Larsen & Levine, 2005, p. 362).

Prototype validation consists of a comparison of the prototype with the software consumer’s (i.e. the user’s or customer’s) mental model and the determination whether the former is an accurate representation of the latter (e.g. see Dussart et al., 2004). By building a prototype, the systems developer (prototype builder) is proposing a mini-theory of the software consumer’s mental model. If it is found that the prototype does not correspond in some way to the software consumer’s mental model and thus cannot be validated, the prototype need not be rejected outright. Instead, either the prototype or the software consumer’s mental model will need to be revised, or adjusted. Accordingly, we argue that the activity of prototype validation does not adhere to Popper’s falsificationist philosophy of science but rather follows a Quinean approach to belief revision, which is a central plank of Quine’s philosophy of science.

## POPPER’S PHILOSOPHY OF SCIENCE

The two core ideas in Popper’s philosophy of science are falsifiability, or refutability, as the touchstone of science and the rejection of induction as the method of science (Popper, 1959; 1965). In Popper’s account of science, scientists put forth bold conjectures for trial and then systematically attempt to falsify these conjectures. Those conjectures that are not falsified are retained ‘for the time being’ (Popper, 1959, p. 104). According to Popper’s falsifiability criterion, for a proposition – statement, hypothesis or theory – to qualify as scientific, it must put itself at risk by specifying certain predictions and forbidding certain observations. Thus, each scientific proposition must state under what conditions it will be deemed as having been disconfirmed. On a Popperian view although a scientific proposition can be conclusively refuted upon the occurrence of a single, isolated counterinstance, such proposition can never be established as true or even probable, irrespective of the number of confirming instances. For Popper, even well-tested theories are merely provisionally true, always subject to being rejected upon an experimental result or observation contrary to its predictions.

Popper’s approach is contrary to the traditional induction-based verificationist view of science espoused by the logical, or empirical, positivists, that a theory can be proven true, or at least probable, by cumulative observations consistent with the theory’s predictions (see Carnap, 1966, p. 20). Thus, for verificationists, the method of science is induction, a mode of reasoning that proceeds from specific observations to general theories. According to the verificationist position, for a statement to be meaningful, it must be empirically verifiable in principle, that is, it must be possible to describe the type of test or ‘the sort of observation . . . which would confirm or disconfirm [the statement]’ (Edwards & Pap, 1965, p. 677). For the verificationists, then, what distinguishes scientific assertions from non-scientific (metaphysical or pseudoscientific) ones is this verifiability criterion of meaningfulness.

## The problem of induction

Popper has attacked verificationism’s use of induction, whereby knowledge develops by generalizations derived from observations. According to Popper, employing induction to establish the truth of a theory is not rationally justified because of the logical difficulty eponymously known as ‘Hume’s problem of induction’ after its discoverer the philosopher David Hume, ‘who argued that from the strict logical point of view we have no justification in generalizing from instances we have experience of to those of which we have no experience’ (O’Hear, 1989, p. 27). Gillott & Kumar (1997) have offered this succinct illustration of the problem of induction:

How can we say all swans are white just because we have not seen any black ones? It could be the case that the next swan seen is black. No amount of observing white swans allows any inferences to be made about the probability of the next swan being white. (Gillott & Kumar, 1997, p. 16)

Popper’s solution to the problem of induction is that induction does not exist because it is impossible to have observations that have not been influenced, or tainted, by theory. Observations – the ‘bedrock’ of the traditional empiricist approach of verificationism (Laudan, 1990, p. 35) – are never theory-free, but rather are embedded within ‘a frame of expectations’ or ‘a frame of theories’ (Popper, 1965, p. 47). Thus, theories, or conceptual pigeonholes, necessarily precede and colour observations so that all observations and observation reports are ‘interpretations in light of theories’ (p. 38, note 3). Knowledge develops not by inductive inferences but by a process of trial and error, of learning from our mistakes.

## The problem of demarcation

Popper has put forward the falsifiability criterion as not only the solution to the problem of induction but also the solution to the problem of demarcation: ‘[H]ow can you distinguish the theories of the empirical sciences from pseudo-scientific or nonscientific or metaphysical speculations?’ (Popper, 1983, p. 159). Under a verificationist view, a scientific theory is demarcated, or distinguished, from a non-scientific speculation by the former’s use of induction. For Popper, however, it is the falsifiability of a theory or other assertion that confers scientific status: ‘A theory which is not refutable by any conceivable event is non-scientific. Irrefutability is not a virtue of a theory (as people often think) but a vice’ (Popper, 1957, p. 159).

Popper (1957, p. 160) has recognized that, consistent with Duhem’s and Quine’s holistic insights (see below), ‘[s]ome genuinely testable [falsifiable] theories, when found to be false, are still upheld by their admirers’ by the introduction of auxiliary hypotheses, or background assumptions, that save the theories from refutation. According to Popper, ‘[s]uch a procedure is always possible, but it rescues the theory from refutation only at the price of destroying or at least lowering its scientific status’ (Popper, 1957, p. 160) and thus should be generally avoided (Popper, 1959, pp. 82–83). For Popper, the scientists must adopt a decision rule to conclusively reject theories that have been falsified without resort to post-experiment or postobservation auxiliary hypotheses (Popper, 1959, p. 37).

## Criticisms of Popper’s philosophy of science

The strand that unites most of the criticism of Popper’s philosophy of science is that it does not conform to reality and ‘that it is virtually impossible to put into practice’ (Sayer, 1984, p. 205). In the real world, a theory is usually not abandoned because of a sole experimental result or observation contrary to the theory that is being tested (Lewthwaite, 2003). The typical scenario is that the scientist saves the theory from refutation by attributing the recalcitrant finding to a faulty implicit auxiliary hypothesis (e.g. the instrumentation is in good working order), a belief that now has to be revised. Such rescue of a theory under investigation is the central insight of Quine’s holist, or Duhem-Quine, thesis (see below), which renders conclusive falsifications beyond the bounds of the feasible and thereby poses a significant challenge to Popper’s philosophy of science. Moreover, a literal interpretation of Popper’s falsificationist criterion will mandate the abandonment of a theory upon a single counterinstance, all but prohibiting the human sciences – which involve probabilistic, and not deterministic, relationships (see Straub et al., 2004, p. 4) – from retaining any theories and ultimately resulting in the disappearance of the human sciences as disciplines (see Webb, 1995, pp. 87–88).

Reduced to its essence, then, the core arguments of Popper’s critics are that scientists do not – and should not – go about their work with the aim of discrediting and rejecting the very theories that they have created. One such critic, Quine, has presented an alternative account of science wherein Popper’s sceptical falsifiers are replaced by even more sceptical revisers, who are ‘hoping to save [their theories] rather than refute [them]’ (Quine, 2000a, p. 6).

## QUINE’S PHILOSOPHY OF SCIENCE

For Quine, falsifications are on the same epistemological footing as verifications, and hence both are viewed as equally suspect and inconclusive. Quine has starkly distinguished his approach from that of Popper thus: ‘Karl Popper argued that experiment can only refute hypotheses, not prove them. I hold that experiment is fallible both ways’ (Quine, 2000b, p. 412). Accordingly, Quine has viewed both verifications and falsifications as tentative and defeasible, true only for the time being and subject to revision. This sceptical stance towards all evidence, confirming and disconfirming, derives from Quine’s holism, a non-foundationalist philosophy of science that views all knowledge as a seamless, interconnected ‘web of belief’ (Quine & Ullian, 1970) that, unlike Popper’s falsificationism, admits of no demarcation between science and non-science (Quine, 1951, p. 20). Thus, philosophy, logic, mathematics and the human, or social, sciences are all continuous with natural science (see Ben-Menahem, 2005, p. 248). At the core of holism is the notion that all beliefs – even the laws of logic and mathematics – are in principle revisable (universal revisability). ‘No statement [in a larger theoretical network] is immune to revision’ (Quine, 1951, p. 40).

For Quine, like for Popper, all observation is theory-laden, refracted through the lens of preconceived theoretical assumptions (see Quine, 2000a, p. 5). However, both Quine and Popper have agreed to provisionally accept observation statements, or reports, as correct as a matter of convention (Laudan, 1990, p. 44) because, despite the limitations of evidence perceived by our senses, ‘whatever evidence there is [italics in original] for science is [italics in original] sensory evidence’ (Quine, 1969, p. 75), with ‘observation, however, inconclusive, [being] the locus of evidence’ (Quine, 2000b, p. 412).

According to Quine, a theory is actually a complex whole, or ‘theory-bundle’, consisting of ‘a substantial bundle of interlocking [components]’ (Quine, 2000b, p. 412), including the theory or hypothesis under investigation and various auxiliary hypotheses, or background assumptions. Contrary to a Popperian perspective, under which even isolated, individual hypotheses of a larger theory are falsifiable piecemeal (see Vuillemin, 1986, p. 595; Simkin, 1993, p. 167), on a Quinean view, only an entire theory – the ‘theory-bundle’ – is subject to being tested, with the constituent individual hypotheses of that theory not being separately falsifiable (Quine, 1951).

## The holism thesis

Quine (1951) has brought renewed scholarly attention to the holism thesis that had been initially advanced by Duhem (1906), which suggested that the researcher confronting a contrary experimental result is not compelled to reject or alter the theory or hypothesis under investigation, but instead can change any of the auxiliary hypotheses and thereby rescue the theory or hypothesis under investigation.

Duhem’s standpoint was informed by his conventionalism, a position within philosophy of science that holds that a scientist’s choice of theory or hypothesis is not governed solely by empirical findings, but rather is determined by conventions that assist in the organization of observation and knowledge. Thus, ‘theories evolve by convention, on the basis of considerations like simplicity, not merely on the basis of their ability to withstand falsification’ (Rosenthal & Rosnow, 1991, p. 34).

Quine has extended Duhem’s thesis, which was solely concerned with physical theory, to all knowledge. Moreover, ‘[i]n taking logic and mathematics to be continuous with science, and therefore revisable when experience so mandates, Quine’s holism goes beyond Duhem’s’ (Ben-Menahem, 2005, p. 248). According to Quine (1975, pp. 314–315), then, ‘[i]n the face of recalcitrant observations, we are free to choose what statements [in a larger theoretical network or “theory-bundle”] to revise and what ones to hold fast.’ Thus, ‘[a] recalcitrant experience can . . . be accommodated by any of various alternative re-evaluations in various alternative quarters of the total [theoretical] system’ (Quine, 1951, p. 40). For Quine, these revisions – even revisions of the laws of logic – can be made on pragmatic grounds.

## The underdetermination thesis

This holism thesis advanced by Quine has given rise to his notion of the underdetermination of theories by evidence, referred to commonly as the underdetermination thesis, which holds that empirical evidence cannot support, or determine, the choice of one theory over another (Quine, 1975). Put another way, in principle, ‘[a]ny set of data can be fit by many different [mutually inconsistent] theories’ (Weinberg, 1998, p. 51), ‘[a]nd so, the argument concludes, we are never in a position to know that any of these theories is the truth’ (Papineau, 1996, p. 302). According to Hacking (1999, p. 73), Quine, in his underdetermination thesis, was making ‘a logical point’ that ‘[e]ven if all possible data were in, there would still “in principle” be infinitely many theories that were formally consistent with such data.’ Thus, for Quine, choice of theory, or revision of belief, is not made on purely logical or rational grounds.

Quine has explained that the underdetermination thesis follows from the holism thesis because ‘[i]f in the face of adverse observations we are free always to choose among various adequate modifications of our theory [holism thesis], then presumably all possible observations are insufficient to determine theory uniquely [underdetermination thesis]’ (Quine, 1975, p. 313). Both the holism and underdetermination theses represent a significant challenge to Popperian falsificationism because a theory’s ‘[predictive] failure falsifies only a block of theory as a whole, a conjunction of many statements. The failure shows that one or more of those statements are false, but it does not show which’ (Quine, 1969, p. 79). Hence, on a Quinean view, it is impossible to conclusively falsify a theory.

In positing ‘that there are in principle an indefinite number of theories that fit the observed facts more or less adequately’ (Ariew, 1984, p. 313), the underdetermination thesis allows scientists and researchers, when encountering a contrary empirical result, to choose one of three alternative strategies, or ‘theory-bundle’ configurations, in order to restore consistency: (a) abandonment of the theory or hypothesis under investigation and retention of the auxiliary hypotheses; (b) retention of the theory or hypothesis under investigation and revision of any one or more of the auxiliary hypotheses, thereby rescuing the theory or hypothesis under investigation (‘auxiliary fudging’, Lipton, 1991, p. 142); or (c) revision (adjustment or tinkering) of the theory or hypothesis under investigation and retention of the auxiliary hypotheses (‘theory fudging’, Lipton, 1991, p. 142).

How should a scientist or researcher choose among the three alternative strategies or ‘theory-bundle’ configurations? According to Quine, pragmatic norms, such as conservatism, simplicity and generality (see below), should offer – and do offer – guidance but are not determinative. However, it is but a short distance from Quine’s relativist view, derived from the underdetermination thesis, that belief revision, or theory choice, is not strictly governed by logic or reason to the social constructivist position that social factors account for the ‘theory-bundle that is selected (see Laudan, 1990, pp. 146–170). This position holds that ‘there are other [i.e. social] forces working on a scientist besides evidence and the rules of scientific method’, and that ‘[i]t is these other [social] causes which take up the slack left by the evidence in shaping scientists’ beliefs’ (p. 157). Thus, ‘the way we think about things . . . are not just consequences of the way the world is, but are conditioned by our immersion in a particular society’ (Weinberg,

2000, p. 8). Social constructivism ‘recognise[s] the socially situated character of all knowledge, and hence the need to interpret scientific theories always with regard to their sociocultural contexts and conditions of emergence’ (Norris, 2000, pp. 21–22).

## Belief revisions

For Quine, all theory formulation and hypothesis generation are instances of belief revision. As we are confronted by experiences contrary to our previous beliefs, we will make revisions somewhere in our ‘web of belief’ so as to make our beliefs and experiences consistent with each other. According to Quine (1951, pp. 39–40), although ‘there is much latitude of choice as to what statements [of beliefs] to re-evaluate’, these revisions should be guided by pragmatic norms.

These pragmatic norms are heuristics that assist the scientist in belief revision and hypothesis generation (Quine, 1951, p. 43; 1991, p. 269). Conservatism and simplicity are the chief pragmatic norms. Conservatism, also called by Quine as the ‘maxim of minimum mutilation’ (Quine, 1991, p. 268), refers to the principle of ‘retain[ing] those hypotheses that clash least with the rest of our body of beliefs’ (Orenstein, 1977, p. 83). According to Quine & Ullian (1970):

The less rejection of prior beliefs required, the more plausible the hypothesis – other things being equal. The plausibility of a hypothesis varies inversely with the plausibility of the prior beliefs that it disallows. (Quine & Ullian, 1970, p. 44)

The norm of simplicity, also known as Ockham’s razor, admonishes us not to multiply theoretical entities unnecessarily and to prefer simpler theories over complex ones. ‘When there are hypotheses to choose between, and their claims are equal except in respect of simplicity, we choose the one that looks simpler’ (Quine & Ullian, 1970, p. 45). Another norm to guide belief revision is generality, which advises us that our beliefs or hypotheses should be articulated with sufficient generality so that our initial experimental results will hold in subsequent test situations even though the latter do not correspond exactly to the first experimental run (p. 44).

## Criticisms of Quine’s philosophy of science

Quine’s work has been almost universally admired in philosophical circles, the consensus view being that ‘[t]he last half-century in philosophy certainly belonged to Quine’ (Blackburn, 2001, p. 37). Most criticisms of Quine’s philosophy of science have acknowledged the main contours of his holism and underdetermination theses while disagreeing with their importance, taking issue with their implications, or disputing some elements therein (e.g. see Popper, 1957; 1959; Glymour, 1980; Stove, 1999).

Quine’s holism thesis – the notion that scientific statements are not tested in isolation but only as parts of a larger theoretical network, so that a contrary finding can be accommodated by making revisions somewhere in the network – has proven to be a hardy insight that could be attacked only at its margins. For example, Stove (1999) has conceded the correctness of Quine’s holism thesis but has played down its significance:

[T]he [holism] thesis is simply the most trivial of contingent truths about human beings: that given any proposition whatever, a scientist (or anyone) can take it into his head to affirm it, and can then stick to it through thick and thin. (Stove, 1999, p. 57)

As explored earlier, Popper (1957; 1959) has assailed Quine’s holism thesis for allowing of post-experiment or post-observation revisions of auxiliary hypotheses (e.g. instrumentation in good working order) to explain away a contrary finding and thereby save from refutation the theory under investigation. Admitting the possibility of such a Quinean rescue strategy, Popper has questioned the strategy’s legitimacy and has condemned its use in general, asserting that such preservation of the theory comes at the cost of diminished scientific status.

Quine’s underdetermination thesis – the argument that in principle there are many equally plausible and mutually inconsistent theories to explain a given set of experimental or observational data – has been challenged in some philosophical quarters as technically correct for the most part but of limited practical consequence (e.g. see Lipton, 1991). Okasha (2002) has summarized the two central criticisms of the underdetermination thesis:

In principle, there will always be more than one possible explanation of a given set of observations. But . . . it does not follow that all of these possible explanations are as good as one another. . . . [Moreover,] there are relatively few real cases of underdetermination in the history of science. . . . Far from scientists being faced with a large number of alternative explanations of their observational data, they often have difficulty finding even one [italics in original] theory that fits the data adequately. (Okasha, 2002, p. 73)

The strengths and weaknesses of a Quinean stance make it the appropriate philosophy of science for some endeavours but not for others. Not all scientific activity conforms to a Quinean philosophy of science. For instance, Klein & Herskovitz (2005) have argued that a Quinean perspective is ill suited for computer simulation validation because, in accordance with Quine’s view that all falsifications as well as all verifications are ambiguous, a falsified model cannot be conclusively rejected. Hence, a Quinean philosophy of science discourages the improvement of computer simulation models as model developers will not know when to reject a model and make attempts to build a potentially better alternative. The adoption of a Quinean approach under such circumstances will lead to ‘epistemological nihilism’ (Quine, 1969, p. 88). Accordingly, with respect to computer simulation validation, Klein & Herskovitz (2005) have concluded that a Popperian philosophy of science, which provides model developers with a firm decision rule of conclusively rejecting a falsified model, is the appropriate stance as it would encourage the building of improved models.

## PROTOTYPE VALIDATION AS A QUINEAN UNDERTAKING

In line with the work of Herskovitz (1991) and Klein & Herskovitz (2005), which suggests that different philosophies of science may be appropriate for various discrete scientific endeavours, the thesis of this paper is that the activity of prototype validation in both custom and packaged software development should follow – and does follow – a Quinean script. Specifically, we argue that the systems developer and software consumer are collaborators in a Quinean enterprise in which the prototype is appraised (by the user in custom software development or by an independent team of the vendor and then the customer in packaged software development), as to whether it conforms to the software consumer’s initial mental model or, if circumstances have changed for the software consumer, to the software consumer’s revised mental model. The software consumer has three options: (a) accepting the prototype as completely conforming to the software consumer’s mental model; (b) requesting revisions in the prototype or revising the mental model so that they are in conformity with each other; and (c) rejecting the prototype as not conforming to the software consumer’s mental model.

Under a Quinean perspective, rejection of the prototype should be reserved for only the most egregious situations, for example, when there is a total mismatch between the prototype and the software consumer’s mental model, or when there has been a drastic change in the software consumer’s circumstances (see Lichtblau, 2005). In most circumstances, the software consumer will not reject the prototype outright and scuttle the entire system if the prototype does not conform to the software consumer’s mental model. Rather, the software consumer will request modifications or adjustments to fine-tune the prototype. There may be, and usually are, several iterations, or rounds, to the prototype validation process.

Under a Popperian perspective, if the prototype in any way does not conform to the software consumer’s mental model, the revision option is not available and the prototype is rejected. Such rejection belies the underlying assumption upon which prototyping is grounded: a prototype is constructed with the intention that it will be revised as the systems developer and software consumer interact with each other and obtain a better or more precise understanding of the software consumer’s requirements. The expectation is that fine-tuning will be needed to bring the prototype and the software consumer’s initial or revised mental model into conformity with each other. For example, Özcan (1998) has noted:

Our experience suggests that the existence of a software tool to automate a task often alters [software consumers’] perception of what the task involves. As a result, it is possible that even those requirements that are perceived to be well-understood may still need to be modified. (Özcan, 1998, p. 1373)

As revisions are at the very heart of prototyping, a Popperian falsificationist philosophy of science, which prohibits prototype revisions and mandates a rejection if the prototype and the software consumer’s mental model diverge in any way, is ill suited as a theoretical framework for prototype validation.

By contrast, the application of a Quinean philosophy of science to prototype validation allows the prototype to be revised, which, in fact, is the main advantage of the prototyping approach to ISD (see Dearnley & Mayhew, 1983). As the systems developer is expected to modify, tweak and tinker with the prototype until it conforms to the software consumer’s initial or revised mental model, it is a Quinean philosophy of science that provides a suitable theory for prototype validation.

Anderson et al. (1986, p. 236) have captured the significance of the revision option under a Quinean approach thus: ‘In the face of disconfirmation we are not given only one alternative, namely rejecting the theory [as embodied in the prototype].’ Rosenthal & Rosnow (1991, p. 35) have recognized that the essential distinction between the Popperian and Quinean philosophies of science is that the former holds that scientific theories that are empirically falsified must be unambiguously rejected and that only those that survive attempts at falsification should be retained, while the latter asserts that ‘there is no such thing as a completely decisive falsifying test because when a refutation occurs, it merely tells us that the general formulation needs to be adjusted [italics added], not that it needs to be discarded.’ Quine’s holistic philosophy of science, then, is a philosophy of revision, ‘an epistemology of reevaluation’ (Katz, 1998, p. 72). As such, it is well suited to serve as a theoretical framework for prototype validation.

## Pragmatic norms

According to a Quinean philosophy of science, as embodied in Quine’s naturalized epistemology, revisions to prototypes should be – and are – guided, or restrained, by pragmatic norms, such as conservatism, simplicity and generality (see above). Concerning the norm of conservatism, if the prototype is judged not conform to the software consumer’s mental model or if circumstances have changed between the construction of the software consumer’s mental model and the building of the prototype, the systems developer should make the least extreme changes to accommodate the software consumer’s mental model. The systems developer needs to modify the prototype in such a way so as to preserve as much of the original features as possible while satisfying the software consumer’s requirements. According to Dearnley & Mayhew (1983, p. 41), ‘[a] good prototype must be built on the basis of information already gathered, keeping in view the information required.’ Drastic revisions and major overhauls may result in the loss of software consumer confidence in the system and increased costs (see Dearnley & Mayhew, 1983).

Another aspect of the norm of conservatism is consistency with generally accepted IS design practices and standards. Revisions to the prototype should cohere with current custom and usage in the profession. Morcor (2005) has made this point thus:

[C]ertain features and buttons must be in a certain place on the screen so users feel at home. . . . We spent a lot of time talking to [software consumers] about the positioning of buttons. Closer to the top means a certain thing, over towards the right means another. There is a certain personality to the user interface that the [software consumers] get to know like a reliable friend. (Morcor, 2005; p. 9)

With respect to the norm of simplicity, both the systems developer and the software consumer should understand that the revisions should be as simple as possible to accomplish the task needed or the result requested. In fact, the software consumer should bear in mind the simplicity norm when constructing the mental model. Simplicity is a key concept in ISD in general and in prototyping in particular, and following its dictates confers significant benefits to the software consumer. For example, as articulated by Morcor (2005, p. 10), ‘Minimum mouse clicks, minimum keystrokes, minimum screens. The fewer things that have to be done, the more powerful the [software consumer] feels.’ Similarly, Berkun (1999) has remarked:

[F]eatures improve a product only if they are actually used by the [software consumer]. . . . Each feature gets an icon or a link on a Web site or toolbar, and is yet another item that the [software consumer] needs to wade through before they can find the one that they need. (Berkun, 1999, p. 1)

Writing in the context of Web design, Nielsen (2000) has observed:

A general principle for all user interface design is to go through all of your design elements and remove them one at a time. If the design works as well without a certain design element, kill it. Simplicity always wins over complexity, especially on the Web where every five bytes saves is a millisecond less download time. (Nielsen, 2000, p. 22)

Dearnley & Mayhew (1983) have made the case for simplicity in prototyping thus:

A prototype must be simple and [thereby] relatively quick to create, amend and rebuild. . . . The more simple a prototype is to build and modify, the faster the analyst can respond to the [software consumers’] criticisms and ideas. This speed is reassuring to the [software consumer], as he can see his comments being put into action, rather than have to wait weeks or months for the next version, by which time he may have lost enthusiasm. (Dearnley & Mayhew, 1983, p. 41)

The norm of generality, in the context of ISD, prescribes that, in order to ensure maximum flexibility, prototypes, revisions to prototypes, and systems should not be hard-coded, but rather should contain ‘code that doesn’t need to change with every change in the details of its input data’ (Aster, 1998, p. 5). For example, customer billing software that includes tax calculations should be written in generalizable code so that if tax conditions change (e.g. business expands to other tax jurisdictions or tax rate increases), the software can be easily adapted. The prototype should be tested with a variety of different inputs and the systems developer should be made aware of features that are subject to change. If it turns out that the prototype does not contain generalizable code for these features, the systems developer can make the appropriate revisions at that point.

## Social factors

We argue that, in addition to being guided by pragmatic norms, prototype revision is determined by social, or sociological, factors, such as organizational culture, professional training and professional self-interest (see Taylor, 1989; Wager et al., 2005, p. 180). This insight is derived from the social constructivist approach in the sociology of science (see above), which holds ‘that social causes are always present’ (Brown, 1984, p. 9), along with other causes, as determinants of belief revision. As we have noted earlier, social constructivism has been held to be the logical implication of Quine’s underdetermination thesis that there are many – and in principle, an infinite number – alternative theories that fit one set of data. Accordingly, the argument goes, theory choice, or belief revision, is determined by extra-scientific beliefs, that is, beliefs which are not grounded in reason or experience, and so ‘it follows that social [sociological] factors must be invoked to explain why a scientist adopts a particular theory [or revises a particular belief]’ (Ariew, 1984, p. 313). To assert, as social constructivist do, that scientific beliefs are socially determined is to suggest that scientists form particular social beliefs as a consequence of belonging to a community of scholars, which sets professional standards, offers rewards of peer recognition, endorses certain formulae, provides exemplars of research, values some behaviours and establishes model curricula for education and training of future scientists.

In accordance with a social constructivist approach, it is suggested that, for example, in the case of a prototype of a customer relationship manager (CRM) being built for a user law firm, there will be many revision requests from the lawyers on what will appear to the systems developer as trivial or debatable discrepancies between the prototype and the user’s model. We argue that this is so because finding flaws, attentiveness to minute details and probing, interrogative questioning are behaviours that are encouraged by the legal community in law school, continuing legal education and law reviews (e.g. see DeJarnatt, 2002; Proctor, 2004). Moreover, these behaviours are in the lawyers’ professional self-interest as lawyers are rewarded for these activities in their professional practices (see Raasch, 2004).

Similarly, in developing for a hospital an electronic health record system prototype with the aim of having data entry forms in fixed, discrete formats, the systems developer should anticipate that physician users – many of whom are reluctant to use computers in the first instance (Watkins et al., 1999) – will request prototype revisions that will enable them to enter their clinical notes and observations in any format (see Ranganathan et al., 2004). For physicians, especially the older ones, writing with pen on paper is a well-established medical tradition that was observed in medical school and that has continued in medical practice (see Landro, 2005).

IS researchers (e.g. see Narayanan et al., 2002) have long recognized what Flynn & Jazi (1998, p. 53) have referred to as ‘the user-developer culture gap’ in ISD, whereby systems developer and software consumer have differing perspectives – and even different vocabularies (see Özcan, 1998, p. 1360) – so that they perceive the same problem from different vantage points. Systems developers, for example, tend to view user requirements as technical concerns, which are known from the outset and do not change, while paying ‘inadequate attention . . . to the social context within which the computer system will function, with the result that many systems eventually fail’ (Flynn & Jazi, 1998, p. 54). By contrast, software consumers view the requirements through the prism of their domain of interest (e.g. profession, specialization, occupation). Thus, according to the social constructivist insight, both the systems developer and software consumer conceive user requirements differently by virtue of belonging to different professional or occupational communities with varying social beliefs.

Flynn & Jazi (1998) have argued that, in interacting with each other, the systems developer and software consumer revise their socially determined beliefs concerning user requirements and arrive at a set of requirements that they have jointly socially constructed. According to Flynn and Jazi:

[T]he requirements process is a social process and that it is based on the principles of iteration, which may occur within and between rounds, and [software consumer] involvement. We take the view that requirements are not objective artefacts, available at the start of the requirements process. . . . Rather, requirements are emergent: they are socially constructed by the interactions involving [software consumers] and developers in the requirements process [italics in original]. (Flynn & Jazi, 1998, p. 56)

The research of Flynn and Jazi, which dealt with ISD in general and did not address itself specifically to prototyping, suggests that the software consumer’s requests for prototype revisions (as well as the recommended revisions of an independent team of the vendor in alpha testing during packaged software development), and the systems developer’s responses, are influenced by beliefs widely held by other members of the professional or occupational group they belong to and that software consumer–developer interaction will subsequently produce a new set of socially constructed prototype revisions.

The recent scholarly study by Lloyd & Sivin (2002) has considerable bearing on our treatment of how sociocultural circumstances shape prototype revision. Lloyd and Sivin have argued that early Chinese and Greek science and medicine have developed differently because of the existence of different sociological factors, as encapsulated in a ‘cultural manifold’, a global term that includes ‘the continuum of thinkers’ concepts, social goals, professional milieu, mode of discourse, and political associations’ (Keyser, 2004, p. 62). According to Lloyd & Sivin (2002), the divergent social beliefs of the markedly different cultures of ancient China and Greece were responsible for the development of contrasting modes of scientific inquiry, with the Chinese focusing on scholarly consensus and synthesis and the Greeks fostering intellectual disagreement, demand for proof and the search for certainty.

Importing and extending the reach of Lloyd and Sivin’s historical and sociological insights concerning ancient Greek and Chinese scientific development to prototype validation, we suggest that different professions and occupations have different ‘cultural manifolds’, which will influence the content, form and frequency of prototype revisions (see Huysman, 2002). Consider again our previous example of the construction of a CRM prototype for a law firm. We conjecture that there is a cultural divide between systems developers, who hail from a professional community with a collaborative work culture and an emphasis on seeking consensus (Borsook, 2000, p. 233), and lawyers, who come from a competition-oriented work culture where a high premium is placed on adversariality (Proctor, 2004). Thus, as suggested above, such lawyer users will generally seek prototype revisions for slight and arguable discrepancies between the prototype and the user’s mental model, although the collegial orientation of the systems developers should facilitate the joint social construction of revisions to the prototype. Future researchers from both the IS and sociology of knowledge disciplines may wish to further investigate how the differing ‘cultural manifolds’ of systems developers and software consumers influence prototype revisions.

## RELEVANCE OF QUINEAN PHILOSOPHY FOR RESEARCH AND PRACTICE

In light of the ‘applied nature of the IS/IT field’ (Pearson et al., 2005, p. 61), it is fitting that we delineate the practical consequences of adopting a Quinean stance as a theoretical framework for prototype validation.

## Pragmatic commitments

Acceptance of a philosophy of science entails certain pragmatic commitments (van Fraassen, 2002, p. 90). For the researcher, philosophy of science guides what topics are investigated, and for the practitioner, it influences how activities associated with practice are approached. Accordingly, we suggest that, for example, a Quinean IS researcher exploring prototype validation is likely to study user involvement in custom software development and customer involvement in packaged software development as a Quinean perspective, with its key notion that all beliefs are revisable, necessarily underscores the importance of software consumer involvement in revising prototypes. Moreover, we argue that such a Quinean researcher will also tend to examine pragmatic norms and social factors (e.g. sociocultural contexts, professional culture), which are determinants of revision according to a Quinean perspective. With respect to social factors, Lippert & Anandarajan (2004) identified the need to study the influence of organizational culture and social context on the ISD process, a stream of research that a Quinean philosophy would foster.

Similarly, we suggest that practitioners working within a revision-centred Quinean framework will encourage software consumer involvement in refining prototypes, which would be especially beneficial to packaged software development, where generally there is less customer interaction and where there are greater physical distances between software consumer and developer than by custom software development (see Natt och Dag, 2002). A Quinean philosophy of science will also sensitize practitioners to the cultural context within which the software consumer is embedded. In this respect, it is worth noting that Lippert & Anandarajan (2004) have offered practitioners Quinean advice to pay attention to organizational culture – which can be a source of conflict especially in custom software development (see Barki & Hartwick, 2001) – and its influence on systems development. Viewing prototype validation through a Quinean lens will lessen such culture-related conflict.

## The theory ladenness of all software consumers’ observations

Many philosophers of science, among them Quine as well as Popper, Kuhn and Hanson, have held that all of our observations are theory-laden. This concept has been frequently referred to as perspectivism, which ‘is the idea that our knowledge of reality is never “unmediated,” that it is always mediated by a point of view, by a particular set of predilections’ (Searle, 1998, p. 18). Thus, individuals view reality ‘from their own slant, with their own assumption and preconceptions’ (Fay, 1996, p. 72).

We suggest that the software consumer’s perceptions and expectations concerning the prototype are shaped by preconceived ideas conveyed by the developer. In interacting with a software consumer, a Popperian-minded developer will communicate, explicitly or implicitly, to the software consumer that the aim in prototype validation is to find how the prototype differs from the software consumer’s mental model, and hence the software consumer will be predisposed to finding minor flaws and exaggerating their importance. Focusing on prototype-mental model discrepancies, such a user or customer will likely reject and jettison the prototype. In fact, the IEEE Computer Society Professional Practices Committee (2004, pp. 2–9) has warned that in prototype validation there is ‘the danger of [the] users’ [or the customers’] attention being distracted from the core underlying functionality by cosmetic issues.’ For instance, a software consumer who is given the notion by the developer that prototype validation is a Popperian activity may regard the prototype as significantly flawed – and thus grounds for a potential conflict between software consumer and developer – because the screen layout (see Bourn, 2000, p. R14) does not perfectly comport with the software consumer’s mental model when the discrepancy is actually an unimportant issue and can be remedied by a small adjustment.

A Quinean-oriented developer, by contrast, will send a message to the software consumer that the objective in prototype validation is not to reject the prototype but to cooperate with the developer in tweaking and refining the prototype so that it matches with the software consumer’s mental model. Under a Quinean perspective, prototype validation is a revisionary exercise, whereby prototype-mental model discrepancies are to be expected and are not a sufficient cause for software consumer-developer conflict, such discrepancies do not disqualify a prototype, and fine-tuning is the norm. The software consumer provided with a Quinean lens will not dismiss the prototype as non-conforming to the mental model but rather will view it as merely needing some tinkering.

We contend that prototype validation, whose very essence is a series of iterative revisions, in fact, albeit implicitly, follows a Quinean philosophy of science. By stating so explicitly, we are in a position to diffuse and reinforce this approach through IS institutions – university departments, scholarly journals, professional publications, academic and practitioner conferences, and the like.

## Legitimation, rationalization and justification of practice

A Quinean philosophy of science is relevant to practice in that the former serves a justificatory function for the latter. This function is in accordance with Benbasat & Zmud’s (1999, p. 11) suggestion that ‘[t]heories, concepts, and findings from IS research could be used by practitioners to legitimate, rationalize, and justify courses of action taken.’ For Benbasat and Zmud (p. 11), ‘it is important that authors [of IS research papers] develop frames of reference which are intuitively meaningful to practitioners.’ We argue that a Quinean perspective on prototype validation – whereby the prototype is viewed as a mini-theory to be compared to the software consumer’s mental model and is subject to revision so as to conform to such mental model – furnishes an intuitively meaningful frame of reference that encapsulates and justifies the prototype validation endeavour. In particular, the adoption of the revision-centred Quinean philosophy of science, under which revisions are a function of pragmatic norms and social factors, provides a rational warrant for the revision-centred enterprise of prototype validation and places prototype validation within the wider contexts of theory formulation, knowledge acquisition and evidence evaluation. Prototype validation, then, is not viewed as some arbitrary activity in IS that happens to work, but is deemed as an instance of a well-reasoned and welldeveloped philosophy of science.

Moreover, this legitimation, rationalization and justification of the practice of prototype validation supplies an intuitively meaningful frame of reference to IS students – future IS researchers and practitioners – by linking prototype validation to the Quinean general idea that all theories and knowledge are revisable. Hence, ‘we can then firmly ground our attempts at research education in that philosophical framework and convey to students the understanding that method alone is not sufficient for a research programme’ (Wilson, 2003, p. 451). In justifying the practice of prototype validation, a Quinean philosophy of science offers IS students ‘a firm place upon which to stand’ (p. 451).

## CONCLUSION

In this paper, we have set for ourselves the task of situating a theoretical framework for prototype validation in custom and package software development within the philosophy of science. Towards that end, we have compared the Popperian and Quinean accounts of scientific knowledge and have argued that a Quinean philosophy of science, whose cornerstone principle is that all beliefs are revisable, actually corresponds to the activity of prototype validation, and that such correspondence is well warranted. Specifically, we have suggested that prototype revisions are belief revisions, and, as such, are determined by pragmatic norms and social, or sociological, factors.

Our thesis, then, is that the systems developer and software consumer have joined forces – not as Popperian falsifiers, who have a decision rule to reject the prototype on account of any divergence, major or minor, from the software consumer’s mental model, but – as Quinean revisers, with the objective of fine-tuning the prototype (or the software consumer’s mental model) so that the prototype and the software consumer’s mental model are congruent with each other. Rather than focus on searching for inconsistencies between the prototype and the software consumer’s mental model – which would invalidate the prototype – in the manner of Popperian falsifiers, the systems developer and software consumer adopt the stance of Quinean revisers to save the prototype from rejection by removing inconsistencies via adjustments. Such a stance, we have argued, has pragmatic implications for both research and practice.

## REFERENCES

Anderson, R.J., Hughes, J.A. & Sharrock, W.W. (1986) Philosophy and the Human Sciences. Barnes & Noble, Totowa, NJ.

Ariew, R. (1984) The Duhem thesis. British Journal for the Philosophy of Science, 35, 313– 325.

Aster, R. (1998) Coding for Posterity. University of California, Los Angeles, CA, USA, viewed 19 January 2005, [WWW document]. URL http://www.ats.uclas.edu/stat/ sas/library/nesug98/p131.pdf

Barki, H. & Hartwick, J. (2001) Interpersonal conflict and its management in information system development. MIS Quarterly, 25, 195–228.

Benbasat, I. & Zmud, R.W. (1999) Empirical research in information systems: the practice of relevance. MIS Quarterly, 23, 3–16.

Ben-Menahem, Y. (2005) Black, white and gray: Quine on convention. Synthese, 146, 245–282.

Berkun, S. (1999) The importance of simplicity: creating ease of use without losing power. Microsoft Corporation, viewed 19 January 2005, [WWW document]. URL http://msdn.microsoft.com/library/en-us/dnhfact/html/ humanfactor8 4.asp

Blackburn, S. (2001) A. J. Ayer: a life, by B. Rogers Reviewed in: The New Republic, 29 January, pp. 36–40.

Borsook, P. (2000) Cyberselfish: a Critical Romp Through the Terribly Libertarian Culture of HIGH TECHNICAL. PublicAffairs, New York, NY, USA.

Bourn, J. (2000) Report of the controller and auditor general class III vote 9: appropriation accounts (Volume X) 1999– 2000 (National Audit Office Report, London), viewed 9 January 2006, [WWW document]. URL http://www.nao. org.uk/publications/nao\_reports/00-01/dvla.pdf

Boyd, R. (1991) Confirmation, semantics, and the interpretation of scientific theories. In: The Philosophy of Science, Boyd, R., Gasper, P. & Trout, J.D. (eds), pp. 3–35. MIT Press, Cambridge, MA, USA.

Brown, J.R. (1984) Scientific Rationality: the Sociological Turn. Reidel, Dordrecht, the Netherlands.

Carnap, R. (1966) Philosophical Foundations of Physics: an Introduction to the Philosophy of Science. Basic Books, New York, NY, USA.

Dearnley, P.A. & Mayhew, P.J. (1983) In favour of system prototypes and their integration into the systems development cycle. Computer Journal, 26, 36–42.

DeJarnatt, S.L. (2002) Law talk: speaking, writing, and entering the discourse of law. Duquesne Law Review, 40, 489–522.

Duhem, P. (1906) La Théorie physique, son objet et sa structure. Chevalier et Rivière, Paris, France.

Dussart, A., Aubert, B.A. & Patry, M. (2004) An evaluation of inter-organizational workflow modeling formalisms. Journal of Database Management, 15, 74–104.

Edwards, P. & Pap, A. (eds) (1965) A Modern Introduction to Philosophy: Readings from Classical and Contemporary Sources, rev. ed. Free Press, New York, NY, USA.

Elliot, S. & Avison, D. (2004) The discipline of information systems. The International Federation for Information Processing (IFIP) Technical Committee on Information Systems (TC 8) Website, viewed 19 September 2004, [WWW document]. URL http://ifiptc8.itu.dk/superwork/ Ch4Mar04.pdf

Fay, B. (1996) Contemporary Philosophy of Social Science: a Multicultural Approach. Blackwell, Oxford, UK.

Floridi, L. (2002) What is the philosophy of information? Metaphilosophy, 33, 123–145.

Flynn, D.J. & Jazi, M.D. (1998) Constructing user requirements: a social process for a social context. Information Systems Journal, 8, 53–83.

van Fraassen, B.C. (2002) The Empirical Stance. Yale University Press, New Haven, CT, USA.

Gillott, J. & Kumar, M. (1997) Science and the Retreat from Reason. Monthly Review Press, New York, NY, USA.

Glymour, C. (1980) Theory and Evidence. Princeton University Press, Princeton, NJ, USA.

Hacking, I. (1999) The Social Construction of What? Harvard University Press, Cambridge, MA, USA.

Herskovitz, P.J. (1991) A theoretical framework for simulation validation: Popper’s falsificationism. International Journal of Modelling and Simulation, 11, 56–58.

Hirschheim, R., Klein, H.K. & Lyytinen, K. (1995) Information Systems Development and Data Modeling: Conceptual and Philosophical Foundations. Cambridge University Press, Cambridge, UK.

Hookway, C. (1988) Quine: Language, Experience and Reality. Stanford University Press, Stanford, CA, USA.

Huysman, M. (2002) Organizational learning and communities of practice: a social constructivist perspective. Proceedings of the Third European Conference on Organizational Knowledge, Learning, and Capabilities, pp. 1–16.

IEEE Computer Society Professional Practices Committee (2004) Guide to the software engineering body of knowledge, viewed 9 January 2006, [WWW document]. URL http://www.swebok.org/ironman/pdf/SWEBOK\_ Guide\_2004.pdf

Katz, J.J. (1998) Realistic Rationalism. MIT Press, Cambridge, MA, USA.

Keil, M. & Carmel, E. (1995) Customer-developer links in software development. Communications of the ACM, 38, 33–44.

Kemeny, J.G. (1959) A Philosopher Looks at Science. Van Nostrand, Princeton, NJ, USA.

Keyser, P.T. (2004) The way and the word: science and medicine in early China and Greece, G. Lloyd & N. Sivin. Reviewed in: Aestimatio, 1, 62–72.

Klein, H.K. (2004) Seeking the new and the critical in crit ical realism: déjà vu? Information and Organization, 14, 123–144.

Klein, E.E. & Herskovitz, P.J. (2005) Philosophical founda tions of computer simulation validation. Simulation and Gaming, 36, 303–329.

Kujala, S. (2003) User involvement: a review of the benefits and challenges. Behaviour and Information Technology, 22, 1–16.

Landro, L. (2005) The high-tech cure. The Wall Street Journal, 17 January, pp. R4, R5.

Lantz, K.E. (1987) The Prototyping Methodology. Prentice Hall, Upper Saddle River, NJ, USA.

Larsen, T.J. & Levine, L. (2005) Searching for management information systems: coherence and change in the discipline. Information Systems Journal, 15, 357– 381.

Laudan, L. (1990) Science and Relativism: Some Key Controversies in the Philosophy of Science. University of Chicago Press, Chicago, IL, USA.

Lewthwaite, A. (2003) A new look at falsification in light of the Duhem-Quine thesis. Ecclectica, viewed 23 January 2005, [WWW document]. URL http://www.ecclectice.ca/ issues/2003/1/lewthwaite.asp

Lichtblau, E. (2005) F.B.I. may scrap vital overhaul for com puters. The New York Times, 14 January, pp. A1, A20.

Lippert, S.K. & Anandarajan, M. (2004) Academic vs. prac titioner systems planning and analysis. Communications of the ACM, 47, 91–94.

Lipton, P. (1991) Inference to the Best Explanation. Rout ledge, London, UK.

Lloyd, G. & Sivin, N. (2002) The Way and the Word: Sci ence and Medicine in Early China and Greece. Yale University Press, New Haven, CT, USA.

Mäntyniemi, A., Pikkarainen, M. & Taulavuori, A. (2004) A Framework for Off-the-Shelf Software Component Development and Maintenance Processes. VTT Technical Research Centre, Vuorimiehentie, Finland.

Monod, E. (2004) Einstein, Heisenberg, Kant: methodological distinction and conditions of possibilities. Information and Organization, 14, 105–121.

Morcor Solutions Inc. (2005) Importance of user interface, viewed 19 January 2005, [WWW document]. URL http://www.morcor.com/intrface.htm

Murphy, F. & Seddon, P. (2003) An initial model of the motivations of packaged-software developers and their customers to establish close relationships. Proceedings of Australasian Conference on Information Systems (ACIS), viewed 8 October 2005, [WWW document]. URL http://www.dis.unimelb.edu.au/oasis/felicityacis2003.doc

Nagel, E. (1960) Preface. In: Philosophy of Science, Danto, A. & Morgenbesser, S. (eds), pp. 11–14. Merid ian Books, Cleveland, OH, USA.

Narayanan, S., Bailey, W., Tendulkar, J., Daley, R., Pliske, D.B. & Wilson, K. (2002) Design of model–based interfaces for a real world information system. IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans, 32, 11–24.

Natt och Dag, J. (2002) Elicitation and management of user requirements in market-driven software development (Lund University Institute of Technology, Sweden, Technical Report no. 146), viewed 22 December 2005, [WWW document]. URL http://www.lucas.lth.se publications/pub2002/020612Johan.pdf

Naumann, J.D. & Jenkins, A.M. (1982) Prototyping: the new paradigm for systems development. MIS Quarterly, 6, 29–44.

Nielsen, J. (2000) Designing Web Usability: the Practice of Simplicity. New Riders Publishing, Indianapolis, IN, USA.

Norris, C. (2000) Minding the Gap: Epistemology and Philosophy of Science in the Two Traditions. University of Massachusetts Press, Amherst, MA, USA.

O’Hear, A. (1989) Introduction to the Philosophy of Science. Clarendon Press, Oxford, UK.

Okasha, S. (2002) Philosophy of Science: a Very Short Introduction. Oxford University Press, Oxford, UK.

Orenstein, A. (1977) Willard Van Orman Quine. Twayne Publishers, Boston, MA, USA.

Oz, E. (2004) Management Information Systems, 4th edn. Course Technology, Boston, MA, USA.

Özcan, M.B. (1998) Use of executable formal specifications in user validation. Software – Practice and Experience, 28, 1359–1385.

Papineau, D. (1996) Philosophy of science. In: The Blackwell Companion to Philosophy, Bunnin, B. & Tsui-James, E.P. (eds), pp. 290–324. Blackwell, Oxford, UK.

Pearson, J.M., Pearson, A. & Shim, J.P. (2005) The relevancy of information systems research: the practitioner’s view. Information Resources Management Journal, 18, 50–67.

Popper, K.R. (1957) Philosophy of science: a persona report. In: British Philosophy in the Mid-Century: a Cambridge Symposium, Mace, C.A. (eds), pp. 155–191. Macmillan, New York, NY, USA.

Popper, K.R. (1959) The Logic of Scientific Discovery, K.R. Popper, with J. Freed & L. Freed (trans). Basic Books, New York, NY, USA.

Popper, K.R. (1965) Conjectures and Refutations: the Growth of Scientific Knowledge, 2nd edn. Basic Books, New York, NY, USA.

Popper, K.R. (1983) Realism and the Aim of Science. Rowman and Littlefield, Totowa, NJ, USA.

Proctor, P. (2004) Toward mythos and mythology: applying a feminist critique to legal education to effectuate a socialization of both sexes in law school classrooms. Cardozo Women’s Law Journal, 10, 577–602.

Quine, W.V. (1951) Two dogmas of empiricism. Philosophical Review, 60, 20–43.

Quine, W.V. (1969) Epistemology naturalized. In: Ontological Relativity and Other Essays, Quine, W.V. (ed.), pp. 69–90. Columbia University Press, New York, NY, USA.

Quine, W.V. (1975) On empirically equivalent systems of the world. Erkenntnis, 9, 313–328.

Quine, W.V. (1991) Two dogmas in retrospect. Canadian Journal of Philosophy, 21, 265–274.

Quine, W.V. (2000a) I, you, and it: an epistemological triangle. In: Knowledge, Language and Logic: Questions for Quine, Orenstein, A. & Kotatko, P. (eds), pp. 1–6. Kluwer Academic Publishers, Boston, MA, USA.

Quine, W.V. (2000b) Response to Lehrer. In: Knowledge, Language and Logic: Questions for Quine, Orenstein, A. & Kotatko, P. (eds), pp. 411–412. Kluwer Academic Publishers, Boston, MA, USA.

Quine, W.V. & Ullian, J.S. (1970) The Web of Belief. Random House, New York, NY, USA.

Raasch, J.E. (2004) Learn to understand, appreciate, and work with the legal personality. Legal Market Association, 19 October, viewed 17 January 2005, [WWW document]. URL http://www.legalmarketing.org/news/ news.asp?news\_id=350

Ranganathan, C., Watson-Manheim, M.B. & Keeler, J. (2004) Bringing professionals on board: lessons on executing IT-enabled organizational transformation. MIS Quarterly Executive, 3, 151–160.

Rosenthal, R. & Rosnow, R.L. (1991) Essentials of Behavioral Research: Methods and Data Analysis, 2nd edn. McGraw-Hill, Boston, MA, USA.

Sawyer, S. (2000) Packaged software: implications of the differences from custom approaches to software development. European Journal of Information Systems, 9, 47–58.

Sayer, A. (1984) Method in Social Science: a Realist Approach. Hutchinson, London, UK.

Searle, J.R. (1998) Mind, Language Society: Philosophy in the New World. Basic Books, New York, NY, USA.

Simkin, C. (1993) Popper’s Views on Natural Social Science. E. J. Brill, New York, NY, USA.

Skinner, Q. (1985) Introduction: the return of Grand The ory. In: The Return of Grand Theory in the Human Sci-

ences, Skinner, Q. (ed.), pp. 1–20. Cambridge University Press, Cambridge, UK.

Stove, D. (1999) Against the Idols of the Age. Transaction Publishers, New Brunswick, NJ, USA.

Straub, D., Gefen, D. & Boudreau, M. (2004) Qualitative research in information systems. The International Federation for Information Processing (IFIP) Technical Committee on Information Systems (TC 8) Website, viewed 10 August 2004, [WWW document]. URL http:// ifiptc8.itu.dk/superwork/Ch6Mar04.pdf

Taylor, P. (1989) Revising models and generating theory. Oikos, 54, 121–126.

Taylor, R.G. (2005) The growth of scientific knowledge in MIS: The MIS paradigm. Proceedings of the Eleventh Americas Conference on Information Systems, pp. 2897–2903.

Vuillemin, J. (1986) On Dunhem’s and Quine’s theses. In: The Philosophy of W. V. Quine, Hahn, L.E. & Schilpp, P.A. (eds), pp. 595–622. Open Court, La Salle, IL, USA.

Wager, K.A., Lee, F.W. & Glaser, J.P. (2005) Managing Health Information Systems: a Practical Approach for Health Care Executives. Jossey-Bass, San Francisco, CA, USA.

Watkins, C., Harvey, I., Langley, C., Faulkner, A. & Gray, S. (1999) General practitioners’ use of computers during the consultation. British Journal of General Practice, 49, 381–383.

Webb, K. (1995) An Introduction to Problems in the Philosophy of Social Sciences. Pinter, London, UK.

Weinberg, S. (1998) The revolution that didn’t happen. The New York Review of Books, 8 October, pp. 48–52.

Weinberg, S. (2000) Could we live without quarks? Times Literary Supplement, 18 February, p. 8.

Wilson, T.D. (2003) Philosophical foundations and research relevance: issues for information research. Journal of Information Science, 29, 445–452.

Winder, R.L., Probert, S.K. & Beeson, I.A. (eds) (1997) Philosophical Aspects of Information Systems. Taylor & Francis, London, UK.

## Biographies

Esther E. Klein is Assistant Professor in the Department of Business Computer Information Systems/Quantitative Methods at the Frank G. Zarb School of Business, Hofstra University. She received her PhD in computer science with a specialization in management information systems from the Graduate Center of the City University of New York (CUNY). Prior to joining academia, she served as senior statistical analyst at Pfizer and systems analyst for the Power Authority of the State of New York. Her current research interests include: philosophical issues in information technology; ethical issues in computer-mediated communication; epistemology of computer simulation; collaborative technologies and organizations; group support systems (GSS); leadership in computer-mediated contexts; and creativity and gender in computer-mediated decision-making groups. She has had articles published in various journals, including Computers in Human Behavior and The Journal of Leadership Studies and in various academic proceedings such as those of AIS, DSI, IRMA and NEDSI. She has recently authored a chapter on GSS in an edited scholarly book and an article on GSS and creativity in a technology encyclopaedia. Dr Klein is the recipient of the ‘Best Published Paper of the Year’ award by The Journal of Leadership Studies for ‘The Impact of Information Technology on Leadership Opportunities for Women: The Leveling of the Playing

Field’ (Summer 2000). She has been a guest speaker at many academic forums.

Paul J. Herskovitz is Associate Professor in the Depart ment of Business at the College of Staten Island, CUNY. His current research interests include: philosophy of science and the law of evidence; the intersection of law, technology and philosophy; legal aspects of compute simulation; philosophy of science and information systems; epistemology of computer simulation; philosophica aspects of computer-supported collaborative work, ethical aspects of computer-mediated communication; leadership in computer-mediated contexts; and the legal liability of accountants. He has had articles published in various jour nals, including Midwest Law Review, Journal of Law and Business, Computers in Human Behavior and International Journal of Modelling & Simulation and in various academic proceedings. He is a member of the New York and Florida Bars, various professional organizations. Currently, he is on sabbatical.
