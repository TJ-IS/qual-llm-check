---
otero_id: 25806
otero_key: "K33J8C8V"
title: "Do‐it‐yourself as a means for making assistive technology accessible to elderly people: Evidence from the ICARE project"
authors: "Tobias Mettler; Stephan Daurer; Michael A. Bächle; Andreas Judt"
year: "2023"
journal: "Information Systems Journal"
doi: "10.1111/isj.12352"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
S P E C I A L I S S U E P A P E R

# Do-it-yourself as a means for making assistive technology accessible to elderly people: Evidence from the ICARE project

Tobias Mettler<sup>1</sup> | Stephan Daurer<sup>2</sup> | Michael A. Bächle<sup>2</sup> | Andreas Judt<sup>3</sup>

<sup>1</sup>Swiss Graduate School of Public Administration, University of Lausanne, Lausanne, Switzerland

<sup>2</sup>Department for Management Information Systems, Baden-Wuerttemberg Cooperative State University Ravensburg, Ravensburg, Germany

<sup>3</sup>Department for Informatics, Baden Wuerttemberg Cooperative State University Ravensburg, Friedrichshafen, Germany

## Correspondence

Tobias Mettler, Swiss Graduate School of Public Administration, University of Lausanne, Rue de la Mouline 28, 1022 Chavannes-près-Renens, Switzerland. Email: tobias.mettler@unil.ch

## Abstract

New assistive technology (AT) is at our disposal for improving the everyday life of people in need. Yet, the current way how AT is produced and provisioned is hindering certain marginalised groups in the population, particularly elderly people, to get access to it. To expedite time-to-market, reduce costs, and increase accessibility to otherwise unattainable AT, we explore if do-it-yourself (DIY) could be a feasible and desirable alternative to commercial applications. We provide answers to the following research questions: (1) For whom does the DIY approach work in the context of assistive technology? (2) Under which circumstances do DIY work? and (3) How can researchers make DIY a satisfying experience? The evidence we collected during the “iCare” project suggests that DIY attracts both, elderly people with a need-based motive and a hedonic motive. It also shows that a participatory approach and an early engagement with potential users, their family members, and informal caregivers is beneficial for improving design and use-related aspects of the AT and the DIY intervention.

K E Y W O R D S

democratisation of IT, design research, do-it-yourself, home care,

remote health monitoring systems

## 1 | INTRODUCTION

Due to the demographic change that developed countries are facing in the next decades, the cure and care of elderl people have become a prominent theme in the political agenda-setting and decision-making (Ho et al., 2019). In fact, providing health services to a rapidly aging population with fewer resources has grown into one of the grand chal lenges of this century (U.S. National Academy of Medicine, 2021). Building upon this premise, about 30% of tota U.S. health care expenditures are attributed to the adoption and renewal of health information technology (HIT) (Pearson & Frakt, 2018). Similarly, in Western Europe, the spending for modernising HIT infrastructures has grown from \$13.2 billion in 2013 to \$14.6 billion in 2018 and are forecast to grow in the upcoming years to respond to new demands presented by the COVID-19 pandemic (IDC, 2020). Besides investments in proven technologies, a multitude of research programs have been launched, such as the Active and Assisted Living (AAL) program of the European Commission (2021a), to discover and pilot new technology-reliant solutions that increase the quality of life, autonomy, or social participation of elderly people (van Grootven & van Achterberg, 2019). Such initiatives hav considerably rushed the development of forward-looking assistive technologies (AT) which, in this paper, we under stand as any piece of equipment, device, or system, whether acquired off-the-shelf, self-built or customised, that is used to increase, maintain, or improve functional capabilities of a person with a disability

However, the resulting AT products and services have not always reached the ones in need (World Healt Organization, 2021). Reasons for that are manifold. The release of funds of big research programs is usually organised as a competitive project selection process. The amount of time and effort to prepare a convincing project proposal is significant, which has frequently prevented small and medium-sized companies (SME) or smaller researc groups to take part in this contest and has favoured larger research groups and private-public-partnerships, coordinated by big multi-national corporations, instead. As priority is given to projects that promise bold solutions or pledge to address many policy goals at a time, overpromising has been common (Charette, 2005) and, as a result, the developed AT products either insufficient or too complicated for actual patients, family members, or caregivers (Karunanithi, 2007; van den Kieboom et al., 2019). Requiring an advanced technical setup and extensive training before using the AT for the first time (Olsson et al., 2012; Unbehaun et al., 2020) has particularly discouraged les tech-savvy or financially disadvantaged elderly people (Borg et al., 2011; Pethig & Kroenung, 2019). Furthermore many new AT products need to undergo a complex, lengthy, and costly approval process before entering the highly regulated market of medical devices (European Commission, 2021b; U.S. Food & Drug Administration, 2021). On th positive side, this has led to highly reliable product and service designs and improved patient safety (Emanue et al., 2008). But it equally increased administration, production costs, and time to market, making it difficult fo SMEs and smaller research groups to share their inventions

In this paper, we, therefore, want to explore if a do-it-yourself (DIY) approach is suitable for disseminating AT. DIY is an established concept, known primarily from the home improvement and makers scene (Anderson, 2012). However, since costs for most technical components have been declining, it has also found it way into different areas of healthcare (Carrera & Dalton, 2014; Hurst & Tobias, 2011; Jennings & Hussain, 2020) We are interested if such an approach could be an alternative to expensive commercial products so that elderly peo ple, their families, and caregivers get timely access to new, yet affordable AT products. We seek to provide an answer to the following research questions: (1) For whom does the DIY approach work in the context of assistive technology? (2) Under which circumstances do DIY work? and (3) How can researchers make DIY a satisfying experience?

The remainder of this paper is organised as follows. In the next section, an analysis of extant research is undertaken to clarify key concepts and to define a set of meta-requirements for AT products suitable for DIY. Thereafter we describe our research strategy and exemplify the DIY approach based on the solutions we developed during th so-called “iCare” project. We then present the findings we obtained from a one-week field trial and a maker work shop we organised for elderly people. We conclude by discussing the limitations and possibilities for future researc and the practical relevance of our results

## 2 | BACKGROUND

## 2.1 | Assistive technology and the elderly

Over the past 30 years, ‘assistive technology’ (AT) has been a common term used by the scientific and practice community, mostly in the United States (Galvin, 1990), to refer to any kind of ‘aids,’ ‘community equipment,’ or ‘housing adaptations,’ which have been the terms used more regularly in Europe (Tinker, 2003). Broadly speaking, AT can b defined as any device or system that allows an individual to perform a task that they would otherwise be unable to do, or increases the ease and safety with which the task can be performed” (Cowan & Turner-Smith, 1999, p. 325) According to McCreadie and Tinker (2005) such a definition of AT embodies a social model of disability,<sup>1</sup> which recognises that older people's disability arises from the interaction between their physical and mental capacities and th environment, especially their housing. Similarly, the US Technology-Related Assistance Act of 1988 (often referred to as the Tech Act ) highlights that the main purpose of AT is to increase, maintain or improve functional capabili ties of individuals with cognitive, physical or communication disabilities and adds that given an individual's circum stances and housing conditions AT can be “acquired commercially, off the shelf, modified or customized.” Although the development of AT by one's own effort is not explicitly stipulated, it nevertheless recognises that AT may possi bly require a contextual adaptation or alteration to function properly. Therefore, many solutions have either inte grated some sort of customization (Gibson et al., 2019; Wessel et al., 2019) or have tried to anticipate the needs of a specific target group, such as young adults (Newman et al., 2017) or the elderly (Albina & Hernandez, 2018), respec tively of specific health conditions like dementia (Bächle et al., 2018), autism (Cassidy et al., 2016), or cerebral palsy (Preston et al., 2016) to mention just a few.

Gibson et al. (2016) emphasise that AT must not only refer to high-tech equipment, such as digital persona assistants, remote health monitors, miniature hearing aids, or sensor-based fall detectors, but may also include low tech devices such as walking sticks, special door handles, or fitted furniture or cooking utensils, as long as they help with activities of daily living or promote activity and enjoyment. However, as Greenhalgh et al. (2012) noted, in recent years the implementation of AT has been determined by a modernist and rationalist discourse in many countries which has propagated a shift of responsibility for care from the state to the individual, and from healthcare insti tutions to people's homes (Langstrup, 2013) and, as a result, favoured the use of advanced technologies, like th Internet of Things (Hollier & Abou-Zahra, 2018), smart homes (Lê et al., 2012), wearables (Mettler & Wulf, 2019), o social robots (Gongora Alonso et al., 2019), as opposed to cheaper low-tech solutions.

This has particularly been problematic for elderly people due to their lower economic income (Mohd et al., 2018 and lower familiarity with digital technologies (Niehaves & Plattfaut, 2014). Mao et al. (2015) state that high-tech AT solutions, because of their advanced functionalities and customizability, are frequently too hard to use for older peo ple. However, it was found that the usability of new AT has not only been problematic for the elderly but also for family members and caregivers (Karunanithi, 2007; Olsson et al., 2012). While most designers, engineers, and inven tors of AT products have understood the importance of inclusive, human-centered design, there still is a deep-rooted conceit that “not all potential consumers can visualize a product until they can try it out and use it for a span of tim in the natural environment” (Smith et al., 2018, p. 478). This ‘urge to be innovative’ manifests itself, among others, in the use of a myriad of sensors, actuators, and other hardware, reducing the odds of an AT product at a reasonable cost (Chan et al., 2008; Mao et al., 2015), and a constant information overflow caused by triggered alert messages or flashy dashboards trying to visualise the entirety of collected data from all that hardware (Evans et al., 2011; Meiland et al., 2014). Olsson et al. (2012) report that it is therefore not uncommon that elderly people, family members, o caregivers require considerable training before using an AT for the first time. Such an investment in terms of tim and money reduces the chance that the people involved in the care of the older person promote and support the us of the solution. Hurst and Tobias (2011) found that 35% or more of AT products, respectively 8% for life-saving devices, end up unused or abandoned.

McCreadie and Tinker (2005) state that the decision whether to use an AT or not is not only dependent on the above-mentioned ‘utility calculus’ concerning benefits and costs, but also whether the older person feels that the use of the device either supports or undermines his/her sense of personal identity. Many AT fail to take an indi vidual's personality and emotional state into account (Burmeister, 2016). Several studies have shown that AT based on intrusive technologies, such as body-worn GPS tracker (McShane, 2013), may not only limit an older person's mobility but also lead to stigmatisation because of the conspicuity of AT since the user is clearly marked as disabled or ‘debilitated’ (Lotfi et al., 2012; Robinson et al., 2009). Table 1 summarises the identified problems found in th extant literature and displays AT meta-requirements and possible resolution strategies

## 2.2 | Do-it-yourself for producing and provisioning AT

The majority of the extant literature on AT has centred on questions related to the design and use of solutions fo specific settings or health conditions. To a much lesser extent research has emphasised the fact that access to AT products, either because of their high price or educational prerequisites, is often out of reach for certain groups of people, particularly the elderly. McCarthy et al. (2013) report that companies developing innovative AT solutions commonly play on their first-mover advantage to create lock-in effects which do not always necessarily favour the best technology or service for users. Gibson et al. (2019) criticise that a market-driven approach creates “passive consumers with ‘need’ being defined by those providing technology rather than those receiving them”. Being the result of a century-long ‘codification’ of best practices, Smith et al. (2018) state that production, deployment, and support all occur within and under the control of one company or a tightly coordinated network of companies. Older people, family members, or caregivers have only limited influence in the process. More so, Lane (2015) argues that certain groups will be ignored completely given that the economic incentives for companies to invest in new or improved AT products for small or niche markets are marginal and regulatory requirements or reimbursement poli cies often additionally reduce their return on investment.

T A B L E 1 Identified problems with corresponding meta-requirements and resolution strategies

<table><tr><td>Identified problem</td><td>Meta-requirement</td><td>Possible problem resolution</td></tr><tr><td>Technology-centeredness</td><td>Inclusive, human-centered design</td><td>Older person, family members, and caregivers should be the centre of attention, not technology</td></tr><tr><td>Affordability</td><td>Open design of software and hardware</td><td>Building upon open software and standard hardware components to reduce costs and increase integration</td></tr><tr><td>Usability and training effort</td><td>Lean design and harnessing existing skills and tools</td><td>Using a user interface that is already known by the people involved in the care environment</td></tr><tr><td>Cognitive overload and information overflow</td><td>Simplified incident reporting and user interfaces</td><td>Limiting activity reports and alert messages to a minimum and allowing users to adjust the type and frequency of alerts</td></tr><tr><td>Stigmatisation</td><td>Non-intrusive design</td><td>Using only a few, standard components, which can easily be arranged in the rooms of an elderly person</td></tr></table>

Voices have become louder that ask for a re-thinking of the way how AT is produced and provisioned to move away from a consumer or economically-driven model, to a more social or humanistic model (Andrich, 2016; Cham akiotis et al., 2021). For many, do-it-yourself (DIY) has not only been an approach for describing self-driven, self directed amateur design carried out by or with end-users (Baldwin et al., 2019; Wolf & McQuitty, 2011) but it has also been framed as antithesis of prescribed design of the mass market and as a means to subvert and transcend cap italism (Atkinson, 2006; Holtzman et al., 2007). Different forms and notions of DIY, therefore, appear in the literature.

A view that has been popularised through a variety of media is that of DIY as a leisure activity in relation to home maintenance and improvement (Gelber, 1999). It comprehends DIY as a series of overlapping activities wit the purpose of making, tinkering, or tweaking some artefacts, particularly to bricolage and maintenance of the home In the context of AT, the motivation to carry out such activities may differ largely and be driven by economic neces sity (Aflatoony & Lee, 2020; Alharbi et al., 2020) or individual desire, such as for better controlling the aesthetics or programmability of devices (Hurst & Tobias, 2011; Woo & Lim, 2015). The extent to which creativity is required in DIY may also differ and range from being a highly creative process to simple assembly according to a predefined plan.

In this paper, we comprehend DIY as a phenomenon that goes beyond the ‘creation of things’ (Atkinson, 2006 as it opens up previously preconceived thinking patterns—like the idea that AT should be designed by professionals only—and therefore has the potential to democratise access to health services which otherwise would not be avail able (Carrera & Dalton, 2014). Holtzman et al. (2007) argue that DIY particularly helps marginalised groups of societ to re-approach power in a non-alienating, self-organised and purposely anti-capitalist manner. Given that artefact are created for its use-value, rather than for its exchange-value, it not only undermines the imposition of work that underlies the consumer or economically-driven model of producing and provisioning AT, but also sets the message that we can change the world and escape from the idea that there is no alternative. Matzat and Sadowski (2012 argue that DIY is also a way to reduce ‘digital inequality’ as trial-and-error learning enhances digital skills. Aflatoony and Lee (2020) expand on this idea and add that, if DIY is organised as a collaborative learning workshop betwee users, designers, and health experts, it may generate knowledge about situations, user needs, lifestyles, and priorities unknown or unanticipated by the AT developers and, as a result, reduce task-technology misfit. For sure, not all users will be able to perform DIY activities or participate in ‘maker workshops’ (Aflatoony & Lee, 2020). In such a case, Slegers et al. (2020) suggest adopting ‘do-it-for-others’ (DFO) instead and involve informal caregivers, volunteers, or family members to create the AT product for the person in need

## 3 | RESEARCH DESIGN AND METHODS

We have opted for an interventionist research strategy to explore if DIY is a feasible and desirable approach for pro ducing and provisioning AT products. Following Breu and Peppard (2003) interventionist research includes any form of inquiry that is committed to the implementation of research results in a cooperative and/or participatory manner Rather than placing the practitioner, or as in our case the older person, at the receiving end of the knowledge crea tion process, interventionist research recognises the capacity of laypersons for knowledge creation. Dumay (2010 states that, while interventionist research can have different labels such as action research, clinical research, ‘design science’ or ‘constructive research,’ a common denominator to all of these approaches is that they integrat theory and practice as well as combine reflection and action. The core advantage is the possibility to collect more subtle and significant data allowing researchers to iteratively cycle between action-oriented and more reflectiv activities, exploring experiences from diverse perspectives, developing alternative solutions and interpretations, and testing different forms of action

Consisting of a team of four researchers with varying disciplinary backgrounds (i.e., information systems, soft ware engineering, e-health, economics, and ethics), in fall 2014, we started a project called “iCare” with the aim to collaboratively design AT products, more specifically remote health monitoring solutions, and subsequently dissemi nate the code—for free and without strings attached—together with detailed instructions for DIY. The project whic officially lasted until 2018, but informally still is active with a small installed user base and a series of presentations workshops, and website can roughly be divided into three phases, as illustrated in Figure 1.

The first phase of the project was concerned with ‘design’ and, thus, methodologically rooted in the principles of the sciences of the artificial (Simon, 1996). Following an iterative ‘build and evaluate’ logic (Hevner et al., 2004), we first launched a search process for mapping the problem space (i.e., “why are IT-reliant AT not common in the homes of older people?”) with the solution space (i.e., “what characteristics do AT products have?”). In reviewing the extant literature on AT, and specifically those addressing elderly users, we derived a set of meta-requirements (Walls et al., 1992), as we presented in Table 1. Since one member of the researcher team has a family member who requires increased care and aid, we had pre-existing relations and access to regional nonprofit care associations, sup port groups, and home care institutions with which we could discuss and validate our design hypotheses. Stepping out from the lab to the field helped us to broaden our view and to prioritise functionalities of the AT prototype to b developed. This exchange also facilitated the recruitment of caregivers and elderly people interested in testing earl versions of our prototype which, as shown in other studies (Martin et al., 2013; Meiland et al., 2014; Robinso et al., 2009), proved to be essential for improving usability.

The second phase of the project was concerned with better understanding ‘use’ of the designed AT prod ucts. A particularly important intervention during the early stages of prototyping, was a one-week field tria which we conducted in spring 2017 at the home of an elderly couple, both over 75 years old (the female participant was in good health, while the male participant was diagnosed with early-stage dementia). Using a passive, or non-participant observation approach (Luna-Reyes et al., 2005; Nandhakumar & Jones, 1997), the goa was to see “in the real world” how elderly users interact with the designed AT products on a day-to-day basis and if the installation and configuration procedure is practical enough so that either the older person herself or an informal caregiver or family member can put the proposed AT solution design into operation. The field trial allowed us to identify and reflect on many practical problems, such as what happens if users accidentally unplug the device from the power source or what happens when users move from the indoor to the outdoor environment.<sup>2</sup> In addition, it stimulated our thinking about intended and unintended uses of AT (Mettler, 2018) and led to us some anecdotal evidence concerning artefact emergence (Sein et al., 2011), as we discuss later.

![](/api/attachments/K33J8C8V/fulltext/images/e59fea02b39c4ed087271f6b63f41f67e294839a17f8296ecb92d6b3a668f603.jpg)  
F I G U R E 1 Chronology of research activities and interventions

The third phase, which is the main focus of this paper, was dedicated to exploring if our AT products ar not only usable but also ‘producible’ by older people. In fall 2018, we, therefore, organised a so-called ‘maker workshop’ (Aflatoony & Lee, 2020; Slegers et al., 2020) for testing whether our target user group is capable of assembling and setting up our designed AT solutions autonomously by simply following the building plan which we documented in a handbook and captured in short, step-by-step video clips. In this sense, the nature of DIY was rather an assembly than creative activity. Based on referrals from a non-profit association related to the education and care of elderly people, we invited 18 independent testers to take part in this workshop The age of the participants ranged between 42 and 79, respectively 67.88 years on average (see Table 2). Th group was mainly composed of elderly people who wanted to build a remote health monitoring system (RHMS) for their personal use or for someone in their household. More than half of the group have never had any exposure to programming, rating their computer literacy to be the one of a ‘novice’ or ‘intermediate’ computer user. Four testers described themselves to be ‘experts’ in computing with some knowledge in programming.

The maker workshop kicked off with a short presentation about the “iCare” project and a brief explanation of the use cases and features of the designed AT products. All materials needed for developing our remote monitoring system were provided and outlined on tables. Without any detailed instruction, we then let the participants indepen dently assemble and configure their solution. While one researcher attentively observed and documented the scen by taking reflective field notes, another researcher responded to questions, if needed. A short questionnaire was sent out at the end of the maker workshop to collect some additional information concerning the DIY experience and us intention of the AT (see Appendix A).

T A B L E 2 Characteristics of testers participating in the maker workshop

<table><tr><td>Gender</td><td>Age</td><td>Marital status</td><td>Computer literacy</td><td>People to care for</td></tr><tr><td>Male</td><td>42</td><td>Unmarried</td><td>Expert</td><td>None</td></tr><tr><td>Male</td><td>52</td><td>Married</td><td>Intermediate</td><td>Personal use</td></tr><tr><td>Female</td><td>55</td><td>Divorced</td><td>Novice</td><td>Personal use</td></tr><tr><td>Male</td><td>66</td><td>Married</td><td>Intermediate</td><td>Personal use</td></tr><tr><td>Female</td><td>68</td><td>Widowed</td><td>Novice</td><td>One person</td></tr><tr><td>Male</td><td>68</td><td>Married</td><td>Advanced</td><td>Personal use</td></tr><tr><td>Male</td><td>68</td><td>Married</td><td>Novice</td><td>None</td></tr><tr><td>Female</td><td>69</td><td>Partnership</td><td>Intermediate</td><td>One person</td></tr><tr><td>Male</td><td>69</td><td>Partnership</td><td>Expert</td><td>None</td></tr><tr><td>Male</td><td>69</td><td>Married</td><td>Intermediate</td><td>One person</td></tr><tr><td>Male</td><td>70</td><td>Married</td><td>Advanced</td><td>Personal use</td></tr><tr><td>Male</td><td>71</td><td>Married</td><td>Intermediate</td><td>One person</td></tr><tr><td>Male</td><td>72</td><td>Married</td><td>Intermediate</td><td>One person</td></tr><tr><td>Male</td><td>74</td><td>Married</td><td>Advanced</td><td>Two persons</td></tr><tr><td>Male</td><td>74</td><td>Married</td><td>Expert</td><td>Personal use</td></tr><tr><td>Male</td><td>77</td><td>Married</td><td>Expert</td><td>None</td></tr><tr><td>Male</td><td>79</td><td>Married</td><td>Intermediate</td><td>One person</td></tr><tr><td>Male</td><td>79</td><td>Married</td><td>Intermediate</td><td>None</td></tr></table>

## 4 | THE ICARE PROJECT

## 4.1 | AT solution components

Based on the regular exchange with and input we got from regional non-profit care associations, support groups, home care institutions, and elderly people, we developed three AT products. Our first component, which we named iCareBot (see Figure 2a), is conceived for the purpose of indoor remote monitoring, alerting caregivers in case of unusual activity (e.g., nocturnal wandering) or inactivity (e.g., caused by a fall or stroke). Given that people diagnose with early-stage dementia sometimes suffer episodes of aimless or disoriented ambulation throughout the house or residential neighbourhood, we designed DeSearch (see Figure 2b) to locate a person in a close environment. Base on the reactions we got after the one-week field trial, we recognised the necessity to determine more precisely if person has switched from the indoor to the outdoor environment, which is why we built the so-called ScanBot (se Figure 2c), to track more precisely if a person has left the building. Next, we explain the iCareBot in more detail, a we concentrated our DIY intervention on this AT component only.

Following the described meta-requirements, in particular lean design and (re-)use of standard hardware and open software, the iCareBot is a simple, yet powerful RHMS. Instead of developing the most advanced and custom solution possible, which typically comes with pricy hardware, we decided to use Raspberry Pi, a \$40 minicomputer of the size of a credit card running a Debian-based operating system (Raspberry Pi Foundation, 2021). As demon strated in prior research, the Raspberry Pi hardware has proven to be sufficiently reliable for smart home application (Jain et al., 2014), offers a good value for money (Duarte et al., 2016), and can easily be extended with specific onboard accessories like webcams or motion sensors. During the design phase, we have experimented with two different versions. The first design variation (see Figure 3 left side) is based on a Raspberry Pi 2 minicomputer and contains an integrated camera and motion sensor module. The second design variation of the iCareBot is based on a Raspberry Pi 3 minicomputer with on-board Wi-Fi, USB port, Bluetooth, and Ethernet, protected by a simple cas made out of grey plastic (see Figure 3 right side). This box (around 8 cm respectively 3 inches in length and width can be positioned anywhere in the home of an elderly person if there is a power supply nearby.

For motion detection, we use a \$40 battery-operated wireless sensor with ultra-low power consumption which can be placed anywhere in the room of the elderly person. This sensor can be programmed individually, for example for having a scheduled activation/deactivation (e.g., to be turned on only at night). This allows users to trigger alert messages for different use cases, such as sending a message to family members and caregivers in case there is no activity i the morning or when a person leaves home at unusual hours. We use a webcam—costing around \$20—for making photo or short videos triggered by a sensor event or upon request. This basic configuration of the iCareBot is easily expandabl by adding motion sensors, webcams, or other peripherals as it uses an open standard for connecting all the devices. While the integrated version is more compact, the second variant allows for more precise motion detection and higher qualit of pictures as the sensors and webcams can be placed at the exact right spot in the room

![](/api/attachments/K33J8C8V/fulltext/images/613c4e8c4b2ffefe678374ba900d45368dbe6e1a9ae3c0af639ba218c42219a7.jpg)  
(b) DeSearch Bluetooth-Button  
F I G U R E 2 Solution components developed during the iCare project [Colour figure can be viewed at wileyonlinelibrary.com]

![](/api/attachments/K33J8C8V/fulltext/images/c3157f28b97fe1647c19e6456e9518c73ebba9ccaf4a61e1444f65116d71a3af.jpg)

![](/api/attachments/K33J8C8V/fulltext/images/5877c3975acc5cec8471f8d98158e0c19071118ab6b2532a74d4d5f986ed64fc.jpg)  
F I G U R E 3 Left: Integrated version of the iCareBot based on raspberry pi 2. Right: iCareBot based on raspberry pi 3 with standalone motion sensor and webcam [Colour figure can be viewed at wileyonlinelibrary.com]

To avoid extensive onboarding training and given that many of our elderly testers were familiar with and regular users of messaging apps, we used Telegram Messenger (Telegram, 2020) as the interface for interacting with the iCareBot. We opted for this solution as it allows for end-to-end encrypted messaging, is free, open-source, has an extensive API, does not restrict the size of messages (so that longer videos can be transmitted), and runs on most common platforms (i.e., PC, Mac, Linux, iOS, Android, Windows Phone, and Ubuntu Touch). A key feature of th Telegram Messenger is the possibility to create a chatbot, which is a computer program that facilitates a humanmachine dialogue using written or natural spoken language (Klüwer, 2011). It often serves as an interface for trigger ing code by scanning for keywords within the messages. Such chatbots have already been purposefully applied in a variety of use cases in outpatient medicine and social care for senior citizens (Abashev et al., 2017; Atay et al., 2016 Tokunaga et al., 2017). Among other things, we use the chatbot for user management (see Figure 4 left side). Instead of lengthy and complicated installation routines, which usually come with a RHMS, the chatbot helps setting up the home environment. By sending a message to the chatbot, users can add a Wi-Fi network (using the command wif [ssid][user][password]), or assign a person to a list of alert recipients (using the command add [username]). Similarly an undesirable person can be removed from the care network (using the command del [username]). Additiona commands are available for modifying other settings, such as for testing the picture brightness of the webcam or for connecting other sensors that measure the heartbeats of the user

Besides setting up the technical environment, the most important functions of the chatbot is to send alert messages in case of certain events or incidents (see Figure 4 right side). At this stage, we can trigger notifications in cas of unusual activity (using the command active [start] [end]) or in case of unusual inactivity (using the command period [time interval]). Whether the motion sensors are set for detecting movement or react to idleness, the iCareBot dispatches a photo message to the Telegram Messenger including a timestamp and type of alarm (see Figure 4 right side). This message is received by all people in the defined care network, allowing them to quickly assess the situation to decide whether to send professional help or visit the person later. A particular use case that can be supported by the iCareBot is, for instance, protocolling the frequency of wandering during nighttime

![](/api/attachments/K33J8C8V/fulltext/images/ff1b86c452712c9790ad512e7e12c57ba121ec1bb3f23523a9870048df6c2509.jpg)  
F I G U R E 4 Left: List of commands to interact with chatbot. Right: Alert message sent by the iCareBot and displayed on the telegram messenger triggered by unexpected activity [Colour figure can be viewed at wileyonlinelibrary.com]

## 4.2 | DIY dissemination materials

In line with DIY underlying goal to ‘democratise’ access to new products and services (Carrera & Dalton, 2014), we published our code and all other materials on our website https://www.unil.ch/icare. Besides a technical description a shopping list (for the hardware part of the solution), and a visual handbook, we also made additional step-by-step video instructions for the assembly, configuration, and use of the iCareBot (see Figure 5). The same materials wer used during our maker workshop, which findings we discuss next.

## 5 | FINDINGS

## 5.1 | For whom does DIY work

In the literature, DIY is either presented as a hobby (Gelber, 1999) or as a transformative approach (Holtzman et al., 2007) with which it is possible to democratise access to products or services beyond reach. While in the cas of the former not much persuasion is needed to convince an elderly person to engage in bricolage activities, it might be different in the latter scenario since not everybody is open for or capable of handicraft work, especially when it comes to potentially lifesaving pieces of equipment, devices, or systems. This is why our initial research question aimed at exploring for whom does the DIY approach work in the context of AT.

![](/api/attachments/K33J8C8V/fulltext/images/a4107e1d045d4534eb6d7d714be6af0a4f9cda54f497afea152fe9433581642c.jpg)  
F I G U R E 5 Practical installation guide in the form of short videos [Colour figure can be viewed at wileyonlinelibrary.com]

As we found out, the participants of our maker workshop had varying motivations. On the one hand, we ha people participating because they were interested in AT either for themselves or because they had a family member at home requiring special attention. Although some of our testers were in an advanced age themselves, roughly 39% had to care for one or two relatives and 33% wished an AT for personal use. Because of a lack of viable and/o affordable alternatives in the market, for those participants our DIY solutions represented an alternative source of support to explore. On the other hand, the remaining 28% of our testers, some of them being retired engineers, had no immediate need for AT and participated in our maker workshop out of curiosity and joy in tinkering or tweaking technological artefacts. In this sense, we could determine two groups of elderly users: the ones driven by a need-based motive (Au et al., 2008), and the ones with a hedonic motive regarding DIY (Van der Heijden, 2004).

In line with Deci and Ryan (1980), and corroborated in several recent studies (James et al., 2019; Menard et al., 2017), our observations indicate that participants' self-determined motivation was influenced by their auton omy (i.e., the degree to which they engaged in DIY on their own desire), competence (i.e., the degree to which they think they can produce the desired outcomes), or relatedness (i.e., the degree to which they feel connected wit others). For example, testers who rated their computer literacy high or indicated some programming skills were in general more favourable toward DIY. Similarly, participants who expressed that the iCareBot helped them to better interact and improve their relations with the person in need of care, other informal caregivers, and family members were more positive. Overall, 58.8% of participants found DIY a suitable approach and indicated that they wil continue using the produced AT. The remaining 41.2% were indecisive but did not express any major concerns.

In summary, it appears that a strong motivating factor to engage in DIY is a personal need, but equally are curiosit and diversion. We found that elderly people who have the ability and joy to familiarise themselves with new things wer the ones we could reach best with our approach. This also explains why our testers' computer literacy was rather high fo this age group. If a participant was not tech-savvy, at least a family member or someone in their close environment was This suggests that having either a certain familiarity and competency with technology or a fallback person, who can hel in case of problems, is an important premise for elderly people to engage in self-organised AT development. But it als means that we might potentially miss those, who so far have shut themselves away from technology or who lack a tech-savvy reference person, which still is a considerable proportion of the elderly population.

## 5.2 | When does DIY work

There are a couple of additional factors which are crucial to making a participatory and engaging DIY experience meaningful for both, elderly people, and interventionist design researchers

First, DIY works when the underlying problem that technology tries to solve is relevant for the elderly person Arguing that one's solution increases health and safety is a good entry point for making people curious, yet it is not sufficient for increasing participation. We had to learn that trying to convince an elderly person to give it a shot due to the many benefits over commercially available solutions or of not having such a system at home was a wasted effort. Instead, we had to acknowledge the fact that relevance differs from the eye of the beholder. As was reporte in previous studies (McCabe & Innes, 2013; Meiland et al., 2014), frequent encounters with potential users, their family members, and informal caregivers early in the design process was not only useful to better understand th particular living circumstances and personal histories of elderly who prefer independent living rather than being institutionalised, but it also shed some light into what older adults and their environment need, the possible context of use, and other situational determinants influencing the acceptance of a DIY approach. This proofed to b extremely valuable when we had to decide on which design parameters to focus on (e.g., privacy versus safety, cost versus aesthetics, and ease-of-use versus customizability).

Second, DIY works when elderly people have realistic expectations. Previous research has shown that satisfaction with a technological artefact is shaped by several factors, such as ease of use, design aesthetics, and most importantl design-expectations fit (Lowry et al., 2015). More than 63% of testers rated the base functionality of our iCareBot to b above expected, 19% to exactly as expected, and only 18% stated that it was below their expectations. 31% of partici pants found that the iCareBot is very easy to use, respectively 57% that it is reasonably easy to use. Only 12% of partici pants stated that the usability could be improved. The vast majority of 93% of participants found that the costs for producing and maintaining the solution were reasonable and within their reach. However, DIY is not just about considerations related to the artefact design but equally about the instruction process (i.e., helping elderly people to master the assembly of the artefact) and ongoing support (i.e., helping them to overcome technical issues). While our testers generally appreciated the short step-by-step videos and handbook, some participants were dissatisfied that we could not pro vide 24 7 first-level support. Likewise many open source initiatives (Tufekci, 2019), we had to remind them on multipl occasions that, since our grassroots project relied mainly on volunteer labour, we could not offer the same service a commercial technology providers do and that they have to accept the fact that they need to assume a much highe personal responsibility as if they would have simply bought an off-the-shelf product

Third, related to what was just said, DIY works when elderly people abandon the idea of being passive consumers and take a more active role in managing their health. This means that they have to understand that DIY comes with some personal investment (e.g., intellectual engagement with technology, persuading family members and caregivers to take part in the process) as well as some potential nuisances (e.g., having to wait for getting technical support, immature design features). For sure, some elderly people might not be in the physical or mental condition or lack the necessary skills to build AT by themselves (see the previous sub-section). But there is also that post-war generation of elderly people who simply have become accustomed to the convenience that capitalism brings: With money one may not only acquire prod ucts and services, but also a certain “peace of mind”. This is somehow opposite to the DIY idea, which requires som “skin in the game” (Taleb, 2018), hence, not only financial but also an emotional investment. To our view, this is probably the most crucial factor because it is outside the sphere of influence of the research team

## 5.3 | How to make DIY a satisfying experience

As we outlined earlier, much of what is perceived to be relevant, serviceable, and satisfying is context and situation specific. Whereas for some elderly the activity of assembling and playing with technology could already be a satisfy ing experience, the satisfaction level of others might be rather determined by the extent to which DIY is capable of solving the specific real-world problems they are faced with in everyday life. It is therefore extremely difficult fo interventionist design researchers to content such a diverse group as of today's elderly population. Nevertheless, w found some rules of conduct and principles which proofed to be effective when engaging with them.

First, it is important to listen without prejudging or rashly dismissing any expressed concerns or novel ideas Sometimes elderly people participating in DYI can be astonishingly creative or interact with technology in fo designers unforeseen ways, up to the point of temporarily or even permanently developing workarounds for bypassing or overcoming some capability limitations of the solution (Alter, 2014; Ejnefjäll & Ågerfalk, 2019). In our case, the analysis of the use protocols of the one-week field trial showed us that the elderly couple had programmed the iCareBot not only to send messages in case of a noteworthy incident but to deliberately trigger alerts at a given point in time so that the members of their care network receive a regular photo message from them (in a similar way young people use SnapChat). This circumstance has led to some discussions if we need to develop filters or more contextualised and situated notifications (Boger & Mihailidis, 2011; Ghorbel et al., 2013) which would have required to store some personal settings but equally would have raised privacy concerns and complexity of DIY instructions. It is tempting to fix as many encountered day-to-day problems as possible or to satisfy the needs of particular person, but this also risks overburdening the others.

Second, when planning an intervention, such as a maker workshop, it is worthwhile to let some room for trial and-error (Matzat & Sadowski, 2012). Although our testers were comparatively tech-savvy for their age group, the found that having some “unplanned time” during the DIY instruction is propitious for their learning and fo developing self-reliance in case of future technical difficulties.

Third, if possible, try to equally involve and address the needs of family members, informal caregivers, and health professionals. Volunteers that support the elderly person are invaluable. However, we know relatively little about the will and conditions under which health professionals (Alharbi et al., 2020) and informal caregivers (Aflatoony & Lee, 2020) would be open to being engaged in producing AT for a patient or relative in need. For sure, utilitarian fac tors may overweigh the hedonic motives of DIY in a professional care setting. But it could equally be that allowing certain degree of creativity and increasing the fun factor could lead to higher long-term engagement and participation of, in particular, younger volunteers (Slegers et al., 2020). While our AT components allow a certain degree of creativity (e.g., case modding, programming of chatbot), we have not systematically explored what impacts different instruction formats, interactivity levels, design activities, etc. could have had on the experience and satisfaction wit DIY of the care environment.

Fourth, do not underestimate the way of communication. Avoiding technical or medical jargon is important when interacting with elderly people. On the other hand, speaking a simple language could be misinterpreted as inexperience or alienness when communicating with health professionals (Vaughn et al., 2018). Again, situationa understanding and contingent knowledge and action are key.

## 6 | CONCLUSION

According to World Health Organization (2014), it is expected that more than 2 billion people will need AT by 2030 And although the United Nations (2007) Convention on the Rights of Persons with Disabilities stipulates that al persons with all types of disabilities must enjoy all human rights and fundamental freedoms”, we will most probabl not achieve this goal anytime soon with the current consumer or economically-driven model around AT. In this paper, we therefore set out to investigate if DIY could be a feasible and desirable approach for producing and provisioning IT-reliant AT to expedite time-to-market, reduce costs, and improve usability and accessibility to other wise for elderly people unattainable technology. Our goal was not to replace certified, professionally manufactured medical devices, but rather to present a possible alternative, especially for those groups of society who lack the eco nomic resources or technical expertise to purchase and operate standard AT products currently available on the mar ket. We also wanted to show that DIY could be a vehicle for research groups, particularly those without interest or expertise in commercialising science, for transferring their knowledge and disseminating their solutions to practice

Our study certainly is not without limitations. With respect to the DIY intervention, we are aware of severa biases potentially impacting our observations. First, besides a small sample size of 18 testers only, the selection of participants for the maker workshop followed a purposive sampling strategy, as we relied on the referrals we got from a non-profit association related to the education and care of elderly people. Accordingly, the recruited testers might already have had positive, or not so positive, previous experiences with IT-reliant AT, which might have increased or lowered their expectations concerning the learning, affective, and physical outcomes of the DIY inter vention. More so, we intervened when a tester encountered problems or asked specific questions and, therefore, we were not always just neutral observers but had sometimes a facilitating or supporting role. Although this was rather an exception, which either indicates that our DIY instructions and AT products were clear and easy to follow or ou test group not necessarily representative for the broad mass of the elderly. Certainly, we could not fully control for all situational and contextual factors during the DIY intervention, which seems to be inherent in engaged forms of research (Haj-Bolouri et al., 2018; Rai, 2019; Van de Ven, 2007).

We are also aware that the generalizability of interventionist research is difficult (Davison et al., 2004) and the findings produced in such research projects are often indigenous, and culturally biased (Davison & Díaz Andrade, 2018; Lee & Baskerville, 2003). For sure, in some societies and communities, young and old living together in a multi-generation household is still the dominant life model. In this case, our idea to produce AT in a self organised way may seem useless, or maybe even absurd. Our research, hence, only makes sense for and reflects the needs of older people who wish to have an independent life at home or who cannot fall back on such socia structures.

Despite these limitations, we believe that the results of our study have significant implications for practice particularly for public policy. DIY, and similar ideas underlying grassroots projects not only address specific societa problems (Buntz, 2014) to which politics and economy have not developed an answer yet (either because of lobbying activities or lack of economic incentives for private companies to invest in small or niche markets) but also have a sig nalling effect that change is possible (Atkinson, 2006; Holtzman et al., 2007). Different from large policy-driven ini tiatives which envision ambitious and risky grand designs to justify public spending (Charette, 2005), bottom-up initiatives bear less risk and are, in most instances, better rooted in and more responsive to the needs of society. According to Hurst and Tobias (2011) they succeed more frequently in developing low-cost, custom-built artefacts based on principles of participatory design due to their limited funding available and/or capabilities of the involved participants. Since these projects are emergent and exploratory in nature, typically following a trial-and-errorlearning strategy, the risk of ‘unproductive’ investments is marginal compared to big research programs. This should encourage policymakers to also include such bottom-up initiatives in their political agenda. However, as reported by Windrum (2008), the interest to do so is minimal due to fewer possibilities to exert regulatory control, unknown collaboration structures, and limited prospects to obtain high media coverage.

For researchers, interventionist and engaged research also presents some risks. While it has proven to be usefu to create ‘real value’ for people, particularly in the healthcare context (Sherer, 2014), it lacks some well-defined and widely accepted standards for evaluating and presenting research findings, which might discourage certain scholars to follow this path. We would like to end this paper by motivating everyone to step outside the personal comfort zone of describing, analysing, and predicting, and to use one's knowledge about IT as a catalyst for addressing, or even fixing societal problems. The list of technological and social issues and challenges remains very long indeed With DIY we have just presented one concept, yet there are many, potentially more disruptive approaches and ideas with which IS researchers may generate a real-world impact.

## DATA AVAILABILITY STATEMENT

The data that support the findings of this study are openly available at https://www.unil.ch/icare/.

## ORCID

Tobias Mettler https://orcid.org/0000-0002-7895-7545

Stephan Daurer https://orcid.org/0000-0002-4972-1779

Michael A. Bächle https://orcid.org/0000-0002-9037-1889

Andreas Judt https://orcid.org/0000-0002-6406-6397

## ENDNOTES

<sup>1</sup> Also see the Convention on the Rights of Persons with Disabilities (United Nations, 2007) and the Global Cooperation on Assistive Technology (World Health Organization, 2014).

<sup>2</sup> The first problem was fixed by incorporating an uninterruptible power supply (UPS) module which delivers enough electricity to safely shut down the equipment and to inform family members and caregivers using an alert message when th device is deactivated. The second problem lead to the emergence of a new solution component, we named ScanBot which we present in the next section<sup>.</sup>

## REFERENCES

Abashev, A., Grigoryev, R., Grigorian, K., & Boyko, V. (2017). Programming tools for messenger-based Chatbot system orga nization: Implication for outpatient and translational medicines. BioNanoScience, 7(2), 403–407.

Aflatoony, L. & Lee, S. J. (2020). At makers: A multidisciplinary approach to co-designing assistive technologies by cooptimizing expert knowledge. Proceedings of the 16th Participatory Design Conference 2020, Manizales, Colombia 128–132.

Albina, E. M. & Hernandez, A. A. (2018). Assessment of the elderly on perceived needs, benefits and barriers: Inputs for the Design of Intelligent Assistive Technology. Proceedings of the 16th international conference on ICT and knowledge engi neering, Bangkok, Thailand, 1–10.

Alharbi, R., Ng, A., Alharbi, R., & Hester, J. (2020). "I am not an engineer": Understanding how clinicians design & alter assis tive technology. Proceedings of the 2020 CHI conference on human factors in computing systems, Honolulu, USA, 1–8.

Alter, S. (2014). Theory of workarounds. Communications of the Association for Information Systems, 34, 1041–1066

Anderson, C. (2012). Makers: The New Industrial Revolution. Random House.

Andrich, R. (2016). Re-thinking assistive technology service delivery models in the light of the UN convention. Proceedings of the international conference on computers helping people with special needs, Linz, Austria, 101–108

Atay, C., Ireland, D., Liddle, J., Wiles, J., Vogel, A., Angus, D., Bradford, D., Campbell, A., Rushin, O., & Chenery, H. J. (2016) Can a smartphone-based Chatbot engage older community group members? The impact of specialised content Alzheimer's & Dementia: The Journal of the Alzheimer's Association. 12(7). P1005-P1006

Atkinson, P. (2006). Do it yourself: Democracy and design. Journal of Design History, 19(1), 1–10

Au, N., Ngai, E. W., & Cheng, T. E. (2008). Extending the understanding of end user information systems satisfaction forma tion: An equitable needs fulfillment model approach. MIS Quarterly, 32(1), 43–66.

Bächle, M., Daurer, S., Judt, A., & Mettler, T. (2018). Assistive technology for independent living with dementia: Stylized facts and research gaps. Health Policy and Technology, 7(1), 98–111.

Baldwin, M. S., Hirano, S. H., Mankoff, J., & Hayes, G. R. (2019). Design in the public square: Supporting assistive technology design through public mixed-ability cooperation. Proceedings of the ACM on Human-Computer Interaction, 1–22

Boger, J., & Mihailidis, A. (2011). The future of intelligent assistive technologies for cognition: Devices under development to support independent living and aging-with-choice. NeuroRehabilitation, 28(3), 271–280.

Borg, J., Larsson, S., & Östergren, P. O. (2011). The right to assistive technology: For whom, for what, and by whom? Disabil ity & Society, 26(2), 151–167.

Breu, K., & Peppard, J. (2003). Useful knowledge for information systems practice: The contribution of the participatory paradigm. Journal of Information Technology, 18(3), 177–193

Buntz, B. (2014). How a doctor became an award-winning device inventor [Online]. http://www.qmed.com/mpmn medtechpulse/how-doctor-became-award-winning-device-invento

Burmeister, O. K. (2016). The development of assistive dementia technology that accounts for the values of those affected by its use. Ethics and Information Technology, 18(3), 185–198.

Carrera, P. M., & Dalton, A. R. (2014). Do-it-yourself healthcare: The current landscape, prospects and consequences. Maturitas, 77(1), 37–40.

Cassidy, S., Stenger, B., Van Dongen, L., Yanagisawa, K., Anderson, R., Wan, V., Baron-Cohen, S., & Cipolla, R. (2016). Expressive visual text-to-speech as an assistive Technology for Individuals with autism Spectrum conditions. Computer Vision and Image Understanding, 148, 193–200

Chamakiotis, P., Petrakaki, D., & Panteli, N. (2021). Social value creation through digital activism in an online health community. Information Systems Journal, 31(1), 94–119.

Chan, M., Estève, D., Escriba, C., & Campo, E. (2008). A review of smart homes—Present state and future challenges. Com puter Methods and Programs in Biomedicine, 91(1), 55–81.

Charette, R. N. (2005). Why software fails. IEEE Spectrum, 42(9), 42–49.

Cowan, D., & Turner-Smith, A. (1999). The role of assistive technology in alternative models of care for older people. In Royal commission on long term care (pp. 325–346). Stationery Office.

Davison, R. M., & Díaz Andrade, A. (2018). Promoting indigenous theory. Information Systems Journal, 28(5), 759–764

Davison, R. M., Martinsons, M. G., & Kock, N. (2004). Principles of canonical action research. Information Systems Journal, 14 (1), 65–86.

Deci, E. L., & Ryan, R. M. (1980). The empirical exploration of intrinsic motivational processes. In L. Berkowitz (Ed.), Advance in experimental social psychology (pp. 39–80). Academic Press.

Duarte, T., Piment\~ao, J. P., Sousa, P., & Onofre, S. (2016). Biometric access control systems: A review on technologies to improve their efficiency. Proceedings of the 2016 IEEE international power electronics and motion control conference, Varna Bulgaria. 795-800

Dumay, J. C. (2010). A critical reflective discourse of an interventionist research project. Qualitative Research in Accounting & Management, 7(1), 46–70.

Ejnefjäll, T., & Ågerfalk, P. J. (2019). Conceptualizing workarounds: Meanings and manifestations in information system research. Communications of the Association for Information Systems, 45, 340–363.

Emanuel, L., Berwick, D., Conway, J., Combes, J., Hatlie, M., Leape, L., Reason, J., Schyve, P., Vincent, C., & Walton, M. (2008). What exactly is patient safety? In K. Henriksen, J. B. Battles, & M. A. Keyes (Eds.), Advances in patient safety: New directions and alternative approaches (pp. 1–18). Agency for Healthcare Research and Quality

European Commission. (2021a). Active and assisted living programme (AAL) [Online]. http://www.aal-europe.eu

European Commission. (2021b). European medical device directives [Online]. http://ec.europa.eu/growth/single-market european-standards/harmonised-standards/medical-devices

Evans, N., Carey-Smith, B., & Orpwood, R. (2011). Using smart technology in an enabling way: A review of using technolog to support daily life for a tenant with moderate dementia. British Journal of Occupational Therapy, 74(5), 249–253

Galvin, J. C. (1990). Evaluation of assistive technology. Request Rehabilitation Engineering Center, National Rehabilitation Hospital.

Gelber, S. M. (1999). Hobbies: Leisure and the culture of work in America. Columbia University Press.

Ghorbel, M., Betgé-Brezetz, S., Dupont, M. P., Kamga, G. B., Piekarec, S., Reerink, J., & Vergnol, A. (2013). Multimodal notifi cation framework for elderly and professional in a smart nursing home. Journal on Multimodal User Interfaces, 7(4) 281–297.

Gibson, G., Dickinson, C., Brittain, K., & Robinson, L. (2019). Personalisation, customisation and Bricolage: How people wit dementia and their families make assistive technology work for them. Ageing and Society, 39(11), 2502–2519.

Gibson, G., Newton, L., Pritchard, G., Finch, T., Brittain, K., & Robinson, L. (2016). The provision of assistive technology prod ucts and Services for People with dementia in the United Kingdom. Dementia, 15(4), 681–701

Gongora Alonso, S., Hamrioui, S., de la Torre Díez, I., Motta Cruz, E., L opez-Coronado, M., & Franco, M. (2019). Social robot for people with aging and dementia: A systematic review of literature. Telemedicine and e-Health, 25(7), 533–540

Greenhalgh, T., Procter, R., Wherton, J., Sugarhood, P., & Shaw, S. (2012). The Organising vision for telehealth and telecare: Discourse analysis. BMJ Open, 2(4), e001574.

Haj-Bolouri, A., Purao, S., Rossi, M., & Bernhardsson, L. (2018). Action design research in practice: Lessons and concerns Proceedings of the 26th European conference on information systems, Portsmouth, UK, 1–15.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105.

Ho, S. Y., Guo, X., & Vogel, D. (2019). Opportunities and challenges in healthcare information systems research: Caring for patients with chronic conditions. Communications of the Association for Information Systems, 44(1), 852–873.

Hollier, S. & Abou-Zahra, S. (2018). Internet of things (IoT) as assistive technology. Proceedings of the internet of accessibl things, Lyon, France, 1–4.

Holtzman, B., Hughes, C., & Van Meter, K. (2007). Do it yourself… and the movement beyond capitalism. In S. Shukaitis, D Graeber, & E. Biddle (Eds.), Constituent imagination: Militant investigations//collective theorization (pp. 44–61). AK Press

Hurst, A. & Tobias, J. (2011). Empowering individuals with do-it-yourself assistive technology. Proceedings of the 13th international ACM SIGACCESS conference on computers and accessibility. Dundee. UK. 11-18

IDC. (2020). Worldwide ICT Spending Guide. IDC.

Jain, S., Vaibhav, A., & Goyal, L. (2014). Raspberry pi based interactive home automation system through E-mail. Proceeding of the 2014 international conference on reliability optimization and information technology, Faridabad, India, 277–280

James, T. L., Deane, J. K., & Wallace, L. (2019). An application of goal content theory to examine how desired exercise out comes impact fitness technology feature set selection. Information Systems Journal, 29(5), 1010–1039

Jennings, P., & Hussain, S. (2020). Do-it-yourself artificial pancreas systems: A review of the emerging evidence and insight for healthcare professionals. Journal of Diabetes Science and Technology, 14(5), 868–877.

Karunanithi, M. (2007). Monitoring technology for the elderly patient. Expert Review of Medical Devices, 4(2), 267–277.

Klüwer, T. (2011). From chatbots to dialog systems. In D. Perez-Marin & I. Pascual-Nieto (Eds.), Conversational agents and natural language interaction: Techniques and effective practices (pp. 1–22). IGI Global.

Lane, J. P. (2015). Aligning policy and practice in science, technology and innovation to deliver the intended socio-economic results: The case of assistive technology. International Journal of Transitions and Innovation Systems, 4(3–4), 221–248

Langstrup, H. (2013). Chronic care infrastructure and the home. Sociology of Health and Illness, 35(7), 1008–1022

Lê, Q., Nguyen, H. B., & Barnett, T. (2012). Smart homes for older people: Positive aging in a digital world. Future Internet, 4 (2), 607–617.

Lee, A. S., & Baskerville, R. L. (2003). Generalizing generalizability in information systems research. Information Systems Research, 14(3), 221–243.

Lotfi, A., Langensiepen, C., Mahmoud, S. M., & Akhlaghinia, M. J. (2012). Smart homes for the elderly dementia sufferers: Identification and prediction of abnormal behaviour. Journal of Ambient Intelligence and Humanized Computing, 3(3), 205–218.

Lowry, P. B., Gaskin, J., & Moody, G. D. (2015). Proposing the multi-motive information systems continuance model (MISC to better explain end-user system evaluations and continuance intentions. Journal of the Association for Information Sys tems, 16(7), 515–579.

Luna-Reyes, L. F., Zhang, J., Ramon Gil-García, J., & Cresswell, A. M. (2005). Information systems development as emergent socio-technical change: A practice approach. European Journal of Information Systems, 14(1), 93–105.

Mao, H. F., Chang, L. H., Yao, G., Chen, W. Y., & Huang, W. N. (2015). Indicators of perceived useful dementia care assistiv technology: Caregivers' perspectives, Geriatrics & Gerontololgy International. 15(8). 1049–1057

Martin, S., Augusto, J. C., McCullagh, P., Carswell, W., Zheng, H., Wang, H., Wallace, J., & Mulvenna, M. (2013). Participator research to design a novel Telehealth system to support the night-time needs of people with dementia: Nocturnal. Inter national Journal of Environmental Research and Public Health, 10(12), 6764–6782

Matzat, U., & Sadowski, B. (2012). Does the “do-it-yourself approach” reduce digital inequality? Evidence of self-learning of digital skills. The Information Society, 28(1), 1–12.

McCabe, L., & Innes, A. (2013). Supporting safe walking for people with dementia: User participation in the development of new technology. Gerontology, 12(1), 4–15.

McCarthy, T., Pal, J., & Cutrell, E. (2013). The “voice” has it: Screen reader adoption and switching behavior among visio impaired persons in India. Assistive Technology, 25(4), 222–229.

McCreadie, C., & Tinker, A. (2005). The acceptability of assistive technology to older people. Ageing & Society, 25(1), 91–110.

McShane, R. (2013). Should patients with dementia who wander be electronically tagged? Yes. British Medical Journal, 346, f3603.

Meiland, F. J., Hattink, B. J., Overmars-Marx, T., de Boer, M. E., Jedlitschka, A., Ebben, P. W., Stalpers, C., II, Flick, S., van der Leeuw, J., Karkowski, I. P., & Droes, R. M. (2014). Participation of end users in the Design of Assistive Technology fo people with mild to severe cognitive problems: the Furopean Rosetta proiect, International Psychogeriatrics. 26(5) 769–779.

Menard, P., Bott, G. J., & Crossler, R. E. (2017). User motivations in protecting information security: Protection motivatio theory versus self-determination theory. Journal of Management Information Systems, 34(4), 1203–1230.

Mettler, T. (2018). Contextualizing a professional social network for health care: Experiences from an action design research study. Information Systems Journal, 28(4), 684–707.

Mettler, T., & Wulf, J. (2019). Physiolytics at the workplace: Affordances and constraints of Wearables use from an Employee's perspective. Information Systems Journal, 29(1), 245–273.

Mohd, S., Senadjki, A., & Mansor, N. (2018). Trend of poverty among elderly: Evidence from household income surveys. Journal of Poverty, 22(2), 89–107.

Nandhakumar, J., & Jones, M. (1997). Too close for comfort? Distance and engagement in interpretive information system research. Information Systems Journal, 7(2), 109–131.

Newman, L., Browne-Yung, K., Raghavendra, P., Wood, D., & Grace, E. (2017). Applying a critical approach to investigat barriers to digital inclusion and online social networking among young people with disabilities. Information Systems Jour nal, 27(5), 559–588.

Niehaves, B., & Plattfaut, R. (2014). Internet adoption by the elderly: Employing IS technology acceptance theories for understanding the age-related digital divide. European Journal of Information Systems, 23(6), 708–726

Olsson, A., Engstrom, M., Skovdahl, K., & Lampic, C. (2012). My, your and our needs for safety and security: Relatives' reflec tions on using information and communication technology in Dementia care. Scandinavian Journal of Caring Sciences, 2 (1), 104–112.

Pearson, E., & Frakt, A. (2018). Administrative costs and health information technology. Journal of the American Medical Asso ciation, 320(6), 537–538.

Pethig, F., & Kroenung, J. (2019). Specialized information systems for the digitally disadvantaged. Journal of the Associatio for Information Systems, 20(10), 5.

Preston. N.. Weightman. A., Culmer. P.. Levesley. M.. Bhakta. B., & Mon-Williams. M. (2016). The cerebral palsy kinematic assessment tool (CPKAT): Feasibility testing of a new portable tool for the objective evaluation of upper limb kinematic in children with cerebral palsy in the non-laboratory setting. Disability and Rehabilitation: Assistive Technology, 11(4), 339–344.

Rai, A. (2019). Engaged scholarship: Research with practice for impact. MIS Quarterly, 43(2), iii–viii

Raspberry Pi Foundation. (2021). https://www.raspberrypi.org

Robinson, L., Brittain, K., Lindsay, S., Jackson, D., & Olivier, P. (2009). Keeping in touch everyday (KITE) project: Developing assistive technologies with people with dementia and their Carers to promote Independence. International Psycho geriatrics, 21(3), 494–502

Sein, M. K., Henfridsson, O., Purao, S., Rossi, M., & Lindgren, R. (2011). Action design research. MIS Quarterly, 35(1), 37–56.

Sherer, S. A. (2014). Advocating for action design research on IT value creation in healthcare. Journal of the Association for Information Systems, 15(12), 860–878.

Simon, H. A. (1996). The sciences of the artificial (3rd ed.). MIT Press.

Slegers. K., Kouwenberg, K., Loučova, T., & Daniels. R. (2020), Makers in healthcare: The role of occupational therapists ir the Design of Diy Assistive Technology. Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems Honolulu, USA, 1–11.

Smith, R. O., Scherer, M. J., Cooper, R., Bell, D., Hobbs, D. A., Pettersson, C., Seymour, N., Borg, J., Johnson, M. J., & Lane, J. P. (2018). Assistive technology products: A position paper from the first global research, innovation, and educa tion on assistive technology (GREAT) summit. Disability and Rehabilitation: Assistive Technology, 13(5), 473–485

Taleb, N. N. (2018). Skin in the game: Hidden asymmetries in daily life. Random House.

Telegram. (2020). https://telegram.org

Tinker, A. (2003). Assistive technology and its role in housing policies for older people. Quality in Ageing: Policy, Practice and Research, 4(4), 4–12.

Tokunaga, S., Tamamizu, K., Saiki, S., Nakamura, M., & Yasuda, K. (2017). Virtualcaregiver: Personalized smart elderly care International Journal of Software Innovation, 5(1), 30–43

Tufekci, Z. (2019). Altruism still fuels the web. Businesses Love to Exploit It. https://www.wired.com/story/altruism-opensource-fuels-web-businesses-love-to-exploit-it/

U.S. Food & Drug Administration. (2021). U.S. medical devices regulation [Online]. https://www.fda.gov/MedicalDevices DeviceRegulationandGuidance/Overview/

U.S. National Academy of Medicine. (2021). Healthy longevity global grand challenge [Online]. https://nam.edu/initiatives grand-challenge-healthy-longevity

Unbehaun, D., Aal, K., Vaziri, D. D., Tolmie, P. D., Wieching, R., Randall, D., & Wulf, V. (2020). Social technology appropriation in dementia: Investigating the role of caregivers in engaging people with dementia with a videogame-based training system. Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, Honolulu, USA, 1–15.

United Nations. (2007). Convention on the Rights of Persons with Disabilities [Online]. https://www.un.org/development desa/disabilities/convention-on-the-rights-of-persons-with-disabilities.htm

Van de Ven, A. H. (2007). Engaged scholarship. Oxford University Press.

van den Kieboom, R. C., Bongers, I. M., Mark, R. E., & Snaphaan, L. J. (2019). User-driven living lab for assistive technology to support people with dementia living at home: Protocol for developing co-creation–based innovations. JMIR Research Protocols, 8(1), e10952.

Van der Heijden, H. (2004). User acceptance of hedonic information systems. MIS Quarterly, 28(4), 695–704

Van Grootven, B., & van Achterberg, T. (2019). The European Union's ambient and assisted living joint Programme: An eval uation of its impact on population health and well-being. Health Informatics Journal, 25(1), 27–40.

Vaughn, L. M., Whetstone, C., Boards, A., Busch, M. D., Magnusson, M., & Määttä, S. (2018). Partnering with insiders: A review of peer models across community-engaged research, education and social care. Health & Social Care in the Com munity, 26(6), 769–786.

Walls, J. H., Widmeyer, G. R., & El Sawy, O. A. (1992). Building an information systems design theory for vigilant EIS. Information Systems Research, 3(1), 36–59.

Wessel, L., Davidson, E., Barquet, A. P., Rothe, H., Peters, O., & Megges, H. (2019). Configuration in smart service systems A practice-based inquiry. Information Systems Journal, 29(6), 1256–1292

Windrum, P. (2008). Innovation and entrepreneurship in the public services. In P. Windrum & P. M. Koch (Eds.), Innovation i public sector services: Entrepreneurship, creativity and management (pp. 3–20). Edward Elgar Publishing

Wolf, M., & McQuitty, S. (2011). Understanding the do-it-yourself consumer: DIY motivations and outcomes. AMS Review, 1 (3–4), 154–170.

Woo, J.-B. & Lim, Y.-K. (2015). User experience in do-it-yourself-style smart homes. Proceedings of the 2015 ACM interna tional joint conference on pervasive and ubiquitous computing, Osaka, Japan, 779–790.

World Health Organization. (2014). Global Cooperation on Assistive Technology (GATE) [Online]. https://www.who.int/phi implementation/assistive\_technology/phi\_gate/en/

World Health Organization. (2021). Policy Brief: Access to Assistive Technology [Online]. https://www.who.int/publications/i item/978-92-4-000504-4

## AUTHOR BIOGRAPHIES

Tobias Mettler is professor at the Swiss Graduate School of Public Administration, University of Lausanne. His research interests are in the area of design science research, health information technology, and applications of data science with a particular focus on the public sector.

Stephan Daurer is professor of Business Information Systems and academic director data science at DHBW Ravensburg–Baden-Württemberg Cooperative State University. He is co-founder and director of the Center for Digital Innovations (ZDI). His research interests are in the area of platform business models and design science research.

Michael A. Bächle is professor of Business Information Systems at DHBW Ravensburg–Baden-Württemberg Cooperative State University. His research interest are in the area of knowledge management and enterprise social software.

Andreas Judt is professor of Computer Science and academic director of Information Technology, Mobile Informatics, IT Security and Intelligent Systems at DHBW Ravensburg-Baden-Württemberg Cooperative State Uni versity. His research interests are software architectures and assistive technologies

How to cite this article: Mettler, T., Daurer, S., Bächle, M. A., & Judt, A. (2021). Do-it-yourself as a means for making assistive technology accessible to elderly people: Evidence from the ICARE project. Information Systems Journal, 1–20. https://doi.org/10.1111/isj.12352

## APPENDIX A: QUESTIONNAIRE USED IN THE MAKER WORKSHOP

Thank you for your support and your willingness to participate in this survey. The aim of the questionnaire is to evaluat the practical suitability of the iCareBot and to get suggestions for future developments. The questionnaire refers to your expectations and experiences with the system. Please note that there are no right or wrong answers here, but rather you personal assessment. The completion of the questionnaire takes about 5–10 mins. In addition to questions to tick off there are also some questions where text is desired. Your responses will be used exclusively for research purposes within the iCare project. A personal evaluation will not take place. Therefore no conclusions can be drawn about individua persons. The results will be incorporated into the further development of the iCareBot and into project-related scientifi publications. You can find further information and publications on this subject at: https://www.unil.ch/icare.

If you have any questions regarding the questionnaire or the project, please contact judt@dhbw-ravensburg.de. Part 1: Demographics

• Please specify your age (number)

• Please specify your gender (male, female, other)

• Please specify your marital status (single, married, widowed, divorced, partnership)

• Please specify how many people you are responsible for providing care assistance to (number)

• Please specify your level of computer literacy (beginner, intermediate, advanced)

• Programming skills; if yes, which ones? (free text)

## Part 2: Evaluation of the iCareBot.

For all items in this question block, we used a five-point Likert scale (Strongly disagree, Disagree, Neither agree nor disagree, Agree, Strongly agree).

Did the iCareBot meet your expectations concerning…

• Functionality (e.g., programming of alarms)

• Usability (e.g., control via telegram)

• Robustness (e.g., triggering of alarms)

• Trustworthiness (e.g., encryption of alarms)

• Comprehensibility (e.g., output texts in telegram)

• Assistance (e.g., DIY instructions and website)

• Costs (e.g., for assembly, maintenance)

## The use of the iCareBot…

• …is useful for me

• …has simplified the support of others

• …has simplified my coordination with others

• …is easy to learn

• …has overwhelmed me

• …is intuitive to use

• …has frustrated me

• …is interesting

• …is fun

## Part 3: Final questions

• Will you use the iCareBot in the future? (yes/no/do not know)

• Would you recommend the iCareBot to other people? (yes/no/do not know)

• Would you like to support us in the production of the iCare-Bots? (yes/no/do not know)

• Do you have any ideas for improvement that you would like to share with us? (free text)

• Do you want to be informed about innovations in the project? (yes/no)

• If yes, please enter your e-mail address (free text)

[The questionnaire was administered in German language.]
