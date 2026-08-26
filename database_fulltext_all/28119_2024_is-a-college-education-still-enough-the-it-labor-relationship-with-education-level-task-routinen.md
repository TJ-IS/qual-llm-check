---
otero_id: 28119
otero_key: "GSM3CVDE"
title: "Is a College Education Still Enough? The IT-Labor Relationship with Education Level, Task Routineness, and Artificial Intelligence"
authors: "Dawei (David) Zhang; Gang Peng; Yuliang Yao; Tyson R. Browning"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0391"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Is a College Education Still Enough? The IT-Labor Relationship with Education Level, Task Routineness, and Artificial Intelligence

Dawei (David) Zhang,<sup>a,</sup>\* Gang Peng,<sup>b</sup> Yuliang Yao,<sup>c</sup> Tyson R. Browning<sup>d</sup>

<sup>a</sup> Department of Decision and Technology Analytics, College of Business, Lehigh University, Bethlehem, Pennsylvania 19015; <sup>b</sup> Department of Information Systems and Decision Sciences, College of Business and Economics, California State University, Fullerton, California 92831; <sup>c</sup> Alfred Lerner College of Business & Economics, University of Delaware, Newark, Delaware 19716; <sup>d</sup> Department of Information Systems and Supply Chain Management, Neeley School of Business, Texas Christian University, Fort Worth, Texas 76129 \*Corresponding author

Contact: daz215@lehigh.edu, https://orcid.org/0000-0002-6688-2961 (DDZ); gpeng@fullerton.edu, https://orcid.org/0000-0001-8773-002X (GP); oyao@udel.edu, https://orcid.org/0000-0001-9384-6707 (YY); t.browning@tcu.edu, https://orcid.org/0000-0002-9089-1403 (TRB)

Received: July 28, 2021 Revised: September 10, 2022; April 8, 2023; May 5, 2023 Accepted: May 11, 2023 Published Online in Articles in Advance: August 10, 2023

https://doi.org/10.1287/isre.2021.0391

Copyright: © 2023 INFORMS

Abstract. Although information technology (IT) is increasingly replacing human labor, the IT-labor relationship is more nuanced than it appears. We examine the IT-labor relationship in terms of various levels of education, intensities of routine tasks, and exposure to artificial intelligence (AI). Making use of an industry-level data set covering 60 U.S. industries from 1998 to 2013, we adopt an innovative measure of elasticity of substitution that enables us to capture the asymmetric price impact between IT and labor. Our findings indicate that IT generally complements high-education labor (master’s degree or above), while substituting for low-education labor (high school degree or below). For middle-education labor (bachelor’s or associate’s degree), however, the IT-labor relationship is more nuanced: They are complements in non-routine-intensive industries, but substitutes in routine-intensive industries. We also find that IT is a complement (substitute) with high-education labor in industries with lower (higher) AI exposure and remains a net substitute for low- and middle-education labor, regardless of their AI exposure. Our findings suggest that even college-educated labor has now become susceptible to IT displacement, whereas labor with graduate education largely remains a strong complement to IT (with an exception in high-AI-exposure industries). Theoretical and policy implications are discussed.

History: Eric Zheng, Senior Editor.

Funding: Tyson Browning is grateful for support from a Neeley School of Business Research Excellence Award.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0391.

Keywords: information technology • human labor • college education • elasticity of substitution • task routineness • artificial intelligence

Labor will become less and less important … More workers will be replaced by machines. I do not see that new industries can employ everybody who wants a job. (Leontief 1952)

## 1. Introduction

The past few decades have witnessed rapid growth in the use of information technology (IT)—broadly defined as computers and related digital communication technology (Brynjolfsson and Hitt 2000). According to the Bureau of Economic Analysis, the average IT capital per industry in the United States has increased 13.2% annually during 1987–2015, from \$7.34 billion to \$44.17 billion. Globally, IT investment was projected to reach \$4.4 trillion in 2022, a 4% increase from 2021 (Costello 2019). Two main forces are believed to be behind this rapid growth in IT investment. One is the constant improvement in the price-performance ratio for IT, which incentivizes firms to take advantage of cheaper, but more productive, IT (Bureau of Labor Statistics 2015); the other is the gradual increase in labor costs (Bureau of Labor Statistics 2020). As IT becomes cheaper and more productive, while labor becomes more expensive, profit-maximizing firms tend to invest more in IT to replace human labor (Brynjolfsson and McAfee 2012). As a result, a growing number of jobs have been replaced by IT. Recent studies projected that 36 million further U.S. jobs will be disrupted, as they could soon be performed by machines equipped with current technologies (Associated Press 2019), and that 6%–33% of jobs are highly automatable and, thus, susceptible to IT displacement across 32 Organisation for Economic Co-Operation and Development (OECD) countries (Nedelkoska and Quintini 2018). According to a recent report by Goldman Sachs (2023), shifts in workflows triggered by advances in artificial intelligence (AI) systems could expose the equivalent of 300 million full-time jobs to automation within the next 10 years.

Although industry statistics suggest that IT is increasingly displacing labor, research shows that the IT-labor relationship is more nuanced than it appears. On one hand, some studies showed that IT substitutes for human labor in general; that is, the input of IT reduces the input of human labor (Dewan and Min 1997, Hitt and Snir 1999, Chwelos et al. 2010, Zhang et al. 2015). On the other hand, other studies have shown that IT may complement skilled human labor with higher education levels (Bound and Johnson 1992, Acemoglu 1998, Goldin and Katz 1998), but substitute for labor performing routine tasks (Autor et al. 2003, Goos et al. 2014).

The mixed evidence demonstrates that the relationship between IT and labor is not straightforward, but may depend on the education levels of labor, routineness of job tasks, and technology advancement, such as AI. Not all workers are susceptible to displacement by IT; workers of different education levels may interact with IT differently. Although prior studies have argued that technology advancement favors college-educated labor, they do not distinguish between a bachelor’s degree and a graduate degree (Goldin and Katz 1998, Bresnahan et al. 2002, Autor et al. 2003). Increasing evidence has shown that technology advancement in recent decades, such as AI, has automated even nonroutine tasks that used to be performed by college-educated workers (Selingo 2017, Tarrant 2023). Today, AI has been extensively applied in various scenarios, such as selfdriving cars, drones, robotics, and generating text and software code, and is quickly replacing humans in performing not only routine, but also some nonroutine tasks. Some scientists and business leaders have even concluded that all human jobs would disappear in less than 20 years (Brown 2016), and full development of AI could spell the end of the human race, because humans are limited by slow biological evolution and could not compete with AI (Cellan-Jones 2014, Sainato 2015). Others expect that AI will increase productivity by removing the drudgery of some office jobs and thereby freeing up time for humans to engage in higher-contact and critical thought activities.

In this paper, we distinguish between college and graduate degrees in the roles of education levels and examine the relationships between IT and labor of different education levels at the industry level and how this relationship is moderated by task routineness and exposure to AI. We stratify labor into three education levels and divide our sample of industries into subsamples: routine-intensive and non-routine-intensive, and high and low AI exposure. We then estimate the IT-labor relationship using a combination of Allen elasticity of substitution (AES) and Morishima elasticity of substitution (MES) for each education level in each industry subsample. Our key findings are as follows. First, IT complements high-education labor (master’s degree or above), substitutes for low-education labor (high school degree or below), and, contrary to prior findings and conventional wisdom, substitutes for middle-education labor (bachelor’s or associate’s degree) in general. Second, although these findings hold for both high- and low-education labor in both routine-intensive and nonroutine-intensive industries, IT complements middleeducation labor in non-routine-intensive industries, while substituting for it in routine-intensive ones. Third, as IT becomes cheaper, its substitution effect is strongest for low-education labor employed by non-routineintensive industries. As labor prices go up, the substitution by IT is strongest for middle-education labor in routine-intensive industries, and the complementarity of IT is strongest for high-education labor in nonroutine-intensive industries. Fourth, we find that IT is complementary to high-education labor in industries with lower AI exposure, but a net substitute for low and middle-education labor, regardless of their AI expo sure. These results suggest that although labor with a graduate education largely remains a complement to IT, this complementarity may gradually diminish and convert to a substitution, as evidenced in industries with relatively more exposure to AI.

Our study makes a number of important contributions. First, we contribute to the literature by studying the role of education on the IT-labor relationship with more granular measures of education levels, revealing novel findings with more recent data. Although the role of education on the IT-labor relationship has been examined before (Bound and Johnson 1992, Acemoglu 1998, Goldin and Katz 1998, Bresnahan et al. 2002, Autor et al. 2003, Moshiri and Simpson 2011), few prior studies have distinguished the IT and labor relationships between a bachelor’s degree and a graduate degree, and the findings are inconsistent. For example, Autor et al. (2003) and Goldin and Katz (1998) concluded that technology favors college-educated workers, but they did not distinguish between a bachelor’s degree and a graduate degree. On the other hand, several other studies (Autor et al. 2006, Goos and Manning 2007, Autor et al. 2008, Goos et al. 2009, 2014) found that the labor market has become polarized, such that employment of high- and lowskilled workers had increased, whereas that of middleskilled workers had decreased, as a result of increasing IT investment. Our study expands on these studies with finer granularity in education level to distinguish between undergraduate and graduate degrees and shows that, counter to the findings in prior research, the only “winner” is the graduate education group, as IT has now become a net substitute for both middle- and loweducation labor groups in general.

Second, by collecting occupation-level data and classifying industries into routine- and non-routine-intensive, we are able to explore the mechanisms by which education influences the relationship between IT and human labor. Whereas the labor performing routine tasks is more susceptible to IT substitution, the labor performing nonroutine tasks is more likely to complement IT. Our findings show this mechanism at work for high-education labor, as well as low-education labor. What is most interesting regards the labor of middlelevel education (bachelor’s or associate’s degree): We demonstrate that IT and labor of middle-level education are complements in non-routine-intensive industries, but substitutes in routine-intensive industries. These findings are novel and contribute to the literature on the IT-labor relationship by conceptualizing and testing it at different education levels and across routine-intensive and non-routine-intensive industries.

Third, our findings that IT substitutes with labor regardless of education level in high-AI-exposure industries are novel, as they reveal nuanced differences in how AI may affect the IT-labor relationship when compared with the impact of task routineness. This finding also alarms policy makers regarding the potentially negative impact of technological advancement on labor demand at the macro level. To the best of our knowledge, we are among the first to study how AI moderates the relationship between technology and human labor, particularly those with a high education level.

## 2. Literature and Theory

## 2.1. The Relationship Between IT and Labor

Firms use factors of production as inputs for the creation of a good or service. Input factors come in different forms, primarily as labor and capital. To investigate the impact of IT on production output, researchers have divided capital into IT capital and non-IT capital (Brynjolfsson and Hitt 1996, Dewan and Min 1997). During the production process, firms minimize cost by adjusting the amounts of input factors according to their price changes (Varian 1992). Two input factors are considered to be complements (substitutes) if an increase in the input of one factor increases (decreases) the input of another factor (Allen 1938). The metric of elasticity of substitution (ES) captures this relationship between input factors.

Our research relates primarily to the IT-labor interaction research stream at the aggregate level (e.g., industry or firm levels). Several studies in the information systems (IS) literature have applied the ES approach (Dewan and Min 1997, Hitt and Snir 1999, Chwelos et al. 2010, Zhang et al. 2015), whereas others have examined how IT affects the marginal contribution of labor (Francalanci and Galal 1998, Bresnahan et al. 2002, Moshiri and Simpson 2011). However, these studies’ findings are inconsistent, having found both substitutive and complementary relationships between IT and labor. Several reasons may have led to this inconsistency. First, studies from the IS literature have typically considered human labor as a monolithic whole and ignored the possible impact of IT on different types of labor (Dewan and Min 1997, Zhang et al. 2015). Hence, these studies estimate the relationship between IT and labor in general. Second, almost all prio studies using the ES approach have applied only the AES, which has critical drawbacks, such as not being informative beyond the cross-price elasticity of demand and misleading in analyses with more than two inputs (Blackorby and Russell 1989). As a result, another ES approach, the MES (Morishima 1967, Zhang et al. 2015), was proposed to overcome these drawbacks and measure the degree of substitution/complementarity more accurately. In Table 1, we summarize prior studies from the IS literature that used the ES approach. In this study, we propose a novel approach to assess the IT-labor relationship using both AES and MES.

## 2.2. IT, Education Levels, and Task Routineness

Although prior studies using the ES approach have found IT and labor to be substitutes in general, a stream of literature in economics has also examined the relationship between technology and employment and found that the relationships may depend on labor skills (i.e., skill-biased technological change, SBTC) or the routineness of the tasks performed (routine-biased technological change, RBTC). A detailed summary of literature on SBTC and RBTC is provided in Online Appendix A.

The central theme of SBTC is that IT and skilled labor are complementary: Higher-skilled workers make greater use of IT and have, thus, witnessed the fastest growth in employment (Bound and Johnson 1992, Goldin and Katz 1998). This complementarity is typically manifested through a positive correlation between IT investment and a more educated labor force, particularly those with a college degree (Autor et al. 2003). For example, Bartel and Lichtenberg (1987) found that firms introducing new technologies hired more skilled workers. Krueger (1993) found that the use of computers at work was associated with higher education levels of the workers. Based on an analytical model in which skill assignment is endogenous, Acemoglu and Autor (2011) showed that the relationship between technological change and labor depends on worker skill level and the nature of the technologies. Bresnahan et al. (2002) and Moshiri and Simpson (2011) showed that IT capital is complementary to workers with higher educational attainment, which gives them a comparative advantage in performing nonroutine tasks. Autor and Dorn (2013) also found that computerization has substituted for low-skill workers performing routine tasks, while complementing highly educated workers performing creative and problemsolving tasks.

The relationship between IT and labor also depends on the routineness of the tasks, as advocated by RBTC (Goos et al. 2014). According to RBTC, tasks can be defined as routine or nonroutine (Autor et al. 2003). Rou tine tasks follow a limited and well-defined set of activities and can be accomplished by following explicit rules, whereas nonroutine tasks are not well defined and usu ally exhibit a higher number of exceptions and lower task analyzability. Examples of routine tasks include manual assembly lines and cognitive clerical tasks; examples of nonroutine tasks include a manager’s job for analyzing complex situations and using subjective decision making, which typically cannot be performed entirely through predetermined rules (Atasoy et al. 2016). Routine tasks involve more unvarying repetition of a process at regular time intervals and, thus, are easier to manage and automate via prescribed algorithms. Nonroutine tasks require more creativity and problem-solving, which are much less susceptible to computerization (Autor and Dorn 2013). Overall, RBTC predicts that, because of the different impacts of IT on routine versus nonroutine tasks, technological advancement would displace workers performing routine tasks, while driving up demand for those performing nonroutine tasks (Autor et al. 2006, Goos and Manning 2007, Autor et al. 2008, Goos et al. 2009, 2014, Michaels et al. 2014).

Table 
1. Summary of Literature on the IT-Labor Relationship Using an ES Approach

<table><tr><td>Studies</td><td>Method</td><td>Time period</td><td>Data source for IT</td><td>Measure of IT</td><td>Measure of labor</td><td>Key findings</td><td>IT vs. labor</td></tr><tr><td>Dewan and Min (1997)</td><td>AES</td><td>1988–1992</td><td>IDG/ComputerWorld</td><td>Computer capital and IS labor expenses</td><td>Total labor expense net of IS labor expense</td><td>IT is a perfect substitute for both non-IT capital and labor in all sectors of the economy.</td><td>Substitutes</td></tr><tr><td>Hitt and Snir (1999)</td><td>AES</td><td>1987–1994</td><td>Computer Intelligence Infocorp database</td><td>IT stock</td><td>Labor expense</td><td>IT and non-IT capital are substitutes in traditional organizations, whereas they are complements in modern organizations; IT and labor are consistently substitutes across all organizations.</td><td>Substitutes</td></tr><tr><td>Chwelos et al. (2010)</td><td>AES</td><td>1987–1998</td><td>Computer Intelligence database</td><td>Hardware</td><td>Labor expense</td><td>IT and non-IT capital are complements, whereas IT and labor are substitutes.</td><td>Substitutes</td></tr><tr><td>Zhang et al. (2015)</td><td>AES and MES</td><td>1998–2009</td><td>BLS</td><td>Hardware and software</td><td>Labor hours</td><td>IT is a substitute for both non-IT capital and labor.</td><td>Substitutes</td></tr></table>

## 2.3. The Impact of AI on Labor

In recent years, increasingly more attention has been paid to the impact of AI on work and human labor (Raj and Seamans 2019, Iansiti and Lakhani 2020, Jia et al. 2020). Goldman Sachs (2023) economists estimated that “roughly two-thirds of U.S. occupations are exposed to some degree of automation by $\mathrm { A } \hat { \mathrm { I } } . { } ^ { \prime \prime }$ Jia et al. (2020) con ducted a firm-level field experiment and found that AI complemented human managers who provided training to employees. In particular, transformational leadership benefits more than transactional leadership from AI assistance in creating greater value for the organization. Teodorescu et al. (2021) explored the augmentation between human and machine learning (ML) applications and developed a theoretical framework of AI aug mentation. Through simulations, Sturm et al. (2021) showed that ML reduced an organization’s demand for using human explorative learning to uncover new ideas and that humans need to make adjustments to ML systems in order to facilitate organizational learning. Jussu pow et al. (2021) explored how AI advice influences physicians’ decision-making process and found that correct AI advice improved physicians’ accuracy, although this decision augmentation could only be successful if decision makers drew on both self-judgment and AI advice. Fu¨ gener et al. (2022, p. 678) found through experi ments that the human-AI collaboration could improve performance “only when the AI delegates work to humans but not when humans delegate work to the $\mathrm { A I . \Omega } ^ { \prime \prime }$ Lysyakov and Viswanathan (2022) examined designers responses to the introduction of an AI system for simple logo designs on a crowdsourcing design platform, finding that the more capable designers were able to avoid competition with the AI by adding more complexity and emotional content in their designs. Through a field experiment, Luo et al. (2019, p. 938) found that chatbots were “as effective as proficient workers and four times more effective than inexperienced workers in engendering customer purchases,” indicating a potentially substitutive role of this AI application. Brynjolfsson and Mitchell (2017) discussed the impact of ML on the workforce, claiming that ML has become the new “general purpose technology” just like electricity and that it is unclear whether the net effect of ML on labor demand would be positive or negative. Webb (2020) found that workers with lower levels of education were less exposed to AI compared with those with higher levels of education, such as a master’s degree, and that the most AI-exposed jobs were those involving high levels of education and accumulated experience. Using establishment-level data from 2010 to 2018, Acemoglu et al. (2022) studied the impact of AI on labor markets, finding that the adoption of AI was associated with reduced hiring for non-AI positions, as well as a change in job requirements. However, AI has also created new jobs, such as the “prompt engineers” required by firms to utilize AI systems like ChatGPT most effectively (Snow 2023). Indeed, will AI continue the trend that “more than 85% of employment growth over the last 80 years is explained by the technologydriven creation of new positions” (Goldman Sachs 2023)?

Prior research on the impact of AI on labor demand has primarily been at the task, individual, or establishment level. Our research provides timely industry-level empirical evidence with further reference to labor of various education levels and adds to this important and rapidly growing literature that studies the impact of AI on the human workforce.

## 2.4. Research Framework

Labor can be differentiated by education level, which may interact with IT in different patterns. Education has a profound impact on individuals’ cognitive skills, analytical abilities, capacity to perform specific tasks, social capabilities, and health, among other things (Lochner and Moretti 2004, Moretti 2004, Hout 2012), thereby increasing their productivity in the labor market (Schultz 1961, Becker 1962). In this paper, we define low education as a high school degree or below, middle education as a bachelor’s or associate’s (college or undergraduate) degree, and high education as a master’s or professional (graduate) degree or above. Whereas many prior studies lump undergraduate and graduate education together, we intentionally separate them to determine whether undergraduate education is still enough to keep workers jobs from being displaced.

In SBTC, the IT-labor relationship is examined through the effects of IT on labor of different skills or education levels, whereas RBTC shifts the focus to the routineness of tasks performed by labor. However, a closer examination of the IT-labor interaction reveals that the impacts of SBTC and RBTC are dynamic and intertwined. This process is shown in Table 2, where the vertical arrows represent stocks of low-, middle-, and high-education labor. Workers of higher (lower) education levels are more likely to conduct nonroutine (routine) tasks. The upward arrow represents the stock of routine tasks and their displacement potentials by IT at each education level. Overall, low-education labor is most likely to perform routine tasks, because they take the largest share of employment, and their job content is more routine, compared with the other two groups (Acemoglu and Autor 2011, Richards and Terkanian 2013). Yet, advancing technology also creates new jobs, which are more likely to be nonroutine. The downward arrow represents the stock of nonroutine tasks and the amount of IT-induced job creation at each education level. Here, the stock of jobs demanding a high education takes the largest share, whereas that demanding a low education takes the smallest share. The horizontal arrows in Table 2 indicate that, although nonroutine tasks exist at all three education levels, the nonroutine tasks can become increasingly routinized as IT continues to advance. However, the routinization does not happen equally across educational levels: A greater extent of routinization occurs with the tasks at the lower education levels. The above process shows a pattern of RBTC. In addition, it is important to keep in mind that this process is continuous—as it happens, jobs at the low-education level are more likely to be displaced, followed by those at middle education and, lastly, high education. This is because lower education levels are more likely to be associated with routine tasks that are more likely to be displaced by IT and also with fewer jobs to be created by IT. Conceptually, if we encapsulate the RBTC process as depicted above, as technology continues to develop, the RBTC process is pushed upward along the education line, so that RBTC continues to take effect at higher levels of education. Overall, technology favors labor of higher education levels, displaying a pattern of SBTC. Thus, we see both RBTC and SBTC at work in this integrative view of the IT-labor relationship.

Table 2. (Color online) Research Framework

<table><tr><td>Education level</td><td>Routine tasks</td><td>Nonroutine tasks</td></tr><tr><td>High education (graduate or professional school)</td><td></td><td></td></tr><tr><td>Middle education (bachelor&#x27;s or associate&#x27;s degree)</td><td></td><td></td></tr><tr><td>Low education (high school or below)</td><td></td><td></td></tr></table>

Notes. The upward arrow represents the stock of routine tasks and their displacement potential by IT at each education level. The downward arrow represents the stock of nonroutine tasks and the amount of IT-induced job creation at each education level. The horizontal arrows represent task transformation from nonroutine to routine at each education level due to IT advancement and their width the potential for such transformation.

## 3. Hypothesis Development 3.1. IT, High-Education Labor, and Task Routineness

The technological change triggered by IT in recent decades has shifted labor demand toward more skilled workers, who are better prepared to participate in economic, political, and social activities and engage in the complex, technology-oriented dimensions of today’s economy (Goldin and Katz 1998). Highly educated employees are more likely to work on cognitive, nonroutine tasks, such as those typically performed by engineers, consultants, executives, and physicians (Manning 2004, Acemoglu and Autor 2011, Michaels et al. 2014, Beaudry et al. 2016). These tasks involve semistructured or unstructured problems and require expert thinking and complex communication, coordination, and integration, which are hard to program and delegate to computers. For example, the adoption of data analytics in business has triggered a large demand for data scientists in many companies across industries (Davenport 2006).

As purported by SBTC, education plays a critical role in increasing worker skills and affecting technology use. Education enhances one’s ability to receive, decode, and understand information, and more highly educated workers can distinguish more quickly between systematic and random elements of productivity (Bartel and Lichtenberg 1987). In general, high-education workers exhibit the following properties with respect to their capabilities. First, they not only have the skills to use existing technologies, but also are more flexible and adapt more readily to the introduction and implementation of new technologies (Bartel and Lichtenberg 1987). Second, high-education workers are more capable of applying new, risky technologies, innovating, and developing accurate mental models and effective strategies and plans to better adapt to a changing external reality (Krueger and Kumar 2004). Third, high-education workers with stronger cognitive abilities will be more prepared to perform complicated tasks and are well versed in multitasking. As a result, disproportionally more high-education employees work on cognitive, nonroutine tasks that are less susceptible to IT automation.

Furthermore, as shown in Table 2, the new job opportunities created by IT advancement are disproportionately more nonroutine tasks requiring high-education labor (Bresnahan et al. 2002). Therefore, we propose the following hypothesis:

Hypothesis 1(a). IT complements human labor of high education level in both routine-intensive and non-routineintensive industries.

## 3.2. IT, Low-Education Labor, and Task Routineness

Prior studies suggested that low-education labor was more likely to perform routine tasks, manual or cognitive, which are increasingly susceptible to IT substitution (Lewandowski et al. 2020). IT has been adopted mainly to automate routine tasks and, thus, has been a net substitute to low-education labor (Autor et al. 2003) for two reasons. First, task routineness lends itself to automation. Second, tasks that require low-education labor are the easiest to automate among all routine tasks because they require the fewest skills (Autor et al. 2003). For example, telephone operators were replaced by automatic switching devices, and drive-through tellers were replaced by automated teller machines (Frey and Osborne 2017). Other examples include factory assemblers, elevator operators, grocery store cashiers, etc. This substitution pattern has been reported in prior studies (Hunt and Hunt 1983, Berndt et al. 1992, Autor et al. 1998, Lewis 2011).

As shown in Table 2, not all tasks performed by loweducation labor are routine, such as nonroutine manual tasks (Autor et al. 2003). With rapid advancement in IT capabilities in areas such as processing, communication, storage, and application algorithms, these nonroutine manual tasks are increasingly routinized and automated (Autor et al. 2003). For example, janitors and house cleaners, two typical types of low-education workers, were considered extremely difficult to automate, but recent inventions such as household robots are increasingly adopted to do household chores (Levy and Murnane 2004). Similarly, jobs by waiters and bartenders were hard to automate, but today, more and more restaurants and fast-food chains are using self-service kiosks (Frey and Osborne 2017). Driving used to be considered nonroutine because it requires complex coordination and information processing (Levy and Murnane 2004), but nowadays, with the advancement of both IT hardware and software, selfdriving cars, as piloted by Tesla, Waymo, Zoox, and many other companies, are quickly becoming reality. Therefore, we propose the following hypothesis:

Hypothesis 1(b). IT substitutes for human labor of low education level in both routine-intensive and non-routineintensive industries.

## 3.3. IT, Middle-Education Labor, and Task Routineness

Although prior research has found that technology favors college-educated workers (Bound and Johnson 1992, Goldin and Katz 1998), with the technological advancements and gradual routinization of tasks over time, the impact of IT on middle-education labor is less clear because, as shown in Table 2, middle-education workers perform a mix of routine and nonroutine tasks. We therefore posit that the effect of IT on middleeducation labor depends on the routine intensity of industries.

As the capability of IT continues to advance, more of the nonroutine tasks performed by middle-education workers are being routinized, thus subjecting them to automation (Frey and Osborne 2017). For example, the introduction of various kinds of accounting software, which has automated many data-collection and -processing tasks, has corresponded with a fast decline in bookkeeping jobs (Stebbins and Sauter 2016). Similarly, the number of bank clerks, a typical type of middle-education worker, has declined with the wide adoption of computer-based tools. Because routine tasks follow rule-based logic, they can be easily programmed and delegated to computers and machines. Lu et al. (2018) found that the staffing level for licensed nurses, a middle-education labor that requires a minimum of an associate’s degree, decreased by 5.8% in high-end nursing homes that are equipped with more IT, but increased by 7.6% in low-end homes that are equipped with less automation technology.

Recent research in AI, robotics, and cognitive science documented that even the routine tasks performed by middle-education labor can be programmed and delegated to computers and machines (Pinker 1994, Ford 2013). Over the past few decades, with the sharp drop in computer costs, more firms have deployed technologies to replace middle-education labor because IT can perform the same types of tasks better, faster, and cheaper (Brynjolfsson and Hitt 2000). Increased IT investment is more likely to substitute for middle-education labor in routine-intensive industries.

Yet, some of the tasks performed by middle-education labor remain nonroutine, making them difficult to automate, particularly for those in non-routine-intensive industries (Frey and Osborne 2017). These jobs include business managers, financial analysts, engineers, pharmacists, news editors, and nurse practitioners, and most of them require a higher level of analytical or interactive skills, which are highly demanded in non-routineintensive industries (Autor et al. 2003, Frey and Osborne 2017). As argued earlier, when jobs are not automated, increased IT investment requires more labor input. Therefore, in non-routine-intensive industries, IT and middle education labor tend to be complementary.

As shown in Table 2, not only can IT displace workers, but it can also create new job opportunities, including those for middle-education labor (Acemoglu and Restrepo 2019). For example, in recent decades, many jobs have been created due to the advancement of IT, such as software coders, system analysts, web develo pers, online marketers, and database administrators (Manyika et al. 2017). Many of them are IT-related jobs that require college degrees. The concurrent growth between IT investment and these middle-education-level jobs suggests their complementarity in non-routineintensive industries. Therefore, we expect different relationships between IT and middle-education labor, depending on the routine intensity of an industry.

Hypothesis 2(a). IT substitutes for human labor of mid dle-education level in routine-intensive industries.

Hypothesis 2(b). IT complements human labor of middle education level in non-routine-intensive industries

## 4. Methods and Data 4.1. Estimation Methods

In a production process, two input factors are considered complements (substitutes) if an increase in one increases (decreases) the input of the other (Allen 1938). This tradeoff between input factors is captured through the metric of ES, which has been adopted by prior IS studies (see Table 1). Estimating ES requires a production function that accounts for the tradeoff between input factors for a constant level of output. ES takes any price changes of input factors into account, which is particularly attractive, given the precipitous drop in the price of computing equipment over time (Ba and Nault 2017) and firms’ desire to minimize cost by adjusting input factors according to their price changes (Varian 1992). We treat IT and labor as input factors in the production functions and estimate the ES between them.

For an n-input production function, Y � f (x), where Y is the output and x is the vector of inputs. For constant output, the rate at which input i can substitute for input j is described as the marginal rate of technical substitution (MRTS):

$$
\partial x _ {i} / \partial x _ {j} = - \frac {\partial f (x) / \partial x _ {j}}{\partial f (x) / \partial x _ {i}} = - f _ {j} / f _ {i}.
$$

However, the MRTS does not incorporate the impact of prices, so we use the ES, defined as the percentage change in the input ratio in response to the percentage change in the MRTS (Hicks 1932):

$$
\sigma = \frac {d (x _ {i} / x _ {j}) / [ x _ {i} / x _ {j} ]}{d (f _ {j} / f _ {i}) / [ f _ {j} / f _ {i} ]}.
$$

The Allen ES generalizes the ES to the n-factor case (Uzawa 1962). The AES between inputs i and j is given as:

$$
\sigma_ {i j} ^ {A} = \frac {\sum_ {i} x _ {i} f _ {i}}{x _ {i} x _ {j}} \frac {\mathbf {H _ {i j}}}{\mathbf {H}},\tag{1}
$$

where H is the bordered Hessian determinant of $f ( x )$ and $\mathbf { H } _ { \mathrm { i j } }$ is the cofactor associated with $f _ { i j } .$ . Inputs i and j are substitutes if $\sigma _ { i j } ^ { A } > 0 .$ , meaning that an increase in the price of j decreases the input quantity of ${ \mathrm { ~ ; ~ } } j ,$ but increases the input quantity of i. Inputs i and j are complements if $\sigma _ { i j } ^ { A } < 0$ . The AES measures the amount of change in one input factor due to a price change in another, holding output and all other input prices constant, which corresponds to what we test in this study.

The Morishima ES is constructed as:

$$
\sigma_ {i j} ^ {M} = \frac {f _ {j}}{x _ {i}} \frac {\mathbf {H _ {i j}}}{\mathbf {H}} - \frac {f _ {j}}{x _ {j}} \frac {\mathbf {H _ {j j}}}{\mathbf {H}},\tag{2}
$$

where $\sigma _ { i j } ^ { M }$ measures the change in input i relative to input j as a result of a price change in input j. When $\sigma _ { i j } ^ { M }$ $> 0 ,$ inputs i and j are Morishima substitutes, which is different from the standard definition of substitutes and means that an increase in the price of j increases the quantity ratio of input i over input j. Similarly, when $\bar { \sigma } _ { i j } ^ { M } < 0 ,$ inputs i and j are Morishima complements. The MES is asymmetric, so that $\sigma _ { i j } ^ { M } \neq \sigma _ { j i } ^ { M }$ . Therefore, the MES measures the change in the quantity ratio between two inputs when the price of one of the inputs is changing. The MES provides an important tool for assessing tradeoffs in the mix of inputs when input price changes differ so widely over time, as in the case of the sharply falling price of IT capital, in contrast to the steady increases in the prices of labor and other capital (Ba and Nault 2017). In contrast to the AES, the MES provides a substitution measure where the scale is meaningful, even when there are more than two input factors, and the measure differs depending on which price is changing (Blackorby and Russell 1989).

As shown by prior research, the AES can be expressed as $\sigma _ { i j } ^ { A } \propto \partial$ ln $x _ { i } / \partial$ ln p (Blackorby and Russell 1989) and the MES as $\dot { \sigma } _ { i j } ^ { M } = \dot { \partial } \ln [ x _ { i } / x _ { j } ] / \dot { \partial } \ln p _ { j }$ (Chambers 1988). In this paper, we use them jointly in determining the substitution/complementarity relationship between input factors and the strength of complementarity. Table 3 presents their joint interpretation, with mathematical proof provided in Online Appendix B. In Table 3, AES\_ij is the AES between inputs i and j, and MES\_ij is the MES between inputs i and j when the price of j changes. When the AES and MES are both positive, inputs i and j are substitutes, as the price increase of input j will increase the input quantity of i (but decrease the input quantity of j).

Table 3. Interpretation of the AES and MES Estimates

<table><tr><td>AES_ij</td><td>MES_ij</td><td>Relationship between input i and input j</td></tr><tr><td>+</td><td>+</td><td>Substitutes</td></tr><tr><td>-</td><td>+</td><td>Weak complements</td></tr><tr><td>-</td><td>-</td><td>Strong complements</td></tr></table>

Note. Mathematically, the case of $" + "$ and $^ { \prime \prime } - \prime \prime$ does not exist.

When the AES is negative and the MES is positive, inputs i and j are complements, as the price increase of input j will decrease the input quantity of i, but the percentage change in input i is always smaller than the percentage change in input j. Therefore, in this case, we define input j as a “weak complement” to input i. When the AES and MES are both negative, input j becomes a “strong com plement” to input i, as the percentage change in input i is greater than the percentage change in input j as a result of a price change in j. See Online Appendix B for a proof of these results.

To estimate the AES and MES, we adopt a more flexible functional form that imposes fewer restrictions on substitution elasticities, the three-input Translog production function (Dewan and Min 1997, Hitt and Snir 1999, Chwelos et al. 2010, Zhang et al. 2015):

$$
\begin{array}{r l} & {\log (V _ {i t}) = \delta + \alpha_ {c} \log C _ {i t} + \alpha_ {K} \log K _ {i t} + \alpha_ {L} \log L _ {i t}} \\ & {\qquad + \beta_ {C C} (\log C _ {i t}) ^ {2} + \beta_ {C K} \log C _ {i t} \log K _ {i t}} \\ & {\qquad + \beta_ {C L} \log C _ {i t} \log L _ {i t} + \beta_ {K K} (\log K _ {i t}) ^ {2}} \\ & {\qquad + \beta_ {K L} \log K _ {i t} \log L _ {i t} + \beta_ {L L} (\log L _ {i t}) ^ {2} + \varepsilon ,} \end{array}\tag{3}
$$

where $V _ { i t }$ is value-added for industry i in year $t , C _ { i t }$ is IT capital, $K _ { i t }$ is non-IT capital, and $L _ { i t }$ is labor, with respective output elasticities $\alpha _ { C } , \alpha _ { K } ,$ and $\alpha _ { L }$ . To incorporate the impact of three different levels of labor, we expand Equation (3) to estimate a five-input Translog production function:

$$
\begin{array}{r l} & {\log (V _ {i t}) = \delta + \alpha_ {c} \log C _ {i t} + \alpha_ {K} \log K _ {i t} + \alpha_ {L h} \log L h _ {i t}} \\ & {\qquad + \alpha_ {L m} \log L m _ {i t} + \alpha_ {L l} \log L l _ {i t} + \beta_ {C C} (\log C _ {i t}) ^ {2}} \\ & {\qquad + \beta_ {C K} \log C _ {i t} \log K _ {i t} + \beta_ {C L h} \log C _ {i t} \log L h _ {i t}} \\ & {\qquad + \beta_ {C L m} \log C _ {i t} \log L m _ {i t} + \beta_ {C L l} \log C _ {i t} \log L l _ {i t}} \\ & {\qquad + \beta_ {K K} (\log K _ {i t}) ^ {2} + \beta_ {K L h} \log K _ {i t} \log L h _ {i t}} \\ & {\qquad + \beta_ {K L m} \log K _ {i t} \log L m _ {i t} + \beta_ {K L l} \log K _ {i t} \log L l _ {i t}} \\ & {\qquad + \beta_ {L h L h} (\log L h _ {i t}) ^ {2} + \beta_ {L h L m} \log L h _ {i t} \log L m _ {i t}} \\ & {\qquad + \beta_ {L h L l} \log L h _ {i t} \log L l _ {i t} + \beta_ {L m L m} (\log L m _ {i t}) ^ {2}} \\ & {\qquad + \beta_ {L m L l} \log L m _ {i t} \log L l _ {i t} + \beta_ {L l L l} (\log L l _ {i t}) ^ {2} + \varepsilon ,} \end{array}\tag{4}
$$

where $L h _ { i t }$ is high-education labor, $L m _ { i t }$ is middle education labor, and $L l _ { i t }$ is low-education labor. The

Translog production function has been adopted by prior research as a quadratic approximation to the “real” production function (Dewan and Min 1997) and reduces to the Cobb-Douglas form when all of the coefficients of the quadratic terms equal zero. Using coefficient estimates from (4), we estimate the AES and MES by following the specific steps provided in Online Appendix C. For the purpose of this study, we are primarily interested in estimating the elasticity measures between IT capital (C) and labor of different education levels (L, Lh, Lm, and Ll).

## 4.2. Data

4.2.1. Productivity Data. We acquired industry-level productivity data on gross output, value-added, labor, and intermediate inputs from the Bureau of Economic Analysis (BEA) and IT capital and non-IT capital data from the Bureau of Labor Statistics (BLS). The industry categories are based on the 2007 North American Industry Classification System (NAICS) at the three-digit level (provided in Online Appendix D). We merged data from the two sources based on the NAICS codes. The merged data set covers 60 U.S. industries over 16 years, from 1998 to 2013.

Specifically, value-added $( V _ { i t } )$ is the gross output minus total intermediate inputs, which include raw materials, energy, and purchased services. IT capital $( C _ { i t } )$ is the aggregate stock of information-processing equipment and software. Non-IT capital $( K _ { i t } )$ is obtained by subtracting IT capital from the total stock of private fixed assets. Labor (L<sub>it</sub>) is the number of full-timeequivalent employees. All value-based variables have been converted to constant 2009 U.S. dollars using chaintype quantity indices provided by the BEA.

4.2.2. Education Levels. To stratify labor input L into different groups by education levels, we use the March Annual Social and Economic Supplement (ASEC) to the U.S. Current Population Survey (CPS) over the years 1998–2013. The CPS is a monthly survey of U.S. households conducted by the Bureau of Census and the BLS, and it is the primary source of labor-force statistics for the U.S. population. Currently, more than 60,000 households and over 140,000 individuals are surveyed each month. The survey identifies employees in the labor force, their occupations, industry sectors, and education levels. The March ASEC survey has additional data items such as income, earnings, poverty, and the foreign-born population, and it has additional sample households. For each CPS industry, we group all employees by their highest education level: low (high school or below), middle (bachelor’s or associate’s), or high (master’s or above). We then calculate the percentages of each group of employees in the CPS industries and match them to the NAICS-based industries for each corresponding year, using the industry crosswalks provided by the U.S.

Census Bureau.<sup>1</sup> Finally, given the labor input of each NAICS industry and the percentages of employees of the three education levels from the CPS, we can determine the input of low-, middle-, and high-education labor to obtain $L l _ { i t } , L m _ { i t } ,$ , and $L h _ { i t } ,$ respectively.

From the education level of employees, we can also derive their work experience. Consistent with prior literature, we use (age � years of education � 6) to measure work experience (Mincer 1974, Krueger 1993, Mithas and Lucas 2010). We further aggregate employee work experience for each industry at the three education levels.

4.2.3. Routine- vs. Non-Routine-Intensive Industries. We categorized all industries into routine-intensive or nonroutine-intensive by using the Dictionary of Occupa tional Titles (DOT) database. The DOT was created by the U.S. Department of Labor to measure occupational skills and match job applicants to jobs. It contains more than 12,000 detailed occupations, each scored on 44 variables, such as training time, aptitude, temperament, interest, physical demand, and environmental condi tion. These scores are further aggregated at the census occupations level, which we use in this study (Autor et al. 2003). The DOT has been updated several times, and the latest version is DOT 1991, which has been widely used in research on the content of tasks performed by employees (Acemoglu and Restrepo 2019, Zhang 2019, Acemoglu and Restrepo 2020, Deming and Noray 2020).

Following Zhang (2019), we obtained DOT scores on each occupation’s required level of skills in performing non-routine-cognitive, nonroutine-manual, and routine tasks. Manual work requires use of physical labor, such as body movements, whereas cognitive work relies more on workers’ knowledge and mental and interactive abilities. For each employee in the CPS surveys, we identified their occupation and matched it to its DOT scores. We then aggregated the data at the CPS industry level and merged them with our main productivity data set.

We calculated an “abstract score” for each industryyear observation, which equals its nonroutine cognitive skills divided by the sum of its nonroutine-cognitive, nonroutine-manual, and routine skills—that is, the nonroutine-cognitive percentage of its total skill requirements. Similarly, we calculated a “nonroutinemanual score” for each industry-year observation as the nonroutine-manual percentage of its total skill requirements. We then calculated the average abstract score and average nonroutine-manual score for each industry. Because nonroutine tasks can be either cognitive or manual, we classified an industry as nonroutine-intensive if its average abstract score or its average nonroutine-manual score ranked in the top 25% (quartile). The rest of the industries are classified as routine-intensive industries. This divided our sample into two exclusive groups, with (coincidentally) exactly half of the industries being routine-intensive and half non-routine-intensive. (Online Appendix D provides the industry groupings.)

Figure 1. (Color online) Percentages of Labor Inputs Over Time (Full Sample)  
![](/api/attachments/GSM3CVDE/fulltext/images/35572bf3735efda604bf6af0e2703a7d997d419dd8c7d6a3268ed0769bb42a6f.jpg)

4.2.4. Summary Statistics. Table A1 in Online Appendix E provides summary statistics for our pooled, full sample, as well as the subsamples. Figure 1 shows the percentages of labor inputs over time for the full sample. High-education labor increased steadily, as did middleeducation labor since 2000, albeit at a slower pace. Meanwhile, low-education labor steadily decreased its share in the total labor force. The trends are more obvious post-2000. Middle-education labor overtook loweducation labor in 2001 as the largest labor group employed in the U.S. economy and remained so for the rest of our sample period. High-education labor has consistently been the smallest of the three groups.

Figures 2 and 3 show the percentages of labor inputs for the routine-intensive and non-routine-intensive subsamples, respectively. Overall, both subsamples exhibit trends similar to the full sample: High-education and middle-education labor increased their shares over time, whereas the low-education labor percentage generally decreased. Among the three labor groups, higheducation labor exhibits the clearest trend, steadily increasing in both subsamples. Low-education labor kept falling in total labor shares in the non-routineintensive industries, although in the routine-intensive industries, it has had greater fluctuations, especially prior to 2006. Middle-education labor increased in both subsamples, again with greater fluctuations in the routineintensive industries. The volatilities that we observe for low- and middle-education labor in the routine-intensive industries may be due to structural changes undergone by many of the traditional manufacturing and labor-intensive industries.

Figure 2. (Color online) Percentages of Labor Inputs Over Time (Routine-intensive Industries)  
![](/api/attachments/GSM3CVDE/fulltext/images/9bd180e773b483ebd24bc0609cfd6a779f690ce422a435bc15a742e55c1f289b.jpg)

Figure 3. (Color online) Percentages of Labor Inputs Over Time (Non-Routine-Intensive Industries)  
![](/api/attachments/GSM3CVDE/fulltext/images/e54904a537f2bf418971bbe8e7eabaeccdc9bebf5ba0064d634844bd832b950e.jpg)

Figure 4 shows the general time trends for IT capital in the full sample and the subsamples. IT capital has steadily increased in all (sub)samples, except for in low-AI-exposure industries. The slopes of the routineintensive and non-routine-intensive industry groups run almost parallel except from 2002 to 2005, when the increase in IT slowed in routine-intensive industries. The amount of IT capital has been consistently and significantly greater in high-AI-exposure industries than in low-AI-exposure ones.

## 5. Estimation Results

## 5.1. Econometric Issues

Because we have a panel data set, we consider two common econometric issues in our estimation: heteroscedasticity and autocorrelation. Heteroscedasticity is possible because the industries may exhibit idiosyncrasy. Firstorder autocorrelation may arise because the output in any year is likely to be correlated with that of the prior year within an industry. We performed a Breusch-Pagan/Cook-Weisberg test for heteroscedasticity and obtained a significant result $( \chi ^ { 2 } = 9 . 8 0 ) $ , rejecting the null hypothesis of no heteroskedasticity in our data set. We performed a Wooldridge test for autocorrelation and obtained a significant result (F-statistic � 116.62), rejecting the null hypothesis of no first-order autocorrelation. Therefore, we estimate Equations (3) and (4) using a feasible-generalized-least-squares (FGLS) panel model, adjusting for heteroscedasticity and panel-specific autocorrelation. We also include industry and year dummies as additional independent variables to control for these fixed effects.

Figure 4. (Color online) IT Capital Over Time (Full Sample)  
![](/api/attachments/GSM3CVDE/fulltext/images/3ce339bcf73efed8efcdef27251a38bf9c0064c75df6a24869df1d8faebd85fd.jpg)

Our estimation of Equation (4) may present an endogeneity issue, where our key independent variables may be correlated with any unobserved heterogeneity affecting an industry’s output level. For example, a productivity shock (not observable to researchers) might affect both input and output in a production function. To the extent that industries have time- or industryinvariant responses to such shocks, incorporating our yearly and industry fixed effects in the FGLS regression mitigates the endogeneity concern. Moreover, to the extent that any unobserved productivity shocks may be correlated over time, our econometric adjustments with panel-specific autocorrelation should also mitigate the endogeneity concern. Our estimation may also be affected by endogeneity because of possible omitted variables that are time- and industry-variant.

To fully address the endogeneity concerns, we use a generalized method of moments (GMM) estimation with robust standard errors. Following prior research in industry-level production-function contexts (Mittal and Nault 2009, Cheng and Nault 2012, Zhang et al. 2015), and assuming lagged inputs can only affect current-year output through their effects on current-year input levels (and, thus, no direct correlation with current output), we use two-year lags of the five input variables (i.e., IT capital, non-IT capital, and labor of three education levels) and their interactions as the excluded instruments. The Lagrange-multiplier (LM) statistic (7.474) is significant (Kleibergen and Paap 2006), rejecting the null hypothesis that our model is underidentified and that the excluded instruments are not correlated with the endogenous regressors. To test that we have addressed the endogeneity issues from omitted variables, we examine the correlation between the regression residuals and the five main independent variables. If a significant omitted variable is correlated with an independent variable, then the residuals wil correlate with the independent variable. We find that the pairwise correlations between the residuals and each independent variable are all 0.00 and insignificant, indicating that omitted variables are not a concern in our model.

## 5.2. Baseline Results

Table A2 in Online Appendix F presents the estimates from the three-input and five-input translog production functions (Equations (3) and (4), respectively). To compare results with those from prior studies, we also estimated the three-input Cobb-Douglas production function as a benchmark and report the results in column (2). Our coefficient estimates from the Cobb-Douglas function are consistent with prior results (Chwelos et al. 2010, Zhang et al. 2015) in terms of sign, relative magnitude, and significance. Columns (3) and (4) present results from the three-input and five-input translog production functions, respectively. Results of the GMM regression are provided in column (5) and are consistent with our main results in column (4).

We use coefficient estimates in column (4) of Table A2, translog Equation (4)–FGLS, to calculate the AES and MES for each observation in the sample.<sup>3</sup> We then bootstrap (with replacement) the medians of the AES and MES for 200 replications.<sup>4</sup> Table A3 in Online Appendix F presents the AES and MES values for the translog production function with three inputs: IT capital (C), non-IT capital (K), and Labor (L). Table 4 presents the ES results for the translog production function with five inputs: IT capital (C), non-IT capital (K), higheducation labor (Lh), middle-education labor (Lm), and low-education labor (Ll).

Recall that AES\_ij is the AES between inputs i and j. As the AES is symmetric, it does not matter which input’s price changes. MES\_ij is the MES between inputs i and j when the price of input j changes. Table A3 shows the AES and MES estimates between IT Capital (C) and Labor (L) are positive (i.e., substitutes), providing results consistent with prior findings (Dewan and Min 1997, Zhang et al. 2015) that IT is a substitute to labor as a whole. In Table 4, AES\_CLh is negative, whereas both MES values remain positive. This indicates that IT capital is a weak complement to high-education labor; and AES\_CLm and AES\_CLl are positive, whereas both MES values remain positive, indicating that IT capital is a substitute to low- and middle-education labor.

These results show that, as the price of IT decreases, IT substitutes for low- and middle-education workers with a college degree or less, but weakly complements high-education workers with a graduate or professional degree. The baseline results are consistent with our conceptual arguments that, for low- and middle-education labor, the substitution effect of IT dominates, whereas for high-education labor, the complementarity effect of IT dominates.

Table 4. Estimated AES and MES and Interpretations—Full Sample

<table><tr><td>Input i</td><td>Input j</td><td>AES_ij</td><td>MES_ij</td><td>Interpretation</td></tr><tr><td>C</td><td>Lh</td><td>-0.521***(0.162)</td><td>0.279***(0.051)</td><td>Weak complements</td></tr><tr><td>C</td><td>Lm</td><td>1.084***(0.095)</td><td>1.212***(0.102)</td><td>Substitutes</td></tr><tr><td>C</td><td>Ll</td><td>0.947***(0.063)</td><td>1.792***(0.047)</td><td>Substitutes</td></tr><tr><td>Lh</td><td>C</td><td>-0.521***(0.162)</td><td>0.728***(0.034)</td><td>Weak complements</td></tr><tr><td>Lm</td><td>C</td><td>1.084***(0.095)</td><td>0.365***(0.041)</td><td>Substitutes</td></tr><tr><td>Ll</td><td>C</td><td>0.947***(0.063)</td><td>0.456***(0.028)</td><td>Substitutes</td></tr></table>

Note. C is IT capital; Ll, Lm, and Lh are low-education, middleeducation, and high-education labor, respectively. \*\*\*p < 0.01.

## 5.3. Routine- and Non-Routine-Intensive Industries

To test our hypotheses, we divided our data set into two subsamples: routine-intensive industries and nonroutine-intensive industries. Recall that routine-intensive industries are in the top quartile of all industries ranked by either their cognitive or manual nonroutine scores. Table A4 in Online Appendix F presents the FGLS estimation results for Equation (4) for the two subsamples. The results are used to further calculate the AES and MES estimates in Table 5.

For high-education labor in non-routine-intensive industries (Table 5), AES\_CLh (�1.605) is negative and MES\_CLh (0.522) is positive, indicating that the demand for IT will decrease, but with a smaller percentage ratio (i.e., they are weak complements) when labor price increases in the non-routine-intensive industries. In addition, AES\_CLh (�1.605) and MES\_LhC (�1.239) are negative for high-education labor, indicating that the demand for labor will decrease, but with a larger percentage ratio (i.e., they are strong complements) when IT price increases. Hence, when either IT or labor price changes, IT and high-education labor are complements in the nonroutine-intensive industries. Similarly, in the routineintensive industries, AES\_CLh (�2.233) and MES\_CLh (�0.018) are negative, indicating that the demand for IT will decrease, but with a larger percentage ratio (i.e., they are strong complements) when labor price increases. AES\_CLh (�2.233) is negative and MES\_LhC (0.014) is positive, indicating that the demand for labor will decrease, but with a smaller percentage ratio (i.e., they are weak complements) when IT price increases. Hence, in both ways, when either IT or labor prices increase, they are complements in the routine-intensive industries. These results support Hypothesis 1(a). Comparing routine- and non-routine-intensive industries, our results suggest that when IT price drops over time, the corresponding increase in demand for high-education labor is stronger in non-routine-intensive industries than in routine-intensive ones, possibly because advanced IT adoption tends to create more cognitive, nonroutine tasks, which are more likely to be in non-routineintensive industries. On the other hand, when higheducation labor becomes more expensive over time, it decreases the demand for IT with a greater magnitude in routine-intensive industries.

Low-education labor is a net substitute with IT in both routine- and non-routine-intensive industries, supporting Hypothesis 1(b). When labor price is changing, substitution is stronger in routine-intensive industries; when IT price is changing, substitution is stronger in non-routine-intensive industries. When IT price falls, it triggers a stronger substitution for low-education labor than for middle-education labor in routine-intensive industries. Moreover, when IT price falls, the substitution effect is the strongest for the low-education group in non-routine-intensive industries (MES\_LlC � 1.260). When labor price rises, the increase in IT investment is strongest as middle-education labor becomes more expensive in routine-intensive industries (MES\_CLm � 0.410), suggesting that firms have more incentives to invest in IT and increase the utilization level of existing IT in response to rising labor costs.

Middle-education labor is a net substitute for IT in routine-intensive industries, supporting Hypothesis 2(a). However, IT becomes a net complement with middle-education labor in non-routine-intensive industries, which supports Hypothesis 2(b), and specifically a weak complement, regardless of which price is changing. Again, comparing routine- and non-routine-intensive industries, when IT becomes cheaper, the demand for middle-education labor increases in non-routine-intensive industries, while decreasing in routine-intensive ones. This is likely because IT creates nonroutine tasks, cognitive or manual, disproportionally in non-routine-intensive industries and, thus, drives up the demand for middleeducation labor, who can have meaningful interactions with new technology systems. Given that IT and middleeducation labor are net substitutes in our full sample, the substitution effect in routine-intensive industries has likely outweighed the complementary effect in nonroutine-intensive industries for middle-education labor.

Table 5. Interpretation of the AES\_ij and MES\_ij Estimates: Routine-Intensive- vs. Non-Routine-Intensive Industries

<table><tr><td rowspan="2">Input i</td><td rowspan="2">Input j</td><td colspan="3">Routine-intensive industries</td><td colspan="3">Non-routine-intensive industries</td></tr><tr><td>AES_ij</td><td>MES_ij</td><td>Interpretation</td><td>AES_ij</td><td>MES_ij</td><td>Interpretation</td></tr><tr><td>C</td><td>Lh</td><td>-2.233***(1.005)</td><td>-0.018***(0.005)</td><td>Strong complements</td><td>-1.605***(0.685)</td><td>0.522***(0.080)</td><td>Weak complements</td></tr><tr><td>C</td><td>Lm</td><td>1.001***(0.096)</td><td>0.410***(0.031)</td><td>Substitutes</td><td>-7.988***(1.149)</td><td>0.117***(0.028)</td><td>Weak complements</td></tr><tr><td>C</td><td>Ll</td><td>0.732***(0.173)</td><td>0.343**(0.160)</td><td>Substitutes</td><td>3.658***(0.754)</td><td>0.054*(0.030)</td><td>Substitutes</td></tr><tr><td>Lh</td><td>C</td><td>-2.233***(1.005)</td><td>0.014***(0.002)</td><td>Weak complements</td><td>-1.605***(0.685)</td><td>-1.239***(0.027)</td><td>Strong complements</td></tr><tr><td>Lm</td><td>C</td><td>1.001***(0.096)</td><td>0.087***(0.032)</td><td>Substitutes</td><td>-7.988***(1.149)</td><td>1.330***(0.023)</td><td>Weak complements</td></tr><tr><td>Ll</td><td>C</td><td>0.732***(0.173)</td><td>0.171**(0.080)</td><td>Substitutes</td><td>3.658***(0.754)</td><td>1.260***(0.046)</td><td>Substitutes</td></tr></table>

Notes. C is IT capital; Ll, Lm, and Lh are low-education, middle-education, and high-education labor, respectively \*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Furthermore, as the price of labor changes (labor price has been generally increasing over time, but at a much slower pace than changes in IT price), its substitution for IT is stronger when it is induced by a change in the middle-education labor price in routine-intensive industries than by a similar change in the low-education labor price in either routine or non-routine-intensive industries (MES � 0.410 > 0.343 or 0.054). Considering that the increase in IT will, in turn, impact labor demand, we may end up losing more middle-education labor than loweducation labor as a result of the increasing labor cost. This is a very interesting finding because it indicates that middle-education labor in routine-intensive industries may suffer the most as the average labor price increases: Firms have strong incentives to react to such price increases by investing in IT and automation.

## 6. Additional Analysis on the Impact of AI

We argue that the relationship between IT and labor is also affected by the extent to which labor is potentially exposed to AI influences. AI generally refers to computer software that uses sophisticated algorithms to discover patterns in data and make predictions about the future (Broussard 2018). By this definition, AI could be viewed as a subset of general IT capital. Over the past few decades, rapid deployment of AI increasingly competes with human employees (Frey and Osborne 2017). Specifically, AI makes use of a variety of algorithms, such as logistical regression, K-nearest neighbors, Bayesian models, decision trees, and neural networks, to name a few. Depending on whether rules for actions can be predefined or not, AI can be broadly categorized into expert systems and machine learning (Ben-David and Frank 2009, Arrieta et al. 2020).<sup>5</sup> Expert systems are designed primarily to solve rule-based problems or to process data according to predetermined procedures. One of the key limitations of expert systems is that they depend on rules and procedures derived by humans and do not adapt easily. ML has gained increasing popularity in recent years because it can potentially overcome this limitation. At its most basic, ML is the practice of using algorithms to parse data, learn from the data, develop its own rules, and then use them to make future predictions. A key advantage of ML is that it can be used even in cases where it is impossible or difficult for humans to derive rules (Levy 2018, Peng and Bhaskar 2023).

Therefore, different from past IT, AI has the potential to automate various nonroutine tasks across a wide range of occupations. In fact, AI systems go beyond simple automation of routine tasks and have been increasingly deployed for performing nonroutine and creative tasks that used to involve high levels of education and accumulated experience (Webb 2020, Lysyakov and Viswanathan 2022, Tarrant 2023). The consequence is that, in industries with a higher exposure to AI applications (high-AIE industries), IT could shift the comparative advantage from humans to machines, regardless of employees’ education levels, and, thus, reduce the overall demand for human labor in these industries. In other words, in high-AIE industries, IT substitutes not only for labor of middle and low-education levels, as predicted by SBTC and RBTC, but also for high-education labor, due to AI’s evolving capabilities to perform nonroutine tasks.

Industries with a lower exposure to AI applications (low-AIE industries), however, are less influenced by A on cognitive tasks, but more affected on the physical ones. Consequently, AI’s substitution effect is not strong enough yet, and the impact of SBTC and RBTC prevails. For high-education labor, IT capital is still complementary to those who can perform nonroutine and creative tasks. Moreover, low-AIE industries are in a less advanced stage of AI adoption compared with high-AIE industries. Hence, these industries rely structurally less on AI to produce output and stay competitive, and, thus, there is less competition from AI with higheducation labor. For labor of middle- and low-education levels, IT is superior to them in performing routine and standardized tasks (Lysyakov and Viswanathan 2022), and, thus, we expect that IT would remain a substitute with them, as predicted by our research framework in Table 2.

To test the impact of AI on the IT-labor relationship, we used the industry-level AI exposure (AIE) index developed by Felten et al. (2021). AIE measures the extent to which occupations in an industry are exposed to AI applications. The AIE index was constructed using data from 10 selected AI applications that “are likely to have implications for the workforce,” including abstract strategy games, real-time video games, image recognition, visual question answering, image generation, reading comprehension, language modeling, translation, speech recognition, and instrumental track recognition. A higher AIE score reflects a larger influence of AI on cognitive tasks and abilities and a smaller influence on physical ones. The most exposed industries tend to be “white-collar” industries that require high levels of education, as well as information processing, such as financial and legal services, whereas “blue-collar” industries that involve more manual labor, perhaps unsurprisingly, are less exposed to AI (Felten et al. 2021).

Table 6. Interpretation of the AES\_ij and MES\_ij Estimates: High- vs. Low-AIE Industries

<table><tr><td rowspan="2">Input i</td><td rowspan="2">Input j</td><td colspan="3">High-AIE industries</td><td colspan="3">Low-AIE industries</td></tr><tr><td>AES_ij</td><td>MES_ij</td><td>Interpretation</td><td>AES_ij</td><td>MES_ij</td><td>Interpretation</td></tr><tr><td>C</td><td>Lh</td><td>1.103***(0.001)</td><td>1.250***(0.001)</td><td>Substitutes</td><td>-0.341***(0.001)</td><td>0.584***(0.020)</td><td>Weak complements</td></tr><tr><td>C</td><td>Lm</td><td>0.065***(0.012)</td><td>1.313***(0.010)</td><td>Substitutes</td><td>1.030***(0.000)</td><td>0.765***(0.005)</td><td>Substitutes</td></tr><tr><td>C</td><td>Ll</td><td>0.878***(0.000)</td><td>0.744***(0.001)</td><td>Substitutes</td><td>2.038***(0.039)</td><td>0.702***(0.050)</td><td>Substitutes</td></tr><tr><td>Lh</td><td>C</td><td>1.103***(0.001)</td><td>1.034***(0.000)</td><td>Substitutes</td><td>-0.341***(0.001)</td><td>0.976***(0.001)</td><td>Weak complements</td></tr><tr><td>Lm</td><td>C</td><td>0.065***(0.012)</td><td>0.837***(0.003)</td><td>Substitutes</td><td>1.030***(0.000)</td><td>1.013***(0.000)</td><td>Substitutes</td></tr><tr><td>Ll</td><td>C</td><td>0.878***(0.000)</td><td>0.996***(0.000)</td><td>Substitutes</td><td>2.038***(0.039)</td><td>1.103***(0.003)</td><td>Substitutes</td></tr></table>

Notes. C is IT capital; Ll, Lm, and Lh are low-education, middle-education, and high-education labor, respectively \*\*\*p < 0.01.

We first divided our industries into those of high and low AIE using the median AIE score in our sample. (A complete classification of the breakdown is provided in Online Appendix D.) Compared with our routineness classification for industries, 62% of the high-AIE industries and 36% of the low-AIE industries are nonroutine industries. The percentages of labor inputs for high-AIE and low-AIE subsamples are presented in Online Appendix G. It is worth noting that middle-education labor has a consistently larger share in the labor force than loweducation labor in high-AIE industries, whereas it is the opposite in low-AIE industries.

Table A5 in Online Appendix F presents the estimation results for Equation (4) for high-AIE and low-AIE subsamples. We then estimate the AES and MES measures between IT and labor for the two subsamples and present the results in Table 6. The results indicate that, for the high-AIE industries, IT becomes a net substitute for labor, regardless of the education level. For the low-AIE industries, IT is a weak complement with high-education labor and a net substitute for low- and middle-education labor. For industries that involve a relatively higher level of information processing and cognitive tasks, IT has become increasingly more capable of automating these tasks, even at the level that requires the involvement of high-education labor. For the industries involving more manual work and less exposure to AI applications, IT has been replacing labor of low- and middle-education levels, but complementing labor of high-education levels.

## 7. Concluding Remarks

With IT prices falling and labor prices rising, IT has increasingly been used to displace human labor. However, the phenomenon is more nuanced than it appears. On one hand, literature from SBTC argues that the use of IT helps increase productivity, thereby complementing skilled labor (Bound and Johnson 1992, Goldin and Katz 1998). On the other hand, as demonstrated by studies from RBTC, IT may automate routine tasks and, thus, displace labor performing these tasks (Autor et al. 2003, Goos et al. 2014). In this study, we develop an integrative view of the IT-labor relationship that incorporates the influence of both SBTC and RBTC. We delve deeper into the relationship between IT and human labor by examining it with three different levels of education with regard to industry-level routine intensity, AI exposure, and STEM intensity.<sup>6</sup> Our findings are novel and bear important policy implications.

## 7.1. Discussion of Findings

Our findings suggest that IT has been displacing collegeeducated labor in the full sample and in routine-intensive industries, which runs counter to the conventional wis dom that a college degree provides sufficient job security. A college degree used to be considered an advanced degree, and only a talented few could go to college in earlier times (Autor 2014)—and college graduates typically performed nonroutine tasks. However, in more recent decades, college education has proliferated in the United States, as “college for all” has become the new norm (Goyette 2008). As more and more people receive a college education, workers with a college education increasingly perform more routine tasks, which can be manual or cog nitive in nature, in occupations such as machine operators, accountants, and bank clerks (Manning 2004, Acemoglu and Autor 2011, Michaels et al. 2014, Beaudry et al. 2016). Moreover, fast advancement of IT has increasingly turned some of the nonroutine tasks performed by these workers into routine ones, and, thus, jobs associated with a college degree are becoming increasingly vulnerable to IT replacement, especially in routine-intensive industries.

These results reflect the reality that the price of IT has fallen drastically over the past few decades, and more firms have adopted IT to replace positions that require relatively less training and education. They suggest that more tasks that used to be done by college-educated workers are gradually computerized with increasing IT investments, which differs from prior literature that finds technology and college-educated labor are complements (Bound and Johnson 1992) and reflects a more recent trend in the IT-labor relationship. When the price of labor changes, we find similar results: When the price of low- and middle-education workers goes up (e.g., a higher minimum wage), IT substitutes for labor, and more IT investment is well incentivized; when the price of high-education labor increases, labor becomes a weak complement to IT and, thus, would reduce the utilization level of existing IT.

In addition, as the price of IT has dropped significantly and steadily, its substitution for labor has been strongest for low-education workers in non-routineintensive industries. On the other side, increasing wages for labor over time triggered the strongest increase in IT investments when middle-education labor from routineintensive industries became more expensive, indicating that middle-education labor may eventually suffer even more than low-education labor when firms respond to rising labor costs by investing in IT. Moreover, as IT has become cheaper, it has triggered greater demand for high-education labor in non-routine-intensive industries than in routine ones. These findings complement prior ones (Autor et al. 2003, Zhang et al. 2015, Atasoy et al. 2016) by providing additional, more nuanced comparisons of the strength of substitution/complementarity based on education level and task routineness.

We also explore the impact of AI exposure and STEM occupations on the IT-labor relationship by dividing our sample based on the AI exposure index and STEM intensity, respectively. We find that IT is only complementary with high-education labor in industries with a lower AI-exposure index or higher percentages of STEM workers, while being a net substitute with low- and middleeducation labor, regardless of their AI exposure and STEM intensity. This result further supports our main findings that even college-educated labor has now become susceptible to IT displacement. More critically, IT could become a substitute even with high-education labor in industries with relatively higher exposure to AI.

## 7.2. Practical Implications

Our findings have important implications for individuals, managers, and policy makers. First, our study provides timely empirical evidence on a topic that is of practical importance for policy making. With the advancement of IT and the expansion of education, many practitioners feel unsure about whether the impacts of IT on middle- or high-education levels have changed (Arreola 2019, Binkley and Fingerhut 2019, Talabi 2019). Through substitution/complementarity with labor, IT is playing an increasingly important role in job destruction and creation. It is critical for practitioners and policy makers to understand how IT interacts with workers—substituting for or complementing them. Our results show that IT not only substitutes for low-education labor, but also may replace college educated labor in routine-intensive industries. This may be because the advancement of technology has changed the nature and responsibilities of many middleeducation jobs in routine-intensive industries, requiring workers to have more technical knowledge and stronger critical thinking skills that have not been sufficiently provided by some sources of college education (Rampell 2014, Davenport and Kirby 2015). Our results also show that the group benefiting the most from the massive adoption of IT by U.S. industries over the past few decades is the high-education group—those with graduate or professional degrees in non-routine-intensive industries. Our findings support the role of higher education in creating new jobs that are complementary to IT investment; hence, they have rich policy implications.

Second, our study has implications for individuals pursuing education. A large percentage of young people today do not believe in college or graduate education. A recent survey showed that about 40% of people between ages 13 and 29 believed that a bachelor’s degree prepares people only somewhat well, or even poorly, for today’s economy and that a high school diploma is sufficient (Binkley and Fingerhut 2019). On the other hand, some others believe that even a college education is insufficient and that graduate education is needed to meet the requirements of today’s jobs (Arreola 2019, Talabi 2019). Therefore, examining the role that education plays in the IT-labor relationship will inform individuals making decisions about pursuing future education, as well as educators designing polices in response to the rapid development of IT. Our findings support the second perspective, that a college degree may not be enough in today’s labor market, especially in routine-intensive industries, and that a graduate degree may be increasingly needed to meet the challenges of the computerized work environment. As companies turn to IT more and more, workers must adapt and develop IT-based skills that will allow them to make the most of technologies. To take full advantage of IT and enhance the productivity of the labor force, firms need to support their employees’ continuous education.

Third, governments should be aware of the potential impact of advanced technologies, such as AI, and should continue their support for higher education to meet the labor demands driven by accelerating IT implementation. Because it is impossible to send everyone to graduate school, policies and funding should support the creation and delivery of long-term training programs that can offer less educated workers the skills they need to survive during a time of technological upheaval. Governments must watch out for the potential downsides of an IT-driven economy, given that advanced IT (e.g., AI) is likely to displace increasingly more labor, regardless of education level, and, thus, may lead to a higher unemployment rate. Special attention should be given to low-education labor in non-routineintensive industries, because IT has the strongest substitution effect on this group. Governments should also understand that increasing minimum wage levels may merely strengthen incentives for firms to invest in automation and, thus, should be mindful about its potential long-term impact on labor demand.

## 7.3. Limitations and Future Research

This study has limitations, many of which suggest avenues for future research. First, as not all undergraduate degrees are equal, middle-education labor is a very heterogeneous category (e.g., schools, majors, etc.). Therefore, the middle-education group deserves a finergrained exploration in future research. Second, our data are from the U.S. economy at the industry level, which limits our ability to locate another appropriate U.S. data set to validate our findings. As a future research direction, we plan to collect and analyze data from other countries for comparison. Third, our data set covers only the years 1998–2013; we do not have more recent data to analyze the trends in the last decade. With the advancement of IT (especially AI) and the expansion of higher education, the impact of IT on workers of middle- or high-education levels will continue to evolve. Today’s challenging work environment requires humans to compete with machines (Brynjolfsson and McAfee 2012). It is widely accepted that humans have a comparative advantage for performing nonroutine tasks, whereas computers are better at carrying out routine tasks, leading to a division of labor between humans and computers. The concept behind comparative advantage is opportunity cost, which assumes that one agent cannot perform both tasks and, thus, needs to specialize. However, computers may be somewhat of an exception because of the precipitous decrease in IT cost per unit of capability: Computers may not incur opportunity cost in producing any products or performing any tasks and, therefore, will not need to engage in division of labor with humans; rather, they can simply replace humans. Therefore, it is conceivable that the complementarity effect may diminish in the long run, whereas the substitution effect strengthens, echoing the quotes by Leontief (1952) at the beginning of our paper that more workers will be replaced by machines. Therefore, future studies may collect more recent data to explore and verify this unfolding trend between IT and labor. Hopefully, results such as ours will figure into philosophical and ethical discussions about the appropriate places and roles of humans, computers, and work.

## Endnotes

<sup>1</sup> The crosswalks between CPS and NAICS industries are recorded in the CPS surveys and also available at https://www.census.gov/ topics/employment/industry-occupation/guidance/code-lists.html.

<sup>2</sup> The routine tasks include both routine cognitive and routine manual.

<sup>3</sup> For details of steps calculating the AES and MES, please see Online Appendix C.

<sup>4</sup> We chose medians over means to make sure our results are not driven by outliers.

<sup>5</sup> Some researchers consider ML the same as AI, and others consider them parallel technologies, but most researchers view ML as a subfield of AI (Jordan and Mitchell 2015, Russell and Norvig 2020).

<sup>6</sup> We also examined the impact of STEM (science, technology, engineering, and mathematics) occupations on the IT-labor relationship. Details can be found in Online Appendix H.

## References

Acemoglu D (1998) Why do new technologies complement skills? Directed technical change and wage inequality. Quart. J. Econom. 113(4):1055–1089.

Acemoglu D, Autor D (2011) Skills, tasks and technologies: Implica tions for employment and earnings. Card D, Ashenfelter O, eds. Handbook of Labor Economics (North Holland, Amsterdam), 1043–1171.

Acemoglu D, Restrepo P (2019) Automation and new tasks: How technology displaces and reinstates labor. J. Econom. Perspect 33(2):3–29.

Acemoglu D, Restrepo P (2020) Robots and jobs: Evidence from US labor markets. J. Polit. Econom. 128(6):2188–2244.

Acemoglu, D, Autor D, Hazell J, Restrepo P (2022) Artificial intelligence and jobs: Evidence from online vacancies. J. Labor Econom. 40(S1):S293–S340.

Allen RGD (1938) Mathematical Analysis for Economists (Macmillan, London).

Arreola M (2019) Is a bachelor’s degree enough or only the first step? Golden Gate Xpress (May 21), https://goldengatexpress.org/89218/ latest/opinion/is-a-bachelors-degree-enough-or-only-the-firststep/.

Arrieta AB, Diaz-Rodriguez N, Del Ser J, Bennetot A, Tabik S, Barbado A, Garcia S, et al. (2020) Explainable artificial intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. Inform. Fusion 58:82–115.

Associated Press (2019) Over 30 million U.S. workers will lose their jobs because of AI. https://www.marketwatch.com/story/ai-is set-to-replace-36-million-us-workers-2019-01-24.

Atasoy H, Banker RD, Pavlou PA (2016) On the longitudinal effect of IT use on firm-level employment. Inform. Systems Res. 27(1):6–26.

Autor DH (2014) Skills, education, and the rise of earnings inequal ity among the “other 99 percent.” Science 344(6186):843–851.

Autor DH, Dorn D (2013) The growth of low-skill service jobs and the polarization of the US labor market. Amer. Econom. Rev. 103(5):1553–1597.

Autor DH, Katz LF, Kearney MS (2006) The polarization of the US labor market. Amer. Econom. Rev. 96(2):189–194.

Autor DH, Katz LF, Kearney MS (2008) Trends in U.S. wage inequal ity: Revising the revisionists. Rev. Econom. Statist. 90(2):300–323.

Autor DH, Katz LF, Krueger AB (1998) Computing inequality: Have computers changed the labor market? Quart. J. Econom. 113(4): 1169–1213.

Autor DH, Levy F, Murnane RJ (2003) The skill content of recent technological change: An empirical exploration. Quart. J. Econom 118(4):1279–1333.

Ba S, Nault BR (2017) Emergent themes in the interface between economics of information systems and management of technol ogy. Production Oper. Management 26(4):652–666.

Bartel AP, Lichtenberg FR (1987) The comparative advantage of edu cated workers in implementing new technology. Rev. Econom. Statist. 69(1):1–11.

Beaudry P, Green DA, Sand B (2016) The great reversal in the demand for skill and cognitive tasks. J. Labor Econom. 34(S1):199–247.

Becker GS (1962) Investment in human capital: A theoretical analysis. J. Polit. Econom. 70(5):9–49.

Ben-David A, Frank E (2009) Accuracy of machine learning models versus “hand crafted” expert systems—a credit scoring case study. Expert Systems Appl. 36(3):5264–5271.

Berndt ER, Morrison CJ, Rosenblum LS (1992) High-tech capital formation and labor composition in U.S. manufacturing industries: An exploratory analysis. NBER Working Paper 4010, National Bureau of Economic Research, Cambridge, MA.

Binkley C, Fingerhut H (2019) Many youths say a high school diploma is enough to succeed, poll shows. Experts are alarmed. USA Today (November 12), https://www.usatoday.com/story/ news/education/2019/11/12/high-school-diploma-vs-collegedegree-what-young-americans-value/2573037001/.

Blackorby C, Russell RR (1989) Will the real elasticity if substitution please stand up? (A comparison of the Allen/Uzawa and Mor ishima elasticities). Amer. Econom. Rev. 79(4):882–888.

Bound J, Johnson G (1992) Changes in the structure of wages in the 1980s: An evaluation of alternative explanations. Amer. Econom. Rev. 82(3):371–392.

Bresnahan TF, Brynjolfsson E, Hitt LM (2002) Information technol ogy, workplace organization, and the demand for skilled labor: Firm-level evidence. Quart. J. Econom. 117(1):339–376.

Broussard M (2018) Artificial Unintelligence: How Computers Misun derstand the World (MIT Press, Cambridge, MA).

Brown A (2016) YOUR job won’t exist in 20 years: Robots and AI to ‘eliminate’ ALL human workers by 2036. Daily Express (February 5), https://www.express.co.uk/life-style/science-technology/640744 Jobless-Future-Robots-Artificial-Intelligence-Vivek-Wadhwa.

Brynjolfsson E, Hitt L (1996) Paradox lost? Firm-level evidence on the returns to information systems spending. Management Sci. 42(4): 541–558.

Brynjolfsson E, Hitt LM (2000) Beyond computation: Information technology, organizational transformation and business perfor mance. J. Econom. Perspect. 14(4):23–48.

Brynjolfsson E, McAfee A (2012) Race Against the Machine: How the Digital Revolution Is Accelerating Innovation, Driving Productivity, and Irreversibly Transforming Employment and the Economy, 1st ed. (Digital Frontier Press, Lexington, MA).

Brynjolfsson E, Mitchell T (2017) What can machine learning do? Workforce implementations. Science 358(6370):1530–1534.

Bureau of Labor Statistics (2015) Long-term price trends for computers, TVs, and related items. Accessed July 27, 2023, https:// www.bls.gov/opub/ted/2015/long-term-price-trends-for-computerstvs-and-related-items.htm.

Bureau of Labor Statistics (2020) Employment Cost Index: Wages and salaries: private industry workers. Accessed July 27, 2023, https://fred.stlouisfed.org/series/ECIWAG.

Cellan-Jones R (2014) Stephen Hawking warns artificial intelligence could end mankind. BBC (December 2), https://www.bbc.com/ news/technology-30290540.

Chambers RG (1988) Applied Production Approach: A Dual Approach (Cambridge University Press, Cambridge, UK).

Cheng Z, Nault BR (2012) Relative industry concentration and customer-driven IT spillovers. Inform. Systems Res. 23(2):340–355.

Chwelos P, Ramirez R, Kraemer KL, Melville NP (2010) Does technological progress alter the nature of information technology as a production input? New evidence and new results. Inform. Sys tems Res. 21(2):392–408.

Costello K (2019) Gartner says global IT spending to grow 1.1 percent in 2019. Accessed July 27, 2023, https://www.gartner.com/en/news room/press-releases/2019-04-17-gartner-says-global-it-spendingto-grow-1-1-percent-i.

Davenport TH (2006) Competing on analytics. Harvard Bus. Rev 84(1):98–107.

Davenport TH, Kirby J (2015) Beyond automation. Harvard Bus. Rev 93(6):59–65.

Deming DJ, Noray K (2020) Earnings dynamics, changing job skills and STEM careers. Quart. J. Econom. 135(4):1965–2005.

Dewan S, Min CK (1997) The substitution of information technology for other factors of production: A firm level analysis. Management Sci. 43(12):1660–1675.

Felten E, Raj M, Seamans R (2021) Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. Strategic Management J. 42(12):2195–2217.

Ford M (2013) Could artificial intelligence create an unemployment crisis? Commun. ACM 56(7):37–39.

Francalanci C, Galal H (1998) Information technology and worker composition: Determinants of productivity in the life insuranc industry. MIS Quart. 22(2):227–241.

Frey CB, Osborne MA (2017) The future of employment: How susceptible are jobs to computerisation? Tech. Forecasting Soc. Change 114:254–280.

Fu¨ gener A, Grahl J, Gupta A, Ketter W (2022) Cognitive challenge in human–artificial intelligence collaboration: Investigating the path toward productive delegation. Inform. Systems Res. 33(2): 678–696.

Goldin C, Katz LF (1998) The origins of technology-skill complementarity. Quart. J. Econom. 113(3):693–732.

Goldman Sachs (2023) Generative AI could raise global GDP by 7% Accessed July 27, 2023, https://www.goldmansachs.com/insights/ pages/generative-ai-could-raise-global-gdp-by-7-percent.html

Goos M, Manning A (2007) Lousy and lovely jobs: The rising polari zation of work in Britain. Rev. Econom. Statist. 89(1):118–133

Goos M, Manning A, Salomons A (2009) Job polarization in Europe Amer. Econom. Rev. 99(2):58–63.

Goos M, Manning A, Salomons A (2014) Explaining job polarization: Routine-biased technological change and offshoring. Amer. Econom. Rev. 104(8):2509–2526.

Goyette KA (2008) College for some to college for all: Social background, occupational expectations, and educational expectations over time. Soc. Sci. Res. 37(2):461–484.

Hicks JR (1932) The Theory of Wages, 2nd ed. (Macmillan, London).

Hitt LM, Snir EM (1999) The role of information technology in mod ern production: Complement or substitute to other inputs? Working paper, University of Pennsylvania, Philadelphia.

Hout M (2012) Social and economic returns to college education in the United States. Annu. Rev. Sociol. 38:379–400.

Hunt AH, Hunt TL (1983) The robotics are coming. Human Resources Implications of Robotics (W. E. Upjohn Institute for Employment Research, Kalamazoo, MI), 1–17.

Iansiti M, Lakhani KR (2020) Competing in the Age of AI: Strategy and Leadership When Algorithms and Networks Run the World (Harvard Business Review Press, Boston).

Jia N, Luo X, Fang Z (2020) Can artificial intelligence (AI) substitute or complement managers? Divergent outcomes for transformational and transactional managers in a field experiment. Working paper, University of Southern California.

Jordan MI, Mitchell TM (2015) Machine learning: Trends, perspectives, and prospects. Science 349(6245):255–260.

Jussupow E, Spohrer K, Heinzl A, Gawlitza J (2021) Augmenting medical diagnosis decisions? An investigation into physicians decision-making process with artificial intelligence. Inform. Systems Res, 32(3):713-735

Kleibergen F, Paap R (2006) Generalized reduced rank tests using the singular value decomposition. J. Econometrics 133(1):97–126.

Krueger AB (1993) How computers have changed the wage structure: Evidence from microdata, 1984-1989. Quart. J. Econom. 108(1):33–60.

Krueger D, Kumar KB (2004) Skill-specific rather than general education: A reason for US-Europe growth differences? J. Econom. Growth 9(2):167–207.

Leontief W (1952) Machine and man. Sci. Amer. 187(3):150–164

Levy F (2018) Computers and populism: Artificial intelligence, jobs, and politics in the near term. Oxford Rev. Econom. Policy 34(3): 393–417.

Levy F, Murnane RJ (2004) The New Division of Labor: How Computers Are Creating the Next Job Market (Princeton University Press, Princeton, NJ).

Lewandowski P, Park A, Schotte S (2020) The global distribution of routine and non-routine work. IBS Working Paper, Instytut Badan Strukturalnych, Warsaw.

Lewis E (2011) Immigration, skill mix, and capital skill complemen tarity. Quart. J. Econom. 126(2):1029–1069.

Lochner L, Moretti E (2004) The effect of education on crime: Evidence from prison inmates, arrests, and self-reports. Amer. Econom. Rev. 94(1):155–189.

Lu SF, Rui HX, Seidmann A (2018) Does technology substitute for nurses? Staffing decisions in nursing homes. Management Sci. 64(4):1842–1859.

Luo X, Tong S, Fang Z, Qu Z (2019) Frontiers: Machines vs. humans: The impact of artificial intelligence chatbot disclosure on customer purchases. Marketing Sci. 38(6):937–947.

Lysyakov M, Viswanathan S (2022) Threatened by AI: Analyzing users’ responses to the introduction of AI in a crowd-sourcing platform. Inform. Systems Res., ePub ahead of print November 15, https://doi.org/10.1287/isre.2022.1184.

Manning A (2004) We can work it out: The impact of technological change on the demand for low-skill workers. Scottish J. Polit. Econom. 51(5):581–608.

Manyika J, Chui M, Miremadi M, Bughin J, George K, Willmott P, Dewhurst M (2017) A future that works: Automation, employ ment, and productivity. McKinsey Global Institute, New York.

Michaels G, Natraj A, Van Reenen J (2014) Has ICT polarized skil demand? Evidence from eleven countries over twenty-five years. Rev. Econom. Statist. 96(1):60–77.

Mincer JA (1974) Schooling, Experience, and Earnings (Columbia Uni versity Press, New York).

Mithas S, Lucas HC (2010) Are foreign IT workers cheaper? US visa policies and compensation of information technology professionals. Management Sci. 56(5):745–765.

Mittal N, Nault BR (2009) Investments in information technology: Indirect effects and information technology intensity. Inform. Systems Res. 20(1):140–154.

Moretti E (2004) Estimating the social return to higher education: Evidence from longitudinal and repeated cross-sectional data. J. Econometrics 121(1–2):175–212.

Morishima M (1967) Danryokusei rison ni kansuru ni-san no teian (a few suggestions on the theory of elasticity). Keizai Hyoron (Econom. Rev.) 16:144–150.

Moshiri S, Simpson W (2011) Information technology and the changing workplace in Canada: Firm-level evidence. Indust. Corporate Change 20(6):1601–1636.

Nedelkoska L, Quintini G (2018) Automation, skills use, and training. OECD Social, Employment and Migration Working Papers

No. 202, Organisation for Economic Co-Operation and Devel opment, Paris.

Peng G, Bhaskar R (2023) Artificial intelligence and machine learning for job automation: A review and integration. J. Database Management 34(1):1–12.

Pinker S (1994) The Language Instinct: How the Mind Creates Language (HarperCollins, New York).

Raj M, Seamans R (2019) Primer on artificial intelligence and robot ics. J. Organ. Design. 8(1):11.

Rampell C (2014) The college degree has become the new high school degree. Washington Post (September 9), https://www.washington post.com/opinions/catherine-rampell-the-college-degree-hasbecome-the-new-high-school-degree/2014/09/08/e935b68c-378a-11e4-8601-97ba88884ffd\_story.html.

Richards E, Terkanian D (2013) Occupational employment projec tions to 2022. Mon. Labor Rev. 136:1–48

Russell S, Norvig P (2020) Artificial Intelligence: A Modern Approach 4th ed. (Pearson, London).

Sainato M (2015) Stephen Hawking, Elon Musk, and Bill Gate Warn About artificial intelligence. Observer (August 19), https:// observer.com/2015/08/stephen-hawking-elon-musk-and-bill gates-warn-about-artificial-intelligence/.

Schultz TW (1961) Investment in human capital. Amer. Econom. Rev. 51(1):1–17.

Selingo JJ (2017) Are colleges preparing students for the automated future of work? Washington Post (November 17), https://www. washingtonpost.com/news/grade-point/wp/2017/11/17/arecolleges-preparing-students-for-the-automated-future-of-work/.

Snow J (2023) ChatGPT can give great answers. But only if you know how to ask the right question. Wall Street J. (April 12), https:/ www.wsj.com/articles/chatgpt-ask-the-right-question-12d0f035.

Stebbins S, Sauter MB (2016) Will your job disappear? USA Toda (March 5), https://www.usatoday.com/story/money/business 2016/03/05/247-17-disappearing-middle-class-jobs/80517434/.

Sturm T, Gerlach JP, Pumplun L, Mesbah N, Peters F, Tauchert C, Nan N, Buxmann P (2021) Coordinating human and machine learning for effective organizational learning. MIS Quart. 45(3):1581–1602.

Talabi I (2019) Your college degree isn’t enough for the workforce. Signal (October 8), https://georgiastatesignal.com/your-collegedegree-isnt-enough-for-the-workforce/.

Tarrant G (2023) Generative AI is already changing white-collar work as we know it. Wall Street J. (March 29), https://www.wsj.com/ articles/generative-ai-is-already-changing-white-collar-work-as we-know-it-58b53918.

Teodorescu MHM, Morse L, Awwad Y, Kane GC (2021) Failures of fairness in automation require a deeper understanding of human–Ml augmentation. MIS Quart. 45(3):1483–1499.

Uzawa H (1962) Production functions with constant elasticities of substitution. Rev. Econom. Stud. 29(4):291–299.

Varian HR (1992) Microeconomic Analysis (W. W. Norton & Company, Inc., New York).

Webb M (2020) The impact of artificial intelligence on the labor market. Working paper, Stanford University.

Zhang DW, Cheng Z, Mohammad H, Nault BR (2015) Information technology substitution revisited. Inform. Systems Res. 26(3): 480–495.

Zhang MB (2019) Labor-technology substitution: Implications for asset pricing. J. Finance 74(4):1793–1839.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
