---
otero_id: 20957
otero_key: "BNZZYY89"
title: "Management policies and the diffusion of data warehouse: a case study using system dynamics-based decision support system"
authors: "Mohammed Quaddus; Arunee Intrapairot"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00133-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Management policies and the diffusion of data warehouse: a case study using system dynamics-based decision support system

Mohammed Quaddus <sup>a,)</sup>, Arunee Intrapairot <sup>b</sup>

a Graduate School of Business, Curtin UniÕersity of Technology, GPO Box U 1987, Perth, WA 6845, Australia b Rajamangala Institute of Technology, Northern Campus, Huay Kaew Road, Chiang Mai 50300, Thailand

## Abstract

This paper studies the impact of management policies on the diffusion of data warehouse DW in a large commercialŽ . bank in Thailand. A system dynamics SD -based decision support system DSS is developed and analysed for this purpose.Ž . Ž . System dynamics was used as the modelling tool because of its rigorous approach in capturing interrelationships among variables and in handling dynamic aspects of the system behaviour. A qualitative model is first formulated to understand the present state of the DW diffusion. The quantitative model is then formulated to simulate seven management policies. Findings unearth two dominant policies of ‘increase level of training’ and ‘decrease training delay’ that will speed up the diffusion significantly. None of the policies, however, achieve the bank’s target diffusion level within a specified time period. Sensitivity analyses reveal various combinations of the dominant policies that the management can adopt. The analyses act as an eye-opener for the bank executives as they understand what can be feasibly achieved given a number of constraints. With easy interfaces and supportive tools, bank executives can use the DSS to test various scenarios, which will enhance their learning process and improve their decision making. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Data warehouse; System dynamics; Banking; Case study

## 1. Introduction

Intense competition in the global market impels executives in organisations to make swift and appropriate decisions. Since good decisions need accurate and timely information, many organisations are inclined to invest in data warehousing technology in order to use information to support decision-making processes. The usage of data warehouses DWs is Ž . growing significantly, especially in the fields of financial services. Worldwide expenditure on DWs has climbed from \$3.5 billion in 1997 to an expected \$5.4 billion in 1999 39 .<sup>w</sup> <sup>x</sup>

A DW is a central source of data that is extracted, standardised and integrated from various operational and management databases of an organisation 38 . It<sup>w</sup> <sup>x</sup> typically provides clean information reconciling dif-Ž ferences in semantics, transaction dates, currencies, etc. of sufficient breadth integrating data from sev- . Ž eral sources and depth consolidating data to higher . Ž levels while still supporting queries down to the detailed level 54 . Given these properties, success- . <sup>w</sup> <sup>x</sup> ful DWs provide accurate and timely information, support more effective decision making, help organisations avoid costs before they occur, capitalise on previously unrecognised business opportunities, and provide mass customisation of products and services to fit customers’ requirements 7,8,25,28 .<sup>w</sup> <sup>x</sup>

Despite the above, the current potential benefits from DWs are still considered low, intangible and inconclusive, and projects take longer than expected. Consultants and vendors estimate optimistically that a DW can furnish the investment within 6 months to 3 years, with paybacks ranging from 100% to 700%. However, actual investors, particularly banks, rarely confirm benefits from investment 40 . Furthermore, <sup>w</sup> <sup>x</sup> quite a few DW projects end in failure even before full implementation owing to lack of immediate substantial economic returns on massive investment <sup>w</sup> <sup>x</sup> 24,25,67 .

A careful analysis of the above problems reveals that a DW, like any other technology, requires in-depth planning and ultimately large scale diffusion to all potential users. It must be emphasised that benefits from a DW come, in fact, from the intensity of its usage. That is, the benefits cannot be obtained from the mere provision of the actual physical technology. Therefore, once a DW is adopted, enterprise-wide diffusion is a must. Appropriate policies are therefore needed to achieve sustained enterprise-wide diffusion of a DW.

## 1.1. Research objectiÕes and questions

The primary research objectives of this paper are twofold: i to develop a system dynamics SD -based Ž . Ž . decision support system DSS to study the diffusionŽ . process of data warehousing technology, and ii to Ž . calibrate the DSS and apply it to study the impact of management policies on the diffusion of DW in a large commercial bank in Thailand. Thus, the following two research questions guide our research.

Ž .i What is a requisite model of diffusion of a DW for the bank?

Ž . ii What are the impacts of management policies on the diffusion of DW in the bank?

The paper is organised as follows. Section 2 presents the brief background information on the adoption<sup>r</sup>diffusion process of information technologies IT in general and banking technologies inŽ . particular, and on SD-based modelling of IT adoption<sup>r</sup>diffusion. Section 3 introduces the banking case with current information on the perception of the users towards technology usage. The qualitative diffusion model is developed in Section 4, while the transformation to quantitative model is presented in Section 5. Section 6 shows how the DSS is used for strategic policy analysis. Section 7 presents implications of the policy analyses for management of the bank. Conclusions are presented in Section 8.

## 2. Background

2.1. Adoption and diffusion of information technologies

Adoption is the process of selecting an innovation Ž . technology, idea, process, etc. for organizational use 32,50 . The need for adoption may come from<sup>w</sup> <sup>x</sup> internal or external forces. Internally, the organization may feel a need for a technology, and externally various agents vendors, etc. may persuade the orga- Ž . nization to adopt a technology. On the other hand, diffusion is the process during which an innovation is communicated among members of a social system via certain channels over time. According to Rogers <sup>w</sup> <sup>x</sup> 50 a diffusion process consists of four main elements: an innovation, communication channels, time and a social system. It has been observed that diffusion of technology over time can be modelled by a logistic or S-shaped curve. The literature suggests that new technology is not adopted all at once. Some early adopters adopt new technology. If they are successful a bandwagon effect takes place and the potential adopters then imitate 33,50 . However,<sup>w</sup> <sup>x</sup> there is much variation in the slope of the S-shape curve. If the technology diffuses relatively rapidly, the S-shaped curve becomes quite steep. On the other hand, some technology may have a slower rate of diffusion resulting in a relatively flat S-shaped curve 50 .<sup>w</sup> <sup>x</sup>

Information and communications technology Ž . ICT , at present, is the main technology acquired in most countries, with more than 50% of the acquired technology adopted via imports from developed countries 41 . ICT adoption, in many cases, pro- <sup>w</sup> <sup>x</sup> vides the organization a competitive advantage. ICT that impacts on organisations are individual work support, group work support, advanced organisational automation, and enhanced global communications 64 .<sup>w</sup> <sup>x</sup>

The efficacy of technology and its advantages depend more on proper management of technology rather than the physical technology itself. Technology adoption and diffusion should therefore focus on managerial<sup>r</sup>organisational processes, social contexts, and adapt to local cultures, markets and the circumstances 6,23 . Furthermore, an organisation <sup>w</sup> <sup>x</sup> should find ways to incorporate business needs, match technology with the knowledge workers, and take all the actions that may help the organisation to exploit the benefits of the technology 10,13 . <sup>w</sup> <sup>x</sup>

Various studies suggest ways to ensure the success of technology adoption. for example, Geisler <sup>w</sup> <sup>x</sup> 22 identified seven criteria for IT adoption including the capabilities of technology, consistencies between technologies and organisational requirements, user acceptance, extendibility, compatibility, and life cycle of technology. For small and medium enterprises, factors such as business size and executive characteristics are critical for the success of technology adoption. The preferred characteristics of chief executives are innovative orientation, positive attitude toward technology adoption, and sufficient IT knowledge 70 . Fink and Kazakoff 18 suggest that<sup>w x</sup> <sup>w x</sup> the staff of an organisation need to: 1 assess ITŽ . benefits, organisational culture and compatibility between IT and organisation environment; 2 deter-Ž . mine availability and sufficiency of resources and appropriate procedures for the successful selection and implementation; and 3 evaluate external envi-Ž . ronment, support and resources, to decide if outsourcing is needed. Furthermore, in a competitive environment, an organisation should have a strategic management of technology that promotes an ability to understand technological status and trends, focus on process technologies rather than product technologies, and enhance an ability to accurately assess new technology 44 . <sup>w</sup> <sup>x</sup>

In spite of spending massive resources on technology adoption and implementation, rejection of technology commonly occurs because organisations fail to deal with technological problems. Many factors obstruct the rapid rate of the technology diffusion process. Literature suggests a number of obstacles for technology adoption and diffusion which include: high costs of technologies, rapid obsolescence, selecting inappropriate technologies, under-utilisation, unproductive usage, low acceptance from customers<sup>r</sup>staff, lack of capable employees, lack of high executive support, unexpected performance from an adopted technology, technological mismatch, and technological difficulty 4,11,14,17,21,22,57,58 ,<sup>w</sup> <sup>x</sup> among many others.

## 2.2. Adoption and diffusion of banking technologies

Financial institutes gain their reputation not only from their robust financial status but also from adoption of new technologies. For example, the reputation of Wells Fargo Bank was enhanced from the early adoption of the Internet and Mondex’s electronic cash product. The First Union was well known for developing an Internet strategy 61 . Banking<sup>w</sup> <sup>x</sup> technologies contribute great benefits not only to banks themselves but also to their customers e.g., Ž convenience, security, improvements, better access to information and an alternative to cash 62 .<sup>w</sup> <sup>x</sup>.

Banking technologies had been introduced since 1980 in the form of electronic banking and home banking services 16 . In fact, banks are being forced<sup>w</sup> <sup>x</sup> to adopt new technologies and make technological changes for many reasons. First, older technologies cannot be extended. Second, new technologies provide more lucrative opportunities. Third, old technologies cannot keep up with business growth rates or fulfill organisational needs 26 . Consequently, the<sup>w</sup> <sup>x</sup> banking industry is prompt to integrate various kinds of banking technologies with their business performance. Prendergast and Marr 43 reveal the greatest<sup>w</sup> <sup>x</sup> potential of bank technologies i.e., ATMs, EFTPOS,Ž telephone banking and credit cards and predicted. that human tellers in transaction-based services would be replaced by self-service technologies. Their finding is consistent with that of Smith 60 who sug- <sup>w</sup> <sup>x</sup> gests that ATMs and EFTPOS would dominate up until 1995. Roth and Van Der Velde 51 report that<sup>w</sup> <sup>x</sup> self-service technology such as ATMs conduct the vast majority of routine transactions in the USA;

however, smart cards are not perceived as being a major force in technology within the near future.

Exploratory research regarding banking technology adoption and diffusion has been conducted mostly using surveys, interviews and Delphi techniques. Arthur Anderson and Co. 2 interviews<sup>w</sup> <sup>x</sup> banking executives and technology suppliers in Australia to identify the shape of banking technologies in the 1990s. Prendergast 42 surveys the use of three<sup>w</sup> <sup>x</sup> key self-service technologies i.e., Automatic Teller Ž Machines—ATM, Electronic Fund Transfer at Point of Sale—EFTPOS and telephone banking in New. Zealand to identify stages of adoption of these technologies and recommends strategies to enhance the rate of diffusion. Prendergast and Marr 43 , using a <sup>w</sup> <sup>x</sup> Delphi study, indicate that the adoption of all technologies will increase, but the level of adoption will be different for each. Those with the greatest potential are ATMs, EFTPOS, telephone banking and credit cards. Their findings are consistent with those of Roth and Van Der Velde 51 .<sup>w</sup> <sup>x</sup>

Sayeed and Brightman 55 , investigating the use <sup>w</sup> <sup>x</sup> and effectiveness of computerised information and communications to support within the banking industry, reveal the following facts. First, branch managers frequently use computerised information and communications to support their activities. Second, technologies are used for resolving both strategic and operational problems. Third, IT applications enhance managerial intelligence by promoting planning, learning from experience and quick information access from a large number of sources. However, when compared to non-computerised support, computerised information or communications support does not produce more accurate problem finding.

While literature on DW is plentiful Refs. Ž <sup>w</sup> <sup>x</sup> 9,24,26 , among many others , a formal study on the. adoption and<sup>r</sup>or diffusion of DW in an organizational context is not available. Clearly, the success in technology diffusion of a DW, similar to other information technologies, relies on a fabric of many factors, not only technical but also organisational. Furthermore, its diffusion process is contingent upon the technology life cycle stages and related variables such as the economic life of the technology and time delays e.g., training, perceived satisfaction . There- Ž . fore, the SD model 12,72 is proposed as an appro- <sup>w</sup> <sup>x</sup> priate decision-making tool to develop the diffusion model of a DW, because it is capable of handling interrelationships among variables and their dynamic aspects.

## 2.3. System dynamics and IT diffusion

SD, initially developed by Jay Forrester 19 , is a<sup>w</sup> <sup>x</sup> method for qualitative description and analysis of complex systems and quantitative simulation of system behaviour. The SD model and its methodology put emphasis on conceptualisation, formulation and simulation 47 . It is divided into two stages, qualita-<sup>w</sup> <sup>x</sup> tive and quantitative analysis. In the first stage, modellers identify system variables for the problem in concern and develop a qualitative system model in the form of a causal loop diagram CLD . In theŽ . second stage, the qualitative model is transformed into a system flow diagram and is calibrated for quantitative analysis using simulation techniques <sup>w</sup> <sup>x</sup> 72,73 . Over the years, SD has been applied in many diverse areas from software development, strategic planning to project management 15,37,49,<sup>w</sup> 52 .<sup>x</sup>

Application of SD in innovation diffusion area had been patchy. One of the early applications of SD modelling in innovation diffusion was by Sharif and Kabir 59 . The authors developed a comprehensive <sup>w</sup> <sup>x</sup> model of multi-level technological substitution. However, their approach can be effectively used for any technology diffusion application. Maier 34 de-<sup>w</sup> <sup>x</sup> veloped a SD-based diffusion model using the Bass 5 model as the basis. The author extended his model to study the substitution among successive product generations. Milling 36 applied SD ap- <sup>w</sup> <sup>x</sup> proach to develop an innovation diffusion model using the possible communications between potential customers and adopters as the basis.

Other related applications include the work of Anderson and Jogleker 1 who developed a model<sup>w</sup> <sup>x</sup> of the evolution of technological performance using SD-based simulation approach. Kim and Juhn 29 <sup>w</sup> <sup>x</sup> developed a SD model for investigating the behaviour of network growth and decay.

It must be emphasized that we took a ‘group model building’ approach to develop the SD-based diffusion model 71 . The actual process followed <sup>w</sup> <sup>x</sup> Wolstenholme’s 72 stepwise approach of finding <sup>w</sup> <sup>x</sup> the Aprimary actorsB of the adoption and diffusion process and their actions on various Aresource flowsB. Details of this approach are available elsewhere <sup>w</sup> <sup>x</sup> 72,73 . We also took the view of SD model as a tool for learning in line with the views of Coyle 12 ,<sup>w</sup> <sup>x</sup> Morecroft 37 and Senge 56 among many others.<sup>w x</sup> <sup>w x</sup>

## 3. Adoption of banking technologies—the case of Siam Commercial Bank

The banking industry in Thailand consists of four types of banking systems: a central bank, commercial banks, savings banks and banks for specific purposes. The commercial banks are under the supervision of the Bank of Thailand BOT . Our case, TheŽ . Siam Commercial Bank SCB , is one of the fourŽ . largest banks in Thailand. The Bank was recognized as one of the best banks in Asia by Asia Money Magazine in 1996. The bank has a main office in Bangkok and 416 branches nationwide and 7 overseas.

Electronic banking began in Thailand when the SCB installed a magnetic accounting recorder machine for withdrawal–deposit service in 1965. Later in the 1970s, Bangkok Bank and the SCB began to service customers with deposit and withdrawal facilities at all branches. ATM transaction service was initially installed by the SCB in 1983, which was the starting point for the banks to use electronic banking systems in order to provide new services to their customers. Bangkok Bank and the SCB provided EFTPOS at the same time in 1985 63 . The Thai<sup>w</sup> <sup>x</sup> Farmer Bank issued a ‘smart card’, a combination of ATM and ‘electronic purse’ card. In 1993, the bank initially adopted a program to ‘re-engineer’ bank operations to improve customer service and operational efficiency 65 .<sup>w</sup> <sup>x</sup>

Table 1  
Evolution of banking technology adoption at the SCB. Source: The Siam Commercial Bank PCL publications

<table><tr><td>Technologies</td><td>Adoption year</td></tr><tr><td>ATM</td><td>1983</td></tr><tr><td>Tele-banking</td><td>1984</td></tr><tr><td>EFTPOS</td><td>1985</td></tr><tr><td>Info-Banking (to facilitate information flows between banks and customers)</td><td>1986</td></tr><tr><td>GIS</td><td>1989</td></tr><tr><td>BETAS (to serve small- and medium-sized customers)</td><td>1995</td></tr><tr><td>Video conferencing, Intranet, and SCB cash management</td><td>1996</td></tr><tr><td>Data Warehouse, New network and IT infrastructure</td><td>1997</td></tr></table>

Table 2  
Inhibiting factors of technology use at SCB

<table><tr><td>Factors</td><td>Main office (%)</td><td>Branch offices (%)</td><td>Total (%)</td></tr><tr><td>Insufficient training</td><td>75.86</td><td>76.37</td><td>75.52</td></tr><tr><td>Lack of understanding of new technology</td><td>51.23</td><td>62.09</td><td>55.93</td></tr><tr><td>Limitation of time in learning new technology because of routine work</td><td>53.69</td><td>58.24</td><td>55.41</td></tr><tr><td>Insufficient support from IT people</td><td>34.98</td><td>35.16</td><td>34.79</td></tr><tr><td>Technology changes too fast</td><td>27.09</td><td>27.47</td><td>27.06</td></tr><tr><td>Technology does not suit requirements</td><td>13.30</td><td>13.74</td><td>13.40</td></tr></table>

In order to adopt technology the SCB has established a unit called Applied Technology Office Ž . ATO . ATO is responsible for the research and development including adoption of innovative tech-Ž . nologies in financial business. The unit follows both external ‘push’ and internal ‘pull’ approaches of technology adoption 45 . Table 1 shows the evolu-<sup>w</sup> <sup>x</sup> tion of technology adoption at SCB over the last two decades.

It is observed that the SCB has adopted requisite banking technologies at regular intervals. However, despite spending millions of dollars in technologies the bank is not free from its technology-related problems. To understand the factors that inhibit the use of technologies, a survey was conducted among the users at the main and branch offices of SCB. Table 2 presents the findings. It is observed that ‘insufficient training’ is perceived to be the top most inhibiting factor to technology use. It is closely followed by ‘lack of understanding’ and ‘limitation of time to learning’.

We conducted another survey to find the perceived factors that would promote the use of banking technologies. Table 3 presents the findings. It is observed that ‘training’ is the topmost perceived factor to promote the use of technology. Other important factors are ‘technological assistance’, ‘user friendliness’, etc.

Data collection  
Table 3  
Supportive factors to promote technology use at SCB

<table><tr><td>Supportive factors</td><td>Main office (%)</td><td>Branch offices (%)</td><td>Total (%)</td></tr><tr><td>Training from the bank</td><td>82.76</td><td>87.91</td><td>84.54</td></tr><tr><td>Support from high executive managers</td><td>51.72</td><td>58.79</td><td>54.64</td></tr><tr><td>Involvement with IT people when the bank brings new technologies to use</td><td>58.13</td><td>56.59</td><td>56.96</td></tr><tr><td>Technological assistance from IT people when problems occur</td><td>70.44</td><td>59.89</td><td>64.95</td></tr><tr><td>User friendly technologies</td><td>65.02</td><td>57.14</td><td>60.82</td></tr><tr><td>Provide additional benefits as an incentive in learning and using technology</td><td>12.32</td><td>18.68</td><td>15.21</td></tr></table>

It is interesting to note that in both surveys there is a very close correlation between the responses of main and branch offices.

The two surveys acted as the basis of further study of the diffusion of DW at SCB. The SCB has committed huge investment in the infrastructure of DW. Given the perception of the users the next obvious question is ‘how can one make the data warehouse a success?’ To achieve this goal, policies were needed to be specified for sustained diffusion of DW.

## 3.1. Primary data collection

The study employed various methods of data collection including observations, interviews, questionnaires, and documents. The initial conceptual model of DW diffusion was used as a guide for data collection. It was then modified based on data from the bank to adapt it to the specific case situation Ž . validation .

A preliminary visit to the bank was first made. With the permission of the bank, the formal data collection was carried out at the main office of the SCB, for two months. Many types of data were required beyond the initial expectations. All required information was captured to fulfill the objectives of the study. The details of data collection are presented in Table 4.

## 4. Qualitative diffusion model of DW

In the mid 1990s, the bank executives of the SCB decided that a DW was the most preferred technology that may fulfill the bank’s mission of being ‘the best managed bank in Thailand with sustainable<sup>w</sup> <sup>x</sup> excellent performance’ 27 . However, the informa-<sup>w</sup> <sup>x</sup> tion from current users showed a low rate of diffusion. For example, of the anticipated number of users of 200, only 54 revealed that they actually used it 69 . Furthermore, factors that may hinder the diffusion of DW still exist in the bank see Table 2 .Ž .

The qualitative SD begins with creating a causal loop diagram CLD to identify information feed-Ž .

Table 4

<table><tr><td>Topic</td><td>No. of respondents</td><td>Method of data collection</td><td>Name of questionnaire/interview</td><td>Purposes</td></tr><tr><td>1. Data warehouse</td><td>10 (people in charge)</td><td>Questionnaire, interview and document</td><td>‘Data Warehouse’ [67]</td><td>Variables regarding the data warehouse</td></tr><tr><td>2. Prospective users of data warehouse</td><td>389 out of 500</td><td>Questionnaire</td><td>‘Technology and Bank Staff’ [68]</td><td>Information regarding prospective users of the data warehouse</td></tr><tr><td>3. Data warehouse users</td><td>54 out of 200</td><td>Questionnaire and interview</td><td>‘Data Warehouse Users’ [69]</td><td>Information regarding the perception of data warehouse users</td></tr><tr><td>4. Policy analyses</td><td>16 (executives)</td><td>Questionnaire and interview</td><td>‘Policy Analysis’ [66]</td><td>Variables for policy analyses</td></tr></table>

back loops. The analysis of feedback loops facilitates the understanding of how processes, organisational boundaries, delays, information, and strategies of systems interact to create system behaviour. Two types of feedback loops, positive and negative, may exist in a CLD. A positive feedback loop i.e., Ž reinforcing, or growth producing generates growth. or decay in a system variable. It tends to accelerate towards extremes, leading to greater system instability. On the other hand, a negative feedback loop i.e., Ž balancing, goal seeking, or controlling helps a sys- . tem adapt to unexpected and undesirable changes. It corrects to a balance or desired norm, or reduces a gap between a variable and a target variable 12 . <sup>w</sup> <sup>x</sup>

The qualitative model was developed based on various data<sup>r</sup>information collected during the study. First, extensive literature review was carried out to develop an initial version of the model for example, Ž see Refs. 4,7,8,11,21,25,28,40 among many others . <sup>w</sup> <sup>x</sup> . This version was then fine-tuned based on information, and explanations of the DW technology derived from the bank staff via interviews and observations. Fig. 1 presents the final version of the qualitative model.

As shown in Fig. 1, four main actors who affect the diffusion of DW at SCB are the staff of SCB, customers, SCB itself, and the vendors. Operational definition of DW diffusion in our study has been set as the number of staff of SCB who actually uses DW for their decision and information support. As such, staff of SCB plays a very dominant role. Customers of SCB are also affected by the DW diffusion. It is emphasized that DW was initially developed around a customer management system. The SCB itself, along with its attitude towards investment in DW, making good use of the opportunities provided by the DW and managing the associated running costs, is the most important player of successful DW diffusion. Finally, the technological support provided by the vendors is also important.

![](/api/attachments/BNZZYY89/fulltext/images/fb4f4c3f8014a42a7b768e319cd2d7a46900a115f9599377472c6e8b8a42f632.jpg)  
Fig. 1. Qualitative system dynamics SD model of data warehouse diffusion. Ž .

The qualitative model has a number of feedback loops Fig. 1 , for exampleŽ . $\mathrm { \bf A 1 } + , ~ \mathrm { \bf A 2 } + , ~ \mathrm { \bf B } - ,$ C<sup>y</sup>, etc. A1<sup>q</sup> is a positive feedback loop and it reads as follows: The more is the ‘investment in DW’ the more is the ‘rate of technology diffusion which leads to higher level of ‘diffused DW’. This in turn leads to more ‘economic gains’ after some delay and ultimately leads to even more ‘investment in DW’. That is, more investment in DW leads to even more investment as a result of loop A1 <sup>q</sup> . It is to be noted that delay, in SD, has significant impacts on the levels of system variables 72 . Complex delay <sup>w</sup> <sup>x</sup> pattern may destabilise the system behaviour. The negative loop B <sup>y</sup> is read as follows: The more is the ‘investment in DW’ the more is the ‘rate of technology diffusion’, which also leads to more ‘backlog of problems’ related to DW. This increases the ‘total costs’ and reduces the ‘economic gains’. The less ‘economic gains’ will lead to less ‘investment in DW’. That is, more investment in DW will lead to eventually less investment as a result of loop B<sup>y</sup>. Other loops of Fig. 1 can be interpreted similarly.

In qualitative SD, loop analyses are normally carried out in a group environment to understand the impact of different policies variables on the possi-Ž . ble system behaviour. New policies are incorporated into the qualitative model to find out if any undesirable loop results in the model 72,73 . However, the<sup>w</sup> <sup>x</sup> qualitative SD lacks the capability to produce the final outcomes of each or combined variables precisely and conclusively, because a variable or strategic policy not only produces intended impacts in one loop but also creates negative unintended impacts on other loops. The positive and negative impacts may cancel out each other, or one may have more influence than the others. For example, if the bank promotes the training support policy, knowledge worker gap will be reduced resulting in increased rate of technology diffusion Fig. 1 . However, tracing Ž . through the feedback loop of Fig. 1, it is also observed that this policy would increase training costs, and accumulate the backlog of problems viaŽ increased rate of diffusion . These may lead to de- . creased customer satisfaction and ultimately reduced economic gains. To understand the impact of interacting loops of Fig. 1, a quantitative model was thus developed and various simulations were run.

## 5. From qualitative to quantitative SD model

The transformation from qualitative to the quantitative SD flow diagram was a complex task. This was done in two steps. First, a price-less model was developed. The price-less model is defined as the model that highlights only the process of technology diffusion without dealing with the variables related to costs, benefits, etc. 30 . A great deal of learning<sup>w</sup> <sup>x</sup> took place while developing and testing the price-less model.

An estimated price model was then developed based on the causal loop diagram of Fig. 1. The model was parameterised using the available data from the bank and estimated data obtained via various surveys and interviews see Table 4 . Fig. 2Ž . shows the SD flow diagram of the DW diffusion model of the SCB. Tests on the validation of the model were performed following the guidelines of Barlas 3 and Forrester and Senge 20 . Specific <sup>w x</sup> <sup>w</sup> <sup>x</sup> attention was given to the behaviour of the variable ‘diffused DW’ which, in theory, should be S-shaped <sup>w</sup> <sup>x</sup> 33,50 .

The simulation was run in stages. In the first stage, influence of knowledge workers on the diffusion of DW was investigated. In subsequent simulations, backlog of problems, created by the use of DW, and the economic life of the DW were added to investigate their impacts on the diffusion.

5.1. Simulation 1: training as transforming deÕice for DW diffusion

As shown in Fig. 2, the diffusion process began with the objective of transforming unskilled workers or ‘required knowledge workers’ to ‘actual knowledge workers’ via ‘training’. After training, the ‘actual knowledge workers’ were considered as a proxy variable for ‘diffused data warehouse’ if they used the technology regularly. This simulation model captured three main variables.

( )i Required knowledge workers. The initial number of required knowledge workers was set at 6000. The bank ideally aims to diffuse the DW to almost all of the bank staff, approximately 13,000, though not all are expected to use it. Therefore, the analysis assumed that only half of them were the expected clients of the technology 67 . <sup>w</sup> <sup>x</sup>

![](/api/attachments/BNZZYY89/fulltext/images/0fa6c466d4dec48390c2f6ef249f4416a78ab14d290dcc5bcab0ba2fd94e926d.jpg)  
Fig. 2. SD flow diagram of the DW diffusion model.

( ) ii Actual knowledge workers. There were 200 knowledge workers in 23 departments who are expected to use the technology. Thus, the initial number of knowledge workers was set at 200. ‘Required knowledge workers’ who attend training courses would be accumulated as ‘actual knowledge workers’. The rate of training was determined by two main variables: ‘levels of training’ and ‘training delays’. The level of training from the bank was a low 0.40 in a scale of 0 to 1 see Table 5 .Ž . Ž . Furthermore, since bank officials differed in background, experience and job responsibility, it took time to provide training for them. The analysis used 12 months as the current period of training delays <sup>w</sup> <sup>x</sup> 67,69 .

(a) Simulation 1: Training as transforming device for technology diffusion.  
![](/api/attachments/BNZZYY89/fulltext/images/32f9ffe8f3b1a6479271b0ec879314ff24e3f4d328997d58ccc59d7c2799dfb8.jpg)

(b) Simulation 2: Adding the backlog of problems  
![](/api/attachments/BNZZYY89/fulltext/images/2cba8b8456f22780fa24cec381f9122c797567c5991dfaf43f08e55004c260b0.jpg)

(c) Simulation 3: Adding economic life of technology  
![](/api/attachments/BNZZYY89/fulltext/images/75f8d34b27fb720c159f7852ada6b2a2a11a86a390e18560745f4a2c694a6c10.jpg)  
Fig. 3. Diffusion of the data warehouse.

( ) iii Diffused data warehouse. As mentioned earlier, knowledge workers were considered as ‘diffused data warehouse’ if they were the regular users of the technology. Our survey found that only 54 knowledge workers out of the expected 200 currently use the technology 69 . <sup>w</sup> <sup>x</sup>

The simulation result, shown in Fig. 3a, reveals that the rate of DW diffusion is very rapid during the first few periods. Then the rate diminishes and remains low for a sustained period of time. Although the diffusion process was compulsory as directed by the bank executives, the bank was not quite ready for diffusing the technology because of the low level of training 0.40 , low perceived relative advantages Ž . Ž . Ž . Ž 0.64 and time delays for training 12 months see Table 5 . The simulation 1 reveals that the bank. accrues only 5133 users of DW out of the target of 6000 users within 60 months.

## 5.2. Simulation 2: adding the backlog of problems

The backlog of problems was added next to the simulation. According to the developers of the DW, backlog of problems, accumulated by the introduction of DW, is created at the rate of 12% per year <sup>w</sup> <sup>x</sup> 67 .

The result in Fig. 3b reveals that the diffused DW is lower than that of Fig. 3a of simulation 1, because the impact of the backlog of problems leads to increased rate of technology abandonment and decreased rate of technology diffusion see Fig. 1 .Ž .

## 5.3. Simulation 3: adding economic life of technology

All technologies become obsolete after a time <sup>w</sup> <sup>x</sup> 46,53 . The rate of technology obsolescence impacts on technology diffusion especially when that time is close to the economic life of the technology. The economic life of the DW was taken as 5 years unless substantial investment is made in the technology again 67 . The result in Fig. 3c reveals that the<sup>w</sup> <sup>x</sup> diffused DW decreased dramatically when the time is close to its economic life. Apart from technology abandonment, technology obsolescence also drains the diffused technology because technology is insufficient or no longer fulfils users’ requirements.

After the initial simulation, a number of sensitivity analyses on some important policy variables were performed. It was observed that training delays, backlog of problems, percent of resolved problems, and percent of DW abandonment are the most significant variables which impact the diffusion. Based on these and the results of the initial survey Tables 2 Ž and 3 the bank executives developed a number of . policies to enhance the DW diffusion, which are now explored in the next section.

## 6. Using DSS for strategic policy analysis

An easy-to-use DSS has been developed based on the SD model of the previous section. Fig. 4 shows the user interfaces of this DSS. It is observed that the DSS contains seven policy slide bars, the level of which can be selected by the user. It also shows that, at the highest level the ‘SCB’, ‘customers’ and ‘staff’ interact to produce the diffusion of the DW. After selecting the levels of the seven policy slide bars i.e., fixing a scenario , the user can run theŽ . simulation. The results are displayed in the form of graphs and tables. The user can also interrupt the simulation run at any time, re-adjust the policy slide bars and complete the remaining simulation run to investigate the dynamic effects of the policy variables. Using this DSS, we have performed an analyses of the impacts of the policy variables, which is discussed next.

The strategic policies to diffuse data warehousing technology involve endogenous factors such as staff and bank environments. The bank officials identified seven main strategic policies that they felt were important to increase the rate of technology diffusion. They also identified a level of perceived actual performance for each policy see Table 5 at the timeŽ . of this study. The levels of actual and desired performance of each policy were identified via survey and interviews 66 . A likert scale of 1 to 7 was used,<sup>w</sup> <sup>x</sup> where 7 represented the highest desired level of performance of a policy. Table 5 shows the actual and desired level of performances of each policy. Since, the actual performance of each strategic policy based on the developers’ perception is different from that of the users’, the average values of the two groups were used. The level of performance 1 to 7 Ž . was then transformed to a 0-to-1 scale value in order to make it suitable for simulation by ITHINK software 48 The seven strategic policies are briefly <sup>w</sup> <sup>x</sup> described below.

![](/api/attachments/BNZZYY89/fulltext/images/93a5444168c0558d02ddf533902090904266b3b0eba4d42c6f399a8e35f0f1e9.jpg)

<table><tr><td>Rate of technology dif</td><td>50.6</td></tr><tr><td>Diffused data warehou</td><td>2,873.6</td></tr><tr><td>Required knowledge wo</td><td>1,520.8</td></tr><tr><td>Actual knowledge work</td><td>74.1</td></tr><tr><td>Rel advantages</td><td>165,985.</td></tr><tr><td>Operation costs</td><td>75,167.3</td></tr><tr><td>Training costs</td><td>7,666.2</td></tr><tr><td>Total cost</td><td>134,422.</td></tr><tr><td>Economic gains</td><td>49,585.2</td></tr></table>

![](/api/attachments/BNZZYY89/fulltext/images/ba84b84353b735da186bfd1bde44b662d6fc50bc72c168167e60278ad7b4d13f.jpg)

Technology Diffusion of a Data Warehouse: The Estimated Price Model  
![](/api/attachments/BNZZYY89/fulltext/images/6ef221e202c85b30cf5015eae0b0c4f945de370b9d0da31fa54eb138981b0fa3.jpg)  
Fig. 4. User interfaces of the SD-based DSS.

Table 5  
List of strategic policies of data warehouse diffusion and their perceived actual and desired performance. Sources: Refs. 66,67,69<sup>w</sup>

<table><tr><td>Policy</td><td>Level of actual performance (average weight—1 low and 7 high)</td><td>Level of desired performance (average weight—1 low and 7 high)</td><td>Value used in ITHINK (average weight—0 low and 1 high)</td></tr><tr><td rowspan="3">1. Increased levels of training</td><td>2.67 (users)</td><td>7</td><td>From 0.40 to 1.00</td></tr><tr><td>3.00 (developers)</td><td></td><td></td></tr><tr><td>2.84 (average)</td><td></td><td></td></tr><tr><td rowspan="3">2. Increased cooperation between IT people and user</td><td>3.50 (users)</td><td>7</td><td>From 0.64 to 1.00</td></tr><tr><td>5.43 (developers)</td><td></td><td></td></tr><tr><td>4.47 (average)</td><td></td><td></td></tr><tr><td rowspan="3">3. Make it easy to use</td><td>3.24 (users)</td><td>7</td><td>From 0.46 to 1.00</td></tr><tr><td>3.14 (developers)</td><td></td><td></td></tr><tr><td>3.19 (average)</td><td></td><td></td></tr><tr><td rowspan="3">4. Increased perceived relative advantages</td><td>5.29 (users)</td><td>7</td><td>From 0.64 to 1.00</td></tr><tr><td>3.71 (developers)</td><td></td><td></td></tr><tr><td>4.50 (average)</td><td></td><td></td></tr><tr><td>5. Increased management support</td><td>6.14</td><td>7</td><td>From 0.88 to 1.00</td></tr><tr><td>6. Increased positive features of technology</td><td>4.67</td><td>7</td><td>From 0.67 to 1.00</td></tr><tr><td>7. Decreased time for training delays</td><td>12 months</td><td>6 months</td><td>From 12 to 6</td></tr></table>

( ) ( ) i Training support current level 0.4 : Clearly, training is an instrument in creating knowledge workers and enhancing their levels of understanding <sup>w</sup> <sup>x</sup> 32,35,46 . Training support calls for a higher level of training to be provided by the Bank. Bank staff recommended that the bank provide the highest level of knowledge regarding the DW via user manuals or an Intranet-based system of the bank, since staffs are unable to attend every training program. Additionally, they considered that the bank should freely allow any bank staff interested in learning and getting information to access the DW 69 .<sup>w</sup> <sup>x</sup>

( ) ( ii Cooperation between IT and users current level 0.64): Cooperation between IT departments and key users will enhance the diffusion of technology <sup>w</sup> <sup>x</sup> 35 . Since data warehousing technology is perceived as complicated, requiring versatile knowledge and tailor-made tools, end users tend to depend heavily upon IT people 67 . Therefore, technological assis-<sup>w</sup> <sup>x</sup> tance, full understanding of users’ requirements, close communication and follow-up are essential for IT staff.

( ) ( ) iii Ease of use current level 0.46 : Currently, the DW appears difficult to use. The bank is planning to decrease these perceived difficulties by installing user friendly software applications to extract required data, perform queries and create reports. Additionally, a data catalogue is planned to be designed to illustrate available data in order that users can index data that might meet their requirements. It is believed that once end-users know how to get access to their required data easily, they will use the DW regularly and develop their learning skills to maximise advantages from the available data 67 .<sup>w</sup> <sup>x</sup>

( ) iv Increased perceived relative advantages ( ) current level 0.64 : If users feel that they gain relative advantages from the DW in terms of convenience, efficiency and workload reduction, they would be pleased to use it voluntarily 21 .<sup>w</sup> <sup>x</sup>

( ) ( v Top management support current level 0.88): Given the hierarchical nature of Thai society, and the conservative culture of the bank, top management support and firm direction is vital in convincing bank staff to increase the use of the technology 67,69 .<sup>w</sup> <sup>x</sup>

( ) vi Increased positive features of technology ( ) current level 0.67 : As previously mentioned, bank staff are still confronted with many technological issues related to the DW. First, problems regarding data integrity, incompleteness, redundancy and nonupdatedness are hard to avoid due to many legacy databases. Second, the response time to retrieve, extract or transfer data is slow due to traffic jams in limited communication lines. Third, high security to protect the system from misuse by unauthorised people may reduce the convenience of usage or increase the complexity of the system. Thus, increased positive features of the technology e.g., increased relia-Ž bility, decreased response time and intensified security without added complexity are vital for diffusing. the DW 4,31,55,67,69 .<sup>w</sup> <sup>x</sup>

( ) ( vii Decreased training delays current level 12 months): The sensitivity analysis performed earlier showed that a decrease in training delays substantially boosts the rate of technology diffusion in the initial periods.

The impacts of seven strategic policies were investigated using the DSS Fig. 4 . The policy analy- Ž . sis used the current perceived values of each policy Ž . last column of Table 5 in the baseline simulation.

All the policies were simulated to detect a policy that provides the strongest impact in increasing the technology diffusion. The end results of each policy were compared as shown in Fig. 5.

Fig. 5 reveals some interesting findings. Contrary to the traditional belief, ‘management support’ policy did not change the diffusion much from the baseline simulation. This is probably due to the fact that DW adoption was initially conceived and driven by the top management and their support was already existing in the process a high current level of Ž 0.88 . Other policies, for example co-operation be- . tween IT and users, ease of use, relative advantage, features of technology, etc., produce moderate impact on the DW diffusion. However, increased level of training and decreasing training delay seemed to have the greatest impacts on the diffusion. As mentioned earlier, the SCB lacked in providing appropriate training support in the effective use of DW and their training took a long 12 months. Addressing these two issues will have the greatest impact on the diffusion of DW.

![](/api/attachments/BNZZYY89/fulltext/images/7040d950bbdb637d893b86612f827feb3fff8d67608f2e140f60153e3a6580bd.jpg)  
Fig. 5. Comparison of the impacts of strategic policies on data warehouse diffusion.

## 6.1. SensitiÕity analyses of the dominant policies

Sensitivity analyses on the two dominant policies, training delay and level of training, were performed to understand their impact on the diffusion of DW. As mentioned before, the policy of ‘level of training calls for a higher level of training in accessing and using the DW i.e., ways to use the DW extensively,Ž getting most out of DW, etc. . Table 6 presents the. results. Three levels of training delay 6, 12 and 18 Ž months and three levels of training support 0.4, . Ž 0.75 and 1 were investigated in a total of nine. combinations. It is noted that the current levels of training delay and training support are 12 months and 0.4, respectively see Table 5 . We shall call it aŽ . Ž . 12, 0.4 policy. It is emphasized that 0.4 level of training support is the perceived value, which is obtained via a survey of the users and then transformed to 0–1 scale.

The sensitivity analysis shows that the 12, 0.4Ž . policy achieves the maximum diffusion of the DW of 4102 users in month 66. The level of diffusion in month 60 with this policy will be 4097, falling far short of management’s desire of 6000. The best policy is 6, 1 , providing a possible diffusion ofŽ . 5406 in month 19 going down to the level of 4382 in month 60. This policy asks for reducing the training delay from 12 to 6 months and increasing the level of training support from 0.4 to 1. Policy of this kind could be very costly to implement. A compromise policy seems to be 6. 0.4 or 12, 0.75 , both ofŽ . Ž . which achieve similar levels of diffusion of DW seeŽ Table 6 . The first policy calls for reducing the. training delay from 12 to 6 months, keeping the training level at 0.4. The second policy increases the training level to 0.75 keeping the training delay at 12 months. Other policies can also be adopted by the management depending on factors like cost of implementation, feasibility of implementation, etc. It is interesting to note that none of the policies with a training delay of 18 months are attractive. This highlights the sensitivity of the training delay policy.

Table 6  
Sensitivity analyses on dominant policies

<table><tr><td rowspan="2">Training delay (month)</td><td rowspan="2">Level of training (0.4–1.0)</td><td colspan="2">Maximum diffusion</td><td rowspan="2">Level of diffusion at month 60</td></tr><tr><td>Level</td><td>Time (month)</td></tr><tr><td>6</td><td>0.4</td><td>4745</td><td>40</td><td>4502</td></tr><tr><td>6</td><td>0.75</td><td>5212</td><td>23</td><td>4431</td></tr><tr><td>6</td><td>1</td><td>5406</td><td>19</td><td>4382</td></tr><tr><td>12</td><td>0.4</td><td>4102</td><td>66</td><td>4097</td></tr><tr><td>12</td><td>0.75</td><td>4703</td><td>42</td><td>4504</td></tr><tr><td>12</td><td>1</td><td>4923</td><td>34</td><td>4499</td></tr><tr><td>18</td><td>0.4</td><td>3658</td><td>83</td><td>3505</td></tr><tr><td>18</td><td>0.75</td><td>4328</td><td>55</td><td>4316</td></tr><tr><td>18</td><td>1</td><td>4595</td><td>46</td><td>4474</td></tr></table>

Fig. 5 also shows that while each policy enhances diffused DW to some extent, none of the policies individually could produce the target technology diffusion of 6000 users within 60 months.

Since the model developed was based on the SD-based DSS, decision makers are able to use the model to test all the policies by themselves by using user-friendly tools. That is, although the model was developed using rich data e.g., literature reviews,Ž interviews and questionnaires , employing complex . tools e.g., influence diagrams, mathematical equa- Ž tions and simulation models and consuming consid-. erable time, it presents the decision makers with easy interfaces such as control tools, maps, figures, graphs and tables for effective decision support.

## 7. Implications for management

The SD-based DSS for the DW diffusion provides some valuable lessons for the management of the SCB.

None of the policies devised by the management achieve the target diffusion of 6000 by the stipulated time of 60 months. This is extremely valuable information for the managers in charge. They should now realize what is feasibly achievable for the DW diffusion. Fig. 5 also shows that even a combination of all the policies does not achieve the goal. It, however, diffuses the DW very quickly. But implementing a combined policy could be extremely costly.

Two dominant policies, training delay and level of training support, emerged as having the greatest impact on the diffusion. The sensitivity analyses

Ž . Table 6 show the various combinations of these two policies. Management should be careful in implementing these two policies. Reducing the training delay for example, from 12 months to 6 monthsŽ . perhaps easily achievable, albeit being costly. But the level of training support policy must be carefully planned for implementation. It is highlighted that low level of training has been found to be an important deterrent of the diffusion. On the other hand, high level of training has been suggested to be a significant factor for promoting the diffusion in our survey see Tables 2 and 3 . The following approachŽ . may be followed to plan and implement the training support policy.

Our survey reveals that the current level of training support is a low 0.40 see Table 5 . The manage-Ž . ment can now list the items of training being provided currently and find how are they being provided. Keeping this as the benchmark a level of 0.4 theŽ . management can make a list of items, which will increase the level of training support. This might include preparing extra easy-to-use brochures, providing intranet-based training suggested by the usersŽ in our survey , dedicated help desk, among many . others. Each of these will add to the training support. A combination of these would probably give the maximum training support possible a level of 1 .Ž . Management can then select the items of training to be provided to increase the current level of training support.

## 8. Conclusion

This paper presents a model of technology diffusion of DW using the SD-based DSS approach. The model demonstrates the ways to develop a requisite model of diffusion of DW using the SD approach incorporating user-friendly tools. Therefore, decision makers are able to test their decisions using their own insights.

A qualitative SD approach was initially employed to identify the present state of this technology. The qualitative model provides holistic perspectives, but it is not capable of investigating the impacts of interaction among the feedback loops. A quantitative SD approach was therefore taken.

The quantitative model was simulated which provided insights on how to diffuse the DW to the bank staff via training and other policies. The dominant policies for successful diffusion were: increasing the leÕels of training, and decreasing training delays. Other policies had moderate impact on the diffusion. Sensitivity analyses of the two dominant policies showed various combinations, which could be adopted by the bank executives. If the bank implements all policies effectively, it may dramatically decrease the time for technology diffusion and substantially increase the level of DW diffusion. However, such an undertaking is probably not feasible in reality. The bank should therefore concentrate on the dominant policies and then gradually move into other policies, which are politically, socially and technically feasible to achieve.

## References

<sup>w</sup> <sup>x</sup> 1 E.G.J. Anderson, N.R. Joglekar, Modelling the dynamics of innovation at the firm level,System Dynamics Conference, Cambridge, Massachusetts, 1996.

<sup>w</sup> <sup>x</sup> 2 Arthur Anderson and Co., Trends and Issues in Retail Financial Services Technology: Case Study-Australia Lafferty,Ž 1989 ..

<sup>w</sup> <sup>x</sup> 3 Y. Barlas, Formal aspects of model validity and validation in system dynamics, System Dynamics Review 12 3 1996Ž . Ž . 183–210.

<sup>w</sup> <sup>x</sup> 4 R. Barras, Interactive innovation in financial and business services: the vanguard of the service revolution, in: E. Rhodes, D. Wield Eds. , Implementing New Technologies, Black-Ž . well, London, 1994, pp. 106–120.

<sup>w</sup> <sup>x</sup> 5 F.M. Bass, A new product growth model for consumer durables, Management Science 15 1969 215–227.Ž .

<sup>w</sup> <sup>x</sup> 6 S.C. Bhatnagar, Is technology transfer the answer? in: K. Duncan, K. Krueger Eds. , The IFIP, 13th World Computer Ž . Congress 94, vol. 3, Elsevier, North-Holland, Amsterdam, 1994, pp. 453–455.

<sup>w</sup> <sup>x</sup> 7 Butler Group, Business Case for Data Warehousing Strategies and Technologies, 1996, available from http:<sup>rr</sup> www.butlergroup.co.uk<sup>r</sup>manguide<sup>r</sup>dwuk1096<sup>r</sup>s1.htm.

<sup>w</sup> <sup>x</sup> 8 Butler Group, Brio Technology: The Keys to the Data Warehouse: Access Tools for End Users Desktop Data Access, 1996, available from http:<sup>rr</sup>www.butlergroup.co.uk<sup>r</sup> manguide<sup>r</sup>dwuk1096<sup>r</sup>brio.htm.

<sup>w</sup> <sup>x</sup> 9 Butler Group, Business Case for Data Warehousing Strategies and Technologies Online , 1997, available from http: <sup>w</sup> <sup>x</sup> <sup>rr</sup> www.butlergroup.co.uk<sup>r</sup>manguide<sup>r</sup>dwuk1096<sup>r</sup>s1.htm.

<sup>w</sup> <sup>x</sup> 10 M. Cervantes, Diffusing technology to industry, OECD Observer 207 1997 20–23.Ž .

<sup>w</sup> <sup>x</sup> 11 R.B. Cooper, R.W. Zmud, Information technology imple-

mentation research: a technological diffusion approach, Management Science 36 2 1990 123–139.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 R.G. Coyle, System Dynamics Modelling: A Practical Approach, Chapman & Hall, London, 1996.

<sup>w</sup> <sup>x</sup> 13 C. Currid, Technology takes centre stage in a changing business world, InfoWorld 15 18 1993 62.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 B.L. Dos Santos, K. Peffers, Rewards to investors in innovative information technology applications: first movers and early followers in ATMs, Organisation Science 6 3 1995Ž . Ž . 241–259.

<sup>w</sup> <sup>x</sup> 15 I. Dyner, R.A. Smith, G.E. Pena, System dynamics modelling for residential energy efficiency analysis and management, Journal of Operational Research Society 46 1995Ž . 163–173.

<sup>w</sup> <sup>x</sup> 16 Federal Bureau of Consumer Affairs, A Cashless Society? Electronic Banking and the Consumer, AGPS, Canberra, 1995.

<sup>w</sup> <sup>x</sup> 17 R.G. Fichman, C.F. Kemerer, Toward a theory of adoption and diffusion of software process innovations, in: L. Levine Ž . Ed. , IFIP TC8: Diffusion, Transfer and Implementation of Information Technology, North-Holland, Pittsburgh, 1994, pp. 23–30.

<sup>w</sup> <sup>x</sup> 18 D. Fink, K. Kazakoff, Getting IT right, Australian Accountant 67 10 1997 50–52.Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 J.W. Forrester, Principles of Systems, Wright-Allen, Cambridge, 1968.

<sup>w</sup> <sup>x</sup> 20 J.W. Forrester, P.M. Senge, Tests for building confidence in system dynamics models, TIMS Studies in the Management Sciences 14 1980 209–228.Ž .

<sup>w</sup> <sup>x</sup> 21 Y.C. Gagnon, J.M. Toulouse, The behaviour of business managers when adopting new technologies, Technological Forecasting and Social Change 52 1996 59–74.Ž .

<sup>w</sup> <sup>x</sup> 22 E. Geisler, Managing information technologies in small business: some practical lessons and guidelines, Journal of General Management 18 1 1992 74–81. Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 S. Gozlu, Transfer of information technology to a developing environment: the Turkish case, in: K. Duncan, K. Krueger Ž . Eds. , The IFIP, 13th World Computer Congress 94, vol. 3, Elsevier, North-Holland, Amsterdam, 1994, pp. 465–470.

<sup>w</sup> <sup>x</sup> 24 R. Hackathorn, Data warehousing energises your enterprise, Datamation 41 2 1995 38–42.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 C. Horrock, Making the Warehouse Work, 1996, available from http:<sup>rr</sup>www.computerworld.com<sup>r</sup>sear . . . -htm1<sup>r</sup> 9606<sup>r</sup>960624DW1SL96dw10.html.

<sup>w</sup> <sup>x</sup> 26 W.H. Inmon, R.D. Hackathorn, Using the Data Warehouse, Wiley, New York, 1994.

<sup>w</sup> <sup>x</sup> 27 A. Intrapairot, M. Quaddus, Adoption and Diffusion of Data Warehousing Technology: A System Dynamic Approach, 16th International Conference of the System Dynamics Society, Quebec City, Canada 1998 .Ž .

<sup>w</sup> <sup>x</sup> 28 S. Kelly, Data Warehousing: The Route to Mass Customisation, Wiley, Chichester, 1994.

<sup>w</sup> <sup>x</sup> 29 D.H. Kim, J.H. Juhn, Dynamics of networks: System Dynamics Model for Network Externality and Critical Mass, 1996, available from http:<sup>rr</sup>soback.kornet.nm.kr<sup>r</sup> <sup>;</sup> sddhkim<sup>r</sup>96dyn.html.

<sup>w</sup> <sup>x</sup> 30 M. Kummerow, M. Quaddus, Office market cycles: a system

dynamics approach to improve allocative efficiency,Proceedings of Sixteenth International Conference of the System Dynamics Society CD-ROM , Quebec, Canada, 1998. Ž .

<sup>w</sup> <sup>x</sup> 31 T.H. Kwon, R.W. Zmud, Unifying the fragmented models of information system implementation, in: R.J. Boland, R.A. Hirschheim Eds. , Critical Issues in Information SystemsŽ . Research, Wiley, New York, 1987, pp. 227–251.

<sup>w</sup> <sup>x</sup> 32 C.N. Madu, Transferring technology to developing countries: critical factors for success, Long Range Planning 22 4Ž . Ž .1989 115–124.

<sup>w</sup> <sup>x</sup> 33 V. Mahajan, R.A. Peterson, Models of Innovation Diffusion, Sage, Beverley Hills, 1985.

<sup>w</sup> <sup>x</sup> 34 F.H. Maier, New product diffusion models in innovation management: a system dynamics perspective, System Dynamics Review 14 4 1998 285–308.Ž . Ž .

<sup>w</sup> <sup>x</sup> 35 G.G. Manross, R.E. Rice, Don’t hang up: organisational diffusion of the intelligent telephone, Information and Management 10 1986 161–175.Ž .

<sup>w</sup> <sup>x</sup> 36 P.M. Milling, Modelling innovation processes for decision support and management simulation, System Dynamics Review 12 3 1996 211–234.Ž . Ž .

<sup>w</sup> <sup>x</sup> 37 J.D.W. Morecroft, Executive knowledge, models and learning, in: J.D.W. Morecroft, J.D. Sterman Eds. , Modelling forŽ . Learning Organisations, Productivity Press, Portland, 1992, pp. 1–27.

<sup>w</sup> <sup>x</sup> 38 J.A. O’Brien, Management Information Systems: Managing Information Technology in the Networked Enterprise, 3rd edn., Irwin, Chicago, 1996.

<sup>w</sup> <sup>x</sup> 39 A.F. Orenstein, Putting information to work, Bank Systems and Technology 34 8 1997 30–34. Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 O. O’Sullivan, Data warehousing: without the warehouse, ABA Banking Journal 88 12 1996 42–45.Ž . Ž .

<sup>w</sup> <sup>x</sup> 41 G. Papaconstantinou, N. Sakurai, A. Wyckoff, Domestic and international product-embodied Randd diffusion, Research Policy 27 3 1998 301–314.Ž . Ž .

<sup>w</sup> <sup>x</sup> 42 G.P. Prendergast, Self-service technologies in retail banking: current and expected adoption patterns, International Journal of Bank Marketing 11 7 1993 29–35.Ž . Ž .

<sup>w</sup> <sup>x</sup> 43 G.P. Prendergast, N.E. Marr, The future of self-service technologies in retail banking, Service Industries Journal 14 1Ž . Ž . 1994 94–114.

<sup>w</sup> <sup>x</sup> 44 R.M. Price, Executive forum: technology and strategic advantage, California Management Review 38 3 1996 38–Ž . Ž . 56.

<sup>w</sup> <sup>x</sup> 45 M.A. Quaddus, Diffusion of information technology: an exploration of the stage models and facilitating the user’s choice by systems approach, Proceedings of the Second Pacific Asia Conference on Information Systems, Singapore, 1995.

<sup>w</sup> <sup>x</sup>46 M.A. Quaddus, GSS Supported System Dynamics: A Model for IT Planning, Curtin University of Technology, Perth, Western Australia, 1996.

<sup>w</sup> <sup>x</sup> 47 G.P. Richardson, Problems for the future of system dynamics, System Dynamics Review 12 2 1996 141–157.Ž . Ž .

<sup>w</sup> <sup>x</sup> 48 B. Richmond, S. Peterson, C. Charyk, Introduction to System Thinking and Ithink, High Performance Systems, Hanover, 1994.

<sup>w</sup> <sup>x</sup> 49 A.G. Rodrigues, T.M. Williams, System dynamics in project management: assessing the impacts of client behaviour on project performance, Journal of Operational Research Society 49 1 1998 2–15.Ž . Ž .

<sup>w</sup> <sup>x</sup> 50 E.M. Rogers, Diffusion of Innovations, 3rd edn., The Free Press, New York, 1983.

<sup>w</sup> <sup>x</sup> 51 A.V. Roth, M. Van Der Velde, Investing in retail delivery system technology, Journal of Retail Banking 11 2 1989Ž . Ž . 23–34.

<sup>w</sup> <sup>x</sup> 52 K. Saeed, Government’s ability to manage political conflict over the course of economic development, in: P.M. Milling, E.O.K. Zahn Eds. , Computer-Based Management of Com-Ž . plex Systems: The 1989 International Conference of the System Dynamics Society, Springer, Berlin, 1989, pp. 624– 632.

<sup>w</sup> <sup>x</sup> 53 K. Saeed, Managing technology for development: a systems perspective, Socio Economic Planning Science 24 3 1990Ž . Ž . 217–228.

<sup>w</sup> <sup>x</sup> 54 K. Sahin, Multidimensional Database Technology and Data Warehousing, 1997, available from http:<sup>rr</sup>www.Kenan. Com<sup>r</sup>Acumate<sup>r</sup>Byln Mdw.Htm.

<sup>w</sup> <sup>x</sup> 55 L. Sayeed, H.J. Brightman, Can information technology improve managerial problem finding? Information and Management 27 6 1994 377–390.Ž . Ž .

<sup>w</sup> <sup>x</sup> 56 P.M. Senge, Organisational learning: a new challenge for system dynamics, in: P.M. Milling, E.O.K. Zahn Eds. ,Ž . Computer-Based Management of Complex Systems: The 1989 International Conference of the System Dynamics Soci ety, Springer, Berlin, 1989, pp. 229–236.

<sup>w</sup> <sup>x</sup> 57 M.N. Sharif, Technology change management: imperatives for developing economies, Technological Forecasting and Social Change 47 1994 103–114.Ž .

<sup>w</sup> <sup>x</sup> 58 M.N. Sharif, Integrating business and technology strategies in developing countries, Technological Forecasting and Social Change 45 1994 151–167.Ž .

<sup>w</sup> <sup>x</sup> 59 M.N. Sharif, C. Kabir, System dynamics modelling for forecasting multilevel technological substitution, Technological Forecasting and Social Change 9 1976 89–112.Ž .

<sup>w</sup> <sup>x</sup> 60 C. Smith, Retail Banking in the 1990s: The Technology Suppliers’ View, Lafferty, London, 1984.

<sup>w</sup> <sup>x</sup> 61 H. Sraeel, Who’s who in banking: the best and worst players of 1996, Bank Systems and Technology 33 12 1996 7.Ž . Ž .

<sup>w</sup> <sup>x</sup> 62 P.F. Takac, C.P. Singh, Banking technology: improving its potential through better management, Management Decision 30 5 1992 17–20.Ž . Ž .

<sup>w</sup> <sup>x</sup> 63 J. Tesawanich, Money and Banking, 3rd edn., Odean Store, Bangkok, 1991.

<sup>w</sup> <sup>x</sup> 64 L. Thach, R.W. Woodman, Organisational change and information technology: managing on the edge of cyberspace, Organisational Dynamics 23 1 1994 30–46.Ž . Ž .

<sup>w</sup> <sup>x</sup> 65 Thai Farmer Bank Public Company Limited. Competitive Advantage: Re-Engineering Program, 1999, available from http:<sup>rr</sup>www.tfb.co.th<sup>r w</sup> <sup>x</sup> 1999, April 23 .

<sup>w</sup> <sup>x</sup> 66 The Siam Commercial Bank’s Executives, Policy Analysis Questionnaire and Interview, 6 January–28 February 1998 Ž . Personal Communication.

<sup>w</sup> <sup>x</sup> 67 The Siam Commercial Bank’s Staff, Data Warehouse Questionnaire and Interview, 6 January–28 February 1998 Per-Ž . sonal Communication.

<sup>w</sup> <sup>x</sup> 68 The Siam Commercial Bank’s Staff, Technology and Bank Staff Questionnaire, 6 January–28 February 1998 PersonalŽ . Communication.

<sup>w</sup> <sup>x</sup> 69 The Siam Commercial Bank’s Staff, Data Warehouse Users Questionnaire and Interview, 6 January–28 February 1998Ž . Personal Communication.

<sup>w</sup> <sup>x</sup> 70 J. Thong, C.S. Yap, CEO characteristics, organisational characteristics and information technology adoption in small businesses, Omega 23 4 1995 429–442.Ž . Ž .

<sup>w</sup> <sup>x</sup> 71 J.A.M. Vennix, D.F. Anderson, G.P. Richardson, J. Rohrbaugh, Model building for group decision support: issues and alternatives in knowledge elicitation, European Journal of Operational Research 59 1992 28–41.Ž .

<sup>w</sup> <sup>x</sup> 72 E.F. Wolstenholme, System Enquiry: A System Dynamics Approach, Wiley, Chichester, 1994.

<sup>w</sup> <sup>x</sup> 73 E.F. Wolstenholme, R.G. Coyle, The development of system dynamics as a methodology for system description and qualitative analysis, Journal of Operational Research Society 34 Ž . Ž .1 1983 569–581.

Dr. M.A. Quaddus received his Ph.D. from the University of Pittsburgh and his MS from the University of Pittsburgh and Asian Institute of Technology. His research interests are in decision support systems, group decision and negotiation support systems, multiple criteria decision making, systems dynamics, business research methods and in the theories and applications of innovation diffusion process. Dr Quaddus has published in a number of journals including Technological Forecasting and Social Change, Socio-Economic Planning Sciences, Journal of OR Society, Interfaces, Engineering Optimization, Eng Costs and Production Economics, International Journal of Management, Computers and Education, etc., and contributed to several books and monographs. In 1996, he received the researcher of the year award in the Curtin Business School. Currently, he is an Associate Professor with the Graduate School of Business, Curtin University of Technology, Australia. Prior to joining Curtin, Dr. Quaddus was with the University of Technology-Sydney and with the National University of Singapore.

Ms. Arunee Intrapairot is a lecturer in computer and information systems at the Rajamangala Institute of Technology, Chiang Mai, Thailand. The research for this paper was conducted when Ms. Intrapairot was pursuing her Ph.D. at the Graduate School of Business, Curtin University of Technology, Perth, Australia. Her research interests are in system dynamics for policy analysis, IT adoption and multicriteria analysis for dispersed groups.
