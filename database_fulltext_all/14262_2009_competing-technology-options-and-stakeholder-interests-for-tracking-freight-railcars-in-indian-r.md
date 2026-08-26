---
otero_id: 14262
otero_key: "SX4V3HAV"
title: "Competing Technology Options and Stakeholder Interests for Tracking Freight Railcars in Indian Railways"
authors: "Shirish C Srivastava; Sharat S Mathur; Thompson SH Teo"
year: "2009"
journal: "Journal of Information Technology"
doi: "10.1057/jit.2009.9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Teaching Case

# Competing technology options and stakeholder interests for tracking freight railcars in Indian Railways

Shirish C Srivastava<sup>1</sup>, Sharat S Mathur <sup>2</sup>, Thompson SH Teo<sup>3</sup>

<sup>1</sup>Operations Management and Information Technology Department, HEC School of Management, Paris, France; <sup>2</sup>Centre for Railway Information Systems, Indian Railways, New Delhi, India; <sup>3</sup>School of Business, National University of Singapore, Singapore

Correspondence:

SC Srivastava, Operations Management and Information Technology Department, HEC School of Management, Paris, 1 Rue de la Libe´ ration, Jouy-en-Josas Cedex, 78351, France.

Tel: þ 33 1 39 67 95 66;

Fax: þ 33 1 39 67 94 15;

E-mail: srivastava@hec.fr

## Abstract

This teaching case examines the implementation of a new technology for tracking individual freight railcars (wagons) by Indian Railways. After exploring multiple ‘technological options,’ the Indian Railways decided to undertake a pilot project based on timetested Automatic Equipment Identification system using Radio Frequency Identification (RFID) technology. However, a number of other technological options are now available, which include EPC Gen2-based RFID systems, Global Positioning System solutions, Optical Character Recognition (OCR)-based systems, and manual hand-held data collection devices integrated with the current Freight Operations System. Each of these systems has its own advantages and limitations. Although Indian Railways officials are going ahead with the pilot project, they are uncertain as to the appropriate technological choice, given the wide range of available technology options. Further, they are faced with competing interests from different stakeholder groups (departments), who favor different technologies.

Journal of Information Technology (2009) 24, 392–400. doi:10.1057/jit.2009.9

Published online 8 September 2009

Keywords: RFID; GPS; technology choice; options; railroad; India

## Introduction

R <sup>anbir</sup> <sup>Singh</sup> <sup>was</sup> <sup>concerned.</sup> <sup>He</sup> <sup>had</sup> <sup>become</sup> <sup>the</sup> <sup>head</sup>of the Centre for Railway Information Systems (CRIS) of the Centre for Railway Information Systems (CRIS) in 2007, after spending more than 33 years handling various operational assignments for the Indian Railways. His last assignment had been as the Head of Operations of one of the Railway Zones<sup>2</sup> of the Indian Railways; he had worked as a senior IT executive in the Indian Railways’ Corporate Office a few years before and prior to that he had headed the computerized ticketing system in one of the Zones. So it was with a sense of familiarity that he had taken up the assignment in CRIS 8 months previously.

In recent years, CRIS had been entrusted with over 20 large new projects pertaining to almost all technology-related aspects of railway working by the Indian Railway Board. As India’s GDP grew by over 9% annually between 2005 and 2008, operational efficiency through IT assumed ever greater importance in the Indian Railways, which had committed itself to capital expenditure on Information Technology of over INR<sup>3</sup> 52 billion (USD 1.3 billion) between 2007 and 2012, most of it channeled through CRIS.<sup>4</sup>

Amidst the burst of frenetic activity that resulted, it was easy to lose sight of strategic issues. But Ranbir Singh realized from the beginning that one innocuous project – a pilot project to track a small sample of Indian Railways’ fleet of 200,000 wagons (freight railcars) using Radio Frequency Identification (RFID) technology, estimated to cost a mere INR 10 million (USD 250,000) – had the potential to change the way in which its freight operations could work in the future. Handled well, the technology could boost the efficiency of freight operations, yielding revenue gains of up to INR 30 billion (USD 750 million) annually. Handled improperly, the resulting chaos could well become the source of missed opportunities and place a drag on revenues, apart from directly costing Indian Railways over INR 4 billion (USD 100 million) in equipment and implementation costs<sup>5</sup> [Indian Railways’ total revenues in 2007–2008 were approximately INR 720 billion (USD 17.5 billion)].

What caused Ranbir concern was the lack of consensus among the various stakeholder groups in the Indian Railways about the idea of ‘tracking’ the rolling stock (freight railcars, passenger coaches, locomotives). The need to automate such tracking – especially for freight railcars<sup>6</sup> – had been felt for almost two decades. Initially, the available technology was too expensive, and experimental in nature; however, lately, technologies had stabilized, and costs had come down. Various options had become available to automate the tracking, ranging from the use of RFID tags to the use of Global Positioning Systems (GPS)-based technology. Other available alternatives were the use of optical tracking systems using OCR, or the use of hand-held devices to manually record wagon identification data.

Ranbir scrutinized the thick file of papers in front of him. It described the pilot project for automatic wagon tracking, which had recently commenced. The pilot project envisaged the use of RFID technology, already proven in North American railroads and other Railways, to tag 500 coal hopper wagons (Figure 1). Three trackside tag readers would be placed along one of the routes used for hauling high-grade coal (Figure 2). All the equipments would be procured from a vendor whose products were already being used successfully in North America. A leading local system integrator had been retained to handle the entire contract including software interfacing with Indian Railways’ Freight Operations System. After a 2-month evaluation of the pilot, the lessons learnt would be incorporated into the detailed project report for introduction of a similar system all over the Indian Railways.

## Indian Railways and the CRIS

Indian Railways is a government agency that operates all passenger and freight rail services in the country.<sup>7</sup> As is seen from the schematic map of Indian Railways, it is among the largest and most complex railway networks in the world.<sup>8</sup> It is the principal mode of passenger and freight transport in India and has played an important role in nation building since its inception in 1853. Currently it has 63,140 route kilometers of rail track, over 8000 railway stations, and about 200,000 freight-carrying wagons.<sup>9</sup> It is similar in size to the BNSF<sup>10</sup> Railroad, a major Railway in the USA. Indian Railways<sup>11</sup> moved nearly 800 million tonnes of freight last year. The increasing freight traffic and loading volume over the years is given in Table 1.

![](/api/attachments/SX4V3HAV/fulltext/images/02265f17e7a9807d70baf6bd3477703171e40b82ec15a2520303176f0100585b.jpg)  
Figure 1 RFID tag fitted on a freight wagon in Indian Railways (pilot project)

In 1986, the Ministry of Railways established the CRIS at New Delhi. CRIS has been set up as an umbrella unit for all IT-related activities in Indian Railways. It is a projectoriented organization, with the mandate to develop and implement IT systems, ensure standardization of computer hardware and software, and also ensure close coordination of IT and business goals.

## Motivation for the use of an automated wagon tracking system: The initial need

The need to use automated means to track railway wagons was first experienced in the Indian Railways as early as the 1970s. At that time, increasing freight traffic, a large number of freight wagons, and the need for quicker freight movement began to stretch manual tracking methods beyond their limits. This increase in freight traffic roughly corresponded to the increasing economic activity in India. Computerized systems for managing freight railways were at an incipient stage at that time in railway systems around the world. These so-called ‘Total Operating Systems’ were being developed and deployed in the railroads of the USA, while railways in Canada and the UK had begun to explore such systems as well. Indian Railways decided to implement a ‘Total Operating System’ christened as the ‘Freight Operations System.’ The project was started in 1985 and the first implementation of the Freight Operations System started in 1993. However, by 1996 it was apparent that the entire system needed a thorough revamp, as it was not meeting users’ needs. Therefore, in 1997, a completely rewritten, indigenously developed version of the Freight Operations System was conceived. It was rolled out between 1999 and 2004. It enabled the tracking of wagon consists, as well as individual freight wagons. However, there was one serious lacuna in the system: individual wagon identification numbers were not automatically captured, but were recorded manually, by approximately 2500 ‘train clerks’ at 600 locations. Not only was manual recording tedious and stressful for the staff, but it introduced errors in the Freight Operations System’s database, and introduced delays in the tracking process. The annual staff cost on manual tracking is estimated at INR 450 million (USD 11 million). This cost could potentially be reduced with the adoption of technology. Further, there are also cost and time savings in elimination of errors through automated tracking.

![](/api/attachments/SX4V3HAV/fulltext/images/1f1f87d87a64acee163fa2885ce5507dba56078fb416a5243e7335e020603441.jpg)  
Figure 2 Track side RFID reader – Indian Railways (pilot project).

Table 1 Growth of Total Freight Traffic and Loading Capacity in Indian Railways

<table><tr><td>Year</td><td>Originating freight loading (Million Tonnes)</td><td>Avg. annual growth rate of freight loading (%)</td><td>Revenue earning freight traffic (Net Tonne Km, Billion)</td><td>Number of wagons (1000 vehicle units)</td><td>Total capacity of wagons (Million Tonnes)</td><td>India&#x27;s GDP growth rate (%)</td></tr><tr><td>1960–1961</td><td>119.8</td><td>3.89</td><td>72.3</td><td>295</td><td>6.3</td><td>3.0 (approx)</td></tr><tr><td>1990–1991</td><td>318.4</td><td>3.85</td><td>235.8</td><td>335</td><td>11.5</td><td>4.0 (approx)</td></tr><tr><td>2000–2001</td><td>473.5</td><td>3.28</td><td>312.4</td><td>214</td><td>10.2</td><td>4.4</td></tr><tr><td>2003–2004</td><td>557.4</td><td>5.02</td><td>381.2</td><td>216</td><td>10.7</td><td>8.3</td></tr><tr><td>2004–2005</td><td>602.1</td><td>7.42</td><td>407.4</td><td>211</td><td>10.6</td><td>9.2</td></tr><tr><td>2005–2006</td><td>666.5</td><td>9.66</td><td>439.6</td><td>198</td><td>10.0</td><td>9.0</td></tr><tr><td>2006–2007</td><td>727.8</td><td>8.42</td><td>481.0</td><td>198</td><td>10.0</td><td>9.4</td></tr><tr><td>2007–2008</td><td>794.2</td><td>8.36</td><td>511.8</td><td>200 (est.)</td><td>10.1 (est.)</td><td>8.7</td></tr></table>

Moreover, in the present day scenario, the need to track individual freight wagons accurately has become more pronounced for the Indian Railways. Highways have improved, so trucks compete fiercely with rail for freight. Organized logistics chains have emerged that need real time shipment-related information; just-in-time inventories have become common in industry; wagon leasing organizations want online information about their assets; and most customers demand guaranteed transit times. Further, Indian Railways is gradually shedding its image of a pure ‘public service organization’ and is metamorphosing into a ‘socio-commercial’ organization. Hence, financial performance and accountability for various investments is increasing day by day. As seen in Table 1, the significant increase in GDP in the past 5 years has further compounded the need for an increase in freight carriage requirements in India.

Further, the increase in the number of freight wagons is not keeping pace with the growing freight traffic. In recent years, a combination of newly replaced track and modern wagon designs has enabled axle loads (and hence the loading capacity of each wagon) to be increased significantly on major routes of the Indian Railways (Table 1). This has helped the Indian Railways to increase its freight loading by about 9% each year. Any further increase in physical capacity of the wagons is now difficult to achieve, so newer and more efficient methods are required to enhance the utilization of the existing wagon capacity. This again translates into a need for more accurate monitoring of wagon movement so as to reduce turnaround time.<sup>12</sup> To achieve this, a technology for automatic tracking of individual wagons has become imperative. While this need appears to be indisputable, the methods to be adopted to accomplish such tracking are disputed by some important stakeholders within Indian Railways, delaying the adoption of suitable technology.

## Stakeholder interests and available tracking options for individual wagons

US railroads had been looking for a solution to the problem of ‘automated tracking of freight wagons’ since the 1970s. Starting with a system of colored bar codes painted to the sides of the wagons, long years of research and development led them to develop an RFID-based system in the early 1990s called the Automatic Equipment Identification system. This Equipment Identification System enables track-side devices called ‘reader/interrogators’ to read RFID ‘tags’ fitted to the sides of the railcars, thus capturing their identification numbers automatically. Tags are ‘passive’ or ‘beam powered’; that is, they have no batteries or power source of their own. They draw their power from the reader/interrogators, whenever they pass within reading range. The information captured by the reader is then transmitted to a central railcar tracking database. This system has since been standardized and made mandatory by the Association of American Railroads for all US Class 1 Railroads. A description of the Automatic Equipment Identification system is given in Appendix A.

Even though the Equipment Identification system had been chosen for the pilot project in Indian Railways for tracking freight wagons, Ranbir Singh was aware that many competing technologies had now become available for doing a similar job. Even in the domain of RFID, new standards like the interoperable EPC Gen2 had emerged, which promised enhanced capabilities and lower cost in the tracking system. Another technology that could be used for the purpose was the satellite-based GPS, which was already being tried out by Indian Railways for passenger trainrelated applications. In fact, the research wing of Indian Railways had been working on a real-time GPS train tracking system for the past several years. This GPS based Satellite Imaging System improves the quality of information provided to Indian Railways’ passengers by monitoring every passenger train in a specific range for its location, speed, and direction of movement. A description about the GPS as currently being used by Indian Railways is given in Appendix B. Many in the Indian Railways believed that the use of the existing GPS could be extended for tracking individual wagons.

In addition to RFID- and GPS-based technology, some stakeholders had also contemplated using other technologies that could serve the purpose, such as identification of wagon numbers through OCR, or the use of hand-held devices by train clerks to key in the wagon identifier into the Freight Operations System (cost implications of using these alternative methods of tracking are given in Table 2).

It was not only the relative technological capabilities of the ‘alternative options’ that worried Ranbir. What bothered him more was the fact that the proposition of a new technology for individual wagon tracking had opened the Pandora’s Box for multiple stakeholder groups in Indian Railways [as shown in the organizational chart of Indian Railways with various stakeholder groups (departments) in Figure 3]. Although the prime need for tracking the individual wagons originated from the ‘Operations Department,’ other stakeholder groups in Indian Railways like the ‘Mechanical Department’ (the custodian of all the rolling stock and wagons in Indian Railways) and the ‘Signal and Telecom Department’ (the custodian of all signaling and communication-related devices for train running) were also interested in the impact that the implementation of such technology could have on their performance. As these stakeholder groups would be intricately involved with the implementation of the chosen technology, they had already started weighing the potential benefits that their respective departments could derive from the available ‘wagon tracking technology’ options (Table 3). Their opinions about the choice of a solution would depend in large measure on the technology’s ability to cater to some of their major requirements linked to the tracking of wagons. Although the pilot project for the Equipment Identification system was already underway, Ranbir realized that it would be myopic to zero in on one final solution without considering the pros and cons of other options, and without having a consensus among all the major stakeholders.

Ranbir recalled that, when the Equipment Identification system (RFID tagging of freight railcars) had started in North America, the state of the technology was very different from the situation today. At that time, one vendor dominated the technology, which had been progressively improved upon specifically for railcar identification, and was extensively proven in harsh railway environments. Today, with improvement in technology, and the recent explosion in interest in RFID, Ranbir had found that users were gravitating toward the idea of general purpose standards for RFID, known as the ‘EPC Gen2’ standards. These standards promised to provide interoperability between different manufacturers of RFID equipment while drastically bringing down costs. Although EPC Gen2 tags had never yet been used to track railcars, Ranbir wondered whether it was right to reject this technology without due consideration.

Anjali Ghosh, CRIS’ General Manager for Asset Management systems, managed a project for tracking of other assets such as high-value spare parts and other maintenance-related issues. She had said to Ranbir in her candid way:

I have been exploring RFID technology extensively for my own projects, and I recommend that we should not ignore EPC Gen2 standards: they are the future of RFID. Proprietary RFID systems of the type that we are planning to adopt in the pilot project will eventually wither away, so why try them out? As it is, the frequency of operation of the Equipment Identification system in

India (865–867 MHz) differs from the North American frequency (902–921 MHz). So why try out such a nonstandard system?

M. Chandrashekharan, the Project Manager for the RFID project, countered:

We want to work with a proven technology, one that has been used in other railways and has been proven there. The North American system is being adopted in Australia, South Africa, and China in a big way. The least risk approach is to adopt the same technology (though we have to adhere to the frequency ranges prescribed by our government, which means a minor modification to the tag and reader design). We are not an R&D outfit: we cannot afford to risk projects for the sake of unproven technologies, purely based on media hype.

As mentioned earlier, another option that was being seriously contemplated by many stakeholders was the use of GPS technology, a pre-requisite for which was a small inexpensive GPS unit with a long-lasting power source that could be placed on every rolling asset in Indian Railways. Such a unit was not available yet, but many solutions involving GPS occupied the mind of important project stakeholders because of the sheer glamour associated with the technology. As succinctly put by Abdul Javed, the Senior Technical Director in charge of the GPS project in Indian Railways’ Research organization:

Since all trackside signaling equipment is maintained by our department, the RFID-based system will work in the long run only if our department maintains the track-side RFID readers. However, my real concern is that GPS devices are the future for any sort of asset tracking. Please do not start any initiative on asset tracking without the use of GPS devices; the present problems with batteries and power sources will be solved in the near future.

His views found an echo in the other members of the Signal and Telecom Department, who wanted to use a GPS system for the tracking of individual wagons.

Despite the predominant support for RFID- and GPSbased systems, a few stakeholders felt that trackside optical cameras could accomplish the same purpose in a much easier and cheaper way. Anjali Ghosh had already advised Ranbir:

Optical character recognition systems have become very powerful nowadays. They are no longer affected by dust or oil on the vehicle sides. They are the ideal method of reading wagon numbers from the track side. Optical systems need nothing more than a set of trackside cameras, and you are right in business! Contrast this with the task of fitting 200,000 wagons with RFID tags!

## But M. Chandrasekharan, was equally emphatic:

In Indian Railways, wagon numbers of many of the wagons cannot be read by the best of equipment, since the paint fades so badly, or the numbers get obscured by thick dust. Optical tracking systems will be a miserable failure.

l<sub>uat</sub>i<sub>on</sub> <sub>of</sub> <sub>Ava</sub>il<sub>a</sub><sup>b</sup>l<sup>e</sup> <sup>Opt</sup>i<sup>ons</sup> <sup>for</sup> <sup>Track</sup>i<sup>ng</sup> I<sup>nd</sup>i<sup>v</sup>i<sup>d</sup>

<table><tr><td>Technology Option</td><td>Evaluation parameter</td><td>Evaluation</td></tr><tr><td rowspan="3">Hand-held devices with trains clerks for entry into Freight Operations System (Upgradation of manual system)</td><td>Cost to Indian RailwaysBenefits to Indian Railways</td><td>Low cost (under INR 50 million)Minimal changes to existing system of data captureAddresses delays in transcription of data into Freight Operations System; however, does not address the issues of unreadable/obliterated wagon numbersReduces data entry errorsImplementation process is moderately simple.Staff needs to be trained.</td></tr><tr><td>Ease of implementation</td><td>Moderate, as staff may revert to manual process if glitches surface</td></tr><tr><td>Risk of failureStakeholder conflict</td><td>Addresses the needs of Operations Department only</td></tr><tr><td rowspan="3">Optical tracking through Optical Character Recognition (OCR) $^a$ </td><td>Cost to Indian RailwaysBenefits to Indian Railways</td><td>Moderate (between INR 500 million and INR 1 billion)Can provide comprehensive wagon track and traceTrain clerks could be redeployed to other areasComparatively easy to implement, as no device is to be placed on the wagonMight need some human intervention during identification</td></tr><tr><td>Ease of implementation</td><td>Moderate, because dust and dirt on the wagon side and camera lens may obscure the wagon identity</td></tr><tr><td>Risk of failureStakeholder conflict</td><td>As there is no need to fix a device on the wagon, there is little stakeholder conflict</td></tr><tr><td rowspan="3">RFID (Equipment Identification system) $^b$ (Also refer to Appendix A)</td><td>Cost to Indian RailwaysBenefits to Indian Railways</td><td>High (over INR 2 billion)Can provide comprehensive wagon track and traceTrain clerks could be redeployed to other areasImplementation process is moderately difficult.Tag has to be affixed to the wagon side.However, no human intervention is needed during wagon identification.</td></tr><tr><td>Ease of implementation</td><td rowspan="2">Low, as the model has been running in other railwaysPotentially addresses the needs of all departments, but conflict due to placement of device on wagon remains</td></tr><tr><td>Risk of failureStakeholder conflict</td></tr><tr><td rowspan="3">RFID (EPC Gen2 system) $^c$ </td><td>Cost to Indian RailwaysBenefits to Indian Railways</td><td rowspan="2">Moderate (between INR 500 million and INR 1 billion), if costs of tags go down to the expected levelsCan provide comprehensive wagon track and traceTrain clerks could be redeployed to other areasImplementation process is moderately difficult.Tag has to be affixed to the wagon side.There is as yet no experience of such tags for wagon trackingHowever, no human intervention is needed during wagon identification.</td></tr><tr><td>Ease of implementation</td></tr><tr><td>Risk of failureStakeholder conflict</td><td>Moderate, as the equipment has not been proved in other railwaysPotentially addresses the needs of all departments, but conflict due to placement of device on wagon remains</td></tr><tr><td rowspan="3">GPS-based system $^d$ (Also refer to Appendix B)</td><td>Cost to Indian RailwaysBenefits to Indian Railways</td><td rowspan="2">Very high (over INR 5 billion)Can provide real-time trackingTrain clerks could be redeployed to other areasImplementation is difficult, as the GPS device is comparatively fragile and has a finite life.Device has to be affixed to the wagon side.There is as yet little experience of such devices for wagon trackingHowever, no human intervention is needed during wagon identification.</td></tr><tr><td>Ease of implementation</td></tr><tr><td>Risk of failureStakeholder conflict</td><td>High, as the devices are fragile and have a finite lifePotentially addresses the needs of all departments, but conflict due to placement of device on wagon remains</td></tr></table>

<sub>escr</sub>i<sub>pt</sub>i<sub>on</sub> <sub>of</sub> <sub>GPS</sub> i<sub>s</sub> <sub>g</sub>i<sub>ven</sub> <sub>at</sub> <sub>http</sub>:<sub>//w</sub><sup>ww</sup>. <sub>out</sub> <sub>RF</sub>I<sub>D</sub> <sub>(EPC</sub> G<sup>en</sup> <sup>2)</sup> <sup>can</sup> <sup>be</sup> <sup>seen</sup> <sup>at</sup> <sup>http</sup>:<sup>//zone</sup>.<sup>n</sup>i.<sup>com/devzone/c</sup> bA brief description of RFID in general available at http://en.wikipedia.org/wiki/RFID and a brief description of RFID (Automatic Equipment Identification) available at http://www.saic.com/products/transportation/railnet/. cSome details about RFID (EPC Gen 2) can be seen at http://zone.ni.com/devzone/cda/tut/p/id/4300. <sub>of</sub> <sub>the</sub> <sub>OCR</sub> <sub>techno</sub>l<sub>ogy</sub> <sub>ava</sub>il<sub>ab</sub>l<sub>e</sub> <sub>at</sub> <sub>http</sub>:<sub>//en</sub>.wi<sup>k</sup>i<sup>ped</sup>i<sup>a</sup>.<sup>org/w</sup>i<sup>k</sup>i<sup>/Opt</sup>i<sup>ca</sup>l<sup>\_char</sup>

![](/api/attachments/SX4V3HAV/fulltext/images/baabebdad2422a2e1f7236b31877220b327f837334967c7f39fc510fd7481d09.jpg)  
Figure 3 Stakeholders for wagon tracking in Indian Railways and their reporting relationships.

Other stakeholders were of the opinion that simply improving the existing manual number-recording scheme, coupled with simple low-cost hand-held readers, would achieve similar results, at a substantially lower cost. This view was voiced by Elizabeth M. Doungel, the Executive Director of Finance in the Railway Board. She was responsible for clearing all IT-related projects in the Indian Railways Board from the financial angle. She cleared the RFID-based pilot project; but she was blunt in her personal assessment:

Fanciful schemes of tagging wagons and reading the tags are a needless waste of money. Have we even tried to improve the system of manual reading of wagon numbers? Why not give selected trains’ clerks hand-held devices into which they could type in the wagon numbers at the points of interchange? While I am formally recommending the RFID-based pilot project at this point of time, I would not like to clear the main wagon tracking project in future until alternative processes and technologies have been adequately examined.

Despite efforts to keep all stakeholders involved in the project, the Mechanical Department, responsible for maintaining all of Indian Railways’ rolling stock, remained out of the loop to a large extent during the decision-making process. In fact, P.S. Reddy, the Indian Railways Board Member heading the Mechanical Department, had recently voiced his concern in an internal meeting, going so far as to tell his Operations counterpart, Virendra Dayal:

If the equipment that the Operations Department wants to fit on our wagons interferes with our maintenance work, we reserve the right to remove it without notice.

Coming from such a senior person in the Indian Railways hierarchy, the statement appeared portentous to Ranbir. But the Mechanical Department had a real interest in implementing a wagon tracking system if it helped them to manage the maintenance schedules of the individual wagons, and integrated well with their ‘Rolling Stock Component Management’ system.

In addition to internal stakeholders within Indian Railways, there are some external stakeholders whose needs cannot be ignored; the most important group among these being the ‘freight customers’ who are the ultimate beneficiaries of this technology implementation. The list of external stakeholders also includes vendors of tracking solutions, be they RFID-based, or based on competing technologies, and also the various lobby and pressure groups championing the use of a particular technological option.

## Current situation

In addition to the competing technologies for wagon tracking, recent improvements in RFID technology and the emergence of competing RFID standards, and conflict in stakeholder interests, Ranbir was also worried about the two important aspects of (1) inadequate cost–benefit analysis, and (2) inadequate analysis on extending the use of RFID to other functions.

## Inadequate cost–benefit analysis

Despite reading in general terms about the possible benefits of RFID-based wagon tracking, Ranbir had seen no study in which the benefits of such a system had been laid out in clear, unambiguous, financial terms. How much could Indian Railways afford to spend on a wagon tracking system? The answer to that question was a deafening silence. There was only Elizabeth M. Doungel’s remark:

The pilot project is being sanctioned by the Board as proposed, but no more funding until a water-tight business case is made.

Ranbir had been in touch with his counterparts in other countries that had implemented RFID-based wagon tracking. Although all generally favored the technology, they did not provide any concrete cost–benefit analyses. North American Class 1 Railroads were mandated by the Association of American Railroads to use the system, so they had no choice. South African Railway had previously used active tags and abandoned them before turning to the current Equipment Identification system. They were understandably tightlipped about the reasons behind their decision. The conditions in Australian freight railroads, characterized by a small labor force and harsh ground conditions were very different from those in the Indian Railways. The Chinese Railways had not yet responded to queries. In effect, Ranbir had inadequate answers in this area.

## Extending the reach of RFID to other areas

Though not of immediate relevance, the issue of extending the reach of the RFID system rankled in Ranbir’ mind. Should he not plan, right at this moment, how the RFID technology, being contemplated for wagon tracking, should be extended to other types of rolling stock as well? Could the readers not be used to read end-of-train (‘last vehicle’) devices also? Could they not be used to give inputs to the

Table 3 Indian Railways Stakeholder Objectives

<table><tr><td>Major stakeholder group</td><td>Objectives of stakeholder group pertaining to individual wagon tracking</td></tr><tr><td>Indian Railways</td><td>Ability to track and trace its assets, leading to better analysis of distribution of wagons, enabling better planning for reducing idle time, and increasing availability of the wagons</td></tr><tr><td>Operations Department</td><td>Automatic capture of wagon numbers into Freight Operations System, to eliminate manual data captureIdentifying wagons spending extra time in maintenance facilities/non-productive activitiesTotal automation while preparing invoices for loaded goods</td></tr><tr><td>Mechanical Department</td><td>Tracking down the wagons due for maintenanceCalculating the distance traveled by each wagon between each maintenance cycle, to ensure that no wagon goes beyond its prescribed distance</td></tr><tr><td>Signal and Telecom Department</td><td>No direct objective, but sees itself as the natural custodian of all trackside equipment, so wants to take ownership of trackside readers</td></tr></table>

Control Office Automation system, which automated the working of the 70 Train Control Offices in Indian Railways? Anjali Ghosh gave her vociferous opinion:

Trackside readers should be common for tracking all assets. EPC Gen2 technology is therefore a must. The present system will not give you any synergies with other systems.

M. Chandrashekharan, on the other hand, was clear that the wagon tracking system should be independent of any other system.

It is important to keep the system free of complexity. That’s the only way it will succeed. And when it succeeds, this one system will in itself change the way Indian Railways works; that’s a promise.

These were the doubts and concerns that crossed Ranbir’s mind as he went through the case file. Lately, there had been other irritants. Vendors hounded him constantly with details of their ‘RFID practice,’ dubious looking ‘agents’ from different countries wanted to meet him, and the media caught onto the magic word ‘RFID’ and bombarded him with questions and interview requests, as well as queries through India’s ‘Right to Information Act.’ Through all this, Ranbir soldiered on. But now, the pressure was getting higher. Virendra Dayal, the Indian Railways’ Board Member for Operations, had recently said:

You need to get your pilot project working quickly; we need some results now.

Ranbir knew that Dayal, a known technology supporter, had only a few months to retire. Quick results from the system were therefore of utmost importance. As if to underline the above, Subodh Kumar, Executive Officer to the Minister for Railways, had already conveyed the Minister’s wishes:

The Minister would like to ensure that the full-fledged wagon tracking project is initiated before the end of the current financial year. Efficient utilization of our wagons is the basis of our recent spectacular performance, so we need all the technology inputs that we can get to further improve the utilization. Funds will not be a constraint for this project, provided quick results are shown.

Ranbir realized that the Ministry was banking heavily on automated wagon tracking to help achieve higher freight loading targets, and it would not tolerate slow progress of the project; in this scenario, his dilemma was:

\- If the pilot project worked out, Ranbir was in a quandary about the subsequent steps to follow.

 Should a study be done on alternative technologies such as GPS and optical systems?

 Should the concern about EPC Gen2 standards be addressed? If so, how?

 Should a more rigorous cost–benefit analysis be done after the pilot?

 How should the Mechanical Department and other stakeholders be brought into the loop so that alienation of stakeholders was avoided at the time of the main project?

 How and when should he try to extend the technology to other areas? How much synergy, in terms of equipment sharing, should he aim for?

\- If the pilot project failed for some reason, what should be done?

 Should he recommend the abandonment of RFIDbased wagon tracking altogether? Or should the RFID approach be tried again?

 Should an alternative technology be tried out? If so, which one?

Ranbir relished problem solving. So the complex issues surrounding this innocuous looking project only energized him. He was glad to have thought things through at this preliminary stage: the questions that had arisen in his mind would need answers as the project progressed. With renewed vigor, he picked up the phone to get the latest update from his RFID team.

## Notes

1 The authors prepared this case as a basis for class discussion, rather than to illustrate either effective or ineffective handling of an administrative situation. Names of the persons involved have been disguised, and some roles have been combined for clarity. The facts presented in the case are loosely based on on-going projects of the Indian Railways.

2 For administrative purposes, Indian Railways is divided into geographically demarcated 17 Railway Zones, viz. Northern, North Eastern, North East Frontier, North Western, North Central, Western, West Central, Eastern, East Central, East Coast, Southern, South Eastern, South Western, South Central, South East Central and Central.

3 1 US Dollar (USD) is approximately 40 Indian Rupees (INR).

4 Report of Working Group of IR http://planningcommission .nic.in/aboutus/committee/wrkgrp11/wg11\_railway.pdf.

5 Based on Indian Railways’ internal estimate of the cost of automatic wagon identification for all wagons.

6 Henceforth referred to as ‘wagons’. ‘Wagons’ is the term used in Indian Railways for describing freight railcars.

7 For more information about the governance in Indian Railways see http://www.indianrailways.gov.in.

8 A map of the Indian Railways can be seen at http://www.indian railways.gov.in/maps/all\_india.htm.

9 More contextual information about Indian Railways can be found at http://en.wikipedia.org/wiki/Indian\_Railways and also in Srivastava et al (2007).

10 http://www.bnsf.com/investors/annualreports/2007annrpt.pdf.

11 More information about the IR is available in its Annual Report http://www.indianrailways.gov.in/deptts/stat-eco/Year-Book\_06\_07.htm.

12 The time between two subsequent loadings.

## Reference

Srivastava, S.C., Mathur, S.S. and Teo, T.S.H. (2007). Modernization of Passenger Reservation System: Indian Railway’s dilemma, Journal of Information Technology 22: 432–439.

## About the authors

Shirish C. Srivastava is an Assistant Professor at HEC School of Management, Paris. He obtained his Ph.D. from the School of Business, National University of Singapore. His research has been published in several international refereed journals such as MISQ Executive, Journal of Management Information Systems, Journal of Information Technology, Communications of the AIS, Journal of Global Information Management, Information Resources Management Journal, and Electronic Government: An International Journal, among others. He has also authored several book chapters and has presented his research in key international refereed conferences like International Conference on Information Systems (ICIS), Academy of Management (AOM), Academy of International Business (AIB), Institute for Operations Research and the Management Sciences (INFORMS), and Americas Conference on Information Systems (AMCIS). He has been thrice nominated for the prestigious Carolyn Dexter Award at the Academy of Management (AOM) Meetings 2005, 2007, and 2008 and was a finalist for the award at AOM 2007. Recently, he has been nominated for the academy wide William H. Newman award at the AOM 2009, Chicago and is the winner of the Gerardine DeSanctis Dissertation Award for the best doctoral dissertation paper in organizational communication and information systems. He has also been a winner at the Society for Information Management (SIM) Paper Award Competition, 2007. His research interests include IT-enabled offshore sourcing, e-government, IS strategy, and e-business strategy.

Sharat S. Mathur is an IT Manager in the Indian Railways, presently posted at the CRIS at New Delhi as its General Manager – IT. He has worked extensively in the area of IT in the Indian Railways since 1988. His primary assignments have been in IT-based systems for material procurement, material resource planning, shop floor scheduling, EDI, and logistics. He has been the CIO of Container Corporation of India Ltd., a Government of India Undertaking, during 1997–2000. He has also worked on IT strategy planning and management during his assignment as Director, Computerization and Information Systems in the Ministry of Railways during 2002–2006. His present assignment involves coordination of IT resources for the IT projects executed by CRIS for the Indian Railways.

Thompson S.H. Teo is an Associate Professor in the Department of Decision Sciences at the School of Business, National University of Singapore. His research interests include strategic use of IT, e-commerce, adoption and diffusion of IT, strategic IT management and planning, and offshoring. He has published more than 100 papers in international refereed journals. He is Senior Associate Editor for the European Journal of Information Systems, Regional Editor (Asia-Pacific) for the International Journal of Information Management and is also on several editorial boards such as Communications of the AIS, Internet Research and Omega. He has co-edited four books on IT and e-commerce, and is also a two-time winner of the SIM Paper Competition Award.

## Appendix A

Tracking freight railcars through automatic equipment identification system

The Equipment Identification system (Figure A1) has been standardized by the Association of American Railroads under the S-918 standard. It is mandatory for all Class 1 Railroads in North America to use this system. The system has essentially two components: RFID tags, affixed to both sides of the wagon; and reader/interrogators, placed at the trackside to read the tags. The system uses radio frequency in the UHF range (902 to 922 MHz range in North America) to communicate.

![](/api/attachments/SX4V3HAV/fulltext/images/e6ed7286077ab223cbc7fbfaedec8c29249e78c78ca51f738a96f86015a0eb16.jpg)  
Figure A1 Simplified schematic diagram of Equipment Identification system.

Tags are ‘passive’; that is, they have no batteries or power source of their own. They draw their power from the reader/interrogators, whenever they pass within their reading range. They are therefore also called ‘beampowered.’ ‘Reader/interrogators’ are trackside devices that can read tags coming within their range (in case of the Equipment Identification system, this is approximately 2 meters, at speeds of upto 128 Km/h, with a maximum reader isotropic power of 1 W).

In the North American system, data read by the readers are processed in a ‘field processor’ to produce a ‘clean list’ of railcar numbers. This ‘clean list’ is then transferred to the different railroads’ central computer systems. The primary purpose of the Equipment Identification system is identification of the railcars passing a reader location; however, other information such as the number of axles, length of the railcar, and type of wheel bearings used, is also encoded in the tag. The tags carry 128 bits of suitably encoded data. The Equipment Identification system was standardized and made mandatory for all Class 1 Railroads in North America in 1993. By 1995, over 2 million railcars had been tagged, and over 1000 locations were provided with trackside readers in the region, and all interchange across the participating railroads was accomplished through this system.

## Appendix B

## The use of GPS in Indian Railways

Indian Institute of Technology, Kanpur and the research wing of Indian Railways viz. Research Design and Standards Organization, Lucknow are the major collaborators in a Technology Mission formulated in 2003 to modernize monitoring, control, communications, design, electronics, and materials for Indian Railways. Under this mission, Satellite Imaging for Railway Navigation (SIMRAN) is a ‘real time tracking system’ aimed at improving the quality of information provided to the passengers of Indian Railways.

SIMRAN is a GPS-based continuous train-tracking system that enables monitoring every passenger train in a specific range for its location, speed, and the direction of movement. SIMRAN utilizes Global System for Mobile communications for transmitting train-related information, once every minute, to passengers through display boards at stations, through the Internet, via telephonic Interactive Voice Response Systems, and through Short Message Service on mobile phones. The pilot phase of the project was implemented over selected trains and sectors of Indian Railways by December 2007 at a cost of about INR 20 million.
