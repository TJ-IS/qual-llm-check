---
otero_id: 23631
otero_key: "5FHP7TJ8"
title: "Strategic choice and data envelopment analysis: comparing computers across many attributes"
authors: "John Doyle; Rodney Green"
year: "1994"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1994.7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Strategic choice and data envelopment analysis: comparing computers across many attributes

JOHN DOYLE and RODNEY GREEN
School of Management, University of Bath BA7 2AY, UK

A linear programming approach (Data Envelopment Analysis) is described to determine the relative merits of a set of multi-input, multi-output systems, in which more output for less input is considered good. The method is applied to benchmarks of microcomputers, and is contrasted with a multiple regression analysis of the same data. It is also argued that the essence of two opposing strategic outlooks can be captured within the method.

## Introduction

A few years ago the received wisdom in strategic management was that companies should compete primarily either on price, or quality, or service, or innovation; but not on more than one. To compete across a wider range of attributes, the orthodoxy stated, was to dangerously risk losing focus. Porter (1980) described such a lack of focus as 'piggy in the middle'. However, the counter-argument can be heard increasingly often today: that companies must be prepared to compete on combinations of price and quality and service and innovation.

The textbooks talk about finding your competitive niche or area of ‘distinctive competency’. Perhaps your company is the cost leader in the industry. Then, the book will say, you should expect your quality to be somewhat lower, your response time a bit slower, and your flexibility less. If you get the product out the door faster than everybody else, then your quality is unlikely to be as good and your costs are higher, so charge more.

Now we know that all this is balderdash. The best manufacturers of the world are likely to be good in all those areas.

(Schonberger, 1986, p. 204)

Paradoxically, the increasingly demanding customer may also find it more difficult to determine, amongst these multi-attribute offerings, what (for them) is the best buy.

We do not intend to arbitrate between these opposing views, but given such a shift in emphasis it is essential that managers should at least have the analytical tools to be able to manage this multi-objective outlook, and this means in turn that decision support systems should have models which are adequate to the task. A dominant decision support model, or family of models, can act as a constraining force. Implicit assumptions which come with the technique can limit the questions which are considered worth asking of data, in much the same way that dominant scientific paradigms have been said to constrain science in general (Kuhn, 1962), and similarly for technological paradigms (Dosi, 1982). Multiple regression analysis is one such model.

In this article we present an application of linear programming called Data Envelopment Analysis (DEA), which has been used extensively in the analysis of not-for-profit organizations (Silkman, 1986). Although DEA has been applied outside of its original domain of application and even within the computing industry (Banker and Kemerer, 1989; Banker et al., 1991) it is relatively new to apply DEA to the analysis of product data (Doyle and Green, 1991). In so doing we open up a much wider domain of application for DEA. Furthermore, as will be shown, two different forms of Data Envelopment Analysis capture the aspirations of the two strategic outlooks described above.

We take data which has already been analysed in one of the most respected and widely read computer journals (The Communications of the ACM – henceforth CACM), and show what different questions could have been asked and answered of the data using DEA.

## Computer performance benchmarks

## The multiple regression perspective

Over the past ten years or so the CACM has carried a number of articles investigating the relationship between the price of a computer and its performance (Cale et al., 1979; Ein-Dor, 1985; Sircar and Dave, 1986; Ein-Dor and Feldmesser, 1987; Kang, 1989; Lynch et al., 1990) to list but some of them. All these studies make use of multiple regression analysis, in which the cost of a machine (the one dependent variable) is explained as a function of its performance attributes (the many independent variables).

Those who do use multiple regression on such data seem to be addressing one of four possible issues.

(1) To help the computer manufacturer in determining the price to be put on a new machine.

(2) To determine the variables that most affect cost of a computer.

(3) To determine whether Grosch's Law (economies of scale exist) still is true, or if it ever was.

(4) To determine what the future trends in price and/or performance of computers may be. This analysis requires time as one of the independent variables.

For goals 1–4 a ‘successful’ outcome is when most of the variation in the dependent variable (cost) is explained, which occurs when the $R^{2}$ statistic gets closer to the value 1, or, to put it another way, when the residuals become as small as possible. The implicit assumption, that residuals are undesirable, acts as a constraint on what you get out of your data.

It is easy to allow the sub-goal of maximizing $R^{2}$ to dominate the analysis, by adding more independent variables than the number of observations warrants and transforming the raw data in highly artificial ways. RAM, for instance, is approximately an additive cost to the manufacturer since it nowadays amounts to the number of chips that are plugged into a card. There seems to be no justification for subjecting it to logarithmic transformations, other than to increase $R^{2}$ .

Let us step back and ask why we do these analyses. To whom are they useful? First of all, to every manufacturer there are thousands, sometimes millions of customers. So it is necessarily a minority of people who would be interested in goal (1). Goal (2) seems of most interest to economists, but of limited practical benefit to the manager. Goal (3) is oriented towards the decision whether to buy distributed or centralized processing. Finally, goal (4) is potentially of interest to a wider audience, though few studies actually have time (year the machine appeared) as a factor.

## The data envelopment perspective

If we look at where much of the data comes from we begin to see what the majority audience actually is.

Increasingly, the data are drawn from computer magazines which typically have benchmarked a clutch of machines with the aim of informing the reader which are the best ones. The way that this is done is the reviewer's particular art, which at best might be based on an average over the performance criteria, and at worst may be entirely ad hoc.

In this article we present a method of analysing price/performance data, using a technique based on linear programming, known as Data Envelopment Analysis (DEA). Initially, at least, the technique concentrates on determining which machines are particularly good in some way (100% 'efficient' in the jargon). The 'efficiency' of the other machines is measured relative to the set of 100% efficient machines, which are said to stake out the 'efficiency frontier' – terms which will be defined more rigorously below.

Thus we go back to the original purpose for which the data was collected. This is not a complete rejection of goals 1–4, because many of the same issues re-emerge in a different light using DEA, and many new insights emerge. For instance, which machines should be compared with which (i.e. who, as a manufacturer, are your competitors?). How best to improve the specification of your machine. Or, whether the machine should best aim to fill a gap in a particular niche of the market (and what that niche might consist of), or whether it should compete squarely in the middle of the market. It will be immediately appreciated from these examples that DEA helps to inform questions that a manager might pose, rather than questions that an economist might pose.

To show how DEA works we shall first present a simple worked example. We then use DEA on some data already published in CACM, but which was analysed to fulfill goal 2 above. We shall see that DEA is powerful in that incisive recommendations seem to arise naturally out of the analysis, which was not the case when analysed by standard multiple regression. We conclude by comparing DEA with multiple regression, and by setting DEA in a broader context. DEA, like multiple regression, is not confined to computing applications.

## DEA's origins

Data Envelopment Analysis originated as an accounting tool in the analysis of not-for-profit organizations (Charnes et al., 1978). Let us take a university computing department as an example. When we come to examine which of a set of computing departments is best we are usually faced with a problem. It is this: there are a number of different measures of excellence we could take. For instance, one department may point to the number of undergraduates it processes. Another might cite the number of successful candidates for higher degrees. Another might point to the number of refereed publications it produces. Yet another, seeing itself in a support role, might prefer you to focus on the number of users it supports in the rest of the university. In the jargon of DEA any, or all, of these are outputs from the computing departments.

But of course, all other things being equal a big department is going to produce more of all the above, so we want some size dividing factor. But what should it be? In a similar manner to the outputs we can identify a number of inputs into the department. The combined academic staff salaries would be one; the capital equipment budget would be another; research funding would be yet another. Each of these could be taken as a potential dividing factor.

The most general measure of the efficiency with which any given department transforms its inputs into its outputs is a weighted sum of its outputs divided by a weighted sum of its inputs thus:

$$
h _ {\mathrm{k}} = \frac {\sum_ {y = 1} ^ {s} v _ {\mathrm{ky}} \cdot O _ {\mathrm{ky}}}{\sum_ {x = 1} ^ {r} u _ {\mathrm{kx}} \cdot I _ {\mathrm{kx}}}
$$

where $h_{K}=$ efficiency of department k, $I_{kx}=$ amount of input x for department k, $O_{ky}=$ amount of output y for department k, $u_{kx}=$ weight attached to input x, $v_{ky}=$ weight attached to output y, r=number of inputs, s=number of outputs, and n=the number of departments.

It is natural to expect each department to want to choose weights to optimize its own efficiency as defined here. But for 100% efficiency to mean anything at all, we need the additional constraint that no other department using department k's weights should have an efficiency greater than 100%. That is:

$$
\frac {\sum_ {y = 1} ^ {s} v _ {\mathrm{ky}} \cdot O _ {\mathrm{iy}}}{\sum_ {x = 1} ^ {r} u _ {\mathrm{kx}} \cdot I _ {\mathrm{ix}}} \leqslant 1 \quad \text { for } i = 1, 2,.. k,.. n
$$

These two expressions can be re-written as a straightforward linear program, which can be solved on a computer, giving department k the most favourable weights possible:

Maximize:

$$
h _ {\mathrm{k}} = v _ {\mathrm{ky}} \cdot O _ {\mathrm{ky}}
$$

subject to:

$$
u _ {\mathrm{kx}} \cdot I _ {\mathrm{kx}} = 1
$$

and:

$$
\begin{array}{r l} (v _ {\mathrm{ky}} \cdot O _ {\mathrm{iy}}) - (u _ {\mathrm{kx}} \cdot I _ {\mathrm{ix}}) & \leqslant 0 \\ & \text { for } i = 1, 2,.. k,.. n \end{array}
$$

Also:

$$
\begin{array}{c} u _ {\mathrm{kx}} \geqslant 0 \\ \text { and } v _ {\mathrm{ky}} \geqslant 0 \end{array}
$$

for all $k, x$ , and $y$

Similar linear programs can be established for each of the remaining n - 1 departments.

## DEA and microcomputers: an example

A Data Envelopment Analysis of a collection of computing departments is no doubt a worthy undertaking in its own right, but this kind of analysis has been written up many times already (Tomkins and Green, 1988). It is our intention to use DEA in a new way, in order to analyse the performance of microcomputers.

If we look at Figure 1, we see that any multi-input, multi-output system (not just non-profit making organizations) are potential candidates for DEA. In particular, we could consider the purchase of a microcomputer as such a system. The critical conceptual link is to conceive of a microcomputer (or any product for that matter Bromwich, 1990; Doyle and Green, 1991) as a bundle of features; the features are modelled as the microcomputer's DEA-outputs (not to be confused with output in the traditional computing sense).

![](/api/attachments/5FHP7TJ8/fulltext/images/67e0345083b6f8fa85b5101ee2dfc7372547ed58ea56445dc3d38951e3790e25.jpg)  
Figure 1 Possible inputs and outputs for a university computing department treated as a ‘black box’

As a simple example, let us consider a one-input, two-output analysis, in which the one input (cost) is the price of the machine in dollars, and the outputs (benefits) are memory size and disk size, as in Table 1. The most efficient microcomputers are those which transform lower costs into greater benefits (better features).

The graph of $O_{1}/I$ vs. $O_{2}/I$ in Figure 2 shows that machine A is worse than machines E and D on both dimensions. So one would have little trouble in deciding that E and D are a better buy than machine A. Machine B is not quite so simple, since it beats machine C on the first ratio, but not on the second, whereas it beats machine E on the second ratio, but not on the first.

However, it will be clear that the most efficient machines are upwards and rightward in Figure 2. Machines C, E, and D mark out what is known as the efficiency frontier. The linear program considers machines C, E, and D to be 100% efficient. The efficiency of machine B is measured relative to a pseudo machine B' which is the projection of OB onto the line CE. Machine B' is a linear combination of machines C and E. The efficiency of B is the ratio OB/OB', and similarly, the efficiency of machine A is found by projecting onto ED.

Machines C and E are B's reference set, whereas A has E and D as its reference set.

## Analysis

Almost any set of benchmarks would do to demonstrate the technique, but we have turned to a study by Sircar and

Table 1 Hypothetical one-input, two-output case for five machines

<table><tr><td rowspan="2">Machine</td><td>Cost (dollars)</td><td>RAM (Kb)</td><td>Disk (Mb)</td><td></td><td></td><td rowspan="2">Efficiency (%)</td></tr><tr><td>I</td><td> $O_1$ </td><td> $O_2$ </td><td> $O_1/I$ </td><td> $O_2/I$ </td></tr><tr><td>A</td><td>2000</td><td>640</td><td>40</td><td>0.32</td><td>0.020</td><td>53.8</td></tr><tr><td>B</td><td>1800</td><td>512</td><td>90</td><td>0.28</td><td>0.050</td><td>87.5</td></tr><tr><td>C</td><td>1900</td><td>378</td><td>120</td><td>0.20</td><td>0.063</td><td>100.0</td></tr><tr><td>D</td><td>1500</td><td>1024</td><td>40</td><td>0.68</td><td>0.027</td><td>100.0</td></tr><tr><td>E</td><td>1300</td><td>640</td><td>64</td><td>0.49</td><td>0.049</td><td>100.0</td></tr></table>

![](/api/attachments/5FHP7TJ8/fulltext/images/a88dd36a1fbd8f3febddb886e17a565b052ff483f5bc60de2a2114d9e1e0df3c.jpg)  
Figure 2 Graphical representation of DEA

Dave (1986). This re-analysis of their data makes a good contrast between what is (not) revealed using multiple regression analysis and what is revealed using DEA. Furthermore, this particular paper can be used to represent an ongoing series of papers published over a dozen years or more to the present day. Since they have been published in one of the best and most widely-read computing journals in the world, the topic and approach represented by Sircar and Dave cannot be considered parochial. Finally, although the data are historic in computing terms (mid 1980s), they have the distinct advantage over current data in that we know what happened next.

Sircar and Dave's original data (their Table III) are reproduced in our Table 2. We decided to ignore the three 'Real-life' applications for two reasons. First, they do not exercise independent functions of the system, but must be a reflection of some unknown combination of the other four measures. Second, we shall see that DEA yields prescriptive information, telling how each machine might most rapidly increase its efficiency. To an engineer put in charge of such a task the first four measures have a meaning, whereas the ‘real-life’ applications do not.

Hence we are left with the following four output measures:

(1) Memory size

(2) Disk size

(3) CPU speed (from CPU intensive application)

(4) Disk access speed (from I/O intensive application)

The one input considered appropriate here was dollar cost.

We see from Table 3 that five of the twenty-two machines are 100% efficient (machines 4, 5, 9, 10, and 11). It may come as some surprise that the IBM-PC (at that particular point in time) was right up there with the leaders. Contrary to a currently popular version of history, marketing muscle was not the only reason for the success of the IBM-PC: it was clearly good value for money. As we shall see below, it was also good all-round value for money.

Another point that might strike the reader is the large spread of efficiencies (going down to 29% in the case of the DEC Station 78). According to DEA not all machines are exemplars of a highly predictive cost function; some machines were just rotten value!

Reference sets and associated duals are shown in Tables 4 and 5. Recall that for a non-efficient machine, efficiency was measured relative to a linear combination of a number of machines on the efficiency horizon (its reference set). This can be conceived of as a pseudo-machine. The duals are the coefficients which enable the characteristics of the pseudo-machine to be determined.

We can distinguish two kinds of 100% efficient machines. On the one hand there are those machines which achieve 100% efficiency by giving value for money on a narrow range of features (for instance, they might have fastest disk access, but be rather pedestrian on all other features). Such machines inhabit a technical niche in the competitive world of business.

On the other hand there are machines that compete in the same way that most other machines do, and achieve efficiency by giving value for money across a broad range of features (though perhaps not the best on any one in particular). This is the good all-rounder.

Table 2 System attributes and benchmark performance (Sircar and Dave, 1986)

<table><tr><td>System</td><td>Price(£)</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr><tr><td>1 IBM 5120</td><td>13,705</td><td>32</td><td>2800</td><td>48.0</td><td>163.3</td><td>2129.7</td><td>25.0</td><td>256.2</td></tr><tr><td>2 SD System SD-200</td><td>12,300</td><td>64</td><td>2000</td><td>20.4</td><td>75.0</td><td>1062.8</td><td>10.5</td><td>376.2</td></tr><tr><td>3 NEC Astra 205</td><td>11,950</td><td>128</td><td>2400</td><td>353.3</td><td>432.5</td><td>1218.8</td><td>512.3</td><td>1586.2</td></tr><tr><td>4 Altos ACS 8000-15</td><td>9875</td><td>208</td><td>1000</td><td>188.4</td><td>159.2</td><td>474.5</td><td>150.6</td><td>641.5</td></tr><tr><td>5 WANG 2200 SVP</td><td>14,600</td><td>32</td><td>3000</td><td>4.5</td><td>10.6</td><td>133.3</td><td>70.6</td><td>143.3</td></tr><tr><td>6 Dynabyte 5300</td><td>8535</td><td>64</td><td>1000</td><td>117.3</td><td>168.5</td><td>463.7</td><td>142.2</td><td>661.5</td></tr><tr><td>7 Billings BC 12 DF-2M</td><td>12,395</td><td>64</td><td>2000</td><td>24.3</td><td>115.1</td><td>1308.6</td><td>14.2</td><td>309.2</td></tr><tr><td>8 Commodore CBM 8032</td><td>4085</td><td>32</td><td>1000</td><td>35.9</td><td>67.8</td><td>1425.1</td><td>20.0</td><td>216.6</td></tr><tr><td>9 Smoke Signal Cheiftian</td><td>8149</td><td>56</td><td>1000</td><td>7.4</td><td>93.7</td><td>193.3</td><td>5.7</td><td>100.7</td></tr><tr><td>101 Vectyor Graphic 3005</td><td>11,150</td><td>56</td><td>5800</td><td>13.6</td><td>41.3</td><td>694.1</td><td>13.1</td><td>465.6</td></tr><tr><td>11 IBM Personal Computer</td><td>4550</td><td>64</td><td>320</td><td>20.3</td><td>59.4</td><td>1049.6</td><td>15.6</td><td>561.8</td></tr><tr><td>12 Xerox 820</td><td>7220</td><td>64</td><td>480</td><td>28.4</td><td>68.3</td><td>1477.0</td><td>10.6</td><td>330.1</td></tr><tr><td>13 TI 771</td><td>10,195</td><td>64</td><td>502</td><td>28.2</td><td>48.7</td><td>1325.4</td><td>14.2</td><td>218.1</td></tr><tr><td>14 North Star Horizon</td><td>6911</td><td>64</td><td>1400</td><td>15.0</td><td>52.8</td><td>721.9</td><td>11.7</td><td>117.7</td></tr><tr><td>15 Cromemco System 2</td><td>9275</td><td>64</td><td>350</td><td>27.2</td><td>66.3</td><td>892.6</td><td>10.0</td><td>168.0</td></tr><tr><td>16 Vector Graphic Sys B</td><td>7750</td><td>64</td><td>630</td><td>22.9</td><td>127.7</td><td>1170.0</td><td>18.3</td><td>356.5</td></tr><tr><td>17 DEC Station 78</td><td>14,295</td><td>32</td><td>1024</td><td>48.3</td><td>57.4</td><td>1335.6</td><td>63.7</td><td>304.8</td></tr><tr><td>18 Radio Shack TRS 80</td><td>7648</td><td>64</td><td>1527</td><td>27.3</td><td>131.8</td><td>1200.7</td><td>14.1</td><td>218.6</td></tr><tr><td>19 Apple II Plus</td><td>4270</td><td>48</td><td>270</td><td>31.6</td><td>89.6</td><td>1271.0</td><td>15.1</td><td>377.4</td></tr><tr><td>20 Digital Micro Sys DSC-2</td><td>9085</td><td>64</td><td>2270</td><td>35.9</td><td>127.6</td><td>828.2</td><td>56.6</td><td>269.9</td></tr><tr><td>21 Ohio Scientific C3-A</td><td>10,440</td><td>48</td><td>600</td><td>17.9</td><td>74.6</td><td>730.7</td><td>11.9</td><td>943.3</td></tr><tr><td>22 Alpha Micro</td><td>15,605</td><td>64</td><td>2400</td><td>8.1</td><td>40.7</td><td>323.9</td><td>10.5</td><td>205.3</td></tr></table>

Note: A = Memory size (Kb), B = Disk size (Mb), C = CPU intensive application, D = I/O intensive application, E = Real life application 1, F = Real life application 2, G = Real life application 3.

Table 3 Efficiencies for the 22 microcomputers

<table><tr><td>4</td><td>Altos ACS 8000-15</td><td>1.000</td></tr><tr><td>5</td><td>WANG 2200 SVP</td><td>1.000</td></tr><tr><td>9</td><td>Smoke Signal Chieftain</td><td>1.000</td></tr><tr><td>10</td><td>Vector Graphic 3005</td><td>1.000</td></tr><tr><td>11</td><td>IBM Personal Computer</td><td>1.000</td></tr><tr><td>8</td><td>Commodore CBM 8032</td><td>0.951</td></tr><tr><td>14</td><td>North Star Horizon</td><td>0.925</td></tr><tr><td>19</td><td>Apple II Plus</td><td>0.773</td></tr><tr><td>3</td><td>NEC Astra 205</td><td>0.738</td></tr><tr><td>18</td><td>Radio Shack TRS 80</td><td>0.721</td></tr><tr><td>20</td><td>Digitl Micro Sys DSC-2</td><td>0.668</td></tr><tr><td>12</td><td>Xerox 820</td><td>0.625</td></tr><tr><td>22</td><td>Alpha Micro</td><td>0.623</td></tr><tr><td>16</td><td>Vector Graphic Sys B</td><td>0.609</td></tr><tr><td>2</td><td>SD System SD-200</td><td>0.523</td></tr><tr><td>13</td><td>TI 771</td><td>0·505</td></tr><tr><td>7</td><td>Billings BC 12 DF-2M</td><td>0.499</td></tr><tr><td>6</td><td>Dynabyte 5300</td><td>0.494</td></tr><tr><td>15</td><td>Cromemco System 2</td><td>0.475</td></tr><tr><td>21</td><td>Ohio Scientific C3-A</td><td>0.434</td></tr><tr><td>1</td><td>IBM 5120</td><td>0.407</td></tr><tr><td>17</td><td>DEC Station 78</td><td>0.294</td></tr></table>

Table 4 Reference sets

<table><tr><td>1</td><td>IBM 5120</td><td>4</td><td>10</td><td></td></tr><tr><td>2</td><td>SD System SD-200</td><td>4</td><td>10</td><td>11</td></tr><tr><td>3</td><td>NEC Astra 205</td><td>4</td><td>10</td><td></td></tr><tr><td>4</td><td>Altos ACS 8000-15</td><td>4</td><td></td><td></td></tr><tr><td>5</td><td>WANG 2200 SVP</td><td>5</td><td></td><td></td></tr><tr><td>6</td><td>Dynabyte 5300</td><td>4</td><td>10</td><td>11</td></tr><tr><td>7</td><td>Billings BC 12 DF-2M</td><td>4</td><td>10</td><td>11</td></tr><tr><td>8</td><td>Commmodore CBM 8032</td><td>5</td><td>10</td><td>11</td></tr><tr><td>9</td><td>Smoke Signal Chieftain</td><td>9</td><td></td><td></td></tr><tr><td>10</td><td>Vector Graphic 3005</td><td>10</td><td></td><td></td></tr><tr><td>11</td><td>IBM Personal Computer</td><td>11</td><td></td><td></td></tr><tr><td>12</td><td>Xerox 820</td><td>4</td><td>10</td><td>11</td></tr><tr><td>13</td><td>TI 771</td><td>5</td><td>10</td><td>11</td></tr><tr><td>14</td><td>North Star Horizon</td><td>5</td><td>9</td><td>10</td></tr><tr><td>15</td><td>Cromemco System 2</td><td>4</td><td>10</td><td>11</td></tr><tr><td>16</td><td>Vector Graphic Sys B</td><td>4</td><td>10</td><td>11</td></tr><tr><td>17</td><td>DEC Station 78</td><td>5</td><td>10</td><td>11</td></tr><tr><td>18</td><td>Radio Shack TRS 80</td><td>4</td><td>10</td><td>11</td></tr><tr><td>19</td><td>Apple II Plus</td><td>4</td><td>10</td><td>11</td></tr><tr><td>20</td><td>Digtl Micro Sys DSC-2</td><td>4</td><td>10</td><td>11</td></tr><tr><td>21</td><td>Ohio Scientific C3-A</td><td>5</td><td>9</td><td>10</td></tr><tr><td>22</td><td>Alpha Micro</td><td>5</td><td>9</td><td>10</td></tr></table>

Table 5 Reference sets and associated duals (in brackets) for each machine

<table><tr><td colspan="5">Machine number</td></tr><tr><td>1</td><td>4 (0.025)</td><td>10 (0.478)</td><td></td><td></td></tr><tr><td>2</td><td>4 (0.061)</td><td>10 (0.305)</td><td>11 (0.534)</td><td></td></tr><tr><td>3</td><td>4 (0.529)</td><td>10 (0.323)</td><td></td><td></td></tr><tr><td>4</td><td>4 (1.000)</td><td></td><td></td><td></td></tr><tr><td>5</td><td>5 (1.000)</td><td></td><td></td><td></td></tr><tr><td>6</td><td>4 (0.250)</td><td>10 (0.125)</td><td>11 (0.080)</td><td></td></tr><tr><td>7</td><td>4 (0.112)</td><td>10 (0.305)</td><td>11 (0.368)</td><td></td></tr><tr><td>8</td><td>5 (0.060)</td><td>10 (0.121)</td><td>11 (0.364)</td><td></td></tr><tr><td>9</td><td>9 (1.000)</td><td></td><td></td><td></td></tr><tr><td>10</td><td>10 (1.000)</td><td></td><td></td><td></td></tr><tr><td>11</td><td>11 (1.000)</td><td></td><td></td><td></td></tr><tr><td>12</td><td>4 (0.051)</td><td>10 (0.029)</td><td>11 (0.808)</td><td></td></tr><tr><td>13</td><td>5 (0.042)</td><td>10 (0.011)</td><td>11 (0.969)</td><td></td></tr><tr><td>14</td><td>5 (0.010)</td><td>9 (0.109)</td><td>10 (0.176)</td><td>11 (0.745)</td></tr><tr><td>15</td><td>4 (0.037)</td><td>10 (0.006)</td><td>11 (0.874)</td><td></td></tr><tr><td>16</td><td>4 (0.047)</td><td>10 (0.057)</td><td>11 (0.797)</td><td></td></tr><tr><td>17</td><td>5 (0.093)</td><td>10 (0.109)</td><td>11 (0.358)</td><td></td></tr><tr><td>18</td><td>4 (0.125)</td><td>10 (0.220)</td><td>11 (0.402)</td><td></td></tr><tr><td>19</td><td>4 (0.031)</td><td>10 (0.006)</td><td>11 (0.643)</td><td></td></tr><tr><td>20</td><td>4 (0.208)</td><td>10 (0.355)</td><td>11 (0.014)</td><td></td></tr><tr><td>21</td><td>5 (0.013)</td><td>9 (0.166)</td><td>10 (0.037)</td><td>11 (0.566)</td></tr><tr><td>22</td><td>5 (0.086)</td><td>9 (0.534)</td><td>10 (0.263)</td><td>11 (0.260)</td></tr></table>

There are two ways we can distinguish between the technical-niche and the all-round machine, or what we might call the focus dimension. The first way is to go through each of the 100% efficient machines and count the number of times that it appears in the reference sets of the non-100%-efficient machine. A technical-niche machine will rarely appear in other machines' reference sets. The all-round machine will appear frequently in other machines' reference sets. When we do this we find the ordering, with all-rounders listed first, are machine numbers: 10 (Vector Graphics 3005), 11 (IBM PC), 4 (Altos), 5 (WANG), and 9 (Smoke Signal Chieftain). The number of times these appear in other reference sets are: 17, 15, 11, 6, 3 respectively.

The second approach starts by calculating what are known as the cross-efficiencies. To calculate the cross-efficiencies for machine X one calculates its efficiency using not its own preferred weights now, but each of the other machines' preferred weights in turn. Thus one ends up, in our case, with a $22 \times 22$ matrix of cross efficiencies (i.e. 22 cross-efficiencies for 22 machines). We can see now that our initial calculations of efficiency are just the special cases of cross-efficiencies found on the leading diagonal (machine X rated on machine X's best weights). Cross-efficiency is a kind of peer-rating by the other machines on the features they think are important. An all-rounder will have a better average rating than a technical-niche machine. The average cross-efficiencies of all 22 machines are shown in Table 6.

Three points are noteworthy. First, the five 100% machines appear in the same order in both methods of calculating focus. But the second point is that, although more complex to calculate, the cross-efficiency method applies to all machines considered, not just the 100% efficient ones. Third, we see that machine 9 (the Smoke Signal Chieftain) is well beaten by both the North Star Horizon (No. 14) and the Commodore CBM 8032 (No. 8). So, the average cross-efficiency is an alternative to simple efficiency; it downplays the technical-niche machine (maverick?) and allows the all-rounder to come through.

The perspective offered by simple efficiency and the perspective offered by (averaged) cross-efficiency reflect the relative strategic outlooks of focus (as argued by Porter) and all-round excellence (as argued by Schonberger), respectively. The manufacturer who is aiming to focus will naturally concentrate on the insights prompted by simple efficiency; the aspiring ‘world class manufacturer’ may be more persuaded by the insights prompted by cross-efficiencies. DEA itself is flexible enough to accommodate both these points of view.

Table 6 Average cross-efficiencies

<table><tr><td>10</td><td>Vector Graphic 3005</td><td>0.887</td></tr><tr><td>11</td><td>IBM &#x27;Personal Computer</td><td>0.886</td></tr><tr><td>4</td><td>Altos ACS 8000-15</td><td>0.844</td></tr><tr><td>5</td><td>WANG 2200 SVP</td><td>0.803</td></tr><tr><td>14</td><td>North Star Horizon</td><td>0.796</td></tr><tr><td>8</td><td>Commodore CBM 8032</td><td>0.767</td></tr><tr><td>9</td><td>Smoke Signal Chieftain</td><td>0.718</td></tr><tr><td>19</td><td>Apple II Plus</td><td>0.679</td></tr><tr><td>18</td><td>Radio Shack TRS 80</td><td>0.607</td></tr><tr><td>20</td><td>DigiTM Micro Sys DSC-2</td><td>0.574</td></tr><tr><td>3</td><td>NEC Astra 205</td><td>0.570</td></tr><tr><td>12</td><td>Xerox 820</td><td>0.532</td></tr><tr><td>16</td><td>Vector Graphic Sys B</td><td>0.503</td></tr><tr><td>22</td><td>Alpha Micro</td><td>0.499</td></tr><tr><td>2</td><td>SD System SD-200</td><td>0.451</td></tr><tr><td>7</td><td>Billings BC 12 DF-2M</td><td>0.422</td></tr><tr><td>6</td><td>Dynabyte 5300</td><td>0.413</td></tr><tr><td>15</td><td>Cromemco System 2</td><td>0.405</td></tr><tr><td>13</td><td>TI 771</td><td>0.400</td></tr><tr><td>21</td><td>Ohio Scientific C3-A</td><td>0.361</td></tr><tr><td>1</td><td>IBM 5120</td><td>0.325</td></tr><tr><td>17</td><td>DEC Station 78</td><td>0.218</td></tr></table>

Table 7 Weights of the 4 outputs and 1 input for each of the 22 machines

<table><tr><td rowspan="2"></td><td colspan="4">OUTPUTS</td><td>INPUT</td></tr><tr><td>Memory</td><td>Disk</td><td>CPU speed</td><td>Disk speed</td><td>Cost</td></tr><tr><td>1</td><td>0.0029256</td><td>0.0001120</td><td>0.0000000</td><td>0.0000000</td><td>0.0000730</td></tr><tr><td>2</td><td>0.0033547</td><td>0.0000915</td><td>2.5565433</td><td>0.0000000</td><td>0.0000813</td></tr><tr><td>3</td><td>0.0033552</td><td>0.0001285</td><td>0.0000000</td><td>0.0000000</td><td>0.0000837</td></tr><tr><td>4</td><td>0.0048077</td><td>0.0000000</td><td>0.0000000</td><td>0.0000000</td><td>0.0001013</td></tr><tr><td>5</td><td>0.0000000</td><td>0.0000000</td><td>4.0458311</td><td>1.0698366</td><td>0.0000685</td></tr><tr><td>6</td><td>0.0045726</td><td>0.0001319</td><td>0.0000000</td><td>11.7749635</td><td>0.0001172</td></tr><tr><td>7</td><td>0.0033290</td><td>0.0000908</td><td>2.5369489</td><td>0.0000000</td><td>0.0000807</td></tr><tr><td>8</td><td>0.0091757</td><td>0.0002731</td><td>0.0000000</td><td>26.0880960</td><td>0.0002448</td></tr><tr><td>9</td><td>0.0000000</td><td>0.0000000</td><td>7.4000074</td><td>0.0000000</td><td>0.0001227</td></tr><tr><td>10</td><td>0.0000000</td><td>0.0001724</td><td>0.0000000</td><td>0.0000000</td><td>0.0000897</td></tr><tr><td>11</td><td>0.0102563</td><td>0.0000000</td><td>6.9750088</td><td>0.0000000</td><td>0.0002198</td></tr><tr><td>12</td><td>0.0054055</td><td>0.0001560</td><td>0.0000000</td><td>13.9195725</td><td>0.0001385</td></tr><tr><td>13</td><td>0.0036766</td><td>0.0001094</td><td>0.0000000</td><td>10.4531508</td><td>0.0000981</td></tr><tr><td>14</td><td>0.0044842</td><td>0.0001523</td><td>5.4968719</td><td>3.0800889</td><td>0.0001447</td></tr><tr><td>15</td><td>0.0042078</td><td>0.0001214</td><td>0.0000000</td><td>10.8355055</td><td>0.0001078</td></tr><tr><td>16</td><td>0.0053243</td><td>0.0001452</td><td>4.0574816</td><td>0.0000000</td><td>0.0001290</td></tr><tr><td>17</td><td>0.0026221</td><td>0.0000780</td><td>0.0000000</td><td>7.4550453</td><td>0.0000700</td></tr><tr><td>18</td><td>0.0053953</td><td>0.0001471</td><td>4.1115955</td><td>0.0000000</td><td>0.0001308</td></tr><tr><td>19</td><td>0.0091399</td><td>0.0002637</td><td>0.0000000</td><td>23.5361390</td><td>0.0002342</td></tr><tr><td>20</td><td>0.0045419</td><td>0.0001239</td><td>3.4612529</td><td>0.0000000</td><td>0.0001101</td></tr><tr><td>21</td><td>0.0029684</td><td>0.0001008</td><td>3.6387818</td><td>2.0389362</td><td>0.0000958</td></tr><tr><td>22</td><td>0.0019859</td><td>0.0000675</td><td>2.4344045</td><td>1.3640817</td><td>0.0000641</td></tr></table>

## Discussion

Let us now turn to comparing Sircar and Dave's original multiple regression analysis of the same raw data, with our Data Envelopment Analysis. Already a distinct difference in philosophy between the two approaches can be seen. As we mentioned in the introduction, a ‘successful’ regression analysis has a high $R^{2}$ . Thus:

"Since our model has a very high coefficient of multiple determination $(R^2 = 0.9998)$ ... it is considerably more accurate than the model developed by Cale et al. for small business systems (which had an $R^2$ of 0.6266) and is therefore a much better predictor of system price"

(Sircar and Dave, 1986)

It would be tempting to conclude from this quote that there can be no such thing as an over-priced machine, since cost appears to be perfectly explained: every machine is priced at such and such because of a mysterious mixture of independent variables, their log transformations and interaction terms. The DEA analyses, however, show quite clearly that some machines were poor value, whether assessed by simple efficiency, or cross-efficiency.

So, multiple regression attempts to fit all data to one all-inclusive model against which each datum is merely an instance of the 'law'. The temptation is to make the model too complex, under the implicit assumption that each datum is a perfect exemplar of the model. By contrast, DEA fits a simple linear model to the data, and takes the differences it finds as true differences in performance. Without differences DEA would have nothing to say. If anything, DEA users should suffer from the opposite temptation to multiple regression users: to include too few variables in order to observe large differences between machines.

In fact, multiple regression analysis can be used to provide a rather cruder version of what DEA is getting at. Suppose we run a multiple regression analysis without interaction terms, and without additional variables as transformations of the original data, and we accept that an $R^{2}$ of rather less than 1 is not an admission of defeat, but just the way the world is. Then, the positive residuals are machines which perform better than predicted by the model. Machines with negative residuals do worse. Machines with positive residuals will also tend to be DEA-efficient.

However, there are some distinct advantages that DEA has over regression. First, the form of a multiple regression analysis is limited to one dependent variable (corresponding to one DEA input) and many independent variables (corresponding to many DEA outputs). DEA, of course, can have many inputs as well as many outputs.

Second, for each machine we have the reference set of 100% efficient machines against which it should be compared. These represent the best of the competition. In addition, the duals can be used to determine an optimal path for improvement towards 100% efficiency. It is also the case that if a manufacturer cannot or will not improve the machine towards the best, then the reference set and the duals also provide information about how advertising money might be spent to reduce the perceived gap in the customer's mind between one's own machine and the best of the rest.

DEA is not without its drawbacks. For instance, there must be rather more units than attributes, otherwise almost all units may be computed as 100% efficient (though this problem does not apply to cross-efficiency). On the other hand, multiple regression itself requires many more observations than independent variables. DEA cannot be used predictively (e.g. to determine the expected price of a 23rd machine from its features alone), as multiple regression can. However, we hope we have done enough to convince that DEA does have its domain of applicability, in which it provides buyers and manufacturers alike with useful information which they would not otherwise have. In surveying the multiple regression analyses of computer benchmarks we can summarize by the following aphorism: "If all you have is a hammer, then everything else must be a nail". We offer DEA as a complementary analytic tool in which new questions can be addressed of the same data.

## Conclusions

The old proverb may have it that ‘comparisons are odious’, but nonetheless a buyer who did not compare and contrast would likely end up with a pig in a poke. In circumstances where the choice is complicated and involves many attributes, human choice maybe unacceptably poor. We suggest the following conclusions to this article.

(1) There are many structurally similar problems in which multi-attributed objects must be compared. For want of an adequate methodology such objects are often not satisfactorily compared.

(2) DEA is a promising, and relatively new decision support tool for multi-attribute comparison, which yields a wealth of comparative information (principally: efficiency, cross-efficiency, reference sets, and dual multipliers).

(3) Each decision support tool circumscribes the kinds of questions that seem appropriate to pose a database. Multiple regression leads the buyer and manufacturer to ask the 'wrong' questions of computer performance data, concentrating as it does on abstracting general ‘laws’ from the data, with each computer seen as merely an instance of the law. DEA focuses on relative performance, and thus draws attention to what is the principal reason for collecting computer performance data: to determine what are the good buys and the bad buys.

(4) Since DEA also points out what should be compared with what, DEA may be equally as important for the strategist as for the buyer in providing new perspectives on the competitive environment.

## Appendix (Implementation)

The form of the DEA analysis allows some programming short-cuts to be taken, when compared with a general LP computer program. A tailor made program was written in C to run portably under MS-DOS and UNIX. Despite the large number of LPs involved, a run of the above analysis took only six and a half seconds on an IBM-AT compatible (80286) machine running at 10 MHz, and with floating point support. Furthermore, the MS-DOS version can also read Lotus worksheets, allowing the user to flit between the DEA program and Lotus using the escape/system, which considerably enhances interactivity.

## References

Banker, R.D., Datar, S.M. and Kemerer, C.F. (1991) A model to evaluate variables impacting the productivity of software maintenance projects, Management Science 37(1), 1–18.

Banker, R.D. and Kemerer, C.F. (1989) Scale economies in new software development, IEEE Transactions on Software Engineering 15(10), 1199–1205.

Bromwich, M. (1990) The case for strategic management accounting: the role of accounting information for strategy in competitive markets, Accounting Organisation and Society, 15(1/2), 27–46.

Cale, E.G., Gremillion, L.L. and McKenny, J.L. (1979) Price/performance patterns of US computer systems, Communications of the ACM, 22(4), 225–231.

Charnes, A.W., Cooper, W.W. and Rhodes, E. (1978) Measuring efficiency of decision-making units', European Journal of Operational Research, 2(6), 429–444.

Dosi, G. (1982) Technological paradigms and technological trajectories, Research Policy, 11(2), 147–162.

Doyle, J.R. and Green, R.H. (1991) Comparing products using Data Envelopment Analysis, Omega, 19(6), 631–638.

Ein-Dor, P. (1985) Grosch's law revisited: CPU power and the cost of computation, Communications of the ACM, 28(2), 142–151.

Ein-Dor, P. and Feldmesser, J. (1987) Attributes of the performance of central processing units: a relative performance model, Communications of the ACM, 30(4), 308–316.

Kang, Y.M. (1989) Computer hardware performance: production and cost function analyses, Communications of the ACM, 32(5), 586–593.

Kuhn, T.S. (1962) The structure of scientific revolutions, University of Chicago Press, Chicago.

Lynch, B.D., Rao, H.R. and Lin, W.T. (1990) Economic analysis of microcomputer hardware, Communications of the ACM, 33(10), 119–129.

Porter, M.E. (1980) Competitive strategy (The Free Press, New York).

Schonberger, R.J. (1986) World Class Manufacturing (The Free Press, New York).

Silkman, R.H. (1986) Measuring Efficiency: An Assessment of Data Envelopment Analysis (Jossey-Bass, San Francisco).

Sircar, S. and Dave, D. (1986) The relationship between benchmark tests and microcomputer price, Communications of the ACM, 29(3), 212–217.

Tomkins, C.R. and Green, R.H. (1988) An experiment in the use of data envelopment analysis for evaluating the efficiency of UK university departments of accounting, Financial Accountability and Management, 4(2), 147–164.

## Biographical notes

John Doyle is lecturer at the School of Management, University of Bath, UK, where he teaches courses in psychology, quantitative methods, and information systems. He is currently researching human aspects of the decision process and techniques (both computer-based and non-computer-based) to support decision making.

Rodney Green is a lecturer in the School of Management, University of Bath. After qualifying as a chemical engineer he worked on the design of computer-based process control systems. The inevitable compromises in such systems led to an interest in operational research and he now teaches and researches in that area.

Address for correspondence: Dr J.R. Doyle, School of Management, University of Bath, Bath BA2 7AY, UK.
