---
otero_id: 5550
otero_key: "BZG4YBFK"
title: "Activity-based design"
authors: "Peter Bøgh Andersen"
year: "2006"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000599"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Activity-based design

Peter Bøgh Andersen<sup>1</sup>

<sup>1</sup>Department of Information and Media Studies, The Wiener Building, IT City Katrinebjerg, Aarhus University, Aarhus N, Denmark

Correspondence: Peter Bøgh Andersen, Department of Information and Media Studies, The Wiener Building, Room 224, IT City Katrinebjerg, Aarhus University, Helsingforsgade 14, DK 8200 Aarhus N, Denmark. Tel: þ 45 8942 9250; Fax: þ 45 8942 5950; E-mail: pba@imv.au.dk, Homepage: http://imv.au.dk/Bpba

## Abstract

In many types of activities, communicative and material activities are so intertwined that the one cannot be understood without taking the other into account. This is true of maritime and hospital work that are used as examples in the paper. The spatial context of the activity is also important: what you can do depends upon where you are. Finally, human and automatic machinery alternate in filling certain roles in the activity: sometime the officer maintains the course, sometimes the autopilot. Such activities require us to rethink the traditional oppositions between communication and instrumental actions, between human and non-human participants, and between an activity and its spatio-temporal context. The advent of pervasive technologies, where active or passive systems become embedded in our working and living spaces, from where they offer their services to us, puts the need to reconsider these basic oppositions high on the research agenda. This paper presents a consistent framework called habitats for understanding communicative and material activities and their interplay, for understanding how activities can be associated to physical surroundings, and for understanding how humans and automatic machinery can replace one another in an activity. It also gives an example of how to use the framework for design. European Journal of Information Systems (2006) 15, 9–25. doi:10.1057/palgrave.ejis.3000599

Keywords: activities; habitats; semantic roles; pervasive computing

## Purpose

The purpose of this paper is to develop a design-oriented notation where activities associated to physical space are the basic concept. The background is a project in maritime work and technology in the Danish Center for Man–Machine Interaction. It is a characteristic of the maritime domain that (1) human activities and automatic systems are blended and regularly replace one another, (2) communicative and material actions are intertwined, and (3) the participant’s location in physical space determines his action possibilities. Here are a few examples: (1) whereas the officer manually controls the course as well as the speed of the ship inside a harbour, these tasks are gradually delegated to automatic equipment as we approach open sea; (2) bridge-work involves simultaneously the physical manipulation of the ship and communication with crew, other ships, and vessel traffic services; and (3) the activity of berthing a ship must often be moved to the wing of the bridge, where an unimpeded view to the quay is available. Another example of the latter – in an investigation of ‘mobile’ hospital work (Bardram & Bossen, 2005), the authors list four main causes for movements in a hospital ward, one of which is specialised places. The purpose of movements is to ‘make the right configuration of people, places, resources, and knowledge emerge’ (Bardram & Bossen, 2005, p 151; a similar example is given in Brynskov & Andersen, 2004).

The relevance of such settings increases with the advent of pervasive and ubiquitous computing that promises an even closer integration of activity, artefact, and space. These technologies are distributed in space and/or attached to moving objects and humans, and are intended to become an integrated part of our daily life. Context-sensitive technology exploits the fact that our activities are often connected to specific locations:

The archetypical example is the medicine tray that a nurse puts onto the bed tray on a patients bed. ABC senses the nearness of the nurse, medicine tray, and patient, and infers that the EPR system should be reconfigured to show the medicine schema for the particular patient and with the EPR logged in as the nurse. Focus was on being able to forward these activities to any computing device in the vicinity of the nurse; and that activity execution should not be automatic (Christensen et al., 2004, p 5).

The purpose of the paper is to present a conceptual framework that (1) allows us to describe activities as firstclass citizens, (2) provides a clear connection between communicative and material activities, and between human participants and automated systems, (3) allows us to bind (parts of) activities to times and places, and (4) indicates possible implementations in an object-oriented framework.

The paper is organised as follows. The next section describes other approaches to solve the problems described above and pinpoints the characteristics of the habitat approach. Inspired by linguistics, a specification language is proposed in the last two Sections. The penultimate section discusses the notion of activities, actions, roles, and participants, and the last section introduces the notion of habitats, spatial–temporal chunks that are designed to support a delimited set of activities, and suggest a way of combining the actions afforded by the habitat with those desired by participants of activities.

## Previous work

In this section, we describe previous attempts to handle the above-mentioned four requirements. First, we discuss individual design-oriented approaches. Then, we evaluate larger theoretical frameworks.

## Design-oriented approaches

Bardram (2004, 2005, 2006) describes pervasive tools for supporting mobile hospital work. The research uses activity theory (see later) and is therefore based on the idea that Subjects (users) change their work Object by using an assortment of Mediators (materials, tools) within a delimited spatial–temporal context. A main idea is that activities must be represented explicitly in the system:

User activities become first class entities that are represented explicitly, and activities are inherently collaborative, treating single-user activities as collaborative activities that just happen to have only one participant (Bardram, 2004, p 166).

## Moran (2005) proposes a comparable solution:

We hypothesized the need to explicitly represent activity as a computational construct and to provide an infrastructure to support it (Moran 2005, p 2).

Moran’s motivation is not tied particularly to pervasive technology, but to the general observation that we tend to organise our work in activities and that this organisation is not supported by existing software. In Moran’s model, activities involve actors playing different roles; in addition, there are artefacts, tools, and subactivities.

Both Bardram and Moran argue for a dynamic model that lets the user start, suspend, resume, end, enter, and leave activities. The idea is, on the one hand, that such models can help users by displaying the resources needed at the current stage of the activity, and, on the other hand, can help users plan and reflect on their activities.

Kristensen (2002, 2003) in the same way argues that associations should be a first-class citizen in pervasive applications, and points out that this may create a problem in traditional object-oriented design: one tends to model things as objects, and activity parts as methods of the objects. This spoils activities since their parts have to be distributed to the objects that participate in the activities.

The following example, where two ships negotiate how to pass one another, illustrates his point. Via VHF radio, the ships can arrange to sail starboard-to-starboard or port-to-port if they sail towards one another and port-tostarboard if one is overtaking the other (see Table 1).

## Table 1 Negotiating passage of two ships

S. Atlantic Sally Mærsk, the Sealand Atlantic [call up]

Pilot Sally Mærsk [acknowledge]

S. Atlantic Yeah, good afternoon captain, are you turning to port now, are you, over? [greeting+question]

Pilot Yes, I’m turning slowly to port, yes [answer]

S. Atlantic Okay, we, we are, we will be steering our course of about two nine zero, and we will stay to the north of you, if that is agreeable with you [promise]

Pilot Yeah fine, I will be following the deep draft route outside [acknowledge+promise]

S. Atlantic Yeah, and can you give us a red to red passing, please, port to port [propose passage]

Pilot Port to port, yeah fine okay [accept proposal]

The activity involves methods like Call up, Acknowledge, Propose passage, Accept proposal, and Reject proposal. The methods are interdependent; for example, proposing a passage presupposes you have called up, and accepting or rejecting presupposes a proposal has been suggested. However, these dependencies will be hidden inside the methods, and thus not be explicit, as shown in Figures 1 and 2. UML offers abstractions for modelling collaborations between objects, but they will not be explicit in the programme if you do not use special design patterns (Gamma et al., 1995).

In line with Moran (2005), Kristensen suggests that objects representing participants of an association should be linked to objects representing their roles, which again are linked to the association itself.

Thus, the activity–role–participant schema recurs in these approaches. The role-component is particularly emphasised by Herrmann et al. (2004), which investigates the use of a web-based collaborative learning environment. They suggest that support for managing roles is helpful in such applications.

Roles are also used in the ORM method (Object-Role Management; Halpin, 1996, 1998). The ORM model (Halpin, 1998) is an alternative to traditional Entity-Relation and Object-Oriented modelling and consists of a set of objects that play roles. It focuses on databases, design, and querying, and has strong formal properties, for example, formalised conversion to ER/OO/SQL. According to Halpin (1996), it only handles the static properties of a model (although various ORM extensions have been proposed for process and event modelling), but since we need to represent the execution of activities, for the reasons mentioned by Moran, Bardram, and Kristensen, we will define a dynamic model too (cf. also Bækgaard, 2001).

![](/api/attachments/BZG4YBFK/fulltext/images/1d5ee0d2dff3334fd0804fd671937cc9b007178823b1ce5a9383982feae7ace1.jpg)  
Figure 1 Two ships passing.

![](/api/attachments/BZG4YBFK/fulltext/images/279e7c1d93b673f07593746e971a990a5f3d6b11d6f04e182eb315be38f1e0d7.jpg)  
Figure 2 Implicit dependencies between methods.

The attractiveness of the role-notion is probably due to the fact that we use a small set of roles when we speak about activities. This, at least, is what the linguistic theory of semantic roles claims. The theory goes back to antiquity, but was revived by Fillmore (1968, 1977). An overview of the theory can be found in Blake (2001). Technical applications of semantic roles are discussed in Jurafsky & Martin (2000), and a critique of the theory can be found in Valin & LaPolla (1997). Sowa (2000) uses semantic roles in his conceptual graphs, a knowledge specification language.

The term semantic role should not be confused with the term syntactic role. A syntactic role like subject, direct object, and indirect object denotes the way phrases behave in the sentence: Which are the prepositions or inflections used? Where are the phrases placed? How can they be moved? In opposition to this, a semantic role denotes the relation the participant plays in the activity: an Agent, for example, is the active participant who initiates and controls the activity and the Patient is the passive participant that undergoes the largest change.

The example in Table 1 illustrates the notion: the activity of two ships passing one another consists of two actions:

1. Ship A passes ship B starboard-to-starboard or port-toport at time T.

2. Ship B passes ship A in the same manner at time T.

In (1), ship A plays the role of Agent since it initiates and controls the action, whereas ship B is a Location that must be avoided. ‘Starboard-to-starboard or port-to-port’ describes the Manner in which the action can be performed. In (2), ship B is the Agent, ship A is the Location, and the Manner is the same.

Using the theory of semantic roles has two advantages: it provides a unified description of all the elements of an activity, actors, mediators, space, and time, and if semantic roles are used as a data structure, it makes the activity verbalisable and thereby understandable, cf. a similar argument made by Parunak (1995) for using semantic roles in specifying computational agents. The reason for the latter is that there exist linking rules, relating semantic roles to syntactic roles and thereby to well-formed sentences (cf. Andersen, 2004b).

Semantic roles are one of the two concepts that build the foundation of this paper. The other concept is the sign concept that is introduced below.

The third requirement above, that we want to be able to bind (parts of) activities to specific times and places, raises two questions: What do we mean by ‘place’ and What does it mean that activities are ‘bound’ to a place? Harrison & Dourish (1996) distinguish between space and place. ‘Space is the structure of the world; it is the threedimensional environment, in which objects and events occur, and in which they have relative position and direction’ (Harrison & Dourish, 1996, p 2), whereas ‘a place is a space which is invested with understandings of behavioural appropriateness’ (Harrison & Dourish, 1996, p 3). Space provides the constraints and opportunities for creating places. It is places, not spaces, that regulate our behaviour and, for example, prevent us from dancing in a conference auditorium. Harrison & Dourish (1996) tend to separate space and place by positing virtual space-less places; Brown & Perry (2002) criticise this because, as they say, users are still in the physical space of their computer even if they work in the virtual digital place. The place concept corresponds to the notion of locales in Giddens (1995) and has strong connections to the notion of affordances in Gibson (1986). Gibson claims that what we perceive is not the physical space, but places that offer action possibilities to us. Thus, when we see a chair, we see something we can sit on, and not a particular geometrical object.

We use the second founding concept, the sign concept, to describe the relationship between space and place. A sign is a relation between a representation (sometimes called a signifier), something represented (sometimes called the signified), and an interpretation (for example, a reaction to the sign). All three elements must be present in the sign. If we let space play the role of the representation, place the role of the signified, and appropriate behaviour the role of interpretation, then we come to accept Brown & Perry’s claim that place should not be divorced from space, since without the space we would have no signifier representing the place. A place is thus simply an interpreted space, and the interpretation includes behavioural opportunities and constraints. For example, the physical differentiation between a roadway and a footway is interpreted as signifying places for cars and pedestrians, respectively. The behavioural constraints include those described in the Road Traffic Act. The precise bindings between activities and places are described by means of the semantic roles, which places, actors, artefacts, and information sources can play in the activities afforded by the place. For example, humans, not cars, are allowed as Agents of movement activities on footways. This conception of places and the bindings between places and activities is called a habitat in Section 4.

## Theories and communities

In this section, I shall discuss three theories/communities where notions like activities, roles, participants, and communication have been in focus.

The language action perspective (LAP) community is inspired by the works of John Searle and Ju¨rgen Habermas on communicative actions. The approach to artefact design in Winograd & Flores (1986) has also been an inspiration to the community. LAP basically views use of IT as the execution of speech acts mediated by technol ogy. The notion of speech acts is also central to this paper, but we need to extend the concepts to also cover noncommunicative ‘material’ acts and the relation between the two. The LAP community has emphasised the communicative type, but to a certain degree failed to realise that communicative actions are intertwined with material acts in actual work processes. There is therefore a need to build an integrated theory that encompasses the two (Goldkuhl, 2001). The bias towards communicative actions can, for example, be seen in the DEMO method described in Dietz (2003). Dietz offers a finely grained typology of communicative acts (request, promise, decline, quit, state, accept) but only distinguishes between few material acts. The reason is that technical systems are seen as social systems and understood in this way. Communicative acts are thus used as a metaphor for physical processes, but no arguments are given for this position. Another problematic feature, which is also noticeable in DEMO, stems from Winograd & Flores (1986): conversation patterns tend to be described in temporal terms, one act comes before or after another act, like in a finite state automaton. In this paper, I shall present a more detailed analysis that describes how participation in one activity affects the participants’ abilities, rights, desires, or obligations to participate in other activities. Thus, dependencies between activities are tied to the organisational or individual effects participation has on the participants. Furthermore, since there is no reason to assume that physical systems behave like social systems, I present a framework that is neutral to these distinctions.

Activity theory: Activity theory originated from the dialectical materialist psychology developed by Vygotsky and his students in the Soviet Union in the beginning of the 20th century. Activity theory goes beyond the popular human–machine dyad and insists on cultural and technical mediation of human activity. Therefore, the unit of analysis includes technical artefacts and cultural organisation, and the focus of activity theory is wider than what has been the core concern of past HCI research (Bødker & Andersen, 2005). But activity theory seems to have the opposite problem of the LAP community: it emphasises material activities where a Subject applies a tool to change some Object; only recently, spoken and written discourse has begun to figure as mediators in activity theoretical analyses of work, and the effort to explore its role as mediators has been limited (Wells, 2002). The present paper has borrowed the notion of activity from activity theory but differentiates its three basic concepts, Subject (E Agent), Mediator (E Instrument), and Object (E Patient), by means of the theory of semantic roles. The reason is that otherwise important parts of the activity would fall outside the theory. For example, transportation involves a Source and a Destination, and a lawyer acts on behalf of his clients – the role of Beneficiary. Most problematic, communication could not be described since the Addressee role is not comparable to the role of Object of the activity. Splitting firewood is fundamentally different from talking to a person.

Actor network theory (ANT): ANT is not a real theory but rather a number of related methodologies and assumptions (Law, 1987; Latour, 1999) focused on empirical ethnographic fieldwork. The present paper is obviously inspired by this tradition with its emphasis on the significance of networks and relations and its (structuralistic?) insistence that participants in the network primarily acquire their properties from their position in the network. I deviate from the tradition by claiming that it is possible to refine the vague concept of ‘actor’ into a set of more precisely defined roles in a network. Another deviation is that our framework is biased towards design of pervasive technology, which is not the case with ANT.

## Summary

Each of the approaches described above offers valuable insight into delimited aspects of the type of worksituation we want to understand, but there is no consistent framework in which the individual observations and concepts can find a place. For example, the LAP tradition is good at describing communicative actions but lack concepts for material ones, and activity theory has the opposite problem. The important role of space/ place is convincingly argued by some authors, but the relation between activities and space is only sketched. In the following, we shall present a framework that attempts to remedy some of these defects, using the two basic concepts, semantic roles and signs.

## The specification language

In defining a language for handling these questions, I rely on classical structuralism, since here, relations are more important than things (Hjelmslev, 1963). In fact, linguistic ‘things’ like tones, morphemes, words, etc. are defined by the relations they contract to one another. From a structuralist point of view, the basic concept in the specification language should therefore be relations of some kind. In this connection, we choose the activity as the basic unit. It consists of a set of interconnected actions with associated roles subsumed under at common purpose. Things and persons can fill these roles and acquire their main characteristics from this. Since activities contain connected actions, things will typically fill roles in several activities. In Figure 3 that represents the events of Table 1, Sally fills the Agent role in her part of the passage and the Location role in Sealand’s part, and conversely for Sealand’s action part. Finally, the two parts of the activity share the Time filler: it is now.

The term activity is used more or less as in activity theory (Bødker & Andersen, 2005): according to Vygotsky (1962), human activity has three fundamental characteristics; firstly, it is directed towards a material or ideal Object (in Figure 3, the Object is to avoid collision); secondly, it is mediated by artefacts (which are the VHF radio and the standard equipment of maritime bridges); and thirdly, it is socially constituted within a culture (which in this case is the IMO traffic regulations plus non-regulated norms of good seamanship). Thus, there are three fundamental roles— the Subject; the Object; and the Mediator. However, as mentioned in ‘Theories and communities’, I need a broader repertoire of roles – Time (in the example now) and Location are necessary of course, but so are Source, Destination, Beneficiary, Agent, Instrument, Patient, Path, Material, and Result.

![](/api/attachments/BZG4YBFK/fulltext/images/db0b38f5da1c3a2be0c83d507613c9cadf85b4e3dd695f8d56717495f3134bd9.jpg)  
Figure 3 Activities. Obl ¼ obligation.

An example for this is the following description of organisational actions, where Agent, Result, and Beneficiary are important roles:

Organizations [Agent] create products [goods or services, Result] beneficial for their environment [Beneficiary]; i.e., for their customers or clients Goldkuhl & A<sup>˚</sup> gerfalk (2002, p 95, my brackets).

Another example is flow-oriented activities that consist of actions of the form Agent transports Object from Source to Destination, for example, ‘The conveyor belt (Agent) transports ore (Object) from the storage yard (Source) to the furnace (Destination)’. Flow diagrams often pick out the Source and Destination roles and code them visually by means of boxes and arrows (Lind, 1994; Andersen, 2004b).

As mentioned above, I borrow these additional roles from linguistic theory. Although there is a correspondence between the psychological and the linguistic ones (the Subject is often coded as the Agent, the Mediator often as the Instrument, and the Object often as the Patient), they are defined differently and sometimes there is no one-to-one correspondence between the concepts we use when we act and when we talk (cf. again Bødker & Andersen, 2005).

The semantic roles are only valid with simple actions. To whole activities, we conventionally associate macroroles or positions. A macro-role denotes the way a participant can partake in a set of simple actions. For example, the give-way role in the passing of two ships is required to be the Agent of actions like slow down and change course.

Most actions live a large part of their life in an uncompleted state, with missing role fillers, or fillers that may not be well qualified for playing their role (Andersen, 2004a). For example, a captain may know the harbour he is heading for, but not the exact berth he is going to have, one of his echo-sounders has lost track of the seabed, or rain is cluttering the radar.

Another example of partially filled roles is advertisements. They can have the form Agent buys Object from Source for Price, where all roles, except the Agent has been filled out. The purchase can only be executed when someone assumes the obligation to fill the Agent role.

A participant may have conflicts with filling a role; for example, it may be obligated but not able to fill it, or it may be desire to fill it but be prohibited to do so. A train for example is obligated by the timetable to arrive at a certain station at a certain time, but may be unable to do so because of engine trouble or because other trains are delayed and use the rails. Or a trucker wants to get to his destination fast but is constrained by the traffic regulations.

If we are to produce realistic descriptions, we must therefore allow for incomplete, suboptimal, and conflictridden actions.

In order to model these phenomena, we add the notion of glue. Glue describes the relationship between filler and role along several dimensions: useful dimensions are ability, obligations, rights, and desire (Ryan, 1991).

Basically, glue is used to describe the probability of a participant successfully filling a role. In the example in Figure 3, both ships are obliged to participate as Agents in the passage agreed upon, after having had the conversation in Table 1.

But the concepts are not confined to communicative activities; they are also applicable to material actions. An example, lawn mowing, is shown in Figure 4. The activity requires an Agent (me), an Instrument (a mower), and a Patient (the lawn). If my desire is low, the probability of me filling the Agent role is low, but it can be counteracted by my being obligated to do it (what will the neighbours say?), which increases the probability. The mower has no desires, but it has abilities: if the sparking plug is sooted, its ability to start is low, and so is its chance of playing the role of Instrument in the mowing activity. Finally, the grass of the lawn may be so high that it is unable to participate as the Patient in the activity.

The representation in Figure 4 describes an interpreted material action. It is interpreted since its components have been assigned to roles that make sense to us in the present activity, but in other circumstances could have been assigned to other roles; however, it is still a material, non-communicative action since its purpose is not to influence the beliefs or attitudes of an Addressee but to shorten the length of the grass. Note also that the interpretation needs not to be ‘naı¨ve’ but can rest on scientific grounds. We shall later give, an engineering example of flows of mass and energy based on the physical laws of conservation of mass and energy.

![](/api/attachments/BZG4YBFK/fulltext/images/9b8b7f5735e63fed6a817377d9cc5ad97b22c66ecbe4ce121300995051efb2c4.jpg)  
Figure 4 Lawn mowing: The agent is obliged but does not feel like participating [ þ obl, des]; the lawn is able to participate [ þ abil]; but the mower cannot be started [abil].

Figure 3 showed how the passage of the two ships looks in this framework: the activity consists of two actions, a ship passing another ship to port. The Agent, Location, and Time roles in the actions share fillers: the Agent of one action is the Location of the other, and they share the Time. According to the definition in Schmidt & Simone (1996), this makes it a cooperative activity:

Cooperative work is constituted by the interdependence of multiple actors who, in their individual activities, in changing the state of their individual field of work, also change the state of the field of work of others and who thus interact through changing the state of a common field of work (Schmidt and Simone, 1996, p 158).

Since the lawn mowing in Figure 4 does not feature two or more Agents that change the fields of work of one another, it is not a cooperative activity. The existence of shared fillers can thus be used to diagnose cooperative activities.

The next question to ask is, How was Figure 3 created? In the example, it is very clear: the obligation glue was created by the preceding negotiation in Table 1. How do we represent this?

## Changing activities

As shown in Figure 5, when captain 1 proposes to captain 2 a passage port-to-port, he creates an obligation in captain 2, the Addressee, to either accept or reject the proposal, that is, an obligation to become the Agent of the speech acts of rejecting or accepting. Furthermore, fulfilling this obligation for one of the options will destroy his obligation to perform the other option. Finally, if he performs the ‘accept’ speech act, this creates an obligation for him to materially pass the other ship to port. Specifically, the probability of the captain filling the Agent role of the action of ‘passing to port’ is increased and in addition, he becomes liable to reprimands if he fails to do so.

![](/api/attachments/BZG4YBFK/fulltext/images/bde2846d11e5265d7509cf1d8ecc5805ee51970acb78dde084d592bd84eaebfd.jpg)  
Figure 5 Creating activities. [+obl] means that participating in a certain role in one action increases the obligation to participate in a certain role in another activity. The same applies for desire, ability, and right.

The role ‘Reference’ in Figure 5 means that the role is filled by a representation that is intended to be interpreted as a referring to another action than the one it is part of. Language commands a host of constructions to express this structure: embedded sentences, infinitives, ing-forms, nominalisations, etc. Halliday (1994) proposes roles such as phenomenon and verbiage to account for this phenomenon, while Jurafsky & Martin (2000, p 609) suggests the role-name content.

Dependencies between material activities can be described in the same way. For example, repairing the defect lawn mower from Figure 4 can be described as follows: if the mower participates as Patient in a repair activity using a wrench, it increases its ability to participate in the mowing activity as Instrument (Figure 6)

Note that the effects of speech acts (Figure 5) and material acts (Figure 6) are described in exactly the same way: a change of glue. This means that the relationship between communicative and material actions is well defined.

The two examples also illustrate the general idea that new activities are created and made executable by the participants participating in other activities! The outcome of participating in an action is thus a list of changes of glue belonging to other actions. If we want to represent this in an information system, using an object-oriented framework where actions are full-blown data objects (as in ‘Previous work’), we can do it in the following way:

## Action propose

Roles: Agent, Addressee, Reference.

Execute

Generate a new rejection action with the same Reference as my Reference

<table><tr><td>Agent</td><td>Action</td><td>Patient</td><td>Instrument</td></tr><tr><td></td><td>mow</td><td>lawn</td><td></td></tr><tr><td colspan="4">[+ability]</td></tr><tr><td>Agent</td><td>Action</td><td>Patient</td><td>Instrument</td></tr><tr><td></td><td>repair</td><td></td><td>wrench</td></tr></table>

Figure 6 Repairing the lawn mower.

Generate a new accept action with the same Reference as my Reference

Send message to my Agent-role: ‘increase obligation of your filler to become Agent of the rejection action’

Send message to my Agent-role: ‘increase obligation of your filler to become Agent of the accept action’

End Execute

end propose

## Action accept

Roles: Agent, Reference, RejectReference.

Execute

Send message to my Agent-role: ‘increase obligation of your filler to become Agent of my Reference’

Send message to my Agent-role: ‘decrease obligation of your filler to become Agent of the RejectReference’

End Execute

end accept

The ability to account for communicative as well as material activities is necessary since they are mixed in the maritime domain (and in many others). In addition, it is necessary to account for the way communicative actions influence material ones, and conversely. This is done in accept by allowing a material action to fill the Reference role and by letting accept influence the glue of this action.

The examples also show how the dependencies between actions in activities are described:

 Action A depends upon action B iff the glue of action A is modified by executing action B.

In the pseudo-code above, glue change is described as message passing between fillers, roles, and activities in the manner of Kristensen (2002, 2003). The arrows in Figure 5 [+obl] are thus viewed as denoting message passing to role fillers.

In the following, I shall use various abstractions of the basic diagramming techniques shown above. The reason is that activity diagrams are not only scientific tools but are intended as representations that should help people keeping track of their tasks:

Activity descriptions are social artefacts that support the management and execution of work (Moran, 2005, p 5).

In such uses, precision may be a nuisance if it tells people what they already know. For example, Taxe´n & Lillieskio¨ld (2005) describe an anatomy diagram that has been used for over 250 projects at the Swedish Ericsson Company. The diagram is not very precise and yet it works because it leaves out features its users knew anyway and focuses on coordination and timing features that are difficult to handle.

Figure 7 shows an abstraction of Figure 5.

The abstraction is made in the following way:

 The participants, roles, and glue changes responsible for the dependency between the actions are stripped away.

 Abilities and rights are merged under the heading possibility and represented by a single-headed arrow -

 Desire and obligation are merged under the heading necessity and represented by a double-headed arrow .

 Inability, prohibitions, and loss of obligations are merged as impossibility and represented by .

Figure 7 only says that the proposal makes two other actions, rejection or acceptance, mandatory, that accepting makes rejecting impossible and triggers the material action of passing port-to-port, and that rejecting makes accepting impossible. A lot of information is lost, but the main dynamics stands out more clearly.

![](/api/attachments/BZG4YBFK/fulltext/images/f28a2cbbb9021f54f4180d87bff27a4ca29fa33ca3da45ec9f49f50ada82661e.jpg)  
Figure 7 Another coding of Figure 5.

In other cases, we may wish to add more detail to Figure 5. Figure 5 only says that a request increases the obligation of the addressee to undertake some action. If we want to focus the indirect nature of speech acts emphasised by Posner (1993), we must add cognitive activities to the description, for example, that the speaker intends the addressee to realise that the speaker intends his utterance to make the addressee do the action requested – and hopes that this will actually make the addressee comply with the request. Representing this will require us to add the semantic role of purpose and enter cognitive processes like realising and believing.

In order to illustrate the concepts in a design-oriented context, I introduce an example that will be used in the rest of the paper. The purpose is to design a train information system that exploits pervasive technology. The purpose is, on the one hand, to enhance the existing information system directed towards the passengers and, on the other hand, to make the sales and control functions more efficient.

The railroad example (1): the travel activity consists of at least the following actions: the passenger buys a ticket from the railroad company (RC) and boards the train at the departure station at the departure time. RC drives him from departure to destination while informing him of the progress of the travel. At the destination station, the passenger leaves the train. The action dependencies are as follows: buying a ticket entitles the passenger to become the Agent of the boarding action, the Beneficiary of the driving and the informing events, and obliges him to be the Agent of the leaving action. The RC is obligated to make the train available for the boarding action and to deliver the information; finally, it gains the right to be left at the departure station.

## Agency

This section discusses the substitution of human and non-human participants that is so frequent in maritime work and in process control generally. The substitution is easily described in the framework by allowing humans as well as non-humans to play the Agent role. But does it make sense?

Here is an example of this interchange. When a ship leaves a harbour, the following happens: in the beginning, captain, helmsman, and pilot cooperate to maintain the course and keep the ship on track. When traffic decreases, the activity of maintaining the course is delegated to the autopilot, and in open sea the whole activity of keeping the ship to the track may be delegated to the voyage management system (VMS). Thus, humans are regularly replaced by automation in the activities of maintaining the course and in keeping to the track. Should we say that the humans and machinery replace one another as fillers of the Agent role?

In ANT, this is an uncontroversial analysis, since the theory endorses the principle of symmetry: non-humans like an autopilot can be agents in the same way as humans (Law, 1987, p 132). However, this is not the whole truth: although the crew places the VMS as the grammatical subject like a human, and say ‘You can just put it in ‘Nav’ Mode, then it sails by itself’, the operation procedures treat humans and non-humans differently: the more complex the manoeuvre is, the more manual should it be. Thus, although discourse treats humans as well as non-humans as Agents, actions differentiate.

In Activity Theory (Bødker & Andersen, 2005), one would say that the autopilot represents crystallised human operations that can be activated in their mechanical form. In this theory, one would tend to reserve the Subject/Agent role for humans and view machinery as an Instrument. However, this analysis does not capture the fact that the signals sent to the autopilot by the officer in manual mode and by the VMS in automatic mode are exactly the same, and that the strategy of the two participants is comparable if not the same.

In the framework presented here, a possible solution is the following: the ability dimension of the glue binding officer and VMS to the Agent role is comparable (although the two parties may use slightly different tactics for keeping the ship on track), whereas the obligation dimension differs. In case of failure, the blame tends to fall on the officer, not the VMS (maritime accident reports blame the human operator in a vast majority of cases). This is one of the benefits of the glue concept: one does not have to accept complete equivalence or complete separation between humans and nonhumans. It becomes possible to say that in the ability dimension, their function as Agents is comparable, while it is very different in the obligation dimension.

Another relevant point is that semantic roles are functional concepts: they describe how participants function in the activity but do not say anything about the ‘internal’ implementation of these abilities. Who- or whatever is able to play the role of Agent in a competent way under the current circumstances can function as Agent. Therefore, assigning the autopilot to the Agent role in the activity of maintaining the course outside the harbour implies neither that autopilots and officers use the same methods to maintain the course, nor that the autopilot can also maintain the course inside the harbour. It just means that under the circumstances, both are qualified.

A consequence of this approach is that management consists of the same simple process regardless of the nature of the participants – humans or non-humans – namely changing the glue between participants and the Agent role: with human agents, assignments to tasks consist in increasing the obligation, right, and ability of the human to participate in the task; with non-human agents, only the ability is increased. In modern organisations, which comprise networks of humans as well as automatic systems, this viewpoint is an advantage.

The railroad example (2): in (1) it was suggested that the company drives the passenger. Clearly, this is a metonymi. In reality it is the train or the conductor that plays the role of Agent.

If the information system is connected to a resource management system, we need to make a finer grained description where a delegation of responsibilities is described. The company requests someone to request someone to y request the conductor to make the train available at the departure platform and to perform the actual driving. Chains of command can be represented as a chain of requests Agent requests Addressee to do Action where Addressee<sub>i</sub> ¼ Agent<sub>i þ 1</sub>and the action can be a new request.

## Execution

What causes an activity to execute and what does an execution consist of?

The latter question has already been answered in ‘Agency’. Execution of activities consists of the following:

(1) Change of the glue between fillers and roles in actions.

(2) Creation and deletion of actions.

A natural way to conceptualise execution of actions is that the fillers change properties. However, if we are to stick to structuralism, this is not a possible answer. Instead, we can add a history to representations of things, describing the past actions, in which the things have participated and the current state of unfinished activities (implemented as the usage store in Bardram, 2005). Later, we shall add affordances to things describing the future actions they can participate in.

A history has obvious uses. For example, a participant may be obligated but not yet able to execute an action because it requires the participant to be close to another participant. This could be implemented as a ‘to-do’ list whose items are brought to the attention of the user when he becomes able to perform the action. For example, a doctor is obliged to examine a certain patient, but only when he approaches her bedside, the locationsensitive PDA suggests resuming the treatment activity for the patient in the bed (Bardram (2006, p 9).

The question of when an execution occurs is a bit complex. The reason is that actions may be incomplete now, and only become completed at a later stage or that some fillers are suboptimal. One possible rule could be:

An action executes if and only if

(3) All fillers are able to fulfil their roles to some degree.

(4) The Agent filler is strongly obligated and/or strongly desires to fulfil his role.

The execution model implied by these rules is not a sequential one. Rather, there is an agenda of more or less executable actions, each of which is executed when (3) and (4) are fulfilled. For example, in Figure 5, when the proposal has been made, the addressee is obligated to reject or accept. But as long as he has not decided (i.e., the desire/intention component is too low), none of them are executed. Only when the decision has been made and the desire glue is above a threshold one of the options will be realised. In the example with the doctor doing the rounds in the hospital, the obligation and desire component may be in order, but the ability component is only increased when he approaches the bed. Only then, the action will execute.

The railroad example (3): when a passenger buys his ticket, only rights and obligations are distributed as described in (1). At this time nothing is known about abilities. The train information system contains a list of all instances of travel activity representations (itineraries) involving the train. The passenger’s ticket is stored on a device that can communicate with the train’s information system, e.g. a RFID tag or his cell-phone. When the passenger enters the train, a sensor reads the ticket. The system now knows that the passenger is able to enter the train, and if he is allowed to do so too according to his travel activity, the system increases his ability to participate in the digital boarding action and executes it. This enables the passenger to receive travel information, and, since he is entitled to do this, the information activity is started. The principle is: participants are represented by mobile information sources and activities are maintained in the habitats offering them. A representation of a travel activity is thus executed when sensors have decided that the participant is able to do so because of his physical location and because his itinerary gives him the right.

## Creating, suspending, resuming, and defecting

Since the actions of the activity are not linearly ordered, the typical pattern is that they are executed when circumstances are right, that is, suspending and resuming activities are the rule rather than the exception. When there is a temporal schedule, as in ward rounds, the time role can be used. Consider, for example, the action Doctor Smith examines Jones between 10 and 12. At 8 o’clock, the current time is not qualified for participating, but as the clock approaches 10, its ability increases. After 12 o’clock, the time’s ability to participate decreases again. Therefore, the action will be executed sometime between 10 and 12.

Multitasking is also easy to present: it simply means that a participant plays the Agent role in more than one activity.

But how are activities created? Many are of course created by verbal means, as in Figure 5, but others are triggered by a specific situation. For example, a heart stop triggers the resuscitation activity in a hospital (Brynskov & Andersen, 2004). An interesting source of knowledge of triggers of maritime activities is the The International Regulations For Preventing Collisions At Sea (IMO, 2002; Force Technology, no year). The rules describe manoeuvres for avoiding collision to a great detail, and here we find the category of Situation detection (cf. also the activity discovery component in Bardram, 2006).

Situations are described in great detail in IMO (2002), because the activity to be executed depends upon the situation at hand: passing vessel head-on, overtaking vessel, or crossing vessel? For example, a head-on situation exist ‘when a vessel sees the other ahead or nearly ahead and by night she could see the masthead lights of the other in a line or nearly in a line and/or both sidelights and by day she observes the corresponding aspect of the other vessel’.

The process of role-assignment is also regulated: for example, if we have a passing situation, the two boats are assigned to the roles of ‘give way’ and ‘right of the way’, depending upon their trajectory and position. In other cases, role-assignment depends upon the history of the participants: in a resuscitation activity there are two roles, the doctor and the nurse, that must be filled, and the selection of participants depends upon their educational history (certified doctor and nurse) and their organisational rights and duties (e.g., the watch schedule).

During execution of an activity, roles can change; for example, in one session of a virtual community, a participant may play the scaffolder that structures the discussion, in the next a regular contributor (Herrmann et al., 2004).

The regular alternation between humans and automation from ‘Agency’ can also be described as a role-change. The rule is that the more complicated the activity is, the more manual it becomes.

All these processes are easy to represent in the framework presented. The next one, defections, requires an addition. Since most things can go wrong, participants may abandon the roles they play during an activity. Human participants may decide not to participate or may not be able to do so any more, and equipment may break. It is necessary for the activity to specify what actions to take, in case its participants do no longer fulfil their roles properly (cf. the idea of raising and catching exceptions in programming languages). When the 10 cm radar does not work, it must be possible to shift to the 4 cm radar. If the officer of the watch falls ill, the dead man’s button should sound the alarm, and action should be taken to replace him. If the ship assigned to the ‘give-way’ role does not give way, the ‘right-of-way’ role must know what to do.

Technical systems in safety critical areas are prepared for such defections. Maritime technology is, for example, often built in levels, with the more automatic levels on top of the more manual ones. When the automatic level fails, the level below has controls that let the officer take over the responsibilities of the automation (Bødker & Andersen, 2005).

The railroad example (4): the traveling activity must contain procedures for cases where the train or the rails defect: the train may be delayed or the rails are used by another train. The passengers should be informed of delays or cancellations and alternative travel routes should be made available to them without extra cost.

## Speech acts and material acts

As noted in the beginning of ‘The specification language’, activities live large parts of their life in an incomplete state. Some fillers may be missing while others are bound too loosely to their roles (lack of ability, desire, obligation, or rights). In still other cases, the filler is not the real thing but only a representation of it. For example, the activity of delivering a product (Patient) to a customer (Destination) may start with an order form containing the product number (the Patient role) and the name and address of the customer (the Destination role). As a part of the work flow, representations are replaced by their references; the product number is replaced by the real product by the warehouseman, and the carrier replaces the name and address by the real customer when he actually delivers the product at the customer’s address (Latour (1999, p 56) describes the opposite process, going from ‘the real thing’, via a multitude of small transformations, to a representation of the thing).

In some activities, the representation stays on until the activity is terminated. For example, the Destination role of a driving activity is filled out by a representation, for example, a map or a written address, until the driver arrives at his Destination. Only then, one can say that the Destination role has come to contain the ‘real thing’. The representation works as a guide to achieve this transformation. Thus, roles can be filled with ‘the real thing’ either by getting hold of the thing or by moving to it.

An information system cannot execute the action of delivering a product to a customer, but it is helpful in executing three types of processes necessary for making the activity executable: (1) it can change the glue binding fillers to roles, (2) it can provide the representations that are later replaced by their references, and (3) it can monitor the current activities and their states and provide representations to the participant that help him remember the next step. In the example, an order increases the obligations of the company to fill the Agent role of the delivery activity (cf. 1), and it fills out the Patient and Destination by representations (cf. 2).

However, the material action of actually delivering the product can only be represented, not executed, in the information system. For example, some haulage contractors use a system where it is possible to monitor the actual movements of the vans by means of GPS (cf. 3). The important function of informing the participants of the progress of their activities poses demands on the representation of the activities. It must be easy to convert the representations into understandable texts or diagrams, and this is where the semantic roles come in handy. By exploiting the linking rules mentioned in ‘Design-oriented approaches’, it is quite easy to convert data consisting of semantic roles into readable sentences or diagrams. An example is the small prototype described in Andersen (2004b). It implemented a Multi-Level Flow Model (Lind, 1994) of a furnace plant and used data structures of the form Agent transports Object from Source to Destination and Agent stores/distributes/blocks/provides/consumes Object from which it produced combined graphical and verbal representations. An example of the diagrams is shown in Figure 8, and when the furnace icon is clicked, the following text appears (slightly beautified): ‘A furnace is an energy storage, to which air transports heat from a burner. Furthermore: the furnace stores the heat, air transports it from the furnace to the furnace walls, and from the furnace to the ore.’

![](/api/attachments/BZG4YBFK/fulltext/images/2fa4e641b4ce07ad42719b115ca6f661d03d4d775a62ec88de49b2f91f17ad81.jpg)  
Figure 8 Multi-Level Flow diagram of furnace plant.

The railroad example (5): The purpose of the design project is to provide better information to the passenger of the progress of the travel. This includes notifying him in good time to get up and walk to the doors, telling him which platform to go to in case of change of trains, and informing him of delays and other possible connections. It also includes giving only information that is relevant to this passenger’s travel. Since the train system contains the current state of all travel instances involving the train and since it knows which passengers has actually boarded the train, the system knows when a passenger is to leave the train and it knows about delays affecting him. Both types of information are communicated to the cell-phones of the affected passengers.

## Habitats

As noted in ‘Previous work’, many activities are associated to habitats, that is, particular physical places where particular artefacts and information sources are available (see Andersen & Nowack (2002), Brynskov & Andersen (2004), Andersen (2004c), and the papers in Qvortrup & Andersen (2004)).

## Activities and habitats

If we are to stick to structuralism, we must classify the place, its artefacts, and information sources according to the role they can play in activities for a particular type of inhabitant. A ship bridge, for example, offers controls and displays that can act as Instruments for the crew in activities such as setting the rudder angle, maintaining the course, and following the track.

Thus, a part of the habitat for maritime officers is given in Figure 9. It says that the wheel and the rudder angle display can be used as an Instrument for setting the rudder angle. In addition, Officer of the watch means that the filler of the Agent role must be the officer of the watch (and not, for example, the helmsman or the pilot). Thus, the action is ‘half-baked’ (Andersen, 2004a); some participants are instantiated and present, while others are absent but still restricted to certain types.

The connection between the activity concept from the previous sections and the habitat concept is straightforward: it is based on the observation that the typical state of an activity is half-baked. We normally do not start with completely empty activities; rather, some fillers are in place while others are lacking. In particular, many activities exist with a default Location filler. Setting the rudder angle must be done from the bridge (Figure 9), and entering a train must be done at a railroad station. The activity of setting the rudder angle comes as a package where the Instruments are wheel and angle display and the Location is the bridge. We do not reinvent the world each time we are to act. Habitats are thus defined as default Location fillers of half-baked activities.

<table><tr><td>Agent</td><td>Action</td><td>Patient</td><td>Instrument</td><td>Location</td></tr><tr><td>Officer of the watch</td><td>set</td><td>Rudder angle</td><td></td><td></td></tr></table>

![](/api/attachments/BZG4YBFK/fulltext/images/c6ea277f37619df5c7f0d674019fc6a2092cc139ea979cca8ef6ff3fe50dc041.jpg)  
Figure 9 Controls and displays as affordances.

The tools and media of the habitat are signs whose physical shape is their signifier; they signify the halfbaked actions they afford (cf. similar ideas in Eco (l977, p 23), where tools are described as signs that signify their function). Although artefacts are ‘things’, they are described by the activities they are able to participate in.

The question is now, how the action possibilities and desires of participants can combine with the affordances of the habitat. One way of posing the problem is that participants as well as habitat specify constraints on the possible actions that can or should occur in the habitat. The participant says: ‘I want to do an action of this type’, and the habitat says: ‘Inside me you can do an action of that type’. The purpose is to construct an executable action with instantiated participants that satisfy both constraints. If we want to represent this in an information system, we can find inspiration in the constraintbased unification method defined in Jurafsky & Martin (2000, 395ff.) where it is used for describing contextual features in language.

The idea in the following is that of supply and demand: the participant demands some executable action, and the habitat offers its affordances. A demand can combine with a supply if they are compatible. If we write an action as a list of roles [[Agent: Officer of the watch], [Action: set], [Patient: Rudder Angle], [Instrument: #wheel], [Instrument: #angle display], and [Location: #bridge]], where # represents an instantiated object (#wheel means ‘that particular wheel’), we can define the result of unifying a demand with a supply in the following way:

1. All role fillers of the demand must match with corresponding role fillers of the supply.

2. A role filler matches another role filler iff they are identical or if one is a member or a subclass of the other.

3. If (1) is not fulfilled, the result is the empty list. Otherwise, the result consists of the most concrete fillers among the demand and supply roles that match plus all the unmatched supply roles.

As an illustration of how this works, consider the following supplies and demands. The supplies from the maritime habitat are as follows.

1. Shoals: Yachts can sail in me, [[agent, yacht], [action, sail], [location, #shoals]].

2. Fairways: Ships can sail in me, [[agent, ship], [action, sail], [location, #fairway]].

3. Lanes: Ships can sail North in me, [[agent, ship], [action, sail], [location, #lane], [direction, north]].

The demands from the ships are as follows.

a. Yacht: I want to sail in water, [[agent, #ship2], [action, #sail], [location, water]].

b. Container ship 1: I want to sail in water, [[agent, #ship1], [action, #sail], [location, water]].

c. Container ship 2: I want to sail south in water, [[agent, #ship1], [action, #sail], [location, water], [direction, #south]].

Supply 1 þ demand A unifies to ‘This yacht can sail in these shoals’ ([[agent, #ship2], [action, #sail], [location, #shoals]]) since this yacht is a yacht and these shoals are water. Supply 2 þ demand A also produces an executable action, ‘This yacht can sail in this fairway’, since this yacht is a ship and this fairway is water. However, 1 þ B does not unify since a container ship is not a yacht. In this way we can allow or forbid participants to execute the actions afforded by the habitat. Container ships should not sail in the shoals because the water depth is too low, but yachts can do it. Note also that some parts of the resulting executable action come from the participant, others from the habitat. This way of combining abilities from agent and environment is useful in designing migrating agents, as argued by Cabri et al. (2004) who also use a role-based architecture. We shall term it contextual execution. The term means that an execution of an action consists of pieces, some of which originate from the participant, while others come from the habitat. This enables participants to act flexibly in different contexts, without having to remember the exact details of each particular context. A technical example of contextual execution is the decoupling of activity-related services from the applications yielding the service described in Bardram (2005).

We get an even better illustration of this principle if we unify 3, ‘Ships can sail North in me’ with B, ‘I want to sail in water’: the result is the action ‘This container ship can sail north in this lane’: [[agent, #ship1], [action, #sail], [location, #lane], and [direction, north]]. In this case, the direction ‘north’ is forced upon the container ship because of the traffic regulations. If the ship’s demand were C ¼ ‘I want to sail South in water’, it would not unify with the lane’s supply since #south is not a member of northbound courses.

The railroad example (6): unification can describe what happens when the passenger matches his demands for travels with the offers of the railroad habitat (e.g. its timetable).

<table><tr><td>Thing</td></tr><tr><td>Identity:...</td></tr><tr><td>History: the past events in which the thing has participated</td></tr><tr><td>Affordances: the future events in which the thing can participate</td></tr><tr><td>End thing</td></tr><tr><td>The repair example in Figure 6 can now be described as follows:</td></tr><tr><td>Thing mower</td></tr><tr><td>Identity:...</td></tr><tr><td>History:was overhauled last spring.couldn&#x27;t start last week-end.</td></tr><tr><td>Affordances: someone can mow the lawn with it</td></tr><tr><td>End mower</td></tr><tr><td>Action repair</td></tr><tr><td>Roles: Agent, Patient (default: mower), Instrument (default: monkey wrench).</td></tr><tr><td>Situation detection: mower won&#x27;t start.</td></tr><tr><td>Role assignment: Agent = owner of mower</td></tr><tr><td>Execution:Send message to Patient: ‘increase the ability of your filler to participate in the filler&#x27;s affordances as Instrument’</td></tr><tr><td>End Execution</td></tr></table>

Suppose the database of the company contains the following offers: Humans can travel from Aarhus to Copenhagen via Odense at 12.00 12/02/05, Humans can travel from Aarhus to Copenhagen via Kalundborg with animals at 13.00 12/02/05, and Humans can travel from Aarhus to Copenhagen via Odense at 14.00 12/02/05. The second one has the formal shape: [[agent, human], [action, travel], [source, #Aarhus], [destination, #Copenhagen], [com, animal], [path, #Kalundborg], [time, #13.00], [date, #12/02/05]], where com is the comitative role (Blake, 2001, p 154).

Mr. Smith wants to know how he can travel from Aarhus to Copenhagen in the afternoon with his dog (formally [[agent, #Smith], [action, #travel], [source, #Aarhus], [destination, #Copenhagen], [com, #dog], [time, afternoon]]). Unification with the database produces one instantiated action, namely the departure via Kalundborg at 13.00 where pets are allowed: [[agent, #Smith], [action, #travel], [source, #Aarhus], [destination, #Copenhagen], [com, #dog], [time, #13.00], [path, #Kalundborg], [date, #12/02/05]]. There are two ways of converting structures of semantic roles to databases. One way is to implement the activity as a table and use the roles to name the columns of the table. The other is to let the roles become tables and add a third argument representing the activity. Thus Destination(#1000, # Copenhagen) means that Copenhagen is the destination of departure #1000. Jurafsky & Martin (2000, 525ff.) present arguments in favour of the latter solution.

Unification is one way to precisely describe the interaction between the demands of the inhabitants of the habitat and its affordances. If we add the notion of history and an indication of the identity of the thing, we end up with the following format for things:

Defections:

if the monkey wrench can’t loosen the plug, use the box spanner as Instrument

if the owner can’t make it work, make the repair man the Agent

End repair

The preceding can be summarised in the following characterisation of the habitat concept along three dimensions:

(1) The physical dimension: a delimited chunk of time space that is designed to support a delimited set of activities. It includes tools (e.g., the wheel and the autopilot on the bridge) and other facilities (e.g., the map-table) for conducting the activities.

(2) The informational dimension: The informational habitat consists of representations referring to topics relevant to the activity. On the bridge, there are maps and displays of rudder angle, course, speed, etc.

(3) The pragmatic dimension: Here, the activities and their role requirements are specified. Officers are allowed one repertoire of actions, ordinary seamen another one, while the captain rules supreme.

## Representing habitats

How should we represent habitats? Since their purpose is to handle activities that are bound to specific locations, the diagram should focus spatial relations, so location fillers must be coded graphically. We use the following map-like conventions (cf. Brynskov & Andersen, 2004 and Figure 10):

The physical dimension: A bold line delimits the physical shape of the habitat. In Figure 10, three embedded physical habitats are shown: an area of the sea where cooperation with the vessel traffic service is mandatory; the ship itself that is used for sailing; and the bridge where navigation and manoeuvring are done.

The informational dimension: Representations are signs consisting of a signifier (representation) and a signified (reference). Therefore, for each representation we indicate the area within which it can be seen or heard (the access area) and the area holding the signified object (the reference area). The areas are marked by dashed polygons and are connected by an arrow pointing from the representation to the represented. Two kinds of references are marked: the full ‘rigid’ arrow represents a relative reference where the distance between access and reference area remains constant, so if the access area moves, so does the reference area. The radar is an example in Figure 10. Its reference area is a circle around the ship that moves as the ship moves. The ‘elastic’ dashed arrow represents an absolute reference: the reference area stays where it is, no matter how much the access area moves. The machine telegraph is an example since its position represents the intended revolutions of the engine. The access area is extremely important on a bridge, where the crew must have a correct understanding of the situation: can the display be seen from all locations? Can it be seen in sunlight and in dark?

![](/api/attachments/BZG4YBFK/fulltext/images/f5a929da1b5be87f8147e62d7fb1e93c6bd369162385986e399c4bdccdc747af.jpg)  
Figure 10 Radar and machine telegraph.

Relative references have the two variants shown in Figures 11 and 12 . In Figure 11, A displays information referring to objects (B) located in A’s neighbourhood (the reference area) and A is inside its own reference area. The radar is a prototypical example. In Figure 12, the reference area is A, and the access area is A’s neighbourhood. Objects (B) in the neighbourhood can thus receive information about A as long as they are in the access area. An example is AIS, the maritime transponder system, that provides both static information like MMSI number (used for VHS radio), IMO number, call sign, vessel name, vessel type, vessel dimensions, and dynamic representations like position, course, rate of turn, speed, and status (e.g., anchored, limited manoeuvrability). Other examples of this type are barcodes and RFID tags that typically contain information about the physical thing they are attached to. The access area is particularly important in relative references because of the variations: barcodes (centimetres), RFID tags (meters), or transponders (kilometres).

Finally, we mark the main signal path with small arrows: in controls, signals mainly travel from access to reference area, whereas in displays, the main signal transmission goes from reference to access area. For example, according to CEI, 1995, the rudder angle sensor will send $^ { \prime } \ S \mathrm { - R S A } , x , A , x , A ^ { \star } h < \mathrm { C R } > < \mathrm { L F } > ^ { \prime }$ to the rudder angle display, where x is a number measuring starboard and port rudder angle and h is the time. If we only consider the annotated arrows, we have a traditional dataflow diagram. We can therefore say that the notation emphasises that data flows represent something. Visually, it upgrades their semantic aspects and downgrades the data aspects, but both are still present.

The pragmatic dimension: We use callouts to associate activity parts to physical locations. For example, on the bridge, one can set the rudder angle, maintain course, and keep to the track.

The three dimensions interact. For example, the decimation of crew size (pragmatic) in the last two bridge (informational). When you can inspect the side of the ship from a remotely controlled camera from the bridge, you do not need a lookout. Access to the engine from the bridge has also diminished the needs for staff, and in Denmark, it has changed the maritime education as well, since bridge officers now need a thorough engineering knowledge.

![](/api/attachments/BZG4YBFK/fulltext/images/4bc81555f33bae4d683071531f94e854fed861d7c5cac48b210135835fba82e0.jpg)  
Figure 11 Radar.

decades was enabled by adding more access areas to the  
![](/api/attachments/BZG4YBFK/fulltext/images/0081d95fbb8826d894340820454897fa882de3ca290146187f2b8b7b75573cda.jpg)  
Figure 12 The AIS transponder system.

The habitat concept is motivated by the fact that physical space, information sources, artefacts, and activities are often connected in practice: physical spaces are designed to support a delimited set of activities and provide information relevant for these activities. However, it is important to remember that not all activities have a default Location filler, and that not all physical spaces are designed to support specific activities. Open water is not a habitat since it is not designed to support any activity. Trafficked coastal areas are often habitats since they provide buoys and landmarks to help navigation.

The railroad example (7): The train has at least three subhabitats involving passengers: the entrance; the isles, and the compartment. The entrance affords boarding and leaving, the isles walking, and the compartment sitting, reading, working, and talking, depending upon the type of compartment. Apart from updating the train information system and functioning as a ticket inspector, the entrance should also offer directions for reaching one’s reserved place and for warning the passenger if he is entering the wrong train.

## Conclusion

Let us conclude by summarising what the framework has to offer, compared to the other approaches mentioned in Section titled ‘Previous work’.

One characteristic is that the framework is based on two simple concepts: the concept of signs, and the concept of semantic roles. These concepts are used to define the other elements in the framework, such as the notion of activities, execution of activities, macro-roles, space and place, habitats, access area, and reference area. In this sense, the paper simplifies, systematises, and connects concepts used by other researchers within a single theoretical framework.

Compared to the LAP tradition and to Activity Theory, it has no bias towards communicative or material activities but offers a method for understanding both activity types and the way they influence one another. This is mandatory in the application areas discussed.

Compared to the LAP tradition, we have used a broader concept of signs. The LAP tradition focuses on the speech act as the main sign vehicle, whereas we add other sign types such as architectural layout, artefact design, and various types of displays. As architectural artefacts, habitats are signs that signify action possibilities in the shape of possible role structures; desired activities are represented in the same way, and this enables us to define a precise method for unifying the former and the latter.

Because of its two fundamental concepts, the approach does emphasise the interpretational aspect of activities and artefacts. Even if material activities can be accommodated, they are viewed as interpreted material activities, and even if data flows can be defined, the paper insists

## About the author

Peter Bøgh Andersen is currently a Professor in the Department Information and Media Science, University of Aarhus. He was awarded his Ph.D. in 1971, a gold medal in comparative linguistics in 1972, and a Dr. Phil. in 1991 all from Aarhus University. He has published over 135 papers on IT systems in organizations, artificial that data flows are representations that mean something. Finally, the choice of semantic roles as the basic representation points to methods for converting these representations to texts and images that are interpretable to users. There is an underlying ethos that complex information systems that are interweaved with our daily life should be made intelligible. Intelligibility plays a role in the ORM methodology, but is not a prominent theme in the other design-oriented approaches.

Compared to the ANT, the framework is more oriented towards design and implementation of information systems. One example is that it standardises the notion of actor to a score of different varieties based on linguistic evidence. Another example is that the activity concept has been presented together with indications of possible digital representations, either in terms of object orientation or in terms of databases. On the other hand, compared to the design-oriented approaches in ‘Previous work’, the framework still needs considerable elaboration before it can yield practical guidelines with respect to possible implementations.

Finally, the method advocated here is realistic in the sense that it considers the normal situation to be one where sufficient information and resources are not available, demands are conflicting, tools break, and humans make errors. In this way, it differs from methods that focus on the ideal – how the system or the work procedures ought to function. The advantage of the realistic method, particularly in safety critical domains, is that one remembers to provide tools for error diagnosis and recovery from faults.

## Acknowledgements

I thank the FUSS group for interesting discussions. The FUSS network is financed by the IT-West organization. I also thank the anonymous reviewers who pointed unclear issues out to me, and to Owen Eriksson and Michael Cooke who took pains to present discussant papers targeting this paper during the ALOIS 2005 conference. The maritime data were collected in the Center for Human–Machine Interaction, funded by the Danish Foundation for Basic Research. Another version of this paper can be found in Proceedings of ALOIS 2005 (eds. P. J. A<sup>˚</sup> gerfalk, L. Bannon & B. Fitzgerald. University of Limerick, Limerick) under the title Things considered harmful.

intelligence, pervasive computing, computer games, multimedia, HCI, communication, and cooperation in organizations, and completed theoretical work in linguistics, semiotics, non-linear dynamic systems, and, recently, activity theory. Most of his research is oriented towards analysis and design of IT systems. One main interest is the crossfertilization of traditional media skills, such as filmmaking, and design of usable interfaces for instrumental systems, such as, for example, maritime

## References

ANDERSEN PB (2004a) Anticipated activities in maritime work, process control, and business processes. In Virtual, Distributed and Flexible Organizations. Studies in Organizational Semiotics (LIU K, Ed), pp 35–60, Kluwer Academic Publishers, Dordrecht.

ANDERSEN PB (2004b) Diagramming complex activities. Proceedings of ALOIS 2004, March 17–18, Linko¨ping, Sweden. http://www.vits.org/ konferenser/ alois2004/proceedings.asp.

ANDERSEN PB (2004c) Habitats: staging life and art. Invited paper for COSIGN 2004: Computational Semiotics, University of Split, Croatia, 14th–16th September. Addenda to A Clarke (Ed): Cosign 2004 Proceedings. Art Academy, University of Split, Split.

ANDERSEN PB and NOWACK P (2002) Tangible objects: connecting informational and physical space. In Virtual Space: Spatiality of Virtual Inhabited 3D Worlds (QVORTRUP L, Ed), pp 190–210, Springer Publishers, London.

BæKGAARD L (2001) Event modeling. In Information Modeling in the New Millennium (ROSSI M and SIAU K, Eds), Idea Group Publishing, Hershey, PA.

BARDRAM JE (2004) Activity-based support for mobility and collaboration in ubiquitous computing. In Proceedings of the Second International Conference on Ubiquitous Mobile Information and Collaboration Systems, Lecture Notes in Computer Science (Luciano B, Ed), pp 169–184, Springer Publishers, London.

BARDRAM JE (2005) Activity-based computing: support for mobility and collaboration in ubiquitous computing. Personal and Ubiquitous Computing 9(5), 312–322.

BARDRAM JE (2006) From desktop task management to ubiquitous activity-based computing. In Integrated Digital Work Environments: Beyond the Desktop Metaphor (VICTOR K and MARY C, Eds), MIT Press, Cambridge, MA.

BARDRAM JE and BOSSEN C (2005) Mobility work – the spatial dimension of collaboration at a hospital. Journal of Computer Supported Cooperative Work 14(2), 131–160.

BLAKE BJ (2001) Case. Cambridge University Press, Cambridge.

BøDKER S and ANDERSEN PB (2005) Complex mediation. Human–Computer Interaction (20)(4), 353–402.

BROWN B and PERRY M. (2002) Of maps and guidebooks. DIS 2002, 246–254.

BRYNSKOV M and ANDERSEN P Bøgh (2004) Habitats, activities, and signs. Proceedings of the Seventh International Workshop on Organisational Semiotics, OS 2004, INSTICC Press, Portugal, pp 128–151.

CABRI G, FERRARI L and ZAMBONELLI F (2004) Role-based approaches for engineering interactions in large-scale multi-agent systems. In SELMAS 2006, Lecture Notes in Computer Science No. 2940(LUCENA C, et al. Eds.), pp 243–263, Springer, Berlin, Heidelberg.

CEI (1995) Maritime Nagivation and Radiocommunication Equipment and Systems – Digital Interfaces, CEI IEC 1162-1.

CHRISTENSEN HB, HANSEN KM, SCHULTZ UP, ØRBÆK P and BOUVIN NO (2004) Architecture Presentations: Experiences from Pervasive Computing Projects at Computer Science. Center for Pervasive Computing Report Series Publication CfPC-2004-PB-1, Department University of Aarhus, Denmark.

DIETZ JLG (2003) Designing technical systems as social systems. In Proceedings of the Eigth International Working Conference on the Language-Action Perspective on Communication Modelling (LAP 2003) (WEIGAND H, GOLDKUHL G, de MOOR A, Eds), July 1–2, 2003, pp 187– 207, Tilburg, the Netherlands.

ECO U (l977) A Theory of Semiotics. The Macmillan Press, London.

FILLMORE CHJ (1968) The case for case. In Universals in Linguistic Theory (BACH E and HARMS RT, Eds), pp 1–90, Holt, Rinehart and Winston: London, New York, Sydney, Toronto.

FILLMORE CHJ (1977) The case for case reopened. In Syntax and Semantics: 8. Grammatical Relations (COLE P and SADOCK GM, Eds), pp 59–81, Academic Press, New York.

instruments. He has authored three books and co-edited six books. He is co-editor of the journal Systems, Signs, and Actions.

FORCE TECHNOLOGY (no year) Rules of the Road Course. CBT system.

GAMMA E, HELM R, JOHNSON R and VLISSIDES J (1995) Design Patterns. Elements of Reusable Object-Orientered Software. Addison-Wesley, Boston.

GIBSON JJ (1986) The Ecological Approach to Visual Perception. Lawrence Erlbaum, Hillsdale, NJ/London.

GIDDENS A (1995) The Constitution of Society. Polity Press, Cambridge.

GOLDKUHL G and A<sup>˚</sup> GERFALK PJ (2002) Actability: a way to understand information systems pragmatics. In Coordination and Communication Using Signs: Studies in Organizational Semiotics 2 (LIU K, et al. Eds), pp 85–113, Kluwer, Boston/Dordrecht/London.

GOLDKUHL G (2001) Communicative vs Material Actions: Instrumentality, Sociality and Comprehensability. CMTO Research Papers No. 2001: 06. Centre for Studies of Humans, Technology and Organization, Lindko¨ping University, Lindko¨ping.

HALLIDAY MAK (1994) An Introduction to Functional Grammar. Edward Arnold, London.

HALPIN T (1996) Business rules and object role modeling. Database Programming & Design 9(10), 66–72. Quoted from http://www.orm. net/overview.html.

HALPIN T (1998) Object role modeling (ORM/NIAM). In Handbook on Architectures of Information Systems (BERNUS P, MERTINS K and SCHMIDT G, Eds), 1998, Springer, London. Quoted from http://www.orm.net/ overview.html.

HARRISON S and DOURISH P (1996) Replaceing space. The roles of place and space in collaborative systems. In Proceedings of the ACM Conference on Computer Supported Cooperative Work ’96 (ACKERMAN M, Ed), Boston, MA, pp 67–76.

HERRMANN T, JAHNKE I and LOSER K-U (2004) The role concept as a basis for designing community systems. In Cooperative Systems Design (FRANCOISE D, ROSE D, CARLA S and MANUEL Z, Eds), pp 163–178, IOS Press, Amsterdam.

HJELMSLEV L (1963) Prolegomena to a Theory of Language. The University of Wisconsin Press, Menasha, WI (First edition 1961. Translated from ‘Omkring Sprogteoriens Grundlæggelse’. University of Copenhagen, 1943, reprinted and published by Copenhagen: Akademisk Forlag, 1966).

IMO (2002) Convention on the International Regulations for Preventing Collisions at Sea. International Maritime Organization, London.

JURAFSKY D and MARTIN JH (2000) Speech and Language Processing. Prentice-Hall: Englewood Cliffs, NJ.

KRISTENSEN BB (2002) Associative modeling and programming. In Proceedings of the Eighth International Conference on Object-Oriented Information Systems (OOIS’2002) (BALLAHSENE Z, PATEL D and ROLLAND C, Eds), pp 358–371, Montpellier, France, 2002.

KRISTENSEN BB (2003) Associations: abstractions over collaboration. In Proceedings of the 2003 IEEE International Conference on Systems, Man & Cybernetics, Washington, DC, USA, 2003.

LATOUR B (1999) Pandora’s Hope. Harvard University Press, Cambridge, MA.

LAW J (1987) Technology and heterogeneous engineering: the case of Portuguese expansion. In The Social Construction of Technological Systems (BIJKER W, HUGHES TP and PINCH T, Eds), pp 111–134, MIT Press: Cambridge, Massachusetts.

LIND M (1994) Modeling goals and functions of complex industrial plants. Journal of Applied Artificial Intelligence 8, 259–283.

MORAN T (2005) Unified activity management: explicitly representing activity in work-support systems. ECSCW 2005 (European Conference on Computer Supported Cooperative Work), Workshop on Activity: From a Theoretical to a Computational Construct, Paris, 20 September 2005.

POSNER R (1993) Believing, causing, intending. The basis for a hierarchy of sign concepts in the reconstruction of communication. In Signs, Search and Communication (JORNA RJ, VAN HEUSDEN B and POSNER R, Eds), pp 215–270, Gruyter, Berlin, New York.

QVORTRUP L and ANDERSEN P Bøgh (2004) Virtual Applications. Applications with Virtual Inhabited 3D Worlds. Springer Publishers, London.

RYAN M-L (1991) Possible Worlds, Artificial Intelligence and Narrative Theory. Indiana University Press, Bloomington and Indianapolis.

SCHMIDT K and SIMONE C (1996) Coordination mechanisms: towards a conceptual foundation of CSCW systems design. Computer Supported Cooperative Work. The Journal of Collaborative Computing 5(2–3), 155– 200.

SOWA JF (2000) Knowledge Representation: Logical, Philosophical, and Computational Foundations. Brooks Cole Publishing Co., Pacific Grove, CA.

TAXe´N L and LILLIESKIo¨LD J (2005) Manifesting shared affordances in system development: the system anatomy. In Proceedings of ALOIS

2005 (A<sup>˚</sup> GERFALK PJ, BANNON L & FITZGERALD B, Eds), pp 28–47, University of Limerick, Limerick.

VALIN Van RD and LAPOLLA RJ (1997) Syntax, Chapter 3. Cambridge University Press, Cambridge.

VAN DYKE PARUNAK H (1995) Case grammar: a linguistic tool for engineering agent-based systems. http://www.erim.org/Bvparunak/ casegram.pdf.

VYGOTSKY LS (1962) Thought and Language. The MIT Press, Cambridge, MA.

WELLS G (2002) The role of dialogue in activity theory. Mind, Culture and Activity 9(1), 43–66.

WINOGRAD T and FLORES F (1986) Understanding Computers and Cognition. Ablex, Norwood, New Jersey.
