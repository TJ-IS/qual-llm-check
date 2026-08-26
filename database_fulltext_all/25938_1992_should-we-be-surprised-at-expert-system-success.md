---
otero_id: 25938
otero_key: "CC9FF2JP"
title: "Should we be surprised at expert system success ?"
authors: "P. Powell"
year: "1992"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1992.tb00082.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Should we be surprised at expert system success?

P. Powell

Department of Accounting and Management Science, University of Southampton, Southampton SO9 5NH, UK

Abstract. Expert systems proliferate. They are now a usable and used tool in a variety of organizations. However, little research has been undertaken on the quantification of success or failure of expert system projects. By and large the only test carried out for expert system validation is one of comparison of the conclusions of the system with those of an expert or team of experts. While questioning the validity, this paper accepts that this method is being used and analyses whether or not the results obtained from this type of test should be a surprise. That is, what sort of results should be expected and to what extent do the reported ones live up to these expectations? Earlier research from the field of human information processing casts doubts on the success claims made for current expert systems. The implications of this research are then analysed in order to explore the possible redeeming features of expert systems which are not taken into account in such comparisons. The use of linear models as comparators for expert systems may prove beneficial.

Keywords: expert systems, success, human information processing.

## INTRODUCTION

Expert systems (ES) proliferate. They are now a usable and used tool in a variety of organizations. However, little research has been undertaken on the quantification of success or failure of ES projects. As Connell & Powell (1992) point out, it is not clear what constitutes success, how success should be measured, nor if success criteria are stable over time and between projects. Nevertheless, the increasing use of ES does point to at least an informal, unvalidated view that they have worth.

By and large, the only test carried out for ES validation is one of comparison of the conclusions of the system with those of a human expert or team of experts. The degree of congruence between the two recommendations or decisions is taken as a measure of the success or otherwise of the system. Often the expertise for the knowledge base of the system is derived from this same individual, against whom the system is evaluated. This paper does not question whether this congruence is an appropriate metric, since this question has been addressed elsewhere (see Connell & Powell, 1992). Rather, it accepts that this method is being used, and analyses whether or not the results obtained from this type of test should be a surprise. That is, what sort of results should be expected and to what extent do the reported results live up to these expectations? Earlier research in other fields casts serious doubts on the success claims made for current ES.

The paper is structured as follows. The reported results of evaluations of ES are critically reviewed. Then a step back is taken both metaphorically and temporally, in order to assess the literature on human information processing (HIP). Of particular interest is the research on clinical vs statistical judgement. This research, predating that on ES, centred on attempts to replace expert human decision makers by models, usually of a statistical nature. Such experiments were undertaken in a number of fields including medicine (Elstein et al., 1978), banking (Libby, 1975; Zimmer, 1981) and stockbroking (Libby, 1976; Ebert & Kruse, 1978). This breadth of applications demonstrates that such models are applicable across a wider range of domains. These encompass domains that are apparently complex, calling for rule-based solutions. As will be demonstrated, linear models may be applicable in such domains though it is accepted that in certain areas for which ES have been built, a linear model approach may not be feasible. A comparison of the results of these tests to those undertaken for ES is enlightening. The implications of the comparison are then analysed in order to explore the possible redeeming features of ES which are not taken into account in such contrasts.

## EXPERT SYSTEM SUCCESS

Success is often claimed for ES based on non-rigorous testing. Often this testing is not of success but of other surrogate, or supposedly surrogate, features such as acceptance and use. Where testing or validation does take place it is usually based on the accuracy of the advice of the system compared to that of an individual or set of human experts. Bonnet (1985), for instance, talks of this method as being the only way of validating a system. Validation is done 'by having a group consisting of experts and less expert users apply the system to the solution of a selected set of real-life problems'. Due to the nature of the domains in which ES work, Bonnet sees the only feasible test as the comparison of human expert and machine on a set of real-life cases. Difficulties arise in defining what constitutes correct or even acceptable responses from both sides. The same author does, however, point to other measures, both quantitative and qualitative. Among the quantitative are correctness, precision, robustness and response time. These other factors may be crucial in determining if ES are a demonstrable improvement on other systems. Qualitative factors such as ease of learning, understanding and acceptability are proposed as alternative measures. It might be argued that quantitative and qualitative measures of success are complementary rather than alternatives; however, little of the literature gives cognizance to this. In information technology evaluation Powell (1992) differentiates between objective (i.e.

quantifiable) factors and subjective (qualitative) factors. He finds little evidence of the two being used together. Rather than metrics of success, Dhaliwal & Benbasat (1990) look at measures of the quality of the knowledge base. Measures they identify include representative validity (comparison with the source expert), value, usability and acceptance, and design architecture (ease of modification). However, it is not clear how, even if measurable, these factors are combined to form a global assessment of ES success.

Harmon & King (1983) state that performance criteria for systems should be 'specified in unequivocal terms'. System success might be reaching the same conclusions, in five existing or new cases, as the human experts. Liebovitz (1986), however, differentiates between validation, i.e. correctness, and evaluation criteria which are essentially a measure of the utility of the system. Such evaluation can be achieved by blind verification or the use of a modified Turing test. Shpilberg et al. (1986) provide no results but talk of validation against other experts for their tax ES, although they admit that exhaustive testing is difficult.

Business users will often focus on the bottom line, i.e., return on investment. Kraft (1987) claims that 'there are definite financial benefits. Almost all of our projects, with the exception of a few early prototypes did pay for themselves.' Kraft, however, writes of the DEC experiences with ES, involving the construction of the XCON family of systems, which are probably the most highly regarded of all ES implementations. There is little evidence that this financial success is universal.

Other empirical evidence of ES testing is sketchy. Often comparison claims are made, but these are presented in a non-rigorous way. For example, Kerschberg and Dickinson (1988) report on a corporate ratio analysis ES, though give no details of testing. This field is one in which a large number of human information processing studies, in which, typically, linear regression models of expert judgement are constructed, have been undertaken and it would have been interesting to compare the two result sets. AUDITOR (Dillard & Mutchler, 1988), a system for evaluating the adequacy of allowance for bad debts, was tested using both real and hypothetical cases with validation being assessed by the predictive accuracy of the system. Here results are given. In two tests, one blind, one open book, the expert system produced 19 acceptable decisions out of a possible 21. The authors question whether predictive accuracy is, in fact, a good guide for ES design, offering the view that prediction is a necessary but not sufficient condition for explaining behaviour.

Reporting on EvEnt, which assessed small to medium sized companies for loan purposes, Rozenholc (1988) writes, of validation by verifying, that the system came to the same conclusions as the expert; 'when it did not we fine tuned EvEnt so that it arrived at the correct appreciation of the file'. MYCIN, perhaps the most famous ES, was validated by a double blind test of 10 cases competing against human diagnosticians. MYCIN outperformed its human adversaries by 65% to 42.5–62.5% accuracy. In contrast, Michaelson (1982) reports that TAXADVISOR, an estate planning tool, produced no unacceptable recommendations and made more acceptable recommendations than two human experts (45% vs 33%), while the human experts outperformed the system in recommendations rated equivalent to a judging estate planning expert (55–67%). Thus overall, the system performed worse than the two human experts against whom it was evaluated.

The paucity of reported results points to two things. Firstly, that most ES tend not to be tested rigorously and secondly, in the few cases that are tested, performance is usually inferior to that of the human experts. On the latter point King & Phythian (1992) caution that testing ES against known results may be 'unfair' as it implicitly assumes a superhuman fallacy and the system will always appear poor. Testing against human experts requires 'much benefit of doubt' to be given to the system.

## HUMAN INFORMATION PROCESSING

Human information processing (HIP) research predates ES research. In a sense the aims of the two are remarkably similar. HIP investigates the use, by people, of information for decision purposes. The subjects are often experts. ES attempt to replicate human expertise in the form of a computer system which is then made available for use by the expert and others. While the similarity between the two fields is marked, the paucity of cross-fertilization of ideas and findings is surprising. Indeed, it is impossible to find any literature prior to 1987 which relates findings from the two fields. Even here, while the overlaps between the two are noted, the specific uses of existing HIP research findings for ES building are not thoroughly explored.

Hammond (1987) sees a number of similarities between the aims of ES (or artificial intelligence[Al]) and of what is often termed J/DM (judgement/decision-making) research. Hogarth (1987), too, views these areas as conceptually similar. Both fields attempt to capture the cognitive activity of experts, and both wish to evaluate it and use the results to aid novice decision-makers. The notion of decision-making under uncertainty is prevalent in both, as is an advanced study of cognition in its purest form. Yet as the same author points out, the results are remarkably different. A broad conclusion from J/DM would be that experts are poor and perform no better than models and seldom significantly better than novices, while Al views experts as good or takes their expertise for granted. Klein et al. (1989) caution that most cognition research is of the process of decision-making, while ES research focuses on the content knowledge of experts. Yet conversely, Lehner & Abelman (1990) state that J/DM research concentrates on models rather than processes.

Of crucial interest are insights into the following. How good are human judges? Are their judgements consistent and stable over time? To what extent do different experts agree with one another? Can a human judge be replaced by a simple set of equations and, if so, how well does each perform?

Expert system research has largely side-stepped the thorny question of whether the expert being modelled actually is expert and the extent of this supposed expertise. Replication of inadequate human experts is pointless, as is the testing of a system based on flawed expertise against an expert, or group of experts, who also exhibit the same tendencies. The same would be the case if human experts showed inconsistency in their decisions over time, or if, in general, human judges did not agree. However, Johnson (1983) maintains that knowledge-based systems which reason using the same processes as the human experts and reach the same conclusions are superior to those with the same conclusions but different lines of reasoning.

While there are reasons why one may not wish to use a linear regression model as the inference engine for an ES, building such a model and using it as a test competitor to the knowledge base might be worthwhile. In fact, as will be discussed below, the reasons why a simple mathematical model may outperform a human are closely allied to the reasons why an ES should similarly outperform an expert. If it does not, then what is being lost in ES construction that is not lost in linear model building? Conversely are the trade-offs in facilities offered by ES sufficient to make them more useful than a technically superior statistical model?

## How good are human judges?

One of the early HIP findings relates to the modelling of expert decision processes by simple linear models. The aim of this work was to provide a floor against which expert capabilities could be measured (Dawes & Corrigan, 1974). However, the floor became a ceiling as the simple equations outperformed the experts from whom they were derived. Hence, rather than comparing humans to a base level given by the model, they were seen to be striving to attain the same level of success as their model.

Many examples of this phenomenon are available. Ashton (1975) feels the results are robust across disciplines. He cites, for instance, studies by Goldberg (1970), in which a clinical psychology model was at least as good as that of the human judge in 28/29 cases, and Wiggins & Kohen (1971), where a student performance prediction model outperformed the human judge in each of 98 cases. Libby (1976) points to five cases in Dawes & Corrigan (1974), again psychologically based, in which models were rated as superior to man. His own bankruptcy prediction results show a model averaging 52.9 correct responses out of 60 whilst the humans had a mean of 44.4. Libby (1975) also investigated the capabilities of bank loan officers in predicting firm bankruptcy. A model derived from these experts correctly classified 88% of firms as likely to fail or not.

The term ‘bootstrapping’ has been applied to these situations in which models of experts outperform the experts from whom they were derived. Hogarth (1987) identifies admission to graduate school, loan grading and prediction of stock returns as fields in which bootstrapping models have been shown to work. Camerer (1981) gives 15 examples drawn from the literature of this phenomenon, and identifies the conditions under which bootstrapping models are most useful: where environmental structures are unknown or criterion information vague and it is impossible to pretest prediction models. These factors would be found in a number of ES domains, especially high-level diagnostic ones.

Libby (1976) postulates that if bootstrapping works then the implication is that one must 'get the human decision maker out of the decision process at the earliest possible moment'. This work is one of the few pieces of empirical work to question whether models actually were superior to experts rather than merely superior to naive subjects. Libby points to conflicting evidence for man's superiority over models, which Goldberg (1976) refutes. Libby believes that Wiggins & Kohen's (1971) conclusion of always using a model in preference to man is an over-generalization. Hogarth (1987), however, firmly concurs with Wiggins & Kohen, stating "the evidence overwhelmingly suggests that statistical methods should be used instead of intuitive judgement".

The reason for the superiority of models of man over man himself was summed up as early as 1966. Dudycha & Naylor (1966) state "humans tend to generate "correct" strategies but then in turn fail to use their own strategy with any great consistency . . . one is left with the conclusion that humans may be used to generate inference strategies but that once the strategy is obtained the human should be removed from the system and replaced by his own strategy'. Camerer (1981) concurs 'since the residuals from such a regression equation generally represent random variances in clinical judgments, bootstrapping models work because they eliminate a source of judgmental variance that doesn't provide information about outcomes'. If this conclusion is generally true, then the replacement of experts by ES should be beneficial. Yet, as the J/DM literature repeatedly shows, it is the consistency with which the models operate, more than anything else, which gives models an inherent superiority. If it is possible to provide this consistency with a simple model, then the added complications and expense of ES construction is hardly valid. Hence, in evaluating ES the marginal or incremental benefit of the ES over a simple model, not over the human expert, should be the appropriate metric. If models outperform man as the J/DM literature would have us believe, while the ES literature points to general superiority of man over ES, then it is necessary to question further this "success".

MacCrinnon & Wagner (1987) argue that the term ES itself may be a misnomer, 'if problem structuring has to be done by humans and if humans decide if sets of circumstances are relevant then expert is too strong a word for a computer'.

Although bootstrapping has not been shown to apply universally, Camerer (1981) sees it as especially successful where the environment is more predictable than man. He further makes the point that bootstrapping may be more applicable than the former might suggest since the predictability of men and environments tends to move together across tasks. Hence bootstrapping 'will generally work to a small consistent degree'. Stewart & McMillan (1987) disagree. They view bootstrapping as only being applicable to problems that are amenable to statistical modelling and hence not universally suitable. It can be used on static tasks where judgement is based on a few items of information and there is high task uncertainty and high inconsistency in the judgement of experts.

Ernst (1988) questions whether the purpose of ES building is to explain human behaviour or to predict outcomes of behaviour. He feels that mere predictive accuracy offers little guidance for the designing of ES, regarding prediction as a necessary but not sufficient condition for explaining behaviour. The power of any theory lies in its ability to explain rather than predict. Yet, in practical environments, prediction may be all that is required to be expert. A deep causal model, while theoretically appealing, may be overkill.

There is a crucial difference between knowledge and cognitive control which has relevance here, according to Mumpower (1987). Knowledge is knowing how to do something, whereas cognitive control is the ability to apply that knowledge in a consistent fashion. Indeed, the author points out that knowledge and access to an information base are sometimes mistaken for expertise, when it is the ability to predict or diagnose which is the critical measure. A number of early ES particularly in the taxation/legal domain rely more on their database abilities than on cognitive ones. For instance, the Government Grants Advisor ES (Evens, 1986) is symptomatic of such systems. Mumpower concludes 'The value of developing an ES that produces with great fidelity the inferential behaviour of experts who have little predictive ability is questionable'.

The J/DM research, so far mentioned, relates exclusively to linear models. While it might be thought that such simple models could be much improved by more complex non-linear models, there is little empirical evidence for this (see Ashton, 1975). Ebert & Kruse (1978) see linear models as accounting for 70–80% of the explained variance in judgemental responses while interactive terms explain less than 10% more. The complexity of the inferential models often applied in ES construction may be uneconomic. That is, little performance enhancement can be achieved by using complex rather than simple models.

Finally it should be pointed out that, poor as human experts might perform, there is evidence to show that they are better than a random model. For example, Zimmer (1981) shows that the majority of loan officers in his sample outperformed random results. Caution is necessary here until further evidence reveals if superiority over a random model is universal or application dependent.

## CONSENSUS AMONGST EXPERTS AND COMPOSITE JUDGES

Expert systems have generally been built to replicate the expertise of a single expert. In rarer cases multiple experts have been used, but this is usually manifest in separate small knowledge bases, perhaps interacting through a blackboard system which allows multiple knowledge bases to share information. An example would be the PROSPECTOR system (Duda et al., 1981) developed using the expertise of seven geologists, each of whom contributed a separate module. Very few systems are developed using knowledge elicited from several experts. The primary reason for this is the inconsistency among multiple experts and the ensuing reconciliation problems in knowledge base construction. A secondary reason may be the knowledge structure of the domain. Certain domains are inhabited by experts who exhibit global but relatively shallow expertise, while others rely on experts with deep, narrow knowledge. Models of man have no such difficulty in combining the predictive abilities of many judges into a single composite judge. Composite judges tend to outperform human experts but naturally do not perform better than models of the best human judge. In the empirical work of Libby (1976) referred to above, the composite judge scored 49/60, lower than the mean score of individuals' models, yet higher than all but one human expert. Ebert & Kruse (1978) report that their composite judge model outperformed human judges on 34 out of 35 occasions. Zimmer (1981) concurs with the finding that a composite judgement model performed at a higher level than the majority of loan officers he sampled.

The implication of this for ES knowledge elicitation is somewhat reassuring since composite judges do not tend to perform markedly better than single judges (Einhorn, 1972). A further point of interest of ES testing is the degree of agreement exhibited by different experts when confronted with the same problem. If most experts are shown to agree then expert systems might reliably be built by and tested against a single expert. Zimmer (1981) points to high levels of consensus among his expert loan officers as does Einhorn (1972) of his sample.

## Stability of judgements and self-insight of judges

Decision stability has been found to be high in most judges. That is, a human expert will tend to make the same decision now, based on the same data set, as at some time in the future (see, for instance, Ebert & Kruse, 1978). Einhorn & Hogarth (1978) conclude that experts find it very difficult to evaluate accurately the quality of their own judgement. Again, the loan officers in Zimmer's (1981) research showed accurate self-insight but were unable to assess their own overall performance. Shanteau (1987) feels expertise increases confidence not accuracy. Experts may be better able to defend and explain their judgements but the judgements themselves may be no better than those made by novices.

## In defence of expert systems

When compared to the models of man, ES do not appear to have been shown to perform at higher levels of competence. Both Levi (1989) and Norman & Javeed (1990) write of such a comparison; however, only the former formally evaluates performance. Even so, it would be hasty to jump to the conclusion that a linear model would be a good substitute for the knowledge base and inference engine of an ES.

Linear models are only applicable to predictive tasks, whereas ES are deployed in functions which require both prediction and diagnosis. Models of man cannot diagnose (at least not in the sense of providing reasons for observed entities). This is not so severe a limitation considering the fields in which ES have been built. Certainly some are diagnostic, while others are predictive. There may even be predictive elements to the diagnostic systems. Perhaps the HIP research should be a warning that there are better techniques for constructing predictive systems than the ES literature gives cognizance.

Mumpower (1987) points out that ES attempt to tackle problems for which a simple linear model would not be an adequate basis. Schmalhofer (1987) reinforces this by indicating that J/DM models use few variables and rely on consistency and transitivity or the maximization of subjective utility in order to function. He goes on to say that models do not accurately describe the cognitive decision processes of humans, who instead use heuristics. There is no doubt that ES are better able to reproduce these cognitive rules of thumb than are linear models. However, as a counter to this, it could be argued that heuristics are not a superior method of reaching a conclusion, but merely a satisficing technique which requires little processing effort. It is also fair to point out that J/DM research is usually performed in the cosy, closed world of the laboratory, while ES are more often thrown into the real world.

The advantages ES have over linear models are broadly similar to the advantages proscribed for ES over conventional programs, i.e., the explanation, justification and interrogative abilities which are an ES feature. There is little evidence that prescriptive models, for all their immediate attractions, perform well in real decision situations as opposed to the artificial ones used in the research (Milton, 1987). Einhorn (1972) cautions that at issue is not that machines are better at combinatorial problems but whether they are superior at the expert measurement or data input tasks. In essence ES are deductive. That is, they deduce conclusions from evidence. In contrast, linear models are inductive to the extent that they derive their weighting and factors from instances.

A large part of the requirement for successful ES is that of ensuring that an action is taken. As early as Shannon & Weaver (1946), there has been awareness that the mere correct and understandable nature of a message is irrelevant unless it motivates the recipient to carry out the appropriate action. ES may provide a higher level of motivation to users over a linear model.

Yet even ES producers fall back on attributes applicable to linear models of judgement in defence of ES. For instance, Harmon & King (1983) attribute the success of DENDRAL to its systematic search for all possible molecular structures rather than its knowing more than a human expert. They see MYCIN too as being successful because it does not overlook evidence or forget things and always checks all alternatives. However, its knowledge base was derived from the 'best humans' so some element of its success may be ascribed to this factor.

The decision as to the use of linear models or ES rests on a number of factors. Of concern would be the problem type, while will be related to the domain of the system. The need for dialogue may be crucial. ES are far superior at handling dialogue with the user and integrating often fuzzy responses into the knowledge base. Interaction with the system may also take the form of the user questioning the system, especially at the conclusion stage. While the traditional rule-trace explanation has been discredited (Kidd, 1987), linear models can offer no such assistance. ES may be non-mathematical, coping with fuzzy linguistic variables; linear models are sets of variables, mathematically expressed. The educational ability of ES technology cannot be overlooked. Indeed, the prime benefit of systems such as the Department of Health and Social Security one which represented benefits entitlement regulations in a knowledge based system (Hammond, 1983), lies in its training role. Rule derivation, that is the construction process for ES, has benefits which the hidden nature of linear model construction cannot match. Lastly, the declarative nature of ES construction has an inherent flexibility that a linear model lacks. On the other hand, Levi (1989) argues that ES should be expected to be more accurate than human experts. This conclusion rests on two premises: first that ES have to be more accurate if they are to be cost effective and second, ES share factors which contribute to human accuracy but not factors which detract from it. Though his own nuclear medicine linear model outperforms its expert derivers, he defends ES on the following grounds. There is more to expert performance than the combining of evidences — for instance, selection of a hypothesis to test, devising a course of action, judging implementations of classification and producing a causal explanation of classification. It is the ability to perform some of these tasks which may redeem ES, though demonstration of these actual abilities within working ES is not evident. Von Winterfeldt (1988) concludes that combining models of experts and models by experts may be beneficial, although both may provide a 'ceiling' on performance. He feels that the important issue is to allocate tasks between model types: unstructured tasks are better handled by humans, structured ones by a model. Finally, Lehner & Adelman (1990) suggest J/DM findings are useful for research if the ES goal is to maximize performance but not if it aims to evaluate or capture knowledge.

## CONCLUSIONS

The major conclusion from the above is the need to reiterate how valuable cross-fertilization of ideas would be from J/DM research to ES research. In the field of testing, ES are in their infancy. Firstly, no real tests are often applied to so-called successful systems. Those tests that are applied usually rely on comparison between the expert from whom the knowledge was derived and the system, or between the system and another set of judges. But as the J/DM literature shows, experts are often not very good, their judgement stability and consistency over time are not perfect and the extent of self-insight they exhibit is lacking. The degree of consistency between multiple human experts is also far from perfect. All these factors should cause ES developers to think again about their testing methods. Finally, simple linear models can be shown to outperform human experts; human experts can be shown to outperform ES and this apparent ranking should give cause for concern. Two possible solutions should be investigated. Either inferential procedures in ES could be replaced by models, or models derived from the expert could be used as a test bank for the ES. If the system is predictive their linear models should provide a viable and stringent test of the capabilities of the system. Indeed, if the system is predictive, then perhaps a better, although less glamorous, methodology already exists for knowledge replication. Alternatively, triangulation upon a difficult problem might be provided by employing both techniques.

Whatever the case, the success of ES is certainly not proven, yet some valuable tools for this function are available and should be used. The final choice may be a cost-benefit consideration, where the decision is not whether to build an ES or not, but whether the incremental benefits of an ES, over a linear model, are worth the price. As has been demonstrated repeatedly in the decision support literature, the building of a system is often more beneficial than its use. This complicates further the cost-benefit equation.

## REFERENCES

Ashton, R. (1975) User prediction models in accounting: an alternative use. Accounting Review, 50, 710–722.

Bonnet, A. (1985) Artificial Intelligence: Promise and Performance. Prentice Hall, Englewood Cliffs, NJ.

Camerer, C. (1981) General conditions for the success of bootstrapping models. Organizational Behavior and Human Performance, 27, 411–422.

Connell, N. & Powell, P. (1992) Measuring success and failure in the commercial application of expert systems:

'hard' measures for 'soft' systems. In: Artificial Intelligence in Operational Research, Paul, R.J. & Doukidis, G.I. (eds), pp. 349–357. MacMillan, Basingstone.

Dhaliwal, J. & Benbasat, I. (1990) A framework for the comparative evaluation of knowledge acquisition tools and techniques. Knowledge Acquisition, 2, 145–166.

Dillard, J. & Mutchler, J. (1988) Knowledge-based expert systems in auditing. In: Management Expert Systems,

Ernst, C. (ed.), pp. 135–154. Addison-Wesley, Wokingham.

Dawes, R. & Corrigan, B. (1974) Linear models in decision making. Psychological Bulletin, 84, 95–106.

Duda, R., Gaschnig, J. & Hart, P. (1981) Model design in the PROSPECTOR consultant program for mineral exploration. In: Expert Systems in the Microelectronic Age, Michie, D. (ed.), pp. 153–167. Edinburgh University Press, Edinburgh.

Dudycha, L. & Naylor, J. (1966) Characteristics of the human inference process in complex choice behavior situations. Organizational Behavior and Human Performance, 1, 110–128.

Dungan, C. & Chandler, J. (1986) AUDITOR: a microcomputer-based expert system to support auditors in the field. Expert Systems, 3, 210–221.

Ebert, R. & Kruse, T. (1978) Bootstrapping the security analyst. Journal of Applied Psychology, 63, 110–119.

Einhorn, H. (1972) Expert measurement and mechanical combination. Organizational Behavior and Human Performance. 7, 86–106.

Einhorn, H. & Hogarth, R. (1978) Confidence in judgment: persistence of the illusion of validity. Psychological Review, 85, 395–416.

Elstein, A., Shulman, L. & Sprafka, S. (1978) Medical Problem Solving: An Analysis of Clinical Reasoning. Harvard University Press, Cambridge, MA.

Ernst, C. (1988) Management Expert Systems. Addison-Wesley, Wokingham.

Evens, M. (1986) Expert Systems in the account profession. Proceedings of the London Conference on Expert Systems, Mackintosh Int.

Goldberg, L. (1970) Man versus models of man: just how conflicting is that evidence. Organizational Behavior and Human Performance, 16, 13–22.

Hammond, K. (1987) Towards a unified approach to the study of expert judgment. In: Expert Judgment and Expert Systems, Mumpower, J., Phillips, L., Renn, O. & Uppuluri, V. (eds). Springer-Verlag, Berlin.

Hammond, P. (1983) Representation of DHSS regulations in a Logic program. Proceedings of the BCS Expert Systems Conference, Cambridge, pp. 225–235..

Harmon, P. & King, D. (1983) Expert Systems: Artificial Intelligence in Business. Addison-Wesley, Reading.

Hogart, R. (1987) Judgement and Choice. Wiley, Chichester.

Johnson, P. (1983) What kind of expert should a system be? Journal of Medicine and Philosophy, 8, 77–97.

Kerschberg, L. & Dickinson, J. (1988) FINEX: a PC-based expert support system for financial analysis. In: Manage-

ment Expert Systems, Ernst, C. (ed.), Addison-Wesley, Wokingham.

Kidd, A. (1987) Knowledge Elicitation for Expert Systems: A Practical Approach. Plenum Press, New York, NY.

King, M. & Phythian, G. (1992) Validating an expert support system for tender enquiry evaluation: a case study. Journal of the Operational Research Society, 43, 203–214.

Klein, G., Calderwood, R. & MacGregor, D. (1989) Critical decision method for eliciting knowledge. IEEE Transactions on Systems, Man and Cybernetics, 19, 462–472.

Kraft, T. (1987) Artificial intelligence: next generation solutions. In: Intelligent Knowledge-Based Systems, O'Shea, T., Self, J. & Thomas, G. (eds), pp. 110–121. Harper & Row, London.

Lehner, P. & Adelman, L. (1990) Behavioural decision theory and its implications for knowledge engineering. Knowledge Engineering Review, 5, 5–14.

Levi, K. (1989) Expert Systems should be more accurate than human experts: evaluating procedures for human judgement and decision making. IEEE Transactions in Systems, Man and Cybernetics, 19, 647–657.

Libby, R. (1975) The use of simulated decision makers in information evaluation. Accounting Review, 50, 475–489.

Libby, R. (1976) Man versus models of man: some conflicting evidence. Organizational Behavior and Human Performance, 16, 1–26.

Liebovitz, J. (1986) Useful approaches for evaluating expert systems. Expert Systems. 3, 2.

MacCrimmon, K. & Wagner, C. (1987) Expert systems and creativity. In: Expert Judgment and Expert Systems, Mumpower, J., Phillips, L., Renn, O. & Uppuluri, V. (eds). Springer-Verlag, Berlin.

Michaelson, R. (1982) TAXADVISOR. PhD Dissertation, University of Illinois, IL.

Milton, L. (1987) Expert systems and expert judgment: a user's perspective. In: Expert Judgment and Expert Systems, Mumpower, J., Phillips, L., Renn, O. & Uppuluri, V. (eds), pp. 195–216. Springer-Verlag, Berlin.

Mumpower, J. (1987) Very simple expert systems: an application of judgment analysis to political risk analysis. In: Expert Judgment and Expert Systems, Mumpower, J., Phillips, L., Renn, O. & Uppuluri, V. (eds), pp. 217–216. Springer-Verlag, Berlin.

Norman, P. & Javeed, S. (1990) A comparison of expert system and human performance for cement kiln operation. Journal of the Operational Research Society, 41, 1007–1019.

Powell, P. (1992) Information technology evaluation: is it

different. Journal of the Operational Research Society, 43, 29–42.

Rozenholc, M. (1988) EvEnt assesses risk taking. In: Management Expert Systems, Ernst, C. (ed.), pp. 155–168. Addison-Wesley, Wokingham.

Schmalhofer, E. (1987) Expert systems as cognitive tools for human decision making. In: Expert Judgment and Expert Systems, Mumpower, J., Phillips, L., Renn, O. & Uppuluri, V. (eds), pp. 269–288. Springer-Verlag, Berlin.

Shannon, C. & Weaver, W. (1946) The Mathematical Theory of Communication. University of Illinois Press, Chicago, IL.

Shanteau, J. (1987) Psychological characteristics of expert decision makers. In: Expert Judgment and Expert Systems, Mumpower, J., Phillips, L., Renn, O. & Uppuluri, V. (eds), pp. 289–304. Springer-Verlag, Berlin.

Shpilberg, D., Graham, L. & Schatz, H. (1986) ExperTax—an expert system for corporate tax planning. Expert Systems, 3, 3.

Stewart, T. & McMillan, C. (1987) Descriptive and prescriptive models for judgment and decision making: implications for knowledge engineering. In: Expert Judgment and Expert Systems, Mumpower, J., Phillips, L., Renn, O. & Uppuluri, V. (eds), pp. 305–320. Springer-Verlag, Berlin.

Von Winterfeldt, D. (1988) Expert systems and behavioral decision research. Decision Support Systems, 4, 461–471.

Wiggins, N. & Kohen, E. (1971) Man vs. model of man revisited: the forecasting of graduate school success. Journal of Personality and Social Psychology, 19, 100–106.

Zimmer, I. (1981) A comparison of the predictive accuracy of loan officers and their linear-additive models. Organizational Behavior and Human Performance, 27, 69–74.

## Biography

Philip Powell is Lecturer in Information Technology in the Department of Accounting and Management Science, University of Southampton. He has taught in Australia and held a number of posts overseas. He is the author of two books, numerous book chapters and his work has appeared in Omega, Journal of the Operational Research Society and Journal of Accounting and Business Research. His main interests are the organizational impacts of IT, especially DSS and ES, and the way such systems might be evaluated.
