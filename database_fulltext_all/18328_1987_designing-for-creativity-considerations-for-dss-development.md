---
otero_id: 18328
otero_key: "J7WPC5H3"
title: "Designing for creativity: Considerations for DSS development"
authors: "Joyce J. Elam; Melissa Mead"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90045-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing for Creativity: Considerations for DSS Development

Joyce J. Elam \*

College of Business, The University of Texas at Austin, Austin, Texas 78712, USA

and

Melissa Mead

Graduate School of Business Administration, Harvard University, Boston, MA 02163, USA

Decision support systems (DSS) can be designed to support the creative and intuitive aspects of decision making. Our purpose is to provide a new perspective for the design of DSS by focusing on the important external factors that have been shown to influence creative activity. Design guidelines can then be developed by viewing a DSS as a special environment that incorporates these factors.

Keywords: Creativity, Decision Support Systems, System design, Decision making.

Dr. Joyce J. Elam is currently the Marvin Bower Fellow at the Harvard Business School for the academic year 1987–88. She is on leave from the University of Texas where she is an Associate Professor in the Management Science and Information Systems department. Dr. Elam holds two degrees from The University of Texas at Austin, a B.A. in mathematics and a Ph.D. in operations research. Prior to joining the faculty at the University of Texas, she was an Assistant Profes-

sor at The Wharton School. Dr. Elam is currently an Associate Editor for MIS Quarterly. Dr. Elam's major research interests focus on the use of information technology to support decision making activities of both individuals and groups. Her work has appeared in such journals as Decision Sciences, Decision Support Systems, and Interfaces.

![](/api/attachments/J7WPC5H3/fulltext/images/0909e674b8e439ee6f3f36ec496795c923a573371d3b3bf00c5346471e329202.jpg)

## 1. Introduction

Early articles defining the DSS concept advocate a usage pattern where there is a high degree of synergy between the user and the DSS:

The DSS is interactive to allow the manager or his representative fast access to models and data ... to given access to data and models at a speed that matches the thought processes of the manager. [47]

Dss rely on the discision maker's insights and judgements at all stages of problem solving – from problem formulation, to choosing the relevant data to work with, to picking the approach to be used in generating solutions, and on to evaluating the solutions presented. [48]

Alter [1], however, in his study of 56 DSS found little evidence of this type of usage:

It was surprising that very few situations were encountered which could be described as “interactive problem-solving” ... a process involving a single person adaptively exploring a

![](/api/attachments/J7WPC5H3/fulltext/images/f5e6a83178396dc5e24786263b401def4d40c469155155e91259316636f83a6d.jpg)

Melissa Mead joined the Information Systems faculty at the Harvard Business School in 1985. Her teaching at Harvard includes first-year MBA courses in both Control and Management Information Systems. In addition, she has taught knowledge-based systems in the second-year MBA curriculum and conducted doctoral seminars focused on research methods and research topics in Information Systems. Professor Mead teaches in Managing the Information Services

Resource, an HBS summer executive program.

Professor Mead completed a Ph.D. in Management Science and Information Systems at The University of Texas at Austin in 1985. Prior to her arrival at Harvard, Professor Mead worked as a consultant for Analysis, Research & Computation Inc. She provided consulting services for Fortune 500 firms as well as U.S. government agencies.

Her research interests include the incorporation of information technology as an element of business strategy; particularly the use of information technology by general managers during times of transition to foster and sustain changes in strategic direction.

problem space ... more typical user behavior involved performing a preconceived set of runs which tested the effect of various values of particular variables.

The limited degree to which managers make direct use of a DSS in innovative problem solving endeavors is shown in other studies of DSS applications. A survey of 300 IFPS applications [31] found that 66 percent of the time analysts simply responded to a manager's request and got an ad hoc system up and running quickly. Seventy-four percent of the applications in the survey replaced manual procedures. A more recent study of 18 DSS in use at major corporations [28] found that many decision makers utilize intermediaries to operate the DSS, either as a substitute for, or in addition to, the decision maker. The study found that 77 percent of the DSS are operated, at least occasionally, by a staff intermediary.

Today DSS provide support for managerial decision making in a convenient, timely, and cost-effective manner. However, based on the published studies of DSS usage, the interactive problem solving environment envisioned for DSS remains to be realized. The current state of practice raises concerns within the academic community and motivates discussions as to why the broad charter of DSS to support the creative and intuitive aspects of decision making is not following $[18]$ . Young states that most DSS applications address structured problems using features that are “left-brained”. He argues that a whole class of problems (e.g. formulating general policy, determining methods and processes to influence individual and group behavior, and conceptualizing alternative new products) are essentially qualitative in nature and, in order to support them, DSS must incorporate “right-brained” attributes. El Sawy $[16]$ found that conventional DSS did not have the capabilities necessary to aid executives in understanding how information technologies might be used to improve competitive advantage, developing strategies for the use of information resources, or identification of marketing opportunities in information technologies and services.

This current state of practice is not surprising when one examines the research on design features and guidelines for development that have appeared in the DSS literature over the last 11 years. In a recent review, only 28 of the 211 DSS articles appearing in major information systems journals were identified as focusing on design features [19]. The specific questions addressed in these articles were [17]:

1. What is an appropriate design architecture that incorporates models, data, and interfaces?

2. How should graphics be used in DSS?

3. What are the features of various DSS intended for different organizational environments, different decision making situations, and different management levels?

4. What features should be incorporated into the user interface, the modeling component, and the database component?

Only one article specifically focused on issues of creativity [53]. In a review of the major information systems conference proceedings [29], only 5 additional creativity-related articles were found.

Here we adopt a social psychology perspective in developing a set of guidelines for designing DSS that support the creative and intuitive aspects of decision making. Our focus is on establishing an environment, via the DSS, that facilitates creativity. We refer to these DSS as creativity-enhancing DSS. This perspective augments previous research in the area that views the design of creativity-enhancing DSS primarily from a cognitive psychology perspective $[39,50,53]$ .

## 2. A Social Psychology of Creativity

DSS design guidelines have been heavily influenced by Simon's intelligence-design-choice model of decision making. Scott Morton [45], in a review of the DSS literature, states that all methodologies in the DSS arena use this basic view of decision making. Interestingly, models of the creative process look remarkably similar to models of decision making [6,27,49]. They are stepwise models that include problem identification, information gathering, alternative generation, assessment, and selection. This “decision model” perspective is incomplete for designing creativity-enhancing DSS since differences in the creativity of decision outcomes cannot be attributed solely to differences in the decision process. Thus a different perspective is needed to drive the design of creativity-enhancing DSS. It calls for examining the environment in which the decision process unfolds. We propose that this perspective should come from the social psychology of creativity.

![](/api/attachments/J7WPC5H3/fulltext/images/84bff74c3822cac7ad8cd1b6195e2330cd68867ee7589af9b572a52ca1d7a637.jpg)  
Fig. 1. Amabile's componential model of creativity.

A general theoretical framework of creativity includes both a focus on distinctive personality and individual characteristics associated with highly creative individuals as well as the social environments that hinder or foster creativity. Amabile [2] proposes that creativity be conceptualized as a set of components or factors that are necessary and sufficient for creative production in any domain. The components involve both cognitive and social dimensions. These components do not represent processes, rather they are sets of elements that control, determine, and enter into processess. The parts of her model are shown in Fig. 1.

In our research, we are interested in developing a set of guidelines for designing DSS that provides an environment that is conducive to creative decision making and provides “thinking” tools to aid in the generation of creative ideas. Since DSS are aimed at a wide variety of users with different levels of domain knowledge and different personalities, these design principles should not be based upon individual and personality characteristics associated with creativity. Rather, they should be focused on providing the best environment for supporting creativity in a variety of individuals. We, therefore, reclassify the components of Amabile’s model into two segments: those that are related to personality and cognitive characteristics of the individual influenced indirectly through the DSS environment (internal factors), and those more directly influenced (external factors). These factors are shown in Fig. 2. In developing design guidelines, we are primarily interested in the external factors. However, internal factors are examined to the extent that they interact with external factors in facilitating creative behavior.

## 2.1 Internal Factors

Domain-relevant knowledge is an individual characteristic that significantly influences creativity. It includes known facts about the task domain, relevant technical skills and special (domain-related) talents. From one perspective, domain-relevant knowledge should facilitate creativity. That is, creativity involves combining known, but previously unrelated, facts and ideas in such a way that new ones emerge. Clearly, one must have the components to combine, and DSS can assist in extending this domain-relevant knowledge.

![](/api/attachments/J7WPC5H3/fulltext/images/b5786dad89959c0af21982e18f630a3ca48a83f616ab9de07476a883409000e4.jpg)  
Fig. 2. Factors influencing creativity.

On the other hand, individuals with large stores of domain-relevant knowledge may have learned conventions that prevent them from viewing the world in new ways $[20]$ . This may take the form of “perceptual set”, where an individual adopts a narrow view of problem formulation. The importance of breaking this set in finding innovative solutions was cleverly demonstrated by Duncker $[14]$ in his classic experiments on “functional fixedness”. Similarly, individuals may develop a “cognitive set”, where a restricted range of solution approaches is repeatedly used. Newell et al. $[42]$ suggest the ability to break the cognitive set and follow new approaches and strategies may lead to more creative solutions. Thus persons with expertise in a given task domain may produce more creative solutions to problems, particularly when they are supported in abandoning either of these mindsets.

Other individual characteristics influencing creativity can be thought of collectively as the set of trait-based attributes associated with highly creative individuals. Guilford [23] identified several traits associated with creativity including a general sensitivity to problems, orginality, and an ability or tendency to redefine problems. He also suggests [22] that the trait of curiosity leads people to build a larger memory base upon which they may draw for facts, ideas, approaches, and strategies in the future. Gough [21] also identified curiosity as an important trait-based determinant of creativity. MacKinnon [38], in his study of architects, found creative individuals to have the following traits: inventiveness, independence, individuality, enthusiasm, determination, industry, self-acceptance, openness to new experiences, and tolerance of increasing tension when striving for solutions. Barron [4] noted in his study of artists that creative people have a desire or preference for cognitive complexity as well as an ability to reject suppression and be less controlled.

Certainly DSS are not likely to instill or eradicate individual traits. They may, however, create an environment that encourages the expression of creativity-enhancing traits and reduce the impact of creativity-suppressing traits.

## 2.2 External Factors

The first group of external factors influencing creativity are methods to aid creative thinking and problem solving. We refer to these approaches as creativity-relevant skills. These approaches include facility with breaking perceptual or cognitive set, divergent thinking, and delayed judgement. Breaking out of established patterns either perceptually or cognitively allows for the development of a broader range of alternative, perhaps creative, solutions $[5,30,51]$ .

Divergent thinking refers to the production of a variety of alternative solutions for a task. This is an explicit component of most models of the creative process. Divergent thinking may also require breaking perceptual and cognitive set. Availability of time, ease of producing solutions, and the decision maker's willingness to persevere influence the number of alternatives considered. The production of a greater quantity of possible solutions generated from different perspectives is linked in the literature with enhanced creativity $[24,43]$ . In addition, later, less obvious solutions are more likely to be creative ones, so the prolonging of alternative generation is likely to turn up creative solutions.

Related to devergent thinking is the practice of delaying judgment: A suspension of critical evaluation of ideas until a great deal of “free thinking” has been done. This has been suggested as a factor contributing to creativity $[34,41]$ . Creative solutions are likely to be later solutions. Thus, thinking of more solutions is important. Once the focus of thinking shifts to critical evaluation, convergent thinking displaces divergent thinking. While convergence to a final solution is necessary, premature selection may prelude the conception and consideration of more creative alternatives. DSS must be designed to foster new approaches and consider broader decision spaces.

The second group of external factors include task motivation, incubation, maintaining control over the problem situation, a sense of competence, and stress. Task motivation may be the most important determinant of the gap between what an individual can do and will do. Amabile [2] suggests that task motivation is a combination of individuals' baseline attitude toward a task (a trait) and their perception of the reasons for undertaking the task (a state). Thus, it may range from completely intrinsic interest in an enjoyed task to completely extrinsic motivation to perform a disliked task. It has been hypothesized that there is an inverse relationship between extrinsic constraints and intrinsic motivation, and that freedom from extrinsic constraints will enhance creativity [3,7,9,10,11,33,35]. While decision making is often externally motivated, it is the challenge of the DSS to provide an environment that allows users to focus on the intrinsically interesting elements of the decision and that adds minimal additional restrictions.

Incubation involves ceasing conscious effort on a difficult problem for a period of time. This rest may be linked with illumination, a sudden awareness of a solution to the problem. Simon [46] provides an information processing explanation of this phenomenon: “selective forgetting”. In incubation, Simon proposes that short-term memory is lost, allowing the decision maker to forget unproductive search efforts. When the individual returns to the task, a new search for solutions is begun aided by the useful information retained in long-term memory. Amabile [2] adds that during incubation, social contexts may change. Extrinsic constraints may fade and the individual may return to the task with intrinsic interest restored. The potential benefits of incubation include the generation of a larger range of alternative solutions, delayed judgement, and the consideration of a broader range of solution strategies.

Research suggests that intrinsic task motivation is promoted when individuals perceive themselves to be in control of their own task engagement $[8,9,37,44]$ . Retained control of task engagement means that individuals are free to undertake the task in whatever way they choose. This freedom nurtures the deep involvement an playfulness that many theorists believe is critical to creativity $[15,32,40]$ .

There are two important ways in which an individual's competence may be a factor that enhances creativity. The first is actual intellectual competence [21,25]: this is related to domain-relevant knowledge. The second way is one that may be readily influenced by environment: an individual's perceived competence, which may or may not accurately reflect true competence. A number of researchers propose that success, which affirms competence, will result in greater intrinsic motivation [8,12,13,26,36,52]. Other researchers suggest that creativity will be fostered by an environment where personal criticism is minimized [25,44]. A DSS can foster perceived competence when it operates smoothly and positively support individuals in exercising their intellectual gifts.

Stress is a factor that affects creativity. Some types of stress associated with the creative process may be unavoidable, such as the frustration preceding or accompanying perceptual/cognitive set breaking or incubation. In fact, the ability to withstand stress and uncertainty is a personality trait associated with creative people. However, not all people enjoy this ability. While some degree of stress may be unavoidable, increasing amounts of stress may lead to early termination of alternative generation and, thus, inhibit creativity. DSS designers can avoid stress-promoting features while creating tools to assist decision makers in their struggle toward effective solutions.

## 3. Creativity-Enhancing Design Guidelines

We now provide a set of guidelines for designing creativity-enhancing DSS. An overview of the design guidelines and their relationship to the external factors, creativity-relevant skills, and environmental conditions, is shown in Fig. 3. The first three relate to general capabilities and the remaining two involve the delivery of these capabilities to the user. The guidelines are intended to provide a new perspective for building DSS and a framework for the development of specific functional tools to support creative decision making.

Design Guideline 1: A DSS should provide depth and positive tenor in its feedback.

Depth of feedback requires that the DSS identify imperfections, search for causes to account for exceptions, find new directions or strategies for solving a problem, or present the problem to the user in a different way. In these ways a DSS can assist users in breaking their cognitive and perceptual sets surrounding decision making tasks. Positive tenor requires that meaningful, helpful, and encouraging responses be provided to eliminate unnecessary stress and engender a sense of competence in the user. All of these effects should encourage prolonged alternative generation and delayed judgement.

<table><tr><td colspan="10">External Factors Influencing Creativity</td></tr><tr><td>Creativity-Enhancing Design Principles</td><td>Breaking Perceptual Set</td><td>Breaking Cognitive Set</td><td>Divergent Thinking</td><td>Delayed Judgement</td><td>Task Motivation</td><td>Incubation</td><td>Retained Control</td><td>Competence</td><td>Stress Reduction</td></tr><tr><td>Depth and Tenor of Feedback</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>Restart Capability</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Range of Tools</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>Technical Ease of Use</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>Enjoyable, “fun” Environment</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td></tr></table>

Fig. 3. Creativity-enhancing guidelines/external factor linkages.

Design Guideline 2: The DSS will allow users to stop, store work sessions in progress, then resume work later.

This guideline calls for DSS features that remove any system-induced necessity to complete all work on a task in a single session to avoid incurring large start-up costs in subsequent sessions. Such features reduce stress, and give the user control and choice over when, and to some extent how, to engage in the decision making task. Further, this ability to easily stretch the time dimension in decision making facilitates delayed judgement and allows for incubation of ideas between work sessions.

Design Guideline 3: The DSS will make available a full range of qualitative as well as quantitative decisions aids.

A characteristic that will distinguish DSS designed to enhance creativity from most previously developed DSS is a focus on problem conceptualization. Current DSS design practices recommend that a model describing the decision making situation be identified and, either implicitly through a data-oriented DSS or explicitly through a model-oriented DSS, be made available to the user as an aid to exploring alternatives. Creativity is supported in these DSS through the generation of alternative scenarios based on the underlying model. Such an approach, however, runs counter to research concerning ways to facilitate creativity. First, the generation of alternatives is convergent in nature, since the overall structure of the problem is predetermined. Thus, divergent thinking is not fostered. Second, aids to creativity in a DSS require that users conceptualize the decision making task freely and in a variety of ways. Providing data and models or modeling capabilities is certainly necessary in any DSS. These must, however, be provided within a flexible environment that facilitates their creative use.

Problem conceptualization can be supported through qualitative aids such as rehearsal tools, sketching tools, analogical tools, script writing tools, pattern matching tools, and decomposition tools $[50]$ . El Sawy $[16]$ employed relevance trees, morphological analysis, and heuristics of lateral thinking in a system to support divergent thinking. Young $[53]$ suggests that idea processing capabilities support problem conceptualization by incorporating and manipulating verbal data in a combinatorial fashion.

A range of qualitative aids such as these can support the user in employing creativity-relevant skills. Quantitative aids are found in currently implemented DSS, but an emphasis must be placed on providing a greater number of accessible tools. The availability of a broader range of tools offers the user a variety of choices concerning how to approach the decision making task. This principle extends choice to include user control over the conceptual approach, as well as over the solution methodology employed. Additionally, a choice of analytical aids allows users to better fit their analysis to the task at hand, thereby avoiding the stress of “making do” with a less appropriate tool.

Design Guideline 4: A DSS will be technically easy to use.

Ease to use is a theme that runs through much of the DSS literature and is viewed primarily as a means to engender positive user attitudes. From a creativity perspective it is critical for other reasons: it leads to a sense of competence, allows for the generation of a greater number of alternatives in a given time, and reduces stress related to technical operation of the DSS. These benefits, in turn, support the user's sense of control over the DSS.

Emphasis on technical ease of use is intended to draw a distinction between systems that are functionally straightforward and those that are conceptually easy to use. Maintaining broad conceptualizing capabilities may render a DSS more conceptually difficult to use. That is, these DSS require the user to do more abstract thinking. This effort is necessary if creative solutions are to be found. However, the system need not introduce technical difficulties that distract the user. DSS should assist the user in focusing on the primary task of decision making rather than on intricacies of operating the software.

Design Guideline 5: The DSS will provide an enjoyable of “fun” computing environment.

In contrast to ease of use, “fun” has a connotation that includes enjoyment and becoming deeply engrossed in an activity. Thus, such an environment offers inducement for the user to spend more time in alternative generation for the decision making task. This offers the advantages of encouraging the user to examine a larger number of solutions, delay judgement, and, perhaps, allow for incubation if the user is drawn to return to the system. Additionally, an enjoyable environment will help to reduce stress as well as reduce the saliency of any external control the user may feel. Finally, “fun” is often associated with play rather than work, another factor linked positively to creativity.

## 4. Conclusions

Viewing the design of creativity-enhancing DSS within the context of a social psychology of creativity provides a new perspective for DSS: one of shaping an environment in which creativity may flourish. From this perspective, we have developed broad design guidelines that, taken as a whole, establish a framework for studying the linkage of DSS and creativity. Derived from almost 60 years of accumulated empirical research in creativity, this framework has significant face value.

It calls for two streams of research. One is the design and testing of specific DSS that include some or all of the proposed design guidelines. The other is carefully constructed experimental work to extend our knowledge of how creativity is influenced by DSS designed according to these guidelines. With this research, the original charter of the DSS movement should be achieved.

## References

[1] S. Alter: “A Study of Computer Aided Decision Making in Organizations”, unpublished Ph.D. thesis, MIT (1975).

[2] T.M. Amabile: The Social Psychology of Creativity, New York: Springer-Vcrlag, (1983).

[3] T.M. Amabile, W. DeJong, and M. Lepper: “Effects of Externally Imposed Deadlines on Subsequent Intrinsic Motivation”, Journal of Personality and Social Psychology, Vol. 34 (1976).

[4] F. Barron: “The Disposition Toward Originality”, Journal of Abnormal and Social Psychology, Vol. 51 (1955).

[5] E. Boring: “Great Men and Scientific Progress”, Proceedings of the American Philosophical Society, Vol. 94 (1950).

[6] D.T. Campbell: “Blind Variation and Selective Retention in Creative Thought as in Other Knowledge Processes”, Psychological Review, Vol. 67 (1960).

[7] J. Condry: “Enemies of Exploration: Self-Initiated versus Other-Initiated Learning”, Journal of Personality and Social Psychology, Vol. 35 (1977).

[8] R. deCharms: Personal Causation, New York: Academic Press (1968).

[9] E. Deci: “Effects of Mediated Rewards on Intrinsic Motivation”, Journal of Personality and Social Psychology, Vol. 18 (1971).

[10] E. Deci: “Intrinsic Motivation, Extrinsic Reinforcement, and Inequity”, Journal of Personality and Social Psychology, Vol. 22 (1972).

[11] E. Deci: “The Effects of Contingent and Noncontingent Rewards and Controls on Intrinsic Motivation”, Organizational Behavior and Human Performance, Vol. 8 (1972).

[12] E. Deci: Intrinsic Motivation, New York: Plenum (1975).

[13] E. Deci, and R.M. Ryan: “The Empirical Exploration of Intrinsic Motivational Processes”, in L. Berkowitz (ed.), Advances in Experimental Social Psychology, New York: Academic Press (1980).

[14] K. Duncker: “On Problem Solving”, Psychological Monographs, Vol. 58, No. 270 (1945).

[15] A. Einstein, autobiography, in P. Schilpp, Albert Einstein: Philosopher-Scientist, Evanston, IL: Library of Living Philosophers, Inc. (1949).

[16] O. El Sawy: “Prolificator: A Decision Support System for the Creation of Strategic Opportunities”, DSS-86 Transactions (1986):

[17] J. Elam: “An Examination of the DSS Literature (1975–1985)”, presentation at the IFIP 8.3 Working Group Conference, DSS: A Decade in Perspective, Amsterdam (1986).

[18] J. Elam, J. Henderson, P.G.W. Keen, and B. Konsynski: "A Vision for Decision Support Systems", unpublished manuscript.

[19] J. Elam, G. Huber, and M. Hurt: "An Examination of the DSS Literature (1975–1985)", in E. McLean and H. Sol (eds.), DSS: A Decade in Perspective, North-Holland (1986).

[20] W. Gordon: Synectics: The Development of Creative Capacity, New York: Harper & Row (1961).

[21] H.G. Gough: “Imagination – Undeveloped Resource”, Proceedings of the First Conference on Research Developments in Personnel Management, Los Angeles: University of California, Institute of Public Relations (1957).

[22] J.P. Guilford: “The Structure of Intellect”, Psychological Bulletin, Vol. 53 (1956).

[23] J.P. Guilford: The Nature of Human Intelligence, New York: McGraw-Hill (1967).

[24] J.P. Guilford: “Creativity: Yesterday, Today and Tomorrow”, Journal of Creative Behavior, Vol. 1, No. 1 (1967).

[25] J.P. Guilford: “Creativity: A Quarter Century of Progress”, in I.A. Taylor and J.W. Getzels (eds.) Perspectives in Creativity, Chicago: Aldine (1975).

[26] S. Harter: “Effectance Motivation Reconsidered: Toward a Developmental Model”, Human Development, Vol. 21 (1978).

[27] R. Hogarth: Judgment and Choice, Chichester: Wiley (1980).

[28] J. Hogue, and H. Watson: “Current Practices in the Development of Decision Support Systems”, Proceedings of the Fifth International Conference on Information Systems (1984).

[29] M. Hurt, J. Elam, and G. Huber: "An Examination of DSS Articles Appearing in Major IS Conference Proceedings (1980–1985)", Proceedings of the Seventh International Conference on Information Systems (1986).

[30] G. Katona: Organizing and Memorizing, New York: Columbia University Press (1940).

[31] P. Keen: “Value Analysis: Justifying Decision Support Systems”, MIS Quarterly, Vol. 5, No. 1 (1981).

[32] A. Koestler: The Art of Creation, New York: Dell (1964).

[33] A.W. Kruglanski: “The Endogenous-Exogenous Partition in Attribution Theory”, Psychological Review, Vol. 82 (1975).

[34] T.S. Kuhn: “The Essential Tension: Tradition and Innovation in Scientific Research”, in C.W. Taylor and F. Barron (eds.), Scientific Creativity: Its Recognition and Development, New York: Wiley (1963).

[35] M. Lepper, and D. Greene: “Turning Play into Work: Effects of Adult Surveillance and Extrinsic Rewards on Children’s Intrinsic Motivation”, Journal of Personality and Social Psychology, Vol. 31 (1975).

[36] M. Lepper, and D. Greene (eds.): The Hidden Costs of Reward, Hillsdale, NJ: Lawrence Erlbaum Associates (1978).

[37] M. Lepper, D. Greene, and R. Nisbett: “Undermining Children’s Intrinsic Interest with Extrinsic Rewards: A Test of the ‘Overjustification’ Hypothesis,” Journal of Personality and Social Psychology, Vol. 28 (1973).

[38] D.W. MacKinnon: “Creative Architects”, in R.S. Albert (ed.), Genius and Eminence, New York: Pergamon (1983).

[39] M. Manheim: “Theories of Decision-Making and Their Implications for Development of Creativity-Supporting DSS”, DSS-85 Transactions (1985).

[40] D. Meichenbaum: “Enhancing Creativity by Modifying What Subjects Say to Themselves”, American Educational Research Journal, Vol. 12 (1975).

[41] R.M. Milgram, N.A. Milgram, G. Rosenbloom, and L. Rabkin: “Quantity and Quality of Creative Thinking in Children and Adolescents”, Child Development, Vol. 49 (1978).

[42] A. Newell, J. Shaw, and H. Simon: “The Processes of Creative Thinking”, in H. Grubcr, G. Terrell, and M. Wertheimer (eds.), Contemporary Approaches to Creative Thinking, New York: Atherton Press (1962).

[43] A. Osborn: Applied Imagination: Principles and Procedures of Creative Thinking, New York: Scribner's (1963).

[44] C. Rogers: “Towards a Theory of Creativity”, ETC: A Review of General Semantics, Vol. 11 (1954).

[45] M. Scott Morton: “The State of the Art of Research”, in F. Warren McFarlan (ed.), The Information Systems Research Challenge, Boston: Harvard Business School Press (1984).

[46] H. Simon: “Scientific Discovery and the Psychology of Problem Solving”, in Mind and Cosmos: Essays in Contemporary Science and Philosophy, Pittsburgh: University of Pittsburgh Press (1966).

[47] R. Sprague, and H. Watson: “A Decision Support System for Banks”, Omega, Vol. 4, No. 6 (1976).

[48] A. Vazsonyi: “Decision Support Systems: The New Technology of Decision Making?” Interfaces, Vol. 8, No. 11 (1978).

[49] G. Wallas: The Art of Thought, New York: Harcourt Brace (1926).

[50] E.S. Weber: “Systems to Think With”, Journal of Management Information Systems, Vol. 2, No. 4 (1986).

[51] M. Wertheimer: Productive Thinking, New York: Harper & Row (1959).

[52] R. White: “Motivation Reconsidered: The Concept of Competence”, Psychological Review, Vol. 66 (1959).

[53] L. Young: “Right-Brained Decision Support Systems”, Database, Vol. 14, No. 4 (1983).
