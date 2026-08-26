---
otero_id: 23470
otero_key: "JVANFCHT"
title: "A critical look at expert systems for business information applications"
authors: "Pamela K Coats"
year: "1991"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1991.35"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A critical look at expert systems for business information applications

PAMELA K. COATS\*

Department of Finance, Florida State University, USA

Abstract: This paper argues that, contrary to the expectations of researchers, academics and practitioners, current expert systems (ES) for business information and decision making applications are actually quite primitive and fall disturbingly short of claims of intelligence. The focus of the article is a discussion of the problems with expert systems and a realistic assessment of the narrow spectrum of ES successes. The problems seriously detract from the prospects of expert systems as practical enhancements to most present-day business information systems.

## Introduction

Increasingly, the technical term ‘expert system’ is appearing in business information journals and magazines. According to these sources, expert systems (also called intelligent or knowledge-based systems) can do remarkably sophisticated tasks with reliable success. Unfortunately, such a view, in most cases, naively oversells today’s expert systems. The purpose of this article is to address the distinct handicaps inherent in the emerging field of expert systems and to provide realistic estimates of the current capabilities that expert systems hold for business information systems.

## Expert systems

As the name implies, an expert system (ES) is expected to perform a difficult task or resolve a substantial problem well. Expert systems are usually described by eight ideal characteristics:

(1) they solve complex problems as well as or better than human experts;

(2) they reason using what experts consider to be effective heuristics;

(3) they manipulate and reason about symbolic descriptions;

(4) they can function with data which contain errors, using rules which can handle uncertainty;

(5) they can contemplate multiple, competing hypotheses simultaneously;

(6) they can justify why they are asking a question;

(7) they can justify their conclusions;

(8) they interact with humans in appropriate ways, including natural language.

An overview and discussion of expert systems can be found in many papers and books (e.g. Hayes-Roth et al., 1983; Silverman, 1987). Briefly and simply, an expert system is computer software. Unlike traditional computer programs, however, an ES (1) manipulates symbols (words, phrases, complex formulas) in addition to numbers, and (2) processes using rules of symbolic inference rather than sequential mathematical calculations. An ES computer program, called an ‘inference engine’, mimics the organizational, interpretational and scheduling techniques that human experts have internalized for using knowledge to solve a particular problem. The inference engine drives the decision process using a ‘knowledge base’ for reference. A knowledge base is a formal structure of associated information (e.g. facts, relationships, rules, heuristics and situational patterns) unique to the problem at hand. The distinct, bounded field of knowledge for the problem is known as the ‘domain’. For reference, a chart of an expert system’s composition and a summary of its intended functioning appear in Figure 1.

Arthur D. Little predicted that US corporations would be spending \$1.25 billion annually on expert systems by the end of 1991. Sperry Corporation's research estimated industry sales to be closer to \$4 billion a year by this date.

Roughly 50% of the Fortune 500 firms are currently investing in ES tools, and about 10% have applications under development. Most of these are in science, medicine, engineering and the military. However, the list of documented business applications has been growing since 1980. These efforts are essentially experiments or simple prototypes.

From these pioneer efforts, a variety of benefits are alleged:

<table><tr><td>DOMAIN KNOWLEDGE BASE</td><td>INFERENCE ENGINE</td></tr><tr><td>Represents available knowledge as rules, facts, patterns, relationships and heuristicsDerived from experts, research, literature, databases, textbooks and simulation modelsContains metaknowledge (rules about how to use knowledge)</td><td>Schedules and controls the selection process of when and in what order to invoke the rules that pertain to the solution of the problemInterprets domain knowledgeExplains how the system arrived at its conclusion</td></tr></table>

![](/api/attachments/JVANFCHT/fulltext/images/fd2c21842b603fd7ebec9613427ac44b2d8a3b56178e49db5d7bdbb9d0ea64dc.jpg)  
Figure 1 Expert system operation

(1) improved decision making;

(2) more consistent decision making;

(3) reduced decision making time;

(4) improved training;

(5) better use of expert time;

(6) improved service levels;

(7) capture of rare or dispersed knowledge.

Negative effects or unsuccessful efforts are almost never reported.

## ES features

To be fair, even the most severe critics of ES seem to think that the business community could be one of the more promising commercial application areas for ES. The features of ES which might be suited to business information problems are as follows.

Pattern recognition, using sophisticated heuristic search strategies to distinguish trends that may be subtle or be obscured by the sheer volume and diversity of information available.

Understanding of prose material, which is usually subjective or soft data handled at a conceptual level. This includes the ability to converse interactively with a user in an unstructured natural dialogue format.

Ability to explain the path of reasoning used and rephrase material without losing the original contextual meaning. Tracing its own logic is considered critical for developing and validating ES software, as well as gaining the confidence of users and training future experts.

Ability to represent the uncertainty of an imprecise situation and the probability that the advice/forecast given is appropriate.

Ability to learn and make inferences through deductive and inductive reasoning, as well as by being told.

Ability to process and remember large amounts of information.

The expectations for ES look impressive.

## Problems with expert systems

However, a different story begins to emerge when we look at the accumulating disillusionment of users, developers and investors who have first-hand experience with trying to launch business expert systems for commercial use. One such commercial developer estimates that in today's environment there are 100 ES failures for every one success. In general, the stocks of software companies that produce business ES products have performed very poorly (Simon, 1987).

While there are some situations for which expert systems are actually helpful, expert systems in the main have serious problems with methodology, coding and knowledge acquisition. Too many unresolved theoretical issues, computer limitations and people problems exist.

Moreover, many ES applications fail simply because momentum, enthusiasm, competitive pressure or need swept management past a frank analysis of the suitability of their problem for ES. Even projects that are suitable may not survive the high costs, long development times, insufficient validation or the realization that the final product turns out to be unusable.

These problem areas as they relate to business information applications are discussed below.

## Methodology

Production rules (the 'IF [conditions] THEN [actions]' form of knowledge representation that is the foundation of most business information expert systems) were invented and vigorously explored by the business programming community in the 1960s. Rules were eventually abandoned as clumsy, resource-hungry, and unsuitable for complex applications (Martins, 1984). Today's systems are essentially based on those same 25-year-old programming techniques, resurrected only because computing power has become cheaper. However, according to pre-eminent authorities like Marvin Minsky of MIT and Roger Schank of Yale, the methodology remains clumsy and unsuitable. They argue that enthusiasm for the present technology is quite unfounded (Alexander, 1984).

## Code

Expert system code for real world applications is generally not easy to understand, debug, extend or maintain. Very much like BASIC, rule-based languages (e.g. PROLOG) present a superficial appearance of simplicity and transparency. However, just as with BASIC, these illusory qualities rapidly vanish for applications of more than trivial complexity (Martins, 1984). Also, many languages do not provide for adequate user interfaces (Waterman, 1986).

## Unresolved theoretical issues

Business expert systems presently in operation work with essentially closed knowledge bases. Automatically learning new information (Bramer, 1982) and refining existing information on the basis of experience gained (i.e. accumulating 'case lore') (Buchanan and Shortliffe, 1985) are virtually untried areas (Schank, 1984) and we are still very far (i.e. 15–50 years) from cracking them (Schank, 1984). This is a serious handicap to any ES targeted at environments where information is constantly churning, like the exchange markets (stocks, options, futures, etc.). An example is the case of the Digital Equipment Corporation's XCON, probably the most extensively tested (for nine years) ES in commercial use. XCON operates in a structured, relatively restricted 10 000 rule domain to help salesmen configure computer systems for clients. The company spends \$2 million a year just to keep XCON manually updated (Simon, 1987), yet it still does not contain all the knowledge it needs. From this, Luconi et al. (1986) conclude, "it appears much less likely that we will ever be able to codify all the knowledge needed for less clearly bounded problems like financial analysis."

Even when knowledge bases grow by being told rather than by learning, there are almost always stability problems. Preventing contradictory items of knowledge from entering the knowledge base is extremely difficult (Bramer, 1982). In real life, ES rules are not independent chunks of expertise; they quickly become highly independent, often in subtle ways. Adding new rules to a large rule-based program nearly always requires revision of the control variables and left-hand side conditions of earlier rules, and it is often far from obvious just which of these will need fixing to make the new rule work (Martins, 1984). Theoretically, an ES can explain its own behaviour by tracing its inference chains, i.e. the paths of rules it has executed. For toy problems with shallow inference chains, this may aid in updating, debugging, and validating, but on problems of realistic complexity with complicated and lengthy inference chains, like planning tax strategies or analysing consumer preference surveys, the trace itself can be a frustrating source of confusion (Martins, 1984). No generalized technique for logically analysing an ES's completeness and consistency has been developed as yet (Sheil, 1987; Waterman, 1986).

Another problem is setting default assumptions for incompletely specified domains. Deductions may need to be made which are consistent with the available information but are not provably correct, and may in fact turn out to be incorrect in light of information subsequently obtained (Bramer, 1982). For all the claims and expectations to the contrary, expert systems cannot really deal with erroneous, inconsistent or incomplete knowledge because most expert systems rely on rules that represent abstracted knowledge of the domain and thus the expert systems are not able to reason from basic principles (Waterman, 1986).

Fourth, exhibiting common sense is a huge stumbling block for expert systems. Because of the enormous quantity of such knowledge, there is no easy way to build it into a single domain ES (Waterman, 1986). Educated estimates indicate it would take millions of idiosyncratic rules. Most of those rules have not been articulated well enough to convey to other human beings, much less computers, and there are no signs that this limitation will be transcended soon (Alexander, 1984). Even what seems to be trivial common sense can be overlooked. In its early field tests, a Ford Motor Company ES designed for credit analysis of routine car loans failed to question an application from a 20-year-old who claimed 10 years of experience (Simon, 1987).

Fifth, most expert systems do not degenerate gracefully; that is, they cannot recognize when a problem is outside their expertise. This is related to the problem above in that common sense also means identifying what is not known. At the boundaries of their expertise expert systems become suddenly fragile, incapable, and usually ridiculous rather than gradually less proficient at solving problems (Buchanan and Shortliffe, 1985).

Sixth, most business problems, even though of a single domain, still require more than one knowledge representation protocol (e.g. frames, production rules, or object-attribute-value systems). Blending these methods such that processing can skip nimbly from one to another is not yet feasible (Waterman, 1986).

Seventh, little agreement exists among ES researchers on the relative utility of the psuedoprobability (e.g. certainty factors) and fuzzy logics employed to represent uncertainty when data are incomplete or when strictly numerical solutions would be difficult or nonsensical to achieve. The common failing is the extreme dependency on metaknowledge (rules about how to use knowledge) to do things that human experts would do in uncertain situations (e.g. correct data, revise assumptions or combine evidence). However, metaknowledge is another essentially unresearched area of expert systems because of our lack of understanding of how humans deal with incomplete data, make decisions quickly or react smoothly to unforeseen circumstances (Alexander, 1984). This suggests that business risk assessment expert systems, such as insurance underwriting and credit scoring, are not using 'expert' knowledge in a fashion significantly different from traditional probability-based computer programs.

Finally, conversational-quality dialogues, i.e. natural language, between user and ES are not materializing at a satisfactory level of sophistication; nor is the ability to read and understand conceptually complex prose material (Barr and Feigenbaum, 1981; Waterman, 1986). For example, Security Pacific Corporation's attempts to build an ES for foreign exchange trading have reached a dead end because the system cannot evaluate the emotional content of news wire stories in terms of its relative impact on interrelated currencies (Simon, 1987). Reading requires an understanding of what to store, what to forget, and how prior knowledge can be modified by new information, but this kind of understanding requires interdisciplinary knowledge spanning many domains. For the foreign exchange trading ES, that means having knowledge on domains from armaments to the Middle East situation, from dissident ballet dancers to the economics of grain exports. Having multiple domains, in turn, effectively requires the ability to learn. We are thus back to the learning problem again (Schank, 1984).

## Computer limitations

Most expert systems and shells are slow in performing numerical calculations because they run on specialized hardware (like Vax and Symbolics), designed primarily to do non-procedural symbolic reasoning. A few ES applications run on microcomputers, but this adaptation is more for convenience than suitability, and efficient execution is always compromised because of concessions to the equipment.

Moreover, interesting problems that require even minimally sophisticated knowledge representation also require massive processing power. The situation might be partially relieved by the advent of parallel processing, where more than one computer (sometimes thousands) work simultaneously on a problem. But this technology is experimental and very expensive.

## Knowledge acquisition

By far the majority of effort, time, and expense in expert system development comes in deciding what knowledge should be encoded into the knowledge base and inference engine. Programmers (or knowledge engineers) spend weeks, months, sometimes years, with the experts (e.g. seven years in the case of MYCIN, a landmark medical ES Buchanan and Shortliffe, 1985)) coaxing them to articulate the objective and subjective factors, rules, and thought processes used in problem solving.

The process is dependent on the methods developed from cognitive science of revealing human knowledge structures. According to Olson and Reuter (1987), there are two classes of investigative methods: (1) direct – asking the experts to report on knowledge they can articulate explicitly (e.g. by interviews, questionnaires, observations of task performance, thinking-out-loud protocols, and drawing causal relationship diagrams); and (2) indirect – collecting the experts' responses to a variety of rating, scaling, ordering, and clustering problems, and inferring what the experts must have known in order to respond the way they did. Binbasioglu and Jarke (1986) note that to date, Bouwman (1983) offers one of the few descriptions in the literature of a way to extract a business knowledge base from an experienced analyst.

The stark fact is that extracting knowledge from the experts presents a serious bottleneck (Sacerdoti,

1991). Too often key knowledge is so ingrained that experts use it implicitly, but cannot explain it. They find it difficult to put hunches and instinctive feelings into words and rules (Corcoran, 1991). This leaves the ES incomplete and ill-defined (Waterman, 1986). Moreover, when several experts are used, the knowledge base must be checked for contradictions. Also, knowledge engineers still do not know how to reconcile differing or conflicting views among acknowledged experts (Lin, 1986). Some people think these problems may eventually be resolved by 'teaching' the system to use inductive learning (IL). IL techniques seek to automatically infer an operational rule by distilling the common factors inherent in examples of good domain decisions (Buchanan and Shortliffe, 1985; Michalski, 1983). However, again, learning capabilities of current systems are at best superficial (Hoffman et al., 1986) and more often considered non-existent (Barr and Feigenbaum, 1981; Winston and Prendergast, 1984).

## People problems

For an ES to exist presupposes the existence of some recognized human expertise for the ES to emulate. However, it is rare to find more than a handful of truly talented individuals (and sometimes even one) able to solve any given non-trivial business problem. For example, lack of acknowledged investment expertise forced a leading ES software house to scratch its plans for a portfolio management and stock selection system (Schank, 1984). Or sometimes a business practitioner is very successful primarily because of personal traits that cannot be reproduced by a machine. Take the case of an investment banker who trades on his uncanny ability to negotiate deals, make valuable contacts, and just generally be creative. In addition to just finding someone who is suitable, a designated expert has to be available, willing, and able to share his or her skill and knowledge, usually over a long period of time and often in quite arduous and frustrating debriefing sessions (Waterman, 1986).

Also, there is a marked scarcity of ES knowledge engineers, as noted by Minsky (Winston and Prendergast, 1984). Large companies and government agencies seem to be absorbing the people who have done the pioneering ES research. These people are now working on proprietary products, and their results are not being widely shared. There is concern that this is crippling university-sponsored ES research and teaching, and stunting the general advancement of the field (Buchanan, 1986; Schank, 1984; Winston and Prendergast, 1984).

Finally, exaggerations and inaccuracies in the recent burst of media attention to business expert systems have caused unrealistic expectations. That, in turn, has led to disappointment and disillusionment with expert systems. Business expert systems are being naively oversold and the resulting backlash has hindered progress (Buchanan, 1986; Luconi et al., 1986; Simon, 1987; Waterman, 1986).

## Picking the wrong problem

ES scientists find it difficult to describe the exact characteristics that makes a problem a good candidate for ES development. However, experience with expert systems has led researchers to simple guidelines that they think improve the chances of filtering out poor candidates before a serious commitment of time or resources is made. Poor candidates seem to be ones where the following occurs.

(1) The problem definition is elusive or ill-structured. Applications need clear boundaries, for example tax advising (Connell, 1987) is a bounded domain, strategic planning (Goul, 1987) is not.

(2) No one has consistently mastered the task. Without standard cases, knowledge cannot be formulated or validated (Liang, 1988).

(3) Conclusions or solutions are based on many factors not well enough understood to be explained (Goul, 1987), e.g. dividend policy models are too controversial and incomplete, while designing executive compensation plans would be well enough understood.

(4) Conclusions or solutions are based on many factors that are inherently unpredictable, like forecasting the cash flows from venture capital projects. The cash flows for the lease analysis of computer equipment are comparatively more predictable.

(5) The problem requires representation of temporal or spatial knowledge (Beckman, 1991). It takes huge amounts of memory to keep track of varying interrelated time periods and physical locations. So far, big knowledge bases, like time series stock market data, have proven too costly and error prone (Corcoran, 1991; Liang, 1988).

(6) The cost of a bad decision is extremely high.

(7) The task requires common sense (Beckman, 1991). For example, expert systems used to forecast the likelihood of default for loan applicants cannot yet form or integrate judgements about character (Alexander, 1984).

(8) Conventional programs are adequate for the application (Beckman, 1991).

## Cost and time

Even when the task is appropriate, the effort may not be justified. Expert systems cannot yet be built quickly. It usually takes a minimum of two person-years to build an ES to do very simple, well-understood tasks (Waterman, 1986); 40 person-years to build expert systems to do somewhat difficult tasks (Abdolmohammadi, 1987). Data from existing business expert systems, though meager, seem to suggest that even in the best cases, at least five person-years are necessary before an ES begins to perform tolerably (Winston and Prendergast, 1984). One survey indicates that the average cost for developing a system is \$700 per rule, excluding the costs of hardware, software tools, and the time experts contribute to the knowledge base (Fried, 1987). Present expert systems can employ from 50 to 10 000 rules, and in most problems of any significance, the '80/20 syndrome' appears to emerge. That is, a large proportion of the knowledge may be represented by a small number of rules, but the representation of the final portion of knowledge will require a significant effort (Connell, 1987; Sacerdoti, 1991). A recent article in Forbes observed that moderately sized ES efforts (maybe 300 rules) typically cost \$250 000 to \$500 000 just to design (Simon, 1987).

In general, one of the following situations must exist before the cost and commitment to build a business information ES might be economically justified (Waterman, 1986).

(1) The task's accomplishment or the problem's solution has an extremely high payoff. One study suggests that forecasting the viability of loan applications over \$100 000 may be worth it, but less than that is definitely not (Johnson, 1986). American Express claims that its Authorizer's Assistant raises a credit authorizer's productivity by as much as 20% and reduces losses from over extension of credit (but the exact financial benefit is undisclosed) (Leonard Barton and Sviokla, 1988).

(2) Human experts are unavailable, e.g. too scarce or too expensive.

(3) An important human expert is being lost to an organization through personnel changes, e.g. retirement, promotion or change of employers.

(4) The identical expertise is needed in many locations.

(5) Expertise is needed in a hostile environment.

Even in these situations, it is unusual to find a documented instance where a business ES promotes savings or generates revenues in excess of its development and implementation costs (Barr and Feigenbaum, 1981)

## Validation

There is often pressure to hurry or omit the validation process. This is because expert systems which finally get to the validation stage have already cost a lot and probably have taken more time than expected.

Shortchanging the validation process is tempting, but it can lead to costly failures when the ES eventually reveals that it cannot be trusted.

As with traditional model building, the methodology surrounding the validation of an ES remains distressingly ill-specified (Sacerdoti, 1991). Leading ES reference works almost uniformly either do not address the topic of validation, e.g. Barr and Feigenbaum (1981), or else broach it in a cursory manner, e.g. Waterman (1986). Regarding the literature on business ES applications, an extensive review reveals a general neglect by authors in discussing their validation approaches, leaving it unclear as to how or whether validation of any rigour was undertaken. Ribar et al. (1991) is an example of one of the few exceptions. In the minimal formal work that has been done, the focus of validation efforts is on answering the question Does the system produce the same decision as the expert when given a particular problem? There has been virtually no attempt to validate business systems by addressing the question Does the user of the ES make better decisions by using it? (Goul, 1987).

## Usefulness

Finally, an ES that successfully runs the gauntlet of inadequate technology, cost, time and validation, may have made so many concessions along the way that the results it produces are so trivial, general or superficial as to have no real usefulness. This is a particularly likely outcome for applications using off-the-shelf or turn-key systems without customization.

## Characteristics of successful ES

When we eliminate all the applications and problems in business information systems that either do not fit the nature of a successful ES domain, or do not meet the payoff criteria or usefulness test, only a small collection of tasks remain.

A review of successful ES given today's technology reveals some interesting common characteristics (Beckman, 1991; Winston and Prendergast, 1984):

(1) there are recognized experts who are provably better than amateurs;

(2) the task requires only one small low-level closed domain where the rules are static, i.e. a highly specialized or extremely narrow problem (Beckman, 1991; Schank, 1984; Sheil, 1987).

(3) the task is cognitive rather than physical (Beckman, 1991);

(4) the task takes an expert a few minutes to a few hours;

(5) the skill is routinely taught to novices, which means the experts are accustomed to explaining themselves;

(6) the task domain has a high payoff;

(7) the task requires no common sense (Beckman, 1991);

(8) the cost of a bad decision is not high.

Not much more can be accomplished without advances in ES technology, and researchers working on the major stumbling blocks conservatively estimate that ground breaking advances are at least a decade away. Some believe substantial progress may be as much as 50 years in the future, if, indeed, such systems can be built at all (Schank, 1984).

## Appropriate tasks

So, the question is, 'what kinds of business information tasks would you entrust to a literal-minded, by-the-rules person who needs explicit instructions about everything, even though that person possesses a flawless memory and endless patience?'

It looks like the answer is: 'Tasks that are routine, mundane and that require only surface understanding, not deep knowledge.' That means concentrating on low responsibility applications in which the consequences of errors are nil, or in which an occasional mistake can be rectified easily. However, the reality of the situation is that most routine decision problems of this caliber can already be solved with much simpler traditional software.

Thus the compromise between the promise and the reality of expert systems seems to be to package them as assistants rather than primary decision makers. This casts expert systems in supportive and subordinate roles that are a good match for the technology's uneven capabilities (Sheil, 1987).

Finally, it seems that the strongest leverage point of existing business expert systems is repetition. Successful expert systems primarily structure repetitive tasks. In general, expert systems monitor and guide users through an established pecking order of considerations, collect responses to queries they make, and impose uniformity and thoroughness on the process (e.g. assessing loan applications, setting up capital budgeting scenarios, planning the effects of financial product mixes). Such expert systems principally rely on storage, retrieval, comparison, computation and natural language processing which, though relatively primitive, make the expert systems look more intelligent than they are. What expert systems offer over and above traditional methods right now is the illusion and promise of expertise, not real capabilities.

## Conclusion

Possibly the most candid summary of the current state of the art in expert systems comes from the chief scientist at the Atari Corporation. He labels it “stuff that is interesting that we do not know how to do yet." (Waterman, 1986). In fact, for business information systems, the most valuable feature of the present ES methodology may not even show up in an ES's operation, but rather in its development. Human experts, in attempting to produce an ES, are forced to disassemble and examine their experiences and thought processes in detail. They must reconsider 'what' they know and 'how' they know it. Over time, the discipline of this activity may spur innovative associations and promote insights and understanding that improve our current techniques of handling information (Beckman, 1991; Corcoran, 1991; Martins, 1984; Leonard Barton and Sviokla, 1988; Schank, 1984).

## References

Abdolmohammadi, M.J. (1987) Decision support and expert systems in auditing: a review and research directions. Accounting and Business Research, Spring, 173–184.

Alexander, T. (1984) Why computers can't outthink the experts. Fortune, 20 August, 105–118.

Barr, A. and Feigenbaum, E.A. (eds) (1981) The Handbook of Artificial Intelligence, Volume I (Addison-Wesley, Reading, MA).

Beckman, T.J. (1991) Selecting expert-system applications. AI Expert, 6, 42–48.

Binbasioglu, M. and Jarke, M. (1986) Domain specific DSS tools for knowledge-based model building. Decision Support Systems, 2, 213–223.

Bouwman, M.J. (1983) Human diagnostic reasoning by computer: an illustration from financial analysis. Management Science, June, 653–672.

Bramer, M. (1982) A survey and critical review of expert systems research, in Introductory Readings in Expert Systems, Michie, D. (ed) (Gordon and Breach, New York).

Buchanan, B.G. (1986) Expert systems: working systems and the research literature. Expert Systems, 3, 32–51.

Buchanan, B.G. and Shortliffe, E.B. (eds) (1985) Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project (Addison-Wesley, Reading, MA).

Connell, N.A.D. (1987) Expert Systems in Accountancy: A Review of Some Recent Applications. Accounting and Business Research, Summer, 221–233.

Corcoran, E. (1991) Sorting out chaos on Wall Street. Scientific American, June, 121.

Fried, L. (1987) The dangers of dabbling in expert systems. Computerworld, 29 June, 65–72.

Goul, M. (1987) On building expert systems for strategic planners. Information and Management, November, 131–141.

Hayes-Roth, F., Waterman, D. and Lenat, D. (1983)

Building Expert Systems (Addison-Wesley, Reading, MA).

Johnson, B. (1986) A survey of current AI applications in business. Research paper for Arthur Anderson and Company.

Leonard Barton, D. and Sviokla, J.J. (1988) Putting expert systems to work. Harvard Business Review, March/April, 91–98.

Liang, T. (1988) Expert systems as decision aids: issues and strategies. Bureau of Economic and Business Research Faculty Working Paper No. 1378, University of Illinois, Urbana-Champaign.

Lin, E. (1986) Expert systems for business applications: potential and limitations. Journal of Systems Management, July, 18–21.

Luconi, F.L., Malone, T.W. and Scott Morton, M.S. (1986) Expert systems: the next challenge for managers. Sloan Management Review, Summer, 3–14.

Martins, G. (1984) The overselling of expert systems. Datamation, November, 76–80.

Michalski, R.S. (1983) A theory and methodology of inductive learning, in Machine Learning, Michalski,

R.: Carbonell, J. and Mitchell, T. (eds), (Tioga Publishing Co., Palo Alto, CA).

Olson, J.R. and Rueter, H.H. (1987) Extracting expertise from experts: methods for knowledge acquisition. Expert Systems, August, 152–168.

Ribar, G., Arcoleo, F. and Hollo, D. (1991) Loan probe: testing a big expert system. AI Expert, 6, 43–49.

Sacerdoti, E.D. (1991) Managing Expert-System Development. AI Expert, 6, 26–33.

Schank, R.C. (with Childers, P.) (1984) The Cognitive Computer (Addison-Wesley, Reading, MA).

Sheil, B. (1987) Thinking about artificial intelligence. Harvard Business Review, July/August, 91–97.

Silverman, B.G. (ed) (1987) Expert Systems for Business. (Addison-Wesley, Reading, MA).

Simon, R. (1987) The morning after. Forbes, 19 October, 164–168.

Stansfield, J.L. and Greenfield, N.R. (1987) PlanPower: a comprehensive financial planner. IEEE Expert, Fall, 51–59.

Waterman, D.A. (1986) A Guide to Expert Systems (Addison-Wesley, Reading, MA).

Winston, P. and Prendergast, K. (1984) The AI Business: Commercial Uses of Artificial Intelligence (The MIT Press, Reading, MA).

## Biographical note

Pamela K. Coats is a professor of finance at The Florida State University. She teaches seminars in computer modelling for financial decision support and her current research is in neural networks.

Address for correspondence: P.K. Coats, College of Business, Florida State University, Tallahassee, FL 32306-1042, USA.
