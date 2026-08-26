---
otero_id: 21562
otero_key: "HP4624KE"
title: "On hypermedia-based argumentation decision support systems"
authors: "Gary H Hua; Steven O Kimbrough"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00062-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On hypermedia-based argumentation decision support systems <sup>1</sup>

Gary H. Hua <sup>a,2</sup>, Steven O. Kimbrough <sup>b,)</sup>

<sup>a</sup> Research and DeÕelopment Department, Reed Technology and Information SerÕices, One Progress DriÕe, Horsham, PA 19044, USA UniÕersity of PennsylÕania, The Wharton School, Steinberg Hall–Dietrich Hall, Suite 1300, Philadelphia, PA 19104-6366, USA

## Abstract

This paper presents and discusses a logical apparatus which may be used to support machine-based inferencing and automatic creation of hypertext links in what we call hypermedia-based argumentation decision support systems HADSS .Ž . This logical approach has important advantages over other sorts of argument representation, found in the current literature. We present and discuss a prototype implementation in the context of three examples. We also present an exploratory experiment indicating that graph-based logical representations can materially help people make better inferences. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Argumentation; Decision support systems; Defeasible reasoning; Hypermedia; Hypertext; Logic

## 1. Introduction

There is a growing consensus, supported by a growing literature, to the effect that principles of hypermedia including hypertext and multimedia ,Ž . when applied in argumentation decision support sys-Ž . <sup>3</sup> tems DSSs , will add enormous value. The theory here is that hypermedia systems add value: by facilitating information filtering e.g., with graphical rep- Ž resentations of arguments , by assisting in informa-. tion retrieval e.g., at the click of a mouse , and byŽ . facilitating vivid and forceful presentation of information e.g., with animation and business graphics . Ž . The consensus—with which we are in accord—is widely shared and is expressed in a broadly-based literature. Argumentation concepts have been articu-Ž <sup>w</sup> <sup>x</sup>. <sup>4,</sup> <sup>5</sup> lated e.g., see Refs. 22,30,31,36 , and systems have been built e.g., Refs. 1,9–11,22,42,43,49 .Ž <sup>w</sup> <sup>x</sup>.

This consensus—on the need for, and practicality of, hypermedia-based argumentation DSS HADSSŽ . —is supported by two sorts of evidence. First, existing systems, while mainly prototypes, have generally been convincing to those who have seen them and worked with them. People, at least many people, have found the idea of hypermedia-based argumentation DSS very attractive, once they have seen examples of such systems. This evidence, however, has circulated more in the oral tradition than in the literature. Second, there is a small but growing body of empirical research showing that people, unaided by supporting technology, perform rather poorly at constructing, evaluating, and communicating arguments e.g., see Refs. 2,37 and Ref. 24 , especially Ž <sup>w</sup> <sup>x</sup> <sup>w x</sup> Chapter 2 . This work can be seen as doing for logic. and argumentation what Kahneman et al. 27 and<sup>w</sup> <sup>x</sup> Tversky and Kahneman 61,62 have done for utility<sup>w</sup> <sup>x</sup> theory: demonstrating that, unaided by appropriate technology, people’s performances fall considerably short of what the best available normative theory prescribes. <sup>6</sup>

Our aims in this paper are to raise three central questions about HADSSs there are others , and toŽ . advance admittedly partial answers to these ques- Ž . tions: 1 How should arguments including rebut-Ž . Ž tals, counter-arguments, rebuttals of rebuttals, and so on be represented? See Section 2; 2 What features. Ž . can and what should be provided by way of machine support for creating, evaluating, comparing, and exploring arguments? See Section 3. 3 How usefulŽ . and practicable is the HADSS idea? See Section 4, where we discuss examples suggesting that a positive answer to this question can, with further research, be made; see Section 5, where we present an experiment that indicates that with proper graphical representation people make fewer deductive infer-Ž . ential mistakes?

## 2. Arguments and argumentation theory

Reasoning has been described as ‘‘mental activity that consists of transforming given information Ž . called the set of premises in order to reach conclusions’’ Ref. 18 , p. 333 . In the jargon of logic, theŽ <sup>w</sup> <sup>x</sup> . conclusion is a particular statement, and the premises are also statements linguistic expressions that can be Ž either true or false . Together, they are called an. argument. It is the main business of logic to study arguments. As reasoning is the transformation of premises to reach a conclusion, then we may characterize a reason as an account of how particular premises were transformed to produce a particular conclusion. Equivalently, then, we may say that it is the main business of logic to study reasons.

An argument, thus, from the point of view of logic, consists of zero or more premises, and a conclusion. Both premises and conclusion are statements, possibly complex statements that are composed from other statements. In a successful argument, the premises can be taken as good reasons to believe the conclusion, because it can be established that if the premises are true, then the conclusion must be true. Arguments with this property are said to be valid. If the premises of a valid argument are also true, then the argument is said to be sound. Logic, to repeat, is the study of arguments, of what makes some better than others, of what makes an argument successful or not, of what constitutes validity, and so on. The actual truth or falsehood of premises is usually taken not to be part of logic, but part of natural science, broadly conceived. Similarly, the actual causal processes we undergo in transforming premises to conclusion is usually seen as part of cognitive psychology. Consequently, the theory of arguments and argumentation is a very broad one, and has at least a logical aspect and a psychologi-Ž . cal aspect. We shall touch on both aspects in what follows.

There are two traditions in the study of logic: formal logic and informal or semi-formal logic.Ž . Formal or symbolic or mathematical logic is theŽ . study of logic in which the arguments under consideration are symbolized into a well-defined language that can be manipulated according to a strict set of rules and independently of the meanings or intendedŽ interpretation of the sentences in the argument sym-. bolized. Logic was first studied from a formal point of view by Aristotle and has been studied, and developed, more or less continually since his time. Precision and rigor have been the motivations for the formal study of logic, and a rich variety of fully formal logical calculi have been developed and examined. A happy consequence of this formalization is that the resulting calculi can be—and have been—implemented in software.

Formal logic, then, can be thought of as providing a computational and a normative theory of argument.

This is just what is needed, or so it would seem, for computerized argumentation support systems. There are problems, however. First, as might be expected of any effort at formalization, there are problems of limitation in scope we call this the scope problem .Ž . Although the range of formal logical languages is impressive and growing, it still falls well short of the requirements of everyday, practical deliberation. Things as simple as newspaper articles particularlyŽ editorials and op ed pieces severely stretch the . natural expressive capabilities of the standard logics, which do not do well at representing such concepts as time and obligation 35 . Much worse, in our view, is that standard logics do poorly at handling defeasible reasoning, reasoning that involves inferences that may be defeated by new information See,Ž e.g., Refs. 7,19,20,38,45–49,52,53,55 for discus- <sup>w</sup> <sup>x</sup> <sup>7</sup> sion of defeasible reasoning. See Refs. 23,29,32–<sup>w</sup> 34 for a technical introduction to the methods of<sup>x</sup> logic graphs and of sweeping presumptions, the logic we have developed for argumentation DSSs. Since. nearly all practical inferences are defeasible someŽ examples, including a newspaper example, are presented in Section 4 , this is indeed a worrisome . shortcoming.

Formal logics have a second serious problem, if they are to serve as bases for computerized argumentation support systems. Logical notation is arcane Ž . we call this the friendliness problem . Without extensive training in logic, it is simply not on to expect users to have meaningful understanding of formalized expressions.

These problems have long been recognized and have led to the study of logic from a non-formal, or semi-formal, point of view. Such studies have been conducted since the time of Plato. There are broadly two relevant literatures. First, there is an extensive literature that goes by the name of informal logic. There are two primary journals in this field, Informal Logic, and Argumentation, as well as two professional societies, the Association for Informal Logic and Critical Thinking, and the International Society for the Study of Argumentation. In addition, quite a number of textbooks have appeared devoted to the subject e.g., see Refs. 12,14,15,26,28,50,54,59,60 Ž <sup>w</sup> <sup>x</sup> as well as Refs. 63–66 . The second body of <sup>w</sup> <sup>x</sup>. literature is much smaller. It consists of reports of experiences with implementations of argumentation systems. Examples include Refs. 1,4,11,21,22, <sup>x</sup> <sup>4</sup> 36,39–44,56,57 .

It is not to our purpose here to review this literature in any depth. What matters most, for present purposes, is that both literatures are essentially in agreement that arguments can and, for pragmaticŽ reasons, should be represented as directed graphs, in. which nodes stand for statements and arcs stand for certain ‘semantic’ relations between statements. <sup>8,</sup> <sup>9</sup> For example, Hashim’s Ref. 22 , p. 238 list ofŽ <sup>w</sup> <sup>x</sup> . semantic relations for Issue-Based Information Systems IBISs includes ‘supports’, ‘challenges’, ‘re-Ž . sponds to’, and ‘objects to’, but there is no broad agreement on these labels.

We may compare formal and informal or semi- Ž formal approaches to argument representation in . computerized support systems. Formal logics are beset with the scope and friendliness problems. Informal or semi-formal approaches are agreed on Ž . resolving the friendliness problem by representing arguments as directed graphs, although different informal approaches will differ on how these graphs are to be constructed. Informal approaches may be thought of as dealing with the scope problem by treating the semi-formal, graph-based representation as an approximate model of the underlying argument. Users viewing the representation are then free to make transformations and manipulations that reflect intuitive concepts of, say, time, obligation, and defeasibility. The graph representation is used much as a rough map: not itself a calculation device, it helps by prompting the user to think things through.

The informal approaches, thus, have much to be said in their favor. What they lack is a principled theory of inference. Using the IBIS framework butŽ the point generalizes , if statement A supports B, . which supports C, if D challenges C, and if both A and D are presumed true, then what are we to believe about C? There is no theory to help us, nor is there any calculation that might be offered in this regard. Addressing the scope problem by going informal is a sword that cuts two ways.

Ideally, we would like graph-based argumentation representations with an underlying proof theory that addresses the problem of scope. This is not a world in which ideals are often realized. We submit, however, that logic graphs and sweeping presumptions Ždiscussed in Refs. 23,33,34,29 are fair contenders.<sup>w</sup> <sup>x</sup>. Fair enough, at least, to be worth exploring. The main purpose of the remainder of this paper is to report upon our initial investigations of using logic graphs for deductive inference and sweeping pre- Ž . sumptions an extension of logic graphs, for defeasi- Ž ble reasoning as a graph-based representation . scheme for argumentation DSSs.

## 3. Machine assistance

The problems of scope and friendliness hardly exhaust the challenges in designing and implementing a HADSS. Paramount among the remaining challenges is the treatment of hypermedia.

A HADSS, as we conceive it, would have two broad categories of hypermedia links: links between elements of the argumentation network internalŽ links , and links between elements in the network. and elements outside the network external links .Ž . For example, at a given node, the presence of an incoming arc might be exploited to determine that another node the node originating the incoming arc Ž . provides support for the statement at the node we are at, i.e., the given node. This would be an internal link. An external link at a node might be used to display corroborating documents, videos, and so on for the assertion at the node.

As we have noted indeed, emphasized , in logic Ž . graphs and sweeping presumptions arguments are representable as networks. This fact can be exploited to counter a well-known problem with hypermedia: the high cost of building hyperdocuments due to manual node creation and linking 5,6,9 .<sup>w</sup> <sup>x</sup>

Any HADSS should facilitate interactive, ad hoc construction and modification of arguments, and provide hypertext-style access to documents relevant to particular arguments. These aims would strongly suggest that a gIBIS-style graphical IBIS, see aboveŽ . interface 11 could be usefully adapted for browsing <sup>w</sup> <sup>x</sup> through argumentation representations. In gIBIS-style systems, the user is presented with a graph in which the nodes and arcs are given special meaning, pertaining to the subject at hand. For example, in an argumentation system as noted earlier nodes mightŽ . represent issues, positions, or arguments, and arcs might represent such ‘semantic’ notions as ‘supports’, ‘rebuts’, and ‘suggests’.

We agree that such a facility a gIBIS-style inter- Ž face for a HADSS would very likely be useful.. Merely having such an interface, however, leaves unresolved two important problems. <sup>10</sup>

The first problem is that of building a system that can automatically construct hypertext links. Specifically, documents will be relevant to particular nodes and arcs. A user should be able to direct the system to produce, say, all the documents relevant to the node representing objections to the ‘pay or play’ proposal for health care financing. Additionally, the HADSS should, insofar as is possible, find these documents automatically, that is without a person having explicitly to specify that a particular document is relevant. In previous works, we have addressed this problem successfully, but in a different context 5,6,36 . We believe, however, that the tech-<sup>w</sup> <sup>x</sup> niques developed and applied in that work can be useful in the present context. Because the nodes andŽ the arcs are meaningful they represent propositions. Ž or relations among propositions and formally repre-. sented, they can be exploited to create external links automatically. For example, if a node asserts that P, then documents that discuss P are possibly relevant to that node. Since P is a formal expression, text generation techniques can be used to generate key words, which may then be used to search the database of documents. Further, the location of node P in the network can be exploited to focus the search for relevant documents. For example, if Q implies P and Q is known or presumed to be true , then it may beŽ . prudent to focus the automated search on documents pertaining to both P and Q. Generalizations of these points are easy to imagine. It remains to test them on real databases and apply them to real problems.

The second problem with relying only on gIBIS-Ž style interfaces has to do with a limitation in exist- . ing gIBIS-style systems, which use the IBIS framework for representing arguments and other things, Ž such as discussions graphically. For the purpose of . modeling arguments, the IBIS framework is but one of many see references above , and it has someŽ . important shortcomings. For present purposes, the most salient limitation of the IBIS framework is that it is not a logic and does not support logical inference. At best, it would be difficult to support machine-based inference for an IBIS representation.

Thus, as an alternative to IBIS, we are proposing to use logic graphs and the method of sweeping presumptions to represent arguments in HADSS implementations. <sup>11</sup> A HADSS could be given a number of operations that help with decision support by exploiting the network representation and underly-Ž ing theory, sweeping presumptions to produce links. automatically. These operations include procedures to answer the following questions. Answers could be assembled dynamically and displayed as new hypertext nodes.

Ž . 1 Is the argument valid? This operation checks if an argument is constructed according to the argument formation rules syntax validity checking . TheŽ . operation also checks if there are any conflicts among the subarguments and if all the assumptions are supported by the evidence semantics validity check- Ž ing . In the case of a finding of invalidity, a recom-. mendation can be proposed.

Ž . 2 Are there counter-arguments to a given argument? This operation generates a set of potential counter-arguments to an argument from the evidence and reasonable assumptions. A counter-argument is any rebutting defeater or undercutting defeater to the argument See, e.g., Refs. 51 for definitions of Ž <sup>w</sup> <sup>x</sup> these terms ..

Ž . 3 Is a counter-argument effective? This operation compares the relative strengths between the conflicting arguments, and recommends some methods to enforce an argument. For example, the strength of an argument can be increased by increasing support to a critical premise or by increasing the strength on the defeasible rules in the argument or by introducing the defeaters to the counter-argument.

Ž . 4 What if we changed a given assumption? ‘What-if’ analysis is the process of making changes to the evidence data, the assumption data or the strengths of defeasible inference rules and observing the impact to an argument and its counter-arguments.

Ž . 5 What would need to be the case for this argument or counter-argument to be effective Ž . Ž . goal-seeking analysis ? Goal-seeking analysis is the process of providing a reasoning chain for an argument which supports a desired conclusion. This operation identifies the critical evidence, assumptions, as well as the defeasible inference in the arguments. The argument can be weakened or invalidated by weakening the strengths of the defeasible inferences or by removing the critical evidence or assumptions. Alternatively, the irrelevant information for an argument can also be identified.

We have developed a prototype implementation of a HADSS, and we call it HADSS. This prototype is based on sweeping presumptions, and is able to draw theoretically-correct logical inferences. Thus, it directly addresses the validity question 1, above forŽ . the arguments it represents. Our implementation also directly addresses the effectiveness of the counterargument question see 3, above . Counter-argu-Ž . ments are represented as rebutting and<sup>r</sup>or undercutting defeaters and the program totals up the strengths Ž . as determined by sweeping presumptions of the reasons pro and con. The what-if question 4, above Ž . is directly addressed by our HADSS. Users may interactively set statements represented as nodes to Ž . be true, false, or not known to be either. In virtue of having the what-if capability, our HADSS has modest support for the goal-seeking question 5, above . Ž . Users may seek goals by iterating what-if questions. Finally, there is some computational support for the counter arguments question 2, above . HADSS canŽ . list the rebuttals and defeaters see Ref. 23 for aŽ <sup>w</sup> <sup>x</sup>. given conclusion. We note, however, that at present the listings become hard to follow if the underlying arguments are complex. Users must often rely on visual inspection of the argument graph. We plan to address this problem in a future version.

## 4. Implementation

We will describe our HADSS implementation in the context of three examples.

## 4.1. Toulmin’s Anne

Toulmin Ref. 59 , p. 126 presents a simple, but Ž <sup>w</sup> <sup>x</sup> . interesting and commonsensical, example of defeasible reasoning: 1 Anne is one of Jack’s sisters; 2 Ž . Ž . All Jack’s sisters have previously been observed to have red hair; 3 So, presumably, Anne now has redŽ . hair, unless Anne has dyed her hair, gone white, lost her hair, etc.

Toulmin has his own diagrammatic approach to representing arguments, but for the sake of conserving space we shall not further discuss his approach here. Under our approach, this argument might be graphed as in Fig. 1. <sup>12</sup>

Briefly, our implementation works as follows. HADSS allows the argument graph to be constructed interactively. Once the network is constructed, the user may declare certain assumptions and perform the operations for answering the questions listed in Section 3. In the present example, one declares the assumption that Anne is one of Jack’s sisters by clicking on the S x node and responding to a dialog Ž . box. If there are no further assumptions, the user may then click on the conclusion node, NR x , andŽ . ask whether it can be inferred. The system then produces a report regarding the assertion at this node. Here, HADSS would report that PPNR x canŽ .

![](/api/attachments/HP4624KE/fulltext/images/c5b85e38e345c57837d7d1e2384f8683bfa65b395a21649ba2c800a11a126052.jpg)  
Fig. 1. The HADSS representation of Toulmin’s Anne: S x , x isŽ . one of Jack’s sisters; R x , x has red hair; D x , x has dyed hair,Ž . Ž . P , presumably, ; W , it was true at least once that ; N , it is now true that .

be derived ‘Presumably, presumably it is now trueŽ that R x ’ with a valid argument which supportsŽ . . NR x , and that nothing else can be derived concern-Ž . Ž . <sup>13</sup> ing NR x . Suppose the user adds the assumption that Anne now has dyed hair this is done as above,Ž by clicking on the appropriate node . If then we click . on the conclusion node, HADSS reports see Fig. 2 Ž . that PPNR x can be derived as before , but alsoŽ . Ž . reports this argument is defeated by an undercutting defeater. Consequently, nothing can be concluded regarding the color of Anne’s hair. HADSS provides users with a graphical interface for constructing argument networks and for making initial assumptions, so the users can easily perform what-if analysis by adding or deleting links and changing the assumptions. Further, since the strengths of relevant arguments are explicitly displayed, the users may analyze how changes on strengths of competing arguments may effect the conclusion.

## 4.2. Presidential polls

Our second example comes from an op ed piece, which discusses why on June 27, 1992 the variousŽ .

![](/api/attachments/HP4624KE/fulltext/images/ddcef620801732d2f5867cdd6e3b349e5a401a86bea413ef70c758faf60ed0c5.jpg)  
Fig. 2. The HADSS report on Toulmin’s Anne.

presidential polls were in so much disagreement 16 .<sup>w</sup> <sup>x</sup> In essence, the thesis of the article is that the polls are in disagreement with each other because theŽ . voters’ judgments are volatile. The author of the article, Kathleen Frankovic, assumes that if voters are volatile VV then presumably the polls will be Ž . in mutual disagreement PD . She provides evidence Ž . Ž . more on this shortly that in fact the polls are in disagreement. Most of the article which is quiteŽ short is given over to providing evidence regarding. the fact that different questions are asked by different polling organizations DQDA and that theseŽ . lead to the different answers we see. At the end of her article, Frankovic briefly asserts that the polls also show that voters are distressed and confused Ž . VDC . Her argument may be summarized with the argument network in Fig. 3, which is a screen dump from the HADSS representation of the network.

![](/api/attachments/HP4624KE/fulltext/images/64be429e357a0a0c43144fc4af40c90314431bc503ffc748fb7559978d266a10.jpg)  
Fig. 3. The HADSS representation of presidential polls argument: DQDA, different questioning by different polls produces different answers; PD, the polls disagree; VV, the voters are volatile; VDC, the voters are distressed and confused.

![](/api/attachments/HP4624KE/fulltext/images/9c1f8b0dd795ddaa651054724cead2eb02f14f7a4fe270dc57fad9b39048b342.jpg)  
Fig. 4. The HADSS representation of information attached to node DQDA in the presidential polls argument.

The features described above with regard to Toulmin’s Anne Section 4.1 apply here as well. The Ž . argument in the network is a simplified and abstracted version of that presented in the article. For example, Frankovic presents specific claims about how The New York Times<sup>r</sup>CBS News poll was taken, about the Time–CNN poll, and so on. This information is not represented in the argumentation network per se, but it is available to the HADSS user. Sticking to our present example, the polling information is relevant to the argument because it supports the assertion at the DQDA node. A user may gain access to this information by clicking on the DQDA node and asking for more information Ž . see Fig. 4 .

![](/api/attachments/HP4624KE/fulltext/images/a14d4da7f6a11516dfdd572739f17f3fc7759f23ddcadcf427bc786acdb879fd.jpg)  
Fig. 5. The HADSS representation of documents associated with the keyword argumentation in the presidential polls argument.

In the current implementation more information is obtained inferentially and dynamically, at run timeŽ . by using key word indices to extract a list of relevant documents from a document description database. That list is then presented to the user see Fig. 5 ,Ž . who may then select detailed information on a particular document. In Fig. 6, we see that in Frankovic’s article polling methods are discussed for the New York Times<sup>r</sup>CBS polls, the Time–CNN polls, and the Gallup Organization polls. Although our implementation does not currently do this, it would be a simple matter to allow the user to view a particular document at this point.

## 4.3. PNB’s money access center MAC decision ( )

Money Access Center is one of the country’s largest ATM networks and has been dominant in the Philadelphia region, where its owner, Philadelphia National Bank PNB , is located. MAC is by allŽ . accounts a high-quality, profitable system with an excellent business record and good prospects for continuing success. Surprisingly, however, MAC is a shared network—many competing banks participate in it—owned by a single bank PNB , which com-Ž . petes with most of the network’s customers. Further, MAC was launched in the presence of a competing ATM network—Girard Bank’s George—that had high visibility and extensive coverage in the Philadelphia area.

The story of how MAC was conceived, launched and brought to success is a fascinating one, rich in implications for IS and strategy. This story, moreover, has been ably recounted by Clemons 8 . Our<sup>w</sup> <sup>x</sup> purpose here is not to repeat the story, but to extract from it something of the argumentation structure presented to PNB’s decision makers prior to the decision to launch MAC as a shared network. Space limitations confine us to a discussion of the argumentation network, but the HADSS functionality should be apparent.

![](/api/attachments/HP4624KE/fulltext/images/ba71bd4932fa525a1a49d8056bbe246072be70964b1bf81f9bb226b51e157d70.jpg)  
Fig. 6. The HADSS representation of information about a certain document linked to the presidential polls argument.

![](/api/attachments/HP4624KE/fulltext/images/d87c7b160cc542b501243364affb02f821179d10d915e836250dd31b7408b48d.jpg)  
Fig. 7. Stage 1 of the PNB MAC decision: the problem. Because Girard’s George ATM network is successful GGIS , if PNB doesŽ . not get a large ATM network Ž . <sup>!</sup>LATM , then presumably PNB will have a serious loss in its retail banking business SLRBB .Ž .

<sup>w</sup> <sup>x</sup> <sup>14</sup> According to Clemons 8 , strategy formulation by PNB regarding MAC may be reconstructed as a three-stage process. In stage 1, PNB recognized a problem. Girard Bank had successfully launched the George ATM network, and PNB was concerned that its retail customers would move in droves to Girard, unless PNB developed a similarly large ATM Ž . LATM network. The situation is summarized in Fig. 7.

In stage 2 of the policy formulation process, options were identified for consideration. The first thing assumed was that PNB would have a LATM network available to it. In terms of our argumentation network, this is the denial of <sup>!</sup>LATM. Similarly, <sup>!</sup>SLRBB no significant loss of retail bankingŽ business is added as a node, since that is a main. objective of the policy formulation exercise. See Fig. 8.

A critical assumption at stage 2 was that if PNB is to have an LATM, then presumably it would haveŽ . to build its own private network BONET . GivenŽ . this, there would seem to be two main options: build a network with about as many ATM machines as Girard George’s 1TO1 or xor node in Fig. 8 buildŽ . Ž . a much smaller network with about the same ratio of customers to ATM machines as Girard’s George Ž . PCENT . The problem with these options is that neither leads to averting a significant loss of retail banking business Ž . <sup>!</sup>SLRBB , as is clear in Fig. 8. Both options fail to produce an LATM network for PNB, PCENT by design and 1TO1 because it is simply infeasible due to cos t. <sup>15</sup>

![](/api/attachments/HP4624KE/fulltext/images/95b5809bcab09cb3a974e1cf62dce3ecd305d64b7cf9b21d512a72c58006c119.jpg)  
Fig. 8. Stage 2 of the PNB MAC decision. BONET, PNB builds its own ATM network; 1TO1, PNB matches the number of ATMs fielded by Girard’s George; PCENT, PNB fields an ATM network, matching the machines to customer ratio of George.

In terms of sweeping presumptions and the argumentation network in Fig. 8, if we assume that PNB is to have an LATM network, then we are led to conclude that either PPPPSLRBB if 1TO1 is cho-Ž sen or, again, PPPPSLRBB if PCENT is chosen .. Ž . These are horns of an unhappy dilemma, and they in fact correspond to what common sense reports andŽ PNB’s management saw about this situation. Is. there a way out? The diagram is helpful. Consider the assumptions that are being made at stage 2. Clearly, nodes GGIS and LATM are assumed, and clearly they really are not at all controversial in this context. There are other assumptions, however. Each arc represents an assumption. For example, Fig. 8 assumes defeasibly that if BONET, then there areŽ . exactly two options available, PCENT and 1TO1. This is certainly false, but not in any way that matters Argumentation is a form of modeling, too. Ž Like other forms, successful practice requires tasteful and judicious embracing of the false in favor of the feasible..

What Clemons reports personal communicationŽ . is that the LATM–BONET arc was, in effect, recognized by PNB as meaningfully defeasible. The arc is assuming that PNB will have, as Girard did, a single-bank network. Once this conceptual shift was made, it was fairly clear what the options were.

There were two alternatives to reduce cost while meeting PNB’s very demanding requirements for retail service delivery: to reduce cost by shared development of a multiple-owner, consortium ATM network, or to reduce final cost to PNB by developing the type of network PNB desired and aggressively marketing it to other Philadelphia area banks. The second alternative, marketing of services, was seen to have better ‘up-side’ potential. Moreover, the consortium development was seen as impractical at the time: most banks that were able to commit resources were developing or planning to develop proprietary networks, and consortium development appears very difficult to coordinate. No more detailed formal analysis was done, and the decision to launch and market a single-owner network was made in 1978 Ref. 8 , emphasis added .Ž <sup>w</sup> <sup>x</sup> .

This reasoning is modeled in Fig. 9. Given the model, it is clear why MAC wins over CNET, assuming we are using sweeping presumptions. We conclude with sweeping presumptions that Ž . PPP<sup>!</sup>SLRBB with MAC or PPPŽ . <sup>!</sup>SLRBB but undermined with PPPP<sup>!</sup>SLRBB with CNET .Ž . Thus, the weight of the argument favors MAC, and with sweeping presumptions we choose it, as inŽ effect did PNB’s management..

![](/api/attachments/HP4624KE/fulltext/images/22c3fa9c9955a17d6ce665672d989c8a519596ec95afef8a3be534133c61a8a1.jpg)  
Fig. 9. Stage 3 of the PNB MAC decision. MUNET, PNB participates in a multiuser ATM network; MAC, PNB builds the MAC ATM shared network; CNET, PNB promotes a consortium ATM network; CRSK, the consortium network risks coordination¨ difficulties. Note: indicates denial; here, ‘presumably not. <sup>5</sup>

## 5. An experimental study

Argumentation DSSs are aimed at helping people construct, evaluate, and communicate arguments. Do they work? How can they best be designed and what might we expect from them? These are large, important, and difficult questions, questions that only a long stream of yet-to-be-done research can answer. Existing prototypes, including the work reported above, are mostly only prototypes. They are but the beginning of the exploration of an interesting idea. Our purpose in this section is to extend the conceptual<sup>r</sup>prototyping results ours and others by report-Ž . ing on an experiment in which subjects were asked to make logical inferences either with or without aid of the sorts of argument representation-directed graphs-used in argumentation DSSs.

Substantial recent research has shown that people often do not reason in accord with the rules of formal logic. By way of explanation, Johnson-Laird presents a different point of view by introducing a theory, called ‘mental models,’ to describe how people solve deductive problems. Johnson-Laird in Ref.Ž <sup>w</sup> <sup>x</sup> 24 , p. 98 observes that ‘‘ . . . human reasoners ap-. pear to retain a superficial representation of the propositions expressed by the premises—one that is close to their linguistic form—but from the errors they make, they appear to make inferences by manipulating mental models rather than by deploying rules of inference on these superficial representations’’. Johnson-Laird shows that mental models can explain many aspects of human reasoning 24 .<sup>w</sup> <sup>x</sup>

Despite the differences in the descriptions and models for reasoning processes, there is a general consensus that people should follow what the normative theory prescribes for deductive reasoning. One interesting observation is that people are normally willing to make corrections when they realize that they have violated the logical inference rules. It is not our purpose here to review and study the different theories of reasoning. Our focus is on developing tools for supporting people in reasoning processes. As discussed above, many features in argumentation support systems, including graph-based representation of arguments, inference support mechanisms, and information document retrieval techniques, can Ž . support people in reasoning processes. In this section, we present an experiment to demonstrate that people can improve their deductive reasoning by using appropriate supporting tools. Because this is an initial experiment, and because of an extensive related literature, we have focused on deductive ratherŽ than, say, defeasible reasoning. .

## 5.1. Experimental method

In the experiment, the subjects were presented with a set of deductive reasoning problems, and they were asked to derive conclusions from a set of given statements. The statements are conditional English sentences, which are similar to those Johnson-Laird and Byrne used in their experimental studies seeŽ Refs. 24,25 . Previous studies by Johnson-Laird,<sup>w</sup> <sup>x</sup>. Ž Byrne and others have shown that people make . systematic errors when they solve similar problems based on their intuitive judgments. In our experiment, we provide one group of subjects with a special tool, called the logic graph method 13,29 .<sup>w</sup> <sup>x</sup> As we discussed above, the logic graph method plays an important role in our logical framework. We developed the theory of argumentation support systems, as well as our prototype system, based on the ideas of the logic graph method and its extension, the method of sweeping presumptions. This experiment is designed to assess the usefulness of the logic graph method in deductive reasoning.

## 5.2. Subjects and procedures

The subjects were 57 University of Pennsylvania undergraduate students. None of the subjects had previously received any formal training in logic. Subjects were assigned randomly to two groups of approximately equal size: a control group group Ž Ž . . Ž Ž . A , N <sup>s</sup> 28 and an experimental group group B , N<sup>s</sup>29 . The subjects in both groups were presented . a set of problems. Each problem consisted of a set of English statements with a list of possible conclusions. The subjects were asked to choose the correct conclusion s for each set of given statements. Fur-Ž . ther, in addition to the problem statements in English, the subjects in group B were presented with aŽ . logic graph representation of the problem, which they could use to help them in reasoning. Prior to the experiment, the subjects in each group were given 10 min to read training materials. To encourage the subjects to try their best to solve the problems, we offered a payment of US\$3.00 for each correct answer, for two randomly chosen subjects.

## 5.3. Training materials

## 5.3.1. Control group group A ( )

The training material for group A consisted ofŽ . examples and non-technical explanations on how to draw a conclusion from given statements. The following is a part of the training material. The complete training material is presented in Ref. 23 .<sup>w</sup> <sup>x</sup>

## Example:

Statement 1: If there is a circle then there is a triangle.

Statement 2: If there is a triangle then there is a square.

Statement 3: There is a circle.

Circle all the correct conclusions.

Ž .a There is not a circle.

Ž . b There is not a square.

Ž .c There is a triangle.

Ž . d There is not a triangle.

Ž .e None of the above is correct.

Ž Ž .. Conclusion: c

Statement 1 is a conditional statement, in which, ‘there is a circle’ is the precondition, and ‘there is a triangle’ is the conclusion. Similarly, statement 2 is also a conditional statement, in which, ‘there is a triangle’ is the precondition, and ‘there is a square is the conclusion. In general, when the precondition of a statement is satisfied, its conclusion must follow. Therefore, when making inferences with conditional statements, we always check their preconditions first. As in this example, the given fact, ‘there is a circle’ statement 3 , satisfies the precondition ofŽ . statement 1. We can draw the conclusion c ‘there isŽ . a triangle’. Further, since this conclusion, ‘there is a triangle’, satisfies the precondition of statement 2, we can draw another conclusion ‘there is a square Ž .which is not in the list of the choices .

## 5.3.2. Experimental group group B ( )

Similarly, subjects in group B read training ma-Ž . terial consisting of examples, the logic graph representation of conditional statements, and non-technical explanations on how to draw a conclusion from the given statements with the logic graph method. The following is a part of the training material. The complete training material is presented in Ref. 23 .

The logic graph method is a tool for representing statements and supporting users in making inferences. The representations of logical statements in the logic graph method are rather simple. We illustrate the logic graph method with three examples. Please read these examples very carefully.

## Example:

Statement 1: If there is a circle then there is a triangle.

Statement 2: If there is a triangle then there is a square.

Statement 3: There is a circle.

Circle all the correct conclusions.

Ž .a There is not a circle.

Ž . b There is not a square.

Ž .c There is a triangle.

Ž . d There is not a triangle.

Ž .e None of the above is correct.

Ž Ž .. Conclusion: c

Fig. 10 illustrates how to use the logic graph method to represent and solve the problem in the example. Step 1 depicts the logic graph representation of statement 1 and statement 2. The node with label ‘C’ represents ‘there is a circle’, and the node with label ‘T’ represents the statement ‘there is a triangle’. The ‘if–then’ relationship between ‘C’ and ‘T’ is represented by the arrow from node ‘C’ to node ‘T’. a in step 1 depicts the representation ofŽ . statement 1—‘if there is a circle then there is a triangle’. Every conditional statement has a contrapositive equivalent statement. The contrapositive equivalent statement is just a different way to state the original statement. Sometimes, we find this equivalent statement is convenient to use in making inferences. The contrapositive equivalent statement of statement 1 is ‘if there is not a triangle then there

(a)

(b)

(bb)

(bb)

Step 1:

![](/api/attachments/HP4624KE/fulltext/images/b891c2becf6dee109d69e3fb4ee1cdd67dc9a0ae00a6a4fa30868170aaa04b29.jpg)  
Fig. 10. Example in the training material presented to the experimental group.

is not a circle’, and it can also be easily represented in logic graph. aa in step 1 depicts the logic graph Ž . representation of this statement. The node $\mathbf { \epsilon } \cdot \mathbf { \lambda } \mathbf { T } ^ { \prime }$ represents ‘there is not a triangle’, and the node $\mathbf { \dot { \Psi } } _ { \neg \mathbf { C } } ,$ represents ‘there is not a circle’. The symbol $"  "$ represents the meaning of ‘not’. Similarly, bŽ . in step 1 depicts the representation of statement 2—‘If there is a triangle ‘T’ then there is a squareŽ . Ž . Ž . ‘S’ ’, and bb depicts its equivalent statement—‘if there is not a square ‘Ž . <sup>!</sup>S’ then there is not a triangle ‘Ž . Ž . <sup>!</sup>T’ ’. c in step 1 depicts the representation of statement 3—‘there is a circle’. We shade node ‘C’ to indicate that ‘C’ is a given fact.

Step 2 illustrates how to make inferences with the logic graph method. We first shade all nodes labeled with $\mathbf { \epsilon } ^ { 6 } \mathbf { C } '$ in the graph. Then we shade all the nodes reachable from node ‘C’ by traversing the arrows . Ž . Thus, node $\mathbf { \hat { \Omega } } ^ { \ast } \mathbf { T } ^ { \ast }$ is shaded. This operation of travers-Ž ing the arrows represents the action of making an. inference based on the statements ‘if ‘C’ then ‘T’’ and $\mathbf { \ddot { C } } _ { }$ . We will continue the process of shading all reachable nodes by traversing the arrows until we can’t go any further. In this example, we can reach node $\mathbf { \epsilon } ^ { \prime } S ^ { \prime }$ from node ‘T’ by traversing arrows. Therefore, ‘S’ is shaded Step 3 . Since we can’t go anyŽ . further from node ‘S’, we stop at this step. The conclusions that we can draw are represented by all of the shaded nodes Step 4 .Ž .

Then, we can check the list of the choices and circle the correct conclusions. Since we have node ‘T’ shaded in example 1, we choose the conclusion Ž . Ž c ‘there is a triangle’ Node ‘S’, which represents ‘there is a square’, is also shaded; but, it is not in the list ..

## 5.4. Test problems

The test problem booklet consisted of 15 problems. Each problem contained three conditional statements and one simple statement. In addition, the subjects in the experimental group were provided with a logic graph representation of the statements. The task for the subjects was to evaluate the given statements and choose all of the correct conclusions that deductively followed from the given statements.

The conditional statements in the problems are given in either ‘if–then’ form or ‘only–if’ form. The following is a standard ‘if–then’ statement.

If John is a lawyer, then Bill is not a doctor.

In this statement, ‘John is a lawyer’ is the precondition, and ‘Bill is not a doctor’ is the conclusion. According to the rules of logic, if the precondition of a statement is satisfied, its conclusion must follow. For instance, if we have ‘John is a lawyer’ as a fact, we must conclude ‘Bill is not a doctor.’ This type of deductive reasoning is formally called modus ponens in logic.

Every conditional statement has a contrapositive equivalent statement, which is just a different way to state the original statement. For instance, the above statement, ‘if John is a lawyer, then Bill is not a doctor’ is equivalent to ‘if Bill is a doctor, then John is not a lawyer.’ Therefore, if we have ‘Bill is a doctor’ as a fact, we must conclude ‘John is not a lawyer’. This type of deductive reasoning is called modus tollens in logic.

Johnson-Laird and Byrne have shown in their experiments that reasoning with modus tollens is more difficult than the reasoning with modus ponens

Table 1 Test problem design

<table><tr><td>Problem ID</td><td>Problem type</td></tr><tr><td>#301</td><td>Three modus ponens statements</td></tr><tr><td>#302</td><td>Three modus ponens statements</td></tr><tr><td>#303</td><td>Two modus ponens and one modus tollens statements</td></tr><tr><td>#304</td><td>Two modus ponens and one modus tollens statements</td></tr><tr><td>#305</td><td>Two modus ponens and one modus tollens statements</td></tr><tr><td>#306</td><td>One modus ponens and two modus tollens statements</td></tr><tr><td>#307</td><td>One modus ponens and two modus tollens statements</td></tr><tr><td>#308</td><td>One modus ponens and two modus tollens statements</td></tr><tr><td>#309</td><td>Three modus tollens statements</td></tr><tr><td>#310</td><td>Three modus tollens statements</td></tr><tr><td>#311</td><td>One modus ponens and two modus tollens (with one ‘only-if’) statements</td></tr><tr><td>#312</td><td>One modus ponens and two modus tollens (with one ‘only-if’) statements</td></tr><tr><td>#313</td><td>One modus ponens and two modus tollens (with one ‘only-if’) statements</td></tr><tr><td>#314</td><td>One modus ponens and two modus tollens (with one ‘only-if’) statements</td></tr><tr><td>#315</td><td>Three modus tollens (with two ‘only-if’) statements</td></tr></table>

Žsee Ref. 25 , p. 55 . According to the mental model<sup>w</sup> <sup>x</sup> . theory, people do not follow the logical rules in their deductive reasoning processes, but rather represent conditional statements as mental models. Because reasoning with modus tollens involves more complicated manipulation of mental models than reasoning with modus ponens, people tend to make more mistakes in the former type of reasoning.

A conditional statement can also be in an ‘only–if form. For instance, the statement, ‘John is a lawyer only if Bill is not a doctor’, is equivalent to ‘if Bill is a doctor, then John is not a lawyer’, or ‘if John is a lawyer, then Bill is not a doctor’. Although it is easy to transform an ‘only–if’ statement into an ‘if–then statement, Johnson-Laird has shown that people tend to make more mistakes with ‘only–if’ statements than with ‘if–then’ statements when they make inferences. Johnson-Laird also provides an explanation of this in terms of his mental model theory.

Our purpose in this experiment was to investigate the effectiveness of the logic graph method in various types of problems. We designed the test problem with different levels of difficulty by combining the modus ponens inferences and modus tollens inferences, as well as, ‘if–then’ statements and ‘only–if statements. Our design of the test problem is slightly different from Johnson-Laird’s approach. In Johnson-Laird’s experiments, the test problems were given as a single conditional statement, then subjects were asked to derive any conclusions that follow the statement. In our experiment, the test problems contain three conditional statements, and the answers were presented in multiple choice format. In general, our test problems are more difficult than Johnson-Laird’s. Although our experimental results generally agree with what the mental model theory predicted, we found some differences. We believe that these differences are caused by different forms of solutions given in the multiple choice. We will analyze the experimental results below. In our experiment, the order of the test problems in the test booklet was randomly assigned for each subject. Table 1 lists the test problems by type. The complete set of test problems is in Ref. 23 .<sup>w</sup> <sup>x</sup>

## 5.5. Results and discussion

Table 2 presents the percentage of subjects who made at least one error for each problem. <sup>16</sup> As shown in Table 2, the subjects in the experimental group group B generally performed better than theŽ . subjects in the control group group A . The subjectsŽ . in group B made fewer errors than the subjects in group A did on 13 test problems out of the total 15 test problems. Among those 13 problems, the subjects in group B significantly outperformed the subjects in group A on nine test problems $( p < 0 . 0 5 )$ . In the other two test problems, the subjects in both groups had the same performance in one case idŽ a301, the subjects in both groups made the equal number of errors on one problem , and the subjects . in group A performed slightly better than the subjects in group B did in the other case idŽ . a311 .

The test problems were designed to be at different levels of difficulty. We observed that the subjects in both groups performed quite differently across the test problems. For example, in the control group, only 4% of the subjects made at least one error on problem a301, and 82% of the subjects made at least one error on problem a304. This difference is

Percentage of the subjects who made at least one error for each test problem and Z-test comparison between the control group and the experimental group

<table><tr><td>Problem ID</td><td>Percentage of errors in control group (A)</td><td>Percentage of errors in experimental group (B)</td><td>Z-test</td></tr><tr><td>#301</td><td>4±7</td><td>4±7</td><td>Z=0, p=0.5</td></tr><tr><td>#302</td><td>19±15</td><td>15±13</td><td>Z=0.365, p=0.358</td></tr><tr><td>#303</td><td>22±16</td><td>19±15</td><td>Z=0.338, p=0.368</td></tr><tr><td>#304</td><td>82±15</td><td>30±17</td><td>Z=3.834, p&lt;0.001</td></tr><tr><td>#305</td><td>19±15</td><td>4±7</td><td>Z=1.732, p&lt;0.05</td></tr><tr><td>#306</td><td>70±17</td><td>26±17</td><td>Z=3.628, p&lt;0.001</td></tr><tr><td>#307</td><td>11±12</td><td>0±0</td><td>Z=1.728, p&lt;0.05</td></tr><tr><td>#308</td><td>7±10</td><td>4±7</td><td>Z=0.594, p=0.276</td></tr><tr><td>#309</td><td>19±15</td><td>11±12</td><td>Z=0.766, p=0.222</td></tr><tr><td>#310</td><td>78±16</td><td>30±17</td><td>Z=3.548, p&lt;0.001</td></tr><tr><td>#311</td><td>11±12</td><td>15±13</td><td>Z=-0.41, p=0.675</td></tr><tr><td>#312</td><td>40±19</td><td>4±7</td><td>Z=3.273, p&lt;0.001</td></tr><tr><td>#313</td><td>37±18</td><td>7±10</td><td>Z=2.619, p&lt;0.001</td></tr><tr><td>#314</td><td>70±17</td><td>26±17</td><td>Z=3.628, p&lt;0.001</td></tr><tr><td>#315</td><td>26±17</td><td>7±10</td><td>Z=1.826, p&lt;0.05</td></tr></table>

The numbers of percentage errors in the table are the means of percentage errors in each type of the problems in the corresponding groups. Error margins indicated in the table are half-widths of 95% confidence intervals for the respective conditions.

![](/api/attachments/HP4624KE/fulltext/images/b40d4ec38150e15d961d1632a983c47c444801652767d29219bd3ed5321713bd.jpg)  
Fig. 11. The performance comparison of the control and experimental groups across the test problems.

Ž quite significant Z <sup>s</sup> 5.78, $p < 1 \times 1 0 ^ { - 8 } )$ . In general, the difference reflects the level of difficulty in the test problems in terms of the two types of reasoning processes modus ponens and modus tol-Ž lens and two types of conditional statements ‘if–. Ž then’ and ‘only–if’ . Johnson-Laird has shown that, . in $\cdot _ { \mathrm { i f - t h e n } } ,$ conditional statements, people make more mistakes with modus tollens than with modus ponens. He has also shown that, in the ‘only–if conditional statements, there is no significant difference between modus ponens and modus tollens types of reasoning. But people are more likely to have problems with ‘only–if’ statements than ‘if–then’ statements 25 . Generally, our experimental results <sup>w</sup> <sup>x</sup> are consistent with those of Johnson-Laird.

Fig. 11 illustrates the performance comparison of the control and experimental groups across the test problems. Each point in the figure corresponds to a test problem with the percentages of errors made by the subjects in the control group horizontal axisŽ . Ž . <sup>17</sup> and the experimental group vertical axis . Since almost all the corresponding points in Fig. 11 fall below the diagonal line, it concisely shows that the subjects in the experimental group performed better than the subjects in the control group. The trend of improvement in the experimental group is shown by a simple linear regression. On the easy problems the Ž percentage of errors is less than 25% in the control group , the effectiveness of the logic graph method is. not apparent. As the problem difficulty level increases, the improvement becomes more and more manifest. The overall performance analysis was done with a Kruskal–Wallis test. The test results Ž H <sup>s</sup> 5.395, $\alpha < 0 . 0 5 )$ demonstrate than the subjects in the experimental group performed significantly better than the subjects in the control group. See Ref. 23<sup>w</sup> <sup>x</sup> for a detailed discussion of the findings.

In summary, our experimental results indicate that the logic graph representation method is a useful tool for helping people in deductive reasoning. Through the graphical representation of conditional statements, deductive reasoning processes are simplified as graph traversal. This procedure is easily understood and followed. In theory, no matter what forms Ž . ‘if–then’ or ‘only–if’ of conditional statements are given, no matter what types of reasoning processes Ž .modus ponens or modus tollens are required, people only need to follow one simple rule to manipulate the graph to reach correct conclusions. However, in our experiment the subjects still performed differently across the test problems. Our explanation is that people have a tendency to rely on their mental models in their reasoning processes. By examining the test booklets of the experimental group, we found that a large number of mistakes were made because the subjects didn’t complete ‘coloring’ the graph before making their choices, especially when the conclusion appeared to be obvious. In these cases, they just chose the ‘correct’ conclusions based on their mental models. This explains our observation that the pattern of the error rates in the experimental group B is similar to that of the control group A . Ž . Ž . In fact, when people understand and follow the logic graph method in deductive reasoning, they have little chance to make mistakes. In the experimental group Ž . B , 37% of the subjects made 0 errors, and 56% of the subjects made one error or less. In the control group A , however, no subjects made one error orŽ . less, only 13% of the subjects made two errors, and 87% of subjects made three or more errors. Although our experiment has been limited on testing deductive reasoning based on conditional statements, we believe our conclusion can be generalized—that is, with appropriate supporting tools, people can significantly improve their ability in reasoning.

## 6. Conclusion

This has been an exploratory exercise. The concept of an argumentation DSS, particularly one with hypermedia elements, is of recent vintage. Neither the requirements nor the operating characteristics of such systems are well understood. Our implementation is very much a prototype. The inferences it makes are elementary and in many ways naıve e.g., ¨ Ž in realistic systems it would not be reasonable to present all known documents that mention presidential polling . Still, the prototype makes inferences . and supports hypertext. If, as we have demonstrated, relevant textual documents can be found and displayed using node-specific contextual information, then so can documents in media other than text. There is no reason to think that the principles and the architecture will not generalize, once appropriate indexing schemes and bridge laws 5 are developed<sup>w</sup> <sup>x</sup> for multimedia documents. Finally, our experiment indicates much promise for finding technology that effectively supports reasoning and argumentation of a logical sort. But it is only one experiment and is limited to deductive inference. Very much remains to be investigated with respect to these systems.

A problem that exercises us a great deal is whether very many people will find it useful or attractive to work with an argumentation system, regardless of how friendly and clear it is. We suspect that philosophers and lawyers, who work professionally with arguments, are promising users, but there are serious questions whether many others can be induced to acquire the habits of mind required to reason carefully with arguments. Who, however, would have predicted 30 years ago the widespread, personal, interactive use of computer software? There is reason to hope that, with the accumulation of experimental knowledge, we may yet learn how usefully to bring hypermedia argumentation DSSs to a broad audience.

## References

<sup>w</sup> <sup>x</sup> 1 K.D. Ashley, Modeling Legal Argument: Reasoning with Cases and Hypotheticals, The MIT Press, Cambridge, MA, 1990.

2 J. Baron, Review of the Skills of Argument by Deanna Kuhn, Informal Logic XIV 1 1992 59–67.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 E. Berk, J. Devlin Eds. , Hypertext Ž . <sup>r</sup>Hypermedia Handbook, McGraw-Hill, New York, NY, 1991.

<sup>w</sup> <sup>x</sup> 4 M. Bieber, Automating hypermedia for decision support, forthcoming in Hypermedia.

<sup>w</sup> <sup>x</sup> 5 M.P. Bieber, S.O. Kimbrough, On the concept of generalized hypertext, MIS Q. 16 1 1992 77–93.Ž . Ž .

6 M.P. Bieber, S.O. Kimbrough, On the logic of generalized hypertext, forthcoming in Decision Support Syst.

<sup>w</sup> <sup>x</sup> 7 R.L. Causey, EVID: a system for interactive defeasible reasoning, forthcoming in Decision Support Syst., 1993.

<sup>w</sup> <sup>x</sup> 8 E.K. Clemons, MAC—Philadelphia National Bank’s strategic venture in shared ATM networks, J. Manage. Inform. Syst. 7 1 1990 5–25.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 J. Conklin, Hypertext: an introduction and survey, Computer, September 1987, pp. 17–41.

<sup>w</sup> <sup>x</sup> 10 J. Conklin, M.L. Begeman, gIBIS: a hypertext tool for exploratory policy discussion, Proceedings of the Conference on Computer-Supported Cooperative Work, Sept. 1988, pp. 140–152.

<sup>w</sup> <sup>x</sup> 11 J. Conklin, M.L. Begeman, gIBIS: a tool for all reasons, J. Am. Soc. Inf. Sci. 40 3 1989 200–213.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 F.W. Dauer, Critical Thinking: An Introduction to Reasoning, Oxford Univ. Press, New York, NY, 1989.

<sup>w</sup> <sup>x</sup> 13 J.R. Elliott, S.O. Kimbrough, A graph-based theorem prover for sentence logic model management, University of Pennsylvania, Department of Decision Sciences, working paper 90-01-01, 1990.

<sup>w</sup> <sup>x</sup> 14 E.R. Emmet, Learning to Think, Taplinger Publishing, New York, NY, 1980.

15 A. Fisher, The Logic of Real Arguments, Cambridge Univ. Press, Cambridge, 1988.

<sup>w</sup> <sup>x</sup> 16 K.A. Frankovic, Reading Between the Polls, The New York Times, June 27, 1992.

<sup>w</sup> <sup>x</sup> 17 D. Gabbay, C. Hogger Eds. , Handbook of Logic for Artifi-Ž . cial Intelligence and Logic Programming, Vol. III, Oxford Univ. Press, Oxford, England, 1993.

<sup>w</sup> <sup>x</sup> 18 K.M. Gallotti, Approaches to studying formal and everyday reasoning, Psychol. Bull. 105 1989 331–351.Ž .

<sup>w</sup> <sup>x</sup> 19 M.R. Genesereth, N.J. Nilsson, Logical Foundations of Artificial Intelligence, Morgan Kaufmann Publishers, Palo Alto, CA, 1987.

<sup>w</sup> <sup>x</sup> 20 M.L. Ginsberg Ed. , Readings in Nonmonotonic Reasoning,Ž . Morgan Kaufmann Publishers, Los Altos, CA, 1987.

<sup>w</sup> <sup>x</sup> 21 F.G. Halasz, Reflections on note cards: seven issues for the next generation of hypermedia systems, CACM 31 7 1988Ž . Ž . 836–855.

<sup>w</sup> <sup>x</sup> 22 S.H. Hashim, Exploring Hypertext Programming: Writing Knowledge Representation and Problem-Solving Programs, Windcrest Books, TAB BOOKS, Blue Ridge Summit, PA, 1990.

<sup>w</sup> <sup>x</sup> 23 H. Hua, Theory and applications of argumentation support systems, PhD thesis, University of Pennsylvania, Philadelphia, 1995.

<sup>w</sup> <sup>x</sup> 24 P.N. Johnson-Laird, Mental Models: Towards a Cognitive

Science of Language, Inference, and Consciousness, Harvard Univ. Press, Cambridge, MA, 1983.

<sup>w</sup> <sup>x</sup> 25 P.N. Johnson-Laird, R.M.J. Byrne, Deduction, Lawrence Brlbaum Associates, Publishers, Hillsdale, USA, 1991.

<sup>w</sup> <sup>x</sup> 26 H. Kahane, Logic and Contemporary Rhetoric: The Use of Reason in Everyday Life, 5th edn., Wadsworth Publishing, Belmont, CA, 1988.

<sup>w</sup> <sup>x</sup> 27 D. Kahneman, P. Slovic, A. Tversky Eds. , Judgment UnderŽ . Uncertainty: Heuristics and Biases, Cambridge Univ. Press, Cambridge, England, 1982.

<sup>w</sup> <sup>x</sup> 28 D. Kelley, The Art of Reasoning, W.W. Norton & Company, New York, NY, 1988.

<sup>w</sup> <sup>x</sup> 29 S.O. Kimbrough, A graph representation for management of logic models, Decision Support Syst. 2 1986 27–37.Ž .

<sup>w</sup> <sup>x</sup> 30 S.O. Kimbrough, The argumentation theory of decision support systems, University of Pennsylvania, Decision Sciences Department working paper 87-12-07, 1987.

<sup>w</sup> <sup>x</sup> 31 S.O. Kimbrough, Notes on the argumentation theory for decision support systems, Proceedings of the 1990 International Society on DSS Conference, Austin, TX, September 1990, pp. 17–39.

<sup>w</sup> <sup>x</sup> 32 S.O. Kimbrough, An introduction to the method of sweeping presumptions for modeling nonmonotonic reasoning, in: J.F. Nunamaker Jr. Ed. , Proceedings of the 24th Annual HawaiiŽ . International Conference on System Sciences, Vol. III, DSS and Knowledge-Based Systems and Collaboration Technology Tracks, IEEE Computer Society Press, Los Alamitos, CA, 1991, pp. 339–348.

<sup>w</sup> <sup>x</sup> 33 S.O. Kimbrough, F. Adams, Why nonmonotonic logic?, Decision Support Syst. 4 1988 111–127. Ž .

<sup>w</sup> <sup>x</sup> 34 S.O. Kimbrough, H. Hua, On modeling nonmonotonic reasoning with the method of sweeping presumptions, Minds and Machines 1 4 1991 393–416.Ž . Ž .

<sup>w</sup> <sup>x</sup> 35 S.O. Kimbrough, S.A. Moore, On obligation, time, and defeasibility in systems for electronic commerce, in: J.F. Nunamaker Jr., R.H. Sprague Jr. Eds. , Proceedings of theŽ . 26th Annual Hawaii International Conference on System Sciences, Vol. III, Information Systems: DSS<sup>r</sup>Knowledge-Based Systems, IEEE Computer Society Press, Los Alamitos, CA, January 1993, pp. 493–502.

<sup>w</sup> <sup>x</sup> 36 S.O. Kimbrough, C.W. Pritchett, M.P. Bieber, H.K. Bhargava, The coast guard’s KSS project, Interfaces 20 6 1990Ž . Ž . 5–16.

<sup>w</sup> <sup>x</sup> 37 D. Kuhn, The Skills of Argument, Cambridge Univ. Press, Cambridge, England, 1991.

<sup>w</sup> <sup>x</sup> 38 H. Kyburg, R. Loui, G. Carlson Eds. , Knowledge Repre-Ž . sentation and Defeasible Reasoning, Kluwer Academic Publishers, Boston, MA, 1990.

<sup>w</sup> <sup>x</sup> 39 J. Lee, Sibyl: a qualitative decision management system, in: P. Winston Ed. , Artificial Intelligence at MIT: ExpandingŽ . Frontiers, 1, The MIT Press, Cambridge, MA, forthcoming.

<sup>w</sup> <sup>x</sup> 40 J. Lee, T.W. Malone, Partially shared views: a scheme for communicating among groups that use different type hierarchies, MIT Sloan School working paper, SSM WP a2052-88, March 1988.

<sup>w</sup> <sup>x</sup> 41 J. Lee, T.W. Malone, How can groups communicate when

they use different languages? Translating between partially shared type hierarchies, MIT Sloan School working paper, SSM WP a3076-89-MS, Sept. 1989.

<sup>w</sup> <sup>x</sup> 42 D.G. Lowe, Co-operative structuring of information: the representation of reasoning and debate, Int. J. Man–Machine Stud. 23 1985 97–111.Ž .

<sup>w</sup> <sup>x</sup> 43 D.G. Lowe, SYNVIEW: the design of a system for cooperative structuring of information, Computer-Supported Cooperative Work CSCW ’86 Proceedings, Austin, TX, DecemberŽ . 3–5, 1986.

<sup>w</sup> <sup>x</sup> 44 C.C. Marshall, F.G. Halasz, R.A. Rogers, W.C. Janssen Jr., Aquanet: a hypertext tool to hold your knowledge in place, Proceedings of Hypertext 1991, San Antonio, TX, 1991, pp. 261–276.

<sup>w</sup> <sup>x</sup> 45 D. McDermott, J. Doyle, Nonmonotonic logic I, Artif. Intell. 13 1980 41–72.Ž .

<sup>w</sup> <sup>x</sup> 46 D. Nute, Defeasible reasoning and decision support systems, Decision Support Syst. 4 1988 97–110.Ž .

<sup>w</sup> <sup>x</sup> 47 D. Nute, Review of readings in nonmonotonic reasoning, Philos. Psychol. 2 1989 351–355.Ž .

<sup>w</sup> <sup>x</sup> 48 D. Nute, K. Erk, Defeasible logic graphs: I. Theory, Decision Support Syst., this issue.

<sup>w</sup> <sup>x</sup> 49 D. Nute, Z. Hunter, C. Henderson, Defeasible logic graphs: II. Implementation, Decision Support Syst., this issue.

<sup>w</sup> <sup>x</sup> 50 R.C. Pinto, J.A. Blair, Reasoning: A Practical Guide, Prentice-Hall, Englewood Cliffs, NJ, 1993.

<sup>w</sup> <sup>x</sup> 51 J. Pollock, Self-defeating arguments, Minds and Machines 1 Ž . Ž .4 1991 367–392.

<sup>w</sup> <sup>x</sup> 52 M. Reinfrank, J. de Kleer, M.L. Ginsberg, E. Sandewell Ž . Eds. , Non-Monotonic Reasoning, Springer, Berlin, 1989.

<sup>w</sup> <sup>x</sup> 53 R. Reiter, A logic for default reasoning, Artif. Intell. 13 Ž . 1980 81–132.

<sup>w</sup> <sup>x</sup> 54 R.D. Rieke, M.O. Sillars, Argumentation and the Decision Making Process, 2nd edn., Scott, Foresman, Glenview, IL, 1984.

<sup>w</sup> <sup>x</sup> 55 G. Shafer, J. Pearl Eds. , Readings in Uncertain Reasoning,Ž . Morgan Kaufmann Publishers, San Mateo, CA, 1990.

<sup>w</sup> <sup>x</sup> 56 P. Smolensky, B. Bell, B. Fox, R. King, C. Lewis, Constraint-Based Hypertext for Argumentation, Hypertext ’87, Ž . November 13–15, 1987 , pp. 215–246.

<sup>w</sup> <sup>x</sup> 57 R.M. Stein, Browsing through Terabytes–Wais opens a new frontier in personal and corporate information services, Byte 16 5 1991 157–164.Ž . Ž .

<sup>w</sup> <sup>x</sup> 58 P.A. Strassmann, P. Berger, E.B. Swanson, C.H. Kriebel, R.J. Kauffman Eds. , Measuring Business Value of Informa-Ž . tion Technologies, ICIT Press, International Center for Information Technologies, Washington, DC, 1988.

<sup>w</sup> <sup>x</sup> 59 S.E. Toulmin, The Uses of Argument, Cambridge Univ. Press, London, 1958.

<sup>w</sup> <sup>x</sup> 60 S. Toulmin, R. Rieke, A. Janik, An Introduction to Reasoning, 2nd edn., Macmillan, New York, 1984.

<sup>w</sup> <sup>x</sup> 61 A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185 1974 1124–1131.Ž .

<sup>w</sup> <sup>x</sup> 62 A. Tversky, D. Kahneman, The framing of decisions and the psychology of choice, Science 211 1981 453–458.Ž .

<sup>w</sup> <sup>x</sup> 63 D.N. Walton, Informal Logic: A Handbook for Critical Argumentation, Cambridge Univ. Press, Cambridge, England, 1989.

<sup>w</sup> <sup>x</sup> 64 D.N. Walton, The Place of Emotion in Argument, The Pennsylvania State Univ. Press, State Park, PA, 1992.

<sup>w</sup> <sup>x</sup> 65 D.N. Walton, Plausible Argument in Everyday Conversation, State University of New York Press, State University Plaza, Albany, NY, 1992.

<sup>w</sup> <sup>x</sup> 66 A. Weston, A Rulebook for Arguments, Hackett Publishing, 1987.

![](/api/attachments/HP4624KE/fulltext/images/ae5cdf672314f9692d2fb44f17f745b65ca604216d87ce4d57c80ab3f5634260.jpg)  
Gary H. Hua is a senior architect at Reed Technology and Information Services. He holds a PhD in management information systems from the Wharton School, University of Pennsylvania. Prior to joining Reed Technology, Dr. Hua was Principal Software Engineer at Unisys and an Assistant Professor in Information Systems at the New Jersey Institute of Technology. Currently, he is working in the areas of internet and intranet technology and electronic commerce.

![](/api/attachments/HP4624KE/fulltext/images/280d73edc779a5521d5af4316cf1ed713dbb40298709df885350856bcc8192ee.jpg)

Steven O. Kimbrough is Professor in the Wharton School, University of Pennsylvania. He holds a PhD in philosophy from the University of Wisconsin at Madison. His teaching and research interests include decision support systems, logic modeling, electronic commerce, and computational theory of rationality.
