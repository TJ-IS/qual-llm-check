---
otero_id: 16931
otero_key: "63XPMCEW"
title: "Eliciting and modelling expert knowledge"
authors: "George Wright; Peter Ayton"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90032-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Eliciting and Modelling Expert Knowledge

George WRIGHT \* and Peter AYTON \*\*
\* Bristol Polytechnic, Bristol BS16 1QY, UK
\*\* City of London Polytechnic, London E1 7NT, UK

This paper evaluates the usefulness of various psychological techniques that can be utilized to elicit and model expert knowledge for subsequent representation in rule-based expert systems. Interviewing, protocol analysis and multidimensional scaling are described and evaluated as complementary methods of knowledge elicitation. In addition ‘context-focusing’ and card-sorting are introduced as short-cut methods for the knowledge engineer’s ‘tool box’.

It is argued that expert knowledge about uncertainty can be represented as subjective probabilities and that these assessments can (and therefore should) be checked for consistency and coherence as a pre-condition for realism.

Finally, the issue of whether it is possible to improve upon expert judgement is discussed and evidence is reviewed which shows that, in repetitive decision-making situations, statistical models of the expert can out-perform the expert on whom the models are based. Statistical modelling has a valid but limited application as a replacement for expert judgement.

![](/api/attachments/63XPMCEW/fulltext/images/c27e99c6cbfabec37e58ab562e321ca881dbf9a05e3c33c15e49738773a79814.jpg)

George Wright recieved his PhD from Brunel University in 1980. He has since published widely on the human aspects of decision-making and forecasting. His publications include Behavioral Decision Theory, Beverly Hills: Sage and Harmondsworth: Penguin, 1984, Behavioral Decision Making, New York: Plenum, 1985, Investigative Design and Statistics, Harmondsworth: Penguin, 1986 and Judgemental Forecasting, Chichester: Wiley, in press.

$^{1}$ This research was supported in part by the Knowledge Engineering Business Centre of International Computers Ltd and in part by the British Economic and Social Research Council via project grant C00232037. We especially wish to thank Leslie Rabbitts at ICL for enabling us to test out our academic ideas in the real-world of business.

## 1. Introduction

Factual knowledge can be represented in terms of classifications and relationships. This sort of knowledge is often termed declarative knowledge. Procedural knowledge is concerned with the procedures and rules for manipulating the declarative knowledge and also with the control structures which contain information about when and how to apply the procedures and rules. In expert systems the knowledge represented is often that acquired from a human expert. This paper discusses the nature of expertise and evaluate the usefulness of various psychological techniques to aid the elicitation or acquisition of human knowledge.

## 2. What is Expert Knowledge?

Expert knowledge is additional to knowledge contained in textbooks:

'Learning by observing seasoned experts is a very important step in the development of medical expertise. Prior to observing experienced physicians, a medical student first spends two or three years studying and acquiring textbook knowledge of diseases and the physiology of the human body. At the end of this period, despite a significant repertoire of factual medical knowledge, the student is unable to demonstrate any real diagnostic expertise.... Expertise is acquired during an apprenticeship period in which the student watches his or her mentors diagnosing real cases and at-

![](/api/attachments/63XPMCEW/fulltext/images/03ff141204f5aa5e111ea8582f9814750cf6203a8dd9939eae29334e02d4b980.jpg)

Peter Ayton conducted research in memory and language at University College London before joining the Decision Analysis Group. His current research activities include the development of statistical methods for individual difference analysis and the study of intuitive statistical concepts.

tempts to duplicate this skill on his or her own through practice.' [Wilkins et al. (1984)]

Feigenbaum (1979) notes that expert knowledge consists of unwritten ‘rules of thumb’:

'(it is)... largely heuristic knowledge, experimental, uncertain – mostly 'good guesses' and 'good practice', in lieu of facts and figures. Experience has also taught us that much of this knowledge is private to the expert, not because he is unwilling to share publicly how he performs, but because he is unable. He knows more than he is aware of knowing.... What masters really know is not written in the textbooks of the masters. But we have learned that this private knowledge can be uncovered by the careful painstaking analysis of a second party, or sometimes by the expert himself, operating in the context of a large number of highly specific performance problems.' (p. 8)

Even understanding one expert's actions can require the expertise of another:

'The ability to infer the reasons for the action of another expert when watching the expert solve a problem is as much a dimension of expertise as problem solving, explanation of expertise, and technology of expertise. A familiar example of this within the field of artificial intelligence is seen during organised human-machine chess matches. There is often a highly ranked player present who explains the probable reason for the moves of each player during the game.... When a physician asks a question of a patient, another physician watching the patient/physician interview can usually infer the reason for each question asked of the patient.' [Wilkins et al. (1984)]

## 3. Is it Easy to Elicit Expert Knowledge?

All of the published articles in the area of knowledge engineering point to the difficulties of eliciting expert knowledge. Hayes-Roth et al. (1983) have described the problem in this way:

'Knowledge acquisition is a bottleneck in the construction of expert systems. The knowledge engineer's job is to act as a go-between to help build an expert system. Since the knowledge engineer has far less knowledge of the domain than the expert, however, communication problems impede the process of transferring expertise into a programme. The vocabulary initially used by the expert to talk about the domain with a novice is often inadequate; thus the knowledge engineer and expert must work together to extend and refine it.' (p. 129)

## Duda and Shortcliffe (1983) conclude that:

'The identification and encoding of knowledge is one of the most complex and arduous tasks encountered in the construction of an expert system.... Thus the process of building a knowledge base has usually required a time-consuming collaboration between a domain expert and an AI researcher. While an experienced team can put together a small prototype in one or two man-months, the effort required to produce a system that is ready for serious evaluation (well before contemplation of actual use) is more often measured in man-years.' (p. 265)

Wilkins et al. (1984) also emphasise the effort required:

'A bottleneck in the creation of an expansion of these knowledge-intensive systems is knowledge acquisition. Acquiring the necessary domain knowledge is a very tedious and time-consuming manual process requiring many person-years of effort on the part of a domain expert and a knowledge engineer. There is good motivation to automate this process but methods to date have proved unsuccessful.' (p. 1)

## 4. What Techniques Can Aid the Elicitation of Expert Knowledge?

Currently expert knowledge is often elicited by informal interviews and the knowledge obtained is coded into empirical rules. In many descriptions of how expert systems are built, knowledge elicitations is glossed over. For example, Pauker et al. (1976) said that they elicited the problem-solving strategies that physicians use by ‘introspection and through direct observations of the clinician’s problem-solving behaviour. The insights gained in this way were represented as a computer program.’ (p. 983)

Duda and Gaschnig (1981), commenting on the development of the PROSPECTOR system for mineral exploration, noted: 'We developed each model by interviewing a geologist who is an authority on a particular class of deposits, and then translating the geologist's knowledge of the associations between field-observable evidence and relevant geological hypotheses into a structured collection of rules.' (p. 259)

The reason why the methods of knowledge elicited are often unstated or vague is because they are mainly ad hoc and non-scientific. The knowledge engineers are often computer specialists without training in relevant psychological techniques.

In the next sections of this paper we will describe, in some detail, techniques that have been successfully used to elicit and model expert knowledge.

## 4.1. Interviewing - questioning the expert

What precise questions should you ask? Perhaps the best way to start is to ask the expert to talk for a set period, say half-an-hour, on the domain of expertise that you are interested in modelling in order that you can establish an overview of the area. It is then possible to ask direct probing questions to access declarative and procedural knowledge. However, this sort of knowledge elicited by interview may not be easily translated into the rules and control structures of an expert system. Perhaps the best method to obtain these rules is by protocol analysis, which we describe in the next section.

Interviewing can be used to gain an overview of the domain of expertise and an understanding of the expert's jargon.

## 4.2. Protocol analysis - getting the expert to 'think aloud'

As the expert works through a problem in his field of expertise ask him to 'think aloud' about his every thought and action. Record this verbalisation and have it typed out. The problem may be a real one or an imaginary one or a set of problems that describe in a fairly complete fashion the types of problem that the expert system is to be able to solve in the same way as the expert solves them. This technique is a method of concurrent protocols since the think aloud data is obtained at the time the expert solves the problem. Below is an example of a protocol of a clinical expert examining data on a patient who may have leukaemia. This protocol is taken from Myers et al. (1983).

'This patient is a fifty year old adult who in common with the last patient was said to have chronic myeloid leukaemia diagnosed in 1978 and has now gone into blastic transformation and is said to be lymphoid by morphological and cytochemical criteria.... Looking at bone marrow which has 70% BLASTS. Um I also know, though I can't give a numerical value to it, than when this value of 70% is obtained from a smear of blood then in the process of doing the market tests there is an ENRICHMENT OF BLASTS, SO 70% MAY BE A MINIMUM value and there may be rather more. TERMINAL TRANSFERASE IS 90%. IN FACT THERE HAS BEEN SOME ENRICHMENT, SINCE IN AN ADULT THIS IS A LEUKAEMIA MARKER. An ADULT PATIENT WITH NORMAL TdT POSITIVE CELLS ARE NOT MORE THAN 5%. So this is...are all leukaemic lymphoblasts in lymphoblastic transformation of CLL rather then myeloblastic. And I'm looking to see what subset it is – the IM-MUNOGLOBULIN IS ONLY 4% SO ITS NOT B. T-CELL MARKERS ARE 14%, 5%, 6% AND LESS THAN 1%. ALL LESS THAN 20. YOU COULD SAY THAT 90% OVERLAPS WITH 14% BUT I REGARD THAT AS AN IN-SIGNIFICANT OVERLAP...WITHIN THE ERROR OF OUR TECHNIQUES.'

These investigators have placed in block capitals the information that they thought useful in extracting from the protocol the knowledge statements shown below:

70% blasts, preparation gives enrichment of blasts, so 70% may be a minimum.

Terminal transferase is 90%. In fact there has been some enrichment.

Since in an adult this is a leukaemia marker. An adult patient with normal TdT positive cells are not more than 5%.

immunoglobulin is only 4% so it's not B.

T-cell markers are 14%, 5%, 6% and less than 1%. All less than 20. You could say that 90% overlaps with 14% but I regard that as an insignificant overlap...within the error of our techniques.

and the rules:

preparation enriches for blasts, so take the blast count to be a minimum

TdT > blast count → suggests enrichment
TdT in adult → leukaemic marker
normal adult level of TdT less than 5%
immunoglobulin < 5% → not B-cells
T-cell markers less than 20% → not T-cells
overlap of 14 with 90 → insignificant

Sometimes it may be more appropriate to video the expert performing the task and, after the solution has been achieved, play back the video and ask the expert to say what he was thinking and doing. This method is one of retrospective protocols. This procedure is justified when it is thought that obtaining a concurrent protocol will affect the expert's performance on the task. Conversely, it may also be useful when performance of the task is suspected to interfere with the expert's ability to offer a coherent protocol. Even if no apparent hindrace is evident in either activity additional insights may be available to the expert when engaged in focussed contemplation of his or her own performance. This should be valuable when the expert's knowledge is largely tacit and not easily translated into a verbal format. This problem is considered further in the next section.

## 4.2.1. Some problems with protocol analysis

Some investigators [e.g., Ericsson and Simon (1980)] have noted that over time recurrent cognitive processes tend to become automated. Consider trying to explain to someone how you coordinate your own actions to enable you to jump on a moving bus.

You may be able to verbalise about some other cognitive processes more easily but perhaps not accurately. Consider the task of explaining to someone how you know how far away objects are. For example the distance, from yourself, of two other cars on a road as you drive along the road. How do you measure such distances without a ruler or tape measure? Psychologists have shown, by extensive experimentation, that we judge distance by several cues. The first set of cues are physiological and come from feedback from muscle contractions in our eyes. The muscles press hard on our eye lens to focus on near objects but relax to focus on distant objects. Also with distance the texture of fine detail becomes less distinct and colours appear to fade to a hazy blue. Familiar size is another cue to distance – we know that all cars are roughly the same physical size even though the size of the image of the car on the back of the eye's retina (which is like the film in a camera) reduces dramatically the further away a car is – thus a change in image size can be used as a cue to how far away a car is. Another cue to depth is the interposition of one object over another. Consider fig. 1. From this diagram it appears C is in front of B which is in front of A.

From this overview of four of the many cues to distance that we use you will have begun to realise that how we say we do something, like judge distance or depth, may not be a true description of how we really do it. It follows that expert protocols may also be invalid descriptions of 'real' cognitive processes and operations. As knowledge engineers, we may be able to model what the expert says he does but these verbalisations may not be a valid description of real processes, which may be very difficult for the expert to verbalise. Interviews, especially, may encourage the expert to speculate and theorise about his or her cognitive processes. In this regard it is worth noting that Nisbett and Wilson (1977) have argued that we have no conscious access to mental processes – only the mental products of such processes. From these products the existence and nature of the processes can only be inferred.

Asking the expert to perform a range of tasks is more likely to provide relevant knowledge than simply asking the expert what he does.

Obtaining concurrent protocols is also more likely to result in valid knowledge of expert processes than probing questioning.

![](/api/attachments/63XPMCEW/fulltext/images/a1bcefc2ed81f41941706b37c716190b4e23096d0bbf9c38fd3ecc0983cddd16.jpg)  
Fig. 1. A cue to depth.

Consider the following three methods of eliciting knowledge:

(1) Focused question: Did you use X as a subgoal?
Answer: Yes

(2) Unfocused question: Did you use any sub-goals? If so which?
Answer: Yes, I used X

(3) Concurrent protocol: ...I was first trying to get X and I... when I attained X...

All three elicitation methods gave the knowledge engineer the same information but the first method also tells the expert what is required and may encourage the expert to say what he thinks is the 'correct' answer. The second prompts the expert to generate a plausible answer which, consequently, may not be valid. The third method contains the strongest evidence that the expert really used X as a subgoal.

Does the generation of verbal protocols affect the way in which the expert performs his expertise? Ericsson and Simon have argued that think aloud protocols will not change task performance although the speed of task performance may be slowed down. For example Roth (1966) found that verbalisation had no effect on the effectiveness of task performance. However, asking the expert (by probing questioning) to explain why he is doing what he is doing requires the expert to attempt to access additional knowledge and information in his memory and so will disturb task performance. It follows that probing questions should follow immediately after the expert has demonstrated his expertise or as the expert performs another task.

Ericsson and Simon (1979) have noted that the automation of expertise is analogous to executing a computer algorithm in compiled instead of interpretive mode. Automation and compilation have two important consequences. They greatly speed up the process, and they make the knowledge of the process unavailable to memory and hence unavailable for verbal reporting.

Fast automatic processes may proceed in parallel and unpractised processes may follow a slower serial sequence. Consider the slow deliberate movements of a novice bricklayer and the movements of a skilled man. With an increase in experience of a task the cognitive processes that the novice is able to verbalise may be unavailable to the expert when asked to 'think aloud'.

Many studies have shown that people can display consistent and accurate behaviour without being able to report verbally the concepts being used [e.g., Bugelski and Scharlock (1952)]. There appears to be a negative relation between degree of practice and awareness of the intermediate stages of a cognitive process. Ericsson and Simon (1980) argue that many overlearned processes operate automatically without leaving any more trace than their final result in memory.

In a recent study, Berry and Broadbent (1984) explored the relationship between a person's performance on a cognitive task and the person's ability to make explicit the knowledge underlying that performance – assessed on a post-task questionnaire. The task was computer-implemented and required individuals to reach and maintain specified target values of an output variable by varying a single input variable. The nature of the equation was such that there was no unique output associated with any one input. The resulting output depended on previous input. The task, like a manual skill, required sustained performance and also cognitive decision-making. They found that practice significantly improved performance but had no effect on the ability to answer task-related questions. Berry and Broadbent concluded that assessing knowledge by means of a questionnaire did not give a true picture of an individual's competence. Also, providing an individual with appropriate detailed verbal instructions which are understood (and are later shown to have been remembered on the post-task questionnaire) is not necessarily sufficient to improve task performance – the individual must implement this verbal understanding.

It has also been shown that people tend to stop verbalising or to verbalise incompletely when the task is difficult and takes a lot of mental effort for a solution. Chess grandmasters seem unable to report intermediate stages in their thought processes as they contemplate difficult moves [de Groot (1965)]. Rather these experts tend to report experience of 'insight' where the solution appears as a whole as if from nowhere.

In general it would appear that a protocol is potentially useful for what it contains rather than what it omits.

Another conclusion to be drawn is that when people are asked probing questions about their cognitive processes they frequently do not base their answers on the specific memory of what they did but tend to speculate and theorise about what they did. Such speculations may of course not be valid. People try to 'fill out' and generalise incomplete or missing memories. Such speculations are shown by long pauses in replying to questioning and 'tentative' answering.

To summarise, verbal protocols are best taken at the time the expert performs a task within his domain of expertise. Several tasks which illustrate different aspects of the expertise should be used to elicit protocols; repetitive successive elicitations will check the validity of expert protocols. Probing questions should be left until the task has been completed, or perhaps asked as the expert performs another task, and the expert should be questioned in as indirect a way as possible so that words are not put in the expert's mouth as he helpfully tries to describe a thought process that may be automatic or compiled and so not available for verbalisation. Nevertheless, probing questions may uncover underlying cognitive processes that have not been verbalized as protocols.

Another form of protocol analysis which allows direct and often more convenient access to procedural knowledge than concurrent and retrospective protocols is that of ‘context-focusing’.

4.2.2. Context-focusing: Short-cut protocol analysis
Context focusing $^{1}$ is applied after the knowledge engineer has used investigative interviewing to gain an initial account of a problem area and has decided that development of a knowledge based system may be an appropriate solution to a problem. Context-focusing gives the knowledge engineer access to the expert's sequence of rule testing. By itself it does not directly allow access to the expert's knowledge of the classification or relationships between the objects, experience and rules of the expert's world. Multi-dimensional scaling and card-sorting tasks, to be discussed later in section 4.3, are used for this purpose.

In context-focusing the knowledge engineer imagines a particular state of the system or classification and the expert has to find out what it is. For example, a car-fault diagnosis problem where the knowledge engineer (KE) is trying to discover the sequence of rule testing that a mechanic (M) uses to diagnose why a car won't start.

M Does the ignition light come on when you turn the key?

KE Yes.

M Does the petrol gauge show that there is petrol in the tank?

KE Yes.

M Does the engine turn over when you turn the key?

KE Yes.

M Does it turn over as quickly as it does normally?

KE No.

M ...

If the mechanic is using his expertise efficiently the earlier questions in a sequence should serve to eliminate the most likely cases of a car failing to start. In other words, the early testing of a rule indicates that it has higher priority than rules that are tested later. Ideally the knowledge engineer should initiate the context-focusing procedure many times, each time imagining an alternative state of the system. In this way it is possible to check that the expert's priority ordering of rule testing is consistent from task to task. If it is not then the knowledge engineer should ask the expert why his or her sequence of questioning changed. If the sequence is consistent then the knowledge engineer should discuss the rationale behind the ordering with the expert.

In the above example of car-fault diagnosis, the mechanics may reply that the most frequent cause of a car not starting is a flat battery but often failure to start is the result of an empty petrol tank. It follows that the expert's second question eliminates a common cause of failure and the third and subsequent questions begin to focus down on the electrical system, in order to ensure that the cause is not there. Intuitively it would seem that the expert's fourth question would be a more appropriate initial question. But remember that the expert will often be transferring knowledge that is previously unfamiliar to the knowledge engineer. Only by questioning the expert on the rationale for the sequence will a more efficient sequence of rule testing normally become apparent.

If the knowledge engineer is relatively unfamiliar with the domain of expertise in which a knowledge based system is to be built, he or she may not be able to answer the expert's questions in the process of view-changing. In these circumstances the knowledge engineer should act as an observer whilst two experts, who share a common understanding of the knowledge domain, initiate the context-focusing technique. In this case the observer should make a careful record of the sequence of rule testing for later elaboration in discussion with the expert, or experts. The knowledge engineer should bear in mind the potential problems of combining knowledge obtained from different experts.

## 4.3. Elicitation of declarative knowledge using multidimensional scaling

When there are a number of closely related concepts and there is no specialised vocabulary to describe subtle distinctions and relationships, a technique called multidimensional scaling can be a useful tool for the knowledge engineer. Multidimensional scaling allows experience and relationships to be communicated from one person (an expert) to another person (a knowledge engineer) whilst de-emphasizing the mediating role of language.

A problem often faced in building an expert system is how to measure and understand the way experts view relationships between objects and experiences. Multidimensional scaling analysis allows us to represent visually the psychological similarities between objects or experiences as points on a scattergram. Decreasing physical separation between objects represents increasing psychological similarity. Objects judged to be psychologically dissimilar will be represented as being far apart.

By asking experts to rate the similarity of objects and subsequently representing the similarity as physical distance it is possible to make interpretations of the underlying dimensions on which the objects have been judged relative to one another. Multidimensional scaling (MDS) procedures do not require any a priori knowledge of these dimensions and, since only similarity judgements are required, the knowledge engineer does not 'put words into the expert's mouth'. Conversely the expert does not put jargon into the knowledge engineer's ear.

MDS is an attempt to measure and understand the relations between objects within an assumed spatial model of psychological similarity. MDS is simply a mathematical tool for representing the adjudged similarities between objects as a spatial map.

In multidimensional scaling studies, each possible pairing of objects from an object set is presented to the expert who then rates the similarity of the pair on a seven-point scale ranging from, say, no similarity at all to completely similar. In most situations these ratings will be ordinal-level. The intention of non-metric multidimensional scaling is to represent, as closely as possible, the rank order of the similarity judgements as rankordered distances in some psychological 'space'.

In some cases, it can be shown that MDS techniques can be used to elicit subjective perceptions that are not accessible with protocol-based methodologies. Protocols and interviews are dependent upon the mediating role of language and may therefore be inappropriate for some situations. Below we detail one such case, described by Whalley (1984), involving the perception of pain. Another example might be the diagnosis of the cause of an unaccustomed noise in a particular type of machine.

The dominant methodology at present used to explore pain perception involves checking descriptive words on a questionnaire. From the words an individual has checked to describe his pain it is possible to make a preliminary diagnosis. This diagnosis is based on previously observed relations between words checked and subsequent final diagnoses, based in some cases on surgical investigation. Words included in the questionnaire including 'pulsing', 'drilling', 'cutting', 'tender', 'dull', 'tight' etc. Whalley showed that these linguistic descriptions have different meanings for different people and advocates a multidimensional scaling approach to pain. In his study, patients were required to make comparative similarity judgements between the pain that they were experiencing and a set of commonly occurring painful events. The relational information shown between the new pain and the set of common pairs can then be used as a method for diagnosis without requiring patients to use imprecise ambiguous adjectives. One of Whalley's two-dimensional reference plots is given in fig. 2. He has labelled the two pain dimensions 'intensity' and 'duration'.

Other variations of multidimensional scaling and cluster analysis allow access to hierarchies in declarative knowledge. However, since most implementations of these analyses are on main-frame computers the knowledge engineer may find card-sorting techniques, to be discussed in the next section, more convenient to use.

## 4.3.1. Card-sorting: A short cut to declarative knowledge

Card-sorting techniques $^{2}$ are very easy to use and involve the knowledge engineer writing the names of the objects, experiences or rules in the expert's world onto individual cards. Only those concepts which the knowledge engineer feels need to be explored should be used in the card-sorting tasks. These tasks give the knowledge engineer access to the expert's knowledge of the classifications and relationships between objects, experiences or rules. Essentially the tasks allow access to an understanding of the structure of the knowledge underlying the expert's jargon.

4.3.1.1. Group separation task. Take the whole set of cards and ask the expert to sort them into two groups which the expert should then name. For example, the names of fifteen particular models of cars may be sorted into 'foreign' and 'British' models. Shuffle the cards and then ask the expert to sort the cars into three named groups. For example, the fifteen cars may be sorted into 'estates', 'sports cars' and 'family cars'. Next re-shuffle the cards and ask the expert to sort the cars into four named groups. For example, the fifteen cars may be sorted into ‘expensive British cars’, ‘less expensive British cars’, ‘expensive foreign cars’ and ‘less expensive foreign cars’. The latter sort may lend itself to representation as the hierarchy shown in fig. 3. But a hierarchical representation of classifications and relationships may not always be appropriate. The first two card-sorts cannot be combined directly as a hierarchy.

![](/api/attachments/63XPMCEW/fulltext/images/9a027e2f6917994bc888a681f3d42fc9d48592358d1c9139486e3365b36e0863.jpg)  
Fig. 2. Multidimensional scaling of subjective perceptions of pain.

![](/api/attachments/63XPMCEW/fulltext/images/375b428d5ca5f0e6b5e631652bdce4f7ceaadae3c048e394450fe0e02d1389b1.jpg)  
Fig. 3. A possible hierarchy.

Even the third card-sort may be represented as the alternative hierarchy illustrated in fig. 4. Perhaps if the fifteen cards were sorted into twelve categories the hierarchy shown in fig. 5 would result. Check that any constructed hierarchy matches the expert's view of the world by presenting him or her with the objects in the lower classifications of a hypothesised hierarchy and asking him or her to create fewer classifications by combining categories. The combined categories should match your hierarchy. For example, the four categories of 'expensive foreign', 'expensive British', 'less expensive foreign' and 'less expensive British' may be combined into the two groupings of 'expensive' and 'less expensive'.

4.3.1.2. Group creation task. Instead of sorting the group of cards into successively smaller groupings another way to approach the problem is to ask the expert to find a pair of cards in the set that are more similar to each other than any other possible pairing. For example, two car models made by the same manufacturer may be seen as the most similar of all possible pairings of the cards. Next ask the expert to find the next most similar pairing or allow him or her to add another car to the first pairing. In this way the relationship between what the knowledge engineer has written on the cards can be explored with the expert as he or she groups and sorts the cards. To this end it is particularly important that the knowledge engineer asks the expert to try and name the groups or links that are formed. The knowledge engineer will find himself or herself asking the expert questions about groups that have been formed such as: 'How are these cards similar but yet different from these cards?'

![](/api/attachments/63XPMCEW/fulltext/images/d5833cbb201c2e12a23be3c6ce78665e86ed2c872f6900703cb6280124dd4f45.jpg)  
Fig. 4. An alternative hierarchy.

![](/api/attachments/63XPMCEW/fulltext/images/4365cba98c9de754b86a73f1b09defa1cf50f7b4f0018ffaeef6adf8b5caba5f.jpg)  
Fig. 5. A hierarchy with four levels.

By this method the knowledge engineer becomes aware of the structure of the expert's knowledge and, for example, may hear the expert answer by saying:

'On these cards are items that we normally stock.'
'On these cards are the names of the chemical processes by which our products are made'.

‘These are parts of the machine’s electrical system.’
‘These are types of weed that respond to weed-killer X whilst these are types of weed that require weedkiller Y.’

‘These are forms that need to be completed to obtain a stock item, these are forms for non-stock items whilst these are forms to call in an outside contractor for repair work. All these forms need authorisation by manager X before they can progress through the purchasing system.’

4.3.1.3. Triadic comparisons This card-sorting method requires the knowledge engineer to take three cards at random from the set of cards. The three cards are the presented to the expert who is asked to put the cards into two groups such that the two cards in one group are more similar to each other than to the third card. The expert is then asked to try and name the way in which the groups differ. For example the expert may say: 'On these two cards are the names of dials I need to keep a careful eye on. The third dial's reading is less critical.'

In general, the different techniques of card-sorting will not produce identical representations of the structure of an expert's knowledge. However, they do provide a means of achieving a more focussed and systematic understanding of the classifications and relationships present in the expert's view of the world.

## 4.4. Elicitation of expert knowledge about uncertainty

Many of the rules elicited from experts will follow the form ‘A and B together often imply C’ and many expert systems have in-built facilities to deal with uncertain information. For example, Joseph (1982) notes that not all expert knowledge is a set of ‘black-and-white’ facts. Most expert systems that can tolerate uncertainty employ some kind of probability-like measure to weigh and balance conflicting evidence. PROSPECTOR assigns probabilities to conclusions using an approximate form of Bayes’ theorem to update probabilities as more information is acquired. MYCIN uses ‘certainty values’, but the meanings of the numbers are debatable since they do not follow the probability laws.

Indeed as Feigenbaum (1979) notes: 'Mycin was the first of our programs that forced us to deal with what we had always understood: that experts' knowledge is uncertain and that our inference engines had to be made to reason with this uncertainty.' (p. 18)

## 4.4.1. Methods of eliciting subjective probabilities

The direct method for probability assessment is very simple; the probability assessor is simply required to state a number between 0 and 1, with 0 meaning that it is thought impossible that an event will occur and 1 meaning it is thought absolutely certain that the event will occur.

It is also possible to vary the response mode and ask the expert to assess his or her uncertainty in odds. Assessed odds of 1 to 1 would mean that it is thought that the event's occurrence is equally likely as its non-occurrence. Odds of 1,000 to 1 against would mean that it is thought that the event's occurrence was extremely unlikely. Conversely, odds of 1,000 to 1 on would mean that the event's occurrence is thought to be extremely likely.

It is easy to convert an odds response to probability. For example, odds of 10 to 1 against the event happening is equivalent to a probability of 0.91 that the event will not happen or 0.09 that the event will happen. Odds of 10 to 1 on are equivalent to a 0.91 probability that the event will happen. It is often found that a converted odds response is not identical to a direct probability estimate for the occurrence of the same event. We will return to this issue later.

![](/api/attachments/63XPMCEW/fulltext/images/a957364028959e42e1634f756772e82715b444b4bf52f0c9260f494ecdec4901.jpg)  
Fig. 6. Indirect Measurement of Probability.

Next we will consider an indirect way of measuring your degree of belief. Consider wager A presented in fig. 6. If it does rain at 11 a.m. tomorrow over your home you win £100; if it doesn't you win nothing.

Now consider wager B, which refers to the 'spinner bet' consisting of a pointer which is free to rotate over a circle comprising two colours, black and white. I can adjust the relative amount of these two colours. If the pointer lands in the black you win £100; if it lands in the white you win nothing. Given that the proportion of black and white sectors is that in fig. 6, which wager would you prefer, wager A or wager B, or are you indifferent between the wagers?

If you preferred wager A to wager B then I would increase the proportion of black to white until you prefer wager B to wager A. I would then reduce the proportion of black until you are indifferent between the two wagers. The relative proportion of black to white would then be equivalent to your subjective probability that it will rain tomorrow. This indifference bet method allows the knowledge engineer to measure subjective probability without requiring the expert to state any numbers to describe his or her degree of belief. The only restriction in this method is that the utilities of the outcomes in the two wagers must be strictly identical. In this instance wager B must be played at, or shortly after, 11 a.m. tomorrow, when we known whether it has actually rained or not. If the result of wager B was to be paid out now, the expert's utility for an ‘instant’ £100 may be higher than that for a ‘delayed’ £100 and so the two wagers would not be strictly identical.

Notice that although people may differ in their utility for £100, this amount is similar in both wagers and therefore has no bearing on the measurement of subjective probability.

Which of these three methods is the best for elicitation of subjective probability? The empirical evidence is, unfortunately, contradictory. Sometimes the indirect methods are inconsistent with direct methods and sometimes they are not. Some studies have shown consistency between probability estimates inferred from wagers and direct estimates. However, other studies have shown that statistically naive subjects were inconsistent between direct and indirect assessment methods, whereas statisticians were not. Generally, direct odds estimates, perhaps because they have no upper or lower limit, tend to be more extreme than direct probability estimates.

If probability estimates derived by different methods for the same event are inconsistent, which method should be taken as the true index of degree of belief?

One way to answer this question is to use the method of assessing subjective probability that is more reliable. In other words there should be high agreement between the subjective probabilities, assessed at different times by a single assessor for the same event, given that the assessor's knowledge of the event is unchanged. Unfortunately, there has been relatively little research on this important problem. Goodman (1973) reviewed the results of several studies using direct estimation methods. Test-retest correlations were all above 0.88 with the exception of one study using students assessing odds – here the reliability was 0.66. Goodman concluded that most of the subjects in all experiments were very reliable.

Whatever direct or indirect method of obtaining a numerical estimate is used it is clear that the elicited probabilities can be utilised easily in an expert system. By contrast, consider verbal reports of uncertainty, for example, 'very probably' or 'extremely likely'. These estimates are less precise than numerical estimates and interpretation of their meaning varies from person to person. Table 1 sets out the variation in numerical meaning attributed to some probability expressions found by Lichtenstein and Newman (1967). Also notice the asymmetry found between mirror-image pairs. Clearly verbal expressions of probability are open to misinterpretation.

Variations in the numerical meaning of probability expressions.

<table><tr><td></td><td>Mean associated probability</td><td>Range of associated probabilities</td></tr><tr><td>Highly probable</td><td>0.89</td><td>0.60–0.99</td></tr><tr><td>Quite likely</td><td>0.79</td><td>0.30–0.99</td></tr><tr><td>Probable</td><td>0.71</td><td>0.01–0.99</td></tr><tr><td>Possible</td><td>0.37</td><td>0.01–0.99</td></tr><tr><td>Improbable</td><td>0.12</td><td>0.01–0.04</td></tr><tr><td>Quite unlikely</td><td>0.11</td><td>0.01–0.50</td></tr><tr><td>Highly improbable</td><td>0.06</td><td>0.01–0.30</td></tr></table>

Wright, Ayton and Whalley (1985) have developed a computer program called FORECAST which helps experts make subjective assessments of probability. The program checks for consistency between direct and indirect assessments of probability and reports inconsistencies back to the expert for interactive resolution. The program then goes on to check for coherence in probability assessment by using the probability laws. For example, one simple probability law states that the probability of event A and event B both occurring is equal to the probability of event A occurring multiplied by the probability of event B occurring given that event A has occurred. More formally:

$$
\mathrm{P} (\mathrm{A} \text { and } \mathrm{B}) = \mathrm{P} (\mathrm{A}) * \mathrm{P} (\mathrm{B} \setminus \mathrm{A})
$$

Consider an imaginary diagnostic expert system for asserting why a car won't start. It is possible to work out the probability that the cause of the starting failure is due to both badly set contact points and sparking plugs [P(A and B)] if we can assess the probability that the contact breaker gap is badly set [P(A)] and the probability that the plug gaps are wrongly set given that we know the contact-breaker gap is wrongly set. [P(B \ A)]

Why bother to work through this probability law? The reason is that the two sides of the equation seldom balance - experts show marked incoherence in judgemental assessment of probability (Ayton and Wright, in press). The FORECAST program monitors subjective probability assessments for coherence and interactively resolves incoherence with the probability assessor.

Only when probability assessments are consistent and coherent is it sensible to check that they are also realistic. One measure of the realism of probability assessments is calibration. A person is said to be perfectly calibrated if, for all events or propositions to which he or she assigns a given subjective probability (P), the proportion that occurs, or is correct, is P. For example if you assign a probability of 0.7 to each of ten questions concerning the possible occurrence of future events, you should get seven of those questions correct. Similarly, all events that you assess as being certain to occur (1.0 probability assessment) should, in fact, occur. Wright and Ayton (1986) discuss the relationship between consistency, coherence and validity in more detail.

## 5. How Good is the Expert's Expertise: Is It Possible to Improve on Expert Judgement?

Up to now we have discussed some of the approaches to eliciting expert knowledge for modelling in rule-based inference systems. This discussion has been founded on the assumption that it is worth-while modelling the expert in this way. In the next section of this paper we discuss some research which has shown that expert judgement can be improved upon by statistical modelling.

Expert judges have been studied making illness diagnoses on the basis of patient symptoms or characteristics. One of the most extensive evaluations of medical expertise was that conducted by Meehl (1959). The judgemental problem used was that of differentiating psychotic from neurotic patients on the basis of their personality questionnaire profile.

Each patient upon being admitted to hospital had taken eleven personality tests. Expert clinical psychologists believe (or at least used to believe) that they can differentiate between psychotics and neurotics on the basis of profile of eleven questionnaire scores.

Initially researchers tried to 'capture' or 'model' expert judges by a simple linear regression equation. This judgemental representation is constructed in the following fashion. The clinician is asked to make his diagnostic or prognostic judgement from a previously quantified set of cues for each of a large number of patients. These judgements are then used as the dependent variable in a standard linear regression analysis. The independent variables in this analysis are the value of the cues. The results of such an analysis are a set of regression weights, one for each cue, and these sets of regression weights are referred to as the expert's 'model' or his 'policy'. Fig. 7 sets out the basic paradigm.

![](/api/attachments/63XPMCEW/fulltext/images/4138cdbd68ad2e1082393608ef0bb553044f296c6bee8a196d338527bc1fec2e.jpg)  
Fig. 7. Basic paradigm for the construction of a linear additive model of an expert judge.

How do these models make out as predictors themselves? That is, if the regression weights (generated from an analysis of one clinical judge) were used to obtain a ‘predicted diagnosis’ for each patient, would these diagnoses be more valid, or less valid, than the original clinical diagnoses from which the regression weights were derived? To the extent that the model fails to capture valid nonlinear variance to the expert’s decision processes, it should perform worse than the expert; to the extent that it eliminates the random error component in human judgements, it should perform better than the expert.

What were the results of this research? The overwhelming conclusion was that the linear model of the expert's behaviour out-performed the expert. Dawes (1975) noted: 'I know of no studies in which human judges have been able to improve upon optimal statistical prediction.... A mathematical model by its very nature is an abstraction of the process it models; hence if the decision-maker's behaviour involves following valid principles but following them poorly these valid principles will be abstracted by the model.'

Goldberg (1965) reported an intensive study of clinical judgement, pitting experienced an inexperienced clinicians against linear models in the psychotic/neurotic prediction task. He was led to conclude that Meehl chose the wrong task for testing the clinician's purported expertise. The clinicians achieved a 62 per cent rate, while the simple linear composite achieved 70 per cent. A 50 per cent hit rate could have been achieved by chance as the criterion base rate was approximately 50 per cent neurotic, 50 per cent psychotic.

Dawes and Corrigan (1974) have called the replacement of the expert by his model bootstrapping. Belief in the efficacy of bootstrapping is based on a comparison of the validity of the linear model of the expert with the validity of his or her holistic judgements.

Dawes and Corrigan concluded that the human decision-maker need specify with very little precision the weightings to be used in the decision – at least in the context studied; what must be specified is the variables to be utilised in the linear additive model. It is precisely this knowledge of 'what to look for' in reaching a decision that is the province of the expert clinician. It is not in the ability to integrate information that the expert excels.

The distinction between knowing what to look for and the ability to integrate information is illustrated in a study by Einhorn (1972). Expert doctors coded biopsies of patients with Hodgkin's disease and then made an overall rating of severity. These overall ratings were very poor predictors of survival time, but the variables the doctors coded made excellent predictions when utilised in a linear additive model.

In conclusion, we can say that in a repetitive prediction task only the knowledge of which variables to include in the prediction equation is important. Clinical expertise is, of course, the source of this knowledge – without it the linear models could not work. However, the clinician's importance weightings are not at all crucial. This result remains true in all the contexts so far investigated.

The research discussed in this section can be viewed as being highly critical of the conceptual basis of expert systems. However, it must be remembered that linear models only work in repetitive situations where the set of cue variables is constant from diagnosis to diagnosis – only the values or scores of the cue variables change with each decision. By contrast, the structures for knowledge representation in expert system shells allow a more flexible representation of human expertise. Perhaps the best way for the knowledge engineer to view the research on linear models is to recognise that statistical modelling has valid but limited application as a replacement for expert judgement.

## 6. The Future of Knowledge Elicitation

The next major breakthrough may come in the automation of knowledge acquisition. Robert Englemere, director of knowledge systems development for Teknowledge notes ‘we’re handcrafting now’ [quoted by Swaine (1983)]. Other researchers have developed various tools that can facilitate the process of acquiring knowledge.

For example, RULEMASTER [Michie, Muggleton, Riese and Zubrick (1984)] has been proposed and implemented as a ‘general purpose expert-system building tool’ which builds rules by ‘rule induction’ or generalisation over examples of expert decision-making. For instance, in a hypothetical example of building a system to classify animals on the basis of colour and shape the expert may type in ‘grey, big and elephant’, yellow, big and giraffe’ and ‘grey, small and tortoise’. Rulemaster would then generate the following rule:

If the animals colour is

(a) yellow, then it is a giraffe

(b) grey, then if the animals' size is

(i) big, then it is an elephant

(ii) small, then it is a tortoise.

However, computer-based automation of the full scope of knowledge may be an unrealisable dream, given our discussion of the difficulties of knowledge elicitation in this paper. Our view is supported by Meyers et al. (1983): 'In our view the automatic construction of rules by algorithmic or heuristic methods, is some way from routine practical applicability...we also believe that the attempt to automate knowledge base construction may be based on a somewhat premature rejection of knowledge elicitation techniques.'

Indeed, problems inherent in the goal of defining and representing knowledge have been the subject of debate and dispute since at least the time of Aristotle. With the development of computers these matters have now become a hot technological issue and it is perhaps tempting to suppose that some major progress is about to be made. The emergence of ‘cognitive science’ as a new discipline is, arguably, symptomatic of that optimism. Nevertheless one only has to scan reports of research in computer simulation, semantic memory modelling, natural language comprehension and other pertinent areas to appreciate the enormity of the task. The formulation of ideal, definitive and a priori principles for capturing knowledge in any domain will no doubt prove to be elusive yet awhile. Knowledge is ethereal stuff. Its successful elicitation and modelling will depend on active efforts to realise the subtleties and complexities of the problems. We hope that this discussion of the advantages and limitations of the various knowledge elicitation techniques has demonstrated the potential applicability of psychological methodology to aid modelling of expertise for the construction of expert systems.

## References

Ayton, P. and G. Wright, n.d., Assessing and improving judgemental probability forecasts, OMEGA International Journal of Management Science, forthcoming.

Berry, D.C. and D.E. Broadbent, On the relationship between task performance and associated verbalizable knowledge, Quarterly Journal of Experimental Psychology (1984) 36A, 209–231.

Bugelski, B.R. and D.P. Sharlock, An experimental demonstration of unconscious mediated association, Journal of Experimental Psychology (1952) 44, 334–338.

Dawes, R.M., Graduate admission variables and future success, Science (1975), 187, 721–743.

Dawes, R.M. and B. Corrigan, Linear models in decision-making, Psychological Bulletin (1974) 81, 95–106.

de Groot, A.D., Thought and choice in chase (Mouton, The Hague, 1965).

Duda, T.O. and J.G. Gaschnig, Knowledge-based expert systems come of age, Byte (1981) 9, 238–281.

Duda, R.O. and E.H. Shortcliffe, Expert systems research, Science (1983) 220, 261–268.

Einhorn, H.J., Expert measurement and mechanical combination, Organizational Behavior and Human Performance (1972) 7, 86–106.

Ericsson, K.A. and H.A. Simon, Verbal reports as data, Psychological Review (1980) 87, 215–251.

Feigenbaum, E.A., Themes and case studies in knowledge engineering, in: D. Michie, ed., Expert systems in the micro-electronic age (Edinburgh University, Press, 1979).

Goldberg, L.R., Diagnosticians versus diagnostic signs: The diagnosis of psychosis versus neuroses from the MMPI, Psychological Monographs (1965) 79, 602–643.

Goodman, B.C., Direct estimation procedures for eliciting judgement about uncertain events, Engineering Psychology Technical Report (University of Michigan, 1973).

Hays-Roth, F., D.A. Waterman and D.B. Lenat, eds., Building Expert Systems (Addison Wesley, Reading, MA 1983).

Joseph, E.C., Defense computer and software – what's ahead for AI? Concepts (1982) 5, 141–147.

Lichtenstein, S. and J.R. Newman, Empirical scaling of com-

mon verbal phrases associated with numerical probabilities, Psychonomic Science (1967) 9, 563–564.

Meehl, P.E., A comparison of clinicians with five statistical methods of identifying psychotic MMPI profiles, Journal of Counselling Psychology (1959) 6, 102–122.

Michie, D., S. Muggleton, C. Reise and S. Zubrick, RULEMASTER: A second generation knowledge engineering facility, Radian Technical Report MI-R-623 (Radian Corporation, Austin, TX, Dec. 1984).

Myers, C.D., J. Fox, S.M. Pegram and M.F. Greaves, Knowledge acquisition for expert systems: experience using Emycin for leukaemia diagnosis, Proceedings of Expert Systems 83 (1983).

Nisbett, R.E. and T.D. Wilson, Telling more than we can known: Verbal reports on mental processes, Psychological Review (1977) 84, 231–259.

Pauker, S.G., G.A. Gorry, J.P. Kassirer and M.D. Schwartz, Towards the simulation of clinical cognition, The American Journal of Medicine (1976) 60, 981–998.

Reboh, R., The knowledge acquisition system, in: R.O. Duda, ed., A computer based consultant for mineral exploration, Final Report, SRI International, Project 6415 (Menlo Park, CA, 1979).

Roth, B., The effect of overt verbalisation on problem solving, Dissertation Abstracts (1966) 27, 957B.

Swaine, M., Knowledge engineers' handcraft diagnostic software, Infoworld (1983) 5, 11–12.

Whalley, P.C., The psychology of similarity, Unpublished PhD. dissertation (Open University, 1984).

Wilkins, D.C., B.G. Buchanan and W.J. Clancey, Inferring an expert's reasoning by watching, Proceedings of the 1984 conference on Intelligent Systems and Machines (1984).

Wright, G. and P. Ayton, The psychology of forecasting. Futures (1986) 18, 420–439.

Wright, G., P. Ayton and P. Whalley, A general-purpose computer aid to judgemental forecasting: Rationale and procedures, Decision Support Systems (1985) 1, 333–340.
