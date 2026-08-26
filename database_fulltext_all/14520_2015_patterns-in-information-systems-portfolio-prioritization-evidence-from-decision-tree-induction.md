---
otero_id: 14520
otero_key: "MSBGCYRT"
title: "PATTERNS IN INFORMATION SYSTEMS PORTFOLIO PRIORITIZATION: EVIDENCE FROM DECISION TREE INDUCTION"
authors: "Prasanna Karhade; Michael J. Shaw; Ramanath Subramanyam"
year: "2015-06"
journal: "MIS Quarterly"
doi: "10.25300/misq/2015/39.2.07"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# PATTERNS IN INFORMATION SYSTEMS PORTFOLIO PRIORITIZATION: EVIDENCE FROM DECISION TREE INDUCTION<sup>1</sup>

Prasanna Karhade

Department of Information Systems, Business Statistics and Operations Management, The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, HONG KONG {karhade@ust.hk}

Michael J. Shaw and Ramanath Subramanyam

Department of Business Administration, University of Illinois at Urbana–Champaign, Champaign, IL 61820 U.S.A. {mjshaw@illinois.edu} {rsubrama@illinois.edu}

Questions pertaining to the locus of information systems (IS) governance have been extensively examined in existing research. However, questions pertaining to the decision rationale applied for IS portfolio prioritization (why are certain initiatives approved, and why are certain others rejected), noted to be a critical component of IS governance, need further investigation. We submit that the IS strategy of a firm is likely to explain the decision rationale it applies to IS portfolio prioritization and maintain that it is critical to ensure this decision rationale is in congruence with the firm’s IS strategy. By extending prior theoretical work on IS strategy types, we develop theoretical profiles of the decision rationale applied to IS portfolio prioritization using three attributes: communicability of decision rationale, consistency in applying decision rationale, and risk appropriateness of decision rationale. Since the decision rationale applied for IS portfolio prioritization is often tacit, unknown even to the decision makers themselves, we employ the decision tree induction methodology to discover this tacit decision rationale. We analyze over 150 IS portfolio prioritization decisions on a multimillion dollar IS portfolio of a multibusiness, Fortune 50 firm and our findings, which support our propositions, indicate that firms that adopt different IS strategies rely on systematically different profiles of decision rationale for IS portfolio prioritization. Implications for IS governance practices are developed.

Keywords: IS strategy, IS portfolio prioritization, IT portfolio management, IS governance, IT governance, decision making, decision tree induction

## Introduction

For most Fortune 500 firms today, their investment in initiatives that depend on information systems (IS) is growing in importance (Kohli 2007; Piccoli and Ives 2005). As most firms have hundreds of such initiatives running simultaneously (Jeffery and Leliveld 2004), chief information officers (CIOs) need to ensure that the decision rationale used for IS portfolio prioritization is in congruence with their IS strategies. The impact of IS strategies on the decision rationale (DR) used for IS portfolio prioritization (ISPP) has been rather understudied.<sup>2</sup> Although prior research contrib utes insights by examining approved IS investments, “it is also important to understand which investments do not make it through the decision process and why” (Xue et al. 2008, p. 88, emphasis added).

One of the key goals of IS governance is to encourage desirable behavior in the prioritization and use of IS (Weill and Ross 2004, p. 11). As decision rights are integral to IS governance, it is important to ensuring effective ISPP decision making. Understanding the DR used for ISPP is critical as incongruence between DR and a firm’s IS strategy is not only likely to be associated with allocation of investment in unsuitable IS initiatives, but also associated with firms missing out on key IS-enabled strategic business opportunities. In spite of extensive research delving into who, and at what stages of the process, makes IS governance decisions (Brown 1997; Sambamurthy and Zmud 1999; Weill and Ross 2004; Xue et al. 2008), there exists a need for research that focuses on why certain initiatives are approved and why certain others are rejected.

To address this gap, we extend prior theoretical work on IS conservative–innovator Strategy types (Chen et al. 2010) to develop theoretical profiles of the DR used for ISPP. We develop theoretical profiles of the DR by relying on three attributes that succinctly characterize decision making, namely (1) communicability of DR (Segars and Grover 1999), (2) consistency in applying DR (Chen et al. 2010), and finally (3) risk appropriateness<sup>3</sup> of DR (Boynton and Zmud 1987). We propose that characteristics of IS conservative strategy— a stable external environment, formal decision-making structure, and risk-averse tendencies for continual efficiency improvements—are likely to collectively exert a similar influence on DR it uses for ISPP. Characteristics of IS innovator strategy include a dynamic external environment, organic decision-making structure, and risk-taking tendencies for pursuing new opportunities. As ignoring emerging opportunities in the external environment imposes prohibitively high opportunity costs on IS innovators (Chen et al. 2010, p. 252), the dynamic external environment is likely to exert a strong influence on the DR it uses for ISPP.

We analyze ISPP decisions pertaining to a multimillion dollar IS portfolio, gathered from two business units, that have adopted two distinct IS strategies within a naturally controlled Fortune 50 multibusiness empirical setting. We collected detailed data on all initiatives in the IS portfolio of both these business units, with each initiative characterized by benefit, risk-assessment, and risk-mitigation information attributes. At the end of the ISPP, we gathered data on the final (approve or reject) prioritization decision awarded to each initiative.

Our contributions to the literature are threefold. First, we broaden prior theoretical work on IS strategy types by developing theoretical profiles for the DR used for ISPP in congruence with these IS strategies. This contingency view of IS strategy considered in the context of ISPP is consistent with the view that firms adopting different IS strategies follow correspondingly different DR for ISPP (Chen et al. 2010; Weill and Ross 2004, p. 159). We also articulate the implications of deviations from these theoretical profiles for each IS strategy.

Second, while much of the prior research has centered on the locus of decision making for IS governance (e.g., Sambamurthy and Zmud 1999), we address a key question linking IS governance and ISPP: Why are certain initiatives approved and simultaneously why are certain others rejected? We broaden research on IS governance by maintaining that the IS strategy adopted by firms is likely to explain the DR it uses for ISPP.

Third, our research makes key methodological contributions. DR used for ISPP is often tacit, making it difficult to capture or share (Markus et al. 2002). This difficulty inevitably means that, even when this rationale can be made explicit, it cannot easily be represented numerically, but must instead be represented in terms of if–then decision rules (Baligh et al. 1996; Huber 1981). All information attributes<sup>4</sup> are available to the decision makers, but interconnections among these information attributes that occur during decision making— leading to the formation of decision rules—often remain tacit even to the decision makers themselves. Decision tree induction methodology (DTIM) enables us to codify these tacit interconnections and link these emergent decision rules to final decision outcomes. Thus, we employ a DTIM (Quinlan 1993), which enables us to open up the black box of decision making (Langley et al. 1995) by uncovering tacit interconnections among multiple decision attributes without imposing any ex ante biases on the manner in which these attributes are expected to be associated with decisions. Decisions trees, outcomes of DTIM, are collections of decision rules and are credible approximations of the tacit DR<sup>5</sup> (Huber 1981; Quinlan 1993) used for ISPP. While prior research on IS governance has exclusively focused on approved decisions, we submit that a juxtaposition of the DR used for approving initiatives with the DR used for rejecting other initiatives is likely to deepen our understanding of IS governance.

This paper is organized as follows. The following section integrates existing literature. The subsequent section presents the theoretical logic guiding our propositions. The DTIM is then described, followed by a discussion on the implications of our findings. Finally, we present our concluding remarks.

## Theoretical Background

While assessing the business application needs of IS and ISPP has been suggested to be a critical component of IS governance (Weill and Ross 2004, p. 11), research that examines the DR firms use for ISPP is much needed (Xue et al. 2008). Our framework, which examines DR used for ISPP, is presented in Figure 1 and our theory development effort is summarized in Table 1.

## IS Strategy Types

Recent research that has developed an IS strategy typology by developing profiles of IS conservatives and IS innovators (Chen et al. 2010) serves as our theoretical foundation. IS conservatives adopt a strategy that enables them to reap the benefits of IS by reducing operational inefficiencies. IS innovators adopt a strategy to apply IS in innovative ways to explore new business opportunities. Looking ahead, although profiles of IS strategy types have been developed, theoretical linkages between IS strategy and corresponding profiles of DR used for ISPP need further investigation.

## Decision Rationale

Although prior research has identified information attributes crucial for ISPP, a school of thought maintains that decisions often emerge based on tacit interconnections among information attributes during decision making (Markus et al. 2002).

Interconnections among multiple information attributes converge into patterns as decisions emerge (Mintzberg 1994). Since decision making often involves tacit interconnections among multiple information attributes, a suitable methodology is needed for opening up the black box of decision making (Langley et al. 1995). DTIM is suitable for discovering these tacit interconnections as it does not impose ex ante biases (Quinlan 1990, 1993) on the manner in which information attributes influence decisions. DTIM identifies the most informative attributes for explaining decisions (namely, decision attributes) and excludes all noninformative attributes from the decision tree. Decision trees, outcomes of DTIM, are collections of decision rules generated based on the informative attributes. We employ three heuristics (high prediction accuracy, parsimony, and reliability) to help us select the most credible approximation (decision tree) of the tacit DR (Huber 1981).

## IS Portfolio Prioritization and IS Governance

Although prior research has examined the locus of IS governance decisions and the valuation of IS portfolios, theoretical profiles of DR used for ISPP have not yet been examined. Understanding the DR that firms apply for ISPP is critical as ineffective prioritization is not only likely to be associated with investment in unsuitable IS initiatives, but also associated with firms missing out on IS-enabled strategic business opportunities (Weill and Ross 2004).

We expect a strong link between ISPP and IS governance. One of the key goals of IS governance is to encourage desirable behavior in the prioritization of IS portfolios. Decision rights are central to IS governance and, thus, ensuring that ISPP decisions (approval and rejection decisions on IS initiatives to pursue in the future) are made effectively is critical.

Prior research on IS governance has focused on the locus of decision making by examining the extent to which decision makers share responsibility (Sambamurthy and Zmud 1999). Recently, Xue et al. (2008) incorporated an additional dimension of the timing of IS governance decisions by examining who the key decision makers are and when, at which stages in the IS investment process, are they involved in making decisions? Although existing research (see Table 1) has studied the valuation of portfolios from a real-options perspective (Bardhan et al. 2004; Bardhan et al. 2010; Kauffman and Sougstad 2008; Reyck et al. 2005), the influence of a firm’s IS strategy on the DR it uses for ISPP remains unaddressed.

We examine the link between IS strategy and IS governance by submitting that a firm’s IS strategy is likely to influence the DR it uses for ISPP. We develop theoretical profiles for

![](/api/attachments/MSBGCYRT/fulltext/images/589d20065c9bc557210f748e8d729e794fa41f370b00ca2b18e75729d92e0b5b.jpg)  
Figure 1. Research Framework

<table><tr><td colspan="4">Table 1. Theoretical Development</td></tr><tr><td rowspan="2">Theoretical Building Blocks</td><td colspan="2">Role in Theory Development</td><td rowspan="2">Our Theoretical Rationale</td></tr><tr><td>Existing Research</td><td>Our Research</td></tr><tr><td>Decision Rationale</td><td>Boynton and Zmud 1987Chen et at. 2010Earl 1993Quinlan 1990Segars and Grover 1999</td><td>Develops theoretical profiles of DR based on communicability, consistency and risk appropriateness</td><td>DR is often tacit; DTIM gives us a credible approximation of this tacit DR</td></tr><tr><td>IS Portfolio Prioritization</td><td>Bardhan et al. 2004Bardhan et al. 2010Kauffman and Sougstad 2008Kumar et al. 2008Reyck et al. 2005</td><td>Examines the critical link between ISPP and IS governance</td><td>Provides unique insights for IS Governance by developing DR profiles</td></tr><tr><td>IS Strategy – Decision Rationale Link</td><td>No prior work in IS research.</td><td>Extends work on IS strategies by examining its impact on ISPP DR</td><td>IS Strategy types enable us to develop DR profiles</td></tr></table>

the DR firms used for ISPP by relying on three key attributes that have strong implications for IS governance. First, senior management’s commitment, in terms of their time and attention, is critical for effective prioritization (Rajegopal 2012, pp. 88-90). Thus, communicability of the DR has strong implications for IS governance and effective resource utilization, especially the scarce resource of senior management’s time and attention (Segars and Grover 1999). Next, consistency in applying the DR is important to IS governance as proposals with similar characteristics warrant similar decisions (e.g., Chen et al. 2010). Finally, for effective IS governance, the DR used for ISPP must ensure that an appropriate risk posture is embodied in the firm’s future IS portfolios (Boynton and Zmud 1987).

In summary, we broaden the literature on IS governance by addressing a key question on ISPP: Why are certain initiatives approved and why are certain others rejected? Next, we develop theoretical profiles of DR used for ISPP in congruence with a firm’s IS strategy.

## Research Propositions

## Decision Rationale Profiles

The IS strategy adopted by a firm is likely to exert a strong influence on the DR it uses for ISPP. We identify characteristics that determine the IS strategy of a firm (Chen et al. 2010) and collectively influence its DR. We maintain that DR applied for ISPP is likely to be effective, from an IS governance perspective, when it is easy to communicate, is applied consistently, and is risk-appropriate with respect to the IS strategy of the firm. We rely on three attributes to define theoretical profiles of the DR: (1) communicability of the DR (Segars and Grover 1999), (2) consistency in applying the DR (Chen et al. 2010), and (3) risk appropriateness of the DR (Boynton and Zmud 1987).<sup>6</sup> The three attributes discussed below have been noted to effectively characterize decision processes (Boonstra 2003; Markus et al. 2002) and have strong implications for IS governance.

Communicability: Complexity in decision making is likely to be influenced by the IS strategy of a firm. As the complexity<sup>7</sup> of DR increases, its communicability (the ease with which it can be articulated and shared with others) is likely to suffer. Simple, communicable DR uses scarce resources (senior management’s time and attention) judiciously (Segars and Grover 1999).

Consistency: Decision rules often emerge when informational exchanges between decision makers converge into patterns (Mintzberg 1994), facilitating tacit interconnections among multiple information attributes. Since the tacit DR used for ISPP is typically difficult to capture (Markus et al. 2002), this DR is best represented in the form of if–then decision rules (Huber 1981). Each decision rule explicitly codifies the tacit DR. Some decision rules are used with a higher frequency and are consistently reused to make a larger number of decisions. The frequency with which decision rules are applied (the number of decisions made using the same decision rule) represents the consistency with which the tacit DR is applied for ISPP.

Risk Appropriateness: Different IS strategies represent different risk profiles. Firms that adopt different IS strategies are likely to differ in their risk appetite (Boynton and Zmud 1987; March and Shapira 1987). Given differences in the risk appetites of firms, we propose that a correspondingly different DR is likely to be considered risk appropriate (March 1994), as firms differing in risk appetites are likely to raise/answer different kinds of questions before making ISPP decisions. For a given IS strategy, the DR used for ISPP is risk appropriate if the right kinds of questions, in congruence with the chosen IS strategy, have been raised/answered before approving/ rejecting initiatives. Theoretical profiles for the DR used for ISPP are summarized<sup>8</sup> in Table 2 and theoretical explanations are presented next.

## Decision Rationale for IS Conservatives

IS conservatives focus on improving the efficiency of their internal operations (Chen et al. 2010). IS conservative strategy is associated with three characteristics: (1) a relatively stable external environment, (2) formal decision-making structure, and (3) risk-averse tendencies in the quest for efficiency improvements. We propose that these characteristics are likely to collectively exert a similar influence on DR used by IS conservatives for ISPP. Stability in the external environment coupled with a formal decision-making structure makes it easy for risk-averse IS conservatives to apply DR consistently in a top-down manner.

A stable external environment fosters simplicity in the DR; thus, complexity of the DR used by IS conservatives is likely to be low. IS conservatives adopt a formalized decisionmaking structure (Jansen et al. 2006) to maintain stability (Chen et al. 2010) by applying a simple, highly consistent DR. Acting risk appropriately, decision makers with a lowrisk appetite are likely to approve high-risk initiatives only after ensuring that risk-mitigation mechanisms have been designed to control risks (Boynton and Zmud 1987; Straub and Welke 1998). We investigate the DR tacitly applied for ISPP by relying on DTIM which yields DTs (Column 1 in Table 3<sup>9</sup>). In summary, the easily communicable, highly consistent DR used by IS conservatives for ISPP is likely to focus on the assessment/mitigation of risks.

<table><tr><td colspan="3">Table 2. Theoretical Profiles for IS Portfolio Prioritization Decision Rationale</td></tr><tr><td></td><td>IS Conservative Strategy</td><td>IS Innovator Strategy</td></tr><tr><td>Communicability of Decision Rationale</td><td>High Communicability</td><td>Low-Moderate Communicability</td></tr><tr><td>Consistency in applying Decision Rationale</td><td>High Consistency</td><td>Low-Moderate Consistency</td></tr><tr><td>Risk Appropriateness of Decision Rationale</td><td>Focus on Risk Assessment/Mitigation</td><td>Focus on Exploring Opportunities</td></tr></table>

<table><tr><td></td><td>Column 1: IS Conservatives</td><td>Column 2: IS Innovators</td></tr><tr><td rowspan="2">IllustrativeDecision Tree (DT)</td><td><img src="/api/attachments/MSBGCYRT/fulltext/images/087757954fe9219efcafcab4e713abc2597ee0afa03f9d596fb476feb6565216.jpg"/></td><td><img src="/api/attachments/MSBGCYRT/fulltext/images/8f45028bb7baab85f8744ef25ce171b05a4480bffa5eb40067f2884abfcf5c5c.jpg"/></td></tr><tr><td> $DT_{Conservative}$ </td><td> $DT_{Innovator}$ </td></tr><tr><td>Legend</td><td colspan="2">= Benefit-related information attribute= Risk Assessment/Mitigation-related information attribute= Thicker lines represent decision rules applied to consistently make more decisions</td></tr><tr><td colspan="3">Decision Rationale Profile Attributes</td></tr><tr><td colspan="3">Communicability: Inversely related to complexity of the DT: One key measure of complexity of a DT is the number of decision attributes included in the DT</td></tr><tr><td></td><td>Complexity of  $DT_{Conservative} = 3$ </td><td>Complexity of  $DT_{Innovator} = 6$ </td></tr><tr><td colspan="3">Consistency: Number of decisions made consistently using the same decision rule: Thicker lines represent decision rules consistently applied to make more decisions using the same rule</td></tr><tr><td colspan="3">Risk Appropriateness: Kinds of questions raised/answered: Mix of decision attributes</td></tr><tr><td></td><td>2 of 3 attributes are risk assessment/mitigation attributes</td><td>4 of 6 attributes are benefit-related attributes</td></tr></table>

Proposition 1: The decision rationale used by IS conservatives for IS portfolio prioritization is likely to be easy to communicate, applied with high consistency, and focused on risk assessment/mitigation.

## Decision Rationale for IS Innovators

IS innovators monitor an eclectic array of new opportunities in their dynamic external environment (Chen et al. 2010). IS innovator strategy is associated with three characteristics:

(1) a dynamic external environment, (2) an organic decisionmaking structure, and (3) risk-taking tendencies. IS innovators are expected to enter new markets; therefore, they must quickly adapt to changes in their dynamic external environment since ignoring these changes imposes prohibitively high opportunity costs (Chen et al. 2010, p. 252). Thus, dynamism in the external environment is likely to exert a strong influence on the DR used by IS innovators for ISPP.

IS innovators are expected to continually analyze dynamic information flows in their external environment, which is likely to necessitate a complex DR. To exploit new opportunities, IS innovators are compelled to experiment, and are encouraged to act before engaging in extensive debate and dialogue. Formalized/rigid rules stifle experimentation (Jansen et al. 2006), which is important to IS innovators. To take risks intelligently, IS innovators often develop tacit rules, representing well-designed experiments (March and Shapira 1987), to increase the likelihood of success in exploring new opportunities. However, these tacit rules are likely to be applied less consistently owing to the high dynamism in the external environment.

IS innovators thrive on change in their environment and often create this change by intelligently taking risks. They explore new opportunities by focusing on the potential business value associated with their proposed initiatives, notwithstanding the riskiness of these initiatives. Thus, IS innovators are likely to de-emphasize risk mitigation during ISPP. In summary, DR used by IS innovators is not likely to be easy to communicate, is not likely to be applied with a high consistency, and is likely to be focused on exploring opportunities (Column 2 in Table 3).

Proposition 2: The decision rationale used by IS innovators for IS portfolio prioritization is likely to be focused on exploring opportunities, not easy to communicate, and not applied with high consistency.

## An Empirical Analysis of IS Portfolio Prioritization

We choose a multibusiness firm as our research setting (see our overall data collectoin strategy in Table 4). Business units within our empirical setting pursued different IS strategies along the IS conservative–innovator continuum<sup>10</sup> in congruence with their differing business strategies. IS portfolios of business units at the ends of the IS conservative– innovator continuum are selected for further investigation.<sup>11</sup>

Front-line<sup>12</sup> managers characterized their proposals, business initiatives they submitted for funding, with a rich set of information attributes (see in Table 5). DTIM was applied across data gathered from both business units to discover the DR tacitly applied for ISPP by CIOs and other key decision makers. Since DTIM discovers approximations of the tacitly applied DR, we rely on the best representative DT, a credible approximation of the tacit DR, for each portfolio to examine support for our propositions. The steps in DTIM are outlined next.

## Ascertaining the IS Strategy

To characterize differences in IS strategies adopted by business units at our research site, we adopt recent theoretical research on IS strategy types (Chen et al. 2010). Our research site affords us a naturally controlled empirical setting that enables us to closely examine differences in DR tacitly applied for ISPP across business units, within one Fortune 50 firm, that are pursuing different IS strategies. Data are gathered via various mechanisms to ascertain the IS strategies adopted by these business units.<sup>13</sup>

For effective triangulation (Miles and Huberman 1984), data are collected by the following methods: face-to-face, semistructured, open-ended interviews with key informants (members of the top management team, vice president (VP) and CIO, and multiple senior business executives) spanning more than 20 hours; confidential documents obtained from key informants; observation of ISPP sessions; content analysis of annual reports. The IS strategy of one business unit was classified as an IS conservative whereas the IS strategy of another business unit was classified as an IS Innovator. 14

## Input Portfolio Data

Front-line managers can be a source of new ideas and firms can miss out on numerous IS-enabled business opportunities if they do not listen to their front-line managers (Kohli 2007). On an annual basis, front-line managers at our research site are encouraged to identify new IS-enabled business application areas to pursue in the future. These funding proposals are collected across the two business units and each proposal is described using multiple information attributes. We refer to these data as the input portfolio data. We distinguish between information attributes and decision attributes as follows: Information attributes are inputs to DTIM, and decision attributes, a subset of information attributes, are outputs identified by DTIM. Decision attributes are the most pertinent information attributes for explaining decisions, as identified by DTIM. Data on all information attributes are provided by front-line managers (see Table 5<sup>15</sup>). Input portfolio data were collected by collaborating with the metrics group within the firm. Since these initiatives deal with extensive financial commitments, these data are strictly audited. By focusing on a controlled sample<sup>16</sup> of business applications of IS, we attribute differences in DR used for ISPP to differences in IS strategies of these two business units.

<table><tr><td>Constructs</td><td>Source of Data</td><td>Data Collection Methods</td><td>Validation of Data</td></tr><tr><td>IS Strategy: IS conservative and IS innovator</td><td>VP, CIO, and one senior business executive each from the IS conservative and Innovator business unit</td><td>Open-ended, semi-structured interviews, research collaboration meetings, and immersion sessions with VP and CIO</td><td>VP and CIO validated our classification; data from annual reports provided additional validation</td></tr><tr><td>Input Portfolio Data: Benefits, risk, mitigation attributes</td><td>Front-line managers</td><td>Proposals collected in collaboration with the members of metrics group within the firm</td><td>VP, CIO, and senior executives validated the portfolio data, comprehensiveness of information attributes</td></tr><tr><td>ISPP Decisions: Initiatives rejected or approved</td><td>VP, CIO, and one senior business executive each from the IS conservative and innovator business unit</td><td>Collected from the VP, CIO, and senior business executives at the end of unobtrusive observation sessions of ISPP meetings</td><td>Members of metrics group within the firm validated that the ISPP decisions were recorded correctly</td></tr></table>

<table><tr><td colspan="4">Table 5. Information Attributes for Characterizing Initiatives</td></tr><tr><td></td><td>Information Attribute</td><td>Definition</td><td>Key References</td></tr><tr><td></td><td colspan="3">Benefit information attributes</td></tr><tr><td>1</td><td>Efficiency improvements</td><td>IS that automated manual tasks and business activities</td><td rowspan="5">Aral and Weill 2007; Broadbent et al. 1999; Sabherwal and Chan 2001; Philip 2007</td></tr><tr><td>2</td><td>Inter-organizational process improvements</td><td>IS aimed at improving interorganizational business processes</td></tr><tr><td>3</td><td>Cycle time reductions</td><td>IS aimed at reducing product/service delivery cycle times</td></tr><tr><td>4</td><td>Marketing benefits</td><td>IS that create and promote new products/services</td></tr><tr><td>5</td><td>Strategic benefits</td><td>IS aligned to a firm&#x27;s strategic goals</td></tr><tr><td></td><td colspan="3">Risk-assessment information attributes</td></tr><tr><td>6</td><td>Initiative size</td><td>Firm Thresholds: Low: Size &lt; $100,000 USDMedium: $100,000 &lt; Size &lt; $1,000,000 USDHigh: $1,000,000 USD &lt; Size</td><td rowspan="3">Iversen et al. 2004; Lyytinen et al. 1995; McFarlan 1981; Nolan and McFarlan 2005</td></tr><tr><td>7</td><td>Initiative structure</td><td>Low: Lack of clearly defined objectivesHigh: Well-defined objectives</td></tr><tr><td>8</td><td>Prior experience</td><td>Low: Technologies not familiar to firmMedium: Technologies moderately familiarHigh: Standard technologies familiar to firm</td></tr><tr><td></td><td colspan="3">Risk-mitigation information attributes</td></tr><tr><td></td><td colspan="3">Internal Risk Mitigation Mechanisms</td></tr><tr><td>9</td><td>Employ in-house software</td><td>Software application developed internally by the firm</td><td>Earl 1993; Mitchell and Zmud 2006</td></tr><tr><td>10</td><td>Internal maturity</td><td>Low: Idea in early stages of developmentMedium: Goals/requirements are clearly definedHigh: Controls envisioned/put in place across life cycle stages of this mature initiative</td><td>Boonstra 2003; Ramasubbu et al. 2008</td></tr><tr><td></td><td colspan="3">Process Risk Mitigation Mechanisms</td></tr><tr><td>11</td><td>Business process redesign completed</td><td>Process redesign completed and controls indicated</td><td>Broadbent et al. 1999</td></tr><tr><td>12</td><td>Resources for process redesign committed</td><td>Process redesign resources identified and assigned</td><td>Lambert 1986</td></tr><tr><td></td><td colspan="3">External Risk Mitigation Mechanisms</td></tr><tr><td>13</td><td>Employ consultant knowledge</td><td>Initiative involved leveraging capabilities of integration partners and/or external consultants</td><td>Ko et al. 2005; Susarla et al. 2010</td></tr><tr><td>14</td><td>Utilize specialized software applications</td><td>Initiative involved procurement of specialized software applications</td><td rowspan="2">McFarlan 1981; Nolan and McFarlan 2005</td></tr><tr><td>15</td><td>Leverage third-party solutions</td><td>Initiative supported by third party software building blocks</td></tr></table>

## Input Portfolio Data

Three types of information attributes (Boynton and Zmud 1987; McFarlan 1981; Sabherwal and Chan 2001) used to richly describe business initiatives are analyzed in this study. First, the CIO and other key business leaders seek a rich description of initiatives in terms of potential benefits they can offer. Such a description helps these decision makers to gauge the business value associated with these initiatives and enables them to identify promising initiatives to pursue (Aral and Weill 2007). Second, since ISPP involves the selection of initiatives to pursue in the future, ISPP requires managing risks. Thus, assessment of risks associated with proposed initiatives in the portfolio is an integral component of ISPP. Third, risk mitigation is a critical component of IS governance (Nolan and McFarlan 2005) and thus decision makers at our research site demanded data on risk-mitigation mechanisms designed by front-line managers to control risks associated with their proposals (March and Shapira 1987). Managers can either exert additional effort or gather additional information to control risks associated with their proposals (Lambert 1986). Thus, these three types of attributes are pertinent for ISPP and essential for effective IS governance (Maizlish and Handler 2005). Descriptions of the 15 information attributes used by front-line managers to characterize their proposed initiatives are presented next.

Benefit information attributes: Based on the information on proposed initiatives prepared by front-line managers, we create a total of five variables to capture the different types of benefits, these business applications of IS can offer. Insights from prior research (Aral and Weill 2007; Broadbent et al. 1999; Sabherwal and Chan 2001) guided these transformations. For all benefit-related variables, the inter-rater reliability was over 95 percent.<sup>17</sup> Our characterizations of benefits are validated for us not only by the front-line managers proposing the initiatives, but also decision makers responsible for ISPP.

Risk-assessment information attributes: Risk assessment is critical for ISPP (Nolan and McFarlan 2005). Based on suggestions from prior work (Lyytinen et al. 1995), measures from McFarlan (1981) are used to assess risks associated with initiatives in our data.<sup>18</sup>

Risk-mitigation information attributes: Risk-mitigation mechanisms are critical for the successful implementation of IS-enabled business initiatives (Broadbent et al. 1999; Piccoli and Ives 2005; Ramasubbu et al. 2008; Straub and Welke 1998). We rely on three categories of risk-mitigation mechanisms (Iversen et al. 2004; Nolan and McFarlan 2005; Sherer and Alter 2004), namely internal, external, and process riskmitigation mechanisms. The comprehensiveness and effectiveness of these risk-assessment and risk-mitigation mechanisms is validated for us by the front-line managers and the key decision makers at our research site.

## IS Portfolio Prioritization Decisions

For each proposed initiative, ISPP decisions are made by a steering committee comprising of the VP, the CIO, and senior business executives responsible for IS governance. Decisions for an initiative could either be a rejection or an approval. At the end of ISPP, we gather these decision data from these decision makers. The decision makers at our research site were fairly certain that they had effectively addressed the risks associated with the funding proposals and had selected a promising set of initiatives to pursue in the future. Decision makers at the research site validated for us that the ISPP was effective. In summary, data on all the information attributes pertaining to the input portfolio, prepared by front-line managers, are collected in collaboration with the metrics group within the firm (see Table 5<sup>19</sup>) and final decisions on these proposed initiatives are independently gathered from the VP, CIO, and senior business executives responsible for IS Governance. This independence limits the extent to which our study suffers from the common methods bias.

## Decision Tree Induction Methodology

DTIM (Quinlan 1993) enables us to open up the black box of decision making ( Langley et al 1995) and empowers us to discover the underlying, tacit DR applied during ISPP, which can often be unknown to the decision makers themselves. This is particularly true when decisions emerge based on interactions between groups of decision makers. DTIM iteratively groups together observations (i.e., initiatives) such that they are similar not only in certain information attributes but also in their final decision outcomes. There are two key inputs to DTIM: (1) a set of initiatives described by all the 15 information attributes, and (2) the final decisions made on these initiatives.

The objective of DTIM is to discover tacit combinations of information attributes associated with similar final decisions (Quinlan 1990, 1993). The output of DTIM is a DT which only retains the most pertinent information attributes (i.e., decision attributes) for explaining decisions. DTIM organizes attributes in a context-dependent manner; certain questions are only raised depending on answers obtained to other questions answered previously (Quinlan 1990).

We would like to clarify that DTs discovered by DTIM are not reflective of the exact rules or the “script” used by the decision makers during ISPP, but rather, are approximations<sup>20</sup> of the tacit underlying DR. DTIM utilizes the most informative attributes to construct the DT. Instead of the correlations between information attributes, DTIM relies on the amount of information a particular attribute conveys about the final decision. Thus, we do not report correlations between information attributes, but rather present the relationship between each information attribute and the final decision (see the fourth section of Appendix C).

## Credible Approximations of Decision Rationale

To ensure that DR is comprehensively discovered from all the initiatives in the input portfolio, a process of drawing bootstrapped, mutually exclusive, training and testing subsamples is repeated multiple times. An iteration of DTIM is described next. In each iteration (shown as artifact DTI in the Figure 2), we draw two random, mutually exclusive subsamples of initiatives from the original portfolio; one set, known as the training set (Step A1 in Figure 2), from which the tacit DR is discovered (Step B in Figure 2 and elaborated on in the next section) by the DTI algorithm (Quinlan 1986), and another disjoint set of initiatives, known as the testing set (Step A2 in Figure 2), which is used to test the predictive accuracy of this discovered DR.<sup>21</sup>

Specifically, a randomly drawn sample of 80 percent of the portfolio was used for training and the prediction accuracy of the discovered DR was tested on a disjoint randomly drawn sample of 20 percent of the total portfolio. Prediction accuracy of the DT discovered from the training set is assessed by applying the DT to predict (Step C in Figure 2) decisions for initiatives in the mutually disjoint testing set.

Multiple such iterations are performed on 80/20 training/ testing sample splits to yield multiple plausible DR approximations (trees). Parsimonious DTs are preferable as they compactly articulate the discovered tacit DR. Further, for robustness, a similar analysis is conducted using other training/testing subsample splits. These multiple iterations help us judge the robustness of the discovered tacit DR. In the next section, we describe the DTI algorithm in detail and follow it with a discussion of the heuristics used to determine the best representative DT from the multiple approximations generated by the DTI algorithm.

## Discovering the Most Informative Attributes

The theoretical basis for inducing DTs on a portfolio of decisions, each of them described by a set of information attributes and final decisions, is summarized as follows (Quinlan 1986,1990; Tessmer et al. 1993). This procedure recursively partitions the sample into smaller subsets, in step with the growth of the DT. DTIM (see Figures 2 and 3) chooses the most pertinent information attribute on which to split the training sample and thus which attributes will be included in the DT (i.e., decision attributes) and is driven by the information-theoretic justification presented below.

![](/api/attachments/MSBGCYRT/fulltext/images/1d3bd61b0371a5263d592fd1eae78cfac25ed32307599803a617013c97708d52.jpg)  
Figure 2. Decision Tree Induction Methodology

## If

-- all decisions belong to a single class (e.g., are all accept/reject decisions, the tree is a leaf labeled with that class

Otherwise,

-- select a test, based on an information attribute, with mutually exclusive outcomes;

-- divide the sample into subsets, each corresponding to one value of the information attribute;

Repeat the same procedure with each subset.

Figure 3. Decision Tree Induction Algorithm

The concept of information entropy (Shannon and Weaver 1963) serves as the theoretical basis for determining which attributes to include in the DT.

The amount of information (or the reduction in uncertainty) provided by the information attribute is the primary justification for classifying the examples and only the most informative attributes are included in the DT. The entropy or uncertainty is equal to 0 if and only if all the $p _ { i }$ ’s but one are equal to 0. The entropy is maximum when all the $\boldsymbol { p } _ { i } ^ { \ \prime } { \bf s }$ are equal; that is, when all alternatives are equally likely. Any change toward an even distribution of $\boldsymbol { p } _ { i } ^ { \ \prime } { \bf s }$ increases the entropy but as soon as one of the alternatives become more probable than others, the entropy decreases. All the DTs are induced by using the most widely used C4.5 algorithm<sup>22</sup> (Quinlan 1986, 1990). This algorithm builds DTs from a dataset using information entropy and information gain ratio for choosing which information attributes are included in the DT (Quinlan 1993). DTs are induced using the open source, software DTIM platform called Weka (Hall et al. 2009).

## Three Heuristics for Selecting the Best Representative Decision Tree

Multiple approximations of the underlying, tacit DR are derived by repeating the process of drawing two mutually disjoint training/testing subsamples of differing sizes. This repetition is integral to DTIM to ensure that multiple approximations of the underlying DR are available to the researchers. Given these multiple approximations, we systematically rely on three heuristics to select the best representative approximation, a credible approximation, of the underlying DR.

1. High predictive accuracy: Prediction accuracy of DTs induced on a subset of training data is tested on a mutually disjoint testing data set. This heuristic represents a goodness-of-fit measure for the DT induced on the training dataset in terms of predicting decisions from unseen data, namely from the mutually disjoint testing subsample.

2. High parsimony: The induced DT is expected to be a compact, parsimonious approximation of the underlying, tacit DR so that it can serve as an effective decisionmaking aid.

3. High reliability: Since the process of drawing training samples to induce DTs and testing the predictive accuracy of induced DTs on mutually disjoint testing samples is repeated several times, we are able to assess the robustness of the induced DT. For instance, DTs with the same top-most attribute, showing up reliably across these multiple iterations, represent a robust approximation of the underlying DR. We are, thus, fairly certain that the DTs presented in this research are credible approximations of the underlying, tacit DR applied for ISPP. The best representative DTs for IS conservative and IS innovator are presented in Figures 4 and 5.

## Interpreting a Decision Tree

We would like to reiterate that the DTs presented here were discovered by DTIM as approximations of the tacit DR applied for ISPP. These DTs do not represent the exact rules or the script that decision makers were following for ISPP. Since we employ three heuristics (high prediction accuracy, parsimony, and reliability) to choose a best representative DT, we are fairly certain the DTs that we present here represent credible approximations<sup>23</sup> of the tacit DR.

All 15 information attributes characterizing initiatives (see Table 5) in conjunction with the final decision, are inputs to DTIM. All information attributes discovered by DTIM to be most informative for explaining decisions are included in the DTs as decision attributes and DTIM excludes all the noninformative attributes from the DT. The most informative decision attribute is the top-most attribute in the DT. Importance of attributes decreases as we move away from the top of the DT to the leaves, namely the endpoints of the DT. DTIM organizes attributes in a context-dependent manner; certain questions are raised depending on answers obtained to questions answered previously (Quinlan 1990).

Next, we summarize the operationalization details for three attributes that define the DR profile: (1) communicability of the DR, (2) consistency in applying the DR, and (3) risk appropriateness of the DR. Communicability of the DR is inversely related to the complexity of the DT. Number of decision attributes included in the DT is an effective proxy of the complexity of the DR. Highest proportion of decisions made by tacitly applying the same decision rule represents the consistency in applying the DR. As this proportion increases, it informs us that the same rule was consistently applied to decide upon a large number of distinct initiatives. Finally, we assess the risk appropriateness of the DR by counting the number and kinds of decision attributes included in the DT across the three categories identified in Table 5: benefits, risk assessment, and risk mitigation attributes. A higher proportion of risk assessment and/or mitigation attributes in the DT represents a focus on risk assessment/mitigation, as opposed to a focus on exploring new business opportunities.

## Discussion of Results and Implications

## IS Strategy Types and Best Representative Decision Trees

## IS Conservative’s Decision Tree

The number of decision attributes included in the DT, as a proportion of the total number of 15 information attributes provided as inputs to DTIM, serves as an effective proxy for the complexity, which is inversely related to the communicability, of the tacitly applied DR. Of the 15 information attributes provided as inputs, the DR tacitly applied by the IS conservative for ISPP is best<sup>24</sup> represented using only five (5/15 = 33%) attributes (see Figure 4). This simple DT easily communicates the DR tacitly applied for ISPP. The IS conservative’s DR contains a decision rule consistently applied with a very high frequency. In all, 63 percent of the decisions for the IS conservative’s portfolio are explained by the application of just this one main<sup>25</sup> decision rule. In other words, we observe that the IS conservative’s DR comprises of a simple, highly consistent line of reasoning. IS conservative’s DT includes only 1 benefit attribute and 2 decision attributes each for assessing and mitigating risks.

![](/api/attachments/MSBGCYRT/fulltext/images/617d9e87427dce2f41096aaf114a885bbdbfbf162df207468eb48f3141ca68bc.jpg)  
Figure 4. IS Conservative’s Decision Tree

![](/api/attachments/MSBGCYRT/fulltext/images/53b1892b256ca0c50afb04a13cafa591db920a94657a630b59d9e3ed06ff29c7.jpg)

When deciding on the IS conservative’s portfolio, decision makers seem to rely on a higher proportion (4/5 = 80%) of risk assessment/mitigation decision attributes. Thus, the IS conservative’s DR is highly consistent, easily communicable, and focuses on assessment/mitigation of risks. Our findings support Proposition 1.

Additionally, the IS conservative’s DT reveals that certain medium-sized initiatives that do not offer cycle time reductions are approved and similar small-sized initiatives are rejected. Collectively, these decisions seem rationally unjustifiable. Alhough we do not investigate the political aspects of the DR in this study, DTIM empowers us to identify instances of rationally unjustifiable decisions. These decisions might be politically motivated, thus DTIM can serve as a starting point for scholars interested in investigating politically driven decision making.

## IS Innovator’s Decision Tree

Of the 15 information attributes provided as inputs, DTIM discovered that the DR tacitly applied by the IS innovator (see Figure 5) for ISPP was best<sup>26</sup> represented by six decision attributes. A total of 40 percent (6/15 = 40%) of the information attributes are needed to communicate the IS innovator’s DR, implying that this rationale is not very simple. Only 40 percent of the decisions in the IS innovator portfolio are explained by the use of the most consistent decision rule<sup>27</sup> (see Figure 5). The proportion of decisions made most con-

<table><tr><td colspan="3">Table 6. Summary of Findings</td></tr><tr><td></td><td>IS Conservative Strategy</td><td>IS Innovator Strategy</td></tr><tr><td colspan="3">Decision Rationale Profile Attributes</td></tr><tr><td colspan="3">Communicability: Inversely related to complexity of DT: Total Number of attributes provided as inputs to the decision iree induction methodology = 15</td></tr><tr><td>Measures of Complexity{Number of Decision Attributes, Number of attributes in the Longest Decision Rule,Total Number of Leaves}</td><td>{5,4,7}</td><td>{6, 6, 7}</td></tr><tr><td>Proportion of decision attributes included</td><td>5/15 = 33%</td><td>6/15 = 40%</td></tr><tr><td colspan="3">Consistency: Proportion of distinct initiatives decided upon using the same rule</td></tr><tr><td></td><td>63% of distinct decisions made using one decision rule</td><td>40% of distinct decisions made using one decision rule</td></tr><tr><td colspan="3">Risk Appropriateness: Focus during decision making</td></tr><tr><td>Proportion of risk assessment and mitigation attributes included</td><td>80% (4 of total 5 attributes are risk assessment/mitigation attributes)</td><td>50% (3 of total 6 attributes are risk assessment/mitigation attributes)</td></tr><tr><td colspan="3">Decision Rationale Profile</td></tr><tr><td colspan="3">DR Profile = {Proportion of Information Attributes Retained as Decision Attributes, Proportion of distinct decisions made using one decision rule, Proportion of Risk Assessment/Mitigation Attributes in the DT}</td></tr><tr><td>Observed Profile</td><td>{33%, 63%, 80%}={High Communicability , High Consistency, Focus on Risk Mitigation}</td><td>{40%,40%,50%}={Low-Moderate Communicability, Low-Moderate Consistency, Focus on Exploring Opportunities}</td></tr></table>

sistently using just one decision rule was lower than the proportion that was observed in the IS conservative’s portfolio. The IS innovator’s DT includes three benefits attributes, one attribute for risk assessment, and two decision attributes for risk mitigation.

When prioritizing the IS innovator portfolio, decision makers seem to rely on a higher proportion (that is, 50%) of benefitrelated decision attributes implying a focus on exploring opportunities. In summary, the IS innovator’s DR is not necessarily easy to communicate, does not apply a decision rule with high consistency, and focuses on exploring opportunities. Our findings support Proposition 2. A summary of our findings is presented in Table 6.

## Theoretical Implications

One of the key goals of IS governance is to encourage desirable behavior in the prioritization of IS portfolios. Thus, our research, which examines DR used for ISPP, has strong implications for IS governance. Next, we present these implications from our research for IS governance.

First, although prior research has provided extensive insights on the locus (centralization and/or decentralization) of the decision making for IS governance, questions pertaining to why firms make ISPP decisions have been left unanswered. Our study is one of the first to empirically examine the relationship between ISPP decisions (namely, approval and rejection decisions on IS-enabled business initiatives to pursue for the future) and the IS strategy of the firm, which is critical for IS governance.

Second, our research proposes that the IS strategy of a firm<sup>28</sup> is likely to be a key antecedent in explaining the DR it applies for prioritizing its IS portfolios. We submit that congruence between a firm’s IS strategy and its ISPP DR is likely to be associated with effectively planned IS portfolios as it not only incentivizes managers to develop the right kinds of initiatives but also guides decision makers to approve the right kinds of initiatives for future implementation. We map DR profiles for strategies along the IS conservative–innovator continuum in Figure 6.

![](/api/attachments/MSBGCYRT/fulltext/images/0bdfce2fa7f74393309f170395a9eab756130acb9875021eb529c9ebe4378442.jpg)  
Figure 6. Mapping Decision Rationale Profiles

Third, while existing research has examined IS strategies by analyzing variations in the composition of IS application portfolios (Sabherwal and Chan 2001), we broaden this important body of work by investigating the theoretical properties of DR applied during ISPP. We contribute to the literature on IS governance by addressing a key question on ISPP: Why are certain initiatives approved and simultaneously why are certain others rejected? We do so by developing theoretical profiles of the ISPP DR by encompassing three dimensions: communicability of DR, consistency in applying DR, and risk appropriateness of DR. We submit that understanding theoretical DR profiles across differing IS strategies strongly complements extant IS governance research by explicitly examining if the right kinds of questions are raised during ISPP. Thus, we present theoretical properties of the DR which can encourage rulefollowing in congruence with a firm’s IS strategy. We adopt a portfolio-level unit of analysis to contribute insights on the means firms adopt to effectively prioritize their IS portfolios.

## Extensions

We extended research on IS conservative–innovator strategy by proposing DR profiles for ISPP, in congruence with these

IS strategies. Analysis of our data yielded support for our propositions. Building on this foundation, we identify two extensions for future research.

## Egregious Deviations from Theoretical Decision Rationale Profiles

Deviations<sup>29</sup> from the theoretical DR profile applied by firms who have adopted strategies along the IS conservative– innovator continuum is likely to be associated with ineffective ISPP (Segars and Grover 1999) for at least three reasons.

First, for IS conservatives, a complex DR is indicative of an unnecessarily complex decision process that is inefficiently consuming resources such as executive time and attention. In contrast, an overly simple DR for an IS innovator is indicative of a decision process that is not sufficiently responsive to information flows in the IS innovator’s dynamic external environment.

Second, a low consistency in the DR applied by an IS conservative is likely to indicate that similar initiatives are being awarded different decisions, which would be unsuitable from an IS governance perspective. Favoritism could be one underlying explanation for why similar initiatives might inconsistently be awarded different ISPP decisions. This would be ineffective from an IS governance perspective as it would mean that front-line managers whose proposals are being rejected are being given no credible feedback for improving their proposals. This outcome of the ISPP represents a major loss of learning opportunities for front-line managers. Very high consistency in the DR applied by an IS innovator is indicative of an rigid decision process, unsuitable to IS innovators whose decision making is expected to be organic, in response to the dynamism of its external environment.

Third, a misguided focus during ISPP, revealed by an inappropriate mix of decision attributes in the DTs, would be indicative of two crucial deficiencies. A misguided focus during ISPP is likely to suggest that unsuitable initiatives are being approved and/or unsuitable initiatives are not being rejected. Deviations along this dimension could result in an IS conservative’s portfolio that is incongruently focused on exploring opportunities, which is indicative of the IS conservative taking on unjustifiable risks. Along similar lines, an IS innovator’s misguided focus on risk mitigation, would be indicative of missed opportunities.

Thus, deviations along any of the three dimensions defining the theoretical DR profile, is likely to be detrimental to ISPP and IS governance.

Proposition 1 for Future Research: Deviation between the decision rationale applied by firms adopting strategies along the IS conservative– innovator continuum and the theoretical decision rationale profile, is likely to be associated with ineffective IS portfolio prioritization.

## Mediating Role of the Decision Rationale Profile

Prior research maintains that a chosen IS strategic posture or digital business strategy is an antecedent of firm-level outcomes (Mithas et al. 2013). Our results highlight an intervening theoretical mechanism, namely DR applied by firms for ISPP, which is likely to have a strong impact on firm-level performance outcomes. This revised articulation sheds light on the mediating influence of the DR applied for ISPP for two reasons, which we elaborate next.

First, congruence between a firm’s IS strategy and the DR it uses for prioritizing its IS portfolio fosters a rule-based approach to portfolio prioritization which provides front-line managers with the right incentives to design suitable ISenabled initiatives and disincentivizes (rule-defiant) behavior (e.g., Prendergast 1999). Incentivizing managers is critical for effective ISPP and eventually the superior business value of IS (Kohli and Grover 2008). Second, congruence between DR employed by firms during ISPP and their IS strategies is likely to ensure the suitable initiatives are approved for future implementation and the unsuitable initiatives are weeded out earlier in the prioritization stages. Often, unsuitable choices made early during strategic IS portfolio planning are costly to correct later during plan implementation. Thus, we maintain that the DR used during prioritization has a strong bearing on the implementation of planned IS portfolios, which eventually influences the business value realized from these portfolios. Incorporating this new theoretical construct into the business value of IT research (e.g., Kohli and Grover 2008) would require scholars to carefully choose a unit of analysis suitable for evaluating the true impact of ISPP DR on the business value realized from IS strategies.

Proposition 2 for Future Research: Decision rationale profile is likely to mediate the relationship between planned IS strategies along the IS conservative–innovator continuum and the business value realized from these investments.

## Managerial Implications of Our Results

DTs open up the black box of IS decision making by codifying the tacit DR applied during ISPP in a manner that can easily be scrutinized by decision makers. Our findings enable us to develop recommendations for assisting CIOs in managing their IS portfolios (Maizlish and Handler 2005). The first three steps we outline next (see Table 7) follow from our research design whereas the latter three follow from our findings.

Identify initiatives in distinct portfolios: Although DR for prioritizing distinct portfolios (IT hardware/infrastructure portfolios versus IS portfolios) is likely to be different, we propose that to govern these portfolios effectively, it is critical for CIOs to catalogue all initiatives in these portfolios (Kumar et al. 2008). Identifying initiatives in distinct portfolios enables CIOs to govern them effectively, as they can systematically track the progress of all their portfolios.

<table><tr><td>Portfolio Management Lifecycle</td><td>Key Recommendations</td></tr><tr><td>Identify initiatives in distinct portfolios</td><td>Maintain distinct portfolios in hardware (infrastructure) and software (business applications of IS)</td></tr><tr><td>Gather portfolio data</td><td>Define initiatives in a portfolio in an information-rich manner</td></tr><tr><td>Define the decision schemes</td><td>Select decision schemes suitable to the firm strategic objectives</td></tr><tr><td>Develop a repository of decision rules</td><td>CIOs need to articulate their decision rules; DTs we present in our research could serve as a starting point</td></tr><tr><td>Apply decision rules</td><td>Determine nonnegotiable decision rules to apply and identify means to deal with exceptions.</td></tr><tr><td>Manage portfolio lifecycles</td><td>Identify opportunities for continual refinements for IS portfolio management capabilities</td></tr></table>

Gather portfolio data: Information attributes used to describe initiatives must be consistently used across all initiatives within a portfolio. Ideally, initiatives need to be described in adequate detail to assist CIOs to make well-informed decisions. At the same time, providing too much information can be overwhelming to CIOs, ultimately proving to be counterproductive.

Define the decision scheme: For some portfolios, a binary (yes/no) decision scheme might be suitable whereas other instances might necessitate an additional partial funding decision outcome. For instance, binary decisions can be simplistic to administer but can create divisive, disincentivizing rifts between managers within a firm. Thus, the implications of choosing between different decision schemes need to be systematically evaluated.

Develop a repository of decision rules: CIOs need to articulate their DR in the form of decision rules. These rules capture the decision attribute(s) that guide CIOs to either approve or reject initiatives within a portfolio. DR typically taps into vast amounts of tacit, prior experience that enables CIOs to identify combinations of attributes that describe initiatives they believe are likely to be successful. Decision rules codify tacit DR in the form of if–then–else statements.

In other words, decision rules can tie information attributes to the decision outcomes. As various decision makers articulate their individual DRs in the form of rules, to the extent possible, they develop a repository of decision rules. More importantly, decision makers can compare their DRs, understand the point of view of others, and eventually agree upon decision rules to apply during ISPP. Such collective exercises can enable decision makers to arrive at a set of rules that are collectively deemed nonnegotiable. Ideally, decision makers need to arrive at a consensus on nonnegotiable decision rules to apply before they start prioritizing IS portfolios. DTs we present in our study can serve as a starting point in assisting

CIOs, adopting different kinds of IS strategies, in developing a repository of decision rules.

Although codification of tacit DR is likely to assist decision makers responsible for ISPP, there are often darker consequences to openly sharing all these rules. For instance, if all rules are made explicit, then managers proposing initiatives are likely to game the system by designing initiatives to only comply with these codified approval rules. CIOs should exercise caution in sharing their rules with managers responsible for proposing new initiatives.

Apply decision rules: Having reached a consensus on the repository of nonnegotiable decision rules to apply, interactions between CIOs and front-line managers proposing initiatives during ISPP are likely to be more efficient and fair. To the extent possible, CIOs can consistently apply the repository of nonnegotiable decision rules to prioritize their portfolios. A repository of explicit decision rules can also enable CIOs to systematically handle exceptions to rules. We propose that a rule-based approach to ISPP improves the transparency of decision making and enables CIOs to incentivize front-line managers to continually improve their initiatives.

Manage portfolio lifecycles: CIOs should strive to improve the consistency of their decision making, to the extent possible, and educate front-line managers to develop better initiatives. As portfolio decisions are implemented over time, additional data on the performance of approved initiatives can become available to CIOs. This performance data could guide future decisions but should be used with caution. If approved initiatives are not eventually successful, the associated penalties should not be too severe or else managers hoping for funding will, in future, only craft conservative initiatives. Such a systematic conservative bias is likely to prevent managers from realizing the true potential of IS. On the other hand, if there are no penalties associated with failed initiatives, managers might not cultivate any discipline and are likely to continue to craft grandiose initiatives without exerting effort to manage risks. Thus, CIOs need to appraise the performance of approved initiatives, but leverage this performance data judiciously.

## Concluding Remarks

## Limitations

Our study has certain limitations. First, our data are obtained from two business units within one large Fortune 50 firm. This could imply that our work suffers from limited generalizability. To address this limitation, we integrate three attributes (communicability of DR, consistency in applying DR, and risk appropriateness of D) for developing theoretical profiles of DR tacitly applied during ISPP. Our research enables us to theorize the linkages between the IS strategy adopted by firms and the corresponding DR applied during ISPP. Insights from our research are thus likely to be applicable to firms that can be characterized using the IS conservative–innovator typology. Second, while the categories and specific anchors used as information attributes in this study (see Table 5) were validated for their comprehensiveness at our research site, we acknowledge that investigations at other firms might require refinements to these information attributes. Information attributes used to characterize initiatives in our data can serve as a starting point in guiding other scholars who wish to build on our research.

The limitations identified above, meanwhile, do offer other advantages. Our research allows us to test differences in DR across two business units pursuing different IS strategies within a naturally controlled empirical setting. In line with suggestions from prior research (Sabherwal and Chan 2001), we examine one kind of portfolio, namely business applications of IS, and this focus enables us to control for confounding factors pertinent to other kinds of IS portfolios.

## Conclusion

In this paper, we submit that the IS strategy of a firm is likely to explain its ISPP DR. We examine differences in the ISPP DR across different IS strategy types. We develop theoretical profiles of DR used for ISPP by relying on three attributes: communicability of DR, consistency in applying DR, and the risk appropriateness of DR. Since DR applied during ISPP is often tacit, unknown even to the decision makers themselves, we adopt DTIM, which is appropriate for discovering this tacit DR. By analyzing over 150 actual ISPP decisions, we find support for our theoretical DR profiles. Implications for IS governance practices are developed.

## Acknowledgments

We are grateful to senior executives and managers at the research site for assistance with this project. We acknowledge financial support from The Hong Kong University of Science and Technology, University of Illinois, and the Leonard C. and Mary Lou Hoeft endowment at the University of Illinois. We would like to thank John Burke, Wooje Cho, Joe Mahoney, Arun Rai, and seminar participants at The City University of Hong Kong and Seoul National University for their helpful comments on this paper. We would also like to thank the senior editor, Rajiv Kohli, the associate editor, Paul Pavlou, and the three reviewers for their helpful comments and excellent suggestions. The usual disclaimer applies.

## References

Aral, S., and Weill, P. 2007. “IS Assets, Organizational Capabilities, and Firm Performance: How Resource Allocations and Organizational Differences Explain Performance Variation,” Organization Science (18:5), pp. 763-780.

Baligh, H. H., Burton, R. M., and Obel, B. 1996. “Organizational Consultant: Creating a Useable Theory for Organizational Design,” Management Science (42:12), pp. 1648-1662.

Bardhan, I., Baghchi, S., and Sougstad, R. 2004. “Prioritizing a Portfolio of Information Technology Investment Projects,” Journal of Management Information Systems (21:2), pp. 33-60.

Bardhan, I. R., Kauffman, R. J., and Naranpanawe, S. 2010. “IT Project Portfolio Optimization: A Risk Management Approach to Software Development Governance,” IBM Journal of Research and Development (54:2), pp. 2-1.

Boonstra A. 2003. “Structure and Analysis of IS Decision-Making Processes,” European Journal of Information Systems (12:3), pp. 195-209.

Boynton, A. C., and Zmud, R. W. 1987. “Information Technology Planning in the 1990’s: Directions for Practice and Research” MIS Quarterly (11:1), pp. 59-71.

Broadbent, M., Weill, P., Clair, D. S., and Kearney, A. T. 1999. “The Implications of Information Technology Infrastructure for Business Process Redesign,” MIS Quarterly (23:2), pp. 159-182.

Brown, C. V. 1997. “Examining the Emergence of Hybrid IS Governance Solutions: Evidence from a Single Case Site,” Information Systems Research (8:1), pp. 69-94.

Chen, D., Preston, D. S., Mockler, M., and Teubner, A. 2010. “Information Systems Strategy: Reconceptualization, Measurement, and Implications,” MIS Quarterly (34:2), pp. 233-259.

Drazen, R., and Van de Ven, A. 1985. “Alternative Forms of Fit in Contingency Theory,” Administrative Science Quarterly (30), pp. 514-539.

Earl, M. J. 1989. Management Strategies for Information Technology, Englewood Cliffs, NJ: Prentice-Hall.

Earl, M. J. 1993. “Experiences in Strategic Information Systems Planning,” MIS Quarterly (17:1), pp. 1-24.

Eisenhardt, K. M., and Bourgeois, L. J. 1988. “Politics of Strategic Decision Making in High-Velocity Environments: Toward a Midrange Theory,” Academy of Management Journal (31:4), pp. 737-770.

Hall, M., Frank, E., Holmes, G., Pfahringer, B., Reutemann, P., and Witten, I. H. 2009. “The WEKA Data Mining Software: An Update,” ACM SIGKDD Explorations Newsletter (11:1), pp. 10-18.

Huber G. P. 1981. “Organizational Decision Making and the Design of Decision Support Systems,” MIS Quarterly (5:2), pp. 1-10.

Iversen, J. H., Mathiassen, L., and Nielsen, P. A. 2004. “Managing Risk in Software Process Improvement: An Action Research Approach,” MIS Quarterly (28:3), pp. 395-433.

Jeffery, M., and Leliveld, I. 2004. “Best Practices in IS Portfolio Management,” Sloan Management Review (45:3), pp. 41-49.

Jansen, J. J. P., Van Den Bosch, F. A. J., and Volberda, H. W. 2006. “Exploratory Innovation, Exploitative Innovation, and Performance: Effects of Organizational Antecedents and Environmental Moderators,” Management Science (52:11), pp. 1661-1674.

Kauffman, R. J., and Sougstad, R. 2008. “Risk Management of Contract Portfolios in IT Services: The Profit-at-Risk Approach.” Journal of Management Information Systems (25:1), pp. 17-48.

Ko, K., Kirsch, L. J., and King, W. R. 2005. “Antecedents of Knowledge Transfer from Consultants to Clients in Enterprise System Implementations,” MIS Quarterly (29:1), pp. 59-85.

Kohli, R. 2007. “Innovating to Create IS-Based New Business Opportunities at United Parcel Service,” MIS Quarterly Executive (6:4), pp. 199-210.

Kohli, R., and Grover, V. 2008. “Business Value of IT: An Essay on Expanding Research Directions to Keep Up with the Times,” Journal of the Association for Information Systems (9:1), pp. 23-39.

Kumar, R., Ajjan, H., and Niu, Y. 2008. “Information Technology Portfolio Management: Literature Review, Framework, and Research Issues,” Information Resources Management Journal (21:3), pp. 64-87.

Langley, A., Mintzberg, H.,Pitcher, P. Posada, E., Saint-Macary, J. 1995. “Opening Up Decision Making: The View from the Black Stool,” Organization Science (6:3), pp. 260-279.

Lambert, R. A. 1986. “Executive Effort and Selection of Risky Projects,” RAND Journal of Economics (17:1), pp. 77-88.

Lyytinen K., Mathiassen L., and Ropponen J., 1998. “Attention Shaping and Software Risk: A Categorical Analysis of Four Classical Approaches,” Information Systems Research (9:3), pp. 233-255.

Maizlish, B., and Handler, R. 2005. IS Portfolio Management: Unlocking the Business Value of Technology, New York: John Wiley & Sons.

Markus, M. L., Majchrzak, A., and Gasser, L. 2002. “A Design Theory for Systems that Support Emergent Knowledge Processes,” MIS Quarterly (26:3), pp. 179-212.

March, J. G. 1994. Primer on Decision Making: How Decisions Happen, New York: Free Press.

March, J. G., and Shapira, Z. 1987. “Managerial Perspectives on Risk and Risk Taking,” Management Science (33:11), pp. 1404-1418.

McFarlan, F. W. 1981. “Portfolio Approach to Information Systems,” Harvard Business Review (59:5), pp. 142-150.

Miles, M., and Huberman, A. M. 1984. Qualitative Data Analysis, Beverly Hills, CA: Sage Publications.

Mintzberg, H. 1994. The Rise and Fall of Strategic Planning, New York: MacMillan.

Mitchell, V. L., and Zmud, R. W. 2006. “Endogenous Adaptation: The Effects of Technology Position and Planning Modes on IT-Enabled Change,” Decision Sciences (37:3), pp. 325-355.

Mithas, S., Tafti, A., and Mitchell, W. 2013. “How a Firm’s Competitive Environment and Digital Strategic Posture Influence Digital Business Strategy,” MIS Quarterly (37:2), 511-536.

Nolan, R., and McFarlan, F. W. 2005. “Information Technology and the Board of Directors,” Harvard Business Review (83:10), pp. 96-106.

Philip, G. 2007. “IS Strategic Planning for Operational Efficiency,” Information Systems Management (24:3), pp. 247-264.

Piccoli, G., and Ives, B. 2005. “IT-Dependent Strategic Initiatives and Sustained Competitive Advantage: A Review and Synthesis of the Literature,” MIS Quarterly (29:4), pp. 747-776.

Prendergast, C. 1999. “The Provision of Incentives in Firms,” Journal of Economic Literature (37:1), pp. 7-63.

Quinlan, J. R. 1986. “Induction of Decision Trees,” Machine Learning (1:1), pp. 81-106.

Quinlan, J. R. 1990. “Decision Trees and Decision Making,” IEEE Transactions on Systems, Man, and Cybernetics (20:2), pp. 339-346.

Quinlan, J. R. 1993. C4.5: Programs for Machine Learning, San Mateo, CA: Morgan Kauffman Publishers.

Rajegopal, S. 2012. Portfolio Management: How to Innovate and Invest in Successful Projects, Basingstoke, UK: Palgrave Macmillan.

Ramasubbu, N., Mithas, S., Krishnan, M., and Kemerer, C. 2008. “Work Dispersion, Process-Based Learning, and Offshore Software Development Performance,” MIS Quarterly (32:2), pp. 437-458.

Reyck, B. D., Grushka-Cockayne, Y., Lockett, M., Calderini, S. R., Moura, M., and Sloper, A. 2005. “The Impact of Project Portfolio Management on Information Technology Projects,” International Journal of Project Management (23:7), pp. 524-537.

Sabherwal, R., and Chan, Y. E. 2001.”Alignment between Business and IS Strategies: A Study of Prospectors, Analyzers, and Defenders,” Information Systems Research (12:1), pp. 11-33.

Sambamurthy, V., and Zmud, R. W. 1999. “Arrangements for Information Technology Governance: A Theory of Multiple Contingencies,” MIS Quarterly (23:2), pp. 261-290.

Segars, A. H., and Grover, V. 1999. “Profiles of Strategic Information Systems Planning,” Information Systems Research (10:3), pp. 199-232.

Shannon, C. E., and Weaver, W. 1963. The Mathematical Theory of Communication, Urbana, IL: University of Illinois Press.

Sherer, S. A., and Alter, S. 2004. “Information Systems Risks and Risk Factors: Are They Mostly About Information Systems?,”

Communications of the Association for Information Systems (14:1), Article 2.

Straub, D. W., and Welke, R. J. 1998. “Coping with Systems Risk: Security Planning Models for Management Decision Making,” MIS Quarterly (22:4), pp. 441-469.

Susarla, A., Subramanyam, R., and Karhade, P. 2010. “Contractual Provisions to Mitigate Holdup: Evidence from Information Technology Outsourcing,” Information Systems Research (21:1), pp. 37-55.

Tessmer, A. C., Shaw, M. J., and Gentry, J. A. 1993. “Inductive Learning for International Financial Analysis: A Layered Approach.” Journal of Management Information Systems (9:4), pp. 17-37.

Weill, P., and Ross, J. W. 2004. IS Governance: How Top Performers Manage IS Decision Rights for Superior Results, Boston: Harvard Business School Press

Xue, Y., Liang, H., and Boulton, W. R. 2008. “Information Technology Governance in Information Technology Investment Decision Processes: The Impact of Investment Characteristics, External Environment, and Internal Context,” MIS Quarterly (32:1), pp. 67-96.

## About the Authors

Prasanna Karhade is currently an assistant professor in the Department of Information Systems, Business Statistics and Operations Management at The Hong Kong University of Science and Technology. He earned his Ph.D. from the University of Illinois at Urbana-Champaign in 2009. His research interests include design of formal contracts for governing IT outsourcing relationships, IT governance, and the impact of IT on firm innovation. His research has been published in Information Systems Research. Prasanna is the contact author for this article.

Michael J. Shaw is Hoeft Chair of Information Systems in the Department of Business Administration at the University of Illinois at Urbana-Champaign. He has been the editor-in-chief (with J. Becker) of the journal Information Systems and e-Business Management. He is affiliated with, in addition to his home department, the National Center for Supercomputing Applications and the Information Trust Institute. His most recent research has focused on business analytics and on the functions of chief information officers, supply-chain management, and electronic commerce.

Ramanath (Ram) Subramanyam is an associate professor of Business Administration at the University of Illinois at Urbana-Champaign. He earned his Ph.D. from the Ross School of Business, University of Michigan (2004) and a Bachelors of Electronics and Communication Engineering from NIT, Trichy, India. His research interests include IT sourcing governance, management of IS design processes and project management, new product development, customer influences on technological product design, and IT-driven sustainability in products and processes. His research has appeared in various journals, including Information Systems Research, Manufacturing & Service Operations Management, IEEE Transactions on Software Engineering, and Decision Support Systems.

# PATTERNS IN INFORMATION SYSTEMS PORTFOLIO PRIORITIZATION: EVIDENCE FROM DECISION TREE INDUCTION

Prasanna Karhade

Department of Information Systems, Business Statistics and Operations Management, The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, HONG KONG {karhade@ust.hk}

Michael J. Shaw and Ramanath Subramanyam Department of Business Administration, University of Illinois at Urbana–Champaign, Champaign, IL 61820 U.S.A. {mjshaw@illinois.edu} {rsubrama@illinois.edu}

## Appendix A

## Theory Development: Decision Rationale Profile for Firms that Adopt Dual IS Conservative- and IS Innovator-Like Strategies

Some firms adopt dual (IS-conservative-like and IS innovator-like) strategies. The behavior of firms that adopt a dual IS strategy is associated with the following characteristics: they (1) adhere to dual goals with a simultaneous emphasis on efficiency improvements and cautious exploration of new opportunities, (2) adopt a relatively formal decision-making structure, and (3) are inherently risk averse. Dual goals ar likely to exert a conflicting influence on the behavior of firms that adopt both IS conservative- and IS innovator-like strategies.

Balancing dual goals can be cognitively demanding and thus we maintain that the complexity of the decision rationale applied by such firms is likely to be high. Thus, the communicability of this decision rationale is likely to be low. The consistency with which decision rules are applied by such firms in the process of managing these dual conflicting goals is likely to be low as applying the same rule with a high consistency would imply that one of the dual goals is most likely not being sufficiently addressed. Acting appropriately, decision makers with a low-risk appetite are expected to approve high-risk initiatives only after ensuring that risk mitigation mechanisms have been designed to lower the likelihood of failures (Boynton and Zmud 1987; March and Shapira 1987; Straub and Welke 1998). In summary, the decision rationale applied by firms that adopt dual IS conservative- and IS innovator-like strategies is likely to be complex, applied with a low consistency, and likely to focus on the assessment/mitigation of risks.

Proposition 3: The decision rationale used by firms that adopt dual IS conservative-like and IS innovator-like strategies for IS portfolio prioritization is likely to be difficult to communicate, applied with low consistency and focused on risk assessment/mitigation.

## Appendix B

## Identifying the IS Strategy

Semi-structured interviews with key informants within different business units at the research site revealed several recurring themes which enabled us to determine their adopted IS strategies.

IS Conservative Classification: Interviews revealed that executives within one business unit at our research site place a high emphasis on adopting a safe and stable approach to running their business, as one executive noted, “[a] significant portion of our revenues were generated primarily based on a set of stable, proven, technologies.” The approach they adopt toward investment in IS tends to be very safe and stable. They largely invest in proven, safe IS and perceive IS as a vehicle to support their business operations in a stable manner. Informants also revealed that they are extremely conservative and risk averse when it comes to investments in IS. Given their conservative approach to investing in IS, this firm is not in any hurry to adopt new, emerging IS. They only invest in IS that is proven to be a stable, predictable technology in their industry. Informants also revealed an emphasis on intensive planning and a top–down formal structure for decision making within their firm. Their conservativeness enables them to ensure that all of their investment is geared toward stable and proven IS that systematically improves the efficiency of their business operations. Given the prevalence of such strong themes, this firm was classified as an IS conservative. This research choice was unanimously validated for us by the informants at our research site.

IS Innovator Classification: Interviews revealed that executives within another business unit at our research site place a high emphasis on the necessary experimentation for their continual growth and perceive IS as a vehicle for their experimentation/growth. Corroborating evidence for this emphasis on continual growth was also obtained from the annual report:

[We] have been working feverishly to globalize this business….[A] significant fraction of our orders now come from outside the U.S.…[New] customers in Country A, B, C are now buying our products….We want to take advantage of a new market of \$4 billion in global opportunities....[We] have effectively doubled the market for this great business

Informants revealed that they are focused on experimentation and take risks when it comes to investments in IS. Given their innovative approach to investing in IS, this firm is more likely to quickly respond to signals from their external dynamic environment to adopt new, emerging IS. Informants revealed their reliance on a less formal, more bottom–up approach to decision making within their firm. Given the prevalence of such strong themes emphasizing experimentation with IS for growth, this firm was classified as an IS innovator. This research choice was also unanimously validated for us by the informants at our research site.

Dual IS Strategy Classification: Finally, interviews with executives at another business unit at our research site revealed the presence of both the IS conservative- and IS innovator-like behavior, described above, in their philosophy in the use of IS. This firm was classified as having dual IS strategies. (Theoretical development for this IS strategy is discussed in Appendix A; data are presented in the fourth section of Appendix C; results are presented in Appendix D. Finally, we discuss the managerial implications of this IS strategy in the subsection, “Mediating Role of the Decision Rationale Profile,” of the main paper.)

## Appendix C

Sample Selection Criteria, Characterizing Initiatives (Information Attributes)

## Elimination of Initiatives

To account for various confounding factors, prior research has suggested focusing on only one kind of portfolio (e.g., Earl 1989; Sabherwal and Chan 2001). In accordance with this recommendation, we employed a rigorous selection process to retain only initiatives pertaining to business applications of IS.

Regulatory compliance related proposals (e.g., Sarbanes-Oxley Act) were eliminated.

A key decision maker at the research site commented on this elimination step as follows:

Managers who really need funds to finish off their older initiatives will sometimes pitch “new” initiatives and say that these are SOX initiatives …expecting us to readily agree…but SOX initiatives are very different and different forces guide those choices….There always is this dark side to planning effort and I am glad you excluded SOX initiatives from your analysis.

Such discussions with key decision makers at the research site provided validation for our sampling criteria.

Next, proposals strictly pertaining to IT infrastructure, identified for us by the decision makers, were also eliminated. In this research study, we intend of examine the influence of the strategic orientation of an organization on the decision rationale it uses for IT governance. At our research site, the IT infrastructure portfolio was governed as an enterprise-wide, shared capability. The theoretical justification for governing IT infrastructure portfolio as an enterprise-wide centralized capability, at our research site, is discussed next.

As multibusiness organizations have to make a choice between granting autonomy to their separate businesses (or business units) and extracting synergies across their businesses (or business units), prior work has framed this choice as a tradeoff (Weill and Ross 2004). In the context of the portfolio of IT investments, we find that organizations can enjoy the benefits of both of these paradigms if they leverage these different mechanisms for different kinds of IT portfolios. At our research site, we found that the IT infrastructure portfolio was relatively standardized and there were significant synergies to be extracted across various businesses on the IT infrastructure portfolio. From the IT governanc standpoint, given the high levels of standardization within the IT infrastructure, this IT infrastructure portfolio was managed as an enterprisewide capability. With regard to these IT infrastructure components, a standardized approach was leveraged across the entire organization to derive synergies from this IT infrastructure portfolio.

IT infrastructure components are systematically different from business applications of IS in three ways. First, approvals for certain IT infrastructure initiatives do not require comprehensive search (decision) processes (Boonstra 2003). For instance, typically, the decision to use Microsoft Office as the office productivity software does not require elaborate search processes. Second, IT infrastructure components are often used in this organization, across the entire enterprise, almost in a “plug-and-play” manner with very little or no customization. Business applications of IS, on the other hand, required systematic customization depending on the various different business needs across individual businesses or business units within the organization. Third, IT infrastructure initiatives enjoy extensive scale advantages such that the licensing fees for these hardware/software components that are used in a plug-and-play/standardized manner across the entire enterprise significantly decrease with increasing scales/volumes. Typically, standardized vendor contracts kick in and large organizations can get better deals and services as they purchase multiple licenses in larger volumes. Centralization of such IT infrastructure capabilities has some strong advantages in the form of significant cost savings and an enterprise-wide shared capability approach also leverages technology expertise across the company while permitting large and cost-effective contracts with hardware/software vendors. Governing the IT infrastructure portfolio as an enterprise-wide, shared capability was especially considered better at this particular large organization as it operated in multiple countries and continents and the senior management believed that standardization of the IT infrastructure would significantly reduce coordination costs (Weill and Ross 2004). Given these theoretical reasons, we excluded IT infrastructure initiatives from our consideration set and, in accordance with prior research (e.g., Earl 1989; Sabherwal and Chan 2001), exclusively focused only on one portfolio pertaining to the set of proposals that systematically described business applications of IS.

## Information Attributes

## Characterizing Benefits

Our key informants indicated that although managers proposing new initiatives were required to richly characterize the benefits associated their initiatives, quantifying these benefits with a number was not a requirement. In other words, IT governance decisions did not depend on a numeric measure of benefits. Arguably, a rigorous quantification of benefits associated with initiatives (with a return-on-investment measure) would be a desirable decision-making aid. But often, arriving at such a numeric measure is extremely difficult given the bounded rationality of the economic actors involved in planning (Simon 1955). Detailed discussions with the decision makers revealed numerous challenges associated with quantifying the benefits associated with proposed initiatives. Discussions with the CIO, senior management, and members of the top management teams revealed that especially in the early planning stages, ROI metrics were not exclusively used as decision-making criteria.

These insights revealed that decisions on proposed initiatives are often made on a tacit level by relying on qualitative information on the type of benefits proposals are designed to deliver. Based on our understanding of the pertinent literature (e.g., Broadbent et al. 1999; Sabherwal and Chan 2001), five kinds of benefits that initiatives could potentially offer were used to create five variables to comprehensively characterize benefits associated with initiatives. The comprehensiveness of these five variables was validated for us by the key decision makers at the research site. Initiatives were designed such that they could offer multiple types of benefits and thus these five different kinds of benefit associated with proposals were not mutually exclusive.

Although all of the initiatives we examine in this study (annual planning cycle for investments spanning the 2006–2007 time period) were of high substantive significance to the organization, not all these initiatives offered strategic benefits. Some of these initiatives were designed specifically with efficiency improvements in mind. Based on several consultations with members of the CIO’s office and the metrics within this organization, such initiatives were classified as initiatives that offered only efficiency improvements and not as initiatives that offered strategic benefits. Such proposals were crafted very differently, highlighting the strategic benefits offered by their initiatives, and it was thus very easy for us to identify such initiatives (in consultation with the members of the metrics groups at the research site) which offered strategic benefits and efficiency improvements. Discussions with the members of the CIO’s office and the metrics group within this organization guided us to systematically classify benefits and helped us validate these nuanced distinctions/classifications. Given the dark side to the planning effort, senior executives feared that there would be a tendency for every manager to claim that all initiatives offered strategic benefits so as to warrant approval and funding. Senior management cautioned managers that all the initiatives claiming to offer strategic benefits could warrant additional scrutiny. Thus, we do not find evidence to suggest that managers were claiming benefits that were not genuinely built into the design of their initiatives.

1. Efficiency improvements: Certain initiatives were designed so as to develop IS that replaced, digitized, or automated manual tasks or business processes (Camillus and Lederer 1985; Philip 2007). These initiatives, focused on exploitation (e.g., March 1991), helped managers automate various business activities and thus operate with higher efficiency.

2. Marketing benefits: Certain initiatives were designed to develop IS that enabled businesses to create, promote, and better position new products/services. These initiatives helped managers to effectively market their products (Sabherwal and Chan 2001).

3. Strategic benefits: Certain initiatives were designed to develop IS which were deemed strategic. These initiatives helped managers to develop strategic capabilities to enable them to achieve some strategic advantages (Piccoli and Ives 2005).

4. Efficient interorganizational business processes: Certain initiatives were designed to develop IS that improved the efficiency of interorganizational business processes including critical supplier-, customer-facing processes (e.g., Kumar and van Dissel 1996).

5. Cycle Time Reductions: Certain initiatives were designed to develop IS that had the potential to offer business process improvements, specifically aimed at reducing the business cycle implementation times associated with certain business processe (Broadbent et al. 1999)

## Characterizing Risks

Risk assessment is critical for IT governance (Iversen et al. 2004; McFarlan and Nolan 2005). Based on the recommendations from prior work (Lyytinen et al. 1998), we adopt McFarlan’s (1981) approach for assessing the risk of proposed initiatives, resulting in these three measures.

6. Initiative Size: This attribute was measured based on the estimated investment required to implement the initiative. Risk associated with an initiative increases with its size (McFarlan 1981). This variable was assigned the following three values: low size (investment less than U.S. \$100,000), medium size (investment greater than U.S. \$100,000 but less than U.S. \$1,000,000), and high size (investment greater than U.S. \$1,000,000). These anchors for the size measure were validated for their suitability based on inputs from the senior management and the CIO at the research site.

7. Initiative Structure: Some initiatives by their very definition are well-defined and have high clarity and certainty in terms of their expected inputs and outputs. Thus, the corresponding organizational tasks required to implement such initiatives are relatively straightforward (Eisenhardt 1985). Initiatives whose inputs/outputs are vulnerable to change have low structure. Initiatives of high structure are less risky when compared to initiatives of low structure (McFarlan 1981). This variable was assigned two values: high structure (well-defined objectives for the initiative) and low structure (initiative with relatively fluid objectives). The vulnerability to change and the extent of clarity of the objectives, which separates low-structured, high-risk initiatives from high-structured, lowrisk initiatives, was ascertained by the managers proposing initiatives and validated for us by the members of the senior management and the CIO at the research site.

This variable was assigned only two values. The decision makers indicated that, from an IT governance standpoint, such a measurement scheme was satisfactory as it helped them to identify and separate the high-structured, low-risk initiatives from the highrisk, low-structured initiatives. Although in theory the degree of inherent structure in a project is a continuous variable, this use of a two-category variable demonstrates satisficing behavior from the boundedly rational decision makers involved in IT governance tasks.

8. Prior Experience: As the familiarity of an organization with a technology increases, the likelihood of encountering technical problems reduces. The higher the prior experience with technologies used in the execution of initiatives, the lower the risk associated with such initiatives (McFarlan 1981). This variable was assigned three values: low (initiatives with new, emerging technologies with low familiarity within the organization), medium (initiatives involving technologies when the familiarity with that technology was neither high nor low), and high (initiatives involving standard technologies very familiar to the organization).

The design of this variable also provides evidence of the satisficing behavior of the decision makers. Values at the ends of the spectrum for this variable were very easy to identify. Managers had worked with certain mature technologies in the past and delivered successful projects. Some technologies were nascent and emerging, and managers had not yet adopted these technologies within the organization. Identifying initiatives with high/low prior experience with technologies was relatively straightforward, and thus identifying the technologies for which the prior experience was neither high nor low was also easy. From a decision-making standpoint for IT governance, the design of this three category variable was deemed satisfactory.

## Characterizing Risk Mitigation Mechanisms

Diverse kinds of risk mitigation mechanisms are critical for successful implementation of business initiatives that depend on IS (e.g., Iversen et al. 2004; Nolan and McFarlan 2005; Piccoli and Ives 2005; Sherer and Alter 2004). Prior research points to at least three kinds (e.g., Baskerville 1993), including (1) internal risk mitigation mechanisms pertaining to software and technological capabilities (e.g., Baskervill 1993), (2) process risk mitigation mechanisms pertaining to the management of software development processes and methodologies (Ramasubbu et al. 2008; Sherer and Alter 2004), and (3) external risk mitigation mechanisms concerning the business process redesign implications of new initiatives (Broadbent et al. 1999). Variables on these categories of decision criteria,<sup>1</sup> used for managing risks associated with these initiatives are described next.

## Internal Risk Mitigation Mechanisms

9. Employ in-house software: Software applications developed in-house potentially embed organizational knowledge (e.g., Earl 1993; Mitchell and Zmud 2006; Saarinen and Vepsalainen 1994) and thus their use in the execution of proposed initiatives can be viewed as a risk mitigating factor. Since in-house software applications embed organizational process knowledge, this familiarity with the technological solution to an organizational process problem makes it relatively easy to redeploy this solution in the context of a new initiative. This variable was assigned a value of 1 if a proposed initiative could leverage a software application developed in-house or a value of 0 otherwise.

10. Internal Maturity: Managers who have managed certain initiatives in the past (e.g., an e-commerce website to solve some business problem in the past) are likely to develop mature plans<sup>2</sup> for future initiatives. So although the development work for the subsequent initiatives is not done, it is easy to see how the proposals for these subsequent initiatives are likely to be considered mature and thus perceived to be less risky (Boonstra 2003). Risks associated with an initiative decrease as the maturity associated with the proposed initiative increases (Ramasubbu et al. 2008). Uncertainties associated with an initiative are often resolved by dedicating more resources to develop the plan for a proposed initiative and advancing it further along the software development lifecycle (SDLC) maturity phases. In other words, a proposal or plan of an idea that is more developed and further along the SDLC maturity phases is likely to be less risky.<sup>3</sup> This variable has been assigned three values: low (proposed initiative in its early stages of conception), medium (requirements and goals associated with the initiative are clearly defined), and high (several different future contingencies have been envisioned and controls have been systematically developed to manage those risks by crafting a complete, mature proposal). In other words, the proposals for some initiatives are more mature and less risky than others as managers proposing these initiatives can build on some similar initiatives they have implemented in the past, so the internal maturity of such proposals is relatively high. These plans, given their high maturity, are likely to be perceived as being less risky.

## Process Risk Mitigation Mechanisms

Exploiting potential business opportunities that critically depend on IS involves several organizational tasks in addition to just deploying the software. Process capabilities are often deemed critical in delivering successful initiatives. The CIO and other members of the top management teams we interviewed validated that the likelihood of success is critically dependent not only on the maturity of the initiative proposals but also on the teams (collaborations between the internal and external partners) assembled to manage and implement the initiatives. Potential business opportunities that critically depend on IS often have a significant impact on the business processes of an organization. Such initiatives which critically depend on IS can either constrain or facilitate business process redesign (BPR) initiatives and vice versa (Broadbent et al. 1999). Managing the BPR implications of IT initiatives and vice versa is critical for successfully executing proposed initiatives.

11. Business process redesign completed: Before starting initiatives that critically depend on IS, envisioning process changes, and redesigning work flow activities, exerting effort and planning for such BPR tasks is critical to minimizing process risks (Broadbent et al. 1999). This variable was assigned a value of 1 when BPR planning tasks were completed and these controls were systematically presented in the proposal and a value of 0 when the BPR planning tasks were not described in the proposal.

12. Resources for process redesign committed: Identifying organizational resources and committing them for undertaking BPR planning tasks before starting initiatives can be a critical risk mitigation factor (Lambert 1986). For the successful delivery of these new business initiatives that critically depend on IS, the early involvement of the right resources that systematically understand the business process implications and ramifications of these initiatives is critical. This variable was assigned a value of 1 when resources were identified and assigned to proposed initiatives for conducting BPR tasks and a value of 0 otherwise.

## External Risk Mitigation Mechanisms

13. Employ consultant knowledge: Specialized external consultants/partners can add value to large IT initiatives and integrating these external sources of knowledge with internal expertise can mitigate risks. Consultants can offer expertise in specific areas and, in particular, their exposure of several different organizational contexts on similar initiatives can be helpful in minimizing the likelihood of project failure (Ko et al. 2005). For each initiative, this variable was assigned a value of 1 when managers identified and proposed leveraging capabilities from external consultants and a value of 0 otherwise. The identification of external partners who have worked on similar initiatives in the past is a nontrivial task and managers are required to exert significant effort to systematically identify such external partners.<sup>4</sup> In the context of this large organization, proposals from managers that identified such pertinent, external partners that have worked on similar initiatives in the past were considered less risky.

14. Utilize specialized software applications: Organizations can potentially manage successful delivery of large initiatives by procuring specialized software products. These partial solutions to specialized organizational problems can potentially expedite initiative progress and improve likelihood of success (McFarlan 1981). Given the large size of this organization, managers within all the business units could exert significant bargaining power to attract very competitive contracts from multiple software vendors. Given the high bargaining power of this large organization, risks of vendor opportunism were relatively easy to mitigate. This identification of vendors early on in the process of designing an initiative helped managers systematically manage risks and understand how these building blocks, in the form of specialized software applications, could be leveraged to expedite the development of their initiatives.

This variable was assigned a value of 1 if the initiative proposed the procurement of specialized software and a value of 0 otherwise.

15. Leverage third-party solutions: Executives can also potentially manage successful delivery of large initiatives by leasing third party technologies (e.g., McFarlan 1981) solutions as building blocks. Third party applications model best practices and thus can expedite the delivery of proposed initiatives, simultaneously improving likelihood of success. This variable was assigned a value of 1 if the proposed initiative recommended leveraging third party software applications and a value of 0 otherwise.

This risk mitigation mechanism is conceptually similar to the purchase of specialized software solutions from external vendors. In the event of the purchase of licenses, these software components would need to be hosted within the organization and would necessitate additional maintenance effort over the duration of the initiative. The lease of third party applications would free the organization from the burden of hosting software applications as a part of the internal IT infrastructure. Barring these minor differences, both of these risk mitigation mechanisms demonstrated that managers proposing new initiatives had exerted significant effort to identify vendors, craft preliminary contract/service level agreements, and negotiate preliminary price quotes to systematically manage the risks associated with their initiatives. Both of these mechanisms depended on external vendors, but given the large size of this organization, the likelihood of opportunistic behavior on behalf of the vendors was deemed very low. In essence, both of these mechanisms were considered risk mitigating as they demonstrated that managers proposing new initiatives, while managing the threat of opportunistic behavior on the part of the external vendors, had exerted significant effort to leverage partial solutions as building blocks to assuage the risks associated with their initiatives.

Measure definitions for these 15 attributes were consistently enforced across all proposal submissions before the commencement of planning. Portfolio data analyzed in our study was subjected to at least two rounds of validation before decision making started.

## Summarized Views of Portfolio Data

IS Conservative’s Portfolio (Total Number of Initiatives = 72)  
![](/api/attachments/MSBGCYRT/fulltext/images/aeb6ab4c53cfde999c612e36c1622c9380bd6e64724da6f94fb14ce5a8b28816.jpg)

Accepted Rejected

Accepted Rejected

AcceptedRejected

IS Conservative’s Portfolio: Risk Mitigation Attributes (Total Number of Initiatives = 72)  
![](/api/attachments/MSBGCYRT/fulltext/images/cffcc1d572d883940db3176f95ea5f4c7ff14e040c23ec1c9a6cca4ca24aedbd.jpg)  
AcceptedRejected  
AcceptedRejected

IS Innovator’s Portfolio (Total Number of Initiatives = 32)  
![](/api/attachments/MSBGCYRT/fulltext/images/cdc1c60036b5f46f8f772390d5990592cb3bf4ac8ce2db066daca8c6cbef80f6.jpg)

IS Innovator’s Portfolio: Risk Mitigation Attributes (Total Number of Initiatives = 32)  
![](/api/attachments/MSBGCYRT/fulltext/images/34b70136cf9a3b8314889ea4dccfbc637f2dd4abf41761d7c4b7d74f6f4465da.jpg)

Portfolio of a Business Unit with a Dual IS Conservative- and IS Innovator-Like Strategy (Total Number of Initiatives = 57)  
![](/api/attachments/MSBGCYRT/fulltext/images/a05f9266981f7eb2cd5972ff1cd9fd7bc492274763eed06811cd4ab6e57c1f77.jpg)

Portfolio of a Business Unit with a Dual IS Conservative- and IS Innovator-Like Strategy (Total Number of Initiatives = 57)

<table><tr><td>Internal Risk Mitigation Mechanisms</td><td>External Risk Mitigation Mechanisms</td><td>Process Risk Mitigation Mechanisms</td></tr><tr><td rowspan="2"><img src="/api/attachments/MSBGCYRT/fulltext/images/d2377445ad32e49ea28e16edfbf6c5a2381f957449313c543d75e90bb717a0a9.jpg"/>☑ Accepted ☐ Partial ☐ Rejected</td><td rowspan="2"><img src="/api/attachments/MSBGCYRT/fulltext/images/68d60806fed55181b988a32e93b59c7fbbe4167cfce71540f5443cdc09d08d19.jpg"/></td><td><img src="/api/attachments/MSBGCYRT/fulltext/images/f8a1bf99079a4c081755135d87a094f96bb54be346683fa10531be7ade91ba4a.jpg"/></td></tr><tr><td>☑ Accepted ☐ Partial ☐ Rejected</td></tr><tr><td rowspan="3"><img src="/api/attachments/MSBGCYRT/fulltext/images/56d2801c8fad41f965e68b5a3643a2c105122aefd8422cd9e2dbe4d6c334abab.jpg"/>☑ Accepted ☐ Partial ☐ Rejected</td><td><img src="/api/attachments/MSBGCYRT/fulltext/images/b37249dd129b738600a7d6c008fe22be69c2866de49032c78178d841e5e737a8.jpg"/></td><td rowspan="2"><img src="/api/attachments/MSBGCYRT/fulltext/images/4a8e815f1a4cfbf9cfc3c5689845ee895cefce547057375926988147bf5b2ec0.jpg"/></td></tr><tr><td>☑ Accepted ☐ Partial ☐ Rejected</td></tr><tr><td><img src="/api/attachments/MSBGCYRT/fulltext/images/97acab8ad7c55e8b0257b623ee32b03c69007dde8f0c74ffd2762c4b06eb1d1a.jpg"/></td><td>☑ Accepted ☐ Partial ☐ Rejected</td></tr></table>

## Appendix D

Decision Tree for Business Unit that Adopted Dual IS Conservativeand IS Innovative-Like Strategies  
![](/api/attachments/MSBGCYRT/fulltext/images/179b7bb281090ffe069c3c77929e2ba75fd881c0007f144febe126ef66c445ad.jpg)

## References

Baskerville, R. 1993. “Information Systems Security Design Methods: Implications for Information Systems Development,” ACM Computing Surveys (25:4), pp. 375-414.

Boonstra A. 2003. “Structure and Analysis of IS Decision-Making Processes,” European Journal of Information Systems (12:3), pp. 195-209.

Boynton, A. C., and Zmud, R. W. 1987. “Information Technology Planning in the 1990’s: Directions for Practice and Research” MIS Quarterly (11:1), pp. 59-71.

Broadbent, M., Weill, P., Clair, D. S., and Kearney, A. T. 1999. “The Implications of Information Technology Infrastructure for Business Process Redesign,” MIS Quarterly (23:2), pp. 159-182.

Camillus, J. C., and Lederer, A. L. 1985. “Corporate Strategy and the Design of Computerized Information Systems,” Sloan Management Review (26), pp. 35-42.

Earl, M. J. 1989. Management Strategies for Information Technology, Englewood Cliffs, NJ: Prentice-Hall.

Eisenhardt, K. M. 1985. “Control: Organizational and Economic Approaches,” Management Science (31:2), pp. 134-149.

Iversen, J. H., Mathiassen, L., and Nielsen, P. A. 2004. “Managing Risk in Software Process Improvement: An Action Research Approach,” MIS Quarterly (28:3), pp. 395-433.

Ko, K., Kirsch, L. J., and King, W. R. 2005. “Antecedents of Knowledge Transfer from Consultants to Clients in Enterprise System Implementations,” MIS Quarterly (29:1), pp. 59-85.

Kumar, K., and van Dissel, H. G. 1996. “Sustainable Collaboration: Managing Conflict and Cooperation in Interorganizational Systems,” MIS Quarterly (20:3), pp. 279-300.

Lambert, R. A. 1986. “Executive Effort and Selection of Risky Projects,” RAND Journal of Economics (17:1), pp. 77-88.

Lyytinen, K., Mathiassen, L., and Ropponen, J. 1998. “Attention Shaping and Software Risk: A Categorical Analysis of Four Classic Approaches,” Information Systems Research (9:3), pp. 233-255.

March, J. G. 1991. “Exploration and Exploitation in Organizational Learning,” Organization Science (2:1), pp. 71-87.

March, J. G., and Shapira, Z. 1987. “Managerial Perspectives on Risk and Risk Taking,” Management Science (33:11), pp. 1404-1418.

McFarlan, F. W. 1981. “Portfolio Approach to Information Systems,” Harvard Business Review (59:5), pp. 142-150.

Mitchell, V. L., and Zmud, R. W. 2006. “Endogenous Adaptation: The Effects of Technology Position and Planning Mode on IT-Enabled Change,” Decision Sciences (37:3), pp. 325-355.

Nolan, R., and McFarlan, F. W. 2005. “Information Technology and the Board of Directors,” Harvard Business Review (83:10), pp. 96-106.

Philip, G. 2007. “IS Strategic Planning for Operational Efficiency,” Information Systems Management (24:3), pp. 247-264.

Piccoli, G., and Ives, B. 2005. “IT-Dependent Strategic Initiatives and Sustained Competitive Advantage: A Review and Synthesis of the Literature,” MIS Quarterly (29:4), pp. 747-776.

Ramasubbu, N., Mithas, S., Krishnan, M., and Kemerer, C. 2008. “Work Dispersion, Process-Based Learning, and Offshore Software Development Performance,” MIS Quarterly (32:2), pp. 437-458.

Saarinen, T., and Vepsäläinen, A. P. J. 1994. “Procurement Strategies for Information Systems,” Journal of Management Information Systems (11:2), pp. 197-208.

Sabherwal, R., and Chan, Y. E. 2001.”Alignment between Business and IS Strategies: A Study of Prospectors, Analyzers, and Defenders,” Information Systems Research (12:1), pp. 11-33.

Sherer, S. A., and Alter, S. 2004. “Information Systems Risks and Risk Factors: Are They Mostly About Information Systems?,” Communi cations of the Association for Information Systems (14:1), Article 2.

Simon, H. A. 1955. “A Behavioral Model of Rational Choice,” The Quarterly Journal of Economics (69:1), pp. 99-118.

Straub, D. W., and Welke, R. J. 1998. “Coping with Systems Risk: Security Planning Models for Management Decision Making,” MIS Quarterly (22:4), pp. 441-469.

Weill, P., and Ross, J. W. 2004. IS Governance: How Top Performers Manage IS Decision Rights for Superior Results, Boston: Harvard Business School Press.
