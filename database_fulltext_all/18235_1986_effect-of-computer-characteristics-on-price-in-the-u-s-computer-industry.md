---
otero_id: 18235
otero_key: "BKQSFDX3"
title: "Effect of computer characteristics on price in the U.S. computer industry"
authors: "S. Sircar; D.S. Dave"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90037-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Effect of Computer Characteristics on Price in the U.S. Computer Industry

S. Sircar

Department of Information Systems and Management Science, School of Business Administration, The University of Texas at Arlington, Arlington, 76019, USA

and

D.S. Dave

Department of Management, College of Business, Marshall University, Huntington, West Virginia 25701, USA

The relationship between the cost of a computer and its power is analyzed. Previous work by Grosch, Knight, and Cale et al. has been thoroughly revised. A highly reliable model is developed, with cost as the dependent variable and memory size, millions of instructions per second, (MIPS) memory cycle time and year of introduction as independent variables. This is done for four computer classes: IBM machines, IBM plug-compatible machines, IBM competitor machines, and superminicomputers. MIPS emerges as the single most important predictor of price. Pricing strategies for different computer classes are discerned. The model can be used by both users and manufacturers to determine appropriate computer system prices.

Keywords: Computer Price/Performance, Computer selection, economics, pricing.

![](/api/attachments/BKQSFDX3/fulltext/images/eb9cdf6a16fb4e8a40e6aac045bae660079ce3a4efd6a384373f4f32465e188e.jpg)

Dr. Sumit Sircar is an Associate Professor in the Information Systems and Management Science Department in the College of Business Administration of the University of Texas at Arlington. He earned a doctoral degree in 1976 at the Harvard Business School in the field of computer-based systems. Since then his research, teaching and consulting activities have been in the field of information resource management. He has published several articles in various journals on

different aspects of information management, including the appropriate management of emerging information technologies. He has also conducted numerous professional seminars on related topics.

## 1. Introduction

The relationship between the cost of a computer system and its power has been a topic of major interest throughout the history of computing. In their excellent study performed seven years ago, Cale et al. [2] reviewed previous efforts as quantifying this relationship. (The “cost” of a computer is usually defined as its market price because information about the actual costs are usually unavailable.)

The most well-known formulation of the price/power relationship is Grosch's law, which stated that the speed of computer systems increases in proportion to the square of their costs, giving rise to significant economies of scale [9]. The validity of the law was tested in a rigorous study by Knight in the mid-60's [13]. He defined computer power as a function of memory, compute time and input/output time and proceeded to establish a single value for the power of a system. He was then able to determine the relationship between computer power and price and, in fact, to confirm Grosch's law.

Major changes in computer technology since Knight's study (virtual memory, distributed intelligence, interactive computing, etc.) have rendered his formula for computer power quite unusable. In the view of some experts [1,11], the effect of advancing technology has been such that the power/price relationship is different for different price classes of computer, although the economies of scale argument is still valid. Grosch himself felt that the original law is still accurate [10].

![](/api/attachments/BKQSFDX3/fulltext/images/8e55d4f6fb067a1a09f7be03dc057c238a52906ec34644fb115c3dad962eaec0.jpg)  
management and information systems.

Some of the conclusions that Cale et al., arrived at were as follows

(i) Grosch's law is no longer valid.

(ii) The best single measure of computing power is computer price.

(iii) Measurement of a computer's power must be work-specific. It is meaningful to talk about how well different computers execute a certain job-stream.

They developed a model which directly related system price to measures of significant component characteristics. The model which provided the most consistent results was:

$$
\begin{array}{r l} \operatorname{Cost} & = \left(B _ {0} + B _ {3} D _ {1} + \dots + B _ {n} D _ {n}\right) \\ & \times \left(\text { Memory } ^ {B _ {1}} + \text { DASD } ^ {B _ {2}}\right), \end{array}
$$

where B represented coefficients and D represented the year of introduction in pairs (1972–73, 1974–75, etc.).

Furthermore, the study divided computer systems into two classes: general purpose computers and small business computers. It found significant differences in the relationship between system price, memory size, DASD capacity, between different years and system types.

This paper attempts to answer the general question of what has happened in the five years since the Cale et al., study to the relationship between system cost and characteristics. However, there are several important differences between the two approaches:

(a) Instead of classifying computer systems into general and small business classes, we have four different categories: IBM Mainframes, IBM Plug Compatible Machines (PCMs), IBM Competitor Mainframes and Superminis.

(b) The effect of advancing technology with the passage of time is established by individual years of introduction (1978, 1979, 1980, etc.).

(c) The independent variables used as computer system characteristics have been changed. The characteristics found to be most important were memory size, millions of instructions per second (MIPS), memory cycle time and year of introduction (see section on model development). The effects of each of these variables on system price are estimated for each of the four categories previously mentioned.

The main objective of the present study is thus to develop a reliable model that can identify which factors most significantly affect computer price. This will be attempted for all computer systems together, as well as for the separate classes of computers. Having achieved this, the model can be used to make managerial decision by determining whether a given computer system is underpriced or over priced relative to the norms for its class. The model is tested against several recent computer model introductions, including IBM's new Sierra computer and found to be reliable. A second objective is to estimate the effect of advancing technology by introducing year of introduction as a system characteristic.

## 2. Procurement of Data

Research in the information system field is severely hampered by the paucity of meaningful data. Fortunately, for this research, enough data were found in studies conducted by Computerworld during the period of 1980–1982 [3]. Some additional data were procured from the newly established Data Decisions information service [4] and later editions of Computerworld from 1984 and 1985 [3]. The data collected are presented in Table 1. System prices for IBM are for processor only; for all other manufacturers they include processor, console, power supply and all prerequisites, e.g., cooling systems. This is customary in the computer industry.

In work of this nature, it is now standard practice to use the “typical” configuration for each machine. The other parameters, viz., machine cycle time and MIPS, are constant for a given computer system.

## 3. Development of the Model

To determine the effects of the computer characteristics on system price, it is necessary to establish the relationship between them. Using the free market price of the systems as the most generally accurate measure of system performance [2], a model was developed that directly relates system cost to measures of significant system component characteristics. Out of different linear and non-linear models we tried, the model which provided the most consistent results was:

$$
\begin{array}{l} \text {Ln Price} = \beta_ {0} + \beta_ {1} (\text {Ln Memory}) + \beta_ {2} (\text {Ln MIPS}) \\ \quad + \beta_ {3} (\text {Ln Machine Cycle Time}) \\ \quad + \beta_ {4} (\text {Ln Memory}) D _ {7} + \beta_ {5} (\text {Ln Memory}) D _ {8} \\ \quad + \beta_ {6} (\text {Ln Memory}) D _ {9} + \beta_ {7} (\text {Ln MIPS}) D _ {7} \\ \quad + \beta_ {8} (\text {Ln MIPS}) D _ {8} + \beta_ {9} (\text {Ln MIPS}) D _ {9} \\ \quad + \beta_ {1 0} (\text {Ln Machine Cycle Time}) D _ {7} \\ \quad + \beta_ {1 1} (\text {Ln Machine Cycle Time}) D _ {8} \\ \quad + \beta_ {1 2} (\text {Ln Machine Cycle Time}) D _ {9} + \beta_ {1 3} D _ {1} \\ \quad + \beta_ {1 4} D _ {2} + \beta_ {1 6} D _ {3} + \beta_ {1 7} D _ {4} + \beta_ {1 8} D _ {5} + \beta_ {1 9} D _ {6} \\ \quad + \beta_ {2 0} D _ {7} + \beta_ {2 1} D _ {8} + \beta_ {2 2} D _ {9} + \beta_ {2 3} D _ {1} D _ {7} \\ \quad + \beta_ {2 4} D _ {2} D _ {8} +..... \end{array}
$$

where $\beta_{0}$ , $\beta_{1}$ , $\beta_{2}$ , $\beta_{3}$ , $\beta_{4}$ , … are the parameters to be estimated using a least square regression program [7].

The system of binary variables representing the year of introduction was defined as follows:

$$
\begin{array}{l l} D _ {1} = \left\{ \begin{array}{l l} 1 & \text { if   year   of   introduction   was   1978. } \\ 0 & \text { otherwise. } \end{array} \right. \\ D _ {2} = \left\{ \begin{array}{l l} 1 & \text { if   year   of   introduction   was   1979. } \\ 0 & \text { otherwise. } \end{array} \right. \\ D _ {3} = \left\{ \begin{array}{l l} 1 & \text { if   year   of   introduction   was   1980. } \\ 0 & \text { otherwise. } \end{array} \right. \\ \vdots \\ D _ {6} = \left\{ \begin{array}{l l} 1 & \text { if   year   of   introduction   was   1983. } \\ 0 & \text { otherwise. } \end{array} \right. \end{array}
$$

Here separate variables were used instead of one time variable so that the differing effects over different years could be estimated. Note that the base case, if $D_{1}=D_{2}=\ldots=D_{6}=0$ , covers computers introduced in 1977 or before.

Further, $D_{7}$ , $D_{8}$ , $D_{9}$ and $D_{10}$ discriminate between different computer systems, e.g.,

$$
D _ {7} = \left\{ \begin{array}{l l} 1 & \text { if   IBM   Mainframe   Computers. } \\ 0 & \text { otherwise. } \end{array} \right.
$$

$$
D _ {8} = \left\{ \begin{array}{l l} 1 & \text { if   IBM   Competitor   Computers. } \\ 0 & \text { otherwise. } \end{array} \right.
$$

$$
D _ {9} = \left\{ \begin{array}{l l} 1 & \text { if   IBM   Plug   Compatible   Computers. } \\ 0 & \text { otherwise. } \end{array} \right.
$$

The base case, $D_{7}=D_{8}=D_{9}=9$ gives the Supermini class.

Note that buffer size was not considered in the model. The reason is that in all formulations which were tried for the model, the co-efficient derived for such a measure was not significantly different from zero. Thus, the final model was run without this variable and finally we were left with three hardware characteristics in our measure of computer performance

## 3.1. MIPS and Machine Cycle Time

The potential problem of multicollinearity between MIPS and machine cycle time was investigated but found not to be a problem. A correlation matrix of the variables was obtained and the value of the zero-order correlation coefficient (r) found to be less than that of the middle correlation coefficient (R) [6,12].

Further note that the natural logarithm of memory (M-bytes), MIPS and machine cycle time (nsec) were not large enough to obtain $|X'X|$ as a sufficiently large number. Therefore, the matrix $(X'X)$ could not exist and hence, we could not get unbiased estimates for some of the parameters. In order to obtain a unique solution for the parameters, we converted memory size to k-bytes and MIPS and machine cycle time were multiplied by $10^{3}$ .

## 4. Results Obtained From the Model

## 4.1. Model Validity

Table 2 shows the results of the model run on all observations, using dummy variables for time and type of computer. The validity of the model is demonstrated by the high value of $R^{2}$ (0.989) obtained. \*

The model suggests that there are, in fact, significant differences in the relationship between system price, memory size, MIPS and machine cycle time, between years and type of computer.

Table 1  
Computer Characteristics and System Prices

<table><tr><td>System</td><td>Price(in $)</td><td>Memory(M-Bytes)</td><td>MIPS</td><td>Machine Cycle Time(n-sec)</td><td>YearIntroduced</td></tr><tr><td>Cyber 176</td><td>4505460</td><td>0.20</td><td>15.00</td><td>27.5</td><td>1974</td></tr><tr><td>Burroughs 1100/81</td><td>1554557</td><td>2.0</td><td>2.20</td><td>50.0</td><td>1976</td></tr><tr><td>DG MV 4000</td><td>56500</td><td>0.384</td><td>0.40</td><td>700.0</td><td>1976</td></tr><tr><td>Burroughs 1100/83</td><td>4200000</td><td>6.00</td><td>6.90</td><td>50.0</td><td>1977</td></tr><tr><td>Burroughs 1100/84</td><td>5400000</td><td>8.00</td><td>8.90</td><td>50.0</td><td>1977</td></tr><tr><td>CDC Omega 480/-I</td><td>218000</td><td>1.50</td><td>0.38</td><td>50.0</td><td>1977</td></tr><tr><td>Burroughs 7800</td><td>700000</td><td>3.00</td><td>3.50</td><td>63.0</td><td>1978</td></tr><tr><td>HP 3000/33</td><td>84739</td><td>1.00</td><td>0.29</td><td>90.0</td><td>1978</td></tr><tr><td>vHP 3000/111</td><td>126930</td><td>2.00</td><td>0.38</td><td>175.0</td><td>1978</td></tr><tr><td>DEC 11/780</td><td>143000</td><td>0.512</td><td>1.90</td><td>200.0</td><td>1978</td></tr><tr><td>IBM 3033 U</td><td>1626000</td><td>4.00</td><td>5.30</td><td>57.0</td><td>1978</td></tr><tr><td>IBM 3032</td><td>1338000</td><td>8.00</td><td>2.40</td><td>80.0</td><td>1978</td></tr><tr><td>IBM 3031</td><td>833900</td><td>8.00</td><td>1.10</td><td>115.0</td><td>1978</td></tr><tr><td>Burroughs 1100/61</td><td>693000</td><td>2.00</td><td>1.30</td><td>116.0</td><td>1979</td></tr><tr><td>CDC Cyber 170/720</td><td>460950</td><td>0.18</td><td>1.40</td><td>50.0</td><td>1979</td></tr><tr><td>CDC Cyber 170/730</td><td>731315</td><td>0.20</td><td>2.30</td><td>50.0</td><td>1979</td></tr><tr><td>CDC Cyber 170/750</td><td>2310025</td><td>0.20</td><td>7.50</td><td>25.0</td><td>1979</td></tr><tr><td>CDC Cyber 170/760</td><td>3100000</td><td>0.20</td><td>10.00</td><td>25.0</td><td>1979</td></tr><tr><td>HP 3000/30</td><td>72369</td><td>1.0</td><td>0.29</td><td>90.0</td><td>1979</td></tr><tr><td>Amdahl 470V/7A</td><td>1550000</td><td>4.0</td><td>4.60</td><td>29.0</td><td>1979</td></tr><tr><td>Amdahl 470V/8</td><td>2175000</td><td>4.0</td><td>7.00</td><td>26.0</td><td>1979</td></tr><tr><td>IBM 8140 A</td><td>80440</td><td>1.00</td><td>0.36</td><td>800.0</td><td>1979</td></tr><tr><td>IBM 4331-1</td><td>62170</td><td>1.00</td><td>0.20</td><td>900.0</td><td>1979</td></tr><tr><td>IBM 8130</td><td>30000</td><td>0.256</td><td>0.22</td><td>1500.0</td><td>1979</td></tr><tr><td>IBM 4341-1</td><td>225000</td><td>4.00</td><td>0.70</td><td>300.0</td><td>1979</td></tr><tr><td>IBM 3033 M</td><td>1833500</td><td>16.00</td><td>9.10</td><td>57.0</td><td>1979</td></tr><tr><td>Burroughs B 1900</td><td>109000</td><td>0.524</td><td>0.33</td><td>167.0</td><td>1980</td></tr><tr><td>Univac Sys. 80 Mod. 3</td><td>59261</td><td>0.262</td><td>0.13</td><td>180.0</td><td>1980</td></tr><tr><td>Univac Sys. 80 Mod. 5</td><td>82241</td><td>0.262</td><td>0.27</td><td>180.0</td><td>1980</td></tr><tr><td>CDC Cyber 170/740</td><td>1492500</td><td>0.20</td><td>4.20</td><td>25.0</td><td>1980</td></tr><tr><td>Burroughs B 6900</td><td>440000</td><td>3.00</td><td>1.08</td><td>167.0</td><td>1980</td></tr><tr><td>Honeywell DPS 8/20</td><td>199460</td><td>2.00</td><td>0.38</td><td>140.0</td><td>1980</td></tr><tr><td>DEC 11/750</td><td>89900</td><td>0.512</td><td>1.10</td><td>320.0</td><td>1980</td></tr><tr><td>DG MV/8000</td><td>175900</td><td>1.00</td><td>1.40</td><td>400.0</td><td>1980</td></tr><tr><td>Magnuson M80-31</td><td>182100</td><td>4.00</td><td>0.46</td><td>100.0</td><td>1980</td></tr><tr><td>Magnuson M80-32</td><td>217100</td><td>4.00</td><td>0.50</td><td>100.0</td><td>1980</td></tr><tr><td>Cambex 1636</td><td>170000</td><td>4.00</td><td>0.39</td><td>50.0</td><td>1980</td></tr><tr><td>Cambex 1641</td><td>280000</td><td>8.00</td><td>0.63</td><td>50.0</td><td>1980</td></tr><tr><td>NAS AS/3000N</td><td>275000</td><td>2.00</td><td>2.72</td><td>115.0</td><td>1980</td></tr><tr><td>NAS AS/3000</td><td>335000</td><td>4.00</td><td>0.90</td><td>115.00</td><td>1980</td></tr><tr><td>NAS AS/5000N</td><td>38500</td><td>4.00</td><td>0.90</td><td>92.0</td><td>1980</td></tr><tr><td>NAS AS/7000 DPC</td><td>2175000</td><td>8.00</td><td>5.40</td><td>72.0</td><td>1980</td></tr><tr><td>IPL</td><td>315000</td><td>8.00</td><td>0.81</td><td>50.0</td><td>1980</td></tr><tr><td>Amdahl 470V/7B</td><td>1250000</td><td>4.00</td><td>2.80</td><td>29.0</td><td>1980</td></tr><tr><td>IBM Sys 38/Mod. 5</td><td>118560</td><td>2.00</td><td>0.28</td><td>600.0</td><td>1980</td></tr><tr><td>IBM 4331-2</td><td>82500</td><td>1.00</td><td>0.40</td><td>900.0</td><td>1980</td></tr><tr><td>IBM 303N</td><td>1274000</td><td>8.00</td><td>3.70</td><td>57.0</td><td>1980</td></tr><tr><td>IBM 3033A</td><td>1833500</td><td>16.00</td><td>9.10</td><td>57.0</td><td>1980</td></tr><tr><td>NCR V 8650</td><td>1189000</td><td>6.00</td><td>2.20</td><td>38.0</td><td>1981</td></tr><tr><td>NCV V 8670</td><td>1813000</td><td>8.00</td><td>4.70</td><td>38.0</td><td>1981</td></tr><tr><td>Burroughs B 5900</td><td>240000</td><td>3.00</td><td>0.54</td><td>125.0</td><td>1981</td></tr><tr><td>Perkins 3230</td><td>65800</td><td>0.512</td><td>0.93</td><td>250.0</td><td>1981</td></tr><tr><td>Prime 150 II</td><td>47000</td><td>0.512</td><td>0.46</td><td>120.0</td><td>1981</td></tr><tr><td>Prime SRS 50/250 II</td><td>48500</td><td>0.512</td><td>0.46</td><td>120.0</td><td>1981</td></tr><tr><td>Prime 550 II</td><td>130000</td><td>2.00</td><td>0.63</td><td>120.0</td><td>1981</td></tr><tr><td>Prime 850</td><td>343000</td><td>4.00</td><td>1.52</td><td>120.0</td><td>1981</td></tr><tr><td>Magnuson M 80-42</td><td>324200</td><td>8.00</td><td>0.90</td><td>100.0</td><td>1981</td></tr><tr><td>Magnuson M 80-43</td><td>384200</td><td>8.00</td><td>1.10</td><td>100.0</td><td>1981</td></tr><tr><td>Cambex 1651</td><td>378000</td><td>8.00</td><td>0.92</td><td>50.0</td><td>1981</td></tr><tr><td>NAS AS/9000 N</td><td>1995000</td><td>4.00</td><td>7.10</td><td>48.0</td><td>1981</td></tr><tr><td>NAS AS/9000</td><td>2975000</td><td>8.00</td><td>8.80</td><td>40.0</td><td>1981</td></tr><tr><td>NAS As/9000 DPC</td><td>5555000</td><td>16.00</td><td>15.90</td><td>40.0</td><td>1981</td></tr><tr><td>IBM 3081-D</td><td>3260000</td><td>16.00</td><td>10.40</td><td>26.0</td><td>1981</td></tr><tr><td>IBM 4341-2</td><td>350000</td><td>4.00</td><td>1.20</td><td>180.0</td><td>1981</td></tr><tr><td>IBM 3033-S</td><td>990000</td><td>4.00</td><td>2.30</td><td>57.0</td><td>1981</td></tr><tr><td>NCR V 8555 M</td><td>101830</td><td>1.00</td><td>0.29</td><td>84.0</td><td>1982</td></tr><tr><td>NCR V 8565 M</td><td>173630</td><td>2.00</td><td>0.40</td><td>56.0</td><td>1982</td></tr><tr><td>NCR V 8575 M</td><td>252070</td><td>2.00</td><td>0.54</td><td>56.0</td><td>1982</td></tr><tr><td>NCR V 8585 M</td><td>442520</td><td>4.00</td><td>0.90</td><td>56.0</td><td>1982</td></tr><tr><td>HP 3000/44</td><td>178575</td><td>4.00</td><td>0.56</td><td>26.5</td><td>1982</td></tr><tr><td>DG MV/6000</td><td>87000</td><td>1.00</td><td>1.00</td><td>220.0</td><td>1982</td></tr><tr><td>Amdahl 580-5860</td><td>3800000</td><td>16.00</td><td>13.90</td><td>24.0</td><td>1982</td></tr><tr><td>IBM 3081-K</td><td>3860000</td><td>16.00</td><td>15.00</td><td>26.0</td><td>1982</td></tr><tr><td>IBM 4341-11</td><td>240000</td><td>2.00</td><td>0.88</td><td>120.0</td><td>1982</td></tr><tr><td>IBM 4341-10</td><td>170000</td><td>4.00</td><td>0.58</td><td>300.0</td><td>1982</td></tr><tr><td>IBM 8140-C</td><td>125450</td><td>2.00</td><td>0.50</td><td>800.0</td><td>1982</td></tr><tr><td>IBM 3081-G</td><td>3260000</td><td>16.00</td><td>11.40</td><td>26.0</td><td>1982</td></tr><tr><td>Amdahl 580-5880</td><td>7500000</td><td>16.00</td><td>24.40</td><td>24.0</td><td>1983</td></tr><tr><td>Amdahl 580-5870</td><td>5400000</td><td>16.00</td><td>22.90</td><td>24.0</td><td>1983</td></tr><tr><td>IBM 4341-2</td><td>500000</td><td>16.00</td><td>1.20</td><td>230.0</td><td>1983</td></tr><tr><td>IBM 3083-E</td><td>1120000</td><td>8.00</td><td>3.70</td><td>26.0</td><td>1983</td></tr><tr><td>IBM 3083-B</td><td>1820000</td><td>8.00</td><td>5.50</td><td>26.0</td><td>1983</td></tr><tr><td>IBM 3083-J</td><td>2420000</td><td>8.00</td><td>7.40</td><td>26.0</td><td>1983</td></tr><tr><td>Amdahl 5840</td><td>2000000</td><td>16.00</td><td>8.40</td><td>23.25</td><td>1984</td></tr><tr><td>Burroughs A9-F</td><td>613000</td><td>6.00</td><td>1.80</td><td>72.5</td><td>1984</td></tr><tr><td>IBM 8140X</td><td>60000</td><td>1.00</td><td>0.36</td><td>800.0</td><td>1984</td></tr><tr><td>IBM 3090-200</td><td>5000000</td><td>64.00</td><td>29.30</td><td>18.5</td><td>1985</td></tr></table>

\* Sources: (1) Computerworld, see [3].  
(2) Data Decisions, see [4].

This is demonstrated by the magnitude of the t-statistics for the interaction terms for type of computer and memory size, MIPS and machine cycle time. Note that the interaction terms between type of computer and year of introduction do not remain in the model because the null hypothesis, $H_{0}$ : $\beta = 0$ could not be rejected at the 95% significance level. This is significant because we cannot isolate the effect of year of introduction on system price for each type of computer. Had there been more data points, these interactions would have probably enabled the estimates.

## 4.2. Prediction of Recent Prices

Table 3 shows the predicted and actual prices of representative recently announced systems in each of the four computer categories. These systems were either introduced in 1984 or 1985, e.g., the Burroughs A9 and the IBM Sierra, or have been modified and have a new price, e.g., the DEC VAX 11/780. The predicated prices are compared with the actual prices and found to be quite close. The model may therefore be used by managers to determine whether a given system is overpriced or underpriced. Similarly, computer manufacturers may use the model as a guide for establishing prices.

## 4.3. Price Differences Between Computer Classes

Table 4 and 5 show the calculated price of representative systems, using the model, which were introduced from 1980 to 1985. For

Table 3  
Table 2  
Results of Regression Model Run on All Observations

<table><tr><td>Variable</td><td> $\beta *$ </td><td>t-Statistics</td></tr><tr><td>Constant Term</td><td>4.464311</td><td>7.95</td></tr><tr><td>Ln Memory Size</td><td>0.647844</td><td>10.29</td></tr><tr><td>Ln MIPS</td><td>0.459264</td><td>7.91</td></tr><tr><td>(Ln Memory Size)*IBM Computers</td><td>-0.341962</td><td>-3.96</td></tr><tr><td>(Ln Memory Size)*IBM PCMs</td><td>-0.565461</td><td>-5.74</td></tr><tr><td>(Ln Memory Size)*IBM Competitors</td><td>-0.503213</td><td>-7.32</td></tr><tr><td>(Ln MIPS)*IBM PCMs</td><td>0.471797</td><td>6.64</td></tr><tr><td>(Ln MIPS)*IBM Competitors</td><td>0.304642</td><td>3.69</td></tr><tr><td>(Ln Machine Cycle Time)*IBM Computers</td><td>-0.402164</td><td>-5.94</td></tr><tr><td>(Ln Machine Cycle Time)*IBM Competitors</td><td>-0.328833</td><td>-3.03</td></tr><tr><td>Effect for 1978</td><td>-0.279911</td><td>-2.55</td></tr><tr><td>Effect for 1979</td><td>-0.403549</td><td>-4.10</td></tr><tr><td>Effect for 1980</td><td>-0.364729</td><td>-3.73</td></tr><tr><td>Effect for 1981</td><td>-0.494068</td><td>-4.96</td></tr><tr><td>Effect for 1982</td><td>-0.637112</td><td>-5.55</td></tr><tr><td>Effect for 1983</td><td>-0.628923</td><td>-4.85</td></tr><tr><td>Effect for IBM Computers</td><td>7.929046</td><td>6.58</td></tr><tr><td>Effect for IBM PCM Computers</td><td>1.683099</td><td>2.09</td></tr><tr><td>Effect for IBM Competitor Computers</td><td>6.260698</td><td>3.76</td></tr><tr><td colspan="3"> $R^{2} = 0.988962$ </td></tr></table>

Degrees of Freedom = 82  
$t \geq 1.96 = 95\%$ level of confidence  
$\beta^{*}$ is the co-efficient in the regression equation for each variable. It is the amount the dependent variable changes for each unit change in the independent variable.

mainframes, a representative configuration of 8M bytes of memory, 1 MIPS and 100 nsecs machine cycle time is used. For superminis, a configuration of 1M byte of memory, 0.8 MIPS and 200 nsecs machine cycle time is used. The parameters of these systems are all within the relevant range of any of the models presented. It can be observed that in almost all formulations of the models, the effect of advancing technology is unmistakable. A system of given hardware characteristics would cost less if introduced later. Also, the prices of IBM competitors are lower than IBM's and IBM's PCM's are much lower. The reasons are analyzed in the next section.

Predicted Prices in Each Category for 1984-85 Computers Using the Model

<table><tr><td>System</td><td>Price ($)</td><td>Memory (M-Bytes)</td><td>MIPS</td><td>Machine Cycle Time (nsecs)</td><td>Predicted Price Using Fitted Model ($)</td><td>Difference (%)</td></tr><tr><td colspan="7">IBM Mainframes</td></tr><tr><td>IBM 8140</td><td>60,000</td><td>1</td><td>0.36</td><td>800.00</td><td>61,289</td><td>2.15</td></tr><tr><td>IBM 3090 Model 200 * (Sierra)</td><td>4,400,00</td><td>16</td><td>29.3</td><td>18.5</td><td>4,670,669</td><td>6</td></tr><tr><td colspan="7">IBM Plug Compatibles</td></tr><tr><td>Amdahl 5840</td><td>2,000,000</td><td>16</td><td>8.40</td><td>23.25</td><td>2,193,722</td><td>9.68</td></tr><tr><td colspan="7">IBM Competitors</td></tr><tr><td>Burroughs A9-F</td><td>613,000</td><td>6</td><td>1.8</td><td>72.5</td><td>602,698</td><td>1.68</td></tr><tr><td colspan="7">Super Minis</td></tr><tr><td>DEC 11/780</td><td>145,000</td><td>2</td><td>1.06</td><td>280.0</td><td>142,608</td><td>-1.65</td></tr></table>

\* Adjustment to Computerworld, February 18, 1985 price had to be made to bring memory size within model range.

Calculated Price of Mainframe Computers Introduced in Years 1980-1985 With 8-M Bytes of Memory Size, 1 MIPS and 100 (nsec) Machine Cycle Time

<table><tr><td rowspan="2">Year</td><td colspan="3">Calculated Price (in $)</td></tr><tr><td>IBM Computer</td><td>IBM Competitor Computer</td><td>IBM PCMs</td></tr><tr><td>1980</td><td>609,289</td><td>514,604</td><td>422,783</td></tr><tr><td>1981</td><td>535,386</td><td>452,170</td><td>371,489</td></tr><tr><td>1982</td><td>464,012</td><td>391,903</td><td>321,976</td></tr><tr><td>1983</td><td>467,827</td><td>395,125</td><td>324,623</td></tr><tr><td>1984</td><td>427,160</td><td>360,778</td><td>296,405</td></tr><tr><td>1985</td><td>376,961</td><td>318,380</td><td>261,572</td></tr></table>

For calculation method see Appendices I and II.

## 4.4. Most Important Independent Variables

In order to determine impact on price of the attributes of a computer system, a stepwise regression procedure was performed. It showed that MIPS was the single most important predictor of price, because it was the first variable found. Furthermore, it was observed that 88% of the sample variation is explained by MIPS. Next in importance as a predictor is memory size.

## 4.5. Effect of Year of introduction

The effect of year of introduction on system price across all types of computer was calculated (see Appendix I for method). In 1978 prices dropped 24%, and in 1979 dropped a further 12%. However, in 1980, the data show a slight increase of 3%. This may be due to market forces. In 1981 and 1982, the downward trend continues with drops of 12% and 13% respectively. Price for 1983 remained stable. Further, the effects for the years 1984 and 1985 were predicted (See Appendix II for method.). In 1984, the prices indicate a 9% drop in and 1985 it is about 12%. The annual drop in price is about 10%. Prices in some segments of the computer industry may, of course, be falling at a faster rate.

Calculated Price of Supermini Computers Introduced in Years 1980-1985 With 1-M Bytes Memory Size, 0.8 MIPS and 200 (nsec) Machine Cycle Time

<table><tr><td>Year</td><td>Calculated Price (in $) for Supermini Computers</td></tr><tr><td>1980</td><td>114,089</td></tr><tr><td>1981</td><td>100,247</td></tr><tr><td>1982</td><td>86,886</td></tr><tr><td>1983</td><td>87,599</td></tr><tr><td>1984</td><td>79,985</td></tr><tr><td>1985</td><td>70,585</td></tr></table>

## 5. Conclusions

The model developed to estimate computer system price, given memory size, machine cycle time, MIPS and year of introduction appears to be highly reliable, because the calculated values of $R^{2}$ and F are impressively high. Since the price is not simply the square root of speed (MIPS) it must be assumed that Grosch's law is not valid, even within different computer classes, as some have suggested.

Interestingly though, the parameter having the greatest effect on price is the speed in MIPS of the system. Thus, although the concept of how fast a system processes instructions is often thought of as being only partially related to overall system throughput, the system's speed in MIPS is still very significant as a price determinant. As expected, memory size is also an important predictor of price, which is consistent with the fact that it is the most expensive single component of a computer system.

The pricing strategies within the different classes of computers is rather interesting. For a computer system with the same hypothetical attributes, the IBM PCMs are priced significantly lower (23%) than the equivalent IBM systems. This is because the only reason for customers to buy a PCM is price. It is their Raison d'etre. On the other hand, IBM competitor prices are only about 6% lower than IBMs'. This can be explained by the fact that customers are generally locked into a vendor, so pricing is less important, whereas IBM has far greater economies of scale than its competitors. Since the late 1970s, IBM has been forced to cut prices drastically because of the plug-compatible competition. Its current emphasis is on getting new technology into production quickly, driving for volume, with slimmer margins [14]. IBM's competitors do not have a plug-compatible threat, nor the resources to reduce prices and increase volume. Their prices are therefore not as far below IBM's as those of the PCMs.

The model, as expected, confirms the widely held belief that the effect of advancing computer technology has been to reduce system price over time. This is true for all classes of machines, although the magnitude of the effect for individual types of computers could not be estimated, owing to the absence of the appropriate interaction terms in the regression model, caused by insufficient data within the required classifications.

Finally, the chief contribution of the model is probably that it provides a method of price/performance comparisons amongst computers better than those previously available. This should be useful to both purchasers of computer systems as well as their manufacturers for determining price competitiveness. The continued availability of “standardized” price/performance data in Computerworld would therefore be valuable.

## Appendix I

The change in prices pertaining to Table 2 were computed as follows. The model is formulated as:

$$
\begin{array}{r l} \text { Ln   Price } & = \beta_ {0} + \beta_ {1} (\text { Ln   Memory }) + \beta_ {2} (\text { Ln   MIPS }) \\ & + \beta_ {3} (\text { Ln   Machine   Cycle   Time }) \\ & + \beta_ {4} (\text { Ln   Memory }) D _ {7} + \dots \\ & + \beta_ {1 2} (\text { Ln   Machine   Cycle   Time }) D _ {9} \\ & + \beta_ {1 3} D _ {1} + \beta_ {1 4} D _ {2} + \dots + \beta_ {2 2} D _ {9} \\ & + \beta_ {2 3} D _ {2} D _ {7} + \beta_ {2 4} D _ {1} D _ {8} + \dots \end{array}
$$

To observe the effect on price due to the year of introduction for identical configurations:

$$
\begin{array}{r l} \text { Ln   Price } & = \text { CN } + \beta_ {4} (\text { Ln   Memory }) D _ {7} + \dots \\ & + \beta_ {1 2} (\text { Ln   Machine   Cycle   Time }) D _ {9} \\ & + \beta_ {1 3} D _ {1} + \beta_ {1 4} D _ {2} + \dots \beta_ {2 2} D _ {9} \\ & + \beta_ {2 3} D _ {1} D _ {7} + \beta_ {2 4} D _ {1} D _ {8} + \dots \end{array}
$$

where $CN = \beta_{0} + \beta_{1}(Ln\ Memory) + \beta_{2}(Ln\ MIPS) + \beta_{3}(Ln\ Machine\ Cycle\ Time)$ , e.g., to observe the change in price due to the years 1981 to 1982 for IBM Computers (see Table 2): For 1981:

$$
\begin{array}{r l} \text { Ln   Price } & = 4. 4 6 4 3 1 1 + (0. 6 4 7 8 4 4) (\text { Ln   Memory }) \\ & + (0. 4 5 9 2 6 4) (\text { Ln   MIPS }) \\ & - 0. 3 4 1 9 6 2 (\text { Ln   Memory }) \end{array}
$$

$$
\begin{array}{l} - 0. 4 0 2 1 6 4 (\text { Ln   Machine   Cycle   Time }) \\ + 7. 9 2 9 0 4 6 - 0. 4 9 4 0 6 8, \end{array}
$$

$$
\begin{array}{r l} \text { Ln   Price } & = \text { CN } - 0. 3 4 1 9 6 2 (\text { Ln   Memory }) \\ & - 0. 4 0 2 1 6 4 (\text { Ln   Machine   Cycle   Time }) \\ & + 7. 9 2 9 0 4 6 - 0. 4 9 4 0 6 8, \end{array}
$$

where

$$
\begin{array}{r l} \mathrm{CONT} & = \mathrm{CN} - 0. 3 4 1 9 6 2 (\mathrm{LnMemory}) \\ & - 0. 4 0 2 1 6 4 (\mathrm{LnMachineCycleTime}) \\ & + 7. 9 2 9 0 4 6, \end{array}
$$

$$
\text { Price } = \exp \text {   CONT   } - 0. 4 9 4 0 6 8
$$

For 1982:

$$
\mathrm{Ln} \quad \text { Price } = \mathrm{CONT} - 0. 6 3 7 1 1 2,
$$

$$
\frac {\text { Price in 1982}}{\text { Price in 1981 }} \times 100 = \exp (- 0.143044) = 86.67 \%
$$

Decline in price in 1982 as compared to 1981 will be 13.33%.

## Appendix II

The model developed was:

$$
\begin{array}{l} X _ {t} = \alpha_ {0} + \alpha_ {1} t + \xi_ {t}, t = 1, 2, 3, \dots \\ \xi_ {t} = \phi_ {1} \xi_ {t - 1} + \mu_ {2} \xi_ {t - 2} + \eta_ {t} \end{array}
$$

where $X_{t}=$ the effect for the year t and t=1 implies the year 1978 and so on. $\eta_{t}$ is normally distributed with zero mean and finite variance.

The results obtained are given in Table A.

To calculate the effect for the year 1984, we should find $\hat{\xi}_5$ and $\hat{\xi}_6$ .

$$
\begin{array}{l} \hat {\xi} _ {5} = x _ {5} - \left\{- 0. 1 9 3 6 2 1 - (0. 0 7 7 5 0 6) (5) \right\}, \\ \hat {\xi} _ {5} = - 0. 0 5 6 2 1 9 9 \end{array}
$$

and

$$
\begin{array}{l} \hat {\xi} _ {6} = x _ {6} - \left\{0. 1 9 3 6 2 1 - (0. 7 7 5 0 6) (6) \right\}, \\ \hat {\xi} _ {6} = - 0. 0 2 9 7 3 4. \end{array}
$$

Table A

<table><tr><td>Parameter</td><td>Estimated Values</td><td>t-Statistics</td></tr><tr><td> $\alpha_0$ </td><td>-0.193621</td><td>-8.53</td></tr><tr><td> $\alpha_1$ </td><td>-0.077506</td><td>-12.721</td></tr><tr><td> $\mu_1$ </td><td>-0.705357</td><td>-2.3079</td></tr><tr><td> $\phi_2$ </td><td>-0.662994</td><td>-2.1693</td></tr><tr><td> $R^2 = 0.9878$ </td><td></td><td></td></tr></table>

Now

$$
\hat {\xi} _ {7} = \phi_ {1} \hat {\xi} _ {6} + \phi_ {2} \hat {\xi} _ {5}
$$

$$
\hat {\xi} _ {7} = 0. 1 6 3 0 0 4
$$

Now using $\hat{x}_t = \alpha_0 + \alpha_1 t + \xi_t$ ,

$$
\hat {x} _ {7} = - 0. 1 9 3 6 2 1 - (0. 0 7 7 5 0 6) (7) + 0. 0 1 6 3 0 0 4
$$

$$
\hat {x} _ {7} = - 0. 7 1 9 8 6 3
$$

Similarly, the effect for the year 1985 is determined as -0.84480.

## References

[1] Booth, G. "Distributed Data Processing: It's a Question of Experience." Datamation, Vol. 22, No. 9, September 1976, pp. 160–2.

[2] Cale, E.G., Gremillion, L.L., and McKenney, J.L. "Price/Performance Patterns of U.S. Computer Systems." CAMC, Vol. 22, No. 4, April, 1979, pp. 225-232.

[3] Computerworld: The following issues:
Vol. XIV, No. 47, Nov. 17, 1980, p. 1.
Vol. XIV, No. 48, Nov. 24, 1980, p. 1.
Vol. XV, No. 28, July 13, 1981, pp. 12–18.
Vol. XV, No. 29, July 20, 1981, p. 4.
vol. XVI, No. 14, April 5, 1982, p. 4.
Vol. XVI, No. 17, April 26, 1982, p. 4.

Vol. XVI, No. 36, Sept. 13, 1982, p. 6.

Vol. XVI, No. 41, Oct. 11, 1982, p. 5.

Vol. XVI, No. 43, Oct. 25, 1982, p. 4.

Vol. XVIII, No. 34, Aug. 20, 1984, pp. 23–40.

Vol. XIX, No. 7, Feb. 18, 1985, p. 4.

[4] Data Decisions, Computer Systems, Ziff Davis Publishing, Vol. 2 and 3, 1983.

[5] Draper, N. and Smith, H. Applied Regression Analysis. John Wiley and Sons, New York, 1966.

[6] Dutta, M. Econometric Methods. Southwestern, 1975, p. 150.

[7] Freund, R.J. and Littell, R. SAS for Linear Models: A Guide to the ANOVA and GLM Procedures. SAS Institute, Inc., North Caroline, 1981.

[8] Graybill, F.A. Theory and Application of the Linear Model. North Scituate, Massachusetts, 1976.

[9] Grosch, H.A. "High Speed Arithmetic: The Digital Computer as a Research Tool." Jr. Opt. Soc. America, Vol. 43, No. 4, 1953.

[10] Grosch, H.A. "Grosch's Law Revisited." Computerworld, Vol. 8, No. 16, 1975, p. 24.

[11] Hayes, R.H. "Europe's Computer Industry: Closer to the Brink." Columbia Journal of Business, Vol. IX, No. 2, 1974, pp. 115–120.

[12] Klein, L.R. An Introduction to Econometrics. Prentice Hall, New York, 1962, pp. 64, 101.

[13] Knight, K.E. "Changes in Computer Performance." Datamation. Vol. 12, No. 9, 1966, pp. 40–54.

[14] Magnet, M. "How to Compete with IBM." Fortune, February 6, 1984, pp. 58–71.
