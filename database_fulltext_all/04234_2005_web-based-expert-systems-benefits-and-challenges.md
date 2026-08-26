---
otero_id: 4234
otero_key: "DZF4XTK8"
title: "Web-based expert systems: benefits and challenges"
authors: "Y. Duan; J.S. Edwards; M.X. Xu"
year: "2005"
journal: "Information & Management"
doi: "10.1016/j.im.2004.08.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Web-based expert systems: benefits and challenges

Y. Duan<sup>a,\*</sup>, J.S. Edwards<sup>b</sup>, M.X. Xu<sup>c</sup>

<sup>a</sup>Luton Business School, University of Luton, Luton LU1 3JU, UK <sup>b</sup>Aston Business School, Aston University, Birmingham B4 7ET, UK <sup>c</sup>Portsmouth Business School, University of Portsmouth, Portsmouth PO4 8JF, UK

Received 27 June 2003; received in revised form 28 May 2004; accepted 21 August 2004 Available online 8 December 2004

## Abstract

Convergence of technologies in the Internet and the field of expert systems have offered new ways of sharing and distributing knowledge. However, there has been a general lack of research in the area of web-based expert systems (ES). This paper addresses the issues associated with the design, development, and use of web-based ES from a standpoint of the benefits and challenges of developing and using them. The original theory and concepts in conventional ES were reviewed and a knowledge engineering framework for developing them was revisited. The study considered three web-based ES: WITS-advisor — for ebusiness strategy development, Fish-Expert — for fish disease diagnosis, and IMIS — to promote intelligent interviews. The benefits and challenges in developing and using ES are discussed by comparing them with traditional standalone systems from development and application perspectives.

Keywords: Expert systems; Knowledge based systems; Internet; Benefits and challenges; Web-based

## 1. Introduction

Expert systems (ES) emerged as a branch of artificial intelligence (AI), from the effort of AI researchers to develop computer programs that could reason as humans [6]. Many organizations have leveraged this technology to increase productivity and profits through better business decisions [5,10,11,19,26]. ES are one of most commercially successful branches of AI [17]. Although there have been reports of ES failures [18,27], surveys [15,28] show that many companies have remained enthusiastic proponents of the technology and continue to develop important and successful applications.

The early applications of expert systems were standalone, based on mainframe, AI workstations or PC platforms. Later came LAN-based distributed applications. Despite their commercial success, Grove [12] pointed out that several problems and limitations are associated with traditional ES applications:

 Knowledge bottleneck. It is difficult to acquire knowledge from different sources. Experts are often unable to express explicitly their reasoning process.

 Performance brittleness. An ES is limited in its coded expertise, which relates to a narrow domain and the ES therefore performs poorly outside its boundary.

 Availability. Having the expertise provided by an ES at the place and time where it is needed is a problem when limited to the use of a stand-alone system.

 Software distribution. Updating the software and interface requires many separate installation and upgrades over time. This is often beyond the competence of the users.

 Communication between distributed applications. A lack of common protocols for knowledge transfer tends to discourage designs involving co-operation or dynamic information sharing.

Internet-centered information and communication technologies (ICT) are changing IS applications. Power [21] argued that rapid advances in Internet technologies have opened new opportunities for enhancing traditional DSS and ES. Internet technology can change the way that an ES is developed and distributed. For the first time, knowledge on any subject can directly be delivered to users through a webbased ES. Since its main function is to mimic expertise and distribute expert knowledge to non-experts, such benefits can be greatly enhanced by using the Internet. However, few web-based ES have been offered and analysed to shed light on the methodology and challenges of developing them [20,23]. This is all the more surprising when commercial ES development tools such as EXSYS CORVID<sup>TM</sup> and XpertRule Knowledge Builder<sup>TM</sup> have been extended to offer web-based delivery.

## 2. Current web-based expert systems applications

The literature appears to offer contradictory pictures on the status and use of web-based ES. Grove [13] provided some examples of web-based expert systems in industry, medicine, science and government and claimed that ‘‘there are now a large number of expert systems available on the Internet.’’ He argued that there are several factors that make the

Internet, by contrast to standalone platforms, an ideal base for KBS (knowledge based system) delivery. These factors include:

 The Internet is readily accessible.

 Web-browsers provide a common multimedia interface.

 Several Internet-compatible tools for KBS development are available.

 Internet-based applications are inherently portable.

 Emerging protocols support co-operation among KBS.

Grove also identified several problems in the development of web-based KBS:

 Keeping up with rapid technological change to servers, interface components, inference engines, and various protocols; and

 Reducing the potential delivery bottleneck caused by communication loads and a limited infrastructure.

Adams [1] pointed out that ‘‘there are numerous examples of expert systems on the web, but many of these systems are small, non-critical systems.’’ The most successful example is probably the web-based legal expert system reported by Bodine [4], who remarked that ‘‘Law firms are collecting hundreds of thousands of dollars in subscription fees from clients who use their question-and-answer advisory services based on the web.’

Contrary to Grove and Adams, Huntington [14] stated that ‘‘there are not many ES on the web’’ due to the fact that the Internet was not created with applications such as expert systems in mind. As a result, the manner in which the web and web browsers interface made it difficult to perform the actions required by ES. Athappilly [2] reported a ‘‘dynamic web-based knowledge system for prototype development for extended enterprise.’’ He suggested that the use of emerging Internet technology made the development of multifunctional AI systems relatively easy and less expensive, but that many users in the business arena were unaware of these technologies and their potential benefits. Consequently, the business community was not aware of the value or educated to deploy the potential available from these technologies in making their business more efficient and competitive.

## 3. Case studies of web-based expert systems

## 3.1. The knowledge engineering process as a framework for case studies

There are many different views of the traditional knowledge engineering process. Rather than discussing their merits, we start with that given in the well known text by Turban and Aronson [25].

Though the term knowledge engineering (KE) has been used in different contexts, such as knowledge management, the framework described here is relevant to any system development of AI and expert systems. It deals with knowledge acquisition, validation, representation, inferencing, explanation, and maintenance and includes five major activities:

 Knowledge acquisition. The acquisition of domain knowledge from identified sources, such as human experts, books, documents, WWW, sensors, etc.

 Knowledge validation. It is validated and verified against test cases until its quality is acceptable.

 Knowledge representation. The preparation of a knowledge map and encoding of the knowledge in the knowledge base.

 Inferencing. The design of software to allow the computer to make inferences based on the knowl edge and the specifics of the problem.

 Explanation and justification. The design and programming of an explanation capability; a program that allows the system to answer questions about a specific piece of information or how a certain conclusion was derived.

The KE process is therefore extended to include evaluation, implementation, and maintenance as depicted in Fig. 1. This extended process is used as a framework in the analysis and discussion of the three case studies.

## 3.2. Case 1: WITS

## 3.2.1. Domain background and system description

WITS, a web-based intelligent training and support system, was developed for providing training and intelligent support for small and medium sized enterprises (SMEs) in the use of information and communication technologies. It was a pilot research project funded by the European Commission’s Leonardo Da Vinci programme and was inspired by statements that lack of adequate skills and knowledge are major barriers that SMEs exhibit in successfully adopting and running e-commerce and e-business. As a result, there is an emerging need for better education and decision support for SME managers who are eager to embrace the technology and afraid of being left behind.

The e-business is not regarded as just a technical issue but, more importantly, a business issue. A sound understanding of the technical issues would help managers understand the methods but it does not guarantee a successful application. Since e-business will affect the whole business process, including the way business runs, managers need to be able to conduct business analysis and develop appropriate strategies. Companies should be willing to change their organization and business processes to exploit the opportunities when using e-commerce. Expert help on strategic and managerial issues is critical and this is reflected in the WITS system design, which consists of two components: WITS-training and WITS-advisor. The first aims to provide training material to SME managers who need to understand the technology and its application. It has three modules: the Internet and WWW, electronic data interchange (EDI), and e-commerce. It also has sections discussing frequently asked questions (FAQ), Internet and ecommerce Jargon, and case studies.

![](/api/attachments/DZF4XTK8/fulltext/images/d804cc512afd8f0c5a791cb01028880a056e74bb2017ff128ebe6bc67cafa21e.jpg)  
Fig. 1. Extended process of knowledge engineering (adapted from Turban and Aronson [25]).

WITS-advisor is the more important component; it can be regarded as a web-based ES. It has three subsystems that are designed to facilitate SME managers’ decision making in considering the adoption of ecommerce and e-business. Fig. 2 shows a sample screenshot of WITS. It helps SME managers assess their company’s business activities and develop an ecommerce strategy, with operational support for running the applications successfully. The components of the WITS function are as follows.

Business assessment. To help managers assess their company’s business performance and make recommendations on whether it needs an e-commerce solution. This forms an important part of any business strategy development. A manager should have a clear understanding of the company operations in order to decide where the company should automate the business. To help, business activities are classified into different functional areas, such as marketing, sales, and information management. To assess performance, users answer a number of questions about the effectiveness of their performance. The questions are carefully designed to evoke and support the managers’ critical understanding. Based on the answers, the system is able to provide a brief assessment of the business performance in each functional area and make provisional recommendations on the value of using Internet technology. The assessment results can be summarized and displayed in a bar chart and a summary table, as shown in Fig. 2. Business assessment not only serves to determine the company’s business performance, it also plays an important role in defining the strategy. The assessment outcome helps users decide their business objectives and how to achieve those objectives.

![](/api/attachments/DZF4XTK8/fulltext/images/7694020f8bfe581adc49af209a9c26660fabfda5b77d6031386e6739ad1ad495.jpg)  
Fig. 2. A sample screenshot of WITS business assessment.

Strategy development. To help managers to develop e-commerce strategy. Based on the business assessment, this sub-system works independently as an ebusiness strategy advisor. Developing e-commerce strategy with WITS-advisor involves selecting the business objective and then answering questions related to it. The system can recommend the ebusiness objectives based on the business assessment but users can still change the recommendations and select their own objectives. They must decide the degree to which they intend to achieve each of the objectives. These results help decide what e-commerce/e-business strategy should be considered.

Operational support. To provide information and guidelines at the operational level. E-Commerce is not a single event; its effective management and operations will ensure its continuing success. This sub system will provide interactive intelligent support using the knowledge base for solving operational problems in technical, security, and legal areas when users have been involved in e-commerce.

## 3.2.2. Knowledge engineering for WITS

The sources of knowledge were mainly documented materials and information collected from various sources, such as books, journal papers, magazines, documents from government organizations, and web sites. A few lecturers and technical experts were involved in contributing and validating knowledge. The main techniques for knowledge acquisition were text analysis and interviews. Knowledge was represented in simple production rules constructed in JavaScript and JavaApplets. No server-side processing was needed. A major disadvantage, however, was that once users logged out of the system, the data disappeared, as no historical data was saved as there was no server-side database to store it.

The system design involved specification of the individual pages and some knowledge base programming. The following development tools were employed:

 Web page design software.

 JavaScript which was mainly used to realize the ES functionality, such as knowledge representation and inferencing. There are two main benefits of using JavaScript:

\- Its programs are embedded in web pages executed automatically by the user’s browser. They do not need users to download or install them.

\- It has no special demand on hardware or software on the user’s computer.

 JavaApplets to run within the browser.

WITS was evaluated with different users, including SME managers, MBA and MSc students taking ebusiness related courses, and experts in the field of ICT training. A number of evaluation methods were used to determine the overall satisfaction, effectiveness, and usability of the WITS system; they included interviews, questionnaires, and user walkthroughs using verbal protocols. A paper-based questionnaire was filled in by users after using the system. An online evaluation form was also available to use. The results of the WITS initial evaluation were positive and encouraging. It achieved a high level of user satisfaction in terms of content, format, ease of use, accuracy and timeliness. However, some users felt that some recommendations and advice were too brief. More information on WITS initial evaluation can be found in [9].

## 3.2.3. Discussion

WITS is a client side ES without server-side data processing. It was easy to develop and can be used by anyone with Internet access and a web browser. The web-based ES made the evaluation and implementation of WITS easier than a conventional ES. There is no need to install the system in advance. It is easy to collect feedback. Visitors can be easily traced and analyzed. By collecting information, it was possible to profile the users and determine the value of the system. Compared with traditional ES development tools, the web design software simplifies the user interface design. HTML-based user interfaces allow the incorporation of rich media elements. Hyperlinks provide an extra facility in enhancing ES explanation and help functions; users can access the relevant web site easily. Also, the WWW helps in acquiring the knowledge needed in constructing the knowledge base. Any knowledge updating and maintenance can be handled centrally. Useful links are incorporated to help the user understand and interpret the ES recommendations. The e-mails, feedback forms and other Internet communication functions allow users to question and comment on the system.

However, it does not have an easy to use knowledge updating facility. Updating has to be performed by system developers. Other challenges include:

 Informing end users about the system updates and encouraging them to maintain contact with it.

 Making users inform system developers of their future needs.

 Concentrating on defining interfaces that provide up-to-date quality training materials and effective intelligent support.

The dynamic nature of business knowledge makes identifying and locating knowledge sources difficult and when searching the Internet for relevant knowledge, the sheer volume of information poses a challenge in scanning, filtering, and refining it.

## 3.3. Case 2: Fish-Expert

## 3.3.1. Domain background and system description

Fish disease diagnosis is a complicated process in aquaculture production activities. An infected fish will normally die quickly if treatment is not provided in time. Ideally, fish disease diagnosis and treatment should have on-the-spot investigation by a veterinary surgeon (vet), but in practice this is impossible due to the shortage of expertise and remote location of aquaculture sites. Most breeding sites are remote and in rural areas. The potential benefits of an ES are therefore clear. However, although some diseases involve a single infection, most are mixed with multiple pathogens. This poses a major challenge in developing an ES capable of providing accurate and timely diagnosis.

Fish-Expert is a web-based ES for fish disease diagnosis developed in China. This system can mimic human fish disease expertise and diagnose a number of fish diseases; it has a user-friendly interface. Fig. 3 shows its architecture. It contains a large amount of fish disease data and images used to conduct online disease diagnosis.

## 3.3.2. Knowledge engineering for Fish-Expert 3.3.2.1.

 Knowledge acquisition. Through years of experience, fish disease experts have developed a body of knowledge that they can use to make a diagnosis. A multiple knowledge acquisition (KA) approach was adopted in the project. It consisted of user surveys and interviews, expert interviews, case studies, and knowledge elicitation over the Internet.

 Surveying and interviewing farmers to understand and identify problems. Questionnaire surveys and interviews were carried out with around 130 fish farmers in an attempt to identify the common problems and diseases of fish farming. Much data was collected on symptoms. The farmers’ experience in identifying, preventing, and treating fish diseases was also collected.

 Interviewing human experts. Thirty-five fish disease experts from Beijing, Tianjin, and Shandong province took part in knowledge acquisition. Amongst them were the five most highly regarded experts of North China.

 Knowledge elicitation via the Internet. Aweb-based KA component was designed to help the experts and knowledge engineers gather facts and generate rules. An interface was designed to help collect data on fish disease symptoms, the treatment, and prevention methods. This online system helps experts input, update, modify and search data, information, and rules of the Fish-Expert knowledge and database. This process not only helps the knowledge engineer represent the domain knowledge correctly but also helps the expert clarify the reasoning processes. All domain knowledge is thus analyzed and represented in production rules in a rule base that is used to control the diagnostic process.

![](/api/attachments/DZF4XTK8/fulltext/images/aed1874198d61381ce86d12923918d78b436548b61bcff5b6d325895004838b6.jpg)  
Fig. 3. System architecture of Fish-Expert.

3.3.2.2. Development tool. Fish-Expert was developed using a mixture of Internet techniques and SQL. DHTML (Dynamic Hypertext Markup Language), JavaScript, Java, VB script, and ASP (Active Server Pages) were also used. A three-layer structure (client– web server–application server) was adopted. Several software packages, including Visual InterDev, Visual J++, and Photoshop5.0, were used in developing the system.

3.3.2.3. Database. The server-side database played an important role in the development. It was used for storing all the information needed for disease diagnosis. Most of the data and images were initially collected from fish disease experts using Excel spreadsheets whose information was then placed in SQL Server 7.0 by the system developers. The eight databases involved: symptoms, pond inspection, microscope examination, a water quality, fish medicine information, fish disease, a fish disease treatment and prevention, and an image base. Information on fish type, age, seasons, symptoms, causes of disease, and actions needed to establish the type of disease were included in the fish disease database. The graphic image base included fish disease symptom photos, microscopic examination data, and diagnosing results graphic data.

3.3.2.4. Knowledge base. The knowledge base contains rules for disease diagnosis. Each rule has two sections: symptom pattern and action represented as:

## IF symptom E THEN disease H

for example, if the head is black and the gill full of blood then the fish is suffering from gill rot.

A typical rule looks like:

IF ðspecies ðF1Þ; breeding condition ðFð1; 2ÞÞ;

symptoms ðC106; C203; T505ÞÞ

THEN ðdisease ðD12Þ; Action ðE33ÞÞ

Fish-Expert users can query the system using a forward chaining inference process that automatically matches facts against patterns to determine which rules are applicable.

3.3.2.5. User interface. A multimedia interface was used in the system. Matching of pre-defined text description and images of symptoms was provided to users who can choose text and/or images to describe the symptoms. Different interfaces were designed for pond inspection, fish inspection, etc. For example, in the fish inspection interface, users can input information by selecting matching symptom pictures and descriptions from eight symptom groups (single or multiple selections are allowed).

3.3.2.6. System testing and evaluation. System tests were carried out by the developers to make sure the system would work correctly before it was distributed to farmers. Fish-Expert was then made available for pilot implementation. User feedback was gathered by conducting interviews and collecting information using the built-in feedback interface. In general the system has been an effective and practical tool, but some shortcomings and limitations were found, such as performance brittleness. A tele-diagnosis system is being developed to overcome brittleness by engaging a human expert in a web-based telediagnostic process. More details can be found in [7,16]. The system is currently available on line for registered users and is regularly updated and improved.

## 3.3.3. Discussion

A number of points related to the benefits and challenges of web-based ES emerged:

 The use of an Internet database was effective in storing large amounts of facts and data for webbased inferencing.

 Online knowledge acquisition is welcomed by domain experts, but a knowledge engineer is still needed: the final responsibility of checking and updating the knowledge base still lies in his or her hands.

 Online user feedback and evaluation of the ES was effective and popular.

 Internet access speed was seen as a bottleneck for web-based ES applications; this is especially true in developing countries.

 Using HTML makes it easier to enhance the ES user interface. The multimedia interface was effective in helping the user query the system, but it slows down the access speed.

 Expert systems are not able to deal with exceptions or complex problems due to their inflexibility and the limitations of the knowledge base [22]. The interactive nature of Internet communication provides an opportunity to reduce these limitations as users can talk to a human expert via telediagnostic equipment.

## 3.4. Case 3: web-based IMIS

## 3.4.1. Domain background and system description

Instead of distributing knowledge through the Internet, an intelligent multimedia interview system (IMIS), collects information through computer-based interviews. It is a prototype system for conducting interviews for an interviewee’s psychological assessment. The domain expert is a clinical psychologist. He developed expertise in identifying whether company employees are psychologically healthy by assessing their psychological status and the company work environment. The assessment is conducted through interviews and observation. Interviewing employees is, however, extremely time consuming. Given that the expert’s time is expensive, there are benefits in a computer system with domain knowledge and a multimedia interface to act as the input device. A prototype intelligent interview system was developed to do so. Its major role was to act as an intelligent engine to search for appropriate questions. Multimedia methods were used for presenting questions, providing help, and giving explanations.

IMIS demonstrates how expert systems, multimedia, and the use of the Internet can enhance the performance of traditional computer-based interview systems. Analysis of the initial evaluations of IMIS showed that it was more effective and appealing to the interviewees.

The use of IMIS can assist experts by:

 Saving expert time. It is estimated that, by using a computerised interview system, the expert time could be reduced by 60%.

 Analysing the survey results. The data collected is stored in the database and easily analysed by the system’s built-in database analyser. In a face-toface interview an expert has to make notes and analyse the material immediately.

Though face-to-face interviews have many advantages, such as clarifying questions, better responses, and correcting misinterpretation, they have some drawbacks that IMIS can overcome. For example, IMIS can:

 be a useful tool for anonymous interviews when people are reluctant to have a face-to-face interview;

 eliminate personal bias. The computerised system will not be affected by environment, emotions, interviewees’ personal styles, and personal prejudice or attitude;

 be more attractive and appealing to interviewees.

## 3.4.2. Knowledge engineering for IMIS

Knowledge acquisition. As IMIS was designed to mimic one expert in psychological assessment interviews, only that expert was used as a knowledge source. A number of semi-structured and structured interviews were conducted with him.

Knowledge base. This was designed to contain the expert’s knowledge in the form of production rules. A typical IF–THEN–ELSE rule structure was considered to be inefficient for the knowledge base. Instead, a simple array (decision table) was used to represent the structure. The questions, answers, and subsequent questions were represented with an ID number. This is shown in Fig. 4.

This array represents rules in the following way: IF ðfor Quest 1 the Answer is 1Þ THEN ðnext Quest 2Þ IF ðfor Quest 1 the Answer is 2Þ THEN ðnext Quest 2Þ IF ðfor Quest 1 the Answer is 3Þ THEN ðnext Quest 4Þ

Fig. 5 shows the system architecture. All the files for the environment reside on a web server but when IMIS is running it uses a distributed architecture; some of the components reside on the server and some on the local machine. When IMIS is invoked via a standard web browser, all the necessary files for a particular interview session are downloaded to the local machine. This ensures a good balance of resources between the local client and the host server. Fig. 5 shows the basic system architecture when running a session. Use of the distributed architecture provides multiple user access. The system was developed using Java Media Framework for the multimedia applications.

<table><tr><td rowspan="2">Questions 1</td><td colspan="3">Answers</td></tr><tr><td>2</td><td>3</td><td></td></tr><tr><td>Quest 1</td><td>Quest 2</td><td>Quest 2</td><td>Quest 4</td></tr><tr><td>Quest 2</td><td>Quest 3</td><td>Quest 5</td><td>Quest 4</td></tr><tr><td>Quest 3</td><td>Quest 4</td><td>Quest 4</td><td>Quest 5</td></tr></table>

Fig. 4. Rule array structure.

![](/api/attachments/DZF4XTK8/fulltext/images/eb18437a82f15e66c53709962c2ccd8c0a830d0e61cc1bc5c549942111cd474b.jpg)  
Fig. 5. The system architecture of IMIS.

User interface. The GUI interacts with the user through a standard browser. As IMIS is multimedia enhanced, it interacts with the media base via the control module. The user responses are sent to the local database, again, via the control module.

Media base. This contains the video and audio files for an interview session. IMIS is capable of scheduling both audio and video for each set of questions. The files are loaded from the web server, for one interview session.

Control. This module controls events in the user interface and schedules the necessary audio, video, and questions for the interview session.

Database. The database is divided into a local database that collects the user responses and after one set has been completed, they are transferred to the host server database.

Question base. Each question is given an ID number and stored in an array.

Data analyser. The analytical tools used by the expert for data processing and result generation will be stored here; in conjunction with the knowledge base, a company profile can then be generated automatically. The data analyser has not yet been implemented.

System evaluation. The IMIS was evaluated by university students. The test was primarily concerned with the users’ views of its quality and student feelings about using a computer as an interview tool. Questionnaires were used for gathering opinions before and after they used the system. 20 people participated. Most of them felt that the quality of the multimedia was good. Seventeen felt that IMIS was very similar to a face-to-face interview. The use of video clips gave interviewees a more realistic scenario. A question about the use of video clips in increasing interview motivation resulted in 17 users saying that it did while three said it made no difference. Also, 16 people felt that watching video reduced their cognitive load when processing lengthy portions of print. Nineteen said that IMIS gave them more privacy than a face-to-face interview. More information can be found in [8].

## 3.4.3. Discussion

Again, the web-based nature of the system made access and use of the system straightforward. Users could log in and be interviewed provided that they could access the Internet. There was no need to install the system in different locations and collect individual responses. Technically, the combined server and client side data processing in IMIS ensured a balance of resources between the client PC and the host server. There were, however, some difficulties in using video in a web-based system. This again demonstrates that access speed is the bottleneck in the use of web-based ES.

## 4. Benefits and challenges

Benefits and challenges were examined from different perspectives: technological, methodological, and applications. Some insights obtained from involvement in developing the web-based ES are outlined in Table 1.

Knowledge acquisition. The impact of the Internet on knowledge acquisition can be profound. Firstly, it provides another valuable knowledge source. Secondly, it makes knowledge elicitation from the domain expert possible at a distance. Thirdly, as Basden [3] argued, the users can be closely involved in the selection and generation of the knowledge. However, these benefits bring with them problems and challenges including dealing with information overload, effective knowledge mining techniques, locating and verifying online experts, filtering knowledge, managing conflict when several online experts are involved, and security and reliability consideration.

Knowledge representation and inferencing. Traditional development methodologies, tools, and techniques that work effectively in a standalone environment may not work well in a web situation.

Knowledge validation. The knowledge validation, verification, and testing process is likely to be one of the most useful additions to ES development. Users can directly submit their test cases or provide feedback to system developers via the Internet. Alternatively, the knowledge base can be uploaded for validation and be accessed directly by users. However, this approach needs a centrally managed validation process. Generic online debugging tools would be welcomed by developers.

Explanation and justification. One of the distinguishing features of an ES is its ability to explain and justify results. This function is enhanced by using Internet technology. It is also possible to receive explanation and justification from a human expert via the Internet. Therefore, future web-based ES shells could have built-in functions to facilitate online real time communications.

System evaluation, implementation, and maintenance. From the users’ point of view, systems can be easily accessed globally; their location is irrelevant and no installation is needed at the users’ location. Any updating and maintenance can be carried out centrally. Users’ feedback can be collected via online feedback forms for later analysis. Web-site analysis tools can be installed to trace the number of visitors and their behaviour; this is not normally possible with traditional ES. As the system can be operated at the site of the originators who are responsible for it, its maintenance, upgrading, and monitoring can be more effective and efficient.

Experience with the Fish-Expert implementation suggested that performance brittleness could be partially answered by using tele-communication tools.

Web-based ES development tools. Traditional ES were developed for standalone computers. However, many shells do not support the openness and interoperability required for deploying ES over a wide area network [24]. Unfortunately, the web was originally conceived as a document distribution infrastructure and any attempt to use it for distributing expert systems must cope with difficulties. Some webbased ES tools are commercially available, but no formal evaluation and comparison of different ones has been conducted.

Table 1  
Benefits and challenges of web-based expert systems

<table><tr><td>Process of knowledge engineering</td><td>Internet opportunities and benefits</td><td>Challenges</td></tr><tr><td>Knowledge acquisition</td><td>New knowledge sourcesUse of intelligent agent for knowledgeSearching, scanning and refiningOnline knowledge acquisition and updating by domain experts to save travel cost and expert&#x27;s timeOnline community as a potential source of knowledge</td><td>Information overloadKnowledge mining on the InternetLocating and verifying online “experts”Responsibility issues on checking conflicting and invalid knowledge collected onlineSecurity issuesInterface design issues</td></tr><tr><td>Knowledge representation</td><td>Sharing of online knowledge representation tools</td><td>Development of web-based ES shellsTools for online knowledge induction and representationEffective online knowledge base management techniquesTransfer of local knowledge base into the web-based system automatically</td></tr><tr><td>Knowledge validation</td><td>Testing cases submitted by users via the Internet Involving users in validation process with online feedback form</td><td>Central management of the validation processDevelopment of generic online debugging tool</td></tr><tr><td>Inferencing</td><td>Sharing of online inference tools</td><td>Use of server and client side inferencingSpeed considerationsDevelopment of common inference enginesKeeping up with the rapid changes in web technologies</td></tr><tr><td>Explanation and justification</td><td>Enhance traditional explanation and justification functions with hyperlinks to other relevant sitesPossibility for tele-consulting with real expert through video conferencing, chat room, message board and email facilities</td><td>Internet speed bottleneckfor tele-consultingDevelopment of built-in facilityfor online explanation and justification</td></tr><tr><td>System evaluation, implementation and maintenance</td><td>Online user evaluationKnowledge available across boundaries of geography, culture, or even economic statusPossibility of dealing with exceptions by involving real expert via web-based facilities, such as:video conferencing, chat room, discussion forum, etc.End user computing via the InternetCollection of user feedback via online formsCentrally-controlled updating and maintenance</td><td>Offline user support when the user base grows in size and in geographical locationInternet access speed bottleneckProject managementResponsibility issues for system management and maintenanceHow to make local ES available on the web easilyIntellectual property protection and security issues</td></tr></table>

Though our paper focused on benefits and challenges for web-based expert systems, some of them may also be applicable to information systems in general.

## 5. Conclusion

The rapid development of Internet technology has changed the way that expert systems can be developed and distributed. The essence of an expert system is to mimic expertise and distribute expert knowledge into non-experts’ hands. This can be enhanced significantly by using the Internet.

From our searches of the literature, which found little reporting on the topic, we ask: are there few ES on the web or are they there but not being reported in the literature? There also appears to be a lack of a general methodology for developing web-based expert systems. We believe that web-based expert systems will become more sophisticated, complex, and capable and fulfil their great promise. However, this requires effort to address the challenges discussed in this paper. It is anticipated that web-based expert systems could bring new life to the field of expert systems and generate a new era for their applications.

## Acknowledgements

The authors would like to express their gratitude to the following people for their contribution to developing the web-based expert systems discussed in the paper: Prof. Zetain Fu and Dr. Daoliang Li of China Agriculture University (Fish-Expert); Roisin Mullins of the University of Wales, Lampeter (WITStraining) and Yuangu Lei of the Knowledge Media Institute, Open University (WITS-advisor); Dr. Phillip Burrell and Jose M. Gost of South Bank University (web-based IMIS).

## References

[1] J.A. Adams, The feasibility of distributed web based expert systems, in: Proceedings of the 2001 IEEE International Conference on Systems, Man, and Cybernetics, Tucson, AZ, October, 2001.

[2] K. Athappilly, A dynamic web-based knowledge system for prototype development for extended enterprise, in: Proceedings of the 3rd International Conference on the Practical Applications of Knowledge Management, PAKEM 2000, Manchester, April, 2000.

[3] A. Basden, Some technical and no-technical issues in implementing a knowledge server, Software — Practice and Experi ence 30(10), 2000, pp. 1127–1164.

[4] L. Bodine, Finding new profits: delivering legal services via web-based expert systems. The LawMarketing Portal, last accessed at 21 May 2003 at http://www.lawmarketing.com publications/legalmarketingtech/pub34.cfm.

[5] E. Coakes, K. Merchant, Expert systems: a survey of their use in UK business, Information and Management 30(5), 1996, pp. 223–230.

[6] K. Darlington, The Essence of Expert Systems, Prentice-Hall, Essex, England, 2000.

[7] Y. Duan, R. Mullins, Project report on WITS system evaluation, Luton Business School, University of Luton, 2001.

[8] Y. Duan, P. Burrell, J.M. Gost, Enhance web-based interview system with expert systems and multimedia, in: Proceedings of the IASTED International Conference on Applied Informatics, AI 2001, Innsbruck, Austria, February, 2001, pp. 160–165.

[9] Y. Duan, Z. Fu, D. Li, Towards developing and using webbased tele-diagnosis in aquaculture expert systems with applications, An International Journal 25(2), 2003, pp. 247–254.

[10] J.D. Durkin, Expert systems: a view of the field, IEEE Expert 11(2), 1996, pp. 56–63.

[11] T.G. Gill, Early expert systems: where are they now? MIS Quarterly 19(1), 1995, pp. 51–81.

[12] R.F. Grove, Design and development of knowledge-based systems on the web, in: Proceedings of ISCA 2000: Ninth International Conference on Intelligence Systems: Artificial Intelligence Applications for the New Millennium, Louisville, KY, USA, June 2000, International Society of Computer Applications (ISCA), 2000, pp. 147–150.

[13] R.F. Grove, Internet-based expert systems, Expert Systems 17(3), 2000, pp. 129–136.

[14] D. Huntington, Web-based expert systems are on the way: Java-based web delivery, PC AI Intelligent Solutions for Desktop Computers 14(6), 2000, pp. 34–36.

[15] A.S. Kunnathur, M. Ahmed, R.J.S. Charles, Expert systems adoption: an analytical study of managerial issues and concerns, Information and Management 30(1), 1996, pp. 15–25.

[16] D. Li, Z.Y. Fu, Duan Fish-Expert: a web-based expert system for fish disease diagnosis, Expert Systems with Applications: An International Journal 23(3), 2002, pp. 311–320.

[17] K. Metaxiotis, J. Psarras, Expert Systems in business: applications and future directions for the operations researcher, Industrial Management and Data Systems 103(5), 2003, pp. 358–361.

[18] R.M. O’keefe, D. Rebne, Understanding the applicability of expert systems, International Journal of Applied Expert Systems 1(1), 1993, pp. 3–24.

[19] E. Oz, J. Fedorowicz, T. Stapleton, Improving quality, speed and confidence in decision making: measuring expert system benefits, Information and Management 24(2), 1993, pp. 71–82.

[20] W.D. Potter, X. Deng, J. Li, M. Xu, Y. Wei, I. Lappas, M.J. Twery, D.J. Bennett, A web-based expert system for gypsy moth risk assessment, Computers and Electronics in Agriculture 27(1–3), 2000, pp. 95–105.

[21] D.J. Power, Web-based and model-driven decision support systems: concepts and issues, in: Proceedings of the Americas Conference on Information Systems (AMCIS 2000), Long Beach, CA, August, 2000.

[22] B.G. Raggad, M.L. Gargano, Expert systems: defection and perfection, Logistics Information Management 12(5), 1999, pp. 395–406.

[23] A. Riva, R. Bellazzi, S. Montani, A knowledge-based web server as a development environment for web-based knowledge servers, IEE Colloquium on Web-based Knowledge Servers (Digest No. 1998/307), May, London, UK, 1998.

[24] T.A. Sedbrook, A collaborative fuzzy expert system for the web, Data Base for Advances in Information Systems 29(3), 1998, pp. 19–30.

[25] E. Turban, J.E. Aronson, Decision Support Systems and Intelligent Systems, 6th ed., Prentice-Hall, Upper Saddle River, NJ, 2001.

[26] B.K. Wong, The role of top management in the development of expert systems, Journal of Systems Management 47(4), 1996, pp. 36–40.

[27] B.K. Wong, J.A. Monaco, Expert system applications in business: a review and analysis of the literature, Information and Management 9(3), 1995, pp. 141–152.

[28] Y. Yoon, T. Guimaraes, Q. O’neal, Exploring the factors associated with expert systems success, MIS Quarterly 19(1), 1995, pp. 83–106.

Y. Duan (PhD) is a Principal Research Fellow at Luton Business School, University of Luton. She received her BSc and MSc from China Agriculture University, and her PhD from Aston Business School, Aston University. Her principal research interest is the development and use of intelligent systems in business and management, especially for decision-making, marketing planning and e-business. She is also interested in knowledge management in SMEs and e-learning. She has published widely in international journals and books.

J.S. Edwards is Professor of Operational Research and Systems, and Head of Academic Programmes at Aston Business School, Birmingham, UK. He has an MA in mathematics and a PhD degree from the University of Cambridge. His doctorate was in human resource planning models. His principal research interests now are in knowledge management, especially methods for the development of knowledge-based systems and decision support systems. He has published more than 40 research articles on these topics, and two books, Building Knowledge-based Systems and Decision Making with Computers. He is editor of the journal Knowledge Management Research and Practice.

M.X. Xu (PhD) is a senior lecturer at University of Portsmouth. He is author of CIMA (UK) study books, and has published widely in international journals and books. His research interests are in ebusiness strategy and implementation, Executive information systems and strategic information management. He serves in editorial board for a number of international journals.
