---
otero_id: 21558
otero_key: "GHBDTEGV"
title: "Categorizing automated messages"
authors: "Scott A Moore"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00060-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Categorizing automated messages

Scott A. Moore \*

Computer and Information Systems Department, UniÕersity of Michigan Business School, 701 Tappan, Ann Arbor, MI 48109-1234, USA

## Abstract

The author discusses a field study that investigates the relationship between a linguistic theory called speech act theory Ž . SAT and automated electronic messages. The results reveal that standards for both electronic data interchange and inter-application communication messages have the structure predicted by SAT. This provides some evidence supporting computerized systems based on SAT. The benefits of such systems are that they would be easier to construct and support than existing systems. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Speech act theory; Electronic data interchange; Interorganizational communication; Automated message processing; Electronic commerce; Structured organizational communication

## 1. Introduction

Businesses use paper forms for standard information exchange. This exchange, when performed by computers, is called electronic data interchange Ž . EDI . Businesses use EDI for many inter-company messages: requesting a transportation schedule, providing one, confirming that containers have been picked up, reporting a bank’s assets and liabilities position, authorizing a commitment of resources, etc. With the wide availability of computers and reliable communication technologies, businesses are increasingly relying on EDI for timely information exchange. About 70,000 businesses worldwide use some form of EDI 38 . SWIFT Society for World-<sup>w</sup> <sup>x</sup> Ž wide Interbank Financial Telecommunications alone,. for example, switched about 2.8 million EDI messages per day during 1996.

As reported in a survey done in 1989 by Straub and Wetherbe, information systems executives believe that communications technology—with EDI being mentioned specifically—is a critical information technology 39 . These executives forecast that<sup>w</sup> <sup>x</sup> EDI will be one of the dominant technological forces that will affect organizational change in the 1990s. Unfortunately, EDI systems are difficult and expensive to develop, and are not as capable as they could be 31 . Reasons for these drawbacks become appar-<sup>w</sup> <sup>x</sup> ent by contrasting how EDI systems add new capabilities with how this is done in another system. Each EDI message is an instance of one of hundreds of possible message types. Each of these message types has a specific, rather limited, structure. To interpret the meaning of a particular message instance, the reader must be familiar with the idiosyncrasies of its message type. To say something new, a new message type must be created—someone or some committee must define fields, determine their order, determine if each is required or optional, determine how it should be interpreted and responded to, etc.

Contrast this with the English language, the foundation of a very capable communication system. It comprises a very stable grammar and a large and evolving vocabulary. This combination allows speakers to express new ideas by combining existing words in novel ways within the boundaries imposed by the grammar. Given appropriate knowledge of the vocabulary, a person can understand most sentences because the grammar is constant.

Since EDI is part of a communication system among computers and people, fields that study human communication might have much to say about how to develop a more capable EDI system with less difficulty and expense. How is a flexible language Ž . e.g., English structured? What kind of utterances can be made? Can utterances be classified in any useful way? Are there general skills or knowledge that can be learned? If so, what are they and how general are they? Speech act theory SAT , a theoryŽ . of communication discussed in Section 2, has much to say about these questions.

EDI developed with little regard for linguistics or SAT. The following research reveals the remarkable fact that the message structure implicit in the investigated electronic messaging systems is consistent with SAT. I believe this is not simply a remarkable coincidence, but indicates that SAT usefully describes the communication activities performed by EDI systems stronger claims could be made and areŽ discussed in Section 7. If this were so, then, possi-. bly, EDI systems could be designed to take advantage of what we know about SAT and human communication, thereby making these systems more capable and flexible.

Other papers have explored the added capabilities and increased flexibility of EDI systems based on SAT 16,29 . Here I will summarize specific ways in<sup>w</sup> <sup>x</sup> which SAT would affect EDI. The most obvious application would be in the design of EDI message sets. A message set is, roughly, the electronic counterpart of a paper form. A message set definition describes how it is to be used, the fields it needs Ž . think of blanks on the form , the values that are allowed in these fields, the definitions of those values, the order in which the fields can be listed, and the meaning of the message when it has certain values in certain fields. Applying SAT to EDI message sets results in a message set in which the message’s purpose—that is, whether it requests or predicts or informs—would be explicitly represented. Currently, much detailed knowledge is needed in order to determine what a message is doing. One message set can have multiple purposes e.g., bothŽ predict and inform or can have one of many pur- . poses e.g., either predict or inform . A particular Ž . message’s purpose is determined by its contents. An alternative would be that each message set has just one purpose e.g., always a prediction whose con-Ž . tents merely determine the specifics e.g., the subjectŽ of the prediction . Current practice makes it more. difficult to write programs to interpret these messages, react to them, and retrieve information contained in them.

Second, all message sets in a SAT-based EDI system would have a common format in which the message’s purpose called the Ž illocutionary force by speech act theorists is separated from its content . Že.g., whether it is about a purchase order, or a shipment of goods, etc. . SAT holds that. all utterances have a common structure. Currently, each EDI message has a format distinct from all others.

Third, each message set would always have a force chosen from a small set of known forces. Speech act theorists posit that there are a limited number of forces, and that these do not change with different subject areas. The forces of the examples in the first paragraph are shown in Table 1.

The possible effects of the above three proposals for firms engaging in electronic commerce are many. Developers would be able to re-use computer code among messages with the same illocutionary point, thus making addition of new messages to an EDI system less troublesome. Companies would find it easier to build both search engines that could find information hidden in huge message repositories and message management systems that could help manage the flow of information between and within organizations. Companies would be able to send new kinds of messages without going through the bureaucratic maze of defining a new message set. This would make it easier to say more things electronically and, thus, to forge deeper electronic links between organizations. These and other organizational and strategic implications are discussed in Section 7.

I conducted a field study discussed in Section 3Ž . of three standards described in Section 4 : two forŽ .

Table 1  
Sample phrases and their illocutionary forces

<table><tr><td>Phrase</td><td>Force</td></tr><tr><td>Requesting a transportation schedule</td><td>Requestive</td></tr><tr><td>Providing a transportation schedule</td><td>Predictive</td></tr><tr><td>Confirming that containers have been picked up</td><td>Confirmative</td></tr><tr><td>Reporting a bank’s assets and liabilities position</td><td>Descriptive</td></tr><tr><td>Authorizing a commitment of resources</td><td>Permissive</td></tr></table>

EDI and one for inter-application communication. The purpose was to determine the correspondence between the standards and SAT. SAT predicts that all utterances share the same high-level structure. Since a message from one of these standards helps two parties communicate, it can be considered an utterance. Thus, SAT asserts that these messages must have the predicted structure. I tested this prediction. The findings of this investigation supported that SAT-messages can be mapped to the structure predicted by SAT discussed in Sections 5 and 6 .Ž . Implications and future research are discussed in Section 7.

## 2. Review of speech act theory

Work on SAT began, roughly, with the publication of Austin’s How to Do Things with Words <sup>w</sup> <sup>x</sup> 4 , the text of his William James Lectures at Harvard University in 1955. These lectures specified two very important, though quite general, ideas. The first rebuts the then commonly accepted idea that language’s only function is to say things that are true or false. Austin felt this was not enough. He believed statements also accomplish something, that people are doing things with words.

Austin also proposed that every for our purposes Ž . utterance is the speaker’s expression of an attitude toward some possibly complex proposition. For example, if the speaker says ‘‘It will rain’’, then typically the speaker is predicting it will rain. The proposition is it will rain and the attitude is that of a prediction. If the speaker says Will it rain? then typically the speaker is asking whether it will rain. In this case, the proposition is the same—it will rain— and the attitude expressed is that of a question. Thus, speakers can express different attitudes toward the same proposition. Speech act theorists call these attitudes illocutionary forces. Summarizing this idea: every speech act i.e., utterance has the structure Ž . F PŽ ., where F, the illocutionary force, is applied to P, the propositional content. This is called the F P( ) framework.

This is a strong claim. Speech act theorists propose that the outermost operator of eÕery utterance Ž . everything we could possibly say is not Boolean, not temporal, not even defeasible—it is an illocutionary force. If this were true, then a communication system might benefit from representing the structure explicitly so that the system could reason about it more on this later .Ž .

Speech act theorists propose widely differing categorization schemes for these forces, each of which could be used as an organizing scheme for a message hierarchy. Different versions of SAT 6,32 are more<sup>w</sup> <sup>x</sup> or less suited to be such an organizing scheme because of the opportunities for inheritance. A less useful hierarchy would be one level deep with no inheritance. A more useful hierarchy would be deeper, allowing messages to inherit properties from other messages. A small number of illocutionary forces that are categorized into a relatively deep tree would be ideal for a communication system based on SAT.

I work with the version of SAT proposed by Bach and Harnish 5 . It is representative of other propos-<sup>w</sup> <sup>x</sup> als such as the one by Searle 34 and the one by<sup>w</sup> <sup>x</sup> Ballmer and Brennenstuhl 6 . The linguistic commu-<sup>w</sup> <sup>x</sup> nity has not settled on any one scheme and, for the purposes of this paper, there are not big differences among them. Also, they define a system of inferential communication that is a useful basis for electronic communication Kimbrough et al. 19 ; MooreŽ <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 27 . Roughly, under an inferential communication. theory, which is also supported by some cognitive scientists and philosophers Grice 11 , Nolan 30 ,Ž <sup>w x</sup> <sup>w x</sup> Sperber and Wilson 37 , the recipient must infer <sup>w</sup> <sup>x</sup>. what the speaker means and then take the message as a basis of inference for how to act. This is in contrast to Searle’s position that communication is a decoding system and that all the information needed to understand a message is contained in the message itself 32,33,35 . The effects of this choice are dis-<sup>w</sup> <sup>x</sup> cussed in Section 5.

Bach and Harnish propose two major categories of illocutionary forces and six main sub-categories with further subcategorization. The two major categories, communicatiÕe and conÕentional, designate how the hearer should process the utterance. ‘‘Communicative illocutionary acts succeed by means of recognition of intention, whereas conventional ones succeed by satisfying a convention’’ 5 p. 110 . For <sup>w</sup> <sup>x</sup> Ž . example, if a speaker performs a requestive, an example of a communicative illocutionary act, then this act succeeds if the hearer recognizes that the intent of the speaker was, in fact, to perform a requestive ‘recognition of intention’ . ConventionalŽ . forces can only succeed under much more restrictive circumstances i.e., ‘by satisfying a convention’ .Ž . For example, appointing a person to a position can only be done in a certain way by certain people at certain times. It is not simply by recognizing the intent of the speaker to appoint, but it is the satisfaction of the conventions of appointing that determines whether the act succeeds or not. As for the six main sub-categories:

[ ] C onstatiÕes express the speaker’s belief and his intention or desire that the hearer have or form a like belief. DirectiÕes express the speaker’s attitude toward some prospective action by the hearer and his intention that his utterance, or the attitude it expresses, be taken as a reason for the hearer’s action. CommissiÕes express the speaker’s intention and belief that his utterance obligates him to do something Ž . perhaps under certain conditions . And acknowledgments express feelings regarding the hearer or, in cases where the utterance is clearly perfunctory or formal, the speaker’s intention that his utterance satisfy a social expectation to express certain feelings and his belief that it does 5 , p. 41 .<sup>w</sup> <sup>x</sup> Ž .

‘‘EffectiÕes effect changes in institutional states of affairs . . . VerdictiÕes are judgments that by con-

## Communicative

Constatives assertives, predictives, retrodictives, descriptives. ascriptives, informatives, confirmatives, concessives, retractives, assentives, dissentives, disputatives, responsives, suggestives, suppositives

Directives requestives, questions, requirements, prohibitives, permissives, advisories

Commissives promises, offers

Acknowledgments apologize, condole, congratulate, greet, thank, bid, accept (acknowledge an acknowledgment), reject (reject an acknowledgment)

## Conventional

effectives appoint, nominate, suspend, demote, enlist, apply, resign, abdicate, arrest, indict

verdictive acquit, certify, disqualify, clear, rule adjudicate

Fig. 1. Classification of forces and verbs.

vention have official, binding import in the context of the institution in which they occur’’ 5 p. 110–<sup>w</sup> <sup>x</sup> Ž 111 ..

Fig. 1 lists the four categories of forces that are communicative illocutionary acts the two categories Ž of conventional illocutionary forces are discussed below . Table 2 provides informal definitions, Ap-. pendix A provides their formal definitions, while Table 3 provides examples of utterances that typically would have these forces. Bach and Harnish also include a constatiÕe of type ‘responsive’. This is meant to distinguish illocutionary acts in which the speaker is responding to an earlier inquiry by the hearer. That an utterance is considered to be a response is classifying the utterance based on discourse- or dialogue -related information. Other dis-Ž . course type information would indicate if the utterance is an interruption of a continuing conversation, an elaboration of a previous utterance, or a correction of a previous utterance. Many researchers e.g.,Ž Litman and Allen 23 , Cohen and Perrault 7 , Mc-<sup>w</sup> <sup>x</sup> <sup>w x</sup> Cafferty 24 , and Moore 28 have argued for com- <sup>w x</sup> <sup>w x</sup>. municative frameworks in which the discourse information is considered separately from that of illocutionary force. I agree with this position. Since inclusion of this force would confound the results of the study, I do not include ‘responsives’ in the list of possible illocutionary forces.

Table 2 Informal definitions of illocutionary forces

<table><tr><td>Force</td><td>Description</td></tr><tr><td>Acknowledgment</td><td>Perfunctorily express certain feelings</td></tr><tr><td>Advisory</td><td>Advise that the hearer should do something</td></tr><tr><td>Ascriptive</td><td>Claim that some result or situation is related to some other situation</td></tr><tr><td>Assentive</td><td>Agree to something claimed by the hearer</td></tr><tr><td>Assertive</td><td>Tell someone some fact</td></tr><tr><td>Concessive</td><td>Express something contrary to what was believed</td></tr><tr><td>Confirmative</td><td>Tell someone something he/she already knows</td></tr><tr><td>Descriptive</td><td>Describe something</td></tr><tr><td>Disputative</td><td>Claim there is reason to not believe something</td></tr><tr><td>Dissentive</td><td>Disagree with something claimed by the hearer</td></tr><tr><td>Effective</td><td>Saying it makes it so</td></tr><tr><td>Informative</td><td>Tell someone some fact that they probably don’t know</td></tr><tr><td>Offer</td><td>An offer to do something</td></tr><tr><td>Permissive</td><td>Tell someone they can perform some act</td></tr><tr><td>Predictive</td><td>Describe some event that has yet to occur</td></tr><tr><td>Prohibitive</td><td>Require that the hearer not do a certain thing</td></tr><tr><td>Promise</td><td>Commit yourself to something</td></tr><tr><td>Question</td><td>Ask a yes/no question</td></tr><tr><td>Requestive</td><td>Ask something</td></tr><tr><td>Requirement</td><td>Ask someone else to do something from a position of authority</td></tr><tr><td>Retractive</td><td>Claim that the speaker no longer believes some fact</td></tr><tr><td>Retrodictive</td><td>Describe some event that has occurred</td></tr><tr><td>Suggestive</td><td>Claim that there is some reason to believe some fact</td></tr><tr><td>Suppositive</td><td>Claim that it is worth considering the consequences of something</td></tr><tr><td>Verdictive</td><td>A judgment that has official, binding import</td></tr></table>

Conventional illocutionary acts can only be distinguished at the verb level. Examples of verbs with an effective or verdictive illocutionary force are in Fig. 1. An example of an utterance classified as an effec tive is ‘‘I nominate Seymour Evil as the next president’’. An example of a verdictive is ‘‘I certify that Eustus L. Emons is insane’’.

Speech act theorists contend that all utterances can be described within the F PŽ . framework. Bach and Harnish propose the thirty-plus illocutionary forces in the six categories listed above; others propose different numbers of forces in different categories. The exact categorization scheme used is not important for this paper. What is important is the contention that all utterances—verbal, electronic, or otherwise—have an illocutionary force. It is this contention that is investigated in this paper.

## 3. A field study

The best way to determine if all utterances can be understood within the F PŽ . framework is to translate all utterances into the framework. However, there are infinitely many utterances, so this is not possible.

It is also not clear that a random sampling of utterances is feasible. For example, what would the population be? What would a random sample look like?

A more feasible test is to translate some appropriate sample of utterances. Since I am concerned with electronic commerce and the realm of doing things electronically and automatically, appropriate samples are existing sets of utterances that reflect the diverse activities performed electronically. The scientist’s challenge is twofold. First, find a diverse set of utterances so the results can be regarded with some confidence. Second, choose an application domain close enough to electronic commerce so that the results are considered relevant. Satisfying these requirements should increase the external validity of this study 8 . I conducted this test by completing a <sup>w</sup> <sup>x</sup> kind of field study. First, I gathered some data—two EDI standards and an inter-application communication IAC standard. These were not random choices.Ž . They are existing, rich, diverse commercial standards developed independently of SAT. Each domain serves a different purpose, and the messages within each set differ. Presumably, the creators of a standard defined it so that a complete range of activities could be performed electronically. The central task of this study is organizing messages from these standards into a framework. The purpose of this task is to validate the framework, although others dis-Ž cussed below are also of some interest. .

Table 3  
Examples of each illocutionary force

<table><tr><td>Force</td><td>Example</td></tr><tr><td>Acknowledgment</td><td>Thanks for sending the shipment.</td></tr><tr><td>Advisory</td><td>You should pick up the shipment before its rots.</td></tr><tr><td>Ascriptive</td><td>The shipment was not sent because we lost your paperwork.</td></tr><tr><td>Assentive</td><td>Yes, we should pay for the shipment.</td></tr><tr><td>Assertive</td><td>The goods are ready to be shipped.</td></tr><tr><td>Concessive</td><td>We now believe that it was our fault that the shipment was not delivered.</td></tr><tr><td>Confirmative</td><td>We verified that we sent the shipment.</td></tr><tr><td>Descriptive</td><td>The shipment weighs 50 pounds.</td></tr><tr><td>Disputative</td><td>We weighed the shipment and it does not weigh 45 pounds as you claimed.</td></tr><tr><td>Dissentive</td><td>I don’t believe that you are ready to use this shipment yet.</td></tr><tr><td>Effective</td><td>Yes, I accept your offer to insure the shipment.</td></tr><tr><td>Informative</td><td>We have enough in stock to send two more shipments if you need them.</td></tr><tr><td>Offer</td><td>I will insure the shipment if you want me to.</td></tr><tr><td>Permissive</td><td>You may install the contents without my supervision.</td></tr><tr><td>Predictive</td><td>I believe the shipment will get there tomorrow.</td></tr><tr><td>Prohibitive</td><td>You may not use the contents until I arrive.</td></tr><tr><td>Promise</td><td>You will be satisfied with this product.</td></tr><tr><td>Question</td><td>Did the shipment arrive?</td></tr><tr><td>Requestive</td><td>Please open the shipment when it arrives.</td></tr><tr><td>Requirement</td><td>Open the package now.</td></tr><tr><td>Retractive</td><td>Now I don’t believe that the shipment will get there tomorrow.</td></tr><tr><td>Retrodictive</td><td>We packed the contents with great care.</td></tr><tr><td>Suggestive</td><td>Shipments are usually picked up at 4 pm.</td></tr><tr><td>Suppositive</td><td>I wouldn’t use that for that purpose because it might break.</td></tr><tr><td>Verdictive</td><td>I find you not guilty of shipping hamsters across state lines.</td></tr></table>

Speech act theorists predict all utterances should map to the F PŽ . framework. In this study, I test this prediction by attempting to classify each message of each standard into one or more of the illocutionary forces. The usefulness of SAT for electronic com-Ž merce and other will be measured by its perfor-. mance along several dimensions.

## 3.1. Successfully mapping onto the F P framework ( )

SAT will clearly have failed if even one message cannot be mapped onto the F PŽ . framework. SAT predicts that all utterances fit this framework—so even one failure will contradict SAT. However, two types of messages will not be included: messages that are text-only, non-formal messages that act more like e-mail, and messages that simply transport data from sender to recipient as a freight car would. In the first type, the message’s content is not part of the standard. It is impossible to categorize these messages not because SAT fails, but because the standard provides nothing to categorize. In the second type, the message perform a physical act but not a communicatiÕe act. It is more like a delivery of bananas than a communication of some intent.

Successfully mapping a message does not mean each message will map onto only one illocutionary force. SAT does not predict this about normal language nor is it present. Suppose a person says ‘‘Please come in here and shut the door’’. This naturally maps onto two separate acts—a request to come into the room and a request to shut the door. It would be surprising if each message mapped onto just one illocutionary force.

3.2. Mapping onto much of the illocutionary force categorization

The hierarchy of illocutionary forces described by SAT can be thought of as a tree. Mapping the messages onto SAT will be much more useful if both the tree’s depth categories and each level of sub-cat-Ž egorization and breadth illocutionary forces are. Ž . used, or covered. Property inheritance is more useful to application developers if many categories and sub-categories are used—i.e., the depth is utilized. Using a higher percentage of the forces—i.e., utilizing the breadth—indicates the force is contributing to more of the message’s meaning than if a lower percentage of the forces were used.

To understand the importance of this, consider the extreme example in which all messages map into one illocutionary force—that is, messages X, Y, etc. all map onto force A. This example suggests the illocutionary force does not contribute much to understanding the message. Even if it does contribute, other factors clearly outweigh its importance. The cost of adding this information to a message’s representation would probably outweigh its usefulness.

## 3.3. How much the standards segment the hierarchy

The more that different standards use the same parts of the tree, the more useful SAT becomes. If the tree were segmented by the standards, then the generality of SAT would have to be questioned. It would cause one to hypothesize that, as more message standards are analyzed, more illocutionary forces, sub-categories, and categories would be needed. It would also raise interesting questions about SAT, such as: Is it always the case that certain illocutionary forces are used together? Is this to the exclusion of other forces? Does this say anything about the complexity of the communication?

## 4. Message standards

This section describes the application domains and message standards used in this study. These include two EDI standards and two inter-application communication IAC standards. I included the IACŽ . standards because their uses are similar to those of

EDI. Whereas EDI involves applications at one company sending messages to applications at another company, IAC involves applications sending messages to other applications generally, but not universally, on the same computer. Further, though not by any means a requirement, applications that are acting on the receipt of an EDI message could send IAC messages to other applications and could, thus, be seen as participating in electronic commerce. It is not too much of a stretch to envision an IAC message containing information of the type that is currently only contained in EDI messages—and vice versa.

## 4.1. EDI: UN-EDIFACT open standard

The United Nations supports Electronic Data Interchange for Administration, Commerce, and Transport UN-EDIFACT 40 . This standard defines ‘‘a Ž . <sup>w</sup> <sup>x</sup> set of internationally agreed standards, directories and guidelines for the electronic interchange of structured data, and in particular that related to trade in goods and services between independent, computerized information systems’’ 40 , p. 5 . This is the<sup>w</sup> <sup>x</sup> Ž . official international standard for EDI. The American National Standards Institute ANSI X.12 EDI stan-Ž . dard 1 has been the EDI standard in the United<sup>w</sup> <sup>x</sup> States; however, ANSI has stated that it is their intent to migrate to the UN-EDIFACT standard after 1997 14 . These messages span many industries. <sup>w</sup> <sup>x</sup> Companies send these messages to their trading partners. Some messages require a return message; others require the company to send goods; others are purely informational messages.

## 4.2. EDI: SWIFT proprietary standard

‘‘SWIFT is a worldwide organization working in partnership with its customers to provide them with communication and financial data processing services of the highest quality, security and integrity’’ <sup>w</sup> <sup>x</sup> 36 , p. 5 . SWIFT developed a standard for sending Ž . messages about financial securities, such as trading of securities, settlement of trades, and securities lending and borrowing. Companies send these messages to their trading partners and to other institutions involved in financial transactions. Similar to the UN-EDIFACT messages, these messages may or may not require responses.

Table 4  
DDE messages from sample applications

<table><tr><td>Description</td><td>Excel [9]</td><td>Word [10]</td><td>Visual Basic [26]</td></tr><tr><td>Opens a DDE channel to an application</td><td>DDEInitiate</td><td>DDEInitiate</td><td>LinkOpen</td></tr><tr><td>Closes a channel to another application</td><td>DDETerminate</td><td>DDETerminate</td><td>LinkClose</td></tr><tr><td></td><td></td><td>DDETerminateAll</td><td></td></tr><tr><td>Runs a command or takes other actions in another application</td><td>DDEExecute</td><td>DDEExecute</td><td>LinkExecute</td></tr><tr><td>Requests information from the specified application</td><td>DDERequest</td><td>DDERequest</td><td>LinkRequest</td></tr><tr><td>Sends data to an application</td><td>DDEPoke</td><td>DDEPoke</td><td>LinkPoke</td></tr><tr><td>Notify the user that new data is available</td><td></td><td></td><td>LinkNotify</td></tr><tr><td>Notify the user that an error has occurred</td><td></td><td></td><td>LinkError</td></tr></table>

## 4.3. IAC on the Macintosh: Apple EÕent Registry

The Apple Event AE Registry 2 defines stan-Ž . <sup>w</sup> <sup>x</sup> dard IAC messages known as Apple Events on the Ž Apple Macintosh . Applications use these messages . to send information to other programs and to get them to perform tasks. Just as with the EDI standards, this standard does not exhaust all possible messages. This standard defines the basic messages that the operating system and common business applications e.g., a word processing or spreadsheetŽ program should be able to understand. Thus, if a. word processing application on a Macintosh claims to understand AEs, then it should understand the appropriate messages defined in this standard.

When an AE expects information in return, it leaves an electronic ‘return envelope’ with the receiver to put its information into. This envelope can contain an answer to a question or information about a problem encountered by the receiver. Thus, each message that asks a question implicitly defines a separate reply message.

## 4.4. IAC on Windows: OLE automation and Dynamic data exchange

Microsoft Windows and Windows 95 do not have a standard comparable to the AE Registry. Each application defines the OLE automation calls the Ž Microsoft implementation of IAC messages that it. can understand without regard to the messages that other, similar applications can understand. Thus, whereas all spreadsheets that run on the Macintosh are expected to understand the AEs for spreadsheets, each spreadsheet under Microsoft Windows and

Windows 95 defines the OLE automation calls that it can understand independently of other spreadsheets. Since there is no standard set of OLE messages, OLE automation is not included in the study.

DDE messages, which are a precursor with limited functionality to OLE automation calls, have a very limited vocabulary. For example, Microsoft Excel 7 for Windows 95, Word 7 for Windows 95, and Microsoft Visual Basic can send the OLE messages defined in Table 4. The limited vocabulary, the variety in nomenclature, the lack of a standard vocabulary, and the fact that DDE has essentially been replaced by OLE, are all reasons for excluding DDE messages from the study.

## 5. Procedure

I mapped each message in each standard to the illocutionary forces defined by Bach and Harnish. There are 260 messages in all: 125 UN-EDIFACT, 41 SWIFT, and 94 Apple Events. I used the following procedure for each standard:

1. Read the message’s functional description. Where this is ambiguous, investigate the message’s notes, field definitions, and the possible content of the fields.

2. Extract from the functional description a verb phrase that describes what the message means. Where this is not possible, again look to the notes for more information. I used the exact form and wording where possible, only changing to make verb tense and form more consistent among messages.

3. Continue extracting verb phrases until exhausting all the message’s possibilities. Write each on a separate line. Extract verb phrases for all messages in the standard.

4. Determine the appropriate illocutionary force for each verb phrase. Use the force hierarchy shown in Fig. 2. Write the chosen force next to the verb phrase.

I constructed Fig. 2 based on the definitions given in Appendix A. This organizes the forces into categories that helped me find relevant possibilities most quickly. Acknowledgments are not included because no messages had any of these forces.

The following describes the steps I took and decisions I made when mapping a relatively simple message, MT 501 shown in Fig. 3 . Ž .

Step 1 is information gathering—i.e., reading the scope of the message shown in the figure and theŽ . information in the rest of the definition not shown .Ž . In this case, the scope contains all that is needed. This other information is needed when the scope is not clear about the message’s function. Step 2 requires extracting from the definition a verb phrase that describes the message’s meaning. The verb phrase for this message is ‘instruct the receiver to sell a specified quantity of the identified security’. The rest of the scope is not relevant to the determination of the message’s illocutionary force; it defines who sends the message, who it is sent to, how a message should be interpreted when some information is missing, and how certain fields should be

![](/api/attachments/GHBDTEGV/fulltext/images/c07563d9e561e27ee413438c62fd47e98da4c36eee40b4616f928471f3ff4bce.jpg)  
Fig. 2. Hierarchy of illocutionary forces used during mapping.  
Fig. 3. Definition of the scope of MT 501 from the SWIFT Securities Market Binder <sup>w</sup> <sup>x</sup> 36 , p. 5-1.

MT 501 Order to Sell This message type is sent by the client, or its authorized representative, to a financial institution.

It is used to instruct the Receiver to sell a given quantity of an identified security under specified conditions.

The following guidelines apply when sending an MT 501:

• When settlement instructions are not provided, standing instructions for delivery and payment apply.

● When a specific type of deal, such as spot or forward, needs to be identified, this identification will be located in field 23.

filled in given certain circumstances. Step 3 instructs the mapper to look for other verb phrases. As we can see, MT 501’s definition does not have any.

Although steps 1–3 are essentially mechanical, step 4 is not nearly so clear-cut. The mapper’s judgment comes into play when determining which illocutionary force the verb phrase carries. Ideally, the mapper reads the verb phrase and then finds the corresponding force from those shown in the classification in Fig. 2 with reference to Fig. 1, the infor- Ž mal definitions in Table 2, and the formal definitions in Appendix A . Bach and Harnish present the forces. as all being on the same ‘level’ of the hierarchy as Ž shown in Fig. 1 . This is not the case—some are. specializations of others.

Consider the utterance ‘‘It is raining’’ and assume that the speaker is speaking directly and literally. <sup>1</sup> Without knowing more about the situation, it appears that this utterance is either an assertive or an informative. The definitions in Appendix A specify that an informative occurs when the speaker is telling the hearer something that the speaker assumes the hearer does not know, while an assertive occurs when the speaker is simply telling the hearer something without that assumption. Since the mapper does not know if the hearer knows if it is raining without beingŽ able to ask , this utterance should be classified as an . assertive. If the mapper had known that the speaker actually did think that the hearer did not know it was raining, then the mapper would have classified the utterance as an informative.

This highlights several important facets of mapping. First, a message’s force is determined by what the speaker is attempting to accomplish with the utterance and not by what he actually accomplishes, or what the hearer thinks the speaker is trying to accomplish. For example, with the utterance above, the force is an assertive because the speaker is attempting to tell the hearer that it is raining. It is irrelevant for our purposes as to whether the hearerŽ . believes that it is raining, or whether the hearer thinks that the speaker is attempting to get her to turn off the garden hose. This is where the choice of an inferential model comes to the fore. Under a decoding theory, there is little difference between understanding the utterance, and knowing what the speaker wants the hearer to do. An inferential theory separates these two. When classifying an EDI message the mapper need only know the meaning of the message as specified by the speaker. Information about whether a particular message is understood correctly or whether or not it had the intended consequences does not change its illocutionary force. The implications of this separation are discussed in Section 7.

Second, it is quite possible to misclassify an utterance i.e., a message because of a lack of Ž . information about the speaker’s intentions. This mostly has to do with the sometimes vague, and always complex, message definitions rather than with some failure of the mapper or the process. A quote from a practitioner relayed by Ronald Lee reflectsŽ . this: ‘‘I’m the only one using a purchase order as a purchase order’’. Fortunately, this does not have dire consequences in most cases when mapping EDI messages; that is, it has little effect on how the message should be interpreted. The misclassification is generally minor because of the assumption about speaking literally and directly. A graphical interpretation of ‘minor’ in Fig. 2 is that the differing illocutionary Ž . forces are on the same ‘branch’ of the hierarchy. For example, if the mapper had misclassified the raining assertion as an informative, this would be considered minor since informative is on the same branch as assertive.

Further, this misclassification problem only exists because the messages are being mapped after they haÕe been defined. If companies were to implement an EDI system that has each message defined in terms of its illocutionary forces, this problem need not exist. Each illocutionary force would be defined, and each message would be defined in terms of these forces. The possibility for misunderstandings would be greatly reduced because the sending party’s intentions would be clear, and each partner would be mutually aware that the sending party sent the message with full knowledge of these definitions.

Third, the most specific illocutionary force possible should be mapped to a message. Graphically, this can be interpreted as saying that the applicable force farthest to the right in the graph in Fig. 2 should be chosen. In the above example, the choice is between informative and assertive. I chose assertive because informative did not seem applicable as explained above. If it had been applicable, I would have chosen it because it would have most specifically mapped to the message.

Thus, much of a mapper’s judgment comes into play in Step 4. Determining what the speaker is attempting to accomplish is very much an educated guess based on the evidence presented in the message’s definition. As mentioned above, much of the difficulty of this decision for an actual implementation would be removed because trading partners would define the messages in terms of the illocutionary forces before they are used. The benefits of this are discussed in Section 7.

Returning to MT 501: Applying Step 4 to this message involves determining the force carried by ‘instruct the receiver to sell a specified quantity of the identified security’. This involves choosing the appropriate force from Fig. 2. In this case, I started at the left side of the tree and moved to the right by choosing the appropriate branches. In this message, the speaker is instructing the receiver—that is, the speaker is directing the receiver to do something. This narrows down the search for an illocutionary force to the directing branch of Fig. 2. For definitions of each force those items in Fig. 2Ž . in this font I first referred to Tables 2 and 3; if this was not sufficient, then I referred to the definitions in Appendix A. This verb phrase seems to map to requirement: ‘ask someone else to do something from a position of authority’. The ‘position of authority’ is a contractual obligation that already exists between the sender and the receiver, which specifies that the receiver will dispose of assets owned by the sender under instructions from the sender. MT 501 fits the definition of requirement. Looking in the notes found in Table 6, MT 501 is listed on just one line and is classified as a requirement. This is one verb phrase from one message from one standard. Each line in the appendix represents other verb phrases, the associated illocutionary force, and a similar mapping process.

![](/api/attachments/GHBDTEGV/fulltext/images/b189be23aec7104859c50b6fd8ab4c5c8d32ed375119eceb22ad27914350e1f2.jpg)  
Fig. 4. Definition of the scope of MT 550 from the SWIFT Securities Market Binder.

Not all mappings are as straightforward as that for MT 501. Consider MT 550 shown in Fig. 4. The mapper must first determine the verb phrase s thisŽ . message definition contains. I propose that there is but one: ‘‘provide the Receiver with details of rights to a current or future debt or equity subscription’’. It could be argued that this actually should be two verb phrases: ‘provide details of rights to a current subscription’ and ‘provide details of rights to a future subscription’. However, this message describes the current status of the recipient’s rights in regards to the current or future subscription. If a separate verb phrase were to be needed for the rights to the future subscription thereby changing it to a predictive , theŽ . message would have to convey information either about the possibility that the recipient will have

![](/api/attachments/GHBDTEGV/fulltext/images/25073b5a8abb5c7ba44b3143e7a6d10b14d0d54127fe906e0cfc91bf81aec14f.jpg)  
Fig. 5. Definition of the scope of MT 526 from the SWIFT Securities Market Binder.

MT 526 General Securities Lending/Borrowing Message This message type is sent from one financial institution to another, both of which are involved in the lending of securities. It is used to:

• list specified securities available for lending by the Lender or its agent

• list specified securities no longer available for lending by the Lender or its agent

● request the borrowing of a specified security from the Lender or its agent

• notify the Borrower or its agent of a partial or total return of the securities out on loan

• notify the Lender or its agent of a partial or total return of the securities borrowed

• request the potential Lender to hold the specified securities until further notice

• confirm that specified securities are being held

● request the potential Borrower to confirm a securities loan or cancel a request to hold securities until further notice.

future rights, or about the projected amount of future rights that the recipient might have. Since neither is the case, I propose that MT 550 has just one verb phrase. Further, I propose that this verb phrase is a descriptive, since the sender describes an object and intends that the recipient believe the description see Ž the definition of descriptive in the appendix ..

The definition of MT 550 also states that it normally requires a response instructing the custodian of any actions it should take. I could not find anything in the extended definition in the scope or fieldŽ definitions that explicitly requests or requires that. the recipient respond to the message. Thus, I assumed that this ‘normal requirement’ is an industry practice that has been established. That a response would end up being sent as a result of the original MT 550 message seems to be less of a result of some request for that response, and more of an expected or intended effect that the speaker hoped the message would have. This expected or intended effect is exactly what linguists define as the perlocutionary effect of a message. Thus, I did not classify MT 550 as having either a requirement or requestive force.

Other messages are more explicit about their ability to perform multiple functions e.g., MT 526Ž shown in Fig. 5 . Depending on the contents of the. message, one particular MT 526 might be categorized as an informative ‘list’ , a retrodictiveŽ . Ž . Ž . ‘notify’ , a requestive ‘request’ , or a confirmative Ž . ‘confirm’ . It holds any one of these forces to the exclusion of the others. Other messages can be used in different ways at the same time.

## 6. Results

Table 6 shows how I mapped the messages in each of the three standards. The results generally supported SAT. The following is an analysis of each dimension of the study.

## 6.1. Successfully mapping onto the F P framework ( )

I mapped all the well-defined messages onto the F PŽ . framework. The SWIFT standard contains two messages 598, 599 that could not be mapped be-Ž . cause their contents were not well defined. Message 598 is defined as a ‘proprietary message’ with no further explanation. Message 599 is defined as a ‘free format’ message. Its contents are not interpretable by a machine. Both of these messages are not well-defined and were not included in this test.

Similar to Message 599, UN-EDIFACT messages DIRDEF ‘transfer contents of a directory set’ , Ž . GENRAL ‘send general application support infor-Ž mation’ , GESMES ‘transmit statistical data set’. Ž . and RDRMES ‘report raw data’ perform more of aŽ . transportation function than a communicative function. Other messages have sections that can contain plain text e.g., section FTX in UN-EDIFACT mes-Ž sage ORDRSP in addition to the computer- . processable sections. These plain text sections are similar to the free text message SAT 599. All of these messages and sections were excluded.

A more interesting verb phrase that could not directly be mapped is from STATAC: ‘remind of payment due’. ‘Remind’ does not fit the definition of any illocutionary force. It is actually a perlocutionary effect that the speaker hopes the message in thisŽ case, an assertion that payment is due will have on. its recipient. This definition went beyond simply defining what the message means to defining its possible effects on the recipient. As stated in Section 5, this study separates these two. The first relates to the illocutionary force and the second to the perlocutionary effect.

Another interpretation of ‘remind’ is that it occurs when a speaker asserts some fact that the speaker thinks the hearer already knows, but may have forgotten. This reading would classify this phrase as an assertive. The primary use of STATAC is to provide information about the status of an account a descrip-Ž tive . Again, there is nothing in the extended defini-. tion that indicates that the message is serving as a reminder separate from its function as a descriptive. Thus, I read the ‘reminding’ function of this message as an expected effect the speaker hopes the message to have—that is, as its perlocutionary effect. As a perlocutionary effect, ‘remind’ is not appropriate for inclusion in this study.

There were not any AEs that could not be mapped; however, five AE replies messages replying to an Ž inquiry from another AE fit this category: Cre- . ateElement, GetData, DoScript, EditGraphic, and ImageGraphic. Each of these simply transmit data from one program to another without any communicative intention.

The above were the only messages that I was not able to map onto the F PŽ . framework. Certainly, this investigation does not provide the final word on this subject. The main objection is that the author performed the mappings that are the foundation of the investigation and its conclusions. To counter this objection, I have presented as much of the raw data as is feasible within these pages. Much of the rest of the needed information is available on the Web Žeither from Premenos or my web site, both of which are mentioned in the Notes at the end of this article .. This allows the interested reader to perform the mapping herself and compare results with those presented here.

## 6.2. Mapping onto much of the illocutionary force categorization

For each standard Table 5 displays the number of messages that can possibly have each illocutionary force. The number of messages in each standard Ž . displayed in the first row of the table does not equal the sum of the numbers below it in the table for two reasons. First, some messages in each standard can have one of several forces. Second, others can have several forces each time they are sent depending on how they are constructed.

Table 5  
Messages assigned to each force

<table><tr><td rowspan="2">Category</td><td>Force</td><td>UN-EDIFACT</td><td>SWIFT</td><td>AE</td></tr><tr><td>No. of messages</td><td>125</td><td>41</td><td>59</td></tr><tr><td colspan="5">Communicative</td></tr><tr><td rowspan="6">Constatives</td><td>Confirmative</td><td>6</td><td>8</td><td></td></tr><tr><td>Descriptive</td><td>36</td><td>8</td><td>34</td></tr><tr><td>Disputative</td><td>1</td><td></td><td></td></tr><tr><td>Informative</td><td>24</td><td>12</td><td>35</td></tr><tr><td>Predictive</td><td>20</td><td>4</td><td></td></tr><tr><td>Retrodictive</td><td>28</td><td>13</td><td>3</td></tr><tr><td rowspan="4">Directives</td><td>Permissive</td><td>3</td><td></td><td></td></tr><tr><td>Question</td><td>1</td><td></td><td></td></tr><tr><td>Requestive</td><td>22</td><td>6</td><td>55</td></tr><tr><td>Requirement</td><td>12</td><td>13</td><td></td></tr><tr><td rowspan="2">Commissives</td><td>Offer</td><td>5</td><td></td><td></td></tr><tr><td>Promise</td><td>7</td><td></td><td></td></tr><tr><td colspan="5">Conventional</td></tr><tr><td>Effectives</td><td>8 verbs</td><td>17</td><td></td><td></td></tr><tr><td>Verdictives</td><td>1 verb</td><td>1</td><td></td><td></td></tr></table>

Messages can be assigned to more than one force. No messages categorized as an advisory, ascriptive, assentive, assertive, concessive, dissentive, prohibitive, retractive, suggestive, or suppositive. Further, no messages were classified as an acknowledgment of any kind.

This table relates to Table 6 in the following way. The table shows that 6 messages in the UN-EDIFACT standard can have a confirmative illocutionary force. The first 7 rows of Table 6 show confirmative messages in this standard. It also shows that the CODECO message can have the confirmative force in two different ways. CODECO counts as one confirmative since the table shows the number of messages, not verb phrases, that were mapped to each force. Other values in the table are computed similarly.

The UN-EDIFACT standard covered the largest proportion of the tree: 13 forces 20 if you count the Ž different types of effectives and five of six cate-. gories constatives, directives, commissives, effec-Ž tives, and verdictives . This still leaves 10 other. forces without messages mapped to them plus the whole acknowledgment category. Thus, this investigation neither fully supports nor refutes the contention that the standards would map onto much of the illocutionary force categorization. There are at least two possible reasons for this. First, the difficulty, in a bureaucratic sense, of the standardization process limits the number of messages that will ever be defined and the speed at which they are defined. Second, people do not expect computers to express certain types of messages. For example, a condolence in any type of automated system would be perceived as inappropriate.

The SWIFT standard covered the next largest portion of the tree: 7 forces and only two of six categories constatives and directives . It is instruc- Ž . tive to note which categories are not included in the SWIFT standard but are covered by the UN-EDIFACT standard: commissives promises and of-Ž fers , effectives e.g., accept, cancel, reject , and . Ž . verdictives e.g., attest . These are the forces withŽ . which commitments are made and work is done. This pattern of exclusion makes it clear that SWIFT uses their EDI system to transfer information. Very little of the system is used to actually do financial trading; this is left up to people or some other Ž system ..

The AE standard only expresses four illocutionary forces directly the AE column of Table 6 . This is aŽ . clear signal that the designers of the AE communication system had a narrow vision of how applications would use them. Similar to the SWIFT standard, it only has constatives and directives. Further, it does not have any retrodictives statements about the pastŽ . or predictives statements about the future . AEsŽ . focus strictly on current events and the current environment.

However, this system is not quite as simplistic as it seems. Two other places within AEs can contain an illocutionary force. First, the reply message can express an illocutionary force as shown in the AEŽ reply column of Table 5 . This adds one more force. Ž . Ž descriptive to the list of forces used by AEs either directly or within a response . Second, the message. can express another illocutionary force within the message; this is called an iterated illocutionary force. As I have assumed throughout this article and, IŽ hope, have begun to show , all utterances and,. Ž hence, all EDI messages fit within the. Ž . F P framework. As defined in Section 2, P is the message’s propositional content. Sometimes this P can have, instead of just a simple predicate, a more complex form such as $F _ { 1 } ( P )$ where $F _ { 1 }$ is any illocutionary force. For example, you can request that Fred inform Barney that Betty went outside—F is request, $F _ { 1 }$ is inform, and P is that Betty went outside. The second column of Table 7 counts the $F _ { 1 }$ for all the AEs of the form $F ( F _ { 1 } ( P ) )$ where F is a requestive force. The third column lists the corresponding AEs. For example, GetEventInfo is listed on the informative row. This message ‘requests information about the Apple events in a suite.’ Rewording this to clarify the structure of the sentence we get ‘the sender requests that the receiver inform the sender about the Apple events in a suite.’ This corresponds to a message with an $F ( F _ { 1 } ( P ) )$ structure, that is request inform P . By considering this iterated force,Ž Ž .. we can see that AEs use two more forces, permissives and retractives. However, this still leaves AEs using only 7 illocutionary forces.

Table 6  
Classification of UN-EDIFACT and SWIFT messages

<table><tr><td>Illocutionary force</td><td>Message ID</td><td>Verb phrase</td></tr><tr><td></td><td></td><td>UN-EDIFACT messages</td></tr><tr><td>Confirmative</td><td>CODECO</td><td>Confirm that containers have been delivered</td></tr><tr><td>Confirmative</td><td>CODECO</td><td>Confirm that containers have been picked up</td></tr><tr><td>Confirmative</td><td>CONWQD</td><td>Justify to receiver information already given</td></tr><tr><td>Confirmative</td><td>COSTCO</td><td>Confirm that goods have been stuffed into (or stripped from) containers</td></tr><tr><td>Confirmative</td><td>JOBCON</td><td>Confirm receipt of information about jobs</td></tr><tr><td>Confirmative</td><td>ORDRSP</td><td>Confirm acceptance</td></tr><tr><td>Confirmative</td><td>SSREGW</td><td>Confirm a registration number</td></tr><tr><td>Descriptive</td><td>BANSTA</td><td>Provide status information</td></tr><tr><td>Descriptive</td><td>BAPLIE</td><td>Transmit information about equipment on a means of transport</td></tr><tr><td>Descriptive</td><td>BAPLTE</td><td>Transmit information about the total numbers of equipment on a means of transport</td></tr><tr><td>Descriptive</td><td>BOPBNK</td><td>Report a bank&#x27;s assets and liabilities position</td></tr><tr><td>Descriptive</td><td>COMDIS</td><td>Provide details about an existing dispute</td></tr><tr><td>Descriptive</td><td>CONDRO</td><td>Describe general project organization</td></tr><tr><td>Descriptive</td><td>CONRPW</td><td>Give details of networks where construction work will be undertaken</td></tr><tr><td>Descriptive</td><td>CUSRES</td><td>Report errors in data</td></tr><tr><td>Descriptive</td><td>DESADV</td><td>Inform the recipient about goods in a consignment</td></tr><tr><td>Descriptive</td><td>DOCADV</td><td>Indicate terms and conditions of a documentary credit</td></tr><tr><td>Descriptive</td><td>DOCAMA</td><td>Inform the beneficiary of the terms and conditions of an amendment to a documentary credit</td></tr><tr><td>Descriptive</td><td>DOCAMI</td><td>Indicate terms and conditions of an amended documentary credit</td></tr><tr><td>Descriptive</td><td>DOCINF</td><td>Indicate terms and conditions of an issued documentary credit</td></tr><tr><td>Descriptive</td><td>FINSTA</td><td>Provide a statement of booked items in an account</td></tr><tr><td>descriptive</td><td>IFTIAG</td><td>Convey information relating to one conveyance of a means of transport on the dangerous goods carried on board</td></tr><tr><td>Descriptive</td><td>IFTMAN</td><td>Give details of the arrival of a consignment</td></tr><tr><td>Descriptive</td><td>IFTSTA</td><td>Report transport status</td></tr><tr><td>Descriptive</td><td>INVRPT</td><td>Specify information relating to held inventories</td></tr><tr><td>Descriptive</td><td>JAPRES</td><td>Provide detailed information of the employment of an applicant</td></tr><tr><td>Descriptive</td><td>JAPRES</td><td>Provide detailed information of the rejection of the applicant by the employer</td></tr><tr><td>Descriptive</td><td>JAPRES</td><td>Provide detailed information of the rejection of the offered job by the applicant</td></tr><tr><td>Descriptive</td><td>JOBMOD</td><td>Modify information about a previously offered job</td></tr><tr><td>Descriptive</td><td>JOBOFF</td><td>Specify details for job vacancies at an employer to an agency</td></tr><tr><td>Descriptive</td><td>MEDPID</td><td>Pass detailed information on persons between organizations</td></tr><tr><td>Descriptive</td><td>ORDERS</td><td>Specify details for goods ordered under conditions agreed upon</td></tr><tr><td>Descriptive</td><td>PARTIN</td><td>Transmit basic information regarding trading partners</td></tr><tr><td>Descriptive</td><td>PAXLST</td><td>Transmit passenger data</td></tr><tr><td>Descriptive</td><td>PAYEXT</td><td>Provide details</td></tr><tr><td>Descriptive</td><td>PRICAT</td><td>Transmit information regarding catalog details for goods offered for sale</td></tr><tr><td>Descriptive</td><td>BOPDIR</td><td>Report foreign assets</td></tr><tr><td>Descriptive</td><td>SAFHAZ</td><td>Communicate data on materials supplied</td></tr><tr><td>Descriptive</td><td>SANCRT</td><td>Provide details about the means of conveyance of a product</td></tr><tr><td>Descriptive</td><td>SSIMOD</td><td>Communicate details related to worker identity</td></tr><tr><td>Descriptive</td><td>STATAC</td><td>Provide information about status of an account</td></tr><tr><td>Descriptive</td><td>SUPMAN</td><td>Specify membership information</td></tr><tr><td>Descriptive</td><td>TANSTA</td><td>Transmit current status about non-cargo deadweight items</td></tr><tr><td>Descriptive</td><td>WKGRDC</td><td>Specify Details of a decision</td></tr><tr><td>Descriptive</td><td>WKGRRE</td><td>Detail information about a person</td></tr><tr><td>Disputative</td><td>RECADV</td><td>Report discrepancies about physical receipt of goods</td></tr><tr><td>Effective: Accept</td><td>DOCARE</td><td>Advise the acceptance of an amendment</td></tr><tr><td>Effective: Accept</td><td>IFTMBC</td><td>Accept the booking of a consignment</td></tr><tr><td>Effective: Accept</td><td>JAPRES</td><td>Specify decisions of an employer related to job applications</td></tr><tr><td>Effective: Accept</td><td>JAPRES</td><td>Specifies acceptance of an employer related to job applications</td></tr></table>

Table 6 continued Ž .

<table><tr><td>Illocutionary force</td><td>Message ID</td><td>Verb phrase</td></tr><tr><td>Effective: Accept</td><td>RECECO</td><td>Accept request for credit protection</td></tr><tr><td>Effective: Accept</td><td>WKGRDC</td><td>Inform of the acceptance of a work grant request</td></tr><tr><td>Effective: Agree</td><td>COMDIS</td><td>Notify the receiver that the sender agrees to the settlement</td></tr><tr><td>Effective: Apply</td><td>RECECO</td><td>Apply for credit protection</td></tr><tr><td>Effective: Cancel</td><td>RECECO</td><td>Cancel credit protection</td></tr><tr><td>Effective: claim</td><td>INVOIC</td><td>Claim payment for goods or services supplied under conditions agreed upon claim</td></tr><tr><td>Effective: Declare</td><td>CUSDEC</td><td>Declare information about goods for import, export, or transit</td></tr><tr><td>Effective: Non-accept</td><td>DOCARE</td><td>Advise the non-acceptance of an amendment</td></tr><tr><td>Effective: Non-accept</td><td>ORDRSP</td><td>Notify of non-acceptance</td></tr><tr><td>Effective: Reject</td><td>IFTMBC</td><td>Reject the booking of a consignment</td></tr><tr><td>Effective: Reject</td><td>JAPRES</td><td>Specify decisions of an employer related to job applications</td></tr><tr><td>Effective: Reject</td><td>JAPRES</td><td>Specifies rejection of an employer related to job applications</td></tr><tr><td>Effective: Reject</td><td>RECECO</td><td>Reject request for credit protection</td></tr><tr><td>Effective: Reject</td><td>WKGRDC</td><td>Inform of the rejection of a work grant request</td></tr><tr><td>Informative</td><td>CONITT, CONTEN</td><td>Communicate project design changes</td></tr><tr><td>Informative</td><td>CUSREP, CUSEXP</td><td>Report on the means of transport on which cargo is carried</td></tr><tr><td>Informative</td><td>APERAK</td><td>Inform that a message has been rejected due to errors</td></tr><tr><td>Informative</td><td>APERAK</td><td>Acknowledge a message</td></tr><tr><td>Informative</td><td>BANSTA</td><td>Report on errors in a message</td></tr><tr><td>Informative</td><td>BOPDIR</td><td>Report responses to a questionnaire</td></tr><tr><td>Informative</td><td>COEDOR</td><td>Report containers that are in stock</td></tr><tr><td>Informative</td><td>CONDRA</td><td>Give information about engineering computer files</td></tr><tr><td>Informative</td><td>CONPVA</td><td>Advise receiver about the value of work already performed</td></tr><tr><td>Informative</td><td>CUSRES</td><td>Report errors in data</td></tr><tr><td>Informative</td><td>IFCSUM</td><td>Provide a statement for a means of transport for cargo</td></tr><tr><td>Informative</td><td>IFTCCA</td><td>Provide the calculation of transport charges</td></tr><tr><td>Informative</td><td>IFTDGN</td><td>Declare that goods are dangerous goods</td></tr><tr><td>Informative</td><td>IFTFCC</td><td>Specify freight, handling, and transport costs</td></tr><tr><td>informative</td><td>IFTMAN</td><td>Give notice of the arrival of a consignment</td></tr><tr><td>Informative</td><td>IFTRIN</td><td>Provide transport rate information</td></tr><tr><td>Informative</td><td>INSPRE</td><td>Notify the recipient about premiums due from a client</td></tr><tr><td>Informative</td><td>ORDRSP</td><td>Acknowledge understanding of data</td></tr><tr><td>Informative</td><td>QALITY</td><td>Transmit results of tests</td></tr><tr><td>Informative</td><td>RESETT</td><td>Send information necessary for reinsurance settlement</td></tr><tr><td>Informative</td><td>RETACC</td><td>Report a position with respect to one reinsurance contract</td></tr><tr><td>Informative</td><td>SSREGW</td><td>Communicate social security numbers</td></tr><tr><td>Informative</td><td>WKGRRE</td><td>Modify an existing work grant request</td></tr><tr><td>Offer</td><td>CONTEN</td><td>Submit a tender (a commercial offer to execute the project work)</td></tr><tr><td>Offer</td><td>IFTMBC</td><td>Define the terms under which requested services would take place</td></tr><tr><td>Offer</td><td>JOBAPP</td><td>Propose applicants for a job</td></tr><tr><td>Offer</td><td>ORDRSP</td><td>Propose an amendment</td></tr><tr><td>Offer</td><td>QUOTES</td><td>Provide information for potential sales of goods</td></tr><tr><td>Permissive</td><td>AUTHOR</td><td>Authorize a bank to execute a transaction</td></tr><tr><td>Permissive</td><td>COREOR</td><td>Give permission for containers to be picked up</td></tr><tr><td>Permissive</td><td>DELFOR</td><td>Authorize commitment of resources</td></tr><tr><td>Predictive</td><td>CREADV, CREEXT, CREMUL</td><td>Inform account owner that its account will be credited</td></tr><tr><td>Predictive</td><td>CREADV, CREEXT, CREMUL</td><td>Provide the payee details of a transaction that will occur</td></tr><tr><td>Predictive</td><td>CUSCAR, CUSEXP</td><td>Report that consignments will be arriving</td></tr><tr><td>Predictive</td><td>DEBADV</td><td>Inform account owner that its account will be debited</td></tr><tr><td></td><td>DEBMUL</td><td>Specify short-term delivery schedules</td></tr><tr><td>Predictive</td><td>DELFOR, DELJIT</td><td>Requested by a buyer</td></tr></table>

Table 6 continuedŽ .

<table><tr><td>Illocutionary force</td><td>Message ID</td><td>Verb phrase</td></tr><tr><td>Predictive</td><td>CALINF</td><td>Provide information about planned arrival of a vessel</td></tr><tr><td>Predictive</td><td>CODENO</td><td>Notify for which cargo that customs documents will expire at short notice</td></tr><tr><td>Predictive</td><td>COMDIS</td><td>Notify the receiver that certain actions will be taken</td></tr><tr><td>Predictive</td><td>CONAPW</td><td>Advise authorities of sender&#x27;s intention to start work</td></tr><tr><td>Predictive</td><td>COPARN</td><td>Announce the impending arrival of containers</td></tr><tr><td>Predictive</td><td>COPINO</td><td>Notify the receiver of the delivery or pick-up of containers</td></tr><tr><td>Predictive</td><td>COPINO</td><td>Indicate a location at which the means of transport is to arrive</td></tr><tr><td>Predictive</td><td>DELFOR</td><td>Provide details about a product&#x27;s future production schedule</td></tr><tr><td>Predictive</td><td>DESADV</td><td>Advise the recipient as to when goods will be dispatched</td></tr><tr><td>Predictive</td><td>IFTSAI</td><td>Provide transport schedule</td></tr><tr><td>Predictive</td><td>PRPAID</td><td>Notify about premiums that will be collected</td></tr><tr><td>Predictive</td><td>SLSFCT</td><td>Forecast data related to products or services</td></tr><tr><td>Predictive</td><td>TANSTA</td><td>Transmit forecast status about non-cargo deadweight items</td></tr><tr><td>Promise</td><td>CONRPW</td><td>Giving legally binding information about existing services or networks</td></tr><tr><td>Promise</td><td>IFTMCS</td><td>Provide actual details of the service to be provided</td></tr><tr><td>Promise</td><td>PRODEX</td><td>Provide information about movement of Products that will occur</td></tr><tr><td>Promise</td><td>REMADV</td><td>Provides detailed accounting relative to a payment to be made</td></tr><tr><td>Promise</td><td>IFTMBF, IFTMIN</td><td>Book forwarding services for a consignment contract</td></tr><tr><td>Promise</td><td>CONEST</td><td>Amend the original contractual documentation with changes approved by both contract parties</td></tr><tr><td>Promise</td><td>IFTMIN</td><td>Provide final details of services to be provided, resulting in a contract</td></tr><tr><td>Requestive</td><td>RESMSG, SUPRES</td><td>Request services</td></tr><tr><td>Requestive</td><td>AUTHOR</td><td>Request authorization to execute a transaction</td></tr><tr><td>Requestive</td><td>CONAPW</td><td>Request receiver to send information</td></tr><tr><td>Requestive</td><td>CONITT</td><td>Issue an invitation to tender to contractors</td></tr><tr><td>Requestive</td><td>CUSRES</td><td>Request a declaration about goods</td></tr><tr><td>Requestive</td><td>DOCAMR</td><td>Request a bank to amend terms and conditions</td></tr><tr><td>Requestive</td><td>DOCAPP</td><td>Request issuance of a documentary credit</td></tr><tr><td>Requestive</td><td>FINCAN</td><td>Request cancellation of a financial message or transaction</td></tr><tr><td>Requestive</td><td>IFTCCA</td><td>Request the calculation of transport charges</td></tr><tr><td>Requestive</td><td>IFTMBP</td><td>Request forwarding services for a consignment</td></tr><tr><td>Requestive</td><td>IFTRIN</td><td>Request transport rate information</td></tr><tr><td>Requestive</td><td>IFTSAI</td><td>Request transport schedule</td></tr><tr><td>Requestive</td><td>IFTSTQ</td><td>Request an international multimodal status report</td></tr><tr><td>Requestive</td><td>JINFDE</td><td>Request additional information about a person and/or a job</td></tr><tr><td>Requestive</td><td>ORDCHG</td><td>Request to change a purchase order</td></tr><tr><td>Requestive</td><td>RECLAM</td><td>Request settlement concerning a loss</td></tr><tr><td>Requestive</td><td>REQDOC</td><td>Request sending of data</td></tr><tr><td>Requestive</td><td>REQOTE</td><td>Solicit price</td></tr><tr><td>Requestive</td><td>SSREGW</td><td>Request details about a worker&#x27;s social security insurance record</td></tr><tr><td>Requestive</td><td>TANSTA</td><td>Advise of a desired arrival condition</td></tr><tr><td>Requestive</td><td>WKGRRE</td><td>Request a work grant or permit</td></tr><tr><td>Requirement</td><td>PAYEXT, PAYMUL, PAYORD</td><td>Instruct to debit</td></tr><tr><td>Requirement</td><td>PAYEXT, PAYMUL, PAYORD</td><td>Arrange for payment</td></tr><tr><td>Requirement</td><td>COHAOR</td><td>Order that receiver perform special handling on containers</td></tr><tr><td>Requirement</td><td>CONDPV</td><td>Instruct receiver to pay subcontractors</td></tr><tr><td>Requirement</td><td>COPARN</td><td>Order to release containers</td></tr><tr><td>Requirement</td><td>COPRAR</td><td>Order that containers have to be discharged from or loaded into a seagoing vessel</td></tr><tr><td>Requirement</td><td>COREOR</td><td>Order to release containers</td></tr><tr><td>Requirement</td><td>COSTOR</td><td>Order that goods should be stuffed into (or stripped from) containers</td></tr><tr><td>Requirement</td><td>DIRDEB</td><td>Instruct a bank to claim some amount from another bank</td></tr></table>

Table 6 continuedŽ .

<table><tr><td>Illocutionary force</td><td>Message ID</td><td>Verb phrase</td></tr><tr><td>Requirement</td><td>HANMOV</td><td>Identify handling services to be performed by a distribution center to move goods from seller to buyer</td></tr><tr><td>Requirement</td><td>MOVINS</td><td>Instruct regarding the loading and discharging of cargo</td></tr><tr><td>Retrodictive</td><td>BOPBNK, BOPCUS, BOPDIR</td><td>Report transactions</td></tr><tr><td>Retrodictive</td><td>CREADV, CREEXT, CREMUL</td><td>Inform account owner that its account has been credited</td></tr><tr><td>Retrodictive</td><td>CREADV, CREEXT, CREMUL</td><td>Provide the payee details of a transaction that has occurred</td></tr><tr><td>Retrodictive</td><td>CUSCAR, CUSEXP</td><td>Report consignments that have arrived</td></tr><tr><td>Retrodictive</td><td>DEBADV, DEBMUL</td><td>Inform account owner that its account has been debited</td></tr><tr><td>Retrodictive</td><td>APERAK</td><td>Inform that a message has been received</td></tr><tr><td>Retrodictive</td><td>BOPINF</td><td>Report receipt of payment in settlement of a transaction</td></tr><tr><td>Retrodictive</td><td>COARRI</td><td>Report that containers have been discharged</td></tr><tr><td>Retrodictive</td><td>COARRI</td><td>Report that containers have been loaded</td></tr><tr><td>Retrodictive</td><td>CODENO</td><td>Notify for which cargo regulatory customs clearance has taken place</td></tr><tr><td>Retrodictive</td><td>COMDIS</td><td>Notify the seller that something was found wrong with goods delivered</td></tr><tr><td>Retrodictive</td><td>CONQVA</td><td>Submit progress details to a client</td></tr><tr><td>Retrodictive</td><td>CUSRES</td><td>Notify of release or clearance of a shipment</td></tr><tr><td>Retrodictive</td><td>CUSRES</td><td>Declare that a previous message has been accepted</td></tr><tr><td>Retrodictive</td><td>CUSRES</td><td>Declare that a previous message has been rejected</td></tr><tr><td>Retrodictive</td><td>DESADV</td><td>Advise the recipient as to when goods were dispatched</td></tr><tr><td>Retrodictive</td><td>ORDRSP</td><td>Acknowledge receipt of a purchase order</td></tr><tr><td>Retrodictive</td><td>SSREGW</td><td>Acknowledge receipt of a notification of registration of a worker</td></tr><tr><td>Retrodictive</td><td>PAYDUC</td><td>Detail payments made</td></tr><tr><td>Retrodictive</td><td>PRPAID</td><td>Notify about premiums that have been collected</td></tr><tr><td>Retrodictive</td><td>RECADV</td><td>Report physical receipt of goods</td></tr><tr><td>Retrodictive</td><td>RECLAM</td><td>Send information concerning a loss</td></tr><tr><td>Retrodictive</td><td>SLSRPT</td><td>Transmit sales data</td></tr><tr><td>Retrodictive</td><td>SSRECH</td><td>Gives details of a worker&#x27;s social security insurance history</td></tr><tr><td>Retrodictive</td><td>SSREGW</td><td>Advise that a national has registered</td></tr><tr><td>Retrodictive</td><td>SSREGW</td><td>Advise of a SSN allocated to a national</td></tr><tr><td>Retrodictive</td><td>SUPCOT</td><td>Detail payments made</td></tr><tr><td>Retrodictive</td><td>VESDEP</td><td>Inform of the closing of a file</td></tr><tr><td>Retrodictive</td><td>VESDEP</td><td>Give information on actual operations</td></tr><tr><td>Verdictive: attest</td><td>SANCRT</td><td>Attest to the status of a product</td></tr><tr><td></td><td></td><td>SWIFT messages</td></tr><tr><td>Confirmative</td><td>512</td><td>Confirm the details of a securities trade and its settlement</td></tr><tr><td>Confirmative</td><td>516</td><td>Confirm the details of a securities loan</td></tr><tr><td>Confirmative</td><td>516</td><td>Confirm the details of a partial recall or return of securities out on loan</td></tr><tr><td>Confirmative</td><td>526</td><td>Confirm that securities are being held</td></tr><tr><td>Confirmative</td><td>530</td><td>Confirm the receipt of securities</td></tr><tr><td>Confirmative</td><td>531</td><td>Confirm the receipt of securities</td></tr><tr><td>Confirmative</td><td>532</td><td>Confirm the delivery of securities</td></tr><tr><td>Confirmative</td><td>533</td><td>Confirm the delivery of securities</td></tr><tr><td>Confirmative</td><td>563</td><td>Confirm the completion of a corporate action undertaken by the Sender on behalf of the Reciever</td></tr><tr><td>Confirmative</td><td>563</td><td>Confirm the final execution advising the Receiver of the status of a corporate action transaction</td></tr><tr><td>Descriptive</td><td>510</td><td>Provide a detailed accounting of securities purchased by the sender</td></tr><tr><td>Descriptive</td><td>531</td><td>Include the itemised accounting details of the receipt of specified securities</td></tr><tr><td>Descriptive</td><td>533</td><td>Include the itemised accounting details of the delivery of specified securities</td></tr></table>

Table 6 continuedŽ .

<table><tr><td>Illocutionary force</td><td>Message ID</td><td>Verb phrase</td></tr><tr><td>Descriptive</td><td>550</td><td>Provide details of a formal notice of rights to a current or future debt subscription</td></tr><tr><td>Descriptive</td><td>552</td><td>Describe an offer by a third party in respect of a specified security</td></tr><tr><td>Descriptive</td><td>571</td><td>List the quantity and identification of securities held by the sender for the receiver on a particular date</td></tr><tr><td>Descriptive</td><td>573</td><td>Provide details of transactions received but not yet effected</td></tr><tr><td>Descriptive</td><td>583</td><td>Provide details on one transaction or event</td></tr><tr><td>Informative</td><td>526</td><td>List securities available for lending</td></tr><tr><td>Informative</td><td>526</td><td>List securities no longer available for lending</td></tr><tr><td>Informative</td><td>526</td><td>Notify the return of securities borrowed</td></tr><tr><td>Informative</td><td>534</td><td>Advise the Receiver of a problem</td></tr><tr><td>Informative</td><td>539</td><td>Inform that the receiver appears not to have been credited so far</td></tr><tr><td>Informative</td><td>539</td><td>Inform that the Beneficiary is unable to identify the transaction</td></tr><tr><td>Informative</td><td>539</td><td>Inform that the account the sender indicated is not held by the receiver</td></tr><tr><td>Informative</td><td>539</td><td>Inform that the account the sender indicated is held with us under another title</td></tr><tr><td>Informative</td><td>560</td><td>Specify particular matters of the meetings</td></tr><tr><td>Informative</td><td>562</td><td>Acknowledge the receipt of a corporate action instruction</td></tr><tr><td>Informative</td><td>572</td><td>Inform that the securities listed have been loaned out</td></tr><tr><td>Informative</td><td>573</td><td>Inform that securities are not deliverable as they are pledged as collateral</td></tr><tr><td>Informative</td><td>574</td><td>Identifies orders to buy or to sell which have been accepted but which have not yet been executed</td></tr><tr><td>Informative</td><td>577</td><td>Provide certificate numbers of securities</td></tr><tr><td>Informative</td><td>579</td><td>Replace or supplement the &quot;certificate numbers&quot; field in another message</td></tr><tr><td>Informative</td><td>580</td><td>Report information on the receipt of securities including the cancellation of such a transaction</td></tr><tr><td>Informative</td><td>581</td><td>Notify of a change in the amount of collateral held</td></tr><tr><td>Predictive</td><td>554</td><td>Advise the receiver of an event related to cash income that will take place</td></tr><tr><td>Predictive</td><td>555</td><td>Advise the receiver of an event related to income in the form of additional securities that will take place</td></tr><tr><td>Predictive</td><td>556</td><td>Provide notice of a forthcoming redemption</td></tr><tr><td>Predictive</td><td>582</td><td>advise that funds will be remitted by the sender</td></tr><tr><td>Requestive</td><td>526</td><td>Request the potential Lender to hold securities</td></tr><tr><td>Requestive</td><td>526</td><td>Request the borrowing of securities</td></tr><tr><td>Requestive</td><td>526</td><td>Request the potential Borrower to confirm a securities loan</td></tr><tr><td>Requestive</td><td>539</td><td>Request to please send the particulars of a transaction</td></tr><tr><td>Requestive</td><td>539</td><td>Request to investigate a discrepancy and instruct the sender accordingly</td></tr><tr><td>Requestive</td><td>539</td><td>Request to authorize the sender to debit the recipient&#x27;s account</td></tr><tr><td>Requestive</td><td>559</td><td>Specifies any questions concerning the claim for payment or reimbursement</td></tr><tr><td>Requestive</td><td>560</td><td>Request the receiver to inform its bond customers about a meeting</td></tr><tr><td>Requestive</td><td>560</td><td>Invite shareholders to give proxies</td></tr><tr><td>Requestive</td><td>570</td><td>Request for a statement concerning securities</td></tr><tr><td>Requirement</td><td>500</td><td>Instruct the receiver to buy a specified quantity of the identified security</td></tr><tr><td>Requirement</td><td>501</td><td>Instruct the receiver to sell a specified quantity of the identified security</td></tr><tr><td>Requirement</td><td>520</td><td>Instruct the receiver to receive securities</td></tr><tr><td>Requirement</td><td>521</td><td>Instruct the receiver to receive securities</td></tr><tr><td>Requirement</td><td>522</td><td>Instruct the receiver to deliver securities</td></tr><tr><td>Requirement</td><td>523</td><td>Instruct the receiver to deliver securities</td></tr><tr><td>Requirement</td><td>553</td><td>Instruct the custodian as to any required action</td></tr><tr><td>Requirement</td><td>559</td><td>Claim reimbursement of income or redemption proceeds</td></tr><tr><td>Requirement</td><td>559</td><td>Claim for payment of the principal paying agent&#x27;s fees and expenses</td></tr><tr><td>Requirement</td><td>561</td><td>Give voting instructions</td></tr><tr><td>Requirement</td><td>573</td><td>Instruction from your counterparty with settlement date later than statement date</td></tr><tr><td>Requirement</td><td>580</td><td>Instruct an International Clearing System to receive securities</td></tr><tr><td>Requirement</td><td>581</td><td>Claim an increase or decrease to the collateral amount</td></tr><tr><td>Requirement</td><td>582</td><td>Claim reimbursement of funds paid on behalf of the receiver</td></tr><tr><td>Retrodictive</td><td>510</td><td>Convey the payment details of the purchase that has occurred</td></tr><tr><td>Retrodictive</td><td>519</td><td>Report brief information about a securities deal that has been executed</td></tr></table>

Table 6 continuedŽ .

<table><tr><td>Illocutionary force</td><td>Message ID</td><td>Verb phrase</td></tr><tr><td>Retrodictive</td><td>526</td><td>Notifies the return of securities previously out on loan</td></tr><tr><td>Retrodictive</td><td>539</td><td>Provide information of a receipt or delivery of securities</td></tr><tr><td>Retrodictive</td><td>551</td><td>Provide particulars of an event affecting a security, including an early notice of rights, a notice of money income or of income in the form of securities declared but not yet booked</td></tr><tr><td>Retrodictive</td><td>554</td><td>Advise the receiver of an event related to cash income that has taken place</td></tr><tr><td>Retrodictive</td><td>555</td><td>Advise the receiver of an event related to income in the form of additional securities that has taken place</td></tr><tr><td>Retrodictive</td><td>556</td><td>Advise of the money amount of the completed redemption</td></tr><tr><td>Retrodictive</td><td>557</td><td>Provide advise of details and disposition of the proceeds following a presentation of coupons</td></tr><tr><td>Retrodictive</td><td>562</td><td>Advise a change in the status of an action previously instructed by or executed on behalf of the receiver</td></tr><tr><td>Retrodictive</td><td>572</td><td>Provide the details of all changes in holdings which occurred during a specified period</td></tr><tr><td>Retrodictive</td><td>582</td><td>Advise that funds have been remitted by the sender</td></tr><tr><td>Retrodictive</td><td>583</td><td>Advise a change in the status for good delivery</td></tr><tr><td></td><td></td><td>Apple Event messages</td></tr><tr><td>Question</td><td>DoObjects-Exist</td><td>Ask if a set of objects exists</td></tr><tr><td>Requestive</td><td>OpenApplication</td><td>request to perform any tasks that your application would perform when a user launches the application</td></tr><tr><td>Requestive</td><td>OpenDocuments</td><td>Request to open specified documents</td></tr><tr><td>Requestive</td><td>PrintDocuments</td><td>Request to print specified documents</td></tr><tr><td>Requestive</td><td>QuitApplication (required)</td><td>Request to perform any tasks that your application would perform when a user chooses Quit from the File menu</td></tr><tr><td>Requestive</td><td>Clone</td><td>Request to create a clone of a set of objects</td></tr><tr><td>Requestive</td><td>Close (core)</td><td>Request to close a set of objects</td></tr><tr><td>Requestive</td><td>CountElements</td><td>Ask for the number of elements of a particular object class in each object in a set of objects</td></tr><tr><td>Requestive</td><td>CreateElement</td><td>Request to create a new element</td></tr><tr><td>Requestive</td><td>Delete</td><td>Request to delete one or moRe elements</td></tr><tr><td>Requestive</td><td>GetClassInfo</td><td>Request information about the properties and elements of an object class</td></tr><tr><td>Requestive</td><td>GetData</td><td>Request the data for a set of objects</td></tr><tr><td>Requestive</td><td>GetDataSize</td><td>Request the sizes, in bytes, of the data for a set of objects</td></tr><tr><td>Requestive</td><td>GetEventInfo</td><td>Request information about the Apple events in a suite</td></tr><tr><td>Requestive</td><td>Move (core)</td><td>Request to move a set of objects</td></tr><tr><td>Requestive</td><td>Open</td><td>Request to open a set of objects</td></tr><tr><td>Requestive</td><td>Print</td><td>Request to print a set of objects</td></tr><tr><td>Requestive</td><td>QuitApplication (core)</td><td>Request to perform any tasks that your application would perform when the user chooses Quit from the File menu</td></tr><tr><td>Requestive</td><td>Save</td><td>Request to save a set of objects</td></tr><tr><td>Requestive</td><td>SetData</td><td>Request to set the data of a set of objects to a particular value</td></tr><tr><td>Requestive</td><td>About</td><td>Ask the Finder to display the About This Macintosh window</td></tr><tr><td>Requestive</td><td>Close (Finder)</td><td>Ask the Finder to close one of its windows</td></tr><tr><td>Requestive</td><td>Drag</td><td>Ask the Finder to move copies of one or more icons in the same folder to a new folder</td></tr><tr><td>Requestive</td><td>Duplicate-Selection</td><td>Ask the Finder to duplicate one or more icons in the same folder</td></tr><tr><td>Requestive</td><td>EmptyTrash</td><td>Ask the Finder to empty the Trash</td></tr><tr><td>Requestive</td><td>GetInfo-Selection</td><td>Ask the Finder to display Info windows for one or more icons in the same folder</td></tr><tr><td>Requestive</td><td>AliasSelection</td><td>Ask the Finder to create aliases for one or more icons in the same folder</td></tr><tr><td>Requestive</td><td>Move (Finder)</td><td>Ask the Finder to move one or more icons to a new folder</td></tr><tr><td>Requestive</td><td>SetPosition</td><td>Ask the Finder to move one of its windows to a specified location</td></tr></table>

Table 6 continuedŽ .

<table><tr><td>Illocutionary force</td><td>Message ID</td><td>Verb phrase</td></tr><tr><td>Requestive</td><td>Open-Selection</td><td>Ask the Finder to open one or more icons in the same folder</td></tr><tr><td>Requestive</td><td>PageSetup</td><td>Ask the Finder to display the Page Setup window for a specified Finder window</td></tr><tr><td>Requestive</td><td>PrintSelection</td><td>Ask the Finder to print the contents of one or more documents</td></tr><tr><td>Requestive</td><td>PrintWindow</td><td>Ask the Finder to print the contents of one of its windows</td></tr><tr><td>Requestive</td><td>PutAway-Selection</td><td>Ask the Finder to put one or more icons back into the folders from which they were last moved</td></tr><tr><td>Requestive</td><td>Grow</td><td>Ask the Finder to set the size of a Finder window</td></tr><tr><td>Requestive</td><td>Restart</td><td>Ask the Finder to terminate all open applications and restart the computer</td></tr><tr><td>Requestive</td><td>Reveal</td><td>Ask the Finder to display the window for the folder that contains specified icons</td></tr><tr><td>Requestive</td><td>Reveal</td><td>Ask the Finder to select specified icons</td></tr><tr><td>Requestive</td><td>ChangeView</td><td>Specify what view of a folder window&#x27;s contents the Finder should display</td></tr><tr><td>Requestive</td><td>GetPrivilege-Selection</td><td>Ask the Finder to display Sharing windows for one or more icons in the same folder</td></tr><tr><td>Requestive</td><td>Show-Clipboard</td><td>Ask the Finder to display the Clipboard window</td></tr><tr><td>Requestive</td><td>Shutdown</td><td>Ask the Finder to terminate all open applications in preparation for turning off the power</td></tr><tr><td>Requestive</td><td>Sleep</td><td>Put a portable computer into its power-conserving state</td></tr><tr><td>Requestive</td><td>Zoom</td><td>Ask the Finder either to make a Finder window larger or smaller</td></tr><tr><td>Requestive</td><td>Begin-Transaction</td><td>Request to begin a transaction and return a transaction ID</td></tr><tr><td>Requestive</td><td>Copy</td><td>Request to copy the objects in the current user selection and put them on the Clipboard</td></tr><tr><td>Requestive</td><td>Create-Publisher</td><td>Request to create an Edition Manager publisher</td></tr><tr><td>Requestive</td><td>Cut</td><td>Request to remove the set of objects in the current user selection and put them on the Clipboard</td></tr><tr><td>Requestive</td><td>DoScript</td><td>Ask an application that understands a scripting language to perform the actions specified in a script</td></tr><tr><td>Requestive</td><td>EditGraphic</td><td>Request to let the user edit a graphic</td></tr><tr><td>Requestive</td><td>ImageGraphic</td><td>Request to convert a graphic from one format to another and/or to enhance it</td></tr><tr><td>Requestive</td><td>IsUniform</td><td>Request for information about a set of objects</td></tr><tr><td>Requestive</td><td>MakeObjects-Visible</td><td>Ask an application to bring a set of objects into view within one of the application&#x27;s windows</td></tr><tr><td>Requestive</td><td>Paste</td><td>Request to make a copy of the objects on the Clipboard and either have them replace the current user selection or move them to the current insertion point</td></tr><tr><td>Requestive</td><td>Redo</td><td>Request to reverse the action of the undo operation that immediately preceded the Redo Apple event</td></tr><tr><td>Requestive</td><td>Revert</td><td>Request to replace a set of objects with the versions of the object that were most recently saved</td></tr><tr><td>Requestive</td><td>Undo</td><td>Request to undo the result of the immediately preceding Apple event or user</td></tr><tr><td>Retrodictive</td><td>Application-Died</td><td>Notify that an application launched by your application has terminated action</td></tr><tr><td>Retrodictive</td><td>EndTransaction</td><td>Inform an application that an Apple event transaction is complete</td></tr><tr><td>Retrodictive</td><td>Transaction-Terminated</td><td>Inform an application that a transaction in progress has been terminated</td></tr><tr><td></td><td></td><td>Apple Event reply messages</td></tr><tr><td>Descriptive</td><td>GetClassInfo</td><td>Inform about the properties and element classes of the object class</td></tr><tr><td>Descriptive</td><td>GetDataSize</td><td>A list of descriptor records specifying the size, in bytes, of a specified object</td></tr><tr><td>Descriptive</td><td>GetEventInfo</td><td>A list containing descriptor information about Apple events</td></tr><tr><td>Informative</td><td>Count-Elements</td><td>Specify the number of elements of the specified class in a particular object</td></tr><tr><td>Informative</td><td>DoObjects-Exist</td><td>Specify whether or not all of the objects exist</td></tr><tr><td>Informative</td><td>Move</td><td>Specify the object that has been moved</td></tr><tr><td>Informative</td><td>Begin-Transaction</td><td>The transaction ID</td></tr><tr><td>Informative</td><td>IsUniform</td><td>Indicates whether all the objects in the set have the same value for the specified property</td></tr><tr><td>Retrodictive</td><td>Clone</td><td>Specify the object or objects that have been cloned</td></tr></table>

Table 7  
Mapping information for Apple events

<table><tr><td>Illocutionary force</td><td>Inside request</td><td>Apple events</td></tr><tr><td>Descriptive</td><td>1</td><td>GetClassInfo</td></tr><tr><td>Informatives</td><td>5</td><td>CountElements, GetDataSize, GetEventInfo, BeginTransaction, IsUniform</td></tr><tr><td>Permissives</td><td>1</td><td>EditGraphic</td></tr><tr><td>Retractives</td><td>1</td><td>Undo</td></tr></table>

Looking at the forces in Fig. 2 that are not in Table 7 highlights that there are many forces which did not have any messages mapped onto them. An implication which might be drawn is that these forces are somehow ill-defined, ill-conceived, or somehow faulty. This should not be concluded for at least two reasons. First, the sample is too small to conclude no messages fit into these categories. Messages from other standards might map onto these forces. Second, these are simple electronic messaging systems whose expressive power and purpose are limited. Many normal language expressions would fit into these categories. These systems developed under the restriction of their highly limited languages. Given this limitation it would have been surprising to see a wide variety of messages spanning the F PŽ . hierarchy. Instead, what was observed was a limited set of expressions that are needed for the systems to function. A more powerful messaging system would encourage the use of a wider range of expressions.

## 6.3. How much the standards segment the hierarchy

As shown in Table 6, there was significant overlap between standards. With these three standards, descriptive, informatives, requestives, and requirements account for a high percentage of the messages. For the two EDI systems, adding in the predictives and retrodictives accounts for another large portion of the messages. Further, only one force question Ž . was used by either SWIFT or AE and not used by UN-EDIFACT. Clearly, these standards did not segment the illocutionary force hierarchy.

## 7. Discussion

## 7.1. Implications

The results of this study paint an interesting picture. The message structure implicit in three separate electronic communication standards all map onto the F PŽ . framework proposed by SAT. These standards were not defined with SAT in mind, nor was SAT defined with electronic communication in mind. It is hard to think of a reason that the mapping should have been successful, except for the possibility that this framework or something like it is correct.Ž . These three standards were a convenient sample, but there is no reason to think other standards would present a significantly different result. This is evidence in favor of SAT.

Not only is SAT supported, but the researchers who have proposed that SAT be used as the basis for electronic communication systems are also supported ŽAuramaki et al. 3 , Kimbrough and Moore 17 ,¨ <sup>w x</sup> <sup>w</sup> <sup>x</sup> Lehtinen and Lyytinen 22 , Mora et al. 25 , Wino-<sup>w x</sup> <sup>w x</sup> grad and Flores 41 , Woo 42 , Woo and Chang <sup>w x</sup> <sup>w x</sup> <sup>w</sup> <sup>x</sup> 43 . This study does not indicate the ultimate cor- . rectness or utility of SAT. It does indicate that it is feasible to construct electronic messages within this SAT framework.

It is feasible and also preferable. Previous researchers have demonstrated the benefits of explicitly representing the illocutionary force in electronic messages e.g., Kimbrough and Moore 17,29 , Med-Ž <sup>w</sup> <sup>x</sup> ina-Mora et al. 25 Winograd and Flores 41 , Woo <sup>w x</sup> <sup>w x</sup> <sup>w</sup> <sup>x</sup> 42 . These benefits include better message han-. dling, reusability of message handlers, better message retrieval, clearer message definitions, and the ability to automate more complex tasks.

## 7.1.1. Better message handling

For example, consider the following simple example. Suppose the illocutionary force is added to a message’s header. This gives programs receiving the message more information with which to determine how to handle it. It might have a rule defined to put aside anything but a requestive. Because the force is easily available for inferencing, the system can do more with the message than it could do without it.

Certainly, more can be done with the force than simply putting it in the header. Moore and Kimbrough have proposed 17 , defined 16,27 , and <sup>w x</sup> <sup>w</sup> <sup>x</sup> demonstrated 29 a formal language for business <sup>w</sup> <sup>x</sup> communication FLBC . This language allows fully Ž . formal messages to be composed and interpreted with few limits on the contents of the messages. <sup>2</sup>

```txt
Am I familiar with the organization asking this question?
If yes, then:
    Do I know what they're asking?
    If yes, then
    Are there any restrictions on this information?
    If yes, then:
    Does this company pass these restrictions?
    If yes, then:
    Process this request.
    Otherwise:
    Tell them the answer is not available.
    Otherwise:
    Process this request.
    Otherwise:
    Tell them I do not understand the question.
Otherwise:
Tell them to describe themselves more fully.
```  
Fig. 6. Outline of a possible message handler for a requestive.

## 7.1.2. Reusability of message handlers

A message handler is a piece of a computer program that handles a certain type of message. With an EDI system based on an illocutionary force framework, the basic set of message handlers would include one for each force. The requestive handler might have a logical form similar to that in Fig. 6. <sup>3</sup> Defining one handler for all requestives or as-Ž sertives, etc. is possible because the distinguishing. characteristic of a requestive or assertive, etc. isŽ . how it is understood. Writing some code that will handle i.e., understandŽ . all requests having to do with a business sounds like an impossible task but is not. Separating the illocutionary force from the perlocutionary effect makes it possible. I propose that the speaker’s communicative intention i.e., illocu-Ž tionary point can be understood for all requestives. using the same, relatively small, section of code, but most messages will need additional code to handle differing perlocutionary effects.

What does this all mean? Suppose that a company’s EDI system knows about 20 business objects Ž . e.g., purchase orders . Further, it must handle requests about the status of each, about when they Ž were processed, etc. and be able to accept new . descriptives and informatives about each. With current methods, this would require at least 60 separate message sets, field definitions, and handlers. Under my proposal, this company would write three message handlers. If any further processing were necessary for any particular requestive or descriptive,Ž etc. to handle the perlocutionary effect of the mes-. sage, then up to 60 pieces of code would have to be written, although it is my experience in developing prototypes that this number will be much smaller. However, even if there are 60 pieces of code that have to be written, they will be much simpler than required using current techniques because much of the processing is already included in the handler for its illocutionary force e.g., Fig. 6 . In short, integrat-Ž . ing SAT into an EDI system should significantly increase the reusability of message handlers, making deployment of additional messages more cost-effective.

## 7.1.3. Better message retrieÕal

Explicitly representing the illocutionary force improves retrieval via the same mechanism that improves message handling. The retrieval system is given more information than it was previously. This allows the system to construct more precise queries than it could have without the information.

## 7.1.4. Clearer message definitions

As discussed in Section 5, much of the difficulty of mapping arises because the messages are being mapped after they have been defined. An alternative is to use the hierarchy to guide the message definition process more will be said on this below . InŽ . short, since the definitions would rely only on known building blocks i.e., the illocutionary forces insteadŽ . of ambiguous natural language, they would haÕe to be clearer than they are now.

## 7.1.5. Automate more complex tasks

Since more types of messages could be automated more easily than is possible now, more tasks would be automated. The inferencing required for responding to these messages is also more complex than was previously needed Kimbrough and Moore 18 . Ž <sup>w</sup> <sup>x</sup>. Thus, a greater number of more complex tasks could be automated than was possible without the force.

Thus, the benefits that would accrue to business would be many if the findings of this paper, or something like them, were true.

![](/api/attachments/GHBDTEGV/fulltext/images/fb35d974860a65b1200c00fcd5a575b01314325a8c06a55b7f895fa49e3f67ad.jpg)  
Fig. 7. Changing the conversation structure.

The larger point here related to EDI is how to define a message set so that its meaning is evident, unambiguous, and automatically inspectable. <sup>4</sup> Each of these attributes would simplify the creation of EDI systems while simultaneously making them more powerful see below and more widespread. OfŽ . course, I propose that SAT is part of the solution— SAT imposes a discipline on the message definition process that provides several benefits and contributes to the above goals. First, since a message’s meaning is partially defined by its force, a message from one message set should not be able to have one of several different illocutionary forces. Each message set should have only one illocutionary force, and that force should be explicitly represented. If a message expressing another force were needed, then a new message set should be defined. This would make it easier to interpret and locate messages that have a specified force.

For example, in Fig. 7 1 company A uses oneŽ . version of UN-EDIFACT message SSREGW to advise company B that a social security number has been allocated to someone. Company B replies with another version of SSREGW that both informs company A that it understands the original message, and that confirms the SSN that has been allocated. The illocutionary force of the first message is retrodictive, while the second message carries both informative and confirmative forces. The logical structure of the conversation is shown in Fig. 7 2 . My point here Ž . is that if this is what actually occurs, then the message flow should reflect it. Why should not company B be able to tell company A that it received the message without, at the same time, confirming the allocated number?

Second, applying SAT unambiguously acknowledges that EDI does not simply involve sending forms back and forth. These organizations are conversing within the context of some business process in which they hope to accomplish some work. Since this is the case, why not use a conversational structure that we know a bit about i.e., natural languageŽ . to represent the expected conversational structure? Moore 28 outlined the basic steps for using Petri nets to represent conversational structure based on illocutionary forces and, more generally, SAT and other linguistic theories. Statecharts 12 could be<sup>w</sup> <sup>x</sup> used for the same purpose. Lee 21 used Petri nets <sup>w</sup> <sup>x</sup> to represent bureaucratic systems. These authors demonstrated that computer-processable and inspectable representations can be used to represent conversational structure and business processes. Using these representations, a company could define its standard business process for handling a purchase order. This could define, in a computer-processable and inspectable language, the messages it expects to be sent during the completion of this task, and the order in which it expects them to be sent. When the company gains a new business partner, it could send the relevant business processes to the partner so that the EDI systems of both companies would understand the processing necessary for a purchase order. A predicate logic representation of Fig. 7 2 couldŽ . easily be developed and included in the definition of SSREGW to show the expected conversational structure when a SSN is allocated.

Third, and related to the previous point, SAT requires that a message’s intended meaning be separated from the eventual effect on its recipient. This clarifies what the message definition should and should not include. Since the message definition is analogous to something like Fig. 7 2 , and since theŽ . people defining the message know the intended effect of each illocutionary force see Appendix A , Ž . they do not have to include in the definition of the message that, e.g., company B is expected to believe that the SSN was allocated by company A. The message recipient gains this expectation, and others like it, through inferences included in the handler for the illocutionary force.

Fourth, applying SAT and using the F PŽ . framework allows natural representation of iterated illocutionary forces. Previous researchers have claimed that iterated forces occur naturally within messages ŽKimbrough and Lee 15 , Kimbrough and Moore<sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> 17 , Kimbrough and Thornburg 20 . This study .

found a significant example of iterated operators in the Apple Events messages. If this were a general finding, then it would be a compelling reason to use a formal language for communication that could explicitly and naturally represent this information.Ž .

In short, the definition of message sets will change under this message processing regime. Messages are already defined by the set of illocutionary forces. Conversational structures that define the expected course of events for accomplishing certain goals would be defined. This ‘expected course of events’ Ž . i.e., the conversational structure would include the expected order of messages and their illocutionary forces as in Fig. 7 2 . The task of standard bodiesŽ Ž .. would change to defining both these conversational structures and the vocabulary that is needed to carry them out. The result should be that 1 it is easier toŽ . express new types of messages something that cur- Ž rently involves creating a new message set , and 2 . Ž . more types of messages can be expressed in an automated EDI message and not have to be handled manually or in a free-text EDI message. Both should allow more to be said electronically, so that EDI could become a part of more processes.

Certainly, the marginal cost of handling an electronic message is smaller than that for handling a telephone call or reading a free text EDI message. The technology proposed here results in both automation of more types of electronic messages and reduction in development costs. This should have two results. First, a firm should see more competition for its electronic business e.g., both in elec-Ž tronic markets and suppliers or customers that use EDI . Second, since the amount of customer-specific. technology has also been reduced, switching costs should be reduced. Thus, economic relationships will be more fluid and extensive. This is a broad agreement with Kimbrough and Moore’s argument for more powerful systems for electronic commerce 17 .<sup>w</sup> <sup>x</sup>

All the above benefits can only be realized if there is a common set of illocutionary forces across all messages that is infrequently extended. If no common set exists, then for every set of messages, new message handling and retrieving mechanisms would have to be constructed. Further, automation of tasks would be much more difficult because new inferencing mechanisms for understanding messages would have to be built for each new message type.

This brings us back to today’s technologies EDI etŽ al. . This investigation provides some evidence that. there is such a common set.

Even if there were a common set of illocutionary forces, if we could not map messages onto these forces reliably or consistently, then we would not be able to represent the illocutionary force in the message. This would have the same unfortunate effects as described above. To summarize the above points: if messages could be mapped onto the F PŽ . framework, and if this framework were correct, then many benefits could be realized. The purpose of this investigation is to indicate the first supposition is correct and provide a bit of evidence for the second. It is left to other papers as referenced above to explore the Ž . benefits.

## 8. Future research

Though this study indicates answers to some questions, many more questions remain about the utility of applying SAT to electronic communication systems. Clearly, the F PŽ . framework may help a system understand a message but is neither necessary nor sufficient for doing so. There are not just 26 orŽ any finite X . number of messages. A request to paint the house is different from a request to buy 200 gallons of paint. Both would be represented as requestives in the F PŽ . framework. A message’s content and context—i.e., that information contained in the P—must be represented to allow systems to process the message. Defining a general system for representing this information would contribute to the utility of a SAT-based message system.

Another research area concerns the typology of inquiries. The Bach and Harnish categorization forces all inquiries into two illocutionary forces: requestives and questions. Questions require a yes or no response. Requestives are all other types of inquiries. As was shown in Table 6, systems can request to inform, retract, permit, or describe. The Bach and Harnish hierarchy draws no distinction between these types of requestives but separates a yes-or-no question from the requestive. This seems to be somewhat arbitrary. Researchers need to determine what types of questions they want to ask. Great disagreement in the philosophy literature exists as to what types of questions can be asked e.g., Ref. 13 . ResearchersŽ <sup>w</sup> <sup>x</sup>. should then determine if an addition to the hierarchy is needed to handle these new types, or if it is correct and useful the way it stands.

In addition to this simple question about the Bach and Harnish hierarchy, there is the question of whether or not there is a better hierarchy. One good place to start investigating this question is to map these message standards and others to this hierar-Ž . chy and alternatives. This process can reveal whether the mapping can be done and can also reveal weaknesses or strengths of each hierarchy as we saw inŽ this study ..

A more fundamental question is whether or not SAT is correct. It may be the case that people do not communicate in the manner described by speech act theorists. This line of research will not prove that SAT is correct, but it could provide some support for the contention that it is correct or incorrect. If a robust, expressive, and powerful communication system can be built based on SAT, then supporters of SAT would have strong evidence that it is correct. On the other hand, if no such system can be built, then supporters of SAT would have to explain the failure. Currently, however, SAT represents the best work of linguists and philosophers of language describing how people communicate. The study described here represents one effort that takes this finding seriously. Much effort remains before we are finished.

Finally, it is difficult to define what it means to say ‘‘SAT is correct’’ or that ‘‘this hierarchy is correct’’. One possibility is that it means there are no alternative ways to think about language that provide more insight than this way. If that is how the statements should be interpreted, then I think that, ultimately, it might better serve the SAT researcher and practitioner to substitute the word useful for correct in the above two statements. It is the utility of SAT and a corresponding hierarchy that we are interested in. Certainly, researchers should pursue answers to the two questions as phrased above. Happily, answering the two ‘utility’ questions should provide insight into the two ‘correct’ questions. Certainly, relevant research questions concern defining a SAT hierarchy and determining how businesses might become more efficient and effective by using a messaging system based on it.

## Appendix A. Formal definitions of illocutionary forces

The following are definitions of the illocutionary forces classified as constatiÕes, directiÕes,or commissiÕes on pages 42–55 of 5<sup>w</sup> <sup>x</sup>

Adzisory Ž . admonish, advise, caution, counsel, propose, recommend, suggest, urge, warn In uttering e, S advises H to A if S expresses:

1. The belief that there is sufficient reason forŽ . H to A, and

2. The intention that H take S’s belief as sufficient reason for him to A.Ž .

Ascriptize Ž . ascribe, attribute, predicate In uttering e, S ascribes F to o if S expresses:

1. The belief that F applies to o, and

2. the intention that H believe that F applies to o.

Assentize Ž . accept, agree, assent, concur In uttering e, S assents to the claim that P is S expresses:

1. The belief that P, as claimed by H Ž .or as otherwise under discussion , and

2. The intention perhaps already fulfilled thatŽ . H believe that P.

Assertize Ž Ž . affirm, allege, assert, aver, avow, claim, declare, deny assert . . . not , indicate, maintain, Propound, say, state, submit In uttering e,. S asserts that C if S expresses:

1. The belief that C, and

2. The intention that H believe that C.

Concessize Ž . acknowledge, admit, agree, allow, assent, concede, concur, confess, grant, own In uttering e, S concedes that P if S expresses:

1. The belief that P, contrary to what he would like to believe or contrary to what he previously believed or avowed, and

2. The intention that H believe that P.

Confirmatize Žappraise, assess, bear witness, certify, conclude, confirm, corroborate, diagnose, find, judge, substantiate, testify, validate, verify, vouch for In uttering e, . Ž . S confirms the claim that C if S expresses:

1. The belief that C, based on some truth-seeking procedure, and

2. The intention that H believe that C because S has some support for P.

Descriptize Žappraise, assess, call, categorize, characterize, classify, date, describe, diagnose, evaluate, grade, identify, portray, rank In uttering e,. S describes o as F if S expresses:

1. The belief that o is F, and

2. The intention that H believe that o is F.

Disputatize Ž . demur, dispute, object, protest, question In uttering e, S disputes the claim that P if S expresses: 1. The belief that there is reason not to believe that P, contrary to what was claimed by H Žor was otherwise under discussion , and.

2. The intention that H believe that there is reason not to believe that P.

Dissentize Ž . differ, disagree, dissent, reject In uttering e, S dissents from the claim that P if S expresses:

1. The disbelief that P, contrary to what was claimed by H Ž . or was otherwise under discussion , and

2. The intention that H disbelieve that P.

Informatize Žadvise, announce, apprise, disclose, inform, insist, notify, point out, report, reveal, tell, testify. In uttering e, S informs H that C if S expresses:

1. The belief that C, and

2. The intention that H form the belief that C.

Offer Ž . offer, propose; also volunteer, bid In uttering e, S offers A to H if S expresses:

1. The belief that S’s utterance obligates him to A on condition that H indicates he wants S to A,

2. The intention to A on condition that H indicates he wants S to A, and

3. The intention that H believe that S’s utterance obligates S to A and that S intends to A, on condition that H indicates he wants S to A.

Permissize Žagree to, allow, authorize, bless, consent to, dismiss, excuse, exempt, forgive, grant, license, pardon, release, sanction In uttering e,. S permits H to A if S expresses:

1. The belief that his utterance, in virtue of his authority over H, entitles H to A, and

2. The intention that H believe that S’s utterance entitles him to A.

Predictize Ž . forecast, predict, prophesy In uttering e, S predicts that C if S expresses:

1. The belief that it will be the case that C, and

2. The intention that H believe that it will be the case that C.

Prohibitize Ž . enjoin, forbid, prohibit, proscribe, restrict In uttering e, S prohibits H from A-ing if S expresses:

1. The belief that his utterance, in virtue of his authority over H, constitutes sufficient reason for H not to A, and

2. The intention that because of S’s utterance H not do A.

Promise Žpromise, swear, vow; also contract, bet, swear that, guarantee that, guarantee x, surrender, invite. In uttering e, S promises H to A if S expresses:

1. The belief that his utterance obligates him to A,

2. The intention to A, and

3. The intention that H believe that S’s utterance obligates S to A and that S intends to A.

## Question Ž . ask, inquire, interrogate, query, question, quiz In uttering e, S questions H as to whether or not C if S expresses:

1. The desire that H tell S whether or not P, and

2. The intention that H tell S whether or not C because of S’s desire.

## Requestize Žask, beg, beseech, implore, insist, invite, petition, plead, pray, request, solicit, summon, supplicate, tell, urge In uttering e, . S requests H to A if S expresses:

1. The desire that H do A, and

2. The intention that H do A because at least partly of Ž . S’s desire.

## Requirement Žbid, charge, command, demand, dictate, direct, enjoin, instruct, order, prescribe, require. In uttering e, S requires H to A if S expresses:

1. The belief that his utterance, in virtue of his authority over H, constitutes sufficient reason for H to A.

2. The intention that H do A because of S’s utterance.

Retractize Žabjure, correct, deny, disavow, disclaim, disown, recant, renounce, repudiate, retract, take back, withdraw In uttering e,. S retracts the claim that C if S expresses:

1. That he no longer believes that C, contrary to what he previously indicated he believed, and

2. The intention that H not believe that C.

Retrodictize Ž . recount, report In uttering e, S retrodicts that P if S expresses:

1. The belief that it was the case that P, and

2. The intention that H believe that it was the case that P.

Suggestize Ž . conjecture, guess, hypothesize, speculate, suggests In uttering e, S suggests that P if S expresses:

1. The belief that there is reason, but not sufficient reason, to believe that P, and

2. The intention that H believe that there is reason, but not sufficient reason, to believe that P.

Suppositize Ž . assume, hypothesize, postulate, stipulate, suppose, theorize In uttering e, S supposes that P if S expresses

1. The belief that it is worth considering the consequences of P, and

2. The intention that H believe that it is worth considering the consequences of P.

## Acknowledgements

Thanks to Premenos www.premenos.com forŽ . maintaining such an outstanding EDI Web site. Thanks to Chuck Wiley of SWIFCO US for pro-Ž . viding information about the SWIFT standards. Also, thanks to Steve Kimbrough for his encouragement and guidance with this paper. I can be reached at samoore@umich.edu; my web site is wwwpersonal.umich.edu<sup>r;</sup>samoore<sup>r</sup> Žfile: cat-edi.tex; a previous version of this paper appeared in the Proceedings of HICSS-29 ..

## References

<sup>w</sup> <sup>x</sup>1 American National Standards Institute, X12 Transaction Set Index Version 3040, http:<sup>rr</sup>www.premenos.com<sup>r</sup>standards<sup>r</sup>X12<sup>r</sup>index<sup>r</sup>setindex.html, accessed from August 13– 16, 1996.

<sup>w</sup> <sup>x</sup> 2 Apple Computer, Apple Event registry: Standard suites, http:<sup>rr</sup>dev2.info.apple.com<sup>r</sup>FTPIndices<sup>r</sup>App-3.html, downloaded on August 13, 1996.

<sup>w</sup> <sup>x</sup> 3 E. Auramaki, E. Lehtinen, K. Lyytinen, A speech-act-based ¨ office modeling approach, ACM Trans. Office Info. Syst. 6 Ž . Ž . 2 1988 126–152.

<sup>w</sup> <sup>x</sup> 4 J.L. Austin, How To Do Things With Words, 2nd edn. Harvard Univ. Press, 1975.

<sup>w</sup> <sup>x</sup> 5 K. Bach, R.M. Harnish, Linguistic Communication and Speech Acts, MIT Press, 1979.

<sup>w</sup> <sup>x</sup> 6 T. Ballmer, W. Brennenstuhl, Speech Act Classification, Springer, New York, 1981.

<sup>w</sup> <sup>x</sup> 7 P.R. Cohen, C.R. Perrault, Elements of a plan-based theory of speech acts, in: A.H. Bond, L. Gasser Eds. , Readings inŽ . Distributed Artificial Intelligence, Morgan Kaufman, 1988, pp. 169–186.

<sup>w</sup> <sup>x</sup> 8 T.D. Cook, D.T. Campbell, Quasi-Experimentation, Design and Analysis Issues for Field Settings, Houghton Mifflin, 1979.

<sup>w</sup> <sup>x</sup> 9 Microsoft Corporation, Help topic for Communicating with other applications, Help files distributed with Microsoft Excel 7 for WIndows 95, accessed in September, 1996.

<sup>w</sup> <sup>x</sup> 10 M. Corporation, Help topic for DDE dynamic data ex-Ž change , Help files distributed with Microsoft Word 7 for. Windows 95, accessed in September 1996.

<sup>w</sup> <sup>x</sup> 11 P. Grice, Logic and conversation, in: P. Grice Ed. , StudiesŽ . in the Way of Words, Harvard Univ. Press, 1989, pp. 22–40.

<sup>w</sup> <sup>x</sup> 12 D. Harel, Statecharts: a visual formalism for complex systems, Sci. Comp. Prog. 8 1987 231–274. Ž .

<sup>w</sup> <sup>x</sup> 13 D. Harrah, The logic of questions, in: D. Gabbay, F. Guenthner Ed. , Handbook of Philosophical Logic, Vol. II, D. Ž . Reidel Publishing, 1984, pp. 715–764.

<sup>w</sup> <sup>x</sup> 14 N. Jilovec, EDI standards offer a world of choice, Midrange Syst. 9 4 1996 26.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 S.O. Kombrough, R.M. Lee, On illocutionary logic as a telecommunications language, in: L. Maggi, et al. Ed. ,Ž . Proc. Seventh Int. Conf. on Information Systems, San Diego, CA, December 15–17 1986, pp. 15–26.

<sup>w</sup> <sup>x</sup> 16 S.O. Kimbrough, S.A. Moore, On automated message processing in electronic commerce and work support systems: speech act theory and expressive felicity. ACM Transactions on Information Systems 15 4 1997 321–367.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 S.O. Kimbrough, S.A. Moore, Message management systems: concepts, motivations and strategic effects, J. Manage. Info. Syst. 92 1992 29–52.Ž .

<sup>w</sup> <sup>x</sup> 18 S.O. Kimbrough, S.A. Moore, On obligation, time and defeasibility in systems for electronic commerce, in: J. Nunamaker, Jr., Ed. , Proc. Hawaii Int. Conf. on System Sci.,Ž . Vol. III, Univ. of Hawaii, IEEE Computer Society Press, 1993, pp. 493–502.

<sup>w</sup> <sup>x</sup> 19 S.O. Kombrough, S.A. Moore, M. Thornburg, On messaging with semantic access in an office environment, Working Papers Series, Univ. of Pennsylvania, Wharton School, Decision Sci. Department, December 1993.

<sup>w</sup> <sup>x</sup> 20 S.O. Kimbrough, M. Thornburg, On semantically-accessible messaging in an office environment, in: Proc. Twenty-Second Hawaii Int. Conf. on System Sci. Univ. of Hawaii, IEEE Computer Press, 1989.

<sup>w</sup> <sup>x</sup> 21 R.M. Lee, Bureaucracies as deontic systems, ACM Trans. Office Info. Syst. 6 2 1988 87–108.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 E. Lehtinen, K. Lyytinen, Action based model of information system, Info. Syst. 114 1986 299–317. Ž .

<sup>w</sup> <sup>x</sup> 23 D.J. Litman, J.F. Allen, A plan recognition model for subdialogues in conversations, Cognitive Sci. 11 1987 163–200.Ž .

<sup>w</sup> <sup>x</sup> 24 A. McCafferty, Speaker plans, linguistic contexts and indirect speech acts, in: H.E. Kyburg, Jr., R.P. Loui, G.N. Carlson, Eds. , Knowledge Representation and DefeasibleŽ . Reasoning, Kluwer Academic Publishers, 1990, pp. 191–220.

<sup>w</sup> <sup>x</sup> 25 R. Medina-Mora, T. Winograd, R. Flores, F. Flores, The action workflow approach to workflow management technology, in: J. Turner, R. Kraut Eds. , Proc. Conf. onŽ . Computer-Supported Cooperative Work, ACM SIGCHI and SIGOIS, ACM Press, 1992, pp. 281–288.

<sup>w</sup> <sup>x</sup> 26 Microsoft, Programmer’s Guide, Microsoft Visual Basic Programming System for Windows, 1993.

<sup>w</sup> <sup>x</sup> 27 S.A. Moore, Saying and Doing, Uses of Formal Languages in the Conduct of Business, PhD thesis, Univ. of Pennsylvania, Philadelphia, PA, December 1993.

<sup>w</sup> <sup>x</sup> 28 S.A. Moore, A communication framework for applications, in: J.F. Nunamaker, Jr., R.H. Sprague, Jr. Eds. , Proc. Ž . Hawaii Int. Conf. on System Sci., Vol. III, IEEE Computer Society Press, January 1995, pp. 330–341.

<sup>w</sup> <sup>x</sup>29 S.A. Moore, S.O. Kimbrough, Message management systems at work: prototypes for business communication, J. Org. Computing 52 1995 83–100.Ž .

<sup>w</sup> <sup>x</sup> 30 R. Nolan, Cognitive Practices, Human Language and Human Knowledge, Blackwell Publishers, Cambridge, MA, 1994.

<sup>w</sup> <sup>x</sup> 31 S. Scala, R. McGrath Jr., Advantages and disadvantages of electronic data interchange: an industry perspective, Info. Manage. 25 1993 85–91.Ž .

32 J.R. Searle, Speech Acts, An Essay in the Philosophy of Language, Cambridge Univ. Press, 1969.

<sup>w</sup> <sup>x</sup> 33 J.R. Searle, Expression and Meaning, Cambridge Univ. Press, Cambridge, England, 1979.

<sup>w</sup> <sup>x</sup> 34 J.R. Searle, A taxonomy of illocutionary acts, in: Expression and Meaning, Chap. 1, Cambridge Univ. Press, 1979, pp. 1–29.

<sup>w</sup> <sup>x</sup> 35 J.R. Searle, D. Vanderveken, Foundations of Illocutionary Logic, Cambridge Univ. Press, 1985.

<sup>w</sup> <sup>x</sup> 36 Society for Worldwide Interbank Financial Telecommunications, User Handbook Set, Standards—6, Financial Trading, 93, 2nd edn., New York, NY, September 1994.

<sup>w</sup> <sup>x</sup> 37 D. Sperber, D. Wilson, Relevance, Communication and Cognition, Harvard Univ. Press, 1988.

38 K. Steel, Another approach to standardising EDI, Electronic Markets, 12, 1994.

<sup>w</sup> <sup>x</sup> 39 D. Straub Jr., J.C. Wetherbe, Information technologies for the 1990s: an organizational impact perspective, Comm. ACM 32 11 1989 1328–1339.Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 United Nations, United Nations Directories for Electronic Data Interchange for Administration, Commerce and Transport D96a , http:Ž . <sup>rr</sup>www.unicc.org<sup>r</sup>unece<sup>r</sup>trade<sup>r</sup> untdid<sup>r</sup>d96a<sup>r</sup>d96a.zip, downloaded on August 8, 1996.

<sup>w</sup> <sup>x</sup> 41 T. Winograd, C.F. Flores, Understanding Computers and Cognition, Ablex Publishing, Norwood, NJ, 1986.

<sup>w</sup> <sup>x</sup> 42 C.C. Woo, SACT, A tool for automating semi-structured organizational communication, in: F. Lochovsky, R.B. Allen Ž . Eds. , Proc. Conf. on Office Information Systems, ACM SIGOIS and IEEECS TC-OA, ACM Press, April 1990, pp. 89–98.

<sup>w</sup> <sup>x</sup> 43 C.C. Woo, M.K. Chang, An approach to facilitate the automation of semistructured and recurring negotiations in organizations, J. Org. Computing 21 1992 47–76.Ž .

![](/api/attachments/GHBDTEGV/fulltext/images/d0adeb35970370128c878393fa3f910c147d2bdb0bcc8ff93f45642c0ad90853.jpg)

Dr. Moore is an Assistant Professor in the Computer and Information Systems Department at the University of Michigan Business School. His research program focuses on automated electronic messaging, the technology needed to make it possible, the underlying theory, and its relationship with electronic commerce. The broad areas of applicability for his research are in workflow automation, EDI, and information retrieval. Other lines of research have led him to

construct a SAT for investigating fleet mixes, an environment for creating and investigating mathematical models, a prototype of a document retrieval system based on a formal language, a message management system SAT for an office environment, and a workŽ . management system.
