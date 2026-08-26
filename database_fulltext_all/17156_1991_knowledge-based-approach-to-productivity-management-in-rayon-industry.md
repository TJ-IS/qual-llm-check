---
otero_id: 17156
otero_key: "A24QDAA9"
title: "Knowledge based approach to productivity management in rayon industry"
authors: "S. Arunkumar; N. Janakiram"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90038-d"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge based approach to productivity management in rayon industry \*

S. Arunkumar

Department of Computer Science and Engineering and the Interdisciplinary Programmes in Industrial Management and Biomedical Engineering, Indian Institute of Technology, Bombay, India

N. Janakiram

Interdisciplinary Programme in Industrial Engineering & Operations Research, Indian Institute of Technology, Bombay and Century Rayon, Shahad (Maharashtra), India

Intelligent System for Productivity Management (ISPM) facilitates management of productivity by setting appropriate strategic, tactical and operational objectives, measuring and comparing actual performance with targets and suggesting suitable control actions, as well as techniques for improvements, in case of deviations. Rayon industry is a labour intensive, continuous process chemical industry with a number of product varieties and intricate process conditions. ISPM is ideally suited for such an industry in view of the substantial benefits that can be derived by better management of productivity using ISPM. This paper presents a preliminary analysis for application of ISPM, as also details of operation and specimen outputs of the various modules of the system with examples.

Keywords: Knowledge base, Productivity targets, Strategic, Tactical, Operational, Monitor, Evaluator, Controller, Deviations.

## 1. Introduction

A rayon plant produces rayon filament yarn from wood pulp. It is labour intensive. It is a multi-million rupee industry and a typical 30 T/day semi-automated plant employs a few thousand people in India. The impact of gains in productivity on such a scale of operations would be considerable. It is a multi-stage continuous process chemical industry. The material and energy (power and steam) costs being substantial, any gains in productivity will have a favourable impact on competitiveness. Productivity aspects in chemical industry are studied in Deshpande [1989].

![](/api/attachments/A24QDAA9/fulltext/images/77ffc3bef42e4e329cabc0fbbeb4855eddb9051e0a488194d437d40957ca4357.jpg)

![](/api/attachments/A24QDAA9/fulltext/images/779551c4ded4dfe96938719da0ea4bb6de48fd561b66e11bf02709c7b4c95fd7.jpg)

A major quantity of key raw materials, like wood pulp and sulphur, are imported. Import regulations keep changing from time to time, leading to uncertainties in raw material availability.

Process is quite complex. Deep knowledge of operating and process conditions is essential for maintenance of good quality. Corrosion plays havoc on plant and machinery, resulting in high maintenance costs. Few experts are available in this industry.

The final product, rayon yarn, is graded into different qualities before it is marketed. While cost for each product is the same, realisation depends on quality. Rayon market is volatile where prices keep fluctuating (almost on a day to day basis) and competition is keen. Export policy keeps on changing from time to time.

Intelligent System for Productivity Management (ISPM) takes stock of external environment and internal conditions on which productivity depends [Labour Productivity Survey, 1966; Nishikawa, 1969; Bailey, 1978; Sahu, 1986; Ganguly, 1987] before setting appropriate strategic, tactical and operational productivity targets. Actual performance is monitored periodically and significant deviations analysed in detail. Control action is initiated by revising or resetting various targets and by suggesting suitable productivity improvement techniques. When there are drastic changes in environment and/or in planning premises, the targets are reset. ISPM, thus is dynamic and realistic, and facilitates productivity management in a knowledge based environment. This paper presents an application of ISPM to the rayon industry.

## 2. Rayon process

The viscose rayon process [Moncrieff, 1975] consists of STEEPING pulp sheets in Caustic Soda, SHREDDING the soaked sheets into small pieces, CHURNING the small pieces in Carbon Disulphide, DISSOLVING the Xanthate so formed in dilute Caustic Soda, BLENDING the viscose so formed from various dissolvers, RIPENING, FILTERING AND DEAERATING the viscose, SPINNING the viscose through a coagulating bath (spinbath) through a spinnerette and collecting the yarn in the form of cakes and washing the cakes in AFTER TREATMENT department, DRYING and CONING the yarn into cones, which are packed in wooden and corrugated boxes for despatch to markets. Detailed process description is given in the Appendix and flow chart shown in fig. 1.

Rayon yarn is produced in about 10 deniers from 40 D to 600 D. Denier (D) is the weight in grams of 9000 m of yarn; the higher the denier, the coarser the yarn, low deniers being fine yarns. In each denier, there are a minimum of five qualities. The yarn is also produced in different colours and shades. Taking combinations of colour, denier and quality into consideration, nearly three hundred different products are produced.

## 3. Intelligent System of Productivity Management (ISPM)

In this section, we give a brief outline of ISPM proposed by the authors [1989a, 1989b]. ISPM performs two major functions, viz., planning and diagnosis & control and comprises five modules, which are discussed below. The proposed entity relationship diagram of the productivity management process in ISPM framework is shown in fig. 2 and the ISPM architecture in fig. 3.

## 3.1. Planning

The planning function of ISPM is carried out by ESTOPP (Expert Strategic, Tactical and Operational Planner for Productivity) which has two modules, one (ESP) for strategic planning and the other (TOPP) for tactical and operational planning.

## RAYON PROCESS FLOW CHART

![](/api/attachments/A24QDAA9/fulltext/images/f6e234686a41da0cbc51cebf2349917e672991c080b6c631502e0ce416b0e1e3.jpg)

## 3.1.1. Expert Strategic Planner (ESP) [Arunkumar and Janakiram, 1990]

This is the strategic planning module which sets long term corporate objectives using knowledge of various internal and external factors affecting productivity [Rhyne, 1985; Hufnagel, 1987]. ESP resets targets when triggered by Pproductivity E valuator (PE), in the event of drastic changes in the planning premises and/or environment.

## 3.1.2. Tactical and Operational Planner for Productivity (TOPP) [Arunkumar and Janakiram, 1989c]

This module explodes the strategic objective set by ESP to determine tactical as well as operational targets, the latter, in terms of P productivity Indices (PIs). The tactical planning submodule is supported by a K knowledge Base (KB) which has a major portion of the chunk oriented strategic KB at the core, embedded with suitable production rules in appropriate nodes of the chunks. The operational planner submodule uses a rule base for fixing the operational PIs, starting from tactical targets. TOPP also checks on the feasibility of attaining the strategic objectives, using the tactical and operational objectives set. Resetting of these objectives is undertaken by TOPP when triggered by PE, in case of major aberrations in performance.

## 3.2. Monitor, Evaluator and Controller and Productivity (MECOP) [Arunkumar and Janakiram, 1989d]

Diagnosis and Control are achieved through the subsystem MECOP comprising three modules, Productivity Monitor (PM), Productivity E valuator (PE) and Controller of Operational Productivity (COP).

## 3.2.1. Productivity Monitor (PM)

The achieved productivity is measured and monitored against targets laid down. In case of insignificant (negligible) deviations, COP is triggered for revising intermediate targets, retaining the overall (period-en-

# PRODUCTIVITY MANAGEMENT PROCESS Entity-Relationship Diagram

![](/api/attachments/A24QDAA9/fulltext/images/fc5b5516c2f5732bdafcf3a24cb87192e8096dd436f3574be68634fc845f7fee.jpg)  
Fig. 2. Productivity management process-entity relationship diagram.

ding) operational and tactical targets. Control passes to PE, in case of significant aberrations, for detailed investigations. PM also gives an early warning when process is under control, but is showing some adverse trends. KB of PM helps in directing control appropriately and in interpreting trends.

## 3.2.2. Productivity Evaluator (PE)

Whenever the operational performance is outside a control band, PE assesses it with the help of a production rule oriented KB and localises accountability among various departments responsible. If it is a minor aberration, control is passed on to COP. Otherwise, TOPP or ESP is triggered, depending on whether the aberrations are major or drastic, in the latter case accompanied by changes in planning premises/environment.

## 3.2.3. Controller of Operational Productivity (COP)

This module revises intermediate tactical and operational targets, retaining overall (period-ending) tactical as well as strategic objectives. COP triggers TOPP in case overall tactical targets need to be reset.

## ISPM ARCHITECTURE

![](/api/attachments/A24QDAA9/fulltext/images/8023b9da93f95abc6d5bfe61f8cd9acf79707d7f1bd2915842d25cc2095236b3.jpg)  
Fig. 3. ISPM architecture.

COP has a model base to suggest appropriate productivity improvement techniques to facilitate achievement of the revised operational and tactical targets.

## 3.2.4. Modes of operation

MECOP operates in one of four modes – watchdog, diagnostic, review and specific. Under the first mode, PM keeps a watch on certain key process and operational parameters which reflect on achievement of tactical and operational targets. When certain objectives are not met, the second mode takes over and explodes the strategic objective down the productivity tree (fig. 4) into operational productivity targets and compares actual performance with targets. If desired by user, more PIs not meeting the targets can be tracked.

In the review mode, PM compares all PIs from top to bottom of the productivity tree, highlighting major deviations. Analysis, indicating reasons for the deviations, is also presented. In the specific mode, only specific PIs indicated by user are reviewed.

## 4. Application to rayon industry

The functions of various modules of ISPM with respect to its application to rayon industry are described in the following paragraphs.

## PRODUCTIVITY TREE

![](/api/attachments/A24QDAA9/fulltext/images/fde627d0fc6ed46866bf3c2bba459f531c6ff3197e8fbe964245bf1ba4f49882.jpg)  
Fig. 4. Productivity tree.

## 4.1. Setting strategic objectives using ESP

Return On Investment (ROI) along with Sales and growth rate constitute a comprehensive set of strategic objectives [Arunkumar and Janakiram, 1989e]. Sales can be targeted with a certain growth rate over the previous period to achieve the desired market share.

Productivity Data Base (PDB) contains data regarding Earnings Before Interest and Taxes (EBIT), Sales, Output, Capacity, Fixed and Total Investment, Total Market and denier wise Sales and Output for user firm as well as key competitors in the rayon industry for a few years in the past. This data, accessed by Strategic Data Manager (SDM) facilitates computation of indicators like Profit percentage (EBIT/Sales), Marketing Efficiency (Sales/Output), Capacity Utilisation (Output/Capacity), Capacity/Fixed Investment and Fixed Investment/Total Investment, and Market Share percentage. The Strategic Knowledge Base (SKB) contains knowledge in the form of chunks; some examples of chunks are Marketing, Organisation, Technical, Industry (Rayon) [Arunkumar and Janakiram, 1990]. The Strategic Model Base (SMB) has application models for various techniques such as correlation and regression and forecasting models.

The authors [1990] proposed a message passing train type locomotion for navigation of the chunk oriented SKB and a tagged data flow approach for inferencing with reasoning dominated by matching, which culminates in generation of a Figure Of Merit (FOM) for the ROI strategic objective at the super node, to which all chunks are connected. Let us suppose, in a particular consultation, some of the chunks cited in the previous paragraph, say, the Marketing, Organisation and Industry (Rayon) chunks assume the schemas shown in tables 1, 2 and 3, respectively. (It may be noted that certain of the nodes in the schemas are industry specific).

Table 1
Schema of ‘MARKETING’ chunk

<table><tr><td colspan="4">Chunk: MARKETING</td></tr><tr><td colspan="4">Has:</td></tr><tr><td>Macros</td><td>Currency</td><td colspan="2">Connectivity</td></tr><tr><td rowspan="2">Product</td><td rowspan="2">Excellent</td><td>Intra</td><td>Competition, Demand</td></tr><tr><td>Inter</td><td>Image of ORGANISATION chunk</td></tr><tr><td rowspan="2">Marketing skills</td><td rowspan="2">Highly Competent</td><td>Intra</td><td>Product, Competition</td></tr><tr><td>Inter</td><td>Management, People of ORGANISATION chunk</td></tr><tr><td rowspan="2">Service back-up</td><td rowspan="2">Excellent</td><td>Intra</td><td>Product, Demand</td></tr><tr><td>Inter</td><td>Image, People of ORGANISATION chunk</td></tr><tr><td rowspan="2">Demand</td><td rowspan="2">Good</td><td>Intra</td><td>Product, Competition</td></tr><tr><td>Inter</td><td>Image, Industrial relations of ORGANISATION chunk</td></tr><tr><td rowspan="2">Publicity</td><td rowspan="2">Well Covered</td><td>Intra</td><td>Customer profile, Demand</td></tr><tr><td>Inter</td><td>Image of ORGANISATION chunk</td></tr><tr><td rowspan="2">Export possibility</td><td rowspan="2">Good Potential</td><td>Intra</td><td>Government</td></tr><tr><td>Inter</td><td>Image of ORGANISATION chunk</td></tr><tr><td rowspan="2">Competition</td><td rowspan="2">Oligopolistic</td><td>Intra</td><td>Marketing skills, Product, Demand</td></tr><tr><td>Inter</td><td>Image, Industrial relations of ORGANISATION chunk</td></tr><tr><td rowspan="2">Government</td><td rowspan="2">Helpful</td><td>Intra</td><td>Export possibility</td></tr><tr><td>Inter</td><td>Management of ORGANISATION chunk</td></tr><tr><td rowspan="2">Customer profile</td><td rowspan="2">Consumer Product</td><td>Intra</td><td>Price sensitivity</td></tr><tr><td>Inter</td><td></td></tr></table>

In view of the good industry profile, excellent product and market situation and highly competent management, a high FOM for the ROI objective is generated at the super node, inspite of poor industrial relations.

Thus, for the ROI strategic objective, we have the following values:

Based on

(i) Forecasts from past data using SMB : 14%

(ii) Back calculations from given dividend

and interest percentages using SDM : 12%

(iii) Inferencing from SKB : 15–18%

The top manager setting the strategic objective in consultation with concerned divisional manager, views the past data in graphical as well as tabular form (for observing trends/seasonal variations and cyclical patterns), uses his intuition and judgement, as well as fixes the ROI objective at 16%. Likewise, market share percentage is also fixed, from which sales target is determined, say, at 18,500 tonnes of rayon yarn per annum (all deniers and colours included).

Table 2
Schema of ‘ORGANISATION’ chunk

<table><tr><td colspan="4">Chunk: ORGANISATION</td></tr><tr><td colspan="4">Has:</td></tr><tr><td>Macros</td><td>Currency</td><td colspan="2">Connectivity</td></tr><tr><td rowspan="2">Management</td><td rowspan="2">Highly competent</td><td>Intra</td><td>Image, Government</td></tr><tr><td>Inter</td><td>Marketing skills, Customer profile of MARKETING chunk</td></tr><tr><td rowspan="2">People</td><td rowspan="2">Good</td><td>Intra</td><td>Image</td></tr><tr><td>Inter</td><td>Marketing skills of MARKETING chunk</td></tr><tr><td rowspan="2">Industrial relations</td><td rowspan="2">Poor</td><td>Intra</td><td>People, Government</td></tr><tr><td>Inter</td><td>Demand, Competition of MARKETING chunk</td></tr><tr><td rowspan="2">Image</td><td rowspan="2">Poor</td><td>Intra</td><td>Management, People</td></tr><tr><td>Inter</td><td>Demand of MARKETING chunk</td></tr><tr><td rowspan="2">Government</td><td rowspan="2">Indifferent</td><td>Intra</td><td>Industrial relations, Management</td></tr><tr><td>Inter</td><td></td></tr></table>

Table 3
Schema of ‘INDUSTRY’ (rayon) chunk

<table><tr><td colspan="4">Chunk: INDUSTRY (Rayon)</td></tr><tr><td colspan="4">Has:</td></tr><tr><td>Macros</td><td>Currency</td><td colspan="2">Connectivity</td></tr><tr><td rowspan="2">Raw material availability</td><td rowspan="2">Good</td><td>Intra</td><td>Market potential</td></tr><tr><td>Inter</td><td>Demand, Competition of MARKETING chunk</td></tr><tr><td rowspan="2">Scope for modernisation</td><td rowspan="2">Excellent</td><td>Intra</td><td>Market potential, Export scenario, processing</td></tr><tr><td>Inter</td><td>Technology of TECHNICAL chunk</td></tr><tr><td rowspan="2">Market potential</td><td rowspan="2">Very good</td><td>Intra</td><td>Raw material availability, Scope for modernisation, Quality-price interface, Capacity utilisation</td></tr><tr><td>Inter</td><td>Demand, Competition of MARKETING chunk</td></tr><tr><td rowspan="2">Export scenario</td><td rowspan="2">Bright</td><td>Intra</td><td>Scope for modernisation, Quality-price interface, Government policy</td></tr><tr><td>Inter</td><td>Export policy of MARKETING chunk</td></tr><tr><td rowspan="2">Quality/Price interface</td><td rowspan="2">Encouraging</td><td>Intra</td><td>Market potential, Export scenario</td></tr><tr><td>Inter</td><td>Product of MARKETING chunk</td></tr><tr><td rowspan="2">Government policy</td><td rowspan="2">Complementary</td><td>Intra</td><td>Export scenario, Spinning sector, Weaving sector</td></tr><tr><td>Inter</td><td>Government, Demand of MARKETING chunk</td></tr><tr><td rowspan="2">Capacity utilisation</td><td rowspan="2">Broadbanded</td><td>Intra</td><td>Market potential</td></tr><tr><td>Inter</td><td>Demand of MARKETING chunk</td></tr><tr><td rowspan="2">Spinning sector</td><td rowspan="2">Optimum utilisation</td><td>Intra</td><td>Government policy</td></tr><tr><td>Inter</td><td>Demand, Export possibility of MARKETING chunk</td></tr><tr><td rowspan="2">Processing sector</td><td rowspan="2">Keen competition</td><td>Intra</td><td>Scope for modernisation</td></tr><tr><td>Inter</td><td>Demand of MARKETING chunk</td></tr><tr><td rowspan="2">Weaving sector</td><td rowspan="2">Growth oriented</td><td>Intra</td><td>Government policy</td></tr><tr><td>Inter</td><td>Demand of MARKETING chunk</td></tr></table>

## 4.2. Setting tactical and operational targets with TOPP [Arunkumar and Janakiram, 1989c]

Rayon industry has its marketing operations located at a number of centres geographically distributed across the country. Some of the three hundred product varieties have predominant demand at certain of these centres. Tactical planning concerns itself with disaggregating the overall sales and growth targets (strategic objectives) into achievable, productwise, modelwise sales and growth targets for each region, taking the regional characteristics and seasonal variations into account. Further, product level productivity targets (at tactical level) are also determined. Operational planning consists of breaking these tactical sales targets into shopfloor unit/department level operational productivity and other targets in terms of key operational parameters.

## 4.2.1. Tactical targets

PDB contains data regarding, say, sales forecast (planned and actual), production, inventory, price realised per unit, variable cost, contribution per unit, sales value, cost of sales, total market, market share, growth in sales as well as market share at each of the marketing centres for each product and in aggregate for the entire country for the firm as also for key competitors in the industry for the past few years.

Tactical Knowledge Base (TKB) has a major portion of the chunk oriented strategic knowledge of the SKB at the core, embedded with appropriate rule bases at concerned nodes for considering aspects such as expansion, diversification and exports. Navigation is similar to that of SKB. For the particular consultation being discussed, the sales growth factors for various marketing centres and the country as a whole are found to be in the following range:

(i) from forecasts using Tactical Model Base (TMB) : 15–26%

(ii) by inferencing from TKB : 18–25%

The Rayon Marketing Manager, after obtaining these figures, views the data in graphical form for observing any typical trends and patterns or seasonal variations. He decides to set the growth rate at 18% for certain marketing centres, 20% for a few and 25% for others, in consultation with his colleagues on such aspects as capacities, batch quantities, inventory requirements and restrictions, maintenance of plant and equipment and raw material availability. These growth rates are then converted into tactical sales targets for each centre and further aggregated to determine the overall sales target for the country. The ROI is computed using this overall sales target.

(i) Computed ROI : 13%

(ii) Computed overall sales target : 11,000 tonnes

Since these are lower than the strategic objectives laid in Sec. 4.1, the tactical planning exercise is repeated. Sales quantities and prices are reviewed; prices of 120 D and 300 D are increased at four marketing centres, while sales target (quantity to be sold) is increased at two other centres. After three iterations, the expected ROI improved to 16% and overall sales to 18,500 tonnes, thus meeting the strategic targets.

We illustrate below how the rule base embedded in concerned nodes of respective knowledge chunks is invoked, with the help of a consultation walk-through. 'S' represents System queries and 'U' User responses, while explanation under text is within brackets.

## Consultation:

## \* \* \* TACTICAL AND OPERATIONAL PLANNER FOR PRODUCTIVITY (TOPP) WORKING \* \* \*

## \* \* \* Hypothesis

Demand potential exists and not fully met. Capacity utilisation is 100%.

RULE 3
IF 1. Market potential exists, AND
2. Production capacity exists

## THEN Sales can be increased

S : Which is the bottleneck department?

U : After Treatment

S : Can balancing equipment augment capacity?

U : Yes

S : By how much?

U : 20%

RULE 25

IF 1. Demand is not fully met, AND

2. Capacity utilisation = 100%, AND

3. Demand is likely to continue, AND

4. Balancing equipment can augment capacity

THEN Consider expansion by balancing equipment

## \* \* \* Inference

## Consider expansion

S : Do you require any other plant and machinery?

U : No

S : Do you need to import additional raw material or components?

U : No

S : Any scarce raw material used?

U : Why?

S : IF No strain on scarce raw material due to extra production
THEN Additional production upto 25% of approved capacity allowed (System displays Rule 16 of ‘Industry’ Chunk)

Any scarce raw material used?

U : No

## \*\*\* Finding

Approval for 20% addition capacity can be obtained by procuring balancing equipment in After Treatment department.

(TOPP works out that ROI can be increased up to 15% by augmenting capacity in AT department, when the sales will go up by 20% to 14,500 Tonnes. These are not yet matching the corporate objectives of 16% ROI and 18,500 tonnes sales. Further, the system knows from TKB that deniers above 300 D can also be produced on tyre cord machinery, and from PDB that tyre cord demand has shrunk.)

## RULE 24

IF Capacity is granted separately for each item in an industrial licence and demand for some shrinks

THEN Capacities can be merged and overall licence got issued

[Also from 'Industry' (Rayon) Chunk]

RULE 23

IF Demand shrinks for tyre yarn/cord

THEN Tyre cord plant can produce filament yarn within existing capacity

## \* \* \* Inference

Produce filament yarn of higher deniers (> 300 D) in tyre cord plant.

(TOPP works out that if higher deniers are produced in tyre cord plant, more quantity of lower deniers can be produced in Rayon filament yarn plant and the overall production/sales can be increased beyond the target of 18,500 tonnes and the ROI increased up to 16%, thus satisfying the strategic targets.)

(The intermediate and annual tactical sales targets are finalised as shown in table 4.)

## 4.2.2. Operational targets

The Operational Planner (OP) submodule of TOPP develops operational targets from the tactical targets, by exploding the latter [see Gold in Eilon, 1976] to unit, department or stage level (fig. 4). At the first level of explosion, the total quantity of yarn to be produced is broken into tonnes of viscose in VISCOSE department, tonnes of spinbath in SPINBATH department, number of cakes in SPINNING department, number of carriers (cakes) processed in AFTER TREATMENT, number of cones wound in

Table 4
Tactical sales targets

<table><tr><td rowspan="2">Product/ Denier</td><td colspan="12">Monthly sales targets (tonnes of yarn)</td><td rowspan="2">Annual target 1989</td></tr><tr><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td></tr><tr><td>Bright</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 D</td><td>120</td><td>130</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>160</td><td>160</td><td>160</td><td>180</td><td>180</td><td>1840</td></tr><tr><td>75 D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100 D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>120 D</td><td>250</td><td>250</td><td>320</td><td>300</td><td>280</td><td>290</td><td>310</td><td>300</td><td>300</td><td>300</td><td>350</td><td>350</td><td>3600</td></tr><tr><td>180 D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>200 D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>250 D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>300 D</td><td>300</td><td>300</td><td>350</td><td>350</td><td>375</td><td>375</td><td>375</td><td>375</td><td>240</td><td>240</td><td>350</td><td>350</td><td>4000</td></tr><tr><td>400 D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>600 D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 D Colour Peacock</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Blue</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>2400</td></tr><tr><td>Orange Yellow</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Black</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>250</td><td>250</td><td>200</td><td>200</td><td>200</td><td>200</td><td>2200</td></tr><tr><td>Red</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dull</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100 D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>120 D</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>250</td><td>250</td><td>250</td><td>250</td><td>300</td><td>300</td><td>300</td><td>2900</td></tr><tr><td>140 D</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 5  
Operational productivity targets

<table><tr><td>Productivity Index (PI)</td><td>Unit</td><td>Target</td></tr><tr><td colspan="3">a) Raw Material</td></tr><tr><td>i) Pulp</td><td>Kg/Kg of yarn</td><td>1.09</td></tr><tr><td>ii) Caustic Soda</td><td>Kg/Kg of yarn</td><td>0.65</td></tr><tr><td>iii) Carbon Disulphide</td><td>Kg/Kg of yarn</td><td>0.30</td></tr><tr><td>iv) Sulphuric Acid</td><td>Kg/Kg of yarn</td><td>1.00</td></tr><tr><td colspan="3">b) Auxiliary Material</td></tr><tr><td>i) Zinc</td><td>Kg/Kg of yarn</td><td>0.01</td></tr><tr><td>ii) Filter Medium</td><td>Ps/Kg of yarn</td><td>11.00</td></tr><tr><td>iii) AT Wrappers</td><td>Ps/Kg of yarn</td><td>10.00</td></tr><tr><td>iv) AT Chemicals</td><td>Ps/Kg of yarn</td><td>30.00</td></tr><tr><td>v) Coning Oil</td><td>Ps/Kg of yarn</td><td>18.00</td></tr><tr><td>vi) Additives</td><td>Ps/Kg of yarn</td><td>11.00</td></tr><tr><td>vii) Water</td><td>Gallons/Kg of yarn</td><td>105.00</td></tr><tr><td colspan="3">c) Energy</td></tr><tr><td>i) Power</td><td>Kwh/Kg of yarn</td><td>7.00</td></tr><tr><td>ii) Steam</td><td>Kg/Kg of yarn</td><td>17.50</td></tr><tr><td colspan="3">d) Labour</td></tr><tr><td>i) Direct</td><td>Mandays/Kg of yarn</td><td>7.50</td></tr><tr><td>ii) Indirect</td><td>Mandays/Kg of yarn</td><td>2.15</td></tr></table>

TEXTILE department and number of cones inspected and packed by PACKING department. In each department, further explosion is made and operational targets for each section, stage determined; for e.g., in SPINNING, number of candle filters assembled, jets washed and polished, gooseneck assemblies made per manday are some of the operational targets. Likewise, key operational parameters (see sec. 4.3) for each process are laid down, for e.g., in SPINNING, the spinning speed and godet waste for each product and machine type are determined from past performance.

PDB contains data on PIs achieved in past years, the best so far, as well as competition and industry averages for material (raw, auxiliary and maintenance stores), energy, labour and other partial productivities.

The production manager in consultation with his key operational staff determines the operational targets in terms of PIs in light of standards, past performance and trends thereof, as well as prevailing operational conditions. Appropriate adjustments are made for any improvements brought about in methods, process, materials and/or operating conditions. A typical output of TOPP showing PIs (operational targets) is presented in table 5.

Using the tactical objectives and the PIs as also the cost and price data, EBIT and ROI are computed and found that an ROI target of 16% (strategic objective) can be achieved. These targets are then frozen for the year for the plan premises.

## 4.3. Performance Monitoring by PM [Arunkumar and Janakiram, 1989d]

<table><tr><td colspan="4">PM obtains actual values of certain operational parameters on a day to day basis and compares them with targets laid down by PS. Some operational parameters and their norms are:</td></tr><tr><td>(i)</td><td>VISCOSE</td><td>: Number of batches steeped/shift</td><td>34</td></tr><tr><td>(ii)</td><td>SPINBATH</td><td>: Number of central troughs of spinning machine emptied/shift</td><td>30</td></tr><tr><td>(iii)</td><td>SPINNING</td><td>: Number of doffs/shift</td><td>22</td></tr><tr><td>(iv)</td><td>AFTER</td><td>: a) Number of carriers processed/shift</td><td>45</td></tr><tr><td></td><td>TREATMENT</td><td>: b) Number of hold-up cakes</td><td>10,000</td></tr><tr><td>(v)</td><td>TEXTILE</td><td>: First Quality percentage</td><td>55%</td></tr><tr><td>(vi)</td><td>PACKING</td><td>: Number of cases packed/shift</td><td>500</td></tr></table>

A consultation walk-through for Monitor working is given below:

## \* \* \* PRODUCTIVITY MONITOR (PM) WORKING \* \* \*

<table><tr><td rowspan="3">Mode: WatchdogNumber of Doffs per Shift:</td><td colspan="4">Period: 1</td></tr><tr><td>Actual:</td><td>21;</td><td>Target:</td><td>22</td></tr><tr><td>Variation:</td><td>-1;</td><td>Shortfall:</td><td>-4.55%</td></tr></table>

(The diagnostic mode will take over for investigating reasons for number of doffs being less than target.)

RULE 10

IF 1. Spinning machine downtime >22 HRS, OR

2. Power failure occurs, OR

3. Spinning mandays per tonne are higher than normal

THEN Number of doffs per shift will be < 22

(PM checks that there was no power failure and that downtime is within norm. PM finds spinning mandays per tonne are higher by 0.3 (actual of 2.4 against a target of $2 \pm 0.1$ , i.e., a deviation of $14.3\%$ ).

## RULE 1

IF 1. Performance is outside control limits, AND

2. It is the first or second time, AND

3. Variation is $< 5\%$

THEN 1. Indicate there is no cause for alarm, AND

2. Pass control to COP

## ELSE Pass control to PE

(Since variation is >5%, control is passed to PE for detailed investigation).

A typical output from PM in the review mode is shown in table 6.

## 4.4. Performance Evaluation by PE-Spinning Mandays / Tonne of yarn

PE, upon receiving a trigger from PM, splits the productivity index into its constituent elements, viz.,

$$
\begin{array}{l} \text {Spinning} \\ \text {Mandays} \\ \text {Per Tonne} \\ \text {of Yarn} \end{array} = \frac {\frac {\text {Spinner}}{\text {Mandays}} + \frac {\text {Patrolman}}{\text {Mandays}} + \frac {\text {Doff}}{\text {Truckman}} + \frac {\text {Cake}}{\text {Truckman}}}{\text {(m} _ {1}) \text {(m} _ {2}) \text {(m} _ {3}) \text {(m} _ {4})} \text {(m} _ {4}){\text {Tonnage of Yarn produced}} = \frac {\mathrm{m} _ {1}}{\text {Tonnage}} + \frac {\mathrm{m} _ {2}}{\text {Tonnage}} + \frac {\mathrm{m} _ {3}}{\text {Tonnage}} + \frac {\mathrm{m} _ {4}}{\text {Tonnage}}.
$$

$m_{3}/Tonnage$ is found to be out of control while the other three ratios are within control. $m_{3}$ is found to be well within the targeted figure, while tonnage differed from target, which is broken up as

Tonnage = Good cakes × Weight per cake.

Good cakes = Total cakes - Kanji cakes - Damaged cakes - Shaved cakes - Repieced cakes - Curly cakes.

Consultation proceeds as follows:

```kotlin
* * * PRODUCTIVITY EVALUATOR (PE) WORKING * * *
```

(Upon checking quantities of various types of bad cakes, PE found that repieced cakes are higher than permitted)

## \* \* \* Finding

Number of Repieced cakes produced, viz., 450 is more than the permitted limit of 400.

## \*\*\* Hypothesis

Number of Repieced cakes is more than desirable

## RULE 8

IF

1. Filtration pressure is >3.4, OR

2. Ripening index is $< 9.8 \pm 0.2$ , OR

3. Spinbath temperature is $< 54^{\circ}\mathrm{C}$ , OR

4. Guides are jammed/scratched/pitted, OR

5. CF maintenance is delayed, OR

6. Acidity is $>138 \pm 1$ gpl

THEN Repieced cakes will be more than desirable

(Upon checking process conditions, PE finds spinbath temperature is $50^{\circ}$ C only. PE continues further:)

Table 6  
Typical output of Productivity Monitor (review mode)

<table><tr><td colspan="5">Monitor review for the month of</td></tr><tr><td>Productivity Indices</td><td>Target</td><td>Actual</td><td>Variance</td><td>Remarks</td></tr><tr><td>Raw material</td><td></td><td></td><td></td><td></td></tr><tr><td>Pulp</td><td>1.090</td><td>1.150</td><td>-ve</td><td>Pulp combination to be checked</td></tr><tr><td>Caustic</td><td>0.650</td><td>0.650</td><td>OK</td><td></td></tr><tr><td> $CS_2$ </td><td>0.300</td><td>0.295</td><td>OK</td><td></td></tr><tr><td> $H_2SO_4$ </td><td>1.000</td><td>1.005</td><td>OK</td><td></td></tr><tr><td>Zinc</td><td>0.010</td><td>0.010</td><td>OK</td><td></td></tr><tr><td>Auxiliary material</td><td></td><td></td><td></td><td></td></tr><tr><td>Filter Cloth</td><td>7.750</td><td>11.000</td><td>-ve</td><td>42% variation, first time; Evaluation necessary</td></tr><tr><td>AT Chemicals</td><td>30.000</td><td>30.000</td><td>OK</td><td></td></tr><tr><td>Coning Oil</td><td>18.000</td><td>18.050</td><td>OK</td><td></td></tr><tr><td>Additives</td><td>11.000</td><td>11.000</td><td>OK</td><td></td></tr><tr><td>AT Wrappers</td><td>10.000</td><td>12.000</td><td>-ve</td><td>20% variation, Quality of wrappers to be checked</td></tr><tr><td>Packing material</td><td></td><td></td><td></td><td></td></tr><tr><td>Wooden Cases</td><td></td><td></td><td></td><td></td></tr><tr><td>Corrugated Boxes</td><td></td><td></td><td></td><td></td></tr><tr><td>Other Materials</td><td></td><td></td><td></td><td></td></tr><tr><td>Energy</td><td></td><td></td><td></td><td></td></tr><tr><td>Power</td><td>6.970*</td><td>7.250</td><td>-ve</td><td>-ve for 4th time in a row showing rising trend over last 3 reviews</td></tr><tr><td>Steam</td><td>17.910</td><td>17.800</td><td>OK</td><td></td></tr><tr><td>Water</td><td>105.000</td><td></td><td></td><td></td></tr><tr><td>Effluent</td><td></td><td></td><td></td><td></td></tr><tr><td>Treatment</td><td></td><td></td><td></td><td></td></tr><tr><td>Chemicals</td><td></td><td></td><td></td><td></td></tr><tr><td>Waste</td><td></td><td></td><td></td><td></td></tr><tr><td>Godet</td><td>1.100±0.10</td><td>1.180</td><td>OK</td><td>Within control, but 5 out of 7 points near UCL</td></tr><tr><td>Hard</td><td>1.250±0.15</td><td>1.360</td><td>OK</td><td>Within control, but 5 out of 7 points near UCL</td></tr><tr><td>Maintenance</td><td></td><td></td><td></td><td></td></tr><tr><td>Spares</td><td></td><td></td><td></td><td></td></tr><tr><td>Consumables</td><td></td><td></td><td></td><td></td></tr><tr><td>Other Expenses</td><td></td><td></td><td></td><td></td></tr><tr><td>Labour</td><td></td><td></td><td></td><td></td></tr><tr><td>Direct</td><td>7.500</td><td></td><td></td><td></td></tr><tr><td>Indirect</td><td>2.150</td><td></td><td></td><td></td></tr></table>

\* Revised target.

## \* \* \* Finding

Spinbath temperature is less than specified

RULE 21

1. Heat Exchanger in spinbath department is not properly adjusted, OR

2. Thermostat of Heat Exchanger is not working properly

THEN Spinbath temperature will be less than specified

S : Is the thermostat of Heat Exchanger working properly?

U : Why?

S : It is to find out why spinbath temperature is less than specified. If thermostat is working properly, it may be concluded. Heat Exchanger is not properly adjusted. In the thermostat machine approach?

U : Yes

## \* \* \* Inference

Heat Exchanger in spinbath department is not adjusted properly

(It is thus found that spinning labour productivity suffered because of inefficient working in spinbath department.)

## 4.4.1. Runs And Trends

If the number of repieced cakes is within tolerable limit, but is showing an increasing trend, PE checks, which one of, filtration pressure, ripening index, spinbath temperature, acidity and CF maintenance schedule, is showing an increasing trend over a period and gives an early warning accordingly. If none of these is showing an increasing adverse trend, PE concludes that the remaining reasons, viz., jammed/scratched/pitted guides are responsible for increasing number of repieced cakes.

## 4.4.2. Changes in Plan Premises

While monitoring the material PIs, PM observes, that actual pulp yield ratio of 0.80, is lower than the target of $0.95 \pm 0.05$ and invokes PE for evaluation, by virtue of Rule 1 mentioned in the consultation walk-through of Sec. 4.3.

```txt
* * * PRODUCTIVITY EVALUATOR (PE) WORKING * * *
Evaluation Period: January 89
RULE 40
IF    1. α-Cellulose is < 89%, OR
2. Moisture percentage is >5–10%, OR
3. Hemicellulose is >4–5%
THEN    Yield ratio of yarn will be < 0.9
```

(PE checks that $\alpha$ -Cellulose and Hemicellulose content are less than 89% and 4% respectively in January 1989 and these are associated with a blending ratio of 50:50 between imported and local pulp against a plan target combination of 60:40. PE works out yield ratio expected for 50:50 combination.)

## \* \* \* Inference

Pulp ratio assumed under plan : 60:40

Actual pulp ratio : 50:50

Yield ratio for 50:50 combination : 0.75

Performance okay.

(Thus, though PM indicated adverse variation, PE justified the performance as okay in view of the changed conditions. Yield ratio has an effect on production of yarn. Further, the system makes the following queries.)

S : Will the pulp combination be restored in February 89?

S : In March 89?

U: No

S : When will the pulp combination be restored to 60:40 level?

```txt
U: Why?
```

Table 7  
Typical output of Productivity Evaluator

<table><tr><td colspan="6">Evaluation Report for the Month of......</td></tr><tr><td>Productivity Index</td><td>Target</td><td>Actual</td><td>Variance</td><td>Monitor report</td><td>Evaluation</td></tr><tr><td>Filter material</td><td>7.75</td><td>11.00</td><td>-ve</td><td>42% variation, First time, Evaluation necessary</td><td>Impurities in viscose abnormal due to low quality of pulp (Impurity level more than specification limits). PURCHASE department to be consulted.</td></tr><tr><td>Power</td><td>6.97*</td><td>7.25</td><td>-ve</td><td>-ve for 4th time in a row</td><td>Power consumption in SPINNING exceeds target for 4th time in a row. SPINNING department to be consulted.</td></tr><tr><td>Steam</td><td>17.91</td><td>17.80</td><td>OK</td><td>Showing rising trend over last three reviews</td><td>Dryer consumption exceeds target due to wet cake condition. SPINNING department to be consulted.</td></tr><tr><td>Godet waste</td><td>11±1</td><td>1.18</td><td>OK</td><td>Within control; but five out of seven points near UCL</td><td>Waste is rising due to delay in attending to idle positions caused by thread breakages owing to high Ripening Index.Consult VISCOSE department.</td></tr><tr><td>Hard Waste</td><td>1.25±0.15</td><td>1.36</td><td>OK</td><td></td><td>Hard waste seems to be increasing due to improper handling and defective peg boards in TEXTILE department.</td></tr></table>

\* Revised target.

S : If the restoration of pulp combination to 60:40 level takes longer than 3 months, strategic objectives need to be reset. Otherwise, the tactical targets only will have to be revised.

When will the pulp combination be restored to 60:40 level?

U: April 89

(PE concludes the aberrations are major and invokes TOPP for resetting the strategic objectives for the remaining plan period).

(If the user's answer was ‘February 89’, the aberration would have been insignificant and control would have gone to COP for revising intermediate targets, retaining overall period-ending tactical and operational targets).

(On the other hand, if the user had answered ‘November 89’, PE would have concluded the aberrations are drastic and control would have passed to ESP for resetting strategic objectives. Shifting of control depends on whether the shortfall can be made good under the changed conditions, in the remaining part of the plan period.)

A typical output from PE is shown in table 7.

## 4.5. Revision of targets by COP

Suppose, in the consultation walk-through presented in Sec. 4.4.2, the user has responded 'yes' to the system's query "Will the pulp combination be restored in February 89?", PE would treat it as a minor variation (variation being $11.1\%$ and time remaining for make up being 11 months) and control would pass to COP. The consultation walk-through, for this case is given below:

## \* \* \* CONTROLLER OF OPERATIONAL PRODUCTIVITY (COP) WORKING \* \* \*

THEN 1. Adjust difference over remaining periods, AND

2. Keep period-ending targets same

(Original monthly production target is 30 T. Shortfall of 11.1% in January, will be equally distributed to all months from February to December.)

## \* \* \* Result

The revised monthly target from February to December is: 30.303 T

(Alternatively, if the user desires so, targets for February, March and April can be increased appropriately to fully make up the shortfall and balance months can have original targets).

(Suppose, production in the month of January was 29 T against a target of 30 T. PM directs control to COP, variation being less than 5% and occurring for the first time.)

## RULE 1

IF Shortfall is $< 10\%$ in any period

THEN 1. Adjust difference over remaining periods, AND

2. Retain period-ending targets same

## \* \* \* Result

The revised monthly target from February to December is: 30.09 T

(Alternatively, user, by interaction, may choose to increase targets for February and March to 30.5 T and for the remaining months, retain the old target of 30 T. COP suggests appropriate productivity techniques also for achieving the revised targets by invoking Rule 9 of its KB.)

## RULE 9

IF Production is to be increased marginally (< 5%) over a small period (1–3 months)

THEN 1. Spinning speed can be increased, OR

2. Doff time can be increased

(Rayon plant manager can increase spinning speeds if scope exists or doff time or both in order to make up for the shortfall in January).

## A typical output from COP is shown in table 8.

## Table 8

Typical output of Controller of Operational Productivity.

<table><tr><td colspan="11">Controller Report for the Month of......Targets for the remaining months of the year are reset as follows:</td><td></td></tr><tr><td rowspan="2">Productivity index</td><td rowspan="2">Original target</td><td rowspan="2">Achieved till April</td><td colspan="8">Reset Targets</td><td rowspan="2">Suggested productivity technique</td></tr><tr><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td></tr><tr><td>Yarn production</td><td>35.62</td><td>35.00</td><td>36</td><td>36</td><td>36</td><td>36</td><td>36</td><td>36</td><td>36</td><td>36</td><td>PERT (increasing machine utilisation by reducing maintenance time)</td></tr><tr><td>Hard waste</td><td>1.25 ± 0.15</td><td>1.36</td><td colspan="8">|←→1.0 ± 0.1→|</td><td>Training, educating and motivating labour</td></tr><tr><td>Packing manpower</td><td>0.05</td><td>0.75</td><td colspan="8">|←→0.1→|</td><td>Work study</td></tr><tr><td>Steam</td><td>17.91</td><td>17.80</td><td colspan="8">|←→18.0→|</td><td>Training and educating spinners (to reduce wet cakes)</td></tr></table>

## 5. Conclusion

Rayon industry, a labour intensive, multi-stage continuous chemical processing industry, is an important sector for the application of ISPM. ISPM being knowledge based, fixes up realistic and achievable objectives, after proper environmental scanning and situational assessment [Granger, 1964]. ISPM monitors actual performance vis-a-vis targets and presents detailed evaluation of adverse and extremely favourable performances. In particular, the conditions, leading to extremely favourable performance, can be captured by the learning mechanism of the system and incorporated in the KB for bringing future improvements. The system helps control deviations by revising/resetting targets (in light of changed conditions and planning premises) and suggesting suitable techniques for improvement.

As seen from the consultation illustrated, PE might justify an adverse performance indicated by PM as okay in the changed circumstances. Whenever drastic changes in environment or planning premises are noticed, the system automatically resets various objectives, thus making them realistic. Also if objectives at any of the upstream stages are not achieved, and if this has an effect on one or more of the down-stream stages, the system can detect the same accurately and pinpoint responsibility properly.

PIs can be formulated uniformly in terms of the final (and major) output, viz., kg. of yarn produced; stage wise, inter temporal comparisons can be achieved with the help of SOFT model proposed by the authors $[1989f]$ . Substantive benefits can be derived from productivity improvements in rayon industry through the application of ISPM.

## 6. Acknowledgement

The authors wish to thank Mr Durgeshchandra, Joint President, Century Rayon for his encouragement. This research is part of the Intelligent Systems (IS) Project at IIT, Bombay from the Ministry of Human Resources Development, Government of India.

## References

Arunkumar, S., and Janakiram, N.: Management for Greater Productivity - A Pivotal Role for a Knowledge Based System, Proceedings of the XI National Convention of Institution of Industrial Managers, India at Bombay (April 1989a).

Arunkumar, S., and Janakiram, N.: Intelligent System for Productivity Management, Technical Report No. ISP-4, Intelligent Systems Project, Indian Institute of Technology, Bombay (1989b).

Arunkumar, S., and Janakiram, N.: TOPP: Tactical and Operational Planner for Productivity, Technical Report No. ISP-6, Intelligent Systems Project, Indian Institute of Technology, Bombay (1989c).

Arunkumar, S., and Janakiram, N.: MECOP: Monitor, Evaluator and Controller of Productivity, Technical Report No. ISP-7, Intelligent Systems Project, Indian Institute of Technology, Bombay (1989d).

Arunkumar, S., and Janakiram, N.: A Study of Capital Productivity Measure ROI as Strategic Objective, Productivity, 30 (3) (Oct-Dec 1989e) pp. 296–303.

Arunkumar, S., and Janakiram, N.: SOFT: A Structured Approach to Productivity Measurement, Technical Report No. ISP-2, Intelligent Systems Project, Indian Institute of Technology, Bombay (1989f).

Arunkumar, S., and Janakiram, N.: Knowledge Based Strategic Planning System, Proc. of IEE International Conference on Export Planning Systems, Brighton, UK (June 1990) pp. 239–244.

Bailey, J.E.: Energy, Labour and Capital Considerations in Productivity Enhancements: An Editorial, AIIE Transactions, 10 (3) (Sept. 1978) pp. 279–284.

Deshpande, M.M.: A Study of Productivity Aspects in Chemical Process Industry, Ph.D. Seminar Report, Industrial Management Programme, Indian Institute of Technology, Bombay (May 1989).

Eilon, S., Gold, B., and Soesan, J.: Applied Productivity Analysis for Industry, Pergamon Press (1976).

Ganguly, A.S.: Productivity and Development, Speech delivered by the Chairman at the Annual General Meeting, Hindustan Lever Ltd., Bombay (May 15, 1987).

Granger, C.H.: The Hierarchy of Objectives, Harvard Business Review (May–June 1964) pp. 63–74.

Hufnagel, E.M.: Information Systems Planning: Lessons from Strategic Planning, Information and Management (Dec. 1987) pp. 263–270.

Labour Productivity Survey: 1952–1965, Ministry of Labour, Government of Japan (1966).

Moncrieff, R.W.: Man-made Fibres, Sixth Edition, Newnes-Butterworths, London (1975).

Nishikawa, S., Sazanami, Y., and Yamada, S.: Productivity Measurement Manual, Asian Productivity Organisation, Tokyo, Japan (1969).

Rhyne, L.C.: The Relationship of Information Usage Characteristics to Planning System Sophistication: An Empirical Examination, Strategic Management Journal, 6 (4) (1985) pp. 319–337.

Sahu, K.C.: Managing Productivity: Some Basic Issues, Industrial Engineering Journal, 15 (8) (1986) pp. 11–12.

## Appendix

## Rayon process description

I STEEPING: Sheets of wood pulp (cellulose purified to about 92–93%) are soaked for about an hour in a strong solution of Caustic Soda (about 19% NaOH) in rectangular tanks called steeping presses. A surface active chemical, Dope B, is added in the Caustic for better penetration. The pulp sheets become greatly swollen and the impurities are dissolved in Caustic Soda. The excess alkali is pressed out by a hydraulic ram in the steeping press. This is the conventional form of steeping and is called the Batch Process. In the Slurry Process of steeping, pulp and Caustic are agitated inside a tank and the slurry so formed is passed between squeeze rollers to get a swollen pulp mat.

$$
\begin{array}{c}\left(\mathrm{C} _ {6} \mathrm{H} _ {1 0} \mathrm{O} _ {5}\right) _ {\mathrm{n}} + \mathrm{nNaOH} \rightarrow \left(\mathrm{C} _ {6} \mathrm{H} _ {9} \mathrm{O} _ {4} \mathrm{ONa}\right) _ {\mathrm{n}} + \mathrm{nH} _ {2} \mathrm{O}\\\uparrow\\\text {Cellulose}\end{array}
$$

II SHREDDING: The soaked and pressed pulp sheets from the steeping process are dumped inside shredders and broken up into finely divided consistent fluffy crumbs by grinding action. Dope B is added inside the shredder to prevent sticking. The shredder is jacketed for hot and cold water and inside it are located two serrated blades. The Alkali Cellulose formed during shredding is aged by heating (using hot water externally) and cooling in order to get the desired viscosity for viscose.

III CHURNING: The Alkali Cellulose crumbs are dumped inside hexagonal churns and Carbon Disulphide is introduced into the churn through a distribution pipe. The churns are jacketed for cold water circulation and are rotated for about an hour, during which time the Alkali Cellulose is converted into a soluble compound called Sodium Cellulose Xanthate.

$$
\begin{array}{c}\left(\mathrm{C} _ {6} \mathrm{H} _ {9} \mathrm{O} _ {4} \mathrm{ONa}\right) _ {\mathrm{n}} + \mathrm{nCS} _ {2} \rightarrow \quad \mathrm{SC} \left\{\mathrm{SNaOC} _ {6} \mathrm{H} _ {9} \mathrm{O} _ {4} \right\} _ {\mathrm{n}}\\\uparrow\\\text {Alkali Cellulose}\end{array}
$$

IV DISSOLVING: The Xanthate is dropped into dissolvers containing cooled dilute solution of Caustic Soda (2.5% NaOH) and stirred vigorously to form a golden brown viscous liquid known as Viscose.

V BLENDING: Viscose from various dissolvers is mixed together in a big common tank called Blender and stirred constantly to get viscose of uniform quality and characteristic.

VI RIPENING, FILTRATION AND DEAERATION: The fresh viscose solution from Blender is ripened for about 20 hours at controlled temperature. During this time, viscose is purified by filtering through different media to remove undissolved impurities. Finally, air bubbles in the viscose are removed by deaeration under vacuum.

VII COAGULATING BATH (SPINBATH): Viscose is spun through a coagulating bath to produce yarn. The coagulating bath is made up of Sulphuric acid, Zinc Sulphate and Sodium Sulphate and is kept at a temperature of 55–56°C. Zinc is added in the form of Zinc plates, Zinc Oxide or Zinc Hydroxide and

Zinc Sulphate is formed by the reaction of Zinc with Sulphuric acid. Dope B is also added in the bath for reducing the surface tension. Addition of defoamer is also necessary to prevent foaming. The coagulating bath is continuously recirculated in the process, after making up for process losses. Sodium Sulphate is formed by neutralization of Sodium Hydroxide present in the viscose with Sulphuric acid of the bath. The concentration of acid in spinbath is maintained by the addition of strong Sulphuric acid. Viscose, coming in contact with spinbath, gets coagulated and cellulose is regenerated in the form of fine filaments. The presence of Zinc helps to impart more stretch to the yarn and improve its strength by controlling the rate of coagulation and regeneration of viscose.

VIII SPINNING: The viscose solution is forced with pressure along pipe lines by a gear pump to the spinnerette on the spinning machine through a candle filter. Viscose comes out of the spinnerette into the coagulating bath, generating cellulose in the form of fine filaments. As the filaments emerge from the spinnerette, they are first guided round the bottom glass godet through special ceramic thread guides. From the bottom godet, the filaments pass to the top glass godet. The top godet is driven faster than the bottom one, thus stretching the filaments in between. From the top godet, the yarn descends vertically through a glass funnel into a centrifugal spinning pot.

![](/api/attachments/A24QDAA9/fulltext/images/62386c90571ea853a34fe094f0794bf11eb8281155e5229b27cfe952646e37dc.jpg)

IX CAKE FORMATION: The spinning pot revolves at a speed of about 8,000 rpm. The yarn gets collected inside the pot in the form of a cake. The high speed of the pot gives a twist to the yarn. The cake is removed (doffed) at regular intervals.

X AFTER TREATMENT: The yarn in the raw cakes is impure containing acid and other metallic impurities and therefore has to be purified. The cakes are placed on carriers (after wrapping them in cloth jackets to prevent the layers of wound yarn getting disturbed during washing) and given a series of washes in the following order:

Water washes for removing acidity, Sodium Bicarbonate solution wash for removing residual acidity, Sodium Sulphide solution wash for removing Sulphur, Bleach solution wash for bleaching, E.D.T.A. solution wash for removing metallic impurities and lastly, Finish solution (Finish oil + soap) wash for giving softness to the yarn.

The cakes are hydro-extracted in high speed spinning pots to remove free water and fed into the dryers, on trucks.

XI DRYING: The cakes are dried in dryers at a temperature of 80–85°C for about 72 hours, whereby the moisture in the cakes is removed. The dried cakes are then stored in a conditioning room at 27°C and 65% relative humidity. Under these conditions, the yarn regains up to the specified amount of moisture.

XII CONING: The conditioned yarn is then wound into compact cones on coning machines. During coning, the yarn is brought in contact with a moving roller dipped in a coning oil. This imparts a soft feel to the yarn and reduces yarn-to-metal friction. The cones are then graded for quality by visual inspection and packed in cases.
