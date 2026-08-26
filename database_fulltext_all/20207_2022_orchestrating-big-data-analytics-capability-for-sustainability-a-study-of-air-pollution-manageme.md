---
otero_id: 20207
otero_key: "KDRHY7GQ"
title: "Orchestrating big data analytics capability for sustainability: A study of air pollution management in China"
authors: "Dan Zhang; Shan L. Pan; Jiaxin Yu; Wenyuan Liu"
year: "2022"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103231"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Journal Pre-proof

Orchestrating Big Data Analytics Capability for Sustainability: A Study of Air Pollution Management in China

Dan Zhang, Shan L. Pan, Jiaxin Yu, Wenyuan Liu

![](/api/attachments/KDRHY7GQ/fulltext/images/e49fdb46b5852d962067330f411bc4dde28847823b672008aeb1809048600984.jpg)

PII: S0378-7206(19)30201-0

DOI: https://doi.org/10.1016/j.im.2019.103231

Reference: INFMAN 103231

To appear in: Information & Management

Received Date: 1 March 2019

Revised Date: 25 October 2019

Accepted Date: 3 November 2019

Please cite this article as: Zhang D, Pan SL, Yu J, Liu W, Orchestrating Big Data Analytics Capability for Sustainability: A Study of Air Pollution Management in China, Information and amp; Management (2019), doi: https://doi.org/10.1016/j.im.2019.103231

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# Orchestrating Big Data Analytics Capability for Sustainability: A Study of Air Pollution Management in China

Dan Zhang<sup>a</sup>, Shan L. Pan<sup>b</sup>, Jiaxin Yu<sup>c</sup> and Wenyuan Liu<sup>c\*</sup>

<sup>a</sup> Department of Information Resources Management, Business School, Nankai University, Tianjin, China;

<sup>b</sup> School of Information Systems and Technology Management, UNSW Australia

Business School, Sydney, Australia;

<sup>c</sup> School of Information Science and Engineering, Yanshan University, Qinhuangdao, China;

\*Correspondence Email Address:

lwy@ysu.edu.cn

\*Correspondence Postal Address:

Wenyuan Liu, School of Information Science and Engineering, Yanshan University, No. 438, Hebei Avenue, Qinhuangdao, China, 066004

## Abstract

Under rapid urbanization, cities are facing many societal challenges that impede sustainability. Big data analytics (BDA) gives cities unprecedented potential to address these issues. As BDA is still a new concept, there is limited knowledge on how to apply BDA in a sustainability context. Thus, this study investigates a case using BDA for sustainability, adopting the resource orchestration perspective. A process model is generated, which provides novel insights into three aspects: data resource orchestration, BDA capability development, and big data value creation. This study benefits both researchers and practitioners by contributing to theoretical developments as well as by providing practical insights.

Keywords: Big data, big data analytics, sustainability, air pollution, resource orchestration

## Introduction

Many cities have joined the worldwide competition among cities through rapid development, which plays a significant role in shaping socioeconomic aspects at a global level [1]. As a result, cities have gained unprecedented economic benefits that they can invest in improving citizens’ wellbeing and promoting further urban development [2]. However, along with rapid economic development, cities also face numerous challenges during the development process, such as resource deficiencies, air pollution, climate change, human health concerns, crime, traffic congestion, and deteriorating infrastructure [3-5]. These sustainability challenges run counter to the original objectives of city development [6]. It is extraordinarily difficult to analyze and address these challenges, as they are complex, involving nonlinear dynamics as well as multiple domains, interactions and associations, and they are uncertain, as their ongoing evolution creates barriers to assessing and forecasting their future state [7]. The traditional path of city development and management is becoming insufficient for addressing the challenges and inapplicable to the current context. This not only hinders the normal operation and sustainable development of cities but also hampers citizens’ quality of life. Thus, cities are adopting innovative technologies and seeking new forms of management to build the needed capabilities to solve the sustainability challenges [3].

Meanwhile, the emergence and development of big data analytics (BDA) provides cities with great potential to extract meaningful information and gain valuable insights from the oceans of data collected through diverse sources [8, 9]. Governments have started to embrace city development initiatives with BDA applications to solve key societal challenges and improve citizens’ living standards [10]. Acknowledging the potential and opportunity brought by big data to all of society, the United Nations launched the “Big Data for Sustainable Development” initiative in 2017 to achieve the sustainable development goals (SDGs) [11]. The SDGs highlight the promising contribution of big data science and BDA to many aspects of sustainable development, including those related to climate, environmental degradation, poverty, inequality, prosperity, peace, and justice [12]. Accordingly, an increasing number of studies have noted the positive role played by BDA in addressing cities sustainability challenges [8, 13, 14].

Nevertheless, as both the big data technique itself and the application of BDA in a sustainability setting remain in their infancy [8, 15], there are still significant obstacles to utilizing BDA to promote cities’ sustainable development. For instance, data are collected from various sources with different features and formats, which causes data isolation and increases the complexities of data fusion [16, 17]. Meanwhile, there is a lack of data infrastructure, skilled personnel and other resources to support further data processing and analysis and achieve the specified goals, particularly sustainability goals [18, 19]. Data security concerns and privacy issues also hinder data disclosure to the public and data sharing within the public sector [20, 21]. Finally, some argue that the value of big data cannot be unearthed by the simple action of acquiring data [22, 23].

A 2016 Gartner survey revealed that many big data projects show disappointing results, and more than half probably fail to create value and are likely to be abandoned in the near future [24]. Similarly, researchers have argued that most big data investments fail to pay off because the organization either has limited knowledge on how to realize the value of big data or it lacks managerial support for doing so [25, 26]. Accordingly, it has been suggested that organizations rethink their big data strategies and shift their focus from the glamor of big data itself to the capabilities related to creating value from the data [23]. However, as many organizations are still in the early stage of adopting big data [27], there is an urgent call for both theoretical support and practical guidelines on using BDA in various contexts, especially for sustainability.

To respond to this call, the goal of the current study is to understand the use of BDA for sustainability. The necessity of conducting such a study can be seen in both practice and theory. Practically, the findings of the study are expected to provide constructive guidelines for addressing sustainability challenges by successfully utilizing BDA, which will help responsible stakeholders make cost-effective investments in and make full use of BDA within the specific context of sustainability. Theoretically, the current study will contribute to the literature on both BDA and sustainability by linking the two fields and exploring the inner mechanism of using BDA for sustainability.

To achieve the research goal, we introduce the resource orchestration perspective, which is derived from the resource-based view (RBV) [28]. Adopting this perspective, we focus on how the government can effectively orchestrate big data-specific resources to develop BDA capability for sustainability. The adoption of this theoretic lens is based on both practical and theoretical considerations. Practically, BDA capability is essential in unearthing data value, which determines the success of big data projects [29]. In this regard, big data, as the central resource, need to be effectively collected, integrated, coordinated, and leveraged to develop BDA capability. As the resource orchestration perspective is consistent with the trend toward highlighting these resource-focused actions, it is suitable for this study, which aims to provide some practical guidelines. Theoretically, by highlighting the dynamic utilization of resources, the resource orchestration perspective was developed to make up for the flaws of the statics in RBV [28]. This perspective allows the current study to offer insights into the dynamic orchestration of big data resources as well as to examine the process of BDA capability development.

For the current research, we conduct a case study of air pollution management in the Beijing-Tianjin-Hebei (BTH) region in China. The BTH region, as the home to eight of China’s 10 smoggiest cities, is considered by the Chinese government to be the key area in the “War Against Pollution” in China [30]. Air pollution has become an international problem and has several negative impacts on human health [31, 32]. In China, air pollution accounts for an estimated 1.1 million deaths per year, while the annual costs of death, suffering, and decreased food production due to air pollution are approximately US \$38 billion [33]. As one of the greatest sustainability challenges, air pollution management has attracted much attention from the government and the public. The BTH region, covering 216,000 square kilometers and containing 110 million people, is one of the most polluted areas in both China and the world [5]. The governments in the region have been collecting big data to monitor and forecast air quality in real time and are exploring ways to generate novel big data-driven insights for air pollution management. Accordingly, the current study uses air pollution management based on BDA as the study artifact to answer the research question:

“How have big data analytics been used for air pollution management in China?”

The remainder of the paper is organized as follows: The next section illustrates the related theoretical background. The third section introduces the research design, explaining the case selection and describing the data collection and the analysis. The fourth section depicts the case, while the fifth section analyzes the case to identify the process of BDA capability development for sustainability. Finally, the sixth section discusses both the theoretical and practical contributions, and the last section concludes the study.

## Theoretical Background

## Big data and big data analytics

The concept of big data emerged in the last decade and is associated with the development of new sources of data (e.g., social media, machines, smart phones, and sensors), novel technologies, and advanced user skills [29, 34]. Big data is considered the latest era in data’s evolution [35]; big data is defined as datasets whose size makes them beyond the ability of traditional data-related software tools to collect, store, manage, and analyze [36]. This term is often used to describe “massive, complex, and real-time streaming data that require more sophisticated management, analytical, and processing techniques to extract insights” [37, p. 1050]. The features of big data can be summarized as the three Vs: high volume (the quantity of data), high velocity (the speed at which data are generated), and high variability (the different types of data) [38]. De Mauro et al. [39] provided a formal definition of big data: “Big Data are the Information asset characterized by such a High Volume, Velocity and Variety to require specific Technology and Analytical Methods for its transformation into Value” (p. 131).

It has been widely acknowledged that only collecting and storing big data creates little value [23, 40]. To generate value, big data must be processed and analyzed to provide results to decision makers and organizational processes [29]. Thus, big data is considered a resource that has the potential to create actionable and novel insights for both businesses and society when properly managed, processed, and analyzed [15, 41]. Thus, the key to creating value from big data is the use of BDA. Generally, BDA refers to “the activities involved in the specification, capture, storage, access and analysis of such datasets to make sense of its content and to exploit its value in decision-making” [42, p. 771]. The potential of BDA is considered to be its ability to provide insights, enhance decision making, and optimize processes [43]. Researchers have stated that traditional data management and data analysis approaches are unable to manage and analyze big data as the volume, velocity, and variety of data increase [44]. Accordingly, a number of techniques, approaches, and products have emerged that meet the special requirements of BDA applications [37, 45].

BDA processes contain several big data-based activities, such as acquisition, extraction, cleaning, annotation, integration, aggregation, representation, visualization, modeling, analysis, interpretation and so on [16]. Some research further classifies BDA into three types based on the technologies and architectures used, including descriptive analytics, predictive analytics, and prescriptive analytics [29]. It has been argued that some types of BDA can show better performance on some platforms than on others in terms of achieving specific objectives [46, 47]. The differences between BDA types are distinguished as follows: descriptive analytics reveal what has happened; predictive analytics forecast what will happen in the future; and prescriptive analytics assists in the process of decision making by identifying inner mechanisms and optimal solutions [29].

Some researchers have highlighted the importance of generating BDA capability by arguing that the overemphasis on investigating the characteristics of big data directs the focal point away from addressing the essential issue, which is creating BDA capability [37, 48]. BDA capability is highlighted because it allows decisions to be made and supported in more innovative and scientific ways, which also provides novel challenges and opportunities to realize the value of big data [43]. By having BDA capability, organizations can gain unprecedented insights into the investigated subjects and into operations [38]. Mills et al. [43] have argued that although success with big data is not guaranteed, an organization with BDA capability is more likely to gain insights and unearth value from big data. Gupta and George [37] emphasized that it is imperative for organizations to be aware of big data resources and then to determine which to use to develop related BDA capabilities. In their perspective, different from other digital capabilities such as IT capability, the creation of BDA capability particularly requires big data-specific resources and the corresponding data-based actions [37]. Thus, while the challenges associated with big data keep emerging, it is urgent that organizations focus on utilizing big data resources to build organizational BDA capability for addressing related challenges [25].

## Big data analytics for sustainability

Sustainability reflects a concern for the wellbeing of future generations and requires that three core elements be harmonized: economic growth, social inclusion, and environmental protection [49]. The increasing urban population and rapid urbanization require a demanding imperative for sustainability [50] because cities are not only hotspots of natural resource consumption and waste generation but also motors for economic growth and the development of citizens’ living standards [51]. Rapid urban population growth is placing unprecedented pressure on city governments and creating new challenges in addressing emerging problems and maintaining balanced development to meet the needs of multiple stakeholders. Consequently, some societal challenges are appearing in the majority of cities worldwide, including pollution, poverty, discrimination, and crime [52, 53]. To solve these sustainability challenges, in 2015, the United Nations set the 2030 Agenda for Sustainable Development, which has been widely adopted by countries. The 2030 Agenda contains 17 SDGs including 169 targets to be achieved by 2030. SDGs aim to “end poverty, protect the planet, and ensure prosperity for all” [54, p. 1881]. Figure 1 shows a concise representation of the 17 SDGs.

![](/api/attachments/KDRHY7GQ/fulltext/images/37a30027aaebd8af71a3edb2f33e8d5a46972dcffdbcd247a5ad93c44affc9d0.jpg)  
Figure 1. United Nations’ Sustainable Development Goals  
Source: United Nations [55]

Providing guidelines for actions to address the SDGs for global sustainability is very challenging because each development goal includes various concerns and involves numerous stakeholders [56]. Thus, it is required that any decision made to address sustainability issues must be based on strong and sufficient scientific support rather than on the decision makers’ instincts [57]. In this context, big data is expected to help people discover new relationships and mechanisms to make better decisions [16, 29], with great potential for addressing sustainability problems. It has been suggested that big data techniques could assist in the resolution of SDGs [58, 59]. The United Nations has also launched the “Big Data for Sustainable Development” initiative to utilize big data resources and BDA approaches for achieving the corresponding SDGs (see Appendix A). Mills et al. [43] described the following scenario of a world that is benefiting from big data as it pursues sustainability:

“Imagine a world with an expanding population but a reduced strain on services and infrastructure; dramatically improved health care outcomes with greater efficiency and less investment; intensified threats to public safety and national borders, but greater levels of security; more frequent and intense weather events, but greater accuracy in prediction and management. Imagine a world with more cars, but less congestion; more insurance claims but less fraud; fewer natural resources, but more abundant and less expensive energy. The impact of big data has the potential to be as profound as the development of the Internet itself.”

Acknowledging the potential of BDA to address sustainable development issues, some researchers have started to develop BDA tools, algorithms, models, and systems that are expected to assist in the relevant problem solution process [e.g., 60, 61, 62]. Nevertheless, as BDA is still a novel concept, and its application in the context of sustainability is even newer, there is limited knowledge on how to effectively and efficiently use BDA to achieve sustainability goals. Without a relatively clear and sufficient understanding of this topic, it will also be difficult for stakeholders in the relevant fields of sustainability to accomplish the SDGs by 2030. Therefore, there is an urgent call for studies on BDA for sustainability to address the literature gap [57, 63]. Pursuant to the call, this study seeks to develop a process model for using BDA for sustainability, adopting the resource orchestration perspective as the theoretical lens, as discussed in the following subsection.

## The resource orchestration perspective as a theoretical lens

This study adopts the resource orchestration perspective as its theoretical lens. This perspective is derived from the widely known resource-based theory (RBT) [28]. RBT views an organization as a collection of resources and provides a framework for combining these resources [64]. The ability to combine resources determines the organization’s performance and creates its competitive advantages [65]. RBT has been criticized by some researchers for its static nature [66, 67], and they point out that RBT cannot explain why different organizations with similar resources show different performance levels [68].

Considering the dynamic nature of the environment and its influence on resources, a dynamic capability perspective was developed to supplement RBT [69, 70]. Dynamic capability is defined as an organization’s ability to obtain new forms of competitive advantage by renewing its technological, organizational and managerial resources in correspondence with the changing environment [71, 72]. Extending the RBT, this perspective argues that resource reconfiguration can consequently create related capabilities within an organization, which are key to the organization improving its performance and achieving a competitive advantage [68, 73].

Some studies have also criticized RBT for failing to consider resource management actions [28, 70]. These argue that it is the actions conducted with the resources, rather than the resources alone, that affect organizational performance and create an organizational competitive advantage [74]. To address this concern, the resource orchestration perspective was developed by Sirmon et al. [28]; it focuses on investigating how organizations effectively manage and use resources to achieve competitive advantage and improve organizational performance [68]. Sirmon et al. [28] developed a framework to describe three major actions used to orchestrate resources: structuring the portfolio of resources (i.e., acquiring, accumulating, and divesting), bundling resources to build capabilities (i.e., stabilizing, enriching, and pioneering), and leveraging capabilities to create value (i.e., mobilizing, coordinating, and deploying). The resource orchestration perspective has been adopted by some studies as a principal view for assessing the relationship between organizational resources and organizational performance [37]. For example, Chan et al. [68] developed a process model capturing how resources were utilized for successful implementation of an egovernment system based on a resource orchestration perspective. Wang et al. [75] found that in a stable environment, the resource-focused action of resource structuring plays a more significant role in value creation from information technology, while in a dynamic environment, capability building is relatively more significant.

Given the context of the current study and its focus on using BDA for sustainability, the resource orchestration perspective is important because the key to making better decisions about sustainability lies in understanding what big data resources the government has and identifying the best way to utilize the specific data resources [37, 48]. Previous studies have commonly acknowledged that big data is one of the critical resources determining organizational performance [27]. However, it has been argued that big data alone is unlikely to influence performance [25]. To achieve specific purposes, such as addressing sustainability issues, an organization needs to orchestrate certain big data resources to build BDA capabilities [76]. Thus, the resource orchestration perspective seems to be a suitable choice as the theoretical lens for the current study.

Meanwhile, in adapting the theoretical lens to the current context, preliminary concepts have been identified from the resource orchestration perspective to guide the further case analysis. These concepts mainly address resource orchestration, capability, and performance; are derived from previous studies adopting the resource orchestration perspective [68, 77, 78]; and are particularly related to big data and BDA, as the current context focuses on using BDA for sustainability. Specifically, focal capability regarding BDA and sustainability is generated by diverse data resources and corresponding data-focused actions, which consequently influence performance to achieve data value. The entire process evolves with dynamic data resource orchestration. The identified concepts are consistent with the previous literature arguing that the resource orchestration perspective provides a useful and comprehensive view for understanding processes involving resource orchestration, capability, and ultimately, performance [28, 68].

## Research Design

The case study method is appropriate for the current study for several reasons. First, this study attempts to answer a “how” question: “How have BDA been used for air pollution management in China?” The case study method is suitable for addressing such questions [79, 80]. Second, the literature review demonstrates that there is limited understanding of how organizations can build BDA capabilities based on their captured big data to achieve their specific goals [37]. In this situation, the case study method is particularly effective for building novel insights into contexts to extend the current understanding of specific topics [81, 82]. Third, to answer the research question, this study mainly focuses on the process of utilizing BDA for sustainability, and the case study method is particularly suitable for analyzing such process-focused research [71, 83].

We selected the BDA-based air pollution management project in the BTH region in China as the case to study. There are several reasons for the case selection. First, air pollution is by far the single greatest environmental health risk, and it kills an average of 1.1 million people in China each year and costs the Chinese economy approximately US \$38 billion a year in the form of early deaths and lost food production [33]. Thus, air pollution, as one of the most significant targets for sustainability, is the research context of this study. Second, considering air pollution, the BTH region in China is among the most polluted areas in the world, and control and management are urgently required for sustainability [30]. Thus, the research result within this artifact is expected to provide practical contributions. Third, China’s government has realized the severity of pollution and the risk it poses to the sustainable development of cities, so it has invested a significant amount of money in managing air pollution in this area. To manage the air pollution problems, the researchers and practicing experts in the related fields agree that it is important to first understand the level of pollution at specific locations and where the pollution is most concentrated [84]. Big data is thus expected to provide an innovative way to address the related issues, which ties in with the research focus of this study, which is BDA. Accordingly, this case study provides both theoretical and practical contributions to specific air pollution issues and the sustainability context.

## Data collection

The air pollution management project in the BTH region aimed to gradually implement information systems based on big data and BDA in relevant cities to manage air pollution in the region. This project center introduced us to data collection for studying this entire process, specifically focusing on the use of BDA for air pollution management. Accordingly, data were collected in two major stages. First, before conducting interviews, we collected secondary data from a variety of sources, such as newspapers, magazines, books, and the Internet. We retrieved and reviewed articles and news reports related to the air pollution situation and the corresponding management strategy and actions taken by the government, especially those focused on adopting BDA in the BTH region. This first step enabled us to understand the phenomenon of utilizing BDA for sustainability (i.e., air pollution management) by providing rich background information on the case, such as in regard to existing relevant problems, the adopted technologies and information systems related to big data and BDA, actions taken, and achievements made.

Second, we collected interview data via either face-to-face interviews on site in the Hebei Province or through telephone interviews as a supplement. The informants included government officers from the relevant governmental departments (i.e., Hebei Department of Environmental Protection and the Environmental Emergency and Heavy Pollution Forewarning Center in Qinhuangdao city in Hebei), staff members from IT companies that were collaborating with the government on air pollution management (i.e., YSUSoft and LeadingSoft), and researchers from the IT Research Institution in Yanshan University, which was also collaborating with the government on air pollution management. In total, twenty indepth interviews were conducted (refer to Appendix B for the list of interviewees), with questions focused on the detailed process of using BDA for air pollution management in the BTH region from different stakeholders’ perspectives (refer to Appendix C for the list of key interview questions). Each interview was voice recorded and transcribed. During the interviews, we also took field notes, photographs, and short videos when the governmental staff members showed us how to use the air pollution management system. The transcripts, field notes, photographs, videos, and collected secondary data enabled the triangulation of data for analyzing, supporting and substantiating the findings derived from the data analysis [85].

## Data analysis

The data analysis for this study was conducted in conjunction with the data collection process to utilize flexibility, which is one of the advantages of adopting the case study method [86]. An interpretive approach was used to analyze the data under the theoretical lens of the resource orchestration perspective [87]. To simplify the investigation of the complex process of air pollution management based on BDA, the process was divided into three phases, each with a different objective: establishing air quality monitoring sites, adopting air pollution management systems, and identifying air pollutant dispersion pathways.

The interview data were coded with both open and axial coding approaches [87]. For open coding, we read through the data multiple times to create and refine the codes for the chunks of data with related information. For axial coding, we related the open codes to each other based on a combination of inductive and deductive thinking.

There were three rounds of data analysis to ensure that the collected data were well analyzed and to create insights [88]. In round 1, based on the preliminary concepts identified by adapting the resource orchestration perspective to the current context (i.e., data resources, data-focused actions, focal capability, and data value), we investigated both the transcribed interviews and the collected secondary data to code those data chunks corresponding with information related to these concepts in the three phases of air pollution management. To ensure the consistency of the coding process, we met several times to collectively review the 1st order initial codes emerging in this round [79]. In round 2, we merged the 1st order initial codes into 2nd order themes based on the theoretical lens and further refined the themes [87]. Through this process, the preliminary concepts were accordingly specified, validated, and revised and their features were ultimately generated. In round 3, we connected the identified and modified themes into a process model following a coherent logic [89], thereby creating a theoretical model based on this study. To validate and refine the model, we conducted an iterative process, shifting the focus across the data, the

## Case Description

Approximately ten years ago, the air pollution problem in China became increasingly serious and caused worldwide concern. It has been commonly assumed that the major factors contributing to air pollution are industrialization, population growth, and socioeconomic development, which are all associated with urbanization. The BTH region, which is the largest urbanized megalopolis region in Northern China, had to face the air pollution challenge together while collectively developing their economies. As one of the world’s most air-polluted regions, the “War Against Pollution” launched by the Chinese government is intensified in the BTH region.

## Phase One: Establishing air quality monitoring sites

To initiate air pollution management, the governments of the BTH region took advice from researchers and practicing experts in the field, who argue that it is critical to first capture more accurate information about the pollution level at a certain location. Doing so is expected to allow real-time air pollution monitoring to be provided to the responsible departments of local governments as well as real-time air pollution broadcasting to the public. To achieve this goal, in 2010, the governments of the BTH region took the action of establishing air quality monitoring sites in the main districts in Beijing, Tianjin municipalities and the main cities in Hebei Province. At that time, there were a total of 24 monitoring sites allocated to the region, including 9 sites in Hebei, 8 in Beijing, and 7 in Tianjin. These sites were equipped with multiple sophisticated sensors, which capture the main indicators of air pollution $( \boldsymbol { \Theta } . \boldsymbol { \mathrm { g } } . , \mathrm { \ P M } _ { 2 . 5 } , \mathrm { \ P M } _ { 1 0 } , \mathrm { \ S O } _ { 2 } , \mathrm { C O } , \mathrm { \ } 0 _ { 3 } , \mathrm { \ N O } _ { 2 } )$ in real time. The director of the Hebei Department of Environmental Protection (HDEP) further explained the motivation for establishing air quality monitoring sites in the BTH region,

“On one side, with the increasing severity of air pollution in BTH, we gradually realized that the traditional air pollution monitoring paradigm, which could only provide coarse-grained, periodical and isolated data on the air pollution situation in some places, was not suitable for the growing requirements of air pollution management anymore. On the other side, we found that the development of IoT technology and affiliated sensor equipment could offer us opportunities to transform the traditional monitoring paradigm into the more accurate, real-time, and networked one.”

Since installing and debugging the original 24 monitoring sites, outstanding performance on air pollution monitoring and broadcasting has been seen by both the BTH governments and the public. The director of HDEP described the effects of the real-time data reported by the sensors in the sites:

“Although it is very expensive to build monitoring sites, each of which costs at least two million yuan, we found it was extremely worthwhile. Before fixing these sites, we could just have a general and blurry view of the air pollution situation. The reported information was always delayed because of a lack of real-time data. This made us very passive about making responses and further decisions on pollution management. Moreover, it also decreased citizens’ satisfaction with local government from the perspective of information disclosure…

When we had these monitoring sites, the previous issues were easily addressed. With the data reported by the sites, we can better understand the air pollution situation at a certain place in real time. We knew where it was being most polluted at the time and what kinds of pollutants caused this situation… The data are important to assist in developing cost-effective policies and solutions in the future…

The real-time data also helped us to provide public information on current air quality. Through simply calculating with the data on different air pollutants, we could update the real-time air quality index (AQI) in places hourly via the official website to inform citizens to take corresponding actions when they are outdoors.”

Realizing the importance of air quality monitoring sites and considering the limited coverage range of each site, the Chinese government then massively increased its investment in the construction of the monitoring sites in BTH. To date, there are more than

200 air quality monitoring sites allocated in Hebei, approximately 50 sites in Beijing and 30 sites in Tianjin. Considering the limitation of each site’s coverage range as well as budget constraints, these sites are arranged either in the main administrative regions or in major areas that are more likely to experience pollution, as suggested by experts. The BTH region has formed a routine air quality monitoring network that provides abundant real-time big data on air pollution. The big data generated in each site in a certain district or city is reported to the local and the higher-level Department of Environmental Protection. For missing data or data exceptions due to sensor instrument failure or regional blackouts, statistical methods, such as cubic spline interpolation, were used to refine the data. The refined data were accumulated in the pollution-monitoring database to show the real-time data for each major

## Phase Two: Adopting an air pollution management system

The construction of air pollution-monitoring sites that started in 2010 to some extent fulfilled the requirement of monitoring the air pollution situation and broadcasting it to the public in real time. Having realized the great potential for big data in air pollution management, the Chinese government started to take further action. In September 2013, the State Council of the Chinese government made an announcement requiring the construction of an air pollution management system that could provide early warning of heavy air pollution events. The announcement stated that major cities in China would be required to construct their own air pollution management systems and that the evaluation of the systems would be included in the annual performance examination of local governments on aspects of environmental protection.

To meet this requirement, local governments in the BTH region started to supervise and urge cities to implement their own air pollution management systems to provide an early warning of pollution events. Taking the city of Qinhuangdao in Hebei, one of China’s most famous tourism cities, as an example, to implement such a system, a new department called the Emergency and Heavy Pollution Forewarning Center (EEHPFC) was founded by the local government. The EEHPFC is an independent department in the government that is specifically responsible for providing an early warning of heavy pollution events. As this task requires sophisticated IT knowledge and techniques, the EEHPFC decided to cooperate with YSUSoft and Leading Soft, two IT companies, for IT support. The director of the EEHPFC recalled the original requirements for the air pollution management system as discussed with YSUSoft,

“Through several occasions of preliminary discussion, we finally decided the requirements on the system to meet our needs for practical utilization and operation:

first, the system needs to provide predictive results of air quality in the city for the next few days; second, the system need to contain the function of early warning of heavy pollution events in the city; third, the system should be put into use in relatively short time, approximately six months, to meet the requirement from the upper government.”

With an overall consideration of the requirements and considering suggestions from experts in the field of air pollution management, the EEHPFC in cooperation with the IT companies decided to adopt a mature air pollution management system using the community multiscale air quality (CMAQ) model as its core. The CMAQ system is a thirdgeneration air quality modeling system that was designed by the U.S. Environmental Protection Agency. The source code of the system is highly transparent and is available online at http://www.cmaq-model.org. Accordingly, air pollution management systems based on the CMAQ model have been widely adopted to forecast air quality, based on which the government can make corresponding decisions. The project manager from YSUSoft explained the choice of the CMAQ system:

“We, together with EEHPFC, only had six months to implement an air pollution management system, and we had limited financial investment and human resources, which is unrealistic to develop a new system from zero. Through consultation with the experts, we found that the CMAQ system could satisfy all the requirements for forecasting air quality and forewarning heavy pollution. Furthermore, it has been maturely applied, for example, in America, and it is easy to get from the online source. Thus, our task could be simplified from developing a system to preparing data as

Following the operation manual of the CMAQ system, the EEHPFC needed to gather all the required data. In addition to real-time air quality data reported by the 15 air quality monitoring sites in the city of Qinhuangdao, other data, such as meteorological data (e.g., air temperature, wind direction, wind speed, and humidity) and pollution source data (e.g., the pollutant emission inventory of the pollution source), were also needed. To collect these data, the EEHPFC coordinated with other departments of the local city government, such as the Meteorological Bureau and Environmental Protection Department, to receive relevant data in a timely manner. With the IT support from the cooperating IT companies, the gathered data were further preprocessed by refining and restructuring them to meet the required input format. By integrating the data from various sources into the air pollution management system for processing, the prediction results could be presented as the outputs.

Through a short pilot of the system, the EEHPFC found that the predictive accuracy of the system was less than 60%. Discussing this issue with the IT companies, the EEHPFC realized that even with the ready-developed system, they still needed to adjust the relevant parameters of the system. One staff member from EEHPFC explained is as follows:

“After pilot operation, we had to adjust the system by correspondingly changing some parameters before it could be formally used. This is because different cities may have different topography, pollutant sources or weather conditions and thus, corresponding adjustment should be conducted to ensure the accuracy and effectiveness of system prediction.”

To adjust the system, the EEHPFC first gathered the accumulated big data on air quality and other corresponding data for previous years because the monitoring sites were set as the historical database. With the help of the IT companies, the prediction results generated by the system based on historical data were continuously compared with the actual monitoring data on air quality at a specific time. The relevant parameters were adjusted iteratively to decrease the differences between the prediction results and the realtime monitoring data. Ultimately, the predictive accuracy of the system was increased to up to 70%, and the system was put into use to predict air quality and provide an early warning of heavy pollution events. Since the implementation of the system, the EEHPFC has continued to adjust parameters at regular intervals to continuously improve the forecast accuracy.

![](/api/attachments/KDRHY7GQ/fulltext/images/9559bddcfd2504c495adfec6ce7d0478c7e7e71a16e3369a7228edeb6240bde4.jpg)

![](/api/attachments/KDRHY7GQ/fulltext/images/621a09cd4af791a21282084853fb7995ec55425ce5ef18d3ebf9d1436004f562.jpg)  
Figure 2. User Interface for the Air Pollution Management System

Source: EEHPFC of Qinhuangdao

The user interface for the air pollution management system is shown in Figure 2, which presents the prediction results in both a map format to provide an overall view of the city in terms of air pollution forecasting and a graph format to show the pollution trends at specific locations to provide forewarning of heavy pollution. The system provides scientific results for forecasting air quality that satisfy the government requirement by providing an understanding of real-time monitoring results and allowing users to master the development trend of air quality and air pollution. It also offers key technical and data support for decision making to maintain the prevention and control of air pollution, and it provides warning information and timely suggestions for emergency measures in heavy air pollution.

## Phase Three: Identifying air pollutant dispersion pathways

The establishment of air quality monitoring sites enabled real-time monitoring, while the adoption of an air pollution management system allowed air quality prediction and heavy pollution early warning. Through the process of implementing these tasks, an ocean of relevant data was accumulated and stored in the database. The collected data already fulfilled the original responsibility to either monitor or predict, but the governments of the BTH region started to consider reusing these data to generate new and actionable insights based on BDA to further improve air pollution management in the BTH region. In September 2015, the HDEP launched a cooperative project with practicing air pollution experts and IS researchers from Yanshan University to explore valuable insights from BDA to enhance air pollution management. The main objective of this project is to identify the pathways of air pollutant dispersion. The director of HDEP described the initiation of this project:

“The idea of using BDA for identifying the pollutant dispersion pathways was derived from the process when we implemented the province-level air pollution management system, as required by the upper government. At that time, we realized that the quality of data on air pollution was also very significant for predictive accuracy. As there is a coverage limitation for the monitoring sites, higher data quality requires a more representative siting of the air quality monitors, which can cover the majority of key sites prone to pollution…

Due to the consideration of saving cost and increasing efficiency, we found it was essential to understand the pollutant dispersion pathways to optimize the regional monitoring network and forecast air quality more accurately… For united air pollution management among Beijing, Tianjin, and Hebei, we also wanted to figure out how the air pollution of a certain city influences the adjacent cities. The air pollutant dispersion pathways were expected to help us understand this question, which would assist us in distinguishing the respective responsibility of the cities and help the related cities take measures in advance of coming heavy air pollution.”

To achieve this goal, the HDEP, working together with air pollution management experts and IS researchers, first determined the regular law of pollutant dispersion and the corresponding data involved. In addition to the data that had already been collected as the input of the air pollution management system, they found that other data, such as socioeconomic data (e.g., population density and traffic flow rate) and terrain data, could also influence pollution dispersion. The HDEP then coordinated with the Statistics Bureau to obtain the data. After supplementing the big data pool, the data were cleaned and preprocessed with the relevant imputation techniques, such as cubic spline interpolation.

Next, abductive computer reasoning with machine learning was utilized to develop the data model for this project. Through several discussions between the HDEP, the practicing experts and the IS researchers, a complex network model was determined for data modeling by comparing all the possible models with the existing dispersion law. The complex network model was considered suitable for modeling pollutant dispersion because it could clarify patterns of connections between network nodes that are neither purely random nor purely regular. As one of the IS researchers on this project at Yanshan University explained,

“The complex network model is capable of simulating the interactions among the components for air pollutant dispersion. In the model, the nodes are mapped as certain locations and edges represent the flow of air pollutants from original location to others in a region.”

Complex network theories helped to guide how data were modeled. The data modeling was an iterative process that adapted complex network theories to pollutant dispersion through constant comparison of data with data and of data with complex network theories to progressively develop a proper data model. Meanwhile, the corresponding machine learning algorithm was developed by the IS researchers, as detailed in Liu et al. [90]. By utilizing machine learning, a series of data-driven clustering explorations were conducted to develop the initial set of pathways, which was then iteratively refined by constantly adapting the set to fit the data. Finally, the set of pathways of air pollutant dispersion was created (see Figure 3, for example).

![](/api/attachments/KDRHY7GQ/fulltext/images/4b5ed30e957dd25194d3d33eb5c0b0557209d623cc8dd42bf78ef85e450c3350.jpg)  
Figure 3. Pathways of Air Pollutant Dispersion Identified using Machine Learning

The set of identified dispersion pathways was reported to the governments of the BTH region as a foundation for advising the future construction of new air quality monitoring sites. Furthermore, it helped the governments trace pollution’s origins and distinguish the responsibility for air pollution management for each city, which could enhance united management across the BTH region.

## Case Analysis

The above case description illustrates the process of developing BDA capability for sustainability in the setting of air pollution management, as shown in Figure 4. The resource orchestration perspective was adopted as the theoretical lens for case analysis. On the basis of the case description, the case was analyzed across three phases: setting air quality monitoring sites (Phase 1), adopting an air pollution management system (Phase 2), and identifying air pollutant dispersion pathways (Phase 3).

In general, the development of BDA capability is the result of big data resource orchestration, but different BDA capabilities require different orchestration methods. In addition, BDA capability can be further classified into two different levels, and concrete-level BDA capability leads to the abstract-level BDA capability. Furthermore, applying BDA in a specific context (i.e., sustainability) enables the BDA capability to be transformed into the corresponding contextual capability to achieve sustainable goals. Finally, with the accumulation of BDA capability, the value of big data is progressively excavated.

![](/api/attachments/KDRHY7GQ/fulltext/images/b5784960d97061bdbf2ae499547d6adaf7d02ac544d5792c948dfb234060a057.jpg)  
Figure 4. The process model of BDA capability development in air pollution management

## Developing BDA capability through big data resource orchestration

The case analysis reveals that BDA capability as the focal capability in each phase of the case was developed by orchestrating the focal resource—big data resource. Unlike the conventional view of resource orchestration, which considers all the possible focal resources and all the corresponding capabilities [28], we narrow down the scope of analysis to keep it specific to big data because the current research focus is on BDA for sustainability. Thus, we propose that this orchestration occurs when governments purposefully orchestrate large data resources, which leads to the generation of corresponding BDA capability. Taking a longitudinal view across the three phases, we find that to create different BDA capabilities, different data resources, different data-focused actions, and different data-specific investments are required. Additionally, the study reveals that there are two different levels of BDA capability developed based on big data resource orchestration. Concrete BDA capability is directly associated with data resource-focused actions. In other words, concrete BDA capability refers to the ability of the activities to orchestrate big data resources. Abstract BDA capability is derived from a combination of concrete BDA capabilities, which generalizes the capability created through big data analytics. Furthermore, through this analysis process, we specifically reveal that different data-specific investments focus on different roles for big data in different phases, thereby influencing the development of different BDA capabilities.

In Phase 1, the requirement of air pollution management at the primary stage is to more precisely understand the pollution level. Thus, the focal abstract BDA capability is the ability to describe the situation of pollution accurately and in a timely manner. To achieve this, big data can describe the situation where necessary. Air quality monitoring sites with advanced sensors and Internet of things (IoT) technology were set in designated locations to capture such data. It is notable that for some monitoring sites, missing data or data exceptions occurred due to sensor instrument failure or regional blackout, which could influence the accuracy of big data. As argued by the resource orchestration research, resource-focused actions realize the value of a resource [28]. Thus, the descriptive capability was developed through data resource-focused actions, which were collecting the sensor data in each site and cleaning the collected data so that it could ultimately show real-time air quality in a specific location. To conduct such actions, the corresponding concrete BDA capability, which is the ability to collect data and the ability to clean data, must be developed. At this stage, the major data-specific investment is in the data infrastructure, which functions as the source of the big data.

In Phase 2, when the governments met the requirement of knowing what is happening in terms of air pollution, they next wanted to predict what would happen in the future with the help of BDA. This is a significant development of the focal abstract BDA capability—predictive capability—which is expected to enable governments to prepare a relevant response to air pollution in advance. To generate the predictive capability, an existing air pollution management system was adopted; thus, as the input, the single source of sensor data was insufficient. To achieve predictive capability, the pool of big data was enriched by integrating other sources of data, such as meteorological data and pollutant source data, with the sensor data. All the data were used as inputs to the air pollution management system. With the existing adapted system, the governments in cooperation with IT companies did not need to understand the inner mechanisms for predicting air quality. Instead, they only needed to process the data with the help of the system. Therefore, at this stage, the main data resource-focused actions to develop predictive capability are integrating multiple sources of data and processing the data using an information system. Accordingly, to undertake these resource-focused actions, the corresponding concrete BDA capabilities—the ability to integrate data and the ability to process data—were required. In the stage, which focused on processing the data to generate prediction results, the data system was the major data-specific investment. This is different from the role of the data system investment plays a role as a “black box” machine to process the data.

In Phase 3, the governments wanted to further unearth the value of the already-inuse data. They wanted to identify the pathways of pollutant dispersion so that they could improve the siting of the air quality monitors and make united decisions on air pollution management. To achieve this prescriptive capability, the existing sources of data were orchestrated in a different way so that the “black box” of pollutant dispersion was opened. Cooperating with both the IS researchers and air pollution management experts, the governments tried to determine the dispersion mechanisms, utilizing machine learning with complex network modeling to identify the pathways of air pollutant dispersion. In this process, the multiple data resources were coordinated to identify the law of air pollutant dispersion, and the data were deployed with machine learning to identify the dispersion pathways, which finally developed the focal abstract BDA capability—the prescriptive capability. To accomplish resource-focused actions, the corresponding concrete BDA capability, which is the capability of coordinating data and the capability of reusing data, was required. Additionally, in this stage, the main data-specific investment was to adopt machine learning methods, which played a role as a tool to interact with big data to generate data value.

Synthesizing the process of developing BDA capability in the three phases, different types of abstract BDA capabilities are identified (i.e., descriptive, predictive, and prescriptive capabilities) for sustainability. The current study finds that to develop such BDA capabilities, the focal resources are different types of data resources, such as sensor data, meteorological data, pollutant source data, and so on in the specific context of air pollution management. It further reveals that to achieve the goal of developing the three BDA capabilities, there are two data-focused concerns that need to be well considered: data quality and activities involved in the data lifecycle.

First, regarding the use of BDA for air pollution management, data resources are to be extracted to describe the air quality, processed through the information system to predict high pollution levels, and analyzed with machine learning to prescribe solutions for pollution management. Accordingly, the quality of the data is essential for the entire process of data orchestration involved in developing BDA capability. Among the diverse dimensions of data quality [91], the accuracy, timeliness, accessibility, completeness, relevance, and costeffectiveness of the data are the central concern, and corresponding investments and efforts were made in this case to achieve these quality measures. In Phase 1, investments were made in data infrastructure (i.e., advanced sensors and IoT technology) to obtain data that could report accurate air quality information in real time. In Phase 2, to input the required data into the adapted information system, cooperation among governmental departments was promoted to ensure that the data were accessible and complete before being imported, which further influenced the success of the system in delivering the predictive results. In Phase 3, machine learning was utilized to identify the pathways of pollutant dispersion, and thus, the relevance of the data for the dispersion mechanisms was mainly discussed. The analysis results, in turn, were used to guide the construction of monitoring sites, aiming to collect more accurate data at a relatively lower cost.

Second, based on Sirmon et al. [28]’s research on the resource orchestration perspective, three major actions were proposed to orchestrate diverse resources (i.e., structuring, bundling, leveraging), which have been applied as a theoretical framework to analyze the relevant processes [77, 78]. Narrowing down the analysis scope to big data resource orchestration, the current study proposes that the major actions taken to orchestrate big data resources for developing BDA capability can involve the entire data lifecycle, from data creation to data reuse. For the current context of air pollution management, the specific data-focused actions in the data lifecycle were identified within three phases; these are collecting, cleaning, integrating, processing, coordinating, and reusing data. In Phase ${ \mathrm { } } ^ { 1 , }$ to develop the descriptive BDA capability, sensor data were collected and cleaned in order to accurately describe real-time air quality. In Phase 2, to develop the predictive BDA capability, various types of data were integrated and then processed through the information system to predict the air pollution level based on the output results. In Phase 3, to develop the prescriptive BDA capability, multiple data were coordinated to identify the pollution mechanisms and consequently deployed with machine learning to further prescribe solutions for air pollution management. This finding links the literature on the data lifecycle and resource orchestration to provide a framework for data resource orchestration that identifies the possible data-focused actions through which BDA capability is correspondingly developed.

## Transforming BDA capability into sustainability capability

The case analysis reveals that by applying BDA in the context of sustainability, there is a capability transformation chain in each phase. In general, concrete BDA capability, which is associated with data resource orchestration, can be further transformed into abstract BDA capability and finally into the situational sustainability capability by being combined with the specific context. The three different types of capability are also hierarchical in that only when the development of the former capability is fulfilled can the latter capability be created.

In Phase 1 of establishing the air quality monitoring sites, the concrete BDA capabilities are collecting data and cleaning data. By setting the monitoring sites and obtaining the concrete BDA capabilities, the data on pollutant indicators at the sites are collected and cleaned. With big data on air quality, the government consequently gained descriptive capability, which is the abstract BDA capability to describe real-time air quality. When the BDA capability was applied to the sustainability context, it was transformed into the reactive capability of the government to offer a timely response to a pollution event as it occurs because it knows the real-time situation.

In Phase 2, which is adopting an air pollution management system, the concrete BDA capabilities are integrating data and processing data. With these concrete BDA capabilities, governments could integrate multiple sources of data into the adapted system for processing to produce the output, which is the air quality forecast. Thus, this process enables the government to obtain the capability to predict air quality and offer early warning of heavy pollution events. With early warning about heavy air pollution, governments can then have sufficient time to consult and make relevant decisions to prevent losses due to the coming pollution events. Thus, in this regard, the government has accordingly developed a preventive capability by applying the predictive BDA capability to the sustainability context.

In Phase 3 of identifying air pollutant dispersion pathways, the concrete BDA capability is the ability to coordinate data and the ability to reuse data. By utilizing machine learning, governments have successfully transformed the concrete BDA capabilities into a prescriptive capability by identifying the pathways of air pollutant dispersion. With the identified pathways, governments can make decisions to improve the siting of air quality monitoring equipment. Thus, when the prescriptive BDA capability was applied to the sustainability context, the governments obtained the proactive capability to assist in addressing the problem rather than only reacting to it.

The identified capability transformation chain also explicates the essential role of BDA in sustainability by arguing that BDA capability can be progressively transformed into sustainability capability within the specific context. As a result, three major sustainability capabilities are built based on the transformation: reactive, preventive, and proactive capabilities. To develop these capabilities, the abstract BDA capabilities (i.e., descriptive, predictive, and prescriptive capabilities) need to be created by developing corresponding concrete BDA capabilities. In other words, when governments have the specific BDA capability, their understanding, predicting, and decision making related to sustainable issues changes from the original expert-driven approach, which was mainly based on some sustainability experts’ experience and opinions, to a data-driven approach, which is derived from a great amount of accurate and real-time data and their analysis results. Thus, the change enables governments to react to the issues in a timely manner, prevent emergencies and loss caused by the issues, and take proactive actions to address the issues.

The finding on the capability transformation also reveals that whether and to what extent BDA can have a major impact is highly dependent on the context, rooted in the contextualized goals, and achieved through the process of transforming BDA capability into the domain-specific capability. For the current study, the context is air pollution management, which is particularly in the domain of sustainability. Thus, the entire process of utilizing BDA capability needs to be matched with the context of sustainability: the selection of big data types, the corresponding data-focused actions, the development of BDA capability, and the interpretation and discussion of BDA results need to all consider sustainability. Accordingly, the study further states that cooperation between the BDA researchers/practitioners and the experts in the specific sustainability domain is necessary when using BDA for sustainability.

## Realizing big data value progressively while accumulating BDA capability

Through data analysis, it is found that big data value can be progressively excavated by accumulating BDA capabilities. In this case, sensor data were collected for real-time monitoring of air quality. When the collected data achieved this original goal, they were accumulated into a database including historical data. It appears that these historical data represent “data exhaust,” referring to data that do not have an attached direct value [92]. This is consistent with one of the specific characteristics of big data, which is its “low value density,” as researchers have argued that the data received in their original form are always of low value compared to their enormous volume [16]. The low value density of big data also means that discussion of how to make full use of big data to create more data value attracts high attention from both practitioners and researchers [23]. For this case, the study finds that as governments developed and accumulated their BDA capability, the value of the data was gradually unearthed.

In Phase 1, the governments obtained the concrete BDA capability of collecting data and cleaning data and thus gained the abstract descriptive capability. In this process, the basic data value of the collected sensor data was generated, which is the data presenting value to achieve the goal of monitoring air quality in real time. As discussed above, at the end of this phase, the original goal of the sensor data was accomplished.

In Phase 2, the governments then obtained the concrete BDA capability of integrating multiple sources of data and processing data with an information system. They consequently obtained predictive capability and could predict data change trends. Through this capability accumulation process, the governments exploited another way to unearth the value of already-collected sensor data by integrating them with other sources of data and inputting all the data into an information system for output offering air pollution predictive results, thus creating the data processing value from its early warning ability.

At the beginning of Phase 3, the real-time sensor data were being used in two different ways to create different data values. The data had overfulfilled their mission and were being accumulated in the database as historical data, which became data exhaust. In this phase, the governments then developed the concrete BDA capability of coordinating multiple sources of data and reusing data to yield new insights with machine learning. The concrete capability empowered the governments to gain the prescriptive capability of identifying the inner mechanisms and corresponding solutions based on the results generated from the machine learning process. During this process, governments accumulated diverse and powerful BDA capabilities, which enabled the already-used data exhaust to produce novel insights that enable the generation of data analyzing value to optimize air pollution management.

Synthesizing data value creation across the three phases shows that in the process of applying BDA to sustainability, which in this case is air pollution management, the value of big data is progressively created. As the BDA capability of the government accumulates, the created data value was upgraded from “presenting value” to “processing value” and, ultimately, to “analyzing value”. The “presenting value” is delivered by providing the real-time monitoring of air quality information on the sites; the “processing value” is delivered by the outputs from the information system, which are used as the basis of an early warning system for high pollution levels; the “analyzing value” is delivered through the identification of air pollutant dispersion pathways, using machine learning to guide future construction of monitoring sites and trace pollution’s origins for air pollution management optimization.

The findings also show that there are several actionable ways to unearth data value, which involve various data investments in infrastructure, systems, and analytic techniques. In the current study, IoT technology and advanced sensors help directly obtain accurate and real-time sensor data on air quality and the original “presenting value” of the data from the single source (i.e., sensor data) can be generated. Then, by integrating the sensor data with other sources of data, the data set is used as an input to the information system for processing, which allows further exploration of the “processing value”. Subsequently, after coordinating the accumulated sensor data with additional relevant data from multiple sources, machine learning is used to further analyze them to deeply excavate the “analyzing value” of the big data.

## Discussion

## Theoretical and practical contributions

This study investigates the case of air pollution management based on BDA and reveals both the relationship between big data resource orchestration and BDA capability and the interaction between BDA capability and sustainability capability. Focusing on using BDA for sustainability, two levels of BDA capability are identified, abstract BDA capability being developed through concrete BDA capability. When BDA capability is applied to a specific context, sustainability in this case, it is transformed into the corresponding sustainability capability to achieve sustainable goals. Furthermore, as the BDA capability accumulates, the data value is progressively unearthed. This study makes both theoretical and practical contributions.

First, this study is an early attempt to understand BDA for sustainability using the theoretical lens of the resource orchestration perspective. Pursuant to the call by Baert et al. [93] for application of the resource orchestration perspective to contexts other than business, this study contributes by extending this perspective to the sustainability context and studying the process of BDA capability development. Previous studies adopted the resource orchestration perspective by considering all possible types of resources and resourcefocused actions to investigate organizational performance [28, 68]. However, the current study proposes an innovative and more focused view based on using the resource orchestration theory to understand the process of air pollution management, focusing on the relationship between big data resource orchestration, BDA capability, and data value creation. The study finds that to unearth different types of data value, different BDA capabilities need to be developed, for which different sources of data must be orchestrated in different ways and, accordingly, different data-specific investments are required. Thus, the study extends and specifies the resource orchestration perspective to provide a data-specific view on investigating sustainability issues that utilize BDA to uncover the key solution.

Second, this study responds to the call for an empirical study to discover “how to develop” BDA capability [37], contributing to BDA studies by utilizing the case study method to investigate the process of developing BDA capability for air pollution management. First and foremost, to successfully manage air pollution, it is essential to have BDA capability. It has been agreed that there are different levels of capability [70]. This study extends this argument by identifying two hierarchical levels of BDA capability. Concrete BDA capability is associated with the activities in data lifecycle. Abstract BDA capability is developed based on the acquisition of concrete BDA capability, which is more closely related to using BDA to solve practical issues. The theoretical lens of resource orchestration shows that BDA capability is developed through big data resource orchestration, which requires different sources of data, different actions to orchestrate data, and different data-specific investments. Accordingly, the study suggests two major concerns for developing focused BDA capability, which are data quality and the data lifecycle.

Third, this study further contributes to the sustainability literature by highlighting the role of BDA in achieving sustainable goals. It finds that BDA capability can be transformed into sustainability capability (i.e., reactive, preventive, and proactive capabilities) when it is applied to the sustainability context. This study to some extent illustrates how BDA works to solve sustainability issues by supporting the relationship between BDA capability and performance for sustainability, which extends the view of this context. It emphasizes that BDA is contextualized and has a major impact only when all the BDA activities are conducted under consideration of a specific sustainability domain, such as air pollution management. Thus, the study further suggests that cooperation between BDA researchers/practitioners and sustainability experts is necessary for the successful use of BDA for sustainability.

Fourth, in line with the call for understanding how to effectively create big data value [23], this study contributes to both the BDA research and sustainability studies by revealing that big data value for sustainability is progressively created along with the process of accumulating BDA capabilities. The finding agrees with the previous argument that big data itself can produce little value and that its value is generated through processing and analyzing the data [40]. This study further highlights the critical role of developing BDA capability to excavate big data value and accordingly suggests some actionable ways to further unearth data value in the context of sustainability.

Last, this study also makes important practical contributions, especially for achieving sustainable goals (air pollution management in this case). It illustrates the process of developing BDA capability in the setting of air pollution management. The description and analysis of the case in the BTH region provide a practical reference that governments can use to develop BDA capability for solving similar pollution issues or other sustainability problems. By highlighting the importance of big data-specific resources and the corresponding actions, this study has attempted to enlighten city managers in governments by showing that maximizing the ultimate value of big data for sustainability is not simply making investments and collecting hordes of data. City managers need to cooperate with both BDA experts and sustainability experts to identify which potential sustainability capabilities to develop and the value of types of data in achieving the specific sustainability goals, which can guide management. Furthermore, management needs to focus on developing corresponding BDA capability to deeply unearth big data value so that it can assist with decision making and solutions for sustainability. By referring to the findings of this study, governments can select sources of data (e.g., sensor data, meteorological data, and pollutant source data), conduct data-focused actions (e.g., collecting, cleaning, integrating, processing, coordinating, and reusing data), make data-specific investments (e.g., investments in data infrastructure, data systems, and data analytics) based on their realities and the BDA capability they need to develop, to achieve specific sustainability goals.

## Conclusion

This study is motivated by the high influx of interest in BDA for sustainability among both practitioners and academics. As BDA is still a relatively novel concept, there is a call for a greater and deeper understanding of this topic within different contexts [94, 95]. The majority of the extant big data literature discusses the great potential of BDA in both business and society without clearly illustrating the process of developing BDA capability or how it works for sustainability. This study conducted a case study of air pollution management based on BDA adopting the resource orchestration perspective and proposed a process model to illustrate the process of developing BDA for sustainability. This study provides theoretical and practical insights into using BDA for achieving sustainable goals and thus makes valuable contributions to both researchers and practitioners in the field.

In terms of future research direction, further study is still required to add to the existing knowledge. There is a need to extend the current research artifact of air pollution management to other sustainability issues to understand the process of developing BDA capability for sustainability. For instance, using BDA for intelligent agriculture may lead to novel concerns and new insights into developing BDA capability as different data-specific investments and different sources of data may be needed to address this specific issue. Future investigations of cases achieving different SDGs could develop more new paths for BDA capability development, which are expected to contribute both theoretically and practically.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China [grant numbers 61672448, 71529001, 71632003] and the Fundamental Research Funds for the Central Universities [grant number 63192112].

## Appendix A. United Nations’ SDGs and Roles of Big Data

![](/api/attachments/KDRHY7GQ/fulltext/images/ea9ee6e18e63b0fa4ee14c06870fd2bcddd73a82b6b6f607daff2ccbaa185bea.jpg)

How data science and analytics can contribute to sustainable development

![](/api/attachments/KDRHY7GQ/fulltext/images/44fe5a4f794b204f3d955f563f352db5f4742e9eef1cc0913633df46e8cde13f.jpg)

@UNGlobalPulse 2017

## 0 NO POVERTY

Spending patterns on mobile phone services can provide proxy indicators of income levels

## ②

Crowdsourcing or tracking of food prices listed online can help monitor food security in near real-time

## 3 GOOD HEALTH AND WELL-BEING

Mapping the movement of mobile phone users can help predict the spread of infectious diseases

## 4 QUALITY EDUCATION

Citizen reporting can reveal reasons for student drop-out rates

## ⑤ GENDER EQUALITY

Analysis of financial transactions can reveal the spending patterns and different impacts of economic shocks on men and women

## CLEAN WATER AND SANITATION

Sensors connected to water pumps can track access to clean water

##

Smart metering allows utility companies to increase or restrict the flow of electricity, gas or water to reduce waste and ensure adequate supply at peak periods

## 8 DECENT WORK AND ECONOMIC GROWTH

Patterns in global postal traffic can provide indicators such as economic growth remittances, trade and GDP

## 9 INDUSTRY INNOVATION AND INFRASTRUCTURE

Data from GPS devices can be used for traffic control and to improve public transport

## ① REDUCED INEQUALITY

Speech-to-text analytics on local radio content can reveal discriminatior concerns and support policy response

##

Satellite remote sensing can track encroachment on public land or spaces such as parks and forests

## 12 RESPONSIBLE CONSUMPTION AND PRODUCTION

Online search patterns ol e-commerce transactions can reveal the pace of transition to energy efficient products

## 13 CLIMATE ACTION

Combining satellite imagery crowd-sourced witness accounts and open data can help track deforestation

## 14 LIFE BELOW WATER

Maritime vessel tracking data can reveal illegal unregulated and unreported fishing activities

## 15 LIFE ON LAND

Social media monitoring can support disaster management with real-time information on victim location effects and strength of forest fires or haze

## 16 PEACE, JUSTICE AND STRONG INSTITUTIONS

Sentiment analysis of social media can revea public opinion on effective governance, public service delivery or human rights

## 17 PARTNERSHIPS FOR THE GOALS

Partnerships to enable the combining of statistics mobile and internet data can provide a better and realtime understanding of today's hyper-connected worlc

Source: United Nations [96]

Appendix B. List of Interviewees

<table><tr><td>Organization</td><td>Organization Introduction</td><td>Role</td><td>Number</td></tr><tr><td rowspan="3">Hebei Department of Environmental Protection (HDEP)</td><td rowspan="3">HDEP is the department in the government of Hebei Province in China that is specifically responsible for addressing issues of environmental protection. The mission of HDEP is “to improve environmental quality and build a beautiful place that enjoys blue sky, green land, and clean water.” For air pollution management in the BTH region, HDEP is mainly responsible for establishing air quality monitoring sites in Hebei, supervising the establishment and improvement of air pollution management systems in each city, taking measures and making decisions on air pollution issues, and coordinating with the cities of Beijing and Tianjin for united pollution management.</td><td>Director of HDEP</td><td>1</td></tr><tr><td>Staff members of HDEP</td><td>2</td></tr><tr><td colspan="2"></td></tr><tr><td rowspan="3">Qinhuangdao Environment Emergency and Heavy Pollution Forewarning Center (QEEHPFC)</td><td rowspan="3">The QEEHPFC is an independent center in the city government of Qinhuangdao in Hebei, which was established specifically for implementation and daily operation of the air pollution management system in Qinhuangdao. Based on the results from the system, the QEEHPFC is also responsible for reporting air quality predictions and early warnings of heavy pollution to the upper departments in the city government, as well as publishing these results for the public.</td><td>Director of QEEHPFC</td><td>1</td></tr><tr><td>Staff member of QEEHPFC</td><td>4</td></tr><tr><td colspan="2"></td></tr><tr><td rowspan="3">YSUSoft</td><td rowspan="3">YSUSoft is an IT company that provided IT services and support to the QEEHPFC for the implementation of the air pollution management system. It was mainly responsible for the installation and testing of the system and the preparation of the input data.</td><td>General manager of YSUSoft</td><td>1</td></tr><tr><td>Project manager of YSUSoft</td><td>1</td></tr><tr><td>Staff member of YSUSoft</td><td>3</td></tr><tr><td rowspan="2">LeadingSoft</td><td rowspan="2">LeadingSoft is an IT company that provided IT services and support to the QEEHPFC for the implementation of the air pollution management system. It was</td><td>Project manager of LeadingSoft</td><td>1</td></tr><tr><td>Staff member ofLeadingSoft</td><td>1</td></tr><tr><td rowspan="2"></td><td rowspan="2">mainly responsible for adjusting the system parameters and improving the system to increase its predictive accuracy.</td><td></td><td></td></tr><tr><td colspan="2"></td></tr><tr><td rowspan="3">IT/IS Research Institution in Yanshan University</td><td rowspan="3">This institution includes researchers in the field of information technology and information systems from Yanshan University in Hebei. It cooperated with HDEP on the project to identify the pathways of air pollutant dispersion in the BTH region.</td><td>Director of the institution</td><td>1</td></tr><tr><td>Team leader of the research project</td><td>1</td></tr><tr><td>Team member of the research project</td><td>3</td></tr></table>

Appendix C. List of Key Interview Questions

<table><tr><td>Organization</td><td>Role</td><td>Key questions</td></tr><tr><td rowspan="3">Hebei Department of Environmental Protection (HDEP)</td><td>Director of HDEP</td><td rowspan="3">- Why did the government begin its initiative in air pollution management in the BTH region?- What is the department's role and responsibilities in air pollution management?- Why did the HDEP decide to use big data and BDA for air pollution management?- What actions related to BDA have been undertaken for air pollution management?- What kinds of big data have been involved in each action? How did the department obtain them and manage the use of them? How did the department analyze them and how did the department make decisions based on the analysis results?- Have the actions related to BDA changed the department's ways of reacting to or making decisions on air pollution issues? If so, how?- Until now, what has the air pollution management based on BDA achieved?- What challenges related to using BDA for air pollution management were encountered and what was done to address them?- What was the department's motivation for launching the project to identify pollutant dispersion pathways based on BDA?- How did the department conduct the project?- How did the department cooperate with other organizations for the project?- What problems were encountered in the project and what was done to address them?- What has the project achieved in the aspects of air pollution management?</td></tr><tr><td>Staff member of HDEP</td></tr><tr><td></td></tr><tr><td>Qinhuangdao</td><td>Director of</td><td>- What is the center's role and responsibilities in</td></tr><tr><td rowspan="3">EnvironmentEmergency and HeavyPollution ForewarningCenter (QEEHPFC)</td><td>QEEHPFC</td><td rowspan="3">air pollution management?- What was the motivation for implementing the air pollution management system?- What were your requirements for the system?- How did the center implement the system?- How did the center cooperate with other departments in the government and other organizations, such as the IT companies?- What kind of data were required for the system? How did the center collect the data and process them?- What are the main functions of the system?What are the results produced from the system?How does the center use the system for daily work?- What problems were encountered in the process of implementing and operating the system and what was done to address them?</td></tr><tr><td>Staff memberof QEEHPFC</td></tr><tr><td></td></tr><tr><td rowspan="3">YSUSoft</td><td>Generalmanager ofYSUSoft</td><td rowspan="5">- What is the company's role and responsibilities in the project of implementing the air pollution management system?- How did the company cooperate with QEEHPFC?- What data-related technologies/systems were involved in the project?- What has been done by the company in the project?- What results/benefits have been produced by the system? How did they assist in air pollution management?- What difficulties/problems were encountered during the project and what was done to address them?</td></tr><tr><td>Projectmanager ofYSUSoft</td></tr><tr><td>Staff memberof YSUSoft</td></tr><tr><td rowspan="2">LeadingSoft</td><td>Projectmanager ofLeadingSoft</td></tr><tr><td>Staff memberof LeadingSoft</td></tr><tr><td rowspan="3">IT/IS ResearchInstitution in YanshanUniversity</td><td>Director of theinstitution</td><td rowspan="3">- What was the motivation for launching the project of identifying pollutant dispersion pathways based on BDA and cooperating with the HDEP?- What is the institution's role and responsibilities in the project?- How did the university cooperate with HDEP?- What data and BDA technologies were involved in the project? What has been done for the project?- What difficulties/problems were encountered during the project and what was done to address them?- What has the project achieved in the aspect of air pollution management? What was the feedback and evaluation of the project from the government?</td></tr><tr><td>Team leader ofthe researchproject</td></tr><tr><td>Team memberof the researchproject</td></tr></table>

## References

1. Albino, V., Berardi, U., and Dangelico, R.M., Smart cities: Definitions, dimensions, performance, and initiatives. Journal of Urban Technology, 2015. 22(1): p. 3-21.

2. Batty, M., Axhausen, K.W., Giannotti, F., Pozdnoukhov, A., Bazzani, A., Wachowicz, M., Ouzounis, G., and Portugali, Y., Smart cities of the future. The European Physical Journal Special Topics, 2012. 214(1): p. 481-518.

3. Gil-Garcia, J.R., Pardo, T.A., and Nam, T., What makes a city smart? Identifying core components and proposing an integrative and comprehensive conceptualization. Information Polity, 2015. 20(1): p. 61-87.

4. Chan, J., Mojumder, P., and Ghose, A., The digital Sin City: An empirical study of Craigslist's impact on prostitution trends. Information Systems Research, 2018. 30(1): p. 219-238.

5. Wang, L., Zhang, F., Pilot, E., Yu, J., Nie, C., Holdaway, J., Yang, L., Li, Y., Wang, W., and Vardoulakis, S., Taking action on air pollution control in the Beijing-Tianjin-Hebei (BTH) region: Progress, challenges and opportunities. International Journal of Environmental Research and Public Health, 2018. 15(2): p. 306.

6. Bibri, S.E., A foundational framework for smart sustainable city development: Theoretical, disciplinary, and discursive dimensions and their synergies. Sustainable Cities and Society, 2018. 38: p. 758-794.

7. Fabrizio, F., Dror, E., and Joel, G., Tackling grand challenges pragmatically: Robust action revisited. Organization Studies, 2015. 36(3): p. 363-390.

8. Hashem, I.A.T., Chang, V., Anuar, N.B., Adewole, K., Yaqoob, I., Gani, A., Ahmed, E., and Chiroma, H., The role of big data in smart city. International Journal of Information Management, 2016. 36(5): p. 748-758.

9. Guo, Y., Zhu, Y., Barnes, S.J., Bao, Y., Li, X., and Le‐Nguyen, K., Understanding cross product purchase intention in an IT brand extension context. Psychology & Marketing, 2018. 35(6): p. 392-411.

10. Jimenez, C.E., Solanas, A., and Falcone, F., E-government interoperability: Linking open and smart government. Computer, 2014. 47(10): p. 22-24.

11. Angelidou, M., Psaltoglou, A., Komninos, N., Kakderi, C., Tsarchopoulos, P., and Panori, A., Enhancing sustainable urban development through smart city applications. Journal of Science and Technology Policy Management, 2018. 9(2): p. 146-169.

12. Nilsson, M., Griggs, D., and Visbeck, M., Policy: Map the interactions between Sustainable Development Goals. Nature News, 2016. 534(7607): p. 320.

13. Gupta, A., Deokar, A., Iyer, L., Sharda, R., and Schrader, D., Big Data & Analytics for societal impact: Recent research and trends. Information Systems Frontiers, 2018. 20(2): p. 185-194.

14. Chen, H., Chiang, R.H., and Storey, V.C., Business intelligence and analytics: From big data to big impact. MIS Quarterly, 2012. 36(4): p. 1165-1188.

15. Chen, M., Mao, S., Zhang, Y., and Leung, V.C., Big data: Related technologies, challenges and future prospects. 2014, Cham: Springer International Publishing.

16. Gandomi, A. and Haider, M., Beyond the hype: Big data concepts, methods, and analytics. International Journal of Information Management, 2015. 35(2): p. 137-144.

17. Jagadish, H., Gehrke, J., Labrinidis, A., Papakonstantinou, Y., Patel, J.M., Ramakrishnan, R., and Shahabi, C., Big data and its technical challenges. Communications of the ACM, 2014. 57(7): p. 86-94.

18. Kim, G.-H., Trimi, S., and Chung, J.-H., Big-data applications in the government sector. Communications of the ACM, 2014. 57(3): p. 78-85.

19. Barbierato, E., Gribaudo, M., and Iacono, M., Performance evaluation of NoSQL bigdata applications using multi-formalism models. Future Generation Computer Systems, 2014. 37: p. 345-353.

20. Barnaghi, P., Sheth, A., and Henson, C., From data to actionable knowledge: Big data challenges in the Web of Things. IEEE Intelligent Systems, 2014. 28(6): p. 6-11.

21. Lafuente, G., The big data security challenge. Network Security, 2015. 2015(1): p. 12-14.

22. Sandhu, R. and Sood, S.K., Scheduling of big data applications on distributed cloud based on QoS parameters. Cluster Computing, 2015. 18(2): p. 817-828.

23. Grover, V., Chiang, R.H.L., Liang, T.P., and Zhang, D., Creating strategic business value from Big Data Analytics: A research framework. Journal of Management Information Systems, 2018. 35(2): p. 388-423.

24. Heudecker, N. and Hare, J., Survey analysis: Big data investments begin tapering in 2016. 2016, Gartner Report.

25. Ross, J.W., Beath, C.M., and Quaadgras, A., You may not need big data after all. Harvard Business Review, 2013. 91(12): p. 90.

26. LaValle, S., Lesser, E., Shockley, R., Hopkins, M.S., and Kruschwitz, N., Big data, analytics and the path from insights to value. MIT Sloan Management Review, 2011. 52(2): p. 21.

27. Kwon, O., Lee, N., and Shin, B., Data quality management, data usage experience and acquisition intention of big data analytics. International Journal of Information Management, 2014. 34(3): p. 387-394.

28. Sirmon, D.G., Hitt, M.A., Ireland, R.D., and Gilbert, B.A., Resource orchestration to create competitive advantage: Breadth, depth, and life cycle effects. Journal of Management, 2011. 37(5): p. 1390-1412.

29. Watson, H.J., Tutorial: Big data analytics: Concepts, technologies, and applications. Communications of the Association for Information Systems, 2014. 34: p. Article 65.

30. Hansen, M.H. and Ahlers, A.L., Air pollution: how will China win its self-declared war against it?, in Routledge Handbook of Environmental Policy in China, E. Sternfeld, Editor. 2017, Routledge: Oxon. p. 107-120.

31. Kampa, M. and Castanas, E., Human health effects of air pollution. Environmental Pollution, 2008. 151(2): p. 362-367.

32. Mannucci, P.M., Harari, S., Martinelli, I., and Franchini, M., Effects on health of air pollution: a narrative review. Internal and Emergency Medicine, 2015. 10(6): p. 657- 662.

33. Kao, E., Air pollution is killing 1 million people and costing Chinese economy 267 billion yuan a year, research from CUHK shows, in South China Morning Post 2018.

34. Guo, Y., Barnes, S.J., and Jia, Q., Mining meaning from online ratings and reviews: Tourist satisfaction analysis using latent dirichlet allocation. Tourism Management, 2017. 59: p. 467-483.

35. Watson, H.J. and Marjanovic, O., Big data: The fourth data management generation. Business Intelligence Journal, 2013. 18(3): p. 4-8.

36. Wixom, B., Ariyachandra, T., Douglas, D.E., Goul, M., Gupta, B., Iyer, L.S., Kulkarni, U.R., Mooney, J.G., Phillips-Wren, G.E., and Turetken, O., The current state of business intelligence in academia: The arrival of big data. Communications of the Association for Information Systems, 2014. 34: p. Article 1.

37. Gupta, M. and George, J.F., Toward the development of a big data analytics capability. Information & Management, 2016. 53(8): p. 1049-1064.

38. Russom, P., Big data analytics. TDWI Best Practices Report, Fourth Quarter, 2011. 19(4): p. 1-34.

39. De Mauro, A., Greco, M., and Grimaldi, M., A formal definition of Big Data based on its essential features. Library Review, 2016. 65(3): p. 122-135.

40. Foster, J., McLeod, J., Nolin, J., and Greifeneder, E., Data work in context: Value, risks, and governance. Journal of the Association for Information Science and Technology, 2018. 69(12): p. 1414-1427.

41. Sivarajah, U., Kamal, M.M., Irani, Z., and Weerakkody, V., Critical analysis of Big Data challenges and analytical methods. Journal of Business Research, 2017. 70: p. 263-286.

42. Miah, S.J., Vu, H.Q., Gammack, J., and McGrath, M., A big data analytics method for tourist behaviour analysis. Information & Management, 2017. 54(6): p. 771-785.

43. Mills, S., Lucas, S., Irakliotis, L., Rappa, M., Carlson, T., and Perlowitz, B., Demystifying big data: a practical guide to transforming the business of government. 2012, TechAmerica Foundation: Washington.

44. Wu, X., Zhu, X., Wu, G.-Q., and Ding, W., Data mining with big data. IEEE Transactions on Knowledge and Data Engineering, 2014. 26(1): p. 97-107.

45. Tim Y, Hallikainen P, Pan S, and T, T., Actualizing Business Analytics for Organizational Transformation: A Case Study of Rovio Entertainment. European Journal of Operational Research (forthcoming), 2019.

46. Wang, G., Gunasekaran, A., Ngai, E.W., and Papadopoulos, T., Big data analytics in logistics and supply chain management: Certain investigations for research and applications. International Journal of Production Economics, 2016. 176: p. 98-110.

47. Ransbotham, S., Kiron, D., and Prentice, P.K., Minding the analytics gap. MIT Sloan Management Review, 2015. 56(3): p. 63.

48. Marr, B., Big Data: Using SMART big data, analytics and metrics to make better decisions and improve performance. 2015, New Jersey: John Wiley & Sons.

49. Kuhlman, T. and Farrington, J., What is sustainability? Sustainability, 2010. 2(11): p. 3436-3448.

50. Nam, T. and Pardo, T.A. Smart city as urban innovation: Focusing on management, policy, and context. in Proceedings of the 5th international conference on theory and practice of electronic governance. 2011. ACM.

51. Marceau, J., Introduction: Innovation in the city and innovative cities. Innovation: Management, Policy & Practice, 2008. 10(2-3): p. 136-145.

52. Miles, A., Zaslavsky, A., and Browne, C., IoT-based decision support system for monitoring and mitigating atmospheric pollution in smart cities. Journal of Decision Systems, 2018. 27(sup1): p. 56-67.

53. Chan, J., Ghose, A., and Seamans, R., The Internet and racial hate crime: Offline spillovers from online access. MIS Quarterly, 2016. 40(2): p. 381-403.

54. George, G., Howard-Grenville, J., Joshi, A., and Tihanyi, L., Understanding and tackling societal grand challenges through management research. Academy of Management Journal, 2016. 59(6): p. 1880.

55. Nations, U. The Sustainable Development Agenda. 2015 [cited 2019 12 Jan]; Available from: https://www.un.org/sustainabledevelopment/development-agenda/.

56. Leach, M., Rockström, J., Raskin, P., Scoones, I.C., Stirling, A.C., Smith, A., Thompson, J., Millstone, E., Ely, A., and Arond, E., Transforming innovation for sustainability. Ecology and Society, 2012. 17(2): p. 11.

57. Malhotra, C., Anand, R., and Singh, S., Applying Big Data Analytics in Governance to Achieve Sustainable Development Goals (SDGs) in India, in Data Science Landscape, V.N. Munshi U., Editor. 2018, Springer: Singapore. p. 273-291.

58. Tien, J.M., Big data: Unleashing information. Journal of Systems Science and Systems Engineering, 2013. 22(2): p. 127-151.

59. Beck, E.J., Gill, W., and De Lay, P.R., Protecting the confidentiality and security of personal health information in low-and middle-income countries in the era of SDGs and Big Data. Global Health Action, 2016. 9(1): p. 32089.

60. Rathore, M.M., Paul, A., Ahmad, A., and Jeon, G., IoT-based big data: From smart city towards next generation super city planning. International Journal on Semantic Web and Information Systems, 2017. 13(1): p. 28-47.

61. Rahman, M.N., Esmailpour, A., and Zhao, J., Machine learning with big data an efficient electricity generation forecasting system. Big Data Research, 2016. 5: p. 9- 15.

62. Chatterjee, S., Byun, J., Dutta, K., Pedersen, R.U., Pottathil, A., and Xie, H., Designing an Internet-of-Things (IoT) and sensor-based in-home monitoring system for assisting diabetes patients: iterative learning from two case studies. European Journal of Information Systems, 2018. 27(6): p. 670-685.

63. Weerasinghe, K., Pauleen, D., Scahill, S., and Taskin, N., Development of a theoretical framework to investigate alignment of Big Data in healthcare through a

social representation lens. Australasian Journal of Information Systems, 2018. 22: p. 1-23.

64. Palmatier, R.W., Dant, R.P., and Grewal, D., A comparative longitudinal analysis of theoretical perspectives of interorganizational relationship performance. Journal of Marketing, 2007. 71(4): p. 172-194.

65. Barney, J.B., Resource-based theories of competitive advantage: A ten-year retrospective on the resource-based view. Journal of Management, 2001. 27(6): p. 643-650.

66. Helfat, C.E. and Peteraf, M.A., The dynamic resource based view: Capability lifecycles. Strategic Management Journal, 2003. 24(10): p. 997-1010.

67. Lin, Y. and Wu, L.-Y., Exploring the role of dynamic capabilities in firm performance under the resource-based view framework. Journal of Business Research, 2014. 67(3): p. 407-413.

68. Chan, C.M., Hackney, R., Pan, S.L., and Chou, T.-C., Managing e-Government system implementation: a resource enactment perspective. European Journal of Information Systems, 2011. 20(5): p. 529-541.

69. Tan, B.C., Pan, S.L., and Hackney, R., The strategic implications of web technologies: A process model of how web technologies enhance organizational performance. IEEE Transactions on Engineering Management, 2010. 57(2): p. 181- 197.

70. Helfat, C.E., Finkelstein, S., Mitchell, W., Peteraf, M., Singh, H., Teece, D., and Winter, S.G., Dynamic capabilities: Understanding strategic change in organizations. 2009, New Jersey: John Wiley & Sons.

71. Pan, S., Pan, G., and Hsieh, M.H., A dual level analysis of the capability development process: A case study of TT&T. Journal of the American Society for Information Science and Technology, 2006. 57(13): p. 1814-1829.

72. Pan, S.L., Pan, G., Chen, A.J., and Hsieh, M.H., The dynamics of implementing and managing modularity of organizational routines during capability development: Insights from a process model. IEEE Transactions on Engineering Management, 2007. 54(4): p. 800-813.

73. Huang, P.-Y., Pan, S.L., and Ouyang, T.H., Developing information processing capability for operational agility: implications from a Chinese manufacturer. European Journal of Information Systems, 2014. 23(4): p. 462-480.

74. Ndofor, H.A., Sirmon, D.G., and He, X., Firm resources, competitive actions and performance: investigating a mediated model with evidence from the in vitro diagnostics industry. Strategic Management Journal, 2011. 32(6): p. 640-657.

75. Wang, N., Liang, H., Zhong, W., Xue, Y., and Xiao, J., Resource structuring or capability building? An empirical study of the business value of information technology. Journal of Management Information Systems, 2012. 29(2): p. 325-367.

76. Teece, D.J., The foundations of enterprise performance: Dynamic and ordinary capabilities in an (economic) theory of firms. Academy of Management Perspectives, 2014. 28(4): p. 328-352.

77. Cui, M. and Pan, S.L., Developing focal capabilities for e-commerce adoption: A resource orchestration perspective. Information & Management, 2015. 52(2): p. 200- 209.

78. Cui, M., Pan, S.L., Newell, S., and Cui, L., Strategy, resource orchestration and ecommerce enabled social innovation in Rural China. The Journal of Strategic Information Systems, 2017. 26(1): p. 3-21.

79. Pan, S.L. and Tan, B., Demystifying case research: A structured–pragmatic– situational (SPS) approach to conducting case studies. Information and Organization, 2011. 21(3): p. 161-176.

80. Walsham, G., Interpretive case studies in IS research: nature and method. European Journal of Information Systems, 1995. 4(2): p. 74-81.

81. Eisenhardt, K.M., Building theories from case study research. Academy of Management Review, 1989. 14(4): p. 532-550.

82. Chen, J.E., Pan, S.L., and Ouyang, T.H., Routine reconfiguration in traditional companies’e-commerce strategy implementation: A trajectory perspective. Information & Management, 2014. 51(2): p. 270-282.

83. Gummesson, E., Qualitative methods in management research. 2000, California: Sage.

84. Aunan, K., Hansen, M.H., and Wang, S., Introduction: air pollution in China. The China Quarterly, 2018. 234: p. 279-298.

85. Klein, H.K. and Myers, M.D., A set of principles for conducting and evaluating interpretive field studies in information systems. MIS Quarterly, 1999. 23: p. 67-93.

86. Eisenhardt, K.M. and Graebner, M.E., Theory building from cases: Opportunities and challenges. Academy of Management Journal, 2007. 50(1): p. 25-32.

87. Corbin, J., Strauss, A., and Strauss, A.L., Basics of qualitative research. 2014, California: Sage.

88. Andriopoulos, C. and Lewis, M.W., Exploitation-exploration tensions and organizational ambidexterity: Managing paradoxes of innovation. Organization Science, 2009. 20(4): p. 696-717.

89. Montealegre, R., A process model of capability development: Lessons from the electronic commerce strategy at Bolsa de Valores de Guayaquil. Organization Science, 2002. 13(5): p. 514-531.

90. Liu, W., Kang, X., Yu, J., Wang, X., Song, W., Wei, Y., and Zhang, L., An approach to find critical transport paths of air pollutant based on complex netwok. ICIC Express Letters. Part B, Applications: An International Journal of Research and Surveys, 2017. 8(2): p. 387-394.

91. Wang, R.Y. and Strong, D.M., Beyond accuracy: What data quality means to data consumers. Journal of Management Information Systems, 1996. 12(4): p. 5-33.

92. George, G., Haas, M.R., and Pentland, A., Big data and management: From the Editors. Academy of Management Journal, 2014. 57(2): p. 321-326.

93. Baert, C., Meuleman, M., Debruyne, M., and Wright, M., Portfolio entrepreneurship and resource orchestration. Strategic Entrepreneurship Journal, 2016. 10(4): p. 346- 370.

94. Markus, L.M., New games, new rules, new scoreboards: the potential consequences of big data. Journal of Information Technology, 2015. 30(1): p. 58-59.

95. Zhao, J.L., Fan, S., and Hu, D., Business challenges and research directions of management analytics in the big data era. Journal of Management Analytics, 2014. 1(3): p. 169-174.

96. Nations, U. Big Data for Sustainable Development. 2018 [cited 2019 12 Jan]; Available from: http://www.un.org/en/sections/issues-depth/big-data-sustainabledevelopment.

## Author Biography

Dan Zhang is a lecturer in the Department of Information Resources Management, Business School, Nankai University, China. Her research interests are emerging digital enablement phenomena in businesses and societies. She has conducted in-depth case studies on stateowned enterprises, commercial organizations, and non-profit organizations in China. She received her Bachelor in E-Commerce from Tianjin University in China, her Master in Management Science and Engineering from Nankai University in China, and her Ph.D. in Information Systems and Technology Management from the University of New South Wales (UNSW) in Australia.

Professor Shan L Pan is an AGSM scholar and a professor of Information Systems and Technology Management at the UNSW Business School. He is the founder and leader of the Digital Enablement Research Network (DERN) at UNSW Business School, a research group focused on transformational effects of technologies and consumerization effects of technologies. He is currently affiliated with the Alexander von Humboldt Institute for Internet and Society, Germany. He is also an advisor to Alibaba Research Institute, China. His research interest is digital enablement in business and social innovation. Professor Pan has conducted in-depth studies on state-owned enterprises, commercial organizations, rural villages, and non-profit organizations in China, Germany, Finland, India, and Southeast Asia. He has published widely in top journals such as MIS Quarterly, Information Systems Research, Journal of the AIS, Information Systems Journal, European Journal of Information Systems, Journal of Strategic Information Systems, Journal of Information Technology, Journal of the Academy of Marketing Science, Journal of the Association for Information Science and Technology, European Journal of Operational Research, IEEE Transactions on Engineering Management, Communications of ACM, and among others.

Jiaxin Yu is a lecturer at the School of Information Science and Engineering of Yanshan University. His research interests include artificial intelligence, data mining, and machine learning, with particular emphasis on deep learning in the field of natural language processing.

Wenyuan Liu<sup>\*</sup> is a Professor and serves as the doctoral supervisor of the School of Information Science and Engineering of Yanshan University. He also serves as the Chairman of Hebei District of ACM. His research interests include intelligent information processing for large data, Internet of Things perception and mobile computing, electronic commerce and business intelligence. He has presided over three National Natural Science Foundations and published dozens of papers indexed by EI or SCI in international journals and conferences.
