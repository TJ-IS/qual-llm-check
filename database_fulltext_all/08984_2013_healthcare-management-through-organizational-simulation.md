---
otero_id: 8984
otero_key: "PKP8D54H"
title: "Healthcare management through organizational simulation"
authors: "Rahul C. Basole; Douglas A. Bodner; William B. Rouse"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Rahul C. Basole <sup>a,</sup>⁎, Douglas A. Bodner <sup>b</sup>, William B. Rouse <sup>c</sup>

<sup>a</sup> School of Interactive Computing & Tennenbaum Institute, Georgia Institute of Technology, 85 Fifth Street, NW, Atlanta, GA 30332, United States

<sup>b</sup> Tennenbaum Institute, Georgia Institute of Technology, 75 Fifth Street, NW, Atlanta, GA 30332, United States

<sup>c</sup> School of Systems & Enterprises, Stevens Institute of Technology, Castle Point on Hudson, Hoboken, NJ 07030, United States

## a r t i c l e i n f o

Available online 5 October 2012

Keywords: Healthcare management Organizational simulation Serious games Health Advisor Information complexity Decision-making

## a b s t r a c t

Quality, affordable healthcare remains a contentious, complex and urgent societal problem. Given the scale and complexity of healthcare, systemic changes addressing emergent cost escalation and quality de<sup>fi</sup>ciencies are dif<sup>fi</sup>cult to study, evaluate, and implement. In particular, it is dif<sup>fi</sup>cult to empirically study alternative means of delivery that do not yet exist. To enable the study of such issues, we designed and developed Health Advisor, a web-based game using organizational simulation. Players are tasked to manage people through the healthcare system by making various information, cost, and quality of care trade-offs with score based on health outcomes and costs incurred. This paper reports on a series of evaluations of Health Advisor and the insights gained from these studies. In particular, results show that people's perceptions of the usability and usefulness of information sources have a strong impact on the use of these sources, and a signi<sup>fi</sup>cant impact on their subsequent performance in diagnoses and referrals.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Quality, affordable healthcare remains one of the most contentious, complex and urgent problems facing U.S. policy‐makers, businesses and the public at large [42]. Recent statistics have shown that healthcare costs are increasing dramatically, both to consumers and as a percentage of GDP [9]. At the same time, there are signi<sup>fi</sup>cant issues of quality in the healthcare system, exempli<sup>fi</sup>ed by high levels of inappropriate care [25]. Several studies point to systemic problems that prevent cost‐effective quality, among them the organization of the overall healthcare system, increasing complexity of care, insuf<sup>fi</sup>- cient information support, a lack of patient lifecycle management, and misaligned incentives that motivate dysfunctional provider behaviors [17,30,42]. This conclusion highlights the nature of the U.S. healthcare system as a complex adaptive system [36]. A complex adaptive system differs from traditional systems in that outcomes and performance are determined by a heterogeneous set of actors and their interactions, rather than as a result of intentional system design or by a central command‐and‐control function. This is particularly the case in the context of healthcare, in which a myriad of providers, insurers, businesses, government agencies, and consumers interact to provide healthcare products and services [4,39]; not surprisingly, the result is emergent (i.e., unintended and unplanned) cost and quality de<sup>fi</sup>ciencies.

Although there are many reform ideas for providing quality healthcare and insurance coverage to the public, while at the same time containing or reducing sky‐rocketing costs, there is no consensus and few or no ways to test novel ideas at scale. Unquestionably, substantial systemic changes in healthcare are dif<sup>fi</sup>cult to implement and evaluate. Potential healthcare innovations may succeed or fail based on reactions of this diverse set of agents. Piecemeal investments or reforms to improve healthcare have seldom affected the overall enterprise. A broader set of ideas and initiatives are needed to affect sustainable, valuable change [42].

Recent attention has focused on the application of systems engineering (SE) methods to study these complex healthcare system issues [2,35,42]. While it is unlikely that healthcare will become a designed system in an engineering sense, the goal is to use SE methods to improve system operation and outcomes. Our research uses an emerging SE method, organizational simulation [41], to create a web‐based game called Health Advisor. Players have the objective of managing a set of clients through the healthcare system by making various information, cost, and quality of care trade‐off decisions. People are clients rather than patients as the players are not clinicians — they provide advice rather than diagnosis and treatment.

The emphasis of the game is thus on understanding healthcare decision‐making and behavior in terms of routing clients through the system in a way that provides high-value care while also sustaining the health advising business. The primary objective of our research is to assess the impact of information on healthcare delivery strategies and, consequently, health states and costs. More speci<sup>fi</sup>cally, our objective is to use this “serious” game as a platform to study what strategies players employ to maximize healthcare value, what information they access to make decisions, and how they hedge the downside risks of client costs. Our research paradigm is premised on the value of wisdom of crowds or crowd sourcing [16,50], the notion that a large number of people addressing a problem is likely to result in a handful of novel and important ideas for improving healthcare delivery. For example, what if we could let 10,000 12-year olds run healthcare? What successful strategies would emerge? What would we learn? To this end, our game is designed to capture players' strategies and assess the performance of these strategies. A secondary objective is focused on potential applications in education, ranging from health bene<sup>fi</sup>t functions in enterprises to student education in medical, nursing, public health, and business schools.

Research on the Industrial Revolution [34] and more recent times of great innovations suggest that a large number of people being motivated to invent ideas and then trying to morph them into market innovations will, over time, result in a few great ideas that prevail. For systems like healthcare delivery, there is no readily available way for people to experiment with different approaches to running the overall system. This is true for many types of large public–private systems that can be characterized as federations of large numbers of organizations with, in effect, no one in charge. Organizational simulation can provide a platform for such experimentation and enable the generation and evaluation of a large number of ideas for improving the overall organizational system. The key is to create a valid representation of the system – so that insights gained are meaningful – and a compelling simulation environment – so that people will be motivated to gain insights and demonstrate new ways of running the system.

## 2. Organizational simulation and healthcare

Computer simulation is a well-established method of analyzing systems for purposes of decision support in design and on-going improvement. Traditional engineering approaches to simulation focus on the technical and process aspects of systems. For instance, simulation has been used extensively over the past forty years to study and improve factory performance, where the focus has been on <sup>fl</sup>ow of raw and intermediate materials as they are transformed to <sup>fi</sup>nished goods via manufacturing processes [44]. Similarly, this work has been extended to the domain of supply chains, where the focus is on the <sup>fl</sup>ow of good from sources, through a manufacturing and assembly network, then through a distribution facility network, to the <sup>fi</sup>nal stage where end consumers take possession of <sup>fi</sup>nished goods [5]. These types of simulation models typically involve discreteevent, process oriented simulation technology [20].

Other types of simulation technology include system dynamics simulation [46] and agent-based simulation [14]. System dynamics models focus on continuous processes, <sup>fl</sup>ow rates and feedback phenomena and typically are used to represent continuous technical processes (e.g., a re<sup>fi</sup>nery) or population level effects (e.g., disease transmission). Agent-based models, on the other hand, focus on individual system component behaviors and how those behaviors interact to form emergent system behavior. Such models may, for instance, be used to study the interaction of people in a social setting (e.g., rumor transmission or product adoption).

Clearly, a variety of simulation technologies exist to support a variety of different modeling needs. What perhaps has been missing, though, is a focus on one of the fundamental artifacts of society — organizations. Organizations feature a combination of technical behavior, processes, human behavior, and social network phenomena, among other things. As such, they present a potentially rich domain for simulation analysis. A variety of research has studied organizational modeling and simulation [6,8,28,31,40,41].

Organizational simulation focuses on a number of key themes. These include business process modeling, individual and team behavior modeling, decision logic modeling and organizational performance and value modeling. Organizational simulations may offer an immersive experience for the analyst or user, providing a means to experience organizational futures given different decisions about the future, before those decisions are implemented. The organizational story, characters and world model form the core of the simulated world. This model is implemented using simulation software that runs on computers, perhaps in a networked system. It is presented to the user with a visualization interface and perhaps guidance through the simulated story. An organizational simulation may be purely constructive, or it may engage human-in-the-loop technology so that one or more people interact with the simulated world.

In traditional simulation, the world model is typically the most mature component. Representing realistic human behavior is noted as a grand challenge in simulation [54]. Thus, organizational simulation looks to <sup>fi</sup>elds such as interactive computing (e.g., serious gaming and interactive drama) for technologies to support the organizational story and character models. Arti<sup>fi</sup>cial intelligence concepts such as drama management [33] and character programming frameworks [23] potentially address these concepts, respectively.

Consider healthcare as a set of phenomena that occur in an organizational context. The most fundamental aspect of this domain is the patient who seeks treatment from a doctor for an illness. The doctor typically is a sole proprietor, belongs to a practice, or is employed by a hospital. The patient, on the other hand, is usually an employee whose employer provides insurance that hopefully pays for doctor services. Thus, two immediate organizational contexts are the healthcare provider organization and the healthcare payer organization. Both organizations seek to pro<sup>fi</sup>t and provide quality healthcare outcomes, although perhaps with different perspectives.

Expanding this notion, government increasingly is involved in the healthcare sector, both as a payer and a regulator. Third-party services provide devices, pharmaceuticals and information technology. This presents a multi-organizational, or enterprise perspective to the system being modeled. Fig. 1 provides a framework for healthcare phenomena in an organizational context [42].

The healthcare <sup>fi</sup>eld increasingly is using simulation to aid efforts aimed at ef<sup>fi</sup>ciency [13]. This type of usage is analogous to the use of constructive simulation to study factory performance. Simulation is increasingly being used to aid with clinical decision support. For example, Mathe et al. [24] report on a decision support system that uses an underlying simulation model to aid with disease management. This model integrates disease and treatment modeling with process phenomena such as privacy and security protocols. It is based on a generic representation that provides domain-speci<sup>fi</sup>c model specialization [19].

This type of model-based decision support depends on such things as disease progression modeling [12,47]. Sumner et al. [49] present the use of a virtual patient simulator to support testing and diagnosis. This is based on a Bayesian network formalism that underpins the simulation of patient disease progression over time [48].

The use of such model-based decision support tools points to a critical issue. Healthcare is a complex <sup>fi</sup>eld, requiring detailed knowledge about:

• medical phenomena, interventions and progression over time;

• organizational and inter-organizational processes that dictate, among other things, patient <sup>fl</sup>ow and information <sup>fl</sup>ow;

• costs, reimbursement and capitation rules, and trade-offs between cost and health outcomes;

• the effect of incentives and information on individual actor behavior and overall system performance.

Quite clearly, it is beyond any one individual to comprehend the knowledge to optimize the healthcare system. Basole and Rouse [4] study the complexity of different industries and conclude that successful industries tend to address information complexity in back-room systems that end-users do not experience, while providing relatively simple interfaces to support end-user decision-making. Alas, in this respect, healthcare cannot be said to fall into the category of successful industries. This paper explores the use of organizational simulation as a potential method by which insight can be gained into trade-offs between information complexity and management versus effective decision-making in healthcare.

![](/api/attachments/PKP8D54H/fulltext/images/c4830adc7a8537bd160212e8b1a0d3d044588931cb3de4bd1770e56fe3543616.jpg)  
Fig. 1. Healthcare modeling context.

## 3. Health Advisor: concept and prototype

Health Advisor is a web-based game in which players assume the role of a health advisor. A health advisor manages healthcare delivery for clients<sup>1</sup> by assessing and monitoring their healthcare needs and referring them to medical providers (e.g. general practitioners and specialists) for tests and treatments. For this advising service, health advisors are paid an annual fee by clients and incur the cost of their health services. The health advisor represents a new type of business model. The value-add of this business model is that the health advisor has access to information, such as provider cost, availability and performance. The typical consumer, of course, does not generally have access to this type of information. The advisor's service, therefore, is to use this information to make referrals that improve the client's outcomes, either by reducing cost, improving health outcomes, or both. In our game, the goal of the health advisor is to maximize her score de<sup>fi</sup>ned by the average health state of clients divided by the costs of providing health care. The ratio of these two factors is commonly referred to as healthcare value [30].

It is important to note that some of the functions of health advisors are emerging in terms of health coaches and partners [32]. These types of personnel use health assessments to support people in setting goals, developing plans to achieve goals, and executing and adapting plans to ongoing results. This is driven in part from a need to decrease the cost of labor in the delivery system [37,38]. Thus, the notion of health advisor explored in this paper represents a likely new approach to delivery, albeit one that does not yet fully exist. This is why we have explored the nature of this role using organizational simulation. Table 1 summarizes the game data types and elements. The following sections describe them in further detail.

## 3.1. Game flow

At the start of game play, advisors enter their of<sup>fi</sup>ce and choose whether to see a client, or to review client records, provider information, or their current performance score. During an appointment, the advisor interacts with the client, asks relevant questions, accesses the client's electronic health record (EHR), obtains relevant medical

## Table 1

Summary of game data types.

<table><tr><td>Data type</td><td>Elements</td></tr><tr><td>Advisor</td><td>Appointment list, revenues produced so far, costs incurred so far, assessment accuracy, and fees charged to clients</td></tr><tr><td>Client</td><td>Name, birth date, gender, personality type, health history prior to first visit, current lifestyle (e.g., smoking, amount of exercise), current disease and severity level</td></tr><tr><td>Dialog</td><td>Dialog lines available to the user during an appointment, and response lines available to a client in response to user dialog (parameterized by personality type, symptoms, lifestyle, health history, etc.)</td></tr><tr><td>Disease, severity, and symptom</td><td>Different symptoms known to be associated with diseases at certain severity levels</td></tr><tr><td>Disease progression</td><td>Markov probabilities of transition from one severity level to another by discrete time interval</td></tr><tr><td>EHR</td><td>Health history as first reported to the user, diagnosis history, treatment history, and lifestyle information as subsequently reported to the user</td></tr><tr><td>Provider</td><td>Name, cost, performance, and appointment schedule (used to determine availability)</td></tr><tr><td>Tests and treatments</td><td>Tests and treatments that user can select, medical recommendations by disease, and cost by doctor</td></tr></table>

![](/api/attachments/PKP8D54H/fulltext/images/0c53d96f7546f6ae0ee37466bd9657832533c43c919372216340e802d464a4c0.jpg)  
Fig. 2. Game <sup>fl</sup>ow.

information through Med<sup>fi</sup>le (an online medical information source), and based on assessment of the client's condition, makes a referral to a provider.<sup>2</sup> Tests, treatments, and disease progression occur outside the health advisor's “game world” and are performed in the background by the simulation engine. Clients return back to the health advisor after a certain period of time for a follow-up meeting. Fig. 2 shows an outline of the basic game <sup>fl</sup>ow.

## 3.2. Game characters

The game has two classes of non-player characters. The <sup>fi</sup>rst consists of the clients whom the advisors serve. The second consists of the providers to whom the advisors refer clients. The advisors have a direct interaction with clients in that they see clients and have a dialog with them. The advisors do not have a direct interaction with providers.

## 3.2.1. Clients

Our aim was to create a large set of clients with a broad range of characteristics, including age, gender, race, lifestyle, and disease. Clients are assumed to be from the general U.S. adult population. Consequently, clients are sick in proportion to national morbidity rates. Each client has a speci<sup>fi</sup>c disease and severity level. The assigned disease had to be representative of the age, race, and gender of the client. Clients were also assigned a set of lifestyle characteristics, which includes different levels of diet, exercise, and stress, which could impact the advisors' assessment and referral decisions. To ensure further game realism, each client was given a <sup>fi</sup>rst and last name. Names were selected based on the age (i.e. traditional names were used for older clients), race, and gender of the client. We also used facial images for each client and ensured it matched the client demographic [26]. Our <sup>fi</sup>nal population contained 433 clients (Table 2).

## 3.2.2. Providers

The game models two categories of providers: primary care physicians (PCP) and specialists. A complete list of specialists can be found in Table 3. Each provider has a cost and quality associated with them.

Table 2 Client descriptives. Adapted from [26].

<table><tr><td rowspan="3">Race</td><td colspan="8">Age</td></tr><tr><td colspan="2">18–29</td><td colspan="2">30–49</td><td colspan="2">50–69</td><td colspan="2">70–93</td></tr><tr><td>Male</td><td>Female</td><td>Male</td><td>Female</td><td>Male</td><td>Female</td><td>Male</td><td>Female</td></tr><tr><td>African-American</td><td>14</td><td>29</td><td>7</td><td>9</td><td>3</td><td>12</td><td>2</td><td>13</td></tr><tr><td>Caucasian</td><td>42</td><td>45</td><td>22</td><td>28</td><td>23</td><td>52</td><td>26</td><td>47</td></tr><tr><td>Other</td><td>38</td><td>11</td><td>3</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Totals</td><td>94</td><td>85</td><td>32</td><td>39</td><td>28</td><td>65</td><td>29</td><td>61</td></tr></table>

The cost ranges from 1 to 10 and quality ranges from 1 to 100. While cost information is to a certain extent available and transparent today, quality information is less common. We assign cost ratings based on our understanding of the type of tests and treatments performed by PCPs and specialists. An appointment with a primary care physician is likely to be less costly, but if the condition is advanced may delay needed treatment. Similarly, a specialist's fee may not be cost-effective for a mild condition. Along the same lines, PCPs cannot treat advanced severities, while specialists can. The player must make this trade-off based on his or her judgment.

## 3.3. Game design

## 3.3.1. Diseases and symptoms

A client can have one of any of nineteen diseases. These diseases include breast cancer, colon cancer, lung cancer, prostate cancer, coronary artery disease, arrhythmias, heart valve disease, heart failure, stroke, bronchitis, emphysema, asthma, diabetes (type 1 and type 2), in<sup>fl</sup>uenza, pneumonia, Alzheimer's, nephritis and septicemia.<sup>3</sup> Diseases have severity levels such as asymptomatic, symptomatic, chronic and acute. Severity levels change in the course of time due to (a) natural disease progression or (b) the effect of treatment interventions. A severity level transition diagram is shown in Fig. 3. The arcs represent the transition probabilities between severity states. Note that it is possible for two transitions to be possible from a given state (e.g., transition from chronic to acute or recovered). The probabilities can be set to match a particular disease's progression pattern and transition probabilities. Thus, an acute disease may have positive transition probabilities only on those arcs that do not connect with the chronic severity state. A chronic disease, on the other hand, is likely to have positive transition probabilities on all arcs.

Table 3  
List of specialist providers.

<table><tr><td>Allergy and immunology</td><td>Neonatology</td><td>Psychiatry</td></tr><tr><td>Cardiology</td><td>Nephrology</td><td>Psychology</td></tr><tr><td>Dentistry</td><td>Neurology</td><td>Pulmonary diseases</td></tr><tr><td>Dermatology</td><td>Ophthalmology</td><td>Radiation oncology</td></tr><tr><td>Endocrinology</td><td>Orthopedics</td><td>Rheumatology</td></tr><tr><td>Gastroenterology</td><td>Otorhinolaryngology (ear/nose/throat)</td><td>Urology</td></tr><tr><td>Hematology/oncology</td><td>Physical medicine and rehabilitation</td><td></td></tr><tr><td>Infectious disease</td><td>Podiatry</td><td></td></tr></table>

We assume a baseline transition probability matrix for each disease. This matrix contains the baseline transition probabilities between each set of severities for the particular disease. These baseline probabilities are affected by age, sex and risk factors. For example, the transition probabilities for Alzheimer's are zero when age is below a certain threshold, and will increase with increasing age afterward. In addition, for any particular client, we assume that the transition probabilities for each disease are independent of other diseases — i.e., progression of one disease does not cause progression of any other. We realize that this is a limiting assumption for diseases such as diabetes and cardiovascular disease (CVD) and we expect to remove this constraint in later versions of Health Advisor.

Disease progression is assumed to occur as a Markovian process, whereby for any given disease, a client may experience a transition from one severity to another at discrete points in time. A client who is asymptomatic with heart disease, for example, has a certain probability of transitioning from that severity to symptomatic. Transition probabilities are compiled from various medical studies sources, including feedback from experts. It should be noted that the <sup>fi</sup>delity and accuracy of transition probabilities are rough estimates. Exact transition probabilities are very dif<sup>fi</sup>cult to estimate without considerable additional health information, e.g. see [52,53]. Within the game, transitions occur at periodic game status update (i.e., the transition points), and are executed by the simulation engine. The transition probability remains the same at each transition point. Thus, over time, the cumulative probability of transition increases. Transition paths are determined by Monte Carlo sampling.

Both health advisors and providers do not know a client's true health state, but rather must diagnose it based on symptoms. Thus, each client has a symptom state. The symptom state is modeled as a pair of disease (cause) and symptom. For each of the aforementioned diseases and their severity levels, we therefore have a set of symptoms. These symptoms are based on medical knowledge. For any disease not represented in a client's set of health state pairs, the client is asymptomatic. Some symptoms may be experienced in multiple diseases and a client may also have symptoms not related to their actual disease and severity level. Thus, a health advisor faces potentially signi<sup>fi</sup>cant challenges in assessing the disease of a client for treatment recommendations.

## 3.3.2. Assessment and referral

We considered a number of important issues in design of the assessment dialog between players and clients in Health Advisor. Our <sup>fi</sup>rst goal was to ensure that the content of clients' statements roughly re<sup>fl</sup>ects ground truth, although clients do not fully know their health states. Similarly, the content of clients' statements should re<sup>fl</sup>ect their previous treatments, the speci<sup>fi</sup>c providers they have seen, and past conversations with the player. Furthermore, the health state of the client frames the symptoms that they will divulge — if probed by the player. The ways in which they state the experienced symptoms also depend on previous dialogs with the player – in both current and past meetings – and their personality. We thus created emotional state based characters. As a result, clients' statements are modeled to be neutral, nervous, con<sup>fi</sup>dent, know-it-all, passive, or collaborative.

The general setting of a client–advisor dialog is across the player's desk. Dialogs begin with an introduction by the health advisor (e.g. “Hello” or “How are you doing?”). Dialog then proceeds as a series of questions posed by the advisor and answers offered by the client. Questions posed by the advisor relate to symptoms, previous diagnoses, risk factors, payment and treatments. Client response will depend on whether this is the <sup>fi</sup>rst meeting or a follow up meeting. In order to ensure consistency and dialog logic, we developed a “client–advisor dialog” state as well as a rule-set to determine allowable transitions between states. This capability allowed us to keep track of the course of an appointment and responses from previous ones. This is important as it ensured, for example, that if the same question was asked twice during an appointment, a client's response would re<sup>fl</sup>ect that.

We assume that, in any one appointment, the advisor addresses only one disease. Thus after a health advisor has reached a satisfactory level of insight into a client's conditions and gauged the likely disease and severity level – obtained through the dialog or access to the EHR or Med<sup>fi</sup>le – the player makes an assessment through a selection of one of four options:

• Advisor needs further information.

• Client has a problem/issue with a particular area or system.

• Advisor suspects that client has a particular disease.

• Advisor suspects that client has a particular disease and severity level.

![](/api/attachments/PKP8D54H/fulltext/images/5b43126b934e503fdda368cb05f7ba50086b721134082bfb016f08f2a2cbe30a.jpg)  
Fig. 3. Disease severity state transitions

An appointment <sup>fi</sup>nishes with a referral made by the health advisor. A referral includes the decision of whether to send a client to a PCP or a specialist and the type of test or treatment the provider should perform. Players must make cost, performance, and availability trade-offs when selecting a provider. Players make a referral through the selection of a speci<sup>fi</sup>c PCP or specialist from a list of providers as well as a list of diagnosis tests and treatments.

## 3.3.3. Diagnosis and treatment

Similar to disease progression, provider diagnoses and treatment occurs outside of the player's game experience. Each provider has a probability of correct diagnosis of a disease-severity pair. For a specialist, this probability is constant across a client's disease-severity spectrum, given that the client is correctly referred. For instance, an oncologist presented with a client having cancer has a probability p of diagnosing the correct severity level, no matter what severity the client has. However, this same oncologist, when presented with a patient who has heart disease but was referred for cancer, has a probability qbp that the client will be misdiagnosed — for cancer. If not misdiagnosed in this way, the provider sends the client back to the advisor, with an appointment scheduled by the Simulation Manager. A PCP has a decreasing probability $r _ { i }$ of diagnosing disease-severity for severity level i, where $r _ { i }$ is assumed constant across all diseases.

Diagnosis takes time, with time increasing by severity level in general, due to tests that must be done, etc. At the end of diagnosis, a specialist treats the client, no matter what the severity level. A PCP refers clients with advanced severity back to the advisor for a specialist referral for treatment, but treats clients with symptomatic or chronic severities. The correct treatment followed by the client results in a change to the probabilities in the progression matrix, such that progression is slowed or reversed. The client may not adhere to recommended treatments, in which case the natural progression model is used for disease progression. This is determined via Monte Carlo sampling based on probabilities associated with the client's tendency to follow instructions.

## 3.4. Health information sources

Access to accurate, integrated, and comprehensive health information sources is critical to effective healthcare delivery [29]. Our game provides two health information sources during game play: electronic health records (EHR) and an online knowledge repository called Med<sup>fi</sup>le.

## 3.4.1. Electronic health records

One of the central information sources of the game is the EHR. An EHR is a longitudinal electronic record of patient health information generated by one or more encounters in any care delivery setting, including patient demographics, progress notes, problems, medications, vital signs, past medical history, immunizations, laboratory data and radiology reports [15]. EHRs are major, complex software systems that capture massive amounts of clinical information. An inclusion of all possible <sup>fi</sup>elds is therefore beyond the scope of the game. Since there is no standard for EHRs, our design is tailored to support basic functionality for the game. The EHR captures mainly information from appointments with the health advisor and the results and outcomes of the tests and treatments conducted by providers. One of the unique aspects of our EHR is that it is automatically populated with relevant dialog information. In other words, once the player and client discuss something, it is captured automatically in the EHR. Table 4 shows the various categories of information captured in our basic EHR.

## 3.4.2. Medfile

At any point in the game, the advisor has also access to an online medical knowledge base called Med<sup>fi</sup>le. Med<sup>fi</sup>le contains descriptive information on symptoms, diseases, diagnostic tests, treatments, and provider specialties. For each symptom, Med<sup>fi</sup>le provides a description as well as the corresponding set of diseases and disease severity levels in which they are observed. For each disease, it lists a description including the most common symptoms, a list of con-<sup>fi</sup>rming tests, and a list of possible treatments. Information in Med<sup>fi</sup>le is organized by search category; within a category information is sorted alphabetically. We utilized a combination of reputable online medical resources to build Med<sup>fi</sup>le (e.g. WebMD).

Table 4 Electronic health record (EHR).

<table><tr><td>Category</td><td>Description</td></tr><tr><td>Client information</td><td>Provided in the initial appointment with the advisor. Contains name, gender, age, and a photo</td></tr><tr><td>Health history</td><td>Provided in the initial appointment with the advisor. Contains general health state history, date of last physical and parents&#x27; health state (including cause of death if deceased)</td></tr><tr><td>Lifestyle</td><td>Updated at each appointment with the advisor. Contains information on alcohol and caffeine usage, diet and exercise, smoking activity, stress level and sexual activity</td></tr><tr><td>Symptom</td><td>Updated at each appointment with the advisor. Contains each symptom reported by the client, including frequency and onset date.</td></tr><tr><td>Assessment</td><td>Updated at each appointment with the advisor. Contains the advisor&#x27;s assessment of the client in terms of disease and stage.</td></tr><tr><td>Referral</td><td>Updated at each appointment with the advisor. Contains the referral made by the advisor (provider plus service requested, e.g., consult, test, treatment).</td></tr><tr><td>Advisor note</td><td>Updated at each appointment with a provider. Contains free-form text with any notes that the advisor wishes to make during an appointment.</td></tr><tr><td>Diagnosis</td><td>Updated at each appointment with a provider. Contains the provider&#x27;s diagnosis of the client in terms of disease and stage.</td></tr><tr><td>Service outcome</td><td>Updated at each appointment with a provider. Contains the outcome of each service performed by the provider, e.g., test or treatment outcome.</td></tr></table>

## 3.5. Architecture and implementation

Health Advisor is implemented as a web-based Java™ (J2EE) application under a JBoss application server framework. JBoss utilizes the Tomcat servlet container and the Apache web server technologies. Further information on these technologies is provided by Marrs and Davis [22]. Within this framework, the Health Advisor application utilizes servlets to serve pages with dynamic content in response to user actions, and a relational MySQL™ database for persistent data storage. The interface pages use Java Server Pages (JSP) to display dynamic content. Game interface elements were designed and implemented with Adobe Creative Suite. Fig. 4(a–h) shows several screenshots of the web‐based game interface.

The servlets provide logic to support user interaction, as well as the simulated activities that occur outside of the direct user interaction (e.g., evolution of a client's disease state). This logic requires access to data to support player decision-making and simulation execution. To perform this function. the serylets invoke data access objects, which in turn query the persistent database using the JDBC protocol and then populate data transfer objects that can be used by the player to display and manipulate data. The data transfer objects map to the database tables using an object-relational mapping (ORM). This architecture is intended to provide the <sup>fl</sup>exibility and scalability to enable evolution of Health Advisor to include multiple types of players, including providers of information services, insurance, and marketing services.

![](/api/attachments/PKP8D54H/fulltext/images/ce4a8ee48d395d5e2b31cae3257a3b8ff4148bc6c1d616451772144074c1082a.jpg)  
(a) Front Office

![](/api/attachments/PKP8D54H/fulltext/images/150a7ac95c96c9b3ec3eda68f2bce2d872e26c8b3aad4c29f9119130d818d579.jpg)  
(b) Health Advisor Office

![](/api/attachments/PKP8D54H/fulltext/images/10e6d8486a97c08e7f1fc56075350e7a67371e3dababdb480c22f0715c69cc28.jpg)  
(e) Client Information

![](/api/attachments/PKP8D54H/fulltext/images/122d41ff25899fa04fd993308a2bd09b4d89c25a69ba99db8e40a922d8e8eb85.jpg)  
(f) Provider Information

(c) Dialog Mode  
![](/api/attachments/PKP8D54H/fulltext/images/c61fd9e9650474215e48ce972f158501b9775a4a528b6c7b927ffdbfe3c5d9a9.jpg)

![](/api/attachments/PKP8D54H/fulltext/images/dfff36d4dca4a6f7364f3cd978d66fb91d09fff89dea1b0a470e453ef584c077.jpg)

![](/api/attachments/PKP8D54H/fulltext/images/ac94fc940c51d54ac3983baef4f3bcd2106d6b91ae2229b62734bd8e08f0a876.jpg)  
(d) Electronic Health Record (EHR)

(g) Review Provider  
Fig. 4. Health Advisor screenshots.  
![](/api/attachments/PKP8D54H/fulltext/images/d640c55a7dcce798a762427123ce9e2074bcd888855d05e715c3369f9914808a.jpg)  
(h) Make Assessment

## 4. Methodology

The long-term goal of this research is to use the serious games approach to study systemic changes in the healthcare delivery system, such as introduction of new business models. In a complex system such as healthcare, the usability and usefulness of information sources can have an impact on decision-making effectiveness. This paper focuses on the more limited goals of studying how this usability and usefulness impacts decision-making effectiveness, as well as validating the concept and design behind the Health Advisor game. We used a combination of qualitative and quantitative research methods to study the relevance, use and effectiveness of our Health Advisor game. Research has shown that a combination of empirical methods is particularly valuable when studying new and perhaps poorly understood phenomenon [10,27]. Study participants included physicians, healthcare academics and researchers, human behavior specialists, medical school students/researchers, practicing healthcare professionals, and undergraduate students, and game playing teenagers. Each of these respondent groups provided important game validation perspectives. Our approach included four distinct phases: senior healthcare practitioners (Phase 1); healthcare practitioners in training (Phase 2); college students with interest, but no expertise in health (Phase 3); and teenagers with substantial game playing experience (Phase 4). The purpose of including such a diverse group of participants is that one needs all four perspectives to fully evaluate this type of serious game. In other words, the game needs to make sense to domain experts, be usable and useful to trainee domain experts, be accessible to highly motivated but not yet knowledgeable players, and re<sup>fl</sup>ect best practices in game design (somewhat independent of domain).

## 4.1. Phase 1: expert study (senior healthcare practitioners)

The <sup>fi</sup>rst phase of our research involved a live demonstration and subsequent in-depth discussion of our game with a group of 17 physicians and healthcare professionals attending a national healthcare conference. We chose this group and venue as it provided access to experienced practitioners in medical care and disease and case management. The purpose was to receive feedback about the overall game objective and playability and validate our game design and assumptions.

## 4.2. Phase 2: focus group (healthcare practitioners in training)

For the second phase, we conducted a small roundtable discussion with eight medical school students and researchers. We provided a step-by-step demonstration of Health Advisor and asked each participant to comment on game design, playability, and accuracy as well as ways to improve it.

## 4.3. Phase 3: game play and survey (undergraduate students)

In the third phase of the research, we provided undergraduate students in a predictive health course at a major research university access to the Health Advisor game. These students have an interest, but no expertise in health. The instructions were to play the game and then complete a post-game assessment survey. No incentives were given. However, students were required to participate in either this study or complete an alternative, more traditional homework assignment.

We modi<sup>fi</sup>ed the game slightly for the purpose of this phase of the research; each player saw only 24 clients (e.g. 3 days of simulated time), each for their initial appointments. All players experienced the same client order. Clients with a wide range of different diseases, severity levels, and demographic characteristics (e.g. age, race, and gender) were selected to provide players with a broad array of clients and client interactions. There were two reasons for this adjustment: <sup>fi</sup>rst, limiting interactions to 24 clients ensured that players could complete the entire game within a short timeframe — an hour or so. Second, a standardized order of clients allowed us to easily compare the types of decisions and strategies players used.

Once players had completed all client appointments they were given a summary screen with their performance score and a link to the post-game assessment survey. The survey asked players to comment on game usability and ease of use, realism of game play, and improvement opportunities. All questions were measured on a 5-point Likert scale (1 = Strongly Disagree to 5 = Strongly Agree). Access to the game and survey was provided for two weeks; a reminder email was sent after one week. 44 (out of 48) students played the game and completed the survey, resulting in a response rate of 91.7%. In addition to the survey, we also captured keystrokes, mouse clicks and performance data (e.g. MedFile, EHR access, diagnosis, referral choices) to gain an understanding how players interacted with the game.

## 4.4. Phase 4: comparative study of serious games (teenagers)

We are cognizant that Health Advisor is a simpli<sup>fi</sup>ed and merely a <sup>fi</sup>rst step towards a more comprehensive serious game of healthcare management. Many game-speci<sup>fi</sup>c improvements could be made. The fourth and last phase thus included a comprehensive comparative study of current commercial serious games with teenagers with substantial game-playing experience [1]. The purpose of this phase was to understand – beyond the speci<sup>fi</sup>c content and context of healthcare – what game elements are desirable in serious games and in what ways we could improve Health Advisor in future versions. The review involved a comparison of Health Advisor with seven other popular serious games, ranging from Simunomics, to Cruise Ship Tycoon, to Sims 3. Games were compared in terms of objectives of the game, interactions in the game, decisions made by players, and information provided during game play. Games were also characterized in terms of Rouse and Boff's [41] organizational simulation architecture, i.e., world model, nature of characters, and organizational story, in some cases in terms of the “back story.”

## 5. Results

## 5.1. Game concept, usability, and playability

The overall response for game concept, usability, and playability was positive across all phases. Comments from the <sup>fi</sup>rst two phases included that the game was a “novel and intriguing new prototype for understanding healthcare” and that the game interface was “very useable and self-explanatory in terms of navigation.” The notion of using simulation to gain understanding of alternative ways to transform healthcare delivery strategies was particularly well received. Respondents emphasized that the “the ability to test out strategies before they are actually implemented” presented the most compelling aspect of organizational simulation. It was also evident, from our post-game assessment that the role and objectives of the health advisor were generally well understood (see Table 5).

There were, however, some concerns and suggestions, as well. Physicians, for example, did not seem to relate well to the role of the health advisor; in fact, they preferred to treat patients rather than manage clients. Medical students, on the other hand, noted a number of detailed issues, many of which involve future work.

Descriptive statistics of game usability and playability assessment (n=44).

<table><tr><td>Category</td><td>Item</td><td>Mean</td><td>S.D.</td></tr><tr><td rowspan="3">Game concept</td><td>I understand the role of a health advisor.</td><td>4.51****</td><td>0.71</td></tr><tr><td>The options available to the health advisor are reasonable.</td><td>4.26****</td><td>0.74</td></tr><tr><td>The sequence of play makes sense to what a health advisor would do.</td><td>4.15****</td><td>0.93</td></tr><tr><td rowspan="5">Game play</td><td>It was easy to learn how to play Health Advisor.</td><td>3.92***</td><td>1.04</td></tr><tr><td>It was easy to use Health Advisor once you learned how to play.</td><td>4.10****</td><td>1.06</td></tr><tr><td>It was interesting to play Health Advisor.</td><td>4.58****</td><td>1.01</td></tr><tr><td>It was fun to play Health Advisor.</td><td>3.96***</td><td>1.06</td></tr><tr><td>It was educational to play Health Advisor.</td><td>4.53***</td><td>0.69</td></tr><tr><td rowspan="8">Game content</td><td>The dialogs with clients make sense.</td><td>4.33****</td><td>0.76</td></tr><tr><td>The tests and treatments available are appropriate.</td><td>4.35****</td><td>0.75</td></tr><tr><td>The information on providers is understandable.</td><td>4.34**</td><td>1.02</td></tr><tr><td>The information on providers is helpful.</td><td>4.36**</td><td>0.87</td></tr><tr><td>The information in Medfile is understandable.</td><td>4.51****</td><td>1.06</td></tr><tr><td>The information in Medfile is helpful.</td><td>4.71****</td><td>0.78</td></tr><tr><td>The performance feedback provided is understandable.</td><td>3.67**</td><td>1.01</td></tr><tr><td>The performance feedback provided is helpful.</td><td>3.83**</td><td>1.09</td></tr></table>

• An issue underlying the game is patient selection. An advisor that is purely pro<sup>fi</sup>t driven would prefer to have healthy patients rather than unhealthy ones. This is a real world issue that employers face with their insurance programs.

• The appointment format is modeled on a PCP appointment. Consequently, certain aspects may not be appropriate for a health advisor appointment.

• Feedback from PCPs is that they would like access to specialists' calendars or availability in making their referrals. This aspect of the game is therefore very appealing.

• The current provider metrics are notional. Work needs to be done, in the general <sup>fi</sup>eld of healthcare, to establish good metrics. This involves controversy.

• The game assumes that clients tell the truth. In reality, this is often not the case.

• It would be interesting to correlate player background with performance. For instance, do MBA players perform better than non-MBA players in <sup>fi</sup>nancial metrics?

• There are alternate EHR formats that should be investigated [7,18,21,51].

• The tension between costs incurred and health outcomes in the advisor performance brings up the issue of ethics. It would be interesting to use the game as a platform to develop ethics guidelines.

• Issues not modeled that would be of interest in the future are (i) prevention, (ii) liability, and (iii) client loss/gain due to advisor performance and competition.

## 5.2. Game play and performance

In Phase 3 of our study, participants had the opportunity to play a modi<sup>fi</sup>ed version of the game. This phase provided several important insights into game play and the resulting player performance. Table 6 provides descriptive statistics of the game play. It can be observed that players referred clients more to specialists than PCPs. Nearly 50% of players accessed Med<sup>fi</sup>le and over 65% viewed the EHR. The performance of players was assessed by the level of assessment and referral accuracy. A fully accurate assessment and referral resulted in 4 points, 2 points for each category. A correct assessment included identi<sup>fi</sup>cation of the disease and severity level. Partial points were given for correct identi<sup>fi</sup>cation of a disease, body part, or related body part. A correct referral was made when a client with the appropriate provider type and specialist category (for specialist referral) and a disease/severity appropriate test or treatment was selected. Partial points were given for selecting a provider type, test, or treatment that was partially appropriate for a disease and severity. The

Game play descriptives (Phase 3).

<table><tr><td>Number of players</td><td>44 (14 males, 30 females)</td></tr><tr><td>Mean game play time/player</td><td>1:08:14 (male: 57:38; female: 1:12:00)</td></tr><tr><td>Mean number of clicks/client</td><td>27.01</td></tr><tr><td>Game play</td><td></td></tr><tr><td>Percentage of players that view Medfile</td><td>48.2%</td></tr><tr><td>Percentage of players that view EHR</td><td>65.2%</td></tr><tr><td>Provider choice</td><td></td></tr><tr><td>- PCP</td><td>45.2%</td></tr><tr><td>- Specialist</td><td>54.8%</td></tr><tr><td>Performance</td><td></td></tr><tr><td>- Assessment accuracy</td><td>44.9%</td></tr><tr><td>- Referral accuracy</td><td>52.7%</td></tr><tr><td>- Total accuracy</td><td>48.8%</td></tr></table>

\*\*\*\* p≤0.0001.

Table 7  
Summary of game play and performance (Phase 3).

<table><tr><td rowspan="2">Client order</td><td rowspan="2">Disease</td><td rowspan="2">Severity level</td><td rowspan="2">Complexity (bits)</td><td rowspan="2">Mean clicks</td><td rowspan="2">Medfile view (%)</td><td rowspan="2">EHR view (%)</td><td colspan="3">Mean points</td></tr><tr><td>Assessment</td><td>Referral</td><td>Total</td></tr><tr><td>1</td><td>Arrhythmias</td><td>Chronic</td><td>2.560</td><td>45.12</td><td>26</td><td>45</td><td>0.73</td><td>1.05</td><td>1.77</td></tr><tr><td>2</td><td>Colon cancer</td><td>Acute</td><td>1.695</td><td>37.52</td><td>29</td><td>40</td><td>0.85</td><td>0.79</td><td>1.63</td></tr><tr><td>3</td><td>Prostate cancer</td><td>Symptomatic</td><td>0.528</td><td>32.98</td><td>55</td><td>43</td><td>0.77</td><td>1.12</td><td>1.89</td></tr><tr><td>4</td><td>Emphysema</td><td>Chronic</td><td>2.253</td><td>31.88</td><td>29</td><td>40</td><td>1.01</td><td>1.24</td><td>2.25</td></tr><tr><td>5</td><td>Asthma</td><td>Acute</td><td>3.525</td><td>34.29</td><td>26</td><td>55</td><td>0.75</td><td>1.14</td><td>1.89</td></tr><tr><td>6</td><td>Lung cancer</td><td>Chronic</td><td>1.028</td><td>32.60</td><td>38</td><td>43</td><td>1.00</td><td>0.98</td><td>1.98</td></tr><tr><td>7</td><td>Lung cancer</td><td>Acute</td><td>1.028</td><td>28.86</td><td>40</td><td>40</td><td>0.92</td><td>1.24</td><td>2.15</td></tr><tr><td>8</td><td>Alzheimer&#x27;s</td><td>Acute</td><td>4.645</td><td>30.21</td><td>52</td><td>50</td><td>0.08</td><td>0.62</td><td>0.70</td></tr><tr><td>9</td><td>Influenza</td><td>Symptomatic</td><td>3.497</td><td>28.81</td><td>45</td><td>40</td><td>1.10</td><td>1.52</td><td>2.62</td></tr><tr><td>10</td><td>Colon cancer</td><td>Acute</td><td>1.695</td><td>26.69</td><td>33</td><td>50</td><td>1.15</td><td>0.64</td><td>1.80</td></tr><tr><td>11</td><td>Nephritis</td><td>Acute</td><td>2.208</td><td>27.33</td><td>33</td><td>24</td><td>1.11</td><td>1.24</td><td>2.35</td></tr><tr><td>12</td><td>Diabetes type II</td><td>Chronic</td><td>3.521</td><td>23.48</td><td>43</td><td>38</td><td>0.76</td><td>1.40</td><td>2.17</td></tr><tr><td>13</td><td>Stroke</td><td>Chronic</td><td>5.364</td><td>24.26</td><td>43</td><td>40</td><td>0.30</td><td>0.71</td><td>1.01</td></tr><tr><td>14</td><td>Alzheimer&#x27;s</td><td>Symptomatic</td><td>4.645</td><td>20.29</td><td>45</td><td>50</td><td>1.55</td><td>1.07</td><td>2.62</td></tr><tr><td>15</td><td>Coronary artery disease</td><td>Acute</td><td>2.028</td><td>27.93</td><td>29</td><td>33</td><td>1.05</td><td>1.38</td><td>2.43</td></tr><tr><td>16</td><td>Nephritis</td><td>Chronic</td><td>2.208</td><td>25.48</td><td>48</td><td>38</td><td>0.95</td><td>0.88</td><td>1.83</td></tr><tr><td>17</td><td>Pneumonia</td><td>Chronic</td><td>3.138</td><td>24.48</td><td>48</td><td>36</td><td>0.99</td><td>1.31</td><td>2.30</td></tr><tr><td>18</td><td>Diabetes type II</td><td>Symptomatic</td><td>3.521</td><td>21.52</td><td>45</td><td>21</td><td>0.32</td><td>1.55</td><td>1.87</td></tr><tr><td>19</td><td>Lung cancer</td><td>Chronic</td><td>1.028</td><td>24.88</td><td>45</td><td>36</td><td>1.21</td><td>1.00</td><td>2.21</td></tr><tr><td>20</td><td>Coronary artery disease</td><td>Acute</td><td>2.028</td><td>24.88</td><td>43</td><td>33</td><td>1.29</td><td>0.21</td><td>1.50</td></tr><tr><td>21</td><td>Coronary artery disease</td><td>Symptomatic</td><td>2.028</td><td>16.10</td><td>43</td><td>33</td><td>1.32</td><td>0.19</td><td>1.51</td></tr><tr><td>22</td><td>Asthma</td><td>Chronic</td><td>3.525</td><td>21.90</td><td>26</td><td>45</td><td>1.21</td><td>1.14</td><td>2.36</td></tr><tr><td>23</td><td>Breast cancer</td><td>Symptomatic</td><td>1.423</td><td>18.48</td><td>29</td><td>40</td><td>1.06</td><td>1.24</td><td>2.30</td></tr><tr><td>24</td><td>Breast cancer</td><td>Symptomatic</td><td>1.423</td><td>18.31</td><td>55</td><td>43</td><td>1.12</td><td>1.67</td><td>2.79</td></tr></table>

results show that players' assessment accuracy was less than 50% and their referral accuracy slightly greater than 50%. In other words, almost half the time, players reached the wrong initial conclusion, and over half the time they sent clients to the wrong provider. This is, obviously, an in<sup>fl</sup>ated error rate compared to real practice, but these results enabled us to understand why errors were made. Table 7 provides a more in-depth explanation to the <sup>fl</sup>ow of the game. It shows the order of clients, their diseases, and disease severity levels. Several interesting observations can be made.

## 5.2.1. Total performance increased during game play

We notice a slight improvement (2%) in total player performance over the course of the game suggesting that some form of learning has occurred. We measured this by examining the growth in total performance score (assessment + referral) from the <sup>fi</sup>rst to the last client a player saw. We also observe that the total performance improves on average by 12% the second time a player sees a previously assessed disease/severity pair. This also supports the learning hypothesis.

## 5.2.2. Medfile access significantly increased performance

A key observation of the game play is that Med<sup>fi</sup>le access signi<sup>fi</sup>- cantly increases total as well as both assessment and referral performance (0.86, p 0.01). This result suggests that information in Med<sup>fi</sup>le helped players understand the symptoms, conditions, and referral options. Interestingly, Med<sup>fi</sup>le was accessed most frequently for chronic cases. A possible explanation for this is that chronic diseases have a higher number of symptoms as well as overlapping symptoms with other diseases and therefore a greater understanding of the underlying disease roots is required. Over the course of play, Med<sup>fi</sup>le access increased signi<sup>fi</sup>cantly suggesting that players realized the value of having access to medical knowledge: 26% of players accessed Med<sup>fi</sup>le for the <sup>fi</sup>rst client, while 55% of players accessed Med<sup>fi</sup>le for the last client.

5.2.3. Players who rated Medfile highly useful were much more likely to access it

The correlation between highly rating Med<sup>fi</sup>le and using it was 0.93 (p≤0.05). Succinctly, using Med<sup>fi</sup>le improves performance, but it is only used when it is highly rated. This agrees with the literature [3,45] as well as our workshop experiences with clinicians where they report that usability and usefulness issues determine whether they bother to access information systems. Our results show that this is also true for undergraduates in predictive health. Perceived usability and usefulness of health IT is a pervasive and important issue.

## 5.2.4. EHR access did not improve performance

Interestingly, EHR access decreased over the course of play from 67% to 33%. In fact, use of the EHR signi<sup>fi</sup>cantly decreased total performance (0.89, p≤0.05). This observation is contradictory to the common understanding of the value of EHR. However, we do not think this is surprising. The EHR was not populated with any additional information beyond that players had already gathered through the dialog with clients. The EHR thus only reinforced what players already knew. This situation most likely led to a greater level of uncertainty in their decision making and less relevance of the EHR. However, we did notice that EHR access was higher for acute (45.7%) and chronic cases (45.4%) than symptomatic cases (34.1%).

What is most interesting is that players decreased their use of the EHR over time, apparently recognizing that it was not helping them. This reinforces the notion that people's perceptions of the usability and usefulness of information resources has a strong effect on their use of these sources [11]. This result, when considered in combination with the results for use of Med<sup>fi</sup>le, suggests a hypothesis for why less than 50% of medical decisions nationwide are evidence based [25]. People tend not to use information that is dif<sup>fi</sup>cult to identify and access, as well as dif<sup>fi</sup>cult to interpret. We hypothesize that these perceptions of health IT undermine adoption of evidence-based medicine.

It is important to emphasize the bene<sup>fi</sup>ts of having used undergraduates highly motivated by health but lacking in medical and clinical knowledge for exploring the use of information sources. If we had employed health professionals, the impacts of Med<sup>fi</sup>le and the EHR would have been confounded with players a priori knowledge. Instead, we knew that all of players' knowledge had to come from Med<sup>fi</sup>le and the EHR. We were, therefore, able to replicate phenomena reported for (and by) healthcare professionals, but dif<sup>fi</sup>cult to demonstrate empirically. Organizational simulation with motivated but naïve subjects enabled exploring these issues.

## 5.2.5. Game duration and number of clicks improved performance

Not surprisingly, those that played the game longer and used more clicks performed signi<sup>fi</sup>cantly better than those with short game durations and lower number of clicks (signi<sup>fi</sup>cant at p≤0.1 and p≤0.05). There were no signi<sup>fi</sup>cant differences in game duration across acute, chronic, and symptomatic cases. However, there were signi<sup>fi</sup>cantly fewer clicks for symptomatic cases (23.26) than chronic (28.23) and acute (29.71) suggesting that players were able to make decisions fastest for symptomatic and slowest for acute. Interestingly, the number of clicks substantially decreased from the <sup>fi</sup>rst to the last client appointment (45.12 to 18.31 clicks). There could be three reasons for this. First, learning must have increased signi<sup>fi</sup>cantly over the course of play; thus players required fewer clicks to navigate the game. Second, players may also have gained an understanding of how to make assessments and referrals over the course of play. Third, players came to understand their information resources and how best to use them.

## 5.2.6. Disease severity levels influenced performance

Overall, total performance was the highest for symptomatic cases (51.9% accuracy), moderate for chronic cases (49.6%), and the lowest for acute (45.1%). Upon further examination, assessment performance stayed relatively constant for chronic, acute, and symptomatic diseases (43.4–45.0%). Referral performance varied, however, signi<sup>fi</sup>cantly (45.3–53.9%). It was the highest for symptomatic and lowest for acute cases. This may suggest that players were able to correctly refer symptomatic diseases and had a more dif<sup>fi</sup>cult time referring acute cases.

## 5.2.7. Disease/severity complexity decreased total performance

Our results indicate that as the complexity<sup>4</sup> of the disease/severity increases, total performance decreased exponentially. This is not a surprising observation. Complexity is a measure operationalized as the number of binary “symptom existence” questions one must ask to comprehensively determine the health state of a client [43]. The higher the complexity, the more questions must be asked. Thus, performance would be expected to decrease the greater the complexity is unless additional information is sought. Indeed, our results show that performance increases with higher information sought for higher levels of complexity. This suggests that information sources can play very important role in mitigating disease/severity complexity.

## 5.3. Comparative study of serious games

Five recommendations for enhancing Health Advisor resulted from our comparative study of serious games. First, the nature of the challenge should be clearly understandable by players. There should be a clear goal with increasing levels of dif<sup>fi</sup>culty as players gain knowledge, skill and success. Second, the game should be entertaining and fun, including interactions that are interesting and consequences of actions that are logical, not totally predictable and relatively soon following decisions. Third, the scenarios should not be too repetitive and should include some variety in choices and consequences. Fourth, knowledge should be gained in the game, with some mechanism for players to specify their initial level of knowledge. Finally, the game interface should be easy to use in the sense of being intuitively obvious; while graphics and colors are important, they are secondary. Each of these recommendations presents an important and interesting future research opportunity for Health Advisor.

## 6. Conclusions, limitations, and future work

This paper has presented the applicability and use of organizational simulation, an emerging modeling paradigm from systems engineering, to study complex healthcare issues. We designed and developed a serious game called Health Advisor to examine the effectiveness of different healthcare management strategies aimed at addressing the trade-offs between good health outcomes and healthcare costs. Through multiple empirical studies we validated the game concept, evaluated its usability, and assessed initial player performance. Our study provided several interesting insights:

• The role of a health advisor is new and quite different than that of a physician. Physicians prefer to treat patients and perhaps are less interested in the business aspects involving cost/outcome trade-offs. This points to an unaddressed need in the healthcare system, especially as a major area of national concern relates to escalating system costs.

• Access to information on symptoms, diseases and severity levels helps inform diagnostic and referral skills among users. This is not an unexpected result, but it does point to the importance of having up-to-date information sources available for personnel involved in healthcare.

• People's perceptions of the usability and usefulness of information sources affects their access and use of these sources and their subsequent performance. Our use of a subject population that was motivated by health issues, but not fully informed on diseases, symptoms, etc. enabled showing that people, in general, make tradeoffs between perceived usability and usefulness, and subsequent access and use of information.

• Our results did not indicate that electronic health records improved performance. Most likely, this is a result of the limitations associated with the current version of the game, which does not include detailed client history records.

• Users improved their performance as they continued to play and as they navigated the game, measured via user clicks. Again, this is not unexpected.

• Increased disease/severity complexity decreased user performance. While not unexpected, this reinforces the need for effective decision support in terms of diagnosis and referral. Helping the user navigate complexity is an important avenue of future research.

Our approach does have some limitations. To date, we have assessed player performance only in terms of correct diagnosis and referral to the best type of provider. Future work involves integrating the cost trade-offs into this decision set. Client characters are also limited in their realism. We intend to address this via arti<sup>fi</sup>cial intelligence technologies currently used in interactive gaming and drama, which provide tools for realistic character representations [23]. From a scienti<sup>fi</sup>c perspective, the disease progression model for clients is rather simplistic and limited. Our current research is addressing this limitation by studying and integrating disease progression models from a variety of sources. In particular, we are building on models developed using national data sets such as that from the

Framingham Study [52,53]. We have been able to decompose such models to inform estimation of transition probabilities for the disease progression models. Another limitation of the game, as currently framed, is that it does not speci<sup>fi</sup>cally address the needs of multiple potential audiences. Medical professionals are interested in treating patients and may desire direct interaction with them to assess their health states, make diagnoses, etc. Healthcare managers and policy makers, on the other hand, may be less interested in direct contact and may want summary data presented to help inform their decision-making on costs and outcomes as well as policy reform. Finally, the game does not include many important components of a realistic healthcare system, such as competition between health advisors, liability, prevention, government regulation and the impact of recently adopted legislation, health insurance, and ethics.

Each of these limitations presents enormous future research opportunities involving study of systemic changes in health care. In particular, the results from our study of information usage point to the importance of systemic changes involving effective information usage. We believe that there are important opportunities for improving the healthcare system using an organizational simulation/serious gaming approach to capitalize on crowd-source solutions and anomaly innovations. Our work provides a fundamental step towards this vision.

## Acknowledgments

This research was supported, in part, by a series of faculty grants from IBM Research. We would like to thank the Robert Wood Johnson Foundation, the reviewers of the Serious Games in Health initiative, and Dr. Mark Braunstein for their feedback and validation of the Health Advisor game, Kristi Kirkland for help with data collection, Rebecca Rouse for developing the patient personalities, and two graduate students for their assistance in data analysis.

## References

[1] W.H. Rouse, Serious games: evaluation and comparison, Tennenbaum Institute, Atlanta, GA, 2011.

[2] Unknown, National Academies: engineering the health care system, The National Academies Press, Washington, DC, 2006.

[3] M.J. Ball, S. Bierstock, Clinician use of enabling technology: creating a new healthcare system through the use of enabling technologies requires changes on a profound scale, Journal of Healthcare Information Management 21 (3) (2007) 68–71.

[4] R.C. Basole, W.B. Rouse, Complexity of service value networks: conceptualization and empirical investigation, IBM Systems Journal 47 (1) (2008) 53–70.

[5] S. Biswas, Y. Narahari, Object oriented modeling and decision support for supply chains, European Journal of Operational Research 153 (2004) 704–726.

[6] D.A. Bodner, W.B. Rouse, Understanding R&D value creation with organizational simulation, Systems Engineering 10 (1) (2007) 64–82.

[7] C. Bossen, Evaluation of a computerized problem-oriented medical record in a hospital department: does it support daily clinical practice? International Journal of Medical Informatics 76 (2007) 592–600.

[8] K.M. Carley, T.L. Frantz, Modeling organizational and individual decision making, in: A.P. Sage, W.B. Rouse (Eds.), Handbook of Systems Engineering and Manage ment, John Wiley & Sons, Hoboken, NI. 2009, pp. 723–762.

[9] CMS, National Health Expenditure Data, Centers for Medicare & Medicaid Services. (Accessed) http://www.cms.hhs.gov/NationalHealthExpendDataJuly 29 2010.

[10] J.W. Creswell, Research Design: Qualitative, Quantitative, and Mixed Methods Approaches. (Sage Publications) Third ed., 2009.

[11] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3) (1989) 319–340.

[12] B.T. Denton, M. Kurt, N.D. Shah, S.C. Bryant, S.A. Smith, Optimizing the start time of statin therapy for patients with diabetes, Medical Decision Making 30 (2010) 474-483.

[13] B.T. Denton, A.J. Miller, H.J. Balasubramanian, T.R. Huschka, Optimal allocation of surgery blocks to operating rooms under uncertainty, Operations Research 58 (4) (2010) 802–816.

[14] E. Hillebrand, J. Stender, Many-Agent Simulation and Arti<sup>fi</sup>cial Life, IOS Press, Am sterdam. 1994

[15] HIMSS, Electronic Health Record. (Accessed) http://www.himss.org/ASP/ topics\_ehr.aspSeptember 1 2010.

[16] J. Howe, Crowdsourcing: Why the Power of the Crowd is Driving the Future of Business, Crown Publishing Group, New York, 2009.

[17] IOM, Crossing the Quality Chasm: A New Health System for the Twenty-First Century, The National Academies Press, Washington, D.C., 2001.

[18] S.B. Johnson, S. Bakken, D. Dine, S. Hyun, E. Mendonça, F. Morrison, T. Bright, T. Van Vleck, J. Wrenn, P. Stetson, An electronic health record based on structured narrative, Journal of the American Medical Informatics Association 15 (2008) 54–64.

[19] G. Karsai, A. Ledeczi, S. Neema, J. Sztipanovits, The model-integrated computing toolsuite: metaprogrammable tools for embedded control system design, in: IEEE Joint Conference CCA, ISIC and CACSD, IEEE Press, Munich, Germany, 2006, pp. 50–55.

[20] A.M. Law, W.D. Kelton, Simulation Modeling and Analysis, 2nd ed. McGraw-Hill, Boston, MA, 2000.

[21] I. Maistrello, P. di Pietro, S. Renna, M. Boscarini, A. Nobili, A surveillance-oriented medical record as a source of data for both drug and quality of care surveillance, Pharmacoepidemiology and Drug Safety 8 (1999) 131–139.

[22] T. Marss, S. Davis, JBoss at Work: A Practical Guide, O'Reilly, Sebastopol, CA, 2006.

[23] M. Mateas, A. Stern, A behavior language: joint action and behavioral idioms, in: H. Prendinger, M. Ishizuka (Eds.), Life-Like Characters: Tools, Affective Functions and ApplicationsSpringer, Berlin, 2004.

[24] J.L. Mathe, A. Ledeczi, A. Nadas, J. Sztipanovits, J.B. Martin, L.M. Weavind, A. Miller, P. Miller, D.J. Maron, A model-integrated, guideline-driven, clinical decisionsupport system. (Jul/Aug) IEEE Software (2009) 54–61.

[25] E.A. McGlynn, S.M. Asch, J. Adams, J. Keesey, J. Hicks, A. DeCristofaro, E.A. Kerr, The quality of healthcare delivered to adults in the United States, The New England Journal of Medicine 348 (26) (2003) 2635–2645.

[26] M. Minear, D.C. Park, A lifespan database of adult facial stimuli, Behavior Research Methods, Instruments, & Computers 36 (4) (2004) 630–633.

[27] D. Morgan, Focus Groups as Qualitative Research, Sage Publications, Thousand Oaks, CA, 1997.

[28] M.E. Nissen, Computational experimentation on new organizational forms: exploring behavior and performance of edge organizations, Computational and Mathematical Organization Theory 13 (3) (2007) 203–240.

[29] L. Olsen, D. Aisner, M.J. McGinnis, The Learning Healthcare System, National Academies Press, Washington, D.C., 2007.

[30] M.E. Porter, E.O. Teisberg, Rede<sup>fi</sup>ning Health Care: Creating Value-Based Competition on Results, Harvard Business School Press, Boston, MA, 2006

[31] M. Prietula, K. Carley, L. Gasser, Simulating Organizations: Computational Models of Institutions and Groups, AAAI Press, 1998.

[32] K.J. Rask, K.L. Brigham, M.M.E. Johns, Integrating comparative effectiveness research programs into predictive health: a unique role for academic health centers, Academic Medicine 86 (6) (2011) 1–6.

[33] D.L. Roberts, C.L. Isbell, A survey and qualitative analysis of recent advances in drama management, International Transactions on Systems Science and Applications 4 (2) (2008) 61–75.

[34] W. Rosen, The Most Powerful Idea in the World: A Story of Steam, Industry, and Invention Random House New York 2010

[35] W.B. Rouse, Managing complexity: disease control as a complex adaptive system, Information Knowledge and Systems Management 2 (2) (2000) 143–165.

[36] W.B. Rouse, Healthcare as a complex adaptive system, The Bridge 38 (1) (2008) 17–25.

[37] W.B. Rouse, Engineering perspectives on healthcare delivery: can we afford technological innovation in healthcare? Systems Research and Behavioral Science 26 (2009) 573–582.

[38] W.B. Rouse, Impacts of healthcare price controls: potential unintended consequences of <sup>fi</sup>rms' responses to price policies, IEEE Systems Journal 4 (1) (2010) 34–38.

[39] W.B. Rouse, R.C. Basole, Understanding complex product and service delivery systems, in: P.P. Maglio, C.A. Kieliszewski, J.C. Spohrer (Eds.), Handbook of Service ScienceSpringer, 2010, pp. 461–480.

[40] W.B. Rouse, D.A. Bodner, Organizational simulation, in: A.P. Sage, W.B. Rouse (Eds.), Handbook of Systems Engineering and ManagementJohn Wiley & Sons, New York, 2009.

[41] W.B. Rouse, K.R. Boff, Organizational Simulation, Wiley, New York, 2005

[42] W.B. Rouse, D.A. Cortese, Engineering the System of Healthcare Delivery, IOS Press, Amsterdam, 2010.

[43] C. Shannon, A mathematical theory of communication, Bell Systems Technical Journal 27 (1948) 379-423.

[44] J.S. Smith, Survey on the use of simulation for manufacturing system design and operation, Journal of Manufacturing Systems 22 (2) (2003) 157–171.

[45] W.W. Stead, H.S. Lin, Computational technology for effective health care: immediate stens and strategic directions Committee on Engaging the Computer Science Research Community in Health Care Informatics, National Research Council, National Academies Press, Washington, D.C., 2009.

[46] J.D. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World, McGraw-Hill, Boston, 2000

[47] W. Sumner, J.Z. Xu, Modeling fatigue, in: AMIA 2002 Annual Symposium, San Antonio, TX, 2002, pp. 747–751.

[48] W. Sumner, M.D. Magen, R. Rovenelli, The item generation methodology of an empiric simulation project, Advances in Health Sciences Education 4 (1999) 49–66.

[49] W. Sumner, J.Z. Xu, G. Roussel, M.D. Hagen, Modeling relief, in: AMIA 2007 Annual Symposium, IL, Chicago, 2007, pp. 706–710.

[50] J. Surowiecki, The Wisdom of Crowds, Anchor Books, New York, 2005

[51] L.L. Weed, Medical records, medical evaluation, and patient care, in: The Problem-Oriented Record as a Basic Tool, Year Book Medical Publishers, Chicago, 1969.

[52] P.W. Wilson, R.B. D'Agostino, D. Levy, A.M. Belanger, H. Silbershatz, W.B. Kannel, Prediction of coronary heart disease using risk factor categories, Circulation 97 (1998) 1837–1847.

[53] P.W. Wilson, J.B. Meigs, L. Sullivan, C.S. Fox, NathanD.M. , R.B. D'Agostino, Prediction of incident diabetes mellitus in middle-aged adults: the framingham off spring study, Archives of Internal Medicine 167 (2007) 1068–1074.

[54] G.L. Zacharias, J. MacMillan, S.B. Van Hemel, Behavioral modeling and simulation: from individuals to societies, in, The National Academies Press, Washington, DC, 2008.

![](/api/attachments/PKP8D54H/fulltext/images/c61c134139eb47b628ad569b9ef0e534669c175a6af7ec052a7d36720165c770.jpg)

Rahul C. Basole, Ph.D. is an Associate Professor in the School of Interactive Computing, the Associate Director for Enterprise Transformation in the Tennenbaum Institute/ IPaT, and an af<sup>fi</sup>liated faculty member in the GVU Center at the Georgia Institute of Technology. His research fuses system science and visualization to study IT strategy, innovation management, and transformation of complex enterprise systems. His work has been published in leading computer science, engineering, and management journals, including Journal of Enterprise Transformation, Journal of Information Technology, IBM Systems Journal, Decision Support Systems, INFORMS Service Science, Journal of Systems Engineering, and IEEE Computer Graphics & Applications. He received his Ph.D. in industrial and systems engineering from the Georgia Institute of Technology.

![](/api/attachments/PKP8D54H/fulltext/images/478e3a02785ad308e98c9be29d7025cc078b8fc0d64d4eafc062fd7b3a4df089.jpg)

Douglas A. Bodner, Ph.D., is a Senior Research Engineer in the Tennenbaum Institute at the Georgia Institute of Technology. His research focuses on computational analysis and decision support for design, operation and transformation of enterprise systems. His work has spanned a number of industries, including aerospace and defense, automotive elec: tronics, energy, health care, paper, semiconductors and telecommunications. He is a senior member of the Institute of Electrical and Electronics Engineers (IEEE) and the Institute of Industrial Engineers (IIE) and a member of the Institute for Operations Research and Management Science (INFORMS). He is also a registered professional engineer.

![](/api/attachments/PKP8D54H/fulltext/images/248083a5a61983b7c651ba6c75c7b130d8f6e0409a55767378032d0a3febc3ae.jpg)

William B. Rouse, Ph.D. is the Alexander Crombie Humphreys Chair in Economics of Engineering in the School of Systems and Enterprises at Stevens Institute of Technology and Profes sor Emeritus in the School of Industrial and Systems Engineering at the Georgia Institute of Technology. His earlier positions include Executive Director of the university-wide Tennenbaum Institute, Chair of the School of Industrial and Systems Engineering, CEO of two innovative software companies – Enterprise Support Systems and Search Technology – and earlier faculty positions at Georgia Tech, University of Illinois, Delft University of Technology, and Tufts University. He has written hundreds of articles and book chapters, and ha authored many books, including most recently The Economics of Human Systems Integration (Wiley, 2010), Engineering the System of Healthcare Delivery (IOS Press, 2009), Handbook of Systems Engineering and Management (Wiley, 2009), People and Organizations: Explorations of Human-Centered Design (Wiley, 2007), Essential Challenges of Strategic Management (Wiley, 2001) and the award-winning Don’t Jump to Solutions (Jossey-Bass, 1998). He is editor of Enterprise Transformation: Understanding and Enabling Fundamental Change (Wiley, 2006), coeditor of Organizational Simulation: From Modeling & Simulation to Games & Entertainment (Wiley, 2005), coeditor of the best-selling Handbook of Systems Engineering and Management (Wiley, 1999), and editor of the eight-volume series Human/Technology Interaction in Complex Systems (Elsevier). Among many advisory roles, he has served as Chair of the Committee on Human Factors of the National Research Council, a member of the U.S. Air Force Scienti<sup>fi</sup>c Advisory Board, and a member of the DoD Senior Advisory Group on Modeling and Simulation. He is a member of the National Academy of Engineering, as well as a fellow of four professional societies: the Institute of Electrical and Electronics Engineers, the International Council on Systems Engineering, the Institute for Operations Research and Management Science, and the Human Factors and Ergonomics Society. He received his B.S. degree from the University of Rhode Island, and his S.M. and Ph.D. degrees from the Massachusetts Institute of Technology.
