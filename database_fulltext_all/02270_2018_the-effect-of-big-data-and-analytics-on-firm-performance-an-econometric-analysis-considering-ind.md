---
otero_id: 2270
otero_key: "STUD438V"
title: "The Effect of Big Data and Analytics on Firm Performance: An Econometric Analysis Considering Industry Characteristics"
authors: "Oliver Müller; Maria Fay; Jan vom Brocke"
year: "2018"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2018.1451955"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Effect of Big Data and Analytics on Firm Performance: An Econometric Analysis Considering Industry Characteristics

Oliver Müller, Maria Fay & Jan vom Brocke

To cite this article: Oliver Müller, Maria Fay & Jan vom Brocke (2018) The Effect of Big Data and Analytics on Firm Performance: An Econometric Analysis Considering Industry Characteristics, Journal of Management Information Systems, 35:2, 488-509, DOI: 10.1080/07421222.2018.1451955

To link to this article: https://doi.org/10.1080/07421222.2018.1451955

![](/api/attachments/STUD438V/fulltext/images/39e4d5329dd8a42f92130b6facfde08c5db5933197207e204643c57f23d90130.jpg)

Published online: 15 May 2018.

![](/api/attachments/STUD438V/fulltext/images/b10d0891fdbaaa1e6a22a37605b89999de7d82c82a4d8ab76f96747900606877.jpg)

Submit your article to this journal

![](/api/attachments/STUD438V/fulltext/images/c1f52eeffab276513e9eaff39079ad3dba88282febca4c2a35c154ea6481acdf.jpg)

View related articles

![](/api/attachments/STUD438V/fulltext/images/f14e83e19d5db86203ef50f2a8aba0069e57da2b07633ed80ae34c9d173ceddd.jpg)

View Crossmark data

# The Effect of Big Data and Analytics on Firm Performance: An Econometric Analysis Considering Industry Characteristics

OLIVER MÜLLER, MARIA FAY, AND JAN VOM BROCKE

OLIVER MÜLLER (olmy@itu.dk; corresponding author) is an associate professor in the Business Information Technology Department at the IT University of Copenhagen. He holds a Ph.D. from the University of Münster’s School of Business and Economics. He studies how organizations create value with (big) data and analytics. His work has been published in the Journal of the Association of Information Systems, European Journal of Information Systems, MIS Quarterly Executive, European Journal of Operational Research, and other journals.

MARIA FAY (maria.fay@uni.li) is a Ph.D. candidate in business economics (information and process management) at the University of Liechtenstein. She holds an MSc in business informatics and is working on her dissertation investigating the relationship between advanced analytics and business value. She has experience in information technology strategy and technology innovation consulting, and her current research interests include effects of technology adoption on firm performance and decision making.

JAN VOM BROCKE (jan.vom.brocke@uni.li) is Professor of Information Systems, the Hilti Chair of Business Process Management, Director of the Institute of Information Systems, and Vice President Research and Innovation at the University of Liechtenstein. His research focusses on business process management and related aspects of digital innovation and transformation. He has published, among others, in MIS Quarterly (MISQ), Journal of Management Information Systems (JMIS), Journal of Information Technology (JIT), European Journal of Information Systems (EJIS), Information Systems Journal (ISJ), Communications of the ACM (CACM), and MIT Sloan Management Review (MIT SRM). He has held various editorial roles and leadership positions in Information Systems research and education.

ABSTRACT: The emergence of big data has stimulated enormous investments into business analytics solutions, but large-scale and reliable empirical evidence about the business value of big data and analytics (BDA) remains scarce. This article presents the results of an econometric study that analyzes the direction, sign, and magnitude of the relationship between BDA and firm performance based on objective measurements of BDA assets. Using a unique panel data set that contains detailed information about BDA solutions owned by 814 companies during the time frame from 2008 to 2014, on the one hand, and their financial performance, on the other hand, we estimate the relationship between BDA assets and firm productivity and find that live BDA assets are associated with an average of 3–7 percent improvement in firm productivity. Yet we also find substantial differences in returns from BDA when we consider the industry in which a firm operates. While firms in information technology-intensive or highly competitive industries are clearly able to extract value from BDA assets, we did not detect measurable productivity improvement for firms outside these industry groups. Taken together, our findings provide robust empirical evidence for the business value of BDA, but also highlight important boundary conditions.

KEY WORDS AND PHRASES: big data analytics, econometric analysis, firm performance, IT business value, productivity.

Unprecedented growth in data volume, variety, and velocity has emerged over the course of the past decade, a phenomenon often referred to as “big data.” While for most organizations data have traditionally been time-consuming and costly to acquire, today many businesses are confronted with a data deluge. The following quote by Eric Schmidt, former chief executive officer of Google, illustrates the extent of the recent data explosion: “There was five [E]xabytes of information created between the dawn of civilization through 2003, but that much information is now created every two days, and the pace is increasing” [21, p. 1].

The emergence of big data has increased organizations’ demand for business analytics, defined as the “extensive use of data, statistical and quantitative analysis, explanatory and predictive models, and fact-based management to drive decisions and actions” [18, p. 7]. A survey fielded by the Wall Street Journal [68] in collaboration with Oracle found that 86 percent of surveyed executives consider the ability to gain insights from data to be one of their top three business priorities. Similarly, according to studies by Gartner [26] and IBM [33], business intelligence and analytics are today’s top priority for chief information officers (CIOs) and the top technology priority for chief financial officers (CFOs). IDC [34] predicted that the worldwide market for big data and business analytics solutions will increase by more than 50 percent between 2015 and 2019, from \$122 billion to more than \$187 billion. And according to Gartner [25], more than half of the world’s largest organizations will be applying advanced analytics solutions to large data sets by 2018.

At the same time, the adoption of analytics solutions for extracting value from big data —in the following called big data and analytics (BDA)—is associated with substantial financial investments for firms. For example, the three-year total cost of ownership for an IBM PureData System for Analytics,<sup>1</sup> an appliance for big data processing, is estimated to be \$39 million, and the overall costs for a comparable Cloudera Hadoop cluster,<sup>2</sup> for the same period sum up to more than \$50 million [13].

These figures lead to the question of whether investments in BDA pay off for companies, that is, whether they actually generate business value. The need to conduct “critical, intensive assessments of the actual impact of big data investment and use and understand if and how one can attain instrumental benefits (such as performance and profitability)” has recently also been raised in the information systems (IS) literature by Abbasi et al. [1, p. xi]. While the business and information technology (IT) press is picturing companies that transformed their businesses or even entire industries through the use of BDA, scientific evidence for the business value of BDA is scarce. Existing empirical evidence has come either from qualitative case studies that discuss the opportunities and challenges of BDA [58, 64] or from surveys that are based on self-reported perceptual measures of business value [5, 17, 44, 54,], while large-scale studies that have drawn on objective measures of firm performance, such as productivity, are rare (Brynjolfsson et al. [12] and Tambe [62] are exceptions). These observations indicate a gap in the academic literature that a recent report of the Organization for Economic Cooperation and Development (OECD) [47, p. 18] has also pointed out: “While [case] evidence . . . strongly suggests a positive link between [data-driven innovation] and productivity growth across the economy, few empirical studies exist with robust quantitative estimates.”

Our study addresses this research gap by using econometric methods to investigate the relationship between live BDA assets and firm performance. We compiled a unique panel data set that contains detailed information about BDA solutions owned by 814 companies over a period of seven years from 2008 to 2014. By combining this information with financial performance data from the Compustat database, we can estimate the direction, sign, and magnitude of the relationship between BDA assets and firm performance.

We find that over all industries, ownership of live BDA assets is associated with an average increase in productivity by about 4.1 percent, but we can only speculate about the direction of the causality of this relationship. When we take industry characteristics into consideration, the causality becomes clearer and we find that live BDA assets are associated with substantial improvements in a firm’s productivity— 6.7 percent productivity gains in IT-intensive industries and 5.7 percent in competitive industries. Taken together, our results provide robust empirical evidence for the business value of BDA, but also highlight important boundary conditions.

## Background

## Business Value of Big Data and Analytics

To understand the current discourse on BDA business value, it is useful to recall how this class of IT is different from other enterprise IT. As early as 1971, Gorry and Scott Morton [27], in their seminal article “A Framework for Management Information Systems,” used the distinction between operational, managerial, and strategic management activities, on the one hand, and structured (or programmed) and unstructured (or nonprogrammed) problems, on the other hand, to distinguish different categories of information systems. They coined the term “decision support systems” (DSS) to refer to a class of information systems meant to support humans in making management and strategic decisions in unstructured problem situations (e.g., sales and production planning) and distinguish these systems from the information systems for supporting structured operational tasks (e.g., order entry, accounts management) prevailing at that time. In today’s enterprise IT architectures, this distinction is still reflected in the separation of transactional systems, for example, enterprise resource planning (ERP), customer relationship management (CRM), or supply chain management (SCM), from analytical systems, such as, data warehouses, data mining solutions, or dashboards.

Zuboff’s [69] “automate/informate” framework explains how transactional and analytical IT differently affects firm performance. The framework distinguishes between IT that is meant to automate operations by increasing the continuity and control of work processes from IT that is meant to inform decision makers by creating information that improves the comprehensibility of an organization’s work processes. While Zuboff compared the first type of systems with Ford’s automated assembly line, which was meant to replace human labor with machines, she argued that the second type of systems can “create a different and potentially more penetrating, comprehensive, and insightful grasp of the business [that,] in turn, can serve as the catalyst for significant improvement and innovation in the production and delivery of goods and services, thus strengthening the competitive position of the firm” [69, p. 9]. According to this view, transactional systems (e.g., ERP) mainly aim at improving the efficiency of existing business processes, while analytical systems (e.g., BDA) enable managers to explore new process, product, and service innovations.

Since the inception of the first DSS in the 1960s, analytical information systems have undergone a number of evolutionary waves, from batch processing of structured numerical data stemming from company-internal sources and using technologies like relational databases, Structured Query Language (SQL), and report generators to real-time processing of unstructured data originating from social media or sensor networks and using technologies like distributed NoSQL databases, in-memory computing, machine learning, and interactive visualization tools [1, 15]. But not only the data types and technologies have changed, but also the information value chain, that is, how these technologies are leveraged by managers to extract knowledge from data and support decision making [1]. While the business intelligence (BI) applications from the 1990s focused on providing management with a consistent set of metrics to measure past and current business performance, today’s BDA applications enable analytics-savvy managers and data scientists to explore, discover, and predict [1, 18]. Hence, similar to the way communication and collaboration technologies have transformed early DSS, the latest developments around big data and analytics “give rise to a new class of big data IT artifacts” [1, p. viii].

There is first quantitative evidence suggesting that BDA leads to measurable improvements in firm performance. The existing quantitative studies can be roughly divided into market research surveys and academic studies applying econometric methods.

Most studies in the first category have been published in the business press or stem from industry-sponsored research. For example, Davenport and Harris [18] showed a positive correlation between intensity of analytics use and a firm’s annual growth rates, based on a survey of 32 companies. Likewise, a survey among nearly 3,000 executives conducted by IBM [36] found that top-performing organizations use analytics five times as much as lower performers do. Similar results have been reported by major consulting companies like Accenture [2] and Bain & Company [65].

Econometric studies go beyond simple correlational analysis and use research designs that try to control for confounding effects and ensure a causal interpretation of the associations between input and output variables. These methods have been used for many years to investigate the business value of transactional IT systems, such as ERP, CRM, and SCM systems [4, 19, 28, 32, 48].

The first econometric studies investigating the impact of analytical systems on firm performance predate the BDA era and focused on DSS [35] and BI [22]. Although they found a positive impact of these solutions on organizational performance, at the same time they highlighted the importance of considering contextual moderators, such as industry sectors, in the analysis [22].

Another prominent econometric study in the field comes from Brynjolfsson et al. [12], who investigated the relationship between decision making based on data and business analytics—that is, data-driven decision making (DDD)—and firm performance. The authors surveyed 179 large firms concerning their business practices, such as the use of data for business decision making or for creating new products and services, and combined this data with financial data from the Compustat database. Using several econometric models of firm productivity, profitability, and market value, they showed that “firms that adopt DDD have output and productivity that is 5–6% higher than what would be expected given their other investments and information technology usage” [12, p. 1].

Finally, the econometric study conducted by Tambe [62] investigated the relationship between the distribution of big data skills and firm performance. In particular, Tambe used the LinkedIn skills database to measure firms’ investments in big data skills (especially Hadoop) and test whether these investments were associated with higher firm productivity. The results indicated that “firms Hadoop investments were associated with 3% faster productivity growth, but only for firms a) with significant existing data assets and b) in labor networks characterized by significant aggregate Hadoop investment” [62, p. 1452].

In sum, there are well-grounded conceptual arguments and a small but emerging body of empirical evidence for the business value of BDA. Yet, existing empirical studies either predate the big data era (i.e., they focus on the business value of DSS or BI) or rely on self-reported surveys or proxy variables (e.g., BDA skills reported on social networks) to quantify the business value of BDA. To the best of our knowledge, our study is the first econometric study that uses primary data to operationalize BDA through actual live BDA assets, which allows us to obtain more objective estimations of BDA business value. The next section addresses the methodological challenges of quantifying this business value.

## Measuring the Impact of IT on Firm Performance

The impact of IT and IT investments (input or independent variable) on firm performance (output or dependent variable) has been widely studied using a variety of methodological approaches. Sabherwal and Jeyaraj’s [51] meta-analysis identified 303 empirical studies published from 1990 to 2013, and Schryen [55] identified 327 research papers related to the business value of IT. However, only a handful of these studies investigated the impact of BDA systems or its predecessors (i.e., BI, DSS) [20, 22, 35]. In the following section, we will thus focus on the wider range of studies on IT business value in order to identify the most suitable approach for our objectives and research design.

On the input side, early studies operationalized the independent variable of a firm’s IT investments with highly aggregated measures, such as IT expenditures (for hardware, software, personnel, etc.), technical IT assets (e.g., number of PCs and servers), or human IT assets (e.g., number of IT employees). Only recently have studies started to look at more disaggregated measures and at specific IT assets [55]. ERP systems have been the most frequently studied specific IT asset, and Mangin et al.’s [43] literature review covering 54 articles published from 1999 to 2014 found that most studies reported a positive post-implementation impact of ERP systems on firm performance, especially among large companies over a long period of time. In addition to the stream of research that has focused on ERP systems, positive performance impacts have been found for CRM systems [4, 27], SCM systems [4, 19], and knowledge management (KM) systems [23].

On the output side, the most commonly used measure for firm performance has been multifactor productivity [51, 55]. Typically, researchers have related a measure of firm output (e.g., sales or value-added) to a firm’s input factors, such as capital, labor, and materials. The most commonly used functional form for this relationship in the literature has been the Cobb–Douglas production function, which, in addition to the classical production factors capital, labor, and materials, can include other input factors, such as IT assets, and whose resulting coefficients can be interpreted as the marginal effects of these input factors on firm productivity. While early studies that used this approach to estimate the effect of IT on firm productivity did not yield positive effects (which led to the creation of the term “IT productivity paradox”), more recent literature has reported primarily positive productivity effects of IT [10, 11, 41, 55, 57].

## Hypotheses

Sharma et al. [56] conceptualized the process and conditions under which big data and analytics (BDA) can create business value. The authors proposed that BDA’s first-order effects are on decision-making processes and that better decision making can, in turn, lead to improvements in organizational performance, which is in line with the literature on decision support systems’ effect on organizational processes (e.g., [35, 46, 56]).

Mithas et al. [46] offered a complementary conceptualization of the path between a firm’s information management capability and organizational performance, proposing that information management capabilities support the development of three important organizational capabilities that can lead to superior organizational performance: customer management, process management, and performance management.

In their study of the effect of data-driven decision making (DDD) on firm performance, Brynjolfsson et al. [12], drawing on information theory and the information-processing view of the firm, offered additional theoretical views on the topic. According to information theory, information that is more fine-grained, less noisy, better distributed, and available in greater volumes should see more use by managers in decision-making processes, which should improve decision quality [8]. Their second argument stems from the information-processing view of the firm, which posits that the greater a task’s uncertainty, the more information has to be processed between decision makers in order to achieve a given level of performance [24]. One strategy to address this trade-off is to increase the organization’s information-processing capacity by investing in vertical information systems that allow managers to plan and replan business operations frequently by efficiently transmitting information from the point of origin to the point of decision [24].

Taken together, the theoretical arguments outlined above suggest that technologies that improve the collection of data and its efficient distribution in an organization, such as BDA, should increase the use of this data in decision-making processes, which, in turn, should improve decision quality and ultimately drive organizational productivity [12]. This leads us to our first hypothesis:

## Hypothesis 1: BDA assets have a positive impact on firm productivity.

Industry-level factors are important context variables that moderate the impact of IT on firm productivity, and among them is an industry’s IT intensity—sometimes called information or data intensity—which has been found to play an essential role [31, 53].

This argument can be theoretically grounded in the literature on complementary assets [63]. Teece [63] argued that in order to profit from a technological innovation, in almost all cases, a firm needs to use the innovation in combination with other existing capabilities or assets. For example, a BDA solution for building predictive models or visualizing large data sets requires other IT assets, such as transactional ERP or CRM systems, that can act as data sources. These complementary IT assets are generic in the sense that they do not need to be tailored to the BDA solution, and vice versa (assuming that standard interfaces exist to exchange data between the systems). Complementary assets are also exemplified by data scientists who possess the knowledge and skills to use BDA tools to extract patterns and trends from large amounts of data. These human assets are more specialized, because they require training and experience to effectively use the methods and tools in question and develop technological and informational task complementarities in order to apply them productively [40]. Especially this need for investments in human resources seems to be crucial in the field of BDA. The importance of skilled data scientists has, for example, been highlighted in a recent study by McKinsey Global Institute [44], which found a 50–60 percent talent gap between the demand for deep analytical talent and its supply by 2018. Similarly, a study by PricewaterhouseCoopers in cooperation with the Business-Higher Education Forum and Gallup [49] found that 69 percent of employers say that by 2021 they will prefer job candidates with data science and analytics over ones without, but that only 23 percent of educators say that their graduates will have these skills.

Various empirical studies have found that the availability of complementary technological and human IT assets within a firm or its network (e.g., industry or geographic region) is an important moderator of the business value of IT [9] and, more specifically, BDA. For example, Stiroh [59, 60] showed that companies that are IT producers (e.g., electronic equipment, industrial machinery and equipment) or heavy IT users (e.g., wholesale, transportation and utilities, services) enjoyed much larger IT-related productivity gains over the past few decades than other industries (e.g., agriculture, mining, construction) did. Similarly, Lee and Kim’s [38] review of the IT investment literature found that studies with observations from high information-intensive industries (e.g., financial services, insurance, retail, health care) report a more positive impact of IT investments on firm performance than do those from low information-intensive industries (e.g., construction, some manufacturing industries). In a similar line, but specifically focusing on BDA, a recent study by the Centre for Economics and Business Research (CEBR) [14] identified an industry’s data and IT intensity as important moderating factors for the adoption of big data analytics and its potential for increasing firm productivity. Finally, Tambe [62] found in his study on the influence of investments in big data skills on firm productivity that only companies in data-driven industries could extract business value from big data investments and that there was a positive interaction effect between a firm’s investment in big data skills and the pool of big data skills available in the industry in which the firm is operating.

Taken together, the theoretical arguments and empirical evidence outlined above suggest that companies in industries with low availability of complementary IT assets (i.e., low IT-intensity) may experience difficulties in extracting business value from BDA assets. Therefore, we formulate our second hypothesis as follows:

## Hypothesis 2: The effect of BDA assets on firm productivity is higher in ITintensive industries than it is in other industries.

A second important industry-level context factor that moderates the impact of IT on firm performance is the intensity of the competition [55]. Melville et al. [45] drew on two theoretical foundations to explain the role of competitive pressure in extracting business value from IT.

First, Melville et al. [45] state that under competitive pressure firms become more innovative, for example, by utilizing existing IT assets (e.g., BDA) for enabling new business processes (e.g., data-driven decision making), which, in turn, increases their productivity. The first part of this argument is supported by the findings of Basole et al.’s [7] review of 472 articles published between 1977 and 2008 on the adoption of IT innovations by enterprises, in which they found that for more than 30 years competitive pressure has been among the top 3 external characteristics that trigger IT innovations. In the context of BDA, the argument is further supported by Malladi and Krishnan’s [42, p. 9] empirical results, which showed that “higher industry competitive intensity is positively associated with the extent of business intelligence and analytics usage in organizational business activities.” The second part of the argument, follows the same logic and is backed up by the same evidence as H1.

Second, Melville et al. [45] draw on the X-efficiency hypothesis, which states that in the absence of competitive pressure firms tend to build up slack and other inefficiencies while still being able to stay in business [45]. This leads to decreased efficiency of individual production input factors, such as capital, labor, and IT. Several empirical studies have provided evidence for this argument (e.g., [37, 39, 52]). For example, Melville et al. [45] found that the marginal product of IT is significantly lower in highly competitive industries and proposed that “though less competitive industries utilize IT for similar purposes . . . the absence of competitive pressure leads to less efficient use of IT” [45, p. 233].

Taken together, the above arguments suggest that strong competition (a) increases the usage of BDA, which according to H1 drives firm productivity, and (b) leads to more efficient use of BDA. Therefore, we define our third hypothesis as follows:

Hypothesis 3: The effect of BDA assets on firm productivity is higher in highly competitive industries than it is in other industries.

## Methods

## Data

In cooperation with one of the world’s largest enterprise software vendors, we collected a unique longitudinal data set about its customers’ BDA assets. These assets included a broad range of products that can be broadly organized into three categories: (1) foundational database technologies, (2) data mining and machine learning solutions, and (3) data visualization and presentation tools. The first product category comprised, for example, databases and data warehouses running on highperformance in-memory computing appliances, both on-premise and in the cloud, as well as tools for modeling and management of data. In contrast to traditional data warehouses optimized for processing structured numerical data in batch mode, these technologies are also designed to handle unstructured (e.g., from social media) and streaming (e.g., from sensor networks) data. The second product category comprised, for example, advanced analytics solutions including supervised and unsupervised machine learning algorithms for predictive analytics, anomaly detection, text mining, or social network analysis. The third product category comprised mainly solutions for visual intelligence (e.g., dashboards) and mobile or self-service interfaces for users.

We merged these data with financial data from the Compustat Global Fundamentals Annual database for companies that are publicly traded on U.S. stock markets. After joining and cleaning the data sets, we were left with a balanced panel data set containing data on BDA assets as well as financial performance of 814 firms from 2008 to 2014—overall 5,698 firm-year observations. The data set contains information about companies who have adopted BDA during the time frame of our study (i.e., 2008–14), who had already adopted it before 2008, and who—as of 2014—have not adopted BDA at all. This data set opens unique opportunities to study the effect of BDA assets on firm performance, as it contains a large sample of companies and is based entirely on primary objective data comprising both crosssectional and longitudinal observations.

Table 1 shows the definitions of our main variables of interest. The binary IT assets variables have the value 0 in the years preceding a system go-live and the value 1 in the year of go-live and all following years. Besides collecting data about BDA systems, we also collected data about firms’ ERP, CRM, and SCM systems in order to control for firms’ transactional IT assets. To test H2, we adopted a classification of industry sectors’ IT-intensity from Stiroh [59, 60], which is based on the share of IT capital stock in a firm’s total reproducible capital stock. Like Stiroh [59, 60], we considered industries with an above-median IT capital stock share as IT-intensive industries (i.e., wholesale trade, transportation, and public utilities, including telecommunications, services, finance insurance and real estate, and durable manufacturing). To test H3, we classified industries according to their competitiveness using the Herfindahl–Hirschman Index (HHI), which measures the size of firms in relation to the industry in which they operate and therefore indicates the level of competition among them [50]. Following Cetorelli and Strahan [16] and Zwanziger et al. [70], we classify industries with an HHI in the lower twenty-fifth percentile of all industries as highly competitive. (A low HHI indicates a low level of concentration and a high level of competition.)

Table 1. Definition of Variables

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td>Firm</td><td>Unique ID of firm</td></tr><tr><td>Year</td><td>Year of observation</td></tr><tr><td>Industry</td><td>Industry code at the 2-digit Standard Industry Classification (SIC) level</td></tr><tr><td>BDA</td><td>Binary indicator variable: 1 indicates that the firm has BDA assets; otherwise 0</td></tr><tr><td>ERP</td><td>Binary indicator variable: 1 indicates that the firm has ERP assets; otherwise 0</td></tr><tr><td>CRM</td><td>Binary indicator variable: 1 indicates that the firm has CRM assets; otherwise 0</td></tr><tr><td>SCM</td><td>Binary indicator variable: 1 indicates that the firm has SCM assets; otherwise 0</td></tr><tr><td>IT-intensity</td><td>Binary indicator variable: 1 indicates that the firm is in an IT-intensive industry; otherwise 0</td></tr><tr><td>Competitiveness</td><td>Binary indicator variable: 1 indicates that the firm is in a competitive industry; otherwise 0</td></tr></table>

Table 2. Firms’ BDA Diffusion Rate over Time and by Industry Groups

<table><tr><td>BDA diffusion rate</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td></tr><tr><td>Overall</td><td>0.61</td><td>0.68</td><td>0.70</td><td>0.73</td><td>0.75</td><td>0.77</td><td>0.79</td></tr><tr><td>IT-intensive industries</td><td>0.62</td><td>0.68</td><td>0.72</td><td>0.74</td><td>0.76</td><td>0.77</td><td>0.79</td></tr><tr><td>Competitive industries</td><td>0.63</td><td>0.69</td><td>0.72</td><td>0.74</td><td>0.76</td><td>0.78</td><td>0.79</td></tr></table>

Table 2 shows the development of the BDA diffusion rate in our data set over time and split up by industry groups. In 2008, about 61 percent of firms in our panel already had live BDA assets and this share increased to 79 percent over the seven years of observation. When comparing the diffusion rate between IT-intensive and not IT-intensive and competitive and not competitive industries, only marginal differences can be found.

Table 3 shows the distribution of firms by industry groups (see Figure 1A in the Appendix for a distribution by industries). The statistics show that our panel is mainly composed of firms in IT-intensive and competitive industries, predominantly from manufacturing, which is probably due to our data collection strategy, which was focused on the customers of one of the world’s largest enterprise software vendors.

Table 4 provides an overview of the input and output variables required to estimate productivity functions, and Table 5 shows their correlation coefficients. All data were extracted from the Compustat Global Fundamentals Annual database and were then adjusted to 2010 values using domestic producer price indices obtained from the OECD.<sup>3</sup>

Table 3. Totals and Percentages of Firms in Industry Groups

<table><tr><td></td><td>Yes</td><td>No</td></tr><tr><td>IT-intensive industries</td><td>564 (69.3%)</td><td>250 (30.7%)</td></tr><tr><td>Competitive industries</td><td>579 (71.1%)</td><td>235 (28.9%)</td></tr></table>

Table 4. Descriptive Statistics for Input and Output Factors

<table><tr><td>Variable</td><td>Mean</td><td>Median</td><td>SD</td><td>Minimum</td><td>Maximum</td></tr><tr><td>Sales (in millions of US$)</td><td>15,083.06</td><td>3,088.80</td><td>39,216.03</td><td>0</td><td>528,972.00</td></tr><tr><td>Labor (in thousands of employees)</td><td>34.53</td><td>8.40</td><td>96.95</td><td>0</td><td>2,201.00</td></tr><tr><td>Capital (in millions of US$)</td><td>6,273.18</td><td>686.51</td><td>18,775.34</td><td>0</td><td>276,419.80</td></tr><tr><td>Materials (in millions of US$)</td><td>9,937.51</td><td>1,735.34</td><td>30,650.40</td><td>0</td><td>478,069.90</td></tr></table>

Table 5. Correlations Among Input and Output Factors

<table><tr><td></td><td></td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>1</td><td>Sales</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>2</td><td>Labor</td><td>0.66</td><td>1.00</td><td></td><td></td></tr><tr><td>3</td><td>Capital</td><td>0.76</td><td>0.40</td><td>1.00</td><td></td></tr><tr><td>4</td><td>Materials</td><td>0.98</td><td>0.60</td><td>0.72</td><td>1.00</td></tr></table>

## Model Specifications and Estimators

As discussed earlier, we apply techniques developed in the IT business value literature to quantify the effect of BDA assets on firm performance. While there are a number of approaches to measure the impact of IT on firm performance, we use the Cobb–Douglas production function framework to measure the marginal effect of BDA on firm output after accounting for various firm inputs (i.e., labor, capital, materials, IT assets) and external factors (i.e., industry, year). Formally, the following regression specification is used to test H1:

$$
\begin{array}{l} \log (S a l e s) = \beta_ {0} + \beta_ {1} \log (L a b o r) + \beta_ {2} \log (C a p i t a l) + \beta_ {3} \log (M a t e r i a l s) \\ \qquad + \beta_ {4} B D A + C o n t r o l s + \varepsilon \end{array}
$$

where Sales is measured as firm sales, Labor is a measure of production input in terms of human labor and measured as number of employees, Capital is a measure of production input in terms of physical capital stock, Materials is a measure of production input in terms of material expenses. BDA is a binary dummy variable indicating whether a firm has BDA assets. The Controls comprise three binary dummy variables controlling for a firm’s general level of nonanalytical IT assets by indicating whether it has adopted transactional enterprise systems, namely, ERP, CRM, and SCM systems, and indicator variables for Industry and Year in order to account for structural differences between industries and industry-wide economic shocks.

To test H2 and H3, we augment the production function with binary dummy variables indicating whether a firm is in an IT-intensive (ITI) and/or competitive (COMP) industry as well as with interaction terms between BDA and ITI and/or COMP:

$$
\begin{array}{l} \log (S a l e s) = \beta_ {0} + \beta_ {1} \log (L a b o r) + \beta_ {2} \log (C a p i t a l) + \beta_ {3} \log (M a t e r i a l s) + \beta_ {4} B D A \\ \qquad + \beta_ {5} I T I + \beta_ {6} C O M P + \beta_ {7} B D A \times I T I + \beta_ {8} B D A \times C O M P \\ \qquad + C o n t r o l s + \varepsilon \end{array}
$$

We use three regression methods to estimate the coefficients of the above models. First, we use ordinary least squares (OLS) regression with cluster-robust standard errors to account for the repeated observations of the same firms over time and for potential heteroskedasticity. Second, we use a fixed-effects (FE) estimator with cluster-robust standard errors to control for any time-invariant factors related to individual firms that may bias the results (addressing omitted variable bias for those factors). Finally, we use a fixed-effects two-stage least squares (2SLS) regression with cluster-robust standard errors, instrumental variables (IV), and FE to avoid potential endogeneity issues. A well-known source of endogeneity in econometric studies on IT business value is reverse causality, a situation in which the output determines one or more of the inputs, rather than vice versa. For example, firms with high productivity can build up slack resources that they may decide to invest in acquiring new, innovative technologies, such as BDA. Another potential source of endogeneity is simultaneity bias, that is, bias that arises because two or more variables are simultaneously determined by the same omitted factors [4]. For example, if unobserved positive external shocks to a firm’s output (e.g., because of an exceptionally high demand for its products or hiring of a new highly skilled management) occur during an observation period, they may simultaneously increase productivity of the firm and its investments into BDA assets. In such situations, a firm’s BDA assets would be positively correlated with productivity, but BDA assets would not be the cause of the productivity gains. To address these problems, we treat the BDA variable as well as the control variables for ERP, CRM, and SCM as endogenous and use the average diffusion rates for these systems in a company’s industry for a given year as instrumental variables to correct for potential biases.

## Results

The primary results regarding the estimates of the impact of BDA—as well as capital, labor and materials—on firm output are shown in Table $6 . ^ { 4 }$ As the Cobb– Douglas production function measures the relationship between a firm’s inputs and its output, and due to the log-transformation of the output variable, the coefficient of the BDA dummy variable can be interpreted as the percent productivity change associated with owning BDA assets [4, 30].

To test H1, we estimate the general effect of BDA assets using three different estimators. In Column 1 we examine the impact of BDA assets using a pooled OLS regression with cluster-robust standard errors. The results show a positive and significant relationship between BDA and firm productivity, suggesting that live BDA assets are associated with a 4.1 percent increase in firm productivity. Column 2 shows the results of estimating the same model using an FE estimator, which controls for additional time invariant firm-level factors. The coefficient of the BDA variable remains significant and positive and is of the same magnitude (3.8 percent) as in the model before. Finally, Column 3 shows the results of using a 2SLS/IV with FE. In this model, we treat the BDA variable as well as the control variables for a firm’s nonanalytical IT assets (i.e., ERP, CRM, SCM) as endogenous and use the average percentage of adopters of BDA, ERP, CRM, and SCM in a firm’s industry as instruments to control for potential biases arising from reverse causality or omitted variables.<sup>5</sup> The magnitude of the coefficient estimate of the BDA variable falls considerably and becomes insignificant, indicating that the OLS and FE results should be interpreted with caution and that the direction of the causality between BDA and firm productivity in these models remains unclear. Hence, our empirical evidence does not fully support H1.

Table 6 Productivity Estimates

<table><tr><td rowspan="2"></td><td colspan="6">Dependent variable: log(Sales)</td></tr><tr><td>OLS(1)</td><td>FE(2)</td><td>2SLS/IVwith FE(3)</td><td>2SLS/IVwith FE(4)</td><td>2SLS/IVwith FE(5)</td><td>2SLS/IVwith FE(6)</td></tr><tr><td>log(Capital)</td><td>0.090***(0.015)</td><td>0.127***(0.029)</td><td>0.127***(0.029)</td><td>0.128***(0.029)</td><td>0.128***(0.029)</td><td>0.129***(0.029)</td></tr><tr><td>log(Labor)</td><td>0.296***(0.024)</td><td>0.472***(0.043)</td><td>0.472***(0.043)</td><td>0.471***(0.043)</td><td>0.471***(0.043)</td><td>0.470***(0.043)</td></tr><tr><td>log(Materials)</td><td>0.667***(0.023)</td><td>0.442***(0.035)</td><td>0.442***(0.035)</td><td>0.443***(0.035)</td><td>0.442***(0.035)</td><td>0.443***(0.035)</td></tr><tr><td>BDA</td><td>0.041**(0.020)</td><td>0.038*(0.021)</td><td>0.016(0.022)</td><td>-0.031(0.032)</td><td>-0.023(0.031)</td><td>-0.047(0.037)</td></tr><tr><td>BDA × ITI</td><td></td><td></td><td></td><td>0.067*(0.034)</td><td></td><td>0.053(0.033)</td></tr><tr><td>BDA × COMP</td><td></td><td></td><td></td><td></td><td>0.057*(0.035)</td><td>0.039(0.033)</td></tr><tr><td>Industry dummies?</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Year dummies?</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>IT Asset dummies?</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>5,698</td><td>5,698</td><td>5,698</td><td>5,698</td><td>5,698</td><td>5,698</td></tr><tr><td> $R^2$ </td><td>0.977</td><td>0.791</td><td>0.790</td><td>0.790</td><td>0.790</td><td>0.790</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.977</td><td>0.755</td><td>0.755</td><td>0.754</td><td>0.754</td><td>0.754</td></tr><tr><td colspan="7">*p&lt;0.1; **p&lt;0.05; ***p&lt;0.01.Notes: Robust standard errors are clustered on firms as shown in parentheses. IT Asset dummies include ERP, CRM, and SCM. All 2SLS/IV estimations use average percentage of BDA, ERP, CRM, and SCM adopters in a firm&#x27;s industry for a given year as instrumental variables.</td></tr></table>

Column 4 shows the results of estimating a 2SLS/IV with FE model to test H2. (In the following, we will only report the results of the 2SLS/IV with FE estimations, as they are able to address potential endogeneity issues.) The main effect of BDA assets on firm productivity becomes insignificant, but we see a significant (at the p < 10% level) positive relationship between BDA assets and productivity for firms operating in IT-intensive industries. The results suggest a 6.7 percent higher productivity for firms with live BDA assets in IT-intensive industries, which is a substantial increase in magnitude compared to the models in Columns 1 and 2. As the 2SLS/IV estimator is able to control for endogeneity, we can be more confident in interpreting these associations as causal relationships between BDA assets and firm performance, hence providing empirical support for H2. Companies in IT-intensive industries seem to profit substantially from live BDA assets, while companies that are not in ITintensive industries seem not to be able to extract measurable productivity increases from BDA assets.

In Column 5 we examine the impact of BDA on firm productivity for companies in highly competitive industries (H3). Again, the coefficient estimate for the main effect of BDA assets is insignificant and the coefficient of the interaction term is significant and positive. Comparing the productivity effect of BDA for companies in highly competitive industries with the effect for companies in IT-intensive industries shows that it is slightly lower in magnitude (5.7 percent), but still substantially larger than the estimates obtained when averaging over all industries (H1). Again, these results indicate that live BDA assets are associated with higher productivity for firms in highly competitive industries, while for firms in noncompetitive industries no measurable impacts can be observed. Hence, the results support H3.

It is difficult to disentangle moderating effects of industry IT-intensity (H2) and competitiveness (H3) on BDA business value, as many important industries in our sample are both IT-intensive and highly competitive (e.g., manufacturing industries). Column 6 shows the results of simultaneously considering the effect of both context variables. The coefficient estimates for both interaction terms shrink in magnitude and are only statistically significant at the 11 percent (for IT-intensity) and 24 percent (for competitiveness) level. When considering these results in combination with the results in Columns 4 and 5, it is likely that the lower and insignificant coefficient estimates can be explained by the reduced statistical power of the analysis when increasing the complexity of the regression model.

## Discussion

This study is one of the first to quantify the impact of technical BDA assets on productivity for a large and diverse sample of firms. Although prior studies (e.g., [12, 62]) have provided first empirical evidence for the positive impact of BDA on firm performance, to the best of our knowledge our study is the first that completely relies on objective measurements of BDA assets, rather than on self-reported perceptual measures or proxies. In addition, our study is the first to provide detailed insights into industryspecific differences in the business value of BDA. Hence, the main contribution of our work is that it adds large-scale, reliable, and differentiated empirical evidence to the emerging body of knowledge on the business value of BDA.

Our OLS and FE results for H1 indicate when averaging over all industries, live BDA assets, are associated with a 4 percent increase in firm productivity. This estimate is in the range of effects found by other econometric studies on the business value of DDD [12] or investments in big data skills [62], which lends credibility to both our findings and theirs. However, the insignificant results obtained from the 2SLS/IV with FE regression suggest that we have to be careful when interpreting these relationships as a causal effect and that our estimates may be biased due to reverse causality or omitted variables. Hence, building on our findings, future research should continue to examine the causality between BDA and firm performance. A promising approach might be to combine measures of BDA assets with data about data-driven decision-making practices to model the information value chain at a more fine-grained level, starting from the collection and extraction of knowledge from big data via BDA assets over the actual use of this knowledge in decision making to enhanced firm performance. In addition, it might also be helpful to consider other firm performance measures than productivity. As Hitt et al. [30, p. 80] noted, production functions are a “short run measurement framework,” and some firms or industries might not realize short-term benefits from BDA, but rather mid- to long-term benefits. Or the benefits may have a more intangible nature (e.g., more operational flexibility, deeper knowledge about customers) and require unique measurement approaches in order to be detected. Hence, another direction for future research is to triangulate and extend our findings using different measurement instruments.

When testing H2 and H3, we found major differences in returns from BDA between industries. While live BDA assets in firms in IT-intensive industries increase productivity by 6.7 percent, we found no measurable productivity impacts of BDA assets for firms outside of this group, supporting H2. Similarly, we found BDA-associated productivity gains of 5.7 percent for firms in highly competitive industries and no measurable productivity impact for firms that do not belong to those industries, supporting H3. Both estimates were obtained using 2SLS/IV with FE models, which control for reverse causality and omitted variables. Hence, when focusing on these industry subgroups, we can be more confident in interpreting the observed correlations as cause-and-effect relationships. Our findings related to ITintensity support the results obtained by Tambe [62], who found that only firms with substantial data assets and access to labor markets with big data skills are able to profit from big data investments. These results can probably be explained by the fact that BDA solutions require complementary IT assets and capabilities, such as transactional enterprise systems or data scientists, which can provide the necessary data and skills to extract knowledge out of this data. When it comes to industry competitiveness, our study is the first study investigating its moderating effect on the process of extracting business value from big data. It seems that BDA enables companies in highly concentrated markets to eliminate slack, for example by automating routine decision-making tasks, and to design products and services that offer superior value to the customer and are distinct from the competition, for example, by making them smarter through data and algorithms [67]. Overall, our analysis of industry-specific differences in the value of BDA should motivate future research to empirically investigate further industry-level moderators, such as, the nature of the value proposition (e.g., product vs. service, tangible vs. intangible, physical vs. digital), the type of markets (e.g., B2B vs. B2C), or different distribution channels (e.g., online vs. bricks-and-mortar).

Our findings also have important managerial implications. Overall, they suggest that BDA is a productive investment and that the potential return yields are more lucrative than for many other types of IT assets [59, 60]. However, before deciding to invest in BDA assets, managers should consider the specifics of the industry in which they operate, as our findings suggest that only companies in IT-intensive and/ or highly competitive industries experience measurable productivity improvements that can be associated with BDA. By quantifying the magnitude of these improvements, our study can inform decision makers in preparing business cases calculating the costs and benefits of BDA assets before making investment decisions.

## Limitations

As is the case with any econometric study, our research design has certain limitations. Methodologically, our findings can potentially be undermined by a multitude of interrelated factors that influence firm productivity, not all of which we were able to consider in our model specifications. Although we used instrumental variables regression to address potential endogeneity problems, one has to be careful with interpreting the relationship between BDA assets and productivity as a causal relationship, as it is difficult to control for temporal precedence and alternative explanations in an observational study. In addition, there are a number of limitations that are related to our data set. First, our data set includes only companies that are publicly traded on U.S. stock exchanges. Although our sampling choice was justified by the availability of financial performance data, it restricts the generalizability of our findings to medium and large enterprises that act in global markets. Second, we investigated only companies that adopted BDA solutions from one particular vendor. Although this vendor is among the global leaders in enterprise systems, care should be taken in transferring our findings to BDA solutions that come from other vendors or are based on other technical architectures (e.g., open-source solutions for distributed big data processing, such as Hadoop). Third, our models do not include lagged variables to test for time lags in the effect of BDA assets on firm productivity. Introducing time lags leads to a decrease of the number of observations in a panel data set, which, in our case, led to a substantial reduction of the statistical power of our regression models. Testing for time lags with larger data sets could therefore be another direction for further research. Finally, our study focused on technical BDA assets, that is, ownership of hardware and software licenses, and did not explicitly measure other types of BDA assets, such as, BDA-related human resources or management capabilities [55]. Although the effects of the latter types of assets on firm performance have been investigated in other studies [12, 62], future research should aim to simultaneously quantify the business value of technical, human, and managerial BDA assets.

## Outlook

The market for BDA solutions is one of the fastest-growing IT markets, and while companies across industries are making substantial investments in BDA, the body of empirical evidence for the positive impact of BDA on organizational performance is still only emerging. Against this background, our study makes a substantial contribution to the body of knowledge on IT business value and business analytics by adding large-scale and reliable empirical evidence for the positive effect of BDA assets on firm productivity while also highlighting industry-level variables that can constrain firms’ ability to profit from BDA. The fact that not all companies in our sample showed immediate measurable productivity effects of BDA also provides motivation for further research on the business value of BDA. Besides studying other industry-level conditions, researchers should study the business value of various types of BDA assets, such as infrastructural, transactional, informational, and strategic BDA assets [66]. In addition, some organizational functions may benefit more from BDA than others. For example, research has suggested that most companies implement BDA to support customer-facing business processes [3, 6, 53].

## NOTES

1. Eight server racks and 1,500 terabytes of storage capacity.

2. Cluster with 750 nodes.

3. The current OECD data use 2010 as the default reference year.

## REFERENCES

1. Abbasi, A.; Sarker, S.; and Chiang, R.H. Big data research in information systems: Toward an inclusive research agenda. Journal of the Association for Information Systems, 17, 2 (February 2016), i–xxxii.

2. Accenture. Winning with analytics. 2016. www.accenture.com/us-en/\~/media/ Accenture/next-gen/hp-analytics/pdf/Accenture-Linking-Analytics-to-High-Performance-Executive-Summary.pdf.

3. Acker, O.; Gröne, F.; Blockus, A.; and Bange, C. In-memory analytics: Strategies for real-time CRM. Journal of Database Marketing and Customer Strategy Management, 18, 2 (July 2011), 129–136.

4. Aral, S.; Brynjolfsson, E.; and Wu, D.J. Which came first, IT or productivity? The virtuous cycle of investment and use in enterprise systems. In D. Straub and S. Klein (eds.), Proceedings of the International Conference on Information Systems. Milwaukee, 2006, 1–22.

5. Asadi Someh, I., and Shanks, G. How business analytics systems provide benefits and contribute to firm performance? In R. Baskerville, S. Gregor, J. v. Hilgersberg, and E. Winter (eds.), Proceedings of the European Conference on Information Systems. Münster, 2015, 1– 16.

6. Bange, C.; Grosser, T.; and Janoschek, N. Big data use cases: Getting real on data monetization. BARC Research Study, July 2015. barc-research.com/research/big-data-usecases-2015/.

7. Basole, R.C.; Seuss, C.D.; and Rouse, W.B. IT innovation adoption by enterprises: Knowledge discovery through text analytics. Decision Support Systems, 54, 2 (January 2013), 1044–1054.

8. Blackwell, D. Equivalent comparisons of experiments. Annals of Mathematical Statistics, 24, 2 (June 1953), 265–272.

9. Bloom, N.; Sadun, R.; and Van Reenen, J. Americans do IT better: US multinationals and the productivity miracle. American Economic Review, 102, 1 (February 2012), 167–201.

10. Brynjolfsson, E., and Yang, S. Information technology and productivity: A review of the literature. Advances in Computers, 43 (January 1996), 179–214.

11. Brynjolfsson, E., and Hitt, L. M. Paradox lost? Firm-level evidence on the returns to information systems spending. Management Science, 42, 4 (April 1996), 541–558.

12. Brynjolfsson, E.; Hitt, L.M.; and Kim, H.H. Strength in numbers: How does data-driven decision-making affect firm performance? Technical report. April 22, 2011. ssrn.com/ abstract=1819486.

13. Cabot Partners Group. Cost-benefit analysis: Comparing the IBM PureData System with Hadoop implementations for structured analytics. April 2015. dwi.org/\~/media/ 81023B6D9E3F4C9C870378E6FCD42227.PDF.

14. Centre for Economics and Business Research (CEBR). Data equity: Unlocking the value of big data. Report for SAS. April 2017. https://www.cebr.com/wp-content/uploads/ 2013/03/1733\_Cebr\_Value-of-Data-Equity\_report.pdf.

15. Chen, H.; Chiang, R.H.; and Storey, V.C. Business intelligence and analytics: From big data to big impact. MIS Quarterly, 36, 4 (December 2012), 1165–1188.

16. Cetorelli, N., and Strahan, P.E. Finance as a barrier to entry: Bank competition and industry structure in local US markets. Journal of Finance, 61, 1 (February 2006), 437–461.

17. Côrte-Real, N.; Oliveira, T.; and Ruivo, P. Assessing business value of big data analytics in European firms. Journal of Business Research. 70, 4 (2016), 379–390. dx.doi. org/10.1016/j.jbusres.2016.08.011.

18. Davenport, T.H., and Harris, J.G. Competing on Analytics: The New Science of Winning. Boston: Harvard Business Press, 2007.

19. Dehning B.; Richardson V.J.; and Zmud R.W. The financial performance effects of ITbased supply chain management systems in manufacturing firms. Journal of Operations Management, 25, 4 (June 2007), 806–824.

20. De Oliveira, M.P.V.; McCormack, K.; and Trkman, P. Business analytics in supply chains: The contingent effect of business process maturity. Expert Systems with Applications, 39, 5 (April 2012), 5488–5498.

21. Einav, L., and Levin, J. The data revolution and economic analysis: Technical report. Innovation Policy and the Economy, 14 (June 2014), 1–24.

22. Elbashir, M.Z.; Collier, P.A.; and Davern, M.J. Measuring the effects of business intelligence systems: The relationship between business process and organizational performance. International Journal of Accounting Information Systems, 9, 3 (September 2008), 135–153.

23. Feng, K.; Chen, E.T.; and Liou, W. Implementation of knowledge management systems and firm performance: An empirical investigation. Journal of Computer Information Systems, 45, 2 (January 2005), 92–104.

24. Galbraith, J.R. Organization design: An information processing view. Interfaces, 4, 3 (May 1974), 28–36.

25. Gartner. Magic Quadrant for Advanced Analytics Platforms. February 9, 2016. www. gartner.com/doc/reprints?id=1-2YEIILW&ct=160210&st=sb.

26. Gartner. Magic Quadrant for Business Intelligence and Analytics Platforms. February 4, 2016. www.gartner.com/doc/reprints?id=1-2XYY9ZR&ct=160204&st=sb.

27. Gorry, G.A., and Scott Morton, M.S. A Framework for Management Information Systems. Cambridge, MA: Massachusetts Institute of Technology, 1971.

28. Hendricks, K.B.; Singhal, V.R.; and Stratman, J.K. The impact of enterprise systems on corporate performance: A study of ERP, SCM, and CRM system implementations. Journal of Operations Management, 25, 1 (January 2007), 65–82.

29. Hitt, L.M., and Brynjolfsson, E. Productivity, business profitability, and consumer surplus: Three different measures of information technology value. MIS Quarterly, 20, 2 (June 1996), 121–142.

30. Hitt, L.M.; Wu, D.J.; and Zhou, X. Investment in enterprise resource planning: Business impact and productivity measures. Journal of Management Information Systems, 19, 1 (Summer 2002), 71–98.

31. Hu, Q., and Quan, J.J. Evaluating the impact of IT investments on productivity: A causal analysis at industry level. International Journal of Information Management, 25, 1 (February 2005), 39–53.

32. Hunton, J.E.; Lippincott, B.; and Reck, J.L. Enterprise resource planning systems: Comparing firm performance of adopters and nonadopters. International Journal of Accounting Information Systems, 4, 3 (September 2003), 165–184.

33. IBM. The essential CIO: Insights from the Global Chief Information Officer Study Executive Summary. New York: IBM Global Services, 2011.

34. IDC. Worldwide big data and business analytics revenues forecast to reach \$187 billion in 2019, according to IDC. Press release. May 23, 2016. www.idc.com/getdoc.jsp? containerId=prUS41306516.

35. Kohli, R., and Devaraj, S. Contribution of institutional DSS to organizational performance: Evidence from a longitudinal study. Decision Support Systems, 37, 1 (April 2004), 103–118.

36. LaValle, S.; Lesser, E.; Shockley, R.; Hopkins, M.S.; and Kruschwitz, N. Big data, analytics and the path from insights to value. MIT Sloan Management Review, 52, 2 (Winter 2011), 21–31.

37. Lee, B., and Menon, N.M. Information technology value through different normative lenses. Journal of Management Information Systems, 16, 4 (March 2000), 99–119.

38. Lee, S., and Kim, S.H. A lag effect of IT investment on firm performance. Information Resources Management Journal, 19, 1 (January 2006), 43–69.

39. Leibenstein, H. Allocative efficiency vs.” X-efficiency.” American Economic Review, 56, 3 (June 1966), 392–415.

40. Lindbeck, A., and Snower, D.J. Multitask learning and the reorganization of work: From Tayloristic to holistic organization. Journal of Labor Economics, 18, 3 (July 2000), 353–376.

41. Mahmood, M.A., and Mann, G.J. Information technology investments and organizational productivity and performance: An empirical investigation. Journal of Organizational Computing and Electronic Commerce, 15, 3 (January 1995), 185–202.

42. Malladi, S., and Krishnan, M. Determinants of usage variations of business intelligence and analytics in organizations: An empirical analysis. In R. Baskerville and M. Chau (eds.), Proceedings of the International Conference on Information Systems. Milan, 2013, 1–22.

43. Mangin, P.; Hovelaque, V.; and Bironneau, L. Enterprise resource planning contribution to firm performance: A literature review over the last 15 years. In Proceedings of the Congres International De Genie Industriel. Quebec, 2015, 1–10.

44. Manyika, J.; Chui, M.; Brown, B.; Bughin, J.; Dobbs, R.; Roxburgh, C.; and McKinsey Global Institute. Big data: The next frontier for innovation, competition, and productivity. June 2011. www.mckinsey.com/business-functions/business-technology/our-insights/big-datathe-next-frontier-for-innovation.

45. Melville, N.; Gurbaxani, V.; and Kraemer, K. The productivity impact of information technology across competitive regimes: The role of industry concentration and dynamism. Decision Support Systems, 43, 1 (February 2007), 229–242.

46. Mithas, S.; Ramasubbu, N.; and Sambamurthy, V. How information management capability influences firm performance. MIS Quarterly, 35, 1 (March 2011), 237–256.

47. Organization for Economic Cooperation and Development (OECD). Data-Driven Innovation for Growth and Well-Being: Interim Synthesis Report. Paris, 2014.

48. Poston, R., and Grabski, S. The impact of enterprise resource planning systems on firm performance. In S. Ang, H. Krcmar, W. Orlikowski and P. Weil (eds.), Proceedings of the International Conference on Information Systems. Brisbane, December 2000, 479–493.

49. PricewaterhouseCoopers. Investing in America’s data science and analytics talent. Business Higher Education Forum, April 2017. https://www.pwc.com/us/en/publications/ assets/investing-in-america-s-dsa-talent-bhef-and-pwc.pdf.

50. Rhoades, S.A. The Herfindahl–Hirschman index. Federal Reserve Bulletin, 79, 3 (March 1993), 188–189.

51. Sabherwal, R., and Jeyaraj, A. Information technology impacts on firm performance: An extension of Kohli and Devaraj (2003), MIS Quarterly, 39, 4 (December 2015), 809–836.

52. Sathye, M. X-efficiency in Australian banking: An empirical investigation. Journal of Banking and Finance, 25, 3 (March 2001), 613–630.

53. Saunders, A. Has information technology leveled the competitive playing field? Wharton School, University of Pennsylvania, Philadelphia. Working paper, 2010. dspace. mit.edu/bitstream/handle/1721.1/68967/773931578-MIT.pdf?sequence=2#page=59.

54. Schroeck, M.; Shockley, R.; Smart, J.; Romero-Morales, D.; and Tufano, P. Analytics: The Real-World Use of Big Data. Executive report. New York: IBM Institute for Business Value, 2012.

55. Schryen, G. Revisiting IS business value research: What we already know, what we still need to know, and how we can get there. European Journal of Information Systems, 22, 2 (March 2013), 139–169.

56. Sharma, R.; Mithas, S.; and Kankanhalli, A. Transforming decision-making processes: A research agenda for understanding the impact of business analytics on organisations. European Journal of Information Systems, 23, 4 (July 2014), 433–441.

57. Sircar, S.; Turnbow, J.L.; and Bordoloi, B. A framework for assessing the relationship between information technology investments and firm performance. Journal of Management Information Systems, 16, 4 (March 2000), 69–97.

58. Sodenkamp, M.; Kozlovskiy, I.; and Staake, T. Gaining IS business value through big data analytics: A case study of the energy sector. In T. Carte, A. Heinzl, and C. Urquhardt (eds.), Proceedings of the International Conference of Information Systems. Fort Worth, TX, 2015, 1–19.

59. Stiroh, K.J. Information technology and the US productivity revival: What do the industry data say? FRB of New York staff report. January 2001. papers.ssrn.com/sol3/ papers.cfm?abstract\_id=923623.

60. Stiroh, K.J. Investing in information technology: Productivity payoffs for US industries. Current Issues in Economics and Finance, 7, 6 (June 2001), 1–6.

61. Tambe, P.; Hitt, L.M.; and Brynjolfsson, E. The extroverted firm: How external information practices affect innovation and productivity. Management Science, 58, 5 (May 2012), 843–859.

62. Tambe P. Big data investment, skills, and firm value. Management Science, 60, 6 (June 2014), 1452–1469.

63. Teece, D.J. Profiting from technological innovation: Implications for integration, collaboration, licensing and public policy. Research Policy, 15, 6 (December 1986), 285–305.

64. vom Brocke, J.; Debortoli, S.; Müller, O.; and Reuter, N. How in-memory technology can create business value: insights from the Hilti case. Communications of the Association for Information Systems, 34, 1 (January 2014), 151–167.

65. Wegener, R., and Sinha, V. The value of big data: How analytics differentiates winners. Bain & Company, 2013. www.bain.com/Images/BAIN%20\_BRIEF\_The\_value\_of\_Big\_Data. pdf.

66. Weill, P., and Broadbent, M. Leveraging the New Infrastructure: How Market Leaders Capitalize on IT. Boston: Harvard Business School Press, 1998.

67. Wixom, B.H., and Ross, J.W. How to monetize your data. MIT Sloan Management, January 2017. sloanreview.mit.edu/article/how-to-monetize-your-data/.

68. Wall Street Journal Custom Studios. Data mastery: The global driver of revenue. Oracle, CA, 2015. www.oracle.com/us/dm/global-executive-study-2618506.pdf.

69. Zuboff, S. Automate/Informate: The two faces of intelligent technology. Organizational Dynamics, 14, 2 (September 1985), 5–18.

70. Zwanziger, J.; Melnick, G.A.; and Bamezai, A. Costs and price competition in California hospitals, 1980–1990. Health Affairs, 13, 4 (Fall 1994), 118–126.

## Appendix

![](/api/attachments/STUD438V/fulltext/images/150fbb6b2af2dd00bd7d1bc829df4ea078c3f1022ff3fede3e4bf1f1b1e833a8.jpg)  
Figure 1A: Distribution of firms by industries (SIC-1 level)
