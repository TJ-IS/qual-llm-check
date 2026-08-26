---
otero_id: 5430
otero_key: "CEG5PPV9"
title: "Inverse Transparency and the Quest for Empowerment through the Design of Digital Workplace Technologies"
authors: "Maren Gierlich-Joas; Abayomi Baiyere; Thomas Hess"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00879"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# Inverse Transparency and the Quest for Empowerment thr     ough the Design of Digital Workplace Technologies

Maren Gierlich-Joas , mg.digi@cbs.dk

Abayomi Baiyere Queen's University / Copenhagen Business School / MIT Center for Information Systems Research, a.baiyere@queensu.ca

Thomas Hess , thess@lmu.de

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Inverse Transparency and the Quest for Empowerment through the Design of Digital Workplace Technologies

Maren Gierlich-Joas,<sup>1</sup> Abayomi Baiyere,<sup>2</sup> Thomas Hess<sup>3</sup>

<sup>1</sup>Department of Digitalization, Copenhagen Business School, Denmark, Mg.digi@cbs.dk <sup>2</sup>Smith Business School, Queen’s University, Canada / Copenhagen Business School, Denmark / MIT Center for Information Systems Research, USA a.baiyere@queensu.ca <sup>3</sup>Institute for Digital Management and New Media, LMU Munich School of Management, Germany, thess@lmu.de

## Abstract

Digital workplace technologies lead to increasing levels of transparency. This, however, can invoke tensions: On the one hand, transparency facilitates employee empowerment, and on the other hand, transparency drives employee surveillance and privacy concerns. Furthermore, transparency has traditionally been one-sided, with control vested in managers, leading to a panoptical scenario. The contemporary workforce demands empowerment and bidirectional, inverse transparency, which challenges the assumptions of agency theory. These tensions are pertinent challenges that are even more salient today. Following a design science research process, we examine how a technica solution could be designed to mitigate these tensions and overcome the panopticon. Drawing on the knowledge base of stewardship theory and the concept of inverse transparency, we derive design requirements, design principles, and design features for an artifact that instantiates inverse transparency and drives the movement to stewardship behavior. We develop three theoretical conjectures on the artifact’s implications on kernel theory and conclude by advancing a design theory on inverse transparency that guides the design of digital workplace technologies. Lastly, our study illuminates the emerging understanding of transparency-related challenges in the contemporary workforce and further contributes to the discourse with theoretical and design knowledge.

Keywords: (Inverse) Transparency, Digital Workplace Technologies, Stewardship Theory, Design Science Research

René Riedl was the accepting senior editor. This research article was submitted on February 24, 2022 and underwent three revisions.

## 1 Introduction

Digitalization is impacting numerous facets of our daily lives, including the workplace (Baskerville et al., 2020). Digital workplace technologies, such as smart agents and analytics technologies, are not a new phenomenon, but the extent of their usage has been triggered by technological advances and changing market demands—for example, the need for remote work (Faraj et al., 2021). According to market overviews by Gartner Research, companies are leveraging increasing amounts of digital trace data from digital workplace technologies, such as Microsoft 365 applications, process mining tools, and employee surveys (Moore, 2020).

The ongoing use of digital workplace technologies is causing companies to experience certain benefits but also severe risks (Baptista et al., 2020; Zimmer et al., 2023). On the one hand, these technologies offer tools to facilitate collaboration and idea generation (Van Osch et al., 2023) and bridge distances between members of virtual teams (Baptista et al., 2020). Thus, the use of digital workplace technologies such as people analytics is increasing transparency, efficiency, and fairness (Giermindl et al., 2021). On the other hand, especially if they are driven by artificial intelligence, they present challenging issues for management (Berente et al., 2021). Unintended nudging, algorithm opacity, and datafication are among the threats of digital workplace technologies (Gal et al., 2020; Mettler 2023, Ngwenyama et al. 2023). These technologies are also driving employee privacy concerns as employees are increasingly fearful of unauthorized data access (Bhave et al., 2020). Thus, the increased level of transparency is leading to a field of tension between employee empowerment and employee surveillance.

The prominent example of Microsoft illustrates the tightrope that managers have to navigate between employees’ data usage for monitoring versus employees’ data usage for empowerment. In October 2020, Microsoft launched the new feature Microsoft Productivity Scores to “power digital transformation with insights from Microsoft Productivity Scores” (Microsoft, 2020). Since the productivity scores contain sensitive data on employees, Microsoft has been accused of spying on employees. Only five weeks after the launch, following massive protests, Microsoft had to adjust its productivity scores significantly in December 2020 (Microsoft, 2020b). In February 2021, however, Microsoft introduced the employee experience platform Viva, replacing Scores. The solution’s value proposition was adapted slightly: Instead of providing transparency on all processes for management, Microsoft now seeks to empower employees and create more transparency (Microsoft 2021). In contrast to the initial approach, the platform has received better feedback; however, researchers have questioned if Viva leads to employees unconsciously accepting datafication as well (Ngwenyama et al. 2023). With the introduction of Microsoft Copilot, which contains AI-enabled features such as communication assistants (Microsoft, 2023), this debate will likely gain further momentum.

This recent example emphasizes the importance of welldesigned workplace technologies that overcome panoptical control—a metaphor used to describe the disciplinary power and dark side of information technology (IT) (Zuboff, 1988). This example illustrates a shift in mental paradigms for employees and managers. As recent information systems (IS) studies have highlighted, employees are demanding participation (Cortellazzo et al., 2019) and benefits from empowerment in order to reduce workers’ stress and role ambiguity (Windeler et al., 2017). These unfolding changes are challenging the traditional understanding of agency theory (Davis et al., 1997). Employees are increasingly envisioning themselves as engaged stewards instead of opportunistic agents, as postulated by agency theory (Wiener et al., 2019). If employees follow the paradigm of stewardship, this will lead to principal-steward instead of principal-agent relationships at companies, and power will have to be democratized (Hernandez, 2012). Stewardship theory captures this change in the established mental model of agency theory. However, we wish to explore how stewardship behavior can be facilitated and how this will impact the design of workplace technologies.

For the design of digital workplace technologies, a stewardship frame implies that transparency and the way it is implemented takes a key role. Transparency needs to be shared between managers and employees and data need to be democratized. The described case of Microsoft illustrates the difference between stewardship and agency: Microsoft’s Productivity Scores enhanced unidirectional transparency and surveillance and led to agency settings. In contrast, the empowerment platform Viva led to data sharing. This is an important first step to address employee needs.

However, looking beyond the Microsoft example, the problem is that current workplace technologies are built for unidirectional transparency and employee surveillance, as indicated by overviews on current market solutions (Hüllmann et al., 2021; Kalischko & Riedl, 2021; Klöpper, 2023; Tursunbayeva et al., 2018). In contrast to employees’ demands, the stewardship paradigm is not yet guiding the design of digital workplace technologies. Current contributions have problematized this imbalance (Nyman et al., 2023) and called for design-oriented research to build novel solutions for employee empowerment (Mettler, 2023). To overcome this problem, it is necessary to develop an understanding of how to foster stewardship behavior via employee behavior and novel approaches to the design of digital workplace technologies.

One solution to overcome the outlined tensions between employee empowerment and surveillance may lie in tools that foster bidirectional, inverse transparency. We consider inverse transparency to be a novel type of transparency that empowers employees to control access to data about themselves (Gierlich-Joas et al., 2020). Thus, we stress the need for a common ground between tracking uses of employee data and enabling uses. Despite its relevance to the unfolding tensions of digital technology use in the contemporary workforce, inverse transparency is a relatively new concept. Hence, there is still much to be learned about how digital technologies can be designed to enable inverse transparency and how organizations can leverage them. Finally, it is unclear how inverse transparency can facilitate stewardship. Driven by this need emerging from both practice and research, we propose the following research question:

RQ: How can inverse transparency support empowerment through the design of digital workplace technologies?

To answer the research question, we adopted a design science research (DSR) process, following Peffers et al. (2007). The research site is a software company with about 5,000 employees working in an agile manner. To develop the artifact, we started by describing the knowledge base comprising stewardship theory (ST) as kernel theory and the concept of transparency in stewardship theory. We reported our research on the technical artifact by describing three design cycles. Throughout the three iterative cycles, we verified the problem and derived design requirements (DRs). These requirements were transferred into design principles (DPs) and, finally, the design features (DFs) of the artifact. The artifact was demonstrated as a proof of concept. Next, it was evaluated as a proof of value in a summative, naturalistic manner using qualitative expert interviews and two confirmatory focus groups. We discussed our findings in the light of agency theory and stewardship theory and derived three theoretic conjectures. Furthermore, we derived a design theory on how inverse transparency can guide the development of digital workplace technologies for employee empowerment.

With this study, we contribute to the literature in the following ways: First, in accordance with Baskerville et al. (2018), the technical artifact represents a valuable contribution. Second, the derived DRs, DPs, and DFs are prescriptive knowledge for the design of digital workplace technologies that ensure employee empowerment. Third, we propose three theoretical conjectures that extend the conversation and contribute to the broader phenomenon of stewardship behavior as a requirement for inverse transparency. Furthermore, our findings challenge prior assumptions that view stewardship theory and agency theory as competing paradigms and suggest a complementary relationship between them. We draw on these knowledge contributions to formulate a design theory of inverse transparency in accordance with Gregor and Jones (2007). Finally, since we aim to solve a practical problem in this DSR study, the research has implications for practitioners seeking the right balance between securing employee data and exploring these data for employee empowerment.

## 2 Stewardship Theory as Kernel Theory

## 2.1 Foundations of Stewardship Theory

Following the idea of sociotechnical systems (Bostrom & Heinen, 1997), a technical artifact unfolds in a social system. Therefore, it is of the utmost importance to consider the social system, the established norms, and the underlying paradigm before beginning the design process. Since the artifact will impact organizational transparency and aims to support employee empowerment, the current relationship between managers and employees and the current assumptions on data sharing must be considered.

In prior literature, agency theory is a well-established lens to investigate the relationship between managers and employees. This theory defines humans as rational actors who aim to maximize their self-interest and thus follows an economics-based view (Eisenhardt, 1989). It explains the origin of information asymmetries between the two parties and outlines monitoring and signaling as a means to overcome them (Eisenhardt, 1989). Hence, agency theory postulates unidirectional transparency between managers and employees. A prominent example of an agency problem in companies is the application process, due to the information asymmetries between the applicant and the hiring team (Twyman et al., 2020). Following agency theory, increasing datafication at the workplace can be viewed as a panopticon.

However, more recently, stewardship theory has questioned the assumptions of agency theory (Davis et al., 1997) (see Table 1). Stewardship theory is based on intrinsically motivated actors who strive for higherorder needs (ST1) and identify with the workplace and its culture (ST2). Following stewardship theory, employees gain power due to expertise rather than taking a certain position (ST3) (Davis et al., 1997). Finally, stewards are interested in trusting, long-term relationships (ST4), low power distance and collectivism (ST5), and shared goals (ST6) (Davis et al., 1997).

Table 1. Comparison of Agency Theory and Stewardship Theory  
(based on Davis et al., 1997; Wiener et al., 2019)

<table><tr><td>Distinguishing factors</td><td>Agency theory (AT)</td><td>Stewardship theory (ST)</td></tr><tr><td>Motivation</td><td>Low-order needs, extrinsic motivation (AT1)</td><td>High-order needs, intrinsic motivation (ST1)</td></tr><tr><td>Identification</td><td>Low value commitment (AT2)</td><td>High value commitment (ST2)</td></tr><tr><td>Power</td><td>Institutional (AT3)</td><td>Personal (ST3)</td></tr><tr><td>Management philosophy</td><td>Coercive control, short-term orientation (AT4)</td><td>Enabling control, long-term orientation (ST4)</td></tr><tr><td>Cultural differences</td><td>Individualism, high power distance (AT5)</td><td>Collectivism, low power distance (ST5)</td></tr><tr><td>Goals of managers and employees</td><td>Goal incongruence (AT6)</td><td>Congruence with overall goals (ST6)</td></tr><tr><td>View on transparency</td><td>Direct, one-directional transparency leading to surveillance (AT7)</td><td>Inverse, bi-directional transparency leading to empowerment (ST7)</td></tr></table>

Both theories follow distinct mental paradigms, they share different cognitive structures and are usually viewed as competing logics. They present two different frames (Orlikowski & Gash, 1994) that hold certain assumptions and expectations and have been characterized as competing world views (Davis et al., 1997) based on an either-or-approach (i.e. Park et al. 2020). For the kernel theory that guides our design, we decided to use stewardship theory, as its underlying principles are in line with employee empowerment.

Prior literature suggests that employees and managers can choose between agency and stewardship relations. This can lead to incongruent or congruent frames. Since both parties choose individually, four different dynamics are possible: a mutual agency relationship, a mutual stewardship relationship, and two different dilemmas where noncoherent choices are made. In the mutual agency configurations, both parties aim to minimize agency costs by applying signaling and monitoring mechanisms (Eisenhardt, 1989). This leads to a panopticon. If managers decide on steward behavior, but employees follow agency behavior, the manager is betrayed, and we observe a control gap. If employees reversely adopt stewardship, but managers act as agents, employees are betrayed and lack empowerment. These incongruent frames are known to harm organizations’ performance (Orlikowski & Gash, 1994). In line with this argument, studies suggest that the mutual stewardship relationship maximizes potential performance and is thus the most desirable outcome (Davis et al., 1997; Torfing & Øllgaard Bentzen, 2020). At the crux of the matter is a lack of understanding on how this desirable configuration can be reached and facilitated through the use of workplace technologies.

## 2.2 Role of Transparency in Stewardship

The established mental paradigms impact how individuals perceive transparency and how they enact it. Hence, how transparency is enacted in firms is an indicator of a culture built on agency or stewardship.

Transparency is omnipresent in companies because more data is constantly becoming available (e.g. Bhave et al., 2020; Ngwenyama et al., 2023; Van Osch et al., 2023). Much employee data are only collected as a “by-product” of seeking to optimize processes—for example, trace data (Eggers et al., 2021). However, some data are collected with the explicit purpose of increasing transparency in the workforce. Thus, transparency can be defined using different modes: monitoring, surveillance, process visibility, and information disclosure (Bernstein, 2017). This study considers transparency to be the disclosure of information, especially employee data, within organizations to enhance trust and accountability. As we state in the course of this research, transparency may have different outcomes: Certain outcomes are very desirable, such as improved collaboration (Baptista et al., 2020; Van Osch et al., 2023), while others, such as employee privacy concerns, are best avoided (Tams et al., 2020; Teebken & Hess, 2021). The question is: What leads to positive or negative outcomes of transparency? How do the types of transparency differ?

We distinguish between two types of transparency, one associated with agency theory and the other with stewardship theory (see Table 1). Following frame of agency theory, most current workplace technologies lead to direct transparency. Data are often used to create transparency about work processes in order to execute control and surveillance with the goal of value appropriation. The direction of transparency is unidirectional because data flow from employees to managers. This fosters a principal-agent relationship as employees can be easily tracked by their managers in a coercive manner (Wiener et al., 2016). In contrast, we wish to investigate if in stewardship relations, transparency can be implemented as inverse transparency for the purpose of mutually empowering all stakeholders and creating trust (Gierlich-Joas et al., 2020). In this case, the flow of data would thus need to be bidirectional. This type of transparency builds on the assumptions of stewardship theory: i.e., the perspective of highly committed employees who are guided by enabling control forms.

If it is appropriately implemented, inverse transparency can thus also be understood as a measure to overcome information asymmetries and eliminate privacy concerns. If data and usage are transparent for the manager and the employee, this can enable trust, innovation, and changes to leadership concepts (Gierlich-Joas et al., 2020). Through inverse transparency, employees can not only see their own data flow but also that of their managers. They can also restrict data access and use the data to improve processes by themselves. Inverse transparency can offer a solution to agency problems because it leads to the democratization of data. We envision this type of transparency as a design requirement (DR) for our artifact and thus apply the lens of stewardship theory.

## 2.3 The Impact of Stewardship Theory on the Technical Design

Because of its underlying assumptions, we perceive stewardship theory as a suitable kernel theory to design an inverse transparency artifact. It provides a frame that examines how individuals interpret transparency. Other IS studies have applied stewardship theory as a governance model when describing users’ needs for transparency and reflexiveness (Baptista et al., 2017). Wiener et al. (2019) used stewardship theory to postulate modern control styles (Wiener et al., 2019). Benbya et al. (2021) stressed the need to consider stewardship theory when exploring artificial intelligence-enabled automation (Benbya et al., 2021).

Following the paradigm of stewardship theory not only illuminates the interaction between managers and employees but also opens up a means to investigate novel technologies “beyond controllability and explainability” (Benbya et al., 2021, p. 286).

Using stewardship theory as a kernel theory has implications for the understanding and the design of the artifact and, beyond this, for digital workplace technologies (see Figure 1). The value proposition of such technologies changes significantly. Instead of providing insights purely to the managers (Hüllmann et al., 2021; Tursunbayeva et al., 2018), employees are considered important stakeholders as well. As market reviews have highlighted, current digital workplace technologies are mainly designed to support strategic decision-making, data handling, and people management (Tursunbayeva et al., 2021). However, today, the use of such technologies needs to come with incentives and benefits for employees, even if this value proposition might conflict with the former one aimed only at managers. Aligning the interests of the different stakeholder groups becomes an important design requirement (Mettler, 2023; Nyman et al., 2023). In the following, we outline how the kernel assumptions from stewardship theory impact the design of the artifact and thus serve as a technological frame (Orlikowski & Gash, 1994).

![](/api/attachments/CEG5PPV9/fulltext/images/9d1f0f7dd24478e4b3ebf7c3a389cfdd34f269ab576682f21bef33e5ec4b00ef.jpg)  
Figure 1. Relationship of the Core Concepts and Positioning of the Work

![](/api/attachments/CEG5PPV9/fulltext/images/a66cdb4385e4381594f43938d872e5302f7cbf2377992ca84c87bb6756499231.jpg)  
Figure 2. DSR Model (Based on Peffers et al., 2007)

## 3 Design Science Research Methodology

We chose the DSR methodology to instantiate the proposed design (also see Hevner & Gregor, 2020). Kalischko and Riedl (2021) highlighted the potential of DSR studies to build artifacts beyond traditional electronic performance monitoring tools and explore their organizational embedding (Kalischko & Riedl, 2021). In the project, we followed the methodology by Peffers et al. (2007), which has been applied to solve similar research problems (e.g. Silica & Lowry, 2020). The methodology comprises six iterative phases: the identification of the problem and the motivation, the definition of the objectives of a solution, design and development, demonstration, evaluation, and communication (see Figure 2).

For the identification of the problem, we applied a scenario perspective, as suggested, for example, by Ciriello and Richter (2018). Based on qualitative interviews, we used two scenarios to describe transparency-related challenges faced by prototypical employees and managers at a partner company from the German software industry (“SoftCo” hereafter) that have meaningful consequences for the actors. These story-like scenarios set the stage for the artifact’s development. Having derived initial DRs, we used solution scenarios to illustrate how the solution can affect actors’ daily lives. Based on this, we derived DPs and DFs.

The evaluation of the artifact was guided by the framework for evaluation in design science research (FEDS) (Venable et al., 2016). We followed the “human risk and effectiveness” evaluation strategy characterized by Venable et al. (2016) because our artifact is highly user dependent, and a purely technical evaluation would not have considered the artifact’s organizational embeddedness. Because evaluation in the SoftCo environment was critical, we selected summative, naturalistic evaluation methods, such as expert interviews and focus groups, to allow users at SoftCo interact with the artifact in their everyday work life. In contrast to quantitative methods, qualitative evaluation allowed us to illuminate the phenomenon in depth and answer “why,” “how,” and “what if” questions (Benbasat et al., 1987).

## 3.1 Embedding of the Project

Our research was embedded in a three-year research project with two other research institutes: One from sociology and one from informatics. The project was examined by legal experts who evaluated the legal feasibility of the solution. As IS researchers, we assumed the role of bridging the diverse perspectives and shedding light on the sociotechnical system. The project benefitted substantially from interdisciplinary research because the topic lies at the intersection of multiple research disciplines.

Besides the academic partners, we also partnered with “SoftCo,” a German software company. SoftCo is a global player founded about 50 years ago. Two fulltime SoftCo coordinators supported us during the project. Moreover, we interacted closely with 10 employees (design team) from the company during the design phase. The design team and the research team were responsible for the development and the design of the artifact, which was developed bottom-up. The development process followed agile principles and was organized in three iterative sprints. After each sprint, we asked seven managers from different functions at SoftCo for feedback and evaluation (steering team). Besides these core players from the design team, the steering committee, and the two coordinators, we relied on additional interview partners from different departments, such as support, human resources (HR), research and development (R&D), and the workers council. Overall, we collaborated with 46 individuals.

## 3.2 Data Collection and Data Analysis

Data collection and data analysis were conducted in three iterative design cycles. The collected data are mainly qualitative, involving interviews, workshops, discussion rounds, and field observations. Before the pandemic, we performed frequent site visits with the research team. Beginning in April 2020, interactive online sessions and interviews via video-call solutions replaced these site visits. Overall, we conducted 38 semi-structured interviews, two focus group discussions, about 78 hours of extended design team meetings and observations at the company, 12 hours of steering team meetings, and 18 hours of workshops with external experts (see Table A1 in the Appendix). The accumulated transcripts consist of more than 700 pages.

For each qualitative interview, we followed the guidelines by Myers and Newman (2007) when developing the questionnaires. All interviews were semi-structured. The content of the interviews varied according to the design cycle when they were conducted because the interviews were either used to understand the problem, reevaluate our preliminary findings, or evaluate prototypes. The questions covered topics like the available data at SoftCo and their usage, existing IT infrastructure, means of work, and empowerment from the three research perspectives of sociology, informatics, and IS. Depending on the interviewee, the interview guidelines were slightly adjusted to cover role-specific topics. The interviews lasted between 30 and 120 minutes. Information on the contact persons at SoftCo can be found in Table A2.

The interviews were pretested, recorded, transcribed, and anonymized following established standards (Saldaña, 2016). For content analysis, we used the software Atlas.ti. To ensure the quality of the coding, multiple researchers were involved. We first coded inductively, before deductively aggregating the codes into categories (Gioia et al., 2013; Saldaña, 2016). The coding schemes differed depending on the design cycle but all codes stemmed from the literature and covered topics like IS success factors (DeLone & McLean, 2004), dimensions of empowerment and stewardship (Davis et al., 1997), and control styles (Wiener et al., 2019). An extract of the different coding schemes can be found in Table A3. Additional secondary data, for example newspaper articles, were added to increase validity. All direct citations in the following were translated into English.

For the focus groups, we followed the instructions in Tremblay et al. (2010). We understand focus groups to be moderated discussions involving six to 12 participants with a specific aim. In the following, we report on two

## 4 First Design Iteration

The first design cycle of the DSRM began by identifying the problem. In this initial stage, we conducted 20 semi-structured interviews with employees from support and development, managers from support and development and HR, and members of the workers’ council.

## 4.1 Setting the Stage: Digital Transformation at SoftCo

Founded about 50 years ago, SoftCo offers software solutions to worldwide clients. Although headquartered in Germany, SoftCo has offices around the world and over 5,000 employees. SoftCo’s leadership is organized in a matrix, with many departments working in an agile manner. In the data collection, we found that SoftCo was undergoing a digital transformation that was also impacting leadership and culture. The initiative began when a new CEO took over in 2018. Since then, many management positions have been reassigned, and the company’s identity has changed significantly.

We have around 700 managers at [SoftCo] who are currently doing a balancing act between the old and the new world. Until two years ago, the company was very focused on processes, approvals, reviews, and controlling. Now, a new wind is blowing. Innovations have to be built on the historical legacy. We are learning every day—according to the motto ‘not knowing it all, but learning it all.’ We also need to move away from silo thinking because only together can we become strong. To make this happen, we have more than tripled our investment in people and culture over the past 14 months. (Head of HR, archival data)

different types of focus groups: the exploratory focus group, which aims to generate ideas on a vague solution, and the confirmatory focus group, which is meant to evaluate a concrete, existing solution (Tremblay et al., 2010). We conducted both focus types of focus groups with users at SoftCo to evaluate the artifact into action. The exploratory focus group approach was used in the first design cycles, while the confirmatory focus group discussions took place in the evaluation stage. The focus groups had a designated moderator, consisting of three building blocks: (1) introduction of the topic, (2) livetesting of the artifact by the participants using guiding scenarios, and 3) a moderated discussion round. As with the interviews, the group discussions followed interview guidelines that covered the DPs we used to evaluate the artifact. The interviews and focus groups were recorded, transcribed, and analyzed using Atlas.ti (see Table A3).

## 4.2 Initial Problem Understanding: Transparency-Induced Tensions at SoftCo

Due to its industry, SoftCo company is highly digitized and works in an agile manner. Tools like Confluence (tool for collaboration), Jira (tool for agile software development), and iTrac (tool for problem tracing) form the backbone for every software-related function: “We could no longer work without these tools. Our entire process, both the development process and the maintenance process, are stored in Jira and in iTrac.” (R&D Manager, Interview 2). This setup leads to the tracing of much of the employee data.

However, sometimes SoftCo cannot exploit technologies’ potential to their full extent, for two main reasons: connectivity issues between the systems, and data privacy settings. For the connectivity issues, a manager outlined: “We have real system breaks in some processes” (R&D Manager, Interview 8). The HR department agreed with that: “In the HR environment, in particular, we have about 60 different parallel systems in use worldwide, where employee data are recorded. This is not efficient” (HR & Data Privacy Employee, Interview 11).

Moreover, privacy settings hinder unlimited use of employee data, which, on the one hand, is considered positively: “For me, the highest premise is actually the opt-in [for personal data at the workplace]. In my opinion, this is the highest premise that employees are the masters of their data” (ICT Committee Employee, Interview 13). On the other hand, managers often expressed the danger of lacking information. As a data privacy manager stated: “So, I even have the feeling that I get less data because of legal regulations than is perhaps good for me as a manager in that position” (Interview 10). The restriction of data access leads to individual workarounds: “We once had the intention to build up a skill database properly but it was rejected. So,

I have this Excel list. I don’t think the workers’ council knows about it, otherwise, I would probably have to delete it” (R&D Manager, Interview 2). Even employees expressed frustration at the lack of data usage: “In the rest of the world, data are free to use. Only German employees experience restrictions” (HR Manager, Interview 3). These restrictions on data usage are strongly impacting transparency within the organization. Software development tools, such as Jira and Confluence, are already providing a high degree of direct transparency: “Employees in the support function are completely transparent and I can find out anything about Colleague X or Y within a couple of minutes” (Workers’ Council Member, Interview 1). Despite the high level of direct transparency, bidirectional forms of transparency remain low. We observed information asymmetries. As one employee stated: “It is completely opaque for most employees what the management does with the data” (Development Employee, Interview 5). This is particularly problematic: due to SoftCo’s industry, employees and managers have high data literacy. Therefore, managers and employees expressed the need for (inverse) transparency: “Personally, I would wish for more transparency since I perceive it as a chance to engage with motivated colleagues” (Support Manager, Interview 18). “I wish we had a tool whereby all these data were accessible to all employees” (R&D Manager, Interview 2).

The initial problem interviews led to a long list of 24 initial design requirements, which were organizational, technical, and legal in nature. As these requirements were too heterogeneous and broad to define design principles, we iterated the first stage of the design cycle.

## 5 Second Design Iteration

## 5.1 Revisiting the Problem Understanding: Articulating Problem Scenarios

After the initial problem interviews, we conducted interactive workshops with 10 employees from the field of development to refine the problem. Based on these, we conceptualized two problem scenarios as syntheses of our problem understanding. For the first scenario, we focused on the employee’s point of view; for the second scenario, we took the manager’s perspective. The problem scenarios helped us bridge the gap between the problem verification and the definition of solutions.

## Problem Scenario 1: An employee wants to prepare for the annual performance review

Jonathan, a 28-year-old software developer at SoftCo, prepares for his annual performance review with his manager, Sarah. Overall, they have a very positive relationship and Jonathan values Sarah’s leadership style. He is free to choose the modes of solving a problem and he experiences trust in his work. However, he notices that during his daily programming tasks, he leaves various data traces in Jira and Confluence. Though he knows that performance tracking is prohibited by company agreement, he would like to know which data are visible to teammates and managers and how the data are used. Especially, he is interested if Sarah has looked at specific data before the performance review. With these insights, he would feel more secure to meet Sarah on an equal footing.

## Problem Scenario 2: A manager wants to plan the team’s leadership pipeline

Sarah is 42 years old and holds a management position in the development department at SoftCo. Twelve people report to her; one of them is Jonathan. Sarah fully supports the digital transformation initiative and the required change in leadership toward more empowerment. She therefore grants her employees lots of freedom. One challenge that Sarah struggles with, lies in developing a leadership pipeline and in conducting strategic HR planning for her area. Since she is not allowed to track any employee performance data, the skills of her workforce are a blind spot. Officially, she does not have any tool illustrating the expertise of the employees, nor their development directions, or performance. However, since the data are available in all systems and since Sarah holds coding capabilities, she finds workarounds, building her own dashboards. She knows that this is not desired by SoftCo and she has to invest extra time in maintaining these dashboards, but otherwise she can hardly fulfill her managerial duties.

Guided by the first problem scenario and the initial design requirements from the first cycle, we adjusted our initial design requirements and grouped them. Employees lacked crucial insights into the use of their data and feared potential misuse. Furthermore, building on the second problem scenario, we noticed that incomplete information also restricted managers’ work. Thus, in the current situation, SoftCo was building on direct but incomplete transparency. Inverse transparency could provide a solution for both problem scenarios. Consequently, we derived DR1:

## DR1: Enable inverse transparency so that employees and managers can view access to their data.

Moreover, both problem scenarios outline the clear wish for leadership that embodies stewardship theory. With intrinsically motivated employees, congruent goals, and trust, this goal is already reached to a certain extent. We, therefore, aim to cultivate self-efficacy and self-determination to facilitate stewardship behavior as both of them are drivers for stewardship behavior (Hernandez, 2012).

We thus suggest:

DR2: Facilitate employees’ self-determination.

Apart from these functional requirements, certain economic considerations have to be taken into account. The artifact’s users might conduct a cost-benefit analysis, including effort expectancy, when deciding to use the artifact (Venkatesh et al., 2003). Ultimately, ease of use is crucial: “It’s all a question of efficiency and effectiveness. If I am required to type data manually into a system, I’d do this half-heartedly. (R&D Employee, ID: 21)

## We state:

DR3: Use real-time data without generating additional effort or costs for users.

## 5.2 Defining Objectives of a Solution

To connect the problem space and the solution space, we illustrated solution approaches to the problem scenarios through solution scenarios (Ciriello & Richter, 2018). The first solution scenario addresses the employees’ perspective; the second focuses on the managers’ needs.

Solution Scenario 1: An employee wants to prepare for the annual performance review

Jonathan, a 28-year-old software developer at SoftCo, is interested in the usage of his personal data at SoftCo because he is a tech-affine person. In Jira, the tool he uses for his daily development tasks, he can access a monitor, which has different features. First, Jonathan can manage access rules according to data types, stakeholders, and time spans. He decides to grant access to his scrum team lead, Sarah, for all collected performance-based data for the last year because he believes he has nothing to hide and it can only be beneficial to him as a well-performing employee. Second, in the monitor, he can oversee all data accesses during the last week in an intuitive graph and request further details. He feels like he can own his data and that he understands for which purpose they are used. This feeling helps him a lot in trusting SoftCo, even though he uses the monitor sporadically. Having it as a safety anchor means a lot to him.

Recently, Jonathan was invited to the yearly performance review with his boss, Sarah. For this purpose, he is especially interested in the data that Sarah has retrieved. Through the monitor, he can access a self-report, which summarizes all relevant data accesses Sarah filtered for. With this report, Jonathan joins the review, feeling he can talk to Sarah with fewer information asymmetries.

Solution Scenario 2: A manager wants to plan the team’s leadership pipeline

As a manager at SoftCo, Sarah is responsible for 12 individuals. She wants to support her team members in their personal development and she wants to address their needs in a personal manner. Furthermore, she aims at optimizing her strategic planning by using reliable workforce data. Before the introduction of the inverse transparency gadget in Jira, she spent many hours configuring her own leadership dashboards, which was not in keeping with the workers’ councils regulations. Now, with the new tool, she has access to many data of her team that were shared with the individuals’ consent. In a customizable dashboard, she can oversee the workforce’s data and prepare annual performance meetings. For Jonathan, she figured out that he has a lot on his table and works extra hours because he is the only expert in his field. This led to a reduced performance and many errors that could have been avoided. To reduce his workload, she suggests training for his co-workers Tine and Matthias such that they can develop the needed capabilities. Sarah is relieved to have a professional solution to fulfill her managerial duties that has also been approved by the workers’ council.

Building on the solution scenarios, we derived DPs, which refer to rationales from prior literature. The objectives of the solution were derived via workshops at SoftCo with different stakeholders via steering committee meetings and feedback from public debates with external guests. The first DPs were derived inductively by the research team without much guidance.

To carve out the DPs with more clarity and integrate the rigor cycle, we iterated them following the guidelines by Gregor et al. (2020). We aimed to develop design principles (DPs) that would help managers and employees understand what the users should be able to do with the artifact and what characteristics the DP should possess (Gregor et al., 2020). Thus, our DPs were not intended to purely describe the user activity or the technical artifact itself but the interaction of both, following the logic of sociotechnical systems. As Gregor et al. (2020) suggest, the DP should account for the deterministic nature of the artifact but also for the intended and unintended affordances that the artifact provides when used. It should consist of the user, the aim, the context, the mechanism, the implementor, and the rationale. (Gregor et al., 2020).

DR1 is intended to enable inverse transparency. As a basis for inverse transparency, managers and employees should have access to the same data. This can be related to enabling control (ST4) as a defining characteristic of stewardship theory. Moreover, the flow of employee data should be visible. Thus, we envisioned reducing opacity, a DP that Gal et al. (2020) also articulated in the context of ethical people analytics. We found other evidence for a DP to address a similar requirement because transparency is applied to make competencies visible to the entire firm when designing a competence management system (Lindgren et al., 2004). Artifacts to assist employees in owning their data build on the assumption of intrinsically motivated employees who follow high-order needs and are interested in taking over responsibility (ST1). In sum, this approach is congruent with enabling control styles and fosters stewardship behavior (Gierlich-Joas et al., 2021; Hernandez, 2012; Wiener et al., 2019). We derived DP1 and DP2 to realize DR1:

DP1: For managers in the context of software development, to allow employees to benefit from their data, similar data should be made accessible within teams and across departments, which is congruent with Davis et al.’s (1997) stewardship theory. (ST1 and ST4)

DP2: To allow data owners to comprehend the usage of their data in the context of software development, organizations should make the flow and the use of employee data visible, because this will lead to intrinsic motivation and enabling control. (ST1 and ST4)

DR2 is intended to facilitate self-determination. This DP has been implemented in numerous privacy-bydesign studies seeking to avoid manipulative nudges in people analytics (Gal et al., 2020) and implement options for user control (Lindgren et al., 2004). Zieglmeier and Pretschner (2021) articulated a similar concept, enabling data sovereignty through trustworthy transparency by design. Moreover, Lindgren et al. (2004) suggested flexible reporting. Finally, following stewardship theory as a rationale, self-determination drives stewardship behavior (Hernandez, 2012). To facilitate empowerment, the technical artifact must be customizable to the individual’s needs:

“Everyone works in different ways. Thus, each employee should be able to take [from the tool] what he needs for his job.” (R&D Manager, Interview 17)

I don’t like working with ready-made dashboards; I prefer building my own “traffic light system.” (R&D Manager, Interview 4)

These articulated design requirements can be related to certain dimensions of stewardship theory. The quotes express that the employees are intrinsically motivated (ST1) and that they demand power due to their personal experience and skills instead of their institutionally legitimated roles (ST3). They aim to enable control (ST4) and seem to have a low power distance (ST5) in their requests for the democratization of power. We therefore aimed to address DR2 with DR3 and DR4 in congruence with Davis et al.’s (1997) stewardship theory:

DP3: Managers in the context of software development should facilitate employees’ decisions regarding who should be able to access their data via transparency by design. (ST1, ST4, and ST5)

DP4: To allow employees to benefit from their data, organizations in the context of software development should support customizable dashboards as visualizations of internal data such that users can select individual key performance indicators (KPIs) and adapt the system to their needs. (ST3 and ST4)

To realize DR3, i.e., the use of real-time data without additional efforts or costs, we noticed similar approaches in Lindgren et al. (2004) who built their competence management system by capturing realtime knowledge from already documented knowledge and skills to avoid inconsistencies and incomplete data (Lindgren et al., 2004). This approach is congruent with Rivera et al. (2021), who investigated the benefits of direct feedback, which relies on real-time data. On a more general level, offering a solution without any extra costs or required efforts is in line with theories on the acceptance and use of technologies, which state that effort expectancy has an impact on use behavior (Venkatesh et al., 2003). This requirement cannot be linked to stewardship theory but it extends the perspective. We thus articulate DP5:

DP5: For implementers in the context of software development firms, existing data sources from the company should be integrated such that users do not have to adjust their data manually and data inconsistencies can be avoided, because this increases the artifact’s acceptance rate (Venkatesh et al., 2003).

The relation between DRs and DPs is illustrated in Figure 3.

## 5.3 Design and Development

In the next step, we derived DFs, which describe means to implement a DP in an actual artifact (Walls et al., 1992). While the DPs were still generic, the DFs were implemented in a specific artifact at SoftCo. Prior to the design phase, we collaborated within the research team and collected data via interviews and observations. The collaboration intensified in the design phase because we worked in agile sprints together with two design teams from SoftCo consisting of five employees each. The workshops were conducted in a virtual and interactive manner using collaboration tools. We were able to use a mirror system with data from SoftCo and were therefore able to work with real use cases. Additional data were collected in the steering committee meetings.

When developing the artifact, we followed the two problem scenarios as a guideline. In addition to the DFs presented below, the design teams derived various use cases and distinct artifacts. However, in this study, we focused on the presentation of the core artifact that facilitated inverse transparency between managers and employees.

![](/api/attachments/CEG5PPV9/fulltext/images/411f111947718c66cbb3e30a78ad96fbfeedbb7120ac7008975555bdf83f6516.jpg)  
Figure 3. Relation between Design Requirements, Design Principles, and Design Features (Based on Gierlich-Joas et al., 2021)

![](/api/attachments/CEG5PPV9/fulltext/images/a66917aa8c045fb470382e7b91df82073fae3c434821afa97ca1fd20716cb324.jpg)  
Figure 4. Technical Architecture of the Artifact

For the data source, we relied on the SQL Server at SoftCo to use real data. The main data source was the issue ticketing system Jira, which was mentioned in the problem interviews and problem scenarios. Issues in Jira represent work items created by and assigned to individuals. Collaborators can comment on the issues and work on them together. In the process, various data trails are collected on individual collaborators. This data can be accessed via dashboard plugins. Our artifact is an additional dashboard plugin we are developing for Jira using the real-time data at SoftCo.

On the architectural level, Figure 4 visualizes how the DPs were implemented. The interaction with the artifact can be described as follows: Once a data user (e.g., Sarah) requests a datum from the data source (Jira), this is observed by the Monitor. The Monitor is a gatekeeping tool behind the Jira dashboard that retrieves the access information from the Overseer component, which stores each data owner’s privacy settings. If the datum is consented to for processing, the data user can access the data. The Monitor logs and stores the usage at the Overseer. Data owners (e.g., Jonathan) can retrieve this usage information via the interface “Watch the watcher” (see Figure 4).

Next, the DPs were broken down into specific features of the solution. To realize DP1, similar data have to be accessible to everyone. The option to search for data about processes and employees across different teams and departments appears to be crucial. Following the idea of Problem Scenario 1, employees generally want to know which data were accessed. We thus derived DF1:

DF1 (realizing DP1): Implement an expert search function as a dashboard plug-in in Jira to find colleagues based on topics they work on (Jira ticket system as underlying data source).

These expert search functions and dashboard gadgets were implemented in the artifact via a display app, a single-page web application serving as the front-end for the user. This is the only part of the artifact that the users see; the back-end parts are described below.

To realize DP2, a plugin for monitoring data accesses on different data sources must be implemented. The monitor is helpful in overseeing data flows (DR2), but can also enhance transparency by design (DR3) because individuals can restrict data access for certain user roles, time spans, or data types. This option would be appealing to employees like Jonathan because data are being democratized and the ownership of these data is vested in the employee. We thus propose:

DF2 (realizing DP2 and DP3): Enable the monitoring of data accesses in the Jira back-end related to the expert search via a single-page app (JavaScript) in the monitor.

DF3 (realizing DP3): Include an option for the data owner to adjust access policies in the monitor for specific persons, periods, and data types such that the individual is not displayed in the expert search.

These design features were implemented in the artifact as a plug-in for Jira. Every time data are requested from the Jira API, the monitor reports this to the data subject. Thereby, the flow of the data becomes transparent (DP2) and transparency can be designed by the individual data subject (DP3) (see Figure 5).

We also had to address Problem Scenario 2 where Sarah, the scrum master, struggled to use the workforce efficiently because she lacked crucial insights. She wanted customizable dashboard gadgets, for example, on performance data. With this DF, we addressed DP4. Moreover, by offering customizable dashboard gadgets in Jira, we also realized DP1 and DP5:

DF4 (realizing DP1, DP4, and DP5): Provide customizable drag & drop dashboard plug-ins for Jira consisting of a Java back-end and a JavaScript front-end such that users can configure their dashboards.

![](/api/attachments/CEG5PPV9/fulltext/images/01bf545d6faf78b3c55c143bca6bebbe29a614ae5dc269d158d28d864332ee84.jpg)  
Figure 5. Technical Artifact

This DF was embedded in the artifact by providing different filter options in the front-end display app. The user can decide on the KPIs and topics to filter for which supports employees’ ownership.

Lastly, existing data should be used (DP5) to avoid redundancies, additional effort, and costs (DR5). At the moment, Sarah is struggling with inefficiencies because she has to build the dashboards by herself. This individual solution is also not in keeping with the guidelines of the workers’ council. Since many processes are already digitized and various systems collect data, it is necessary to make use of application programming interfaces (APIs). We propose:

DF5 (realizing DP 5): Use Jira APIs once data is requested in the expert search such that the artifact can be embedded in the Jira platform.

In our context, we used the Jira API to access different data sources. The advantage of Jira is that it reports all data in real time without manual effort.

## 5.4 Demonstrating the Artifact

In the demonstration phase, we first showed that the artifact can solve one or more specific instantiations of the problem. As the first proof of concept was successful, we followed the “human risk & effectiveness” pathway described by Venable et al. (2016) and moved toward a summative, naturalistic setting within the organizational context. We demonstrated the artifact three times in the steering committee meetings at SoftCo using realistic use cases. The seven managers provided us with their feedback, which we used for the next design cycle.

Next, we evaluated the feedback more formally via focus groups and interviews. For the formal demonstration, we first relied on nine semi-structured qualitative interviews with the employees from the design teams. In the 1:1 interviews, we demonstrated the artifact in a think-aloud fashion. This approach provided space for participants to share their impressions during the usage and their thoughts on the advantages and disadvantages of the solution. The interviews were transcribed and coded. The focus groups with the design teams had a designated moderator and covered three building blocks: (1) a brief introduction to the topic, as the teams were already very involved; (2) a brief interaction to the artifact; and (3) a moderated discussion round. The feedback we received was mostly positive and focused on minor technical issues.

Overall, the technical proof of concept was successful and the features worked correctly. We learned that the artifact was “intuitive,” “comprehensive,” and “easy to use” (Focus Groups I and II): “Having 20 years of experience with Jira, there was no problem in using the artifact” (Workers’ Council Member, Focus Group I,

ID: 30). The tool helped with the self-determined handling of data because it allowed data access to be restricted.

However, certain points for improvement were discussed and can be grouped as follows:

1. Specificity of the search terms: The expert search was working. However, to conduct the search correctly, the user needed certain background knowledge. For example, the user had to be familiar with the key terms and employees’ IDs: “We apply many abbreviations that are also used in the artifact. However, it might be nice to have some kind of translation” (Support Employee, ID: 22).

2. More filter criteria: The participants requested additional filter criteria in the search function, and when displaying the results; as otherwise, they worried they might experience an information overload: “I had the impression that it didn’t work so well. I had received a long list of results with five pages” (Workers’ Council Member, Focus Group II, ID: 37). “I would wish for more specific filter options, e.g., for time and teams, in the search” (R&D Manager, ID: 26).

3. More underlying data: While the participants valued the integration of existing data sources, they drew attention to data quality because “it is extremely important that the data sources are neutral and that the tools provide an unbiased analysis” (Workers’ Council Member, Focus Group I, ID: 30). Furthermore, the participants stressed the need to integrate all data sources rather than relying on Jira only.

4. Quality of the output: Overall, the results of the search were comprehensive. However, the output list “could have been sorted for timeliness as newer experiences should gain more weight than expertise from some years ago” (Support Employee, ID: 22). Moreover, they described the applied measure of “completed issues” to filter for experts as “relevant, yet it could be more elaborate as it is a multidimensional problem to put ranking on employees” (Research Employee, ID: 23).

5. Create extensions of the artifact: In the demonstration, some participants started to brainstorm about further functionalities of similar artifacts: “An idea would be, saying: ‘Now we have the expert search but I am also interested in other transparency related issues.’” (Workers’ Council Member, ID: 24). “Something like a reverse search would be nice: I’d be interested to see who searches for which topics and get recommendations based on these meta data” (Workers’ Council Member, ID: 37).

Overall, the demonstration of the artifact via interviews and focus groups where participants interacted with the artifact resulted in mostly positive feedback. However, minor adjustments had to be integrated, so we returned to the design and development phase.

## 6 Third Design Iteration

## 6.1 Revisiting the Design and Development

The feedback from the artifact’s demonstration called for minor adjustments in the implementation of the DFs. The DPs remained unchanged. We report the changes by illustrating how we addressed the five feedback points.

For the first point, specificity of the search term, we slightly adjusted the front-end of the display app, such that not only employee IDs but also full names could be entered and displayed. For the context-specific search terms, we did not adjust the artifact, as the tool user would have sufficient knowledge to properly conduct a search.

For the second point, more filter options, we integrated a filter to restrict the time of the search.

The third point, integrate more data, triggered long discussions within the research team. We agreed that it would be great to have a holistic tool that covered every data source of SoftCo. However, we wanted to develop a very specific artifact with low projectability as a proof of concept that could potentially be transferred to other data sources in a next step after the project. Hence, we opted not to integrate more data sources in the first instantiation.

The fourth point, the quality of the output, is a main concern that we took seriously. In the front-end, we added a filter to select timely issue tickets that might indicate greater expertise in comparison to issues from previous years. Still, the question of how to measure quality and expertise apart from “number of completed issues” was challenging, as performance measures in software engineering are not very tangible. Therefore, we continued to rely on the metric of “issues completed.”

Similar to the third point, for the fifth point, we decided not to develop further extensions of the artifact. We aimed to design one specific instantiation of inverse transparency first. To our surprise, the design teams came up with distinct ideas for artifacts building on the same idea, which we could not examine in this project. However, the design teams followed up on these ideas in hackathons and ideation challenges at SoftCo, underlining their engagement and the project’s impetus for further initiatives.

## 6.2 Evaluating the Artifact

Finally, with some minor adjustments and a successful demonstration, we proceeded to evaluate the artifact at SoftCo by not only demonstrating it but by also having employees interact with it. The goal of the evaluation was to assess the artifact’s utility at SoftCo and identify desired and undesired side effects. The artifact’s utility was assessed using certain metrics. We referred to our DPs, embedded them in our kernel theory of stewardship theory with its six dimensions (motivation, identification, power, management philosophy, cultural differences, and goals of managers and employees), and used them as evaluation criteria.

We conducted two confirmatory focus groups for the evaluation of the artifact. In contrast to the steering committee and the design team members, the participants of the focus groups were mostly new stakeholders, who had not been involved in the design phase to avoid bias. The focus groups followed a similar procedure to the ones in the demonstration phase: (1) a more extensive introduction to the topic, as it was new to most participants; (2) intensive interaction with the artifact and work on realistic everyday use cases; and (3) discussion of their views on the artifact.

From a technical perspective, the evaluation of the artifact was successful, as in the prior demonstration rounds. Regarding the evaluation, we were specifically interested in the sociotechnical aspects and the actual value generated by the artifact. The feedback from the interviews and the focus groups can be summarized as follows:

DP1 was fulfilled, as we showed that employees, like managers, can benefit from their data, when they are made accessible within teams and across departments. The participants agreed that personal data is accessible at SoftCo. Therefore, they reported that they value the artifact for facilitating positive use cases with the data:

I have no reservations. I have done a lot in the history of workers’ councils and I know the concerns, but nowadays to oppose such data collection, analysis, and transparency would only be abstinence. If, as in this case, one cannot protect oneself from [data collection], then I think a transparency tool makes absolute sense. (Workers’ Council Member, Focus Group I, ID: 30)

Similar, and congruent to DP2, the flow and the usage of the data became visible.

It is possible to oversee who has accessed which data and to identify potential “stalkers.” This might not be bad intuition by my boss, but to me, it is very important to know that and that is what I can achieve with the tool. (Marketing Employee, Focus Group I, ID 33)

The managers agreed:

The benefit of the tool is that it creates a mutual basis for managers and employees, so everyone has similar information. I would never use the tool to track my employees but it would help me a lot in realizing who has too much on his or her desk and who needs to be taken care of. (Director of Globalization, Focus Group II, ID 38)

Some employees further stressed the value of the artifact:

In our case, we have personal dashboards at our boss’s. It has never been interpreted negatively, but we suspect it. That’s why it’s so interesting to know which queries my boss makes about me. Thus, that absolutely hits the use case. (HR Employee, Focus Group II, ID: 42)

These quotes are indicative of how employees became empowered and how managers used enabling control forms, which is strongly related to stewardship theory (ST1 and ST4).

Evaluating DP3, transparency by design was achieved, as employees gained the option to control data access. “It’s good and, in my opinion, this is the highest premise that must be accepted by the employer: The employee is the master of his data” (R&D Employee, ID: 13). This requirement for self-determination was realized in the artifact. However, if many employees were to decide not to share their data, the artifact’s outcome would be restricted, as these people could not be ranked as experts. Therefore, trust needs to be fostered so that employees are willing to provide their data for further analysis.

For DP4, the participants agreed that the dashboards are customizable and intuitive. “I really like the descriptions and the summaries. I would definitely keep using the tool” (Research Employee, ID: 25). However, participants expressed wishes for even more customization and expansion of the tool to generate more value. As described above, we purposefully excluded these aspects of the tool from this initial project but the participants continued working on it in hackathons afterward.

Lastly, DP5 was also met, as the data were determined to be up to date and no manual effort in data preparation was needed to run the expert search. This DP was fulfilled because the artifact was developed free of cost during a third-party-funded research project. As real-time data from Jira were used, the data did not have to be entered manually and there were no system breaks.

In sum, the DPs were successfully implemented. However, despite the positive evaluation of the DPs, the stakeholders had some contentious discussions during the proof-of-value focus group. Despite the iterative process of identifying and defining the problem through the various interviews we conducted, which highlighted the need for inverse transparency, the participants’ perceptions with regard to the artifact’s overall usefulness varied greatly. Many participants, especially managers, criticized the artifact for lacking a real use case:

I have to say: I can’t really think of any use cases for the tool. If there’s going to be inverse transparency, then I’d like to be able to see that no one is misusing my data. That’s the only thing I can think of. Not that it’s something that really bothers the employees at the moment because we have a good overall relationship of trust throughout the company. (R&D Manager, Focus Group II, ID: 36)

Similarly, a member of the workers’ council stated:

Of course, managers were looking at employee data. Why? Because they had a legitimate interest! But this vicious, classic performance and behavior control, that’s not what happens at SoftCo. Yes, I know there are exceptions. But those are really the exceptions and not the rule. (Workers Council Member, Focus Group I, ID: 1)

Summarizing the impressions, the technical implementation appeared to be fine, and the design principles were met. However, the sociotechnical embedding of the artifact revealed unexpected challenges. In the discussion, we shed light on this finding, explain underlying causes, and derive boundary conditions that must be met for the artifact to work.

## 7 Discussion

## 7.1 Explaining and Contextualizing the Findings

To make sense of the surprising evaluation and add to the knowledge outcome, we reviewed the empirical material we collected during the three years of research again. As researchers, we crafted certain affordances and opened a potential action space for users (Seidel et al., 2018). Therefore, our findings depend on users’ mental paradigms, i.e., how they interact with the artifact for inverse transparency. We closely examined the people at SoftCo and their beliefs. As Hevner et al. (2004) suggested, we especially focused on the context factors at SoftCo because they determine how the artifact interacts with the environment (Hevner et al.,

2004). In line with Baskerville et al. (2018), reflecting on the literature and questioning our data anew allowed our DSR project to provide theoretical contributions that extend the kernel theory.

Following the assumption that stewardship theory and agency theory are competing mental paradigms, we chose stewardship theory as kernel theory to inform the design of the artifact. With inverse transparency, we built on the assumption of information asymmetries existing at firms, which are only present in larger companies with clear hierarchies. The artifact’s value can best be seen in mutual stewardship relationships. With the digital transformation initiative, the mental paradigm at SoftCo moved further in the direction of stewardship theory. However, we took a closer look and examined the social system at SoftCo by referring back to the stewardship dimensions ST1-ST6 illustrated in Table 1. Ideally, these six dimensions would lean toward stewardship theory for the artifact to be applied successfully.

ST1: Regarding the motivation, we found that SoftCo’s employees and managers are highly intrinsically motivated. Especially during the pandemic, “people are super productive, almost more so than before. Communication is great, thanks in part to our collaboration tools” (Head of HR, archival data). Especially for knowledge workers in an IT company like SoftCo, intrinsic motivation is essential and many employees expressed high-order needs: “I love to tinker with the code” (Employee R&D, ID: 28). These observations suggest that the motivation at SoftCo corresponds to stewardship behavior, which can be further reinforced by inverse transparency.

ST2: We observed that employees at SoftCo have a high-value commitment and a strong identification with the company. In remote settings, which are typical for software companies, it is especially important to keep identification high: “We try to stay in touch virtually via coffee talks, sports events, and meet and greets. And we also stay very close to our people as a management team” (Head of HR, archival data). The high identification with the company is also reflected in the long tenure of many employees with SoftCo. Many employees have never worked for anyone else , which is very uncommon in the software industry. Thus, identification also aligns with stewardship theory.

ST3: Decisions are made at SoftCo by a well-educated workforce, and power is granted based on personal expertise rather than institutional rules and strict hierarchies: “Letting go, leading with trust, empowerment. Let those decide, who know the most about it” (Head of HR, archival data). This factor also reflects stewardship theory.

ST4: As a management philosophy, the head of HR envisions an enabling leadership style for the whole company: “I give a lot of trust and leave a lot of room for maneuvering and decision making” (Head of HR, archival data). Back in the spring of 2019, however, many employees shared a different opinion: “I think [empowerment] is a treasure for a company that doesn’t get lifted” (R&D Employee, Interview 7). Today, many employees still lack trust: “At least for my team, I have to say: I don’t have the trust. It would be great if this changed, but I don’t have it” (HR Employee, Focus Group II, ID: 42). Hence, the picture we derived is unclear: while some employees and managers behave and see themselves as stewards, others do not. This mismatch can potentially be amplified with inverse transparency.

ST5: With regard to cultural differences, we also have mixed impressions. For certain employees, the individualist view is more dominant: “It’s really a matter of everyone working on their own” (Support Employee, Interview 17). This also relates to the deeply rooted silo thinking that had been established within SoftCo for decades. Today, however, silos are being broken down. Despite the urge to establish team cultures, individualism is nevertheless still high— reflecting, perhaps, SoftCo’s location in Germany, which has a high individualism score (Hofstede Insights, 2021). Therefore, this dimension partly has an expression that leans partly toward stewardship and partly toward agency.

ST6: Lastly, we focused on the goal congruency between managers and employees. At SoftCo, we became acquainted with a culture deeply rooted in mutual trust: “Yes, I rely on trust. I trust the people and hope they trust me.” (R&D Employee, Interview 7). However, certain employees disagreed with the assumption of trust.

These observations and reanalysis of the data led to the insight that the philosophy has gradually shifted toward stewardship behavior through SoftCo’s ongoing digital transformation, even though agency persists in certain pockets of the organization. The psychological factors—motivation, identification, and power—are congruent with the stewardship paradigm. However, for the situational factors—philosophy, cultural differences, and goal congruency—the results are unclear, and reflections of agency theory seem to exist.

In mutual stewardship relationships, both parties trust each other. In this scenario, the inverse transparency artifact acts as a safety measure. Employees know they can check the flow and usage of their data with the artifact. However, if they trust that their manager will not misuse them, they may not feel compelled to do so, reinforcing the inherent trust dynamic of mutual stewardship.

In contrast, in mutual agent settings where both employees and managers adopt agency, the artifact can be used to increase employees’ bargaining power: “It stops people from acting like a stalker because they know there’s some control—it’s noticeable” (Technical Writer, Focus Group I, ID: 35). In this scenario, inverse transparency enables an equalizing or leveling in the agential leverage managers have over employees. This is a departure from prior thinking on mutual agency situations, which suggests that both actors will aim to minimize agency costs through monitoring mechanisms (Eisenhardt, 1989). In this scenario, there is an upending of the monitoring mechanism, with inverse transparency having the propensity to influence the prior control dynamics and power traditionally held by managers.

In mismatching situations, the artifact is not applicable as we had envisioned it because it may even increase tracking. This implies that actors operating under the stewardship paradigm would be further enabled to act opportunistically, while actors operating under the agency paradigm would be further betrayed. This is consistent with the observation that inverse transparency amplifies the existing dynamic in such contexts. Building on these observations, we propose three theoretical conjectures:

Theoretical conjecture 1: Inverse transparency reinforces prior dynamics in contexts of mutual stewardship

Theoretical conjecture 2: Inverse transparency amplifies prior dynamics between stewards and agents in contexts of mismatch

Theoretical conjecture 3: Inverse transparency equalizes prior dynamics in contexts of mutual agency

Figure 6 provides an overview of how our findings extend prior knowledge (Davis et al., 1997; Torfing & Øllgaard Bentzen, 2020) on the interaction between agency and stakeholder perspectives with inverse transparency afforded by digital workplace technology.

Based on these contextual factors, which became salient in the evaluation of our artifact, we propose a boundary condition for contextualizing the design and implementation of the artifact. The boundary condition highlights the circumstances under which the artifact and corresponding design principles can be effectively deployed.

Boundary condition: Mutual stewardship is required to effectively facilitate inverse transparency with digital workplace technologies.

![](/api/attachments/CEG5PPV9/fulltext/images/32597248ef781db7e0c293d217d2ba1582379d1232a39f8b2ebc27cca00ac683.jpg)  
Figure 6. Inverse Transparency Implications of Agent-Steward Choice Model (Extending Davis et al., 1997)

We suggest that to implement an artifact as an instantiation of inverse transparency, the organizations’ mental frame should be based on a mutual stewardship paradigm such that the artifact can be used for empowerment rather than for tracking. For the surprising results on the evaluation of the organizational artifact, we can explain that in selected cases, the present mental paradigm was not in keeping with the underlying principles of stewardship theory. This understanding enabled us to sharpen the boundary conditions for implementing digital workplace technology in facilitating inverse transparency, allowing us to contribute to knowledge that could prove useful in future design considerations of similar digital workplace technologies.

Finally, our findings go beyond the reflection upon the artifact and its implementation under defined boundary conditions. Instead, this DSR project contributes to understanding the relationship between agency theory and stewardship theory. Prior studies have conceptualized both theories as competing world views (Davis et al., 1997), following an either-or-approach (i.e. Park et al. 2020). However, our evaluation reveals that both mental paradigms can coexist within the same organization and same team, depending on situational factors. This finding challenges prior assumptions and leads to a complementary understanding of both theories.

## 7.2 Toward a Design Theory on Inverse Transparency

Gregor differentiates between five theory types—(1) theories for analyzing, (2) theories for explaining, (3) theories for predicting, (4) theories for explaining and predicting, and (5) theories for design and action (2006). In Section 7.1 we explained the results, so we offered a Type 2 theory. But the case also suggests a theory for designing an artifact—a Type 5 theory. Below, we add the following theory (see Table 2).

Design theories as part of design knowledge are a controversial topic (e.g. vom Brocke et al. 2020; Iivari 2020). While researchers agree on the importance of design knowledge as an outcome of DSR projects (e.g. Gregor & Hevner, 2013), its form can range from the situated implementation of an artifact, to constructs and models, a nascent design theory, or mid-range design theories (vom Brocke et al. 2020). Various contributions have either built upon or questioned the early work by Walls et al. (1992), which distinguishes between “design process” and “design product” when referring to design theories (e.g. Gregor & Jones, 2007; Baskerville & Pries-Heje, 2010). We adhere to the notion of design theories to explain why and how an artifact can overcome a problem that was derived in the problem space (Iivari, 2020; vom Brocke et al., 2020).

To describe the anatomy of our design theory, the eight components of a design theory by Gregor and Jones (2007) provide clarity. The purpose and scope (1) describe what the system is for. Our design theory is intended for the design of digital workplace technologies that facilitate employee empowerment through the democratization of data and the principle of inverse transparency. The constructs (2) are the representations of the entities of interest in the theory—e.g., manageremployee-relationships, digital workplaces, transparency, data democratization, and leadership approaches. The principles of form and function (3) specify the blueprint of the IS artifact—i.e., the concept of inverse transparency with its design requirements, design principles, and design features. The artifact mutability (4) describes the degree of artifact change that is encompassed by the theory. For our design theory, the instantiation of inverse transparency is realized in a modular manner (i.e., as a plug-in for the Jira software), allowing for artifact mutability. Gregor and Jones (2007) further introduced testable propositions (5) as truth statements about the design theory. Our theoretical conjectures serve this need. Justification knowledge (6) is the underlying knowledge that guides the design (kernel theories)—i.e., stewardship theory and agency theory. Moreover, the design theory is supported by the knowledge derived from the empirical material collected during the three design cycles. As optional components of a design theory, the principles of implementation (7) describe the process of implementing the design theory (Gregor & Jones, 2007). We illustrate the iterative process of developing the solution and initial insights on its implementation. Finally, for the optional expository instantiation (8)—i.e., that is the physical implementation of the artifact that can assist in representing the theory— the demonstration and evaluation of the artifact at SoftCo provide an example of what the physical implementation of the artifact might look like.

With this design theory, we articulate the design knowledge from the design process. As a result, we not only explain the observed phenomenon at SoftCo (Type 2 theory), but the design theory can help to inform the design of similar artifacts—i.e., how to do the design of digital workplace technologies for empowerment (Type 5) (Gregor, 2006).

## 7.3 Embedding the Findings in Prior Literature

Relating our findings to prior work, we build upon the state of the art of datafication technologies such as people analytics. A variety of studies have criticized digital workplace technologies for leading to employee surveillance (e.g., Giermindl et al., 2021; Ngwenyama et al., 2023). Similar to this work’s motivation, some of these studies have also used the case of Microsoft as an example to unpack the problem (Ngwenyama et al., 2023; Nyman et al., 2023). These works share the understanding of transparency as enacted onedirectionally, such that managers oversee employees’ actions. Investigating the body of research, the plethora of studies on transparency share this notion (Bernstein, 2017). This interpretation and the current design of digital workplace technologies lead to what Zuboff described as a panopticon for employees (1988).

Table 2. Design Theory for Realizing Inverse Transparency through the Design of Digital Workplaces

<table><tr><td>Component</td><td>Application</td></tr><tr><td>Purpose and scope</td><td>The design theory is intended for the design of digital workplace technologies that facilitate employee empowerment through the democratization of data and the principle of inverse transparency. This design theory provides an alternative approach besides the datafication and surveillance trends at the digital workplace.</td></tr><tr><td>Constructs</td><td>Manager-employee-relationships, digital workplaces, transparency, data democratization, leadership approaches.</td></tr><tr><td>Principle of form and function</td><td>The concept of inverse transparency with its design requirements, design principles, and design features. (See Figure 3)</td></tr><tr><td>Artifact mutability</td><td>The instantiation of inverse transparency is realized in a modular manner (i.e. a plug-in for the Jira software), allowing for artifact mutability. Due to the manifold nature of digital workplace technologies, different use cases, that all can build on the concept of inverse transparency, are envisioned.</td></tr><tr><td>Testable propositions</td><td>The concept of inverse transparency with its instantiation in an IT artifact facilitates companies to empower their employees through data democratization. This requires mutual stewardship and, in return, strengthens stewardship behavior.</td></tr><tr><td>Justification knowledge</td><td>The design theory is grounded in the kernel theories of agency theory and stewardship theory. These theories were used as a knowledge base when deriving the design requirements and design principles. Moreover, the design theory is supported by the knowledge derived from the empirical material collected during the three design cycles.</td></tr><tr><td>Principles of implementation</td><td>The implementation of the design theory is iterative. Designers can, first, develop conceptual models, and then instantiate artifacts based on the design principles.</td></tr><tr><td>Expository instantiation</td><td>The demonstration and evaluation of the artifact at SoftCo provide an example of how the implementation of the artifact might look, assisting the representation of the theory.</td></tr></table>

Moving toward a solution, some studies have derived the need for novel logics behind digital workplace technologies such that employees are empowered and data are democratized (Gierlich-Joas et al., 2020; Mettler, 2023; Nyman et al., 2023). Mettler (2023) emphasized how design-oriented approaches have the potential to shape future digital workplace technologies. Nyman et al. (2023) argued that productivity assistants can be used to help employees negotiate workloads at eye level. Both studies share the understanding of bidirectional, inverse transparency—a concept coined by Gierlich-Joas et al. (2020). However, these works are conceptual papers and while they provide a valuable knowledge base for this DSR study, they do not introduce empirical concepts. Hence, although our work needs to be seen in the context of these critical works on digital workplace technologies and transparency, it also extends the state of research.

## 8 Conclusion

Datafication at the workplace is on the rise, especially due to remote work settings triggered by the pandemic. The availability of vast employee data creates multiple opportunities but also poses challenges for companies. On the one hand, the availability of data can make decisions less error prone and can help to optimize processes. On the other hand, however, employees have expressed surveillance and privacy concerns. The panoptical scenario is more apparent than ever before. Managers often face difficulties regarding whether they can use employee data for leadership, and, if so, how. Finding the balance between tracking and empowering employees becomes a tightrope act.

In this paper, we engage with such managerial tensions at the digital workplace by answering the research question: How can inverse transparency support empowerment through the design of digital workplace technologies? Using stewardship as a theoretical lens and building on the concept of inverse transparency, we advance DPs for creating such an artifact. The design, demonstration, and evaluation of the concept highlight its potential to facilitate inverse transparency. However, the artifact needs to be implemented under suitable boundary conditions of mutual stewardship.

## 8.1 Theoretical and Design Knowledge Contributions

With this study, we contribute to knowledge in multiple ways. First, we provide a thorough design and instantiation of an artifact that engages with the problem of fostering inverse transparency. Our study presents a very tangible instantiation of inverse transparency. This artifact illustrates one option of how employee data can be used in mutually beneficial ways at the workplace. This is a very specific type of knowledge contribution to the solution space. As Baskerville et al. (2018) argued, artifacts are valuable and expected knowledge contributions of DSR projects that offer solutions to specific problem spaces (Baskerville et al., 2018).

Second, beyond providing an artifact, we derive DRs, DPs, and DFs that elevate the transferability (van Aken et al., 2016) of the knowledge generated by this study. In particular, DPs are nascent design theory contributions that are more generalizable than the artifact itself (Gregor et al., 2020). They also serve as the foundation for our derived design theory, which explains why, how, and under which conditions the artifact works. Describing the eight components of our design theory, we specify how digital workplace technologies can be designed so that they incorporate inverse transparency. Hence, next to the artifact, the design theory is a central outcome of our study. Such knowledge contributions can serve as the foundation for multiple instantiations of the concept of inverse transparency.

Third, from a theoretical perspective, we contribute to the conversation on transparency in digital workplace technologies. IS research has emphasized that risks evolve with digital workplace technologies that can lead to panoptical scenarios. In this study, we show how transparency can replace surveillance mechanisms known from agency theory. By integrating bidirectional transparency in digital workplace technologies, we illustrate a means to empower employees and mitigate the panopticon situation. Prior studies on stewardship theory have outlined several behavioral configurations at firms. However, these studies have mostly neglected the impact of transparency on stewardship relationships. This study emphasizes how inverse transparency relates to stewardship theory in two ways: Without trusting stewards, inverse transparency cannot be effectively implemented. This is one of the key takeaways from our research, as highlighted by our three theoretical conjectures. We expect that once effectively implemented, inverse transparency will be able to facilitate long-term stewardship behavior. Inverse transparency is thus a vehicle that can be used to overcome the panopticon. Furthermore, it lays the foundation for novel leadership practices in the digital age.

Furthermore, our investigation of inverse transparency enabled by a digital artifact extends prior views about the interrelation between agency and stewardship theories. Our work challenges the understanding of stewardship theory and agency theory as competing logics that occur under an either-or framework. Instead, we found evidence for both mental paradigms existing complementarily within the same organization, each serving to explain different situations. The highlighted conjectures provide stepping-stones and opportunities for future research seeking to unpack how inverse transparency reorients our thinking about agents and stewards.

Lastly, our research raises questions about the implicit assumption that is often perpetuated in the reporting of DSR studies. That is, the assumption that the evaluation of an artifact is only worth reporting if it is a success, with cases of unsuccessful evaluation implying the failure of the DSR project. Based on the experience in our study, we argue that this is not necessarily the case. While we do not advocate upholding failure cases as the gold standard for DSR projects, our study demonstrates that valuable knowledge can be gleaned from different ways in which an artifact would not function or meet its intended objectives. We argue that within such experience lies unique opportunities to contribute to knowledge about what not to do in designing artifacts in similar problem spaces. This can prevent other researchers from reinventing the wheel or repeating the same mistakes. Hence, we call for relaxing this assumption to accommodate knowledge contributions that defy our traditional expectations. As we have shown, such cases can yield illuminating knowledge just as much as successful cases.

## 8.2 Practical Implications

The study also has valuable insights for practitioners. Since workplaces have become increasingly digital and remote work settings continue to be very popular, more and more employee data are being collected. Since the tensions between tracking and empowering control mechanisms are growing, managers must find approaches that can integrate transparency in leadership. Transparency cannot be denied but has to be embraced. With the concept of inverse transparency and its instantiation in an artifact, we derive a solution that can facilitate bidirectional transparency and empower employees to work in a self-determined manner. This study sheds light on the implications for organizations culture when implementing an artifact that enhances inverse transparency. Moreover, the study illustrates levers that managers can use to strengthen stewardship behavior. Thus, inverse transparency can be seen as one facet of a broader managerial change management initiative. Empowerment can be a competitive advantage in a contested labor market and this study is a call to action for managers and HR departments.

For the designers of digital workplace technologies, especially software vendors, the study also provides guidance. Vendors for HR and management software, such as people analytics, might acknowledge the different target groups for which they develop their tools, including not only managers but also employees. These target groups have different needs and follow different paradigms (stewardship vs. agency). Therefore, the technical solutions must address different configurations at companies. For companies leaning toward stewardship relationships, we offer DPs and DFs that facilitate empowerment and thereby serve pressing employee needs. We encourage designers of similar tools to incorporate the concept of inverse transparency already in the design phase. As the example of Microsoft Productivity Scores and the Viva platform has shown, users’ acceptance is strongly impacted by early design decisions for digital workplace technologies.

## 8.3 Limitations and Outlook

Though thoroughly conducted, this study is not without limitations. The overall topic of employee tracking and empowerment is highly culture dependent. We build on the assumptions that (1) employee data are traced, (2) employees want to be empowered and share a stewardship mentality, and (3) data regulations at the workplace are relatively conservative and do not allow the use of employee data per se. These assumptions are true in the case of SoftCo. As a German software company, employee data are often already traced due to the nature of the work. Employees have high data literacy and they want to be empowered. Finally, the data regulations are relatively strict. While these assumptions may be applicable in other digital workplaces in different countries and industries, they may not hold worldwide. Using stewardship theory as a theoretical lens may have certain shortfalls.

Furthermore, mutual stewardship relations are presented as an ideal constellation. The binary choices between agents and stewards are, however, very simplistic, and, depending on the organizational context, different constellations might be desirable. From a long-term perspective, the choice between agency and stewardship is further influenced by learning experiences and the organizational context. The instantiation of inverse transparency is therefore not a one-size-fits-all solution and its projectability across companies needs to be carefully considered.

This study also has certain limitations with regard to its methodology. For the design, demonstration, and evaluation, we initially planned multiple company visits, which were not feasible because of the COVID-19 pandemic. We replaced these visits and observations with interactive video conference solutions, which received good feedback. However, the virtual setting might have caused biases. Furthermore, in line with many other DSR studies, the artifact was tested in dedicated focus groups at SoftCo. Nevertheless, the artifact’s implementation at the firm as a whole would have led to more robust evaluations.

Considering these limitations, we propose the following steps for further research. To further refine and evaluate the artifact, we suggest implementing it on a larger scale at SoftCo and investigating the interaction of the technical artifact and the organizational environment. The artifact should also be tested at companies other than SoftCo from diverse industries with different context factors to understand if and how the artifact is still applicable. Also, quantitative studies would be desirable in this context. Moreover, we highly encourage other researchers to reuse the DPs and DFs when building other instantiations of inverse transparency. Lastly, we see great potential in connecting our research to the context of digital innovation and interpreting the artifact as a digital innovation in the context of leadership comprising a technical and a social component.

## Acknowledgments

The authors wish to thank the senior editor and the reviewers for their support and guidance throughout the review process. This project was funded by the German Federal Ministry of Education and Research.

## References

Baptista, J., Stein, M.-K., Klein, S., Watson-Manheim, M. B., & Lee, J. (2020). Digital work and organisational transformation: Emergent digital/human work configurations in modern organisations. The Journal of Strategic Information Systems, 29(2), 1-10.

Baptista, J., Wilson, A. D., Galliers, R., & Bynghall, S. (2017). Social Media and the emergence of reflexiveness as a new capability for open strategy. Long Range Planning, 50(3), 322-336.

Baskerville, R., & Pries-Heje, J. (2010). Explanatory design theory. Business & Information Systems Engineering, 2, 271-282.

Baskerville, R., Baiyere, A., Gregor, S., Hevner, A., & Rossi, M. (2018). Design science research contributions: Finding a balance between artifact and theory. Journal of the Association for Information Systems, 19(5), 358-376.

Baskerville, R., Myers, M. D., & Yoo, Y. (2020). Digital first: the ontological reversal and new challenges for IS digital first: The ontological reversal and new challenges for IS research. MIS Quarterly, 44(2), 509-523.

Benbasat, I., Goldstein, D. K., & Mead, M. (1987). The case research strategy in studies of information systems. MIS Quarterly, 11(3), 369-386.

Benbya, H., Pachidi, S., & Jarvenpaa, S. L. (2021). Artificial intelligence in organizations: implications for information systems research. Journal of the Association for Information Systems, 22(2), 281-303.

Bennis, W. (2013). Leadership in a digital world: Embracing transparency and adaptive capacity. MIS Quarterly, 37(2), 635-636.

Berente, N., Seidel, S., & Safadi, H. (2021). Data-driven computationally intensive theory development. Information System Research, 30(1), 50-64.

Bernstein, E. (2017). Making Transparency transparent: The evolution of observation in management theory. Academy of Management Annals, 11(1), 217-266.

Bhave, D. P., Teo, L. H., & Dalal, R. S. (2020). Privacy at work: A review and a research agenda for a contested terrain. Journal of Management, 46(1), 127-164.

Bostrom, R. P., & Heinen, J. S. (1997). MIS problems and failures: A socio-technical perspective. Part I: The causes. MIS Quarterly, 3(1), 17-32.

Ciriello, R. F., & Richter, A. (2018). Scenario-based design theorizing. Business & Information Systems Engineering, 61(1), 31-50.

Cortellazzo, L., Bruni, E., & Zampieri, R. (2019). The role of leadership in a digitized world: A review. Frontiers in Psychology, 10, 1-21.

Davis, J. H., Schoorman, F. D., & Donaldson, L. (1997). Toward a stewardship theory of management. Academy Management Rev., 22(1), 27-49.

DeLone, W. H., & McLean, E. R. (2004). Measuring ecommerce success: Applying the DeLone & McLean information systems success model International Journal on Electronic Commerce, 9(1), 31-47.

Eggers, J., Hein, A., Böhm, M., & Krcmar, H. (2021). No longer out of sight, no longer out of mind? How organizations engage with process mininginduced transparency to achieve increased process awareness. Business & Information Systems Engineering, 63(5), 491-510.

Eisenhardt, K. M. (1989). Agency theory: An assessment and review. Academy of Management Review, 14(1), 57-74.

Faraj, S., Renno, W., & Bhardwaj, A. (2021). Unto the breach: What the COVID-19 pandemic exposes about digitalization. Information and Organization, 31(1), 1-7.

Gal, U., Jensen, T. B., & Stein, M.-K. (2020). Breaking the vicious cycle of algorithmic management: A virtue ethics approach to people analytics. Information and Organization, 30, 1-15.

Gierlich-Joas, M., Hess, T., & Neuburger, R. (2020). More self-organization, more control⸻or even both? Inverse transparency as a new digital leadership concept. Business Research, 13, 921- 947.

Gierlich-Joas, M., Zieglmeier, V., Neuburger, R., & Hess, T. (2021). Leading Agents or stewards⸻ Exploring design principles for empowerment through workplace technologies. Proceedings of the International Conference on Information Systems.

Giermindl, L. M., Strich, F., Christ, O., Leicht-Deobald, U., & Redzepi, A. (2021). The dark sides of people analytics: Reviewing the perils for organisations and employees. European Journal of Information Systems, 31(3), 410-435.

Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2013). Seeking qualitative rigor in inductive research: Notes on the Gioia methodology. Organizational Research Methods, 16(1), 15-31.

Gregor, S. (2006). The nature of theory in information systems. MIS Quarterly, 30(3), 611-642.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337-355.

Gregor, S., Chandra Kruse, L., & Seidel, S. (2020). Research perspectives: The anatomy of a design principle. Journal of the Association for Information Systems, 21(6), 1622-1652.

Hernandez, M. (2012). Toward an understanding of the psychology of stewardship. Academy of Management Review, 37(2), 172-193.

Hevner, A., March, S., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Hevner, A., & Gregor, S. (2020). Envisioning entrepreneurship and digital innovation through a design science research lens: A matrix approach. Information & Management, 59(3), Article 103350.

Hofstede Insights. (2021). Country comparison tool. https://www.hofstede-insights.com/countrycomparison

Hüllmann, J. A., Krebber, S., & Troglauer, P. (2021). The IT artifact in people analytics: Reviewing tools to understand a nascent field. Proceedings of the International Conference on Wirtschaftsinformatik.

Iivari, Juhani (2020). Editorial: A critical look at theories in design science research. Journal of the Association for Information Systems, 21(3), 502-519.

Gregor, S. & Jones, D. (2007). The anatomy of a design theory. Journal of the Association for Information Systems, 8(5), 312-335.

Kalischko, T., & Riedl, R. (2021). Electronic performance monitoring in the digital workplace: Conceptualization, review of effects and moderators, and future research opportunities. Frontiers in Psychology, 12, Article 633031.

Klöpper, M. (2023). Every break you take, every click you make—Empirical insights on employees’ perception of people analytics. Proceedings of the European Conference on Information Systems.

Lindgren, R., Henfridsson, O., & Schultze, U. (2004). Design principles for competence management systems: A synthesis of an action research study. MIS Quarterly, 28(3), 435-472.

Mettler, T. (2023). The connected workplace: Characteristics and social consequences of work surveillance in the age of datification, sensorization, and artificial intelligence. Journal of Information Technology. Advance online publication

Ngwenyama, O., Rowe, F., Klein, S., & Henriksen, H. Z. (2023). The open prison of the big data revolution: False consciousness, Faustian bargains, and digital entrapment. Information Systems Research. Advance online publication.

Microsoft (2020). Power your digital transformation with insights from Microsoft Productivity Score. https://www.microsoft.com/en-us/microsoft-365/blog/2020/10/29/power-your-digitaltransformation-with-insights-from-microsoftproductivity-score/

Microsoft (2021). Microsoft Viva: Empowering every employee for the new digital age. https://www.microsoft.com/en-us/microsoft-365/blog/2021/02/04/microsoft-vivaempowering-every-employee-for-the-newdigital-age/

Microsoft (2020b). Our commitment to privacy in Microsoft Productivity Score. https://www. microsoft.com/en-us/microsoft-365/blog/2020/12/01/our-commitment-toprivacy-in-microsoft-productivity-score/

Microsoft. (2023). Introducing Microsoft 365 Copilot— Your copilot for work. https://blogs. microsoft.com/blog/2023/03/16/introducingmicrosoft-365-copilot-your-copilot-for-work/

Moore, S. (2020). Digital workplace trends you can’t ignore. Gartner Research. https://www.gartner. com/smarterwithgartner/digital-workplacetrends-you-cant-ignore

Myers, M. D., & Newman, M. (2007). The qualitative interview in IS research: Examining the craft. Information and Organization, 17(1), 2-26.

Nyman, S., Bødker, M., & Blegind Jensen, T. (2023). Reforming work patterns or negotiating workloads? Exploring alternative pathways for digital productivity assistants through a problematization lens. Journal of Information Technology. Advance online publication.

Orlikowski, W. J., & Gash, D. C. (1994). Technological frames: Making sense of information technology in organizations. ACM Transactions on Information Systems, 12(2), 174-207.

Park, Y.K., Fiss, P, & El Sawy, O. A.. 2020. Theorizing the multiplicity of digital phenomena: The ecology of configurations, causal recipes, and guidelines for applying QCA. MIS Quarterly, 44(4), 1493-1520.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77.

Rivera, M., Qiu, L., Kumar, S., & Petrucci, T. (2021). Are traditional performance reviews outdated? An empirical analysis on continuous, real-time feedback in the workplace. Information System Research, 32(2), 1-24.

Saldaña, J. (2016). The coding manual for qualitative researchers (3rd ed.). SAGE.

Seidel, S., Kruse, L., Székely, N., Gau, M., & Stieger, D. (2018). Design principles for sensemaking support systems in environmental sustainability transformations. European Journal of Information Systems, 27(2), 221-247.

Silica, M., & Lowry, P. B. (2020). Using design-science based gamification to improve organizational security training and compliance. Journal of Management Information Systems, 37(1), 129-161.

Tams, S., Ahuja, M., Thatcher, J., & Grover, V. (2020). Worker stress in the age of mobile technology: The combined effects of perceived interruption overload and worker control. The Journal of Strategic Information Systems, 29(1), 1-10.

Teebken, M., & Hess, T. (2021). Privacy in a digitized workplace: Towards an understanding of employee privacy concerns. Proceedings of the Hawaii International Conference on System Sciences.

Torfing, J., & Øllgaard Bentzen, T. (2020). Does stewardship theory provide a viable alternative to control-fixated performance management? Administrative Science, 10(86), 1-19.

Tremblay, M. C., Hevner, A. R., & Berndt, D. J. (2010). Focus groups for artifact refinement and evaluation in design research. Communications of the Association for Information Systems, 26(27), 599-618.

Tursunbayeva, A., Di Lauro, S., & Pagliari, C. (2018). People analytics—A scoping review of conceptual boundaries and value propositions. International Journal of Information Management, 43, 224-247.

Tursunbayeva, A., Pagliari, C., Di Lauro, S., & Antonelli, G. (2021). The ethics of people analytics: risks, opportunities and recommendations. Personnel Review, 511(3), 900-921.

Twyman, N. W., Pentland, S. J., & Spitzley, L. (2020). Design principles for signal detection in modern job application systems: Identifying fabricated qualifications. Journal of Management Information Systems, 37(3), 849-874.

van Aken, J., Chandrasekaran, A., & Halman, J. (2016). Conducting and publishing design science research: Inaugural essay of the design science

department of the Journal of Operations Management. Journal of Operations Management, 47-48, 1-8.

Van Osch, W., Bulgurcu, B., & Liang, Y. (2023). Living in a fishbowl or not: The role of transparency and privacy in creative dialogues on enterprise social media. Journal of the Association for Information Systems, 24(3), 846-881.

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: a framework for evaluation in design science research. European Journal of Information Systems, 25(1), 77-89.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.

vom Brocke, J., Winter, R., Hevner, A., & Maedche, A. (2020). Special issue editorial: Accumulation and evolution of design knowledge in design science research: A journey through time and space. Journal of the Association for Information Systems, 21(3), 520-544.

Walls, J., Widmeyer, G. R., & El Sawy, O. A. (1992). Building an information system design theory for vigilant EIS. Information Systems Research, 3(1), 36-59.

Wiener, M., Mähring, M., Remus, U., & Saunders, C. (2016). Control configuration and control enactment in information systems projects: Review and expanded theoretical framework. MIS Quarterly, 40(3), 741-774.

Wiener, M., Mähring, M., Remus, U., Saunders, C., & Cram, A. W. (2019). Moving IS project control research into the digital era: The “why” of control and the concept of control purpose. Information Systems Research, 30(4), 1387-1401.

Windeler, J., Maruping, L. M., & Venkatesh, V. (2017). Systems development risk factors: The role of empowering leadership in lowering developers’ stress. Information Systems Research, 28(4), 775- 796.

Zieglmeier, V., & Pretschner, A. (2021). Trustworthy transparency by design. arXiv. https://arxiv. org/abs/2103.10769

Zimmer, M. P., Baiyere, A., & Salmela, H. (2023). Digital workplace transformation: Subtraction logic as deinstitutionalising the taken-for-granted. The Journal of Strategic Information Systems, 32(1), 101757.

Zuboff, S. (1988). In the age of the smart machine: The future of work and power. Basic Books.

## Appendix

Table A1. Overview of Data Collection and Data Use

<table><tr><td>Project phase</td><td>Cycle</td><td>Time span</td><td>Data type</td><td>Amount</td><td>Utilization</td></tr><tr><td rowspan="5">1: Identify Problem</td><td>1</td><td>Feb 2019</td><td>Thought protocol from kick-off meeting with company responsible</td><td>1</td><td>Initial understanding of the problem</td></tr><tr><td>1</td><td>May-June 2019</td><td>Interviews with different stakeholders at SoftCo</td><td>20</td><td>In-depth understanding of the problem</td></tr><tr><td>1</td><td>Aug 2019</td><td>Thought protocol from technical review at SoftCo</td><td>1</td><td>Understanding of the technical context</td></tr><tr><td>2</td><td>Jan 2020</td><td>Thought protocol from workshop on legal objectives</td><td>1</td><td>Understanding of the legal context factors</td></tr><tr><td>2</td><td>May-July 2020</td><td>Interviews with different stakeholders at SoftCo</td><td>9</td><td>Reevaluation of the problem understanding</td></tr><tr><td rowspan="4">2: Define objectives of solution</td><td>1</td><td>Oct 2019</td><td>Thought protocol from workshop with company responsible</td><td>1</td><td>Initial definition of objectives</td></tr><tr><td>1</td><td>Dec 2019</td><td>Thought protocol from presentation with all stakeholders at SoftCo</td><td>1</td><td>Refinement of objectives with different users</td></tr><tr><td>2</td><td>Feb 2020</td><td>Thought protocol from public debate</td><td>1</td><td>Enhancement of objectives by external experts</td></tr><tr><td>2</td><td>Sep 2020-June 2021</td><td>Thought protocol from steering committee meetings</td><td>3</td><td>Re-adjustment of the objectives in iterative design sprints</td></tr><tr><td rowspan="2">3: Design &amp; Development</td><td>2 &amp; 3</td><td>Sep 2020-June 2021</td><td>Through protocols from sprints with the design teams &amp; exploratory focus groups</td><td>12</td><td>Deriving of design requirements internally</td></tr><tr><td>2 &amp; 3</td><td>Sep 2020-June 2021</td><td>Thought protocol from steering committee meetings</td><td>3</td><td>Refinement of DRs, DPs and DFs</td></tr><tr><td rowspan="3">4: Demonstration</td><td>2</td><td>Sep 2020-March 2021</td><td>Thought protocol from technical tests</td><td>1</td><td>Demonstration in artificial setting (proof of concept)</td></tr><tr><td>2</td><td>Sep 2020-June 2021</td><td>Thought protocol from steering committee meetings</td><td>3</td><td>Demonstration in environment of SoftCo (proof of concept)</td></tr><tr><td>3</td><td>May 2021</td><td>Interviews and focus groups with design teams</td><td>9</td><td>Demonstration of the artifact in design teams at SoftCo</td></tr><tr><td rowspan="2">5: Evaluation</td><td>3</td><td>July 2021</td><td>Transcripts from two confirmatory focus groups</td><td>2</td><td>Ex post evaluation of the artifact with new stakeholders at SoftCo (proof of value)</td></tr><tr><td>3</td><td>July 2021</td><td>Thought protocol from retrospective with design teams</td><td>1</td><td>Evaluation of the design process and methodological learnings</td></tr></table>

Table A2. Overview of Contact Persons

<table><tr><td>ID</td><td>Role at SoftCo</td><td>Role in research project</td><td>ID</td><td>Role at SoftCo</td><td>Role in research project</td></tr><tr><td>1</td><td>Workers&#x27; council and data security</td><td>Interview partner &amp; Focus Group II</td><td>24</td><td>Workers&#x27; council</td><td>Design team</td></tr><tr><td>2</td><td>R&amp;D manager</td><td>Interview partner</td><td>25</td><td>Employee research</td><td>Design team</td></tr><tr><td>3</td><td>HR director</td><td>Interview partner &amp; steering committee</td><td>26</td><td>R&amp;D manager</td><td>Design team</td></tr><tr><td>4</td><td>R&amp;D manager</td><td>Interview partner &amp; steering committee</td><td>27</td><td>Employee support</td><td>Design team</td></tr><tr><td>5</td><td>R&amp;D specialist</td><td>Interview partner</td><td>28</td><td>Employee</td><td>Design team</td></tr><tr><td>6</td><td>R&amp;D product owner</td><td>Interview partner</td><td>29</td><td>Manager support</td><td>Design team</td></tr><tr><td>7</td><td>R&amp;D employee</td><td>Interview partner</td><td>30</td><td>Workers&#x27; council</td><td>Focus Group I</td></tr><tr><td>8</td><td>R&amp;D manager</td><td>Interview partner &amp; steering committee</td><td>31</td><td>R&amp;D employee</td><td>Focus Group I</td></tr><tr><td>9</td><td>R&amp;D product owner</td><td>Interview partner &amp; design team</td><td>32</td><td>Support employee</td><td>Focus Group I</td></tr><tr><td>10</td><td>R&amp;D team lead</td><td>Interview partner</td><td>33</td><td>Marketing employee</td><td>Focus Group I</td></tr><tr><td>11</td><td>Data security</td><td>Interview partner</td><td>34</td><td>R&amp;D employee</td><td>Focus Group I</td></tr><tr><td>12</td><td>R&amp;D employee</td><td>Interview partner</td><td>35</td><td>Technical writer</td><td>Focus Group I</td></tr><tr><td>13</td><td>ICT department</td><td>Interview partner</td><td>36</td><td>R&amp;D manager</td><td>Focus Group II</td></tr><tr><td>14</td><td>Employee quality</td><td>Interview partner &amp; steering committee</td><td>37</td><td>Workers&#x27; council</td><td>Focus Group II</td></tr><tr><td>15</td><td>R&amp;D team lead</td><td>Interview partner</td><td>38</td><td>Director globalization</td><td>Focus Group II</td></tr><tr><td>16</td><td>Employee support</td><td>Interview partner</td><td>39</td><td>Support employee</td><td>Focus Group II</td></tr><tr><td>17</td><td>R&amp;D manager</td><td>Interview partner &amp; steering committee</td><td>40</td><td>R&amp;D manager</td><td>Focus Group II</td></tr><tr><td>18</td><td>Manager support</td><td>Interview partner</td><td>41</td><td>Employee support</td><td>Focus Group II</td></tr><tr><td>19</td><td>R&amp;D employee</td><td>Interview partner</td><td>42</td><td>HR employee HR</td><td>Focus Group II</td></tr><tr><td>20</td><td>Employee support</td><td>Interview partner</td><td>43</td><td>Employee research</td><td>Coordinator</td></tr><tr><td>21</td><td>R&amp;D manager</td><td>Design team</td><td>44</td><td>Workers&#x27; council</td><td>Coordinator</td></tr><tr><td>22</td><td>Employee support</td><td>Design team</td><td>45</td><td>Workers&#x27; council</td><td>Steering committee</td></tr><tr><td>23</td><td>Employee research</td><td>Design team</td><td>46</td><td>Research coordinator</td><td>Steering committee</td></tr></table>

Table A3. Exemplary Coding Schemes from Different Project Phases

<table><tr><td>Project phase &amp; data source</td><td>Theme</td><td>Code</td><td>Exemplary code</td></tr><tr><td rowspan="6">1: Identify problem• 20 + 9 interviews with stakeholders at SoftCo</td><td rowspan="2">Meta-requirements on information quality</td><td>Completeness of the data</td><td>“It is not justifiable, this tool [Jira]. It just shows everything.” (ID: 7)</td></tr><tr><td>Freedom from bias</td><td>“A lot of employees are just also concerned about everything being reduced to a number, the number of reports they’ve processed in a day or whatever, I think that’s just the wrong measure.” (ID: 4)</td></tr><tr><td>Meta-requirements on information quality</td><td>Integration of different systems</td><td>“So I have a short list of 20 systems that should be hooked up there to make that attractive to even more employees.” (ID: 7)</td></tr><tr><td rowspan="2">Meta-requirements on organizational fit</td><td>Inverse transparency</td><td>“Well, I personally would like to see a little bit more transparency, because I see it as an opportunity to promote the employees who are willing to perform.” (ID: 20)</td></tr><tr><td>Involvement of employees</td><td>“Not only those who are now introducing it on the systems side or those who are always involved in the works council and accompany the whole process, but every single employee within the company really has to understand [the artifact].” (ID: 13)</td></tr><tr><td>Meta-requirements on legal aspects</td><td>Current legal requirements as a burden</td><td>“So I actually feel like I’m less informed due to legal requirements than might actually be good for me as a manager at that point. ... For example, I can no longer judge which employee is doing particularly well?” (ID: 10)</td></tr><tr><td rowspan="3">4: Demonstration• 9 interviews with stakeholders at SoftCo</td><td>Evaluation of DP1</td><td>Quality of the search function</td><td>“We apply many abbreviations that are also used in the artifact. However, it might be nice to have some kind of translation” (ID: 22)</td></tr><tr><td>Evaluation of DP3</td><td>Privacy assurance</td><td>“It’s good and, in my opinion, this is the highest premise that must be accepted by the employer: The employee is now the master of his data” (ID: 13)</td></tr><tr><td>Evaluation of DP4</td><td>Added value of the expert dashboard</td><td>“I really like having this description and also this brief summary. I would like working with this dashboard.” (ID: 25)</td></tr><tr><td rowspan="4">5: Evaluation• Two focus groups at SoftCo</td><td rowspan="2">Perception of artifact given the underlying management philosophy</td><td>ST4: enabling control</td><td>“I think [empowerment] is a treasure for a company that doesn’t get lifted” (ID: 7)</td></tr><tr><td>AC4: coercive control</td><td>“Of course, managers were looking at employee data. Why? Because they had a legitimate interest!” (ID: 1).</td></tr><tr><td rowspan="2">Perception of artifact given the goals of managers &amp; employees</td><td>ST6: goal congruency</td><td>“Yes, I rely on trust. I trust the people and hope they trust me.” (ID: 7)</td></tr><tr><td>AC6: goal incongruency</td><td>“At least for my team, I have to say: I don’t have the trust.” (ID: 42)</td></tr></table>

## About the Authors

Maren Gierlich-Joas is an assistant professor in the Department of Digitalization at Copenhagen Business School. She holds a PhD and MBR from Ludwig-Maximilians-Universität Munich. Her study background is in industrial engineering and she holds a BSc and MSc. from Karlsruhe Institute of Technology. In her research, she investigates digital workplace transformation using qualitative and design-oriented methods. Her work has been published in management journals and the proceedings of leading IS conferences.

Abayomi Baiyere is an associate professor at Smith Business School, Queen’s University, and an affiliate at Copenhagen Business School and MIT CISR. His research focuses on digital transformation and digital disruption. He leads the SIG DITE special interest group of the Association for Information Systems. His works have appeared in leading IS and management journals. Some of his publications have been recognized with best paper awards/nominations.

Thomas Hess is a professor of information systems and management at the Ludwig-Maximilians-Universität München (LMU), LMU Munich School of Management, where he also serves as director of the Institute for Digital Management and New Media. He is also a co-director of the Bavarian Research Institute for the Digital Transformation and a board member of the Internet Business Cluster Munich. He holds a PhD from the University of St. Gallen, Switzerland, and a Diplom degree in business informatics from the Technical University of Darmstadt, Germany. His research focuse on the potential of digital technologies for the value creation and the management of companies. His work has appeared in international journals such as MIS Quarterly, Journal of Management Information Systems, European Journal of Information Systems, Electronic Markets, and Long Range Planning. Professor Hess has also published in the proceedings of conferences such as ICIS and journals for management practice like MISQ Executive. According to Google Scholar, his work has been cited more than 26,000 times.

Copyright © 2024 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
