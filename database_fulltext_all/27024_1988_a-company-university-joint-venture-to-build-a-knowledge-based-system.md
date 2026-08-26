---
otero_id: 27024
otero_key: "P86WDDFY"
title: "A Company/University Joint Venture to Build a Knowledge-Based System"
authors: "John R. Weitzel; Kenneth R. Andrews"
year: "1988"
journal: "MIS Quarterly"
doi: "10.2307/248799"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Company/University Joint Venture to Build a Knowledge-Based System
Author(s): John R. Weitzel and Kenneth R. Andrews
Source: MIS Quarterly, Vol. 12, No. 1 (Mar., 1988), pp. 23-34
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248799

Accessed: 28/06/2014 08:12

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# A Company/University Joint Venture to Build a Knowledge-Based System

By: John R. Weitzel
Management Science Department

Kenneth R. Andrews
Linguistics Department

University of South Carolina
Columbia, South Carolina 29208

## Abstract

A joint venture between a university-based research institute and a health insurance company to build a knowledge-based system to perform medical review of health insurance claims is described. In an early formal test, the system made appropriate decisions for approximately 70% of the claims. The remaining claims were referred to human reviewers in accordance with company policy. Forming a joint venture proved to be a reasonable cost alternative to distant and more expensive consultants.

The article examines the impact of the differing cultures of the company and the university on the cohesion in the joint knowledge engineering group. It also examines the current literature on the development cycle for building knowledge-based systems as the framework for analyzing the events in this project, particularly the influence of the claims review task on system design. From another perspective, it examines participant roles in terms of shifts of attention among domain knowledge, knowledge representation, system performance, and the kinds of skills needed to improve the evolving system. The conclusion includes a series of recommendations that may assist other companies and universities setting up similar joint ventures.

Keywords: System development, insurance claims processing, knowledge-based systems

ACM Categories: K.6.1, I.2.1, H.4.2

## Introduction

In September 1985, Blue Cross and Blue Shield (BC/BS) of South Carolina and the Institute of Information Management, Technology, and Policy (IIMTP) in the College of Business Administration at the University of South Carolina formed a joint venture to build a knowledge-based system to perform medical review on Medicare claims. $^{1}$

Managing the knowledge engineering process was complicated by having members from two dissimilar organizations on the same knowledge engineering group. This arrangement affected cohesion within the knowledge engineering group and inter-organizational dynamics. It also influenced the definition of the problem, the design of the system, and its final form.

The venture developed from circumstances similar to those that led Digital Equipment Company and Carnegie-Mellon University to start the development of an expert system to configure computer systems (McDermott, 1984); someone in the company was aware of the university's work in developing knowledge-based systems. At a meeting of the advisory committee, a professor in the Department of Management Science made a presentation on the university's work to date in building knowledge-based systems and on their potential to solve significant business problems. This presentation caught the attention of a senior vice president of BC/BS who was a member of IIMTP's advisory committee. He believed that an expert system approach could provide BC/BS with a competitive advantage.

He had a number of strategic and operational reasons to improve the processing of Medicare claims. First, in 1984 Medicare claims comprised 41% of the company's total volume and 48% of the total value of benefits paid (Blue Cross, 1984). BC/BS anticipated substantial growth in the volume of health care claims under this program. Second, the federal Health Care Financing Administration (HCFA) was beginning to place increased emphasis on prepayment review of claims. Third, although the company relied on computation to produce economies of scale in processing, the labor-intensive manual review of these claims had not yielded to attempts at automation. Hiring and training sufficient reviewers to capture a competitive advantage would have significantly increased personnel and supervisory costs. Fourth, certain characteristics of the review process seemed suited to a knowledge-based approach. The process was subjective and partly judgmental (Harmon and David, 1985). Registered nurses with clinical experience gained knowledge of detailed review policies and procedures through a long on-the-job apprenticeship. The most experienced reviewers were significantly faster and made fewer errors than the least experienced reviewers.

BC/BS management decided to search for a way to learn about knowledge-based systems. After considering several choices (see Table 1), they decided to strengthen the company's ties with IIMTP and to use faculty members' experience in building experimental knowledge-based systems as a foundation for building a commercial system.

By engaging IIMTP solely as an external consultant, BC/BS would not have increased its skills in developing knowledge-based systems. Because BC/BS and IIMTP both wanted to develop a permanent source of internal expertise, they created a knowledge engineering team by taking existing personnel from both organizations and providing them with training in knowledge engineering methodology and programming. This team consisted of two members of BC/BS's data processing staff, two faculty members and one doctoral candidate from the Department of Management Science, a staff member from IIMTP, and a master's candidate from the Department of Computer Science. $^{2}$

IIMTP participants were responsible for project management during the project's first two contractual phases, which lasted approximately ten months. During this time, the knowledge engineering group reached a technical solution to the problem. In the third contractual phase, which lasted seven months, the project changed from exploratory research and development to recoding the knowledge-based system in a procedural language for operation with the company's other production systems. Consequently, during the third phase of the project BC/BS participants assumed responsibility for project management.

## The Development Cycle in Building Knowledge-Based Systems

There are several descriptions of the development cycle. Various authors call the stages by different names and emphasize slightly different activities in each stage. Most versions describe similar activities in essentially the same sequence, and suggest a single underlying model containing five stages: identification, conceptualization, formalization, implementation and validation.

The first stage identifies a domain, a problem within that domain, and a task (Bobrow, et al., 1986 and Buchanan, et al., 1983). “Task” refers to the role that an automated system will play in relation to the humans whose expertise it will emulate and the level of expertise it should exhibit (McDermott, 1984). This stage requires identifying available resources to undertake a knowledge-based approach: an articulate expert whose time can be devoted to the project, knowledge engineers, and suitable knowledge engineering tools. It also requires the identification of a user, test cases, and acceptable solutions (Bobrow, et al., 1986). Finally, the system developers should identify a performance objective and an estimate of the economic benefits and costs to attain them (Harmon and King, 1985).

The second stage is conceptualization (Bobrow, et al., 1986, and Buchanan, et al., 1983). The knowledge engineers begin to observe the expert's problem solving approach. They and the expert often organize working sessions around actual cases (Harmon and King, 1985, and Bobrow, et al., 1986). The expert describes the approach in solving the case, and the knowledge engineers identify key facts and relationships.

The third stage, formalization (Buchanan, et al., 1983), shifts the primary focus of attention from discovering the expert's problem solving approach to identifying an appropriate representation of the knowledge.

The fourth stage is implementation (Buchanan, et al., 1983). In this stage the knowledge engineers build a prototype. They should select an “implementation technology” from among existing expert system shells. These shells have built-in programming features which accommodate quick changes to the evolving system. The knowledge engineers attempt to get the prototype to run “correctly” from start to finish. The

Table 1. Organizational Choices to Build a Knowledge System

<table><tr><td>Source</td><td>Option</td><td>Advantages</td><td>Disadvantages</td></tr><tr><td rowspan="3">Internal Development</td><td>MIS professionals</td><td>Available source of talentSystems analysis experience is transferableKnowledge of integration into existing DP systems (if mainframe support necessary)Desire to learn</td><td>Lack of familiarity with AI or knowledge engineering processes or tools</td></tr><tr><td>Existing users</td><td>Available source of talent</td><td>Lack of knowledge of data processingUnfamiliarity with AI or knowledge engineering processes or tools</td></tr><tr><td>New hire of AI professional</td><td>Current knowledge of AI, its tools and potential applications</td><td>High demand and low supply creates asking salaries in the $50K-75K rangeAssumes continuing demand for services</td></tr><tr><td rowspan="2">Development by Outside Consultants</td><td>Private sector</td><td>Short term commitment possible</td><td>No local sourceDistance would have raised costs considerablyMost real applications require extended development time; extremely short supply; costs would have been excessive</td></tr><tr><td>Academic sector (national reputations)</td><td>Short term commitment possible</td><td>Far awayLimited availabilityExcessive cost</td></tr><tr><td rowspan="3">Joint Ventures</td><td>Company-to-company research</td><td>Long range development</td><td>Company not oriented toward research and developmentCompetitor companies also unfamiliar with AIPotential difficulties in sharing proprietary knowledgePotential conflicts of interestPotential complications with federal regulators</td></tr><tr><td>Investing in an AI start-up company</td><td>Commitment to company</td><td>Exceedingly riskyExceedingly expensiveLong-range potential uncertain</td></tr><tr><td>Company-to-local-university joint venture</td><td>Local availability; more reasonable costExperience in building small knowledge systems for instructional and demonstration purposesDesire more experience</td><td>Few faculty in the field</td></tr></table>

expert observes and comments on inadequacies and oversights, and the knowledge engineers make improvements to the system. Problems discovered during this process frequently lead the knowledge engineers and the expert to start over. The case-driven “test and refine” process and informal testing continue throughout the development cycle. The prototype often convinces the expert of the validity of a knowledge-based approach (Harmon and King, 1985).

Like decision support systems, knowledge-based systems must evolve (Keen, 1986). The design process must prevent blockage of evolution because of inflexible design structures or development tools. Therefore, attention may shift from domain knowledge to a way to find or develop better tools, then shift back to domain knowledge (Smith, 1984).

Smith (1984) suggests that the purpose of the implementation stage is to demonstrate the system's commercial viability and utility. This stage should also begin the transfer of “ownership” of the knowledge-based system from its builders to its intended users, who need to begin learning how to monitor, maintain, and enhance it (Harmon and King, 1985). By the end of this stage, the knowledge engineers should have a better understanding of the design characteristics of the system, including rules, procedures, and constraints (Bobrow, et al., 1986).

A more thorough test and validation of system performance is required in the fifth stage, validation (Buchanan, et al., 1983). Although validation occurs when implementation is considered complete, problems found during validation often force reformalization and reimplementation (Bobrow, et al., 1986). The prototype may be reimplemented several more times, followed by more validation. Previously overlooked circumstances lead to the incremental expansion of the number of rules in the knowledge base.

There are two main performance criteria to be used during testing. First, the system should function well in comparison to human performance of the same task. Second, the system should perform a commercially viable task efficiently enough to show economic justification. Initial expectations of system performance are generally too high, and a lengthy apprenticeship should be anticipated before the system will begin to achieve the desired levels of functional and economic performance (Bachant and McDermott, 1984).

Initially, organizations usually concentrate on the system's performance instead of its integration into existing systems and work processes (McDermott, 1981). It is crucial that the organization develop an implementation plan that will fit the system into the established organizational structure with as little disruption as possible. Furthermore, a group must be established in the existing organization to continue monitoring and expanding the system's capabilities (Harmon and King, 1985). The final system may be recoded in procedural language as an embedded kernel in a larger system (Smith, 1984; Harmon and King, 1985). Since procedural languages limit the flexibility of the system, some organizations make and validate changes to the knowledge base in the original knowledge engineering tool, and then recode the changes in procedural language.

## Evolution of the Project: Developmental Stages

McDermott (1984) views the nature of the organizational task selected for implementation as a knowledge-based system as the motivating force behind the development cycle. Smith (1984) suggests that the development cycle is a function of the power of the knowledge engineering tool to represent the task. Elements of both viewpoints can be seen in the joint venture between BC/BS and IIMTP. The task of the medical reviewer and the kind and level of knowledge desired in the knowledge-based system largely determined system design. The focus shifted periodically from the task, the tool, and the system design.

Changes in task definition, the design of the system, the integration of database and graphic interfaces with the knowledge engineering tool, and the need for different skills at different times created a shifting pattern of influence in the joint knowledge engineering group. In addition, the chances of continuing the joint venture rose and fell with the knowledge engineering group's progress in problem solving and its likelihood of success.

Managing risk was important to the continued existence of the joint venture. Three separate contracts permitted BC/BS to make incremental commitments to the development effort. If the first or second phase had failed, BC/BS could have limited its losses by terminating the joint venture. The next three sections describe the three phases of the joint venture.

## Phase I: requirements analysis

Organizations usually expect information system departments to deliver completed, working systems on schedule and within budget. Quite often systems are late and over budget, but they usually work after initial start-up problems are resolved. In contrast, there is no guarantee that an AI approach will produce a system at all. Senior management decided to define the project as “research and development,” and they assured the managers assigned to monitor the project that a failure to deliver a working system would not affect annual performance reviews or bonuses.

## Objectives

The first contract funded an exploratory study of the viability of a knowledge engineering approach to review medical reimbursements. Members of the knowledge engineering group interviewed several members of BC/BS management to learn their expectations for the proposed system. With that background, the knowledge engineering team met periodically with BC/BS's top claim reviewer, who served as the domain expert throughout the project. This reviewer became an integral part of the knowledge engineering team.

In early meetings with the reviewer, the group decided to concentrate on the relatively straightforward issue of assessing a patient's eligibility for health care services. This task became the focus of the first phase of the joint venture. The team members believed that if they could first build a small prototype to solve this issue, then they had a chance to create a system that would address the entire review process. The group evaluated the features of the eligibility issue and the suitability of three commercial knowledge-based system tools. The team selected a package by the end of the first phase. At various times, three BC/BS employees and two university participants attended training sessions provided by the vendor.

## System Design and Problem Solving Approaches

The initial design assumption was that the knowledge-based system would advise experienced reviewers on difficult claims and would tutor inexperienced reviewers. This assumption implied that the system would query the user for information found on the bill and on supporting documentation.

The knowledge engineering team based its discussions on actual claims. $^{3}$ The reviewer selected a variety of claims ranging from simple to complex. The team saved these claims to test the evolving prototype.

The knowledge engineers were overwhelmed with details during these meetings with the reviewer. When the team asked the reviewer to explain the claim decisions, they received long, detailed justifications. The explanations became difficult for the reviewer and the knowledge engineers because the reviewer had not previously scrutinized the claim reviewing process, which had become automatic, making it difficult to explain — a phenomenon noted by Johnson (1983).

After several false starts, the team members eventually drew an “and/or” tree which they reduced to an if-then formalism (Hayes-Roth, 1985). The team first wrote the if-then rules in English, and then coded them in the knowledge engineering tool. The interactive prototype followed the sequence of events that the reviewer used in examining medical claims and their supporting records. She based her decisions on a generalized expectation for any patient with a particular diagnosis and on the specific information found on this patient’s claim and medical records.

## Intra-Group Dynamics and Project Leadership

The university participants saw the project as a way to gain experience in developing an actual commercial knowledge-based system. They had major research and development goals (Keen, 1986), such as studying the effect of a knowledge-based system on organizational structure and behavior, studying the kind of knowledge used to review claims, developing a knowledge engineering methodology (Weitzel and Kerschberg, 1986), designing the information system requirements, and publishing research findings. BC/BS also intended to gain experience, but its goals were more utilitarian: improved productivity, improved quality and consistency of review, the possibility of marketing the completed knowledge-based system to other BC/BS plans and health care providers, and the addition of value to the company's existing distribution networks (Kerschberg, 1985).

These different orientations surfaced in several ways. The BC/BS team members continued to believe that a failure to produce a working system would have a negative impact on their performance evaluations. They pressed to assign target dates, pushed for tangible results, and adopted tactics to reduce uncertainty and risk.

They also appeared to feel a need to take charge, so that the group would meet its targets and produce a result.

On the other hand, some of the IIMTP team were more interested in applying various theoretical constructs to a real problem. As academicians, they chafed at attempts to manage their activities. They were subject to an entirely different set of pressures, including their concern to produce a working system for BC/BS and to publish worthwhile research findings for the academic community. BC/BS team members' discomfort increased whenever the university participants addressed research issues that did not seem to be directly related to producing concrete results on schedule. Tension resulted on both sides, culminating in arguments about how the project should proceed and what the system design should look like.

## Inter-Organizational Relations

The importance of an initial prototype to maintain the expert's interest and to focus on relevant issues is well documented (Smith, 1984). Partially as a result of working with the prototype, the reviewer became a proponent of a knowledge-based approach and was the system's most enthusiastic spokesperson. Having a "champion" or a sponsor (McDermott, 1981) was a crucial element in convincing BC/BS to continue funding the project beyond the exploratory stage, especially in light of the tension between the corporate and academic cultures.

Presented with a working pilot prototype and an enthusiastic champion, BC/BS's management decided to fund the second phase of the joint venture. BC/BS and IIMTP made some changes in their working relationship to lessen the difficulties encountered during the first phase. These changes are discussed below.

## Phase II: building a prototype

## Objectives

The primary purpose of the second phase of the joint venture was to build a prototype system that addressed the entire review process, of which eligibility was only a part. A successful prototype would demonstrate the feasibility of creating a production version of the system.

## System Design and Problem Solving Approaches

Even though the eligibility issue had been solved, the remainder of the problem seemed much more difficult. The remaining part of the problem was to determine if health care services were medically necessary. Medical necessity involved assessing the patient's diagnoses, surgical procedures, the length of time since they occurred, and the severity of the patient's condition.

Initially the knowledge engineering group assumed that the problem required diagnostic knowledge. The knowledge engineering group was concerned that the system would need to reason about the underlying physiological mechanisms of the body and a patient's subsequent recovery.

In hindsight, describing the problem in terms of monitoring certain indicators on the claims and medical records is more appropriate. The system flags claims for subsequent human review if these indicators fall outside a specified range (Clancey). The reviewer used the recency of the patients' diagnoses and the severity of their condition to determine the propriety of the kind and level of health care services. Such systems, as Brown (1984) describes, “encode experiential knowledge, or empirical associations, that an expert has accumulated after seeing many similar situations . . . This kind of knowledge underlies the handling of typical cases or standard problems.” (p. 85)

If this knowledge had been represented using an if-then formalism, the knowledge base would have been huge. For example, to represent 500 diagnoses and surgical procedures and the expected levels for weekly services for 100 weeks for six types of health care services would have required 300,000 production rules (500 × 100 × 6). Instead, a way to represent this knowledge was devised using a series of arrays. This insight was the first of two breakthroughs that simplified system design.

These arrays could have been put into the rule-base, but even a small number of them slowed system performance considerably. The team discussed what should be done. One viewpoint suggested that building the prototype first was more important than performance considerations. Another viewpoint suggested that if the prototype performed too slowly during demonstrations, BC/BS's management would not consider a production system feasible.

The second viewpoint won out. The arrays were placed in a database separate from the rule base. One of the BC/BS participants devised a graphic-interface that an expert could use directly to build arrays without the assistance of a knowledge engineer. Rule-based templates were used to extract the appropriate ranges of indicators from the arrays in the database and check the claim against them.

The eligibility prototype had been interactive, and up to this point so had the extended prototype. It became obvious that while a complete system in consultative mode might be a useful tutor for inexperienced reviewers, it would seriously degrade the productivity of more experienced reviewers.

Furthermore, the arrays were based on an average patient with a particular diagnosis. The reviewer used textual information on the medical forms to determine how the individual patient deviated from the average. Although some members of the knowledge engineering team were interested in trying to have the computer interpret the free-form text, the prevailing opinion was that such an approach was too difficult and too risky.

The system design changed from an exclusively consultative mode to a combination of batch processing and consultation. One would continue to read text to determine if the patient were better or worse than the average profile in the database and override the system's recommendation if necessary. Such a design might have produced some gain in productivity, but expecting human reviewers to wait at terminals to be queried by the automated system seemed unreasonable. Besides, the reviewers would need to read most of the form before coming to a decision, and they could make decisions faster without the system. This approach was not satisfactory.

The second breakthrough took place at this time. The reviewer was troubled by the use of an average profile. She felt that she needed an indicator of the severity of the patient's condition that could be used to assess the patient's potential for recovery. For example, severity of a heart attack affects the length and type of treatment.

The team discovered a single indicator on the forms that could be used as a proxy to classify the patient's recuperative potential. This was an item-labeled prognosis, which consisted of five small boxes labeled from “poor” to “excellent.” This indicator became a substitute for most of the reviewer’s earlier, more elaborate verbal deliberations. It eliminated the need to read text and permitted a completely automated system without human intervention. This change eliminated the interactive mode. Rapid prototyping and interactive testing made it easy to rethink the problem and redesign the system.

## Intra-Group Dynamics and Project Leadership

Changes were made in the team's working relationships at the end of Phase I to alleviate some of the tensions between the academic and the corporate cultures. To reinforce the project as a research and development project, two participants from BC/BS moved into offices at IIMTP. Their relocation removed them from day-to-day pressure at BC/BS.

In keeping with the university's mode of operation, the knowledge engineering group was organized as a collection of peers to encourage diverse opinions and individual initiative. However, some problems arose from this arrangement. Neither the BC/BS participants nor the IIMTP participants had formal control over the other group. Since BC/BS was funding the project, its participants felt they should play a relatively greater leadership role. IIMTP's credibility was at stake because it said it could build a prototype. For this reason and because the faculty participants had more experience in building knowledge-based systems, IIMTP also wanted to play a greater leadership role. Differing amounts of time spent working on the project also caused problems. The team members from BC/BS and the IIMTP staff member were assigned full time to the project, whereas the faculty members and the graduate students participated on a part-time basis.

## Inter-Organizational Relations

The team completed a fully operational prototype before the end of the project's second phase. As a result of this and in spite of the tensions inside the team, relations between BC/BS and IIMTP were at their highest. BC/BS's senior executives were delighted that the gamble on a research and development project had succeeded. They perceived the knowledge-based system experiment as a success, largely as a result of the university's participation.

Phase III: integration into operations

## Objectives

This phase's objective was to recode the knowledge-based system in procedural language to achieve suitable run-time performance. Even though the core problem had been solved, the knowledge-based system lacked a completed database.

Most of these issues were straightforward, and they could have been accomplished without IIMTP. On the other hand, some factors indicated the need for IIMTP's continued involvement. IIMTP felt obligated to see the project through to the end. Both IIMTP and some managers at BC/BS were concerned that removing BC/BS participants from the university would result in their assignment to routine tasks in the company, leaving the knowledge-based system incomplete and unintegrated into production. The system required volume testing and a rigorous analysis of its results compared to those of human reviewers. IIMTP's participation was needed to design the test and to analyze and certify the results. BC/BS and IIMTP continued the joint venture in a third and final contractual phase.

## System Redesign

Redesign considerations were based on a batch mode approach in which paper forms (the patients' bills and supporting documentation) would be put into electronic form at company headquarters, screened by a parameter-screening module, and passed to the production version of the knowledge-based system. The knowledge-based system would review the claims, assemble justification for its recommendation, and send a result indicator ("pay" or "suspend") and the justification to the main claims system.

Because denied claims almost always result in appeals and additional costs to BC/BS, there was no incentive to be very strict. The system was designed to make a “pay” decision not only on clear-cut but also on borderline situations. Medical service providers never appeal an over-payment, and HCFA only questions clear-cut abuses. Therefore, minimal risk was incurred by acting on “pay” decisions without human intervention. In contrast, human reviewers would examine suspended claims, first, in case additional documentation was needed either to pay or deny, and second, because erroneous denials created extra costs.

The bias toward paying was used to increase efficiency. The knowledge-based system was redesigned to halt review of the claim when sufficient data had been collected to conclude that total services billed were authorized for reimbursement. In this situation there was no need to further analyze the claim. On the other hand, if not all services were authorized it was necessary to have a human reviewer look at the reason for partial nonpayment.

## Intra-Group Dynamics and Project Leadership

The first two phases had been oriented toward research and development. This third phase, implementation, was quite different in nature. The BC/BS team members assumed a greater leadership role, while IIMTP participants assumed the role of protecting the integrity of the system design.

## Inter-Organizational Relations

During this period, BC/BS was developing another major automated system, which in part would serve as the mechanism to pass data to the knowledge-based system. This second project was a higher priority, and it consumed large amounts of the company's resources and management attention. The team concentrated on recoding the knowledge-based system so that it would be available to go into production in conjunction with this other system. Neither BC/BS nor the knowledge engineering team had time to plan how to integrate the knowledge base into BC/BS's daily operations. Furthermore, resources were not available to create a framework to monitor and develop the system over time or to transfer its problem-solving structure to analogous claims monitoring areas.

To populate the database, the knowledge engineering group adopted a strategy similar to the one used by the Digital Equipment/Carnegie-Mellon development team on their computer configuration expert system. That development team decided to wait until a component showed up on an order before adding it to the parts database (Bachant and McDermott, 1984). The claims review knowledge-based system produced a report of missing diagnoses that needed to be added to the database. Unfortunately, with few resources to devote to testing, few diagnoses were added to the database during the early stages of testing.

In an early formal test, the knowledge-based system reviewed a set of claims used by HCFA for quality control testing. The system arrived at appropriate decisions for approximately 70% of the claims without further human review. Most of the remainder needed to be reviewed by a human because the database was incomplete. (Although the system designers anticipated that 5-10% of all claims would require human review because of expected suspensions and circumstances not accommodated by the system, almost all the suspensions in this test resulted from diagnoses missing from the database.) Therefore, as BC/BS prepared to implement IIMTP's plan for final system validation and installation a delay occurred while more diagnoses were added to the database.

## Conclusion

## Risk management

Although BC/BS of South Carolina funded the joint venture with the IIMTP in its entirety, its successful outcome should not obscure the very real risk of the undertaking. There was no guarantee that any result would be forthcoming. BC/BS reduced its risk by creating opportunities to stop the joint venture at the end of each phase if the problem proved insoluble within a reasonable expenditure of time and money. The joint venture's initial objectives were modest. The costs were justifiable in relation to projected benefits. Risk diminished as the problem unraveled.

## Problem-solving approach

A refrain that occurs over and over in the current literature on building commercial knowledge-based systems is to select a problem and a design that can be solved using available technology. During this project, the knowledge engineering team discussed processing natural language and modeling the patient's diagnoses and recuperative potential. Little is known about solving problems using these approaches. From the very first, the expert reviewer explained how decisions were made in “if-then” terms, a clue that the problem involved surface knowledge. By deciding to stay within the limitations of the available technology, an approach that found relevant indicators in the medical records, a common pattern to their use, and a constrained representation schema was discovered.

## The knowledge engineering group

Some of the desirable qualities for a knowledge engineer include analytical abilities, an ability to develop rapport with an expert (Harmon and King, 1985), curiosity, unconventional educational backgrounds (Taylor, 1985), and conventional programming skills (Smith, 1984). Unconventional educational backgrounds often include individuals with an education in the core areas of artificial intelligence, computer science, linguistics, philosophy, and psychology. Harmon and King (1985) also recommend considering instructional designers (who modernize, design, and impart knowledge), technical writers (who identify “objects,” “attributes,” and “values” and prepare technical specifications), and managers (who sort out complex organizational policies in writing) as candidates for the development team. Finally, the prospective knowledge engineers should be provided with training knowledge engineering methodology and programming from an experienced source. The knowledge engineering group for this project had backgrounds in computer science, linguistics, and psychology, and they received training in knowledge engineering methodology and programming from the vendor of the expert system shell.

## Project management

This project had three distinct objectives, which had varying degrees of explicitness in delineating responsibility and determining performance measures.

The first objective was learning. It was not explicit who should learn what. For example, the faculty members who had actively participated in the design of the prototype during Phase I reduced their level of activity in Phase II to allow other members of the group more opportunity to become actively involved. Some members did not take advantage of this opportunity. Since this objective was not clearly stated, there was no way to correct this situation.

The second objective was to learn the knowledge engineering approach. This aspect of the project involved both knowledge engineering and technical support. The faculty members had greater experience in knowledge engineering. The BC/BS participants had greater experience in using microcomputers. As a result, technical leadership shifted back and forth, but not always at the appropriate times. A more explicit delineation of responsibility would have eased this problem — at the expense of the learning objective.

The third objective was administrative. IIMTP was clearly responsible for administrative details at the university. BC/BS participants were responsible for handling administrative details such as arranging interviews with BC/BS employees. Administrative leadership was divided.

There was no simple solution to these problems. A balance was needed among learning, technical leadership, and administration. Organizations entering into a similar joint venture need to staff it with people who are flexible and have a high tolerance for ambiguity.

## Inter-organizational relationships

Companies and universities are very different organizations. These differences were apparent in inter-organizational relations and in the dynamics of our joint knowledge engineering group.

A senior vice president at BC/BS was disappointed with the organizational dynamics. Friction occurred from differences between the two organizational cultures and between individuals. BC/BS chose its most “academic” people to participate, all of whom had received vendor training in developing knowledge-based systems, but this did not contribute to as smooth of a working relationship as was expected. In part, this friction arose, because each group felt the other side was not giving enough credit for what the group knew of knowledge-based systems.

A certain level of cultural tension should be expected and tolerated. Nonetheless, at various times, different perspectives and skills contributed to better task definition, design suggestions, and technical solutions.

## Middle ground for AI applications

A senior vice president at BC/BS commented that when the project took academic ideas and people and put them together with production-oriented people, a “gray area” was discovered that is ripe for exploitation. This is an area between leading-edge artificial intelligence and everyday data processing. Many applications that are “not sophisticated enough” for artificial intelligence researchers offer promising opportunities for organizations that depend upon information systems.

## The development cycle and implementation planning

Careful attention needs to be paid to the role that the knowledge system will play in the organization, designing it to complement existing work processes, and making its future users accustomed to the benefits it will provide them in their daily jobs. Their early involvement will speed the implementation process.

Although the results of a single case study cannot be taken as universal truth, they do provide indicators of where other companies in similar situations may look for problems and opportunities. In retrospect, it seems useful to assess how this joint venture fared in relation to the other options that were available to Blue Cross and Blue Shield of South Carolina.

Developing internal expertise overcame a tight job market for AI skills. The few candidates available in the marketplace were more expensive than the company was willing to pay. Similarly, consultants with extensive background in AI were far away and too expensive. Considering these factors, the company's decision to train existing employees as knowledge engineers is a solution that many organizations are likely to follow.

The joint venture created a partnership. IIMTP was willing to risk its reputation to demonstrate it could provide leadership in an exploratory study of knowledge-based systems. BC/BS, in turn, was willing to risk funding for the venture. Both risks paid off, and comments from involved managers at BC/BS indicated that they viewed university participation as a major factor in the successful outcome.

The joint venture had an adherent whose support and enthusiasm convinced corporate management that success was possible. As noted earlier, the demonstration of feasibility (Smith, 1984) is largely intended to convince the expert that a knowledge-based approach can help solve significant problems. The experience gained in the project is consistent with this insight. The reviewer initially told BC/BS's top management that she did not believe that automating the review of these health care claims was possible. Her change of opinion during the exploratory phase was a persuasive argument to continue funding for the second contractual phase.

The joint venture has given BC/BS a new awareness that problems they could not solve with automation five years ago now may yield to artificial intelligence techniques. As a result, BC/BS needs to re-evaluate many other systems besides Medicare.

These experiences between BC/BS and IIMTP suggest that joint ventures between business or government organizations and universities may be a viable way to develop knowledge-based systems. The organizations engaging in such a venture should limit their risks by proceeding with a series of small projects, which can be terminated if they are not working out. A productive relationship can result, even if the two cultures do not blend easily.

## References

Bachant, J. and McDermott, J. "R1 Revisited: Four Years in the Trenches," AI Magazine, 5:3, Fall 1984, pp. 21-32.

Blue Cross and Blue Shield of South Carolina and Companion Corporation. Annual Report, Columbia, SC, 1984.

Bobrow, D.G., Mittal, S., and Stefik, M.J. “Expert Systems: Perils and Promises,” Communications of the ACM, 29:9, September 1986, pp. 880-894.

Brown, J.S. “The Low Road, the Middle Road, and the High Road,” in The AI Business: The Commercial Uses of Artificial Intelligence, P.H. Winston and K.A. Prendergast (eds.), The MIT Press, Cambridge, MA, 1984, pp. 81-90.

Buchanan, B.G., Barstow, D., Bechtal, R., Bennett, J., Clancey, W., Kulikowski, C., Mitchell, T., and Waterman, D.A. “Constructing an Expert System,” in Building Expert Systems, F.

Hayes-Roth, D.A. Waterman, and D.B. Lenat (eds.), Addison-Wesley Publishing Company, Inc., Reading, MA, 1983, pp. 127-167.

Clancey, W.J. “Heuristic Classification,” Stanford Knowledge Systems Laboratory, Department of Computer Science, Stanford University, Palo Alto, CA (undated).

Harmon, P. and King, D. Expert Systems: Artificial Intelligence in Business, John Wiley & Sons, New York, NY, 1985.

Hayes-Roth, F. “Rule-Based Systems,” Communications of the ACM, 28:9, September 1985, pp. 921-932.

Johnson, P.E. "What Kind of Expert Should a System Be?" The Journal of Medicine and Philosophy, 8:1, February 1983, pp. 77-97.

Keen, P.G.W. “Decision Support Systems: A Research Perspective,” in The Rise of Managerial Computing: The Best of the Center for Information Systems Research, J.F. Rockart and C.V. Bullen (eds.), Dow Jones-Irwin, Homewood, IL, 1986, pp. 25-48.

Kerschberg, L. "A Proposal for the Development of an Expert System for Medical Claims Processing: MEDCLAIM," Institute of Information Management, Technology, and Policy, College of Business Administration, University of South Carolina, Columbia, SC, July 1985.

McDermott, J. "R1: The Formative Years," AI Magazine, 2:2, Summer 1981, pp. 21-29.

McDermott, J. "Building Expert Systems," in Artificial Intelligence Applications for Business, Reitman (ed.), Ablex Publishing Corporation, Norwood, NJ, 1984, pp. 11-22.

Smith, R.G. "On the Development of Commercial Expert Systems," AI Magazine, 5:3, Fall 1984, pp. 61-73.

Taylor, E.C. “Developing a Knowledge Engineering Capability in the TRW Defense Systems Group,” Al Magazine, 7:2, Summer 1985, pp. 58-63.

Weitzel, J.R. and Kerschberg, L. “Developing Knowledge-Based Systems: Reorganizing the System Development Life Cycle,” working paper, University of South Carolina, Columbia, SC, and George Mason University, Fairfax, VA, December 1986.

## About the Authors

John R. Weitzel is Assistant Professor of Management Science in the College of Business Administration at the University of South Carolina, Columbia. He has a Ph.D. in Management from the University of Cincinnati. Dr. Weitzel spent 13 years as a programmer, systems analyst, and project manager for computer-based information systems, primarily in the banking industry. His research interests include the strategic use of information systems, implementation of information systems, and applications of artificial intelligence to management information systems and decision support systems.

Kenneth R. Andrews was, until recently, a Senior Research Associate with the Institute of Information Management, Technology, and Policy in the College of Business Administration at the University of South Carolina, Columbia. While with the Institute, he was involved in strategic planning for information resources for several major state agencies in South Carolina and in the development of a knowledge-based system for Blue Cross and Blue Shield of South Carolina. Prior experience included budgetary, financial, and program analysis in banking and local government administration. He holds graduate degrees in Public Administration (from the University of North Carolina, Chapel Hill) and Slavic Linguistics (University of Illinois). He is currently pursuing a Ph.D. in Linguistics at the University of South Carolina.
