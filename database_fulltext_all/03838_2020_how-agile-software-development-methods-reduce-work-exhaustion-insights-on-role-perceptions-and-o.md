---
otero_id: 3838
otero_key: "E2TQE2DC"
title: "How agile software development methods reduce work exhaustion: Insights on role perceptions and organizational skills"
authors: "Viswanath Venkatesh; James Y. L. Thong; Frank K. Y. Chan; Hartmut Hoehle; Kai Spohrer"
year: "2020"
journal: "Information Systems Journal"
doi: "10.1111/isj.12282"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
R E S E A R C H A R T I C L E

# How agile software development methods reduce work exhaustion: Insights on role perceptions and organizational skills

Viswanath Venkatesh<sup>1</sup> | James Y. L. Thong<sup>2</sup> | Frank K. Y. Chan<sup>3</sup> | Hartmut Hoehle<sup>4</sup> | Kai Spohrer<sup>5</sup>

<sup>1</sup>Department of Information Systems University of Arkansas, Fayetteville, Arkansa

<sup>2</sup>Department of Information Systems, Business Statistics and Operations Management, The Hong Kong University of Science and Technology, Kowloon, Hong Kong

<sup>3</sup>Department of Information Systems, Decision Sciences and Statistics, ESSEC Business School, Cergy-Pontoise, France

<sup>4</sup>Department of Enterprise Systems, University of Mannheim, Mannheim, Germany

<sup>5</sup>Department of General Management and Information Systems, University of Mannheim, Mannheim, Germany

## Correspondence

Viswanath Venkatesh, Department of Information Systems, University of Arkansas, Fayetteville, AR. Email: vvenkatesh@vvenkatesh.us

Funding information Research Grants Council of Hong Kong, Grant/Award Number: GRF693313

## Abstract

Agile methods are widely used in the software industry as a way to more rapidly develop and deliver new software. They define iterative work processes, advocate selforganization and openness for change, and prescribe how software developers interact with each other and external stakeholders. Despite their popularity, it is unclear how agile methods influence work exhaustion in software developers and how developer skills play into this effect. On the one hand, agile methods may reduce software developers' work exhaustion by levelling out their workload across the entire duration of a project. On the other hand, agile methods exert a high level of pressure on software developers to continuously deliver working software, create many intensive social interactions, and to frequently adapt to changes. In light of these effects, prior research could not explain why some software developers become less exhausted from using agile methods, whereas others perceive the exact opposite. Based on the job demand-control model, we develop a theoretical model connecting agile method use to individual developer skills and to two established determinants of employee exhaustion: role conflict and role ambiguity. We tested our research model in a field study among 1894 software developers in 217 project teams that used agile methods. The random coefficient modelling results show that agile method use facilitates the achievement of clear and unambiguous role perceptions and thereby reduces work exhaustion in developers, particularly if developers possess the organizational skills to effectively interact with others in their organization. We highlight implications for theory on the individual-level effects of software development methods and provide practical insights for software companies.

K E Y W O R D S

agile systems development, developer skills, organizational skills, role ambiguity, role conflict, work exhaustion

## 1 | INTRODUCTION

With a global spending volume of nearly US\$400 billion in 2018 (Costello & Omale, 2019), the enterprise softwar industry constitutes a significant segment of the global economy that has become increasingly fast paced in recent years (Fitzgerald & Stol, 2017; Gallagher, Kaiser, Simon, Beath, & Goles, 2010; Sarker & Sarker, 2009). For example, rapid technological developments, fast changing market dynamics, a growing variety of data sources, and increasing needs for enterprise software to span multiple domains of business force software companies to adapt more quickl to altering conditions, to continuously redefine development processes and roles, and to facilitate the ongoing acqui sition of new skills in their workforce (Akter, Wamba, Gunasekaran, Dubey, & Childe, 2016; Davis, Niederman, Greiner, Wynn, & York, 2006; Fosso Wamba et al., 2017; Ke & Zhang, 2010; Weerakkody, Irani, Kapoor, Sivarajah, & Dwivedi, 2017). These rapid changes place great demands on software companies and especially on their softwar developers who consequently suffer from increased stress and work exhaustion (Thong & Yap, 2000; Venkatesh Rai, & Maruping, 2018; Watson, Boudreau, York, Greiner, & Wynn, 2008; Windeler, Maruping, & Venkatesh, 2017) Increased work exhaustion in software developers is highly problematic because it accounts for more than 30% of al technical development errors (Furuyama, Arai, & Iio, 1994; Furuyama, Arai, & Iio, 1997), causes substantive maintenance costs, impacts development teams' performance, and can derail entire projects (Venkatesh et al., 2018; Wind eler et al., 2017). In addition to negative effects on their performance, high work exhaustion negatively impacts software developers' health and makes them more likely to quit their jobs (Moore, 2000; Ply, Moore, Williams, & Thatcher, 2012). In order to achieve high productivity and long-term retention of their developers, it is therefore critical for software companies to understand which work conditions and skills help their developers to alleviate wor exhaustion during software development.

The use of software development methods is one important factor that can reduce or increase software devel opers' stress and work exhaustion (Drury, Conboy, & Power, 2012; Furuyama et al., 1997). As such, software devel opment methods affect developers' daily work by defining roles and interactions, partitioning projects into smaller steps, and laying the foundations for team work and the division of labour (Fitzgerald, 1998). Particularly, agile devel opment methods, such as extreme programming (XP) and Scrum, have become widespread in industry during recent years because they facilitate adaptation to changing environments and customer needs (Lee & Xia, 2010; Maruping et al., 2009a, 2009b; Yu & Petter, 2014). These agile methods entail a people-centric, iterative development process that is based on self-organizing teams of software developers who continuously solicit and evaluate feedback on their progress in developing a desirable software product (Hoda & Murugesan, 2016). Although experience in agil methods has become an important occupational qualification (Cram & Newell, 2016; Dingsøyr, Nerur, Balijepally, & Moe, 2012), it is largely unclear how the use of agile methods actually affects individual developers in their job (Tripp, Riemenschneider, & Thatcher, 2016). Industry reports are particularly inconsistent regarding the effects of agile methods on the work exhaustion of software developers. On the one hand, some developers report that th use of agile methods helps them to achieve a sustainable, less exhausting working pace (Laanti, 2013). On the other hand, there are developers who report increased exhaustion from the use of agile methods due to the “constant strive for improvement, the relentless drive for feedback, the subsequent changes in direction and the incessant social interactions” (Balbes, 2017). Software companies, therefore, have contradictory guidance regarding the ques tions how the use of agile methods affects their core resource, namely, software developers and why some devel opers become more exhausted than others when using agile methods.

Prior research has recently started to examine the effects of agile software development on individual developers, eg, regarding job satisfaction, job autonomy, and work exhaustion (Hoda, Salleh, Grundy, & Tee, 2017; Tripp et al., 2016; Tuomivaara, Lindholm, & Känsälä, 2017). With regard to software developers' work exhaustion, extant research focused primarily on whether agile methods for project management indeed help to balance the workload of development projects across the entire project duration, thereby preventing exhausting phases with extrem workload prior to milestones or toward the end of a project (Tuomivaara et al., 2017). Although valuable, such a pro ject management perspective does not account for differences between individual developers and does not explain why some developers may become more exhausted than others when using agile methods. A possible reason fo such differences could be that software developers can be more or less skilled in coping with the demands of specific software development methods. For example, agile methods demand frequent and intensive social interactions and tremendous informal communication (Hummel, Rosenkranz, & Holten, 2013) that may be more exhausting for those developers who lack the skills to effectively engage in such activities. Yet, research currently provides little insight into how agile methods influence work exhaustion in software developers or what role individual developer skills play in this regard. This is a theoretically and practically relevant issue because psychological theories suggest that work exhaustion often results from a mismatch between employees' capabilities and the demands of their work envi ronment (Häusser, Mojzisch, Niesel, & Schulz-Hardt, 2010; Jung, Schneider, & Valacich, 2010; Karasek, 1979 Karasek et al., 1998). Failure to understand the role of individual developer skills in the relationship of agile methods and software developers' work exhaustion consequently limits our ability to achieve a more complete understanding of how to manage and staff contemporary software development projects. Against this backdrop, our research aim to answer two overarching research questions:

1. What is the impact of agile method use on work exhaustion in individual developers?

2. How do individual developer skills influence the relationship of agile method use and developers' work exhaustion?

To address these questions, we rely on and extend an established theory. First, we draw on the job demand control model (JDCM; Karasek, 1979) to understand the influence of agile methods on software developers' work exhaustion. Second, we draw on the taxonomy of information systems (IS) skills by Nelson (1991) to understand the role of software developer skills in this relationship. More specifically, we focus on (a) role conflict and role ambiguity to theorize why agile method use influences work exhaustion in developers (Häusser et al., 2010; Karasek et al., 1998; Van der Doef & Maes, 1999) and (b) organizational skills of developers to theorize how the skills of individual developers alter the effect of agile method use on work exhaustion (Gallagher et al., 2010; Lee, Trauth, & Farwell, 1995; Nelson, 1991; Wade & Parent, 2001). To date, systematic research that aids in understand ing the effects of agile methods on individual developers is scarce (Tripp et al., 2016; Tuomivaara et al., 2017) Scholars have therefore called for more theory-driven research to examine the consequences of agile method use in quantitative studies (Chan & Thong, 2009; Chuang, Luor, & Lu, 2014; Dingsøyr et al., 2012; Mangalaraj, Nerur, Mahapatra, & Price, 2014). We respond to this call with a field study on the influence of agile method use on soft ware developers' work exhaustion. To this end, we test our model in a field study among 1894 developers in 217 project teams.

## 2 | THEORETICAL BACKGROUND

## 2.1 | Agile software development methods and work exhaustion

The rise of agile software development has resulted in a variety of agile methods, such as XP (Beck, 2000), Scrum (Schwaber & Beedle, 2002), and Lean Programming (Poppendieck & Poppendieck, 2003). Although the various agil methods differ in the practices they comprise, all adhere to the same set of underlying values that they instantiate in different ways (Fowler & Highsmith, 2001). They advocate an iterative, people-centric approach to software devel opment that facilitates quick adaptation to changing business requirements, markets, and technologies and directs development efforts toward perceived customer value (Conboy, 2009; Ramesh, Cao, Kim, Mohan, & James, 2017) Agile methods, therefore, generally follow an incremental process that builds on self-organizing, empowered teams of developers who frequently interact with customers to solicit feedback on their development outcomes and adapt their targets and development activities accordingly (Hoda & Murugesan, 2016). There is persuasive evidence that agile methods benefit team performance and project outcomes (Hoda et al., 2017). As such, agile method us increases software quality and project performance by making development teams more responsive to uncertaint and requirements volatility (Lee & Xia, 2010; Maruping et al., 2009a, 2009b) and by letting them come to a more accurate and shared understanding of customer needs and development obstacles (Ghobadi & Mathiassen, 2016 2017; Yu & Petter, 2014).

Self-organization and continuous adaptation, which are germane to agile methods, necessitate that developers communicate frequently with their colleagues and customers, force them to confront potentially controversia opinions, and require them to coordinate their actions informally based on mutual adjustment rather than on explicit role descriptions or detailed process models (Conboy, 2009; Ghobadi & Mathiassen, 2017; Hoda & Murugesan, 2016: Matook & Maruping. 2014: Ramesh, Mohan, & Cao. 2012: Yu & Petter, 2014), In addition, agile methods mandate that developers continuously deliver working software and increase the value of their software product in each step (Drury et al., 2012). They enforce that developers identify issues with extant solutions, communicate with colleagues to draw on their team's combined expertise, and show extensive backup behaviou (Kudaravalli, Faraj, & Johnson, 2017). Although all this makes agile methods effective for improving outcomes of development projects (Lee & Xia, 2010; Maruping et al., 2009a, 2009b), it is not yet fully understood how these specific demands of agile methods affect the individual developers who need to fulfil them (Tripp et al., 2016). O the one hand, developers may benefit from increased job control through self-organization of their teams. On th other hand, the specific job demands entailed in agile methods may exhaust developers if they lack the skills to cope with the demands. In line with these contradictory views, industry reports show that some developers fee more exhausted from using agile methods whereas others see agile methods as a safeguard against work exhaus tion (Balbes, 2017; Laanti, 2013).

Prior research on software developers' work exhaustion and agile methods has primarily taken a project management perspective. It examined whether agile methods indeed help balance the workload of development projects across the entire project duration, a long-standing promise of agile methodology (Beck, 2000; Fowler & Highsmith, 2001). This line of work found support for a reduction of workload peaks and a subsequent reduction in developers' work exhaustion (Tuomivaara et al., 2017). However, research has remained silent about the effects of agile methods on developers' work exhaustion that go beyond balancing workload. As such, there are also developers who do not cope well with the demands of agile development, who feel that agile methods increase work stress and feel forced into exhausting activities by them (Laanti, 2013). Some developers have actually been found to struggle with their jobs when using agile methods and to become emotionally drained (Balbes, 2017; Ghobadi & Mathiassen, 2017). These ambivalent observations suggest that there are differences at an individua level that influence how exhausting agile methods are for software developers. For example, agile methods emphasize self-organization and adaptation, and thus require frequent and intensive informal communication as well as social interaction with team members, customers, and other stakeholders (Hummel et al., 2013; Sarker &

Sarker, 2009). However, not all developers are equally skilled in communicating and interacting informally (Wade & Parent, 2001). The effects of agile methods may consequently be related to individual software developers' skills and how well they fit with the demands of agile methods

To date, rigorous research on the effects of agile method use has not yet addressed these issues. It has, in fact largely overlooked differences between individual developers in coping with their job demands (Tripp et al., 2016) Yet, this topic is important because frequent failure to cope with the challenges of one's job, here created by agil methods, can have long-term effects such as burnout (Häusser et al., 2010; Moore, 2000). We turn to an established theory, ie, the JDCM, to help understand the effects of job demands and potential controls on employees' work exhaustion.

## 2.2 | A job demand-control perspective on agile methods

To better understand the impact of agile methods on software developers' work exhaustion, we base our research on one of the most impactful theories on organizational psychology, namely, the JDCM (Häusser et al., 2010 Karasek, 1979; Van der Doef & Maes, 1999). The JDCM holds that there are two central factors influencing employees' appraisal of their job and consequent psychological and physiological reactions: job demands—ie, activities and outcomes necessary to complete one's organizational tasks—and job control—ie, ability to direct or manage one's own work activities. The JDCM posits that employees working in a high-strain context, ie, when job demand are high and job control is low, are prone to suffering from negative impacts such as psychological stress, feelings of helplessness, and exhaustion (Van der Doef & Maes, 1999). In contrast, such adverse effects are less likely in low strain contexts, ie, when job demands are low and job control is high (Häusser et al., 2010)

In line with JDCM, software engineers have been found to experience high work exhaustion and low satisfactio when facing very high job demands (Schreurs & Taris, 1998). In addition to causing work exhaustion in software developers, overly high job demands impair team processes and harm work results if not managed adequately (Maruping, Venkatesh, Thatcher, & Patel, 2015; Windeler et al., 2017). In laymen's terms, “work exhaustion” is often used interchangeably with the term “job burnout” (Moore, 2000). Although there are more detailed conceptualiza tions of exhaustion and other physiological and psychological facets of burnout in prior research, work exhaustion is widely seen as an equivalent of burnout (Häusser et al., 2010). Consistent with prior IS literature (Moore, 2000), w therefore define work exhaustion as the depletion of mental resources in the workplace.

Software projects can put particularly high strain on software engineers by affecting their role perceptions, spe cifically role conflict and role ambiguity (Windeler et al., 2017). Role ambiguity refers to the degree to which a soft ware developer's role expectations are unclear (Rizzo, House, & Lirtzman, 1970). Developers who work in a group of interdependent members but have no guidance regarding their individual responsibilities may not know which task to complete in which order, how to communicate with external stakeholders, and how to evaluate their work (Häusser et al., 2010; Swanson & Power, 2001; Windeler et al., 2017). Although self-organization inherent to agile methods may support development teams in clarifying role expectations, prior work suggests that individual developers sometimes suffer from ambiguous role perceptions even when using agile methods. For example, Moe Dingsøyr, and Dybå (2010) state that Scrum leaves many important development activities unspecified and puts high demands on development team members to interactively clarify what needs to be done and by whom. Hoda and Murugesan (2016) emphasize that some developers perceive it as particularly challenging to clarify, select, and self assign their development tasks. Yet, elaborations of the individual-level factors that drive these challenges and corresponding empirical tests have been left to future research (Hoda & Murugesan, 2016). Although developers can work together effectively with either overlapping or nonoverlapping areas of expertise (Kudaravalli et al., 2017), it is important for each individual to know whether a task, be it self-assigned or assigned top-down, falls into one's are of expertise and responsibility or not (Faraj & Sproull, 2000). Otherwise, uncertainty about individual responsibilitie translates to role ambiguity.

Role conflict refers to the degree to which behaviours expected from an individual are inconsistent (Rizzo et al., 1970). For example, managers often need to balance software quality, functional scope, and resource consumption i development projects. They face role conflict if they are equally constrained by customer demands for quality and scope as by internal demands for minimized resource investments. Conflicting and ambiguous role perceptions are the oretically and empirically established causes of work exhaustion. They have frequently been examined in the JDCM lit erature (Häusser et al., 2010; Swanson & Power, 2001; Wong, DeSanctis, & Staudenmayer, 2007) and are linked to dissatisfaction, work overload, and turnover intentions (Joseph, Ng, Koh, & Ang, 2007; Moore, 2000; Ply et al., 2012) Yet, it is unclear how they relate to the use of software development methods or to the skills of individual developers

To understand individual differences in how exhausting the use of agile methods is for developers, we furthe examine individual developer skills because the evaluation of job demands and job control is generally influenced b skills (Karasek, 1979). In this regard, organizational skills refer to an individual's knowledge and capability to effec tively manage interpersonal communication, interpersonal behaviour, and group dynamics as a member of a work group (Nelson, 1991). In the past, scholars found that the work of software developers depended much more on technical skills (eg, skills in programming and the use of software packages) than on organizational skills (Gallagher et al., 2010; Lee et al., 1995; Nelson, 1991; Wade & Parent, 2001). Given the emphasis on people, interactions, and self-organization in agile methods (Hoda & Murugesan, 2016), this assumption may no longer hold in contemporary, agile software development.

## 3 | THEORY DEVELOPMENT

In light of prior work and the gaps discussed, we theorize that a larger extent of agile method use helps developer to better understand their roles and responsibilities, thereby reducing role ambiguity and role conflict and that orga nizational skills amplify this effect. More specifically, we theorize that organizational skills facilitate communication and mutual adjustment among developers that are particularly important during the use of agile methods becaus these methods require developers to engage in frequent personal interactions, confront controversial opinions of colleagues and customers, and informally align perspectives throughout a team. Lower role ambiguity and role con flict are then expected to be associated with lower work exhaustion. Figure 1 depicts these relationships that we develop further in this section.

## 3.1 | Use of agile methods

Although agile methods have been widely adopted, the software industry rarely relies exclusively on either agile or plan-driven methods (Ramesh et al., 2012). Once adopted, agile methods become instead part of an organization' portfolio of diverse software development methods that can be drawn on selectively, in sequence or in combination (Ramasubbu, Bharadwaj, & Tayi, 2015; Ramesh et al., 2012). Over time, software developers may therefore appl agile methods to varying degrees, alternate between plan-driven and agile methods, and even apply plan-driven and agile methods at the same time (Bick, Spohrer, Hoda, Scheerer, & Heinzl, 2018; Ramasubbu et al., 2015). We therefore conceptualize the extent of agile method use as the frequency and intensity with which developers apply agil methods in a particular project.

In order to complete their tasks successfully, software developers need to understand the role they play in their team, be aware of their own responsibilities compared with those of their team members, and coordinate their activi ties with their colleagues (Espinosa, Slaughter, Kraut, & Herbsleb, 2007; Faraj & Sproull, 2000; Zhang, Venkatesh, & Brown, 2011). Although this holds true for software development teams following plan-driven methods with special ized roles and for software development teams following agile methods with more flexible roles (Kudaravalli et al., 2017), we expect that the use of agile methods helps software developers to more effectively achieve clear and

![](/api/attachments/E2TQE2DC/fulltext/images/e834c09ee7337591c9fe9a9a1ea602981f3a909e27137933d7c4b73aacfa87eb.jpg)  
Note: All main variables at the individual level.

## F I G U RE 1 Research model

congruent role perceptions. As such, agile methods stimulate self-organization and continuous adaptation, entai short and comprehensible development cycles, foster the creation of shared mental models, and provide developers with a set of guiding core values (Conboy, 2009; Ramesh et al., 2017). These elements of agile method use can b expected to reduce both role ambiguity and role conflict for individual developers

More specifically, agile methods empower teams to self-organize and make relevant decisions about the design and implementation of the software product they are building. Such autonomy fosters feelings of self-determination (Deci & Ryan, 1985; Hoda & Murugesan, 2016; Wang, Schneider, & Valacich, 2015) that intrinsically motivate soft ware developers and help them to be more proactive about information gathering to define their own role (Ke & Zhang, 2011; Windeler et al., 2017). Using agile methods, developers can also more easily resolve situations of role conflict. Developers in self-organized teams are empowered to make relevant development decisions and can thus decide to follow the expectations that are more congruent with their team goals. Self-organization inherent to agil methods consequently provides software developers with a sense of control that reduces role conflict. Similarly, the core values underlying agile methods reduce the potential for conflicting expectations toward individual developers. For example, agile methods consistently emphasize software quality over following a process or creating detailed documentation. These core values guide decisions and thus reduce the chance for developers to get caught between conflicting expectations, for example, between the expectations of project managers pushing for clean documentation and process adherence on the one hand and customers pushing for the rapid and complete development of th software product on the other hand.

Lastly, agile methods help reduce role conflict through short, structured development iterations that entail col laborative interactions with team members and customers. Collaborative agile practices such as pair programming daily meetings, and continuous integration stimulate communication and exchange between developers about solu tion strategies, development obstacles, and intermediary work results. The use of agile methods thereby facilitates the mutual adjustment of developers and helps them establish shared perspectives that reduce the risk of conflictin role expectations toward individual developers. Short development cycles entail frequent exchange of software developers with customers and other stakeholders about product increments, customer needs, and development goals. These regular interactions help developers reduce the salience of the strong boundary between customers and developers. Plan-driven development methods typically span this boundary with specific roles and personnel (eg, business analysts) who often face role conflict because expectations toward them differ on the two sides of th boundary (Baroudi, 1985; Joseph et al., 2007; Speier & Venkatesh, 2002). Agile methods, by contrast, have cus tomers and developers interact frequently and force them to regularly discuss small product increments. These inter actions and discussions help both groups to align their expectations and reduce the chance of role conflict in developers. Thus, we hypothesize:

H1: The extent of agile method use will be negatively associated with role conflict.

Using agile methods, software developers engage in communication and knowledge sharing with team members and other stakeholders to self-organize their development activities. Developers can use these discussions to solicit more information about the expectations of team members, managers, and customers about them and about their work output. The frequent, informal discussions help to achieve a common understanding of requirements, chal lenges, and areas of developer expertise (Kudaravalli et al., 2017; Yu & Petter, 2014). They thereby reduce ambiguity in who should do what in a software development team and help each developer understand their personal role in it. In self-organized agile teams, members do not have firmly specialized roles (Hoda & Murugesan, 2016). Conse quently, informally exchanged knowledge about team members' expertise and mutual expectations allow developers in such teams to shape their own roles and get a clearer understanding of their responsibilities

Agile methods moreover make developers iteratively collect feedback from customers and team members that reduces uncertainty about their expectations. It helps establish clearly understood and agreed upon target visions for the next steps of a project. In particular, iterative evaluations of their work results allow developers to refin their understanding of the problem domain and even force them to explicitly adapt their goals (Ramesh et al., 2012). This aids in making developers' own expectations of themselves clearer and less ambiguous. Lastly, close col laboration enforced by agile practices, such as shared code ownership, pair programming, and shared coding stan dards, stimulates the transfer of tacit knowledge within a team through socialization (Dingsøyr et al., 2012) Imitating coding styles, design patterns, and problem-solving strategies of colleagues, for example, lets team mem bers implicitly come to joint perspectives on challenges and supports the emergence of common norms. The clos collaboration enforced by agile methods thereby results in clearer developer expectations of each other. Thus, we hypothesize:

H2: The extent of agile method use will be negatively associated with role ambiguity

## 3.2 | Organizational skills

Given that self-organization, continuous adaptation, and intensive collaboration are intrinsic parts of agile method use, software developers need organizational skills to effectively benefit from agile methods. As such, the beneficia effects of agile method use on role conflict and role ambiguity may be particularly pronounced for developers wit extensive organizational skills because organizational skills facilitate interpersonal interactions and direct communication that are crucial elements of effective agile method use. Whereas plan-driven methods build on specialized role definitions and authoritative task assignments by managers, generalist members of self-organized agile teams need to engage in discussions with their team to understand and clarify their implicit roles (Hummel et al., 2013). For example, developers may realize that their colleagues expect them to work on tasks that do not fit their own percep tions of their roles and responsibilities. Especially agile development teams are known to critically review selfassignment practices of their members and discuss individual task self-assignments in order to prevent undesired specializations of team members and knowledge silos (Hoda & Murugesan, 2016). Developers with better organiza tional skills can more easily understand the specific arguments of their counterparts in such discussions and can clar ify the situations based on sound argumentation and persuasive reasoning. Better organizational skills thereby allow developers to communicate more easily with their team members to reduce role conflict during agile method use. In contrast, lack of organizational skills may be particularly harmful for developers' role perceptions when using agile methods. As such, lack of organizational skills may result in a failure to resolve conflicting expectations in agile devel opment contexts because agile methods repudiate formal, specialized roles and hierarchies. Instead, they urge devel opers to distribute work and responsibilities in their teams based on informal communication and team processes (Dingsøyr et al., 2012). The distribution of roles and responsibilities in agile teams thereby becomes subject to group dynamics, and developers cannot point to formal role specifications that would help them make their point. Instead, they need to cope with group discussions and possibly more persuasive counterparts to resolve conflicting viewpoints on their roles, even though they may lack the skills to do so effectively. Developers in agile teams who lack organizational skills will therefore more frequently run into role conflicts with team members, customers, and managers that they are unable to resolve. Thus, we hypothesize:

H3: Organizational skills will moderate the negative relationship between the extent of agile method use and role conflict such that the relationship will be stronger at higher levels of organizational skills

Agile method use includes frequent, periodic meetings and discussions with customers and other stakeholders that aim at sharing knowledge and opinions to probe new ideas and adjust misguided developments (Ghobadi & Mathiassen, 2016). Individuals possessing better organizational skills may use these meetings to seek more effective clarification and understand existing expectations and requirements more easily. Moreover, collaborative agile practices, such as pair programming, build on the synchronized and joint cognitive efforts of developers that involves a significant amount of verbalizing ideas, putting forth own perspectives, and taking others' perspectives (Balijepally Mahapatra, Nerur, & Price, 2009; Mangalaraj et al., 2014). Developers with better organizational skills may more easily conduct these activities and thereby reflect more effectively on their activities, roles, skills, and responsibilities They may therefore face less role ambiguity when using agile methods. In contrast, developers who lack organiza tional skills may experience high role ambiguity and high job strain when using agile methods. As such, the lack o formal developer role descriptions in agile methods forces developers to understand the specifics of their roles pri marily based on informal interpersonal communication (Hummel et al., 2013). For developers who lack organizationa skills, it is, however, harder to discern the meaning behind others' suggestions and comments during such informa encounters. They may thus face particularly strong challenges in clearly understanding all facets of their roles and the expectations that others have. Failure to communicate effectively with team members may moreover be particu larly stressful for developers who are frequently forced to engage in intense collaborative agile practices, like pair programming, with their colleagues. They may more frequently fail to comprehend the meaning of team members problem analyses and proposed solutions, leaving them with unclear expectations about the task at hand, the role of others, and their own role. Thus, we hypothesize:

H4: Organizational skills will moderate the negative relationship between the extent of agile method use and role ambigu ity, such that the relationship will be stronger at higher levels of organizational skills

## 3.3 | Work exhaustion through role ambiguity and role conflict

In line with prior research, we expect both role ambiguity and role conflict to increase work exhaustion of devel opers. Prior work has consistently suggested that role conflict and role ambiguity are linked to negative outcome such as job dissatisfaction, anxiety, exhaustion, reduced job engagement, and turnover intentions (Joseph et al. 2007; Tubre & Collins, 2000). Conflicting and ambiguous role perceptions are problematic because they obfuscat the clear and single flow of authority within organizations that allows employees to experience less uncertainty increase accountability, and discern meaning about their positions regarding how they will be evaluated (Rizzo et al. 1970). Employees will face lower cognitive demands for decisions related to their responsibilities if expectations are clear and congruent (Feldman & Rafaeli, 2002). When multiple expectations from different sources are introduced employees need to cognitively and emotionally cope with more demands that cannot necessarily be reconciled. Consequently, employees who face role conflict or role ambiguity spend more cognitive resources on weighing differen expectations, become more hesitant in decision making, and have to resort to trial-and-error in meeting expectations (Pettijohn, Pettijohn, Taylor, & Keillor, 2001; Wang et al., 2015).

In software development, incongruent expectations of developers' behaviour and unclear responsibilities both put high strain on software engineers and cause them psychological stress (Windeler et al., 2017), a well-know antecedent of work exhaustion (Häusser et al., 2010; Van der Doef & Maes, 1999). This is particularly prevalent for individuals who engage in boundary spanning and are continuously exposed to multiple sources of influence such a vendors, managers, and users (Baroudi, 1985; Speier & Venkatesh, 2002; Windeler et al., 2017). Collecting and evalu ating role-related information from these various sources creates an additional burden on developers (Joseph et al., 2007; Moore, 2000). Lastly, developers within the interdependent structures of a team need to work with and rely on the output of their team members in order to benefit from team work rather than working alone (Espinosa et al. 2007; Faraj & Sproull, 2000; Mangalaraj et al., 2014). In this context, role ambiguity and role conflict reduce individ uals' sense of control over their own work and the possibility to do justice to their responsibilities, resulting in anxi ety and stress (Wang et al., 2015; Windeler et al., 2017). Thus, we hypothesize:

H5: Role ambiguity will be positively associated with work exhaustion

H6: Role conflict will be positively associated with work exhaustion.

In sum, our research model suggests that agile method use facilitates the achievement of clear and unambiguous role perceptions and thereby reduces work exhaustion for developers, particularly if they possess the organizationa skills to effectively interact with others in their organization

## 4 | METHOD

## 4.1 | Study setting and participants

To test our model, we conducted a field study at a leading Indian business software vendor with software developers who were actively involved in projects using agile methods. The developers worked mostly in projects to custom develop and provide software solutions for clients. The software vendor used agile methods in their portfolio of development methodologies. Although there were no fixed rules about the application of agile software develop ment methods, the company encouraged its developers to make use of the agile development practices of XP. Development teams could draw from a broad set of software development methods, and developers would engage to different degrees in agile practices. The developers in our sample therefore all had a basic understanding of various agile methods. Once companies have progressed beyond the initial adoption of agile methods, such situa tions of process diversity with developers applying multiple different methods to varying degrees over time are quite common in the software industry (Ramasubbu et al., 2015).

We focused on XP as the agile method of our investigation given its use by the software vendor. XP consists of 12 specific practices, namely, the planning game, small releases, use of metaphor, simple design, coding standards collective ownership, sustainable pace, testing, refactoring, pair programming, continuous integration, and involve ment of an on-site customer (Beck, 2000). Together, these practices instantiate the core values of the agile mani festo. Prior research has examined their use in different settings (Ramesh et al., 2012; Ramesh et al., 2017; Sarker & Sarker, 2009; Sharp & Robinson, 2008), and to some degree, their outcomes (Balijepally et al., 2009; Mangalara et al., 2014; Maruping et al., 2009a, 2009b). We focus on XP to understand the effects of the application of agile methods on software developers' work exhaustion for several reasons: (a) XP consists of an established collection of agile best practices, adheres to the values outlined in the agile manifesto, and closely resembles agile principles (Beck, 2000); (b) XP is used widely in the software industry and one of the most popular agile methods (Dingsøyr et al., 2012); and (c) there is a substantive body of scholarly research on this particular method and its practice (Chan & Thong, 2009; Dingsøyr et al., 2012; Dybå & Dingsøyr, 2008; Fitzgerald, Hartnett, & Conboy, 2006; Hoda et al., 2017; Hong, Thong, Chasalow, & Dhillon, 2011; Maruping et al., 2009a).

Our sampling frame consisted of 3989 software developers working in development projects at our target soft ware vendor in 2016. We approached the developers via the company's management team who invited them to par ticipate in our two-stage survey. We discarded responses from developers who did not complete both surveys Moreover, we restricted our sample to projects that had no overlap in terms of developers in order to prevent con founding effects of multiple project/team membership. These exclusions resulted in a final sample of individual-leve data from 1894 developers who worked in 217 software development projects.

The average age in our sample was 29.4 years (SD = 4.75) and average tenure at the company was 2.98 years $( S D = 1 . 6 0 )$ , with 58% of the respondents being men. On average, developers had 3.1 years of experience in softwar development (SD = 1.8), and 1.9 years of experience in agile methods (SD = 1.5). To minimize potential nonresponse bias, we obtained demographic data of everyone in our sampling frame and compared them with our sample. Com paring respondents and nonrespondents, there were no significant differences in terms of gender $( \relax z = 1 . 1 7 ; P = . 2 4 )$ age $\left( z = - 1 . 0 8 ; P = . 2 8 \right)$ , tenure $( z = - 1 . 4 0 ; P = . 1 6 )$ , software development experience (z = −1.75; P = .08), or XP experience $\left( z = - 1 . 4 8 ; P = . 1 4 \right)$

## 4.2 | Measurement

We relied on established and validated scales to measure all constructs and modified them only where necessary to fit the specific research context. The measurement scales can be found in the Appendix A. Where not indicated oth erwise, constructs were measured with multiple items on a 7-point Likert scale ranging from 1 (strongly disagree) to 7 (strongly agree). To create variable scores, we averaged the responses to the respective items.

## 4.2.1 | Extent of agile method use

Consistent with prior research (Maruping et al., 2009a), we measured the extent of agile method use by capturing the frequency with which developers used the six key XP practices, namely, pair programming, continuous integra tion, refactoring, unit testing, collective ownership, and coding standards. These practices are identified as instru mental in enabling software development teams to respond to requirement changes (Maruping et al., 2009a) an thus expected to influence developers' understanding of their constantly evolving roles in the development process In total, the measure consisted of 18 items (three for each XP practice) that we averaged to create a score for th extent of agile method use. The reliability of this measure was α = .79. Although it could be reasonably argued that these practices should each be modelled as separate constructs, given our conceptualization and the fact that in ou dataset, the correlations ranged from .74 to .86 across these six practices, we modelled them as a single construct— an approach that is consistent with Windeler et al. (2017) when first-order specifications are highly correlated

## 4.2.2 | Role conflict and role ambiguity

We measured role conflict and role ambiguity using the established scales of Rutner, Hardgrave, and McKnight (2008). Although recent research has proposed refined scales for role conflict and role ambiguity (Bowling et al., 2017), we used the scale of Rutner et al. (2008) for the following reasons. First, the scales by Bowling et al. (2017 are relatively new and were not available during our instrument design phase. Second, the scales of Rutner et al (2008) are well established and have been used to measure role conflict and ambiguity in the context of softwar development (Windeler et al., 2017). Using these scales allows for easier comparisons to prior work. The reliability of these scales was $\alpha _ { c o n f l i c t } = . 7 5 \ : \mathrm { a n d } \ : \alpha _ { a m b i g u i t y } = . 7 7$

## 4.2.3 | Organizational skills

The measure for organizational skills was adapted from Wade and Parent (2001), based on the definition of Nelson (1991), and encompasses an individual's skills in interpersonal communication, interpersonal behaviour, and project group dynamics. The reliability of this scale was α = .70.

## 4.2.4 | Work exhaustion

We measured developers' work exhaustion using the scale of Rutner et al. (2008). This scale focuses on emotiona exhaustion as an integral element and measureable symptom of job burnout and as an established predictor of turn over intentions (Joseph et al., 2007; Moore, 2000). The reliability of this scale was α = .75

## 4.2.5 | Control variables

In order to isolate the effects of agile method use as well as role conflict and role ambiguity, we controlled for individual-level and project-level characteristics. We controlled for age, gender, and team tenure as developers may become accustomed to formal and informal tasks and responsibilities over time, become more aware of their role, and gain legitimate authority in the eyes of colleagues, thereby making them less strained by managing unclear socia relationships (Faraj & Sproull, 2000; Lewis, Belliveau, Herndon, & Keller, 2007). We controlled for experience in software development (in general and in using XP in particular) as employees face challenges of uncertainty and increased effort requirements when first adopting new development methodologies and need time to understand the specific roles and responsibilities they entail (Cram & Newell, 2016). We thereby ensured that any significant effects of agile method use were not caused by a lack of job experience or experience with agile methods. As prior research suggested that they may influence coping behaviours and exhaustion of employees, we further controlled for perceived autonomy and perceived fairness of rewards (Furuyama et al., 1997; Moore, 2000; Rutner et al., 2008) Moreover, workload is known as an important factor associated with work exhaustion (Moore, 2000; Ply et al., 2012), and Tuomivaara et al. (2017) proposed that agile method use reduces developers' work exhaustion primarily through reduced workload. We therefore controlled for perceived workload to examine whether the effects of role perceptions are relevant for software developers' work exhaustion beyond the effects of workload. At a project level, we controlled for team size and requirements uncertainty because they can make it harder to establish clear and unambiguous role perceptions (Windeler et al., 2017). In addition, we controlled for the presence of a client repre sentative in the project team because it can be an important aid for agile teams relying on XP (Beck, 2000) and ma influence how easily developers can access customer feedback to refine their role perceptions and how well devel opment teams can engage in self-organization (Hoda, Noble, & Marshall, 2011).

## 4.3 | Procedure and analysis

The software vendor used agile methods in 325 projects in 2016, and these were our target for data collection. Afte exclusions, as described earlier (eg, overlapping team members), we collected data in two waves during the projects—ie, at the beginning and at the end of the project. The projects lasted between 80 and 140 days, consistent with the general philosophy underlying agile projects. In the first wave, we measured job skills, capabilities, and prior training, ie, organizational skills, experience in software development, and experience in XP. In the second wave, we measured individuals' work exhaustion, extent of agile method use, and job-related perceptions, including rol ambiguity, role conflict, perceived workload, autonomy, and fairness of rewards. After the projects, we obtained th scores for team size, requirements uncertainty, and the presence of a client representative from archival data.

Table 1 shows the descriptive statistics, reliabilities, and correlations. Convergent and discriminant validity were assessed using factor analysis with oblimin rotation allowing for correlated factors. All items loaded significantly on their specified constructs, with factor loadings greater than .70 and cross-loadings below .35. Cronbach alph exceeded .70 for all constructs. A power analysis suggested that our sample size of 1894 developers was larg enough to detect even small effects with the conventionally assumed power of .80 (Cohen, 1988).

We used random coefficient modelling (RCM) to test our model. Specifically, we employed the R studio multilevel package for data analysis. We chose RCM for its capability to adequately account for the nested nature of our data. In our sample, 1894 developers were nested in 217 projects. This leads to nonindependence of observations and calls for testing a $" 1 - 1 - 1 "$ two-level model that corrects relationships between variables at a lower (ie, individual level for error induced by commonalities of observations at a higher (ie, project) level (Bauer, Preacher, & Gil, 2006) RCM tools remedy many of the threats of type I and type II errors due to nested data by explicitly modelling nonindependence (Bliese & Hanges, 2004). RCM has been widely used and accepted in IS for analysing multilevel effect on team and individual levels (eg, Maruping & Magni, 2015, Venkatesh et al., 2018, Windeler et al., 2017). To report the explained variance that is proportionally reduced for level 1 and level 2 errors, we provide Snijders and Bosker (1999)'s overall pseudo $R ^ { 2 } \left( \sim R ^ { 2 } \right)$ . To establish that it is reasonable to use a multilevel RCM approach, we first ran a two-level null model with no predictors included. Results of a $\chi ^ { 2 }$ test indicate sufficient variability at both levels of analysis. In the null model, 62% of variance in developers' work exhaustion was attributable to individual-level differ ences, whereas 38% $\langle \chi ^ { 2 } = 1 1 1 2 . 6 6 , P < . 0 0 1 \rangle$ of variance was attributable to differences between projects. Thi reinforced the need to control for project-level effects

Following Venkatesh et al. (2018), we conducted multiple tests to exclude common method bias. We ran Harman one factor test (Podsakoff, MacKenzie, Lee, & Podsakoff, 2003) with an unrotated factor analysis. The first factor extracted only about 10% of the variance, thus reducing the concern of common method bias in this study. In addition, we conducted a marker variable test (Lindell & Whitney, 2001). The resulting attenuation was below 0.04 in the correlations between the variables, and the significance levels remained stable. This test further reduces th concern for common method bias.

## 5 | RESULTS

The results of testing the two-level model for H1 to H4 are shown in Table 2A. Models 1a and 1b represent the baseline models, models 2a and 2b represent the main effects only models, and models 3a and 3b represent the moderated models. All models account for the nested nature of our data. In H1 and H2, we predicted that a larger extent of agile method use would be negatively associated with developers' perceptions of role ambiguity and rol conflict. The results show that a larger extent of agile method use is negatively associated with both role ambiguity $( \gamma = - 0 . 1 6 , P < . 0 1 )$ ) and role conflict $( \gamma = - 0 . 1 8 , P < . 0 1 )$ , thus supporting H1 and H2. Moreover, the results show that there are significant interaction effects of agile method use and organizational skills on role ambiguity $( \gamma = - 0 . 2 0 ,$ $P < . 0 1 )$ and role conflict $( \gamma = - 0 . 2 8 , P < . 0 0 1 )$ . To understand the nature of the interactions, we plotted the signifi cant interactions, per Aiken and West (1991). Figure 2A,B illustrates the simple slopes of agile method use on rol ambiguity and role conflict, respectively, at high and low values of organizational skills (ie, 1 SD above and below th mean). As shown in Figure 2A,B, a larger extent of agile method use is more negatively related to role ambiguity an role conflict when developers have high organizational skills than when they have low organizational skills. This sug gests that organizational skills amplify the relationship between agile method use and clearer and less ambiguous role perceptions. Taken together, these results provide support for our H3 and H4 on the moderating relationship of organizational skills. All models, for main effects (models 2a and 2b) and for interaction effects (models 3a and 3b)

TABLE 1 Descriptive statistics and correlations

<table><tr><td colspan="2">Variables</td><td>Avg</td><td>SD</td><td>CA</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>1.</td><td>Age</td><td>29.4</td><td>4.75</td><td>NA</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2.</td><td>Gender</td><td>0.42</td><td>.50</td><td>NA</td><td>.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3.</td><td>Tenure</td><td>2.98</td><td>1.60</td><td>NA</td><td>.21**</td><td>.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4.</td><td>Experience in software development</td><td>3.1</td><td>1.80</td><td>NA</td><td>.19**</td><td>.19**</td><td>.17**</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5.</td><td>Experience in XP</td><td>1.9</td><td>1.51</td><td>NA</td><td>.15*</td><td>.14*</td><td>.16**</td><td>.22***</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6.</td><td>Perceived workload</td><td>5.46</td><td>1.90</td><td>.84</td><td>.16**</td><td>.05</td><td>.08</td><td>.09</td><td>.13*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7.</td><td>Autonomy</td><td>5.07</td><td>1.51</td><td>.79</td><td>.21***</td><td>.14*</td><td>.10</td><td>.16**</td><td>.14*</td><td>.07</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8.</td><td>Fairness of rewards</td><td>4.81</td><td>1.81</td><td>.76</td><td>.24***</td><td>.19**</td><td>.08</td><td>.19**</td><td>.16**</td><td>.13*</td><td>.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9.</td><td>Team size</td><td>8.73</td><td>1.93</td><td>NA</td><td>.04</td><td>.07</td><td>.09</td><td>.05</td><td>.12*</td><td>.14*</td><td>-.12*</td><td>.04</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10.</td><td>Client representative</td><td>0.55</td><td>0.50</td><td>NA</td><td>.07</td><td>.05</td><td>.05</td><td>.08</td><td>.09</td><td>.13*</td><td>-.13*</td><td>.08</td><td>.15*</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11.</td><td>Requirements uncertainty</td><td>24.87</td><td>11.39</td><td>NA</td><td>.10</td><td>.08</td><td>.06</td><td>.04</td><td>.05</td><td>.10</td><td>.08</td><td>.06</td><td>.17**</td><td>.18**</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12.</td><td>Extent of agile method use</td><td>4.66</td><td>1.53</td><td>.79</td><td>.17**</td><td>.17**</td><td>.13*</td><td>.21***</td><td>.24***</td><td>.17**</td><td>.08</td><td>.17**</td><td>.13*</td><td>.15**</td><td>.16**</td><td></td><td></td><td></td><td></td></tr><tr><td>13.</td><td>Organizational skills</td><td>4.88</td><td>2.17</td><td>.70</td><td>.27***</td><td>.23***</td><td>.17**</td><td>.23***</td><td>.08</td><td>.19**</td><td>.13*</td><td>.16*</td><td>.07</td><td>.10</td><td>.14*</td><td>.20**</td><td></td><td></td><td></td></tr><tr><td>14.</td><td>Role ambiguity</td><td>4.98</td><td>1.64</td><td>.77</td><td>.17**</td><td>.08</td><td>.10</td><td>-.23***</td><td>.13*</td><td>.14*</td><td>.19**</td><td>.20**</td><td>.13*</td><td>-.17**</td><td>.17**</td><td>-.37***</td><td>-.20**</td><td></td><td></td></tr><tr><td>15.</td><td>Role conflict</td><td>4.60</td><td>1.31</td><td>.75</td><td>.19**</td><td>.10</td><td>.12*</td><td>-.19**</td><td>.06</td><td>.10</td><td>.13*</td><td>.14*</td><td>.21***</td><td>-.19**</td><td>.17**</td><td>-.39***</td><td>-.19**</td><td>.21***</td><td></td></tr><tr><td>16.</td><td>Work exhaustion</td><td>5.17</td><td>1.21</td><td>.75</td><td>.21***</td><td>.09</td><td>.10</td><td>-.24***</td><td>.10</td><td>.04</td><td>.11*</td><td>.17**</td><td>.17**</td><td>-.22***</td><td>.26***</td><td>-.28***</td><td>-.27***</td><td>-.39***</td><td>.41***</td></tr></table>

T A B L E 2 A Results of RCM analysis predicting role ambiguity and role conflict

<table><tr><td rowspan="2">Variables</td><td colspan="3">Role Ambiguity</td><td colspan="3">Role Conflict</td></tr><tr><td>Model 1a</td><td>Model 2a</td><td>Model 3a</td><td>Model 1b</td><td>Model 2b</td><td>Model 3b</td></tr><tr><td colspan="7">L1 control variables</td></tr><tr><td>Age</td><td>.13* (.007)</td><td>.12* (.010)</td><td>.06 (.017)</td><td>.16** (.016)</td><td>.12* (.019)</td><td>.07 (.022)</td></tr><tr><td>Gender</td><td>.04 (.012)</td><td>.03 (.022)</td><td>.02 (.025)</td><td>.04 (.024)</td><td>.03 (.027)</td><td>.01 (.029)</td></tr><tr><td>Tenure</td><td>.05 (.023)</td><td>.03 (.027)</td><td>.02 (.029)</td><td>.08 (.023)</td><td>.07 (.026)</td><td>.05 (.035)</td></tr><tr><td>Experience in software development</td><td>-.14* (.009)</td><td>-.10 (.012)</td><td>-.05 (.019)</td><td>-.16** (.015)</td><td>-.13* (.019)</td><td>-.11* (.018)</td></tr><tr><td>Experience in XP</td><td>.08 (.031)</td><td>.04 (.031)</td><td>.03 (.037)</td><td>.05 (.024)</td><td>.05 (.026)</td><td>.04 (.028)</td></tr><tr><td colspan="7">L2 control variables</td></tr><tr><td>Team size</td><td>.08 (.040)</td><td>.05 (.044)</td><td>.04 (.047)</td><td>.16** (.013)</td><td>.13* (.017)</td><td>.11* (.019)</td></tr><tr><td>Client representative</td><td>-.12* (.011)</td><td>-.10 (.022)</td><td>-.08 (.029)</td><td>-.13* (.012)</td><td>-.11* (.015)</td><td>-.08 (.025)</td></tr><tr><td>Requirements uncertainty</td><td>.13* (.010)</td><td>.11* (.012)</td><td>.09 (.025)</td><td>.11* (.013)</td><td>.08 (.022)</td><td>.05 (.026)</td></tr><tr><td colspan="7">Main effects</td></tr><tr><td>Extent of agile method use</td><td></td><td>-.23*** (.008)</td><td>-.16** (.013)</td><td></td><td>-.22*** (.012)</td><td>-.18** (.013)</td></tr><tr><td>Organizational skills</td><td></td><td>-.13* (.010)</td><td>-.12* (.011)</td><td></td><td>-.11* (.010)</td><td>-.09 (.027)</td></tr><tr><td colspan="7">Interaction effect</td></tr><tr><td>Extent of agile method use × organizational skills</td><td></td><td></td><td>-.20** (.009)</td><td></td><td></td><td>-.28*** (.010)</td></tr><tr><td>Deviance</td><td>1512.40</td><td>951.48</td><td>804.13</td><td>1398.29</td><td>933.56</td><td>727.19</td></tr><tr><td> $\chi^2$ </td><td>416.22***</td><td>329.17***</td><td>254.28***</td><td>401.12***</td><td>301.19***</td><td>210.46***</td></tr><tr><td> $R^2$ </td><td>.08</td><td>.17</td><td>.25</td><td>.11</td><td>.19</td><td>.30</td></tr><tr><td> $\Delta R^2$ </td><td></td><td>.09</td><td>.08</td><td></td><td>.08</td><td>.11</td></tr></table>

Note. Results for two-level model: variables team size, client representative, and requirements uncertainty on leve 2 (project, n = 217), all other variables on level 1 (individual developer, n = 1894). Standard errors are shown in parentheses. Abbreviations: RCM, random coefficient modelling; XP, extreme programming. \*P < .05; \*\*P < .01; \*\*\*P < .001.

show significant improvements in deviance and explained variance that lends further support for H1 to H4. In total, the moderated models explain 25% and 30% of variance in role ambiguity and role conflict, respectively.

Table 2B shows the results of the RCM analysis predicting work exhaustion based on role conflict and role ambiguity. As predicted by H5 and H6, both role ambiguit $( \gamma = 0 . 1 9 , P < . 0 0 1 )$ and role conflict $( \gamma = 0 . 2 1 , P < . 0 0 1 )$ have significant positive effects on work exhaustion beyond the effects of the control variables $( \Delta R ^ { 2 } \ = \ . 0 8 ,$ $P < . 0 1 )$ . Two individual-level control variables—age and workload—and two project-level control variables— requirements uncertainty and the presence of a client representative—have significant effects on work exhaustion, but their path coefficients are lower for the model including role ambiguity and role conflict (model 2). This lends support to the reasoning that the effects of agile method use through role perceptions have a significant impact on developers' work exhaustion beyond project-level effects and beyond workload effects that have been suggested by prior work (Tuomivaara et al., 2017). Overall, the model explains 32% of the variance in work exhaustion.

We next examined the direct and indirect effects of the extent of agile method use on work exhaustion in mor detail. To do so, we conducted a moderated mediation analysis following Edwards and Lambert (2007) in which boo tstrapping was used to create bias-corrected confidence intervals and simple effects. Table 3 shows the results of this analysis. It outlines the simple effects of agile method use on developers' work exhaustion as mediated by role conflict and role ambiguity and moderated by organizational skills. The results indicate that a larger extent of agil method use has significant negative indirect, direct, and total effects on developers' work exhaustion that are all sig nificantly stronger for higher levels of organizational skills. The results thus provide strong support for the hypothe sized moderating effect of organizational skills. The indirect and direct effects of agile method use on wor exhaustion are negative and significant when mediated by role ambiguity and role conflict. This suggests that th mediated effects of agile method use and its interaction with organizational skills through role perceptions entail sig nificant consequences for individual developers' work exhaustion. More specifically, the results show that role ambi guity and role conflict partially mediate the effects of agile method use on software developers' work exhaustion conditional on organizational skills. Although this partial mediation lends support to our reasoning in H1 through H6 it also suggests that role perceptions are not the only mechanism through which agile method use influences work exhaustion in software developers.

![](/api/attachments/E2TQE2DC/fulltext/images/39cef70fe3e2c0d16f9a3c3b69a38b0db6374298fad9afbdbaac695c6ff653dd.jpg)

![](/api/attachments/E2TQE2DC/fulltext/images/264586feac0c3fc96e71745fc7519f8bb9577f3ca749a8b048dc9c196f9b2633.jpg)  
F I G U R E 2 A, Interaction effect of agile method use and organizational skills on role ambiguity; B, Interaction effect of agile method use and organizational skills on role conflict

We further took procedural precautions to demonstrate the robustness of our results. Specifically, endogeneity could constitute a problem for our results if the extent of agile method use or organizational skills were endogenous to role perceptions that would result in omitted variable bias or selection bias (Wooldridge, 2012). Thus, we took several steps to rule out potential threats of endogeneity. First, as part of our research design, the multi-wave data collection reduced endogeneity concerns because effects that occurred and were measured later in the projects (eg, role perceptions and work exhaustion) could unlikely influence what occurred and was measured earlier in the projects (eg, organizational skills). Second, consistent with prior work (eg, Hsieh, Rai, & Xu 2011, Mani, Barua, & Whinston, 2012, Venkatesh, Shaw, Sykes, Wamba, & Macharia, 2017), we conducted a two stage Heckman procedure to address endogeneity concerns regarding the extent of agile method use. Originally intended to correct estimates for selection bias, this approach is often used to rule out broader endogeneity threats (Venkatesh et al., 2017). Appendix B reports the results of this procedure. The results do not hint toward any endogeneity threats and indicate that selection bias does not constitute a threat to our analyses (see Appendix B). Third, we followed the approach suggested by Frank (2000) to assess the danger of possible omitted variable bias. We calculated the impact threshold for a confounding variable (ITCV) at which an omitted variabl would render the effect of an independent variable (eg, extent of agile method use) on a dependent variable (eg, role ambiguity or role conflict) nonsignificant. The ITCV determines the minimum correlations of a potentia omitted variable with both the independent variable and the dependent variable that are necessary to render the effect of the independent variable on the dependent variable nonsignificant after controlling for all covariates. W calculated ITCV scores for the hypothesized relationships H1 to H4. Of all these relationships, the relationship of the extent of agile method use with role ambiguity showed to be the least robust against omitted variable bias Still, a potential omitted variable would have to be correlated with both the extent of agile method use and rol ambiguity at more than 0.488 after controlling for covariates to invalidate our inferences. Given that this is much higher than the correlations observed in our sample (see Table 1), we deem it unlikely that an omitted variabl could fulfil these conditions. As all other effects were even more robust, there are no indications that omitted vari able bias would constitute an issue for our results. In sum, these precautions heavily reduce endogeneity concerns regarding H1 to H4.

T A B L E 2 B Results of RCM analysis predicting work exhaustion

<table><tr><td rowspan="2">Variables</td><td colspan="2">Work Exhaustion</td></tr><tr><td>Model 1</td><td>Model 2</td></tr><tr><td>L1 control variables</td><td></td><td></td></tr><tr><td>Age</td><td>.13* (.009)</td><td>.12* (.011)</td></tr><tr><td>Gender</td><td>.07 (.024)</td><td>.06 (.027)</td></tr><tr><td>Tenure</td><td>.05 (.026)</td><td>.04 (.029)</td></tr><tr><td>Experience in software development</td><td>-.15* (.011)</td><td>.08 (.033)</td></tr><tr><td>Experience in XP</td><td>-.13* (.011)</td><td>.09 (.020)</td></tr><tr><td>Perceived workload</td><td>.13* (.012)</td><td>.11* (.014)</td></tr><tr><td>Autonomy</td><td>.14** (.006)</td><td>.10 (.020)</td></tr><tr><td>Fairness of rewards</td><td>.06 (.027)</td><td>.05 (.031)</td></tr><tr><td>L2 control variables</td><td></td><td></td></tr><tr><td>Team size</td><td>.14* (.010)</td><td>.13* (.011)</td></tr><tr><td>Client representative</td><td>-.17** (.012)</td><td>-.14* (.014)</td></tr><tr><td>Requirements uncertainty</td><td>.19** (.011)</td><td>.17** (.014)</td></tr><tr><td>Main effects</td><td></td><td></td></tr><tr><td>Role ambiguity</td><td></td><td>.19*** (.010)</td></tr><tr><td>Role conflict</td><td></td><td>.21*** (.011)</td></tr><tr><td>Deviance</td><td>2155.12</td><td>1941.60</td></tr><tr><td> $\chi^2$ </td><td>371.68***</td><td>260.43***</td></tr><tr><td> $R^2$ </td><td>.24</td><td>.32</td></tr><tr><td> $\Delta R^2$ </td><td></td><td>.08</td></tr></table>

Note. Results for two-level model: Variables team size, client representative, and requirements uncertainty on level 2 (project, n = 217), all other variables on level 1 (individual developer, n = 1894). Standard errors are shown in parentheses.  
Abbreviations: RCM, random coefficient modelling; XP, extreme programming.  
\*P < .05; \*\*P < .01; \*\*\*P < .001.

T A B L E 3 Simple effects analysis of agile method use on work exhaustion

<table><tr><td rowspan="2">Moderator variable</td><td colspan="3">Mediation through Role Ambiguity</td><td colspan="3">Mediation through Role Conflict</td></tr><tr><td>Direct</td><td>Indirect</td><td>Total</td><td>Direct</td><td>Indirect</td><td>Total</td></tr><tr><td colspan="7">Organizational skills</td></tr><tr><td>Low (mean – 1 SD)</td><td>-.06*</td><td>-.07**</td><td>-.13***</td><td>-.07**</td><td>-.05**</td><td>-.12**</td></tr><tr><td>High (mean + 1 SD)</td><td>-.19***</td><td>-.11**</td><td>-.30***</td><td>-.16**</td><td>-.11**</td><td>-.27***</td></tr><tr><td>Difference</td><td>.13**</td><td>.04*</td><td>.17***</td><td>.09**</td><td>.06**</td><td>.15**</td></tr></table>

Note. Results for direct, indirect, and total effects following Edwards and Lambert (2007). Bootstrap estimates based on 1000 resamples  
\*P < .05; \*\*P < .01; \*\*\*P < .001

T A B L E 4 Key contributions

<table><tr><td>Research Stream</td><td>This Study&#x27;s Key Contribution to the Research Stream</td></tr><tr><td>Effects of agile development methods on work exhaustion</td><td>Beyond its established effects on workload, the use of agile development methods is associated with lower work exhaustion in developers through clearer and more congruent role perceptions.</td></tr><tr><td>Skills in software development</td><td>Organizational skills are an important lever for developers to effectively cope with agile methods. The established assumption that developers primarily need technical skills and experience, rather than organizational skills, does not hold anymore in agile development environments.</td></tr><tr><td>Effectiveness of software development methods</td><td>Prior work suggested that agile methods improve development outcomes primarily through better project-level control. We show that agile methods additionally allow developers to increase control at the individual level. This calls for further multilevel investigations.</td></tr></table>

## 6 | DISCUSSION

We set out to explain the effects of agile development methods on software developers' work exhaustion. This was accomplished by developing and testing a model suggesting that agile method use facilitates the achievement of clear and unambiguous role perceptions and thereby reduces work exhaustion for developers, particularly if the possess the organizational skills to effectively interact with others in their organization. We found strong support for our model in a field study on 1894 software developers in 217 project teams that used agile methods. Our finding have several theoretical and practical implications. Table 4 outlines the key contributions of our study

## 6.1 | Theoretical contributions

First, we elaborate on the effects of using agile development methods on work exhaustion in software developers and show that the use of agile methods reduces work exhaustion by lowering both role ambiguity and role conflict in software developers. This finding is important because work exhaustion in software developers leads to programming errors and subsequently high maintenance costs, reduces team performance, and increases employee turnover (Furuyama et al., 1997; Venkatesh et al., 2018; Windeler et al., 2017). A better understanding of how the use of pop ular agile methods influences software developers' work exhaustion consequently helps to better understand success and failure in contemporary software development projects. Prior work in this area has primarily taken a project management perspective and found that agile methods reduce work exhaustion by distributing the workload in soft ware development projects more evenly over time (Tuomivaara et al., 2017; Vidgen & Wang, 2009). Our researc theorized and empirically found support for a different effect of agile methods on developers: Beyond the effects on their workload, agile methods let developers come to clearer and more congruent role perceptions that in turn lower developers' work exhaustion. Our work thus provides a new, behavioural explanation of individual-level effects of agile method use on developers' work exhaustion. Whereas workload effects hinge primarily on the project-wide use of agile methods for project management (Tuomivaara et al., 2017; Vidgen & Wang, 2009), the frequency and inten sity in which developers engage individually in agile practices vary within projects and thus influences developers at an individual level rather than at a project level. Future research on the effectiveness of software development methods needs to take into account that methods such as XP may not only change project management activities but also have distinctive effects on individual developers' role perceptions and work exhaustion. Although a moderated mediation analysis lent strong support to our research model and the indirect effects of agile method use on work exhaustion through role perceptions, it also showed significant direct effects of agile method use on work exhaustion that were not mediated by role perceptions. Future research should investigate the mechanisms that underlie these unexplained direct effects to further extend the emerging stream of research on the effects of agil methods on individual software developers (Balijepally et al., 2009; Tripp et al., 2016; Tuomivaara et al., 2017)

Second, our work shows that software developers' organizational skills facilitate the benefits of agile methods in terms of improved role perceptions and reduced work exhaustion. Based on the JDCM, we found empirical support for our theorizing that the use of agile methods places specific demands on software developers that they can best address if they possess organizational skills to effectively manage interpersonal communication and group dynamics This finding is important because prior work on the effects of agile methods has not fully accounted for individual level differences between software developers. Specifically, prior work could not explain why some software devel opers become less exhausted from using agile methods than others who perceive the exact opposite (Balbes, 2017 Laanti, 2013). Tapping into this gap, our work suggests that organizational skills facilitate software developers' inter actions with team members and external stakeholders that become necessary when following agile methods. Organi zational skills thereby allow developers to reap the benefits of agile methods. In line with this reasoning, a moderated mediation analysis showed that the use of agile methods without appropriate organizational skills resulted in significantly higher levels of role ambiguity, role conflict, and work exhaustion in software developers. The more general literature on the effects of software development methodologies learns from our research that dis tinct developer skills can decide about the favourable or unfavourable effects of software development methodolo gies. Prior work in this direction stressed the importance of experience with software development in general and with specific development methodologies in particular for coping with software development work (Ang, Thong, & Yap, 1997; McManus, 2003; Sultan & Chan, 2000). We add to this stream of research by pinpointing the importanc of specific skills, rather than experience, for coping with job demands and preventing work exhaustion during soft ware development.

Third, our findings contribute to research on the importance of technical and organizational skills in softwar development (eg, Ang et al., 1997, Wade & Parent, 2001). Prior work often argued that software developers primar ily need technical skills and that deficiencies in organizational skills should not be as dramatic for them as for othe occupational groups (Gallagher et al., 2010; Nelson, 1991; Wade & Parent, 2001). Our findings show that this assumption is questionable with regard to contemporary software development. Given the widespread use of agil methods, developers may increasingly need organizational skills to effectively apply these methods. In fact, agil software development today appears to follow predictions by Lee et al. (1995) who envisioned organizational skill to become continuously more important.

Lastly, prior research has shown that agile methods are particularly beneficial for outcomes in projects with high complexity and requirements volatility (Maruping et al., 2009a). Extant theory holds that this advantage results from improved project-level control structures (Maruping et al., 2009a; Venkatesh et al., 2018). Our findings add to this view by suggesting that agile methods not only improve the project-level control but also allow developers to increase control at the individual level as they gain less conflicting and less ambiguous role perceptions. Examining possible interactions between these project-level and individual-level effects of agile methods may therefore be a fruitful avenue for future research. In fact, recent work suggests that especially multi-level views on developer role perceptions can strongly improve our understanding of project performance (Windeler et al., 2017)

## 6.2 | Practical implications

IT organizations have previously been found to hire applicants primarily based on their technical skills, largely ignoring their organizational skills (Wade & Parent, 2001). Our findings call this practice into question, at least for software developers working with agile methods. Our results suggest that software companies that are interested in preventing work exhaustion and burnout of their developers should provide training in organizational skills and agil methods, or they need to make sure that their software developers already have these skills when they are hired

Role conflict and role ambiguity are especially prevalent in software projects with high technical risk and requirements volatility (Windeler et al., 2017). Our results show that agile methods can be used to reduce role con flict and role ambiguity. From an individual-level perspective, agile methods may therefore fit particularly well with high risk projects and volatile requirements. Given that technical risk factors and volatile requirements continu to be two of the most common and influential obstacles to successful software development work (Hoda & Murugesan, 2016; Maruping, Venkatesh, Thong, & Zhang, 2019; Venkatesh et al., 2018), our findings have a sub stantial impact for the software industry and can help reduce the notoriously high failure rates of software develop ment projects.

Lastly, software vendors can learn in which way the use of agile development methods relates to one of thei core resources, namely, software developers. The increased application of agile methods is associated with reduced software developers' work exhaustion. To preserve the long-term performance and employability of their devel opers, even conservative organizations may consequently want to utilize agile methods, at least to a certain degre in some of their projects.

## 6.3 | Limitations and future research

Our work focused on software developers' work exhaustion through role conflict and role ambiguity. This focus was reasonable because contemporary theory in organizational psychology has established role conflict and role ambiguit as crucial determinants of work exhaustion (Häusser et al., 2010; Karasek et al., 1998; Van der Doef & Maes, 1999) that are particularly relevant in the context of empowered teams (Windeler et al., 2017). Future research may want to replicate our study using the refined conceptualizations and measurements of role conflict and role ambiguity that were proposed in recent research (Bowling et al., 2017). Although we controlled for a number of potentially confounding var iables, there are also other sources of job strain possibly related to agile methods that this study did not account for. For example, time pressure, project complexity, and the temporal distribution of workload affect how developers fee and how they interact with their team members (Maruping et al., 2015; Tuomivaara et al., 2017; Venkatesh et al., 2018; Venkatesh, Maruping, & Brown, 2006). Likewise, process maturity and how well a software development method is implemented in a project might influence developers' role perceptions (Ramasubbu et al., 2015). Given that such factors would influence all members of a project team in the same way and that our RCM analysis controlled for project-level nonindependence of observations, our results are to some degree robust against the confounding effects of these factors. Moreover, our robustness checks for potential omitted variable bias did not raise any concerns. Nonetheless, we suggest that future research should examine these potential sources of job strain and their effects more explicitly. Another avenue for research is to evaluate individual level conditions, such as Internet addiction, that might influence work exhaustion in software developers, especially if they work in contexts with high autonomy such as agile teams (Venkatesh, Sykes, Chan, Thong, & Hu, 2019). Future research may also investigate psychological and performance-related outcomes that can have more complex relationships with job strain (Onyemah, 2008)

Our study examined the use of XP, a particularly popular agile method for which there is a body of scholarly research. Yet, there are other agile methods. Scrum, for example, is partly more concerned with project management than with actual collaborative development work that differentiates it from XP (Dingsøyr et al., 2012). The amount of collaborative development work may, however, influence how often developers can engage with team members, users, customers, and external stakeholders to seek mutual understanding and clarify their roles. Future research should therefore examine how other agile development methods influence role perceptions. For example, qualitative investigations into multiple other development methods may be used to extend and complement our quantitative results. In addition, our study was set in a context where XP had already been introduced as the company's choice of agile method. This meant that XP was one method in the company's overall portfolio of development methods. XP was therefore used selectively and to varying degrees of intensity. Such selective use of development methods is typical for most organizations in the software industry that have progressed beyond the initial adoption of agil methods (Ramasubbu et al., 2015) that makes our findings relevant for a variety of organizations. Yet, we did not study the introduction of agile methods or a comparison of projects that exclusively used either agile or plan-drive methods. Consequently, our findings do not speak to the question of whether the introduction of agile methods alle viates developers' work exhaustion or possibly even causes more role conflict and role ambiguity. Future research that examines such effects can draw on an extensive body of literature on the individual-level effects of introducing new technology in teams and organizations (Bala & Venkatesh, 2015; Dennis, Venkatesh, & Ramesh, 2008; Venkatesh & Windeler, 2012). Likewise, it is a limitation of our research that we did not examine patterns of simulta neous use of multiple development methods that can affect software quality and project performance (Bick et al., 2018; Ramasubbu et al., 2015). For example, if teams combine XP with elements of other methods, such as Scrum, the combined effects of the individual methods could create synergies or cancel each other out. These issues an how they relate to individual developer's work exhaustion are interesting directions for future research.

Our study paid special attention to developers' organizational skills because we expected and found that organi zational skills are important for developers who use agile methods. In doing so, we did not aim at drawing a full pic ture of all the relevant job skills of developers and did not collect data on many other skills that successfu developers may need (Gallagher et al., 2010; Nelson, 1991; Wade & Parent, 2001). This limitation of our work is an opportunity for future work that may draw a more comprehensive picture of the relevant job skills for developers. In light of our findings, this line of work should evaluate the relative importance of different skills in agile and plan driven development environments.

Finally, our empirical focus on a single organization allowed us to naturally control for inter-organizational differences. Such a focus on a single vendor firm to study IT projects is consistent with prior research (eg, Kudaravall et al., 2017, Rai, Maruping, & Venkatesh, 2009, Ramasubbu et al., 2015, Venkatesh et al., 2018, Windeler et al. 2017) as it helps to control for organizational-level effects. But it also calls for replicating our work in other organiza tions to increase generalizability. There is substantial evidence that organizational and national cultures influence th adoption and adaptation of software development methods (Persson, Mathiassen, & Aaen, 2012; Rai et al., 2009; Ramesh et al., 2017; Sarker & Sarker, 2009). Future research should therefore aim to understand the cultural aspect of how agile methods affect developer role perceptions and should try to outline how agile methods can be used to reduce developers' work exhaustion in globally distributed and culturally heterogeneous settings.

## 7 | CONCLUSION

We presented a research model with the goal to explain the effects of agile software development methods on indi vidual developers' work exhaustion. We theorized that agile method use helps software developers to achieve clear and unambiguous role perceptions that reduce work exhaustion if the developers have organizational skills to effec tively interact with customers and stakeholders within their organization. We found strong support for our model in a field study of 1894 software developers applying the popular agile development method XP in 217 project teams

Our findings have substantial implications for theory on the individual-level effects of agile development method and show that the effectiveness of development methodologies can hinge on specific skills of individual developers We encourage organizations to use agile software development methodologies but caution that developers need to have organizational skills to be able to reap the benefits of these methods

## ACKNOWLEDGEMENTS

This project was funded by a grant from the Research Grants Council of Hong Kong (GRF693313).

## ORCID

Viswanath Venkatesh https://orcid.org/0000-0001-8473-376X

James Y. L. Thong https://orcid.org/0000-0002-1640-0581

Frank K. Y. Chan https://orcid.org/0000-0001-9301-7634

Hartmut Hoehle https://orcid.org/0000-0001-8117-0105

Kai Spohrer https://orcid.org/0000-0001-8659-7554

## REFERENCES

Aiken, L. S., & West, S. G. (1991). Multiple regression: Testing and interpreting interaction. Newbury Park, CA: SAGE

Akter, S., Wamba, S. F., Gunasekaran, A., Dubey, R., & Childe, S. J. (2016). How to improve firm performance using big dat analytics capability and business strategy alignment? International Journal of Production Economics, 182, 113–131

Ang, K. T., Thong, J. Y. L., & Yap, C. S. (1997). IT implementation through the lens of organizational learning: A case study of INSUROR. Proceedings of the 18th International Conference on Information System (pp. 331–348). Georgia: Atlanta

Bala, H., & Venkatesh, V. (2015). Adaptation to information technology: A holistic nomological network from implementa tion to job outcomes. Management Science, 62, 156–179.

Balbes, M. (2017) The stress of agile. Application Development Trends. Retrieved from https://adtmag.com/articles/2017 01/24/stress-of-agile.aspx on March 15<sup>th</sup>, 2018.

Balijepally, V., Mahapatra, R., Nerur, S., & Price, K. H. (2009). Are two heads better than one for software development? The productivity paradox of pair programming. MIS Quarterly, 33, 91–118

Baroudi, J. J. (1985). The impact of role variables on IS personnel work attitudes and intentions. MIS Quarterly, 9, 341–356.

Bauer, D. J., Preacher, K. J., & Gil, K. M. (2006). Conceptualizing and testing random indirect effects and moderated media tion in multilevel models: New procedures and recommendations. Psychological Methods, 11, 142–163

Beck, K. (2000). Extreme programming explained: Embrace change (The XP Series). Boston: Addison-Wesley Professional.

Bick, S., Spohrer, K., Hoda, R., Scheerer, A., & Heinzl, A. (2018). Coordination challenges in large-scale software develop ment: A case study of planning misalignment in hybrid settings. IEEE Transactions on Software Engineering, 44, 932–950

Bliese, P. D., & Hanges, P. J. (2004). Being both too liberal and too conservative: The perils of treating grouped data as though they were independent. Organizational Research Methods, 7, 400–417

Bowling, N. A., Khazon, S., Alarcon, G. M., Blackmore, C. E., Bragg, C. B., Hoepf, M. R., … Li, H. (2017). Building better mea sures of role ambiguity and role conflict: The validation of new role stressor scales. Work & Stress, 31, 1–23.

Chan, F. K. Y., & Thong, J. Y. L. (2009). Acceptance of agile methodologies: A critical review and conceptual framework. Deci sion Support Systems, 46, 803–814

Chuang, S.-W., Luor, T., & Lu, H.-P. (2014). Assessment of institutions, scholars, and contributions on agile software devel opment (2001-2012). Journal of Systems and Software, 93, 84–101

Cohen, J. (1988). Statistical power analysis for the behavioral sciences. Hillsdale: Lawrence Erlbaum.

Conboy, K. (2009). Agility from first principles: Reconstructing the concept of agility in information systems development Information Systems Research, 20, 329–354.

Costello, K. & Omale, G. (2019) Gartner says global IT spending to grow 1.1 percent in 2019. Retrieved from https://www.gartner. com/en/newsroom/press-releases/2019-04-17-gartner-says-global-it-spending-to-grow-1-1-percent-i on April 30<sup>th</sup>, 2019

Cram, W. A., & Newell, S. (2016). Mindful revolution or mindless trend? Examining agile development as a management fashion. European Journal of Information Systems, 25, 154–169.

Davis, A. R., Niederman, F., Greiner, M. E., Wynn, D., Jr., & York, P. T. (2006). A research agenda for studying open source I: A multi-level framework. Communications of the Association for Information Systems, 18, 129–149

Deci, E., & Ryan, R. M. (1985). Intrinsic motivation and self-determination in human behavior. New York: Springer Science and Business Media.

Dennis, A. R., Venkatesh, V., & Ramesh, V. (2008). Adoption of collaboration technologies: Integrating technology acceptance and collaboration technology research. Sprouts: Working Papers on Information Systems, 3, Article 8.

Dingsøyr, T., Nerur, S., Balijepally, V., & Moe, N. B. (2012). A decade of agile methodologies: Towards explaining agile soft ware development. Journal of Systems & Software, 85, 1213–1221

Drury, M., Conboy, K., & Power, K. (2012). Obstacles to decision making in agile software development teams. Journal of Systems and Software, 85, 1239–1254.

Dybå, T., & Dingsøyr, T. (2008). Empirical studies of agile software development: A systematic review. Information and Software Technology, 50, 833–859.

Edwards, J. R., & Lambert, L. S. (2007). Methods for integrating moderation and mediation: A general analytical framework using moderated path analysis. Psychological Methods, 12, 1–22

Espinosa, J. A., Slaughter, S. A., Kraut, R. E., & Herbsleb, J. D. (2007). Team knowledge and coordination in geographically distributed software development. Journal of Management Information Systems, 24, 135–169

Faraj, S., & Sproull, L. (2000). Coordinating expertise in software development teams. Management Science, 46, 1554–1568

Feldman, M. S., & Rafaeli, A. (2002). Organizational routines as sources of connections and understandings. Journal of Man agement Studies, 39, 309–331.

Fitzgerald, B. (1998). An empirical investigation into the adoption of systems development methodologies. Information & Management, 34, 317–328

Fitzgerald, B., Hartnett, G., & Conboy, K. (2006). Customising agile methods to software practices at Intel Shannon European Journal of Information Systems, 15, 200–213

Fitzgerald, B., & Stol, K. J. (2017). Continuous software engineering: A roadmap and agenda. Journal of Systems and Software 123, 176–189.

Fosso Wamba, S., Gunasekaran, A., Akter, S., Ren, S. J.-f., Dubey, R., & Childe, S. J. (2017). Big data analytics and firm perfor mance: Effects of dynamic capabilities. Journal of Business Research, 70, 356–365.

Fowler, M., & Highsmith, J. (2001). The agile manifesto. Software Development, 9, 28–35.

Frank, K. A. (2000). Impact of a confounding variable on a regression coefficient. Sociological Methods & Research, 29, 147–194

Furuyama, T., Arai, Y., & Iio, K. (1994). Fault generation model and mental stress effect analysis. Journal of Systems and Soft ware, 26, 31–42.

Furuyama, T., Arai, Y., & Iio, K. (1997). Analysis of fault generation caused by stress during software development. Journal of Systems and Software, 38, 13–25

Gallagher, K. P., Kaiser, K. M., Simon, J. C., Beath, C. M., & Goles, T. (2010). The requisite variety of skills for IT professionals Communications of the ACM, 53, 144–148

Ghobadi, S., & Mathiassen, L. (2016). Perceived barriers to effective knowledge sharing in agile software teams. Information Systems Journal, 26, 95–125.

Ghobadi, S., & Mathiassen, L. (2017). A model for assessing and mitigating knowledge sharing risks in agile software devel opment. Information Systems Journal, 27, 699–731

Häusser, J. A., Mojzisch, A., Niesel, M., & Schulz-Hardt, S. (2010). Ten years on: A review of recent research on the job demand-control (-support) model and psychological well-being. Work & Stress, 24, 1–35.

Hoda, R., & Murugesan, L. K. (2016). Multi-level agile project management challenges: A self-organizing team perspective Journal of Systems and Software, 117, 245–257

Hoda, R., Noble, J., & Marshall, S. (2011). The impact of inadequate customer collaboration on self-organizing agile teams Information and Software Technology, 53, 521–534

Hoda, R., Salleh, N., Grundy, J., & Tee, H. M. (2017). Systematic literature reviews in agile software development: A tertiary study. Information and Software Technology, 85, 60–70.

Hong, W., Thong, J. Y. L., Chasalow, L. C., & Dhillon, G. (2011). User acceptance of agile information systems: A model and empirical test. Journal of Management Information Systems, 28, 235–272

Hsieh, J. J. P.-A., Rai, A., & Xu, S. X. (2011). Extracting business value from IT: A sensemaking perspective of post-adoptiv use. Management Science, 57, 2018–2039

Hummel, M., Rosenkranz, C., & Holten, R. (2013). The role of communication in agile systems development. Business & Infor mation Systems Engineering, 5, 343–355

Joseph, D., Ng, K.-Y., Koh, C., & Ang, S. (2007). Turnover of information technology professionals: A narrative review, meta analytic structural equation modeling, and model development. MIS Quarterly, 31, 547–577.

Jung, J. H., Schneider, C., & Valacich, J. (2010). Enhancing the motivational affordance of information systems: The effect of real–time performance feedback and goal setting in group collaboration environments. Management Science, 56, 724–742.

Karasek, R., Brisson, C., Kawakami, N., Houtman, I., Bongers, P., & Amick, B. (1998). The job content questionnaire (JCQ): An instrument for internationally comparative assessments of psychosocial job characteristics. Journal of Occupationa Health Psychology, 3, 322–355.

Karasek, R. A. (1979). Job demands, job decision latitude, and mental strain: Implications for job redesign. Administrative Sci ence Quarterly, 24, 285–308

Ke, W., & Zhang, P. (2010). The effects of extrinsic motivations and satisfaction in open source software development. Jour nal of the Association for Information Systems, 11, 784–808

Ke, W., & Zhang, P. (2011). Effects of empowerment on performance in open-source software projects. IEEE Transactions on Engineering Management, 58, 334–346.

Kudaravalli, S., Faraj, S., & Johnson, S. L. (2017). A configural approach to coordinating expertise in software development teams. MIS Quarterly, 41, 43–64.

Laanti, M. (2013) Agile and wellbeing—Stress, empowerment, and performance in scrum and kanban teams. Proceedings of th 46th Hawaii International Conference on System Sciences, Maui, USA, 4761–4770

Lee, D. M. S., Trauth, E. M., & Farwell, D. (1995). Critical skills and knowledge requirements of IS professionals: A joint aca demic/industry investigation. MIS Ouarterly. 19. 313-340

Lee, G., & Xia, W. (2010). Toward agile: An integrated analysis of quantitative and qualitative field data on software develop ment agility. MIS Quarterly, 34, 87–114.

Lewis, K., Belliveau, M., Herndon, B., & Keller, J. (2007). Group cognition, membership change, and performance: Investigatin the benefits and detriments of collective knowledge. Organizational Behavior and Human Decision Processes, 103, 159–178.

Lindell, M. K., & Whitney, D. J. (2001). Accounting for common method variance in cross-sectional research designs. Journa of Applied Psychology, 86, 114–121.

Mangalaraj, G., Nerur, S., Mahapatra, R., & Price, K. H. (2014). Distributed cognition in software design: An experimenta investigation of the role of design patterns and collaboration. MIS Quarterly, 38, 249–274.

Mani, D., Barua, A., & Whinston, A. B. (2012). An empirical analysis of the contractual and information structures of busines process outsourcing relationships. Information Systems Research, 23, 618–634.

Maruping, L. M., & Magni, M. (2015). Motivating employees to explore collaboration technology in team contexts. MIS Quar terly, 39, 1–16.

Maruping, L. M., Venkatesh, V., & Agarwal, R. (2009a). A control theory perspective on agile methodology use and changing user requirements. Information Systems Research, 20, 377–399.

Maruping, L. M., Venkatesh, V., Thatcher, J. B., & Patel, P. C. (2015). Folding under pressure or rising to the occasion? Per ceived time pressure and the moderating role of team temporal leadership. Academy of Management Journal, 58 1313–1333

Maruping, L. M., Venkatesh, V., Thong, J. Y. L., & Zhang, X. (2019). A risk mitigation framework for information technolog projects: A cultural contingency perspective. Journal of Management Information Systems, 36, 120–157.

Maruping, L. M., Zhang, X., & Venkatesh, V. (2009b). Role of collective ownership and coding standards in coordinatin expertise in software project teams. European Journal of Information Systems, 18, 355–371.

Matook, S., & Maruping, L. M. (2014). A competency model for customer representatives in agile software development pro jects. MIS Quarterly Executive, 13, 77–95.

McManus, J. (2003). Team agility. The Computer Bulletin, 45, 26–27.

Moe, N. B., Dingsøyr, T., & Dybå, T. (2010). A teamwork model for understanding an agile team: A case study of a Scrum project. Information and Software Technology, 52, 480–491.

Moore, J. E. (2000). One road to turnover: An examination of work exhaustion in technology professionals. MIS Quarterly 24, 141–168.

Nelson, R. R. (1991). Educational needs as perceived by IS and end-user personnel: A survey of knowledge and skill require ments. MIS Quarterly, 15, 503–525.

Onyemah, V. (2008). Role ambiguity, role conflict, and performance: Empirical evidence of an inverted-u relationship. Journa of Personal Selling & Sales Management, 28, 299–313.

Persson, J. S., Mathiassen, L., & Aaen, I. (2012). Agile distributed software development: Enacting control through media and context. Information Systems Journal, 22, 411–433

Pettijohn, C., Pettijohn, L. S., Taylor, A. J., & Keillor, B. D. (2001). Are performance appraisals a bureaucratic exercise or can they be used to enhance sales-force satisfaction and commitment? Psychology and Marketing, 18, 337–364

Ply, J. K., Moore, J. E., Williams, C. K., & Thatcher, J. B. (2012). IS employee attitudes and perceptions at varying levels of software process maturity. MIS Quarterly, 36, 601–624.

Podsakoff, P., MacKenzie, S., Lee, J., & Podsakoff, N. (2003). Common method biases in behavioral research: A critica review of the literature and recommended remedies. Journal of Applied Psychology, 88, 879–903.

Poppendieck, M., & Poppendieck, T. (2003). Lean software development: An agile toolkit. Boston, MA: Addison-Wesley.

Rai, A., Maruping, L. M., & Venkatesh, V. (2009). Offshore information systems project success: The role of socia embeddedness and cultural characteristics. MIS Quarterly, 33, 617–649.

Ramasubbu, N., Bharadwaj, A., & Tayi, G. K. (2015). Software process diversity: Conceptualization, measurement, and analy sis of impact on project performance. MIS Quarterly, 39, 787–807.

Ramesh. B., Cao. L.. Kim. J., Mohan. K., & James. T. L. (2017). Conflicts and complements between eastern cultures and agile methods: An empirical investigation. Furopean Journal of Information Systems. 26. 206-235

Ramesh, B., Mohan, K., & Cao, L. (2012). Ambidexterity in agile distributed development: An empirical investigation. Informa tion Systems Research.23.323-339

Rizzo, J. R., House, R. J., & Lirtzman, S. I. (1970). Role conflict and ambiguity in complex organizations. Administrative Scienc Quarterly, 15, 150–163.

Rutner, P. S., Hardgrave, B. C., & McKnight, D. H. (2008). Emotional dissonance and the information technology professional MIS Quarterly, 32, 635–652

Sarker, S., & Sarker, S. (2009). Exploring agility in distributed information systems development teams: An interpretive stud in an offshoring context. Information Systems Research, 20, 440–461

Schreurs, P. J. G., & Taris, T. W. (1998). Construct validity of the demand-control model: A double cross-validation approach Work & Stress, 12, 66–84.

Schwaber, K., & Beedle, M. (2002). Agile software development with scrum (Vol. 18). Upper Saddle River, NJ: Prentice Hall.

Sharp, H., & Robinson, H. (2008). Collaboration and co-ordination in mature eXtreme programming teams. International Jour nal of Human-Computer Studies, 66, 506–518

Snijders, T. A. B., & Bosker, R. J. (1999). Multilevel analysis: An introduction to basic and advanced multilevel modeling Thousand Oaks, CA: Sage.

Speier, C., & Venkatesh, V. (2002). The hidden minefields in the adoption of sales force automation technologies. Journal o Marketing.66.98-111

Sultan, F., & Chan, L. (2000). The adoption of new technology: The case of object-oriented computing in software compa nies. IEEE Transactions on Engineering Management, 47, 106–126

Swanson, V., & Power, K. (2001). Employees' perceptions of organizational restructuring: The role of social support. Work & Stress, 15, 161–178.

Thong, J. Y. L., & Yap, C. S. (2000). Information systems and occupational stress: A theoretical framework. Omega, 28 681–692.

Tripp, J. F., Riemenschneider, C., & Thatcher, J. B. (2016). Job satisfaction in agile development teams: Agile development a work redesign. Journal of the Association for Information Systems, 17, 267–307.

Tubre, T. C., & Collins, J. M. (2000). Jackson and Schuler (1985) revisited: A meta-analysis of the relationships between rol ambiguity, role conflict, and job performance. Journal of Management, 26, 155–169.

Tuomivaara, S., Lindholm, H., & Känsälä, M. (2017). Short-term physiological strain and recovery among employees working with agile and lean methods in software and embedded ICT systems. International Journal of Human-Computer Interac tion, 33, 857–867.

Van der Doef, M., & Maes, S. (1999). The job demand-control (-support) model and psychological well-being: A review of 20 years of empirical research. Work & Stress, 13, 87–114.

Venkatesh, V., Maruping, L. M., & Brown, S. A. (2006). Role of time in self-prediction of behavior. Organizational Behavior and Human Decision Processes, 100, 160–176

Venkatesh, V., Rai, A., & Maruping, L. (2018). Information systems projects and individual developer outcomes: Role of pro ject managers and process control. Information Systems Research, 29, 127–148

Venkatesh, V., Shaw, J. D., Sykes, T. A., Wamba, S. F., & Macharia, M. (2017). Networks, technology, and entrepreneurship A field quasi-experiment among women in rural India. Academy of Management Journal, 60, 1709–1740

Venkatesh, V., Sykes, T. A., Chan, F. K. Y., Thong, J. Y. L., & Hu, P. J. H. (2019). Children's internet addiction, family-to-work conflict, and job outcomes: A study of parent-child dyads. MIS Quarterly, 43, 903–927

Venkatesh, V., & Windeler, J. (2012). Hype or help? A longitudinal field study of virtual world use for team collaboration Journal of the Association for Information Systems. 13. 735-771

Vidgen, R., & Wang, X. (2009). Coevolving systems and the organization of agile software development. Information Systems Research, 20, 355–376

Wade, M. R., & Parent, M. (2001). Relationships between job skills and performance: A study of webmasters. Journal of Man agement Information Systems, 18, 71–96.

Wang, X., Schneider, C., & Valacich, J. S. (2015). Enhancing creativity in group collaboration: How performance targets and feedback shape perceptions and idea generation performance. Computers in Human Behavior, 42, 187–195

Watson, R. T., Boudreau, M. C., York, P. T., Greiner, M. E., & Wynn, D., Jr. (2008). The business of open source. Communications of the ACM, 51, 41–46.

Weerakkody, V., Irani, Z., Kapoor, K., Sivarajah, U., & Dwivedi, Y. K. (2017). Open data and its usability: An empirical view from the citizen's perspective. Information Systems Frontiers, 19, 285–300.

Windeler, J., Maruping, L. M., & Venkatesh, V. (2017). Systems development risk factors: The role of empowering leadershi in lowering developers' stress. Information Systems Research. 28. 775-796

Wong. S. S., DeSanctis. G., & Staudenmaver. N. (2007). The relationship between task interdependency and role stress: A revisit of the iob demands-control model. Journal of Management Studies, 44 284-303

Wooldridge, J. M. (2012). Introductory econometrics: A modern approach (5th ed.). Mason: South-Western.

Yu, X., & Petter, S. (2014). Understanding agile software development practices using shared mental models theory. Informa tion and Software Technology, 56, 911–921

Zhang, X., Venkatesh, V., & Brown, S. A. (2011). Designing collaborative systems to enhance team performance. Journal o the Association for Information Systems, 12, 556–584.

How to cite this article: Venkatesh V, Thong JYL, Chan FKY, Hoehle H, Spohrer K. How agile software development methods reduce work exhaustion: Insights on role perceptions and organizational skills. Info Systems J. 2020;1–29. https://doi.org/10.1111/isj.12282

## APPENDIX

## A. MEASUREMENT SCALES

Extent of agile method use (Maruping, Venkatesh, & Agarwal, 2009a)

Pair programming

1. How often is pair programming used on this team? (1 = never; 7 = all the time)

2. On this team, we do our software development using pairs of developers.

3. To what extent is programming carried out by pairs of developers on this team? (1 = never; 7 = all the time)

## Collective ownership

4. Anyone on this team can change existing code at any time.

5. If anyone wants to change a piece of code, they need the permission of the individual(s) that coded it.

6. Members of this team feel comfortable changing any part of the existing code at any time.

## Coding standards

7. We have a set of agreed upon coding standards in this team

8. Members of this team have a shared understanding of how code is to be written.

9. Everyone on this team uses their own standards for coding.

## Continuous integration

10. Members of this team integrate newly coded units of software with existing code.

11. We combine new code with existing code on a continual basis.

12. Our team does not take time to combine various units of code as they are developed.

## Refactoring

13. Where necessary, members of this team try to simplify existing code without changing its functionality.

14. We periodically identify and eliminate redundancies in the software code.

15. We periodically simplify existing code.

## Unit testing

16. We run unit tests on newly coded modules until they run flawlessly.

17. Members of this team actively engage in unit testing.

18. To what extent are unit tests run by this team? (1 = never; 7 = all the time)

Role ambiguity (Rutner et al., 2008)

1. I know exactly what is expected of me.

2. I have clear, planned goals and objectives for my task assignment.

3. I have a defined role in my team.

## Role conflict (Rutner et al., 2008)

1. I sometimes have to buck a rule or policy in order to carry out an assignment.

2. I often perform work for two or more parties who operate quite differently

3. In my work, I have to try to balance two or more conflicting preferences.

## Organizational skills (Nelson, 1991; Wade & Parent, 2001)

1. I can communicate effectively with others.

2. I can recognize and manage personality problems which interfere with job completion.

3. I can work effectively in groups.

4. I can manage projects.

Work exhaustion (Rutner et al., 2008)

1. I feel emotionally drained from my work.

2. I feel used up at the end of the workday.

3. I feel burned out from my work.

## Perceived workload (Rutner et al., 2008)

1. I feel that the number of requests, problems, or complaints I deal with is more than expected.

2. I feel that the amount of work I do interferes with how well it is done.

3. I always feel busy.

## Autonomy (Rutner et al., 2008)

1. In my work, I usually do not have to refer matters to my direct supervisor for a final decision.

2. Usually, my direct supervisor does not have to approve my decisions before I can take action.

3. I can usually do what I want on this job without consulting my direct supervisor.

Fairness of rewards (Rutner et al., 2008)

1. I think my level of pay is fair.

2. Overall, the rewards I receive here are quite fair.

Client representative (Rai et al., 2009)

Following Rai et al. (2009), we used a dummy variable that indicated whether a project team had a client repre sentative present or not.

Requirements uncertainty (Rai et al., 2009)

The number of formal, written changes to the project contract between our focal software vendor and the respective customer was used to measure requirements uncertainty.

## B. TWO-STAGE HECKMAN ANALYSIS

We conducted a two-stage Heckman analysis with an instrumental variable to address endogeneity concerns regard ing the extent of agile method use. This analysis aims to correct path estimates for sample selection bias an provides insight into whether selection bias constitutes a threat to the original analysis of a sample (Wooldridge 2012, p. 619). For example, one would expect the second-stage results of the Heckman analysis (ie, path estimates corrected using the Inverse Mills Ratio) to differ strongly from the original estimations if there were mentionabl sample selection bias.

Because we had controlled for reasonable explanatory variables, we had no options remaining for additiona suitable instrumental variables. We therefore dropped experience in XP that had served as a control variable from the original models and used it as an instrumental variable for the extent of agile method use after re-estimating the models. Following standard procedures (Wooldridge, 2012), we examined the relevance and exogeneity of experi ence in XP for the relationships of the extent of agile method use with role ambiguity and role conflict. Experience in XP lent itself as an instrument as it can reasonably be expected to influence the use of XP and is highly correlated with it in our sample whereas it cannot reasonably be caused by role perceptions and does not show high correla tions with them in our sample (see Table 1)

Models M2 and M5 in Table B1 display the re-estimated models of the original analysis after dropping experience in XP. These models serve as a baseline for comparing corrected and uncorrected estimates. Models M3 and M6 in Table B1 depict the corrected results based on the two-stage Heckman procedure using experience in XP as an instrumental variable for the extent of agile method use. The results of the analysis show that mode M3 does not differ strongly from model M2, and model M6 does not differ strongly from model M5. Instead, the estimates remain qualitatively the same after correcting for the Inverse Mills Ratio. This suggests that sampl selection bias does not constitute a relevant threat to our original analyses and thus reduces endogeneit concerns.

T A B L E B 1 Two-stage Heckman procedure for extent of agile method use and role perceptions

<table><tr><td rowspan="3">Models</td><td colspan="3">Role Ambiguity</td><td colspan="3">Role Conflict</td></tr><tr><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td><td>M6</td></tr><tr><td>Original (Model 2a Table 2A)</td><td>Dropping instrumental var.</td><td>Second stage Heckman model</td><td>Original (Model 2b Table 2A)</td><td>Dropping instrumental var.</td><td>Second stage Heckman model</td></tr><tr><td colspan="7">L1 control variables</td></tr><tr><td>Age</td><td>.12* (.010)</td><td>.13* (.011)</td><td>.11* (.009)</td><td>.12* (.019)</td><td>.13* (.014)</td><td>.11* (.019)</td></tr><tr><td>Gender</td><td>.03 (.022)</td><td>.05 (.020)</td><td>.01 (.025)</td><td>.03 (.027)</td><td>.04 (.029)</td><td>.01 (.030)</td></tr><tr><td>Tenure</td><td>.03 (.027)</td><td>.07 (.029)</td><td>.01 (.031)</td><td>.07 (.026)</td><td>.08 (.029)</td><td>.06 (.030)</td></tr><tr><td>Experience in software development</td><td>-.10 (.012)</td><td>-.11* (.009)</td><td>-.08 (.015)</td><td>-.13* (.019)</td><td>-.11* (.017)</td><td>-.11* (.016)</td></tr><tr><td>Experience in XP</td><td>.04 (.031)</td><td></td><td></td><td>.05 (.026)</td><td></td><td></td></tr><tr><td colspan="7">L2 control variables</td></tr><tr><td>Team size</td><td>.05 (.044)</td><td>.02 (.040)</td><td>.01 (.047)</td><td>.13* (.017)</td><td>.12* (.014)</td><td>.11* (.013)</td></tr><tr><td>Client representative</td><td>-.10 (.022)</td><td>-.10 (.018)</td><td>-.07 (.025)</td><td>-.11* (.015)</td><td>-.12* (.014)</td><td>-.11* (.013)</td></tr><tr><td>Req. uncertainty</td><td>.11* (.012)</td><td>.13* (.009)</td><td>.11* (.011)</td><td>.08 (.022)</td><td>.06 (.027)</td><td>.04 (.028)</td></tr><tr><td colspan="7">Main effects</td></tr><tr><td>Extent of agile method use</td><td>-.23*** (.008)</td><td>-.24*** (.007)</td><td>-.22*** (.008)</td><td>-.22*** (.012)</td><td>-.24*** (.011)</td><td>-.19** (.014)</td></tr><tr><td>Organizational skills</td><td>-.13* (.010)</td><td>-.13* (.009)</td><td>-.11* (.010)</td><td>-.11* (.010)</td><td>-.12* (.009)</td><td>-.11* (.011)</td></tr><tr><td>Model details</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Heckman correction</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Inverse mills ratio (for extent of agile method use)</td><td></td><td></td><td>.15* (.009)</td><td></td><td></td><td>.14* (.011)</td></tr><tr><td>Deviance</td><td>951.48</td><td>996.50</td><td>887.54</td><td>933.56</td><td>958.67</td><td>894.25</td></tr><tr><td> $\chi^2$ </td><td>329.17***</td><td>341.60***</td><td>304.62***</td><td>301.19***</td><td>318.63***</td><td>286.55***</td></tr><tr><td> $R^2$ </td><td>.17</td><td>.17</td><td>.20</td><td>.19</td><td>.19</td><td>.23</td></tr></table>

Note. Results for two-level model: variables team size, client representative, and requirements uncertainty on leve 2 (project, n = 217), all other variables on level 1 (individual developer, n = 1894). Standard errors are shown in parentheses Abbreviation: XP, extreme programming. $^ { * } P < . 0 5 ; ^ { * * } P < . 0 1 ; ^ { * * * } P < . 0 0 1 .$
