---
otero_id: 18719
otero_key: "MP828HGP"
title: "Using a DSS to incorporate expert opinion in strategic product development funding decisions"
authors: "Michael C. Kettelhut"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90035-z"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Applications

# Using a DSS to incorporate expert opinion in strategic product development funding decisions

Michael C. Kettelhut

The University of Dallas, Irving, TX 75062-4799, USA

Research investigating Decision Support Systems (DSS) suggests they provide support to decision makers confronted with unstructured problems. Strategic decisions are often characterized as unstructured: they address external markets, new products, and changing competitors. This paper examines the development and adaptive implementation of a multicriterion DSS, which captured the expertise of recognized experts in different functional groups of an organization, for use in allocating product development funds to new programs. The DSS increased the number of factors considered by decision makers and provided a method for ranking competitors using a discrete set of criteria. The study demonstrates the use of DSS as a vehicle for incorporating of expert opinion in group decision processes, and illustrates specific DSS benefits that include information aggregation and problem structuring.

Keywords: Decision support system, Multi-criterion decision making, DSS in group decision processes, Expert opinion in DSS, Evolutive DSS design

![](/api/attachments/MP828HGP/fulltext/images/1bc61aa79e1c336d0ae7ad6fc4ad4738135b2399f06beae5f271e188ba427d79.jpg)

Michael C. Kettelhut is Assistant Professor of Management Information Systems at The University of Dallas. He received a Ph.D. in Management Science and Information Systems from the University of Texas at Arlington in 1986. He joined the faculty of The University of Dallas in 1987 after holding both division level and corporate positions as Director of Strategic Planning in two different corporations. His current research interests include individual and group decision making, and health care applications of Information technology. He is actively involved in the design of both imaging technologies and research data bases with Humana Advanced Surgical Institutes in Dallas and the Humana Hospital Centers of Excellence Programs across the United States.

## Introduction

The use of information and information technologies as means of furthering a corporation's strategic goals has received considerable attention in recent years [12,28]. King, Grover and Hufnagel [16] suggest that information must be differentiated from information technology to enable a firm to “...focus attention on opportunities involving both kinds of resources during planning and decision making processes…” (page 88). The value of information may be enhanced if it is appropriately aggregated, structured, or provided to decision makers when required to support decision making.

Facilitating technologies include expert systems and DSS. Expert Systems are often developed to provide for the retention and distribution of expertise within an organization [40]. Expertise is often held by lower level organizational members, who, do to the nature of their position or education, possess specialized knowledge [22]. This knowledge may be of specific competitors, particular technologies, or particular processes. Expert systems capture this knowledge and make it available to other organizational members.

DSS aggregate information from models and data bases. They facilitate individual communication and learning $[1,24]$ , and improve communications in group decision making $[8,9,11]$ . Lauer and Jenkins $[18]$ suggest that DSS may be evaluated based upon their “cognitive benefits.” This view suggests that development and use of DSS may improve understanding of decision processes, calibration of decision makers, and may reduce both the bias and variance associated with prediction of outcomes. Further, these benefits may arise from use of the DSS for assumption testing or sensitivity analysis, independent of its accuracy.

This paper discusses the implementation of a DSS which was used to control the allocation of new business development funds. It was implemented to incorporate expert opinion and judgement in the decision making process. In particular, it aggregated the expert views of lower level organizational members who were normally excluded from funding decisions, but who had detailed knowledge of key technologies, processes, and competitors.

The author directed development of, and participated in the implementation of the DSS described in this paper. At the time, he held the position of Director of Business Planning and Analysis in the division which is discussed. In this position, he was responsible for developing the Division's strategic and operating plans and for articulating those plans to corporate offices. Information reported in the following case discussion was collected from both informal notes and formal minutes of meetings in which the author was both an observer and direct participant. Discussion begins with a brief description of the organization and the decision making environment.

## The organization and the decision making environment

The organization was a defense manufacturing division of a Fortune 500 Corporation. The division had two major vehicle product lines. Their primary vehicle was scheduled to be in production for 10–15 years and their secondary vehicle was nearing the end of its production cycle. The division had been recently acquired by a new parent corporation, and following the acquisition, was charged with the responsibility of continuing research and development, and of winning new contracts to replace the revenues that would be lost when their secondary vehicle product line was phased out of production.

Two aspects of the environment are noteworthy. First, the division had one primary customer with a well defined acquisition cycle. Second, there were relatively scarce resources which could be applied to winning a new contract. The acquisition cycle of the customer is portrayed on the left side of Figure 1. As indicated, the procuring agency translated a customer requirement into a “Request for Proposal” (RFP). The

![](/api/attachments/MP828HGP/fulltext/images/2d20ae6b426ef5823046f13caf40e75e8b8e6c4fefbfb8ccf8aca64d53dc879a.jpg)  
Fig. 1. The proposal process.

RFP was forwarded to the division and to other potential suppliers who either prepared a detailed technical proposal or elected not to bid on the particular RFP. After the procuring agency received responses, they were reviewed with the ultimate user (the using command) and contracts were awarded as appropriate. In all cases, the procuring command held a bidders conference in which results of the proposal evaluation were discussed. As a result, organizations who had submitted losing proposals received information about the customer evaluation of their individual proposals.

Within the division, the review process for proposals is outlined in the box “Division Process” in Figure 1. Copies of proposals were forwarded to two engineering directors following receipt. Based upon their assessment of the proposal, the Vice President (VP) of engineering usually made a decision to either prepare a proposal or advise the customer that the division would not respond to the RFP. If the VP Engineering elected to bid on a proposal, resources were allocated and a proposal was prepared.

![](/api/attachments/MP828HGP/fulltext/images/d02dd7591204ed5bb7f19ea0f8e96e9bdfeef628168d4571547199f9bd5131b5.jpg)  
Fig. 2. Funding growth.

The process of preparing a detailed technical proposal was time consuming and resource intensive. Resource allocation was a major issue within the division. At the time the division was acquired, a minimum level of funding was available for development of new technologies and proposals. Figure 2 illustrates planned increases in funds for both bid and proposal (B&P) and Independent Research and Development (IR&D).

Unlike commercial firms, the costs of B&P and IR&D are negotiated as part of the cost of doing business for defense contractors. A technical report describing IR&D results is prepared each year and submitted to the government for review and scoring. The scoring of the IR&D reports is one of the factors used to determine funding in subsequent years. If the divisions' work is not satisfactory, the negotiated levels for B&P and IR&D may be reduced. Further, if the division spent more than the negotiated amount for B&P and IR&D, the excess expenditures were directly charged against profits.

In this environment, the decision to bid on a program could directly impact profitability of the division if negotiated B&P ceilings were exceeded. The decision could also impact the division's ability to negotiate future funding if resources allocated to technical research (IR&D) were redirected to proposals. When this occurred, IR&D projects were not completed satisfactorily, and the divisions technical scores for IR&D were reduced, leading to reduced funding in subsequent years.

As suggested by Figure 1, the process of determining which RFPs to respond to had been dominated by the engineering organization. The VP Engineering routinely held meetings to review RFPs. These meetings were used to formally approve the development of a proposal responding to an RFP (the bid/no-bid decision), and led to allocation of marketing and engineering resources. When proposals were completed, they were again reviewed by the VP Engineering who recommended their approval to both division and corporate management.

The VP Engineering was viewed as the technical expert by the division's previous owner, and had retained the political power to make decisions leading to proposal development. However, in the first two years following the acquisition, the division had not been awarded a single new government development contract despite the additional B&P and IR&D funding which was made available by the new parent corporation. Staff members transferred to the division attributed government rejections of proposals to lack of focus, inadequate funding for specific proposals, the customer's emphasis on different technologies, and soft program requirements. Other organizational members reported feeling that meetings the VP Engineering held, after initial reviews of RFPs by his two senior Directors, were called to confirm the VPs decision to prepare a proposal, not to prepare for or make these decisions which led to resource allocation and funds expenditures.

As a result, the Director of Business Planning was directed to develop and implement procedures governing the allocation of funds to new business development (B&P and IR&D). These procedures were to assure that funds were not allocated to programs where there was a low probability of winning a government development contract. The effort to implement appropriate policies and procedures led to the development of the DSS described in the following section.

## Development and implementation

The Director of Business Planning and Analysis initially attempted to implement control procedures similar to those in use in other divisions of

the corporation. These required formal circulation of RFPs to more individuals within the division, and they required representation in meetings from a larger number of functional groups. However, the VP Engineering held greater power in the division and was able to prevent implementation of these procedures. He argued that while greater participation was possible, it would preclude rapid response to RFPs, particularly since the key technical expertise was held by individuals in the engineering function.

As an alternative, a multi-criterion model was developed by the Business Planning and Analysis Organization. This provided a method for weighting financial, technical, production, and political factors viewed as critical to preparation of a successful proposal. The factors in the model were carefully selected to include categories emphasized in the customer's RFPs that required data from outside the engineering function (e.g., labor rates, labor availability, production capacity).

Table 1 Competitive analysis

<table><tr><td rowspan="2"></td><td colspan="5">Competitors</td><td rowspan="2">Average competitor</td><td rowspan="2">Div</td><td rowspan="2">Delta</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td colspan="9">Technical Factors</td></tr><tr><td>Composites</td><td>7</td><td>5</td><td>7</td><td>4</td><td>5</td><td>5.6</td><td>6</td><td>0.4</td></tr><tr><td>Vetronics</td><td>8</td><td>8</td><td>6</td><td>4</td><td>7</td><td>6.6</td><td>4</td><td>-2.6</td></tr><tr><td>Armor</td><td>6</td><td>7</td><td>5</td><td>8</td><td>9</td><td>7.0</td><td>7</td><td>0.0</td></tr><tr><td>Sensors</td><td>4</td><td>4</td><td>9</td><td>7</td><td>8</td><td>6.4</td><td>7</td><td>0.6</td></tr><tr><td>AI/Robotics</td><td>6</td><td>5</td><td>7</td><td>6</td><td>9</td><td>6.6</td><td>4</td><td>-2.6</td></tr><tr><td>Drive Systems</td><td>5</td><td>7</td><td>7</td><td>7</td><td>9</td><td>7.0</td><td>5</td><td>-2.0</td></tr><tr><td>Integration</td><td>8</td><td>8</td><td>8</td><td>6</td><td>8</td><td>7.6</td><td>7</td><td>-0.6</td></tr><tr><td>Suspension</td><td>9</td><td>7</td><td>7</td><td>5</td><td>5</td><td>6.6</td><td>3</td><td>-3.6</td></tr><tr><td>Sub-Total</td><td>53</td><td>51</td><td>56</td><td>47</td><td>60</td><td>53.4</td><td>43</td><td>-10.4</td></tr><tr><td colspan="9">Production Factors</td></tr><tr><td>Current Capacity</td><td>8</td><td>4</td><td>2</td><td>5</td><td>3</td><td>4.4</td><td>2</td><td>-2.4</td></tr><tr><td>Welding Technology</td><td>5</td><td>6</td><td>7</td><td>5</td><td>8</td><td>6.2</td><td>6</td><td>-0.2</td></tr><tr><td>Fabrication</td><td>4</td><td>10</td><td>7</td><td>9</td><td>6</td><td>7.2</td><td>4</td><td>-3.2</td></tr><tr><td>Composites</td><td>7</td><td>5</td><td>9</td><td>9</td><td>7</td><td>7.4</td><td>2</td><td>-5.4</td></tr><tr><td>Quality</td><td>7</td><td>6</td><td>8</td><td>5</td><td>9</td><td>7.0</td><td>5</td><td>-2.0</td></tr><tr><td>Labor Availability</td><td>9</td><td>7</td><td>6</td><td>4</td><td>9</td><td>7.0</td><td>6</td><td>-1.0</td></tr><tr><td>Cutting Technologies</td><td>4</td><td>8</td><td>8</td><td>10</td><td>5</td><td>7.0</td><td>6</td><td>-1.0</td></tr><tr><td>Sub-Total</td><td>44</td><td>46</td><td>47</td><td>47</td><td>47</td><td>46.2</td><td>31</td><td>-15.2</td></tr><tr><td colspan="9">Economic Factors</td></tr><tr><td>Current Programs</td><td>5</td><td>3</td><td>5</td><td>4</td><td>6</td><td>4.6</td><td>7</td><td>2.4</td></tr><tr><td>R&amp;D Funding Trends</td><td>4</td><td>6</td><td>9</td><td>2</td><td>8</td><td>5.8</td><td>3</td><td>-2.8</td></tr><tr><td>Cash Generation</td><td>4</td><td>5</td><td>4</td><td>9</td><td>4</td><td>5.2</td><td>4</td><td>-1.2</td></tr><tr><td>Current Assets</td><td>6</td><td>6</td><td>8</td><td>5</td><td>9</td><td>6.8</td><td>3</td><td>-3.8</td></tr><tr><td>Labor Rates</td><td>6</td><td>4</td><td>8</td><td>7</td><td>8</td><td>6.6</td><td>2</td><td>-4.6</td></tr><tr><td>Parent Strength</td><td>5</td><td>4</td><td>6</td><td>9</td><td>7</td><td>6.2</td><td>7</td><td>0.8</td></tr><tr><td>Sub-Total</td><td>30</td><td>28</td><td>40</td><td>36</td><td>42</td><td>35.2</td><td>26</td><td>-9.2</td></tr><tr><td colspan="9">Political Factors</td></tr><tr><td>Congressional Support</td><td>6</td><td>4</td><td>7</td><td>5</td><td>8</td><td>6.0</td><td>4</td><td>-2.0</td></tr><tr><td>Budget Share</td><td>3</td><td>5</td><td>6</td><td>7</td><td>9</td><td>6.0</td><td>5</td><td>-1.0</td></tr><tr><td>Cost Performance</td><td>5</td><td>4</td><td>7</td><td>9</td><td>6</td><td>6.2</td><td>3</td><td>-3.2</td></tr><tr><td>Schedule Performance</td><td>6</td><td>8</td><td>9</td><td>9</td><td>5</td><td>7.4</td><td>5</td><td>-2.4</td></tr><tr><td>Customer Relations</td><td>6</td><td>5</td><td>8</td><td>7</td><td>8</td><td>6.8</td><td>5</td><td>-1.8</td></tr><tr><td>Related Programs</td><td>8</td><td>8</td><td>5</td><td>2</td><td>9</td><td>6.4</td><td>4</td><td>-2.4</td></tr><tr><td>Sub-Total</td><td>34</td><td>34</td><td>42</td><td>39</td><td>45</td><td>38.8</td><td>26</td><td>-12.8</td></tr><tr><td>Total Score</td><td>161</td><td>159</td><td>185</td><td>169</td><td>194</td><td>173.6</td><td>126</td><td>-47.6</td></tr><tr><td colspan="9">Weighted Scores:</td></tr><tr><td>Technical (25%)</td><td>13.3</td><td>12.8</td><td>14.0</td><td>11.8</td><td>15.0</td><td>13.4</td><td>10.8</td><td>-2.6</td></tr><tr><td>Production (40%)</td><td>17.6</td><td>18.4</td><td>18.8</td><td>18.8</td><td>18.8</td><td>18.5</td><td>12.4</td><td>-6.1</td></tr><tr><td>Economic (20%)</td><td>6.0</td><td>5.6</td><td>8.0</td><td>7.2</td><td>8.4</td><td>7.0</td><td>5.2</td><td>-1.8</td></tr><tr><td>Political (15%)</td><td>24.2</td><td>23.9</td><td>27.8</td><td>25.4</td><td>29.1</td><td>26.0</td><td>18.9</td><td>-7.1</td></tr><tr><td>Weighted Totals:</td><td>61.0</td><td>60.6</td><td>68.6</td><td>63.1</td><td>71.3</td><td>64.9</td><td>47.3</td><td>-17.7</td></tr></table>

Implementing the model for a particular program and set of competitors required entering scores for each factor, by competitor, in a spreadsheet. Sample results are portrayed in Table 1. Summing entries by competitor yielded an unweighted ranking of competitors by program. Weights could be assigned to each set of factors to reflect their relative importance as defined by the customer in the RFP (shown at the bottom of Table 1).

While the DSS technique (as defined) seems straightforward, members of the organization later described the manner in which it was implemented as “surreptitious” or “devious.” It was introduced during a meeting called to review a customer RFP. The customer had requested competitive proposals for a product requiring different capabilities than those immediately available within the division. An engineering manager had completed a presentation addressing the solicitation and made a recommendation for allocation of funds to develop a major proposal. The Engineering V.P. confirmed the managers recommendation and asked how the group should proceed.

During the ensuing discussion, the Director of Business Planning and Analysis presented the results of a competitive analysis which had been prepared using the funding DSS (Table 1). The analysis, which had been completed using information provided by some of the participants in the meeting, suggested that the division was poorly placed compared to its competitors.

The VP Engineering reacted negatively to several specific values, but not to the general approach. In response to disagreement over these specific values, the Director of Business Planning and Analysis suggested that the spreadsheet be recalculated using values provided by experts in the engineering, production and financial organizations. He further suggested, that results could be provided to the experts for a second round of revision (in Delphi fashion [26]). The VP Engineering, who had used such Delphi procedures, and who was confident the views of his staff would positively affect the results of the analysis, agreed to the use of the model at the next meeting.

At the next meeting, the revised competitive analysis suggested that the division was not as competitive as originally indicated. Discussion initially focused on specific numbers, but soon turned to a comparison of the division's competitors on a category by category basis: it focused on specific factors that provided a poor competitive rating for the division. The decision to prepare a proposal and to enter the competition was reversed. Further, the VP Engineering and VP Marketing agreed to use the DSS prior to allocating funds or manpower to any new proposal.

## Evolution

During the months following the initial use of the DSS, several other RFPs were reviewed. Funds were not allocated to the development of proposals responding to any of these RFPs. As division management continued to use the model and gained a better view of their competitive position, a technology manager approached the planning organization and suggested another use of the evaluation model. He believed that the division was focused on technologies that were not critical to changing customer needs. The customer had no specification for an ideal system, and as technologies were traded off against cost, there were numerous false starts.

In response to the manager's request, the planning organization developed a chronology of customer initiated programs. The chronology suggested that the customer did not have a clear view of performance requirements. The customer had awarded development contracts for a number of programs since the division was acquired. Of these, one had been combined with another vendor's current production contract, and six had been cancelled. Following this exercise, the planners met with the technology manager to develop a second model that assessed the importance of various technologies to potential customer programs. Sample results from this model are shown in Table 2.

Scores for each technology, by program, were collected from division program managers, and the division technology and program managers were asked to identify technical experts in the customer organization. These experts were interviewed and asked to estimate the importance of technologies to various programs. This expertise was sought to minimize bias expected when division technology managers were asked about the importance of their own area of research. Scoring also required that individuals recognize minimum values for certain characteristics of the technology. For example, if the technology was viewed as critical, and could provide a decisive competitive advantage, a score of eight (8) or higher would be assigned. For baseline technologies, those that competitors were expected to define in their proposals, scores were to be four (4) or less.

Table 2  
Technology scores for programs

<table><tr><td rowspan="2"></td><td colspan="3">Programs</td><td rowspan="2">Total</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Vetronics</td><td>9</td><td>7</td><td>9</td><td>25</td></tr><tr><td>Sensors</td><td>9</td><td>7</td><td>8</td><td>24</td></tr><tr><td>Composites</td><td>9</td><td>5</td><td>8</td><td>22</td></tr><tr><td>Armor</td><td>7</td><td>8</td><td>6</td><td>21</td></tr><tr><td>Integration</td><td>6</td><td>6</td><td>7</td><td>19</td></tr><tr><td>Drive Systems</td><td>7</td><td>4</td><td>4</td><td>15</td></tr><tr><td>AI/Robotics</td><td>4</td><td>4</td><td>5</td><td>13</td></tr><tr><td>Suspension</td><td>4</td><td>4</td><td>4</td><td>12</td></tr></table>

Scores were aggregated and the relative importance of each technology was compared to the relative funding level of each technology (Figure 3). Results suggested that certain technologies were adequately funded. However, they also suggested that AI/Robotics was over funded, and that sensors, vetronics (vehicle electronics), and composites were under funded. When these results were presented to division management, they began to reallocate R&D technical resources.

![](/api/attachments/MP828HGP/fulltext/images/8ecaee1ec9a5c19a73606bd522c751a69ae42819f9b50248ce702f83963f6c22.jpg)  
Fig. 3. Comparative technical funding levels.

Use of the competitive analysis and technical funding models was institutionalized when the general manager used the two models to defend division decisions on both program proposals and R&D technology funding in quarterly performance reviews with corporate staff. In fact, corporate staff requested that other divisions review the models and consider their use.

## Discussion

Research credits successful implementation of Decision Support Systems (DSS) to user involvement during development, top management support, availability of technical resources and clearly defined objectives $[20,31,35,39]$ . Successful DSS implementation is also attributed to an understanding of the decision process and the needs of the decision makers/users $[16,17,36]$ . Stabell suggests that decision behavior defines the type of system to be considered $[37]$ . In the case reported, planners observed decision making processes in meetings and reviewed minutes of previous meetings. Decision makers considered certain technical variables, but they could not accurately describe how variables were aggregated, or even if all appropriate variables were considered. Cognitive biases and experience from past efforts provided a framework for decision making that had not changed for several years.

Examination of the decision making process identified several problems which the DSS addresses. First, it contributed directly to the intelligence phase of the decision making process. Second, it added structure in R&D funding decisions that have been described as unstructured [15,40]. Third, it provided the basis for group discussion of factors perceived as important to the decision at hand, increasing communications and understanding critical to the choice process.

The DSS allowed additional information to be used in the process. King, Grover, and Hufnagel point out that less clearly defined information may be pushed into the background [16]. If used, the information may have great potential for producing benefits. In our case, decision makers in engineering could not clearly define the relevance of non-technical information from other parts of the organization. Before the DSS was implemented, they had relied upon a limited number of information sources. Zmud [46] proposes that a decision maker's acquisition and use of information is often based upon a simple, self-enhancing schema which reflects historical rather than current environments. O'Reilley [24,25] suggests ease of access to information may be more important than quality of information in the decision maker's data collection process. The use of DSS to capture and integrate information, particularly the subjective views of experts is cited as a learning device by Lauer and Jenkins. The DSS implemented here formally incorporated production, financial and political factors that were not previously addressed. As a result, information sampled from a broader base was used in decision making, further reducing decision maker bias [29].

Environmental change may be a precursor to changes in both search strategy and information collection. While continued use of current search strategies and problem solving approaches is predictable $[2,21,32]$ , the division failed to win R&D contracts which decision makers thought they should have won. Although the competitive environment had changed, Culnan $[4]$ suggests that decision makers do not seek new sources of information until environmental changes are easily perceived. In our case, technical approaches that had been successful in the past no longer worked; the decision rules had changed and past approaches led to high levels of error $[29]$ . Such factors favor the use of a model which both adds and helps to integrate information $[6]$ .

The DSS also added structure to the decision process. Quantitative models aggregate numeric data for review, facilitating objective analysis and reducing cognitive bias. In particular, spreadsheet models present problems in a decision matrix format, simplifying the task of combining information cues from various sources $[2,38]$ . Spreadsheet models allow easy formulation of problems with multiple criteria or factors, and in microcomputer applications such as Lotus 1-2-3, they facilitate the rapid turnaround that allows additional iterations $[3]$ . Weighting the decision variables reduces complexity of analysis, allowing decision makers to focus on key factors. Identification of key variables (most heavily weighted) facilitates a “divide and conquer” approach and reduces cognitive overload [33].

Finally, the DSS provided a basis for discussion of both division and competitor strengths and weaknesses with respect to specific programs or proposals. Values in the model were challenged rather than the model itself, and comments of the VP Engineering were typical of those associated with anchoring and subsequent adjustment of numeric estimates $[42]$ . The ranking factors applied in the spreadsheet were not strictly additive and linear (they were derived from ordinal numbers). However, Dawes argues that “improper linear models” outperform human decision makers in predicting a criterion variable (in this case the competitive score) in a variety of settings. In this implementation, the goal was to increase understanding the of the division’s competitive position compared to its competitors, and not to estimate of the division’s position independent of its competitors.

The use of models to stimulate discussion of decisions facilitated group evaluation and increased consensus in decisions. These outcomes have been attributed to Group Decision Support Systems (GDSS) [13]. However, our DSS does not fit the description of GDSS in current usage [14,34,45]. Had the models been manipulated in meetings, using a computer, data display device, and an overhead projector, then the DSS would resemble some current GDSS [7]. Even without manipulation, presentation of the spreadsheet results have provided benefits that accrue to GDSS.

## Conclusions

Success in implementation has been attributed to detailed study of the decision making process. In an R&D environment, where technologies are complex or less certain and where high performance is necessary, decision makers may require more, rather than less information [10,41]. The DSS reported here aggregated expert opinion and helped determine the division's competitive position, thereby contributing directly to problem resolution.

The DSS was designed and implemented in what Mahmood and Medwitz describe as an “evolutive” fashion [23]. Short cycles were used, and the model was rapidly modified to add factors and modify the sources of data input for the values in the spreadsheet. For example, decision makers exercised some control over the model by identifying the experts to be used as a source of data for computing competitive rankings used in subsequent meetings. The use of experts designated by group leaders helped commit them to the process, assuring that their organizations improved the model $[27,30]$ . The Delphi approach $[5,43]$ is often used in technological forecasting and has been used to generate discussion in unstructured decision making situations $[26]$ . Our suggestion to use Delphi techniques reduced apprehension, as the original model was viewed as conceptual and subject to revision.

Liang [19] suggests that the use of DSS in a group meeting facilitates discussion of assumptions, conflict resolution, and data manipulation while increasing consistency in the use of information and control over the decision process. In our case, the models developed for group review provided a new “norm for how decisions should be made” which was adopted by the group and reinforced by the actions of the General Manager and Corporate Staff.

The models presented in this study suggest that Liang's views of the value of using straightforward individual DSS in group settings deserve further examination. More sophisticated examples of DSS have been reported, and various authors suggest that "Group" DSS must have sophisticated information sharing, alternative generating, voting, or other facilities. Vogel and Nunamaker support the use of models in GDSS, and suggest that multicriterion decision-making models such as the DSS implemented in this study are particularly relevant to extended versions of GDSS [44].

The DSS development and implementation described in this paper suggests that if the decision making process and environment are understood, appropriate support at an appropriate level of technology may be more easily identified. The situation described is representative of many problems which occur in development of organizational strategy-there are multiple opportunities which require different technical, production, or marketing competencies. Often decision makers cannot distinguish the capabilities of organizational groups which are not under their direct control. In such cases, multi-criterion models may facilitate aggregation of important information. There are two precursors. First, the decision makers must recognize the existence and value of information held by other organizational members. Second, individuals in the organization must be willing to have expert opinion aggregated in models which reduce the communications filtering that normally occurs as information is moved from person to person within an organization. The enabling technologies – computers and software are not at issue.

## References

[1] Alter, S.L., Decision Support Systems, Current Practice and Continuing Challenges, Addison-Wesley, Reading PA., 1980.

[2] Burris, R.W., “Human Learning”, in Handbook of Industrial and Organizational Psychology, in M. Dunnette, (Editor), Rand McNally, 1976.

[3] Chandrasekaran, G., and R Ramesh, “Microcomputer Based Multiple Criteria Decision Support System for Strategic Planning.” Information & Management, Vol. 12, 1987 pp 163–172.

[4] Culnan, M., “Environmental Scanning: The Effects of Task Complexity and Source Accessibility on Information Gathering Behavior”, Decision Science, Vol. 14, No. 2, April 1983.

[5] Dalkey, N.C., Studies in the Quality of Life: Delphi and Decision Making, Lexington, MA: Lexington Books, 1972.

[6] Dawes, R.M., “Case-by-Case versus Rule Generated Procedures for the Allocation of Scarce Resources”, in Kaplan & Schwartz (Eds.) Human Judgment and Decision Processes in Applied Settings, N.Y., Academic Press, 1977.

[7] Dennis, A.R., J.F. George, L.M. Jessup, J.F. Nunamaker Jr., and D.R. Vogel, “Information Technology to Support Electronic Meetings”, MIS Quarterly, Vol. 4, 1988, pp. 591–624.

[8] Desanctis, G., and B. Gallupe, “Group Decision Support systems: A New Frontier”, Data Base, Winter 1985, pp. 3–10.

[9] Desanctis, G., and B. Gallupe, “A Foundation for the Study of Group Decision Support Systems”, Management Science, Vol. 33, No. 5, May 1987, pp. 589–609.

[10] Galbraith, J.R., “Organizational Design: An Information Processing View”, Interfaces, Vol. 4, No. 3, May 1974.

[11] Huber, G.P., Issues in the Design of Group Decision Support Systems", MIS Quarterly, September, 1984, pp. 195–204.

[12] Ives, B. and G.P Learmouth. “The Information System as a Competitive Weapon.” Communications of the ACM, Vol. 27, No. 12, 1984, pp. 1193–1201.

[13] Jarvenpaa, S.L., V.S. Rao and G.P. Huber, “Computer Support for Groups Working on Unstructured Problems: A Field Experiment”, MIS Quarterly, Vol. 4, 1988, pp. 645–666.

[14] Jelassi, M.T., and R.A. Beauclair, “An Integrated Framework for Group Decision Support Systems Design”, Information & Management, Vol. 13, 1987 pp. 143–153.

[15] Keen, P.G.W., and M.S. Scott-Morton, Decision Support Systems, An Organizational Perspective, Addison-Wesley, 1978.

[16] King, W.R., V. Grover and E.H. Hufnagel, "Using Information and Information Technology for Sustainable Competitive Advantage: Some Empirical Evidence." Information & Management, Vol. 17, 1989, pp. 87–93.

[17] Kozar, K.A. and J.M. Mahlum, “A User Generated Information System: An Innovative Development Approach”, MIS Quarterly, Vol. 2, 1987, pp. 163–173.

[18] Lauer, T.W. and A.M. Jenkins, “Implications of Behavioral Decision Theory for Decision Support Systems Implementation and Research”, Discussion Paper #273, School of Business, Indiana University, Sept. 1984.

[19] Liang, T.P., “Model Management for Group Decision Support”, MIS Quarterly, Vol. 4, 1988, pp. 667–680.

[20] Lucas H.C. Jr., The Design, Analysis and Implementation of Information Systems, McGraw Hill, N.Y., 1985.

[21] March, J.G. and Z. Shapra, “Behavioral Decision Theory and Organizational Decision Theory”, in Decision Making, An Interdisciplinary Approach, Braunstein, D. and G.R. Ungson, Eds., Kent Pub., N.Y., 1982.

[22] Mechanic, D., “Sources of Power of lower Participants in Complex Organizations”, Administrative Science Quarterly, Vol. 7., 1962, pp. 349–364.

[23] Mahmood, M.A. and J.N. Medewitz. "Impact of Design Methods on Decision Support Systems Success: An Empirical Assessment." Information & Management, Vol. 9, 1985, pp. 137–151.

[24] O'Reilley, C.A., "Supervisors and Peers and Information Sources, Work Group Supportiveness, and Individual Decision Performance", Journal of Applied Psychology, Vol. 62, 1977, pp. 632–635.

[25] O'Reilley, C.A., "Variations in Decision Makers' Use of Information Sources: The Impact of Quality and Accessibility of Information", Academy of Management Journal, Vol. 28, No. 4., 1982.

[26] Perez, V.L. and R. Schuler, “The Delphi Method as a Tool for Information Requirements Specification”, Information & Management, Vol. 5, 1982, pp. 157–167.

[27] Pfeffer, J. and G.R. Salancik, The External Control of Organizations, Harper & Row, N.Y., 1978.

[28] Porter, M., and V.E. Millar. "How Information Gives You a Competitive Advantage." Harvard Business Review, July-August 1985, pp. 149–160.

[29] Sage. A.P., “Behavioral & Organizational Considerations in the Design of Information Systems and Processes for Decision Support and Planning”, IEEE Transactions on Systems, Man & Cybernetics, Vol SMC-11, No 9, pp. 640–678, Sept 1981.

[30] Salancik, G. and J. Pfeffer, “The Basis and Use of Power

in Organizational Decision Making: The Case of a University", Administrative Science Quarterly, No. 19, 1974, pp. 453–473.

[31] Schultz, R., D. Slevin and J.K. Pinto, “Strategy and Tactics in a Process Model of Project Implementation”, Interfaces, Vol. 17, May-June, 1987, pp. 34–46.

[32] Simon, H.A., Models of Man, Wiley & sons, N.Y. 1957.

[33] Slovic, P., B. Fischoff and S. Lichtenstein, “Behavioral Decision Theory”, Annual Review of Psychology, 1977, Vol. 28, pp. 1–39.

[34] Smith, J.Y., and M.T. Vanecek, “Computer Conferencing and Task-Oriented Decisions: Implications for Group Decision Support”, Information & Management, Vol. 14, 1988, pp. 123–132.

[35] Sprague, R.H., and E.D. Carlson, Building Effective Decision Support Systems, Prentice Hall, N.J., 1982.

[36] Stabell, C.B., “Decision Research: Description and Diagnosis for Decision Making in Organizations”, Working Paper No. 79.006. Bergen: Institute for Information Systems Research, Norwegian School of Economics and Business Administration. 1979.

[37] Stabell, C.B., “A Decision-Oriented Approach to Building DSS”, in Bennett, J.L., Building Decision Support Systems, Addison Wesley, 1983.

[38] Teng, J.T.C. and S. Vijay, Psychological Studies of Decision Making and Its Implementation for DSS", Proceedings, Decision Sciences Institute 1987 Annual Meeting, pp. 309–341, 1987.

[39] Thierauf, R.J., User Oriented Decision Support Systems, Accent on Problem Finding, Prentice Hall, N.J., 1988.

[40] Turban, E., Decision Support and Expert Systems, Managerial Perspectives, MacMillan, N.Y. 1988.

[41] Tushman, M., “Technical Communications in Research and Development Laboratories: The Impact of Project Work Characteristics”, Academy of Management Journal, Vol. 21, 1978, pp. 624–645.

[42] Tversky, A. and D. Kahneman, “Judgment under Uncertainty: Heuristics and Biases”, Science, 1974, vol. 185, Sept. 1974, pp. 1124–1131.

[43] Van de Ven, A.H., and Delbecq, A.L., The Effectiveness of Nominal, Delphi, and Interacting Group Decision Making Processes", Academy of Management Journal, 1974, 17, pp. 605–621.

[44] Vogel, D. and J. Nunamaker, “Group Decision Support System Impact: Multi-Methodological Exploration”, Information & Management, Vol. 18, 1990, pp. 15–28.

[45] Zigurs, I., M.S. Poole, and G.L. DeSanctis, “A Study of Influence in Computer-Mediated Group Decision Making”, MIS Quarterly, Vol 4., 1988, pp. 625–644.

[46] Zmud, R.W., “Opportunities for Manipulating Information Through New Information Technology”, forthcoming in Fulk, J and C. Steinfield (Eds.), Perspectives on New Information Technology, Sage Press (Forthcoming).
