---
otero_id: 22163
otero_key: "TBGP2GQE"
title: "The impact of software process improvement on quality: in theory and practice"
authors: "Noushin Ashrafi"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(02)00096-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
<sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

# The impact of software process improvement on quality: in theory and practice

Noushin Ashrafi

Department of MSIS College of Management, University of Massachusetts, 100 Morrisey Blvd., Boston, MA 02125, USA Accepted 22 August 2002

## Abstract

To remain competitive, software companies must establish practices that enhance quality and advance process management. To this end, they have increasingly turned to software process improvement (SPI) methodologies, of which the ISO 9000 standards and the capability maturity model (CMM) are the best known. The underlying principle of both methodologies is to assess organizational capabilities to produce quality software, but they depend on different underlying processes.

Whether the practices advocated by these methodologies lead to high-quality software has been the topic of ongoing debates. Both scholars and practitioners are looking for hard evidence to justify the time and effort required by such guidelines to improve the software-development process and its end product.

In this paper, we investigate the impact of SPI methodologies on software quality, first by theoretical comparison and then with empirical data. Our findings reveal that each methodology has had a different level of impact on software quality factors. These findings could help software-development organizations select the methodology or combination that best meets their quality requirement.

Keywords: Software process improvement; Software quality assurance; The capability maturity model; ISO 9000-3; Quality factors

## 1. Introduction

Despite rapid advances in all facets of technology, the software industry is still struggling with the formidable task of developing software applications that meet quality standards, time pressure, and budget constraints [26,29]. Cost and time elements are quantitative, and therefore can be measured and evaluated. Quality on the other hand, is a multi-dimensional concept, difficult to define and measure. The focus of this paper is on the quality aspect of software development.

Software organizations differ in their strategies for improvement of the quality of their products. In the past, looking for a quick solution, some organizations have tried to use special packages or approaches to their software-development processes, hoping to get quality software products out fast and within budget. Since these efforts did not deliver as promised, the slower paced and methodical approaches, such as software process improvement (SPI), started to gain momentum [13].

Two established sources, the ISO 9000-3 standards and the capability maturity model (CMM), have provided guidance for software-development companies. While these SPI techniques may be considered mainstream approaches in the software industry, their deployment is expensive and time consuming. Therefore, organizations are looking for hard evidence to justify the time and effort required to use these guidelines to improve the software-development process and thus hopefully the end product.

The purpose of this paper is to examine SPI methodologies, specifically ISO 9000-3 and the CMM, to find out to what extent they address quality factors, and once implemented, their impact on various quality factors. This line of analysis should be of value in determining which SPI methodology should be adopted to build quality into the software-development process.

## 2. Background

The elusive concept of software quality has been the topic of debate since computers were first invented [19]. Manufacturing quality concepts initiated by Deming [5] and continued by Juran and Gryna [17] such as conformance for requirements and fitness for customer use, have been applied to software products. Pressman [30] and Humphrey [14] showed quality as a multi-dimensional concept perceived differently in different domains. Fournier [9] has indicated that, ‘‘quality very often signifies different things to different people in the context of a software system.’’

To illustrate various aspects of software quality, software professionals pioneered a quality model that attempted to identify factors representing the behavioral characteristics of the software system. Each factor was subsequently associated with at least two or more software quality attributes used to enforce the definition of a specific quality factor [23]. Throughout the years, experts have come up with different versions of the model. While varying in detail, all versions lay a foundation to cover all dimensions of quality for a software product, ensuring that quality is built into the software system package being created [7,10,11,27]. The Software Quality Assurance (SQA) group, which is a professional organization founded to promote the quality assurance profession through proliferation and advancement of high professional standards, embraced this framework as a guideline to judge the quality of a software system. Table 1 shows a version of the software quality model printed in the handbook of SQA. This model identifies 14 quality factors in three stages of the development life cycle: design, performance, and adaptation. Although it is difficult, if not impossible, to develop a piece of software that adheres to all of these 14 factors, the model provides a good frame of reference to understand software quality. We used this quality model throughout the study.

Table 1 Software quality factors

<table><tr><td colspan="2">Software quality factors</td></tr><tr><td colspan="2">Quality of design</td></tr><tr><td>Correctness</td><td>Extent to which the software conforms to its specifications and conforms to its declared objectives</td></tr><tr><td>Maintainability</td><td>Ease of effort for locating and fixing a software failure within a specified time period</td></tr><tr><td>Verifiability</td><td>Ease of effort to verify software features and performance based on its stated objectives</td></tr><tr><td colspan="2">Quality of performance</td></tr><tr><td>Efficiency</td><td>Extent to which the software is able to do more with less system (hardware, operating system, communications, etc.) resources</td></tr><tr><td>Integrity</td><td>Extent to which the software is able to withstand intrusion by unauthorized users or software within a specified time period</td></tr><tr><td>Reliability</td><td>Extent to which the software will perform (according to its stated objectives) within a specified time period</td></tr><tr><td>Usability</td><td>Relative ease of learning and the operation of the software</td></tr><tr><td>Testability</td><td>Ease of testing to program to verify that it performs a specified function</td></tr><tr><td colspan="2">Quality of adaptation</td></tr><tr><td>Expandability</td><td>Relative effort required to expand soft ware capabilities and/or performance by enhancing current functions or by adding new functionality</td></tr><tr><td>Flexibility</td><td>Ease of effort for changing the soft ware&#x27;s mission, functions or data to meet changing needs and requirements</td></tr><tr><td>Portability</td><td>Ease of effort to transport software to another environment and/or platform.</td></tr><tr><td>Reusability</td><td>Ease of effort to use the software (or its components) in another software systems and applications</td></tr><tr><td>Interoperability</td><td>Relative effort needed to couple the software on one platform to another software and/or another platform</td></tr><tr><td>Intra-operability</td><td>Effort required for communications between components in the same software system</td></tr></table>

Source: the Handbook of Software Quality Assurance, Prentice Hall, 1998.

Finding a way to improve software quality for all software-development organizations is not possible; what is considered the ultimate target for quality in one organization may not be important to another; for example, an organization that produces mission critical software, considers reliability to be the most important factor while, portability may be a necessity for organization that produces a software product for a variety of platforms. Obviously, increasing some quality factors may cause others to decline.

What an experienced software developer wants is an approach that reflects his or her organization and its goals. Organizations that find themselves in a process of choosing a methodology to improve their quality management system face a dilemma: which, if any of these methodologies meet their quality requirements [8].

Also, there has been some concern about the lack of hard evidence that SPI methodologies do indeed improve the quality of software products [16,24,28,31].

Recently, a number of empirical studies addressed the effect of the CMM or ISO device on quality. These studies, however, measure software quality as reduced number of defects and less rework, hence offering a narrow definition of quality. CMM specifies 18 key process areas (KPAs) categorized into five process maturity levels. Studies have shown that a higher maturity level leads to increased productivity and quality, defined as reduced defects and rework [12,15,21,22]. A similar study investigated the emerging ISO/IEC 15504 international standard on software process assessment [6]. Their findings indicate that improvements in process capability are associated with reduction in rework.

The Software Engineering Institute’s report recently summarized the observations from a 1999 survey of high maturity CMM-based efforts. It basically provided a perspective on the practices of high maturity level organizations regarding their management, engineering, tools, and technology [4].

Several other studies have been conducted to compare and contrast ISO 9000-3 and CMM. Most have focused on one-on-one comparison of CMM key process areas and ISO 9000-3 requirements [1– 3,20,25,33]. Although very useful in answering questions such as ‘‘Is complying with a certain level of CMM equivalent to complying with ISO standards?,’ they do not assess and compare the impact of the two approaches. In fact, there has apparently been no effort to investigate SPI methodologies on various dimensions of software quality, such as design, performance, and adaptation.

In our attempt to do this, first we need to compare and contrast SPI and SQA approaches to the development process and how they define and embrace quality issues.

## 3. Comparing SPI with the SQA factors

Although both SQA guidelines and SPI methodologies more or less claim to address the same subject B, quality assurance (QA) B, they attempt to do so from different starting points.

SQA treats processes as part of a ‘‘package’’ with factors and attributes that can be simply illustrated in tables and cross-charts. Fournier notes that, ‘‘Quality . . . encompasses the complete system package being created, including its supportive elements, such as system documentation, staff training, and even postinstallation support processes B, in other words, all those items that meet the expectations of our customers . . . in addition to the software product.’

In contrast, SPI sees the development process as the deciding factor in software improvement and tends to take most other (but by no means all) factors from outside the domain of QA. For example, CMM describes the principles and practices intended to help organizations improve the maturity of their software process development through an evolutionary path from ad hoc and chaotic to mature and disciplined [34]. A formal definition given by the Software Engineering Institute (SEI) shows the emphasis on process rather than product: ‘‘the capability maturity model summarizes the key practices of a key process area and can be used to determine whether an organization or project has effectively implemented the key process areas.’’

ISO 9000-3 guidelines emphasize consistency through extensive documentation. It states, ‘‘ . . . this part of ISO 9000 is intended to describe the suggested controls and methods for producing software which meets a purchaser’s requirements. This is done primarily by preventing non-conformity at all stages from development through to maintenance.’’ [18]. Though expectations may have been heightened by

Table 2 Quality of design

the title of ISO 9000-3 ‘‘quality management and quality assurance standards: guidelines for the application of ISO 9001 to the development, supply and maintenance of software,’’ it has a very narrow focus, as spelled out in its Section 1: ‘‘this part of ISO 9000 deals primarily with situations where specific software is developed as part of a contract according to purchaser’s specifications.’’

Both of these definitions lead us to believe that SPI models tend to reflect a developer’s view, while SQA reflects more of a user’s view. This contrast creates a Heisenberg effect: following one or the other of these approaches, you concentrate either on development processes, or the external attributes of the product, but not on both at the same time.

Basically, SPI methodologies provide a generic recipe for improving the software-development process. This would have a better chance of raising product improvement if we could establish a framework within which improvement can be tailored to meet business needs and organizational quality requirements.

Questions such as: ‘‘Do process improvement activities reflect the understanding of the relationship between process characteristics and quality improvement goals?’’ have remained unanswered. To address such concerns and specifically to identify the strengths and weaknesses of SPI methodologies as they relate to quality, we mapped software quality factors to ISO clauses and key processes of CMM.

This mapping provided theoretical evidence that ISO and CMM cover quality factors as described in the handbook of SQA. The next step for this study was to find out whether there is a correlation between theory and practice when deploying SPI methodologies. Hence, we conducted an empirical study, in which we were surveying the users of these methodologies (software developers) and asking for their perception of the impact of SPI methodologies on quality factors.

For our theoretical assessment, we used SQA as the initial basis for our mapping. Quality factors are divided into three categories: design, performance, and adaptation. Table 2 depicts the mapping of quality factors affecting design to ISO standards and CMM key process areas.

Thus, ISO 9000-3 covers all three factors that improve the quality of design whereas CMM falls short of addressing maintainability. It should be noted that ISO uses a more direct language to address correctness and verifiability then CMM.

Next, we examined the coverage of quality factors for performance by ISO 9000-3 clauses and CMM process areas. Table 3 demonstrates the mapping of these quality factors.

All factors for the quality of performance are addressed both by ISO 9000-3 and CMM, but the language used is not as clear as that for quality of design. For example, both methodologies cover efficiency; however, they refer to efficiency of process rather than efficiency of product. This raised the question: Does improving the efficiency of process improve the efficiency of product? Both address usability through training, rather than ease of use of the product. Although the ultimate goal is the same, enhancing the ability to use the product via training focuses on the users, whereas ease of use focuses on the product. Table 4 shows the mapping of the quality factors for adaptation to CMM key process areas and ISO standards.

<table><tr><td>Quality factors</td><td>ISO standards</td><td>CMM key process areas: goals</td></tr><tr><td>Correctness: extent to which the software conforms to its specifications and conforms to its declared objectives</td><td>5.9.2: provisions should be made for verifying the correctness and completeness of copies of the software product delivered</td><td>Product engineering: consistently performs a well-defined engineering process that integrates all the software engineering activities to produce correct, consistent software products effectively and efficiently Not available</td></tr><tr><td>Maintainability: ease of effort for locating and fixing a software failure within a specified time period</td><td>5.6.2: subsequent processes: the product should be designed to the extent practical to facilitate testing, maintenance and use</td><td>Not available</td></tr><tr><td>Verifiability: ease of effort to verify software features and performance based on its stated objectives</td><td>5.4.6: the supplier should draw up a plan for verification of all development phase outputs at the end of each phase</td><td>Project tracking and oversight: establishes a common understanding between the customer and software project of the customer&#x27;s requirements that will be addressed by the software project</td></tr></table>

Table 3 Quality of performance

<table><tr><td>Quality factors</td><td>ISO standards</td><td>CMM key process areas: goals</td></tr><tr><td>Efficiency: extent to which the software is able to do more with less system (hardware, operating system, communications, etc.) resources</td><td>5.4.1: the organization of the project resources, including the team structure, responsibilities, use of sub-contractors and material resources to be used</td><td>Product engineering: consistently performs a well-defined engineering process that integrates all the software engineering activities to produce correct, consistent software products effectively and efficiently</td></tr><tr><td>Integrity: extent to which the software is able to withstand intrusion by unauthorized users or software within a specified time period</td><td>5.3.1: ..., the supplier should have a complete, unambiguous set of functional requirements; in addition, these requirements ... include, but are not limited to, the following: performance, safety, reliability, security, and privacy; these requirements should be stated precisely enough so as to allow validation during product acceptance</td><td>Configuration management: establishes and maintains the integrity of the products of the software project throughout the project&#x27;s software life cycle</td></tr><tr><td>Reliability: extent to which the software will perform (according to its stated objectives) within a specified time period</td><td>5.3.1: ..., the supplier should have a complete, unambiguous set of functional requirements. In addition, these requirements ... include, but are not limited to, the following: performance, safety, reliability, security, and privacy; these requirements should be stated precisely enough so as to allow validation during product acceptance</td><td>Project tracking and oversight: establishes a common understanding between the customer and software project of the customer&#x27;s requirements that will be addressed by the software project</td></tr><tr><td>Usability: relative ease of learning and the operation of the software.</td><td>6.9: the supplier should establish and maintain procedures for identifying the training needs and provide for training of all personnel performing activities affecting quality</td><td>Training program: the purpose of training program key process area is to develop skills and knowledge of individuals so they can perform their roles effectively and efficiently</td></tr><tr><td>Testability: ease of testing to program to verify that it performs a specified function</td><td>5.7: testing may be required at several levels from the individual software item to the complete software product, there are several different approaches to testing and integration</td><td>Peer reviews: the purpose of peer review is to remove defects from the software work products early and efficiently...</td></tr></table>

Comparatively, ISO 9000-3 guidelines provide better coverage. However, the ISO 9000-3 clauses that cover the quality factors for adaptation and performance are not as strong as those for design.

The mapping revealed that the coverage of quality factors by the two SPI methodologies ranges from explicit to implicit or not covered at all. For example, both ISO and CMM cover design factors explicitly, except for maintainability. Both cover all of the performance factors, but the level of coverage is mixed. ISO addresses adaptation implicitly except for portability. CMM does not address adaptation factors except for flexibility, which is covered lightly.

## 4. The empirical study

To find out the consequences of their coverage in practice, and to attempt to assess whether using these methodologies does indeed improve the quality of a piece of software, we embarked upon an empirical study. We targeted developers who have used CMM and ISO and asked them to evaluate the impact of SPI on the quality of the design, performance, and adaptation of their software products. We compared their responses on the basis of the type of SPI methodology they used.

Table 4 Quality of adaptation

<table><tr><td>Quality factors</td><td>ISO standards</td><td>CMM key process areas: goals</td></tr><tr><td>Expandability: relative effort required to expand software capabilities and/or performance by enhancing current functions or by adding new functionality</td><td>5.10.1.c: functional expansion or performance improvement: functional expansion or performance improvement of existing functions may be required by the purchaser in the maintenance stage</td><td>NA</td></tr><tr><td>Flexibility: ease of effort for changing the software&#x27;s mission, functions or data to meet changing needs and requirements</td><td>5.10.7: the supplier and purchaser should agree and document procedures for incorporating changes in a software product resulting from the need to maintain performance</td><td>Project tracking and oversight: establishes a common understanding between the customer and software project of the customer&#x27;s requirements that will be addressed by the software project</td></tr><tr><td>Portability: ease of effort to transport software to another environment and/or platform</td><td>NA</td><td>NA</td></tr><tr><td>Reusability: ease of effort to use the software (or its components) in another software systems and applications</td><td>5.6.2.c: use of past design experience: utilizing lessons learned from past design experiences, the supplier should avoid recurrence of the same or similar problems</td><td>NA</td></tr><tr><td>Interoperability: relative effort needed to couple the software on one platform to another software and/or another platform</td><td>6.1.3.1.c: (procedures should be applied to ensure that) all interfaces to other software items and to hardware (can be identified for each version of the software)</td><td>NA</td></tr><tr><td>Intra-operability: effort required for communications between components in the same software system</td><td>5.7.3.b: any discovered problems and their possible impacts to and other parts of the software should be noted and those responsible notified</td><td>NA</td></tr></table>

We selected four professional organizations in New England and distributed our survey to their members: The SPI Network (SPIN), The Association of Computing Machinery (ACM) Boston Chapter, The American Society for Quality (ASQ) of Massachusetts, and The New England Software Quality Assurance Forum (NESQAF). The method of data gathering was that of semi-structured interviews: the surveys were handed out in person, and questions were answered as they were raised. We approached more than 200 members of these organizations and screened out those who were not part of a SW development team. Our findings and analysis are based on the 67 responses that we collected.

The first part of the questionnaire was designed to identify the users and non-users of SPI methodologies. We separated projects that were developed using an SPI methodology from those that were not. Table 5 depicts this distribution.

In the second part of the survey, we asked questions about the impact of SPI methodologies on quality; for design, this is determined by its correctness, maintainability, and verifiability. To analyze the impact of the SPI methodologies, we asked the respondents to rank their perceived impact from very low ¼ 1, low ¼ 2, average ¼ 3, high ¼ 4, to very high ¼ 5.

Fig. 1 shows histograms indicating the proportion of developers that perceive the impact of the methodology they use on design factors from very low to very high.

Table 5  
Percentage of respondents using a SPI methodology

<table><tr><td></td><td>ISO</td><td>CMM</td><td>ISO &amp; CMM</td><td>Other</td><td>Total</td></tr><tr><td>SPI</td><td>16%</td><td>10%</td><td>12%</td><td>22%</td><td>60%</td></tr><tr><td>Non-SPI</td><td></td><td colspan="2">40%</td><td></td><td>40%</td></tr></table>

![](/api/attachments/TBGP2GQE/fulltext/images/7036c08d005c97475a03911ebbed1a5ca25c09f829a67455ef106ade334ecb89.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/5dfc903c046de5886dd63db7979ab66a92baf6c6dc6e8237d684b73a60f3b8d4.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/3839df3f8bc172c6dbe68a84fc5e0a869d68fcbf17b306af842cfc2f5adb3fb2.jpg)  
Fig. 1. Impact of software process improvement methodology on the quality of design.

Overall, this shows that our respondents perceived the impact of using ISO on design factors much stronger than that of CMM. They reported, however, that when companies adopt both ISO and CMM a higher level of correctness, maintainability, and verifiability is achieved.

Histograms provide a graphical description of our respondents’ perception; however, they do not tell the whole story. For example, while the mode shows the highest frequency for a level of perception, it does not measure variability. Numerical descriptive measures, such as mean and standard deviation provide a measure of central tendency and of variability, respectively hence providing additional insight into comparing the methodologies. Low variability indicates agreement between respondents on the level of impact and manifests predictability, which is an important factor in selecting a methodology. Table 6 shows the average and standard deviation for design factors for each group.

Table 6  
Mean and standard deviations for design quality factors

<table><tr><td></td><td>Correctness</td><td>Maintainability</td><td>Verifiability</td></tr><tr><td rowspan="2">ISO</td><td> $S_{\text{B}} = 3.64$ </td><td> $S_{\text{B}} = 3.27$ </td><td> $S_{\text{B}} = 3.50$ </td></tr><tr><td> $S_{\text{S}} = 1.21$ </td><td> $S_{\text{S}} = 1.19$ </td><td> $S_{\text{S}} = 1.27$ </td></tr><tr><td rowspan="2">CMM</td><td> $S_{\text{B}} = 3.44$ </td><td> $S_{\text{B}} = 3.33$ </td><td> $S_{\text{B}} = 3.00$ </td></tr><tr><td> $S_{\text{S}} = 1.88$ </td><td> $S_{\text{S}} = 2.12$ </td><td> $S_{\text{S}} = 2.12$ </td></tr><tr><td rowspan="2">ISO and CMM</td><td> $S_{\text{B}} = 3.67$ </td><td> $S_{\text{B}} = 3.67$ </td><td> $S_{\text{B}} = 3.33$ </td></tr><tr><td> $S_{\text{S}} = 1.03$ </td><td> $S_{\text{S}} = 1.51$ </td><td> $S_{\text{S}} = 1.21$ </td></tr><tr><td rowspan="2">Other</td><td> $S_{\text{B}} = 3.50$ </td><td> $S_{\text{B}} = 3.18$ </td><td> $S_{\text{B}} = 3.25$ </td></tr><tr><td> $S_{\text{S}} = 0.80$ </td><td> $S_{\text{S}} = 0.98$ </td><td> $S_{\text{S}} = 0.87$ </td></tr></table>

The table suggests that the mean values for four categories are all above average (3) and quite close. Standard deviations provide additional information regarding the consistency of the perception among the users of a methodology. The largest variability was detected among those who use only CMM; whereas those who use other, mostly ‘‘home grown,’’ methodologies were cohesive in their perception of the impact.

Fig. 1 and Table 6 are consistent with our mapping for ISO, whose requirements explicitly address the issues of correctness, maintainability, and verifiability. The empirical study indicates that most of the respondents thought that ISO had a high impact on these factors. The results, however, are somewhat inconsistent for CMM. Although it covers correctness and verifiability and not maintainability, the responses are moderate and close for them. Using both techniques is considered the best. Obviously, deploying both ISO 9000-3 and CMM is costly and time consuming, and only companies who are truly committed to improving the development process would use both. In practice, the developers of mission critical software, where correctness is of crucial importance use both methodologies [32]. In our study, 12% of the respondents reported using both.

Many companies that cannot afford to deploy both techniques should select the methodology that meets their requirements. Our study suggests that using ISO would have a greater impact on the quality of design than using CMM or other methodologies.

The quality of a software product depends upon a good design, and good performance. This is measured by the efficiency, integrity, reliability, testability and usability of a software product. Fig. 2 demonstrates our respondents’ perspectives on the impact of SPI on performance quality factors.

Our data for performance is not as obvious as that for design. Using both ISO and CMM has the greatest impact on reliability and testability, which are two related factors. It seems that other methodologies combined showed the highest impact on efficiency, and that usability can be improved using ISO alone. It is not clear which methodology has the highest impact on integrity. Table 7 depicts mean and standard deviation for each factor and clarifies some of the ambiguity in Fig. 2. While histograms did not indicate which methodology has the highest impact on integrity, Table 7 shows them to be ISO and CMM, thus indicating that the combination is the best.

As we pointed out earlier, performance quality factors are not addressed as strongly as in design,

Table 7  
Mean and standard deviations for performance quality factors

<table><tr><td></td><td>Efficiency</td><td>Integrity</td><td>Reliability</td><td>Usability</td><td>Testability</td></tr><tr><td rowspan="2">ISO</td><td> $S_B = 2.64$ </td><td> $S_B = 2.64$ </td><td> $S_B = 3.64$ </td><td> $S_B = 3.73$ </td><td> $S_B = 3.70$ </td></tr><tr><td> $S_S = 1.12$ </td><td> $S_S = 0.81$ </td><td> $S_S = 1.03$ </td><td> $S_S = 0.90$ </td><td> $S_S = 1.06$ </td></tr><tr><td rowspan="2">CMM</td><td> $S_B = 2.75$ </td><td> $S_B = 2.75$ </td><td> $S_B = 3.67$ </td><td> $S_B = 3.33$ </td><td> $S_B = 3.78$ </td></tr><tr><td> $S_S = 2.05$ </td><td> $S_S = 2.19$ </td><td> $S_S = 2.00$ </td><td> $S_S = 2.00$ </td><td> $S_S = 1.99$ </td></tr><tr><td rowspan="2">ISO and CMM</td><td> $S_B = 2.83$ </td><td> $S_B = 3.17$ </td><td> $S_B = 4.00$ </td><td> $S_B = 2.50$ </td><td> $S_B = 3.67$ </td></tr><tr><td> $S_S = 0.75$ </td><td> $S_S = 0.98$ </td><td> $S_S = 1.10$ </td><td> $S_S = 1.22$ </td><td> $S_S = 1.51$ </td></tr><tr><td rowspan="2">Other</td><td> $S_B = 3.18$ </td><td> $S_B = 3.00$ </td><td> $S_B = 3.58$ </td><td> $S_B = 3.42$ </td><td> $S_B = 3.67$ </td></tr><tr><td> $S_S = 1.17$ </td><td> $S_S = 1.18$ </td><td> $S_S = 1.08$ </td><td> $S_S = 1.31$ </td><td> $S_S = 1.30$ </td></tr></table>

![](/api/attachments/TBGP2GQE/fulltext/images/88b10c8468f5cf1e0171c76161b280f529428779322b8234c934d1bcaa7f9c54.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/38ac617be94dec0a0c4bdf44c7d0f7cf437f4b8439c31465fa3d236aaea5cf67.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/9379a9e4badffa81d0098c8007f2dcf50c9da335735fb2375a3979e64341286a.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/ef09b9c5d35c6ed982ab7c1585e52729a724612e15c2c5edd188e98f1a69699b.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/1ec86bfb4231a13691583690c025995d2ae639b73968e2f3030e3aeb198354ae.jpg)  
Fig. 2. Impact of software process improvement methodology on the quality of performance.

![](/api/attachments/TBGP2GQE/fulltext/images/34451c24585c40daf73451aaff3ac79ce00ffdfeec34f1d6af53e8f7a7e628fb.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/6292192a2cc4227bc0e02527230c1aeb5e4d3bae3dbd610b7f0a80eaba120e95.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/38d6ba17459f982d4b23725c3203d0b569280bc96c0a599f8be7ee626bbfa104.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/dbaf1cfb90415f9c1bcb796ab007e56c5662cd6744ff4750363b2bfefb1f6630.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/11bdd2a471c242c1b924b131857d843464b83cc6d5acd8905aea7e6423942a0e.jpg)

![](/api/attachments/TBGP2GQE/fulltext/images/f44c995a7e5007829729b1fcf9cb45bd5eba66e3a8582108d3265314b134941b.jpg)  
Fig. 3. Impact of software process improvement methodology on the quality of adaptation.

except for reliability and testing. Table 7 shows mean values mostly below average (3) for efficiency and integrity, above average for reliability and testability, and a mixed for usability. In Table 3 the language used by ISO for addressing efficiency is not very strong, and Fig. 2 indicates the percentage of respondents that perceived its impact as high or very high are 27 and 0%, respectively. Also, apparently CMM covers efficiency only lightly, and its histogram shows that respondents are not impressed by its impact on efficiency. The histograms in Fig. 3 depict the reported impact on the factors of the quality of adaptation; it was quite uneven.

Table 8  
Mean and standard deviations for adaptation quality factors

<table><tr><td></td><td>Expandability</td><td>Flexibility</td><td>Portability</td><td>Reusability</td><td>Interoperability</td><td>Intra-operability</td></tr><tr><td rowspan="2">ISO</td><td> $S_B = 3.60$ </td><td> $S_B = 3.50$ </td><td> $S_B = 3.10$ </td><td> $S_B = 3.50$ </td><td> $S_B = 3.20$ </td><td> $S_B = 4.10$ </td></tr><tr><td> $S_S = 0.97$ </td><td> $S_S = 1.08$ </td><td> $S_S = 1.60$ </td><td> $S_S = 1.08$ </td><td> $S_S = 1.23$ </td><td> $S_S = 0.99$ </td></tr><tr><td rowspan="2">CMM</td><td> $S_B = 4.00$ </td><td> $S_B = 3.00$ </td><td> $S_B = 3.13$ </td><td> $S_B = 3.13$ </td><td> $S_B = 3.00$ </td><td> $S_B = 3.33$ </td></tr><tr><td> $S_S = 1.87$ </td><td> $S_S = 1.93$ </td><td> $S_S = 2.03$ </td><td> $S_S = 2.10$ </td><td> $S_S = 1.77$ </td><td> $S_S = 2.18$ </td></tr><tr><td rowspan="2">ISO and CMM</td><td> $S_B = 3.80$ </td><td> $S_B = 3.40$ </td><td> $S_B = 3.60$ </td><td> $S_B = 2.80$ </td><td> $S_B = 3.40$ </td><td> $S_B = 3.40$ </td></tr><tr><td> $S_S = 1.10$ </td><td> $S_S = 1.14$ </td><td> $S_S = 1.34$ </td><td> $S_S = 0.84$ </td><td> $S_S = 0.89$ </td><td> $S_S = 1.14$ </td></tr><tr><td rowspan="2">Others</td><td> $S_B = 2.80$ </td><td> $S_B = 3.40$ </td><td> $S_B = 2.80$ </td><td> $S_B = 3.20$ </td><td> $S_B = 3.30$ </td><td> $S_B = 3.55$ </td></tr><tr><td> $S_S = 1.14$ </td><td> $S_S = 1.17$ </td><td> $S_S = 1.55$ </td><td> $S_S = 1.40$ </td><td> $S_S = 1.25$ </td><td> $S_S = 1.29$ </td></tr></table>

![](/api/attachments/TBGP2GQE/fulltext/images/25dc4710b8f898dc7bb33135ee5d3af68aff59326ddc6977911c8fc863a71b48.jpg)  
Fig. 4. Decision tree for selecting SPI methodology.

Altogether, the histograms do not provide a clearcut distinction between methodologies in their impact on adaptation factors. Table 8 shows means and standard deviations for these factors.

Table 8 indicates that using ISO, CMM, or both has greater impact on most adaptation factors. This contradicts our mapping results that showed that CMM does not cover expandability, portability, reusability, interoperability, and intra-operability, and covers flexibility lightly. According to the respondents, ISO ranks high in its impact on all adaptation factors, even though it does not cover portability at all and its coverage for the rest is quite light and not direct.

## 4.1. The results

Our empirical data basically supports the theoretical framework and indicates that process improvement enhances software quality factors; however, the levels of impact on various quality factors differ depending on which methodology is used. To put our entire findings in perspective, we created a decision tree that organizations could use as a guideline for the selection of an SPI methodology that meets their quality requirements. Fig. 4 shows this decision tree.

Real-time software products, where performance is a critical factor, include reservation and trading software applications. Organizations involved in developing this type of software product should use ISO, if their primary concerns are usability; use ISO and CMM, if integrity, reliability, and testability are the most important quality factors for them, and use other methodologies if efficiency is the primary concern.

The impact on adaptation quality factors is the most difficult to analyze. Histograms did not provide a clear-cut selection for those organizations with adaptation factors as quality requirements. However, while the empirical findings, more or less, supported the results of theoretical investigation for design and performance factors, the results for adaptation factors mostly contradicted the findings of our mapping.

The intrinsic characteristics of CMM and ISO 9000 could explain their shortcomings here. Both methodologies primarily deal with the status quo and try to improve the existing development process rather than engaging in innovation that ultimately requires adaptation quality factors. Their guidelines reflect their philosophy. Hence, one would believe that for organizations involved with developing software products that need to adapt to constant change, home grown’’ SPI methodologies are the best strategy. However, our empirical findings did not support this idea.

The majority of our respondents ranked the impact of using ISO and CMM together first for those quality factors that address technical aspects of software development (correctness, maintainability, verifiability, reliability, and testability). On the other hand, improving managerial aspects (efficiency, usability, flexibility, reusability, and intra-operability) did not require using both ISO and CMM. This seems counterintuitive, because ISO and CMM both address managerial issues extensively.

The CMM users consistently showed a wide discrepancy in their perceptions of CMMs impact on design, performance, and adaptation factors. One possible reason is that the respondents belonged to firms at different levels of CMM maturity.

## 5. Conclusions and limitations

The key to survive is to develop and market quality products, on time, and within budget. In this study we examined SPI methodologies as they relate to quality guidelines. We cross-referenced factors to ISO 9000-3 clauses and key process areas of the CMM to learn whether SPI methodologies deal with SQA guidelines as part of their process improvement strategy. We conducted an empirical study to find the extent of the impact of SPI methodologies on quality factors in practice. Based on our findings, we built a decision tree, which could be used as an instrument for methodology selection.

Our study produced some inconclusive results, including, for example, the inconsistency between the theoretical framework and the empirical results for adaptation factors, wide variability among CMM users, and the possible biases inherent in the perception of technical people for managerial issues. This research has two limitations:

1. Statistical analysis is descriptive rather than inferential. We chose descriptive statistics because it does not require a scientific sampling procedure. Although our sample size is large enough for inferential statistics, our primary concern was the integrity and accuracy of our responses; therefore, rather than random sampling, we concentrated on developers, with whom we could meet face-toface and know that we could gauge their opinions and their perceptions of SPI methodologies.

2. The ISO 9000-3 clauses and the CMM key process areas are intentionally vague to allow organizations to interpret them according to their own quality system. Our interpretation of their strengths and weaknesses as they relate to quality factors is also subjective and may differ from that of other.

## References

[1] S.R. Bailey, A.J. Donnell, R.M. Hough, Process Control (ISO 9000) and Process Improvement (APEX) in the Transmission Systems Business Unit, AT & T Technical Journal (1994) 17–25.

[2] R.C. Bamford, W.J. Deibler, When the CMM meets ISO 9001, cross-talk, The Journal of Defense Software Engineering (1998) 3–8.

[3] R.C. Bamford, W.J. Deibler, Comparing and contrasting ISO 9001 and the SEI capability maturity models, IEEE Computers 26 (10), 1993, pp. 68–70.

[4] CMM-CMU/SEI-93-TR-25, Key Practices of the Capability Maturity Model, Version 1.1, Carnegie Mellon University, Pittsburg, 1993, pp. 0–11.

[5] W.E. Deming, Quality, Productivity, and Competitive Position, MIT Center for Advanced Engineering Study, Cambridge, MA, 1982.

[6] K.E. Emam, A. Birk, Validating the ISO/IEC 15504 measure of software requirements analysis process capability, IEEE Transactions on Software Engineering 26 (6), 2000, pp. 541–566.

[7] M.W. Evans, J. Marciniak, Software Quality Assurance and Management, Wiley, New York, NY, 1987.

[8] B. Fazlollahi, M.R. Tanniru, Selecting a requirement determination methodology-contingency approach revisited, Information and Management 21, 1991, pp. 291–303.

[9] R. Fournier, Practical Guide to Structured System Development and Maintenance, Prentice-Hall, Englewood Cliffs, NJ, 1991, Chapter 13, pp. 316–322.

[10] D. Garvin, What Does ‘‘Product Quality’’ Really Means?, Sloan Management Review, 1998, pp. 25–45.

[11] T. Gilb, Principals of Software Engineering Management, Addison-Wesley, Reading, MA, 1987.

[12] D.H. Harter, M.S. Krishan, S.A. Slaughter, Effects of maturity on quality, cycle time, and effort in software product develop ment, Management Science 46 (4), 2000, pp. 451–466.

[13] J. Herbsleb, D. Zubrow, D. Goldenson, W. Hayes, M. Paulk, Software quality and the capability maturity model, Communications of ACM 40 (6), 1997, pp. 30–40.

[14] W.S. Humphrey, Managing the Software Process, Addison Wesley, Reading, MA, 1989.

[15] J. Ingalbe, D. Shoemaker, V. Jovanovic, A MetaModel for Capability Maturity Model for Software, in: Proceedings of the AIS, August 2001.

[16] C. Jones, The economics of software process improvement, IEEE Computer 29 (1), 1996, pp. 95–97.

[17] J.M. Juran, F.M. Gryna, Quality Planning and Analysis, McGraw-Hill, New York, 1993.

[18] R. Kehoe, A. Jarvis, ISO 9000-3: A Tool for Software Product and Process Improvement, New York, 1996.

[19] B. Kitchenham, S.L. Pfleeger, Software quality: the elusive target, IEEE Software 13 (1), 1996, pp. 12–21.

[20] D.H. Kitson, Relating the spice framework and SEI approach to software process assessment, Software Quality Journal 5 (3), 1996, pp. 145–156.

[21] M.S. Krishan, C.H. Kriebel, S. Keker, T. Mukhopadhyay, An empirical analysis of productivity and quality in software product, Management Science 46 (6), 2000, pp. 754–759.

[22] M.S. Krishan, M.I. Keller, Measuring process consistency: implications for reducing software defects, IEEE Transactions on Software Engineering 25 (6), 1999, pp. 800–815.

[23] J.A. McCall, et al. Factors in Software Quality, RADC-TR-77-369, 13441-5700, Rome Air Development Center, Griffiss Air Force Bas, NY, November 1977, pp. 1–3.

[24] L. Osterweil et al., Strategic directions in software quality, ACM Computing Surveys 28 (4), 1996, pp. 738–750.

[25] M. Paulk, How ISO 9001 compares with the CMM, IEEE Software 12 (1), 1995, pp. 74–83.

[26] M.J. Pearson, C.S. McCahon, R.T. Hightower, Total quality management: are information systems managers ready? Information and Management 29, 1995, pp. 251–263.

[27] W.E. Perry, Quality Assurance for Information Systems: Methods, Tools, and Techniques, QED Technical Publishing Company, Wellesley, MA, 1991.

[28] S.L. Pfleeger, Does organizational maturity improve quality? IEEE Software 13 (5), 1996, pp. 109–110.

[29] D.D. Phan, J.F. George, D.R. Vogel, Managing software quality in a very large development project, Information and Management 29, 1995, pp. 277–283.

[30] R.S. Pressman, Software Engineering: A Beginner’s Guide, McGraw Hill, New York, 1988.

[31] R.S. Pressman, Software process perceptions, IEEE Software 13 (16), 1996, pp. 16–18.

[32] H. Saiedian, L. McClanahan, Frameworks for quality software process: SEI capability maturity model versus ISO 9000, Software Quality Journal 5, 1996, pp. 1–23.

[33] S.A. Sheard, The frameworks quagmire, cross-talk, The Journal of Defense Software Engineering (1997) 1–8.

[34] G.J. Van der Pijla, G.J.P. Swinkelsb, J.G. Verrijdtc, ISO 9000 versus CMM: standardization and certification of IS development, Information and Management 32 (6), 1977, pp. 267–274.

![](/api/attachments/TBGP2GQE/fulltext/images/01c4e5ce2d8486ab3c95247401f2d7b6a17c278c9bf9bc00284ea47bf870d1dc.jpg)

Noushin Ashrafi is an associate professor in the Management Science and Information Systems Department, College of Management at the University of Massachusetts Boston. Dr. Ashrafi received her PhD in management and information systems from the University of Texas at Arlington. Her extensive publications on software reliability, software process improvement, technology and society, and application of mathematical models to assess fault tolerance software have appeared in journals such as IEEE Transactions on Software Engineering, IEEE Transactions on Software Reliability, IEEE Computer Society, Information and Management, The Journal of Information Technology Management, Information and Software Technology, Information System Management, Computer and Society, and Journal of Database Management. Dr. Ashrafi has made numerous presentations on various topics of information systems in national and international conferences.
