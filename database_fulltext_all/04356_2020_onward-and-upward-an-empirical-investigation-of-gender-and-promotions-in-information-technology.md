---
otero_id: 4356
otero_key: "2B86DYES"
title: "Onward and Upward? An Empirical Investigation of Gender and Promotions in Information Technology Services"
authors: "Nishtha Langer; Ram D. Gopal; Ravi Bapna"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0892"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.238.7.40] On: 13 May 2020, At: 06:37 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/2B86DYES/fulltext/images/533a36c21b0ac685136c81edfa5723634408a2b60b804f22abbc2689bce28888.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Onward and Upward? An Empirical Investigation of Gender and Promotions in Information Technology Services

Nishtha Langer, Ram D. Gopal, Ravi Bapna

To cite this article: Nishtha Langer, Ram D. Gopal, Ravi Bapna (2020) Onward and Upward? An Empirical Investigation of Gender and Promotions in Information Technology Services. Information Systems Research

Published online in Articles in Advance 28 Apr 2020

https://doi.org/10.1287/isre.2019.0892

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Onward and Upward? An Empirical Investigation of Gender and Promotions in Information Technology Services

Nishtha Langer,<sup>a</sup> Ram D. Gopal,<sup>b</sup> Ravi Bapna<sup>c</sup>

<sup>a</sup> Lally School of Management, Rensselaer Polytechnic Institute, Troy, New York 12180; <sup>b</sup> Business School, Southern University of Science and Technology, Shenzhen 518055, P. R. China; <sup>c</sup> Carlson School of Management, University of Minnesota, Minneapolis, Minnesota 55455 Contact: langen@rpi.edu, https://orcid.org/0000-0002-9561-7163 (NL); ram@sustech.edu.cn, https://orcid.org/0000-0003-4241-9355 (RDG); rbapna@umn.edu, https://orcid.org/0000-0002-5251-7218 (RB)

Received: Revised: August 2, 201<sub>Accepted:</sub> Published Online in Articles in Advance: April 28,2020

https://doi.org/10.1287/isre.2019.0892

Copyright:

Abstract. The shaky ascent of women up the organizational ladder is a critical factor that may contribute to the lack of women in information technology (IT). In this study, we examine the effect of gender on the likelihood of employee promotions. We further examine whether women get an equal lift in promotion likelihood from performance improvements, work experience, and training as men. We analyze archival promotion data, as well as demographic, human capital, and administrative data for 7,004 employees at a leading IT services firm located in India for the years 2002–2007 and for multiple levels of promotion. We develop robust econometric models that consider employee heterogeneity to identify the differentia effect of gender and performance on promotions. We find that, contrary to expectations, women are more likely to be promoted, on average. However, looking deeper into the heterogeneous main effects using hierarchical Bayesian modeling reveals more nuanced insights. We find that, ceteris paribus, women realize less benefit from performance gains than men, less benefit from tenure within the focal firm, but more benefit from training than men. These results suggest that despite the disparity in returns to performance and experience improvements, women can rely on signaling mechanisms such as training to restore parity in promotions. We find that the effects of gender and performance vary with the level of employee promotion; although not as much as men, women benefit more from performance gains at higher organizational levels. Our findings suggest several actionable managerial insights that can potentially make IT firms more inclusive and attractive to women.

History: Anindya Ghose, Senior Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0892.

Keywords: gender • women in IT • IT human capital • performance • training • promotions • IT services industry

Wanted: More women in technology. (Sprague 2015)

## Introduction and Background

The motivation for this study is the observation that women make up 57% of the U.S. labor market (U.S. Department of Labor 2015b), yet they make up only 23.1% of computer and information technology (IT) occupations (U.S. Department of Labor 2015a). These inequitable trends echo across global IT firms (McGregor 2014, Woetzel et al. 2015).<sup>1</sup> Recent reports even suggest that the number of women in IT jobs has been dropping significantly (Sherman 2015). While gender inequalities in labor market participation are large and globally persistent (International Labour Organization 2014), the glaring underrepresentation of women in the IT industry makes the “glass ceiling” seem particularly pertinent to technology firms (Ahuja 2002, MacMilan 2012, Vara 2014).

Gender equality is desirable not just from humanitarian but also from economic perspectives.<sup>2</sup> Reducing gender disparity by recruiting and retaining more female employees, especially for the IT industry, where women are severely underrepresented, positively affects top-line growth (Woetzel et al. 2015). Despite the obvious benefits of gender parity, several social and structural barriers impede women in advancing their careers within the IT industry (Ahuja 2002). In particular, the lack of female role models and/or mentors in managerial ranks has emerged as one of the critical factors endemic to IT organizations. More women are earning degrees in science, technology, engineering, math, and medicine (STEM), yet many do not opt for IT as a career because they do not find women rising to the top echelons of IT firms or even having successful careers in IT (Mundy 2017). Thus, the lack of women in leadership positions affects not only the inflow of women into IT but also their career growth prospects (Ahuja 2002). The conspicuous dearth of women in technology and leadership roles has been decried in both the academic literature (e.g., Trauth et al. 2009) and the popular press (Vara 2014, Mundy 2017). Yet little systematic research has focused on identifying how women rise in IT organizations.

In this study, we examine how gender affects the likelihood of promotions in the context of the IT industry.

Prior literature suggests that promotions are nonwage incentives aimed at identifying and retaining highability employees (Lazear and Rosen 1981). Firms typically reward good performance with promotions (e.g., Prendergast 1993, Gibbons and Waldman 1999a, DeVaro 2006a, Melero 2010) such that promotions mimic tournaments in an organization’s internal labor market (DeVaro 2006a, b; Lazear 1992). If promotions are arguably driven by employee performance, does the lack of women in higher echelons of IT firms indicate that they are less effective than men? While this strand of research has examined the role of performance on promotions, it is only now that a systematic examination of the interplay between gender and performance on promotions has begun. This examination is especially important to the IT industry, in which tasks such as programming, analysis and design, testing, and project management are seen as “masculine” tasks (Trauth et al. 2004, 2010; Chan and Wang 2017) and women are seen as the archetypal out-group (Ahuja 2002, Trauth et al. 2005, Vara 2014, Mundy 2017). Thus, to understand the pertinent mechanisms affecting promotions, we further examine whether men and women gain similarly from performance improvements in determining promotions. To date, firms have incorporated egalitarian policies that ostensibly prevent discriminatory practices, yet women in IT continue to be visibly absent, and especially so as we move up the organizational ladder. Our research aims to comprehensively identify the role and extent of prejudicial ascriptive biases in the IT work environment that preclude successful careers for women in IT.

Extant research has sought to understand differential labor market outcomes between men and women in hiring, promotions, and wage differences. In particular, research on gender-based discrimination has focused extensively on hiring decisions and wage inequality (Booth et al. 2003, Booth 2009), real or perceived gender differences in competitiveness ( Croson and Gneezy 2009, Buser et al. 2014), and organizational constraints (Ibarra 1997, Ahuja 2002, Trauth et al. 2009, Ibarra and Andrews 2015), yet discrimination in promotion decisions remains under-researched (Sheridan et al. 1997, DeVaro et al. 2018). The current literature that assesses how employee gender and performance affect promotion remains tenuous when it comes to empirical validation (Sheridan et al. 1997); furthermore, it is unclear whether these findings directly translate to the IT industry, where women constitute less than 25% of the IT workforce and rarely rise to influential managerial positions and may be perceived as violating the traditional gender roles by pursuing masculine careers (Trauth et al. 2004, 2010; Chan and Wang 2017), thereby meriting a closer examination.

Finally, prior literature may also be constrained by methodological concerns intrinsic to this problem. Factors such as employee motivation and innate capability (Cappelli 2004) or gender-based self-selection into jobs (Gneezy et al. 2003) may possibly confound the results. Together these factors may hinder a more thorough understanding of how gender, together with performance, affects promotions of women in IT.

We address this gap in the literature by analyzing detailed archival data on promotions, as well as demographic and human capital data, for 7,004 IT professionals from 2002 to 2007 for multiple levels of promotions. The firm, focal in this study, is a leading IT services firm with stellar human resources (HR) practices that invests heavily in formal employee training Using this detailed individual-level data set and a hierarchical Bayesian modeling approach that models heterogeneity of the main effects, we are able to parse out not only the effect of pertinent factors such as performance, human capital investments, work experience, and organizational roles but also how they affect the likelihood of promotions for women versus men.

Surprisingly, at least on the surface, we find that women are more likely to be promoted. We also find that past performance has a positive impact on the likelihood of promotion but that there are differential returns to performance improvements for men and women: female employees are penalized for higher performance. Compared with men, all else being equal, women are also less likely to benefit from experience within the organization. This is suggestive of the fact that they are more likely to be taken for granted. They are, however, more likely to benefit from training, consistent with the literature that suggests that women are less likely to have time to nurture influential mentor networks and instead use training as a signaling mechanism, enhancing promotion likelihood. Together our results reveal a nuanced effect of gender, performance, experience, formal training, and their interactions on employee promotions.

We contribute to the growing body of research on gender issues in IT organizations. In particular, using revealed preference-based individual-level administrative data on promotions at multiple levels, our findings on the negative interaction between gender and performance or gender and experience are consistent with covert forms of discrimination against women in IT, complementing previous studies that relied on self-reported survey data (e.g., Hersch and Viscusi 1996, Melero 2010). In not paying attention to such nuanced sources of bias against women in IT, egalitarian HR policies seeking to stem discriminatory practices may bear little fruit. Our findings also emphasize the palliative effect of mechanisms such as trainingonwomen’s promotability, which help women credibly signal their worth to senior management when they may be less inclined to lean in and directly ask for promotions they feel are due to them.

## Conceptual Framework and Hypotheses

Our conceptual framework explores the theoretical linkages between gender, performance, and promotions. Conventional wisdom suggests that in a meritocratic organization, ceteris paribus, an increase in employees performance should increase the likelihood of their promotion, irrespective of their gender. Nevertheless, the social science and management literature presents mixed evidence with respect to gender, performance, and promotions. For instance, some of this research proposes that once differences between motivation and capability are accounted for, women are found to be at least as likely to be promoted (Lewis 1986, Booth et al. 2003, Buchan et al. 2008). In particular, Lewis (1986) analyzed data for 10,000–12,000 federal employees in white-collar jobs but found no significant differences between the promotion probabilities for men and women once the demographic and occupational attributes were controlled for. In contrast, there is also overwhelming evidence that women are penalized more in terms of career growth and that men are more likely to be promoted compared with women (Darity and Mason 1998, Ibarra et al. 2010, Ellingrud et al. 2015), especially in jobs with “masculine” attributes, such as those in IT (e.g., Darity and Mason 1998, Gneezy et al. 2003, Ibarra et al. 2010).

Although the broader social sciences and management research finds the effect of gender on promotions to be ambiguous and therefore an open empirical question, our focus on women in IT paints a less rosy picture: these women, in taking on job profiles that have traditionally been considered masculine, may not be as likely as men to succeed in such careers (Trauth et al. 2004, 2010; Chan and Wang 2017), reflecting tastebased ascriptive discrimination in performance evaluations (Nieva and Gutek 1980, Wallston and O’Leary 1981, Heilman 2001, Crandall and Eshleman 2003, Lyness and Heilman 2006)<sup>3</sup> and promotions (Becker 1971, Darity and Mason 1998). Extant research suggests that perception of their performance and sociostructural factors impede women’s careers in IT organizations.

In meritocratic organizations, because performance is the single most important factor in promotion decisions, we argue that the link between gender and performancebased promotions in the IT industry is subtler. Whereas absolute performance is desirable, it is only the relative evaluation of performance that leads to promotion for knowledge workers such as those in the IT sector (Rosen 1986, MacCrory et al. 2014). Therefore, factors such as preconceived notions of performance or capability (Landau 1995), gender-role orientation (Judge and Livingston 2008), and gender-biased evaluations (Nieva and Gutek 1980, Heilman 2001) may adversely affect relative performance assessment for women in IT and therefore lower the likelihood of their promotion.

In particular, IT tasks such as programming, analysis and design, testing, and project management are seen as masculine tasks (Trauth et al. 2004, 2010; Chan and Wang 2017). In a male-dominated industry such as IT, women are the quintessential out-group (Ahuja 2002, Trauth et al. 2005, Vara 2014, Mundy 2017) Women in IT are therefore more likely to be perceived as violating the traditional gender roles (Baron and Bielby 1980, Baron et al. 1991, Eagly and Karau 2002, Heilman and Eagly 2008) such that differences in economic outcomes such as promotions for men versus women cannot be attributed to intrinsic gender differences, if any.

We contend that such gender-role orientation (Unger 1976, Judge and Livingston 2008) for women in IT may engender prejudicial behavior on the part of supervisors (Crandall and Eshleman 2003, Choi et al. 2014, Verniers and Vala 2018). Furthermore, organizations that claim to be meritocratic may also suffer from the paradox of meritocracy (Castilla and Benard 2010) that ironically results in lower promotion likelihoods for women in IT. Castilla and Benard (2010) suggest that such structural biases may arise because claiming to be a meritocratic organization could merely be a symbolic gesture adopted for gaining legitimacy (Meyer and Rowan 1977) but not actually implemented (Edelman 1992). It could also be that senior managers in such “meritocratic” organizations may paradoxically believe themselves to be unbiased and thus have moral credentials (Monin and Miller 2001, Choi et al 2014) or be personally objective and therefore unbiased (Uhlmann and Cohen 2007, Castilla and Benard 2010) In such a scenario, they are less likely to closely examine their own motivation and biases and feel justified in expressing their ingrained prejudices (Crandall and Eshleman 2003, Choi et al. 2014) in lowering women’s chances of promotion in IT organizations.

Given these prejudicial biases, as well as the existing sociocultural and structural barriers, we expect women to be at a disadvantage when advancing their careers in the IT industry. We posit the following.

Hypothesis 1. Ceteris paribus, women are less likely to be promoted than men.

The impact of both performance and gender on the likelihood of promotions is clearly understood; it is less clear whether men and women derive commensurate benefits from performance gains. We now elucidate the more nuanced narrative of whether women are penalized or rewarded for better performance compared with men. Milgrom and Oster (1987) examine promotions through the lens of discrimination in labor markets and propose the invisibility hypothesis. In a typical organizational context, although there is uncertainty about the productivity of new employees, it gets resolved over time as firms learn more about these employees’ abilities and productivity. However, it is likely that this uncertainty persists in the external labor market. Because more productive employees are promoted earlier, one way in which other firms can gauge the productivity of an IT employee is through promotions (Waldman 1984, DeVaro and Waldman 2012). Milgrom and Oster (1987) extend this argument to suggest that the normative employee is more visible in that his ability is publicly known, whereas the out-group employee is invisible because her ability is not known ex ante. Therefore, women, being the IT minority, are perceived to be lacking IT capabilities or simply deemed incompetent (Weinberger 2006). This invisibility could arise because of prejudice, more because of such misconceptions than because of antagonism for women, or the consistent presence of old boys’ clubs in IT firms that deem the productivity of male IT employees to be more visible (Morgan et al. 2004). Milgrom and Oster (1987) propose that when a high-ability invisible employee is promoted, the external labor market more accurately perceives her ability, and she becomes more desirable to other firms, making it difficult to retain her without raising her wages. Even for organizations with meritcentric policies of promotion and evaluation, this is not a salubrious situation. As a result, to deter poaching and prevent wage hikes, the dominant strategy for the current employer would be not to promote women (the invisible employee) of high ability.

Research on discrimination against out-groups presents an alternate explanation for why women are unlikely to realize gains similar to men from performance evaluations in being promoted: compensatory stereotype (Igbaria and Baroudi 1995, Carton and Rosette 2011). This theory suggests that managers engage in goalbased stereotyping by rationalizing that women (but not men) fail because of negative attributes and succeed because of positive attributes other than capabilities (i.e., compensatory stereotypes). Consider the previous discussion about women in IT not being expected to be as successful as men in executing masculine tasks such as programing and analysis. When they are unsuccessful in these tasks, managers explain it to be because they are, after all, women in IT and therefore could not be expected to accomplish such masculine tasks. However, when women in IT are successful and perform well at their tasks, it violates these managers gender-role expectations. In such cases, occupational minorities such as women in IT are thought to have compensatory attributes that may explain high performance. Managers may be less likely to attribute female employees’ performance to their domain expertise or technical and analytical capabilities (capabilities that are typically valuable in an IT employee) but instead attribute it to luck or other external factors such as their people skills, their ability to work with various stakeholders, or their “warmth” (Igbaria and Baroud 1995, Yzerbyt et al. 2005, Carton and Rosette 2011) In sum, differences in what the performance is attributed to—ability and skills for men versus luck and external factors for women—are likely to affect women’s promotability. We thus posit the following

Hypothesis 2. Women and men experience differentia outcomes from performance improvements in lifting pro motion likelihood such that, compared with men, women gain less from performance improvements.

## Research Setting and Empirical Analysis Research Setting

To evaluate our hypotheses, we conducted an extensive in-depth field study at a leading IT services vendor headquartered in Bangalore, India. We collaborated and connected with the senior management at the company to enable this research. We held interviews with managers responsible for HR practices such as promotions and employee learning and development in order to understand the firm’s promotion policies, organizational dynamics, and performance evaluation processes.

The firm employed around 70,000 people at the time of data collection, and since then it has grown to around 160,000 employees. The gender ratio of women versus men within the firm is similar to that of many global IT firms, around 23:77 (U.S. Department of Labor 2015a, Woetzel et al. 2015); this ratio persists to date. Most of the projects delivered by the company adapt the waterfall methodology for software production such that there are distinct phases for design, analysis, programming, testing, and implementation (Royce 1970). Dedicated project teams deliver these software projects. The typical career path at this firm reflects this such that an employee progresses along the corporate hierarchy from being a software engineer (SE) to a programmer analyst (PA) to project manager (PM) and further on. Our discussions with senior management at the focal firm suggested that we focus our analysis on employees in the SE, PA, and PM categories for the following reasons: (1) these three rungs constitute the largest portion of the employee pyramid, and (2) these three categories are most critical to human capital development and directly responsible for the success or failure of various projects.<sup>4</sup> We detail their roles and expectations in Table A.1 in the online appendix.

The focal firm follows industry best practices to objectively evaluate adequate performance. To that end, the firm ensures that it has a meticulous performance evaluation process in place. Our interviews revealed that the firm was particularly sensitive to innate gender biases within the IT industry and Indian society. To help provide reviews that are as unbiased as possible, the firm uses a 360-degree feedback system to measure employee performance annually instead of relying just on a supervisor-provided rating. The employee performance evaluation considers how well an employee accomplished specific project-oriented tasks, performance consistency, complexity of the work environment, and adherence to the firm’s values. This elaborate metric incorporates feedback from multiple stakeholders with whom an employee transacts, such as team members, peers, subordinates, and supervisors, thereby providing a comprehensive performance evaluation (see also Bapna et al. 2013). To provide adequate incentive for its employees to improve their performance, the firm uses this performance metric to inform employees’ annual raises.

## Data and Measurement

We collected detailed archival data on 7,004 employees for the years 2002–2007; these employees were randomly selected from the SE/PA/PM employee categories and represent an adequate sample from about 70,000 total firm employees. We were able to gain access to data on an employee’s current and previous roles (e.g., SE, PA, or PM), annual performance ratings, and other pertinent attributes such as the employee’s gender, work experience in years (both at the focal company and the total work experience), time in current role, and complete training records. We describe these data next, and Table provides the summary statistics for the overall sample, as well as for the male and female subsamples.

Promotion. We were able to impute whether and when employees have been promoted by comparing their last and current roles. We code the variable GotPromotion as 1 if we observe the employee being promoted in a particular year and 0 otherwise. We observe two levels of promotions: SE to PA and PA to PM. In our sample, we observe each employee being promoted at most once. In our data set, we observe that 27.16% of employees were promoted from SE to PA, and 21.43% were promoted from PA to PM.

Female. The variable Female is the dummy variable indicating the employee’s gender. This variable is coded as 1 if the employee is female and 0 otherwise. Table 1 shows that 23.4% of our sample are women.

Employee Performance Rating. Each year, the performance evaluation process scores each employee relative to others to yield a relative performance rating. This rating is on a scale from 1 to 4, with 1 indicating the highest performance level, where the employee exceeded expectations, and 4 the lowest, where the employee did not meet expectations. Because of the meticulous and comprehensive nature of the evaluation, we assume that these ratings truly capture relative employee performance (Bapna et al. 2013). Furthermore, because a rating of 1 is better than a rating of 4, any increase in this rating indicates a decrease in employee performance. In order to interpret the coefficients with ease, we use PerfRating (computed as <sup>−</sup>1 × Employee Rating) in our analysis (Langer et al. 2014). As Table 1 shows, the average performance rating is <sup>−</sup>1.776. The average performance rating for women is <sup>−</sup>1.845, and the average performance rating for men is <sup>−</sup>1.755.<sup>5</sup>

Table 1. Data Dictionary and Summary Statistics

<table><tr><td rowspan="2">Variable name</td><td rowspan="2">Variable description</td><td colspan="3">Mean (SD)</td></tr><tr><td>Overall</td><td>Male</td><td>Female</td></tr><tr><td> $GotPromotion_{(t)}$ </td><td>Variable indicating whether promotion occurred in year t or not.</td><td>0.232(0.422)</td><td>0.232(0.422)</td><td>0.231(0.422)</td></tr><tr><td>Female</td><td>Dummy variable indicating the employee&#x27;s gender (1: female; 0: male).</td><td>0.234(0.424)</td><td>—</td><td>—</td></tr><tr><td>PerfRating</td><td>The relative performance rating of the employee, this ranges from 1 (excellent) to 4 (poor). To ease interpretation, we use -1 × PerfRating.</td><td>1.776(0.734)</td><td>1.755(0.734)</td><td>1.845(0.730)</td></tr><tr><td>TotalExp</td><td>An employee&#x27;s total IT work experience in years.</td><td>6.145(2.273)</td><td>6.263(2.351)</td><td>5.757(1.946)</td></tr><tr><td>FirmExp</td><td>An employee&#x27;s work experience at the focal firm in years.</td><td>4.307(2.132)</td><td>4.333(2.163)</td><td>4.224(2.026)</td></tr><tr><td>PriorTraining</td><td>The total number of training courses taken by an employee prior to promotion, normalized by course duration.</td><td>0.669(1.003)</td><td>0.652(0.993)</td><td>0.726(1.104)</td></tr><tr><td>DirectHire</td><td>Dummy variable indicating whether an employee is a direct (from college) or lateral hire (1: direct; 0: lateral).</td><td>0.442(0.497)</td><td>0.432(0.495)</td><td>0.477(0.499)</td></tr><tr><td>LastRole</td><td>Dummy variable indicating the last role: whether SE, PA, or (PM); coded as SE = 0, PA = 1, and PM = 2.</td><td>1.278(0.448)</td><td>1.306(0.461)</td><td>1.189(0.391)</td></tr></table>

Note. SD, standard deviation.

Experience. Prior literature suggests that performance, promotions, and experience are correlated (Joseph et al. 2015). Furthermore, it is possible that the employees who have been longer with the firm are considered more valuable (Slaughter et al. 2007). Hence, we control for an employee’s total (TotalExp) and firmspecific experience (FirmExp); the average experience is 6.14 years, and the average firm experience is 4.31 years. This varies between men and women: men have an average work experience of 6.26 years compared with 5.76 years for women, and men have an average firm-specific experience of 4.33 years compared with 4.22 years for women.

Prior Training. Our data include detailed information on the courses that each employee took, including the names and short descriptions of the courses and the years in which they were taken. These courses were labeled by type, that is, whether they contained content related to domain, technology, behaviors, firm-level processes, or project management methodologies. To compute the training variable, we sum the total number of courses taken by an employee prior to promotion, normalized by the course duration. We find that 27.48% of employees took some training. We examine whether women or men take more training. The t-statistic is <sup>−</sup>0.112, with 47,506 degrees of freedom; the corresponding p-value is 0.911, showing that women and men take statistically the

Subsamples<sup>.</sup> Because we want to isolate the relationship between gender and promotions, we use the detailed demographic data to construct subsamples for our analyses using gender. These subsamples allow us to validate the hypotheses and are useful in analyzing the nuanced relationship between gender, performance, and promotions.

Table 1 describes our variables and provides the summary statistics. The correlation matrix between the dependent and explanatory variables is provided in Table 2. We standardized the relevant variables prior to our analysis to ease interpretation as well as to assuage any collinearity concerns (Aiken and West 1991).

## Methodology

The descriptive statistics provided in Table 1 suggest that there is considerable heterogeneity in our sample.<sup>7</sup> Employee performance and attributes of experience differ across gender, across laterals and direct hires, and across roles. For instance, consider the inherent hierarchy in the organization, where a policy of merit-based promotions portends that competition gets tougher going forward. Therefore, an employee’s current role may moderate the effect of performance on promotion decisions. Likewise, direct hires, in comparison with lateral hires, may manifest specific human capital that is more desirable to senior management, which may, in turn, moderate the effect of performance and hence the likelihood of promotion (Becker 2003, Slaughter et al. 2007). Any examination of the drivers of promotion that does not take into account such intrinsic differences in employees would yield biased coefficient estimates (Gonul and Srinivasan 1993, Venkatesan et al. 2007) These, in turn, would lead to senior management making inferior promotion decisions and implementing suboptimal policies (Allenby and Rossi 1998). Accordingly, we model heterogeneity explicitly in our analysis using a hierarchical Bayesian model-ing approach.

Our dependent variable is binary, and we estimate the following binary logit model to confirm our hypotheses. The primary explanatory variables that inform our model in estimating the likelihood of employees’ promotions are their performance and gender, allowing us to validate Hypothesis 1.

Table 2. Correlation Matrix

<table><tr><td>No.</td><td>Variable name</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>1</td><td> $\text{GotPromotion}_{(t)}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Female</td><td>-0.0015</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td> $\text{PerfRating}_{(t-1)}$ </td><td>0.0543*</td><td>0.0515*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>TotalExp</td><td>0.0057</td><td>-0.0942*</td><td>0.2462*</td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>FirmExp</td><td>0.0202*</td><td>-0.0217*</td><td>0.1173*</td><td>0.2738*</td><td></td><td></td><td></td></tr><tr><td>6</td><td>PriorTraining</td><td>0.0068</td><td>0.0311*</td><td>-0.0957*</td><td>-0.2783*</td><td>0.0583*</td><td></td><td></td></tr><tr><td>7</td><td>DirectHire</td><td>0.0066</td><td>0.0386*</td><td>-0.1097*</td><td>-0.3828*</td><td>0.3595*</td><td>0.2944*</td><td></td></tr><tr><td>8</td><td>LastRole</td><td>0.0016</td><td>-0.1108*</td><td>0.0923*</td><td>0.7259*</td><td>0.3215*</td><td>-0.0469*</td><td>-0.1614*</td></tr></table>

\*Significant at the 5% level.

In addition, we include firm and total experience as pertinent factors:

$$
\begin{array}{r l} & G o t P r o m o t i o n _ {i, t} = \beta_ {0 i} + \beta_ {1 i}. P e r f R a t i n g _ {i, (t - 1)} \\ & \qquad + \beta_ {2 i}. F e m a l e _ {i} + \beta_ {3 i}. F i r m E x p _ {i, t} \\ & \qquad + \beta_ {4 i}. T o t a l E x p _ {i, t} + \varepsilon_ {i, t}, \end{array}\tag{1}
$$

where GotPromotion 1 if GotPromotion $\begin{array} { r } { \imath _ { i , t } ^ { * } > 0 ; } \end{array}$ Got-$P r o m o t i o n _ { i , t } = 0$ otherwise. Thus, the likelihood of promotions can be shown to be

$$
\operatorname * {P r} (G o t P r o m o t i o n _ {i, t} = 1) = \exp [ x _ {i} ^ {\prime}. \beta_ {i} ] / 1 + \exp [ x _ {i} ^ {\prime}. \beta_ {i} ].\tag{2}
$$

In Equations (1) and (2), i is each employee, and t is the year. We have that $G o t P r o m o t i o n _ { i , t }$ is 1 if an employee i is promoted in year t and 0 otherwise, and Female is a dummy variable indicating whether the employee is female (Female = 1) or male $\begin{array} { r } { ( F e m a l e \textbf { = } 0 ) } \end{array}$ . Because promotions depend on how the employee performed in the previous year, we use $P e r f R a t i n g _ { i , ( t - 1 ) }$ as the lagged variable capturing employee performance for the year $( t - 1 )$ . Finally, the variables $F i r m E x p _ { i , t }$ and $T o t a l E x p _ { i , t }$ are the firm-level experience and total experience, respectively, of employee i at time t. We assume the error terms $\varepsilon _ { i , t }$ to be the standard type I extreme value distribution. In the preceding model, $P e r f R a t i n g _ { i , ( t - 1 ) }$ is particularly useful because it encapsulates the effect of prior performance on the likelihood of promotion and hence subsumes some of the unobservable factors (both time invariant and time varying) in the panel model, such as an employee’s capability, inherent drive, and task specificity within a project (Bapna et al. 2013). We use the simplified notation $\beta _ { i } ^ { ' } = [ \mathsf { \bar { \beta } } _ { 0 i } \beta _ { 1 i } \beta _ { 2 i } \beta _ { 3 i } \beta _ { 4 i } ]$ such that $\beta _ { i } ^ { ' }$ denotes all the coefficients in our model that affect the likelihood of an employee’s promotion.

We assume that the employees within the firm vary along the following attributes: whether they were hired directly or laterally, the kind of training that they took prior to promotion, and their place in the organizational hierarchy (whether a software engineer, an analyst, or a project manager). To understand the nuances of this heterogeneity on the model parameters, we estimate a continuous employee heterogeneity model in which we allow the coefficients to be employee specific, as shown in Equation (3):

$$
\begin{array}{c} \beta_ {i} = \delta_ {0} + \delta_ {1}. d D i r e c t H i r e _ {i} + \delta_ {2}. P r i o r T r a i n i n g _ {i} \\ + \delta_ {3}. L a s t R o l e _ {i} + \nu_ {i}, \end{array}\tag{3}
$$

where $\nu _ { i } \sim \mathrm { i i d } \ N ( \theta , V _ { \beta } )$ (iid = independent and identically distributed). The hierarchical relationship shown in Equations (1)–(3) indicates that $\beta _ { i } ^ { ' }$ can be thought of as a function of the three observable employee attributes and allows us to examine the effect of heterogeneity on our model parameters. Denoting $\Delta = [ \delta _ { 0 } \stackrel { \smile } { \delta } _ { 1 } \delta _ { 2 } \stackrel { \bullet } { \delta } _ { 3 } ]$ , this hierarchical relationship is

$$
\begin{array}{c} V _ {\beta} \\ \downarrow \\ \varDelta \end{array} \searrow \beta_ {i} \to y _ {i}.
$$

Thus, $\beta _ { i } ^ { ' }$ becomes a function of the three observable employee attributes and allows us to examine the effect of heterogeneity on our model parameters; the variables $\delta _ { 1 } , \delta _ { 2 } ,$ and $\delta _ { 3 }$ in $\Delta$ specify how $D i r e c t H i r e _ { i } ,$ PriorTraining , and $L a s t R o l e _ { i }$ affect the parameters specified in Equations (1) and (2). For example, $\beta _ { 1 i }$ measures the effect of performance on promotions for employee i. Furthermore, the effect of $D i r e c t H i r e _ { i }$ on $\beta _ { 1 i }$ denotes the differential impact of past performance rating on the likelihood of promotion for direct versus lateral hires. Thus, if $\beta _ { 1 i } < 0$ and $\delta _ { 1 } < 0 ,$ , then a lower performance rating lowers the likelihood of promotions, and this effect is greater for direct hires than it is for lateral hires.

In Equation (3), the random variable $\nu _ { i }$ is the unobservable error component of the employer’s heterogeneity, which we assume to be distributed normally with mean 0 and variance–covariance matrix $V _ { \beta } .$ The model specification in Equations (1)–(3) is quite appealing because it allows us to estimate coefficients at the individual level, which, in turn, allows us to evaluate the precise effect of various employee attributes on promotions. That is, the hierarchical spec ification allows us to understand the moderation effect of direct hires, organizational roles, and prior training on performance, gender, and experience in a more nuanced manner.

We use the hierarchical Bayesian inference process to help with the computation intensity that is typical with such models (Rossi et al. $2 0 0 5 ) . ^ { \mathrm { ~ 8 ~ } }$ In particular, we use standard techniques employed in estimating Bayesian inference models: we set diffuse priors for the model parameters and then apply Markov chain Monte Carlo (MCMC) methods using a Gibbs sampler for data augmentation. Specifically, this semiparametric approach involves draws from the inverse-Wishart distribution in the Gibbs sampler. We run the MCMC simulation for 50,000 draws and only use the last 30,000, discarding the first 20,000 as burn-in. This exercise follows the guidelines about the convergence of the posterior distribution; Figure 1 illustrates the likelihood convergence. In addition to this, we deploy the standard practice of using a thinning parameter of 20—that is, we retain every 20th draw of the posterior distribution—which helps to reduce the associated storage and computational burden for the simulation. The mean rejection rate for the

Figure 1. Values of the Log-Likelihood of the Hierarchical Bayesian Model Evaluated at Posterior Draws of Individual Coefficient Estimates Show Convergence; Every 20th Draw Retained for Analysis  
![](/api/attachments/2B86DYES/fulltext/images/c5fbf74546af8e30cdaab8ede9bc7deb4c85e69c5ab4cd0ab321e297498cdec1.jpg)

Metropolis–Hasting algorithm is 0.79; the desired rejection rate is 0.6–0.9.

Subsample Analysis. In addition to examining the effect of employee attributes on our sample, we are interested in understanding whether the effect of the model coefficients varies between men and women and whether men and women have differential returns to performance improvements in increasing promotion likelihood. Therefore, to validate Hypothesis 2, we analyze Equations (1)–(3) for different subsamples constructed based on employee gender, omitting the variable Female<sub>i</sub> in Equations (1) and (2) from the subsample analysis.

## Results and Discussion

Table 3 reports the population-level parameter estimates $( \overline { { \beta _ { 0 } } } \hat { \beta } _ { 1 } \overline { { \beta _ { 2 } } } \overline { { \beta _ { 3 } } } \overline { { \beta _ { 4 } } } )$ for Equations (1) and (2). Contrary to our expectations, the positive coefficient for Female $( \overline { { \beta _ { 2 } } } = 0 . 2 \dot { 0 } 9 , p < 0 . 0 1 )$ ) indicates that women are, on average, more likely to be promoted. Whereas this result may seem counterintuitive to our hypothesis, several alternate explanations emerge when we take a deeper perspective. First, consider the widely recognized wage differential between men and women (Babcock and Laschever 2003, Spotlight HBR 2013, Leibbrandt and List 2015). Booth et al. (2003) explain that women are more likely to be promoted because they are a “lower cost $o p t i o \dot { n } ^ { \prime \prime }$ than men for tasks that need to be performed at higher organizational levels. Second, in more recent research examining gender, trust, and helpfulness, women are found to be more helpful and trustworthy than men (see Orbell et al. 1994, Buchan et al. 2008). Hence, as employees move to more responsible roles that require increased interactions with various stakeholders (PA compared with SE and PM compared with PA), it is likely that women are perceived to be a better fit. Third, it is also possible that these women are being promoted to a “glass cliff” anchoring projects that are destined to fail (Bruckmüller et al. 2014, Cook and Glass 2014) Fourth, policies and processes implemented at the organizational level that increase transparency and accountability from managers potentially reduced overt biases against women in IT (Lerner and Tetlock 1999, Uhlmann and Cohen 2007, Castilla 2008). Together these factors may explain why women are more likely to be promoted and why Hypothesis 1 is not supported.

As expected, the coefficient for past year’s performance is positive and significant; this result is consistent for the overall sample $( \breve { \beta _ { 1 } } = 1 . 3 1 2 , p < 0 . 0 1 ) ,$ , as well as the male $( \overline { { \beta _ { 1 } } } = 1 . 4 \dot { 8 3 } , p \dot { < } 0 . 0 1 )$ and female $( \overline { { \beta _ { 1 } } } = 1 . 2 4 3 ,$ $p { < } 0 . 0 1 )$ ) subsamples. In Hypothesis 2, it is argued that women are likely the invisible employees whose performance is unknown, and therefore, firms have an incentive to not promote high-performing women to prevent their being poached. Consistent with the extant literature (Igbaria and Baroudi 1995), the effect of performance on promotion likelihood is smaller for women, supporting Hypothesis 2. Thus, a major nuance of our findings is that while on average women are more likely to be promoted, the returns to a marginal improvement in performance are lower for women. Note that all variables are standardized, and thus a comparison of coefficients representing the identical marginal effects across the gender models is valid, and the difference is statistically significant.

Our estimates also indicate an interesting effect of experience on promotions. Firm-level experience is positively associated with the likelihood of promotion $\dot { ( \beta _ { 3 } } = 0 . 7 \dot { 7 } 3 , p < 0 . 0 1 )$ . Again, this effect is smaller for women $( \overline { { \beta _ { 3 M } } } = 0 . 8 5 6 , p \stackrel {  } { < } 0 . 0 1 ; \overline { { \beta _ { 3 F } } } = 0 . 2 2 3 , p < 0 . 0 1 )$ suggesting that spending too long in the same role signals more missed opportunities for promotions for women than for men. Thus, whereas firm-level experience is likely to increase the likelihood of promotion, it may weaken the case for future promotions for women, such that the more time women spend within the focal firm, the more they are taken for granted and higher is their hurdle to promotion. In contrast, experience outside the focal firm, which is associated with market power and outside options, enhances promotion opportunities because the total experience is positively related to promotion $( \overline { { \beta _ { 4 } } } =$ 0.931, ${ \cdot } p { < } 0 . 0 1 )$ ; we find that women benefit more from total experience than men $( \overline { { \beta _ { 4 M } } } = 0 . 7 6 2 , p < 0 . 0 1 ; \overline { { \beta _ { 4 F } } } =$ 2.081, ${ \cdot } p { < } 0 . 0 1 )$ because they are less taken for granted

Table 3. Likelihood of Promotion: Population-Level Estimates

<table><tr><td rowspan="2">Promotion likelihood</td><td colspan="3">Coefficient (SE)</td></tr><tr><td>Overall</td><td>Male</td><td>Female</td></tr><tr><td>Performance (t-1)</td><td>1.3123**(0.0034)</td><td>1.4834**(0.0036)</td><td>1.2434**(0.0092)</td></tr><tr><td>Female</td><td>0.209**(0.0013)</td><td></td><td></td></tr><tr><td>Firm experience</td><td>0.7727**(0.0068)</td><td>0.8564**(0.0077)</td><td>0.2233**(0.0204)</td></tr><tr><td>Experience</td><td>0.9310**(0.0105)</td><td>0.7619**(0.0108)</td><td>2.0807**(0.0404)</td></tr><tr><td>Intercept</td><td>-1.9352**(0.0129)</td><td>-2.002**(0.014)</td><td>-1.3216**(0.0374)</td></tr></table>

Note. Standard errors are in parentheses.  
\*\*Significant at the 1% level.

Tables 4–6 report the estimation results of the posterior distribution of the hierarchical regression coefficients in Equation (3) for the overall sample, male subsample, and female subsample, respectively. These estimates offer several interesting insights. First, the heterogeneity variables are all positively associated with $\beta _ { 1 } ,$ the coefficient measuring the effect of performance gains on promotion likelihood. The reader is advised to read across row 1 of Tables 4–6 to interpret this. We find that, intrinsically, performance is positively associated with promotion likelihood: $\delta _ { 0 }$ is positive and significant for all three analyses. Further, the hierarchical Bayesian model capturing individuallevel heterogeneity reveals that direct hires benefit more from performance gains, prior training is complementary to performance and to women, and those higher up in the organizational hierarchy reap more from performance improvements.

Some of these results speak to the specific human capital that direct hires garner in an organization; for the same total work experience, direct hires would have been longer in the focal organization and more in tune with the organizational goals, and their performance accomplishments are more likely to be perceived as more valuable to the firm (Becker 2003, Slaughter et al. 2007), leading to the complementary relationship between direct hires and performance. Further, the complementary relationship between training and performance (Becker 1962) suggests that it is likely that employees with superior performance are better able to use their training to improve future productivity, send stronger signals, or indicate their future trainability and hence enhance their chances of a promotion (Spence 1973). The positive coefficients (<sup>Δ</sup>) in Table 4 for performance validate the theoretical predictions of DeVaro and Waldman (2012) and can provide precise predictions about the linkage between performance and promotions at the individual and cohort levels for firms.

Tables 5 and 6 show how these coefficients diffe among men and women. Women intrinsically benefit less from performance gains, especially when they are direct hires $( \delta _ { 1 \mathrm { M } } = 0 . 1 7 \bar { 1 } , p < 0 . 0 \bar { 1 } ; \delta _ { 1 \mathrm { F } } = 0 . 1 0 4 , p < \bar { 0 } . 0 1 )$ This is again suggestive of the fact that in the absence of market power and outside options that go along with laterals, women within the company’s hiring and promotion ladder are more likely to be taken for granted. This is further reflected in the fact that compared with men, they seem to benefit less from performance gains at higher levels $( \delta _ { 3 \mathrm { M } } = 0 . 5 7 2 , p <$ $\bar { 0 . 0 1 ; \delta _ { 3 \mathrm { F } } } = 0 . 4 \bar { 0 5 } , p < 0 . 0 1 )$ ), suggesting that the bar gets disproportionately higher with time and tenure for women. There is no clear ex ante theoretical rationale for this. Nonetheless, it is interesting to note that even though women do not realize benefits similar to men from performance gains, they seem to get more rel ative benefits from better performance at higher organizational levels. An increase of one unit in performance for a woman increases the promotion probability from 0.390 to 0.637 (an increase of 63.3%, compared with 146.53% for men) at the software engineer level, but from 0.017 to 0.066 (an increase of 290.65%, compared with 475.23% for men) at the programmer analyst level. We reasoned that the effect of performance improvement on promotion likelihood is lower for women to prevent poaching of the invisible minority (Milgrom and Oster 1987), but our results suggest that this effect varies within the organizational hierarchy. Whereas th desire to prevent poaching is still a factor, the fit of women’s supposed compensatory attributes, such as people and communication skills and warmth, with the more managerial role of PM manifests in ou findings that high-performing women are penalized less when being promoted to PM than when being promoted to PA (Yzerbyt et al. 2005, Carton and Rosette 2011).

Second, the effect of the heterogeneity variables on $\beta _ { 2 }$ is considerably varied, although the intrinsic effect

Table 4. Likelihood of Promotion: Heterogeneity Estimates for the Overall Sample

<table><tr><td>Promotion likelihood</td><td>Intercept</td><td>Direct hire</td><td>Prior training</td><td>Last role</td></tr><tr><td>Performance (t-1)</td><td>0.5374**(0.001)</td><td>0.1473**(0.0005)</td><td>0.1854**(0.0003)</td><td>0.4395**(0.0007)</td></tr><tr><td>Female</td><td>0.2665**(0.0015)</td><td>-0.003**(0.001)</td><td>0.0881**(0.0004)</td><td>-0.0957**(0.0011)</td></tr><tr><td>Firm experience</td><td>1.8002**(0.0012)</td><td>-0.2519**(0.0014)</td><td>0.3821**(0.0004)</td><td>-0.9293**(0.0007)</td></tr><tr><td>Experience</td><td>-1.6526**(0.0015)</td><td>1.0566**(0.0016)</td><td>0.3647**(0.0005)</td><td>1.3952**(0.0009)</td></tr><tr><td>Intercept</td><td>1.1744**(0.0009)</td><td>-0.1172**(0.001)</td><td>0.0586**(0.0003)</td><td>-2.4184**(0.0007)</td></tr></table>

Note. Standard errors (SE) are in parentheses  
\*\*Significant at the 1% level.

Table 5. Likelihood of Promotion: Heterogeneity Estimates for the Male Subsample

<table><tr><td>Promotion likelihood</td><td>Intercept</td><td>Direct hire</td><td>Prior training</td><td>Last role</td></tr><tr><td>Performance (t-1)</td><td>0.5539**(0.0013)</td><td>0.1705**(0.0008)</td><td>0.1666**(0.0004)</td><td>0.5717**(0.0009)</td></tr><tr><td>Firm experience</td><td>1.8848**(0.0018)</td><td>-0.0806**(0.0026)</td><td>0.3381**(0.0006)</td><td>-0.9462**(0.0011)</td></tr><tr><td>Experience</td><td>-1.5989**(0.0021)</td><td>0.7692**(0.0034)</td><td>0.3742**(0.0006)</td><td>1.3116**(0.0013)</td></tr><tr><td>Intercept</td><td>1.0032**(0.0017)</td><td>-0.2622**(0.0017)</td><td>0.0802**(0.0005)</td><td>-2.247**(0.0014)</td></tr></table>

Note. Standard errors are in parentheses.  
\*\*Significant at the 1% level.

$\delta _ { 0 }$ was positive for the overall sample, as also evidenced by ${ \overline { { \beta _ { 2 } } } } .$ . Women who are direct hires gain less than laterals $\overline { { ( } } \delta _ { 1 } = - 0 . 0 0 3 , p < 0 . 0 1 ,$ ); however, they gain more from training $( \delta _ { 2 } = 0 . 0 8 8 , p < 0 . 0 1 )$ ). Interestingly, taking training, a more passive-aggressive form of signaling the desire to improve, learn, and be ready to lead is shown to be beneficial to women. As the analysis indicates, they benefit more from training $( \delta _ { 2 \mathrm { M } } \mathrm { \dot { = } } 0 . 1 6 7 , p < 0 . 0 1 ; \dot { \delta _ { 2 \mathrm { F } } } = 0 . 2 4 9 , p < 0 . 0 1 )$ . This effect is demonstrated in the finding that training enhances the effect of firm and total experience for women more than men. As an example, consider the effect of a oneunit increase in training in the promotion probability for a direct-hire software engineer with average performance. For a woman in this position, the promotion probability is increased by 8.53%, compared with a 6.73% increase for a man in this same position. At a higher organizational level (e.g., a PA seeking to be a PM), a one-unit increase in training increases the probability of promotion by 14.51% for a female employee compared with 8.14% for a male employee. Women face more time constraints because of family and other obligations (Ahuja 2002, Bianchi et al. 2012, Kamp Dush et al. 2018). They are less likely to have time to nurture peer and mentor networks that enhance the likelihood of promotions. Therefore, female employees likely identify training as a structured approach to advance in their careers as opposed to ad hoc personal interconnections. Consistent with the logic presented earlier, our results also suggest that training enhances the effect of firm and total experience for women more than men and that this effect gets stronger as women rise up the value chain, indicating the strength of this credible signal in getting promotions.

Table 6. Likelihood of Promotion: Heterogeneity Estimates for the Female Subsample

<table><tr><td>Promotion likelihood</td><td>Intercept</td><td>Direct hire</td><td>Prior training</td><td>Last role</td></tr><tr><td>Performance (t-1)</td><td>0.5008**(0.0047)</td><td>0.104**(0.0027)</td><td>0.2487**(0.0014)</td><td>0.4046**(0.0034)</td></tr><tr><td>Firm experience</td><td>1.6568**(0.0072)</td><td>-1.2186**(0.0061)</td><td>0.5518(0.002)</td><td>-1.0355**(0.0043)</td></tr><tr><td>Experience</td><td>-2.1628**(0.0082)</td><td>2.6526**(0.0075)</td><td>0.4839**(0.0024)</td><td>2.0435**(0.005)</td></tr><tr><td>Intercept</td><td>2.5344**(0.006)</td><td>0.633**(0.0033)</td><td>0.138**(0.0014)</td><td>-3.6142**(0.0061)</td></tr></table>

\*\*Significant at the 1% level.  
Note. Standard errors are in parentheses.

## Robustness Checks and Endogeneity

Although the employees in our sample were randomly selected, in considering alternate specifications, we need to account for potential endogeneity in our model before we ascribe a causal linkage between these variables and the likelihood of promotions. The proposed Bayesian inference model is semiparametric and hence not as restrictive as classical inference models in its assumptions of exogeneity, but any alternate specification requires instrumental variables to account for endogenous performance or human capital variables. To do so, we use the following Arellano–Bover/ Blundell–Bond dynamic panel model (Arellano and Bover 1995, Blundell and Bond 1998) with robust standard errors:

$$
\begin{array}{r} G o t P r o m o t i o n _ {i, t} = \beta_ {0} + \beta_ {1}. G o t P r o m o t i o n _ {i, (t - 1)} \\ + \beta_ {2}. P e r f R a t i n g _ {i, (t - 1)} \\ + \beta_ {3}. T r a i n i n g _ {i, (t - 1)} + \varepsilon_ {i, t}. \end{array}\tag{4}
$$

In addition to the lagged dependent variable (Got-$P r o m o t i o n _ { i , t } ) .$ , we use past performance and past train ing as explanatory variables (Bapna et al. 2013). The structure of the dynamic panel model is such that we can construct instruments using lagged values of our dependent variable, wherein these instruments have been shown to be uncorrelated with the error term. Note that this model is unable to account for any time-invariant variable such as Female. We estimate the model specified in Equation (4) for the overall sample and then separately for the two subsamples for men and women.

Table 7 presents the results from the dynamic panel specification. Overall, this model suggests that past promotion, past performance, and past training investments are positively related to promotion likelihood. Examining columns (2) and (3), we find that past promotion is positive and significant for men only, whereas the performance gains are significantly higher for men compared with women. Both of these results support our previous findings. We also find that women gain better economic return from training investments.

In summary, our overall results indicate that women in IT may not face blatant disadvantages in promotion decisions.<sup>10</sup> Indeed, on average, they are more likely to get promoted than men, ceteris paribus. Our current analysis is limited in its data to be able to pin down the exact mechanism for this. The literature points out that pay differentials could account for some of this; for the same job, women are a cheaper resource for profit-maximizing firms (Castilla and Benard 2010, Albanesi et al. 2015). Alternatively, it could be linked to issues of superior soft skills (Blau and Kahn 2000, Bruckmüller et al. 2014). Whereas future research is needed to examine this aspect, we do have striking evidence of heterogeneity in the gender effect.

Our findings are plausibly suggestive of covert discrimination (Swim et al. 1995) owing to the differential returns from performance gains, where, as reasoned by the invisibility hypothesis, high-performing women are less likely to be promoted (Milgrom and Oster 1987). Put differently, all else being equal, women performing at the same level as men are less likely to get promoted. Further, all else being equal, women with longer tenure in the company are less likely to be promoted. This is strong evidence that they are taken for granted, because the effect flips to a positive sign for women hired from the outside.

These prejudicial tactics against women are somewhat mitigated by them, arguably in a passiveaggressive fashion, by taking training. Training has a strong positive effect, all else being equal, for women seeking an alternative, less-in-your-face vehicle for climbing the promotion ladder. Thus, we argue that human capital investments such as training (Acemoglu 1997) may help women provide credible signals to circumvent structural impediments in technology firms (Gibbons and Waldman 1999b). Moreover, women, who may be less inclined to lean in and directly ask for promotions that they feel are due to them are relatively more amenable to using these signals (Ibarra 1992, Ahuja 2002). Our results suggest that training serves as a signaling mechanism that helps women circumvent traditional biases and notions and establish their credentials as capable and driven IT employees. As we conclude in the next section, our findings have important implications for senior managers as they balance gender bias and reward employees for performance improvements and skills acquisition via promotions.

## Conclusions and Directions for Future Research

The dearth of women in IT, which is well documented by both academia and industry, has been attributed in part to the lack of women in the higher echelons of the organizational ladder, which not only affects the immediate career prospects of women in IT but also dissuades women who want to be part of IT labor markets (Ahuja 2002). Whereas performance has long been understood to be the primary factor affecting promotions, the paucity of granular data has led to only an imperfect understanding of the interplay between gender and performance as they affect promotions for women in IT. In this study, we investigate the factors affecting women’s rise in IT organizations. Our primary focus is on examining the role of gender on promotions in IT firms, but we also examine whether men and women experience differential or commensurate returns from performance gains in augmenting promotion likelihood.

Our study uses a unique setting in which to examine this research question—a leading IT services provider headquartered in India. At the time of this study, the firm employed close to 70,000 employees and made significant investments in processes geared toward fair promotion, training, and evaluation for its employees. We gained access to detailed archival and administrative data on promotions, demographics, performance, and training for 7,004 employees from 2002 to 2007. This comprehensive data set affords us the opportunity to examine the effect of not only gender but also performance for different levels of promotion (from SE to PA to PM) and for lateral versus direct hires.

Our findings reveal that gender is a strong predictor of the likelihood of promotion. Contrary to our expectations, we find that women are more likely to be promoted than men. We offer several alternate explanations for the pure gender effect revealed in our findings. First, considering the wage differential between men and women, we posit that women are more likely to be promoted because they are a lowercost option compared with men for the task that needs to be performed at the higher level of organizational ladder. Second, recent studies suggest that women might be more helpful and trustworthy than men. Hence, as employees move into roles with greater responsibility that require increased social interactions with various stakeholders, it is likely that women are perceived to be a better fit. Such a promotion strategy may also reflect glass cliffs such that women are promoted to be part of failing projects (Cook and Glass 2014). Finally, it is possible that equitable organizational policies result in more transparency and accountability from managers and reduce blatant biases against women (Lerner and Tetlock 1999, Castilla 2008). Together these factors may explain why women are more likely to be promoted. We also argued that gains from performance improvements in increasing promotion likelihood are lower for women. We find that women may be penalized for better performance in that their promotion likelihood increases with performance at a lesser rate than for men. Considering that women are an occupational minority in the IT industry, it is likely that their competence is not known except to their employers; therefore, a firm has an incentive not to promote women with high performance and keep them “hidden” from competing firms (Milgrom and Oster 1987). It is also possible that senior management may attribute their performance less to ability than to luck, and hence women do not gain as much from performance improvements (e.g., Carton and Rosette 2011).

Table 7. Robustness Checks: Dynamic Panel Model

<table><tr><td>Promotion likelihood</td><td>Overall</td><td>Male</td><td>Female</td></tr><tr><td>Promotion (t-1)</td><td>0.0897**(0.0274)</td><td>0.1142**(0.032)</td><td>0.0094(0.0525)</td></tr><tr><td>Performance (t-1)</td><td>0.4395**(0.0157)</td><td>0.4608**(0.0187)</td><td>0.3576**(0.0278)</td></tr><tr><td>Training (t-1)</td><td>0.0578**(0.0109)</td><td>0.038**(0.0129)</td><td>0.129**(0.0197)</td></tr><tr><td>Intercept</td><td>0.2792**(0.0077)</td><td>0.2524**(0.2524)</td><td>0.3559**(0.0133)</td></tr></table>

Notes. Standard errors are in parentheses. Postestimation Sargan test of overidentifying restrictions failed to reject the null hypothesis (Hypothesis 0) that overidentifying restrictions are valid, with Prob > χ<sup>2</sup> = 0.228 (overall sample), 0.155 (male subsample), and 0.834 (female subsample) respectively. \*\*Significant at the 1% level.

Further, we find that women benefit disproportionately more from training. Although our study does not delineate why it may be so, it is possible that women may be more opportunistic when it comes to enrolling for courses that ensure faster promotions, or they may imbibe knowledge more effectively and are more adept at translating knowledge gains into promotability and/or signaling (Becker 1962, 2003; Stiglitz 1975). This allows them to circumvent any social and structural biases that may have otherwise prevented their climb up the corporate ladder, leading to promotions.

We believe that the strength, robustness, consistency, and validity of our findings stem from (1) using detailed employee data for gender, performance, experience, and training for multiple levels of promotion that provide an adequate backdrop for examining the more intricate predictions of theories from economics and social sciences, and (b) employing robust empirical specifications that address the heterogeneous differences between employees. The validity of our results is reflected in their consistency across different specifications, including those that account for endogenous constructs such as motivation and drive that affect performance.

Our study contributes to the extant literature on IT labor markets in several important ways. First, we contribute to research on promotions and tournaments by positioning gender as an important determinant of promotions for women in IT. Ours is one of the first studies to unequivocally establish the economic significance of performance, outside experience, and training for women in IT seeking promotions. In sum, our study draws from and contributes to the labor economics and social sciences literature to provide a more nuanced but complete picture of the linkages between gender, relative employee performance, human capital investments, and promotions in the context of knowledge workers.

Our findings also have important implications for senior executives as they manage their human capital (Luftman et al. 2009). Prior studies suggest that women lack influential mentoring networks (e.g., Ibarra 1993), leading to differences in how women are evaluated and promoted within an organization. Our primary managerial implication is that training helps women with low performance by thwarting any structural biases that may have otherwise inhibited them, especially at higher levels of promotion, underscoring the importance of training as a credible signal of ability and value. Although many IT organizations have diligently pursued unbiased evaluation and promotion practices, it is likely that subtle biases persist. Senior managers can instill best practices such that women use training as a way to ameliorate any gender issues and climb the organizational ladder faster. Further, we find that training and performance are complementary such that training can help employees with high performance rise faster in the organizational hierarchy. Therefore, managers can nurture their high-performing employees and provide them with resources to excel even more. Further, prior re search suggests that fair evaluations and training are exemplary HR practices that affect firm performance positively (Delaney and Huselid 1996). Our study suggests that the adoption of processes and policies that limit an individual manager’s discretion (Elvir and Graham 2002) and promote transparency and accountability (Lerner and Tetlock 1999, Castilla 2008), as well as the adoption of adequate managerial incentives (Sherf et al. 2018) that go beyond symbolic gestures, will also help reduce biases against women in IT. In essence, such practices create a virtuous cycle; employees witness the value in investing in training to foster their growth within the organization and thereby improve their own, and consequently the firm’s, performance; managers understand that they will be held accountable for biases but will also enjoy suitable rewards in being more equitable and fairer. Finally, we note that although focused on IT labor markets, the findings of this research are generalizable to women in other male-dominated industries, such as those in STEM.

## Limitations and Future Research

Like all research, this study has limitations and provides opportunities for further study. We rely on critical data around three representative positions in the IT services work ladder from a single firm. It is possible that the results may not generalize to other firms or to other positions such as data analyst or data scientist. However, this firm has exemplary HR practices and resembles not only the other top-five competitors within India but also global IT giants such as IBM and Accenture, which operate captive centers in India and garner close to 80% of the Indian IT services market share. Although the growth in this sector portends wider appreciation and applicability of our findings and implications (Bartel et al. 2014), we caution readers that our results may not generalize to firms that do not yet have process-oriented HR practices that inhibit overt gender biases. Additionally, we are hampered by not having access to wage data, which could offer a more comprehensive insight into biases against women in IT. Finally, we note that our data analysis is limited to lower levels of promotion. Therefore, our findings may not take into account the risk-loving and competitive behavior sought in executive positions (Gneezy et al. 2003), where many of the gender issues surface. It would be interesting to understand how gender, performance, experience, and training dynamics change as one examines the higher echelons of the corporate ladder (Powell and Butterfield 1994).

We hope that future work can use wage and promotion data to develop new insights. For instance, future research could examine discrimination against women in IT taking into account societal and countrylevel norms. Future research can further examine how factors such as peer and mentor networks impact employee promotions.

## Acknowledgments

This paper has profited from the feedback and encouragement of many people. The authors thank Anindya Ghose for his valuable guidance and advice during the review process. The authors are also grateful to the participants of the 2014 Workshop on IS Economics (WISE), Auckland, New Zealand; the 2015 Symposium on Statistical Challenges in Electronic Commerce Research, Addis Ababa, Ethiopia; and the 2015 Sandra A. Slaughter Software Conference, Scheller College of Business, Georgia Tech, Atlanta, Georgia, as well as the seminar participants at the Rensselaer Polytechnic Institute, University of Illinois at Urbana–Champaign, Arizona State University, University of Pittsburgh, and University of Oklahoma for their constructive comments on earlier versions of the paper. Last, but not the least, the authors are indebted to the senior management at their research site for believing in the premise of this research, for providing them with the panel data, and for answering their queries patiently and meticulously. All errors remain the authors’.

## Endnotes

<sup>1</sup> A diversity report released by Google in 2014 indicates that only 30% of its employees are women; in technical jobs, the search giant employs only 17% women (McGregor 2014).

<sup>2</sup> A recent report published by the Organisation for Economic Cooperation and Development (2012) finds that parity between men and women in labor markets in developed countries is expected to increase their gross domestic product (GDP) by 12% by 2030. Gender disparity is even more acute in Asia, and particularly so in India. If India and China matched the gender parity that exists in Singapore, then the incremental gains in GDP would amount to \$3.2 trillion (Woetzel et al. 2015).

<sup>3</sup> Research has also shown that any performance shortfall on the part of men often may be explained away as occurring because of adverse work conditions (such as a tough client, risky technology, and more competition); however, women are more likely to be subjected to harsher criticism and blamed for their inadequate capabilities, resulting in performance shortfalls rather than any unfavorable work environ ment (Park and Westphal 2013).

<sup>4</sup> From this study’s perspective, these are the formative rungs, and it is important to examine concomitant biases at these early career stages when these can potentially be fixed; these biases may be exacerbated or confounded at later career stages (Gneezy et al. 2003).

<sup>5</sup> The t-statistic assuming equal variances is 8.569 with 27,630 degrees of freedom, yielding a p-value of <0.0001, indicating that men’s ratings are slightly better than those of women.

<sup>6</sup> A probit model estimating the propensity to take training shows that the coefficient for Female is insignificant; thus, there are no differences between women and men in their propensity to take training. The results for this regression are available from the authors upon request.

<sup>7</sup> For the sake of brevity, in Table 1, we report only the descriptive statistics for the overall sample and for samples for both men and women. We are happy to provide these statistics for different sub samples, such as those for direct versus lateral hires and those across different roles, on request.

<sup>8</sup> Estimation using Bayesian inference techniques can be more parsimonious in its data requirements because the estimation procedure is able to partially pool data across observations and thus present more information that can help estimate the individual-specific parameters (Allenby and Rossi 1998, Rossi et al. 2005). Allenby and Rossi (1998) offer more discussion on the appeal and constraints of Bayesian inference.

<sup>9</sup> For instance, although gender is exogenous, there is a possibility that performance is endogenous; employee motivation and innate drive could influence employee performance. Further, the firm’s commitment to provide incentives such as promotions and fair evaluations may attract high-performing individuals (Cappelli 2004). Classical econometric models mandate that we account for this endogeneity, or else we may overestimate the marginal effect of performance on the likelihood of promotions. In other words, a naive probability model would measure the marginal effect not of the performance but rather of the combined effect of performance improvement and being identified as an employee who improves a marginal performance.

<sup>10</sup> We provide additional robustness checks in Table A.1 in the online appendix. We further highlight the importance of considering employee-level heterogeneity in modeling promotion decisions in the online appendix. Table A.2 in the online appendix compares the model-fitting statistics for these models, that is, the proposed model in Equations (1)–(3), with alternate specifications; our proposed model fares better than these competing models, indicating that accounting for employee heterogeneity is critical for policy and management decisions.

## References

Acemoglu D (1997) Training and innovation in an imperfect labour market. Rev. Econom. Stud. 64(3):445–464.

Ahuja MK (2002) Women in the information technology profession: A literature review, synthesis and research agenda. Eur. J. Inform. Systems 11(1):20–34.

Aiken LS, West SG (1991) Multiple Regression: Testing and Interpreting Interactions (Sage Publications, Newbury Park, CA)

Albanesi S, Olivetti C, Prados MJ (2015) Gender and dynamic agency: Theory and evidence on the compensation of top executives. Res. Labor Econom. 42:1–59.

Allenby GM, Rossi PE (1998) Marketing models of consumer het erogeneity. J. Econometrics 89(1–2):57–78.

Arellano M, Bover O (1995) Another look at the instrumental variable estimation of error-components models. J. Econometrics 68(1):29–51.

Babcock L, Laschever S (2003) Women Don’t Ask: Negotiation and the Gender Divide (Princeton University Press, Princeton, NJ)

Bapna R, Langer N, Mehra A, Gopal R, Gupta A (2013) Human capital investments and employee performance: An analysis of IT services industry. Management Sci. 59(3):641–658.

Baron JN, Bielby WT (1980) Bringing the firms back in: Stratification, segmentation, and the organization of work. Amer. Sociol. Rev. 45(5):737–765.

Baron JN, Mittman BS, Newman AE (1991) Targets of opportunity: Organizational and environmental determinants of gender integration within the California Civil Service, 1979–1985. Amer. J. Sociol. 96(6):1362–1401.

Bartel AP, Beaulieu ND, Phibbs CS, Stone PW (2014) Human capital and productivity in a team environment: Evidence from the healthcare sector. Amer. Econom. J. Appl. Econom. 6(2): 231–259.

Becker GS (1962) Investment in human capital: A theoretical analysis. J. Political Econom. 70(5):9–49.

Becker GS (1971) The Economics of Discrimination, 2nd ed. (University of Chicago Press, Chicago, IL)

Becker GS (2003) Human Capital: A Theoretical and Empirical Analysis with Special Reference to Education, 3rd ed. (University of Chicago Press, Chicago, IL)

Bianchi SM, Sayer LC, Milkie MA, Robinson JP (2012) Housework: Who did, does or will do it, and how much does it matter? Soc. Forces 91(1):55–63.

Blau F, Kahn L (2000) Gender differences in pay. J. Econom. Perspect. 14(4):75–99.

Blundell R, Bond S (1998) Initial conditions and moment restrictions in dynamic panel data models. J. Econometrics 87(1): 115–143.

Booth AL (2009) Gender and competition. Labour Econom. 16(6):599–606.

Booth AL, Francesconi M, Frank J (2003) A sticky floors model of promotion, pay, and gender. Eur. Econom. Rev. 47(2):295–322.

Bruckmüller S, Ryan MK, Rink F, Haslam SA (2014) Beyond the glass ceiling: The glass cliff and its lessons for organizational policy. Soc. Issues Policy Rev. 8(1):202–232.

Buchan NR, Croson RTA, Solnick S (2008) Trust and gender: An examination of behavior and beliefs in the investment game. J. Econom. Behav. Organ. 68(3–4):466–476.

Buser T, Niederle M, Oosterbeek H (2014) Gender, competition and career choices. Quart. J. Econom. 129(3):1409–1447.

Cappelli P (2004) Why do employers pay for college? J. Econometric 121(1–2):213–241.

Carton AM, Rosette AS (2011) Explaining bias against black leaders: Integrating theory on information processing and goal-based stereotyping. Acad. Management J. 54(6):1141–1158.

Castilla EJ (2008) Gender, race, and meritocracy in organizational careers. Amer. J. Sociol. 113(6):1479–1526.

Castilla EJ, Benard S (2010) The paradox of meritocracy in organi zations. Admin. Sci. Quart. 55(December):543–576.

Chan J, Wang J (2017) Hiring preferences in online labor markets: Evidence of a female hiring bias. Management. Sci. 64(7): 2973–2994.

Choi B, Crandall CS, La S (2014) Permission to be prejudiced: Legitimacy credits in the evaluation of advertisements. J. Appl. Soc. Psych. 44(3):190–200.

Cook A, Glass CM (2014) Analyzing promotions of racial/ethnic minority CEOs. J. Management Psych. 29:440–454.

Crandall CS, Eshleman A (2003) A justification-suppression model of the expression and experience of prejudice. Psych. Bull. 129(3): 414–446.

Croson R, Gneezy U (2009) Gender differences in preferences. J. Econom. Lit. 47(2):448–474.

Darity WA Jr, Mason PL (1998) Evidence on discrimination in employment: Codes of color, codes of gender. J. Econom. Perspect. 12(2):63–90.

Delaney JT, Huselid MA (1996) The impact of human resource management practices on perceptions of organizational per formance. Acad. Management J. 39(4):949–969.

DeVaro J (2006a) Internal promotion competitions in firms. Rand J. Econom. 37(3):521–542.

DeVaro J (2006b) Strategic promotion tournaments and worke performance. Strategic Management J. 27(8):721–740.

DeVaro J, Ghosh S, Zoghi C (2018) Job characteristics and labor market discrimination in promotions: New theory and empiri cal evidence. Indust. Relations 57(3):389–434.

DeVaro J, Waldman M (2012) The signaling role of promotions: Furthe theory and empirical evidence. J. Labor Econom. 30(1):91–147.

Eagly AH, Karau SJ (2002) Role congruity theory of prejudice toward female leaders. Psych. Rev. 109(3):573–598

Edelman LB (1992) Legal ambiguity and symbolic structures: Or ganizational mediation of civil rights law. Amer. J. Sociol. 97(6): 1531-1576

Ellingrud K, Riefberg V, Technology I, Maybank A, Us F, Popular M, Blogs G, et al. (2015) Women in the workplace: A research roundup. Harvard Bus. Rev. 88(September):86–91.

Elvira MM, Graham ME (2002) Not just a formality: Pay system formalization and sex-related earnings effects. Organ. Sci. 13(6): 601–617.

Gibbons R, Waldman M (1999a) A theory of wage and promotion dynamics inside firms. Quart. J. Econom. 114(4):1321–1358.

Gibbons R, Waldman M (1999b) Careers in organizations: Theory and evidence. Handbook Labor Econom. 3:2373–2437.

Gneezy U, Niederle M, Rustichini A (2003) Performance in competitive environments: Gender differences. Quart. J. Econom. 118(3):1049–1074.

Gonul F, Srinivasan K (1993) Modeling multiple sources of heterogeneity in multinomial logit models: Methodological and managerial issues. Marketing Sci. 12(3):213–229.

Heilman ME (2001) Description and prescription: How gender ste reotypes prevent women’s ascent up the organizational ladder. J. Soc. Issues 57(4):657–674

Heilman ME, Eagly AH (2008) Gender stereotypes are alive, well, and busy producing workplace discrimination. Indust. Organ. Psych. 1(4):393–398.

Hersch J, Viscusi WK (1996) Gender differences in promotions and wages. Indust. Relations 35(4):461–472.

Ibarra H (1992) Homophily and differential returns: Sex differences in network structure and access in an advertising firm. Admin. Sci. Quart. 37(3):422–447.

Ibarra H (1993) Personal networks of women and minorities in management: A conceptual framework. Acad. Management Rev. 18(1):56–87.

Ibarra H (1997) Paving an alternative route: Gender differences in managerial networks. Soc. Psych. Quart. 60(1):91–102.

Ibarra H, Andrews SB (2015) Power, social influence, and sense making: Effects of network and centrality proximity on employee perceptions. Admin. Sci. Q. 38(2):277–303.

Ibarra H, Carter NM, Silva C (2010) Why men still get more promotions than women. Harvard Bus. Rev. 88(9):80–85.

Igbaria M, Baroudi J (1995) The impact of job performance evaluations on career advancement prospects: An examination of gender differences in the IS workplace. Management Inform. Systems Quart. 19(1):107–123.

International Labour Organization (2014) Global employment trends 2014: Risk of a jobless recovery? Report, International Labour Office, Geneva.

Joseph D, Ang S, Slaughter SA (2015) Turnover or turnaway? Competing risks analysis of male and female IT professionals’ job mobility and relative pay gap. Inform. Systems Res. 26(1):145–164.

Judge TA, Livingston BA (2008) Is the gap more than gender? A longitudinal analysis of gender, gender role orientation, and earnings. J. Appl. Psych. 93(5):994–1012.

Kamp Dush CM, Yavorsky JE, Schoppe-Sullivan SJ (2018) What are men doing while women perform extra unpaid labor? Leisure and specialization at the transitions to parenthood. Sex Role 78(11–12):715–730.

Landau J (1995) The relationship of race and gender to managers ratings of promotion potential. J. Organ. Behav. 16(4):391–400.

Langer N, Slaughter SA, Mukhopadhyay T (2014) Project managers practical intelligence and project performance in software offshore outsourcing: A field study. Inform. Systems Res. 25(2): 364–384.

Lazear EP (1992) The job as a concept. Bruns WJ, ed. Performance Measurement, Evaluation, and Incentives (Harvard Business School Press, Boston, MA), 183–215.

Lazear EP, Rosen S (1981) Rank-order tournaments as optimum labor contracts. J. Political Econom. 89(5):841–864.

Leibbrandt A, List JA (2015) Do women avoid salary negotiations? Evidence from a large-scale natural field experiment. Management Sci. 61(9):2016–2024.

Lerner JS, Tetlock PE (1999) Accounting for the effects of accountability. Psych. Bull. 125(2):255–275.

Lewis GB (1986) Gender and promotions: Promotion chances of white men and women in federal white-collar employment. J. Human. Resources 21(3):406–419.

Luftman J, Kempaiah R, Rigoni EH (2009) Key issues for IT executives 2008. MIS Quart. Executive 8(3):151–159.

Lyness KS, Heilman ME (2006) When fit is fundamental: Perfor mance evaluations and promotions of upper-level female and male managers. J. Appl. Psych. 91(4):777–785.

MacCrory F, Choudhary V, Pinsonneault A (2014) Designing promotion tournaments to mitigate turnover of IT professionals. Working paper, University of California, Irvine.

MacMilan D (2012) The rise of the “brogrammer.” Businessweek (March. 1). http://www.businessweek.com/articles/2012-03 -01/the-rise-of-the-brogrammer.

McGregor J (2014) 2% of Google employees are black and just 30% are women. Forbes (May 29), http://www.forbes.com/sites/ jaymcgregor/2014/05/29/2-of-google-employees-are-black-and -just-30-are-women/.

Melero E (2010) Training and promotion: Allocation of skills or incentives? Industrial Relations (Berkeley) 49(4):640–667.

Meyer JW, Rowan B (1977) Institutionalized organizations: Formal structure as myth and ceremony. Amer. J. Sociol. 83(2):340–363.

Milgrom P, Oster S (1987) Job discrimination, market forces, and the invisibility hypothesis. Quart. J. Econom. 102(3):453–476.

Monin B, Miller DT (2001) Moral credentials and the expression of prejudice. J. Personality Soc. Psych. 81(1):33–43.

Morgan AJ, Quesenberry JL, Trauth EM (2004) Exploring the importance of social networks in the IT workforce: Experiences with the “Boy’s Club.” Stohr E, Bullen C, eds. Proc. 10th America Conference on Information Systems (Association of Information Systems, New York), 1313–1320

Mundy L (2017) Why is Silicon Valley so awful to women? The Atlantic (April), https://www.theatlantic.com/magazine/archive 2017/04/why-is-silicon-valley-so-awful-to-women/517788/.

Nieva VF, Gutek BA (1980) Sex effects on evaluation. Acad. Man agement Rev. 5(2):267–276.

Organisation for Economic Co-operation and Development (2012) Closing the gender gap: Act now. Accessed September 8, 2016, http://www.oecd.org/gender/issues/.

Orbell J, Dawes R, Schwartz-Shea P (1994) Trust, social categories, and individuals: The case of gender. Motivation Emotion 18(2): 109–128.

Park SH, Westphal JD (2013) Social discrimination in the corporate elite: How status affects the propensity for minority CEOs to receive blame for low firm performance. Admin. Sci. Quart. 58(4):542–586.

Powell GN, Butterfield DA (1994) Investigating the “glass ceiling” phenomenon: An empirical study of actual promotions to to management. Acad. Management J. 37(1):68–86.

Prendergast C (1993) The role of promotion in inducing specific human capital acquisition. Quart. J. Econom. 108(2):523–534.

Rosen S (1986) Prizes and incentives in elimination tournaments Amer. Econom. Rev. 76(4):701–715.

Rossi PE, Allenby GM, McCulloch R (2005) Bayesian Statistics and Marketing (John Wiley & Sons, New York)

Royce WW (1970) Managing the development of large software systems. Proc. IEEE WESCON (IEEE Computer Society Press, Washington, DC), 1–9.

Sherf EN, Gajendran RS, Venkataramani V (2018) When managers are overworked, they treat employees less fairly. Harvard Business Review (June 4) https://hbr.org/2018/06/research-when -managers-are-overworked-they-treat-employees-less-fairly.

Sheridan JE, Slocum JW, Buda R (1997) Factors influencing the probability of employee promotions: A comparative analysis of human capital, organization screening and gender/race discrimination theories. J. Bus. Psych. 11(3):373–380

Sherman E (2015) Report: Disturbing drop in women in computing field. Fortune (March 26), http://fortune.com/2015/03/26/report -the-number-of-women-entering-computing-took-a-nosedive/.

Slaughter SA, Ang S, Boh WF (2007) Firm-specific human capital and compensation-organizational tenure profiles: An archival anal ysis of salary data for IT professionals. Human Resource Man agement 46(3):373–394.

Spence M (1973) Job market signaling. Quart. J. Econom. 87(3):355–374.

Sprague K (2015) Wanted: More women in technology. Interview, McKinsey Digital. Accessed November 25, 2019, https://www .mckinsey.com/business-functions/mckinsey-digital/our-insights wanted-more-women-in-technology.

Spotlight HBR (2013) Women in the workplace: A research roundup Harvard Bus. Rev. (September):86–91.

Stiglitz JE (1975) The theory of “screening,” education, and the distribution of income. Amer. Econom. Rev. 65(3):283–300.

Swim JK, Aikin KJ, Hall WS, Hunter BA (1995) Sexism and racism: Old-fashioned and modern prejudices. J. Perspect. Soc. Psych. 68(2):199–214.

Trauth E, Joshi K, Kvasny L, Chong J (2010) Millennials and masculinity: A shifting tide of gender typing of ICT? Proc. 16th Amer. Conf. Inform. System Lima (Association of Information Systems, New York), 5022–5031.

Trauth EM, Quesenberry JL, Huang H (2009) Retaining women in the U.S. IT workforce: Theorizing the influence of organizational factors. Eur. J. Inform. System 18(5):476–497.

Trauth EM, Quesenberry JL, Morgan AJ (2004) Understanding the under representation of women in IT: Toward a theory of individual differences. 2004 ACM SIGMIS Conf. Comput. Personnel Res. Careers, Culture Ethics a Networked Environ. (Association of Com puting Machinery, Tuscon, AZ), 114–119.

Trauth EM, Quesenberry JL, Yeo B (2005) The influence of environmental context on women in the IT workforce. Proc. 2005 ACM SIGMIS CPR (Association of Computing Machinery, Atlanta), 24–31.

Uhlmann EL, Cohen GL (2007) “I think it, therefore it’s true”: Effects of self-perceived objectivity on hiring discrimination. Organ. Behav. Human Decision Processes 104(2):207–223.

Unger RK (1976) Male is greater than female: The socialization of status inequality. Counseling Psychologist 6(2):2–9.

U.S. Department of Labor (2015a) Computer and information technology occupations. Report, U.S. Department of Labor, Washington, DC.

U.S. Department of Labor (2015b) Data and statistics: Women in the labor force. Report, U.S. Department of Labor, Washington, DC.

Vara V (2014) Pandora and the white male. New Yorker (August 22), http://www.newyorker.com/tech/elements/pandora-white -male.

Venkatesan R, Mehta K, Bapna R (2007) Do market characteristics impact the relationship between retailer characteristics and online prices? J. Retailing 83(3):309–324

Verniers C, Vala J (2018) Justifying gender discrimination in the work place: The mediating role of motherhood myths. PLoS One 13(1):1–24.

Waldman M (1984) Job assignments, signalling, and efficiency. RAND J. Econom. 15(2):255–267.

Wallston BS, O’Leary VE (1981) Sex makes a difference: Differentia perceptions of women and men. Wheeler L, ed. Review of Personality and Social Psychology (Sage Publications, Newbury Park, CA), 9–41.

Weinberger CJ (2006) A labor economist’s perspective on college educated women in the information technology workforce. Trauth EM, ed. Encyclopedia of Gender and Information Tech nology (IGI Publishing, Hershey, PA).

Woetzel J, Madgavkar A, Ellingrud K, Labaye E, Devillard S, Kutcher E, Manyika J, Dobbs R, Krishnan M (2015) How advancing women’s equality can add \$12 trillion to global growth. Report, McKinsey Global Institute, New York.

Yzerbyt V, Provost V, Corneille O (2005) Not competent but warm . . . really? Compensatory stereotypes in the French-speaking world Group Processes Intergroup Relations 8(3):291–308.
