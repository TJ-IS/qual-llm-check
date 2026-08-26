---
otero_id: 23589
otero_key: "UF3X2TXF"
title: "The organization of organizations: issues for next-generation office IT"
authors: "Chris Hutchison; Duska Rosenberg"
year: "1994"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1994.11"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The organization of organizations: issues for next-generation office IT

CHRIS HUTCHISON

Department of Information Systems, Kingston University, Penrhyn Road, Kingston, Surrey KT1 2EE, UK

DUSKA ROSENBERG

Department of Computer Science, Brunel University, Uxbridge, Middlesex UB8 3PH, UK

The emerging new breed of IS (group decision support systems and decision simulation, multimedia, next-generation knowledge-based systems, deductive databases and DBMSs, and such like, together with the evolving networking capabilities) will have a more significant impact on the way people work than have ‘conventional’ IT products. This will have implications for what one might call the ‘cognitive style’ of the user interaction. This paper describes further a view of the organization of organizations that has already been sketched briefly elsewhere (Hutchison & Rosenberg, 1993; Hutchison, 1994), and proposes a strategy for the formal modelling of cooperative group work.

## Introduction

## The scope of the paper

Knowledge-based IS, office networking and groupware, and multimedia – and, more so, the confluence of the three technologies – are rapidly changing the ways in which people, in particular ‘knowledge workers’ in organizations, work with computers; together, they will have a far more significant impact on the way people work than have ‘conventional’ IT products (e.g. word processors, spreadsheets, databases).

First, knowledge-based IS – AI products for the business market such as expert decision support systems and decision simulation, intelligent project management systems, expert system shells, deductive databases and intelligent DBMS – are now gradually gaining broader acceptance within organizations. Unlike ‘conventional’ IT applications, which are unpretentiously tools devoid of agentivity, it is implicit in the design of knowledge-based systems that, more than merely technological innovations, their design crucially and explicitly includes reference to abilities that have historically been seen as exclusively human, such as knowledge processing, intelligence, expertise, problem-solving, as well as the products of these abilities such as problem solutions, explanations, justifications, and so on.

Secondly, multimedia technology (laser disks, desktop CD-I, the Macintosh AV range, etc.), enabling the simultaneous presentation of graphics, photographs, sound, animation, video and text based information, together with the emergence of a wide range of versatile and easy-to-use hypertext and multimedia authoring software packages (HyperCard, ToolBook, Authorware, etc.) and the availability of high quality off-the-peg 'clip media' on CD-ROM, are changing and expanding the ways in which we envisage, present, and interpret information.

Thirdly, ‘workgroup’ computing is moving beyond simple networking (shared resources such as printers and servers; use of electronic mail) towards true computer-supported cooperative working, which may incorporate both knowledge-based technologies (see e.g. Hewett, 1986; Nirenburg and Lesser, 1986; Winograd and Flores, 1986; Malone, 1987) and multimedia (see e.g. Brittan, 1992; Jeffcoate et al., 1993).

These developments in office technology will in turn have implications for what one might call the ‘cognitive style’ of the user interaction – crudely, one does not ‘converse’ with an expert system in the way one does with, say, a spreadsheet, just as one does not ‘walk through’ a multimedia ‘virtual museum’ or a wide-area information server in the way one navigates a conventional database. Against that background, the present paper describes further a view of the organization of organizations that has already been sketched briefly elsewhere by way of theoretical backdrop to studies of cooperation and conflict in CSCW (Hutchison and Rosenberg, 1993) and the role of language in organizational behaviour and IS design (Hutchison, 1994).

Our interest was motivated by the observation that, although the intended beneficiaries of IS are organizations, the actual users are people; the 'bounded rationality' (Simon, 1972, 1976) of the IS user within the cognitive space in part defined and delimited by her formal role in the organization may entail that her personal objectives diverge from the corporate goals of the organization. Poor design of the computer system – one that does not take account of the knowledge, goals, routines and values, the culturally-embedded semiotic, of the real user(s) – may in consequence lead to its under-efficient use or, in the worst case, its abandonment or overt rejection. The central concern that has therefore underlain our work has been to give a principled account of the impact on organizations as socio-cultural entities of the introduction of IS and, in particular, of the new generation of knowledge-based, multimedia, and workgroup IS – we shall call these NGISs. More narrowly, we are above all concerned with the impact on information management of the substitution of a machine-based for culturally-embedded semiotic. By ‘semiotic’, we simply mean a system of signs; by ‘culturally-embedded semiotic’, we intended to identify the specific system of cultural signs by which members of an organization exchange meanings in the context of the work they do. We want to distinguish informally, what one might call ‘cognitive work’ from ‘mechanical work’ – that is, work that involves what is perceived to be agentitive ‘thinking’ or ‘problem-solving’ from simple data-processing work which is executed by computers only in direct response to instructions from a human operator. The vertical line in Figure 1 bisects the domain of information-processing work such as to separate the ‘cognitive’ from the ‘mechanical’ (in reality, the line is not so sharply defined); a core aim of NGIS research is, as it were, to move that line further to the right such that the behaviour of the computer system (the word balloon B) falls increasingly within the ‘cognitive’ area of work. As the line moves, so more of the ‘cognitive work’ done by human beings is delegated to the computer. However the computer remains an intrinsically asocial agent. The effective use of the computer NGIS consequently rests on its production of symbolic behaviour that ‘makes sense’ to, or is ‘readable’ by, the user.

![](/api/attachments/UF3X2TXF/fulltext/images/4a2225185d15d65c844591440472e7bf01739e81e54b22cd9286589bd550d924.jpg)  
Figure 1 Distribution of cognitive work

In that framework, a further informal distinction is made between ‘transparent systems’ (the information is ‘readable’ by the user via a VDU or some other output device) and ‘opaque systems’ (the information is hidden to the user, e.g. bar codes without automatic VDU display); our interest lies in the former $^{1}$ .

The focus of the work is therefore clearly distinguished from studies of the impact of IT on organizations' strategic performance, about which we have nothing to say. The medium-term outcomes of our research are intended to be, in the first instance, at least a better understanding of the process of accommodation of NGISs into the workplace; and if that, then secondly, a set of guiding principles for the enhancement of the user requirements capture and knowledge engineering processes and subsequently for a more supportive human-centred approach to the design, integration and exploitation of NGISs. The longer term goal is the construction of computational models of contextually-situated cooperative knowledge-based working. We consider that formal modelling will be an important and natural extension of our research programme (c.f. Hutchison, 1988; Devlin and Rosenberg, 1993, 1994) $^{2}$ , not only because it will provide a means of explicitly and rigorously testing our theory against already observed scenarios, but also because it will enable exploration of scenarios that have not yet occurred, but in principle could occur, in reality. To put that objective into perspective, a word needs to be said about our view of organizations.

The theory sketched out in earlier papers was in essence fairly simple: organizations in toto may be viewed as distributed knowledge-based information-processing systems, in large part structured and maintained by patterns of (mainly textual) communication, that NGISs are channels for the flow of information between members of organizations and between organizations and their environments, and consequently that NGISs that optimize the flow of information, by non-disruptively enabling ‘natural conversations’ between group members and between the group and the organization, are likely to be preferred by user and consequently to be of greater benefit to the organization and its clients. (Systems that disrupt established work routines will, however apparently ‘conversational’, be dispreferred.) In this respect, there is clearly some degree of overlap between the concerns addressed in this paper and some issues in HCI; however, our present work is more strictly confined to epistemological (e.g. do communicating agents have a common referent for a symbol?), ontological (e.g. how is the choice of domain entities determined?) and representational questions (e.g. is the granularity of the representation appropriate to the task?) We believe that such questions are fundamental to the information engineering (as opposed to the software engineering) stage of NGIS design.

The novel core of the theory was in the distinction made between overt and covert organizational structure – roughly speaking, a static formal description of the structure of organizations and a dynamic process-based description, respectively. (A similar, but not identical, distinction has frequently been made by sociologists between formal and informal organization.) It was claimed that, by taking explicit account of the covert structure, which captures actors' practical reasoning $^{3}$ about their activities, organizational innovation and change (e.g. the integration and exploitation of NIGISs) can be more successfully managed.

The ideas we have drawn upon in our work are in large part not our own and not new; the synthesis of heterogeneous ideas into a cohesive view of organizational structure was novel and undoubtedly contentious, however, and therefore some clarification is in order. We shall not go into any great technical detail in this paper; our purpose for the present is simply to paint a richer conceptual picture of the theory. It is expected that the theory will continue to evolve as we continue our research, and therefore this will not be a definitive statement but rather a description of a research pathway we believe will lead to interesting insights into organizational behaviour, cooperative working and NGIS integration.

## Terminology

One of the difficulties any writer on organizational behaviour is likely to face is that of finding a descriptive language precise enough to convey the exact meanings the writer wishes to express. Words such as 'organization', 'role', 'information', 'structure', 'culture', 'communication', and so forth, carry with them a ragged history of prior usage that may quietly clutter rather than clarify the arguments put forward. One has the choice, then, either of inventing a new vocabulary and defining a new set of terms, or of using an existing vocabulary and then refining and sharpening the meanings of terms as the arguments proceed. Although some novel terms will be introduced in this paper, we have for the most part opted for the second strategy, adopting a typographic convention of flagging technical terms through the use of SMALL CAPS, where our use of the terms is intended to differ from or be more precise than their common usage.

## Organization and culture

## The ontological status of organizations: object vs process

"What is an ‘organization’? It may be argued that the question itself is of little practical interest, though we do not subscribe to that view. It has been argued that, in any case, it is the wrong sort of question, since organizations cannot properly be conceived to exist (or more categorically, ‘really don’t exist’) as entities distinct from the social arrangements of individuals that make them up. There is, for instance, a significant body of literature that would deny their existence in any but a nominalistic sense. Interpretivists, among others, question the very existence of an ‘organization’ (Albrow, 1980; Thompson, 1980) levelling against, e.g. system theories the criticism that

by framing their analyses in terms of organisational tasks or functions, they reify the organisation as an entity, with characteristics independent of the social processes through which organisational members construct and construe social reality. (Thompson, 1980, p. 216)

For much of the time, on the other hand, organizations are fairly clearly experienced by their members, and by those affected by their activities, as 'real' in having properties and powers that are neither those of the collectivity nor of salient individuals (e.g. the chief executive officer, the board of directors, ...). That is, as 'social facts' in something like Durkheim's sense.

There is very possibly no single, straightforward answer to the question, then. What an ‘organization’ is will depend on who is asking and why they are interested. On that issue, Albrow (1980) draws attention to ‘the contribution of social science to structuring the very reality it seeks to analyse’, e.g.

there is ample evidence from its history that organisational study, even where its proponents may have adhered to public claims of value-freedom, has invariably at fundamental levels both implied and contributed to value-commitments and has thereby helped to structure its own subject matter. (Albrow, 1980, p. 278)

The reproach applies as much to ‘folk’ theorists professionally involved with organizations as it does to social scientists, and one might do well to take that as a caution against uncritically espousing this or that definition. Indeed, a plethora of published studies over the past century (e.g. Weber, 1957; March and Simon, 1958; Etzioni, 1970; Parsons, 1970; Silverman, 1970;

Blau and Schoenherr, 1971; Stewart, 1972) has not culminated in any consensual view. As March and Simon (1958, p. 1) put it, 'It is easier, and probably more useful, to give examples of formal organizations than to define the term'.

Perhaps the real reason why there is no agreed definition of ‘organization’ is that there is no sound and coherent underlying theory of organizations, although there are innumerable ad hoc descriptions and narratives masquerading as theories. None of these has the breadth, internal consistency and rigour that might underpin a coherent understanding how people work and how NGISs may influence working practices. We might, however, take as a starting point some fairly uncontentious definition such as the following:

Organizations are social arrangements for the controlled performance of collective goals. (Huczynski and Buchanan, 1991, p. 7)

So far as it goes, we endorse this definition, and consider each of the constituent phrases of the definition to be crucial. Organizations are collections of people who interact with each other as a group for the purpose of performing tasks that are set and monitored by the organization itself; moreover, membership of the group is controlled within and by the organization. But note that this definition makes no claims for the existence of some entity over and above a 'social arrangement' of the personnel who constitute its membership. Nor is reference made to, e.g., the physical and conceptual paraphernalia that support the activities of the personnel as a cohesive goal-oriented body: the premises and their geographic location, the office furniture and office technology, the flows of information through and beyond the personnel, and so forth. Should these be considered part of the organization? If not, why not? Would the organization still exist as just that organization if significant change were made to any part of the physical and conceptual infrastructure? And what about the information that flows in and out of the organization? Is that a defining part of it? If so, at what point does that information shift from being external to internal to the organization (assuming that question makes any kind of sense)? If the organization has boundaries, where do they lie? If, e.g., a crucial element of the organization's activities is the transport of parts into the factory and of products out of the factory, then should the trucks and the roads on which they travel be, for operational reasons, considered part of the organization? Patently 'external' circumstances, such as the recent (Autumn 1992) lorry drivers' action in France or security alerts on the London underground at rush hour, can have at least a short term effect on the behaviour and decision-making of the organization. Is it, then, possible to draw a line demarcating something that clearly is the organization from everything else that clearly is not?

There are no ready answers to most of these questions, though such lines might be arbitrarily drawn, according to whether one's interests are motivated by ergonomic concerns (yes, the physical paraphernalia are important), economic issues (no, the physical paraphernalia are not important), or whatever other partisan or disciplinary bias. We firmly believe, however, than an organization conceived just as a social collectivity is overly simplistic if one is concerned to understand the processes by which people work and work together.

In the text and following sections, arguments are considered for understanding organizations as distributed knowledge-based information-processing systems.

## 'Organization' and 'office'

We take it that people, whether or not it is formally acknowledged in the organizational context in which they work (or indeed even acknowledged by organization theorists; but see Barnard, 1970), actually do work collaboratively and cooperatively, in highly complex and often unexpected ways, and often in consequence of, rather than in spite of, competition and conflict. Since much of the character of this cooperative and collaborative work may be implicit – ‘collusive’, to use Bittner’s (1974, p. 73) term – rather than overtly specified in, e.g., specific task assignments or more generally in organizational charts or in employees’ conditions of service, we believe that a proper understanding of organizations, and in particular of the impact of NGISs on the behaviour of organizations, requires a richer and more abstract characterization than that which views them simply as social collectivities. We shall hereafter use the term ORGANIZATION, distinguished from lowercase ‘organization’, to refer not to concrete commercial entities but rather to the network of abstract dependency relationships between functional parts by virtue of the presence of which that ORGANIZATION is just that ORGANIZATION, as a stable and coherent whole $^{4}$ . By way of comparison, consider other questions of the same kind: ‘What is a car?’ or ‘What is a chess set?’ For us to judge an object to be a car, there must exist a certain specific and invariable relationship between parts we call wheels, transmission shaft, engine, seats, steering wheel and so on, in such a way as to make its use as a car possible. Similarly, for some ensemble of objects to be a chess set it must comprise just the number of pieces of just the right kinds for us to be able to use it in the normal way to play a recognizable game of chess. Put differently, the behavioural or operative properties of the complex object in its characteristic environment is a function of its ORGANIZATION.

For business and public service organizations, we take the major functional components to be OFFICES (Kahn et al., 1964; Salaman, 1980) which for the present may be equated roughly with the job descriptions corresponding to each of the nodes in the standard chain-of-command organizational chart. Each member of the organization occupies an OFFICE defined in terms of the formal contribution it is deemed to make, relative to and in coordination with other OFFICES, to the overall functioning of the organization as ORGANIZATION. This will be spelled out in the 'job specification', and the assignment of an individual (by external appointment or internal move) to the OFFICE will be constrained by the educational, professional and personal requirements for the post. At a more fine-grained level of analysis, there will be associated with each OFFICE a core task specification, which will (generally implicitly and, where explicit, almost invariably informally) carry with it a model of the task domain for that specific OFFICE and of the functional 'fit' of the task domain model within a model of the broader activities of the organization $^{5}$ . The model will include an ontology (what the objects in the domain are and of what type, its universe of discourse), a 'knowledge base' (how the objects are meaningfully and purposefully ordered into structured representations of the domain), and a process model (a repertoire, partly case-based, of programs determining the permissible computations on the knowledge base). The 'knowledge base' will also include two privileged groups of representations: one corresponding to possible initial states for tasks (or 'templates' for recognizing some situation as a task-instance), the other to acceptable goal states. The three components of the model will have been 'designed' to support not only the goal-driven activities of the individual but also, indirectly, the top-level goals of the organization itself. This is minimally to assume that

for some $\mathcal{D} \subset \mathcal{E}$ , where $\mathcal{D}$ is a set of typed entities $e_1 \ldots e_i \ldots e_n$ associated with an OFFICE and $\mathcal{E}$ is the set of entities recognized by the organization, $e_i, \mathcal{D} \to e_i \in \mathcal{E}$ .

the functional and relational base sets for D is a subset of those for E.

Thus the fact that, in some company, O'Mara is a sales engineer, that Patel is an accountant, or that Toby is the tea-boy, or that Toby has green eyes and weighs 60 kg is, from this perspective, irrelevant to the ORGANIZATION just as, in the case of a chess set, the pieces are made of wood or onyx is irrelevant for the purpose of playing a game of chess, and has nothing to do with our classifying the ensemble as a chess set. We are concerned, that is, solely with identifying the OFFICE of sales engineer, accountant or tea-boy. Now consider that seven of the chess pieces are missing; as a chess set the ORGANIZATION has ceased to exist, though one may functionally bring it back into existence by, e.g., using buttons or coins in the place of the missing pieces. Consider also that if the ensemble consists of of, say, 43 pieces, 17 of which are pawns, five of which are splidgets, and the single Queen can only move forward one square at a time, then whatever that ensemble is, it is not a chess set and it is not clear to the chess-player what can be done with it.

One very crucial fact that distinguishes organizations, as networks of OFFICES, from cars and chess sets is that the former alone have an autonomous internal dynamic that under normal circumstances serves to perpetuate their own existence. Or, to put it another way, it is the existence of the organization that determines the activities undertaken by it; while, at the same time, it is the performance of these very activities that determines the continued functioning of the organization. Thus, e.g., it is the collective complementary activities of groups of individuals working towards the common purpose of producing and selling goods that defines their collectivity as a manufacturing organization, while the existence of the organization in which they participate defines the nature of the activities that they perform. Moreover, such an organization will quickly cease to exist if it ceases to manufacture; in that sense, an indirect but seminal product of the organization is the organization itself. While we would want to reject a crude social Darwinism, clearly those organizations most likely to survive and thrive are those which adapt most quickly and flexibly to their environment (e.g. consumer demand, behaviour of competitors, selection of and arrangements with suppliers, and so on).

How is it that the many individuals making up the collectivity are brought to conform as a body to the overarching objectives of the organization of which they are members? Or in other words, how is the integrity of the organization qua ORGANIZATION maintained? Consider that, after all, the very fact that different OFFICES prescribe different priorities itself suggests internal conflicts of interests. For example, Simon (1976) envisions an imaginary conversation between a sales manager, a production scheduler, a factory department head and a production design engineer, in which he observes:

that the sales manager would be most concerned with customers' wishes for low price, prompt delivery and product quality; that the scheduler would want predictability of sales; that the factory man would urge longer lead times and less reckless promises to customers; that the design engineer would complain about the inflexibility of the factory in introducing design improvements; and so on. (Simon, 1976, pp. xviii–xix)

Each is working with a model for their OFFICE which, by virtue of its being task-specific, may conflict with the models of those with whom they have to coordinate activities in order to accomplish to top-level organizational goals. But it may very well turn out that the actual source of the conflict is not in incompatibilities between the models thus narrowly conceived but between the models as assimilated and reconstructed by the individuals who instantiate those OFFICES. There is perhaps an irony here: motivated by (generally implicit) appeals to their professionalism rather than by the exercise of direct control (via the promises of rewards and threats of sanctions) more common at shop-floor level, organization members may on that basis form goals and take decisions that in the short term impede the goals of others. (Extreme cases, which may lead to overt political confrontation, might include teachers who, as professional educators, or doctors who, as professional health workers, perceive conflicts between their own skill-related objectives and those of their managers.)

The section on structure and role resumes the issue of organizational conflict, and will show why the concept of OFFICE is insufficient to account for actual behaviour and goal-formation. By contrast, the cognitive glue, as it were, of the organization, holding the various OFFICES and their occupants together in a cohesive purposeful unity, is arguably its ‘corporate culture’, and it is therefore this that we will take as our point of departure in the next section. As will become clear, the concept of a ‘culture’ and ‘cultural knowledge’ will help us understand what it is that organization members actually do and the process by which, in that light, NGISs are accommodated into organizations.

## Corporate culture, working culture

Since the publication of two key books a decade ago (Deal and Kennedy, 1982; Peters and Waterman, 1982), there has been some enthusiasm in recent years for endeavouring to understand what an organization is, and how it behaves, in terms of its ‘culture’. (Whether a ‘culture’ is something an organization has or something an organization is has been a matter of active debate, but possibly less a debate about substantive issues than about what might be the appropriate ‘experiential Gestalt’.) The ‘culture’ of an organization is most commonly thought of as the complex fabric of shared beliefs, values, behavioural norms, expectations, sometimes even company-specific jargon for naming jobs, processes and products, the socialized sense and cognitive style of ‘who we are’ and ‘how we do things’. Whether from a historical perspective it has been consciously engineered or not, it will very often happen that a specific culture is fostered by the company itself, in so far as it serves as cognitive support for company goals. It is this that we might properly call the ‘corporate’ (or ‘company’ or ‘organizational’) culture; and it has effectively become a management tool (e.g. Kilmann et al., 1985).

To better understand the concept and the manner in which it impacts on individual performance, we would like to take a rather more specialized perspective on 'culture' however. In the first place, 'corporate cultures' as commonly understood are in large part themselves the products of, transmitted through, and sustained by, activity at a more fundamental level; pre-eminently in the webs of communication and affiliation – 'the human social processes by which people create, raise, and sustain group consciousness' (Bormann, 1983, p. 100) – that criss-cross the organization. One would want to look for indices of the culture in, e.g., overt forms of textual communication (proposals, reports, letters, contracts and written job descriptions, memoranda, face-to-face conversations, telephone conversations, electronic mail, in-house newsletters, health and safety regulations and other rulebooks, noticeboard messages, etc. viewed as forms of discourse). Less obvious but equally crucial in the construction of the social realities shared by members of organizations are verbal rituals and protocols (formulae and verbal gestures embedded in exchanges between speakers), forms of address (use of addressees' names or titles; 'personal' versus 'positional' dialogue, c.f. Bernstein, 1971), stories (verbal repetition of company 'lore'/'folk history'/'myths' about the organization or about specific individuals; company rumours and 'grapevine' gossip; 'inside jokes'; see Bormann, 1983), interpretations, legitimations, and styles of explanation (e.g. appeal to causal processes, to company goals, to rational conduct, to company culture – 'the way we do things here – and so forth), and jargons ('corporate slang'; task-specific terms; organization-specific labels for objects, concepts, and practices; and so on). Finally, one would look at the non-verbal semiotics of dress, office topology, smoking areas, 'rites of passage' for internal job moves, and so on.

Verbal and non-verbal communications are a primary vehicle for the transmission of the culture to newcomers to the organization, and are therefore a necessary (though not sufficient) ground for organizational culture. For example, company folklore about its ‘heroes’ – ‘Bill Morton, hired as a tea-boy, is now on the Board’ – can become a vehicle for the transmission of that part of the corporate culture relating to those qualities of individual performance and their rewards that serve the interests both of the individual worker and of the company. Similarly, the acquisition of company-specific jargons may serve to reinforce the individual’s sense of belonging to, of having been initiated into, a prestige group. Each of these, in turn, supports the company's interests in maintaining a cohesive goal-oriented workforce.

In a more fine-grained analysis one would want to examine the substantive content of communicative acts, and perhaps in particular the linguistic content of verbal exchanges, between individuals for a principled description of the interactions out of which the culture emerges as a symbolic universe. A detailed analysis is the subject of another paper (Hutchison, 1994), and will not be pursued here.

Clearly communicative acts, while evidencing the culture, are themselves the outcomes of (often largely unconscious) choices made, on the basis of internalized knowledge and incoming information, at a more fundamental level. We shall hereafter want ‘culture’ to be taken to refer more precisely to ‘the knowledge people use to generate and interpret social behavior’ (Spradley and McCurdy, 1972, p. 8; see also Spradley, 1980, p. 6) with a sufficiently liberal understanding of ‘social behaviour’ to include intersubjectively interpretable manifestations of technical knowledge (as indeed Spradley and McCurdy themselves implicitly take it to mean). Provisionally (though note the qualification in the structure and role section), we shall follow Goodenough (1957, p. 167) in holding that

A society's culture consists of whatever it is one has to know or believe in order to operate in a manner acceptable to its members ... Culture is not a material phenomenon; it does not consist of things, behaviour, or emotions. It is rather an organisation of these things. It is the form of things that people have in mind, their models for perceiving, relating, and otherwise interpreting them. (My italics) $^{6}$

This knowledge will have been learned, in the course of primary and secondary (including organizational $^{7}$ ) socialization, and will to a certain extent be shared with others. (Hutchison, 1993, addresses the question of what it means for knowledge to be ‘shared’ by a group and to what degree it can be ‘shared’. For succinct descriptions of ‘primary’ and ‘secondary’ socialization, see Berger and Berger, 1976, p. 62). In the most general terms, this knowledge constitutes a tacit, unarticulated and unanalysed background of commonplace assumptions against which events take place and in terms of which events make sense. That adults normally work for so many hours a day through a large part of their lives, that work is ordinarily remunerable, that time is a measurable resource, that most work presupposes some form of appropriate prior training, and such like, are all items of tacit knowledge that fall within this taken-for-granted background.

At the other extreme, there are forms of knowledge pertaining to particular skills. Take, as a very specific and restricted example, the rules learned by the individual for the creation of documents with a word-processor. They will in the first place, long before ever laying hands on a keyboard, have learned a set of (language-specific) rules for arranging characters in sequence to represent words, and for arranging words in syntactically acceptable sequences to form sentences. Further, they will later have learned how to switch on a computer, how to insert a floppy disk, how to boot up the system, how to use a mouse, how to use the on-line tools for the formatting of text, how to send output to a printer. Also they will have learned specifically how to create memoranda, business letters, reports, and so on, including any features of in-house style of the organization of which they are a member. Each behaviour is the product of actions in part generated by the cultural knowledge related to writing. At the same time, this knowledge, to the extent that it is shared, enables other to interpret the behavioural outputs.

Culture, according to the definition we shall use, is then not the overt behaviour, nor is it the complex coordination of actions producing that behaviour. Rather, it is that knowledge which one must have internalized in order to generate that behaviour.

Earlier, we discussed the task domain model associated with each OFFICE. This model will (under an idealized view) satisfy the condition of constituting, for some OFFICE, 'the knowledge that organization members use to generate and interpret organizational behaviour' proper to the task domain. Further, it is culturally transmitted knowledge, communicated to the incumbent of the OFFICE through talk (face-to-face training, managerial direction, etc.), documents (the job specification, the contract of employment, and so forth), and often practical demonstration; moreover, given that the incumbent of the OFFICE has become so in virtue of appropriate prior training and experience, the model will be enriched by the process of its assimilation by the OFFICE holder. But it is at this point that usefulness of the idealization breaks down.

## 'Structure' and 'role'

We shall distinguish between the ORGANIZATION of an organization and its STRUCTURE. Whereas the ORGANIZATION is the network of formal dependency relationships between OFFICES that define in the abstract the social collectivity as an organization, the STRUCTURE is the physical actualization of that network by individuals enacting ROLES. So, e.g., if the sales engineer O'Mara leaves and Cohen is recruited to take over his OFFICE, the ORGANIZATION does not change, but the STRUCTURE does to the extent that Cohen and O'Mara are two physically distinct individuals, with different personalities, different professional histories, different biographical paths that have led them into the organization. Similarly, if Cohen spends a great deal of time talking to the service staff while O'Mara did not, the STRUCTURE changes, though the ORGANIZATION remains the same. Note also that, to the extent that 'experts' become experts as individuals – that the ultimate locus of the learning process is in the individual learner – the resultant expertise is more properly construed as the property of a ROLE than of an OFFICE. (It is the failure to distinguish the two, that may give rise to inappropriate specification of the knowledge-base).

We shall provisionally think of the STRUCTURE, then, as the network of actual relationships – paths of communication and affiliation – that members of the work group, as individuals enacting ROLES, contract with others in the organization. Or, in other words, we assume the homology

## ORGANIZATION : OFFICE :: STRUCTURE : ROLE

The ORGANIZATION/OFFICE pair, focusing on non-dynamic formal relations, represents a normative idealization; the STRUCTURE, actualized by cooperative activity between ROLES, captures the dynamic reality of the organization. From the discriminations made thus far it follows that:

the STRUCTURE is self-renewing (individual members are recruited and leave), while the ORGANIZATION is self-sustaining the STRUCTURE (by virtue of the fact that employees come and go) has an inherent temporal dimension; the ORGANIZATION has not.

from the perspective of an external observer, descriptions of behaviour may be in terms of changes of state in some system over time; the complex behaviour of the organization that is empirically observed is a function of its STRUCTURE, not of its ORGANIZATION.

The OFFICE, by virtue of its being an idealization, underdetermines the cultural knowledge that enables the individual to perform his/her ROLE successfully. This is so for at least four kinds of reasons. Consider that, in the first place, the OFFICE specifies for the individual actor some initial information about the task domain, including the form of idealized inputs, resource (including time) constraints, a prescriptive repertoire of actions that the actor may select from according to some decision function to transform the inputs into outputs, and an evaluation function for assessing the 'goodness' of the outputs. Order processing, e.g., will for the most part be a fairly straightforward business with, for each stage (OFFICE) in its itinerary through the organization, the inputs and outputs well-defined. For non-trivial (and all non-algorithmic) tasks, however, the actual model used by interacting agents is likely, by virtue of the form and quality of the information that actually presents itself, to diverge to some significant degree from the idealized model specified for the OFFICE. For example, the influx of information necessary for deciding action is likely to be asynchronous (not all the information necessary for acting will arrive at the same time, or even in time), the information may likewise be incomplete, inconsistent, corrupted and 'noisy'. Also, individual tasks may be interrupted (e.g. while awaiting information) and interleaved.

In the second place, the individual brings to the execution of organizational duties a wealth of unique professional experience acquired both from other OFFICES prior to assuming their present OFFICE and also from the day-to-day practice of working. Since much of the total working environment (which includes what was earlier referred to as the physical and conceptual paraphernalia that support the work activities) is quite properly not represented in the task domain model associated with the OFFICE, there remains unaccounted for the cumulative effect on the ROLE of the daily regular cycles of decision-action-outcome-feedback-decision (see Figure 2), including feedback from others in the work group, that are firmly embedded in and played out against that environment. The actor's internal representation of his/herself, his/her activities, and environment, as well as the team culture that emerges through the routinization of their collective cooperative activities, need bear little more than superficial resemblance to the abstract representation of the OFFICE.

In the third place, work is likely to become routinized in fairly determinate ways as, through numerous decision-action–outcome–feedback–decision cycles, the pattern of action on tasks tend to ‘settle’ into repetitive sequences, quasi-atomic in the sense that they are not perceived by the worker as orderings of discrete actions. By ‘routinized’, therefore, we mean much the same as March and Simon mean by the term:

![](/api/attachments/UF3X2TXF/fulltext/images/d2ae5a952834cb84ce7d5916bbd998b0ec6466a5eb8e6701db27b647edf942c3.jpg)  
Figure 2 Feedback loops to ROLE

We will regard a set of activities as routinized ... to the degree that choice has been simplified by the development of a fixed response to defined stimuli. If search has been eliminated, but a choice remains in the form of a clearly defined and systematic computing routine, we will still say that the activities are routinized. We will regard activities as unroutinized to the extent that they have to be preceded by program-developing activities of a problem-solving kind. (March and Simon, 1958, p. 142)

For example, a task, possibly procedurally underspecified by the model for some OFFICE, may be expanded by the incumbent of the OFFICE into set of subgoals satisfied by the sequence of actions U, V, W, X, Y, Z. The sequence may, at a later moment for the incumbent of the OFFICE or for some other individual assuming that OFFICE, be collapsed into a single routine. In other words, what at time $t_{1}$ may be perceived to be a compound action may at time $t_{2}$ be effectively a single action. Alternatively, a sequence may be replaced by some functionally equivalent single action or vice versa. (Consider, as a ‘domain-independent’ illustration, moving files in UNIX either by using mv or by using cp to make a copy of the file in the target directory and then using rm to delete the original $^{8}$ ).

Fourthly and finally, the individual, in interpreting and executing the duties and responsibilities tied to the OFFICE, beyond observing the task-specific operational rules for jobs as well as general rules of conduct, develops meta-rules of various kinds. Some of these may pertain to the organization and ordering of tasks; some to engaging the help of, or coordinating activity with, other people; some to integrating the performance of tasks within personal goal agendas; and so on. In regard to this last case, it may be worth parenthetically noting that, corporate culture notwithstanding, there may well be incompatibilities between organizational goals and the individual worker's personal goals ('I want to simplify the process by which I accomplish tasks', 'I'd get things done more efficiently if I were working with Tomkins rather than McCawley', 'I want a rise/promotion', 'I want the desk near the window', 'I want to keep my job', 'I will oppose the installation of this system, which is a threat to my job/self-esteem', ...). All talk, then, of an organization having 'goals', 'values' is essentially talk about its top level decision-makers; the organization, conceived abstractly, has none such. Hence:

action' is mediated by processes of interpretation and negotiation in which groups attempt to protect and advance their specific interests. It cannot be stressed too strongly that what is at issue in this type of analysis is not simply different viewpoints and interests regarding rewards and efforts (inducements and contributions), but also different contributions to the social construction of reality — the reality in the case of organizations being such notional entities as goals, rules, roles and other elements that are believed to constitute the organization's structure. (Thompson, 1980, p. 216)

In conclusion, to understand how individuals really work, and work with others, one needs to empirically observe the actual group dynamics of ROLES rather than rely on the presumed group dynamics of OFFICES.

## 'O-structure' and 'C-structure'

The organization specifies formal paths of communication – who reports to whom, who delegates what to whom, who liaises with whom for what purpose – and these paths are enshrined in, e.g., standard chain-of-command organizational charts and a concomitant background meta-discourse that includes such formulae as ‘going through (the proper) channels’ or ‘bypassing’ them. It may very well happen, and is in fact probably the normal state of affairs, that there is at least a partial mismatch between the paths represented in the organizational chart and those which are ongoingly negotiated between actual individuals. Or, in other words, that the ROLE network (STRUCTURE) will not be wholly isomorphic with the OFFICE network (ORGANIZATION). Formal relationships of authority and responsibility will still ordinarily be (in fact, must be) observed if the organization is to maintain its internal integrity, and indeed the ORGANIZATION remains the canonical reference grid for members’ legitimation of their own and others’ activities. However, by virtue of the fact that the organization is constituted of individuals with their own personalities, interests, goals, and work routines, the actual (and usually unintended) STRUCTURES that emerge naturally from the dynamics of interpersonal behaviour will be far richer and denser than that formally represented in the organizational chart. Put differently, the abstracted ORGANIZATION of the organization expresses a normative idealization of the functions (OFFICES) of its members and their interrelationships: it tells us who does what and who communicates with whom but nothing about the actual processes and procedures by which those functional roles are acted out in such a way as to effect that organization.

Let us then say that the basic organizational chart envisions the overt STRUCTURE of the organization; the chart augmented with paths showing who actually talk to whom (about what, how frequently, etc.) traces each of many possible concurrent covert STRUCTURES (hereafter, the impact of ‘organizational goals’ on ‘organizational

O-STRUCTURE and C-STRUCTURE, respectively). The C-STRUCTURE is regarded as the network of actual relationships – paths of communication and affiliation – that members of the work group, as individuals enacting ROLES, contract with others in the organization.

It is the C-STRUCTURE which, representing the actual dynamics of human activity, determines the performance of the organization. Moreover, significant activity within the C-STRUCTURE can, when it is perceived to coincide with the corporate goals recognized in the overt structure, lead to a modification both of the organization (in terms of abstract roles and responsibilities) and of the O-STRUCTURE (in terms of who is sanctioned to do what).

Therefore if some new element, e.g. a NGIS, is introduced into the organization, the result of the incorporation of this element is by no means uniquely determined by the inherent properties of the element in itself; much more so, by the manner in which that element is assimilated into the organizational context. Specifically, the changes that occur in the organization will principally be those occasioned by the perceptions that the work groups concerned have of the new element in itself, by their interpretations of the proposed relationship that the element will have with existing elements in the working unit – for instance, with other members of the group – and by the actions subsequently taken by those members, either individually or collectively, to accommodate the new element. The process of accommodation will, we contend, be shaped by a number of factors, including:

prior assumptions by members of the organization (and in particular, of the work group concerned) with regard to what the relevant domain information and knowledge is, and how it is expressed

(possibly inexplicit) conventions for the interpretation of the data elements routinely processed by the group (i.e. a shared ontology and agreed mappings between data elements and entities, properties and processes in the 'real world')

assumptions and agreements regarding who, prior to the introduction of the system, owns and controls the relevant information and knowledge, where it comes from, and who has access to it

'folkloric' assumptions with regard to what exactly an information system is, what it is capable of, and what consequences its introduction will have for the working practices of members of the organization

the routinized day-to-day activities not only of the individual user themselves but also of other members of the immediate work group who are affected in some way by those activities

We prefer to see these questions and potential conflicts as effects on the organization of possible or anticipated disruptions to the culture that has characterized the work group prior to the introduction of the technology. Before we look at any of these factors in more detail, consider that there are at the very least three stances one can take towards computer IS. In the first place, whatever else it is, a (NG)IS is (or, viewed more narrowly as software, is embodied in) hard technology, something with a shape, constituent parts, a price, a manufacturer and a physical location in the office. We might call this the 'physical stance' (the same term is used by Dennett, 1978, with a somewhat different meaning, but I cannot think of a better alternative expression). Its use as technology, under this stance, presupposes the acquisition of a set of basic motor skills (insertion of disks, use of keyboard, hand-eye coordination in using the mouse to move the cursor, and so on) and a possibly more nebulous repertoire of basic attitudes (symbiotic relationship between operator and computer, computer as tool, computers increase personal efficiency, computers enhance clarity and consistency of data, and so on). Specifically physical characteristics of the machine (other than HCI issues such as high/low resolution, brightness, flicker, glare, colour, key sensitivity, optimum character founts, screen size) may foster more peripheral attitudes (e.g. computers are 'clever', computers do not make mistakes). Turkle (1984, p. 13), e.g. notes that:

The impact of the computer is constrained by its physical realities. One such reality is the machine's physical opacity. If you open a computer [...] , you see no gears that turn, no levers that move, no tubes that glow. Most often, you see some wires and one black chip. [People] faced with wires and a chip [...] can find no simple physical explanation.

Computer IS can engender rejection under this stance in users who are, e.g. not proficient in the basic motor skills and attitudes.

Beyond the physical stance, we understand the (NG)IS in terms of its functionality – as a device for the collection, storage, processing, transmission, distribution, retrieval or utilization of information; that is, we assume something akin to what Dennett (1978) calls the 'design stance' towards it. Under this task-orientated stance the user is guided by assumptions with regard to the information-/knowledge-processing capabilities of the system. And it is under this task-orientated 'design stance' that most knowledge engineering (including the knowledge elicitation) takes place: the knowledge engineer characteristically shares with the prospective user(s) the view that the task to be accomplished or the problem to be solved is a specifically technical one, and that it is both possible and necessary to identify, isolate and describe only those domain entities that directly participate in the problem-solving activity and only those cognitive processes that are directly involved in solving the technical problem.

While we acknowledge that there are many knowledge-based systems for purely technical jobs (image processing, medical diagnosis, interpretation and analysis of physical data etc.) that successfully perform the tasks for which they were designed, we believe that this is an overly restrictive view of human problem-solving, and have suggested (Hutchison and Rosenberg, 1993) that one important reason for the frequently unsuccessful integration of expert systems into organizations (in particular, systems intended for the support of coordinated multi-agent knowledge-based activities) is in consequence of a misconception of the nature of the knowledge and behaviour of both human experts and expert systems alike. In brief, the popular conception (not unsurprising in a culture which continues to nurture the caricatural image of the white-coated bespectacled 'boffin') is inherently reductionist and consistent with the idea of the inter-substitutivity of individuals in organizational OFFICES. We believe that, on the contrary, the knowledge and information that experts, as people, have and use are not, and cannot be, neatly contained in discrete packages, but rather carry indicators of the broader C-STRUCTURE.

Both the physical and the design stances to different degrees identify a physically and conceptually bounded system with certain intrinsic properties and behaviours. The manufacturer's literature telling you that it requires a hard-disk drive, System 7, and 2.5 mb of RAM, and the manual or user-guide telling you how to use it and what it does, pertain to these two stances.

It may be a misconception of the role of IS to perceive them as solely technical tools; i.e. to adopt a strictly technological-physicalist rather than a more broadly functional-cultural perspective on the technology. In the context of cooperative working, the development and integration of IS into the industrial environment may imply a radical shift of perspective on such systems.

There is a third stance one may take towards (NG)ISs – one might call it the ‘cultural stance’ – which shifts the perspective away from the image of the stand-alone, asocial tool, operating within clearly specified operational boundaries, and towards an image of the technology as nothing more than a functional ‘cultural’ component of a broader ‘open system’ that includes not only the user but also the work group of which the user is a part (Hutchison and Rosenberg, 1991) $^{9}$ . Or, in other words:

(i) the work group or organization as a whole may, at this level of abstraction, be conceived as an ‘information system’ in so far as the machine’s symbols (words, numbers, graphs, pictures, ...) have meaning only in the context of the interests, practices and interpretive procedures of those who use the system or who use the information mediated by the system

(ii) viewing the work group (or maximally the organization) in toto as a distributed knowledge-based information processing system accepting inputs from and outputting to its environment, there is little sense in distinguishing that part of the information processing which is executed mechanically and that part which is executed by human beings (just as, if one is interested only in input and output solely as information, there is little sense in distinguishing between a human being calculating the sum of two numbers and a pocket calculator doing so).

In the context of computer-supported cooperative work, the design, deployment and integration of maximally effective groupware in the business or industrial environment may imply such a radical shift of perspective on such systems. Under this stance, it is unhelpful to think of even single-user systems as being within the sphere of responsibility and control of some specific individual user who may consider that they have proprietary rights over the technology and more importantly, over the information that that technology generates.

The NGIS will be viewed as a part of a more global system involving not only the direct user of the system but also the other collaborating agents in the organization. Therefore, our analysis will by necessity have to include those aspects of human expert behaviour that make her a part of a social structure. The expert systems will effectively no longer be saying 'I know everything within my world and my user is the sole owner of that knowledge'. Instead, it will in its design reflect the organization of the community which shares a body of knowledge required for knowledge-based activities. The distinction between single-user and multi-user systems in fact dissolves as one adopts the stance that views all such systems as effectively filters for information exchanged between social beings.

Consider, e.g. a simple pie graph or bar chart. The visual display is understood to represent, in highly stylized form, some collection of facts about the real world. We have learned public conventions, in reading such visual display forms, of interpreting the world in terms of n-dimensional coordinates where each dimension is understood to correspond paradigmatically to some scalar category (time, cost, volume or whatever) or to some closed set of discrete entities (employees, product lines, ...). Which categories are selected determine what part of the world we are looking at and what the salient entities are. It may turn out that, to all intents and purposes, the representation supplants the world of which it is a partial image and 'becomes' that world; the content of the visual display becomes the conceptual currency of those whose business it is to generate and read such displays. Clearly, organizational work in which graphs or charts are used as an information resource – i.e., are used to mediate between members of the organization meanings which will inform subsequent decision-making – must depend on members sharing a common ontology of objects and relations, and common conventions for the interpretation of the formal and substantive elements of the underlying semiotic system.

## An example: the 'design review'

The three main issues raised by our attempt to define C-STRUCTURE are epistemological, ontological and representational in nature. More specifically, in our attempt to identify C-STRUCTURE in a specific working environment, we ask questions such as the following:

epistemological: do communicating agents have a common referent for a symbol? do they 'speak the same language'?

ontological: how is the choice of domain entities determined?

representational: is the granularity of the representation appropriate to the task?

These are discussed further by way of illustrative example of language use in context, based on the data obtained in the case study of working groups in manufacturing engaged in the process of developing a new product. The process is generally referred to as 'design review' and has a formal definition in all manuals and documents relating to the O-STRUCTURE of the organization. However, an analysis of the use of the term 'design review' in interaction among the people involved in developing new products, shows much richer patterns of use of the term than that suggested by the formal definition. Thus in the C-structure, the meaning of 'design review' is illustrated in the sentences below. The first sentence:

'Engineering ... quality people ... we are all on design review.'

describes a group of people who are members of a committee called 'design review', while the sentence:

'The new system, ME39, is on design review next week.'

mentions an object which will be discussed at a meeting of the design review committee next week. In other words, in the first sentence ‘design review’ means ‘a specific group of people’, while in the second it means ‘a meeting (of that group)’. This recognition comes naturally even to people who do not know that the definition of ‘design review’ is something like

'a formal procedure that experts in manufacturing (who specialize in engineering, financial management, and quality control) engage in when developing a new product. The procedure is divided into three main stages which involve design from specification, prototyping and the testing of the prototype' [Int TW 1/13]

and so on. Thus, people's ability to interpret different meanings of ‘design review’ illustrated in the three examples above does not seem to require any expertise in the domain of manufacturing, but can be viewed as a manifestation of their general language competence and of an awareness of the principles that govern language use in context.

One task for an analyst of C-STRUCTURE is therefore to explicate these principles and to account for the participants' language competence which enables them to understand which of the different meanings of the term is appropriately evoked in a given context. The significance of context here is not only that it resolves potential linguistic ambiguity between possible meanings of the term, but also that it can serve as a manifestation of how the group activity (or a collection of activities) that can be referred to as 'design review' is organized and conducted in socially accepted ways.

Why is it that it has been so difficult to explain the meaning and use of numerous terms like 'design review', and to account for speakers' institutions that we are here dealing with one (polysemous) word which can be used in different senses determined by the context, and not with several distinct words which may or may not be related to one another? The issue can be, and has been, considered from different perspectives in various disciplines ranging from practical considerations in the design of computational lexicons and term banks used as aids in machine translation, through methodological orientation of lexicographers involved in the development of dictionaries, to semantic and philosophical analyses of the correlation between the meaning of a word and the object denoted by its use in a given context $^{10}$ . The approach adopted in this paper is that of analyst concerned with problems of accounting for lexical variation and attempting to construct a model of language use, i.e., not a model of language behaviour, but of the regularities manifest in that behaviour, in other words, a model of the underlying language system which is systematically related to the social life it is used to describe.

The main aim here is to provide a characterization of C-STRUCTURE in terms of 'the fit' between empirical language-data obtained from the study of interaction in an application domain, such as manufacturing, and the formal system which provides the framework for the description and explanation of the data. In this search for theoretical underpinning that would make the definition of C-STRUCTURE precise and explicit, it will be necessary, in the first instance, to sketch out an analysis to establish what steps must be taken to make the 'raw' data fit a formal system. In this paper the data have been obtained from interviewing informants in manufacturing, and the illustrative example below shows how the informants refer to the term ‘design review’ (throughout this paper ‘design review’ will for the sake of exposition be regarded as a single term, although it is recognized that a full analysis of it would have to take into account the fact that it is a compound noun).

“… we then go into a formal procedure which is called design review … actually we start at phase 0 … for example this week … sorry … next week we have … design review for a three and a half inch size 2 Mb floppy disc drive … engineering, quality people … we’re all on design review, … we get together and decide what it is that’s needed … so we then identify a list of suppliers that is then in the next design review …” [TW 1/3] … then at design review 2 … at the end … it’s the meeting that says … have we done all that we’re supposed to have done … [GB 1/6] … but we have other reviews with business centres and product centres … er … called troikas … which implies the meeting … meeting of three people … [GB 1/21]

Out of this, a small corpus of data is checked for accuracy and selected to illustrate representative linguistic processes relevant to identification of C-STRUCTURE, such as the examples below:

(1) purchasing people ... quality people ... we're all on design review ...

(2) the new system .. ME39 .. is on design review next week

(3) this week we have design review 0 for ME39

(4) Who's on design review for ME39?

(5) What's on design review this week?

(6) What's in this design review?

The use of the term ‘design review’ in (1) suggests that it is a committee which implements the procedure and these people are all members of the committee. In (2) ‘design review’ is a meeting of the committee where the introduction of the product ME39 is to be discussed. In (3) ‘design review’ is a document (usually) containing the minutes of the meeting. In the questions we have the following interpretations:

(4) Who's on design review for ME39? (= people, committee)

(5) What's on design review this week? (= product, meeting)

(6) What's in this design review? (= information, document)

Thus, on the basis of the observation of the data illustrated above, it seems that it is, on the one hand, necessary to consider the use of the term ‘design review’ in terms of different uses of the term itself, i.e., its reference to a group of people, a meeting of the group, a document recording the meeting, and so on. On the other hand, there are different interpretations of what it means to be 'on design review', i.e., being members of the group or the committee (as in (1)), or alternatively being a topic discussed at a meeting of the committee (as in (2)). Such an account would essentially involve explaining the fact that in (1) and (2) the uses of 'on design review' are closely related to the context provided by the other parts of the sentence. In (1), the combination of 'we' and 'on design review' forces one interpretation of what the term refers to, namely, a committee or a group of people. In (2), on the other hand, the combination of 'the new system - ME39' with 'on design review' influences the choice of quite a different kind of referent, that is, a meeting.

Although these observations may have captured only a small number of the issues that could reasonably be considered (and indeed in some approaches to linguistic analysis such distinctions may not even be central, c.f. Kempson, 1977, pp. 81–3), it is necessary to consider the observed use of 'design review' from a practical, and a methodological, viewpoint. Practically, people's interpretation of the referents in different contexts could lead to different courses of action. That is, if 'design review' is interpreted as a committee, the answer to the query 'Who is on design review?' would be sought in the personnel database containing job descriptions, whereas the interpretation of it as a meeting, e.g. in 'What is on design review next week?' would involve consulting a departmental planner.

More importantly, however, the use of 'design review' in interaction may be seen to indicate what conceptual categories there are that can provide candidate referents for the term. It is perhaps also appropriate to say that the various uses of the term are indicators of the ways in which the cognitive agents in question individuate their world. In this sense, we are dealing with ontological issues concerning the primitives to be provided by any adequate theory of the organization of social life. Although in many approaches to formal specification of computer systems, e.g. the theory provides the ontology that is supposed to capture the actual entities recognized by the agents in a given application domain, it is by no means clear that this is the way elements of C-STRUCTURE can be truthfully and accurately described. The main problem is that the actual entities recognized by individual agents and clearly discriminated by them is evidenced both by their actions/behaviour and in their use of language when talking about significant activities/aspects of behaviour. Both the actions and the language vary from context to context and, indeed, the social meanings relevant to both evolve in the course of interaction – they should not therefore be fixed in a priori manner. (The ontological issues are considered further below.)

This gives us two basic kinds of representation problem. First, how to represent the meaning of the term so that it can in different contexts be used to refer to objects or notions as distinct from one another as a group of people, an event or a stage in a procedure, a document and so on. The second, related, problem is how to express the interaction between, on the one hand the constituents of the phase ‘on design review’, and on the other, the subjects of the sentences (1) and (2), that is, ‘we’ and ‘ME39’ respectively, with the interpretation of the phase ‘on design review’.

For the purposes of this analysis lexical variation in the use of 'design review' in context will be described as a system of choices. The choices refer to information associated with both the possible uses of the lexical item and the context of human activity in which these choices are realized. We use systematic nets as a tool for capturing the complexity of information present in such an activity on the one hand, and for explicating the kinds of constraints and the ways they may be realized on the other $^{11}$ .

When applied to the data, the possible uses of 'design review' can be recorded in the form of links and conditions provided by the systemic network formalism, where the links represent two kinds of choices, the exclusive and the inclusive choice, illustrated in Figure 3.

Thus (a) means that a location is specified in terms of information about both time and place, while the meaning of procedure includes information that it can be divided into stages which are, phase 0, or phase 1 or phase 2.

The conditions are similar, in that we can define the meaning of the phrase ‘design review 0’ as a paradigm which incorporates two aspects of its meaning, namely that of a meeting session and that of a phase in the procedure. The exclusive condition specifies the restriction on the possible phases of the procedure being phase 0 or phase 1 or phase 2, but not all simultaneously, as illustrated in Figure 4.

In this way the connections of the term ‘design review’ with meetings, procedures and committees can be represented as complex interrelated classifications, or paradigms, in which these connections or constraints are realized. Different kinds of relatedness of meaning can then be specified as different realizations of these constraints. For example, the meaning of the phrase ‘design review’ can be captured by the paradigm which

![](/api/attachments/UF3X2TXF/fulltext/images/6a8eecc6c8fe75907d82c3f54ffa4d32d94fc8af4c075e6ad4cbbc9c4c61ba2d.jpg)  
Figure 3 Choice

$^{11}$ Systemic networks were originally used in Systemic Grammars, but have subsequently been adapted to describe large amounts of qualitative data in social science, and knowledge engineering research. For an overview of the uses of formalism in this context, see Bliss et al., 1983, Johnson et al., 1985.

![](/api/attachments/UF3X2TXF/fulltext/images/5766c7c05b9e4cd3658155bb442188909c6587a39fde1571a0fe188d75b4fd06.jpg)  
(a)

![](/api/attachments/UF3X2TXF/fulltext/images/95ffbc317e33bff76e94eb3bacfa23d8b294c35dc2d5b5d8668d79b23bde0a38.jpg)  
(b)  
Figure 4 Conditions

expresses the simultaneous choice of phase 0 which is a part of a procedure, together with the first session in the series of meetings associated with the procedure. Once the constraint has been identified as the connection between two categories, meeting and procedure, the paradigm can be constructed such that it systematically relates all relevant information about both categories in a complete description of the situated meaning of 'design review' in this particular context.

Thus, we can take the definition of ‘design review’ as procedure to be the core meaning of the term (this is implied by an informant, see (3)); different paradigms can then be expressed as different conditional constraints, with their use being governed by background conditions. Therefore, if ‘design review’ is also used to refer to a meeting (as shown in Figure 4), then the relatedness between the core and the ‘additional’ meaning can be expressed as a change in the background conditions which shows how the two meanings can be combined. Thus, the paradigm

## 'design review' is a meeting and also a procedure'

must contain additional information concerning phases of a procedure and sessions of a series of meetings which are expressed as restrictions on 'procedure' and 'meeting'. There is also a possibility of introducing optional rules relating or identifying a given phase of the procedure with a corresponding session of the meeting, in the event that, e.g., at each phase there must be only one meeting.

Therefore, it seems quite easy to create data descriptions, expressed as paradigms generated by systemic nets which capture the systematic variations in the observed use of the term. This, however, does not overcome two main (related) problems with qualitative data analysis when grounded in systemic networks as described here. One concerns the overall organization of the network in terms of some hierarchy (usually referred to as the problem of 'delicacy'), while the other concerns the status of the categories or nodes which are linked to one another in a system of choices $^{12}$ . The problem arises because the focus of this analysis of C-STRUCTURE is not only on the representation of word meaning, but also on the account of its interaction with other parts of linguistic structure that constitute the context of its use in social life.

![](/api/attachments/UF3X2TXF/fulltext/images/ed25f85b929a64b65dfa5a82ff6bc1ea62f3f06bcd94931fa9cfe0417df64c5d.jpg)  
Figure 5 The meaning of 'on design review'

In other words, the flexibility of the network formalism, which has definite advantages in the early stages of an analysis, does not provide guiding principles that would prevent arbitrary introduction of choice systems at any point in the network. If we take Figure 5 as an example of a complete network that provides the basis for describing possible meanings of the phrase ‘on design review’, then the paradigms generated by the network show that (reading from right to left):

(i) being ‘on design review’ involves both a session in a series of meetings (which are further specified in terms of topic, session id in a sequence, outcome) which are parts of process

(taking place at a location) which is a kind of event and — a phase in a procedure which is a part of process which is a kind of event (ii) being ‘on design review’ involves either specifying, testing or release which are both procedure and parts of a process which is a kind of event and kinds of collaboration which is an activity of a given range

The delicacy problem can be characterized as how to provide the intermediate choices between the rightmost and the leftmost sides of the net. Assuming that the leftmost categories are the most general, representing types of objects and relations among them, the rightmost ones can be viewed as the most specific, representing the actual terms whose meanings are to be described. In this context, the only restriction on the rest of the network is that the intermediate choice systems which link the general with the specific categories, must play a useful role in specifying what kind of information is needed if we are to arrive at the correct interpretation of the term 'design review'. In other words, we need to address issues involved in identifying significant components of C-STRUCTURES at an ontological level.

## Accessing the C-STRUCTURE: an ethnography of the workplace

In a great many respects the process of knowledge acquisition (broadly enough construed to include relevant parts of systems analysis) and the ethnographic interview are strikingly similar: in each case, in the most general terms, the business of the interviewer is to elicit actors' (e.g. a domain expert's) representations of some task, activity, event or scene, and of the knowledge they use to generate and interpret behaviour (e.g. problem-solving behaviour) in that context. In each case, the interviewer will bring only a bare minimum of prior assumptions into the interviews in the recognition that an understanding of the actor's behaviour (including, of course, verbal behaviour used in reporting) can only be achieved through an understanding of the underlying knowledge structures and cognitive processes. Consequently:

you don't start getting any information from an utterance or event until you know what it is in response to – you must know what question is being answered. It could be said of ethnography that until you know the question that someone in the culture is responding to you cannot know many things about the responses. Yet the ethnographer is greeted, in the field, with an array of responses. He needs to know what questions people are answering in their every act. He needs to know which questions are being taken for granted because they are what ‘everybody knows’ without thinking ... Thus the task of the ethnographer is to discover questions that seek the relationships among entities that are conceptually meaningful to the people under investigation. (Black and Metzger, 1964, p. 144; quoted in Spradley, 1980, p. 32)

We suggest that the initial stage in formulating a description of the cooperative work activity (and the concomitant C-STRUCTURE emerging from collaborating ROLES) should be the determination, by interviewing ('grand tour' questions) and observation, of the following components (adapted from Spradley, 1980, p. 78):

(i) Actors Identify the people involved in the work group. Allow the actors themselves to demarcate the boundaries of the work group. A sociometric analysis, based on interview and observation, might produce a sociogram that can then be checked back with the actors for confirmation. Members of the work group should themselves be allowed to identify particular kinds of actor: do actors have descriptive names? are the descriptions done by others or by themselves? do they accept these descriptions? is there an acknowledged coordinator of the activity? is there an agreed social structure in the team? etc.

(ii) Goal/task The identification of the actors in (i) will have been done on the basis of a preliminary conceptualization of the ACTIVITIES undertaken by the work group in the EVENTS in which they participate. Actors are asked to name and describe the tasks undertaken individually and collectively by the group.

(iii) Event This is the set of related ACTIVITIES that actors carry out. 'Design Review', e.g. will in one of its interpretations constitute an event made up of a sequence of activities. How do participating actors characterize the event?

(iv) Objects This will include not only the physical and conceptual objects involved in the narrowly technical dimension of the problem-solving activity (the 'domain conceptualisation') but also all other objects that actors interact with: telephone, fax, photocopier, coffee machine, ...

(v) Resources What are the resources used in the task, as identified by the actors themselves? Time? other people (including support staffs)? white boards? etc

(vi) Activities What are the activities that constitute the EVENT? How is the performance of these activities distributed across the work group? Do individual actors undertake discrete tasks?

(vii) Acts Identify a set of low-level (atomic) constituent acts of each of the activities. Again, the actors themselves will determine what count as ‘acts’.

(viii) Time Activities take place over time. Some is subjective time, rather than clock time. How do actors conceptualize the temporal dimension of an EVENT? e.g. do activities and acts take place relative primarily to external temporal constraints (schedules, deadlines, ...) or to each other?

(ix) Space Actors work in physical environments, and the topography of the environment may to some degree affect work practices; consequently it should be described. Actors are asked to describe places and locations in detail; to describe ways in which space is used by actors; the ways in which space is organized by objects, acts, activities and events; the ways space is related to goals, etc.

(x) Feeling How people feel about the work they do and about the others they work with is likely to have some influence on the way the work is done. Actors will also have personal goals and objectives. Actors are thus probed for the affective correlates of goals, events, fellow actors, time, and so on.

As a simple example, with regard to ACTORS, there is often a systematic variation in the way experts refer to and talk with employees of the organization and their colleagues. Thus, in the O-STRUCTURE, the people working in the department may be referred to in terms of their hierarchized and purely structural (job titles) as line managers, line engineers, branch engineers and so on, whereas in the context of C-STRUCTURE the same individuals may be referred to non-hierarchically as kinds of 'people', e.g. 'engineering people', 'customer support people', 'service people' and so forth, as front-line participants in the activities undertaken by the work group.

Such initial data will suggest the types of questions that might appropriately and productively be asked in subsequent stages of the analysis, leading finally to a rich description of the C-STRUCTURE and of the roles that constitute it.

## Conclusions

We have argued that understanding how an organization and its constituent workgroups operate, and consequently an understanding of the culturally-embedded semiotic that underpins communicative and collaborative behaviour in the work group, is dependent upon a recognition of the emergent C-STRUCTURES. We proposed that the successful design of NGISs must be founded upon:

an understanding of the social and organizational setting of work, and of the distinction between the abstract ORGANISATION and the concrete STRUCTURE, as well as between the OFFICE and ROLE

the formal modelling not a single user (problem-solver) but of the whole work group

## We argued that:

domain knowledge must in consequence be elicited from multiple sources, including all members of the cooperative work team, and that:

an ethnography of work' might generate a multidimensional (actor, goal, event, objects, resources, activities, acts, time, space, and feeling) representation of group work that will constitute the data input for the formal modelling of the behaviour of the cooperative work team

As a postscript, it is worth noting that, although in this paper our explicit interest has been in business and public sector organizations, many of the remarks will be of equal relevance to other kinds of user (e.g. the introduction of computer-based learning in schools, on-line catalogues for library users, multimedia information systems in public galleries and museums) as well as to much larger social groupings (e.g. the impact of IT on third world cultures). Since in general terms the value of a technology may be measured in large part by the quality of the service it enables the organization to provide to its clients, then if an IS in its design embodies assumptions that bias or too narrowly constrain the information it delivers – if ‘what is incarcerated in the officially approved software defines the borders of permitted thinking’ (Large, 1986, p. 5) – the system, even when, from a software engineering point of view, ‘successfully’ integrated into and used by the organization, may not, from an information engineering perspective, be providing optimal solutions for the client. The impact on the social environment (including the manner and ratiocinative style with which the system seeks to meet the client's informational requirements, and the consequences for the client group) of the use of computer information systems by organizations was not a direct issue for the present paper, though in a very narrow and specific sense we have been concerned with cultural presuppositions with regard to what it is that NGISs actually do.

## References

Albrow, M. (1980) The dialectic of science and values in the study of organizations, in Control and Ideology in Organizations, Salaman, G. and Thompson, K. (eds), (The Open University Press, Milton Keynes).

Barnard, C. I. (1970) Cooperation, in The Sociology of Organizations: Basic Studies, Grusky, O. and Miller, G.A. (eds), (The Free Press, New York).

Bateson, G. (1973) Steps to an Ecology of Mind, (Paladin, London).

Berger, P.L. and Berger, B. (1976). Sociology: A Biographical Approach, (Penguin, Harmondsworth).

Berger, P.L., Berger, B. and Keller, H. (1973) The Homeless Mind (Penguin, Harmondsworth).

Bernstein, B. (1971) Class, Codes and Control. Volume 1: Theoretical Studies towards a Sociology of Language (Routledge & Kegan Paul, London).

Bittner, E. (1974) The concept of organization, in Ethnomethodology, Turner, R. (ed.) (Penguin, Harmondsworth).

Black, M. and Metzger, D. (1964) Ethnographic description and the study of law, in The Ethnography of Law, Nader, L. (ed.), (special issue of American Anthropologist, 67(2), pp. 141–65).

Blau, P.M. and Schoenherr, R.A. (1971) The Structure of Organizations (Basic Books, New York).

Blumer, H. (1969) Symbolic Interactionism (Prentice Hall, Englewood Cliffs, NJ).

Bormann, E.G. (1983) Symbolic Convergence: Organizational Communication and Culture, in Communication and Organizations: An Interpretive Approach, Putnam, L.L. and Pacanowsky, M.E. (eds), (Sage Publications, Beverley Hills).

Brittan, D. (1992) Being there: the promise of multimedia communications, in Readings in Groupware and Computer-Supported Cooperative Work, Baecker, R.M. (ed.), (Morgan Kaufmann Publishers Inc. 1993; San Mateo, C.A.)

Deal, T.E. and Kennedy, A.A. (1982) Corporate Cultures: The Rites and Rituals of Corporate Life (Addison-Wesley; Reading, MA).

Dennett, D.C. (1978) Brainstorms (The MIT Press, Cambridge, MA).

Devlin, K. and Rosenberg, D. (1993) Situation theory and cooperative action, in Situation Theory and Its Applications, Vol. 3, CSLI Lecture Notes No. 37, Aczel, P., Israel, D., Katagiri, Y. and Peters, S. (eds), (Centre for the Study of Language and Information, Stanford University).

Devlin, K. and Rosenberg, D. (1994). Networked Information Flow via Stylized Documents (in preparation).

Durkheim, É. (1937) Les règles de la méthode sociologique (Presses Universitaires de France, Paris) [First French edition, 1895].

Etzioni, A. (1970) A Comparative Analysis of Complex Organizations (The Free Press, New York).

Fauconnier, G. (1985) Mental Spaces: Aspects of Meaning Construction in Natural Language (MIT Press, Cambridge, MA).

Garfinkel, H. (1967) Studies in Ethnomethodology (Polity Press, Cambridge).

Goodenough, W. (1957) Cultural Anthropology and Linguistics, in Report of the Seventh Annual Round Table Meeting on Linguistics and Language Study, Garvin, P. (ed.), (Georgetown University Press, Washington).

Hewett, C. (1986) Offices are open systems, ACM Transaction on Office Information Systems, 4(3), 271–87.

Huczynski, A. and Buchanan, D. (1991) Organizational Behaviour (2nd edn) (Prentice Hall, London).

Hutchison, C.S. (1988) New York is on the line: issues in the interpretation of referring expressions (MS of staff seminar, Kingston Polytechnic, June)

Hutchison, C.S. (1993) The shared knowledge paradox and the objectivity of knowledge and belief. Proceedings of the 13th International Congress on Cybernetics (Namur, Belgium, 24–28 August 1992).

Hutchison, C.S. (1994) Patterns of language in organizations: implications for CSCW, in Design Issues in Computer-Supported Co-operative Work, Rosenberg, D. and Hutchison, C.S. (eds), (Springer-Verlag, London).

Hutchison, C.S. and Rosenberg, D. (1991) Human-Centred Knowledge Elicitation (KIS Working Paper, Kingston University).

Hutchison, C.S. and Rosenberg, D. (1993) Conflict and Cooperation in knowledge-intensive computer-supported cooperative work, in CSCW: Cooperation or Conflict?, Easterbrook, S. (ed.), (Springer-Verlag, London).

Jeffcoate, J., Li, M.-S. and Timms, S. (1993) Networked Multimedia: The Business Opportunity, (Ovum Press, London).

Kahn, R.L., Wolfe, D.M., Quinn, R.P and Snoef, J.D. (1964) Organizational Stress: Role Conflict and Ambiguity, (John Wiley, New York).

Kempson, R.M. (1977) Semantic Theory (Cambridge University Press, Cambridge).

Kilmann, R.H., Saxton, M.J. and Serpa, R. (1985) Gaining Control of the Corporate Culture (Jossey-Bass, San Fransisco).

Large, P. (1986). Is AI a notifiable disease? in Artificial Intelligence for Society, Gill, K.S. (John Wiley & Sons, Chichester).

Lave, J. (1988) Cognition in Practice (Cambridge University Press, New York).

Leavitt, H.J. (1951) Some effects of certain communication patterns on group performance. Journal of Abnormal Social Psychology, 46, 38–50.

Louis, M.R. (1980) Surprise and sense-making: what newcomers experience in entering unfamiliar organizational settings. Administrative Science Quarterly, 23, 225–51.

Malone, T.W. (1987) Modelling coordination in organizations and markets. Management Science, 33(10), 1317–32.

Manis, J. and Meltzer, B. (eds) (1967) Social Interaction: A Reader in Social Psychology (Allyn and Bacon, Boston).

Manning, P.K. (1971) 'Talking and becoming: a view of organizational socialization', in Understanding Everyday Life, Douglas, J.D. (ed.), (Routledge & Kegan Paul, London).

March, J.G. and Simon, H.A. (1958) Organizations (Wiley, New York).

McGraw, K. and Harbison-Briggs, K. (1989) Knowledge Acquisition: Principles and Guidelines (Prentice Hall, Englewood Cliffs, NJ).

Mead, G.H. (1962) Mind, Self, and Society (University of Chicago Press, Chicago).

Morgan, G. (1986) Images of Organization (Sage, Beverly Hills).

Mullins, L.J. (1989) Management and Organizational Behaviour (2nd edn), London: (Pitman, London).

Nirenburg, S. and Lesser, V. (1986) Providing intelligent assistance in distributed office environments. Proceedings of the ACM Conference on Office Information Systems, pp. 104–12.

Parsons, T. (1970) Social Systems, in The Sociology of Organizations: Basic Studies, Grusky, O. and Miller, G.A. (eds) (The Free Press, New York).

Peters, T.J. and Waterman, R.H. (1982) In Search of Excellence: Lessons from America's Best-Run Companies, (Harper & Row, New York).

Rosenberg, D. (1988) Knowledge acquisition for interaction with expert systems in manufacturing (Kingston Polytechnic: CIM Centre Technical Report No. 067).

Rosenberg, D. and Hutchison, C.S. (eds) (1994) Design Issues in CSCW (Springer-Verlag, London).

Salaman, G. (1980) Roles and Rules, in Control and Ideology in Organizations, Salaman, G. and Thompson, K. (eds), (The Open University Press, Milton Keynes).

Silverman, D. (1970) The Theory of Organizations (Heinemann, London).

Simon, H.A. (1972) Theories of bounded rationality, in Decision and Organisation, Rander, C.B. and Rander, R. (eds), (North Holland, Amsterdam).

Simon, H.A. (1976) Administrative Behaviour: A Study of Decision-Making Processes in Administrative Organization (3rd edn) (The Free Press, New York).

Spradley, J.P. (ed) (1970) You Owe Yourself a Drunk: An Ethnography of Urban Nomads (Little, Brown, and Co, Boston).

Spradley, J.P. (1980) Participant Observation (Holt, Reinhart & Winston, London).

Spradley, J.P. and McCurdy, D.W. (1972) The Cultural Experience: Ethnography in Complex Society. (Science Research Associates Inc, Chicago).

Stewart, R. (1972) The Reality of Organizations (Pan Books, London).

Turkle, S. (1984) The Second Self: Computers and the Human Spirit (Granada Publishing Ltd, London).

Weber, M. (1957) The Theory of Social and Economic Organization. Translated by Henderson, A.M. and Parsons, T. (The Fress Press, Glencoe, IL) [First German edition, 1922].

Weeks, D.R. (1980) Organizations: interaction and social processes, in Control and Ideology in Organizations, Salaman, G. and Thompson, K. (eds) (The Open University Press, Milton Keynes).

Winograd, T. and Flores, C.F. (1986) Understanding Computers and Cognition. (Ablex Publ. Corp, Norwood, NJ).

## Biographical notes

Chris Hutchison has been a senior lecturer in information systems at Kingston University since 1988. He previously lectured in linguistics at the universities of East Anglia, Amsterdam, and Mohammed V University (Rabat), and in Artificial Intelligence at Sussex University. His main research interests are in the areas of linguistics, CSCW, and the ethnology of work.

Duska Rosenberg has been a lecturer in computer science at Brunel University, UK, since 1989. She was previously a research fellow and lecturer in the School of information systems at Kingston University, UK. Her background is in linguistics, anthropology, and computer science. Her major interests are in linguistic semantics, CSCW, and computational linguistics.

Address for correspondence: Chris Hutchison, Department of Information Systems, Kingston University, Penrhyn Road, Kingston, Surrey KT1 2EE, UK.
