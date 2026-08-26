---
otero_id: 17791
otero_key: "KYEP5N4J"
title: "A prototype approach to information system design and development"
authors: "Laurent Bally; John Brittan; Karl H. Wagner"
year: "1977"
journal: "Information & Management"
doi: "10.1016/0378-7206(77)90005-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Prototype Approach to Information System Design and Development

Laurent BALLY
SESA-Deutschland GmbH.

John BRITTAN
Military Vehicles and Engineering Establishment, Chertsey, UK

and

Karl H. WAGNER
FEM, Bonn, Fed, Rep. Germany

Many organisations view the development of an information processing system as a linear process consisting of an ordered sequence of steps from conception to hand-over and make no provision for alternative strategies. While excellent in many circumstances, the linear strategy is not the only possible approach. This paper discusses alternatives, with particular reference to a prototype strategy, which has some important advantages.

Keywords: System design, systems analysis, information systems, prototype, development strategy, project management

## 1. Introduction

An information system, as implemented, represents a synthesis between what the users want, think they want, or state that they want, the designer's appreciation of the users' wants and needs, and the constraints of time, cost, human capability and tech-

![](/api/attachments/KYEP5N4J/fulltext/images/ed0d89b3823d36713a21f4e048db3d1c1c6b9d197b9104f52989e34af19cd238.jpg)  
John Brittan is Head of Management Services at the Military Vehicles and Engineering Establishment at Chertsey, U.K. He has had experience in the design and development of real time systems and MIS.

Laurent Bally is a Technical Manager of SESA-DEUTSCHLAND GmbH, a software and engineering consulting organization. His activities include the design and implementation of large scale real-time information and control systems, in particular for the aerospace industry. Prior to joining SESA, he was with SIEMENS A.G. in the process control division.

![](/api/attachments/KYEP5N4J/fulltext/images/96d3cec92007b7a6d2a4f08d7cd2f7ad1595996ce584fbd7402c3e9565e24708.jpg)

![](/api/attachments/KYEP5N4J/fulltext/images/2b251a4b056233e6e7a24e5dd558bebec9e3d1088ca0e7690514ce59469e571b.jpg)  
Karl H. Wagner is with a research institute for electronics and mathematics (FFM) in Germany near Bonn working on problems concerning the system/user interface of MIS. His main experiences in this area come from the experimental system EMFIS.

nical feasibility. In a large project, all these factors are likely to change as development proceeds so that this process of synthesis is very complex. The lack of a mechanism for ensuring that this synthesis leads to an acceptable solution is a possible recipe for disaster, as witness the many failures of information systems in the sixties. This lesson has been learned and nearly all organisations have sets of procedures for information systems analysis, design and development which attempt to provide a framework for taking a project from initial conception to successful implementation and operation. This paper suggests that most procedures are based on one particular development strategy, points out that alternative strategies are possible and discusses one such alternative in some detail.

Most procedures regard an information systems project as a set of activities which are carried out serially. A typical project “life cycle” is as follows:

1. Initial conception

2. Study(ies) of the problem

3. Establishment of requirements

4. Detailed investigation and analysis

5. Design

6. Implementation

7. Testing and trials

8. Acceptance

9. Operation and maintenance

10. Post implementation audit

11. Modification

The terms used to describe the different stages and the degree of emphasis placed on each vary from organisation to organisation; for example, stage 2 can be described by such terms as initial study, preliminary study or feasibility study, or it may be broken into two steps called the initial survey and feasibility study. Decision points are usually included so that effort, conclusions, and recommendations can be justified to management and approval sought to proceed to the next stage.

## 2. The linear strategy

The serial definition of the project life cycle embodies one fundamental concept: that one activity follows logically from its predecessor, so that each stage is complete before the next begins. Some allowance is however, often made for “looping back”

when detailed investigation and analysis reveal problems or when questions indicate that a change in requirement may be necessary. But any extensive looping is regarded as both unusual and unsatisfactory; it implies deficiencies in earlier work.

An important feature of the linear strategy is that it must be possible to take all important decisions at the appropriate time in the life cycle. In particular, it must be possible to establish a comparatively firm and "solid" system requirement during stage 3; significant modifications during later stages (although they frequently occur in practice) are contrary to the spirit of this strategy and must be very tightly controlled. Although provision for modification after implementation is normally allowed, such modifications are required to be minor so that no fundamental redesign is necessary. Thus the linear strategy places great reliance on the studies of the early stages of the life cycle.

## 2.1. Shortcomings of the linear strategy

When the organisation responsible for designing and implementing the system has experience of similar systems, and when the users have a “feel” for what they want, the linear strategy works well, but when these conditions are not fulfilled, success is much more patchy. All too often, a project starts on the linear strategy but the initial requirement is vague, over ambitious, or fails to meet the real need: the requirement is still fluid. The project then proceeds in a series of short term loops as the requirement solidifies:

— Analysis is started on the basis of the requirement, which then changes, requiring further analysis.

\- Part of the system is then designed to the new requirement, which changes again.

\- Further analysis and design is required.

\- When implementation starts, a feature of the new design is found to be impracticable; it is changed.

\- Before the project is complete, the requirement is changed again, causing a loop back to design
- and so on.

## 3. The loopy linear strategy

We shall call the method of proceeding in a series of somewhat haphazard and short term loops, the loopy linear strategy. Some loops are inevitable in any difficult project but too many will be disastrous. One of the symptoms of excessive loopiness is a feeling of antipathy between the different groups associated with the project, particularly if they are geographically dispersed; the system designers will grumble about users never knowing what they want and users will be annoyed by the apparent lack of good project management as the system overruns its budget in both time and cost.

Excessive loopiness is usually caused by frequent changes of user requirement or by design inadequacies revealed at implementation or later stages. These are the effect of shortcomings in the studies and design stages for in the linear strategy, these can only be based on investigations, calculations, estimations, simulation or experience of similar systems. Unfortunately, most end users who ultimately determine the degree of system success are not usually adept at such conjecture and extrapolation, especially when they have no experience in the potential use of computers or automated information systems. They can, of course, describe the operation of the existing system (if there is one), but to ask them to extrapolate too far beyond their experience is dangerous. Once a user can get to grips with the new system, the comments, criticisms, and suggestions come in thick and fast. Yet the truly linear strategy, by definition, cannot allow for valuable user feedback. New user requirements and minor modifications can usually be put into effect subsequently, but major modifications or fundamental r-design pose serious problems for the linear strategy.

Two other approaches, which have been called the "plug-in" and "prototype" strategies, do not suffer from the same shortcomings as the linear strategy, although they have other disadvantages.

## 4. The plug-in strategy

In the plug-in strategy, the project life cycle proceeds in the same fashion as the linear strategy up to and including stage 4, but then a broad design framework is established, after which different individual sub-systems are designed in detail and implemented in sequence.

Suppose that, for example, an organisation has a requirement for a management information system which is to produce information to support four different functions, A, B, C and D. Using the plug-in strategy the development of this system might proceed as follows. Study, investigation and analysis would define the boundaries of the system and its inputs and outputs in sufficient detail to enable the information flow to be designed in broad terms and the data and file structure to be designed in more detail. The various elements making up function A – input and output formats, procedures and so on – would then be designed in detail. Function A would then be taken through all the steps in the project life cycle up to and including acceptance by the user and live operation before starting on the detailed design and implementation of function B for which a similar procedure would be carried out, with C and D following on in sequence after B. This contrasts with the conventional linear strategy in which work on all four functions would proceed in parallel during stages 5 to 8 of the project life cycle.

It can be argued that the plug-in strategy is a very common practice in system development and is nothing more than a different way of implementing the linear strategy and should not therefore be given a separate strategy designation. The advantage of identifying 'plug in' separately is that it emphasises that there is a choice to be made early in the project about the sequencing of the later stages of the life cycle which will have a considerable effect on how and when the different parts of the system are presented to the users.

## 5. The prototype strategy

In the prototype strategy, an initial and usually highly simplified prototype version of the system is designed, implemented, tested and brought into operation. Based on the experience gained in the operation of the first prototype, a revised requirement is established, and a second prototype designed and implemented. The cycle is repeated as often as is necessary to achieve a satisfactory operational system, bearing in mind the possibly escalating cost of each subsequent cycle; it may well be that only one prototype is necessary before producing the final system.

## 5.1. An example of the prototype strategy

Our example concerns a small scale workshops planning system in which one of the authors was involved. A survey showed that none of the available planning and production control systems would be suitable since all were too complicated for the job in hand. Thus a system would have to be developed to meet the requirement, seen initially as simply recording information on the various jobs as they were presented to the shops. The information included items like title, job number, estimates of requirement for resources of different types (pattern shop, foundry, etc.) and priority. There would also be a requirement to sort the information in various ways (such as jobs in priority order and predicted load on various types of resource). Eventually some limited scheduling might be attempted using the system.

The staff in the workshops had no experience in using this type of automated system, so that although the management were fairly sure of current needs, they could not say what they might want in the future. The only programming effort available was one student gaining industrial experience during one six-month period. It was decided to use the prototype strategy with the first prototype essentially a punched-card system (i.e., extremely simple). Cards representing job transactions were input to a file using the standard facilities of the operating system, and the resulting file (with information on all the jobs) was listed weekly on the line printer in the computer room about one-half mile from the workshops. This system required no computer programming and was implemented within one month of the statement of requirements.

This first prototype was valuable in familiarizing the workshops staff in interacting with a computer. The second prototype involved the development of sorting facilities so that more valuable management information could be produced.

The success and cost effectiveness of this very simple system has now convinced management that they should take the further step of purchasing a terminal which will be located in the workshops planning area but linked to our remote computer for further development of the system. Job data will be keyed in directly, thereby eliminating transcription to special forms for transmission by messenger to the Computer

Centre and key punching. Experiments with a limited degree of job scheduling are also under way.

It is important to note that each step in this simple development sequence was taken in response to a clearly perceived demand based on practical experience gained in the previous step.

## 6. Comparison of plug-in and prototype strategies

There are wide variations possible in the plug-in and prototype strategies. Despite this the two are fundamentally different; it is essential to the plug-in strategy that each sub-system be part of the final system, and therefore compatible with the basic design framework, while in the prototype strategy, prototypes are regarded as test vehicles built to gain information about the final system. Possibly the final system will have features of one or more of the prototype systems, but the basic philosophy is pragmatic and experimental; the aim of the early prototypes is to learn, to find out, to discover. It may well be that circumstances, previous experience or other knowledge will enable the project management to define the "unknowns" in a particular project as belonging to certain areas and to confine the learning element in the strategy to these areas. It may be possible to standardise on a specific hardware range and on a particular documentation system and programming language, but shackles and constraints that are attached to the prototype strategy (particularly if these are built in to a standard procedure), must inevitably detract from the heuristic nature of this strategy.

The different project life cycles under the four strategies are summarised in figure 1. Notes: 1. The confused set of arrows in the loopy linear column represents a haphazard and unplanned series of advances and loops back to previous stages. 2. The linear, plug-in and prototype columns are idealised; some unplanned looping back is almost inevitable whatever strategy adopted.

## 7. Advantages and disadvantages of the prototype strategy

As has already been stated, a major advantage of the prototype strategy is that it is designed to cope with a fluid situation. We have all been involved with the fuzzy type of requirement such as: "I have a management problem: I don't seem to be getting the right information, or if I get the right information it is too late. I am sure your computer could help me. Go away and produce a scheme for getting my information on to the computer."

![](/api/attachments/KYEP5N4J/fulltext/images/bb641221581bd0e5e381fc95276824d9fd0caafa71f5d0fa68373b9a74145a12.jpg)  
Fig. 1. Four development strategies.

In order to use the linear strategy for system development, the analyst would refine this requirement in increasing detail by investigations and studies involving the originator, various subordinate levels of management, and a host of other agencies or relevant activities. Frequently such investigations throw up problems which were not suspected at the outset; for example, the organisation may not be clearly defined or it does not behave in the way that it is defined on paper. Under these circumstances analysts can spend weeks, months and even years probing all these highways and byeways of the existing system before they can design the "final" system.

With the prototype strategy, these investigations and studies are far less protracted. In devising the system, the analysts can often base their detailed interpretations on their own assumptions. The users, for their part, knowing that these assumptions can be proved or disproved when the prototype is put into operation, can be far bolder about accepting them than when faced with a "last chance to make up your mind on the detailed requirement" situation which occurs when using the linear strategy. This shows the greatest advantage of the prototype strategy: the generation of user confidence. Any information processing system must achieve both "technical" and "psychological" success. Technical success is the degree to which the actual performance of the system matches its specifications, while psychological success is the degree to which the end user has confidence in the final system. Of course these components are closely interrelated: technical success is a prerequisite for psychological success, but a psychological failure can negate a technical success. Now the prototype strategy is designed to allow the user to learn about, and gain experience in, the system at an early stage in the project life and allow modification, perhaps radical, to meet the real needs. Thus having tailored the final system to requirements based on actual experience of the prototype(s) the user is far more likely to have confidence in the final product. Automated information system designers tend to underestimate the demands which the linear strategy makes on the inexperienced user. It is rather like asking him to agree to having a new and exotic breakfast food every day, on the basis of paper studies, but without having tasted it. The prototype strategy gives him a change to taste it first.

However, the prototype strategy has a number of disadvantages. The greatest is that it is apparently more expensive – indeed it looks wasteful. It is often only with hindsight that one can see that there was enough uncertainty (either in the requirement or implementation) at the start of the project to justify a prototype strategy. Once can imagine the following diatribe by a manager: "You computer people are all the same; give you an inch and you take a yard. The management agreed to your plan for a computer based management information system, it may even be essential to the company's survival, but now you want us to agree to one or perhaps two prototypes before you build the final version. I know you say that this procedure will not lead to much greater cost, but we all know what happens to that sort of estimate in practice. This Company exists to make a profit, and not to finance bright ideas from your young men in Management Services. Go away and come back with a detailed design proposal for a system that will work first time".

Whatever one may wish, this argument is very difficult to refute. Of course three or four years later, having used a linear strategy, the manager may be singing quite a different tune: "You computer people all have your heads in the clouds. We budgetted for \$70,000 for the development of your system over 18 months. Not only has the system cost \$110,000 and been delivered 9 months late, but no one has a good word to say for it. You should have started with a simple version so that we could all have seen what it was all about, and pulled it to pieces before you inflicted the final system on us".

Of course, for systems where the requirement is well established and their implications are well understood, it will cost more, possibly up to twice as expensive for a single prototype and a final system. Furthermore it is difficult to find the right balance between the aims of keeping the prototype simple and giving it enough resemblance to the final system to enable the correct lessons to be learned by the system developers and users. The “model effect” is well known in engineering development where the effects of size, dimensionality, complexity and lack of inclusion of all possible facets can lead to the wrong conclusions being drawn from a prototype.

## 8. Comparison with other fields of engineering

There is much to be gained from looking at fields other than information processing. The development of information processing systems can be considered a branch of engineering, and the concepts that are well established in engineering are often equally applicable to information system design and development.

Ideas and procedures which seem novel when applied to software (e.g., decomposition into sub-systems and modules, and rigorous quality assurance and testing procedures applied to each) have very close analogy with the development of engineering models, where such procedures are taken for granted. Indeed, in engineering, the prototype strategy is well established. There are of course differences between a large management information system which is probably "one off" and a vehicle or radio set which may have a production run of many thousands, but the basic idea of building something and trying it before going ahead with the final version can be equally applicable to both products.

One important difference concerns terminology. Here we have used the term prototype system to cover a range of complexity between a scaled down version of the ultimate system and something very close to the final system. In more established branches of engineering, a number of terms are used; e.g., bread board model, test vehicle, engineering prototype, production prototype. When the prototype strategy becomes widely accepted in information system development, equivalent terms may well come into use.

## 9. Conclusion

This paper emphasises the fact that there are alternatives to the linear strategy for the development of information processing systems. It suggests that the analyst should understand these alternatives and thus be able to make a balanced and reasoned judgement between them at the start of a project. In particular cases it may be necessary to adopt a combination of strategies rather than a single “pure” strategy. We have emphasised the prototype strategy not because it is better in any general sense but because it is much less widely accepted than the other strategies.

In one sense the prototype strategy is an admission of failure, an admission that there will be circumstances in which, however good our techniques and tools for investigation, analysis and design, we shall not develop the right system at the first attempt. But surely this is only realism based on hard experience, theoretically ideal solutions are often far from satisfactory in a very imperfect world.
