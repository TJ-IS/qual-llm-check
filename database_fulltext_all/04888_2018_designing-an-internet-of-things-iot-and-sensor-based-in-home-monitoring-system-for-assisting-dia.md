---
otero_id: 4888
otero_key: "U2FYEW84"
title: "Designing an Internet-of-Things (IoT) and sensor-based in-home monitoring system for assisting diabetes patients: iterative learning from two case studies"
authors: "Samir Chatterjee; Jongbok Byun; Kaushik Dutta; Rasmus Ulslev Pedersen; Akshay Pottathil; Harry (Qi) Xie"
year: "2018"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2018.1485619"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing an Internet-of-Things (IoT) and sensorbased in-home monitoring system for assisting diabetes patients: iterative learning from two case studies

Samir Chatterjee, Jongbok Byun, Kaushik Dutta, Rasmus Ulslev Pedersen, Akshay Pottathil & Harry (Qi) Xie

To cite this article: Samir Chatterjee, Jongbok Byun, Kaushik Dutta, Rasmus Ulslev Pedersen, Akshay Pottathil & Harry (Qi) Xie (2018): Designing an Internet-of-Things (loT) and sensor-basec in-home monitoring system for assisting diabetes patients: iterative learning from two case studies, European Journal of Information Systems, DOI: 10.1080/0960085X.2018.1485619

To link to this article: https://doi.org/10.1080/0960085X.2018.1485619

![](/api/attachments/U2FYEW84/fulltext/images/b55bcb7c291cb277ead67eefa80600a404c887fed4050f6772146c1914701e13.jpg)

Published online: 03 Jul 2018.

![](/api/attachments/U2FYEW84/fulltext/images/bb1235ffc8ec7a04494f7d21e94cf42b89e398fc5423d6507985b459ec6302e8.jpg)

Submit your article to this journal

![](/api/attachments/U2FYEW84/fulltext/images/29b5b658a8b8b5359540967bfa696ad5854c4ecc6c9d030271cf3d1ac07d8f8b.jpg)

Article views: 23

![](/api/attachments/U2FYEW84/fulltext/images/47ac9f4c9f48fbb40a0ba188a0befd49493aac9224c84426a73950ec03f97141.jpg)

View Crossmark data

EMPIRICAL RESEARCH

Check for updates

# Designing an Internet-of-Things (IoT) and sensor-based in-home monitoring system for assisting diabetes patients: iterative learning from two case studies

Samir Chatterjee <sup>a</sup>, Jongbok Byun<sup>b</sup>, Kaushik Dutta<sup>c</sup>, Rasmus Ulslev Pedersen<sup>d</sup>, Akshay Pottathil<sup>e</sup> and Harry (Qi) Xie<sup>a</sup>

<sup>a</sup>Center of Information Systems and Technology, Claremont Graduate University, Claremont, USA; <sup>b</sup>Forbes School of Business and Technology, Ashford University, San Diego, USA; <sup>c</sup>Muma College of Business, University of South Florida, Tampa, USA; <sup>d</sup>Department of Digitization, Copenhagen Business School, Copenhagen, Denmark; <sup>e</sup>Center for Information Convergence and Strategy, San Diego State University, San Diego, USA

## ABSTRACT

The ageing of the global population is creating a crisis in chronic disease management. In the USA, 29 million people (or 9.3% of the population) su<sup>f</sup>er from the chronic disease of diabetes; according to the WHO, globally around 200 million people are diabetic. Left unchecked, diabetes can lead to acute and long-term complications and ultimately death. Diabetes prevalence tends to be the highest among those aged 65 and older (nearly 20.6%), a population which often lacks the cognitive resources to deal with the daily self-management regimens. In this paper, we discuss the design and implementation of an Internet-of-Things (IoT) and wireless sensor system which patients use in their own homes to capture daily activity, an important component in diabetes management. Following Fogg’s 2009 persuasion theory, we mine the activity data and provide motivational messages to the subjects with the intention of changing their activity and dietary behaviour. We introduce a novel idea called “persuasive sensing” and report results from two home implementations that show exciting promise. With the captured home monitoring data, we also develop analytic models that can predict blood glucose levels for the next day with an accuracy of 94%. We conclude with lessons learned from these two home case studies and explore design principles for creating novel IoT systems.

ARTICLE HISTORY Received 10 June 2015 Revised 17 March 2018 Accepted 26 April 2018

KEYWORDS Internet-of-Things; persuasive systems; design science research; diabetes; mobile phones; neura networks

## 1. Introduction

Diabetes mellitus is the most common and serious chronic disease in the United States. Of nearly 29.1 million Americans with diabetes, 30% are aged 65 or older (Centers for Disease Control and Prevention, 2014). California, the largest state in the USA, has the highest incidence of new diabetes cases, with nearly 3.9 million people (diagnosed and undiagnosed) estimated to be su<sup>f</sup>ering from the disease (California Diabetes Program, Diabetes Information Resource Center, 2011). According to the 2010 census, of California’s 3.9 million, nearly 20.6% were aged 65 and older (subsequently referred to as “older adults”). The most worrisome statistic is that the number of Californians aged 65 or older is projected to increase by 100% from 2010 to 2030, to 7.75 million as the Baby Boomer generation turns 65 years old (SCAN Foundation Report, 2012a, 2012b). The global situation is similar (World Health Organization, 2014): nearly 55 million in Europe, 114 million in China, and 62 million people in India have diabetes.

Diabetes is characterised by a sustained elevated blood glucose (BG) level caused by a reduction of insulin secretion where related metabolic disturbances generate severe, acute, and long-term complications that are responsible for premature death and disability (ADA, 2012). The World Health Organization projects that diabetes deaths will increase by more than 50% in the next 10 years, and by over 80% in low–middle income countries between 2009 and 2017 (World Health Organization, 2014). The costs of caring for this disease in the USA are estimated to exceed \$174 billion annually.

Most diabetic patients can manage their disease by complying with self-management guidelines at home. Poor adherence is a signi<sup>fi</sup>cant barrier to e<sup>f</sup>ective glycemic control. Improved outcomes are associated with better adherence to medications, blood sugar self-monitoring, diet and lifestyle changes, and appointment attendance (Blonde & Karter, 2005, Heisler et al., 2007; Schectman, Nadkarni, & Voss, 2002). Barriers include time constraints, knowledge de<sup>fi</sup>cits, denial, limited social support, inadequate resources, declining cognitive abilities, and low selfe<sup>fi</sup>cacy.

Our focus is on older adult patients in the USA, receiving long-term care services in a variety of settings including their homes (home care), the community (e.g., adult day care), residential settings (e.g., assisted living or board and care homes), or institutional settings (e.g., intermediate care facilities or nursing homes). Many of the elderly have di<sup>fi</sup>culty adhering to guidelines because managing diabetes requires a high degree of cognitive resources. A major challenge in chronic disease self-management, particularly in elderly Americans, is social isolation (Liu, 2011). In 2010, approximately 42% of Californians aged 65 and older were living alone.

Healthcare workers are scarce, and the cost of this disease is already a burden for many. Though families and friends want to help their loved ones to better manage their conditions, they often do not know how to act or when to act. Studies consistently show that patients with empowered caregivers or peers have better outcomes; elderly diabetic patients with poor social support have twice the mortality rate of those with adequate support (Chesla, 2010).

Older adults increasingly <sup>fi</sup>nd it harder to deal with the daily regimens as recommended by American Diabetes Association (ADA) guidelines (ADA, 2012). Regularly measuring blood sugar levels, staying physically active, watching diet and calorie intake, and remembering to take medications and insulin can help to manage the disease, but the patients often fail to do so.

A novel approach is to utilise the “Internet-of-Things” (IoT), sensors and mobile phones within the home environment, to monitor activity of daily living (ADL) of older adults; the collected data reveals behaviour patterns and context. In this paper, we introduce a novel concept that we call “persuasive sensing”. Mining patterns from the extracted sensor data, we interact with older adult patients via motivational short message service (SMS) text messages and weekly newsletters whose contents encourage them to adhere to their regimens. Our ultimate objective is to change behaviours. We report results from two home implementations that show exciting promise. Using the data collected from their homes, we show that, with the help of an arti<sup>fi</sup>cial neural network (ANN), we can predict next-day BG levels with 94% accuracy. The predictive model presented here is a breakthrough in at-home sensing research.

In this paper, we describe the design, implementation, and evaluation of this IoT/sensor home monitoring system. In particular, we leverage our expertise in “persuasive technologies”, which are applications and devices intentionally designed to change user behaviour (Chatterjee & Price, 2009; Fogg, 2002, 2009; Hassan & Chatterjee, 2008; Li & Chatterjee, 2010). We address two research questions:

RQ 1: How can using IoT/sensor systems in the home to continuously monitor ADL help to address the adherence issue of self-management in diabetic patients?

RQ 2: How can we build efective predictive models using the home data to predict patient health events?

The rest of the paper is organised as follows. We begin by covering the foundations that are used in the building of the artefacts. Then, we discuss Fogg’s (2009) kernel theory that drives our design principles. We then present our overall methodology. A detailed description of the design and instantiation of our IoT/sensor system follows. Next, we present the evaluation of our artefacts, including subject recruitment, data collection from two iterative case study implementations, and their analyses. We describe the development of the predictive models using ANN. We conclude with a summary of our <sup>fi</sup>ndings, lessons learned, and research contributions.

## 2. Foundations

## 2.1. Wireless sensor networks

Dishongh and Mcgrath (2010) investigate use of wireless sensor networks (WSN) for healthcare; others have discussed challenges of classifying activity (Atallah, Lo, Ali, King, & Yang, 2009; Stankovic, 2004). According to Mukhopadhyay, Gaddam, and Gupta (2008, p. 8), “Sensor networks permit data gathering and computation to be deeply embedded into the environment”. These technologies can deduce a person’s activity from the environmental state. Chen, Yang, Malkin, and Wactlar (2007) tracked social interaction patterns among geriatric patients in a nursing home, using visual, and audio sensors. They noted that changes in behavioural patterns often signal changes in mental and physical states that may not be detected during brief examinations by physicians; some early predictors of dementia, for example, may include simple changes in walking speed, movement around the room, and social interaction behaviours. Under a pilot programme at the Oregon Health & Science University, 300 homes in the Portland area have been wired with tiny sensors that track elderly people’s movements to validate these early clues of dementia and impending Alzheimer’s disease (Neergaard, 2007). Dick et al. (2011) wired a home with sensors to detect ADL. Xiao and Chen (2008) showed that simple SMS reminders are promising in increasing compliance. Tran, Tran, and White (2012) reviewed how smartphone apps can work with BG monitors. Medica devices, information technology, and mobile communications have started to converge; this shift has the potential to revolutionise healthcare in the home (Baker et al., 2007; Xiao & Chen, 2008).

Our research project di<sup>f</sup>ers from the above as we develop “persuasive sensing” methods that leverage data from IoT devices and sensors which interact with the diabetic patients to improve their compliance behaviour. We integrate data from IoT devices and sensors, match those data against the subjects goals, and then persuade them to improve their health outcomes through messages prompting action. Our technology is aimed at lowering caregiver burden while enhancing the patient’s quality-of-life.

## 2.2. Internet-of-Things

The IoT is the network of physical objects or “things” embedded with electronics, software, sensors, and connectivity enabling them to exchange data. The number of IoT devices connected to the Internet will increase to approximately 20–25 billion by 2020 (ABI Research, 2013; Gartner, 2015). The predicted growth and current market indications of IoT-related solutions have prompted a developmental paradigm shift. Along with growth in the IoT, mobile phones are an ideal platform for sending feedback to diabetes patients because the phones are ubiquitous, low-cost, reliable, real time, and versatile, and unlike most technologies, actually enjoy greater usage among racial and ethnic minorities. Mobile phones can serve as self-management tools to help individuals remember and record various health-related activities; they also enable caregivers to review ongoing health patterns and respond quickly to changes in health status (Årsand, Tatara, Østengen, & Hartvigsen, 2010; Fogg & Adler, 2009).

Recent research on creating a framework for IoT (Turber, Brocke, Gassmann, & Fleish, 2014) also provides a number of activities that go into developing a design science research (DSR)-driven IoT artefact. Of special interest in the framework is “Activity A4”, which is the proof-of-concept (PoC) of the applicability of the proposed framework. In this research, we instantiate such an IoT PoC aimed to motivate older diabetic patients to manage their chronic disease and maintain a healthier lifestyle.

## 3. Methodology

## 3.1. Overall research approach

Over the past decade, DSR has emerged as an important research paradigm within Information Systems research, including discussion of the process of DSR, its concomitant artefacts, and the role of theory (Gregor & Hevner, 2013; Hevner & Chatterjee, 2010). From a process perspective, researchers have proposed several frameworks and principles for conducting, justifying, and evaluating DSR (Hevner, March, Park, & Ram, 2004; Pe<sup>f</sup>ers, Tuunanen, Rothenberger, & Chatterjee, 2007). From a product perspective, di<sup>f</sup>ering types of artefacts proceed from DSR studies, such as constructs, models, methods, and instantiations (Hevner et al., 2004; March & Smith, 1995; Pries-Heje & Baskerville, 2008).

In this paper, we follow the DSR paradigm. This research paradigm is about problem solving and presenting solutions through systems and IT artefacts, broadly de<sup>fi</sup>ned as constructs, models, methods, and instantiations. By examining the maturity of the problem domain and the maturity of the solutions space (Gregor & Hevner, 2013), we can present a framework for evaluating the knowledge and research contribution of a design science work. We argue that the application domain is diabetes management which is quite mature, but the solution maturity (especially a technology solution) is low. Hence, we are designing a system to “improve” upon previous approaches.

Our improvement is novel and distinct from previous work in three ways:

(1) While apps are available to measure BG values or maintain diaries for food intake, our system is holistic, combining data from a variety of body-wearable sensors as well as from ambient or environment sensors providing a rich data set. The system then generates messages to prompt necessary actions. This is akin to the G4 type of automated artefacts described by Chatterjee and Price (2009).

(2) We provide persuasive messages that motivate the subjects by tailoring them to the individual’s goals. Fogg’s theory of persuasion (2009) drives the design of these messages.

(3) Most machine-learning techniques in past studies used medical records data from clinics/ hospitals. Instead, we built our predictive models using the home data collected from sensors and IoT devices.

## 3.2. Design cycles

Following Takeda, Veerkamp, Tomiyama, and Yoshikawa (1990), Figure 1 shows the overall methodology adopted in this project, including the six stages in the process and the corresponding methods and activities in this DSR project. We also show in the last column, actual DSR outcomes (see, e.g., Meth, Mueller, & Maedche, 2015).

The genesis of our problem is from medical literature and surveys that clearly highlight the importance of chronic disease management and of diabetes in particular. An IoT/sensor technology system requires certain design principles. The development of the idea led to several actual artefact prototypes. We researched the messages to be sent to patients to alter behaviour and developed them with the help of a medical team.

We obtained Institutional Review Board (IRB) approval for the project. Once the ethics board approved this proposal, we identi<sup>fi</sup>ed two homes with diabetic older adult patients to demonstrate case feasibility, then instantiated and deployed the IoT/sensor systems in the homes. We then analysed all the results. In each iteration of the home deployment, we learned lessons that helped us improve the design cycles. Finally, we list and discuss those lessons and theorising from this DSR project.

![](/api/attachments/U2FYEW84/fulltext/images/a3eadc0e3258cd971fd7dacd6181d68cc939ceabc96da8922571cd11898f7dc6.jpg)  
Our design science research approach.

## <sub>3.2.1</sub> Case study approach

The IoT/sensor system that we deployed within the subjects’ homes is complex. Hence, we view each home with our installed system as a case, an indepth exploration of a given phenomenon. We justify/evaluate (see, e.g., Hevner et al., 2004) the case study and intervention design by the development and evaluation of multiple artefacts.

Thomas (2011, p. 513) suggests that a case study must comprise two elements:

1. A “practical, historical unity”, which I shall call the subject of the case study, and

2. An analytical or theoretical frame, which I shall call the object of the study.

Taking account of this, he summarises as follows:

Case studies are analyses of persons, events, decisions, periods, projects, policies, institutions, or other systems that are studied holistically by one or more methods. The case that is the subject of the inquiry will be an instance of a class of phenomena that provides an analytical frame – an object – within which the study is conducted and which the case illuminates and explicates (p. 513).

While the validity of the case study cannot derive from its representativeness or typicality, as it is not a representative sample from a larger set, the essence of selection must rest in the dynamic of the relation between subject and object. In most case study research, the number of cases is small. But they can still provide meaningful insights (Walsham, 1995, 2006).

In exploratory DSR projects, we often try to demonstrate a PoC. A proof-of-concept or proof-ofprinciple is a realisation of a certain method or idea to demonstrate its feasibility, or a demonstration in principle, whose purpose is to verify that some concept or theory has usable potential. A PoC is usually small and may or may not be complete (POC 2016). But such proof often con<sup>fi</sup>rms whether the researchers are ready for full-scale implementation. We position our work as a PoC via case study and intervention study approach (see Figure 1). This is in itself an important combination of DSR techniques by drawing the case method from the social sciences.

## 4. Designing an IoT/sensor system – the build phase

Our system’s primary objective was to detect activities of older adults in the home and collect diabetesrelated parameters. Our artefact included a network of sensors (environmental or ambiance, several room-based, and body-worn IoT devices). This provided the team with an ideal technology platform for detecting and responding to health-relevant parameters such as movement, sleep, weight, physiological data, and social activity. The system also included daily motivational and relevant text messages to alter the patient’s behaviour.

## 4.1. Kernel theory – Fogg’s B = MAT model

Our design and development is guided by Fogg’s 2009 theoretical model and in<sup>fl</sup>uenced by Fogg’s (2009). In that theory, Fogg posits that Behaviour = Motivation \* Ability \* Trigger, exploring the trade-o<sup>f</sup>s between motivation and ability. In other words, Fogg argues that behaviour changes when motivation, ability, and trigger converge. Most people have low motivation and ability to change. But often an external trigger can help to move them into a high motivation and high ability zone. The SMS/text messages and tailored newsletters in our project are the designed triggers; persuasion is e<sup>f</sup>ective when these triggers are hot, i.e., the subject can act on them easily.

## 4.2. Key design principles

In designing our system, we observed the following key requirements and design principles throughout the process:

DP1 (Socio-technical system): This is a healthcare problem, not a technology problem (Dishongh & Mcgrath, 2010). At the centre is the patient, not the technology. That also means that, as the intervention progresses, we must adapt the design based on patients’ feedback.

DP2 (Simplicity matters): The simpler the technology, the better. As medical professionals have noted, patients must comprehend what the devices are sending as feedback.

DP3 (Interoperability): The WSN (Dutta, Grimmer, Arora, Bibyk, & Culler, 2005) and IoT devices must be reliable and interoperate with a data collection hub inside the home.

DP4 (Tailored trigger): The daily feedback persuasive messages must be fresh, not boring, and tailored so that patient is eager to receive them and remains engaged with the system (Fogg & Adler, 2009). This principle is derived from Fogg’s theory.

DP5 (Reliability and robustness): The system must work in the home, not just in the lab. We require a certain level of reliability so that this can be deployed in a consumer setting.

The overall system architecture is depicted in Figure 2. We used wearable devices and sensors in the subjects’ homes to collect data on their daily activity. We describe below the details of the sensors. An inhome computer installed for this purpose locally integrated data from all of the sensors, communicating using Wi-Fi or Ethernet. A computer periodically uploaded the data to the server in the laboratory over a secured VPN connection through public Internet. In large-scale deployment, this lab server could be hosted in a cloud provider such as Microsoft Azure or Amazon AWS. We analysed the data collected daily at the lab server. We applied machine-learning techniques to estimate blood sugar level and to identify whether the behaviour of the subject deviated signi<sup>fi</sup>cantly from the subject’s “normal” behaviour. The results of these analyses identi<sup>fi</sup>ed the appropriate intervention message, which we sent daily using SMS. Any regular cellphone or smartphone can accept SMS/text. Additionally, we provided to the users a weekly newsletter summarising the week’s progress. Having described the overall system architecture, we now describe the details of the sensors and wearable devices used to collect data.

A WSN device is a packaged data-collecting or -actuating (Pedersen, 2007) component, which includes a sensor and/or actuator, a radio stack, an enclosure, an embedded processor, and a power delivery mechanism (Dishongh & Mcgrath, 2010). The sensor interacts with the environment and sends an appropriate signal (analogue or digital) to the embedded processor (also called microcontroller unit). We used Iris Mote technology developed by Intel and UC Berkeley labs running TinyOS (Levis, 2005). The mote hardware platform consists of a Mote processor radio (MPR) board, a microprocessor, and radio chip. Sensors connect directly to the MPR boards via various interfaces. This combination gives the mote the ability to sense, compute, and communicate. The mote enables analysis of the raw data collected by the sensors before sending it to a data hub (in our case a Windows laptop) that we placed within the home. Subsequently, the hub then uploads daily activity data to the cloud through secured channels via the Internet. We used the following types of sensors and IoT devices in this project:

![](/api/attachments/U2FYEW84/fulltext/images/44a34213102e4aae5378dcc63e3af07ee7eea4da72b985414c3df198fa89907b.jpg)  
Overall system architecture.

## <sub>4.2.1.</sub> Ambient sensors from MEMSIC

A simple on/o<sup>f</sup> switch that detected opening/closing of a garage door (through which a subject leaves homes) also detected use of the back-porch door for outdoor access. An infrared analogue sensor detected presence in the bedroom, a method also used in the Active Bat system (e.g., Coulouris, Dollimore, Kindberg, & Blair, 2011). We placed a pressure pad sensor (from Colonial Medical) in the couch in the living room in front of the TV to help us detect sedentary activity. We used simple on/o<sup>f</sup> sensors to detect opening and closing of a medicine cabinet containing the patient’s medicines and insulin. Note that opening or closing of medication cabinets denotes activity but it does not give us a guaranteed granularity of whether the patient actually took the medicines. A photo sensor connected to the TV detected television usage patterns.

## <sub>4.2.2.</sub> IoT device-level sensors

We chose a BG monitor device that can connect easily to the laptop via USB and can upload BG values daily. We rejected a Bluetooth-enabled glucometer which had reliability issues. In the family room, we placed a wireless weight machine (from Tanita Corporation) that sends weight values via Bluetooth.

## <sub>4.2.3.</sub> Body-wearable IoT device

Patients wore, 24 h a day, a commercial body-wearable <sup>fi</sup>tness-band (armband) from BodyMedia Inc. This multi-sensor records number of steps walked, quality of sleep, and other physiological parameters such as skin temperature. Patients uploaded their data to the cloud by connecting it to a USB port for less than 5 min daily. We showed the subjects how to log into BodyMedia website where they could input diet/nutrition information. Our system fetched daily diet data, with which we computed total calories consumed. We also provided the patients with bottled water and asked them to drink only that during the course of the case study. This was a simple way for us to monitor water intake. We show the details of the various sensors and IoT devices in Figure 2.

## 4.3. Persuasive messaging design

Patients with Type 2 diabetes can manage their chronic conditions by following certain recommendations (ADA guidelines). Prevention strategies for Type 2 diabetes include:

● Losing weight and keeping body mass index (BMI) under control.

● Exercising 30 min or more daily (brisk walking is <sup>fi</sup>ne).

● Developing a low-calorie and low-fat diet. Nutrition guidelines include recommendations for a diet rich in whole grains, fruits, and vegetables.

● Taking necessary medications (including insulin) and measuring blood sugar level regularly.

Most elderly patients cannot adhere to these regimens because of declining cognitive abilities and lack of resources to help them follow the guidelines. Our system is designed to monitor and remind them to do the necessary self-management steps.

Our intervention has multiple components/ artefacts.

● The system sent daily SMS texts on a cell phone. These are persuasive messages based on the subjects’ activity data and target behaviour change.

● We provided a weekly tailored newsletter that summarises healthy living parameters for the subject and a family member or diabetes educator.

Note our intervention (through the prototype IoT/ sensor system) is aimed at engaging patients in diabetes self-management through interactive SMS and newsletter. We ensured that daily text messages sent to the subject were fresh and relevant, to alleviate so-called message fatigue (Fogg & Adler, 2009) and enable hot triggering. Each day the subjects received up to three text messages over a mobile phone. Research has shown the e<sup>fi</sup>cacy of telephone reminders (Dick et al., 2011) and technological cues. However, our system sends feedback on the subject’s actual daily behaviour, which is much more targeted and context relevant. Table 1 shows examples of the persuasive messages, varied for physical activity. We based the texts on the subject’s goals and whether the subject has met or has not met those goals. The speci<sup>fi</sup>c algorithms are artefacts that we have designed.

Messaging algorithm for physical activity. We sent similar daily persuasive text messages for calorie intake, blood <sup>Table 1.</sup>glucose measurement values, and sedentary activity.

<table><tr><td>Case</td><td>Steps ≥8000</td><td>Steps &lt;8000</td></tr><tr><td>Mon</td><td>Great Job! Keep up the good work.</td><td>Don’t give up on physical activity. Try walking a mile each day.</td></tr><tr><td>Tue</td><td>You have exceeded your goal. Congratulations.</td><td>Don’t give up on physical activity. Have you taken the stairs?</td></tr><tr><td>Wed</td><td>You are doing very well. Keep it up!</td><td>Have you reached your goal of 8000 steps?</td></tr><tr><td>Thu</td><td>You are a super hero. You have exceeded your goal.</td><td>You fell short of your goal. Don’t worry. Try to walk a mile after dinner.</td></tr><tr><td>Fri</td><td>You have exceeded your goal. Super job!</td><td>Never say never. You can do it.</td></tr><tr><td>Sat</td><td>Steps graph for past 5 days</td><td>Steps graph for past 5 days</td></tr><tr><td>Sun</td><td>Great Job. Enjoy the Sunday with friends and family.</td><td>It is a beautiful day. Go out and do brisk walking for 30 min.</td></tr></table>

Messaging algorithm for food and nutrition.

<table><tr><td>Case</td><td>Calorie ≤ 2500</td><td>Calorie &gt; 2500</td></tr><tr><td>Mon</td><td>Your careful diet is going to help you reduce weight.</td><td>Try to eat reduced portions today!</td></tr><tr><td>Tue</td><td>Great job. You are watching your diet and will see results soon.</td><td>Avoid takeout and snack foods that are high in fat.</td></tr><tr><td>Wed</td><td>Enjoy green vegetables and salads and you are on your way to lose weight.</td><td>Try 10 baby carrots and a tablespoon of fat-free dressing for a 100-calorie snack.</td></tr><tr><td>Thu</td><td>Your diet calorie intake is under control. Congratulations!</td><td>Did you know that obesity is one of the leading causes of death in this country?</td></tr><tr><td>Fri</td><td>Very well done. If you can walk 5000 extra steps, then treat yourself to a Starbucks Frappuccino.</td><td>Have you tried low calorie drinks such as Diet Sprite?</td></tr><tr><td>Sat</td><td>Your diet trend is looking very good. Keep it up.</td><td>Add a variety of colorful vegetables to your meal today.</td></tr><tr><td>Sun</td><td>Show calorie graph for past 6 days.</td><td>Choose low-fat dairy foods and lean meat.</td></tr></table>

The Bodymedia sensor measures physical activity by the number of steps the subject takes (Table 2).

The customised newsletter is a PDF <sup>fi</sup>le of 4–5 pages which carefully summarises the details of the subject’s weekly performance. The subject and one of our team members (including a diabetes educator) read the report together.

## 5. Evaluation

We demonstrated the feasibility of our prototype system by implementing it in two homes. This is to show viability of the PoC via a small number of cases.

## 5.1. Subject recruitment

With IRB approval, we distributed announcements to recruit subjects via hospitals, diabetes clinics, and personal contacts. The basic eligibility criteria that we included in our recruitment e<sup>f</sup>orts were:

● Subject must have type 2 diabetes,

● Age can be between 45 and 85,

● Gender and race are not relevant,

● Subject must be familiar with cell phone and texting,

● Subject must have a broadband Internet connection at home.

From the pool of prospective candidates who expressed interest, we selected two subjects. The <sup>fi</sup>rst was an 82- year-old retired white male living in the Vista community near San Diego. We instantiated our system in this subject’s home. The second subject was a 60-year-old white female who lives and works in San Diego. She also has type 2 diabetes and hypertension and is obese. She had elevated BG levels and was considered a highrisk subject.

## 5.2. Evaluation design

We designed a pre-/post-type of intervention (see Figure 3). We installed the systems in the two homes sequentially, with 1 week in each home to engineer and set up all of the IoT devices and sensors. The pre-study “benchmarking” period represents 2 weeks during which we collected all data but provided no feedback to the subjects. The 2-week pre-study was su<sup>fi</sup>cient to make sure that the system components (sensors and IoT devices) were stable and operating reliably. We also con<sup>fi</sup>rmed during the pre-study that the subject was doing what he or she had been asked to do. In the post-study period, our system provided messages and feedback. We ran the post-period for nearly 1 month. The <sup>fi</sup>rst implementation was at the male subject’s home, starting October 18 2011, and ending November 25 2011. The second home implementation was for the female subject, starting January 2 2012 and ending March 1 2012. We removed all sensors and other equipment from the subjects’ homes after the interventions. We thanked the subjects and gave them token honoraria for their participation.

## 5.3. Research goals and proposition testing

The goal of the research was to help diabetic patients adhere to better self-management regimens and in the process improve their quality of life. We believe the daily reminders, weekly newsletter, and continuous monitoring can help them adhere to the necessary self-management guidelines. Consequently, we state the following propositions through a pre/post-test:

![](/api/attachments/U2FYEW84/fulltext/images/3228b0fceec894518753367e627cfa15e1f0a6e3803a1aeee0daa36cb49ef19c.jpg)  
Research design for intervention.

P1 (ADL improvement): After using our IoT/sensor system for a fixed period of time, we hope to see improved physical activity, lower calorie intake, and improved weight loss by our subjects.

We also believe that such in-home monitoring systems can help patients lead a better quality of life. Hence, we state our second proposition:

P2 (Health marker and diabetes self-e<sup>fi</sup>cacy (DSE) improvement): After using our system for a fixed period of time, the subject can show reduction in HbA1c and demonstrate greater success in self-eficacy of diabetes management as measured by the dissociative experiences scale (DES).

## 6. Evaluation results

We present the results in Figure 4.

Fitted for BG data (Figure 4A), the trend lines for both the subjects show a gradual decline. This shows positive improvement in maintaining BG levels. We asked both subjects to provide their HbA1c (considered a 90-day average of blood sugar) before and after the intervention. For Subject 1, HbA1c dropped from 12.8% to 6.6%, a highly signi<sup>fi</sup>cant improvement (50% decrease). For Subject 2, HbA1c went down from 8.9% to 8.5%, a positive result but smaller improvement (4% decrease). Clearly, Subject 2 had greater daily <sup>fl</sup>uctuations of her BG-levels. The weight (Figure 4B) and idle time (Figure 4C) trends also show a gradual decline. Figure 4D shows that the trend for the number of steps walked (which re<sup>fl</sup>ects physical activity) is increasing. These results justify our <sup>fi</sup>rst Proposition P1.

Our daily text messages and weekly newsletter were meant to improve the subjects’ behaviour. We conducted a post-intervention exit survey in which we assessed self-e<sup>fi</sup>cacy, using an adaptation of Sarkar, Fisher, and Schillinger (2006) DSE scale. The DSE scale is a reliable, validated 4-item instrument that assesses patients’ perceived competence in diabetes self-management. The survey result in Table 3 shows that subjects’ ability to manage diabetes is improving. It indicates that their quality of life is improving as well. This justi<sup>fi</sup>es our second Proposition P2.

A. Blood Glucose Level  
![](/api/attachments/U2FYEW84/fulltext/images/6e7771bdb4c09c63acb6fe063330b493f58f93e035d74a71d8fede5d16e16fc4.jpg)  
C. Idle Time

B. Weight  
![](/api/attachments/U2FYEW84/fulltext/images/90b0c982eae9e1005c6cf0ff7def8f3589803c2fc9f3c931a246e815add4c587.jpg)

![](/api/attachments/U2FYEW84/fulltext/images/d821f163a33d01fcf841e8243a9a59d86a2368872ca89001ba06f52f90a6025e.jpg)

D. Number of Steps  
![](/api/attachments/U2FYEW84/fulltext/images/d0b5cef572f123b3762a352332bcb12e6b97587ef17fe9a056810cff2711a7df.jpg)  
Intervention results from the subjects’ homes. (A) BG levels; (B) weight trends; (C) idle time; and (D) physical activity.

Table 4 shows the pre- and post-data on various ADL parameters that the systems captured in both home implementations. Besides improvement in weight and BG for both the subjects, we see improvement in sleep e<sup>fi</sup>ciency and sedentary (idle) time. Time in the bedroom not spent sleeping also decreases, representing activity desirable for diabetic patients. We also notice that Subject 2 has a drop in steps compared to pre-study, though over time we see an upward trend in the number of steps taken each day throughout the intervention. Subject 2 was unable to control her calorie intake. Thus, Proposition P1 is only partially true for Subject 2, but justi<sup>fi</sup>ed for Subject 1. We discuss the reasons for this in a later section.

The DSE survey reveals that overall, both subjects feel more con<sup>fi</sup>dent and capable of managing diabetes, supporting P2. It is important to note that this con<sup>fi</sup>dence cannot be tied directly to our persuasive-sensing system. But it is also important to know that as a PoC, the trends showed no worsening.

One of the challenges in ADL research is how such data can help identify a patient’s condition. In short, can we predict the patient’s future condition by monitoring home ADL data? In this DSR project, we set out to do that by designing and building predictive models as another DSR artefact, an output of this research.

## 7. Predictive models using arti<sup>fi</sup>cial neural networks

Generally, the <sup>fi</sup>eld of <sup>predictive</sup> <sup>analytics</sup> combines techniques from statistics, arti<sup>fi</sup>cial intelligence, and data mining based on previously collected sensor data or learned knowledge to make decisions about the present state or future. The <sup>fi</sup>eld of predictive analytics can be divided into three general categories of model types: predictive models, which make nearterm projections based on previous data; descriptive models, which classify data based on commonality of characteristics in the data; and decision models, which are used to interpret data and take actions based on the interpretation, according to a prede<sup>fi</sup>ned set of rules. In this section, we explain and demonstrate an approach for health behaviour pro<sup>fi</sup>ling by applying machine learning techniques to human behaviour data captured by sensors. Some of the key challenges in developing such pro<sup>fi</sup>les are:

(i) The sensor data may be inaccurate.

(ii) The subject’s behaviour may di<sup>f</sup>er from day to day.

(iii) Daily routine activities may vary because of unexpected scenarios such as a guest’s arrival or an urgent family situation.

We need to develop an approach for disease pro<sup>fi</sup>ling that addresses these situations but is still able to model human behaviour. Fundamentally, we have relied on a replicator neural network (RNN) (Hoang, Vic, & Andy, 2014; Schmidhuber, 1992) to model human behaviour. Traditionally, researchers have used RNNs to detect anomalies and outliers.

The total number of days for which we could collect data di<sup>f</sup>ered for the two subjects. For Subject 1, we obtained only 21 days of (intervention) data, as the subject had made travel plans before he enrolled in our study. However, for Subject 2, we obtained 30 days of (intervention) data. For each subject, we identi<sup>fi</sup>ed the <sup>fi</sup>rst 14 days (2 weeks) of data as the training data and the rest of the data as the testing data. Thus, for Subject 1 we had 7 days of testing data and for Subject 2 we had 16 days of testing data. Each data point in both the training and testing data set had 11 <sup>fi</sup>elds (see Figure 7, input layers).

Diabetes dissociative experiences scale (DES) exit survey results.

<table><tr><td rowspan="2"></td><td colspan="2">Subject 1 (82-year-old male)</td><td colspan="2">Subject 2 (60-year-old female)</td></tr><tr><td>Pre-persuasive-sensing care</td><td>Post-persuasive-sensing care</td><td>Pre-persuasive-sensing care</td><td>Post-persuasive-sensing care</td></tr><tr><td>I feel confident in my ability to manage my diabetes</td><td>Agree</td><td>Agree</td><td>Agree</td><td>Strongly agree</td></tr><tr><td>I feel capable of handling my diabetes</td><td>Agree</td><td>Agree</td><td>Agree</td><td>Agree</td></tr><tr><td>I am able to do my own routine diabetes care.</td><td>Agree</td><td>Strongly agree</td><td>Agree</td><td>Strongly agree</td></tr><tr><td>I am able to meet the challenge of controlling my diabetes.</td><td>Neutral</td><td>Neutral</td><td>Neutral</td><td>Agree</td></tr></table>

Comparison of all the activity of daily living (ADL) data pre- and post-intervention.

<table><tr><td></td><td>Subject</td><td>Weight</td><td>Blood-glucose</td><td>Steps</td><td>Sleep efficiency</td><td>Lying down time (minutes)</td><td>Sleeping time (min)</td><td>Calorie intake</td><td>Time in bedroom (not sleeping)</td><td>Total in-out number</td><td>Idle time (min)</td></tr><tr><td rowspan="2">Pre-study (mean)</td><td>1</td><td>202.60</td><td>155.00</td><td>2328</td><td>0.60</td><td>863</td><td>383</td><td>2277</td><td>1606</td><td>42</td><td>1912</td></tr><tr><td>2</td><td>265.80</td><td>200.00</td><td>3942</td><td>0.58</td><td>644</td><td>222</td><td>1588</td><td>14</td><td>23</td><td>169</td></tr><tr><td rowspan="2">Post-study (mean)</td><td>1</td><td>193.26</td><td>125.42</td><td>5251</td><td>0.78</td><td>660</td><td>510</td><td>1549</td><td>531</td><td>18</td><td>771</td></tr><tr><td>2</td><td>261.70</td><td>190.41</td><td>2445</td><td>0.83</td><td>522</td><td>463</td><td>1614</td><td>6.52</td><td>10</td><td>72</td></tr></table>

One of the key characteristics of an RNN is that the input and outputs are same. In our scenario, we used daily human behaviour data (such as number of steps, total sleep time, minutes lying down, time in watching TV, weight, number of times in/out of home, etc.) as both the input and output. The RNN is trained based on the same input and output. During testing, the mean square error (MSE) between the input and output is taken as the indication of whether the test input data follows the pattern derived from the training input data (see Figure 6).

One of the challenges in feeding the data of daily behaviour into the RNN is that the data may have some anomalies for reasons not related to our research and out of our control (such as visitors in the subject’s home, a long absence from the house, or issues related to sensors). The <sup>fi</sup>rst step in building the pro<sup>fi</sup>le data was to identify these data items. For this, we applied the K-mean clustering technique on the daily behavioural data of the subject. We took the data points related to the largest cluster in the K-mean output as the routine daily behaviour of the subjects, then fed the daily data into the RNN as both input and output to train the RNN. Figures 5 and 6 depict the process.

We collected the daily behaviour data of two subjects (marked as Subject 1 and Subject 2) over the course of 21 days and 30 days, respectively. The data included – (i) weight, (ii) BG, (iii) number of steps taken, (iv) quality of sleep, (v) total minutes lying down, (vi) total sleep time, (vii) total calorie intake, (viii) bedroom time, (ix) couch time, (x) TV time, and (xi) total number of times in and out of the house. We computed these data items daily from the raw sensor data. Thus, the data had 11 columns, one for each data item. For Subject 1, we had 21 rows and for Subject 2, we had 30 rows (one row per day per subject).

For Subject 1, we <sup>fi</sup>rst applied the K-mean clustering algorithm on these 21 data points. The clustering resulted in only one cluster, indicating that there were no outlier data points. Next, we randomly divided the 21 data points into two groups: the training data set and the testing data set. We fed the training data set into the RNN with 11 input variables, 11 output variables and 3 hidden layers, each with 8 neurons (see Figure 7). Once we had built up the RNN model, we fed the second group, i.e., the testing data set, into the model. The average MSE of the testing data for the RNN was just 6.21%. We applied the same approach to the second subject’s data with a similar RNN structure, <sup>fi</sup>nding a testing error of 3.52%.

This indicates that Subject 1’s behaviour can be predicted with an accuracy of 93.79% and Subject 2’s behaviour can be predicted with an accuracy of 96.48%. Such a di<sup>f</sup>erence could be due to the demographic di<sup>f</sup>erences between the two subjects and the nature of their daily behaviours. For example, Subject 1 was more open to change than Subject 2, based on persuasive messages sent.

![](/api/attachments/U2FYEW84/fulltext/images/9871c3f719c0a852c2caddb27e73a2b97a47214f9c44e07e75adce20c3e1ad9a.jpg)  
RNN architecture for pro<sup>fi</sup>le building.

![](/api/attachments/U2FYEW84/fulltext/images/82000a381fb70f6242ee67cfed65c676b3a0457869afe944b6bcb4e1bffad8ca.jpg)  
Using RNN model for disease identi<sup>fi</sup>cation and matching.

Overall, our interventions demonstrate that the RNN was capable of pro<sup>fi</sup>ling the subjects based on daily sensor data. Such a model can be used daily to identify a major deviation from the pro<sup>fi</sup>le and thus a possible health condition that needs attention.

## 8. Predicting blood sugar levels

In this section, we demonstrate how an ANN-based model can use daily behaviour data to predict a BG level. We know that calorie intake and physical activity directly impact the BG level (Blonde & Karter, 2005). However, patients may <sup>fi</sup>nd it di<sup>fi</sup>cult to gauge whether their daily activities and calorie intake are appropriate to reach their target blood sugar level. In this section, we demonstrate an ANN-based model patients can use to predict their daily blood sugar level based on their behavioural data captured by sensors. We propose two models for this purpose.

For the <sup>fi</sup>rst model for Subject 1, we have 20 data points; note that we do not have the BG level for 22nd day of the intervention. Therefore, we cannot use the behavioural data for the 21st day. We prepare 20 data points, where the input is the behavioural and physiological data on day D and the output is the morning BG level on day D + 1. We randomly divide the data into two sets: training and testing. First, we train the model with the training data set. Next, we run the testing data set through the model to measure the testing error. We got an error of 7.5%, i.e., the model is able to predict the next day’s BG level with an average accuracy of 92.5%. We applied the same approach for the BG level prediction for Subject 2, and got an error of 6.6%, i.e., accuracy of 93.4%.

For the second model, we added the blood sugar level of day D in the input layer. In this model, we predict the morning BG level of day D + 1 based on behavioural and physiological data in day D and the morning BG level in day D. Other than the addition of the day D morning BG level in the input layer, the neural network structure remains the same as in Figure 8. As in the previous scenario, we divide our data randomly into two sets, training and testing. First, we train the model and then we test it using the test data. We got a test error of only 4.1% for Subject 1 and 6.1% for Subject 2, i.e., an accuracy of 95.9% and 93.9% for Subject 1 and Subject 2, respectively.

![](/api/attachments/U2FYEW84/fulltext/images/d63c7271674eb235205c8c87a44820475365e5201c951ef91ffa8afc9eab3bef.jpg)  
ANN model for predicting BG level.

Summary of results.

<table><tr><td rowspan="2"></td><td colspan="2">BG level of previous day not included</td><td colspan="2">BG level of previous day included in the model</td></tr><tr><td>Training error</td><td>Testing error</td><td>Training error</td><td>Testing error</td></tr><tr><td>Subject 1</td><td>3.3%</td><td>7.5%</td><td>3.1%</td><td>4.1%</td></tr><tr><td>Subject 2</td><td>2.4%</td><td>6.6%</td><td>2.9%</td><td>6.1%</td></tr></table>

Thus, if the BG level is available for 1 day, based on behavioural data we can predict the expected BG level for the next day morning with an accuracy of 93.9–95.9%. If the BG level is not available, we can still predict the BG level of the subject with an accuracy of 92.5–93.4%. This is a high accuracy of prediction and has major implications for medical decisionmaking research.

Table 5 shows the summary of our results for the two ANN-based predictive models for both Subject 1 and Subject 2. Considering the complexity of the health scenario, we believe these are acceptable results.

## 9. Lessons learned from iterative case studies

This persuasive-sensing DSR project was extremely challenging for the team in several respects. Recruiting older adult patients who <sup>fi</sup>t our eligibility criteria was di<sup>fi</sup>cult. When we met a group of prospective subjects at a retirement community, one subject expressed keen interest in participating; a few days later, that person was hospitalised and hence unavailable for the project. Over the course of the project, we learned other important lessons which we describe below. These general lessons from this research can be used to further enhance new system designs.

The <sup>fi</sup>rst home implementation produced the following challenges and lessons:

Lesson 1 (sensor reliability): The Iris mote sensor system was unreliable, sometimes malfunctioning. We had to <sup>fi</sup>x errors several times before the mote sensors became stable. We quickly realised that such IoT and sensor system deployment needs <sup>fi</sup>eld support.

Lesson 2 (wearable computing): The BodyMedia armband needs to be tight around the skin. Our male subject had skin sclerosis, so sometimes the armband did not connect properly; at other times it produced a skin rash. We solved this by placing the BodyMedia on his leg, under his sock to anchor the device against his leg and deliver a better measurement than placing the device on his arm. Future studies must address the comfort and usability of wearable computing products.

Lesson 3 (interoperability hub): The base computer we used as a hub, a Windows laptop, rebooted itself (probably following a security update). The reboot killed many of the processes we were using and required manual intervention to bring everything back to the normal state. Sometimes the subject’s home Wi-Fi would malfunction, a<sup>f</sup>ecting our ability to collect data. Such systems require a very reliable and robust Wi-Fi infrastructure along with a 24/7 data hub design.

Lesson 4 (aesthetics): Our <sup>fi</sup>rst subject was married, and his wife had some issues with us placing sensors and IoT devices throughout the house, as they destroyed her notion of home beauti<sup>fi</sup>cation. We had to deploy the equipment in a way that minimised the disruption.

The second subject did not seem to respond well to dietary messages. We later learned that her daughter, living in an adjacent apartment, actively undermined the subject’s e<sup>f</sup>orts to eat more healthy foods. This suggests that “peer” in<sup>fl</sup>uence can have a signi<sup>fi</sup>- cant impact on behaviour. Hence, we now are looking at a “buddy” project where both the subject and a peer/buddy receive text messages about the health condition of the subject.

At a higher level of abstraction, this research provided several lessons that could further the research and commercial product development in this domain, sensor-based in-home monitoring system to assist a particular health condition.

● The architecture depicted in Figure 2 is both innovative and generic (Uckelmann, Harrison, & Michahelles, 2011). Though we deployed it to target diabetic patients, a similar architecture can target heart disease patients, geriatric patients, etc. The overall approach of data collection to monitor subjects, applying machine learning techniques to identify anomalies in the subject’s behaviour and providing mobile device-based interventions to assist the subjects in behaviour change is unique and generic to apply in other situations. Much silo research exists in intervention design, smart home design, and sensor based activity recognition. We believe this is the <sup>fi</sup>rst paper to demonstrate that the appropriately designed system combining sensor, data collection, machine learning and mobile device-based intervention actually works well in helping to change behaviour for subjects who may not be technologically savvy.

● In addition to the complexity of developing new models of prediction and intervention messages, researchers should not underestimate the engineering challenges associated with deploying these technologies in homes.

● One of the reasons we used a simple SMS-based message intervention and used cell phones was ease of use by the population group (60 and above) in the study. This population has spent most of their life without any cell phone; using an Android or iPhone would have signi<sup>fi</sup>cantly challenged the subjects. With the simple user interface in our research, we did not see any challenge for the subjects to use the technology. Researchers must select appropriate devices that are simple to interact with.

● To have the highest impact, intervention messages should be limited. We sent no more than three daily SMSs. Too many intervention messages reduce the value of such messages and subjects tend to ignore them.

● The weekly newsletter played an important role in providing feedback. The newsletter provided us a chance to create interactions and open communication between care providers, family member and the subject. Such an interaction improved the subject’s motivation to do better in subsequent weeks or at least stay on top of the self-management.

● The machine learning could derive summary information that otherwise is not possible to gather. We used the neural network approach to assess each patient’s overall condition and raise any deviation through daily SMS or weekly newsletter for follow-up. The predictive ANN model can help to identify high-risk alerts for patients who may have adverse episodic events.

## 10. Contributions of this study

This highly innovative DSR project on persuasive sensing contributes to both practice and theory.

## 10.1. Contributions to practice

We designed and built an in-home activity-monitoring system using IoT devices and sensors with the goal of achieving behaviour changes and improved health outcomes. Using a pre- and postintervention method, the subjects received daily text messages based on their behaviour the previous day. These persuasive messages used strategies such as motivation, praise, guilt, or reward to encourage positive behaviour change. Each subject also received a tailored health newsletter at the end of each week that summarised various physiological and biological parameters. Subject 1 showed tremendous improvement in HbA1c (a 90-day average) levels, which dropped from 12.8% before intervention to 6.6% after intervention. Subject 2’s HbA1c decreased from 8.9% to 8.5%.

We present the design of the IoT/sensor system as a novel PoC. This PoC di<sup>f</sup>ers from prior e<sup>f</sup>orts in that it is a holistic system that aims to assist older adults who su<sup>f</sup>er from cognitive decline issues by suggesting actionable ideas and linking feedback messages to their actual activity behaviour. Moreover, the 24/7 monitoring system can interact with the subjects in real time. Current healthcare providers typically provide ine<sup>f</sup>ective paper-based informational materials to patients. Most existing apps for diabetes management are stand-alone, relying wholly upon e<sup>f</sup>orts by the subjects, as opposed to making it easier for subjects to act upon self-management guidelines. Our system integrates vital data with persuasive messages to provide relevant actionable messages, a combination which has a greater impact on subjects.

Our RNN model shows that it is possible to pro<sup>fi</sup>le a subject and accurately predict relevant medical parameters with 93.9–95.9% accuracy. The ability to predict blood-glucose levels 24 h in advance enables noti<sup>fi</sup>cation of the patient, family members, and even the patient’s physician that adverse health conditions may be impending.

Treating diabetic patients who are not able to manage their own conditions is extremely costly because of the large number admitted to emergency rooms (or ICUs); many of those diabetics are readmitted within 30 days. With changes in healthcare laws, hospitals are not fully reimbursed for these visits; those same hospitals face penalties based on the patient-readmission percentages, so reducing hospital readmission is crucial. Our persuasive-sensing system along with RNN modelling of a diabetic patient contributes signi<sup>fi</sup>cantly toward achieving healthy lifestyles for older patients who are su<sup>f</sup>ering from this potentially deadly disease. Such intervention systems, which we foresee becoming commonplace in the near future, can relieve burdens of caregivers who are already overwhelmed with caseloads and help patients to better self-manage their chronic conditions in their homes.

## 10.2. Contributions to theory

As Gregor and Hevner (2013) note:

“We are of the view, as expressed in other branches of science, that contributions to knowledge could be partial theory, incomplete theory, or even some particularly interesting and perhaps surprising empirical generalization in the form of a new design artifact”. (p. 339)

Our artefacts are a major contribution to DSR knowledge. We note that the relationship between the nature of the artefact/object/problem space studied in DSR is separate from the contributions made by a DSR study. In general, we use the term “artefact” in this paper to refer to a thing that has, or can be, transformed into a material existence as an arti<sup>fi</sup>cially made object (e.g., model, instantiation) or process (e.g., method, software). The construction of an artefact and its description in terms of design principles and technological rules are steps in the process of developing more comprehensive bodies of knowledge or design theories.

Artefacts as DSR Knowledge.

<table><tr><td>Artefact Entity from this persuasive-sensing DSR project</td><td>A: Artefact TypeK: Kernel theoryE: Evaluation</td><td>TheorisingPrincipal embodied knowledgeLessons learned</td></tr><tr><td>Texting/SMS system &amp; tailored newsletters</td><td>A: Method/algorithmK: Fogg&#x27;s theory (Fogg, 2009)E: Focus group and two propositions</td><td>We based each triggering message on ADL data and followed Fogg&#x27;s &quot;hot trigger&quot; theory. Built-in rules keep the messages engaging and easily actionable. Medical practitioners vetted the actual messages in a focus group.The tailored newsletter PDF file summarises all relevant activity data for the week and presents the subject with information that enhances his or her understanding of the disease. Jointly read by a family member or certified diabetes educator and the patient, the newsletters can also remedy the social isolation problem older adult patients often have. We confirmed this benefit during exit interviews when subjects mentioned that the discussion with the diabetes educator enhanced their knowledge about their status and progress.</td></tr><tr><td>The ADL IoT/sensor system</td><td>A: InstantiationK: Internet-of-ThingsE: In situ deployment and data collection</td><td>Designing clean architecture for using a variety of IoT devices and sensors requires understanding of the subjects&#x27; preferences in the home; a key design principle is that it should be unobtrusive. Choice of what to sense and how much to sense depends on intended outcomes and goals. Even though we are demonstrating a proof-of-concept, a general architecture for data acquisition and integration emerges that is applicable to monitoring other diseases such as heart failure or COPD.</td></tr><tr><td>Predictive analytics tool (RNN and ANN models)</td><td>A: ModelK: Machine learning and artificial intelligenceE: Generalisation (i.e., predictive accuracy on test data)</td><td>Neural network models can help to build disease profiles of patients with their activity data. These models can also successfully predict next-day vitals, significantly assisting the patient and preventing hospital admissions.</td></tr></table>

![](/api/attachments/U2FYEW84/fulltext/images/bb94f07a0c48bb33fa381977e176fa50542d82571cf3a1f5c14c29c0ceb4fd0f.jpg)  
Application Domain Maturity  
IoT/sensor instantiation falls in improvement knowledge quadrant.

In this DSR project, we have constructed several di<sup>f</sup>erent artefacts that each embody knowledge, and their collective working makes the entire system operate. Table 6 lists the di<sup>f</sup>erent artefacts that are outputs of this project along with some key knowledge contributions from each.

A DSR project has the potential to make di<sup>f</sup>erent kinds of research contributions depending on its starting points in terms of problem maturity and solution maturity (Gregor & Hevner, 2013). Figure 9 presents a 2 × 2 matrix of research project contexts and potential DSR research contributions. The x-axis shows the maturity of the problem context from high to low. The y-axis represents the current maturity of artefacts that exist as potential starting points for solutions to the research question, also from high to low. The four quadrants represent:

● Invention: invent new solutions to new problems (this is sparse as of now),

● Improvement: develop new solutions for known problems,

● Exaptation: extend known solutions (perhaps from reference disciplines) to new problems,

● Routine design: apply known solutions to known problems (this is typically what consultants do).

The domain of our work is in diabetes treatment and monitoring. The health application domain is quite matured. However, technology-driven solutions in this <sup>fi</sup>eld are relatively new and immature. Hence this IoT/sensor system is a novel PoC solution in the upper left quadrant and provides an improvement over other solutions.

We should also note that our work is not simply a solution to a known problem. Rather, we have built a solution to an entire class of problems. The solution can be generalised. A similar architecture using IoT devices and sensors to monitor vitals and other data can work for patients su<sup>f</sup>ering from other chronic diseases such as chronic obstructive pulmonary disease, heart failure, cancer, or stress/anxiety. Some devices and parameters would change, but the architecture for collecting IoT data remains valid. Hence, we argue that the research contribution is generalisable across a class of problems.

Extensions of our work will bene<sup>fi</sup>t several new directions with respect to data privacy and applicability. For example, data can be shared directly to the patient, to the healthcare provider or even to an employer. This might lead to incentive plans lowering insurance premiums paid by the patients out-of-pocket when they can demonstrate better self-management actions. Who gets to see what data and when is in itself a project researchers should address in the future.

## 11. Conclusions

In this DSR project, we explained the design, development, and implementation of an IoT/sensor system that monitors diabetic patients in their homes and uses text messages along with tailored newsletters to alter their behaviour and achieve improved health outcomes. The system as a design science exemplar is novel and highly innovative. We have further developed models to pro<sup>fi</sup>le diseases and help predict vital parameters which could provide an extra window of time for caregiver teams to help the patient. Our predictive models have an accuracy rate of 94%.

One of the key limitations of our research is the small number of cases – just two. The complexity in engineering the sensors and devices and a constrained access to resources were behind this small number. However, even though the number of case studies in this DSR project is low (see Walsham, 1995, 2006), we are able to generalise our insights and interpretations to more general models and methods. In future research, we intend to run a random control trial (RCT) before commercial release of the system. RCTs are expensive. An RCT would be the ideal way to proceed before rolling out full-scale commercial implementations.

When designing a persuasive system based on IoT devices and sensors and guided by Fogg’s (2009) persuasive theory work, researchers must take into account more than the purely technical factors. We must pay extra attention to the so-called backend of a system and ensure that the user is respected throughout the system, including the sensitive nature of the data and the in<sup>fl</sup>uence of the messages sent to the diabetes patients. Spiekermann addresses this indirect design aspect in the “Idea of Man” in Systems Design (Uckelmann et al., 2011). In this case, we decided to use only US Food and Drug Administration approved devices and store the data in a central secured database, privacy being of utmost concern throughout the project.

We already know that there are not enough caregivers to assist the world’s growing older population. As the IoT phenomenon grows (ABI Research, 2013; Gartner, 2015), we are likely to see its usage in healthcare. Ours is one of the early attempts to understand how IoT and sensors can assist older adult patients in the home. Systems such as ours present novel technological breakthroughs that can help patients su<sup>f</sup>ering from chronic diseases to change their self-management behaviours and achieve improved health outcomes. At the same time, our predictive tools can curtail the rise in the cost of treating such patients, thereby lowering the <sup>fi</sup>nancial burden that societies have to face.

## Acknowledgements

We acknowledge Miles Moore for helping us recruit subjects and many reviewers who have helped improve this manuscript.

## Disclosure statement

No potential con<sup>fl</sup>ict of interest was reported by the authors.

## Funding

This project was partially supported by an EAGER grant from the National Science Foundation CNS [Award no.: 1048366]

## ORCID

Samir Chatterjee http://orcid.org/0000-0002-3268-6604

## References

ABI Research (2013) More than 30 billion devices will wirelessly connect to the internet of everything in 2020. http://www.stsc.hill.af.mil/crosstalk/2003/01/George. html, accessed 15 May 2015.

American Diabetes Association (2012) Living with diabetes: Treat and care. http://www.diabetes.org/living-with-dia betes/treatment-and-care/?loc=DropDownLWD-treat ment, accessed 14 March 2012.

Årsand, E., Tatara, N., Østengen, G., & Hartvigsen, G. (2010). Mobile phone-based self-management tools for type 2 diabetes: The few touch application. Journal of Diabetes Science and Technology, 4, 328–336.

Atallah, L., Lo, B., Ali, R., King, R., & Yang, G.-Z. (2009). Real-time activity classi<sup>fi</sup>cation using ambient and wearable sensors. IEEE Transactions on Information Technology in Biomedicine : A Publication of the IEEE Engineering in Medicine and Biology Society, 13, 1031–1039.

Baker, C. R., Armijo, K., Belka, S., Benhabib, M., Bhargava, V., Burkhart, N., & Wright, P. K. (2007) Wireless sensor networks for home health care. In Proceedings the 21st international conference on advanced information networking and applications workshops, 2007 (AINAW’07), 832–837.

Blonde, L., & Karter, A. J. (2005). Current evidence regarding the value of self-monitored blood glucose testing. The American Journal of Medicine, 118(9A), 20–26.

California Diabetes Program, Diabetes Information Resource Center. (2011). California diabetes fact sheet. San Francisco, CA: California Department of Public Health, University of California, San Francisco.

Centers for Disease Control and Prevention. (2014). National diabetes statistics report: National estimates and general information on diabetes and pre-diabetes in the United States. Atlanta, GA: Author.

Chatterjee, S., & Price, A. (2009). Healthy living with persuasive technologies: Framework, issues, and challenges. Journal of the American Medical Informatics Association, 16, 171–178.

Chen, D., Yang, J., Malkin, R., & Wactlar, H. D. (2007). Detecting social interactions of the elderly in a nursing home environment. ACM Transactions on Multimedia Computing, Communications and Applications, 3(1), 1–22.

Chesla, C. A. (2010). Do family interventions improve health? Journal of Family Nursing, 16, 355–377.

Coulouris, G., Dollimore, J., Kindberg, T., & Blair, G. (2011). Distributed systems: Concepts and design (5th ed.). USA: Addison-Wesley Publishing Company.

Dick, J. J., Nundy, S., Solomon, M. C., Bishop, K. N., Chin, M. H., & Peek, M. E. (2011). The feasibility and usability of a text-message based program for diabetes self-management in an urban african–american population. Journal of Diabetes Science and Technology, 5, 1246– 1254. doi:10.1177/193229681100500534

Dishongh, T. J., & Mcgrath, M. (2010). Wireless sensor networks for healthcare applications. Boston, MA: Artech House.

Dutta, P., Grimmer, M., Arora, A., Bibyk, S., & Culler, D. (2005) Design of a wireless sensor network platform for detecting rare, random, and ephemeral events. In Proceedings of the 4th international symposium on Information processing in sensor networks. IEEE Press.

Fogg, B. J. (2002). Persuasive technology: Using computers to change what we think and do (1st ed. ed.) Interactive Technologies. San Francisco: Morgan Kaufmann.

Fogg, B. J. (2009) A behavior model for persuasive design. In Proceedings of the 4th International Conference on Persuasive Technology, Claremont, CA.

Fogg, B. J., & Adler, R. (Eds.). (2009). Texting 4 health: A simple powerful way to improve lives. Stanford persuasive lab. California: Stanford Captology Media.

Gartner (2015) Gartner. http://www.gartner.com/news room/id/3165317, accessed 17 April 2017.

Gregor, S., & Hevner, A. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37, 337–356.

Hassan, T., & Chatterjee, S. (2008) A sensor based mobile context-aware system for healthy lifestyle management. In Proceedings of the 3rd International Conference on Persuasive Technology, Oulu, Finland. Springer.

Heisler, M., Faul, J. D., Hayward, R. A., Langa, K. M., Blaum, C., & Weir, D. (2007). Mechanisms for racial and ethnic disparities in glycemic control in middle-aged and older americans in the health and retirement study. Archives of Internal Medicine, 167, 1853–1860 doi:10.1001/archinte.167.17.1853.

Hevner, A., & Chatterjee, S. (2010). Design research in information systems: Theory and practice. US: Springer Publisher Inc.

Hevner, A., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28, 75–105.

Hoang, A. D., Vic, C., & Andy, S. (2014) Anomaly detection using replicator neural networks trained on examples of one class. In W. N. Browne et al. (Eds.) 10th International Conference Proceedings of Simulated Evolution and Learning (SEAL 2014) (pp. 311–322) Dunedin, New Zealand: Springer International Publishing.

Levis, P. (2005). TinyOS: An operating system for sensor networks. In W. Weber, Rabaey, & E. Aarts (Eds), Ambient intelligence (pp. 115–148). Berlin Heidelberg: Springer Berlin Heidelberg.

Li, H., & Chatterjee, S. (2010). Designing e<sup>f</sup>ective persuasive systems utilizing the power of entanglement: Communication channel, strategy and a<sup>f</sup>ect. In T. Ploug, P. Hasle, & H. Oinas-Kukkonen (Eds.), Persuasive technology, lecture notes in computer science. LCNS, 6137(27), 274–285 Springer Berlin/Heidelberg.

Liu, L. (2011). Social connections, diabetes mellitus, and risk of mortality among white and African–American adults aged 70 and older: An eight-year follow-up study. Annals of Epidemiology, 21, 26–33.

March, S. T., & Smith, G. F. (1995). Design and natural science research on information technology. Decision Support Systems, 15, 251–266.

Meth, H., Mueller, B., & Maedche, A. (2015). Designing a requirement mining system. Journal of the Association for Information Systems, 16(9), 799–837.

Mukhopadhyay, S. C., Gaddam, A., & Gupta, G. S. (2008). Wireless sensors for home monitoring – A review. Recent Patents on Electrical Engineering, 1, 32–39.

Neergaard, L. (2007). Can motion sensors predict dementia. http://www.forbes.com/feeds/ap/2007/06/18/ap3831975. html?partner=alerts, accessed 19 September 2007.

Pedersen, R. U. (2007). TinyOS education with LEGO MINDSTORMS NXT. In J. Gama and M. M. Gaber

(Eds.), Learning from data streams: Processing techniques in sensor networks. (pp. 231–241). Berlin, Heidelberg: Springer.

Pe<sup>f</sup>ers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24, 45–77.

POC (2016). https://en.wikipedia.org/wiki/Proof\_of\_con cept, accessed February 17 2016.

Pries-Heje, J., & Baskerville, R. (2008). The design theory nexus. MIS Quarterly, 32, 731–755.

Sarkar, U., Fisher, L., & Schillinger, D. (2006). Is self-e<sup>fi</sup>cacy associated with diabetes self-management across race/ ethnicity and health literacy? Diabetes Care, 29, 823–829.

SCAN Foundation Report. (2012a, February). Demographic & economic characteristics of aging Californians (updated). Long Beach, CA: SCAN Foundation.

SCAN Foundation Report. (2012b, April). Who needs and uses long-term care in California. Long Beach, CA: SCAN Foundation.

Schectman, J. M., Nadkarni, M. M., & Voss, J. D. (2002). The association between diabetes metabolic control and drug adherence in an indigent population. Diabetes Care, 25, 1015–1021.

Schmidhuber, J. (1992). Learning complex, extended sequences using the principle of history compression. Neural Computation, 4, 234–242.

Stankovic, J. A. (2004). Research challenges for wireless sensor networks. ACM SIGBED Review, 1, 9–12.

Takeda, H., Veerkamp, P., Tomiyama, T., & Yoshikawa, H. (1990). Modeling design processes. AI Magazine, 11(4), 37–48.

Thomas, G. (2011). A typology for the case study in social science following a review of de<sup>fi</sup>nition, discourse, and structure. Qualitative Inquiry, 17, 511–521.

Tran, J., Tran, R., & White, J. R. (2012). Smartphone-based glucose monitors and applications in the management of diabetes: An overview of 10 salient “apps” and a novel smartphone-connected blood glucose monitor. Clinical Diabetes, 30, 173–178.

Turber, S., Brocke, J. V. O. M., Gassmann, O., & Fleish, E. (2014). Designing business models in the era of the internet of things: Towards a reference framework. In M. C. Tremblay, D. VanderMeer, M. Rothenberger, & A. Gupta (Eds.), Advancing the impact of design science: Moving from theory to practice (pp. 17–31). DESRIST 2014, LCNS 8463. Switzerland: Springer.

Uckelmann, D., Harrison, M., & Michahelles, F. (2011). Architecting the internet of things. Berlin Heidelberg: Springer.

Walsham, G. (1995). Interpretive case studies in IS research: Nature and method. European Journal of Information Systems, 4, 74–81.

Walsham, G. (2006). Doing interpretive research. European Journal of Information Systems, 15, 320–330.

World Health Organization. (2014). 10 facts about diabetes. WHO website. http://www.who.int/features/fact<sup>fi</sup>les/dia betes/en/index.html, accessed 2014.

Xiao, Y., & Chen, H. (2008). Mobile telemedicine: A computing and networking perspective (1st ed.). Boston, MA: Auerbach Publications.
