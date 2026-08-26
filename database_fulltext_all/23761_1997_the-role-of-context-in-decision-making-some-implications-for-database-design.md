---
otero_id: 23761
otero_key: "SVZVPSYC"
title: "The role of context in decision making: some implications for database design"
authors: "D J Grimshaw; P L Mott; S A Roberts"
year: "1997"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000261"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The role of context in decision making: some implications for database design

DJ Grimshaw, PL Mott and SA Roberts

School of Computer Studies, University of Leeds, Leeds LS2 9JT, UK

With increasing integration of computer systems through local and wide area communication networks, there exists the capability in many organizations to retrieve information from databases to support ad hoc decision making by many different users. The idea that information is a corporate resource is now something more than business school hype. But the implications of sharing data are only just dawning on the corporate mind. How do managers interpret data? Where decision making is carried out by several people, perhaps in several different locations for different purposes the same data is used in multiple decision contexts. This paper explores the role of context as a way of adding value to information from databases. Two types of context are defined and discussed in relation to some examples of decisions where the role of context is vital. These examples are taken from some empirical research conducted with users of spatial decision support systems. Here the use of background information on maps, for example roads, add context to maps which otherwise simply display statistical data. The paper concludes by suggesting a model of context based on the notion that context acts as a filter between user and database.

## Introduction

At the heart of recent debates in the literature about the nature of the information systems domain lies the discussion about the characteristics of information itself. If the understanding of information is the key characteristic of the discipline then more work is certainly needed to take us beyond the comment made by Metcalfe and Powell (1995) that understanding the nature of information is not trivial.

In this paper we focus on the concept of context as a key to transforming data into information. Taking Wilson’s (1984) definition of information as data plus context we conclude that meaning is conferred in a particular context. The first part of the paper discusses context in relation to meaning, highlighting problems where failures in communication, or ‘breakdowns’ occur. The notion of a ‘context space’ is introduced as a way of illustrating variations in context. Before discussing context in relation to database design, two types of context are defined. Each context type (‘meta-data context’ and ‘extension context’) are then discussed in relation to some practical examples. In the final section of the paper a model architecture for these two types of contexts is outlined. The model is based on the notion of context as a filter and assumes the case of users within several contexts accessing a single database. The paper concludes with a discussion of the limitations of the model and directions for future work.

## Context and meaning

It is a normal and common observation that when two people communicate there will be interactive and rapid adjustment of meaning to take account of visual clues (sometimes referred to as body language) and other contextual clues, for example business conversation or personal, culture, etc. Linguists often use the term ‘marked’ to denote the way language changes meaning by adding something, for example the use of le and la in French to denote gender. Sociolinguists have used the ‘marked’ concept to help explain, for example, the ways in which women in the workplace are often ‘marked’ out from men by virtue of the clothes, conversational styles and attitudes (Tannen, 1995). Such observations are meant to be neutral, with no implied judgement about what is good or better.

Recent linguistic and more broadly philosophical research has suggested strongly that the interpretation of utterances depends not on isolated sentences but on the context, or holistic texts (Barwise & Perry 1983; Wiebe et al, 1996). Refinement of meaning takes place in conversations between people as the content and context is gradually revealed and understood. This process of adjustment and change is usually invisible to the participants because it works so smoothly. But failures do happen and are then experienced sharply as a ‘breakdown’ in communication and mutual understanding (Winograd & Flores, 1987).

In the case of human interaction with computer information systems, especially ad hoc access to database and information retrieval systems, the interaction is comparatively limited and stylised – often to: define query, submit, retrieve data. It should be noted, however, that some apparently limited communications media, such as email, have altered the ways in which people communicate (Lee, 1994). All the same there is no iterative element presently in our communication with machines, no space for the subtle adjustments of human communication. What follows is limited to a much simplified model of the interplay of meaning and context. We shall think of a user accessing a database where the user is located in a context that may well be different from the context of the database’s designers. We wish to mediate the interaction of the user with the database in such a way as to accommodate this difference in context.

## Shared meanings and shared contexts

Data becomes information to a user when that user interprets or gives meaning to the data (Wilson, 1984). This seems incontrovertible. The task of ensuring that an end user interprets data in precisely the correct way is probably an impossible one since ultimately database semantics can only be described through natural language and, as was noted in the previous section, the meaning of that is negotiated within a context, not static and given.

Some progress can be made, however, by recognising that users who share a context are more likely to interpret data in sufficiently similar ways to be useful than those from widely divergent contexts. Madnick (1995) distinguished three central ways that context may vary: culture, function, and organization. (An example of functional divergence might be the different interpretations put on capital data by an economist and an accountant). In Figure 1 we have illustrated three users accessing a database. A and B share all but their organizational context while C diverges on all three. We should expect C to be more likely to interpret the data differently from A and B.

![](/api/attachments/SVZVPSYC/fulltext/images/c75acf95bc578cf627f5e26e15603d125dea8b9e28d6197be858cb09a7a13c30.jpg)  
Figure 1 A context space.

On a recent visiting assignment at Universiti Utara Malaysia a lecture on information systems planning had to be changed so that it made sense in the context of the Malaysian economy, dominated by small business. Most of the concepts and ideas had come from observations made in large multi-national business units in western economies. For the Malaysian students to understand the ideas, it was important to relate them to their familiar context. Here a divergence of cultural context between lecturer and audience forced a change in the material presented.

Cultural context, any context for that matter, is nonlinguistic. It is a surrounding environment, not a set of sentences. But the lecturer changed not the context (which of course he could not change) but rather the linguistic formulations of his talk. What guided his changes? Two principles: that the new talk should mean the same to him as the old (more or less); and that the Malaysian students should understand it. This, we suggest, is just the additional requirement that it should mean to them what it meant to him. Divergent contexts created divergent interpretations. Transformation of the data occurred so that all understood it in the same way.

Suppose user B was in Malaysia and user A was in the UK. In technology terms it would be trivial to share a database to allow users A and B to have access. Even if both A and B were economists (same functional context) working for the same multinational company (same organizational context) there would still be the cultural contextual differences between them which, as the previous example showed, is capable of leading to extensive misunderstanding. As organizations increasingly distribute their activities across many countries the potential for errors arising from divergent contexts becomes greater. In the past those accessing an organization’s database could be assumed to share a context, and hence there was no need to represent it. This is increasingly not the case today. Data needs to be transformed to accommodate various user contexts. The standard of the transformation is that it means the same to all its users (Mott, 1995).

We summarise the discussion so far. A single data item within a database may be available to many users; each user may require data from a number of databases. Each user invests the data with meaning thus transforming it into information. Because of their different contexts this information will (or may) be different for each of them. Our aim is to transform the data item requested by the given users in such a way that each derives the same information from the version that they receive or, equivalently, so that it means the same to each user. In order to do this we need to know, not just the context within which each user is making decisions, but also the context within which the database was designed to be used. These two contexts are recognised in the work by Sciore and Segel (1994) who use the term ‘context-mediation’ to denote the ability to convert values from one context to another. The same term is used by Wiederhold (1994) to discuss the problem of interoperability between knowledge domains. Through context mediation data that is delivered to a user will be changed to ensure equivalence of information delivered to all users.

A context is an object in that it has both data and methods. A context, for example, might hold the data that its CURRENCY = yen while supporting methods that allowed the translation of data items from contexts where CURRENCY = USdollar. The application of the methods of the context C to the transformation of a dataitem, we shall refer to as the ‘action of C’.

We distinguish two types of context depending on the changes of ‘action of $\dot { \mathrm { C } } ^ { \ j }$ may make. Where the ‘action of $C ^ { \bar { \bf { \Lambda } } }$ will amplify or extend the data returned to a user, we speak of ‘extension contexts’. Alternatively the ‘action of $\mathbf { C } '$ may simply transform the data to take account of the context (the CURRENCY example above). We adopt the term ‘meta-data context’ for contexts having this latter type of action, recognising that a context will likely exploit information from the system catalogues. Data held there is often called meta-data. The concept of ‘meta-data context’ is roughly equivalent to ‘context’ as defined by Sciore and Segel (1994).

The next section discusses examples of these two types of context in relation to the implications for database design. The discussion is limited to databases in order to help us focus on some tentative solutions.

## The role of context in database design

A database could return all data in the fullest available detail to every query. But that would simply swamp the users. The action of a context should act as a filter that selects data appropriately. Thereby making a contribution to the solution of the ‘information overload’ problem. How might this be achieved?

Previous work by Roberts and Gahegan (1991) considered the notion of context in database design by focusing on the significance of data. Their context is an example of an ‘extension context’ with rules designed to filter data such that only significant, summary information is presented. Although their system has room for different user views, it does not support the concept of ‘context mediation’.

The question we are interested in is the structure of databases in which some of those who access the data held there will not share the context of the first-users. For these users the database has been designed without knowledge of their own context, for them it is a ‘foreign database’. Sciore and Segel (1994) take a similar approach, but have a more limited view of context than presented in this paper (they do not deal with ‘extension contexts’). More significantly, their approach leads to user contexts being described within a query language, thus restricting usage to specially-designed databases.

## An example of ‘extension context’

As part of a wider research project into the use of spatial decision support systems it was decided to seek the cooperation of ten organizations – five in financial services and five in retail. One of the financial services organizations declined to cooperate with the study and one of the retail organizations did not respond to requests for interviews. So the data and analysis presented here are based on interviews carried out in four financial services and four retail organizations during October to December, 1995. The interviewer adopted a phenomenological approach to the research.

Users of Spatial Decision Support Systems (SDSS) were interviewed, using a semi-structured questionnaire. In most of the case organizations the interviews were conducted with more than one person. A range of questions were asked relating to the use of SDSS (Grimshaw & Clarke, 1996). The question of context arose from answers to a question about the role of data representation: “what improvements to the display would you like to see?” The displays in question were maps that are output as the result of running scenarios typical of location planning issues, for example, “What if we open a new branch located at X?” Responses to this indicate that five out of eight case study organizations expressed a need for additional contextual data. Typical responses were, some of the maps would be easier to interpret if there was an overlay of features such as roads, rivers, railways, etc. In terms of our previously defined types of context, this is an example of ‘extension context’.

## Some examples of ‘meta-data context’

As a first step we propose some generic contexts within, but not restricted to, geographical information systems (GIS). Our assumption is that the database is a ‘foreign database’ to the user.

## Data units

The user may be assuming in his query a certain unit of measurement while the data may be stored using another. The action of the context should perform the required transformations (Kowalski, 1995).

## Data timeliness

Timeliness is closely related to accuracy. The timeliness information that the user needs might take several forms. It might be sufficient to know that the information is the most up-to-date available. It might be that the user needs to know that each of the data represent a real-world state that was ‘true’ at some point within (say) the last 24 hours. Or it might be that it is important that all states represented by the data were true at the same point in time (the precision of the point needs to be specified) within some specified interval.

## Data accuracy

Where numerical data is retrieved from a database there will almost always be an implied associated ‘accuracy’. The user may need to know the implied accuracy of data in order to judge whether the information based on that data is suitable for his/her purposes.

Spatial information provides a particularly interesting example. Digital map information is still sold with an associated ‘map-scale’. Unlike paper maps, this information does not tell the end user what size the image will be on screen or print-out since the software can set the scale to whatever is appropriate for the task. Rather, the ‘scale’ refers to the scale of the map that has been digitised, and as such gives information (in a rather indirect way) about how accurate the positional information is likely to be. It would also indicate to what extent the underlying reality has been generalised, for example whether individual buildings, or only the more important, will be represented. So map scale gives an indication of what information is likely to be missing (due to generalisation) as well as accuracy.

That timeliness is related to accuracy should be clear. For example, a large-scale map will change in order to represent the changing underlying reality more rapidly than a small-scale map.

## Data source

It might be argued that information about the data source is an alternative to the above meta-data, rather than an additional requirement. Just as the scale of a map embodies a number of messages regarding data quality, so too the source of the data may give implicit information about the accuracy (from knowledge of measuring instruments used for example), timeliness (from knowledge of frequency of measurement), completeness (from knowledge of procedures) etc.

A good example of the need for information on data source comes again from spatial data management. A description of a part of the earth’s surface will be useful for different applications depending on whether the underlying data was derived from a digitised map, or from remote sensing or aerial photography.

## Data consistency

If data is retrieved from several tables as a result of a single query there is clearly a need to ensure that these tables are consistent along the dimensions described above. If the database was consolidated from several earlier databases so that one table holds map information at a scale of 1 inch to the mile and another at a 6-inch scale then combining the information is going to be problematic. The user needs to be told of the discrepancies.

## Data completeness

Suppose table A contains a table of ‘Ground deposition readings’ taken every year and table B contains readings – for different regions, assume – taken quarterly (once more this may have arisen from consolidating several pre-existing databases). The latter readings are more complete than the former, and the question is how they might be reconciled. Alternatively database A might simply lack a field that database B provides but the information might be better returned partially than not at all. Null values in some form or another would then have to appear in the result. Since null values may mean different things there is a serious issue of how they are to be compounded from several sources.

## A model of context

In the case of federated databases (for example) the end user may not have had any influence in the design of some of the component databases which will be foreign databases for him. The issues of schema integration and semantic conflict resolution that arise here have been studied (Naiman & Ouksel, 1995) to integrate data from disparate sources. This work concentrates on assisting the schematic mapping between two databases but is not specifically concerned with issues of scale, timeliness or precision of the underlying datasets. Also it assumes that once conflicts have been resolved, the end user will interpret the information obtained from the integrated database in an appropriate manner. So their concerns are rather different from ours.

## An architecture for contexts

We assume a relational database supporting a standard language such as SQL. We describe an architecture for adding a context layer to such a system. Our approach is to define contexts through a class hierarchy. A context will be an instance of a class within such a hierarchy. Various contexts can be created by specialising existing context classes. A query to the database will always be made through a context which operationally means that it is pre-processed by the action of the context before being submitted to the database. As we shall see it is necessary for the response from the database also to undergo translation. Figure 2 shows the simplest version of this architecture where user A submits query Q to DB through context $\mathrm { C } _ { \mathrm { A } } .$ The action of the context changes both the query and the response received from the database.

It is necessary to translate both the query and the response. We will use perhaps the simplest contextual element, that of different units. Suppose that User A submits the following query to a database:

<table><tr><td>Name</td><td>AvgTemp</td></tr><tr><td>Sussex</td><td>7.5</td></tr><tr><td>Somerset</td><td>7.4</td></tr><tr><td>Dorset</td><td>7.2</td></tr></table>

![](/api/attachments/SVZVPSYC/fulltext/images/9b4d5668ba035d8489a37fc63b3599fa1a6bec2ac65179e86e59c71282abde59.jpg)  
Figure 2 Simple architecture for context.

Select (Regions.name) from Regions where Region.AvgTemp . 45

and let us suppose that the user assumes degrees F but the database stores degrees C. Unprocessed the database will return an empty list which will shock user A not a little (here is a typical ‘breakdown’). To correct it we may pass the query through context A which converts to centigrade before submitting to the database, This would result in the correct information being returned say:

Name Sussex Somerset Dorset

Suppose, however, that the modified query was submitted:

Select (Regions.name, Regions.AvgTemp) from Regions where Region.AvgTemp . 45

then under present assumptions this table would be returned:

which would again create a breakdown. So the action of the context must transform both the query into the database and its result. The latter is a requirement to ‘rewrite’ tables which are not usually conceived of as linguistic objects at all. It suggests that the action of a context must be a symbolic level more general than relational languages.

The result of a query may be made available to many different users. Figure 3 shows a query Q submitted by A whose result is distributed to B and X as well. Of course R′, $\mathrm { R } _ { \mathrm { B } }$ and $\mathtt { R } _ { \mathrm { X } }$ may well be different tables. No matter, our criterion of correctness is that $\mathrm { R _ { A } }$ means to A in context $\mathrm { C _ { A } }$ and $\mathrm { R } _ { \mathrm { B } }$ means to B in context $\mathrm { C _ { B } }$ and likewise for X. They are thus all being told the same thing – at least insofar as this requirement can in principle be met.

The objection might be made at this point that all that we have described, at least in the examples, could be achieved through definition of relational views. However, the problem with an approach based on views is that, either a database must anticipate all possible decision-making contexts required by users and provide a set of views for each, or else the end user must be aware of the context within which each database has been designed to be used, and must construct the views for himself/herself. The first option may be impracticable, given that we are interested in access to foreign databases, whereas the second option represents no step forward since it requires the end user to have complete knowledge of each database accessed.

Finally the model so far assumes that there is only a single context that a query passes through. Reference to Figure 1 will suggest that this is an unduly simple model. In fact users might share some of the contexts that their queries passed through. In Figure 4 below User A passes queries through two contexts, users B and X through one each.

## Mechanisms of access

We consider how the action of a context might process queries and retrieve data with reference to the issues in the previous section. Our object is to suggest how the proposed architecture provides a framework for managing issues of context, not a detailed specification. This process is conceived after the manner of translation rules that look for patterns in the incoming query.

## Data units

A rule may be imposed upon an attribute of a table in the database. Adopting a style reminiscent of the Postgres rule system (Stonebraker et al, 1991) we might have a rule:

$$
\begin{array}{l l} \text {op } & \text {"Regions.AvgTemp"} \\ \text {op } & \text {} \\ \text {d} & \text {} \\ \text {FtoC} (\mathbb {S}) \end{array}
$$

This rule would be fired on any incoming query that included an expression such as Region.AvgTemp . 45 and the effect would be to replace the literal value given by the result of applying the conversion function. We have used ‘op’ to indicate any relational symbol and ‘\$’ to indicate any expression. On export we require a format that permits the action of the context to detect that Regions.AveTemp is being returned as an attribute in a table. Some formulation such as:

$$
\begin{array}{r l} & \text {   =   } \\ & \text {   =   } \end{array}
$$

“Regions.AvgTemp

$$
\mathbb {S} \text {   ♦   } \mathrm{CtoF} (\mathbb {S})
$$

We acknowledge here that there is no obvious sense in which the expression Regions.AvgTemp occur in an output table. It is for this reason that a more powerful formalism is required to represent both input and output formats. Note though that the linguistic point of view persists. We need to construe the database as exporting linguistic constructs for which a notion of translation makes sense.

![](/api/attachments/SVZVPSYC/fulltext/images/01dcf7aba68116b4fd01124cf761539e54b39c8a3d6805955ca8331c0c5ffc8e.jpg)  
Figure 3 Multiple users and single context.

![](/api/attachments/SVZVPSYC/fulltext/images/7aae3db593f78a4b1d1f2bec34426092d5d2321137900d95dea3b95a9c4adc35.jpg)  
Figure 4 Multiple users and multiple contexts.

## Data timeliness

Discrepancies of data units substitute new values for old in a fairly straightforward way in manner that ‘le chien’ translates ‘the dog’. In the case of timeliness of data let us assume the user’s context maintains a timeliness condition on a relation independently of a user’s query mentioning such in his query. This condition (we assume) is that the information returned from relation Population must be no older than 01-1-90. Then a rule might be placed upon the Population relation that adds this condition to an incoming query:

## on import exprsion “select \$1 from \$2 Population where \$3” do replac \$3 by “\$3 and Population.date . ‘01-1-90’”

In this case no export rule is needed.

Issues of data consistency and completeness are potentially much more extensive than those considered so far, for they arise most naturally when there are several data-sources being accessed from a single context. Consistency then requires that the data held in those sources be commensurable, completeness (perhaps misleadingly called) requires that we accommodate the differences in the data held at different sites.

The example of the two maps at different scales is not so easily handled. It would be necessary for the designer of the contexts to decide how such information was to be reconciled. In our architecture this decision takes the form of translating queries that match an input pattern.

The above description assumes that the appropriate translation rules can be readily identified on receipt of a user’s query. This raises the question of how a user can make known her context to the database system. We believe what is needed is a language for describing contexts which can be used both by the end user, and also to describe the context within which the assumptions were made at the time of the database design. The user would be required to submit a context description along with each query (or a context could be defined for a query session). In answering a query within a given context the database system would have to compare the user context with the database context and invoke re-write rules if appropriate, or possibly refuse to answer the query if the contexts couldn’t be matched.

The language would need to be capable of describing meta-data and extension contexts. All database contexts would be meta-data contexts, whereas the user context could be a meta-data or extension context or include elements of both types.

Finally let us return briefly to the perceived requirement for more background information reported in Grimshaw and Clarke (1996). We have here to think of a context retrieving (say) data about a road network from one database, enriching this with other contextual data (say a railway network) and returning the combination of these into a single representation for the user. If we assume that the contextual information is itself held in another table, then this is a problem of combining information from two tables. Our translational approach requires that the information that is displayed graphically may nonetheless be viewed as a linguistic structure that allows such combination. This is further evidence, if any is needed, that a ‘contextual database’ requires an underlying formalism that is able to represent a wide range of informational objects in a uniform manner for the purposes of data-manipulation.

## Conclusion

This paper has brought together ideas from the information systems, philosophy and database literature in order to explore, clarify, and suggest a way forward which would allow the notion of context to be part of the design of the database. The classification of context into ‘meta-data context’ and ‘extension context’ has shown two ways in which context has to be taken account of in database design. We have emphasised a process whereby queries to a database are passed through contexts as a filter to access the database and given a criterion of correctness for comparing the output to various users. Finally we have claimed that contexts need to represent heterogeneous data in a single form. Future work will look for a formal representation for context and we are considering situation theory (Barwise & Perry, 1983; Devlin, 1991), an approach to information which acknowledges the centrality of context and furthermore realises that information comes in many forms, as a vehicle for doing so.

The emphasis throughout has been on the implications of context for database design. Yet it should be stated clearly that not all information systems are databases. While context is significant for all information systems, the treatment given here is limited to database considerations. Beyond the scope of the paper are considerations of the role of context in computer supported co-operative work environments, group decision support systems, and more informal information retrieval systems.

## References

<sup>Barwise</sup> <sup>J</sup> and <sup>Perry</sup> <sup>M</sup> (1983) Situations and Attitudes. MIT Press, Cambridge, Massachusetts.

<sup>Devlin</sup> <sup>K</sup> (1991) Logic and Information. Cambridge University Press, Cambridge.

<sup>Grimshaw</sup> <sup>DJ</sup> and <sup>Clarke</sup> <sup>M</sup> (1996) The use of spatial models to support decision making: an empirical investigation of financial services and retail sectors. Journal of Targeting, Measurement and Analysis for Marketing 4(4), 314–325.

<sup>Kowalski</sup> <sup>VJ</sup> (1995) The POSC solution to managing E&P Data. In Modern Database Systems, (<sup>Won</sup> <sup>Kim</sup>, Ed), pp 281–302, ACM Press.

<sup>Lee AS</sup> (1994) Electronic mail as a medium for rich communication: An empirical investigation using hermeneutic interpretation. MIS Quarterly 18(2), 143–157.

<sup>Madnick</sup> <sup>SE</sup> (1995) Integrating information from global systems: dealing with the ‘on-and-off ramps’ of the information superhighway. Journal of Organizational Computing 5(2), 69–82.

<sup>Metcalfe</sup> <sup>M</sup> and <sup>Powell</sup> <sup>P</sup> (1995) Information: a perceiver-concerns perspective. European Journal of Information Systems 4(3), 121– 129.

<sup>Mott</sup> <sup>PL</sup> (1995) Towards a Winograd-Flores Semantics. Minds and Machines 5, 69–87.

<sup>Naiman</sup> <sup>CF</sup> and <sup>Ouksel</sup> <sup>AM</sup> (1995) A classification of semantic con

flicts in heterogenous database systems. Journal of Organizational Computing 5(2), 167–193.

<sup>Roberts SA</sup> and <sup>Gahegan MN</sup> (1991) Supporting the notion of context within a database environment for intelligent reporting and query optimisation. European Journal of Information Systems 1(1), 13–22.

<sup>Sciore E</sup> and <sup>Siegel M</sup> (1994) Using semantic values to facilitate interoperability among heterogeneous information systems. ACM Transactions on Database Systems 19(2), 254–290.

<sup>Stonebraker</sup> <sup>M</sup> and <sup>Kemnitz</sup> <sup>G</sup> (1991) The postgres next-generation database management system. Communications of the ACM 34(10), 78–92.

<sup>Tannen</sup> <sup>D</sup> (1995) Talking from 9 to 5, Virago Press, London.

<sup>Wiebe</sup> <sup>J,</sup> <sup>Hirst</sup> <sup>G</sup> and <sup>Horton</sup> <sup>D</sup> (1996) Language use in context. Communications of the ACM 39(1), 102–111.

<sup>Wiederhold G</sup> (1994) Interoperation, mediation, and ontologies. In Proceedings of the International Symposium on Fifth Generation Computer Systems, Tokyo, Vol. W3, pp 33–48.

<sup>Wilson</sup> <sup>B</sup> (1984) Systems: Concepts, Methodologies and Applications. John Wiley & Sons, Chichester, Second Edition.

<sup>Winograd</sup> <sup>T</sup> and <sup>Flores</sup> <sup>F</sup> (1987) Understanding Computers and Cognition. Addison-Wesley, Reading, Mass.

## About the authors

David Grimshaw is Senior Lecturer in Information Systems at the University of Leeds. Previously at Warwick Business School, University of Warwick. Research interests include the use of geographical information by business and the impact of IT on organisations. He is author of Bringing GIS into Business, published by GeoInformation International.

Peter Mott is lecturer in Computer Studies at the University of Leeds. His current research interests are in databases, logic and formal semantics. He previously taught Philosophy at the University of Lancaster.

Stuart Roberts is Senior Lecturer in Databases at the University of Leeds. Principal research interests are in the area of intelligent databases. Recently work has centred on the management of spatial and temporal data. Work includes objectmodelling for spatial and spatio-temporal databases.
