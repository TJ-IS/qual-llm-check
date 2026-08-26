---
otero_id: 728
otero_key: "5T5SFCC8"
title: "Diffusion of knowledge in social media networks: effects of reputation mechanisms and distribution of knowledge roles"
authors: "Taha Havakhor; Amr A. Soror; Rajiv Sabherwal"
year: "2018"
journal: "Information Systems Journal"
doi: "10.1111/isj.12127"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Diffusion of knowledge in social media networks: effects of reputation mechanisms and distribution of knowledge roles

Taha Havakhor,\* Amr A. Soror<sup>†</sup> & Rajiv Sabherwal<sup>‡</sup>

\*Management Science & Information Systems Department, Spears College of Business, Stillwater, OK USA, email: taha.havakhor@okstate.edu, <sup>†</sup>Department of Information Systems and Decision Sciences, Mihaylo College of Business and Economics, California State University, Fullerton, AR USA, email: asoror@fullerton.edu, and <sup>‡</sup>Information Systems Department, Sam M. Walton College of Business, University of Arkansas, Fayetteville, AR USA, email: RSabherwal@walton.uark.edu

Abstract. Social media platforms serve as important tools for diffusing knowledge within organizations. The factors affecting knowledge diffusion through social media networks (SMNs) need to therefore be better understood. Accordingly, this paper focuses on two SMN-speci<sup>fi</sup>c characteristics – reputation mechanisms and the distribution of knowledge roles – which are argued to enhance and enable, respectively, the smooth transfer of knowledge in a SMN. To examine their effects, we distinguish between two types of reputation mechanisms – adaptive and objective – and across three distinct knowledge roles in SMNs: seekers, contributors and brokers. We argue that the extent of knowledge diffusion in the SMN depends on the type of mechanism and the relative distribution of these three roles. Using data collected through an agent-based simulation, we <sup>fi</sup>nd that (a) the distribution of knowledge roles affects knowledge diffusion, with distributions consisted of more brokers outperforming others and (b) objective reputation mechanisms outperform adaptive mechanisms. Furthermore, we <sup>fi</sup>nd that reputation mechanisms and distribution of knowledge roles interact to in<sup>fl</sup>uence knowledge diffusion. The study’s implications for future research and practice are discussed in the ligh of its limitations. © 2016 John Wiley & Sons Ltd

Keywords: knowledge diffusion, social media networks, distribution of knowledge roles, knowledge reputation mechanisms, seekers, contributors, brokers

## INTRODUCTION

The last few years have been marked by an increasing interest in the organizational use of Facebook-like communications among employees for facilitating the diffusion of knowledge within organizations (Kiron et al., 2012; Kane et al., 2014; Leonardi, 2015). Popular examples of such social media networks (SMNs) include Jive,<sup>1</sup> Salesforce.com’s Chatter,<sup>2</sup> and Yammer,<sup>3</sup> which may be described as:

A company’s private social network that helps … start conversations, collaborate on <sup>fi</sup>les, and organize around projects (Yammer 2016)

SMNs generally host pro<sup>fi</sup>le pages and news feeds of employees within the organization. Moreover, SMNs provide affordances through which the communication between any two employees, enabled by the SMN, can be viewed and stored by any other user in those two employees’ contacts or throughout the entire organization (Majchrzak et al., 2013; Kane et al., 2014; Leonardi, 2015). As a result, SMNs facilitate the development of a forum for public discourse among employees within an organization (Mcafee et al., 2009), which entails a great potential for improving connectivity (Phang et al., 2009) and collaboration within organizations (Chiu et al., 2011).

Recent reports indicate an 80% SMN adoption rate in organizations (Overby, 2012), with 86% of managers believing that SMNs play an important role in their organizations (Kiron et al., 2012). This interest in SMNs has been triggered by SMN’s potential to fundamentally change the nature of the knowledge diffusion – de<sup>fi</sup>ned as the extent to which knowledge gets spread within a network of individuals (Guechtouli et al., 2013) – in organizations (Von Krogh, 2012). While traditional knowledge management (KM) approaches for knowledge diffusion rely on users contributing and eliciting knowledge through interactions with centralized knowledge repositories (Grover & Davenport, 2001), SMNs rely on a decentralized approach (Bradley & McDonald, 2011; Von Krogh, 2012; Beck et al., 2014) to spread knowledge within the organization by enabling interpersonal interactions among individuals seeking and sharing knowledge (Beck et al., 2014). By enabling interpersonal ties (i.e. information-carrying connections between individuals (Granovetter, 1973)), SMNs allow individuals to seek knowledge from and share knowledge with others within the organization and thus help knowledge transfer from experts to novices.

The decentralized nature of knowledge seeking and sharing activities in SMNs causes the knowledge diffusion processes to differ from those associated with the traditionally used centralized repositories, thus representing new implementation challenges for managers and organizations. This is apparent in a recent report showing that about 60% of KM practitioners consider making SMNs effective for knowledge diffusion within the organization as one of their top three challenges McKenzie & van Winkelen (2012)). Thus, the use of SMNs for knowledge diffusion within organizations necessitates a fresh look at how SMNs are developed, deployed and managed. Successful knowledge diffusion through SMNs requires knowledge exchange through social interactions among network members (Abrahamson & Rosenkopf, 1997) and ensuring the quality of the exchanged knowledge (Cross et al., 2001; Bock et al., 2005). Knowledge exchange, which represents one step for understanding knowledge diffusion, may be de<sup>fi</sup>ned as

a dyadic … communication process between two individual a knowledge seeker and a knowledge contributor (Beck et al., 2014, p. 1247).

The issue of how knowledge exchange could be promoted in SMNs has been salient in KM research (e.g. Wasko & Faraj, 2005; Ren et al., 2012; Beck et al., 2014). However, prior research has mostly examined knowledge seeking and knowledge sharing at the individual-level (e.g. Wasko & Faraj, 2005; Ren et al., 2012), with less attention paid to knowledge diffusion as a network-level phenomenon. Diffusion of knowledge in SMNs follows a bottom-up process, wherein seeking and sharing of knowledge at the individual level cumulate into the emerging pat tern of knowledge spread across the network (Macy & Willer, 2002). Although this network-leve emerging pattern is an artefact of knowledge seeking and knowledge sharing at the individual level, it is not directly deducible from the individual-level behaviour. Accordingly, research that looks beyond knowledge seeking and knowledge sharing at the individual level and investigates knowledge diffusion as a network-level phenomenon is integral to the effective utilization of SMNs for KM purposes within organizations. This call for research has been echoed by Kane et al. (2014) in their proposed framework on recent and unique theoretical issues raised by the advent of SMNs. They urged future IS research not only to examine the different factors in<sup>fl</sup>uencing user’s behaviour (i.e. participation) in SMNs at the micro-level but also to investigate how content (i.e. knowledge) spreads within SMNs at the network-level. For example, in a question about the effects of SMNs’ features on knowledge diffusion, they propose the following inquiry:

How do the features of the user pro<sup>fi</sup>le (e.g. content type, digital trace, third-party <sub>contributions) affect</sub> users<sub>’</sub> behavior <sub>and in</sub>fl<sub>uence</sub> the way content spreads across a social media network<sub>? (p. 288)</sub>

In order to study knowledge diffusion via SMNs in this paper, we leverage the knowledge diffusion literature, as well as the prior research on SMNs to address the following research question: What are the SMN-speci<sup>fi</sup>c characteristics, and their possible interactions, that drive knowledge diffusion within an organization? More speci<sup>fi</sup>cally, we examine (a) the design of SMNs’ reputation mechanisms and (b) the distribution of knowledge roles as two interdependent and SMN-speci<sup>fi</sup>c factors that affect knowledge diffusion in SMNs within an organization.

We discuss reputation mechanisms, i.e. a SMN’s features that signal the network’s members’ knowledgeability, as the more studied technological features that affect knowledge diffusion. We distinguish between two types of reputation mechanisms: adaptive reputation mechanisms, in which the knowledge sources are identi<sup>fi</sup>ed through knowledge seeking and sharing (Bush & Tiwana, 2005), and objective reputation mechanisms, in which the knowl edge is re<sup>fl</sup>ected objectively and independent of their interactions in seeking and sharing knowledge (e.g. Kamvar et al., 2003).

© 2016 John Wiley & Sons Ltd, Information Systems Journa

We also examine the distinct knowledge roles in SMNs, i.e. seekers (i.e. those who mainly seek knowledge and rarely share it), contributors (i.e. those who mainly share knowledge and rarely seek it), and brokers (i.e. those who comparably seek and share knowledge in a balanced fashion), and investigate the distribution of these knowledge roles as a second SMN-speci<sup>fi</sup>c factor that can affect knowledge diffusion. We view the distribution of knowledge roles in terms of the proportional presence of seekers, contributors and brokers. We discuss and identify the distributions of these roles that lead to higher diffusion of knowledge.

Furthermore, we argue that the effects of the distribution of knowledge roles and reputation mechanisms on knowledge diffusion are intertwined. Therefore, a joint consideration of both aspects is needed to obtain insights into the management of organizational SMNs to enhance knowledge diffusion.

Using agent-based modelling, a tool for simulating bottom-up processes (Macy & Willer, 2002), we address our research questions in a simulated network of 1000 agents (individuals). Our results indicate that SMNs with a high presence of knowledge brokers outperform SMNs with other distributions of knowledge roles, but the positive effect of replacing seekers and contributors with brokers wears off gradually. Compared with contributors, seekers are more instrumental in knowledge diffusion. Further, the differences between distributions of knowledge roles are more salient in platforms that utilize objective reputation mechanisms

## THEORETICAL BACKGROUND

In this section, we <sup>fi</sup>rst review prior literature on knowledge diffusion in SMNs and identify the gaps that this study seeks to address. We subsequently discuss the factors identi<sup>fi</sup>ed by KM literature as in<sup>fl</sup>uencing knowledge diffusion.

## Review of literature investigating SMNs as KM tools

In the light of our interest in investigating KM in the context of SMNs, we conducted a systematic review of the prior literature on the intersection of KM and SMNs. i.e. on user's behaviour (knowledge seeking and knowledge sharing) or spread of content in the network (knowledge diffusion). More speci<sup>fi</sup>cally, we conducted a search of Web of Science for all English-language journal articles that include: (a) ‘knowledge’; (b) one or more of ‘knowledge contribution’, 'knowledge transfer'. 'knowledge sharing'. knowledge seeking' or 'knowledge diffusion': and (c) one or more of ‘social media network’, ‘social media’ or ‘social network’. We then excluded studies on knowledge sharing across organizations and other macro-level studies. This produced a set of 120 individual or intra-organizational network-level studies. Two authors then developed a coding scheme to code dependent variable(s), independent variables, methodology and the KM related focal constructs of the manuscripts (knowledge seeking, knowledge sharing and knowledge diffusion). We identi<sup>fi</sup>ed 59 articles that jointly focus on KM and SMNs. Table 1 summarizes the foci of these articles. We found that a majority of the articles (51, or 86.44%) focus on knowledge sharing, whereas much fewer (11, or 18.64%) focus on

Table 1. Summary of SMNS knowledge diffusion literature

<table><tr><td></td><td>Study*</td><td>Dependent variable/Focus</td><td>Independent variable**</td><td>Method</td><td>Knowledge seeking</td><td>Knowledge sharing</td><td>Knowledge diffusion</td><td>Knowledge roles</td><td>Reputation mechanisms</td></tr><tr><td>1</td><td>Wasko &amp; Faraj (2005)</td><td>Knowledge contribution</td><td>Enjoyment (4); reciprocity (2); reputation (2)Outcome expectation</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>2</td><td>Chiu et al. (2006)</td><td>Knowledge sharing</td><td rowspan="2">(5) reciprocity (2)Awareness about the size and shape of the network (4)Trust (2);self-efficacy (5);</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>3</td><td>Norman &amp; Huerta (2006)</td><td>Knowledge contribution</td><td>Experiment</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>4</td><td rowspan="3">Hsu et al. (2007)Ma &amp; Agarwal (2007)Quigley et al. (2007)</td><td>Knowledge sharing</td><td rowspan="4">outcome-expectation (5)Persistent labelling (6);virtual identity (6)Trust (2); self-efficacy (5);outcome expectation (5)Trust (2);task-interdependence (2);virtualness (6)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>5</td><td>Knowledge contribution</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>6</td><td>Knowledge sharing;performance</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>7</td><td rowspan="2">Staples &amp; Webster (2008) Wang &amp; Haggerty (2009)</td><td>Knowledge sharing</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>8</td><td>Knowledge transferContinuing knowledge sharing; Continuing</td><td>Virtual competency (5)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>9</td><td>He &amp; Wei (2009)</td><td>knowledge seeking</td><td rowspan="2">Confirmation of expectations (5); habit (4)Outcome expectation (5); trust (2); self-efficacy (5);reciprocity (2)Enjoyment (4);reputation (2);</td><td>Survey</td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>10</td><td>Lin et al. (2009)</td><td>Knowledge sharing</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>11</td><td rowspan="2">Marett &amp; Joshi (2009)Phang et al. (2009)</td><td rowspan="2">Information sharingKnowledge contribution;knowledge seeking</td><td rowspan="4">knowledge role (4)Perceived usability (5);perceived sociability (5)Tenure in the occupation (4);expertise (4); reputation (2)</td><td>Survey</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>12</td><td>Survey</td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>13</td><td rowspan="2">Wasko et al. (2009)Chen &amp; Hung (2010)</td><td rowspan="2">Knowledge contributionKnowledge sharing;knowledge seeking</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>14</td><td>Survey</td><td>X</td><td>X</td><td></td><td></td><td></td></tr></table>

© 2016 John Wiley & Sons Ltd, Information Systems Journa

<sub>onti</sub>n<sup>ue</sup>

<table><tr><td></td><td>Study*</td><td>Dependent variable/Focus</td><td>Independent variable**</td><td>Method</td><td>Knowledge seeking</td><td>Knowledge sharing</td><td>Knowledge diffusion</td><td>Knowledge roles</td><td>Reputation mechanisms</td></tr><tr><td></td><td></td><td></td><td>Reciprocity (2); trust (2); self-efficacy (5); outcome expectation (5)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>Erkunt (2010)</td><td>Distribution of knowledge roles</td><td>None</td><td>Social networks analysis</td><td>X</td><td>X</td><td></td><td>X</td><td></td></tr><tr><td></td><td>Suh &amp; Shin (2010)</td><td rowspan="2">Knowledge sharing</td><td>Frequency of system interactions (2); position of system interactions (3)</td><td rowspan="2">Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>16</td><td>Tseng &amp; Kuo (2010)</td><td>Trust (2); self-efficacy (5); social awareness (4)</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>17</td><td>Yu et al. (2010)</td><td>Knowledge sharing</td><td>Enjoyment (4)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>18</td><td>Bateman et al. (2011)</td><td>Knowledge sharing</td><td>Need (4); affect (4); obligation (2)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>Knowledge contribution</td><td>Playfulness (4); self-worth disconfirmation (5); distributive justice (2); interactional justice (2)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>20</td><td>Chiu et al. (2011)</td><td>Intention to continue sharing knowledge</td><td>Trust (2); guanxi orientation (2)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>21</td><td>Huang et al. (2011)</td><td>Knowledge sharing</td><td>Network position (3); cultural proclivity (2)</td><td>Experiment</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>22</td><td>Lee &amp; Cho (2011)</td><td>Knowledge seeking</td><td>Network position (3); mediating roles vs directing or monitoring (4)</td><td>Survey/ experiment</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>23</td><td>Sutanto et al. (2011)</td><td>Knowledge role (leadership)</td><td>Reputation (2); reciprocity (2)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>24</td><td>Chang &amp; Chuang (2011)</td><td>Knowledge sharing</td><td>Reputation (2); reciprocity (2)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Enjoyment (4); outcome-expectations (5); self-efficacy (5); learning orientation (4)</td><td>Survey</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>25</td><td>Oh (2012)</td><td>Knowledge sharing</td><td>Number of contributors (6)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td></td><td>Ransbotham et al. (2012)</td><td>Extent of user generated content Participation;</td><td>Number of contributors (6)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>26</td><td>Ren et al. (2012)</td><td>Willingness to help</td><td>Member attachment (2)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr></table>

Table 1. Continued  
© 2016 John Wiley & Sons Ltd, Information Systems Journa

<sub>onti</sub>n<sup>ue</sup> <sub>onti</sub>n<sup>ue</sup>

<table><tr><td></td><td>Study*</td><td>Dependent variable/Focus</td><td>Independent variable**</td><td>Method</td><td>Knowledge seeking</td><td>Knowledge sharing</td><td>Knowledge diffusion</td><td>Knowledge roles</td><td>Reputation mechanisms</td></tr><tr><td></td><td></td><td></td><td>Motivation - extrinsic(expected organizational rewards (1); reciprocal benefits (2)); intrinsic(knowledge self-efficacy (5);enjoyment in helping</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28</td><td>Aalberset al. (2013)</td><td rowspan="3">Knowledge positionPerceived Value inperson-to-personknowledge sharingKnowledge sharing;knowledge contributionKnowledge Seeking;</td><td rowspan="2">others (4))Nature of the knowledgedShared (6); an individual&#x27;ssocial network (3)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>29</td><td rowspan="2">Brown et al.(2013)de Krakeret al. (2013)</td><td>Social networksanalysis</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>30</td><td>System design (6)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>31</td><td>Lin &amp; Lai (2013)</td><td>Knowledge sharing</td><td>Network position (3)Social adjustivemotive towards</td><td>Experiment</td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>32</td><td>Peddibhotla(2013)</td><td rowspan="2">Knowledge contributionDesign of a reputationmechanism</td><td rowspan="2">specific others (2)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>33</td><td>Wang et al.(2013)Zhang &amp;</td><td>Design ScinceresearchSocial networksanalysis</td><td>X</td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>34</td><td rowspan="2">Venkatesh (2013)Zhao &amp; Chen(2013)</td><td rowspan="2">Job performanceFeatures promotingknowledge sharing</td><td>Network ties (3)</td><td>Case study</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>35</td><td>NoneParticipation andinvolvement insocial media (6)</td><td>Case study</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>36</td><td>Alberghini et al.(2014)</td><td>OrganizationalperformanceIdentify individualswith strategic roles inadvice networksLearning outcomes</td><td>Personality traits (4)</td><td>Case study</td><td>X</td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>37</td><td>Battistoni &amp;Colladon (2014)</td><td rowspan="2">(Knowledge seekingand sharing)</td><td rowspan="2">Social network structure(density, centrality) (3)</td><td rowspan="2">Social networkanalysis</td><td rowspan="2">X</td><td rowspan="2">X</td><td></td><td></td><td></td></tr><tr><td>38</td><td>Hamraet al. (2014)Hsu &amp;</td><td></td><td></td><td></td></tr><tr><td>39</td><td>Chang (2014)</td><td>Knowledge sharing</td><td>Trust (2); uncertainty (5)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr></table>

Table 1. Continued  
© 2016 John Wiley & Sons Ltd, Information Systems Journa

<table><tr><td></td><td>Study*</td><td>Dependent variable/Focus</td><td>Independent variable**</td><td>Method</td><td>Knowledge seeking</td><td>Knowledge sharing</td><td>Knowledge diffusion</td><td>Knowledge roles</td><td>Reputation mechanisms</td></tr><tr><td>40</td><td>Jiang et al. (2014)</td><td>Degree of cooperation and knowledge sharing</td><td rowspan="2">Evolutionary game rule (1); social network structure (3)Communication competence (4); social network centralities (3)Recipient trust (2); centrality (3); tenure (4); perceived expertise (5); strength of ties (3)</td><td>Experiment</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>41</td><td>Jo et al. (2014)</td><td>Learning outcomes</td><td>Social network analysis/ survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>42</td><td>Kang &amp; Hau (2014)</td><td rowspan="2">Knowledge transfer Distribution of Knowledge roles (knowledge owners and providers)</td><td rowspan="3">User-cluster (6)Recommendationsprecision (6)Role in software development(4); project phase (1)</td><td>Survey</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>43</td><td>Kim et al. (2014)</td><td>Case study</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>44</td><td>Li et al. (2014)</td><td>Learning effectiveness</td><td>Experiment</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>45</td><td>Licorish &amp; MacDonell (2014)</td><td rowspan="3">Knowledge sharing Motivation, self-efficacy, and opennessof sharingPersonal and collective dimensions of knowledge articulation</td><td rowspan="3">Self-construal relationships (2)</td><td>Social network Analysis</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>46</td><td>Liu &amp; Rau (2014)</td><td>Experiment</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>47</td><td>Razmerita et al. (2014)</td><td>Literature review</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>48</td><td>Tseng &amp; Kuo (2014)</td><td rowspan="4">Knowledge-sharing behaviorsMotivation to produce UGC Innovative knowledge sharingSMN use</td><td rowspan="4">Self-efficacy (5); performance expectations (5); prosocial attitude (4); strength of ties (3)Enjoyment of UGC (4); trust (2); competence (4); and autonomy (4)Role Orientation (4) (Internal versus External)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>49</td><td>Wang &amp; Li (2014)</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>50</td><td>Dolfsma (2015)</td><td>Case study</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>51</td><td>Chin et al. (2015)</td><td>Case study</td><td>X</td><td>X</td><td></td><td></td><td></td></tr></table>

Table 1. Continued  
© 2016 John Wiley & Sons Ltd, Information Systems Journa

<sub>enotes</sub> <sub>perceptua</sub>l <sub>factors</sub>. <sub>And</sub> <sub>(6)</sub> <sub>denotes</sub> <sub>factors</sub> <sub>that</sub> <sup>do</sup> <sup>not</sup> <sup>be</sup>l<sup>ong</sup> <sup>to</sup> <sup>any</sup> <sup>of</sup> <sup>the</sup> <sup>ment</sup> ,,,,<sup>(</sup>, <sub>tor</sub> <sub>shown</sub> i<sub>n</sub> <sub>parenthes</sub>i<sub>s</sub> <sub>next</sub> <sub>to</sub> i<sub>t</sub>. <sub>(1)</sub> <sub>Denotes</sub> <sub>organ</sub>i<sub>zat</sub>i<sub>ona</sub>l <sub>facto</sub><sup>rs</sup>. <sup>(2)</sup> <sup>Denotes</sup> <sup>soc</sup>i<sup>a</sup>l <sup>re</sup>l<sup>at</sup>i<sup>onsh</sup>i<sup>p</sup> <sup>factors</sup>. <sup>(3)</sup> <sup>Denotes</sup> <sup>network</sup> <sup>pos</sup>i<sup>t</sup> , <sub>on</sub> <sub>know</sub>l<sub>edge</sub> <sub>se</sub>e<sup>k</sup>i<sup>ng</sup> <sup>know</sup>l<sup>edge</sup> <sup>shar</sup>i<sup>ng</sup> <sup>or</sup> <sup>both</sup> <sup>as</sup> <sup>the</sup> <sup>dependent</sup> <sup>var</sup>i<sup>ab</sup>l<sup>e</sup> <sup>each</sup> i<sup>nfluenc</sup>i<sup>ng</sup> <sup>factor</sup> i.<sup>e</sup>. i<sup>ndependent</sup> <sup>var</sup>i<sup>ab</sup>l<sup>e)</sup> i<sup>s</sup> <sup>c</sup>l<sup>as</sup> <sub>ab</sub>l<sub>e</sub> <sub>are</sub> li<sub>sted</sub> <sub>chrono</sub>l<sub>og</sub>i<sub>ca</sub>ll<sub>y</sub> <sub>w</sub>i<sub>th</sub> <sub>stud</sub>i<sub>es</sub> <sub>fro</sub>m <sup>the</sup> <sup>same</sup> <sup>year</sup> <sup>be</sup>i<sup>ng</sup> li<sup>sted</sup> i<sup>n</sup>

<table><tr><td colspan="2">Study*</td><td>Dependent variable/Focus</td><td>Independent variable**</td><td>Method</td><td>Knowledge seeking</td><td>Knowledge sharing</td><td>Knowledge diffusion</td><td>Knowledge roles</td><td>Reputation mechanisms</td></tr><tr><td>52</td><td>Chung et al. (2015)</td><td>Travel information adoption</td><td rowspan="3">Technological, organizational (1); social (2) and individual factors (4)Argument quality (5); perceived usefulness (5); source credibility (2); and social relationships (2)Sociability (2), knowledge contribution beha-viors (4), and structural social capital (2)Relational deposits (3) (i.e. network and valued network centralities); withdrawals (3) (i.e. network and valued network densities); reward systems (1)</td><td rowspan="2">Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>53</td><td>Faraj et al. (2015)</td><td>Leadership of online community</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>54</td><td>Lin &amp; Lo (2015)Makkonen &amp;</td><td>Knowledge sharing</td><td>Survey</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>55</td><td>Virtanen (2015)Wanberg</td><td>Productivity</td><td rowspan="3">Knowledge sharing patternsNetwork capacity (3);homophily (2)Online activity (6);emotions (4) reciprocity (2)</td><td rowspan="2">Case studySocial networksanalysis</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>56</td><td>et al. (2015)</td><td>Knowledge sharing</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>57</td><td>Wu et al. (2015)</td><td>Knowledge sharing</td><td>SurveySocial networksanalysis</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>58</td><td>Xu et al. (2015)</td><td>Knowledge sharingDesign of a reputation mechanism</td><td>Health role similarity (2)</td><td>Analysis</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>59</td><td>Yang et al. (2015)Number of articles examining each aspect</td><td></td><td>NA</td><td>Design science</td><td></td><td>X</td><td></td><td></td><td>X</td></tr><tr><td></td><td>Percentage (out of the 59 articles)</td><td></td><td></td><td></td><td>11</td><td>51</td><td>0</td><td>8</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>18.64%</td><td>86.44%</td><td>0.00%</td><td>13.56%</td><td>3.39%</td></tr></table>

l<sub>e</sub> <sub>1</sub>. C<sup>ont</sup>i<sup>nu</sup>

knowledge seeking in SMNs. Moreover, we could not identify any articles that focus on knowledge diffusion in SMNs.

At the micro-level, a plethora of studies focused on investigating the participation of users in knowledge seeking as well as knowledge sharing activities. These studies focus on several categories of variables affecting knowledge sharing and seeking. First, some studies identify the effects of organizational factors. More speci<sup>fi</sup>cally, the presence of organizational rewards, such as salary raises, bonuses and opportunities for promotions (Aalbers et al., 2013; Quigley et al., 2007) as well as the presence of leadership and management support for KM initiatives (e.g. Faraj et al., 2015) lead to favourable attitudes among users toward engagement in knowledge exchange activities. Second, several studies focus on the effects of the nature of social relationships among network members. Social relationships are re<sup>fl</sup>ected in multiple dimensions that in<sup>fl</sup>uence engagement in knowledge exchange activities, such as trust between network members (Quigley et al., 2007; Staples & Webster, 2008; Hsu & Chang, 2014), the norms governing network members interactions and reciprocity (Chang & Chuang, 2011; Beck et al., 2014; Wu et al., 2015) and the strength of ties connecting network members (Chiu et al., 2006; Tseng & Kuo, 2014). Third, the participants’ network structure and their positions in the knowledge exchange networks also play an in<sup>fl</sup>uential role (Brown et al., 2013; Jiang et al., 2014; Wanberg et al., 2015). Fourth, a host of individual differences among users were found to in<sup>fl</sup>uence participation in knowledge exchange activities. They include users’ enjoyment of knowledge exchange (Wasko & Faraj, 2005; Marett & Joshi, 2009; Aalbers et al., 2013), affect toward knowledge exchange (Bateman et al., 2011; Wu et al., 2015), habit of knowledge exchange (e.g. He & Wei, 2009), level of expertise and reputation (Marett & Joshi, 2009; Wasko et al., 2009; Kang & Hau, 2014). Furthermore, perceptual beliefs such as outcomes expectations (Lin et al., 2009; Chen & Hung, 2010; Tseng & Kuo, 2014) and self-ef<sup>fi</sup>cacy (Hsu et al., 2007; Quigley et al., 2007, 2014; Oh, 2012) shaped participation in knowledge seeking and knowledge sharing activities.

However, as ‘knowledge diffusion’ column indicates in Table 1, factors that lead to spread of knowledge across the SMN have received minimal empirical attention. The phenomenon of spread of content across a network is regarded as diffusion in the social network literature (e.g. Borgatti & Cross, 2003). While users’ behaviour of seeking and sharing knowledge eventually leads to its diffusion in a SMN, the diffusion literature suggests that it is not a simple aggregation of individual actions (Macy & Willer, 2002). This logic is best captured by Macy & Willer’s (2002, p. 143–144) following analogy:

Consider a <sup>fl</sup>ock of geese <sup>fl</sup>ying in tight formation. Collectively they form the image of a giant delta-shaped bird that moves as purposively as if it were a single organism. Yet the <sup>fl</sup>ock has no “group mind” nor is there a "leader bird" choreographing the formation (Resnick, 1997). Rather, each bird reacts to the movement of its immediate neighbors who in turn react to it. The result is the graceful dancelike movement of the <sup>fl</sup>ock whose hypnotic rhythm is clearly patterned yet also highly nonlinear.

Knowledge diffusion, as a network-level phenomenon, is similar to the collective delta shaped image of the <sup>fl</sup>ock, but it emerges through the individual acts of seeking and sharing knowledge in a non-linear fashion. In a similar fashion, Guechtouli et al. (2013, p. 50) distinguish knowledge diffusion as a phenomenon from the knowledge-related individua interactions:

The process of knowledge transfer within a community is considered as complex: it is a local phenomenon (interactions among agents) with consequences at the level of the community as a whole (diffusion). In that sense, everything that shapes the interactions and anything that de<sup>fi</sup>nes what agents know of the others and who they can interact with, has a huge impact on the dynamics of knowledge diffusion. Facing complexity, there is not simple and direct correspondence between regularities observed at the individual leve and the global level and human is almost unable to predict consequences of the local mode at the global scale.

Because the network-level pattern of knowledge diffusion is not directly deducible from individual acts of knowledge seeking and knowledge sharing, additional studies are required to unfold how knowledge spreads throughout SMNs within organizations.

## Knowledge diffusion

To better understand knowledge diffusion in SMNs, we draw upon the general literature on knowledge diffusion that is mostly developed in the context of face-to-face networks (F2FNs) This literature primarily concerns factors that in<sup>fl</sup>uence extent and speed of diffusion in a network of inter-related individuals (e.g. March, 1991) or organizations (e.g. Ernst & Kim, 2002). Diffusion is described as a network-level phenomenon emerging from interactions among actors in the network (Abrahamson & Rosenkopf, 1997; Macy & Willer, 2002). Interindividual interactions that lead to diffusion of knowledge are knowledge seeking, i.e. asking a presumably knowledgeable individual about his/her knowledge (Borgatti & Cross, 2003), and knowledge sharing, i.e. disseminating knowledge to others, at its core processes (Cross et al., 2001; Bock et al., 2005). Because knowledge diffusion is shaped from individual-leve knowledge seeking and knowledge sharing, it is described as an emergent bottom-up phenomenon. Macy & Willer (2002) describe knowledge diffusion as a global pattern that is generated by knowledge seeking and sharing interactions among individuals in the network.

Knowledge traverses a network in a sequential fashion such that knowledge is obtained from those who have it and is learned by those who do not, with the learned knowledge being then passed to others in the network (Abrahamson & Rosenkopf, 1997). Hence, the <sup>fi</sup>rst condition for successful diffusion of knowledge is the possibility for smooth traverse of knowledge in the network. The more easily knowledge can be passed along in the network, the greater would be its diffusion. Although this condition is necessary for successful knowledge diffusion, it is not suf<sup>fi</sup>cient. Individual knowledge can vary in value; that is, while some individuals hold true beliefs, others can hold false beliefs, and they are distinguishable from those who do not holo any beliefs. Successful knowledge diffusion happens only when those holding true beliefs pass their knowledge to those who do not hold any belief on a certain topic. Thus, the second condition for successful knowledge diffusion is the possibility for extraction and elicitation o ‘true beliefs’ in the network.<sup>4</sup> This condition complements the <sup>fi</sup>rst and ensures the spread of sound knowledge within an organization. In other words, neither is suf<sup>fi</sup>cient by itself.

The general literature on knowledge diffusion has mostly focused on the <sup>fi</sup>rst condition and has identi<sup>fi</sup>ed some factors that facilitate smooth traverse of knowledge (f1), such as tie strength (Hansen, 1999), structure of local networks (Bala & Goyal, 1998) and topology of the global network (Cowan & Jonard, 2004). For example, Mu et al. (2010) show that compared with hierarchical networks, a scale-free network topology is more effective in transferring knowledge in a network. Some other studies have focused on the second condition and identi<sup>fi</sup>ed factors that facilitate better extraction of true beliefs (f2). These studies point to factors such as the learning rate of individuals (March, 1991; Miller et al., 2006), and the presence of transactive memory (e.g. Oshri et al., 2008) as factors that in<sup>fl</sup>uence extraction of true beliefs in a network. For example, March (1991) notes that lower learning rates leads to greater exploration in the network, which in turn leads to higher extraction of true beliefs. Table 2 summarizes the <sup>fi</sup>ndings of the general literature on knowledge diffusion.

## THEORETICAL DEVELOPMENT

## Knowledge diffusion in SMNs

Although the literature on knowledge diffusion in F2FNs has contributed to our understanding as well as the advancement of KM in modern organizations, it did little to inform research and practice about SMN-speci<sup>fi</sup>c factors that facilitate: smooth traverse of knowledge (f1) and better extraction of true beliefs (f2). Despite some similarities with conventional F2FNs, SMNs have a number of distinct characteristics. To start with, both F2FNs and SMNs rely on interpersonal ties among individuals to distribute knowledge in the network in a decentralized fashion (Borgatti & Cross, 2003), but the nature and reach of ties are different. To add, F2FNs operate through interpersonal ties, often shaped through social and work-related similarities among colleagues (e.g. Contractor et al., 2006), whereas SMNs rely on electronic ties, which expand beyond ties to familiar colleagues and enable access to strangers. Further, SMNs involve technological features that can explicitly and precisely re<sup>fl</sup>ect the knowledge map of the network, whereas in F2FNs, such knowledge maps exist only implicitly and perceptually among the network actors (e.g. Austin, 2003; Kane et al., 2014). For example, SMNs explicitly draw the boundaries of knowledge through segmenting the network into knowledge topics (e.g. Li et al., 2014). Also, SMNs can form a precise history of users’ actions and re<sup>fl</sup>ect them through explicit signals, such as users’ contribution status (e.g. Kim & Sundar, 2011). Thus, SMNs as KM tools represent niche contexts of knowledge diffusion with idiosyncratic characteristics worthy of serious investigation.

In an effort to extend the literature on knowledge diffusion in SMNs, we shed light in the rest of this section on the characteristics that are speci<sup>fi</sup>c to SMNs and can potentially in<sup>fl</sup>uence knowledge diffusion. Speci<sup>fi</sup>cally, we discuss two of SMN’s distinct characteristics, i.e.

Table 2. Summary of the general literature on knowledge diffusion

<table><tr><td></td><td>Factors influencing knowledge diffusion</td><td>Instances</td><td>Citations</td></tr><tr><td rowspan="5">Facilitating smooth transfer of knowledge (f1)</td><td>Inter-individual tie strength</td><td>The frequency of interactions among individualsThe multiplexity of network ties</td><td rowspan="2">Hansen (1999); Reagans &amp; McEvily (2003); Singh (2005); Ozel (2012); Liu et al. (2015)Bala &amp; Goyal (1998);Abrahamson &amp; Rosenkopf (1997); Rodan (2008); Gao &amp; Guan (2012);Guechtouli et al. (2013);Licerish &amp; MacDonell (2015);Chen &amp; Guan (2016)Ellison &amp; Fudenberg (1995);Deroian (2002); Amblard &amp; Deffuant (2004);Cowan &amp; Jonard (2004);Delre et al. (2004);Stauffer &amp; Sahimi (2005);Tang et al. (2006); Delre et al. (2007);Tang et al. (2008); Kim &amp; Park (2009);Lin &amp; Li (2010); Zappa (2011);Choi et al. (2013)</td></tr><tr><td>Structure of local networks</td><td>Core-peripheral formation of ties in central areas of networkNeighbor network&#x27;s structure</td></tr><tr><td>Topology of the global network</td><td rowspan="3">Hierarchy of networkSmall-world resemblance of networkScale-free resemblance of networkAbsorptive capacity of individuals in a networkThe average probability of learning knowledge from a knowledge source in a networkShared mental map of know-who in a network</td><td rowspan="3">March (1991); Tsai (2001);Giani et al. (2005); Miller et al. (2006);Kane &amp; Alavi (2007); Mu et al. (2010);Liu et al. (2011); Wang et al. (2015)Lewis et al. (2005); Oshri et al. (2008);Wang et al. (2015)</td></tr><tr><td>Learning rate of individuals</td></tr><tr><td>Transactive memory</td></tr></table>

reputation mechanisms (affecting knowledge diffusion through $\mathbf { f } 2 ) ^ { 5 }$ and presence of distinct knowledge roles (affecting knowledge diffusion through f1), and explain how they can affect knowledge diffusion. Our review of the existing literature, summarized in Table 1, indicates the relevance of reputation mechanisms and distinct knowledge roles to the studies investigating KM and SMNs (3.39% consider reputation mechanisms, while 13.56% consider the presence of distinct knowledge roles); however, none of these studies have investigated the in<sup>fl</sup>uence of reputation mechanisms and knowledge roles simultaneously in driving knowledge diffusion. In the following sections, we explain the mutual and interdependent relevance of these two factors to knowledge diffusion and discuss how by focusing on the two our understanding about the way that knowledge diffusion happens in SMNs extends.

## Reputation mechanisms

Reputation mechanisms are recognized in the extant literature as important and distinct feature of SMNs (e.g. Aberer & Despotovic, 2001; Chen et al., 2007; Rahbar & Yang, 2007; Kane et al., 2014). The importance of reputation mechanisms could be attributed to their role in the construction of SMNs user’s digital pro<sup>fi</sup>le, a core feature that distinguishes SMNs from F2FNs (Ellison & Boyd, 2013; Kane et al., 2014). A user’s digital pro<sup>fi</sup>le is unique and constructed by the user, the members of the user’s network and by the network platform (Kane et al., 2014). Platform designers implement certain features such as reputation mechanisms to aid in the con struction of a consistent identity for the user within SMN. Kane et al. (2014, p. 289) emphasize:

“The user’s identity in the network may be supported by reputation mechanisms that explicitly record his or her activity in the network, such as when online communities explicitly identify the most proli<sup>fi</sup>c or helpful contributors.”

Social media platforms, de<sup>fi</sup>ned as tools that enable users to build a unique pro<sup>fi</sup>le and publish text, images, video and other shareable media (Fernandez, 2014), utilize signals of individuals’ reputation in order to re<sup>fl</sup>ect their trustworthiness (Resnick et al., 2000). In the KM context, such signals re<sup>fl</sup>ect knowledgeability of individuals (Havakhor & Sabherwal, 2013) and provide a tool that broadcasts the know-who information to actors. Borgatti & Cross (2003) contend that information about know-who is required for knowledge seeking to occur. While the information about know-who resides in the transactive memory of F2FNs (Liang et al., 1995; Oshri et al., 2008), social media platforms provide explicit tangible mechanisms to provide this information. Through signalling knowledgeability of individuals, reputation signals are the main mechanism of SMNs to ensure true beliefs are obtained and distributed in the networks.

Reputation mechanisms vary in how they operate. Two main types of reputation signals exist in social media platforms. The first type includes social media reputation signals based on feedback mechanisms (Friedman et al., 2007). In the context of KM, this means that the knowledgeability of an actor is rated by knowledge recipients and those feedbacks accumulate to re<sup>fl</sup>ect the overall knowledgeability. We call such reputation mechanisms adaptive mechanisms because they change adaptively as individuals seek and share knowledge. The value of these reputation mechanisms depends on the patterns of knowledge seeking and sharing up to that point, with low levels of prior knowledge seeking and sharing implying less information for these mechanisms to be useful. If individuals who are asked questions do provide answers, adaptive reputation mechanisms would be based on greater information and therefore offer more value. By contrast, a knowledgeable individual might be overlooked if that individual is either not asked enough questions to accumulate ratings or if that individual has not shared knowledge despite being asked, because no feedback is generated in either case. Thus, knowledge seeking and sharing among individuals enable reputation scores to build up as needed for this type of reputation mechanisms.

Another type of reputation signals are those that are independent of network feedbacks. Havakhor & Sabherwal (2013) refer to this type as objective mechanisms. For example, the number of code lines that a programmer has contributed to an open-source software project can be utilized as an objective reputation signal for the programmer in an online community of open source developers. Such a reputation signal has not emerged adaptively and endogenously as a result of knowledge seeking and sharing in the SMN itself; instead, it is objectively and exogenously solicited from outside the SMN’s boundaries. Because such signals are generated exogenously, they do not depend on knowledge seeking and sharing among individuals. Sources of knowledge will be identi<sup>fi</sup>ed as a knowledgeable, even if they have not shared their knowledge or been approached by others.

So far, we have highlighted that the reputation mechanism used in a SMN represents a SMN-speci<sup>fi</sup>c factor that facilitates better extraction of true beliefs (f2). We argue that it is tied to the second condition of knowledge diffusion as reputation mechanisms enable the identi<sup>fi</sup>cation of those holding true beliefs in the network and hence, foster better extraction of true beliefs in SMNs. Thus, we propose:

P1: Type of the reputation mechanism affects the extent of knowledge diffusion in a SMN.

While design of reputation mechanisms has been in the SMN research’s spotlight, they alone cannot guarantee diffusion of knowledge. In other words, although satisfying the second condition of knowledge diffusion is necessary, it is not suf<sup>fi</sup>cient. Rather, such designs should be studied, while considering SMN-speci<sup>fi</sup>c factors that facilitate smooth traverse of knowledge, thereby taking into account the <sup>fi</sup>rst and second conditions simultaneously. Therefore, in the next section, we discuss a SMN-speci<sup>fi</sup>c factor that facilitates smooth traverse of knowledge.

## Distinct knowledge roles

The literature on knowledge diffusion assumes that that all actors in a network follow the same logic while exchanging knowledge: (a) they seek knowledge when they lack it and (b) they share knowledge if they possess the acquired knowledge (e.g. March, 1991; Miller et al., 2006; Kane & Alavi, 2007; Liao & Wang, 2010; Kunz, 2011). Thus, individuals are assumed to be homogeneous in their tendency to share and seek knowledge. However, studies on SMNs show lack of homogeneity in individuals’ tendency to share and seek knowledge. Particularly, empirical evidence points to presence of three distinct knowledge roles in SMNs with varying tendency to share and seek knowledge (e.g. Welser et al., 2007; Zhang et al., 2007; Adamic et al., 2008; Nam et al., 2009). These distinct knowledge roles include: seekers, i.e. those who mainly seek knowledge and rarely share it; contributors, i.e. those who mainly share knowledge and rarely seek it; and brokers, i.e., those who seek and share knowledge in a balanced fashion (Drew et al., 2013). For example, Nam et al. (2009, p. 783) report on the presence of these distinct knowledge roles as follows:

… the users are largely divided into askers [i.e., seekers] and answerers [i.e., contributors], with only 5.4% both asking and answering [i.e., brokers].

The presence of distinct knowledge roles in SMNs is recognized in the extant literature (e.g. Gray, 2004; Ridings et al., 2006; Marett & Joshi, 2009). Further, empirical research shows the presence of different distributions of these roles in SMNs. For example, while Nam et al. (2009) <sup>fi</sup>nd a distribution with high presence of both seekers and contributors with low presence of brokers, Adamic et al. (2008) report a relatively more balanced presence of seekers, contributors and brokers, where their

… dataset includes 8,452,337 answers to 1,178,983 questions, with 433,402 unique repliers and 495,414 unique askers. Of those users, 211,372 both asked and replied. These numbers are already a hint to the diversity of user behavior in YA [Yahoo] (p.667).

The above roughly translates into 40% seekers, 31% contributors and 29% brokers. We discuss that distribution of knowledge roles in SMNs can be a factor influencing knowledge diffusion. Speci<sup>fi</sup>cally, we focus on distribution of knowledge roles for two reasons: (a) presence of distinct knowledge roles is a prevalent observed pattern in SMNs and thus focusing on it informs potential adopters of SMNs about its potential outcomes and (b) it has theoretical merit as it directly relates to the <sup>fi</sup>rst condition of knowledge diffusion; certain distributions of knowledge roles better facilitate knowledge traverse in SMNs. The presence of seekers, contributors and brokers, can present some bene<sup>fi</sup>ts and some drawbacks for smooth traverse of knowledge in SMNs. More precisely, ‘seekers’, with their greater tendency to seek knowledge compared with those in the other two roles, help obtain knowledge from experts. However, because of their relatively lower tendency to share knowledge, they are less effective in passing the acquired knowledge to others in the network. Conversely, ‘contributors’, with their greater tendency to share knowledge, can be effective in contributing knowledge, but they may not have acquired others’ knowledge themselves because of their lower knowledge seeking. Finally, ‘brokers’ do not obtain knowledge from the knowledgeable individuals as well as is performed by ‘seekers’ and are less effective in contributing knowledge compared with ‘contributors’, but they can maintain a balanced approach in both sharing and seeking knowledge, thereby performing an important mediating role in knowledge diffusion. Table 3 summarizes this trade-off associated with the three knowledge roles.

The above trade-off between knowledge seeking and sharing in different knowledge roles prevalent in SMNS presents a non-trivial question about the effect of the distribution of knowledge roles on the way knowledge traverses in a network: which distributions maintain a smoother traverse of knowledge? We highlight distribution of knowledge roles as a SMN-speci<sup>fi</sup>c factor that in<sup>fl</sup>uences smooth traverse of knowledge (f1). Thus, we propose:

P2: Distribution of knowledge roles affects knowledge diffusion in a SMN.

## Interdependence of reputation mechanisms and distribution of knowledge roles

Aligned with the theories of knowledge diffusion, we discuss that the effect of reputation mechanisms is inter-related with the effect of distribution of knowledge roles. By contrast, the distribution of knowledge roles changes the way that knowledge traverses in the network, and on the other hand, determining individual reputation scores can depend on the way that knowledge traverses the network, especially in the case of adaptive systems with their effectiveness being sensitively dependent on patterns of knowledge seeking and knowledge sharing among individuals. Further, underlying theories of knowledge diffusion suggest that both conditions are needed to maintain the success of knowledge diffusion. This interdependent relationship calls for coordinated consideration of reputation mechanisms and distribution of knowledge roles in SMNs. Hence, we study the interdependent role of reputation mechanisms and distribution of knowledge roles in affecting knowledge diffusion in SMNs. We propose (Figure 1):

Table 3. Knowledge Seeking and Knowledge Sharing across Knowledge Roles in SMN

<table><tr><td></td><td>Seekers</td><td>Brokers</td><td>Contributors</td></tr><tr><td>Knowledge seeking</td><td>High</td><td>Medium</td><td>Low</td></tr><tr><td>Knowledge sharing</td><td>Low</td><td>Medium</td><td>High</td></tr></table>

P3: The effect of knowledge role distribution on knowledge diffusion in a SMN changes with the type of reputation mechanism.

## Methods

Agent-based simulation is regarded as a viable technique that enables theorization about bottom-up emergent processes (Harrison et al., 2007) such as knowledge diffusion. Research on diffusion of knowledge in organizations has adopted this method (March, 1991; Miller et al., 2006; Kane & Alavi, 2007) because of its versatility in creating experimentation environments (Nan, 2011). This study requires experimentation conditions where researchers have control over varying distribution of knowledge roles in a network. Network phenomena are hard to replicate in experimental settings and are usually studied through either <sup>fi</sup>eld studies (e.g. Reagans & McEvily, 2003) or simulations (e.g. Bampo et al., 2008). While <sup>fi</sup>eld studies have highexternal validity, complexity arising from interactions of several factors and actions over time is dif<sup>fi</sup>cult to capture in <sup>fi</sup>eld settings (Harrison et al., 2007). More speci<sup>fi</sup>cally, because constituents of knowledge diffusion, knowledge seeking and knowledge sharing, involve considerable time and numerous interactions (Fiol & Lyles, 1985), it is dif<sup>fi</sup>cult to study knowledge diffusion to its full extent in <sup>fi</sup>eld settings. Considering the study’s research question, and following the tradition of research in knowledge diffusion, we conduct a series of agent-based simulations, which address these issues and allow studying the phenomenon of interest over a long period.

![](/api/attachments/5T5SFCC8/fulltext/images/fd2a4d111baf8996a69855f86b66f2eedf902cc9d8eb02665cc2778bd957ab8e.jpg)  
Figure 1. Summarizes the research model that is tested in this study We considered alternative individual-level attributes that can be aggregated up to the network level such as the distribution of intrinsic motivation and extrinsic rewards fo knowledge sharing across individuals in the network, However, we focused on reputation mechanisms and the distributior of knowledge roles because: (a) these aspects seem more central to knowledge seeking and sharing within a network; and (b) aspects such as intrinsic motivation and extrinsic rewards may be indirectly captured by the distribution of knowledge roles.

© 2016 John Wiley & Sons Ltd, Information Systems Journa

## A complex adaptive system model of knowledge diffusion

Following Nan’s (2011) guidelines, a complex adaptive system (CAS) model of knowledge diffusion in SMNs is created. CAS models comprise of two distinct components: agents and interactions among them (Nan, 2011). In our CAS model of knowledge diffusion, agents are members of the network and are attributed with a knowledge set and two probabilities: probability to share knowledge (SHARE) and probability to seek knowledge (SEEK). The knowledge set of agents is defined as a one-by-ten vector of knowledge elements, where each element corresponds to an area of expertise. This is consistent with the previous models of organizational learning, which consider individual knowledge as complex and including several expertise areas (e.g. Kane & Alavi, 2007). Each element can take a value of 1 (true belief), 0 (no belief) or 1 (false belief). This approach is consistent with the current practice in organizationa learning domain where individuals can hold beliefs that are not correct (Miller et al., 2006) and with de<sup>fi</sup>nition of knowledge as ‘individual true beliefs’ (Nonaka, 1994, p. 15). We assume<sup>6</sup> knowledge value of each element to be uniformly distributed in the network.

SHARE and SEEK value for each agent identi<sup>fi</sup>es the probabilities (between 0 and 1) that the agent shares knowledge when is being asked and that the agent seeks knowledge when lacking it, respectively. For each agent, the value of these attributes is determined based on the distribution of roles in the network. In order to create the three categories of seekers, contributors and brokers, we allow SHARE = 1 – SEEK. This formulation allows for seekers td have high probability of seeking and low probability of sharing, contributors to have high probability of sharing and low probability of seeking and brokers to have moderate probabilities of both sharing and seeking. For ‘seekers’, the values of SEEK and SHARE are set at 0.8 and 0.2, respectively, while these values are set at 0.2 and 0.8, respectively, for ‘contributors’.<sup>7</sup> For ‘brokers’, both values are set at 0.5. Consistent with prior suggestions to model communication systems that loosely connect all members of a network (Kane & Alavi, 2008), agents in the network are fully inter-connected through electronic linkages that abstract social media technologies.

Interactions among agents in the network are actions to seek and share knowledge, which follow a <sup>fi</sup>ve-step procedure: (1) The reputation value of all members is visible to every other member in the network. (2) Members acquire knowledge on elements of knowledge that are 0 with the probability of (SEEK), form their neighbor<sup>8</sup> with the highest reputation. (3) Members who are asked questions on a speci<sup>fi</sup>c dimension of their knowledge provide that knowledge to the seeker with probability of (SHARE) and the seeker learns it with no error. (4) In case of adaptive reputation signals, the reputation value of members is updated in two rounds<sup>9</sup> after knowledge accumulation, through a feedback from the individual acquiring knowledge. (5) Individuals change their adopted false beliefs ( 1 values) to 0 after two rounds.<sup>10</sup>

Table 4. Key computations for the CAS mode

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
At each round of the simulation:

- $K_{ij}$ denotes $j$th element of knowledge of individual $i$
- $I_{iz}$ denotes the dummy for occurrence of knowledge sharing between individual $i$ with individual $z$ (1, if the $i$ shares knowledge with $z$)
$\text{Ad}_i = \sum_{z=1}^{n} \sum_{j=1}^{m} K_{ij} * I_{iz}$ Adaptive reputation
$\text{Ob}_i = \sum_{j=1}^{m} K_{ij}$ Objective reputation
At the equilibrium point ($t = T$):
$\text{KD} = \left( \sum_{j=1}^{n} \sum_{j=1}^{m} K_{ij} \right)_{t=T - } \left( \sum_{j=1}^{n} \sum_{j=1}^{m} K_{ij} \right)_{t=0}$ Extent of knowledge diffusion
</div>

As discussed earlier, we introduce two different approaches to reputation mechanisms: adaptive and objective. At each round of the simulation, adaptive reputation signal of each agent is calculated to be the sum of knowledge value transferred from a focal agent to other agents. We assume that each actor provides honest feedback after receiving knowledge from a source. By contrast, the objective reputation mechanism re<sup>fl</sup>ects the sum of the knowledge values for agent’s knowledge vector regardless of whether or not that element of knowledge is being transferred in a transaction. Finally, the extent of diffusion in the network is calculated as the change in the sum of knowledge values of all the actors from the start of the simulation to the equilibrium point. The greater this measure, the higher the spread of true beliefs. Table 4 summarizes the key calculations in the CAS model, whereas Appendix A provides the pseudo-code of our simulated model.

In our experiment, we construct distributions of knowledge roles by varying the percentage of each knowledge role in the network from 0% to 100% with 1% increments. This yields 5050 blocks with 40 replication per block for each of the objective and adaptive reputation mechanisms (404 000 runs in total).

## RESULTS

To test the propositions, we construct two dummies, percentage of ‘seekers’ (Seeker) and percentage of ‘contributors’ (Contributor), while using the percentage of ‘brokers’ as the reference, and analyse the effect of these factors on the extent of knowledge diffusion in the network (Diff, the difference between sum of knowledge values for all agents $( \sum _ { j = 1 } ^ { n } \sum _ { j = 1 } ^ { m } K _ { i j } )$ at the start and end of the simulation). To account for possible non-linear effects, we specify a quadratic model:

$$
\begin{array}{r l} \text { Diff } _ {\mathrm{i}} & = \alpha_ {0} + \beta_ {1} ^ {*} \text { Seeker } _ {\mathrm{i}} + \beta_ {2} ^ {*} \text { Contributor } _ {\mathrm{i}} + \beta_ {3} ^ {*} \text { Seeker } _ {\mathrm{i}} ^ {*} \text { Contributor } _ {\mathrm{i}} \\ & + \beta_ {4} ^ {*} \text { Seeker } _ {\mathrm{i}} ^ {2} + \beta_ {5} ^ {*} \text { Contributor } _ {\mathrm{i}} ^ {2} \end{array}
$$

Table 5. Results of quadratic analysis

<table><tr><td></td><td colspan="2">Direct Effect</td><td colspan="2">Quadratic Effect</td></tr><tr><td>DV = Diff</td><td>Global</td><td>Local</td><td>Global</td><td>Local</td></tr><tr><td>Contributor</td><td>-0.673***</td><td>-0.188***</td><td>-0.781***</td><td>-0.152***</td></tr><tr><td>Seeker</td><td>-0.264***</td><td>-0.127***</td><td>0.116***</td><td>-0.098**</td></tr><tr><td>Seeker * Contributor</td><td></td><td></td><td>-0.613***</td><td>-0.223***</td></tr><tr><td> $Contributor^2$ </td><td></td><td></td><td>-0.167***</td><td>-0.095***</td></tr><tr><td> $Seeker^2$ </td><td></td><td></td><td>-0.338***</td><td>-0.116***</td></tr><tr><td>Constant</td><td>0.910***</td><td>0.428***</td><td>0.912***</td><td>0.425***</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.48</td><td>0.37</td><td>0.64</td><td>0.58</td></tr></table>

\*p < 0.05  
\*\*p < 0.01  
\*\*\*p < 0.001; All variables are mean-centred.  
The quadratic models have a signi<sup>fi</sup>cantly (p < 0.001) higher R<sup>2</sup> compared with a direct effect model with only Contributor and Seeker as inde pendent variables.

![](/api/attachments/5T5SFCC8/fulltext/images/d19932dce46b9fba9a02e18ec4c0e8d90c6234604b30ade3f411adef3624a68b.jpg)

![](/api/attachments/5T5SFCC8/fulltext/images/ab6cd55a231e2bdfbe6c1da0d5c59aa0ed1f603287627f80ac8d7691a43b347f.jpg)  
0-0.1 0.1-02 0.2-03 0.3-0.4 0.4-05 0.5-0.6 0.6-0.7 0.7-0.8 0.8-0.9 0.9-1  
Figure 2. (a) 3D Surface plot of knowledge diffusion<sup>11</sup>: objective reputation. (b) Contour plot of knowledge diffusion: objective reputation.

In the aforementioned model, Diff is the extent of diffusion in ith run, $\alpha _ { 0 }$ is the intercept, Seeker is the percentage of seekers in ith run and Contributor is the percentage of contributors in ith run. We start with a simple direct-effects model where both in objective and adaptive reputation mechanism conditions, the signi<sup>fi</sup>cant and negative coef<sup>fi</sup>cients of Seeker and Contributor in the <sup>fi</sup>rst two columns of Table 5 indicate that replacing brokers with either seekers or contributors decrease knowledge diffusion. Also, a less negative coef<sup>fi</sup>cient for Seeker indicates that compared to contributors, replacing brokers with seekers has less negative effects on knowledge diffusion, We also tested the full quadratic model which outperforms the direct-effects model. The third and fourth columns in Table 5 report the results of regression analysis for runs in block of the objective and adaptive reputation mechanisms, respectively. Figures 2 and 3 present the surface response plots of the two quadratic models.<sup>12</sup> The plots complement the regression results showing that objective reputation mechanisms outperform adaptive ones, providing evidence supporting P1. Also, both plots show that the highest extent of diffusion can be achieved when both the percentage of seekers and contributors is set at zero (i.e. in networks where all the individuals show characteristics of brokers). Further, the negative and signi<sup>fi</sup>cant sign of the quadratic terms suggest that the positive effect of replacing contributors or seekers with brokers decreases as the number of brokers in the network increase. This provides evidence that distribution of knowledge roles in<sup>fl</sup>uence knowledge diffusion in SMNs, supporting P2. Also, as can be inferred from both the tilted shape of the surface and the less negative sign of the Seeker dummy compared with the Contributor dummy, ‘seekers’ contribute more than ‘contributors’ to knowledge diffusion. This is visible in the plots where keeping the percentage of brokers constant (i.e., diagonal cuts to the surface), distributions with higher presence of seekers have more knowledge diffused compared to distributions with more contributors present.

![](/api/attachments/5T5SFCC8/fulltext/images/b3cee5a02087f88fe0a2614af091d2614ab476bf09ab7446aae184998cedc1a9.jpg)  
0-0.10.1-0.20.2-0.30.3-0.4 0.4-0.50.5-0.60.6-0.70.7-0.80.8-0.90.91

![](/api/attachments/5T5SFCC8/fulltext/images/c696914286edf00e043f9677317425ee93edf69f5dd1024f7bc2bdbae10fc79f.jpg)  
Figure 3. (a) 3D Surface plot of knowledge diffusion: adaptive reputation. (b) Contour plot of knowledge diffusion: adaptive reputation.

Table 6. Summary of knowledge role distributions

<table><tr><td>Knowledge role distribution</td><td>Proportion of seekers (%)</td><td>Proportion of contributors (%)</td><td>Proportion of brokers (%)</td></tr><tr><td>Normal</td><td>L (16.7)</td><td>L (16.7)</td><td>H (66.6)</td></tr><tr><td>Uniform</td><td>M (33.3)</td><td>M (33.3)</td><td>M (33.3)</td></tr><tr><td>PowerHSEE</td><td>H (80)</td><td>L (20)</td><td>-</td></tr><tr><td>EqualSHSEE</td><td>M (50)</td><td>M (50)</td><td>-</td></tr><tr><td>PowerHSH</td><td>L (20)</td><td>H (80)</td><td>-</td></tr></table>

In order to further explore the <sup>fi</sup>ndings, we focus on <sup>fi</sup>ve distinct distributions of knowledge roles and examine their diffusion plots. These <sup>fi</sup>ve distributions are Normal, Uniform, powerlaw with high presence of seekers (PowerHSEE), power-law with high presence of contributors (PowerHSH) and a distribution with equal presence of seekers and distributors (EqualSHSEE). Table 6 presents these distributions de<sup>fi</sup>ned by the proportion of each knowledge role.

Diffusion, as a phenomenon, can be examined by plotting its trajectory (March, 1991; Kane & Alavi, 2007). Because of our focus in knowledge diffusion, we plot the trajectory of overall knowledge-calculated as the sum of individual’s knowledge values $( \sum _ { j = 1 j = 1 } ^ { n } \sum _ { K _ { i j } ) } ^ { m } ( \sum _ { j = 1 } ^ { n } K _ { i j } )$ – from the start of

the simulation to where it reaches a steady point, a point after which no variation happens in the extent of the overall knowledge. In order to study the effect of distribution of knowledge roles on knowledge diffusion, we <sup>fi</sup>rst combine the results for adaptive and objective reputation mecha nisms and present the overall results. Figure 4 presents plots of the knowledge diffusion trajectories for the <sup>fi</sup>ve distributions of knowledge roles. In the <sup>fi</sup>rst set of results, comparing the Normal and Uniform distributions indicates that a normal distribution of knowledge roles leads to greater knowledge diffusion. By contrast, comparison of the PowerHSH, PowerHSEE and EqualSHSEE distributions indicates that the distribution with dominant presence of seekers (PowerHSEE) outperforms the other two. Also, it is shown that an equal presence of seekers and contributors out performs a skewed situation where contributors are dominant. Further, the results show that in a PowerHSEE distribution, the absence of brokers is compensated by high presence of seekers to a level that it reaches the knowledge diffusion extent of a uniform distribution. Overall, norma distribution performs the best in terms of diffusion, followed by uniform and PowerHSEE distribu tions being about the same, followed by EqualSHSEE, with PowerHSH performing the worst.

Figures 5 and 6 present the trajectories of knowledge diffusion in platforms with objective and adaptive reputation mechanisms. Aside from the considerable superiority of objective mecha nisms compared with adaptive signals, the trend of results in the objective cell (Figure 5) is consistent with the overall results. That is, Normal distribution outperforms the Uniform distribution of knowledge roles. Similarly, PowerHSEE outperforms the PowerHSH and EqualSHSEE and performs similar to the Uniform distribution. This trend is almost replicated in adaptive mechanism cell with two differences. First, the diffusion extent for EqualSHSEE and PowerHSH becomes comparably similar. This is contrary to the pattern in the other cell where EqualSHSEE outperforms the PowerHSH. Further, in the adaptive mechanism cell, the PowerHSEE does not perform as well as a uniform distribution, unlike their similar performance

![](/api/attachments/5T5SFCC8/fulltext/images/3c93786169806ee3ee7eba6049ee856816ed6550565c36c25199542e80f6fd7a.jpg)  
Figure 4. Extent of diffusion for knowledge role distributions

![](/api/attachments/5T5SFCC8/fulltext/images/595197d0edffce13c7a0e6e38533be75d78eb393f202db8e8956d633a82c270a.jpg)  
Figure 5. Extent of diffusion for knowledge role distributions: objective reputation.

![](/api/attachments/5T5SFCC8/fulltext/images/643a909d92eafaa8b4601a4a8c46c0bdf5143fe672f9136c2434b0f15f0e460e.jpg)  
Figure 6. extent of diffusion for knowledge role distributions: adaptive reputation.

overall and in the objective mechanism cell. Hence, our results suggest that reputation mechanisms can change the way that distributions of knowledge role affect knowledge diffusion, providing evidence for P3.

Taken together, these results provide evidence that guides us in building a theory about the effects of distribution of knowledge roles and the kind of reputation mechanisms on knowledge diffusion. Appendix B describes the process used to validate our simulation model.

## DISCUSSION

This study investigates the interdependent effect of reputation mechanisms and distribution of knowledge roles on knowledge diffusion in SMNs. With their distinct tendencies for seeking and sharing knowledge, seekers, contributors and brokers play distinctly different roles in knowledge diffusion in SMNs. Because of their greater tendency to seek knowledge, seekers help obtain knowledge, whereas contributors, with their greater tendency to share knowledge, help distribute it. Between these two roles, brokers, tend to perform both these actions to some extent, thus acquiring and passing knowledge from one part of network to another, and bridging the gap between seekers and contributors (Lavis, 2006). In fact, they facilitate a smoother tra verse of knowledge in the network.

Consistently, our results demonstrate the importance of knowledge brokers, who bridge between knowledge contributors and knowledge seekers, in SMNs. Moreover, the results of this study indicate that a high proportion of knowledge seekers can offset the lack of brokers in the network to the extent that the diffusion of the PowerHSEE distribution is almost as high as a uniform distribution where knowledge brokers are present in a high proportion. These results re<sup>fl</sup>ect the importance of knowledge seeking when SMNs are used for knowledge diffusion within organizations, suggesting that a skewed composition with high presence of seekers is as effective as a balanced composition where seekers, contributors and brokers are present in equal proportions. Consistent with the greater importance of knowledge brokers followed by knowledge seekers, increasing the presence of contributors has the least effect on knowledge diffusion. These results, compared with the described power of seekers, suggest a differential importance of knowledge seeking and knowledge sharing with respect to knowledge diffusion.

Thus, our results indicate that knowledge seekers play a more important role than knowledge contributors in diffusing knowledge across networks of individuals. One possible explanation for this somewhat surprising <sup>fi</sup>nding is that under high proportion of contributors, there are few seekers in the network to exploit the network in order to source true beliefs; instead, the few seekers may end up in a myopic early adoption of potentially untrue beliefs. Further, a high presence of contributors implies that less knowledge acquisition occurs in most parts of the network. Our <sup>fi</sup>ndings pertaining to the importance of knowledge seekers resonate with suggestions of KM researchers who had called for greater attention to seekers’ (e.g. Huber, 2001; Wiig, 2003) highlighting their potential importance in statements such as the following:

The key to [KM] success is the recipient, because he alone determines whether or not the information will be accessed and utilized (Davy, 2006, p. 18)

Our results also highlight the interdependent role that distribution of knowledge roles and reputation mechanisms play in shaping knowledge diffusion in SMNs. The results indicate that the importance of knowledge role distribution diminishes when using adaptive reputation mechanisms. The peak of surface plots for objective reputation mechanisms rest at higher point compared with the adaptive plot. Further, while in a situation where objective mechanisms of reputation are used the extent of diffusion almost doubles moving from uniform to normal distribution, the improvement in platforms with adaptive reputation mechanisms drops to less than 30%. Similarly, the results show that when adaptive reputation mechanisms are used, the difference between the diffusional diffusion of PowerHSEE and PowerHSH almost disappears.

As discussed earlier, adaptive reputation mechanisms are highly sensitive to the patterns of knowledge seeking and knowledge sharing. It appears that these feedback-based mechanisms become inferior when knowledge sharing decreases in the network. Unless individuals share their knowledge, their reputation remains unrated and that can lead to relatively blind search for knowledge in the network. Thus, drawback of the PowerHSEE distribution in an adaptive environment is that the lack of knowledge sharing in the network dampens the ef<sup>fi</sup>ciency of the know-who system. This, in turn, leads to decreased diffusion in such distributions. Because of this problem, in adaptive environments, PowerHSEE distribution loses its comparability to uniform distribution and cannot compensate for the relative lack of knowledge brokers.

## Limitations and future research

The <sup>fi</sup>ndings of this study should be viewed in the light of its several limitations, in addition to the inherent limitation of an agent-based simulation approach, which simpli<sup>fi</sup>es complex microbehaviours to theorize about the macro-level phenomenon (Macy & Willer, 2002). First, our effort to build a simulated reality that does not violate known rules of micro-behaviour led us to limit variations in individual behaviour into three distinct knowledge roles. While our focus is primarily motivated by the prevalence of these categories in SMNs, we acknowledge that other knowledge roles may exist in SMNs that can potentially affect knowledge diffusion. For example, in addition to these three roles, literature on SMNs identi<sup>fi</sup>es lurkers, i.e. individuals who do participate in neither knowledge seeking nor knowledge sharing. Instead, they only passively observe and follow knowledge seeking and sharing (Lai & Chen, 2014). A possible extension to this work can be the introduction of lurkers to the network and experiment over their co-presence with the three knowledge roles discussed in this study.

Second, prior literature on personal characteristics points to factors such as self-esteem that can (a) predict the tendency to seek and share knowledge and (b) tie those tendencies to feedback received from reputation signals (e.g. Baumeister, 1982; Baumeister et al., 1996). We suggest future research can further investigate knowledge diffusion in SMNs from the lens of such personal characteristics.

Third, in studying the knowledge-related features of social media platforms and distribution of knowledge roles, we speci<sup>fi</sup>cally focused on reputational mechanisms as one attribute that distinguishes them from conventional social networks. However, social media platforms have other exclusive attributes (Von Krogh, 2012; Oh et al., 2013), such as user pro<sup>fi</sup>ling and content search mechanisms (Kane et al., 2014), that might also interact with distribution of knowledge roles to in<sup>fl</sup>uence knowledge diffusion. We believe that future research can look into other distinct structural features of social media platforms that have the potential to interact with the diffusional effect of distribution of knowledge roles.

Finally, in this study, we only model speci<sup>fi</sup>c types of social media platforms that connect all individuals (e.g. online forums and wikis). However, recent reports suggest that other types of social media, such as pro<sup>fi</sup>le-based social networking platforms, are becoming popular as mediums to seek and share knowledge. From a network topology perspective, such platforms involve different patterns of connection (e.g. small-world and scale-free) (e.g. Ellison, 2007; Viswanath et al., 2009) that do not resemble our fully connected grid of individuals. Hence, we suggest that future research extends this study by investigating how different network topologies change the diffusional effects of distribution of knowledge roles.

## Theoretical contributions

Despite the aforementioned limitations, we believe that this study contributes to the current literature on KM and SMNs. We extend the literature on SMNs, which has mainly focused on the determinants of individual participation, by shifting the focus to knowledge diffusion, as an important end-result of utilizing SMNs. Focus of previous literature on SMNs has been on individuals’ participation, thereby leaving gaps in insights about the complex, emergent and organizational-level processes and outcomes of KM through SMNs. Utilizing the power of ABM in studying emergent phenomena, this study bridges this gap by shedding light on factors driving knowledge diffusion in SMNs, as one of the important outcomes of interest in KM.

Further, this study extends the literature on knowledge diffusion that has mainly focused on F2FNs and general factors by studying knowledge diffusion in the context of SMNs and identifying the effects of SMN-speci<sup>fi</sup>c factors, namely, reputation mechanisms and distribution of knowledge roles. We focus on these two distinct characteristics enabled and emerged in SMNs and show how they can complement existing theories of organizational learning and knowledge diffusion. Additionally, while most studies of knowledge diffusion consider either factors that facilitate smooth traverse of knowledge or factors that facilitate better extraction of true beliefs, this study shows that interdependent consideration of both factors in an interactive manner better explains the nature of knowledge diffusion in SMNs.

Finally, surprising <sup>fi</sup>ndings from our study can potentially in<sup>fl</sup>uence the focus of research on knowledge sharing and seeking behaviours. Results of this study highlight the importance of knowledge brokering and suggest that compared to knowledge sharing, knowledge seeking plays a more important role in diffusing knowledge in SMNs. Despite its importance in diffusing organizational knowledge. knowledge seeking has gained less attention compared with knowledge sharing (Borgatti & Cross, 2003). We believe that the focus on knowledge sharing or contribution is rooted in the traditional KM contexts where knowledge repositories played a key role in organizational learning. Because knowledge repositories rely on accumulation of individual knowledge (Kankanhalli et al., 2005), contributing knowledge to these repositories has become the centre of attention. However, with the emergent change in KM practices and the call for attention to decentralized ways of governing knowledge through SMNs, the relative attention to knowledge seeking and sharing behaviour needs to be reexamined.

## Implications for practice

The insights pertaining to the distribution of knowledge roles and reputation mechanisms also have potential implications for practice. Categories of reputation mechanisms and distribution of knowledge roles are identi<sup>fi</sup>able and measurable in organizations. Most reputation mechanisms of SMNs have their algorithm for building reputation scores accessible and open for adopters to study and even modify, Further, advancement of open-source social graphing tools such as NodeXL (Greenhow & Hansen, 2011) enables <sup>fi</sup>rms to analyse SMN transaction of users and groups them into categories of contributors, seekers and brokers.

Our results inform KM of<sup>fi</sup>cers striving for monitoring and increasing transfer of knowledge in their organizational network utilizing SMNs by suggesting joint consideration of reputation mechanisms and distribution of knowledge roles. First, for managers concerned with reshaping the boundaries of their SMNs, our results provide contingent strategies regarding the reputation mechanisms used in those SMNs. For example, managers dealing with multiple electronic communities of practice should decide about reshaping strategies such as cross-posting rules and combining or disaggregating existing communities (Butler & Wang, 2012). Such decisions can be governed by considering: (a) the reputation mechanism used and (b) the current as wel as expected distribution of knowledge roles. For instance, allowing cross-posting for members of a community with high presence of brokers in a community with PowerHSH distribution can contribute signi<sup>fi</sup>cantly to improvement of knowledge diffusion especially if an objective reputation mechanism is utilized.

Additionally, this study enables managers adopting new reputational features for their currently operating SMNs to decide about the value of those features based on the current distribution of knowledge roles. For example, while our results suggest that in SMNs where knowledge roles are distributed in a PowerHSH fashion, investment in more objective reputation mechanisms increase knowledge diffusion only by 10%, this increase for SMNs with normal distributions can be up to 65%. This expected increase in knowledge diffusion could then be compared with the costs of upgrading to more objective solutions, thereby enabling better decisions regarding the appropriate reputation mechanisms.

Finally, our results pointing to the importance of seekers for knowledge diffusion can help managers to better design incentives for participation as a seeker. For the most part, SMNs have mechanisms that encourage sharing knowledge. For example, those sharing more answers in Q&A forums receive more recognition via titles, bonus points and so on, and such recognition is shown to boost intentions for sharing knowledge. Nonetheless, asking questions is rarely applauded leaving many who might seek knowledge, reluctant to do so and remain as lurkers rather than knowledge seekers or contributors. In fact, research shows that some communities have a population of passive users as large as one fourth of their active members (van Uden-Kraan et al., 2008). Considering our <sup>fi</sup>ndings, managers can achieve greater knowledge diffusion if they can recognize the value of seeking knowledge.

In conclusion, this study sheds light on the ways in which organizations can enhance knowledge diffusion via SMNs. It informs the practice about the interdependence of two SMN-speci<sup>fi</sup>c factors, i.e. reputation mechanisms and distribution of knowledge roles, affecting knowledge diffusion. We hope that this study can motivate further investigation into identifying other SMN-speci<sup>fi</sup>c factors that can be leveraged to enhance knowledge diffusion.

## REFERENCES

Aalbers, H.L. & Dolfsma, W. (2015) Bridging <sup>fi</sup>rm-interna boundaries for innovation: directed communication orientation and brokering roles. Journal of Engineering and Technology Management, 36, 97–115.

Aalbers, R., Dolfsma, W. & Koppius, O. (2013) Individua connectedness in innovation networks: On the role of individual motivation. Research Policy, 42, 624–634.

© 2016 John Wiley & Sons Ltd, Information Systems Journa

Aberer, K. & Despotovic, Z. (2001) Managing trust in a peer-2-peer information system, in Proceedings of the tenth international conference on Information and knowl edge management 2001, ACM, 310-317.

Abrahamson, E. & Rosenkopf, L. (1997) Social network ef fects on the extent of innovation diffusion: a compute simulation. Organization science, 8, 289–309.

Adamic, L.A., Zhang, J., Bakshy, E. & Ackerman, M.S. (2008) Knowledge sharing and yahoo answers: every one knows something, in Proceedings of the 17th inter national conference on World Wide Web 2008, ACM, 665-674.

Alberghini, E., Cricelli, L. & Grimaldi, M. (2014) A method ology to manage and monitor social media inside a com pany: a case study. Journal of Knowledge Management, 18, 255–277.

Amblard, F. & Deffuant, G. (2004) The role of network to pology on extremism propagation with the relative agree ment opinion dynamics. Physica A: Statistical Mechanics and its Applications, 343, 725–738.

Austin, J.R. (2003) Transactive memory in organizationa groups: the effects of content, consensus, specialization, and accuracy on group performance. Journal of Applied Psychology, 88, 866.

Bala, V. & Goyal, S. (1998) Learning from neighbours. The review of economic studies, 65, 595–621.

Bampo, M., Ewing, M.T., Mather, D.R., Stewart, D. & Wallace, M. (2008) The effects of the social structure o digital networks on viral marketing performance. Information Systems Research. 19. 273–290

Bateman, P.J., Gray, P.H. & Butler, B.S. (2011) The impact of community commitment on participation in online com munities. Information Systems Research, 22, 841–854.

Battistoni, E. & Colladon, A.F. (2014) Personality correlates of key roles in informal advice networks. Learning and Individual Differences, 34, 63–69.

Baumeister, R.F. (1982) Self-esteem, self-presentation, and future interaction: a dilemma of reputation. Journa of Personality, 50, 29–45.

Baumeister, R.F., Smart, L. & Boden, J.M. (1996) Relation of threatened egotism to violence and aggression: the dark side of high self-esteem. Psychological Review, 103, 5.

Beck, R., Pahlke, I. & Seebach, C. (2014) Knowledge ex change and symbolic action in social media-enabled electronic networks of practice: a multilevel perspective on knowledge seekers and contributors. MIS Quarterly, 38, 1245–1270.

Bock, G.W., Zmud, R.W., Kim, Y.G. & Lee, J.N. (2005) Be havioral intention formation in knowledge sharing: exam ining the roles of extrinsic motivators, socialpsychological forces, and organizational climate. MIS Quarterly, 29, 87–111.

Borgatti, S.P. & Cross, R. (2003) A relational view of infor mation seeking and learning in social networks. Man agement science, 49, 432–445.

Bradley, A.J. & McDonald, M.P. (2011) Social media versus knowledge management. Harvard Business Review Blog, 9:27 AM Wednesday, (October 26, 2011).

Brown, S.A., Dennis, A.R., Burley, D. & Arling, P. (2013) Knowledge sharing and knowledge management sys tem avoidance: the role of knowledge type and the social network in bypassing an organizational knowl edge management system. Journal of the American Society for Information Science and Technology, 64, 2013–2023.

Bush, A.A. & Tiwana, A. (2005) Designing sticky knowl edge networks. Communications of the ACM, 48, 66–71.

Butler, B.S. & Wang, X. (2012) The cross-purposes o cross-posting: boundary reshaping behavior in online discussion communities. Information Systems Re search, 23, 993–1010.

Chang, H.H. & Chuang, S. (2011) Social capital and indi vidual motivations on knowledge sharing: participant in volvement as a moderator. Information & management 48, 9–18.

Chen, C. & Hung, S. (2010) To give or to receive? Factors in<sup>fl</sup>uencing members’ knowledge sharing and commu nity promotion in professional virtual communities. Infor mation & Management, 47, 226–236.

Chen, W., Zeng, Q., Wenyin, L. & Hao, T. (2007) A use reputation model for a user-interactive question answer ing system. Concurrency and Computation: Practice and Experience, 19, 2091–2103.

Chen, Z. & Guan, J. (2016) The core-peripheral structure o international knowledge <sup>fl</sup>ows: evidence from patent ci tation data. R & D Management, 46, 62–79.

Chin, C.P., Evans, N. & Choo, K.R. (2015) Exploring factors in<sup>fl</sup>uencing the use of enterprise social networks in mul tinational professional service <sup>fi</sup>rms. Journal of Organi zational Computing and Electronic Commerce, 25, 289–315.

Chiu, C., Hsu, M. & Wang, E.T. (2006) Understanding knowledge sharing in virtual communities: an integratio of social capital and social cognitive theories. Decisio Support Systems, 42, 1872–1888.

Chiu, C., Wang, E.T.G., Shih, F. & Fan, Y. (2011) Understanding knowledge sharing in virtual communities an integration of expectancy discon<sup>fi</sup>rmation and justice theories. Online Information Review, 35, 134–153.

Choi, J., Sang-Hyun, A. & Cha, M. (2013) The effects o network characteristics on performance of innovation clusters. Expert Systems with Applications, 40, 4511–4518.

Chung, N., Han, H. & Koo, C. (2015) Adoption of travel in formation in user-generated content on social media: the moderating effect of social presence. Behaviour & In formation Technology, 34, 902–919.

Contractor, N.S., Wasserman, S. & Faust, K. (2006) Testing multi-theoretical, multilevel hypotheses about

organizational networks: an analytic framework and empirical example. Academy of Management Review, 31, 681–703.

Cowan, R. & Jonard, N. (2004) Network structure and the diffusion of knowledge. Journal of Economic Dynamics and Control, 28, 1557–1575

Cross, R., Parker, A., Prusak, L. & Borgatti, S.P. (2001) Knowing what we know: supporting knowledge creation and sharing in social networks. Organizational dynamics, 30, 100–120.

Davis, J.P., Eisenhardt, K.M. & Bingham, C.B. (2007) Developing theory through simulation methods. Academy of Management Review, 32, 480–499.

Davy, C. (2006) Recipients: the key to information transfer. Knowledge Management Research & Practice, 4, 17–25.

de Kraker, J., Corvers, R., Valkering, P., Hermans, M. & Rikers, J. (2013) Learning for sustainable regional development: towards learning networks 2.0? Journal of Cleaner Production, 49, 114–122.

Delre, S., Jager, W. & Janssen, M. (2004) Percolation and innovation diffusion models compared: do network structures and social preferences matter, in Proceedings of M2M2 workshop and ESSA conference. Valladolid. Spain 2004.

Delre, S.A., Jager, W. & Janssen, M.A. (2007) Diffusion dy namics in small-world networks with heterogeneous consumers. Computational and Mathematical Organization Theory, 13, 185–202.

Drew, H., Richie, F. & King, A. (2013) How do knowledge brokers work? Implications for policy and practice in the case of WERS. International Journal of Technology Management & Sustainable Development, 13, 205–218.

Ellison, N.B. (2007) Social network sites: De<sup>fi</sup>nition, history, and scholarship. Journal of Computer-Mediated Communication, 13, 210–230.

Ellison, N.B. & Boyd, D. (2013) Sociality through social network sites. The Oxford Handbook of Internet Studies, 151–172.

Ellison, G. & Fudenberg, D. (1995) Word-of-mouth communication and social learning. The Quarterly Journal of Economics, 93–125.

Erkunt, H. (2010) Emergence of epistemic agency in college level educational technology course for preservice teachers engaged in cscl. Turkish Online Journal of Educational Technology, 9, 38–51.

Ernst, D. & Kim, L. (2002) Global production networks, knowledge diffusion, and local capability formation. Research policy, 31, 1417–1429.

Faraj, S., Kudaravalli, S. & Wasko, M. (2015) Leading collaboration in online communities. Mis Quarterly, 39, 393–412.

Fernandez, J. (2014) Social media platform. US Patent, 8 910,076.

Fiol, C.M. & Lyles, M.A. (1985) Organizational learning. Academy of management review, 10, 803–813.

Friedman, E., Resnick, P. & Sami, R. (2007) Manipulation resistant reputation systems, In: Algorithmic Game Theory, pp. 677–697. Cambridge University Press, UK.

Gao, X. & Guan, J. (2012) Network model of knowledge dif fusion. Scientometrics, 90, 749–762.

Giani, U., Romano, A. & Bruzzese, D. (2005) An epidemio logical model of knowledge diffusion in virtual learning networks: an application to learning statistics in medi cine. Cybernetics and Systems, 36, 445–456.

Granovetter, M. (1973) The strength of weak ties American Journal of Sociology, 78, 1360–1380.

Gray, B. (2004) Informal learning in an online community o practice. Journal of Distance Education, 19, 20–35.

Greenhow, C. & Hansen, D.L. (2011) Exploring social me dia relationships. On the Horizon, 19, 43–51.

Grover, V. & Davenport, T.H. (2001) General perspective on knowledge management: fostering a research agenda. Journal of Management Information Systems, 18.5-21

Guechtouli, W., Rouchier, J. & Orillard, M. (2013) Structur ing knowledge transfer from experts to newcomers. Journal of Knowledge Management, 17, 47–68.

Hamra, J., Wigand, R., Hossain, L. & Owen, C. (2014) Network effects on learning during emergency events. Knowledge Management Research & Practice, 12, 387–397.

Hansen, M.T. (1999) The search-transfer problem: the role of weak ties in sharing knowledge across organization subunits. Administrative Science Quarterly, 44, 82–111.

Harrison, J.R., Carroll, G.R. & Carley, K.M. (2007) Simulatio modeling in organizational and management research Academy of Management Review, 32, 1229–1245.

Havakhor, T. & Sabherwal, R. (2013) Knowledge Sharing in Peer-to-Peer Online Communities: The Effects of Rec ommendation Agents and Community Characteristics, in System Sciences (HICSS), 2013 46th Hawaii International Conference on 2013, IEEE, 3553–3562.

He, W. & Wei, K. (2009) What drives continued knowledge sharing? An investigation of knowledge-contribution and-seeking beliefs. Decision Support Systems, 46, 826–838.

Hsu, M. & Chang, C. (2014) Examining interpersonal trust as a facilitator and uncertainty as an inhibitor of intraorganisational knowledge sharing. Information Systems Journal, 24, 119–142.

Hsu, M., Ju, T.L., Yen, C. & Chang, C. (2007) Knowledge sharing behavior in virtual communities: The relationship

between trust, self-ef<sup>fi</sup>cacy, and outcome expectations. International Journal of Human-Computer Studies, 65, 153–169.

Huang, Q., Davison, R.M. & Gu, J. (2011) The impact of trust, guanxi orientation and face on the intention of Chi nese employees and managers to engage in peer-to peer tacit and explicit knowledge sharing. Information Systems Journal, 21, 557–577.

Huber, G.P. (2001) Transfer of knowledge in knowledge management systems: unexplored issues and sug gested studies. European Journal of Information Sys tems, 10, 72–79.

Jiang, G., Ma, F., Shang, J. & Chau, P.Y.K. (2014) Evolution of knowledge sharing behavior in social commerce: an agent-based computational approach. Information Sciences, 278, 250–266.

Jo, I., Kang, S. & Yoon, M. (2014) Effects of communication competence and social network centralities on learne performance. Educational Technology & Society, 17, 108–120.

Judge, T.A. & Bono, J.E. (2001) Relationship of core self evaluations traits—self-esteem, generalized self-ef<sup>fi</sup>cacy, locus of control. and emotional stability—with job satisfaction and job performance: A meta-analysis. Journa of applied Psychology, 86, 80–92.

Kamvar, S.D., Schlosser, M.T. & Garcia-Molina, H. (2003) The eigentrust algorithm for reputation manage ment in p2p networks, in Proceedings of the 12th international conference on World Wide Web 2003, ACM, 640-651.

Kane, G.C. & Alavi, M. (2007) Information technology and organizational learning: an investigation of exploration and exploitation processes. Organization Science, 18, 796–812.

Kane, G.C. & Alavi, M. (2008) Casting the net: a multi modal network perspective on user-system interactions. Information Systems Research, 19, 253–272.

Kane, G.C., Alavi, M., Labianca, G. & Borgatti, S.P. (2014) What's different about social media networks? A framework and research agenda. MIS Quarterly, 38, 275–304.

Kang, M. & Hau, Y.S. (2014) Multi-level analysis of knowl edge transfer: a knowledge recipient’s perspective. Jour nal of Knowledge Management, 18, 758–776.

Kankanhalli, A., Tan, B.C. & Wei, K. (2005) Contributing knowledge to electronic knowledge repositories: an em pirical investigation. MIS Quarterly, 29, 113–143.

Kim, H. & Park, Y. (2009) Structural effects of R&D collaboration network on knowledge diffusion perfor mance. Expert Systems with Applications, 36, 8986–8992.

Kim, H. & Sundar, S.S. (2011) Using interface cues in on line health community boards to change impressions

and encourage user contribution, in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems 2011, ACM, 599-608.

Kim, Y., Hau, Y.S., Song, S. & Ghim, G. (2014) Trailing or ganizational knowledge paths through social network lens: integrating the multiple industry cases. Journal o Knowledge Management, 18, 38–51.

Kiron, D., Palmer, D., Phillips, A.N. & Kruschwitz, N. (2012) Social business: What are companies really doing? Sloan Management Review, Summer.

Kunz, J. (2011) Group-level exploration and exploitation: a computer simulation-based analysis. Journal of Arti<sup>fi</sup>cia Societies & Social Simulation, 14.

Lai, H. & Chen, T.T. (2014) Knowledge sharing in interes online communities: a comparison of posters and seekers. Computers in Human Behavior, 35, 295–306.

Lavis, J.N. (2006) Research, public policymaking, and knowledge-translation processes: Canadian efforts to build bridges. Journal of Continuing Education in the Health Professions, 26, 37–45.

Lazer, D. & Friedman, A. (2007) The network structure o exploration and exploitation. Administrative Science Quarterly, 52, 667–694

Lee, J. & Cho, H. (2011) Factors affecting information seek ing and evaluation in a distributed learning environment. Educational Technology & Society, 14, 213–223.

Leonardi, P.M. (2015) Ambient awareness and knowledge acquisition: using social media to learn" who knows what" and" who knows whom". MIS Quarterly, 39, 747–762.

Lewis, K., Lange, D. & Gillis, L. (2005) Transactive memor systems, learning, and learning transfer. Organizatio Science, 16, 581–598.

Liang, D.W., Moreland, R. & Argote, L. (1995) Group ver sus individual training and group performance: the medi ating role of transactive memory. Personality and Socia Psychology Bulletin, 21, 384–393.

Li, Y., Lin, L. & Lin, Y. (2014) A recommender mechanism fo social knowledge navigation in an online encyclopedia Information Processing & Management, 50, 634–652.

Liao, L. & Wang, K. (2010) Network and Organizationa Learning: The Effect of Structure and Tie Strength, in E-Business and E-Government (ICEE), 2010 Interna tional Conference on 2010, IEEE, 1860-1863.

Licorish, S.A. & MacDonell, S.G. (2014) Understanding th attitudes, knowledge sharing behaviors and task perfor mance of core developers: a longitudinal study. Informa tion and Software Technology, 56, 1578–1596.

Licorish, S.A. & MacDonell, S.G. (2015) Communication and personality pro<sup>fi</sup>les of global software developers. Information and Software Technology, 64, 113–131.

Lin, J. & Lai, Y. (2013) Online formative assessments with social network awareness. Computers & Education, 66, 40–53.

Lin, M. & Li, N. (2010) Scale-free network provides an optimal pattern for knowledge transfer. Physica A: Statistical Mechanics and its Applications, 389, 473–480.

Lin, M.J., Hung, S. & Chen, C. (2009) Fostering the determinants of knowledge sharing in professional virtua communities. Computers in Human Behavior. 25. 929–939

Lin, S. & Lo, L.Y. (2015) Mechanisms to motivate knowl edge sharing: integrating the reward systems and socia network perspectives. Journal of Knowledge Management, 19, 212–235.

Liu, J. & Rau, P.P. (2014) Impact of self-construal on choice of enterprise social media for knowledge sharing. Socia Behavior and Personality, 42, 1077–1089.

Liu, X., Jiang, S., Chen, H., Larson, C.A. & Roco, M.C. (2015) Modeling knowledge diffusion in scienti<sup>fi</sup>c innovation networks: an institutional comparison between china and US with illustration for nanotechnology. Scientometrics, 105, 1953–1984.

Liu, X., Kaza, S., Zhang, P. & Chen, H. (2011) Determining inventor status and its effect on knowledge diffusion: a study on nanotechnology literature from china, russia, and india. Journal of the American Society for Information Science and Technology, 62, 1166–1176.

Ma, M. & Agarwal, R. (2007) Through a glass darkly: Information technology design, identity veri<sup>fi</sup>cation, and knowledge contribution in online communities. Information Systems Research, 18, 42–67.

Macy, M.W. & Willer, R. (2002) From factors to actors: computational sociology and agent-based modeling. Annual review of sociology, 28, 143–166.

Majchrzak, A., Wagner, C. & Yates, D. (2013) The impact of shaping on knowledge reuse for organizational improvement with wikis. MIS Quarterly, 37, 455–469.

Makkonen, H. & Virtanen, K. (2015) Social capital approach on enterprise 2.0: a multiple case study. Technology Analysis & Strategic Management, 27. 1212–1225.

March, J.G. (1991) Exploration and exploitation in organizational learning. Organization science, 2, 71–87.

Marett, K. & Joshi, K. (2009) The decision to share information and rumors: examining the role of motivation in an online discussion forum. Communications of the Association for Information Systems, 24, 4.

McAfee, A. (2009) Enterprise 2.0: New collaborative tools for your organization’s toughest challenges. Harvard Business Press.

McKenzie, J. & van Winkelen, C. (2012, White Paper) http://www.henley.ac.uk/web/FILES/corporate/ cl\_KM\_Forum\_Knowledge\_sharing\_2\_0.pdf.

Miller, K.D., Zhao, M. & Calantone, R.J. (2006) Adding in terpersonal learning and tacit knowledge to March’s exploration–exploitation model. Academy of Management Journal, 49, 709–722.

Mu, J., Tang, F. & MacLachlan, D.L. (2010) Absorptive and disseminative capacity: knowledge transfer in intraorganization networks. Expert Systems with Applications, 37, 31–38.

Nam, K.K., Ackerman, M.S. & Adamic, L.A. (2009) Questions in, knowledge in?: a study of naver’s question answering community, in Proceedings of the SIGCHI conference on human factors in computing systems 2009, ACM, 779-788.

Nan, N. (2011) Capturing bottom-up information technol ogy use processes: a complex adaptive systems model. MIS Quarterly, 35, 505–532.

Nan, N. & Johnston, E.W. (2009) Using multi-agent simulation to explore the contribution of facilitation to GSS transition. Journal of the Association for Information Systems, 10, 252–277.

Nonaka, I. (1994) A dynamic theory of organizationa knowledge creation. Organization science, 5, 14–37.

Norman, C.D. & Huerta, T. (2006) Knowledge transfer & exchange through social networks: building foundations for a community of practice within tobacco control. Implementation Science, 1, 20.

Oh, O., Agrawal, M. & Rao, H.R. (2013) Community intelligence and social media services: a rumor theoretic anal ysis of tweets during social crises. MIS Quarterly, 37, 407–426.

Oh, S. (2012) The characteristics and motivations of health answerers for sharing information, knowledge, and experiences in online environments. Journal of the American Society for Information Science and Technology, 63, 543–557.

Oshri, I., Van Fenema, P. & Kotlarsky, J. (2008) Knowledge transfer in globally distributed teams: the role of transactive memory. Information Systems Journal, 18, 593-616.

Overby, E. (2012) Migrating processes from physical to virtual environments: Process virtualization theory, In Information systems theory: Explaining and predicting our digital society, vol. 1, Dwivedi, Y.K., Wade, M.R. & Schneberger, L.S.L. (eds), pp. 107–124. Springer Publishing, New York.

Ozel, B. (2012) Individual cognitive structures and collabo ration patterns in academia. Scientometrics, 91, 539–555.

Peddibhotla, N.B. (2013) Why different motives matter in sustaining online contributions. Electronic Commerce Research and Applications, 12, 90–102.

Phang, C.W., Kankanhalli, A. & Sabherwal, R. (2009) Usability and sociability in online communities: A com parative study of knowledge seeking and contribution. Journal of the Association for Information Systems, 10, 2.

Quigley, N.R., Tesluk, P.E., Locke, E.A. & Bartol, K.M. (2007) A multilevel investigation of the motivationa mechanisms underlying knowledge sharing and perfor mance. Organization Science, 18, 71–88.

Rahbar, A. & Yang, O. (2007) Powertrust: a robust and scalable reputation system for trusted peer-to-peer com puting. Parallel and Distributed Systems, IEEE Transac tions on, 18, 460–473.

Ransbotham, S., Kane, G.C. & Lurie, N.H. (2012) Network characteristics and the value of collaborative user-generated content. Marketing Science, 31, 387–405.

Razmerita, L., Kirchner, K. & Nabeth, T. (2014) Social me dia in organizations: leveraging personal and collective knowledge processes. Journal of Organizational Com puting and Electronic Commerce, 24, 74–93.

Reagans, R. & McEvily, B. (2003) Network structure and knowledge transfer: the effects of cohesion and range. Administrative Science Quarterly, 48. 240–267.

Ren, Y., Harper, F.M., Drenner, S., et al. (2012) Building member attachment in online communities: applying the ories of group identity and interpersonal bonds. MIS Quarterly, 36, 841–864.

Resnick, M. (1997) Turtles, termites, and traf<sup>fi</sup>c jams: Ex plorations in massively parallel microworlds. MIT Press.

Resnick, P., Kuwabara, K., Zeckhauser, R. & Friedman, E. (2000) Reputation systems. Communications of the ACM, 43, 45–48.

Ridings, C., Gefen, D. & Arinze, B. (2006) Psychologica barriers: lurker and poster motivation and behavior in on line communities. Communications of the Association fo Information Systems, 18, 16.

Rodan, S. (2008) Organizational learning: effects of (net work) structure and (individual) strategy. Computationa and Mathematical Organization Theory, 14. 222–247.

Singh, J. (2005) Collaborative networks as determinants o knowledge diffusion patterns. Management Science, 51, 756–770.

Staples, D.S. & Webster, J. (2008) Exploring the effects of trust, task interdependence and virtualness on knowl edge sharing in teams. Information Systems Journal, 18, 617–640.

Stauffer, D. & Sahimi, M. (2005) Diffusion in scale-free net works with annealed disorder. Physical Review E, 72, 046128.

Suh, A. & Shin, K. (2010) Exploring the effects of online so cial ties on knowledge sharing: a comparative analysis o

collocated vs dispersed teams. Journal of Informatio Science, 36, 443–463.

Sutanto, J., Tan, C., Battistini, B. & Phang, C.W. (2011) Emergent leadership in virtual collaboration settings: a social network analysis approach. Long Range Plan ning, 44, 421–439.

Tang, F., Mu, J. & MacLachlan, D.L. (2008) Implication o network size and structure on organizations’ knowledg transfer. Expert Systems with Applications, 34, 1109–1114

Tang, F., Xi, Y. & Ma, J. (2006) Estimating the effect of orga nizational structure on knowledge transfer: a neural net work approach. Expert Systems with Applications, 30, 796–800.

Tsai, W. (2001) Knowledge transfer in intraorganizationa networks: Effects of network position and absorptive ca pacity on business unit innovation and performance Academy of Management Journal, 44, 996–1004.

Tseng, F. & Kuo, F. (2010) The way we share and learn: an exploratory study of the self-regulatory mechanisms in the professional online learning community. Computers in Human Behavior, 26, 1043–1053.

Tseng, F. & Kuo, F. (2014) A study of social participation and knowledge sharing in the teachers’ online profes sional community of practice. Computers & Education, 72, 37–47.

Van Maanen, J. (1995) Crossroads Style as Theory. Orga nization Science, 6. 133–143

van Uden-Kraan, C.F., Drossaert, C.H., Taal, E., Seydel, E. R. & van de Laar, M.A. (2008) Self-reported differences in empowerment between seekers and posters in online patient support groups. Journal of medical Internet re search, 10, e18.

Viswanath, B., Mislove, A., Cha, M. & Gummadi, K.P (2009) On the evolution of user interaction in facebook, in Proceedings of the 2nd ACM workshop on Online so ciaL networks 2009 ACM.37-42

Von Krogh, G. (2012) How does social software change knowledge management? Toward a strategic research agenda. The Journal of Strategic Information Systems, 21, 154–164.

Wanberg, J., Javernick-Will, A., Chinowsky, P. & Taylor, J. E. (2015) Spanning cultural and geographic barriers wit knowledge pipelines in multinational communities o practice. Journal of Construction Engineering and Man agement, 141, 04014091.

Wang, J., Guo, Q., Yang, G. & Liu, J. (2015) Improved knowledge diffusion model based on the collaboration hypernetwork. Physica A: Statistical Mechanics and its Applications, 428, 250–256.

Wang, G.A., Jiao, J., Abrahams, A.S., Fan, W. & Zhang, Z. (2013) ExpertRank: a topic-aware expert <sup>fi</sup>nding

© 2016 John Wiley & Sons Ltd, Information Systems Journa

algorithm for online knowledge communities. Decision Support Systems, 54, 1442–1451.

Wang, X. & Li, Y. (2014) Trust, psychological need, and motivation to produce user-generated content: a selfdetermination perspective. Journal of Electronic Commerce Research, 15, 241–253.

Wang, Y. & Haggerty, N. (2009) Knowledge transfer in virtual settings: the role of individual virtual competency. Information Systems Journal. 19. 571–593.

Wasko, M.M. & Faraj, S. (2005) Why should I share? Examining social capital and knowledge contribution in electronic networks of practice. MIS quarterly, 29, 35–57.

Wasko, M.M., Teigland, R. & Faraj, S. (2009) The provision of online public goods: examining social structure in an electronic network of practice. Decision Support Systems, 47, 254–265.

Welser, H.T., Gleave, E., Fisher, D. & Smith, M. (2007) Visualizing the signatures of social roles in online discussion groups. Journal of social structure, 8, 1–32.

Wiig, K.M. (2003) A knowledge model for situationhandling. Journal of Knowledge Management, 7, 6–24.

Wu, B., Jiang, S. & Chen, H. (2015) The impact of individ ual attributes on knowledge diffusion in web forums. Quality & Quantity 492221–2236

Xu, W.W., Chiu, I., Chen, Y. & Mukherjee, T. (2015) Twitter hashtags for health: applying network and content

analyses to understand the health knowledge sharing in a twitter-based community of practice. Quality & Quantity, 49, 1361–1380.

Yang, C., Ma, J., Silva, T., Liu, X. & Hua, Z. (2015) A multilevel information mining approach for expert recom mendation in online scienti<sup>fi</sup>c communities. Computer Journal, 58. 1921–1936

Yu, T., Lu, L. & Liu, T. (2010) Exploring factors that in<sup>fl</sup>u ence knowledge sharing behavior via weblogs. Computers in Human Behavior, 26, 32–41.

Yammer. (2016) https://products.of<sup>fi</sup>ce.com/en-us/yammer yammer-overview.

Zappa, P. (2011) The network structure of knowledge sharing among physicians. Quality & Quantity, 45, 1109–1126.

{Parameter setting: also see Table A1}

Zhang, J., Ackerman, M.S. & Adamic, L. (2007) Expertise networks in online communities: structure and algorithms, in Proceedings of the 16th international conference on World Wide Web 2007, ACM, 221-230.

PSUEDO-CODE

Ask reputation mechanism [Adaptive/Objective].

Zhang, X. & Venkatesh, V. (2013) Explaining employee job performance: the role of online and of<sup>fl</sup>ine workplace communication networks. MIS Quarterly, 37, 695 +.

Zhao, R. & Chen, B. (2013) Study on enterprise knowledge sharing in ESN perspective: a chinese case study. Jour nal of Knowledge Management 17416—434

APPENDIX A: SIMULATION PSUEDO-CODE AND PARAMETER SETTINGS

Ask number of agents [N].

Ask number of knowledge seeking and sharing rounds [H].

Ask the distribution of knowledge roles:

Seekers: x,

Contributors: y.

{x and y represent the proportion of seekers and contributors in the network.}

{Creating agents based on the set parameters}

Create N agents with the following attributes for each agent:

© 2016 John Wiley & Sons Ltd, Information Systems Journa

10 knowledge attributes (K )

For each attribute ${ \sf K } _ { \mathrm { i } } \mathrm { : }$

Create a random number [R] between 0 and 1:

If R < = 0.33 then $\mathsf { K } _ { \mathrm { i } } = - 1$ else

If R < = 0.66 then $\mathsf { K } _ { \mathrm { i } } = 0$ else

K<sub>i</sub> = 1.

SEEK.

SHARE.

{The above code will create agents each with 10 knowledge elements (K s) and two other at tributes, SEEK and SHARE which are the probability of the agent to seek and share knowledge, respectively.}

For $( x ^ { \star } N )$ agents:

SEEK = 0.8,

SHARE = 1 – SEEK.

For $( \mathsf { y } ^ { \star } \mathsf { N } )$ agents:

SEEK = 0.2,

SHARE = 1 – SEEK.

For ((1-x-y) \* N) agents:

SEEK = 0.5,

SHARE = 1 – SEEK.

Create ties among all agents.

{Simulating knowledge seeking and sharing}

Repeat for H rounds:

Set the value of falsely adopted knowledge elements 2 rounds back [i.e., $\mathsf { K } _ { \mathrm { i } }$ which were adopted from the source with value of -1] to value 0.

Calculate the reputation of each agent [ j]:

If reputation mechanism = ‘Objective’ then

Reputation<sub>j</sub> = Sum (K<sub>ij</sub>),

If reputation mechanism = ‘Adaptive’ then

Reputation = Sum (K’ ).

{K’ denotes value of knowledge element[i] that is shared with others. Since there wil be no shared knowledge in the beginning of the simulation, this value will be zero for all agents.}

Update the sum of knowledge values of all agents in the network to re<sup>fl</sup>ect the overal value of knowledge:

$$
K \cdot = \cdot \sum_ {j = 1} ^ {n} \sum_ {j = 1} ^ {m} K _ {i j}
$$

{The difference of this K’s value in the <sup>fi</sup>rst round and the <sup>fi</sup>nal round re<sup>fl</sup>ects the diffused knowledge. (also see Table 4 in the main document)}

Ask each of the agents:

Randomly choose a knowledge element [K ] which is 0.

Randomly select one of in-tie agents [j] with Maximum (Reputation<sub>j</sub>).

{In situations wheremore than one person has the highest reputation value, the source is selected randomly.}

Generate a random number [R],

If R < = SEEK then

Ask selected in-tie agent [ j] its ${ \mathsf { K } } _ { \parallel } .$

Generate a random number [R],

$$
\text {   If   } R <   = \text { SHARE   then   }
$$

Set $\mathsf { K } _ { \mathrm { i } }$ of seeking agent to the value of $\mathsf { K } _ { \mathrm { i } }$ of the selected in-tie agent [ j].

Parameter Settings

Table A1 shows the values used as input in the <sup>fi</sup>rst block of the pseudo-code (the ‘parameter setting’ block):

Table A1. Simulation parameters and their possible values

<table><tr><td>Parameter</td><td>Main analysis values</td><td>Robustness $^{\dagger}$  values</td></tr><tr><td>N</td><td>1000</td><td>500</td></tr><tr><td>reputation mechanism</td><td>Adaptive; Objective</td><td>Unchanged</td></tr><tr><td>H</td><td>4000 $^{\ddagger}$ </td><td>Unchanged</td></tr><tr><td>x</td><td>[0–1] (0.01 increments)</td><td>Unchanged</td></tr><tr><td>y</td><td>[0–1] (0.01 increments)</td><td>Unchanged</td></tr><tr><td>SEEK for Seekers</td><td>0.80</td><td>0.70; 0.75; 0.85; 090</td></tr><tr><td>Seek for contributors</td><td>0.20</td><td>0.10; 0.15; 0.25; 0.30</td></tr><tr><td>Seek for brokers</td><td>0.50</td><td>0.40; 0.45; 0.55, 0.60</td></tr></table>

<sup>†</sup>See Appendix B for details of each robustness test.  
<sup>‡</sup>4,000 rounds in each simulation was chosen as it was the number of rounds through which the knowledge diffusion plots become stabilized. We obtained this number through pilot runs.

## APPENDIX B: MODEL VALIDATION

Davis et al. (2007) suggest three steps to validate the results of an agent-based simulation. These three steps involve assessing: (a) the computational validity of the simulation model; (b) robustness of results to changes in parameters or peripheral assumptions; and (c) externa validity of results. Other researchers (e.g. Nan and Johnston, 2009; Lazer and Friedman, 2007) suggest a pre-step that corresponds to grounding the key assumptions of the computational model. We start our process of model validation with the grounding pre-step. This step aims to assure that the constructed model does not violate the rules of social reality and involves providing theoretical reasoning about the behavioural rules, agent attributions and construction of the agent’s environment. We have performed the grounding process for behavioural rules extensively in our review of literature where we summarize the evidence on prevalent existence of the three categories of knowledge roles in SMNs. Further, in building the knowledge attribute of agents, we have explained how a vector representation of knowledge corresponds to theoretical de<sup>fi</sup>nition of knowledge and is grounded in studies of organizational learning. Finally, we have provided theoretical support for the connectivity between agents based on suggestions of Kane & Alavi (2008) who offered such abstraction for social media platforms.

Davis et al. (2007) suggest that the computational validity of the model be validated by repli cating results of similar studies. Given the closeness of our computational model to that of March (1991), we speci<sup>fi</sup>ed a learning rate to agents, in addition to their other attributes. We simulated diffusion of knowledge under high and low levels of learning rate (10% and 90%). Our results converge with that of March’s, indicating that decreasing individual rate of learning increases overall diffusion in the network by 36%. We run this step in order to make sure that our constructed model behaves appropriately.

The next step in model validation involves two phases. The <sup>fi</sup>rst phase is making sure that the results are not sensitive to arbitrariness of the model parameters<sup>13</sup> (Nan and Johnston, 2009). A simulation model should be designed such that the number of parameters is limited (Macy & Willer, 2002). We have followed this guideline and designed our model with minimal parameters. One of the few parameters in our model is the number of agents in the network,<sup>14</sup> which is currently set at 1000. In order to test the arbitrariness of this result, we run our simulation model in a network of 500 agents and replicate the results. Model 1 in Table B1 presents the results of this model, which remain qualitatively unchanged.

The other parameter in the model concerns the probability of knowledge seeking (and thereby, knowledge sharing = 1 – probability of knowledge seeking) for each knowledge role. In our model, this probability is set at 0.80 for Seekers, 0.20 for Contributors and 0.50 for Brokers. To test the robustness of our results to variations in those probability measures, we varied each probability in a [ 0.10, +0.10] range with 0.05 increments. This resulted in <sup>fi</sup>ve different values (one of those values is the one used in the main model) for each of the three probabilities. We examined all the possible combinations of these numbers (i.e. 125) and

\*p < 0.05

Table B1. Results of the robustness analyses<sup>†</sup>

<table><tr><td rowspan="2">DV = Diffusion</td><td colspan="2">Model 1 $^{\ddagger}$ </td><td colspan="2">Model 2</td><td colspan="2">Model 3</td></tr><tr><td>Global</td><td>Local</td><td>Global</td><td>Local</td><td>Global</td><td>Local</td></tr><tr><td>Contributor</td><td>-0.694***</td><td>-0.106***</td><td>-0.615**</td><td>-0.169***</td><td>-0.822***</td><td>-0.143***</td></tr><tr><td>Seeker</td><td>0.042***</td><td>-0.033**</td><td>0.112*</td><td>-0.078**</td><td>0.083**</td><td>-0.072**</td></tr><tr><td>Seeker*contributor</td><td>-0.428***</td><td>-0.221***</td><td>-0.307**</td><td>-0.420***</td><td>-0.524***</td><td>-0.285***</td></tr><tr><td>Contributor $^{2}$ </td><td>-0.054**</td><td>-0.088**</td><td>-0.103***</td><td>-0.153**</td><td>-0.076**</td><td>-0.092***</td></tr><tr><td>Seeker $^{2}$ </td><td>-0.216***</td><td>-0.158***</td><td>-0.273***</td><td>-0.442***</td><td>-0.282***</td><td>-0.133***</td></tr><tr><td>Probability of seeking for seekers</td><td></td><td></td><td>0.004</td><td>-0.003</td><td></td><td></td></tr><tr><td>Probability of seeking for contributors</td><td></td><td></td><td>-0.012</td><td>0.013</td><td></td><td></td></tr><tr><td>Probability of seeking for brokers</td><td></td><td></td><td>0.005</td><td>0.002</td><td></td><td></td></tr><tr><td>Constant</td><td>0.923***</td><td>0.428***</td><td>0.894***</td><td>0.397***</td><td>0.903***</td><td>0.421***</td></tr><tr><td>Adjusted  $R^{2}$ </td><td>0.67</td><td>0.56</td><td>0.66</td><td>0.59</td><td>0.61</td><td>0.55</td></tr></table>

\*\*p < 0.01  
\*\*\*p < 0.001  
All variables are mean-centred.  
<sup>†</sup>The quadratic-effects models have signi<sup>fi</sup>cantly (p < 0.001) higher R2 values compared with the direct-effects model with only contributor and seeker as independent variables

replicated our experiment with each distinct combination. Then we include the values for the probability of seeking for each knowledge role as a covariate in our main analyses. Model 2 in Table B1 represents these results. The pattern of results remains qualitatively similar when these covariates are considered. This suggests that the model is not sensitive to the values of knowledge seeking probabilities in a [ 0.10, +0.10] range.<sup>15</sup>

The second phase in validation of the model is to check whether the results remain robust when assumptions peripheral to theory building are relaxed. Speci<sup>fi</sup>cally, in developing our simulation model, we have made the assumption that an individual’s knowledge does not have any association with the individual’s knowledge role. However, literature of KM suggests that individuals possessing greater knowledge generally show higher levels of tendency to share knowledge (Judge and Bono, 2001). That is, amount of individual knowledge (regardless of its trueness) can be positively correlated with the attribute SHARE in our model. This realistic association makes the relationship between knowledge role distribution and knowledge diffusion more complex. Considering this association means that as individuals exchange knowledge, their SHARE (and thereby SEEK) changes as well. In other words, as individuals become more knowledgeable, they change their roles and turn from seekers to contributors gradually. This will make the value o SHARE (and SEEK) endogenous and adaptive to the interactions among individuals. Hence, it is imperative to make sure that the pattern of results seen in our simulated model does not change if the assumption about independence of knowledge and SHARE (SEEK) is to be relaxed.

We relax this assumption by (a) distributing knowledge such that the portion of non-zero elements of one’s knowledge equals to his SHARE<sup>16</sup> at the beginning of the simulation<sup>17</sup> and (b) specifying a sixth step in our agent interaction steps such that: at the end of each round, the value of one’s SHARE (and thereby SEEK) is updated to the portion of non-zero elements of one’s knowledge. Doing so accomplishes two goals: (a) we make an individual knowledge and SHARE (SEEK) associated and (b) by following (a), we inherently assign a knowledge dis tribution that is no longer uniform.

We run the same experiment with the new model, allowing for SHARE (and SEEK) to become endogenous and adapted based on one’s knowledge. The overall results of this round of simu lation in addition to results for adaptive and objective reputation mechanisms are presented in Model 3 of Table B1. The pattern of results has remained unchanged for the most part.

The <sup>fi</sup>nal stage in the validation of simulation models is to examine the external validity of results by showing that the results of the simulation study converge with empirical <sup>fi</sup>ndings that exist in relevant literature (Davis et al., 2007). However, it is noted that the importance of this stages depends on the on the theory that the simulation assumptions are based on. Speci<sup>fi</sup>cally, Davis et al. (2007, p. 494) contend: ‘If this theory is based primarily on empirical evidence (e.g. <sup>fi</sup>eld-based case studies and empirically grounded processes), then validation is less important, because the theory already has some external validity.

Because our study is grounded in the empirical <sup>fi</sup>ndings that asserts presence of the three distinct knowledge roles in SMNs (e.g. Welser et al., 2007; Zhang et al., 2007; Adamic et al., 2008), we argue that our simulation model is in less need of further external validation. As discussed earlier, the phenomenon of interest in this study requires power of experimenting and a longer time horizon that is not usually affordable in <sup>fi</sup>eld settings, precluding externa validation for the model by supporting its results from other <sup>fi</sup>eld studies. Indeed, the presence of similar results in <sup>fi</sup>eld studies would refute the need for conducting simulation of a complex phenomenon. Several researchers argue that the questions pertaining to agent-based model ling should not be trivial (Lazer and Friedman, 2007). When simulation models are pursued to answer questions that can be studied the <sup>fi</sup>eld settings, the results are theories that are neither interesting nor inductive (Van Maanen, 1995).
