---
otero_id: 4702
otero_key: "SG4XB22N"
title: "Exploring the tension between transparency and datification effects of open government IS through the lens of Complex Adaptive Systems"
authors: "Olivera Marjanovic; Dubravka Cecez-Kecmanovic"
year: "2017"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2017.07.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring the tension between transparency and datafication effects of open government IS through the lens of complex adaptive systems

Olivera Marjanovic <sup>a,</sup>⇑, Dubravka Cecez-Kecmanovic <sup>b</sup>

<sup>a</sup> Business Information Systems Discipline, The University of Sydney Business School, NSW 2006, Australia

<sup>b</sup> School of Information Systems Technology and Management, UNSW Business School, UNSW Sydney, NSW 2052, Australia

## a r t i c l e i n f o

Article history: Available online xxxx

Keywords: Datafication effects Transparency Open government IS Complex Adaptive Systems Social consequences Strategic implications

## a b s t r a c t

Government agencies worldwide continue their commitment to providing open data in order to increase transparency of education, healthcare and other public services. Focusing on open government information systems (IS) that provide performancerelated data, this paper explores the ongoing tension between government’s goal of transparency and the resulting largely opaque datafication effects. Our research insights are derived from an empirical longitudinal study of a controversial open government IS called My School, currently providing performance data on almost 10,000 schools in Australia. We investigate the tension between transparency intended with schools’ open performance data and datafication effects they create within the education system and a broader society, through the theoretical lens of Complex Adaptive Systems (CAS). Our study reveals how the tension emerges due to unpredictable use, propagation and reinterpretation of open data by more and more users. Consequently, the original meaning of data gets distorted, as these users continue to reconstruct and reinterpret ‘data’ in their own contexts and adapt their behavior in pursuit of their strategic goals. We also identify and theorize seven datafication patterns underlying the tension and the ways they produce various social consequences. Based on these research contributions we discuss important strategic implications for government decision makers and identify new opportunities for future research on open government IS.

 2017 Published by Elsevier B.V.

## 1. Introduction

Driven by the pressing need for transparency, governments around the world are making data available to the public. Transparency has become a key objective in public sector reforms as an ‘‘apparently simple solution to complex problems – such as how to fight corruption, promote trust in government, support corporate social responsibility, and foster state accountability” (Birchall, 2014, p. 77). As part of the growing ‘open government movement’ (Baack, 2015; Janssen, 2011), transparency is expected to lead to government accountability and better services to citizens (Michener and Bersch, 2013). Over the years the main focus of transparency has shifted from visibility of data through, for instance, public reporting, to a new focus on empowering citizens to infer their own insights from open data (Michener and Bersch,

2013). By providing open data and simple-to-use tools for data analysis it is assumed that citizens would be able to ‘infer’ their own valuable insights. The open government movement thus marks a new era of transparency in which government data are not only publicly available but also, and importantly, analyzed and interpreted by citizens. For example, citizens are invited to ‘interrogate’ open data on public spending in order to help government identify waste and possible fraud (Lourenco, 2013). This opens, according to the UK Government, ‘‘a new era in which people can use open data to generate insights, ideas, and services to create a better world for all” (UK GOV Cabinet Office, 2013, p. 1).

Academic literature, as well as industry and government sources, report many examples of various benefits of open government and data transparency—anticipated or already achieved. Academic literature in particular focuses on social, political, economic, operational and technical benefits (Baack, 2015; Borzacchiello and Craglia, 2012; Janssen et al., 2012; Lourenco, 2013; Zuiderwijk and Janssen, 2014). Industry reports promote open data as a new source of innovation (Manyika et al., 2013) and a common good (Tadjeddine and Lundqvist, 2016). However, despite widespread enthusiasm for open data, some researchers are voicing their concerns regarding ‘‘the enduring problems of false transparency and unintelligible disclosures” (Michener and Bersch, 2013, p. 236) and the negative implications of open data (see e.g. Bannister and Connolly, 2011; Gurstein, 2011; Janssen et al., 2012; Zuiderwijk and Janssen, 2014). Nonetheless there is an implicit and unquestioned assumption, shared both by politicians and scholars, that the benefits of open data outweigh the risks and negative effects (Zuiderwijk and Janssen, 2014). Furthermore, there is a lack of literature that investigates tensions between the positive effects and the negative, unintended consequences of data transparency (Zuiderwijk and Janssen, 2014). As Zuiderwijk and Janssen (2014) assert there is ‘‘barely any discussion going on in the literature concerning whether certain disadvantages of open data outweigh their advantages and vice versa” (p. 104).

Further concerns focus on the related area of datafication, initially introduced in relation to big data (Mayer-Schonberger and Cukier, 2013). As Mayer-Schonberger and Cukier explain to ‘‘datafy a phenomenon is to put it in a quantified format so it can be tabulated and analyzed” (2013, p. 79). Specifically, there are concerns about the datafication of a particular type of open data that represent performance of individuals, groups, institutions or government agencies (so-called open performance data). The central problem arises when open data are reused and continuously re-interpreted in different contexts and for different and unintended purposes. When this happens open performance-related data may easily produce unintended and negative implications for various stakeholders including society at large (Jeacle and Carter, 2011). For example, publication of mortality data taken to represent quality of clinical care may result in surgeons’ reluctance to operate on highrisk cases—even though these cases stand to gain most from high-risk surgery (Bevan and Hood, 2006; Marshall et al., 2000). The serious implications of these unintended consequences are discussed in more detail later in this paper, drawing on examples from prior literature in education, accounting, and public policy.

In this paper we address the concerns with social implications of transparency and datafication effects of open government information systems (IS). We use the term open government IS to denote government IS designed to provide open data to public. We focus on a specific category of open government IS that makes performance data available to public, along with the simple tools designed to enable interested parties to infer insights from these data. Of our particular interest is the ongoing tension between data transparency as the key government objective and the associated datafication effects these IS create throughout society, including various unintended negative consequences. While acknowledging that datafication may result in positive effects, such as empowerment of citizens (Loebbecke and Picot, 2015), we draw attention to the negative effects of datafication of open government IS and the government objective of data transparency. This is important due to a widespread belief that transparency of performance data increases responsibility and accountability in the public sector (Birchall, 2014; Michener and Bersch, 2013) and thus benefits everybody—governments, organizations, communities and citizens. Consequently, the government objective of transparency is more often celebrated than questioned (Michener and Bersch, 2013; Zuiderwijk and Janssen, 2014). What is particularly worrying is the widespread disregard for negative datafi cation effects of open data and the tension arising between these effects and transparency.

We thus seek to answer the following research questions: What is the nature of tension between transparency and datafi cation effects of open government IS that provide performance data? What are the underlying datafication patterns influencing the tension? We explore these questions by drawing from a case study of a controversial open government IS in Australia called My School. Currently in its 7th year of operation, the government IS My School collects and processes performance-related data from almost 10,000 schools in Australia and makes school performance data together with the simple data analysis tools open to the public. Drawing from this case study, we theorize the tension between data transparency and datafication effects of open government IS through the lens of Complex Adaptive Systems (CAS) (Benbya and McKelvey, 2006; Merali, 2006; Stacey et al., 2000). The theoretical lens of CAS is particularly useful to study the emergent nature of the open government IS and the complex dynamic relations it creates within wider society. More precisely, CAS enables us to open the ‘‘black box” of open performance data and their datafication effects and identify and theorize various datafication patterns and their societal implications. Grounded in the analysis of the My School case, we propose seven datafication patterns that explain different patterns underlying the tension between transparency and datafication effects of open performance data. These datafication patterns can be used and further refined and/or extended by other researchers interested in the societal effects of open government IS. In addition to the theoretical contribution, our paper provides an important practical contribution for strategic considerations by senior government decision-makers managing open government IS. These theoretical and practical contributions respond to Galliers et al. (2015) call for further research on the effects of datafication as well as to Newel and Marabelli’s (2015) call ‘‘for action on the long-term societal effects of datafication’ (p. 3). Through our empirical and theoretical examination of societal effects of open performance data, we extend the IS discourse on the negative datafication effects beyond privacy and security, as recommended by Markus (2015).

The paper is organized as follows. The next section provides an overview of related work from several domains of the literature including datafication and its effects, open government IS and open performance data. We then discuss the theoretical foundation of our study including a brief engagement with Complex Adaptive Systems literature and our appropriation of CAS to study open government IS. This is followed by My School case description and our research methodology. We go on to discuss our findings on the rising tension between transparency achieved through My School and its ongoing datafication effects. By engaging with CAS in the analysis of My School case we answer our research questions and theorize key datafication patterns and their societal consequences. We then discuss some important strategic implications for senior government decision-makers managing open government IS. We conclude by reflecting on our contribution to understanding transparency, open government IS and their datafication effects and offer some ideas for future IS research.

## 2. Related work

## 2.1. Datafication

Datafication of all aspects of work and personal life is in full progress (Galliers et al., 2015; Loebbecke and Picot, 2015; Lycett, 2013; Newell and Marabelli, 2015). Consequently, datafication and its effects on organizations, governments, individuals and society have attracted a growing number of researchers across several disciplines. Current literature offers promising examples of new opportunities opening up with increasing datafication such as growth in employment, improved productivity and more value for consumers (Loebbecke and Picot, 2015). However, datafication also creates negative and often unintended consequences such as the distortion of meaning, which can occur through datafication, for it can ‘‘unavoidably omit many features of the world, distort others and potentially add features that are not apparent in the first instance” (Lycett 2013, p. 384). Galliers et al. (2015) warn that ‘‘the problem with ‘datafication’ is that ‘‘somebody else may. . . use the data thus produced—often with purposes different from those originally intended’’ (p. III). Consequently, datafication has the power to re-shape the organizational, technological and cultural worlds, often in unpredictable and undesirable ways (Gitelman, 2013).

Despite these growing concerns, the wider IS community is vet to investigate undesirable negative effects of datafication on individuals, organizations and society. As observed by Markus (2015), the bulk of the current discourse on the negative data-related consequences is still very limited and mostly focused on threats to privacy and security as well as different forms of data-enabled discrimination of individuals. Yet, these negative consequences reveal only the tip of the iceberg and do not address deeper and potentially more socially damaging consequences of emerging datafication. If we are truly to develop and live in an ‘information civilization' (Zuboff 2015) current understandings of datafication and its social effects must move beyond their highly limited (Loebbecke and Picot, 2015, p. 154) and under-theorized state. Specifically, the strategic implications of datafication for individuals, governments and wider society are unclear and often controversial. Particularly questionable are datafication effects emerging from propagation and reuse of the open data made available by government IS in the name of transparency, which we discuss in the next section.

## 2.2. Open government IS and challenges of transparency

In their pursuit of transparency, accountability and citizen participation (Attard et al., 2015; Davies et al. 2013) many governments are joining the so-called ‘‘Open data movement” (also known as ‘‘Open government”). As governments continue to promote the goal of open data (Attard et al., 2015), the academic debate about government transparency continues (Meijer et al., 2014). Proponents of open government data see them as ‘‘indispensable for public policy development and service delivery . . . [and] also very valuable to citizens, organizations, and businesses for public participation, for decisionmaking, and for creating innovative products and services” (Janssen, 2011, p. 446). In contrast, Breton et al. (2007) argue that the widespread assumption that more transparency leads to better outcomes, is simply ‘‘too enthusiastic” (p. 1). Prior literature also identifies numerous risks associated with transparency, including those arising from ‘‘misinterpretation and misunderstanding of information, the ability of the public to understand this information, and the willingness of some indi viduals and groups to deliberately use transparency as a weapon to promote socially undesirable outcomes” (Bannister and Connolly, 2011, p. 24). These risks need to be weighed against the goals of increased transparency (Bannister and Connolly, 2011; Martin 2014; Meijer et al., 2014). While this stream of research identifies the tension between, on one hand, open government and transparency and, on the other hand, numerous risks of transparency including unintended negative social effects, it does not consider further risks associated with propagation and re-use of open government data. According to Meijer et al. (2014), ‘‘our academic knowledge about the effects of open data is still surprisingly limited” (p. 101). In particular, social impacts of open data are under-researched and poorly understood (Davies et al., 2013).

In addition to the current academic debate on datafication and inherent tensions in governmental attempts to be transparent, we highlight the importance of the strategic implications for the senior government decision makers in charge of decisions about the release of open data. Zuiderwijk and Janssen (2014) identify significant challenges for senior officials who may not be aware of possible misinterpretations and misuse of data and a number of trade-offs that need to be

Please cite this article in press as: Marianovic, O. Cecez-Kecmanovic D. Exploring the tension between transparency and dataficatior leffects of open government IS through the lens of complex adaptive systems. I. Strateg, Inform. Syst. (2017). http://dx.doi,org/10.1016 j.jsis.2017.07.001

considered when making data open. As Zuiderwijk and Janssen emphasize they need guidance and decision support when making decisions about releasing open government data. To meet those needs, they propose a decision-making model that includes a number of variables that should be taken into account when opening up data. However, their model for decision support does not consider possible datafication effects of open government data and the ongoing tension with the goal of transparency.

## 2.3. Open performance data

Our research focuses on open performance data in the education sector, which are increasingly made available to public in the name of transparency and accountability. Prior research offers exemplary studies of different aspects of these systems from several countries. For example, the UK government made performance data of all state schools public in the form of school league tables (Smith, 1995). Smith reported that teachers and parents warned that such simple interpretation of school performance data is misleading and dysfunctional. Similar studies were conducted in Denmark (Henriksen et al., 2011) and USA (Jacob and Levitt, 2003; Earl and Katz, 2006), all reporting serious negative consequences that could be attributed to propagation and reuse of performance data. Other researchers in education policy are raising concerns with datafication of early years pedagogy. Roberts-Holmes (2015) warns that publishing schools’ performance data results in ‘‘teachers and children’s visibility” being increased ‘‘through public displays of data” (p. 313). Roberts-Holmes’ interviews with primary school teachers offer insights into the experiences of datafication effects, including negative outcomes related to the simplistic interpretation of data, which they claim results in ‘‘harsh disciplinary consequences if targets are not met, served to ensure the head teachers focused their efforts on producing the expected data from the youngest children in the school” (Roberts-Holmes, 2015, p. 306).

In summary, prior literature (primarily published in non-IS outlets) points to important challenges of government transparency and open data (Janssen et al., 2012) and in particular open performance data (Roberts-Holmes, 2015; Smith, 1995). While the importance of open data and datafication is increasing and evidence of their effects is mounting, there is the lack of research on social consequences of open data (Davies et al., 2013; Meijer et al., 2014) and their datafication effects and strategic implications (Galliers et al., 2015; Loebbecke and Picot, 2015; Zuiderwijk and Janssen, 2014). We address these challenges and weaknesses by empirically investigating the ongoing tension between transparency and its datafication effects, which is particularly poorly understood. More specifically, we examine the following research questions: What is the nature of tension between transparency and datafication effects of open government IS that provide performance data? What are the underlying datafication patterns influencing the tension? Before we discuss our empirical study we first present the theoretical foundations of our research

## 3. Theoretical foundations

## 3.1. Complex Adaptive Systems

Complexity thinking and Complex Adaptive Systems (CAS) in particular offer important insights for better understanding the emergent nature of IS in their environments (Benbya and McKelvey, 2006; Merali, 2006). This is especially the case ‘‘in digital worlds, [where] complexity and solutions based on digital technology present new phenomena that offer new opportunities and challenges for information systems (IS) researchers and practitioners” (McKelvey et al., 2016). Yet, complex systems thinking and CAS have not found a fertile ground in IS research (Benbya and McKelvey, 2006; Jacucci et al., 2006; Merali, 2006; Merali and McKelvey, 2006; McKelvey et al., 2016; Knight, 2011).

Merali (2006) defines complex systems as ‘‘non-linear systems, composed of many (often heterogeneous) partly connected components that interact with each other through a diversity of feedback loops” (p. 219). Of our particular interest are complex systems with an added ability to adapt and evolve over time and in unpredictable ways – termed Complex Adaptive Systems. They do so because, as Stacey et al. (2000) explain, ‘‘a complex adaptive system consists of a large number of agents, each of which behaves according to its own principles of local interaction. No individual agent, or group of agents, determine the patterns of behavior that the system as a whole displays, or how these patterns evolve” (p. 106).

Reflecting on prior studies in management and other fields that adopted complexity theory and CAS, Stacey et al. (2000) warn about ‘‘the danger of regarding complexity theory as another strand in systems thinking” (p. 79). The key issue is fundamentally different understandings of the core concept of 'system'—the mechanistic versus the organic (Merali. 2006)– with different underlying teleologies and ontologies.

The dominant ‘‘classical” systems view of IS (in the IS literature) is best described as ‘‘mechanical”: the system consists of pre-defined components and their structure externally designed to achieve a pre-defined goal (Merali, 2006). The mechanical concept of a system is underpinned by rationalist teleology, assuming movement of a system towards goals chosen by rational autonomous humans. It is predicated on the ontological assumptions of persistent hierarchy (systemsubsystems), fixed causal relationships among system’s components and stable feedback loops used to regulate the system behavior so as to achieve a desirable (known or knowable) goal and a steady state (Merali, 2006). Consequently, parts of an IS are considered separate and their individual behaviors are analyzed and modelled, in order to infer the behavior/model of the ‘‘whole”. In contrast, CAS are organic systems whose components are not pre-given but contingent, assuming transformative teleology. Thus, a system can evolve in any direction, and therefore it emerges towards an unknown (and most importantly, unknowable) future state due to the non-linear interactions of its components leading to unpredictable impact on the system’s behavior. Importantly, how CAS components interact is not determined by any of the individual components nor the system as a whole, and is therefore unpredictable, having ‘‘a life of their own” (Stacey et al., 2000, p. 106).

In providing background for our use of CAS, we discuss five central concepts as follows. First, by definition CAS are open systems as they interact and exchange information with their environment in a mutually shaping manner. Changes within a system shape the system’s environment while in turn the system continues to be shaped by its environment. The environment is also considered to include other CAS. As these systems co-evolve and co-exist in an eco-system, any adaptation in one system leads to adaptation and reciprocal changes in the others (Vidgen and Wang, 2009).

Second, the ‘‘openness” property of CAS requires us to re-consider the concept of a system’s boundary as the means of distinguishing the system under observation from its environment. While the traditional view of boundaries assumes the bounds of a system, CAS assumes ‘‘a more dynamic view of boundaries as relative and relational phenomena, linking system and environmental elements through different couplings” (Merali, 2006, p. 220). Thus, a boundary is malleable, influenced by an observer and a perceived system’s purpose (Cilliers, 2004).

Third, assuming a malleable boundary we use Stacey et al.’s (2000) definition of a CAS consisting of components as autonomous and loosely connected agents. A set of agents is not stable, but constantly changing. They have ‘agency’, that is, an ability to intervene ‘meaningfully’ in response to actions of other agents (Choi et al., 2001). Agents interact typically within a very short range, based on information received from immediate neighbors (Cilliers, 2013). However, these interactions are propagated, creating wide-ranging influences. A system’s overall behavior emerges through propagation of short-range interactions occurring among its agents—each adapting to, or initiating changes in its own immediate environment. However, a system’s behavior cannot be inferred from localized behaviors of its agents<sup>1</sup> (Benbya and McKelvey, 2006). Due to their adaptive behaviors, CAS operate under conditions far from equilibrium (Cilliers, 2013, 2004) with an ever-present tension that McKelvey et al. (2016) describe as a main force behind change and new order generation.

Fourth, another important property of CASs is self-organization, which Vidgen and Wang (2009) define as ‘‘the ability of interconnected autonomous agents of a complex adaptive system to evolve into an organized form without external force” (p. 358). Rather than being pre-determined, self-organization is spontaneous and emergent, manifested through the ongoing interactions between a system and its environment as well as through local interactions among system’s components (Merali, 2006). Self-organization implies that no agent can determine the system’s change. As Stacey (2003) points out ‘‘[i]t is the very essence of self-organization that none of the agents, as individuals, nor any small group of their own, can directly design, or even directly shape, the evolution of the system as a whole. The impact of any agent, no matter how powerful, on the system is indirect through their local interactions only” (p. 267). Also, while interacting with others, each agent is ignorant of the behavior of the system as a whole and can only respond to information that is available locally (Cilliers, 2013). This point is considered to be vitally important for complexity because: ‘‘complexity is the result of a rich interaction of simple elements that only respond to the limited information each of them are presented with” (Cilliers, 2004, p. 24). To emphasize decision-making of CAS agents which is bounded by limited information and uncertainly, we term this particular characteristic of CAS as ‘‘bounded rationality” after Simon (1955, 1979). In doing so, we also expand Simon’s concept of ‘‘bounded rationality” to societal context beyond management decision making within organizational boundaries where it was originally proposed.

These local interactions also have other important characteristics. They are non-linear which means that small local changes may have disproportionally large and unpredictable effects on other parts of a system as well as a system as a whole. This phenomenon is known as the ‘‘butterfly effect” (Cilliers, 2004). The interactions involve and are shaped by various feedback loops that can be positive (enhancing, reinforcing) or negative (inhibiting, correcting, regulating). Both kinds are considered necessary and exist simultaneously in a CAS (Cilliers, 2004). As Madden et al. (2012) emphasize, it is ‘‘[t]hese interactions and relationships among agents, rather than agents themselves, [that] define CAS” (p. 693). Such a conception of CAS implies its malleable boundary.

Last, each agent acts locally in pursuit of its own goal—the behavior known as ‘‘individual optimality” (Choi et al., 2001). Different agents have individual and often competing or mutually inconsistent goals that they pursue at the same time. Because individual localized goals are ‘optimized’ in isolation and without any regards for the others Choi et al. (2001) warn that ‘‘optimization [of a CAS as a whole] can be an illusion” (p. 355). Metaphorically speaking a CAS’ landscape is ‘‘rugged”, consisting of many ‘‘peaks” corresponding to different goals optimization (Merali, 2006; Choi et al., 2001). Consequently CAS are emerging in unpredicted and unpredictable ways. The source of this emergence can be found in the pattern of conflicting goals and constraints that create an ongoing tension which results in further adaptation. Through interactions system’s components co-evolve and their learning and mutual adaptation trace an emergent pathway into the future rather than converge towards some equilibrium (Allen and Varga, 2006, p. 230). Consequently, the future is not and cannot be pre-determined. Instead, it is unknown and unknowable as it emerges through agents’ interactions. CAS thus always have histories with their past influencing their present behavior (Cilliers, 2004). Any analysis of these systems that does not consider their evolution over time is thus considered incomplete, merely a snapshot that prevents understanding systems’ behavior.

In the absence of a clear dominant theory of CAS (Madden et al., 2012), we base our work on the main characteristics of CAS identified by Cilliers (2004, 2013), Stacey et al. (2000), Stacey (2003), Merali (2006) and Benbya and McKelvey (2006), as discussed above. In the following section we briefly describe our interpretation of open government IS as a CAS

## 3.2. Appropriation of CAS to study open government IS

This study is predicated on the understanding of open government IS as a CAS. Conceptualizing open government IS as CAS enables understanding of complex interactions of numerous agents using open data in a wider societal system, itself a complex adaptive system (Allen and Varga, 2006; Buckley, 2013; Merali, 2006). This allows us to explore the emergence of open government IS driven by the transparency goal and reveal the tension between the IS and its datafication effects in the wider social system. We can also explain why the boundaries of an open government IS system cannot be controlled and how its influence and impact (through datafication) in the wider system cannot be predetermined or predicted. Table 1 provides a summary of the main characteristics of open government IS as CAS, informed by prior work of Cilliers (2013, 2004), Stacey et al. (2000), Stacey (2003), Merali (2006) and Benbya and McKelvey (2006) discussed above. This forms a foundation for our theorizing of datafication effects of open government IS.

Conceptualizing open government IS as CAS allows us to explore the nature of ongoing tension between transparency (achieved by making performance data open to public) and datafication effects. We also theorize this tension and underlying datafication patterns in order to discuss their societal consequences and strategic implications for government decision makers responsible for making data open.

## 4. Research methodology: An interpretative case study

## 4.1. Research context – the My School case study

To answer our research questions about the nature of tension between transparency and datafication effects, and the underlying datafication patterns, we draw insights from an interpretive case study of My School. The history of My School began in July 2006 with the formal approval of nation-wide testing in literacy and numeracy. The new government agency called the Australian Curriculum Assessment Report Authority (ACARA) was formed and made responsible for development of the so-called National Assessment Program – Literacy and Numeracy (NAPLAN) test (ACARA, 2010). In 2008 and 2009 ACARA administered NAPLAN tests to all Year 3, 5, 7 and 9 students in all Australian schools. The tests results in both years were returned to schools and parents for self-assessment and improvement (i.e., they were not publicly available).

However, this internal ‘‘feedback loop” from ACARA to individual schools was made visible outside of the education system in January 2010 when ACARA launched the so-called My School web site/portal. Through My School, ACARA made school NAPLAN test results (performance data) available to public. This was done in response to the new education reform agenda to move towards ‘transparency in reporting and assessment’ (ACARA, 2010). When launched, My School included two sets of NAPLAN results for 2008 and 2009.

Now in its 7th vear of operation. My School provides open performance data of almost 10,000 schools (see an info graph of My School in Appendix A). Government argues that My School provides ‘‘valuable data to support good teaching and learning and school improvement” that benefit students, schools and the education system (ACARA, 2016, p. 1). However, numerous unintended negative effects of My School for children, parents, teachers, school principals and schools have been publicly reported and studied by many (non-IS) researchers (see e.g. Mocker, 2013; Lingard et al., 2016; Mocker, 2016; Thompson et al., 2016; Thomson and Cook, 2013). As a result of public concerns, My School has been subjected to two Senate inquiries (in 2010 and 2014) and two major reviews commissioned by the Australian Government (see Cook, 2014; Ziino and Matheson, 2015). These public inquiries and reviews reflected the tension between the Government’s transparency policy (implemented through My School) and the reported negative effects produced by misinterpretation, misuse, propagation and reuse of school performance data.

Being an open government IS, My School is heavily regulated. Consequently, all evidence—Government policy documents, all submissions and official transcripts of public hearings conducted during both Senate inquiries, interim and the final Government reports containing recommendations for improvement, and debates—is publicly available. The My School case thus offers ample empirical material to study the use of open performance data and their consequences.

## 4.2. Research approach, data collection and analysis

We approach My School case as a case of’ an open government IS that provides performance data to the public which is a novel phenomenon. This type of government IS is not recognized as such and its nature, functioning and effects in society are not known. The lack of distinction between a general concept of government IS that serves governments and citizens (Attard et al., 2015; Janssen et al., 2012; Bannister and Connolly, 2011) and the open government IS that provide performance data to the public is not only theoretically relevant, it is also practically consequential. Due to such lack of distinction open government IS are treated as any other government IS thus preventing recognition of their specific negative social effects that warrant investigation and appropriate action. By emphasizing that our My School case is ‘a case of’ (Tsoukas, 2009) we indicate

Please cite this article in press as: Marianovic, O. Cecez-Kecmanovic D. Exploring the tension between transparency and datafication leffects of open government IS through the lens of complex adaptive systems. I. Strateg. Inform. Syst. (2017). http://dx.doi.org/10.1016 j.jsis.2017.07.001

Table 1  
Interpreting open government IS as CAS.

<table><tr><td>CAS characteristics</td><td>Open government IS as CAS</td></tr><tr><td>Openness</td><td>Open government IS is embedded in and is co-evolving with the wider societal system, itself a complex adaptive system;</td></tr><tr><td>CAS are open systems because they interact with their environment in a mutually shaping manner; Components of CAS are autonomous and loosely connected agents; A collection of agents is changing indicating that CAS&#x27; boundaries also change; CAS thus have malleable boundaries.</td><td>The boundary of the open government IS is malleable as various agents in society become or cease to be its users.</td></tr><tr><td>Transformative teleology</td><td rowspan="2">An open government IS involves many agents (including, e.g., government agency and numerous unpredictable users), each of which may have its goal but neither of which can determine the whole system&#x27;s goal or its outcomes; This is due to society-wide propagation and reuse of data by unpredicted users in unpredictable ways; As a result open government IS does not have a known or knowable future.</td></tr><tr><td>There is no final goal or outcome that a CAS is working towards; The future of CAS is unknowable.</td></tr><tr><td>Interactions and emergence</td><td>Open government IS is defined by dynamic and unpredictable interactions among unpredictable and loosely connected agents; The influence and impact of open government IS (through datafication) are neither predictable nor determinable due to unpredictable and non-linear interactions among agents, and emerging positive and negative feedback loops.</td></tr><tr><td>Dynamic interactions and relationships among agents, rather than agents themselves, define CAS; Interactions are local and short ranging, but through propagation their effects may be wide-ranging; Interactions arenon-linear(i.e. small changes can create disproportional effects).</td><td rowspan="2">After implementation an open government IS emerges through mutually shaping interactions among its various agents as well as their interactions with the wider social system.</td></tr><tr><td>There are feedback loops in interactions among agents that could be positive (enhancing, stimulating) or negative (regulating, inhibiting). CAS overall behavioremergesthrough ongoing and mutual interactions of its agents.</td></tr><tr><td>Self-organization</td><td rowspan="2">Autonomous agents involved in open government IS (government agency collecting, processing and producing open data; citizens using the data; professionals; public sector organizations whose performance data are being collected and made public) change through local interactions, each behaving according to their own goals, principles and intentions.The impact of any agent on the whole open government IS is indirect through their local interactions only; No agent can directly shape the evolution of the whole open government IS.</td></tr><tr><td>Autonomous agents as components of CAS self-organize spontaneously through local interactions—each behaving according to their own goals, principles and intentions; None of the individual agents can directly shape the evolution of CAS as a whole.</td></tr><tr><td>Adaptation</td><td rowspan="2">As agents within open government IS adapt to the behaviors of others (through action and reaction), the overall system changes. For example, open performance data are interpreted as indicators of schools&#x27; quality leading parents putting pressure on schools; Schools, in turn, change teaching practices and entrance policies.The behavior of open government IS cannot be controlled by any of its agents (including the government agency) because open data continue to be propagated and re-used in uncontrollable and unpredicted ways.</td></tr><tr><td>Agents are able to adaptonlyin response to changes in their local environment, that is, neighboring agents&#x27; behavior and their actions; They can also initiate change, again only in their local environment; None of the agents can control or design the whole system, and can only act locally in their own environment.</td></tr><tr><td>Bounded rationality</td><td rowspan="2">The behavior of the government agency as an agent of open government IS is characterized by bounded rationality. While the government agency is the owner of open data, it cannot know the full extent of data propagation and reuse by other agents; However, it has the means to broaden interactions with users and thus reduce ignorance of IS effects on users (that is become less bounded in its rationality).</td></tr><tr><td>Each agent of CAS only responds to limited information (interactions) that is available to it locally and is thus ignorant of the behavior of CAS as a whole.</td></tr><tr><td>Individual optimality</td><td rowspan="2">Open government IS is introduced to achieve transparency—this goal is assumed to be desirable for society.When government pursues its goal despite the negative effects on other agents (students, teachers, schools) or the education system as a whole, government behavior exhibits individual optimality</td></tr><tr><td>Each agent of CAS pursues its own goal that is best for it, but may not be good for others or good for the whole system.</td></tr></table>

that we not only aim to provide a rich description of the particular case of My School (which we believe is in itself useful). We aim also to develop conceptual abstractions that help characterize the distinct nature of such kind of open government IS. Our study is thus intended to contribute to understanding the phenomenon of My School in its particularity as well as make a case for a more general phenomenon of open government IS that provide performance data to the public

As this approach appreciates the ‘epistemology of the particular’ (Tsoukas, 2009) and attention to the context we adopt an interpretive research methodology founded on hermeneutics as both a philosophy and a methodology for interpreting meanings (Gadamer, 1960, 1976; Crotty, 1998). Consequently, we assume that understanding is always a practical, lived and temporal experience and that interpretation is inevitably provisional and progressive, never ‘finally correct

Please cite this article in press as: Marianovic, O. Cecez-Kecmanovic D. Exploring the tension between transparency and dataficatior leffects of open government IS through the lens of complex adaptive systems. I. Strateg, Inform. Syst. (2017). http://dx.doi,org/10.1016 j.jsis.2017.07.001

(Heidegger, 1962). Following this approach and methodology, our interpretation of My School has emerged gradually through a dialogical engagement with growing empirical evidence from a variety of sources. The hermeneutic way of understanding has helped us gain insights into and develop a rich description of My School emergence within a wider societal system and answer our research questions. Through the development of the rich description of the My School case we derived conceptual abstractions of datafication patterns that reveal how such open government IS emerge in a broader social context and produce negative effects.

Importantly our hermeneutic analysis is also underpinned by philosophy of CAS discussed above (Cilliers, 2004; Merali, 2006). The longitudinal nature of our study (2006–2017) has allowed us to explore history of My School emergence and ongoing adaptation that is relevant for any CAS (Cilliers, 2004). We have followed the design and introduction of NAPLAN testing since 2006 (when it was first announced) and My School since its inception in 2008 (two years before it went online in 2010) and have continued to the present time. Following Merali’s (2006) recommendation that CAS has to be studied simultaneously from the perspective of different agents, we have studied My School datafication effects from the multiple perspectives of different agents and through their interactions.

We have collected all relevant documents, reports, My School website content, government and independent research reports as well as media articles since 2006. Data analysis started together with data collection. We read documents as soon as they were acquired and classified each according to the origin (source/authority), relevance, purpose, key topics, relevant actors, datafication effects and related events on the My School timeline. Such reading and our classification have provided broad insight into emerging discourses, significant actions by various social actors, and claims to benefits and arguments about negative implications. Based on our initial classification, we selected documents relevant for addressing research questions explored in this paper. In Appendix B we list a sample (out of 430 selected documents) of the most relevant documents used for this research including the most authoritative documents made available on the Australian government websites, documents from 2 Senate inquiries, newspaper articles and various reports.

We then coded selected documents by identifying sections of the text related to: (a) the Government objective of data transparency; development and introduction of My School and achievement of data transparency in practice (My School provision of data and tools); (b) propagation and reuse of data by many social actors (i.e. datafication) and traced consequences of their actions. We interpreted the identified sections of the document in the context of the related event along My School timeline (e.g. introduction of My School in Jan 2010; Senate inquiries; Government responses). Each document and its selected sections contributed to our emerging view of My School within a broader societal system. At the same time, the emerging view of My School embedded in an overall societal system informed a deeper understanding of these events, individual documents and selected sections. In such a way, our interpretation involved a number of continuously widening hermeneutic circles, enabling growing understanding of My School, data proliferation, and specific datafication effects as we continuously moved from the parts to the whole and then from ‘‘the whole to the part and back to the whole” (Gadamer, 1976, p. 117; Crotty 1998). Understanding documents and related events, on the one hand and My School within the social context, on the other, were mutually informing (Gadamer, 1960, 1976). In this way, we gradually developed a holistic, historically and socially situated, multi-agent understanding of My School and its emergence within the societal system. Importantly this understanding clarified the dynamics of data propagation and reuse and various datafication effects of My School.

Thus, through recurrent hermeneutic circles we observed and interpreted My School as a complex adaptive system, embedded and co-evolving within a broader societal system (itself a CAS) (Buckley, 2013; Merali, 2006). We focused on the emerging tension between government’s goal of transparency in the Australian education sector (realized through My School) and the reported consequences of propagation and reuse of data. Importantly, we interpreted this tension from the perspectives of different agents as it evolved through their complex dynamic interactions (Weick, 2007). Thus, we investigated the tension from the perspective of ACARA (expressed on My School website and Government documents), perspectives of schools and teachers (and their associations), perspectives of students and their parents (expressed in media articles and Senate inquiries), as well as perspectives of journalists and newspapers. This approach enabled us to discover how the data from My School were propagated, used and reused, and how in turn the meanings intended by ACARA became transformed and distorted (discussed below). This analysis further revealed how the distorted meanings produced specific unintended negative effects on some children, parents, teachers, and schools as well as teaching practices and the education system.

While interpreting the empirical evidence and developing in depth understanding of the My School case we engaged simultaneously in another hermeneutic circle that we term ‘from the particular to the general and back’. This hermeneutic circle characterizes interpretive studies that attempt to abstract from a specific case and infer some general features of a type of phenomena the case exemplifies. While attending to the particular of My School and developing rich descriptions we also revealed some general datafication patterns at play when performance data are made open to the public by a government. Such hermeneutic analysis focused on the particular while at the same time moving beyond the particular, looking ‘‘for patterns and their systemic implications” (Stacey, 2006, p. 96). Through abstracting from the particular of My School case we identified seven different types or exemplary patterns of the underlying datafication processes that produced and are continuing to produce the negative effects. We propose datafication patterns as open-ended generalizations that ‘‘aid generic understanding without annihilating the epistemic significance of the particular” (Tsoukas, 2009, p. 287). These datafication patterns (described in the Discussion section) are heuristic in nature, they help identify new distinctions that make a difference in understanding unintended social effects of transparency and a type of open government IS that achieve it. In this hermeneutic process datafication patterns were iteratively abstracted from and then instantiated in the My School case, leading to further refinement and elucidation. Paraphrasing Tsoukas (2009), the particular datafication processes are not subsumed into the general datafication patterns, they ‘‘rather further specif[y] the general” patterns (p. 288).

Keeping in mind that Gadamer’s hermeneutic approach to understanding and interpretation is not reducible to a technique, the assessment of quality of our hermeneutic inquiry needs to be grounded in its epistemological assumptions. That our understanding and conceptualization of datafication patterns emerged though dialogical hermeneutic processes (a two fold hermeneutic circle between the parts and the whole and between the particular and the general) suggests that such theorizing is contextually situated and practically oriented. As a result the mode of insight into the My School case as our practical ‘being-in-the world’ led to rich and authentic reporting (evidenced in the Research findings section) and plausible argumentation and theorizing (provided in the Discussion) as the key processes of convincing (Golden-Biddle and Locke, 1993; Guba and Lincoln, 2005). In the hermeneutics tradition we also deliberately nurtured openness to different agents perspectives, their concerns, voices, claims and counterclaims (Weick, 2007). However, as hermeneutic researchers employing CAS we acknowledge that we also (and inevitably) become a part of the system we study (Merali, 2006).

## 5. Research findings – Transparency and datafication effects of My School

## 5.1. Government commitment to transparency

The Australian Government’s strong commitment to transparency of the education sector is demonstrated by the following ongoing activities: collection and provision of open data; technical improvement of the My School portal and the associated processes; engagement in ongoing public debate; and continuous activities designed to improve users’ ability to understand and analyze data in order to derive their own insights.

When launched in Jan 2010, the My School portal provided two sets of data (2008 and 2009) collected from around 9.500 schools. Today, the portal provides nine years of data from almost 10.000 schools (ACARA, 2016). Over time data sets have been expanded to provide more data types, such as recently included student attendance data (My School, 2016). To facilitate a more appropriate comparison between schools, ACARA also engaged in generation of new data, using its own proprietary methodologies developed by experts for this particular purpose. Examples include the so-called Index of Community Socio-Educational Advantage (ICSEA) and financial data (The Australian Senate, 2010).

Considerable efforts and resources continue to be invested in ongoing technical improvements of the My School portal: ‘‘Many enhancements have been made to My School since its release in 2010, such as better functionality, improved navigation, new categories of information and more financial information. Changes reflect decisions made by ministers for education, as well as feedback from stakeholder and consumer groups” (My School, 2016).

Following the recommendation of the Second Senate Inquiry, from 2017 NAPLAN tests will be administered online. The main objective is to improve the efficiency of data collection and processing. According to Lingard et al. (2016), the Australian Government has already committed resources to NAPLAN online ‘‘with the promise that online tests will provide faster feedback and deliver a more sophisticated and personalized test through adaptive, branching logic in the test items. It is claimed that branching creates pathways for students with different abilities to take different test items so a more accurate measure of student capability is provided” (p. 9).

Government’s engagement in the public debate started before My School was launched and continues to this day. For example, the day before My School went live, the then Federal Minister of Education issued the following invitation to the Australian public:

‘‘The much talked about, much criticised, My School website will go live tomorrow, and I urge you to log on, explore and judge the new resources for yourself. . .For the first time, parents will be able to see exactly how their child’s school is doing. The My School web site is the big step forward. It will shine the light on schools that are bolting ahead, allow us to look at that best practice and share it around. It will also shine the light on those schools that may be struggling to teach the basics and need a helping hand.” (Gillard, 2010)

Another important form of engagement with the public relates to ACARA’s ongoing efforts to educate the public about the nature of NAPLAN tests and data being collected:

‘‘It should be emphasised that NAPLAN is a tool to inform school improvement, not an improver of educational outcomes. It is not the tests that will improve students’ literacy and numeracy skills, but the way students’ results (including school, system and national level results) are used by teachers, schools and systems to identify strengths and weaknesses, particularly in teaching practices and programs, that will improve student outcomes”. (Second Senate Inquiry, Submission 58, p. 7)

Nevertheless, empowering users to analyze data in order to infer their own insights remains one of the key challenges of My School with considerable efforts and resources invested in this activity. There are ongoing problems with this as Gorur (2016) observes in relation to the first year of My School, ‘‘[d]espite claims of transparency, the methods and calculations were presented as too complex for the average citizen to understand” (p. 39). The ICSEA provides a good example of this complexity; it is used for grouping and comparisons among similar schools yet, its meaning and applications are frequently misunderstood or misinterpreted. The same observation also applies to the underlying method used to determine the value of this index for different schools. Consequently, the appropriateness and accuracy of ICSEA is widely disputed and remains a matter of public debate (Gorur, 2016).

## 5.2. Evidence of datafication effects

Through propagation and reuse for purposes other than those intended, the school performance data have acquired a life of their own. As Lingard et al. explain, ‘‘this life extends well beyond classrooms and schools to the reworking of political and educational systems and the integration of testing data with other data sets created outside of education and beyond the nation” (Lingard et al., 2016, p. 15). The reported effects of this society-wide datafication are positive, negative or highly debatable (i.e., positive for some, negative for others).

Notable examples of positive effects include data analysis by public activists such as Bonnor and Shepherd (2016) who demonstrated that more funding does not lead to improved learning outcomes. Similarly, independent researchers Miller and Voon (2012) analyzed the performance of government versus non-government schools, tackling some common misconceptions about the superiority of one over another.

Furthermore, as data continue to be propagated throughout society, a wider group of stakeholders are deriving value from My School data. For instance, by combining My School data with their own proprietary data, financial and property advisors are now publishing reports about the impact of My School on property prices and offer advice about ‘‘good value for money schools”, see for example (Green, 2015; Finder.com, 2016; PropertyValue 2016).

However, any other unintended use of My School is overshadowed by public media’s controversial use of data and construction of the so-called school league tables. For example, within hours of My School going live, public media started publishing school league tables on the basis of their own, crude analyses of the My School data (Herald Sun Editorial, 2010). In one instance, a leading national newspaper produced ‘‘a ‘wrap-around’ of school ‘results’, based on aggregating 10 test results and producing an average mark” (NSW PPA, 2010, p. 2). Arguing that previously parents had to make their choices on ‘‘anecdotes and gossip” (Canberra Times Editorial, 2010, p. 8), media promoted My School as the place to obtain ‘‘critical information” to make ‘‘one of the most important decisions of their lives: where to send their children to school” (Herald Sun Editorial, 2010, p. 30). Others argued that accountability is essential for school improvement (The Australian Editorial, 2010), school leagues are necessary (Sydney Morning Herald, 2010a), and that students will benefit from scrutiny of schools and teachers (The Advertiser Editorial, 2009; Sydney Morning Herald Editorial, 2010b). The media fully supported and celebrated the provision of ‘‘objective, measurable and reputable data” about school performance (Mocker, 2013), warning that ‘‘[t]he teaching profession should accept that it cannot shield misfits” (Sydney Morning Herald Editorial, 2010b, p. 12).

While many parents welcomed the publication of the school league tables, media hype and sensationalism started to create what was labelled ‘‘parent frenzy” (Lam, 2010). This resulted in parents withdrawing their children from ‘‘underperforming schools” and seeking to enroll them in ‘‘high-performing” ones (Lam, 2010). School authorities were also concerned about the influence of the media. Schools were labelled ‘‘good” or ‘‘bad” depending on their ranking. The media also took it upon themselves to start ‘‘teaching” parents (i.e., consumers) to read the abstract data so that they can ‘‘interrogate good teaching’” (Mocker, 2013; Thomson and Cook, 2013). In response, the Australian Secondary Principals Association (ASPA) and the NSW Primary Principles Association raised a number of concerns with the Australian government about mis: use of My School data (ASPA, 2010; NSW PPA, 2010). In particular, they highlighted the over-simplification of data and their misinterpretation as well as the potentially serious consequences of publishing school league tables (NSW PPA, 2010). This unexpected and unprecedented public attention, media interference and ensuing avalanche of concerns and complaints resulted in the First Senate Inquiry in May 2010, less than six months after the launch of My School. The 268 public submissions to the First Senate Inquiry further confirmed the extent and nature of both positive and negative effects of datafication on all actors included in the education process.

Different parent groups had opposing responses to publishing the data. The Australian Parents Council argued the case for their rights for access to My School data, claiming that ‘‘parents need and are entitled to information on their children’s education and progress” (First Inquiry, Submission 233). At the same time, another large association of parents and citizens claimed that publishing open data:

‘‘. . .punishes, humiliates and demoralizes students, teachers and schools who have been singled out by the crude and at times inaccurate comparisons made between apparently ‘‘similar” schools as well as from the creation of simplistic league tables by the media and other organizations.” (First Inquiry, Submission 226, p. 6.)

Their central concern and that of other groups and individuals is the labelling students as ‘good’ or ‘bad’ based on their NAPLAN test scores, making them thus more or less desirable in a school or a class. Concerns grew as it was reported that some schools discouraged ‘bad’ students from enrolment or took a discriminating actions against the students with low scores (see Anderson. 2010: Barry. 2011). It was also reported that some students were advised not to come to school on the testing day. Apart from the obvious negative impacts of these unintended outcomes of the Government’s transparency agenda, this parent’s submission highlights a more insidious impact of school ranking on children:

‘‘Children are especially vulnerable, and if labelled as low achievers, tend to feel that it’s pointless to try harder. We need to make school results more accurate and detailed without simplistic labels, so that parents know where their child needs more help, but the child doesn’t feel like a failure.” (Fist Inquiry, Submission 153, p. 1).

A number of submissions reported on teachers’ experiences and the effects of datafication on teachers:

‘‘. . .not every school can be at the top of the pile. . .teachers like myself will become disillusioned and add to the burnout statistics” (First Inquiry, Submission 49, p. 1).

‘‘[T]eachers now had their reputations at stake and had been given an incentive to teach strong performers and gifted students” (First Inquiry Submission 200, p. 1).

At a subsequent public hearing, (conducted on the 29 Oct 2010) even ACARA confirmed its strong position against league tables:

‘‘One thing that I think every educator would agree with is that we do not want league tables. A league table, to my mind, is where you rank schools without regard to the nature of the students within the school. My School explicitly does not do that, and all of us in Australia are very much against having league tables (First Inquiry, Proof Committee Hansard, p. 75)

During the same public hearing, the Australian Primary Principals Association offered their view that NAPLAN testing had turned into a ‘high stakes” test because of \$350 million of reward money offered to schools for improvement in their NAPLAN scores and the My School web site that made the performance public:

‘‘We think it is fantastic that there is money for schools in need. That is a big tick. But when reward money is used to threaten principals or set targets—you must improve by five per cent or 10 per cent before you can get the reward money—I think that has a perverse effect of what the reward money is intended to do. . . That is what we have to keep in perspective—it was not happening before [public availability of test results via My School]. We do not have a problem with students doing the NAPLAN test; we have always supported the NAPLAN test. The test itself is not the problem”. (First Inquiry, Proof Committee Hansard, p. 5)

The first Senate Inquiry confirmed the negative effects of My School data on a large segment of students, parents, teachers and schools. Based on collected evidence, the committee produced 12 recommendations regarding My School improvements and the use of public data (Australian Government, 2011; The Australian Senate, 2010). They included changes to the publication and representation of test data, improvements to the My School portal and the recommendation not to publish lea gue tables in media.

However, apart from the recommended technical improvements, not much has changed in terms of data use, the datafication effects and their societal consequences (The Australian Senate, 2014). Media persisted with publishing and promoting school league tables. The public controversy continued and a Second Senate Inquiry followed in 2014. The new round of sub: missions echoed the sentiment of submissions made to the First Inquiry. For example, an experienced teacher spoke of the way her teaching was negatively impacted:

‘‘. . . since NAPLAN, my teaching time has been greatly reduced. I have felt pressure to ‘teach to the test’ enabling my students to understand the test format (multiple choice comprehension questions) and how to complete a formulaic persuasive writing response. This bears very little resemblance to what I consider to be excellent literacy learning” (Second Senate Inquiry, Submission 86, p. 1).

A principal voiced his concerns about the role of media in promoting league tables, commenting on the negative effects it had on disadvantaged schools and their teachers, students and parents:

‘‘Dismantle the opportunities for the ‘‘media circus”, supported by NAPLAN and My School reporting. The celebration of the ‘‘already advantaged” is denigrating to disadvantaged schools and undermines the confidence of their teachers, students and families. Take action when NAPLAN results are used for self-promotion, program promotion and exaggerated claims (i.e. the rhetoric and marketing of ’improvement’)” (Second Senate Inquiry Submission 82, p. 3).

The above evidence illustrates the public controversy and tension between transparency achieved by open school performance data (via My School) and society-wide datafication effects that continue to this day (see for example APPA, 2014; The Australian Senate, 2014; Wyn et al., 2014; Bonnor and Shepherd, 2016; Mocker, 2016; Wiltshire, 2016). While strong claims have been made attesting to serious datafication effects, the underlying patterns creating these effects remain unclear and thus require further explanation and theorizing as described in the next section

## 6. Discussion

6.1. The nature of tension between transparency and datafication effects

The empirical evidence shows that tension between transparency and datafication effects has been rising since ACARA made NAPLAN test data for individual schools (performance data) open to the public via My School. To understand the nature of this tension we look at the goals and actions of the key agents. It is clear that transparency in the education sector remains

Please cite this article in press as: Marianovic, O. Cecez-Kecmanovic D. Exploring the tension between transparency and dataficatior leffects of open government IS through the lens of complex adaptive systems. I. Strateg, Inform. Syst. (2017). http://dx.doi,org/10.1016 j.jsis.2017.07.001

the main goal and the driving force behind My School. On the other hand, as soon as My School data were used to create simple school league tables, which were then published by newspapers, the meaning of school performance data (NAPLAN test results) changed: the data were interpreted as evidence of ‘school quality’. Hence schools became ‘good schools’ or ‘bad schools’ depending on the ranking in the league tables. This had further effects on students: their literacy and numeracy (NAPLAN) tests became important as contributors to school ranking and thus students with above average scores were considered ‘good students’ while the others were ‘bad students’. Consequently teachers became ‘good teachers’ or ‘bad teachers depending on their students’ scores. As we can see, such labelling of schools, students and teachers, all resulted from datafication caused by proliferation and reuse of My School data throughout the society. As data got propagated and reused they became further and further disconnected from the original context and meaning of the NAPLAN test and the intended use of data.

The tension continued to rise as different agents (ACARA, media companies, schools, parents, students and other agents in the education system) use My School data (and also their reinterpretation) to pursue their own individual goals irrespective of, or even unaware of, the effects on other agents. Starting with ACARA, they continued to pursue the goal of transparency by working on technical improvements to data provision and methodologies for processing them. This was evident in ACARA’s response to public criticism and recommendations from Senate inquires, where they committed to improve the accuracy of data on the My School website and efficiency of their collection. While ACARA persisted with this approach, the media celebrated and sensationalized My School (that will revolutionize education') and continued to publish simple school league tables, in spite of Senate recommendations not to do it. Individual schools, on the other hand, pursued their goals of improving ranking and/or acquiring more funding. Schools adopted various strategies, with some discouraging enrolment of ‘low achievers’, while others adopted practices of ‘teaching to test’, at the expense of planned curriculum. These and many other actors in the education sector used My School data as well as data reinterpretation by other agents (e.g. school league tables derived from the data) to ‘optimize’ their individual performance, while disregarding the effects on others. In other words, by seeking individual optimality (Cilliers, 2004), responding to other actors’ actions in unexpected ways, and using available information without considering the wider social effects, actors are contributing to increasing tension despite Senate inquiries and Government attempts to address it.

We conclude that the tension between transparency and datafication effects of open government IS emerges through mutually shaping interactions among many actors as they adapt to changes in their local environment. In the case of My School, this tension was initially triggered by open government data and continues through data propagation and reuse. Actors initiate further changes by reusing open data in pursuit of their individual goals that may be best for them but not good for (other) students, teachers, schools, the education sector and society as whole. As different actors pursue different, and as we have seen, often incompatible and competing goals, this tension is oscillating with the resulting effect having a ‘‘rugged” landscape (Cilliers, 2004). In this landscape, some actors manage to achieve their goals (often at the expense of others) at different points in time. However, no single unifying goal for the whole open government IS has been achieved or imposed by an individual agent, no matter how powerful.

This analysis taken from the CAS perspective reveals the nature of tension between transparency and datafication in open government IS. Based on the rich and comprehensive publicly available evidence (and illustrative examples provided above), our analysis shows that this tension arises due to proliferation and reuse of open performance data in unpredictable and unexpected ways by numerous users. Through proliferation, reuse and reinterpretation of data the original meaning of data is distorted: NAPLAN test results are interpreted as the measure of schools’, teachers’ and students’ performance and then used as legitimate and objective information to support actors’ decisions. In such a way all involved actors were seeking their individual optimality (parents choosing the ‘best’ school; schools discriminating against ‘low performing students’ and punishing ‘non-performing’ teachers; teachers ‘teaching to test’). The tension arises in a cascading manner—one actor’s reinterpretation becomes information for other actors who in turn re-interpret it again and take action to ‘optimize’ their goals. Proliferation of data and its cascading datafication effects are unpredictable and most importantly non-linear in nature. This means that more transparency may or may not lead to more datafication effects. This also means that we cannot predict that datafication effects will be automatically reduced, by reducing the existing level of transparency. Therefore, our My School case ably illustrates that the datafication effects of open government IS are unpredictable, far reaching, and not centrally controllable. Open government IS thus have an unknowable future.

## 6.2. Datafication patterns of open government IS

Through our hermeneutic analysis and the engagement with the empirical material from the My School case study, we identified seven different datafication patterns. In this section we define each datafication pattern and explain how it manifested in the observed open government IS (My School). We also provide examples of its unintended societal consequences. They are also summarized in Table 2.

## De-contextualization

De-contextualization of data happens when data get propagated and separated from their original contexts and then reused in other (unforeseen) contexts. As the original context gets effaced, reinterpretation of data in a new context may create new meaning, often different from the initially intended one. In the case of My School, the data were generated in a particular context, that is, in the educational context of a particular school, with students in particular classes who were doing a standardized numeracy and literacy (NAPLAN) test, at a particular point of time. As test score data get propagated, processed and reused new meanings are attached: for example, the test data are interpreted as the evidence of ‘‘school performance” or ‘‘teaching quality”, that is used to determine ‘‘good” or ‘‘bad” schools. The initial meaning of school NAPLAN test scores is lost, and new meanings of school performance continue to be used and propagated further. As described earlier these new meanings are then used by various agents in pursuit of their own goals

```txt
Please cite this article in press as: Marjanovic, O., Cecez-Kecmanovic, D. Exploring the tension between transparency and datafication effects of open government IS through the lens of complex adaptive systems. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.07.001
```

Table 2  
Datafication patterns of open performance data, their CAS manifestations and unintended societal consequences.

<table><tr><td>Datafication patterns</td><td>Example from My School case</td><td>Open government IS as CAS</td><td>Examples of societal consequences</td></tr><tr><td>De-contextualizationData taken out of original context and then propagated and used in other contexts</td><td>NAPLAN test data collected and processed by ACARA and made publicly available on My School portal are used and interpreted as indicators of &#x27;school quality&#x27; expressed in School league tables</td><td>- Impact on bounded rationality of individual agents determined by their access to and ability to understand different information- As new meanings of data get used in pursuit of individual goals: actors seek their individual optimality based on distorted interpretation of data</td><td>- De-contextualized information derived from the My School portal (such as school rankings) propagated further and used as given and valid facts;- New meanings attached to My School data: schools considered &quot;good&quot; or &quot;bad&quot; schools (effacing the meaning of data in their original context - students&#x27; NAPLAN test results)</td></tr><tr><td>RecombinationCreation of new data/information through re-combination of de-contextualized data from other sources</td><td>Recombination of My School data with financial and real-estate data, used to produce new information about &quot;good value for money schools&quot; and to forecast future real-estate trends</td><td>- Impact on bounded rationality of individual agents as they acquire new data/information (that may be misleading because of the missing original context)- Amplified individual optimality of agents executing re-combination of data to derive new value from data in pursuit of their local goals</td><td>- Parents make renting/buying decisions based on misleading information (about &quot;good value for money schools&quot;); this in turn creates disproportional demand for enrolment across schools- New meaning of &#x27;good&#x27; and &#x27;bad&#x27; schools, teachers, and students inferred from school league tables and their interpretations by different agents- Real-estate prices affected by the perceived &#x27;quality of schools&#x27;</td></tr><tr><td>Using quantified proxiesUsing quantified data as proxy measures for complex phenomena</td><td>- The use of NAPLAN test results to express (quantify) complex phenomena of learning and teaching quality-The use of quantified measures to represent socio-economic status</td><td>- Impact on bounded rationality of individual agents as new measures (proxies) are taken to be objective and valid representations of schools&#x27; quality- Individual optimality guided by quantified proxies as measures of complex phenomena</td><td>- Complex decisions on interventions (funding) to improve school performance based on oversimplified proxy measures;- Schools change their practices to improve schools&#x27; score (e.g. teach to test; reward teachers based on their students&#x27; scores)</td></tr><tr><td>GamingStrategic and selective collection and use of data in pursuit of individual goals</td><td>- Media proclaiming a new role in &#x27;leading educational revolution&#x27; while pursuing their individual goal of improving revenue streams-Politicians using My School data to argue pro/against education reform</td><td>- Amplified individual optimality of agents as they use selected and decontextualized data strategically to justify their actions/reactions in pursuit of individual goals- Impact on &quot;bounded rationality&quot; of each agent as they use (mis) information selectively- New feedback loops used to exert power or influence over neighboring agents- Adaptation by impacted agents triggering new feedback loops</td><td>- Increased pressure on students, teachers, principals to increase the reported test scores supported by the selective use of data- Teachers &quot;teaching to test&quot; and helping students during tests to achieve performance targets- Discriminatory actions towards &quot;low performing&quot; students taken by some schools (justified by the school performance target)</td></tr><tr><td>Propagation of legitimationLegitimacy of inferred information based on legitimacy of original data</td><td>- Legitimacy of school league tables and new data repositories created by the media are based on legitimate data provided by My School</td><td>- Amplified individual optimality as de-contextualized and recombined data become &quot;legitimate&quot; and as such used to justify actions and reactions- Amplified reinforcing feedback loops, as agents are &#x27;armed&#x27; with correct and legitimate information</td><td>- The &quot;legitimacy&quot; claim used to further influence, even manipulate public opinion about school funding, and actions that reward or punish schools based on the legitimate measures of performance; these actions in turn intensify the existing, and create new, negative consequences for some sections of society</td></tr><tr><td>Auditing by non-expertsNon-experts using open performance data judge the quality of complex expert activities</td><td>- &#x27;Armed with data&#x27; parents, politicians, government administrators and journalists are judging, and even interfering with the education practices that require expert knowledge</td><td>- New positive feedback loops (e.g. those triggered by parents&#x27; analysis and interpretation of school performance) used to exert pressure on neighboring agents (e.g. parents putting pressure on teachers)- Amplified individual optimality of agents (e.g. parents &#x27;armed with objective data&#x27; exerting even more power on other agents (teachers, principles) in pursuit of their individual goals)- Adaptation of targeted agents</td><td>- &#x27;Empowered&#x27; public as everyone legitimately judges &quot;school quality&quot; data- Public pressure (by non-experts) targeting &quot;non-performing schools&quot; and &quot;non-performing teachers&quot; with negative effects on some schools and teachers;</td></tr></table>

<table><tr><td>Please cite this article in press as: Marjanovic, O., Cecez-Kecmanovic, D. Exploring the tension between transparency and datafication effects of open government IS through the lens of complex adaptive systems. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.07.001</td></tr></table>

Table 2 (continued)

<table><tr><td>Datafication patterns</td><td>Example from My School case</td><td>Open government IS as CAS</td><td>Examples of societal consequences</td></tr><tr><td>Amplified performativityData used to amplify impact of measures on what is being measured</td><td>- Gaming response to data by teachers ‘teaching to test’ or principals enrolling students with “good” NAPLAN results lead to improved ‘performance measure’</td><td>- Pressured to achieve performance targets (measured by quantified proxies), agents adapt by establishing new behaviors and practices and achieve these external goals (thus pursuing individual optimality); In turn, these practices perform reality in accordance with the measures</td><td>- What is measured further amplifies and influences public opinion on what matters when it comes to good education thus putting pressure on the agents to change behavior according the measures</td></tr></table>

## Recombination

This datafication pattern refers to the phenomenon whereby new data are created by recombination of de-contextualized data to create brand new meanings. As the original contexts are missing, the resulting combination can be misleading. My School offers numerous example of this pattern. For instance, school ‘‘performance data” are combined with other data sources (real-estate) to offer advice about ‘‘good value for money schools”. This brand new meaning is attached to schools through the combination of previously derived meanings of ‘‘good schools” and ‘‘good-value for money properties”. Such derived information is used for instance by parents to decide where to buy or rent a house/apartment. Apart from consequences for the families, information generated from recombined and de-contextualized data produces increased demand for some highly ranked schools while decreasing demand for others (Finder.com, 2016; PropertyValue, 2016). That information about ‘‘good value for money schools” is developed based on NAPLAN test results is by now completely forgotten. This is an example of misleading information used by individual agents to ‘optimize’ their goals (to enroll their children in the best schools) that in turn affects other agents (disproportional demand for enrolments across schools).

## Using quantified proxies

This datafication pattern refers to simple quantified measures (proxies) introduced in order to measure complex social activities that are typically difficult to quantify (such as learning and teaching performance). Such measures are used to compare performance levels, establish improvement targets (e.g. in percentages), calculate and report achievements, and reward good (or punish low) performers. Thus, ‘‘student learning” performance is ‘‘measured” by the standardized numeracy and literacy test scores. The ‘‘teaching quality” of teachers is measured by the test scores of their students. The quality of schools is measured by their students’ score. These proxies are taken to be objective and valid (especially by people outside of the education context) and used, often inappropriately, for auditing, setting performance targets, funding, and various improvement initiatives.

## <sub></sub> Gaming

This datafication pattern denotes strategic and highly selective collection and use of data in pursuit of individual goals. We observed ‘‘gaming” in the process of data collection by numerous actors seeking better test results. A good example of this aspect is selective enrolment of students based on their prior NAPLAN score, practiced by some school principals. Some teachers also advised selected ‘‘low performing” students not to come to school on a testing day. We also observed ‘‘gaming” related to highly selective use and interpretation of ‘data’ by different interested parties. The examples of this type of gaming include media using league tables (i.e. their own interpretation of a subset of data) to sell newspapers or politicians using their interpretation of data to argue pro/against education reforms.

## Propagation of legitimation

This datafication pattern is observed in relation to various agents claiming legitimacy of the inferred (de-contextualized and re-combined) information on the basis of the legitimacy of the ‘‘original” data provided by My School. Examples include claimed legitimacy of the league tables or predicted real-estate prices because they are based on the legitimate (government) My School data.

## Auditing by non-experts

Oversimplification of performance measures (by quantified proxies) encourages or even amplifies auditing by nonexperts (e.g., by parents, politicians, government administrators, journalists). In the case of My School, non-experts are

Please cite this article in press as: Marianovic. O.. Cecez-Kecmanovic. D. Exploring the tension between transparency and datafication leffects of open government IS through the lens of complex adaptive systems. I. Strateg. Inform. Syst. (2017). http://dx.doi.org/10.1016 j.jsis.2017.07.001

further empowered by accessing the legitimate data (provided by the government) as well as by using simple tools so they can infer their own conclusions from My School. They use the resulting insights as a basis of their ‘expert’ opinion, to put more pressure on teachers and principals.

## Amplified performativity

This pattern describes the performative effect of data whereby the measure (i.e. performance data) impacts and (re)creates what is being measured. In essence, by publishing performance data, what is measured, how and with what results, are all made open to the public. The old adage ‘‘what is measured is what matters”, then creates a gaming response by those being measured (e.g., teachers start teaching to the test; schools take actions to enroll ‘‘good” students). Importantly ‘‘what is measured” also influences public opinion as to what high quality education means in a particular societal context (e.g., high test scores). This in turn triggers additional localized feedback loops that are in essence misdirected towards regulating the symptoms (while increasing gaming behavior), but without any understanding of the underlying systemic issues (i.e. performance data made open).

Table 2 summarizes these datafication patterns of open government IS and their societal consequences and provides examples from My School case.

## 7. Strategic implications of open government IS and their datafication effects

Based on the above analysis and theorizing of the tension between transparency and datafication effects of open government IS by explaining the underlying datafication patterns influencing the tension, we propose several important strategic implications for senior government decision makers in charge of making data open:

## Open government IS cannot be centrally controlled through direct interventions

Any attempt to control open government IS centrally and through direct interventions aimed at the whole system are neither feasible nor effective. Instead, these types of interventions create forms of gaming and resistance that are very likely to result in further datafication effects (often undesirable and negative for some sections of society). As Gall (2012) explains, the belief that complex adaptive systems may be controlled and changed through direct intervention is overly optimistic and is ‘‘a classic example of a Systems-delusion” (p. 163). Therefore, any government top-down interventions, including public policies designed to control the overall open government IS or prescribe its behavior, are destined to fail, due to the unpredictable ways these complex adaptive systems emerge and adapt

## Open government IS cannot be performance-managed towards a predefined future goal

Ultimately, the future of any open government IS is unknowable, due to its far reaching and unpredictable datafication effects and their underlying patterns. Therefore any government strategy that pours more resources into changing the behaviors of agents towards a predefined goal (one goal for the whole system such as transparency) is likely to fail because of the complex adaptive nature of these open government IS.

## Open government IS could be influenced and changed through localized, small-scale experimentation

Even though an open government IS cannot be controlled in a top-down manner. its behavior can be influenced. Previous research offers some interesting ideas and conceptual frameworks about possible ways of influencing and changing CAS. For example, Snowden and Boone (2007) show that a CAS can only be changed through ‘emergent practices,’ that is, local and carefully planned small-scale experiments. Moreover, El Sawy and Majchrzak (2004) provide an example of the so-called OODA (Observe, Orient, Decide, Act) loops as a framework for ‘‘quickening the learning action loops” (Benbya and McKelvey, 2006, p. 23). We suggest a model of ‘emergent practices’ developed from Snowden and Benbya and McKelvery’s work as a possible way of engaging and influencing the complex open government IS such as My School. We envisage this model to involve iterations of small-scale experiments implemented as OODA loops. Drawing from our research findings that highlight characteristics of bounded rationality—as they relate to the ‘‘Observe and Orient” activities—we propose that these activities would need to involve a diverse group of agents, government decision makers, teachers, principals, parents and private citizens, each contributing their localized point of view. Similarly, the ‘‘Decide and Act” activities also need to consider individual optimality of different agents.

Due to the ‘‘bounded rationality” and ‘‘individual optimality” characteristics of individual actors (CAS’ agents), we envisage that each OODA implementation should also involve a boundary-spanner role (e.g. an independent facilitator or ombudsmen). As any CAS cannot be controlled centrally, this role should not be in charge of the whole system. Instead, this system-level role should ensure that individual perspectives are carefully considered and aligned as much as possible. However, given the ‘‘rugged landscape” of the open government IS, it is also important to acknowledge that one universal, optimal-for-all goal is not possible.

A possible way forward towards practical implementation of these small-scale experiments would be to first establish a permanent advisory group led by an independent boundary-spanner role (e.g. the above mentioned ombudsmen) and consisting of a number of representatives of all interested parties. A similar example of a boundary-spanning group already exists in the UK in the form of the newly established Privacy and Consumer Advisory Group (PCAG, 2017). This independent group of academics, government and industry representatives, subject matter experts and citizens, advises the UK government ‘‘on how to provide users with a simple, trusted and secure means of accessing public services” (PCAG, 2017, p. 1). We envisage a similar group advising the Australian government on provision and reuse of My School data. This yet-to-be-established group would be in charge of design and implementation of small-scale experiments, as well as evaluation of their effectiveness. Examples of small-scale experiments might include design and implementation of a public campaign on intended purpose and interpretation of My School data (as opposed to media league tables) or design and implementation of a new type of IS enabling more effective participation in public discourse by all interested parties.

## Guiding principles for localized (autonomous) actions

Rather than prescribing actions it is important to offer guiding principles for localized (autonomous) actions. When considering strategic implications for CAS, Levy (2006) argues that guidelines (rather than prescriptions) are needed to cope with complexity. We envisage that in the case of open government IS, these principles should include ethical and moral use of open data as possible foundations of mutual accountability for open government IS through agents’ own localized actions and their societal consequences (Cecez-Kecmanovic and Marjanovic, 2015).

## 8. Contributions, conclusions, limitations and future research

In this article, we outline a novel approach to researching societal challenges of datafication by applying CAS to investigate the ongoing tension between transparency and datafication effects of open government IS. Following Galliers et al.’s (2015) call for future research on datafication and inspired by Merali’s (2006) and McKelvey et al.’s (2016) proposals for CAS-informed IS research, we provide a new way of researching and theorizing open government IS and their datafication effects. We draw our research insights from an extensive, in depth examination of the My School case, an open government IS in Australia, which makes school performance data public.

Our study offers several theoretical and practical contributions:

(1) Theorizing the ongoing tension between transparency and datafication effects of open government IS through the CAS lens reveals the non-linear nature of this tension and how it arises due to proliferation and reuse of open performance data by numerous users in unpredicted and unexpected ways;

(2) Identification and conceptualization of seven datafication patterns of open government IS reveal further how unintended negative societal effects are produced thus enabling deeper understanding of the tension; grounded in the empirical evidence from the My School case these datafication patterns represent heuristic generalizations (Tsoukas, 2009) that may help us make new distinctions about social consequences of open government IS that make performance data open to public;

(3) Development of a distinct hermeneutic approach to a longitudinal study of open government IS and their societal effects based on CAS as a theoretical lens enables, on the one hand, in-depth insights into the particular example of My School from the Australian context and, on the other, the dynamic processual conceptualization of more general patterns; this is achieved by investigating My School ‘as a case of’ open government IS that allowed conceptual abstraction from while preserving the epistemic significance of the particular;

(4) Identification and discussion of key strategic implications of the theoretical claims about the nature and societa effects of open government IS for senior government decision-makers responsible for making performance data open to public.

Our use of CAS as an innovative approach to study open government IS and conceptualize their strategic implications for government decision makers contributes to Merali et al.’s (2012) future research agenda for Strategic Information Systems (SIS). In particular, we contribute to the priority area of ‘‘The conceptualization of the SIS domain as a complex adaptive system for the co-evolution of physical and social technologies” (Galliers et al., 2012, p. 88). Our research expands the SIS domain beyond organizational boundaries to include open government IS as CAS. Also, the proposed key strategic implications of open government IS further expand the SIS research direction as identified by Gable (2010) to the new domain of open government IS.

Our study has several limitations. First, recognizing the inherent nature of My School as CAS means that our research perspective is inevitably limited due to our own ‘‘bounded rationality”. Being a part of the system we study and embedded within its historical and social context allowed our dialogical encounters with the variety of evidence and events related to or created by different agents (individual students, parents, teachers, schools; government agency ACARA, teachers’ and principals’ associations, education research organizations). Such dialogical encounters and numerous hermeneutic circles enabled us to trace the emergence of My School as a ‘‘whole” over a long period of time (since 2006) and the effects experienced by different agents. In such a way we were able to reflectively offset this limitation to the extent that enabled us to convincingly answer our research questions.

Second, one of the proposed strategic implications include changing/influencing open government IS through localized, small-scale experiments. While in this paper we do not consider design and implementation of these experiments, we believe that this is an interesting research topic worth exploring.

Third, the tension between transparency and datafication effects inevitably creates ethical challenges and dilemmas for the senior government decision makers in charge of making performance data open, the discussion of which is beyond the scope of our paper. However, by showing how My School performs as CAS and how unintended social effects are created through datafication patterns that characterize this type of systems, we provide empirical and theoretical arguments for the decision makers to reconsider the unquestioned goal of transparency and its achievement via open government IS from an ethical perspective. While this is certainly a very serious ethical question for governments, it is also relevant to all other agents of this kind of open government IS. We call for further academic research into the ethicality of transparency and open government IS offering performance data.

Finally, our hermeneutic approach and heuristic generalization from a particular case (My School) ‘as a case of’ a more general phenomenon (open government IS) deserve a reflexive comment. Drawing from the debate on generalizability of research findings from particular cases in the IS literature (Lee, 1989; Walsham, 1995; Lee and Baskerville, 2003; Tsang, 2014) we recognize the significance of the notion of ‘analytic generalization’ variously argued as an epistemological defense of non-positivist case study research. In this paper we adopted a slightly different notion of ‘heuristic generalization’ that provides ‘‘conceptual abstractions from concrete data” and thereby ‘‘refine the distinctions through which we understand general processes” (Tsoukas, 2009, p. 298). Heuristic generalizations are open-ended and preserve the significance of the particular while abstracting to the general.

In summary, our research contributions and the observed limitations open several promising directions for future research in IS, including strategic IS. They include:

(1) Further refinement and potential expansion of the proposed datafication patterns, based on other examples of open government IS;

(2) Investigation and assessment of the proposed strategic implications for conceptualizing and managing open government IS, in collaboration with government decision makers responsible for open data initiatives in different contexts;

(3) Design, implementation and evaluation of a new type of large-scale IS to support public involvement in the proposed quickened OODA loops;

(4) Further investigation of ethical dilemmas faced by senior government decision makers who are confronted by the ongoing tension between transparency and datafication effects;

(5) Further research on CAS applications to other types of open government IS;

(6) Investigation of new research methods suitable for large-scale CAS (beyond open government IS) that are rapidly emerging in the age of big data and causing yet-to-be understood society-wide datafication effects.

Given the growing commitment to opening up performance-related data (such as those from education and healthcare sectors), as well as the complex nature of open government IS, we conclude that the resulting tension between transparency and datafication effects cannot be avoided. Here we see a challenge and an opportunity for IS researchers, educators and practitioners to advance our collective capacity for ‘‘living with” these open systems. We offer three reasons as to why we believe this both possible and desirable. First, because the IS community is well positioned to engage in researching complex datafication effects and contribute to a much-needed understanding of the datafication effects of open-data government IS, as described in our research. In such a way the IS community will be able to provide knowledge and expertise to policymakers and stakeholders and thus, as Stahl (2012) emphasizes, ‘‘fulfil its broader social responsibilities and help achieve what arguably should be its core mission: to improve our individual and collective lives by making the best possible use of available technologies” (p. 209). However, this requires that we: (i) move beyond traditional understandings of and reduc tionist approaches to ‘‘systems”; and (ii) abandon a ‘‘cargo cult” mentality (Lowry et al., 2016) of seeing our collective research ‘‘tradition” as a priori superior even when faced with previously-unknown phenomena such as datafication effects. Second, by considering ideas and approaches from the field of large-scale community organizing such as those discussed by Ford (2007), we envisage opportunities for the development of a new type of large-scale public IS to support public involvement in the quickened OODA loops. Third, we argue that the IS community is well placed to educate both the wider public and their students about various datafication effects of open government IS.

Finally, the wide proliferation and use of data big and small have re-surfaced and amplified the old management adage of ‘‘what is measured is what matters”. Our research on open government IS and their datafication effects invites our collective reflection on what truly matters in education, well before we can decide if, and how it can be measured, let alone shared with the public in the most appropriate and ethical ways. We echo Meadows' (2008, p. 171) words that “Living successfully in a world of systems requires more of us than our ability to calculate. It requires our full humanity — our rationality, our ability to sort out truth from falsehood, our intuition, our compassion, our vision, and our morality”.

![](/api/attachments/SG4XB22N/fulltext/images/7405b3eb529a47206961efdb7c6f969a36eb6c82502930d30c60045314abb220.jpg)

## NAPLAN Natic Literacy and Numeracy

NAPLAN provides benefits from the ground up for students, schools and Australian education systems.

![](/api/attachments/SG4XB22N/fulltext/images/7527972337ab2eb2f2ac268ccbc4b3640813aecbc10ec110a10666b33b912eff.jpg)

You're not alone...

1 MILLION STUDENTS sit the NAPLAN test.

![](/api/attachments/SG4XB22N/fulltext/images/f350c5f43819ff9db7223d0696026f5fcfb5cc75361652fa5b22ed73f0cae64f.jpg)

No pass. No fail. Familiarisation is important. Drilling and excessive practice is unnecessary

![](/api/attachments/SG4XB22N/fulltext/images/e69a290b99d86009b8e59c34dd9557f6cc8942b788b58d232f3d9f30371c312c.jpg)

ISCHOOE

![](/api/attachments/SG4XB22N/fulltext/images/4baffa933bb42c7db393420fe752d63a89824869430ba491c9d2ba1e2dbaafce.jpg)

WHO BENEFITS?

![](/api/attachments/SG4XB22N/fulltext/images/db6fc7a88f40db84c078a7bc9d14eab3ca2048c5a8ce6c0f1774217c28190706.jpg)

![](/api/attachments/SG4XB22N/fulltext/images/f8d58ccc7a2af5d80cfbdd9831c9df9c0c52adb7bf1a43d28d4a816b31bde2e1.jpg)

TESTDOMAINS

![](/api/attachments/SG4XB22N/fulltext/images/63db586f6bb8b252db9af977c099f94a1e81132ed5e573d60fe2fb9c31b84433.jpg)

Students and parents Discuss progress with teachers and compare performance against national peers

WHO BENEFITS?

TEACHERS: Help teachers to challenge higher performers and identify students needing support.

![](/api/attachments/SG4XB22N/fulltext/images/80eaeeb79a545febfa1062d69410a24f165971302367dd229f60e52049e0b35e.jpg)

## AUSTRALIAN EDUCATION SYSTEMS

![](/api/attachments/SG4XB22N/fulltext/images/f2ead4c7e1f8e1635491bfc6132bd2297ddc626e25ff332edf757f937f03a631.jpg)

EQUITY: Afairgoforall Australian students.

五由

KNOWLEDGE:

![](/api/attachments/SG4XB22N/fulltext/images/71c7621af9d40dec8770c1874e62c7f8c59fdded680ed1d573ac6fed19091d05.jpg)

Open corversation abouttheimportant skills ofliteracyand numeracy

NATIONAL STANDARDS:

88888

Comparable data about literacyand numeracystandards

WHO BENEFITS?

School systems and governments: Valuable data to support good teaching and learning, and schoo improvement.

The data and information we gain from NAPLAN drives ongoing improvement at school, state and national levels.

acara AUSTEAHAN CHRRICULUM ASSESSMENT AND REPERTINGTUHORITY

Please cite this article in press as: Marianovic, O. Cecez-Kecmanovic D. Exploring the tension between transparency and datafication leffects of open government IS through the lens of complex adaptive systems. I. Strateg. Inform. Syst. (2017). http://dx.doi.org/10.1016 j.jsis.2017.07.001

## Appendix B

Data sources (total of 430 documents) used in this project, expanded from (authors’ previous reference)

<table><tr><td>Timeline</td><td>Significant events</td><td>Relevant (selected) documents</td></tr><tr><td colspan="3">Initiation of NAPLAN</td></tr><tr><td>July 2006</td><td>The Ministerial Council on Education, Employment, Training and Youth Affairs (MCEETYA) formally endorsed the introduction of national testing in Literacy and Numeracy</td><td>ACARA Media Releases:2008National Curriculum Board Framing Papers Released for Feedback;National Curriculum Consultation Begins Today;</td></tr><tr><td>During 2007</td><td>Development of the NAPLAN (National Assessment Program - Literacy and Numeracy) test</td><td>National Curriculum Journey Begins2009ACARA welcomes inaugural Chief Executive Officer;Key features in national curriculum examined at forums;</td></tr><tr><td>May 2008</td><td>ACARA administered the first test</td><td rowspan="2">ACARA Update Archive: Issue 1, 27 Nov 2009 and Issue 2, 14 Dec. 2009</td></tr><tr><td>May 2009</td><td>ACARA administered the second test</td></tr><tr><td colspan="3">Launch of My School online portal</td></tr><tr><td>Jan 2010</td><td>ACARA makes My School portalAvailable online (with 2008 and 2009NAPLAN results at the level of individual schools)</td><td>ACARA media Releases, 2010:Statement from ACARA ChairNational Consultation on the draft Australian Curriculum March 2010;</td></tr><tr><td>May 2010</td><td>Third NAPLAN test administered, results made available on My School in Sept 2010.</td><td>My School website launch;ACARA Update archive: Issues 3-15 (March - Dec 2010);</td></tr><tr><td colspan="3">First Senate inquiry</td></tr><tr><td>13 May 2010</td><td>The Senate referred the matter of NAPLAN to the Senate Education, Employment and Workplace Relations Reference Committee</td><td rowspan="2">- 268 written submissions to the Senate Inquiry, June 2010;- Interim report: “Effectiveness of the National Assessment Program - Literacy and Numeracy”, Aug. 2011</td></tr><tr><td>25 June 2010</td><td>Public submissions open - 268 submissions received</td></tr><tr><td>27 July 2010</td><td>Interim report prepared</td><td>- Transcript of the public hearing (84 pages) - Friday 29 Oct 2010 Canberra</td></tr><tr><td>29 Oct &amp; 1 Nov 2010</td><td>Public hearing in Canberra</td><td>- Transcript of public hearing (49 pages) - Mon 1 Nov. 2010. Canberra</td></tr><tr><td>24 Nov 2010</td><td>Final report released</td><td rowspan="3">- Final report Nov. 2010;- Australian Government Response to the Senate Education, Employment and Workplace Relations Reference Committee: Report on the Administration and Reporting of NAPLAN Testing, Aug 2011</td></tr><tr><td>May 2011</td><td>Fourth test administered</td></tr><tr><td>Aug 2011</td><td>Australian Government responds</td></tr><tr><td colspan="3">My School post 1st Senate inquiry</td></tr><tr><td>May 2012</td><td>Fifth suite of tests administered</td><td>ACARA media releases, 2013:</td></tr><tr><td>May 2013</td><td>Sixth suite of tests administered</td><td>SCSEEC (from 1 July 2014 known as Education Council)media release - 2013 NAPLAN National Report2013 NAPLAN Summary Report releaseDelay in release of 2013 NAPLAN Student ReportsACARA Update archive for 2012 - Issues 36-58 (Feb - Dec 2010);ACARA Update archive for 2013 - 12 updates (Feb - Dec 2010)</td></tr></table>

(continued on next page)

Appendix B (continued)

<table><tr><td colspan="3">Second Senate inquiry</td></tr><tr><td>15 May 2013</td><td>The Senate referred the matter of NAPLAN to the Senate Education, Employment and Workplace Relations References Committee for inquiry and report.</td><td>-93 written public submissions to the Senate Inquiry June 2013;-Interim report:The effectiveness of the National Assessment Program Literacy and Numeracy (NAPLAN) - 27 June 2013</td></tr><tr><td>7 June 2013</td><td>Public submissions close</td><td rowspan="4">-Transcript of the public hearing (53 pages) - 21 June 2013 Melbourne</td></tr><tr><td>21 June 2014</td><td>Public hearing in Melbourne</td></tr><tr><td>27 June 2013</td><td>Interim report: The effectiveness of the National Assessment Program - Literacy and Numeracy (NAPLAN)</td></tr><tr><td>27 March 2014</td><td>Final report released</td></tr><tr><td>Jun 2014</td><td>Australian Government responds</td><td>-Final report:-Final Report, March 2014;-Australian Government Response to the Senate Education, Employment and Workplace Relations Reference Committee: Report on the Effectiveness of NAPLAN Testing, Jun 2014;</td></tr><tr><td colspan="3">My School post-2nd Senate inquiry</td></tr><tr><td>May 2014</td><td>Seventh suite of tests administered (results made available on My School in Sept 2014)</td><td>ACARA Media releases:-Fair comparisons: My School website released for 2015;-NAPLAN 2015: the last paper-based tests for some</td></tr><tr><td>March 2015</td><td>Plans announced to introduce online testing from 2017</td><td rowspan="3">-National Assessment and Surveys Online Program: tailored test design 2013 study;-NAPLAN summary information released;-NAPLAN tests start tomorrow;-ACARA releases statement to the review of Australian Curriculum;-Release of My School 2014;-ACARA Update archive for 2014- 27 update documents (Feb - Dec 2014);-ACARA Update archive for 2015- 12 update documents (Jan - June 2015)</td></tr><tr><td>22 March 2015</td><td>Australian Government Review of My School announced</td></tr><tr><td>(expected) 2017</td><td>Online testing</td></tr><tr><td colspan="3">Additional documents</td></tr><tr><td>2014</td><td>Independent and Commissioned research reports</td><td>-Research Report: “The experience of Education: The impacts of high stakes testing on school students and their families: A qualitative Study” Whitlam Institute &amp; University of Western Sydney, May 2014 (findings from the interviews with 16 Principals/School Leaders; 29 teachers, 26 parents and 70 students (22 Grade 5, 25 Year 7, 23 Year 9)-Research Report: “The Experience of Education: The impact of high stakes testing on school students and their families: An Educator’s Perspective”, Whitlam Institute Australia &amp; University of Western Sydney, June 2012 (findings from online survey of 8353 participants)-Australian Primary Principal Association: My School-NAPLAN Discussion Paper, 8th Sept. 2014</td></tr><tr><td>2010-present(ongoing)</td><td>Media publications</td><td>Over 200 media documents (editorials, articles, video clips and social media posts)</td></tr><tr><td>2014/2015/2016</td><td>My School reviews (commissioned by ACARA and Australian Government</td><td>-Final report of the Review of My School Web Site (2014)-ACARA- Perspectives on the My School website (2015)-School Daze: What my School really says about our schools (2016)</td></tr></table>

Guba, E.G., Lincoln, Y.S., 2005. Paradigmatic controversies, contradictions, and emerging confluences. In: Denzin, N.K., Lincoln, Y.S. (Eds.), National Testing in Guba, E.G., Lincoln, Y.S., 2005. Paradigmatic controversies, contradictions, and emerging confluences. In: Denzin, N.K., Lincoln, Y.S. (Eds.), National Testing in

## References

ACARA, 2010. Australian Curriculum Assessment and Reporting Authority: My School <http://www.myschool.edu.au>, (accessed 27 Nov 2016).

ACARA, 2016. CEO Report: My School, May 2016 <http://www.myschool.com> (accessed 27 Nov 2016).

Allen, P.M., Varga, L., 2006. A co-evolutionary complex systems perspective on information systems. J. Inf. Technol. Rev. 21 (4), 229–238.

Anderson, B., 2010. Struggling students ‘‘exempt” from test. ABC News. 11 May 2010, <http://www.abc.net.au/news/2010-05-11/> (accessed 28 Nov 2016).

APPA, 2014. Australian Primary Principal Association: My School – NAPLAN Discussion Paper, 8th September 2014.

ASPA, Australian Secondary Principals’ Association, 2010. My School Survey Results. J.K. See Consulting.

Attard, J., Orlandi, F., Scerri, S., Auer, S., 2015. A systemic review of open government data initiatives. Gov. Inf. Quart. 32 (4), 399–481.

Australian Government, 2011. Australian Government Response to the Senate Education, Employment and Workplace Relations Reference Committee: Report on the Administration and Reporting of NAPLAN Testing, Aug 2011.

Baack, S., 2015. Datafication and empowerment: how the open data movement re-articulates notions of democracy, participation, and journalism. Big Data Soc. 2 (2), 1–11.

Bannister, F., Connolly, R., 2011. The trouble with transparency: a critical review of openness in e-government. Policy Internet 3 (1), 1–30.

Barry, E., 2011. Geelong east primary urged parents to keep boy from NAPLAN tests. Herald Sun, 4 May 2011.

Benbya, H., McKelvey, B., 2006. Towards a complexity theory of information systems development. Inf. Technol. People 19 (1), 12–34.

Bevan, G., Hood, C., 2006. What’s measured is what matters: targets and gaming in health care in England. Public Admin. 84 (3), 517–538

Birchall, C., 2014. Radical transparency? Cult. Stud. – Crit. Methodol. 14 (1), 77–88.

Bonnor, C., Shepherd, B., 2016. School daze: what My School really says about our schools. <http://saveourschools.com.au> (accessed 27 Nov 2016).

Borzacchiello, M.T.B., Craglia, M., 2012. The impact on innovation of open access to spatial environmental information: a research strategy. Int. J. Technol. Manage. 60 (1–2), 114–129.

Breton, A., Galeoitti, G., Salmon, P., Winrobe, R., 2007. The Economics of Transparency in Politics. Ashgate Press, Aldershot, UK.

Buckley, W., 2013. Society as a complex adaptive system. In: McKelvey, B., Bragin, J. (Eds.), Complexity – Critical Concepts. Routledge, New York, USA.

Canberra Times Editorial, 2010. A little scrutiny goes a long way. Canberra Times, 10 May 2010.

Cecez-Kecmanovic, D., Marjanovic, O., 2015. IS serving the community: The pragmatic, the ethical and the moral questions. Proceedings of the 36th International Conference on Information Systems (ICIS 2015) Fort Worth, TX, USA.

Choi, T.Y., Dooley, K.J., Rungtusanatham, M., 2001. Supply networks and complex adaptive systems: control versus emergence. J. Oper. Manage. 19 (3), 351– 366.

Cilliers, P., 2004. A framework for understanding complex systems. In: Adriani, P., Passiante, G. (Eds.), Complexity Theory and the Management of Networks. Imperial College Press, London, UK, pp. 23–27.

Cilliers, P., 2013. Approaching complexity. In: McKelvey, B., Bragin, J. (Eds.), Complexity – Critical Concepts. Routledge, New York, USA.

Cook, G., 2014. Review of My School Web Site. Australian Department of Education <https://docs.education.gov.au/system/files/doc/other/ reviewofmyschoolwebsite.pdf> (accessed 26 Nov 2016).

Crotty, M., 1998. The Foundations of Social Research – Meaning and Perspective in the Research Process. Allen & Unwin, London, UK.

Davies, T.. Perini, F.. Alonso, I.M., 2013. Researching the Emerging Impacts of Open Data: ODDC Conceptual Framework, World Wide Web Foundation International Development Research Centre <www.opendataresearch.org/sites/default/files/posts/Researching%20the%20emerging%20impacts%20of% 20open%20data.pdf> (accessed 29 Nov 2016).

Earl, L.M., Katz, S., 2006. Leading Schools in a Data-rich World: Harnessing Data for School Improvement. Corwin Press, Thousand Oaks, CA, USA.

El Sawy, O., Majchrzak, A., 2004. Critical issues in research on real-time knowledge management in enterprises. J. Knowl. Manage. 8 (4), 21–37.

Finder.com. 2016. The best public schools with the cheapest cost of living – don't spend millions of dollars to send your kinds to à top public school. <https://www.finder.com.au/best-public-schools-with-the-cheapest-cost-of-living> (accessed 29 Noy 2016).

Ford, J.K., 2007. Building capability throughout a change effort: leading the transformation of a police agency to community policing. Am. J. Community Psychol. 39 (3–4), 321–334.

Gable, G., 2010. Strategic information systems research: an archival analysis. J. Strat. Inf. Syst. 19 (1), 3–6.

Gadamer, H.-G., 1960. Truth and Method. Continuum, New York, USA.

Gadamer, H.-G., 1976. The Historicity of understanding. In: Connerton, P. (Ed.), Critical Sociology. Selected Readings, Penguin Books, Harmondsworth.

Gall, J., 2012. The Systems Bible: The Beginner’s Guide to Systems Large and Small. General Systematics Press, New York, USA

Galliers, R., Newell, S., Shanks, G., Topi, H., 2015. Call for papers for the special issue: the challenges and opportunities of ‘datafication’: strategic impacts of 'big' (and 'small') and real-time data – for society and for organizational decision makers. I Strat, Inf, Syst, 24 (2) II-III

Galliers, R., Jarvenpaa, S.L., Chan, Y.E., Lyytinen, K., 2012. Editorial: strategic information systems: reflections and prospectives. J. Strat. Inf. Syst. 21 (2), 85– 90.

Gillard. I. 2010, My School web site for parents: live dailytelegraph com au blog with Julia Gillard, The Daily Telegraph, ≤http://www dailytelegraph.com au/news/opinion/my-school-website-for-parents-live-dailytelegraphcomau-blog-with-julia-gillard/story-e6frezz0-1225823697826> (accessed 27 Nov 2016).

Gitelman, L., 2013. Raw Data is an Oxymoron. MIT Press, Cambridge, MA, USA.

Golden-Biddle, K., Locke, K., 1993. Appealing work: investigation of how ethnographic texts convince. Organ. Sci. 4 (4), 595–616

Gorur, R., 2016. Local experiences, global similarities: teacher perceptions of the impacts of national testing. In: Lingard, B., Thompson, G., Seller, S. (Eds.), National Testing in Schools – An Australian Assessment. Local/Global Issues in Education. Routledge, New York, USA, pp. 30–44.

Green, M., 2015. Since when has NAPLAN been a house price guide? The Sydney Morning Herald, 3 June 2015. 1–2.

Schools – An Australian Assessment. Local/Global Issues in Education. third ed. The Sage Handbook of Qualitative Research, Sage, Thousand Oaks, pp. 191-215.

Gurstein, M.B., 2011. Open data: empowering the empowered or effective data use for everyone? First Monday 16 (2), 1–2. <http://firstmonday.org/ojs/ index.php/fm/article/view/3316/2764> (accessed 30 Nov 2016).

Heidegger, M., 1962. Being and Time (Macquarie, J., Robinson, E. trans). Harper & Row, New York, USA.

Henriksen, H.Z., Andersen, K.N., Medaglia, R., 2011. Public sector IS maturity models: legal pluralism invades public schools. Electronic Government. Lecture Notes in Computer Science, vol. 6846, Springer, Berlin Heidelberg, Germany, pp. 100–111.

Herald Sun Editorial, 2010. Rank schools to get results. Herald Sun, 28 January 2010, 30.

Jacob, B.A., Levitt. S.D., 2003, Rotten apples: an investigation of the prevalence and predictors of teacher cheating, O. I. Econ, 118 (3), 843–877

Jacucci, E., Hanseth, O., Lyytinen, K., 2006. Introduction: taking complexity seriously in IS research. Inf. Technol. People 19 (1), 5–11.

Janssen, K., 2011. The influence of the PSI directive on open government data: an overview of recent developments. Gov. Inf. Quart. 28 (4), 446–456

Janssen, M, Charalabidis. Y., Zuiderwiik, A., 2012, Benefits, adoption barriers and myths of open data and open government, Inf, Syst, Manage, 29 (4), 258– 268.

Jeacle, I., Carter, C., 2011. In TripAdvisor we trust: ranking, calculative regimes and abstract systems. Acc. Organ. Soc. 36 (4–5), 293–309

Knight, S., 2011. Considering complexity theory in understanding information management in health systems. J. Inf. Technol. Rev. 2 (4), 172–182

Lam, M., 2010. My School launch leads to parent frenzy. News.Com. Australia. 31 January 2010. <http://www.news.com.au/national/my-school-launchleads-to-parent-freny/story-e6frfkw9-1225825079749> (accessed 29 Noy 2016).

Lee, A.S., 1989. A scientific methodology for MIS case studies. MIS Quart. 13 (1), 33–35.

Lee, A.S., Baskerville, R.L., 2003. Generalizing generalizability in Management Information Systems. ISR 14 (3), 221–243.

Complexity and Organization: Readings and Conversations. Routledge, London, UK.

S. (Eds.), National Testing in Schools – An Australian Assessment, Local/Global Issues in Education. Routledge, New York, USA, pp. 181–199 S. (Eds.). National Testing in Schools – An Australian Assessment, Local/Global Issues in Education, Routledge, New York, USA pp, 181-199

Levy, D., 2006. Chaos theory and strategy: theory, application, and managerial implications. In: MacIntosch, MacLean, Stacey, Griffin (Eds.), Complexity and Organization: Readings and Conversations. Routledge, New York, USA.

Lingard, B., Thompson, G., Seller, S., 2016. National testing from an Australian perspective. In: Lingard, B., Thompson, G., Seller, S. (Eds.), National Testing in Schools – An Australian Assessment, Local/Global Issues in Education. Routledge, New York, USA, pp. 1–18.

Loebbecke, C., Picot, A., 2015. Reflection on societal and business model transformation arising from digitization and big data analytics: a research agenda. J. Strat. Inf. Syst. 24 (3), 149–157.

Lourenco, R.P., 2013. Data disclosure and transparency for accountability: a strategy and case analysis. Inf. Polity 18 (3), 243–260.

Lowry, P.B., D’Arcy, J., Hammer, B., Moody, G.D., 2016. ‘‘Cargo Cult” science in traditional organization and information systems survey research: a case for using non-traditional methods of data collection, including Mechanical Turk and online panels. J. Strat. Inf. Syst. 25 (3), 232–240.

Lycett, M., 2013. Editorial: ‘Datafication’: making sense of (big) data in a complex world. Eur. J. Inf. Syst. 22 (4), 381–386

Madden, L.T., Duchon, D., Madden, T.M., Plowman, D.A., 2012. Emergent organizational capacity for compassion. Acad. Manag. Rev. 37 (4), 689–708

Manyika, J., Chui, M., Groves, D., Farrell, S., et al, 2013. Open data: unlocking innovation and performance with liquid information. McKinsey Global Institute,

pp. 1–116 <http://www.mckinsey.com/business-functions/digital-mckinsey/our-insights/open-data-unlocking-innovation-and-performance-withliquid-information> (accessed 31 Dec 2016).

Markus, L., 2015. New games, new rules, new scoreboards: the potential consequences of big data. J. Inf. Technol. 30 (1), 58–59.

Marshall, M.P., Shekelle, P., Brook, R., Leatherman, S., 2000. Dying to Know: Public Release of Information about Quality of Care. The Nuffield Trust, London, UK.

Martin, C., 2014. Barriers to the open government data agenda: taking a multi-level perspective. Policy Internet 6 (3), 217–240.

Mayer-Schonberger, V., Cukier, K., 2013. Big Data: A Revolution That Will Transform How We Live, Work and Think. John Murray Publishers, London, UK.

McKelvey, B., Tanriverdi, H., Yoo, Y., 2016. Call for papers management information systems quarterly special issue: complexity and information systems

research in the emerging digital world. <http://www.misq.org/skin/frontend/default/misq/pdf/CurrentCalls/MISQ\_CALL\_EmergingDigitalWorld.pdf> (accessed 1 June 2016).

Meadows, D.H., 2008. Thinking in Systems – A Primer. In: Wright, D. (Ed.). Chelsea Green Publishing Company, White River Junction, USA.

Meijer, A., de Hoog, J., van Twist, M., van der Steen, M., Scherpeniss, J., 2014. Understanding the dynamics of open data: from sweeping statements to

Merali, Ý, Papadopoulos, T., Nadkarni, T., 2012, Information systems strategy: past, present, future? I. Strat, Inf, Syst, 21 (2), 125–153

Merali, Y., 2006. Complexity and information systems: the emergent domain. J. Inf. Technol. Rev. 21 (4), 216–228.

Merali, Y., McKelvey, B., 2006, Using complexity science to effect a paradigm shift in information systems for the 21st century, I. Inf, Technol. Rey, 21 (4) 211–215.

Michener, G., Bersch, K., 2013. Identifying transparency. Inf. Polity 18 (3), 233–242.

Miller, P., Voon, D., 2012. Government versus non-government schools: a nation-wide assessment using Australian NAPLAN data. Aust. Econ. Pap. 51 (3), 147–166.

Mocker, N., 2013. Reporting on the ‘Education Revolution’ My School.edu.au in the Print Media. Discourse: Stud. Cult. Polit. Educ. 34 (1), 1–16.

Mocker, N., 2016. NAPLAN and the problem frame: exploring representations of NAPLAN in the print media, 2010–2013. In: Lingard, B., Thompson, G., Seller,

My School, My School portal, 2016. <www.myschool.gov> (accessed 29 Nov 2016).

Newell, S., Mirabelli, M., 2015. Strategic opportunities (and challenges) of algorithmic decision-making: a call for action on the long-term societal effects of ‘datafication”. J. Strat. Inf. Syst. 24 (1), 3–14.

NSW, P.P.A., 2010. NSW PPA Survey – ‘My School’ Website. NSW Primary Principles Association, 1–5 <http://www.nswppa.org.au> (accessed 27 July 2016).

PCAG, 2017. Privacy and Consumer Advisory Group. The UK Government <https://www.gov.uk/government/groups/privacy-and-consumer-advisorygroup> (accessed 14 March 2017).

PropertyValue, 2016. Upgrade to premium to view NAPLAN and ICSEA scores, fees and funding <http://www.propertyvalue.com.au>, (accessed 26 July 2016).

Roberts-Holmes, G., 2015. The ‘datafication’ of early years pedagogy: ‘‘If teaching is good, the data should be good and if there’s bad teaching, there is bad data”. J. Educ. Policy 30 (3), 302–315.

Simon, H.A., 1955. A behavioural model of rational choice. Quart. J. Econ. 69 (1), 99–118.

Simon H.A. 1979. Rational decision-making in business organizations, Am. Econ, Rey, 69 (4) 493–513.

Smith, P., 1995. On unintended consequences of publishing performance data in the public sector. Int. J. Public Admin. 18 (2&3), 277–310.

Snowden, D.J., Boone, M., 2007. A leader’s framework for decision making. Harvard Bus. Rev. 85 (11), 69–76.

Stacey, R.D., 2003. Strategic Management and Organizational Dynamics: The Challenge of Complexity. Prentice Hall, Harlow, UK.

Stacey, R.D., 2006. The science of complexity: an alternative perspective for strategic change processes. In: MacIntosch, MacLean, Stacey, Griffin (Eds.),

Stacey, R.D., Griffin, D., Shaw, P., 2000. Complexity and Management – Fad or Radical Challenge to Systems Thinking? Routledge, New York, USA.

Stahl, B.C., 2012. Editorial: responsible research and innovation in information systems. Eur. J. Inf. Syst. 21 (3), 207–211.

Sydney Morning Herald Editorial, Why we are publishing a league table, Sydney Morning Herald, 14 January 2010a.

Sydney Morning Herald Editorial, Testing time for teachers, Sydney Morning Herald, 12 January 2010b.

Tadjeddine, K., Lundqvist, M., 2016. Policy in the Data Age: Data Enablement for the Common Good. The McKinsey Global Institute, pp. 1–12 <http://www. mckinsey.com/business-functions/digital-mckinsey> (accessed 30 Dec 2016).

The Advertiser Editorial, Students will benefit from school scrutiny, The Advertise, 18 December 2009.

The Australian Editorial, Accountability is essential to improve all our schools, The Australian, 15 May 2010.

The Australian Senate, 2010. Final report: Education, Employment and Workplace Relations References Committee: Administration and reporting of NAPLAN testing, November 2010.

The Australian Senate, 2014. Final report: The Senate: Education and Employment Reference Committee: Effectiveness of the National Assessment Program – Literacy and Numeracy, March 2014.

Thomson, G., Cook, I., 2013. Manipulating the data: teaching and NAPLAN in the control society. Discourse: Stud. Cult. Polit. Educ. 35 (1), 129–142.

Thompson, G., Sellar, G., Lingard, B., 2016. The life of data: evolving national testing. In: Lingard, B., Thompson, G., Lingard, B. (Eds.), National Testing in Schools – An Australian Assessment, Local/Global Issues in Education, Routledge, New York, USA, pp. 212–231.

Tsang, E.W.K., 2014. Case studies and generalization in information systems research: a critical realist perspective. J. Strat. Inf. Syst. 23 (2), 174–186

Tsoukas, H., 2009. Craving for generality and small-N studies: a Wittgensteinian approach towards the epistemology of the particular in organization and management studies. In: Bryman, A., Buchanan, D. (Eds.), The Sage Handbook of Organizational Research Methods. Sage, London, UK, pp. 285–301.

UK GOV Cabinet Office, 2013. G8 Open Data Charter <https://www.gov.uk/government/publications/open-data-charter/g8-open-data-charter.pdf>, (accessed 27 Nov 2016).

Vidgen, R., Wang, X., 2009. A coevolving systems approach to the organization of agile software development. Inf. Syst. Res. 20 (3), 355–376.

Walsham, G., 1995. Interpretive case studies in IS research: nature and method. Eur. J. Inf. Syst. 4 (2), 74–81.

Wiltshire, K., 2016. Rigid curriculum fails students with special needs. The Australian, 1–2. 18 March 2016.

Weick, K., 2007. The generative properties of richness. Acad. Manag. J. 50, 14–19.

Wyn, J., Turnbull, M., Grimshaw, L., 2014. The Experience of Education: The Impacts of High Stakes Testing on School Students and Their Families: A Qualitative Study. The Whitlam Institute, University of W. Sydney, Sydney, Australia.

Ziino, R., Matheson, P., 2015. ACARA. Perspectives on the My School website, ACARA’s Commissioned Report by Colemar Brunton. <http:// www.colmarbrunton.com.au> (accessed 27 Nov 2016).

Zuboff, S., 2015. Big other: surveillance capitalism and the prospects of an information civilization. J. Inf. Technol. Rev. 30 (1), 75–89

Zuiderwijk, A., Janssen, M., 2014. Open data policies, their implementation and impact: a framework for comparison. Gov. Inf. Quart. 31 (1), 17–29.
