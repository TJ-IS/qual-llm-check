---
otero_id: 5628
otero_key: "U2YG7MRF"
title: "Leveraging Crowdsourcing: Activation-Supporting Components for IT-Based Ideas Competition"
authors: "Jan Marco Leimeister; Michael Huber; Ulrich Bretschneider; Helmut Krcmar"
year: "2009"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222260108"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Leveraging Crowdsourcing: Activation-Supporting Components for IT-Based Ideas Competition

Jan Marco Leims te r, Michael Hube r, Ul rich Bre ts chneid r, and Helm ut Krcmar

Jan Marco Leimeister is a Full Professor of Information Systems and holds the Chair for Information Systems at Kassel University since 2008. He is also a Research Group Manager at the Computer Science Department at Technische Universitaet München, Munich, Germany. He runs research groups on virtual communities, e-health, and ubiquitous/mobile computing and manages several publicly funded research projects. His teaching and research areas include IT innovation management, service science, ubiquitous and mobile computing, collaboration engineering, e-health, online communities, and IT management.

Michael Huber is a Researcher at the Chair for Information Systems, Technische Universität München since he graduated from there with an M.S. in Computer Science in 2007. His research interests include community engineering, virtual communities, communities for innovations, IT support of collaborative activities, and human– computer interaction. He is engaged in the research project GENIE, a project that supports customer-driven development of innovations for software companies, funded by the German Federal Ministry of Research and Education. He also runs the research project SAPiens—an Internet-based ideas competition for students and scholars, collaboratively developing innovations.

Ul rich Bretschneider is a Researcher at the Chair for Information Systems, Technische Universität München, Munich, Germany. He graduated in Business Administration (majoring in Information Systems) at the University of Paderborn, Paderborn, Germany. His current research experiences and interests include virtual communities as well as open innovation, especially ideas competitions and ideas communities. He runs the research project GENIE, which is funded by the German Federal Ministry of Education and Research. He is also engaged in the research project SAPiens.

Helm ut Krcmar is a Full Professor of Information Systems and holds the Chair for Information Systems at the Department of Informatics, Technische Universitaet München, Germany, since 2002. He worked as a Postdoctoral Fellow at the IBM Los Angeles Scientific Center, as Assistant Professor of Information Systems at the Leonard Stern School of Business, New York University, and at Baruch College, City University of New York. From 1987 to 2002 he was Chair for Information Systems, Hohenheim University, Stuttgart. His research interests include information and knowledge management, IT-enabled value webs, service management, computer-supported cooperative work, and information systems in health care and e-government.

Abstract: Ideas competitions appear to be a promising tool for crowdsourcing and open innovation processes, especially for business-to-business software companies. Active participation of potential lead users is the key to success. Yet a look at existing ideas competitions in the software field leads to the conclusion that many information technology (IT)–based ideas competitions fail to meet requirements upon which active participation is established. The paper describes how activation-enabling functionalities can be systematically designed and implemented in an IT-based ideas competition for enterprise resource planning software. We proceeded to evaluate the outcomes of these design measures and found that participation can be supported using a two-step model. The components of the model support incentives and motives of users. Incentives and motives of the users then support the process of activation and consequently participation throughout the ideas competition. This contributes to the successful implementation and maintenance of the ideas competition, thereby providing support for the development of promising innovative ideas. The paper concludes with a discussion of further activation-supporting components yet to be implemented and points to rich possibilities for future research in these areas.

Key words and phrases: activation, crowdsourcing, ERP software, ideas competition, incentives, motivation, open innovation, theory-driven design.

Let us consider an instructive scenario of an innovation environment. Innovative strength in Germany can be found in the domain of engineering and industrial commodities. A prominent example is the German automobile industry [18]. This statement cannot, however, be applied to German software producers, who are only average compared to other leading European countries or, for example, the United States. According to a survey by the German Federal Ministry of Education and Research, German software producers lack a business culture that fosters systematic innovation activities. There is no systematic brainstorming in order to generate ideas for innovations: idea generation takes place informally without sustainability and is often driven by coincidence [18]. To further complicate the matter, software producers are not using the innovative potential of customers to drive innovation. For example, the demands, wishes, and requirements of customers are often not used systematically for new product development. Customers are treated as recipients of products, not as a source of innovation.

As a consequence, German software producers generate fewer real innovations compared to software producers from other countries. Software companies, which are often organized as one-man as well as one-product businesses, generate incremental innovations and improve their existing software products over a long period of time without generating disruptive or radical innovations. This situation has the potential to endanger software producers’ future perspectives in the highly competitive software market.

A chance for software companies to overcome these problems lies on opening up their innovation activities to customers. In general, customer integration into innovation activities stands for an important competitive strategy, known as open innovation [3, 14]. In literature and practice, ideas competitions are discussed, and generally acknowledged as an effective practice for integrating customers into the early stages of the innovation process [21]. Through the organization of ideas competitions, companies attempt to collect innovative ideas from customers via an Internet-based platform.

Although ideas competitions sound like a familiar approach to access the knowledge of customers, there is only limited research that has studied these customer integration practices in detail [12, 37]. The literature that is available solely focuses on studying ideas competitions from the perspective of social science, especially business administration. For example, Walcher [43] explored lead-user characteristics of participants of ideas competitions. Lacking are studies that address the design of Internet-based platforms for ideas competitions that typically address the domain of information science. As the technical and organizational design of an ideas competition will influence a customer’s participation, design aspects are an important variable for optimizing their successful implementation. Putting research effort into designing Internet-based ideas competitions in general and into supporting active participation in particular is important for research and practice.

Our research seeks to address this gap in knowledge of effective designs for supporting active participation in ideas competitions. We implemented a pilot project, called SAPiens, whose design of incentive-supporting components was derived from motivation theory and led to active participation in SAPiens.

## Theoretical Background

## Open Innovation

In the twentieth century, many leading industrial companies generated, developed, and commercialized ideas for innovations in self-reliance. Nowadays, companies are increasingly rethinking the fundamental ways of managing their innovation activities. Overcoming companies’ boundaries in order to open up to other sources of innovation has become increasingly important. In this context, customers are seen as one of the biggest resources for innovations [4, 5, 11, 22].

Customer and user integration into innovation activities is a mode of value creation [4]. Companies gather ideas for innovations from customers and users by integrating them into the early stages of the innovation process. The ideas expressed by customers reflect their needs and wishes and have been described as “need information” [11, 41]. Customers also express ideas that have been called “solution information.” Solution information represents not only need information but also customer-based suggestions describing how ideas can be transferred into marketable products [41].

The underlying idea of integrating customers into the early stages of the innovation process is the following: the integration of stakeholders will open up the company’s innovation funnel whereby potential perspectives or ideas for creating innovations come into the innovation process [44]. Or, in other words, the amount of innovation potential that can be poured into the innovation funnel increases because more parties are actively involved. The company, therefore, gains more ideas for innovations. Surowiecki describes this concept as follows: “Large groups of people are smarter than an elite few, no matter how brilliant—better at solving problems, fostering innovation, coming to wise decisions, even predicting the future” [36, p. 1]. The principle of “collective intelligence” or “wisdom of crowds” is the underlying assumption of this idea [27, 36], which is illustrated in Figure 1.

![](/api/attachments/U2YG7MRF/fulltext/images/313e78eccf00305f4ac7ae35fa50c2c3fcac53e82c17b76bcdfd7af4bef146ec.jpg)  
Figure 1. Open Versus Closed Innovation Process Source: Adapted from [3].

In literature and in practice, there are three core practices for integrating customers into the early stages of the innovation process. These are the Lead-User Method, Internet Toolkits, and Ideas Competitions. The Lead-User Method implies systematic identification of innovative customers, so-called lead users, and their integration into workshops in order to generate ideas and concepts for new products or services together with companies’ employees [39, 40]. With the help of Internet Toolkits, customers are asked to design concepts for new products via an Internet-based or stand-alone software application on self-reliance [13, 42]. Through Internet-based ideas competitions, companies attempt to collect innovative ideas from customers [43].

## Ideas Competitions

An ideas competition can be defined as an invitation of an organizer—namely, a firm— to a general public or a targeted group to submit contributions to a certain topic within a predefined period of time. A review committee evaluates the submitted ideas and selects the winner [10, 38]. In conducting ideas competitions, firms aim to integrate customers into the early phases of the innovation process. So, ideas competitions are a method to expand the source of potential new ideas. The competitive character inherent in an ideas competition encourages participants to produce a winning idea that is innovative and perhaps even unique.

Although research on ideas competitions in the context of open innovation processes is limited, in practice ideas competitions have become an elaborate method for integrating customers into innovation activities (Table 1).

Table 1. Selected Examples of Ideas Competitions for Students

<table><tr><td>Organizer: name of the competition (URL)</td><td>Characteristic value</td></tr><tr><td>IBM: Global Innovation Jam (www.globalinnovationjam.com)</td><td>Innovation Jam was not just a large online brainstorm. The Jam&#x27;s goal was to move beyond simple invention and idea generation. IBM wanted to identify new market opportunities and create real solutions that advance business, communities, and society in meaningful ways.</td></tr><tr><td>Motorola: Motofwrd (http://promo.motorola.com)</td><td>Create the future of seamless mobility in a world without borders. Descriptions by short stories (fiction), essay/white papers (nonfiction), (animated) short films, comic strips, or digital arts.</td></tr><tr><td>Adidas: miadidas (www.miadidas.com)</td><td>Miadidas was the appeal to customers to submit ideas on the design or functionality of sport shoes.</td></tr><tr><td>Fujitsu Siemens: Innovation Contest (http://innovation-contest.fujitsu-siemens.com)</td><td>The contest was dedicated to “IT Services for Tomorrow’s Data Center” and addressed issues of strategic business importance to the users of Fujitsu Siemens products. It was important to anticipate how data centers will function and to find out what services will be required in the years ahead.</td></tr><tr><td>Henkel: Henkel Innovation Challenge (www.henkel.com)</td><td>The 2007 event was focused on the Laundry and Home Care Business Sector of Henkel. In teams of three, participants were asked to submit visions on new household products.</td></tr><tr><td colspan="2">Source: Extended and adapted from [10].</td></tr></table>

There are some prominent examples. In 2006, IBM invited customers as well as employees to their ideas competition called “Innovation Jam.” More than 140,000 international participants joined the Innovation Jam, which yielded more than 46,000 ideas. The best ideas produced projects such as software applications and services for micro-finance institutions. Adidas [29], Motorola, and Fujitsu Siemens are only a few examples of firms that run ideas competitions in order to integrate customers into innovation activities.

A categorization system for ideas competitions does not exist. The following systematization was derived from an analysis of the ideas competitions mentioned above. We also included some characteristics from early research on ideas competitions [29, 42]. The main characteristics of ideas competitions are summarized in Table 2.

The analysis of ideas competitions reveals that although diversity exists in the composition of the various components, common trends and best practices can be identified. Typically, the tasks given to the participants are kept generic, offering them a broad platform on which they can base their ideas. Submissions in the initial phases of ideas competitions include a brief description of ideas usually limited to five pages.

Table 2. Characteristics of Ideas Competitions

<table><tr><td>Criteria</td><td>Description</td><td>Characteristic value</td></tr><tr><td>Task specificity</td><td>Addresses the scope of theme [29]</td><td>If task specificity is high, organizers search for ideas concerning a specific scope. If task specificity is low, no specific scope is addressed.</td></tr><tr><td>Degree of idea elaboration</td><td>Addresses the quality and complexity of participants&#x27; ideas [29]</td><td>In technically related ideas competitions, such as IBM&#x27;s “Innovation Jam,” organizers asked for more elaborated ideas in order to make the ideas comprehensive and tangible to the jury.</td></tr><tr><td>Organizational appearance</td><td>Addresses which way participants can submit ideas</td><td>In some cases, ideas have to be submitted by e-mail or letter. In most cases, ideas have to be submitted via an Internet-based platform. After submission, the ideas are presented on the platform and can be viewed, discussed, or even evaluated by other participants during the competition.</td></tr><tr><td>Time line</td><td>Addresses the duration of submission phase</td><td>Duration ranges from a few weeks (minimum four) to several weeks (up to 30).</td></tr><tr><td>Incentives</td><td>Addresses the prizes offered</td><td>Prices range from cash prices to nonmonetary prices, such as iPods, vouchers, etc.</td></tr><tr><td>Target group</td><td>Addresses participants&#x27; qualification</td><td>Sometimes ideas competitions are characterized by participants&#x27; age, interests, skills, etc.</td></tr></table>

Incentives for participation often comprise cash prices of up to <sup>e</sup>1,000. The evaluation process is carried out by juries and the typical duration is between 4 and 26 weeks.

Most ideas competitions are Internet-based: ideas can be submitted via an Internetbased platform. After submission, the ideas are presented on the platform and can be viewed, discussed, or even evaluated by other participants. Internet technology facilitates the realization of an ideas competition, provides access to a large group of customers, and facilitates easy submission of ideas. Internet-based competitions, therefore, lower the effort and costs for participants as well as for organizers [29].

## What Prompts Participation in Ideas Competitions? Some Fundamental Considerations Concerning Participant Motivation

Participation in ideas competitions depends on the motives of a participant. In the field of motivation psychology, a motive is seen as an individual’s psychological disposition (e.g., [23]). A relatively stable set of motives is developed during an individual’s socialization process (e.g., [10, 23]). In a particular situational context, an analogous motive will be activated and subsequently causes a particular behavior. Activation means that the individual is responsive to perceived inborn stimuli (e.g., an inborn desire) or external incentives (e.g., salary, social contacts, etc). Rosenstiel [30] describes the activation of human behavior in a simple model (MIAB ; motiveincentive-activation-behavior), illustrated in Figure 2.

![](/api/attachments/U2YG7MRF/fulltext/images/65ccc412a1765ee5f90fc07482475067890294d632d2626c7eefc8bda462e7a8.jpg)  
Figure 2. Motive-Incentive-Activation-Behavior Model (MIAB )  
Source: Adapted from [30].

Several motivation concepts are based on this explanatory MIAB model. One of the most popular motivation concepts outlines the distinction between intrinsic and extrinsic motivation. Intrinsic motivation occurs when an individual engages in a behavior, such as a hobby, that is initiated without obvious external incentives. External motivation is activated by external incentives, such as direct or indirect monetary compensation, or recognition by others. The distinction between intrinsic and extrinsic motivation is fundamental to the theories of several psychologists. For example, intrinsic and extrinsic motivation is emphasized in Deci and Ryan’s cognitive evaluation theory [8] as well as in Heider’s attribution theory [16]. The distinction of intrinsic and extrinsic motivation is also the basis for Herzberg’s “two factor” theory [28].

Both intrinsic and extrinsic motivational factors may play a role in an individual’s decision to participate in an ideas competition. Due to the competitive component of ideas competitions, a comparison with sports competitions can be made. Researchers studying the motivation of athletes found intrinsic motives, such as self-esteem or fun, versus extrinsic motives, such as the crowd cheering the athlete on or winning trophies [9, 31, 38], to be important. Applied to ideas competitions, the potential to win a prize may act as an external incentive. Similarly, for some individuals, intrinsic motivation to participate in an ideas competition could be the prospect of personal fulfillment, or having fun while developing a new idea. These motives likely stem from a participant’s inborn desire and from feelings of competence, satisfaction, and fulfillment.

Participation in ideas competitions is influenced by incentives that potential participants perceive and then activate. In order for this sequence of events to occur, organizers of ideas competitions must distribute the right mix of incentives in order to motivate people to participate. The right mixes of incentives are those that appeal to or match the participant’s motivations for participating. While competition organizers have little or no influence on internal incentives (i.e., feelings of competence, satisfaction, or fulfillment), organizers can develop a competition that provides external incentives.

## Research Design and Methodology

Our research aimed at designing organizational as well as technical components that stimulate people for participate in ideas competitions. We used the MIAB model explained above to design these components. Relying on this motivation model, we assumed that the design components would serve as external incentives and encourage participation.

The framework of our research is based on the approach of theory-driven design as proposed by Briggs [2], which we applied to the MIAB model. Using this approach, we ground our research proceeding as shown in Figure 3.

In step 1, we identified motives of relevance to activating participation in ideas competitions. We derived these motives from the MIAB model and a literature review. On the basis of the identified motives, we derived incentives (step 2) that had the potential to stimulate motivation. Based on this, we designed incentive supporting components (step 3).We then applied these design components in a real-world field test and launched an ideas competition in cooperation with the software manufacturer SAP in order to evaluate our theory-based design of components for activation and participation support (step 4).

In this research, formative evaluation was applied to evaluate the derivation of incentives. The following research question guided the evaluation:

To what extent do the activation-supporting components and incentives influence the motivation of individuals to participate in the competition?

The results of this research provide information on the appropriateness of each incentive.

## Derivation of Motives and Incentives

## Identifying Relevant Motives: A Brief Literature Review

Participation in ideas competitions is activated by incentives that potential participants perceive and that activate corresponding motives. In order for this sequence of events to occur, organizers of ideas competitions must distribute the right mix of incentives in order to motivate people to participate. The right mixes of incentives are those that appeal to or match participants’ motives for participating. As internal incentives solely arise from a participant’s inner motives—such as a natural internal desire or from feelings of competence, satisfaction, or fulfillment—organizers are only able to influence external incentives. Because of this, we will focus in the scope of derivation of design elements solely on motives that are activated in terms of extrinsic motivation. The question remains, what specific motives that are activated in extrinsic motivation finally are? As research in the field of ideas competitions is new, no theoretical and empirical insights exist. A review of existing literature on motivation is helpful in order to extract relevant motives. We conducted a search in the scope of a brief literature review.

![](/api/attachments/U2YG7MRF/fulltext/images/6fe9c43999475597ca4edc297897aee45d32f468e60c9bd401a7889fd1a40881.jpg)  
Figure 3. Research Approach for Designing Components for Activation and Participation Support Derived from the MIAB Model

Research on exploring and explaining human behavior in different social settings revealed different motives. For example, Klandermans [20] and Simon et al. [35] explored motives that explain voluntary engagement in social movements, such as the civil rights movement, or involvement in specific social groups, such as attending to elderly. Several authors revealed motives that explain motivation of participants in open source projects [15, 17, 23, 24, 26].

Due to the competitive factor, ideas competitions are comparable to sport competitions. Because of that, it is worth taking a deeper look at the research on sport science first. Extrinsic activated motives in the field of sport motivation research can be divided into two classes [9, 31, 38]. The first class is direct compensation. In sporting events, direct compensation is manifested as monetary or nonmonetary prizes such as medals, trophies, or other prizes for the (three) best participants. Ideas competitions also award winners with monetary as well as nonmonetary prizes. Thus, direct compensation may be also a relevant motive for participating in ideas competitions.

The second class of extrinsic activated motives typically related to sport competitions is social motives. Social motives include the expected reactions of significant others, friends, or the audience. Motivation to participate in a competition is greater if significant others indicate the importance of participating in the event. This relation is formally expressed as a multiplicative function. Applied to ideas competitions, participants may expect positive reactions from other participants as well as from the organizer of the competition.

Insights from research on motivation in the field of open source could be also relevant for our research. Hars and Ou [15] figured out that programmers regard participation in open source projects as an effective way to demonstrate their capabilities and skills. Their achievements in open source projects are used to demonstrate competency to other developers or sponsors of the project. Therefore, participating in open source projects is seen as a channel for self-advertisement for those seeking new job opportunities. This self-marketing motive can also be assigned to ideas competitions.

Table 3. Motives and Incentives of the SAPiens Ideas Competition

<table><tr><td>Motives</td><td>Incentives</td></tr><tr><td>Learning</td><td>Access to the knowledge of expertsAccess to the knowledge of mentorsAccess to the knowledge of peers</td></tr><tr><td>Direct compensation</td><td>PrizesCareer options</td></tr><tr><td>Self-marketing</td><td>Profiling options</td></tr><tr><td>Social motives</td><td>Appreciation by the organizerAppreciation by peers</td></tr></table>

There is another motive often discussed in open source context that can be applied at its face value to ideas competitions—learning (e.g., [15, 23, 24, 26]). Participants may take part in ideas competitions in order to expand their skill base. The presentation of competitor’s ideas as well as the competitor’s and organizer’s feedback to one’s own idea enables participants to gain learning experiences.

## Identifying Incentives

Table 3 summarizes the interplay between motives and incentives that imply requirements for incentive-supporting components. The first column contains the motives as mentioned before. The second column contains the incentives assigned to the motives in the first column. Each motive can be activated by one or more of these incentives.

## Incentives Fostering “Learning”

In order to identify incentives that lead to an activation and thus participation in the ideas competition by fostering the motive learning, we started by identifying the sources of knowledge in the competition, followed by proposing components that make this knowledge accessible.

The motive learning implies the question: “from whom or what can a participant in an ideas competition learn?” In the SAPiens ideas competition, there are several groups of people involved [10]:

1. Experts that provide specialized knowledge on the competition’s subject, for example, being part of the organizer’s staff. In the case of the SAPiens competition, these experts are employees of SAP. This incentive implies functionalities and organizational measures that enable participants of the competition to converse with these experts.

2. Mentors assisting attendants in the participation and providing their knowledge on the subject. As the SAPiens ideas competition addresses students, scholars, and trainees, there are lecturers, tutors, teachers, and similar persons that are located in the proximate environment of the participants. These mentors can support the participants in a personal way beyond the virtual community of the ideas competition. Mentors provide expert knowledge basically without the use of the Internet-based ideas competition platform due to their direct relation to the participants. This incentive implies requirements for mainly organizational measures that enables the address of tutors in a nontechnical/organizational manner.

3. Participants themselves. In addition to drawing on the knowledge provided by external sources such as the previously mentioned experts and mentors, learning can also be achieved by the knowledge of the community itself. The community of participants steadily produces knowledge as the amount of ideas in the competition grows and may act as inspiration and knowledge base for its own members. This incentive implies requirements for functionalities to access the pool of knowledge in terms of submitted ideas.

## Incentives Fostering “Direct Compensation”

As discussed, a participant’s willingness to actively submit ideas is, among others, motivated by direct compensation, for example, by winning a cash prize. Because of this, we identified the incentives “prizes” and “career options,” implying requirements to provide these in terms of suitable awards and, for example, possibilities for job applications.

## Incentives Fostering “Self-Marketing”

The third motive we introduced above is called self-marketing. As a suitable incentive, we identified “profiling options.” This incentive implies requirements for functionalities that enable users to present themselves, their skills, knowledge, and work to the community in order to get attention and gain tribute.

## Incentives Fostering “Social Motives”

As discussed above, in ideas competitions, participants expect positive reactions from other participants and the organizer by demonstrating their capabilities, skills, and competence—social motives. Therefore, we identified two incentives, named “appreciation by the organizer” and “appreciation by peers.” These incentives require suitable components that enable the organizer as well as the community to acknowledge the capabilities, skills, and competence of the participants.

## Designing Activation-Supporting Components

## The Case Background: SAPiens—Characteristics of an IT-Based Ideas Competition for an ERP Company

SAP iens is an Internet-based ideas competition initiated by the enterprise resource planning (ERP) software producer SAP. The ideas competition was run in summer

2008 over a period of 14 weeks and targeted student users of SAP software who know the software from their university education. The invited people were students from randomly selected German universities. These invited SAP users were asked to submit ideas to improve the SAP software or to bring out radical innovation in the scope of the SAP software. Thus, there were no limits on task specification.

Ideas had to be submitted via an Internet-based platform that was designed and implemented especially for the SAPiens ideas competition and could be visited only after registration. Each submitted idea, phrased in a maximum length of a letter page, was visualized during the runtime in an idea pool, a separate section of the online platform that was visible for everyone who visited the Internet platform. After the runtime of the competition, submissions were evaluated by a qualified jury committee consisting of 10 SAP experts. The 10 best ideas were assigned by lucrative cash prices as well as nonmonetary prices worth <sup>e</sup>6,000 in total. Figure 4 shows the home page of the Internet platform of the SAPiens ideas competition.

During the runtime of SAPiens, 127 student SAP users visited (after registration) the SAPiens Web site. Of those users, 39 actively participated in the competition by submitting at least one idea. The contributors submitted 61 ideas in total. The rest out of 127 registered student SAP users participated in just scoring and commenting on submissions of other users or simply lurking. The comments and user evaluations were a helpful measure in the later evaluation phase when the submissions were evaluated and discussed by the 10 jury members. Evaluations and feedback from other users helped the ideas presenters to refine their ideas during the runtime of SAPiens.

## Design Components

In this section, we identify concrete tools, functionalities, and organizational measures that can be implemented in an Internet-based ideas competition such as SAPiens based on the requirements for incentive-supporting components.

As a theoretical basis for technical components, we use the extant literature dealing with creativity support tools as the development of ideas in an ideas competition can also be described as a creative process. One of the most established models for supporting creativity is the “Genex framework” for developing user interfaces for supporting creativity [32, 33, 34]. We will use this framework as Shneiderman proposes “a checklist for designers of software tools” [34, p. 118]. The Genex framework identifies four activities during the process of creativity—collect, relate, create, and donate. The activity collect implies tasks such as searching, browsing, and visualizing resources in order to gather and assign information. Relate refers to consulting with peers and mentors. Create comprises tasks such as associating and exploring solutions, composing artifacts, and reviewing and replaying session histories. The fourth activity, donate, refers to disseminating the results elaborated during the creativity process [34].

Table 4 shows the correlation between incentives and technical functionalities as well as organizational measures we implemented in the SAPiens ideas competition.

As we lean on the Genex framework for creativity support tools, we try to cover each activity of the framework by providing at least two technical or organizational measures. Thus, we aim at comprehensively supporting the process of creativity build ing on a well-established framework.

![](/api/attachments/U2YG7MRF/fulltext/images/009cfce8d84dae4aea78e2919ba7e75634abcc22df068fe6676b0a1b94d0d86b.jpg)  
Figure 4. Screenshot of the Home Page of the SAPiens Ideas Competition

Figure 5 shows the correlation of the four activities the Genex framework proposes for creative tasks and the measures we implemented in the SAPiens ideas competition.

## Access to the Knowledge of Experts

The knowledge of people identified as experts can be accessed in several ways. We assume that there is usually no face-to-face contact between participants and experts. Thus, in our mind, the experts’ knowledge can be transferred best by audio or in written form. We are limited to techniques that can be implemented directly by the ideas competition’s Internet platform or in its organizational context. We identified skypecasts and phone-based conference calls as suitable measures to make the experts knowledge accessible to the competition participants.

Skypecasts. Skypecasts are Internet-based conference calls using the free of charge messaging and voiceover Internet protocol software Skype. Skype can be used to offer conference calls in regular intervals and without forcing competition participants to install a proprietary software solution bound to the competition (e.g., implemented on and offered by the competition’s Internet platform). Expert Skypecasts require technical as well as organizational support. Skypecasts require the use of Skype as a software tool that has to be installed by all parties involved in the conference call. Using Skype also requires organizational tasks such as predefining and announcing an agenda for each Skypecast with an expert and the moderation of the conference call (see Figure 6).

Table 4. Incentives and Related Incentive-Supporting Functionalities

<table><tr><td rowspan="2">Incentives</td><td colspan="2">Incentive-supporting functionalities and organizational measures</td><td rowspan="2">Activities of the Genex framework</td></tr><tr><td>Technical</td><td>Organizational</td></tr><tr><td rowspan="2">Access to the knowledge of experts</td><td>Skypecasts</td><td></td><td rowspan="2">Collect, relate</td></tr><tr><td>Phone-based conference calls</td><td></td></tr><tr><td>Access to the knowledge of mentors</td><td></td><td>Addressing tutors by e-mail, phone call, and face time</td><td>Collect, relate</td></tr><tr><td rowspan="2">Access to the knowledge of the community</td><td>Browsable, sortable, searchable, and paginated list of ideas</td><td></td><td rowspan="2">Collect, relate</td></tr><tr><td>Tag cloud</td><td></td></tr><tr><td>Prizes</td><td></td><td>Cash prizes Noncash prizes</td><td>—</td></tr><tr><td>Career options</td><td></td><td>Opportunity for job applications</td><td>—</td></tr><tr><td>Profiling options</td><td>User profile Idea description Linking people to ideas</td><td></td><td>Collect, relate, create, donate</td></tr><tr><td>Appreciation by the organizer</td><td></td><td>Jury rating of ideas</td><td>Collect, relate</td></tr><tr><td>Appreciation by peers</td><td>Community rating of ideas</td><td></td><td>Collect, relate, create, donate</td></tr></table>

The incentive supporting Skypecast can be assigned to the activities collect and relate of the Genex framework as it supports the collection of information as well as consulting with peers and experts.

In the SAPiens ideas competition, we implemented a subsection on the Internet platform containing all relevant information on SAPiens Skypecasts. We described what SAPiens Skypecasts are, how they work, where to get the required software, when the next conference call will take place, and how to join it. The date and agenda of the next Skypecast was announced in the newsletters we provided as well.

![](/api/attachments/U2YG7MRF/fulltext/images/fd6042c13be081e21e56f3f00ec9371719690f206c78f3c4ba8b013a7b9e8805.jpg)  
Figure 5. Activation-Supporting Components Implemented in the SAPiens Ideas Competition Derived from the Genex Framework

![](/api/attachments/U2YG7MRF/fulltext/images/4682e27e447a9a4326343645b039f70bf65389274f117b8537d3e529d9af133b.jpg)

We are looking forward to your participation!

Figure 6. Implemented Component: Skypecasts

Phone-Based Conference Calls. As Skypecasts were still at the stage of development (in the meantime, Skypecasts are not provided anymore by Skype Limited) and the sound quality gets worse with the increase of participants, conventional conference calls via telephone are an alternative to the SAPiens Skypecasts mentioned above. The advantage of conventional conference calls is the superior sound quality and the independence from any software solution since one can assume every participant of the ideas competition has a conventional telephone. The major disadvantages of these conference calls are fees that have to be paid either by the participants or the organizer of the ideas competition. Nevertheless, conference calls based on conventional phones are a suitable way to provide the knowledge of experts to the participants of an ideas competition as well.

Similar to the Skypecast component, phone-based conference calls can be assigned to the activities collect and relate of the Genex framework as they support the same activities.

## Access to the Knowledge of Mentors

We identified the organizational measure of addressing mentors in the prephase of the competition as a suitable way to initiate mentors as providers of expert knowledge. We asked lecturers, tutors, and teachers to assist their scholars and students in elaborating and developing ideas by providing their expertise in the SAP software they have according to their teaching activities. Therefore, we used e-mail, telephone, and face time as instruments to address mentors independent from the competition’s Internet platform. In the Genex framework for creativity support tools, mentors as experts supporting participants can be assigned to the activities collect and relate. Participants can consult mentors concerning thematic support and they can gather useful information in order to elaborate their ideas.

## Access to the Knowledge of the Community

To access the knowledge of the community itself, we implemented functionalities to make submitted ideas accessible in several ways.

Browsable, Sortable, Searchable, and Paginated List of Ideas, Tag Cloud. Each idea submitted to the SAPiens ideas competition is included into a pool of ideas that can be accessed in the form of a browsable, sortable, searchable, and paginated list of ideas (see Figure 7). This list can be sorted and browsed according to criteria such as date, title, rating, or author. Furthermore, it is possible to search and thus filter ideas by entering search terms, or using a tag-cloud view of the key words ideas can be tagged with during the submission process. Thus, participants are expected to get helpful suggestions, inspiration, and motivation by browsing these ideas.

The list of ideas is a tool that can be assigned to the activities collect and relate of the Genex framework as it supports tasks such as searching, browsing, and also consulting with others.

![](/api/attachments/U2YG7MRF/fulltext/images/0e81cb1ddaede437cba14ba2da1c1e53f7ac1b947a041b76b5c4950b9105f896.jpg)  
Figure 7. Implemented Component: List of Ideas

## Prizes and Career Options

As organizational measures, we announced a cash prize worth <sup>e</sup>2,000 for the participant submitting the best jury-rated idea (see Figure 8). For participants of the second-best through the tenth-best ideas, cash prizes worth <sup>e</sup>200 were arranged. The elevenththrough thirtieth-best ideas evaluated by the jury were awarded an Amazon.com gift card in the amount of <sup>e</sup>50. Furthermore, we offered SAP-related training courses for the participants submitting the 10 best jury-rated ideas in terms of noncash prizes. The first 30 places got the chance to apply for a job at SAP in a preferred application procedure.

Direct compensation cannot be classified in terms of the Genex framework as it cannot be classified in terms of a creativity-supporting implementation, but it is motive for participation that can be supported through direct incentives.

## Profiling Options

We tried to identify suitable tools that enable users to present themselves, their skills, knowledge, and work to the community in order to get attention and gain tribute. Therefore, we implemented two functionalities described as follows.

User Profile. In order to encourage self-marketing, we identified personal information of a participant presented to others as a first alternative. Every participant of the SAPiens ideas competition has their own virtual user profile (see Figure 9). This profile contains personal information such as name, prename, e-mail, telephone number, skype-id, and a list of submitted ideas. Furthermore, the user profile contains a section “über mich” (“about me”) where participants can enter free text about themselves. We identified the user profile and especially the “about me” section as the most important tool for encouraging self-marketing. All personal information on a participant is

![](/api/attachments/U2YG7MRF/fulltext/images/42d194a365a804548c2f563223cb8be1c6fe3eab9639ad3a65112fc942ec50f7.jpg)

The first 5 winners will be invited for the awards show to the UCC User Meeting 2008 in Heidelberg. On this weekend, you will also have the opportunity to develop your idea together with SAP Inspire Team.

The awards for the lecturers will be assigned for the monitoring of the students. Does an attendant/team win one of the first 6/4 awards for his/their handed in /developed idea, his/their lecturer will also win a award for his mentoring abilities.

1. Place (mentoring of the best handed in idea): 1 year hosting of an SAP UCC product

Figure 8. Implemented Component: Direct Compensation  
![](/api/attachments/U2YG7MRF/fulltext/images/0444c3bf06d9ce353cc47b5405312910805e529510f05727f8b4b14433a6d360.jpg)  
Figure 9. Implemented Component: User Profile

aggregated in its user profile and, thus, it is the only way to present oneself to other participants and, of course, SAP.

Regarding the Genex framework, we assigned the user profile to the activity collect and relate as participants are able to consult with other community members using the contact information listed in the user profiles and to gather information on the skills and submitted ideas of others.

![](/api/attachments/U2YG7MRF/fulltext/images/0e3e7e93420e1553c050b0fa9e2d882f89a0c21aead91af60bec6ac2ee808bb0.jpg)  
Figure 10. Implemented Component: Idea Description

Idea Description. Another powerful component to encourage self-marketing is the submission form for ideas. This form enables the participant to describe and submit his or her ideas by filling out several text boxes, according to a consistent framework for the description (see Figure 10). Providing a detailed description and highlighting aspects such as the novelty or particularity of the ideas enables the participants to present their skills, knowledge, and work to the community.

According to the Genex framework, this functionality covers the activities create and donate as the participant creates a new contribution to the competition and donates his or her creative work to the community.

Linking People to Ideas. In order to encourage self-marketing in terms of showing one’s creativity skills, we implemented the incentive-supporting functionality to link people’s user profiles to submitted ideas. Each idea submitted to the competition is tied to one or more user profiles, depending on the number of its authors and editors. The description of an ideas contains the pictures and names of its authors and editors. This linking between ideas and participants implements a way to encourage the self marketing of participants as, for example, high-quality and top-rated ideas are tied to one or more specific persons.

We assigned this linking to the activities collect and relate of the Genex framework as the provided functionalities supports gathering information and consulting with peers similar to the user profiles mentioned above.

![](/api/attachments/U2YG7MRF/fulltext/images/e35801f38b58bbcd3d08df32a42347b2eed0dedae1a5ce79c3c754bc22e29923.jpg)  
Figure 11. Implemented Component: Community Rating

## Appreciation by the Organizer and by Peers

As discussed above, in ideas competitions, participants expect positive reactions from other participants and the organizer by demonstrating their capabilities, skills, and competence. Therefore, we identified two incentives—appreciation by the organizer and appreciation by peers. In the SAPiens ideas competition, we therefore implemented three incentive-supporting components described as follows.

Community Rating. Every idea submitted to the ideas competition can be rated by other participants according to several dimensions such as originality, degree of innovation, marketing potentials, or customer value (see Figure 11). As the rating of an idea is visible to others, the skills, capabilities, and competence of the idea’s author is exposed in case of a positive review. Thus, the component encourages gaining appreciation by peers.

We assigned the functionality community rating to the activities relate and create and donate of the Genex framework on one hand in terms of implementing a way of gathering feedback from and thus consulting with others; on the other hand, in terms of creating feedback by rating ideas according to several dimensions that are optionally enriched by further comments.

Jury Rating. In order to determine the winners of an ideas competition, all submitted ideas were rated by a jury. In the SAPiens competition, the rating by the jury took place after idea development and community rating was completed. The jurors had expert knowledge of the competition’s topic. The evaluation of the questionnaires submitted by the participants provided a ranking of ideas to determine the winners of the competition.

The jury rating of ideas was necessary to comply with the requirements of a competi tion and was a tool to encourage social motivation: the possibility to obtain a high rating also meant the opportunity to be recognized by the organizer of the competition.

In analogy to the incentive-supporting component community rating mentioned above, the jury rating can be assigned to the activities collect and relate in the Genex framework.

## Evaluation of Derived Activation-Supporting Components

Eval uation, according to Bortz/Doering, deals with the verification of the efficacy of an intervention (e.g., a therapy, an action, etc.) by means of empirical research. Summative evaluation focuses on the outcome or the final results of an action, whereas formative evaluation focuses on the continuous development of the intervention [1]. Within a formative evaluation, the interventions are tracked continuously and the results are used as a basis for appropriate further actions (if necessary) in order to achieve the overall objective of the intervention [1]. Thus, the formative evaluation serves to track and improve interventions. In our research, formative evaluation is applied in order to verify the derived incentives. The following research question guided the evaluation:

To what extent do the external incentives activate the extrinsic motivation that finally motivates participants to take part in the SAPiens ideas competition?

The results provide information on the appropriateness of each incentive. For the proposed formative evaluation, we used self-reporting data collected by an online survey.

## Methodological Aspects

Because perceived motivation-related issues can only be expressed by the participants of the SAPiens ideas competition, conducting an online survey was the best method to evaluate the derived incentives. A statement was formulated for each incentive as shown in Table 5. Using a rating scale from 1 (totally disagree) to 5 (totally agree), participants were asked to rank the degree to which each incentive motivated him or her to take part in the SAPiens ideas competition.

The questionnaire used in this study was structured, tested, and consequently adapted to the needs of the target audience. The questionnaire was pretested by 10 experts pursuing doctoral and master’s degrees in information technology (IT) or business administration. An additional online pretest was carried out to control the content and functionality of the questionnaire. The objective of the two pretests was to ensure that none of the statements was ambiguous and that the statements adequately captured the domain of interest [6].

Table 5. Statements Used to Obtain a Ranking of the Design Elements

<table><tr><td>Underlying motive</td><td>Incentive</td><td>ItemI attended the SAPiens ideas competition because . . .</td></tr><tr><td rowspan="3">Learning</td><td>Knowledge of experts</td><td>... I would like to discuss my ideas with SAP experts in order to learn more about SAP software and the SAP company.</td></tr><tr><td>Knowledge of mentors</td><td>... I would like to discuss my ideas with my mentor in order to learn more about SAP software and the SAP company.</td></tr><tr><td>Knowledge of peers</td><td>... I hope that the ideas listed in the “idea pool” will extend my knowledge pool and I can learn more about SAP software and the SAP company.</td></tr><tr><td rowspan="2">Direct compensation</td><td>Prizes</td><td>... I hope to win a monetary or nonmonetary prize.</td></tr><tr><td>Career option</td><td>... I hope to get the chance to work for SAP.</td></tr><tr><td>Self-marketing</td><td>Profiling options</td><td>... I want to present my creativity skills as well as my expertise to other participants and to SAP by displaying my ideas on the SAPiens platform as well by listing my expertise on my personal profile.</td></tr><tr><td rowspan="2">Social motives</td><td>Appreciation by the organizer</td><td>... I would be very proud if my idea is acknowledged by the jury.</td></tr><tr><td>Appreciation by peers</td><td>... I want to receive acknowledgment from the other participants.</td></tr></table>

Expert opinion indicated that the content of the scales was valid. The questionnaire was implemented using the online survey service “2aks.” Each participant was provided with a personalized link to the online survey. The survey was administered over a period of five weeks and was sent to all participants of the SAPiens ideas competition who submitted at least one idea. Thirty-two participants provided answers to the questionnaire, which represented a 100 percent response rate.

## Results and Analysis

The purpose of this empirical study was to explore whether the implemented incentives of the competition were perceived as motivational by the participants. The results revealed that all incentives were rated as motivational for participating in the SAPiens ideas competition (Table 6). Because the means of each answer representing one incentive are higher than 3.31, the implemented incentives were able to activate the attendant’s participation. The results clearly show that the respondents’ extrinsic motivation was driven by learning, compensation, social, as well as self-marketing motives.

Table 6. Means and Standard Deviations

<table><tr><td>Incentive</td><td>ItemI attended the SAPiens ideas competition because . . .</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Knowledge of experts</td><td>... I would like to discuss my ideas with SAP experts in order to learn more about SAP software and the SAP company.</td><td>3.750</td><td>1.191</td></tr><tr><td>Knowledge of mentors</td><td>... I would like to discuss my ideas with my mentor in order to learn more about SAP software and the SAP company.</td><td>3.719</td><td>0.991</td></tr><tr><td>Knowledge of peers</td><td>... I hope that the ideas listed in the “idea pool” will extend my knowledge and I can learn more about SAP software and the SAP company.</td><td>3.313</td><td>0.859</td></tr><tr><td>Prizes</td><td>... I hope to win a monetary or nonmonetary prize.</td><td>3.875</td><td>1.008</td></tr><tr><td>Career options</td><td>... I hope to get the chance to work for SAP.</td><td>3.750</td><td>1.191</td></tr><tr><td>Profiling options</td><td>... I want to present my creativity skills as well as my expertise to other participants and to SAP by displaying my idea on the SAPiens platform as well by listing my expertise on my personal profile.</td><td>3.531</td><td>1.244</td></tr><tr><td>Appreciation by the organizer</td><td>... I would be very proud if my idea is acknowledged by the jury.</td><td>4.406</td><td>0.756</td></tr><tr><td>Appreciation by peers</td><td>... I wish for acknowledgment from the other participants.</td><td>3.313</td><td>1.148</td></tr></table>

Surprisingly, the incentive “Appreciation by SAP” (mean 4.41; standard deviation [SD] ±0.76) was rated much higher than the “Prizes” incentive (mean 3.88; SD ±1.01), which indicates that material compensation is not the most activating driver for participating in the SAPiens ideas competition. Further, incentives providing direct compensation were not the sole reason people engaged in this competition.

Knowledge of Experts was the next-highest-ranked motivation, with a mean score of 3.75 (SD ±1.191), followed by Knowledge of Mentors, with a mean of 3.72 (SD ±0.991). This indicates that participants in the SAPiens ideas competition are willing to learn about SAP software and the SAP company. This result is in accordance with current research on motivation of programmers participating in open source projects, revealing that participants in open source projects are highly motivated by the opportunity to learn from other participants [15, 24]. Although participants in the SAPiens ideas competition rated the possibility to learn from experts and mentors higher than the possibility to learn from other participants as (Knowledge of Peers: mean 3.31; SD ±0.859), our results show the same tendency as those reported from previously mentioned open source surveys.

Answers concerning the incentive Career Options reached a mean of 3.75 (SD ±1.191), which indicated that participants were motivated to a certain extent by the possibility to be considered in the preferred application procedure at SAP. Further, this result indicates that this design element in the SAPiens ideas competition can serve as an instrument for the human resources department at SAP to recruit young academics. These results go hand in hand with the results for the incentive profiling options contained in the motive self-marketing. The mean for profiling options was 3.53 (SD ±1.244). The profiling options were used by the participants to show their expertise to the community in general and especially to catch the attention of SAP mentors or recruiters within the competition.

Obtaining appreciation by the organizers of the competition seemed to be an important motivation factor. But surprisingly, appreciation from other participants was less important (mean 3.31; SD ±1.15). Obviously, it is more important for attendants to get appreciation from the “right” persons: the “right” persons were members of the jury—namely, responsible SAP employees. This insight is in accordance with current research results from Jeppesen and Frederiksen [19], which substantiate our results. The results of a survey conducted by Jeppesen and Frederiksen showed that members of firm-hosted innovation communities are more responsive to appreciation concerning their innovative contributions from the community-initiating firm than from other community members. Respondents of the Jeppesen–Frederiksen survey were more motivated by the desire to be recognized for innovative behavior by the firm than by peer members. Jeppesen and Frederiksen obtained their results from the members of a firm-hosted innovation community and they provide an interesting reason for their survey results: the means by which the firm provides firm recognition to community members is by exposing and promoting important user innovation on their community Web site. Therefore, artifacts that provide firm recognition can be highlighted as important incentives motivating people to participate in ideas competitions.

## Summary and Implications

SAPiens is an IT-based ideas competition intended to generate user-driven innovations and leverage crowdsourcing or “wisdom of crowds” throughout the creative process of generating innovative ideas. Observations and archive analyses indicate that members candidly interact with one another, especially via the discussion board and the skypecasts. The amount and quality of generated ideas underline the success of the project.

The results of the surveys intended to measure the effect of incentives for participation provide support for the success of the activation and participation support. The design measures seem to have had a positive effect on perceived incentives and consequently on active participation. These results support the underlying theoretical constructs by showing that the elements of the design measures had an impact on perceived incentives, activation, and consequently the decision to participate.

Artifacts of usage as well as the results of extensive observations comply with this result: the document and archive analyses of the community give a clear impression of the motivation for participation in the SAPiens ideas competition, of the personal benefit for the users, and of the role incentives play in the ideas competition. This research is the first to show that theory-based design in the context of open innovation can be applied successfully in a real-world setting.

These results must be seen in light of the study’s limitations. The findings need further empirical substantiation, especially in respect to other IT-based ideas competitions within and external to the IT industry. The study sample consisted only of participants of SAPiens; those who visited the site but decided not to participate were lost to possible inclusion in the study. The inclusion of nonparticipants could have provided valuable data for testing the effect of the design measures and the underlying concepts: Was it an issue of incentives that made them decide not to become members? In reality, it would have been difficult to gain access to anyone who visited the site but did not participate. Interestingly, the log file analyses of SAPiens show a low rate of one-time visitors, regardless of which criteria proposed for Web sites or virtual communities in the literature [7] is applied.

## Future Outlook and Research Recommendations

The impl emented components are only a first step toward understanding activation and participation support in the context of competitions as a means for open innovation and crowdsourcing.

Motives, activation, and participation are multidimensional constructs; a complete in-depth analysis was not possible within the confines of this project. We believe that the full potential of technical or organizational support of activation and participation support for ideas competitions and open innovation concepts have not yet been explored.

In extension of the models introduced in Figures 2 and 3, future steps should focus on further factors influencing activation, such as the development of social capital within the ideas competition. One possibility for achieving this can be the use of reputation indicators that assist with this process.

Future research should focus on possibilities of appropriate reputation mechanisms. The development of rating mechanisms for user-generated content, users, and operators is a promising starting point for supporting incentives and activation in open innovation activities in general, and in ideas competitions in particular. Rating information in the context of SAPiens means that single information items can be rated by each registered user. Thus, the ideas could be evaluated by the users in the context of usefulness and comprehensibility. Positive feedback should strengthen trust in the quality of the content.

In addition to technical components geared toward supporting incentives, activation, and participation, competence and benevolence of the operators of an ideas competition play an important role for the creation of innovative ideas and maintenance of trust in operators and peers [25]. Moderation should guide the community according to intersubjectively comprehensible rules to support trust within the competition. The structure and content of these rules for moderation and management as well as questions such as “What has to be moderated, how, and when?” have yet to be researched.

Future work should also aim at developing more mechanisms to support and harvest the wisdom of crowds in selecting the best ideas. Furthermore, there is a conceptual gap between the generation and selection of ideas and their transformation into innovations. We need to explore further methods, concepts, and tools to support the processing of ideas into innovations, also using the wisdom of crowds.

In addition to the limitations of research stated previously, future work should address the following open research questions:

How could we apply the concept of this ideas competition to target groups other than students and academics? Transferring the Community for Innovations concept to users of the software (e.g., in firms) is stated to be one of the most promising concepts for the future—but what would need to be adapted and why?

What are the theoretical implications for wisdom of crowds and open innovation theories applying the concept of an “ideas competition,” for example, when distinguishing between different cultures, target groups, product domains, and so forth?

The interaction structures of such innovation communities and other open innovation concepts need deeper understanding. More research is needed to understand the antecedents, structural features, design parameters, and outcomes of ideas competitions, especially in the context of innovation communities.

## References

1. Bortz, J., and Döring, N. Forschungsmethoden und Evaluation: für Human- und Sozialwissenschaftler [Research Methods and Evaluation for Social Scientists]. Berlin: Springer, 2006.

2. Briggs, R.O. On theory-driven design and deployment of collaboration systems. International Journal of Human–Computer Studies, 64, 7 (2006), 573–582.

3. Chesbrough, H. The era of open innovation. MIT Sloan Management Review, 3, 44 (2003), 35–41.

4. Chesbrough, H. Open Business Models. Boston: Harvard Business School Press, 2007.

5. Chesbrough, H., and Crowther, A.K. Beyond high tech: Early adopters of open innovation in other industries. R&D Management, 36, 3 (2006), 229–236.

6. Churchill, G.A. A paradigm for developing better measures of marketing constructs. Journal of Marketing Research, 16, 1 (1979), 64–73.

7. Cothrel, J. Measuring the success of an online community. Strategy & Leadership, 28, 2 (2000), 17–21.

8. Deci, E.L., and Ryan, R.M. Intrinsic Motivation and Self-Determination in Human Behavior. New York: Plenum Press, 1985.

9. Duda, J.L., and Whitehead, J. Measurement of goal perspectives in the physical domain. In J.L. Duda (ed.), Advances in Sport and Exercise Psychology Measurement. Morgantown, WV: Fitness Information Technology, 1998, pp. 21–48.

10. Ebner, W.; Leimeister, M.; Bretschneider, U.; and Krcmar, H. Leveraging the wisdom of crowds: Designing an IT-supported ideas competition for an ERP software company. In R.H. Sprague Jr. (ed.), Proceedings of the Forty-First Annual Hawaii International Conference on System Sciences. Los Alamitos, CA : IEEE Computer Society Press, 2008 (available at www2.computer.org/plugins/dl/pdf/proceedings/hicss/2008/3075/00/30750417.pdf?template= 1&loginState=1&userData=anonymous-IP%253A%253A127.0.0.1).

11. Enkel, E.; Perez-Freije, J.; and Gassmann, O. Minimizing market risks through customer integration in new product development: Learning from bad practice. Creativity and Innovation Management, 14, 4 (2005), 425–437.

12. Ernst, H. Virtual customer integration. In S. Albers (ed.), Cross-Functional Innovation Management: Perspectives from Different Disciplines. Wiesbaden, Germany: Gabler, 2004, pp. 192–208.

13. Franke, N., and Piller, F. Value creation by toolkits for user innovation and design: The case of the watch market. Journal of Product Innovation Management, 21, 6 (2004), 401–415.

14. Gassmann, O., and Enkel, E. Open innovation: die Öffnung des Innovationsprozesses erhöht das Innovationspotenzial [Open innovation: Opening innovation process advances potential of innovation]. Führung und Organisation, 75, 3 (2006), 132–138.

15. Hars, A., and Ou, S. Working for free? Motivations for participating in open-source projects. International Journal of Electronic Commerce, 6, 3 (2002), 25–39.

16. Heider, F. The Psychology of Interpersonal Relations. Mahwah, NJ: Lawrence Erlbaum, 1958.

17. Hertel, G.; Niedner, S.; and Herrmann, S. Motivation of software developers in open source projects: An Internet-based survey of contributors to the Linux kernel. Research Policy, 32, 7 (2003), 1159–1177.

18. Holl, F.L.; Menzel, K.; Morcinek, P.; Mühlberg, J.T.; Schäfer, I.; and Schüngel, H. Studie zum Innovationsverhalten deutscher Software-Entwicklungsunternehmen [Study of German software companies innovation activities]. In F.L. Holl (ed.), Entwicklungen in den Informations- und Kommunikationstechnologie [Developments in Information and Communication Technologies], vol. 2. Berlin: Eigen-verlag, 2006, pp. 1–221.

19. Jeppesen, L.B., and Frederiksen, L. Why do users contribute to firm-hosted user communities? The case of computer-controlled music instruments. Organization Science, 17, 1 (2006), 45–63.

20. Klandermans, B. The Social Psychology of Protest. Oxford, UK: Blackwell, 1997.

21. Koufteros, X.; Vonderembse, M.; and Jayaram, J. Internal and external integration for product development: The contingency effects of uncertainty, equivocality, and platform strategy. Decision Sciences, 36, 1 (2005), 97–133.

22. Kristensson, P.; Magnusson, P.R.; and Matthing, J. Users as a hidden resource for creativity: Findings from an experimental study in user involvement. Creativity and Innovation Management, 11, 1 (2002), 55–61.

23. Lakhani, K.R., and von Hippel, E. How open source software works: “Free” user-to-user assistance. Research Policy, 32, 6 (2003), 923–943.

24. Lakhani, K.R., and Wolf, R.G. Why hackers do what they do: Understanding motivation and effort in free/open source software projects. MIT Sloan Working Paper no. 4425–03, Cambridge, MA, 2003.

25. Leimeister, J.M.; Ebner, W.; and Krcmar, H. Design, implementation, and evaluation of trust-supporting components in virtual communities for patients. Journal of Management Information Systems, 21, 4 (Spring 2005), 101–135.

26. Lerner, J., and Tirole, J. Some simple economics of open source. Journal of Industrial Economics, 50, 2 (2002), 197–234.

27. Libert, B., and Spector, J. We Are Smarter Than Me: How to Unleash the Power of Crowds in Your Business. Upper Saddle River, NJ: Prentice Hall, 2007.

28. Mausner, B.; Snyderman, B.B.; and Herzberg, F. Motivation to Work. Edison, NJ: Transaction, 1993.

29. Piller, F., and Walcher, D. Toolkits for idea competitions: A novel method to integrate users in new product development. R&D Management, 36, 3 (2006), 307–318.

30. Rosenstiel, L. von. Grundlagen der Organisationspsychologie: Basiswissen und Anwendungshinweise [Basics of Organizational Psychology]. Stuttgart, Germany: Schäffer-Poeschel, 2007.

31. Ryan, R.M.; Vallerand, R.J.; and Deci, E.L. Intrinsic motivation in sport: A cognitive evaluation theory interpretation. In W.F. Straub and J.M. Williams (eds.), Cognitive Sport Psychology. Lansing, NY: Sport Science International, 1984, pp. 231–242.

32. Shneiderman, B. User interfaces for creativity support tools. In E.A. Edmonds and L. C andy (eds.), Proceedings of the Third Conference on Creativity & Cognition. New York: AC M Press, 1999, pp. 15–22.

33. Shneiderman, B. Creating creativity: User interfaces for supporting innovation. ACM Transactions on Computer–Human Interaction, 7, 1 (2000), 114–138.

34. Shneiderman, B. Creativity support tools. Communications of the ACM, 45, 10 (2002), 116–120.

35. Simon, B.; Loewy, M.; Stürmer, S.; Weber, U.; Freytag, P.; Habig, C.; Kampmeier, C.; and Spahlinger, P. Collective identification and social movement participation. Journal of Personality and Social Psychology, 74, 3 (1998), 646–658.

36. Surowiecki, J. The Wisdom of Crowds. New York: Random House, 2005.

37. Toubia, O. Idea generation, creativity, and incentives. Marketing Science, 25, 5 (2006) 411–425.

38. Vallerand, R.J., and Fortier, M.S. Measures of intrinsic and extrinsic motivation in sport and physical activity: A review and critique. In J.L. Duda (ed.), Advances in Sport and Exercise Psychology Measurement. Morgantown, WV: Fitness Information Technology, 1998, pp. 81–101.

39. von Hippel, E. Lead users: A source of novel product concepts. Management Science, 32, 7 (1986), 791–805.

40. von Hippel, E. The Sources of Innovation. New York: Oxford University Press, 1988.

41. von Hippel, E. “Sticky information” and the locus of problem solving: Implications for innovation. Management Science, 40, 4 (1994), 429–439.

42. Wagner, C., and Prasarnphanich, P. Innovating collaborative content creation: The role of altruism and wiki technology. In R.H. Sprague Jr. (ed.), Proceedings of the Fortieth Annual Hawaii International Conference on System Sciences. Los Alamitos, CA : IEEE Computer Society Press, 2007 (available at www2.computer.org/plugins/dl/pdf/ proceedings/hicss/2007/2755/00/27550018b.pdf?template=1&loginState=1&userData= anonymous-IP%253A%253A127.0.0.1).

43. Walcher, P.-D. Der Ideenwettbewerb als Methode der aktiven Kundenintegration [The Ideas Competition as an Approach for Active Customer Integration]. Wiesbaden: Deutscher Universitäts-Verlag, 2007.

44. Zhang, X.; Miao, C.; Li, Y.; and Zhang, H. Beyond product customization: Towards a conceptual framework for collaborative customer innovation. Paper presented at the Twelfth International Conference on Computer Supported Cooperative Work in Design, Xi’an, China, April 16–18, 2008.
