---
otero_id: 26241
otero_key: "R5QYHGDB"
title: "Adopting SAP at Siemens Power Corporation"
authors: "Sabine Gabriele Hirt; E. Burton Swanson"
year: "1999"
journal: "Journal of Information Technology"
doi: "10.1177/026839629901400304"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Adopting SAP at Siemens Power Corporation

SABINE GABRIELE HIRT and E. BURTON SWANSON

The Anderson School at UCLA, Department of Information Systems,

110 Westwood Plaza, Los Angeles, CA 90095, USA

This case describes how Siemens Power Corporation, a Richland, Washington, USA-based manufacturer of nuclear fuel assemblies, came to adopt and implement SAP’ s R/3 application suite, the world’s leading enterprise resource planning (ERP) package. The case introduces the reader to the type of decision making related to an ERP adoption and implementation and provides some interesting examples of factors which may in¯ uence actual decisions and outcomes. Among other things, the case touches on the following issues: the relationship between restructuring (re-engineering) and software adoption and implementation, the choice of package software, the pros and cons of alternative implementation approaches (‘big bang’ versus phased’). the selection of hardware and the value of consultants.

By January 1999 Siemens Power Corporation’ s (SPC’s) restructuring project was more than 2 years under way. To SPC’s top management’s great relief, the company had made major progress ever since SPC’s German parent Siemens AG hired a consulting team to help SPC get back on its path towards pro® tability. In particular, the largest and riskiest of its individual restructuring subprojects ± SPC’ s SAP R/3 implementation ± seemed on the way to becoming a success.

## Introduction

Siemens Power Corporation (SPC) is a globally operating manufacturer of both fossil fuel and nuclear power generation systems. It is wholly owned by its German parent Siemens AG.

SPC’s Richland, Washington, USA-based nuclear fuel fabrication plant engages in the manufacturing of nuclear fuel assemblies for both boiling water reactors (BWRs) and pressurized water reactors (PWRs) and related services. The company was originally founded as Exxon Nuclear in 1969 and later bought by Siemens AG. While its German sister plant serves the European markets, SPC primarily competes in the USA. By 1994, the plant employed approximately 1100 people and had revenues of approximately \$200± 300 million. With a market share of approximately 20%, SPC is the third largest competitor after Westinghouse and GE, which command 35 and 25% of the market, respectively. The remaining 20% of the market is approximately evenly divided between ABB/CE and Framatome/Cogema.

## The nuclear fuel industry’s value chain

SPC’ s business, nuclear fuel fabrication, forms an essential part of the nuclear fuel industry’s value chain or \`fuel cycle’ .

(1) Mining. Uranium ore retrieved from mining operations contains, on average, approximately 0.7± 0.8% of the isotope <sup>235</sup>U (naturally enriched <sup>235</sup>U). However, most reactors currently in use operate at somewhere between an average of 3 and 5% enriched <sup>235</sup>U. Thus, the ore needs to be arti-® cially enriched before it can be turned into fuel. (2) Conversion. Once the uranium is extracted from the ore, it is sent to a plant where it is converted into a gas (uranium hexa¯ uoride (UF )). (3) Enrichment. The gas is then sent to an enrichment plant of which only a few exist in the world. The one located in the US is operated by the US Government. Here, the concentration of <sup>235</sup>U is increased from 0.7% to typically 3± 5% according to the speci® cations of the ® nal customer, the utility operating the reactor.

(4) Fuel fabrication. The fuel fabrication plants turn the enriched gas into uranium powder which is ® rst sintered into pellets and then ® lled into metallic fuel rods. These rods are arranged in socalled fuel assemblies.

(5) Energy generation. The fuel assemblies are then loaded into the reactors where they will remain for approximately 18 months. Through the process of nuclear ® ssion, reactors generate heat which is converted into electrical power by steam turbines. After the fuel is burned up, its residue is retrieved from the reactors.

(6) Reprocessing. Uranium and plutonium, the reusable energy materials from spent fuel, can be recovered by dissolving used fuel in acidic solutions and by separating the uranium, plutonium and ® ssion products with solvents. Both materials are then recycled through the fabrication of fresh fuel elements. The residual waste undergoes special processing and conditioning for ® nal disposal.

## SPC’s business situation: past and present

After a promising start in the early 1970s, SPC’ s business prospects soon dimmed. One of SPC’s top managers explained.

Back then expectations were high that nuclear power would continue to grow and ultimately would be the power generation of choice for virtually every country. We thought 50± 70% of electricity would eventually be produced by nuclear power because it was at that time pretty cheap and clean. No wonder our company started out with great plans. But, unfortunately, not all of them have materialized. In the beginning our goal was not only to be in nuclear fuel supply, but also to be in the fuel reprocessing business, in nuclear fuel design and fuel storage. We wanted to get involved in new types of enrichment services such as uranium enrichment, laser enrichment, centrifugal enrichment.

But all of these things sort of collapsed on us in the late 1970s. When Jimmy Carter was president he signed a non-collaboration agreement to minimize the chance of plutonium existing in the world. But during reutilization you produce plutonium ± so this agreement killed most of our plans. As a consequence, the company has been pretty narrowly focused. It was involved almost exclusively in nuclear fuel supply and fuel services.

The public’s call for safer and cheaper energy sources led the industry’s main customers ± USA-based utilities ± to reduce their involvement in nuclear power sharply. Utilities operating nuclear power plants started to shut down their nuclear reactors in favour of cheaper and safer energy sources such as oil and natural gas. Simultaneously, as a consequence of the increased environmental awareness in the USA, energy consumption decreased nationwide. This further spurred competition among the utilities. The nuclear fuel industry’s customer base continued to shrink. In addition, the industry’s lucrative uranium brokerage services were no longer sought after as uranium was in ample supply and, thus, quite inexpensive to come by.

Taking their business abroad to compensate for the slump in their home market was not a viable solution either, since the nuclear fuel industry is heavily regulated and opportunities for export are very limited. Overall, the combined effect of these factors was close to disastrous for the nuclear fuel industry. At the beginning of the 1990s, SPC found itself competing against its four US rivals in a stagnant market operating at half capacity and this situation had little prospect for change.

The reason for that is that typically a contract is for four reactor reloads. And a reload in the US market is typically for about 1.5 years, i.e. it lasts for a year and a half in the reactor. If you sign a contract with me for four reloads then we are committed for about 6 years. So if you looked at our production schedule for the next 3 years, 100% of that work is already contracted and ® rm. There is no new business. All new business is beyond that because of the link of these contracts (Top management).

SPC has never been involved in the business of building nuclear reactors, in contrast to its competitors. GE specializes in the construction of BWRs, whereas Westinghouse and the two smaller competitors build reactors of the PWR type. Importantly, the competitors’ specialization in reactor types is re¯ ected in the type of fuel designs they offer. Speci® cally, GE only manufactures fuel for BWRs, while Westinghouse and the two smaller competitors specialize in PWR fuel. SPC, however, offers fuel designs for both types of reactors.

Their costs are much lower as a result. Our manufacturing plant is more complex since we have to build many different designs. There are many more standardized products that we do. We are always retooling from one contract to the next. Whereas GE and Westinghouse can run long production periods with the same product (Top management).

In the past, SPC was ± despite its less favourable cost structure ± capable of effectively competing in the market due to its reputation of being a supplier of high-quality fuel. However, the distinction in quality between SPC and its competitors has diminished over time, gradually eroding SPC’ s competitive advantage.

## Restructuring SPC’s business

By the beginning of the 1990s it had become clear that SPC would not be able to survive much longer if it continued to conduct business as usual. Thus, in 1994, Siemens AG decided to send in a McKinsey team to help restructure SPC’s organization.

## Adopting SAP at Siemens

The McKinsey consultants agreed with SPC’s management on a two-pronged approach that aimed at (1) extending SPC’s technical lead and (2) improving its productivity. In collaboration with SPC they developed close to 600 restructuring ideas for simultaneous improvements in timeliness, quality and productivity. The ideas cut across all functions/departments at SPC. For every single one, savings potentials were assessed, implementation schedules developed, implementation control measures put in place, implementation risks assessed and top management’s approval secured.

The implementation of the ideas resulting from this effort was scheduled to be completed by September 1997 (see Figure 1).

## Idea 15: \`Scrap the IBM!’

SPC’s computer information systems (CIS) department happened to be among the ® rst to undergo the \`restructuring effort.’ One of the most important ideas coming from the CIS group was idea #15 which proposed to getting rid of SPC’s IBM 4381 mainframe-centric environment.

IBM will not sell us their operating system and only leasing it is very expensive. We talked with IBM about reducing those costs, but they were not interested at all. So it became obvious that we needed to remove that machine. This is probably not what you want to hear with an SAP installation. But that is what drove it. We had to get that machine out of here (CIS manager).

The savings associated with the removal of the IBM 4381 were estimated to amount to \$800 000 annually (see Table 1). In addition to the considerable savings promised by the machine’s removal, concerns about the machine’s reliability had recently surfaced. Furthermore, an overhaul of SPC’ s various legacy systems (AMAPS (manufacturing and resource planning), PER-MAC (preventive maintenance), ® nancial systems, nuclear materials system, etc.) ± many of which were running on the IBM ± seemed to be inevitable.

![](/api/attachments/R5QYHGDB/fulltext/images/e54e584c56f2422080d221786bed01558a346c6f6f3c71c83ff09c29257cff53.jpg)  
Figure 1 Integration of restructuring with the SAP project

Table 1 Anticipated annual savings through replacement, updating or integration of various IS systems

<table><tr><td>Idea</td><td>Anticipated annual savings</td></tr><tr><td>Replace IBM 4381</td><td>800 000</td></tr><tr><td>Develop new nuclear materials system</td><td>170 000</td></tr><tr><td>Replace legacy manufacturing resource planning system (AMAPS)</td><td>170 000</td></tr><tr><td>Upgrade the preventive maintenance system (PERMAC)</td><td>150 000</td></tr><tr><td>Integrate the financial system</td><td>100 000</td></tr><tr><td>Replace nuclear materials database</td><td>2500</td></tr></table>

Being among the ® rst of SPC’ s units to complete the measure generation phase of the restructuring project, the CIS department started with the implementation of its ideas in January/February 1995.

While the restructuring project was certainly the ® nal trigger for overhauling SPC’ s information systems (IS) infrastructure, CIS’s management had already been worried about the state of its systems for some time.

We recognized we had to do something about these systems. With regard to the AMAPS system, we dropped maintenance because the software vendor did not have what we want. On the ® nancial side we did a study in client server systems back in 1991 or 1992.

We also had to think about the Year 2000 problem and we wanted to have systems that are more integrated. In CIS, we certainly felt that integration was important because each one of these systems ± AMAPS, the ® nancial systems ± were all separate. And then ± we traditionally were responsible for writing interfaces to these machines. We spent a considerable amount of time writing or updating interfaces and this was costing us too much money.

CIS knew that developing a new system from scratch was not an option. While the department had been in charge of setting up and maintaining business packages such as AMAPS or PERMAC in the past, it had never developed any of these larger programs from scratch. To complement their expertise, CIS would have to hire additional IT staff from outside. However, this would have compromised SPC’s restructuring plans, which called for signi® cant head count reductions across the entire company.

## But what package?

CIS was now left with the question of what software package to pick to meet SPC’s various requirements.

It was felt that, at the very least, the new system should (1) seamlessly integrate SPC’ s ® nance, purchasing, materials planning, plant maintenance and nuclear materials functions, (2) solve the Year 2000 problem, (3) be reliable and affordable and (4) have the ¯ exibility to support SPC’ s speci® c business processes. CIS quickly realized that all of these requirements were probably best met by one particular type of package: enterprise resource planning software or ERP.

## What is ERP software?

The term ERP was reportedly coined by analysts at the Gartner Group. ERP software is designed to model and automate many of the basic processes of a company, from ® nance to the shop ¯ oor, with the goal of integrating information across the company and eliminating complex, expensive links between computer systems that were never meant to talk to each other (CIO, 1997).

As part of their design, integrated systems allow information to enter at a single point in the process (for example, at the materials receiving stage of a manufacturing process) and update a database for all functions that directly or indirectly depend on this information. This integration should take place in real-time, not through interfaces or programs that transfer information to one or more modules only after the information has already been processed and updated in the module through which it entered the system. Once placed into the system, the information should be available in all the necessary forms through which it may be accessed, throughout the system (Lozinsky, 1998, p. 16).

ERP systems are sold by many different vendors. The ® ve most well-known are SAP, Oracle, PeopleSoft, Baan and JD Edwards. While they compete with each other in the same market, it is important to note that their systems differ signi® cantly from each other. Each system has its strengths and weaknesses, which are rooted in its individual development history. None of the systems is superior in every respect and how well it can support a particular business is very much determined by the ® t of its design characteristics with the requirements of the customer’s business.

SAP AG, a German software company, was one of the ® rst vendors in the ERP market. It started its business in 1972 and soon enjoyed moderate success (mainly in Europe) with its ® rst major package called R2 (R2 stands for release 2 and R/3 stands for release 3). The problem with R2 was, however, that its architecture was mainframe centric and its user interface extremely cumbersome. SAP’s chances to extend its business beyond Europe appeared limited. However, when \`client/server’ architecture became popular, SAP revamped its system to bene® t from the new approach. The result was R/3 ± a client/serverbased ERP system that offers R2’s advantages, while overcoming many of its weaknesses including the user interface problem. Today, SAP enjoys major success worldwide (currently, having 16 500 installations) (see: http://www.sap.com). It is the market leader in ERP software and the fourth largest software company overall.

## Preparing the ground for going with SAP R/3

Focusing on ERP, CIS management went to work on collecting the necessary information on which top management could base a sound decision for a particular package. In particular, they wanted to understand how well the various systems could support SPC’s needs and what resources (e.g. time, money and expertise) it would take to install them.

As a primary source of information, CIS sought out other mid-sized companies that would share their respective implementation experiences with SPC. Most of the data collection effort was done by telephone. However, when CIS learned about an implementation effort that was very similar to their own project, they arranged for a site visit to take a closer look at the installation.

The only visit we made was to Comdex Computers in Dallas. They were very much like us and this is why we went there: they also make a highly engineered product which is very expensive but only sold at low volumes. Comdex was one of the few we found with a really good manufacturing implementation. They did the implementation pretty well with a limited amount of support people. But it was hard to ® nd a company like them. A lot of my time I was just calling people trying to get into places or trying to talk to people who have gone through this (CIS management).

While CIS looked at various systems, from the outset their research effort was mainly geared towards learning whether SAP’s R/3 software would be capable of meeting SPC’s requirements. The reason for their narrow focus was that, years ago, Siemens AG had bought a large number of SAP software licences that it had intended to disseminate gradually throughout its entire organization. Siemens’ subsidiaries could purchase these licences through SNI (Siemens Nixdorf ± a systems integrator) at a signi® cant discount. This and the fact that it was/is corporate policy \`to go with SAP’, made it the \`system of choice’ for CIS.

I knew that I had to look at SAP because Siemens had this agreement con® rmed to give us a good deal on it. So if we had said we wanted to buy Oracle Software, somebody at Siemens would say, why did you not look at SAP? So the very ® rst thing we had to do was to look at SAP and to see whether it would work. Quite honestly, we did not look at much else (CIS management).

We identi® ed pros and cons of different software. I think if we had developed a very strong case for something other than SAP, we would have had the possibility to choose something else. But the fact is that we did not have anything that would cause us to say that we absolutely cannot use SAP (CIS management).

Interestingly, SPC’ s top management viewed the decision-making process as much less dependent on the \`Siemens condition’ than did CIS.

We were predisposed to SAP for quite a while. For what reason I am not sure I know. But the CIS people obviously kept up to speed on those kinds of things and saw this thing called SAP and all the wonderful things that they claimed it could do. So I think we were predisposed that way, regardless of the Siemens licence deal. I do not think the decision process would have been a lot different without the Siemens deal. We ± as the management ± actually required, however, an assessment of other vendors. We did not really challenge how detailed that effort was, but I am guessing it was pretty sketchy. There was at least an effort, a presentation made, as to why we felt that SAP was what we needed for replacing certain applications for particular tasks. And the management accepted that as an enough of a look at others to be satis® ed (SPC top management).

Despite their predisposition towards SAP R/3, CIS decided to conduct a more comprehensive analysis to assess the ® t and features of the SAP R/3 software before ® nally recommending the package to SPC’s top management. By now they knew that R/3 was a very powerful package, if not the silver bullet many would have hoped for: \`It becomes to me choosing the lesser evil. It is not that any one package is necessarily good. It is what is the least amount bad!’

## SAP R/3 ± in a nutshell

R/3 provides a set of business applications designed for the client/server environment. It consists of approximately 80 highly integrated modules which support the major business functions, including human resources, ® nance/accounting, manufacturing/logistics and sales/distribution, on a real-time basis. The software modules are designed according to \`best business/industry practices’ and can be con® gured so that they map an organization’s activities encompassing everything from corporate structure down to the speci® cs of pricing discounts.

Thus, among the advantages widely associated with implementing SAP R/3 is its promise to provide an organization’s workforce with access to information on a real-time basis from across the entire company. Furthermore, it promises cost reductions through increased productivity, re-engineered business processes and improved information ¯ ows for decision making. Finally, due to its seamless integration across different organizational functions, R/3 encourages if not requires teamwork during both implementation and use.

Despite these advantages, R/3 is not without problems of its own. Among the most severe is that its entire architecture is based on late 1980s client/server architecture. Further, its con® guration is limited to the \`SAP way’ of doing business, thus forcing many organizations to change their way of operating rather than being able to adapt the software to their needs. Moreover, R/3’ s high level of integration makes it very complex and, thus, hard to con® gure. Usually, outside help provided by specialized consulting ® rms is required to ensure successful implementation. Consultant help is, however, often hard to come by and very costly. Finally, even with support from experienced consultants, many SAP projects suffer from both cost and time overruns, with ® gures reaching 200± 300% not being uncommon. No wonder then that \`horror stories’ abound, causing many organizations to think twice about whether SAP R/3 is worth the risk.

## Seeking external help ± choosing an SAP consultant

To compensate for its own lack of SAP expertise, CIS looked around for consulting help to support them in their analysis. They requested bids from three different consulting ® rms: SNI (Siemens Nixdorf Ltd), IBM and Hewlett Packard. Other, more well-known SAP systems integrators, such as Price Waterhouse, Andersen Consulting or Coopers & Lybrand, were not approached.

SNI said they could do this for us. And we thought it would be good way of learning how SAP would ® t our business processes. But I really felt that we should at least call some other companies about this. Just to see. Since I have a lot of faith in IBM, I asked them to make a bid for the implementation analysis as well. I also got information from Siemens

Medical who used ABC Consulting\* for the planning, but now their project was on hold. I noticed that for the implementation analysis, Siemens Medical had requested six bids. And three of the larger systems integrators did not even bid because they were too busy. So ± because of where we are located and because of our size ± I did not think that we would get a competitive bid from any one of the Big 5 companies. They would not bother with us. But with IBM we had a good relationship and so we did get a bid from them. We turned them down because I felt they did not have anybody on the team with suf® cient manufacturing experience. On top of that they were more expensive than SNI. Bob from Siemens Stromberg Carlson who was working with SNI told me he was very impressed with their performance. So we ® nally went with SNI.

The implementation analysis (IA) started in summer 1995 and took approximately 3 months. Constituting an important part of SNI’s methodology, the IA represents a \`theoretical SAP implementation’ in the course of which the consulting ® rm conducts numerous workshops with the client to understand its speci® c business requirements. Understanding these requirements is a necessary precondition for its subsequent assessment of how well SAP’s R/3 software can satisfy the data processing needs of the client ® rm.

Based on its IA assessment, SNI developed a detailed work plan for the SAP project as well as an estimate of the associated consulting costs. The results of the IA were summarized by SNI in its IA report in the following way: \`According to the answers given by SPC, the available functionality matches the requirements of SPC to a level of 100% in the Controlling and Financial Accounting Modules. Materials Management has a 90% ® t. Production Planning has a 70% ® t. There are no requirements in Sales and Distribution. In the remainder of the R/3 modules there are some exceptions. All the noted exceptions can be resolved with either process-reengineering or enhancements to SAP.’ SNI’s assessment con® rmed SPC’ s impression of the usefulness of SAP to their business.

When we really took a look at it, we could not ® nd a reason why we would fail. We felt we had a good ® t. We had already decided that it looked like as if we would be successful. SNI con® rmed that with the analysis (SPC project manager).

In autumn 1995, shortly after the IA was completed, SPC’s top management made the ® nal decision to go with SAP. Overall, the anticipated scope of SPC’s

SAP implementation involved integrating the ® nancial, MRP and plant maintenance data working from a single integrated database. In the context of the overall restructuring effort, the SAP project was by far the largest single subproject: the original budget was \$5 million. However, top management authorized, only \$4 million, holding back \$1 million in case something went wrong. Approximately 220 users were scheduled to work on the system by September 1997.

At the same time that SPC’s management decided to go with SAP, it also decided to hire SNI for the remainder of the project. However, while the decision to go with SAP R/3 was a logical consequence of what SPC knew about the package, the reasons for why SPC decided to stick with SNI were not quite as apparent. For example, neither project management nor CIS were convinced that SNI’s 3 months long IA project helped them in any way to get up to speed with regard to the actual implementation.

We spent a lot of money on the IA. It did not get us any closer to installing the software and of getting it up and running. It got me a lot further along in my expense column. I think what it taught us ± more than anything else ± was how expensive it is to do SAP! (SPC project management).

I never felt that the IA helped anybody. When SNI ® nally started the project in fall 1995 it was like starting all over from scratch. I felt more uncomfortable than before because nobody could really demonstrate how it would be done. We could not get any PM [plant maintenance] consultants to talk to us. And there were a lot of consultants that just came and went. Maybe the IA effort got the users aware of how big it would be. But it also got some users mad because they felt they would not be part of it. And then people would ® nd horror stories about SAP because they had not committed to it. There was a lot of anxiety (CIS management).

Maybe worse, some of SNI’s most fundamental recommendations did not even appear to make sense to SPC in the light of its present situation.

It is really dif® cult for someone who is working in the client’s business to really know whether or not to go with the big bang. Your advice is limited to and based on the experience of the consultants who are recommending the implementation to you. SNI will recommend the big bang. Why? That is what they did in the last two implementations. That is what they did back at the fertilizer company. Well, it blew up after they implemented it, but at least they got it implemented on time. That is one reason why, when I looked at it, I did not feel comfortable with it (SPC project manager).

## Adopting SAP at Siemens

SNI had originally recommended the big bang because of the weak ® nancial situation of its client as well as the limited amount of time left before the September 1997 deadline. Implementing SAP R/3 with a big bang approach is, however, fairly risky as it requires going \`live’ with all the newly implemented SAP modules at the same time. Furthermore, because all implementation activities have to occur in parallel rather than sequentially, the big bang approach needs signi® cant resources at one time ± resources that SPC did not have.

The big bang approach was an approach that was used early on with SAP and in a lot of implementation efforts by our consulting partners. And it was recommended to us by SNI. We turned them down on that. And the reason for that is that it required more resources than I typically have available (SPC project manager).

While less risky, the phased approach is generally slower and more expensive than the big bang. This is mainly because temporary interfaces have to be written that connect parts of the existing (but soon-to-bereplaced) system with the newly implemented SAP modules to ensure uninterrupted data processing during the period of the SAP project. In addition, some of the con® guration performed in earlier phases of the project may need to be adjusted in later phases to accommodate for necessary changes when additional SAP modules are linked to the system.

Avoiding the big bang approach, SPC planned to divide the SAP implementation into three major phases. During the ® rst phase, the ® nance, controlling, account receivables, accounts payable, purchasing and essential material modules were to be put in. This was to be followed by the rest of the materials management module and the production planning and quality management modules. Finally, in a last step, the plant maintenance module was to be implemented (see Figure 2).

The SAP modules would have permanent interfaces to several existing systems such as payroll, Leitstand and freight-billing. (Leitstand is a PC-based production scheduling system that offers excellent graphical representations of the outcome of the scheduling process. SPC regards it as a \`best of breed’ stand-alone application. Since SAP does not excel in providing graphical output, it was decided to leave the Leitstand system outside of SAP.) With regard to timing, phase 1 was to be completed in September 1996, phase 2 was due in April 1997 and phase 3’ s completion date was planned to coincide with the overall end of the restructuring project, September 1997.

Despite their concerns, SPC decided to hire SNI as their systems integrator. As the conditions in SPC’ s contract with SNI show, however, SPC’s project management was aware of the risk involved. Learning from their experience during the IA, SPC insisted on the right to remove SNI consultants whose performance it considered unsatisfactory. In particular, no inexperienced consultants were to be tolerated. However, SPC permitted SNI to use its project as a training ground for inexperienced consultants provided no fees were assessed and the project was not disturbed. SNI also had to commit itself to transfer knowledge wherever possible. That would allow SPC to save money on off-site user and developer training. Further, SPC would not be liable for any cost overruns in consulting fees beyond 20% over the \$1.4 million estimated during the IA. Finally, SNI agreed on consulting fees that were low compared to average market prices. Clearly these conditions were not favourable for SNI. However, at the time, SNI was only a minor player in the USA and, thus, quite willing to make compromises.

![](/api/attachments/R5QYHGDB/fulltext/images/d3173b132de4307b1ab3dd67ea8eb084b93918b3bd85f1ead3fa5f82cd3ec889.jpg)  
Figure 2 General approach to implementation (time line)

Whenever a new consultant came in and we had lost one through no fault of mine, Siemens Nixdorf had to make an adjustment with the billing. That was by mutual agreement. I did not put a gun to their head but I do know how to negotiate a tough contract. And I would have expected that they would come around. It would have been harder to get the same conditions from one of the Big 5. But on the positive side ± SNI has now an installation here that they are more than happy to give as a reference (SPC project manager).

## Deciding upon hardware

Finally, only one major decision remained to be made before the implementation could start: the hardware ± what to buy and where from? After seriously considering bids from Hewlett Packard and IBM, SPC opted to buy a Pyramid 600/320 computer running the Sinix OS.

From the outset, CIS was in favour of buying a Hewlett Packard machine. Over the past 7 years they had developed an effective working relationship with Hewlett Packard. In addition, they knew that if problems occurred they would not have to go through a lot of trouble to have it ® xed since Hewlett Packard’s customer support was very good. Similar reasoning could be applied in IBM’s case. Despite the dispute over the lease versus buy of IBM’s operating system, SPC had faith in IBM’s capability to deliver on its promises. With regard to Pyramid, however, the situation was different. Pyramid, a Siemens company, was a relatively new player in the US market and, thus, did not yet have in place a customer support system that would match those of its competitors. While initially both Hewlett Packard’s and IBM’s bids were signi® cantly lower than Pyramid’s, Pyramid eventually matched its competitors’ offers and promised ± should the need arise ± to do everything in its power to help SPC overcome potential problems. They would even ¯ y in spare parts from Germany within less than 24 h if necessary. With promises like this, SPC’ s top management felt that the reasons against Pyramid’s offer were not signi® cant enough to justify a decision in favour of a non-Siemens company.

## A ® rst success

In October 1996 SPC went live with its ® rst set of SAP modules. Beating the odds typically associated with SAP R/3 implementations, SPC had completed the ® rst phase of its project on time and below budget. The cooperation with the SNI consultants had worked out very well. Furthermore, some unexpected as well as anticipated bene® ts associated with SAP had already started to materialize. The SAP-driven integration of SPC’s business functions began bearing fruit in rendering operations more ef® cient and promoting increased cooperation between the people working in different departments.

I believe the SAP system will have a tremendous effect. We restructured and tried to reorganize in anticipation of those improved interfaces. For some we have kind of bet on the come and I am very hopeful that they will in fact occur. People talk to one another. We all work with the same common database, sharing the same information. That has to help improve communication. And I am guessing when the software is fully implemented we may ® nd some further strengthening or restructuring organizationally may in fact be valuable to get full bene® t out of that. In other words, this passes across organizational lines and questions whether we need that organizational line there at all? Would it improve things if this line did not exist? (SPC top manager).

It would, however, be far too simple to assume that just about everything went well when the ® rst SAP modules went into production. For example, regarding the end users of the system, SPC’s project manager was faced with some major acceptability problems.

It is kind of funny because the users hated the system in the beginning because it was so hard to understand. And the other thing was that I did not put them through a lot of education and training. I cannot afford all that. So sometimes we had to tell them to do it by rote. You need to know that if you want to place an order, this is what you have to do.

To compensate for the lack of formal training, project management put a lot of effort into the preparation of narrative descriptions that would guide users through the individual steps of performing speci® c transactions. In addition, much time was spent on oneon-one training, prompt addressing of user concerns and, last but not least, encouragement of users to help each other.

Our project manager sure has been a terri® c help. For all three of our departments. When we need him, he comes to us and helps us with whatever problem we are having. But we are pretty much on our own with a lot of it (user, accounts payable module).

We had group meetings amongst ourselves where we shared information and learnt about problems we encountered! (user, essential materials module).

Approximately 3 months after the cut-over, the end users had indeed gradually become more familiar with the software and had begun to see its advantages as they explored the system.

At the time of the data collection for this case (January 1997), the SPC’s SAP project was in the middle of its second phase. Even though many of SPC’s managers were much more con® dent about the ® nal success of their project than they were when the project started, the remaining risk is still considerable.

On a scale from 1 (low risk) to 5 (high risk), I would personally put it now at about 2. From a 5 in fall 1995 to a 2. I think there is still some risk and we have only seen one module really up and running ± the ® nance<sup>\*</sup> module. But based on our tremendous success in getting the system running on time and the fact that the bene® ts that we have already seen have exceeded our expectations, the

## Adopting SAP at Siemens

risk has come down signi® cantly. But it is not 1! There are some big modules yet to do and communication may not have been the best. And of course, we will have some acceptance issues, when they [the remaining modules] come in. But the risk associated with the project has turned around in my mind signi® cantly. I feel much better now than I did when the decision was made. I was very nervous! (SPC top manager).

## Assignment/Questions

(1) How do SPC’s reasons for making the move to ERP and SAP compare to those of other companies as described in the trade press? Do SPC’ s reasons make sense?

(2) In deciding to adopt SAP, did SPC prepare itself well for implementation? Is the company likely to avoid common pitfalls?

(3) What is the nature and magnitude of the remaining risk in the implementation as of January 1997?

## References

Bancroft, N., Seip, H. and Sprengel, A. (1998) Implementing SAP R/3: How to Introduce a Large System into a Large Organization (Manning, Greenwich).

Lozinsky, S. (1998) Enterprise-wide Software Solutions: Integration Strategies and Practices, (Addison-Wesley, Reading, MA).

## Address for correspondence:

Sabrine Gabriele Hirt, The Anderson School at UCLA, Department of Information Systems, 110 Westwood Plaza, Los Angeles, CA 90095, USA.
