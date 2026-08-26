---
otero_id: 1812
otero_key: "QWKMCUQN"
title: "No News is Bad News: The Internet, Corruption, and the Decline of the Fourth Estate"
authors: "Ted Matherly; Brad N. Greenwood"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/17869"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# NO NEWS IS BAD NEWS: THE INTERNET, CORRUPTION, AND THE DECLINE OF THE FOURTH ESTATE<sup>1</sup>

Ted Matherly Department of Marketing, D’Amore-McKim School of Business, Northeastern University Boston, MA, U.S.A. {t.matherly@northeastern.edu}

Brad N. Greenwood

Department of Information Systems and Operations Management, George Mason University Fairfax, VA, U.S.A. {bgreenwo@gmu.edu}

The rise of the internet has upended numerous industries, but none more so than news production. The connectivity fostered by digitization has been accompanied by the emergence of content aggregation, the proliferation of fake news, and the extended geographic reach of industry leaders, all of which have served to hollow out local reporting capacity. In this work, we examine the result of changes wrought by the internet on an outcome of theoretical and practical significance: corruption. Inasmuch as newspapers are viewed as an important investigative arm of local communities, it is possible that corrupt local actors will be emboldened in their absence. To test this hypothesis, we employed a difference-in-differences approach, exploiting the phased closure of major daily newspapers across the country. Our results indicate a significant and positive correlation between federal corruption charges and newspaper closures. Further, we observed no evidence that the rise in online news vendors or the democratization of the press ameliorates this effect. This suggests a key issue with the increased geographic reach of digitized firms in the form of “information blindness” to local issues.

Keywords: Difference-in-differences, media, news, corruption

## Introduction

“The day I run into a Huffington Post reporter at a Baltimore zoning board hearing is the day that I will be confident that we have reached some sort of equilibrium. The next 10 or 15 years in this country are going to be a halcyon era for state and local political corruption. It is going to be one of the great times to be a corrupt politician. I really envy them.”

–David Simon, Creator of HBO’s The Wire Senate Hearing on the Future of Journalism, May 6, 2009

The rise of the internet and the digitization of news delivery has indelibly changed the face of journalism. Weekly and Sunday circulation topped 62 million households as recently as 1990.<sup>2</sup> It now stands at less than half of that, obliterated by classified advertisers like Craigslist (Gao et al., 2020;

Seamans & Zhu, 2013), competition from remote providers (Clemons et al., 2002), and the proliferation of social media (Aral et al., 2013; Aral & Zhao, 2019). Yet despite a large body of IS scholarship investigating the origins of declining reporting capacity, and the questionable quality of news that has filled the void in the absence of institutionalized media (e.g., fake news, see Kim & Dennis, 2019; Kitchens et al., 2020; Wang et al., 2021), less work has been devoted to the downstream implications of digitizing news delivery (with some notable exceptions, see Gao et al., 2020; George & Waldfogel, 2006). This is concerning because if dominant media outlets like the New York Times are displacing local vendors (Clemons et al., 2002; George & Waldfogel, 2006) and local reporting capacity is not being backfilled, coverage gaps may emerge. In this work, we highlight a worrying consequence of this knowledge gap: corruption. In doing so, we respond to recent calls to better understand the effects of the internet as it relates to media, politics, and public policy (Kitchens et al., 2020; Miranda et al., 2016; Wattal et al., 2010).

Corruption is a global scourge. It undermines the stability of prices, the ability to trade, and the ability to modernize economies (Mauro, 1995). Yet why might the decline of investigative journalism be associated with increased levels of corruption? On the one hand, research has emphasized the investigative capability of newspapers (Abernathy, 2018; Mahone & Napoli, 2020; Turkel et al., 2021). Given traditional conceptualizations of the press as a watchdog for the public interest (Coronel, 2010), it is possible that its absence might lead people to engage in corrupt practices. Further, as the press plays a role in vetting elected officials, corrupt persons who otherwise may not have run might no longer be filtered out in the election process, meaning incumbent officials may be replaced with less scrupulous ones (Hirano & Snyder, 2014; Larreguy et al., 2020). Finally, without the fear of having scandals appear on the front page, actors may feel emboldened to risk corrupt behavior, safe in the knowledge that it may all just “blow over.”

On the other hand, the democratizing effects of digitization might offset the loss of these newspapers by facilitating citizen journalism. Other contexts demonstrate such benefits. In finance, democratized peer-to-peer lenders often outperform their institutional counterparts (Lu et al., 2021). In innovation, outsourcing capital acquisition to the crowd is a viable alternative to early-stage financing (Burtch et al., 2014, Lin et al., 2023). In media, work has recognized the obsolescence of gatekeepers, following the success of self-published novels (e.g., 50 Shades of Gray) and self-promoted artists (e.g., Macklemore) (Dewan & Ramaprasad, 2012). And in journalism itself, Darnella Frazier’s recording of the murder of George Floyd sparked outrage and reforms, eventually earning her a Pulitzer Prize. This suggests that the hollowing out of local newspapers may have little effect on government officials’ perception that they are under scrutiny.

We investigate this tension by exploring the relationship between newspaper closures and federal corruption charges using a difference-in-differences design. We hypothesize that the closure of a major daily newspaper is associated with an increase in corruption charges filed by prosecutors. Data on charges of corruption were drawn from the Federal Judicial Center and data on newspaper closures were drawn from the UNC News Deserts database. Results indicate that newspaper closure is associated with increases in the per-capita number of corruption cases filed (7.32%), charges brought (6.80%), and defendants indicted (6.04%). Further, we observe no attenuating effect from the introduction of alternate content provision models. This undermines hopes that citizen journalism will counteract the declining ranks of professional journalists by increasing the diversity of sources (Carpenter, 2010) but is consistent with research on the limited effectiveness of citizen journalists (Anderson et al., 2015, Miller, 2018). Finally, limited evidence suggests that these relationships may be due to risk adjustments made by corrupt actors following a newspaper closure who erroneously perceive a lower risk of discovery, though further work is needed in this space to uncover the mechanism(s) driving these changes.

## Related Literature

## The Changing Media Landscape

The rise of the internet and the downfall of the newspaper industry has upended the world of journalism. Indeed, numerous scholars have laid the downfall of the newspaper industry at the feet of the internet (Aral et al., 2013; Cho et al., 2016). Three reasons have been put forward: advertising, reach, and competition. And although these are not mutually exclusive, they are largely seen as collectively exhaustive (Hayes & Lawless, 2021). Regarding advertising, researchers have long noted that news generation is a public subsidy, as evidenced by factors like the provision of reserved frequencies and the collective accessibility of costless media. As the internet has undermined the efficacy of the advertising subsidy (Anderson et al., 2015, Angelucci & Cagé, 2019), through both increased competition for dollars and more efficient ad targeting (Gentzkow, 2014, Seamans & Zhu, 2013), newsrooms have been scaled back.

Scholars have also noted that newspapers no longer exclusively serve their local communities (George & Waldfogel, 2006). As it is costless to digitally transmit information, better-funded newspapers like The Wall Street Journal can reach well beyond their markets (George & Waldfogel, 2006), which puts pressure on local newspapers. And while this increased reach is accompanied by superior financial performance for news vendors who can achieve it, it does not create an incentive to generate local coverage in newly entered areas. Finally, de novo competition has also had a substantial impact—from the increased reach of dominant papers to online-only entrants (Mahone & Napoli, 2020) to increased competition for classified advertising dollars (Djourelova et al., 2021, Gao et al., 2020, Seamans & Zhu, 2013) to competition from content aggregators (Clemons et al., 2002; Dellarocas et al., 2013) These shifts in costs have led to a belt-tightening effect, wherein newsrooms have shrunk and costly investigative journalism has been scaled back (Anderson et al., 2015; Miller, 2018; Peterson, 2021). As Jeff Zucker of CNN put it, journalists are trading “analog dollars” for “digital pennies.”

This raises the question of how newspapers are responding to the new digital environment. The internet is not the first phenomenon to threaten newsprint. Indeed, television had similar implications in the 1940s and 50s (Angelucci & Cagé, 2019; Park et al., 2018). As newspapers found their revenue streams thinning, they focused on smaller market segments with a higher willingness to pay. This scaling back led to changes both in the size of newsrooms and in the amount of content that could be produced (Miller, 2018; Peterson, 2021). And, unfortunately for local communities, the content that has been most strongly undermined is costly investigative coverage (Claussen, et al., 2021; Peterson, 2021), leading to predictable declines in quality.

Yet what is most striking is the limited attention that has been devoted to the downstream societal implications of declining print media (with some notable exceptions). Gao et al. (2020), for example, found that the reduced monitoring of public sector finance increases the cost of municipal borrowing, suggesting that newspapers play a role in governmental accountability. Further, Jiang and Kong (2021) examined the willingness to contravene local regulations, finding that polluters are less likely to be discovered after a local newspaper closes.

Thus, while extensive research has been devoted to the implications of emerging digital forms—e.g., classified advertisers (Chan & Ghose, 2014; Seamans & Zhu, 2013) and home-stay networks (Cui et al., 2016; Horton, 2015; Zervas, et al., 2017)—limited work has been devoted to the societal implications of the hollowing out of media and the increased reach of dominant media players (Gao et al., 2020; George & Waldfogel, 2006; Jiang & Kong, 2021). This is concerning, given the role that journalists play in holding governmental actors to account. Given that increased digitization has led to smaller newsrooms that are less able to produce in-depth local content (Anderson et al., 2015; Miller, 2018), there is a prima facie case suggesting that the internet’s deleterious effect on the newsprint industry may lead to changes in the decision-making of economic agents.

## Investigative Journalism and Corruption

The decreased costs of information and the proliferation of digital alternatives have fractured the news audience, making it less attractive to advertisers, decreasing revenue, and causing papers to close. Those local outlets that remain have been forced to redirect resources, with investigative journalism being first on the chopping block due to its high cost (Hamilton, 2016). Research has highlighted that the entry of Craigslist into U.S. markets has led to declines in political coverage (Djourelova et al., 2021), siphoned-off advertising dollars (Seamans & Zhu, 2013), and decreased monitoring (Gao et al., 2020).

There is also little evidence that the expansion of the internet has filled the gap caused by the closure of local news outlets by democratizing access to information through amateur journalists (Anderson et al., 2015; Miller, 2018). While anecdotal evidence exists that digital journalists have been able to impact the electorate (e.g., the murder of George Floyd), systematic scholarship showing these effects is limited. Wider internet access has not expanded access to local news (Hindman, 2008) and broadband access has decreased the incumbency advantages for political candidates by shifting attention to national issues (Trussler, 2022). In turn, as the thirst for national news has grown, interest in local news has withered, receiving a quarter of the page views and a sixth of the percapita minutes of national news sites (Hindman, 2011). Taken together, this suggests that the growth of the internet (1) has decreased the quantity and quality of local reporting and (2) has not provided suitable digital replacements, despite the potential for democratization (Burtch et al., 2014; Kim & Hann, 2019; Lin et al., 2023; Lu et al., 2021). The result is local areas where there is either a real or perceived decline in the public oversight of governance, with multiple pathways by which corruption might arise. We discuss three.

First, reduced oversight of local governance may affect the cohort of candidates who run for office, creating a selection effect. Newspaper endorsements are a signal of quality (Hirano & Snyder, 2014) and are key sources for the public to learn about elected officials (Larreguy et al., 2020). As a result, losing a newspaper that informs voters may impact who chooses to seek office. On the one hand, the media is often supportive of incumbents (Kahn, 1993) and the loss of a newspaper may embolden challengers. On the other hand, a newspaper closure might encourage individuals who would otherwise shy away from scrutiny to run in a race they believe will be largely unscrutinized. When fewer resources are available to inform the public, those who are more likely to engage in corrupt acts may seek office and unseat previously vetted incumbents.

Second, investigative journalism can serve an auditing function on government and thereby suppress corruption. Prior work has shown that increased access through freedom of information laws stimulates arrests for public corruption (Cordis & Warren, 2014) while a decline in media coverage decreases accountability (Gao et al., 2020). Further, media coverage is associated with the responsiveness of elected officials, whereas a limited press diminishes the degree to which officials advocate for their constituents (Snyder & Strömberg, 2010). Thus, as newspaper closures have been linked to declines in political coverage (Djourelova et al., 2021; Peterson, 2021), prior work suggests that newspaper closures may lead to reduced scrutiny of the actions taken by government officials, making malicious actors more likely to engage in corrupt practices.

Finally, the loss of a newspaper might exert an indirect effect by leading officials to incorrectly adjust their beliefs about risk. Through their interactions with journalists via the selection and auditing process, corrupt actors may come to believe that newspapers represent frontline investigators of illicit behaviors who are ready and willing to publicize wrongdoings and alert law enforcement. Such beliefs are pervasive among the public, notably in the popular perception of the Fourth Estate’s work as “custodians of public conscience” (Ettema et al., 1998), typified, for example, by the Washington Post’s investigation of Watergate. Thus, observing the closure of a local newspaper, corrupt officials may believe that the likelihood of discovery has declined and decide it is worth the risk. However, the reality is that it is much more common for cases to be uncovered by law enforcement’s own investigations. In turn, the media typically elevates the salience of such scandals by covering them ex post, increasing public awareness of issues through an agenda-setting process (Benediktsson, 2010).

Taken in sum, this work suggests that corruption may increase following the closure of a newspaper with investigative capacity. And while the above mechanisms are not mutually exclusive, they universally suggest that corruption rises when local newspapers are shuttered.

## Materials and Methods

## Measuring Corruption

Corruption is, by its nature, an activity that perpetrators seek to conceal, making it challenging to measure. Following prior work, we proxied corruption using administrative records of federal prosecutions (Albanese & Artello, 2019; Alt & Lassen, 2003, 2008, 2012; Cordis & Milyo, 2016). Employing this process afforded us three advantages over other approaches, such as surveys.<sup>3</sup> First, since we focused on federal charging, the legal standards were consistent in all locales. This decreased the likelihood that any differences were driven by heterogeneity in the definition of corruption.<sup>4</sup> Second, the assistant U.S. attorneys (AUSAs) tasked with prosecuting corruption are highly trained and have formalized procedures, presumably ensuring a consistent application of the law. Third, because corrupt actors generally seek to conceal their behavior, the total charges likely undercount actual corruption. Thus, while we predict that corruption will rise, our estimates will likely be conservative.<sup>5</sup>

## Data

To explore the association between declining investigative journalism and corrupt behavior, we examined the change in per-capita federal charges, defendants, and cases filed in district courts following the closure of a newspaper in that district. Note that federal prosecutions represent the overwhelming majority of corruption cases in the United States (Alt & Lassen, 2003, 2012).

Data were collected from several sources. Data on charges of corruption were drawn from the Federal Judicial Center. These data were sourced from U.S. attorney central charge files, which are organized at the defendant level. They contain the five most significant charges<sup>6</sup> filed against a census of defendants in U.S. district courts (1996-2018).<sup>7</sup> Details include: district, case, defendant count, filing date, and the statute that has allegedly been violated. We defined corruption-related charges based on reports from the FBI’s

Public Integrity Section (PIN).<sup>8</sup> Charges include bribery, embezzlement, fraud, interference with commerce, and schemes to defraud. A complete list is presented in Appendix Table B1.<sup>9</sup> In our robustness checks, we used an alternate measure of corruption from prior work (Cordis & Milyo, 2016). The results remained consistent.

Together, these data include 179,367 charges brought under the federal criminal code against 125,094 defendants in 91,888 cases across the 94 U.S. district courts. Data were aggregated at the district-year level. Data on newspaper closures were drawn from the UNC News Deserts database maintained by Abernathy (2018).<sup>10</sup> As our focus was on the effect of investigative journalism, which smaller newspapers rarely have the resources for, we focused on the closure of 65 major daily newspapers (details are given in Appendix Table B2). Additional data used to account for time-varying factors that might correlate with both the closure of a newspaper and a change in corruption were drawn from a variety of sources, including the U.S. Bureau of Labor Statistics, Census Bureau, and Bureau of Economic Analysis. Summary statistics and correlations are presented in Appendix Table B3. Variable definitions and sources are shown in Appendix Table B4 (online at https://papers.ssrn.com/sol3/papers.cfm?abstract\_ id=4440544)

## Variable Definitions

## Dependent Variable

We focused on three primary dependent variables. Consistent with prior work, we normalized the dependent variables by population (Alt & Lassen, 2012; Glaeser & Saks, 2006). The first is the per-capita number of defendants, Defendants, charged in district court in the district-year. This measure allowed us to capture the number of people who have been indicted by a grand jury to a probable cause standard. The second measure is the per-capita number of unique cases brought, Cases. As cases can have multiple defendants, this allowed us to capture the total number of criminal endeavors that have been discovered and charged. Finally, the third variable is Charges, the per-capita number of charges levied against defendants in the district-year. As a defendant might have multiple charges brought against them, this variable allowed us to capture the scope of charging. We log these variables to interpret the effect as an elasticity.

## Independent Variables

Consistent with prior work (Gao et al., 2020; Gentzkow et al., 2011), the independent variable of interest is Closure, a 0/1 indicator that a major newspaper shut down in district j at or before time t. The value is set to 1 the year after the district experienced a closure. The value is 0 prior to that time. Sixteen of the 94 districts were affected by multiple closures. The results were also consistent when closures were coded as an ordinal value. Since our treatment is the closure of a major daily newspaper, this does not imply the closure of all newspapers or media outlets in a district, i.e., “total closure.” As districts are large, sometimes encompassing entire states, the totality of a district’s media outlets closing is implausible.

To complete the difference-in-differences analysis, we included fixed effects for the district and year. Year fixed effects allowed us to parse out general changes in the level of corruption that occurred year-on-year across all districts. District fixed effects were used to capture time-invariant heterogeneity regarding the level of corruption in any given location. The unit of analysis was the district court-year. There are 94 districts in the U.S. Due to the limited number of charges brought in districts corresponding to the territories of Puerto Rico, Guam, the Mariana Islands, and the U.S. Virgin Islands, these districts were dropped.

## Estimation Procedure

We estimate the effect of the closure of newspapers using the following equation:

$$
y _ {j t} = \beta_ {1} C l o s u r e _ {j t} + \theta_ {j} + \lambda_ {t} + \epsilon
$$

Closure indicates that a major newspaper closed in district j before time t. θ<sub>j</sub> and λ<sub>t</sub> represent the district and time fixed effects. The unit of analysis is the district-year from 1996- 2018. The relationship was estimated using an OLS and replicated with a PPML (Appendix Table B5). Robust standard errors are clustered on the district. The results are presented in Columns 1-3 of Table 1.

<table><tr><td colspan="11">Table 1. Correlation Between Newspaper Closure and Corruption</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td></tr><tr><td>Estimator</td><td>OLS</td><td>OLS</td><td>OLS</td><td>Goodman-Bacon</td><td>Goodman-Bacon</td><td>Goodman-Bacon</td><td>Callaway &amp; Sant&#x27;Anna</td><td>Callaway &amp; Sant&#x27;Anna</td><td>Callaway &amp; Sant&#x27;Anna</td><td>OLS (Brazil)</td></tr><tr><td>Dependent variable</td><td>In(Charges)</td><td>In (Defendants)</td><td>In(Cases)</td><td>In(Charges)</td><td>In(Defendants)</td><td>In(Cases)</td><td>In(Charges)</td><td>In(Defendants)</td><td>In(Cases)</td><td>In(Cases)</td></tr><tr><td>Closure</td><td>0.0680* (0.0272)</td><td>0.0604* (0.0252)</td><td>0.0732** (0.0254)</td><td>0.0680* (0.0272)</td><td>0.0604* (0.0252)</td><td>0.0732** (0.0254)</td><td>0.0961** (0.0314)</td><td>0.0696** (0.027)</td><td>0.0886*** (0.0235)</td><td>0.134+ (0.0667)</td></tr><tr><td>Observations</td><td>2,070</td><td>2,070</td><td>2,070</td><td>2,070</td><td>2,070</td><td>2,070</td><td>2,070</td><td>2,070</td><td>2,070</td><td>297</td></tr><tr><td>R-squared</td><td>0.953</td><td>0.959</td><td>0.96</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.794</td></tr><tr><td>District fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Year fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Note: Unit of analysis: district year. Robust standard errors in parentheses (clustered on the district). \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05. Estimator: OLS: sample years: 1996-2018.

Before discussing our results, we note three important concerns. First, as our analysis leveraged multiple treatments applied over time, there was the potential for an inverse weighting issue because the estimate of the association represented the weighted average between districts that had a newspaper closure and those that did not, and between districts that had a newspaper closure earlier in the panel, and those that had not yet experienced a closure (Goodman-Bacon, 2021). This is concerning because it is possible that the relationship between newspaper closure and corruption changes over time (Callaway & Sant’Anna, 2021; Goodman-Bacon, 2021), in which case our estimate may be biased. To address this, we replicated our estimates using a Goodman-Bacon (2021) decomposition and a Callaway & Sant’Anna (2021) estimation. The results are presented in Columns 4-9 of Table 1 and Appendix Figure B1.

Second, it is possible that the trends in the dependent variable across treated and untreated districts were different prior to the closure (Angrist & Pischke, 2008). As such, newspaper closures in areas with increasing levels of corruption could have biased our estimates. To rule this out, we employed a popular variant of the Autor (2003) leads and lags model. In doing so, we interacted an indicator for when a district’s closure occurred with a series of dummies capturing the relative distance in years from the treatment to the current time t. Formally:

$$
\begin{array}{r} y _ {j t} = \sum_ {k} \tau_ {k} P r e C l o s u r e _ {j t} (k) + \beta C l o s u r e _ {j t} + \\ \sum_ {m} \omega_ {m} P o s t C l o s u r e _ {j t} (m) + \theta_ {j} + \lambda_ {t} + \epsilon \end{array}
$$

$P r e C l o s u r e _ { j t } ( k )$ is an indicator that is equal to 1 if the chronological distance between the newspaper closure in jt and the focal observation is k years. ??????????????????????<sub>????</sub>(??) is the corresponding set of post-treatment dummies. To meet the assumptions of the difference-in-differences approach, there should be no heterogeneous pre-treatment trends. Indicators of 10 years or more (before or after treatment) were collapsed into a single indicator for interpretability. The results are presented in Table 2 and Figure 1.

Finally, we note that newspapers do not close at random. While difference-in-differences is a robust identification strategy, replication in a second context greatly increases external validity. Therefore, we replicated our approach using data from Brazil, the most populous country in South America and the 12th largest by GDP in the world. Data on newspaper closures came from the Atlas da Notícia (Atlas da Notícia, 2022<sup>11</sup>), which gathers data on more than 14,000 media outlets in Brazil, including 2556 daily newspapers. Of these newspapers, 65 closed between 2011-2021, affecting 14 of Brazil’s 26 federative units (states). Data on corruption came from records from the Brazilian comptroller general— specifically, the Registration of Unfaithful and Suspended Companies, which prior work has used to measure corruption (Szerman, 2023). These data track companies and individuals who have engaged in corrupt acts with officials (e.g., bribery, fraud, obstruction of justice). The law requires registration of those found guilty of such actions and prohibits those entities from participating in contracts with the government. The results are presented in Column 10 of Table 1 (base) and Column 4 of Table 2 (relative time).

## Results

The results in Table 1 indicate a significant and positive correlation between newspaper closure and corruption in local areas, as measured by charges (Column 1), defendants (Column 2), and cases (Column 3). An economic interpretation of the coefficients suggests a 6.80% increase in charges brought, a 6.04% increase in the number of defendants charged, and a 7.32% increase in the cases filed. This provides evidence that newspaper closure is associated with increases in corruption.

<table><tr><td colspan="5">Table 2. Correlation between Newspaper Closure and Corruption in Relative Time</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Estimator</td><td>OLS</td><td>OLS</td><td>OLS</td><td>OLS</td></tr><tr><td>Context</td><td>US</td><td>US</td><td>US</td><td>Brazil</td></tr><tr><td>Dependent variable</td><td>In(Charges)</td><td>In(Defendants)</td><td>In(Cases)</td><td>In(Charges)</td></tr><tr><td colspan="5"></td></tr><tr><td>Closure (t-10+)</td><td>0.00645(0.0493)</td><td>-0.0100(0.0419)</td><td>-0.0426(0.0417)</td><td></td></tr><tr><td>Closure (t-9)</td><td>0.0403(0.0394)</td><td>0.0296(0.0356)</td><td>0.00315(0.0338)</td><td>-0.0513(0.145)</td></tr><tr><td>Closure (t-8)</td><td>-0.00391(0.0394)</td><td>0.00259(0.0338)</td><td>-0.0302(0.0380)</td><td>-0.0273(0.133)</td></tr><tr><td>Closure (t-7)</td><td>0.0130(0.0391)</td><td>0.00963(0.0356)</td><td>-0.00446(0.0315)</td><td>-0.0414(0.135)</td></tr><tr><td>Closure (t-6)</td><td>0.0282(0.0426)</td><td>0.0353(0.0337)</td><td>0.0219(0.0265)</td><td>-0.000(0.109)</td></tr><tr><td>Closure (t-5)</td><td>0.00953(0.0474)</td><td>0.00938(0.0371)</td><td>-0.0170(0.0307)</td><td>-0.0415(0.0746)</td></tr><tr><td>Closure (t-4)</td><td>0.00844(0.0411)</td><td>0.0208(0.0328)</td><td>0.00112(0.0288)</td><td>-0.0755(0.0794)</td></tr><tr><td>Closure (t-3)</td><td>0.00593(0.0329)</td><td>0.0199(0.0231)</td><td>0.00171(0.0225)</td><td>-0.0310(0.0736)</td></tr><tr><td>Closure (t-2)</td><td>0.0304(0.0367)</td><td>0.0392(0.0277)</td><td>0.0283(0.0222)</td><td>-0.0305(0.0548)</td></tr><tr><td>Closure (t-1)</td><td>0.0116(0.0250)</td><td>0.0266(0.0212)</td><td>0.00710(0.0171)</td><td>0.0121(0.0656)</td></tr><tr><td colspan="5">Closure (t0) omitted from the estimation</td></tr><tr><td>Closure(t+1)</td><td>0.0416(0.0360)</td><td>0.0425(0.0282)</td><td>0.0316(0.0238)</td><td>0.103(0.0882)</td></tr><tr><td>Closure(t+2)</td><td>0.0853*(0.0343)</td><td>0.0749**(0.0281)</td><td>0.0500*(0.0244)</td><td>0.161(0.0952)</td></tr><tr><td>Closure(t+3)</td><td>0.0856**(0.0311)</td><td>0.0757**(0.0236)</td><td>0.0783***(0.0227)</td><td>0.280*(0.112)</td></tr><tr><td>Closure(t+4)</td><td>0.0926*(0.0465)</td><td>0.0992*(0.0432)</td><td>0.0911+(0.0482)</td><td>0.279*(0.127)</td></tr><tr><td>Closure(t+5)</td><td>0.0842+(0.0462)</td><td>0.0958*(0.0393)</td><td>0.107*(0.0460)</td><td>0.246+(0.133)</td></tr><tr><td>Closure(t+6)</td><td>0.135*(0.0567)</td><td>0.124**(0.0449)</td><td>0.111**(0.0397)</td><td>0.243*(0.102)</td></tr><tr><td>Closure(t+7)</td><td>0.133**(0.0464)</td><td>0.116**(0.0358)</td><td>0.102**(0.0327)</td><td></td></tr><tr><td>Closure(t+8)</td><td>0.135**(0.0419)</td><td>0.139***(0.0353)</td><td>0.139***(0.0377)</td><td></td></tr><tr><td>Closure(t+9)</td><td>0.200*(0.0761)</td><td>0.168**(0.0511)</td><td>0.139***(0.0369)</td><td></td></tr><tr><td>Closure(t+10+)</td><td>0.168*(0.0712)</td><td>0.148*(0.0608)</td><td>0.122*(0.0551)</td><td></td></tr><tr><td>Observations</td><td>2070</td><td>2070</td><td>2070</td><td>297</td></tr><tr><td>R-squared</td><td>0.953</td><td>0.959</td><td>0.96</td><td>0.807</td></tr><tr><td>District fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Year fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Note: Unit of analysis: location-year. Robust standard errors in parentheses (clustered on the district). \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05. Estimator: OLS: sample years: 1996-2018 (U.S.) 2011-2021 (Brazil).

Figure 1. Visualization of OLS Estimates in Relative Time  
![](/api/attachments/QWKMCUQN/fulltext/images/4a9ae1966062a76e4c3115678a4ffc42cf8ed1af6f4d41a7512ffde996b11045.jpg)

![](/api/attachments/QWKMCUQN/fulltext/images/11d55a94343adfeb195887da8f453c62b341c4abd25bda48d49a972605a00aaf.jpg)  
Note: Y-axis, dependent variable. X-axis time. 95% confidence intervals displayed

![](/api/attachments/QWKMCUQN/fulltext/images/6411b2148e0b49907e439259e4e61532b79e1723ca7dd988fca0681d6ab7ee6c.jpg)

Results of the Goodman-Bacon (2021) decomposition and the Callaway & Sant’Anna (2021) estimations are in Columns 4-9. Recall that the purpose of these estimators is to account for bias emerging from inverse weighting. As can be seen, these estimates are nearly identical to the base estimates. Further, we note that most of the estimated relationship (83.3%) is due to comparisons of treated and untreated groups, with only 16.7% coming from variations in treatment timing. While we caution the reader that the estimates in the tails are based on small groups, the visual representation of the Callaway & Sant’Anna model is illustrative (charges are shown in Appendix Figure B1). Figures for defendants and cases are nearly identical. Two things are immediately visible. First, we observe no demonstrable pre-treatment trends. Instead, there is a random walk above and below the x-axis. Second, there is a visible uptick after treatment, suggesting a significant change in corruption that grows over time. In sum, the consistency with our baseline analyses suggests that the differences in treatment timing did not materially bias the estimate.

We next consider the results of the event study models (Table 2 and Figure 1). As can be seen, no systematic pre-treatment trends exist across the three dependent measures. This is indicated by the t-x dummies. Of the 33 pre-treatment estimates, none are significant, and tests of joint significance are not different from 0 (all $F s < 0 . 9 1$ , all ps > 0.54). This suggests parity across the treated and untreated groups pretreatment. Following closure, the relationship is initially insignificant, but grows over time, becoming stable three years after treatment. This is consistent with the lag that would accompany the emboldening of a criminal element.<sup>12</sup> This once again suggests that the closure of major newspapers is associated with more corruption.

Finally, we turn to our estimates in the Brazilian context. Once again, the results remain consistent. In the base estimation (Column 10 of Table 1), we observe a significant and positive correlation between the closure of a daily newspaper and the number of corruption charges brought by Brazilian prosecutors in that state.<sup>13</sup> Similarly, in the relative time estimates (Column 4 of Table 2), we observe no significant pre-treatment trends and a significant correlation with the number of cases brought after treatment. This suggests that the association between newspaper closure and increases in corruption is not a U.S.-only phenomenon.

## Robustness Checks

While the above provides strong prima facie evidence of the correlation between declining investigative journalism spurred by the internet and corruption, alternate explanations could be proposed. In what follows, we subject our results to a battery of falsification tests. A summary of the tests is presented in Table 3. A full description is given in Appendix B. We briefly discuss each.

<table><tr><td colspan="3">Table 3. Summary of Robustness Checks</td></tr><tr><td>Alternative explanation</td><td>Test</td><td>Finding</td></tr><tr><td>Treatment effect heterogeneity due to variation in timing and dispersion in geography</td><td>Event study model to test how effect evolves over timeGoodman-Bacon decomposition for inverse weightingCallaway &amp; Sant&#x27;Anna estimation</td><td>Significant positive effects observed following closure that are consistent (Table 2, Figure 1).Results remain consistent (Table 1).Results remain consistent (Table 1, Appendix Figure B1).</td></tr><tr><td>Potential endogeneity of the treatment and outcome within the U.S. system</td><td>Replicate analysis using administrative data from Brazil</td><td>Results remain consistent (Tables 1 and 2) in replication.</td></tr><tr><td>Time-varying social, economic, and governmental factors are correlated with newspaper closure and an increase in crime.</td><td>Include relevant time-varying controls relating to the local news environment, economics, governance, social media use, and prosecutorial resources</td><td>Results (Appendix Table B6) remain consistent.</td></tr><tr><td>Effects may be due to the set of crimes classified as corruption</td><td>Replicate estimations using the set of consolidated crimes from Cordis and Milyo (2016)</td><td>Results (Appendix Table B7) remain consistent.</td></tr><tr><td>The US attorney&#x27;s office is increasing its aggressiveness in a manner that is spuriously correlated with newspaper closure</td><td>Replicate the estimations with placebo crimes (drug-related crimes) which should not be influenced by newspaper closure</td><td>No significant relationship between newspaper closure and drug offenses is observed (Appendix Table B8).</td></tr><tr><td>Corruption is causing newspapers to close, i.e. reverse causality</td><td>Examine pre-treatment trends to determine if the effect manifests before closureRegress closure on corruption measures using a hazard modelReplicate analysis using administrative data from Brazil</td><td>No significant pre-treatment differences detected (Table 2)No consistent effects of correlation between corruption measures and the closure of newspapers (Appendix Table B9)Consistent results (Tables 1 and 2) in replication.</td></tr><tr><td>Serial correlation in the regression errors</td><td>Random treatment testInclude lags in the estimation as proposed by Bertrand et al. (2004)</td><td>Pseudo-treatments are clustered around zero and actual treatment is well outside the 95% confidence interval (Appendix Figures B2a-B2f).Results (Appendix Table B10) remain consistent.</td></tr><tr><td>Prosecutors alter behavior to prosecute different crimes after newspaper closure.</td><td>Investigate changes in penalties as defined by average prison time, probationary period, and fine</td><td>No significant change in penalties accrued by defendants (Appendix Table B11).</td></tr></table>

First, to assess whether time-varying factors correlating with closure and corruption would result in an omitted variable bias, we included a series of time-varying controls regarding news generation, economic issues, governance, social media use, and the U.S. attorney’s office. Results are shown in Appendix Table B6 and remain consistent. Second, while the charges included in our measure of corruption are based on the FBI PIN’s definition, it is worth considering alternate approaches to demonstrate that the estimate is not dependent on the charges used. We thus replicated our estimations using the definition contained in Cordis and Milyo (2016). Results are given in

Appendix Table B7 and remain consistent. A third check explored placebos. While our interviews suggest that corruption is consistently a top priority, it is conceivable that newspaper closures correlate with a generally more aggressive U.S. attorney’s office (Boylan & Long, 2003). We thus replicated our estimations using drug crimes, the most common crime in federal courts, which should be uncorrelated with corruption levels (Campante et al., 2013). Results are given in Appendix Table B8 and indicate no material change in the number of drug charges brought, defendants charged, or cases indicted. This suggests that prosecutors are not altering their behavior.

A fourth concern relates to reverse causality. It is possible, for example, that spikes in corruption are driving newspaper closure rather than vice versa. To investigate this, we estimated a logit hazard model with newspaper closure as the DV. Results are presented in Appendix Table B9 and indicate that corruption is not positively correlated with closure. A fifth concern relates to structural issues in a two-way fixed effect estimation. Scholars have noted that such estimates can deflate standard errors (Bertrand et al., 2004). To probe this possibility, we employed two approaches: the creation of pseudo-treatments and the inclusion of lags in the estimates (Appendix Figure B2 and Table B10). Both approaches indicate that serially correlated standard errors are not a material concern.

Our final concern relates to prosecutorial discretion and the possibility that prosecutors are changing the severity of corruption pursued, i.e., charging less severe cases. To investigate this possibility, we examined outcomes in the form of average prison and probabtion sentences, and fines imposed. The results are shown in Appendix Table B11 and indicate no significant change in penalties. This suggests that prosecutors are not changing their targets in the cases they pursue.

To further explore the mechanism between newspaper closures and corruption, we conducted a series of additional analyses. However, as noted in Appendix C of the online supplement, we found null effects, suggesting that the selection and auditing mechanisms do not explain the relationship. Due to data limitations, we were not able to identify strong evidence for a risk adjustment by corrupt actors following closures. We return to this as an area for future research in the general discussion.

## Empirical Extensions: Digital News Vendors

The above suggests that the closure of newspapers is strongly correlated with increased levels of corruption. This prompts the question of what solutions might exist. Prior work has suggested several potential venues for this information. First, many journalists have left shuttered newspapers and moved to nonprofit investigative reporting centers (Lanosga & Houston, 2017). These organizations rely on donations or grants to fund investigations (Bonica, 2013). To investigate the relationship, if any, between this venue and corruption, we gathered data from the Institute for Nonprofit News and matched each center’s opening to the federal district-year based on location. The second potential venue is online-only news sites. While many digital news sites are of high quality, some of these outlets merely seek to look like a traditional newspaper but provide highly partisan content (i.e. “pink slime,” Bengani, 2019). These sites typically publish content produced elsewhere, presented alongside opinion pieces and repackaged press releases (Mahone & Napoli, 2020). We gathered data on high-quality digital news organizations from Project News Oasis as well as data on low-quality sites. We also included locally focused news competitors and aggregators, i.e., Craigslist and Patch.com. Five new treatments were then created (Non-Profit News, Project News Oasis, Online Only News, Craigslist, and Patch), corresponding to the opening of each of these site types in the district-year. This allowed us to evaluate whether there was any relationship between these potential alternatives to newspapers and corruption.

The results are presented in Table 4. As can be seen in Columns 1-3, the association between newspaper closures and local corruption persisted when these covariates were added. Further, we observed no systemic relationship between the opening of any of these online-focused competitors and corruption. This is not surprising, given the amateurism (Anderson et al., 2015; Miller, 2018) and hyper-partisan nature of many of these outlets (Bengani, 2019). Still, it is concerning because it undermines the case proposed within the information systems community, i.e., that a democratized press can resolve the issues emanating from the closure of newspapers. Taken in sum, these findings suggest that neither nonprofit news centers nor online news vendors have a significant statistical relationship with corruption.

## Discussion

In this work, we examined the downstream implications of one of the great casualties of the rise of the internet: the demise of the newspaper industry. While IS scholarship has focused on the implications of digitization for years, ranging from the changing nature of work (Gopal & Koka, 2009) to issues of public health and safety (Chan & Ghose, 2014; Liu & Bharadwaj, 2020; Park et al., 2021), limited attention has been devoted to the changing nature of news generation, with a few notable exceptions (Gao et al., 2020, Jiang & Kong, 2021).

Our results suggest two key findings. First, the closure of a major newspaper is associated with a significant rise in corruption in areas where that paper operated. Second, we observed no evidence that any of the contemporary approaches to news distribution through democratization have been able to temper or reverse this effect. This raises the question of why. Exploratory analysis (Appendix C) provides some suggestive evidence of the media’s agendasetting role, but further scholarship is needed to understand the underlying mechanism.

<table><tr><td colspan="4">Table 4. Correlation Between Digital News Sources and Corruption</td></tr><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>In(Charges)</td><td>In(Defendants)</td><td>In(Cases)</td></tr><tr><td>Closure</td><td>0.0727*(0.0277)</td><td>0.0632*(0.0259)</td><td>0.0762**(0.0259)</td></tr><tr><td>Online only “local” news</td><td>0.000674(0.0508)</td><td>-0.0221(0.0441)</td><td>-0.0369(0.0453)</td></tr><tr><td>Project news oasis</td><td>-0.0245(0.0258)</td><td>-0.0115(0.0233)</td><td>-0.0172(0.0215)</td></tr><tr><td>Craigslist</td><td>0.0340(0.0270)</td><td>0.0224(0.0237)</td><td>0.0118(0.0207)</td></tr><tr><td>Nonprofit news</td><td>-0.0558(0.0440)</td><td>-0.0576(0.0414)</td><td>-0.0398(0.0399)</td></tr><tr><td>Patch</td><td>0.0474+(0.0276)</td><td>0.0291(0.0240)</td><td>0.0162(0.0218)</td></tr><tr><td>Observations</td><td>2,070</td><td>2,070</td><td>2,070</td></tr><tr><td>R-squared</td><td>0.953</td><td>0.959</td><td>0.960</td></tr><tr><td>District fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Year fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Note: Unit of analysis: district year. Robust standard errors in parentheses (clustered on the district). \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05. Estimator: OLS: sample years: 1996-2018.

## Contributions to IS Scholarship

We make two contributions to IS scholarship. First, we contribute to the corpus of work on the societal effects of digitization. While scholars have extensively examined the after-effects of information systems adoption, including online posting boards (Chan & Ghose, 2014; Chan et al., 2019), transportation network firms (Burtch et al., 2018; Greenwood & Wattal, 2017; Liu et al., 2021; Park et al., 2021), crowdfunding (Agrawal et al., 2013; Burtch & Chan, 2014; Kim & Hann, 2019; Rhue & Clark, 2016), and peer-topeer marketplaces (Ozer et al., 2019; Wang & Overby, 2022), little attention has been devoted to the downstream implications of hollowing out institutional media. And the research that has focused on the effects of media has largely focused on the decline of newspapers overall (George & Waldfogel, 2006; Greenwood & Gopal, 2015; Seamans & Zhu, 2013) rather than addressing the societal implications of that decline. This is striking given the importance of a robust free press to the function of a stable democracy and the degree to which citizens are engaging with news media each day (Kim & Dennis, 2019). We therefore respond to calls to investigate how digitization is influencing consumer welfare (Brynjolfsson et al., 2018) and the changing dynamics of media, politics, and policy (Aral et al., 2013; Lucas et al., 2013; Miranda et al., 2016; Wattal et al., 2010).

We further contribute to recent scholarship on news media. Once again, the findings are rich and varied and include explorations of how social media has influenced the sharing of traditional media content (Aral & Zhao, 2019), the varied impacts of de novo classified ad providers (Djourelova et al., 2021; Liu & Bharadwaj, 2020; Seamans & Zhu, 2013) and news vendors (Usher & Kim-Leffingwell, 2023), and the burgeoning body of research on fake news (Kim & Dennis, 2019; Kim et al., 2019; Wang et al., 2021). We push this body of work forward, investigating the relationship between the fall of the institutional press, as precipitated by the internet, and a deleterious societal outcome: corruption.

## Implications for IS Scholarship

Our findings highlight three paths forward for IS scholarship. First, there is an evident need to devote future scholarship to uncovering the mechanisms behind the observed relationships. And while the inability to detect the precise mechanism(s) curtails the scope of the practical implications of this work, it also offers rich opportunities for future IS media scholars.

Second, it is evident that the faltering economic incentives to engage in regional media are problematic. Because the increased reach of major newspapers creates local information blindness for consumers and subsequently correlates with increases in corruption, there is a need for scrutiny in markets with a failing institutional press. At least three potential approaches exist: (1) sharing models of content creation across news organizations, (2) increasing the efficacy of digital journalism by upskilling digital reporters, or (3)

abdication. As the shared content model already exists through the various newswires (e.g., AP, Reuters), there is a proof of concept that collaborative content generation works, notably under groups like the Independent Consortium for Investigative Journalism, which uncovered immense schemes to defraud the public (e.g., The Panama Papers, The Pandora Papers). Yet this model has apparently had limited success at the local level. Such de novo investigative bodies could be wholly owned by papers in the form of satellite offices or take the form of independent contractors who are supported based on output. Such ownership issues aside, there is an evident need for a deeper understanding of how to resolve the paucity of local coverage by effectively pooling resources or increasing the quality of content provided through digital outlets (again, by either upskilling digital journalists or incentivizing national newsvendors like USA Today to seriously investigate local issues).

The second path for IS scholars to consider is the effective democratization of labor. Considerations of democratization to date have included both skilled knowledge work (e.g., coding, online lending) and unskilled labor (e.g., Mechanical Turk, crowdsourcing) (Burtch et al., 2014; Kim & Hann, 2019; Lin et al., 2023; Lu et al., 2021), with a clear bias toward contexts that exhibit a significant effect, i.e. the file drawer problem. Yet, the absence of a relationship in our context suggests boundary conditions in the efficacy of democratized labor. This underscores the need for theoretical work along three paths that identifies the conditions under which (1) democratizing will succeed and fail in skilled and unskilled labor markets, (2) it makes sense for decision makers (managers or policy makers) to invest in the upskilling of democratized labor, (3) the skills gap across democratized and professional labor has no material effect on the quality of output. It is evident that democratized journalism can shape public discourse. The release of videos showing the murders of George Floyd and Ahmaud Arbery illustrates how potent this can be. Yet merely having this information available is rarely sufficient, and additional labor is required to provide context and help audiences understand the implications of the information. It is critical for IS scholars to better understand the boundary conditions under which such effects are likely to manifest.

## Practical Implications

Important implications for newsvendors, policy makers, and the public at large extend from this work, even absent a definitive mechanism. For policy makers, given the degree to which newsrooms have been scaled back—and with them the coverage of local corruption (Djourelova et al., 2021)—it is clear that providing local news to the public is becoming difficult (Hindman, 2008). At the same time, there has been a shift in attention to national issues (Hindman. 2011; Trussler,

2022), further exacerbating the risks associated with local news being usurped by national media providers, whose reach has been facilitated by the internet. As a result, there is an evident need for public policy to incentivize local journalism, with guidance from IS researchers on how the internet can facilitate the gathering and dissemination of this information. This could be delivered in various ways. Given that newspapers have historically run multiple versions based on location (e.g., the domestic and international editions of the Times), with global content being produced through standardized news wires (e.g., the AP, Reuters, or UPI), the proof of concept is largely in place, though further refinement of these models is obviously needed in the digital age.

For news vendors, as discussed, there is a need for more effective models of content creation in media markets that are currently underserved. Managers at media vendors have several options: collaborate across organizations to service news deserts at lower costs, develop lower-cost means of monitoring and reporting, or wait for government intervention. Given the extent of recent consolidation in news media, it is surprising that collaboration between organizations remains a challenge. To reduce the costs of monitoring and reporting, IT tools such as digital news marketplaces could facilitate collaboration despite greater organizational distance. In any case, IT solutions have not yet led to any meaningful changes in the ability to cover underserved areas. This suggests that technology alone is insufficient to address the underlying issues, and that significant human capital is required in the journalistic process. Thus, managers of news production need to either upskill workers or devise new ways to farm data.

Governmental intervention also represents a potential path. Intuitively, this is already ongoing because criminals are being apprehended by the Department of Justice, rather than being deterred by the free press. But given the expense of federal investigations, the current status quo is likely an inefficient allocation of public resources. Since its inception, the press has continuously been subsidized; as such, one possible remedy would be a direct subsidy from Congress to mitigate the costs of covering underserved news areas. However, this form of collaboration is risky, as it would require the free press to become subsidized by the state, which carries other risks.

## Limitations

This work is not without limitations and represents only a sliver of the potential downstream implications of the shuttering of the newspaper industry; thus, it is inappropriate to make any broad conclusions about welfare based on this research alone. First, we were unable to observe the mechanism(s) underpinning the associations we uncovered in this work. This offers a clear path forward for future scholars. We also were unable to observe the true rate of corruption— we could only proxy it based on charges that were filed. This limitation would be more concerning if the number of charges filed decreased after a newspaper closed because it would not be possible to differentiate between a falling level of crime and a dependence upon reporters to uncover crime. However, given that the number of charges is increasing, it suggests that our results are, if anything, conservative. Second, although we focused on newspapers as a proxy for coordinated investigatory human capital, we were unable to observe the amount of human capital persisting after closure. While our results were consistent when controlling for the number of journalists and journalist wages, we were unable to ascertain whether journalists were continuing their work with other information vendors following a newspaper closure. To the extent that newspapers have a reputation for more serious and impactful reporting than many other types of vendors (Brians & Wattenberg, 1996), this should not be an issue. Third, we were unable to observe the resources devoted to uncovering each crime and whether that is changing. Intuitively, the cost of discovery would be the sum of the costs accrued by federal and local law enforcement. To calculate costs, we would need budgetary information from these sources. We were unable to find any reliable sources of data, which is unsurprising given their sensitivity.

Fourth, we did not consider the effect of television news. This is a function of three general facts. The first is that local television news is largely stable (an affiliate for CBS, NBC, ABC, and Fox being available in almost all media markets), meaning that consumers in these markets are experiencing little disruption. Second, the degree of investigative journalism conducted across newspapers and television is different (as evidenced by the Pulitzer Prize, Peabody Award, etc.). While serious journalism does exist on shows like 60 Minutes or in broader national syndicates, local television news coverage is constrained to the limited space available for content, relative to print media, thus limiting its ability to provide in-depth information (Robinson & Davis, 1990). Third, much local televised news coverage is mixed with commercial content as well as cross-promotions with other station shows of limited news value (Wood et al., 2004). Taken together, these factors suggest that the journalism provided by local print media is substantively different from that provided by local television news. This topic also offers rich opportunities for scholars in the digital age.

## Conclusion

The proliferation of communication platforms has fundamentally altered how individuals share information, but its second-order effects remain understudied. We found evidence of one such impact, a rise of corruption following the shuttering of local newspapers. However, the solutions proposed to remedy the withdrawal of local newspaper coverage, such as the democratization of the press, have not delivered on their promise. This highlights the continued importance of the Fourth Estate as a check on corruption and the need for innovation in the design of information systems to support this vital institution.

## Acknowledgments

The authors wish to thank the senior editor, Jerry Kane, as well as the incredibly constructive review panel. In addition, the authors thank participants of the Georgetown University Seminar Series, the UT Dallas Seminar Series, the University of Rochester Seminar Series, the Virginia Tech Seminar Series, the Clemson University Seminar Series, the University of Florida Scholarship Workshop, the University of Oregon Seminar Series, the University of Minnesota Seminar Series, the Tilburg University Seminar Series, the University of Illinois Seminar Series, the Johns Hopkins University Seminar Series, and the University of Southern California Seminar Series. Earlier versions of this paper received significant feedback from Corey Angst, Gord Burtch, Daniel Malter, Marshall Van Alstyne, and the University of Maryland Reading Group. Each author contributed equally to this work. The authors have no conflicts to disclose. Any remaining errors are our own.

## References

Abernathy, P.M. (2018). The expanding news desert. Center for Innovation and Sustainability in Local Media, School of Media and Journalism, UNC Chapel Hill.

Agrawal, A., Ch, C., & Goldfarb, A. (2013). Some simple economics of crowdfunding (NBER working paper 19133). National Bureau of Economic Research. https://doi.org/10.3386/w19133

Albanese, J. S., & Artello, K. (2019). The behavior of corruption: An empirical typology of public corruption by objective & method. Journal of Criminology, Criminal Justice, Law & Society, 20 (1), 1-12. https://doi.org/10.1080/15564886.2020.1823543

Alt, J. E., & Lassen, D. D. (2003). The political economy of institutions and corruption in American states. Journal of Theoretical Politics, 15 (3), 341-365. https://doi.org/10.1177/ 09516928030150030

Alt, J. E., & Lassen, D. D. (2008). Political and judicial checks on corruption: Evidence from American state governments. Economics & Politics, 20(1), 33-61. https://doi. org/10.1111/j.1468-0343.2007.00319.x

Alt, J. E., & Lassen, D. D. (2012). Enforcement and public corruption: Evidence from the American states. The Journal of Law, Economics, and Organization, 30 (2), 306-338. https://doi.org/10.1093/jleo/ews036

Anderson, C. W., Bell, E., & Shirky, C. (2015). Post-industrial journalism: Adapting to the present. Geopolitics, History and International Relations, 7 (2), 32-123.

Angelucci, C., & Cagé, J. (2019). Newspapers in times of low advertising revenues. American Economic Journal:

Microeconomics, 11 (3), 319-364. https://doi.org/10.1257/mic. 20170306

Angrist, J. D., & Pischke, J. S. (2009). Mostly harmless econometrics: An empiricist’s companion. Princeton University Press. https://doi.org/10.1515/9781400829828

Aral, S., Dellarocas, C., Godes, D. (2013). Introduction to the special issue—Social media and business transformation: A framework for research. Information Systems Research, 24(1), 3-13. https://doi.org/10.1287/isre.1120.0470

Atlas da Notícia (2022). Veículos cadastrados, desertos de notícia e não desertos. https://www.atlas.jor.br/dados/app/.

Aral, S., Zhao, M. (2019). Social media sharing and online news consumption. SSRN. http://dx.doi.org/10.2139/ssrn.3328864

Autor, D.H. (2003). Outsourcing at will: The contribution of unjust dismissal doctrine to the growth of employment outsourcing. Journal of Labor Economics. 21(1), 1-42. https://doi.org/ 10.1086/344122

Benediktsson, M. O. (2010). The deviant organization and the bad apple CEO: Ideology and accountability in media coverage of corporate scandals. Social Forces, 88(5), 2189-2216. https://doi.org/10.1353/sof.2010.0032

Bengani, P. (2019). Hundreds of “pink slime” local news outlets are distributing algorithmic stories and conservative talking points. Columbia Journalism Review. https://www.cjr.org/tow\_center\_ reports/hundreds-of-pink-slime-local-news-outlets-aredistributing-algorithmic-stories-conservative-talking-points.php

Bertrand, M., Duflo, E., Mullainathan, S. (2004). How much should we trust differences-in-differences estimates? The Quarterly Journal of Economics, 119(1), 249-275. https://doi.org/10.1162 003355304772839588

Bologna, J. (2017). Corruption, product market competition, and institutional quality: Empirical evidence from the US states. Economic Inquiry, 55(1), 137-159. https://doi.org/10.1111/ecin. 12378

Bonica, A. (2013). Ideology and interests in the political marketplace. American Journal of Political Science, 57(2), 294-311. https://doi.org/10.1111/ajps.12014

Boylan, R. T., & Long, C. X. (2003). Measuring public corruption in the American states: A survey of state house reporters. State Politics & Policy Quarterly, 3(4), 420-438. https://doi.org 10.1177/153244000300300405

Brians, C. L., & Wattenberg, M. P. (1996). Campaign issue knowledge and salience: Comparing reception from TV commercials, TV news and newspapers. American Journal of Political Science, 40(1), 172-193. https://doi.org/10.2307/ 2111699

Brynjolfsson, E., Diewert, W. E., Eggers, F., Fox, K. J., & Gannamaneni, A. (2018). The digital economy, GDP and consumer welfare: Theory and evidence. In Proceedings of the ESCoE Conference on Economic Measurement, Bank of England (pp. 16-17).

Burtch, G., Carnahan, S., Greenwood, B.N. (2018). Can you gig it? An empirical examination of the gig-economy and entrepreneurial activity. Management Science, 64(12), 5497- 5520. https://doi.org/10.1287/mnsc.2017.2916

Burtch, G., & Chan, J. (2014). Reducing medical bankruptcy through crowdfunding: evidence from GiveForward. In Proceedings of the 35th International Conference on Information Systems.

Burtch, G., Ghose, A., & Wattal, S. (2014). Cultural differences and geography as determinants of online prosocial lending. MIS

Quarterly, 38(3), 773-794. https://doi.org/10.25300/misq/ 2014/38.3.07

Callaway, B., & Sant’Anna, P. H. (2021). Difference-in-differences with multiple time periods. Journal of Econometrics, 225(2), 200-230. https://doi.org/10.1016/j.jeconom.2020.12.001

Campante, F. R., Do, Q. A., & Guimaraes, B. V. (2013). Isolated capital cities and misgovernance: Theory and evidence (NBER working paper 19028). National Bureau of Economic Research,. https://doi.org/10.3386/w19028

Carpenter, S. (2010). A study of content diversity in online citizen journalism and online newspaper articles. New Media & Society. 12(7) 1064-1084. https://doi.org/10.1177/1461444809348772

Chan, J., Ghose, A. (2014). Internet’s dirty secret: Assessing the impact of online intermediaries on HIV transmission, MIS Quarterly, 38(4), 955-976. https://doi.org/10.25300/misq/2014 38.4.01

Chan, J., Mojumder, P., Ghose, A. (2019). The digital Sin City: An empirical study of Craigslist’s impact on prostitution trends. Information Systems Research, 30(1), 219-238. https://doi.org 10.1287/isre.2018.0799

Cho, D., Smith, M. D., & Zentner, A. (2016). Internet adoption and the survival of print newspapers: A country-level examination. Information Economics and Policy, 37, 13-19. https://doi.org/ 10.1016/j.infoecopol.2016.10.001

Claussen, J., Ferreira, P., Grad, T., Sen, A. (2021). (How) does UGC impact professionals? Evidence from local news. SSRN Electronic Journal. http://dx.doi.org/10.2139/ssrn.3834570

Clemons, E. K., Gu, B., & Lang, K. R. (2002). Newly vulnerable markets in an age of pure information products: An analysis of online music and online news. Journal of Management Information Systems, 19(3), 17-41. https://doi.org/10.1080 07421222.2002.11045738

Cordis, A. S., & Milyo, J. (2016). Measuring public corruption in the United States: Evidence from administrative records of federal prosecutions. Public Integrity, 18(2), 127-148. https://doi.org 10.1080/10999922.2015.1111748

Cordis, A. S., & Warren, P. L. (2014). Sunshine as disinfectant: The effect of state Freedom of Information Act laws on public corruption. Journal of Public Economics, 115, 18-36. https:// doi.org/10.1016/j.jpubeco.2014.03.010

Coronel, S. (2010). Corruption and the watchdog role of the media. In P. Norris (Ed.). Public sentinel: News media and governance reform (pp. 111-136). World Bank.

Cui, R., Li, J., & Zhang, D. J. (2020). Reducing discrimination with reviews in the sharing economy: Evidence from field experiments on Airbnb. Management Science, 66(3), 1071-1094. https://doi.org/10.1287/mnsc.2018.3273

Dellarocas, C., Katona, Z., & Rand, W. (2013). Media, aggregators, and the link economy: Strategic hyperlink formation in content networks. Management Science, 59(10), 2360-2379. https://doi. org/10.1287/mnsc.2013.1710

Dewan, S., & Ramaprasad, J. (2012). Music blogging, online sampling, and the long tail. Information Systems Research, 23 (3- 2), 1056-1067. https://doi.org/10.1287/isre.1110.0405

Djourelova, M., Durante, R., Martin, G. (2021). The impact of online competition on local newspapers: Evidence from the introduction of Craigslist (CEPR discussion paper No. DP16130). SSRN. https://ssrn.com/abstract=3846243

Ettema, James S., and Theodore L. Glasser. (1998). Custodians of conscience: Investigative journalism and public virtue. Columbia University Press.

Gao, P., Lee, C., & Murphy, D. (2020). Financing dies in darkness? The impact of newspaper closures on public finance. Journal of Financial Economics, 135(2), 445-467. https://doi.org 10.1016/j.jfineco.2019.06.003

Gentzkow, M. (2014). Trading dollars for dollars: The price of attention online and offline. American Economic Review, 104(5), 481-488. https://doi.org/10.1257/aer.104.5.481

Gentzkow, M., Shapiro, J. M., & Sinkinson, M. (2011). The effect of newspaper entry and exit on electoral politics. American Economic Review, 101(7), 2980-3018. https://doi.org/10.1257/ aer.101.7.2980

George, L. M., & Waldfogel, J. (2006). The New York Times and the market for local newspapers. American Economic Review, 96 (1), 435-447. https://doi.org/10.1257/000282806776157551

Glaeser, E. L., & Saks, R. E. (2006). Corruption in America. Journal of Public Economics, 90(6-7), 1053-1072. https://doi.org/ 10.1016/j.jpubeco.2005.08.007

Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. Journal of Econometrics, 225(2), 254-277. https://doi.org/10.1016/j.jeconom.2021.03.014

Gopal, A., & Koka, B. R. (2009). Determinants of service quality in offshore software development outsourcing. In R. Hirscheim, A. Heinzl, J. Dibbern (Eds.), Information systems outsourcing: Enduring themes, global challenges, and process opportunities (pp. 497-523). Springer.

Greenwood, B. N., & Gopal, A. (2015). Research note—Tigerblood: Newspapers, blogs, and the founding of information technology firms. Information Systems Research, 26(4), 812-828. https://doi. org/10.1287/isre.2015.0603

Greenwood, B.N., Wattal, S. (2017). Show me the way to go home: An empirical investigation of ridesharing and motor vehicle fatalities. MIS Quarterly, 41(1), 163-187. https://doi.org/ 10.25300/misq/2017/41.1.08

Hamilton, J. (2016). Hybrid news practices. In A. Hermida, C. W. Anderson, D. Domingo, & T. Witschge (Eds.), The SAGE handbook of digital journalism (pp. 164-178). SAGE.

Hayes, D., & Lawless, J. L. (2021). News hole: The demise of local journalism and political engagement. Cambridge University Press.

Hindman, E. B. (2008). Black eye: The ethics of CBS News and the National Guard documents. Journal of Mass Media Ethics, 23(2), 90-109. https://doi.org/10.1080/08900520801909202

Hindman, M. (2011). Less of the same: The lack of local news on the internet. Federal Communications Commission. https://docs.fcc. gov/public/attachments/DOC-307476A1.pdf

Hirano, S., & Snyder Jr, J. M. (2014). Primary elections and the quality of elected officials. Quarterly Journal of Political Science, 9(4), 473-500. http://doi.org/10.1561/100.00013096

Horton, J.J. (2015). The tragedy of your upstairs neighbors: Is the Airbnb negative externality internalized? arXiv. https://doi.org/ 10.48550/arXiv.1611.05688

Jiang, J. X., & Kong, J. (2023). Green dies in darkness? Environmental externalities of newspaper closures. Review of Accounting Studies. https://doi.org/10.1007/s11142-023-09786-5

Kim, A., & Dennis, A. R. (2019). Says who? The effects of presentation format and source rating on fake news in social

media. MIS Quarterly, 43(3), 1025-1039. https://doi.org/ 10.25300/misq/2019/15188

Kim, A., Moravec, P. L., & Dennis, A. R. (2019). Combating fake news on social media with source ratings: The effects of user and expert reputation ratings. Journal of Management Information Systems, 36(3), 931-968. https://doi.org/10.1080/07421222. 2019.1628921

Kim, K., & Hann, I. H. (2019). Crowdfunding and the democratization of access to capital—An illusion? Evidence from housing prices. Information Systems Research, 30(1), 276- 290. https://doi.org/10.1287/isre.2018.0802

Kitchens, B., Johnson, S. L., & Gray, P. (2020). Understanding echo chambers and filter bubbles: The impact of social media on diversification and partisan shifts in news consumption. MIS Quarterly, 44(4). https://doi.org/10.25300/misq/2020/16371

Lanosga, G., & Houston, B. (2017). Spotlight: Journalists assess investigative reporting and its status in society. Journalism Practice, 11(9), 1101-1120. https://doi.org/10.1080/17512786. 2016.1228472

Larreguy, H., Marshall, J., & Snyder Jr, J. M. (2020). Publicising malfeasance: When the local media structure facilitates electoral accountability in Mexico. The Economic Journal, 130(631), 2291-2327. https://doi.org/10.1093/ej/ueaa046

Lin, M., Sias, R. W., & Wei, Z. (2023). Experts vs. nonexperts in online crowdfunding markets. MIS Quarterly, 47(1), 97-126. https://doi.org/10.25300/misq/2022/17321

Liu, J., & Bharadwaj, A. (2020). Drug abuse and the internet: Evidence from Craigslist. Management Science, 66(5), 2040- 2049. https://doi.org/10.1287/mnsc.2019.3479

Liu, M., Brynjolfsson, E., & Dowlatabadi, J. (2021). Do digital platforms reduce moral hazard? The case of Uber and taxis. Management Science, 67(8), 4665-4685. https://doi.org/10.1287/ mnsc.2020.3721

Lu, K., Wei, Z., & Chan, T. Y. (2022). Information asymmetry among investors and strategic bidding in peer-to-peer lending. Information Systems Research, 33(3), 824-845. https://doi.org 10.1287/isre.2021.1084

Lucas Jr, H., Agarwal, R., Clemons, E. K., El Sawy, O. A., & Weber, B. (2013). Impactful research on transformational information technology: An opportunity to inform new audiences. MIS Quarterly, 37(2), 371-382. https://doi.org/10.25300/misq/2013/ 37.2.03

Mahone J. & Napoli, P. (2020,). Hundreds of hyperpartisan sites are masquerading as local news. This map shows if there’s one near you. Nieman Lab. https://www.niemanlab.org/2020/07/ hundreds-of-hyperpartisan-sites-are-masquerading-as-localnews-this-map-shows-if-theres-one-near-you/

Mauro, P. (1995). Corruption and growth. The Quarterly Journal of Economics. 110(3), 681-712. https://doi.org/10.2307/2946696

Meier, K. J., & Holbrook, T. M. (1992). “I seen my opportunities and I took’em:” Political corruption in the American states. The Journal of Politics, 54(1), 135-155. https://doi.org/10.2307/ 2131647

Miller, J. (2018). News deserts: No news is bad news. In Manhattan Institute (Ed.), Urban policy 2018 (pp. 59-76). Manhattan Institute. https://media4.manhattan-institute.org/sites/default/ files/MI\_Urban\_Policy\_2018.pdf#page=71

Miranda, S. M., Young, A., Yetgin, E. (2016). Are social media emancipatory or hegemonic? Societal effects of mass media

digitization in the case of the SOPA discourse. MIS Quarterly, 40 (2), 303-329. https://doi.org/10.25300/misq/2016/40.2.02

Olken, B. A. (2009). Corruption perceptions vs. corruption reality. Journal of Public Economics, 93(7-8), 950-964. https://doi.org/ 10.1016/j.jpubeco.2009.03.001

Ozer, G. T., Greenwood, B., & Gopal, A. (2019). Digital platforms and women’s health: An analysis of peer-to-peer lending and abortion rates. In Academy of Management Proceedings. https://doi.org/10.5465/AMBPP.2019.18171abstract

Park, J., Pang, M. S., Kim, J., & Lee, B. (2021). The deterrent effect of ride-sharing on sexual assault and investigation of situational contingencies. Information Systems Research, 32(2), 497-516. https://doi.org/10.1287/isre.2020.0978

Park, K., Seamans, R., Zhu, F. (2018). Multi-homing and platform strategies: Historical evidence from the US newspaper industry (Harvard Business School Technology & Operations Management Unit working paper No. 18-032). SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3048348

Peterson, E. (2021). Paper cuts: How reporting resources affect political news coverage. American Journal of Political Science, 65(2), 443-459. https://doi.org/10.1111/ajps.12560

Rhue, L., Clark, J. (2022). Who are you and what are you selling? Creator-based and product-based racial cues in crowdfunding. MIS Quarterly, 46(4), 2229-2260. https://doi.org/10.25300/ misq/2022/15214

Richey, S. (2010). The impact of corruption on social trust. American Politics Research, 38(4), 676-690. https://doi.org/10.1177/ 1532673X09341531

Robinson, J. P., & Davis, D. K. (1990). Television news and the informed public: An information-processing approach. Journal of Communication, 40(3), 106-119. https://doi.org/10.1111/ j.1460-2466.1990.tb02273.x

Seamans, R., & Zhu, F. (2014). Responses to entry in multi-sided markets: The impact of Craigslist on local newspapers. Management Science, 60(2), 476-493. https://doi.org/10.1287/ mnsc.2013.1785

Snyder Jr, J. M., & Strömberg, D. (2010). Press coverage and political accountability. Journal of Political Economy, 118(2), 355-408. https://doi.org/10.1086/652903

Szerman, C. (2023). The employee costs of corporate debarment in public procurement. American Economic Journal: Applied Economics, 15(1), 411-441. https://doi.org/10.1257/app.2020 0669

Trussler, M. (2022). The effects of high-information environments on legislative behavior in the US House of Representatives. Legislative Studies Quarterly, 47(1), 95-126. https://doi.org/ 10.1111/lsq.12325

Turkel, E., Saha, A., Owen, R. C., Martin, G. J., & Vasserman, S. (2021). A method for measuring investigative journalism in local newspapers. Proceedings of the National Academy of Sciences, 118 (30), Article e2105155118. https://doi.org/10.1073/pnas. 2105155118

Usher, N., & Kim-Leffingwell, S. (2023). How Loud does the watchdog bark? A reconsideration of losing local journalism,

news nonprofits, and political corruption. The International Journal of Press/Politics. https://doi.org/10.1177/1940161223 1186939

Wang, H., & Overby, E. M. (2022). How does online lending influence bankruptcy filings? Management Science, 68(5), 3309- 3329. https://doi.org/10.1287/mnsc.2021.4045

Wang, S., Pang, M. S., & Pavlou, P. A. (2021). Cure or poison? Identity verification and the posting of fake news on social media. Journal of Management Information Systems, 38(4), 1011-1038. https://doi.org/10.1080/07421222.2021.1990615

Wattal, S., Schuff, D., Mandviwalla, M., & Williams, C. B. (2010). Web 2.0 and politics: the 2008 US presidential election and an epolitics research agenda. MIS Quarterly, 34(4), 669-688. https://doi.org/10.2307/25750700

Wood, M. L., Nelson, M. R., Cho, J., & Yaros, R. A. (2004). Tonight’s top story: Commercial content in television news. Journalism & Mass Communication Quarterly, 81(4), 807-822. https://doi.org/10.1177/107769900408100406

Zervas, G., Proserpio, D., & Byers, J. W. (2017). The rise of the sharing economy: Estimating the impact of Airbnb on the hotel industry. Journal of Marketing Research, 54(5), 687-705. https://doi.org/10.1509/jmr.15.0204

## About the Authors

Ted Matherly is a visiting assistant professor of marketing at Northeastern University’s D’Amore-McKim School of Business. His research lies at the intersection of digital platforms and signaling, examining how these platforms facilitate different forms of communications, with a focus on the effects of digitization for marketers and society. His work has appeared in the Journal of Marketing, the Journal of Marketing Research, and the International Journal of Research in Marketing. He received his Ph.D. in Marketing from the University of Maryland. ORCID: 0000-0002-8628-1004

Brad N. Greenwood is the Dean’s Distinguished Professor of Business at George Mason University. His research examines the intended and unintended consequence of innovation and how access to the resulting information affects welfare at the interface between business, technology, and social issues, notably in the contexts of healthcare and entrepreneurship. He is an associate editor at Management Science and MIS Quarterly. He received his bachelor’s degree in information technology and management information systems from Rensselaer Polytechnic Institute. Dr. Greenwood also received an M.B.A. from the University of Notre Dame, a master’s of IT from Virginia Polytechnic Institute; a juris master’s from the Antonin Scalia Law School, and a Ph.D. from the University of Maryland, College Park. He is currently an L.L.M. student at George Mason University’s Antonin Scalia Law School. ORCID: 0000-0002-0772-7814
