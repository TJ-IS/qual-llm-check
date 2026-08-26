---
otero_id: 25632
otero_key: "RC9ZK6PS"
title: "Designing financial education applications for development: applying action design research in Cambodian countryside"
authors: "Anna Zaitsev; Salla Mankinen"
year: "2022"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2021.1978341"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing financial education applications for development: applying action design research in Cambodian countryside

Anna Zaitsev & Salla Mankinen

To cite this article: Anna Zaitsev & Salla Mankinen (2022) Designing financial education applications for development: applying action design research in Cambodian countryside, European Journal of Information Systems, 31:1, 91-111, DOI: 10.1080/0960085X.2021.1978341

To link to this article: https://doi.org/10.1080/0960085X.2021.1978341

© 2021 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group.

![](/api/attachments/RC9ZK6PS/fulltext/images/7fc8f27847f28ba2b1065bb97d392a57f28730a54c62a21a8a635fbd372709d4.jpg)

Published online: 22 Dec 2021.

![](/api/attachments/RC9ZK6PS/fulltext/images/87d9206d198ba603bab69a4098ddef741c694971de1f54012ba7f92e9ace5e1c.jpg)

Submit your article to this journal

![](/api/attachments/RC9ZK6PS/fulltext/images/5c018c6e83b3507077617ba5a321e6e0c691a20f1a554aaf5375d81d5d312a0a.jpg)

Article views: 1840

![](/api/attachments/RC9ZK6PS/fulltext/images/6577a87f9fa892c1b7c46de69ed118e330e8105d8f3f94567145d755ac5aa7ab.jpg)

View related articles

![](/api/attachments/RC9ZK6PS/fulltext/images/d90208e541342dbe793bc988f6bd998cfc3051d1839c45f6888c26db94657985.jpg)

View Crossmark data

EMPIRICAL RESEARCH

∂ OPEN ACCESS

Check for updates

# Designing financial education applications for development: applying action design research in Cambodian countryside

Anna Zaitsev <sup>a</sup> and Salla Mankinen<sup>b</sup>

<sup>a</sup>The University of California, Berkeley; <sup>b</sup>Orijin

## ABSTRACT

Combining financial literacy education with technology literacy is a logical step for organisations focusing on finance-education programsin developing countries. Our study sought to foster and improve this process by exploring how design science, specifically the Action Design Research (ADR) method, could be efectively used in developing such technology. The study describes an IT development project where a small NGO-based team designed and developed a tablet application that assisted rural Cambodians in understanding and managing simple financial matters. We describe how the project applied ADR from the problem formulation to the formalisation of learning in the form of design principles that can be applied to IT projects in rural and remote locations in any developing country. We conclude our study by recommending the further use of information systems in conjunction with more traditional teaching methods, and encourage the further application of ADR and Agile methods when considering software development in the context of developing countries. This study fills a gap in the literature by combining a theoretical model with practical application for more efective learning.

ARTICLE HISTORY Received 29 September 2020 Accepted 3 September 2021

KEYWORDS ICT4D; action research design; Cambodia; financia education

## 1. Introduction

Southeast Asia is one of the fastest-developing regions globally, with accelerating growth patterns and constant technological advancements (Asian Development Bank, 2019). Among the countries experiencing significant GDP growth is the Kingdom of Cambodia. Nonetheless, the country is still struggling to address many developmental gaps, including a lack of education, poor infrastructure (Deth et al., 2016), and access to financial services such as banking and financing. However, microfinance institutions are bridging the access gap and have become an essential part of the finance economy in Cambodia (Bylander, 2016; CMA, 2016). Studies identify the sector as the developmental vehicle that drives poverty reduction, empowerment, and livelihood generation for the disadvantaged (Bylander, 2016; Chhay, 2011). Nevertheless, poor access to financial services and financial education is still an issue in remote and rural regions (Good Return, 2017). Lack of financial literacy can lead to poor business decisions and possibly a debt spiral (Bylander, 2016; Morris, 2016). As a preventive measure, financial education initiatives aim to boost financial understanding and knowledge worldwide (OECD/INFE, 2012).

Training rural Cambodians in financial literacy serves a vital role in preparing them for interactions with microfinance institutions (Good Return, 2017). Moreover, empowering local actors to take the lead in such initiatives benefits the country as a whole, potentially reducing reliance on foreign aid (Ear, 2007). Combining financial literacy with technological literacy seems a logical next step for financial educators, given the expanding prevalence of technology, especially smartphone technology (GSMA Connected Society, 2019; Phong et al., 2016).

In Cambodia, several non-governmental organisations (NGOs) support government initiatives and form an essential part of the Cambodian economic landscape (Khieng & Dahles, 2015). We studied one such organisation, Good Return, and its financial programcalled the Consumer Awareness and Financial Empowerment (CAFE) Initiative. The CAFE initiative 1 combines learner-centred, classroom-based sessions, supported by printed materials and with a little bit of technology literacy in the form of an application designed for the program, to give rural inhabitants the tools they need for dealing with microfinance institutions (Good Return, 2017, 2021).

The NGO embarked on a novel project to design and build systems for rural Cambodians (Avgerou & Walsham, 2017). Information and communications technology for development (ICT4D) research has identified that developing countries face unique challenges for software development (e.g., lack of large IT talent pool) (Mursu et al., 2003). Moreover, ICT4D studies often report negative results regarding adoption and application of software project outcomes (Yim & Gomez, 2021).

Cambodians’ issues stem from a complex historical and cultural context with diferent traditions and approaches, and examples from elsewhere may not apply (Brickell & Springer, 2016). Despite the lack of related projects to use as reference, the NGO planned similar initiatives in other countries where they operate, with an expectation that lessons learned in Cambodia would inform other work. Thus, the application had to apply generally to remote and rural locations in developing countries and allow the organisation to learn from the design and development process for future endeavours. To better achieve these goals, the organisation chose a design science approach – specifically, the Action Design Research (ADR) process (Sein et al., 2011).

ICT4D authors have suggested that software development projects could apply design science methods to create lasting efects (Gregor et al., 2014). Therefore, our research set out to respond to the following question: How does design science, specifically the Action Design Research process, inform the development of applications in rural communities within developing countries?

We responded to this question by detailing the steps for designing and developing one such application, the CAFE application (the CAFE app), a tool to support financial education. We also presented lessons learned from the process, and the generalisable outcomes (Gregor & Hevner, 2013; Sein et al., 2011).<sup>2</sup>

This introduction outlines our design project’s challenge, i.e., the lack of financial education and exposure to technology such as smartphones and smartphone applications. The remainder of the paper is structured as follows: first, we present a literature review on design-science projects conducted in developing countries and a description of Action Design Research (ADR) (Sein et al., 2011). This is followed by a description of project context and methods applied. Next, we detail the ADR steps taken and present a set of design principles derived from our study. These principles outline factors to consider when designing for rural and remote areas in developing countries. The principles are followed by a more general discussion on project outcomes. The paper concludes by detailing the contributions to theory and practice, as well as our plans for future research.

## 2. Research context

## 2.1. Design science research in the developing countries

Design science is a design-oriented research paradigm aimed at generating a product, or an artefact, with practical and theoretical utility (Baskerville, 2008; Engel et al., 2019). Based on lessons learned from building and evaluating artefacts (Vaishnavi et al.,

2004), the design scientist generates theories that can be extended beyond a single instance of an artefact (Gregor & Jones, 2007). Design research’s theoretical contributions are design theories that can range from artefact implementation situated in the design context, to nascent design theories, to more mature design theories (Gregor & Hevner, 2013). These difer from explanatory or predictive theories due to their prescriptive and evaluative approach (Baskerville, 2008). The design studies apply kernel theories that inform the construction of the IT artefact, subsequently leading to the formulation of the design theory (Gregor & Jones, 2007). The studies often follow frameworks that guide the planning, reporting, evaluating, and communicating of outcomes of design science research projects (Gregor & Hevner, 2013). The established design science paradigm is widely applied in information systems (Baskerville, 2008; Engel et al., 2019).

Some studies show the design science approach can generate exciting outcomes in developing countries. For example, a study conducted in Bangladesh described the requirements for successful tools for intervention, tools that facilitate better e-government outcomes there (Gregor et al., 2010). Another study described how designers apply participatory design to assist with the creation of distributed development settings in health information systems programs in South Africa (Titlestad et al., 2009). Similar to the Gregor et al. (2010) study, this paper also highlights the necessity of local contacts who can act as boundary spanners, mediating between diferent parties. Another study from South Africa applied design science to a project whereby researchers from several universities created a knowledge-sharing tool to enable collaboration (Van Biljon et al., 2017). This study is a good example of one that follows the suggested schema of a research design study (Gregor & Hevner, 2013). The study’s theoretical outcomes are user requirements, system features, and development principles, and the practical outcome is the artefact itself. Finally, a study based in eSwatini investigated the development of a mHealth application with the ADR method (Greve et al., 2020). This study, similar to the Van Biljon et al. (2017) study, proposes a nascent design theory captured in design requirements and corresponding design principles.

Participatory design, a practitioner-oriented design approach involving all stakeholders in the design process (Schuler & Namioka, 1993), has gained prominence (Drain et al., 2019), and some studies applying participatory design have focused on Cambodia. These papers discuss a variety of tools, ranging from prosthetic legs (Hussain et al., 2012) to mango-pickers (Drain et al., 2018), and pottery (Kang, 2016). However, these examples of design approaches involve tangible tools rather than information systems. When it comes to information systems, developed countries apply participatory design more commonly than developing countries (Byrne & Sahay, 2007). Nevertheless, the method has been making headway in ICT4D as well, especially in studies discussing the design of health information systems in countries ranging from South Africa (Byrne & Sahay, 2007) to India (Puri et al., 2009).

However, participatory design studies often lack the final steps that ADR suggests, i.e., the formalisation of the learning step or a set of design principles that would provide a generalised understanding based on the design project (Sein et al., 2011). For this reason, we turn towards the ADR method (Sein et al., 2011), a design research approach that focuses on designing practice-inspired artefacts (Pefers et al., 2018; Sein et al., 2011). ADR has strong potential as one of the methods to fill gaps in the literature and understanding of design in the ICT4D context, and it has been previously applied in the eSwatini study (Thapa & Sæbø, 2014).

## 2.2. Action design research

ADR projects consist of four stages: problem formulation; building, intervention and evaluation; reflection and learning; and formalisation of learning (Sein et al., 2011). Each stage draws on a set of principles. The first stage, problem formulation, consists of two principles: practice-inspired research and theory-ingrained artefact. Practice-inspired research means that the research outcome should be knowledge applicable to a class of problems, not just a single problem. Theory-ingrained artefact means that theories should inform the artefact created via ADR (Sein et al., 2011).

The second phase – building, intervention and evaluation (BIE) – consists of three principles: reciprocal shaping, mutually influential roles, and authentic and concurrent evaluations. Reciprocal shaping discusses the inseparable reciprocal influences of the IT artefact and the organisational context in which the artefact is created. Mutually influential roles stresses that the ADR encompasses both the theoretical knowledge of the action design researcher, and the practitioners knowledge and practical hypotheses. Concurrent evaluations suggest that the artefact should be evaluated concurrently as it is being built.

The principle of the third stage, reflection and learning, is guided emergence. By guided emergence, the creators of ADR mean that the artefact’s preliminary design is shaped by organisational use, perspectives, participants, and evaluation (Sein et al., 2011, p. 44). The principle guiding the fourth stage, formalisation of learning, is labelled as generalised outcomes. This principle states that both the problem and the artefact can be generalised, and one can derive a set of design principles based on the ADR project. Designing according to these principles should result in an IT artefact that addresses problems encountered in a specific organisation, as well as the class of problems overall. This strategy results in real system implementation as well as a set of design principles (Iivari, 2015).

We found the ADR method well suited to the design dilemma that Good Return was facing in embarking on the first phases of its CAFE initiative. Furthermore, the team felt ADR stages aligned well with the values and principles of Agile software development, a collaborative and iterative softwaredevelopment methodology championed by the lead designer at the NGO (Schwaber & Beedle, 2002), as well as the kernel theory of the CAFE application development (Gregor & Jones, 2007; Kuechler & Vaishnavi, 2008). For example, Agile software development principles advocate an open approach to changes, even later in the development, as well as continuous self-reflection by the development team (Beck et al., 2001), which aligns with the BIE stage of ADR (Sein et al., 2011).

## 3. Project context

This section details the steps of the ADR method used in the CAFE app design and development. We begin the research description by providing more background on the organisation and the educational initiative, the focus of this study. Next, we describe the role of trainers, the application’s primary user group. The section also discusses the demographic information of the learners, the secondary user group. A detailed description of the CAFE app and its main features follows.

## 3.1. Good return and CAFE initiative

Good Return, an Australian NGO, provides improved access to financial services and financial education in several countries around the Asia-Pacific region, including Cambodia, Nepal, and the Solomon Islands. The NGO has created and implemented many financial-education initiatives, aiming to reduce poverty and promote economic empowerment through education and the development of local capabilities (Good Return, 2017).

Our focus was the application-development project that accompanied the CAFE initiative. Cambodia was chosen to launch the CAFE initiative due to the strong on-site presence of Good Return in the capital, Phnom Penh.

The CAFE training initiative consisted of in-person financial capability training delivered through 20 onehour weekly sessions, targeted at rural Cambodians with limited literacy skills. The training was facilitated by the CAFE curriculum materials and the CAFE app. By CAFE curriculum, the NGO meant the structure and content of each session (i.e., lesson plans) and all supporting materials, including support for the trainers. The sessions were presented by trainers but designed by educational experts at Good Return. Good Return had partnered with the Cambodia Microfinance Association, local microfinance institutions and NGOs to ofer the program. Local bank branches provided trainers, printed materials, and hardware; Good Return provided the CAFE curriculum, design of print materials, the CAFE app, and trainers’ training.

The first stage of the program targeted the country’s poorest areas, identified by the Poverty Probability Index (Poverty Probability Index, 2021). The initial selection yielded 800 learners across 28 groups (500 graduated from the first-stage program), and six trainers in four diferent provinces across the country. The trainers often had a background in microfinance. Each learning group ranged from 15 to 30 learners. The lessons consisted of diferent learning activities such as interactive exercises, short interaction with the CAFE app, take-home challenges, and supporting resources, including booklets and printed handouts.

At the beginning of the CAFE initiative program, the second author of this paper was the leader of the technical team at Good Return, located on the Phnom Penh premises. This team consisted of the second author, a technical-support person, an e-learning specialist, and one additional technically adept member who acted as liaison between the tech team and local program trainers.

As noted, the NGO launched the CAFE initiative gradually. Figure 1 presents its high-level schedule in Cambodia. The initiative was split into several phases, beginning with two phases scheduled in different locations. Each phase allowed the designers to integrate lessons learned and examine whether different regions required any special adjustments. At the beginning of the program, it was understood that Cambodian provinces would have unique challenges and learning opportunities stemming from their locations across the country. For example, a few training locations were extremely remote and only accessible by boat, whereas provinces closer to large cities had more infrastructure and resources at their disposal.

The first phase of training took place in 2015, after which the tech team improved and enhanced the app. The second phase took place in 2016, in a new set of locations across rural Cambodia. At this stage, the first author joined the Sydney and Cambodia project to formalise lessons learned from the first two phases.

After the second phase, the CAFE program became a recurring ofering in Cambodia and a few other countries. The program began to ofer the class on finance fundamentals and a more advanced, applied version. At this writing, the global coronavirus pandemic has required temporary adjustments to the program based on the government’s COVID-19 restrictions, but it has continued throughout 2020 and early 2021.

## 3.1.1. Learner demographic data

Designing for rural learners in Cambodia began with understanding the context and demographics of intended users. By context, we mean not only the customs and culture but also a broader set of factors that influence learners’ lives. For example, it was relevant for us to understand the economic circumstances in each province, the health conditions that might afect learners, and the local infrastructure. Infrastructure includes, in the case of rural and remote locations, not only ICT infrastructure, i.e., internet and phone connections, but also roads and their condition, bridges, ferries and other waterways, and other hazards such as landmines or other dangerous relics of the past.

To get acquainted with user circumstances, the tech team visited villages in early 2015, concurrent with the first stages of app development, for discussions with local trainers and the NGO’s contacts at local organisations and institutions. Halfway through the firstphase, the tech team also helped collect a dataset from nine provinces. An afiliated NGO collected 500 completed questionnaires making up the dataset. This data provided the team with a better understanding of the target users’ context, and cognitive and physical limitations.

The data showed that most attendees were women, with farming as their primary occupation. Many learners had at least a primary-school education, but most lacked access to smartphones (see Table 1). When designing for these users, the team had to consider the lack of prior exposure to technology and work within the restrictions that the location of the farming communities might impose. In addition, the application had to function in conditions where a secure internet connection was not necessarily available.

![](/api/attachments/RC9ZK6PS/fulltext/images/baed25703888651c8521f70ab041a621f6dba5cba3a5965a4cda33c44fc913e9.jpg)  
Figure 1. The CAFE program and app development timeline.

Table 1. The learner demographics.

<table><tr><td>Learner gender</td><td></td><td>Female 87.88%</td><td>Male 12.12%</td></tr><tr><td>Age</td><td>Minimum 17 years</td><td>Maximum 99 years</td><td>Average 47 years</td></tr><tr><td>Occupation</td><td>Farming 77.32%</td><td>Home or family 18.56%</td><td>Other 4.12%</td></tr><tr><td>Marital status</td><td>Married 80.41%</td><td>Widowed 14.43 %</td><td>Single 5.15%</td></tr><tr><td>Education</td><td>No formal education 20%</td><td>Primary school 60%</td><td>Lower secondary or higher education 16%</td></tr><tr><td>Phone type</td><td>No phone 26%</td><td>Simple phone 68%</td><td>Smartphone 6%</td></tr></table>

The learners’ literacy levels and impediments were other vital factors in the design. Half of the learners were illiterate or had issues with reading and writing. Illiteracy and other impediments significantly impacted the design of the interface and features (see Table 2).

## 3.2. The CAFE application

The CAFE app was a simple application with two main features: session-attendance tracking and personalfinance tracking. The app was an add-on to the largely print-based training materials, providing some learners’ first introduction to tablet technology and software applications. The application’s objective was to add a small element of novelty to the sessions, expose learners to technology that they might encounter later in life, and support learner retention by providing an accountability tool in the attendance-tracking feature.

The tech team designed the application and developed it to work on Android tablets. The selection of these tablets was primarily due to their availability – one of the microfinance organisations collaborating with the initiative had donated them. However, one of the limitations that the tech team had to consider was that the initiative could not give a tablet to each learner; only the trainers had tablets, and they had to regulate access to the application during each training session. The lack of tablets also meant that the learners would only be exposed to the technology during the training and could not practice technology use independently. A mobile application was considered but the demographic data (see Table 1) showed that creating a mobile app would not be feasible as smartphoneownership figures were less than 10%. However, the CAFE team believed that even limited exposure could create meaningful moments of engagement, so developing an application was worthwhile. Further, with the limited number of tablets available, the trainer was always on hand to help learners with the app.

Table 2. Learner literacy skills and impediments.

<table><tr><td>Skill</td><td>No skill</td><td>Many issues</td><td>Some issues</td><td>No issues</td></tr><tr><td>Reading</td><td>29.29%</td><td>22.22%</td><td>24.24%</td><td>24.24%</td></tr><tr><td>Writing</td><td>29.29%</td><td>21.21%</td><td>25.25%</td><td>24.24%</td></tr><tr><td>Language</td><td></td><td>5%</td><td>11%</td><td>85%</td></tr><tr><td>Impediment</td><td>Significant impediment</td><td>Many issues</td><td>Some issues</td><td>No issues</td></tr><tr><td>Vision</td><td>0%</td><td>3%</td><td>38%</td><td>59%</td></tr><tr><td>Hearing</td><td>0%</td><td>0.3%</td><td>17%</td><td>83%</td></tr><tr><td>Walking</td><td>0%</td><td>0.01%</td><td>8%</td><td>92%</td></tr><tr><td>Remembering</td><td>0%</td><td>8%</td><td>34%</td><td>57%</td></tr></table>

The limited scope of the app was intentional. The app had to be very specific and contain features accessible to all users, regardless of their prior experience with software or their impediments. The application had three main features:

• Attendance: a record of attendance at a session

• Learner questionnaires: on spending, savings, reasons for missing a session (simple attendee polls)

• Capturing data (for trainers): questionnaire results, how much time users spent on the app; the speed of completing an activity

Figure 2<sup>3</sup> illustrates the first feature, the log-in screen trainers used for taking session attendance. On the first day of the training, the trainer took a photo of every learner. These photos, along with the names of the learners, were uploaded to the application database. The application created an account for each attendee. Learners accessed their account to log progress of the educational initiative. In the next session, learners could click their photos to log in. In addition to visual cues, learners could click on a speaker symbol to hear instructions in their native Khmer language.

We designed simple questions to measure learning. Responses did not require literacy skills. The learners could either read or listen to the questions, and small icons, designed to be universally understandable, guided the learners through the questions and responses. Figure 3 shows the layout of a selected set of questions and responses.

Furthermore, the application also benefitted the trainers, providing them with a way to capture data to analyse a session’s impact, and track weekly progress. Figure 4 illustrates the view of the questionnaire and the attendance data available to trainers, which is accessible via a web-based dashboard.

The development team grounded its process in the principles of Agile development (Beck et al., 2001). The Agile approach, iterative and user-centric, also aligned the development with the principles of ADR, especially the “build, intervention, evaluation” cycle (Sein et al., 2011). In short, the application development occurred in short increments. The development team held feedback sessions with key stakeholders after each new feature or significant modification, abiding by the ADR and Agile development principles.

![](/api/attachments/RC9ZK6PS/fulltext/images/022907bc7e721f7bf44880fa22154f720b669532deb49d88a0bfd3013893ded8.jpg)  
Figure 2. Learner log-in screen.

![](/api/attachments/RC9ZK6PS/fulltext/images/7537c2b0fd99f743b5f36130650eb9ef7ecdd3bbec0d6564ce6543bb77a9132b.jpg)  
Figure 3. Financial Status Questionnaire in English and Khmer.

![](/api/attachments/RC9ZK6PS/fulltext/images/af317c54948b8a5efa6398e862dfef537b50e847f0d61f65f3c2b1be66ab2483.jpg)

CAFE F2F NEPAL (Feb 8,2016) Number of Learners signed up: 517  
![](/api/attachments/RC9ZK6PS/fulltext/images/766f4c40f2c44efbcc9133571bf8cd40e26e9371f7736d2719d9415ad78046a1.jpg)  
Figure 4. Example interfaces.

## 4. Data collection with interviews and fieldwork

This section describes data collection via fieldwork during the first stages of the project, and the additional data-collection methods applied during the project’s formalisation-of-learning phase (Sein et al., 2011).

## 4.1. Data collection during BIE and reflection and learning

The second author, the tech-team lead, began the data collection using multiple methods and continued it throughout the iterative app-development cycle, BIE, and the reflection and learning stage of ADR (Sein et al., 2011). The initial data included user observations and informal discussions with both learners and trainers, as well as the demographic dataset (presented in Section 3.1.1).

Data was incorporated into each new version of the app design. The data enabled gradual improvements when the app was in the prototype state. The CAFE tech team presented design and development progress to the NGO on several occasions, showcasing how the app was designed and what improvements had been made, generating additional feedback and designimprovement suggestions from NGO members.

## 4.2. NGO employee interviews

Halfway through the second phase in Cambodia, the ADR progressed into the final phase, formalisation of learning (Sein et al., 2011). To formalise the lessons learned from the design process, the tech team invited an outside researcher, i.e., the first author, to conduct a more formal qualitative data analysis in collaboration with the other initiative members.

To better understand the complex web of collaboration across the Australian government, Cambodian NGOs, and other stakeholders, the researcher first joined an induction training session for the NGO to understand its background in the financial education field. The researcher spent several hours over a few days in the Sydney premises of the NGO discussing the initiative and app development. Six hours of formal interviews were recorded, in addition to informal discussions. These semi-structured interviews (Myers & Newman, 2007) and informal discussions provided valuable information on Cambodia’s background, the background of the microfinance sector, Good Returns role in the education sector, and the challenges and benefits of the diferent software applications to be used. The questions for NGO staf interviews are presented in Appendix A.

The formal data-gathering interviews continued during the first author’s visit to the Cambodian premises. For the first few days, the first author shadowed Phnom Penh ofice employees to understand the background and help the tech team formalise lessons learned. A field trip to the villages took place after a few days. The objective was to observe and interview the trainers and trainees. Field observations and interviews are described in detail in the following section. During the visit to Phnom Penh, we recorded an additional eight hours of formal interviews and conducted numerous informal discussions with the ofice staf. The same set of interview questions (Appendix A) were used both in Sydney and Cambodia, with minor changes in the focus of the discussion; Sydney interviews focused more on the NGO and the project context; Cambodia interviews provided more in-depth information about the CAFE program. Table 3 summarises the interview dates, locations, roles of the interviewees and interview topics.

After taking part in the initial Cambodian and subsequent Nepalese programs, the second author and the NGO parted ways. However, the first author conducted a research follow-up with the CAFE project management in January 2020, and again in February 2021. The purpose of the discussion was to learn the latest developments in the program and its expansion.

## 4.3. Field observations, interviews with the learners and trainers

After completing the first version of the CAFE app, the tech team conducted field visits in August and September of 2015. During these visits, the team members observed how the trainers and learners used the application, what issues they had when using it, and the overall reception. Notes and photos were used to record the field visits.

For the follow-up visits in September 2017, we designed interview questions that focused on learner responses to using the application. The questions had to be clear and concise, to account for the cultural context, and interviews kept brief, polite, and unobtrusive. An interpreter helped us validate and clarify the questions, to ensure that they were appropriate to administer to learners. These interview questions are presented in Appendix B, Section B.1.

Table 3. Interviews with the Good Return in 2017, 2020 and 2021.

<table><tr><td colspan="4">Sydney Office Visit</td></tr><tr><td>Interview date</td><td>Interviewee Role</td><td>Interview topics</td><td>Location</td></tr><tr><td>February 6 2017</td><td>The CEO of the NGO</td><td>The role of the NGO in financial education, program background</td><td>Australia</td></tr><tr><td>February 6 2017</td><td>Tech Lead (the second author)</td><td>Software development and design, Agile methods, fieldwork, challenges</td><td>Australia</td></tr><tr><td>February 7 2017</td><td>Project Lead</td><td>The project background, training session, technical challenges</td><td>Australia (via Skype)</td></tr><tr><td>February 7 2017</td><td>eLearning Manager</td><td>The project background, other technical initiatives, challenges</td><td>Australia</td></tr><tr><td>February 7 2017</td><td>eLearning Expert</td><td>The project background, training session, technical challenges</td><td>Australia (via Skype)</td></tr><tr><td colspan="4">Cambodia Office and Field Visit</td></tr><tr><td>September 5 2017</td><td>Marketing Coordinator</td><td>Background information on the NGO, Cambodia and training</td><td>Cambodia</td></tr><tr><td>September 5 2017</td><td>Trainer Contact/Software Developer</td><td>Training sessions, technical support</td><td>Cambodia</td></tr><tr><td>September 6 2017</td><td>Tech lead (the second author), second interview</td><td>Agile methods, field work, challenges</td><td>Cambodia</td></tr><tr><td>September 6 2017</td><td>eLearning Expert, second interview</td><td>Field work, technical challenges</td><td>Cambodia</td></tr><tr><td>September 7 2017, cont. March 29 2017</td><td>Local Contact Organiser</td><td>Background information of the NGO, villages and training</td><td>Cambodia</td></tr><tr><td>September 7 2017</td><td>Training Content Coordinator</td><td>Training material development, the financial education program</td><td>Cambodia</td></tr><tr><td>September 7 2017</td><td>Field Support Officer</td><td>Background information of the NGO, microfinance in Cambodia</td><td>Cambodia</td></tr><tr><td colspan="4">Follow-up (via email and Skype)</td></tr><tr><td>January 10 2020</td><td>CAFE Program Manager</td><td>Follow-up interview on the state of the program in 2020</td><td>Cambodia</td></tr><tr><td>February 3 2021</td><td>CAFE Program Manager</td><td>Second follow-up interview on the state of the program in 2020</td><td>Cambodia</td></tr></table>

After the first session finished, we interviewed seven learner-participants as a group. As a courtesy to the learners, we captured the interviews manually in our notebooks. Unfortunately, there was no time for interviews after the second session we visited. However, we do note that conducting user interviews was dificult due to language and cultural barriers. The Cambodian learners had less time for engagement with NGO employees, excluding the trainers in the financial initiative, with whom they had formed a rapport. The learners were cautiously curious when asked about doing interviews, but only a few agreed. The reluctance to take part persisted, even when our translator explained that the interviews would consist of only a few questions and would take only a few minutes. A partial interview with the learners is presented as part of a field visit vignette (Section 5.3.1).

Additionally, we briefly interviewed the two trainers whose training sessions we observed during the field visit. These interviews were conducted mostly in English, with some help from our interpreter. These two short interviews were coded similarly to the NGO staf interviews. However, due to time constraints, we limited the interviews to a discussion on the training sessions, CAFE application, and how the trainers perceived it. An excerpt from the second trainer interview is presented in Section 5.2. The semi-structured interview questions for the trainers are presented in Appendix B.1, Section B.2.

## 5. Action design research process and CAFE app development

This section discusses how the design-science project applied ADR step-by-step, starting from the problem formulation and ending with the formalisation of the learning. We illustrate how the ADR process was incorporated with quotes from the NGO members, the learners, and the trainers.

Each step of the ADR process was also applied to format a set of design principles for apps for remote and rural developing countries. We present the principles after each ADR process section and finally summarise them in Section 5.4. Figure 5 outlines the steps, including the ADR process and principles, with the CAFE app team’s actions.

## 5.1. Problem formulation

The ADR process begins with problem formulation (Sein et al., 2011), in this case, part of the overarching problematic context of the financial education initiative. The NGO wanted to apply modern means of educating trainers and learners. The project manager explained these goals:

The focus [of the NGO] was initially on functional literacy for adult women so that they could participate in the formal economy. Get a job or start a business. Fast forward to today, and technology obviously opens up a lot of opportunities in terms of scale and cost eficiency, and reinforcement of key messages or methodologies.

Our interviewees were well-versed in the NGO scene and had participated in international conferences on NGO technology initiatives. They described anecdotally other organisations’ struggle with technologyfocused initiatives in developing countries; many applications were developed, but user adoption was low. Good Return wanted to avoid these issues, and create an application that would be well received and provide insights into technology use as part of the CAFE initiative. The design challenge led to the initiation of the design study in early 2015.

As the first principle of ADR, practice-inspired research states the need to understand how to design applications that would work in the context of the CAFE initiative and beyond (Sein et al., 2011). Neither the problem nor the design solution was limited to a single instance, namely, the CAFE initiative’s first iteration. Organisation members sought to understand how the NGO could conduct similar initiatives in several countries where it operated. The project manager described the ambitions of the NGO:

I think Cambodia is the natural place to pilot [the CAFE program] because we have the biggest team there and the experience. We would also like to leverage relationships that we have in diferent countries, and so the idea would be that Good Return would set up and maintain the platform, including doing the translation or development of the content and expand into eLearning modules for the trainers as well.

If successful, the CAFE app could provide a better understanding of the level of complexity that would be appropriate to Cambodia and similar remote and rural locations. The initial prototype of the CAFE app provided an opportunity for the organisation to test the design, collect user feedback, and refine features that would translate across diferent cultures and reflect the program’s core goals. The team also hoped to uncover some of the poorly understood infrastructure limitations of remote and rural locations.

The second principle of ADR, theory-ingrained artefact, suggests that the artefact should be informed by theories (Sein et al., 2011). In the case of the CAFE app, the artefact was grounded in theories for design and action (Gregor, 2006; Pefers et al., 2018), such as best practices and guidelines of user experience (UX) design (Nunnally & Farkas, 2016), as well as Agile software development methods (Schwaber & Beedle, 2002). The team planned to apply best practices: cultural probes (Gaver et al., 2004), prototyping (Warfel, 2009), user surveys (Nunnally & Farkas, 2016) and iterative and incremental design and development cycles (Schwaber & Beedle, 2002).

![](/api/attachments/RC9ZK6PS/fulltext/images/5f7c8d60321888e9e19fd6e8b368117a2942964441129acc0d8191918e2c5ee7.jpg)  
Figure 5. The ADR process for CAFE application design and development.

![](/api/attachments/RC9ZK6PS/fulltext/images/b05471b43b34e7e8ad496c4c9c26603d28f9b62dfaf0ee439c7badbc38bce582.jpg)  
Figure 6. First training session of the day.

Adopting an Agile way of working was natural for a small, self-organising team, such as the design and development team at Good Return. The lead designer described the need for Agile process and stakeholder engagement:

Heavy processes would make us never deliver anything All we would be doing is paperwork, approvals, steering committees, reporting back. When you are working in this type of context, you have to be Agile. For example, we would never have known that the trainers [of the microfinance institutions] do not have email addresses if we had not gone there, done some [field testing with the software] and reported back.

![](/api/attachments/RC9ZK6PS/fulltext/images/2c325deb3560defa0158ecd380451342c48dcfca37d7846e33a7e851a777ef63.jpg)

![](/api/attachments/RC9ZK6PS/fulltext/images/7e84bf3199cb8970e0252f4f55f4ac71675a8f85a304a827bd67c101ecedd996.jpg)  
Figure 7. The second training in progress.

Based on the first stage and the first two principles of ADR, the team formulated the following design principles:

• Focus on learner/trainer needs: The first design principle suggests that to generate an application that is not limited to a single instance of use, designers should understand user needs and focus on the design’s human aspects, rather than issues related to the country where the design is first applied.

The team understood that the app’s design elements supporting the trainers should focus on the universal educational aspects. In contrast, the design elements supporting the learners should focus on the ubiquitous issues of saving, spending, and lending money. User-focus enabled the team to focus on the user needs and facilitated further localisation when required (i.e., localisation of language or illustrations).

• Prioritise Agility: The second design principle recommends application of Agile methods. Early in the program, the team learned that the project had to be responsive and nimble to succeed. As applied at Good Return, adherence to Agile softwaredevelopment methods supported a flexible approach to system requirements and features (Schwaber & Beedle, 2002).

Agile methods, with an emphasis on prototyping (Warfel, 2009) and user and stakeholder involvement (Gothelf & Seiden, 2016), supported the team by creating the lightweight structure around the development without hindering the creativity and improvisation that creating an application such as the CAFE app requires.

## 5.2. Building, intervention and evaluation

The second stage of ADR consists of an iterative cycle of BIE, during which the initial design of the system is generated, then reviewed for improvement, and design principles are articulated (Sein et al., 2011). This section discusses how data collection, prototyping, and field testing were applied to create a viable artefact and follow ADR principles.

The third principle of ADR, reciprocal shaping, highlights the IT artefact and the organisational context influencing each other; the project generating both entities’ reciprocal shaping (Sein et al., 2011). The organisation and its goals shaped the CAFE app and, in return, the application shaped the organisation.

For example, the organisation shaping the artefact manifests in how the organisation’s tacit knowledge shaped the initial versions of the application. The features included in the prototype were based on the knowledge and understanding of learner needs provided by NGO employees. Experts in adult learning had an extensive understanding of local circumstances or had spent many years working to advance rural and remote communities.

Due to the organisation’s limitations and priorities, the app’s initial version had simple features but ofered engagement directly linked to the CAFE program’s purpose, i.e., financial literacy. The application needed to give learners a positive view of technology, and interest them in financial studies without overwhelming them with complex features. The project manager described the app:

I think in terms of working with learners at a community level, one area that would be interesting to explore would be whether technology can influence people’s behaviour. We are looking at how we can motivate people to do things like save more or inquire more about the terms and conditions of a product before purchasing it or taking out a loan. We are looking at how using technology can nudge people or reinforce messages that help them in certain decisions and habits.

The mutual shaping became apparent when the app was closer to completion. The desire to create and maintain a viable artefact began to shape the organisation, first by highlighting the importance of the team located in Cambodia and, later, in the form of the team’s expansion. The CAFE curriculum required specialised skills, and the organisation added new people. One of these was the training coordinator, who helped the technical team organise field visits and facilitate data collection in addition to other coordination activities. The coordinator explained the role:

I am responsible for four trainers in Prey Veng, Tbong Khmum, and Svay Rieng. And what I can do [there] during my field trip. That means to support the CAFE session delivery; [to] deliver the session of the CAFE with quality.

Last week, I was in these locations because now Good Return is doing the small research project we call serving involving research. We have a translator that conducts interviews.

Furthermore, the overall CAFE program had created a need for more training for the trainers. The introduction of the artefact required training to accommodate the new tools. The e-learning expert described the trainer training program:

So, part of my role has been skills and capability development associated with those trainers in their capacity to deliver financial literacy training and behaviour change education to community learners in the provinces. So, all of the trainers come from the remote provinces themselves, and they come into Phnom Penh twice during the 20-week program for what we call a training of trainers.

The fourth principle, mutually influential roles, states that there should be mutual learning amongst all participants in the project (Sein et al., 2011). The researchers can ofer theoretical knowledge; practitioners contribute their practical expertise and knowledge of the organisation. The tech lead (i.e., the second author) championed Agile development and UX methods in the organisation, providing theoretical grounding and structure to the app development. The first author facilitated organisational introspection and formalised the reflection and learning that took place during the program. The other CAFE team members were either software-development practitioners or curriculum/e-learning experts, and contributed their practical expertise. However, the small team did not have the luxury of a clear separation of tasks and responsibilities; everyone had multiple roles and helped other team members to the best of their abilities. For example, one of the software developers also doubled as a translator and helped the trainers with their technical issues:

I will help my Facebook chat group, that I can share information in that as well. Every day we communicate through that channel for any issue, experience, sharing, or solving any problems together.

If the CAFE team is asking me for support, especially sometimes they need a translator, if I am available, I have enough time, I will help. One of my real responsibilities is providing support to others as well, if they need me and if it is important. Last time I supported the program coordinator and the CAFE coaches to the field.

According to the team member, the small and nimble team with overlapping capabilities was beneficial to the project, further enhancing knowledge transfer between practitioners and the lead designer.

The fifth principle, authentic and concurrent evaluation, highlights the need for simultaneous design and design evaluation (Sein et al., 2011). The small size of the design and development team ensured high engagement levels within the group. The Agile development method, applied in the project during both the design and development phases, also mandated constant evaluation and reflection on the system and regular conversations with the other members of the organisation, such as the trainers, curriculum developers, program coordinators, and other stakeholders (Schwaber & Beedle, 2002). The curriculum designer discussed the review process and the efects of the CAFE program that the reviews captured:

We have inspiring results from our progress use [at] every phase. Every phase, we do a comprehensive progress review. It has shown positive results in terms of behaviour regarding how people are getting confidence [when dealing with microfinance institutions]. Our evaluations from those are that we know that people actually can use a budget. They know how to budget, they know how to save.

Furthermore, the constant evaluation of the process benefitted not only the learners but also the trainers, who were in regular contact with the design team. Although many trainers had some experience with technology, primarily smartphones, they were not originally regular users of applications. The e-learning manager described the learning process for the trainers:

If you did not grow up with that technology as standard, simple things like drag-and-drop do not make as much sense as they might to us. The little X’s to close a window, not quite sure what that is. We found that at the beginning of the program, the confidence [of the trainers] using the technology was a little bit lower. But, by the end of it, they are quite confident with using technology.

It was essential that the development team constantly supported the trainers and ofered guidance and training sessions. However, the training and discussion channels between the trainers and their contact person within the NGO alleviated early adoption issues. Conversely, the trainers’ engagement and feedback helped the design team better understand the unique challenges and learn more about the Cambodian context.

The following excerpt is part of our first interview with the trainer at the first location we visited.

Translator: So, what do you think about [the CAFE app]? Do you like it?

Trainer: Well, it is kind of useful. It is easy for collecting information. However, sometimes it has problems, there are many errors.

Translator: So, do you think this app is enjoyable to use? Or, does such dificulties make it more troublesome?

Trainer: Well, sometimes it is kind of troublesome also. Because sometimes, when we cannot update it up to the right versions, for example, when the trainees register their presence, there are errors.

Translator: But at least, there are also some benefits, right?

Trainer:Yes, I think when it works fine, without error, it is really useful. Because sometimes it helps summarise the income and expense for trainees as well.

Even though the NGO did not have a long history of internal software development, and even though iterative practices were commonly applied in curriculum design and other non-technical activities, the practices had to be introduced into the newly started IT-intensive projects as well, in a form that specifically supported technical design and development. The tech team saw that the organisation should emphasise evaluations of both the artefact and the process. The team also saw that including other members of the organisation and engaging them regularly would generate better project visibility and understanding of the users and other project stakeholders.

Based on the second stage and the three principles of ADR, the team formulated the following design principles:

• New technology, new skills: The third design principle suggests that if the organisation wants to develop further and maintain software applications, it should increase its pool of talent and ensure that employees are proficient in design and development, as well as in supporting and training users. For a small NGO, this is no trivial realisation; the organisation has to find and retain new members with technical capabilities.

• Inflexible responsibilities, malleable roles: The fourth design principle states that designing and developing an application like the CAFE app requires flexibility and sharing knowledge within the team and the wider organisation. A small team does not have the luxury of silos; everyone has to participate in the design and development to the best of their ability.

However, the responsibilities of the team are not flexible. Even if responsibilities are distributed across members of the team and the organisation, the team has to agree on their tasks and hold itself accountable to the other members of the organisation.

• The first iteration is always wrong: The fifth design principle reiterates the essential lessons from Agile software development and ADR; constant evaluation of the product, often with users or clients (Schwaber & Beedle, 2002). The methods also emphasise continuous internal process evaluation and improvement in retrospective meetings, i.e., meetings where the team assesses and adapts their internal processes and ways of working (Andriyani et al., 2017)

## 5.3. Reflection and learning from the CAFE application

ADR suggests that in parallel with the first two stages, problem formulation and BIE, one should continuously engage in reflection and learning (Sein et al.,

2011). This activity includes understanding the design principles that emerge from the internal response that is the design project. As part of reflection and learning, the members of the initiative team engaged with the other members of the organisation by conducting numerous presentations, demos, field trip photos, and video showcases, as well as short briefs written for annual reports and other oficial publications (Good Return, 2017, 2021)

The sixth principle, guided emergence, states that the artefact emerges from the project. The preliminary artefact, which reflects the initial design guided by the mutual shaping of the organisation and the artefact, will change and become more refined throughout the ADR (Sein et al., 2011).

The tech lead stated that the most helpful practice facilitating the artefact’s guided emergence and enabling the team to learn and reflect on their work was the field visits, where the learners were observed in action. Next, we present a vignette based on the field notes and recordings made during our field trip on September 5 2017. During this visit, both authors had the opportunity to visit two diferent sessions and observe groups interacting with the application and the other curriculum materials. The vignette describes the field visit and includes a shorter extract from one of our interviews with the learners. Photos presented in Figures 6 and 7 were captured during this visit and are published with the learners’ permission.

The remaining session activities were based on the paper materials and simple games that the instructors facilitated. The instructor was skilled at capturing the attention of the learners and keeping them engaged with the materials. The whole group participated.

## 5.3.1. Vignette: field visit to evaluate the CAFE app in use

When we arrived in the Prey Veng province, the first session had already gathered in a shady spot in a large courtyard, next to a large farmhouse. Approximately 20 people, mostly middle-aged or older women and few older men, had seated themselves on a large piece of green tarp. The class was about to begin. We quickly introduced ourselves, and our translator repeated our introductions in Khmer. After the introductions, we let the trainer proceed with the day’s session.

First, the trainer handed a tablet to the first person, an older man, who tapped on his picture in the application and confirmed that he was present at the session. Next, the tablet was passed around until every adult in the session had confirmed that they were present. The lesson we had the privilege to observe this time was the second session of the 20-session long program. The learners had encountered tablet technology only a few times before when the trainers set up their accounts. However, the software application’s novelty or the technology did not hinder the learners; the logging-in process was over quickly.

The trainer laid out the paper materials and distribut[ed] the workbooks. After everyone had their presence confirmed by the app, the trainer began the day’s session on balancing spending and loans

The interviewees told us that they were inexperienced users of technology. However, they indicated that the tablet application they used to sign in to the session seemed important and fun. For most learners, the training sessions were the first time they had encountered tablet technology. However, some of the learners had used Facebook. Following two excerpts from two separate interviews demonstrate the experiences the learners had with the CAFE app:

Translator: So do you have fun when using it?

Translator: So, sister (author’s note: a way of addressing in Cambodia), as you attend this CAFE event, you might have noticed people are using the tablet. So, have you used it before?

Learner 1<sup>4</sup>: Yes, I have used it before.

Translator: So, do you think it is enjoyable to use?

Learner 1: Yes, it is. I never saw one before [the training].

Translator: So, let me now ask you a little bit about the tablet. Well, you all have usedtablets [during the program], right?

Learners<sup>5</sup>: Yes.

Translator: Do you like it?

Learners 2 and 3: Yes, I like it

Translator: So do you have fun when using it?

Learner 4: Yes, it is enjoyable. Because now we know more about how to use it, unlike before when the trainer gave us, we do not really know how to use it But when the trainer told us once, now we understand

After the short interviews, we left the first location and visited another training session in another village an hour away from the first. This village was located in the same province, but the site was slightly easier to access due to better roads. We witnessed a somewhat larger session. The second trainer was skilled at energising the learners, and the session was very lively and engaging. The learners in the second session were all female, ranging from young mothers with children in tow to older women. Everyone participated enthusiastically in the learning exercises, which were the same that the first session was also working through.

The third stage of ADR, reflection and learning, and the principle of guided emergence (Sein et al., 2011) provided the design team with the following design principle:

• Prioritise fieldwork: Even though fieldwork is potentially more expensive and time-consuming in the context of software design for developing countries (Schuler & Namioka, 1993), the field visits helped the designers understand the hardware and infrastructure limitations (Regmi, 2017), as well as the extent of users’ prior exposure to the technology.

Observations and casual interactions with users help not only with understanding the physical limitations, but the team can also capture more clearly many nonverbal cues that are communicated delight or frustration (Nunnally & Farkas, 2016).

## 5.4. Formalisation of learning

The last stage of the ADR process is the formalisation of the learning. The ADR suggests that generalisation of the outcomes has three levels: generalisation of the problem instance; generalisation of the solution instance; and derivation of design principles from the design research outcomes (Sein et al., 2011, p. 44).

Even though the CAFE app was designed first for the Cambodian context, it was never meant to solve only a single problem in a single location, and the organisation was looking to apply the design across multiple locations. The more general problem was using tech as a supplement in financial education in the context of any remote and rural location; the artefact should be nimble enough to fit any country context for which the financial education program was planned. The design principles derived from the project would guide the design of any artefacts meant for rural and remote locations in developing countries, not only simple apps but also more complex systems, such as e-learning platforms or mobile applications for advanced learners.

Finally, our ADR project’s context revealed that the traditional approaches that the literature suggested for these focus areas were often insuficient. Furthermore, many of the classic design techniques of software design and development were not available to the software designers who design for users in rural and remote areas. An experienced software designer and developer might perceive some of the principles as self-evident elsewhere than in the NGO context. However, organisations that do not focus primarily on software development might struggle with ICT4D initiatives (Holzer et al., 2020; Mthoko & Khene, 2018) and could lack initial focus and structure when they embark on IT initiatives. Moreover, designing for an audience accustomed to technology should emphasise the design principles diferently than designing for users with very little or no experience in technology. All the principles highlight the need for proper contextual understanding and gradual improvement. Table 4 summarises the design principles derived from the design and development of the CAFE app.

## 6. Discussion

We argue that organisations operating in developing countries can apply and should not avoid high-tech solutions as long as the technology is designed to fit the intended environment. However, understanding the context, the project users and stakeholders, as highlighted in the literature advocating participatory design (Byrne & Sahay, 2007; Drain et al., 2018; Puri et al., 2004), was the key to success in the CAFE app project. Several design principles capture the need for contextual understanding presented in the previous section, from the focus on user needs to the crucial role of fieldwork.

The system designer must understand the physical and cultural limitations and conduct field research or interview local experts to avoid design missteps and ensure the initial adoption, and later sustainability, of the design (Da Silva & Fernandez, 2016). However, for the core components of training initiatives, especially in complex areas like financial education, traditional teaching methods should not be abandoned. Past unsuccessful ICT4D projects showcase the need for a cautious and incremental approach (Heeks, 2003; Ramadani et al., 2018; Da Silva & Fernandez, 2016). The team learned that overloading learners with applications or other technology with which they have had minimal prior contact is not recommended; when learners have more exposure to smartphones or tablet technologies, adding systems has a greater chance of succeeding. For this reason, we recommend that the primary source of teaching materials should present in a familiar format, namely, via printed hand- outs. There are many benefits to the blended application of low-tech and high-tech materials. Booklets have no learning curve, but tablet apps will add a bit of novelty and excitement. Booklets can use illustrations to support learning, even if learners lack literacy skills (Carney & Levin, 2002). Learners can take the handouts home, whereas the few available tablets must remain with the trainer, limiting learner exposure to the technology. Conversely, as with the trainers who were proficient users of technology, the trainers’ basic understanding of systems and smartphones creates more opportunities for digitising the training materials, online trainer support, and e-learning for the trainers.

Table 4. Summary: the design principles.

<table><tr><td>Principle</td><td>Summary</td></tr><tr><td>Focus on learner/trainer needs</td><td>Create an application that is not limited to a single instance of use.Understand user needs and focus on the design&#x27;s human aspects, not specific issues related to the country.</td></tr><tr><td>Prioritise Agility</td><td>Agile methods facilitate a responsive and fast approach.Apply prototyping (Warfel, 2009), focus on user and stakeholder involvement (Gothelf &amp; Seiden, 2016)Flexibility enables creativity and improvisation.</td></tr><tr><td>New technology, new skills</td><td>Increase the talent pool when introducing new technologies.Focus on finding and retaining technical talent.</td></tr><tr><td>Inflexible responsibilities, malleable roles</td><td>Share knowledge and information: everyone in the team can contribute to the design and development.Maintain responsibilities: the team is together accountable for the success.</td></tr><tr><td>The first iteration is wrong</td><td>Champion constant concurrent evaluations of both the artefact and the process (Sein et al., 2011).Hold retrospective meetings for continuous internal evaluation and improvement of the working practices (Schwaber &amp; Beedle, 2002; Andriyani et al., 2017).</td></tr><tr><td>Prioritise fieldwork</td><td>Include members of the organisation that can help with the evaluation of the work.Fieldwork is the best way to get to know the users and their needs and limitations.Fieldwork allows a better understanding of the physical circumstances and can reveal unexpected hardware and infrastructure limitations.</td></tr></table>

Based on our follow-up discussions with the NGO, we now know that the CAFE app design also works in Nepal (Good Return, 2021). The NGO and partner organisations put significant legwork, travel, and interaction with local contacts into the efort to localise the app’s content. However, the original design, already flexible and minimalist, created according to the design principles, provided a good foundation for localisation.

To measure the success of their programs, Good Return applies a metric titled “Financial Capability”. The metric is a combination of four components: awareness, confidence, behaviour, and well-being. Data for each metric is collected at the beginning of the program (“baseline”) and the end (“endline”) via surveys. Each metric is defined by a set of multiplechoice questions, which are ranked from 0 to 10. Table 5 presents the survey results from Cambodia in 2020, where the baseline survey was administered to 85 learners, and the endline survey had 79 responses (92.3% female, 7.7% male). Notably, the financial capability of the participants increased by 42%. The program’s most significant efect was with the behaviour score (84% improvement) and the confidence score (64% improvement).

However, these results are not limited to the app but measure the whole CAFE curriculum. It is dificult to disentangle the app from the overall experience, and it would be disingenuous to claim that the app was the sole reason the program succeeds year after year. Nevertheless, the positive feedback the NGO received has convinced it to retain the application as part of the curriculum, and it has also encouraged the further development of new technical solutions. The most significant new tools are the e-learning curriculum, the Responsible Inclusive Finance (RIF) Academy, and a new mobile application, My Money Tracker. My Money Tracker is a digital version of the printbased tool used as part of the CAFE curriculum. The application is targeting urban and semi-urban Cambodians for cashflow tracking and management (Good Return, 2021).

Table 5. CAFE Program Results, Cambodia.

<table><tr><td>Metric</td><td>Baseline</td><td>Endline</td><td>Increase %</td></tr><tr><td>Knowledge &amp; Awareness Score</td><td>5.09</td><td>6.13</td><td>20%</td></tr><tr><td>Behaviour Score</td><td>2.32</td><td>6.11</td><td>84%</td></tr><tr><td>Confidence Score</td><td>3.91</td><td>6.48</td><td>66%</td></tr><tr><td>Wellbeing Score</td><td>5.46</td><td>6.58</td><td>20%</td></tr><tr><td>Financial Capability Score</td><td>4.45</td><td>6.32</td><td>42%</td></tr></table>

## 7. Conclusions

This study set to find a response to the following question: How does design science, specifically the ADR process, inform the development of ICT4D solutions in rural communities within developing countries? The results of our research show how to develop novel information system applications and introduce them alongside more traditional teaching methods, as long as the development is done with care. We argue that the key to a successful IS application lies in carefully considering the design principles that appear in Section 5.4, which can guide design and development projects for rural and remote locations in developing countries.

Our research shows that the tenets of Agile software design are especially appropriate for developing countries. However, the process must emphasise local understanding and apply ethnographic methods extensively, especially for system design and validation (Gaver et al., 2004), while simultaneously designing with global requirements in mind. Designers who understand local conditions when they begin their design process are more likely to succeed, and will encounter fewer obstacles and revisions when trialling technical solutions as supporting features for financial literacy programs. A designer who can also consider global issues will face fewer dificulties when extending the design beyond its origins.

## 7.1. Contributions to theory

This study’s theoretical contribution consists of the design principles derived from the ADR process and the process application itself. Our study fills the gap in application of design science in developing countries (Gregor et al., 2010) as well as the gap in application of the ADR process, or other forms of action research, in ICT4D research (Bon & Akkermans, 2019; Thapa & Sæbø, 2014). Our study shows the ADR method is well suited for studying software development in the context of developing countries. The study adds to the body of knowledge of action research, design science, and other innovative methods that have expanded our understanding of the methods that can help software development outside the usual software development paradigm (Gregor et al., 2014; Holzer et al., 2020). The study contributes to the body of knowledge of Agile software development literature (Dikert et al., 2016) by presenting a case study where Agile methods have been successfully applied in a developing country context. Furthermore, the suggested design principles can be seen as a way to refine the Agile practice for the context of application development for users in remote and rural areas of the globe (Kuechler & Vaishnavi, 2008). Our study is one of the few ICT4D studies conducted in the Kingdom of Cambodia and contributes to academic studies in the Cambodian context, which has to date consisted of only a few Cambodia-focused information system studies (i.e., (Grunfeld, 2011; Pors, 2016)).

The study addresses an observed gap in ICT4D literature: prior academic studies provide design principles but lack the follow-up where principles are put into practice (Bon & Akkermans, 2019). However, our study is based on a ground- up efort of the NGO, and our design principles are derived from practice, not vice versa. Moreover, the study presents a positive and successful case of ICT4D, where negative results are often reported (Yim & Gomez, 2021). Finally, the study presents a more holistic approach towards ICT4D: it does not only look at software adoption, nor does it solely focus on understanding the social context; but combines both streams of conventional ICT4D research (Ramadani et al., 2018).

## 7.2. Contributions to practice

Design principles formulated in the context of ICT4D studies that can directly benefit practitioners looking for guidance are not yet common (Greve et al., 2020). The design principles are our contribution to practice. The principles provide a unique set of guidelines for a situation where participatory design (Drain et al., 2018; Hussain et al., 2012) or other design best practices are not feasible due to lack of prior technology experience among the participants or the learners. The principles propose a novel form of IS design thinking by suggesting not only gradual design and development, which is already familiar (Beck et al., 2001; Gothelf & Seiden, 2016), but also encouraging constant reflection and self-evaluation as also recommended in the ADR method, and stressing the importance of fieldwork.

The CAFE app study demonstrates a “proof-ofconcept” for other NGOs or aid organisations looking to apply information systems as part of their develop ing-country eforts. The purpose of the ADR is to generate results that are applicable beyond solving a single issue (Iivari, 2015; Sein et al., 2011). Our study shows that design research methods such as ADR can help practitioners structure their work and facilitate learning that might otherwise be missed.

Furthermore, the generalised design principles are useful for practitioners who wish to consider applying IS tools due to their known eficacy (Leong et al., 2016; McGrath, 2016; Oreglia & Srinivasan, 2016), but are unsure as to the appropriate mix of technology and other tools; and who might be unfamiliar with Agile software development and incremental design practices. The seemingly simple but tried-and-tested design principles outlined in this paper are high-level enough to fit any application design and development project for rural and remote locations, but specific enough to highlight the needs of such development projects in this context. Hence, we argue that the ADR principles are adaptable for design in other developing countries besides Cambodia. The successful launches of the same CAFE initiative, including the CAFE app, in Nepal support our claim.

## 7.3. Limitations

One of the study’s main limitations is that our ADR team, although located in Cambodia and often travelling to the villages to visit users, were not all locals and often had to communicate with the trainers and the trainees through interpreters. Our experience of the design and development process is also tied to the limitations of our contextual understanding. Countries other than Cambodia might have more local talent from which to draw, making the design process smoother (Eskelund et al., 2020). Having an entirely local design team might reduce the need for field visits, and designers more familiar with the local environment could shorten the time required for prototyping and readjustment.

Furthermore, our study’s focus, the rural and remote villages of Cambodia, difers from urban cities and suburbs in the extent of coverage of the mobile network and technological literacy. For example, due to the limited number of available tablets and minimal technology exposure, it is dificult to assess the level of tech literacy gained from interactions with the CAFE app. There might be substantial diferences in how the more technically adept city-dwellers can adopt new applications and features within them, which might impact the design principles. Hence, we limit the generalisation of the principles to rural and remote locations.

However, we believe that our higher-level design guidelines are adaptable to any context. As an in-built feature, the design principles will force the practitioners to begin their journey towards understanding the local context and, thus, better design for their specific audience.

## 7.4. Future research

We hope to continue developing these principles in other similar projects or initiatives that apply novel IS tools in developing countries – the next steps for this study link with the following steps Good Return is taking. Since the CAFE learning initiative’s first success and implementation, Good Return continues to explore new ways to apply even more IS tools to support its initiatives. As mentioned in Section 6, the organisation is piloting a mobile app, My Money Tracker, aimed at Cambodians who already have smartphones and technical skills but lack financial education, and a more extensive e-learning initiative called the RIF Academy. We hope that we can continue the design, development, and evaluation journey along with Good Return.

Finally, there is a growing interest in applying design research (Gregor et al., 2014), and action research (Bon & Akkermans, 2019). Future research in this field should also benefit NGO practitioners looking for success stories and design guidelines. The results and lessons learned from this study should encourage other technology-based programs that can positively impact people’s lives in these remote, rural areas. We suggest that NGOs should investigate more ways to foster the use of applications. They should be confident that people are willing and able to embrace these technologies and benefit from them. If conducted with the correct design principles in mind, the design and development of IS systems can make a diference in learners’ lives.

## Notes

1. By ”classroom,” we refer to the shared community spaces, usually outdoor locations, where sessions take place.

2. The second author of this paper was an NGO insider, the lead of the technical team responsible for the CAFE application design and development project in Cambodia. The first author was an outside researcher who helped formalise the lessons learned.

3. Image of a demonstration-page screen, not an actual user. Demo images are blurred for anonymity.

4. Learner 1: female, age 32, three children, housewife, animal farmer.

5. Learner 2: male, age 60, three children, rice farmers and animal farmer.

Learner 3: female, age 43, two children, vegetable farmer.

Learner 4: female, age N/A, five children, farmer and housewife.

6. Discussed with the second author, project managers.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Notes on contributors

Dr Anna Zaitsev is an expert in Agile software development, design thinking and social media research.

Salla Mankinen is a software Architect for ICT4D. She is a Systems Engineer with 20 years of experience building software for large corporations as well as for small non-profit foundations. She was the Program Technology Lead for Good Return in Phnom Penh, Cambodia.

## ORCID

Anna Zaitsev http://orcid.org/0000-0002-8752-512X

## References

Andriyani, Y., Hoda, R., & Amor, R. (2017). Reflection in agile retrospectives. In International Conference on Agile Software Development (Springer) (pp. 3–19).

Asian Development Bank. (2019) . Asian development outlook 2019.

Avgerou, C., & Walsham, G. (2017). Information technology in context: Studies from the perspective of developing countries: Studies from the perspective of developing countries. Routledge.

Baskerville, R. (2008). What design science is not. European Journal of Information Systems, 17(5), 441. https://doi. org/10.1057/ejis.2008.45

Beck, K., Beedle, M., Van Bennekum, A., Cockburn, A., Cunningham, W., Fowler, M., . . . Jefries, R. (2001). Manifesto for agile software development https://agilema nifesto.org/ .

Bon, A., & Akkermans, H. (2019). Digital development: Elements of a critical ICT4D theory and praxis. In International conference on social implications of computers in developing countries (Springer) (pp. 26–38).

Brickell, K., & Springer, S. (2016). The Handbook of Contemporary Cambodia. Routledge.

Bylander, M. (2016). The promises and pitfalls of microcredit as a development solution Brickell, Katherine, and Springer , Simon. In The Handbook of Contemporary Cambodia (Routledge). (pp. 64).

Byrne, E., & Sahay, S. (2007). Participatory design for social development: A South African case study on community-based health information systems. Information Technology for Development, 13(1), 71–94. https://doi.org/10.1002/itdj.20052

Carney, R. N., & Levin, J. R. (2002). Pictorial illustrations still improve students’ learning from text. Educational Psychology Review, 14(1), 5–26. https://doi.org/10.1023/ A:1013176309260

Chhay, D. (2011). Women’s economic empowerment through microfinance in Cambodia. Development in Practice, 21(8), 1122–1137. https://doi.org/10.1080 09614524.2011.606891

CMA. (2016). Annual report 2016. Cambodia Microfinance Association, (CMA). https://cma-network.org/about-us /annual-report/detail/annual-report-2016/ .

Da Silva, A. P., & Fernandez, W. D. (2016). Sustainability of ictd projects and its influencing factors: A comprehensive literature review. 2016 49th Hawaii International Conference on System Sciences (HICSS) Hawaii, 2718–2727.

Deth, S. U., Moldashev, K., & Bulut, S. (2016). The contemporary geopolitics of Cambodia: Alignments in regional and global contexts Brickell, Katherine, and Springer, Simon. In The Handbook of Contemporary Cambodia (pp. 37–48). Routledge.

Dikert, K., Paasivaara, M., & Lassenius, C. (2016). Challenges and success factors for large-scale agile transformations: A systematic literature review. Journal of Systems and Software, 119, 87–108. https://doi.org/10. 1016/j.jss.2016.06.013

Drain, A., Shekar, A., & Grigg, N. (2018). Participatory design with people with disability in rural Cambodia: The creativity challenge. The Design Journal, 21(5), 685–706. https://doi.org/10.1080/14606925.2018.1488923

Drain, A., Shekar, A., & Grigg, N. (2019). Involve me and i’ll understand: Creative capacity building for participatory design with rural Cambodian farmers. CoDesign, 15(2), 110–127. https://doi.org/10.1080/15710882.2017.1399147

Ear, S. (2007). The political economy of aid and governance in Cambodia. Asian Journal of Political Science, 15(1), 68–96. https://doi.org/10.1080/02185370701315624

Engel, C., Leicht, N., & Ebel, P. (2019). The imprint of design science in information systems research: An empirical analysis of the AIS senior scholars’ basket. In ICIS 2019 proceedings, Munich, Germany.

Eskelund, K., Grunfeld, H., & Des, P. (2020). Exploring the competitiveness of Cambodia as an it outsourcing destination. Journal of Global Information Management (JGIM), 28(2), 29–51. https://doi.org/10.4018/JGIM. 2020040102

Gaver, W. W., Boucher, A., Pennington, S., & Walker, B. (2004). Cultural probes and the value of uncertainty. Interactions, 11(5), 53–56. https://doi.org/10.1145 1015530.1015555

Good Return. (2017). Good Return, annual report 2017. Good Return. https://www.goodreturn.org.au/annualreports

Good Return. (2021). Good Return, annual report 2020. Good Return. https://www.goodreturn.org.au/annualreports

Gothelf, J., & Seiden, J. (2016). Lean UX: Designing great products with agile teams. O’Reilly Media, Inc.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337–355. https://doi.org/10.25300 MISQ/2013/37.2.01

Gregor, S., Imran, A., & Turner, T. (2010). Designing for a ’sweet spot’ in an intervention in a least developed country: The case of e-government in Bangladesh. In SIG GlobDev third annual workshop, Saint Louis, USA.

Gregor, S., Imran, A., & Turner, T. (2014). A ‘sweet spot change strategy for a least developed country: Leveraging e-government in Bangladesh. European Journal of Information Systems, 23(6), 655–671. https://doi.org/10. 1057/ejis.2013.14

Gregor, S., & Jones, D. (2007). The anatomy of a design theory. Journal of the Association for Information Systems, 8(5), 312–335. https://doi.org/10.17705/1jais.00129

Gregor, S. (2006). The nature of theory in information systems. MIS Quarterly, 30(3) , 611–642. https://doi.org/ 10.2307/25148742

Greve, M., Lichtenberg, S., Diederich, S., & Brendel, A. B. (2020). Supporting non-communicable disease prevention through a mHealth application in decentralized healthcare systems: Action design research in Eswatini. In European Conference of Information sSystems, ECIS An Online AIS Conference.

Grunfeld, H. (2011). The contribution of information and communication technologies for development (ICT4D) projects to capabilities, empowerment and sustainability: A case study of iREACH in Cambodia. Victoria University.

GSMA Connected Society. (2019). GSMA mobile connectivity index. Mobile Connectivity Index, Retrieved 30 March 2020, from. http://www.mobileconnectivityin dex.com

Heeks, R. (2003). Most e-government-for-development projects fail: How can risks be reduced? (Vol. 14). Institute for Development Policy and Management, University of Manchester.

Holzer, A., Kocher, B., Bendahan, S., Vonèche Cardia, I., Mazuze, J., & Gillet, D. (2020). Gamifying knowledge sharing in humanitarian organisations: A design science journey. European Journal of Information Systems, 29(2), 153–171. https://doi.org/10.1080/0960085X.2020. 1718009

Hussain, S., Sanders, E. B.-N., & Steinert, M. (2012). Participatory design with marginalized people in developing countries: Challenges and opportunities experienced in a field study in Cambodia. Internationa Journal of Design, 6(2)

Iivari, J. (2015). Distinguishing and contrasting two strategies for design science research. European Journal of Information Systems, 24(1), 107–115. https://doi.org/10. 1057/ejis.2013.35

Kang, L. (2016). Social design as a creative device in developing countries: The case of a handcraft pottery community in Cambodia. International Journal of Design, 10 3 , .

Khieng, S., & Dahles, H. (2015). Commercialization in the non-profit sector: The emergence of social enterprise in Cambodia. Journal of Social Entrepreneurship, 6(2), 218–243. https://doi.org/10.1080/19420676.2014.954261

Kuechler, B., & Vaishnavi, V. (2008). On theory development in design science research: Anatomy of a research project. European Journal of Information Systems, 17(5), 489–504. https://doi.org/10.1057/ejis.2008.40

Leong, C. M. L., Pan, S.-L., Newell, S., & Cui, L. (2016). The emergence of self- organizing e-commerce ecosystems in remote villages of China: A tale of digital empowerment for rural development. MIS Quarterly, 40(2), 475–484. https://doi.org/10.25300/MISQ/2016/40.2.11

McGrath, K. (2016). Identity verification and societal challenges: Explaining the gap between service provision and development outcomes. MIS Quarterly, 40(2), 485–500. https://doi.org/10.25300/MISQ/2016/40.2.12

Morris, C. (2016). Justice inverted: Law and human rights in Cambodia Brickell , Katherine, and Springer, Simon. In The Handbook of Contemporary Cambodia (pp. 49–61). Routledge.

Mthoko, H., & Khene, C. (2018). Building theory in ICT4D evaluation: A comprehensive approach to assessing outcome and impact. Information Technology for Development, 24(1), 138–164. https://doi.org/10.1080 02681102.2017.1315359

Mursu, A., Lyytinen, K., Soriyan, H. A., & Korpela, M. (2003). Identifying software project risks in Nigeria: An international comparative study. European Journal of Information Systems, 12(3), 182–194. https://doi.org/10. 1057/palgrave.ejis.3000462

Myers, M. D., & Newman, M. (2007). The qualitative interview in IS research: Examining the craft. Information and Organization, 17(1), 2–26. https://doi.org/10.1016/j. infoandorg.2006.11.001

Nunnally, B., & Farkas, D. (2016). UX research: Practical techniques for designing better products. O’Reilly Media, Inc.

OECD/INFE. (2012). OECD/INFE high-level principles on national strategies for financial education. The Organisation for Economic Co-operation and Development (OECD).

Oreglia, E., & Srinivasan, J. (2016). ICT, intermediaries, and the transformation of gendered power structures. MIS Quarterly, 40(2), 501–510. https://doi.org/10.25300 MISQ/2016/40.2.13

Pefers, K., Tuunanen, T., & Niehaves, B. (2018). Design science research genres: Introduction to the special issue on exemplars and criteria for applicable design science research. European Journal of Information Systems, 27(2), 2. https://doi.org/10.1080/0960085X. 2018.1458066

Phong, K., Srou, L., & Solá, J. (2016). Mobile phones and internet use in Cambodia 2016. The Asia Fundation https://asiafoundation.org/wp-content/uploads/2016/12 Mobile-Phones-and-Internet-Use-in-Cambodia-2016.pdf

Pors, S. (2016). Introducing and implementing an online learning environment in a Cambodian academic program: Impacts, enabling factors and constraints Unpublished doctoral dissertation. The University of Melbourne.

Poverty Probability Index. (2021). Poverty probability index:. https://www.povertyindex.org/country/cambodia

Puri, S. K., Byrne, E., Nhampossa, J. L., & Quraishi, Z. B. (2004). Contextuality of participation in IS design: A developing country perspective. In Proceedings of the eighth conference on participatory

design: Artful integration: interweaving media, materials and practices-volume 1, Toronto, Ontario, Canada. (pp. 42–52).

Puri, S. K., Sahay, S., & Lewis, J. (2009). Building participatory HIs networks: A case study from Kerala, India. Information and Organization, 19(2), 63–83. https://doi. org/10.1016/j.infoandorg.2008.06.002

Ramadani, L., Kurnia, S., & Breidbach, C. F. (2018). In search for holistic ICT4D research: A systematic literature review. In Proceedings of the 51st Hawaii international conference on system sciences, Hawaii.

Regmi, N. (2017). Expectations versus reality: A case of internet in Nepal. The Electronic Journal of Information Systems in Developing Countries, 82(1), 1–20. https://doi. org/10.1002/j.1681-4835.2017.tb00607.x

Schuler, D., & Namioka, A. (1993). Participatory design: Principles and practices. CRC Press.

Schwaber, K., & Beedle, M. (2002). Agile software development with Scrum (Vol. 1). Prentice Hall Upper Saddle River.

Sein, M. K., Henfridsson, O., Purao, S., Rossi, M., & Lindgren, R. (2011). Action design research. MIS Quarterly, 35(1), 37–56. https://doi.org/10.2307/ 23043488

Thapa, D., & Sæbø, Ø. (2014). Exploring the link between ICT and development in the context of developing countries: A literature review. The Electronic Journal of Information Systems in Developing Countries, 64(1), 1–15. https://doi.org/10.1002/j.1681-4835.2014.tb00454.x

Titlestad, O. H., Staring, K., & Braa, J. (2009). Distributed development to enable user participation: Multilevel design in the HISP network. Scandinavian Journal of Information Systems, 21(1), 3.

Vaishnavi, V., Kuechler, W., & Petter, S. (2004). Design Science Research in iIformation Systems. Created in 2004 and updated until 2019 by Vaishnavi, V. and Kuechler, W. http://www.desrist.org/design-research-in-information systems/

Van Biljon, J., Marais, M., & Platz, M. (2017). Digital platforms for research collaboration: Using design science in developing a South African open knowledge repository. Information Technology for Development, 23(3), 463–485. https://doi.org/10.1080/02681102.2017.1328654

Warfel, T. Z. (2009). Prototyping: A practitioner’s guide. Rosenfeld media.

Yim, M., & Gomez, R. (2021). Strengthening ICT4D evaluation: Lessons from the fields of program evaluation, IS/IT evaluation, and aid/development evaluation. Information Technology for Development, 27(2), 381–415. https://doi. org/10.1080/02681102.2021.1876619

## Appendix A. Semi-Structured Interview Questions with the Good Return Staf

## • Background

° Please tell me about your background.

° Why are you working for this project?

° What are your personal goals?

• Organisation background<sup>6</sup>

° Why was the organisation founded?

° Who works for the organisation?

° How do you fund the projects/programs?

° Are there any issues related to the project funding?

• The project/program

° Tell me about the background of the CAFE initiative

° What are the goals of the CAFE initiative?

° How were the countries selected?

° What do you think this project will achieve for the people in developing countries?

° What do you think this project will achieve for the organisation?

• Project specifics

° What are the goals for the project?

° What is the background of the project employees?

° Who are the main stakeholders?

° What is the application used for?

° How is the application developed?

° What roles do you have in the project?

• Partner organisations

° What is the main role of the partners?

° How do you communicate with the partners? Any dificulties?

• Other initiatives/project/programs

° Are there other similar projects?

° If yes, do the have similar goals?

° Why this project located/developed/aimed to help people in this country?

° What are the main benefits related to this country?

° What are the main challenges related to this country?

• What are the next steps in the project?

## Appendix B. Interview Questions for Learners and Trainers

Interviews conducted via an interpreter who formatted the questions for the cultural context.

B.1. Questions for Learners

• Background and CAFE training

° What is your name, age?

° Are you married or have any children?

° What do you do for living?

° How many times have you attended the training?

° What do you think about the training?

° Do you think the training is easy?

° If not, ask more about the challenges

° Have you previously heard about the concepts taught

today? (Ask about toady’s topic i.e., saving and loans)

° Have you used tables before?

° What is your opinion on using the tables?

° Do you think it’s useful during the training?

• Additional questions (if time)

° Do you think your children understand or can use tablets?

° Have you ever heard about Facebook?

° Would you take part in similar training in future?

B.2. Questions for Trainers

• Background and CAFE training

° What is your name?

° How long have you been teaching (CAFE training)?

° How many students have you had so far? Groups, weeks training?

° Do you live close by to the training location?

° What is your way of getting here?

• CAFE application questions

° Were you familiar with the tablets before you begun training?

° What do you think about the CAFE app?

° Do you have any issues with the CAFE app? Other GoodReturn software?

° How is the internet connection here?

° How do you use Facebook?
