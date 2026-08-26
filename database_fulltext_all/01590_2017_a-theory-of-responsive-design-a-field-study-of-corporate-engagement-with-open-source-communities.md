---
otero_id: 1590
otero_key: "8ZYX277A"
title: "A Theory of Responsive Design: A Field Study of Corporate Engagement with Open Source Communities"
authors: "Matt Germonprez; Julie E. Kendall; Kenneth E. Kendall; Lars Mathiassen; Brett Young; Brian Warner"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0662"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/8ZYX277A/fulltext/images/5ceb392a6b769b49d5597a609074c7957f2ef8e2d69568f51a3f14092965c214.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## A Theory of Responsive Design: A Field Study of Corporate Engagement with Open Source Communities

Matt Germonprez, Julie E. Kendall, Kenneth E. Kendall, Lars Mathiassen, Brett Young, Brian Warner

To cite this article:

Matt Germonprez, Julie E. Kendall, Kenneth E. Kendall, Lars Mathiassen, Brett Young, Brian Warner (2016) A Theory of Responsive Design: A Field Study of Corporate Engagement with Open Source Communities. Information Systems Research

Published online in Articles in Advance 23 Nov 2016

http://dx.doi.org/10.1287/isre.2016.0662

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/8ZYX277A/fulltext/images/9490d5d41cad62c5df12bbd25423f92a20922ac4a8591d1484c12b7630ef2d51.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Theory of Responsive Design: A Field Study of Corporate Engagement with Open Source Communities

Matt Germonprez

Information Systems and Qualitative Analysis, College of Information Science and Technology, University of Nebraska at Omaha, Omaha, Nebraska 68182, mgermonprez@unomaha.edu

Julie E. Kendall, Kenneth E. Kendall

School of Business, Rutgers University, Camden, New Jersey 08102 {julie@thekendalls.org, ken@thekendalls.org}

Lars Mathiassen

GRA Eminent Scholar and Professor of Computer Information Systems, Center for Process Innovation, J. Mack Robinson College of Business, Georgia State University, Atlanta, Georgia 30303, lmathiassen@ceprin.org

Brett Young

Management Information Systems, School of Business, Georgia Gwinnett College, Lawrenceville, Georgia 30043, byoung9@ggc.edu

Brian Warner

Manager of Open Source Engineering and Strategy, Samsung Research America, Mountain View, California 94043, brian.warner@linux.com

lthough our general knowledge about open source communities is extensive, we are only beginning to understand the increasingly common practices by which corporations design software through engagement with these communities. In response, we combine design theorizing with field-study research (1) to analyze rich qualitative data from over 40 corporations participating in the Linux open source community and (2) to synthesize the observed corporate-open source community engagements into a new type of information systems design theory that we call responsive design. Empirically, we document how corporate participants in these contexts respond to market decisions, interdependent ideologies, and distributed relationships by continuously establishing and maintaining connections with community members; connections that stem from the social and material rules inherent in the open source community. Based on these observations, we create the theory of responsive design as a particular form of corporate software design which, beyond the inclusion of external participants, distinguishes itself from traditional monocentric design in which one corporation controls a dedicated team of software designers focused on solving an isolated and singular organizational problem. Guided by the principles of interconnection, opportunism, and domestication, we define responsive design as the kind of design approach that enables corporate participants to create and maintain productive design practices in response to the complex and dynamic landscapes of activities that are the foundation of corporate-communal engagements. We conclude with a discussion of the theoretical and practical implications of this new form of corporate software design.

Keywords: responsive design; open source software; design theory; corporations; open source communities; engaged scholarship; field study; thematic analysis

History: Natalia Levina, Senior Editor; Carsten Osterlund, Associate Editor. This paper was received on February 18, 2014, and was with the authors 14 months for 5 revisions. Published online in Articles in Advance November 23, 2016.

## Introduction

Corporations increasingly engage with open source communities to design software. Consequently, as open source communities represent real options for corporate participants in software design, new organizational forms are created (Ågerfalk and Fitzgerald 2008, Feller et al. 2008, Brooks 2010). On one hand, open source communities facilitate an exchange of existing knowledge, practice, and technology among constituents that benefits all (Kelty 2008). On the other hand, they afford a co-creation of new directions for knowledge and technology that benefits a select few (Hrebiniak and Joyce 1985, Kogut and Metiu 2001). Whatever the form, open source communities have become part of the creative revolution of how corporations operate (Kelly 2013).

At the core of this revolution are new opportunities for knowledge sharing and material exchange in the design of software artifacts: Hewlett-Packard engages with open source communities in the design of print drivers, Citrix in the design of hypervisors, and NYSE Technologies in the design of messaging middleware. In each case, corporate engagement centers on innovation, knowledge, methods, and technologies intended to strengthen the corporation’s design practices. As these engagements mature, it is important for researchers and practitioners to continue to advance our understanding of their associated theoretical and managerial complexities (Lee and Cole 2003; Fitzgerald 2006; Feller et al. 2007, 2008; Wen et al. 2010; Fitzgerald et al. 2011; Crowston et al. 2012). Accordingly, we draw from literature on open source community engagement (Dahlander and Magnusson 2008, Mehra et al. 2011) and design theory (Walls et al. 1992, Buchanan 1995, Gregor and Jones 2007) to present a three-year interpretive field study guided by the following research question: How is design enacted through corporate engagement with open source communities?

Corporate engagement with open source communities provides a context for investigation of design as constituted at the technology-enabled boundary of corporate choice and community influence (Lee 2007, Feller et al. 2008, Brooks 2010, Fitzgerald et al. 2011, Crowston et al. 2012, Fjeldstad et al. 2012). Open source engagements are arrangements of people, organizations, and technology (Howison et al. 2012) in which design is practiced across a distributed and diverse landscape, destabilizing classic assumptions of organizational work and artifact development (Walls et al. 1992, Hevner et al. 2004, Kellogg et al. 2006, Brooks 2010). To theorize these arrangements, we consider design as composed of: (1) theories to describe processes and (2) requirements to represent goals (Walls et al. 1992). Similar elements have been advanced in the design of emergent knowledge systems (Markus et al. 2002), in the positioning of design science research (Hevner et al. 2004), in the anatomy of design theory (Gregor and Jones 2007), and in the articulation of design science methods (Peffers et al. 2007–2008). As these elements have proven fundamental in theorizing design, we build from them to expand our knowledge of what design can be (Weick 1989, Buchanan 1995).

Our focus is neither directly on an open source community artifact (i.e., Linux kernel), nor on specific development methodologies in open source communities. Instead, we advance theory that emphasizes the “critical interactive nature of organizationenvironment relationships” in design (Hrebiniak and Joyce 1985, p. 336). Given the particular context of corporate engagement with open source communities, we explore design as responsive to complex and dynamic landscapes of activities that involve a diverse suite of member relationships, ideologies, and influences as the foundation for corporate-communal engagements (Horgen et al. 1999, Page 2009, Daniel et al. 2012, Tanriverdi et al. 2012).

## Theoretical Background

Open source communities are collections of varied members, including individuals, members of corporations, foundations, and universities organized around goals of consensus, collective action, and value creation (Kelty 2008). Open source communities may be more or less accepting of new members, highly controlled, anarchy, and have variable rules of engagement. Whatever the structure, corporations engage with open source communities at increasing rates and under specific conditions to advance corporate design (Feller et al. 2007, West and Lakhani 2008, Wagstrom et al. 2010, von Krogh and Haefliger 2010, Fitzgerald et al. 2011). Although our knowledge about the practices in corporate-communal engagements is limited, new and valuable insights are now developing.

Prior research has explored corporate-communal markets of corporate engagement with open source communities (Goth 2005, Dahlander and Magnusson 2008, Stuermer et al. 2009). This research illustrated economic and business models that corporations engage in as open source companies (Hecker 1999, Dahlander and Magnusson 2005, Fitzgerald 2006, Dahlander and Magnusson 2008, Lerner and Schankerman 2010) and highlighted the complexities associated with corporate open source products such as Netscape and MySQL. These studies investigated corporate efforts to “commercialise FOSS as their main business model” (Dahlander and Magnusson 2008, p. 632) by leveraging corporate access to resources, alignment of corporate and communal strategies, and corporate assimilation of communal knowledge.

The investigation of corporate-communal markets accommodates how corporations purposefully engage with open source communities to advance proprietary and communal products through the pairing of corporate and community practices (von Hippel and von Krogh 2003, Ågerfalk and Fitzgerald 2008). Corporate engagement with open source communities thus requires sharing of practices in ways that outstrip otherwise isolated corporate design and development efforts (Fitzgerald 2006, Johnson 2006). This affords the opportunity to “appropriate returns” from communities, creating incentives “for firms to engage in innovative activity” beyond the borders of any single corporation (Dahlander 2007, p. 915).

Table 1 Corporate Engagement with Open Source Communities

<table><tr><td>Corporate engagement with open source communities</td><td>Key elements</td><td>Representative corporate-communal papers</td></tr><tr><td rowspan="3">Corporate-communal markets. Corporate engagement with open source communities is evident across economic and business markets that include the advancement of open source and proprietary products.</td><td>Economic models</td><td>Stuermer et al. (2009)</td></tr><tr><td>Business models</td><td>Dahlander and Magnusson (2008)</td></tr><tr><td>Leverage</td><td></td></tr><tr><td rowspan="3">Interdependent ideologies. Corporations coordinate internal innovation activities with external innovation streams of open source communities, aligning the ideologies between the two in the advancement of shared resources.</td><td>Contribution</td><td>Feller et al. (2008)</td></tr><tr><td>Differentiation</td><td>Gurbani et al. (2010)</td></tr><tr><td>Corporate strategies</td><td></td></tr><tr><td rowspan="3">Distributed relationships. Corporate engagement with open source communities is built on social and material rules within an open source community, determining how participants manage the distribution of shared resources.</td><td>Licensing</td><td></td></tr><tr><td>Compliance</td><td>Stewart et al. (2006)</td></tr><tr><td>Intellectual property</td><td>West and Gallagher (2006)</td></tr></table>

Prior research has also shown that engagement can be a balance of interdependent ideologies of an organization with those of a community (Dedrick and West 2007, von Krogh and Haefliger 2010). Such balancing requires the accommodation and management of diverse ideologies (Stewart and Gosain 2006, Elliott and Scacchi 2008, Page 2009, Brooks 2010, Coleman 2012), as corporate members maintain the necessary rights and obligations inherent in the relationships to access and transfer strategic resources (Fitzgerald et al. 2011, Spaeth et al. 2010).

Corporate-communal engagements reveal complementary benefits, including gains in knowledge, learning, reputation, and the diffusion of innovations (Chesbrough 2006, Feller et al. 2008, Stuermer et al. 2009). To realize these gains, corporations engage with open source communities to appropriate communal artifacts for corporate profit (West and Gallagher 2006) and to advance corporate strategy through open source community contributions (Dahlander and Wallin 2006). In these relationships, interdependent ideologies between corporations and communities must remain commensurate to realize the advantages of such engagements (Gurbani et al. 2010).

Finally, prior research revealed corporate engagements with open source communities to include distributed relationships of known open source participants and structures (Stewart et al. 2006, Kelty 2008). Open source is distributed in the use of objects, forms of interpretation, and the actions of participants. However, there must be reasons for open source engagement to become ordinary practice in corporations. Any relationship, whether working with competitors on open source technologies, adhering to open compliance standards or modifying communal governance, must make sense in relation to existing corporate practices (Hovorka et al. 2015).

As such, relationships are social and material propositions in an atmosphere of rival organizations and communal standards, where a community may provide a platform of exchange between long-running, competitive corporate members (West and Gallagher 2006, Mehra et al. 2011). Engagement with open source communities has morphed beyond a powerful, yet increasingly challenged notion of individual volunteers sharing code in a public expression of freedom (Coleman 2012). Engagements now include the distributed relationships of corporate and communal members all protecting intellectual property, vetting licenses, and reviewing corporate compliance efforts as aligned with commercial strategies, development actions, and product design activities (Kelty 2013). Table 1 summarizes this prior literature.

To advance new knowledge about corporate-communal engagements and to focus on the core practices that drive these engagements, we rely on design theory. This theoretical anchoring provides a perspective that accommodates ongoing mediation between people, technology, norms, and practices evident in corporate engagement with open source communities (Howison et al. 2012). As such, it allows us to evidence how engagement is not solely determined by functional aspects of technology, but also by people (Crowston et al. 2012), offering knowledge of design as more than a localized development and evaluation of artifacts (Germonprez et al. 2011).

## Theoretical Development

We theorize design as “created through the activities of invention and planning” (Buchanan 1995, p. 24) when corporate and communal activities shape each other through firm choices and communal influences (Tanriverdi et al. 2012). We focus on the practices evident in corporate engagement with open source communities (von Krogh and Haefliger 2010), identify theoretical principles that represent a theory of responsive design as a significant contribution to the design theory tradition (Walls et al. 1992, Buchanan 1995, Hevner et al. 2004, Gregor and Jones 2007), and identify central aspects of design that articulate the “class of goals to which [design] theory applies” (Walls et al. $1 9 9 2 , { \mathsf { p . 4 3 } } )$

Our approach is indicative of design theorizing that reconsiders design in distributed technology creation (Sein et al. 2011), design utility affecting environmental sustainability (Melville 2010), and behavioral characteristics of design including cognition, emotion, and sociology (Dimoka et al. 2011). These approaches reason that design “continuously mediate[s] between human activity and informational, social, and physical environments” (Germonprez et al. 2011, p. 668). By investigating design as an ongoing activity, corporate engagement with open source communities provides a setting for the ongoing, mediated practices that are communicated, negotiated, and represented throughout diverse environments (Page 2009, Sein et al. 2011).

Design is a set of practices to solve problems, but it is beyond the control of any individual, community or corporation (Hackman 1986, Crowston et al. 2004, Brooks 2010), and it can be influenced in diverse landscapes among a collection of distributed and interconnected members (Buchanan 1995, Kellogg et al. 2006, Page 2009). In advancing design theory, we consider technology as an important, but not the only, consideration in design (Ciborra 2002). Instead, technology is the realization of cooperative and competitive processes that govern the requirements and ongoing practice of design (Walls et al. 1992, Borgmann 1995). “Those who study design often confuse the quality of existing products with the problems of designing new products. From this perspective, design history, theory, and criticism should balance any discussion of products with discussion of the particular conception of design that stands behind the product in its historical context” (Buchanan 1995, pp. 26–27).

Consequently, design involves complex configurations of people, contexts, and technologies (Ciborra 2002, Markus et al. 2002). Design can support the inductive development of theory that explains how arrangements of artifacts, corporate members, and open source communities may produce particular design practices with appropriate and useful outcomes for those involved. To provide the depth (Buchanan 1995) that extends design theory beyond the localized development and evaluation of artifacts (Walls et al. 1992, Hevner et al. 2004), we reveal design in the context of corporate-communal markets, interdependent ideologies, and distributed relationships. Corporate design can be a cause and a consequence of communal effect (Hrebiniak and Joyce 1985), providing a perspective of how design continually responds to environmental influences (Fjeldstad et al. 2012) through organizational choices understood against environmental determinism (Hrebiniak and Joyce 1985, Daniel et al. 2011). We contend that corporate design is responsive to, not determined by, open source community influence. Yet, corporate design is not perfectly synced to communal influence; strict alignment may result in structural inertia that inhibits a corporation’s ability to respond to external changes (Hannan and Freeman 1984). Instead, corporations create relative design adjustments to adapt to communal constraints, respond to the interdependence of participants, and accommodate precise corporate intention (Hrebiniak and Joyce 1985, Page 2009). Corporations engaging with open source communities may find that such adjustments constrain certain activities and allow flexibility in others (Crowston et al. 2012, Fjeldstad et al. 2012). This can result in design to reduce vulnerabilities in corporatecommunal engagements, guide communities for reasons of corporate interest or differentiate from a community in the creation of specialized products.

Design is “a series of processes among people and the systems they inhabit as they experience the world mediated by the system” (Germonprez et al. 2011, p. 679). We advance this position by asserting that design is not the exclusive domain of corporations that leverage an unaware community to extract artifacts (Stol et al. 2011), nor is it the exclusive domain of corporations that use a community to maintain formerly proprietary software (Dahlander and Magnusson 2008). Design can be a response to functional and behavioral choices associated with corporate design activities. Responsive design does not unfold as corporations engage with and disengage from an open source community. Instead, responsive design unfolds as corporate participants respond to market decisions, interdependent ideologies, and distributed relationships among open source community members in ongoing practices of software development (Figure 1).

In such flows of responsive design, corporations continuously establish and maintain relationships with community members that stem from the social and material rules inherent in the open source community. Like birds responding to the environmental conditions of weather, water, food, and predators during migrations, the relationship between corporate design and communal effect accommodates “an inherent uncertainty between design and its realization in practice, since practice is not the result of design but rather a response to it” (Wenger 1999, p. 233). Hence, with corporate-communal engagement as our context, we develop responsive design as evolving beyond the early, often artifact-centric framings of design theory (Walls et al. 1992, Markus et al. 2002, Hevner et al. 2004, Gregor and Jones 2007). Specifically, we consider principles that highlight the balance between corporate and community interests, disintermediating and decentralizing responsive design as the practices understood at the intersection of corporate and community engagement (King 2011).

Figure 1 (Color online) Responsive Design as Corporate Participants Engage with Open Source Communities  
![](/api/attachments/8ZYX277A/fulltext/images/96f821a03ba7a5be7e965fd49522caf5d881bca9bca1a9f5f2d2eea6317d3cd6.jpg)

## Methodology

In this study, we applied the three methodological domains of engaged scholarship (Van de Ven 2007), field study research (Klein and Meyers 1999), and thematic analysis (Boyatzis 1998). This pluralist approach provided context for our research, framed the setting in which we present our findings, and enabled refined analyses and strong theoretical representation of design in our engagement with corporations and open source communities (Weick 1989). Figure 2 provides an overview of the methodological framework applied in the research.

Engaged Scholarship. To allow for empirically driven, inductive development, our research was based on engagement with corporations with significant involvement in open source communities. Van de Ven defines engaged scholarship as “a participative form of research for obtaining the different perspectives of key stakeholders in studying complex problems” (2007, p. 9). To bridge the gap between the different forms of knowledge characteristic of practice and academia, engaged scholarship relies on an interactional view in which professional and research practices contribute to mutual growth (Mathiassen and Nielsen 2008).

To establish our engaged scholarship, we used preliminary interviews, meetings, and observations to ground the research program and to sensitize the research team to corporate-communal engagements. We established a strong connection with practice that provided an opportunity to embed practical concepts from corporate and community members (Davison and Martinsons 2002). We interviewed participants on broad issues of corporate engagement with open source communities to develop appropriate interview and focus group procedures. Members of three corporations and two research team members (one academic and one practitioner) were involved in the development of the initial procedures, iterating over six months. The iteration involved weekly meetings between the two research team members, as well as ad hoc meetings with the corporations to make the procedures as well as the delivery of questions meaningful for research and practice. Engaged scholarship continued beyond preliminary groundwork to include engagement during our intensive, threeyear field study, which involved six research team members, three graduate students, and three undergraduate students in interviews, focus groups, sitevisits, practitioner presentations, and direct community engagement.

Field Study Research. We used field study research as a methodological framework in which we conducted our engaged, qualitative study (Klein and Meyers 1999, Chiasson et al. 2009). Field research enabled our dual goal of developing applied knowledge towards practical problems that were of value to the participants with whom we were working and developing theoretical knowledge of value to a research community involved in design theorizing and open source research (Mathiassen et al. 2012).

We identified participants through personal and professional networks, Linux Foundation membership, practitioner conference participation, and open source community engagement. We exchanged preliminary emails with corporations, requesting interviews with members who could discuss participation with open source communities, corporate design in support of participation, and learning components that could prove useful for students and new community members involved in open source activities. We also informed corporate members that, through their participation, there was an opportunity to attend a National Science Foundation (NSF)-funded practitioner-academic workshop during which findings of the study would be presented and future lines of inquiry would be shared among participants.

Figure 2 (Color online) Methodological Framework Applied  
![](/api/attachments/8ZYX277A/fulltext/images/a7b54078c8d3c2597177977de46694ae74842404b5a33e0376a3432e736e3fd4.jpg)

We used interviews as the primary data source in our field study. Each interview lasted approximately one hour. We conducted over 80 interviews with developers, managers, and executives involved with open source community engagement. The interviewees represent 40 different organizations, primarily rooted in the technology industry. The interviews were conducted by one or more members of the research team and the majority were audio recorded and transcribed.<sup>1</sup> Most interviews were conducted by phone with a limited set accomplished face-to-face and via email. Interviews followed a semi-structured interview guide that afforded the opportunity for interviewees to delve deeper into relevant topics.

In addition to the interviews, we conducted three focus groups with two participating organizations. Both were Fortune 1000 organizations in 2016 with dedicated open source program offices. The focus groups were conducted on-site; involved 6, 8, and 15 participants, and lasted between 3 and 7 hours. The focus groups were organized around a slide deck based on the semi-structured interview questions and provided a way for the research team to gain new insights and form new directions that emerge from larger, focus group conversations. We also performed six site visits, three of which were associated with the focus groups. The site visits included informal conversations, presentations, and site tours. Site visit data was recorded through diary entries from two members of the research team, with the visits generally aimed at validating our communicative capabilities and forging stronger relationships with research participants.

Furthermore, research team members attended 11 practitioner-based Linux open source community conferences. The conferences included the Linux Collaboration Summit, an invitation-only conference aimed at articulating emerging directions related to Linux.<sup>2</sup> This conference was attended by members of the research team from 2011 to 2016. In 2013, 2014, and 2016, the research team was invited to present applied findings about open source license tool development at the Linux Collaboration Summit. The second conference was LinuxCon North America 2012, 2013, and 2015,<sup>3</sup> with the research team participating on an industry panel on practices to improve open source community participation.<sup>4</sup> The third conference was the Linux Foundation Open Compliance Summit in 2013,<sup>5</sup> where the research team was again invited to present results of open source development projects. The fourth conference was LinuxCon Europe 2015,<sup>6</sup> where the research team discussed open source development projects with community members.

In addition to the interviews, focus groups, site visits, and conference transcripts, research members worked with open source communities directly through open source working group meetings in person and online. Our research project hosts, develops, and contributes to numerous open source projects principally focused on open source licensing and compliance management. Additional project data included recorded field notes, researcher meetings, organizational documentation, and developed materials.<sup>7</sup> The data generated from the interviews, focus groups, site visits, and conference involvement included over 100 hours of audio recordings and 800 pages of transcripts and notes. Table 2 shows the organizations with whom we engaged. Not all organizations are listed owing to requests for confidentiality.

Table 2 Representative Organizations

<table><tr><td></td><td colspan="3">Representative organizations</td></tr><tr><td>Antelink</td><td>Black Duck</td><td>Canonical</td><td>Citrix</td></tr><tr><td>ConAgra</td><td>Cray</td><td>CSR Technology Group</td><td>Google</td></tr><tr><td>Hewlett-Packard</td><td>IBM</td><td>Intel</td><td>Linaro</td></tr><tr><td>The Linux Foundation</td><td>Meyer Sound</td><td>Microsoft</td><td>Motorola</td></tr><tr><td>NexB</td><td>NVIDIA</td><td>NYSE Technologies</td><td>OpenLogic</td></tr><tr><td>Outercurve Foundation</td><td>OW2 Consortium</td><td>Parallels</td><td>RedHat</td></tr><tr><td>Rex Systems</td><td>Samsung</td><td>Servint</td><td>SGI</td></tr><tr><td>Software Freedom Conservancy</td><td>SourceAuditor</td><td>Sun Microsystems</td><td>Talend</td></tr><tr><td>Telco Planning</td><td>Texas Instruments</td><td>Twitter</td><td>Two-Stones</td></tr><tr><td>Union Pacific</td><td>VPEP Technology</td><td>Wind River</td><td></td></tr></table>

Thematic Analysis. Based on the field study data, we performed thematic analysis to understand responsive design in the context of corporate engagement with open source communities (Boyatzis 1998, Kendall et al. 2006). Our goal was not to identify terms evident in corporate engagement with open source communities, but to apply relevant terms as a lens for revealing principles of responsive design. As the project began, we identified terms in the existing literature that sensitized us to the foundational practices of corporate engagement with open source communities. This built the necessary language to relate our findings to extant literature on corporate engagement with open source communities. We also connected with corporations to sensitize project team members to open source in practice and to elicit contemporary issues associated with corporate-communal engagements.

This grounding in literature and practice helped us identify appropriate terms for discussing corporate engagement with open source communities and for successfully engaging interviewees, interpreting focus group comments, gaining the most from site visits, and effectively participating with open source communities. We realized that identifying terms as sensitizing concepts and not as prescriptive toolkits (Horton et al. 2005) was essential to increasing our communicative capacity with practice and academe, although this alone did not fully determine our understanding of responsive design. The sensitizing terms provided an interpretive compass that helped us systematically navigate the landscape to reveal the richness of our data set (Boyatzis 1998).

We applied key elements from Table 1 to discover and describe theoretical principles from the empirical material. We used thematic analysis to continuously review the field study data and to discover relevant explanations (Boyatzis 1998). Each transcript was imported in Atlas.ti,<sup>8</sup> using 10 terms: leverage<sup>∗</sup>, econ<sup>∗</sup>, flex<sup>∗</sup>, contrib<sup>∗</sup>, differ<sup>∗</sup>, compli<sup>∗</sup>, licens<sup>∗</sup>, process<sup>∗</sup>, propert<sup>∗</sup>, and design<sup>∗</sup>. These terms helped us focus on key parts of the interview and focus group transcripts, revealing over 1,500 coded statements. Using Atlas.ti, we manually applied terms based on our knowledge of literature and practice to identify quotations relevant to those terms. These quotations were then analyzed. This step provided detailed insight into each of the key elements from Table 1, and helped identify our empirically grounded theoretical principles of responsive design. The quotations clustered into three groups and provided support for the principles of responsive design.

## Principles of Responsive Design

We focus on articulating principles evident in responsive design and not necessarily the complexity of their internal or external relationships (Klein and Meyers 1999). In this way, we do not over-specify relationships that are unique to any one engagement. Instead, we provide proximate associations in and between the principles that can be altered and made actionable for future investigation and validation in specific engagements (Romme 2003, Boyatzis 1998, Doty and Glick 1994). We did not find evidence of all aspects of all principles across all corporate participants, nor did we expect to. Corporate participants are autonomous agents who provide constructive and unique insights through their engagement with open source communities. As such, we present the principles of responsive design as confirming evidence from prior, published research in the context of corporate engagement with open source communities, while also developing new insights based on the extensive evidence from this study. Collectively, the confirmatory and developmental findings define the principles of our primary research objective to advance our understanding of how design is enacted through corporate engagement with open source communities.

Table 3 Forms of Corporate Interconnection When Engaging with Open Source Communities

<table><tr><td></td><td>Low differentiation</td><td>High differentiation</td></tr><tr><td>High contribution</td><td>Participants supply contributions that are compliant with a community and can help define and maintain strategic directions for that community.</td><td>Participants differentiate internal design from a community. Communal systems are used in system-specific ways as knowledge is applied strategically inside of a corporation.</td></tr><tr><td>Low contribution</td><td>Participants have a heavy reliance on communal standards and corporate product innovation is driven from elsewhere within an organization.</td><td>Participants may differentiate a communal system, creating a black box around a private system.</td></tr></table>

Source. Adapted from Germonprez and Warner (2013, pp. 46–48).

## The Principle of Interconnection in

## Corporate-Communal Engagements

Responsive design supports the interconnection of corporations with open source communities through managed engagement at the boundary between the two (Levina and Vaast 2005, 2006). Interconnection is, in part, a reflection of corporate roles in balancing contribution and differentiation at the interface of corporate and communal efforts:

“[We try] to get people to think through ‘is this really differentiating? Are we protecting something highly proprietary here?’ We have the same conversation with teams that will go off and develop a proprietary kernel module for whatever reason, and they sort of go into that thinking ‘We’ve got to keep this proprietary.’ But, as you start talking through, ‘Well why do you think that? or What are you really trying to protect?’ ” [22:22].<sup>9</sup>

Confirming prior research, interconnections can be understood as high and low contributions to a community, representing degrees to which corporations respond to communities (Lakhani and Wolf 2005, Gambardella and Hall 2006). Likewise, interconnections can be understood as high and low differentiation representing the degree to which participants modify stable, open source artifacts to meet specific organizational requirements (Neus and Scherf 2005, Henkel 2006). Table 3 illustrates how corporations can enact responses to open source communities.

As examples of contributions and differentiation, corporations may respond to engagement with open source communities with no differentiation in products and no contributions back to a community:

“We use 0 0 0 the SUSE version of Linux, and we actually purchase it. 0 0 0 But there’s been some confusion [that] we’ve been making modifications to it. We don’t have software engineers per se; we have very good OS level administrators. I would say [our contribution] is pretty low because we purchase our support through a supplier” [3:1, 8].

Additionally, corporations may respond as high contributors and low differentiators, intending to strategically maintain alignment with a community while still designing localized services:

“The only differentiation that we do is when it’s absolutely necessary to create a functional platform. Our goal is to have all the changes that we need for our platforms in the upstream kernel so that we can ask partners to pull those into their distribution” [15:4].

These responses reflect how a corporation connects to a community and how a community accepts new members to improve the alignment of a corporation with an open source community, thus increasing the likelihood of corporate engagement success:<sup>10</sup>

“Our customers want [community engagement], it saves us a large amount of development cost. If we were to get on the bad side of the community and they were to take steps to make it harder for us to use Linux, we would be in a very unfortunate position” [4:49].

In this regard, software licensing was confirmed to be a primary connection concern as corporations respond to communal norms (Lee and Cole 2003, Stewart et al. 2006). A senior open source engineer and Linux community pioneer states:

“If you use Linux, then you abide by the terms of the [General Public License (GPL)]. So if you make derivative works, you’ve got to make the code available. Nobody’s forcing you to use the GPL. But if you use it, you have to meet your obligations under the terms and conditions. 0 0 0 If we want our code to be accepted, [we have] to write the code in the license the community uses whether it’s GPL, Mozilla, or Apache. The key notion is that you have to use the license that the community uses and that’s part of adapting to the community” [9:37, 53].

These findings reflect the importance of conceptually simple, yet practically complex software licenses that define interconnections with communities. Software licenses codify and express the rights and obligations associated with the design of specific pieces of software. Simply, licenses determine the freeness of open source software. However, a deeper examination of software licenses represents more than just the to-do list. Software licenses represent a source of normative, risk-related behavior from which stability can be advanced by open source communities (Stewart et al. 2006, Germonprez et al. 2012).

Whatever the mix of corporate approaches and communal norms, interconnections are not a one-sizefits-all approach, but an alignment of corporate strategy, resources, and community responsibilities. There is no singular best practice for corporate interconnection with open source communities, depending on how industrial cultures, corporate requirements, employee abilities or communal obligations vary. As our developmental findings show, corporate practices have emerged in instances to formalize interconnections at points where open source enters and exits a corporation:

“We have guidelines that our legal team has worked with several [internal] engineering groups to come up with and say, ‘If you’re interested in open source, here are the sorts of things you need to do and think about.’0 0 0 We allow all the different teams and divisions and groupings [internally] to have the ability to work within those guidelines that we’ve established over the last five years to make those kinds of decisions themselves. So it’s not complete laissez faire” [25:83].

At these entry and exit points, corporations respond to communities via design cycles, regulating contributions to as well as differentiation from communal activity. First is a cycle of not contributing corporate design back to an open source community. In this cycle, corporately designed artifacts are maintained, adapted, and integrated exclusively into an internal, corporately maintained code stream:

“[Some] end-users like us because we provided highquality drivers for our products for Linux forever. But some hardcore religious Linux types hate us, because those drivers have been closed source in certain areas. So we struggle with this in both directions. We’ve been trying to be 0 0 0 more active lately in the upstreaming and other things, because that is a purely open sourced world, and it’s needed. But also, we think it would be beneficial to us to have more ownership, have more control, and more influence [over the product]” [26:750].

In this noncontributory model, corporations respond to communal activity by maintaining internal design in parallel with open source community activity and manage the timing of release cycles internally with release cycles of a community (Figure 3).

Figure 3 (Color online) Noncontributory Design Cycles  
![](/api/attachments/8ZYX277A/fulltext/images/7210efa9d2072bad05ddfc66a29c004161206735d6c53a4c631560e2ef70f177.jpg)

Figure 4 (Color online) Contributory Design Cycles  
![](/api/attachments/8ZYX277A/fulltext/images/be1ee70efe2bdb92c613682d4bf1f24f1d98263c0b1ae60a496b75b090f8c172.jpg)

A second design cycle is a contributory model and involves contributing corporate design back to an open source community to reduce corporate design efforts. As described by a manager at a computer industry organization attempting to push design back to a community:

“A few years ago 0 0 0 we had one of our proprietary CPU’s that we built and modified the Linux kernel for. We tried to submit those mods back to the community so that we didn’t have to keep maintaining [it]. They said we don’t want it because, other than my organization internally and my organization’s customers, nobody else can run it. They can’t test it, and it becomes a burden to the community” [5:10].

In a contributory model, design practices (i.e., adaptation and integration) become the responsibility of an open source community as part of an overall open source community artifact; the corporation is only responsible for the design practices of verification and testing (Figure 4).

However, design cycles alone are not sufficient to fully manage these interconnections. Corporate practices are also constituted at the corporate-communal boundary attending to the rights and obligations expressed in such engagements. Codified managerial reviews occur to comply with communal requirements as well as protect against infringement on corporate or customer intellectual property (Figure 5).

Within this management review, license compliance and intellectual property administration was evidenced, managing the risk of unwanted, but licensemandated release of intellectual property to an open source community:

“I think it’s been a challenge in terms of ensuring that we try and maintain a very clean run approach to our codebase so that we’re ensuring that we’re not unintentionally putting our intellectual property into whatever source code we would be required to share” [11:13].

Corporations may further respond to corporatecommunal engagement by extending the review process deeper into the organization, standardizing internal open source training programs for software engineers, and aiding the overall management review process by educating corporate open source participants:

Figure 5 (Color online) Codified Management Review  
![](/api/attachments/8ZYX277A/fulltext/images/3da1680d7c95554c991b8a084ecd26f19bfb103c03e8ad44f911358e4bb3d497.jpg)

“The big concern is projects that we do on our own because that requires a legal review. We give the legal team about five days to give an answer [to] make sure how does this relate to our brand? Are we violating any trademarks with the name of this project to typical stuff you’d see? And we’ve actually kind of implemented 0 0 0 a training program within the walls of [the company] to teach people about copyright, trademark law, and stuff like that and get engineers to choose intelligent names that don’t give our lawyers a headache” [31:59].

The principle of interconnection supports the corporate responses to communal activities, affording processes by which corporations consider their own forms of participation, evident communal practices, and the mutual dependencies between members evident in corporate-communal engagements (Table 4).

The Principle of Opportunism in Corporate-Communal Engagements. Resources are collectively negotiated and openly available in responsive design. They entail a bidirectional contribution to and differentiation from open source communities, accommodating an equitable system of assets distributed among participants (Jullien and Zimmermann 2009, Schaarschmidt et al. 2015). Corporations respond to the opportunities afforded through communal resources as they engage with communities to leverage human resources in the form of expanded designer bases. Before engagement with open source communities, a firm in the computer graphics industry solely bore the costs for all its software developers:

“I think, at our peak, we had hundreds of people in software development. Right now I have 13 developers on my team. You wouldn’t believe everything that we cover with 13 people, because we leverage the opensource community” [16:1].

A manager at a consumer electronics firm expressed how responding to communal resources, as expanded designer bases, allowed corporate time, otherwise allocated to internal design, to be allocated to other client- and corporate-focused activities:

“We’re paying a team of 8 to 10 engineers good money to do work that’s respectfully already being done by a whole bunch of other people, and that doesn’t make a lot of sense. You could get these very talented engineers doing something else 0 0 0 But, why would you consider getting into open source? The question you want to ask is, number one, ‘Why [would] you want to reinvent this particular wheel? Do you actually have something to add here? Are you going to make a better kernel? And, how are you going to do that?’ So, that percolates through all kinds of components. Nobody writes a Bluetooth stack because there’s a perfectly good open source one out there” [32:100].

In a similar vein, available communal resources provide an opportunity to hire designers (Ågerfalk and Fitzgerald 2008), becoming a talent pool from which corporations can observe and recruit individuals:

“We’ve gone to the 0 0 0 community and hired maintainers 0 0 0 because we’re getting people we know who are good and are reporting people who contribute.0 0 0 It’s not every developer we hire in that way, but all the team leads and the people who work on open source are all from the community” [17:27, 28].

Corporations also respond to the opportunities afforded by communities by leveraging artifacts and maintenance of those artifacts in the advancement of corporate innovation streams (West and Gallagher 2006). Communal resources provide a collection of shared artifacts that can be tailored to specific corporate needs and strategies. This could include the use of the Linux kernel in flat panel televisions (e.g., LG’s webOS) or the use of FreeBSD in hardware routers (e.g., Juniper Networks’ Junos), thus enabling design for specific, differentiated corporate needs:

“You’ve got to find a way to make money, and you’ve got to find a way to differentiate yourself 0 0 0 There are pieces of software that run in user space on top of the whole Linux ecosystem that we consider to be proprietary differentiators. There are a lot of companies that do this” [4:19].

Corporations may also respond to the opportunity to offload some responsibility for artifact maintenance to an open source community (Holmström and Fitzgerald 2006, Haefliger et al. 2008), effectively transferring design burden from a corporation to a community:

“The goal is 0 0 0 to get our ideas out there, so they could eventually be implemented [in the community]. And we could benefit from that because we have less maintenance on our end” [31:54].

Without this response, a corporation would repeatedly incur the cost of design not contributed to communal resources whenever there was a new version of a communal artifact:

“The reason you need to look at the long-term is that short-term cost of a port [internally maintained artifact not contributed to a community] is one that you’re going to be incurring over and over and over again. Whereas, if you take the long-term view and contribute the patch to the community, you do that once, and you’re done, in the best case” [4:37].

Thus far, responses to the opportunities afforded by corporate-communal engagements have been confirmatory of prior literature in the expression of corporate engagement with open source communities.

Table 4 Responsive Design Principle of Interconnection in Corporate-Communal Engagements

<table><tr><td>Theoretical principle</td><td>Findings</td><td>Observed forms</td><td>Summary of observed forms</td></tr><tr><td rowspan="4">Interconnection</td><td rowspan="2">Confirming prior corporate-communal open source software literature</td><td>Contribution and differentiation</td><td>Corporations consider the approaches employed when engaging an open source community as balancing between contributions to and differentiation from open source communities.</td></tr><tr><td>Communal norms</td><td>Corporations understand the norms inherent with open source communities including the standards of making contributions and obligations set forth in community licenses.</td></tr><tr><td rowspan="2">Developing new corporate-communal open source software insights</td><td>Design cycles</td><td>Design cycles are modified as corporations engage with open source communities in both contributory and non-contributory forms.</td></tr><tr><td>Management reviews</td><td>Corporations codify how they manage engagement with open source communities in the form of open source management reviews. These reviews are constituted through managerial evaluations, legal vetting, and developer training programs.</td></tr></table>

However, our field study revealed a deeper, developmental understanding of what opportunism entails.

Corporate response to open source communities may include the full divestiture of corporate design as an artifact retirement strategy. A corporation may contribute an entire product to an open source community to provide extended life to otherwise retired artifacts, thus creating design potential around the contribution:

“Some 0 0 0 external requests [came] from people who had been exposed to [our product] over the years and wanted certain functionality that was also available on Linux. So, in cases like that, it often did not make sense for us to want to be a gatekeeper. If we saw that there was 0 0 0 some value in us releasing a bit of code so that somebody else could take it and then run with it 0 0 0 we said, ’Yep. We’ll open-source it, we’ll stick an opensource license on it, and then just throw it over the wall, make it available,’ and [the community] would take it and run with it” [15:31].

Such contributions also reveal apparent philanthropic stances of participants responding to the community for altruistic reasons and the ethos of making the world a better place:

“The line is so fine between partnership and community that it’s almost hard to discern a series of loose partnerships from a community, except that a community has an element, I believe, an element of altruism— that we’re all moving in the same direction, and we’re helping each other do it. In the community, there has to be this engagement where everybody feels like they want to do something for the good of the whole. And that’s the only thing that differentiates a company participating with a community versus a company participating with a series of partners” [17:24].

Yet even the most altruistic stances often carry a tactical undercurrent, as corporations respond to select open source communities to preserve a community, thus helping to maintain corporately valuable communal resources. If a community ceases to function, so too may the communal resources, and a corporation must manage design resources internally or divest from the design engagement:

“So the headline part of it would be altruism 0 0 0 But it’s kind of a self-interested altruism because what it also shows, the things that we open source or the coding patterns that we put out into the world, is all kind of being done from the perspective of we truly do believe that we can organize and make the world better” [19:47].

In fact, some strategies are less subtle and more directed toward reaching and influencing communities, not just maintaining community products:

“[We] have no incentive to differentiate the product. There’s no reason for us to do a differentiation of the product coming out of the open community. But, in fact, our main goals are to actually guide that community and have an influence in it” [26:50].

Responding to impart philosophy to a community deliberately shapes a community and includes computer chip manufacturers aligning internal property with communal artifacts to reach the broadest market (e.g., Intel) or Linux kernel distributions (e.g., Red Hat) that aim to design and consult on the most common form of the artifact:

“Franchise and ownership: That’s [us]. By working upstream on [our product, we] get perceived as one of the go-to companies for [this] technology 0 0 0 If we’re one of the major contributors, the major franchises, we’re the major go-to person for that. In effect this becomes a marketing benefit” [14:7].

By franchising them, contributions help establish worldviews between corporate and communal activities, influencing an open source community in ways that have a clear benefit for the originating corporation:

“You do have the ability to influence where that project goes. This goes right back into community engagement. If you engage with those guys, if you know them, if you’re interacting, if you’re contributing, you’re going to have a lot more ability to influence the direction of that project than somebody who’s just sitting back and taking the code and being pretty quiet” [22:16].

Table 5 Responsive Design Principle of Opportunism in Corporate-Communal Engagements

<table><tr><td>Theoretical principle</td><td>Findings</td><td>Observed forms</td><td>Summary of observed forms</td></tr><tr><td rowspan="5">Opportunism</td><td rowspan="2">Confirming prior corporate-communal open source software literature</td><td>Leveraged human resources</td><td>Corporations engage with open source communities to expand the availability of designers and developers.</td></tr><tr><td>Leveraged artifacts and maintenance</td><td>Corporations leverage shared artifacts and services that are available throughout open source communities.</td></tr><tr><td rowspan="3">Developing new corporate-communal open source software insights</td><td>Artifact retirement</td><td>Corporations contribute to open source communities to extend the life of artifacts that are no longer maintained corporately.</td></tr><tr><td>Community preservation</td><td>Corporations contribute to open source communities so communities remain healthy, providing long-term value to corporate initiatives.</td></tr><tr><td>Franchising</td><td>Corporations instill worldviews into an open source community for reasons of corporate influence.</td></tr></table>

Corporate opportunism represents accepted engagement, whether leveraging communal resources for corporate innovation streams or franchising corporate philosophy for expanding consulting reach. In open source engagements, a common belief is that “a rising tide lifts all boats” and that it takes all kinds of participants to make a successful open source engagement. Without pursuing corporate worldviews, new design innovations may not become communal resources. Without leveraging communal artifacts, new markets may never open in a commercial space. Table 5 summarizes the theoretical principle of opportunism in responsive design.

## The Principle of Domestication in Corporate-Communal Engagements

Corporate engagement with open source communities is becoming domesticated, creating a managed and stabilized environment, and supporting structured practices in the design of corporate and communal artifacts (Kelty 2013). Issues of copyright, regulation, and politics have been brought forward as a “generation of [open source software] hackers become astute legal thinkers and producers” in corporate-communal engagements (Coleman 2012, p. 23). Corporate engagement with open source communities often requires managed and stable environments as participants may fail to meet expectations as open source maintainers, implementing critical features in ways that negatively impact open source release quality or timelines. Communities may fail to sustain a leveraged resource model, requiring abnormal stabilizing duties from participants. Corporations may accidentally or intentionally fail to comply with open source licenses as expressed by communities, resulting in external arbitration and possible litigation. Whatever the case, corporations cannot afford engagement if risks are unclear and design unpredictable.

Confirming prior literature, knowing that the engagement between corporations and communities is domesticated is important to knowing why such engagements exist at all. Such consideration is echoed throughout literature, as engagement is aimed at integrating research and development capacities of corporations and communities (Dahlander and Magnusson 2005, West and Gallagher 2006). Design practices are intended to strengthen and sustain the capabilities of corporations and communities:

“The chief reason for joining a community is to extend the reach of the project or to build the community. They have this dream that they just have to join and they can build a new team. The main reason would be project sustainability. The project beyond the project, the project beyond the team that runs, that develops it—so they want to find people out there—or to provide a life for the project beyond the life of the team” [28:76].

Engagement is the corporate alignment of design practices with business and legal activities that stem from community obligations, attending to the balance required between corporation and community environments (Lerner and Tirole 2002). As a manager at a large technology firm stated, lawyers are now part of domesticating open source engagements:

“We have now a smaller group 0 0 0 of legal experts who are involved in the review process. It’s real important to have your business attorney involved in reviewing the open source. Their role is to provide legal advice to the team to make sure that you comply with the terms of the license and you can see here the various attorneys that support the different business groups” [43:1].

Responses are not just the extraction of resources from a community to a corporation, but now often include the measured alignment of corporate legal activities with communal requirements to stabilize engagement. Knowing corporate engagement as a deliberate and structured arrangement, allows knowing participation as what one interviewee referred to as “professional open source.”

As a domesticated engagement, participation is often realized as a value proposition in an atmosphere of rival organizations where a community may have established, long-running, and competitive corporate involvement (West and Gallagher 2006). In some cases, a community of competitors is a natural occurrence, requiring efforts to maintain competitive advantages but still realizing improved economics through the maintenance and advancement of corporate and communal resources:

“One of the common arguments becomes, well if we put this out, we’re collaborating with our competitors. It’s a very hard thing for people to understand that everything right now these days is time-to-market basis. You might be making it easier for your competitors to do this, but they’re months behind you because it’s going to take them a while to leverage this in. So you’re going to have at least a certain amount of advantage. Then, quite frankly, you’ve got lower costs long term because you don’t have to keep maintaining an alternate set of patches” [1:4].

In other cases, engagement between competing corporations may be deliberate, negotiated prior to any communal formation. As an example, the Open-MAMA<sup>11</sup> project is focused on the design of a “high performance middleware agnostic messaging interface.” In this project, an improved middleware provides value to all members in the management of large-scale data environments including NYSE Technologies, J.P. Morgan, Merrill Lynch, and Bank of America. The middleware itself is nondifferentiating (i.e., providing no competitive advantage for any one corporation), allowing competing corporations to contribute to its design while maintaining internal design activities to focus on leveraging the artifact in corporate-specific, value-added ways (Germonprez et al. 2013):

“If you look at the participants, we have customers on there, users, competitors, other vendors in the industry that were just interested for their own business models to get [involved] in OpenMAMA” [40:15].

From a developmental perspective, the domestication of corporate-communal engagement requires attention to organizing the value streams stemming from engagement, in essence, knowing how and when to explicate and manage the contributory and differentiated roles during participation:

“By getting a new system, one of the requirements was to make it flexible, so we could actually alter the workflow quickly 0 0 0 [Our corporate processes can be modified to] react to the speed of the community. [For example, the] Affero license will affect us because there’s a move towards cloud computing. 0 0 0 [We] needed to make it flexible to react when things change [23:332, 333].

Within such engagements, stabilizing structures have emerged to regulate particularly relevant practices. As an example, the Software Package Data Exchange (SPDX) standard began in 2010 as a Linux Foundation community project to articulate licensing norms as “a standard format for communicating the components, licenses, and copyrights associated with a software package. The SPDX standard helps facilitate compliance with free and open source software licenses by standardizing the way license information is shared across the software supply chain.”<sup>12</sup> SPDX is a bill of materials that represents the multitude of licenses embedded in open source software packages, providing a stabilized form for corporations to understand and distribute open source obligations:

“If you’re putting out a package and you can put it on an SPDX file, you have a pretty good chance of not having 20 people coming at you from different directions and asking for clarification. By generating the stuff out, it’s a forcing function to make sure that it’s clean. If someone’s going to take and bring it into a product, they have something to crosscheck and reference and understand the intent and then verify for themselves” [11:11].

In response to the domestication of corporate-communal engagements, third party support services have also emerged to define, support, and stabilize common activities. We know that nonprofit foundations house open source projects to help articulate governance, mitigation, and licensure for open source communities (West and O’Mahony 2008). Foundations provide brokerage services for participants so as to not represent any shared organization as too heavily influenced by any single participant:

Companies, open source projects, and individual developers can work with our Linux Foundation Collaborative Projects to make collaborative development the de facto way of solving the world’s hardest problems [Linux Foundation].

We additionally found that corporations exist to maintain and profit from the complexities associated with participation, further domesticating corporatecommunal design engagements. It is a challenge for corporations to manage internal code streams against communal obligations, and in response, organizations (e.g., Black Duck, Palamida, Protecode, OpenLogic, and Antelink) exist to provide services to assist with the navigation of this complex engagement:

“Our business model, our value proposition to a customer is around successful and safe adoption of open source. And in that concept or in that mission, if you will, we have a couple of key pieces to our value proposition. One is a provisioning side. We provision all the bids of the support side” [42:2].

Table 6 Responsive Design Principle of Domestication in Corporate-Communal Engagements

<table><tr><td>Theoretical principle</td><td>Findings</td><td>Observed forms</td><td>Summary of observed forms</td></tr><tr><td rowspan="4">Domestication</td><td rowspan="2">Confirming prior corporate-communal open source software literature</td><td>Integrating research and development capacities</td><td>Open source communities are a viable part of corporate innovation streams, providing an extension of corporate research and development capacities.</td></tr><tr><td>Community of competitors</td><td>Corporate-communal engagement entails a community of competitors who share in the design of non-differentiating artifacts to benefit all.</td></tr><tr><td rowspan="2">Developing new corporate-communal open source software insights</td><td>Stabilizing structures</td><td>Standards have also emerged to meet corporate practices of product development and licensure involving engagement with open source software.</td></tr><tr><td>Third party support services</td><td>A support industry has emerged to support license management and intellectual property protection but can include governance, marketing, and collaborative activities.</td></tr></table>

Service corporations do not often participate directly with open source communities in ways that have been presented in our research. Instead, service corporations consult on the identification, representation, and management processes associated with their customer’s engagement with open source communities:

“[Code] review is done by peers technically. The safety net which we’ve been discussing is a tool like Black Duck, which scans proprietary code for open source, and turning that upside down and using it with knowledge of our proprietary source to scan our open source to make sure that none of those constructs show up. It’s one of the key aspects we would like to provide, because it could be instantaneous feedback for a developer, or a very low friction as to whether they have inadvertently polluted the open source community with proprietary software” [26:102].

In the domestication of design engagements, new structures are established to stabilize corporatecommunal engagements beyond a simple extraction of resources in the advancement of proprietary innovation streams. Domestication represents the professional engagement that open source can be, entailing activities that are familiar to participants, recognizable to lawyers, and in line with software supply chains. Table 6 represents domestication in responsive design.

## Discussion and Conclusion

Historically, open source is rooted in an egalitarian engagement of volunteers to advance philosophical principles of free software (Coleman 2012). While these ideals are very much alive across thousands of open source communities, the past 15 years have seen a remarkable rise in for-profit corporations joining open source communities as participants in and carriers of the multiple interwoven, overlapping, conflicting, and divergent practices that enable and constrain open source engagements. Corporate engagement has altered the landscape of open source, and in doing so, has provided a window into new and evolving design environments within distributed engagements (Kelty 2013).

We observed how design extends beyond the boundaries of one organization solving one problem, opening new understandings of what design can be (Walls et al. 1992, Buchanan 1995). We revealed design as a complicated set of practices, consisting of interconnected elements including partnerships, standards, and technologies, all within the background of communal sense making, attitudinal states, practical know-how, and new methods of exchange. Exploring this emergent phenomenon through extant open source software and design theory literature, we came to understand design as a responsive activity grounded in the theoretical principles of interconnection, opportunism, and domestication.

From our research question of how design is enacted through corporate engagement with open source communities, we understand that design is not simply constituted as a problem-solution path to be recognized in the same way by all participants. Design includes the responses of participants in complex landscapes of member relationships, ideologies, and influences. As such, we moved beyond traditional ways of knowing design, exploring it in the context of corporate engagement with open source communities (Walls et al. 1992, Crowston et al. 2012) and advancing a view of design as divided, balanced, and regularized across diverse, dynamic, and evolving landscapes. Responsive design is a particular form of corporate software design that, beyond the inclusion of external participants, distinguishes itself from traditional monocentric design in which one corporation controls a dedicated team of software designers in solving an isolated and singular organizational problem.

In this context, design entails an interconnection of participants, creating new forms of labor and capacity. If design relies exclusively on notions of private property to solve a problem, the rights of that property are fully borne by a single person or corporation. However, design is manifest in environments of interconnected ideologies, market activities, and shared ideation, relying on the practices and resources emergent from and released throughout an interconnected community. Design permits participants to enact distributed forms of work when communally engaged, and accommodates application of localized practices in the management of such distribution throughout the diverse markets of members. As design is enacted across interconnected participants, it accounts for the networks of community intention and localized interpretation in an ongoing exchange of artifacts and as an inseparable part of people translating and expressing design in unique ways (Durkheim 1997). As such, design resides “somewhere between the extremes of one person doing everything” in private and “every smallest activity being done by a separate person” throughout a community (Becker 2008, pp. 9–10).

Furthermore, design includes a balance between value creation and value capture stemming from the opportunism of design participants. Participants strategically attend to design in various ways, delineating courses of action and shaping the rights and obligations of members as subject to and in control of the activities that guide engagement. Design accommodates and adopts the opportunities that contribute to and differentiate from shared artifact development, as the requirements and goals in the intentionality, ideology, and aesthetic rationales of the participants evolve. Hence, rationalizing design as a private, problem-solving experience is one of convenience (Buchanan 1995) and fails to recognize the value creation and value capture opportunities through such corporate- and communal-specific activities of artifact development, preservation, and retirement. In balancing value creation and value capture, participants make adjustments through engagement with communities that are often set against the design of specific artifacts and practices. Design is then evident across the opportunistic ways participants balance value creation and value capture, while still aiming to create consistency in socially constructed communities in ways that promote shared and localized goals.

Finally, design requires the stabilization of conventions and the establishment of domesticated design environments. Corporate-communal engagement demands that there is no singular imposition in a community and that engagement resides in the regularized actions of people and the systematic distribution of knowledge across diverse and evolving landscapes. Design entails a pressure for a shared understanding of consistency as a basis for collective action. Design accommodates the stabilization of conventions for engagement, providing a recognizable environment to house the work for which the community has interest and capacity. As such, design provides a rationale for diverse corporate engagement that affords broad sensemaking as people and organizations assign, interpret, and maintain a shared understanding of design activities and artifacts (Becker 2008). In our domesticated corporate-communal engagements, design was attended to through corporate reviews, communal structures, and a service industry that preserved common language, etiquette, and practice among community participants. Domestication allowed design to be distributed, shared, and understood by a broad range of participants contributing across diverse and distributed communal engagements. Guided by the principles of interconnection, opportunism, and domestication, responsive design enables corporate participants to create and maintain productive design practices in response to the complex and dynamic landscapes of activities that are the foundation of corporate-communal engagements (Figure 6).

As a consequence of deepening our understanding of design in the context of corporate-communal engagement, we saw that the landscape of open source engagement has changed, marginalizing the traditional free agent community member often reported in the literature (Coleman 2012). In investigating responsive design, we observed that community members are now simultaneously community and corporate members, shifting identities between the two, concurrently serving corporate and communal interests. We found few singular corporate members beside singular open source members to which engagement was exclusively corporate or communal. Instead, membership was a transitional position between corporate and communal interests, aligning corporate styles and strategies with communal obligations and resources. As such, corporate engagement with open source communities is a management of transitions, neither fully communal nor fully corporate (Kellogg et al. 2006), supporting structured practices in the design of corporate and communal artifacts (Kelty 2013). Members manage these transitional complexities with varied leaderships (Crowston et al. 2010), communication channels (Yamauchi et al. 2000), and developer skills (Fitzgerald 2006). Hence, we found that membership can be understood, not as a resource-gathering job of one person from a community to a corporation, but as “a realm of pure possibility [where] novel configurations of ideas and relations may arise” (Turner 1967, p. 97).

Our research explored the sophisticated relationships between corporations and communities by following a line of design theorizing that infers such engagements are more than corporations using open source resources for differentiated corporate gain. Strict dichotomies between corporations and communities have blurred, as corporations often comprise the majority of membership in open source communities (Corbet et al. 2012). Open source has

Figure 6 (Color online) Responsive Design as Enacted Through Corporate Engagement with Open Source Communities  
![](/api/attachments/8ZYX277A/fulltext/images/06d3a469a08a3727d2f4e52175fcdf727675aae157b9479f6b0149f6e0ac9208.jpg)

altered corporate design activities to include professional open source communities to foster and sustain innovation on select, non-differentiating projects (West and Gallagher 2006, Germonprez et al. 2013). Communities such as OpenDaylight,<sup>13</sup> include platinum (e.g., Cisco), gold (e.g., NEC), and silver (e.g., Fujitsu) board memberships requiring payment and engineering staff dedicated to the open source project. Open source has altered corporate design activities, accommodating corporate-to-corporate software supply chains, recognizing that open source software often originates from interconnected suppliers, not singular communities. Initiatives such as OpenChain<sup>14</sup> foster transparency between buyers and sellers in the exchange of open source software to manage risks associated with such exchanges. Whatever the construction, the relationship between open source and design is still evolving as free software as a social movement actively transforms into open source as a corporate design engagement (Stallman 1983, Kelty 2013).

## Limitations

There are several clear limitations to our research. The first is our selected context of the Linux open source ecosystem. Other large-scale open source ecosystems such as Apache or Eclipse undoubtedly carry unique ideals, participant types, and governance models. The Linux open source ecosystem represents a unique case for corporate-communal engagement given its extensive corporate involvement (Corbet et al. 2012), its impartiality to a broad array of corporate interests (Shah 2006), and its maturing governance models in brokered communities (Germonprez et al. 2014). To generalize between ecosystem contexts is a challenge; thus, any contributions to corporate engagement with open source communities must be considered in light of our chosen ecosystem context.

As a second limitation to our research, we did not confirm every principle in every corporation. Our field data represented how different corporations pursued various business needs and demands in designing their own software. While we believe we make relevant contributions to design theory from our field study, our approach to identifying theoretical principles raises the question of how information systems design accounts for the different needs of corporations across our chosen field study ecosystem.

Finally, our research did not explicitly reveal direct interactions of responsive design principles. Allusions and inferences are made throughout the interviews and results, but explicit examination into the direct interaction between the principles did not exist. In the future, it may be beneficial to focus on singular interactions between theoretical principles to reveal contradictory and complementary connections between principles in such design engagements.

## Future Research

In spite of these limitations, our study has revealed a deep well of untapped discoveries in corporate engagement with open source communities (Buchanan 1995, Crowston et al. 2012). We explored how corporations engage with open source communities to reveal responsive design and to identify and articulate theoretical principles represented through such engagements.

From a theoretical perspective, future research can identify how exploration and exploitation (Gupta et al. 2006) are constituted through responsive design. In doing so, research could draw on organizational learning (March 1991) to articulate specific corporatecommunal relationships. Such research could identify and understand the principles of learning engagements that afford appropriate balancing of exploration and exploitation in corporate engagement with open source communities. Additionally, future research can explore responsive design practices across foundations, corporations, and communities in the advancement of domesticated structures. The ongoing evolution of open source as a corporate endeavor requires continued attention to the ways that design practices are produced, distributed, and stabilized to federate innovation for all participants (Chesbrough 2006).

From a practice perspective, future research can foster direct engagements with open source community participants to advance new knowledge. Researchers can become contributing members in open source communities by fostering review and training activities. Such engagements could leverage management practice into relevant and actionable insights for open source community managers (Berente et al. 2012) to reduce the tensions in open source communities composed of competing corporations. As academic researchers, we are well positioned to bring unique resources to the advancement of corporate engagement with open source communities in the form of theoretical, empirical, and pedagogical insights.

Across theory and practice, corporate engagement with open source communities reveals that design is not borne solely from technology-based solutions, but also from the responses in which those emerge. Evaluation is not simply the utility, quality, and efficacy of an artifact but also the distribution and exchange of design among participants. By understanding corporate engagement with open source communities, design is revealed as responsive across distributed, communal, and technical spaces. As such, our theoretical contribution of responsive design resides at the confluence of people and technology, articulating the rules of engagement, the rationale of collective behaviors, and the development of communal artifacts intended to be inclusive of all concerns.

## Acknowledgments

This project has been funded through the National Science Foundation’s Division of Advanced Cyberinfrastructure and the Division of Social and Economic Sciences. Specifically, the project received funding through the Virtual Organizations as Sociotechnical Systems and the Innovation and Organizational Sciences Programs [VOSS-IOS: Organizational Participation in Open Communities, 1122642].

## References

Ågerfalk P, Fitzgerald B (2008) Outsourcing to an unknown workforce: Exploring opensourcing as a global sourcing strategy. MIS Quart. 32(2):385–409.

Becker HS (2008) Art Worlds (University of California Press, Berkeley, CA).

Berente N, Claggett J, Howison J, Knobel C, Rubleske J (2012) Managing CI centers: An agenda for organizational scholarship and cyberinfrastructure innovation. Working paper, University of Georgia, Athens, http://ssrn.com/abstract=2128872.

Borgmann A (1995) The depth of design. Buchanan R, Margolin V, eds. Discovering Design: Explorations in Design Studies (University of Chicago Press, Chicago), 13–22.

Boyatzis RE (1998) Transforming Qualitative Information: Thematic Analysis and Code Development (Sage Publications, Thousand Oaks, CA).

Brooks FP (2010) The Design of Design: Essays from a Computer Scientist (Pearson Education, Upper Saddle River, NJ).

Buchanan R (1995) Rhetoric, humanism, and design. Buchanan R, Margolin V, eds. Discovering Design: Explorations in Design Studies (University of Chicago Press, Chicago), 23–66.

Chesbrough HW (2006) Open Innovation: The New Imperative for Creating and Profiting from Technology (Harvard Business School Press, Boston).

Chiasson M, Germonprez M, Mathiassen L (2009) The conventional role of research methods in information systems field research. Inform. Systems J. 19:31–54.

Ciborra C (2002) The Labyrinths of Information: Challenging the Wisdom of Systems (Oxford University Press, Oxford, UK).

Coleman EG (2012) Coding Freedom: The Ethics and Aesthetics of Hacking (Princeton University Press, Princeton, NJ).

Corbet J, Kroah-Hartman G, McPherson A (2012) Linux kernel development: How fast it is going, who is doing it, what they are doing, and who is sponsoring it. Linux Foundation Publications, San Francisco, http://go.linuxfoundation.org/who -writes-linux-2012.

Crowston K, Wiggins A, Howison J (2010) Analyzing leadership dynamics in distributed group communication. Proc. 43rd Hawai’i Internat. Conf. System Sci., Manoa, HI.

Crowston K, Annabi H, Howison J, Masango C (2004) Effective work practices for software engineering: Free/libre open source software development. WISER Workshop Interdisciplinary Software Engrg. Res., SIGSOFT Conf., Newport Beach, CA.

Crowston K, Wei K, Howison J, Wiggins A (2012) Free/libre opensource software development: What we know and what we do not know. ACM Comput. Surveys 44(2):paper 7.

Dahlander L (2007) Penguin in a new suit: A tale of how de novo entrants emerged to harness free and open source software communities. Indust. Organ. Change 16(5):913–943.

Dahlander L, Magnusson MG (2005) Relationships between open source software companies and communities: Observations from Nordic firms. Res. Policy 34(4):617–635.

Dahlander L, Magnusson MG (2008) How do firms make use of open source communities? Long Range Planning (41):629–649.

Dahlander L, Wallin MW (2006) A man on the inside: Unlocking communities as complementary assets. Res. Policy 35(8): 1243–1259.

Daniel S, Maruping L, Cataldo M, Herbsleb J (2011) When cultures clash: Participation in open source communities and its implications for organizational commitment. Internat. Conf. Inform. Systems, Shanghai, China.

Daniel SL, Agarwal R, Stewart K (2012) The diverse effects of diversity in global, distributed collectives: A study of user participation in open source projects. Inform. Systems Res. 24(2):312–333.

Davison R, Martinsons M (2002) Empowerment or enslavement? A case of process-based change in Hong Kong. Inform. Tech. People 15(1):42–59.

Dedrick J, West J (2007) Movement ideology vs. user pragmatism in the organizational adoption of open source software. Kraemer KL, Elliot M, eds. Computerization Movements and Technology Diffusion: From Mainframes to Ubiquitous Computing (Information Today, Medford, NJ), 427–452.

Dimoka A, Pavlou P, Davis F (2011) Research commentary– NeuroIS: The potential of cognitive neuroscience for information systems research. Inform. Systems Res. 22(4):687–702.

Doty DH, Glick WH (1994) Typologies as a unique form of theory building: Toward improved understanding and modeling. Acad. Management Rev. 19(2):230–251.

Durkheim E (1997) The Division of Labor in Society [Translation] (Free Press, New York).

Elliott MS, Scacchi W (2008) Mobilization of software developers: The free software movement. Inform. Tech. People 21(1):4–33.

Feller J, Finnegan P, Fitzgerald B, Hayes J (2008) From peer production to productization: A study of socially enabled business exchanges in open source service networks. Inform. Systems Res. 19(4):475–493.

Feller J, Fitzgerald B, Hissam S, Lakhani K (2007) Perspectives on Free and Open Source Software (MIT Press, Cambridge, MA).

Fitzgerald B (2006) The transformation of open source software. MIS Quart. 30(3):587–598.

Fitzgerald B, Kesan JP, Russo B, Shaikh M, Succi G (2011) Adopting Open Source Software: Challenges and Opportunities (MIT Press, Cambridge, MA).

Fjeldstad ØD, Snow CC, Miles RE, Lettl C (2012) The architecture of collaboration. Strategic Management J. 33(6):734–750.

Gambardella A, Hall B (2006) Proprietary versus public domain licensing of software and research projects. Res. Policy 35: 875–892.

Germonprez M, Warner B (2013) Organizational participation in open innovation communities. Eriksson Lundström JSZ, Wiberg M, Hrastinski S, Edenius M, Ågerfalk P, eds. Managing Open Innovation Technologies (Springer, New York), 35–52.

Germonprez M, Hovorka D, Gal U (2011) Secondary design: A case of behavioral design science research. J. Assoc. Inform. Systems 12(10):662–683.

Germonprez M, Kendall J, Kendall K, Young B (2014) Collectivism, creativity, competition, and control in open source software development: Reflections on the emergent governance of the SPDX working group. Internat. J. Inform. Systems Management 1(1/2):125–145.

Germonprez M, Allen JP, Warner B, Hill J, McClements G (2013) Open source communities of competitors. ACM Interactions 20(6):54–59.

Germonprez M, Kendall J, Kendall K, Mathiassen L, Warner B, Young B, Cao L (2012) Risk mitigation in corporate engagement with open source communities: Protection and compliance in an open source supply chain. Petter S, Mitchell A, eds. AIS SIG-IRWITPM Workshop. ICIS Conf. (AIS, Atlanta), 89–100.

Goth G (2005) Open source business models: Ready for prime time. IEEE Software 22(6):98–100.

Gregor S, Jones D (2007) The anatomy of a design theory. J. Assoc. Inform. Systems 8(5):312–335.

Gupta A, Smith K, Shalley C (2006) The interplay between exploration and exploitation. Acad. Management J. 49(4):693–706.

Gurbani VK, Garvert A, Herbsleb JD (2010) Managing a corporate open source software asset. Comm. ACM 53(2):155–159.

Hackman JR (1986) The design of work teams. Lorsch JW, ed. The Handbook of Organizational Behavior (Prentice Hall, Englewood Cliffs, NJ), 315–342.

Haefliger S, von Krogh G, Spaeth S (2008) Code reuse in open source software development. Management Sci. 54(1):180–193.

Hannan MT, Freeman JH (1984) Structural inertia and organizational change. Amer. Sociol. Rev. 49:149–164.

Hecker F (1999) Setting up shop: The business of open source software. IEEE Software 16(1):45–51.

Henkel J (2006) Selective revealing in open processes: The case of embedded Linux. Res. Policy 35(7):953–969.

Hevner AR, March ST, Park J, Ram S (2004) Design science in IS research. MIS Quart. 28(1):75–105.

Holmström H, Fitzgerald B (2006) Virtual community use for packaged software maintenance. J. Organ. Comput. Electronic Commerce 16(3/4):345–365.

Horgen T, Joroff ML, Porter WL, Schon DA (1999) Excellence by Design: Transforming Workplace and Work Practice (Wiley, Hoboken, NJ).

Horton K, Davenport E, Wood-Harper T (2005) Exploring sociotechnical interaction with Rob Kling: Five “big” ideas. Inform. Tech. People 18(1):50–67.

Hovorka DS, Germonprez M, Levy M (2015) Design history: Exploring corporate communities. Donnellan B, Gleasure R, Helfert M, Kenneally J, Rothenberger M, Chiarini Tremblay M, Vandermeer D, Winter R, eds. DESRIST Conf., Dublin, Ireland (Springer, New York), 47–52.

Howison J, Crowston K, Østerlund C, Bolici F (2012) Stigmery and implicit coordination in software development. Scott S, Venolia G, eds. Proc. 2012 ACM Conf. Comput. Supported Cooperative Work 4CSCW ’125 (ACM, New York), 11–15.

Hrebiniak LG, Joyce WF (1985) Organizational adaptation: Strategic choice and environmental determinism. Admin. Sci. Quart. 30:336–349.

Johnson JP (2006) Collaboration, peer review, and open source. Inform. Econom. Policy 18(4):477–497.

Jullien N, Zimmermann JB (2009) Firms’ contribution to opensource software and the dominant users skill. Eur. Management Rev. 6:130–139.

Kellogg K, Orlikowski W, Yeats J (2006) Life in the trading zone: Structuring coordination across boundaries in postbureaucratic organizations. Organ. Sci. 17(1):22–44.

Kelly K (2013) Dreams. Wired 21(5):48–57.

Kelty C (2008) Two Bits: The Cultural Significance of Free Software (Duke University Press, Durham, NC).

Kelty C (2013) There is no free software. J. Peer Production. http:// peerproduction.net/issues/issue-3-free-software-epistemics/ debate/there-is-no-free-software/.

Kendall JE, Kendall KE, Kah MMO (2006) Examining virtual organizations using fantasy theme analysis: A study of ICT policy advisors’ discourse about developing countries. J. Inform. Technol. Theory Appl. 8(2):1–20.

King JL (2011) CIO: Concept is over. J. Inform. Technol. 26:129–138.

Klein H, Meyers M (1999) A set of principles for conducting and evaluating interpretive field studies in information systems. MIS Quart. 23(1):67–94.

Kogut B, Metiu A (2001) Open-source software development and distributed innovation. Oxford Rev. Econom. Policy 17(2): 248–264.

Lakhani K, Wolf R (2005) Why hackers do what they do: Understanding motivation and effort in free/open source software projects. Feller J, Fitzgerald B, Hissam S, Lakhani K, eds. Perspectives in Free and Open Source Software (MIT Press, Cambridge, MA).

Lee C (2007) Boundary negotiating artifacts: Unbinding the routine of boundary objects and embracing chaos in collaborative work. Comput. Supported Cooperative Work 16(3):307–339.

Lee G, Cole R (2003) From a firm-based to a community-based model of knowledge creation: The case of the Linux kernel development. Organ. Sci. 14(6):633–649.

Lerner J, Schankerman M (2010) The Comingled Code: Open Source and Economic Development (MIT Press, Cambridge, MA).

Lerner J, Tirole J (2002) Some simple economics of open source. J. Indust. Econom. 50(2):197–234.

Levina N, Vaast E (2005) The emergence of boundary spanning competence in practice: Implications for implementation and use of information systems. MIS Quart. 29(2):335–363.

Levina N, Vaast E (2006) Turning a community into a market: A practice perspective on IT use in boundary spanning. J. Management Inform. Systems 22(4):13–38.

March JG (1991) Exploration and exploitation in organizational learning. Organ. Sci. 2(1):71–87.

Markus LM, Majchrzak A, Gasser L (2002) A design theory for systems that support emergent knowledge processes. MIS Quart. 26(3):179–212.

Mathiassen L, Nielsen PA (2008) Engaged scholarship in IS research—The Scandinavian case. Scandinavian J. Inform. Systems 20(2):3–20.

Mathiassen L, Chiasson M, Germonprez M (2012) Style composition in action research publication. MIS Quart. 36(2):347–363.

Mehra A, Dewan R, Freimer M (2011) Firms as incubators of opensource software. Inform. Systems Res. 22(1):22–38.

Melville N (2010) Information systems innovation for environmental sustainability. MIS Quart. 34(1):1–21.

Neus A, Scherf P (2005) Opening minds: Cultural change with the introduction of open-source collaboration methods. IBM Systems J. 44(2):215–225.

Page S (2009) Understanding Complexity (The Great Courses, Chantilly, VA).

Peffers K, Tuunanen T, Rothenberger M (2007–2008) A design science research methodology for information systems research. J. Management Inform. Systems 24(3):45–78.

Romme AGL (2003) Making a difference: Organization as design. Organ. Sci. 14(5):558–573.

Schaarschmidt M, Walsh G, von Kortzfleisch HFO (2015) How do firms influence open source software communities? A framework and empirical analysis of different governance modes. Inform. Organ. 25:99–114.

Sein MK, Henfridsson O, Purao S, Rossi M, Lindgren R (2011) Action design science. MIS Quart. 35(1):37–56.

Shah SK (2006) Motivation, governance, and the viability of hybrid forms in open source software development. Management Sci. 52(7):1000–1014.

Spaeth S, Stuermer M, von Krogh G (2010) Enabling knowledge creation through outsiders: Towards a push model of open innovation. Internat. J. Technol. Management 52(3/4):411–431.

Stallman R (1983) Free unix! http://www.gnu.org/gnu/initial -announcement.html.

Stewart KJ, Gosain S (2006) The impact of ideology on effectiveness in open source software development teams. MIS Quart. 30(2):291–314.

Stewart KJ, Ammeter AP, Maruping LM (2006) Impacts of license choice and organizational sponsorship on user interest and development activity in open source software projects. Inform. Systems Res. 17(2):126–144.

Stol K, Babar MA, Avgeriou P, Fitzgerald B (2011) A comparative study of challenges in integrating open source software and inner source software. Inform. Software Tech. 53(12): 1319–1336.

Stuermer M, Spaeth S, von Krogh G (2009) Extending privatecollective innovation: A case study. R&D Management 39(2): 170–191.

Tanriverdi H, Rai A, Venkatraman N (2012) Reframing the dominant quest for information systems strategy research for complex adaptive business systems. Inform. Systems Res. 21(4): 822–834.

Turner V (1967) Betwixt and between: The liminal period in rites de passage. Turner V, ed. The Forest of Symbols (Cornell University Press, Ithaca, NY), 93–111.

Van de Ven AH (2007) Engaged Scholarship: A Guide for Organizational and Social Research (Oxford University Press, Oxford, UK).

von Hippel E, von Krogh G (2003) Open source software and the private-collective model: Issues for organization science. Organ. Sci. 14(2):209–223.

von Krogh G, Haefliger S (2010) Opening up design science: The challenge of designing for reuse and joint development. J. Strategic Inform. Systems 19(4):232–241.

Wagstrom P, Mockus A, Herbsleb JD, Kraut RE (2010) The impact of commercial organizations on volunteer participation in an online community. Acad. Management Conf., Montreal.

Walls JG, Widmeyer GR, El Sawy OA (1992) Building an information systems design theory for vigilant EIS. Inform. Systems Res. 3(1):36–59.

Weick KE (1989) Theory construction as disciplined imagination. Acad. Management Rev. 14(4):516–531.

Wen W, Forman C, Graham S (2010) The impact of intellectual property enforcement on open source software adoption. ICIS 2010 Proc. (AIS, Atlanta), Paper 187.

Wenger E (1999) Communities of Practice: Learning, Meaning, and Identity (Cambridge University Press, Cambridge, UK).

West J, Gallagher S (2006) Challenges of open innovation: The paradox of firm investment in open-source software. R&D Management 36(3):319–331.

West J, Lakhani K (2008) Getting clear about communities in open. Indust. Innovation 15(2):223–231.

West J, O’Mahony S (2008) The role of participation architecture in growing sponsored online communities. Indust. Innovation 15(2):145–168.

Yamauchi Y, Yokozawa M, Shinohara T, Ishida T (2000) Collaboration with lean media: How open-source software succeeds. Durand DG, ed. Proc. 2000 ACM Conf. Comput. Supported Cooperative Work 4CSCW <sup>0</sup>005 (ACM, New York), 329–338.
