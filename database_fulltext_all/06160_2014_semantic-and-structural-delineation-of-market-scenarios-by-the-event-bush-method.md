---
otero_id: 6160
otero_key: "ZTA92XMK"
title: "Semantic and structural delineation of market scenarios by the event bush method"
authors: "Dmitry Mouromtsev; Cyril Pshenichny; Anthony Yakovlev"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.07.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Semantic and structural delineation of market scenarios by the event bush method

Dmitry Mouromtsev, Cyril Pshenichny ⁎, Anthony Yakovlev

Intellectual Systems Laboratory, National Research University of Information Technologies, Mechanics and Optics, Kronverksky Prospect, 49, St. Petersburg 197101, Russia

## a r t i c l e i n f o

Article history: Received 7 May 2012 Received in revised form 25 July 2013 Accepted 25 July 2013 Available online 8 August 2013

Keywords: Event bush method Scenario Consulting Market Knowledge engineering Expert

## a b s t r a c t

Considered is the retrospective application of a new method of knowledge engineering, the event bush, to a real collision that took place in the North-American market of cool sparkling drinks in the 1980s. The paper brie<sup>fl</sup>y introduces the modeled task, provides an outline of the method, presents the results of modeling and discusses them, stressing new opportunities for market analysis and directions of further work. The results of modeling provide ground to reasonably expect improvement of consulting and advising services with application of the event bush method.

© 2013 Elsevier B.V. All rights reserved

## 1. Introduction

To analyze and forecast the market, one needs to compare various scenarios of market development and behavior of players. In doing this, a question repeatedly posed by any analyst to him/herself is, how much the observed scenario or state of things resemble the known cases. Up to now, this question is being answered mostly intuitively, and following application of statistical computation, neural networks [1] or other mathematical modeling and decision support methods (see, e.g., [2]) has been based on intuitively felt similarity or difference. Successful attempts of more or less strict description of semantics of marketing are performed by means of ontology design [5,9], but ontologies describe classes, their properties and relations, which refer rather to a “<sup>fi</sup>xed state” of market than to an a-developing environment, i.e., present rather “anatomy” than “physiology” of the context. Trying to cope with this shortcoming, the so-called dynamic ontologies [7], process ontologies (see, for instance, UN/CEFACT's Modeling Methodology — UMM, in [4]) and others were suggested. However, process ontologies simply take processes for another kind of “<sup>fi</sup>xed” entities and do not display actual scenarios that take, or may take, place, and dynamic ontologies just postulate the fact that changes of given objects may occur in given time but do not specify what in particular can happen and in what way. The same can be generally referred to another well-known business and technical process modeling tool, the Integrated De<sup>fi</sup>nition (IDEF) 0 notation [6]. Nonetheless, this method, being an extension of Structured Analysis and Design Technique (SADT; see, for instance, [17]), makes one step further and shows particular scenarios and, in the SADT framework, their hierarchical relationships. Still, in doing so, this method, and also some others, e.g., event-based process chains (EPC; [19]), specify only a limited set of scenarios that the mind of the expert suggests. Therefore, in our opinion, these methods are better suitable for analysis of more or less simple business processes or production operations than multiplayer market environments. Besides, they put little or no explicit semantic control on generation of events or require additional features to do this (the presence of decomposed block in SADT or an associated ontology in EPC).

Business Process Modeling Notation (BPMN; [3]) offers much more opportunities for semantic control (like “swim lanes” or inheritance of subjects and predicates from parent to child nodes); however, these opportunities do not take form of strict rules and therefore are insuf<sup>fi</sup>ciently used to formally model the scenarios that the expert has not put forth (e.g., scenarios of possible failures or unexpected success).

Thus, the question remains open, if there is a way to put at least somewhat strict and formal constraints on the market scenarios enabling us to construct (that is, to foresee), extract and compare them in a more or less delimited context.

Obviously, a method is needed that would be semantically as strict as ontology but, unlike the latter, would offer an opportunity to track the changes of objects, their properties and relations. Such method was proposed in the <sup>fi</sup>eld of geosciences by Pshenichny and Khrabrykh [15] and Pshenichny et al. [12,14,16] and recently developed by Pshenichny and Kanzheleva [13]. As stated in the quoted publications, it evolved from a purely applied geoscienti<sup>fi</sup>c tool to a universal method of knowledge engineering applicable in a variety of <sup>fi</sup>elds. Then, it looks straightforward to study the applicability of the event bush method to semantically and structurally delineate the scenarios of market player behavior and expected results. This constitutes the purpose of the present paper; to achieve it, below we will (i) consider a simple and well-known marketing task, (ii) give an outline of the method of event bush, (iii) consider its application to the described task and (iv) discuss the results. In any case, these results should be considered highly preliminary and neither proving nor refuting the applicability of the said method in the marketing <sup>fi</sup>eld; nevertheless, they must shed light on whether the chosen approach to formalization of market scenarios is encouraging and, if yes, what should be done to proceed to its successful application.

## 2. A case story of dramatic market behavior

One of the classical examples of highly versatile behavior of the market dates back to 1985 when the Coca-Cola Company, realizing that the market was increasingly occupied by their main concurrent, the Pepsi, tried to bring it back by producing a drink with a new taste. An exhausting narration of this story can be found in many sources [10,20,21], so only some key facts will be quoted here based on these.

After a detailed market and production study aiming to reveal and test people's preference and create the formula to best satisfy it, which required itself a 4 million dollars investment, the production of new Coke was launched. This was announced in the presence of about two hundred TV and newspaper reporters, at an opulent ad hoc event, to make the US customers aware of the change and make them appreciate it immediately.

However, what happened next ruined all the expectations. Within a week of the change, one thousand calls a day were <sup>fl</sup>ooding the company's phone number, and over forty thousand letters added to these. Customers were furious about the new taste and, many of them, were saying that they were seriously considering switching to Pepsi. Finally the Coca-Cola management decided to turn back to the old <sup>fl</sup>avor that very soon resulted in eighteen thousand calls of gratitude and taking the market back.

This well-known case of market behavior will be analyzed further by means of the event bush. For this, a brief synopsis of the method will be presented below.

## 3. Outline of the event bush method

## 3.1. The purpose

The knowledge engineering method of event bush intends to give a strict and <sup>fi</sup>nite but extendable display of an area of reality and corresponding domain of knowledge. Importantly, it does not intend to paint an objective and true picture of reality based solely on formal grounds. The purpose of the event bush is to more or less impartially structure and shape up the subjective information gathered by an expert and communicated by expert to decision-makers. Like any other formalization, it does not say itself what is true and what is false, or what is relevant and what is not, for the studied market. Nevertheless, it helps organize what expert considers relevant, allowing for formulating everything that can happen given a list of premises. It imposes some requirements on these to ensure the most complete and objective inference, but the choice of premises is totally at the expert's discretion. In a discourse or polemics, the tool of event bush may help us formally express and compare contrasting standpoints. Meanwhile, formalization itself often urges an expert to revise knowledge, <sup>fi</sup>nd gaps and strands of “wooly” reasoning, terminological and conceptual intricacy and the like. Such imperfections can be tackled and to some degree cured by the event bush. But like any other weapon, in principle it can be used alternatively, e.g., to produce a beautiful, formally perfect nonsense.

## 3.2. The technique

The method of event bush rests on the assumption that some areas of reality (e.g., change of consumer preferences given various actions of market players) can be represented as shown in Fig. 1. In the considered area of reality, the following events are identi<sup>fi</sup>ed.

(ia) Primary internal events. These are primary, not overlapping and non-unique inputs (basic objects, processes or tendencies) — e.g., consumers in prehistoric era, having no preferences in cool drinks. Such inputs, according to the concept of event bush, would determine any further course of events (“happenings”).

(ib) Primary external events meaning the circumstances that come from the environment. They indicate the way the environment may affect basic inputs or in<sup>fl</sup>uence their further, indirect manifestations, thus “shaping up” different “happenings”. For instance, appearance of any new player in the market may affect the preference of consumers.

(ii) Secondary events (processes or objects) that result from primary inputs with or without the contribution of incoming circumstances — the “happenings” proper (“Consumers prefer drink A and do not prefer drink B”) formulated in a strict concise way indicating their core features determined by the causes, following the principle “one more cause–one more property”.

(iii) Tertiary events that denote end results, or products, generated either by primary internal or by secondary events, with or without primary external ones. Tertiary events document the completed “happenings”. In the considered case, it looks reasonable to take as end results the various preferences of consumers.

Other types of events (e.g., those describing some other type of results — say, quaternary ones) can be added, but the presence of (i)–(iii) is mandatory. Their general interrelation is shown by an example in Fig. 2.

In accordance with the syntax of event bush presented in Fig. 1, the relations between (i)–(iii) can be set:

Events (ia) and (ib) must not lead to other (ia) or (ib);

Event (ib) may lead to an event only together with (ia) or (ii);

Event (ii) must not lead to (ia) or (ib);

Event (iii) must not lead to (ia), (ib), (ii), and another (iii).

These relations are enforced by the connectives of the event bush, each having a graphic designation. Pshenichny and Kanzheleva [13] de-<sup>fi</sup>ne four connectives, <sup>fl</sup>ux, in<sup>fl</sup>ux, con<sup>fl</sup>ux, and furcation, of which the <sup>fi</sup>rst two, <sup>fl</sup>ux and in<sup>fl</sup>ux, are mandatory for an event bush.

...CHANGE WITH ACTIONS OF MARKET PLAYERS

HOW CONSUMER PREFERENCES...

![](/api/attachments/ZTA92XMK/fulltext/images/9f0ddf5f9165de656bc8ab9d34367f018bfab2a8f99b1b3ccf5cfd1452df6cd2.jpg)  
Fig. 1. Syntax of basic blocks of the event bush.

# ...CHANGE WITH ACTIONS OF MARKET PLAYERS

![](/api/attachments/ZTA92XMK/fulltext/images/9ebc1cbcd0f564aae38ce3b66812017b061362248a26d8cd8b1d0db58a332bfc.jpg)  
Fig. 2. Interrelation between events in the event bush.

If one event leads to another, this is de<sup>fi</sup>ned as <sup>fl</sup>ux:

## E Flux $\mathrm { E _ { j } }$

and denoted by a simple arrow. For instance, in Fig. 2, obviously,

Consumer does not buy Coca-Cola with the old taste, does not buy Coca-Cola with the new taste and does not buy Pepsi-Cola (E ) Flux

Consumer does not buy Coca-Cola with the old taste, does not buy Coca-Cola with the new taste and does not buy Pepsi-Cola (E ).

If two or more events lead to one, this refers either to in<sup>fl</sup>ux (denoted by a rounded crossing, or “right turn” graphic sign) or to con<sup>fl</sup>ux (denoted by “double right turn”) connectives.

Putting the right turn, we express an opinion (or an obvious possibility) that two events together may lead to another event, so that one, above the right turn sign (E ), “<sup>fl</sup>ows in”, or modi<sup>fi</sup>es, another event E (to the left of it), resulting in the event below the said sign (E ):

## E<sub>i</sub>; E <sub>j</sub> Influx $\mathrm { E _ { k } }$ :

For example, in Fig. 2,

Consumer does not buy Coca-Cola with the old taste, does not buy Coca-Cola with the new taste and does not buy Pepsi-Cola (E ), Coca-Cola enters market (E )

Influx

Consumer buys Coca-Cola with the old taste, does not buy Coca-Cola with the new taste and does not buy Pepsi-Cola (E ).

Obviously, all events (ib) act as modi<sup>fi</sup>ers. The subject of the resulting event is inherited from the main premise, and the predicate is formed by the modifying one. For intuitive clarity, we adopt that the “right turn” points always down, from the modifying event to the resulting one, which denotes the in<sup>fl</sup>ux. The main and the modifying events may change places, only if this makes sense in the considered domain of knowledge and involves only the events of type (ii).

Once an event (ia) or (ib) is introduced or event (ii) appears in a bush, one should subsequently coincide it with all previously introduced events to <sup>fi</sup>nd out whether any new event can result from each pair.

Along with the <sup>fl</sup>ux, in<sup>fl</sup>ux is mandatory for the event bush, for solely the in<sup>fl</sup>ux involves the events ib in the inference.

The connective of con<sup>fl</sup>ux implies that two or more events “con<sup>fl</sup>ow” into one playing similar (symmetric) role; this is not used in the present study (see below). The event bush does not admit that more than two events lead to one and play non-symmetric role herewith.

Furcation (graphically denoted as circle) represents the case that one event (E , left of the circle) necessarily leads to one of incompatible alternatives $( \mathrm { E } _ { \mathrm { i } + 1 } , \mathrm { E } _ { \mathrm { i } + 2 } , . . . , \mathrm { E } _ { \mathrm { n } } ,$ right of it):

## E Furcation $\mathrm { E } _ { \mathrm { i } + 1 } , \mathrm { E } _ { \mathrm { i } + 2 } , . . . , \mathrm { E } _ { \mathrm { n } }$

This can be exempli<sup>fi</sup>ed by the following inference shown in Fig. 2:

Consumer buys Coca-Cola with the old taste, does not buy Coca-Cola with the new taste and buys Pepsi-Cola (E )

Furcation

Consumer buys Coca-Cola with the old taste, does not buy Coca-Cola with the new taste and does not buy Pepsi-Cola $( E _ { i } + \mathbb { 1 } ) ,$

Consumer does not buy Coca-Cola with the old taste, does not buy Coca-Cola with the new taste and buys Pepsi-Cola (E ).

Wishing to express a case, in which different crisply de<sup>fi</sup>ned options are compatible, one may put several arcs going out of one node (Fig. 2), i.e., use several <sup>fl</sup>ux connectives. This means that an event can lead to any number of other events, in in<sup>fl</sup>ux/con<sup>fl</sup>ux with others or by itself. However, this is not the case in the present study.

The rules of composition of and inference in the event bush do not envisage an opportunity of producing several events from several events in one single step, so the listed inference options expressed by the connectives of the event bush exhaust the entire variety of possibilities.

Change of events is a correctly built expression including one connective of any type [13]. Change has one causal part (that includes the events, one or more, left of the connective) and one effect part (the events to the right of the connective).

Flow, or scenario, is a <sup>fi</sup>nite totally ordered set [18] of changes, in which the left part of the <sup>fi</sup>rst change is an ia event, the right part of the last change is a iii event, and the right part of every preceding change is the left part of the following change. If there is a change with in<sup>fl</sup>ux in it, the modi<sup>fi</sup>er of this in<sup>fl</sup>ux (ib or ii) is included, but not the events that caused it, unless there are successive in<sup>fl</sup>ux changes.

If there is a scenario, in which at least one event participates in causal parts of two changes (e.g., one, being <sup>fl</sup>ux, and another, furcation), there is another scenario, which overlaps with the former one in the interval from the beginning (ia) to this very event, and then rami<sup>fi</sup>es. Furthermore, if there is a scenario without the ii events, <sup>fi</sup>rst, it may only consist of one change, namely the <sup>fl</sup>ux from ia to iii, and then, there also must be a scenario that overlaps with this one in the beginning (i.e., at the ia event) and includes at least one in<sup>fl</sup>ux. This in<sup>fl</sup>ux of ia and another event, ib or ii, will produce an ii event, which will then route this scenario further.

There must not be an event in a bush not included in a scenario.

For more detail on the methodology of event bush the reader is referred to the papers by Pshenichny et al. [14] and Pshenichny and Kanzheleva [13].

## 4. Modeling of the case story by means of event bush

The market shift from Coca-Cola to Pepsi and then back to Coca-Cola in the USA described in Section 3 was modeled by the event bush method (Fig. 3).

Based on the rules of construction of event bush presented by Pshenichny et al. [12,14], the modeling starts with formulation of the modeling task, which was, as shown in Fig. 1, de<sup>fi</sup>ned as to understand how consumer preferences change with actions of market players (at the cool sparkling drink market in the USA). This determines the choice of primary internal and primary external events. Primary internal event (ia) is the consumer in its initial state (taken broadly, as a community that may become Cola drinkers in the USA but are yet unfamiliar with either of the brands), and the primary external events (ib) are the Coca-Cola and Pepsi-Cola companies entering market. The ia event is placed on the left, and ib ones, on top of all the bushes. “Consumer” is considered as an integer entity (like “public”, “audience” or “readership”), and the consumer's behavior in crisp and qualitative sense is considered uniform (“either the consumer does this or it does that”). This means that such speci<sup>fi</sup>cations of customer as people who died before the Pepsi-Cola entered market (and therefore knew Coca-Cola only), or children who happened to try Pepsi-Cola and had not heard about the Coca-Cola, or those consumers who quitted drinking cool drinks, are ignored, as they are believed to be irrelevant for the market strategy of the companies. If they appear for be relevant for some market (e.g., people who quitted, for the alcohol or tobacco markets), then several primary internals should be taken for the bush that refer to each such group of consumers. However, it is clear that actual behavior of the consumer even under this assumption cannot be entirely uniform; to capture such non-uniformity within the speci<sup>fi</sup>ed scenarios (e.g., the majority of Coca-Cola drinkers were disappointed by new <sup>fl</sup>avor but some still liked it), the event bush should be fuzzi<sup>fi</sup>ed or attributed probabilistic values. This task is outside of the scope of the present paper.

Once the primary internal event is chosen and understood, the “nothing happens” scenario is plotted:

(ia) Consumer is in its initial state FLUX (iii) Consumer is in its initial state (type of event is indicated in the brackets hereinafter).

This scenario is not an event bush yet, as there are no ib event(s) and no in<sup>fl</sup>ux connective(s).

Also, the formulation of the ia, ii and iii events is not <sup>fi</sup>nal; though, <sup>fi</sup>nal formulation of all events except for the ib ones is achieved only at completion of the event bush, and solely the ib events are set in <sup>fi</sup>nal form from the very beginning [12].

The next step of construction of event bush is to describe the observed evolution of things by changes of events, using <sup>fl</sup>ux to express a cause–effect relation, in which the cause leads to the effect just “by itself”, in<sup>fl</sup>ux, when there is an obvious input of another event, con<sup>fl</sup>ux, when several causes play similar role to produce an effect, and furcation, when the modeler means to express an opinion that cause could lead “by itself” not to one but to a number of alternative effects. Even at this stage, plotting what happened, the modeler reconstructs, in fact, by merely formal reasons, some of the scenarios that did not, but could, or may, happen — e.g., putting the (iii) events or continuing the furcation changes of events.

When the observed case is plotted, the modeler examines the resulting bush aiming to suppose what other scenarios can bind the existing events. If this inevitably requires introduction of new events (i.e., new boxes in the event bush), these new events are also examined to <sup>fi</sup>nd out what other, alternative relations to preexisting events they may have, and so forth. There is no formal limit for construction of the event bush. Like any other modeling, it formalizes the scientist's view and the same time strongly relies on the scientist's intuition and desire to produce an adequate and concise conceptualization.

The <sup>fi</sup>rst event bush (Fig. 3.1), including one primary external event “The Coca-Cola enters market” and one in<sup>fl</sup>ux, describes the case that the Coca-Cola opened the market of cool sparkling drinks in the USA (assuming no one had done anything of the kind). In this bush, two scenarios are plausible,

(i) that consumer ignored the product (i.e., Coca-Cola) and

(ii) that consumer liked the product

Obviously, the latter scenario took place, and this is shown by bold line.

The ia event correspondingly changes to “Consumer does not buy Coca-Cola”, and so does the tertiary event <sup>fl</sup>uxing from it.

Formally scenario (i) is the “nothing happens” scenario quoted above, and scenario (ii) can be followed in the bush as

(ia) Consumer does not buy Coca-Cola, (ib) Coca-Cola enters market INFLUX (ii) Consumer buys Coca-Cola;

(ii) Consumer buys Coca-Cola FLUX (iii) Consumer buys Coca-Cola.

The second bush (Fig. 3.2) refers to the next stage of market evolution when there appeared a strong rival of the Coca-Cola. Therefore, the bush includes two primary externals, “The Coca-Cola enters market” and “The Pepsi-Cola enters market”, and two in<sup>fl</sup>uxes involving them. As the customer is considered to be one and integer entity, one should not reason about the customer who has not liked, e.g., the old taste of the Coca-Cola — because he in general actually has liked it. For this reason, there is no in<sup>fl</sup>ux, e.g., of the events “(ia) Consumer does not buy Coca-Cola” and “Pepsi-Cola enters market” — they denote a scenario that surely could not take place. However, if we considered the customer not as an integer entity and aimed to follow the history of each particular consumer (for instance, a kid for whom Pepsi is the <sup>fi</sup>rst thing he tried), we would have considered more primary internal events and put the said in<sup>fl</sup>ux as shown by a dashed line in Fig. 3.2, as well as some other connectives.

An assumption was made that if the consumer buys two items (i.e., two brands of drink) simultaneously, he will then choose one. This was done because in an ideal case, which is the most easy for understanding, all the customers behave as one, and any transitional case (when some people drink Coca-Cola, some, Pepsi, and some, both, and bear no other relevant qualitative distinction from one another) could be much better handled by fuzzi<sup>fi</sup>cation (see, e.g., [8]) of the event bush (see below). However, being fuzzi<sup>fi</sup>ed can be a “crisply built” event bush with contrasting alternatives, which is ensured by the above assumption.

![](/api/attachments/ZTA92XMK/fulltext/images/20379036f6cd70a29adab15c9126bd2f1283876a4c307a16b1b2a89a4709b6b7.jpg)

The scenarios encompassed by this bush (including those covered by the <sup>fi</sup>rst one) are:

(i) consumer ignored the Coca-Cola and Pepsi-Cola,

(ii) consumer liked the Coca-Cola and ignored Pepsi-Cola,

(iii) consumer <sup>fi</sup>rst liked the Coca-Cola, then also liked the Pepsi-Cola but then stopped buying the latter and returned to the Coca-Cola,

(iv) consumer <sup>fi</sup>rst liked the Coca-Cola, then also liked the Pepsi-Cola, and then refused the Coca-Cola and focused on the Pepsi only.

In this bush, the scenario that takes place in reality is (iv). It is marked bold.

The primary internal event is updated further accounting for the new ib and now is “Consumer does not buy Coca-Cola and does not buy Pepsi-Cola”. Correspondingly, all the concomitant events are modi<sup>fi</sup>ed.

The <sup>fi</sup>nal bush (Fig. 3.3) addresses the situation that took place when the Coca-Cola issued a drink with new taste. This made to reformulate the internal primary event once again, adding the distinction between “the Coca-Cola old taste” and “the Coca-Cola new taste” (see Fig. 3.2 and 3.3). The following scenarios are identi<sup>fi</sup>ed in the bush:

(i) consumer ignored both taste of the Coca-Cola and Pepsi-Cola as well,

(ii) consumer liked the Coca-Cola old taste and ignored Pepsi-Cola,

(iii) consumer <sup>fi</sup>rst liked the Coca-Cola old taste, then also liked the Pepsi-Cola but then stopped buying the latter and returned to the Coca-Cola,

(iv) consumer <sup>fi</sup>rst liked the Coca-Cola old taste, then also liked the Pepsi-Cola, and then refused the Coca-Cola and focused on the Pepsi only,

(v) consumer <sup>fi</sup>rst liked the Coca-Cola old taste, then also liked the Pepsi-Cola, and then refused the Coca-Cola and focused on the Pepsi only, yet later tried the Coca-Cola new taste along with the Pepsi but <sup>fi</sup>nally refused any Coca-Cola taste and kept on drinking Pepsi,

(vi) consumer <sup>fi</sup>rst liked the Coca-Cola old taste, then also liked the Pepsi-Cola, and then refused the Coca-Cola and focused on Pepsi only, yet later tried the Coca-Cola new taste along with Pepsi and liked it the most, abandoning Pepsi,

(vii) consumer <sup>fi</sup>rst liked the Coca-Cola old taste, then also liked the Pepsi-Cola, and then refused the Coca-Cola and focused on the Pepsi only, later tried the Coca-Cola new taste along with the Pepsi and <sup>fi</sup>nally disregarded both the Pepsi and the new Coca-Cola and returned to the Coca-Cola old taste.

The scenario marked bold (i.e., the one that actually took place) is the last one, no. vii.

As a result, a succession of the event bushes was composed (Fig. 3), each bush corresponding to particular stage of market evolution. Each bush makes up a part of the following one. They can be used for qualitative and quantitative analysis of market and of strategy of market players.

## 5. Discussion. Implications for market and market player behavior analysis

The event bush modeling of market evolution is qualitative and does not require strict de<sup>fi</sup>nitions of terms. Instead, it offers a way to strictly operate with common descriptive vocabulary more or less uniformly understood by various experts and the public. Therefore, the event bush method can be used to elicit expert judgments, extract and organize relevant knowledge from them – in other words, perform knowledge engineering service for the marketing forecasts. As is known from the experience of knowledge engineering, this often also helps experts to <sup>fi</sup>nd discontinuities and inconsistence in their own knowledge and speculate on this. The event bush is an ef<sup>fi</sup>cient framework for building an interview with expert and for processing his/her answers.

To illustrate the representation power of the event bush, we tried to represent the same case by means of another tool, very often used to model scenarios in various domains of knowledge, the Bayesian Belief Network (Fig. 4).

As can be seen from the <sup>fi</sup>gure, the model has a de<sup>fi</sup>nite advantage of simplicity. Nevertheless, one may note that this simplicity hides most of the scenarios and makes the main lesson to be learnt, the mistake made by the Coca-Cola and its decision to return to old <sup>fl</sup>avor, not pronounced at all. In fact, many of the qualitatively important relations (like that the Pepsi-Cola entered market only after the Coca-Cola did) can be only implicitly expressed by assigning the values of 0 and 1 to some variable states (e.g., taking the probability of given state of given variable for p, $p ( X _ { 1 } ) = 1 , p ( X _ { 2 } ) = 0 , p ( X _ { 3 } ) = 0 , p ( Y _ { 1 } ) = 0 , p ( Y _ { 2 } ) = 0 , p ( Z _ { 1 } ) = 1$ p(Z<sub>2</sub>) = 0, and p(Z<sub>3</sub>) = 0). It is noteworthy that conditional probability values can be attributed to and computed in the event bush as discussed by Pshenichny et al. [16].

Also, the event bush represents a formal structure, which can be used in wide cross-domain comparisons to reveal similar patterns of market behavior. For instance, Fig. 5 shows an evolution of a market that has very little to do with the cool drinks, that of hard and heavy metal rock music. However, the scenarios observed there (beginning of hard rock era in the late 1960s, appearance of “heavy metal” bands in mid-1980s, conceptual and <sup>fi</sup>nancial crisis of classical hard rock out-<sup>fi</sup>ts the same time, their splitting and beginning of solo careers of majority of the musicians, failure of the most of them to the early 1990s and triumphal revival of classical hard rock groups in the early 1990s), when put into event bush framework, appear structurally similar to the evolution of the cool drink market in the USA.

This formal pattern of the event bush may serve as a non-intuitive basis, <sup>fi</sup>rst, for application of mathematical models, and then, for comparison of different scenarios in one environment (e.g., at the market of cool drinks) and in absolutely different environments (markets of cool drinks and pop music), thus leading to understanding of general patterns of behavior of markets and, hopefully, the laws governing this behavior.

Tracing the scenarios chosen in similar event bush framework one can accumulate statistics, e.g., of scenarios of using bank loans and insurance products, scenarios of promotion of new brands in various markets, thus looking for more and less frequently occurring cases. Besides, if data are not abundant in one <sup>fi</sup>eld (e.g., for cool drink market), they can be augmented by the data from another <sup>fi</sup>eld (e.g., pop music market) based on structural similarity of framework and scenarios chosen in this framework and assuming that this similarity stems from general (though possibly unknown) laws acting in both <sup>fi</sup>elds.

An important component missed by the event bush in the form presented here is time. Indeed, the duration of particular events and changes of events may be crucial to assess whether a scenario can ever take place and how probable it is. Each event of the event bush can be attributed time interval or intervals. Theoretical issues of putting temporal and special information into the event bush and implications thereof were discussed by Pshenichny et al. [14].

![](/api/attachments/ZTA92XMK/fulltext/images/81583cd69cf276850308ceeaaf119af96ec3e1cd3f6c6220cdaccfd270047a97.jpg)  
Fig. 4. Representation of the modeled case by Bayesian Belief Network. Variables are bold, variable states, listed and numbered below each variable

Another promising quanti<sup>fi</sup>cation of the event bush is attributing conditional probabilistic values to its connectives: translation of value to the connective of <sup>fl</sup>ux, multiplication, to in<sup>fl</sup>ux and con<sup>fl</sup>ux, and subtraction, to furcation. In probabilistic form, the event/probability bush becomes translatable into Bayesian Belief Network (BBN; [11]) but has a number of advantages to a “blindly built” BBN [14,16].

![](/api/attachments/ZTA92XMK/fulltext/images/5c95edfc0b51b70c684a9cbf5d573faeee6cc354effcc6b2a6dd5cee26bdfd67.jpg)  
Fig. 5. Evolution of hard and heavy metal rock music market in event bush framework. See comments in the text

Perhaps yet more urgent for consulting needs, though still poorly considered theoretically [14] is an interpretation of the event bush in terms of fuzzy sets theory, i.e., fuzzi<sup>fi</sup>cation. Thus, it is obvious that all customers cannot behave uniformly, and saying that having tried two drinks it will prefer one and deny the other, we, of course, express extreme and mutually exclusive cases (“prefers Pepsi-Cola” vs. “prefers Coca-Cola”). In fact, of course, the consumer rather prefers one than the other, and actual scenario would lie somewhere in between. Fuzzy sets theory was suggested exactly to cope with this uncertainty, and therefore its application in the event bush methodology looks very promising especially for the needs of consulting.

Finally, scenarios spanning across interrelated markets can be modeled by compositions and ornaments of bushes as shown by Pshenichny and Kanzheleva [13]. For instance, this can work for planning of discount offers and promotion campaigns.

In general, application of the event bush method for market analysis may help identify best practices, ways of optimization and unforeseen threats in the market, exchange experience within the expert community, including the experience gained in different domains of knowledge, and thus serve well for the purposes of consulting and market strategy development.

## 6. Conclusions

The market collision of shift of consumer's preference in the US from Coca-Cola to Pepsi-Cola and then back is well-known and instructive. The method of event bush, originally designed to organize knowledge in the geoscience, appeared, with further development, formal enough to be genuinely independent of geoscienti<sup>fi</sup>c or any other context and pretends to cover a wide variety of tasks, the structure of which <sup>fi</sup>ts the architecture of event bush regardless of domain of knowledge. Analyzing marketing problem well falls in this set of tasks and appears to be much better conceivable when put into event bush framework. Moreover, such framework immediately opens opportunities to search for analogs in other <sup>fi</sup>elds, apply an armory of mathematical tools (deterministic, probabilistic and fuzzy), and do this less subjectively than before. This must substantially contribute to the quality of consulting and advising services throughout the world. However, to do this, a large number of event bushes must be produced quickly for various branches of business that can be better done by event bush editor software that needs to be created.

## Acknowledgments

The authors are obliged to Igor Dukeov for his friendly encouragement and consulting support. CP expresses his particular gratitude to Marina Sukhorukova for guidance and advice in the <sup>fi</sup>eld of marketing studies.

## References

[1] J.S. Armstrong, K.C. Green, Demand forecasting: evidence-based methods, Working Paper 24/05, 1440-771XDepartment of Econometrics and Business Statistic, Monash University, Australia, 2005, (17 pp. http://www.buseco.monash.edu.au/ebs/pubs wpapers/2005/wp24-05.pdf; last visited 25 July 2013).

[2] R. Born, I. Ståhl, The First Hours of Simulation Education, SSE, Stockholm, 2004. (48 pp.).

[3] SUPER Deliverable 2.2, in: P. Fantini (Ed.), Semantic Business Process Life Cycle, 2007. (Accessible at: http://www.ip-super.org/res/Deliverables/M12/D2.2.pdf; last visited 25 Julv 2013).

[4] C. Huemer, UN/CEFACT's Modeling Methodology (UMM) in a nutshell, http:// www.unece.org/<sup>fi</sup>leadmin/DAM/cefact/umm/UMM\_userguide-nutshell. pdf2010, (last visited 25 July 2013).

[5] Information Technologies — Open-edi reference model, International Standard ISO/IEC 14662, http://www.disa.org/international/is14662.pdf1997, (last visited 25 July 2013).

[6] Integration De<sup>fi</sup>nition for Function Modeling (IDEF0), Federal Information Processing Standards Publication, 1993. (128 pp.).

[7] M. Kröll, A.S. Rath, M. Granitzer, S. Lindstaedt, K. Tochtermann, Contextual Retrieval in Knowledge Intensive Business Environments, GI-Workshop Information Retrieval, 2006.

[8] C.C. Lee, Fuzzy logic in control systems: fuzzy logic controller — part I, IEEE Transactions on Systems, Man, and Cybernetics 20 (2) (1990) 404–418.

[9] E.W. McCarthy, The REA accounting model: a generalized framework for accounting systems in a shared data environment, The Accounting Review (1982) 554–578.

[10] Novelguide.com, The story of Coca-Cola, http://www.novelguide.com/ReportEssay/ history/american-history/story-coca-cola1999–2012, (last visited 25 July 2013).

[11] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Network of Plausible Inference, Morgan Kaufmann, Los Altos, CA, 1988.

[12] C.A. Pshenichny, S.I. Nikolenko, R. Carniel, A.L. Sobissevitch, P.A. Vaganov, Z.V. Khrabrykh, V.P. Moukhachov, V.L. Shterkhun, A.A. Rezyapkin, A.V. Yakovlev, R.A. Fedukov, E.A. Gusev, The event bush as a potential complex methodology of conceptual modelling in the geosciences, in: J. Sanchez-Marre, J. Bejar, J. Comas, A. Rizzoli, G. Guariso (Eds.), Proceedings, iEMSs — International Congress on Environmental Modelling and Software, vol. 2, 2008, pp. 900–912, (Barcelona, July 2008).

[13] C.A. Pshenichny, O.M. Kanzheleva, Theoretical foundations of the event bush method. Societal challenges and geoinformatics, in: K. Sinha, L. Gundersen, J. Jackson, D. Arctur (Eds.), GSA Special Paper 482, 2011, pp. 139–165.

[14] C.A. Pshenichny, S.I. Nikolenko, R. Carniel, P.A. Vaganov, Z.V. Khrabrykh, V.P. Moukhachov, V.L. Akimova-Shterkhun, A.A. Rezyapkin, The event bush as a semantic-based numerical approach to natural hazard assessment (exempli<sup>fi</sup>ed by volcanology), Computers & Geosciences 35 (2009) 1017–1034.

[15] C.A. Pshenichny, Z.V. Khrabrykh, Knowledge base of formation of subaerial eruption unit, in: S. Leroy, I. Stuart (Eds.), Environmental Catastrophes and Recovery in the Holocene (Abstracts), Brunel University, London, 2002, (http://atlas-conferences. com/cgi-bin/abstract/caiq-22; last visited 25 July 2013).

[16] C.A. Pshenichny, R. Carniel, V.L. Akimova, Decreasing the uncertainty of BBN technique by means of complex formal approach to volcanological information treatment, European Geosciences Union (EGU) 2nd General Assembly, Vienna (Austria), 24-29 April 2005, Geophysical Research Abstracts, vol. 7, 2005, (EGU05–A–01016).

[17] D. Ross, K.E. Schoman, Structured analysis for requirements de<sup>fi</sup>nition, ICSE '76 Proceedings of the 2nd international conference on Software engineering, IEEE Computer Society Press, Los Alamitos, CA, USA, 1976, p. 1.

[18] B.S.W. Schröder, Ordered Sets: an Introduction, Birkhäuser, Boston, 2003, p. 391.

[19] O. Thomas, M. Fellmann, Semantic EPC: enhancing process modeling using ontology languages, Proceedings of the Workshop on Semantic Business Process and Product Lifecycle Management (SBPM 2007) in conjunction with the 4th European Semantic Web Conference (ESWC 2007), vol. 251, 2007, pp. 64–75.

[20] Underconsideration.com, Coca-Cola vs. Pepsi, Revised Edition, http://www. underconsideration.com/brandnew/archives/coca-cola\_vs\_pepsi\_revised\_edition. php2009–2012, (last visited 25 July 2013).

[21] Voices.yahoo.com, Browne, A., 2007; Coca Cola Versus Pepsi Cola Products, Which is Better? http://voices.yahoo.com/article/249391/coca-cola-versus-pepsi-cola-productswhich-better-351614.html?cat=682007–2012, (last visited 25 July 2013)

Dmitry Mouromtsev is the Head of Intellectual Systems Lab and an Assistant Professor at the Department of Computer System Design and Security, National Research University of Information Technologies, Mechanics and Optics (NRU iTMO). St. Petersburg, Russia. His research interests focus on information systems, artificial intelligence, enterprise resource planning systems and knowledge management. He received his Ph.D. from NRU ITMO in 2003. He is the General Chair of International Conference on Knowledge Engineering and Semantic Web (KESW) and the current editor of Springer CCIS Volume No. 394. His book, Intelligent Systems in Management, was published in 2008 in Russian. Much of his research has studied arti<sup>fi</sup>cial intelligence, semantic technologies and their use in applications.

Cyril Pshenichny is the Geognosis Project leader and an Assistant Professor at the Department of Computer System Design and Security, NRU ITMO. His Ph.D. defended in 1998 was on composition and history of ancient volcanic rocks. His research path brought him to the issues of arti<sup>fi</sup>cial intelligence and knowledge engineering from the geoscience, where he <sup>fi</sup>rst developed the method of event bush now acquiring much wider application. He has authored and coauthored dozens of research papers, gave lectures and conducted seminars throughout the world. Currently he is a co-editor of the “Collaborative Knowledge in Scienti<sup>fi</sup>c Research Networks” monograph to be published by IGI Global.

Anthony Yakovlev got his Master's degree in Applied Mathematics from NRU ITMO in 2009, A Passionate gamer, he has been involved in video games industry since 2004 and won several Industry Awards. He is an entrepreneur now, looking for innovative approaches to market forecasting and decision support.
