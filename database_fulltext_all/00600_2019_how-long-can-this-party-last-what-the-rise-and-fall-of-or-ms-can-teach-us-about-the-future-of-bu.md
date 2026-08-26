---
otero_id: 600
otero_key: "W3NJBVSR"
title: "How long can this party last? What the rise and fall of OR/MS can teach us about the future of business analytics"
authors: "Robert F. Otondo"
year: "2019"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2019.1598609"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# How long can this party last? What the rise and fall of OR/MS can teach us about the future of business analytics

Robert F. Otondo

To cite this article: Robert F. Otondo (2019): How long can this party last? What the rise and fall of OR/MS can teach us about the future of business analytics, European Journal of Information Systems, DOI: 10.1080/0960085X.2019.1598609

To link to this article: https://doi.org/10.1080/0960085X.2019.1598609

![](/api/attachments/W3NJBVSR/fulltext/images/6aedb459bb3b50fc0017c7e698552697d55b0477852e3b0905c9c10ac3943472.jpg)

Published online: 25 Apr 2019.

![](/api/attachments/W3NJBVSR/fulltext/images/75edd3a4fb79196f09ada836540fc0b2ec0d349e67e8f144d3dece4bb2672e3d.jpg)

Submit your article to this journal

![](/api/attachments/W3NJBVSR/fulltext/images/5aa6e344a79ca1258e4e0578e79b0d44a135fea9469d8905e03f214f62dd0702.jpg)

Article views: 75

![](/api/attachments/W3NJBVSR/fulltext/images/773b749f45d672bdf15d1e6eaff1ff38037de3a405a5a839280af837cc9e9993.jpg)

View Crossmark data CrossMark

Check for updates

# How long can this party last? What the rise and fall of OR/MS can teach us about the future of business analytics

Robert F. Otondo

Department of Management & Information Systems, College of Business, Mississippi State University, Mississippi State, MS, USA

## ABSTRACT

Business analytics (BA) is an important organisational activity and research discipline. However, history has shown that information systems (IS)-related disciplines with promising futures do not always <sup>fl</sup>ourish as expected. The troubled history of one such discipline (i.e., operations research/management science, or OR/MS) serves as a cautionary tale for the BA community because it warns of the dangers of an unquestioning faith in the power of mathematical modelling and analysis. This cautionary tale is especially alarming given the methodological similarities between BA and OR/MS, as well as the sizeable investments organisations have made in their BA capabilities. It is, therefore, appropriate and prudent to ask if a similar fate could befall BA and how such a fate can be avoided. Those questions are addressed in this article by extracting “lessons learned” from the OR/MS literature and applying them to BA. The lessons highlight opportunities and challenges to BA which are then framed within a widely cited research agenda. Theoretical propositions are forwarded to encourage research that can help promote the future of BA – both as an organisational practice and research stream – through a wider, broad-based, and balanced critical discourse among scholars and practitioners.

ARTICLE HISTORY Received 24 February 2017 Revised 13 January 2019 Accepted 15 January 2019

ACCEPTING EDITOR Frantz Rowe

ASSOCIATE EDITOR Paul Tallon

KEYWORDS Analytics; operations research/management science; management decision making; human resource management; organisational structure; strategy formulation

## 1. Introduction

Imagine a discipline in which “data availability. . .is now a driving force”. Its procedures – which can be applied to business units such as “production, <sup>fi</sup>nance, personnel, or marketing” – have been considered to be “special bene-<sup>fi</sup>ciaries of [the] explosion in computing, which allows the results of many years of method development to be turned into easily used tools of analysis”. Because of this computing explosion, the discipline bene<sup>fi</sup>ts from “many nice [software] packages [that] have become available for data visualization, decision analysis, . . .forecasting, . . .and data analysis/statistics”. Its “analytical approach [can] turn data into information and information into the knowledge and insights required for improved decision making”.

The discipline attracts interest from top management because of:

(1) the ever-increasing size and complexity of the business situation; (2) the need for faster response times; (3) the felt need to utilize fully the organization's computer facilities; and (4) the more complete and rapid exchange of information about new techniques, particularly about what competitors are doing, and (5) the need to answer. . .the more sophisticated questions that are being asked of top management about their operations.

Moreover, the discipline’s importance is often justi-<sup>fi</sup>ed because of tumultuous external environments:

Today, the increasing complexity of the world’s economic order, the importance and availability of global computer/communication networks, the emerging stress on technologically based manufacturing systems, and other factors have placed increased emphasis on the need to obtain detailed numerical solutions to very large decision problems.

The above quotations all refer to business analytics (BA), right? Not quite. In fact, all were made decades ago about the <sup>fi</sup>elds of operations research and management science (i.e., Committee on the Next Decade in Operations Research [CONDOR], 1988, p. 620; Eilon, 1980, p. 25; Harris, 1992, p. 1031; Geo<sup>f</sup>rion, 1992, p. 430, 1992, p. 435; Radnor & Neal, 1973, p. 445; Harris, 1992, p. 1031; respectively).

Despite these glowing remarks, operations research and management science (OR/MS) su<sup>f</sup>ered serious declines from the 1970s to the early 1990s. This fall from grace has been un<sup>fl</sup>inchingly scrutinised in the OR/MS literature. A consistent theme in those soulsearching e<sup>f</sup>orts involves the consequences of ignoring social and organisational factors (e.g., Ormerod, 1996; Tomlinson & Kiss, 1984).

The similarities between OR/MS and BA (e.g., Beyer, 2015; Holsapple, Lee-Post, & Pakath, 2014; Liberatore & Luo, 2010, 2011) suggest that BA might su<sup>f</sup>er a similar fate. Indeed, there is evidence that OR/MS’s past problems are beginning to surface in BA and related disciplines such as business intelligence (e.g., Tambo, Gabel, Olsen, & Bækgård, 2012) and “Big Data” (e.g., Richey,

Morgan, Lindsey-Hall, & Adams, 2016). While it is enticing to use those similarities to predict BA’s future demise, this article takes a more optimistic and proactive approach by leveraging lessons learned from OR/MS’s self-examination to guide future information systems (IS) research in ways that could avoid a similar fate for BA. Despite the many stumbles and missteps that have characterised the OR/MS <sup>fi</sup>eld, the <sup>fi</sup>eld continues to produce quality research. Top-tier journals – including this journal – continue to publish research in OR/MS just as practitioner journals continue to tap academics for insights on innovations in the <sup>fi</sup>eld. Equally, there continues to be demand for OR/MS faculty to teach general and specialised courses in undergraduate and graduate degree programmes. Doctoral programmes are also active in recruiting candidates to study OR/MS. One might also consider the 30,000 members of the 52 national societies that make up the International Federation of Operational Research Societies (IFORS, 2018) as evidence that OR/MS has endured, even if in a very di<sup>f</sup>erent form. OR/MS’s resurrection means that a comparison of OR/MS and BA presents a learning opportunity for BA research and practice to avoid similar missteps.

The article is organised as follows: First, major issues relating to the fall of OR/MS practice will be identi<sup>fi</sup>ed. Second, these major issues comprising decentralisation of OR/MS personnel, decreased availability of OR/MS practitioners, persisting management apathy towards OR/MS, and inadequate progress in using OR/MS insights to guide strategy are examined in turn. In each case, I <sup>fi</sup>rst o<sup>f</sup>er evidence to support the existence of the issue; second, I discuss how each issue informs the future of BA research; and third, I discuss how lessons and insights learned from the OR/MS literature can be used to generate theoretical propositions that will guide the future of BA research.

Theoretical propositions will be framed within a well-received research agenda. Several research agendas are available, but Sharma et al.’s (2014) agenda will be used for two reasons. First, it is one of the most widely cited BA research agendas in the IS domain. Second, many articles citing Sharma et al. (2014) leverage its arguments concerning the interplay between managerial decision-making on the one hand, and value creation from BA use on the other (e.g., Hazen, Skipper, Boone, & Hill, 2016; Saldanha, Mithas, & Krishnan, 2017). Those arguments have been applied to issues such as process improvement (e.g., Abbasi, Sarker, & Chiang, 2016), pricing and <sup>fi</sup>rm performance (e.g., Akter & Wamba, 2016), and strategic bene<sup>fi</sup>ts (e.g., Fosso Wamba, Akter, & De Bourmont, 2018; Müller, Junglas, Vom Brocke, & Debortoli, 2016), all of which are found in the OR/MS literature.

It is hoped that the propositions and historical analysis presented in this article will not only provide practical insights into managerial decision-making, problem-solving, strategy guidance, and organisational practice, but will also enhance the longevity and standing of BA research. The article will conclude with a discussion, limitations of the study, and suggestions for future research. For the purposes of this article, the acronym “BA” will refer to BA and related disciplines such as business intelligence and “Big Data”.

## 2. The rise and fall of OR/MS: a warning for business analytics?

A brief history of the rise of OR/MS in the 1940s to its fall in the 1980s and early 1990s is provided in Appendix A. This history is useful for uncovering problems and opportunities regarding OR/MS’s downturn that relate to BA. For example, in the 1940s and 1950s, a number of case studies (e.g., Brown, Hulswit, & Kettelle, 1956; Galer, 1959; Kay & Duckworth, 1957; Waid, Clark, & Acko<sup>f</sup>, 1956) demonstrated the value of OR/MS techniques in improving organisational e<sup>f</sup>ectiveness and e<sup>fi</sup>- ciency. As time went on, however, OR/MS went astray and lost its relevance to managerial problems. Several studies identi<sup>fi</sup>ed underlying reasons for OR/MS’s waning in<sup>fl</sup>uence. These studies include the Management Science Roundtable’s report (MSR, 1986) to The Institute for Management Sciences (TIMS) Council, Collcutt’s (1965) report to The British Iron and Steel Research Association (BISRA), and Rosenhead & Mitchell’s (1986) “Report of the Commission on the Future Practice of Operational Research” (CFPOR Report) to the Operational Research Society. A summary of the problems and opportunities identi<sup>fi</sup>ed in these reports is listed in Table 1.

Geo<sup>f</sup>rion (1992) reviewed that literature and highlighted the more important problems then facing OR/ MS. Four of them are beginning to surface in BA and will, therefore, be addressed in this article: (1) decentralisation of OR/MS personnel, (2) problematic recruitment and retention of OR/MS personnel, (3) management apathy towards OR/MS, and (4) inadequate progress in guiding organisational strategy. These problems can also be seen as trajectories resulting from OR/MS’s declining relevance to solving organisational problems and help explain why organisations and managers shed many of their OR/MS assets.

A number of articles have described these four problems in BA. Decentralisation issues have been reported in Deloitte (2013), Davenport (2014a), and Harris, Craig, and Egan (2010b); recruitment and retention issues in Manyika et al. (2011), McAfee and Brynjolfsson (2012), and Richey et al. (2016); management apathy in Ransbotham, Kiron, and Kirk Prentice (2016), McAfee and Brynjolfsson (2012), and Olavsrud (2016); and poor strategy guidance in Ransbotham et al. (2016) and Richey et al. (2016). These four problems also align with Sharma et al.’s (2014) interest in the interplay between value creation from BA use and managerial decision-making.

Table 1. Problems and opportunities identi<sup>fi</sup>ed in OR/MS Research.

<table><tr><td>Problems</td><td>MSR (1986)a</td><td>BISRA (1986)b</td><td>CFPOR (1986)c</td></tr><tr><td>“Survival of the profession”</td><td>6.17</td><td></td><td></td></tr><tr><td>“Inadequate training of practitioners”</td><td>5.77</td><td></td><td></td></tr><tr><td>“Lack of recognition by sr. managers”</td><td>5.10</td><td></td><td></td></tr><tr><td>“Slow progress on strategic problems”</td><td>5.07</td><td></td><td></td></tr><tr><td>“Stagnation of [The Institute for Management Science (TIMS)] membership rolls”</td><td>4.77</td><td></td><td></td></tr><tr><td>“Technology moving too fast”</td><td>4.67</td><td></td><td></td></tr><tr><td>“Mass marketed MS/OR software”</td><td>4.55</td><td></td><td></td></tr><tr><td>Inadequate co-operation between management and the OR team</td><td></td><td>p. 92</td><td></td></tr><tr><td>“[S]ignificant portion” of “failed” projects due to company politics</td><td></td><td>p. 93</td><td></td></tr><tr><td>“[W]orking in novel situations”</td><td></td><td></td><td>p. 853</td></tr><tr><td>“[O]opportunities were sometimes unidentified until it was too late to contribute”</td><td></td><td></td><td>p. 853</td></tr><tr><td>“[P]ractitioners in small groups or new groups”</td><td></td><td></td><td>p. 854</td></tr><tr><td>“[P]roblems of O.R. managers” (i.e., recruitment, retention, promotion to general management)</td><td></td><td></td><td>pp. 854–855</td></tr><tr><td>Difficulties in “commending the use of O.R. on the [identified] issue to the relevant client”</td><td></td><td></td><td>p. 854</td></tr><tr><td>Clients’ image of O.R. and its role and value was “unduly narrow” (Rosenhead &amp; Mitchell, 1986)</td><td></td><td>pp. 92, 94</td><td>p. 854</td></tr><tr><td colspan="4">Opportunities</td></tr><tr><td>“Ride the desktop computing wave”</td><td>8.70</td><td></td><td></td></tr><tr><td>“Explore new application domains”</td><td>7.81</td><td></td><td></td></tr><tr><td>“More aggressive TIMS &amp; [Operations Research Society of America (ORSA)] leadership”</td><td>7.63</td><td></td><td></td></tr><tr><td>“Crossfertilize with AI”</td><td>7.26</td><td></td><td></td></tr><tr><td>“Use more modern MS/OR techniques”</td><td>4.78</td><td></td><td></td></tr></table>

<sup>a</sup>Management Science Roundtable (MSR). (1986). Problems and Opportunities Facing MS/OR: A Report Prepared for TIMS Council (28 March), p. 1.  
Numbers are “criticality” scores based on a “scale of 1 to 10 according to the weighted average ranking score wherein ‘Not Signi<sup>fi</sup>cant’ counts 1,  
‘Signi<sup>fi</sup>cant’ counts 4, ‘Serious’ counts 7, and ‘Critical’ counts 10” (p. ii). Copyright 1986 by INFORMS. Reprinted with permission.  
<sup>b</sup>“Report to the British Iron and Steel Research Association” (Collcutt, 1965).  
<sup>c</sup>“Report of the Commission on the Future Practice of Operational Research” (Rosenhead & Mitchell, 1986; Chapter 5).

They also align speci<sup>fi</sup>cally with a number of Sharma et al.’s (2014) research questions (Appendix B, Table B-1). BA practitioner decentralisation, recruitment, and retention align with their research question on the in<sup>fl</sup>uence of organisational structures on the generation of insights. Research in this area may help explain the extent to which decentralisation and recruitment issues may compromise an organisation’s ability to hire and retain BA practitioners who can assist managers in extracting and applying value from BA assets to their decision-making processes. Management apathy aligns with their research question on the in<sup>fl</sup>uence of BA clients regarding the use of BA results in decision-making processes. Research in this area may shed light on the extent to which managers trust and apply BA results in their decision-making processes. Organisational strategy issues align with their research questions on the in<sup>fl</sup>uences of organisational learning, knowledge-sharing, and problem-solving on the generation of strategic insights. Research in this area might investigate the strategic rami<sup>fi</sup>cations of BA projects addressing areas such as process improvement, pricing, and <sup>fi</sup>rm performance (Abbasi et al., 2016; Akter & Wamba, 2016; Fosso Wamba et al., 2018). Propositions based on these four symmetries become examples of how future IS research can avoid past mistakes in OR/MS history (Table 1).

## 3. Decentralisation of OR/MS personnel

Geo<sup>f</sup>rion (1992), citing MSR (1986), argued that the most severe problem facing OR/MS at the time was decentralisation, which refers to the lack of a central OR/MS unit and the consequent “dispersion” (Geo<sup>f</sup>rion, 1992, p. 427) and “absorption” (Rosenhead & Mitchell, 1986, p. 849) of OR/MS personnel across organisational units. Decentralisation was especially dangerous because it created several barriers to OR/MS personnel career progression and thereby decreased the attractiveness of OR/MS as a career. One important barrier was the relegation of OR/MS personnel to narrowly based problems within their own hiring unit. Limited job experiences meant that many OR/MS personnel were insu<sup>fi</sup>ciently quali<sup>fi</sup>ed for promotion along “a natural managerial career progression” (Eilon, 1980, p. 26) that would be better served by a centralised OR/MS unit providing broadly based, organisation-wide experiences. Isolation also reduced organisational support for (and the political power of) OR/MS units and their practitioners.

The impact of these issues on the OR/MS <sup>fi</sup>eld is described in Radnor & Neal’s (1973) study of OR/MS in large US industrial corporations. They found that 14 out of 64 formal OR/MS groups “had been disbanded and di<sup>f</sup>used throughout their respective organizations” (p. 433). Similar results were described in the CFPOR Report (Rosenhead & Mitchell, 1986), which found that “Almost 10% per year of O.R. practitioners leave their O. R. groups for jobs elsewhere in the same organization, many presumably in pursuit of some broader career aims” and “27% of O.R. practitioners wish they had taken an M.B.A.” (p. 848). A decade later, Fildes and

Ranyard (1997) reported that “the establishment of OR groups has apparently come to a halt with many organizations never having chosen to create an in-house group” (p. 336).

## 3.1. Evidence of decentralisation of business analytics practitioners

Decentralisation is evidenced in the BA literature. Deloitte (2013) reported that “58 percent of organizations either have uncoordinated pockets of analytical activity (20 percent) or business unit-based analytical capabilities that are in early phases of collaboration”. Some literature is prescriptive, such as Davenport (2014a) and Harris et al. (2010b). The latter article reports, “[M]ost companies with a successful analytical approach have centralised their top pros and semi-pros to some degree” (p. 21). Other articles describe trade-o<sup>f</sup>s in the centralisation–decentralisation decision but provide no absolute recommendations (e.g., Anderson, 2015; Jain, 2013; Staheli, 2016). Unfortunately, much of the extant literature does not explain why or when different BA governance strategies (e.g., centralised, centre of excellence, consulting, functional, and decentralised; Harris, Craig, & Egan, 2010a) are successful.

## 3.2. Research propositions regarding decentralisation of BA practitioners

Decentralisation can compromise an organisation’s ability to hire and retain BA practitioners who can assist managers in applying BA results to their decision-making processes. It is also reasonable to expect that today’s high estimates of BA practitioner decentralisation could increase in some future circumstances, such as when cost-cutting measures aimed at reducing OR/MS overhead were enacted during the 1980s recession (Sodhi & Tang, 2010). The decentralisation of BA practitioners is especially important because it has been associated with a decline in the organisational power of OR/MS groups and increased perceptions of their technical specialisation at the expense of organisational relevance.

The social, organisational, and structural issues of decentralisation parallel similar issues in IS fashion research (e.g., Baskerville & Myers, 2009). Brie<sup>fl</sup>y, the IS fashion literature examines technology dispersion; however, instead of investigating innovations whose adoption rates follow an S-shaped curve overtime (e.g., Bass, 1969; Rogers, 1995), IS fashion research examines less successful technologies that exhibit growth rates similar to fads in the clothing industry (i.e., “rapid, bell-shaped swings” in popularity; Abrahamson, 1996: 256). A particularly relevant example of IS fashion research is Hirschheim et al.'s (2012) comparison of growth rates of business process reengineering (BPR), service-oriented architecture (SOA), and enterprise resource planning (ERP). They found that discourses on the less successful BPR and

SOA technologies had “very ‘light’ arguments concerning the social and organizational impact of their respective innovations and had scarce discourse on the topic” (p. 73). Discourses about ERP – with its “enduring traction in organizational research and practice” (p. 65) – were deemed more valuable because they incorporated an “extensive litany of claims, grounds, quali<sup>fi</sup>ers and warrants related to the organizational and social impacts and implications for the innovation” (p. 74).

This correlation between a discipline’s initial discourse and later success underscores the potency of (and necessity for) social and organisational research in helping BA “develop into an enduring practice” such as ERP rather than “disintegrate into a transient fad” such as BPR (Hirschheim et al., 2012, p. 62). Moreover, this attention to organisational structure parallels the following research question from Sharma et al. (2014, p. 435):

● “How do existing organisational structures, routines and decision-making processes in<sup>fl</sup>uence the ability of managers and analysts to generate insights from data?”

While the OR/MS literature has investigated decentralisation, it has not adequately distinguished its e<sup>f</sup>ects from those of isolation. This distinction is important because decentralised BA practitioners do not necessarily have to be isolated from one another. The strategic management literature suggests at least two ways to mitigate decentralisation’s e<sup>f</sup>ects. The <sup>fi</sup>rst is by promoting horizontal interrelationships that bring decentralised employees together. Porter (1985) argues that horizontal interrelationships can bene<sup>fi</sup>t organisations by reducing cost, enhancing di<sup>f</sup>erentiation, sharing “valuable know-how” (p. 371), and maximising corporate performance over unit performance. Porter recommends four mechanisms: horizontal structures (e.g., partial centralisation, interdivisional task forces, and channel focus committees), horizontal systems (e.g., cross-business management systems addressing planning, control, and capital budgeting), horizontal human resource practices (e.g., forums, training, and job rotation or secondment), and horizontal con<sup>fl</sup>ict resolution processes (e.g., processes relating to management style rather than those implemented in horizontal structures and systems).

A second way to help reduce BA practitioner isolation is through virtual organisational structures (Kocharekar, 2004) implemented via information and communication technologies (ICT). Indeed, the participatory bene<sup>fi</sup>ts of using ICT have been theorised in both IS and management research (e.g., Huber, 1990; Porter, 1985, respectively). Other research (e.g., Adler & Kwon, 2002; Peppard, 2007) suggests that reducing isolation will better enable BA practitioners to share knowledge, assist each other, and otherwise build social capital. This logic is echoed by Karl Kempf, Chief Mathematician at Intel: “If you want to be good at analytical decision making, it’s not about the math. . . It’s about the relationships” (Davenport, 2012). Therefore:

Proposition 1: BA practitioner isolation is inversely associated with the ability of BA practitioners to generate insights from data.

IS research suggests that ICT can help build virtual organisational structures that reduce BA practitioner isolation. This could be valuable in large-scale data mining projects that require many participants from across the organisation (e.g., Hofmann & Tierney, 2003, 2009). Dennis, Wixom, and Vandenberg (2001) note that group support systems (GSS) can support or enhance “communication among participants”, “the evaluation. . .structuring, and analysis of information”, and performance of the group task “in the most e<sup>f</sup>ective and e<sup>fi</sup>cient way(s) possible” (p.170). However, communication support, information processing support, and process structure are largely enabling structures whose success depends on how well the technology <sup>fi</sup>ts the task (Goodhue & Thompson, 1995) and is faithfully appropriated (DeSanctis & Poole, 1994).

Proposition 2a: BA practitioner isolation is inversely associated with the use of group support systems when there is a task-technology fit.

Proposition 2b: BA practitioner isolation is inversely associated with the use of group support systems when that technology is faithfully appropriated by BA practitioners.

The way centralisation is implemented in a BA unit must also be carefully considered. Anand, Sharma, and Coltman (2016), in their study of digital data streams (DDS), found that high-agility resource allocation processes produced greater business value than low-agility processes in situations of high platform maturity or high commitment from data-driven top management. In those situations, high-agility resource allocation processes provide the <sup>fl</sup>exibility line managers need “to identify high payo<sup>f</sup> DDSbased innovations and execute them successfully” (p. 268). Conversely, low-agility resource allocation processes produced greater business value than highagility processes when platform maturity and datadriven top management commitment are low because such processes limit line managers to those DDS investments that can better leverage immature platforms and low top management commitment (Anand et al., 2016: Figure 4, p. 268). Such <sup>fi</sup>ndings can be applied to BA human resource contexts as follows:

Proposition 3a: The agility of the BA human resource allocation process has a positive moderating efect on the relationship between platform maturity and the ability to generate insights from data.

The rami<sup>fi</sup>cations of Proposition 3a are such that high levels of BA human resource allocation process agility will exhibit more positive relationships between platform maturity and the ability to generate insights from data, and low levels of BA human resource allocation process agility will exhibit less positive relationships between platform maturity and the ability to generate insights from data. Similar relationships can be forwarded about data driven top management commitment:

Proposition 3b: The agility of the BA human resource allocation process has a positive moderating efect on the relationship between data driven top management commitment and the ability to generate insights from data.

The rami<sup>fi</sup>cations of Proposition 3b are such that high levels of BA human resource allocation process agility will exhibit more positive relationships between data driven top management commitment and the ability to generate insights from data, and low levels of BA human resource allocation process agility will exhibit less positive relationships between data driven top management commitment and the ability to generate insights from data.

Organisations that successfully reduce BA practitioner isolation should, therefore, be expected to maximise both corporate and unit performance – even in decentralised contexts. This attention to corporate performance has implications for Sharma et al.’s (2014) research question on social capital (i.e., Appendix B, Table B-1, RQ #8). That research question negatively frames social capital, potentially diverting analyses away from its potential bene<sup>fi</sup>ts. In other words, social capital is seen as a half-empty glass rather than a halffull glass. This latter view is framed positively as follows:

● Can organisations grow and leverage social capital structures to improve the use of BA and, if so, how?

The social capital literature di<sup>f</sup>erentiates two types of social capital: bonding social capital arising from “internal ties within collectives” and bridging social capital arising from “external relations” (Adler & Kwon, 2002, p. 19). Given the context of decentralisation and the assumption that decentralised BA practitioners will owe a greater allegiance to their hiring unit, it is probably more fruitful to examine bridging rather than bonding capital. Bridging social capital can reduce isolation by strengthening trust, trustworthiness, reciprocity, and collaboration between actors (Putnam, 2000). Therefore:

Proposition 4: Bridging social capital between BA practitioners in separate hiring units is inversely associated with BA practitioner isolation.

Following Propositions 1 and 4, isolation would be expected to act as a partial mediator between bridging social capital and the use of BA:

Proposition 5: Bridging social capital between BA practitioners in separate hiring units is positively associated with the ability of BA practitioners to generate insights from data.

## 4. Decreased availability of OR/MS practitioners

The decreased availability of OR/MS practitioners in the 1980s was attributed to many causes, including poor career prospects for OR/MS personnel, greater opportunities in other business areas, and dissatisfaction with OR/MS jobs. Another widely discussed reason was the declining enrolments of native-born students in American and British OR/MS university programmes (e.g., Rosenhead & Mitchell, 1986; Sodhi & Tang, 2010; White, 1991). Geo<sup>f</sup>rion (1992) argued that OR/MS’s heavy emphasis on mathematics diminished its attractiveness to native-born US and UK students who were widely perceived as having poor mathematical skills (e.g., Fildes & Ranyard, 1997; Grossman, 2001; White, 1991).

Declining enrolments in turn created a large demand for international students who were more pro<sup>fi</sup>cient in mathematics and science. However, this demographic shift placed the OR/MS profession in a “vulnerable position” (Geo<sup>f</sup>rion, 1992, p. 432) because employers found it di<sup>fi</sup>cult to recruit international student graduates who were permanent residents and possessed strong communication and business application skills. In the early twenty-<sup>fi</sup>rst century, international students are also more likely to be siphoned o<sup>f</sup> by developing economies (e.g., the BRIC countries of Brazil, Russia, India, and China) and by careers in research (Sodhi & Tang, 2010).

Poor career prospects, job dissatisfaction, and declining OR/MS programme enrolments expanded the scope of the recruitment problem into a more holistic competition for limited human resources involving training, compensation, tradition, culture, career progression, turnover, and involvement (Eilon, 1980). The question is whether these past trends will appear in BA.

## 4.1. Evidence of human resource management issues in business analytics

McAfee and Brynjolfsson (2012) argue that one of the <sup>fi</sup>ve management problems facing <sup>fi</sup>rms using BA is “talent management” (p. 66). Their fears are evidenced in expectations that by 2018, the USA could face “a shortage of 140,000 to 190,000 people with deep analytical skills as well as 1.5 million managers and analysts to analyse big data and make decisions based on their <sup>fi</sup>ndings” (Manyika et al., 2011, p. 3). Richey et al. (2016), in their study of Big Data use in supply chains, reported that some study participants disclosed “a lack of knowledgeable scientists available to analyse the data” (p. 728). Similar shortfalls were found in Audzeyeva & Hudson’s (2016) case analysis of the business intelligence unit of a UK retail bank. The inability to hire su<sup>fi</sup>cient numbers of analysts creates “a signi<sup>fi</sup>cant constraint on realizing value from big data” (Manyika et al., 2011, p. 10), which in turn compromises its relevancy to managerial problem-solving.

These fears are re<sup>fl</sup>ected in troubling evidence. First, university-level BA programmes are dependent upon large in<sup>fl</sup>uxes of international students (Belkin & Jordan, 2016). Evidence for such in<sup>fl</sup>uxes is displayed in Table 2, which shows the percentage of international students enrolled in 10 leading BA master’s programmes. Furthermore, there are indications that international student enrolments are declining (e.g., Saul, 2018). China’s slowing economy and devalued currency in the mid-2010s, for example, has led to expectations of decreased future enrolments of their students at US colleges (Schultz, 2016) even though recent enrolments have been strong (e.g., Institute for International Education [IIE], 2016). Fears of enrolment declines also stem from the uncertainties of governmental immigration policies, as evidenced in the 2016 US Presidential campaign (e.g., Stein, 2016), the Brexit vote in the UK (e.g., Bennett, 2016), and more aggressive immigration policies and enforcement thereof in the US (Barajas, 2018; Topan, 2017). In turn, these uncertainties not only create barriers for incoming international students, but often prompt graduating international students to return home (Siddiq, 2013).

A second recruitment concern derives from uncertainties surrounding worker visa programmes. The US H-1B visa lottery programme provides 65,000 work visas to skilled foreign workers annually (Kendall, 2017), but the demand for such workers is estimated to be three times that amount (O'Brien, 2017). Despite this demand, at the beginning of the twenty-<sup>fi</sup>rst century, the number of science and engineering workers entering the USA was declining while the return rate of this talent to their home countries was increasing (Manning, Massini, & Lewin, 2008). In a move that may exacerbate these shortfalls, the Trump administration drafted an executive order in 2017 to “overhaul” the H-1B programme in order to “[prioritize] the protection of American workers” (Kendall, 2017). Indeed, evidence suggests this executive order is generating a “reverse tech migration” (Rivers, 2017). Similar problems confront tech companies in the UK, which faces a “triple whammy” from “a critical fall-o<sup>f</sup> in STEM skills in its own population”, visa restrictions on “the availability of high-skilled specialists from overseas”, and uncertainties relating to Brexit’s e<sup>f</sup>ects on the UK’s “highly international tech workforce” (Butcher, 2017). It is di<sup>fi</sup>cult to predict the extent to which these social and political factors will a<sup>f</sup>ect the availability of BA students and professionals. However, it is clear that these uncertainties are troubling to universities that enrol these students, organisations that hire their graduates, and stakeholders who depend on the ultimate success and survival of BA investments.

Organisations face other human resource management (HRM) problems. Developing countries could siphon o<sup>f</sup> employed BA practitioners, thus creating a turnover problem. The spectre of turnover presents a di<sup>f</sup>erent set of problems than recruitment. Much turnover research (e.g., Allen, Bryant, & Vardaman, 2010; Vardaman et al., 2016) has focused on relationships between turnover and organisational commitment, support, and culture. This could provide an important reference discipline for future BA research.

## 4.2. Research propositions regarding human resource management in business analytics

HRM problems in OR/MS have been framed largely in terms of increased competition for a limited pool of quali<sup>fi</sup>ed job applicants, di<sup>fi</sup>culties in OR/MS practitioner career progression, lower perceptions of organisational support, and stronger intentions to leave the organisation (e.g., Eilon, 1980). If current projections about BA practitioner shortfalls come to pass, there will undoubtedly be increased competition for this limited resource as well as knock-on e<sup>f</sup>ects, such as using undertrained employees to <sup>fi</sup>ll the gap (e.g., Davenport, 2014b). The dangers of relying on undertrained employees could be exacerbated by unrealistic expectations that such employees can e<sup>f</sup>ectively use a<sup>f</sup>ordable, commercially available BA software tools. Indeed, the availability of such tools was seen as a danger by some in OR/MS because it could serve as an excuse to assign undertrained sta<sup>f</sup> to OR/MS problems or even forego hiring OR/MS specialists (e.g., Geo<sup>f</sup>rion, 1992; Powers, 2010). Such HRM-related organisational structures, practices, and decisions parallel the following research question from Sharma et al. (2014, p. 435):

● “How do existing organisational structures, routines and decision-making processes in<sup>fl</sup>uence the ability of managers and analysts to generate insights from data?”

The OR/MS literature suggests several related propositions. The <sup>fi</sup>rst two involve recruitment shortfalls:

Proposition 6a: Increased competition for business analytics practitioners will result in greater numbers of under-trained people using business analytics tools.

Proposition 6b: The number of under-trained people using business analytics tools is inversely related to the ability of managers and analysts to generate insights from data.

Employee turnover is another problem. HRM and organisational behaviour research, founded in organisational support theory (e.g., Eisenberger, Huntington, Hutchinson, & Sowa, 1986, 1990; O’Reilly III & Chatam, 1986), demonstrates that employee turnover can be mitigated by increasing employee perceptions of organisational commitment and support (e.g., Vardaman et al., 2016) and employee engagement through targeted training, rewards, and supervisory practices (e.g., Allen et al., 2010). Perceived organisational support has also been argued to be a critical element in building and embedding the knowledge and skills that BA practitioners possess (e.g., Ransbotham et al., 2016).

Table 2. Percent of international students in various top 25 US MSBA Programmes<sup>a.</sup>

<table><tr><td>Source</td><td>Percent of Int&#x27;l Students</td></tr><tr><td>Arizona State University – W.P. Carey School of Business (2017)</td><td>74% (Fall 2016)</td></tr><tr><td>Case Western Reserve University – Weatherhead School of Management (2017)</td><td>81% (Fall 2016)</td></tr><tr><td>Duke University – Fuqua School of Business (2017)</td><td> $84\%^{\text{b}}$ </td></tr><tr><td>Massachusetts Institute Of Technology – Alfred P. Sloan School of Management (2017)</td><td>57% (Class of 2018)</td></tr><tr><td>North Carolina State Univ. – Institute for Advanced Analytics (2017)</td><td>17% (Class of  $2018^{\text{c}}$ )</td></tr><tr><td>Univ. of California, San Diego – Rady School of Management (2017)</td><td>92% (Fall 2017)</td></tr><tr><td>Univ. of Minnesota – Carlson School of Management (2017)</td><td>84% (Class of 2018)</td></tr><tr><td>Univ. of Southern California – Marshall School of Business (2017)</td><td>85% (Class of 2016)</td></tr><tr><td>Univ. of Texas, Austin – McCombs School of Business (2017)</td><td>41% (2017 Admitted Class Profile)</td></tr><tr><td>Univ. of Texas, Dallas – Jindal Schools of Management (2017)</td><td>86% (Fall 2017)</td></tr></table>

Perceived organisational support thus becomes a knowledge management issue for at least two related reasons. First, BA practitioners are in demand, so increasing perceived organisational support among them provides a means for retaining those employees. Second, turnover is associated with knowledge loss, particularly the loss of tacit knowledge (Droege & Hoobler, 2003). As BA knowledge is lost, managers <sup>fi</sup>nd it harder to obtain relevant “know-how” to generate and explain BA results. Therefore:

Proposition 7a: BA practitioner turnover is inversely related to the ability of managers and analysts to generate insights from data.

Proposition 7b: BA practitioner engagement is inversely related to BA practitioner turnover.

Proposition 7c: BA practitioner perceptions of organisational support are inversely related to BA practitioner turnover.

## 5. Persisting management apathy towards OR/MS

Perhaps, one of the biggest reasons for management apathy was that OR/MS failed to account for the generalised perspectives of organisational managers. Managers need generalised perspectives because they confront messes (i.e., “dynamic situations that consist of complex systems of changing problems that interact with each other”; Acko<sup>f</sup>, 1979a, p. 99). “Messy” and “wicked” problems are the world of managers, a world that has often been seen to be incompatible with OR/MS (e.g., Fildes & Ranyard, 1997).

OR/MS’s inability to appreciate the systemic, systematic nature of organisations has been linked to its Machine Age, reductionist worldview (e.g., Acko<sup>f</sup>, 1979a, 1979b). Managers who felt OR/MS had little relevancy to solving their problems were less motivated to <sup>fi</sup>nd suitable projects. In turn, fewer OR/MS projects led to less visibility, creating a feedback loop that diminished OR/MS’s perceived relevancy and increased management apathy. Andrews (1971) captured this tension when he observed that the OR/MS specialist “prefers to work on problems responsive to his techniques rather than more important though less structured problems” of interest to general managers (p. 17).

A second reason for management apathy was that OR/MS techniques – and the explanations thereof by OR/MS practitioners – were typically opaque to general managers. This opacity was attributed to the strong technique orientation of OR/MS practitioners (e.g., Kirby, 2000) coupled with their inability to explain to their clients’ satisfaction how results were obtained from OR/MS methods (e.g., Collcutt, 1965; Radnor & Neal, 1973; Eilon, 1980; Wagner, Rothkopf, Thomas, & Miser, 1989; Geo<sup>f</sup>rion, 1992 citing MSR, 1986; Fildes, Ranyard, & Crymble, 1999). Several reasons for this orientation were forwarded in the OR/MS literature. Reisman and Kirschnick (1994) stated one shortcoming lay in professional regression (i.e., “professions tend to withdraw into themselves, away from the tasks for which they claim public jurisdiction”; p. 579, citing Abbott, 1988, pp. 118– 119). This shortcoming was reinforced in OR/MS research journals, which Sodhi and Tang (2010) argued, “are inclined toward mathematical theory and are more likely to publish highly mathematical and abstract articles rather than articles that re<sup>fl</sup>ect the complexities of real-world problems that require multiple approaches” (p. 280).

## 5.1. Evidence of management apathy towards business analytics

BA may fall victim to management apathy if managers begin to believe that BA – like OR/MS before it – is less useful than intuition, “gut feelings”, or other methods for carrying out their responsibilities. Indeed, some evidence is beginning to surface that management dissatisfaction with (and apathy towards) BA are already setting in. A recent Forrester study found that “60 percent of respondents were not very con<sup>fi</sup>dent in their [business analytics] insights” and “the lack of trust in data and analytics may start at the top” (Olavsrud, 2016). Similar misgivings about BA suppliers have also been found (e.g., Bennett, 2012). This lack of trust may be due in part to the “black box” nature of BA’s mathematical techniques that obscure the transparency of their methods and interpretability of their results (Müller et al., 2016, p. 290).

Coupled with this lack of trust are signi<sup>fi</sup>cant declines in the perceived bene<sup>fi</sup>ts of BA. Ransbotham et al. (2016), for example, described these changing perceptions between 2010 and 2015. From 2010 to 2012, the percentage of respondents in their study who believed BA creates a competitive advantage rose from about 37% in 2010 to about 67% in 2012. However, that percentage stalled at about 65% in 2013, then declined to about 61% in 2014 and 51% in 2015 (Ransbotham et al., 2016, p. 5). They also noted that “one-third (38%) of their respondents agree that analytics hasn’t lived up to its hype, and 32% think management’s expectations are too high” (p. 7). The reluctance to embrace BA is also evidenced by lower than expected job openings for data scientists (e.g., Burns, 2016). Thus, it appears that BA is beginning to face the same mistrust from managers that OR/MS faced in the late 1960s. A related reason may lie in perceptions that BA’s mathematical and computational techniques and technologies are still immature (e.g., Bennett, 2012). “Despite the hype”, noted Ransbotham et al. (2016), “the reality is that many companies still struggle to <sup>fi</sup>gure out how to use analytics to take advantage of their data” (p. 3).

Such dissatisfaction and perceived irrelevancy are existential threats to BA because widespread scepticism of BA’s ability to resolve problems and exploit opportunities would almost certainly curtail managerial support for long-term allocations of resources to ensure its success and survival.

## 5.2. Research propositions regarding management apathy towards business analytics

Gri<sup>f</sup>eth, Gaertner, and Sager (1999) theorised that apathy could be used as one of the several dimensions to classify employees for the purposes of predicting behaviour. To that end, they created an employee type scale (Appendix C, Table C-1) as an independent variable in their adaptive response model (ARM). ARM “proposes how employees adapt to the organization following changes in organizational policies that are perceived as dissatisfying” (p. 577). They added that an individual’s classi<sup>fi</sup>cation within an employee type is not static but can evolve over time.

ARM is a process model. Initially, employee dissatisfaction is engendered by “shocks” and “catastrophes” (i. e., events requiring quick or slow adaptation, respectively; p. 579). In turn, employee dissatisfaction is followed by di<sup>f</sup>erent response tendencies, initial responses, and behavioural outcomes based on employee type. For example, apathetics exhibit neglect tendencies, calculated job withdrawal responses, and “alternative forms of withdrawal” such as tardiness, absenteeism, theft, and satis<sup>fi</sup>cing. Lone wolves, on the other hand, exhibit exit tendencies, intentions to quit, and job termination behaviours.

Additional research has extended ARM to managerial behaviour; for example, Voutsina, Mourmant, and Niederman (2014) used ARM to explain why managers – who constituted 65% of their sample pool of salaried employees (K. Voutsina, personal communication, January 19, 2017) – voluntarily leave an organisation to start their own businesses. In a BA context, managers can become frustrated by their inability to understand a BA practitioner’s methods, results, or explanations thereof. These “shocks” and “catastrophes” engender dissatisfaction with BA which, according to ARM, will engender di<sup>f</sup>erent tendencies, responses, and behaviours across the di<sup>f</sup>erent employee types. In the BA context, neglectful apathetic behaviours include the failure to apply BA results to organisational decisions; using simpler, less accurate analytical tools (e.g., as has been alleged in OR/MS; Powers, 2010); or exhibiting indi<sup>f</sup>erence towards, low job involvement with, and/or low commitment to BA projects.

ARM further suggests that Sharma et al.'s (2014) focus on “the use of business analytics” can be extended to include the users of BA. This adaptation is consistent with the long history of research associating IS use with a variety of user characteristics, including users’ performance and e<sup>f</sup>ort expectancies (Venkatesh, Morris, Davis, & Davis, 2003), computer literacy and competency (Davis, Kettinger, & Kunev, 2009; Goodhue, 1995), perceptions of usefulness and ease of use (Davis, Bagozzi, & Warshaw, 1989), and training and motivation (Goodhue & Thompson, 1995). In short, BA researchers must study people (e.g., personal characteristics such as trustworthiness and communication abilities) as well as practice and procedure. Accordingly, Sharma et al .'s (2014) research question about organisational decisionmaking processes (i.e., Appendix B, Table B-1, RQ #1) can be modi<sup>fi</sup>ed as follows:

● How do the characteristics and perceptions of BA clients in<sup>fl</sup>uence the use of BA in organisational decision-making processes?

An important insight from ARM is that a specific personal attitude is a less powerful predictor of employee behaviour than a person’s overall employee type. The explanatory power of the latter is predicated on the notion that the mix of personal factors varies across employee type, and that some mixes will mitigate apathy’s e<sup>f</sup>ect more strongly than others will. For example, citizen-type employees might be apathetic to BA, but their high commitment to the organisation wil likely override their apathy. In turn, citizen-type employees will exhibit stay/perform rather than withdrawal behaviours (e.g., Davis, 2013). This insight from ARM transforms the “lessons learned” from OR/MS history from a speci<sup>fi</sup>c attitude (e.g., apathy) to an overall employee type (e.g., apathetic).

The question then becomes one of contextualising dissatisfactions to the BA managerial context. IS research provides some clues. Staples, Wong, and Seddon (2002), for example, argued that perceived net bene<sup>fi</sup>t is a more useful construct than satisfaction because it captures user satisfaction and other dimensions (e.g., IS e<sup>f</sup>ectiveness). Indeed, they found that unrealistic expectations for new IS have adverse e<sup>f</sup>ects on users’ perceived net bene<sup>fi</sup>t, which is strikingly similar to Ransbotham et al.'s (2016) <sup>fi</sup>nding that management’s expectations about BA’s bene<sup>fi</sup>ts are often too high. The focus on perceived net bene<sup>fi</sup>t has additional advantages, including implications that BA projects must deliver positive net bene<sup>fi</sup>ts, that BA clients must perceive those bene<sup>fi</sup>ts correctly, and that the BA practitioner is responsible for communicating that net bene<sup>fi</sup>t to the client. Accordingly, studies investigating the e<sup>f</sup>ects of negative perceived net bene<sup>fi</sup>t could be more fruitful than those investigating dissatisfaction. Therefore:

Proposition 8: Client employee type moderates the relationship between the client’s negative perceived net benefit of BA and their related BA behavioural outcomes.

The rami<sup>fi</sup>cations of Proposition 8 are such that institutionalised stars and citizens will exhibit stay and perform behaviours; lone wolves, leave behaviours; and apathetics, alternative withdrawal behaviours.

## 6. Inadequate progress in using OR/MS insights to guide strategy

The OR/MS literature noted that early leading researchers toted “admirable aspirations” about the way OR/MS interwove strategy and tactics (Fildes & Ranyard, 1997: p. 342), yet many in the <sup>fi</sup>eld contended the discipline was focusing largely on operational problems while leaving strategic problems for other departments (e.g., Dando & Sharp, 1978). This dichotomy is perhaps best exempli<sup>fi</sup>ed as OR/MS’s “slow progress on strategic problems” being ranked as the fourth most important problem facing OR/ MS by the Management Science Roundtable (Table 1).

The lack of contribution to strategic issues was important for several reasons. First, OR/MS’s focus on operational problems diminished the visibility of OR/MS contributions to senior managers, who were thus less likely to recognise or appreciate the contributions of the OR/MS sta<sup>f</sup> (Little, 1991). Indeed, “Lack of recognition by sr. managers” was voted the third most important problem facing OR/MS by the Management Science Roundtable (Table 1). This under-appreciation by senior management led to a second problem: the common perception that OR/MS professionals were largely technical sta<sup>f</sup> who could be dispersed across other departments. While often justi<sup>fi</sup>ed as a way to avoid the overhead costs of an OR/MS department, such dispersions also reduced the political and organisational power of OR/MS sta<sup>f</sup> (Geo<sup>f</sup>rion, 1992; MSR, 1986). Third, OR/ MS’s lack of contribution to strategic issues diminished opportunities to work and develop relationships with senior managers, experiences that strengthened the ability and likelihood of OR/MS sta<sup>f</sup> advancing to top management positions (Kirkwood, 1990).

The OR/MS literature has discussed a number of reasons for inadequate progress in applying OR/MS to strategy formulation and analysis. One reason involved the inherent complexity and interdisciplinarity of strategic problems (Kirkwood, 1990; McClelland, 1975; Wagner et al., 1989). OR/MS techniques, with their high reliance on developing one central mathematical model, cannot adequately represent complex strategic problems involving “many conceptions about the state of the surrounding world, about input data, [and] about what variables can be treated as exogenous”; in short, any strategic OR/MS project must encompass “a linked consortium of models” (Wagner et al., 1989, p. 671).

To address this oversight, Fildes and Ranyard (1997) recommended that OR/MS actively pursue strategic issues in research and practice. Some of this research advised OR/MS researchers and practitioners to learn and apply new methodologies that are more compatible with strategic problem solving. These include systems analysis (Wagner et al., 1989) and “soft” OR methods such as the Soft Systems Methodology (SSM; e.g., Checkland & Scholes, 1990; Ledington & Donaldson, 1997; Ormerod, 1995, 1996).

## 6.1. Evidence of inadequate progress on using BA insights to guide strategy

Ransbotham et al. (2016) found that the “percent of respondents who are somewhat or very e<sup>f</sup>ective at using [BA] insights to guide future strategy” declined from 56% in 2012 to 49% in 2015 (p. 6). Another disturbing <sup>fi</sup>nding involved failures to improve competitive advantage. In 2012, 66% of their respondents indicated that BA created a competitive advantage, but that percentage declined to 51% in 2015. Of those respondents who agreed that their organisation had “di<sup>fi</sup>culty gaining competitive advantage with analytics” (p. 6), 28% agreed with the statement, “We are using analytics, but so are our competitors” (p. 6). While this failure to achieve or increase competitive advantage could be explained by other factors (e.g., 37% agreed with the statement “We have just begun to apply analytics and need more experience”; 29%, “We do not use analytics to drive strategic decisions”; p. 6), it appeared to Ransbotham and colleagues that BA was “losing its luster” and that there was no “simple <sup>fi</sup>x” (p. 5) to the competitive advantage problem.

Another issue is the need for interdisciplinarity in strategy guidance (e.g., Kirkwood, 1990). The importance of interdisciplinarity in BA was shown by Chang, Kau<sup>f</sup>man, and Kwon (2014), who advocate both “interdisciplinary convergence” (p. 70) and “‘walkabout’ observation” to identify key informants in big data projects (p. 78). The latter is particularly important, reason Chang et al., because informants help BA practitioners “understand the simple aspects and complexities of the research settings, and key events that have occurred or are due to happen that make it possible to conduct insightful natural and fully-speci<sup>fi</sup>ed experiments” (p. 78).

## 6.2. Research propositions regarding the use of BA insights to guide strategy

The lack of contribution to strategy by OR/MS and BA is a discomforting criticism. While it may seem unfair given these disciplines’ success in addressing operational problems, that criticism can be justi<sup>fi</sup>ed by the many claims that have been made about BA’s ability to produce strategic insights (e.g., SAS, 2018; see also Chen, Chiang, & Storey, 2012; Evans, 2012; Klatt, Schlaefke, & Moeller, 2011; Lau, Liao, Wong, & Chiu, 2012; Ransbotham et al., 2016). This inequity suggests at least two opportunities for future research. First, what can BA learn from OR/MS’s history about contributing to organisational strategy? Second, instead of asking whether BA is strategic or operational, we should ask how BA could become strategic and operational. It is in this latter context that the last set of propositions is forwarded.

Using statistical methods to guide and formulate strategy has been problematic in both OR/MS and BA. Unfortunately, the OR/MS literature – while arguing for the importance of addressing strategy analysis and formulation – has provided little direction on how to do so. For example, it has tended to frame strategy largely as competitive advantage (e.g., Bell & Anderson, 2002) rather than address such strategic questions as “what set of businesses should we be in?”, “how to compete in a particular industry or product/market segment?”, how to maximise resource productivity, or how to get these various strategies to “<sup>fi</sup>t together to form a coherent and consistent whole” (Hofer & Schendel, 1978, pp. 27–28). In addition, studies examining OR/MS’s contributions to strategy have largely focused on if OR/MS projects have provided competitive advantage or how to convince upper management of such contributions (e.g., Bell & Anderson, 2002; Kirkwood, 1990). Little of that research explained why some OR/MS projects contribute to strategy or how one ensures future OR/MS projects will do so.

Strategy analysis and formulation are complex and multifaceted, so enhancing our ability to apply BA to this domain will require much work. However, focusing solely on “methodological sophistication”, as Richey et al. (2016) caution, “will only widen the gap between research, practice, and impact” (p. 734). We will, therefore, examine two “lessons learned” from the OR/MS literature. The <sup>fi</sup>rst involves perceptions of specialised technique application at the expense of generalised problem-solving (which is more relevant to strategy). The second involves a lack of interdisciplinarity in OR/MS practice that compromised the OR/MS practitioner’s ability to contribute to complex strategic issues.

## 6.3. Generalised problem-solving

“Strategy formulation processes”, state Hofer and Schendel (1978), “can be viewed as a special kind of problem-solving process for de<sup>fi</sup>ning an organization’s strategy” (p. 46). They involve assessments of the organisation’s current strategy; opportunities and threats in the environment; principal skills and resources; gaps between objectives, strategies, and resources against opportunities and threats; available options for building new strategies; and the appropriateness of strategic options vis-à-vis stakeholder values. The complexity of strategy formulation suggests that it is more akin to problem solving (i.e., “<sup>fi</sup>xing agendas, setting goals, and designing actions”) than to decision-making (i.e., “evaluating and choosing”) (Simon et al., 1987, p. 11). Moreover, the process phases of decision-making – especially choice – in the OR/MS context have been heavily in<sup>fl</sup>uenced by economics and statistics, whereas problem-solving focuses more on psychological factors (e. g., intuition and judgment) and the ill-structured nature of problems (e.g., complex, ambiguous, and/or illde<sup>fi</sup>ned goals; con<sup>fl</sup>icting values; shifting problem formulations) (Simon et al., 1987).

Problem-solving subdomains that may be particularly useful include problem structuring and problem– problem solver relationships (e.g., Smith, 1988) as well as problem conceptualisation, representation, and elicitation (e.g., Browne & Rogich, 2001). Participative methodologies such as SSM and other “soft OR” methods (e.g., Checkland & Scholes, 1990; Ledington & Donaldson, 1997; Ormerod, 1995) have been used to develop IS strategy (e.g., Ormerod, 1995, 1996), and may thus be particularly helpful.

This systems-based philosophy reveals at least three related problems within OR/MS: “how to design and manage systems so that they can e<sup>f</sup>ectively serve their own purposes, the purposes of their parts, and those of the larger systems of which they are part” (Acko<sup>f</sup>, 1979a, p. 96). For Acko<sup>f</sup>, OR/MS had been concerned primarily about the <sup>fi</sup>rst problem at the expense of the latter two. “Its models”, Acko<sup>f</sup> (1979a) argued, “are predominantly of closed mechanical systems, not of open purposeful systems” (p. 97). In addition, SSM has been viewed as a way to increase OR/MS’s relevance to “the world of management” by shifting the focus “from optimization to learning; from prescription to insight; from ‘the plan to the ‘planning process’; from reductionism to holism” (Checkland & Scholes, 1990, p. 15, referencing Pruzan, 1988). These shifts are largely consistent with BA (e.g., Audzeyeva & Hudson, 2016; Davenport, Harris, De Long, & Jacobson, 2001; Marchand & Peppard, 2013). Accordingly, these literatures will be used to extend Sharma et al.'s (2014) Research Questions #4 and #6 (Appendix B, Table B-1), respectively:

● How do existing organisational learning, knowledge-sharing, and problem-solving processes in<sup>fl</sup>uence the ability of managers and analysts to generate strategic insights from data?

● How do the structures and processes of organisational learning, knowledge-sharing, and problem-solving in<sup>fl</sup>uence the ability of insight generation teams to generate strategic insights from the use of BA?

While there may be many ways that SSM and related methods can improve BA’s ability to generate strategic insights, one promising way is through improved con<sup>fl</sup>ict resolution. The importance of data for resolving con<sup>fl</sup>icts in strategic decision-making has been widely researched by Eisenhardt and her colleagues. One consistent <sup>fi</sup>nding is that objective, up-to-date data “encourages people to focus on issues, not personalities” and avoids “[wasting] time in pointless debate over opinions” (Eisenhardt, Kaywajy, & Bourgeois III, 1997, p. 79). Importantly, the use of data changes the nature – but not necessarily the level of con<sup>fl</sup>ict. “Management teams troubled by interpersonal con<sup>fl</sup>ict”, they noted, “[relied] more on hunches and guesses than on current data” (p. 79). More successful management teams focused on “substantive” con<sup>fl</sup>ict (p. 80) that “provides executives with a more inclusive range of information, a deeper understanding of the issues, and a richer set of possible solutions” (p. 83) as well as better and faster solutions.

The importance of con<sup>fl</sup>ict resolution in strategic decision-making mirrors SSM’s notion of accommodation (i.e., “<sup>fi</sup>nding versions of the (improved) situation which di<sup>f</sup>erent people with di<sup>f</sup>erent worldviews could nevertheless live with”); (Checkland, 2010, p. 130). Accommodation is accomplished when participants mental models of problematic situations and potential solutions are compared so that con<sup>fl</sup>icting “myths and meanings which human beings attribute to their professional (and personal) entanglements with their fellow beings” are resolved (Checkland & Scholes, 1990, p. 44). Accommodation means that BA practitioners must become pro<sup>fi</sup>cient in both strategy-related and mathematical/statistical analysis, and that BA projects cannot be approached in the same way as large, traditional IT projects. Marchand and Peppard (2013) note that while traditional IT projects typically involve “de<sup>fi</sup>ned outcomes, required tasks, and detailed plans for carrying them out”, a BA project “frames questions to which the data might provide answers, develops hypotheses, and then iteratively experiments to gain knowledge and understanding” (p. 106). They add that “conventional methods” are ill-suited to BA projects; instead, “a fundamentally di<sup>f</sup>erent approach and mind-set” is needed (p. 112). “Soft” systems methodologies can <sup>fi</sup>t such a requirement:

Proposition 9: BA practitioners who use a “soft” systems methodology to address strategy-related BA problems will generate more strategic insights than those who do not.

## 6.4. Interdisciplinarity

The lack of interdisciplinarity has been a common criticism of OR/MS and BA research and practice (e. g., Wagner et al., 1989; Kirkwood, 1990; Davenport,

Harris, & Morison, 2010). IS research can o<sup>f</sup>er important insights into interdisciplinarity because IS practitioners must understand their clients’ knowledge domain in order to construct relevant questions during the elicitation process (e.g., Browne & Rogich, 2001). It is important for BA practitioners as well. For example, Marchand and Peppard (2013) found that “candid conversations across disciplines” helped managers from di<sup>f</sup>erent functions generate “new interpretations of data and business ideas” in a “discovery and learning environment” (p. 110). They concluded that creating environments “where people can use the company’s data and their own knowledge” is necessary to “improve the <sup>fi</sup>rm’s operational and strategic performance” (p. 112; emphasis added).

BA practitioners who employ organisational learning and knowledge-sharing to achieve higher levels of interdisciplinarity will be better able to understand their client’s problem space, and, therefore, be more likely to design BA projects that generate strategic insights from data. However, the ability to generate strategic insights will likely take time as the organisation learns to adapt organisational structures, resolve stakeholder frictions, overcome organisational inertia, and optimise BA projects over the long term (e.g., Audzeyeva & Hudson, 2016). This temporal quality of interdisciplinarity suggests it will have a mediating e<sup>f</sup>ect between BA practitioner isolation and the generation of strategic insights.

Proposition 10a: BA practitioner isolation is inversely associated with BA practitioner interdisciplinarity.

Proposition 10b: BA practitioner interdisciplinarity will be positively associated with the generation of strategic insights from data.

For completeness, Proposition 1 (i.e., BA practitioner isolation is inversely associated with the ability of BA practitioners to generate insights from data) is extended to strategic insights in the following corollary:

Corollary 1: BA practitioner isolation is inversely associated with the ability of BA practitioners to generate strategic insights from data.

Propositions 1, 10a, and 10b, and Corollary 1 can be further extended by envisioning organisational strategy as a three-level problem space: corporate (“what set of businesses should we be in?”), business (“how to compete in a particular industry or product/ market segment”), and functional (“maximization of resource productivity”) (Hofer & Schendel, 1978, pp. 27–29). This three-level structure has been used to frame the extent to which OR/MS activities realised competitive advantage (e.g., Bell & Anderson, 2002). Each level requires a di<sup>f</sup>erent amount of interdisciplinarity, with functional having the lowest requirement level and corporate having the highest. These di<sup>f</sup>ering requirements have an e<sup>f</sup>ect on BA practitioners; that is, they typically begin their careers at the lowest level of strategy (i.e., the functional level) but must increase their interdisciplinarity in order to advance to more complex and more challenging strategic projects. This means that a BA practitioner with a given level of interdisciplinarity will be able to generate more strategic insights at the functional level than at the business level and more strategic insights at the business level than at the corporate level. This suggests strategy environment levels will have a moderating e<sup>f</sup>ect on the relationship between interdisciplinarity and strategy insight generation:

Proposition 11: Strategy hierarchy level will negatively moderate the relationship between BA practitioner interdisciplinarity and that practitioner’s ability to generate strategic insights from data.

In other words, higher strategy hierarchy levels will exhibit less positive relationships between a BA practitioner’s interdisciplinarity and their ability to generate strategic insights from data than lower strategy hierarchy levels will exhibit. There is another way to envision this negative moderation e<sup>f</sup>ect; that is, as BA practitioners move up the strategy hierarchy, they will require higher levels of interdisciplinarity in order to generate similar levels of strategic insights.

Strategy environment hierarchy can moderate other relationships as well. For example, Corollary 1 asserts that increased BA practitioner isolation will lead to decreased levels of strategic insights from data. It is reasonable to assume that interdisciplinarity requirements across the strategy environment hierarchy would come into play here as well. That is, BA practitioners who are isolated from other BA practitioners will not only be less knowledgeable about BA practices and techniques but will also be isolated from other non-BA employees who might share organisational knowledge. This lack of knowledge will make them less able to conduct BA requirements determination successfully in strategic projects. Therefore:

Proposition 12: Strategy hierarchy level will negatively moderate the relationship between BA practitioner isolation and that practitioner’s ability to generate strategic insights from data.

In short, higher strategy hierarchy levels will exhibit more negative (or less positive) relationships between a BA practitioner’s isolation and their ability to generate strategic insights from data than lower strategy hierarchy levels.

## 7. Discussion

OR/MS’s history should temper our predictions and certainties of BA’s future as a research topic or an organisational practice. The opinions and propositions expressed in this article are not intended to predict BA’s future. Indeed, there are many plausible futures for BA. Two opposing possibilities were noted by a reviewer of this article. On the one hand, BA could also end up like entity-relationship diagrams, which are a “very vibrant commercial product” even though it is not the subject of much current research. On the other hand, notes that reviewer, BA could end up as a vibrant research activity with little practical impact. Both futures – and indeed others as well – are possible for BA. Again, the intent is not to predict the future, but to guide BA research in ways that can generate the depth of discourse needed to advance BA’s success and survival as both a research topic and an organisational practice.

In this way, the propositions forwarded herein seek to leverage “lessons learned” from OR/MS’s past to help mitigate potential problems in BA’s future. Technical issues have been avoided in order to focus on BA’s social and organisational aspects. It is hoped that the propositions will direct IS research towards making signi<sup>fi</sup>cant, meaningful, theoretical, and practical impacts on BA’s relevance to managerial decision-making, problem-solving, strategy guidance, and organisational success (Appendix B, Table B-2).

The article also seeks to guide research in ways that assist organisations – as well as individuals – in obtaining greater returns on their investments of time, talent, and treasure in BA. This does not mean IS researchers should use these propositions to save BA at any cost. Rather, the propositions provide starting points from which IS researchers can improve the discourse among themselves and practitioners about BA theory and practice via timely, reasoned arguments evaluating the technical and organisational aspects of these popular new technologies. We must avoid the pitfalls of blindly chasing fads and fashion. Instead, we must follow Hirschheim et al.'s (2012) wise counsel to provide a “more <sup>fi</sup>ne-grained, scholarly analysis at an early stage that would validate reasonable claims about an innovation and simultaneously prevent detrimental ‘<sup>fl</sup>ighty claims from taking o<sup>f</sup>” (p. 77).

Researchers can use these propositions and related discussions to inform and/or guide their future research. However, in keeping with the question of BA’s potentially limited lifespan, researchers – especially aspiring Ph.D. students – should develop contingencies in case the BA wave – like other waves in the ocean of IS research – eventually goes <sup>fl</sup>at. One way to address this danger is to ground BA research in fundamental problems (e.g., social and organisational issues surrounding IS) and be able to generalise those results to other areas.

Attending to fundamental problems can help researchers not only “surf” the current wave of popularity for BA research by providing an important and interesting context of study; it can also ease the transition to new opportunities should the researcher need to “bail” from the BA wave and pursue other topics.

## 7.1. Limitations and future research

There are several limitations to this research. First, many criticisms against OR/MS are from the 1970s to 1990s. The extent to which times have changed must be assessed. Coupled with this limitation are potential objections from current OR/MS researchers who might argue that OR/MS has not lost its relevancy to managerial problems but has instead been temporarily overshadowed by other domains and problems du jour (e.g., BA). The opinions expressed herein are not intended as a criticism of current OR/MS research. Rather, these opinions extend the argument of OR/MS relevancy by pointing out that OR/MS literature published in the early and mid-1980s on their discipline’s near-death experience is especially relevant today because it provides insights that can help current BA researchers and practitioners avoid similar troubles.

Second, many articles from the OR/MS literature of the 1980s cited herein express a more hopeful future for OR/MS (e.g., see the “After the Storm” section of Appendix A). Similarly, several of the BA articles cited herein are optimistic about BA’s future. A CompTIA survey, for example, found that 75% of their respondents agreed “their business would be stronger if they could harness all of their data” (Terdoslavitch, 2016). Ransbotham et al. (2016) report that “Many managers agree that analytical results have not lived up to the hype, yet a large proportion of managers remain optimistic about the potential of analytics and believe the use of analytics in their organization will increase signi<sup>fi</sup>cantly in the next few years” (p. 7). They also found that C-level, senior, and general managers in organisations that were categorised as “analytic innovators” were far more likely to indicate a “moderate or great use of analytics” than managers in other organisations (p. 10). While these positive opinions might be viewed as contradicting the need to investigate the propositions forwarded herein, they would be better seen as a glimpse into a possible future for BA – one that can be realised through interesting research into BA’s social and organisational contexts.

Third, this article focused on just four problem areas and only a few of Sharma et al.'s (2014) research questions. OR/MS is not the only domain whose history can provide insights into future BA research. Promising domains include other management fashions (e.g., scienti<sup>fi</sup>c management and management by objectives), data mining, text mining, and arti<sup>fi</sup>cial intelligence. BA research based on all of the aforementioned domains can produce the balanced, critical discourses that helped establish ERP in many organisations versus the one-sided technical discourses that helped drive BPR to its faddish end (Hirschheim et al., 2012).

## 8. Conclusions

Lessons learned from OR/MS history suggest a number of ways that IS researchers can help foster a successful future for BA and its practitioners and researchers. Extending Sharma et al.'s (2014) research agenda to include questions regarding BA’s social and organisational contexts is one means to that end. Such research can help mitigate BA practitioners isolation, enhance their career potential, facilitate their ability to motivate managerial clients to participate in and accept BA projects, and support their ability to address strategy-related problems.

## Acknowledgments

The author wishes to thank the co-editor, associate editor, and anonymous reviewers for their numerous comments and suggestions. In particular, I would like to thank the associate editor for pointing out that OR/MS’s popularity may have been supplanted only temporarily by other domains “du jour”. I would also like to thank the following individuals for their assistance: Frank Adams, Kent Marett, Laura Marler, and James Vardaman for their suggestions about early drafts of this article; Katerina Voutsina and Fred Niederman for information about their sample from Voutsina et al. (2014); and Tracy Cahall for tracking down a copy of the MSR (1986) report.

## Disclosure statement

No potential con<sup>fl</sup>ict of interest was reported by the author.

## ORCID

Robert F. Otondo http://orcid.org/0000-0002-3502-8877

## References

Abbasi, A., Sarker, S., & Chiang, R. H. L. (2016). Big data research in information systems: Toward an inclusive research agenda. Journal of the Association for Information Systems, 17(2), i–xxxii.

Abbott, A. (1988). The system of professions: An essay on the division of expert labor. Chicago, Illinois: University of Chicago Press.

Abrahamson, E. (1996). Management fashion. Academy of Management Review, 21(1), 254–285.

Acko<sup>f</sup>, R. L. (1979a). The future of operational research is past. Journal of the Operational Research Society, 30(2), 93–103.

Acko<sup>f</sup>, R. L. (1979b). Resurrecting the future of operational research. Journal of the Operational Research Society, 30(3), 189–199.

Adler, P. S., & Kwon, S.-W. (2002). Social capital: Prospects for a new concept. Academy of Management Review, 27 (1), 17–40.

Akter, S., & Wamba, S. F. (2016). Big data analytics in Ecommerce: A systematic review and agenda for future research. Electronic Markets, 26(2), 173–194.

Allen, D. G., Bryant, P. C., & Vardaman, J. M. (2010). Retaining talent: Replacing misconceptions with evidence-based strategies. Academy of Management Perspectives, 24(2), 48–64.

Anand, A., Sharma, R., & Coltman, T. (2016). Four steps to realizing business value from digital data streams. MIS Quarterly Executive, 15(4), 259–277.

Anderson, C. (2015). Creating a data-driven organization: Practical advice from the trenches. Sebastopol, California: O’Reilly Media.

Andrews, K. R. (1971). The Concept of Corporate Strategy. Homewood, Illinois: Dow Jones-Irwin.

Arizona State University – WP Carey School of Business (2017) MS-BA – Entering class of Fall 2016. Retrieved from https://wpcarey.asu.edu/masters-programs/busi ness-analytics/class-pro<sup>fi</sup>le

Audzeyeva, A., & Hudson, R. (2016). How to get the most from a business intelligence application during the post implementation phase? Deep structure transformation at a U.K. retail bank. European Journal of Information Systems, 25(1), 29–46.

Barajas, J. (2018, June 14) How Trump’s separation policy became what it is today. PBS NewsHour [Television broadcast]. Retrieved from https://www.pbs.org/news hour/nation/how-trumps-family-separation-policy-hasbecome-what-it-is-today

Baskerville, R. L., & Myers, M. D. (2009). Fashion waves in information systems research and practice. MIS Quarterly, 33(4), 647–662.

Bass, F. M. (1969). A new product growth for model consumer durables. Management Science, 15(5), 215–227.

Belkin, D., & Jordan, M. (2016, March 17). Heavy recruitment of Chinese students sows discord on U.S. campuses. The Wall Street Journal, http://www.wsj.com/ articles/heavy-recruitment-of-chinese-students-sows-dis cord-on-u-s-campuses-1458224413

Bell, P. C., & Anderson, C. K. (2002). In search of strategic operations research/management science. Interfaces, 32 (2), 28–40.

Bennett, A. (2016, August 25) Theresa May’s Brexit success depends on curbing immigration. Everything else is a sideshow [The Telegraph]. Retrieved from http://www. telegraph.co.uk/news/2016/08/25/theresa-mays-brexitsuccess-depends-on-curbing-immigration-every/

Bennett, M. (2012, March) Opinion: Is big data just big hype? ComputerWeekly.com. Retrieved from http:/ www.computerweekly.com/news/2240143590/Opinion-Is-big-data-just-big-hype

Beyer, M. E. (2015, October) Has operations research outgrown operations research? OR/MS Today. 18–21.

Bouyssou, D. (2005) Questioning the history of operational research in order to prepare its future [HAL ID: hal-00003924]. Retrieved from https://hal.archives-ouvertes. fr/<sup>fi</sup>le/index/docid/28641/<sup>fi</sup>lename/cahierLamsade196.pdf

Brown, A. A., Hulswit, F. T., & Kettelle, J. D. (1956). A study of sales operations. Operations Research, 4(3), 296–308.

Browne, G. J., & Rogich, M. B. (2001). An empirical investigation of user requirements elicitation: Comparing the e<sup>f</sup>ectiveness of prompting techniques. Journal of Management Information Systems, 17(4), 223–249.

Burns, E. (2016) Data science jobs not as plentiful as all the hype indicates [TechTarget]. Retrieved from http:// searchbusinessanalytics.techtarget.com/opinion/Datascience-jobs-not-as-plentiful-as-all-the-hype-indicates

Burstall, R. M., Leaver, R. A., & Sussams, J. E. (1962). Evaluation of transport costs for alternative factory sites – A case study. Journal of the Operational Research Society, 13(4), 345–354.

Butcher, M. (2017, February 21) UK faces triple whammy from skills shortfall, visa restrictions and Brexit uncertainty [TechCrunch]. Retrieved from https://techcrunch. com/2017/02/21/uk-faces-triple-whammy-from-skillsshortfall-visa-restrictions-and-brexit-uncertainty/

Case Western Reserve University – Weatherhead School of Management. (2017). MSM-Business Analytics class pro-<sup>fi</sup>le. Retrieved from https://weatherhead.case.edu/degrees/ masters/ms-management/business-analytics/pro<sup>fi</sup>le

Chang, R. M., Kau<sup>f</sup>man, R. J., & Kwon, Y. O. (2014). Understanding the paradigm shift to computational social science in the presence of big data. Decision Support Systems, 63, 67–80.

Checkland, P. (2010). Researching real-life: Re<sup>fl</sup>ections on 30 years of action research. Systems Research and Behavioral Science, 27(2), 129–132.

Checkland, P., & Scholes, J. (1990). Soft systems methodology in action. Chichester: Wiley.

Chen, H., Chiang, R. H. L., & Storey, V. S. (2012). Business intelligence and analytics: From Big Data to big impact. MIS Quarterly, 36(4), 1165–1188.

Collcutt, R. (1965). The first twenty years of operational research. London: BISRA.

Committee on the Next Decade in Operations Research. (1988). Operations research: The next decade. Operations Research, 36(4), 619–637.

Corbett, C. J., & Van Wassenhove, L. N. (1993). The natural drift: What happened to operations research? Operations Research, 41(4), 625–640.

Dando, M. R., & Sharp, R. G. (1978). Operational research in the UK in 1977: The causes and consequences of a myth. Journal of the Operational Research Society, 29 (10), 939–949.

Davenport, T. (2014a, June 19) Failure to commit – Beyond the analytical center of excellence. Deloitte University Press. Retrieved from https://dupress.deloitte.com/dupus-en/topics/analytics/failure-commit.html

Davenport, T. H. (2012) Successful business analytics: Part II. Retrieved from https://www.youtube.com/watch?v= 48uY17tD-HI

Davenport, T. H. (2014b, April 30). It’s already time to kil the ‘data scientist’ title. The Wall Street Journal, Retrieved from http://blogs.wsj.com/cio/2014/04/30/itsalready-time-to-kill-the-data-scientist-title/

Davenport, T. H., Harris, J. G., De Long, D. W., & Jacobson, A. L. (2001). Data to knowledge to results: Building an analytic capability. California Management Review, 43(2), 117–138.

Davenport, T. H., Harris, J. G., & Morison, R. (2010). Analytics at work: Smarter decisions, better results. Boston: Harvard Business Press.

Davis, F. D., Bagozzi, R. P., & Warshaw, P. R. (1989). User acceptance of computer technology: A comparison of two models. Management Science, 35(8), 982– 1003.

Davis, J. M. (2013). Leveraging the IT competence of non-IS workers: Social exchange and the good corporate citizen. European Journal of Information Systems, 22(4), 403–415.

Davis, J. M., Kettinger, W. J., & Kunev, D. G. (2009). When users are IT experts too: The e<sup>f</sup>ects of joint IT competence and partnership on satisfaction with enterpriselevel systems implementation. European Journal of Information Systems, 18(1), 26–37.

Deloitte. (2013, July 31). Analytics oversight: Who’s in charge here? [CIO Journal/Wall Street Journal]. Retrieved from http://deloitte.wsj.com/cio/2013/07/31/analytics-over sight-whos-in-charge-here/. Statement from WSJ Web site: “CONTENT FROM OUR SPONSOR. Please note: The Wall Street Journal News Department was not involved in the creation of the content below”.

Dennis, A. R., Wixom, B. H., & Vandenberg, R. J. (2001). Understanding <sup>fi</sup>t and appropriation e<sup>f</sup>ects in group support systems via meta-analysis. MIS Quarterly, 25 (2), 167–193.

DeSanctis, G., & Poole, M. S. (1994). Capturing the complexity in advanced technology use: Adaptive structuration theory. Organization Science, 5(2), 121–147.

Droege, S. B., & Hoobler, J. M. (2003). Employee turnover and tacit knowledge di<sup>f</sup>usion: A network perspective. Journal of Managerial Issues, 15(1), 50–64.

Duke University – Fuqua School of Business. (2017) MQM: Class pro<sup>fi</sup>le – Master of Quantitative Management. Retrieved from https://www.fuqua.duke.edu/programs master-quantitative-management/class-pro<sup>fi</sup>le

Eilon, S. (1980). The role of management science. Journal of the Operational Research Society, 31(1), 17–28.

Eisenberger, R., Fasolo, P., & Davis-Lamastro, V. (1990). Perceived organizational support and employee diligence, commitment, and innovation. Journal of Applied Psychology, 75(1), 51–59.

Eisenberger, R., Huntington, R., Hutchinson, S., & Sowa, D. (1986). Perceived organizational support. Journal of Applied Psychology, 71(3), 500–507.

Eisenhardt, K. M., Kaywajy, J. L., & Bourgeois III, L. J. (1997). How management teams can have a good <sup>fi</sup>ght. Harvard Business Review, 75(4), 77–85.

Evans, J. R. (2012). Business analytics: The next frontier for decision sciences. Decision Line, 43, 4–6.

Fabian, T., Fisher, J. L., Sasieni, M. W., & Yardeni, A. (1959). Purchasing raw material on a <sup>fl</sup>uctuating market. Operations Research, 7(1), 107–122.

Fildes, R., & Ranyard, J. C. (1997). Success and survival of operational research groups – A review. Journal of the Operational Research Society, 48(4), 336–360.

Fildes, R., Ranyard, J. C., & Crymble, W. R. (1999). The management of OR groups: Results of a survey. Journal of the Operational Research Society, 50(6), 563–580.

Fosso Wamba, S., Akter, S., & De Bourmont, M. 2018. Quality dominant logic in big data analytics and <sup>fi</sup>rm performance. Business Process Management Journal, doi:10.1108/BPMJ-08-2017-0218

Galer, G. S. (1959). The use of computers for economic planning in the petroleum chemical industry. The Computer Journal, 2(3), 145–150.

Geo<sup>f</sup>rion, A. M. (1992). Forces, trends, and opportunities in MS/OR. Operations Research, 40(3), 423–445.

Goodhue, D. L. (1995). Understanding user evaluations of information systems. Management Science, 41(12), 1827–1844.

Goodhue, D. L., & Thompson, R. L. (1995). Task-technology <sup>fi</sup>t and individual performance. MIS Quarterly, 19 (2), 213–236.

Gri<sup>f</sup>eth, R. W., Gaertner, S., & Sager, J. K. (1999). Taxonomic model of withdrawal behaviors: The

adaptive response model. Human Resource Management Review, 9(4), 557–590.

Grossman, T. A. (2001). Causes of the decline of the business school management science course. INFORMS Transactions on Education, 1(2), 51–61.

Harris, C. M. (1992). OR Forum – Computers and operations research: A marriage for growth. Operations Research, 40(6), 1031–1039.

Harris, J., Craig, E., & Egan, H. (2010b). How successful organizations strategically manage their analytic talent. Strategy & Leadership, 38(3), 15–22.

Harris, J. G., Craig, E., & Egan, H. (2010a, January/February) Executive decisions: How to organize your analytical talent. Analytics. 15–21. Retrieved from http://analytics-magazine. org/executive-decisions-how-to-organize-your-analyticaltalent/

Hazen, B. T., Skipper, J. B., Boone, C. A., & Hill, R. R. (2016). Back in business: Operations research in support of big data analytics for operations and supply chain management. Annals of Operations Research, 1–11. doi:10.1007/s10479-016-2226-0

Hirschheim, R., Murungi, D. M., & Peña, S. (2012). Witty invention or dubious fad? Using argument mapping to examine the contours of management fashion. Information and Organization, 22(1), 60–84.

Hofer, C. W., & Schendel, D. (1978). Strategy formulation: Analytical concepts. St. Paul, MN.: West Publishing.

Hofmann, M., & Tierney, B. (2003) The involvement of human resources in large scale data mining projects. ISICT ’03 Proceedings of the 1st International Symposium on Information and Communication Technologies, Dublin, September 24–26, 103–109. 2017, September 22 Retrieved from http://dl.acm.org/ citation.cfm?id=963622

Hofmann, M., & Tierney, B. (2009) An enhanced data mining life cycle. IEEE Symposium on Computational Intelligence and Data Mining, Nashville, TN, March 30 – April 2, 109– 117. 2017, September 22 Retrieved from http://ieeexplore. ieee.org/stamp/stamp.jsp?arnumber=4938637

Holsapple, C., Lee-Post, A., & Pakath, R. (2014). A uni<sup>fi</sup>ed foundation for business analytics. Decision Support Systems, 64, 130–141.

Huber, G. P. (1990). A theory of the e<sup>f</sup>ects of advanced information technologies on organizational design, intelligence, and decision making. Academy of Management Review, 15(1), 47–71.

IFORS. (2018). History. International Federation of Operational Research Societies. 2018, December 1 Retrieved from http://ifors.org/history/

Institute for International Education. (2016). Open Doors 2016: Report on international education exchange. Retrieved from https://p.widencdn.net/p8fxny/Open-Doors-2016-Presentation

Jain, P. (2013, February 15) To centralize analytics or not, that is the question [Forbes]. Retrieved from https:// www.forbes.com/sites/piyankajain/2013/02/15/to-centra lize-analytics-or-not/#3ca27bed18e7

Johnson, W. T. M. (1955). Letters to the Editor: Why operations research? Operations Research, 3(1), 103–104.

Kay, E., & Duckworth, E. (1957). Linear programming in practice. Journal of the Royal Statistical Society. Series C (Applied Statistics), 6(1), 26–39.

Kendall, M. (2017) Trump poised to overhaul H-1B visas relied on by Silicon Valley tech [The Mercury News (30 January, updated 1 February)]. Retrieved from http:// www.mercurynews.com/2017/01/30/trump-poised-tooverhaul-work-visas-relied-on-by-silicon-valley-tech

Kirby, M. W. (2000). Operations research trajectories: The Anglo-American experience from the 1940s to the 1990s. Operations Research, 48(5), 661–670.

Kirby, M. W. (2007). Paradigm change in operations research: Thirty years of debate. Operations Research, 55(1), 1–13.

Kirkwood, C. W. (1990). Does operations research address strategy? Operations Research, 38(5), 747–751.

Klatt, T., Schlaefke, M., & Moeller, K. (2011). Integrating business analytics into strategic planning for better performance. Journal of Business Strategy, 32(6), 30–39.

Kocharekar, R. (2004). An IT architecture for nimble organizations: Managing access from cyberspace. Information Systems Management, 21(2), 22–30.

Larnder, H. (1984). OR Forum – The origin of operational research. Operations Research, 32(2), 465–476.

Lau, R. Y. K., Liao, S. S. Y., Wong, K. F., & Chiu, D. K. W. (2012). Web 2.0 environmental scanning and adaptive decision support for business mergers and acquisitions. MIS Quarterly, 36(4), 1239–1268.

Ledington, P., & Donaldson, J. (1997). Soft OR and management practice: A study of the adoption and use of soft systems methodology. Journal of the Operational Research Society, 48(3), 229–240.

Liberatore, M., & Luo, W. (2011). INFORMS and the analytics movement: The view of the membership. Interfaces, 41(6), 578–589.

Liberatore, M. J., & Luo, W. (2010). The analytics movement: Implications for operations research. Interfaces, 40 (4), 313–324.

Little, J. D. C. (1991). Operations research in industry: New opportunities in a changing world. Operations Research, 39(4), 531–542.

Magee, J. F. (1953). The e<sup>f</sup>ect of promotional e<sup>f</sup>ort on sales. Journal of the Operations Research Society of America, 1(2), 64–74.

Manning, S., Massini, S., & Lewin, A. Y. (2008). A dynamic perspective on next-generation o<sup>f</sup>shoring: The global sourcing of science and engineering talent. Academy of Management Perspectives, 22(3), 35–54.

Manyika, J., Chui, M., Brown, B., Bughin, J., Dobbs, R., Roxburgh, C., & Hung Byers, A. (2011, May) Big data: The next frontier for innovation, competition, and productivity. Retrieved from http://www.mckinsey.com/busi ness-functions/digital-mckinsey/our-insights/big-datathe-next-frontier-for-innovation

Marchand, D. A., & Peppard, J. (2013). Why IT fumbles analytics. Harvard Business Review, 91(1/2), 104–112.

Massachusetts Institute of Technology – Alfred P. Sloan School of Management. (2017). Master of business analytics. Retrieved from http://mitsloan.mit.edu/master-ofbusiness-analytics/admissions

McAfee, A., & Brynjolfsson, E. (2012). Big Data: The management revolution. Harvard Business Review, 90(10), 60–68.

McClelland, W. G. (1975). Mathematics in management— How it looks to the manager. OMEGA the International Journal of Management Science, 3(2), 147–155.

Meredith, J. R. (2001). Reconsidering the philosophical basis of OR/MS. Operations Research, 49(3), 325–333.

MSR. (1986). Problems and Opportunities Facing MS/OR: A Report Prepared for TIMS Council (March 28). Management Science Roundtable, The Institute of Management Sciences.

Müller, O., Junglas, I., vom Brocke, J., & Debortoli, S. (2016). Utilizing big data analytics for information systems research: Challenges, promises and guidelines. European Journal of Information Systems, 25(4), 289–302.

North Carolina State University – Institute for Advanced Analytics. (2017). Master of science in analytics student pro<sup>fi</sup>le, class of 2018. Retrieved from http://analytics. ncsu.edu/?page\_id=2807andhttp://analytics.ncsu.edu/ reports/admission/MSA2018.pdf

O'Brien, S. A. (2017, February 6) Tech industry braces for Trump’s visa reform. CNN Tech. Retrieved from http:// money.cnn.com/2017/02/05/technology/trump-h1bvisas-executive-order/

O’Reilly III, C., & Chatam, J. (1986). Organizational commitment and psychological attachment: The e<sup>f</sup>ects of compliance, identi<sup>fi</sup>cation, and internalization on prosocial behavior. Journal of Applied Psychology, 71(3), 492–499.

Olavsrud, T. (2016, November 2) Executives still mistrust insights from data and analytics. CIO. Retrieved from http://www.cio.com/article/3138049/analytics/execu tives-still-mistrust-insights-from-data-and-analytics. html?idg\_eid=4603159ab53ea7e8a<sup>f</sup>a814fba81ac31&to ken=%23tk.CIONLE\_nlt\_cio\_insider\_2016-11-04&utm\_ source=Sailthru&utm\_medium=email&utm\_campaign= CIO%20Daily%202016-11-04&utm\_term=cio\_insi der#tk.CIO\_nlt\_cio\_insider\_2016-11-04

Ormerod, R. (1995). Putting soft OR methods to work: Information systems strategy development at Sainsbury’s. Journal of the Operational Research Society, 46(3), 277–293.

Ormerod, R. J. (1996). Information systems strategy development at Sainsbury’s Supermarkets using ‘soft’ OR. Interfaces, 26(1), 102–130.

Parker, H. (1976). Free enterprise and the wealth of nations: Blackett memorial lecture 1976. Operational Research Quarterly, 27(2, Part 2), 423–424.

Peppard, J. (2007). The conundrum of IT management. European Journal of Information Systems, 16(4), 336–345.

Porter, M. E. (1985). Competitive advantage: Creating and sustaining superior performance. New York: The Free Press.

Powers, R. (2010). Retrospective: 25 years applying management science to logistics. In M.-M. S. Sodhi & C. S. Tang (Eds.), A long view of research and practice in operations research and management science (pp. 89– 98). New York: Springer.

Pruzan, P. (1988). Systemic OR and operational systems science. European Journal of Operational Research, 37(1), 34–41.

Putnam, R. D. (2000). Bowling alone: The collapse and revival of American community. New York: Simon & Schuster.

Radnor, M., & Neal, R. D. (1973). The progress of management-science activities in large US industrial corporations. Operations Research, 21(2), 427–450.

Radnor, M., Rubenstein, A. H., & Bean, A. S. (1968). Integration and utilization of management science activities in organizations. Operational Research Quarterly, 19 (2), 117–141.

Ransbotham, S., Kiron, D., & Kirk Prentice, P. (2016) Beyond the hype: The hard work behind analytics success. MIT Sloan Management Review, Global Executive Study and Research Project (Spring). Reprint #57381. Retrieved from http://sloanreview.mit.edu/projects/thehard-work-behind-data-analytics-strategy/

Reisman, A., & Kirschnick, F. (1994). The devolution of OR/MS: Implications from a statistical content analysis of papers in <sup>fl</sup>agship journals. Operations Research, 42 (4), 577–588.

Richey, J. R. R. G., Morgan, T. R., Lindsey-Hall, K., & Adams, F. G. (2016) A global exploration of Big Data in the supply chain. International Journal of Physical Distribution &

Logistics Management. Retrieved from http://www.emeral dinsight.com/doi/pdfplus/10.1108/IJPDLM-05-2016-0134

Rivers, M. (2017). Tech workers <sup>fl</sup>ee US, blame Trump. CNN.com. Retrieved from http://www.cnn.com/videos/ world/2017/12/03/tech-reverse-migration-rivers-pkg.cnn

Rogers, E. M. (1995). Difusion of Innovations (4th ed.). New York: The Free Press.

Rosenhead, J., & Mitchell, G. H. (1986). Report of the commission on the future practice of operational research. Journal of the Operational Research Society, 37(9), 829–889.

Saldanha, T. J. V., Mithas, S., & Krishnan, M. S. (2017). Leveraging customer involvement for fueling innovation: The role of relational and analytical information processing capabilities. MIS Quarterly, 41(1), 267–286.

SAS. (2018). Big Data: What it is and why it matters. Retrieved from https://www.sas.com/en\_us/insights/bigdata/what-is-big-data.html

Saul, S. (2018, January 2) As <sup>fl</sup>ow of foreign students wanes, U.S. universities feel the sting. The New York Times. Retrieved from https://www.nytimes.com/2018 01/02/us/international-enrollment-drop.html

Schultz, A. (2016, February 12) Surge of Chinese students studying abroad could ebb [Barron’s]. Retrieved from http://www.barrons.com/articles/surge-of-chinese-stu dents-studying-abroad-could-ebb-1455254077

Sharma, R., Mithas, S., & Kankanhalli, A. (2014). Transforming decision-making processes: A research agenda for understanding the impact of business analy tics on organizations. European Journal of Information Systems, 23(4), 433–441.

Siddiq, H. (2013, November 18) More Chinese students want a US education, but fewer stay for a job [South China Morning Post]. Retrieved from http://www.scmp. com/comment/insight-opinion/article/1356828/morechinese-students-want-us-education-fewer-stay-job

Simon, H. A., Dantzig, G. B., Hogarth, R., Plott, C. R., Rai<sup>f</sup>a, H., Schelling, T. C., . . . Winter, S. (1987). Decision making and problem solving. Interfaces, 17(5), 11–31.

Smith, G. F. (1988). Towards a heuristic theory of problem structuring. Management Science, 34(12), 1489–1506.

Sodhi, -M.-M. S., & Tang, C. S. (2010). Conclusion: A long view of research and practice in operations research and management science. In M.-M. S. Sodhi & C. S. Tang (Eds.), A long view of research and practice in operations research and management science (pp. 275–297). New York: Springer.

Staheli, R. (2016) Healthcare reporting: Centralized vs. decentralized. HealthCatalyst. Retrieved from https:// www.healthcatalyst.com/healthcare-reporting-centra lized-vs-decentralized

Staples, D. S., Wong, I., & Seddon, P. B. (2002). Having expectations of information systems bene<sup>fi</sup>ts that match received bene<sup>fi</sup>ts: Does it really matter? Information & Management, 40(2), 115–131.

Stein, S. (2016, June 12) Donald Trump and Paul Ryan at odds over a key part of immigration policy [The Hu<sup>fi</sup>ngton Post]. Retrieved from http://www.hu<sup>fi</sup>ngton p o s t . c o m / e n t r y / d o n a l d - t r u m p - p a u l - r y a n \_ u s \_ 575d5e49e4b0ced23ca84690

Tambo, T., Gabel, O. D., Olsen, M., & Bækgård, L. (2012) Organisational dynamics and ambiguity of business intelligence in context of enterprise information systems—A case study. CONFENIS. 2018, September 26 Retrieved from http://pure.au.dk/portal/<sup>fi</sup>les/52355924/BI\_EIS\_15.pdf

Terdoslavitch, W. (2016, January 12) Big data moves from hype to reality, CompTIA <sup>fi</sup>nds [InformationWeek]. Retrieved from http://www.informationweek.com/bigdata/big-data-analytics/big-data-moves-from-hype-toreality-comptia-<sup>fi</sup>nds-/d/d-id/1323816

Tomlinson, R. C., & Kiss, I. (1984). Rethinking the process of operational research and systems analysis. Oxford, England: Pergamon.

Topan, T. (2017, February 21). Trump admin sets stage for mass deportations. [CNN Politics]. Retrieved from http://www.cnn.com/2017/02/21/politics/dhs-immigra tion-guidance-detentions/index.html

University of California, San Diego – Rady School of Management. (2017). M.S. in business analytics: Class pro<sup>fi</sup>le. Retrieved from http://rady.ucsd.edu/programs/ masters-programs/ms-in-business-analytics/pro<sup>fi</sup>le/

University of Minnesota – Carlson School of Management. (2017). Master of science in business analytics. Retrieved from https://carlsonschool.umn.edu/degrees/masterscience-in-business-analytics/admissions

University of Southern California – Marshall School of Business. (2017). MS. business analytics: Class pro<sup>fi</sup>les 2014-2016. Retrieved from https://www.marshall.usc. edu/programs/specialized-masters-programs/masterscience-business-analytics/faq

University of Texas, Austin – McCombs School of Business. (2017). MSBA (Master of science in business analytics): Texas MSBA 2017 admitted class pro<sup>fi</sup>le. Retrieved from https://www.mccombs.utexas. edu/Master-of-Science-in-Business-Analytics/Class-Pro<sup>fi</sup>le

University of Texas, Dallas – Jindal School of Management. (2017). Master of Science in Business Analytics/MS in business analytics student pro<sup>fi</sup>le as of Fall 2017. Retrieved from http://jindal.utdallas.edu/isom/informa tion-systems-programs/ms-business-analytics/#03-stu dent-pro<sup>fi</sup>les-and-employment

Vardaman, J. M., Allen, D. G., Otondo, R. F., Hancock, J. I., Shore, L. M., & Rogers, B. L. (2016). Social comparisons and organizational support: Implications for commitment and retention. Human Relations, 69(7), 1483–1505.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a uni<sup>fi</sup>ed view. MIS Quarterly, 27(3), 425–478.

Voutsina, K., Mourmant, G., & Niederman, F. (2014). The range of shocks prompting entrepreneurial employee turnover through the lenses of exploration and exploitation framework. In U. Stettner, B. S. Aharonson, & T. L. Amburgey (Eds.), Exploration and exploitation in early stage ventures and SMEs (Technology, Innovation, Entrepreneurship and Competitive Strategy, Volume 14) (pp. 39–66). Bingley, UK: Emerald Group Publishing Limited.

Wagner, H. M., Rothkopf, M. H., Thomas, C. J., & Miser, H. J. (1989). The next decade in operations research: Comments on the CONDOR report. Operations Research, 37(4), 664–672.

Waid, C., Clark, D. F., & Acko<sup>f</sup>, R. L. (1956). Allocation of sales e<sup>f</sup>ort in the lamp division of the General Electric Company. Operations Research, 4(6), 629–647.

White, J. (1991). An existence theorem for OR/MS. Operations Research, 39(2), 183–193.

## Appendix A

The rise and fall of OR/MS: A warning for business analytics?

OR/MS history has often been divided into several time periods, including a “golden age” between the 1940s and 1960s followed by a “crisis” and subsequent decline beginning in the late 1960s (e.g., Kirby, 2007, p. 1). While not universally accepted (e.g., Bouyssou, 2005), these periods provide a useful framework for understanding how OR/MS history can provide clues about possible troubles for BA.

## The golden age of OR/MS: Post World War II success

Operations research (OR) arose in response to the need to protect Great Britain from air attacks in World War II (Larnder, 1984). Two particularly important tasks for OR scientists during that time were to observe and study infor mation <sup>fl</sup>ows from radar units and the Royal Observer Corps to Fighter Group operations rooms, and to develop techniques to control British <sup>fi</sup>ghter aircraft against German bombers (Larnder, 1984). Examples of control techniques include ways to “enable [British <sup>fi</sup>ghters] to economize their e<sup>f</sup>orts and attain tactical advantage (use of sun and altitude) in positioning themselves relative to the attacking force” (Larnder, 1984, p. 474).

These control techniques were applied to analogous peacetime uses after WWII (e.g., “logistics, manufacturing, supply chains and risk analysis”; Beyer, 2015, p. 18). The 1940s through the late 1960s were a golden era for operations research theory and application, both within and outside of the military. For example, Royal Dutch Shell used linear programmes at a petroleum chemical plant to show how “marginal pro<sup>fi</sup>t could be substantially increased by a reframing of marketing plans” (Galer, 1959, p. 147). Glacier Metal Company was able to increase their use of recovered metals by 4% via linear programming (Kay & Duckworth, 1957). Other case studies of sales operations (Brown et al., 1956; Magee, 1953; Waid et al., 1956), transport costs for alternative factory sites (Burstall, Leaver, & Sussams, 1962), and purchasing raw materials in a <sup>fl</sup>uctuating market (Fabian, Fisher, Sasieni, & Yardeni, 1959) are just a few examples of successful industrial applications of OR/MS techniques.

Based on several articles of that time (e.g., Johnson, 1955; Galer, 1959; Radnor, Rubenstein, & Bean, 1968), Fildes and Ranyard (1997) later concluded that “In the early years of its establishment in industry, OR was seen as o<sup>f</sup>ering a ‘competitive edge’ that organizations could only neglect at their peril” and cited Peter Drucker’s opinion that management science could contribute to successful management (p. 338). The 1950s through 1970s was also the time when many universities founded OR/MS programmes (Beyer, 2015).

A time of crisis and decline: The late 1960s to early 1990s In spite of its promising start in the post-World War II era, OR/MS ran into di<sup>fi</sup>culties in the late 1960s and 1970s. Even Peter Drucker noted in 1974 that OR/MS was “already a disappointment” (Fildes & Ranyard, 1997, p. 346). Part of that failure was attributed to OR’s restricted use. Roger Collcutt, head of OR at the British Iron and Steel Research Association (BISRA), admitted “many managements remain sceptical whether they can obtain any bene<sup>fi</sup>t from [OR] application to their problems” (Collcutt, 1965, p. 5). Dando and Sharp (1978) described the con<sup>fl</sup>icted opinions of OR/MS practitioners, who admitted to them privately that “[practitioners] talk in public” about mathematics and models but “privately they acknowledge the normal inadequancy [sic] of data, the irrelevance of sophisticated mathematics and the transcendent importance of style and communication” (p. 942).

Other problems stemmed from a lack of organisational support. Kirby (2000) noted that “early British industrial OR was very restricted in its sector coverage and wholly dependent upon high-level personal advocacy rather than being the product of any broadly based and enthusiastic wish to embrace OR” (p. 664). Organisational support, when it existed, largely drove OR/MS towards tactical problems (Eilon, 1980), leaving strategic problems for other departments (Dando & Sharp, 1978). This reality contrasted with the “admirable aspirations” expressed by OR professionals about the way they closely interwove tactics and strategy (Fildes & Ranyard, 1997, p. 342).

In addition, OR/MS practitioners were often criticised for excessive technique-orientation and over-reliance on mathematical models (Acko<sup>f</sup>, 1979a, 1979b; Eilon, 1980; Geo<sup>f</sup>rion, 1992; Grossman, 2001; Kirby, 2000; Meredith, 2001; Wagner et al., 1989). This high degree of technical specialisation caused many managers to ignore OR/MS because they felt OR/MS practitioners could not successfully apply their mathematical knowledge to organisationa problems, especially “messy” interrelated business-context problems (Acko<sup>f</sup>, 1979a; McClelland, 1975). For example, British Petroleum’s experience in the 1967 Arab-Israeli war eroded its con<sup>fi</sup>dence in linear programming and computer simulations for planning global operations and led to a more pragmatic management style (Kirby, 2000). As Geo<sup>f</sup>rion (1992) wryly observed, “rigor mania can lead to rigor mortis when relevance is neglected” (p. 429).

Such perceptions led OR/MS clients – typically managers from other organisational units – to become apathetic or even hostile to OR/MS (Eilon, 1980; Geo<sup>f</sup>rion, 1992; Meredith, 2001). Consequently, many organisations failed to establish OR/MS departments, often because such groups were not started in the <sup>fi</sup>rst place, or if they were, they were broken up and dispersed throughout the organisation for cost-saving purposes (Fildes & Ranyard, 1997; Geo<sup>f</sup>rion, 1992; Radnor & Neal, 1973). Critics also found fault with university research and degree programmes that were focused overwhelmingly on theory rather than practice (Acko<sup>f</sup>, 1979b; Corbett & Van Wassenhove, 1993; Dando & Sharp, 1978; Meredith, 2001; Reisman & Kirschnick, 1994). OR/MS also had increasing competition from other organisational units with expertise in statistics, economics, and organisational design (Fildes & Ranyard, 1997).

While many of these criticisms were aired in published research, perhaps the most telling comments can be found in Hugh Parker’s (1976) Blackett Memorial Lecture (sponsored by The Operational Research Society in memory of Nobel Prize winner Patrick, Lord Blackwell, a pioneer of OR in WWII):

Our failure, in my opinion, has been our tendency to rely too much on rational methods, quantitative methods if you will, in addressing the increasing complex and urgent problems of management. We have tended to ignore or deny the things we could not measure, and to cling, almost as an act of blind faith, to the rational, hardheaded, scientific approaches epitomized in the increasingly sophisticated techniques of the so called “managerial sciences”. . .We managers believed, because we wanted to believe, that rigorous scientific analysis, based on objective data and all available information, must yield the “right” answers and thus enable us to solve the problems. But more often than I care to think about, the event proved us wrong. The answers we got failed to solve the problem – not necessarily because they were wrong, but simply because they were often incomplete, or sometimes quite irrelevant. They missed some key element of the problem we were trying to solve. (Eilon, 1980, p. 19)

Unfortunately, the OR/MS community was slow to respond to such criticisms. “By 1979”, noted Fildes and Ranyard (1997), “OR was in its death throes” (p. 341). Academia, an important part of the OR/MS community, shared in this slow response. Geo<sup>f</sup>rion (1992) observed that academia became “largely decoupled from the economic fortunes of its practitioner constituency” so that the fruit of its labours “appears to many to lack relevance” (p. 429). If all this were not enough, another serious blow was delivered in 1991 by the American Association of Collegiate Schools of Business when it removed management science from the MBA common body of knowledge (Grossman, 2001).

## After the storm

While the previous examples portended a dismal future for OR/MS, there is contradictory evidence in the OR/ MS literature arguing for more optimistic prospects. The CONDOR (1988) report, for example, claimed that <sup>fi</sup>rms “will recognize that OR can genuinely assist management in making decisions” by helping managers “preclude undesirable outcomes, exercise control, and exploit opportunities” (p. 620). Despite the number of articles in the 1970s to 1990s lamenting the imminent demise of OR/MS, “over a million copies of linear and nonlinear optimization code, modi<sup>fi</sup>ed to work with the leading spreadsheet packages”, was shipped by the end of 1991 (Corbett & Van Wassenhove, 1993, p. 626; Geo<sup>f</sup>rion, 1992). There was also an unexpected relationship between decentralisation and the OR/MS job market. In spite of increased decentralisation, Geo<sup>f</sup>rion (1992) exclaimed that the Bureau of Labor Statistics reported in 1990 that the operations research analyst position was “the 10<sup>th</sup> fastest growing among all occupations in the 1990s! Faster than accounting, computer programming, engineering, <sup>fi</sup>nancial management, health services management, management consulting, medicine, and more than 300 other occupations” (p. 432).

In a similar way, it is hoped that leveraging the history of OR/MS can help us lay the foundations for a more optimistic future for business analytics.

## Appendix B

Table B-1. Research questions from Sharma et al. (2014).

<table><tr><td>RQ #a</td><td>Research Question</td></tr><tr><td>1</td><td>&quot;How does the use of business analytics influence organisational decision-making processes?&quot; (p. 434)</td></tr><tr><td>2</td><td>&quot;How is the use of business analytics influenced by organisational decision-making processes?&quot; (p. 434)</td></tr><tr><td>3</td><td>&quot;What are the joint effects of the use of business analytics and organisational decision-making processes on organisational performance?&quot; (p. 435)</td></tr><tr><td>4</td><td>&quot;How do existing organisational structures, routines and decision-making processes influence the ability of managers and analysts to generate insights from data?&quot; (p. 435)</td></tr><tr><td>5</td><td>&quot;How can human sense making and machine learning work together to improve the generation of insights from the use of business analytics?&quot; (p. 436)</td></tr><tr><td>6</td><td>&quot;How do the structures and processes of decision making influence the ability of insight generation teams to generate insights from the use of business analytics?&quot; (p. 436)</td></tr><tr><td>7</td><td>&quot;How do organisational decision-making processes influence the conversion of business analytics-based insights into good decisions? (p. 437)</td></tr><tr><td>8</td><td>&quot;Can organisations use business analytics to compensate for the limitations of managerial and organisational decision-making processes that have their roots in satisficing behaviour, cognitive limitations and structures of social capital and, if so, how? (p. 437)</td></tr><tr><td>9</td><td>&quot;How do decision-making processes influence the successful implementation of decisions arising out of the use of business analytics?&quot; (p. 438)</td></tr><tr><td>10</td><td>&quot;How can business analytics be used to improve the acceptance of decisions?&quot; (p. 438)</td></tr><tr><td>11</td><td>&quot;How can business analytics be used to improve an organisation&#x27;s asset orchestration capability?&quot; (p. 438)</td></tr><tr><td>12</td><td>&quot;How do governance structures evolve as a result of increasing penetration of business analytics?&quot; (p. 438)</td></tr><tr><td>13</td><td>&quot;What governance structures are more effective in capturing value from business analytics-supported strategic decision making?&quot; (p. 438)</td></tr><tr><td>14</td><td>&quot;How can business analytics be used to reduce the outcome uncertainty associated with strategic decisions?&quot; (p. 438)</td></tr></table>

<sup>a</sup>Research Question Numbers are used in the main text to reference these questions.

Table B-2. Research questions adapted from Sharma et al. (2014) with corresponding propositions.

<table><tr><td> $RQ^{\#}^{a}$ </td><td>Adapted Research Question</td><td> $P^{\#}^{b}$ </td><td>Proposition</td></tr><tr><td colspan="4">Research propositions regarding decentralisation of BA practitioners</td></tr><tr><td rowspan="5">4</td><td rowspan="5">&quot;How do existing organisational structures, routines and decision-making processes influence the ability of managers and analysts to generate insights from data?&quot;</td><td>1</td><td>BA practitioner isolation is inversely associated with the ability of BA practitioners to generate insights from data.</td></tr><tr><td>2a</td><td>BA practitioner isolation is inversely associated with the use of group support systems when there is a task-technology fit.</td></tr><tr><td>2b</td><td>BA practitioner isolation is inversely associated with the use of group support systems when that technology is faithfully appropriated by BA practitioners.</td></tr><tr><td>3a</td><td>The agility of the BA human resource allocation process has a positive moderating effect on the relationship between platform maturity and the ability to generate insights from data.</td></tr><tr><td>3b</td><td>The agility of the BA human resource allocation process has a positive moderating effect on the relationship between data driven top management commitment and the ability to generate insights from data.</td></tr><tr><td colspan="4">Research propositions regarding human resource management in business analytics</td></tr><tr><td rowspan="2"> $8^c$ </td><td rowspan="2">Can organisations grow and leverage social capital structures to improve the use of business analytics and, if so, how?</td><td>4</td><td>Bridging social capital between BA practitioners in separate hiring units is inversely associated with BA practitioner isolation.</td></tr><tr><td>5</td><td>Bridging social capital between BA practitioners in separate hiring units is positively associated with the ability of BA practitioners to generate insights from data.</td></tr><tr><td rowspan="5">4</td><td rowspan="5">&quot;How do existing organisational structures, routines and decision-making processes influence the ability of managers and analysts to generate insights from data?&quot;</td><td>6a</td><td>Increased competition for business analytics practitioners will result in greater numbers of under-trained people using business analytics tools.</td></tr><tr><td>6b</td><td>The number of under-trained people using business analytics tools is inversely related to the ability of managers and analysts to generate insights from data.</td></tr><tr><td>7a</td><td>BA practitioner turnover is inversely related to the ability of managers and analysts to generate insights from data.</td></tr><tr><td>7b</td><td>BA practitioner engagement is inversely related to BA practitioner turnover.</td></tr><tr><td>7c</td><td>BA practitioner perceptions of organisational support are inversely related to BA practitioner turnover.</td></tr><tr><td colspan="4">Research propositions regarding management apathy towards business analytics</td></tr><tr><td> $1^c$ </td><td>How do the characteristics and perceptions of business analytics clients influence the use of business analytics in organisational decision-making processes?</td><td>8</td><td>Client employee type moderates the relationship between the client&#x27;s negative perceived net benefit of BA and their related BA behavioural outcomes.</td></tr><tr><td colspan="4">Research propositions regarding the use of BA insights to guide strategy</td></tr><tr><td rowspan="6"> $4^c$ ,  $6^c$ </td><td>How do existing organisational learning, knowledge sharing, and problem-solving processes influence the ability of managers and analysts to generate strategic insights from data?</td><td>9</td><td>BA practitioners who use a &quot;soft&quot; systems methodology to address strategy-related BA problems will generate more strategic insights than those who do not.</td></tr><tr><td rowspan="5">How do the structures and processes of organisational learning, knowledge sharing, and problem solving influence the ability of insight generation teams to generate strategic insights from the use of business analytics?</td><td>10a</td><td>BA practitioner isolation is inversely associated with BA practitioner interdisciplinarity.</td></tr><tr><td>10b</td><td>BA practitioner interdisciplinarity will be positively associated with the generation of strategic insights from data.</td></tr><tr><td> $C1^d$ </td><td>BA practitioner isolation is inversely associated with the ability of BA practitioners to generate strategic insights from data.</td></tr><tr><td>11</td><td>Strategy hierarchy level will negatively moderate the relationship between BA practitioner interdisciplinarity and that practitioner&#x27;s ability to generate strategic insights from data.</td></tr><tr><td>12</td><td>Strategy hierarchy level will negatively moderate the relationship between BA practitioner isolation and that practitioner&#x27;s ability to generate strategic insights from data.</td></tr></table>

## Appendix C

Table C-1. Employee type (from Gri<sup>f</sup>eth et al., 1999).

<table><tr><td>Employee Type</td><td>Description</td><td>Job Involvement</td><td>Commitment to Organisation</td></tr><tr><td>Institutionalised star</td><td>“[O]ften used...as a role model for other employees”; a “water walker” (p. 580).</td><td>High</td><td>High</td></tr><tr><td>Citizen</td><td>“[C]itizens perform, often, without solicitation, tasks that benefit the organization, perhaps more than the citizens themselves do” (p. 581).</td><td>Low</td><td>High</td></tr><tr><td>Lone wolf</td><td>“[C]osmopolitan...They achieve for the sake of achieving for themselves and for their profession, not solely for the organization” (p. 581).</td><td>High</td><td>Low</td></tr><tr><td>Apathetic</td><td>“[A]pathetic employees are more prone to practice calculative behavior, exerting the minimal effort necessary to maintain membership” (p. 581).</td><td>Low</td><td>Low</td></tr></table>
