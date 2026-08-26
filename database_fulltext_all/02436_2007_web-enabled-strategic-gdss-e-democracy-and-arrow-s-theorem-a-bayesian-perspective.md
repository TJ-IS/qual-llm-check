---
otero_id: 2436
otero_key: "QY8QGJV6"
title: "Web-enabled strategic GDSS, e-democracy and Arrow's theorem: A Bayesian perspective"
authors: "Simon French"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.06.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Web-enabled strategic GDSS, e-democracy and Arrow's theorem: A Bayesian perspective

Simon French

Manchester Business School, University of Manchester, Booth Street West, Manchester, M15 6PB, UK

Accepted 9 June 2006

Available online 24 July 2006

## Abstract

Web-technologies bring the possibility of supporting geographically and temporally dispersed decision making. However, although technically feasible, it is not clear that there are valid methodologies for the use of web-based group decision support (wGDSS). Many approaches to decision support are driven by the perspective of a single decision maker. Yet there are many reasons to expect that the extension of individualistic theories to a group context will be fraught with difficulty. This paper explores these issues and considers the way forward for the design and use of wGDSS and for a more substantive approach to participative e-democracy.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Arrow's impossibility theorem; The Bayesian paradigm; Group decision support systems (GDSS); e-democracy; Procedural and substantive democracy; Societal decisions

## 1. Introduction

The advent of web-technologies has brought the possibility of supporting geographically and temporally dispersed decision making. Technically it is now possible to discuss issues, debate objectives, formulate problems, access data, analyse models, conduct sensitivity analyses, vote, decide and implement actions, all without the group meeting other than virtually. However, many approaches to supporting decision making are driven by the perspective of a single decision maker (DM), e.g. the Bayesian model of rationality in statistics, cost benefit analysis from economics, or data mining and artificial intelligence (AI) algorithms from computer science. Yet we have the authority of Arrow's Impossibility Theorem and many other similar results to expect that the extension of these individualistic theories to a distributed group context will be fraught with difficulty. This paper explores the implications of Arrow's result for the design and use of distributed or web-enabled group decision support (wGDSS) and for a more substantive approach to participative e-democracy.

The range of group decision making in our society is enormous: families come together to plan their holidays; management teams address issues within their organisations; boards of directors chart a company's strategy; councils, parliament and cabinets run our countries, elected to do so by all (adult) citizens; and so on. For many years now, decision support systems (DSS) have been developed to help DMs address different decision contexts [42,55,58,64], those supporting groups mainly focusing on smaller groups that come together into the same room to take a decision: see, e.g., Ref. [47]. Now, however, Internet and Web technologies allow the development of distributed DSS to provide support to groups who may seldom or never meet and take their decision through processes mediated through time and space by technology. Moreover, the pressures of modern life – conflicting, overfull diaries, on one hand, and globalisation with distributed teams, on the other – make such distributed decision making very attractive. However, the existence of such technologies along with the need for them does not imply that they will, in fact, support valid decision processes. Indeed, even the concept of validity is not well established in this context. I am thinking particularly here of strategic, unstructured decision making, rather than repetitive, well structured operational contexts [59]; but, of course, the greater power and creativity of groups is usually reserved for just such strategic contexts.

Furthermore, web-technologies offer the possibility of supporting much larger groups, indeed, whole societies. Democratic processes can be web-enabled; and there are many developments in e-democracy, driven by calls for greater participation. Most democracies are procedural: there are procedures for electing representatives which are accepted as democratic; the elected representatives then take the decisions on behalf of society. But technologies now offer a way forward towards a much more substantive, direct, or deliberative implementation of democratic ideals. It is now possible for the public to be involved in societal decision making in much more direct ways. But again the existence of a technological way forward does not necessarily mean it is a valid way forward.

In this paper we explore the implication of some old, but often ignored results from voting theory and social choice to suggest that GDSS and especially wGDSS require much more sensitive, less algorithmic approaches to decision support that DSS builds for individual DMs. We begin in the next section with a brief reference to Arrow's Impossibility Theorem and related results. Next we turn to the development of the Bayesian paradigm for decision support and analysis. This paradigm is adopted in the paper because of my familiarity and adherence to it; but it should be emphasised that the underlying issues that we address affect all such paradigms. There is no escape by simply resorting to other approaches such as analytic hierarchy processes, fuzzy methods, multi-criteria decision aid, or whatever. Our discussion suggests that wGDSS needs to address problems of communication and explanation much more than algorithmic details of voting rules. Thus we turn, first, to the design of human-computer interfaces (HCI) in wGDSS for smaller teams and groups and, secondly, to similar, but much more difficult issues that arise in substantive e-democracy.

The purpose of this paper is not to introduce new theory, but to suggest that failure of GDSS designers to address the implications of some quite old results may lead to the development of some quite inappropriate tools.

## 2. Arrow's Impossibility Theorem

The literature of voting systems, group decision making, social choice and game theory is peppered with discoveries of paradoxes, inconsistencies and impossibility results [5,6,17,21,22,28,31,36,40,44,53,62,63,66]. Perhaps Arrow's Impossibility Theorem [4,36] is the most celebrated result, but it only one of many that show it is far from easy to combine principles of rational decision making with those of democracy. Essentially, no constitution for group decision making exists such that the members of the group can be assured that in every possible circumstance it satisfies some basic principles of rationality, unanimity and Pareto optimality, and independence of irrelevant alternatives without there being an explicit or implicit dictator.

Since Arrow proved his uncomfortable result, many have tried to reframe his assumptions slightly to avoid the impossibility or to argue that one or more is irrelevant to democracy and can therefore be dropped. All have essentially failed. Worse: it transpires that versions of the impossibility hold even if any one of the axioms is abandoned [36]. Arrow has identified a real inconsistency in our hopes and demands for democratic rational decision making. Others have enlarged the debate and shown that any constitution is susceptible to manipulation through strategic voting, dishonest revelation of preferences or agenda rigging [22]. Perhaps the most hopeful way forward seems to be to allow the group members to express not just their preference rankings but also their strength of preference. But while there are a number of mathematical results which offer some hope, e.g. [5,21,22,28,54], all fail because they require an interpersonal comparison of preferences: namely, an unambiguous interpretation of “I prefer coffee to tea more than you prefer a sports car to an mpeg player”. Koning [39], for instance, has recently proposed a fuzzy approach which looks promising, but on closer examination it requires that the set membership functions of the group members are assessed on a common scale: i.e. he assumes that they are interpersonally comparable. Venturing outside the research domains of social choice and voting theory does not increase optimism either: game theory and negotiation theory are just as full of contradictions and counterexamples [13,38, 40,54]. However one formulates the issues, there seems to be no way to develop mechanistic algorithms and prescriptions for voting and group decision making that are fair, just, democratic, honest, open, … — choose your adjective embodying a good moral imperative!

In addition to the references cited above, general introductions to theories of voting and democracy are provided by Taylor [62] and Tulloch [63]. A recent special issue of the Journal of Multi-Criteria Decision Analysis discusses many of the wider issues relating to the use of decision analytic ideas in substantive edemocracy [25].

## 3. The implications of Arrow's result for the Bayesian paradigm

As indicated above, the general thrust of the argument in this paper has relevance to all paradigms for decision analysis and support. However, for concreteness and because of my adherence and familiarity with the paradigm, I shall focus mainly on the Bayesian and then draw out the general issues in the concluding discussion. One can discern five distinct phases in the development of the Bayesian approach.

The first phase occurred in middle decades of the last century with the development of the underlying axiomatic basis and motivation of the Bayesian subjective expected utility (SEU) model $[ 1 4 - 1 6 , 4 0 , 5 6 , 6 6 ]$ . This theoretical work essentially sought to characterise rational beliefs, preferences and decisions, including the consistency that one would expect of these. Details are given in the references, but essentially the work showed that if one made assumptions about the way in which a rational DM organised her beliefs and preferences and further assumed that she would choose between actions in a manner consistent with these, then her preference between any two possible actions, $a _ { 1 }$ and $^ { a _ { 2 } , }$ could and should be modelled by an expected utility ordering, $E _ { \theta } [ u ( a _ { 1 } , \theta ) ] \ge$ $E _ { \theta } [ u ( a _ { 2 } , \theta ) ]$ , where $u ( a , \theta )$ represents her preferences for the consequences of the action a and the state of the world is θ, the expectation being taken with respect to her subjective probability distribution for the unknown θ.

At its heart the Bayesian paradigm is essentially an individualistic one. It models the behaviour of a rational DM. Since all thinking and analysis take place within one individual and are based solely on her judgements, there is no necessity to consider communication and truthfulness. She knows what she is thinking and the theory assumes that she does not lie to herself, either consciously or subconsciously.

Edwards [19] in a seminal paper raised the question whether people really did choose as the SEU model suggested and so founded behavioural decision science, which over the last half century has essentially answered this question negatively. Intuitive decision making generally does not follow the Bayesian paradigm closely [7,33,35,67]. During the same period there have been long debates about the interplay between normative modelling – suggesting how DM should act – and descriptive modelling — characterising how they do [8,27,28].

During the late 1950s and throughout the 1960s with the growing recognition of the gap between the SEU model and DMs' actual behaviour, the methodological foundations of decision analysis were laid, so signalling the second phase in the development of the Bayesian approach [45,51,52,57]. The methodology still focused on a single DM who worked with an analyst to deliberate and decide. The analyst adopted a role similar to a psychotherapist, in that he used the SEU model together with behaviourally sensitive elicitation techniques to reflect the implications of the DM's thinking back to her. While there were communication issues in that the DM and analyst needed to find a common language, they could work together to achieve this. The approach here is now often referred to as prescriptive decision analysis in that it seeks to guide DMs towards the ideals encoded by normative theories within the context of a real, often ill-defined problem, mindful of their cognitive characteristics [8,27,28].

The third phase in the development occurred in the theoretical domain with many attempts to develop a normative theory of group decision making which paralleled the individualistic SEU model. As we have noted in the previous section this effort was ultimately unsuccessful: Arrow had and has identified very real paradoxes in our ambitions for group decision making. Nonetheless, for thirty years or so from Arrow's first publication of his result and contemporary failures to find acceptable solutions to co-operative n-person games through to the early 1980's, researchers struggled to find a way forward. Ultimately, however, the majority accepted the inevitable and recognised that any concept of group decision making is flawed and ill-defined. Rather researchers and analysts began to look upon groups not as some entity, which possesses the power to decide, but a social process [21,28], which translates the decisions of the individual members into an implemented action. Beliefs, preferences, logical analysis, all reside in each of the individual's minds not in some disembodied group mind. In their recent paper [17], Dryzek and List argue similarly that that within the wider context of deliberative democracy, the import of Arrow's impossibility is that meaningful democratic decision making will only be ensured if the citizens engage in true discussion and deliberation, seeking out aspects of the particular circumstances of the decision that will allow them to come to agreement.

This recognition led to the fourth phase: the development of decision conferences and analyses for groups of DMs [23,49,50]. In this the role of the analyst in eliciting, building and analysing decision models is complemented by that of a facilitator who works to help the group communicate and build a common understanding. Decision analysis is used both as a tool for individual members to explore their own perceptions of the problem and as a means of communicating their perceptions to each other. Sensitivity analysis becomes a powerful tool to enable members to identify where their differences really matter and where they are unimportant, thus directing and structuring discussion [26]. Communication is key to facilitation, though it does have other purposes in maintaining task focus, etc. Ackermann [1] found that facilitation helped groups to contribute freely to the discussion, to concentrate on the task, to sustain interest and motivation to solve the problem, to review progress and to address complicated issues rather than ignore them; while Phillips [49] emphasises the role of building shared understandings. A further task of facilitation is to engage the group in creativity and problem formulation techniques to help the group bring structure to the issues facing them. See Refs. [18,29,30,34,41,46] for further discussion. In summary, facilitators and analysts attend to the process of decision making, while the DMs concentrate on the issues themselves. Notice that facilitators and analysts should not have an interest in the ultimate choice: they should be disinterested so that they are not motivated to distort the process. Their loyalties may be to the group or the sponsor of the analysis, but either way they should be transparent.

Facilitated group decision support today is common and adopts a variety of forms, some using group decision support rooms and video conferencing [2,3,9,18,24,47], but all employing some form of face-to-face contact. We are now entering the fifth phase in the development of Bayesian decision analysis and support — and arguably it is the most difficult. Web and internet technologies allow the face-to-face interactivity of the group, facilitators and analysts to be broken. All interaction may be via text and graphs on computer screens separated in both space and time. If one ignored the implications of Arrow's result, each group member could interact individually and the wGDSS would left to aggregate the group's beliefs and preferences in some way. But we have seen that it risks certain paradox and inconsistencies. The imperatives that drove the development of a group decision process built on facilitation and communication remain and these functions need to be built into wGDSS; and that will not be easy. Moreover, we should not forget the second phase of Bayesian analysis: analysts work individual DMs to explore the issues, elicit judgements in ways that are sensitive to and minimise behavioural biases and generally build the DM's understanding of the decision context and her feelings and judgements relating to it. There is a need to introduce these elements of support previously provided by the analyst into the wGDSS.

In the next section we discuss the challenges for wGDSS for moderate sized groups who may share the common mission and objectives of an organisation to help them toward consensual decision making through shared understandings. In the following section, we focus on the even greater challenges facing the development of substantive e-democracy which must work with all the disparate views, perceptions and values across a society.

## 4. Implications for web-enabled GDSS

While some DSS have been web-enabled [11,12,61], few are true wGDSS designed to tackle unstructured strategic problems; rather they have tended to focus on operational, well structured contexts. As we have suggested, effective wGDSS will need to incorporate substantial facilitation and communication tools. While we might look to AI to provide this functionality and while there has been some preliminary work in this area [37,48,68], we should recognise that facilitation skills are complex and that we are a long way off identifying and documenting, much less replicating such skills automatically [30,41]. This is particularly true in the area of problem formulation, a necessary first step in tackling unstructured strategic problems. While software tools can be used to catalyse the identification of issues (see, e.g., Ref. [43]), drawing these ideas together into one or more useful perspectives on the underlying problem(s) is one of the major tasks left to the facilitator and analyst in decision conferences and analysis. True wGDSS will need to replicate these skills. Problem formulation is a highly creative process and it is in areas related to human creativity that artificial intelligence methods have perhaps made least progress. Thus for the present one must expect that wGDSS will need to use human facilitators and analysts to moderate and manage the deliberations.

Even some of the simpler aspects of decision analysis may be difficult to incorporate into distributed analyses conducted over the web. Consider elicitation of probabilities and utilities and weights. There are many ways in which this may be achieved and most decision analytic software incorporate some visualisation of the these quantities to help, first, in their elicitation and, subsequently, in their presentation. Fig. 1 shows two representations of probabilities. Behavioural studies suggest that different people may perceive the relative likelihoods conveyed by these differently, although the numbers are precisely the same. If a DSS is used by a single individual, this issue may be of minor importance, since the user can explore the software and her own perceptions and then tune in. In group meetings the facilitator can work with the group and help them converge to a common perception of the relative likelihoods, but this usually in my experience takes much discussion and requires the facilitator to recognise body language cues as much as respond to questions from the DMs. Thus the use of such representation within wGDSS may risk different members of the group perceiving data in different ways. Gigerenzer [32] has shown that explicating uncertainties in terms of frequencies may resolve some of the misperceptions risked by representations such as in Fig. 1; but there is no obvious way to use frequency interpretations if the numbers represent preference weights rather than uncertainties.

![](/api/attachments/QY8QGJV6/fulltext/images/17eb0098997bfb9804a912c79f249fddddd511c13682cb778422e74a31ad0b13.jpg)  
(a) Probabilities represented by bar height

![](/api/attachments/QY8QGJV6/fulltext/images/3e258707515ce00aa777f2e6b6681cf1c7f1f40b7af1454b5342d42977c20169.jpg)  
(b) Probabilities represented by area  
Fig. 1. Two representations of the same set of probabilities.

There is a general point here concerning the paucity of work on human computer interfaces (HCI) for DSS. Most HCI studies focus on what might be termed narrow issues such as whether the user can find the appropriate button or menu item efficiently to achieve a desired functionality. But there is a much wider set of issues concerning whether the computer supports the user cognitively in their task and, when that task is embedded in a process, does the computer system effectively support the overall process. Behavioural decision studies suggest that there are many possible pitfalls in interpretation to which DMs may be prone in comprehending descriptions of decision contexts, uncertainties and values. Thus it is very possible that the ‘information’ displayed on a DSS does not truly inform the user.

For instance, one such is framing bias [65]: see Fig. 2. When people are asked to choose between programmes A and B, without being shown options C and D, about 75% prefer A. But when people are presented with the same scenario and asked to choose between programmes C and D, without being shown options A and B, about 75% prefer D. But, of course, the

Imagine that you are a public health official and that an influenza epidemic is expected. Without any action it is expected to lead to 600 deaths. However, there are two vaccination programmes that you may implement Programme A would use a well established vaccine which would save 200 lives. Programme B would use a new vaccine which might be effective. There is a $1 / 3 ^ { \mathrm { r d } }$ chance that it would save all 600 lives and $2 / 3 ^ { \mathrm { r d s } }$ chance of it saving none of them. Programme C would use a well established vaccine which would lead to 400 of the population dying Programme D would use a new vaccine which might be effective. There is a $1 / 3 ^ { \mathrm { r d } }$ chance of no deaths and $2 / 3 ^ { \mathrm { r d s } }$ chance of 600 deaths.

Fig. 2. The influenza example.

choice in each case is the same: programmes A and C are identical in their outcomes as are programmes B and D. There is a general finding that positive framing predisposes individuals to be risk averse, while negative framing predisposes them to risk proneness.

These and many similar results suggest that there are major issues to be considered in the design of the interfaces to wGDSS, otherwise the DMs may misinterpret the analyses and support offered. Remember too that while the discussion here is in terms drawn from the Bayesian decision analysis paradigm, the issues apply mutatis mutandis to all other paradigms. In the case that wGDSS is used within organisations, these issues may be addressed not just by HCI design, but also by training and by repeated common use by the team. It will be difficult but not impossible. My concern is that these issues are hardly recognised in the wGDSS literature — or indeed in the GDSS literature. Much more work is needed than is currently envisaged.

## 5. Implications for e-democracy

It is but a short step from providing wGDSS for small groups of DMs to substantive e-democratic systems which involve the public in an Athenian ideal of societal decision making. The European Science Foundation has established a programme Towards Electronic Democracy (TED), to explore this idea. The TED programme envisages a methodology that is based on a common WWW tool-set to provide decision support and a communications infrastructure to support stakeholder interactions. It recognises that citizens not only wish to be informed about major issues, but wish also to articulate their opinions in a way that can affect the decision making process. The tool-set would support (www.esf. org/ted):

• “identification and structuring of the key issues, providing separate complementary perspectives on the uncertainties and the scale of possible impacts;

• recognition of the various stakeholders and the characteristics of their interests;

• identification of experts who may contribute to understanding the uncertainties;

• construction of an outline analysis, capturing initial perceptions of the problem;

• discussions between stakeholders to explore their perceptions and values;

• construction of a comprehensive analysis drawing together uncertainties and value judgements, including expert advice and different stakeholder views;

• exploration of possible consensus via a comprehensive sensitivity analysis, thus pointing to a balanced decision;

• communication throughout the process with all parties, avoiding the use of fright factors, jargon, paternalistic and other misleading language;

• maintenance of appropriate levels of security, which may vary during the decision making process from complete secrecy to complete openness; and, finally,

• documentation of the process in a way which both explains the rationale behind the final decision and lets all stakeholders explore the decision and understand the reasoning”.

TED's vision is clearly one of substantive or deliberative democracy, in which people participate in societal decisions, not one of procedural democracy, in which people elect representatives to take the decisions for them. But there is no simple dichotomy. There are many visions of substantive democracy, just as there are many forms of procedural democracy; and between substantive and procedural democracies there are a wealth of middle grounds. For instance, ones in which individuals and stakeholder groups may participate in the discussions and processes leading up to a decision, while leaving the ultimate choice to an elected body or a statutory body answerable to an elected one. There are many problems and issues to be addressed before such a vision might be adopted: security, definition of constituencies, accessibility, time and cognitive burdens, motivation and participation, and so on. Here we indicate only those that follow from our earlier arguments.

The import of Arrow's theorem is, of course, just as strong — arguably, stronger. There will be no simple algorithmic implementation of an e-democracy. edemocratic systems will need to focus on fostering good communication, building shared understandings and appreciation of different perspectives. In short they will need to foster deliberation, rather than implement algorithmic decision making [17]. The difficulties in achieving this are far greater than those touched upon in the previous section. While organisations which adopt wGDSS to support distributed decision making may reasonably assume that the DMs share common goals – those of the organisation – and may train and work with the group so that they ‘understand’ the system, such will not be the case for e-democracy. Societies are multicultural and often multi-lingual; their citizens span a vast range of abilities and backgrounds, subscribe to many different worldviews and hold many different values. The literature on risk communication warns us that simply discussing and clarifying the issues in many societal problems will be fraught with difficulty [10,20,60]. Effective decision support requires a broad socio-technical approach which recognises and draws into the analysis and debate all the stakeholders' perspectives, however, disparate. That means it has to provide channels for communicating between scientists and experts, on one hand, and lay understandings, on the other. It has to draw in values from economic and financial theory as well as those arising from a variety of potentially strongly held moral philosophies. Above all, it has to work with the cognitive abilities of the DMs as they are, not as some abstract theory it insists that they should be.

The tension between the imperatives implicit in a decision support methodology and the worldviews of DMs will inevitably lead to difficulties. Whereas an organisation can adopt and insist that a single paradigm is used consistently in all its analyses and decision making, society cannot. To be specific – and this is hard for me! – we need to recognise that not all citizens share the Bayesian ideal and so different decision paradigms will need to co-exist within any e-democracy system. Thus it will not be a short step from the development of wGDSS to e-democracy, and we have noted that the development of valid wGDSS is itself fraught with difficulty. But the web does provide the means to involve citizens more in shaping the society in which they live: to establish some form of substantive e-democracy. That goal does give us reason to tackle the difficulties and develop meaningful processes to draw in their perceptions and values. As Thomas Jefferson said: “I know of no safe depository of the ultimate powers of the society but the people themselves; and if we think of them as not enlightened enough to exercise their control with a wholesome discretion, the remedy is not to take it from them, but to inform their discretion.”

## 6. Conclusion

One might ask what is the purpose of a paper reflecting again on results in group decision making and social choice that have been in the literature for half a century. I have said very little in the above that has not been said before; indeed, I have said much of it before. But while Arrow's Impossibility Theorem and related results are long established, they are also much ignored. I have encountered many designers of GDSS who are completely unfamiliar with the issues. Moreover, it is easy to build and sell GDSS which embody algorithmic voting approaches to constructing group decisions. So there are many systems out there which risk leading their users into paradox, irrationality and inconsistency. For small groups who meet and use the system together, there is some protection offered by their interactions and discussions as they use the system — they have the chance to reflect on the decision before they implement it. However, for spatially and temporally dispersed groups there is less possibility of such reflection. Thus it seems imperative to me that we pause and reflect on how we should design and use wGDSS and e-democracy systems. I hope that this paper has raised some issues that need be considered.

## Acknowledgements

Earlier versions of this paper have been presented at the International Society for Bayesian Analysis Conference held in Valparaiso, Chile in May 2004 and at the 15th Mini EURO Conference on Managing Uncertainty in Decision Support Models (MUDSM 2004) held in Coimbra, Portugal in September 2004. The work has also been stimulated and supported by the European Science Foundation Towards Electronic Democracy Programme (www.esf.org/TED). I am also grateful for the very constructive comments of a referee.

## References

[1] F. Ackermann, Participants' perceptions on the role of facilitators using group decision support systems, Group Decision and Negotiation 5 (1996) 93–112.

[2] F. Ackermann, G.-J. De Veerde, European Research on Group Decision Support Systems, Group Decision and Negotiation 10 (2001) 1–94.

[3] F. Ackermann, C. Eden, Contrasting single user and networked Group Decision Support Systems, Group Decision and Negotiation 10 (2001) 47–66.

[4] K.J. Arrow, Social Choice and Individual Values, 2nd ed., John Wiley and Sons, New York, 1963.

[5] M. Bacharach, Group decisions in the face of differences of opinion, Management Science 22 (1975) 182–191.

[6] M. Bacharach, S. Hurley (Eds.), Foundations of Decision Theory, Basil Blackwell, Oxford, 1991.

[7] M. Bazerman, Managerial Decision Making, 5th ed., John Wiley and Sons, New York, 2002.

[8] D.E. Bell, H. Raiffa, A. Tversky, Decision Making, Cambridge University Press, Cambridge, 1988.

[9] V. Belton, T.J. Stewart, Multiple Criteria Decision Analysis: An Integrated Approach, Kluwer Academic Press, Boston, 2002.

[10] P.G. Bennett, K.C. Calman (Eds.), Risk Communication and Public Health: Policy Science and Participation, Oxford University Press, Oxford, 1999.

[11] H.K. Bhargava, D.J. Power, Decision Support Systems and Web Technologies: A Status Report, 2003 http://dssresources.com/ papers/dsstrackoverview.pdf.

[12] M.-D. Cohen, C.B. Kelly, A.L. Medaglia, Decision support with web-enabled software, Interfaces 31 (2001) 109–129.

[13] A.M. Colman, Game Theory and its Applications in the Social and Biological Sciences, Butterworth-Heinemann, Oxford, 1995.

[14] B. De Finetti, Theory of Probability, vol. 1, John Wiley and Sons, Chichester, 1974.

[15] B. De Finetti, Theory of Probability, vol. 2, John Wiley and Sons, Chichester, 1975.

[16] M.H. Degroot, Optimal Statistical Decisions, McGraw-Hill, New York, 1970.

[17] J.S. Dryzek, C. List, Social choice theory and deliberative democracy: a reconciliation, British Journal of Political Science 33 (1) (2003) 1–28.

[18] C. Eden, J. Radford (Eds.), Tackling Strategic Problems: The Role of Group Decision Support, Sage, London, 1990.

[19] W. Edwards, The theory of decision making, Psychological Bulletin 51 (1954) 380–417.

[20] B. Fischhoff, Risk perception and communication unplugged: twenty years of process, Risk Analysis 15 (1995) 137–145.

[21] S. French, Group consensus probability distributions: a critical survey, in: J.M. Bernardo, M.H. Degroot, D.V. Lindley, A.F.M. Smith (Eds.), Bayesian Statistics, vol. 2, 1985, pp. 183–201, North-Holland.

[22] S. French, Decision Theory: An Introduction to the Mathematics of Rationality, Ellis Horwood, Chichester, 1986.

[23] S. French (Ed.), Readings in Decision Analysis, Chapman and Hall, London, 1988.

[24] S. French, Multi-attribute decision support in the event of a nuclear accident, Journal of Multi-Criteria Decision Analysis 5 (1996) 39–57.

[25] S. French, The challenges in extending the MCDA paradigm to e-democracy, Journal of Multi-Criteria Decision Analysis 12 (2003) 61–233.

[26] S. French, Modelling, making inferences and making decisions: the roles of sensitivity analysis, TOP 11 (2) (2003) 229–252.

[27] S. French, J.Q. Smith (Eds.), The Practice of Bayesian Analysis, Arnold, London, 1997.

[28] S. French, D. Rios Insua, Statistical Decision Theory, Kendall's Library of Statistics, Arnold, London, 2000.

[29] S. French, L. Simpson, E. Atherton, V. Belton, R. Dawes, W. Edwards, R.P. Hämäläinen, O. Larichev, F.A. Lootsma, A.D. Pearman, C. Vlek, Problem formulation for multi-criteria decision analysis: report of a workshop, Journal of Multi-Criteria Decision Analysis 7 (1998) 242–262.

[30] S. French, K.N. Papamichail, R. Snowdon, J.-B. Yang, Facilitation Practices in Decision Workshops. Journal of the Operationa Research Society. (under submission).(2005).

[31] A. Gibbard, Manipulation of voting schemes: a general result, Econmetrica 41 (1973) 587–601.

[32] G. Gigerenzer, Why the distinction between single event probabilities and frequencies is important for psychology and vice versa, in: G. Wright, P. Ayton (Eds.), Subjective Probability, John Wiley and Sons, Chichester, 1994, pp. 129–161.

[33] G. Gigerenzer, Reckoning With Risk: Learning to Live With Uncertainty, Penguin Books, Harmondsworth, 2002.

[34] T.L. Griffith, M.A. Fuller, G.B. Northcraft, Facilitator influence in group support systems: intended and unintended effects, Information Systems Research 9 (1) (1998) 20–36.

[35] D. Kahneman, P. Slovic, A. Tversky (Eds.), Judgement Under Uncertainty, Cambridge University Press, Cambridge, 1982.

[36] F.S. Kelly, Arrow Impossibility Theorems, Academic Press, New York, 1978.

[37] D.A. Klein, Decision-Analytic Intelligent Systems: Automated Explanation and Knowledge Acquisition, Lawrence Erlbaum Associates, New Jersey, 1994.

[38] P.R. Kleindorfer, H.C. Kunreuther, P. Schoemaker, Decision Sciences, Cambridge University Press, Cambridge, 1993.

[39] J.-L. Koning, How electronic voting can escape Arrow's Impossibility Theorem, in: J. Padget, R. Neira, J.L. Diaz De Leon (Eds.), E-Government and E-Democracy: Progress and Challenges, 2003, pp. 138–146, Instituo Politecnico Nacional, Centro de Investigacion en Computacion, Unidad Profesiona “Aldofo Lopez Mateos”, Zacatenco, Mexico.

[40] R.D. Luce, H. Raiffa, Games and Decisions, John Wiley and Sons, New York, 1957.

[41] L. Macauley, A. Alabdulkarim, Facilitation of e-meetings: stateof-the-art review, IEEE International Conference on E-Technology, E-Commerce and E-Service, Hong Kong, China, 2005, pp. 728–736.

[42] G.M. Marakas, Decision Support Systems in the 21st Century, Prentice Hall, Upper Saddle River, New Jersey, 1999.

[43] B. Massetti, An empirical examination of the value of creativity support systems on idea generation, MIS Quarterly 20 (1) (March 1996) 83–97.

[44] I. Mclean, A.B. Urken (Eds.), Classics of Social Choice, University of Michigan Press, Ann Arbor, 1995.

[45] P.G. Moore, H. Thomas, The Anatomy of Decisions, Penguin, Harmondsworth, 1976.

[46] O.K. Ngwenyama, N. Bryson, A. Mobolurin, Supporting facilitation in group support systems: techniques for analyzing consensus relevant data, Decision Support Systems 16 (2) (1996) 155–168.

[47] J.F. Nunamaker, L.M. Applegate, B.R. Konsynski, Computeraided deliberation: model management and group decision support, Operations Research 36 (1988) 826–848.

[48] K.N. Papamichail, S. French, Explaining and justifying the advice of a decision support system: a natural language generation approach, Expert Systems with Applications 24 (2003) 35–48.

[49] L.D. Phillips, A theory of requisite decision models, Acta Psychologica 56 (1984) 29–48.

[50] L.D. Phillips, M.C. Phillips, Facilitated work groups — theory and practice, Journal of the Operational Research Society 44 (6) (1993) 533–549

[51] H. Raiffa, Decision Analysis: Introductory Lectures on Choice under Uncertainty, Addison Wesley, Reading, Mass, 1968.

[52] H. Raiffa, R. Schlaiffer, Applied Statistical Decision Theory, Harvard University, 1961.

[53] H. Raiffa, J. Richardson, D. Metcalfe, Negotiation Analysis: The Science and Art of Collaborative Decision Making, Harvard University Press, Cambridge, Mass, 2002.

[54] H. Raiffa, J. Richardson, D. Metcalfe, Negotiation Analysis: The Science and Art of Collaborative Decision Making, Harvard University Press, Cambridge, Mass, 2003.

[55] V. Sauter, Decision Support Systems, John WIley and Sons, New York, 1997.

[56] L.J. Savage, The Foundations of Statistics, 2nd ed., Dover, New York, 1972.

[57] R.O. Schlaifer, Analysis of Decisions under Uncertainty, McGraw–Hill, 1967.

[58] M.S. Silver, Systems that Support Decision Makers: Description and Analysis, John WIley and Sons, Chichester, 1991.

[59] H. Simon, The New Science of Decision Making, Harper and Row, New York, 1960.

[60] P. Slovic, Perceptions of Risk, Earthscan Library, London, 2001.

[61] R.P. Sundarraj, A web-based AHP approach to standardise the process of managing service-contracts, Decision Support Systems 37 (2004) 343–365.

[62] A.D. Taylor, Mathematics and Politics, Springer Verlag, New York, 1995.

[63] G. Tulloch, On Voting: A Public Choice Approach, Edward Elgar, Cheltenham, UK, 1998.

[64] E. Turban, J. Aronson, Decision Support Systems and Intelligent Systems, 6th edition, Prentice Hall, Upper Saddle River, New Jersey, 2001.

[65] A. Tversky, D. Kahneman, The framing of decisions and the psychology of choice, Science 211 (1981) 453–463.

[66] J. Von Neumann, O. Morgenstern, Theory of Games and Economic Behaviour, 2 ed., Princeton University Press, 1947.

[67] D. Von Winterfeldt, W. Edwards, Decision Analysis and Behavioural Research, Cambridge University Press, Cambridge, 1986.

[68] Z. Wong, M. Aiken, Automated facilitation of electronic meetings, Information and Management 41 (2) (2003) 125–134.

![](/api/attachments/QY8QGJV6/fulltext/images/53dcddf74b4c99f146a1dfb2b50971d51e5efefd97251d1531714c16c1fbce22.jpg)  
Simon French is a Professor of Information and Decision Science at Manchester Business School. He has interests in decision and risk analysis, Bayesian statistics, information systems and knowledge management. Recently he has worked risk communication, stakeholder involvement and e-democracy, particularly in relation to societal risk management.
