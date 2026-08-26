---
otero_id: 4932
otero_key: "E7ARHK5X"
title: "An Empirical Investigation of the Factors Affecting Data Warehousing Success"
authors: "Barbara H. Wixom; Hugh J. Watson"
year: "2001"
journal: "MIS Quarterly"
doi: "10.2307/3250957"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# AN EMPIRICAL INVESTIGATION OF THE FACTORS AFFECTING DATA WAREHOUSING SUCCESS<sup>1</sup>

By: Barbara H. Wixom McIntire School of Commerce University of Virginia Charlottesville, VA 22903 U.S.A. bwixom@mindspring.com

Hugh J. Watson Department of MIS Terry College of Business University of Georgia Athens, GA 30602 U.S.A. hwatson@terry.uga.edu

## Abstract

The IT implementation literature suggests that various implementation factors play critical roles in the success of an information system; however, there is little empirical research about the implementation of data warehousing projects. Data warehousing has unique characteristics that may impact the importance of factors that apply to it. In this study, a cross-sectional survey investigated a model of data warehousing success. Data warehousing managers and data suppliers from 111 organizations completed paired mail questionnaires on implementation factors and the success of the warehouse. The results from a Partial Least

Squares analysis of the data identified significant relationships between the system quality and data quality factors and perceived net benefits. It was found that management support and resources help to address organizational issues that arise during warehouse implementations; resources, user participation, and highly-skilled project team members increase the likelihood that warehousing projects will finish on-time, on-budget, with the right functionality; and diverse, unstandardized source systems and poor development technology will increase the technical issues that project teams must overcome. The implementation's success with organizational and project issues, in turn, influence the system quality of the data warehouse; however, data quality is best explained by factors not included in the research model.

Keywords: Data warehousing, success, IS implementation, Partial Least Squares

ISRL Categories: HA03, FD, AI0610, EL03

## Introduction

During the mid- to late 1990s, data warehousing became one of the most important developments in the information systems field. It is estimated that 95% of the Fortune 1000 companies either have a data warehouse in place or are planning to develop one (META Group 1996). The Palo Alto Management Group predicts that the data warehousing market will grow to a \$113.5 billion market in 2002, including the sales of systems, software, services, and in-house expenditures (Eckerson 1998). This is not surprising considering that for the past few years, surveys of CIOs have found data warehousing, Year 2000, and electronic commerce to be at the top of their strategic initiatives (Eckerson 1999).

A data warehouse (or smaller-scale data mart) is a specially prepared repository of data created to support decision making. Data are extracted from source systems, cleaned/scrubbed, transformed, and placed in data stores (Gray and Watson 1998). A data warehouse has data suppliers who are responsible for delivering data to the ultimate end users of the warehouse, such as analysts, operational personnel, and managers. The data suppliers make data available to end users either through SQL queries or custom-built decisionsupport applications (e.g., DSS and EIS).

Data warehousing is a product of business need and technological advances. The business environment has become more global, competitive, complex, and volatile. Customer relationship management and e-commerce initiatives are creating requirements for large, integrated data repositories and advanced analytical capabilities. More data are captured by organizational systems (e.g., barcode scanning, clickstream) or can be purchased from companies like Dun & Bradstreet and Harte Hanks. Through hardware advances such as symmetric multi-processing, massive parallel processing, and parallel database technology, it is now possible to load, maintain, and access databases of terabyte size. All of these changes are affecting how organizations conduct business, especially in sales and marketing, allowing companies to analyze the behavior of individual customers rather than demographic groups or product classes.

Even though there are many success stories (Beitler and Leary 1997; Grim and Thorton 1997), a data warehousing project is an expensive, risky undertaking. The typical project costs over \$1 million in the first year alone (Watson and Haley 1997). While hard figures are not available, it is estimated that one-half to two-thirds of all initia data warehousing efforts fail (Kelly 1997). The most common reasons for failure include weak sponsorship and management support, insufficient funding, inadequate user involvement, and organizational politics (Watson et al. 1999).

Practitioners and researchers need to better understand data warehousing to ensure the success of these promising, yet risky and costly, IT undertakings. The IT literature contains many studies that investigate the factors that affect the implementation of decision-support applications (e.g., Guimares et al. 1992; Rainer and Watson 1995). While these studies are helpful, a data warehouse is arguably different in that it is an IT infrastructure project, which can be defined as a set of shared, tangible IT resources that provide a foundation to enable present and future business applications (Duncan 1995). The capability of such an infrastructure is thought to impact business value by supporting (or failing to support) important business processes (Ross et al. 1996). Few studies have examined the implementation success of infrastructure projects (Duncan 1995; Parr et al. 1999); instead, infrastructure research focuses on the innovation and diffusion of such phenomenon (for several examples, see Chau and Tam 1997; Prescott and Conger 1995).

There is considerable practitioner wisdom on the keys to data warehousing success; however, it is based on anecdotal evidence from a limited number of companies. There has been no academic research that systematically and rigorously investigates the keys to data warehousing success, using data collected from a large crosssection of firms. In this study, we investigate a research model of data warehousing implementation success using data gathered from mail surveys from 111 organizations. The study investigates the implementation of data warehousing in particular, and extends our knowledge of IT implementation in general.

This article first presents a research model for data warehousing implementation success that was developed from a literature review, an exploratory survey, and structured interviews. Next, it describes the cross-sectional survey that was used to collect data and the results from a

Partial Least Squares analysis of the research model. The findings are discussed in the concluding sections.

## The Research Model

To develop the research model, the IT implementation, infrastructure, data warehousing, and success literature were reviewed to identify factors that potentially affect data warehousing success. After the literature review, survey data were collected from 126 attendees of a 1996 conference sponsored by The Data Warehousing Institute (TDWI). The survey contained two openended questions that asked for a list of critica success factors and obstacles to data warehousing success.<sup>2</sup> These findings, together with the literature review, were used to create an initial research model and to structure hour-long interviews with 10 data warehousing experts (e.g., book authors, consultants, and seminar speakers). The interviews confirmed that the research model contained appropriate factors and relationships among the modelís factors. Minor changes were incorporated into the model based on the interviews.

Figure 1 presents the resulting research model. The rationale for the factors and the relationships among the factors are described in the following sections. Implementation factors, such as management support and user participation, are proposed to influence the success of the data warehouse implementation, which has been broken down into three unique facets. These include success with organizational, project, and technical issues that arise during the lifetime of the warehouse project. Thus, implementation success means that the project team has persuaded the organization to accept data warehousing, completed the warehouse according to plan, and overcome technical obstacles that arose. The success of the implementation in turn affects the system success, defined as the quality of the data warehouse system and its data. This impacts the perceived net benefits from the use of the warehouse.

## Information Systems Success

Researchers have investigated the success of information systems in myriad ways (Garrity and Sanders 1998), such as by measuring the satisfaction of users (Melone 1990), service quality (Pitt et al. 1995), and the perceived usefulness of specific applications (Davis 1989; Moore and Benbasat 1991). Researchers should treat IS success as a multi-faceted construct, choose several appropriate success measures based on the research objectives and the phenomena under investigation, and consider possible relationships among the success dimensions when constructing a research model (DeLone and McLean 1992). Drawing on the work of Seddon (1997), three dimensions of system success were selected as being the most appropriate for this study: data quality, system quality, and perceived net benefits. Empirical studies (e.g., Fraser and Salter 1995; Seddon and Kiew 1994) have found that these three dimensions are related to one another: higher levels of data and system quality are associated with higher levels of net benefits.

Data quality refers to the quality of the data that are available from the data warehouse. This factor has received considerable research attention regarding its definition, component measures, and importance (e.g., Wand and Wang 1996; Wang and Strong 1996). Data quality is frequently discussed in the data warehousing literature as well; providing high-quality data to decision makers is the fundamental reason for a building a warehouse (Watson and Haley 1997). More specifically, data accuracy, completeness, and consistency are critical aspects of data quality in a warehouse (Lyon 1998; Shanks and Darke 1998).

With system quality, the focus is on the system itself. Commonly used performance measures include system flexibility, integration, response time, and reliability (DeLone and McLean 1992). Flexibility and integration are particularly important for decision-support applications (Vandenbosch and Huff 1997). Systems that integrate data from diverse sources can improve organizational decision making (Wetherbe 1991; Wybo and Goodhue 1995), and flexibility allows decision makers to easily modify applications as their information needs change (Vandenbosch and Huff 1997). System quality (i.e., flexibility and integration) is one of the most important advantages for data warehousing because a warehouse provides the infrastructure that integrates data from multiple sources and flexibly supports current and future users and applications (Gray and Watson 1998; Sakaguchi and Frolick 1997).

![](/api/attachments/E7ARHK5X/fulltext/images/4d37441b46175cb47b7745d7d62831f5521c1262f18b5207e0e551611278abd2.jpg)

A system displaying high data quality and system quality can lead to net benefits for various stakeholders, including individuals, groups of individuals, and organizations (Seddon 1997). It can give users a better understanding of the decision context, increase decision-making productivity, and change how people perform tasks. A data warehouse significantly affects how decision making for end users is supported in the organization because IT professionals no longer have to extract data and run queries for users as in the past. When supplied with appropriate data access tools and applications, users can perform decision-making tasks faster and more comprehensively (Haley et al. 1999). In general, data warehousing can change the processes for providing end users with access to data and reduce the time and effort required to provide that access (Graham 1996).

Additional success dimensions were not included because they were considered less appropriate for this study than the selected constructs. User satisfaction measures are most often associated with an end-userís perception of a single application, but a data warehouse supports multiple applications rather than being an application itself. Organization-level benefits are difficult or impossible to assess and to isolate from other factors (e.g., actions of competitors) that affect the organization (Lucas 1981; Ragowsky et al. 1996). Extent of implementation has been applied frequently with large-scale systems, such as electronic data interchange (Massetti and Zmud 1996); however, these studies investigate the innovation and diffusion of IT rather than IT implementation success. Also, successful data warehouses may or may not necessarily be implemented widely across an organization. For example, a warehouse may be used by only a few key analysts who are doing critically important work for the company, whereas other companies may find it useful to roll out data warehousing to the entire organization. Use has similar limitations because it is doubtful that frequent or widespread use can accurately identify a successful warehouse.

Data quality, system quality, and perceived net benefits were used in the research model as the three dimensions of data warehousing success. Based on past findings (Fraser and Salter 1995; Seddon and Kiew 1994) and the theoretica foundations developed by DeLone and McLean (1992) and Seddon (1997), we hypothesized:

H1a: A high level of data quality is associated with a high level of perceived net benefits.

H1b: A high level of system quality is associated with a high level of perceived net benefits.

## Implementation Success

In the data warehousing literature, from the initia survey, and during interviews, three facets of warehousing implementation success were identified: success with organizational issues, success with project issues, and success with technical issues. These factors were believed to affect the ultimate success of the data warehouse. Of course, there likely are other facets of implementation success; however, to keep the research model to a manageable size, only three implementation success factors that were best supported by the studyís model development phase were included. These are described in the following sections.

## Organizational Implementation Success

An implementation is not successful unless the system it produces is accepted into the organization and integrated into work processes. However, an information system implementation can cause considerable organizational change that people tend to resist (Markus 1983). The likelihood of this resistance increases with the scope and magnitude of the changes that the system creates (Tait and Vessey 1988). Data warehousing, in particular, has profound effects on organizations because it can shift data ownership, use, and access patterns; change how jobs are performed; and modify business processes. It moves data ownership from the functional areas to a centralized group, shifts the responsibilities for data access from information systems personnel to end users, changes how users perform their jobs as a result of having access to warehouse data, and allows businesses to operate differently. These changes potentially lead to resistance from managers, data suppliers, and end users.

Much has been written about how to effectively address issues that result from change (Markus and Robey 1988). For example, Lewin (1951) introduced a popular three-stage model whereby people first are prepared for change (i.e., unfreezing), the change then takes place (i.e., moving), followed by a solidification of the processes and ways of thinking caused by the change (i.e., refreezing). Project teams can encourage the organization to accept data warehousing by arranging for support throughout these three stages. They can put change management programs in place, deal with political resistance effectively when it arises, and encourage people throughout the organization to embrace data warehousing. Without these efforts, data warehousing projects are unlikely to result in high levels of data quality and system quality because key stakeholders are unwilling to support the changes that are required. For example, the consequences can include that subject area database specialistsí time is not made available to the project, or changes to operational source systems (to improve data consistency) might be resisted. Thus, we hypothesized:

## H2a: A high level of organizational implementation success is associated with a high level of data quality.

H2b: A high level of organizational implementation success is associated with a high level of system quality.

## Project Implementation Success

IS projects often include a complex array of tasks and roles that must be managed (Brooks 1975), and data warehouse projects in particular require highly skilled, well-managed teams who can overcome issues that arise during the project (Devlin 1997; Sakaguchi and Frolick 1997). Project teams must be able to focus on critical goals and pertinent issues, and avoid unforeseen circumstances that can put the project at risk. Success with project issues can be measured by how wel the team meets its critical time, budgetary, and functional goals (Constantine 1993; Waldrop 1984). In meeting these goals, by definition the team will deliver a data warehouse that provides high-quality data and system features to the client. Thus, we hypothesized:

H3a: A high level of project implementation success is associated with a high level of data quality.

H3b: A high level of project implementation success is associated with a high level of system quality.

## Technical Implementation Success

The technical complexity of data warehousing is high because of the large number of diverse and disparate systems that typically need to be understood, reconciled, and coordinated; the large volume of data that must be extracted, transformed, loaded, and maintained; and the complicated analytics that often are applied to the data (e.g., financial profitability models, data mining algorithms). Technical problems may emerge at various points during a data warehousing project, such as when many, heterogeneous data sources must be combined and when new technology for data warehousing must be fit into an existing technical infrastructure. These technical problems may preclude the warehousing team from creating a repository of high-quality data, and the system may not be as flexible or integrated as the organization requires (Rist 1997). Therefore, we hypothesized:

H4a: A high level of technical implementation success is associated with a high level of data quality.

H4b: A high level of technical implementation success is associated with a high level of system quality.

## Implementation Factors

There is no generic model for IT implementation success and, on the whole, the implementation literature is filled with conflicting results (Markus and Robey 1988). One reason for equivocal results is that different IT implementations possess unique qualities that alter the importance or effect of implementation factors. Vatanasombut and Gray (1999) surveyed the data warehousing literature and found nine success factors that are unique to data warehousing, such as cleanse the data to meet the data warehouse quality standard and choose loading intervals that keep data timely. Bischoff and Alexander (1997) indicate that the amount of complexity involved is what makes a data warehousing project different from traditional software engineering or systems development initiatives. As was mentioned earlier, data warehousing is not an application, which has been the research focus of many implementation studies, but is rather an enabler of many different current and future applications. It shares similar characteristics with other infrastructure projects like enterprise networking and enterprise resource planning. Few studies have addressed the implementation success of these kinds of projects.

On the other hand, there are aspects of a data warehousing project that are similar to applicationlevel IT implementations that have been studied thoroughly. For example, project teams must learn new technologies, work with users to gather requirements, select and use appropriate development methodologies, and anticipate and respond to political problems. Therefore, it is reasonable to expect that implementation factors that have consistently been found to affect IT implementation success are relevant to warehousing as well. Seven implementation factors were included in the research model because of their potentia importance to data warehousing success: management support, champion, resources, user participation, team skills, source systems, and development technology. Each factor is theorized to affect one or more of the implementation success factors.<sup>3</sup>

## Management Support

Management support is widespread sponsorship for a project across the management team and consistently is identified as one of the most important factors for data warehousing success. It motivates people in the organization to support the data warehousing initiative and the organizational changes that inevitably accompany it (Curtis and Joshi 1998; Watson et al. 1998). Management support can overcome political resistance and encourage participation throughout the organization (Markus 1983), and it has been found to be important to the success of many kinds of IT implementations, such as decision support systems (Guimares et al. 1992; Igbaria et al. 1997). Users tend to conform to the expectations of management, and they are more likely to accept a system that they perceive to be backed by the management of their organization (Karahanna et al. 1999). Therefore, we hypothesized:

## H5: A high level of management support is associated with a high level of organizational implementation success.

## Champion

A champion actively supports and promotes the project and provides information, materia resources, and political support. Champions are important to data warehousing (Barquin and

Edelstein 1997; Watson et al. 1998), as well as to other IT projects (Beath 1991; Reich and Benbasat 1990). Champions exhibit transformational leadership behavior when they strongly support a project, and they possess the skills and clout needed to overcome resistance that may arise within the organization (Howell and Higgins 1990). Like management support, champions can help data warehousing projects with organizational issues; however, a champion is likely to have even closer ties to the daily actions and goals of the project team. It can be expected that champions not only help data warehousing projects achieve success at an organizational level, but also that they help teams meet their projectlevel goals. We hypothesized:

H6a: A strong champion presence is associated with a high level of organizational implementation success.

H6b: A strong champion presence is associated with a high level of project implementation success.

## Resources

Resources include the money, people, and time that are required to successfully complete the project (Ein-Dor and Segev 1978). Studies have found that resource problems have a negative effect on successful system design and implementation (Tait and Vessey 1988). Resources are likely to be important to data warehousing projects because data warehouses are expensive, timeconsuming, resource-intensive initiatives. The presence of resources can lead to a better chance of overcoming organizational obstacles and communicating high levels of organizational commitment (Beath 1991; Tait and Vessey 1988). Resources also can help project teams meet their project milestones. Once tasks are identified, the project timeline is influenced by the amount of time and the people assigned to do the work, so better resources should affect the accomplishment of milestones during implementation (McConnell 1996). Thus, we hypothesized:

## H7a: A high level of resources is associated with a high level of organizational implementation success.

H7b: A high level of resources is associated with a high level of project implementation success.

## User Participation

User participation occurs when users are assigned project roles and tasks, which leads to a better communication of their needs and helps ensure that the system is implemented successfully (Hartwick and Barki 1994). It is particularly important when the requirements for a system are initially unclear, as is the case with many of the decision-support applications that a data warehouse is designed to support. The data warehousing literature indicates that user participation increases the likelihood of managing users expectations and satisfying user requirements (Barquin and Edelstein 1997; Watson and Haley 1997). When users participate on warehousing projects, they have a better understanding of what the warehouse will provide, which makes them more likely to accept the warehouse when it is delivered. Users also can help the project team stay focused on the requirements and needs of the user community if they participate on the project team throughout the implementation. Thus, we hypothesized:

H8a: A high level of user participation is associated with organizational implementation success.

H8a: A high level of user participation is associated with project implementation success.

## Team Skills

People are important when implementing a system and can directly affect its success or failure (Brooks 1975). In particular, the skills of the data warehousing development team have a major influence on the outcomes of the warehouse project (Barquin and Edelstein 1997). Team skills include both technical and interpersonal abilities, and a team with strong technical and interpersona skills is able to perform tasks and interact with users well (Constantine 1993; Finlay and Mitchell 1994). The skills of development teams have been traced to IT implementation success (Ancona and Caldwell 1992); only a high quality, competent team can identify the requirements of complex projects (Maish 1979). This mix of skills should help warehouse projects more successfully meet their objectives at a project level, and it should be of great value when technical obstacles need to be overcome. A highly skilled project team should be much better equipped to manage and solve technical problems. We hypothesized:

H9a: A high level of team skills is associated with project implementation success.

H9b: A high level of team skills is associated with technical implementation success.

## Source Systems

Past studies have found that the quality of an organization's existing data can have a profound effect on systems initiatives and that companies that improve data management realize significant benefits (Goodhue et al. 1992; Kraemer et al. 1993). A primary purpose of data warehousing is to integrate data throughout the organization; however, data often resides in diverse, heterogeneous sources. Each unique source requires specialized expertise and coordination to access the data. Further, the data that exist often are defined differently across sources, making it challenging for the project team to reconcile and load the data into the warehouse properly. Goodhue et al. (1988) found that the lack of data standards was a "major underlying problem with data, often making it difficult or impossible to share or interpret data across application systems boundaries" (p. 389). Standardized data can result in easier data manipulation, fewer problems, and, ultimately, a more successful system (Bergeron and Raymond 1997). Thus, the quality of data sources depends on the standardization of their technology and data, and we hypothesized:

H10: High-quality source systems are associated with technical implementation success.

## Development Technology

Development technology is the hardware, software, methods, and programs used in completing a project. The development tools that a project team uses can influence the effectiveness of the development effort as much as other factors, such as people. The tools can impact the efficiency and effectiveness of the development team, especially if they are not well understood or easy to use (Banker and Kauffman 1991). The development tools needed to build a data warehouse are different from those used with operational systems because warehousing requires sophisticated extraction, transformation, and loading software; data cleansing programs; data base performance tuning methods; and multidimensional modeling and analysis tools. If the development technology does not meet the needs of the project team or work well with the legacy systems, the data warehouse implementation will suffer (Rist 1997; Watson et al. 1998). Therefore, we hypothesized:

H11: Better development technology is associated with technical implementation success.

## Research Method

## Data Collection

Initial versions of two survey instruments were developed based on the data warehousing, implementation, and success literature. The first instrument was created to measure the implementation factors and the second to measure data warehousing success. Whenever possible, previously tested questions were used, and generally accepted instrument construction guidelines were followed (Converse and Presser 1986; Dillman 1978; Fox et al. 1988). Both surveys were reviewed by the University of Georgia Center for Survey Research; by academics with specific expertise in data warehousing, database, data integration, and survey construction; and by data warehousing experts, such as the head of Arthur Andersen & Co.'s data warehousing practice and the president of The Data Warehousing Institute. The multiple phases of instrument development resulted in some restructuring and refinement of the survey and established its face and content validity (Nunnally 1978). The resulting surveys were then pilot-tested by 10 organizations to identify problems with the instrumentsí wording, content, format, and procedures. Pilot participants returned written comments about the survey instruments, and each was telephoned for a more detailed discussion.

Data were collected from two types of respondents at each participating organization to measure perceptions of implementation factors and success factors separately. This approach ensured that the appropriate person provided perceptions for the study (Hufnagel and Conca 1994); otherwise, ìhalo effectsî or other biases could result from one person providing information for both the independent and dependent constructs. A total of 225 survey packets were mailed to the data warehousing managers of operational data warehouses<sup>4</sup> listed in the researchersí data warehousing database.<sup>5</sup> The survey that included implementation factor questions was completed by the data warehousing manager or the person most familiar with the data warehousing implementation. This contact was instructed to distribute the success factor survey to one or two data suppliers (two people were encouraged to further reduce single-source response bias), who were clearly defined as the managers of end-user computing or people responsible for an application that uses data from the warehouse (e.g., the executive information system manager). It was felt that data suppliers would be best qualified to assess the success of the data warehouse, as opposed to end users who only see the warehouse through the lens of the data access tool (e.g., managed query environment) or application (e.g., DSS) that they are given.

Several rounds of follow-up phone calls and emails were used to remind the participants to return the surveys, and 111 companies responded with usable pairs of surveys (an implementation survey and at least one success survey) for an overall response rate of 49%. A total of 55 organizations returned two success surveys, and we examined the level of participant agreement on the success items using a one-way ANOVA with team variation as the independent variable (Amason 1996). In each case, the between-team variation was significantly larger than the withinteam variation, suggesting that the scores for each organization could be combined into a single organizational response. Thus, the average of the individual responses was used as the success measures for each organization.

The participating organizations represent the different regions of the United States: 24 from the Northeast, 29 from the South, 34 from the Midwest, and 12 from the West. Also, 12 organizations located in South Africa, Canada, or Austria participated in the study. These organizations ranged in size, with mean gross revenues of \$5.8 billion (minimum = \$150,000; maximum = \$40 billion) and a mean number of employees of 23,571 (minimum = 35; maximum = 300,000). Table 1 shows the industries that are represented. All of the companies had operational data warehouses when answering the surveys, and nearly all of them considered their initiative successful<sup>6</sup> (26% = "a runaway success"; 72% = "an up and coming system"; 2% = "potentially in trouble").

Most respondents to the first questionnaire were data warehousing managers (65%). Others were people who had significant knowledge of the data warehousing implementation, such as data warehousing staff members (11%) or employees holding some other position in the organization (e.g., IS manager, CIO (24%)). Of the respondents, 91% were actively involved in the project. The respondents to the second survey included functional area managers and professionals (45%), IS managers (25%), IS staff members (24%), and other members of the organization (6%). All of these people were responsible for providing warehouse data to end users.

## Operationalization of Constructs

All items were developed based on items from existing instruments, the data warehousing literature, and input from data warehousing experts. Existing items were not used unless the measures were well supported by the latter two sources. Items were measured based on a sevenpoint Likert scale ranging from (1) ìstrongly disagreeî to (7) ìstrongly agree.î Table 2 defines the constructs used in the study and lists their respective survey items. Four items were reverse scaled, and they are noted accordingly.

Success factors. Data quality was operationalized as the accuracy, comprehensiveness, consistency, and completeness of the data provided by the warehouse. These dimensions are common measures of data quality for information systems in general (DeLone and McLean 1992), and data warehousing in particular (Lyon 1998; Shanks and Darke 1998). Flexibility and integration have been shown to be important dimensions of system quality; therefore, system quality was measured by four items that asked about the level of flexibility and integration of the data warehouse. Perceived net benefits was operationalized using three items that measured the change in the jobs of data suppliers and the reduction of time and effort required to support decision making in the end-user community (Graham 1996; Seddon 1997).

Organizational implementation success. This construct was measured using three questions that captured the extent that political resistance in the organization was dealt with effectively, change was managed effectively, and support existed from people throughout the organization (Markus 1983). Management support, champion, resources, and user participation are believed to help project teams overcome organizational issues (Beath 1991; Reich and Benbasat 1990; Steinbart and Nath 1992; Tait and Vessey 1988).

<table><tr><td colspan="3">Table 1. Respondents by Industry</td></tr><tr><td>Industry</td><td>Number of Respondents</td><td>Percent of Respondents</td></tr><tr><td>Manufacturing</td><td>16</td><td>14</td></tr><tr><td>Healthcare</td><td>15</td><td>13</td></tr><tr><td>Retail/ Wholesale</td><td>13</td><td>12</td></tr><tr><td>Telecommunications</td><td>13</td><td>12</td></tr><tr><td>Financial Services/ Banking</td><td>11</td><td>10</td></tr><tr><td>Insurance</td><td>9</td><td>8</td></tr><tr><td>Government</td><td>8</td><td>7</td></tr><tr><td>Utilities</td><td>6</td><td>5</td></tr><tr><td>Education/ Publishing</td><td>3</td><td>3</td></tr><tr><td>Petrochemical</td><td>2</td><td>2</td></tr><tr><td> $Other^a$ </td><td>15</td><td>14</td></tr></table>

<sup>a</sup>Other industries included Transportation, Market Research, Reseller, Travel, Defense, Distribution, and Consumer Products

Project implementation success. This construct included questions that asked how well the project was completed on time, on budget, while delivering the right requirements. A champion, resources, user participation, and team skills have been associated with such outcomes (Finlay and Mitchell 1994; Lawrence and Low 1993; Reich and Benbasat 1990; Yoon et al. 1995).

Technical implementation success. This construct was measured by asking about the technical problems that arose and technical constraints that occurred during the implementation of the warehouse. Poor team skills, source systems, and inadequate development tools have been found to affect the complexity of using technology, resulting in greater technical problems (Finlay and Mitchell 1994; Tait and Vessey 1988). Technica implementation success was defined as the ability to overcome these problems, and its questions were worded with help from data warehousing experts.

Implementation factors. Management support was operationalized as the overall support management showed for data warehousing and their interest in user satisfaction (Yoon et al. 1995). Two items for assessing the project champion were developed to measure whether a champion existed from a functional area and from the IS area. User participation was measured using three items that assessed the IS-user relationship, the usersí responsibilities on the project, and hands-on activities performed by the users (Barki and Hartwick 1994). Based on the work of Waldrop (1984), two items measured the data warehousing teamís interpersonal and technical skills. The quality of the source systems was measured based on Wybo and Goodhue (1995) and suggestions from data warehousing experts. The items asked about the diversity of the data source platforms and the data standards that they supported. Development technology items were created to reflect the compatibility of the data warehousing tools with existing technology (Leonard-Barton and Sinha 1993) and the teamís experience with the new tools (McFarlan 1981).

## Data Analysis

The research model was tested using Partial Least Squares (PLS), a structural modeling technique that is well suited for highly complex predictive models (Wold and Joreskog 1982). PLS has several strengths that made it appropriate for this study, including its ability to handle formative constructs and its small sample size requirements.<sup>7</sup> The technique concurrently tests the psychometric properties of the scales used to measure the variables in the model (i.e., the measurement model) and analyzes the strengths and directions of the relationships among the variables (i.e., the structural model) (Lohmoller 1989). (For overviews of PLS, see Barclay et al. [1995] or Chin [1998]).

The test of the measurement model includes the estimation of internal consistency and the convergent and discriminant validity of the instrument items; however, reflective and formative measures should be treated differently. Reflective items represent the effects of the construct under study (Bollen 1984) and, therefore, "reflect" the construct of interest; eight constructs in this study are reflective. Table 2 lists the reflective measures and their internal consistency reliabilities, as defined by Fornell and Larcker (1981). All reliability measures were well above the recommended level of .70, thus indicating adequate internal consistency (Nunnally 1978). These items also demonstrated satisfactory convergent and discriminant validity. Convergent validity is adequate when constructs have an Average Variance Extracted (AVE) of at least .5 (Fornell and Larcker 1981). For satisfactory discriminant validity, the AVE from the construct should be greater than the variance shared between the construct and other constructs in the model (Chin 1998). Table 3 lists the correlation matrix, with correlations among constructs and the square root of AVE on the diagonal. Convergent validity also is demonstrated when items load highly (loading > .50) on their associated factors. Table 2 shows that all of the reflective measures have significant loadings that load much higher than the suggested threshold.

Formative measures are items that cause the construct under study (Bollen 1984). Thus, different dimensions are not expected to correlate or demonstrate internal consistency (Chin 1998). For example, the presence of a champion is caused by having a high-level supporter from the IS area and/or having a high-level supporter from a functional area. The fact that an IS champion exists does not necessarily ensure that a functional area champion exists, and vice versa. Although internal consistency reliability is inappropriate for formative measures, the item weights can be examined to identify the relevance of the items to the research model (see Table 2). The formative constructs also were carefully reviewed to make sure that they performed as expected in the research model and that they were well supported by past studies and data warehousing resources.

Because this was a cross-sectional study that included data warehousing projects that had been operational for different periods of time, t-tests were conducted to test for the potential influence of time on success. Means were compared for the perceived net benefits items for data warehouses that had been operational for a year or less (N = 44) versus data warehouses that had been operational for more than two years (N = 57). This was done to confirm that data warehouses that were in place longer were not experiencing different benefits from newly implemented ones. None of the null hypotheses (t-tests) could be rejected at the .05 level, suggesting that time did not significantly influence the findings.

The test of the structural model includes estimating the path coefficients, which indicate the strengths of the relationships between the dependent and independent variables, and the R<sup>2</sup> value, which represents the amount of variance explained by the independent variables. Together, the R<sup>2</sup> and the path coefficients (loadings and significance) indicate how well the model is performing. R<sup>2</sup> indicates the predictive power of the model, and the values should be interpreted in the same manner as R<sup>2</sup> in a regression analysis. The path coefficients should be significant and directionally consistent with expectations.

PLS Graph version 2.91 (Chin and Frye 1996) was used for the analysis, and the bootstrap resampling method (100 resamples) determined the significance of the paths within the structural model. The sample size of 111 exceeded the recommended minimum of 40, which was adequate for model testing. The results are presented in Figure 2.

<table><tr><td colspan="5">Management Support: widespread sponsorship for a project across the management team. REFLECTIVE</td></tr><tr><td>Fornell = .76</td><td>Mean</td><td>Std. Dev.</td><td>Loading $^{††}$ </td><td>t-Stat</td></tr><tr><td>Overall, management has encouraged the use of DW.</td><td>5.36</td><td>1.33</td><td>.91</td><td>21.2***</td></tr><tr><td>User satisfaction has been a major concern of management.</td><td>5.09</td><td>1.47</td><td>.59</td><td>4.00***</td></tr><tr><td colspan="5">Champion: a person within the organization who actively supports and promotes the project. FORMATIVE</td></tr><tr><td>Fornell = .47</td><td>Mean</td><td>Std. Dev.</td><td>Weight</td><td>t-Stat</td></tr><tr><td>A high-level champion(s) for DW came from IS.</td><td>4.31</td><td>2.18</td><td>.94</td><td>5.35***</td></tr><tr><td>A high-level champion(s) for DW came from a functional area(s).</td><td>5.01</td><td>1.87</td><td>.87</td><td>5.37***</td></tr><tr><td colspan="5">Resources: the money, time, and people required to successfully implement a data warehouse. FORMATIVE</td></tr><tr><td>Fornell = .87</td><td>Mean</td><td>Std. Dev.</td><td>Weight</td><td>t-Stat</td></tr><tr><td>The DW project was adequately funded.</td><td>5.05</td><td>1.63</td><td>.14</td><td>0.50</td></tr><tr><td>The DW project had enough team members to get the work done.</td><td>4.54</td><td>1.80</td><td>.38</td><td>1.82*</td></tr><tr><td>The DW project was given enough time for completion.</td><td>4.45</td><td>1.65</td><td>.60</td><td>3.77***</td></tr><tr><td colspan="5">User Participation: when users are assigned project roles and tasks during implementation of the data warehouse. FORMATIVE</td></tr><tr><td>Fornell = .80</td><td>Mean</td><td>Std. Dev.</td><td>Weight</td><td>t-Stat</td></tr><tr><td>IS and users worked together as a team on the DW project.</td><td>5.66</td><td>1.60</td><td>.82</td><td>4.16***</td></tr><tr><td>Users were assigned full-time to parts of the DW project.</td><td>4.35</td><td>2.20</td><td>.36</td><td>1.30</td></tr><tr><td>Users performed hands-on activities (e.g., data modeling) during the DW project.</td><td>4.34</td><td>2.00</td><td>.06</td><td>0.20</td></tr><tr><td colspan="5">Team Skills: the technical and interpersonal abilities of members of the data warehousing team. FORMATIVE</td></tr><tr><td>Fornell = .90</td><td>Mean</td><td>Std. Dev.</td><td>Weight</td><td>t-Stat</td></tr><tr><td>Members of the DW team (including consultants) had the right technical skills for DW.</td><td>4.84</td><td>1.56</td><td>.62</td><td>3.86***</td></tr><tr><td>Members of the DW team had good interpersonal skills.</td><td>5.19</td><td>1.39</td><td>.46</td><td>2.46***</td></tr><tr><td colspan="5">Table 2. Continued</td></tr><tr><td colspan="5">Source Systems: the quality (e.g., standardization, readiness, disparity) of the source systems that provide data to the warehouse.FORMATIVE</td></tr><tr><td>Fornell = .60</td><td>Mean</td><td>Std. Dev.</td><td>Weight</td><td>t-Stat</td></tr><tr><td>Common definitions for key data items were implemented across the source systems</td><td>4.52</td><td>1.83</td><td>.63</td><td>2.82***</td></tr><tr><td>The data sources used for DW were diverse and disparate applications/systems.R</td><td>2.38</td><td>1.71</td><td>.05</td><td>.21</td></tr><tr><td>A significant number of source systems had to be modified to provide data for DW.R</td><td>4.56</td><td>1.93</td><td>.65</td><td>2.82***</td></tr><tr><td colspan="5">Development Technology: effective hardware, software, methods, and programs to build the data warehouse.REFLECTIVE</td></tr><tr><td>Fornell = .83</td><td>Mean</td><td>Std. Dev.</td><td>Loading</td><td>t-Stat</td></tr><tr><td>The DW technology that the project team used worked well with technology already in place in the organization.</td><td>4.71</td><td>1.58</td><td>.79</td><td>7.04***</td></tr><tr><td>Appropriate technology was available to implement DW.</td><td>5.34</td><td>1.36</td><td>.89</td><td>17.8***</td></tr><tr><td colspan="5">Organizational Implementation Success: implementation-level success in addressing organizational issues, such as change management, widespread support, and political resistance.REFLECTIVE</td></tr><tr><td>Fornell = .91</td><td>Mean</td><td>Std. Dev.</td><td>Loading</td><td>t-Stat</td></tr><tr><td>Any political resistance to DW in the organization was dealt with effectively.</td><td>4.61</td><td>1.44</td><td>.90</td><td>27.2***</td></tr><tr><td>Change in the organization created by DW was managed effectively.</td><td>4.20</td><td>1.5</td><td>.89</td><td>33.1***</td></tr><tr><td>The DW had support from people throughout the organization.</td><td>4.41</td><td>1.59</td><td>.86</td><td>27.4***</td></tr><tr><td colspan="5">Project Implementation Success: implementation-level success in completing the project on time, on budget, with the proper functionality.REFLECTIVE</td></tr><tr><td>Fornell = .84</td><td>Mean</td><td>Std. Dev.</td><td>Loading</td><td>t-Stat</td></tr><tr><td>The DW project met its critical project deadlines (eg., rollout deadline, initial development deadline).</td><td>4.60</td><td>1.85</td><td>.78</td><td>15.3***</td></tr><tr><td>The cost of the DW did not exceed its budgeted amount.</td><td>4.59</td><td>1.79</td><td>.79</td><td>17.7***</td></tr><tr><td>The DW project provided all of the DW functionality that it was supposed to provide.</td><td>4.83</td><td>1.51</td><td>.83</td><td>27.6***</td></tr><tr><td colspan="5">Technical Implementation Success: implementation-level success in overcoming technical problems. REFLECTIVE</td></tr><tr><td>Fornell = .91</td><td>Mean</td><td>Std. Dev.</td><td>Loading</td><td>t-Stat</td></tr><tr><td>Many technical problems arose during the DW implementation.R</td><td>4.51</td><td>1.71</td><td>.89</td><td>23.1***</td></tr><tr><td>Numerous technical constraints were imposed on the DW implementation.R</td><td>3.86</td><td>1.76</td><td>.94</td><td>53.1***</td></tr><tr><td colspan="5">Data Quality: The quality of data that are provided by the data warehouse. REFLECTIVE</td></tr><tr><td>Fornell = .84</td><td>Mean</td><td>Std. Dev.</td><td>Loading</td><td>t-Stat</td></tr><tr><td>Users (or applications) have more accurate data now from DW than they had from source systems (e.g., transaction systems).</td><td>4.96</td><td>1.43</td><td>.80</td><td>5.50***</td></tr><tr><td>DW provides more comprehensive data to users (or applications) than source systems provided.</td><td>5.66</td><td>1.19</td><td>.67</td><td>4.84***</td></tr><tr><td>DW provides more correct data to users (or applications) in respect to source systems.</td><td>4.62</td><td>1.40</td><td>.70</td><td>4.23***</td></tr><tr><td>DW has improved the consistency of data to users (or applications) over that of source systems.</td><td>5.47</td><td>1.22</td><td>.82</td><td>8.80***</td></tr><tr><td colspan="5">System Quality: the flexibility and integration of the data warehouse. REFLECTIVE</td></tr><tr><td>Fornell = .86</td><td>Mean</td><td>Std. Dev.</td><td>Loading</td><td>t-Stat</td></tr><tr><td>DW can flexibly adjust to new demands or conditions.</td><td>4.86</td><td>1.14</td><td>.77</td><td>19.1***</td></tr><tr><td>DW effectively integrates data from systems servicing different functional areas.</td><td>5.40</td><td>1.18</td><td>.73</td><td>12.0***</td></tr><tr><td>DW is versatile in addressing data needs as they arise.</td><td>4.97</td><td>1.07</td><td>.85</td><td>24.0***</td></tr><tr><td>DW effectively integrates data from a variety of data sources within the organization.</td><td>5.47</td><td>1.08</td><td>.76</td><td>17.9***</td></tr><tr><td colspan="5">Perceived Net Benefits: the benefits of the data warehouse as perceived by a data supplier. REFLECTIVE</td></tr><tr><td>Fornell = .88</td><td>Mean</td><td>Std. Dev.</td><td>Loading</td><td>t-Stat</td></tr><tr><td>DW has changed my job significantly.</td><td>5.25</td><td>1.46</td><td>.75</td><td>11.2***</td></tr><tr><td>DW has reduced the time it takes to support decision making to the end-user community.</td><td>5.68</td><td>1.06</td><td>.91</td><td>60.1***</td></tr><tr><td>DW has reduced the effort it takes to support decision making to the end-user community.</td><td>5.44</td><td>1.15</td><td>.86</td><td>29.0***</td></tr></table>

<sup>Ü</sup>The variables were measured using seven-point Likert-type scales ranging from strongly disagree to strongly agree. <sup>ÜÜ</sup>Loadings have been provided for reflective measures. They represent the extent to which the variables are related to the underlying construct. Weights have been provided for formative measures. They represent the extent to which the variables are related to the underlying construct.  
<sup>R</sup>This item was reverse coded.  
Indicates that the item is significant at the p < .05 level.  
\*\* Indicates that the item is significant at the p < .01 level.  
\*\*\* Indicates that the item is significant at the p < .001 level.

<table><tr><td colspan="14">Table 3. Correlations of Latent Variables</td></tr><tr><td></td><td>MANS</td><td>CHSM</td><td>RESO</td><td>USER</td><td>SKIL</td><td>SOUR</td><td>DEVT</td><td>ORGS</td><td>PROS</td><td>TECS</td><td>DATA</td><td>SYST</td><td>PNB</td></tr><tr><td>MANS</td><td>.79</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CHAM</td><td>0.423</td><td>.55</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RESO</td><td>0.411</td><td>0.285</td><td>.84</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>USER</td><td>0.463</td><td>0.289</td><td>0.162</td><td>.76</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SKIL</td><td>0.357</td><td>0.218</td><td>0.350</td><td>0.224</td><td>.90</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SOUR</td><td>0.096</td><td>0.042</td><td>0.136</td><td>0.011</td><td>0.236</td><td>.64</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DEVT</td><td>0.293</td><td>0.235</td><td>0.385</td><td>0.122</td><td>0.525</td><td>0.323</td><td>.84</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ORGS</td><td>0.604</td><td>0.348</td><td>0.435</td><td>0.353</td><td>0.254</td><td>0.093</td><td>0.273</td><td>.88</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PROS</td><td>0.322</td><td>0.304</td><td>0.465</td><td>0.336</td><td>0.555</td><td>0.222</td><td>0.419</td><td>0.311</td><td>.80</td><td></td><td></td><td></td><td></td></tr><tr><td>TECS</td><td>0.062</td><td>0.121</td><td>0.249</td><td>0.090</td><td>0.323</td><td>0.291</td><td>0.403</td><td>0.127</td><td>0.342</td><td>.84</td><td></td><td></td><td></td></tr><tr><td>DATA</td><td>0.099</td><td>0.091</td><td>0.128</td><td>0.052</td><td>0.092</td><td>0.019</td><td>0.109</td><td>0.069</td><td>0.025</td><td>0.090</td><td>.75</td><td></td><td></td></tr><tr><td>SYST</td><td>0.283</td><td>0.139</td><td>0.341</td><td>0.005</td><td>0.262</td><td>0.134</td><td>0.287</td><td>0.298</td><td>0.271</td><td>0.153</td><td>0.304</td><td>.78</td><td></td></tr><tr><td>PNB</td><td>0.180</td><td>0.012</td><td>0.290</td><td>0.032</td><td>0.292</td><td>0.116</td><td>0.191</td><td>0.117</td><td>0.209</td><td>0.135</td><td>0.309</td><td>0.593</td><td>.84</td></tr></table>

D ia<sub>g</sub>onal elements are the s<sub>q</sub> uare root of Avera<sub>g</sub>e Variance Extracted These val u es shou ld exceed the i nter-constru ct correlatio ns for ade<sub>q</sub> uate d iscri m i n a nt va l i d it<sub>y</sub>

Le<sub>g</sub>end :

MAN S = Mana<sub>g</sub>ement S u <sub>pp</sub>ort

CHAM = Cham <sub>p</sub>ion

RESO = Resou rces

U S E R = User Partici <sub>p</sub>ation

S KI L = Team S ki l ls

SO U R = Sou rce S<sub>y</sub>stems

D EVT = Develo<sub>p</sub>ment Tech nolo<sub>gy</sub>

O RGS = Or<sub>g</sub>an izational I m <sub>p</sub>lementation S u ccess

P ROS = Project I m plementation S u ccess

TECS = Tech n ical I m <sub>p</sub>lementation S u ccess

DATA = Data Qual it<sub>y</sub>

SYST = S<sub>y</sub>stem Qual it<sub>y</sub>

P N B = Perceived Net Benefits

![](/api/attachments/E7ARHK5X/fulltext/images/ef4a28e1c8349046b7481cd73a3c90f7c6b64bea4193cfd24b13e1cfa40387d6.jpg)

大 Indicates that the item is significant at the p < .05 level.

\*\* Indicates that the item is significant at the $\mathsf { p } < . 0 1$ level.

\*\*\* Indicates that the item is significant at the p < .001 level.

Figure 2. Model Results

As hypothesized, perceived net benefits was associated with system quality and data quality, which together explained 37% of the dependent constructís variance. Both paths had positive effects, with path coefficients of .549 and .142, respectively. Hypotheses 1a and 1b were supported.

Against expectations, organizational, project, and technical implementation success had no effect on data quality, as shown by the three nonsignificant paths. Hypotheses 2a, 3a, and 4a were not supported. The $\mathsf { R } ^ { 2 }$ value for data quality was .016, suggesting that factors not included in this model are more important in explaining the variance for data quality. Implementation success with organizational and project issues did have significant effects on system quality (paths = .235 and .177). Hypotheses 2b and 3b were supported.

The constructs explained 13% of the variance contained in system quality.

Management support and resources contributed to organizational implementation success, supporting hypotheses 5 and 7a. These factors had path coefficients of .440 and .219, and along with champion and user participation, they explained 42% of the variance. Consistent with hypotheses 7b, 8b, and 9b, resources, user participation, and team skills contributed to project implementation success, with path coefficients of .271, .177, and .401, respectively. When combined with the champion construct, they explained 44% of the variance for the dependent construct. As hypothesized in hypotheses 10 and 11, source systems and development technology contributed to technical implementation success, and they along with team skills explained 21% of the factorís variance.

<table><tr><td colspan="3">Table 4. Hypothesis Results</td></tr><tr><td>H1a</td><td>A high level of data quality will be associated with a high level of perceived net benefits.</td><td>Supported</td></tr><tr><td>H1b</td><td>A high level of system quality will be associated with a high level of perceived net benefits.</td><td>Supported</td></tr><tr><td>H2a</td><td>A high level of organizational implementation success is associated with a high level of data quality.</td><td>Not Supported</td></tr><tr><td>H2b</td><td>A high level of organizational implementation success is associated with a high level of system quality.</td><td>Supported</td></tr><tr><td>H3a</td><td>A high level of project implementation success is associated with a high level of data quality.</td><td>Not Supported</td></tr><tr><td>H3b</td><td>A high level of project implementation success is associated with a high level of system quality.</td><td>Supported</td></tr><tr><td>H4a</td><td>A high level of technical implementation success is associated with a high level of data quality.</td><td>Not Supported</td></tr><tr><td>H4b</td><td>A high level of technical implementation success is associated with a high level of system quality.</td><td>Not Supported</td></tr><tr><td>H5</td><td>A high level of management support is associated with a high level of organizational implementation success.</td><td>Supported</td></tr><tr><td>H6a</td><td>A strong champion presence is associated with a high level of organizational implementation success.</td><td>Not Supported</td></tr><tr><td>H6b</td><td>A strong champion presence is associated with a high level of project implementation success.</td><td>Not Supported</td></tr><tr><td>H7a</td><td>A high level of resources is associated with a high level of organizational implementation success.</td><td>Supported</td></tr><tr><td>H7b</td><td>A high level of resources is associated with a high level of project implementation success.</td><td>Supported</td></tr><tr><td>H8a</td><td>A high level of user participation is associated with organizational implementation success.</td><td>Supported</td></tr><tr><td>H8b</td><td>A high level of user participation is associated with project implementation success.</td><td>Supported</td></tr><tr><td>H9a</td><td>A high level of team skills is associated with project implementation success.</td><td>Supported</td></tr><tr><td>H9b</td><td>A high level of team skills is associated with technical implementation success.</td><td>Not Supported</td></tr><tr><td>H10</td><td>High-quality source systems are associated with technical implementation success.</td><td>Supported</td></tr><tr><td>H11</td><td>Better development technology is associated with technical implementation success.</td><td>Supported</td></tr></table>

The development technology had the greatest impact, with a path coefficient of .276, followed by the source systems with a path of .169. See Table 4 for a summary of the hypothesis test results.<sup>8</sup>

## Discussion and Implications

This study examined the factors that affect data warehousing success by using a research mode that was developed from the IT implementation and data warehousing literature, an exploratory survey, and structured interviews. Implementation success factors were used to help understand why the implementation factors affected the system success and ultimate success from the use of the system. The following sections present key observations regarding the major pieces of the model.

## Perceived Net Benefits

Data quality and system quality had significant relationships with perceived net benefits and explained a good portion of the construct's variance. These results show that the quality of the data warehouse and the data that it provides are associated with the net benefits as perceived by the organization's data suppliers. In other words, a warehouse with good data quality and system quality improves the way data is provided to decision-support applications and decision makers. This supports the data warehousing literature that emphasizes that data warehouses must contain high-quality data, flexibly respond to usersí requests for data, and integrate data in the ways that are required by users, all in order to create value for the organization.

This study furthers the knowledge of IT success by supporting the use of multiple success dimensions and confirming other research findings that show the success dimensions (e.g., system quality, data quality, and perceived net benefits) to be interrelated. System quality and data quality do affect perceived net benefits in the context of data warehousing. More work is needed, however, to examine exactly how the dimensions of success interrelate. Theoretically, we need to understand why relationships exist, and practically, we need to explore how success measures can be applied most effectively. We also need to explore the role of other success dimensions, such as extent of implementation or use, in data warehousing.

## Data Quality and System Quality in a Data Warehouse Context

Factors not included in the research model affect the data quality of the data warehouse. Further research is needed to understand warehouse data quality and the factors that affect it. For example, does poor data quality in source systems undermine the ability to provide high-quality data in a data warehouse? What role does the extraction, cleansing, and transformation process play in creating high-quality data? Do the data model and data storage format have any influence on the perception of the dataís quality? Or, can a data warehouse even exist without data quality? The companies in this sample had at least somewhat successful warehouse implementations, and it may be possible that data quality is required before a warehouse project can be completed. Thus, does a relationship between implementation success and data quality not exist because organizations have to achieve an acceptable level of quality to roll out the warehouse to their users? There are many questions regarding data quality that remain unanswered.

In data warehousing, system quality depends on a number of factors, such as the selection of subject areas and data for the data store, the underlying data model that was created, and the warehouse architecture that was selected. Not all organizations have the vision and knowledge to properly include these considerations in the design of their warehouses, which can lead to a future lack of flexibility and integration of the data. The findings of this study show that system quality was associated with implementation success with organizational and project issues. The reasons for these relationships are clear when one takes into account how much easier it is for a team to create a flexible and integrated data warehouse when organizational barriers are removed and a wellmanaged team is responsible for meeting the demands of the project.

Technical implementation success, however, was not significantly related to system quality. This finding may be because successful, operational data warehouses (as were the ones included in the study) have overcome the technical problems that were encountered. If they had not overcome the most serious problems, their warehouses would not be operational. In order to understand the relationship between system quality and technical implementation success, failed warehousing projects need to be studied.

It should be noted that the R squared value for system quality (.128) suggests that like data quality, other factors not included in the research model also affect the quality of the data warehouse. Thus, the integration and flexibility of the infrastructure that data warehousing creates is also influenced by factors other than those that were considered. For example, how important is the IT infrastructure already in place in the organization? If an organization does not have internal data warehousing expertise, how important is it to bring in external consultants? How do data planning and management practices influence the system quality for data warehousing? These questions still need to be addressed.

## Implementation Factors for Data Warehousing

Management support, a champion, and resources are key ingredients to supporting the change management process in organizations. This finding is consistent with other IT implementation studies that substantiate the value of these organizational factors. A data warehouse is an expensive, enterprise-wide endeavor with significant organizational impacts. Data warehousing creates changes that resonate throughout the entire organization, and it demands broad-based and lasting support. It requires the sponsorship and support of senior management, managers in the business units, and IT. There must be a substantial initial and ongoing commitment of financial and human resources. This commitment must be made while recognizing that the greatest benefits from data warehousing usually occur later rather than immediately. Together, all three organizational factors were found to be significant in the research model, and together they provide organizations with effective mechanisms for increasing widespread support for warehousing, addressing politics, and ensuring that the necessary resources are provided.

Interestingly, a champion for warehousing did not influence the project's ability to address organizational issues. Unlike decision support applications that may benefit from having a single proponent, the large scope and far-reaching impact of data warehousing appears to require broad-based support from multiple sources. A single warehouse champion may abandon the project at the first sign of trouble (Watson et al. 1999) and has limited influence and understanding outside his or her own area of the organization. Likewise, grass-roots support may not be sufficient for implementation success. Although studies have found that user participation can help manage user expectations, this may not be sufficient for the acceptance of a warehouse within the organization. All of these findings highlight some of the challenges that managers should expect when working with a warehouse initiative. An organization that has successfully rolled out applications in the past cannot assume that a data warehouse can be introduced with the same levels of sponsorship and resources.

According to the findings, having resources, appropriate people on the project team, and user participation have positive effects on the project's outcome. Unfortunately, companies sometimes experience problems in these areas. Warehousing demands a large financial investment that can be difficult to sell to management without having guaranteed up-front tangible benefits. Currently, the demand for experienced warehousing personnel exceeds the supply. Many companies have little choice but to staff from within, independent of whether their staff have appropriate experience. As a result, the data warehousing staff may have little or no experience in how to plan for and manage a project of this type. User participation also can be challenging because the needs of many, diverse internal groups (e.g., marketing, production) must be understood and communicated to the project team. Much data warehousing literature advocates an incremental approach when building a warehouse, which means building a warehouse in three- to six-month increments that each deliver substantial value to the business. In this way, project teams can work toward goals that are more manageable in size, users can participate in only relevant parts of the project, and management can be satisfied that the project is delivering value. If management requires postimplementation assessments of its investments, the value that is created during beginning increments can be used as a foundation for a rigorous future cost-benefit analysis.

Technical factors also affect data warehousing implementations. The practitioner literature contains considerable debate over the merits of beginning a decision-support infrastructure with an enterprise-wide data warehouse versus a smallerscale data mart. The data warehouse proponents argue that data marts can quickly grow into an unintegrated collection of information silos that counter the underlying purpose of data warehousing. Data mart supporters explain that data warehouses are more expensive and difficult to construct in a reasonable amount of time. Moreover, a data mart provides a proof of concept. This study indicates that more technical problems are related to warehouses that pull from diverse, unstandardized sources, undoubtably due to the increased technical complexity. Organizations involved in building enterprise-wide data warehouses should prepare for technical obstacles that must be overcome. The development technology that is used also appears to affect the technical problems that may arise during implementation. Data warehousing requires specialized software. The project team must learn how to use this software and how to fit it into the existing technical environment.

Although the source systems and development tools are related to the technical problems that occur during the development of a warehouse, the technical problems do not have long-lasting effects that ultimately affect the benefits from operational warehouses. Likely, project teams are ultimately able to address technical problems effectively, much more so than they are able to overcome organizational and project issues. Also, as was mentioned earlier, this sample includes operational warehouses and does not contain warehouses that failed. This study does not suggest that technical problems in data warehousing are easy to overcome.

## Conclusions

There are few academic empirical studies on data warehousing. A valuable contribution of this study is the extension of the IS implementation literature through the investigation of data warehousing implementation factors. Both the IS implementation and data warehousing areas will benefit from the validation of current understandings and the development of new ideas.

The findings suggest that most of the traditional factors from the implementation literature (e.g., management support, resources) also affect the success of a data warehouse, thus providing further evidence of the existence of a common set of IT implementation factors. However, the study also shows that implementation success models cannot be used to investigate data warehousing without some modification. For example, other factors were needed to explain the data quality and system quality for the data warehouse.

Another contribution of this study is the way in which implementation success factors can be grouped together into organizational, project, and technical success to more clearly communicate the kinds of effects implementation factors can have. This approach allowed us to tie implementation factors to system success and the benefits from the ultimate use of a system. The empirica evidence supported the idea that these connections are important to understand.

As noted previously, there has been little research on the success factors associated with infrastructure projects. Parr et al. (1999) investigated the success factors associated with ERP implementations, which can be viewed as infrastructure investments. Their list of success factors can be organized into three overarching implementation factorsóorganizational, project, and technical successówhich is the same grouping used in this study. While the specific factors in the groups vary somewhat between data warehousing and ERP, it appears that there is a macro-level model for understanding the success factors associated with infrastructure projects that can be used in future research. It is likely that the organizational factors are the most generic (e.g., management support) to implementation success. Many of the project management success factors also are probably the same. The greatest differences are most likely with the technical success factors, because the technical issues vary with the nature of the infrastructure project.

More research is required to further develop our understanding of infrastructure and determine the differences between infrastructure and application-level IT phenomenon. This study presents data warehousing as a viable way of investigating such issues. This study also challenges the notion of applying IT implementation knowledge to an infrastructure context without giving careful thought to how changes should be made.

## Acknowledgments

We would like to thank Dale Goodhue, Peter Todd, Wynne Chin, and Izak Benbasat for their helpful comments on this paper. We also are grateful to Ron Weber, Joe Valacich, and the reviewers whose comments have improved the quality of the paper substantially.

## References

Amason, A. C. ìDistinguishing the Effects of Functional and Dysfunctional Conflict on Strategic Decision Making: Resolving a Paradox for Top Management Teams,î Academy of Management Journal (39:1), 1996, pp. 123-148.

Ancona, D. G., and Caldwell, D. F. ìBridging the Boundary,î Administrative Science Quarterly (37:4), 1992, pp. 634-666.

Banker, R. D., and Kauffman, R. J. ìReuse and Productivity in Integrated Computer-Aided Software,î MIS Quarterly (15:3), 1991, pp. 375-402.

Barclay, D., Higgins, C., and Thompson, R. ìThe Partial Least Squares Approach to Causal Modeling, Personal Computing Adoption and Use as an Illustration,î Technology Studies (2:2), 1995, pp. 285-309.

Barki, H., and Hartwick, J. ìMeasuring User Participation, User Involvement, and User Attitude, MIS Quarterly (18:1), 1994, pp. 59-82.

Barquin, R. C., and Edelstein, H. Planning and Designing the Data Warehouse, Prentice Hall, Upper Saddle River, NJ, 1997.

Beath, C. M. ìSupporting the Information Technology Champion,î MIS Quarterly (15:3), 1991, pp. 355-371.

Beitler, S. S., and Leary, R. ìSearsí EPIC Transformation: Converting from Mainframe Legacy Systems to On-Line Analytical Processing (OLAP),î Journal of Data Warehousing (2:2), 1997, pp. 5-16.

Bergeron, F., and Raymond, L. "Managing EDI for Competitive Advantage: A Longitudinal Study," Information & Management (31), 1997, pp. 319-333.

Bischoff, J., and Alexander, T. Data Warehouse: Practical Advice from the Experts, Prentice Hall, Upper Saddle River, NJ, 1997.

Bollen, K. A. ìMultiple Indicators: Internal Consistency or No Necessary Relationship?î Quality and Quantity (18), 1984, pp. 377-385.

Brooks, F. P. The Mythical Man-month: Essays on Software Engineering, Addison Wesley, Reading, MA, 1975.

Chau, P. Y., and Tam, K. Y. ìFactors Affecting the Adoption of Open Systems: An Exploratory Study,î MIS Quarterly (21:1), 1997, pp. 1-24.

Chin, W. W. ìThe Partial Least Squares Approach to Structural Equation Modeling,î in G. A. Marcoulides (ed.), Modern Methods for Business Research,), Lawrence Erlbaum Associates, Mahwah, NJ, 1998, pp. 295-336.

Chin, W. W., and Frye, T. A. PLS Graph, version 2.91.03.04, Department of Decision and Information Systems, University of Houston, 1996.

Constantine, L. L. ìWork Organizations: Paradigms for Project Management and Organization,î Communications of the ACM (36:10), 1993, pp. 35-42.

Converse, J. M., and Presser, S. Survey Questions: Handcrafting the Standardized Questionnaire, Sage Publications, Newbury Park, CA, 1986.

Curtis, M. B., and Joshi, K. ìLessons Learned from the Implementation of a Data Warehouse,î Journal of Data Warehousing (3:2), 1998, pp. 12-18.

Davis, F. ìPerceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology,î MIS Quarterly (13:3), 1989, pp. 319-339.

DeLone, W. H., and McLean, E. R. ìInformation Systems Success: The Quest for the Dependent Variable,î Information Systems Research (3:1), 1992, pp. 60-95.

Devlin, B. Data Warehouse: From Architecture to Implementation, Addison Wesley Longman, Reading, MA, 1997.

Dillman, D. A. Mail and Telephone Surveys: The Total Design Method, Wiley, New York, 1978.

Duncan, N. B. ìCapturing Flexibility of Information Technology Infrastructure: A Study of Resource Characteristics and Their Measure,î Journal of Management Information Systems (12:2), 1995, pp. 37-57.

Eckerson, W. W. "Post-Chasm Warehousing," Journal of Data Warehousing (3:3), 1998, pp. 38-45.

Eckerson, W. W. Evolution of Data Warehousing: The Trend Toward Analytical Applications, The Patricia Seybold Group, April 28, 1999, pp. 1-8.

Ein-Dor, P., and Segev, E. ìOrganizational Context and the Success of Management Information Systems,î Management Science (24:10), 1978, pp. 1064-1077.

Finlay, P. N., and Mitchell, A. C. ìPerceptions of the Benefits from the Introduction of CASE: An Empirical Study,î MIS Quarterly (18:4), 1994, pp. 353-371.

Fornell, C., and Larcker, D. F. ìEvaluating Structural Equation Models with Unobservable

Variables and Measurement Error,î Journal of Marketing Research (18), 1981, pp. 39-50.

Fox, R. J., Crask, M. R., and Kim, J. ìMail Survey Response Rate: A Meta-Analysis of Selected Techniques for Inducing Response,î Public Opinion Quarterly (52), 1988, pp. 467-491.

Fraser, S. G., and Salter, G. ìA Motivational View of Information Systems Success: A Reinterpretation of DeLone and McLeanís Model,î working paper, Department of Accounting and Finance, The University of Melbourne, Australia, 1995.

Garrity, E. J., and Sanders, G. L. Information Success Measurement, Idea Group Publishing, Hershey, PA, 1998.

Goodhue, D. L., Quillard, J. A., and Rockart, J. F. "Managing the Data Resource: A Contingency Perspective," MIS Quarterly (12:3), 1988, pp. 373-392.

Goodhue, D. L., Wybo, M. D., and Kirsch, L. J. "The Impact of Data Integration on the Costs and Benefits of Information Systems," MIS Quarterly (16:3), 1992, pp. 293-311.

Graham, S. The Foundations of Wisdom: A Study of the Financial Impact of Data Warehousing, International Data Corporation, Toronto, 1996.

Gray, P., and Watson, H. J. Decision Support in the Data Warehouse, Prentice Hall, Upper Saddle River, 1998.

Grim, R., and Thorton, P. ìA Customer for Life: The WarehouseMCI Approach,î Journal of Data Warehousing (2:1), 1997, pp. 73-79.

Guimares, T., Igbaria, M., and Lu, M. ìThe Determinants of DSS Success: An Integrated Model, Decision Sciences (23), 1992, pp. 409-430.

Haley, B. J., Watson, H. J., and Goodhue, D. L. ìThe Benefits of Data Warehousing at Whirlpool,î Annals of Cases on Information Technology Applications and Management in Organizations (1:1), 1999, pp. 14-25.

Hartwick, J., and Barki, H. ìExplaining the Role of User Participation in Information System Use, Management Science (40:4), 1994, pp. 440- 465.

Howell, J. M., and Higgins, C. A. ìChampions of Technological Innovations,î Administrative Science Quarterly (35:2), 1990, pp. 317-341.

Hufnagel, E. M., and Conca, C. ìUser Response Data: The Potential for Errors and Biases,î Information Systems Research (5:1), 1994, pp. 48-73.

Igbaria, M., Zinatelli, N., Cragg, P., and Cavaye, A. L. ìPersonal Computing Acceptance Factors in Small Firms: A Structural Equation Model, MIS Quarterly (21:3), 1997, pp. 279-302.

Karahanna, E., Straub, D. W., and Chervany, N. L. ìInformation Technology Adoption Across Time: Cross-Sectional Comparison of Pre-Adoption and Post-Adoption Beliefs,î MIS Quarterly (23:2), 1999, pp. 183-213.

Kelly, S. Data Warehousing in Action, John Wiley & Sons, Chichester, 1997.

Kraemer, K. L., Danzinger, J. N., Dunkle, D. E., and King, J. L. The Usefulness of Computer-Based Information to Public Managers," MIS Quarterly (17:2), 1993, pp. 129-148.

Lawrence, M., and Low, G. ìExploring Individua User Satisfaction Within User-Led Development,î MIS Quarterly (17:2), 1993, pp. 195-208.

Leonard-Barton, D., and Sinha, D. K. ìDeveloper-User Interaction and User Satisfaction in Internal Technology Transfer,î Academy of Management Journal (36:5), 1993, pp. 1125-1139.

Lewin, K. Field Theory in Social Science: Selected Theoretical Papers, Harper and Brothers, New York, 1951.

Lohmoller, J.-B. ìPredictive vs. Structural Modeling: PLS vs. ML,î in Latent Variable Path Modeling with Partial Least Squares, Physica-Verlag, Heidelberg, 1989, pp. 212-55.

Lucas, H. C. Implementation: The Key to Successful Information Systems, McGraw-Hill, New York, 1981.

Lyon, J. ìCustomer Data Quality: Building the Foundation for a One-to-One Customer Relationship,î Journal of Data Warehousing, (3:2), 1998, pp. 38-47.

Maish, A. M. ìA Userís Behavior Toward His MIS,î MIS Quarterly (3:1), 1979, pp. 39-52.

Markus, M. L. ìPower, Politics, and MIS Implementation,î Communications of the ACM (26:6), 1983, pp. 430-444.

Markus, M. L., and Robey, D. ìInformation Technology and Organizational Change: Causal Structure in Theory and Research,î Management Science (34:5), 1988, pp. 583-598.

Massetti, B., and Zmud, R. W. ìMeasuring the Extent of EDI Usage in Complex Organizations: Strategies and Illustrative Examples,î MIS Quarterly, (20:3), 1996, pp. 331-345.

McConnell, S. Rapid Development Microsoft Press, Redmond, WA, 1996.

McFarlan, F. W. ìPortfolio Approach to Information Systems,î Harvard Business Review (59:5), 1981, pp. 142-159.

Melone, N. ìA Theoretical Assessment of the User-Satisfaction Construct in Information Systems Research,î Management Science (36:1), 1990, pp. 76-91.

META Group. ìIndustry Overview: New Insights in Data Warehousing Solutions,î Information Week, 1996, pp. 1-27HP.

Moore, G., and Benbasat, I. ìDevelopment of an Instrument to Measure the Perceptions of Adopting and Information Technology Innovation,î Information Systems Research (2:3), 1991, pp. 192-222.

Nunnally, J. C. Psychometric Theory, McGraw-Hill, New York, 1978.

Parr, A., Shanks, G., and Darke, P. ìIdentification of Necessary Factors for Successful Implementation of ERP Systems,î in New Information Technologies in Organizational Process, O. L. Ngwenyama, L. D. Introna, M. D. Myers, and J. I. DeCross (eds.), Kluwer Academic Publishers, Boston, 1999, pp. 99-119.

Pitt, L., Watson, R. T., and Kavan, C. B. ìService Quality: A Measure of Information Systems Effectiveness,î MIS Quarterly (19:2), 1995, pp. 173-185.

Prescott, M. B., and Conger, S. A. ìInformation Technology Innovations: A Classification by IT Locus of Impact and Research Approach,î Data Base (26: 2, 3), 1995, pp. 20-40.

Ragowsky, A., Ahituv, N., and Neumann, S. "Identifying the Value and Importance of an Information System Application," Information and Management (31), 1996, pp. 89-102.

Rainer, R. K., and Watson, H. J. ìThe Keys to Executive Information Systems Success,î Journal of Management Information Systems (12:2), 1995, pp. 83-98.

Reich, B. H., and Benbasat, I. ìAn Empirical Investigation of Factors Influencing the Success of Customer-Oriented Strategic Systems,î Information Systems Research (1:3), 1990, pp. 325- 347.

Rist, R. ìChallenges Faced by the Data Warehousing Pioneers,î Journal of Data Warehousing (2:1), 1997, pp. 63-72.

Ross, J. W., C. M. Beath, and Goodhue, D. L. ìDevelop Long-Term Competitiveness Through

IT Assets,î Sloan Management Review (38:1), 1996, pp. 31-42.

Sakaguchi, T., and Frolick, M. N. ìA Review of the Data Warehousing Literature,î Journal of Data Warehousing (2:1), 1997, pp. 34-54.

Seddon, P. ìA Respecification and Extension of the DeLone and McLean Model of IS Success,î Information Systems Research (8:3), 1997, pp. 240-253.

Seddon, P. B., and Kiew, M-Y. "A Partial Test and Development of the DeLong and McLean Mode of IS Success," in Proceedings of the International Conference on Information Systems, J. I. DeGross, S. L. Huff, and M. C. Munro (eds.), Vancouver, Canada, 1994, pp. 99-110.

Seddon, P., Staples, S., and Patnayakuni, R. ìDimensions of Information Systems Success,î Communications of the AIS (2:20), 1999.

Shanks, G., and Darke, P. ìA Framework for Understanding Data Quality,î Journal of Data Warehousing, (3:3), 1998, pp. 46-51.

Steinbart, P. J., and Nath, R. "Problems and Issues in the Management of International Data Communications Networks: The Experiences of American Companies," MIS Quarterly (16:1), 1992, pp. 55-76.

Tait, P., and Vessey, I. ìThe Effect of User Involvement on System Success: A Contingency Approach,î MIS Quarterly (12:1), 1988, pp. 91-108.

Vandenbosch, B., and Huff, S. L. ìSearching and Scanning: How Executives Obtain Information from Executive Information Systems,î MIS Quarterly (21:1), 1997, pp. 81-107.

Vatanasombut, B., and Gray, P. "Factors for Success in Data Warehousing: What the Literature Tells Us," Journal of Data Warehousing (4:3), 1999, pp. 25-33.

Waldrop, J. H. ìProject Management: Have We Applied All That We Know?î Information & Management (7:1), 1984, pp. 13-20.

Wand, Y., and Wang, R. Y. ìAnchoring Data Quality Dimensions in Ontological Foundations, Communications of the ACM (39:11), 1996, pp. 86-95.

Wang, R. Y., and Strong, D. M. ìBeyond Accuracy: What Data Quality Means to Data Consumers,î Journal of Management Information Systems (12:4), 1996, pp. 5-34.

Watson, H. J., Gerard, J. G., Gonzalez, L. E., Haywood, M. E., and Fenton, D. ìData Warehousing Failures: Case Studies and Findings, Journal of Data Warehousing (4:1), 1999, pp. 44-55.

Watson, H. J., Haines, M., and Loiacono, E. T. ìThe Approval of Data Warehousing Projects: Findings from Ten Case Studies,î Journal of Data Warehousing (3:3), 1998, pp. 29-37.

Watson, H. J., and Haley, B. J. ìData Warehousing: A Framework and Survey of Current Practices,î Journal of Data Warehousing (2:1), 1997, pp. 10-17.

Wetherbe, J. C. ìExecutive Information Requirements: Getting It Right,î MIS Quarterly (15:1), 1991, pp. 51-66.

Wold, H., and Joreskog, K. Systems Under Indirect Observation: Causality, Structure, Prediction, Volume 2, North-Holland, Amsterdam, 1982.

Wybo, M. D., and Goodhue, D. L. ìUsing Interdependence as a Predictor of Data Standards: Theoretical and Measurement Issues,î Information & Management (29:6), 1995, pp. 317-330.

Yoon, Y., Guimares, T., and O'Neal, Q. ìExploring the Factors Associated with Expert Systems Success,î MIS Quarterly (19:1), 1995, pp. 83- 106.

## About the Authors

Barbara H. Wixom is an assistant professor of Commerce at the University of Virginiaís McIntire School of Commerce. She received her Ph.D. in MIS from the University of Georgia. Dr. Wixom was made a Fellow of The Data Warehousing Institute for her research in data warehousing. She has published in journals that include MIS Quarterly, Information Systems Research, Communications of the ACM, and Journal of Data Warehousing. She has presented her work at national and international conferences.

Hugh J. Watson is professor of MIS and holds the C. Herman and Mary Virginia Terry Chair of Business Administration in the Terry College of Business at the University of Georgia. He specializes in the design of information systems to support decision making. Dr. Watson is the author of over 100 articles and 22 books, including Decision Support in the Data Warehouse (Prentice-Hall, 1998). He is the Senior Editor of the Journal of Data Warehousing and is a Fellow of The Data Warehousing Institute.
