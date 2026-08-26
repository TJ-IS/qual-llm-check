---
otero_id: 16859
otero_key: "SZQZ5H8F"
title: "Can DSS evolve without changing our view of the concept of ‘problem’?"
authors: "Maurice Landry; Daniel Pascot; Dominique Briolat"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90195-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Can DSS Evolve Without Changing Our View of the Concept of ‘Problem’?

Maurice Landry \*, Daniel Pascot \* and Dominique Briolat \*\*

\* School of Business Administration, Laval University, Québec, G1K7P4, Canada and \*\* Graduate School of Management, ESSEC, B.P. 105, 95021 Cergy Pontoise Cédex, France

DSS have almost exclusively been presented in the context of problem solving. But the term ‘problem’ is never defined. It is unfortunately a fairly ambiguous term whose meaning oscillates from the observation of an unsatisfactory, objective reality which must be corrected, to the subjective representation of one or more actors faced with a reality which he or they perceived as unsatisfactory. The first of these interpretations (i.e., a problem as an unsatisfactory objective reality) implicitly dominates the DSS literature and design methods, which does not avoid the hidden major stumbling block of ‘problem definition’. We believe that the adoption of the second interpretation (i.e., a problem as a subjective representation) is a better guarantee of the effectiveness of DSS and leads to different design methods (we propose one based on a systemic method oriented toward ‘soft problems’) and opens new horizons for potential application to DSS.

Keywords: Decision; Decision Support Systems; Problem; Problem Solving; Construction of Problem; Problem Definition; Design Methodology; Systemic Method.

## 1. Introduction

It has been well over a decade since the extinction of the utopian notion of 'Total Systems' (Wendler, 1966). Today, we are in a much better position to understand its failure upon consideration of the naivety underlying the development of this fantasy. Supporters of the Total Systems approach, carried away by extremely powerful technological advances, had forgotten to take into consideration the minimal conditions necessary to adapt data processing technology to the business environment into which it was destined to be integrated. This lack of foresight led to many oversimplified hypotheses concerning the organization and the motivations and behavior of its actors \*, including their individual decision-making patterns. It is evident that the theoretical base supporting the development of Total Systems was neither sufficiently large nor sufficiently sound.

Do today's decision support systems (DSSs) run the same risk of failure? It would obviously be false to claim that we have not gained experience

![](/api/attachments/SZQZ5H8F/fulltext/images/344dc9ccff31b98e1b905ffb03fccf1a9fdf1b6a9408a54228b7349bed45f96a.jpg)

Maurice Landry is currently Professor of Management Information Systems at the School of Business Administration of Laval University in Québec City. He received his PhD from UCLA (Accounting and Information Systems) in 1970. His current research interests are concerned with the epistemological and methodological aspects of our current ways of coping with complex problems in organizations.

![](/api/attachments/SZQZ5H8F/fulltext/images/0d630bf295555887b02bcf354f6afb7d714fc0304ae75c3dda6e3601085e1ee2.jpg)

Daniel Pascot is currently Professor of Management Information Systems at the School of Business Administration of Laval University in Québec city. He received a Doctorat from the 'Institut d'administration des entreprises' in Aix-en-Provence in 1975. His current research interests are concerned with the theoretical and methodological aspects of the design of information systems with an emphasis on the design of the data bases and information centers.

![](/api/attachments/SZQZ5H8F/fulltext/images/0efb0551db9b883ede7e2c0a59c96551bbd2e98a7ae799967ce0a5c5261dcb9a.jpg)  
Dominique Briolat is currently Associate Professor of Information Systems at ESSEC (Ecole Supérieure des Sciences Economiques et Commerciales), Cergy, France. His current interests are concerned with methods of design of information systems and office automation.

from the past and that DSSs are based strictly upon technological aspects. On the contrary, the work of several authors, such as Keen and Scott-Morton (1978), Alter (1980), Courbon, Grajew and Tolovi (1979) reflects the increasing emphasis placed on the contemplation of the difficulties of adapting data processing to the organization and its actors, considerations which were virtually non-existent during the Total Systems era.

However, the limited use of DSSs due to a still insufficient theoretical framework to guide efforts made in this direction calls for an even more extensive examination of the issue. We believe, as Naylor (1982) does, that the development of DSSs must necessarily be accompanied by a strengthening of the fundamental concepts underlying these systems. This paper is an extension of the reflective effort already begun in this area.

It may be noted that publications relative to DSSs essentially present these systems in the role of decision-making aids, almost exclusively in the context of problem solving; the specific term ‘problem’ through frequently utilized, however, is never defined. It is, unfortunately, a fairly ambiguous term whose meaning oscillates from the notion of the observation of an unsatisfactory, objective reality which must be corrected, to the subjective representation of one or more actors faced with a reality which he or they perceived as unsatisfactory. Further examination reveals that both the role of the DSSs and its associated design steps differ considerably according to which perspective is adopted. It is, therefore, essential to eliminate the ambiguity surrounding the nature of ‘problem’ in the DSS context. This seems all the more important when one considers that the first of these interpretations (i.e., that of a problem as an unsatisfactory, objective reality) presently dominates the DSS literature and this, in our opinion, is not propitious to the development of DSS design methods which will be capable of eliminating a certain number of major stumbling blocks. For example, although certain authors mention the difficulties involved in problem definition, as well as political and other obstacles and dangers inherent in this phase, one does not find, outside of the usual warnings, a practical, proven method to confront them.

We believe that a view of the concept of ‘problem’ as the result of a mental construct by different actors represents a better guarantee of the effectiveness of DSSs. The adoption of this perspective would not only contribute to the elimination of the ambiguity surrounding DSSs, but would open new horizons to their potential application, as well.

The first section of this paper contains a brief review of DSSs to help illustrate our point that these systems have not met up with the hopes placed in them. As previously mentioned, this may be partially attributed to the current interpretation of the concept of ‘problem’. In the second section, we will discuss the value of considering the concept of ‘problem’ as a mental construct and see how this new attitude promises to pave the way for interesting new developments in the field of DSSs. This discussion will lead us naturally into the third section, where we present a DSS design method into which the idea of ‘problem construction’ may be fully integrated.

## 2. DSS - The Incompleted Project

There seems to be a consensus among current authors regarding the ends pursued by DSSs; starting from those ends, Keen and Scott Morton (1978) propose a distinction between MIS and DSS\*. The MIS concerns structured decisions arising from current administrative tasks and concentrates on methods to improve the accomplishment of these tasks by automating them (efficiency); the DSS deals more particularly with semi-structured decisions where the computer and the decision-maker, in some type of symbiotic relationship, come together, for the avowed purpose of not only improving the decision-making process, but to improve the quality of decisions as well (effectiveness).

Theoretically, the DSS attempts to augment the cognitive capacity of an individual or a group of individuals by using the computer to memorize a large amount of data and to manipulate these data at high speed. The computer thus permits the treatment of the structured part of decisions by means of more or less complex algorithms, while the decision-maker undertakes the unstructured part through more or less powerful heuristics. This combination should be a harmonious one, where each party accomplishes the tasks for which it is best suited.

This was the declared objective of the DSS... but what has become of this worthy ideal? A thorough analysis indicates that the utilization of DSS is limited both as to the types of decisions to which they are applied, and as to the phase of the decision-making process which is emphasized (Alter, 1980: Keen and Scott-Morton, 1978; Pascot, 1977).

The majority of DSSs are employed in essentially structured situations. In fact, it has proven very difficult to design DSSs when the judgemental aspect of decisions dominates the ‘programmed’ aspect. Furthermore, although efforts have been made to adapt the DSS to the psychological traits of decision-makers (Botkin, 1973; McKenney and Keen, 1974), in practice it has been necessary to concentrate the design of the DSS on the task to be performed (Pascot, 1975, 1977). This turn of events reinforces the emphasis placed on the structured, or programmable, aspect of a problematical situation, at the expense of the individual interpretations of the situation by the actors involved.

DSSs seem to be essentially employed during the design phase \* of the decision-making process as well (Pascot, 1978). One can, in effect, distinguish two successive levels of activity, both of which may be described by the same process: intelligence, design and choice. The first level consists of a determination of the type of action contemplated, or the decision to be taken; the second consists of the treatment of a new occurrence of a particular type of decision previously identified at the first level; it is at this second level that current DSSs are most prevalent. A specific example of this may be found in the case of the DSS developed by Scott-Morton (1971) for the laundry division of a large company. Scott-Morton was able to demonstrate that the DSS which he had developed had a significant impact of the intelligence phase of the decision-making process. However, the decisions considered in this instance (identification of bottlenecks, inventory stock-outs) were of a predetermined type and had nothing to do with a reconsideration of the distribution network, the organization of the production line, or work schedules. There had already been a preliminary level of activity – explicit or implicit – which lead to the decision to look for solutions in terms of production scheduling.

The very obvious result of this tendency is the marked orientation of DSSs towards the solution rather than the formulation of problems. This orientation has emerged not only in practice, but at the level of conceptual reflection as well. The majority of theoretical references deal with problem resolution. One may begin, for example, with the fundamental work of Newell and Simon (1972), 'Human Problem Solving' which so often serves as a basic reference. Don't these authors explicitly state that they were concerned in this work with human reasoning in regard to the resolution of problems rather than their formulation? It is rare, in the field of DSSs, to find an author who has treated the formulation of problems in depth, although Keen and Scott-Morton (1978) have stressed the fact that 'the problem does not come neatly packaged'. Before being in a position to know how to solve a problem, one must determine the nature of the problem or else risk committing a type III error (Killman and Mitroff, 1972) which consists in solving correctly a wrong problem. Each time that one commits this type of error during the design of a DSS, its effectiveness is reduced considerably.

To what should we attribute this state of affairs which critically effects the effectiveness of DSSs and which currently limits their development? For the moment, we will answer the question by two other questions:

What do we really know, operationally, about the intelligence of problems and about the process by which organizational members perceive and represent them?

How can we elicit serious reflection concerning this step when in practice, problems are only associated with the facts used to construct them, thus sidestepping the difficult consideration of the selection and interpretation process by actors?

DSS designers have, up to this point, generally avoided these fundamental questions. It is precisely for these structured problems, which designers have chosen to solve, that organizational actors have been culturally trained to select ‘the pertinent facts’. It has, therefore, been possible to circumvent the question of divergence of interpretation; but what is the fate of other categories of problems? Without a doubt, the future development of DSSs calls for a profound reflection regarding the concept of 'problem'. We will discuss this topic at greater length in the following paragraphs.

## 3. Reflection on the Concept of 'Problem' for DSS

There are two theoretical perspectives which differ significantly within which problems may be conceived. The DSS design process is not indifferent to the perspective adopted. We will attempt here to describe these two perspectives by contrasting them and to illustrate their respective influence on the DSS design method as well as on the devolved role of the designers.

## 3.1. Problems Viewed as 'Objective Realities'

In practice, problems are often assimilated (especially in the case of DSSs) to unsatisfactory, objective realities uncovered by observation and analysis of facts. Consequently, every well-trained observer, that is also an analyst with an adequate background is, by definition, in a position to define ‘the problem’. Due to the fact that DSS designers have a basic training which inevitably includes an initiation to the traditional scientific method (and are thus, by definition, trained in observation and analysis) they are naturally the experts chosen to define the problem.

Within this perspective, the facts (understood here as what really exists, their collection and their analysis are the focus of the expert. The various interpretations of these facts by the organizational actors are of secondary importance and usually suspected of partiality. The definition of the problem by the designer is thus privileged because the method leading to his definition resembles the traditional scientific method to the extent that the particular ability needed at this stage is more closely related to analysis than to design. Consequently, problem definition is considered as a preliminary step to DSS design rather than being a critical activity within the DSS development process.

The methods which guide the development of DSSs resulting from this objective view of problems tend to have the following characteristics:

\- Preponderance of analysis over design;

\- Minimization of the role of organizational actors to the advantage of that of the expert;

\- Emphasis on what must be done (steps to accomplish) without any particular attention to who should do it;

\- Validity of the method assured by constant reference to reality (the facts) and the necessity to maintain a rigorous organization of the facts;

\- Attempt to eliminate all value judgments;

\- Minimization of the importance of the problem definition stage.

To sum up, the methodological characteristics enumerated above reflect clearly positivist epistemological position. Does this mean that all adherents of this position hence ignore organizational actors? Certainly not. They do, however, wander from the spirit of their methodology and are in an ambiguous and uncomfortable situation.

## 3.2. Problems Viewed as 'Mental Construction'

The alternative to regarding a problem as an unsatisfactory, objective reality is to consider it as rather a subjective representation conceived by a particular actor when confronted with a reality which he perceives as unsatisfactory. There are several consequences of this point of view: the subjective dimension (i.e., the actor's interpretation) is recognized as an essential element in the emergence of a problem, and the concept of 'problem' thus becomes closely related to the cognitive and affective activities of an actor \*. From this standpoint, one can no longer talk about 'a problem' but rather about 'someone's problem'.

How can the notion of an organizational problem, which is the subject of interest for a DSS and which implies the participation of several actors, be reconciled with the individual, subjective interpretation just suggested? The formulation of an organizational problem within this perspective requires:

(i) The identification of the representations, more or less crystallized, of the various participants involved into a problematical situation;

(ii) The identification of zones of convergence and divergence of these representations;

(iii) An attempt to assure the closest reconciliation possible of the divergent zones.

The objective of these steps is thus to construct a common representation which is as compatible as possible with the various individual views of the actors, keeping in mind that a consensus among actors is rarely possible when dealing with complex problems. The set of solutions acceptable to the actors depends upon the breadth of this common representation (Landry, 1978). In other words, the larger is the minimal common representation, the greater is the possibility to find an acceptable solution. The formulation of an organizational problem thus implies the development of a language common to the various participants as well as the existence of mechanism which facilitate exchange, debate and negotiation.

It is important to underline here the substantial differences in the approach to and the solution of organizational problems when viewed as mental constructs rather than as an unsatisfactory, objective reality. The formulation of the problem first requires the identification and the interpretation of the individual perceptions of the different participants. These perceptions are then confronted to arrive by agreement, either spontaneous or negotiated, at the facts (considered here as the shared hypotheses regarding the perceived reality of the situation). The actors are naturally much better qualified to formulate the problem than the expert is. The role and the characteristics required of the expert are therefore considerably different from those required by the alternative view of the nature of ‘problem’. He must assist the actors in their definition of the problem. He must attempt to facilitate the interaction among actors and seek ways to encourage the expression of various points of view. He must suggest methods and measuring instruments \*, knowing that agreement on methods leads naturally to agreement on the facts. Finally, he must avoid imposing his definition of the problem upon the actors \*\*. In addition to the abilities of observation and analysis, the DSS designer must possess abilities in the area of human interaction, synthesis and design as well.

The characteristics of the methods arising from this second perspective of the nature of ‘problem’ may be summarized as follows:

\- Preponderance of design over analysis;

\- Central role attributed to organizational actors, the expert occupying a support function;

\- Necessity to specify not only the steps to accomplish, but who should be responsible for them as well;

\- Validity of the method assured by mechanisms which facilitate communication, debate and negotiation;

\- Acceptance of value judgments as an integral and normal part of the process (these value judgments are subject to discussion within the framework of the method);

\- Emphasis on the problem definition stage.

\*\* For example, an inventory manager declares that his inventory is composed of 4000 items, the majority of which are seasonal, thus generating a formulation of the problem centered on the control of requests for inventory, and the expert remarks, after counting, that there are only 900 items, 20 percent of which are seasonal, thereby generating a definition of the problem centered on the preparation and the follow up of orders from suppliers. It is neither necessary to reject the decision-makers perception nor to be deprived of the expert's viewpoint. In order to arrive at an agreement over the definition of 'facts', it is necessary to first agree upon the choice' of the appropriate measuring instrument. In this example, the agreement concerns the counting, to a precise figure, of the number of items on the shelves as an estimation of the number of items generally in stock, and the compilation of inventory requisitions during a certain time period as and indication of the seasonality of various items. These activities will likely cause the inventory manager to modify his formulation of the problem.

## 3.3. Types of Problems and DSSs

The caricature used to contrast the alternative attitudes concerning problems has highlighted the influence of each on the DSS implementation process. It should be noted that the more indefinite and complex the problem and the greater the number of actors and personal interests that are involved, the greater are the differences. Inversely, the distinction between the two attitudes and the resulting differences in the implementation process diminish when confronted with well-structured problems.

From the point of view of ‘problems as constructs’, a problem is well structured when the representation by various actors of a problematical situation tend to be identical. Under these circumstances, one finds two prerequisite conditions: (i), the situation must not be very complex; and (ii) it must be of a repetitive nature to the point where it is deemed expedient to candidly study the manner in which it should be presented for solving (generally with the aid of algorithms). When this study results in an acceptable solution, it normally becomes a part of managerial custom by way of practice, literature, and education in the area. A common representation thus tends to be established, and the problem is said to be structured. Its definition becomes almost identical to the definition one would obtain using the perspective of problems as unsatisfactory, objective realities.

As we have seen in section 2, DSSs have been chiefly developed to solve structured problems. They have been conceived and utilized in situations where confusion between the two alternatives attitudes regarding problems was of little or no consequence; efforts to clarify the ambiguity have, therefore, not been necessary up to this point. This is the case where a single actor defines and solves his own problems. It is also the case of the DSS for which precise reference models already exist, such as normative models drawn from the literature and for which the design is oriented towards this normative view of the problem. Finally, it is the case of the DSS prescribed and paid for by the principal actor, who imposes his definition of the problem on secondary actors (which may well cause difficulties of implementation and use of the DSS by those who do not share the imposed interpretation).

If DSSs are to go beyond their present restricted application to structured problems, we believe it is of utmost importance to explicitly acknowledge the ‘constructed’ nature of problems. This recognition leads us to the conviction that the majority of current DSSs represent only a subset of the possible range of DSS applications (see Fig. 1).

Cell 1-A is, in our opinion, representative of current DSSs, which have been employed almost exclusively for structured problems; the designer is capable of formulating and adequate representation of the problem, his role consisting essentially of problem analysis aided by pre-existing reference models. Cells 2-A, 2-B and 1-B represent the almost unexplored potential of DSSs in forms possibly very different from what we know now, but which we cannot ignore or refuse to study. For example, for the subset of problems represented by Cell B-1, where the major difficulty would seem to be an inability to sufficiently grasp the relationships existing between the solution and the problem, an evolutionary design approach such as that suggested by Courbon, Grajew and Tolovi (1979) would lead to the discovery, by successive iterations, of the concordance between the problem and its alternative solutions. An increasing number of authors agree on the interest of this kind of approach (McLean, 1979; Sprague, 1980).

But this kind of approach is better suited to situations where only one individual plays the role of the client and the user (according to Churchman's model) and even better plays also the role of the analyst (McLean, 1979).

But as soon as there are several clients and/or users, difficulties to express a common formulation of the problem appear (Landry, 1978) that is why Hoppen and Sitruk (1981) in their dynamic approach, propose to complete the evolutionary design approach by adding a strategic approach that deals with the difficulties to construct a common formulation of the problem. Consequently, for these two subsets of problems (cells 2-A and 2-B) an approach of the type proposed in the next section would be more appropriate.

<table><tr><td rowspan="2">The solution to the problem as formulated is:</td><td colspan="2">DSS is intended to support a problematical situation in which, at the outset:</td></tr><tr><td>(1) A single formulation is called for</td><td>(2) Several formulations are encountered</td></tr><tr><td>(A) Known and accepted</td><td>1-A</td><td>2-A</td></tr><tr><td>(B) Uncertain and not</td><td>1-B</td><td>2-B evident</td></tr></table>

Fig. 1. A Taxonomy of DSS.

## 4. Proposal of a DSS Design Methodology

## 4.1. Checkland's Methodology

Our consideration of the notion of ‘problem’ as a key element in the effectiveness of DSSs leads us to propose a design methodology which permits the operationalization of such a viewpoint. We must find a method which allows us to take the subjective dimension of problem definition into account and which, at the same time, serves as a guide to the various actors during the DSS construction process. Checkland (1972,1981), has suggested a method to approach ‘soft’ organizational problems which seems to be well suited to these objectives. We propose to demonstrate how this approach may be adapted to the case DSS design.

This method was developed to tackle complex, poorly, structured situations in contrast to more or less well-defined situations which are, as we have illustrated, more easily and straightforwardly analyzed. Checkland's methodology is principally systems-based, with constant attention placed on the avoidance of two important obstacles: the utilization of a terminology so vague that its operational utility is sacrificed for an overly general global view; or, at the other extreme, a terminology so rigid as to deform the richness of the situation under study. Contrary to many methods which do not specify the operational rules by which we are to simplify the perceived reality, Checkland explicitly emphasizes the necessity to choose a reference point (or 'root definition'). This reference point is chosen as a perspective from which to examine a situation too complex for a human being to model directly. This chosen perspective must be selected by the actors themselves (and not be the expert), and thus becomes a practical, non-arbitrary rule for pertinent variety reduction (i.e., of confrontation and partial reconciliation of different views of the same unsatisfactory situation). Figure 2 depicts the major steps of Checkland's systemic method.

![](/api/attachments/SZQZ5H8F/fulltext/images/8ffa81dbeb9b32e1087b8d67c14e620852cad64a0fa9ed7662d180e99e271055.jpg)  
Fig. 2. Major Steps of Checkland's Systemic Method.

Checkland proposes, as a first step, the construction of the richest possible picture of reality, in order to arrive at a better understanding of the problematical situation. This step must be accomplished with an attitude of detachment; i.e., without privileging any particular viewpoint. In the case of DSSs, this step begins when at least, one actor broaches the possibility of implementing a DSS and one or more persons (designers) are called in to more fully explore this possibility. The problem sensed by the actor may very well not be formulated explicitly, but may rather be simply a symptom. Checkland's methodology suggests that the designer begins by identifying the principal actors, presumed at this stage to be the future actors who will use the DSS, and by collecting as much information as possible regarding their individual perspectives. In this manner, the designer avoids committing himself to any particular point of view and is at liberty to collect the individual interpretation of each actor. The method thus clearly respects the conception of the nature of 'problem' which we proposed earlier in this paper.

During the second step, these different views of the problem must be reconciled to a certain extent in order to choose a particular point of reference, or root definition. The choice of the root definition is a result of discussions, negotiations and even confrontation among the various actors. The root definition, often defined in terms of a process, is a condensed representation of the system in its most fundamental form, englobing the activities of all actors. To cite one of Checkland's example (1972):

"Is it preferable to consider the system 'church' as a social welfare system, as a ritual-organizing system, as a belief-maintenance system, or as a system to provide support in the face of unanswerable questions?"

It depends on the actors (and certainly not the designer) and the perspective which they believe best describes their situation. One thing, however, is evident: the choice of a root definition is not indifferent, and it strongly conditions the solution or solutions retained. Finally, it is worthy of note that the fact of working collectively during these first two steps inevitably leads the actors to a better understanding of the various tasks and of their interrelationships. This is mainly the result of the inductive type or process followed during these steps and the information generated by each actor.

The third step concerns a deductive process by which the minimal activities necessary to satisfy the root definition are assembled. What are the minimal components which the system must possess? The definition of the conceptual model, or ‘system’, to use Churchman’s terminology (1968), facilitates the discovery of key decisions and key decision-makers. This conceptual model, or minimal system, differs substantially from the normative model as proposed by Keen and Scott-Morton (1978). Checkland’s conceptual model makes no claim of being normative or ideal; it is, rather, as its name suggests, a simple model of the activities necessary to the existence of a system that matches the root definition and serves as a point of comparison with the information collected during step 1.

This comparison, step 4 brings out differences between the model and the picture of reality previously assembled thus allowing the discovery of possible areas of improvement (step 5). During step 6, the actors (and only the actors) choose the relevant and feasible changes required to improve the situation, as well as their order of importance. Finally, steps 7, 8 and 9 are the normal steps advocated by every classical method of systems design.

A first iteration of Checkland's method leads to the selection of areas susceptible to improvement by means of a DSS. A second iteration of this same method is then employed for the actual design of this DSS.

## 4.2. Comparison with the Predesign Cycle of Keen and Scott-Morton

One can recognize in this method, the key elements which lead Keen and Scott-Morton [(1978) ch. 6] to define prior to the design and implementation process, a predesign cycle (Fig. 3) whose objective is to assure that one is working on the right problem. It is therefore interesting to compare the similarities and differences which exist between Checkland's method and this predesign cycle. However, even though at first glance, one finds numerous common elements between the two, it rapidly becomes evident that it is a delicate task to compare step by step.

![](/api/attachments/SZQZ5H8F/fulltext/images/eed6402272800f5307059ef70d11280c1579e75cdb43a9b7d40a8c94f2fc3812.jpg)  
Fig. 3. The predesign cycle of Keen and Scott-Morton [(1978) p. 174].

It must first be noted that the roles played by the various partners differ from one method to another. For Checkland, the expert does not control the evolution of the process; he rather acts as a consultant and cannot become the principal actor except, maybe, within phase 7 and subsequent phases. On the contrary, for Keen and Scott-Morton, the expert is in implicit control of the process: the manner in which they emphasize the necessity to assure user participation is significant, for if the user had control of the process, the authors would, instead, stress the integration of the expert within the process.

Secondly, one finds difference between the two methods with respect to the procedure leading to the formulation of the problem. Checkland does not recognize the existence of an objective, absolute perspective from which the problem may be studied; there exist only root definitions, or points of view, more or less desirable and pertinent for management. Phases 2 and 6 are crucial in this respect (and must be absolutely under the actors' control). This phase only partially exists in Keen and Scott-Morton's method (Fig. 3, phases a, b, d, f) but even then in a very ambiguous and diffuse manner. Phase 6 (selection of changes by the actors) and i (selection of decision areas susceptible to assistance) are fairly comparable, although found at different places within the cycle; these phases being essentially the product of the entire process. This observation is of vital importance: it is evidence of an agreement upon the necessity of employing a process which identifies the problem prior to attempting to use technical tools or solutions; however, there is not total agreement upon the nature of the process. Thus Checkland's systemic method emphasizes the necessity to generate a rich, diversified and subjective picture of the problematical situation, while Keen and Scott-Morton seem to seek from the the outset a clear, objective description of the situation.

Thirdly, it seems important to stress the differences in the nature of Checkland's conceptual model (phase 3) and Keen and Scott-Morton's normative model (phase g). The normative model prescribed by Keen and Scott-Morton is an outgrowth of the presumed scientific nature underlying its development, while Checkland's conceptual model is much more pragmatic, incorporating elements define during phases a, b and c of Keen and Scott-Morton's predesign cycle. In addition, the normative model is essentially a model of the desired solution; conversely, the conceptual model is a minimal reference tool which, by comparison, permits the generation of suggestions regarding desirable changes and their order of importance.

Finally, it is worthy to note that Keen and Scott-Morton emphasize the necessity to complete the cycle at least twice; this seems to authorize iterations between the descriptive and normative models, the new definition of one being based upon the current version of the other, etc. This gives us reason to question the principle of objectivity upon which the predesign process is supposedly based.

It would seem that the differences between the predesign process and the Checkland's systemic method stems from different interpretations of the notion of 'problem'. It appears that Keen and Scott-Morton, as did many of their colleagues, began their study of DSSs with the notion of 'problem' as an unsatisfactory, objective reality. Thereafter, in the face of certain difficulties, they found it necessary to enlarge their frame of reference. This led to the development of a predesign cycle, which implicitly, but not explicitly, treats problems as mental representations. However, this evolution has not been formally identified, so that the process which they propose is expressed from their initial viewpoint. We believe that this causes difficulties, ambiguity and confusion, particularly concerning the respective roles of the models (the descriptions of the problematical situation and of the desired situation) developed during the process.

## 5. Conclusion: The Advantages of Viewing Problems as Mental Constructions During DSS Design

The framework for interpretation provided by the epistemological study of problem definition is of increasing importance for future DSSs. The patterns brought out by DSS designers take on a new dimension when problems are seen as mental constructions. This approach promises to open large, new horizons to DSS development. The observed benefits are transformed from side effects to central phenomena: better communication (Alter, 1980); better understanding of the problematical situation; improvement of the learning process, both individual and collective ... (Ginzberg, 1978). This theoretical framework is obviously not necessary in the face of problems having a single definition and easily accepted, straightforward solutions. It becomes of great value, however, when the designer is faced with uncertainty, multiform situations.

There are two distinct levels at which the developments suggested by this approach may be grouped. The first level concerns theoretical concepts and methods; the second comprises operational concepts and tools. We have demonstrated the appropriateness of Checkland's method at the theoretical and methodological level; however, other methods may be very powerful in this context as well. One particular method which came to mind is the 'Situational Normativism' of Shakun (1975,1981). Other approaches can complete them and are also well suited to this view of problems: the evolutionary approach of Courbon et al. (1979), and the prototype method; see, for example, Keen (1981). Indeed, the construction of a prototype permits an elegant and effective resolution of the various contradictions previously discussed.

This approach also suggests a reorientation of future research. Researchers will have to be more preoccupied with the functioning of the organization, and more particularly, with the existence and the evolution of organizational power structures (Crozier, Friedberg (1977); Markus (1980)). The redefinition of the expert's role is also very important. The approach defines the expert as a consultant or a 'facilitator' (Courbon-Bourgeois, 1981). This view is in agreement with recent DSS design developments in which his role is seen as that of a 'chauffeur' during the design and use of the DSS. It appears that the voluminous literature relative to the implementation as well as the rejection of DSSs is a visible consequence of the role assigned to the expert by the method used.

At the operational level, research regarding DSS generators appears particularly promising. The nature of these generators permits the implementation of the approaches discussed previously, which require several iterations and call for evolutionary DSSs. This implementation should be accompanied by ongoing research concerning the integration of DSSs and data base within transactional systems.

But the physical organization of these data base is designed according to the needs of the transactional systems and is seldom suited to the needs of DSS (Sprague and Carlson, 1982). As a solution, one can design, starting from the same base of data, two different physical data base, one for the need of transactional systems (operational data base) and the other for the needs of DSS (informational data base) (Martin, 1977). But the only difference is the physical organization of the two data bases, the conceptual model is common to both of them, and should not be changed by every evolution of a DSS. (Le Moigne, 1973; Landry and Le Moigne, 1977, Tardieu, Nanci and Pascot, 1979). This research would clarify and reinforce the ties between DSSs and transactional information systems as it is obvious that DSS use many data from the transactional systems.

## References

Alter, S.L., Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, Reading MA (1980).

Botkin, J.W., An Intuitive Computer System: A Cognitive Approach to the Management Learning Process. Ph.D. dissertation Harvard Graduate School of Business Administration, Cambridge MA (1973).

Checkland, P.B., Toward a System Based Methodology for Real World Problem Solving, J. System Engineering 3 (1972) pp. 87–116.

Checkland, P.B. and D.B. Smyth, Using a Systems Approach: the Structure of Root Definitions, J. Applied Systems Analysis 5 (Nov. 1976) pp. 75–83.

Checkland, P.B., Systems Thinking, Systems Practice, Wiley, New York (1981).

Churchman, C.W., Why Measure?, Measurement: Definitions and Theory, Churchman, C.W. and P. Ratoosh, eds., Wiley, New York (1959).

Churchman, C.W., The System Approach, Dell Publishing Co., New York (1968).

Courbon, J.C., J. Grajew and J.R. Tolovi, Conception et mise en oeuvre des systèmes interactifs d'aide à la décision. L'approche évolutive, Informatique et Gestion 103 (Jan. 1979) pp. 51–59.

Courbon, J.C. Bourgeois, L'approche systémique et la conception évolutive, Informatique et Gestion 122 (1981) pp.

Crozier, M. and E. Friedberg, L'acteur et le système, Seuil, Paris (1977).

Ginzberg, M., Redesign of Managerial Task. A Requisite for Successful DSS, Mis Quaterly (March 1978).

Hoppen and Sitruk, L'approche dynamique. Une méthode pour l'implantation des systèmes interactifs d'aide à la décision, Informatique et Gestion 128 (1981) pp. 55–61.

Keen, P.G.W., Value Analysis: Justifying Decision Support Systems, MIS Quarterly 5 (March 1981).

Keen, P.G.W. and M.S. Scott-Morton. Decision Support Systems: An Organizational Perspective, Addison-Wesley. Reading MA (1978).

Killman, R. and I.I. Mitroff, Problem Defining and the Consulting Intervention Process, California Management Review, 21 (Spring 1979) pp. 26–33.

Landry, M. Qu'est-ce qu'un problème?, INFOR 21 (1983) 31–45.

Landry, M. Doit-on concevoir ou analyser les problèmes complexes?, Analyse des systèmes appliqués, Theorie et Pratique 2 (Aug. 1981) 56–66.

Landry, M., Formation et résolution de problèmes en groupe dans un milieu organisationnel. Un schéma d'observation et d'analyse, Relations industrielles: 33 (1978) pp. 591–610.

Landry, M. and J.L. Le Moigne, Towards a Theory of Organizational Information System - a General System Perspective, Information Processing '77, Gilchrist, B., ed., IFIP/North-Holland, Amsterdam, New York (1977).

Le Moigne, J.L., Les systèmes d'information dans les organisations, PUF (1973).

Markus, M.L., Power Politics and MIS Implementation, CISR no. 59, Sloan WP, no. 1155-80 MIT (1980).

Martin, J., Computer Data-Base Organization, Prentice Hall, Englewood Cliffs NJ (1977).

McKenney, J.L. and P.G.W. Keen, How Managers' Minds Work, Harvard Business Review, 52 (May–June 1979) pp. 79–80.

McLean, E.R., End Users as Application Developers, MIS Quarterly 3 (Dec. 1979).

Naylor, T.H., Decision Support Systems or Whatever Happened to MIS? Interface 12 (Aug 1982).

Newell, A. and H.A. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs NJ (1972).

Pascot. D., Les systèmes interactifs de planification budgétaire, amplification du raisonnement humain, unpublished thesis, Aix-en-Provence (1975).

Pascot, D. Les systèmes interactifs d'aide à la décision. La situation actuelle et les axes de recherche, Actes du Congrès AFCET, modélisation et maîtrise des systèmes (1977).

Pascot, d. Les systèmes interactifs d'aide à la décision, 01, Informatique 123 (Sept. 1978).

Scott-Morton, M.S., Management Decision Systems Computer Based Support for Decision-Making, Division of Research, Harvard, Cambridge MA (1971).

Shakun, M.F., Policy Making Under Discontinuous Change: The Situational Normativism, Management Science 22 (Oct 1975).

Shakun, M.F., Formalizing Conflict Resolution in Policy Making, Working Paper no. 81-04, New York University, Garduate School of Business Administration, New York (1981).

Simon, H.A., The New Science of Management Decision, Harper and Row, New York (1960).

Sprague, R.M., A Framework for the Development of Decision Support Systems, MIS Quarterly 4 (Dec. 1980).

Sprague, R.M. and E.D. Carlson, Building Effective Decision Support Systems, Prentice Hall, Engelwood Cliffs NJ (1977). (1982).

Tardieu, H., D. Nanci and D. Pascot, Conception du Système d'Information, construction de la base de données, Edition d'organisation (Paris) et Gaétan Morin, Chicoutimi, Quebec (1979).

Wendler, C., Total Systems: Characteristics and Implementation in: The Systems and Procedures Association, Cleveland OH (1966).
