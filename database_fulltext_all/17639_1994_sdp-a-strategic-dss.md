---
otero_id: 17639
otero_key: "QGX27XMR"
title: "SDP: A strategic DSS"
authors: "R.E. Hornby; P.A. Golder; J. Williams"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90064-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# SDP: A strategic DSS

R.E. Hornby and P.A. Golder

Aston University, Birmingham, UK

J. Williams

Morgan Barnett Associates, Otley, UK

This paper examines a strategic planning support tool developed for school managers. It compares the tool with a typical model of the strategic planning process and while concluding that there is strong agreement also finds that the tool which has been validated by use in the field has a contribution to make to the overall model of the strategic planning process.

Keywords: School planning; Strategic management; Strategy support systems; Strategic decision support system

Paul Golder is a lecturer in the Department of Computer Science with research interests in data modelling and decision support.

Robert Hornby is a graduate in Management and Computer Science from Aston University who undertook a period of Industrial training with Morgan Barnett Associates. Rob has interests in DSS and evolutionary systems development.

Jo Williams is the CEO of Morgan Barnett Associates and has a long experience in education as a teacher and inspector and in the training of school managers.
Correspondence to: Paul A Golder, Department of Computer Science, Aston University, Birmingham, B4 7ET, U.K.

## 1. Introduction

All organisations are involved in strategic planning; the setting of a longer term direction of the “business” is central to their sense of purpose and hence to their success [2]. This is evidently true for large corporations where such a planning process is essential to coordinating the direction of managers responsible for different functions. It is perhaps even more relevant to a flatter smaller organisation where the commitment of every professional to its aims and policies is essential for its continued survival. The current trend in devolution of management of many public institutions including schools and hospitals has meant substantial changes in the management of these organisations.

Although budgetary responsibility is one aspect of this devolution which has attracted much attention the activities of day to day operations of an “opting out” school or hospital will be in many ways similar to its counterpart in the commercial sector. The fundamental change in the management of the organisation is that it will acquire the freedom and responsibility to set its own strategic objectives. Not only does the organisation have to set its own objectives but it has to be able to communicate them in a convincing way to its “owners”, in general the Governing Body, which is responsible for managing the unit on behalf of the community and the Ministry responsible for funding the organisation.

Many commercial organisations have a history of strategic planning and an established, if not always explicit, process for developing strategic plans. Recently the planning processes (previously approached in an often informal manner) has taken on a higher profile in institutions such as schools and hospitals, as their planning processes now have to be open to public scrutiny. The need for a systematic approach to this activity has increased during the past ten years, with both the changes in management responsibilities and the plethora of initiatives which have to be taken into account. There is a need for structure in the process of introducing changes successfully, with success incorporating the continued effective functioning of the school and the maintaining of staff confidence and morale during the period of development. This points to a need for some sort of support system to enable the strategic planning process of such organisations.

## 2. Strategy support systems

Over recent years the literature on Decision Support Systems (DSS) has flourished and now incorporates many specialised areas. Although the original proponents of DSSs $[4]$ identified the need to support unstructured problems, most systems discussed still concentrate on supporting decisions which are either unstructured at the operational level of the organisation $[5]$ or relatively structured strategic systems $[6]$ .

The literature on Strategic Decision Support Systems (SDSS) and the more general concept of Strategy Support Systems is large and varies from detailed architectures for SDSSs [1] to arguments for a multidimensional approach to strategic planning [3] and hence to the functionality of SDSSs. There are also examples of actual approaches to SDSS development, some focusing on specific subjects for strategic planning like Information Systems [10], others on particular approaches to the planning process like scenario planning [7]. From the literature there is a general view of the standard stages which should be supported by an SDSS and these are in line with those suggested by Thierauf [9].

Thierauf proposes a system which attempts to prescribe the essential elements of a strategic planning system. He describes strategic planning as “the process of setting or changing organisation objectives as deemed appropriate, obtaining resources to meet these objectives, and determining the strategies, programmes and policies to govern the use and disposition of these resources”. He states that the strategic process involves “the establishing of policies that govern acquisition, use, and disposition of the organisation’s resources so as to achieve stated organisation objectives that change over time” and also stresses that for effective top level planning, information derived from or relating to areas outside the organisation is required. His approach to strategic decision support is summarised in Figure 1.

![](/api/attachments/QGX27XMR/fulltext/images/ce73bd7b3fcf6397ef13ec627b7ae583ef5d06a2481cf435e4b2b199d1512c9e.jpg)  
Fig. 1. A strategic planning model (after Thierauf).

There is now a significant body of research on the subject of strategic level DSS and there are a large number of systems which are proposed, designed or being developed for SDSS. Naturally most of these systems are in-house projects which are too specific or considered to offer a substantial competitive edge to be made available to other organisations, so commercially available SDSSs are rare. Whilst large corporations may be able to justify the investment required to produce an in-house SDSS, the smaller public organisations discussed in the introduction could not. This paper examines a commercial system designed for school managers and considers to what extent it meets the requirements of a general tool to support strategy development. The dual of this analysis is to ask to what extent a pragmatically conceived system, designed to help with the strategic planning of schools, acts as a validation of the models proposed for the design of Strategy Support Systems.

## 3. The school development planner

The “School Development Planner” (Planner or SDP) produced by Morgan Barnett Associates is designed to assist senior managers in planning the future development of their schools [8]. The Planner was designed by an educational consultant, with some twenty five years of educational experience.

The developers state that “by working through a series of well structured processes, those involved are enabled to develop a clear view of the range of actions which need to be taken and to select priorities for immediate, medium and long term development. Through the planning process, managers and their staff come to feel more in control of the future, and face the challenges of working in education in the 1990’s with greater confidence and with the anticipation of more professional satisfaction”.

The planner has evolved over a period of years. The methodology for the strategic planning process in schools has been developed in a conventional staff training format and tested with a large number of groups of managers who have participated in strategy development courses. Some of these courses involved managers from education and industry working together. This methodology has also been put into practice by managers in schools and has been adapted as a result of feedback.

The software version of the planner has been developed from the training methodology and was initially used as a training tool. This form of application of the methodology owes much to the author's background as a Geography graduate for it draws on systems analysis approaches inherent in work on open physical systems such as drainage basins, slopes and complete ecosystems. The application uses best practice in human-computer interface design to achieve an intuitive interface which assists the planning process. The process embodied in the Planner is both controlled and illustrated by the front screen (Figure 2). It is this structure which will form the basis for the comparison.

## 4. Analysis of the school development planner

As the main stages in the planning process are accessed from the top level screen, the SDP suggests, but does not impose, a particular order of activities. The final generation of the development plan report requires completion of previous stages. However in the normal iterative way such planning proceeds it may be that the earlier stages are completed partially and returned to later as further information becomes available. This comparison will nevertheless follow the recommended sequence of actions.

![](/api/attachments/QGX27XMR/fulltext/images/4646720db1566583569ca61aed7e1b97fb4d758386e820d5914ae3b8168b82db.jpg)  
Fig. 2. Main screen of SDP.

## 4.1. SDP: The school statement

The school statement is designed to support senior managers in producing a concise, understandable and workable statement of their school's overall purpose and objectives. The Planner prompts a staff participation exercise in order to generate sufficient raw material to be sifted and condensed by the managers. When formulated the statement is entered into the Planner and is carried forward to each subsequent stage.

## 4.1.1. Setting organisation objectives

Thierauf suggests that setting organisation objectives is the starting point of the strategic process. He stresses the quantitative aspects of this stage and implies something more extensive than that required by the Planner. Despite this, the essence of the two stages is the same, and they perform the same role within their respective systems. It is also possible that Thierauf has mainly profit making organisations in mind, whose objectives are arguably more easily quantifiable.

## 4.2. SDP: Influencing factors

This is a three stage process starting with an activity to collect background information which is grouped into ‘reviews’, ‘initiatives’, ‘views’ and ‘other’. Once this information is available, a group exercise is triggered to discuss and consolidate it. During the exercise the groups are required to consider the outcome of any reviews (consultancy etc.), national initiatives, school based factors, local initiatives, the views of the governors and other factors considered relevant. The final stage of refinement is to present the information in terms of short, medium and long term issues, thus giving a structure to the time dimension.

## 4.2.1. Organisational policies

According to Thierauf a policy is “a principle or a group of related principles along with any consequent rules of action, that provides for the successful achievement of specific organisation objectives”. These policies, in Thierauf’s view, integrate the organisation’s resources with the organisation’s objectives.

In the Planner the reviews and their associated reports probably contain both formal and informal policy issues. National and local initiatives are essentially externally set policy whilst school based factors are essentially policy set from within. The views of the governors, depending on how much importance they are given, may also equate to informal policy.

It is probably true that the influencing factors stage is broader and more informal in its content than Thierauf's stage. It is also true however that much of the data collected by the Planner's at this stage can be viewed in terms of policy without imposing too unnatural a perspective.

## 4.3. SDP: Audit

This is the most sophisticated part of the Development Planner, allowing a full audit of a wide range of school based resources and thus enabling a comprehensive view of the school's current resource position to be constructed. The audit facilitates extensive reporting with a view to providing a basis for informed decision making. General information about the organisation of the school is also entered during this stage, to provide the system with a workable superstructure within which analysis can take place.

## 4.3.1. Resources to attain objectives

This stage represents one of the closest correlations to the Development Planner: Thierauf sees resources as the ‘starting point for long term strategic decision making’, obviously requiring some kind of ‘audit’ to establish where this starting point lies. Thierauf is necessarily vague about the nature of these resources, although he does break them into broad generic categories such as ‘management’ and ‘people’. The specific nature of the resources audited by the Planner reflects the environment for which it is designed, but the purpose of the stage in every other respect is identical to Thierauf’s.

## 4.4. SDP: Priorities for growth

Having completed as much of the audit as is possible/desirable for the current planning period, the managers are able to establish up to four specific priorities for development. The number is limited to four because experience has shown that if development is focussed into a limited number of areas then there is a greater likelihood of effective coordination, less duplication of effort and smaller danger of development overload for staff. Once these priorities are defined they appear on the main control screen replacing the numbers 1 to 4.

## 4.4.1. Comprehensive strategies

Thierauf describes strategies as the “broad, overall deployment of an organisation’s resources to achieve stated objectives” and believes they provide a general framework for directing senior management thinking and action. Once again it can be clearly seen that there is considerable similarity between these two stages, the latter describing the former in more generic terms.

## 4.5. SDP: Compiling the development plan

The Development Plan Report is the primary output of the Strategic Planning process promoted by the Planner. This report is a structured summary of the preceding stages and serves as a working document for senior managers and advisors. The development plan is usually presented to and approved by the governors before implementation takes place and can be compiled in different ways to meet the divergent needs of the various interested parties. This stage does not compare with one of Thierauf's stages but the significance of the communication process to the success of the strategic planning process suggests that it should be incorporated as a significant level in any SDSS, thus encouraging us to extend the Thierauf model as in Figure 3. This extension is supported by similar features in Zivran's [10] ISSPSS (also a practical SDSS) but whereas he has a rather passive step "9. Produce output: a draft for IS strategic plan", the planner supports a more iterative and focused approach to the different "actors" in the school development process.

## 4.6. SDP: Development processes

Once the plan has been approved the development processes stage enables those responsible for its implementation to organise the practical outworking of the chosen priorities. This process begins with a staff activity designed to provide an initial resource to develop and analyse. Following the group work a series of activities are planned relating to each growth priority which are logged into the Planner for the eventual production of a complete staff schedule. The Planner also allows noting of staff training needs for the achievement of the priorities which can be matched against the available training budget producing a series of costed and scheduled training days.

![](/api/attachments/QGX27XMR/fulltext/images/53ea9ab2c2b898e70a1b3f326b0a24826442e6764b25e0033b333357bda251a2.jpg)  
Fig. 3. The revised strategic planning model.

The Planner also allows a full schedule of meetings to be arranged, under the headings; 'staff', 'parents', 'governors' and 'community', which results in a calender being produced for reference. Finally a communications section is available to plan the release of information to the various interested parties.

## 4.6.1. Specific programmers of action

Thierauf describes these programmes as “a complex of activities, resources to be employed and other necessary elements”. He emphasises the importance of good subprogram planning if the comprehensive strategies are to be implemented. Clearly the development planner offers extensive procedures and exercises for achieving this and ensures that a systematic and comprehensive approach is adopted. These two stages are conceptually identical.

## 4.7. SDP: Evaluation

Although evaluation is an on-going activity at each stage of the development process, there is a more formal stage within the Planner's framework for an overall evaluation. This can be compiled as a part of the development plan report when the priorities have been implemented to provide a permanent record of events and some recorded experience to plough back into the process for future years.

## 4.7.1. Compatibility with organisation objectives

The final stage of Thierauf's model is to assess the previous stages in the light of the original objectives formulated in the first stage. He also stresses the continuous nature of the evaluation but defines a separate stage in a similar way to the Development Planner.

## 5. Superimposing Thierauf's model on the sdp structure

From the preceding discussion it is clear that there is an almost one to one relationship between the stages embodied in the Planner and those of Thierauf's model. There is clearly a difference in the language used to describe each stage, but this stems mainly from the fact that the Planner is an applied system whereas Thierauf is proposing a meta-level system in more generic terms.

As a final illustration of their compatibility it is possible to use Thierauf's terms in the place of those normally found within the Planner (Figure 4). It can be seen that there is no real loss of clarity or change of purpose at each stage when this is done.

## 6. Conclusions

There are several conclusions that we draw from this work. The first is that the Planner is a strategic planning support tool which meets all the requirements outlined by Thierauf and is consistent with the general approach to SDSS on which his work was based. We thus conclude that a denatured version of the package could be of considerable benefit to any small organisation.

As can be seen from the discussion of the Planner, a SDSS, like any Group Decision Support System (GDSS) will involve not only the software and hardware that deliver the system, but also a collection of procedures associated with the planning process (Organizationware). Many of these will be group sessions triggered by output from the planner and “chauffeured” by experienced managers.

Further, in that the Planner has been developed and tested over a period of years by many school managers, it constitutes an experiential validation of the Planner's approach and hence of the Thierauf model for SDSS design. However we also note that the Thierauf model understates the importance of communication of the strategic planning process and the role of a SDSS in enabling this communication, we have thus proposed an extension to the basic Thierauf model which reinforces this aspect of Strategic Decision Support Systems.

![](/api/attachments/QGX27XMR/fulltext/images/69260cd99f9f9696b44297bf9e9d2f95acc7a1bf3e549b50dd43cc5862efecf5.jpg)  
Fig. 4. Thierauf's terms superimposed on the planner.

## References

[1] C.H. Chung, J.R. Lang and Shaw K.N., An approach for Developing Support Systems for Strategic Decision Making in Business, OMEGA 17, Nr 21 (1989) 135–146.

[2] R.F. David, Concepts of Strategic Management: Second Edition, (Merrill Publishing Co. 1989).

[3] P. Fredericks and N. Venkatramen, The rise of Strategy Support Systems, Sloan Management Review Spring 1988, 47–54.

[4] G.A Gorry and M.S. Scott Morton, A framework for

Management Information Systems, Sloan Management Review 1971, 13 Nr 1 (1971) 55–70.

[5] J.B. Kidd and S.P. Prabhu, A Practical Example of a Multi-Attribute Decision Aiding Technique, OMEGA 18 Nr 2 (1990) 139–149.

[6] H. Min, A Model-based Decision Support System for locating Banks, Information and Management 17 (1989) 207–215.

[7] F. Mobasheri, L.H. Orren and F.P. Sioshansi, Scenario Planning at Southern California Edison, INTERFACES 19 Nr 5 (1989) 31–44.

[8] Morgan Barnett Associates, The School Development Planner User Guide. (MBA Associates, Otley, Yorkshire UK. 1991).

[9] R.J. Thierauf, User-Oriented Decision Support Systems: Accent of problem Finding, (Prentice-Hall International. 1988).

[10] M. Zivran, ISSPSS: A decision support system for information systems strategic planning, Information & Management 19 (1990) 354–359.
