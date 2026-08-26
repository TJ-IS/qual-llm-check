---
otero_id: 26164
otero_key: "NBQCAB4S"
title: "Evolutionary Software Development to Support Organizational and Business process Change: A Case Study Account"
authors: "Peter Kawalek; Jenny Leonard"
year: "1996"
journal: "Journal of Information Technology"
doi: "10.1177/026839629601100301"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evolutionary software development to support organizational and business process change: a case study account

PETER KAWALEK

Informatics Process Group, Department of Computer Science, University of Manchester, Manchester, UK

JENNY LEONARD

Information Technology, University of Newcastle, Callaghan, New South Wales, Australia

This paper addresses the issues of software development in situations of organizational and process change. There is wide agreement in the literature that organizations have to be increasingly ¯ exible in order to survive in the current economic climate. They must innovate, replicate, adapt and extemporize. As they do so, the requirements they have of their software applications are likely to change. Equally, as new software solutions are provided, new opportunities for business change arise. The situation is made still more complex because even if the needs of organizations were stable, we still could not be certain of the validity of an application's functions. This is because the process of program development is inherently uncertain. From this situation arise dif® cult, practical challenges for those concerned with the deployment of software in organizations. Starting with a consideration of the nature of organizations themselves, this paper takes looks at these problems by moving between three related points. It looks at software development methodologies and suggests that these have in the past tended to assume that discrete IT solutions can be cast for a \`steady state’ which the organization is attempting to achieve. From the second vantage point it looks at the role of IT staff in supporting the operational needs of the organization. The third is the nature of software systems themselves.

## Introduction

A change project may cease but the organization itself never ceases changing. Whether a particular organization progresses through a series of incremental developments or through a more radical, reengineering \`leap’ , the state which it attains may prove no less transient that the one which preceded it. This is because it is in the interests and nature of organizations to change. Those that are incapable of appropriate change fail.

Ultimately, the core resource of any organization lies with the skill and knowledge of its people (Handy, 1993). The behaviour of organizations can be understood to be a pattern of interactions between these people. In the modern age organizations augment, and sometimes replace, people by using capabilities of software to store, share and manipulate data. Therefore, in software-rich organizations, the behaviour can be understood to be a pattern of interactions between people, between people and software, and between software applications.

This presents us with a conundrum. Change is endemic to organizations and yet organizations rely upon software systems which are ® nite, discrete and unchanging (Lehman, 1991). This is the essence of the legacy system problem. Software which was created to serve an organization in a particular state may not be appropriate to the service of that organization in a developed state. Moreover, it might actually hinder the progress of the organization between this initial state and the state which it seeks to attain. In other words, software systems that are developed to facilitate new ways of working might end up obstructing or even thwarting innovation. Clearly, this suggests that both technologically and methodologically there is a need for an evolutionary viewpoint so that a fruitful relationship between an organization and its software subsystem is maintained.

This paper reviews the literature on organizational change, the nature of software systems, their relationship to organizations, software development methodologies and the role of IT staff. It then explores the dif® culties that arose in a case study. This case study concerns the practices of a federated team of housing of® cers within a large housing organization. They were given the remit of examining all aspects of their work, and implementing new ways of proceeding whenever they decided it was appropriate. The project was designed to maximize the operational ¯ exibility of the team by giving them power to make strategic and operational decisions. They were given the power to de® ne their own IT solutions although they were required to use the functions of a central mainframe-based package for some aspects of their work. This was a pilot project intended to form an important part of a wider series of changes in the organization as a whole. As the project progressed and the staff came increasingly to ® nd new ways of working, their software systems became a constraint upon their development. They were caught in a conundrum. They developed new operational processes around the capabilities of IT, and yet those same software systems would then sti¯ e further development of the processes.

The authors were brought in by the team of housing of® cers to provide IT support and process analysis consultancy. Aware that they had to provide solutions with great ¯ exibility, they took the following approaches:

(1) A user-centred design approach to de® ning the strategic requirements in the project. This used process modelling techniques to focus upon the operational goals of the users, the interactions between people and the contribution made by IT.

(2) A federal, team-based role for IT staff.

The reasons for choosing these approaches, and the resultant successes, failures and unresolved issues are discussed.

## The nature of organizations

The phenomenon of organizational change is perhaps the most prominent concern of modern organizational literature. Senge (1990) advocates a discipline of systems thinking so that people can better understand the structures within which they act. He argues that this study of structures, and the behaviours they embody, should be used to challenge the assumptions (the \`mental models’) of decision makers. The ongoing requirement that assumptions be challenged and the use of group dialogue to catalyse thought processes leads Senge to the appealing notion of the \`learning organization’. For Sch”n (1971, a greater rate of change leads to the increased complexity of the problem faced. The greater the complexity of the problem, the longer it takes to solve it. The consequence of this cycle is that many solutions are stillborn; the problems to which they apply no longer exist in the same form (see also Ackoff, 1981, p. 5). Trisoglio (1995) uses complexity theory to suggest that the rapid increase in connectivity that is bought by a computing and communications revolution will lead to the highly-networked global information economy becoming still more complex and still more turbulent. In a review of organizational structures and strategies for complexity, he highlights the concepts of resilience, adaptability and diversity. Resilience is a static concept of design wherein a system is designed to be ¯ exible and to cope with the everyday crises and shocks that it encounters. Adaptability describes the system’ s ability to recon® gure itself as circumstances change. Diversity allows the generation of alternative responses to similar problems so that their relative merits can be evaluated. These concepts will be revisited later on.

Elsewhere it is increasingly argued that to cope with circumstances of commercial competitiveness and insecurity organizations in general have to be ¯ exible and innovative (Handy, 1992). That they should be process oriented has become a major theme (Davenport, 1993; Hammer and Champy, 1993). It has been vigorously argued that bureaucratic structures are outmoded and ill-suited to today’ s economic and technological climate. Federated (Handy, 1992) and ¯ attened (Scott-Morton, 1991) organizational structures have been advocated. The discussions on ¯ exibility in organizations are permeated by the notion of the empowered employee (for example, Davenport, 1993). Liberated from a bureaucratic infrastructure, the empowered employee depends upon a technological infrastructure to inform decision making, facilitate communications and to align his or her efforts with those of the organizational group. There is a complex bi-directional relationship whereby technological capability drives the adoption of organizational forms which themselves fuel the need for new technological capabilities.

Handy’s (1992) advocacy of federal structures is based upon the fundamentally challenging precept of subsidiarity. This states that power should reside at the lowest level unless reasons can be given for its displacement to some other, higher level. He describes how power is balanced \`among those in the centre of the organization, those in the centres of expertise, and those in the centre of the action, the operating businesses’. He identi® es three motivating factors behind what he perceives to be a widespread trend towards federal structure. The ® rst is the paradox whereby organizations need to be both big and small. They need to be big to take advantage of economies of scale, and small so that people can exercise autonomy and innovate. The second is the paradox whereby businesses advocate free and open markets as the best guarantee of ef® ciency and yet managers instinctively organize their own operations through centralized control. This suggests a need for \`federal compromise’ so that strategic decisions can be taken and yet a high-cost and sti¯ ing centralized bureaucracy is avoided. Thirdly, Handy notes that federalism is motivated by \`the pull of the professionals’. He writes

As organizations everywhere realign themselves around their core activities and competencies, they are realizing that their people are truly their chief assets. These human assets are far from ® xed. They could walk out of the door next Monday. They are the new professionals, high achievers for the most part, who see themselves as having careers beyond the organization. They prefer small, autonomous work groups based on reciprocal trust between leaders and led, groups responsible, as far as possible, for their own destiny. They would like to have it both ways, of course, preferring those autonomous groups to be part of a larger family that can provide resources, career opportunities, and the leverage that comes with size. Federalism to them is thus a way to make it big while keeping it small ± and independent.

## Information technology and changing organizations

This description of organizations as dynamic and complex structures leads to the need to consider further the impact of technological capability upon these structures. In the modern age, how does software technology affect the form of the organization as a whole? It has already been suggested that there is a complex bi-directional relationship. The question has in fact been addressed by writers over a number of years.

Harrington (1991) describes a series of metaphors of organizations as machines, organisms and processes. To perceive an organization as a machine suggests that technology in general is seen as a controllable resource which is used to achieve managerial goals. If an organization is seen as an organism, technology is seen as more integrated and less controllable. Ownership of it rests with the workforce rather than the management. If an organization is perceived as a process then it follows that technology is a behavioural phenomenon. It is managed by the user whose perceptions and culture can be changed through training. Pfeffer (1978) suggests that a possible result of the impact of IT upon organizational form is that staff are allowed more operational freedom. This is because information technology enables managers to assess more easily the outcomes of their actions. Management by outcomes allows the establishment of federated and empowered teams whilst preserving management control structures. The power in \`empowerment’ is thus restricted to control of process and does not carry with it the right to determine aims and objectives. Thus, Pfeffer observes, information technology has the paradoxical effect of supporting the centralization of power in organizations whilst seeming to support decentralization.

Winter et al. (1995) characterize the relationship between IT systems and the broader organization as that of serving and served system. For example, we might describe a team of housing of® cers as a served system whilst its IT infrastructure and capabilities represent a serving system. This neat description is useful for, as Winter et al, point out, conventional views of the system development life-cycle are characteristically concerned with the development of just one system; the serving system. Yet, many organizations embed their corporate memory and aspects of business rules and practice in their IT systems. Such then is the propinquity of the relationship between served and serving systems that to change one is likely to affect the other. Therefore, we need to consider the development of the IT system and the development of the organization that it serves as interdependent. Simon (1981, p. 132) has written of these issues from a wider viewpoint. His concern is for the relationship of the \`arti® cial’ world of man-made technology (the means) and the outer task environment. He writes

The arti® cial world is centred precisely on this interface between the inner and outer environments; it is concerned with attaining goals by adapting the former to the latter. The proper study of those who are concerned with the arti® cial is the way in which that adaptation of means to the environment is brought about ± and central to that is the process of design itself.

To understand the process of software system design raises a number of issues. Next, the role of IT professionals is considered. In later sections, the nature of the software artefact (the software system itself) and design methodology are reviewed.

## The role of the IT professional

In a study to identify the skill and knowledge of IS professionals, Lee et al. (1995) examined the role of IS in the context of changing technologies and business environments. They discuss an \`undisputed trend’ towards distributed computing, with some writers, e.g. Dearden (1987), arguing that the \`central IT department (will) become obsolete and wither away’ while others, e.g. La Belle and Nyce (1987) arguing that some centralized functions will remain. They also quote Keen’s argument that IS professionals must reject a task approach, which \`reinforces an IS culture of narrow technical orientation and stubbornness, leading to the perception by the user community that IS is unresponsive. Keen (1988) argues that future IS activities should be examined from a \`role’ perspective, which emphasizes the relationship between IS and users.

They summarize these arguments as a \`shift in emphasis from a traditional, central IS organization, toward a more decentralized, end-user-focused business orientation’ and point out that a \`focus on process reengineering requires that the IS professionals develop interpersonal and management skills to work with their functional peers in de® ning new ways to conduct business. They then typify the skills which will be required of IS professionals: \`industry will demand a cadre of IS professionals with knowledge and skills of technology, business operations, management, and interpersonal skills to effectively lead organizational integration and process reengineering activities.’

## The nature of software systems

This leads us to take a further step: the consideration of the nature of organizations led to a consideration of the nature of the relationship between organizations and software technology. This now leads to an exploration of the nature of software systems themselves. It is not just that software systems are becoming more signi® cant in modern organizations, but that the form of the software system is changing. Today for many organizations software systems are increasingly large. Commonly, they are constructed not only from many modules but from programs. Discrete tools such as bespoke corporate applications, generic word processors and databases are called upon to serve routine and ad hoc activities. The high cost of developing bespoke software systems leads to a requirement that they be long-lived. This in turn means that their scope, functionality and the assumptions embedded within them are more likely to be breached by new needs which result from broader organizational changes. These changes occur, sometimes with rapidity, as the organization seeks to survive, to compete and to innovate. At the same time the number of solutions available in some generic form off the shelf continues to multiply. These several pressures suggest that when considered as a whole, organizational software systems may increasingly be characterized as heterogeneous, part bespoke, part general purpose, dynamic and acoeval. By \`acoeval’ we mean of different ages or generations. For example, users may be required to work with some tools which are very new and feature multimedia interfaces and others which are older and feature only command line interfaces.

## The evolutionary paradigm

Lehman has written extensively of the nature of software systems and their relationship with their environment (\`the real world’). He describes the inherently uncertain nature of the programming process within which assumption is built upon assumption. He writes:

A computer program or software system is a model of a domain and of an application or problem in that domain. For real applications in real domains, that is for real world applications, the domain is essentially continuous, unbounded and dynamic whereas the software model is essentially discrete, bounded, and, unless changed by human decision and action, static. Moreover, there will always be a time delay between the decision to change the software and the satisfactory completion of the change. The software model, is therefore, an approximation, essentially incomplete and with embedded assumptions (Lehman, 1992).

Thus, a software system embeds a representation of an organization which relates in some partially understood way with the organization at a particular point in time. Organizations are necessarily in a state of ¯ ux, they innovate and replicate in their existing marketplace and may invent or enter new marketplaces. Therefore although the software system which supports the organization is essentially static, the validity of the software model is dynamic. Herein we approach the paradox through which software \`support’ systems hinder organizational change and block progress.

That we cannot be certain of the impact of systems upon their domain leads Dasgupta (1991) to propose a \`Theory of plausible design’. This posits that it is possible to provide evidence that a given design is plausible but that belief in its plausibility may have to be revised. Thus, in practice the designers of software systems are forced to resort to satisfactory rather than optimal positions. Warboys (1995) emphasizes that the design and lifetime of an IT system is therefore intrinsically evolutionary. This has resonance with the concept of an E-type program (Lehman, 1991).

An E-type program (the \`E’ stems from evolution) is required to solve a problem in a real-world domain. As such the acceptability of the system is entirely dependent on subjective human judgement. It cannot be judged against some separate speci® cation or problem statement but is understood in relation to needs and expectations which arise in the domain of which it is a part. An E-type program contrasts with an S-type program, which satis® es a pre-stated speci® cation. This speci® cation serves as a complete and singular determinant of the properties of the program. For an S-type program the only criterion of success is its correctness, in a strict mathematical sense, relative to its speci® cation. Lehman also de® nes a P-type program which is in effect an intermediate classi® cation.

Thus we have an evolution for software systems that rests upon two pillars. The ® rst is that the

## Evolutionary software development

organizational context which the software must serve is dynamic. The second is that the outcome of the operation of the software system is in any case uncertain. It is derived from the nature of the organization which the software system serves and the nature of the software system itself. Put simply, in an environment of constant business change a software system cannot move from steady state to steady state. Nor can it be optimized against static goals. It must constantly evolve to meet new goals, and to facilitate the development of organizational processes. Therefore, in such circumstances it is of necessity that the accent should be on \`satis® cing’ solutions (Simon, 1981, p. 138).

## Legacy systems

This irreconcilable discontinuity between the dynamic organization as a dynamic artefact and its software support systems as static, ® xed-function products invites a consideration of the problem of the legacy system in organizations. The suggestion is that this discontinuity contributes to the problem.

The fact that legacy IT systems pose a general maintenance problem has been discussed for many years. In the 1980s the discussion revolved around the fast increasing percentage of IT resources spent in maintaining legacy code. It was estimated that in 1960 30% of software development resources were used in maintenance, rising to 65% in 1980, and 80% in 1985 (QAI, 1985). At that time, the problem could be divided into three types of maintenance:

(1) corrective maintenance, i.e. error correction;

(2) adaptive maintenance, i.e. modi® cation of software for a new environment;

(3) perfective maintenance, i.e. making enhancements to the functionality and ef® ciency of the code.

The widely reported study of Lientz and Swanson (1980) estimated corrective maintenance as taking up 17% of maintenance effort, adaptive maintenance 18%, with the majority of effort being amendments for the purpose of enhancing functionality and ef® - ciency of the code. A picture could be painted at that time of a backlog of requests for change. Addressing the problem involved increasing the pro® le of software maintenance and using various tools and techniques for improving code (Leonard et al., 1988).

Since then, many new developments have changed the perspective. These include end user computing, increased use of networks, client server architectures and object orientation. Moreover, it has become more widely appreciated that change is intrinsic to organizations, as discussed previously. The seemingly intractable problem of the 1980s of maintaining legacy software in the face of an increasing queue of change requests has become the impossible task of the 1990s; to have instantly adaptable software that is able to support radically changing demands on a series of fast developing platforms and integrating with a series of end user developments. Unsurprisingly in this context, success stories have been few. A recent survey of the deployment of IT systems in 300 ® nancial services companies (of which 100 replied) in the context of business process change (Watkins, 1994) compared them with the MIT model of Business Transformation (Scott-Morton, 1991). This ® ve level model gave the following results:

(1) Level 1 Localised Exploitation 90%

(2) Level 2 Internal Integration 8%

(3) Level 3 Business Process Redesign 2%

(4) Level 4 Business Network Redesign 0%

(5) Level 5 Business Scope Rede® nition 0%

Thus only two of the companies had undertaken business process redesign. Watkins states that \`if the recommendation (for BPR) is to do away completely with the IT infrastructure, the company’s management will not let it happen. This is understandable considering the man-years and costs tied to the existing systems and the fact that they could disrupt the whole future of the company. Basically, almost no-one wants to touch existing systems unless it is to implement nonstrategic systems’. In other words, companies are more likely to succeed in areas which are not their traditional areas of expertise because they do not have legacy IT systems in those areas. In areas where they do have them, they cannot afford to do away with them, particularly with the data contained in them, and yet cannot afford to keep them.

## Software development methodologies

The above description of the development of IT systems as an evolutionary, uncertain and predominately satis® ying process runs counter to current industrial practice. What consultancy would admit that their system is in effect \`. . . an approximation, essentially incomplete and with embedded assumptions’?

This necessitates a review of the way in which IT systems are developed. Fitzgerald (1996) describes the history of development of software development methodologies. He suggests that a more disciplined and methodological approach to software development was ® rst advocated in the early 1970s to deal with the \`software crisis . . . the fact that systems took too long to develop, cost too much, and did not work very well’. He cites estimates of the number of different published methodologies as between 300 and 1000. He points out that there are \`relatively insigni® cant and arti® - cially contrived differences between some methodologies, while there are fundamental differences between others’. Differences occur between methodologies in terms of philosophy, objectives and technique, and may also differ fundamentally in paradigm, some having a \`hard’ scienti® c and rationalistic approach, and others a \`soft’ human-oriented one.

The \`hard’ rationalistic approach is by far the most prevalent in industry. Development methodologies using this paradigm, such as SSADM in the UK and elsewhere, and Department of Defense Standard 2167(US) are used in \`projects totalling billions of pounds each year’ (ibid). This approach is characterized by a subdivision of the development process . . . the complex development process is broken down into categories of analysis of requirements, design of a solution, and implementation of that solution’ (Olerup, 1991). Other broad categories to be added include an initial investigation of the organizational problem context, and a ® nal maintenance stage (Downs et al., 1992). Systems development is thus conceptualized as essentially a linear phased model, albeit with some iteration across phases, leading to increasingly formal de® ning documents until the system emerges. To take one example, Information Engineering methodology proceeds top-down from establishing a broad view of information requirements to a phase in which \`the enterprise realize the full bene® t of the application system as it executes to satisfy some portion of the business requirements identi® ed’ (Texas Instruments Incorporated, 1988, p. 2).

There are, of course, variations within these themes. Kelleher (1995), for example, divides methodologies into ® ve classes: forward engineering, package selection, systems reengineering and systems maintenance. He also discusses two forms of phase sequencing: the sequential, \`waterfall’ approach, and the iterative \`spiral’ approach.

For our purposes, the identi® cation of discrete, sequential subdivisions might restrict the designer’s responsiveness to dynamic situations. The solution proposed by such methods is, for us, the problem. Even the most recent initiatives such as BPR, for which organizational change is the fundamental concern, seem to take the same standpoint. As Hayward (1995) reports, \`Organizations began using BPR for short-term cost-cutting. They turned structures upside down for a few months, but then settled down with new, equally in¯ exible ones ± a process sometimes known as refreezing’.

Turning instead to what Fitzgerald (ibid.) describes as the \`softer’ approach, we ® nd that for some time a number of writers have advocated a user-centred approach, for example Eason (1988), Mumford (1983)

and Macauley et al. (1990). These writers embrace a socio-technical perspective which recognizes the essential duality of developing IT systems and their organizational context. Checkland’s widely reported \`soft systems methodology’ seeks the reconciliation of different views of complex, human oriented problem situations. Critical systems thinking (Schechter, 1991) has gone further by adopting an overt political stance based upon commitments to critique, to emancipation and to pluralism. That political structures can be considered as con¯ ict-based represents a challenge to those user-centred approaches which assume that there is or can be a social cohesion within organizations as they are currently instituted.

The process modelling approach of Kawalek (1995) and Wastell et al. (1994) emphasizes the importance of a multidisciplinary, socio-technical intervention. A role-interaction paradigm is at the heart of this work which emphasizes the notion of interaction between group members, between group members and the software components they use and between software components. The aim is to provide a means for the design and, ultimately, the evolution of complex systems. The role-interaction paradigm is used to explore the synthesis of the system so that user needs and dependencies are understood and supported. Upon declaring who they interact with (e.g. housing of® cer interacts with tenant), users are required to describe the operational goals of the interactions. From this point activities are modelled so as to help to ascertain the IT support which is required by the users in seeking to achieve the operational goal. The use of this method is discussed further in the context of the case study.

## The STAMP Of® ce, Merseyside Improved Houses

## Introduction

The case study considers Merseyside Improved Houses (MIH). This is the seventh largest housing association in England and aims to provide high quality, cost-effective, well managed and affordable homes for people in housing need in the North of England. At the time of the conclusion of this study (late 1995) it has a housing stock of 19 500, 470 salaried staff and 26 local of® ces. It had a wide range of partnerships with voluntary agencies, local authorities, environmental, social and housing groups (MIH 1995).

The business environment at the time of the study was inclement. Financial cut-backs by central government, the collapse of the British housing market in the

## Evolutionary software development

1990s and the privation of large areas of northern cities all had an impact on the work of the organization. They confronted many changes, including loss of various government grants, pressure to manage within market forces and compulsory competitive tendering (wherein public services are opened to bids from private service providers).

MIH as whole has taken a decisive and positive approach to these challenges. It has a commitment to growth, both in numbers of tenancies and in geographical coverage. It is undertaking a review of its processes and organizational structures. Three initiatives can be seen in this context:

(1) The federated of® ce pilot which forms the subject of this paper.

(2) A proposed umbrella 24-hour \`housing direct’ telephone-based service which is to be set up within the next two years.

(3) The development of regional of® ces, to further develop the federal structure, beginning in early 1996.

The creation of the South Team Area Management Project was a pilot project which it was anticipated would assist the migration of the organization as a whole to a federal structure. The establishment of this federal unit was directly informed by the writings of Handy (1992, 1993, 1995). It sought to de® ne new ways of working, to establish software support requirements, implement them, and measure the results.

The pilot was in a separate housing of® ce several miles from the MIH head-of® ce. It had six staff, and 1 000 houses. This represented half the normal ratio of housing staff to households. It also had tough business objectives:

(1) reduction in direct costs of the service;

(2) reduction in overheads and centralized costs;

(3) increase in tenant satisfaction levels, measured by survey;

(4) improvement in performance against a range of pre-de® ned indicators (e.g. stock quality, rent levels);

(5) acceptance of external stakeholders;

(6) improvement in staff morale, measured by survey.

The STAMP team were given complete autonomy about how these objectives were to be met. They were able to de® ne their own IT solutions and were also able to set new objectives and sub-goals, although the business objectives expected of them by MIH were, in effect, beyond challenge.

## Description of the project

Typically, housing of® ces manage the following:

l applications for tenancy

tenant transfers

l reactive repairs, reported by tenants

l cyclical repairs, to maintain and upgrade properties

l rent accounts

rent arrears

l void (empty) properties

l neighbour disputes

estate administration

l special needs tenants

l tenant participation

® nance

With regard to current IT resources, the organization as a whole had two mainframe based systems; an accounts package and a modular package to support all housing management processes. They were both installed about two years ago. The housing management package is known in this report by the pseudonym \`Housing Management System’ (HMS). It was being implemented on a modular basis, gradually replacing a previous system. The following modules were in use:

l rent and services

l property

tenure

l rent registration

The following modules were available but not yet in use:

l voids (empty properties)

repairs (the pilot project implemented this module for its purposes; the results are discussed below)

l allocations

The starting point when the STAMP of® ce opened, was that each member of staff had a workstation running Windows for Workgroups 3.11 and Lotus Smartsuite, networked within the of® ce, and with connections to the central mainframes.

The STAMP team initiated a number of novel ways of working:

(1) A telephone-based team. A freephone system was installed, and tenants were encouraged to use this. The phones were answered by any member of the team and the aim was that eventually all but the most esoteric of calls could be dealt with immediately by the person answering the phone. This replaced a previous system in which each tenant was assigned to a particular housing of® cer and contacts were by tenant visits to the of® ce, letters and occasional calls.

(2) A single contractor for reactive repairs. A telephone line was installed in the contractor’s of® ce, with a separate freephone number. A terminal was also installed, and the contractor had access to the repairs module of the HMS. The contractor answered the phone identifying themselves as the repairs section of MIH. They were able to organize all repairs themselves, provided those repairs were below a certain total price, and of a type pre-de® ned as \`OK to go ahead’. In addition to organizing the repair, the contractor was expected to record it on the HMS (simultaneously checking that the repair was of the \`OK to go ahead’ type), and to use that system to invoice MIH. This innovation is an example of business network redesign whereby IT infrastructure is used to rede® ne the boundaries of trading units, enabling them to come together as a virtual company (Venkatraman, 1991).

(3) Surgeries for three half days per week, in different places within the geographical area covered by the project. These were each manned by one housing of® cer. These were to deal with situations where face to face contact was required (for example, picking up keys to view properties). Again, the aim was that the majority of queries should be answered immediately at the surgery, and not referred back to other housing of® cers.

(4) A specialist social work agency for welfare support for vulnerable tenants.

(5) Accounting support within the team, so as to lessen the team’s dependence on centralized functions.

(6) A local lettings policy. As the area in which the team operated was not a popular one, the waiting list was short. There were problems of instability as people tried to move to new areas. Therefore a lettings policy was developed which allowed \`under-letting’ in certain unpopular roads (letting houses of a larger size than the minimum requirement for a tenant, so that the tenant could stay if their family size grew), and which favoured people for whom the area was their ® rst choice, or who had connections in the area and were therefore likely to stay. This was different from, and simpler than the well-established system used by the rest of the organization in which tenants were awarded points for housing need, and those were matched to the points required to be given a certain house.

(7) A \`borderless’ of® ce. The telephone-based working and surgeries already implied that everyone had to be prepared to do the work as required. Attempts were made to minimize the rigidity of job descriptions. An atmosphere was fostered in which questioning everything was welcome, and individual suggestions for change were always taken seriously.

## The case study: methods used

The authors were brought into the project to provide IT support, and to provide help with analysing further IT needs. One author was engaged on a six-month full-time contact with MIH as a whole; the other author provided eight days of consultancy. Initially, all that was known was that the project required support for situations of rapid change. It was necessary to adopt a methodological approach, and an IT support mechanism, that were able to re¯ ect the dynamic situation.

## Strategic user-centred design

The ideas of federation advocated by Handy as underpinned by the precept of subsidiarity. The rationale is that as the rate of change of business goals increases, so the only way of ful® lling these goals is by having teams whose members can work with ¯ exibility and respond quickly to changes. It is implicit that it is right for users at the local level to own operational goals and to be able to change them as circumstance dictates. It follows that the IT support which serves the goals must be designed from a user-centred approach.

The aim was to ® t the IT support to the changing needs of the organization and to enhance the quality of the systems upon which the staff depend. Initial discussions with staff at a team-building workshop showed that they were well motivated, having all volunteered to come onto the team because of a belief in its goals, and had a clear willingness to innovate and tackle problems. This innovative climate continued to generate requirements for technical change. Meeting these technical requirements proved to be challenging. The user-centred process modelling method which was adopted explored the interaction between agents in the process (e.g. tenants and housing of® cers). These interactions were modelled and then the goals of each interaction were given by the users. The question that then followed was to consider the contribution of IT systems to these goals. For example, a tenant possesses a goal \`seek re-housing’. A housing of® cer possesses the goal \`re-house tenant or provide reasons for not doing so’. The work considered how the IT system serves the housing of® cer in seeking the achievement of this goal.

## Evolutionary software development

Information gathering was done informally as an IT specialist became part of the team (see below) and more formally through interviews with each member of the STAMP team, and with key IT personnel supporting the mainframe systems. Most of these interviews focused upon the nature of the tasks undertaken by the interviewee, leading ultimately to a model of goals and activities. This in turn led to a consideration of the contribution that IT could make within the framework of existing activities or by offering new capabilities to \`re-engineer’ the activities. Ideas were input by all parties (interviewees, interviewer). The emphasis upon goals allowed the creation of role-based models which compartmentalized activities according to the goals that they serve. These role-based models were then presented to the team. The philosophy of the design was that it should never be presumed that the IT system was \`right’ . As the goals of the organization change so the activities would change and new capabilities could be asked of the IT support system.

The process modelling method interpreted \`goal’ in a restricted, operational way. It was not concerned alternative strategies for the organization or individuals within it. It simply sought to relate what users wanted to do tactically to the support services they required. The need to consider the more fundamental goals of STAMP did not arise. This is probably due to the fact that it is a small team with a well-de® ned remit and that all users had volunteered to become part of it.

## Information Technology support

The industry is set up on a basis where IT experts provide \`solutions’ to problems which are rarely wholly technical but are characteristically socio-technical. Thus there is a fusing of IT expertise and business expertise, which whilst plausibly a bene® cial state of affairs can lead to a detrimental technocracy wherein the power to control the technology (a technical exercise) affords power to control the business (a social exercise). Thus, users no longer have power over and responsibility for the tools they use at work but seemingly come to be regarded as specialist intelligent \`processors’ on the periphery of the system. Clearly, this runs contrary to the goals of user-centred design!

In the project the practical solution was to base an IT expert full-time in the team. One of the authors became a full-time member of the team for six months, with complete ¯ exibility to write their own job description. In addition to ful® lling various IT needs the work included sharing the general team duties (e.g. answering telephone calls from tenants). This meant that the IT expert became, in the words of one of the central IT support team \`probably the only member of IT in the whole organization who had ever spoken to a tenant.’

The role of the local IT expert was to facilitate and coordinate user developments by providing consultancy on the best IT platform to use (e.g. PC database, work¯ ow package, mainframe database), specifying new uses of existent applications, providing new ones, and agreeing the interface with other IT systems (e.g. how data should be updated). It also included \`hand holding’ and ad hoc training required to facilitate end user implementation. In this situation, some standard system analysis and design techniques, notably relational data analysis, were used.

Although the role of the HMS had been called into question, the functionality of two further modules was required; that of repairs and that of allocations. There was discussion at team meetings and with central IT support, as to whether this functionality should come from implementing the modules, or from implementing new applications with interfaces to the modules. There was at this stage no clear best method of proceeding ± implementing further modules would allow further integration with the rest of the system, but would mean increasing the in¯ uence of the legacy system. Developing a speci® c application would mean that the team could de® ne one directly relevant to their own needs and attempt to produce something which would be robust to change, but would reduce integration with the rest of the system.

In this situation of uncertainty, it was decided to experiment with two diametrically opposed solutions:

(1) An applications database would be written using a PC database, and would interface with the mainframe via replication. It would be regarded as a pilot for developments which involved the end user and IT support working closely together.

(2) Use of the mainframe repairs module would be implemented ahead of the rest of MIH. Preparing to implement this module for the rest of MIH had already taken more than a year’s elapsed time, and involved teams of up to ® ve housing of® cers and building supervisors on a full time basis during that time. Yet implementation was still incomplete. Therefore, the indications were that using this module would present dif® - culties. Nevertheless, the decision was taken to trial it as it was important to gain a full understanding of the capabilities and weaknesses of the HMS in supporting the project’s needs.

## Case study: speci® c results

## Strategic user-centred design

A prominent conclusion was that easy access to data would signi® cantly aid the daily work activities of the team members. Super® cially, the problem was not complex. The users knew what data they required. The support for it was generally available. However, it was spread amongst the HMS, miscellaneous applications and paper-based ® les. The HMS had particular usability problems distributing a wealth of detail over a number of screens. Many of the new ways of working such as the telephone-based teams, surgeries and \`borderless’ of® ce demanded that access to data be easy and in one place.

Having identi® ed the critical importance of data, further discussion was then based on three issues.

(1) The ability of the HMS to hold the data required. Central IT personnel were able to demonstrate that the system recorded most of the data required. However, information shortages did occur because of reluctance to use the system and as a result of a decision to only include data current from the time when the system was implemented.

(2) The dif® culties inherent in using the HMS. Use of the system was described by one member as \`signi® cantly adding to the stress of the job’ . Two members of the team asked why basic information on a tenant could not be contained in one screen. This latter sentiment was echoed elsewhere in the organization, in informal conversations. It arose in using the system for responding to rent queries. It seemed that somebody, somewhere, had assumed that rent queries would be dealt with by letter. The package would give a great deal of information spread over many screens. When STAMP developed a telephone-based way of working, the need to access several screens to answer one query suddenly became a major drawback. They wanted a cogent summary to give to a tenant rather than a lot of detail.

(3) Solutions to the mix of paper and mainframe sources were discussed, and led to recommendations for a Document Image Processing system, coordinated with the mainframe services via a document management system. In addition, there were some areas where easy access to the rules governing a particular procedure were required. Various work¯ ow packages were examined in this respect, with particular emphasis being paid to those which allowed users to de® ne and change short \`strands’ of work¯ ow. The intention was to explore a model where information is largely coordinated between a series of on-screen \`in trays’ , rather than by accessing databases. A complex, programmer-de® ned work¯ ow system was regarded as an unhelpful solution; in many ways one of the problems with the current system is that data is intricately linked with processes in interdependent ways.

## Support of repairs and allocations

The new, single contractor-based repairs system demanded a software solution which logged all repair results, and then allowed invoicing of them, monitoring of repairs and prices, and linking of repairs to other housing data.

Using the HMS in this respect was not regarded as successful. An inordinate amount of resources was required to produce the simple screens and reports of repairs done and invoices paid, and four months after implementation was still not working adequately. Complexity had been reintroduced as the needs of the project were made to ® t around the concepts for which the system was designed. Findings could be summarized:

(1) Specifying the use of the system was extremely time consuming, and the complexity militated against getting it right ® rst time.

(2) Any subsequent changes would involve the same level of complexity, thus the system could not be regarded as usable in a situation of evolving process.

(3) The centralized structure of the IT system made a nonsense of the federal structure of the organization. Any decision made by the STAMP team forced certain \`paths’ to be taken which the rest of the organization would then have to follow. In a similar vein, any decision made at a particular time froze the use of the system and thus forced future processes to remain similar to those they replaced.

(4) The system was unwieldy. Several screens were required to perform a simple process. Some links between screens could only be made by keeping records on paper. For example, invoicing a repair could only be done by the internal number assigned to that repair by the system. This internal number cannot be read within the invoicing module; it had to be reinput. While this makes sense for the original process for which the system was designed, it presented great dif® culties in the project.

(5) The fact that the data could only be accessed and updated from several unconnected screens meant that the only way for the contractor to present information was by being on-line all day ± an expensive option that also proved to be unreliable. Requests had to be made for reports to be written in-house to allow access to very simple pieces of information.

## Evolutionary software development

The allocations module was developed on a PC database. One of the authors designed it in such a way as to ensure relational integrity and alignment with data on the mainframe. The original interface was designed by IT personnel with close contact with the users. The principle that evolved out of this work was that ¯ exibility could be best provided by creating a minimum speci® cation that would be resilient to many circumstances: many of the designer’s suggestions for increased functionality were turned down as having too small an impact on the way of working, and having a price in terms of increasing the rigidity of the system. Users were trained to use the database, and encouraged to produce new interfaces as required. It was pointed out that new data requirements, or very complicated interfaces should involve IT personnel. The project is still at an early stage, but indications are that this is a prototype with potential. It allows some integrity with central data, while at the same time giving users an easy interface, and the power to change that as their requirements change over time. Its resilience to change over time has not been substantially tested because of the case study timescale, and the issue of con® guration management remains as one that has to be addressed.

## A strategic structure for Information Systems

Having identi® ed that the federally based replicable database had greater potential, the need then arose to place this within an IT strategy which allowed for changes of the business both over space ± different of® ces would do different things ± and time. A paper was drawn up in which a federal structure for IT was suggested (Dawson et al.). Data was classi® ed into that which should be kept centrally as core data, either because it would always be required by the core business (e.g. basic information on houses) or would be required by law, that which could usefully be held centrally, because most people would need it, and that which could be kept only in the of® ces. Of the data that had to be kept centrally, timescales were identi-® ed to see which data had to be always up to date, and therefore should be entered in real time, and that which had to be accurate within a certain timescale, and so could be maintained by replicable databases. At this stage, it is only possible to say that this map made intuitive sense; timescales have not allowed us to test it further.

## Case study: general results

Internal surveys to date indicate that the project is ful® lling many of its objectives ± for example, tenant satisfaction has increased (Wilkie, 1995). We limit our discussions to the way in which IT related to the ful® lling of those objectives.

An atmosphere of \`IT empowerment’ was developed. This came from several sources:

(1) Developing the \`handholding’ by on site IT support into informal education sessions on certain subjects ± for example, the structure of File Manager, the use of Schedule+ ± as these were identi® ed by users.

(2) Involving users in the strategic decision making via the user-centred design (where one member of the team noted that it was \`good to ® nd that IT people were able to listen’)

(3) Involving users at an early stage in high-level technology investigations, such as DIP demonstrations.

(4) Acceptance that end-user solutions would be produced, as it was obvious from the ® rst three weeks of the project that this would happen whether the central IT unit thought it was a good idea or not. Therefore IT support concentrated in ensuring the robustness of these solutions by directing them towards the best platform, giving design advice, etc.

The team’ s attitude towards the time spent on ITbased activities was strategic. They were willing to spend time in mastering new technology which would help them with their job in the future. Team members voluntarily worked at home to learn how to use PC applications, and to read up on new technologies. On the other hand time spent making up for the inadequacies of the present system was bitterly resented. Very fast requirements analyses could be made when the software developer was also a user of the system. This was important if an environment to allow constant software evolution was to be achieved. An IT role of de® ning strategic IT architectures arose out of the ® ndings of the team, rather than the team being provided with that architecture by IT.

The development of speci® c software was characterized by a natural accent on satis® cing. One of the most notable ® ndings was that users often requested less functionality rather than more. There were probably several reasons for this. Firstly, simple systems allow user discretion and ¯ exibility. They are more resilient. Secondly, when the users have so much control of their IT strategy, they can see that the request for one facility will be at the expense of another. In a small cooperative of® ce such as the case study, a natural prioritization occurred, driven by users. The team owned the productivity goals as discussed above. In this context, it was interesting to note that, while certain productivity-based enhancements were requested (e.g.

reduction of data input), there was a stronger accent on IT systems which were pleasant to use, and over which the user had some control.

Despite the general success of the project, the team was restricted by its inability to adapt the legacy housing management system to its needs. The legacy system was unwieldy to use, ill-adapted to the new tasks required of it and very dif® cult to change. Not only was it unsatisfactory in itself, but it introduced some quite fundamental limitations upon the STAMP team’ s ability to rationalize their work. STAMP faced a classic legacy system problem. Although they had instituted new ways of working and some new software applications to support them, they still found it very dif® cult to work with the core housing management package.

Unfortunately for the needs of a dynamic project, it was not possible to analyse these results over signi® - cant timescales. Therefore certain results are untested, notably the con® guration control of the core system, and the development of users’ attitudes towards the new IT support methods and structure over time.

## Conclusions

It is frequently argued that software systems can transform organizational operations. Recently, there have been many case studies presented which argue for a radical approach whereby existing organizational structures and operations are expendable, and new structures be wrought to exploit the power of IT (Hammer, 1990; Davenport, 1993). This case study tells a different story. MIH have adopted an innovative approach. They have reinvented their structure by initiating a move to a federal structure. This is done so as to uncover the bene® ts of ¯ exibility and enterprise that are advocated by Handy (1992). Among MIH’s stated goals are the achievement of ef® ciency bene® ts, improved services and increased staff morale. It has been accepted by the organization that effective use of IT systems is a fundamental part of the jigsaw of innovations by which these bene® ts might be attained. In order to facilitate the greatest possible bene® ts from IT systems, a user-centred design paradigm has been adopted and the organization has had to confront the need to rede® ne the way in which IT support is delivered. Through this latter aspect we see a blurring of the boundary between the operational team and the IT support system. An IT specialist has been working with the operational team and sharing the operational workload. Guided by this specialist the users themselves have been developing their IT skills so that increasingly as new needs arise they can tailor systems themselves. Extrapolating these trends, we anticipate a new set of problems for IT specialists. On the one hand, a greater premium is placed on their ability to understand, and take part in, the operation of the business. This implies that the specialist develops his/her skills both as participant and teacher and becomes less the product or solution provider. On the other hand, as uncoordinated local initiatives grow in federal structures, the IT specialist is faced with new problems such as the support of different tool-sets, the integration of functional areas and the coordination of data so as to maintain the integrity of the core needs of the organization.

The case study suggests that a scenario of usercentred design and new roles for IT staff is challenging but healthy. It is not, however, enough. The case study clearly shows that IT \`support’ systems that cannot be changed to serve the changing circumstances of the organization are not \`support’ systems at all. They are obstructive. They constrain the development of the organization. So it has been in this case study. Innovative thinking, new methodology, and new roles for IT staff were not enough. The organization is stil faced with a legacy system problem. It has invested heavily in a system which now bounds its development. Any attempt to break free of this constraint seems to be problem-laden for it is the technical nature of IT systems that they serve a ® xed set of circumstances. One ® xed-state solution replaces a previous one. Although there is widespread recognition of the problem of legacy systems, the signi® cance of maintenance and the need for adaptive systems, an evolutionary paradigm for system development is not yet established.

In summary, the case study validates the intentions of recent literature which advocates the blurring of the boundary between IT support personnel and the users of IT themselves. From the methodological vantage point, a user-centred paradigm seems apt. Of course, many further questions remain. That software systems should be thought of as intrinsically evolutionary represents a fundamental challenge. It is a challenge which extends to our consideration of the nature of software systems themselves. Are these products like any other which serve a ® xed set of circumstances only to be disposed of when the circumstances change? The case study suggests that a scratch formula for evolutionary system design methods which can be posited from Trisoglio’s (1995) strategies for complexity. First, the system and the process of its development must be adaptable. This requires that there are mechanisms for the adaptation of IT systems to environmental changes. Secondly, the system should be resilient. This may require that simpler systems be built rather than more complex ones. The operational ¯ exibility of the users is critical. Thirdly, diversity should be encouraged.

## Evolutionary software development

Different organizational units and individual users may be encouraged to adopt different solutions. Their relative merits can then be compared through an informal or formal process of comparison. In this way, the organization might learn.

## References

Ackoff, R.L. (1981) Creating the Corporate Future (John Wiley and Sons, Chichester).

Checkland, P. (1981) Systems Thinking, Systems Practice (John Wiley and Sons, Chichester).

Dasgupta, S. (1991) Design Theory And Computer Science (Cambridge University Press, London).

Davenport, T.H. (1993) Process Innovation: Re-engineering Work Through Information Technology (Harvard Business Press, Boston).

Dawson, S., Leonard, J., Kawalek, P. (1995) Insights from the STAMP project, Internal MIH report. Merseyside Improved Houses, 46 Wavertree Road, Liverpool L7 1PH, UK.

Dearden, J. (1987) The withering away of the IS organization. Sloan Management Review, 28 (4) 87± 91.

Downs, E., Clare, P., Coe, I. (1992) Structured Systems Analysis and Design Method: Application and Context (Prentice Hall International (UK) Hertfordshire).

Eason, K. (1988) Information Technology and Organisational Change (Taylor and Francis, London).

Fitzgerald, B. (1996) Formalized systems development methodologies: a critical perspective. Information Systems Journal, 6 3± 23.

Hammer, M. (1990) Re-engineering work: don’t automate obliterate. Harvard Business Review, July± August 104± 112.

Hammer, M., Champy, J. (1993) Re-engineering the Corporation, A Manifesto For Business Revolution (Nicholas Brealey Publishing, London).

Handy, C. (1992) Balancing corporate power: a new federalist paper. Harvard Business Review, November± December.

Handy, C. (1993) Beyond 2000: The intellectual organisation. The Financial Times, 29 December, pp.59± 72.

Handy, C. (1995), Nothing to fear from the F-word. The Independent, 6 February.

Harrington, J. (1991) Organizational Structure and Information Technology (Business Information Technology Series, Prentice Hall, Hemel Hempstead).

Hayward, D. (1995), Death by a thousand cuts. Computing, 6 July.

Kawalek, P. (1995) An introduction to a process engineering approach and a case study illustration of its utility, in Proceedings of IFIP Working Group 5.7, Working Conference on Re-engineering the Enterprise Browne, J. (ed.) (Chapman and Hall, London).

Keen, P.G.W. (1988) Roles and Skill Base for the IS Organizationin Transforming the IS Organization, Elam, J., Ginzberg, M.J., Keen, P. W. G. and Zmud, R. W. (eds) (ICIT Press, Washington DC).

Kelleher, D. (1995) Business programmes and information systems methodologies. Information Systems Journal, 5, 137± 157.

LaBelle, A. and Nyce, H. E. (1987) Whither the IT organization? Sloan Management Review 28, (4) 75± 85.

Lee, D.M.S., Trauth, E.M., Farwell, D. (1995) Critical skills and knowledge requirements of IS professionals: a joint academic/industry investigation. MIS Quarterly, September, 1± 27.

Lehman, M.M. (1991) Software engineering, the software process and their support. Software Engineering Journal, September, pp.243± 258.

Lehman, M.M. (1992) Evolution of processes and process models. IOPener, Newsletter of the IOPT Club 1, 4 May 1992, Praxis Systems plc. Bath.

Leonard, J., Pardoe, J., Wade, S. (1988) Software engineering University of Liverpool, IEE/BCS Conference Publication, 290.

Lientz, B., Swanson, E.B. (1980) Software Maintenance Management (Addison-Wesley, New York).

Macauley, L.A., Fowler, C.J.H., Kirby, M., Hutt, A.T.F. (1990) USTM: a new approach to requirements speci-® cation. Interacting With Computers 2 (1), 92± 118.

MIH (1995) Merseyside Improved Houses Yearbook, 1995, Merseyside Improved Houses, 46 Wavertree Road, Liverpool L7 1PH, UK.

Mumford, E. (1983) Designing Participatively (Manchester Business School Press, Manchester).

Olerup, A. (1991) Design approaches: a comparative study of information system design and architectural design. The Computer Journal, 34 215± 224.

Pfeffer, J. (1978) Organizational Transformation AHM Publishing Co., Arlington Heights.

QAI (1985) Quality Assurance Institute, Research Report, (Orlando, Florida).

Schecter, D. (1991) Critical systems thinking in the 1980s: a connective summary in Critical Systems Thinking: Directed Readings, Flood, R.L. and Jackson, M.C. (eds) (John Wiley and Sons, Chichester).

Sch”n, D.A. (1971) Beyond the Stable State (Random House, New York).

Scott-Morton, M.S. (ed.) (1991) The Corporation of the 1990’s: Information Technology and Organisational Transformation (Oxford University Press, Oxford).

Senge, P.M. (1990) The Fifth Discipline: The Art and Practice of the Learning Organization (Century Business Press, London).

Simon, H.A. (1981) The Sciences of the Arti® cial (second edition) (MIT Press, London).

Texas Instruments Incorporated (1988) A Guide To Information Engineering Using The IEF (second edition).

Trisoglio, A. (1995) Managing Complexity, Research Programme on Complexity (London School of Economics and Political Science, London).

Venkatraman, N. (1991) IT induced business recon® guration, in Information Technology and Organizational Transformation, Scott-Morton, M.S. (ed.) (Oxford University Press, Oxford).

Warboys, B. (1995) The software paradigm. ICL Technical Journal, 1, May.

Wastell, D.G., White, P., Kawalek, P. (1994) A methodology for business process redesign: experiences and issues, Journal of Strategic Information Systems, 3(1).

Watkins, J. (1994) BPR in the UK retail ® nancial services sector. Business Change and Reengineering, 1(4) 38± 48.

Wilkie, F. (1995) STAMP South Team Area Management Project Evaluation Report, August 1995 Internal MIH report, Merseyside Improved Houses, 46 Wavertree Road, Liverpool L7 1PH, UK.

Winter, M., Brown, D., Checkland, P. (1995) A role for soft systems methodology in information systems development. European Journal of Information Systems 4, 130± 142, (Operational Research Society, Ltd., Stockton Press, Basingstoke).

## Acknowledgement

The authors wish to thank everyone at Merseyside Improved Houses, especially the STAMP team and the members of the IT section who worked with them.

## Biographies

Peter Kawalek is a Research Associate in the Informatics Process Group, Department of Computer

Science, University of Manchester. The principle concern of his research is the development of process modelling methods which address problems of usability, integration and evolution of complex software systems. During the past four years he has undertaken a number of collaborative projects with public and private sector partners. These include projects in the insurance, telecommunications, software engineering and local government domains.

Af® liation and address: Informatics Process Group, Department of Computer Science, University of Manchester, Manchester M13 9PL.

Dr. Jenny Leonard worked in IT in the UK from 1980 to 1995, where she held positions in the academic, commercial and public sectors. She is now Associate Director for Information Systems at the University of Newcastle, New South Wales, Australia, where she is introducing new management structures and working processes to support the implementation of new administrative systems.

Address: Information Technology, University of Newcastle, University Drive, Callaghan, NSW 2308, Australia.
