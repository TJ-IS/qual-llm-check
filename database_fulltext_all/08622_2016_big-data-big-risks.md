---
otero_id: 8622
otero_key: "TB6M6JUZ"
title: "Big data, big risks"
authors: "Roger Clarke"
year: "2016"
journal: "Information Systems Journal"
doi: "10.1111/isj.12088"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Big data, big risks

Roger Clarke

Xamax Consultancy Pty Ltd, Canberra, Australia, email: Roger.Clarke@xamax.com.au Research School of Computer Science, ANU, Canberra, Australia, and UNSW Law, Sydney, Australia

Abstract. The ‘big data’ literature, academic as well as professional, has a very strong focus on opportunities. Far less attention has been paid to the threats that arise from repurposing data, consolidating data from multiple sources, applying analytical tools to the resulting collections, drawing inferences, and acting on them. On the basis of a review of quality factors in ‘big data’ and ‘big data analytics’, illustrated by means of scenario analysis, this paper draws attention to the moral and legal responsibility of computing researchers and professionals to tempe their excitement, and apply reality checks to their promotional activities.

Keywords: data quality, decision quality, impact assessment, scenario analysis

## INTRODUCTION

As sensor technologies mature and as individuals are encouraged to contribute data into organizations’ databases, more transactions are being captured than ever before. Meanwhile, improvements in data-storage technologies have resulted in the cost of evaluating, selecting and destroying old data being now considerably higher than that of simply letting it accumulate. The glu of stored data has greatly increased the opportunities for data to be inter-related, and analysed. The moderate enthusiasm engendered by ‘data warehousing’ and ‘data mining’ in the 1990s has been replaced by unbridled euphoria about ‘big data’ and ‘data analytics’. What could possibly go wrong?

The characteristics of big data are commonly depicted as ‘volume, velocity and variety (Laney, 2001), leading to the widespread working de<sup>fi</sup>nition of ‘data that’s too big, too fast or too hard for existing tools to process’ (which appears to have originated as a garbling of Jacobs, 2009, p. 44). Subsequently, a few commentators have added ‘value’. Occasional mention is made of a <sup>fi</sup>fth characteristic, ‘veracity’, <sup>fi</sup>rst seen in Schroeck et al. (2012). The discussion here brings focus to bear on that aspect. It also draws to attention the need to distinguish the notion of ‘a very large data set’ from a consolidation of two or more data sets from different sources, into a single collection, whether of a physical or virtual nature.

A strong form of the big data claim is that “massive amounts of data and applied mathematics replace every other tool that might be brought to bear. Out with every theory of human behavior, from linguistics to sociology. Forget taxonomy, ontology, and psychology. … [F]aced with mas sive data, [the old] approach to science – hypothesize, model, test – is becoming obsolete. … Petabytes allow us to say: ‘Correlation is enough’” (Anderson, 2008).

The level of enthusiasm within business schools is scarcely less effusive (LaValle et al., 2011; McAfee & Brynjolfsson, 2012; Mayer-Schonberger & Cukier, 2013). Whereas observers of the information technology industry have expressed concern, little disquiet is evident within the computer science and information systems literatures. See, however, Jacobs (2009), Obole et al. (2012), Buhl and Heidemann (2013), and Wigan and Clarke (2013).

This paper addresses the question of what risks arise from inadequate attention to quality factors in big data and big data analytics. It does so by using quasi-empirical scenarios to illustrate a review of data quality and decision quality factors in the big data context.

## BIG DATA SCENARIOS

Scenarios are plausible storylines. They commence with real-life situations, which are then extended with elements that are hypothetical or speculative, but that are rooted in real-world processes. Background to their use in this context is provided in Clarke (2015). The scenarios used here are not case studies of speci<sup>fi</sup>c instances of big data at work. Instead, each is generalized, in order to encompass a range of issues not all of which are likely to arise in any particular real-life application. The intention is not to pretend to be a substitute for deep case studies of actual experience, but rather to test the assumptions underlying the big data value proposition.

Several scenarios are presented, in order to capture some of the contextual diversity within which big data ideas are being applied. Each scenario is introduced at the point in the analysis that it illustrates. Re<sup>fl</sup>ecting the patterns evident in the <sup>fi</sup>eld, most of the scenarios involve the consolidation of data from multiple sources, with only one of them dealing explicitly with analysis of a single large-transaction database. The inspiration for each of the scenarios is explained in the Supporting Information document.

## BIG DATA QUALITY

This section brie<sup>fl</sup>y outlines key aspects of the accumulated knowledge about data quality. A series of scenarios is interspersed through the theoretical material. The quality issues are of course evident with all data, but the intention here is to show how the risks are exacerbated in the context of big data. Key sources used in compiling the review include OECD (1980), Huh et al. (1990), van der Pijl (1994), Wand and Wang (1996), Wang and Strong (1996), Shanks and Darke (1998), Shanks and Corbitt (1999), Rusbridge et al. (2005), English (2006), and Piprani and Ernst (2008). An ISO 8000 series of international data quality standards has been slowly emergent for some time (Benson, 2009), but its value is limited because of its naive model of data and information.

Table 1 identi<sup>fi</sup>es the primary quality factors, separated into two categories. The ‘data quality factors are capable of being assessed at the time the data are collected. The ‘information quality’ factors, on the other hand, are not assessable until the data are used. The quality factors provide a framework within which the analysis can be conducted.

Data quality items D2, D3 and D4 are key contributors to the meaning of the data. Meaning is capable of de<sup>fi</sup>nition at the time that the data are gathered. Since the decline of the resource-intensive waterfall method of software development, however, it is much less common for a data dictionary to be even established, let alone maintained. As a result, data de<sup>fi</sup>nitions may be unclear, ambiguous and even implicit. The lack of clarity about the origina meaning increases the likelihood that the meaning will change over time, and that different and even mutually inconsistent usages of the same data item will eventuate. At the time of use, the more or less clear de<sup>fi</sup>nition is overlaid by the perspectives and interpretations of the data’s user(s).

Table 1. Quality factors

<table><tr><td>Data quality factors</td></tr><tr><td>D1 Syntactical validityConformance of the data content with the domain on which the data item is defined</td></tr><tr><td>D2 Appropriate (id)entity associationA high level of confidence that the data item is associated with the particular real-world identity or entity whose attribute(s) it is intended to represent</td></tr><tr><td>D3 Appropriate attribute associationThe absence of ambiguity about which real-world attribute(s) the data item is intended to represent</td></tr><tr><td>D4 Appropriate attribute significationThe absence of ambiguity about the state of the particular real-world attribute(s) that the data content is intended to represent</td></tr><tr><td>D5 AccuracyA high degree of correspondence of the data content with the real-world phenomenon that it is intended to represent, typically measured by a confidence interval, such as ‘±1 degree Celsius’</td></tr><tr><td>D6 PrecisionThe level of detail at which the data content is captured, reflecting the domain on which valid contents for that data item are defined, such as ‘whole numbers of degrees Celsius’</td></tr><tr><td>D7 Temporal applicabilityThe absence of ambiguity about the date and time when, or the period of time during which, the data content represents or represented a real-world phenomenon. This is important in the case of volatile data items such as total rainfall for the last 12 months, marital status, fitness for work, age and the period during which an income figure was earned or a licence was applicable</td></tr><tr><td>Information quality factors</td></tr><tr><td>I1 Theoretical relevanceA demonstrable capability of the data item to make a difference to the decision-making process in which it is to be used</td></tr><tr><td>I2 Practical relevanceA demonstrable capability of the data item’s content to make a difference to the decision-making process in which it is to be used</td></tr><tr><td>I3 CurrencyThe absence of a material lag between a real-world occurrence and the recording of the corresponding data</td></tr><tr><td>I4 CompletenessThe availability of sufficient contextual information that the data content is not liable to be misinterpreted</td></tr><tr><td>I5 ControlsThe application of business processes that ensure that the data quality and information quality factors have been considered prior to the data’s use</td></tr><tr><td>I6 AuditabilityThe availability of metadata that evidences the data quality and information quality factors</td></tr></table>

In Scenario (1) – Fraud detection, suspicious inconsistencies can arise not only from attempts to deceive but also from semantic issues even within a single database, let alone within a consolidation of multiple, inherently incompatible databases.

## Scenario (1) – Fraud detection

A company that has large sums of money <sup>fl</sup>ushing through its hands is under pressure from regulators, knows that stock exchanges run real-time fraud-detection schemes, and accepts at face value the upbeat claims made by the proponents of big data analytics. It combines fraud-detection heuristics with inferences drawn from its large transaction database and generates suspects. It assigns its own limited internal investigation resources to these suspect cases and refers some of them to law enforcement agencies.

The large majority of the cases investigated internally are found to be spurious. Little is heard back from law enforcement agencies. Some of the suspects discover that they are being investigated and threaten to take their business elsewhere and to initiate defamation actions. The investigators return to their tried-and-true methods of locating and prioritizing suspicious cases.

The purpose of collection and the value judgements of the sponsor determine the choice of what data are collected, and against what scales, and what trade-offs are made between data quality and collection costs. Purpose also underlies decisions about what metadata are collected at the same time, and what data are not collected at all. These constraints result in inevitable compromise to all of the data quality factors, yet this is frequently overlooked in the case of large data sets and is all-but submerged when multiple data sets are consolidated. Administrative actions in relation to fraud, and particularly prosecutions, are undermined by poor-quality evidence. In some contexts, commercial liability might arise. For an example, see Scenario (2). In others, a duty of care may be breached. See Scenario (3).

## Scenario (2) – Creditworthiness

A <sup>fi</sup>nancial services provider combines its transactions database, its records of chargebacks arising from fraudulent transactions, and government statistics regarding the geographical distribution of income and wealth. It draws inferences about the risks that its cardholders create for the company. It uses those inferences in its decision-making about individual customers, including credit limits and the issue of replacement and upgraded cards.

Although not publicized by the company, this gradually becomes widely known and results in negative media comments and recriminations on social media. Questions are raised about whether it con<sup>fl</sup>icts with ‘redlining’ provisions in various laws. Discrimination against individuals based on the behaviour of other customers of merchants that they use is argued to be at least immoral, and possibly illegal, but certainly illogical from an individual consumer’s perspective. The lender reviews the harm done to its reputation.

## Scenario (3) – Foster parenting

A government agency responsible for social welfare programmes consolidates data from foster care and unemployment bene<sup>fi</sup>ts databases and discovers a correlation between having multiple foster parents and later being chronically unemployed. On the basis of this correlation, it draws the inference that the longstanding practice of moving children along a chain of foster parents should be discontinued. It accordingly issues new policy directives to its case managers.

Because such processes lack transparency and foster children are young and largely without a voice, the new policy remains ‘under the radar’ for some time. Massive resistance then builds from social welfare non-governmental organizations, as it becomes apparent that children are being forced to stay with foster parents who they are fundamentally incompatible with, and that accusations of abuse are being downplayed because of the forcefulness of the policy directives based on mysterious ‘big data analytics’.

Particularly where data are collected frequently over time, the act of collection may involve data compression, through sampling, <sup>fi</sup>ltering and averaging. These actions affect Data quality 5 (Accuracy) and Information quality 4 (Completeness). Where interesting outliers are being sought, compression is likely to ensure that the potentially most relevant data are absent from the collection. Problems of these kinds arise in Scenario (4).

## Scenario (4) – Precipitation events

Historical rainfall data are acquired from many sources, across an extended period, and across a range of geographical locations. The collectors, some of them professionals but most of them amateurs, used highly diverse collection methods and frequencies, with little calibration and few controls. The data are consolidated into a single collection. A considerable amount of data manipulation is necessary, including the interpolation of data for empty cells, and the arbitrary disaggregation of long-period data into the desirable shorter periods. An attempt to conduct a quality audit against such sources as contemporaneous newspaper reports proves to be too expensive and is curtailed.

Analytical techniques are applied to the data. Con<sup>fi</sup>dent conclusions are reached about historical <sup>fl</sup>uctuations and long-term trends. Climate-change sceptics point to the gross inadequacies in the database and argue that climate-change proponents, in conducting their crusade, have played fast and loose with scienti<sup>fi</sup>c principles.

Data quality factor 2 requires that data have a reliable association with a particular real-world identity or entity. The data held about any particular (id)entity represent its digital persona (Clarke, 1994, 2014a). The reliability of the association between a real-world phenomenon and a data shadow depends on the attributes that are selected as identi<sup>fi</sup>ers, and the process of association has error factors. In some circumstances, the link between the digital persona and the underlying entity is challenging (pseudonymity), and in some cases, no link can be achieved (anonymity). Indeed, in order to protect important interests and comply with relevant laws, it may be necessary for any link to be broken (de-identi<sup>fi</sup>cation/anonymization – UKICO, 2012; DHHS, 2012). On the other hand, rich data sets are vulnerable to re-identi<sup>fi</sup>cation procedures (Sweeney, 2002; Acquisti & Gross, 2009; Ohm, 2010). These problems af<sup>fl</sup>ict all big data collections that are intended to assist in the management of long-term relationships. The problems are compounded by the expropriation of data to support purposes extraneous to the original context of use, such as longitudinal research studies.

Reliable identi<sup>fi</sup>cation processes are dif<sup>fi</sup>cult enough in individual systems. The challenges multiply when data from multiple sources are combined, particularly where the identi<sup>fi</sup>ers used by the underlying systems are not the same. The risks are particularly serious where the data are sensitive. Big social data is one such context, as illustrated by Scenario (5). Serious consequences also arise with big health data.

## Scenario (5) – Ad targeting

A social media service provider accumulates a vast amount of social transaction data, and some economic transaction data, through activity on its own sites and those of strategic partners. It applies complex data analytics techniques to this data to infer attributes of individual digital personae. It projects third-party ads and its own promotional materials based on the inferred attributes of online identities and the characteristics of the material being projected.

The brute force' nature of the data consolidation and analysis means that no account is taken of the incidence of partial identities, conflated identities, obfuscated identities, ano imaginary, fanciful, falsi<sup>fi</sup>ed and fraudulent pro<sup>fi</sup>les. This results in misplacement of a signi<sup>fi</sup>cant proportion of ads, to the detriment mostly of advertisers, but to some extent also of individual consumers. It is challenging to conduct audits of ad-targeting effectiveness, and hence, advertisers remain unaware of the low quality of the data and of the inferences. This approach to business is undermined by inappropriate content appearing on children’s screens, and gambling and alcohol ads seen by partners in the browser windows of nominally reformed gamblers and drinkers.

The big data movement commonly features the use of data for purposes extraneous to its original purpose. The many data quality issues identi<sup>fi</sup>ed earlier are exacerbated by the loss of context (In formation quality factor 4), including lack of clarity about the trade-offs applied at the time of collec tion. The absence of this information greatly increases the likelihood of misinterpretation. The big data movement commonly also involves the further step of physically or virtually consolidating data from multiple sources. This depends on linkages among data items whose semantics and syntactics are different, perhaps substantially, perhaps subtly. The scope for misunderstandings and misinterpretation multiplies. Retrospective studies across long periods, as in Scenarios (1) – Fraud de tection, (3) – Foster parenting and (4) – Precipitation events, face many or all of these problems.

De<sup>fi</sup>ciencies exist in most data sets. Over time, however, many further data integrity problems accumulate. A common problem is the loss of metadata – such as the scale against which data were originally collected, the de<sup>fi</sup>nition at the time of collection, the data’s provenance and any supporting evidence for the data’s quality – as well as loss of contextual information including undocumented changes in meaning over time. These undermine Information quality factors 4 (Completeness), 5 (Controls) and 6 (Auditability) and greatly increase the likelihood of inap propriate interpretation.

To address perceived data integrity shortfalls, analysts devise and deploy data scrubbing, cleansing or cleaning processes (Rahm & Do, 2000; Müller & Freytag, 2003). A few such processes use an external, authoritative reference point, such as a database of recognized location names and street addresses. Most, however, lack any external referent and are merely based on ‘logical data quality’, i.e. internal consistency within the consolidated data sets (e.g. Jagadish et al., 2014). As a result, the notion of ‘cleanliness’ primarily relates to the ease with which analytical tools can be applied to the data, rather than to the data itself.

A special category of challenge is what to do about missing data. It is common to interpolate a value, such as the population mean or mode. This may be a reasonable approach, particularly where the variability of data-item values is low and the analysis is focussed on population characteristics. In other circumstances, however, it may be seriously inappropriate, e.g. where the data item has highly variable values, or the analysis is focussed on individual (id)entities or on outliers. Scenario (4) – Precipitation events illustrates this problem.

Many individual data sets lack the necessary quality to be reliably analysed for new insights, and a great many consolidated collections lack integrity and can be reasonably depicted as being a mere melange. Data sets that are of uncertain original quality, and of lower curren quality, and that have uncertain associations with real-world entities, are combined, and may be modi<sup>fi</sup>ed, using means that are unclear and that are unaudited and possibly unauditable, in order to achieve consolidated digital personae that have uncertain validity and that have uncertain relationships with any particular real-world entity. To this melange, powerful analytica tools are then applied.

## THE QUALITY OF BIG DATA ANALYTICS

There is a variety of ways in which analytical tools can be applied to ‘big data’. The analyses may test hypotheses, which may be predictions from theory, correlations arising in other data sets, existing heuristics or hunches. Inferences may be drawn about the digital personae, which may be further inferred to apply to the population of entities that the data purport to represent, or to segments of that population. Pro<sup>fi</sup>les may be constructed for categories of entities that are of speci<sup>fi</sup>c interest, such as heavy weather incidents, wellness recipes, risk-prone cardholders or welfare cheats. Outliers of many different kinds can be identi<sup>fi</sup>ed. Inferences can be drawn about individual entities, directly from a particular digital persona, or from apparent inconsistencies within a consolidated digital persona, or through comparison of a digital persona against the population of similar entities, or against a previously de<sup>fi</sup>ned pro<sup>fi</sup>le, or against a pro<sup>fi</sup>le created through analysis of that particular big data collection.

It is feasible for big data analytics to be put to use as a decision system. This may be carried out formally, by, for example, automatically sending infringement or ‘show cause’ notices. However, it is also possible for big data analytics to become a decision system not through a conscious decision by an organization, but by default. This can arise where a decision maker becomes lazy or is replaced by a less experienced person who is not in as good a position to check the reasonableness of the inferences drawn by software.

Where decisions are made by analytics, or inferences arising from analytics are highly in<sup>fl</sup>uential in decision-making perhaps to the point of being a default decision that a human has to actively overrule, a number of concerns arise about decision quality. Has the decision re<sup>fl</sup>ected the scale, the accuracy and the precision of the data that were instrumental in leading to the decision? Was the inferencing mechanism that was used really applicable to those catego ries of data? Did the data mean what the inferencing mechanism implicitly treated it as meaning? To the extent that data were consolidated from multiple sources, were those sources compatible with one another in respect of the data’s scale, accuracy, precision, meaning and integrity?

Alternatively, rather than being used as a form of automated decision-making, big data analytics techniques can instead be put to use as a decision support system, with a human decision maker evaluating the inferences before applying them to a real-world purpose. However, the person may have great dif<sup>fi</sup>culty grasping the details of the data’s provenance, quality, meaning and relevance, of the analytical technique’s nature, prerequisites, characteristics and constraints, and of the rationale, which have together given rise to the recommendation.

Each item of data, when it is gathered, represents a measurement against a scale. Some data arise from measurement against a ratio scale and are capable of being subjected to analysis by powerful statistical tools. All too frequently, however, data collected on cardinal, and even on mere ordinal scales (such as Likert-scale data), are blithely assumed to be on a ratio scale, in order to justify the application of statistical inferencing. Meanwhile, a great deal of data is collected against nominal scales (including text and images), which support only weak analytical tools, fuzzy matching and fuzzy logic. A further challenge arises where data that have been measured against different kinds of scale are consolidated and analysed. The applicability of the available analytical tools requires careful consideration. A particularly serious challenge exists in the case of mixed scale data, whose conjoint analysis is more of a murky art than a precise science. These issues all arise in the context of individual data sets but are exacerbated where multiple data sets are con: solidated. Examples of these issues are present in Scenario (6) – Insider detection.

## Scenario (6) – Insider detection

A government agency receives terse instructions from the government to get out ahead of the whistleblower menace, with Brutus, Judas Iscariot, Macbeth, Manning and Snowden invoked as examples of trusted insiders who turned. The agency increases the intrusiveness and frequency of employee vetting and lowers the threshold at which positive vetting is undertaken. To increase the pool of available information, the agency exercises its powers to gain access to border movements, credit history, court records, law enforcement agencies persons-of-interest lists and <sup>fi</sup>nancial tracking alerts. It applies big data analytics to a consolidated database comprising not only those sources but also all internal communications, and all postings to social media gathered by a specialist external services corporation.

The primary effect of these measures is to further reduce employee loyalty to the organization. To the extent that productivity is measurable, it sags. The false positives arising from data analytics explode, because of the leap in negative sentiments expressed on internal networks and in social media, and in the vituperative language that the postings contain. The false positives greatly increase the size of the haystack, making the presumed needles even harder to <sup>fi</sup>nd. The poisonous atmosphere increases the opportunities for a vindictive insider to obfuscate their activities and even to <sup>fi</sup>nd willing collaborators. Eventually, cool heads prevail, by pointing out how few individuals ever actually leak information without authority. The wave of overreaction slowly subsides, leaving a bruised and dissatis<sup>fi</sup>ed workforce with a bad taste in its mouth.

A common feature of these circumstances is that decisions are being made about complex real world phenomena, and which therefore need to be represented by models that embody requisit variety, including explicit recognition of confounding, intervening and missing variables. In practice, however, the models that are applied in big data analytical work may be unduly simple, and even merely implicit. A related concern is that correlations may be, and commonly are, of low grade, yet may nonetheless be treated, perhaps implicitly, as though the relationships were causal, and causal in one direction rather than the other. These issues arise in multiple of the scenarios, but particularly (3) – Foster parenting, earlier, and (7) – Cancer treatment, presented below.

## Scenario (7) – Cancer treatment

Millions of electronic medical records reveal that people with cancer who take a certain combination of aspirin and orange juice see their disease go into remission. Research funding agencies are excited by this development and transfer resources to ‘big health data analytics’ and away from traditional systemic research into causes, pathways and treatments of disease. Pharmaceutical companies follow the trend by purchasing homeopathic suppliers and patenting herb genes. The number of doctoral and postdoctoral positions available in medical science drops sharply.

After 5 years, enough data have become available for the conclusion to be reached that the health treatments ‘recommended’ by these methods are ineffectual. A latter-day prophet emerges who decries ‘the <sup>fl</sup>ight from reason’, fashion shifts back to laboratory rather than digital research, and medical researchers slowly regain their previous high standing. The loss of momentum is estimated to have delayed progress by 10–15 years and generated a shortage of trained medical scientists.

Where decisions have real-world impacts, it is vital that there be transparency and auditability of the decision process and the decision criteria. And of course, the principle of natural justice requires that the decisions be subject to appeal processes and review. In Scenario (6) – Insider detection, the consequences are potentially very serious for an individual falsely accused of disloyalty. Scenario (7) – Cancer treatment, meanwhile, is a particularly concerning example of naive correlation as a substitute for understanding.

Transparency and auditability are dependent on the decision maker and others being able to appreciate the rationale underlying the ‘recommendation’ made by the analytical procedure

With what were once called ‘third-generation’ development tools, the rationale was evident in the form of an algorithm or procedure, which may have been explicitly documented externally to the software but was at least extractable by any person who had access to the source code and who had the capacity to read it. The fourth generation of development tools changed little in this regard, because it merely expressed the decision model in a more generally applicable manner.

The advent of the <sup>fi</sup>fth-generation adopted a different approach, however (Clarke, 1991). Rather than a model of the decision, this involves a model of the problem domain, commonly expressed in logic, rules or frames. It becomes much more dif<sup>fi</sup>cult to understand how the model applies to particular circumstances. Although explanations (in such forms as ‘which rules <sup>fi</sup>red’ lists) are feasible, they appear to be seldom made available.

With sixth-generation tools, an even greater barrier to understanding arises. A neural network embodies no formal model of a decision or even of a problem domain. There is just a pile of data, to which mathematical processes are applied, giving rise to a set of inscrutable weightings, which are then applied to each new instance. There have been expressions of concern from many quarters about the delegation of decision-making to software whose behaviour is fundamentally unauditable (e.g. Roszak, 1986; Dreyfus, 1992; Boyd & Crawford, 2012; Clarke, 2014b).

## IMPACTS AND THEIR MANAGEMENT

Given the uncertain quality of data and of decision processes, many inferences from big data are currently being accorded greater credibility than they actually warrant. Inevitably, resources will be misallocated. Within corporations, the impact will ultimately be felt in lower return on investment, whereas in public sector contexts, there will be negative impacts on public policy outcomes.

Where big data analytics are inappropriately applied to population inferencing and pro<sup>fi</sup>le construction, the harm that can arise includes not only resource misallocation but also unjusti<sup>fi</sup>ed discrimination for and against population segments.

When pro<sup>fi</sup>les generated by big data analytics are applied in order to generate suspects, on the other hand, the result is an obscure ‘predetermined characterisation or model of infraction (Marx & Reichman, 1984, p. 429), based on a ‘probabilistic cause’ rather than a ‘probable cause’ (Bollier, 2010, pp. 33–34). This results in unjusti<sup>fi</sup>ed impositions because the costs are borne by individual people, perhaps just in the form of inconvenience but sometimes with <sup>fi</sup>nancial or psychological dimensions. The lack of transparency relating to data and decision criteria results in mysterious and often undefendable accusations, which may lead to the unjust deprivation of rights. This represents a denial of natural justice, and in countries that are signatories to international conventions to a breach of the human right to information about ‘the nature and cause of the charge’ (ICCPR, 1966, at 14.3).

The already-substantial literature about big data is remarkably lacking in discussion of the issues and the impacts outlined in this paper. Worse still, many papers that touch on these topics fail to re<sup>fl</sup>ect the accumulated understanding of data and decision quality. In an earlier phase, the notion of ‘data quality mining’ was essentially reduced to mere internal consistency within the data collection (Hipp et al., 2001; Luebbers et al., 2003; Brizan & Tansel, 2006). Even balanced assessments of big data, such as Bollier (2010), fail to address the issues. Of seven articles in a special section of a leading information systems journal in December 2012 (Management Information Systems Quarterly 36, 4), not only was there no comprehensive treatment of quality factors, but there was almost no mention of such issues. The very limited guidance that exists relating to appropriate process merely addresses internal consistency checks, overlooking the Data quality and Information quality factors in Table 1, and omitting controls and audit (e.g. Guo, 2013). Similarly, Marchand and Peppard (2013) propose <sup>fi</sup>ve process guidelines but omit any meaningful consideration of processes to assure quality of the data and of the decision processes to be applied to it.

Buhl and Heidemann’s editorial in Business and Information Systems Engineering (2013, pp. 66–67) included this clear statement:

Big Data’s success is inevitably linked to … clear rules regarding data quality. … High quality data requires data to be consistent regarding time …, content …, meaning … , and data that allow for unique identi<sup>fi</sup>ability … , as well as being complete, comprehensible, and reliable.

That call to arms has been to date almost entirely ignored. A survey undertaken in mid-2015 of over a score of Calls for Papers for Big Data Conferences identi<sup>fi</sup>ed no more than <sup>fl</sup>eeting mentions of the topic, with more than half of the calls completely overlooking it.

## CONCLUSIONS

Given that big data harbours big problems as well as big opportunities, should authors be recommending measures that will enable the bad to be avoided, and the good achieved? Alternatively, can computing disciplines and professions wash their hands of these issues, secure in the belief that the responsibility lies elsewhere? Management disciplines study such matters in the abstract, and managers and executives take responsibility for decisions in the real world. So, it is arguable that they are the ones who are obligated to concern themselves with quality assurance, risk assessment and risk management.

Professional associations vary considerably in the extent to which they impose responsibilities on their members. For example, the Association for Information Systems imposes obligations in relation to the conduct of research, but not to the impacts of its members’ work (AIS, 2015). The IEEE requires its members to agree ‘to accept responsibility in making decisions consistent with the safety, health, and welfare of the public, and to disclose promptly factors that might endanger the public or the environment’ (IEEE, 2006). The British Computer Society lists ‘Public Interest’ <sup>fi</sup>rst and requires its members to ‘have due regard for public health, privacy, security and wellbeing of others and the environment’ (BCS, 2011). The Australian Computer Society declares The Primacy of the Public Interest' including 'matters of public health, safety and the environment’ (ACS, 2014). A stronger form is to be found in the Association for Computing Machinery Code of Ethics and Professional Conduct (ACM, 1992). The extracts in Table 2 make abundantly clear that these are not other people’s problems, but are responsibilities of computing and information systems professionals and academics.

## Table 2. Relevant extracts from the Association for Computing Machinery Code

<table><tr><td>1. Contribute to society and human well-beingWhen designing or implementing systems, computing professionals must attempt to ensure that the products of their efforts ... will avoid harmful effects to health and welfare (1.1)One way to avoid unintentional harm is to carefully consider potential impacts on all those affected by decisions made during design and implementation (1.2)Respect the privacy of others. This imperative implies ... that personal information gathered for a specific purpose not be used for other purposes without consent of the individual(s) (1.7)</td></tr><tr><td>2. Avoid harm to othersAny signs of danger from systems must be reported to those who have opportunity and/or responsibility to resolve them (2.5)Computing professionals have a responsibility to share technical knowledge with the public by encouraging understanding of computing, including the impacts of computer systems and their limitations. This imperative implies an obligation to counter any false views related to computing (2.7)</td></tr><tr><td>3. Be honest and trustworthyComputer professionals who are in decision making positions should verify that systems are designed and implemented to protect personal privacy and enhance personal dignity (3.5)</td></tr></table>

Codes of conduct, and ethics more generally, seldom have volitional force. Their value is in providing a basis for evaluating behaviour. Computer science and information systems academics and professionals have direct responsibility in relation to the technical aspects of data collection, storage and access. Our responsibility in relation to data analysis is shared with other disciplines and professions, but not to the extent that our responsibility is extinguished. The human aspects inherent in big data risks can, on the other hand, only be addressed through risk assessment and risk management, by ensuring that business process design incorporates safeguards, compliance audits and enforcement activities. Once again, computer science and information systems researchers and professionals bear some of the responsibility to ensure that problems are identi<sup>fi</sup>ed, publicized and addressed. We have moral responsibility, potentially translated by the courts into legal responsibility, to blow the whistle on hyperbole, and on undue reliance on technology.

How realistic are the scenarios presented in this paper? How reliable are the arguments advanced in the text about data quality and decision quality, and their impact on inferences, on actions based on them and on outcomes? To the extent that they are realistic and reliable, the buoyant atmosphere surrounding big data needs to be tempered. Nuclear physicists and nuclear engineers alike cannot avoid responsibility in relation to the impacts of their work. The same applies to computer scientists and information systems academics, and to computing and information systems professionals. Our discipline and our profession are being culpably timid.

## ACKNOWLEDGEMENTS

This paper has bene<sup>fi</sup>ted signi<sup>fi</sup>cantly from comments by the section editor and editor, which resulted in restructuring of the material and clari<sup>fi</sup>cation of the argument.

## REFERENCES

ACM (1992) ACM Code of Ethics and Professional Conduct Communications of the Association for Computing Machinery, October 1992, at http://www.acm.org/about/code-of-ethics

Acquisti, A. & Gross, R. (2009) Predicting social security numbers from public data. Proc. National Academy of Science, 106, 10975–10980.

ACS (2014) ‘Code of Professional Conduct’ Australian Computer Society, April 2014, at https://acs.org.au/\_\_data/assets/ pdf\_<sup>fi</sup>le/0014/4901/Code-of-Professional-Conduct\_v2.1.pdf

AIS (2015) ‘Code of Research Conduct’ Association for Information Systems, 4 March 2015, at http://c.ymcdn.com/ sites/ais.site-ym.com/resource/resmgr/Admin\_Bulletin/AIS\_ Code\_of\_Research\_Conduct.pdf

Anderson, C. (2008) The end of theory: the data deluge makes the scienti<sup>fi</sup>c method obsolete Wired Magazine 16:07, 23 June 2008, at http://archive.wired.com/science/discoveries/magazine/16-07/pb\_theory

BCS (2011) ‘Code of Conduct’ British Computer Society, 8 June 2011, at http://www.bcs.org/content/conMediaFile/393

Benson, P.R. (2009) ISO 8000 data quality – the fundamentals part 1. Real-World Decision Support (RWDS) Journal 3, 4 (November 2009), at http://www.ewsolutions. com/resource-center/rwds\_folder/rwds-archives/issue.2009- 10-12.0790666855/document,2009-10-12,3367922336

Bollier, D. (2010) The promise and peril of big data. The Aspen Institute, 2010, at http://www.ilmresource.com/collateral/analyst-reports/10334-ar-promise-peril-of-big-data.pdf

Boyd,D.&Crawford,K.(2012)Criticalquestionsforbigdata.Information,Communication&Society,15,662–679,DOI:10.1080/ 1369118X.2012.678878, at http://www.tandfonline.com/doi/ abs/10.1080/1369118X.2012.678878#.U\_0X7kaLA4M

Brizan, D.G. & Tansel, A.U. (2006) A survey of entity resolution and record linkage methodologies. Communications of the IIMA 6, 3 (2006), at http://www.iima.org/CIIMA/8% 20CIIMA%206-3%2041-50%20%20Brizan.pdf

Buhl, H.U. & Heidemann, J. (2013) Big data: a fashionable topic with(out) sustainable relevance for research and practice? Editorial, Business & Information Systems Engineering, 2, 65–69, at http://www.bise-journalarchive.org/pdf/01\_editorial\_36315.pdf

Clarke, R. (1991) A contingency approach to the software generations. Database, 22, 23–34, PrePrint at http:// www.rogerclarke.com/SOS/SwareGenns.htm

Clarke, R. (1994) The digital persona and its application to data surveillance. The Information Society, 10, 77–92, PrePrint at http://www.rogerclarke.com/DV/DigPersona.htm

Clarke, R. (2014a) Promise unful<sup>fi</sup>lled: the digital persona concept, two decades later. Information Technology & People, 27, 182–207, PrePrint at http://www.rogerclarke.com/ID/DP12.htm

Clarke, R. (2014b) What drones inherit from their ancestors Computer Law & Security Review, 30, 247–262, PrePrint at http://www.rogerclarke.com/SOS/Drones-I.html

Clarke, R. (2015) Quasi-empirical scenario analysis and it application to big data quality. Proc. 28th Bled eConference, Slovenia, 7–10 June 2015, PrePrint at http://www. rogerclarke.com/EC/BDSA.htm

DHHS (2012) Guidance regarding methods for de-identi<sup>fi</sup>cation of protected health information in accordance with the Health Insurance Portability and Accountability Act (HIPAA) privac rule. Department of Health & Human Services, Novembe 2012, at http://www.hhs.gov/ocr/privacy/hipaa/understand ing/coveredentities/De-identi<sup>fi</sup>cation/guidance.htm

Dreyfus, H.L. (1992) What computers still can’t do: a critique of arti<sup>fi</sup>cial reason. MIT Press, 1992.

English, L.P. (2006) To a high IQ! Information content quality: assessing the quality of the information product IDQ Newsletter 2, 3, July 2006, at http://iaidq.org/publi cations/doc2/english-2006-07.shtm

Guo, P. (2013) Data science work<sup>fl</sup>ow: overview and challenges. ACM Blog, 30 October 2013, at http://cacm. acm.org/blogs/blog-cacm/169199-data-science-work<sup>fl</sup>ow overview-and-challenges/fulltext

Hipp, J., Guntzer, U. & Grimmer, U. (2001) Data quality mining – making a virtue of necessity. Proc. 6th ACM SIGMOD Work shop on Research Issues in Data Mining and Knowledge Discovery (DMKD 2001), pp. 52–57, at http://www.cs.cornell. edu/Johannes/papers/dmkd2001-papers/p5\_hipp.pdf

Huh, Y.U., Keller, F.R., Redman, T.C. & Watkins, A.R. (1990) Data quality. Information and Software Technology, 32, 559–565.

ICCPR (1966) International covenant on civil and political rights United Nations General Assembly. 16 December 1966. at http://www.ohchr.org/en/professionalinterest/pages/ccpr.aspx

IEEE (2006) Code of ethics. IEEE, 2006, at Ihttp://www. ieee.org/about/corporate/governance/p7-8.html

Jacobs, A. (2009) The pathologies of big data. Communi cations of the ACM, 52, 36–44

Jagadish, H.V., Gehrke, J., Labrinidis, A., et al. (2014) Big data and its technical challenges. Communications of the ACM, 57, 86–94

Laney D. (2001) 3D data management: controlling data volume, velocity and variety. Meta-Group, Februar 2001, at http://blogs.gartner.com/doug-laney/<sup>fi</sup>les/2012 01/ad949-3D-Data-Management-Controlling-Data-Volume Velocity-and-Variety.pdf

LaValle S., Lesser E., Shockley R., Hopkins M.S. & Kruschwitz N. (2011) Big data, analytics and the path from insights to value. Sloan Management Review

(Winter 2011Research Feature), 21 December 2010, at http://sloanreview.mit.edu/article/big-data-analytics-and the-path-from-insights-to-value

Luebbers, D., Grimmer, U. & Jarke, M. (2003) Systematic development of data mining-based data quality tools. Proc. 29th VLDB Conference, Berlin, Germany, 2003, at http://www.vldb.org/conf/2003/papers/S17P02.pdf

McAfee, A. & Brynjolfsson, E. (2012) Big data: the managemen revolution. Harvard Business Review, 90, 61—68.

Marchand, D.A. & Peppard, J. (2013) Why IT fumbles analytics. Harvard Business Review, 91, 104–112.

Marx, G.T. & Reichman, N. (1984) Routinising the discov ery of secrets. Am. Behav. Scientist, 27, 423–452.

Mayer-Schonberger, V. & Cukier, K. (2013) Big data: a revolution that will transform how we live, work and think. John Murray, 2013.

Müller, H. & Freytag, J.-C. (2003) Problems, methods and challenges in comprehensive data cleansing. Technica Report HUB-IB-164, Humboldt-Universität zu Berlin, Institut für Informatik, 2003, at http://www.informatik. uni-jena.de/dbis/lehre/ss2005/sem\_dwh/lit/MuFr03.pdf

Oboler, A., Welsh, K. & Cruz, L. (2012) The danger of big data: social media as computational social science. First Monday 17, 7 (2 July 2012), at http://<sup>fi</sup>rstmonday.org htbin/cgiwrap/bin/ojs/index.php/fm/article/view/3993/3269

OECD (1980) Guidelines on the protection of privacy and transborder flows of personal dataOECD Paris1980

Ohm, P. (2010) Broken promises of privacy: responding to the surprising failure of anonymization. 57 UCLA Law Review 1701 (2010) 1701-1711, at http://www.patents. gov.il/NR/rdonlyres/E1685C34-19FF-47F0-B460-9D3DC 9D89103/26389/UCLAOhmFailureofAnonymity5763.pdf

van der Pijl, G. (1994) Measuring the strategic dimensions of the quality of information. Journal of Strategic Informa tion Systems, 3, 179–190.

Piprani, B. & Ernst, D. (2008) A model for dataqualityassessment. Proc. OTM Workshops (5333) 2008, pp 750–759

Rahm, E. & Do, H.H. (2000) Data cleaning: problems and curren approaches. IEEE Data Eng. Bull., 2000, at http://dc-pubs.dbs uni-leipzig.de/<sup>fi</sup>les/Rahm2000DataCleaningProblemsand.pdf

Roszak, T. (1986) The cult of information. Pantheon 1986

Rusbridge, C., Burnhill, P., Seamus, R., et al. (2005) The dig ital curation centre: a vision for digital curation, Proc, Conf. From Local to Global: Data Interoperability – Challenges and Technologies, Sardinia, 2005, pp. 1–11, at http:// eprints.erpanet.org/archive/00000082/01/DCC\_Vision.pdf

Schroeck, M., Shockley, R., Smart, J., Romero-Morales, D. & Tufano, P. (2012) Analytics: the real world use of big data IBM Institute for Business Value / Saïd Business School a the University of Oxford, October 2012, at http://www.ibm com/smarterplanet/global/<sup>fi</sup>les/se\_\_sv\_se\_\_intelligence\_\_ Analytics\_-\_The\_real-world\_use\_of\_big\_data.pdf

Shanks, G. & Corbitt, B. (1999) Understanding data quality: social and cultural aspects. Proc. 10th Australasian Conf. on Info. Syst., 1999.

Shanks, G. & Darke, P. (1998) Understanding data quality in a data warehouse, The Australian Computer Journal, 30. 122–128

Sweeney L. (2002) k-Anonymity: a model for protecting pri vacy. International Journal on Uncertainty, Fuzziness and Knowledge-based Systems, 10, 557–570, at http://arbor. ee.ntu.edu.tw/archive/ppdm/Anonymity/SweeneyKA02.pd

UKICO (2012) Anonymisation: managing data protection risk: code of practice. Information Commissioners Of<sup>fi</sup>ce, Novem ber 2012, at http://ico.org.uk/for\_organisations/data\_protection topic\_guides/\~/media/documents/library/Data\_Protection/ Practical\_application/anonymisation-codev2.pd

Wand, Y. & Wang, R.Y. (1996) Anchoring data quality dimensions in ontological foundations. Commun. ACM, 39, 86–95.

Wang, R.Y. & Strong, D.M. (1996) Beyond accuracy: wha data quality means to data consumers. Journal of Management Information Systems, 12, 5–33.

Wigan, M.R. & Clarke, R. (2013) Big data’s big unintended consequences. IEEE Computer, 46, 46–53, PrePrint a http://www.rogerclarke.com/DV/BigData-1303.html

## Biography

Roger Clarke is a consultant with a particular focus on strategic and policy aspects of eBusiness, informatio infrastructure, and dataveillance and privacy. He spent a decade as a senior academic and continues as a Visiting Professor in Cyberspace Law and Policy at UNSW in Sydney and in Computer Science at the ANU in Canberra. He holds degrees in Information Systems from UNSW and a doctorate from the ANU. He has been a Fellow of the Australian Computer Society (ACS) since 1986 and of the international Association for Information Systems (AIS) since 2012. His academic CV is at http://www. rogerclarke.com/AcademicCV.pdf. He was a Foundation Councillor of AIS and served as a Task Force member fo the 2008 revision of the Research Code.

## SUPPORTING INFORMATION

The inspirations for the Scenarios presented in this paper are at http://www.rogerclarke.com/EC/ BDBR-Supp.html.
