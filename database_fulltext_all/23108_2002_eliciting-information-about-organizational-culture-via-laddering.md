---
otero_id: 23108
otero_key: "H5SVPDKJ"
title: "Eliciting information about organizational culture via laddering"
authors: "Gordon Rugg; Malcolm Eva; Atiya Mahmood; Nazia Rehman; Stephanie Andrews; Sarah Davies"
year: "2002"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.2002.00124.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Eliciting information about organizational culture via laddering

Gordon Rugg\*, Malcolm Eva, Atiya Mahmood, Nazia Rehman, Stephanie Andrews & Sarah Davies

\*Department of Computer Science, Keele University, Keele, Staffordshire ST5 5BG, UK, e-mail: g.rugg@cs.keele.ac.uk

Abstract. Eliciting information about organizational culture is an important part of system analysis and design. However, eliciting knowledge of this sort is difficult. Laddering is an established technique that is particularly suitable for eliciting information about goals and for eliciting explanations, which are important issues when investigating organizational culture. This paper describes the method, its strengths and limitations, its use in several case studies and its relation to other elicitation techniques. Recommendations for further work are given.

Keywords: Laddering, personal construct theory, organizational culture, system analysis

## INTRODUCTION

It has long been known that installing a technological solution into an organization has an impact beyond that of simply reorganizing a set of tasks. The classic approach to this area is the sociotechnical approach, as exemplified by work by the Tavistock Institute (e.g. Trist & Bamforth, 1951). It is clear from work in this tradition that the structure of a task interacts with various aspects of the culture of the organization – for instance, in the Trist and Bamforth example, with the group dynamics of the miners. ‘Culture’ is a term that can be defined in various ways; for the purposes of this paper the term is used in the broad sense to refer to shared attitudes, norms, goals, values and behaviours within a group or organization. The examples of laddering in the text cover a wide range of areas, hence the broad definition.

Attempts have been made to predict and engineer the organizational impact of technological change, both during the analysis and design phase, as in ETHICS and ISAC (Lundberg et al., 1982; Mumford, 1995), and in the larger framework of an approach such as adaptive structuration theory (De Sanctis & Poole, 1994).

Although there has been a long-standing awareness of both the problem of culture interacting with technology and the need for a rigorous, valid and practical methodology for modelling this interaction, results so far have been less than overwhelming. One possible explanation for this involves the methods used to elicit information about an organization’s culture, and to model the information elicited. The importance of elicitation method as a variable has been recognized for some time in other fields. In knowledge acquisition, for instance, the concept of the ‘knowledge acquisition bottleneck’ (Barr & Feigenbaum, 1982) is so familiar as to be something of a cliché (Cullen & Bryman, 1988), and in requirements engineering there is at least one formal model of elicitation methods for which the main function is to provide theoretically grounded guidance on the choice of the appropriate elicitation method for a particular problem (Maiden & Rugg, 1996).

Approaches that have been mooted for developing a model of culture derive from semiotics (e.g. Liu & Sharp, 1997) and anthropology (Stamper, 1985). Although these can provide valuable models for interpreting a culture, eliciting the data to feed these models is far more problematic. Anthropological methods tend to produce data in a form that does not lend itself readily to integration with traditional system analysis and design methods. Interviews (structured or semistructured) and questionnaires are used by consultants who specialize in cultural analysis (Brown, 1998), and are widely used throughout system analysis, together with various forms of observation. However, the continuing problem of modelling culture strongly suggests that these methods have not proved themselves to be adequate or appropriate for this task, for whatever reasons, and that there is a need for other techniques to elicit information about culture.

A technique well suited to eliciting information about culture, but not widely known in the information systems community, is laddering. This technique was originally developed to elicit and model information about goals, aims and values, which are key components in models of culture. Laddering is well established in other areas, such as knowledge acquisition for expert systems (Rugg & McGeorge, 1995) and requirements acquisition (Maiden & Rugg, 1996), and has been shown to perform well in comparison with other techniques (Corbridge et al., 1994). This paper describes the technique, with examples of its use in eliciting information about organizational culture and information systems development.

Laddering originated in Kelly’s personal construct theory (Kelly, 1955), which was one of the early cognitive approaches and which is still influential and flourishing in psychology. Personal construct theory (PCT) is notable for its emphasis on combining validity of information elicited with rigour and measurement, in contrast to less formalist approaches favoured in psychiatry and in some areas of clinical psychology. The main tool used for this in early PCT was the repertory grid, which is widely used in fields ranging from market research to knowledge acquisition. A drawback of the repertory grid is that it handles only element–construct– value triplets (corresponding closely to the more familiar object–attribute–value triplets of software engineering, but preceding them by some years). The traditional repertory grid is not conveniently able to represent hierarchies of knowledge types such as goals, class memberships or explanations, and laddering was developed by Hinkle ( 1965) as a reaction to this need.

Laddering superficially resembles some types of structured interview, in that it consists in a series of natural language questions and answers based around a limited set of probes. Like interviews and questionnaires (but unlike some other techniques, such as observation and ethnographic approaches) laddering therefore deals with the front (i.e. public consumption) rather than the back (i.e. behind the scenes) version of reality, to use Goffman’s dramaturgical metaphor (Goffman, 1959). The obvious problem with this is the validity of the information being elicited. To some extent, validation can be carried out by cross-checking with results from other approaches such as direct or indirect observation, but the issue of validity remains one to be treated with caution.

There are other grounds for caution when dealing with data gathered using techniques based on respondents’ verbal accounts. Even if access is gained to the back version of events, human memory is liable to numerous well-documented distortions, biases and other imperfections, as has been demonstrated in a considerable body of psychological research, notably that by Bartlett (e.g. Bartlett, 1932), Loftus (e.g. Loftus & Palmer, 1974) and Baddeley (e.g. Baddeley, 1990). In addition, human cognition is prone to various biases in interpreting evidence before it is committed to memory (e.g. Kahneman et al., 1982) and in interpreting the framing of a question (e.g. Kahneman et al., 1982).

There has been a long and frequently heated debate within the psychological community about the extent to which responses are affected by the way in which questions are asked (whether in terms of specific phrasing or more general observer effects). The naive view that respondents will tend to say what they believe the experimenter wants them to say has been discredited for some time as too simplistic (cf. Wuebben et al., 1974). However, there is complex and ambiguous evidence for robust effects arising from the framing of the question (as opposed to the experimenter’s perceived aims). There is, for instance, apparently robust evidence for systematic cognitive shortcomings relating to people’s judgement and decision making (e.g. Kahneman et al., 1982), but it has been argued that these are purely an artefact of a probabilist rather than a frequentist presentation (e.g. Gigerenzer, 1994). This debate extends beyond the scope of the present paper, but any investigator using verbally based approaches such as interviews, questionnaires or laddering would be well advised to study the relevant literature with care.

Laddering was originally developed by Hinkle to investigate superordinate goals. In addition to its application in knowledge acquisition and requirements acquisition described above, laddering has also been used in a variety of areas, including advertising (Reynolds & Gutman, 1988) and architecture (Honikman, 1977). In the domain of knowledge acquisition, an automated version of the technique is included in AQUINAS (Boose & Bradshaw, 1988), and there is also a stand-alone laddering tool, CATO (Major & Reichgelt, 1990). The technique is described briefly in Bannister & Fransella ( 1980) and in more depth in Rugg & McGeorge (1995) and Reynolds & Gutman (1988). Although the underlying concept is the same, each of the authors above uses slightly different versions of the approach to suit the different purposes for which it is being used. The versions most accessibly described are those used by Rugg & McGeorge and by Reynolds & Gutman; the latter, however, was developed for use in market research, so the version described in this paper is that of Rugg & McGeorge unless otherwise stated.

Laddering operates by modelling knowledge as a set of hierarchies. These hierarchies may be hierarchies of goals, tasks, explanations, etc. A small set of probes is used to elicit knowledge and information from the respondent, in a form reflecting this hierarchical structure. This has various advantages from a computational perspective. Hierarchies of this sort lend themselves readily to representation using classic knowledge representation formalisms, such as class hierarchies with inherited attributes, and to automation, as in ALTO (Major & Reichgelt, 1990), so it is unsurprising that the technique has been favourably received in the knowledge acquisition and requirements acquisition communities. In addition, although the technique was designed to probe individuals’ personal views of reality, the formalism of its knowledge representation is in noticeable contrast to the imprecision of more recent approaches such as soft systems methodology (Checkland, 1981), and is another advantage to elicitors dealing with phenomena as ‘soft’ as culture.

Although laddering is designed to be used to elicit hierarchically organized knowledge, it is explicitly recognized in the literature that not all knowledge can be validly represented in this way, and that it is necessary for the elicitor to ensure that the domain is appropriate for laddering, as described below.

## LOCATING LADDERING IN RELATION TO OTHER TECHNIQUES

Laddering is only one of many techniques for eliciting information about organizational culture. The issue of choice of elicitation technique is one which has received considerable interest recently in the field of requirements engineering, and a model from this area (Maiden & Rugg, 1996) provides a convenient framework for locating laddering in relation to the other elicitation techniques available, and for deciding whether a domain is appropriate for the use of laddering.

A key aspect of this model is its categorization of knowledge and memory types, which are then used to guide selection of elicitation technique. Maiden & Rugg distinguish between explicit, semitacit and tacit knowledge, as well as future systems knowledge.

Future systems knowledge is treated as not being knowledge in the strict sense, as it deals with what is wanted from a system that does not exist yet; future systems knowledge is treated as a process of negotiation and discovery, rather than elicitation of existing knowledge. A more detailed discussion of this is provided by Rugg & Hooper (1999).

Explicit knowledge is knowledge that is reliably accessible to introspection. A widespread and mistaken belief is that all knowledge is of this sort, which has serious implications for choice of elicitation technique.

Tacit knowledge, in contrast, is knowledge that is not reliably accessible to introspection. A typical example is touch typing. Experts in tacit skills typically perform much better than novices, but are completely unable to introspect reliably into how they perform the task. A simple example is to ask a touch typist which key is to the right of ‘g’; most touch typists have to visualize themselves typing in order to answer the question, even though the relevant key (‘h’) is one which they use frequently. It appears likely that some skills begin as non-tacit skills but then become tacit with practice (compiled skills; see Neves & Anderson, 1981). Others are learned without conscious intervention at any point (implicit learning; see Seger, 1994). The details of these mechanisms are outside the scope of this paper, but it is important to note that there may be significant mismatches between what respondents believe they are doing and what they are actually doing, when tacit knowledge is involved.

Semitacit skills, memory and knowledge include a variety of phenomena. One obvious example is short-term memory (STM) (Miller, 1956), which has a limited capacity of seven plus or minus two items, which are normally forgotten within a few seconds. STM is important in areas such as design of computer interfaces; it is clearly only accessible while in use, and the only method able to access it is on-line self-report. Other examples in this category include front and back versions (Goffman, 1959), recall versus recognition (Eysenck & Keane, 1995) and taken for granted knowledge (Grice, 1975).

A key finding from this work is that no single technique is able to elicit all types of knowledge, and that use of any technique needs to be guided by an understanding of the types of knowledge which that technique can and cannot handle. It is likely that systematic combinations of two or more techniques will be increasingly used in the future.

## IDENTIFYING SUITABLE DOMAINS FOR LADDERING

In general, laddering works well for handling explanations, goals and sequencing of cognitive tasks; however, it is not suitable for purposes such as eliciting detailed information about skilled physical tasks, as in these tasks tacit knowledge may be involved.

Two simple methods of checking for the presence of tacit knowledge are noting the speed with which the relevant task is performed and noting whether the respondent can carry out a conversation while performing the task. If the task is carried out at high speed, without visible pauses for thought, and/or the respondent is able to carry out a conversation while performing the task, then tacit knowledge is likely to be involved, and techniques dependent on introspection such as interviews, questionnaires and laddering will encounter problems with validity. In such cases, non-verbal techniques such as observation are more likely to obtain valid results.

The interaction between explicit and tacit knowledge, values and beliefs is an issue which remains obscure, and any investigation of a topic as hotly debated as ‘culture’ should be undertaken with appropriate caution. The psychological literature in this field demonstrates the need for caution – for instance, at a general level, it has been argued that much of cognition and its associated behavioural markers is seen as being independent of conscious initiation (e.g. McGeorge et al., 1997). More specifically, there is evidence that attitudes can be activated without conscious awareness (e.g. Greenwald & Bannaji, 1995) and that environmental stimuli can directly activate a goal which can then guide cognitive and behavioural processes without the need for conscious decisions (e.g. Bargh, 1997). Any information about goals and values elicited verbally from respondents should therefore be treated with caution, whether it is derived from interviews, questionnaires or laddering. In the following discussion, for brevity, it is assumed that the system developer is aware of this problem, and will be on the look-out for mismatches between verbal accounts and reality.

Being able to elicit explanations and higher-level goals has obvious implications for investigation of culture. Explanation makes it possible to understand what is meant by the concepts that are important in a given culture; higher-level goals and values are widely claimed to be an important part of a culture (e.g. Blanchard & O’Connor, 1997), although, as should be clear from the discussion above about tacit knowledge, this is a claim which might well repay serious and skeptical investigation. It is perfectly possible to elicit information about both these areas without using laddering. However, as shown in the examples below, the use of a formal, systematic approach has considerable advantages, both practical and theoretical. A brief explanation of laddering follows.

## LADDERING PROCEDURES AND CONCEPTS

Laddering begins with an arbitrarily chosen item, the seed item, and then proceeds outwards from the seed item in the direction chosen by the elicitor. The elicitor operates by using a small set of standard questions (probes) to move in the various directions, and uses a set of standard notations to record questions and answers.

The directions available are upwards, sideways and downwards. Laddering explicitly assumes that the respondent can categorize knowledge from each of several viewpoints (facets) so that the same item may be categorized quite differently on different facets. For instance, on the facet of Linnean taxonomy, pine martens and sea otters are located close to each other, both being mustelids; however, on the facet of preferred habitat, the two species are located far apart, with pine martens living in tree tops and sea otters living in the sea. Apparently inconsistent results obtained using other techniques to elicit preferences may be due to respondents switching from one facet to another during elicitation.

The facets may be of several types, such as goals, explanations or class membership. Each of these requires a different phrasing of the probe. Wording of the probes is an important issue; although some variation during a session is advisable to prevent boredom, this needs to be done with care. In the case of eliciting information about goals, for instance, the question: ‘Why would you do $\times ?$ could either elicit a forward-looking response (‘I did X in order to achieve Y’) or a backwards-looking response (‘I did X because of previous event W’) depending on context.

Upwards laddering elicits information about higher-level goals or categories: for instance, ‘Why would you prefer X to $\Upsilon ?$ or ‘What is X a type of?’ This process can be repeated until it is not possible to go any further upwards (‘topping out’). In the case of goals, this is because the elicitation session reaches top level goals, beliefs, etc. In practice, it is advisable to proceed with caution at the higher levels, because respondents become uneasy about discussing their core beliefs; it is good practice to stop before the respondent becomes embarrassed. Topping out normally occurs surprisingly quickly, within a few upwards levels.

This approach can be applied to investigation of cultural norms, by investigating which higher-level goals are involved in lower-level preferences, and by comparing the higher-level goals in the belief systems of different social or organization cultures. Examples of this are given in the case studies below. Because the probes elicit short chunks of information at a time, it is usually quite easy to compare results across respondents. At the same time, the respondents are able to answer using the phrasing of their choice, so laddering offers a useful combination of formalism with naturalism.

Laddering may also proceed downwards, to elicit explanations or members of classes; for instance, ‘How could you tell that something was an $\times ?$ or ‘Could you give me some examples of $\times ?$ In the case of organizational culture, for example, the concept of ‘professionalism is widespread, but may be interpreted very differently in different cultures. As with upwards laddering, downwards laddering proceeds through successive layers until it is not possible to go any further (‘bottoming out’). Elicitation of explanation will proceed through explanations of the terms used in the explanations of the explanations, and so forth, until none of the terms reached needs any further explanation.

Laddering may also proceed sideways, either to find other examples at the same level (‘Could you give me some more examples of types of $\times ? )$ or for the quite different purpose of eliciting a different concept or facet via a differentiation probe (‘What is the main single difference between X and Y?’).

As this form of laddering is explicitly based in part on graph theory, it is possible to use concepts from graph theory to gain richer information from the sessions. For instance, it is possible to count the layers of explanation before bottoming out occurs (elucidatory depth) and to use this to measure domain complexity. Elucidatory depth is usually between one and seven layers. It is also possible to count the total number of entities elicited below or above a seed item and to use this as a metric of quantity of knowledge in that part of the domain.

As with upwards laddering, responses in sideways laddering are typically brief, and can be readily compared across respondents, in terms of either verbatim agreement (exactly the same words being used in a term) or gist agreement (different words being used which have the same underlying meaning, as assessed by independent judges).

Although laddering makes use of graph theory, it is not practical to record the session using a graph-style notation, because this rapidly expands to an unmanageable size during the session. Rugg & McGeorge (1995) recommend recording each question and its associated answer as a separate chunk, with a small number of standardized notations to show the probe being used: an upward arrow to show an upward goal probe, a downwards arrow to show an explanation probe, an underline beneath an item to show a subcategory, and a double-headed arrow between two items for a differentiation probe. This makes it possible to record the session on paper in something close to real time.

Two features of laddering that tend to surprise novices are the speed with which it can access core beliefs and the way in which those core beliefs can be completely unexpected to the elicitor. An example from a pilot session illustrates this (Bassi, 1998). The respondent was asked whether she would prefer a colour advertisement or a black and white advertisement for an IT product. Her response was that she would prefer the colour advertisement; this was followed by an upward goal probe. Successive upward goal probes elicited the information that the respondent would prefer the colour advertisement because it would be easier to see; that she would prefer this because she would not need to wear glasses; that she would prefer this because it would make her look more attractive; and that she would prefer this because it would increase her chances of finding a husband.

Although this case was a particularly striking one, it was consistent with the data from the subsequent main study, which found two main clusters of top-level goals in the domain of choosing personal IT equipment. One of these clusters consisted of goals relating to social values (the IT equipment as status symbol) and the other consisted of goals relating to function (the IT equipment as a means to achieve work-related goals). The practical significance of such effects for system developers is that stakeholders may appear to be in agreement because they share the same preferences about available options; however, this appearance may mask deep divisions about higher-level goals, if two stakeholders prefer the same option for completely different reasons.

The following case studies provide examples of laddering being used to investigate various aspects of culture, goals and explanation. The first two examples involve culture and change. The third involves explanation within the same social culture.

## Example 1: within-culture comparison of perceptions of innovation

In this example, an organization about to introduce a new IT system was investigated, first using a questionnaire and then using the Reynolds and Gutman version of laddering on the same respondents, to investigate attitudes towards the new technologies. The sample consisted of 21 respondents.

It is relatively simple to perform content analysis on the results of laddering sessions, which can then be compared directly with content analysis results derived from other techniques. In this case, for instance, one noticeable difference between results from the two techniques was that only one respondent stated in questionnaire sessions that the technology would increase their job security, whereas 9 of the 21 respondents stated in laddering sessions that the technology would increase their job security.

Analysis of the number of levels of goals provided some other interesting results. A counterintuitive finding was a tendency for the number of levels of goals relating to the new technology to be smaller for respondents higher in the organizational hierarchy (mean = 1.9) than for respondents lower in the organizational hierarchy (mean = 3.7). This was because respondents higher in the organizational hierarchy tended to move from the seed item directly towards benefits to the organization, whereas respondents lower in the organizational hierarchy tended to move first towards benefits to themselves, then to benefits to the organisation, and then back again to benefits to themselves. The reasons for this difference between groups are debatable, and it would be inadvisable to take the managers’ apparent lack of self-interest completely at face value. The point remains, however, that the difference occurred, whatever its reasons, and was detected as a routine outcome of quantitative analysis of the laddering results.

## Example 2: between-culture comparison of perceptions of innovation

The second example involves two respondents who had been previously asked to describe themselves in relation to the groups or cultures to which they perceived themselves as belonging (their reference groups). The phrasing was deliberately open, so that respondents could describe their affiliation in terms of anything from politics to football club supported; the purpose was to identify the memberships which the respondents considered important in relation to their own identity. The respondents used in this example had described themselves in terms of religious affiliation: one Protestant, one Roman Catholic.

There are some striking anecdotal examples in the laddering literature of religious beliefs figuring in high-level goals; the widespread concept of the ‘Protestant work ethos’ would also predict that religious affiliation ought to appear as a factor in the high-level goals of the two respondents, but in this example that was not the case. Although it would be unwise to read much into a sample of two respondents, the example below demonstrates how laddering can be used to investigate a cultural concept such as ‘the Protestant work ethos’, which would usually be viewed as too vague a concept to be investigated in any systematic manner.

The successively higher level goals mentioned by the first respondent (a Protestant) in relation to choice between swipe cards and payment books for welfare benefit claims are as shown in Figure 1 (highest level goal at the top)

The corresponding goal chain for the second respondent (a Catholic) is shown in Figure 2.

The similarities between the two goal chains are striking. The similarities extend across other goal sequences for the two respondents. Each respondent separately identified five likely changes in their workplace, and four of these were identified by both respondents, including the swipe card example above. The top level goals for the three remaining changes were as follows:

![](/api/attachments/H5SVPDKJ/fulltext/images/43f4e63d4d18f5f4966421355e6f5b1d7fd1a8d9adea90d79ad1099700a8dcae.jpg)  
Figure 1. Higher-level goals for first respondent.

![](/api/attachments/H5SVPDKJ/fulltext/images/d744c231f4fea5c0a6e0289426d1ef63cdbc9f698cda085b022b32b1cb27ac52.jpg)  
Figure 2. Higher-level goals for second respondent.

Respondent 1: so [we] don’t fall behind.

Respondent 2: enable [the organization] to maintain their position/stability in the market

Respondent 1: [avoiding] loss of profit.

Respondent 2: more successful.

Respondent 1: more job satisfaction.

Respondent 2: government will be able to retain the business and [be] less likely to privatize.

For the remaining changes, the top level goals were:

Respondent 1: increase custom levels and profit turnove.

Respondent 2: this will help balance ecology.

Although these responses do include ethics-related goals (e.g. ‘job satisfaction’ and ‘balance ecology’), the majority are function related, which is consistent with a strong organizational culture being used as the primary means of assessing work-related goals and values. This is also consistent with the goal chains in example 1 above. The absence of explicit links to religion is explicable in terms of the respondents using a limited set of facets to handle this part of their life. This can either be taken to mean that they do not construe their work in relation to their religion or to mean that the nature of their work seldom overlaps with the issues salient to their religion. An alternative explanation is that any religious factors were treated as implicit by both respondents, although both respondents used religion as an explicit part of their cultural self-definition. Either way, it is interesting that the similarities between the two respondents’ goal chains are much more noticeable than their dissimilarities.

![](/api/attachments/H5SVPDKJ/fulltext/images/598a33761d064e8cb097a19f7cbb96048369d12e359980b31dfe96a50cb940c6.jpg)  
Figure 3. Top-level tasks for logging onto the Internet and finding a given site.

## LADDERING ON EXPLANATIONS

An important issue in understanding culture is being able to make explicit what is meant by terms, to ensure that everyone involved understands the same term in the same way. This is relevant both in investigating culture (whether social or organisational) and in relation to aspects of IT system development such as explanation facilities, described below.

## Example 3: elicitation of explanations

This example involved using laddering to elicit information about how to log on to the Internet and find a given web site. An initial laddering session produced the set of top-level tasks shown in Figure 3. For reasons of space, only the first half are listed. Each was then broken down by asking, ‘How would you . . .?’. The question ‘How would you double click on “Internet services”?’ produced the response:

Place cursor over ‘Internet services’.

• Double click left mouse button.

![](/api/attachments/H5SVPDKJ/fulltext/images/46ceb601190f8fe7d44abc0f6ae69766c7574a9518a62f1ff11e230d7242b246.jpg)  
Figure 4. Top-level explanations of ‘mouse’.

At this point the elicitor decided that the explanation was sufficiently specific, and moved on to explanations of the next step requiring explanation on the top-level list. However, anyone who has ever attempted to teach total novices will be well aware that this explanation still needs further breaking down: total novices do not always know what a mouse is. A separate session investigating this with another respondent produced the explanation of ‘mouse’ shown in Figure 4.

An important advantage of the formal, systematic nature of laddering is that it helps with elucidation of agreements or disagreements between different people, when terms are broken down into more specific subterms. This is particularly useful in situations where participants think that they understand each other, but in fact are using the same terms to mean quite different things.

It appears that misunderstandings of this sort are most likely to occur at the level of ‘taken for granted’ (TFG) knowledge (Grice, 1975). It is a norm of communication that one does not explicitly mention something which can be safely taken for granted as being known to the other participant in the dialogue; however, people can be mistaken about what can be safely taken for granted. An easy mistake when eliciting explanations is to stop when it appears that there is no real need for further explanation because it can safely be taken for granted that both elicitor and respondent mean the same thing. This, however, is clearly not always the case, and laddering provides a convenient method for tackling such clarification.

## DISCUSSION

The role of culture in organizational change, particularly with regard to innovation in the workplace, has been the focus of research for over half a century. The topic is still the subject of heated debate, and even the definition of ‘culture’ remains controversial.

In this context, laddering is a technique which offers some interesting possibilities to the system developer. The case studies above demonstrate how laddering can be used in a variety of ways to help a system developer gain a clearer understanding of the situation under investigation. The first case study demonstrates, among other things, how the recursive format of laddering can help respondents to identify implications from items which they already knew, but whose implications they had never previously considered in detail. The second case study demonstrates how an investigator can check whether two different cultures within a workplace are reflected in different beliefs and norms about work-related issues. The third case study demonstrates how subjective or technical terms used by a respondent can be systematically clarified (complementing the investigation of personal goals and values, as described above).

Although in principle these things could also be accomplished via interviews, in practice the systematic nature of laddering, together with its formal knowledge representation and its grounding in a well-established literature, is a significant asset for tasks of this kind.

Understanding culture, though a laudable aim, is not by itself enough; there is a need for a rigorous and formalized method to translate this understanding into system design specifications. This topic is outside the scope of this paper. However, the way in which laddering has been automated as an integral part of integrated knowledge acquisition systems for developing knowledge based systems suggests that some similar approach could in the future be used for the development of information systems, in which case laddering could become not just a widely used technique, but a technique of choice.

## CONCLUSION AND FURTHER WORK

The examples above show how laddering can elicit a range of types of information important in understanding culture. The technique is simple, systematic and flexible, and can be integrated conveniently with other techniques. However, laddering alone is not the whole solution to the problem of eliciting information about culture. There are considerable advantages in using several techniques to complement each other, especially when one technique uncovers evidence of processes best investigated using another technique.

There is a need for further empirical studies to clarify the scope and role of laddering, and its use in conjunction with other techniques, both within and between cultures. In addition, there is a more general need for a greater emphasis on elicitation methodology as a factor in understanding culture. This is a topic which is receiving increasing attention in fields such as requirements engineering, so the study of culture may well be about to undergo interesting changes, with all which that entails.

## REFERENCES

Baddeley, A.D. (1990) Human Memory: Theory and Practice. Lawrence Erlbaum Associates, Hove.

Bannister, D. & Fransella, F. (1980) Inquiring Man. Penguin, Harmondsworth.

Bargh, J.A. (1997) The automaticity of everyday life. In: The Automaticity of Everyday Life Advances in Social Cognition, Vol. 10, Wyer, R.S. (ed.), pp. 1–61. Eribaum, Mahwah, NJ.

Barr, A. & Feigenbaum, E. (1982) A Handbook of Artificial. Intelligence. Kaufman, Los. Altos, CA.

Bartlett, F.C. (1932) Remembering: a Study in Experimental Social Psychology. Cambridge University Press, Cambridge.

Bassi, H. (1998) Unpublished undergraduate Thesis, Investigating perceptions of IT products via card sorts, University College Northampton.

Blanchard, K. & O’Connor, M. (1997) Managing by Values. Berrett Koehler, San Francisco, CA.

Boose, J.H. & Bradshaw, J.M. (1988) Expertise transfer and complex problems: using AQUINAS as a knowledge-acquisition workbench for knowledge based systems In. Knowledge-Based Systems, Vol. 2: Knowledge Acquisition Tools for Expert Systems Boose, J. & Gaines, B.R. (eds). Academic Press, New York.

Brown, A. (1998) Organisational Culture, 2nd edn. Pitman, London.

Checkland, P. (1981) Systems Thinking, Systems Practice John Wiley & Sons, Chichester.

Corbridge, C., Rugg, G., Major, N.P., Shadbolt, N.R. & Burton, A.M. (1994) Laddering: technique and tool use in Knowledge acquisition. Knowledge Acquisition, 6, 315–341.

Cullen, J. & Bryman, A. (1988) The Knowledge-acquisition bottleneck: time for reassessment. Expert Systems, 5, 216–225.

De Sanctis, G. & Poole, M.C. (1994) Capturing the complexity in advanced technology use: Adaptive Structuration Theory. Organization Science, 5 (2), 121– 128.

Eysenck, M.W. & Keane, M.T. (1995) Cognitive Psychology. Psychology Press, Hove.

Gigerenzer, G. (1994) Why the distinction between single event probabilities and frequencies is important for psychology (and vice versa). In: Subjective Probability, Wright, D. & Ayton, P. (eds). John Wiley and Sons, Chichester.

Goffmann, E. (1959) The Presentation of Self in Everyday Life. Doubleday, New York.

Greenwald, A.G. & Bannaji, M.R. (1995) Implicit social cognition: attitudes, self-esteem and stereotypes. Psychological Review, 102, 4–27.

Grice, H.P. (1975) Logic and Conversation. In. Syntax and Semantics 3, Cole, P. & Morgan, J.L. (eds). Academic Press, New York.

Hinkle, D. (1965) The change of personal constructs from the viewpoint of a theory of construct implications. Unpublished PhD Thesis, Ohio State University. Cited in: Inquiring Man, Bannister, D. & Fransella, F. (1980). Penguin, Harmondsworth.

Honikman, B. (1977) Construct theory as an approach to architectural and environmental design. In: The Measurement of Interpersonal Space by Grid Technique: Vol. 2: Dimensions of Interpersonal Space, Slater, P. (ed.). John Wiley and Sons, London.

Kahneman, D. Slovic, P. & Tversky, A. (eds) (1982) Judgement under Uncertainty: Heuristics and Biases. Cambridge University Press, Cambridge.

Kelly, G.A. (1955) The Psychology of Personal Constructs, Vols 1 and 2. Norton, New York.

Liu, J. & Sharp, B. (1997) A semiotic and knowledge-based approach to managing information resource. In. Legacy to Client–Server – Have You Chosen Wisely?, Booth, A. (ed.) UNICOM Press, Uxbridge, Middlesex.

Loftus, E.F. & Palmer, J.C. (1974) Reconstruction of automobile destruction: An example of the interaction between language and memory. Journal of Verbal Learning and Verbal Behaviour, 13, 585–589.

Lundberg, M., Goldkuhl, G. & Nilsson, A. (1982) Information Systems Development – a Systematic Approach. Prentice Hall, Englewood Cliffs, NJ.

McGeorge, P., Crawford, J. & Kelly, S. (1997) The relationship between psychometric intelligence and learning in an explicit and an implicit task. Journal of Experimental Psychology: Learning, Memory and Cognition, 23, 239–245.

Maiden, N.A.M. & Rugg, G. (1996) ACRE: a framework for acquisition of requirements. Software Engineering Journal, 183–192.

Major, N. & Reichgelt, H. (1990) ALTO: an automated laddering tool. In: Current Trends in Knowledge Acquisition, Wielinga, B., Boose, J., Gaines, B., Schreiber, G & van Someren, M. (eds). IOS Press, Amsterdam.

Miller, G.A. (1956) The magical number seven, plus or minus two: some limits on our capacity for processing information. Psychological Review, 63, 81– 93.

Mumford, E. (1995) Effective Requirements Analysis. Macmillan, London.

Neves, D.M. & Anderson, J.R. (1981) Knowledge compilation. mechanisms for the automatization of cognitive skills. In: Cognitive Skills and Their Acquisition, Anderson, J.R. (ed.). Erlbaum, Hillsdale, NJ.

Quinn, R.E. & McGrath, M.R. (1985) The transformation of organizational cultures: a competing values perspective. In. Organizational Culture, Frost, P. J. , Moore, L. F., Louis, M. R, Lundberg, C. C. & Martin, J. (eds). Sage, Newbury Park, CA.

Reynolds, T.J. & Gutman, J. (1988) Laddering theory, method, analysis, and interpretation. Journal of Advertising Research, February–March, 11–31.

Rugg, G. & Hooper, S. (1999) Knowing the unknowable: the causes and nature of changing requirements. Proceedings of the EMRPS¢99 Workshop, Venice, 25–26 November, 1999. IASI-CNR, Venice.

Rugg, G. & McGeorge, P. (1995) Laddering. Expert Systems, 12, 339–346.

Seger, C.A. (1994) Implicit learning. Psychological Bulletin, 115, 163–196.

Stamper, R. (1985) Analysing the Cultural Impact of a System. Working Paper. School of Information Systems, London School of Economics, London.

Trist, E.A. & Bamforth, K.W. (1990) Some social and psychological consequences of the longwall method of coal-getting. In Organization Theory. Selected Readings, 3rd edn, Pugh, D.S. (ed.). Penguin, Harmondsworth.

Wuebben, P.L., Straits & Schulman, G.I. (1974) The Experiment as a Social Occasion Glendessary press, Berkeley, CA.

## Biographies

Dr Gordon Rugg is a Senior Lecturer in the Department of Computer Science, Keele University, and a Visiting

Senior Research Fellow in the Department of Computer Science, the Open University. His PhD in Psychology at the University of Reading was followed by post-doctoral research in the Department of Psychology at Nottingham University, in the School of Information Science at City University and in the Centre for HCI Design at City University. He subsequently worked as a Senior Lecturer in the School of Computing Science, Middlesex University, and then as Reader in Technology Acceptance at University College Northampton, before taking up his present post. He is editor of Expert Systems: the International Journal of Knowledge Engineering and Neural Networks.

Malcolm Eva is a freelance consultant. He was previously a senior lecturer in the School of Information Systems, University College Northampton. He is an examiner for the SSADM Examination Board, in SSADM and in Business Systems development. His research interests include development methodologies and requirements acquisition. He has previously worked in industry and in consultancy.

Stephanie Andrews has a BA in Business Information Systems from University College Northampton. She works for British Power.

Sarah Davies has a BA in Business Information Systems from University College Northampton. She works for USC Europe at Abercanaid, Wales.

Atiya Mahmood has a BSc. in Sociology and Cultural Studies from Salford University, and an MSc in Office Systems and Data Communications from University College Northampton. She works for Getronics as an IT analyst.

Nazia Rehman has a BSc in Sociology and Cultural Studies from Salford University and an MSc in Office Systems and Data Communications from University College Northampton. She works for Getronics.
