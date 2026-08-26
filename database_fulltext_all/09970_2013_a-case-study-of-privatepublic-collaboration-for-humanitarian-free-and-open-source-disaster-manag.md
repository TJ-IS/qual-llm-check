---
otero_id: 9970
otero_key: "EAN3CCW4"
title: "A case study of private–public collaboration for humanitarian free and open source disaster management software deployment"
authors: "Jessica P. Li; Rui Chen; JinKyu Lee; H. Raghav Rao"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.030"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A case study of private–public collaboration for humanitarian free and open source disaster management software deployment

Jessica P. Li <sup>a,</sup>⁎, Rui Chen <sup>b</sup>, JinKyu Lee <sup>c</sup>, H. Raghav Rao <sup>d,e,</sup>⁎⁎

<sup>a</sup> The State University of New York at Buffalo, 325 Jacobs Management Center, Buffalo, NY 14260, USA

<sup>b</sup> Miller College of Business, Ball State University, Whitinger Business Building, Room 203, Muncie, IN 47306, USA

<sup>c</sup> Spears School of Business, Oklahoma State University, 317 North Hall, 700 N. Greenwood Ave., Tulsa, OK 74106, USA

<sup>d</sup> MSS, School of Management, The State University of New York at Buffalo, 325 Jacobs Management Center, Buffalo, NY 14260, USA

<sup>e</sup> GSM, Sogang University, Republic of Korea

## a r t i c l e i n f o

Article history: Received 6 December 2011 Received in revised form 3 July 2012 Accepted 18 October 2012

Keywords: Disaster management Humanitarian FOSS Collaboration Private–public partnership

## a b s t r a c t

Free and open source software (FOSS) has been increasingly adopted for humanitarian purpose worldwide, yet the factors for successful deployment of humanitarian FOSS in a disaster situation remain largely unexplored. Drawing upon the Technology–Organization–Environment (TOE) framework, this study identi<sup>fi</sup>es the key issues in collaborative deployment of FOSS for humanitarian relief operations. The research further elaborates the key research issues by adopting a case study approach in which qualitative data were gathered from key informants from both private and public sectors. The results suggest that task–technology <sup>fi</sup>t, expertise management, and inter-organizational relationship management play critical roles in humanitarian FOSS deployment.

Published by Elsevier B.V.

## 1. Introduction

Natural disasters are characterized by large scale detrimental impacts and devastating consequences. Disaster management in practice is challenged in a number of ways. First, response organizations are often constrained by available resources in the affected regions. In addition, a disastrous event may involve rapidly changing conditions, hence frequently forcing responders to perform un-planned tasks. Furthermore, it involves multiple organizations working in a collaborative and coordinated manner. Free and open source software (FOSS) systems present a means to handle these challenges. FOSS offers system developers the freedom to reuse and further improve the software. In recent years, more and more responses to natural disasters have utilized FOSS for disaster management purposes. In general, the use of FOSS systems helps to develop response information systems that help manage humanitarian response resources (e.g. food, shelter, and medical supplies), distribute response intelligence, and coordinate response operations [27]. Thus FOSS has an advantage of bringing in various external expertise (since everyone has the freedom to pick up a FOSS and adapt it to their situations) in handling the challenges mentioned above and thus provides an attractive alternative in the evolution of a more effective disaster management tool.

The research on FOSS in humanitarian relief operations is still in its infancy. Only a handful of countries have full-<sup>fl</sup>edged disaster management information systems in place, yet few of them have actually been deployed full-scale. Considering its potential signi<sup>fi</sup>cance on disaster management, Guo et al. [20] called for new research to further our understanding of humanitarian FOSS. To date, a number of imperative research issues have not been thoroughly explored, including the success factors to the joint deployment of disaster FOSS by public and private sectors. The deployment of a FOSS system is a complex process and often involves multiple stakeholders who represent government agencies, non-government organizations, and volunteers. Without a quick and well-executed deployment, a FOSS system may not achieve its full potential, leaving human lives and properties at risk. The current study <sup>fi</sup>lls this research gap by answering the question of: “What are key issues that affect the success of private–public collaborative deployment of humanitarian FOSS systems?” We identify the imperative issues in FOSS deployment through the lens of the Technology–Organization–Environment (TOE) framework [36]. To elaborate our understanding of the issues, we collect qualitative data about humanitarian FOSS collaboration projects. The data was collected from key informants in private and public sectors who participated in recent disaster management operations worldwide.

Based on the previous literature and our data, we present a set of research propositions.

This paper contributes to the literature of disaster management and FOSS. Research in disaster management information systems design has largely ignored the potential role of FOSS. Through the examination of FOSS deployment with qualitative data collected from global leaders in the <sup>fi</sup>eld, we discuss the potential of humanitarian FOSS for leveraging public and private resources to meet the demand of disaster response. Our study contributes to FOSS literature as we identify the major issues that contribute to the successful deployment of humanitarian FOSS. The research propositions developed in this study are backed by our empirical data and can be distilled to testable hypotheses in future research. The <sup>fi</sup>ndings in this study recognize a core set of antecedents of FOSS success and thus shed light on FOSS deployment. Our research also informs practitioners. Speci<sup>fi</sup>cally we identify issues that are important to help disaster response authorities properly manage FOSS projects. These cover critical aspects such as cost, adaptability, and data ownership in operating a FOSS for humanitarian purpose during large scale disasters.

This paper is organized as follows. The subsequent section introduces the background literature that leads to three focal research issues presented in the next section. Then, our research method and data collection process are described. Conclusions are drawn upon the data. We conclude the paper with discussions of our <sup>fi</sup>ndings, limitations, and avenues to future research.

## 2. Background

## 2.1. Free open-source software

Proprietary software and free open-source software (FOSS) are two popular, but very different business models in the current software marketplace. Proprietary software follows the “private investment” model, meaning that the innovation is carried out by private investment and is protected as intellectual property with a motive of achieving a return on investment as pro<sup>fi</sup>t [12,22,22]. Instead, FOSS follows the collective action model. The contributors share a collaborative sense of contributing their own efforts to a “common pool” as a public good and making the software freely available to all [22]. This implies that anyone can write, modify, or enhance the coding previously contributed by others. The process of learning, sharing, using, and modifying the codes is exercised in the process of the deployment of such systems [22]. GNU/Linux operating system, Apache web server, the Perl scripting language, and MySQL database management system are some of the popular open source software examples. Previously dependent on proprietary and commercial software solutions, organizations <sup>fi</sup>nd FOSS an important substitute for their software needs [5].

In recent literature, academia has recognized the signi<sup>fi</sup>cance of FOSS. Sharma et al. [34] developed a framework for creating a hybrid-OSS community within an organization to capture the bene-<sup>fi</sup>ts offered by FOSS. Crowston et al. [8] developed a theoretical model to explain the performance and effectiveness of FOSS teams. Currion et al. [9] studied how a FOSS system named SAHANA coordinated disparate institutional and technical resources to respond to the Indian Ocean Tsunami in 2004. Morelli et al. [27] examined the mobilization of virtual communities through FOSS systems in an earthquake response.

Some of this previous research focused on system design from the technology perspective, while other research was with regards to the social aspects of the technology/system adoption and diffusion. Other than Currion et al. [9] and Morelli et al. [27], our paper is among the <sup>fi</sup>rst few attempts at studying FOSS in the context of disaster management. A summary of a sample of literature is listed below with their main contributions (Table 1).

Table 1  
Sample literature with their main contributions.

<table><tr><td>Source and title</td><td>Contribution</td></tr><tr><td>Currion et al. [9,10] “Open source software for disaster management”</td><td>Discusses the significance of FOSS software for disaster management. It also discusses the component-based design in SAHANA and focuses on technological aspects.</td></tr><tr><td>[27] “A global collaboration to deploy help to China”</td><td>Descriptive report about the international collaborations on how IBM, SANAHA, and the government were involved in the deployment of a FOSS system to help in the recovery from the Sichuan earthquake.</td></tr><tr><td>[33] “Open source software success: measures and analysis”</td><td>Empirical study of the factors of OSS success as measured by the number of subscribers and developers. The determinants from the technical perspective were found to measure the success of an OSS project.</td></tr><tr><td>[21] “Adoption of open source software: the role of social identification”</td><td>Focuses on the technological and social factors that drive a successful OSS adoption and diffusion. The integrated model was built and evaluated quantitatively.</td></tr><tr><td>[30] “An incident information management framework based on data integration, data mining, and multi-criteria decision making”</td><td>An incident information management system to deal with challenges after a disaster is architected: includes three main modules: high-level data integration module, data mining module, and a multi-criteria decision-making module.</td></tr><tr><td>[25] “Group value and intention to use – a study of multi-agency disaster management information systems for public safety”</td><td>Uses the IS success model and looks at the group value in a large-scale disaster management for public safety. The expected value of IS for collaborating organizations was a major factor studied.</td></tr><tr><td>[35] “Determinants of open source software project success: a longitudinal study”</td><td>Longitudinal data is used to investigate the success of an open source software project. The determinants include OSS license, user-interest, and developer-interest from both the time-invariant and time-dependent perspectives.</td></tr></table>

In this paper, we extend our exploration to study the issues of a successful FOSS deployment in disaster management. While Morelli et al. [27] focus on a similar topic as we have, their report is more descriptive in nature whereas we carry out a qualitative study, to <sup>fi</sup>nd the major factors that drive public–private collaboration in the context of a humanitarian OSS project. Additionally, while some authors have focused on the technical determinants (e.g. [30,33]) our paper has a strong focus on the social perspectives wherein we study the factors of the successful deployment. Additionally, the dimension of human private–public collaboration in the system is also a main focus in our paper. Our study therefore relates to but also departs from the prior studies at both theoretical and methodological levels.

## 2.2. Technology–organization–environment (TOE) framework

Following Vitharana et al. [38], we <sup>fi</sup>rst surveyed the theoretical underpinnings that we could use to explain private–public collaboration in the deployment of disaster management information systems. One analytical framework that we considered was the technology–organization–environment (TOE) framework [36]. At its essence, TOE identi<sup>fi</sup>es three sources of in<sup>fl</sup>uences: technological, organizational, and environmental factors. Technical factors include both technical instruments and processes and require a <sup>fi</sup>t between the task at hand and the technological resources available to react to the situation. Organizational factors are the characteristics and resources that belong to an organization. Environmental factors refer to the social context within which an organization functions. These factors present “both constraints and opportunities for technological innovation” ([36], p. 154). TOE has been used in directing system deployment within the organizational context. A few instances of empirical study regarding technology innovation have used the TOE as a basic framework, including MRP adoption research [7], e-commerce adoption research [41], the adoption of mobile commerce in the insurance industry [24] and governmental adoption on FOSS [20]. Recently Gebauer and Ginsburg [17] examined the black box of task–technology <sup>fi</sup>t in the mobile information system domain and identi<sup>fi</sup>ed ‘use context-related <sup>fi</sup>t’. It is argued that a good match between the information systems and the organizational tasks and context is very important to the system's success [17,19]. Liu et al. [26] investigated the framework of task–individual–technology <sup>fi</sup>t, where ‘individual’ was added as a further dimension. It is argued that the choice of individuals can affect the performance signi<sup>fi</sup>cantly [26]. In our research, we use the TOE categorization to develop factors that are important for successful humanitarian FOSS deployment and extend it to focus on potential partnerships and collaborations across <sup>fi</sup>rms, such as private–public partnerships that are important for disaster response and humanitarian FOSS.

In disaster management, there is potentially a great deal of uncertainty with the situation. Therefore, regarding the technological aspects, coping with urgent tasks in an uncertain environment requires the balancing of cost and adaptability of both technological artifacts and processes [6,23,40]. This is where the “open source code” characteristics of humanitarian FOSS would have a considerable impact. To this end, data ownership and security is an important aspect because of the various different types of data that would need to be made available across organizations while ensuring their security. Sensitive information needs to be carefully protected against data leakages.

Regarding the organizational aspects, the strength of FOSS programming is its community-based deployment approach that invites multiple participants in system deployment. Disastrous events introduce wide impacts on a region and their responses call for joint efforts from multiple participating organizations. These organizations may have never worked together in the past and there is a lack of acquaintance and interaction experience. As a consequence, participants may not be aware of the knowledge and capability of each other, creating a barrier in inter-organizational engagements such as collaborative deployment of FOSS. To this end, clearly collaboration and sharing of knowledge resources are important within [28] as well as across organizations. Three components “what the knowledge is about, what the individual believes they are capable of knowing and what the individual knows about others' knowledge and expertise” are critical in the context of humanitarian FOSS as well [14]. Timely and effective knowledge sharing is important for disaster management. In a disaster recovery situation, people and organizations that may not ordinarily collaborate to synthesize expertise must work together quickly and effectively. A feature of disaster response is that disasters are unexpected and hence humanitarian FOSS deployment teams are formed on the <sup>fl</sup>y and as such FOSS expertise is coordinated without full knowledge of member credibility and capabilities. The deployment team resembles an emerging temporary or task oriented organization with many players unknown to each other. Therefore, knowledge and experience with the system (there is no guarantee of the capabilities of a participating organization), and awareness of skill sets of collaborators (the deployment teams may be loosely coupled and have lack of integration and transparency) are critical to successful deployment.

Finally with regard to the environmental aspect, i.e. the social context in which the organizations function, a critical stakeholder is the government, the primary <sup>fi</sup>rst responder in emergency and disaster situations. There is a lack of prior interactions and credibility of participants is not clear, since emergency operations are expected to be a temporary exercise and the teams operate as a temporary organization. Relationships among participants with weak ties (or prior nonexistent ties) must be managed properly. In order to encourage continuity and cooperation, it is important to strengthen trust between government and the deployment teams [31]. This also requires strong government senior level management support.

In the aftermath of a disaster, rescue crews, government agencies, and private organizations all interact in a chaotic and complicated manner. All information technologies and human interactions in the given social structures as well as organizational procedures and rules do matter in the collaboration of these entities. Some of the major sources of in<sup>fl</sup>uence of humanitarian FOSS collaboration stem from information technology, the organizational and social environment, as well as partnership between private and public organizations.

While TOE offers an integrated framework to study FOSS deployment from technological, organizational, and environmental perspectives, we augment TOE with concepts from other literature so as to understand the managerial challenges that come with typical disaster management. The fact that participating organizations do not possess knowledge to discover expertise and that they lack strong ties to collaborate calls for the aforementioned extensions.

## 3. Issues identi<sup>fi</sup>ed by TOE framework

## 3.1. Research issue 1: task–technology fit

The task technology <sup>fi</sup>t perspective in the TOE model underscores several technical features that pertain to the disaster context. Task technology <sup>fi</sup>t stresses that the matching of technology to tasks brings improvements in work effectiveness [13]. For proper <sup>fi</sup>t to be achieved in a disaster response task, there is the need for low cost, high adaptability, and clarity of data ownership and security issues.

The low cost of FOSS makes it attractive in disaster management. Financial constraints are usually a substantial challenge to response organizations when a disaster occurs. Few countries and organizations commit suf<sup>fi</sup>cient resources to disaster management, regardless of past experience or future potential [10]. The low cost feature of FOSS therefore <sup>fi</sup>ts this need very well. As Currion et al. [10] point out, “FOSS deployment leverages the goodwill and expertise of a global community of IT and non-IT actors at low cost”; FOSS solutions can be supported by technological organizations around the world helping their affected communities. A FOSS solution can potentially pull resources from a vast pool of programmers. All the bene<sup>fi</sup>ts are from social goods, which are free.

Adaptability and <sup>fl</sup>exibility may be another major advantage of FOSS for meeting the particular needs of disaster management. In contrast, proprietary software in general restricts system adaptation and offers limited recon<sup>fi</sup>guration options; its modi<sup>fi</sup>cations often require the involvement of specially trained programmers from the vendors, who may not be able to join and participate in the mitigation to disasters. In the case of humanitarian FOSS system, it can be relatively easily set up, adapted, and con<sup>fi</sup>gured quickly by independent third-party system developers and volunteers, so that it can become responsive to rapidly changing situations [10]. To be used in a local environment, especially one that is non-English speaking, the step of localization is essential. Without adaptability, a FOSS system could not be applied in many countries.

To work with a government leading a disaster response, another area of high concern is data security and ownership. Response to disasters often involves con<sup>fi</sup>dential data that describes the existing response plans, victim identities, medical information, and casualties. In the case of proprietary software, humanitarian systems go through a thorough developmental and testing process and fully comply with the applicable security standards. In addition, organizations that adopt this proprietary software own full possession of the system data. Data security and ownership is therefore not a salient problem for such proprietary systems. In contrast, government and non-government organizations rely on volunteers to develop humanitarian FOSS systems. These volunteers may not be completely veri<sup>fi</sup>ed for their credentials and background. Given the time constraint and resource limitation, the development processes may not fully comply with the highest security standards in the industry. In addition, voluntary developers may be invited to modify FOSS systems while they are actively used during disaster responses. Data security and ownership is therefore a salient issue. Government agencies will not tolerate the leakage of critical data and potential subsequent malicious misuse of this data by others. Thus the protection of data needs to be prioritized and protective designs are expected. In a lot of the cases, the government would like to have the ownership and control of the data.

The above leads us to our <sup>fi</sup>rst research issue for further exploration:

Issue 1. What are the aspects of task technology <sup>fi</sup>t (low cost, high adaptability, and data ownership) that will affect the success of private–public collaborative FOSS deployment in disaster management.

3.2. Research issue 2: community of interest and knowledge awareness among community members

Open-source software development is collaborated through a broad community of interest [22]. Therefore, in addition to technological factors, organizational factors play an essential role in humanitarian FOSS deployment [18]. Programmers from all over the world voluntarily contribute to the code. As a result, it is dif<sup>fi</sup>cult, if not impossible, to ensure that the team is creating high quality code in a collective manner. To this end, a number of imperative issues must be considered before the community as a whole can successfully pursue its objective in system deployment.

The availability of personnel with appropriate skills and knowledge is important to the successful deployment of humanitarian FOSS [18]. In particular, members' knowledge and experience with the systems that are embedded in FOSS deployment will help them to avoid the snares in system deployment and contribute to skillful use [13]. In the case of proprietary software, system vendors are not challenged by the availability of experts in that they may recruit top-notch system developers. On the contrary, FOSS humanitarian systems are solely developed by volunteer developers who are equipped with mixed skills and knowledge. There is no guarantee of highly trained expert professionals who may join and contribute to the FOSS design. Chau and Tam [4] suggested that technical expertise of existing IT staff members is a barrier to the open system deployment. When a FOSS deployment team is assembled to assist in a disaster management operation, the team must be equipped with relevant skill sets and knowledge, or the ability to quickly acquire the missing capacity.

Awareness of the collaborative team's knowledge and support structures is important since these are the sources for planning and accomplishing the tasks. Unlike the case of proprietary software development where system developers mostly work in the same organization, FOSS humanitarian systems are made possible by volunteer developers who have no prior acquaintance with each other. They team together at the instance of a disaster and there is a lack of shared metastructure among each other. They will need the aforementioned awareness in order to develop mechanisms for collaboration and coordination. Without such cognizance, the deployment of FOSS may be delayed or halted completely. Morelli et al. [27] underscored the importance of deployment teams of disaster management system, and most importantly, the knowledge, experiences, and team effort that they provide to help the community. This combination of knowledge, expertise, and collaboration skills is sparse and involves a lengthy learning process, which can be nurtured or arranged by a group, organization, or the volunteer pool. For example, a deployment team may have knowledge about social structures, but if it were short of expertise in disaster systems, a sponsor organization may need to search for the required but missing talents. In these cases, organizational knowledge of volunteer developers and their skills will play a signi<sup>fi</sup>cant role in facilitating this search process and pooling the collective efforts in building an effective FOSS through cross team and/or organizational-collaborations. In case a structure is better known, there will be consistency in the way the system is deployed. Consequently more effective use of the FOSS system may follow.

This leads to the next issue for further exploration:

Issue 2. How does deployment support from organizations and volunteers (inclusive of knowledge and experience of deployment and awareness of the skill set of collaborators) affect the success of private–public collaborative FOSS deployment in disaster management.

## 3.3. Research issue 3: support from social environment

Social environment support may directly affect FOSS system deployment in the context of extreme events. This dimension of in<sup>fl</sup>uence is unique to disaster response information system development since their usage is closely supervised by government. Among others, social environment support concerns top management support. Prior studies have underlined top management support as an important factor on IT development [4,7,18]. Glynn et al. [18] projected that upper management support could be even more important to FOSS deployment than the overall IS infrastructure. Chengalur-Smith et al. [5] found that senior management plays an extremely important role in choosing the technologies of FOSS. We believe this is true for disaster response situations as well where federal governments oversee disaster relief planning and preparation [29]. Many decisions after a disaster have to be made quickly upon review of the immediate area. Without support from the presiding government, decisions on task critical issues, including the deployment of humanitarian FOSS, could be seriously delayed.

Moreover, social environment support may be affected by private– public trust. In the aftermath of a disaster, the government leads the overall recovery process with the participation of volunteer private sectors. Without trust between the public and private sectors, the deployment team would not have received needed support and resources from local authorities. Chengalur-Smith et al. [5] suggested that organizations with stronger ties to the open source community-of-practice may realize more bene<sup>fi</sup>ts from implementing a FOSS project. For example, disaster management may encounter response data that is inaccurate, incomplete, and inconsistent. Data quality assessment is critical [37]. While public and private organizations are likely to keep data repositories that are valuable to triangulate response data, they may be reluctant to share the data with one another. A presence of trust among these organizations will remove perceived uncertainty in data sharing and its subsequent use, consequently encouraging the parties to pool their data repositories in a jointed effort to certify response data.

As a consequence, the following research issue is raised:

Issue 3. How does social environment support (including governmental support and trust between public–private partnership) impact FOSS deployment in disaster management.

## 4. Methodology and data collection

In this study, we examine humanitarian FOSS deployment through the example of the SAHANA system. SAHANA is a leading humanitarian FOSS system for disaster management purposes. “SAHANA” means “relief” in Sinhala, the language of Sri Lanka. It was <sup>fi</sup>rst built by volunteers in the Sri Lankan IT industry and deployed by the Sri Lankan government to help with disaster management after the 2004 Sri Lankan Tsunami (www.wikipedia.com). The SAHANA foundation describes the uniqueness of SAHANA as follows: “SAHANA software projects are different. They are about providing open source solutions for disaster victims and those seeking to help disaster victims. It is about the essence of humanitarianism; doing good in the world” (http://sahanafoundation.org). This free and open source disaster management information system has been growing with deployments during many massive disasters including the tsunami in Sri

Lanka (2004), ‘Asian Quake’ in Pakistan (2005), ‘Southern Leyte Mudslide Disaster’ in Philippines (2006), ‘Sarvodaya’ in Sri Lanka (2006), ‘Terre des Hommes’ in Sri Lanka (2006), ‘Yogyakarta Earthquake’ in Indonesia (2006), ‘Peru Earthquake’ in Peru (2007), ‘Myanmar Cyclone’ in Myanmar (2008), ‘Sichuan Earthquake’ in China (2008), and ‘Haiti Earthquake’ in Haiti (2010) (www.wikipedia.com). Given the positive impacts that SAHANA made on collaborative disaster response and recovery, SAHANA has been well recognized in the FOSS communities, receiving the Red Hat Award [10].

To ful<sup>fi</sup>ll the needs of disaster relief organizations, SAHANA includes the following basic components:

• Organization registry: to monitor and coordinate agencies and their geographic coverage

• Missing people/disaster victim registry: to track missing, displaced, injured, and deceased individuals and allow people to <sup>fi</sup>nd family and friends through its search engine

• Shelter registry: to track and manage shelters and their residents

• Request management system: to track supply and demand of aid

• Inventory management: to track locations and qualities of response resources

• Situation awareness: to collect updates of incident development

• Volunteer coordination: to maintain the directory of volunteers with contact and availability

Many organizations and large IT companies have shown interest in private–public collaboration for disaster management. We choose to collect qualitative data from IBM, since IBM has actively participated in disaster response over the years. IBM crisis response teams have deployed many SAHANA systems around the world and successfully aided governmental disaster responses in multiple natural disasters, including the Indian Ocean Tsunami and China Sichuan Earthquake. Their work in disaster relief has been widely acknowledged by the community. Mr. Susilo Bambang Yudhoyono, the President of Indonesia, recognized IBM for its “continued commitment to aid the people of Aceh and Nias, still suffering from the aftermath of the tsunami that hit the region in 2004.” (http://www.ibm.com/ibm/ibmgives/awards/ index.shtml). In response to the 2008 Sichuan massive earthquake, IBM deployed a SANAHA disaster management system, which was quickly adopted by the local authorities to help their disaster relief efforts. In a newsletter from IBM-China's communication of<sup>fi</sup>ce, the CTO of IBM-China James Yeh gave the following speech with pride [27]:

“All our hard work and sweat paid off when families reunited with their missing members! It was really an emotional moment of truth when we saw the happy tears… Eventually, we can say with pride that what we have done is worth remembering for our whole life. We helped people in the disaster area with our technology. We allied the best talents in IBM and contributed to the open source community.”

Vitharana et al. [38] emphasized that it is critical to get multiple data sources in qualitative case study. Following Vitharana et al. [38], we solicited information from numerous sources in addition to IBM. We contacted three governmental organizations who were heavily involved in the SAHANA deployment. We contacted of<sup>fi</sup>cials at the SAHANA foundation. All these inputs allow us to triangulate the inputs from IBM and to develop a holistic view of FOSS systems in disaster management.

## 4.1. Data collection

Seaman [32] has stated “The principal advantage of using qualitative methods is that they force the researcher to delve into the complexity of the problem rather than abstract it away. Thus, the results are richer and more informative”. Seaman [32] especially noted the needs for qualitative methods for the study of broad issues of software deployment. Given that the topic of understanding governmental adoption of FOSS in disaster management is very complex, involving many different factors and stakeholders, we decided to adopt the qualitative case method in this research [2,15,16]. Our aim in the data collection phase was to gain rich and deep insights. Accordingly, we tried to gather the maximum amount of information by giving the interviewees the freedom to tell us their story, share their experiences, and express their opinions covering any topic that they felt was relevant.

A six-step data collection approach was utilized as shown below:

1. Contact the key contacts of the IBM, SAHANA team, and government agencies in various countries that have experienced disasters.

2. Discuss the potential questions with them to modify or add new questions based on the deployment of the SAHANA product in that country. A list of sample questions is provided in Appendix A.

3. Discuss with the key contacts which individuals would be the appropriate and ideal interviewee to validate our propositions.

4. Identify the ideal interviewees that participated in SAHANA, re<sup>fi</sup>ne the questions, and agree on an interview time.

5. Phone interview those managers or engineers who were identi<sup>fi</sup>ed in step four.

6. Phone interview senior managers and developers from the government and public sectors.

First, senior engineers and project managers who participated in recent humanitarian FOSS deployment projects were interviewed. These interviewees are from multiple local subsidiaries of IBM who lent aid in most of the recent large-scale disasters. The interviewees, as the primary informants, offered their <sup>fi</sup>rst-hand observations and lessons learned in their projects. Then, of<sup>fi</sup>cials from a FOSS foundation and government agencies were interviewed to provide insights about the three research questions discussed in the previous section. All <sup>fi</sup>ve of the project managers and software engineers who we interviewed from IBM China directly participated in the SAHANA implementation project after the 2008 Sichuan massive earthquake. Some of them were sent on site in Chengdu, Sichuan, while others participated in the design, execution, and test processes in Beijing or Shanghai. Some of them were senior project managers and engineers, with many years of hands-on experience, while others were relatively junior, having graduated from college in the last few years. The project manager who we interviewed in Taiwan is the key person of the IBM SAHANA team in Taiwan. He has a crew working for him on this project on the localization and customization of SAHANA. The interviewee in Vietnam was also the key contact and main organizer of the IBM SAHANA implementation in Vietnam. He worked with local universities on the SAHANA project. The project manager that we talked to, in IBM India was an expert in FOSS and disaster management. He had participated in numerous FOSS implementations for disaster relief in India in the past. The software engineer in IBM India who we spoke with is also an expert in SAHANA. He was the key person in the SAHANA implementation team for the tsunami and other disasters in India.

From the side of government and public sectors, our interviewees include a senior of<sup>fi</sup>cer from SAHANA software foundation, one senior manager and a senior software developer from the government of New York City, and two senior of<sup>fi</sup>cers from the National Library of Medicine. They all had worked in the SAHANA deployment team in the corresponding organizations (Table 2).

Informing interviewees about the purpose of the interview is important [32,38]. Before we conducted all the phone interviews, we not only con<sup>fi</sup>rmed the time and date of the interview with the interviewees, we also introduced the purpose of the interview and attached the proposed questionnaire. All the interviews were conducted over the phone. All the interviews were tape recorded, with the conversations later transcribed into <sup>fi</sup>eld notes. Such <sup>fi</sup>eld notes can provide very detailed information [32]; while the recording allowed the researchers time to carefully examine the interview responses. The total of nine interviews in the rounds of data collection generated approximately 100 pages of double spaced text with around 27,000 words and 150,000 characters. The authors crosschecked the validity and consistency of the translation of the transcripts afterwards.

Table 2  
Basic demographics of our interviewees.

<table><tr><td>Interviewee</td><td>Organization</td><td>Activities participated related to SAHANA</td></tr><tr><td>Project manager</td><td>IBM Beijing – China</td><td>Full implementation of SAHANA used in the 2008 Sichuan Earthquake response</td></tr><tr><td>Senior software engineer</td><td>IBM Beijing – China</td><td>Full implementation of SAHANA used in the 2008 Sichuan Earthquake response</td></tr><tr><td>Project manager</td><td>IBM Shanghai – China</td><td>Full implementation of SAHANA used in the 2008 Sichuan Earthquake response</td></tr><tr><td>Senior software engineer</td><td>IBM Shanghai – China</td><td>Full implementation of SAHANA used in the 2008 Sichuan Earthquake response</td></tr><tr><td>Project manager</td><td>IBM Chengdu – China</td><td>Full implementation of SAHANA used in the 2008 Sichuan Earthquake response</td></tr><tr><td>Project manager</td><td>IBM Taiwan</td><td>Implementation of SAHANA in Taiwan – Localization stage</td></tr><tr><td>Project manager</td><td>IBM Vietnam</td><td>Implementation of SAHANA in Vietnam – Localization stage</td></tr><tr><td>Project manager</td><td>IBM India</td><td>Various FOSS projects for disaster relief including Indian Ocean Tsunami and Gujarat Earthquake</td></tr><tr><td>Senior software engineer</td><td>IBM India</td><td>Implementation of SAHANA for various disasters happened in India</td></tr><tr><td>Senior officer (CEO)</td><td>SAHANA Software Foundation</td><td>Guide the implementation of the various SAHANA projects worldwide.</td></tr><tr><td>Senior officer</td><td>The government of New York City</td><td>Implementation of New York&#x27;s shelter project using SAHANA platform</td></tr><tr><td>Senior software developer</td><td>The government of New York City</td><td>Implementation of New York&#x27;s shelter project using SAHANA platform</td></tr><tr><td>Senior officer</td><td>National Library of Medicine</td><td>Implementation of SAHANA disaster management system within National Library of Medicine</td></tr><tr><td>Senior project manager</td><td>National Library of Medicine</td><td>Implementation of SAHANA disaster management system within National Library of Medicine</td></tr></table>

## 5. Results

## 5.1. Task technology fit

The <sup>fi</sup>rst issue we delved into was the task technology <sup>fi</sup>t. In order to do so, we dissected the interviews from the perspective of cost, adaptability, and data ownership.

## 5.1.1. Cost

The low cost advantage of FOSS, which mainly derives from low maintenance cost, is con<sup>fi</sup>rmed with our interviews. A typical misconception of FOSS is that such software is free of any cost. In the context of humanity, however, FOSS is not free given that users have to invest a signi<sup>fi</sup>cant amount of time and efforts for system customization. The initial cost of FOSS may not necessarily be cheaper, or even in some cases more expensive than proprietary solutions. However, when the system is set up, the maintenance cost of proprietary solutions can be signi<sup>fi</sup>cantly higher due to the vendor lock-in problem [1]. This is also noted in some previous research. For instance, Currion et al. [10] stated that besides the initial cost in setting up a humanitarian FOSS disaster management system, there is very low cost to maintain. One of our interviewees offered some insight into this:

Actually the initial cost of open source may be higher with that level of customized support. However once you get it set up, your cost goes down to almost nothing. However, the private product charges you annual maintenance fee, license fee, etc. Those are things that you really don't need, just in order for you to continue to use it. (Senior Of<sup>fi</sup>cer of SAHANA Software Foundation)The proprietary solutions always have very high maintenance cost. For the open source system that we have, we have not updated the application for five years and it is still running. The only thing that we updated was the server. In most of the cases, it is stable, it is solid, and we really don't have to do much work about that. (Senior Of<sup>fi</sup>cer of SAHANA Software Foundation)

The above leads us to suggest our <sup>fi</sup>rst proposition:

P1.1. The low cost of humanitarian FOSS will positively affect the success of private–public collaborative FOSS deployment in disaster management.

There is one important thing that we have noticed. Unlike proprietary software, which mostly involves tangible expenses such as purchasing cost, FOSS incurs a great amount of intangible costs. FOSS is only made available due to the valuable contributions of volunteers and generous donations from the private sector. An outpouring of support in the aftermath of a disaster can leave the response team with a large surplus of people willing and able to do what they can, to help. “This can confer the responders the ability to pick and choose the most capable collaborators from the resource pool. This surplus of free manpower can help overcome many monetary shortages if a way can be found to utilize it.”, a Project Manager of IBM Beijing stated. This condition is not limited in scope to individuals, but includes private organizations large and small. A large number of companies are willing to help after a disaster. This free resource is extremely valuable and helps compensate for monetary constraints. Such a donation from the private sector has led to a very low cost of SAHANA. A few of our interviewees talked about this as follows:

IBM donated a good deal in support of the SAHANA system, which included a great amount of human resources. (Project Manager from IBM Beijing)If we calculate the monetary value of human resources IBM put into SAHANA, it would be an enormous amount. It is far more than the goods you can provide because the human resources are much more valuable. IBM is, to my knowledge, committed to donate its human resource rather than donating money or products. (Project Manager from IBM Shanghai)As to SAHANA, you don't have a license fee, but your cost in terms of labor and support might be equal or greater than the private product. For in the instance of IBM, it puts thousands of thousands of dollars in terms of labor in the project. (Senior Of<sup>fi</sup>cer of SAHANA Software Foundation)

FOSS deployments have the ability to receive a large amount of support in the form of people's time and effort. The ability to accept such donations in lieu of monetary aid is of enormous bene<sup>fi</sup>t. A proprietary solution cannot easily realize this bene<sup>fi</sup>t.

Therefore we suggest:

P1.1.1. In disaster management, the availability of voluntary and highly skilled human resources is a major determinant of the cost advantage of FOSS deployment.

## 5.1.2. Adaptability

Another praised feature of SAHANA is that it has a great adaptability. Proprietary software is not readily adaptable due to the lack of source code visibility to external developers. Unless dedicated support teams from the software vendor are on site during a disaster, proprietary software may not be modi<sup>fi</sup>ed in a timely manner. As a consequence, disaster management teams will have to reorganize their response activities around the existing system features. This problem is most salient in under-developed and developing countries where the local governments can't afford well-supported proprietary systems. In contrast, developed countries such as the

United States maintain ready-to-deploy systems such as the National Emergency Management Information Systems, the core system that Federal Emergency Management Agency uses for response and recovery management [11]. FOSS such as SAHANA enjoys a great level of adaptability due to the publicity of system design details. After an incident strikes, FOSS is able to be quickly adapted when such changes are most needed and subsequently make a more effective contribution to the response teams.

With FOSS, you can easily adapt it to the organization's different business processes. You don't have to go in and say ‘hey stop doing what you are doing now and we are going to give you a new method’. Instead, just keep doing what you are doing. What we are going to do is to get the system adapted to your process and help you do the job better, by handling the forms, the fields, and the matrix more efficiently. That is in general the biggest thing. With open source, in a couple hours, you can adapt that form into your database. (Senior Of<sup>fi</sup>cer from SAHANA Software Foundation)After a disaster happens, someone needs a solution to deal with it. They in general don't care whether it is open source or not. They want something that does the job for them. In my opinion, the adaptability and customizability are the strong points of open source projects. In our presentations, for example, we can say hey here it is already translated to your language. Or let me change the form here to match your paper form. Then they can see it fits their needs right away. (Senior Of<sup>fi</sup>cer from SAHANA Software Foundation)

## The above leads us to suggest the next proposition:

## P1.2. High adaptability will positively affect the success of FOSS deployment in disaster management.

Under the out-of-the-box nature, some customization is usually needed prior to its deployment, such as the language translation [3]. After this localization step, it can be easily implemented under different scenarios. Most of the interviewees are in countries where English is not the primary language. So, the <sup>fi</sup>rst task for the Chinese IBM team after the Sichuan earthquake was to translate and localize the SAHANA system. It was handled in a timely manner; otherwise the wide deployment would not have been a possibility. Below are some highlights of some of the experiences they shared.

A lot of components need to be customized based on local needs. For example, a default form asks about religion. It's not that applicable here. That's just one of the difficulties we faced. We have added a lot of information which was needed here while having to ignore many other items. This customization also applied to the selection of function modules too. We customized two modules. (Project Manager from IBM Shanghai) The Chengdu police told us what interface they would like to see and what information they would like to include. So we customized SAHANA based on their requirements. For example, to input Chinese characters, we use pin-yin. One of several pin-yin methods is to input only the initial pinyin letters and then select from a few options presented by the system. Almost all police officers in Chengdu were already familiar with this input method, so we had to implement this in the SAHANA program particularly for them. So the customization is a big issue here [where operational efficiency is linked to people's lives]. (Manager from IBM Beijing)

Two critical aspects of adaptability are localization/customization and the modularization of system for disaster management. Hence we suggest:

P1.2.1. Localization ability and availability of various functional module are two major dimensions of adaptability.

## 5.1.3. Data ownership and security

When a government is considering deployment of an innovative FOSS system such as SAHANA, one of the main points of concern is data ownership and security. With the FOSS option, the government also has the right to use the system and data, while this is not always the case with proprietary solutions. Governments will in general seek to avoid any risk of intrusion to their internal systems and data. This can create a barrier for adoption of FOSS technology if there are any doubts about data safety. Some insights from the public sector are offered here:

In a typical process, SAHANA is being adopted by the government or some organization. They have control of the system, the data security and decide who is using it.…One government, such as Pakistan, took the whole SAHANA code and integrated into their own system before being used in the governmental central call center …. It was never published, and none of the data was ever shared. The code was never released. It gives them the flexibility for them to accomplish it. (Senior Of<sup>fi</sup>cer from SAHANA Software Foundation)

In the case of the Sichuan earthquake, the Chinese government used the SAHANA system deployed in collaboration with IBM. One of the major reasons was the fact that local police were assured by the IBM team regarding the safety of their internal data. Some summaries are shown below from our interviewees.

In terms of systems architecture, it [implemented SAHANA] has two layers. One is called the backbone which is used for the policemen to input the data. The other one is the public facing interface for them to search with. For the backbone, we have user authentication with user access controls. For example, an individual may only see the modules to which he/she has permission to access. From the construction of — the police network, the two servers, one for the public search and the other for police input, are physically separated from each other. (Manager from IBM Beijing)The internal and external data are physically separate. So the internal data of the police is very safe since no external user has access to them. All the data we need from the police were downloaded by the police and physically handed over to us. (Engineer from IBM Shanghai)

The analysis above leads us to suggest the proposition:

P1.3. A high level of data ownership and security will positively affect successful private–public collaborative FOSS deployment in disaster management.

## 5.2. Deployment support from organizations and volunteers

Emergency response can be very chaotic given all of the numerous organizations and volunteers involved. Since FOSS programmers don't have well de<sup>fi</sup>ned boundaries, the work<sup>fl</sup>ow is very loose and one can leave or join at any time [34]. Without a well-organized and ef<sup>fi</sup>cient team, it is very hard for a FOSS disaster system to function in a timely manner. Thus ef<sup>fi</sup>cient deployment support from organizations and volunteers is very important to achieve a satisfactory performance of disaster response. Some insights from the manager from IBM Taiwan are shown below:

FOSS means that a lot of developers contribute to the codes, which does not necessarily mean the quality is not as good. There always needs to be someone to coordinate the whole process. (Project Manager from IBM Taiwan)

## 5.2.1. Knowledge and experience of the system

As IBM is a leading technology company equipped with thousands of knowledgeable engineers and experts in various <sup>fi</sup>elds, the team on site could always leverage the knowledge and support from other IBM groups during the Sichuan earthquake SAHANA deployment. The interviewees from IBM China crew showed the importance of the deployment team support. Some of the relevant transcripts are shown below:

In general, a large company like IBM has a lot of experience, a lot of technology support and human resources. They were able to help us very quickly deploy SAHANA and implemented it. Their knowledge and experience will definitely help! (Senior Of<sup>fi</sup>cer from the City of New York)The biggest disadvantage is that SAHANA has a very loose structure. If you want, you can add or delete modules. Everyone can contribute their own code to the different modules, so we don't have a standard quality across the various modules. The quality of some modules can be much higher than other modules. In our whole implementation process, we had to spend a lot of time to test it. We required a lot of people who knew about the loose structure to conduct the testing as it was of such a great scale. (Manager 1 from IBM Beijing)Except that they had a very high requirement with regards to timing, we treated it the same as we treat our other projects. So the whole process, including the initial design, and the communication with the clients, functionality tests, system tests, were all the same. Even though they are all volunteers, they are also all highly experienced engineers. The volunteers bring with them so much intelligence and experience from their fields. (Manager 2 from IBM Beijing)Even though SAHANA is an open source program, the program we delivered to the Chengdu police really wasn't open source because it had all the custom features added by our highly experienced engineers and project managers. They all treated it like any of their usual projects. This created a solid foundation for the success of SAHANA. (Engineer from IBM Beijing)

## The above leads to proposition

P2.1. Knowledge and experience of the system will positively affect the success of private–public collaborative FOSS deployment in disaster management.

## 5.2.2. Awareness of skill-set of collaborators

Furthermore, through FOSS platform, the emergency response of-<sup>fi</sup>cials can exchange ideas, experiences, and learn how things are done by different organizations and volunteers [39]. With this extended knowledge pool, the support could be more effective and stronger.

This is extremely important in disaster response. The commercially li censed software cannot be implemented to the large scale which open source software can. Everyone can access the code of the open source program. Finding the appropriate skill-set is not an issue here. The beauty is that if you would like to contribute, you will be able to. (Manager from IBM Beijing)I almost took this for granted. Like I was telling you, I actually used the global delivery center here in India which has many thousand programmers with various specialties. I was taking a very high quality team and high capability level for granted as we have access to that team, but that's not always the case everywhere. (Project Manager from IBM India)

## The above leads us to suggest the proposition:

P2.2. Awareness of the extended knowledge and support skill set will positively affect the success of private–public FOSS deployment in disaster management.

## 5.3. Social environment support

## 5.3.1. Governmental senior level management support

Government is a major player in this content. Our interviewees all detailed the critical role the government plays in the deployment process:

I did mention that the senior government support is critical. They don't have to be involved with the technical stuff, but the signal is very important. The high level government does not need to participate that much, but you do need a senior manager type to commit into the deployment. (Senior Of<sup>fi</sup>cer from SAHANA Software Foundation)It is really almost entirely dependent on the attitude of the government. If they are interested, they would show their requirement and ask the question how this system could integrate to their own database. It then would become a motive for us to move on to the implementation stage. This time, the Taiwan government did not show much interest to implement this system. They said they would try to use it. But I am not sure if they have actually used it. The government plays a huge role to ensure the success of the implementation. That is for sure! (Project Manager from IBM Taiwan)

For context, Taiwan did not successfully deploy the SAHANA project. The above leads to proposition

P3.1. Governmental senior level management support will positively affect the success of private–public collaborative FOSS deployment in disaster management.

## 5.3.2. Trust between the government and the deployment team

Trust between a government and any organization or individual can be dif<sup>fi</sup>cult to attain. Without mutual trust, it is very dif<sup>fi</sup>cult to promote a new technology or system to the government. Take IBM for instance. As a well-known, reputable IT <sup>fi</sup>rm with high social responsibility, for them to gain the government's trust can be much easier and straightforward. It is more likely for a governmental body to build a trustful relationship with large, well-known <sup>fi</sup>rms. This mutual trust could be established in many different forms, not just the reputation of a well respected company. For instance, mere words of promise and a legal contract can instate different levels of trust in the <sup>fi</sup>rm's promise of providing on-going maintenance services.<sup>1</sup> Little or unknown organizations will have a hard time overcoming the trust barrier with the government. In an emergency response situation, not only do they have to gain governmental trust, but they have to do so quickly. It is a hurdle, which can only be cleared by organizations with whom the government is already familiar. In the case of 2008 Sichuan earthquake, Chinese governmental authorities trusted IBM and involved IBM in the joint recovery operations [27]. In an instance where the government could not identify the collaborators that quickly, it is more likely for the government to hire its own agencies to do it.

… the Chengdu police are not willing to share their internal database with the external volunteer teams. However, when IBM volunteered for the development task, they decided to share a portion of their data. This would not be possible in a pure grass-root open-source project. The police trust us more compared to other random volunteers as we have the reputation of the firm to uphold. When the earthquake happened, you could find some people there with good intentions, but some may have malevolent purposes in mind. Without trust, it is very difficult to implement the project in an efficient way. It's not just a technical issue. (Engineer from Shanghai IBM)Because you had IBM there, it may be much easier for the government to agree. It may get the government feel more comfortable when they cooperate with a big technology firm. They don't need to participate, since they only need to know the system is working. In this case, IBM is successful in the public–private collaboration for reason. If you don't trust IBM, whom else will you trust? (Senior Of<sup>fi</sup>cer from the Government of New York City)

The above leads to proposition:

P3.2. Trust will positively affect the success of private–public collaborative FOSS deployment in disaster management.

Based on the above we propose the exploratory model in Fig. 1 below.

## 6. Discussion and conclusion

Disaster management faces numerous challenges in mounting a rescue effort, such as the lack of quali<sup>fi</sup>ed rescue staff, limitations of relief budget and resources, and a constant struggle against time. For response organizations, which often suffer from insuf<sup>fi</sup>cient resources under a disaster situation, humanitarian FOSS presents an attractive alternative with its unique characteristics, including an open and transparent technical architecture, low cost, and high adaptability. It is especially the case when there are not many private solutions available in the market. We have examined the major determinants of successful FOSS deployment in emergency management. The task–technology <sup>fi</sup>t, deployment support from organizations and volunteers, governmental support, and the trust between the public and private parties all have positive relationships with the success of this private–public collaborative deployment.

In addition to these relationships we measured, many of our interviewees also indicated the great importance and value of the human resources donated by people and companies. FOSS offers individuals and companies alike to make a far greater contribution to disaster aid in a non-monetary manner. With a successful deployment requiring a great deal of human resources, much of a highly skilled variety, being able to accept contribution of people's time and effort instead of currency is of enormous bene<sup>fi</sup>t. This is something which would be severely limited, if not impossible with an effort utilizing a proprietary solution.

We feel our research will be of interest to both practitioners and researchers. FOSS can potentially offer technological bene<sup>fi</sup>ts, yet successful collaboration for disaster management FOSS requires organizational and social level supports as well. Regarding the implications to the practitioners, our <sup>fi</sup>ndings can inform them of the key factors that affect the potentials for response organizations to explore this novel and economically preferable approach for disaster management. This could also help them better understand how the partnership between government and a private organization may be initiated in this area, how to encourage government to better support their deployment, and how to coordinate with different organizations and leverage the humanitarian FOSS advantages to the maximum extent. From a collaborative system deployment perspective, Table 3 highlights the key <sup>fi</sup>ndings of the current study and the implications to the disaster management as well:

One limitation of the current study is that only a qualitative case study was used to develop the research propositions. A further validation from a formal quantitative empirical study can also be conducted. This would not only tell us the relationship between the model constructs, but also measure the degree and extent of the relationships. This could serve as a direction for future research. In addition, this study looks at FOSS volunteers who are from IBM. All employed by the same organization, these volunteers exhibit fewer problems in volunteer structuring and organization. Additionally, IBM volunteers are paid by IBM and they are more committed to SAHANA deployment, whereas other volunteers may be restrained by their own jobs and family issues and cannot continue their services for a prolonged period of time. Future study may examine other types of volunteers (e.g., emerging, ad hoc groups) and understand the differences in humanitarian FOSS deployment.

## Acknowledgments

1. We are very grateful to the following individuals for participating in our interviews. They include the software engineers and project managers from IBM China, IBM Taiwan, IBM Vietnam and IBM India: Bin Li, Jin Li, Haijun Zhong, Jian Hu, Winston Wenju Zhang, David Liao, Pham Ngoc Van Giang, Sunil Raghavan, and Ravi Krishnan, CEO of SAHANA Software Foundation: Mark Prutsalis, Program Manager from New York City Of<sup>fi</sup>ce of Emergency Management: Michael Schultz, and Program Managers from the National Library of Medicine's Lost Person Finder Project: Michael Gill and Glenn Pearson. Without their generous help, this research would not have been possible

2. This research was funded by the National Science Foundation grants #0926376 and #0926371. The research of the fourth (correspondent) author has been funded in part by NSF under grant 0916612 and by Sogang Business School's World Class University Project (R31-20002) funded by the Korea Research Foundation as well as by the Sogang University Research Grant of 2011. The usual disclaimer applies.

## Appendix A

List of sample survey questionnaires:

(1) How do you (or from a broader stakeholders' point of view) evaluate the performance of SAHANA with the \*\*\* \*, \*\*\*, or other disasters?

![](/api/attachments/EAN3CCW4/fulltext/images/f019b420c7a40ee49041d8948087bee843ac580b6785d006fb04f7a162559582.jpg)  
Fig. 1. Proposed model.

Table 3  
Key <sup>fi</sup>ndings of the current study and implications to disaster management.

<table><tr><td>Factors</td><td>Impact on humanitarian FOSS</td><td>Implications for management</td></tr><tr><td>Cost</td><td>-Financial constraints are frequently a substantial challenge faced by government when a disaster occurs.</td><td>-Adopt the FOSS approach despite the likelihood of higher initial cost-The cost of labor, in terms of availability of high skill sets in the FOSS deployment community is very critical.-Leverage the goodwill and expertise of a global community of IT and non-IT actors at little cost to cover the intangible costs</td></tr><tr><td>Adaptability</td><td>-In order to fit to a specific situation, the system needs to be set up, adapted to the situation at hand, and localized quickly.</td><td>-Keep high modularity of FOSS systems-In countries where English is not the primary language, translation is the first necessary step for system deployment.-If translation and other localization steps could be performed ahead of time, a great deal of time would be saved.</td></tr><tr><td>Data ownership and security</td><td>-Governments and private organizations are protective of sensitive and confidential data.-Government prefers to have the ownership of data and system if possible.</td><td>-Government obtains the ownership of the data.-Guarantee the collaborators of the safety of any sensitive data-Separation between the government server, the FOSS system, and the public access method-Install security measures (e.g., firewall and access control list) wherever appropriate</td></tr><tr><td>Knowledge and experience of the system</td><td>-The staff&#x27;s knowledge of and experience with the system can be an enabler to the fast deployment of the relief system.</td><td>-Equip the team with relevant skill sets and knowledge through training programs and exercises-Equip the team with staff who has experience with the system and who can quickly assist with any missing capacity to respond to the current situation</td></tr><tr><td>Awareness of extended knowledge and support pool</td><td>-It is difficult for a group to obtain all the necessary knowledge and experience while simultaneously struggling against the clock.-Support from external groups can be in great surplus.</td><td>-Leverage knowledge from inside and outside the organization-Maximize collective efforts by increasing the boundaries of the working group and volunteers globally-Receive consultation and support from the FOSS organization</td></tr><tr><td>Government management support</td><td>-Without the government&#x27;s support, it is very different to obtain the resources needed or deploy the system in a timely manner.</td><td>-Create strategic relationship with government officials-Facilitate the government&#x27;s perception of the merits of the system</td></tr><tr><td>Private-public trust</td><td>-Without the trust, it is hard for the deployment to get any support or resources from the local authorities.-Trust can be a hurdle for collaboration and deployment.-After a disaster, multiple groups and organizations need to collaborate under the lead of the government.</td><td>-Build mutual trust foundation from long term relationships and from institutional trust-Get the parties familiar with each other-Establish a long term public-private relationship-Try to work with the government as closely and transparently as possible</td></tr></table>

a. Your de<sup>fi</sup>nition and examples of success and failures.

(2) Compared to proprietary software, what are the distinctive characteristics of FOSS systems in general (not just SAHANA), that contributes to the governmental deployment?

a. Cost

b. Low network dependency?

c. Adaptability

d. Security?

e. Any other advantages/functions?

f. Which feature(s) appeal the most to the government (expandability, capability of synchronization, localization and customization, separation of data)?

(3) Who leads the deployment of SAHANA systems in the recent disaster responses? Have you found any perceivable differences among the deployment teams in terms of:

a. Deployment team's knowledge and experience of the SAHANA system?

b. Government of<sup>fi</sup>cials' perception of the deployment team's knowledge and support structure?

c. In case of multiple teams jointly deploy SAHANA, how did the collaborative deployment go? Any issues?

d. In relation to the characteristics of the SAHANA deployment teams that worked on past disaster response projects, were there any team attributes/properties that seemed to in<sup>fl</sup>uence the success/failure of the SAHANA deployment project?

(4) How were governments involved (including foreign)?

a. Did the deployment teams receive support from upper-level government of<sup>fi</sup>cials? How important is it?

b. How did government of<sup>fi</sup>cials support or participate in the SAHANA deployment projects (frequency and variety)?

c. Was it possible for the deployment team to gain/build the trust from the government during the projects? If so, how??

d. How did government evaluate the contribution of SAHANA? Any metrics they used? What changes did they recommend to improve SAHANA?

e. Any con<sup>fl</sup>icts, restrains, or challenges that were raised during the deployment of SAHANA by the local government?

i. E.g., any policies and rules did the government pose as a condition under which the deployment makes take place?

ii. How did SAHANA meet the business requirements, if there is any that is set by the local government, in disaster management?

iii. To what extent did the local government deploy the system?

f. Including the issues discussed above, how did political and social environments affect the success of past SAHANA deployment projects?

g. Would government respond differently in dealing with proprietary disaster management systems?

h. Out of the many unique features of SAHANA, what features successfully attracted government and lead to the government deployment?

(5) Was time pressure an important factor that affects the governmental deployment of the system? If so, how did it affect the deployment decision?

a. Any other moderating role it may play?

(6) Was the severity of the disaster an important factor that affects the governmental deployment of the system? If so, how did it affect the deployment decision?

a. Any other moderating role it may play?

(7) Any other experiences and lessons to share? We are in particular interested to learn the new issues that arise due to the distinctive nature of FOSS.

## References

[1] W.B. Arthur, Competing technologies, increasing returns, and lock-in by historica events, The Economic Journal 91 (1989) 642–665.

[2] A. Bhattacherjee, Social Science Research: Principles, Methods, and Practices, 2001

[3] M. Careem, C.D. Silva, R.D. Silva, L. Raschid, S. Weerawarana, Demonstration of SAHANA: free and open source disaster management, in: The Proceedings of the 8th Annual International Conference on Digital Government Research: Bridging Dis ciplines and Domains, 2007.

[4] P.Y.K. Chau, K.Y. Tam, Factors affecting the adoption of open systems: an exploratory study, MIS Quarterly 21 (1) (1997) 1–24.

[5] I. Chengalur-Smith, S. Nevo, P. Demertzoglou, An empirical analysis of the busi ness value of open source infrastructure technologies, Journal of the Association for Information Systems 11 (2010) 708–729 (Special Issue).

[6] M. Conrad, Adaptability, Plenum Press, New York, 1983.

[7] R.B. Cooper, R.W. Zmud, Information technology implementation research: a technological diffusion approach, Management Science 36 (2) (1990) 123–139.

[8] K. Crowston, H. Annabi, J. Howison, C. Msango, Effective work practices for FLOSS development: a model and propositions, in: The Proceedings of the 38th HICSS, 2005.

[9] P. Currion, D.S. Chamindra, V.D.W. Bartel, Open source software for disaster management. Communications of the ACM 50 (3) (2007) 61–65.

[10] P. Currion, D.S. Chamindra, B.V.D. Walle, Open source software for disaster management, Communications of the ACM 50 (3) (2007) 61–65.

[11] F. Deffer, Federal Emergency Management Agency Faces Challenges in Modernizing Information Technology, Department of Homeland Security Of<sup>fi</sup>ce of Inspector General, Washington, DC, 2011.

[12] H. Demstz, Towards a theory of property rights, The American Economic Review 57 (1967) 347-359

[13] G. Desanctis, M.S. Poole, Capturing the complexity in advanced technology use: adaptive structuration theory, Organization Science 5 (2) (1994) 121–147.

[14] D. Devo, Y. Wand, Organizational memory information systems: a transactive memory approach, Decision Support Systems 39 (4) (2005) 549.

[15] K.M. Eisenhardt, Marking fast strategic decisions in high-velocity environment, Academy of Management Journal 32 (1989) 543–576.

[16] K.M. Eisenhardt, Building theories from case study research, Academy of Management Review 14 (1989) 532–550.

[17] J. Gebauer, M. Ginsburg, Exploring the black box of task–technology <sup>fi</sup>t, Communications of the ACM 52 (1) (2009) 130–135.

[18] E. Glynn, B. Fitzgerald, C. Exton, Commercial adoption of open source software: an empirical study, in: Proceedings of the 2005 International Symposium on Empirical Software Engineering, Institute of Electrical and Electronics Engineers, Queensland, Australia, 2005, pp. 225–234.

[19] D.L. Goodhue, R.L. Thompson, Task–technology <sup>fi</sup>t and individual performance, MIS Quarterly 19 (2) (1995) 213–236.

[20] X.H. Guo, H. Yang, N. Zhang, G.Q. Chen, Adoption of open source software in governmental context: a positive case study in China, in: The Proceedings of International Conference on Information Systems, 2010.

[21] K.L. Gwebu, J. Wang, Adoption of open source software: the role of social identi-<sup>fi</sup>cation, Decision Support Systems 51 (1) (2011) 220–229.

[22] E.V. Hippel, G.V. Krogh, Open source software and the “private-collective” innovation model: issues for organization science, Organization Science 14 (2) (2003) 208–223.

[23] R.R. Kampfner, Biological information processing: the use of information for the support of function, Biosystems 22 (1989) 223–230.

[24] C.-C. Lee, H.K. Cheng, H.-H. Cheng, An empirical study of mobile commerce in insurance industry: task–technology <sup>fi</sup>t and individual differences, Decision Support Systems 43 (1) (2007) 95–110.

[25] J. Lee, N. Bharosa, J. Yang, M. Janssen, H.R. Rao, Group value and intention to use — a study of multi-agency disaster management information systems for public safety, Decision Support Systems 50 (2) (2011) 404–414.

[26] Y. Liu, Y. Lee, A.N.K. Chen, Evaluating the effects of task–individual–technology <sup>fi</sup>t in multi-DSS models context: a two-phase view, Decision Support Systems 51 (3) (2011) 688–700.

[27] R. Morelli, C.d. Silva, T.d. Lanerolle, R. Curzon, X.S. Mao, A global collaboration to deploy help to China, Communications of the ACM 53 (12) (2010) 142–149.

[28] D. Nevo, Y. Wand, Organizational memory information systems: a transactive memory approach, Decision Support Systems 39 (4) (2005) 549–562.

[29] L. Palen, S.R. Hiltz, L.S. B, Online forums supporting grassroots participation in emergency preparedness and response, Communications of the ACM 50 (3) (2007) 54–58.

[30] Y. Peng, Y. Zhang, Y. Tang, S. Li, An incident information management framework based on data integration, data mining, and multi-criteria decision making, Decision Support Systems 51 (2) (2011) 316–327.

[31] L. Poppo, T. Zenger, Do formal contracts and relational governance function as substitutes or complements? Strategic Management Journal 23 (2002) 707–725.

[32] C. Seaman, Qualitative methods in empirical studies of software engineering, IEEE Transactions on Software Engineering 25 (4) (1999) 557–572.

[33] R. Sen, S.S. Singh, S. Borle, Open source software success: Measures and analysis, Decision Support Systems 52 (2) (2012) 364–372.

[34] S. Sharma, V. Sugumaran, B. Rajagopalan, A framework for creating hybrid-open source software communities, Information Systems Journal 12 (2002) 7–12

[35] C. Subramaniam, R. Sen, M.L. Nelson, Determinants of open source software project success: a longitudinal study, Decision Support Systems 46 (2) (2009) 576–585.

[36] L.G. Tornatzkey, M. Fleischer, The Processes of Technological Innovation, Lexington Books, Lexington, Mass, 1990

[37] M. Turoff, S.R. Hiltz, Assessing the health information needs of the emergency preparedness and management community, Information Services and Use 28 (2008) 3–4.

[38] P. Vitharana, J. King, H. Chapman, Impact of internal open source development on reuse: participatory reuse in action, Journal of Management Information Systems 27 (2) (2010) 277–304.

[39] C. White, L. Plotnick, J. Kushma, S.R. Hiltz, M. Turoff, An online social network for emergency management, in: The Proceedings of the 6th International ISCRAM Conference, 2009, (Gothenburg, Sweden).

[40] C. Williams, W. Mitchell, Focusing <sup>fi</sup>rm evolution: the impact of information infrastructure on market entry by U.S. telecommunications companies, 1984– 1998, Management Science 50 (11) (2004) 1561–1575.

[41] K. Zhu, K.L. Kraemer, Post-adoption variations in usage and value of e-business by organizations: cross-country evidence from the retail industry, Information Systems Research 16 (1) (2005) 61–84.

Jessica P. Li obtained her Ph.D. from The State University of New York at Buffalo. Some of her publications have appeared in Information Systems Frontiers, Electronic Journal of Information Systems in Developing Countries, International Iournal of Communications. Law and Policy, and other journals. She presented her research at major conferences on Information Systems, including ICIS. AMCIS. HICSS, and WITS.

Rui Chen is an Assistant Professor at Miller College of Business. Ball State University. He obtained his Ph.D. from The State University of New York at Buffalo. Some of his publications have appeared in Communications of the ACM, Communications of the AIS, Decision Support Systems, Journal of the AIS, and other journals. He received an Advanced Certi<sup>fi</sup>cate in Information Assurance from National Center of Excellence in Information Systems Assurance Research and Education (CEISARE). He is also a Microsoft Certi<sup>fi</sup>ed System Engineer (MCSE) and a Database Administrator (MCDBA).

JinKyu Lee is an Assistant Professor at Spears School of Business, Oklahoma State University. He obtained his Ph.D. from The State University of New York at Buffalo. He has published refereed journal and conference articles in CACM, ICIS, AMCIS, ECEG, Springer Lecture Notes in Computer Science and has been involved in several NSF, NSA, and DoD funded research/educational projects in e-government and information assurance areas

H. Raghav Rao is a Professor at the Management Science and Systems Department at the School of Management and an Adjunct Professor at the Computer Science and Engineering Department, The State University of New York at Buffalo. He obtained his Ph.D. degree from Krannert Graduate School, Purdue University. He is a Co-Editor-in-Chief of a new journal by Springer, Information Systems Frontiers: A Journal of Research and Innovation and an associate editor of Decision Support Systems, Information Systems Research, IEEE Transactions on Systems, Man and Cybernetics, Part A. He has also co-guest edited numerous special issues for leading journals including Decision Support Systems, the Communications of the ACM, and the Annals of Operations Research.
