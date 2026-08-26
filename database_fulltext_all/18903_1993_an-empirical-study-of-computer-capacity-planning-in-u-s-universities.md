---
otero_id: 18903
otero_key: "9V3F8T4D"
title: "An empirical study of computer capacity planning in U.S. universities"
authors: "Snehamay Banerjee; Magid Igbaria"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90014-k"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# An empirical study of computer capacity planning in U.S. universities

Snehamay Banerjee and Magid Igbaria
Drexel University, Philadelphia, PA, USA

Computer systems managers need to understand their applications and growth environment to analyze the current and predicted future workload, and plan for future capacity to meet business needs. This paper studies the computer capacity planning (CCP) practices at US universities to provide insight for computer capacity planners and administrators. Data were collected from 170 academic institutions in an attempt to learn the extent to which the various approaches and techniques of CCP are used there and to identify several important environmental factors affecting their use in practice. The study also examined the differences in CCP approaches between US universities and US industries. Results show that the computing environment is more interactive in universities and the computing budget is less than the computing budget of industry, but the basic approaches to CCP in universities are similar to those of in industry.

Keywords: Computer capacity planning, Performance evaluations, Universities.

![](/api/attachments/9V3F8T4D/fulltext/images/14c131256766e2a580896ae05826ca6704f5ce2833b8b83243e243ef68c12d98.jpg)

Magid Igbaria is a Professor of management information systems at Drexel University. Formerly, he lectured at Tel Aviv University, Hebrew University and Ben-Gurion University in Israel. He holds a B.A. in Statistics, and a M.A. in Information Systems and Operations Research from Hebrew University; he received his Ph.D. in Management Information Systems from Tel Aviv University. He has published articles on MIS personnel, economics of computers, computer performance evaluation, charging of computer services, compumetrical approaches in MIS, and microcomputers in business in Applied Statistics, Behaviour and Information Technology, Communications of the ACM, Computers and Operations Research, Decision Sciences, Decision Support Systems, Information and Management, Information Systems Research, Information Systems and Operational Research (INFOR), International Journal of Man-Machine Studies, Omega, MIS Quarterly, and others. His current research interests focus upon economics of computers, management of information systems, career development of MIS professionals, and end-user computing.

## 1. Introduction

Computers are valuable resources for any organization, requiring significant investment for their installation and maintenance. The importance of computing systems is very high at any academic institution, because of their role as a teaching and research tool. The demand in academia has grown in the recent past and is expected to increase in future (Statistical Abstract of the US Department of Commerce, 1990). There are many reasons for such an increase in demand for computing resources in universities. First, computers that were considered to be tools for faster mathematical computation are now used more for a wide range of activities e.g., music composition, painting, word processing. Second, administrators, students, and faculty are demanding information more frequently. Third, the use of sophisticated software and large data availability demands more computing power. Fourth, the use of computers as a teaching tool is increasing. Finally, there is a growing demand from the faculty due to an increase in sophistication and complexity of research projects using computers as calculators and for other needs.

![](/api/attachments/9V3F8T4D/fulltext/images/c315b7d2994edb5bc2580f1856ff4ae2a79c2a3c5898935f0d1a8f69d49ecf9b.jpg)

Growth of computer usage in academia in the recent past has been significant as evidenced by the following facts. Research and development (R & D) expenditure of U.S. universities increased from 6.06 billion dollars in 1980 to 13 billion dollars in 1988. This growth is expected to increase the computer usage in universities. The number of computers used in college campuses increased from 30,000 units (approximately) in 1981 to about 600,000 units in 1988. Also the number of academic fields using computer for teaching and research purposes has increased. All these point to a significant growth of computer usage in academic environments making computers a valuable resource to be utilized judiciously.

Monitoring and projecting computer workload and planning for changing or expanding computer configurations to satisfy future demand in a cost effective manner is generally referred to as Computer Capacity Planning (CCP) [12]. CCP is the process of relating user requirements to data processing (DP) parameters (e.g., Central Processing Unit (CPU) activity, throughput) and estimating the computer system that can satisfy those user requirements [5]. Different users have significantly different views of how to define and measure their requirements and DP professionals have different opinions on how to define and measure data processing parameters. This makes CCP definition difficult to generalize. Increased use of microcomputers in universities also has a major impact on CCP as it reduces the universities' dependence on traditional DP departments. However, such reduction in user dependence on DP departments does not eliminate the need for an effective CCP.

Capacity planning used to be an isolated technical function performed by DP professionals on an ad-hoc basis. However the impact of CCP on efficient running of any organization, the financial commitment associated with acquiring computing resources, and the recent availability of CCP software have allowed planners to focus more on organizational strategy than on analyzing data strictly at a technical level $[18]$ . Top management and administrators are recognizing the importance of CCP and are getting involved in this planning process. It is therefore important to understand and analyze current practices to suggest improvements in this field.

In this paper, the term capacity refers to the computing system as a whole and is defined as containing four critical parts [6]:

(a) System availability.

(b) Service level provided to users.

(c) Workload characterization.

(d) Capacity and utilization of resources.

Therefore capacity of a computing system represents a mixture of hardware and software characteristics and the way they are managed. Thus the scope of CCP goes beyond acquiring hardware and software and managing their utilization. This has led to the development of many models and different approaches to the planning process. Research on capacity planning include $[10,13,17,19]$ . There is also a vast literature available on computer performance measures $[1,2,3,4,7,8,15]$ . However, few studies focus on the extent to which these techniques and models have been used in practice.

Studies have been conducted to find out about capacity planning practices in industries. However, they are primarily aimed at commercial corporations and, to the best of the authors' knowledge no empirical data exists on capacity planning practices in educational institutions. Educational institutions are different from corporations, in many respects: Universities are primarily non-profit organizations and many do not directly charge users for computing resources. When students are charged (e.g., as a lab fee) for the use of computing resources such charges are not often based on their direct use of the resources. Thus computer users in universities do not have to make economic justification for the use of computing resources. They are made available on the basis of expressed or perceived need and not on the basis of a cost benefit analysis. So there are major differences between commercial corporations and the academic institutions about the usage, justification, and user need for computing resources.

These differences suggest that the data gathered from commercial organizations should not be used to predict the CCP practices of academic institutions. The lack of hard data and the need for understanding CCP academic practices have been the primary motivations for this study: it aims at finding what CCP approaches are used in universities, and the methods used for defining and measuring the parameters associated with CCP. These findings will help identify and develop CCP practices for future use. We believe that insight gained will not only benefit the CCP process of academic institutions but may provide insight to develop capacity planning methods for other non-profit organizations.

## 2. Research methodology

In early 1990, a questionnaire was distributed to 1400 directors of computer centers at US and Canadian universities. These participants are members of EDUCOM (a non-profit consortium of higher education institutions which facilitates the introduction, use, access, and management of information resources in teaching, learning, scholarship, and research); EDUCOM provided the authors with the mailing list. Participation in the study was strictly voluntary, and participants were assured that their individual responses to the survey would be treated confidentially. The sample was chosen because members of EDUCOM represent a wide variety of academic computer centers. We used the same questionnaire that was used by Lam for conducting a similar study on corporations [11,12]. Therefore, there was no need to validate this questionnaire. One hundred and eighty four questionnaires (response rate of 13.1 percent) were returned to the researchers. It is acknowledged that the response rate is low due to the mail survey methodology and no follow-up questionnaires were used to increase the response rate. However, this is very similar to other mail surveys [9,16]. Fourteen questionnaires were eliminated due to missing data, leaving a usable sample of 170 academic institutions.

## 3. Survey results

A summary of the computing environment of the universities is presented in Table 1. This provides a profile of the respondents. The data represent computing facilities of a university as a whole.

Table 1  
Computing environment in the US universities.

<table><tr><td>Computing characteristics</td><td>Percentage break down among respondents</td></tr><tr><td>1. Principal Computer facility</td><td></td></tr><tr><td>Main frame computer</td><td>63</td></tr><tr><td>IBM main frame</td><td>47</td></tr><tr><td>Mini computer</td><td>79</td></tr><tr><td>DEC mini computer</td><td>61</td></tr><tr><td>2. Interactive usage</td><td></td></tr><tr><td>0–25% of total</td><td>12</td></tr><tr><td>26–50% of total</td><td>36</td></tr><tr><td>51–75% of total</td><td>37</td></tr><tr><td>76–100% of total</td><td>15</td></tr><tr><td>3. Batch usage</td><td></td></tr><tr><td>0–25% of total</td><td>31</td></tr><tr><td>26–50% of total</td><td>49</td></tr><tr><td>51–75% of total</td><td>17</td></tr><tr><td>76–100% of total</td><td>3</td></tr><tr><td>4. Database usage</td><td></td></tr><tr><td>0–25% of total</td><td>55</td></tr><tr><td>26–50% of total</td><td>32</td></tr><tr><td>51–75% of total</td><td>8</td></tr><tr><td>76–100% of total</td><td>5</td></tr><tr><td>5. Computer budget</td><td></td></tr><tr><td>Less than $0.5 million</td><td>25</td></tr><tr><td>$0.5 to $1 million</td><td>13</td></tr><tr><td>$1 to $2 million</td><td>21</td></tr><tr><td>$2 to $3 million</td><td>15</td></tr><tr><td>$3 to $5 million</td><td>11</td></tr><tr><td>$5 to $10 million</td><td>9</td></tr><tr><td>More than $10 million</td><td>6</td></tr><tr><td>6. Charging end users</td><td></td></tr><tr><td>No Charge</td><td>51</td></tr><tr><td>Charge for some services</td><td>31</td></tr><tr><td>Charge</td><td>18</td></tr><tr><td>7. Planning Horizon</td><td></td></tr><tr><td>1–2 years</td><td>25</td></tr><tr><td>3–4 years</td><td>43</td></tr><tr><td>5 years or more</td><td>32</td></tr><tr><td>8. Degree of decentralization</td><td></td></tr><tr><td>Decentralized 1</td><td>6</td></tr><tr><td>· 2</td><td>15</td></tr><tr><td>· 3</td><td>19</td></tr><tr><td>· 4</td><td>31</td></tr><tr><td>Centralized 5</td><td>29</td></tr></table>

## 3.1. Computing environment of the respondents

The computing environment of the universities represented in our survey can be described as follows:

(a) Sixty three percent of the respondents have mainframe computers of which 75% are IBM and 11% are CDC. In spite of major advances in the use of personal computers, larger computers still represent a major computing resource for universities. Minicomputers are used by 79% of the respondents, of which 76% are DEC-VAX and 13% are Hewlett-Packard. None of the universities in the survey have a Japanese mainframe computer (e.g., NEC, TOSHIBA, FUJITSU).

(b) Thirty six percent of all respondents indicated that 26% to 50% of their jobs are interactive while 37% indicated that 50–75% are interactive. Only 20% of the respondents said that more than 50% of their jobs are batch. This suggests that interactive computing is more commonly used in universities than batch, as 52% of respondents indicated that more than 50% of their computer usage is interactive. Therefore parameters related to interactive computing should play a significant role in CCP exercises. Database related jobs do not represent a high work load, as 55% of the universities indicate that less than 25% of their computer usage is for database purposes.

(c) Utilization of computer resources for CCP is low, as 72% of the universities use less than 2% of their computer usage for this function. However, such low computer usage for CCP is not surprising. The most popular method for projecting computer workload among the respondents is visual trending (a graphical representation of the workload). Hence, sophisticated techniques for projecting computer workload or predicting response time requiring computer usage are not frequently used.

(d) Existence of performance measures is an indication of the importance of the item. About two thirds (65%) of all respondents indicated that they have no defined or established performance objectives; e.g., computer system design, computer system selection, or improving the performance of existing systems. However, 43% of mainframe users have performance objectives. This suggests that performance objectives are more important to mainframe users.

(e) The Computer budget for the universities is not high. Thirty nine percent of the respondents had budgets of less than 1 million dollars and three fourths of the respondents had budgets of less than three million dollars in 1989. Only about 6% of the responding universities had budgets of more than 10 million dollars in 1989.

The distribution of computing budgets (across all respondents) can be summarized as

<table><tr><td>Non PC Hardware</td><td>22.4%</td></tr><tr><td>Personal Computers</td><td>8.5%</td></tr><tr><td>Staff Salaries</td><td>38.4%</td></tr><tr><td>Telecomm, Teleproc. Equip</td><td>7.2%</td></tr><tr><td>Outside Software Pkg.</td><td>6.7%</td></tr><tr><td>Outside Services</td><td>6.3%</td></tr><tr><td>Others (Misc.)</td><td>10.5%</td></tr></table>

Staff salaries represent the largest component of computing budget. Therefore, the computing budget staffing needs should be evaluated carefully.

(f) About half the universities (51%) do not charge the users directly for computer usage and another 31% charge the users only for some services. Only 18% of universities charge their end users directly for computer usage compared to about two thirds of the companies who do the same [12].

(g) The typical Planning Horizon for CCP is either 3 years (used by 36% of respondents) or five years (used by 31% of respondents). Only 1% of the respondents plan beyond 5 years.

(h) The computer planning function is more centralized than decentralized in US universities. Sixty percent of the respondents indicated that they are more centralized than decentralized, with 29% totally centralized. Only 6% of the respondents are totally decentralized. This is contrary to the recent trend of decentralizing computing resources. The universities need to reevaluate their policy of centralizing computing resources.

(i) Most of the respondents (91%) are neutral on their satisfaction with CCP activities and the remaining respondents are symmetrically divided between satisfied and unsatisfied.

(j) The majority of respondents (60%) indicated that they are responsible for hardware, software, and data communication services for both academic and administrative systems. This indicates that administration of academic and administrative computing are not always separate.

![](/api/attachments/9V3F8T4D/fulltext/images/9faa87950dc3486e6e170a9b839868f64081d3003bf9c8193e3772a76c3921d7.jpg)  
Fig. 1. Methods to determine CPU upgrade.

## 3.2. Capacity planning approaches

Understanding capacity planning approaches used by universities is important for making plans. However, comparing such practices with those of the US industries may provide valuable insight to capacity planners. CCP approaches of US industries were reported by Lam [11] and comparisons of CCP approaches between US and Japanese industries were presented in [12]. The questionnaire for this study was adapted from the study by Lam [12]. Therefore, this questionnaire was not validated externally. Statistical analysis of data from this and our survey is not reasonable because of the time difference between them with changes such as evolving use and non availability of variance and sample size for the study on industries. But even a comparison of means can highlight some of the differences in CCP practices and provide ideas for refining existing CCP approaches. Table 2 shows the average ratings of methods used to measure CCP related factors. Questions 2 through 10 in the questionnaire dealt with the factors related to CCP and question 18 deal with the parameters used to select computers. Each method was rated on a Lickert scale of 1 to 5 where 1 represents least frequently used method and 5 represents the most frequently used method. Figures 1 through 10 present this information in a graphical form.

To analyze the data from our survey an analysis of variance and F test for each appropriate question was conducted which concluded that mean ratings of the methods used within a question (see Table 2 for mean ratings and descriptions of associated questions) are significantly different from each other at the 5% significance level (F = 36.5, 51.5, 6.4, 29.9, 18.3, 23.8, 14.9, and 229 for questions 2, 3, 4, 6, 7, 9, 10, and 18). This makes it possible to identify the preferred method(s) for predicting each CCP related factor. T-tests were used ( $\alpha = .05$ ) for finding the significant differences between methods, where appropriate. The results can be summarized as follows:

Table 2 and Figure 1 show that the preferred method to determine CPU upgrade requirement is by predicting response time for all categories of a: Predict disk storage requirements  
b: Predict data access rate  
c: Predict response time  
d: Predict technological innovations  
e: Acquire new disk along with new CPU a: Based on past performance experiences

![](/api/attachments/9V3F8T4D/fulltext/images/f9014a89c6ce872565ae7784d4701d69d5462c7317473d933a714dafb006b869.jpg)

Fig. 2. Methods to determine disk upgrade requirement.  
![](/api/attachments/9V3F8T4D/fulltext/images/ac6e47d66500f0713fec4721b9727cc0238bbae0f8bda08524ed63b5e319b7fa.jpg)  
Fig. 3. Methods to predict response time.

![](/api/attachments/9V3F8T4D/fulltext/images/aa8b5ca8273feeaed1d5c125727cebf3fabb4bed588b5053094c623c9fbd1e1e.jpg)

b: Based on industry-wide practice

c: Based on negotiations with major user groups

d: Based on the effect of response time on user productivity computer users. However, mainframe users also use CPU utilization as a measure [significantly $(\alpha = .05)$ more than non mainframe users]. The

Fig. 4. Methods to establish performance objectives.  
![](/api/attachments/9V3F8T4D/fulltext/images/fcd9b151c30f578e68e8c27092198b4def3983d9a01d462558a0e517ee8e7db1.jpg)  
Fig. 5. Methods for projecting computer workload.

X-axis in each figure represents the methods used to perform the task under consideration as presented in Table 2.

Table 2  
Ratings of the methods used for CCP practices. $^{a}$

<table><tr><td></td><td>U.S. Univ.All Comp</td><td>U.S. Univ.MainFrame</td><td>U.S. Univ.No MainFrm</td><td>IndustryU.S.</td></tr><tr><td colspan="5">Q2 Method used to determine when CPU upgrade is required</td></tr><tr><td>(a) Predict CPU utilization</td><td>3.29</td><td>3.58</td><td>2.80</td><td>4.37</td></tr><tr><td>(b) Predict performance e.g., response time</td><td>3.83</td><td>3.84</td><td>3.82</td><td>4.04</td></tr><tr><td>(c) Predict technological innovations</td><td>2.60</td><td>2.64</td><td>2.52</td><td>2.91</td></tr><tr><td colspan="5">Q3 Methods used to determine when disk upgrade is required</td></tr><tr><td>(a) Predict disk storage requirements</td><td>4.14</td><td>4.16</td><td>4.10</td><td>4.55</td></tr><tr><td>(b) Predict data access rate</td><td>2.35</td><td>2.45</td><td>2.17</td><td>2.75</td></tr><tr><td>(c) Predict response time</td><td>3.30</td><td>3.37</td><td>3.15</td><td>3.34</td></tr><tr><td>(d) Predict technological innovations</td><td>2.55</td><td>2.65</td><td>2.38</td><td>2.80</td></tr><tr><td>(e) Acquire new disk along with new CPU</td><td>3.04</td><td>2.90</td><td>3.28</td><td>2.46</td></tr><tr><td colspan="5">Q4 Methods used to predict response time</td></tr><tr><td>(a) Plot and extrapolate</td><td>2.78</td><td>2.99</td><td>2.40</td><td>3.57</td></tr><tr><td>(b) Use simple queuing models</td><td>2.10</td><td>2.18</td><td>1.96</td><td>2.75</td></tr><tr><td>(c) Use queuing network models</td><td>1.56</td><td>1.46</td><td>1.73</td><td>2.19</td></tr><tr><td>(d) Use performance modeling packages</td><td>1.89</td><td>1.89</td><td>1.90</td><td>2.69</td></tr><tr><td>(e) Use synthetic load benchmarking</td><td>1.82</td><td>1.90</td><td>1.67</td><td>2.07</td></tr><tr><td colspan="5">Q5 Methods used to establish performance objectives</td></tr><tr><td>(a) Based on past performance experiences</td><td>4.06</td><td>3.98</td><td>4.00</td><td>4.19</td></tr><tr><td>(b) Based on industry-wide practice</td><td>2.62</td><td>2.77</td><td>2.56</td><td>2.69</td></tr><tr><td>(c) Based on negotiations with major user groups</td><td>3.50</td><td>3.48</td><td>2.80</td><td>3.59</td></tr><tr><td>(d) Based on the effect of response time onuser productivity</td><td>2.36</td><td>2.32</td><td>2.40</td><td>2.70</td></tr><tr><td colspan="5">Q6 Methods used for projecting computer workload</td></tr><tr><td>(a) Visual trending</td><td>3.89</td><td>3.93</td><td>3.84</td><td>4.04</td></tr><tr><td>(b) Use time-series regression</td><td>2.04</td><td>2.08</td><td>1.98</td><td>2.70</td></tr><tr><td>(c) Use structural models</td><td>2.53</td><td>2.55</td><td>2.50</td><td>3.31</td></tr><tr><td>(d) Use sophisticated forecasting techniques</td><td>1.43</td><td>1.43</td><td>1.43</td><td>1.62</td></tr><tr><td>(e) Survey users for their own projections</td><td>2.81</td><td>2.91</td><td>2.64</td><td>3.37</td></tr><tr><td colspan="5">Q7 Methods used to define computer workload</td></tr><tr><td>(a) Total CPU hours consumed</td><td>3.61</td><td>3.74</td><td>3.39</td><td>3.90</td></tr><tr><td>(b) CPU hours consumed by workload class</td><td>3.19</td><td>3.28</td><td>3.03</td><td>4.04</td></tr><tr><td>(c) Transaction/Job counts</td><td>3.06</td><td>3.40</td><td>2.50</td><td>3.95</td></tr><tr><td>(d) Total composite measure units</td><td>2.40</td><td>2.60</td><td>2.07</td><td>2.97</td></tr><tr><td>(e) Composite measure units by workload class</td><td>2.21</td><td>2.36</td><td>1.97</td><td>2.85</td></tr><tr><td>(f) Traffic rate in communication network</td><td>2.52</td><td>2.66</td><td>2.28</td><td>3.35</td></tr><tr><td colspan="5">Q8 Methods used for data collection and analysis</td></tr><tr><td>(a) Collect continuously and analyze all data</td><td>2.89</td><td>2.99</td><td>2.71</td><td>3.31</td></tr><tr><td>(b) Collect continuously and analyze sample data</td><td>2.67</td><td>2.82</td><td>2.42</td><td>3.15</td></tr><tr><td>(c) Collect and use sample data</td><td>2.80</td><td>2.85</td><td>2.72</td><td>3.012</td></tr><tr><td>(d) Collect only as required at irregular intervals</td><td>2.80</td><td>2.83</td><td>2.75</td><td>2.37</td></tr><tr><td colspan="5">Q9 Methods used for performance measures in capacity planning</td></tr><tr><td>(a) System availability/reliability</td><td>4.01</td><td>4.11</td><td>3.82</td><td>-</td></tr><tr><td>(b) Interactive response time</td><td>4.10</td><td>4.18</td><td>3.97</td><td>-</td></tr><tr><td>(c) Batch turnaround time</td><td>3.08</td><td>3.13</td><td>2.98</td><td>-</td></tr><tr><td>(d) Consistency of response/turnaround time</td><td>3.40</td><td>3.44</td><td>3.33</td><td>-</td></tr><tr><td>(e) System throughput</td><td>3.34</td><td>3.41</td><td>3.23</td><td>-</td></tr><tr><td colspan="5">Q10 Methods used to establish usefulness of skills for capacity planning</td></tr><tr><td>(a) Operating system internals</td><td>3.54</td><td>3.73</td><td>3.23</td><td>-</td></tr><tr><td>(b) Systems programming</td><td>3.69</td><td>393</td><td>3.26</td><td>-</td></tr><tr><td>(c) Applications Programming</td><td>3.06</td><td>3.11</td><td>2.98</td><td>-</td></tr><tr><td>(d) Computer operations</td><td>3.03</td><td>2.91</td><td>3.24</td><td>-</td></tr><tr><td>(e) Statistical analysis</td><td>3.06</td><td>3.15</td><td>2.89</td><td>-</td></tr><tr><td>(f) Modeling skill</td><td>2.52</td><td>2.67</td><td>2.25</td><td>-</td></tr><tr><td colspan="5">Q18 Criteria used to select a computer</td></tr><tr><td>(a) Hardware capacity and performance</td><td>4.45</td><td>4.41</td><td>4.51</td><td>-</td></tr><tr><td>(b) Software performance</td><td>4.17</td><td>4.10</td><td>4.29</td><td>-</td></tr><tr><td>(c) Vendor support and viability</td><td>4.21</td><td>4.24</td><td>4.16</td><td>-</td></tr><tr><td>(d) Application software availability</td><td>3.98</td><td>3.98</td><td>3.98</td><td>-</td></tr><tr><td>(e) Development, installation, and operating cost</td><td>4.16</td><td>4.16</td><td>4.14</td><td>-</td></tr><tr><td>(f) Configuration flexibility and expansion capacity</td><td>394</td><td>3.89</td><td>4.02</td><td>-</td></tr><tr><td>(g) Compatibility with the present computer system</td><td>3.98</td><td>4.04</td><td>3.79</td><td>-</td></tr><tr><td>(h) Delivery date</td><td>2.84</td><td>2.94</td><td>2.68</td><td>-</td></tr><tr><td>(i) Documentation available</td><td>3.44</td><td>3.45</td><td>3.42</td><td>-</td></tr></table>

$^{a}$ The rating used are: 1 = never used, 2 = rarely used, 3 = occasionally used, 4 = frequently used, 5 = very frequently used. The ‘Q’ numbers for each group refers to the question numbers in the questionnaire and are discussed in the text.

![](/api/attachments/9V3F8T4D/fulltext/images/6057c3cb67441d644e10893d6721d9ffd4318d9c41881b409990745e626e78be.jpg)  
a: Total CPU hours consumed

b: CPU hours consumed by workload class

c: Transaction/Job counts

d: Total composite measure units

e: Composite measure units by workload class

f: Traffic rate in communication network

Fig. 6. Methods used to define computer workload.

Predicting disk storage requirement is used to determine when disk upgrade is required (See Figure 2). This is the most popular method irrespective of whether the universities use a mainframe computer or not.

Figure 3 shows that simple plotting and extrapolation is the method used for predicting response time. Though this is not used very frequently, mainframe users tend to use the method more than do non-mainframe users. Sophisticated methods, e.g., queuing or network models, are not generally used for this purpose.

Two thirds of the universities did not have any established performance objective (Figure 4). The universities dealing with mainframe computers are more likely to have established performance objectives. If a university has established performance objectives, past performance is the most likely guide to establishing such objectives.

Sophisticated forecasting methods (including time series analyses) are not used for projecting computer workload (Figure 5). Visual trending is the most popular method for projecting computer workload for all computing environments.

Figure 6 shows that the most popular way to measure computer workload is the total number of CPU hours consumed. Mainframe users are more likely to use this measure than non mainframe users. CPU hours consumed by each workload class is a close second measure for all respondents. However, the mainframe environment uses transaction/job count as the second preferred method for this purpose, though this is not very popular with non-main frame users.

Data collection and analysis is not a frequent activity for computer centers (Figure 7). All forms of data collection and analysis procedures mentioned in the questionnaire are practiced by the computer centers that are engaged in such practices.

Both interactive response time and system availability are used for performance measures in CCP. There is no distinction between the main-frame users and non-users in this practice.

Knowledge of systems programming and operating system internals are described as the most useful skills for CCP by all respondents. However, a systems programming skill is the most desirable one for the mainframe environment, while, for the non-mainframe users, application programming is equally important.

![](/api/attachments/9V3F8T4D/fulltext/images/5f58fa0c853df964ec32705ac2dd26004ac8ee318574f212c5028f514f883e10.jpg)  
Fig. 7. Methods for data collection and analysis.

Hardware capacity and performance are the most significant criteria for selecting a computer. For the non-mainframe users, software performance is also important. Delivery date and documentation are considered least significant. Vendor support, cost, software availability, flexibility, and compatibility with current system are also significant criteria to all respondents for computer selection.

## 4. Analysis of the results

Using the CCP study on industry we observe some differences between universities and industry. Though the computing environment and budget for the universities and industry are not the same, there are many similarities in their use of different CCP methods. We first consider the similarities and differences in computing environments.

\- Universities have much less computer budget than industry. Only $6\%$ of the universities had a budget of more than 10 million dollars in 1989 compared to $37\%$ US companies with this in 1985. So there are more financial restrictions on the computing budget of universities.
- The computing environment is more interactive in universities. In industries only $32\%$ of respondents indicated that more than $50\%$ of their work load is interactive compared to $52\%$ of the universities reporting interactive work. Though the percentage usage of the batch jobs is not available for industry, only $20\%$ of the universities indicated that more than $50\%$ of their workload is batch.

\- The planning horizon for CCP in both universities and industries have a similar pattern, with more longer term planning (i.e., 5 or more years) in universities.

\- Since academic institutions do not look at their computing facilities as a resource that must be cost justified it is not surprising that many (51%) academic institutions do not directly charge users for computing resources. Only 18% of the academic institutions charge back their users directly, compared to 75% of the US companies.

Given the environment of the academic institutions and the background of the major users (i.e., faculty and students) it is expected that these users will expect to have a fast response time. University users may not optimize their utilization of resources, because there is no incentive to sacrifice demand on response time for better use of computing resources. Since more users in industry are charged directly for computing resources use, they tend to be more cost conscious. As a result, CPU utilization is the most favored method for predicting CPU upgrade requirement in US industries with response time running a close second, but response time is the favored criteria in universities.

The methods used by the universities and US industry are similar except for the fact that such measures are used more frequently in industry. The students in a university do not have clear understanding of the limitations of its DP department or of the university as a whole. Also, few universities have a common training program for its employees as do many corporations, and there is very little horizontal linkage between employees. So there is little communication between end users and the university DP department.

The projection of computer workload in the university is not based on volume of business as in industry. There are many uncertain factors, e.g., new research projects or hiring new faculty members who happen to be heavy computer users, can significantly alter the computer usage pattern.

The capacity planning activities in major corporations appear to be changing focus from data analysis and implementation to critical factors and competitive business strategy. In order to implement CCP, capacity planners work closely with non-MIS departments and it is assumed that users are aware of the corporate strategy. In the academic environment the main users (the students) are not concerned about the strategic plan of the university and many faculties are unaware of the long range plans of the university.

The net result should be some impact on the way that capacity planning procedures are handled in these two diverse environments. Our survey results indicate that this is not the case. Our general observation is that the methods are similar, but are less intensively used in the academic environment.

## 5. Conclusion

This study provided interesting insights into capacity planning. Most of the universities have no defined or established performance objectives. Results also show that personnel expenses consumed an average of 38.4 percent of the IS budget, which is consistent with the findings of Lockwood and Sobol [14]. This suggests that universities should manage their DP employees more effectively. Furthermore, most of the universities do not charge back directly. As the demand for computing resources grow and the budget become tighter, it may be advisable to consider a charging system. Finally, while the present study provides some important insights for MIS managers, but it raises several issues that should be further investigated.

Acknowledgements: We are thankful to Dr. E.H. Sibley and the two anonymous reviewers for their assistance in improving the quality of the manuscript.

## References

[1] Ahituv, N., and Igbaria, M., A Model for Predicting and Evaluating Computer Resource Consumption, Communications of the ACM, Vol. 31, No. 12, December 1988, pp. 1467–1473.

[2] Borovits, I., Management of Computer Operations, Prentice Hall, N.J., 1984.

[3] Borovits, I. and Ein-Dor, P., Cost/Utilization: A Measure of System Performance, Communications of the ACM, Vol. 20, No. 3, March 1977, pp. 185–190.

[4] Borovits, I., and Neumann, S., Computer Systems Performance Evaluation, Lexington Books, Lexington, Mass., 1979.

[5] Bronner, L., Capacity Planning Basic Hand Analysis, IBM Technical Bulletin, No. GG22-9344-00, December 1983

[6] Cortada, J., Managing D. P. Hardware - Capacity Planning, Cost Justification, Availability, and Energy Management, Prentice Hall, N.J., 1983.

[7] Denning, P., Performance Analysis: Experimental Computer Science at its Best, Communications of the ACM, Vol. 24, No. 11, Nov. 1981, pp 725–727.

[8] Ein-Dor, P. and Jones, C.R., Information Systems Management, Elsevier, New York, 1985.

[9] George, W. and Barklade, H. Marketing Activities in the Service Industries, Journal of Marketing, Vol. 7, 1974, pp. 65–70.

[10] Igbaria, M., Managing and Forecasting Hardware Resource Consumption, INFOR, Vol. 28, No. 4, November 1990, pp. 412–421.

[11] Lam, S.F. and Chan, K.H., Computer Capacity Planning: Theory and Practice, Academic Press, Orlando, Florida, 1987.

[12] Lam, S.F., An Empirical Study of Computer Capacity Planning in Japan, Communication of the ACM, Vol. 31, No. 8, August 1988, pp. 965–976.

[13] Lazowska, E.D., and Zahorjan, J., Graham, G.S., and Sevcik, K., C., Quantitative System Performance, Computer System Analysis Using Queuing Network Models, Prentice Hall, N.J., 1984.

[14] Lockwood, D.L. and Sobol, M.G., IS Spending Survey: Communications Technologies Dominate Growth Areas, Journal of Systems Management, 40 (December 1989), 31–37.

[15] McKerrow, P., Performance Measurement of Computer Systems, Addison Wesley Publishing Co., 1987.

[16] McNamara, C. The Present Status of the Marketing Concept, Journal of Marketing, 1972, pp. 5–57.

[17] Stroebel, G.J., Baxter, R.D., and Denning, M.J., A Capacity Planning Expert System for IBM System/38, IEEE Computer, Vol. 19, No. 7, July 1986, pp. 42–50.

[18] Sullivan-Trainor, M., Capacity Planning, Computer World, January 12, 1987, pp. 41–50.

[19] Wicks, R.J., Balanced System and Capacity Planning, IBM Technical Bulletin, No. GG22-9299-00, November 1982.
