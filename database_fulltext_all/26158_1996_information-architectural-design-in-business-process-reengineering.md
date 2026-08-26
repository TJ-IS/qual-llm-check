---
otero_id: 26158
otero_key: "CSC7DNQK"
title: "Information Architectural Design in Business Process Reengineering"
authors: "William J. Kettinger; James T.C. Teng; Subashish Guha"
year: "1996"
journal: "Journal of Information Technology"
doi: "10.1177/026839629601100103"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information architectural design in business process reengineering

WILLIAM J. KETTINGER, JAMES T.C. TENG and SUBASHISH GUHA Department of Management Science, College of B usiness Administration, University of South Carolina, Columbia, SC 29208, , USA

Business process reengineering and information architecture share a common strategic and business process focus. Both can be mutually supportive of each other’s objectives. Information architecture design can produce a stable IA capable of supporting existing as well as improved business processes. Reciprocally, business process redesign (BPR) provides a high pro® le business justi® cation for the IA endeavour. Given proper collaboration between corporate and IT strategic planners, both BPR and IA efforts should produce a number of valuable common outputs. These include the identi® cation of business processes within an organization, the prioritization of these processes based on their strategic relevance, the establishment of process performance measures, and the modelling of these processes and their supporting information resources. A synergistic model of IA and BPR is presented and selected IA techniques and modelling methods are recommended. Future research is suggested concerning the need to test the relationship between BPR and IA.

## Introduction

Over the last ten years, dramatic economic, political and structural forces have altered the nature of organizations. To address these dynamic changes, many corporations have embarked on campaigns fundamentally to redesign their business processes to enhance productivity and competitiveness (Alter, 1990; McCormick, 1991). For example, a recent survey of 465 senior executives from large international companies found that 60% of those surveyed were actively involved in some sort of reengineering projects and that the principal factors driving these reengineering efforts were the desire for increased process speed (45%), reduced cost (21%), improved service (16%), improved quality (10%) and increased revenue (10%) (Tendiman, 1992). Typically, business process redesign (BPR) has been driven by such causes as downsizing, mergers, leveraged buyouts and acquisitions, productivity or quality improvement initiatives, and customer demands for product ¯ exibility and innovation (Hammer, 1990).

Moving in tandem with this recent popular attention to BPR has been a more subdued, but equally signi® cant, management initiative within the information systems (IS) community to focus on information as a strategic resource of the ® rm. A recent Delphi study conducted among senior IS executives identi® ed the development of an information architecture as the most critical issue facing IS managers in the 1990s (Niederman et al., 1991). This focus has emphasized the vital need to design a corporate information architecture (IA) to support dynamic competitive strategies and processes.

As we will demonstrate later in this paper, these two critical corporate agenda items (BPR and IA) share a communality in that their success hinges on the identi® - cation and design of ef® cient and effective business processes. Although not formally discussed in the IS research, references to the link between BPR and IA have been inferred. As an early observer of the phenomenon, Martin (1982) described instances of IA-induced process improvement. Goodhue et al. also uncovered that one of the potential outcomes of IA efforts is to \`creatively rethink business processes, allowing innovation and streamlining of some processes and possible elimination of others that are no longer essential’ (Goodhue et al., 1992, p. 14).

It is hoped that this paper will begin to bring some synergy to methodologies used in both IA and BPR and offer initial guidelines in the use of IA to assist in the redesign of organizational processes. We will begin by discussing the origins and current state of information architecture and BPR. We then will establish the conceptual relationship between IA and BPR, which will be validated by a case analysis. Finally, we will conclude by discussing how selected IA techniques and modelling methods may be applied to BPR and by highlighting areas for future research.

## The move to information architecture

The information architecture concept has humble beginnings. In fact, the development of computer-based information systems ® rst employed a ® le-oriented approach that had as its emphasis the programme rather than the data. In these early ® le oriented applications, data was typically not formally de® ned outside of the programme. The redundancy, inconsistency, and in¯ exibility that resulted from these ® le oriented applications eventually led to the acceptance of database management technology (Bachman, 1969; COADAYSL, 1971) based on the 3-schema architecture: external models (subschemas), conceptual model (schema), and internal model (ANSI, 1975).

The database concept of data independence brought with it the realization that the centre of the data processing universe was the data rather than the application programme (Nolan, 1973; Everest, 1974). Through its conceptual model (schema), data independence calls for the design of a stable database structure that is capable of supporting several related applications each with its own external view. To the extent that the conceptual model is properly designed, this goal of data independence is achievable even when some modi® - cations to the external views become necessary. Methods for the logical design of shared databases were advanced greatly by the development of relational database theories and accompanying normalization techniques (Codd, 1971).

IS researchers and developers soon recognized that if a particular subject database could provide a stable data structure for a group of related applications, a set of such databases could also support enterprise-wide information requirements. Researchers\* such as Brancheau and Wetherbe (1986) de® ned:

An information architecture as a high-level map of the information requirements of an organization. It is a personnel-, organization-, and technology-independent pro® le of the major information categories used within an enterprise (Brancheau and Wetherbe, 1986, p. 453).

This macro/architectural approach to structure the entire organization’s information resources was the major thrust of the early IA approach, BSP (business systems planning) developed by the IBM Corporation in 1975. As outlined in BSP, a collection of \`data classes’ can be systematically identi® ed and con® gured to drive the entire organization’s information needs (IBM Corp, 1984). One representation of this high-level map is a process/data class matrix which shows how data classes (information categories) support information requirements of various business processes in the organization, as shown in Figure 1. Vogel and Wetherbe (1991) reported the successful application of this matrix representation in several organizations.

Another representation of IA is the enterprise data model which is typically accomplished via high-level E± R models for the organization. The model reveals Entity relationship data. Martin (1990, vol. 2) and Sowa and Zachman (1992b), in developing information engineering (IE) to help implement IA, de® ne business processes as having two important characteristics: ® rst, processes are not based on organizational structure and can cross functional boundaries; and second, processes should identify what is done, thus emphasizing de® ned business outcomes. Martin (1990) takes further steps to enrich process-oriented IA by incorporating the critical success factors (CSF) method, entity± relationship data modelling, process modelling, and a number of other advanced techniques.

Everest and Kim (1989, p. 6) describe information architecture as \`blueprints or diagrams which re¯ ect, satisfy, and adapt to the needs of business functions, operations, and decision making’. Using this blueprint as a basis, information engineering involves \`the planning, designing, constructing, or managing’ of information architecture using a methodology and a set of formal techniques (Everest and Kim, 1989, p. 7). Information engineering is, then, the recognition that a proactive and implementable approach to IA is needed. At Pillsbury USA Foods, for example, the enterprise data model was presented on 21 pages with two levels of details (Brancheau et al, 1989). Conducted in conjunction with the identi® cation of business processes, enterprise data modelling produces a map for actual database development. Based on these concepts, we de® ne information architecture as:

a high-level model of a set of data classes con® gured to support the organization’s value-adding business processes. The model may be portrayed in graphical form and is independent of technology and organizational structure.

We use the word \`con® gure’ because architecture should be the outcome of a purposeful design. It is customary to present architecture in a graphical blueprint. The last part of our de® nition reaf® rms the abstract nature of the design, following the data independence principle. In recent years, research on IA has continued to advance, and a number of new approaches may further improve its conceptual clarity and practical applicability (Ebels and Stegwee, 1992; Hars and Scheer, 1992).

<table><tr><td>Processes\Data Classes</td><td>Objectives</td><td>Policies &amp; Procedures</td><td>Organization Unit Desc</td><td>Product Forecasts</td><td>Bldg &amp; Real Estate Reqt</td><td>Equipment Requirements</td><td>Organization Unit Budget</td><td>G/L Accounts Desc &amp; Budget</td><td>Long Term Debt</td><td>Employee Requirements</td><td>Legal Requirements</td><td>Competitor</td><td>Marketplace</td><td>Product Description</td><td>Raw Material Description</td><td>Vendor Description</td><td>Buy Order</td><td>Product Warehouse Inventory</td></tr><tr><td>Establish Business Direction</td><td>C</td><td>C</td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td>U</td><td>U</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Forecast Product Requirements</td><td>U</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Determine Facility &amp; Eqt. Requests</td><td>U</td><td></td><td>U</td><td></td><td>C</td><td>C</td><td></td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Determine &amp; Control Fin Requests</td><td>U</td><td></td><td>U</td><td></td><td></td><td></td><td>C</td><td>C</td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Determine Personnel Requests</td><td></td><td>U</td><td>U</td><td></td><td>U</td><td>U</td><td>U</td><td>U</td><td></td><td>C</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Comply with Legal Requests</td><td></td><td>U</td><td></td><td></td><td></td><td></td><td></td><td>U</td><td></td><td></td><td>C</td><td></td><td></td><td>U</td><td></td><td>C</td><td>C</td><td></td></tr><tr><td>Analyze Marketplace</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>C</td><td>C</td><td></td><td></td><td></td><td>U</td><td></td></tr><tr><td>Design Product</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td>U</td><td></td><td>C</td><td>C</td><td></td><td></td><td></td></tr><tr><td>Buy Finished Goods</td><td></td><td></td><td></td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td></td><td>C</td><td>C</td><td></td></tr><tr><td>Control Product Inventory</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td></td><td></td><td>U</td><td>C</td></tr><tr><td>Ship Product</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td></tr><tr><td>Advertise and Promote Product</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td>U</td><td></td><td></td><td></td><td>U</td></tr><tr><td>Market Product (Wholesale)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td>U</td><td>U</td><td></td><td></td><td></td><td></td></tr></table>

Figure 1 Information architecture as represented by a process/data class matrix (C = create; U = use)

While conceptually appealing, the widespread implementation of information architecture has not always met with success. For example, BSP’s comprehensive 13 step methodology has been criticized for requiring too many interviews, taking too long to complete, and often producing voluminous output without visible impacts (Rockart, 1979; Goodhue et al., 1988; Lederer and Sethi, 1988). Attempting to accomplish the major objectives of BSP with greater ease, later IA methods attempted to simplify its complicated procedures and incorporated additional techniques such as critical success factors and the entity± relationship approach to enterprise data modelling (Martin, 1982; McFadden and Hoffer, 1991). These later methods require less time and resources to complete and are generally more ef® cient. This ef® ciency has been further enhanced by means of a number of CASE tools that provide automated support to enterprise-wide modelling and system planning (Katz, 1990). Thus, the historical development of information systems has progressed from programme-centred, ® le oriented applications to isolated databases, to enterprise-wide information architectural design.

## The move to business process reengineering

Organizational theorists propose that the organization of the future will be networked across functions and designed around business processes rather than functional hierarchies (Drucker, 1988; Norton et al., 1989; Rockart and Short, 1989).\* Reengineering business processes is now being offered as a paradigm of organizational change necessary in order to achieve the requisite ¯ exibility and competitiveness of the networked organization (Hammer, 1990; Venkatraman, 1991). In this way, BPR can be conceived as an organizational initiative to regain control of seemingly intractable business processes by streamlining and refocusing how a company operates.

BPR tends to be radical in nature and strives for fundamental structural change. The breadth and depth of these changes make it imperative that BPR be planned and initiated at the strategic level by top management in order to enhance the likelihood of success (Keen, 1991). Based on this strategic orientation, we de® ne business process reengineering as:

a strategy-driven organizational initiative to fundamentally reexamine and redesign business processes with the objectives of achieving competitive breakthrough in quality, responsiveness, cost, satisfaction and other critical process performance measures.

In this way BPR is similar to IA, whose likelihood of success diminishes without strategic focus and managerial support (Goodhue et al., 1992).

The results of reengineering efforts have already begun to surface. For example, in 1989 Kodak reengineered its 1500-employee \`Zebra’ Group which is responsible for black and white ® lm operations. Before reengineering, the Zebra group was 15% over budget, took up to 42 days to ® ll an order, and was late one-third of the time. Focusing on customer satisfaction, the reengineered process turned this situation around and over a period of two years: costs were 15% below budget; response time was cut by half; and only one in 20 orders were late (Stewart, 1992). Other success stories include DEC’ s consolidation of 55 accounting groups into ® ve and elimination of 450 jobs (Krass, 1991) and the CIGNA RE Corporation’s savings of \$1.5 m each year in operations costs with improved access to data following reengineering (Ryan, 1991). Finally, the Ford Motor Corporation and AT&T reported increases in productivity and decreases in staff by about 80% after business reengineering (Krass, 1991).

While business processes can be reworked without IT, recent technological advances have placed greater importance on IT as an enabler of BPR. Increasingly, BPR is being deployed in tandem with the use of IT to revamp or overhaul existing business processes that limit effectiveness (Fried, 1991; Senn, 1991). Technologies such as local area networks (LANs), client-server architecture, electronic data interchange (EDI) and executive information systems (EIS) are some examples of IT which now allow ® rms to achieve performance gains in the communications dimensions of business processes. The emerging technologies of video/teleconferencing, groupware, imaging and work¯ ow technologies are proving to be important enablers of BPR by reducing or replacing manual tasks and improving communication (Huber, 1990).

To the extent that the process to be reengineered requires information processing and exchange, database technology and information architecture (IA) will be critical enablers. As Michael Treacy, a leading information technology consultant quotes:

systems already in place must be selectively destroyed and replaced by cross-functional systems that allow many departments to share a single \`information warehouse’ (Vowler, 1991, p. 18).

To achieve this level of sophistication in information management, it is important to implement an information architecture that supports information access by users in different departments whose work is tied to a common business process. While the association between BPR and other important IT enablers is worthy of future study, this paper targets its attention solely on the relationship between BPR and IA.

## IA and BPR as mutual facilitators

## The role of IA and databases in a BPR project

Traditional systems development tended to target speci-® c operations within a particular functional area. The resulting application systems typically did not readily accommodate changes in procedures and requirements because of their ® le-oriented design. For example, a traditional system development project of a typical accounts payable application may merely seek to automate existing procedures, rather than the entire process of paying vendors, which also involves the purchasing and receiving departments. However, guided by an information architecture, shared databases are capable of serving users in different functional areas. In following an IA approach, the emphasis is placed on identifying the entities that are involved in the entire process. For the payable process, the two critical entities are \`supplier’ and \`part’ . It should be noted that in modelling the underlying data structure, the ¯ exibility to accommodate changes in the payable procedures is gained.

Herein lies a common thrust of IA and BPR, with both having a common focus on process and both striving to crack the boundaries between functional areas. For example, the application of a shared database in reengineering a payable process at the Ford Motor Corporation is illustrated in Figure 2. The \`soul’ of Ford’s newly reengineered accounts payable process is a database shared by the purchasing, accounts payable, and receiving departments.

After reengineering, the purchasing department at the Ford Motor Corporation no longer sends purchasing orders to accounts payable, instead it simply enters the order into the central database (Hammer, 1990). When the goods arrive, the receiving clerk checks the database to see if an outstanding order corresponds to the arriving materials; if not, the materials are sent back to the supplier. Unlike the old system, which dictated that accounts payable clerks check 14 data items when matching the purchase order, receipt record and the invoice, the reengineered process requires the matching of only three data items: part number, supplier code and the unit of measurement. This simplicity can be achieved because the database is normalized and based on the two entities, namely, part and supplier. The uni® ed database schema is capable of serving three different subschemas from the three different departments taking part in the same business process. In the future, if the payable function and the purchasing function are combined, the same database schema will still be valid.

![](/api/attachments/CSC7DNQK/fulltext/images/4502cda1db309c47a899554dbc20b1a166adbf88e3e4d8559ee0b71b7f35801b.jpg)  
Figure 2 The reengineered accounts payable process at the Ford Motor Corporation

## IA as a facilitator for BPR: motives and outcomes

The case example above demonstrates that the design of information architecture, as manifested by the database structure, is supportive of reengineering. This approach forces the designer to adopt a cross-functional process orientation that is not restricted by existing procedures. With a common focus on business process the immediate question at hand is: how does information architecture facilitate business process redesign? To begin to address this question, Figure 3 shows the various relationships between IA and BPR. In an information architectural design, the objective is to produce an information architecture (link 1 in Figure 3) which consists of a set of data classes intended to support a collection of existing business processes (link 2). However, by supporting business processes through data classes, we strive to establish a more stable architectural foundation which may also be capable of supporting changes in business processes via data independence. Therefore, although the immediate bene® t of IA design is to support existing processes (link 2), the information architecture is in principle capable of supporting improved business processes as well (the dotted link 3).

The potential to improve business process through IA as indicated in link 3, has come to the attention of information architects as illustrated by the following remarks:

When we ® rst started this, we thought this was a technique for examining existing procedures. We discovered, a step at a time, that it’ s much more than that. First, we found that the existing procedures had been horrifyingly duplicated. . . . You had numerous different forms where one computerized form would suf® ce. . . . The procedures and the ¯ ow of work had anomalies . . . the management structure itself was wrong. It needed a thorough reorganization of the departments and even divisions in order to get tight control and high administrative productivity (Martin, 1982, pp. 141± 42).

This recognition suggests that efforts to build shared databases and an information architecture to support cross-functional business processes may lead to business process redesign (the dotted link 4). A case in point occurred at Syntex Corporation, a pharmaceutical manufacturer. Moad (1989) reported that the ® rm started to build a cross-functional IS using relational database technology to track the full life cycle of its products, but encountered severe user resistance from the affected functions. Eventually, the project team began to use \`structured data¯ ow and organizational analysis to determine exactly how work got done in the business unit’ and \`discovered that between 30% and 50% of the tasks people were doing were redundant’ (Moad, 1989, p. 74). With top management endorsement, the team began to redesign certain aspects of the process to take full advantage of IA and shared databases (link 5).

![](/api/attachments/CSC7DNQK/fulltext/images/c5767730342d24410dd05c5a6e05369b24682a0eadfda4ec0ea5860b737e2c4b.jpg)  
Figure 3 IA as a facilitator for BPR: motives and outcomes

## BPR as a facilitator of IA

We have discussed the facilitating role of IA in BPR. The reciprocal question is: can BPR facilitate IA? Despite its recognition as the most critical issue facing IS management (Niederman et al., 1991), a variety of implementation obstacles have prevented the widespread adoption of IA (Goodhue et al., 1992). One of the obstacles is the dif® culty in getting different functional units to share the same data resources and coordinate their activities accordingly (Martin, 1982). The organizational inertia preventing the implementation of IA may prove too great for the typical information system group to overcome (Goodhue et al., 1992). Speci® cally, lack of top management support, user resistance, and limited resource commitment may result in little understanding of the tangible bene® ts of IA beyond the technical interests of the IS department (Lederer and Sethi, 1991). However, since the driving force of BPR is business improvement rather than technical re® nement, the goals of BPR are more easily understood by top management and the functional departments involved. Under the \`political’ banner of BPR, IA may be merely viewed as an accompanied technical implementation issue that should be completed. Therefore, it is reasonable to expect that BPR would facilitate the IA cause.

## Striving for synergy between IA design and reengineering

We have shown that IA design and BPR have a common focus on business processes. To build further on the potential synergy between BPR and IA initiatives, it is important to recognize that both should be driven by the strategic thrusts of the organization. IA is an output of strategic data planning (SDP) (Martin, 1982; Goodhue et al., 1992), a critical component of IT strategic planning. Similarly, BPR is strategic. BPR typically has wide-ranging effects on internal operations and attempts breakthroughs in performance. The likelihood of success of BPR is diminished without strategic direction from top management. At the Xerox Corporation, for instance, a strategic business vision for BPR was developed by corporate management (Davenport and Short, 1990). In selecting business processes for redesign, IBM and Cigna determined the strategic relevance of all processes and then chose to reengineer those processes with the highest strategic pay-offs (Davenport, 1993).

While both of these planning activities have typically taken place in isolation, the integration of these planning efforts has been advocated by numerous authors (King,

1978; Earl, 1987). As can be seen in Figure 4, joint effort in delineating corporate strategic plans and IT strategic plans may result in output that is bene® cial to both efforts and, synergistically, of greater bene® t to the ® rm as a whole. Given the use of IT as a powerful competitive weapon (Porter and Milar, 1985; Synnott, 1987; Wiseman, 1988), such collaboration in planning is becoming even more imperative today.

Among the many outputs of this planning collaboration, four are identi® ed in Figure 4. These are identi® cation of business processes, prioritization of these processes, establishment of process performance measures, and modelling of processes. Corporate planners launching a BPR project can now look to their IT colleagues for assistance in identifying IA and other appropriate IT levers that will enable signi® cant breakthroughs in process redesign. Corporate executives can also work with IT planners in applying the critical success factors (CSF) method, a technique for strategic management (Rockart, 1979) and for prioritizing projects (Martin, 1990; McFadden and Hoffer, 1991; Vogel and Wetherbe, 1991). Furthermore, the determination of critical performance measures, such as product/ service quality, customer satisfaction and cycle time must be identi® ed for both process redesign and IA.

![](/api/attachments/CSC7DNQK/fulltext/images/b1621031e496e84c254901b1f099fadf6a5cbf337b0dc8aa0865f2a09369eba1.jpg)  
Figure 4 BPR and IA: achieving synergy through integration of corporate and IT strategic planning

Based on an integrated strategic thrust, as depicted in Figure 4, there are many areas in which IA and BPR can join forces to achieve synergy. In the remaining part of this section, a number of speci® c recommendations are proposed.

## Information architects as BPR team members

Our ® rst recommendation is to include information architects as vital members of a BPR team. These architects will be responsible for designing IA and shared databases for reengineered cross-functional business processes. Their involvement has two major bene® ts. First, an architect can point to parts of the IA of an organization that are immediately applicable to the current reengineering project, by providing common information resources to users in different functional areas involved in the same process. Secondly, as the competitive environment changes and the business adapts, the process may have to be reengineered again. However, this solid information architectural foundation will remain basically intact. For example, an accounts payable process may undergo additional changes, but there will always be a supplier entity and a part entity for the process. While changes in process and procedures will occur, data entities should last as long as the ® rm remains in the same business.

## The identi® cation of business processes

Before beginning BPR one must identify business processes within the ® rm. Some organizations may quickly pick a process to be reengineered based on some simple heuristic. The advantage of such a targeted approach may be a fast payoff and timeliness of project completion. An alternative to the targeted approach is the identi® cation of all the organizational business processes in a comprehensive fashion. This comprehensive approach can be labour intensive and time consuming; however, it can offer a well thought out rationale for BPR in terms of project prioritization that is consistent with corporate strategic goals. A number of organizations have adopted this comprehensive approach to BPR. For example, Rank Xerox UK began the BPR process by uncovering 18 \`macro’ business processes and 143 \`micro’ processes (Davenport and Short, 1990). Charles Schwab Corp.’s BPR team spent ® ve months building a global business model which encompasses 24 business processes (Bartholomew, 1991).

Methods for IA design can be readily utilized for comprehensive identi® cation of an organization’s business processes. In fact, the ® rst critical task in IA design calls for identifying business processes relative to the organization’s products, services and support resources as they pass through the four stages of their life cycle:

requirements, acquisition, stewardship and disposition. In the case of products, for example, typical business processes that can be identi® ed with this method include: new product design, market analysis, product requirements forecast (for the requirement stage), schedule and control, production (for the acquisition stage), inventory control and shipping (for the stewardship stage), advertising and promotion, product marketing, order entry and control (for the disposition stage) (IBM Corp., 1984, p. 31). In prior IS research, this notion of resource life cycle has been successfully applied as a basis for identifying opportunities for strategic IS applications (Ives and Learmonth, 1984). One important advantage in adopting the IA approach to processes identi® cation is that the business processes are not simply listed out in isolation. Rather, they are identi® ed in relation to data classes, data entities, functional departments, application systems, and so on (Martin, 1990). A comprehensive IA not only provides assistance in immediate project selection, but also provide a road map for prioritization and implementation of future reengineering projects. Finally, because the IA provides a blueprint of the information needs of the organization as a whole, bene® ts of cross-functional, intra- and inter-® rm systems integration can be realized.

## Prioritizing IA and BPR projects

Having identi® ed all business processes within the ® rm, the next step in either BPR or IA is to prioritize projects which are consistent with corporate strategic objectives. For IA projects, methods such as critical success factor (CSF) have been applied to prioritize the development of systems and subject databases (Brancheau and Wetherbe, 1986; McFadden and Hoffer, 1991; Vogel and Wetherbe, 1991). In the context of integrated corporate and IT strategic planning, a somewhat similar approach to the prioritization of BPR projects based on CSF can be used.

Planning matrices can be developed to facilitate BPR and IA. Two such matrices are depicted in Figure 5. First, a CSF/process matrix is prepared to identify those business processes that are essential (cells marked by the letter E) or desirable (cells marked by the letter D) to achieve the organization’ s critical success factors as determined by top executives (Bullen and Rockart, 1981; McFadden and Hoffer, 1991). This CSF/process matrix can be used to determine the strategic relevance of all business processes. A subset of these will be designated as \`strategic processes’ and become candidates for redesign. While selection criteria may differ by organization, a possible approach is to assign a value of 2 to E and a value of 1 to D. The resulting row total would then re¯ ect the overall strategic relevance of the process to the various critical success factors. For BPR, the highest row totals would receive top priority in project selection. The results of this analysis, when used in conjunction with cost and risk factors, should lead to a ® nal process selection. Future reengineering efforts could then be based on this same prioritization.

Critical Success Factors

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td><td> $C_6$ </td><td>Total</td></tr><tr><td> $P_1$ </td><td></td><td>E</td><td></td><td>D</td><td></td><td></td><td>3</td></tr><tr><td> $P_2$ </td><td></td><td></td><td>E</td><td></td><td>D</td><td>D</td><td>4</td></tr><tr><td> $P_3$ </td><td>E</td><td>D</td><td></td><td>D</td><td></td><td>D</td><td>5</td></tr><tr><td> $P_4$ </td><td></td><td></td><td></td><td>E</td><td></td><td></td><td>2</td></tr><tr><td> $P_5$ </td><td></td><td></td><td>D</td><td></td><td></td><td></td><td>1</td></tr><tr><td> $P_6$ </td><td></td><td>E</td><td>D</td><td></td><td>E</td><td>E</td><td>7</td></tr><tr><td> $P_7$ </td><td>D</td><td>E</td><td></td><td>E</td><td></td><td>D</td><td>6</td></tr><tr><td> $P_8$ </td><td>D</td><td></td><td>E</td><td>E</td><td></td><td></td><td>5</td></tr></table>

<table><tr><td></td><td> $E_1$ </td><td> $E_2$ </td><td> $E_3$ </td><td> $E_4$ </td><td> $E_5$ </td><td> $E_6$ </td><td> $E_7$ </td><td> $E_8$ </td></tr><tr><td> $P_6$ </td><td></td><td>C</td><td>U</td><td>U</td><td></td><td></td><td></td><td></td></tr><tr><td> $P_7$ </td><td>U</td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $P_3$ </td><td>C</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td>U</td></tr><tr><td> $P_8$ </td><td></td><td>U</td><td>U</td><td></td><td></td><td>U</td><td></td><td>C</td></tr><tr><td> $P_2$ </td><td>U</td><td></td><td></td><td></td><td></td><td>C</td><td></td><td>U</td></tr><tr><td> $P_1$ </td><td></td><td></td><td></td><td></td><td>C</td><td></td><td>U</td><td></td></tr><tr><td> $P_4$ </td><td></td><td></td><td></td><td>C</td><td>U</td><td></td><td></td><td></td></tr><tr><td> $P_5$ </td><td></td><td></td><td></td><td></td><td></td><td>U</td><td>C</td><td></td></tr></table>

Figure 5 BPR/IA planning matrices (E = essential (2 points); D = desirable (1 point); U = used; C = created)

For IA planning, the CSF/process matrix is also ® rst used to establish process priority. The prioritized processes are then listed along the vertical axis in the entities/processes matrix and entities are listed along the horizontal axis. The information architects then designates each cell with either the letter U if the entity is used by the corresponding process, or the letter C if the entity is created by the corresponding process. Those entities either used or created by the top three processes (or any number deemed appropriate) can be selected for database development.

## Establishing process performance measures

A critical step in BPR is to understand and measure the process (Davenport and Short, 1990). Hammer (1990, p. 108) emphasizes this point in stating the importance to \`organize around outcome, not tasks’ . To ensure that the outcome of a process is successful, it is necessary to establish criteria of effectiveness. Further, we must also be concerned with ef® ciency of the process, to minimize the resources needed to produce the outcome. Inappropriate measures for process performance are often the root cause of many fundamental problems in traditional functional hierarchies. For example, at Sears Automotive Service, sales quotas were used as a performance measure. This provided incentive for employees to charge customers for many needless repairs and eventually led to law suits against the company in several states (Kelly and Schine, 1992). To help establish appropriate process measures for BPR, the ends/means (E/M) analysis method developed for IA design (Wetherbe and Davis, 1983; Vogel and Wetherbe, 1991) may be used. Grounded in general systems theory, E/M analysis calls for the examination of two critical questions:

(1) Concerning effectiveness: what makes goods or services provided by this process effective to users or customers? What information or measures are needed to ensure that it is being effective at providing these goods or services?

(2) Concerning ef® ciency: how do you de® ne ef® ciency in providing goods or services by this process? What information or measures are needed to evaluate its ef® ciency?

Applying the E/M method to an automotive service ® rm we ask the question: what makes the service of the ® rm effective to the customers? This should lead to establishment of appropriate effectiveness measures such as customer satisfaction rather than sales revenue. Alternative techniques such as quality function deployment method (QFD) as outlined by Hauser and Clausing (1988) also provide detailed guidelines for establishing customer-based effectiveness measures.

## Process modelling

The success of both IA and BPR efforts depends on a thorough understanding of how a process works and with what resources. The resources of a process include people, material and information. Traditionally, the information requirements for a process are modelled with tools such as E± R diagrams by information architects, while the procedural aspects are modelled by systems analysts with techniques such as data ¯ ow diagrams. Information engineering, which represents an outgrowth of IA, includes speci® c guidelines, procedures and diagramming conventions for process modelling (Martin, 1990). In recent years, information modelling and procedural process modelling have begun to merge under the object-oriented paradigm which also encompasses concurrency, control and other process behaviours (Coad and Yourdon, 1990; Korson and McGregor, 1990). This uni® ed modelling approach offers BPR and IA analysts the capability to collaborate in modelling a business process.

The trend toward this uni® ed approach to process modelling can be seen in the evolution of IDEF (ICAM de® nition), a process de® nition and design methodology developed by the US Air Force in support of its integrated computer and manufacturing (ICAM) programme (Mayer et al., 1992b). Over the years, the methodology has progressed from the initial IDEF0 version, which extends beyond data ¯ ow analysis to capture the nature of a process. This is accomplished through a structured method with notations for inputs, outputs, controls and resources. The IDEF convention has continued to evolve to include support for information architectural design.\* For example, IDEF1 provides tools for identifying information resources in the enterprise, the logical relationships among information, and the rules governing its management. IDEF1X can be used to design relational databases, IDEF2 allows dynamic simulation of function, information and resources of the enterprise, and IDEF4 supports information integration in object-oriented data modelling. This architectural evolution has led to enterprise integration approaches as depicted in the IDEF6 concept paper that attempts to model the knowledge and rationale for process design (Mayer et al., 1992a). The IDEF family of process and information architectural modelling methods have exerted considerable in¯ uence on process reengineering practice, and software is now commercially available from a number of vendors that will facilitate the collaboration of BPR and IA analysts.

## Conclusions

Business process redesign and information architecture have been recognized as high priority agenda items in organizations in the 1990s. This paper provides the premise for integrating these two critical issues. In a synergistic relationship, IA and BPR are mutually supportive of each other’s objectives. Through IA, a solid base can be built in designing processes around stable entities, and many IA methods and techniques may be readily applied to BPR. Reciprocally, BPR provides a high pro® le business justi® cation for the IA endeavour, which has suffered many implementation obstacles in the past.

The synergy between BPR and IA stems from integration of corporate and IT strategic focus. Given proper collaboration between corporate and IT strategic planners, both BPR and IA efforts should produce a number of common outputs. These include the identi® cation of business processes within an organization, the prioritization of these processes based on their strategic relevance, the establishment of process performance measures, and the modelling of these processes and their supporting information resources.

We have conceptually demonstrated the rationale, bene® ts and approaches to integrating IA and BPR. It is recommended that future research empirically test these relationships. It would be interesting to analyse the process and outcome differences between cases of reengineering that implemented enterprise-wide IA as a part of their BPR strategy and those that did not. Likewise, it is important to determine the extent to which IA’s success can be enhanced when it is accompanied by BPR.

In the future, both researchers and practitioners should follow this trend of information architecture and business process redesign integration. In this vein, researchers continue to apply an architecture metaphor better to describe and integrate elements of the organization to achieve higher performance (Kosanke, 1992; Petrie, 1992; Sowa and Zachman, 1992b; Vernadat, 1992). For example, Sowa and Zachman (1992b) have extended ISA to modelling the entire organization by suggesting the need for, and an approach to, integration of data, function, network, people, time and motivation. This trend toward greater integration, ® rst through shared databases, then through information architecture, is now directed at multidimensional enterprise modelling encompassing not only data and IT but strategy, process, people and performance. The linkage between IA and BPR, which has been illustrated in this paper, is a ® rst step towards enterprise integration at the process level. In extending the architectural metaphor, future research can be expected to progress signi® cantly toward comprehensive integration at the organizational level.

## References

Alter, A.E. (1990) The corporate makeover. CIO, 32± 42.

ANSI X3 SPARC/DBMS (1975) Study Group Report. American National Standards Institute, Washington, DC, USA.

Bachman, C.W. (1969) Data base management: the keystone of applied systems architecture, in Critical Factors in Data Management, Gruenberge F. (ed) (Prentice-Hall, Englewood Cliffs, NJ), pp. 215 and 240.

Bartholomew, D. (1991) Charles Schwab: bullish on reengineering, complete overhaul of operations planned. Information week, 330, 12± 14.

Brancheau, J.C. and Wetherbe, J.C. (1986) Information architecture: methods and practice. Information Processing and Management, 22, 453± 63.

Brancheau, J.C., Schuster, L. and March, S.T. (1989) Building and implementing an information architecture. Data Base, 19, 9± 17.

Bullen, C.V. and Rockart, J.F. (1981) A Primer on Critical Success Factors. Center for Information Systems Research Working Paper No. 69 (June), Sloan School of Management, MIT, Cambridge, MA, USA.

Coad, P. and Yourdon, E. (1990) Object-Oriented Analysis (Yourdon Press, Prentice-Hall, Englewood Cliffs, NJ).

CODAYSL (1971) Systems Committee Technical Report, ACM, New York, London and Amsterdam.

Codd, E.F. (1971) A relational model of data for large shared data banks. Communications of the ACM, 13, 377± 87.

Davenport, T.H. (1993) Process Innovation: Reengineering Work Through Information Technology (Harvard Business School Press, Boston, MA).

Davenport, T.H. and Short, J.E. (1990) The new industrial engineering: information technology and business process redesign. Sloan Management Review, 31, N4, 11± 27.

Drucker, P.E. (1988) The coming of the new organization. Harvard Business Review, 66, 45± 53.

Earl, M. (1987) Information systems strategy foundation, in Critical Issues in Information Systems Research, Boland R. and Hirscheim R. (eds) (John Wiley & Sons, London).

Ebels, E.J. and Stegwee, R.A. (1992) A multiple methodology approach toward information architecture speci® cation, in Proceedings of the 1992 Information Resource Management Association (IRMA) Conference, Charleston, SC, USA, pp. 186± 93. May 20± 24.

Everest, G.C. (1974) Database management objectives, organizations, and system functions, unpublished doctoral dissertation, Dept of Management Science, University of Pennsylvania, Philadelphia, PA, USA.

Everest, G.C. and Kim, Y.G. (1989) Perspectives on Data Planning and Information Architectures. MISRC Working Paper WP-89-04, University of Minnesota, Minneapolis, MN, USA.

Fried, L. (1991) A blueprint for change. Computerworld, December 2, 25(48), 91± 95.

Goodhue, D.L., Quillard, J.A. and Rockart, J.F. (1988) Managing the data resource: a contingency perspective. MIS Quarterly, 12, 373± 91.

Goodhue, D.L., Kirach, L.J., Quillard, J.A. and Wybo, M.D. (1992) Strategic data planning: lessons from the ® eld. MIS Quarterly, 16, 11± 34.

Hammer, M. (1990) Reengineering works: don’t automate, obliterate. Harvard Business Review, 68, 104± 12.

Hars, A. and Scheer, A. (1992) Reference models for enterprise-wide data engineering, enterprise integration modeling, in Proceedings of the First International Conference, Petrie Jr, C.J. (ed) (The MIT Press, Cambridge, MA) pp. 320± 38.

Hauser, J.R. and Clausing, D.P. (1988) The house of quality. Harvard Business Review, 66, 63± 73.

Huber, G. (1990) A theory of the effect of advanced information technologies on organizational design,

intelligence, and decision making. Academy of Management Review, 15, 47± 71.

IBM Corp. (1984) Business Systems Planning: Information Systems Planning Guide fourth edition (July) (IBM Corp., White Plain, NY).

Ives, B. and Learmonth, G.P. (1984) The information system as a competitive weapon. Communications of the ACM, 27, 1183± 201.

Katz, R.L. (1990) Business/enterprise modeling. IBM Systems Journal, 29, 509± 25.

Keen, P.G.W. (1991) Shaping the Future: B usiness Design Through Information Technology (Harvard Business School Press, Cambridge, MA).

Kelly, K. and Schine, E. (1992) How did Sears blow a gasket? Business Week (June 29), 38. Issue 272.

King, W.R. (1978) Strategic planning for management information systems. MIS Quarterly, 7, 27± 37.

Korson, T. and McGregor, J.D. (1990) Understand objectoriented: a unifying paradigm. Communications of the ACM, 33, 39± 60.

Kosanke, K. (1992) CISOMA ± a European development for enterprise integration, part 1: an overview, in Enterprise Integration Modeling: Proceedings of the First International Conference, Petrie, C.J. (ed) (The MIT Press, Cambridge, MA) pp. 179± 88.

Krass, P. (1991) Building a better mousetrap: what role do MIS executives play in business reengineering projects? Information Week, 313, 24.

Lederer, A.L. and Sethi, V. (1988). The implementation of strategic information systems planning methodologies. MIS Quarterly, 12, 445± 61.

Lederer, A.L. and Sethi, V. (1991) Critical dimensions of strategic information systems planning. Decision Science, 22, 104± 19.

Martin, J.M. (1982) Strategic Data-Planning Methodologies (Prentice-Hall, Englewood Cliffs, NJ).

Martin, J.M. (1990) Information engineering volumes 1, 2 and 3 (Prentice-Hall, Englewood Cliffs, NJ).

Mayer, R.J., Grif® tch, P.A. and Menzel, C.P. (1992a) IDEF6: A Design Rationale Capture Method Concept Paper. Report No. AL-TP-1992-0050 (November). Air Force Systems Command, USA.

Mayer, R.J., Keen, A. and Wells, M.S. (1992b) Information Integration for Concurrent Engineering (IICE) IDEF 4 Object-Oriented Design Method Report. Report No. AL-TR-19920056 (May). Air Force Systems Command, USA.

McCormick, J.J. (1991) CIO’ s reassess priorities. Information Week, 351, 13.

McFadden, F.R. and Hoffer, J.A. (1991) Database Management third edition (Benjamin/Cummings Publishing, Redwood City, CA).

Moad, J. (1989) Navigating cross-functional IS waters. Datamation, 35, 73± 5.

Niederman, F., Brancheau, J.C. and Wetherbe, J.C. (1991) Information systems management issues for the 1990s. MIS Quarterly, 15, 475± 500.

Nolan, R.L. (1973) Computer data bases: the future is now. Harvard Business Review, 51, 98± 114.

Norton, R.L., Pollock, A.J. and Ware, J.P. (1989) Toward the design of network organizations. Stage by Stage, 9, 1± 12.

Petrie, C.J. (ed) (1992) Enterprise Integration Modeling. Proceeding of the First International Conference (The MIT Press, Cambridge, MA).

Porter, M.E. and Milar, V.E. (1985) How information gives you competitive advantage. Harvard Business Review, 63, 149± 60.

Rockart, J.F. (1979) Chief executives de® ne their own data needs. Harvard Business Review, 57, 81± 91.

Rockart, J. and Short, J. (1989) IT in the 1990s: managing organizational interdependence. Sloan Management Review, 30, 7± 17.

Ryan, A.J. (1991) Cigna re-engineers itself. Computerworld, 25, 79.

Senn, J.A. (1984) Analysis and Design of Information Systems (McGraw-Hill Book Company, New York).

Senn, J.A. (1991) Reshaping business processes through reengineering, SIM Network, 4± 6, 12.

Sowa, J.F. and Zachman, J.A. (1992a) Extending and formalizing the framework for information systems architecture. IBM Systems Journal, 31, 590± 616.

Sowa, J.F. and Zachman, J.A. (1992b) A logic-based approach to enterprise integration, in Enterprise Integration Modeling: Proceedings of the First International Conference (The MIT Press, Cambridge, MA, USA) August 5± 9, pp. 152± 66.

Stewart, T.A. (1992) The search for the organization of tomorrow. Fortune, 125, 92± 98.

Synnott, W.R. (1987) The Information Weapon: Winning Customers and Markets with Technology (John Wiley and Sons, New York).

Targowski, A.S. (1988) Systems planning for the enterprisewide information management complex: the architectural approach. Journal of Management Information Systems, 5, 23± 37.

Tendiman, R. (1992) \`R’ e-engineering: how to make it work, in 2nd Annual Symposium: Recharting Your Information Technology Strategy, October 19± 23, Boston, pp. 21± 32 (Gartner Group, USA)

Venkatraman, N. (1991) IT-induced business recon® guration, in The Corporation of the 1990’s, Information Technology and Organizational Transformation (Oxford University Press, New York) pp. 122± 58.

Vernadat, F.B. (1992) CISOMA ± a European development for enterprise integration, part 2: enterprise modeling, in Enterprise Integration Modeling: Proceedings of the First International Conference, Petrie, C.J., (ed) (The MIT Press, Cambridge, MA) pp. 189± 204. August 5± 9.

Vogel, D.R. and Wetherbe, J.C. (1991) Information architecture: sharing the sharable resource. CAUSE/ EFFECT. 14. 4–9

Vowler, J. (1991) Re-engineering for lateral thinkers. Computer Weekly, 10, June 13, 18.

Wardle, C. (1984) The evolution of information systems architecture, in Proceedings of the 5th International Conference on Information Systems (Association for Computing Machinery) pp. 205± 17.

Wetherbe, J.C. and Davis, G.B. (1983) Developing a longrange information architecture, in Proceedings of the National Computer Conference, October 10± 13, Los Angeles (AFIPS Press, Anaheim, CA) pp. 262± 9.

Wilkinson, R. (1991) Reengineering: industrial engineering in action. Industrial Engineering 23, 47± 50.

Wiseman, C. (1988) Strategic Information Systems, (Richard D. Irwin, Homewood, IL).

Zachman, J.A. (1987) A framework for information systems architecture. IBM Systems Journal, 26, 272± 92.

## Biographical notes

William J. Kettinger is director of the Center of Information Management and Technology Research at the University of South Carolina, USA. Bill has also served as the College of Business Administration’s assistant dean. His current research focuses on business process management, IS quality and strategic IT. He has published in such academic journals as MIS Quarterly, Decision Sciences, Journal of Management Information Systems, Public Administrative Review, Data Base and Information & Management and in such practitioner journals as Journal of Information Systems Management and Journal of Systems Management. His most recent book, Business Process Change: Concepts, Methods and Techniques, was published by Idea Group Publishing. He received his PhD and MS in information systems from the University of South Carolina and an MPA from the University of Massachusetts at Amherst.

James T.C. Teng is associate professor of MIS in the Management Science Department of the College of Business Administration at the University of South Carolina, USA. Dr Teng has also held teaching and research positions at several universities, including most recently the University of Pittsburgh. He has written over 30 articles on numerous IS subjects and recently has focused his research attention on the business process redesign where he has published on this topic in such journals as California Management Review, Omega, Long-Planning, IEEE Transactions in Engineering Management and Data Base. He has a PhD in management information systems from the University of Minnesota. In 1992, he received the Outstanding Achievement Award from the Decision Science Institute.

Subashish Guha is a senior product manager at the Integrated Client Server Systems division of AT&T Corporation. He is also a PhD candidate in MIS from the College of Business Administration at the University of South Carolina, USA. His current research interests are in the areas of business process innovation, TQM and QFD, product planning and strategic marketing. He has authored articles in such journals as MIS Quarterly and Journal of Information Systems Management and several international proceedings.

Address for correspondence: William J. Kettinger, Department of Management Science, College of Business Administration, University of South Carolina, Columbia, SC 29208, USA.
