---
otero_id: 21147
otero_key: "NUMFMV9A"
title: "Evolutionary development and research on Internet-based collaborative writing tools and processes to enhance eWriting in an eGovernment setting"
authors: "Paul Benjamin Lowry; Conan C. Albrecht; Jay F. Nunamaker; James D. Lee"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00119-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evolutionary development and research on Internet-based collaborative writing tools and processes to enhance eWriting in an eGovernment setting

Paul Benjamin Lowry \*, Conan C. Albrecht, Jay F. Nunamaker Jr., James D. Lee

## Abstract

The Center for the Management of Information (CMI) at the University of Arizona has been actively involved in research with various U.S. government organizations for nearly 20 years. This article details the years of evolutionary development and research conducted by CMI in an eGovernment setting that resulted in the creation of an Internet-based collaborative writing ((eWriting) tool, called Collaboratus. By embracing persistence, serendipity, and years of multi-methodological research in the field and in the lab, CMI has built on the foundation of eWriting research that was largely abandoned at the beginning of the eBusiness revolution. This research shows the promising potential for Collaboratus and eWriting tools to help improve digital government through improved document production and collaboration, and highlights many future research opportunities. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Collaborative writing; Group writing; eWriting; eGovernment; eGov; Digital government; GSS; Collaboration; Group work; Facilitation; Distributed work; Self-sustaining writing teams; Multi-methodological research; Collaborative systems development

## 1. Introduction

This article explains how researchers at the Center for the Management of Information (CMI) based at the University of Arizona, along with researchers at Brigham Young University have developed improved collaborative writing (CW) processes and technologies for eGovernment by using a multi-methodological research approach, called the Systems Development Methodology (SDM) [34]. Several years ago, researchers at CMI foresaw the value that could be provided by introducing CW tools in the government sector: CW is an arduous task in government settings and is often poorly executed and excessively costly, and has received sparse research attention. When CMI started its CW research, no commercial tools existed that adequately addressed the needs of large, distributed CW teams that produce government documents, and virtually nothing had been published on the topic. Furthermore, little was known regarding appropriate processes for government-related CW tasks. Thus, we have spent several years addressing CW opportunities from a both a process and technology perspective. We term the combination of processes and technologies for distributed groups working over the Internet ‘‘eWriting’’. Before discussing our application of the SDM to eWriting for eGovernment, this section introduces our view of eGovernment and the important role that CW plays in that domain.

## 1.1. A revolutionary view of eGovernment

Some researchers see eGovernment as a simple extension of eCommerce; however, we see it as a potential collaborative revolution among government stakeholders that is distinct from general eCommerce. We agree that

The Internet revolution that has created an explosion of eBusiness, eCommerce, and all the other ‘‘e’’ initiatives has equally transformed government. Truly, it can be said, ‘‘Government too cannot escape the relentless force of the Internet. Electronic government, or e-gov, will permanently alter the relationship between government and citizen, reshaping both the day-today operations of the government and the political processes that form it. E-gov will change not only the means of communicating with government but also the frequency and quality of those communications. [40]

The revolution of eGovernment is also internal—as manifested by attempts to diminish bureaucracy and more rapidly produce better decisions. How will eGovernment make this transformation? By using the Internet and related technologies to transform the government, both in its internal processes and external processes through its service provision to the public and to suppliers.

While eGovernment shares many attributes with eCommerce, such as the potential for greater efficiencies and cost savings, several aspects of eGovernment are unique [40]: (1) The nature and content of services provided is different; (2) Supply chains and providers cannot be rapidly replaced as seamlessly as in private industry; (3) The government must serve 100% of its citizens regardless of where they are located and how ‘‘profitable’’ they are; (4) eGovernment lies in the public, not-for-profit sector, which involves a myriad of political stakeholders and bureaucrats operating with different agendas. We believe this final point is where Internet-based CW can make a big difference in the eGovernment domain, by re-engineering and improving internal writing processes, and better involving key stakeholders in these processes.

## 1.2. The importance of CW in eGovernment

CW is the act of producing a document with two or more people; as such, CW just may be the most ubiquitous act performed within government. Of course, government is not alone in its insatiable need to produce collaboratively written documents—CW is prevalently used throughout the business and education sectors [4,6,12,14,15,37].

Despite similarities between government and private sectors in CW usage, the process of CW in government sectors has stark differences including that it: (1) Involves longer, more complex documents because of increased regulations and oversight; (2) Requires a much greater number of participants and stakeholders, especially in terms of buy-in and authorization; (3) because of points 1 and 2, CW in eGovernment can have potentially stronger personal and political ramifications than in other settings.

Despite the ubiquity of CW, it is a form of group work that is often difficult, inefficient, unsatisfying, and performed sub-optimally [14]. Thus, given these potential issues, why is CW so heavily utilized in government? One explanation is the potential process and content gains associated with teamwork [34]. These potential gains may even be more pronounced in the government sector. Many writing tasks conducted by government entities require discourse and complex convergence of multiple viewpoints through consensus; thus, one person cannot possibly have all the expertise needed in such an environment. As such, it is not uncommon for hundreds of participants to be involved in the creation of government documents. For example, the U.S. Army Training and Document Command (TRADOC) produces many training documents that require input from hundreds of participants.

## 1.3. Article overview

The remainder of this article discusses the evolution of our research on enhanced CW processes and Internet-based technologies for eGovernment. The next section introduces Nunamaker’s SDM [34], which was used as the framework to guide the building of four generations of CW tools and to perform related, process research. The evolutionary development of these CW tools is then described, along with specific process and technology lessons learned. Finally, this article overviews promising future research opportunities in eWriting in eGovernment.

## 2. Using the Software Development Methodology (SDM) for CW research

This section describes how the SDM was used as the framework to guide CMI’s eWriting research. First, an overview of SDM is presented, along with its unique methodological contribution. Next, we then describe how the application of SDM to other group research led us to inquire into the research domain of CW for eGovernment.

## 2.1. Overview of SDM

For years, MIS as a field suffered from an identity crisis that centered on debates involving relevance versus rigor, diversity of methodologies, and poor use of reference disciplines [7,21,35,38]. In partial response to these debates, Nunamaker et al. [31] developed a powerful research framework, called the Software Development Methodology (SDM), for producing both relevant and rigorous MIS research (see Fig. 1). This multi-methodological framework embraces ‘‘grounded theory’’ that is built by observation (e.g. field research, surveys, case studies), experimentation (e.g. controlled laboratory experiments, simulation, field-based, quasi-experiments), and systems development (e.g. prototyping, product development, and technology transfer). This methodology is iterative, allowing methodologies, theories, and research technologies to grow incrementally over time in conjunction with real-world problems of real clients [34]. It is the real-world nature of the problems with which we work that makes theory built using SDM ‘‘grounded’’ in reality.

2.2. The beginnings of CW tool and process research at CMI

Reflecting our embrace of SDM, CMI’s research in CW tools for eGovernment was an evolutionary process that started with research in group support systems (GSS), including many related theories and technologies. These many years of previous experience using SDM to advance GSS and knowledge management research (e.g. Refs. [30,32,34]) are what guided us to eWriting. In fact, we first conducted CW research as an extension of GSS research that was being conducted for a government client: Because of our successful application of GSS technologies and processes to government domains, a federal government agency asked us to conduct action research through field sessions using GSS technologies and processes to improve their CW outcomes. This initial CW experience provided insight on how group-oriented tools for CW had substantial potential value for government. In particular, a synchronous CW session using GroupSystemsk<sup>1</sup> p roduced the following results (GroupSystemsk is a popular a GSS produced by GroupSystems.com that contains collaborative tools that help facilitate meetings with integrated tools supporting processes such as discussions, brainstorming, outlining, voting, and agenda creation; as explained in Ref. [33]):

![](/api/attachments/NUMFMV9A/fulltext/images/e68155220cbe1eb85e05af84e5ac705590dd886cd101ed032b4580c03110c406.jpg)  
Fig. 1. Revised research and development Methodology, from Nunamaker et al. [34].

A. . . federal government agency team was updating a 150-page regulation document and assigned the project to a technical writer who had traveled the country interviewing appropriate team members for input. After the interviews, the writer authored a draft and sent it out for comment. Several team members disagreed with key sections of the draft and specialists in Washington, DC., overseeing the process, had the writer insert text with which team members strongly disagreed. Eight months into the project, the team met face to face for a one-day meeting but were unable to resolve the disputes over sections of the document. Another draft was attempted but received little support from team members. . ..One year into the arduous process, fourteen key members of the team were brought into a synchronous GSS CW session. Cliques had formed among team members with shared interests. There was scarcely any trust of the Washington specialists. Using a GSS, this team produced a penultimate document in three and a half days. After the session, the team estimated that in a facilitated process without collaborative technology they would have required about ten days of work to create the document, but, in reality, the three and a half days can be measured against the 365 days previously spent. [34]

Similar experiences throughout CMI and with our industry partner, GroupSystems.com, led to the development of a DOS-based CW tool, called GroupWriter for DOS. This tool was the start of four generations of CW tools that have been built from this body of research.

## 3. Four generations of CW tools

This section describes the evolutionary development of four generations of CW tools produced at CMI using SDM. These tools are described with the salient research that was conducted during each generation, along with the key lessons learned. The four generations of eWriting tools that are discussed include: GroupWriter for DOS, Group-Writer for Windowsk, Java GroupWriter, and Collaboratus.

## 3.1. Generation 1: GroupWriter for DOS

GroupWriter for DOS was primarily a prototype tool built on the notion that an automated, grouporiented CW tool would provide enhanced benefits over traditional tools (i.e. using Microsoft Wordk with email). GroupWriter for DOS was one of many tools that was released in the GroupSystems V TM toolset from GroupSystems.com, CMI’s industry partner. Development of this tool evolved over several years, in conjunction with CMI’s research in GSS, collaboration, and eBusiness, and with CMI’s many research projects for government agencies.

GroupWriter for DOS was an important achievement; however, the biggest problem with this DOSbased group application was developing an interface that could effectively promote group awareness and communication, and that could seamlessly integrate with outside applications. Unfortunately, initial user experiences revealed the limitations of GroupWriter’s operating environment in that it did not properly support group awareness and coordination.

This experience led to our first two lessons in eWriting:

Lesson 1. A full understanding of system requirements cannot occur until a system is prototyped and then validated by field tests.

Lesson 2. CW tools need interfaces that promote group awareness, and underlying operating systems that can support these features.

The communication and usability problems we experienced were never adequately addressed because of the limitations of the DOS operating system. As such, group awareness remained a key requirement that was never fully addressed until the common adoption of the Windowsk operating system. This led to our final lesson from this experience: when requirements cannot be adequately addressed by current technology, researchers must decide whether to wait for enhanced technologies, or to examine more leading-edge technologies that may fill the need. We decided to risk waiting it out, as operating systems development was not our area of strongest expertise.

Lesson 3. A strong present need not fulfilled in current technologies will likely be addressed by future technologies.

## 3.2. Generation 2: GroupWriter for Windows TM

When GroupSystems for Windowsk was released, GroupWriter was not included as one of the tools. Because there was a strong need for the functionality of a Windows-based CW tool, CMI decided to create a new version of GroupWriter to take advantage of a GUI-based platform that could help improve the DOS-based interface issues.

True to SDM [31], the development of Group-Writer was an evolutionary process that involved active field research, experiments, and theory building, using Generation 1 as a foundation. Our initial target for action and field research was the Department of Defense (DoD), because of the potential improvement in CW tasks that could be gained and because we had performed several years of research with Defense Environmental Security Corporate Information Management (DESCIM). Our underlying premise was that by using GroupWriter for Windowsk, DoD regulations and documentation could be written with more efficiency, quality, and stakeholder participation.

## 3.2.1. Requirements gathering and prototyping

We based our initial development requirements on a review of data involving hundreds of facilitated sessions with DoD agencies, of which more than a dozen sessions involved CW. Additionally, initial requirements and prototypes were reviewed with a varied array of DoD managers on eight separate occasions. We then prototyped a Windows-based CW tool to meet the DoD’s specific requirements. For example, we learned about the specific kinds of documents and processes produced by the DoD that would most benefit from GroupWriter, which included military regulation documents, military handbooks, manuals, pamphlets, support documentation, and systems analysis specifications. Additionally, this experience provided insight into which interaction parameters were relevant, such as the applicable approval process, the likely stakeholders that needed to be involved, and the typical size of their CW teams. By thoroughly understanding the context of the DoD work and the requirements of the participants, we felt we could develop a tool that could help the DoD to produce more effectively its regulations and documentation, with more stakeholder participation.

Lesson 4. Developing grounded theory requires iterative experience with specific, client-oriented problems that are researched in detail.

Lesson 5. Effective requirements development requires fieldwork and the collection of work artifacts.

## 3.2.2. Key features of GroupWriter for Windows TM

Based on our gathered requirements, we designed a new, Windows-based CW tool that greatly improved on the DOS version [1]. The design included graphical annotations, since field research showed the prevalence and importance of the review process. Annotations identified the participants that created the annotations and provided an open dialogue for annotation-based discussions. We also provided version control and visually identified textual changes that could be accepted, rejected, or merged with the document text as part of the approval and convergence processes. True to the related GroupSystemsk software initially developed at CMI, GroupWriter provided extensive facilitator controls to enable a facilitator to focus the efforts of the participants throughout the CW process. The team leader was able to control the set of buttons and menu items that were available to encourage participants to focus on the particular writing activity being conducted (e.g. outlining, drafting, reviewing, revising). This also included the ability to set up rights for different participants. This was particularly crucial during the review process because the DoD needed the ability for many stakeholders to be able to have read-only access and/or the ability to create annotations during a review, but not be able to modify a document’s text.

A couple of additional features were added into GroupWriter to better address the need for group awareness as learned in Lesson 1. First, GroupWriter for Windowsk included outline-building functionality to support the generation of a group outline, which allowed group members to have an enhanced, overall view of a group document and to better participate in the creation of its structure (see Fig. 2). To improve coordination and communication, GroupWriter was integrated as an additional tool available to Group-Systemsk. Thus, the combination of these tools allowed facilitators to structure CW processes where the actual discussion of document content was handled through GroupSystemsk discussion tools. The discussion content could then be seamlessly imported into GroupWriter for further CW work.

## 3.2.3. Field-testing of requirements

One of the early issues in GroupWriter for Windowsk development was to what extent the product should support full-featured word processing. Stakeholders within the DoD generally agreed that Group-Writer needed basic features such as cut, copy, and paste; however, opinions greatly diverged on whether more advanced features should have been supported, such as styles, grammar checking, and advanced formatting. This conflict centered on trying to balance the primary purpose of the tool, which was to facilitate rapid production of group documents, versus adding more flexibility editing features found in advanced word processors (i.e. Word and WordPerfect). One of the issues with including such features is that they are often expensive to implement (in development time and resources), and are often only sporadically used. Again, field results from actual group writing sessions provided an appropriate solution.

![](/api/attachments/NUMFMV9A/fulltext/images/e716f6c7ab7ba224543d017e54244573203584683a34d5d79b4b85512343137d.jpg)  
Fig. 2. Early screen shot of GroupWriter Table of Contents view.

Lesson 6. When doubt exists about a requirement that is difficult to prototype, researchers should find an alternative implementation of the requirement and test it in the field with actual users.

Our field studies showed that the most significant benefits of GroupWriter were gained through the initial brainstorming, drafting, and review of a CW document; especially when large numbers of stakeholders were involved, and when communication, convergence, and buy-in were crucial. We observed that when groups conducted CW with traditional word processors, their focus was diverted from their primary task of drafting their document as a team, because they tended to worry about font sizes, formatting, and other document minutia when they should have been creating substantive content. Alternatively, when participants used GroupWriter they were much more focused and effective on the drafting activity. We also found that many of the key contributors who developed crucial key document content were rarely interested (or involved) in final formatting and copyediting. In fact, we noted that once the draft of a document was produced, the creation of the final copy of the edited document was often delegated to one person who was not even a team member (e.g. an administrative assistant).

In summary, our field experiences allowed us to conclude that providing advanced editing features in the GroupWriter tool not only would be expensive and time-consuming, but also would likely undermine the purpose of GroupWriter. Because of this, we chose to have GroupWriter support all the major writing stages (group formation, brainstorming, outlining, drafting, reviewing, revising) except for the final copyediting, when the document can be easily exported to a publishing application for final formatting.

Lesson 7. CW tools should not provide advanced word processing features for most group-writing activities.

However, this still was not an easy decision to make, because several inexperienced users automatically expected GroupWriter to be a full-featured word processor. It did not matter that many of them they normally used only 5% (or less) of the functionality of their preferred word processor. We felt this expectation was simply based on what they knew and were used to in word processors, since virtually no users had experiences with CW tools and word processors were their only reference point. Thus, we found in helping users adopt GroupWriter it was useful to explain the rationale of the tool up front, and why it was not a full-featured word processor.

Lesson 8. Derived requirements do not always make sense to end-users, because of their expectations derived from other tool use; thus, for improved tool adoption, it is useful to explain the rationale and design decisions of a tool as part of training.

Lesson 8a. Users do not normally respond well to interface design decisions based solely upon scientific research. Rather, many users require more intuitive reasoning for interface design buy-in.

## 3.2.4. Applying action research in the field

Once the features and requirements of GroupWriter started to mature, we applied GroupWriter to actual problems experienced by government, through action research. The U.S. Army’s Training and Doctrine Command (TRADOC) continually revises and produces hundreds of publications. Often, the process of producing a single publication lasts over an 18-month period that typically involves five or more different drafts. Production of each draft requires different groups to write, revise, edit, and approve sections of the publication. Because the participants are globally dispersed, drafts must be mailed around the world to hundreds of commands, authors, and reviewers who make changes and suggestions. These changes then must be integrated into one coherent document that often requires further buy-in from the hundreds of stakeholders. Given the historical bureaucracy with this document production strategy and the many changes in defense roles and the tightening of budgets, TRADOC had outstripped its ability to efficiently keep up with its vast workload. We used action research to promote specific processes with Group-Writer to help TRADOC dramatically cut its document production cycle time and its costs.

Lesson 9. Action research is an excellent way to both solve highly complex problems and to develop buy in with research clients.

Our action research with GroupWriter at TRADOC involved an intensive CW meeting that lasted three days and involved 14 subject matter experts from the U.S. Army Intelligence Center. The purpose of this meeting was to create a document that detailed the tactics, techniques, and procedures for executing electronic attack (EA) in support of Army operations. The target audience of the document produced by this action research was fire support and military intelligence personnel charged with the planning and execution of EA operations. These full-day sessions were held in an advanced GSS room (see Fig. 3) designed to support such work, and were led by the Doctrine Division, Directorate of Combat Development. The first session laid the groundwork for revising the cornerstone regulation used to govern the production of doctrine in the army. The users quickly mastered GroupWriter and were productive within an hour of starting.

After 1 hour of software training, the CW team worked to create and develop an outline, write section contents, edit sections, and review the publication. To facilitate document production, four small subgroups were formed to produce specific outline sections on deciding, detecting, delivering, and accessing (see Fig. 4). In less than 3 days, these small groups were able to complete the document and essentially perform work that had traditionally taken months for the organization. In addition to providing a dramatically faster CW process, the resultant document was more robust and had increased buy-in because all of the interested parties were represented throughout the process. This experience led to the conclusion that while CW tools can greatly transform government document production, appropriate CW processes need to be followed to fully realize these benefits. Fig. 5 overviews the appropriate process we found for F2F writing in this setting.

![](/api/attachments/NUMFMV9A/fulltext/images/42fa0acb9b9de4e327e802b9b5e25fcbb79971877e69daa4b0fede50ca72e987.jpg)  
Fig. 3. Advanced GSS support room at CMI.

![](/api/attachments/NUMFMV9A/fulltext/images/181c85f1fe8ebca7f28cbec6d7471ba77d5e9a0cd923c981a2e93bf788d95136.jpg)  
Fig. 4. TRADOC document outline for subgroups.

Lesson 10. Following an appropriate process in CW is just as important as using the ‘‘right’’ technology.

## 3.2.5. Field-testing networking technology

In addition to performing action research with GroupWriter, we also conducted a field test of distributed CW with additional military participants to see if GroupWriter would be an effective distributed tool. Using a CITRIXk server, GroupWriter documents were posted to the Internet for distributed review of co-located participants. This addition allowed DoD groups to save weeks in mailing and distribution time and in associated, underlying costs. Additionally, since GroupWriter maintained a single copy of documents, it dramatically enhanced the revision process, because editors no longer had to forcibly create final documents from a mishmash of standing copies; instead, participants worked off the single common version. This allowed reviewers to see each other’s comments and revisions and react to them without waiting for the next draft version.

![](/api/attachments/NUMFMV9A/fulltext/images/a62226fc840e7cf4b7c0b243dfd70505239453d5bac3eccd9e58d741b5665f94.jpg)  
Fig. 5. GroupWriter process.

Lesson 11. Distributed CW on the Internet can produce efficiency and quality gains for government document creation.

## 3.2.6. Additional action research

The next phase of our field project moved Group-Writer out to Army installations where many of the

DoD publications are produced. In the spring of 1999, we worked with the Military Intelligence School at Fort Huachuca, Arizona and the Air Defense Artillery School at Fort Bliss, Texas to produce actual field manuals in a synchronous, distributed environment. The Fort Huachuca group created a new field manual by dividing the participants into subgroups that worked on specific chapters, which were later reviewed by all participants through annotations that were accepted, rejected, and/or merged into the final document. At Fort Bliss, we followed a similar process but revised an existing, extremely large field manual. We imported the existing document from Wordk into GroupWriter and instructed all participants to review the outline of the existing document. Participants then separated into subgroups to review and revise specific chapters and made suggested changes and comments through annotations. Again, in these field experiences, GroupWriter was able to dramatically cut down on the number of days it took to produce these documents.

Lesson 12. Dividing into subgroups improves the outcomes for large groups working on large CW documents.

## 3.2.7. Modeling distributed CW processes

Based on our experiences in the field, and building on previous CW process research [14,34,36], we were able to develop a suggested process model for synchronous, distributed CW for large teams that expanded on our previous F2F research. This improved, general CW process is as follows: First, the team produces or edits an outline for a new or existing document. The writing team quickly steps through the outline and adds basic content as the formation the document. Next, participants work individually, or in small sub-teams, to make parallel additional contributions to the specific sections of the outline. Note that contributors or sub-teams ‘‘lock’’ sections while they work on them; thus, other users can view the sections being worked on but cannot make changes. After making changes, the contributor relinquishes the lock so that another user can make changes to that section. The locking system maintains the integrity of the document while maximizing access for all participants. Additionally, periodic reviews by the group ensure that all efforts remain targeted on the group’s objectives for the document. Finally, a facilitator or group leader leads the group through a final walkthrough of the document to make final revisions.

Lesson 13. Group awareness, coordination, and locking are all the more important in distributed settings where it is easier to become confused.

Our fieldwork provided initial validation that GroupWriter had a sufficient combination of features to help improve government document production, as long as appropriate processes were used. Likewise, complex processes require process facilitation by someone who understands what the ‘‘correct’’ process is; a finding supported by general facilitation literature [19,28]. We also learned that GroupWriter was not a panacea for difficult CW processes, a lesson similar to that learned in CMI’s GSS research [34]. Thus, GroupWriter sessions still needed substantial facilitation support (or leadership) and process structure to be effective. We realized many benefits of using Group-Writer with appropriate processes, compared to traditional CW using F2F meetings, email, and word processors. Some of the benefits we observed are summarized in Table 1.

Lesson 14. Complex CW processes require facilitation support by someone who understands the ‘‘correct’’ process.

## 3.2.8. Scalability issues with GroupWriter

While we discovered several benefits of Group-Writer during these field experiences and were able to formalize appropriate CW processes, we also discovered that GroupWriter was likely inadequate for large, distributed groups, or teams with participants working in more than a couple of locations, because of its client-server architecture. Our experiences at Fort Bliss and Huachuca gave us the strongest insights into limitations of GroupWriter because of the distributed, synchronous work performed. ‘‘Our most poignant technological lesson with GroupWriter was that scalability and performance issues caused it to quickly reached its upper limit on the ability to support large, distributed teams.’’ In fact, this drawback proved to be so significant, it required a complete re-design of GroupWriter and its underlying architectural support (see Generations 3 and 4). This proved to be the unforeseen Achilles Heel of the Windowsk version of GroupWriter.

<table><tr><td>Table 1Benefits of GroupWriter for Windows $^{\text{TM}}$ </td></tr><tr><td>·Faster document production·Inclusion of more participants and content experts·Increased information sharing·More buy-in and convergence of participants·Better process support for lengthy and complex review processes·Support for F2F and synchronous distributed writing·Increased CW process structure·Increased group awareness·Enhanced communication·Greater task focus·Elimination of version control and document merging problems·Support of simultaneous, parallel writing strategies and reciprocal writing·Immediate document access for all participants·Support for various CW roles such as author, reviewer, editor, and facilitator·Compatibility with Microsoft Word·Inclusions of both anonymous and non-anonymous contribution·Low training requirements and rapid learning curves·Inclusion of team members without being as intrusive on their time·Improved ability to “refurbish” and extend the life of existing documents·Increased organizational learning·Higher satisfaction of participants and other stakeholders·Improved document quality</td></tr></table>

The underlying conflict had to do with how we were using CITRIXk in combination with DoD servers. Initial support of distributed, Internet access of GroupWriter was accomplished through a CIT-RIXk server with dial up to the Department of Defense’s Environmental Information Management System (DENIX) website, which made GroupWriter and GroupSystemsk available to various government agencies. However, the use of the CITRIXk server on DENIX to access Windowsk GroupWriter added an additional layer of complication [1]. The configuration of the server had to be modified, and connectivity to a particular session first required access to the CITRIXk server, then GroupSystemsk, and then GroupWriter, which was a process prone to error. CITRIXk (as well as similar screen relay systems) required significant bandwidth due to the amount of graphics being transmitted; thus, low-bandwidth users were significantly less satisfied with the responsiveness and found the overall system unusable for real work.

Lesson 15. Lack of bandwidth is the Achilles heel of synchronous distribution of traditional groupware applications.

Lesson 16. Client-server architectures have signifi cant limitations in their ability to scale and support large, distributed groups.

## 3.3. Generation 3: GroupWriter for Java

While GroupWriter for Windowsk was actively used with government and military groups, its underlying Windows-based architecture limited it to being primarily a LAN-based, face-to-face tool. ‘‘Thus, GroupWriter was severely restricted in its ability to support Internet-based, distributed groups.’’ In addition, many government and military sites would not allow installed applications such as GroupWriter for Windowsk for security reasons. Essentially, we had the right concept and requirements for GroupWriter, but we were still searching for appropriate technologies with which to implement it.

## 3.3.1. Alternative analysis for next generation CW tool

As part of our research, we used alternative analysis, to determine if other viable options existed for CW that would meet the government’s requirements. Our options essentially involved buying an existing CW system, extending an existing application such as Microsoft Wordk, using an existing computer-mediated communication (CMC) tool or GSS, or building a new CW tool from scratch. We found our general requirements for CW tools (summarized in Table 2) to be pivotal in determining which option to choose. Our analysis led us to the conclusion we needed to custom build a CW tool, for three key reasons: (1) We determined that traditional word processing tools, such as Wordk, did not support these requirements. In addition, extending such tools into CW applications was not prudent, since such tools are built on singleuser architectures that are not designed for group awareness, coordination, and scalability [22,24]. (2) While existing GSS and CMC products tended to support group awareness and coordination, they poorly supported CW features, especially in terms of providing simultaneous group editing and group annotations. (3) Finally, no existing CW tool had

Table 2 eWriting tool requirements, adapted from Ref. [22]

Group support tools: <sup>.</sup> Group communication <sup>.</sup> Planning and agenda creation <sup>.</sup> Simultaneous group outlining with locking <sup>.</sup> Voting <sup>.</sup> Categorization <sup>.</sup> Anonymous brainstorming Collaborative writing support: <sup>.</sup> Partitioned, simultaneous parallel writing <sup>.</sup> Annotations pointing to specific pieces of text, supporting different types and symbols <sup>.</sup> Annotations with conversation spaces <sup>.</sup> Simultaneous document access methods such as write, comment, read <sup>.</sup> Different document access methods that correspond to the roles <sup>.</sup> Simultaneous reactive writing support Group awareness and coordination features: <sup>.</sup> Group interface that depicts overall group activity <sup>.</sup> Different rights for different document sections <sup>.</sup> Facilitator controls and support <sup>.</sup> Participant list of all those involved in a session <sup>.</sup> Negotiation support <sup>.</sup> Support of social interactions Technical features: <sup>.</sup> Java/browser support <sup>.</sup> Easy installation/no client-side installation <sup>.</sup> Low-bandwidth communication for distributed teams

been architected and extended for use over the Internet. For example, while several notable CW research tools had been previously created (e.g. GROVE [16], Quilt [5], SASSE [27], Collaborwriter [18], Collaborative Editing System (CES) [3]), none of these tools supported synchronous, parallel writing on the same document over a web browser.

Lesson 17. Alternative analysis of technological implementations is fruitless without well-developed requirements.

## 3.3.2. Prototype of JGW

In response to our alternative analysis, we determined that building a Java-applet-based tool appeared to be the most appropriate technological solution, since Java applets do not require client installations and can be easily designed for efficient data transfer. Thus we built a new tool called Java GroupWriter (JGW).

The key benefit that was envisioned by creating JGW was the ability to truly support distributed eWriting groups, without the need for special server access, proprietary software (e.g. CITRIXk and GroupSystemsk) or arcane installation procedures. A JGW prototype was quickly developed that realized these benefits; however, as described in the next section, we quickly ran into unexpected performance problems with the new prototype.

## 3.3.3. Scalability issues with JGW

Unfortunately, JGW did not live up to expectations because of the complexities involved in developing highly interactive, Internet applications. JGW used a rich client that was downloaded via a web browser and a thin server for collaboration and persistence. However, due to underlying architecture issues, the JGW server was not able to scale and effectively support distributed groups.

The initial performance problem associated with JGW was not native to the tool itself; instead, it was primarily a scalability problem associated with the underlying server that CMI was using. This server had been created several years before for other collaborative, web-based software being developed at CMI. Unfortunately, we soon found that JGW placed more demands on the server than the other Java-based applications that were being developed, because JGW’s focus on group awareness required higher levels of interactivity from the server than could be properly supported. Thus, we chose to move onto yet another generation of CW tools, which we named, Collaboratus. The following summarizes the technical lessons we learned about developing these types of applications in Java [2]:

Lesson 18. Network programming models (such as RMI and CORBA) present complex application programming interfaces (APIs) and new problems not found in local area networks (LAN) environments.

Lesson 19. The Internet is by definition a heterogeneous network of smaller, disparate networks; thus, programmers have little control over the environments within which their applications run.

Lesson 20. Data replication and consistency issues over the Internet can require significant design and programming work.

Lesson 21. Packet and message ordering and timing cannot always be predicted with computers connected over public networks such as the Internet.

Lesson 22. Real-time applications generally require high bandwidth.

Lesson 23. Real-time applications with distributed clients require complex programming to achieve robust and scalable solutions.

## 3.4. Generation 4: Collaboratus

## 3.4.1. Development of Collaboratus

Collaboratus<sup>2</sup> was developed as the next generation of an Internet-based, Java application to support real-time, highly interactive group processes that are conducted over the Internet, including CW and several other forms of related group work such as brainstorming, process modeling, categorizing, and voting. Because of the collaborative framework used to implement Collaboratus, facilitators can mix and match tools and activities according to their needs. One of the primary tools (or activities) that comprises Collaboratus is an improved GroupWriter module. The integrated tools that make up Collaboratus are summarized in Table 3.

As distributed groups rely more upon tool support for group processes, the integration of GroupWriter with other group support tools increased its effectiveness for distributed eWriting. The synergy between these applications provided the basis for full team support of the entire group writing process, including brainstorming, outlining, writing, reviewing, and editing.

Collaboratus was built using a collaborative framework that allowed programmers to quickly develop robust, network-aware user interfaces. This framework provided the basis for a scalable application that supports many different group processes, such as process modeling, document inspections, brainstorming, and team decision support. Thus, the successful completion of the collaborative application framework allowed integration of other Java-based collaborative applications with GroupWriter that were being previously developed separately at CMI. These applications formed a new, Internet-based GSS suite of applications. This was highly appealing to DESCIM, as we were previously building two other collaborative applications for DESCIM that was often performed in conjunction with CW tasks: (1) GroupReview, an application for collaborative code reviews and (2) GroupAnalyzer, an application for collaborative process modeling. Thus, with DESCIM’s support, we extended GroupWriter into a suite of tools that included GroupReview and GroupAnalyzer. Eventually, we also added several other baseline GSS activities such as brainstorming and group discussions. Not only did this integration extend the applicability of the LAN-based GroupWriter to other domains, it also decreased DESCIM’s reliance on GroupSystemsk and CITRIXk.

<table><tr><td>Current Collaboratus tools</td></tr><tr><td>GroupAgenda (for agenda creation and associating tools/activities to a group meeting)</td></tr><tr><td>GroupBrainstormer (for traditional brainstorming)</td></tr><tr><td>GroupCategorizer (for categorizing brainstormed output into “buckets”)</td></tr><tr><td>GroupTopicCommenter (for group discussions on topics)</td></tr><tr><td>GroupOutliner (for creating group outlines)</td></tr><tr><td>GroupReview (for group code reviews)</td></tr><tr><td>GroupAnalyzer (for group process modeling)</td></tr><tr><td>GroupWriter (for group writing)</td></tr></table>

## 3.4.2. Rapid development using a collaborative framework

Having to scrap JGW and start over was not easy, but it was the right decision. In re-architecting our solution, we soon realized that many of CMI’s other distributed, highly interactive applications shared many common behaviors with GroupWriter—such as shared views, data replication, and access control. Thus, we felt an opportunity existed to create a common collaborative framework on which collaborative, Internet-based applications could be built rather than ‘‘reinventing the wheel’’ every time we developed such an application [39]. Thus, we set out to build a new, Internet-based collaborative application development framework with enhanced requirements, as detailed in Table 4.

Development of the new framework was useful as it allowed the rapid development of a new version of GroupWriter, achieving the above-listed goals (see Ref. [39] for more details). The framework was based upon an n-tiered model and utilized messaging systems, collaborative data repositories based upon XML definitions, and model-view-controller interfaces. A high-level overview of the server model is found in Fig. 6.

<table><tr><td>Application development framework requirements, from Ref. [2]</td></tr><tr><td>Facilitation of rapid, iterative collaborative application development.Support of dynamic data structures.Utilizing a thin client framework that can work over low-speed connections.Use of a common client for all applications that provides a standard frame all application panels are placed in.Support of multiple client environments, including applet-based, application-based, and web-browser-based Java environments.Support of user-interface (UI)-driven development so that developers can mostly focus on building UIs—not more complicated server and networking issues.Facilitation of fully, distributed applications accessible from virtually any client computer.Use of a scalable architecture so that code can be written to allow for n-tiered server architectures.Support of a real-time environment so that when one client modifies data on the server, all other clients accessing that same data should immediately see the changes on their screens.Implementation of locking so that multiple users can access the same data at the same time in a robust, consistent way.Delegating all security to the server, so that application clients are not involved.Using an environment that is non-proprietary, portable, and that does not use any third-party code, so that its application can run on a variety of operating systems.Use of highly efficient algorithms to ensure scalability and quick replication (i.e. replication only occurring between clients viewing the same data).Pushing all data control and storage to the server to improve robustness and integrity of data.</td></tr></table>

Lesson 24. Rapid development of collaborative applications requires a collaborative framework.

## 3.4.3. Key features of Collaboratus

The new GroupWriter had several important improvements, not the least of which was tight application integration with the other Collaboratus applications. For example, by using Collaboratus, participants can conduct a brainstorming session using GroupBrainstormer, categorize their brainstormed results using GroupCategorizer, and then transfer the results into a GroupWriter outline. Additionally, the ability to set up user rights and roles was significantly improved to allow support of additional eWriting roles such as researcher and team leader.

The addition of flexible annotations was also a notable improvement. The new annotations allow users to place any number of annotations directly in a document’s text. These annotations are highly flexible so that if an annotator disagrees with an annotation or has questions, he/she can double-click on an annotation and create an on-going dialogue with the original creator of the annotation. Additionally, a customizable set of standard annotation types and underlying graphical shapes can be created to represent different types of comments. Hence, an editor can insert shapes representing different editorial comments throughout a document. Additionally, reporting on the annotation types for statistical purposes is also possible. Finally, we greatly improved group awareness in the CW document creation process by creating an outline view of the document that was better integrated with the text. This outline is displayed to the side of the document’s text, allowing users to quickly navigate through a document and examine what other group members are working on (see Fig. 7).

## 3.4.4. Modeling asynchronous CW processes

Turning from technological considerations to process considerations, we found that asynchronous, distributed CW was a key process in eGovernment, chiefly because the large numbers of stakeholders in government document production often makes it necessary to work at different times and different locations, especially for document reviewing processes.

Furthermore, our initial field research showed that distributed, asynchronous CW processes are fundamentally different from F2F processes and synchronous distributed processes, because of changes in synchronicity and proximity. For example, we found that with our asynchronous DoD groups that it was preferable to have them to meet F2F or in synchronous sessions, where possible, for convergence (or consensus) processes, as a means to improve consensus [1,17]. (This claim is currently being further tested in a large field experiment with 550 participants [22]).

Moreover, the most critical activities that foster convergence and consensus are organizing brainstorming output, planning, and editing the final document draft. For example, session preplanning is even more important than with other types of collaborative work because CW tasks are highly visible and political and can be extremely difficult in government settings. Part of this planning includes ensuring not only the right stakeholders participate, but also they are given appropriate subject matter to review and are personally prepared for the CW sessions. Additionally, participants must be committed to the process, which indirectly suggests that team formation exercises, objective facilitation, and appropriate convergence processes are critical.

![](/api/attachments/NUMFMV9A/fulltext/images/94f25b8e1e50b5fec1c87857032f93f4f4e0d04cc42f6b7e6a678bbc9de180af.jpg)  
Fig. 6. Initial, high-level server model for new architecture, from Ref. [2].

Furthermore, we found that the larger the CW group, the more the group will benefit from effective eWriting technology; likewise, large CW groups that do not use CW technologies will likely experience significantly lengthier and more problematic CW processes. Moreover, relationships and communication are critical aspects of successful CW; yet, these components are significantly challenged by large, distributed teams. We felt that although distributed asynchronous CW teams that use CW tools will not be able to entirely compensate for lack of F2F interaction, similar teams that do not use CW tools will have far more challenges.

In sum, our experiences lead us to believe the following overall process should be used by distributed eWriting teams desiring to do most of their work asynchronously: (1) preplanning and F2F group formation, (2) F2F planning, (3) asynchronous research, (4) asynchronous, anonymous brainstorming, (5) F2F convergence deciding on which brainstormed ideas should be in the paper, (6) asynchronous outlining, (7) asynchronous commenting on initial outlining, (8) asynchronous drafting, (9) asynchronous reviewing, (10) asynchronous revising, (11) F2F group review of the final document (preferably read aloud to the entire group), (12) asynchronous final copy editing by one group member. Steps 6 –10 are iterative and repeated as necessary (see Fig. 8).

![](/api/attachments/NUMFMV9A/fulltext/images/1cf8e7dbeb22c3fe1a53da9728a2d127cb5ae51a56ecf456449cbc3e63e5fb14.jpg)  
Fig. 7. Screen shot of Collaboratus GroupWriter.

Lesson 25. F2F consensus meetings may improve overall CW processes that focus on asynchronous tasks.

## 3.4.5. Collaboratus experiments

We are finally at a point where after years of development and field research that our underlying theories on CW work are gaining strength into a collective framework, and thus, can be more thoroughly tested through laboratory experiments. Our CW research framework (as illustrated in Fig. 9) has matured over time and reflects several key lessons [22].

Lesson 26. Input choices related to a group’s characteristics, the task performed, the tool that is used, and the overall context in which the work is performed heavily influence final CW group outcomes.

Lesson 27. The CW processes that a group chooses to perform (e.g. brainstorming, drafting, outlining, and reviewing) and the quality through which they are followed, also directly affect CW outcomes.

Lesson 28. CW outcomes can be measured in multiple ways [26] and their importance primarily depends on the CW task being performed; however, the primary outcomes that are commonly measured involved quality, satisfaction, and productivity.

Lesson 29. Communication and relationships are important intermediary outcomes in CW that directly affect the quality of the CW processes performed, ultimately affecting the final outcomes. For example, poor communication is likely to undermine convergence on brainstorming. Good relationships are likely to enhance the review and revision processes.

![](/api/attachments/NUMFMV9A/fulltext/images/b3e0652d69b260198d1a6949f389d9c61134380929af8c45ef8d298daf731764.jpg)

![](/api/attachments/NUMFMV9A/fulltext/images/e663260c982dbdb4625392b58ca290ee550ec2ff01319004126d25f01886d17c.jpg)  
Fig. 8. Proposed Asynchronous eWriting process, adapted from Ref. [8].

In examining our research framework, one can quickly conclude that we have years of research left to conduct because of the substantial number of input choices that need to be addressed. We have chosen to start with the input choices we believe have the most significant impact on CW outcomes: technology choices and task choices related to processes. The next two subsections overview laboratory experiments in both of these areas.

Lesson 30. Substantial theory development in new research areas develops only after years of trial and error.

3.4.5.1. Laboratory experiments on CW technologies. Our initial research on Collaboratus indicates that it has the potential to transform government eWriting—especially with large, distributed groups. The bulk of our latest Collaboratus research has involved conducting a series of laboratory experiments involving eWriting in the sector of public education [23]. The purpose of these experiments is not only to substantiate the benefits and refine theory of using Collaboratus for eWriting, but also to better understand eWriting processes, eWriting facilitation, and to improve the usability of Collaboratus. University classroom settings have proven to be excellent test grounds for such experiments because of the ability to naturally integrate CW tasks into existing curriculum. Thus, we have not only been able to have the control of specific behaviors afforded by laboratory experiments, but also the context in which we are conducting these experiments involves realistic academic tasks, where students are graded on the results of their group documents that are produced over several weeks.

![](/api/attachments/NUMFMV9A/fulltext/images/f5e88621bc4aa6d6846cf4bbebdcd7c3da345e6c659c89687b63da6bd01c23b7.jpg)  
Fig. 9. CW research framework, from Ref. [22].

Results of our first laboratory experiment suggested the potential benefit of using Collaboratus for F2F group writing in CW teams compared to groups using Microsoft Wordk [22,25]. We also conducted a laboratory experiment involving distributed, simultaneous document production comparing Word versus Collaboratus groups [8], which also showed the potential superiority of Collaboratus under these conditions. In particular, we found Collaboratus groups producing higher document lengths and quality, having increased communication in chat sessions, experiencing higher satisfaction, and better interpersonal relationships in terms of socialization and positive affiliation [8].

The interpersonal relationship improvements in distributed eWriting with Collaboratus, versus traditional methods, are particularly insightful. Early collaboration research established that the social context for group interaction may have a greater effect on process and outcome than any technical intervention [13]. We believe this is no different for eWriting groups. For example, through observing and coding the synchronous chat logs (all treatments used NetMeetingk for comparative consistency), we found strong differences in the kind, quality, and volume of participation between the groups.

3.4.5.2. Laboratory experiments on CW processes. In addition to technology laboratory experiments, we are conducting research on improving processes for distributed, asynchronous eWriting teams that use Collaboratus [22]. Currently, we are in the process of validating the ideal processes for distributed, asynchronous eWriting in laboratory settings and determining the appropriate level of process structure (or procedural explicitness), so that such groups can ultimately work independently of professional facilitators. This can be accomplished with process scripts, agents, and think-Lets as proposed by Refs. [24,29].

## 3.4.6. Current technical research

In addition to our laboratory research, we are continuing examining ways to improve the underlying architecture of Collaboratus and the group-oriented tool set [22,23]. For example, we are currently in the process of moving the Collaboratus architecture from Enterprise Javabeans (EJB) to a more distributed Jini architecture that was in beta-development when we first developed our framework [39]. This will enhance the scalability and maintainability of Collaboratus applications.

## 3.5. Summary of four generations of CW research

In summary, Section 3 presented the evolutionary research of four generations CW tools, using the SDM. We strongly believe that following the SDM was critical in extracting the lessons we learned, and that a complete picture of eWriting theories and processes for eGovernment can only be gained through successive iterations of requirements gathering, tool development, field observations, process modeling, surveys, usability studies, and experiments. Table 5 summarizes the specific techniques we used in embracing SDM for eWriting research.

Research techniques used in applying SDM to eWriting research

<table><tr><td>(1) Observe</td><td>(2) Experiment</td><td>(3) Develop</td></tr><tr><td>User field observationAction researchTechnical field testingProcess modelingUsability studiesUser surveysField experimentation</td><td>Laboratory experimentation on technologiesLaboratory experimentation on processes</td><td>Requirements gatheringAlternative analysisPrototypingRapid, framework-based developmentUnit testingSystem testing</td></tr></table>

## 4. Conclusion

While some aspects of CW are maturing, increasing distribution of work teams poses new challenges to effective communication and group writing. This section presents potential future CW research and our concluding comments on the value of applying the SDM to eWriting research.

## 4.1. Future research

Future research possibilities with Collaboratus or other eWriting tools in an eGovernment domain are abundant both in the short term and in the long term. In the short term, we are planning on conducting more field experiments and action research involving large, distributed eWriting teams in additional eGovernment settings. Although several researchers have partially examined distributed, asynchronous CW (for example, Refs. [1,10,20]), we believe much more has yet to be learned in this area. We also plan to expand our scope of eWriting research to non-military government entities such as rural community development [8], humanitarian relief efforts, and in international governance. Furthermore, we want to apply our lessons learned with highly complex government CW tasks to complex CW tasks in the private sector that involve many distributed stakeholders, such as requests for proposals, proposals, strategy documents, and systems development documents [24].

We believe a particularly interesting area of opportunity is creating self-sustaining eWriting teams that work in distributed settings. The goal in creating selfsustaining (or auto-facilitating) teams is to wean CW groups off the need of having professional facilitators who know the ‘‘right’’ process through which to lead a group. While complete independence may not be possible for inexperienced groups, we believe that groups can become self-reliant over time using process scripts, wizards, and process agents. This substantial area of exploration is the subject being addressed in Refs. [22].

In addition to more effectively supporting distributed teams, several important technical design considerations need to be examined for inclusion in eWriting tools. These considerations include the integration of multi-media technologies such as multicasts, video conferencing, RealAudiok, and IP telephony. An additional area of exploration would include the utilization of advanced information retrieval, decision agents, visualization, and knowledge management techniques, as addressed in Refs. [9,11]. Since such features could conflict with the general need to support low-bandwidth communications for asynchronous groups, they should only be utilized for synchronous interactions where the appropriate bandwidth is available. As such, eWriting servers could be designed to automatically decide which features should be available to an eWriting group, depending on their connection speed, CPU capabilities, and other important parameters.

Additionally, although replication techniques are generally frowned upon by CW researchers, because of locking and replication conflicts, such techniques may prove to be useful for asynchronous, distributed CW where bandwidth and connection reliability are serious issues. While bandwidth size is generally increasing throughout Internet space, large portion of users will still connect through low-bandwidth pipelines for the foreseeable future. Thus, not all clients can realistically be supported by synchronous applications, which makes replication technologies an interesting area of exploration. Furthermore, it might be useful to develop software that automatically switches to a replicated mode when a server connection is lost. This could be particularly useful for roaming applications such as field-sales contract support, collaborative document production between naval ships, and military field exercise support. Additionally, replication techniques could be useful for supporting the exploding Internet appliance market, including hand-held devices such as Palm Pilots or Pocket PC devicesk

Finally, additional consideration needs to be given to expand the security capabilities of eWriting tools for the eGovernment sector, to include advanced encryption (beyond the current solutions such as triple-DES) and authentication techniques to ensure the right people are viewing the right text. In addition to these research areas, we are examining several design consideration and feature improvements in terms of overall process support, research support, planning, writing, editing, reviewing, roles/identities, and communication support, as summarized in Table 6. These points are further explained in Refs. [23,24].

## 4.2. Concluding comments

Through these several years of eWriting research at CMI, we have gained several key insights—not just about eWriting but about creating relevant MIS research with appropriate research methodologies. For example, we reaffirmed the importance of multimethodological research in MIS and the utility of combining elements of rigor and relevance in creating grounded theories. We certainly could not have achieved these technological and process innovations by merely theorizing or only conducting lab studies. Furthermore, as part of this methodology lesson, we learned that persistence in research pays off when setbacks are encountered, and that dramatic breakthroughs often only materialize as the result of working with real clients in real contexts on real problems. Likewise, we reaffirmed the importance of building a cumulative tradition in a given research area: Rather than abandoning existing research areas when new trends and technologies emerged, we learned to patiently integrate our past work into leading-edge technologies (e.g. distributed, n-tiered, Internet-based architectures). Furthermore, we learned the importance of flexibility in not being overly fixated on one research stream or technology. Clearly, when we started out with our first concepts of CW and the DOS-based GroupWriter tool, we could not fully foresee the advent of GUI interfaces and the explosion of the Internet. Instead, we were able to build a foundation of eWriting research by iteratively building several generations of eWriting tools and conducting applied research.

We believe that eWriting is a promising area of inquiry in collaboration and communication research that not only has application to the DoD, but also to all levels and constituencies of eGovernment. Furthermore, eWriting has excellent promise in the private sector and in education. Today’s paradigm of CW using traditional word processors and ‘‘email passing,’’ executed in a sequential process, is archaic, inefficient, and costly. In the future, we believe that almost all formal group writing can be more effectively conducted on centralized documents, using improved processes and CW-specific technologies that promote greater group awareness and coordination.

Table 6  
Additional eWriting tool design considerations, from Ref. [22]

<table><tr><td>Area</td><td>Design considerations</td></tr><tr><td>Overall process support</td><td>Use of text color and avatars for different participants or groups.Graphical status bars for participants and groups.Graphical snapshot availability to show each participant the changes that were made since he/she logged in.Graphical process modeler that shows overall group and participant activity and milestone process.Wizards and intelligent agents support.Automatic agent support to fire off events and messages as certain deliverables are completed (e.g. form routing and email messages).Ability to switch software support, features, and views according to desired CW strategy (e.g. sequential, parallel, reciprocal) and/or current CW activity being performed (e.g. brainstorming, outlining, reviewing, etc.)Writing templates and wizards for different CW tasks (e.g. strategy documents versus academic journal article) and work modes (e.g. F2F, synchronous distributed, and asynchronous distributed).</td></tr><tr><td>CW Research support</td><td>Document management integration.Indexed information repository for artifacts such as papers, video clips, and recordings.Integration with professional citation managers such as EndNoteTM and ProCiteTM.</td></tr><tr><td>CW Planning</td><td>Negotiation and convergence agents.Project Management (PM) support and integration with PM tools such as Microsoft ProjectTM.Task list creation and integration with external communication tools such as Microsoft OutlookTM.Capturing of internal metrics and external post-project assessment data into a metrics repository for future CW project planning.</td></tr><tr><td>Writing</td><td>Inclusion of context sensitivity to change the writing and editing features available the CW activity groups are engaged in (e.g. advanced Word Processing and grammar checking for final copy editing, and only basic editing for drafting).Allow the facilitator to change the granularity of the locking for the needs of a particular group or task (e.g. word, sentence, paragraph, section, document).Textbases and boilerplates documents to increase the speed of creating document drafts.</td></tr><tr><td>CW editing and review</td><td>Further integration and support of professional editing symbols and standards, as part of the editing and annotation support.Advanced annotation reports and view to allow a facilitator to view all the annotations for specific people, dates, document segments, and annotation types, and to create QBE reports.Include rights to only allow specific reviewers to review certain sections of a document, under given logical dependencies and work flow (e.g. setting up a review to go through a complex, hierarchical chain of command that sends the document to the right people at the right time for approval).Digital signature integration into the review process.Graphical representation of the review process and participants showing what has been completed, and what it left for completion.</td></tr><tr><td>CW roles support</td><td>Include additional roles and security for system administrators, researchers, copy editors, internal stakeholder, and external stakeholder.Ability to support multiple subgroups and teams, with persons belonging from one to many of these.Enhanced facilitator support by using telepointers, support of session lock down, and a mode where participants are able to see everything the facilitator does on his/her machine for instructional purposes.</td></tr><tr><td>Communication support</td><td>XML import and export.Creation of an industry-standard XML protocol for eWriting.Context-sensitive chat support (e.g. simultaneous chat for synchronous session, threaded chat for asynchronous session).Facilitator messaging to individuals and groups.Tight integration with electronic mail systems (e.g. the work flow engine could notify participants when work has been completed and to prompt participants when to start on a particular task).Support of private chat sessions and anonymous chat.White board emulation.Group drawing.Fax server integration.Multilingual support for various character International character sets, languages, and symbols.Automatic translation of text from one language to another for drafts and brainstorming sessions [34] (e.g. designed to be able to switch between standard languages, such as English, Spanish, and Mandarin Chinese).</td></tr></table>

## Acknowledgements

We appreciate contributions made by Mark Adkins, John Kruse, and Queen Esther Booker to this work. We also greatly appreciate the Collaboratus development work conducted by Conan Albrecht, Abhiraj Jadhav, Ankur Jain, and Hemanth Manda. We would also like to acknowledge the support and funding we have received from Defense Environmental Security Corporate Information Management (DESCIM) and Air Force Operational Test and Evaluation Center (AFOTEC).

## References

[1] M. Adkins, J.Q. Reinig, J. Kruse, D. Mittleman, GSS collaboration in document development: using GroupWriter to improve the process, Presented at Proceedings of the 32nd Annual Hawaii International Conference on System Sciences, Hawaii, 1999, pp. 1 – 11.

[2] C.C. Albrecht, A programming framework supporting rapid application development of highly interactive, collaborative applications, Unpublished doctoral dissertation in MIS, University of Arizona, Tucson, 2000, p. 225.

[3] C. Albrecht, Collaborative architectures that support e-business, in: P.B. Lowry, J.O. Cherrington, R.J. Watson (Eds.), The eBusiness Handbook, CRC Press, Boca Raton, FL, 2001, pp. 423–442.

[4] N.J. Allen, D. Atkinson, M. Morgan, T. Moore, C. Snow, What experienced collaborators say about collaborative writing, Journal of Business and Technical Communication 1 (1987) 70– 90.

[5] R.M. Baecker, D. Nastos, I.R. Posner, K.L. Mawby, The user-centered iterative design of collaborative writing software, Presented at ACM Conference on Human factors in Computing Systems, Amsterdam, The Netherlands, 1993, pp. 399–405.

[6] E. Beck, A survey of experiences of collaborative writing, in: M. Sharples (Ed.), Computer Supported Collaborative Writing, Springer Verlag, Berlin, 1993, pp. 87 – 112.

[7] I. Benbasat, R. Weber, Research commentary: rethinking ‘‘diversity’’ in information systems research, Information Systems Research 7 (1996) 389 – 399.

[8] R.O. Briggs, G.J. de Vreede, J.F.J. Nunamaker, D. Tobey, ThinkLets: achieving predictable, repeatable patterns of group

interaction with Group Support Systems (GSS), Presented at 34th Annual Hawaii Conference on Systems Sciences, Maui, HI, 2001, pp. 436 – 444.

[9] H. Chen, A. Houston, J. Yen, J.F. Nunamaker Jr., Toward intelligent meeting agents, IEEE Computer 29 (1996) 62– 70.

[10] H. Chen, Y. Chung, M. Ramsey, C. Yang, An intelligent personal spider (agent) for dynamic Internet/Intranet searching, Decision Support Systems 23 (1998) 41–58.

[11] H. Chen, O. Titkova, R. Orwig, J.F. Nunamaker, Information visualization for collaborative computing, IEEE Computer 31 (1998) 75 – 82.

[12] R.M. Davis, How important is technical writing? A survey of the opinions of successful engineers, Technical Writing Teacher 4 (1977) 83– 88.

[13] A. Easton, G. Easton, M. Flatley, J. Penrose, Supporting group writing with computer software, Bulletin of the Association of Business Communication 53 (1990) 34– 37.

[14] L. Ede, A. Lunsford, Singular Texts/Plural Authors: Perspectives on Collaborative Writing, Southern Illinois Univ. Press, Carbondale, IL, 1990.

[15] L. Faigley, T.P. Miller, What we learn from writing on the job, College English 44 (1982) 557–569.

[16] R.S. Fish, R.E. Kraut, M.D.P. Leland, M. Cohen, Quilt: a collaborative tool for cooperative writing, Presented at Conference on Office Information System (COIS), 1998, pp. 30– 37.

[17] J. Galegher, R.E. Kraut, Computer-mediated communication for intellectual teamwork: an experiment in group writing, Information Systems Research 5 (1994) 110– 138.

[18] I. Greif, R. Seliger, W. Weihl, Atomic data abstractions in a distributed collaborative editing system, Presented at 13th Annual Symposium on Principles of Programming Languages, St. Petersburg, FL, 1986, pp. 160– 172.

[19] T.L. Griffith, M.A. Fuller, G.B. Northcraft, Facilitator influence in group support systems: intended and unintended effects, Information Systems Research 9 (1998) 20 – 36.

[20] A.L. Houston, H. Chen, B.R. Schatz, S.M. Hubbard, R.R. Sewell, D.T. Ng, Exploring the use of concept spaces to improve medical information retrieval, Decision Support Systems 30 (1999) 171–186.

[21] P.G.W. Keen, MIS research: reference disciplines and a cumulative tradition, Presented at First International Conference on Information Systems, Philadelphia, PA, 1980, pp. 9 – 18.

[22] P.B. Lowry, Improving distributed collaborative writing on the Internet using enhanced processes and a Java-based collaborative writing tool, Unpublished doctoral dissertation in MIS, University of Arizona, Tucson, 2002.

[23] P.B. Lowry, J.F. Nunamaker Jr., Improving collaborative writing processes and outcomes through the use of computermediated collaborative writing software (CWS), Working paper, 2000.

[24] P.B. Lowry, J.F. Nunamaker Jr., Using the thinkLet framework to improve distributed collaborative writing, Presented at 35th Annual Hawaii International Conference on System Sciences (HICSS), Hawaii, 2002, pp. 4051– 4060.

[25] P.B. Lowry, J.F.J. Nunamaker, Synchronous, distributed collaborative writing for policy agenda setting using Collaboratus, an Internet-based collaboration tool, Presented at 35th

Annual Hawaii International Conference on System Sciences (HICSS), Hawaii, 2002, pp. 89–98.

[26] P.B. Lowry, C. Albrecht, J. Lee, J.F.J. Nunamaker, Users experiences in collaborative writing using Collaboratus, an Internet-based collaborative work tool, Presented at 35th Annual Hawaii International Conference on System Sciences (HICSS), Hawaii, 2002, pp. 244– 253.

[27] K. McAlpine, P. Golder, A new architecture for a collaborative authoring system: collaborwriter, Presented at Conference of Computer Supported Cooperative Work (CSCW), 1994, pp. 159– 174.

[28] S.M. Miranda, R.P. Bostrom, Meeting facilitation: process versus content interventions, Journal of Management Information Systems 15 (1999) 48 – 114.

[29] D. Mittleman, M. Adkins, Using GroupSystems to improve the process of group document writing, presented at Seventh Annual GroupSystems Users Conference, Tucson, AZ, 1996.

[30] J.F. Nunamaker, D. Vogel, A. Heminger, B. Martz, R. Grohowski, C. McGoff, Experiences at IBM with group support systems, Decision Support Systems 5 (1989) 183 – 196.

[31] J.F. Nunamaker Jr., M. Chen, T.D.M. Purdin, Systems development in information systems research, Journal of Management Information Systems 7 (1991) 89–106.

[32] J.F. Nunamaker Jr., A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34 (1991) 40–61.

[33] J.F. Nunamaker Jr., A.R. Dennis, J.F. George, W.B. Martz, J.S. Valacich, D.R. Vogel, GroupSystems, in: R.P. Bostrom, R.T. Watson, S.T. Kinney (Eds.), Computer Augmented Teamwork: A Guided Tour, Van Nostrand-Reinhold, New York, 1992.

[34] J.F. Nunamaker Jr., R.O. Briggs, D.D. Mittleman, D.R. Vogel, P.A. Balthazard, Lessons from a dozen years of group support systems research: a discussion of lab and field findings, Journal of Management Information Systems 13 (1997) 163–207.

[35] W.J. Orlikowski, J.J. Baroudi, Studying information technology in organizations: research approaches and assumptions, Information Systems Research 2 (1991) 1 – 27.

[36] I.R. Posner, R.M. Baecker, How people write together, Presented at 25th Hawaii International Conference on System Sciences, Hawaii, 1992, pp. 239– 250.

[37] R.P. Rice, J.T. Huguley Jr., Describing collaborative forms: a profile of the team-writing process, IEEE Transactions on Professional Communication 37 (1994) 163– 170.

[38] D. Robey, Research commentary: diversity in information systems research: threat, promise, and responsibility, Information Systems Research 7 (1996) 400– 408.

[39] N. Romano, J.F. Nunamaker Jr., R. Briggs, D. Mittleman, Distributed GSS facilitation and participation: field action research, Presented at Thirty-Second Annual Hawaii International Conference on System Sciences, Hawaii, 1999.

[40] Y. Yao, B. Ives, Electronic government, in: P.B. Lowry, J.O. Cherrington, R.J. Watson (Eds.), The eBusiness Handbook, CRC Press, Boca Raton, FL, 2001, pp. 243 – 259.

![](/api/attachments/NUMFMV9A/fulltext/images/7f1895df57714ce06985e6c6f3e022ff560cce6daef0f0b5ecdfa27caa8f79a6.jpg)

Paul Benjamin Lowry is an assistant professor of Information Systems at Brigham Young University’s Marriot School. Paul’s research interests include Internet-based collaboration (e-collaboration), e-business, GroupWare/GSS, collaboration, technology-assisted virtual teams, and distributed group work. His current research involves creating technologies and analyzing processes that enable distributed groups to effectively collaborate over the Internet,

using brainstorming, group outlining, group discussion, group annotations, and group writing. Paul received his Ph.D. in Management Information Systems from the University of Arizona in 2002; he also attended Brigham Young University, receiving a BS in Information Systems in 1991, and an MBA in 1997. Paul’s work experience comes from several fortune-100 companies including Ernst and Young Management Consulting, Ameritech, SoftSolutions/Novell, Price Waterhouse Management Consulting, and IBM. His key clients have included organizations such as 3M, Imation, Dial Corporation, the United Nations, the Wyoming Transportation Department, and Vanstar/Computerland.

![](/api/attachments/NUMFMV9A/fulltext/images/42fea882c19c05e636a4b70b12b6a5a496d29ce4a0fb9748433bef6968c79cd4.jpg)

Conan C. Albrecht is an assistant professor of Information Systems and a Rollins Fellow at Brigham Young University’s Marriott School. Conan has been involved in Information Systems and Computing for over two decades. He has worked in the areas of computer-related fraud detection, collaborative computing, group support systems, and network programming. He is currently heading a project to create a peerto-peer, worldwide, genealogical network

that will make searching for and publishing of genealogical data more accurate and effective. Conan received his PhD in Management Information Systems from the University of Arizona.

![](/api/attachments/NUMFMV9A/fulltext/images/ec4d6f2e6a18d178fbc15a4f593a1c9235e454bedf24a703247c663bc50e0a42.jpg)

James D. Lee is the Associate Director of CMI and has been with the center since 1990. In his research responsibilities with CMI, he has worked with various government agencies including the U.S. Department of Defense, the Defense Environmental Security Corporate Information Management (DESCIM) Office, the Army Environmental Center, the Air Force Research Laboratory, the Army Research Laboratory, and the U.S. Navy. His research interests include electronic meeting systems support for business modeling, process improvement, systems analysis and design, database management, and activity-based costing. Jim’s work has been published in the Journal of Management Information Systems, the ACM SIG GROUP Bulletin, Interacting With Computers, and also in several conference proceedings.

![](/api/attachments/NUMFMV9A/fulltext/images/818e39583b688e6db48da3ba1f62370f8d27c5fab4d5b9863a011e3756187a52.jpg)

Jay F. Nunamaker Jr. is Regents Professor and Director of the Center for Management of Information at the University of Arizona. He was a faculty member at Purdue University prior to founding the MIS department at the University of Arizona in 1974. Under his leadership for 20 years, the department has become known for its exper tise in collaboration technology and the technical aspects of MIS. In 1996, Dr. Nunamaker received the DPMA EDSIG

Distinguished IS Educator Award. The GroupSystems software resulting from his research received the Editor’s Choice Award from PC Magazine, June 14, 1994. At the GroupWare 1993 Conference in San Jose, he received the GroupWare Achievement Award along with recognition of GroupSystems as best of show in the GDSS category. In 1992, he received the Arthur Andersen Consulting Professor of the Year award. Dr. Nunamaker received his PhD in systems engineering and operations research from Case Institute of Technology, an MS and BS from the University of Pittsburgh, and a BS from Carnegie Mellon University. He was an original member of the ISDOS project (PSL/PSA) under the direction of Professor Daniel Teichroew at Case and the University of Michigan from 1965 to 1968.
