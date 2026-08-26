---
otero_id: 3378
otero_key: "CRYHJ4WB"
title: "Infrastructuring: Toward an Integrated Perspective on the Design and Use of Information Technology"
authors: "Volkmar Pipek; Volker Wulf"
year: "2009"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00195"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
5-28-2009

# Infrastructuring: T  oward an Integr   ated Perspectiv e on the Design and Use of Information Technology

Volkmar Pipek , volkmar.pipek@uni-siegen.de

Volker Wulf Fraunhofer-Institut für Angewandte Informationstechnik FIT and Universität Siegen, volker.wulf@unisiegen.de

Follow this and additional works at: https://aisel.aisnet.org/jais

# Jourņal of the Association for Information Systems JAIS

Special Issue

Infrastructuring: Toward an Integrated Perspective on the Design and Use of Information Technology\*

Volkmar Pipek Institute for Information Systems University of Siegen volkmar.pipek@uni-siegen.de

Volker Wulf Volker Wulf

Institute for Information Systems University of Siegen and Fraunhofer FIT volker.wulf@uni-siegen.de

## Abstract

In this contribution, we investigate how results from the ongoing discussion about e-Infrastructures can be used to improve the design of IT infrastructures in organizations. We first establish a perspective on organizational IT as work infrastructure that focuses on the infrastructural nature of organizational Information Systems and describe challenges for designing within and for this type of infrastructure. Then we elaborate on possible use of concepts from the e-infrastructure discussion, in particular on the concepi of infrastructuring as it was developed by Star and Ruhleder (1996) and Star and Bowker (2002). Using their “salient characteristics of infrastructure” we describe the methodological approach of Infrastructuring to develop methodological and toor support for all stakeholders' activities that contribute to the successful establishment of an information system usage (equivalent to a work infrastructure improvement). We illustrate our ideas by drawina on a case in which new work infrastructures are introducea into an organizational context and by mapping out existing and possible tool support for infrastructuring

Keywords: Infrastructure, Infrastructuring, Design, Software Development, Information Systems

# Infrastructuring: Toward an Integrated Perspective on the Design and Use of Information Technology

## 1. Introduction

In the fields of Computer Science and Information Systems, it is quite common to talk about infrastructure when describing either the multitude or diversity of hardware devices, software applications, and standards that modern organizations use in their everyday procedures, in general, or sometimes one specific but crucial software application, for example, an Enterprise Resource Planning system. In these approaches, the term infrastructure remains underdefined, and it is unclear whether the use of the term implies methods and perspectives other than the use of, for example, artefact, system, or network.

But a number of developments in organizational IT practices require us to take the issue of infrastructures more seriously. As the number of IT devices increases, they spread across more and more application fields (professional as well as private); wireless technologies keep them constantly connected to each other. Simultaneously, the sets of standards that guarantee a working network become more complex. At the same time, except for technological issues, IT support has become taken for granted in many professional and private use environments, and users and organizations have become dependent on a certain quality of service delivered by the IT they work with to such a degree that they prioritize the existing infrastructure over possible additional innovative applications.

In the field of Science and Technology Studies (STS), the term infrastructure has been used to highlight these aspects of Large Technological Systems (LTS), in particular, the role of standardization, dependencies, and emergence from a previous base: for example, Heinze and Kill (1988) on the German railway system, Hughes (1983) on the development of electricity infrastructures, or La Porte (1988) on the US Air Traffic System. Closer to the field of Information Systems, the emergence of the Internet itself has been studied, for example, by Abbate (1994). Focusing on a sociotechnical perspective (i.e., looking at physical entities as well as the role of actors), several conceptualizations have emerged (Hughes 1983, Star and Bowker 2002) that contribute to a better understanding of emergence, inheritance, and appropriation processes in Large Technological Systems.

The discourse of sociotechnical systems has, in general, a straightforward relation to the field of Information Systems. The contemporary network of interconnected devices — both visible (computers, etc.) and invisible (Internet backbone cables and routers, etc.) to users — easily qualifies in any definition as an infrastructure for individuals, organizations, and society as a whole. The sociotechnical perspective on their development matches the general understanding and methodology used in the IS field (Mumford 1987, March and Smith 1995, Hevner et al. 2004). But only a few IS approaches try to make use of concepts from the STS infrastructure discourse (Star and Ruhleder 1994, Hanseth et al. 1996, Ciborra and Hanseth 1998, Hanseth and Lundberg 2001, Bleek 2004, Karasti and Baker 2004). In this paper, we use STS concepts to develop a framework for designing organizational information systems that focuses on the role of IT as a work infrastructure.

## IT-Based Work Infrastructures

Modern work environments mainly use information systems as work infrastructures. We introduce this notion to highlight certain infrastructural aspects of information systems that we consider particularly relevant, while also connecting them with the STS infrastructure discussion:

Interconnectedness and complexity: even in simple cases, modern work environments deploy IT in many interconnected forms, including desktop computers, software (applications, databases, etc.), in- and output devices, servers, and IT-based communication facilities (IP telephony, mobile phones, etc.). Together with background devices, such as routers or name/domain servers within the organization and the general Internet infrastructure outside the organization, these devices form a network of networks that — however local its typical usage may be — remains connected with a global infrastructure.

Layer approach and standardization: to manage the complexity, a number of technology layers emerge (for example, local area networks, organizational intranets, national network infrastructures, the global Internet). These layers may be far removed from the worker's computer as an infrastructure outlet, yet may still have various immediate effects on the worker’s choices to proceed with her work. The layers interoperate by abiding to standards; while some standards (and transitions to new standards) remain in the background of the work environment (for example, moving from IPv4 to IPv6), others emerge in the user's foreground (for example, standards needed to synchronize data between contact databases on a desktop computer and a mobile phone).

(In-)Visibility in use: In most work environments, workers use the infrastructure all the time. Yet they rarely think about this fact once the IT devices and applications have become an integral part of the work practice. As long as the technologies serve their designated purposes, they remain invisible to the user, but when they fail, the interdependencies among work tasks and IT tools make the infrastructure failure a primary concern of workers.

The relevance of these features for IS design methodologies is only partially obvious. Design methodologies require designers to define a design scope (for example, a particular device or software artifact). Doing this requires defining what is internal (things to modify/design) and what is external (issues to consider) to a design process. Parts of the work infrastructure will be (and need to be) excluded from design, but the complexity of the work infrastructure makes this a difficult and error-prone process that may require corrections later. These decisions often remain implicit and are usually not part of a design methodology. Similar dynamics develop in the use of standards that define the technological fit between the newly designed devices/technologies and the existing technological base. Implicitly, designers decide which standards to ignore (as not relevant), consider (as they represent anchors for the new technology in the existing infrastructure), or newly integrate into the work environment (as they guarantee the functioning and/or expandability of a new technology). Corrections may be necessary for conceptual reasons (for example, incorporating stronger encryption standards due to changed risk considerations) or pragmatic ones (for example, because existing technologies do not fully comply with standards). The (in)visibility of a work infrastructure makes it hard for users to be fully aware of their own work procedures, making it difficult for designers to elicit requirements, and making it more likely that a technological solution will need several iterations of evaluation and design improvement before it is considered useful. On the other hand, technological failures may produce significant problems in work environments, making redesign an urgent issue for designers as well as users, and making visible (clarifying/raising awareness for) dependencies that were not previously salient.

This brief discussion makes clear that the term work infrastructure helps highlight aspects of design methodologies that have less to do with designers/developers and their design process, and more to do with how the technologies undergoing design, and the design process itself, are embedded in an existing work environment.

We believe information systems to be a very special type of infrastructure, with a set of problems and opportunities that cannot be found in traditional infrastructures. We can see work infrastructures that transport and distribute information as analogous to electric power grids or water supply systems. However, we consider the following characteristics specific to work infrastructures:

A unique versatility: The infrastructure can be used for many purposes in many work environments, and its success can be partly attributed to the ability to combine multiple purposes into one technology or tool even across spatial, professional and organizational boundaries that previously could only be spanned by using multiple tools.

Reflexivity: Information Systems as work infrastructure can be seen as reflexive in two ways. First, the IS work environments of designers are part of the same global infrastructure as those of users, and second, all improvements to the global infrastructure are developed within that infrastructure. More fundamentally, large and important parts of that infrastructure (i.e., software) can be processed within the infrastructure as information. This has beneficial consequences, such as the possibility for automatic improvements via software updates, and also problematic ones, such as infection by computer viruses.

IS design methodologies face a challenge in coping with these characteristics of work infrastructure. Versatility adds to the complexity issues mentioned above, but generally will not influence design methodologies in any direct way. Instead, it produces opportunities for technology users to modify and appropriate different parts of the infrastructure in ways unforeseen by its designers. A new tool in a work environment may be used in a way not intended by its designers, or users may choose to bypass a newly developed tool and use other available tools to achieve the same purposes. It remains a challenge to integrate both possibilities within design methodologies. Meanwhile, reflexivity affords new ways of organizing design. As work infrastructure, information systems present different possibilities for compromises between design-before-use and design-in-use than do most other types of infrastructures. It also permits forging different intersections between designers’ and users’ work environments. Recent trends such as user-generated content, end-user development, and Web 2.0 indicate that within the infrastructure, different and dynamic divisions of work are possible and useful in the development of information systems.

Here we appropriate concepts of infrastructure developed in the STS literature to highlight these two aspects of IS/work infrastructure, deploying them to help develop a framework for infrastructure aware design methods.

There are related approaches in the literature. Hanseth and Lundberg (2001) developed the notion of work-oriented infrastructures, meaning infrastructures that support a field of work in an organisation. They were also driven by an understanding of collaborative information systems as infrastructures, derived from an inspiring case study in a hospital’s radiology department. They provide the following basic recommendations for the design of work-oriented infrastructures:

users will inevitably reshape a new infrastructure during use, and should always be considered as “designers,”

new technological systems must carefully map all aspects of the artifact and activity chains of the old (and perhaps non-digital) infrastructure.

Consequently, Hanseth and Lundberg do not speak of information system design as the main process; instead they propose infrastructure improvement as the basic approach. We share their perspective, but we derive stronger methodological implications for design.

In the discussion that follows, we will subsume all activities that contribute to a successfu establishment of usages under the term “infrastructuring” to avoid confusion with classic notions of design as design-before-use performed by professional designers. To derive stronger methodological implications, we first elaborate on the theoretical background for our perspective. We then describe our framework and its terminology, and show some examples of how our framework helps in developing infrastructure-oriented perspectives on all activities in application fields that contribute to the successful establishment of a usage as well as examples of specific prototypes that respect an infrastructural perspective.

## 2. Organizational Information Systems between Design and Infrastructuring

The design of information systems for organizations has always confronted the infrastructural aspects of versatility and reflexity, which we described above. We now briefly outline the coping approaches inscribed in traditional design methodologies, as well as the discussions around infrastructure and information systems so far. We then revisit our construct of work infrastructure to refine the challenges our framework must answer.

## Coping With Infrastructural Aspects in Information Systems Design

As groundwork for our interpretation of informations systems as work infrastructure, we describe several infrastructural aspects of information systems in modern work environments: interconnectedness/complexity, layers/standardization, and invisibility during use. We also describe how design problems relate to these aspects: choosing which section of an existing infrastructure to modify during design (interconnectedness/complexity); organizing the relation between aspects interior to a design process and aspects outside by means of standardization (layers/standardization);

and finding out/managing current and potential relations between the technological entities and their use practice (invisibility during use).

The earliest approaches to organizing IT development marginalized these aspects, since the software crisis acknowledged in the late 1960s was perceived as a problem internal to the organization and systematization of software development. Most responses presented systematizing process approaches such as the waterfall model (Royce 1970). Later, failures in large software projects provided the impetus to develop design methodologies further.

## Incremental and Iterative Design Methodologies

After analyzing failed software projects, Boehm (1988) introduced risk management as an important factor for IT development methodologies and created an iterative approach that frequently revisited the design problem to ask whether the design activities still targeted the most relevant features of the work environment. Similar approaches developed with different notions (e.g., Floyd et al. 1989 with a focus on integrated user participation; Henderson, Sellers and Edwards 1990 with a focus on the object-oriented programming paradigm). Today we find refined methods with different strengths (for example, the process-centred Unified Software Process, Jacobson et al. 1999, and the more comprehensive and more formal Capability-Maturity-Model, CMMI, Paulk et al. 1995 and Ahern et al. 2001, which covers virtually all organizational aspects of IT development). The focus on the internal organization of the design process remains, but these methodologies dealt pragmatically with the design issues of the infrastructural aspects described above by frequently revisiting and revising basic decisions made earlier in the design process.

## Organizing User Participation

The second trend in IT development methods was to integrate the users in the design process so as to be able to identify and deal with potential conflicts and misalignments of the newly designed part of a work infrastructure with its existing technological and social environment. The integration approaches reach from (in a wider sense) ethnographic methods (for example, STEPS, Floyd et al. 1989; Use Cases, Jacobson et al. 1999; Contextual design, Beyer and Holtzblatt 1997, many approaches in Requirements Engineering, for example, Robertson and Robertson 1999) to approaches where users actually participate in design decisions (for example, Bødker et al. 2004). Also, user participation is a pragmatic approach to change design methodologies in order to manage issues of complexity and standardized interfaces between new and existing work infrastructure. Its approach of making users more aware of the technologies they use, and motivating them to contribute to the design process, also addresses the third infrastructural aspect “invisibility in use.” It also marks the step from a disconnected engineering perspective to a socio-technical perspective on IT development (in the spirit of — and at least in parts inspired by — Mumford (1987)).

## Supporting and Organizing Design-In-Use

With the third infrastructural aspect we described, a remaining practical problem is highlighted that could not be completely overcome by user participation: capturing and discussing projected usages. From a participating user perspective, this entails imagining and communicating technology usages where the actual use of a tool has sunk into the background of user considerations at use time. The work spheres of professional designers and potential users remain separated. On the one hand, in a participatory IT design process, the designers usually decide that it is “design time,” while the user has problems allocating time for an additional task within the daily work routine and explaining his expectations of unknown new work practices using new technology. On the other hand, when a certain technological improvement occurs to users during use, it is not necessarily “design time” for professional designers.

Approaches like STEPS (Floyd et al. 1989, and even more, its refinement “Integrated organizational and technology development” by Wulf & Rohde 1995) extended into the use phase iterations during the design process to answer this challenge, and replaced the traditional IS design notion that design precedes use with the notion that a finalization of the design happens in-use. Particularly in IT domains where the social aspects dominate the computational aspects of computer support — for example in collaboration-intense applications such as groupware — studies showed that it may not be appropriate to strongly enforce such a clear separation (Mackay 1990; Nardi 1993; Wulf and Golombek 2001). Therefore, Henderson and Kyng (1992) suggested a continuation of design in use in order to enable users to detect and configure relevant aspects of their work infrastructure. As a consequence, highly flexible information systems have been suggested to allow adaptation (tailoring) of technology to new or changing requirements at use-time (Henderson and Kyng 1992; Malone, Lai, and Fry 1992; Wulf, Pipek, and Won 2007). The discussion resulted in the paradigm of End-User Development (EUD) (Lieberman, Paterno, and Wulf 2006) where these approaches were merged with earlier research on adaptive computing or end-user computing. The question marks that remain in these approaches circle around issues such as the computer literacy of users and the time constraints under which users must perform in-use design.

## Infrastructural Challenges to IS Design

Through our account of the development of IS design methodologies, it becomes clear that these, indeed, can be interpreted as coping approaches to the infrastructural aspects of information systems. While the approaches show creativity and a variety of perspectives on IT design, they remain more a net than a solid fabric that captures and supports all aspects and activities relevant to establish successful IT usage.

In particular, these approaches take little account of the creativity of users. With an infrastructure perspective, the fringes of professional design come into focus. Based on our own experiences from long-term studies on collaborative information systems (Pipek and Wulf 1999, Törpel et al. 2003, Pipek and Wulf 2003) together with infrastructure-oriented studies from Hanseth 1996 and Hanseth and Lundberg 2001, we believe that the strict methodological separation of design and use represents a core problem of IS design. The term design may even be misleading, as it focuses on an artifact that should be designed, and neglects the surroundings into which the artifact is placed, which remain in focus when we discuss infrastructures.

The experience with Tailoring and End-User Development (Liebermann et al., 2006, Fischer 2002) showed that indeed, different degrees of technological expertise are involved in using and developing infrastructures. These are not permanently bound to certain professionalization structures, but can also emerge as normal users cope with infrastructural problems. Suchman (2002) analyzed problems in software development, particularly the structures of professionalization in design. In her eyes, professionalization often leads to assumptions and processes that do not respect the true nature of the design problem (from a user’s perspective) and that ignore potential alternative solutions. She pointed out that the phenomena of “design from nowhere” (professionals assuming a comprehensive ahistorical yet external perspective) and “detached intimacy” (professionals searching for skill development within their own community while maintaining a distance from their customer communities) should be considered as opportunities to develop new forms of collaboration between different spheres of professionalization that respect the “located accountabilities” of technology production and use. The principle of “artful integration,” which addresses the cultural production of new forms of material practice, is helpful since it accepts the necessity of and the support for “partial translations” (Suchman 2002). Artful integration shifts the view on knowledge from an objective, privileged, non-situated property of professional masters, toward one of multiple, located, partial perspectives supported by ongoing processes of negotiation. This crucial role of knowledge exchange and negotiation in design is echoed in the critical analysis of the CMMI of Nielsen and Kautz (2008).

Where traditional IT design approaches focus on the artifact, the skills of designers, the information interfaces and practices to be supported, and the effective organization of design work, the infrastructural aspects we described demand opportunities to renegotiate the border between what remains the same and what is changed when designing information systems; to renegotiate who changes aspects of information systems; and to renegotiate when these aspects are changed (before use vs. during use). Terminologies from the STS discussions around infrastructures provide approaches and terminologies that reflect these aspects.

## Infrastructure and Infrastructuring

There are several naïve approaches to understanding information systems as infrastructure. Tanenbaum’s (1996) description of computer networks or Dourish’s (1999) description of collaborative infrastructures serve as examples of a techno-centric understanding of IT infrastructures. These are often understood as organizational infrastructures without clarifying this concept sufficiently; the relationship between IT and organization has often been interpreted only as taking the opportunities IT offers as a starting point for organizational change (Crowston and Malone 1988). For instance, Shaw (2002) argued for the importance of the structure of technology for understanding the complexity and effects of changes to an organizational infrastructure, and provided a Technology Acceptance Model (TAM, Davis 1989; Venkatesh and Davis 2000). McGarty (1992) understood infrastructure resources to be shareable among users, common, enabling, physically embodied, enduring, scalable, and economically sustainable. Hanseth (1996) rightfully criticized such an understanding because it requires too much homogeneity; it is only suitable for closed systems; and it does not involve any non-technological aspects. In these approaches, infrastructure is treated as technology in context with organizational and societal aspects covered as context.

## Learning from the History of Infrastructures

As Van der Vleuten (2004) pointed out, interest in the structures that keep a society running developed as early as the 17<sup>th</sup> century, when (for example) Petty in his “Political Anatomy of Ireland” (1672) described tradesmen as playing “the role of veins and arteries” that nourish the organs of a national economy. Similarly, in military strategy a clear understanding of the value of stable, reliable transportation systems emerged that treated their management behind the lines as a key success factor (Ratzel, 1897, cited in Van der Vleuten, 2004).

In the 1980s a growing research interest in a combined analysis of the “social shaping of technology” and the “technological shaping of society” (Bijker 1995) resulted in a number of systematic treatments of infrastructure. Hughes (1983) analyzed the history of electricity infrastructures and identified as key factors system builders (who develop, implement and maintain a technological system) momentum (the inertial character of large technical systems, not easily shifted), load factor (ratio of average system output and maximum system output), and reverse salients (obstacles to further development of the infrastructure, such as bandwidth in the Internet). With regard to their emergence, Hughes (1987) distinguished the phases invention, innovation, technology transfer, growth, competition, and consolidation, during which different states and organizational settings (including actors) of a new infrastructure may be distinguished. Heinze and Kill (1988) described the emergence of the German railway system, distinguishing the phases “invention and isolated introduction” (local city links installed), “demand-oriented construction” (more cities integrated, usually in line with business interests), “supply-oriented extension” (almost all cities integrated as an act of national solidarity), and “maintenance-oriented cutback” (thinning out non-profitable routes, also considering competing infrastructures like roads). In his description of the US air traffic system, La Porte (1988) pointed out that the (non-)physicality of an infrastructure leads to additional degrees of freedom whose regulation needs to be negotiated and acknowledged by all actors (for example, air traffic routes). Some more recent research in Information Systems referred to the STS discourse under the topic of e-Infrastructures to improve our understanding of the processes of evolving technologica dependencies, for commercial (E-Business) as well as scientific (E-Science/Cyberinfrastructure) application environments (Star and Ruhleder 1996, Törpel et al. 2003; Atkins 2003; Finholt 2004; Karasti and Baker 2004; Karasti and Syrjänen 2004; Lawrence 2006; Ribes and Finholt 2007; Zimmerman and Finholt 2007; Edwards et al. 2007). These frameworks cover aspects of design, but do not usually account for the actual activities of the stakeholders involved. The discussions are certainly inspiring for reconceptualizing information systems in terms of infrastructure (see below), but the lack of a focus on activities makes it difficult to apply them as a foundation for design methodologies.

## 3. E-Infrastructures and Information Systems

In their analysis of a distributed information system that served a scientific community as a platform for archiving and exchanging data, Star and Ruhleder (1996, later rephrased in Star and Bowker 2002) described eight salient characteristics of infrastructure:

embeddedness in other social and technological structures;

transparency in invisibly supporting tasks;

spatial and temporal reach or scope;

the taken-for-grantedness of artifacts and organizational arrangements, learned as part of membership in a community;

infrastructures shape and are shaped by conventions of practice;

infrastructures are plugged into other infrastructures and tools in a standardized fashion, though they are also modified by scope and conflicting (local) conventions;

infrastructures do not grow de novo, but wrestle with the inertia of the installed base and inherit strengths and limitations from that base;

normally invisible infrastructures become visible upon breakdown.

This definition stresses socio-technical relations, in the sense that infrastructure should always be seen in relation to organized human “doing” and social systems. Its answer to the question "what is an infrastructure?" is whatever is perceived as infrastructure by its users. It also connects a global view of a widespread technological infrastructure with a local view of its use. Unlike other frameworks, it also covers aspects that relate to activities of users (“learned as part of membership” implies user learning about the infrastructure; “conventions of practice” implies user negotiations of conventions). It enables a connection between a perspective on infrastructures as developing phenomena (a macro view) and a perspective on infrastructures as embedded in and supporting networks of concrete activities (a micro view), thus opening up the opportunity to create a level playing field for addressing all actors and interests relevant for a successful establishment of an IS usage. We will later explore the potential of this definition to serve as a foundation for an infrastructure-oriented design approach.

Later, Star and Bowker (2002) used the same framework in a broader description of cases of information systems interpreted as infrastructure. Their title “How to infrastructure” stressed a focus on doing and led to the exploration of infrastructuring as a more comprehensive term for the creative design activities of professional designers and users (Karasti and Syrjänen 2004, Karasti and Baker 2004, Pipek and Syrjänen 2006), which we will continue in this contribution. Design implications of Star and Bowker's framework include the need for backward compatibility and modifiability, as well as the need for tentative, flexible, and open design processes and users who are aware of the political and social work an infrastructure is doing.

## 4. Underexplored Issues in E-Infrastructures

In an ICT-based infrastructure, an additional reflexive level is possible that traditional infrastructures could not provide. As Castells has repeatedly shown, information systems can form reflexive infrastructures, in the sense of tools that can mediate their own further development. The very ubiquity of information and communication allows e-infrastructures to provide representations of their inner workings as well as tools for discussing, negotiating and modifying them. (This describes more accurately, in our view, what makes Weiser’s 1991 vision of “ubiquitous computing” so important.) As the space for these tools and representations opens up, traditional competence/skill profiles and professionalization structures become more permeable. These both allow and require new methodological considerations (for example, with regard to different divisions of work between professional designers and users). With the concept of reflexive infrastructures, our discussion goes beyond the experiences described in the analyses of non-IT infrastructures.

## Work Infrastructures Revisited: The Design Challenge

We now develop our informal representation of “work infrastructure” in more detail. We briefly revisit infrastructure-oriented approaches in IS and define our understanding of work infrastructure, we clarify commonalities and differences with the infrastructure approaches in STS, and we present the design challenges we aim to meet.

## Definitions of Work Infrastructure

We don’t find many characterizations of infrastructure within existing IS approaches. Ciborra and Hanseth (1998) illustrate well the use of infrastructure in IS:

Managing an infrastructure to deliver effective information technology (IT) capability today means dealing with problems such as aligning strategy with IT architecture and key business processes (Henderson, Venkatraman and Oldach 1996); universal use and access to IT resources; standardization; interoperability of systems and applications through protocols and gateways; flexibility, resilience, and security. Ideally, infrastructure reconciles local variety and proliferation of applications and usages with centralized planning and control over IT resources and business processes (Hanseth 1996; Weill and Broadbent 1997).

From our point of view, the crucial question is: Who is involved in managing an infrastructure? While traditional IS thinking takes the management to be in charge of the organization of work, the discussion on e-Infrastructures deals with the complete innovation chain that brings infrastructure usages into effect. Obviously, there is need for and articulation of professional technological expertise and management within the creation processes of an infrastructure. However, there are also processes in between concrete product design, such as standardization issues, and processes of developing or discovering usages and their effects on individual end users as well as on the society as a whole.

Hanseth and Lundberg (2006) develop their understanding of work-oriented infrastructures from such an understanding of infrastructure:

When approaching information infrastructures we focus on four aspects. Infrastructures are shared resources for a community; the different components of an infrastructure are integrated through standardized interfaces; they are open in the sense that there is no strict limit between what is included in the infrastructure and what is not, and who can use it and for which purpose or function; and they are heterogeneous, consisting of different kinds of components – human as well as technological.

The authors treat ‘work-oriented infrastructures’ implicitly as supporting (collaborative) work, in their case, the work of a hospital’s radiology department.

A more elaborated conception of IS design in relation to infrastructures is presented by Hanseth and Lyytinen (2004). Their description of a design theory for information infrastructures focuses on the designer’s perspective in establishing an infrastructure. In contrast, we see the designer as one of many roles in an inevitable (and consequently not mainly design-driven) process of developing infrastructures that is driven by tensions resulting from infrastructure breakdowns and user innovation. In our view, an infrastructure-oriented perspective on IS design needs to focus on mapping actors and activities, to acknowledge their contributions to infrastructure development, and to describe the roles that can be identified with regard to methodological issues.

In our framework, the work infrastructure of a worker or organization is the entirety of devices, tools, technologies, standards, conventions, and protocols on which the individual worker or the collective rely to carry out the tasks and achieve the goals assigned to them. These elements are interconnected mainly in two ways: either in a technological sense that the functioning and utility of elements depends on other elements, or through use-based ties motivated by a shared interest of users or shared organizational aspect (work task, department, etc.). Dependencies may be transitive (see Pipek and Kahler 2006 for a more detailed discussion on use-based ties). While our general definition does not exclude non-IT devices, we consider IT devices and technologies to play a crucia role in the ensemble of tools and technologies. Consequently, workers are assumed to have a variety of skills related to using and improving work Information Technology infrastructure. Actors in processes of work infrastructure improvement may be professional IT designers, but basically we consider everybody involved in these processes to be actors who perform a deliberate, creative activity directed toward what they consider a lasting improvement. We also attribute to work infrastructure all of Star and Ruhleder’s (1996) characteristics of infrastructure. We now discuss some other dimensions specific to our perspective on work infrastructure.

## Differentiating Dimensions of Infrastructure

Several dimensions often attributed to infrastructure require further discussion here: issues of size/globalness/localness (work infrastructures may not be global, but on various levels of globalness), issues of longevity/sustainability (work infrastructures endure a long time in relation to the work tasks they support, but may still have a significantly shorter lifetime than classical infrastructures), and the issue of people as elements of infrastructure.

Infrastructure is often considered to be a large technology-shaped network structure of connections or channels, together with related devices, appliances, machines, or vehicles. But how important is large scale as a characteristic of infrastructure? Modern railway transportation networks, for example, span countries and even continents, but how important is that to a commuter who lives in Bonn and works in Siegen, about 60 miles away? How relevant is the continental scale for a company that plans to set up a transportation service between Bonn and Siegen? How relevant is sheer size for an engineer who aims to provide train-based mobile phone services along a track that has as many tunnels as the track between Bonn and Siegen? We believe that the concept of infrastructure remains useful regardless of the artifact’s sheer size. Describing the local transportation service between Bonn and Siegen as an infrastructure permits maintaining a perspective on work activities and environments with regard to the design of services as well as with regard to the train’s use (although, of course, there are indirect effects resulting from scaling issues). For some IT applications, it is often not quite clear whether they will be used as part of a large or a small infrastructure. An Internet browser may usually be employed to browse the global web, but it can also be used very locally, when browsing HTML documents located on the computer's own hard drive.

From address books, calendar databases, or reference libraries, we collect important information. These IT applications are small and local, yet they largely facilitate or hinder our orientation in the scientific work context and have become indispensable for our work. We also expect side artifacts such as calling cards, university department flyers, or paper hand-outs to be important for an efficient work organization. Here, small, local things make up a kind of Infrastructure less technological than cultural in nature. Nevertheless, depending on how taken for granted these cultural rituals are, they may become as significant as technological structures in a work environment. We believe that it is not the technology in itself that has to be large or global; rather it is the degree of customary, shared use that defines the level of globalness.

In addition, we can further question a techno-centric notion of infrastructure with regard to the mutual dependencies between the social and the technological spheres. As Hanseth (1996) described, the Clinton/Gore administration subsumed “people” within its plans for a National Information Infrastructure, to help in designing, configuring, and using it. It is obviously not absurd to consider people who help others to access and appropriate a technology as part of infrastructure. In work infrastructures, we often observe that users who specialize in certain technologies are regarded as technology experts by their colleagues (cf. Nardi 1993; Pipek and Wulf 1999). To a certain extent, these users (by dint of their education, training, communication skills, and experience) become “social infrastructures” in work settings, contributing significantly to establishing technology usages.

One other often mentioned aspect of infrastructures is the issue of longevity, stability, and sustainability (for example, Ribes and Finholt 2007; Zimmerman and Finholt 2007). While the Internet can undoubtedly be seen as an infrastructure that will last for quite some time, its material foundation has completely changed over the last 15 years. The changes regarding bandwidth and speed became relevant in organizations, for example, with respect to acceptable sizes of email attachments and website content. Local access points such as browsers and e-mail clients have changed little with regard to the basic functions they offer. However, what software companies and users consider to be their infrastructure to access the Internet may change quite frequently depending on extensibility or security concerns. This shows that in organizations, different layers of infrastructure may be connected with quite different expectations regarding durability, and that perceived stability at the level of users' experience is more important than the actual stability of network cables and other underlying devices.

## 5. A Framework for Infrastructuring

Improving work infrastructures is a creative activity that can be described as design. For the scope of this contribution, we understand design as any motivated, transformational activity that individuals or groups perform. Motivated means that every design activity has a goal or at least an intention. Transformational means that it induces a change that is intended to have a longer-lasting effect. Although for the scope of this paper, the changes we address refer to programming, configuring, and using collaborative infrastructures, we remain open with regard to other design domains.

We also use the term infrastructuring to distinguish ourselves from notions of design that only refer to professional, or to put it better, professionalized design activities. It is the degree of professionalization with regard to (technical) competencies that leads to the distinction between users and designers. Based on this distinction, traditional design methodologies in IS prioritize the designers’ perspective in a way that obstructs the perception of the users’ contributions to the improvement of infrastructures. However, the users’ perspective on developing IT infrastructure is actually broader. It includes the transition from old to new routines and usage patterns, and it is more diverse. While product-related choices in the application domain may seem straightforward to the designer, any organizational unit and any individual actor confronted with new systems has to find ways to integrate them into existing work practices. Thus, new functionality may only be partially perceived and integrated into users’ practices (for example, they get powerful new image manipulation software, but use it only to apply the “cancel red eye effect” function). Parallel usage of alternative technologies for the same purpose may develop, for instance keeping both an old and a new version of a program for compatibility purposes, or using different Internet browsers for private and business-related web surfing.

Sometimes, new usage patterns go beyond those intended by the designers. In a study on Lotus Notes, Orlikowski (1996) mentioned how call center staff used a commentary field in a helpline case management database for communicating about specific cases in a chat-like manner. These dynamics are addressed in the research about IT adoption or IT appropriation (Orlikowski 1992; DeSanctis and Poole 1994; Pipek and Wulf 1999; Pipek 2005), but they have rarely been captured on an activity level, which would be essential for integrating this research with IS design methodologies. In our view, the elaboration of the meaning of "infrastructure" in the research discussed above provides a good foundation for integrating designers’ and users’ choices in developing an organization’s information system. Taking the concepts of infrastructure and infrastructuring as defined above, we now develop an integrative perspective on activities that contribute to infrastructure improvement.

## Distinguishing Activity Spheres by Work Purpose

Although we want to put the classical design activities of professional designers and creative appropriation activities of users behind us, we do need to distinguish two related activity spheres. The first activity sphere (usually associated with users) consists of all creative activities leading to the improvement of an individual’s or an organization’s own work practice, regardless of the purpose or goal of the work. The second activity sphere revolves around the first, if they target the same work practice: it consists of all creative activities that contribute to the improvement of somebody else’s (individual or organizational) work practice, where this contribution is the main work purpose or goal. In Figure 1 these spheres are already specialized for information systems as work infrastructures: the lower half represents some organizational practice as the first activity sphere (called “work development activities”), while the upper half represents as the second activity sphere: the creative activities of professional designers aimed at improving the same organizational work practice.

## Distinguishing the Whens Of Design: The Point Of Infrastructure

The next consideration addresses the question: “When is design?”. Although we want to address all creative activities related to the successful establishment of a technology in use, there are different modes of awareness for these infrastructuring activities. As a demarcation line, we define the point of infrastructure as the moment when an infrastructure becomes visible to its users. Using the terminology from STS infrastructure discussions, we distinguish two reasons why this moment may occur: first, infrastructure breakdown, and second, the local resolution of a reverse salient (i.e., innovation). During a breakdown, the users experience an insurmountable incongruence between the expected infrastructure service and its actual or perceived behavior. The second point of infrastructure moment is a use innovation, when users successfully appropriate a new infrastructure for a local context. Star and Bowker (2002) describe this phenomenon as “resolving the paradox of demassification.” The opportunity offered by a global infrastructure is met with the creation of and decision to adopt a new local practice. It is important to note that a breakdown can be initiated either from the technology side (for example, when part of the technological infrastructure actually breaks) or from the work side (for example, when an infrastructure that had always served its purpose breaks because an additional, perhaps similar service is required that cannot be delivered.) The same applies to use innovations. These can occur either when the technical infrastructure changes, offering new opportunities, or when new requirements emerge from work activities that can be met with available technologies. It is important to note the subjectivity of our definitions: breakdowns may be only perceived, and an innovation as the local resolution of reverse salients simply represents the discovery of a usage that was already available within the technological system.

We consider these the two defining moments for the infrastructurer when she crosses the border from using to reflecting/modifying technology. This is the point of infrastructure when the routines of performing work meet the technology development activities of professional designers (see Fig. 1). From then on, the local development of infrastructure configuration and usage are considered as in situ-design or design-in-use, as opposed to design-before-use (Pipek and Syrjänen 2006).

## Distinguishing the Degree to Which Activities Are Targeted

From this perspective, we can identify layers of infrastructuring activities around that point of infrastructure. First, there is the in-situ design work of tailoring and configuring the infrastructure, and appropriating and negotiating the actual work, so that either the use innovation becomes manifest in usage or the obstruction caused by the breakdown is eliminated. Breakdowns temporarily generate a stronger implicit tie between the activity spheres, because the new awareness of the now-visible infrastructure results in a stronger sense of urgency regarding infrastructure improvements: the breakdown must be fixed, but how? While activities directed at this question go on, the infrastructure remains visible, but eventually it will sink again into the background of organizational practice. Even before this moment, however, there are relevant activities going on for some actors already engaged in developing or considering the technological infrastructure. We call these activities “preparatory design work.”

With regard to technology development activities, those that indicate an intention of usage (a concrete usage of the technology for work activities) belong to the category of preparatory design work. Those on the work side that indicate an intention of support (engaging technology to support a certain work activity) are preparatory work development activities. As the infrastructure becomes visible at the point of infrastructure, so do the activities that contributed to that point of infrastructure. Even before this, other relevant activities occur; these, which have neither an intention of usage nor an intention of support, we call “infrastructural background work”, which again can take place either in the technology development or the work development sphere (on the work activity side this is adaptive use of technology, as such. These activities have a more strategic nature, informed by issues that may have emerged from previous points of infrastructure (for example, the general need for more bandwidth).

Here the borderline especially between preparatory design work/preparatory work development and infrastructural background work is not very clearly defined. However, we believe that this terminology allows us to shed light on those activities relevant for successfully establishing the usage of an information system (either on the technology development side or on the work activity side) without accepting the designer/user dichotomy and the priorities it implies. Depending on the concrete case, a broader view of infrastructuring activities may be adopted, perhaps placing certain activities in the category of preparatory design work that would be considered infrastructural background work in other cases.

## Resonance Activities around Points of Infrastructure

While our framework describes a single point of infrastructure, it should be obvious that in any concrete work environment, points of infrastructure may show up repeatedly, perhaps even on a daily or weekly basis. Each point of infrastructure not only provokes in-situ design activities and makes visible prior preparatory activities, but also creates resonance activities involving observing and communicating aspects of what has become visible. These resonance activities may become part of the infrastructural background work (for example, when a breakdown illustrates the need for new, strong encryption methods or the preparatory work development or preparatory technology development of another point of infrastructure. Through resonance activities, the social appropriation of certain technology usages can be captured, and the relations between different points of infrastructure become clear.

## Toward Methodological and Tool Support for Infrastructuring

Our framework captures activities that are classically associated with users as well as those that are classically associated with designers in their relation with the point in time when they become relevant for the development of an IS infrastructure. In considering these activities, we can benefit from a located accountabilities (Suchman 2002) perspective: the main contribution to developing IT infrastructure comes from partial translations (Suchman 2002) between the different professiona worlds and different social and technological aspects that characterize these activities.

We have identified five groups of activities (six including the resonance activities) that contribute to the successful establishment of technology usages (background activities with regard to work development, background activities with regard to technology development, preparatory design work, preparatory work development and in-situ design work). A methodology of infrastructuring that would be equivalent to classical IS design methodologies needs to structure, moderate, and support these activities in a way that increases the fit between technology and organizational practice.

Once a point of infrastructure appears, we can recognize and distinguish the design-before-use activities that contributed to it. But design-equivalent methodologies need to help actors move toward improved satisfaction in an unknown future. In our view, infrastructuring activities inform a search for possible points of infrastructure that will evoke an improvement of work infrastructures. The metaphor of a search process also applies to ordinary IS design methodologies, and in both cases it is important that a convergence can be achieved.

In our suggestions for the operationalization of our framework, we try to inform this search process. IS design methodologies mainly aim at informing and structuring the designers’ work. While the designers' work practices may be regarded in our framework as preparatory design with an intention of usage that the designed product will support, the function of informing/structuring also regards the interaction between designer and user domains, and the interaction within the user domain. It is concerned with the questions: “When does the interaction take place?” and “What is the kind and depth of information exchanged?”

In the IS framework, these questions are methodologically answered by the designers, who define when they need information and what information they need. Our infrastructuring framework aims to add a user perspective to this, by

methodologically advising users to perform frequent procedures aimed at infrastructure improvement that may or may not involve technological reconfigurations or the introduction of new tools,

• providing methods as well as tools to systematically perform these procedures, and to

• prepare and engage in interactions with the traditional professional design sphere.

This may include meta-infrastructuring activities, for example, of users who seek additional qualifications (such as programming skills) in order to be more efficient at improving their own infrastructure.

Last, we propose a methodology that provides a variety of options for the shift in roles and collaborative relationships focusing on the improvement of a work infrastructure. It leads us beyond the traditional approaches to developing products toward a long-term perspective on developing work infrastructures.

## Operationalization for IS Analysis and Design

The framework aims to capture, plan, and support activities that contribute to the improvement of an IS infrastructure. Figure 1 describes a temporal structure that includes a notion of directedness of activities with regard to an intent to change, and a notion of integrating contributions from the professional design sphere as well as from the use sphere; but from a methodological perspective, we can only try to support a search process leading to the emergence of points of infrastructure. We now discuss how to identify activities as contributing to an improvement of infrastructure while they go on, not only post hoc. To operationalize our framework, we draw again on the infrastructure characteristics worked out by Star and Bowker (2002) and look for activities that change:

the embeddedness of infrastructures in other social and technological structures: activities that connect different technological and social structures, activities that change standards, routines, or traditions involved in mediating between different technological and socia structures;

• the transparency of invisibly supported tasks: activities that change the visibility of an infrastructure;

both spatial and temporal reach or scope: activities that increase the longevity of an infrastructure, or that add new members, elements, or application areas;

the taken-for-grantedness of artifacts and organizational arrangements learned as part of membership: activities that change, or reflect changes in, the community or communities being supported;

conventions of practice: activities that aim at changing conventional practices, or that impose existing practice on new technologies;

the way infrastructures are plugged into other infrastructures and tools in a standardized fashion, though they are also modified by scope and conflicting (local) conventions: activities that change standards that mediate between infrastructures (may also include activities that aim at local specializations of standards); activities that change the scope to which standards apply; activities that articulate or mediate conflicts;

the inertia of the installed base: activities that interface and align new applications with existing IT infrastructures: activities that challenge and develop existing practices;

the way infrastructures become visible upon breakdown: activities that help in articulating reasons for a breakdown; recovery activities after a breakdown.

We now will describe an illustrative case study and identify infrastructuring activities that would not be covered or supported by traditional IS design methodologies.

## 6. Infrastructuring: An Empirical Case Study

We illustrate our framework by presenting a long-term study about the introduction, appropriation, and removal of a groupware infrastructure in a German state government. We first describe the case and relevant activities that contributed to the shaping of the new infrastructure; as we will see, actors' interpretations of whether and how this shaping constituted "improvement" differed dramatically. We will then sort these activities with regard to the phases of our model and their impact on the work infrastructure.

## Setting and Case Description

The case study reported here took place in the government of a northern German state. The case is covered extensively in Pipek and Wulf (1999) and Pipek and Wulf (2006). In this contribution, we focus on work processes connecting the state government located in the state's capital with the Bundesrat. The Bundesrat is the second chamber of the German parliament, representing the 16 states. It is located in the federal capital, at that time in Bonn. The State Chancellery (SC) plays an important role within the state government. It channels information from and to the different state ministries. Within the State Chancellery, one organizational unit (a head and three employees) is responsible for coordinating the different state ministries vis-à-vis political decision making. The State Representative Body (SRB) is located in the federal capital. In the SRB about 30 people are occupied with representing the interests of their state in the federal legislative process. The SRB belongs to the State Chancellery, and is responsible for transferring documents and distributing information between the state government and the Bundesrat. We will provide detailed description of related work processes later.

Before the beginning of the project, the IT infrastructure consisted only of some PCs connected via a network, with the usual Microsoft Office™ software installed. These PCs were mainly used by typists and secretaries. The SRB had no IT department of its own; instead, the IT department associated with the SRB belonged to the State Chancellery in the state's capital, 700 kilometers away. When problems occurred, the SRB usually "borrowed" IT support from another state's Representative Body located in the same building.

The software development process was based on an off-the-shelf groupware application: LINKWORKS™ by Digital. It was introduced in both the government administration of the state and its SRB in the federal capital. The system offered shared workspaces, electronic circulation folders, email (including electronic document transport), and basic notification services.<sup>2</sup> Starting from LINKWORKS, the research institutes and the industrial partner participating in the research effort developed new system versions according to the specific requirements of the users. During the course of research, many qualitative methods were used for requirements elicitation and analysis (Pipek and Wulf 2006). The contact between researchers and the application field remained intense over almost four years, with at least bi-weekly meetings.

## Preparing for a Session of the Bundesrat

We will now describe the main work processes of the SRB in the federal capital as they existed at the beginning of the project. Aside from the core activity described here, other activities such as event organizing and writing press releases also involved groupware (for example, for collaborative text writing) at a later stage of the project. However, these activities will not be discussed here.

The main task of an SRB is managing the information flow between the federal and the state capital concerning legislative proceedings in the Bundesrat. The Bundesrat meets every three weeks to discuss and vote on an agenda of about 80 different issues. The SRB and specific sections of the State Chancellery and the state ministries cooperate in determining the state's vote on each of those issues. We distinguish four different, but closely connected work processes of the SRB as it prepares for a session of the Bundesrat.

The first work process is referred to as “Issue Distribution,” i.e., the distribution of material from the Bundesrat to the appropriate sections of the state government. Relevant material at the time of the study usually circulated as printed information, via internal as well as external courier services.

The second work process prepares the negotiation processes that leads to the state's vote. We call this “Vote Preparation” (cf. Figure 2). Two weeks before a meeting of the Bundesrat, its various commissions (for example the Commission for Internal Affairs) meet to discuss and vote on the different issues of the upcoming agenda. Any given issue is typically handled by several commissions. The state is represented in each commission by one SRB employee, typically the head of the corresponding SRB section. After the commision meetings, a personal protocol including main discussion points and results of test voting is hand-written by each section head and passed to a secretary for typing. This is followed by further correction and re-typing, until the result is satisfactory. Then, it is faxed to the corresponding state ministry. At the same time, a secretary of the Bundesrat writes an official protocol about each of the commissions' meetings and sends the paper document via the SRB to the corresponding state ministries. Within the commissions, each state ministry acts independently by means of the corresponding SRB section. To coordinate the different ministries' activities concerning each issue on the agenda, the SRB invented a coordination mechanism based on a form sheet.

For every issue, one section of the SRB takes main responsibility (issue leadership). The issue leaders create a hand-written form sheet on each issue for which they are responsible. They describe the issue and give a rough political judgment. They add the result of the test voting in the commission of the Bundesrat, for which they are responsible. Finally they state the names of other SRB sections whose commissions also deal with that issue. On the form sheet, they leave space for the other sections to add their comments and their commission's test vote. This form sheet is then typed and printed by a secretary, and re-checked by the issue leader, who then carries it to the heads of the other sections involved in order to get the result of their test votes. To reach the heads of each section, this process may require several attempts, since the section heads are quite often absent. Finally, all form sheets are handed to one section head, who is responsible for collecting and faxing them to the section of the State Chancellery responsible for coordinating the state's activities in the Bundesrat. The deadline for the arrival of these papers is always on the Tuesday before the Bundesrat meeting, which typically leads to heavy time pressure in completing the papers. The Chancellery uses the form sheets to survey the state of the political process and to catch any

inconsistent actions among the different ministries.

![](/api/attachments/CRYHJ4WB/fulltext/images/a4c3b854d21f8bb8ea784da88f6659ad6c0789fc5ccc8c8f09d1d38645498deb.jpg)  
Figure 2: Vote Preparation in the SRB

The third work process (Vote Negotiation) mainly takes place in the State Chancellery. The state's vote is now negotiated at the government level. Having identified possible conflicts among different ministries, the employees of the State Chancellery contact the conflicting ministries, identify the dissenters, and try to find a compromise. In the State Chancellery, the negotiation results are summarized for the state cabinet, which finally decides how to act on each issue (agree, disagree, abstain, or suggest a modification of the given issue proposal) in a meeting three days before the Bundesrat session. The results are then faxed to the SRB, where they are used to prepare the Bundesrat session (negotiation with other states, additional test votes, etc.).

The fourth process is the so-called “Session Preparation.” The day before the Bundesrat meeting, the modified proposals from the other states are sent to the State Chancellery and ministries.

## The Development of A Work Infrastructure

In the development of this work infrastructure, we roughly distinguish four phases: the introduction, use, removal, and re-introduction of the groupware. The introduction phase covered the analysis of the work processes and the identification of processes that should be improved with the help of the new tools. It also dealt with the installation of the groupware and related qualification processes. During the use phase, the organization gradually appropriated the new technological infrastructure. Activities during this phase included technological fine-tuning, adjusting to new external developments, discovering and implementing organizational innovations, and qualifying new users. The removal phase began with the decision to remove the groupware infrastructure, which took about three months. It included such activities as saving data and realigning work processes. During the reintroduction phase, a new groupware application was provided. This phase was similar to the introduction phase, but more strongly influenced by given expectations and experiences. Data had to be reintegrated and work processes aligned to the new system.

The introduction of groupware into the SRB started quite early, about three months after the project began. For the SRB, it was considered completed about 15 months later. The subsequent usage phase ended about three and a half years later, when the decision to remove it was made. The groupware application was uninstalled within three months, by December 1998. In 1999, after our research project ended, another groupware product was introduced.

We now describe several cases of infrastructuring activities that illustrate our framework.

## Cases of ‘Infrastructuring

In the following, we describe some cases of infrastructuring activities whose full creative potential would not be acknowledged in traditional IS development methodologies. We describe them using concepts from our framework. Since the goal of our framework is to suggest methods for supporting these activities, we also describe some methods derived from these examples that would, in our view, provide more comprehensive support for successfully establishing IT infrastructure usages in an organizational practice.

## Case 1: Using a Groupware Infrastructure

Our first example of a point of infrastructure is the use of a groupware infrastructure, after installing the first network computers outside the typing pool of the SRB. The project team elicited requirements and configured the groupware (which also included the development of smaller applications to integrate the groupware and the office software), using a traditional IS designer approach. These activities had clear intentions of usage (using groupware for document exchange and for process/workflow management) and were based on a web of ‘infrastructural background activities, for example, developing low-level communication protocols. But there were more activities worth considering in the application domain. The existing division of labor in document production (dictating and typing) and its associated infrastructure (recording machines, computers with text processing software, internal courier service) laid a foundation for making the usage of the groupware immediately beneficial (by dramatically increasing the speed of document exchange through sending electronic documents). Activities that involved SRB members as participants in the research project (i.e., enrolling them as ‘members of the group of groupware practitioners) also carried with them an intention of support, and required the stakeholders to reflect on the technological developments. Negotiation activities — which staff members participate in first, and how the data exchanges between the sections and the typing pool were organized (i.e., developing conventions of practice) — could be considered in-situ design.

We can describe this point of infrastructure to be the result of an infrastructure breakdown, since the typing pool had become an extreme bottleneck in the session preparation activities of the section heads. We could also describe it as a technology-induced use innovation.

Deriving recommendations for infrastructuring measures and support from this case, we suggest frequently asking interested users to reflect on interesting technological developments, and actively familiarizing them with the technologies their colleagues already use. We also suggest leaving room to negotiate the usage of a new technology even after it is introduced.

## Case 2: Innovating the Vote Preparation Process

The Vote Preparation process was improved through faster document exchange as well as fewer document exchanges (the section heads now performed minor text corrections themselves), but the main improvement came from parallelizing the previously sequential process of filling in the form. Neither the project members, who were involved in the requirements elicitation, nor the users themselves, after being informed about the features of the application, immediately recognized this potential for process innovation. During a site visit several months after the introduction, a project member and a section head discussed rather accidentally a stack of form sheets (see description of the Vote Preparation process) on the section head's desk. As a result of their discussion, they came up with the idea that the process of filling out the form sheets could be supported by the objectsharing feature of the groupware. They involved other section heads to discuss their idea and work out an electronically supported procedure.

In this newly developed usage, a document template representing the form sheet was stored in a public folder. The issue leader could copy it from there and fill it out for the specific issues for which she was responsible. She could enter her commission's test voting results and further comments. A link to the document was then sent via e-mail to all the other section heads involved in the issue. The recipients could enter the votes of their sections whenever they liked. Because the document was shared, it was not necessary to maintain a temporal sequence. After all sections contributing to an issue had entered their votes and comments, the issue leader sent a link to the completed form sheet via e-mail to the section head responsible for transferring the documents to the State Chancellery. So the “shared workspace” feature of the LinkWorks system enabled them to do away with the sequential order for filling in votes, which had been established in the previous, paper-based version of the Vote Preparation process. Nevertheless, additional conventions were needed to avoid a rush of document accesses as the deadline approached.

In this example, it is significant that the new infrastructure usage (which we could also classify as technology-induced use innovation) was the collaborative product of a software expert and a practice expert. Conceiving the idea required some technological skill, but also an intimate knowledge of the conditions surrounding the work process (for example, the increasing time pressure preceding vote submission). With the development of this usage, the groupware became an indispensable part of the organization's core practices.

Frequent meetings (inducing new group memberships) of design experts and practice experts were an important infrastructuring activity preceding this usage development. The practice of using a form for collecting the test votes also prepared them for the use of a shared document.

On a methodological level, we could suggest infrastructuring measures like establishing use reflection groups with mixed expertise or stimulating frequent considerations of coordination mechanisms like the form sheet to facilitate the conception of new infrastructure usages.

## Case 3: Discovering Individual Infrastructure Usages

The examples given so far have already shown different degrees of localness of infrastructure usages. We were also able to observe highly local or individual usage inventions.

During the introduction of the groupware infrastructure, many section heads were equipped with computers for the first time. The intention was to connect them to the groupware infrastructure, but there was no indication that the section heads were eager to use computers in other ways, especially text production. After the introduction of the groupware, more and more section heads found it convenient to make minor text modifications themselves, which did away with delays from the typists’ pool. Although it was each section head's individual decision (technology-induced use innovation) to engage more directly in text production, the effect was to reduce the number of typists from four to just one half position within three years. The new practice of text production spread through the demonstration and observation of technology usages. It is an example for (non-design) infrastructuring activities that manifest learning as part of membership. In our framework, these are also examples of resonance activities.

A similar case is the transformation of one user into a local system administrator. Based on the necessities of everyday practice, one staff member with a strong interest in information technology slowly familiarized himself with the configuration interface of the groupware, with some help from the project team members responsible for IT support. During the course of the project, groupware administration became an officially acknowledged part of his job description. This is an example of technology-centred learning as an important infrastructuring activity.

A third example of a (very) individual infrastructure usage is the story of the sole remaining typist. Confronted with a dramatic decrease of actors needing her expertise, she became afraid that she would lose her job. Although it was the official policy to share document templates necessary for the organization of work, she decided to store several templates in her personal workspace and to give them out only upon request. That way she hoped to secure her job; it also caused minor infrastructure breakdowns when she was on vacation.

The latter cases serve as examples of practice-induced use innovations. From an infrastructuringoriented design perspective, we would suggest measures that not only target the exchange of infrastructure usages, but also stimulate an assessment of the values of the stakeholders using the infrastructure.

## Case 4: Continued Usage Patterns

A striking and unusual experience in our case study was observing the complete removal of a software infrastructure. In the course of the research project, project members not only observed the developing infrastructure, but also provided support to keep the infrastructure running and to implement use innovations through technology. With the end of the project coming closer, the IT department of the SRB (being located in the State’s capital, about 700 miles away) was not able to provide support for the groupware infrastructure or maintain it. As a consequence, the groupware and the network infrastructure it used were removed.

One interesting problem in this situation was that the groupware product was not prepared for being removed. A fallback to a lower infrastructural level (here: the operating system) could only be performed through additional programming efforts to efficiently remove all files from the groupware database and store them at the operating system level.

Even more interesting were the changes undergone by the voting preparation process. The groupware removal constituted an infrastructure breakdown par excellence. However, the process structure, especially the parallel handling pattern developed in Case 2 (above), was sustained. The old, paper-based routine was not revived. Users started to use floppy disks with the voting form sheet instead of the document link that had been sent by email in Case 2. After the re-introduction of a second groupware product, the parallel handling pattern was implemented again, using a shared workspace.

This example impressively demonstrates that the strength of use patterns coined in practice and conventions may equal the strength of use patterns enforced through technology. To our eyes, this shows that applying an infrastructure perspective to IS requires an integral consideration of technological and social/organizational aspects of information systems.

Therefore, we suggest infrastructuring activities that involve the frequent reflection on strategies for an infrastructure fallback (returning to a lower and presumably more reliable infrastructural level in the case of an infrastructure breakdown) and means to express and collect usage documentation that would assist the re-establishment of usages based on new, but similar, technological systems.

## Additional comment: Failed anticipated usages

We learned in this case study that the successful establishment of a groupware tool as an enhancement of a work infrastructure cannot be fully credited to the efforts associated with classical IS design methodologies. Many important activities are marginalized by a traditional designer-centric perspective and are not acknowledged in their full creative potential by the adoption perspective.

A further indicator for the necessity of a comprehensive perspective is usages that were intended by the designers but never manifested in actual use practice. One example is the workflow management functionality in LinkWorks, considered very important in the initial requirements elicitation phase of the groupware system. However, this capability was never actually used, though the core processes of the SRB (see descriptions above) were easily describable in a formal language. It turned out that the rhythm enforced by the Bundesrat sessions had been so firmly integrated in the everyday practices of the SRB that additional technological support would not have created benefit worth the cost of modeling.

A second example was the group calendar functionality of the new groupware product introduced after the removal of the first one. Although it was one of the product's main selling points and prominent on the agenda of the introductory workshop where users learned about the product, it was never used much in practice. The effort expended on training for the second groupware introduction was only a fraction of that invested during the first introduction, because the management decided to rely on the use experiences gathered from the previous product. However, they did not cover the use of a group calendar.

This finding stresses the necessity for bridging the gap between technology design and appropriation. With the infrastructuring framework, we were able to capture these activities.

## 7. Further Aspects of Infrastructuring in Practice

We have developed a perspective that regards information systems as work infrastructures. This allows us to apply conceptualizations from the research on e-Infrastructures to the design and adoption of information systems. Our ultimate goal is to inform actors in the process of developing an organization’s infrastructure about methods that acknowledge all the necessary contributions of the various actors involved. While it will take more case studies to refine our approach, we can draw on earlier research on affordances and appropriation support to further develop ideas for supporting infrastructuring activities.

## The Design of Everyday Infrastructures

A focal point of our framework is the point of infrastructure, where the activities of professional design and continuous re-conceptualizations of possible uses in the application domain result in activities to discover or develop new infrastructure usages that may or may not involve technological changes. This point of infrastructure is always local, and the accessibility of an infrastructure for usage detection or for usage development is significantly influenced by the way it is presented to possible users. In his popular book, The Design of Everyday Things, Norman (2001) surprisingly (or maybe not) presented a lot of design examples that show user interfaces to infrastructures, such as water faucets, light switches, door handles, and button controls on various electronic devices, to illustrate rules for good design. He also discussed visibility and standardization as design aspects, naturally from a slightly different angle than our own. Visibility relates to “traceability” of the inner workings of an infrastructure in case that is necessary for its correct use. Standardization also relates to an artifact’s use (through a standardized user interface) in case an infrastructure cannot be cloaked into existing use traditions.

However, Norman’s (2001) discussion revealed an important difference between information infrastructures and classic infrastructures. The handles that he described remain simple, no matter how complicated the use situation gets. The interfaces presented offer support and affordances for use situations, they do not provide support in breakdown situations, and they do not, in themselves, provide means to stimulate use innovations. The partly virtual nature of software infrastructures makes it possible to provide simple interfaces for use, but also additional, more complex interfaces to support infrastructuring activities. This nature also allows a development of information infrastructures in much smaller and maybe also more local and more divergent steps, consolidated by negotiations for standardization that are necessary to establish a shared use. These negotiations would also be part of the infrastructuring activities we consider. We now give some examples for technical support of infrastructuring activities from our research.

## Beyond Theorizing: Technological Support for ‘Infrastructuring

In earlier work, we developed (software) appropriation from an analytical concept describing phenomena of technology in use to a concept that covers activities users perform in order to make sense of technology. The activity-centric interpretation of appropriation allowed us to identify and classify possible support infrastructures for appropriation activities (Pipek 2005):

Basic technological support: Building highly flexible systems,

• Articulation support: Support for technology-related articulations (real and online),

Historicity support: Visualize appropriation as a process of emerging technologies and usages, for example, by documenting earlier configuration decisions, or providing retrievable storage of configuration and usage descriptions,

Decision support: If an agreement is required in a collaborative appropriation activity, voting and polling needs to be provided,

Demonstration support: Support showing usages from one user (group) to another user (group), provide necessary channels of communication,

• Observation support: Support the visualization of (accumulated) information concerning the use of tools and functions in an organizational context.

Simulation support: Show effects of possible usage in an exemplified or actual organizationa setting (makes sense only if the necessary computational basis can be established),

Exploration support: Combination of simulation with extended support for technology configurations and test bed manipulations, individual vs. collaborative exploration modes,

Explanation support: Explains reasons for application behavior, fully automated support vs. user-user or user-expert-communication,

• Delegation support: Support delegation patterns within configuration activities; provide remote configuration facilities,

• (Re-) Design support: feedback to designers on the appropriation processes.

In our infrastructuring framework, these support options could be beneficial for both preparatory work development activities and in-situ design activities. Technological support for preparatory technology development activities is one of the classical domains within software engineering (e.g., Integrated Development Environments such as IBM’s Eclipse platform). The support options also strongly support resonance activities within work development activities. Re-design support also describes a very specific infrastructure for resonance activities, as it creates a permanent bridge between the technology development side and the work development side around a specific infrastructure in which support functionality is embedded.

All the supported activities are not covered by traditional IS design methodologies. We will now provide some examples of technical support for infrastructuring that all relate to the idea of embedding platforms for user communities and user collaboration within the IS infrastructure. The examples also help to prepare representations of IS infrastructures that allow easy articulation of issues regarding current practice and possible modifications to the infrastructure.

## Use Discourse Environments

We developed the concept of use discourse environments to support users in negotiating the configuration of the software infrastructures they use. The main ideas were to:

provide users with a communication platform embedded in the infrastructure they use (for example, a discussion forum),

provide means to easily articulate and visualize issues around using and configuring the infrastructure (for example, by providing representations of the software used and support for annotated screenshots),

provide means to organize these communication and negotiation processes (for example, by providing voting support and process visualizations).

Use discourse environments support preparatory work development activities and in-situ design activities and build a platform for resonance activities. We implemented the concept in two prototypes and evaluated it in real organizations (Pipek 2005). The support for articulation, demonstration, negotiation, and exploration activities was well accepted, and partially resulted in use discourses that went beyond the software infrastructures in which the concept was embedded. In our framework, we would classify these activities as infrastructuring with a preparational or an in-situ design character, altering the infrastructure characteristics that relate to conventions of practice and membership.

## ChiC – Community Help in Context

Stevens and Wiedenhöfer (2006) presented a concept to provide similar support for the case of an infrastructure breakdown. Based on the assumption that users press the F1-key when the work infrastructure does not deliver an expected service, they provided a wiki-based help system where users could modify and extend help descriptions provided by the software manufacturer. This made it possible to customize the help descriptions to reflect local usage. Together with a guiding context model, this idea delivered articulation, demonstration, exploration, and explanation support. This functionality can support in-situ design activities, preparatory work development activities, and resonance activities, and also preparatory technology development activities if technology developers get access to the (possibly confidential) information.

## Infrastructure Probes

Based on the concept of Cultural Probes (Gaver et al. 1999), we developed the concept of infrastructure probes (Dörner et al. 2008). A toolkit for self-documentation of infrastructure usages allows users to record the virtual tools at the workplace (using a software snapshot tool and an infrastructure-embedded wiki to document actual or envisioned infrastructure usages), as well as to document real parts of the work infrastructure such as spatial arrangements or constraints that shape local infrastructure usages (by means of a digital camera and stickers to annotate work environments). The probes made it possible to support infrastructuring activities involving narratives about real breakdowns or use innovations. The tools could be a valuable mediator between IT-based and non-IT-based aspects of a work infrastructure. They obviously support resonance activities, but also preparatory work development activities and in-situ design activities.

While these approaches aim to support infrastructuring activities on the user side, they could easily be extended to integrate other actors such as professional designers.

## 8. Conclusion

Traditionally, design methods in IS have focused on developing individual products, accompanied by measures to embed them into existing technological and the social environments where these products will be adopted. These methodologies focus on the development of technology, but miss many activities and decisions that need to be performed in the application domains.

Research on e-Infrastructures provides interesting concepts to overcome the traditional distinction between IT design and IT adoption. A perspective that focuses on the improvement of an organization’s infrastructure, not of specific individual products, offers the potential to integrate multiple social and technological layers. Such a perspective allows one to acknowledge the contributions from designers of information technology as well as from innovators of technologyenhanced practices. We identified Star and Ruhleder’s eight characteristics of infrastructure as an important framework that can guide infrastructure development through a holistic approach.

In our account of technology development methodologies, we described deficiencies having to do with infrastructural aspects of modern information systems. Their complexity, their dependency on standardized interfaces between the interior and the exterior of a design process, and their invisibility in use complicate design approaches focused only on the activities of professional designers.

In organizational settings, we cannot understand or improve infrastructures without integrating creative activities of the ordinary user. Inspired by Star and Bowker’s article “How to Infrastructure,” we followed the impulse to look at the activities that make infrastructure improvements happen in order to conceive methodological and tool support for them. Infrastructuring, understood as reconceptualizing one's own work in the context of existing, potential, or envisioned IT tools, is a natural part of every user’s activities. Large subsets of these activities are not delegable to some management level or the next professional design process. Consequently, infrastructuring activities should be addressed in IS design frameworks to capture the complete chain of innovations that help to establish successful technology usages.

The necessity for a broader perspective on design has been acknowledged in other fields of product development, as well (von Hippel and Katz, 2002; von Hippel, 2005). However, in the domain of information technology, our perspective offers a unique opportunity. Software, as the most important fabric of information infrastructures, is versatile to the extent that it can support the actual use as well as activities that bridge between design and use. The semi-material nature of software makes it less dependent on physical and spatial constraints. It allows building a rich variety of user interfaces that, in turn, allow different, more flexible divisions of labor. So software offers an interesting opportunity to overcome the traditional dichotomy between professional designers and users.

Information and software are quite unique infrastructural materials. Their versatility to support their use as an infrastructure as well as almost all meta-activities of infrastructuring results in new approaches to integrate use, maintenance, and design. In our view, it is a crucial task for IS as a scientific discipline to capture and exploit these infrastructural opportunities. The concept of infrastructure may also become an important boundary object in overcoming the gap between the analytical and the design-oriented schools of thinking within the IS community, as addressed by Hevner et al. (2004).

In addition to these considerations, studying information systems through an infrastructure perspective presents new questions and challenges to the field of Science and Technology Studies (where the foundations for our ideas were developed). Unlike other types of infrastructure, information infrastructures have reflexive characteristics: they can be used in their own (re)design. In addition to their interesting potential for Infrastructuring support, information systems can be compared with earlier infrastructures, offering a perspective from which to revisit the relation between infrastructura and societal change (Van der Vleuten 2004).

## Acknowledgements

We would like to thank the anonymous referees for their helpful comments, as well as the colleagues who contributed valuable discussions to this research, especially Helena Karasti, Gunnar Stevens, Anna-Liisa Syrjänen, and Torben Wiedenhöfer. We also thank Paul N. Edwards and Geoffrey C. Bowker for extensive editing of the manuscript.

## References

Ahern, D. M., Clouse, A. and Turner, R. (2001) CMMI distilled: An introduction to multi-discipline process improvement. Addison-Wesley.

Atkins, D. E. C. (2003) Revolutionizing Science and Engineering Through Cyberinfrastructure: Report of the National Science Foundation Blue-Ribbon Advisory Panel on Cyberinfrastructure. National Science Foundation, USA.

Beyer, H. and Holtzblatt, K. (1997) Contextual design: Defining customer-centered systems. Morgan Kaufmann.

Bijker, W. (1995) Sociohistorical technology studies. In Handbook of science and technology studies (Jasanof, S., Ed), pp 229-256, Sage, London, UK.

Bleek, W.-G. (2004) Software infrastructure. Hamburg University Press, Hamburg, Germany (available only in German).

Bodker, K., Kensing, F. and Simonsen, J. (2004) Participatory IT design: Designing for business and workplace realities. MIT Press, Cambridge, MA. USA.

Bowker, G. C. and S. L. Star (1999) Sorting Things Out: Classification and its consequences: MIT Press.

Ciborra, C. U. and O. Hanseth. (1998) “Towards a Contingency View of Infrastructure and Knowledge: An Exploratory Study.” Int. Conf. on Information Systems (ICIC'98), Helsinki, Finland, 1998, pp. 263-272.

Crowston, K. and T. W. Malone (1988) “Information Technology and Work Organization,” in M. Helander (Ed.) Handbook of Human Computer Interaction, Amsterdam: Elsevier, pp. 1051- 1069.

Davis, F. D. (1989) "Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology," MIS Quarterly (13) 3, pp. 319-339.

DeSanctis, G. and M. S. Poole (1994) "Capturing the Complexity in Advanced Technology Use: Adaptive Structuration Theory," Organization Science (5) 2, pp. 121-147.

Dörner, C., J. Heß, and V. Pipek. (2008) “Fostering user-developer collaboration with infrastructure probes”. In: Proceedings of the Workshop on Collaborative and Human Factors in Software Engineering (CHASE'08) at the International Conference on Software Engineering (ICSE'08), pp 44-48, ACM, New York, NY

Dourish, P. (1999) “Software Infrastructures,” in M. Beaudouin-Lafon (Ed.) Computer Supported Cooperative Work: John Wiley & Sons, pp. 195 219.

Edwards, P., S. Jackson, G. C. Bowker, and C. Knobel. (2007) Understanding Infrastructure: Dynamics, Tensions, and Design: Report of a Workshop on History & Theory of Infrastructure: Lessons for New Scientific Cyberinfrastructures. University of Michigan, School of Information, Ann Arbor, MI, USA.

Finholt, T. A. (2001) Collaboratories, In B. Cronin (Ed.) Annual Review of Information Science and Technology. Washington, DC: American Society for Information Science and Technology, 2001, 73--108.

Fischer, G. (2002) "Beyond 'Couch Potatoes': From Consumers to Designers and Active Contributors," FirstMonday (Peer-Reviewed Journal on the Internet) (7) 12.

Floyd, C., F.-M. Reisin, and G. Schmidt. (1989) “STEPS to Software Development with Users.” 2nd Europ. Conf. on Software Engineering (ESEC'89), Coventry, UK, 1989.

Gaver, B., T. Dunne, and E. Pacenti (1999) "Cultural Probes," interactions (6) 1.

Hanseth, O. (1996) Information Technology as Infrastructure. PhD Thesis, University of Gøteborg, Sweden.

Hanseth, O., Monteiro, E. and Hatling, M. (1996) Developing information infrastructure: The tension between standardization and flexibility. Science, Technology & Human Values 21 (4), 407- 426.

Hanseth, O. and N. Lundberg (2001) "Designing Work Oriented Infrastructures," Computer Supported Cooperative Work: The Journal of Collaborative Computing (10) 3-4, pp. 347–372.

Heinze, G. W. and Kill, H. H. (1988) The development of the german railroad system. In The development of large technical systems. (Mayntz, R. and Hughes, T. P., Eds), pp 105-134 Westview Press, Boulder, CO, USA.

Henderson, J. C., N. Venkatraman, and S. Oldach (1996) “Aligning Business and IT Strategies,” in J. Luftman (Ed.) Strategic Alignment, New York, NJ, USA: Oxford University Press.

Henderson Sellers, B. and J. M. Edwards (1990) "The object-oriented System Life Cycle," Communications of the ACM (33) 9, pp. 143-159.

Hevner, A. R., S. G. March, J. Park, and S. Ram (2004) "Design Science in Information Systems Research," MIS Quarterly (28) 1, pp. 75-105.

von Hippel, E. and R. Katz (2002) "Shifting Innovation to Users via Toolkits," Management Science (48) 7, pp. 821-833.

von Hippel, E. (2005) Democratizing Innovation. Cambridge, MA, USA: MIT Press.

Jacobson, I., Booch, G. and Rumbaugh, J. (1999) The unified software development process. Addison-Wesley.

Karasti, H. and K. S. Baker. (2004) “Infrastructuring for the Long-Term: Ecological Information Management.” 37th Hawaii International Conference on System Sciences (HICSS 2004), 2004.

Karasti, H. and A.-L. Syrjänen. (2004) “Artful Infrastructuring in two cases of community PD.” Participatory Design Conference (PDC'04), Toronto, Canada, 2004, pp. 20-30.

Lawrence, K. A. (2006) "Walking the tightrope: The balancing acts of a large e-Research project," Journal on Computer Supported Cooperative Work (JCSCW) (15), pp. 385-411.

La Porte, T. R. (1988) The united states air traffic system: Increasing reliability in the midst of rapid growth. In The development of large technical systems. (Mayntz, R. and Hughes, T. P., Eds), pp 215-244, Westview Press, Boulder, CO, USA.

Lieberman, H., F. Paternó, and V. Wulf (eds.) (2006) End User Development, Berlin, Germany: Springer.

Mackay, W. E. (1990) Users and customizable Software: A Co-Adaptive Phenomenon. PhD Thesis, MIT, Boston, MA, USA.

Malone, T. W., K.-Y. Lai, and C. Fry. (1992) “Experiments with Oval: A Radically Tailorable Tool for Cooperative Work.” Int. Conference on CSCW (CSCW'92), Toronto, Canada, 1992, pp. 289- 297.

March, S. T. and Smith, G. (1995) Design and natural science research in information technology. Decision Support Systems 15 (4), 251-266.

McGarty, T. (1992) “Alternative Networking Archtectures: Pricing, Policy, and Competition,” in B. Kahin (Ed.) Building Information Infrastructure, New York, NJ, USA: McGraw-Hill.

Mumford, E. (1987) Sociotechnical systems design: Evolving theory and practice. In Computers and democracy (Bjerknes, G. and Ehn, P. and Kyng, M., Eds), pp 59-76, Avebury, Aldershot, UK.

Nardi, B. A. (1993) A small matter of programming. Perspectives on End-User Programming. Cambridge, Massachusetts: MIT Press.

Nielsen, P. A. and Kautz, K. (Eds.) (2008) Software process & knowledge: Beyond conventional software process improvement. Software Innovations Publisher, Aalborg, DK.

Orlikowski, W. J. (1992) "The Duality of Technology: Rethinking the Concept of Technology in Organizations," Organization Science (3) 3, pp. 398-427.

Orlikowski, W. J. (1996) “Evolving with Notes: Organizational change around groupware technology,” in C. U. Ciborra (Ed.) Groupware & Teamwork, Chichester: Wiley, pp. 23 - 60.

Paulk, M. C., Weber, C., Curtis, B. and Chrissis, M. B. (1995) The capability maturity model: Guidelines for improving the software process. Addison-Wesley, Reading, MA, USA.

Pipek, V. (2005) From Tailoring to Appropriation Support: Negotiating Groupware Usage. PhD Thesis, University of Oulu.

Pipek, V. and H. Kahler (2006) “Supporting Collaborative Tailoring,” in H. Lieberman, F. Paterno, and V. Wulf (Eds.) End-User Development, Berlin, Germany: Springer, pp. 315-346.

Pipek, V. and A.-L. Syrjänen. (2006) “Infrastructuring as Capturing In-Situ Design.” 7th Mediterranean Conference on Information Systems, Venice, Italy, 2006.

Pipek, V. and V. Wulf. (1999) “A Groupware's Life.” European Conference on Computer Supported Cooperative Work (ECSCW'99), Copenhagen, Denmark, 1999, pp. 199-218.

Pipek, V. and V. Wulf. (2006) “Appropriation and Re-Appropriation of Groupware: Theoretical and Practical Implications of a Long-term Case Study“. IISI International Reports on Socio-Informatics (IRSI), Vol. 3 Iss. 1.

Ribes, D. and T. A. Finholt (2007) “Tensions across the Scales: Planning Infrastructure for the Long-Term.” Proceedings of ACM Group 2007, 2007, pp. 229-238.

Robertson, S. and Robertson, J. (1999) Mastering the requirements process. Addison Wesley.

Royce, W. W. (1970) Managing the development of large software systems: Concepts and techniques. In Proceedings of WesCon, IEEE Computer Society Press, Los Alamitos, CA, USA.

Shaw, N. G. (2002) "Capturing the Technological Dimensions of IT Infrastructure Change: A Mode and Empirical Evidence," Journal of the Association for Information Systems (JAIS) (2) 8.

Sommerville, I. (2007) Software Engineering, 8th edition: Addison Wesley.

Star, S. L. and G. C. Bowker (2002) “How to infrastructure,” in L. A. Lievrouw and S. Livingstone (Eds.) Handbook of New Media - Social Shaping and Consequences of ICTs, London, UK: SAGE Pub., pp. 151-162.

Star, S. L. and K. Ruhleder (1996) "Steps Towards an Ecology of Infrastructure: Design and Access for Large Information Spaces," Information Systems Research (7) 1, pp. 111-134.

Stevens, G. and T. Wiedenhöfer. (2006) “CHIC - a pluggable solution for community help in context.” Proceedings of the 4th Nordic Conference on Human-Computer interaction: Changing Roles (NordiCHI '06), Oslo, Norway, October 14 - 18, 2006, 2006, pp. 212-221.

Suchman, L. (2002) "Located accountabilities in technology production," Scandinavian Journal of Information Systems (14) 2, pp. 91-105.

Van Der Vleuten, E. (2004) Infrastructures and societal change. A view from the large technological systems field. Technology Analysis & Strategic Management 16 (3), 395-414.

Venkatesh, V. and F. D. Davis (2000) "A Theoretical Extension of the Technology Acceptance Model: Four Longitudinal Field Studies," Management Science (46) 2, pp. 186-204.

Weill, P. and M. Broadbent (1998) Leveraging the New Infrastructure. Boston, MA, USA: Harvard Business School Press.

Weiser, M. (1991) The computer for the 21st century. Scientific American 265 (3), 94-104.

Wulf, V. and B. Golombek (2001) "Direct Activation: A Concept to Encourage Tailoring Activities," Behaviour & Information Technology (20) 4, pp. 249 - 263.

Wulf, V., V. Pipek, and M. Won (2007) "Component-based Tailorability: Enabling Highly Flexible Software Applications," Int. Journal on Human-Computer Studies 66 (1), pp. 1-22.

Zimmerman, A. and T. A. Finholt (2007) “Growing an Infrastructure: The Role of Gateway Organizations in Cultivating New Communities of Users.” Proceedings of ACM Group 2007, pp. 239-248.

## About the Authors

Volkmar Pipek is an assistant professor for CSCW/Collaborative Systems at the Institute for Information Systems, University of Siegen, Germany. His research interests include End-User Development (in Service-Oriented Architectures and Ubiquitous Computing), complex software infrastructures (ERP, Emergency Response systems, etc.), Knowledge Management, E-Science and User-Driven Innovation.

Volker Wulf is a professor in Information Systems and New Media at the University of Siegen, Germany. At Fraunhofer FIT, he heads the research group User-centred Software-Engineering (USE). His research interests lie primarily in the areas of Human Computer Interaction, End-User Development, Computer Supported Cooperative Work, Participatory Design, and Organizational Computing.

Copyright © 2009, by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers for commercial use, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via e-mail from ais@gsu.edu.

# 1JA om Ss

ISSN: 1536-9323

Editor Kalle Lyytinen Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Robert Fichman</td><td>Boston College, USA</td><td>Dennis Galletta</td><td>University of Pittsburgh, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Robert Kauffman</td><td>University of Minnesota, USA</td><td>Frank Land</td><td>London School of Economics, UK</td></tr><tr><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td></tr><tr><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Michael Wade</td><td>York University, Canada</td><td>Ping Zhang</td><td>Syracuse University, USA</td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Kemal Altinkemer</td><td>Purdue University, USA</td></tr><tr><td>Michael Barrett</td><td>University of Cambridge, UK</td><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td></tr><tr><td>Michel Benaroch</td><td>University of Syracuse, USA</td><td>Francois Bodart</td><td>University of Namur, Belgium</td></tr><tr><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td><td>Susan A. Brown</td><td>University of Arizona, USA</td></tr><tr><td>Tung Bui</td><td>University of Hawaii, USA</td><td>Andrew Burton-Jones</td><td>University of British Columbia, Canada</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Mike Chiasson</td><td>Lancaster University, UK</td><td>Mary J. Culnan</td><td>Bentley College, USA</td></tr><tr><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td><td>Samer Faraj</td><td>McGill university, Canada</td></tr><tr><td>Chris Forman</td><td>Carnegie Mellon University, USA</td><td>Ola Henfridsson</td><td>Viktoria Institute &amp; Halmstad University, Sweden</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Hemant Jain</td><td>University of Wisconsin-Milwaukee, USA</td><td>Bill Kettinger</td><td>University of South Carolina, USA</td></tr><tr><td>Rajiv Kohli</td><td>College of William and Mary, USA</td><td>Mary Lacity</td><td>University of Missouri-St. Louis, USA</td></tr><tr><td>Ho Geun Lee</td><td>Yonsei University, Korea</td><td>Jae-Nam Lee</td><td>Korea University</td></tr><tr><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td><td>Ji-Ye Mao</td><td>Renmin University, China</td></tr><tr><td>Anne Massey</td><td>Indiana University, USA</td><td>Emmanuel Monod</td><td>Dauphine University, France</td></tr><tr><td>Michael Myers</td><td>University of Auckland, New Zealand</td><td>Fiona Fui-Hoon Nah</td><td>University of Nebraska-Lincoln, USA</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Brian Pentland</td><td>Michigan State University, USA</td></tr><tr><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td><td>Jaana Porra</td><td>University of Houston, USA</td></tr><tr><td>Sandeep Purao</td><td>Penn State University, USA</td><td>T. S. Raghu</td><td>Arizona State University, USA</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td></tr><tr><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td></tr><tr><td>Ben Shao</td><td>Arizona State University,USA</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Katherine Stewart</td><td>University of Maryland, USA</td></tr><tr><td>Mani Subramani</td><td>University of Minnesota, USA</td><td>Burt Swanson</td><td>University of California at Los Angeles, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Jason Thatcher</td><td>Clemson University, USA</td></tr><tr><td>Ron Thompson</td><td>Wake Forest University, USA</td><td>Christian Wagner</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Eric Walden</td><td>Texas Tech University, USA</td><td>Eric Wang</td><td>National Central University, Taiwan</td></tr><tr><td>Jonathan Wareham</td><td>ESADE, Spain</td><td>Stephanie Watts</td><td>Boston University, USA</td></tr><tr><td>Bruce Weber</td><td>London Business School, UK</td><td>Tim Weitzel</td><td>Bamberg University, Germany</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Kevin Zhu</td><td>University of California at Irvine, USA</td><td>Ilze Zigurs</td><td>University of Nebraska at Omaha, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>Eph McLean</td><td>AIS, Executive Director</td><td colspan="2">Georgia State University, USA</td></tr><tr><td>J. Peter Tinsley</td><td>Deputy Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
