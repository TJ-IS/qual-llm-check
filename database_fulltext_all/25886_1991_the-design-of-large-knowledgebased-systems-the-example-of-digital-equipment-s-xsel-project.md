---
otero_id: 25886
otero_key: "G6SA7NEJ"
title: "The design of large knowledge‐based systems: the example of Digital Equipment's XSEL project"
authors: "E. Mumford"
year: "1991"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1991.tb00029.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The design of large knowledge-based systems: the example of Digital Equipment's XSEL project

E Mumford

Emeritus Professor, Manchester University, Oxford Road, Manchester, UK

Abstract. This paper discusses the management problems associated with building and implementing large systems. The example described is XSEL, a configuring expert system designed by the Digital Equipment Corporation for worldwide application.

Digital, like many other larger computer manufacturers, had experienced problems in achieving a high level of configuring accuracy when assembling its computer. These problems showed up in the manufacturing plants but originated in the sales offices. They caused difficulties with customers and increased manufacturing and selling costs. The company decided that an expert system could solve the problem.

The processes associated with the design of this successful system created as many human as technical challenges. The paper describes these, discusses how and why they originated, and evaluates Digital's strategies for solving them. It makes some general recommendations for the successful management of major change.

Key words: Artificial intelligence (A.I.), design, environment, participation, management, XSEL.

## INTRODUCTION

A number of distinguished researchers have criticized studies of 'change' for concentrating too much on the narrow range of activities that are associated directly with the change (Pettigrew, 1985). They have argued that this approach ignores the influence of history and environment and can make change appear to be a straightforward, sequential set of events. For example, the 'change' process is often split into a number of steps to which terms such as 'diagnosis', 'design' and 'implementation' are attached.

This can make change appear structured and simple because the unexpected obstacles and impetuses that slow or accelerate it are omitted from the analysis. These are frequently due to factors occurring in the environment and can only be explained if this environment is understood. They may be due to company culture, to business policy, to the arrival of new senior managers and/or old ones leaving, or to the reactions of powerful groups who either want or do not want the proposed change. Major change cannot be fully understood unless these contextual factors form part of the analysis.

An understanding of the design processes associated with building and implementing a major expert system requires a knowledge of the attitudes, activities and events that enable the project to reach a successful conclusion. These include philosophies and relationships within and outside the activities of the design team and those responsible for the system's implementation. These processes are assisted by structures: groups created to assist the fulfilment of the design task, and by methods: tools to identify and solve different design problems.

This paper discusses problems and successes associated with the design of XSEL—Digital Equipment Corporation's first major expert system to be implemented world-wide. It will examine the factors in the design environment that influenced the route that the change took and which produced challenges and obstacles that had to be met and overcome.

The design of XSEL was never a neatly bounded task in which single activities followed logically and neatly one after the other. Design was complex with a number of activities requiring management simultaneously. It was often iterative with the design task rotating as options were reviewed and altered and new, unexpected, opportunities appeared. Design was concerned with motivating and influencing people. It was also concerned with the need to handle a complex network of human, technical and organizational factors, which were in a state of constant interaction and change, and required particular skills. Implementation proved to be the most difficult part of the process. Users in both the United States and the rest of the world needed to be convinced of the system's value before they would accept it.

## The influence of DEC culture on design strategy

Like all major computer manufacturers Digital had, for many years, experienced difficulty in handling the configuration task when assembling machines for customers. The manufacturing plants made many mistakes when compiling the multitude of parts that constitute any machine. These errors increased costs and led to poor customer relations and numerous attempts were made to solve the configuration problem. The first successful solution was the development of XCON, Digital's first successful expert system. XCON was located in the manufacturing plants as an aid to correct assembly.

The decision to build XSEL was taken once the management recognized that XCON saved the Company money. XSEL was a front end to XCON and was designed to prevent configuration errors from occurring in the sales offices when sales people gave quotes to customers and prepared orders for transmission to the manufacturing plants.

Both XCON and XSEL were risky ventures because Digital had no experience of building expert systems at the beginning of the 1980s. Few, if any, commercial companies had this knowledge. Artificial intelligence was still in an embryonic state and largely located in University departments. The configuration problem, however, was sufficiently costly and complex to justify pursuit.

The first lesson that can be derived from the XSEL experience is that difficult, innovative endeavours are more likely to be brought to a successful conclusion if the problem that they address is both critical and expensive. Small projects that are embarked on to gain experience in building expert systems may provide some technical knowledge and practical experience but they are unlikely to produce very useful results; nor are they likely to generate much enthusiasm and interest.

Many companies would have baulked at embarking on a high risk project such as XSEL. The fact that Digital did not was due to its pioneering culture and to the need to be ahead of the market in a highly competitive industry. Both these factors meant that the company was good at producing new technical developments and, perhaps even more significantly, at introducing major change into its own organization. It knew how to handle change because change was an essential and continuous part of its commercial success.

Digital's history, culture, knowledge and experience all contributed to the creation of XSEL and assisted in its implementation, although this was to prove more difficult than its design.

## Changes in business strategy

The development of XSEL was not a smooth and easy path. The route to success was strewn with unexpected hazards and unanticipated events. A number of these arose from new business policies and options that were adopted. In the early 1980s Digital rethought its business strategy and changed its structure. This caused a period of stress and trauma because departments and functions were altered and roles and responsibilities reformed. The consequent upheaval pushed XSEL into the background at a time when Bruce MacDonald, the project manager, and the sales force User Design Group were actively seeking top management support for the venture.

A potentially more threatening policy change was the move to increased product standardization, which occurred in 1984. This could have made XSEL unnecessary by simplifying the configuration process through a reduction in the number of models and options that were available to customers. An increase in standardization did take place but the extent of this was insufficient to affect configuration. XSEL was still a required solution.

The impact of organizational change and a new business strategy on XSEL needed to be recognized and responded to by Bruce, his technical development team and the User Design Group. An effective reaction required good intelligence so that early warnings of impending change were received. It also required the ability to respond quickly and effectively to challenging events.

This provides another lesson in the management of change. The recognition that a change-program is never an isolated, protected island, able to exist without external disturbance. It is similar to an island on a lake in the middle of a large town, likely to be visited by people who want to live there or take it over, or even destroy it. If it is to continue to preserve itself and its own harmony it must be able to attract and accommodate those visitors who will support it and enable it to prosper. It must also be able to recognize and protect itself from visitors who are undesirable and threatening.

Project steering groups can be helpful in providing intelligence and protection. Senior managers who are members can provide information on new company strategies, and on events that can significantly affect the project. They can also plead the project's cause with their top management colleagues. XSEL's progress was hindered by the lack of a steering group, which included senior sales management and took a proprietary interest in its development.

## The attitudes of the top management

The attitudes of the top management were an environmental factor of great importance to the progress and acceptance of XSEL throughout its design and implementation. Technical and AI management were always supportive and helped ensure that the resources for building XSEL were available. Sales management, seen by Bruce and his group as the eventual owners of XSEL, were ambivalent. Before accepting ownership they wanted definite proof of XSEL's effectiveness, accuracy and ability to save money.

Whereas manufacturing management recognized that XSEL could help their interests by preventing configuration errors from reaching the manufacturing plants, sales management was less concerned with configuration and much more focused on selling hardware. They wanted evidence that XSEL could help them do this. In the early days of XSEL's design it was not easy to provide this evidence. Bruce secured the co-operation and interest of the sales force by involving them in the design of XSEL. He did not have a comparable strategy that would identify sales management with XSEL.

This securing of support from senior sales management was one of the most difficult aspects of the project in both the United States and Europe. Once US sales had become committed to XSEL and convinced of its value, Bruce had to start again to try to win the acceptance of a sceptical European sales management.

It is not easy to suggest how this problem could have been avoided. Senior sales management was probably wise to require proof of XSEL's effectiveness before accepting it wholeheartedly. They were going to have to pay for it and their staff would use it. Their coolness, however, slowed down XSEL's implementation in both the US and Europe.

There is an important lesson that can be learnt from these cautious attitudes to XSEL. It is that the design of an expert system is one thing, but encouraging users and their managers to accept the system is another and may prove much more difficult. User involvement in design can assist acceptance but it will not be totally effective if important groups do not join in the participation processes. Acceptance will also be hindered if the problem that the expert system addresses is not regarded as significant by the user group.

Configuration was seen as a serious problem at the top of Digital, where its financial implications were clearly recognized. It was seen as a serious problem by manufacturing management whose staff made assembly errors because of inaccurate orders sent in by sales offices. It was also seen as a personal problem by sales people who received criticism from customers if systems were delivered with missing parts. Corporate sales management, however, were not close to the configuration problem and did not experience trauma because of it. They were more concerned with meeting sales targets.

These points highlight the difficulties that can be encountered when expert systems are designed by one group for another. Acceptance may be easier to achieve if a group of experts design a system for their own use: although experience suggests that this is not always the case.

## Interested groups

The work of a number of groups could be assisted or affected by XSEL and their interests had to be known and borne in mind throughout the design process. Sales were the critical group, but manufacturing also had a considerable stake in XSEL as orders based on error-free configurations could make life easier for them. Orders would not have to be sent back to the sales offices for correction before they were put through XCON and a diagram of component relationships produced. Digital also had a committee examine the order administration process in sales offices and XSEL could be an important contributor to this. The field service groups in the sales offices could also be affected by XSEL. Field Service had responsibility for hardware installation and were accustomed to prepare floor layouts to site machines in customer's premises. XSEL's floor layout function could make some of their activities redundant.

Throughout the design process these different groups had to be recognized, consulted and their different interests taken account of as XSEL progressed. Ideally, they had to be supporters of XSEL, seeing it as helpful rather than threatening. This recognition that others besides the sales force had an interest in XSEL was important. The acceptance of innovation can be inhibited if powerful groups, although not the direct users of a system, see themselves as adversely affected by it.

## Rival systems

Another environmental factor that had an impact on the morale of the User Design group was the occasional attempt by other groups inside and outside Digital to solve the configuration problem in different ways. Rival attempts were to be expected, of course, given the high visibility and cost of the configuration problem for Digital. These initiatives can be thought of as either attempts to solve the problem through simplification, or through different methods of dealing with the existing complexity. The latter covered both rival automation schemes as well as alternatives.

In the simplification category, only one major effort appeared: a standard system approach. Eventually, some systems were indeed sold largely in standard configurations, although these were in the minority. Nevertheless, over a considerable period of time, internal uncertainty about how widespread this approach would become delayed the implementation of XSEL. This, in turn, had a negative effect on the User Design Group and the technical team.

A number of rival schemes, which dealt with complexity, appeared over the years. These included two early attempts to demonstrate that the implementation of XCON could be better achieved by traditional technology than by Al. Neither of these were successful, but both caused some uncertainty while they were in progress. Rival solutions also included at least two attempts to build non-automated check list schemes intended to produce accurate configurations. In both cases these schemes were abandoned, one after XSEL became available, and the other before it even started, as a result of the planners learning about XSEL.

These rival efforts annoyed and worried the User Design Group who feared that their own efforts might be put in jeopardy. It can be argued, however, that duplication of effort does have some advantages. A number of solutions are directed at a common problem and one may prove to be superior to the others, but competition can be demoralizing if it is threatening rather than co-operative. Effort can be wasted if development takes place through an absence of knowledge that an alternative solution is being created in the company.

## The impact of the environment on the change process

The design of XSEL was not, therefore, a neat self-contained process. It was constantly influenced by events and attitudes in other parts of the company. These had to be recognized, responded to and managed. Unexpected challenges arose because of changes in business policy, top management attitudes, the interests of the groups XSEL could assist or affect and attempts to solve the configuration problem with alternative solutions. The design of XSEL required the creation and maintenance of a stable design environment in which thinking, discussing, building and testing could all take place. Bruce tried to provide this by monitoring and responding to events which could disturb or slow the design process and lower the morale of the User Design Group and the technical development team.

Any group that embarks on a major change of this kind requires an understanding of the organizational culture in which it operates. Schein states that we cannot understand organizational phenomena without considering culture both as a cause and as a way to explain such phenomena (Schein, 1969). It also needs an intelligence system to warn of significant events in the design environment, and it requires good management skills to enable it to respond quickly and effectively to these challenges. Pettigrew has suggested that successful change is the effective management of the interaction between what is being changed (the change content), how it is being changed (the change process), and what is happening in the change environment (the change context). The XSEL project provides support for this view.

## Designing XSEL

Designing was the critical activity associated with XSEL—without it the expert system could not have been built. A definition that fits well with the technical part of XSEL's design is 'the use of scientific principles, technical information and imagination in the definition of a structure, machine or system to perform pre-specified functions with the maximum efficiency and economy' (Jones, 1981). This was always the intention of $^{3}$ XSEL's technical design, although the reality involved searching for relevant principles and information and, on occasion, coming across these by chance.

## Resource creation

To obtain the necessary skilled resources to commence the design task was not easy as the industry had little experience of building expert systems at the beginning of the 1980s. This absence of expertise enabled Digital to create its own skills and it took the innovative approach of recruiting new staff to develop and build XSEL. These people, including Bruce, were given the necessary training and experience and this approach enabled the company to develop an effective multi-disciplinary and participative philosophy for the building of expert systems. Something which it continues to apply.

Other required resources were money, time, knowledge, interest and commitment, tools and techniques and hardware. The initial funding for XSEL was provided by the AI department, although once the system was implemented sales had to bear the full cost. Time was only occasionally a serious problem although the size of XSEL meant it took a number of years to build. Nor was the need to elicit expert knowledge a serious problem. In contrast to XCON, the XSEL effort did not require the direct involvement of human engineering experts. These experts already provided the input to the XCON process upon which XSEL was built. Therefore, while XSEL ultimately required knowledge elicitation, it was acquired indirectly.

XSEL's rules are largely 'abstractions' of the more 'concrete' XCON rules. Therefore hardware engineers did not have to be a direct part of the User Design effort. In addition, many of the AI technical group had acquired sufficient knowledge to be regarded as experts on configuration. Therefore, if needed, technical information was readily available to the User Design Group.

Interest and commitment in the project were stimulated and maintained through the User Design Group and the members of this found the author's ETHICS methodology a useful tool to help them to analyse their business needs and problems (Mumford, 1989). Perhaps surprisingly in a manufacturer of computers, hardware was not always easily available and XSEL's testing and implementation were often held up because of a shortage of VAX machines.

Effective management and facilitation proved to be an important resource. Social and management skills were required to manage the group processes involved in the design and implementation of XSEL. These were vital to the project's successful completion. They were an aspect of the project's complexity that could easily have been neglected.

## Experiment and learning

Experimentation proved to be a crucial part of the building of XSEL and was directly associated with learning. Bateson has defined learning as requiring stimulus, response and reinforcement (Bateson, 1980). The iterative design approach of discuss, build, test, evaluate, provided this. Knowledge was acquired in a step-by-step evolutionary manner as new routes and techniques were identified, tested and used or abandoned, and as XSEL grew in size and sophistication.

Knowledge had to be continually passed between the technical development teams and the User Design Group. High quality decision making depended upon the success of this communication process. Bruce had an important role to ensure that knowledge was distributed, evaluated, co-ordinated and effectively used. He required a good personal intelligence system so that he could discover events in Digital that might affect the progress of XSEL. The User Design Group became increasingly knowledgeable about the mission and work of the sales offices and about how to build and evaluate an expert system. This knowledge was of continuous benefit and enhanced the Group's ability to contribute to the company's business objectives once XSEL was operational.

Designing XSEL required original thought and considerable hard work. It also required marketing skill: the ability to make its potential known to other groups. Designing XSEL also required the creation and maintenance of a stable design environment in which thought, discussion, building and testing could all take place.

## Involving users

A feature of the XSEL project, and a major contributor to its success in the United States, was the involvement of the future user group—the sales force—in the design of the expert system. This involvement required the creation of a new structure that enabled collective discussion and debate to take place. It also required a 'facilitator', someone who would help the user group to examine their needs and problems systematically and take reasoned decisions. The User Design Group became the vehicle for discussion and decision taking while Bruce, the project manager, took on the role of facilitator.

The User Design Group was a mix of sales people and members of the AI development team who had responsibility for physically building XSEL. Individual experts in the technical aspects of the configuration problem were less important than would be the case with other expert systems, because members of the AI development team became configuration experts in their own right.

Bruce believed strongly that a participative approach would assist XSEL's acceptance by creating a system that met the needs of the sales force. The author who had helped other groups to design systems participatively, believes that this approach enables users to influence the design of the system; assists learning and the exchange of information; creates a strong user identification with the system and a sense of ownership, and ensures that an effective, acceptable system is the eventual outcome. Most groups have difficulty in achieving the latter without assistance and the role of the facilitator is to provide this. He or she must help the group to learn how to work together, acquire knowledge, solve problems, agree solutions and take decisions.

## Early uncertainties

All new user design groups experience uncertainty at the start of a project. Participants arrive at the first meeting with no clear idea of their roles or of the task ahead, and with little confidence in their ability to complete this task. The facilitator too will have feelings of doubt and confusion and Bruce was no exception. He was new to Digital, to expert systems and to the role of XSEL project manager. He had no experience of participative design or of acting as facilitator to a User Design Group.

He knew that he had to help the group to master the four essential tasks ahead: to acquire knowledge to build the system, to build the system and handle the problems associated with this, to manage its own group relationships and to persuade external groups to support the project. He asked the User Design Group members to think about their work missions—what they were trying to achieve. They were also asked to consider the extent to which the successful management of the configuration task contributed to this mission. They were then requested to describe the problems which hindered efficient configuration and caused frustration and a reduction in job satisfaction.

Carnegie–Mellon University was building a prototype of XSEL for Digital. Soon after the first User Design Group meeting the members were given access to this in their sales offices. They were asked to test it and send back their comments via a comments facility in the system.

Uncertainty was therefore reduced and knowledge building started in two important areas—an intellectual consideration of the salesperson's mission and role and the importance and nature of the configuration task in these; and a practical test of XSEL in its embryonic state. This iterative mix of thought and practice was to continue throughout the design and building of the system. It proved successful—the User Design Group saw themselves as both visionaries and entrepreneurs.

Once the prototype was seen to work, responsibility for building XSEL as an operational system was transferred to Digital. A technical group built the actual system, responding all the time to the guidance of the User Design Group. The members specified what was required and tried out each version of XSEL as it was developed.

Bruce found that one of the most difficult aspects of using a participative approach was helping the User Design Group to clarify its role. Prior to XSEL the sales force members had rejected software which they did not find useful. They were now required to improve it and Bruce had to remind them that they were in a development role. This needed creative thought, good judgement and a careful balance of alternatives.

Once the User Design Group meetings were established, Bruce found that the interest of the sales force in XSEL increased and more people wished to attend. This resulted in larger meetings that were more difficult to manage. There was also the problem of communicating what was taking place to members of the sales force who were unable to be present. This was solved through an electronic mail system. At the end of each meeting options that had been discussed were relayed to absent members of the sales force and their views sought. An account was taken of these when the final decision on how to proceed with a particular aspect of the system's design was taken.

From the company's perspective, participation assisted communication and the transfer of information between technologists and users. It brought groups with different interests together in a situation where they could talk to each other and this helped to solve problems in a new development activity. It highlighted and reinforced areas where there was an identity of interest between technologists and users and enabled conflicts of interest to be brought into the open and rationally discussed. It also assisted group learning and an understanding of the feelings, interests, needs, anxieties and hopes of the technologists and the sales staff. Although the dual role of project manager and facilitator was not an easy one to handle, Bruce combined the control functions of a project manager with teaching and motivating. He had to become a leader in the true sense of the word.

The alternatives to this participative approach might have been either a 'lets guess' or a 'lets try it and see what happens' strategy. The first occurs when a group of technical designers build a system with the belief that they know future users' requirements and that there is no need to involve or consult them. The second is when the technologists, with little prior consultation, produce a prototype of the final system for the users to 'play' with. The first approach can lead to expensive disaster. The second to the acceptance of a system that works adequately but does not meet complex needs because these have not been identified and carefully thought through.

Participation produced some clear advantages from a company point of view, but it also provided benefits to the individual members of the User Design Group. One benefit was that participation in group decision taking was accompanied by feelings of personal control. Psychologists suggest that this reduces stress. If we are in control of the roller coaster then we do not want to leave. Psychologists also argue that the pleasure of being in control does not come from the knowledge that allows us to hold that position, but from the excitement that comes from making things happen. There is a feedback loop between these two activities—the process of acquiring new knowledge makes it more possible to make things happen. Also, the more we have opportunities to work as a member of a group, the more our involvement with the group activity deepens.

Participation in group activity enabled the User Design Group to have more control over events and a better knowledge of the environment to be controlled. As the group drew closer to its desired objective of an operational XSEL, enthusiasm, motivation and excitement increased. Individual members felt both competent and confident—they had succeeded in making things happen. There was a sense of achievement. The opposite to feelings of control is feelings of helplessness. The individual sees himself or herself as a passive victim, unable to influence events that are going to have a dramatic impact on work and life.

The experience of designing XSEL suggests that participation pays. A participative approach means that the finished product is likely to be a well designed system that achieves user objectives. The emotional response to the finished product is also likely to be positive. In both instances the result may be better from the company perspective than would otherwise have been achieved.

## Managing the project

Schein had defined leadership, or what he calls ‘managership’ as a highly variable kind of behaviour which depends upon the person, his or her subordinates, the nature of the job requirements and the kind of problem solving to be dealt with (Schein, 1969). The ‘managing’ task for XSEL, and how it was interpreted by Bruce, was certainly influenced by all these things.

Bruce arrived in Digital understanding the company values of entrepreneurship and open management and supporting these, but not directly influenced by the Digital culture which he had yet to experience. His early behaviour in the company was greatly affected by his own philosophy and values. These led him to decide at the start of the XSEL project that a participative approach and user involvement in design was the route to take. He was aware that this strategy would fit the Digital philosophy and he had a pragmatic belief that he could not succeed without it. Unless the sales force were participants in the design of XSEL, they would not accept and use the expert system.

His experience as a school administrator led him to recognize that management is more than the use of a set of techniques. It requires human qualities such as sensitivity, human warmth and the ability to understand the interests and attitudes of other individuals and groups. He had already decided to define his project management task as both managing and facilitating. In addition to controlling a project he also had to help a newly created group to tackle and succeed with a difficult task.

At the start of the project he was probably unaware that managing XSEL required him to assume the various roles of evangelist, explorer, motivator, mediator, protector, planner and problem solver. His responsibility and task was to be the management of a complex organizational sub-culture. He was to become what Schein has called a 'culture manager'.

## Managing as 'evangelizing' and 'exploring'

Bruce was not required to be an evangelist for XSEL in the sense that he had to persuade Digital's AI group that it was a worthwhile project. This case had already been made and accepted. He did, however, have to be an evangelist to convince top management that XSEL was worthy of support, and this was particularly true of top sales management. Throughout the early life of the US part of the project he sought a sponsor in sales, and this effort was repeated when plans were made to introduce XSEL into Europe. This search required emotional strength, the ability to argue cogently and the skill to convince an understandably cautious top management group of the soundness of his evidence.

He also had to be an evangelist as new members joined the User Design Group. He had to articulate and explain the Group's participative philosophy and ensure that they accepted this. Many of the User Design Group meetings began with Bruce stating the mission and values. This helped to clarify a number of issues. It demonstrated that the project manager was not deviating from a participative strategy; it reinforced the group's belief in this approach and it ensured that new members were aware of, and accepted, the Group's co-operative method of working.

Bruce's 'explorer' role was even more demanding than his role as 'evangelist'. In the course of creating XSEL he and his group had to cope with considerable uncertainty and stress. There was no expert to guide them and no set of well-tried techniques to assist them in their task. Managing in this unclear environment was very much an art. It required what Schon has described as 'reflection-in-action'. The ability to use intuitive judgement, to criticize one's own actions, to change direction, to restructure an activity (Schon, 1983).

Confidence was required and relevant organizational experience which could provide some guidelines. At the start of the XSEL project Bruce had to rely on his previous life and work history to provide this. But the project provided its own learning environment. He not only had to memorize the lessons himself, he also had to help his group learn. Schon suggests that one of a manager's most important functions is the education of his or her subordinates. Helping others to learn the required interpersonal skills of self-awareness, communication, tolerance for ambiguity and the ability to manage conflict.

XSEL's journey, from start to finish, involved discovery and learning. New knowledge was acquired and new problems were successfully tackled. Bruce had to encourage the User Design Group to participate in difficult collective tasks where success was uncertain. Like other explorers they came to accept unexpected events as normal. This not only helped Bruce and his group to learn new things, it brought new knowledge into Digital that could spin-off on other projects.

## Managing as 'motivating', 'mediating' and 'projecting'

Bruce had three motivational tasks throughout the project. He had to motivate himself and ensure that his energy, drive and enjoyment of the task did not flag; he had to motivate the User Design Group and maintain their interest and enthusiasm, and he had to motivate the development team who were building XSEL according to the directions of the User Design Group. Motivating oneself is not easy, motivating others is even more difficult, although advice is now available on how to do this. Once again interpersonal skills, rather than formal techniques, are the critical factors.

Despite the length and complexity of the XSEL project, motivation was never a difficult problem. The excitement of the design task kept the User Design Group interested until XSEL was built.

One of Bruce's managerial roles that assisted group motivation was that of mediator. All major change involves the collaboration of a number of different groups, and XSEL was no exception. Inevitably, these groups will have different objectives and perhaps some that conflict. These can sour relationships and prevent active co-operation. It is important to recognize that this conflict exists and to have mechanisms to bring these out into the open so that they can be discussed and worked through.

The User Design Group was an important vehicle for doing this. It helped to overcome difficulties that sometimes arose between the sales force representatives and the members of the development team. These could be discussed in a positive and friendly atmosphere.

Bruce also had to try and mediate between the interests of the US group and those of groups in other countries. In Europe there were two groups with an interest in XSEL within the sales office: the sales people and the customer administration services group. In addition, the manufacturing plants had a keen interest in how the sales offices used XSEL, as did senior sales management in Geneva. This was a much more difficult situation for Bruce to handle because it was largely outside his control. He organized meetings at which issues could be aired and problems discussed but generally Europe went its own way.

Another challenge for Bruce was to keep the morale of the User Design Group and the development team high by protecting them from threats and outside interference. In effect, he had to reduce stress and keep their anxiety level low. He had to create a fast-response system to handle unexpected, threatening events, which could halt the project or cause it to slow down, or change. In this important role the manager acts as a defense force: the soldier ant protecting the queen bee, the secret service around the President.

## Managing as 'planning' and 'problem solving'

Planning and problem solving are two managerial tasks that are most discussed in the text books. This may be because they are viewed as rational activities, which require logical thinking and action. The other aspects of managing, which have been discussed in this paper, are often perceived as ambiguous and unclear: they rely on intuition and interpersonal skills as much as on rational thought. Nevertheless, the XSEL experience shows that these process-related skills are equally, if not more, important in determining the outcome of a project than those that are seen as more amenable to ‘scientific’ thought.

XSEL required considerable planning although not all the plans that Bruce made were used. He constructed plans for the business of the User Design Group meetings, for the building of XSEL and for XSEL's implementation. This was a valuable activity.

Planning and plans are, of curse, two very different products. Planning is a process which requires problem solving, the generation of resources and support, and strategies for implementation. Plans are usually documents that are the outcomes of planning. They may bear little relation to what happens in reality, but they can act as useful communication aids, displaying clearly what is intended and how it is to be achieved. They can also be useful as historical documents: revealing ideas and intentions that are strong enough to be formalized but never occur because they are overtaken by reality.

Bruce found that planning and the production of plans helped him to think clearly about needs and outcomes. They helped ensure that the User Design Group meetings covered all important issues and enabled him to identify necessary strategies and resources for XSEL's implementation. Plans also acted as excellent communicators of the User Design Group's intentions and ideas to top management. Few of his plans were implemented precisely as he intended. Planning was often followed by a need for rapid rethinking as unanticipated events altered the situation.

The design and management tasks associated with XSEL appeared to be very similar to what Schon has described as 'management artistry'. They involved dealing with unique and changing situations; designing and executing on-the-spot experiments, and constantly examining the meaning of old and new situations. It required what Schon calls a 'reflective' manager to create XSEL. It also required an 'influential' manager. One who could generate support and stimulate others to work productively and enthusiastically. This required considerable political knowledge and skill, and it required a 'confident' manager. Schon suggests that credibility, commitment, confidence and competence are all interdependent (Schon, 1983). The XSEL experience suggests he is correct.

## REFERENCES

Bateson, G. (1980) Mind and Nature, Fontana, London.

Jones, J.C. (1981) Design Methods. Wiley, Chichester

Pettigrew, A. (1985) The Awakening Giant. Blackwells Scientific Publications Ltd, Oxford, UK.

Mumford, E. (1989) XSEL's Progress. Wiley, Chichester.

Schein, E.H. (1969) Process Consultation. Addison-Wesley, Wokingham, UK.

Schon, D.A. (1983) The Reflective Practitioner. Temple-Smith, London.

## Biography

Enid Mumford is an Emeritus Professor of Manchester University. Before taking early retirement in 1988 to concentrate on research and consultancy she was Professor of Organizational Behaviour at Manchester Business School. For many years she has carried out research and published widely on all aspects of systems design and the involvement of users in the design task. In 1983 she was awarded the Jean-Dominique Warnier gold medal for contributions to information science.
