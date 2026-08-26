---
otero_id: 8710
otero_key: "J3A42WME"
title: "Impact of Internal Open Source Development on Reuse: Participatory Reuse in Action"
authors: "Padmal Vitharana; Julie King; Helena Shih Chapman"
year: "2010"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222270209"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/J3A42WME/fulltext/images/777ba41edcc67eb031e7fd00864490819e15ac982329f6be3cc89ac2e17b329e.jpg)

# Impact of Internal Open Source Development on Reuse: Participatory Reuse in Action

Padmal Vitharana , Julie King & Helena Shih Chapman

To cite this article: Padmal Vitharana , Julie King & Helena Shih Chapman (2010) Impact of Internal Open Source Development on Reuse: Participatory Reuse in Action, Journal of Management Information Systems, 27:2, 277-304

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222270209

![](/api/attachments/J3A42WME/fulltext/images/a7624140b9a4eae105b2980cafaad572b44b5b535eef8b290dc8e603ceefcf44.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/J3A42WME/fulltext/images/2daebd6430f129328186d33419e366779de755c725178c3508a5e5e2095a912c.jpg)

Submit your article to this journal

Article views: 20

![](/api/attachments/J3A42WME/fulltext/images/1060d1fe32b831d7df637b6dc2f7f79358804930225b3de6aef473deb359f454.jpg)

View related articles

# Impact of Internal Open Source Development on Reuse: Participatory Reuse in Action

Padm al Vitharan a, Julie Kin g, and He len a Shih Chapm an

Padmal Vitharana is an Associate Professor of Information Systems at Syracuse University. He received his B.S., MBA, and Ph.D. from the University of Wisconsin system. His research interests lie in software development in general and reusable component/services in particular. His research has been published in journals such as the Communications of the ACM, IEEE Transactions on Software Engineering, IEEE Transactions on Man, Systems, and Cybernetics, Marketing Science, Information and Management, Database for Advances in Information Systems, Communications of the AIS, and Information Resource Management. He also edited a special issue on service-based development titled “Architecture and Design for Application Agility” in Information Technology and Management.

Julie King is an IBM Vice President and Distinguished Engineer at the Research Triangle Park, NC. Her team incubates technologies that show promise of improving the consumability of Software Group products. She is also the Chair of the Software Group Architecture Board, which provides technical strategy direction for the portfolio; Co-Chair of the Asset Architecture Board, a pivotal element of IBM’s reuse strategy, and a member of the IBM Academy of Technology. She has been working in software product development for over 29 years, having held various chief programmer, chief designer, and technical strategist positions. She holds an undergraduate degree from Duke University and an M.S. in computer science from the University of Oregon.

Helena Shih Chapman is Program Director of IBM’s globalization technology team. She is responsible for the technology, architecture, and development strategy of IBM’s globalization tooling, which enables IBM offerings’ capabilities to meet worldwide customer linguistic needs. Prior to joining IBM’s globalization leadership team, she oversaw IBM’s internal open source program, and managed IBM’s software division’s customer satisfaction and quality management initiatives. She was the recipient of IBM’s outstanding technical award for her work on internationalization support in Sun’s JDK 1.1 and subsequently became the development manager for ICU (international component for Unicode). In addition to her professional experiences at IBM, she held numerous technical lead and development positions at Taligent and Dataware Technologies. She also worked on the Dylan project at Apple’s advanced technology group. She received her M.S. in computer science from the University of Massachusetts.

Abs trac t: Adoption of open source software (OSS) principles to internal software development has gained considerable momentum. Often labeled as “internal open source” (IOS), several large firms have started to implement these programs. Research to date has mostly focused on facilitating IOS adoption. In the present research, we focus on how IOS affects reuse. Employing a qualitative case study, we examine the IOS program at IBM called “Community Source.” Analyzing data gathered from multiple sources reveals that IOS adoption facilitates participatory reuse by enhancing information sharing and leveraging of broader community skills. Participatory reuse manifests itself when potential reusers participate in the entire development process leading to the creation of reusable assets. Based on data, we develop a theoretical model to illustrate how IOS affects reuse. While furthering research on IOS and reuse, the model informs managers wishing to foster participatory reuse that they are wise to adopt IOS as a vehicle to promote greater openness of the software development infrastructure for leveraging broader community skills and enhancing information sharing among projects’ stakeholders.

Key words and phras es : closed source, internal open source, open source, open source software, participatory reuse, software reuse.

Landmark triumphs s uc h as the Apac he Web s erv er and the Linux operating system have fueled considerable interest in open source software (OSS). Successes in these OSS projects have been attributed to several factors. For instance, when members subscribe to the ideology of the OSS community, the corresponding project is expected to realize greater success [47]. Intrinsic motivation of participating developers is also cited as a basis for OSS success [51, 55, 56]. There is evidence that OSS, when compared to closed source development, has manifested in lower development costs, higher quality, greater freedom for participants, enhanced knowledge creation, and greater creativity and innovation [2, 39, 48, 51, 56].

Upon witnessing such OSS successes, many large firms have started to question how this phenomenon could be implemented within their organizational boundaries [36]. If a group of individual freelancing developers and corporate-sponsored developers from a large number of firms are able to come together to develop software that benefits all, why couldn’t a single firm leverage skills of all its employees to benefit the entire organization? In fact, some firms have undertaken programs to implement OSS concepts within their organizational borders [12, 14, 21, 39, 54]. The interest in such OSS-style development, though within a single firm, has been further attributed to shortcomings evidenced in traditional closed source development. For instance, literature on closed source development reports organizational distance measured in terms of the hierarchical organizational structure representing a network of relationships among project’s stakeholders as an impediment to facilitating information sharing among them [41].

Often labeled as “internal open source” (IOS), the aforementioned organization-wide community-based initiatives are now starting to burgeon across the software industry. Many firms, such as Cisco Systems, Hewlett-Packard, IBM, Lucent Technologies, Phillips Healthcare, and SAP, have kicked off IOS programs. Nonetheless, research to date has focused mostly on facilitating IOS adoption (e.g., [12, 21, 39, 43, 54]). In this research, we focus on how IOS affects an important organizational outcome—namely, reuse. Essentially, we investigate the following research question:

## RQ: How does IOS adoption affect reuse?

In employing a qualitative case study, we examine the IOS program at IBM called “Community Source.” Analyzing data gathered from multiple sources reveals that IOS adoption facilitates participatory reuse by enhancing information sharing and leveraging of broader community skills. Participatory reuse emerges in instances where potential reusers participate in the entire development process leading to the creation of reusable assets. Utilizing data, we develop a theoretical model to illustrate how IOS affects reuse.

This paper is organized as follows. Next, we present related literature in IOS and reuse. Research methodology employed to address the research question is presented in the third section. The theoretical model stemming from the findings is illustrated in the fourth section. Then we discuss various aspects of the model and offer theoretical basis for causal linkages in the model. Practical and research implications are discussed in the sixth and seventh sections, respectively. The paper closes with limitations and directions for future research.

## Related Literature

## Internal Open Source (IOS)

In broad terms , we define IO S as the adoption of OSS principles to internal software development. This definition is consistent with definitions adopted by others investigating the IOS phenomenon. For example, in labeling its IOS program as “Corporate Source,” Hewlett-Packard defines it as the “application of Open Source concepts, perspectives, and methodologies within the corporate environment” [12, p. 2]. While firms embracing the new development paradigm are still keen on safeguarding its proprietary assets, IOS is carried out in an open, transparent fashion in which anyone in the organization with an interest in the software being built is allowed to partake in its development efforts and allowed access to various project assets such as code.

Several authors report their experiences in adopting IOS in organizations. In discussing IOS adoption at Hewlett-Packard, Dinkelacker and Garg [12] note that IOS adoption at its heart is more of a process of social change rather than a technical one. They identify key challenges to IOS adoption as (1) resource constraints that may prevent managers from contributing their developers to IOS projects, (2) need for a leader to promote the IOS project/product, (3) managing skill set at the corporate level because the contributor pool spans the entire firm, and (4) training developers to use IOS. As a result of a successful IOS adoption exercise at Lucent, Gurbani et al. [21] observe the need for a “benevolent dictator” to serve as the final arbiter of what goes into code by accounting for organizational needs, by carefully tracking independent strains of the software, and by implementing an effective code distribution strategy. They speculate that IOS will succeed the most when (1) code/product is needed by several groups across the firm, (2) it is relatively immature in that requirements are not fully known at the outset, and (3) groups have different needs and specific expertise. In reporting from IOS experience at Phillip Healthcare, Wesselius [54] underscores the need to give community members adequate control over the software’s evolution. He further highlights the need for incentives to entice manufacturers to produce assets and consumers to use those assets. In admitting that IOS-based co-development has worked well for the company so far, he uses Raymond’s [38] vernacular to acknowledge that it is possible to have a bazaar inside the cathedral.

To date, the most extensive findings on IOS adoption have been reported by Riehle et al. [39]. In contrasting OSS principles of egalitarianism, meritocracy, and selforganization that promote collaboration, Riehle et al. observe key hindrances to collaboration in traditional closed source as a top-down task assignment, focusing on contributor’s status/rank rather than merit, and management’s imposition of which software development processes to follow. These authors identify OSS’s benefits to IOS collaboration as the abundance of volunteers who are motivated to contribute based on their own interests, better quality through quasi-public internal scrutiny, availability of expertise from a vast pool of volunteers, broad support and buy-in from across the organization, and better research-to-product transfer by securing contributions from those in downstream product units. They note that an effective IOS infrastructure needs to provide support for interested parties to easily find a project, understand the project, and contribute to it. From their experiences in an IOS project at SAP, Riehle et al. acknowledge that for the most part, the aforementioned OSS benefits for collaboration were realized. In sum, these authors acknowledge that for IOS to emulate the three OSS principles mentioned earlier, project managers must (1) adopt a mind-set that welcomes anyone who cares to help (egalitarianism principle), (2) realize that contributions can be based on perspectives that might be unfamiliar to the original developers (meritocracy principle), and (3) accept the fact that volunteer contributions sometimes mean adjusting to their needs and timelines (self-organization principle).

Adapted from an IBM internal document, Table 1 offers an itemized comparison of development activities in typical closed source, IOS, and OSS. For example, in closed source development, market planning translates customers’ needs into software requirements. At the same time, IOS mimics the requirements management practices of OSS where project management committees set the priority for a given project. If such a committee does not exist, then providers and contributors drive the requirements process.

## Reuse

One key concern of software development organizations is reuse (e.g., [22]). Reuse is argued to improve software productivity and quality [18, 35, 45]. While some reuse programs have succeeded, many have failed due to lack of reusable assets, crude retrieval technologies, overhead involved in incorporating reusable assets, bias in the not-invented-here syndrome, time and budget pressures, and incentive incompatibility, among others [17, 20, 25].

<table><tr><td></td><td>Traditional product development (closed source)</td><td>IBM internal open source (termed Community Source)</td><td>Typical OSS development</td></tr><tr><td>Requirement management</td><td>Market planning translates customers&#x27; needs into software requirements.</td><td>Same as OSS. Project administrators are usually the main leaders of this process.</td><td>Project management committee (PMC) (if one exists) sets the priority of a given project. Otherwise, the provider and contributors drive the requirement process.</td></tr><tr><td>Project management</td><td>Dedicated product development team leads drive the overall project management, work estimation, change management, and legal or other issues management.</td><td>Same as OSS.</td><td>PMC or provider is usually in charge of the overall project management.</td></tr><tr><td>Development—design</td><td>Detailed design specification and review procedures are documented and kept in team rooms. Reviews are typically limited to the core team.</td><td>Mostly the same as OSS, although the information is only visible to project members.</td><td>Design policy varies among projects. The design is usually proposed by the author(s) and communicated through forums, mailing lists, or other open discussion channels.</td></tr><tr><td>Development—architecture</td><td>Architecture specification is provided and kept in team rooms. Reviews are typically limited to the core team.</td><td>Same as OSS, although the information is only visible to project members.</td><td>Architecture specification is communicated through open forums and mailing lists. Checklist and coding standards are public and well defined.</td></tr></table>

<sub>1.</sub> <sub>Develop</sub>m<sup>ent</sup> <sup>Con</sup>

<sub>le</sub> <sub>1.</sub> C<sup>ontinu</sup>

<table><tr><td></td><td>Traditional product development (closed source)</td><td>IBM internal open source (termed Community Source)</td><td>Typical OSS development</td></tr><tr><td>Development—participation</td><td>By invitation only; the developers and users of a particular asset are well defined and only the people within the asset community are aware of the changes.</td><td>Any interested party can request to join a project in Community Source. The project administrator has the ability to approve the requests for membership. All project information is public by default and the project administrator can create private, member-only project space.</td><td>Any party interested in participating has full access to any information related to the project.</td></tr><tr><td>Quality assurance</td><td>Quality plan and preventive actions are well documented and kept in team rooms. A dedicated test team is provided. Internal feedback (outside of core team) is usually solicited at the end of dedicated quality assurance cycle.</td><td>Same as OSS.</td><td>Relies on the consumer community as an active early adopter to help with ensuring the quality of each release. There are usually a lot of quality assurance activities from outside the core team early in the development cycle. Test plans are usually not provided.</td></tr><tr><td>Release management</td><td>Release plans are well defined and kept in team rooms. Dedicated release engineering teams are provided. Each release usually involves significant feature/defect changes.</td><td>Same as OSS.</td><td>Driven mostly by PMC where a clear release schedule may or may not be provided. Code is generally released frequently with smaller incremental changes in each release.</td></tr></table>

<table><tr><td>Configuration management</td><td>Installation policy, platform support, and configuration plan are well defined and kept in team rooms.</td><td>Same as OSS.</td><td>Installation, platform support, and other configuration plans are usually driven by the PMC and contributors.</td></tr><tr><td>Maintenance and support</td><td>Support and service (including training) is well defined and planned (directly provided by IBM).</td><td>Support and service is negotiated between the provider and consumers.</td><td>Support and service is usually not well defined. The provider or anyone else can offer to provide service and support to a project.</td></tr><tr><td>Packaging and distribution</td><td>Distribution of deliverables is available through physical media or electronic downloads at a single location.</td><td>Distribution of deliverables is usually only available through electronic download through the Community Source Web site.</td><td>Distribution of deliverables is usually only available through electronic download. Typically a central location to various mirroring sites.</td></tr><tr><td>Life cycle management</td><td>End-of-life support (terms/conditions) for a given product release is defined well in advance.</td><td>Does not apply unless specified by the provider.</td><td>Does not apply.</td></tr></table>

The emergence of programming paradigms such as object-oriented development and component-based development has partially addressed the challenges managers face in implementing organization-wide reuse programs. Based on objects and their interactions, object-oriented development relies on concepts such as encapsulation, modularity, inheritance, and polymorphism to promote reuse [8, 29, 34]. However, scholars such as Morisio et al. [35] have found that it is a mistake to hold the belief that object-oriented development is all that is necessary to achieve success in reuse.

In contrast to object-oriented development, component-based development is based on developing applications by integrating independent business components. For example, an accounting application could be built by integrating high-level reusable components such as accounts receivable, order processing, and inventory management. Nonetheless, Kim and Stohr [28] observe that in addition to technical advancements in programming such as object-oriented and component-based development, organizational issues must also be addressed if reuse programs are to be successful.

Several organizational catalysts for promoting firmwide reuse have been identified. First, many acknowledge the need to incorporate reuse into the software development process throughout the enterprise [3, 9, 20, 33]. To this end, managers could promote practices that advance reuse [33]. For example, if a developer uses a piece of code from another project that is not already in the reuse repository, a manager might then mandate that this code segment be placed in the reuse repository for subsequent reuse. Or when producers build reusable assets, managers could direct them to garner feedback from potential consumers from across the organization [16].

Second, as conflicts among reuse stakeholders (e.g., asset producers and consumers) are bound to occur, Sherif et al. [45] concur on the need to promote avenues for communication and coordination to resolve such conflicts. They argue that communication and coordination enable asset producers and consumers to become knowledgeable in each other’s work and alternative perspectives and disagreements to surface. Enhanced communication and collaboration lead to greater organization-wide reuse as parties spread across the firm are better able to resolve conflicts (e.g., functionality of a reusable asset), asset producers become more knowledgeable in consumers’ needs, and consumers are better able to participate in shaping reusable assets.

Third, some identify the need to promote reusable assets throughout the organization (e.g., [33]). Promotion of reusable assets in turn plays a key role in consumers ability to locate potential reusable assets and assess their functionality to determine whether they meet their needs. In a case study examining reuse, Sherif and Vinze report instances where developers were “unaware of assets at an organizational level and relied heavily on word of mouth to find them” [44, p. 171]. Developers in their study attributed lack of means to promote reusable assets as a crucial barrier to organization-wide reuse.

Last, to achieve widespread reuse, organizations need to embrace infrastructures that facilitate reuse [28]. Infrastructures that facilitate reuse include tools for coding reusable assets; soliciting potential consumers’ feedback; and storing, searching, and retrieving reusable assets [26, 45]. Nonetheless, while enablers of reuse are acknowledged, effective organization-wide reuse in the closed source context continues to elude project managers.

Since the emergence of OSS, many scholars have identified it as a catalyst for reuse [1, 23, 46]. For example, Spinellis and Szyperski contend that the “open source community gives us a rich base of reusable software” [46, p. 29]. Over the years, a number of researchers have started to investigate reuse in OSS. In studying reasons for code reuse in OSS, Haefliger et al. [23] report that OSS developers reuse code because they (1) want to write preferred code, (2) operate under limited resources, and (3) aim to mitigate development costs through code reuse. In a similar vein, von Krogh et al. [52] found that developers saw reuse as an opportunity to shift their effort to more creative work. Madanmohan and De [32] report that the most important issues firms face in reusing OSS relate to its functionality, licensing, and the platform fit. Grewal et al. [19] show that social capital measured in terms of network embeddedness (nature of the relationship among projects and developers) affects (re)use of project code. In examining OSS reuse on software development economics, Ajila and Wu [2] found that reuse maturity in adopting OSS has a positive relationship with software development productivity and product quality. These authors assessed reuse maturity at the firm level and measured it on a five-item psychometric scale (initial/ chaotic, monitored, coordinated, planned, and ingrained). Focusing on Linux as the sole OSS, Lee et al. [30] found that consumers’ perception of quality and satisfaction positively affected their use of Linux.

The handful of authors who reported on IOS recognized its potential to enhance reuse [12, 13, 21, 22, 39, 54]. However, except for Wesselius [54], all other authors mention reuse as a by-product of OSS-type adoption within the firm. Wesselius asserts that in order for IOS to realize its full potential as a vehicle for promoting organization-wide reuse, incentives are needed to entice both asset manufacturers and asset consumers. Dinkelacker and colleagues [12, 13] observe that resulting assets have the potential to advance reuse within the firm. Gurbani et al. report that “there was at least one indication that the open source approach [IOS] improved in some ways on earlier efforts in the company to encourage and support reuse” [22, p. 479]. Riehle et al. [39], who reported the most extensive findings on IOS, do not explicitly address reuse. Nonetheless, they do report that IOS project leaders expected an improved research-to-product transfer as a result of contributions from those in downstream product units.

## Summary

Lately, the pace of research in IOS has started to rise. To date, this research has mostly focused on IOS adoption. While our understanding of factors that facilitate IOS adoption and suitability of IOS (vis-à-vis closed source) for various projects has improved, the effect IOS has on important software development outcomes such as reuse is not well understood. But research has also made great strides in enhancing reuse in organizations. In particular, emergence of OSS has enabled developers to (re)use code written by others across the world. However, over the years, reuse within the organizational boundary has only been enhanced incrementally. IOS offers a unique opportunity for firms to significantly advance organization-wide reuse. In this research, we investigate on how IOS affects reuse.

## Research Methodology

Our goal is to gain greater ins ights into the emerging IOS phenomenon and to answer our key research question: how does IOS adoption affect reuse? Toward that end, we conducted a qualitative case study. Data were collected through multiple sources. An analysis was conducted in the context of uncovering constructs related to IOS adoption and reuse. These constructs were then used to develop a theoretical model on how IOS adoption affects reuse.

We adopt recommendations prescribed by Seaman [40] for conducting qualitative research in software engineering. Seaman underscores the need for qualitative methods for investigating new research questions in general and nontechnical aspects of software development in particular. IOS represents a new research genre that covers both technical and organizational dimensions of software development.

## Research Setting

We selected the IOS program at IBM called “Community Source” (CMS). It was chosen because of the relative infancy of the CMS program and because of the first author’s ongoing research partnership with the firm. IBM launched the CMS program in mid-2005.

## A Brief Summary of the CMS Program

Most CMS projects are initiated with management oversight. Small CMS projects initiated by individual developers are also encouraged. All project proposals require approval from the CMS project manager, who uses guidelines set forth for CMS to assess their suitability. Upon approval, the management of the sponsoring division assigns someone as the project administrator. Access to a project is granted at different member authority roles.

The Web-based front-end of CMS is based on the GForge (http://gforge.org) collaborative development software. When the request for a CMS project is approved, work space for CVS (concurrent versioning system) or SVN (subversion, an alternate form of version control), tracker, home page area, forum, mailing lists, task manager, document manager, news, file publisher, and component manager are set up. During registration, the project administrator with divisional management consent appoints individuals for various other roles. At this time, a project management committee (PMC) can be formed to manage the project, maintain priorities, and resolve conflicts. Project administrator(s) and senior developers of the project typically form its PMC.

Table 2. Data Sources

<table><tr><td>Data source</td><td>Description</td></tr><tr><td>The executive who oversaw the conceptualization and launching of the CMS</td><td>Conducted five phone interviews.</td></tr><tr><td>Site visit</td><td>Visited IBM’s Software Group Componentization Team in Raleigh, NC.</td></tr><tr><td>Interviews</td><td>Interviewed 12 project managers and developers.</td></tr></table>

Anyone can request to join the project at any time as a project member, although one needs special approval to contribute code. Membership is typically directed by management, but an individual may subsequently choose to participate (e.g., submit a change request) voluntarily.

## Data Collection

Multiple data sources are critical in qualitative case study research. Data from three sources informed this research (see Table 2). In adopting Seaman’s [40] recommendations for qualitative research, we followed her prescriptions in conducting interviews and note taking during interviews and site visits.

Because this is an exploratory study examining a relatively new phenomenon, a two-step data collection approach was utilized. In step 1, the first two data sources were used to gain insights into IOS. In step 2, constructs that emerged from step 1 were then used to compile interview questions. These constructs were subsequently employed to develop a theoretical model on how IOS adoption affects reuse.

## Conceptualization and Launching of the CMS

The first author interviewed the executive who oversaw the conceptualization and launching of the CMS a total of five times over a six-month period. These interviews, conducted over the phone, focused on the CMS paradigm, how it differed from traditional closed source development, and observations to date. During two of these interviews, two of the executive’s project leads involved in the CMS’s conceptualization, implementation, and operation joined in.

## Site Visit

The first author visited IBM’s Software Group (SWG) Componentization Team in Raleigh, NC. The site visit included discussions with the aforementioned executive and his team involved in the CMS’s conceptualization, implementation, and operation.

More important, the site visit also included a half-day roundtable discussion that focused on the efficacy of the CMS. Participants addressed challenges and opportunities in the CMS-based development, how the CMS has so far changed the development culture, feedback from ongoing CMS projects, and lessons learned. The executive along with 15 managers and developers participated in the discussion (some called in remotely).

## Interviews

During the first round of data collection, reuse emerged as a key construct that delineates closed source and IOS development. Following Kim and Stohr [28], we define this construct to mean the use of a previously developed asset in another application or a product offering. In addition, it was revealed that the level of information sharing and leverage of broader community skills varied in the two development contexts and that they may potentially affect organization-wide code reuse. We define the former to mean sharing of any information in the process of developing final assets (e.g., source code). Such information includes change requests, correspondence among members, code commits, and so forth. We define the latter to mean the project’s ability to recruit members from the broader organizational community. We generated interview questions along these three constructs with the goal of (1) assessing how closed source and CMS projects differed along each construct, (2) gaining a better overall understanding of the CMS paradigm, and (3) identifying relationships among constructs in order to develop a theoretical model on how IOS adoption affects reuse. Because we did not conceive a priori relationships among these constructs, the interview questions were constructed without implying any relationship among the constructs.

Senior management’s help was solicited in subject selection. Commensurate with the goals of this exploratory research study, interview subjects were recruited using the following criteria: (1) experience in CMS projects, (2) participating in more active CMS projects, and (3) availability at the time of interview. In total, six managers and six developers were selected for interviewing. One of the developers interviewed also participated in the roundtable discussion during the site visit. They all had extensive experience in traditional closed source development. Interviews were conducted over the phone. Prior to the interview, when scheduling the interview via e-mail, interviewees were informed of the purpose of the study, which is important in interviewing [40]. The first author conducted the interviews, which were tape-recorded. Interviewees were first presented with some general questions that focused on their experience in OSS, their perceptions on management commitment and employee buy-in to the CMS concept, and strengths and weaknesses of the CMS concept and the current CMS infrastructure. All interviewees answered general questions. Then, they were asked a set of questions corresponding to the three constructs. The Appendix provides the list of interview questions. Because of time constraints, a few interviewees were queried only on reuse or all constructs except reuse. Table 3 summarizes interviewee profiles and constructs covered.

Table 3. Interviewee Profile and Constructs Covered

<table><tr><td>Interviewee rank</td><td>Division (office)</td><td>Number of CMS projects</td><td>Constructs covered</td></tr><tr><td>Developer</td><td>Tivoli (Austin)</td><td>8</td><td>All except reuse</td></tr><tr><td>Developer</td><td>Application Integration Middleware (Raleigh)</td><td>5</td><td>Only reuse</td></tr><tr><td>Developer</td><td>Strategy and Technology (Raleigh)</td><td>9</td><td>All</td></tr><tr><td>Developer</td><td>Strategy and Technology (Raleigh)</td><td>5</td><td>All</td></tr><tr><td>Developer</td><td>Application Integration Middleware (Toronto)</td><td>4</td><td>All</td></tr><tr><td>Developer</td><td>Rational (Toronto)</td><td>5</td><td>All</td></tr><tr><td>Manager (software quality engineering)</td><td>Lotus (Ireland)</td><td>3</td><td>All</td></tr><tr><td>Manager (software development)</td><td>Lotus (Ireland)</td><td>3</td><td>All</td></tr><tr><td>Manager (software development)</td><td>Application Integration Middleware (Raleigh)</td><td>3</td><td>Only reuse</td></tr><tr><td>Manager (software development)</td><td>Strategy and Technology (Raleigh)</td><td>1</td><td>All</td></tr><tr><td>Manager (software engineer)</td><td>Rational (Toronto)</td><td>9</td><td>All except reuse</td></tr><tr><td>Manager (distinguished engineer)</td><td>Tivoli (Tucson)</td><td>3</td><td>All</td></tr></table>

## Analysis

The first set of data collected was from interviews with the executive who oversaw the conceptualization and launching of the CMS. The first author took extensive notes during the five interviews, which spanned a period of six months. This executive and his two project leads, who were also interviewed, participated in the CMS’s conceptualization, implementation, and operation, and hence were able to provide considerable insights into the challenges and opportunities in CMS development and lessons learned. Similarly, the first author took detailed notes during the site visit, which included personal interactions with attendees as well as participation in a halfday roundtable discussion on CMS. To address the research question and to identify relevant constructs, pertinent comments from the executive’s interview and site visit notes were identified and highlighted.

During the next data collection stage, interviews were conducted, which were tape-recorded. These tapes were then transcribed by a staff member of the first author’s university. Seaman [40] highlights the importance of tape-recording and then transcribing the audio to free the interviewer to focus on the task at hand—namely, interviewing. Transcriptions from the 12 interviews resulted in a total of 126 pages of single-spaced text comprising 36,190 words. The first author listened to the recorded tapes and read the interview transcripts several times to become immersed in the data, which is critical in case study research [15]. As transcripts were read, the first author identified and highlighted comments relating to the key research question. Further, with the intention of developing a theoretical model, data from various sources were examined iteratively to identify relationships among the aforementioned constructs. In case study research, iterative examination of the data plays an important role in theory building [40].

Our ultimate goal is to develop a theoretical model on how IOS affects reuse, though we first wanted to assess the extent to which the three constructs manifest in CMS. To this end, the first author and a graduate student in computer science created a grid to rate each interviewee’s (row) perceptions of each construct (column) based on the following categories: strong support, marginal support, no support, and no comment. Marginal support refers to instances where the interviewee offered only scant support for a particular construct without much elaboration; for example, “I think Community Source improves information sharing among team members.” First, two raters jointly reviewed the definitions for each category and categorized a few hypothetical statements. Then, they separately listened to the interview recordings and reviewed transcripts in completing the rating exercise. The two grids were then compared to assess interrater agreement. Note that although there were 12 interviewees, each construct had only 10 completed ratings. This is because two interviewees each did not respond to two of the constructs (see the “constructs covered” column in Table 3). For the three constructs—reuse, information sharing, and leveraging broader community skills— there was 70 percent, 80 percent, and 70 percent interrater agreement, respectively. When strong support and marginal support were grouped into a single “support” category, there was 90 percent interrater agreement for all three constructs. In other instances, mismatches were due to an oversight by the raters. In sum, the relatively high interrater agreement values enhance the validity of the findings reported in this qualitative research study.

When multiple raters are used, mismatches in ratings need to be reconciled [40]. To do so, the two raters reviewed all instances of rating mismatches. Through consensus upon review of the interview transcripts, the raters arrived at final ratings for the level of interviewees’ support for each of the three constructs. Final rating scores revealed 100 percent, 50 percent, and 60 percent “strong” support for reuse, information sharing, and leveraging of broader community skills, respectively. When strong and marginal support are grouped together, “support” for the information sharing construct rose to 70 percent, although no change was observed for the construct leveraging of broader community skills.

One unique characterization of reuse that emerges from CMS development is participatory reuse. We use the term participatory reuse here in a context similar to that of participatory design. Participatory design attempts to actively involve users in the design process to ensure that the end application meets their needs [6]. We conceptualize participatory reuse to mean the scenario in which potential reusers participate in the entire development process (e.g., analysis, design, development, testing) to ensure that the project assets meet their reuse needs.

![](/api/attachments/J3A42WME/fulltext/images/b6458467f27cda153be302f9eaf04b742e1169d1220b7d2e1ac64e3b0ff1a9a6.jpg)  
Figure 1. A Theoretical Model for IOS Development

## Theoretical Model

Ev idenc e from OSS literature points to how it could advance reuse in the wider software development community. Similarly, by adopting IOS, a single firm has the opportunity to promote reuse within the organization. Although several OSS studies have addressed reuse, there is only scant reference to reuse in the IOS literature. To our knowledge, no one has examined how collaboration among an organization-wide community of manufacturers and consumers of reusable assets, and information sharing among them, affect reuse. Against this backdrop, we employ the case study findings to theorize the model depicted in Figure 1. This theoretical model shows the postulated relationships among constructs, which are discussed next.

Results affirmed that IOS offers a more open infrastructure than those offered by typical closed source development (Figure 1, arrow 1). The essence of the IOS concept is to promote greater openness by allowing any interested party to fully participate in the development activities throughout the project. Related comments heard from developers and managers supporting the purported openness include:

It [CMS] gives you a one-stop shop for all different pieces of information and infrastructure for developing a product or a component.

You can pretty easily go out there [to CMS] and see what is new.

You can go off to the Community Source site and quickly find what you are interested in.

[In CMS,] it’s a lot easier to have visibility into what component teams are doing.

## One manager epitomized the openness in CMS by stating:

People know to go to the Community Source area and that they see active projects. . . . They can do a search there and find projects they are interested in; it is a matter of, from that page registering, they have access right away to view the documentation and the source code.

In unison, they reported that in closed source, however, there is an inherent lack of openness of the development infrastructure as the project space is kept in isolation from others. In contrasting infrastructure openness in closed source and CMS, a manager bluntly pointed out, “closed source is just that; it is closed.”

Findings reveal that the greater openness of the IOS infrastructure enhances information sharing among a project’s stakeholders (Figure 1, arrow 2). The heart of IOS conceptualization is based on creating an OSS-style culture within a single organization. OSS promotes information flow that is critical for software development [47, 51]. Similarly, IOS programs such as CMS offer an open and transparent medium for all stakeholders to easily participate and share relevant information. Comments acknowledging the relationship between openness and information sharing heard during interviews include:

A great strength is that the [CMS] infrastructure facilitates communication.

It [CMS] allows groups to have access to source code they wouldn’t normally have access to, to help debug problems or to gain more knowledge of how the code actually works.

We love having source code [in CMS] so we can understand what’s going on; to figure out problems ourselves, create work around ourselves; being able to contribute pages back.

Strength [of CMS] is the sharing of information and how broadly that information can be disbursed.

It [CMS] facilitates more collaboration just because it is easier to try and get involved in something than it could be otherwise.

In contrast, one manager pointed out that in closed source, when you request a piece of code, you would have to wait for days before you get it. This would certainly hinder collaboration among stakeholders. Highlighting modus operandi in closed source, one developer notes, “you normally don’t expose your code to other products within the company.”

Greater openness of the IOS infrastructure also enhances a project’s ability to leverage broader community skills (Figure 1, arrow 3). Unlike closed source development, because of the greater visibility it offers, CMS has the capacity to self-advertise its projects. As a result, potential stakeholders could reach out to interdivisional projects that interest them even without any formal recruiting by the project’s sponsors. In claiming that “in the Community Source, they come to you,” one manager observes that “what we usually find is that the person that comes to us to get involved in the [CMS] project is the specialist on that team, their area.” As can be seen from the following excerpts, managers and developers agree that CMS offers a setting more favorable to leveraging greater involvement among various stakeholders throughout the firm.

Our project has been initially started with people from our own geography. And with the purpose of growing that by gaining momentum in Community

Source, [we] drew in stakeholders into providing people as needed to help it [project]. (manager)

It [CMS] is more apparent and everybody gets more information through this site. Having the one central site is good in that you can actually access information from one area, and everybody is aware of that area. (manager)

In a closed-source project, it’s a job; whoever might be the manager or leads for the project would decide who might be part of the team based on an interview process whether it’s people who are moving internally or externally. In Community Source projects, none of that happens. Somebody says I like this; I want to join your project. You pretty much usually approve them, saying, “feel free to join us,” and then they contribute to that project. (developer)

When you have an open process to development [as in CMS], you get more developers looking at the code and being able to see other people’s code. (developer)

They reported that in closed source, however, because of the lack of openness of the development infrastructure, as the project space is kept in isolation from others, someone with an interest in the project has to go through an elaborate mechanism to get permission to join in. Some affirm how the lack of openness that is evident in closed source hampers a project’s ability to leverage people from across the firm:

[In closed source,] we could have a different source code repository, each person had to request access to and to download drivers, he would need to request access from another team. It seems like there are too many people that had control over too many pieces. (manager)

[In closed source,] in some cases, you could put in a request to access the database and you see a person who needs to approve access takes a while or doesn’t get back to you; depending upon your level of interest, you might just forget about it. (manager)

[In CMS,] it is easy for people to join projects irrespective of where they are, it’s easy for them to contribute code, it’s easy for them to look at the source code of the project . . . , which is very tough to do in closed source [development]. (developer)

Increased information sharing in turn leads to greater reuse of the project’s assets (Figure 1, arrow 4). As many interviewees pointed out, the fact that you can readily participate in CMS projects, submit change requests, share information, and contribute to them leads to greater reuse of the artifacts resulting from those projects. Testimonials supporting the link between information sharing and reuse include:

If it [asset] comes really close to meeting your needs but needs a few changes, in a closed source world, you’d be off to the negotiation table with the other team saying, “please add function a and b,” and if that doesn’t add up with their market management team, you never get the function into the code that you want and you’re at a stalemate. You build essentially fragile, release dependencies on code that hasn’t been implemented. If it’s in Community Source and the code is there, you have the freedom to extend what is there, contribute to it, and contribute it back. (manager)

The strengths [of CMS], of course, are the free exchange of information and access to the source code. It’s pretty easy to find what’s on the Community Source Web site. You can pretty easily go out there and see what’s new and what you might be able to use. (developer)

[In CMS,] we might be able to see what other products are doing and what other people are writing; [therefore,] we would duplicate less and reuse what other folks have already done. (developer)

Finally, findings reveal that a project’s ability to leverage broader community skills positively influences the reuse of that project’s assets (Figure 1, arrow 5). It was apparent from interviews that when personnel from a larger number of divisions constitute the project’s membership, a wider audience will be aware of the project and its resulting assets, thus enhancing the potential for greater reuse of those assets:

If you see that there is some function out there that does what you need to do, and it has the right footprint and other characteristics, first of all, you have knowledge that somebody else developed and can potentially pick it up. In a closed source environment, you never would. So, even the potential for code reuse is out of the question unless you happen to have the right connection in the company in the closed source model. You’re more likely to simply reinvent because you’re ignorant of the fact that some other product or other component existed out there that you could have actually used. (manager)

Most developers join a CMS project to help build assets that they could eventually reuse in their own work. In providing evidence to this scenario, one developer notes that he and his colleagues join CMS projects in other divisions “because the technology that those projects were developing, we were actually interested in reusing them in our code source.” In recalling why she joined in a CMS project, another developer notes: “I recommend we use a particular piece of community source to my manager and my development team.” A third developer offers further evidence of the linkage between interdivisional participation and the reuse of resulting assets by highlighting:

Taking an example where, say, the [closed source] project has already existing code, the project has come to a point where they want to move to the Community Source model. So, there was this notion of that owner of that code already before they got into Community Source. So those owners have a menu of a bunch of people who have been using their code. I will call then the “exploiters.” They know that the exploiters have some additional requirements, additional functions that they would like in their code and now the component owners find that they don’t have the bandwidth to add that function; so they may like these exploiters to join in and contribute to that code [in CMS]. (developer)

Interestingly, another dimension in community-wide involvement leading to greater reuse rests on CMS projects’ ability to generate assets that could be used in a novel way. For example, one developer attributed the greater reuse in the CMS setting to “more people doing different types of things; something the originator of the project didn’t expect it to develop into.”

In sum, the following excerpt highlights the essence of CMS’s power to enhance reuse:

Community Source is all about code reuse. It’s about developers being allowed access to code that performs the functions they might be looking for, that’s already been written, that is going to save them time in incorporating, . . . in that it actually saves time in the whole requirement process if they have requirements against the component that is not quite implemented; but if the component is in Community Source, they can actually contribute back; take what is there and enhance it, contribute it back as opposed to rewriting it from scratch. I also think a lot of our developers don’t understand what functionality has been implemented in our other products, and so they’re likely to reinvent that stuff that has been implemented elsewhere simply because [in closed source development] they don’t have access to the code or the information about the fact that the function exists. (manager)

## Discussion

Our goal in this res earc h was to ans wer the ques tion, how does IOS adoption affect reuse? Using a case study approach, we offered support for the theoretical model focusing on reuse. During interviews, managers and developers reveal that adoption of IOS promotes greater openness of the software development infrastructure leading to leverage of broader community skills and greater information sharing among a project’s stakeholders, which in turn enhance organization-wide reuse. Our findings support the theoretical model identifying two key antecedents of reuse and their relationships, and we now take a step back and attempt to theorize causal linkages in the model.

Overall, our work falls under the organization change research. Within this umbrella, there are several streams that could be utilized to theorize the IOS phenomenon. Of them, the boundary-spanning literature offers a fitting lens to study IOS. On broad terms, the boundary-spanning literature focuses on interorganizational knowledge transfer as well as knowledge transfer across internal organizational boundaries [37], precisely what information systems (IS) development in a large organization such as IBM entails. To date, several IS scholars have applied boundary spanning as a theoretical lens to examine how information technology (IT) facilitates various aspects of knowledge transfer among different units of an organization (e.g., [31, 37]), although to our knowledge, no one has applied it to investigate organization-wide reuse.

Boundary-spanning literature distinguishes between boundary objects and boundary-spanning activities [5, 31, 37]. According to Pawlowski and Robey [37], shared IT systems represent boundary objects linking organizational units. In IS research, boundary objects examined varied from enterprise resource planning to knowledge management and general reporting systems, much the same way CMS “infrastructure” is examined in this research. The CMS infrastructure refers to the corresponding ITs associated with it such as the Web site, concurrent versioning system, mailing lists, discussion forums, asset repository, and the like. However, boundary-spanning activities represent various tasks carried out by stakeholders dispersed across organizational units [37]. In the context of CMS, these activities include coding, submitting change requests, negotiating requirements, reporting defects, and searching for reusable assets. These boundary-spanning activities typify the manifestation of the CMS “concept” (i.e., IOS)—namely, the adoption of OSS practice within an organization. We view infrastructure as the technology “plumbing” employed to implement the CMS concept, thereby facilitating aforementioned boundary-spanning activities.

When compared to CMS, both closed source as a concept and closed source as an infrastructure place hindrances to effective boundary spanning. First, the essence of the closed source concept is based on a team working in isolation from others in the organization to develop some system. Second, even if an existing closed source team chooses to open the project up for everyone in the organization, there are constraints in the closed source infrastructure that would prevent it from readily doing so. As evident from the interviews, an outsider wanting to join in a closed source project has to go through an elaborate sequence of steps. This lack of openness in the closed source infrastructure constrains boundary-spanning activities. For example, unlike in CMS, only those who are assigned to the closed source project are able to make change requests, report defects, and search resulting assets. While closed source development projects might involve parties across divisions/units, because of constraints in its infrastructure, boundary-spanning activities are generally carried offline. For instance, when manufacturers in one division in closed source development need to gather requirements from consumers in other divisions, typically they would call up a meeting or set up a workshop, outside of the closed source “infrastructure.” However, being specifically designed as a boundary object, CMS infrastructure provides online facilities for parties dispersed throughout the organization to identify and negotiate requirements online.

Although deemed efficient, specialization of a division creates obstacles to knowledge transfer among divisions [49]. CMS offers the means to facilitate knowledge transfer across such divisions by employing three approaches (syntactic, semantic, and pragmatic) that, according to Carlile [5], help frame boundary challenges in organizations. First, CMS establishes a shared syntax for individuals across the firm to represent their knowledge (syntactic approach). It does this by providing syntactical boundary integrating devices that facilitate postings, defect reporting, and code submission, archiving, and downloading. Establishing this shared syntax is essential for accurate communication among members across the boundary [42]. Second, CMS offers support for recognizing that there are different interpretations among individuals across divisions (semantic approach). Semantic boundary integrating devices in CMS include shared methods or protocols to acknowledge nuance in point of view, interests, dependencies, and priorities. Last, CMS brings to the fore negative consequences that can arise from differences at the boundary as a result of knowledge being localized, embedded, and invested in each functional area (pragmatic approach). Through various media such as discussion boards and chat rooms, CMS offers pragmatic boundary integrating devices for participants across the firm to represent, learn, negotiate, and alter the existing knowledge and to create new knowledge to resolve negative consequences.

Although the infrastructure may provide the means for collaboration, it has little use unless the members in the community have impetus for collaboration. In large firms, software development projects involve a multitude of stakeholders from various units of the organization who have to communicate and collaborate to achieve project success. Because CMS as a boundary object offers an open environment that lowers the cost of communication and collaboration, parties are more likely to engage in boundary-spanning activities such as accessing documents, making change requests, reporting defects, and so on. The same open environment also enables a CMS software development project to naturally recruit interested parties to readily join a project and carry out various boundary-spanning activities. This reduction of barriers to entry and engagement induces more stakeholders across the firm to congregate to the CMS project.

Scholars such as Wasmund [53] acknowledge the need for effective communication channels between manufacturers and consumers when identifying reusable assets. The need for communication and collaboration further increases due to conflicts that are bound to arise among various reuse stakeholders [45]. When offered, effective communication enables manufacturers and consumers to become conversant in others work and amicably resolve conflicts. As a boundary object, CMS offers manufacturers and consumers a viable communication channel to engage in the aforementioned boundary-spanning activities to develop reusable assets. Enhanced communication and collaboration in turn lead to greater organization-wide reuse as stakeholders across the firm are better able to resolve conflicts, asset producers are better able to keep abreast of consumers’ needs, and consumers are better able to participate in shaping reusable assets.

In essence, through its open infrastructure, CMS promotes participatory reuse. The potential for reusers’ participation afforded by a boundary object such as CMS could materialize from boundary-spanning activities such as requirements identification, change request submission, and bug reporting, among others. The concepts such as co-determination, democratization, and empowerment that participatory design brings to the fore [7] are equally germane to participatory reuse in CMS in strengthening the link between consumers’ participation and their reuse of the resulting assets. Further, it should be noted that the argument for the premise that greater reuser participation (e.g., sharing information) in a project could lead to greater reuse of the project’s resulting assets parallels the argument made in the software development literature where more user participation leads to applications that incorporate their requirements [10], which in turn results in greater use of these applications [24]. In CMS, participatory reuse emerges as more consumer participation manifesting in greater information sharing leads to assets that incorporate their reuse needs, which in turn results in the greater reuse of these assets.

Earlier, we theorized how CMS as a boundary object is able to leverage broader community skills. When stakeholders from a large number of divisions in the organization constitute the project’s membership, a wider audience will be aware of the project and resulting assets, which in turn enhances potential reuse of those assets. Moreover, because the CMS infrastructure affords an equal opportunity to personnel in all divisions in the organization to gain membership, CMS projects are likely to have greater diversity than closed source projects with members from a single department or division. As van Knippenberg et al. point out, such diverse groups representing a cross section of the firm are likely to “possess a broader range of task-relevant knowledge, skills, and abilities that are distinct and nonredundant” and “have different opinions and perspectives on the task at hand” [50, p. 1009]. The exposure to different perspectives brought about by group member diversity could in turn lead to greater creativity [11]. Jackson and Joshi further support this assertion in claiming that the “presence of diverse perspectives may also improve the team’s ability to consider alternative interpretations and generate creative solutions that integrate diverse perspectives” [27, p. 681]. Hence, in the IOS context, membership diversity could manifest in developing an assortment of novel assets that could be reused by the project’s constituents, some even in ways that were not initially envisioned by the project sponsors.

## Practical Implications

CMS is gaining tremendous popularity at IBM. The number of registered CMS projects increased from less than 200 in July 2005 to 1,461 in December 2008. The member counts (those who are registered for at least one CMS project) for the corresponding times are 3,000 and 10,494, respectively. Other organizations are also starting to realize the promise of IOS for enhancing organization-wide reuse (e.g., [12, 21, 39, 54]). Research to date has recognized its potential to advance reuse within the firm, but to our knowledge, no one has examined how collaboration among the organization-wide community of manufacturers and consumers and how information sharing among them affect reuse. Using a case study approach, we developed a theoretical model focusing on reuse. The model informs managers wishing to foster organization-wide reuse that they are wise to adopt IOS as a vehicle to promote greater openness of the software development infrastructure for leveraging broader community skills and enhancing information sharing among projects’ stakeholders.

As noted earlier, closed source that is marked by the presence of different infrastructures across manifold divisions in the firm hinders organization-wide collaboration. In contrast, IOS promotes collaboration among various stakeholders from the onset of the project. More important, it fosters participatory reuse by facilitating potential reusers participation in the entire development process leading to the creation of reusable assets that meet their needs. Research has shown that OSS participants’ interest at any given time affects project success in subsequent periods [48]. Hence, by adopting IOS, management could give interested parties, especially potential reusers, the opportunity to engage in the project from its infancy, thereby enhancing the likelihood of subsequent success more than an analogous closed source project that places impediments to organization-wide collaboration from the onset of the project.

While IOS facilitates greater openness, optimal reuse would be achieved when incentives are in place for the organization-wide community to share information and participate in development activities. Interviews reveal that although CMS projects are funded at the divisional level, incentives for participation mimic those of an OSS project. Regardless of who comes up with the idea for the asset, its growth would come based on the following of that asset. It was further revealed that over time, more individual consumers tend to participate in CMS projects even without direct management oversight when they foresee resulting assets’ potential for reuse in their existing assignments (i.e., participatory reuse).

## Research Implications

Our res earc h has implic ations to sc holars hip on OSS, IOS, and reuse. Much of the prior research has focused on why OSS project members reuse code (e.g., [23, 52]), but only a few have examined project-level antecedents affecting reuse (e.g., [19]). In this research, we show how two project-level factors—namely, information sharing and the breadth of community-wide membership—affect reuse of an IOS project’s artifacts. Although our research is confined to a single organization, we expect similar reuse gains in the OSS context. As Neus and Scherf [36] point out, greater participation and information exchange in traditional closed source development is often hindered by Brooks’s law [4], which can be summarized as “too many cooks spoil the broth,” whereas OSS defies it because of Linus’s law, “given enough eyeballs, all bugs are shallow” [38]. In applying this premise to the reuse context, greater participation and information sharing among those who hold a stake in the OSS project is likely to result in greater reuse of the resulting assets.

Although IOS’s potential to engender organization-wide reuse is acknowledged (e.g., [12, 13, 22, 39]), only Wesselius [54] explicitly studied reuse. He observed the need to provide incentives for both manufacturers and consumers for promoting organization-wide reuse. We draw from the boundary-spanning literature [49] to show how a boundary object such as CMS could promote greater openness of the software development infrastructure for leveraging the broader community skills and enhancing information sharing (e.g., boundary-spanning activities such as negotiating requirements), thereby advancing greater organization-wide reuse. While most IS research that appropriates boundary-spanning literature applies it to conventional knowledge transfer among an organization’s constituents (e.g., [31, 37]), our research is the first to apply this literature stream to knowledge transfer in the context of organizationwide reuse. Moreover, we are the first to introduce the concept participatory reuse to highlight the scenario evident in IOS where potential reusers participate in the entire development process leading to the creation of reusable assets that meet their needs.

Finally, our research in IOS has key implications for conventional research on organization-wide reuse. First, we show how IOS heeds the call for incorporating reuse into the software development process (see, e.g., [3, 9, 20, 33]). For example, IOS offers a platform for any potential consumer in the firm to provide input in shaping reusable assets, but at a much more open and grander scale than how end users get involved in requirement analysis in typical closed source development. Second, we show how IOS heeds the call for promoting avenues for communication and coordination among manufacturers and consumers. Research to date has largely focused on facilitating the relationships between top management and stakeholders affected by a reuse program while neglecting peer-to-peer coordination among asset manufacturers and consumers [45]. In taking a horizontal peer-to-peer view on reuse, Sherif et al. [45] highlight the need for coordination mechanisms for monitoring work processes (e.g., asset creation) and facilitating open communication among manufacturers and consumers in order to sustain a reuse program. IOS epitomizes the peer-to-peer coordination among asset manufacturers and consumers to promote reuse within an organization. IOS provides both a forum for stakeholders to monitor each other to ensure that they make decisions consistent with the welfare of the organization and facilities for communication among asset manufacturers and consumers spread across the firm.

## Limitations and Directions for Future Research

The ap roac h we took to inv es tigate the emerging IOS phenomenon has its merits, but there are certain limitations worth noting. These limitations in turn offer opportunities for further research. First, we studied a single company, albeit an industry leader in software development. Most prior studies have also reported single case studies investigating IOS in firms such as Hewlett-Packard [12], Lucent [21], Philip Healthcare [54], and SAP [39]. Future research should examine IOS endeavors in multiple organizations.

Second, although the case study approach provides rich insights into the phenomenon under study, qualitative empirical studies should be undertaken to reach more definitive conclusions. With the case study approach utilized in this study, we provided some initial support for how greater organization-wide reuse could be achieved by adopting IOS as a vehicle to promote greater openness of the software development infrastructure for leveraging broader community skills and enhancing information sharing among projects’ stakeholders. A qualitative empirical study would require data from closed source and IOS projects with varying degrees of openness, information sharing, and leverage of community skills.

Finally, only two antecedents of reuse emerged from the initial phase of the case study, which were then used to compile questions for the interviews. Future studies should broaden them to include possible other constructs such as consumers’ level of perceived ownership of the software being built, and how it affects their reuse. While those consumers who simply use the software ex post might not claim a stake in the software, those potential consumers who participate in various aspects of the IOS project (e.g., make change requests) could consider themselves part owners. Because of openness and transparency, IOS might offer manufacturers and consumers the potential for an equal say in the software being built. With possible equity in influence, the two parties could conceivably perceive themselves to be equal owners of the software. Literature reports that, compared to developers of closed source software, OSS manufacturers (i.e., developers) take greater ownership of the software being built [43]. However, there is little research examining consumers’ perceptions of ownership in OSS in general and IOS in particular.

Any future study to empirically test the theoretical model needs to precisely define metrics for various constructs. The “open infrastructure” represents a perceptual construct. A multiple-item scale needs to be developed with items such as “ease with which one could register for the project,” “ease with which one could make a change request,” and “ease with which one could access source code.” Possible metrics for assessing information sharing might include the number of general posts on the project Web site, change requests, defects reported, and code submits. Any metric for the leverage of a broader community skills construct needs to account for the project membership across divisions. Assuming $X _ { _ i }$ represents the number of participants from the ith division, the sum of the square root of X (or S √X ) represents a viable metric. Such a measure would give a higher score for projects that are able secure participation from a larger number of divisions. Last, an intuitive measure for the reuse construct is the number of other products using a particular project’s assets.

Research to date has mostly focused on how to promote organization-wide reuse by encouraging manufacturers to build assets that consumers could use. While significant strides have been made over the years, intraorganizational reuse has only been enhanced incrementally. IOS affords organizations an opportunity to achieve significant improvements in the creation of reusable assets. It does so by offering a powerful channel to facilitate participatory reuse by enabling potential consumers to themselves become manufacturers. Future research needs to incorporate the extent of consumers’ participation in the development of the reusable assets in order to fully gauge how IOS adoption fosters participatory reuse.

Acknowledgments: The authors thank the editor-in-chief, Vladimir Zwass, and the review team for constructive suggestions and guidance through the review process. The authors are indebted to the many employees at IBM who generously gave their time and insights. They also thank Kevin Crowston, Katie Stewart, and Eric von Hippel for their feedback on an earlier draft of the paper. This research was funded by a grant from the Earl V. Snyder Innovation Management Center at the Whitman School of Management, Syracuse University.

## Referenc es

1. Adams, P.; Boldyreff, C.; Nutter, D.; and Rank, S. Adaptive reuse of libre software systems for supporting on-line collaboration. Paper presented at the Fifth Workshop on Open Source Software Engineering, St. Louis, MO, May 17, 2005.

2. Ajila, S.A., and Wu, D. Empirical study of the effects of open source adoption on software development economies. Journal of Systems and Software, 80, 9 (2007), 1517–1529.

3. Apte, U. Reusability-based strategy for development of information systems: Implementation experience of a bank. MIS Quarterly, 14, 4 (1990), 421–433.

4. Brooks, F.P. The Mythical Man-Month. Reading, MA: Addison-Wesley, 1975.

5. Carlile, P.R. A pragmatic view of knowledge boundaries: Boundary objects in new product development. Organization Science, 13, 4 (2002), 442–455.

6. Carmel, E.; Whitaker, R.D.; and George, J.F. PD and joint application design: A transatlantic comparison. Communications of the ACM, 36, 6 (1993), 40–48.

7. Clement, A., and van den Besselaar, P. A retrospective look at PD projects. Communications of the ACM, 36, 6 (1993), 29–37.

8. Cockburn, A. The impact of object-orientation on application development. IBM Systems Journal, 32, 3 (1993), 420–444.

9. Davis, T. The reuse capability model: A basis for improving an organization’s reuse capability. Paper presented at the Second International Workshop on Software Reusability, Lucca, Italy, March 24–26, 1993.

10. Dean, D.L.; Lee, J.D.; Pendergast, M.O.; Hickey, A.M.; and Nunamaker, J.F., Jr. Enabling the effective involvement of multiple users: Methods and tools for collaborative software engineering. Journal of Management Information Systems, 14, 3 (Winter 1997–98), 179–222.

11. De Dreu, C.K.W., and West, M.A. Minority dissent and team innovation: The importance of participation in decision making. Journal of Applied Psychology, 86, 6 (2001), 1191–1201.

12. Dinkelacker, J., and Garg, P.K. Corporate source: Applying open source concepts to a corporate environment. Paper presented at the First International Conference on Software Engineering Workshop on Open Source Software Engineering, Toronto, May 12–19, 2001.

13. Dinkelacker, J.; Garg, P.K.; Miller, R.; and Nelson, D. Progressive open source. Paper presented at the 24th International Conference on Software Engineering, Orlando, FL, May 19–25, 2002, proceedings, pp. 177–184.

14. Economist. Open, but not as usual (March 16, 2006), 73–75.

15. Eisenhardt, K.M. Building theories from case study research. Academy of Management Review, 14, 4 (1989), 532–550.

16. Fafchamps, D. Organizational factors and reuse. IEEE Software, 11, 5 (1994), 31–41.

17. Fichman, R.G., and Kemerer, C.F. Incentive compatibility and systematic software reuse. Journal of Systems and Software, 57 (2001), 45–60.

18. Frakes, W.B., and Isoda, S. Success factors of systematic reuse. IEEE Software, 11, 5 (1994), 14–19.

19. Grewal, R.; Lilien, G.L.; and Mallapragada, G. Location, location, location: How network embeddedness affects project success in open source systems. Management Science, 52, 7 (2006), 1043–1056.

20. Griss, M.L. Software reuse: From library to factory. IBM Systems Journal, 32, 4 (1993), 548–566.

21. Gurbani, V.K.; Garvert, A.; and Herbsleb, J.D. A case study of open source tools and practices in a commercial setting. Paper presented at the International Conference on Software Engineering, Shanghai, May 15–21, 2006.

22. Gurbani, V.; Garvert, A.; and Herbsleb, J.D. A case study of a corporate open source development model. Paper presented at the 28th International Conference on Software Engineering, Shanghai, May 15–21, 2006.

23. Haefliger, S.; von Krogh, G.; and Spaeth, S. Code reuse in open source software. Management Science, 54, 1 (2008), 180–193.

24. Hartwick, J., and Barki, H. Explaining the role of user participation in information system use. Management Science, 40, 4 (1994), 440–465.

25. Hummel, O.; Janjic, W.; and Atkinson, C. Code conjurer: Pulling reusable software out of thin air. IEEE Software, 25, 5 (2008), 45–52.

26. Isakowitz, T., and Kauffman, R.J. Supporting search for reusable software objects. IEEE Transactions on Software Engineering, 22, 6 (1996), 407–423.

27. Jackson, S.E., and Joshi, A. Diversity in social context: A multi-attribute, multilevel analysis of team diversity and sales performance. Journal of Organizational Behavior, 25, 6 (2004), 675–702.

28. Kim, Y., and Stohr, E.A. Software reuse: Survey and research directions. Journal of Management Information Systems, 14, 4 (Spring 1998), 113–147.

29. LaBoda, D.M., and Ross, J.W. Travelers Property Casualty Corporation: Building an object environment for greater competitiveness. MIT Sloan School of Management Center for Information Systems Research (CISR) Working Paper Series no. 301, Cambridge, MA, 1997.

30. Lee, S.T.; Kim, H.; and Gupta, S. Measuring open source software success. Omega, 37, 2 (2009), 426–438.

31. Levina, N., and Vaast, E. The emergence of boundary spanning competence in practice: Implications for implementation and use of information systems. MIS Quarterly, 29, 2 (2005), 335–363.

32. Madanmohan, T.R., and De, R. Open source reuse in commercial firms. IEEE Software, 21, 6 (2004), 62–69.

33. Mellarkod, V.; Appan, R.; Jones, D.R.; and Sherif, K. A multi-level analysis of factors affecting software developers’ intention to reuse software assets: An empirical investigation. Information & Management, 44, 7 (2007), 613–625.

34. Meyer, B. Reusability: The case for object-oriented design. IEEE Software, 4, 2 (1987), 50–64.

35. Morisio, M.; Ezran, M.; and Tully, C. Success and failure factors in software reuse. IEEE Transactions on Software Engineering, 28, 4 (2002), 340–357.

36. Neus, A., and Scherf, P. Opening minds: Cultural change with the introduction of opensource collaboration methods. IBM Systems Journal, 44, 2 (2005), 215–225.

37. Pawlowski, S.D., and Robey, D. Bridging user organizations: Knowledge brokering and the works of information technology professionals. MIS Quarterly, 28, 4 (2004), 645–672.

38. Raymond, E.S. The Cathedral and the Bazaar. Sebastopol, CA: O’Reilly, 2001.

B.; and Odenwald, T. Open collaboration within corporations using software forges. IEEE Software, 26, 2 (2009), 52–58.

40. Seaman, C. Qualitative methods in empirical studies of software engineering. IEEE Transactions on Software Engineering, 25, 4 (1999), 557–572.

41. Seaman, C., and Basili, V. Communication and organization in software development: An empirical study. IBM Systems Journal, 36, 4 (1997), 550–563.

42. Shannon, C., and Weaver, W. The Mathematical Theory of Communications. Urbana: University of Illinois Press, 1947.

43. Sharma, S.; Sugumaran, V.; and Rajagopalan, B. A framework for creating hybrid-open source software communities. Information Systems Journal, 12, 1 (2002), 7–25.

44. Sherif, K., and Vinze, A. Barriers to adoption of software reuse: A qualitative study. Information & Management, 41, 2 (2003), 159–175.

45. Sherif, K.; Zmud, R.W.; and Browne, G.J. Managing peer-to-peer conflicts in disruptive information technology innovations: The case of software reuse. MIS Quarterly, 30, 2 (2006), 339–356.

46. Spinellis, D., and Szyperski, C. How is open source affecting software development? IEEE Software, 21, 1 (2004), 28–33.

47. Stewart, K.J., and Gosain, S. The impact of ideology on effectiveness in open source software development teams. MIS Quarterly, 30, 2 (2006), 291–314.

48. Subramaniam, C.; Sen, R.; and Nelson, M. L. Determinants of open source software project success: A longitudinal study. Decision Support Systems, 46, 2 (2009), 576–585.

49. Tushman, M.L., and Scanlan, T.J. Boundary spanning individuals: Their role in information transfer and their antecedents. Academy of Management, 24, 2 (1981), 289–305.

50. van Knippenberg, D.; De Dreu, C.K.W.; and Homan, A.C. Work group diversity and group performance: An integrative model and research agenda. Journal of Applied Psychology, 89, 6 (2004), 1008–1022.

51. von Hippel, E., and von Krogh, G. Open source software and the “private-collective” innovation model: Issues for organization science. Organization Science, 14, 2 (2003), 209–223.

52. von Krogh, G.; Spaeth, S.; and Haefliger, S. Knowledge reuse in open source software: An exploratory study of 15 open source projects. In R.H. Sprague (ed.), Proceedings of the 38th Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2005 (available at www.computer.org/portal/web/csdl/doi/10.1109/ HICSS.2005.378/).

53. Wasmund, M. Implementing critical success factors in software reuse. IBM Systems Journal, 32, 4 (1993), 595–611.

54. Wesselius, J. The bazaar inside the cathedral: Business models for internal markets. IEEE Software, 25, 3 (2008), 60–66.

55. Wu, C.; Gerlach, J.H.; and Young, C.E. An empirical analysis of open source software developers’ motivations and continuance intentions. Information & Management, 44, 3 (2007), 253–262.

56. Ye, Y., and Kishida, K. Toward an understanding of the motivation of open source software development. Paper presented at the Twenty-Fifth International Conference on Software Engineering, Portland, OR, May 3–10, 2003.

## Appendix: Interview Questions\*

## Reuse

1. Prior to launching Community Source (CMS), how extensive was reuse in your division in terms of development-for-reuse (DFR) and development-with-reuse (DWR)?

2. Prior to CMS, what were the challenges to reuse for both DFR and DWR?

3. H as CMS affected reuse in your division (both DFR and DWR)? If so, how?

4. Which aspects of CMS, if any, facilitate reuse?

5. Prior to CMS, in closed source projects, who were involved in identifying reusable artifacts?

6. In CMS projects, who are involved in identifying reusable artifacts?

7. Prior to CMS, to what extent were reusable assets shared among different product lines (i.e., divisions), such as WebSphere, DB2, Rational?

8. Since adopting the CMS model for internal development, to what extent are reusable assets shared among different product lines?

## Information Sharing

1. In closed source projects, what are typical challenges in information sharing among various stakeholders (e.g., user group, developer group, test group)?

2. When compared to closed source development, has the CMS approach changed the information sharing between different stakeholders? If so, how?

## Leveraging Broader Community Skills

1. In closed source projects, how are personnel selected for the project?

2. In CMS projects, how are personnel selected for the project?

3. In your view, is one particular (closed source versus CMS) development model better at forming project teams with individuals with the relevant expertise?

4. A re there any differences in cross-divisional participation between the two models?

\* When necessary, the interviewees were asked to elaborate on their answers.
