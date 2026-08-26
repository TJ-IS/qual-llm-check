---
otero_id: 7488
otero_key: "PH3BH68X"
title: "An Empirical Analysis of the Business Value of Open Source Infrastructure Technologies"
authors: "Indushobha Chengalur-Smith; Saggi Nevo; Pindaro Demertzoglou"
year: "2010"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00242"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
11-25-2010

# An Empirical Analysis of the Business Value of Open Source Infrastructure Technologies

Indushobha Chengalur-Smith , shobha@albany.edu

Saggi Nevo , snevo@uamail.albany.edu

Pindaro Demertzoglou , demerp@rpi.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Journal of the Association for Information Systems JAIS

Special Issue

# An Empirical Analysis of the Business Value of Open Source Infrastructure Technologies

InduShobha Chengalur-Smith University at Albany - SUNY E-mail shobha@albany.edu

Saggi Nevo University at Albany - SUNY E-mail snevo@uamail.albany.edu

Pindaro Demertzoglou Rensselaer Polytechnic Institute E-mail demerp@rpi.edu

## Abstract

Organizations are increasingly interested in exploring Free/Libre Open Source Software (FLOSS) based technologies as viable alternatives to proprietary or commercial solutions, but research on the business value of such technologies is lacking. In this paper, we contribute to this important, yet understudied, topic by examining the antecedents of the business value of open source infrastructure technologies. The paper puts forward a new model for explicating the organizational benefits of these technologies. Our findings suggest that in order to realize benefits from open source infrastructure technologies, organizations should have the human and technological capacities to absorb and utilize them as well as the ability to establish, maintain, and leverage ties with the technologies’ communities of developers and users. The paper focuses on open source databases (specifically, MySQL) as an instance of open source infrastructure technology. A PLS analysis of 149 responses from organizations that have implemented MySQL revealed that absorptive capacity for the database, ties with the technology’s user/developer community-of-practice, and an open source IT infrastructure that facilitates MySQL utilization explain about 20 per cent of the business value of the open source technology. These findings should help organizations realize the numerous potential benefits of open source technologies.

Keywords: Open source, IT infrastructure, business value of IT, databases, absorptive capacity, value cocreation, community-of-practice

\* Michael Wade and Kevin Crowston were the accepting senior editors. This article was submitted on October 15, 2009 and went through two revisions.

Volume 11, Special Issue, pp. 708-729, November 2010

# An Empirical Analysis of the Business Value of Open Source Infrastructure Technologies

## 1. Introduction

A recent major development in information technology is the emergence of Free/Libre Open Source Software (FLOSS). FLOSS-based technologies make their source codes publicly and freely available, and provide the freedom to modify them. Previously considered a revolutionary movement in software development, FLOSS has become a driving force towards an open “source” movement in several different domains, including open courseware and open scientific publication (Boomen and Schäfer, 2005). FLOSS has attracted substantial interest from businesses, governments, and academics as an alternative to proprietary software as well as to commercial software development practices. Over the past decade, open source technologies in general, and open source infrastructure technologies in particular, have evolved to the point where they can practically compete on par with commercial packages (Bloor, 2005). Organizational adoption of open source technologies has occurred in waves, with the first wave being the implementation of open source operating systems and the second wave being the implementation of open source middleware solutions, browsers, and databases (Bruce et al., 2006). Commonly used open source technologies include the Apache web server, the MySQL database, the Linux operating system, the Firefox web browser, the OpenOffice office suite, and the Drupal content management system.

IT infrastructure has been identified as a top management concern due to its impact on firms’ efforts to achieve competitive advantage (Dai et al., 2005). For example, IT infrastructure can play a strategic role in that it entails growth options and can provide organizations with the capability of coping with change (Benaroch, 2002). Specifically, researchers have observed that organizations that invest in IT infrastructure in anticipation of future business needs will be better positioned to respond to new environmental demands (e.g., Fink and Neumann, 2009). Thus, IT infrastructure is a critical organizational resource and its business value should be closely scrutinized.

By their nature, infrastructure technologies tend to be transparent to end-users and the adoption decision is frequently undertaken by IT and other business executives on behalf of the entire organization (Byrd and Turner, 2000; Greis and Kasarda, 1997). The abovementioned unique characteristics of FLOSS, coupled with an organizational level of analysis that is required for infrastructure technologies, such as databases, web and mail servers, and operating systems, call for a modified model of business value of IT (BVIT). Existing models may not be appropriate for studying open source technologies since they were constructed with the underlying assumption that the focal technology is either proprietary (e.g., Mukhopadhyay et al., 1995, 1997; Rao et al., 1995) or closed source and sold on factor markets (e.g., Nevo and Wade, 2010; Ray et al., 2005; Zhu and Kraemer, 2005). To create models that are relevant for IS researchers and practitioners, the outcome variables should reflect the impact of the technology on the organization, i.e., explain how the technology helps to realize or create value for the adopting organization (Kohli and Grover, 2008). The means by which business value can be extracted from open source technologies could go beyond those traditionally considered in prior research – that is, proprietary or closed source technologies.

Furthermore, prior BVIT literature has focused on antecedents of business value that are internal to the firm or embedded in the firm’s value chain, such as resources, capabilities, and relationships with suppliers and buyers (e.g., Nevo and Wade, 2010; Ray et al., 2005; Tanriverdi, 2005; Wade and Hulland, 2004). However, as we argue later, realizing business value from open source technologies involves a new factor – namely, relationships with the open source community. This community-ofpractice is neither a component of the organization nor is it an element of its value chain. On the open source front, research has predominantly been focused inward on topics such as developer participation and contribution, leaving issues pertaining to the usage of open source technologies under-investigated (Fitzgerald, 2006). Consequently, our knowledge of the business value of open source technologies is incomplete. This paper aims to fill a gap in the existing literature on the impact of FLOSS and technology impact at the organizational level by conceptually and empirically examining the factors that affect the realization of the business value of open source infrastructure technologies.

The remainder of this paper is organized as follows. The next section further motivates the study and presents the theoretical support for our research model and hypotheses. We begin by grounding the relevant BVIT literature in the open source context and draw on absorptive capacity and related theories to develop our hypotheses about the antecedents of BVIT gained through the use of open source infrastructure technologies. We test our research model by focusing on a specific open source infrastructure technology, viz. open source databases. Next, we describe our instrument development process, as well as the data collection method. Subsequently, we use the data to assess our model and hypotheses and then discuss our results. We conclude with a presentation of the limitations of our study and avenues for future research.

## 2. Business value of IT: Literature review & theoretical foundations

The BVIT literature seeks to understand and evaluate the organizational benefits of IT investments. Business value has been assessed via efficiency gains (Lin and Shao, 2006), process performance improvements (Mishra et al., 2007), innovativeness (Lind and Zmud, 1991), and other indicators. Although this stream of literature is central to the IS discipline (Agarwal and Lucas, 2005), it has been recently argued that, as a field, not enough is being done to measure IT’s impact on organizations and there is a failure to address its evolving nature (Kohli and Grover, 2008). This study aims to contribute to this important literature by explicating the business value of open source infrastructure technologies and examining the organizational factors affecting them.

Infrastructure technologies may demonstrate their business value in several ways including productivity, efficiency, reliability, and security (Bayrak and Grabowski, 2006; Fink and Neumann, 2009; Gray and Hovav, 2007; Hoving, 2007; Zhu, 2004). Using commercial technologies often involves high exit costs due to vendor lock-in, as well as increased maintenance costs associated with forced upgrades (Niemi et al., 2009). In contrast, open source technologies do not have direct acquisition costs or licensing fees and can be scaled up at the cost of additional hardware alone (Brydon and Vining, 2008; Casadesus-Masanell and Ghemawat, 2006). Recent research suggests that organizations are starting to recognize the opportunities for value creation via FLOSS technologies (e.g., Garrison, 2009). However, even though FLOSS may be freely obtained, it has associated usage costs such as installation, maintenance, and support (Economides and Katsamakas, 2006). Hence, for FLOSS technologies to be considered cost-effective they must offer – after migration, maintenance, and support costs have been accounted for – a reduced total cost of ownership. Focusing on the higher education industry, Fitzgerald and Kenny (2004) found that even with academic discounts for commercial products, and after incorporating the costs of maintenance for open source products, it was advantageous to deploy open source components. Many government organizations, particularly in developing countries, also find FLOSS cost-effective (Kshetri, 2004).

FLOSS technologies provide an opportunity for organizations to customize the software to their own specifications (Sohn and Mok, 2008). Mature FLOSS technologies, such as Linux and Apache, have been calibrated against their proprietary counterparts and were found to be of comparable quality and, in some instances, to have fewer defects per line of code (van Wendel de Joode et al, 2006). Additionally, the availability of the source code can lead to greater confidence in the technology due to the perception that there are fewer hidden features and that bugs will be quickly fixed (Ven et al., 2008). Even if organizations do not modify the software, the ability to do so in the future creates a perception of greater control (Ven et al., 2008). Finally, the contributions of the user/developer community abate the risks traditionally associated with the required long-term maintenance of software (van der Linden et al., 2009). Thus, FLOSS technologies present some unique opportunities for gaining business value.

## 2.1. Antecedents of business value

The IS literature on the BVIT recognizes that in order for organizations to realize benefits from their investments in information technologies, complementary organizational resources must be leveraged (Melville et al., 2004; Ranganathan and Brown, 2006). In other words, IT does not provide value in isolation but rather through the synergies that it creates with other organizational resources (Kohli and Grover, 2008; Nevo and Wade, 2010; Piccoli and Ives, 2005). Ross et al. (1996) identified three key IS resources: the skills and knowledge of the IT staff, the architecture and nature of the technological infrastructure, and the relationship between IT and business. The framework proposed by Ross and her colleagues serves as a conceptual foundation for this study, and is adapted to the open source context to enable us to theorize about the business value of open source infrastructure technologies and its antecedents. Figure 1 presents the conceptual model.

![](/api/attachments/PH3BH68X/fulltext/images/f4b5dac8cae99a1fafce0a6fa942f057f42144fb3132b11f1e8290b435e8f7b8.jpg)  
Figure 1. Conceptual Model

## 2.1.1 Absorptive capacity

According to Ross et al.’s (1996) framework, a competent IT staff, defined as “an IT staff that consistently solves business problems and addresses business opportunities through information technology,” is a key IS resource for an organization that seeks to develop IT-enabled competitiveness. Other researchers have subsequently studied the impact of this human IS resource on organizational performance and concluded that an IT staff with strong technical skills – including knowledge of advanced technologies and competencies in identifying and using emerging technologies and trends – and managerial skills, including project management, coordination, and leadership skills would have the ability to provide efficient and cost-effective IS operations on an ongoing basis (e.g., Bharadwaj, 2000; Wade and Hulland, 2004; Ferratt et al., 2005).

Information technologies often embed new knowledge, making it harder to understand their business value (Dewar and Dutton, 1986), and organizations need to possess the related know-how to be able to apply the technology advantageously (Zahra and George, 2002). Organizations that have accumulated relevant experience and knowledge are more likely to successfully implement new technologies (Fitzgerald and Kenny, 2004; Neo, 1988). In contrast, organizations that perceive a technology as being associated with substantial learning costs are less likely to adopt it (Goode, 2005). Since open source technologies represent a major change in software acquisition, development, and management (Elliott and Scacchi, 2008; Parameswaran and Whinston, 2007), possessing relevant knowledge may be particularly important for realizing benefits from projects involving implementation of these technologies.

Past research has recognized the significance of knowledge barriers and the importance of an existing knowledge base (e.g. Premkumar and Roberts, 1999; Fichman and Kemerer, 1997). However, a firm should not rest on its “knowledge base laurels,” but should be able to effectively use the information it accumulates (Cohen and Levinthal, 1990). Accordingly, Cohen and Levinthal define absorptive capacity as “the ability of a firm to recognize the value of new, external information, assimilate it, and apply it to commercial ends” (p. 128). A similar conceptualization was proposed by Kim (1998) who envisioned absorptive capacity as the ability to learn and solve problems, thus involving both effort and knowledge. A review of the literature on absorptive capacity concludes that this phenomenon is manifested in two modes: potential capacity, which comprises knowledge acquisition and assimilation capabilities; and realized capacity, which centers on knowledge transformation and exploitation (Zahra and George, 2002). Organizations that possess the required specialized expertise – that is, have the ability to exploit the new technology – will be in a superior position to adopt innovative technologies and realize substantial benefits (Cohen and Levinthal, 1990; Fichman and Kemerer, 1997). In particular, the existence of relevant areas of expertise increases the ability of an organization to successfully import external technologies (Rocha, 1997). Thus, the absorptive capacity of the IT staff is an important characteristic of the human IS resource.

Accordingly, we identify the IT staff’s absorptive capacity as a measure of the human IS resource’s skills and knowledge, which can potentially impact the benefits firms realize from their IT investments, open source infrastructure technologies included. Open source infrastructure technologies are typically less user friendly as they are developed for a more technical audience (Andreasen et al., 2006; Levesque, 2004; Porter et al., 2006) and thus lack the comfort zone of commercial technologies (Fitzgerald and Kenny, 2004). In addition, implementing open source technologies requires learning new skills such as accessing the code through the Internet, inspecting it, and making changes to it when necessary (Bonaccorsi et al., 2006). Consistent with this, prior experience with open source software was found to impact the total cost of ownership of new open source software (Ven et al., 2008). Accordingly, absorptive capacity appears to be particularly important for realizing organizational benefits from open source technologies. Hence,

H1: The higher the absorptive capacity of the IT staff for an open source infrastructure technology, the higher the business value of the technology.

## 2.1.2 Infrastructure source openness

The second IS resource identified by Ross et al. (1996) – i.e., the technology infrastructure – consists of shareable platforms and applications, and is essential for integrating systems and building costeffective applications. Organizations with IT infrastructures that consist primarily of closed source technologies are likely to run into difficulties when deploying open source technologies since the former might pose significant barriers to the implementation of the latter (Bonaccorsi et al., 2006; Goode, 2005; Ven et al., 2008). Specifically, IT infrastructures that consist of closed source software can inhibit adoption of open source software (Glynn et al., 2005). This suggests that the extent to which closed source systems are entrenched in an organization could serve as a barometer of how receptive the organization will be to open source technologies, and may influence their potential payback. Thus, it can be argued that the presence of open source technologies in an organization could increase the likelihood of successfully implementing other open source software. The popularity of the LAMP stack (Hu et al., 2008) is a case in point. The LAMP stack is an open source software bundle of operating systems, web servers, databases, and scripting languages. The tendency of organizations to implement a collection of open source technologies which share the same development philosophy and toolsets suggests that there are benefits to be derived from having an open source IT infrastructure. Accordingly, the source openness of the IT infrastructure, which we define as the extent to which the firm’s IT infrastructure is based on open source technologies,<sup>1</sup> can be seen as an assessment of the shared IT asset’s readiness for the technology in question.

Infrastructural compatibility facilitates the assimilation and use of new technologies (Attewell, 1992), but it is the extent of use of the focal technology that ultimately affects performance (Devaraj and Kohli, 2003). Thus, business value is realized only after the newly acquired technology is integrated and attains a certain level of utilization within the organization (Setia et al., 2008). For instance, past research has shown that, for proprietary and commercial technologies, extent of use is related to gains in competitive advantage, improvements in quality outcomes, and increases in revenue (e.g.,

Devaraj and Kohli, 2003; Udo and Davis, 1992). A recent meta-analysis of the IS success literature found that IT’s contribution to organizations is related to its extent of use (Petter et al., 2008).

In summary, we foresee the IT infrastructure’s source openness as an important, albeit indirect, antecedent of business value. Specifically, the source openness of the organization’s IT infrastructure is conceptualized as a key enabler of technology use, the extent of which is expected to positively affect the realization of benefits from investments in open source infrastructure technologies. Consequently,

H2a: The greater the degree of source openness of an organization’s IT infrastructure, the greater the extent of use of the focal open source infrastructure technology.

H2b: The greater the extent of use of the open source infrastructure technology, the greater the business value the technology provides.

## 2.1.3 Open source community ties

The relationship asset suggested by Ross et al. (1996) as the third key IS resource takes a predominantly introspective view (consistent with its underlying theoretical lens, the resource-based view of the firm), and focuses on the relationships of the IT staff with other business units. Since the focal technology in this study is an infrastructure component, its assimilation is expected to be transparent to end-users (Byrd and Turner, 2000; Greis and Kasarda, 1997). Accordingly, we do not foresee a significant role for relationships between the IT staff and other business units within the organization in determining the business value of open source infrastructure technologies. However, the ability to work with, and manage relationships with, stakeholders outside the firm can provide firms with important benefits (Wade and Hulland, 2004). Unlike their proprietary or closed source commercial counterparts, open source technologies are often associated with communities of users and developers who continually modify the code and share valuable information. Given this unique aspect of open source technologies, we propose that ties to these communities can play an important role in the realization of business value. Building on Cohen and Levinthal (1990), we propose that participation in open source communities may be a mechanism that serves to integrate external sources of knowledge that may not reside within the organization. We expand on this notion by drawing on the communities-of-practice literature.

Originally developed to explain differences between expected and actual learning, work and innovation processes within bureaucratic, hierarchical and structured organizations, the communitiesof-practice literature (Brown and Duguid, 1991; Lave and Wenger, 1991) has been expanded to consider communities that transcend geographical and organizational boundaries (Brown and Duguid, 2001; Vaast and Walsham, 2009). According to this perspective, communities-of-practice consist of individuals who share interests or vocational responsibilities and self-organize, self-select, and organically form and maintain their communities.

Several questions may be used to distinguish between communities-of-practice and other collectives such as project teams and formal workgroups: (1) What is the purpose? (2) Who belongs? (3) What holds it together? (4) How long does it last? Wenger and Snyder (2000) noted that in the case of communities-of-practice the answers to these questions are often: (1) to develop members capabilities and to build and exchange knowledge, (2) members who select themselves, (3) passion, commitment, and identification with the group’s expertise, and (4) as long as there is interest in maintaining the group. Open source communities exhibit many of the hallmarks of communities-ofpractice: “Individuals initiate projects... Anyone can participate from anywhere in the world... Labor is mostly self-selected volunteers... Project will continue as long as there is interest… Ideas emerge from a diverse pool of distributed contributors...” (O’Mahoney and Bechky, 2008: 428). And “Using communication technologies, participants in FOSS can jointly create advanced software solutions, and new developments are shared in a collective manner within communities…” (Dahlander and Magnusson, 2008: 629). Also, in “OSS development… the project administrator does not have formal control over the behavior of the developers, and thus their voluntary contribution and performance depends on self-initiatives” (Xu et al., 2009). In addition, Feller et al. (2008) observed that open source communities emphasize interaction, communication, and collaboration activities and operate under agreed-upon norms. These observations suggest that open source communities fit the expanded conceptualization of communities-of-practice (Whelan, 2007).

The communities-of-practice literature recognizes the importance of knowledge and expertise sources that reside outside the organization’s boundaries and can potentially complement internal know-how. According to this perspective, while knowledge is a key resource for organizations, no single organization can possess all the knowledge it requires and must, therefore, search outside its boundaries (Wasko and Faraj, 2005; Whelan, 2007). Prior research has reported that forming and maintaining ties with communities-of-practice provides access to knowledge sources that reside outside the firm’s formal boundaries (Cohen and Levinthal, 1990; Garud and Kumaraswamy, 2005; Tushman 1977). In turn, this knowledge is a key enabler for cost reduction, innovation, and competitiveness (Brown and Duguid, 1991, 2001; Teigland and Wasko, 2003; Wasko and Teigland, 2004). Specifically, as organizations gain experience and knowledge related to the new skill base, they also develop superior capabilities (Teece et al., 1997) and improve their ability to capitalize on emerging opportunities (Raff, 2000).

Thus, we surmise that involvement with open source communities-of-practice can provide organizations that adopt open source infrastructure technologies with important benefits. Accordingly, we expect that firms with stronger ties to the relevant open source community-of-practice will realize greater benefits from the open source technology since those firms will be able to: (1) have source code modifications supported in subsequent versions, (2) leverage their ties to customize the technology to better match its unique needs by getting help from the community, (3) get help to identify and fix bugs, and (4) compensate for lacking or inadequate in-house knowledge. Ties to open source communities-of-practice may enable co-creation of value, whereby in-house IT staff and external users and developers work jointly to maximize benefits from the same technology. Furthermore, involvement with the developer/user community can provide an opportunity to increase the ability to innovate with and customize the technology (Brydon and Vining, 2008). We note that while different organizations may form relationships with the same open source community, they are nevertheless expected to differ in their ability to forge and sustain their ties and leverage them to implement, use, maintain, and customize the technology. Hence,

H3: The stronger the relationships with the open source community-of-practice, the greater the business value garnered through implementing an open source infrastructure technology.

## 3. Research method

## 3.1 Data collection

FLOSS has broadened its scope from operating systems to other infrastructure systems such as Web servers and databases (Ajila and Wu, 2007; Bruce et al., 2006). As the backbone of operational processes in organizations, databases are a critical component of the IT infrastructure (Armstrong and Sambamurthy, 1999; Bharadwaj, 2000; Zhu and Kraemer, 2005; Weill and Vitale, 2002). Databases form the basis for decision support processes and serve as knowledge repositories for organizational know-how (Gregor and Jones, 2007; Zhang and Zhao, 2006). Consequently, databases are key enabling technologies when organizations conceive of and implement business strategies (Subramani, 2004; Tam and Ho, 2005). We submit that given the centrality of databases to organizations’ routine and non-routine processes, major innovations in this IT arena (e.g., open sourcing) should be closely examined.

The open source database MySQL was chosen as an instance of open source infrastructure technology for the following reasons. First, MySQL has a large community of users and developers who interact and communicate via mailing lists and other forums. Second, this community provides support for the product by sharing experiences and discussing and solving problems. Thus it is an exemplar of an active community-of-practice. Third, community members are encouraged to submit bug reports and code patches, allowing for a free exchange of knowledge.

Given the focus of this paper on the business value of open source infrastructure technologies, existing users of MySQL were targeted as informed participants. Accordingly, invitations to participate in a survey were sent to members of an online community for professionals involved in the development, implementation, maintenance, or management of MySQL. There are no costs associated with joining the community and participation is voluntary. Members of the MySQL community-of-practice represent myriad companies in various industries, as is evident from their profiles. A personal invitation (Dillman, 1999) to participate in the study was sent by email to 898 randomly chosen members of the community (out of more than 3,000 members). In exchange for participation in the study, respondents were offered a report of the findings. 162 completed questionnaires were received, representing an 18% response rate. After removing questionnaires with missing values, a final dataset of 149 was obtained. The median number of employees was 64 and, on average, participating organizations have been using MySQL for 5 years. The median number of individuals managing, administering, and directly using the database in any given organization was 4.

To ensure that survey respondents were appropriate for this study we prominently displayed the following text on the first page: Please answer this survey only if (1) your company has implemented MySQL, and (2) you were involved with its implementation, maintenance, use, or management.

## 3.2 Instrument development

Five constructs were used in this study to allow us to test the above hypotheses: business value of an open source infrastructure technology, absorptive capacity for the open source technology, the IT infrastructure’s source openness, the extent of use of the open source technology, and ties to the open source technology’s community-of-practice. In order to account for potential rival hypotheses, we controlled for the overall size of the organization, as well as for the number of employees directly involved with the administration, management, and use of MySQL. To measure absorptive capacity, the scale developed by Szulanski (1996) was adopted and minimally modified to reflect the fact that the object to be absorbed is an open source infrastructure technology. Source openness of the IT infrastructure was assessed by asking respondents to indicate the extent to which their company’s IT infrastructure consisted of open source technologies. Respondents answered this question by selecting a number between 1 (Completely closed source) and 7 (Completely open source).<sup>2</sup> We could not identify valid and reliable scales for community ties, extent of use,<sup>3</sup> and the business value constructs, and as a result developed original scales for the purpose of this study. Despite this paucity, the scale developed by Cadiz et al. (2009) to measure how individuals experience their communities was deemed useful as a starting point for developing candidate items for the community ties scale employed in this study. Additional items for the community ties scale were generated based on the authors’ familiarity with open source communities and the nature of relationships between users/developers and those communities. Items for the business value scale were developed based on an analysis of the open source and the business value of IT literatures (see Appendix A). Finally, the extent of use construct was operationalized using the facets of usage proposed by Massetti and Zmud (1996). All items are presented in Appendix B.

## 3.3 Assessment of common method bias

A concern with self-reported data is the possible presence of a systematic error. To reduce the effects of social desirability, the survey participants were assured of the confidentiality of their responses. In order to assess whether common method bias was a concern, the Harmon one-factor test was conducted by entering all independent and dependent variables in an exploratory factor analysis (EFA) (Podsakoff et al., 2003). The first factor accounted for less than 50% of the total variance, indicating a lack of a substantial common methods bias.

## 3.4 Measurement validation

Since new scales were developed or adapted for this study, an assessment of the psychometric properties of the scales was conducted first via an EFA using SPSS Statistics 17.0. The EFA indicated the unidimensionality of the instrument’s scales. Bivariate correlations among all items revealed strong correlations between one of the items of absorptive capacity and several of the items of extent of use. This item was removed from the model and not used in further analysis. Next, we observed the statistics associated with the measurement model following confirmatory factor analysis using PLS (SmartPLS v.2.0.M3). This structural equation modeling technique was chosen for its ability to handle non-normality in the data and measures that are not well established, and because the goal of this study is to explain variance in the outcome variable (Gefen et al., 2000). A one-sample Kolmogorov-Smirnov test revealed that absorptive capacity, extent of use, and infrastructure source openness did not follow a normal distribution. PLS was also appropriate for the present study since it can handle both reflective and formative scales, both of which are included in the model. Specifically, the business value construct was modeled as formative on the premise that, for example, efficiency and innovativeness are independent of each other and are not interchangeable.

To assess the scales’ psychometric properties, several tests were conducted. We describe those tests next, beginning with the reflective scales and then discussing the formative scale.

## 3.4.1 Convergent validity

Convergent validity is an assessment of the agreement among measures of the same construct (Bagozzi et al., 1991). Hence, high levels of convergent validity indicate that the items reflect the same latent variable. Two tests were used to assess convergent validity. Convergent validity was first assessed by observing the loadings of the items. According to Comrey (1973), items with loadings greater than .70 indicate acceptable convergent validity. All but one item had loadings in excess of .70 (Table 1), demonstrating the instrument’s convergent validity. Convergent validity was also assessed by observing the square root of the average variance extracted (diagonal elements in Table 2). A minimum level of .70 is suggested (Fornell and Larcker, 1981; Gefen and Straub, 2005), since it indicates that, on average, the construct accounts for at least 50% of its measures’ variance. All our scales met this criterion, indicating satisfactory convergent validity.

Table 1: Confirmatory Factor Analysis

<table><tr><td></td><td>Absorptive Capacity</td><td>Community Ties</td><td>Extent of Use</td></tr><tr><td>Absorptive Capacity 1</td><td>.817</td><td>.069</td><td>.327</td></tr><tr><td>Absorptive Capacity 2</td><td>.830</td><td>.182</td><td>.344</td></tr><tr><td>Absorptive Capacity 3</td><td>.658</td><td>.076</td><td>.232</td></tr><tr><td>Absorptive Capacity 4</td><td>.810</td><td>.136</td><td>.356</td></tr><tr><td>Absorptive Capacity 5</td><td>.756</td><td>.097</td><td>.302</td></tr><tr><td>Community Ties 1</td><td>.197</td><td>.853</td><td>.260</td></tr><tr><td>Community Ties 2</td><td>.081</td><td>.878</td><td>.175</td></tr><tr><td>Community Ties 3</td><td>.153</td><td>.867</td><td>.183</td></tr><tr><td>Community Ties 4</td><td>.079</td><td>.797</td><td>.212</td></tr><tr><td>Community Ties 5</td><td>.083</td><td>.836</td><td>.152</td></tr><tr><td>Extent of Use 1</td><td>.403</td><td>.211</td><td>.885</td></tr><tr><td>Extent of Use 2</td><td>.362</td><td>.166</td><td>.913</td></tr><tr><td>Extent of Use 3</td><td>.335</td><td>.268</td><td>.899</td></tr></table>

<table><tr><td>Construct</td><td>Min</td><td>Max</td><td>Mean</td><td>S.D.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>C.R.</td></tr><tr><td> $1.Absorptive Capacity^4$ </td><td>1.000</td><td>7.000</td><td>5.699</td><td>1.106</td><td>.775</td><td></td><td></td><td></td><td>.882</td></tr><tr><td> $2.Community Ties^3$ </td><td>1.000</td><td>7.000</td><td>3.093</td><td>1.509</td><td>.146</td><td>.846</td><td></td><td></td><td>.926</td></tr><tr><td> $3.Extent of Use^5$ </td><td>1.000</td><td>9.000</td><td>6.773</td><td>1.995</td><td>.407</td><td>.238</td><td>.898</td><td></td><td>.927</td></tr><tr><td> $4.Infrastructure Source Openness^6$ </td><td>2.000</td><td>7.000</td><td>4.399</td><td>2.063</td><td>.241</td><td>.136</td><td>.345</td><td>-</td><td>-</td></tr></table>

Diagonal elements are the square roots of the average variance extracted (AVE) between the constructs and their respective measures. Off-diagonal elements are correlations between constructs.

## 3.4.2 Discriminant validity

Discriminant validity indicates that the items measure only the construct for which they were created and not other constructs in the model (Salisbury et al., 2002). To assess the instrument’s discriminant validity, we conducted two tests. Evidence of discriminant validity is obtained when the square root of the average variance shared between a construct’s measures (diagonal elements in Table 2) is larger than the correlations between the construct and other constructs (off-diagonal elements) in the model. All scales met this criterion (Fornell and Larcker, 1981) suggesting good discriminant validity. Another way to assess discriminant validity is by observing the difference between the loadings and the crossloadings. An acceptable difference is .10 (Wixom and Todd, 2005). None of the differences in our study was lower than this cut-off (Table 1).

## 3.4.3 Construct reliability

Composite reliability (C.R.) scores (see Table 2) are used as an indication of the scale’s reliability. All scales met the .70 cut-off suggested by Hair et al. (2009), indicating that results based on these scales should be consistent.

## 3.4.4 Formative scale

Since individual items in formative scales need not correlate, it is inappropriate to subject them to the same reliability tests as reflective scales (Petter et al., 2007). Instead, an indication of item-to-scale importance may be assessed by observing the items’ weights (Chin, 1998). We followed the process proposed by Diamantopoulos and Winklhofer (2001) and removed non-significant items. Specifically, we progressed iteratively, identifying the item with the lowest t-value and excluding it from further analysis. After three iteration, three items exhibited weights which were significant at α = .01 or better and were retained for further analysis (see Appendix B).

Based on these tests, we conclude that the scales are valid and reliable, providing confidence to proceed to hypothesis testing and to assess the overall model fit by examining the structural model.

## 3.5 Structural model

The structural model of the PLS regression (SmartPLS 2.0.M3) was used to test the hypotheses and assessing the predictive power of the model. A bootstrapping procedure (500 samples) was used to assess the significance of the hypothesized paths and the amount of variance in the dependent variables attributed to the explanatory variables (Chin, 1998). The results of the analysis are presented in Figure 2. The path coefficients are summarized in Table 3.

<table><tr><td colspan="6">Table 3: Path Coefficients</td></tr><tr><td>Hypothesis</td><td>From</td><td>To</td><td>β</td><td>Sig. level</td><td>Hypothesis Supported?</td></tr><tr><td>H1</td><td>Absorptive Capacity</td><td>Business Value</td><td>.229</td><td>.01</td><td>Yes</td></tr><tr><td>H2a</td><td>Infra. Source Openness</td><td>Extent of Use</td><td>.345</td><td>.01</td><td>Yes</td></tr><tr><td>H2b</td><td>Extent of Use</td><td>Business Value</td><td>.130</td><td>.01</td><td>Yes</td></tr><tr><td>H3</td><td>Community Ties</td><td>Business Value</td><td>.262</td><td>.01</td><td>Yes</td></tr></table>

![](/api/attachments/PH3BH68X/fulltext/images/6f9a624e780e02aa6df297c34a5557148e21d271df934ee7c72347a34db35ee1.jpg)  
Figure 2. Structural Model

## 3.6 Findings

The results from the structural model generated by PLS support our key arguments for the antecedents of the business value of open source infrastructure technologies. We found empirical support for the hypothesized relationship between the IT staff’s absorptive capacity for an open source technology and the business value obtained from the technology (Hypothesis 1). We also found support for the hypothesized relationship between the IT staff’s ties to the open source technology’s user/developer community and the technology’s business value (Hypothesis 3). Finally, we found support for the hypothesized relationship between the source openness of the IT infrastructure, extent of use, and the business value of the open source infrastructure technology (Hypotheses 2a and 2b). In sum, absorptive capacity for the database, ties with the technology’s user/developer community-of-practice, and an open source IT infrastructure that facilitates MySQL utilization explain about 20 per cent of the business value of the open source technology.

## 4. Discussion

The business value of proprietary and commercial software, including supply chain (e.g., Setia et al., 2008) and e-commerce applications (e.g., Zhu et al., 2006), has been actively examined from the point of view of various constituents. In contrast, the organizational benefits of open source technologies have been examined to a lesser extent, typically from the perspective of software companies that commercialize the software by providing service and support for open source solutions (e.g., West, 2005; Bonaccorsi and Rossi, 2006). Although this kind of revenue generation is clearly a central issue for software manufacturers, it represents but a small component of open source technologies’ business value. In particular, our knowledge of the business value of open source technologies is lacking regarding the organizational benefits derived by organizations that are consumers of such technologies.

There has been little research on the organizational benefits obtained via deployment of open source infrastructure technologies, and the business value focus in related studies often dwindles to savings derived from the lower total cost of ownership relative to proprietary solutions. For example, a recent study of open enterprise systems (Lee et al., 2009) touts the cost-effectiveness of open source ERP systems relative to established proprietary solutions, and another study of open source server-based computing (Niemi et al., 2009) found that it reduced the total cost of ownership by about one half. Those studies clearly contribute to our understanding of the organizational benefits of open source technologies. However, business value is a rich and multi-faceted construct (Kohli and Grover, 2008; Melville et al., 2004) and we have attempted to take a similarly broad view of it in this study. The maturation of open source databases offers new value creation opportunities for organizations, not just through cost savings but also in terms of efficiency, innovativeness, and productivity. Consequently, we cast a wide net to capture different aspects of business value in our study.

In order to realize these potential benefits, organizations must have the necessary human capital in place. Our analysis indicates that absorptive capacity for the open source infrastructure technology had a strong impact on business value in our study. Not only did organizations require certain technical abilities to implement MySQL, but the management of the implementation process was also crucial to realizing business value. Having a strategy in place for the use of the technology, or at the very least, a vision of what the focal technology is intended to accomplish, as well as efforts in assigning roles and responsibilities during implementation, and towards facilitating the absorption of this technology into existing business processes reflect the organization’s capacity to turn potential benefits into realized business value. These findings are consistent with the human capital view advanced by Melville et al. (2004) which emphasizes the balance between the technical skill set within an organization and the managerial activities of planning and coordination. These characteristics may play a more prominent role in the context of open source technologies since the availability of the source code provides the potential for increased technical advances while the licensing arrangements and source code inspection and modification possibilities offer new managerial challenges.

As hypothesized, the source openness of the existing IT infrastructure was a significant enabler of MySQL utilization. This finding is consistent with reports that organizations with closed source IT infrastructures perceive the implementation of open source technologies to be risky and prone to failure (e.g., Glynn et al., 2005; Goode, 2005). It is also in line with studies which found that prior experience with open source technologies allays concerns about hidden costs and adverse outcomes, which typically inhibit organizations from implementing open source technologies (e.g., Goode, 2005). In sum, we find that fewer technological hurdles to implementation of open source infrastructure technology encourages a smoother assimilation process, ultimately resulting in greater use of the technology.

Building on Devaraj and Kohli (2003), we considered extent of use to be an important antecedent of IT value creation and our results bear this out. Organizations in which MySQL was used to a greater extent (say, for supporting most business processes) were, on average, more successful in extracting business value from the technology. This confirms other studies on business value which maintain that any newly acquired technology has to be integrated with current processes and attain a certain level of assimilation and use if it is expected to provide business value (Setia et al., 2008). Thus, this study finds that, in the context of open source infrastructure technologies, the source openness of the IT infrastructure positively impacts the technology’s utilization, which in turn determines the realization of organizational benefits.

An emerging aspect of the BVIT is the co-creation of IT value (Kohli and Grover, 2008). Value cocreation is seen as a form of collaboration between organizations and their customers, whereby the skills and resources of the former are combined with the latter’s product knowledge, and results in more compelling value propositions for customers as well as a competitive advantage for the organization (Kohli and Grover, 2008; Romero and Molina, 2009). In the context of open source technologies, the findings of this study suggest that organizations and the open source community have the opportunity to co-create value by allowing the former to better configure the software and align it with their own applications. Specifically, the study examined the ties that organizations had with the MySQL community and found that those that sought out the knowledge and expertise of the community for troubleshooting and customization were more likely to realize greater business value from the technology. We note that it is not the mere ties to the community that impact an open source technology’s business value but rather the ability to leverage those ties to enhance and complement in-house knowledge. Therefore, the value of the open source community as a knowledge resource as well as a source of frequent updates and product releases appears to be real and directly related to business value realization.

## 4.1 Caveat emptor

We propose that community ties are better seen as a two-way street rather than a one-way alley in that the open source community would likely expect organizations to reciprocate by returning value to the community. For example, providing their own experiences with the open source technology and knowledge gained via assimilation and usage would likely help organizations to sustain and strengthen their community ties. The results of our study provide some evidence in support of the benefits of such reciprocity, in line with Kohli and Grover’s (2008) emphasis on symbiotic relationships and value co-creation. The open source literature (e.g., Fitzgerald and Kenny, 2004) and the communities-of-practice literature (e.g., Wasko and Teigland, 2004) also support the two-way street perspective of community ties.

In sum, to enhance the realization of business value from open source infrastructure technologies, organizations should promote technical and managerial accumulation of relevant knowledge that will be key to the absorption of the technologies. Organizations should also encourage the establishment of ties with the open source community and the maintenance of those ties, especially when in-house knowledge is lacking. It is important to note that strong ties are likely to require reciprocity – that is, organizations will be expected to contribute code back to the community and avoid being seen as free riders (AlMarzouq et al., 2005; Nelson et al., 2006). Finally, organizations should consider their existing IT infrastructure and recognize that its extent of source openness could impact FLOSS-based benefits by enabling or hindering the utilization of the technology.

## 5. Limitations and future research

This paper examined the business value gained through open source infrastructure technologies and its key antecedents. While the paper offers several important contributions to research and practice, there are a number of opportunities to improve upon and extend this study in future research. A limitation of our study is the use of key informants who directly administer, manage, and use the focal open source technology; future research may seek to incorporate additional objective measures to assess the robustness of our findings. Although our model of business value treats the drivers of business value as exogenous variables, it could be argued that absorptive capacity and community ties may form a virtuous cycle, whereby increased knowledge about, and experience with, open source infrastructure technologies within the organization leads to more meaningful interactions with the open source community, which in turn results in improved technical skills of the IT staff, encouraging more sophisticated interactions with the community. This kind of feedback loop can be modeled and investigated in future studies by taking a longitudinal approach to data collection.

Consistent with the objectives of this paper, all the organizations in our study had already implemented MySQL and our study adopted the perspective of FLOSS consumers. Questions that would be of interest to FLOSS producers may be related to expected benefits, e.g. is organizations expected business value similar to perceived usefulness and relative advantage in individual adoption decisions? This would require studying organizations that have not yet acquired an open source infrastructure technology. Also, it would be interesting to examine what factors, if any, might cause a discrepancy between expected and realized business value and what can be done to eliminate those discrepancies.

Finally, there could be resistance to the implementation of open source technologies within the adopting organizations. For instance, IT staff might fear losing their experience with commercial packages or proprietary systems, and thus being deskilled (Fitzgerald and Kenny, 2004). Alternatively, the open source technology may not be mature enough to provide business value. Our study focused on a relatively mature open source technology, however future research may be able to assess the impact, if such impact exists, of the technology’s maturity on business value. For example, the open source databases MySQL and PostgreSQL could be used to examine differences in terms of the impact of standardization or the relative size of the respective open source community. Such factors, whether organizational or technical, that could add to or detract from business value should be examined. Additionally, studies that investigate continued use of open source technologies may help us develop more nuanced views of the BVIT landscape.

## 6. Conclusion

The emergence of open source infrastructure technologies creates new opportunities for organizations, not just in tangible terms such as cost savings and reliability but also in intangible terms such as innovation and flexibility. Our study fills a gap in the BVIT and open source literatures by explicating the kind of business value that can be extracted through the use of such technologies and the organizational drivers that need to be in place to realize said business value. First, extracting organizational benefits from open source technologies involves technical and managerial abilities to explore and exploit the technology effectively. Second, our study shows that strong ties with the open source community can be translated to substantial gains in business value when those ties are maintained, leveraged, and reciprocated. Third, compatibility of the open source technology with the existing technology infrastructure creates an environment that promotes use of the technology and increases the opportunity for realizing business value.

## References

Agarwal, R. and Lucas, H.C. Jr. 2005. The Information Systems Identity Crisis: Focusing on High-Visibility and High-Impact Research. MIS Quarterly 29(3):381-398.

Ajila, S.A. and Wu, D. 2007. Empirical Study of the Effects of Open Source Adoption on Software Development Economics. Journal of Systems and Software 80(9):1517-29.

AlMarzouq, M., Zheng, L., Rong, G. and Grover, V.. 2005. Open Source: Concepts, Benefits, and Challenges. Communications of the Association for Information Systems 16:756-784.

Andreasen M.S., Nielsen, H.V., Schrøder, S.O. and Stage, J. 2006. Usability in Open Source Software Development: Opinions and Practice. Information Technology and Control 35(3):303- 312.

Armstrong, C.P. and Sambamurthy, V. 1999. Information Technology Assimilation in Firms: The Influence of Senior Leadership and IT Infra- structures. Information Systems Research 10(4):304- 327.

Attewell, P. 1992. Technology Diffusion and Organizational Learning: The Case of Business Computing. Organization Science 3(1):1-19.

Bagozzi, R.P., Yi, Y. and Phillips, L.W. 1991. Assessing Construct Validity in Organizational Research. Administrative Science Quarterly 36(3):421-448.

Bayrak, T. and Grabowski, M.R. 2006. Network Performance Impacts on Operators in Safety-critical Systems. International Journal of Information Technology and Decision Making 5(1):173-194

Benaroch, M. 2002. Managing Information Technology Investment Risk: A Real Options Perspective. Journal of MIS 19(2): 43-84

Bharadwaj, A.S. 2000. An Organizational Resource-based Perspective on Information Technology Capability and Firm Performance: An Empirical Investigation. MIS Quarterly 24(1):169-196.

Bloor, R. 2005. So Much Database, So Little Money: MySQL Plays Ball with the Majors. Hurwitz Associates. Accessible online at http://www.mysql.com/why-mysql/analyst-reports/hurwitzvantage-point.php

Bonaccorsi, A., Giannangeli, S. and Rossi, C. 2006. Entry Strategies Under Competing Standards: Hybrid Business Models in the Open Source Software Industry. Management Science 52(7):1085-1098.

Bonaccorsi, A. and Rossi, C. 2006. Comparing Motivations of Individual Programmers and Firms to Take Part in the Open Source Movement: From Community to Business. Knowledge, Technology. & Policy 18(4):40-64.

Boomen, M. and Schäfer, M.T. 2005. Will the Revolution be Open-sourced? How Open Source Travels through Society. In M. Wynants and J. Cornelis (eds.), How Open is the Future? Economic, Social & Cultural Scenarios Inspired by Free & Open-Source Software. Brussels: VUB Brussels University Press, pp 31–67.

Brown, J.S. and Duguid, P. 1991. Organizational Learning and Communities-of-Practice: Toward a Unified View of Working, Learning, and Innovation. Organization Science 2(1):40-57.

Brown, J.S. and Duguid, P. 2001. Knowledge and Organization: A Social-practice Perspective. Organization Science 12(2):198–213

Bruce, G., Robson, P. and Spaven, R. 2006. OSS Opportunities in Open Source Software: CRM and OSS Standards. BT Technology Journal 24(1):127-40.

Brydon, M. and Vining, A.R. 2008. Adoption, Improvement, and Disruption: Predicting the Impact of Open Source Applications in Enterprise Software Markets. Journal of Database Management 19: 73-94.

Byrd, T.A. and Turner, D.E. 2000. Measuring the Flexibility of Information Technology Infrastructure: Exploratory Analysis of a Construct. Journal of Management Information Systems 17(1):167-208.

Cadiz, D., Sawyer, J.E. and Griffith, T.L. 2009. Developing and Validating Field Measurement Scales for Absorptive Capacity and Experienced Community of Practice. Educational and Psychological Measurement 69(6):1035-1058.

Casadesus-Masanell, R. and Ghemawat, P. 2006. Dynamic Mixed Duopoly: A Model Motivated by Linux vs. Windows. Management Science 52(7):1072-1084.

Chin, W.W. 1998. Issues and Opinion on Structural Equation Modeling MIS Quarterly 22(1):vii-xvi.

Cohen, W.M. and Levinthal, D.A. 1990. Absorptive Capacity: A New Perspective on Learning and Innovation. Administrative Science Quarterly 35(1):128-153.

Comrey, A. 1973. A First Course on Factor Analysis. London: Academic Press.

Dahlander, L. and Magnusson, M. 2008. How Do Firms Make Use of Open Source Communities? Long Range Planning 41:629-649.

Dai, Q., Kauffman, R.J. and March, S.T. 2005. Valuing Information Technology Infrastructures: A Growth Options Approach. Information Technology and Management 8(1):1-17.

Devaraj, S., and Kohli, R. 2003. Performance Impacts of Information Technology: Is Actual Usage the Missing Link. Management Science (49:3):273-289.

Dewar, R.D. and Dutton, J.E. 1986. The Adoption of Radical and Incremental Innovations: An Experimental Analysis. Management Science 32:1422-1433.

Diamantopoulos, A. and Winklhofer, H.M. 2001. Index Construction with Formative Indicators: An Alternative to Scale Development. Journal of Marketing Research 38:259-277.

Dillman, D.A. 1999.Mail and Internet Surveys: The Tailored Design Method. New York: John Wiley Company.

Economides, N. and Katsamakas, E. 2006. Two-sided Competition of Proprietary vs. Open Source Technology Platforms and the Implications for the Software Industry. Management Science 52(7):1057-71.

Elliott, M.S. and Scacchi, W. 2008. Mobilization of Software Developers: The Free Software Movement. Information Technology & People 21(1):4-33.

Feller, J., Finnegan, P., Fitzgerald, B. and Hayes, J. 2008. From Peer Production to Productization: A Study of Socially Enabled Business Exchanges in Open Source Service Networks. Information Systems Research 19(4):475-493.

Ferratt, T.W., Agarwal, R., Brown, C.V. and Moore, J.E. 2005. IT Human Resource Management Configurations and IT Turnover: Theoretical Synthesis and Empirical Analysis. Information Systems Research (16)3:237-255.

Fichman, R.G. and Kemerer, C.F. 1997. The Assimilation of Software Process Innovations: An Organizational Learning Perspective. Management Science 43(10):1345-1363.

Fink, L. and Neumann, S. 2009. Exploring the Perceived Business Value of the Flexibility Enabled by Information Technology Infrastructure. Information & Management 46:90-99.

Fitzgerald, B. 2006. The Transformation of Open Source Software. MIS Quarterly 30(3):587-598.

Fitzgerald, B. and Kenny, T. 2004. Developing an Information Systems Infrastructure with Open Source Software. IEEE Software 21(1):50-57.

Fornell, C. and Larcker, D.F. 1981. Evaluating Structural Equation Models with Unobservable Variables and Measurement Error: Algebra and Statistics. Journal of Marketing research 18(3):382-388.

Garrison, G. 2009. An Assessment of Organizational Size and Sense and Response Capability on the Early Adoption of Disruptive Technology. Computers in Human Behavior 25:444-449.

Garud, R. and Kumaraswamy, A. 2005. Vicious and Virtuous Circles in the Management of Knowledge: The Case of Infosys Technologies. MIS Quarterly 29(1):9-33.

Gefen, D., Straub, D. and Boudreau, M.-C. 2000. Structural Equation Modeling and Regression: Guidelines for Research Practice. Communications of the Association for Information Systems 4 Article 7.

Gefen, D and Straub, D. 2005. A Practical Guide to Factorial Validity Using PLS-graph: Tutorial and Annotated Example. Communications of the Association for Information Systems 16(5):91-109.

Glynn, E., Fitzgerald, B. and Exton, C. 2005. Commercial Adoption of Open Source Software: An Empirical Study. International Symposium on Empirical Software Engineering, ISESE 2005: 225- 234

Goode, S. 2005. Something for Nothing: Management Rejection of Open Source Software in Australia’s Top Firms. Information & Management 42(5):669-81.

Gray, P. and Hovav, A.Z. 2007. The IS Organization of the Future: Four Scenarios for 2020. Information Systems Management 24(2):113-120.

Gregor, S., and Jones, D. 2007. The Anatomy of a Design Theory. Journal of the Association for Information Systems 8(5):312-334.

Greis, N.P. and Kasarda, J.D., 1997. Enterprise Logistics in the Information Age. California Management Review 39(3):55–78.

Hair, J.F., Black, W.C., Babin, B.J. and Anderson, R.E. 2009. Multivariate Data Analysis (7th ed.). Upper Saddle River, NJ: Prentice Hall.

Hoving, R. 2007. Information Technology Leadership Challenges: Past, Present, and Future. Information Systems Management 24(2):147-153.

Hu, W., Yang, C. T., Yeh, J. and Hu, W. 2008. Mobile and Electronic Commerce Systems and Technologies. Journal of Electronic Commerce in Organizations 6(3):54-74.

Kim, L. 1998. Crisis Construction and Organizational Learning: Capability Building in Catching-Up at Hyundai Motor. Organization Science 9:506-521.

Kohli, R. and Grover, V. 2008. Business Value of IT: An Essay on Expanding Research Directions to Keep up with the Times. Journal of the Association for Information Systems 9(1):23-37.

Kshetri, N. 2004. Economics of Linux Adoption in Developing Countries. IEEE Software 21(1):74-81.

Lave, J. and Wenger, E. 1991. Situated Learning: Legitimate Peripheral Participation. New York: Cambridge University Press.

Lee, S.M., Olson, D.L. and Lee, S. H. 2009. Open Process and Open-source Enterprise Systems. Enterprise Information Systems 3(2): 201-209.

Levesque, M. 2004. Fundamental Issues with Open Source Software Development. First Monday 9(4).

Lin, W.T. and Shao, B.B.M. 2006. The Business Value of Information Technology and Inputs Substitution: The Productivity Paradox Revisited. Decision Support Systems 42(2):493-507.

Lind, M.R. and Zmud, R.W. 1991. The Influence of a Convergence in Understanding between Technology Providers and Users on Information Technology Innovativeness. Organization Science (2)2:195-217.

Massetti, B. and Zmud, R. W. 1996. Measuring the Extent of EDI Usage in Complex Organizations: Strategies and Illustrative Examples. MIS Quarterly 20(3):331-345

Melville, N., Kraemer, K. and Gurbaxani, V. 2004. Information Technology and Organizational Performance: An Integrative Model of IT Business Value. MIS Quarterly 28(2):283-322.

Mishra, A.N., Konana, P. and Anitesh Barua, A. 2007. Antecedents and Consequences of Internet Use in Procurement: An Empirical Investigation of U.S. Manufacturing Firms. Information Systems Research 18(1):103-122.

Mukhopadhyay, T., Kekre, S. and Kalathur, S. 1995. Business Value of Information Technology: A Study of Electronic Data Interchange. MIS Quarterly 19(2):137-156.

Mukhopadhyay, T., Surendra, R. and Srinivasan, K. 1997. Information Technology Impact on Process Output and Quality. Management Science 43(12):1645-1659.

Nelson, M., Sen, R. and Subramaniam, C. 2006. Understanding Open Source Software: A Research Framework. Communications of the Association for Information Systems 17:266-287.

Neo, B.S., 1988. Factors Facilitating the Use of Information Technology for Competitive Advantage: An Exploratory Study. Information and Management 15:191–201.

Nevo, S. and Wade, M.R. 2010. The Formation and Value of IT-Enabled Resources: Antecedents and Consequences of Synergistic Relationships. MIS Quarterly 34(1):163-183.

Norris, J. 2004 Mission-Critical Development with Open Source Software: Lessons Learned. IEEE Software 21(1):42-49.

Niemi, T., Tuisku, M., Hameri, A. and Curtain, T. 2009. Server-based Computing Solution Based on Open Source Software. Information Systems Management 26(1):77-86.

O’Mahoney, S. and Bechky, B.A. 2008. Boundary Organizations: Enabling Collaboration among Unexpected Allies. Administrative Science Quarterly 53(3):422-459.

Parameswaran, M. and Whinston, A. B. 2007. Social Computing: An Overview. Communications of the Association for Information Systems 19:762-780.

Petter, S.; Straub, D.W.; and Rai, 2007. A. Specification and validation of formative constructs in IS research. MIS Quarterly, 31, 4, pp. 623–656.

Petter, S., DeLone, W. and McLean, E. 2008. Measuring Information Systems Success: Models, Dimensions, Measures, and Interrelationships. European Journal of Information Systems 17:36- 263.

Parthasarathy, M. and Bhattacherjee, A. 1998 Understanding Post-Adoption Behavior in the Context of Online Services. Information Systems Research (9:4):362-379.

Piccoli, G. and Ives, B. 2005. Review: IT-dependent Strategic Initiatives and Sustained Competitive Advantage: A Review and Synthesis of the Literature. MIS Quarterly 29(4):747-776.

Podsakoff, P., MacKenzie, S., Lee, J. and Podsakoff, N. 2003. Common Method Biases in Behavioral Research: A Critical Review of the Literature and Recommended Remedies. Journal of Applied

Psychology 88:879-903.

Porter, A.A., Yilmaz, C., Memon, A. M., Krishna, A. S., Schmidt, D.C. and Gokhale, A. 2006. Techniques and Processes for Improving the Quality and Performance of Open-Source Software. Software Process-Improvement and Practice 11(2):163-176.

Premkumar, G. and Roberts, M. 1999. Adoption of New Information Technologies in Rural Small Businesses. Omega-International Journal of Management Science 27(4):467-484.

Raff, D.M. 2000. Superstores and the Evolution of Firm Capabilities in American Bookselling. Strategic Management Journal 21:1043-1060.

Ranganathan, C. and Brown, C.V. 2006. ERP Investments and the Market Value of Firms: Toward an Understanding of Influential ERP Project Variables. Information Systems Research 17(2):145-161.

Rao, H.R., Pegels, C.C., Salam, A.F., Hwang, T. and Seth, V. 1995. The Impact of EDI Implementation Commitment and Implementation Success on Competitive Advantage and Firm Performance. Information Systems Journal 5(3):185-202.

Ray, G., Muhanna, W.A. and Barney, J.B. 2005. Information Technology and the Customer Service Process: A Resource-based Analysis. MIS Quarterly 29(4):625-652.

Rocha, F. 1997. Inter-firm Technological Cooperation: Effects of Absorptive Capacity, Firm-size and Specialization. Discussion paper series No. 9707, United Nations University, Institute for New Technology, Maastricht, Netherlands.

Romero, D. and Molina, A. 2009. VO Breeding Environments and Virtual Organizations Integral Business Process Management Framework. Information Systems Frontiers 11(5):569-597.

Ross, J.W., Beath, C.M. and Goodhue, D.L. 1996. Develop Long-term Competitiveness through IT Assets. Sloan Management Review 38(1):31-42.

Salisbury, D., Chin, W.W., Gopal, A. and Newsted, P.R. 2002. Research Report: Better Theory through Measurement – Developing a Scale to Capture Consensus on Appropriation. Information Systems Research 13(1):91-105.

Setia, P., Sambamurthy, V. and Closs, D.J. 2008. Realizing Business Value of Agile IT Applications: Antecedents in the Supply Chain Networks. Information Technology and Management 9(1):5-19.

Sohn, S.Y. and Mok, M.S. 2008. A Strategic Analysis for Successful Open Source Software Utilization Based on a Structural Equation Model. The Journal of Systems and Software 81:1014-1024.

Subramani, M. 2004. How Do Suppliers Benefit from Information Technology Use in Supply Chain Relationships. MIS Quarterly 28(1):45-73.

Szulanski, G. 1996. Exploring Internal Stickiness: Impediments to the Transfer of Best Practice within the Firm. Strategic Management Journal 17:27-43.

Tam, K.Y. and Ho, S.Y. 2005. Web Personalization as a Persuasion Strategy: An Elaboration Likelihood Model Perspective. Information Systems Research 16(3):271-293.

Tanriverdi, H. 2005. Information Technology Relatedness, Knowledge Management Capability, and Performance of Multibusiness Firms. MIS Quarterly 29(2):311-334.

Teece, D.J., Pisano, G. and Shuen, A. 1997. Dynamic Capabilities and Strategic Management. Strategic Management Journal 18:509-533.

Teigland, R. and Wasko, M.M. 2003. Integrating Knowledge through Information Trading: Examining the Relationship between Boundary Spanning Communication and Individual Performance. Decision Science 34(2):261–286.

Tushman, M.L. 1977. Special Boundary Roles in the Innovation Process. Administrative Science Quarterly 22(4):587-605

Udo, G.J. and Davis, J. S. 1992. Factors Affecting Decision Support System Benefits Information & Management 23(6):359-372.

van der Linden, F., Lundell, B. and Marttiin, P. 2009. Commodification of Industrial Software: A Case for Open Source. IEEE Software 26(4):77-83.

van Wendel de Joode, R., Lin, Y. and David, S. 2006. Rethinking Free, Libre and Open Source Software. Knowledge Technology & Policy 18(4):5–16.

Vaast, E. and Walsham, G. 2009. Trans-situated Learning: Supporting a Network of Practice with an Information Infrastructure. Information Systems Research 20(4):547-574.

Ven, K., Verelst, J. and Mannaert, H. 2008. Should You Adopt Open Source Software? IEEE Software 25(3), 54–59

Wade, M. and Hulland, J. 2004. The Resource-based View and Information Systems Research: Review, Extension, and Suggestions for Future Research. MIS Quarterly 28(1):107-142.

Wasko, M.M. and Faraj, S. 2005. Why Should I Share? Examining Social Capital and Knowledge Contribution in Electronic Networks of Practice. MIS Quarterly 29(1):35–57.

Wasko, M.M. and Teigland, R. 2004. Public Goods or Virtual Commons? Applying Theories of Public Goods, Social Dilemmas and Collective Action to Electronic Networks of Practice. Journal of Information Technology Theory and Application 6(1):25-42.

Weill, P. and Vitale, M. 2002. What IT Infrastructure Capabilities Are Needed to Implement ebusiness Models? MIS Quarterly 1(1):17-34.

Wenger, E.C. and Snyder, W.M. 2000. Communities of Practice: The Organizational Frontier. Harvard Business Review 78(1):139-145.

Wesselius, J. 2008 The Bazaar inside the Cathedral: Business Models for Internal Markets. IEEE Software 25(3):60-66.

West, J. 2003. How open is open enough? Melding proprietary and open source platform strategies. Research.Policy 32(7):1259–1285.

West, J. 2005. Understanding Open Source Licensing: Three How-To Guides. IEEE Software 22(4):114-118.

Whelan, E. 2007. Exploring Knowledge Exchange in Electronic Networks of Practice. Journal of Information Technology 22(1):5-13.

Wixom, B.H. and Todd, P.A. 2005. A Theoretical Integration of User Satisfaction and Technology Acceptance. Information Systems Research 16(1):85-102.

Xu, B., Jones, D.R. and Shao, B. 2009. Volunteers’ involvement in Online Community Based Software Development. Information & Management 46(3):151-158.

Zahra, S.A. and George, G. 2002. Absorptive Capacity: A Review, Reconceptualization, and Extension. Academy of Management Review 27(2):185-213.

Zhang, D. and Zhao, J.L. 2006. Knowledge Management in Organizations. Journal of Database Management 17(1):1-8.

Zhu, K. 2004. The Complementarity of Information Technology Infrastructure and E-Commerce Capability: A Resource-based Assessment of Their Business Value. Journal of Management Information Systems 21(1):167-202.

Zhu, K. and Kraemer, K.L. 2005. Post-adoption Variations in Usage and Value of e-business by Organizations: Cross-country Evidence from the Retail Industry. Information Systems Research 16(1):61-84.

Zhu, K., Dong, S., Xu, S. X. and Kraemer, K. L. 2006. Innovation Diffusion in Global Contexts: Determinants of Post-adoption Digital Transformation of European Companies. European Journal of Information Systems 15(6):601-617.

## Appendix A: Items and their Sources

<table><tr><td>Item</td><td>Source</td></tr><tr><td>[...] provides my company with lower total cost of ownership</td><td>Niemi et al. (2009); Brydon and Vining (2008); Ven et al. (2008); Fitzgerald (2006); Fitzgerald and Kenny (2004)</td></tr><tr><td>[...] provides my company with improved reliability</td><td>van der Linden et al. (2009); Ven et al. (2008); Fitzgerald (2006); Bonaccorsi et al. (2006); Norris (2004); West (2003)</td></tr><tr><td>[...] provides my company with greater productivity</td><td>Ajila and Wu (2007); Fitzgerald (2006)</td></tr><tr><td>[...] provides my company with greater innovation capability</td><td>van der Linden et al. (2009); Dahlander and Magnusson (2008); Wesselius (2008); Fitzgerald (2006); Lin (2006); Kohli and Grover, 2008</td></tr><tr><td>[...] provides my company with greater efficiency</td><td>Melville et al. (2004)</td></tr><tr><td>[...] provides my company with greater flexibility</td><td>Ajila and Wu (2007); Fitzgerald (2006); West (2003); Fink and Neumann (2009); Benaroch (2002)</td></tr></table>

## Appendix B: Survey Items

## (except where otherwise noted all items were measured on a 1-7 Likert scale)

Absorptive Capacity for [Open Source Infrastructure Technology]

Prior to implementing […]

1. We<sup>7</sup> had a vision of what we were trying to achieve through the use of […]

2. We had information on the state-of-the-art of […]

3. We had the necessary skills to implement […]<sup>8</sup>

4. We had the technical competence to absorb […]

5. We had a clear division of roles and responsibilities to implement […]

6. We had the managerial competence to absorb […]

## […] Community Ties

1. We have tight relationships with the […] community

2. We often use members of the […] community to help us solve problems

3. Members of the community help us customize […]

4. We often modify our version of […] with updates provided by the community

5. We provide important knowledge to the […] community

## Business Value of […]

1. […] provides my company with lower total cost of ownership\*

2. […] provides my company with improved reliability\*

3. […] provides my company with greater productivity

4. […] provides my company with greater innovation capability

5. […] provides my company with greater efficiency

6. […] provides my company with greater flexibility\*

Extent of Use of […]

1. In my company, […] is a minor (1) --- major (9) infrastructure component.

2. In my company, […] is used minimally (1) --- solely (9).

3. In my company, […] supports few (1) --- most (9) processes.

## Infrastructure Source Openness

1. My company’s IT infrastructure is based on open source technologies.

## About the Authors

InduShobha Chengalur-Smith is Associate Professor and Chair of the Information Technology Management department in the School of Business at the University at Albany – SUNY. She received her PhD from Virginia Tech and her research interests are in the areas of open source software, technology adoption and implementation, information quality, and security. She serves on the editorial boards of several journals including Information & Management and the ACM Journal of Data and Information Quality. Her research has been published in journals such as Information Systems Research, Communications of the ACM, and multiple IEEE Transactions.

Saggi Nevo is an Assistant Professor of Information Technology Management at the University at Albany – SUNY. He received his PhD from the Schulich School of Business at York University. His current research interests include the business value of IT, IS continuance, open source software, and virtual worlds. Saggi’s research has appeared in journals such as MIS Quarterly, Journal of Strategic Information Systems, International Journal of Electronic Commerce, Communications of the AIS, and the DATA BASE for Advances in IS.

Pindaro Demertzoglou is currently a Clinical Assistant Professor of Information Systems at the Lally School of Management and Technology at Rensselaer Polytechnic Institute. Pindaro received his PhD in Information Science from the University at Albany – SUNY. His major areas of teaching and research are databases, decision support systems, data warehousing, and the consequences of information technology for businesses. While at RPI, Pindaro received the Faculty of the Year award and has recently published a book titled Access 2007: Pure SQL.
