---
otero_id: 28700
otero_key: "JCK4AVZ5"
title: "Preparedness and Response in the Century of Disasters: Overview of Information Systems Research Frontiers"
authors: "Ahmed Abbasi; Robin Dillon; H. Raghav Rao; Olivia R. Liu Sheng"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2024.intro.v35.n2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Preparedness and Response in the Century of Disasters: Overview of Information Systems Research Frontiers

Ahmed Abbasi,<sup>a,</sup>\* Robin Dillon,<sup>b</sup> H. Raghav Rao,<sup>c</sup> Olivia R. Liu Sheng<sup>d</sup>

<sup>a</sup> Department of IT, Analytics, and Operations, Mendoza College of Business, University of Notre Dame, Notre Dame, Indiana 46556; <sup>b</sup> McDonough School of Business, Georgetown University, Washington, District of Columbia 20057; <sup>c</sup> Department of ISCS, University of Texas at San Antonio, San Antonio, Texas 78249; <sup>d</sup> Department of Information Systems, W.P. Carey School of Business, Arizona State University, Tempe, Arizona 85281

\*Corresponding author

Contact: aabbasi@nd.edu, https://orcid.org/0000-0001-7698-7794 (AA); robin.dillonmerrill@georgetown.edu (RD); hr.rao@utsa.edu (HRR); olivia.liu.sheng@asu.edu, https://orcid.org/0000-0002-5263-2726 (ORLS)

Received: March 22, 2024 Accepted: April 1, 2024

https://doi.org/10.1287/isre.2024.intro.v35.n2

Copyright: © 2024 INFORMS

Abstract. “The Century of Disasters” refers to the increased frequency, complexity, and magnitude of natural and man-made disasters witnessed in the 21st century: the impact of such disasters is exacerbated by infrastructure vulnerabilities, population growth/urbanization, and a challenging policy landscape. Technology-enabled disaster management (TDM) has an important role to play in the Century of Disasters. We highlight four important trends related to TDM, smart technologies and resilience, digital humanitarianism, integrated decisionsupport and agility, and artificial intelligence–enabled early warning systems, and how the confluence of these trends lead to four research frontiers for information systems researchers. We describe these frontiers, namely the technology-preparedness paradox, socio-technical crisis communication, predicting and prescribing under uncertainty, and fair pipelines, and discuss how the eight articles in the special section are helping us learn about these frontiers.

History: Senior editor, Suprateek Sarker.

Funding: This study was funded by the National Science Foundation (NSF) [Grants 2240347 and IIS 2039915]. H. R. Rao is also supported in part by the NSF [Grant 2020252]. The usual disclaimer applies.

Keywords: information systems research • technology-enabled disaster management • preparedness

## 1. Introduction

The 21st century has been described as “The Century of Disasters” (Achenbach 2011), a reference to the increased frequency, complexity, and magnitude of natural and man-made disasters faced today and expected to worsen in the future. Many factors are contributing to a surge in disasters: increasing infrastructure vulnerabilities, population growth and urbanization, climate change, and evolving social dynamics. Disasters, when they occur, inflict a devastating toll on both civil and technical infrastructure as well as society at large including loss of human life, disruptions to social and economic stability, and environmental harm. Notably, disaster management (DM) is a topic that has been studied extensively in multiple fields (Sarker et al. 2023). Countless studies have underscored the important role of technology in DM, yet there remains a paucity of work at the intersection of technology and DM (Beydoun et al. 2019). The purpose of this special section (Abbasi et al. 2021) is to foster a robust dialogue within the information systems (IS) research community on new research frontiers for technology-enabled DM (TDM). Figure 1 describes a framework that shows how various characteristics of the Century of Disasters influence the evolving technologyenabled, multidimensional DM landscape, and how the confluence of these factors leads to four research frontiers for IS researchers. The framework was guided by our experiences managing the review process for the many papers submitted to the special section, including the eight accepted papers. Here, we discuss characteristics of the century of disasters, describe the emerging technology-enabled DM landscape, propose research frontiers, and use these frontiers to introduce the articles in this special section.

## 2. Characteristics of the Century of Disasters

We highlight six significant characteristics of the Century of Disasters that are relevant for technology-enabled disaster management (shown in the upper left quadrant of Figure 1). First, despite technological advancements, the frequency of serious natural and man-made disasters continues to increase (Kundzewicz et al. 2018, Yabe et al. 2022). Figure 2 shows the number of weather and climate disasters in the United States per year where losses from the event exceeded \$1 billion (NOAA 2024). Although this figure only considers U.S. weather and climate events, including other types of events or global data

Figure 1. Framework for TDM in the Century of Disasters  
![](/api/attachments/JCK4AVZ5/fulltext/images/a00885f34ba52d1a353b5a2e7383081abda956936ca55cc4241e2417263a6246.jpg)

would not change the pattern. Unfortunately, as shown in Figure 3, an increasing pattern also exists for fatalities in these events. Although fatality trends may be skewed by a few significant events (i.e., Hurricanes Katrina and Maria in Figure 3), the pattern demonstrates that advancements in information technology (IT) have not had a significant impact in changing these trends, and damages and fatalities in hazardous events persist. Additionally, climate change is accelerating the rise of numerous natural disasters, particularly increasing occurrences of droughts, hurricanes, floods, and tornadoes. Additionally, it intensifies the impact of events such as flooding and tsu namis resulting from elevated sea levels (Bago et al. 2023, USGS 2024).

Figure 2. (Color online) Count of Weather and Climate Disasters in the United States per Year Where Losses from the Event Exceeded \$1 Billion (NOAA 2024)  
![](/api/attachments/JCK4AVZ5/fulltext/images/650d33d5fc915116ecd3b78ba10a03fdc839b99313969aac70dcdf1375144dfc.jpg)

Second, events are becoming more complex and interconnected (Yabe et al. 2022). For example, although past flooding models may have solely addressed coastal storm surges or heavy rainfall, the interplay between these phenomena, worsened by climate change, underscores the necessity of incorporating both types of flooding sources into our decision support models (Zheng et al. 2014). In a particular complex and interconnected event, evacuees from Hurricane Laura in Texas and Louisiana in August 2020 saw challenges because the need for physical distancing from COVID-19 in shelters conflicted with the traditional approach of accommodating large numbers of people in close quarters. The combination of these two events (hurricane requiring evacuation and COVID-19) created challenges in ensuring the safety of evacuees from Hurricane Laura while minimizing the risk of COVID-19 transmission.

Figure 3. (Color online) Fatalities in Weather and Climate Disasters in the United States per Year for Events Where Losses from the Event Exceeded \$1 Billion (NOAA 2024)  
![](/api/attachments/JCK4AVZ5/fulltext/images/9a990b9d8f9b918fb70685c0fd9b18bc3957c509d3ef6247415d6fe6bcca0090.jpg)

Third, events are occurring with greater magnitude and unpredictability (Yabe et al. 2022). For example, prior to the 2004 earthquake in Indonesia, scientists were aware of the potential for large earthquakes in the region but would not have anticipated a quake with a magnitude of 9.1–9.3 occurring. When the large 2004 earthquake occurred, it triggered a tsunami that traveled across the Indian Ocean, affecting coastal areas in multiple countries, including Indonesia, Thailand, Sri Lanka, India, and others. It is estimated that more than 200,000 people were killed in this catastrophic event. The sheer magnitude and global impact of the event made many consider this a black swan event (Taleb 2010), surprising experts and highlighting the need for enhanced IT- supported early warning systems and international cooperation in disaster preparedness. Subsequent efforts have been made to use IT to improve global tsunami warning systems and enhance preparedness for such rare but devastating events, but we need to recognize the magnitude of events are increasing and realize that some disasters may not qualify as a black swan event in the future because we should have been able to recognize the increased risks.

Fourth, the growth of population and urbanization increases the exposure of people and infrastructure to natural disasters (Yabe et al. 2022). As more communities expand into vulnerable areas, the potential for significant impacts and casualties rises. This is especially relevant to the increased wildfire risks when urban areas expand and further encroach on wildland areas. Higher population densities put more people and property at risk for wildfires, increase ignition risks, and make evacuations more challenging.

Fifth, despite technological advancements, many existing structures and infrastructure may not be designed to withstand extreme events (Kundzewicz et al. 2018, Ohenhen et al. 2024). Aging infrastructure or inadequate building codes in certain regions can contribute to increased vulnerability. Hurricane Katrina emphasized the critical need for investing in modern and resilient infrastructure, particularly highlighting the reliance on levees that had been gradually sinking due to subsidence and had not received sufficient updates over time.

Sixth, disaster management has been affected by distrust in institutions, information, and technology (Elinder and Erixson 2012, Betsch et al. 2020, Bago et al. 2023).

Different geographical, economic, and cultural communities are served with disparate disaster management infrastructures, resources, and responses. To prepare for and respond to the growing challenges of disaster management, all stakeholders must step up the efforts to collect, integrate and analyze data from heterogeneous sources to better understand the root causes and develop effective predictive solutions and prescriptive decision support for infrastructure expansion and effective communication, as well as fair preparation, response, and recovery resource allocations. More importantly, it will be necessary to investigate effective technology and platform governance to address the misinformation/ disinformation concerns and regain trust in the information exchanged on climate change and disaster management (Park 2022).

## 3. Technology Enabled DM

## 3.1. Multidimensional DM Landscape

Because of these six identified challenges, DM is increasingly demanding, making technology-enabled solutions even more crucial and pertinent. DM encompasses several crucial phases: mitigation, preparedness, response, and recovery, targeting threats and hazards of the utmost concern (DHS 2015). Recognizing that the problem requires solutions at each of these phases, it involves a proactive and integrated approach, engaging a multitude of stakeholders, each with their distinct objectives. Mitigation strategies aim to reduce the impact of potential disasters through risk reduction measures, aligning the diverse goals of government agencies, nongovernmental organizations, and community leaders. Preparedness focuses on enhancing the capabilities and readiness of communities, response agencies, and other stakeholders, each bringing unique perspectives and priorities to the table. Swift and coordinated actions during the response phase are vital for minimizing casualties and damages, requiring seamless collaboration among government entities, first responders, and various community organizations. In the recovery phase, the emphasis lies on rebuilding and restoring affected areas, accommodating the diverse needs and objectives of stakeholders, including businesses, residents, and social service agencies, to foster resilience. Acknowledging the interconnectedness of these phases is essential for fostering a DM system that addresses the numerous, different multihazards, including natural disasters, disease pandemics, chemical spills, and other man-made hazards such as terrorist attacks and cyber threats (DHS 2015), integrating the diverse objectives of the multiple stakeholders involved.

## 3.2. Crucial and Evolving Role of Technology in Disasters

The importance of technology-enabled DM cannot be overstated. As one example, despite the World Economic Forum (WEF) highlighting a global pandemic as a significant risk 15 times between 2006 and 2020 (World Economic Forum 2020), many national health departments worldwide initially lacked IT systems to track cases. Throughout the first 15 months of the COVID-19 pandemic in the United States, the most reliable data source on key metrics, such as cases, hospitalizations, and deaths, was not the federal government but rather a volunteer effort coordinated by journalists (COVID Tracking Project 2021).

Effective DM demands continuous improvement, incorporating lessons learned from past incidents and embracing innovative technologies to ensure a robust and resilient framework capable of safeguarding communities in the face of adversity. Each phase of DM and every type of disaster present distinct challenges in gathering, sharing, interpreting, and disseminating information, as well as in effectively supporting time-critical decision making. The role of information systems (IS) and technology in addressing these challenges continually evolves, adapting to new information sources and technologies. We highlight four important trends from TDM: smart technologies and resilience, digital humanitarianism, integrated decision support agility, and artificial intelligence (AI)-enabled warning systems.

3.2.1. Smart Technologies and Resilience. Smart technologies combine AI, and technologies such as Internet-of-things (IoT), robots, image/speech recognition, unmanned aerial vehicles (UAVs), mobile, sensors/ wearables, and platforms (Yang et al. 2021). Resilience can be defined as “an endowed or enriched property of a system that is capable of effectively combating (absorbing, adapting to, or rapidly recovering from) disruptive events” (Francis and Bekera 2014, p. 91). Smart technologies have profound implications for disaster management (Can˜ avera-Herrera et al. 2022), including opportunities, challenges, and threats related to greater technology reliance across stages of disaster management.

3.2.2. Digital Humanitarianism. Digital humanitarianism involves using digital technologies, data, and online platforms to support disaster response and humanitarian efforts (Kumar et al. 2022). This includes leveraging platforms and tools such as social media and mobile apps to collect and disseminate information, coordinate relief efforts, facilitate remote participation, and provide aid to affected communities during and after disasters or humanitarian crises. Digital humanitarianism is not without its challenges, however, such as dehumanization and opacity in the human aid process and concerns about algorithmic bias and privacy (Devidal 2023).

3.2.3. Integrated Decision-Support Agility. Integrated decision-support agility pertains to the enhanced situational awareness and responsiveness afforded through increased enterprise-wide and cross-organization data sharing and systems integration. This trend has positive implications for knowledge management and sharing practices during disasters, although questions abound about the implications of variance in organizational capabilities and (lack) of consistency in cross-organization management strategies and sharing practices (Oktari et al. 2020).

3.2.4. AI-Enabled Early Warning Systems. AI-enabled early warning systems are predictive systems powered by machine learning and capable of forecasting natural disaster–related phenomena such as rapidly intensifying storms, pandemics, earthquakes, and flooding (Yabe et al. 2022). As disasters become more complex, older detection systems without AI will lack the capacity and sophistication needed to provide adequate risk identification and assessment capabilities (Wever et al. 2022).

These trends underscore the diverse ways in which TDM is used by stakeholders in disasters, emphasizing the need for continued expansion to meet the challenges of this Century of Disasters.

## 4. Research Frontiers

In curating this special section, four important research frontiers became apparent with the eight papers appearing in the special section contributing to our understanding of these frontiers. Figure 4 presents an overview of the frontiers and how the special section articles relate to them with two papers relating to two different frontiers.

## 4.1. Technology-Preparedness Paradox

The technology-preparedness paradox arises from the growing societal dependence on technology, especially evident during pre- and postdisaster phases, which makes us more vulnerable to technology-related disasters and vulnerabilities. Put another way, the same technologies that allow us to better respond to and recover from disasters may increase the severity of unintended consequences during disasters. A simple example of this is the transition from physical landline telephony to mobile cellular devices that require electricity to function, with the latter being more susceptible to disaster-related power outages. Another power outage–related example is how those in rural environments relying on electric wells may lose access to water. These outage-based preparedness and response issues are exacerbated by the fact that the frequency of weather-related and human vandalism/attack-driven major power outages (i.e., those impacting at least 50,000 people) in the United States have gone up by an order of magnitude this century (DOE 2024).

In real-world settings, the manifestations of this paradox can be far more nuanced than the aforementioned examples related to power outages. They may relate to various other technology/infrastructure vulnerabilities, such as reliance on smart technologies and intelligent sensing that may not be feasible during a severe disaster (Can˜ avera-Herrera et al. 2022). The technologypreparedness paradox may also be induced by existing digital divides, as well as other well-known tensions such as the privacy paradox (Devidal 2023). For instance, Hou et al. (2023) show that during disasters, telework adjustments can alleviate gender inequalities in labor market outcomes; however, this effect is more pronounced in geographical areas with better digital infrastructure (i.e., access to high-speed Internet). IS has only just begun to scratch the surface regarding implications and solutions related to the technology-preparedness paradox. One of the papers in this special section contributes to this research theme.

Figure 4. How Special Section Articles Relate to Research Frontiers for TDM in the Century of Disasters  
![](/api/attachments/JCK4AVZ5/fulltext/images/f57cb68615593b1b89e4383083d6ecd34b6f34710b62a427be2cc3d123383abf.jpg)

Ghose et al. (2024) explore the efficacy of digital trace alerts (DTAs) in inducing protective avoidance behaviors in the form of real-time population movements away from high-risk areas. A critical challenge they acknowledge is the tradeoffs between public safety and personal privacy: the fine line between technologyenabled responsiveness and perceived mass surveillance (Devidal 2023). In their analysis, they explore the impact of the extent of private information disclosed in alerts on aggregate movement patterns. They find that the tensions between private information disclosures and proactive protective behaviors may not be as incompatible as typically described, suggesting that effective disaster response policies might be able to effectively balance the two. We hope that other studies will build on their work and explore other important facets of the technology-preparedness paradox.

## 4.2. Socio-Technical Crisis Communication

Crisis communication has been defined as “the strategic use of words and actions to manage information and meaning during the crisis process” (Coombs 2018, p. 1). Socio-technical crisis communication relates to consideration of psychological and social factors pertaining to the source/sender and recipients of messaging, possibly contextualized to disaster management stages, all as part of a dynamic, omni-channel, customized or personalized communication strategy. It extends the traditional mass communication/broadcast paradigm for crisis communication by intelligently optimizing the style, content, frequency, cadence, and delivery channels across disaster management stages for a robust crisis communication strategy (Valecha et al. 2013).

Facing severe crises, people’s perceptions and reactions tend to be amplified by technology that facilitates interactions, particularly as the result of complex psychological mechanisms dealing with fear and critical decision-making processes (Kasperson et al. 1988). In the current information age where social reactions are strongly shaped by user generated content, digital channels can support crisis responses as mechanisms for fastcirculating communication, news updates, and as means for reflecting public concerns (Rao et al. 2020, Jang et al. 2021). Crisis communication not originating from central agencies and disaster relief organizations (DROs) may also be susceptible to unverified and false information (Tran et al. 2021). In the changing policy landscape rife with erosion of public trust, echo chambers worsen the spread of online harmful misinformation (Avnur 2020, Cinelli et al. 2021, Tran et al. 2022). In light of the sixth characteristic of the Century of Disasters that highlights that DM has been affected by distrust in institutions, socio-technical crisis communication necessitates researchers to find root causes of distrust and develop effective communication mechanisms.

Disaster management agencies become local sources of information during emergencies. Although prior research, such as Hong et al. (2021), underscores the need for “understanding hyper-local disaster response as an important foundation for effective and equitable community planning and urban resilience strategies” (p. 2), current empirical research has not extensively explored the role of socio-technical systems for utilities and infrastructure service providers in achieving equitable disaster management. It is critical that such socio-technical communication consider reducing the inequitable impacts of disasters on historically disenfranchised populations as the communications are not accessible by all users (Cutts et al. 2015, Retzlaff 2020). In capturing the relationship between end users and the communication received from disaster management agencies during crisis situations, it is important that their communications are distributed in an equitable manner and as such are fairly accessed.

New socio-technical crisis communication research is also needed to consider communication context such as the severity, risks, uncertainty, and urgency of the involved decision-making processes (e.g., evacuations or vaccination decisions), gaps in knowledge and expertise of the communication recipients, and the impact of people’s emotions and perceptions (Andi and Akesson 2020). Communication strategies that consider both human-based and machine-based agents within the communication systems are needed (Tran et al. 2023), all while considering the role of smart technologies, platforms (e.g., digital humanitarianism), and AI-enabled proactive messaging. Moreover, socio-technical crisis communication research should examine the effect of twoway interactions between disaster management institutions and the affected public, an underexplored topic. Finally, user actions and responses to messaging are often constrained to microlevel digital engagement measures such as views, likes, and forwarding/retweets. It is important to identify the key drivers that can help institutions to mobilize concerned citizens to react and respond appropriately, beyond existing microlevel digital indicators. The current crisis communication paradigm is plagued with misaligned messaging, such as that observed during the 2021 Texas Winter Storm Uri (Terracciano and Han 2023). Four papers in this special section contribute to this research theme.

Mousavi and Gu (2024) highlight the importance of resilience messaging by community leaders during public health crises, providing both theoretical and practical contributions to the field of DM and crisis communication. Using an interesting language-model-based psychometric analysis approach, they found government leaders played a crucial role in communicating response strategies and that incorporating resilience content in leaders’ communications enhances effectiveness when addressing those affected by disasters, leading to greater community compliance.

Yoo et al. (2024) explore the dynamics of crisis communication by examining the coordination of social media content by DROs during disasters. The study underscores the importance of considering stages of the disaster management cycle, as well as intraorganizational coordination between central and local DRO agencies (i.e., organizational hierarchy), when adapting content coordination strategies for maximal engagement.

Yan et al. (2024) use a computational theoryconstruction framework to offer insights into how firms not directly involved with disasters should communi cate. Looking at an array of observed disasters, they identify competing dimensions such as internal versus external and stable versus flexible in disaster communication, generating latent categories and associations. The paper contributes to the socio-technical crisis communication literature by assessing firm-related content specifically in the context of various natural disasters, and providing insights into how firms can strategically design their messages on social media.

Finally, the aforementioned Ghose et al. (2024) examine the extent to which instant mobile DTAs affect people’s actions, the impact of private information in the messaging on actions, and user heterogeneity in effectiveness.

4.3. Predicting and Prescribing Under Uncertainty Uncertainty poses a significant challenge for decision making across emergency responders, firms engaged in emergency response, and individual decision makers. A key strategy for addressing this uncertainty involves acquiring more information, and modern technology plays a crucial role in facilitating data acquisition and modeling. AI-enabled early warning systems have the capacity to process historical data, climate patterns, and pertinent information to construct predictive models (Yabe et al. 2022). These models, in turn, prove invaluable in forecasting potential disaster events, estimating their magnitude, and identifying at-risk areas. Furthermore, planners can leverage optimization and simulation tools to model diverse disaster scenarios, refining response plans for increased resilience. One example at the forefront of this new TDM frontier of “predicting and prescribing under uncertainty” are disaster world models: AI-based decision-theoretic agents for simulating population responses to disasters (Pynadath et al. 2023). Key characteristics of disaster world models are socially plausible modeling of human behaviors based on subjective beliefs, incorporated into AI frameworks. Computational design research in IS holds significant promise as it involves crafting intricate socio-technical systems to proactively analyze and manage predictive and prescriptive scenarios across varying degrees of uncertainty. Two papers in this special section are contributing to this research frontier theme.

Zhang et al. (2024) address a critical aspect of disaster response; the management of disaster relief resources. The paper develops an effective predictive analytics deep learning method to consider the significant uncertainties in disaster response, coupled with a stochastic optimization model to determine the optimal quantity of resources based on both current unfulfilled and future demand. Their insights can help local disaster relief agencies design prediction-plus-prescription systems to guide decisions under uncertainty.

Suarez et al. (2024) address the central challenge in DM of making long-term, high-cost decisions under uncertainty. They emphasize the importance of rational evaluation of tradeoffs in managing risk at the societal level, highlighting the profound impacts on social, environmental, political, and economic aspects. The paper contributes to the design literature by developing a new decision support framework that can integrate decisions throughout different stages of disaster management for wildfires, facilitate forecasting decisions at the response stage through simulation, and determine adequate decisions at the preparedness stage through optimization. Their framework integrates predictive models that estimate future events, prescriptive models that determine the most suitable course of action, all under different uncertain scenarios.

4.4. Fair Pipelines: Alleviating Allocational Harm Historically, biases in forecasting and allocating resources for disaster prevention and response have manifested in various ways, often tied to social, economic, and systemic factors. Moreover, research on fairnessaware disaster management has been limited (Peacock and Girard 2012, Yang et al. 2020). One challenge for fairness in disaster management is that within the multistakeholder environment, while different stakeholders might agree on the general principle of social good, their exact goals and objectives might vary (Abbasi et al. 2019). More recent trends in TDM may increase the severity of biases manifesting across the stages of disaster management. The classic bias in computer systems literature examines preexisting biases in the data, stemming from social institutions, practices, and attitudes, technical biases arising from technical constraints, and emergent biases from context of use (Friedman and Nissenbaum 1996). More recently, with the injection of machine learning (ML) into multiple activities within a single decision process or system, the notion of fair pipelines, how to mitigate bias in such multiple ML modelbased systems/processes, has garnered attention (Lalor et al. 2024). One important category of fair pipelines for TDM are called cumulative decision pipelines, where predictions from upstream ML models are used as inputs for downstream allocational ML models. Such pipelines have a similar objective to the classic resource allocation fairness problem (Bertsimas et al. 2011), but in a multi-ML model environment.

The ability to effectively detect, measure, and mitigate bias in such fair pipelines is extremely challenging for three reasons (Lalor et al. 2024). First, interaction effects between protected attributes (e.g., age, race, gender, income) create numerous combinations for intersectional bias (Lalor et al. 2022). Second, multiple ML models in the pipeline add combinatorial amplification of bias cal culation across pipelines. Third, the lack of alignment between upstream representational harm and downstream allocation harm makes it harder to anticipate a priori the extent to which a given allocation is unfair (Lalor et al. 2024). Given disasters have a disproportionately greater impact on those most vulnerable in society, these difficulties in realizing fair pipelines are further enlarged in TDM settings. For instance, in the recovery phase of a disaster, resources have not historically been distributed equally, with Hurricane Katrina being an example where the poorest areas faced challenges accessing essential supplies, such as food, water, and medical assistance (Pastor et al. 2006). A new wave of fair pipelines research is needed to alleviate allocational harm in TDM in an increasingly AI-enabled world. Three papers in this special section are contributing to this research frontier theme.

Zhang and Xu (2024) examine the fairness of ratemaking methods in catastrophe insurance, especially in the context of major disasters, to mitigate potential inequal ities. They use an axiomatic approach to illustrate the lack of fairness in catastrophe insurance, provide empiri cal evidence of disparate impact against racial minorities, and use parallels from fair data valuation in ML literature to design a computational tool that results in better fairness outcomes. The work demonstrates how forward looking TDM research can contribute to societal awareness by addressing biases and promoting fairness.

Liu et al. (2024) explore the positive impact of AI in disaster relief lending, addressing biases and contributing to a more equitable allocation of resources for postdisaster recovery. The paper acknowledges the financial distress inflicted by natural disasters on victims, emphasizing the surge in credit needs amongst those most vulnerable during such crises. Recognizing that loans are not readily available to everyone postdisaster, the paper explores the potential of AI-based credit scoring tools in identifying victims who would genuinely benefit from commercial loans. It underscores the potential of AI to assist in a fair and targeted manner, particularly in supporting the financial recovery of underprivileged com munities affected by natural disasters.

The aforementioned Zhang et al. (2024) introduce an advanced computational model that not only improves the efficiency of resource allocation in disaster response, but also integrates predictive and prescriptive analytics to ensure a fair and proactive approach. Their motivation lies in recognizing the critical nature of disaster response and the importance of managing relief resources effectively. The researchers introduce a novel deep learning method to proactively determine optimal quantities of requested resources, considering both currently unfulfilled and future demand. The emphasis on designing systems that consider the specific needs and challenges of disaster-affected communities aligns with the goal of mitigating biases and promoting equitable resource distribution in disaster management.

## 5. Conclusions

We present a framework that shows how various characteristics of the Century of Disasters influence the evolving TDM landscape, and how the convergence of disaster characteristics and technology trends drives the four presented research frontiers. The articles appearing in the special section signify an important first step in understanding important facets of the research frontiers. With disasters becoming increasingly more intense and pervasive and disaster management becoming ever more technology enabled, IS has an important role to play in research on preparedness and response in the Century of Disasters. Our hope is that this special section will be a conversation-starting catalyst for future IS research on this important topic.

## Acknowledgments

The authors thank Alok Gupta, past editor-in-chief, who gave us the opportunity to develop this special section; all the associate editors and referees for their yeoman work in helping develop the special section; the Secure Knowledge Management (SKM) 2023 conference chair Raghu Santanam (ASU) and program chair Victor Benjamin (Arizona State University (ASU)) and the SKM 2021 conference co-chairs Ram Krishnan and H. R. Rao (University of Texas San Antonio) and program co-chairs Sagar Samtani (Indiana University) and Ziming Zhao (University of Buffalo) for coordinating workshops; and the PhD students who helped conduct the 2023 and 2021 workshops on Unleashing the Power of Information Technology for Strategic Management of Disasters: Shalini Kapali Kurumathur, Hrishitva Patel, Qian Wang, and Pranali Mandaokar, Paras Bhatt (University of Alabama at Huntsville), Bingyi Wu, Thi Tran (Binghamton University), Oluwafemi Akanfe (University of Alabama at Birmingham), and Captain Alexis Votto (U.S. Air Force).

## References

Abbasi A, Dillon-Merrill R, Rao HR, Sheng O, Chen R (2021) Call for papers—Special issue of Information Systems Research— Unleashing the power of information technology for strategic management of disasters. Inform. Systems Res. 32(4):1490–1493.

Abbasi A, Li J, Adjeroh D, Abate M, Zheng W (2019) Don’t mention it? Analyzing user-generated content signals for early adverse event warnings. Inform. Systems Res. 30(3):1007–1028.

Achenbach J (2011) The century of disasters. Washington Post (May 16), https://www.washingtonpost.com/blogs/achenblog/post the-century-of-disasters/2011/05/16/AFzy6m4G\_blog.html.

Andi S, Akesson J (2020) Nudging away false news: Evidence from a social norms experiment. Digital Journalism 9(1):106–125.

Avnur Y (2020) What’s wrong with the online echo chamber: A motivated reasoning account. J. Appl. Philosophy 37(4):578–593.

Bago B, Rand DG, Pennycook G (2023) Reasoning about climate change. PNAS Nexus 2(5):pgad100.

Bertsimas D, Farias VF, Trichakis N (2011) The price of fairness. Oper. Res. 59(1):17–31.

Betsch C, Korn L, Sprengholz P, Felgendreff L, Eitze S, Schmid P, Bo¨hm R (2020) Social and behavioral consequences of mask policies during the COVID-19 pandemic. Proc. Natl. Acad. Sci. USA 117(36):21851–21853.

Beydoun G, Abedin B, Merigo ´ JM, Vera M (2019) Twenty years of information systems frontiers. Inform. Systems Frontiers 21: 485–494.

Can˜ avera-Herrera JS, Tang J, Nochta T, Schooling JM (2022) On the relation between ‘resilience’ and ‘smartness’: A critical review. Internat. J. Disaster Risk Reduction 75:102970.

Cinelli M, Morales GDF, Galeazzi A, Quattrociocchi W, Starnini M (2021) The echo chamber effect on social media. Proc. Natl Acad. Sci. USA 118(9).

Coombs TW (2018) Crisis communication. Gephart RP Jr, Miller CC Helgesson KS, eds. The Routledge Companion to Risk, Crisis, and Emergency Management (Routledge, New York), 51–66.

COVID Tracking Project (2021) Accessed March 15, 2024, https:// COVIDtracking.com/about.

Cutts BB, Sinclair KM, Strauch MA, Slivnick B, Emmons Z (2015) Environmental justice and emerging information communication technology: A review for U.S. natural disaster management. Environ. Justice 8(4):144–150.

Department of Energy (DOE) (2024) Electric disturbance events. Accessed March 1, 2024, https://www.oe.netl.doe.gov/oe417 aspx.

Department of Homeland Security (DHS) (2015) National preparedness goal. Accessed March 1, 2024, https://www.fema.gov sites/default/files/2020-06/national\_preparedness\_goal\_2nd\_ edition.pdf.

Devidal P (2023) ‘Back to basics’ with a digital twist: Humanitarian principles and dilemmas in the digital age. Humanitarian Law & Policy (February 2), https://blogs.icrc.org/law-and-policy/wpcontent/uploads/sites/102/2023/02/%E2%80%98Back-to-basicswith-a-digital-twist\_-humanitarian-principles-and-dilemmas-in the-digital-age-Humanitarian-Law-Policy-Blog.pdf.

Elinder M, Erixson O (2012) Gender, social norms, and survival in mari time disasters. Proc. Natl. Acad. Sci. USA 109(33):13220–13224

Francis R, Bekera B (2014) A metric and frameworks for resilience analysis of engineered and infrastructure systems. Reliabilit Engrg. Systems Safety 121:90–103.

Friedman B, Nissenbaum H (1996) Bias in computer systems. ACM Trans. Inform. Systems 14(3):330–347.

Ghose A, Lee HA, Oh W, Son Y (2024) Leveraging the digital tracing alert in virus fight: The impact of COVID-19 cell broadcast on population movement. Inform. Systems Res. 35(2):570–589.

Hong B, Bonczak BJ, Gupta A, Kontokosta CE (2021) Measuring inequality in community resilience to natural disasters using large-scale mobility data. Nature Comm. 12(1):1870.

Hou J, Liang C, Chen P-Y, Gu B (2023) Can telework adjustment help reduce disaster-induced gender inequality in job market outcomes? Inform. Systems Res., ePub ahead of print December 11 https://doi.org/10.1287/isre.2023.0241.

Jang H, Rempel E, Roth D, Carenini G, Janjua NZ (2021) Tracking COVID-19 discourse on Twitter in North America: Infodemiology study using topic modeling and aspect-based sentiment analysis. J. Medical Internet Res. 23(2):e25431.

Kasperson RE, Renn O, Slovic P, Brown HS, Emel J, Goble R, Kasperson JX, et al. (1988) The social amplification of risk: A conceptual framework. Risk Anal. 8(2):177–187.

Kumar A, Joshi S, Sharma M, Vishvakarma N (2022) Digital humanitarianism and crisis management: An empirical study of ante cedents and consequences. J. Humanitarian Logist. Supply Chain Management 12(4):570–593.

Kundzewicz ZW, Hegger DLT, Matczak P, Driessen PPJ (2018) Flood-risk reduction: Structural measures and diverse strategies. Proc. Natl. Acad. Sci. USA 115(49):12321–12325.

Lalor JP, Abbasi A, Oketch K, Yang Y, Forsgren N (2024) Should fairness be a metric or a model? A model-based framework for assessing bias in machine learning pipelines. ACM Trans. Inform. Systems. 42(4):1–41.

Lalor JP, Yang Y, Smith K, Forsgren N, Abbasi A (2022) Benchmarking intersectional biases in NLP. Proc. 2022 Conf. North American Chapter Assoc. Comput. Linguistics Human Language Technologies (Curran Associates, Red Hook, NY), 3598–3609.

Liu Y, Li X, Zheng Z(E) (2024) Smart natural disaster relief: Assisting victims with artificial intelligence in lending. Inform. Systems Res. 35(2):489–504.

Mousavi R, Gu B (2024) Resilience messaging: The effect of gover nors’ social media communications on community compliance during a public health crisis. Inform. Systems Res. 35(2):505–527.

NOAA (2024) National Centers for Environmental Information. Accessed March 1, 2024, https://www.ncei.noaa.gov/access/billions/.

Ohenhen LO, Shirzaei M, Barnard PL (2024) Slowly but surely: Exposure of communities and infrastructure to subsidence on the US east coast. PNAS Nexus 3(1):pgad426.

Oktari RS, Munadi K, Idroes R, Sofyan H (2020) Knowledge management practices in disaster management: Systematic review. Internat. J. Disaster Risk Reduction 51:101881.

Park S (2022) The politics of 21st century environmental disasters. Environ. Politics 31(1):1–7.

Pastor M, Bullard R, Boyce JK, Fothergill A, Morello-Frosch R, Wright B (2006) Environment, disaster, and race after Katrina. Race Poverty Environment 13(1):21–26.

Peacock WG, Girard C (2012) Ethnic and racial inequalities in hurricane damage and insurance settlements. Hurricane Andrew (Routledge, New York), 171–190.

Pynadath DV, Dilkina B, Jeong DC, John RS, Marsella SC, Merchant C, Miller LC, et al. (2023) Disaster world: Decision-theoretic agents for simulating population responses to hurricanes. Comput. Math. Organ. Theory 29(1):84–117.

Rao HR, Vemprala N, Akello P, Valecha R (2020) Retweets of officials’ alarming vs reassuring messages during the COVID-19 pandemic: Implications for crisis management. Internat. J. Inform. Management 55:102187.

Retzlaff KJ (2020) Water utility communications can build trust during the COVID-19 pandemic. J. Amer. Water Works Assoc. 112(8): 24–31.

Sarker S, Whitley EA, Goh K-Y, Hong Y(K), Ma¨hring M, Sanyal P, Su N, et al. (2023) Some thoughts on reviewing for information systems research and other leading information systems journals. Inform. Systems Res. 34(4):1321–1338.

Suarez D, Gomez C, Medaglia AL, Akhavan-Tabatabaei R, Grajales S (2024) Integrated decision support for disaster risk management: Aiding preparedness and response decisions in wildfire manage ment. Inform. Systems Res. 35(2):609–628.

Taleb NN (2010) The Black Swan: The Impact of the Highly Improbable, 2nd ed. (Random House, New York).

Terracciano E, Han AT (2023) Twitter communication during winter storm Uri in San Antonio, Texas-Implications for climate resiliency planning. Cities 139:104407.

Tran T, Valecha R, Rao HR (2022) Health-related misinformation harm during the COVID-19 pandemic: An investigation of non comparative and comparative harm perceptions. AIS Trans Human-Comput. Interactions 14(2):185–206.

Tran T, Valecha R, Rao HR (2023) Machine and human roles for mitigation of misinformation harms during crises: An activity theory conceptualization and validation. Internat. J. Inform. Management 70:102627.

Tran T, Valecha R, Rad P, Rao HR (2021) An investigation of misinformation harms related to social media during two humanitarian crises. Inform. Systems Frontiers 23(4):931–939.

US Geological Survey (USGS) (2024) How can climate change affect natural disasters. Accessed March 1, 2024, https://www.usgs. gov/faqs/how-can-climate-change-affect-natural-disasters.

Valecha R, Sharman R, Rao HR, Upadhyaya S (2013) A dispatch mediated communication model for emergency response systems. ACM Trans. Management Inform. Systems 4(1):1–25

Wever M, Shah M, O’Leary N (2022) Designing early warning systems for detecting systemic risk: A case study and discussion. Futures 136:102882.

World Economic Forum (2020) The global risks report. Accessed March 1, 2024, http://www3.weforum.org/docs/WEF\_Global\_Risk\_Report\_ 2020.pdf.

Yabe T, Rao PSC, Ukkusuri SV, Cutter SL (2022) Toward datadriven, dynamical complex systems approaches to disaster resilience. Proc. Natl. Acad. Sci. USA 119(8):e2111997119.

Yan B, Mai F, Wu C, Chen R, Li X (2024) A computational framework for understanding firm communication during disasters. Inform. Systems Res. 35(2):590–608.

Yang YC, Ying H, Jin Y, Cheng HK, Liang TP (2021) Special issue editorial: Information systems research in the age of smart services. J. Assoc. Inform. Systems 22(3):10.

Yang Y, Zhang C, Fan C, Mostafavi A, Hu X (2020) Toward fairness-aware disaster informatics: An interdisciplinary perspective. IEEE Access 8:201040–201054.

Yoo C, Yoo E, Yan L(L), Pedraza-Martinez A (2024) Speak with one voice? Examining content coordination and social media engagement during disasters. Inform. Systems Res. 35(2):551–569.

Zhang N, Xu H (2024) Fairness of ratemaking for catastrophe insurance: Lessons from machine learning. Inform. Systems Res. 35(2):469–488.

Zhang H, Zhao X, Fang X, Chen B (2024) Proactive resource request for disaster response: A deep learning-based optimization model. Inform. Systems Res. 35(2):528–550.

Zheng F, Westra S, Leonard M, Sisson SA (2014) Modeling dependence between extreme rainfall and storm surge to estimate coastal flooding risk. Water Resources Res. 50(3):2050–2071.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>
