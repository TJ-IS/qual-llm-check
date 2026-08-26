---
otero_id: 23763
otero_key: "MGJ9K2QD"
title: "How evolution of information systems may fail: many improvements adding up to negative effects"
authors: "J J Kaasbøll"
year: "1997"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000264"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How evolution of information systems may fail: many improvements adding up to negative effects

JJ Kaasb<sup>ø</sup>ll

Peninsula School of Computing and Information Technology, Monash University, McMahons Road, Frankston, Victoria 3199, Australia

It has been observed in case studies that computer systems evolve through three main processes: initial development, adaptive maintenance, and replacement. Often one system replaces several existing ones. Models of system evolution should therefore include these processes for all the systems being affected. Sometimes, the cumulative effect of small improvements made during adaptive maintenance was dysfunctional; for example, recurrent changes produced spaghetti code which no one dared to change. Possible negative effects of many small changes can be foreseen through improved planning and organization of maintenance. This indicates that systems should be replaced before they deteriorate through amendments. Replacement seems to be easier to carry out than initial development, due to easier requirements engineering. In fifteen out of sixteen processes where computer systems were replaced with newer ones, the new systems were replicas of the old systems with some functionality added. Through repeated replacements, the organizational structure is reinforced. Repeated replacements may therefore result in an inefficient and rigid organization in the long run. Thus many easy-to-accomplish replacements of program code, each of which were intended to improve efficiency, may cause the counter result in the end.

## Introduction

When having to decide whether to continue updating a computer-based system or replacing it with a new system, the research literature contains little advice. Sakthivel (1994) has suggested a theoretical model of maintenance and development, but organizational and policy issues are often of more importance when decisions to update or replace are made (Mårtensen, forthcoming). Without having any ambition to solve these general problems, this paper aims to show how improvement of systems during one period may increase the need for system replacement at later stages. Furthermore it aims to indicate issues to be considered during replacement.

Since models and methods of system development usually cover the initial development or the lifetime of one application system, changes having effects in the longer run must be studied within a longer frame of reference. This frame of reference is explained in the following paragraphs.

Studies of maintenance (Swanson & Beath, 1989; Marche, 1993) have shown that application systems are continuously adapted to new functional requirements. This finding of adaptive maintenance questions the sharp distinction between use and development found in system development methods.

Empirical studies of system development from the 1990’s (Saarinen & Heikkila¨, 1990; Braa et al, 1996) indicate that a large proportion of development projects consists of replacement of old computer systems with new ones. The new systems, to a large extent, implement the same functionality as the old ones. In addition, a new implementation also often includes the functionality of a small number of minor systems, thus making the minor systems obsolete (Toft, 1992).

Since one computer system may replace several others, a model of development of computer support in an organization should include all the relevant computer systems, not only the life of a single computer application. We identify initial development, adaptive maintenance, and replacements as the three processes that constitute the evolution of computer systems in an organization. These processes may correlate with changes in work tasks, learning, restructuring of the organization, and other organizational changes. Such a model of evolution extends and refines Floyd et al’s (1989) and Budde et al’s (1992) models of evolution of computer systems, which emphasised the relation between use and development of a single system. The evolution of computer systems can be illustrated as in Figures 1 and 2.

Within the initial development and within the replacement process, a range of strategies from a waterfall approach to spiral model with stepwise implementation may be chosen. It has been claimed that the spiral model approach leads to systems that suit user needs better than the waterfall model (Thomson, 1993; Bu¨ rkle et al, 1995). Problems with spiral models have also been recognised; eg, less control (Burns & Dennis, 1985), and mismatch with fixed price contracts (Boehm, 1988). Risk management (Boehm, 1988) has been suggested as a way to manage the process, and the need for tighter project control has been emphasised (Mathiassen & Stage, 1992).

![](/api/attachments/MGJ9K2QD/fulltext/images/5732c55cc34d609472ed239b81efc172f8004aa28f054cbc4c187f690c35fa6b.jpg)  
Figure 1 The initial development, replacement and adaptive maintenance of computer applications.

![](/api/attachments/MGJ9K2QD/fulltext/images/82e79514335917a95dbf16b0151e7bb6b5374489a35fc454db5d224f2693c61f.jpg)  
Figure 2 The initial development, replacement, and adaptive maintenance processes in general.

In the area of adaptive maintenance, backlogs of user requests are often mentioned as a problem, and it has been observed that users develop manual routines for working around computer systems that do not fit work tasks properly (Gasser, 1986). Tailoring has been suggested as a means for adapting computer systems to individual needs (eg, Henderson & Kyng, 1991).

The bulk of research has so far been focused on initial development, with less attention given to adaptive maintenance, and even less to replacements. The research project Functional Integration through Redesign (FIRE) (Braa et al, 1993) was set up to explore replacements. A general observation was that both maintenance and replacement were poorly organised (Braa et al, 1996).

The current paper reports and explains how many improvements of systems do add up to a negative effect. The pattern of change producing undesirable effects tallies with the phenomenon called ‘counterfinality,’ which appears when individuals’ actions create collective results that were not intended (Elster, 1983), see section ‘The structure of counterfinal phenomena’.

Counterfinal changes during maintenance are reported in the next section, and ways to avoid the problems are suggested after the general pattern has been considered. Possible counterfinal phenomena of replacements are discussed at the end.

## Adaptive maintenance

Sixteen studies of the evolution of information systems in organizations were carried out by the project FIRE. The changes observed included both replacements of existing computer systems with new ones as well as small changes of systems currently in operation. The computer systems studied were small to medium sized administrative systems, often being used by several, separate organizational units. The sizes of organizations were from 10 to 10 000 employees.

The projects have been examined through qualitative case studies. The case study methodology was chosen because of the relatively unknown problem area. There were neither prior hypotheses nor interview questions concerning possible counterfinal effects. These were revealed after the data had been collected. Details on research methods are provided in the reports of the empirical studies (Bratteteig & Øgrim, 1992; Toft, 1992; Bjerknes, 1994; Kaasb<sup>ø</sup>ll & Øgrim, 1994; Greenbaum et al, 1996).

Two cases of small changes and one more general observation are presented in the following sections.

## Individual adaptation

One of the phenomena studied took place in a research institution, where researchers used five different editors on computers that were based on four different operating systems (Kaasb<sup>ø</sup>ll et al, 1993). It was quite common that they wrote reports together, and the data from each researcher could not easily be transferred into the common report. The secretaries had to convert the files from each researcher to a common format. Ten of the researchers did not have a printer connected to their computers, so they had to copy their files to a diskette and ask a colleague to use his or her computer for a printout.

The researchers selected the hardware and software equipment to suit their personal preferences, and each of them benefited from the anarchic installation of software. The justification for the lack of standardisation was that many of the researchers only stayed in the institution for a short period of time.

The single computer support person in the institution was fully occupied with the daily operation of the diverse collection of equipment. Consequently, he had little time for planning a more coherent computer network, which he thought would be necessary for providing decent computer support for the researchers in the long run.

Many of the companies and public institutions in the other cases studied in the project had departmental computer solutions, such that the organization had many technological platforms. These organizations had difficulties when transferring data between the organizational units. The strategy of the computer departments was to redesign systems according to organizational standards.

## Software extension

A system for ticket sales in a large transport organization had been in use for some years, and the users seemed satisfied with its operation (Kaasb<sup>ø</sup>ll & [grim, 1994). There was a requirement that the response time for the system at the front-desk should be seven seconds at most. The system was programmed in a fourth generation language because the computer department knew this language well. Since the language required much computing power during run time, the system’s response had been slow, but within the seven seconds.

Over the years, the system was extended with new functionality, piece by piece. Many of the extensions were added because of suggestions from front-desk personnel. The computer department was in charge of deciding whether to add a new extension, and they implemented as many of the changes as possible.

On one occasion, the system was extended with a module that could suggest alternative travel routes. This functionality was added to improve service at the counter. This extension caused a severe increase in response time; bringing it very close to the seven seconds limit. The front-desk personnel reacted negatively, as in Lie and Rasmussen’s (1985, p 69) study:

When the employees, and those who request them, have been accustomed to the quick response time, periods of waiting are felt like an eternity. Because one never knows when the image will pop up on the screen, one keeps waiting and looking at it. This indeterminate waiting compared to the expectation of an immediate feedback, creates what we call waiting stress.

The busier the employee is, because of unfinished work piling up or a customer waiting on the phone, the more stress is experienced during such waiting. One is deprived of one’s own control of the work. The computer controls the speed.

The front-desk personnel also worked in a situation where customers were waiting, so the slow response from the system created unfavourable working conditions. They felt that the response time had increased to a duration that more than outweighed the additional functionality, and hence degraded the service they could offer to their customers.

Extensions of functionality often bring about degraded response time. This is frequently documented in tests of new software products, and the extension of software is used to promote the purchase of faster computers. Because waiting stress is also a common phenomenon, the sum of extensions of functionality intended to improve efficiency becomes counterproductive if the hardware remains unchanged.

## Minor modifications

In all the projects where the code was replaced, the poor quality of the code was mentioned as one of the reasons for the replacements. “The old system was maintained to death” (Toft, 1992) was an expression used to denote the incomprehensible program code of a system. No one took the risk of changing the system any longer, because a small modification could result in unpredictable errors in other parts of the system. This spaghetti quality of the code was itself a result of many small modifications made to align the functionality of the system with changing needs.

Swanson and Beath (1989) report that much effort is put into minor modifications of systems, such that there is reason to believe that the systems of which they report also have had their code quality degraded. Poor code which is a result of many minor modifications may therefore be a reason for replacement projects in general. Since the modifications, to a large extent, are carried out to improve functionality, the total result of the improvements are systems that can no longer be improved. Hence they cannot be adjusted to changing requirements.

## The structure of counterfinal phenomena

In the examples studied, many smaller actions took place successfully. People or departments adapted the software to their needs, each program extension was carried out to take care of a new requirement, and each modification was also made to enhance functionality of the system. Even if each small change improved the computer system, the total result could be counter to what was wanted: data transfer was hampered, response time rose intolerably, and the program code became unmanageable. The common pattern is that individuals’ actions create collective results that no individual intended. In an exposition of different theories of technical innovation, Elster (1983) calls this pattern ‘counterfinality,’ and counterfinal phenomena have a common explanation. The individual action is accounted for through intentional explanation, and the collective results can be causally explained.

The concept of counterfinality is based on the assumption that human beings act in order to reach future goals. To have a reason to reach a goal means that one should both have a motivation to reach the goal, and a belief that the action brings about the goal. An intentional explanation of an action requires that it can be shown that an actor both had the motivation and the belief (Elster 1983, p 70f).

Intentional explanation is defined for individuals. To transfer intentional explanation to a group or organizational level, there have to exist organizational goals, and it must be substantiated that the individuals have internalised the organizational goals.

Two events are causally related if one event, the cause, causes the other, the effect, in a way that corresponds to a physical regularity of nature (von Wright, 1984).

Knowledge of causal regularities can be expressed by causal laws. A causal law states that whenever an event (cause) of type C happens, another event (effect) of type E follows. The type C cannot be completely known, however (von Wright, 1984, p. 140). It relies on ceteris paribus conditions, i.e., other things being equal. For example, in the case of software extension, a cause for a longer response time is that the program has to execute more steps than before the extension.

Counterfinality occurs when intentional actions fulfil the actors’ goals, and the effect of each action causes an overall result counter to the actor’s goals (Elster, 1983, p. 84).

In the case of individual adaptation, the researchers said that they installed the software because they wanted to adapt the computer system to their work and skills. A likely interpretation is that they also believed that the installation would bring about the adaptation. Given that they had the positive attitude and belief, these factors constitute the intentional explanation of their adaptation. In the causal explanation of the total effect, the cause is that each researcher produced data with a different format. The effect was lack of ability to transfer data where needed. A ceteris paribus condition in this case is that there were no automatic conversion programs that could integrate the data with different formats.

In the software extension case, the developers wanted to enhance the functionality of the system, and they believed that adding a module would do so. This is an intentional explanation of the software extension. In total, an extension of program code (the cause) causes prolonged execution time of the program (an effect), which in turn caused delays in service (counterfinal effect). The absence of faster hardware is one ceteris paribus condition for this causal explanation.

The minor modifications were carried out for the same reason as the software extension: the desire to enhance functionality and the belief that modifying software would bring about the enhancement (Toft, 1992). The modifications also caused the deterioration of the software. This effect depends on the software being unprepared for change and the programs not restructured when changes are made.

The structure of counterfinal phenomena outlined above consists of intentional actions and causal connections between effects of actions. This is a very general structure that can be found for most phenomena where human action is involved. In addition, there are specific conditions that produce a cumulative result that contradicts goals. If there exists a global control of the mechanisms that produces the total effect, the conditions for the counterfinal phenomena will be different from the situation where no global control exists. The situation with no global control is called the market setting, while the controlled situation is called an organizational setting. These settings are explored in the two following sections.

## The market setting

In the market setting, actors behave according to individual preferences with no collective goals. Elster (1983)

describes the conditions of counterfinality in this setting:

Erroneous beliefs about others. The actor falsely believes that she or he is the only actor who carries out this kind of action, thus thinking the counterfinal result will never occur, even if knowing that the action also contributes to counterfinal results.

Individual adaptation where no common standards exist resembles the market. If users individually adapt their computer system and also believe that nobody else adapts, they will believe that they obtain both the benefit of the integrated system and those of their own adjustments.

The erroneous belief that others will not carry out the same action was used by Elster (1983) to explain overproduction in a market. When prices are high, producers will increase their production to maximise profit. If every producer thinks and acts the same way, the result will be overproduction and declining prices.

Counterfinality may also emerge if the actors are unaware of the consequences of the actions:

Undetected counterfinal effects. The actor does not know that the action contributes to the counterfinal result.

The ticket sellers in the software extension case probably did not known that their requests for improvements worsened the response time from their own systems, and the developers extending the software may (on some occasions) have been unaware that their efforts produced poorer service.

Both the erroneous belief and the undetected effects may take place in a pure market situation, where actors are free to choose between alternative actions. If there are no regulations for selection of software and hardware in a company, user behaviour may resemble the market mechanism.

## Inside and outside understanding of intentions and causal effects

Developers and users obtain their knowledge of computer systems within different contexts. A person not living within the context of others, but trying to understand them, is gaining an ‘outside understanding’ of the others (Pike, 1967). Since developers and users do not share a context, developers obtain outside understanding of users and vice versa (Kaasb<sup>ø</sup>ll, 1995). The operations for obtaining outside understanding are observation and measurement of material phenomena and behaviour (Pike, 1967). Understanding intentions, meanings, values, rules etc, has to be inferred from behavioural patterns. The way to test whether or not an outside understanding is adequate, is to relate it to observations of people’s behaviour, without asking them about their own opinion of the understanding.

In contrast, inside understanding is gained when studying behaviour as seen from persons inside the context. People understand each other by interacting with each other, in order to learn about their own accounts of their plans, goals, values, meanings, etc, and their own explanations of their behaviour (Pike, 1967, p. 37; Harris, 1990, p. 53). The evaluation of whether an inside understanding of people’s thoughts is adequate and accurate, depends on the opinion of the people themselves (Harris, 1975, p. 159).

Knowledge of the counterfinal situation requires understanding of both the reasons that the actors have and the cumulative effects of these actions. The reasons include people’s intentions and motives, and how they understand the world, i.e., knowledge of their mental states. Mental issues cannot be directly observed. However, when a person, for example, expresses a positive attitude towards a computer system, and an observer knows that the person has not actually used the system when expected, the observer may judge the person’s attitude to be negative, which does not correspond to the person’s own description. In general, others’ inferences about people’s mental states are necessary to describe lies, confusion, forgetfulness and repression.

The causal effects of actions are often more easily open for observation; for example, frequency of use and response time of the computer can be measured.

The distinctions between inside/outside context and intentional/causal explanations lead to four types of understanding of people’s actions and the effects of these actions. The types of understanding inherent in the assessment of user actions and developer actions in the software extension project are summarised in Table 1.

Table 1 Assessments of the software extension project

<table><tr><td>Assessment of users&#x27; actions</td><td>User&#x27;s own opinion</td><td>Developers&#x27; observations and inferences</td></tr><tr><td>Users&#x27; values, goals, intentions</td><td>To carry out their work tasks with computer support and without delay.</td><td>That the users wanted extended functionality.</td></tr><tr><td>Effects of users&#x27; actions</td><td>That the computer&#x27;s response time delays their work.</td><td>That the extended functionality improved their work.</td></tr><tr><td>Assessment of developers&#x27; actions</td><td>Users&#x27; observations and inferences</td><td>Developers&#x27; own opinion</td></tr><tr><td>Developers&#x27; values, goals, intentions</td><td>That the developers wanted to improve the computer systems</td><td>To extend the functionality of the computer systems.</td></tr><tr><td>Effects of developers&#x27; actions</td><td>That functionality was added while response time increased</td><td>That the computer&#x27;s functionality is extended</td></tr></table>

There was a discrepancy between the users’ and the developers’ assessment of the users’ intentions and the effects of their actions. The users experienced the counterfinal effect, while they did not foresee the causal connection between the extensions they wanted and the increasing response time. The developers could foresee the increased response time, but they did not experience it as a serious defect, because they were not sufficiently aware that a quick response was important for the users.

In more general terms, if developers know of the causal link that produces the counterfinal effect, while users carry out the intentional actions, and these groups are ignorant of each other’s knowledge, neither group has sufficient knowledge to foresee the counterfinal effect. To avoid this situation, the users should be informed about the outside understanding of developers, and the developers should become knowledgeable of the inside understanding of users.

## Avoiding counterfinals

One prerequisite to prevent counterfinal phenomena from appearing in the market situation is to bring together the appropriate persons so that they can share their knowledge. Mutual learning between users and developers has been mentioned as essential for system development (Bjerknes & Bratteteig, 1987). Appropriate techniques for bringing user experience and technical competence into development processes are soft systems methodology (Checkland & Scholes, 1990), and cooperative design techniques (Greenbaum & Kyng, 1991). When small changes are carried out, one can hardly engage in laborious techniques for every single modification. A better way of preventing counterfinal phenomena may be to bring the groups together when planning routines for system changes. Then consequences of changes can be discussed and ways of handling them can be organized along with procedures for system maintenance. In order to deal with preferences and interests, techniques aiming at negotiation like “priority workshops” (Braa, 1995) may help to prevent or handle counterfinal situations.

## The organizational setting

In his explanation of counterfinal phenomena, Elster (1983) only refers to settings with no global control. Since counterfinal phenomena are also observed where there is control of individual action, this paper will try to extend the concept to cover this situation as well.

Organizations impose regulations on their members, but this imposition does not guarantee that counterfinal results will not appear. Rules and management decisions may make actors carry out actions they otherwise may have avoided. A third condition for counterfinality when appearing in an organization is therefore:

External reasons. The actor knows that the action also contributes to results that are counter to his or her goals, but there are compelling reasons for nevertheless carrying out the action.

When users demand small changes, the developers may be required to carry out the many minor modifications, even if they know that this will make the code deteriorate.

The researchers in the individual adaptation case knew that their individual choice caused trouble when the reports had to be compiled. They regarded their own effort of learning a new editor as larger than the secretary’s effort of compiling the reports. Their own time for learning was the compelling reason for keeping to the individual adaptation.

In order to reverse the situation in the research institution, the secretaries or the computer support person would have had to work for a change that would have been in conflict with the researchers’ desires. Given the lack of power of the secretaries and the support person, this seemed unrealistic.

To avoid the counterfinal phenomena in the organization setting, knowledge of the phenomena is necessary for the same reasons as in the market setting. The organizational setting differs because knowledge is not sufficient; power to reduce the pressure to act counterfinally is also necessary.

Soft systems methodology (Checkland & Scholes, 1990) and techniques aiming at giving priorities (Braa, 1995) may support negotiations of interests, and thereby possibly influence decisions concerning development and maintenance of the systems. However, the general issues of influence on computer systems will not be considered here; a recent overview of relevant knowledge concerning user participation is found in Cavaye (1995).

## Initial development

In the introduction to the paper, the evolution of computer systems was characterised as consisting of three processes: initial development, adaptive maintenance, and replacement. While the previous examples concerned maintenance, this section will consider a case of initial development. This case may also seem counterfinal. However, in the long run it may turn out not to be so.

A municipal agency for buildings and surveillance has approximately 350 PC’s in a network and 50 application programs (Greenbaum et al, 1996). The computer department, consisting of ten persons, has its working hours more than filled with maintaining the network and integrating the applications. According to a top management decision, the organization is not allowed to develop systems on its own. Even so, when users ask for a simple, new application, the computer department usually helps them by building an application by means of a spreadsheet or another tool. Thus they increase the problem of maintaining and integrating the applications. Continuing this practice probably leads to an incomprehensible web of application systems, which is the counterpart of spaghetti code at the system level.

Being aware of this trap, the computer department finds it useful to also develop the applications when considering long term goals. The reason for long term usefulness is that the small, tailored applications function as specifications when the organization purchases new, large systems for replacing the older ones. Through building the small applications, the organization has learned more about their needs. It is also easier to say that the proposed new system shall have functionality similar to the existing ones, than it is to get the users to provide a written requirement specification. The small initial developments function in this way as prototypes during the replacement process.

## Replacement

In the adaptive maintenance section of this paper, the effect of many minor modifications was discussed. Correspondingly, when shifting focus to replacements, the long term effect of many replacements will be considered.

In a study of systems installed in 184 organizations in New York, Rule and Attewell (1989) found that 85% of the computer systems were direct conversions of noncomputerised operations.

Fifteen of the sixteen replacements of systems studied in FIRE were replicas of the old systems, with some functionality added. It seems that organizational redesign is the exception.

One reason for the high frequency of replacements with only small functional changes may be that this process is much easier to carry out than changing organizational structure and routines. It is assumed that getting to know the requirements is a difficult task in development. During replacement, the old system acts as a prototype for the new one. Some of the requirements for the new system are simply that it reproduces the functionality of the old one. In addition, there is a list of unimplemented changes, constituting the adaptive maintenance backlog.

Developers’ ignorance of users’ tacit knowledge of their work has been emphasised as a problem in initial development. The problem is partly due to users not knowing how the computer system will affect work, so they do not explicate aspects of work which are obvious from their points of view. During replacement, the old system constitutes a tangible object of communication to which both the users and the developers can refer.

Such an object constitutes an advantage as compared to initial development. However, it is known that computer systems are used in ways not intended (Gasser, 1986), often due to users adapting their tasks to the available application functionality. These practices are also often not made explicit unless outside personnel observe the work practices and discuss the computer use in the work setting.

Computer technology can be used for reengineering the organization (e.g., Davenport, 1993). It is claimed that, on the one hand, great benefits of computerisation can only be achieved if the organization is redesigned, although restructuring the organization is a process that requires much effort, and the process may be risky to carry out. On the other hand, if replacing a computer system with a similar one, or making a computer system replicate a manual system, then only minor increases in efficiency can be achieved. A new application with similar functionality as the old system will be less likely to trigger new ideas of use than would a completely different system. In addition, a new computer system mirroring an old solution reinforces the routines and structures of organizations.

Modernised systems that replicate old ones, reinforce structures in the organization, while substantial improvements of efficiency require restructuring. Consequently, repeated replacements of program code make the organizational structures even harder to change. This implies that each replacement decreases the opportunity for boosting efficiency. Thus, replacement of program code may also turn out to be counterfinal: each replacement that is intended to increase efficiency contributes to a contrary result in the long run.

The pros and cons of replacement and restructuring are summarised in Table 2.

## Conclusion

Evolution of computer systems in organizations has been studied and analysed according to three processes: initial development, adaptive maintenance, and replacement. Case studies showed that changes regarded as minor improvements at one stage may add up to dysfunctional results in the long run. The negative effects are due to individuals carrying out actions that create collective results that no individual intended. This is called counterfinality, and insights into all the three processes of evolution have been achieved through analysis of counterfinal effects.

Table 2 Replacing code versus restructuring the organizaton

<table><tr><td></td><td>Pro</td><td>Counter</td></tr><tr><td>Replacing code</td><td>Easy to achieve</td><td>Organizational structure is reinforced</td></tr><tr><td>Restructuring the organization</td><td>Significant increase in efficiency</td><td>Costly and risky</td></tr></table>

Possible negative effects of many small changes can be foreseen through improved planning and organization of adaptive maintenance. User participation in adaptive maintenance may be as important as in initial development. The possible negative effects of maintenance indicate that computer systems should be replaced before the maintenance backlog is overwhelming.

There were also indications of counterfinal replacements. Computer systems were replaced with newer ones, which were reproductions of the old systems with some added functionality. These replacements were easy to carry out, while implementing information systems that support restructuring of the organization is normally a lot harder to carry out. A replacement will therefore reinforce the organizational structure, and repeated replacements may thereby produce an inefficient and rigid organization in the long run. Thus many easy-toaccomplish replacements of program code, each intended to improve efficiency, may cause the counter result in the end.

Long term effects of many replacements cannot be verified through the material reported here. There is a need for longitudinal research concerning the effects of isolated replacements of computer systems.

Budde et al’s (1992) model of system evolution was restricted to one computer system and included initial development, maintenance and versioning. The evolutionary model proposed in this paper is based on the observation that replacement processes constitute a large proportion of the changes of computer applications, and that a new system often replaces several old ones. Therefore, a model of computer systems evolution has to include the initial development, adaptive maintenance, and replacement of several systems.

The observations also indicate that replacements are easier to carry out than initial development, because requirements analysis is easier to carry out on computerised information systems than on manual systems. If this is generally true, models of expenses of system evolution (Sakthivel, 1994) should take this into account. More research should be undertaken to assess the generalisability of the finding.

When an increasing proportion of analysis is carried out based on old computer systems and maintenance backlogs, system analysts should be trained for these tasks. That is not to say that replacement can rely only on these sources. Analysis during replacement also has to compare old systems with current needs, so skills in analysis of work tasks, routines, and organization are still important.

Information systems graduates should be capable of finding requirements from current systems. This need for knowledge should be reflected in courses and textbooks on requirements engineering and system analysis. However, current textbooks do not seem to address this issue properly. The issue is mentioned directly in the textbook of Hawryszkiewycz (1994, p 63), but he provides no guidance for how to carry out the task. An object oriented analysis and design book mentions the usefulness of examining existing systems (Booch, 1994, p 157). Others only mention the usefulness of automated data dictionaries (Kendall & Kendall, 1995), while the issue seems to be totally neglected in some books (e.g., Benyon-Davies, 1993). What is even more disappointing is that the issue of replacement is neglected in recent books on requirements engineering (Jirotka & Goguen, 1994; Macauley, 1996). Textbooks should explain how requirements engineering can be carried out based on existing systems, and also warn against reinforcing organizational structure through repeated replacements.

Acknowledgement – The empirical material used in this paper has also been analysed in a report coauthored with Tone Bratteteig. Des Casey and Nyorie Lindner have helped to strengthen the argument and improve the language. Thanks also to Eevi Beck, Joan Greenbaum, Frieder Nake and Markku Nurminen for constructive comments, to Gitte Mårtensen for discussions of the subject, and to Kristin Braa for encouragement.

## References

<sup>Benyon-Davies P</sup> (1993) Information Systems Development: An Introduction to Information Systems Engineering. (Second Edition) The Macmillan Press, Houndmills, UK.

<sup>Bjerknes G</sup> (1994) Integration of data or information. An example from the police. In Business Process Re-engineering: Information System Opportunities and Challenges. (<sup>Glasson B</sup> et al, Eds), pp 137–145, North-Holland, Amsterdam.

<sup>Bjerknes</sup> <sup>G</sup> and <sup>Bratteteig</sup> <sup>T</sup> (1987) Florence in Wonderland: System development with nurses. In Computers and Democracy: A Scandinavian Challenge (<sup>Bjerknes G, Ehn P</sup> and <sup>Kyng M,</sup> Eds) pp 279–295, Avebury Gower Publ., Aldershot.

<sup>Boehm, BW</sup> (1988) A Spiral Model of Software Development and Enhancement. IEEE Computer 21(5), 61–72.

<sup>Booch</sup> <sup>G</sup> (1994) Object-Oriented Analysis and Design with Applications. (Second Edition) Rational, Santa Clara, California.

<sup>Braa</sup> <sup>K</sup> (1995) Priority Workshops: Springboard for User Participation

in Redesign Activities. In Proceedings of the Conference on Organizational Computing Systems COOCS ’95, pp 246–255, ACM SIGOIS, California.

<sup>Braa K</sup> et al (1993) Barriers and Triggers for Development for Functional Integration – A case study. In Proceedings of the 16th IRIS (<sup>Bansler J</sup> et al, Eds), pp 361–375, Report No. 93/16, Department of Computer Science, University of Copenhagen.

<sup>Braa</sup> <sup>K,</sup> <sup>Bratteteig</sup> <sup>T</sup> and <sup>Øgrim</sup> <sup>L</sup> (1996) Organizing the Redesign Process in System Development. The Journal of Systems and Software 33(2), 133–140.

<sup>Bratteteig</sup> <sup>T</sup> and <sup>Øgrim</sup> <sup>L</sup> (1992) Strategies for cooperation and development. Report from a preliminary project to the FIRE project. (In Norwegian) FIRE Report 5, Department of Informatics, University of Oslo.

<sup>Budde</sup> <sup>R</sup> et al (1992) Prototyping: An Approach to Evolutionary System Development. Springer-Verlag, Berlin

<sup>Burns</sup> <sup>RN</sup> and <sup>Dennis</sup> <sup>AR</sup> (1985) Selecting the appropriate application development methodology. Data Base 16(3), 19–23.

Bu¨ rkle U, Gryczan G <sub>and</sub> Zu¨ llighoven H <sub>(1995) Object-oriented</sub> system development in a banking project: methodology, experience, and conclusions. Human-computer interaction 10(2/3), 293–336.

<sup>Cavaye ALM</sup> (1995) User participation in system development revisited. Information & Management 28, 311–323.

<sup>Checkland</sup> <sup>P</sup> and <sup>Scholes</sup> <sup>J</sup> (1990) Soft Systems Methodology in Action. John Wiley, Chichester.

<sup>Davenport</sup> <sup>TH</sup> (1993) Process innovation: reengineering work through information technology. Harvard Business School Press, Boston, Mass.

<sup>Elster</sup> <sup>J</sup> (1983) Explaining Technical Change. Cambridge University Press and Universitetsforlaget, Cambridge.

<sup>Floyd C, Reisin FM</sup> and <sup>Schmidt G</sup> (1989) STEPS to Software Development with Users. In ESEC ’89: 2nd European Software Engineering Conference (<sup>Ghezzi</sup> <sup>C</sup> and <sup>McDermid</sup> <sup>JA</sup>, Eds), pp 48–64, LN387, Springer-Verlag, Berlin.

<sup>Gasser</sup> <sup>L</sup> (1986) The Integration of Computing and Routine Work. ACM Transactions on Information Systems 4(3), 205–225.

<sup>Greenbaum</sup> <sup>J</sup> and <sup>Kyng</sup> <sup>M</sup> (1991) Design at Work: Cooperative design of computer systems. Lawrence Erlbaum, Hillsdale, NJ.

<sup>Greenbaum</sup> <sup>J</sup> et al (1996) A long term study of the overall need for information technology in the Planning and Building Authority (In Norwegian) Department of Informatics, University of Oslo.

<sup>Harris</sup> <sup>M</sup> (1975) Culture, People, Nature: An introduction to general anthropology. (Second Edition) Thomas Y Crowell, New York.

<sup>Harris</sup> <sup>M</sup> (1990) Emics and Etics Revisited. In Emics and Etics: The Insider/Outsider Debate (<sup>Headland</sup> <sup>TN,</sup> <sup>Pike</sup> <sup>KL</sup> and <sup>Harris</sup> <sup>M,</sup> Eds), pp 48–61 Sage Publications, Newbury Park, California.

<sup>Hawryszkiewycz IT</sup> (1994) Introduction to Systems Analysis and Design. (Third Edition) Prentice-Hall, Sydney.

<sup>Henderson</sup> <sup>A</sup> and <sup>Kyng</sup> <sup>M</sup> (1991) There’s no place like home: Continuing design in use. In Greenbaum & Kyng, 1991, pp 219–240.

<sup>Jirotka M</sup> and <sup>Goguen JA</sup> (Eds) (1994) Requirements Engineering: Social and Technical Issues. Academic Press, London.

<sup>Kaasbøll</sup> <sup>J</sup> (1995) Knowledge from the inside and outside in participative development and research on participative development. In 6th Australasian Conference on Information Systems. Conference proceedings (<sup>Pervan G</sup> and <sup>Newby M,</sup> Eds), pp 413–429, Curtin University, Perth.

Kaasbøll J, Braa K <sub>and</sub> Bratteteig T <sub>(1993)</sub> <sub>User</sub> <sub>Problems</sub> <sub>Con-</sub> cerning Functional Integration in Thirteen Organizations. In Human, Organizational, and Social Dimensions of Information Systems Development (<sup>Avison</sup> <sup>D,</sup> <sup>Kendall</sup> <sup>J</sup> and <sup>DeGross</sup> <sup>JI</sup>, Eds), pp 61– 81, North-Holland, Amsterdam.

<sup>Kaasbøll</sup> <sup>J</sup> and <sup>Øgrim</sup> <sup>L</sup> (1994) Super-Users: Hackers, Management

## About the author

Jens Kaasbøll has published in the Journal of Information Systems, the Journal of Object-Oriented Programming, and at many international conferences. He has been a co-editor of the Scandinavian Journal of Information Systems. His research

Hostages, or Working Class Heroes? A study of user influence on redesign in distributed organizations. In Proceedings of the 17th IRIS (Kerola A, Juustila J and Ja¨rvinen P, Eds), pp 784–798, University of Oulu, Department of Information Processing Science, Research Paper Series A 21, Part II.

<sup>Kendall</sup> <sup>KE</sup> and <sup>Kendall</sup> <sup>JE</sup> (1995) Systems Analysis and Design. (Third Edition) Prentice-Hall, Englewood Cliffs, NJ.

<sup>Lie</sup> <sup>M</sup> and <sup>Rasmussen</sup> <sup>B</sup> (1995) Office Work and Skills. In Women, Work and Computerization: Opportunities and Disadvantages. <sub>(</sub>Olerup A, Schneider L <sub>and</sub> Monod E<sub>,</sub> <sub>Eds),</sub> <sub>pp</sub> <sub>43–52</sub> <sub>North</sub> Holland, Amsterdam.

<sup>MaCauley</sup> <sup>LA</sup> (1996) Requirements Engineering. Springer-Verlag, London.

<sup>Mathiassen</sup> <sup>L</sup> and <sup>Stage</sup> <sup>J</sup> (1992) The principle of limited reduction in software design. Information Technology and People, 6(2–3), 171–185.

<sup>Marche</sup> <sup>S</sup> (1993) Measuring the stability of data models. European Journal of Information Systems 2(1), 37–47.

<sup>M</sup>Å<sup>rtensen</sup> <sup>G</sup> (forthcoming) Conditions for exchanging program code in applications. (In Norwegian) Master’s Thesis, Department of Informatics, University of Oslo.

<sup>Pike</sup> <sup>KL</sup> (1967) Language in Relation to a Unified Theory of the Structure of Human Behaviour (Second, revised edition) Mouton & Co, The Hague.

<sup>Rule</sup> <sup>J</sup> and <sup>Attewell</sup> <sup>P</sup> (1989) What do computers do? Social Problems 36(3), 225–241. Reprinted in Computerization and Controversy: value conflicts and social choices (<sup>Dunlop</sup> <sup>C</sup> <sup>and</sup> <sup>King</sup> <sup>R,</sup> Eds) Academic Press, 1991, pp 131–149.

<sup>Saarinen</sup> <sup>T</sup> and <sup>Heikkila¨ J</sup> (1990) Methods and Tools for Developing New Information Systems and Enhancing or Replacing the Old Ones. In Precedings of the 13th IRIS (<sup>Hellman</sup> <sup>R,</sup> <sup>Ruo-</sup> <sup>honen</sup> <sup>M</sup> and <sup>Sørgaard</sup> <sup>P,</sup> Eds), pp 559–582 Reports on Computer Science & Mathematics, Ser. A, No. 107, Åbo Akademi University, Turku, Finland.

<sup>Sakthivel</sup> <sup>S</sup> (1994) A decision model to choose between software maintenance and software redevelopment. Journal of Software Maintenance 6, 121–143.

<sup>Swanson</sup> <sup>EB</sup> and <sup>Beath</sup> <sup>CM</sup> (1989) Maintaining information systems in organizations. John Wiley & Sons, Chichester.

<sup>Thomson KS</sup> (1993) The Mentor Project Model: A Model for Experimental Development of Contract Software. Scandinavian Journal of Information Systems 5, 113–131.

<sup>Toft</sup> <sup>JHB</sup> (1992) From Old to New Computer Systems: – Data modelling, prototyping, conversions, and training. (In Norwegian) Master’s Thesis, Department of Informatics, University of Oslo.

<sup>von</sup> <sup>Wright</sup> <sup>GH</sup> (1984) Truth, Knowledge and Modality. Basil Blackwell, Oxford.

interests include object oriented analysis and design, management and replacement of information systems, and problem based learning. He is currently on leave from an associate professor position at the University of Oslo, Norway.
