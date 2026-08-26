---
otero_id: 10612
otero_key: "J545KYW9"
title: "A Deontological Approach to Designing Ethical Collaboration"
authors: "Sutirtha Chatterjee; Suprateek Sarker; Mark Fuller"
year: "2009"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00190"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
3-25-2009

# A Deontological Approach to Designing Ethical Collaboration

Sutirtha Chatterjee , schatterjee@millikin.edu

Suprateek Sarker

, sarkers@wsu.edu

Mark A. Fuller

, mark@wsu.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Jourņal of the Asşociation for Information Systems JAIS

Special Issue

# A Deontological Approach to Designing Ethical Collaboration\*

Sutirtha Chatterjee Millikin University schatterjee@millikin.edu

Suprateek Sarker Washington State University sarkers@wsu.edu

Mark A. Fuller Washington State University mark@wsu.edu

## Abstract

A core focus of Collaboration Engineering (CE) research has been to design and deploy codified fundamental building blocks (artifacts) of collaboration, thus making it possible for practitioner groups to collaborate even without the help of a professionar facilitator. Given the fundamentally social nature of collaboration, we believe that designing such fundamental blocks (artifacts) needs to include considerations of participants' ethical values. As such, we propose a conceptual schema for a fundamental artifact having ethical features derived from the deontological view of ethics. Based on the notions of design theory, valuesensitive design, and deontological ethics, this paper develops an object-oriented representation of an Ethical Collaboration class that can be instantiated into objects that, in turn, can serve as fundamental building blocks for ethical collaboration. Contributions and future implications of such a conceptualization are also discussed.

Keywords: collaboration, value-sensitive design, ethics, deontological perspective, design theory, object-oriented approach, modeling

# A Deontological Approach to Designing Ethical Collaboration

## 1. Introduction

Collaboration is widely acknowledged to be a key ingredient underlying the success of contemporary organizations (e.g., Nunamaker et al., 1991) and is “essential in many mission critical activities” (Grunbacher et al., 2004: 9). Increasing evidence shows that businesses rely on technologymediated collaborative meetings to accomplish a variety of tasks (Nunamaker et al., 1991; Briggs et al., 1997). Accordingly, finding ways to facilitate collaboration meetings has become a priority for practitioners and researchers. However, because of the inherently complex nature of collaborative meetings, which today can be undertaken in many ways—synchronously or asynchronously, in a colocated or distributed setting, in homogeneous or diverse groups, etc.—facilitation may be not be simple. Moreover, while organizations depend on the success of such collaborations, few have access to expert facilitators or have standards that guide collaboration processes based on value priorities of the organization (e.g., aesthetical, economical, emotional, or ethical). Thus, understandably, there is emerging interest in the academic and practitioner communities, especially among Collaboration Engineering (CE) scholars, in designing standardized self-managed collaboration processes.

According to Kolfschoten et al. (2006), CE “is an approach that designs, models and deploys repeatable collaboration processes for recurring high-value collaborative tasks that are executed by practitioners using facilitation techniques and technology” (p. 612). The value of CE is that it allows decision makers to design collaborative processes that are self-managed, at least in part, and have repeatable outcomes (Kolfschoten et al., 2006).

A core area of interest in CE is that of designing fundamental building blocks for such collaborative processes (de Vreede et al., 2006; Kolfschoten et al., 2006; Limayem, 2006; Grunbacher et al., 2004; den Hengst and de Vreede, 2004). These building blocks represent an abstraction of the recurring aspects of a collaborative process (den Hengst and de Vreede, 2004). The underlying premise is that, if used in appropriate sequences, these blocks can constitute full-fledged collaboration processes (Bragge et al., 2005). Thus, well-deasigned collaborative processes begin with designing such fundamental building blocks.

Unfortunately, as Briggs (2006) notes, theory-based design of such collaborative processes is lacking—and desperately needed. He asserts that “a rigorous theoretical approach to [their] design can lead us to produce successes beyond those possible with an intuitive, seat-of-the-pants approach” (p. 573). He reiterates this point by adding that “rigorous theory can lead to designs for collaboration technology process[es] that far surpass those produced by a good mind and a gut feel” (p. 573). It is worth noting that Briggs calls for theoretical approaches to be directed more toward designing socio-technical collaboration processes rather than toward designing collaboration technology alone. This paper responds to this call for better theory-driven design by drawing on a specific ethical tradition to propose a “fundamental block” for an ethical collaboration process, which includes, but is not limited to, technological considerations.

Drawing on a formal design approach articulated in existing literature, this paper attempts to specify this fundamental block. In a manner consistent with current CE literature (e.g., Kolfschoten et al., 2006; de Vreede et al., 2006) that has adopted object-oriented conventions to represent designs of collaborative processes (referred to as “thinkLets,” as described later), we outline an Ethical Collaboration class that can be potentially instantiated into a collaboration object. Ethical considerations, though not completely absent in previous CE research, have not been incorporated or utilized systematically. This paper illustrates how ethical principles may be systematically applied within CE. We believe such infusion of ethics in CE is essential, given the potentially critical importance of ethical action in collaboration, a process that involves social interaction.

Apart from answering the call for better theory-driven design of collaboration processes, this paper also contributes to the emerging stream of design science research in the IS discipline.<sup>1</sup> According to

<sup>1</sup> We should note herein that the paradigm of design science is not new to IS. In fact, during the early years of the discipline, computer science was regarded as one of the three important foundational bases of the IS discipline

Hevner et al. (2004), “the design-science paradigm seeks to extend the boundaries of human and organizational capabilities by creating new and innovative artifacts” (p. 75). We see a natural linkage between the CE approach and the design science approach (particularly the engineering aspect of CE) and have, therefore, explicitly used some of the design science guidelines to propose our collaboration artifact. We believe that, in bringing the two traditions together, we are able to offer a useful example for future researchers in both the CE and design science communities.

We should clarify here that this paper’s objective is to provide an ethical CE artifact (i.e., an ethical collaboration class that can be instantiated into objects) that has ingrained values. The view of artifacts having values inscribed within them is consistent with existing IS research (Walsham, 2001) and the information ethics literature (e.g., Floridi, 2002). In general, scholars agree that all design artifacts, such as technologies and associated processes, have, upon implementation, the potential to impact human life, and, thus, need to have appropriate values embedded in them (Klein and Hirschheim, 2001; Friedman, 1996).

The paper proceeds as follows. In the next section, we elaborate on the notion of design and the components of design theory. Following that, we explore the need for value-sensitive design of collaboration processes and articulate the relevance of ethical theories to value-sensitive design. Thereafter, we develop our conceptualization of the ethical CE artifact, guided by a well-designed theory framework. We also illustrate how features of the ethical CE artifact may be inscribed into an ethical thinkLet. Finally, we present our discussion section and conclude with the contribution and future implications of the paper.

## 2. Design and Design Theories

Design Science reflects the engineering paradigm of IS research (Hevner et al., 2004; Lee, 2007). It is geared toward solving practical human problems by creating suitable artifacts (Nunamaker et al., 1991a; March and Smith, 1995).

So, what is design? Design is both a noun and a verb (Walls et al., 1992); that is, it encompasses both the artifact and the process of designing that artifact (Walls et al., 1992; March and Smith, 1995; Hevner et al., 2004). According to March and Smith (1995) and Hevner et al. (2004), there are four kinds of design artifacts: constructs, models, methods, and instantiation. Constructs provide the vocabulary for defining and communicating problems and solutions (Schon, 1993, cited in Hevner et al., 2004). Models represent the real-world situation of the design problem and its solution space (Simon, 1996). Models aid problem and solution understanding and frequently represent the connection between problem and solution components, enabling exploration of the effects of design decisions and changes in the real world (Hevner et al., 2004). They are higher order constructions based on the lower order constructs (March and Smith, 1995). Methods provide guidance on how to solve problems. Instantiations involve incorporation of the constructs, models, and methods in a specific product, for example, a transaction processing system (March and Smith, 1995).

The design artifact we propose is a collaboration class that represents a fundamental building block for a collaboration endeavor informed by a particular tradition of ethics. Broadly, the collaboration object we conceptualize falls under the “models” category of design artifacts (because we are attempting to specify a collaboration process). In effect, using the object-oriented vocabulary and UML notation (constructs), we propose a higher order abstraction of the ethical collaboration process

(Culnan and Swanson, 1986). This observation was also made by Peter Keen (1980) in his influential address at the first International Conference on Information Systems. Consequently, we see a plethora of IS research from the late 1970s through the 1980s that was dedicated to design-related endeavors. For example, works by Nunamaker and colleagues (e.g. Applegate et al., 1986; Choobineh et al., 1988), Sprague and colleagues (e.g. Sprague and Carlson, 1982; Sprague, 1980), and Bonczek and colleagues (e.g. Bonczek et al., 1980; 1981) showcase the rich tradition of design research in the early stage of the IS discipline. A substantial proportion of researchers in the early days of the IS discipline had technical backgrounds (Culnan, 1986), and a focus on design in the discipline during this period could have been due to this fact. However, as specifically noted by Hevner et al. (2004) and Vessey et al. (2002), much of the recent IS research has focused on behavioral rather than design issues. It is only very recently, in the last two to three years, that we are witnessing resurgence in design-oriented research.

in terms of a fundamental building block expressed in object-oriented terms.

Design theories provide an approach for the creation of artifacts and have two components: one dealing with the product (artifact) and another dealing with the process of designing the artifact (Walls et al., 1992).<sup>2</sup> Inspired by Walls et al.’s conception of design theories, this paper presents a preliminary design of a collaboration class (that can be instantiated into objects) with an ethical consideration.

Table 1 and Figure 1 from Walls et al. (1992) show the framework guiding the development of design theories. In this paper, we focus primarily on the artifact itself, and thus, our design theory is primary concerned with explicating the kernel theory, the meta requirements, and the meta design aspects of a design theory for fundamental objects of collaborative processes. Since our basic idea is to provide for a conceptual foundation for building blocks of ethical collaborative processes, the articulation and testing of specific testable hypotheses on the design artifact (and/or on the design process) are beyond the current scope. We now visit the notion of value-sensitive design, which serves as a core foundation of our work.

<table><tr><td colspan="2">Table 1. Components of an Information Systems Design Theory for design as an artifact (Walls et al., 1992)</td></tr><tr><td>Kernel theories</td><td>Theories from natural and social sciences governing the design requirements for artifacts.</td></tr><tr><td>Meta requirements</td><td>Explains the class of goals that need to be satisfied</td></tr><tr><td>Meta design</td><td>Explain the class of artifacts that can meet the meta requirements above</td></tr><tr><td>Testable design product hypotheses</td><td>Used to test whether the meta design meets the meta requirements</td></tr></table>

![](/api/attachments/J545KYW9/fulltext/images/8032d0cb7c8e3c029cc683d917f7b43b0964228a27c8eb974b7dba8c703d34aa.jpg)

Figure 1. The Design Theory Framework for design as an artifact (Walls et al., 1992)

<sup>2</sup> The reader is referred to Walls et al. (1992) for a detailed explanation of the various components of the design theory framework used in this paper.

## 3. Ethical value-sensitive design for CE

The notion of value-sensitive design, a theory-based approach to design that accounts for human values (Friedman et al., 2006), including ethics, has gained ground in recent years. Values such as autonomy (Winograd, 1994) and accountability (Nissenbaum, 1997; Shneiderman and Rose, 1997) have informed the design/development of information systems. However, there is little evidence of systematic and explicit consideration of human values in designing collaboration processes (Briggs and de Vreede, 2005). The aim of this paper is to contribute in this specific arena by focusing on ethical values.

First, however, we should justify why ethical value-sensitive design is important for the information systems field, in general, and the design of CE artifacts, in particular. Human ethical values are inherently embedded in the design of IS artifacts, and such values are widespread, systematic, and pervasive (Friedman, 1996). Indeed, ethical values have been described as “fundamentally part of [IS] practice” (Friedman and Kahn 2003, p. 178). The relevance of ethical values in IS is further substantiated by Chae et al. (2005), who point to ethical implications in the design of decision support systems. Given the impact of technologies and allied processes on various facets of human life, we believe that designers have an obligation to inscribe desirable values within them. Indeed, Klein and Hirschheim (2001) argue, drawing on Plato’s Republic (360 B.C.), that value considerations, in terms of justice and well-being, are of utmost importance. This is particularly true in the context of collaboration, which involves human interaction and cooperation.

Previous CE and IS literature has explicitly addressed the issue of social interaction in the context of computer-mediated groups (e.g., Sarker et al., 2005; Chidambaram, 1996; Huang and Wei, 2000; McGrath, 1991) as well as virtual teams (e.g., Jarvenpaa and Leidner, 1998; Sarker and Sahay, 2004; Fuller et al., 2007). This body of research indicates that, for better collaboration in situations involving complex problems with interdependencies among potential collaborators, the group needs to develop, through social interaction, into an integrated unit. This involves the formation of a shared frame of reference, a congruent identity, and a sense of mutuality rather than mere bidirectionality in the intragroup relationships (Sarker and Sahay 2003). This is possible, for example, by enacting genuine respect for collaborators’ autonomy (e.g., Urry, 2002; Sarker and Sahay, 2003). A process based on social interaction is inherently vulnerable to various distortions arising from the use of expert, structural, or other forms of power, peer pressure, and efficiency imperatives, real or imagined (Hirschheim and Klein, 1989; Hirschheim and Newman, 1991). Ethical principles inscribed into the interaction process specification can be useful in ensuring that basic human values, such as those mentioned above by Hirschheim and Klein (2001), are respected during collaboration. Furthermore, collaboration, no matter what its agenda is, is inherently a knowledge creation and sharing process (where different ideas are exchanged and newer ideas emerge). As Churchman (1971, cited in Courtney, 2001) argues based on Spinoza’s celebrated works, there is a strong philosophical argument that knowledge is inherently intertwined with morality. Thus, the inherent link between collaboration and knowledge further points to the importance of ethical issues in collaboration.

The relevance of ethics to value-sensitive design also stems from Alexander’s (1979; 1980) idea that one should design morally sound objects (cited in de Vreede et al 2006). This point is echoed by Iivari et al. (2000) in the IS literature. Furthermore, as Friedman et al. (2006) point out, ethical values are different from facts (Moore 1903/1959). Thus, ethical values represent the “ought” side of the “is ought” debate, i.e. the descriptive-normative debate (Friedman et al., 2006).

Thus, ethical values are clearly relevant to a collaboration context. This premise drives our explication of the design for our CE artifact, following the design theory framework components: kernel theories, meta requirements, and meta design. In fact, the meta design is essentially the CE artifact informed by the kernel theories and the corresponding meta requirements. Since our aim at this stage is to conceptually “model” a fundamental CE artifact (rather than develop an “instantiation”), providing (and testing) explicit hypotheses remains beyond the intent of this research. In fact, we call upon future researchers to develop explicit hypotheses and conduct empirical studies, consistent with the tenets of the behavioral science paradigm, to provide further insights into ethical collaboration.

## 4. Designing the CE Artifact

## 4.1 Kernel Theories

As depicted in Figure 1, the first component of a design theory for artifacts deals with the kernel theories. Because of our focus on ethical human values and our articulation of the link between human values and ethics, these draw from philosophical theories of ethics. However, ethics has been an extensive field in philosophy, so a multitude of ethical theories are potential candidates for serving as the kernel theory in our study.

In the literature, ethical theories are seen as belonging to three broad streams of thought: consequentialist ethics, deontological ethics, and virtue ethics. The consequentialist and deontological schools form the two major act-based schools of ethics. According to the consequentialist school, early proponents of which were Bentham (1789/1970) and Mill (1861/1979), the rightness (or wrongness) of an action is determined by how much hedonistic consequential benefit (maximizing pleasure and minimizing pain) is derived from the action. According to the early consequentialists, the moral worth of an action is determined solely by its contribution to overall utility in terms of maximizing pleasure and minimizing pain. These hedonistic considerations have since been extended to non-hedonistic considerations such as money and material wealth (Moore 1903/1959), but the primary goal of utilitarianism, in terms of maximization (in positive terms) of the resultant outcome, remains the same.

On the other hand, the deontological school of ethics argues that rightness of action is determined by certain rules in place. A primary proponent of this school was Immanuel Kant, who grounded these rules in the form of the categorical imperatives (1804/1994). Such rules represent duties (in terms of respecting another individual’s rights) to be followed, and an act is deemed ethical if it conforms to these rules.

The third stream of thought in the ethics literature, virtue ethics (O’Neill, 1996; Hursthouse, 1999), judges not the ethicality of actions but rather the ethicality of individuals. Virtue ethics draws from the works of Aristotle, who described certain virtues individuals should have: courage, honesty, compassion, and the like. While the focus of act-based ethical theories (i.e., consequentialism and deontology) is on actions themselves, the focus of virtue ethics is on how one can be a good person. Virtue ethics emphasizes the idea that we should be good persons as opposed to just doing good acts.<sup>3</sup>

There has always been an inherent tension between these three broad schools of ethical thought. While some modern philosophers (e.g., O’Neill, 1996) have attempted to unite certain aspects of these apparently diverse theories, the field of philosophical ethics still holds that these theories are radically different from each other. Thus, it is reasonable to argue that kernel theories pertaining to ethics can draw from either the consequentialist, deontological, or virtue ethics perspectives.

In this paper, we focus on the deontological (i.e., the rights-based) rather than the consequentialist perspective, even though the latter perspective focuses on consequences (or results), which could suggest its usefulness/attractiveness in the organizational collaboration context. One primary reason for our choice is that focusing on the deontological (rule-based) perspective allows us to inscribe such rules within the (collaboration) artifacts, showcasing its natural applicability to the scope of our research. Moreover, a problem with the use of consequentialism for designing such artifacts is that consequences can vary based on a variety of contextual factors (i.e., some collaborative processes might highlight efficiency as a consequence, and others the actual decision quality) and they are unknown a priori;<sup>4</sup> yet we do not deny the potential relevance of consequentialism as an ethica viewpoint. For example, if our ethical focus is not on preserving the rights of individuals in the collaborative decision-making process but rather on the outcome of the process itself (i.e., if we take an end-justifies-the-means perspective), consequentialism can be a potentially effective lens to design collaborative work.

We also focus on the deontological view rather than on virtue ethics because virtue ethics is agentcentered (i.e., the unit of analysis is the individual), not act-centered, as are consequentialism and deontology. The scope of our discussion—collaborative work practices—essentially pertains to what collaborators and facilitators need to do (i.e., act) in the context of a group. Hence, act-based theories are more appropriate than agent-centered theories within our context. Having said that, we could also envisage designing collaborative artifacts from the point of view of “good” or “virtuous” agents (i.e., facilitator or practitioner) and how they can have certain virtuous characteristics, thus making the entire process in which they take part virtuous. This would be an interesting endeavor, and we urge future research to investigate in this direction.

Finally, our choice of deontological ethics as our kernel theory stems also from its relevance in a collaboration context. Essentially, processes of collaboration are social/sociopolitical in nature, making the deontological view applicable. Indeed, the sociopolitical system represented in the U.S. Constitution draws profoundly on deontological or rights-based views. In the collaboration context, the relevance of the deontological view is implicitly evident in the work of de Vreede and de Bruijn (1999), who suggest that fairness and rationality (inherently linked to the deontological view) are important considerations for electronic meetings. Thus, the deontological view of ethics, represented by the rights-based framework of Immanuel Kant (1804/1994) and the distributive justice theory of John Rawls (1971), provides an appropriate kernel theory for our design theory framework. Both these theories provide essential guidance on the design of a sociopolitical system. Rawls’s framework is, in fact, partly based on Kant’s framework of rights-based theories, and hence, both are considered rights-based theories of normative ethics (Payne and Joyner, 2006).

Kant’s (1804/1994) formulation of the deontological view of ethics rested on his three famous categorical imperatives:

“Act only according to that maxim whereby you can at the same time will that it should become a universal law” (p. 30).

“Act in such a way that you treat humanity, whether in your own person or in the person of another, always at the same time as an end and never simply as a means” (p. 36)

“Every rational being must so act as if he were through his maxim always a legislating member in the universal kingdom of ends” (p. 43).

According to Kant, “the categorical imperative would be one, which represented an action as objectively necessary in itself, without reference to another end” (Kant, 1804/1994: 25). Any such objectively necessary action would represent a rule, and it is the individual’s duty to follow the rule. For example, within this perspective, it is objectively necessary to speak the truth; hence, it would be incorrect to lie, even to help somebody.

In his much-celebrated work, Rawls (1971) builds on Kant and proposes his theory of distributive justice, which upholds fairness as a principal aim of sociopolitical systems. Rawls describes the notion of justice as fairness and formulates his theory based on three fundamental ideas: the veil of ignorance, the principle of equal liberty, and the principle of fair equality of opportunity. Veil of ignorance means that if a policy maker could be oblivious to his/her own position in society, then s/he would formulate rules that are most fair. Thus, this concept implies that being ethical is closely related to being nonbiased. In other words, if we do not have any preconceived notions or biases, then our actions would be ethical. According to the principle of equal liberty, often viewed as a call for egalitarianism, “each person is to have an equal right to the most extensive basic liberty compatible with a similar liberty for others” (p. 60). Somewhat related to the principle of equal liberty is the principle of fair equality of opportunity, also called the difference principle. The difference principle states that societal opportunities should be equally available to all, especially to those that are disadvantaged (Rawls, 1971).

To summarize, the deontological views of Kant and Rawls provide useful kernel theories for guiding the design of artifacts corresponding to ethically-informed collaborative processes. The essence of these theories is in treating everyone equally and fairly in a sociopolitical system. We now attempt to explore the implications of the deontological view for collaboration. The specific rights that need to be satisfied by ethical collaborative processes form the set of meta requirements within the design theory framework.

## 4.2. Meta requirements

The rich, time-tested views of Kant and Rawls offer a way to discern specific rights that should be upheld in a collaborative context if ethical concerns are considered paramount. These rights then serve as the meta requirements for the collaboration artifact.

The first categorical imperative of Kant translates to the idea of consistency (the term we will use to refer to this concept in this paper). It refers to the fact that all actions should be universally acceptable and consistent (Payne and Joyner, 2006). Within collaboration processes, the meta requirement of consistency implies that facilitator/participants must act in the same manner with respect to all collaboration group members, regardless of their relative background, skills, and status.

The second categorical imperative translates to respect for an individual’s autonomy. Every human being is a rational and autonomous agent who needs to be inherently respected. Any action must respect human beings as being inherently valuable regardless of any benefits they might bring (Payne and Joyner, 2006). Kraus (1980) and de Vreede and de Bruijn (1999) reinforce our argument here, asserting that autonomy is a core element of collaborative processes. Within a collaborative context, this meta requirement highlights the idea that any participant/facilitator in the collaborative process should view all the participants and their inputs as being inherently valuable in themselves, not just as a means toward achieving the desired outcome of the collaboration.

The third categorical imperative translates to individuals’ accountability for their actions. If everyone were to consider himself/herself as a lawmaking member of the “kingdom of ends,”5 then each would need to have paramount accountability for his or her actions. Kant’s framework deals with rights and, correspondingly, the duty to respect those rights. The essential concept that binds rights and duties is that of accountability because, unless we are accountable, we cannot really have duties. The idea that accountability is closely tied to Kant’s idea of the categorical imperative has been observed by previous researchers (e.g., Brummer, 1986). In a collaborative process, this meta requirement implies that the facilitator/participants should be accountable for whatever activities they undertake, including providing ideas and suggestions. As an aside, the technological feature of anonymity, which might be consistent with certain ethical principles (e.g., freedom of expression, as discussed later), is not necessarily in line with accountability. In collaboration, it is often necessary to be accountable for one’s inputs and for team-members and facilitators to give due credit for input of superior quality.

Rawls’s concept of the veil of ignorance points to the need for freedom from bias. “If we did not know among us who would be rich and poor, who educated and who uneducated” (Hosmer, 1998: 397), we would not have any biases to leave out any individuals who are underserved in these respects. According to Rawls (1971), the veil of ignorance aims to “rule out those principles that it would be natural to propose for acceptance, however little the chance of success, only if one knew certain things that are irrelevant from the standpoint of justice” (p. 18). In other words, the ethical notion of justice derives from our not knowing what level of ability and opportunity is accessible to the ones to whom we impart justice. In a collaborative context, this freedom from bias essentially implies that facilitators and participants should suspend their preconceived notions as much as possible and collaborate with an “open mind,” ready to appreciate and accept new ideas, even if they go against established beliefs.6

Rawls’ second concept, that of equal liberty, is an important basis for ethical acts. In a collaborative context, this translates to the idea that each participant should have freedom of expression, which is our next meta requirement. This meta requirement has been suggested in past work on collaboration (e.g., Kraus, 1980; Warkentin and Beranek, 1999). Essentially, it means that individuals should be able to express their views and contribute in ways they find suitable—not silenced because of existing social (power) structures, personal limitations (e.g., weak written or verbal communication competence, or poor language competence), and physical conditions (time-space divide among collaborators) (e.g., Sarker and Sahay, 2004). In such situations, features of collaboration technology, such as options for different levels of anonymous communication, the availability of multiple channels of communication and language translators, and a choice of asynchronous and rich synchronous communication options, can contribute toward the meta requirement of freedom of expression.

The final concept, fair equality of opportunity, that we adopt from Rawls, implies that every participant should have equality in participation and equal access to resources, such as time and technology. Such fairness allows all collaborators to participate as equals on a level plane.

To summarize, drawing on the deontological tradition, we propose that an ethical collaboration process should engender the goals of consistency, individual autonomy, accountability, freedom from bias, freedom of expression, and equality. These form the meta requirements for the collaboration artifact we seek to design. A summary of the meta requirements is presented in Table 2.

<table><tr><td colspan="2">Table 2. Meta Requirements for ethical collaboration derived from the deontological tradition</td></tr><tr><td>Meta Requirement</td><td>Brief description with relevance to collaboration</td></tr><tr><td>Consistency</td><td>Universal acceptability of acts for self and others; this requirement of consistency implies that facilitator/participants must act in the same manner with respect to all collaborating group members, regardless of their relative background, skills, and status.</td></tr><tr><td>Respect for Individual&#x27;s Autonomy</td><td>Human participants in a collaboration are inherently valuable in themselves, not just as means to achieve an outcome of that collaboration</td></tr><tr><td>Accountability</td><td>All participants should be accountable for the activities they undertake and inputs they provide in the course of the collaboration</td></tr><tr><td>Freedom from Bias</td><td>All participants should participate in the collaboration with an open mind and try not to let any preconceived biases influence their participation</td></tr><tr><td>Equality</td><td>Every human participant should have equal scope and opportunity for participation and should have access to all possible resources to facilitate the same</td></tr><tr><td>Freedom of Expression</td><td>All participants in a collaboration should be encouraged to express their views without any constraints imposed by the technology, facilitator, or fellow participants</td></tr></table>

## 4.3. Meta design

As part of the meta design, we aim to represent a preliminary conceptual schema of a collaboration class, which can serve as a fundamental building block for ethical collaboration processes. The recent literature on CE provides useful guidance in this area, modeling collaboration building blocks as “thinkLets.” A thinkLet “constitutes the smallest unit of intellectual capital required to create one repeatable, predictable pattern of collaboration among people working toward a goal” (Briggs et al., 2003). As mentioned by Kolfschoten et al. (2006), one important focus of current research in CE is “to identify and document reusable elementary building blocks for group process design” (p. 612). ThinkLets are designed to serve this purpose.

Initially, thinkLets were conceptualized as being composed of three elements (Kolfschoten et al.,

2006; Briggs et al., 2003): tool, identification, and script.7 Understandably, the conceptualization and representational strategy for thinkLets has been evolving, and recently they have been represented in object-oriented terms (e.g., de Vreede et al., 2006; Kolfschoten et al., 2006). Our paper proceeds somewhat similarly, and we attempt to represent a preliminary version of an ethical collaboration class (one could think of it as a “pre-thinkLet”) using object-oriented conventions. The proposed ethical collaboration class (which can be instantiated into ethical collaboration objects) differs from other thinkLets described in the literature in a number of respects, most notably on one critical issue: While existing conceptualizations of thinkLets are general, our focus in this paper is to visualize an ethical collaboration class that would uphold the ethical meta requirements articulated above. Moreover, the “meta design” we present is necessarily incomplete and underspecified—our goal is not to be comprehensive but to illustrate the possibilities of “engineering” collaboration objects by using a formal design approach informed by ethical considerations.8

Central to the goal of creating an ethical collaboration class is the premise that such classes, instantiated as morally sound objects, should improve the quality of human life and therefore deliver value over time (Alexander, 1979, cited in de Vreede et al., 2006). Noting that the meta requirements articulated above relate to core individual rights and, thus, are intrinsically related to the quality of work life, we can argue that collaboration objects could be designed to provide a basic satisfaction of the meta requirements.

Before proceeding to the actual schema, we need to delineate a focal role, that of the practitioner, which has implications for the conceptual schema we describe in the following section. Existing literature on CE has highlighted three important roles associated with collaboration: facilitator, practitioner, and collaboration engineer (Kolfschoten et al., 2006). While the facilitator has long been acknowledged as a critical component of collaborative processes (e.g., de Vreede et al., 2006; Limayem, 2006; Griffith et al., 1998; Mittleman et al., 2000), a key objective of the field of CE is to “codify and package key facilitation interventions in forms that can be re-used readily and successfully by teams that do not have professional facilitators at their disposal” (Kolfschoten et al., 2006, p. 612). In other words, CE strives to create systemic processes that can enable organizations to achieve excellence in collaboration even in the absence of the individual talent and experience of facilitators. In a sense, the expectation is that a well-engineered collaborative process would work well even without a facilitator, or with a (novice) practitioner in the role of a facilitator.

A practitioner “is a task specialist who must execute some important collaborative task like risk assessment or requirements definition as a part of his or her professional duties” (Kolfschoten et al., 2006, p. 612). As noted by Kolfschoten et al., a practitioner is not and need not be a professional facilitator; he/she needs to have access to the designed process (e.g., thinkLets) in order to facilitate collaboration. Other than the possibility of a practitioner serving as a facilitator, s/he can also be a participant in a collaborative process.

Finally, a collaboration engineer “designs and documents collaboration processes that can be readily transferred to the practitioner” (Kolfschoten et al., 2006: 612). Thus, within our conception, the collaboration engineer is responsible for designing, and, more importantly, customizing relevant collaboration classes to particular use contexts. For example, if an advertising company charged with developing a new marketing message for a client wishes to implement a collaboration process that balances aesthetic and ethical concerns, the collaboration engineer, much like a consultant, would be responsible for blending aspects of collaboration objects that have inscribed in them the two disparate values (i.e., ethics and aesthetics). In addition, the collaboration engineer would help implement the context-specific details in the schema (i.e., the precise behaviors that would cause exceptions, the precise technology environment needed, the appropriate collaboration protocol, etc.) suitable for a creative meeting of advertising professionals.

As is evident from the above discussion, the field of CE now delineates two important roles:

practitioners and collaboration engineers. Practitioners perform facilitation activities but may also be ordinary participants in a collaborative process. Collaboration engineers are the ones who design or customize the building blocks for collaboration for use by practitioners, and hence, they are outside the scope of the collaboration class. Consequently, the only role included in the conceptual schema for a collaborative process is that of the practitioner.

Based on the above arguments, for the meta design conceptual schema, we delineate two important components: the practitioner facilitator and the practitioner participant. Additionally, we include one more key component in collaborative processes in contemporary organizations, technology (Nunamaker et al., 1996; Briggs et al., 2003). Collaboration technology provides rules and resources to support ethical meta requirements in the context of collaboration, albeit in a “logically malleable” (Moor, 2001) or interpretively flexible manner (e.g., DeSanctis and Poole, 1994).

![](/api/attachments/J545KYW9/fulltext/images/3ace7ba96336f98b88e3a582f21e600cd6f628387efb497a27d3731b86a78e81.jpg)  
Figure 2. The conceptual schema for the Ethical Collaboration Class.

The conceptual schema is represented using the UML notation of object-oriented design (see Figure 2).9 Details of each class (i.e., its attributes and methods) are not depicted within the UML diagram itself. These details are outlined when the respective classes are discussed. Our conceptualization revolves around the Ethical Collaboration (EC) class, an object instantiation, which could be the fundamental building block of an ethical collaborative process in a given situation. We have also argued that an ethical collaboration consists of practitioners (who may either facilitate or participate). As a result, our conceptual schema reflects an aggregation relationship (identified by the “part of” phrase that names these relationships) between the EC class and each of these components, represented as classes themselves. An aggregation in object-oriented terminology refers to the relationships between different objects that are instantiations of their respective classes. In this relationship, object instances of one class essentially comprise of object instantiations of other classes. Thus, the objects of the EC class are comprised of object instances of the Practitioner Facilitator (PF) class and the Practitioner Participant (PP) class. In plain terms, this implies that an EC object is composed of practitioner facilitators and practitioner participant objects. Thus, a practitioner facilitator and one or more practitioner participants are essentially “parts” of the collaboration endeavor.

Apart from this aggregation relationship, two other types of relationships between classes fall under the purview of this preliminary conceptual schema. The first one is a dependency relationship, where one class is dependent on another class (called the independent) in order to carry out some action of the (first) class. In our conceptual schema, the relationship, between the PF class and the Technology (T) class is modeled as a dependency relationship where the PF class is dependent upon the T class to carry out some actions pertaining to that class. We explicate this dependency later in this section. The other relationship that is represented in our conceptual schema is that of an inheritance relationship, formally known as a generalization specialization relationship. In this relationship, one class inherits the attributes and methods from another class. In our conceptual schema, the PF and the PP class both inherit from the Practitioner (P) class.

In summary, our conceptual schema revolves around the object instantiations of three classes: T, PF, and PP. Our EC object consists of PF and PP objects (as articulated earlier). The PF object actually depends upon the T object to carry out some of its operations. We believe that if each of these objects has sufficient ethical aspects (or provides contingencies for such ethical aspects, as in the case of the T class), then the EC class, through its aggregation of the PF and PP classes, would incorporate the same ethical aspects that are exhibited by the PF and PP classes.

Also, true to the object-oriented paradigm, each of the indicated classes has a set of attributes and methods that support the meta requirements we discussed above. However, we should reiterate that our aim in developing the classes is illustrative, not exhaustive. We acknowledge that ethica collaboration can acquire different connotations in different collaborative contexts and problems.10 Our aim is to provide a broad illustrative view of ethical collaborative processes and to elaborate on some of their key attributes and behaviors.

## 4.4. The Practitioner (P) Class

This class represents a practitioner who may not have formal training/experience as a facilitator or a collaboration participant but “only needs to learn specific skills required to accomplish a particular collaboration process” (Kolfschoten et al., 2006: 612). An overview of the P class is shown below. The practitioner represented by this class could perform as a facilitator and also as a participant. An overview of the practitioner class is outlined below in Figure 3. (Note: we use “//” as a commenting style similar to the C++ notation)

Our depiction of this class consists of an important attribute of the practitioner that is potentially important in an ethical collaborative scenario.

The first important attribute of this class is receivedEthicalTraining (see Figure 3). This attribute becomes important because training has been seen as an important precursor to effectiveness in collaborative activities (e.g., Anson et al., 1995; Clawson and Bostrom, 1996; Kelly and Bostrom, 1997; Kang and Santhanam, 2003). Our practitioner needs to pick up the skills (Kolfschoten et al., 2006) that are pertinent to the ethical collaborative process. For example, difficult skills, and ones that need to be carefully cultivated, are respecting team members’ autonomy and reflecting upon one’s preexisting biases to eliminate (or at least control) them in a situation when the focal individual is attempting to convince team-members about the merits of his/her approach. The Boolean attribute receivedEthicalTraining indicates whether (or not) the practitioner has successfully completed the prescribed training for his/her role (participant or facilitator) within an ethical collaborative process.

//attributes of the practitioner facilitator

receivedEthicalTraining; metaRequirementList [];

//methods of the practitioner facilitator

undergoEthicalTraining();

## Figure 3. The Practitioner (P) class

The second important attribute of this class is metaRequirementList [] (see Figure 3). This attribute depicts an array (list) of the meta requirements (discussed above) that should be a part of the practitioner class. The array of meta requirements is a placeholder for the set of meta requirements that the practitioner needs to uphold, arranged according to their relative importance within the specific collaboration context (if applicable). Thus, the index of each array element would represent the priority of the meta requirement. This is necessary because if two meta requirements conflict in a particular collaborative context, then the facilitating practitioner would know which meta requirement to uphold first and foremost. However, we do not attempt to provide any such prioritization within this paper, given that such priorities are context-specific. For example, in some collaborative contexts, consistency might be required more than freedom of expression. However, at a broad level, none of the meta requirements should be compromised unless they come in direct and irresolvable conflict with another meta requirement.

Apart from these three attributes, the P class has a method that represents the actions a practitioner should undertake. This method, called undergoEthicalTraining() (Figure 3), implies that the practitioner needs to undergo training in the ethical meta requirements that have been discussed above. Also, the person(s) conducting the training should be well versed in the area of deontological ethics and of ethical collaboration. The training is an important aspect because it guarantees, at least to some extent, that the facilitators and participants understand the basic ethical concepts and also prove their proficiency in that concept. While the final evaluation of the training participants may be left to the trainer, essentially what is important is that the trainer is satisfied that the participants have a good understanding of the meta requirements. Unless this training is undertaken, the practitioner may not really appreciate the true worth (or implications) of the meta requirements. Our premise is that undergoing ethical training with systematic coverage of the ethical principles, scenarios, etc. is likely to ensure participant or facilitator behaviors (as applicable) that are consistent with the meta requirements.

Herein, we should mention an important aspect of this training. A collaboration is often a complex socio-political process, giving rise to differing situations and contexts. The rules of deontological ethics (meta-requirements) can be treated on a basic abstract hypernorm level, and local, situationspecific norms can be derived from them (Donaldson and Dunfee, 1994). Such local and situationspecific norms are instantiations (e.g., do not talk when another person is talking is a local instantiation of the overarching norm “respect others’ autonomy”) that are essentially derived from the same ethical meta-requirements. And this is where the importance of the training lies. A facilitator or a participant well versed in the concepts of ethics can be expected to be able to derive appropriate instantiations in specific contexts. Note that our CE artifact in fact can be seen as an example of a Kantian System of an Inquiring Organization (Churchman, 1971, cited in Courtney, 2001), which, while being idealistic, is able to appreciate multiple points of view (i.e., multiple definitions of the same meta-requirement) but still work toward idealized solutions, just like our idealized solution to uphold the principles of deontological ethics in collaboration. A suggested outline of this method is provided below (see Figure 4).

## Void undergoEthicalTraining()

Do the following if receivedEthicalTraining <>’Y’

For each meta requirement from the metaRequirementList [] do the following:

//suggested steps

1. Articulate the linkage between the meta requirement and establish the importance of that meta requirement to an ethical collaborative process

2. Ask trainees to write their own ethical dilemmas and ask them construct their own collaborative scenarios where these requirements are satisfied or violated. Alternatively, present them with ethical collaborative scenarios found in the literature or from the experience (of the trainer) where these meta requirements are violated and/or satisfied.

3. Distribute the cases generated amongst the trainees and ask them to reflect on them. Generate a discussion on the same.

4. Describe protocols for collaboration that are consistent with the meta requirements. In addition, discuss what human behaviors or technology malfunctions would need exception handling procedures or even termination of the collaboration process.

5. Each trainee must complete a suitable assessment module for each meta requirement. Upon successful completion, set receivedEthicalTraining to ‘Y’ or else go back and repeat the training for that participant

## Figure 4. The method undergoEthicalTaining

## 4.5. The Practitioner Facilitator (PF) Class

This class represents a practitioner who does not have formal training as a facilitator but “only needs to learn specific skills required to accomplish a particular collaboration process” (Kolfschoten et al., 2006: 612). As can be seen from our UML diagram (Figure 2), the PF class actually inherits from the P class because, after all, a PF is also a P. An overview of the PF class is represented below (see Figure 5). Since this Practitioner Facilitator inherits both the attributes and the method of the Practitioner class, we do not represent the attributes and method that are already inherited. Instead, we concentrate on attributes/methods that are unique to this inherited Practitioner Facilitator class. This class may not need additional attributes of its own, but it must possess its own unique methods. A suggested outline of each (unique) method is provided in this section.

## Class practitionerFacilitator

//attributes of the practitioner facilitator

//this class inherits all the attributes of the practitioner //class and there are no new attributes

//methods of the practitioner facilitator

implementEthicalProtocol();

handleExceptionEthically();

generateReportOnFacilitationExperience();

readPreviouslyGeneratedReports();

Figure 5. The practitionerFacilitator class

The most important method or operation that the practitionerFacilitator needs to undertake is that of implementing the ethical protocol. The method implementEthicalProtocol() (see Figure 6) outlines some possible activities involved in facilitating an ethical collaborative process. A protocol is at the core of a collaborative process (e.g., DeSanctis and Gallupe, 1987; Nunamaker et al., 1996). Extant research on thinkLet-based collaboration also highlights the importance of protocols. For example, in the work of de Vreede et al. (2006), “rules” (which are very similar to protocols) are seen as closely related to the concept of thinkLets. Thus, the method (implementEthicalProtocol()) is at the heart o the specification of an ethical collaborative process. This method consists (partly) of a number of actions to be taken by the practitioner facilitator. Each such step conforms to a specific meta requirement (italicized), as shown below. Apart from that, the facilitator could actually check (and change) any technology features that could be detrimental to upholding any of the meta requirements through the changeFeature (feature, reason) method provided by the technology class. So, the practitioner facilitator has the option of customizing the technology so as to uphold the meta requirements. In essence, the technology, owing to its default features, may provide some constraints for participant action (Kolfschoten et al., 2006). The practitioner facilitator would essentially work around those constraints so that they (i.e., the constraints) do not conflict with the meta requirements. Furthermore, an important outcome, as evident in the body of the method, would be assigning of equal capabilities to each participant.

## Void implementEthicalProtocol()

//articulations to the participants, each articulation pertains to a meta requirement

1. Explain to the participants that their participation is inherently valuable to this collaboration, whether or not the desired outcome is achieved (respect for individual’s autonomy).

2. The chosen protocol is one that provides all participants are treated equally in the collaboration process (equality). Such a protocol could involve two phases:

a. “Round robin” phase initially, where everyone has equal time to contribute.

b. “Token passing” phase, where all individuals are sequentially given equal opportunity to contribute as the token is passed among the collaborators, who may avail the opportunity only when he/she has something to offer (equality).

3. All participants are free to express their views in any way, as long as they do not cause any violation of other participants’ ability to express their views (freedom of expression).

4. While different viewpoints are welcome, any biases must be set aside or discussed openly such that they do not affect the direction of the collaboration process (freedom from bias).

5. All participants have accountability for their inputs and activities (accountability).

6. All participants are expected to act in a manner that would seem fair if they themselves were the recipients of that action (consistency).

//check and manipulate technology features that could be opposed to any meta requirement for each meta requirement in metaRequirementList []

for each feature of technology in feature[]

1. If the feature violates any meta-requirement, invoke the changeFeature(feature, reason) or else leave it as is.

2. Make each feature equally available to all participants.

## Figure 6. The method implementEthicalProtocol

Another important method is named handleExceptionEthically() (see Figure 7). This method essentially describes what the facilitator needs to do to handle an exception within the collaborative process. Within our ethical collaboration context, an exception occurs when one or more of the meta requirements are violated within the collaborative process. For example, there could be evidence that, through peer pressure exerted by a coalition of interests, the autonomy of a particular participant and his/her freedom to express ideas is being curtailed. When this happens, the practitioner who is facilitating needs to intervene, socially and/or technologically (by enabling or disabling certain features) so that the violations are arrested and the collaborative process unfolds in manner consistent with the deontological meta requirements. In some circumstances, the facilitator may be forced to terminate the process altogether and reinitiate the collaborative process from scratch with different participants and in a different technology environment.

## Void handleExceptionEthically()

While collaboration is ongoing, repeat the following steps:

1. Monitor the upholding of the meta requirements during the collaboration process.

2. Judge the meta requirement(s) that is/are being violated.

3. If appropriate, temporarily stop the collaboration proceedings.

4. Reemphasize to the participants what the meta requirement(s) are, and their implications on participants’ expected behaviors.

5. Invoke the changeFeature (feature, reason) method of the Technology class in order to adjust any Technology features that may have been conflicting with the meta requirements or are being unfaithfully appropriated by participants. Note that the first argument of the method indicates the feature that needs to be changed and the second argument reflects the reason behind the change of the feature. /\* For example, one might switch off the feature of anonymity to ensure that the meta requirement of accountability is upheld.\*/

6. Start the collaboration proceedings.

7. Monitor if the meta requirement(s) is/are still being violated.

8. If they are, and if the issues do not appear easy to address through tactics adopted earlier, take more radical steps such as expulsion or termination of the collaboration, etc. (i.e., break out of the loop), otherwise go to the step in the third bullet and repeat.

## Figure 7. The method handleExceptionEthically

## Void genrateReportOnFacilitationExperience()

For each meta requirement in the metaRequirementList []

1. Check extent of violation (if any violation).

2. Note cause(s) of violation.

3. Note remedies of violation attempted, and their effectiveness.

4. Record details to a database/repository.

## Figure 8. The method generateReportOnFacilitationExperience

The last two methods are generateReportOnFacilitationExperience() and readPreviouslyGeneratedReports() (please see Figures 8 and 9, respectively). Essentially, both are related to the learning aspect of group collaboration alluded to in previous research. The first method, generateReportOnFacilitationExperience(), reflects the need for facilitators to generate a report on their experience with the designed ethical collaboration process. The contents of this report can then be entered into a database or repository. For example, in the report, the practitioner facilitator could reflect on whether the meta requirement of autonomy was violated at some point in the collaborative process. If so, the possible reasons and solution to this violation should be updated into the database or repository. Such prior records would enable future practitioner facilitators (and also the current facilitator) to learn how to better uphold autonomy in future collaborative efforts. With such a repository of experience available prior to the start of the collaborative process, the facilitating practitioner can go over the previous experiences in facilitating ethical collaboration processes. This operation is represented by the method readPreviouslyGeneratedReports(), which is, in fact, the firs method that needs to be invoked by the practitioner facilitator.

## Void readPreviouslyGeneratedReports()

//This would be the first method invoked by the practitioner facilitator

Open the database/repository

For each meta requirement in the metaRequirementList []

1. Read of any violation that occurred in previous meetings (if any).

2. Read the cause of violation.

3. Read remedy of violation.

## Figure 9. The method readPreviouslyGeneratedReports

## 4.6. The Practitioner Participant (PP) Class

The Practitioner Participant (PP) is the other class that inherits from the Practitioner class (see Figure 10). While the PF class represents a practitioner who is a facilitator, the Practitioner Participant class represents a practitioner who is a participant. The details of the practitioner participant class are demonstrated below. As before, we concentrate only on the unique method within this class, given that it inherits the attributes and methods from the practitioner class.

## Class practitionerParticipant

//methods of the practitioner participant

followEthicalProtocol();

## Figure 10. The practitionerParticipant class

The primary method within this practitioner participant class is called followEthicalProtocol() (see Figure 11). This followEthicalProtocol() method essentially reflects the operation of each participant to follow what the practitioner facilitator has implemented as the ethical protocol. For example, in the round-robin phase of collaboration (within the ethical protocol implemented by the practitioner facilitator), the participant practitioners should wait for their respective turn to contribute. They should not try to contribute out of turn, and they should make note if any other participant is violating this norm. A suggested outline of this method is provided below.

## Void followEthicalProtocol()

For each meta requirement in the metaRequireMentsList [] do the following

1. Ensure that it is not violated by self.

2. Ensure that it is not violated by others or by any feature of the technology.

3. If violated by self, take immediate remedial action (i.e. stop doing it).

4. If violated by others, notify them.

5. If the violation by others persists, bring to notice of the facilitator.

## Figure 11. The method followEthicalProtocol

## 4.7. The Technology (T) Class

The details of the technology class are represented below (see Figure 12). This class essentially consists of an array of features, denoted by features []. The significance of this array attribute is that technology has many features that may be used and implemented in an ethical manner. For example, the feature of enabling different communication channels is consistent with ensuring equality among those who may be unable to use a particular channel effectively. Similarly, the anonymity feature may support the freedom of expression requirement, or a default fixed-size input box, consistent with the equality requirement, could be provided to everybody.

## Class technology

//attributes of the class technology features [];

//methods of the class technology changeFeature(feature, reason); }

## Figure 12. The technology class

One potentially useful method in the Technology (T) class is named changeFeature (feature, reason). As explained before, this method could get invoked either from the implementEthicalProtocol() method or from the handleExceptionEthically() method of the practitioner facilitator class. Thus, the facilitator may use the changeFeature (feature, reason) method of the technology to “switch off” or “switch on” any feature of technology based on its appropriateness to the particular collaborative scenarios. The facilitator could use this method at the beginning of the collaboration process (the implementEthicalProtocol() method) or while the collaboration process is running and some specific exception calls for a change in the technology features (the handleExceptionEthically() method). A possible application of this changeFeature (feature, reason) method could be as follows. The technology in use could, for example, have differing levels of anonymity. One level could be that everyone actually knows what inputs are being provided by what person (i.e., no anonymity, or level 0 anonymity). The next level could be that only the facilitator knows who contributed what but not the participants (level 1 anonymity). The final level of anonymity could be that nobody (including the facilitator) knows who contributed what input (i.e., absolutely anonymous or level 2 anonymity). Assuming that the facilitator provided level 0 anonymity to start with (to uphold accountability), it might occur during the collaboration process that freedom of expression (another meta requirement) is hampered because of the lack of anonymity. Then the facilitator could increase the level of anonymity to level 1 so that freedom of expression is increased without compromising accountability. A suggested outline description of this method is provided below (see Figure 13).

Void changeFeature (feature, reason)

For the feature that has been passed as an argument, set the corresponding feature to “OFF” or “ON” corresponding to the reason for the change in the feature.

## Figure 13. The method changeFeature.

To summarize, in this section, we presented our conceptualization of the meta design of the ethica collaboration object. We also specified a rudimentary schema and methods. Of course, we acknowledge that alternate schemas could represent the EC class, and ours is but one of them. In the end, our collaboration object is a specification on how a socio-technical system should act. Object-oriented conventions have been used not because we believe that the entire process can be automated through the use of an object-oriented computer program, but because these conventions offer a logically coherent and elegant way to describe a program with human and technological components. In effect, through this object-oriented notation, we are providing a way to program a human system (such as collaboration group) that can be aided by technology in achieving its objectives.

## 5. Illustrating the CE artifact with an existing thinkLet

In this subsection, we discuss how our meta-design, particularly ideas underlying methods such as implementEthicalProtocol(), followEthicalProtocol(), and handleExceptionEthically(), may be integrated into existing thinkLets. For illustrative purposes, we have chosen a thinkLet called FreeBrainstorm (Briggs and de Vreede, 2005), the structure of which is presented in Appendix A. Given that the FreeBrainstorm thinkLet is expressed in structured English (and not in a formal notation such as UML), we do not use UML but instead draw upon ideas embedded in our meta design. We show (in Appendix B) how the adapted version informed by deontological ethics would appear using a representation approach similar to that used by the authors of the original FreeBrainstorm thinkLet. We provide references to the relevant methods, as appropriate, to allow the reader to see how our meta design is incorporated in the adapted version.

## 6. Discussion

Based on the design theory framework, this paper articulates a preliminary conceptual schema for an ethical collaboration class. It also delineates the principal elements of this conceptual schema: the practitioner facilitator class, the practitioner participant class, and the technology class. Essentially, our conception of ethical collaboration revolves around the ethical behaviors of practitioner facilitators and practitioner participants who are supported by appropriate features of the mediating technology.

A possible criticism of the ethical collaboration class presented is that it may not be easy to implement in practice, because of the idealistic and exclusive focus on ethics (without considering other values) within a collaboration context. Our response is that the focus on ethical theories in this paper for deriving underlying meta requirements does not need to be seen as denying the importance of (or the need to draw upon) other considerations in guiding collaboration processes. Rather, noting the relative absence of IS collaboration research based on explicit ethical considerations—in spite of past observations that ethical issues remain unanswered and, hence, need to be addressed in group collaboration (Briggs et al., 1997)—we have chosen to highlight the ethical aspect of collaboration.

Yet another criticism could be that the idea for an ethical collaboration process can be apparently more viable in public organizations than in for-profit organizations, for whom ethical collaboration may become a costly endeavor. For example, it may seem that an agent of public welfare (such as a city planning board) could employ such an ethical collaboration process better (because the focus is not on profits) than an agent of a private for-profit organization (because of the focus on profits). In private organizations, agents are employed by the “principal” (i.e., the organization) to undertake work for a specific purpose (e.g., providing efficient and high quality outcomes in the organizations’ interest) (Eisenhardt, 1989; Jones, 1995). So, it can be argued that if agents do not conform to the principal’s interest (which is inherently focused on reaching a quick and quality outcome) and instead focus on upholding the ethical standards of the decision process itself, then it may become costly for the principal to employ and maintain such agents. However, on closer reexamination, we can find ways to resolve this impasse by observing the linkages between economics and ethics (Jones, 1995). As noted by Jones (1995), according to agency theory, agency costs arise because of the need to minimize the two foremost reasons of agent failure—moral hazard and adverse selection. The former relates to shirking by the agent, while the latter relates to the agent behaving in a manner unexpected by the principal. The former reason is rendered somewhat inapplicable in our context because an ethically behaving agent (here the collaborating team) would, most likely, not indulge in shirking. For the second reason, we need to step back and understand the relation between ethics and economic benefits. Academics have argued, especially in recent times, that ethics and economics are strongly intertwined. For example, Cropanzano et al. (2001), based on Tyler’s (1987) work, argue that fairness or justice (essentially, a focus on ethics) is essentially germane to long-term economic benefits. In other words, organizations that follow an ethical perspective ultimately stand to gain, at least in the long run, in terms of economic profits (Boehm and Sullivan, 2000). This entire argument is put into perspective by Giacalone (2006), who argues that organizations that fail to understand ethical considerations shall “suffer the consequences of their choices” (p. 24). Given this established view that ethical considerations are economically beneficial in the long run, we can easily argue that an agent operating under explicit ethical considerations is actually helping an organization reach a longterm economic benefit, thus alleviating any concerns of adverse selection. For example, some of the many benefits could be greater employee satisfaction and productivity, social acceptability of the organization, and greater governmental support for an organization that follows a fair and just (i.e., ethical) process in all its business matters. All these would lead to economic benefits. It is important that the organizations understand this and promote agent-related processes that are also ethica rather than only efficient.

Also, we dwell on ethical considerations alone rather than a blend of different considerations at this stage because incorporating different values in this meta design would force us to make tradeoffs without knowing the value priorities of the context. Instead of arbitrarily blending values in the basic design of collaboration classes, we believe that it would be productive to design other classes, in parallel, that represent a variety of other relevant value considerations (e.g., efficiency, aesthetic, emotional, and so on). For example, we could design a class aimed at producing efficient collaboration, which would call for different technology features, different protocols, different characteristics of the participants and facilitator, and a different nature of training. Once a collection of these classes based on different values has been designed, it would be up to the “on-site” collaboration engineer to draw on predesigned classes and put together a collaboration class suitable for the context and its value priorities—which would involve using the object-oriented notions of multiple inheritance and overriding. In summary, our message is not that deontological ethics should be the only concern for collaboration, but rather that it is an important (and often overlooked) concern. Given that there have been few efforts to systematically include ethics as an integral part of the collaboration process, we believe that our paper offers a useful contribution.

Finally, we believe it may be worthwhile to outline possible ways in which the CE artifact developed in this paper can be evaluated. This endeavor is important, as design artifacts should be subjected to iterative evaluations, and the outcomes of those evaluations should inform the design artifact itself (Hevner et al., 2004). Of the many methodological approaches for evaluation, for illustrative purposes, we discuss two that seem to be particularly relevant: a controlled experimental method in a laboratory setting and an observational field study in an organization.

The experimental procedure, in the tradition of GSS experimental research, would have different groups, all collaborating using technology. Here, we discuss one possible experimental design using the pretest-posttest design method with treatment and control groups, drawing from the directions provided by Cook and Campbell (1979). The experimental design would look as noted below.

\*O1 and O2 denote observation 1 (pretest assessment) and observation 2 (posttest assessment) respectively

\*\*Treatment Groups; here X1 symbolizes the implementation of the meta design in the thinkLet guiding the group’s collaborative process

\*\*\*Control Groups; here X2 indicates the fact that the meta design is not inscribed into the thinkLet guiding the group’s collaboration process

## Figure 14. The experimental design for evaluating the artifact

Following the usual procedures of a pretest-posttest experimental design setup, both treatment and control groups would initially collaborate on the same given task. After a period of collaborative activity, they would be requested to answer a questionnaire measuring their perceptions of the constructs (ethical meta-requirements) of interest. This would, of course, require the researcher to develop measures capturing the meta requirements (e.g., consistency, freedom from bias, autonomy) similar to de Vreede and de Bruijn (1999). Following this pre-assessment, the treatment groups would collaborate using a thinkLet based on the meta design proposed in this paper (i.e., the treatment). At the same time, the control groups would collaborate on the same task using a thinkLet equivalent to the treatment group, but without the ethical meta-requirements inscribed. Once a certain time has elapsed, the two groups would again be asked to complete the questionnaire measuring their perceptions of the set of meta requirements that were addressed through the meta design (with suitable modifications to account for sensitization issues). A comparison of the two groups’ assessments would indicate if, indeed, the design artifact (more specifically, its instantiation in the experimental context) had an impact on the (ethical) nature of the collaboration process.

Along similar lines, Action Research (Baskerville and Myers, 2004; Reason and Bradbury, 2001) would be another potential strategy. The researcher would need to identify an organizational setting where it is clearly recognized that cross-functional collaborative meetings among, say, midlevel managers, while possibly efficient, are not conducted in line with the high ethical standards mandated by the company’s top management, who wish to be recognized as ethical leaders. After negotiating entry into such an organization, the researcher would first need to understand the status quo (i.e., the ethical problems associated with meetings) through interviews, questionnaires, and participant observations. The researcher would then need to collaboratively come up with the design of a theoretically informed “intervention” that would promote meetings conducted in accordance with key deontological principles. The intervention would be an instantiation of the meta design presented earlier. This design would be adapted to the context by collaborating with a variety of stakeholders. Having implemented the change, the researcher, in the spirit of a “controlled inquiry,” would need to evaluate the consequences of the intervention on the collaboration processes/experiences of the relevant stakeholders. The evaluation would provide not only an assessment of the situation but also feedback to the researcher regarding the “intervention,” in this case, the meta design. This would present the researcher an opportunity to modify the initial meta design and proceed to the next iteration of implementation followed by reflection. This process would improve the status quo and contribute to the development of a better meta design.

## 7. Contribution

We believe a key contribution of this study lies in its use of a systematic design theory approach to propose a preliminary ethical collaboration class. The use of a formal design approach is especially meaningful, since in the past, the themes informing the design of collaboration objects (such as thinkLets) have been captured from past experiences, not consciously derived from theoretical traditions. In using Walls et al.’s formal design framework, which requires the use of kernel theories to derive meta requirements for the artifacts, we respond to the call for the engineering of theoreticallyinformed collaborative work processes (Briggs, 2006).

The second contribution is that the work highlights the relevance of, and need for, a consideration of human ethical values in CE. Issues of ethics have been addressed in past collaboration literature (de Vreede and de Bruijn, 1999), and artifacts such as thinkLets have been reported to incorporate ethica concerns (de Vreede et al., 2006), but the efforts to this point may be characterized as ad hoc, and ethics has clearly not been a focal concern in the CE literature. To illustrate, in Table 3, we provide an assessment of some existing thinkLets (drawn from Briggs and de Vreede, 2005) with respect to the deontological meta requirements articulated in this paper. The table shows that while most thinkLets are not totally devoid of ethical considerations, ethics have not been systematically infused into the artifacts that form the building blocks for collaboration processes—a void we seek to address. Collaboration processes, even those sensitive to ethical concerns, have generally been more concerned with the ends (i.e., ability to come to a consensus, number of ideas generated, collaboration satisfaction, etc.) rather than the means. This reflects a latent consequentialist approach. In this paper, we systematically model an ethical collaboration process, not through a consideration of the ethical implications of collaboration outcome (which we argue is often determined by factors outside a collaboration engineer’s control), but by acknowledging that the process, irrespective of the ends, must promote the basic rights of participants in a collaborative process. We are not aware of past studies on collaboration that are based on a similar deontological understanding.

Table 3. An illustration of how existing thinkLets (as CE artifacts) compare with respect to Meta-requirements derived from deontological ethics

<table><tr><td>ThinkLet Name (from Briggs and de Vreede 2005)</td><td colspan="6">Meta Requirements</td></tr><tr><td></td><td>Respect for individual&#x27;s autonomy</td><td>Equality</td><td>Freedom of expression</td><td>Freedom from bias</td><td>Accountability</td><td>Consistency</td></tr><tr><td>Dealerschoice</td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>Plus-Minus Interesting</td><td></td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>Dimsum</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Crowbar</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>CheckMark</td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Leafhopper</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Richrelations</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fastfocus</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td></tr></table>

Third, we contribute to the reemerging stream of research on design of IS artifacts within the IS discipline. Design has been a relatively neglected aspect in leading IS journals in recent years (Iivari et al., 2006; Vessey et al., 2002); however, there has been a clear acknowledgment in the IS discipline of the need for more design science research that “engineers” sociotechnical artifacts. We are hopeful that this paper will be viewed as a novel contribution in this stream.

Fourth, we address (at least in part) several problems facing ethics research in IS. For example, according to Laudon (1995), this body of research:

 Is not well grounded in the classical or contemporary philosophical theories of ethics,

Has a disorganized topology because IS ethics has usually addressed problems in an ad hoc manner (e.g., piracy, hacking, etc.),

 Is neither normative nor prescriptive.

Our paper addresses each of these issues, at least partly. We draw upon the philosophical theories of ethics in proposing a meta design of a collaboration artifact. We seek to design this artifact not in an ad hoc manner but rather through a systematic coverage of the kernel theories from which appropriate meta requirements are discerned (Table 2). Finally, we address the issue that IS ethics research has been neither normative nor prescriptive. Since a design theory is essentially normative (Siponen and Iivari 2006; Gregor, 2006), the ethically informed design theory approach used here may be seen as an answer to the third concern above.

## 8. Implications for research

Our work also opens up multiple avenues for future research. Future research could investigate other kinds of theories for designing such artifacts based on different considerations. For example, in the human factors literature, a recent study by Brave et al. (2005) explores the effects of emotional expression of design artifacts on individual users. In the same vein, future research in CE could attempt to design collaboration artifacts based on theoretical understandings of human emotion (e.g., Morris and Feldman, 1996). Because collaboration is largely a social phenomenon, issues of human emotion assume importance. As mentioned earlier, these alternate design artifacts based on alternate considerations (e.g., ethics, emotion, etc.) could then be “mixed and matched” (through multiple inheritance) in order to develop the actual collaboration object for a specific scenario.

Future research could also involve numerous empirical studies to examine if the meta design (say, the EC class) could be instantiated into objects that could satisfy the meta requirements above when implemented (through satisfaction of testable hypotheses that are developed). Design and empirical endeavors are closely related, and in fact, one informs the other (March and Smith, 1995; Hevner et al., 2004). As described earlier, empirical studies could take numerous forms, such as lab experiments and action research, aimed at first understanding how this class may be instantiated and deployed, and then at providing an evaluation. The results of these empirical studies could guide us in refining design artifacts and design processes, and also suggest the applicability/inapplicability of the kernel theories.

## 9. Implications for practice

The study here has important implications for practice. It provides prescriptions for designing better ethically driven collaborative processes and, thus, incorporates prescriptions for ethical decision making. We believe the practical implementation of such practices would lead to a greater quality of work life and better satisfaction in terms of collaborative efforts. Furthermore, we believe the practica implementation would also result in a greater recognition of ethical issues among employees. All in all, collaborative work practices designed and implemented using the considerations presented here have a significant potential for impacting businesses and how they are managed.

Second, on a related note, this paper motivates a call to observe collaborative meetings closely in order to assess the degree to which the underlying process of collaboration may be seen as ethical. With a clear assessment of the baseline, organizational decision makers can be given a more tangible sense of the need to seriously incorporate ethical principles into collaborative settings. We note that while ethics is often acknowledged to be an important issue in human collaboration, it is generally not given due attention. If the proposed baseline assessment does establish a lack of ethics in collaboration practices, this would provide great impetus to explicitly incorporate ethical principles into their design. We believe that CE professionals responsible for designing ethical collaboration processes and practices will find the guidelines provided in this paper to be useful and actionable.

Finally, this paper may also have useful implications for IS (and other) educators in disciplines where the importance of collaboration is well understood. For example, many courses within various disciplines involve and encourage collaborative learning and accomplishment of work through group projects. Implementation of such an ethical collaboration class in order to foster better collaboration and learning could be deemed a significant teaching innovation (with the course instructor serving as the facilitator). This may help students learn to respect each other and collaborate in an ethica manner, thereby ultimately contributing to the development of a more ethically informed workforce.

## 10. Conclusion

It is clear that collaboration is a necessary condition for contemporary organizations to succeed. Yet collaboration is a complex human process. Basic human rights tend to be frequently violated in the interest of personal egos, hidden agendas, efficiency, or even just a façade of efficiency. While experienced facilitators may be able to avoid ethical pitfalls in the collaboration process, most organizations around the world simply do not have access to high-quality facilitators. The field of collaboration engineering (CE) sees one of its core missions to offer such organizations a systematic set of instructions that can guide collaborative processes appropriately, even in the absence of experienced facilitators. Our CE efforts have been directed toward developing such a systematic, albeit preliminary, specification of a system of instructions represented as an ethical collaboration class using object-oriented conventions. The hope is that, if implemented, the artifact would enable the organization to conduct collaboration in a manner that would be characterized as “ethical.” Clearly, much remains to be investigated in this exciting area of Collaboration Engineering, and we hope our work provides some impetus to this stream of research.

## References

Alexander, C. (1979) The Timeless Way of Building. New York, NY: Oxford University Press.

Alexander, C. (1980) The Nature of Order: an Essay on the Art of Building and the Nature of the Universe. Berkeley, CA: The Center for Environmental Structure.

Anscombe, G. E. M. (1958) "Modern Moral Philosophy," Philosophy (33) pp. 1-19.

Anson, R., R. Bostrom, and B. Wynne (1995) "An Experiment Assessing Group Support System And Facilitator Effects on Meeting Outcomes," Management Science (41) 2, pp. 189-208.

Applegate, L.M., B.R. Konsynski and J.F. Nunamaker (1986) “Model Management Systems: Designs for Decision Support,” Decision Support Systems. (2)1, pp. 81–91.

Baskerville, R. and M. D. Myers (2005) "Special Issue on Action Research in Information Systems: Making IS Research Relevant to Practice--Foreward," MIS Quarterly, 28 (3), pp. 329-335.

Bentham, J. (1789/1970) An Introduction to the Principles of Morals and Legislation. New York, NY: Methuen.

Boehm, B. and K. J. Sullivan (2000) “Software Economics: A Roadmap,” in A. Finkelstein (ed.) The Future of Software Engineering.

Bonczek, R.H., C.W. Holsapple, and A.B. Whinston (1980) “Future Directions for

Bonczek, R.H., C.W. Holsapple, and A.B. Whinston (1981) “A Generalized Decision Support System Using Predicate Calculus and Network Database Management,” Operations Research (29), pp. 263–281.

Bragge, J., H. Merisalo-Rantanen, and P. Hallikainen (2005) "Gathering Innovative End-User Feedback for Continuous Development of Information Systems: A Repeatable and Transferable E-Collaboration Process," IEEE Transactions on Professional Communication (48) 1, pp. 55-67.

Brave, S., C. Nass, and K. Hutchinson (2005) "Computers That Care: Investigating The Effects of Orientation of Emotion Exhibited by an Embodied Computer Agent," International Journal of Human-Computer Studies (62) 2, pp. 161-178.

Briggs, R.O. (2006) “On Theory-driven Design and Deployment of Collaboration Systems,” International Journal of Human-Computer Studies (64) 7, pp. 573-582.

Briggs, R. O. and G.-J. De Vreede (2005) ThinkLets: Building Blocks for Concerted Collaboration. Omaha.

Briggs, R. O., G.-J. de Vreede, and A. Massey (2006) "Call for Papers for Special Issue on Collaboration Engineering " Journal of the Association for Information Systems.

Briggs, R. O., G.-J. deVreede, and J. F. Nunamaker (2003) "Collaboration Engineering with Thinklets to Pursue Sustained Success With Group Support Systems," Journal of Management Information Systems (19) 4, pp. 31-64.

Briggs, R. O., Jay F. Nunamaker, and J. Ralph H. Sprague (1997) "1001 unanswered research questions in GSS," Journal of Management Information Systems (14) 3, pp. 3-21.

Brummer, J. J. (1986) "Accountability and the Restraint of Freedom: A Deontological Case for the Stricter Standard of Corporate Disclosure," Journal of Business Ethics (5) 2, pp. 155-164.

Chae, B., J.F. Courtney, and D.B. Paradice (2005) “Incorporating an Ethical Perspective into Decision Support Systems Design,” Decision Support Systems (40) 2, pp. 197–212.

Chidambaram, L. (1996) "Relational Development in Computer-Supported Groups," MIS Quarterly (20) 2, pp. 143-165.

Choobineh, J. M. Mannino, J. Nunamaker and B. Konsynski (1988) “An Expert Database Design System Based on Analysis of Forms,” IEEE Transactions on Software Engineering (14)2.

Churchman, C.W. (1971) The Design of Inquiring Systems: Basic Concepts of Systems and Organization. New York, NY: Basic Books.

Clawson, V. and R. Bostrom (1996) "Research-Driven Facilitation Training for Computer Support Environments," Group Decision and Negotiation (5) pp. 7-29.

Courtney, J.F. (2001) “Decision Making And Knowledge Management in Inquiring Organizations: Toward a New Decision-Making Paradigm for DSS,” Decision Support Systems (31), pp. 17– 38.

Cook, T., and D. Campbell (1979) Quasi-experimentation: Design and Analysis Issues for Field Settings. Boston: Houghton Mifflin.

Cropanzano, R., Z. S. Byrne, D. R. Bobocel, and D. E. Rupp (2001) “Moral Virtues, Fairness Heuristics, Social Entities, and Other Denizens of Organizational Justice,” Journal of Vocational Behavior, (58), pp. 164–209.

Culnan, M. (1986) “The Intellectual Development of Management Information Systems,

Culnan, M. J. and E.B. Swanson (1986) “Research in Management Information

Systems, 1980-1984: Points of Work And Reference,” MIS Quarterly (10) 3, pp. 289-302.

Den Hengst, M. and G.-J. de Vreede (2004) "Collaborative Business Engineering: A Decade of Lessons from the Field," Journal of Management Information Systems (20) 4, pp. 85-113.

DeSanctis, G. and R. B. Gallupe (1987) "A Foundation for the Study of Group Decision Support Systems," Management Science (33) 5, pp. 589-609.

DeSanctis, G. and M. S. Poole (1994) "Capturing The Complexity in Advanced Technology Use: Adaptive Structuration Theory," Organization Science (5) 2, pp. 121-147.

De Vreede, G.-J. and H. de Bruijn (1999) "Exploring The Boundaries of Successful GSS Application: Supporting Inter-Organizational Policy Networks," Database for Advances in Information Systems (30) 3/4, pp. 111-130.

De Vreede, G.-J., G. L. Kolfschoten, and R. O. Briggs (2006) "Thinklets: A Collaboration Engineering Pattern Language," International Journal of Computer Applications in Technology (25) 2/3, pp. 140-154.

Donaldson, Thomas and T. W. Dunfee (1994) “Toward a Unified Conception of Business Ethics: Integrative Social Contracts Theory,” Academy of Management Review 19 (2): 252-284.

Eisenhardt, K. M. (1989) “Agency theory: An assessment and Review,” Academy of Management Review, (14), pp. 57–74.

Floridi, L. (2002) "On The Intrinsic Value of Information Objects and the Infosphere," Ethics and Information Technology (4) 4, pp. 287-304.

Friedman, B. (1996) "Value-Sensitive Design," Interactions (3) 6, pp. 16-23.

Friedman, B. and P. H. Kahn (2003) “Human values, ethics, and design,” in J. A. Jacko and A. Sears (Eds.) The Human-Computer Interaction Handbook, Mahwah, NJ: Lawrence Erlbaum Associates., pp. 1177-1201.

Friedman, B., P. H. Kahn, and A. Boring (2006) “Value Sensitive Design and Information Systems,” in P. Zhang and D. Galletta (Eds.) Human-Computer Interaction in Management Information Systems: Foundations., New York, NY: M.E. Sharpe.

Fuller, M. A., A. M. Hardin, and R. M. Davison (2007) "Efficacy in Technology-Mediated Distributed Teams," Journal of Management Information Systems (23) 3, pp. 209-235.

Giacalone, R.A. (2006) “New Ethics in the Office,” BizEd, September/October 2006, p. 24.

Gregor, S. (2006) "The Nature of Theory in Information Systems," MIS Quarterly (30) 3, pp. 611-642.

Griffith, T. L., M. A. Fuller, and G. B. Northcraft (1998) "Facilitator Influence in Group Support Systems: Intended and Unintended Effects," Information Systems Research (9) 1, pp. 20-36.

Grunbacher, P., M. Halling, S. Biffl, H. Kitapci et al. (2004) "Integrating Collaborative Processes and Quality Assurance Techniques: Experiences from Requirements Negotiation," Journal of Management Information Systems (20) 4, pp. 9-29.

Hevner, A. R., S. T. March, J. Park, and S. Ram (2004) "Design Science in Information Systems Research," MIS Quarterly (28) 1, pp. 75-105.

Hirschheim, R. and H. K. Klein (1989) "Four Paradigms of Information Systems Development," Association for Computing Machinery. Communications of the ACM (32) 10, pp. 1199-1216.

Hirschheim, R. and M. Newman (1991) "Symbolism and Information Systems Development: Myth, Metaphor and Magic," Information Systems Research (2) 1, pp. 29-62.

Hosmer, L. T. (1995) "Trust: The Connecting Link Between Organizational Theory and Philosophical Ethics," The Academy of Management Review (20) 2, pp. 379-403.

Huang, W. W. and K. K. Wei (2000) "An Empirical Investigation of The Effects of Group Support Systems (GSS) and Task Type on Group Interactions from an Influence Perspective," Journal of Management Information Systems (17) 2, pp. 181-206.

Hursthouse, R. (1999) On Virtue Ethics. Oxford, UK: Oxford University Press.

Iivari, J., R. Hirschheim, and H. K. Klein (2000) "A Dynamic Framework for Classifying Information Systems Development Methodologies and Approaches," Journal of Management Information Systems (17) 3, pp. 179-218.

Iivari, J., J. Parsons, and Y. Wand (2006) "Research in Information Systems Analysis and Design: Introduction to the Special Issue," Journal of the Association for Information Systems (7) 8, pp. 509-513.

Jarvenpaa, S. L. and D. Leidner (1998) "Communication and trust in global virtual teams," Journal of Computer-Mediated Communication (3) 4.

Jones, T. M. (1995) “Instrumental Stakeholder Theory: A Synthesis of Ethics and

Economics,” Academy of Management Review, (20), pp. 404–437.

Kang, D. and R. Santhanam (2003) "A Longitudinal Field Study of Training Practices in a Collaborative Application Environment," Journal of Management Information Systems (20) 3, pp. 257-281.

Kant, I. (1804/1994) Ethical Philosophy: Grounding for the Metaphysics of Morals (trans. James W. Ellington). Indianapolis, IN: Hackett.

Kelly, G. G. and R. P. Bostrom (1997) "A Facilitator's General Model for Managing Socioemotional Issues in Group Support Systems Meeting Environments," Journal of Management Information Systems (14) 3, pp. 23-44.

Klein, H. K. and R. Hirschheim (2001) "Choosing Between Competing Design Ideals in Information Systems Development," Information Systems Frontiers (3) 1, pp. 75-90.

Kolfschoten, G. L., R. O. Briggs, G. J. Vreede, DE, P. H. M. Jacobs et al. (2006) "Conceptual Foundation of the ThinkLet Concept for Collaboration Engineering," International Journal of Human Computer Studies (64), pp. 611-621.

Kraus, W. A. (1980) Collaboration in Organizations: Alternatives to Hierarchy. New York, NY: Human Sciences Press.

Laudon, K. C. (1995) "Ethical concepts and information technology," Communications of the ACM (38) 12, pp. 33-39.

Lee, A. S. (2007) “Action is an Artifact: What Action Research and Design Science Offer to Each Other,” in N. Kock (Ed.) Information Systems Action Research: An Applied View of Emerging Concepts and Methods, New York: Springer Publishing, pp. 43-60.

Lenman, J. (2000) "Consequentialism and cluelessness," Philosophy and Public Affairs (29), pp. 342- 370.

Limayem, M. (2006) "Human Versus Automated Facilitation in the GSS Context," Database for Advances in Information Systems (37) 2/3, pp. 156-166.

March, S. T. and G. F. Smith (1995) "Design And Natural Science Research on Information Technology," Decision Support Systems (15) 4, pp. 251-266.

McGrath, J. (1991) "Time, Interaction, And Performance (TIP): A Theory of Groups," Small Group Research (22), pp. 147-174.

Mill, J. S. (1861/1979) Utilitarianism Indianapolis, IN: Hackett Publishing.

Mittleman, D. D., R. O. Briggs, and J. F. Nunamaker (2000) "Best Practices in Facilitating Virtual Meetings: Some Notes From Initial Experience," Group Facilitation (2) 2, pp. 5-14.

Moor, J. H. (2001) "The Future of Computer Ethics: You Ain't Seen Nothin' Yet!," Ethics and Information Technology (3) 2, pp. 89-91.

Moore, G. E. (1903/1959) Principia Ethica. Cambrige, UK: Cambridge University Press.

Morris, J. A. and D. C. Feldman (1996) "The Dimensions, Antecedents, and Consequences of Emotional Labor," The Academy of Management Review (21) 4, pp. 986-1010.

Nietzsche, F. W. (1886/1969) Thus Spake Zarathustra (Trans. R. J. Hollingdale). Harmondsworth: Penguin.

Nissenbaum, H. (1997) “Accountability in A Computerized Society,” in B. Friedman (Ed.) Human Values and The Design of Computer Technology, Stanford, CA: CSLI.

Nunamaker, J. F., R. O. Briggs, D. D. Mittleman, D. R. Vogel Et Al. (1996) "Lessons From A Dozen Years of Group Support Systems Research: A Discussion of Lab and Field Findings," Journal of Management Information Systems (13) 3, pp. 163-207.

Nunamaker, J. F., M. Chen, and T. D. M. Purdin (1991a) "Systems Development in Information Systems Research," Journal of Management Information Systems (7) 3, pp. 89-106.

Nunamaker, J. F., A. R. Dennis, J. S. Valacich, D. R. Vogel Et Al. (1991) "Electronic Meeting Systems To Support Group Work," Association for Computing Machinery. Communications of The ACM (34) 7, pp. 40-61.

O’Neill, O. (1996) Towards Justice and Virtue: A Constructive Account of Practical Reasoning. Cambridge, UK: Cambridge University Press.

Payne, D. and B. E. Joyner (2006) "Successful U.S. Entrepreneurs: Identifying Ethical Decision-Making and Social Responsibility Behaviors," Journal of Business Ethics (65) 3, pp. 203-217.

Rawls, J. (1971) A Theory of Justice Cambridge, MA: Harvard University Press.

Reason, P., and Bradbury, H. (2001) Handbook of Action Research: Participative Inquiry and Practice. London, UK: Sage.

Sarker, S. and S. Sahay (2003) "Understanding Virtual Team Development: An Interpretive Study,"

Journal of Association for Information Systems (4), pp. 1-38.

Sarker, S. and S. Sahay (2004) "Implications of Space and Time for Distributed Work: An Interpretive Study of US-Norwegian Systems Development Teams," European Journal of Information Systems (13) 1, pp. 3-20.

Sarker, S., J. Valacich, and S. Sarker (2005) “Technology Adoption By Groups: A Valence Perspective,” Journal of The AIS, (6) 2, pp. 37-72.

Schon, D. A. (1993) The Reflective Practitioner: How Professionals Think in Action. New York, NY: Basic Books.

Shneiderman, B. and A. Rose (1997) “Social Impact Statements: Engaging Participation in Information Technology Design,” in B. Friedman (Ed.) Human Values and The Design of Computer Technology, Stanford, CA: CSLI.

Simon, H. A. (1996) The Sciences of The Artificial. Cambridge, MA: MIT Press.

Singer, M. (1977) "Actual Consequence Utilitarianism," Mind (86), pp. 67-77.

Siponen, M. and J. Iivari (2006) "Six Design Theories for IS Security Policies and Guidelines," Journal of The Association for Information Systems (7) 7, pp. 445-472.

Sprague, R. (1980) “A Framework for The Development of Decision Support Systems,” MIS Quarterly 4 (1980), pp. 1–24.

Sprague, R. and E. Carlson (1982) Building Effective Decision Support Systems. Englewood Cliffs, NJ: Prentice Hall

Tyler, T. R. (1987) “Conditions Leading To Value-Expressive Effects in Judgments of Procedural Justice: A Test of Four Models,” Journal of Personality and Social Psychology, (52), pp. 333– 344.

Urry, J. (2002) "Mobility and Proximity," Sociology: The Journal of The British Sociological Association (36) 2, pp. 255-274.

Vessey, I., V. Ramesh, and R. L. Glass (2002) "Research in Information Systems: An Empirical Study of Diversity in The Discipline and its Journals," Journal of Management Information Systems (19) 2, pp. 129-174.

Walls, J. G., G. R. Widmeyer, and O. A. El-Sawy (1992) "Building An Information System Design Theory for Vigilant EIS," Information Systems Research (3) 1, pp. 36-59.

Walsham, G. (2001) Making A World of Difference: IT in A Global Context. Chichester: Wiley.

Warkentin, M. and P. M. Beranek (1999) "Training To Improve Virtual Team Communication," Information Systems Journal (9) 4, pp. 271-289.

Winograd, T. (1994) "Categories, Disciplines, and Social Coordination," Computer Supported Cooperative Work (2) 3, pp. 191-197.

## Appendix A.

## Setup

1. Create brainstorming pages in Electronic Brainstorming:

a. One page for each participating team member, plus one extra.

b. An additional page for each 10 participants.

c. Examples:

d. For 6 participants create 7 pages (6 + 1).

e. For 10 participants create 12 pages (10 + 1 + 1).

f. For 20 participants create 23 pages (20 + 1+ 2).

2. Enter the Brainstorming Question into the EBS tool.

Steps

## 1. Say This:

a. Please click the “Go” button. The system will bring you an empty electronic page.

b. Each of you now has a different electronic page. You will each start on a different electronic page.

c. You may each type one idea, up to 400 characters long onto that page. Then you must click the submit button to send the page back to the group.

d. The system will randomly bring you back a different page. That page may have somebody else’s ideas on it.

e. When you see a page with somebody else’s ideas on it, you may respond in three ways:

i. i You may agree with an idea by adding detail to it.

ii. ii You may argue against an idea.

iii. iii You may be inspired to contribute a completely new idea.

f. You may type exactly one idea on the new page. Then you must send that page back to the group. The system will bring you a new page.

g. We will continue swapping pages and submitting ideas (Until you run out of ideas; for X minutes).

h. Any questions? You may begin.

## Appendix B.

<table><tr><td colspan="2">Set up related to the Technology for the Collaboration Process</td></tr><tr><td colspan="2">1. Create different user ids for the collaborators in order to log on to the existing Electronic Brainstorming (EBS) tool /* new feature of the ethical FreeBrainstorm thinkLe t*/</td></tr><tr><td colspan="2">2. Enter the Brainstorming question into the EBS Tool /*feature of the original FreeBrainstorm thinkLet */</td></tr><tr><td colspan="2">3. Create brainstorming Pages for each Participant, one page for each participant with a pre-defined text area which is equal for everybody /* modified feature of the original FreeBrainstorm thinkLet */</td></tr><tr><td colspan="2">New setup pertaining to all ethical thinkLets, implementing aspects of implementEthicalProtocol()</td></tr><tr><td colspan="2">4. Refer to the meta requirementsa. For each meta requirementi. For each feature of EBS Tool1. Check if the feature violates the meta requirement2. If violation, adjust the features appropriately, else leave it as is.</td></tr><tr><td colspan="2">New setup pertaining to the ethical FreeBrainstorm thinkLet, implementing aspects of implementEthicalProtocol()</td></tr><tr><td colspan="2">5. Create a new page after the login page which contains the following articulation of the meta requirementsa. Your participation in this FreeBrainstorming exercise is inherently valuable, irrespective of whether the ideas you provide are implemented or not. One of the aims of the FreeBrainstorming exercise is to foster a free interaction of individuals.b. Since the aim of this collaboration is to freely exchange ideas from everybody, all participants would be equally treated as a possible source of new ideasc. You should not intercept the free flow of ideas from anybody, but other than that, you are free to express any views you deem pertinent.d. Remember, that since this is FreeBrainstorming, you need to offer relevant ideas and also listen to others with an open mind. If you want to criticize an idea because you cannot relate to it or have a negative reaction to it (or a priori view of it), think twice. Remember that your ideas could also be similarly criticized by others. Unless you attach much less importance to your pre-conceived negative (or even positive) notions about some idea, you will not be able to appreciate others&#x27; viewpoints. Different viewpoints are especially encouraged in a FreeBrainstorm collaboration process. Also, you should not criticize some idea just because it comes from a person with whom you do not share a rapport or have a preexisting conflict (You will know the person since the user id would accompany the inputs).e. Since this is a FreeBrainstorming scenario, it is likely that many ideas will be generated. Keeping this in mind, each individual providing the ideas should get credit for his/her ideas, even if the ideas are not implemented finally. The effort that you put in should be recognized.f. Remember that since this is FreeBrainstorming, there will be a lot of new ideas generated that you may not relate to. In such cases, please respond in a polite manner. Remember that your ideas may appear equally strange to somebody else and you would want them to respond to you in a polite manner. Also do not use</td></tr></table>

a. You may agree with an idea by adding detail to it. b. You may argue against an idea.

language that might seem to be disrespectful to any one, just as you would not want them to use disrespectful language toward you.

Articulation prior to the collaboration, implementing aspects of implementEthicalProtocol() and followEthicalProtocol()

6. Please log on to the system using your user id and password. /\* new feature for the ethical FreeBrainstorm thinkLet \*/

7. Once you log on, the system will bring you to an electronic page that details certain values that should be upheld during the collaboration process. (created in step 5 above) /\* new feature for the ethical FreeBrainstorm thinkLet \*/

8. Once you have read through the articulation of the values that need to be upheld during the collaboration process, please click on the “I accept” button at the bottom of the page. If you have any questions regarding those values, please ask the facilitator immediately /\* new feature for the ethical FreeBrainstorm thinkLet \*/

9. You will then be redirected to a new empty page. /\* feature of the original FreeBrainstorm thinkLet \*/

10. This is the page where you can type in your inputs during the collaboration process. Please feel free to provide any idea you might think is of relevance to this collaboration agenda. /\* modified feature from the original FreeBrainstorm thinkLet \*/

11. Once you have provided all your inputs, please click on the submit button in order to submit all your ideas to the entire group. When you submit your page(s), your user id will be accompanied together with all your inputs, so that you will get credit for your inputs. /\* modified feature from the original FreeBrainstorm thinkLet \*/

12. The system will randomly bring you back a different page. That page would have somebody else’s ideas on it. /\* feature of the original FreeBrainstorm thinkLet \*/

13. When you see a page with somebody else’s ideas on it, you may respond in three ways: /\* feature of the original FreeBrainstorm thinkLet \*/

14. After your new inputs, click on the “submit” button to send the pages back to the group; the system will bring you a new set of pages. /\* feature of the original FreeBrainstorm thinkLet \*/

15. This process of contribution and exchange of ideas would initially be continued for X minutes, which will be available to every person. After that time, there shall be a time allotted (Y minutes) where somebody wanting to provide any additional inputs may request a small time slot to the facilitator. /\* modified feature from the original FreeBrainstorm thinkLet \*/

16. Remember that at any point of time any of the values should not be compromised and the facilitator would monitor the proceedings accordingly. /\* new feature for any ethical thinkLet \*/

17. If you see any violation (of the values), please use appropriate channel provided to point out to the violating individual (assuming that anonymity feature is not in effect). /\* new feature for an ethical FreeBrainstorm thinkLet \*/

18. If violation persists, bring this to the attention of the facilitator /\* new feature for any ethical thinkLet \*/

19. If you feel that any feature of the tool provided is resulting in a violation of values you have been informed of, please bring to the notice of the facilitator /\* new feature for any ethical thinkLet \*/

20. If you have any questions you may ask them. If none of you have any more questions, you may begin. /\* feature of the original FreeBrainstorm thinkLet \*/

Steps related to handling ethical exceptions during the collaborative process, implements

## aspects of handleExceptionEthically() - generic to all ethical thinkLets

21. For Facilitator -- Monitor the collaboration proceedings and take appropriate action a. Check the input pages being submitted at frequent intervals in order to make sure that none of the values you explained to the team above are being compromised.

b. If you feel that there are any values being violated please notify the corresponding individual(s) that they should discontinue doing so. You can do this through the alternate electronic mechanism that the EBS tool provides to you to communicate solely with each participant.

c. If you feel that the values are still being violated by the concerned individual(s), temporarily stop the proceedings by sending out an electronic message to all the participants.

d. Re-emphasize the values to the participants and their implications on the participants’ behaviors.

e. If you feel that any feature of the technology is hindering the collaboration process, please switch on/off that feature accordingly.

f. Start the collaboration proceedings once more g. Keep monitoring and verify that the same values or different values are not being violated.

h. If the violations are repeated, repeat steps c through g. If the violations do not seem to be easily resolved, consider taking radical steps (e.g., expelling the violator(s), or terminating the collaboration session)

Figure B. The Ethically modified FreeBrainstorm thinkLet

## About the authors

Sutirtha Chatterjee completed his PhD at Washington State University in 2008 and is now an Assistant Professor of Information Technology at Millikin University. Prior to pursuing his PhD, Sutirtha held a degree in Computer Science and Engineering from Jadavpur University, India and worked in the IT industry as a software engineer for five years. Sutirtha pursues research in the areas of IS Ethics, Electronic Markets, and Mobile Work and its application to healthcare. His research has been published at the European Journal of Information Systems (EJIS), Decision Support Systems (DSS), and Communications of the AIS (CAIS). He has also presented (or will be presenting) his work at various conferences such as the Hawaii International Conference on System Sciences, European Conference on Information Systems, Academy of Management Annual Meeting, and Americas Conference on Information Systems. He also received the Dean's Excellence Award for outstanding graduate student researcher within the entire College of Business at Washington State University in 2008.

Suprateek Sarker is an Associate Professor and Parachini Faculty Fellow at Washington State University, Pullman. His research interests include IT-enabled business process change, virtual and mobile collaboration, offshoring, and qualitative research methods. He is currently serving his second term as Associate Editor of the MIS Quarterly, and he is on the editorial boards IT & People, IEEE Transactions on Engineering Management, Information Technology for Development, and JITCAR. He has also served as an editorial board member for the Journal of the AIS (Special Issue) and as a Senior Editor for DATA BASE (Special Issue). He is a past recipient of the Stafford Beer Medal from the OR Society, UK for his co-authored work on virtual collaboration (with S. Sahay).

Mark A. Fuller is the Chair of the Department of Information Systems at Washington State University, the Director for Professional Business Programs for the College of Business, and holds the Philip L. Kays Distinguished Professorship in Information Systems. Professor Fuller received his Ph.D. in Management Information Systems from the University of Arizona. His research focuses on virtual teamwork, technology supported learning, and trust and efficacy in technology-mediated environments, and has appeared in outlets such as Information Systems Research, Management Information Systems Quarterly, Journal of Management Information Systems, Decision Sciences, Journal of the Association for Information Systems, and Decision Support Systems. Professor Fuller has won multiple teaching awards, has published a textbook on Information Systems Project Management, and has taught graduate and undergraduate courses on a variety of topics, including global information systems and strategy, information systems project management, and collaborative technology.

Copyright © 2009, by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers for commercial use, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via e-mail from ais@gsu.edu.

# JAm Ss

ISSN: 1536-9323

Editor Kalle Lyytinen Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Robert Fichman</td><td>Boston College, USA</td><td>Dennis Galletta</td><td>University of Pittsburgh, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Robert Kauffman</td><td>University of Minnesota, USA</td><td>Frank Land</td><td>London School of Economics, UK</td></tr><tr><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td></tr><tr><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Michael Wade</td><td>York University, Canada</td><td>Ping Zhang</td><td>Syracuse University, USA</td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Kemal Altinkemer</td><td>Purdue University, USA</td></tr><tr><td>Michael Barrett</td><td>University of Cambridge, UK</td><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td></tr><tr><td>Michel Benaroch</td><td>University of Syracuse, USA</td><td>Francois Bodart</td><td>University of Namur, Belgium</td></tr><tr><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td><td>Susan A. Brown</td><td>University of Arizona, USA</td></tr><tr><td>Tung Bui</td><td>University of Hawaii, USA</td><td>Andrew Burton-Jones</td><td>University of British Columbia, Canada</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Mike Chiasson</td><td>Lancaster University, UK</td><td>Mary J. Culnan</td><td>Bentley College, USA</td></tr><tr><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td><td>Samer Faraj</td><td>McGill university, Canada</td></tr><tr><td>Chris Forman</td><td>Carnegie Mellon University, USA</td><td>Ola Henfridsson</td><td>Viktoria Institute &amp; Halmstad University, Sweden</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Hemant Jain</td><td>University of Wisconsin-Milwaukee, USA</td><td>Bill Kettinger</td><td>University of South Carolina, USA</td></tr><tr><td>Rajiv Kohli</td><td>College of William and Mary, USA</td><td>Mary Lacity</td><td>University of Missouri-St. Louis, USA</td></tr><tr><td>Ho Geun Lee</td><td>Yonsei University, Korea</td><td>Jae-Nam Lee</td><td>Korea University</td></tr><tr><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td><td>Ji-Ye Mao</td><td>Renmin University, China</td></tr><tr><td>Anne Massey</td><td>Indiana University, USA</td><td>Emmanuel Monod</td><td>Dauphine University, France</td></tr><tr><td>Michael Myers</td><td>University of Auckland, New Zealand</td><td>Fiona Fui-Hoon Nah</td><td>University of Nebraska-Lincoln, USA</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Brian Pentland</td><td>Michigan State University, USA</td></tr><tr><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td><td>Jaana Porra</td><td>University of Houston, USA</td></tr><tr><td>Sandeep Purao</td><td>Penn State University, USA</td><td>T. S. Raghu</td><td>Arizona State University, USA</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td></tr><tr><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td></tr><tr><td>Ben Shao</td><td>Arizona State University,USA</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Katherine Stewart</td><td>University of Maryland, USA</td></tr><tr><td>Mani Subramani</td><td>University of Minnesota, USA</td><td>Burt Swanson</td><td>University of California at Los Angeles, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Jason Thatcher</td><td>Clemson University, USA</td></tr><tr><td>Ron Thompson</td><td>Wake Forest University, USA</td><td>Christian Wagner</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Eric Walden</td><td>Texas Tech University, USA</td><td>Eric Wang</td><td>National Central University, Taiwan</td></tr><tr><td>Jonathan Wareham</td><td>ESADE, Spain</td><td>Stephanie Watts</td><td>Boston University, USA</td></tr><tr><td>Bruce Weber</td><td>London Business School, UK</td><td>Tim Weitzel</td><td>Bamberg University, Germany</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Kevin Zhu</td><td>University of California at Irvine, USA</td><td>Ilze Zigurs</td><td>University of Nebraska at Omaha, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>Eph McLean</td><td>AIS, Executive Director</td><td colspan="2">Georgia State University, USA</td></tr><tr><td>J. Peter Tinsley</td><td>Deputy Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
