---
otero_id: 21291
otero_key: "MX7YRFZQ"
title: "Design of a web site for guaranteed delay and blocking probability bounds"
authors: "Indranil Bose; Kemal Altinkemer"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00080-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design of a web site for guaranteed delay and blocking probability bounds

Indranil Bose<sup>a,</sup>\*, Kemal Altinkemer<sup>b,1</sup>

<sup>a</sup> Department of Decision and Information Sciences, Warrington College of Business Administration, University of Florida, 351 Stuzin Hall, PO Box 117169, Gainesville, FL 32611, USA

<sup>b</sup> Krannert Graduate School of Management, Purdue University, West Lafayette, IN 47907, USA

Received 1 February 2002; accepted 1 July 2002 Available online 28 June 2003

## Abstract

A new mathematical programming model is proposed for minimizing the cost of design of a Web site by optimally determining the number of servers and buffers when a performance guarantee in terms of the average waiting time and loss probability is to be provided to users. The Web site is modeled as an M/G/c/N queuing system where requests for connections represent arriving customers and the browsing of Web sites represents service received by customers. Numerical experiments are conducted with different choices of problem parameters and the optimal design cost, and optimal number of servers and buffers are obtained for these cases.

Keywords: Finite capacity; Loss probability; Queuing model; Waiting time; Web server

## 1. Introduction

The World-Wide-Web has helped in the sharing of information between Internet users throughout the world. It has become synonymous with a mega warehouse of information. From Ref. [4] we know that, though it was initially started as a project for enabling easy exchange of information between researchers who were geographically distant from each other, it has now taken the role of an international information superhighway. The Web has been used for different purposes such as providing useful context sensitive information, allowing exchange of information within and between organizations, and lately, for advertising, selling and buying merchandise, which has been referred to as electronic commerce, as in Ref. [3]. Whatever be the use, there is no denying that the Web has already become a part of everyday life in a large part of the world.

With the advent of user friendly browsers, the Web has become a technology easy to use and understand. However, in spite of the apparent simplicity of use, users have reported several problems in the use of the Web. Among the top three problems reported in Ref. [14] are searching for specific information, speed of data access and locating and navigating sites. More recently, Selvidge et al. [15] studied the variable impact of Web delays on user lostness, frustration and proportion of task completion. Current technology does not allow users to get an estimate of the amount of time they would have to wait when downloading a document but provides a real-time measure of the amount of content that has been downloaded. Sometimes users wait a significant amount of time and are then refused connection. This is quite frustrating for the users and may lead to inertia about visiting a specific site. Hence, for Web site designers it is important to design the Web site in a manner that neither the waiting time for a requested connection nor is the chance that the user is refused connection is too high.

## 2. Motivation

From Ref. [5], we know that the basic mechanism of operation of the Web is the same as that of a client server system. The three main components are a client site that requests specific information, a Web site with servers and buffers and a network connection that allows communication between the client and the site. The underlying network may be a corporate intranet or it can be the Internet itself. Fig. 1 gives a schematic representation of the overall configuration of a Web server. In case of the client server model based on the Internet the problem of communication is extremely complex as it involves a large variety of client sites that request information from the server site. The delay experienced by a user when requesting information is a function of the client, the server and the network. In most cases, the site provider has no control over the network or the client sites.

In most cases, the configuration of the Web site is done on an ad-hoc basis. The final configuration of the site usually depends on the objectives of the site provider. Some goals might be minimizing the cost of server and buffer installation and operation, minimizing the number of lost requests for access to the site or improving the response time experienced by the users when downloading information from the site. Some of the major issues that need to be considered in order to meet these objectives are the number and type of requests for service, the service time for a request, and the load on the servers. At the same time, the Web site administrator needs to have knowledge about the minimum level of service guarantee to be provided to the users.

We propose a new mathematical programming formulation of the problem of optimally designing a Web site by deciding on the optimal number of servers and buffers to be installed at the site. The goal of the design is to minimize the cost of installation of servers and buffers such that certain service related performance bounds are satisfied. The contribution of this research is to show the applicability of queuing theory in modeling a Web site and using the queuing model in a mathematical programming framework for efficient design of a Web site.

![](/api/attachments/MX7YRFZQ/fulltext/images/0f36c1dedbefd48d18974e2f91fcfc2a5e864be26260695899702c1a58a4c12e.jpg)  
Fig. 1. Client – server model of the Web.

The organization of the paper is as follows. In Section 3, we provide a brief literature review on the use of finite capacity queuing models for some applications and list some research that uses queuing theory for modeling performance of Web servers. In Section 4, the optimization model for the design of the Web server is described. Section 5 provides a derivation of the approximate expression for average waiting time of customers in case of an M/G/c/N queuing system, which is required to solve the optimization problem developed in Section 4. Section 6 details the numerical experiments conducted to obtain the opti mal cost and configuration of Web sites for different service distributions and expected arrival rates and service times. The conclusion and directions for future research appear in Section 7.

## 3. Literature review

In the area of performance evaluation and characterization of Web servers, simulation and statistical analyses have been used predominantly. Using various statistical measures, Arlitt and Williamson [2] obtained document size distribution, document type distribution, document referencing behavior and geographic distribution of requests using six different data sets from various educational and commercial site providers. Iyengar et al. [10] used simulation to develop different tradeoffs between delay experienced by the users and the percentage of requests that are lost, under conditions of heavy traffic, from the Web servers. A benchmarking method based on WebStone, for understanding the performance metrics of a Web server is discussed in Almeida et al. [1]. The use of queuing theory for understanding the performance of Web servers is reported in Slothouber [16]. In this high level model that ignores the details of the HTTP protocol, Web servers are modeled as an open queuing network and the effect of various parameters such as file size, server speed and network bandwidth on the server response time is studied using analytical procedures. In an attempt to model the low level details and interactions between the HTTP and the TCP/IP protocols, Hariharan et al. [9] model Web servers as a tandem queuing model consisting of three interacting components and study the dependence and interaction between these sub-components using simulation. There is some similarity between this research and that of Fischer et al. [8] where M/G/c/c queues are used to model call arrivals at Automatic Call Distribution centers and an alternate expression for calculating loss probabilities is suggested that requires significantly less computation time. Whitt [17] discussed an interesting application of a telephone call center where customer satisfaction was improved by informing the customers about anticipated delays before joining the M/M/c/N queuing system. Lu et al. [13] have addressed the problem of management of delays for different service classes on a Web server. They used a feedback control theory-based approach for designing the adaptive architecture for Web servers operating under HTTP 1.1, which could provide relative delay guarantees for different service classes.

The above review shows that queuing theory has proved to be a useful technique for analyzing Web sites. Our paper takes a unique approach by embedding a queuing theory-based model of a Web site in a new mathematical programming-based formulation for solving the problem of optimal configuration of a Web site. Using the known results on approximate analysis of M/G/c/N queues, we are able to determine the optimal number of Web servers and buffers that a designer should install at a Web site at a minimum cost while providing a guaranteed level of service.

## 4. Model

In this research, a Web site is represented as a queuing system, where the requests for connections represent arriving customers and time spent browsing a particular Web site is defined as service. This is a finite capacity queuing model since the Web site can handle only a limited number of requests. We can model the requests for connections approximately as a Poisson process with exponential inter-arrival time distribution. The users request a connection and after getting a connection, spend time browsing pages within a Web site. Once their purpose is served they quit the system (which may be defined as end of service). Different users spend different amounts of time on the Web sites browsing HTML pages and embedded multimedia files of various sizes. Hence, the service can be assumed to follow a ‘general’ distribution. Since each browsing activity involves browsing a number of Web pages and the time spent browsing each page is random, the total time spent in browsing all the Web pages during a single visit can be assumed to follow a general distribution as well (since the sum of general distributions is a general distribution). Every Web site has a fixed number of servers and also has a limit on the number of connections that it can store in its buffer for future service. Once all servers become busy, all subsequent requests for connections are buffered in the TCP/IP listen queue and they wait for the server to be free. If the waiting spaces are all occupied, then the incoming requests for connection are refused. This is known as blocking of the Web site. The queuing model is an M/ G/c/N queuing system where customers are lost from the system once all servers as well as the waiting spaces in the system become busy. The queuing model of a Web site is depicted in Fig. 2.

The goal of the Web site designer is to minimize the total cost of installation of the Web site and to provide a desired performance guarantee to the users. The performance is guaranteed in terms of the average waiting time of a connection and the blocking probability of the connection.

## Notation:

c = Number of available Web servers on a site N = Number of buffers

Z = Maximum allowable average waiting time of a connection specified by the designer (s)

X = Maximum allowable blocking probability of a connection specified by the designer

$$
a = \text { Cost   of   a   server   (US) }
$$

$$
b = \text { Cost   of   a   buffer(US) }
$$

W = Average time spent to fulfill a request for connection including waiting and connection (s) D = Blocking probability of a connection.

Subject to:

Problem P: Minimize $a c + b N .$

$$
W \leq Z\tag{1}
$$

$$
D \leq X\tag{2}
$$

$$
c \geq 0\tag{3}
$$

$$
N \geq 0
$$

c, N are integers.

ð4Þ

In order to solve this problem, the designer has to obtain closed form expressions for W and D. To the best of our knowledge, no exact closed-form expressions are available for the average waiting time and blocking probability of customers in case of an M/G/ c/N queue. In the next section, we provide a derivation for approximate closed-form analytical expressions for W and D.

## 5. Average waiting time and blocking probability

In this section, we derive an approximate expression for the waiting time of customers and the blocking probability in case of an M/G/c/N queue with a single class of service and under heavy traffic condition. This is required for solving Problem P described in the earlier section. Multiserver queues with ‘general’ service are difficult to analyze. Although closed form expressions are available for the M/M/c/N queues, the ‘general’ service distribution for an M/G/c/N queue makes it difficult to obtain exact analytical results.

![](/api/attachments/MX7YRFZQ/fulltext/images/14e879ef07d6b1f1eedbb7fac1fbbe4c61317a3b200b4baf9210c43dbf936a4d.jpg)  
Fig. 2. A queuing representation of a Web site.

## Additional notation:

k = Arrival rate of incoming requests for connection to a Web site (requests/s)

s = Service time for each incoming connection (s) E(s) = Average time spent by a connection at a Web site for browsing activity (s)

P<sub>j</sub> = Probability that there are j servers busy at a Web site where j = 1, 2, . . ., c

L<sub>q</sub> = Average number of requests for connection waiting to be serviced in the buffers

W<sub>q</sub> = Average waiting time experienced by a request for a connection (s)

$$
\rho = \lambda E (s).
$$

According to Kimura [11], the steady-state probability that j servers among c servers remain busy at any time in case of an M/G/c/N queue is given by:

$$
P _ {j} = \left\{ \begin{array}{l l} \frac {(c \rho) ^ {s} P _ {0}}{j !}, & j = 1, \dots , c - 1 \\ \frac {(c \rho) ^ {c}}{c !} \frac {1 - \xi}{1 - \rho} \xi^ {j - c} P _ {0}, & j = c, c + 1, \dots , c + N - 1 \\ \frac {(c \rho) ^ {c}}{c !} \xi^ {N} P _ {0}, & j = c + N \end{array} \right.\tag{5}
$$

where

$$
P _ {0} = \left\{\sum_ {k = 0} ^ {c - 1} \frac {(c \rho) ^ {k}}{k !} + \frac {(c \rho) ^ {c}}{c !} \frac {1 - \rho \xi^ {N}}{1 - \rho} \right\} ^ {- 1}\tag{6}
$$

$$
\xi = \frac {\lambda E (s) R _ {\mathrm{G}}}{c - \{\lambda E (s) + \lambda E (s) R _ {\mathrm{G}} \}}\tag{7}
$$

Expected waiting time for general service distribution R<sub>G</sub> ¼ Expected waiting time for exponential service

ð8Þ

Exact expressions for $R _ { \mathrm { G } }$ are difficult to obtain. However, an asymptotic result on $R _ { \mathrm { G } }$ under the condition of heavy traffic $( \mathrm { i . e . , ~ } \rho \to 1 )$ is available from Kimura [11]. It states that

$$
\lim _ {\rho \rightarrow 1} R _ {\mathrm{G}} = \frac {1 + c _ {\mathrm{v}} ^ {2}}{2}\tag{9}
$$

where $c _ { \mathrm { v } }$ is the coefficient of variation of the underlying service distribution. It is stated in Kimura [11] that ‘‘the approximation is exact for the cases with either no extra waiting space, exponential service-time distribution, or a certain two-parameter family of service-time distribution’’. Hence, the approximation is valid in our case with the only limiting condition that there is heavy traffic in the system and $\rho \to 1$

The value for $P _ { j }$ from Eqs. (5) and (6) can be used together with the Poisson Arrivals See Time Averages (PASTA) property to calculate the number of requests for connection that are lost (D) because the servers and the buffers remain busy. This is same as the blocking probability of a connection. We find,

$$
D = P _ {c + N}\tag{10}
$$

The expression for D is used in constraint (2) of the optimization Problem P described in Section 4. The information conveyed by this formula is important if the Web site provider needs to keep track of the number of connections that are lost. Every site will possibly have a known percentage of ‘lost customers’ that they can tolerate due to unavailability of buffers. Once D exceeds that value, this might give a signal that the site is getting ‘too busy’.

Another figure of merit is the average number of requests for connection waiting to be serviced in the buffers. Using simple algebra, the expression for $L _ { \mathrm { q } }$ is given by

$$
L _ {\mathrm{q}} = \sum_ {n = c + 1} ^ {c + N} (n - c) P _ {n}\tag{11}
$$

Using Little’s Law, the average waiting time of the request for connection is given by

$$
W _ {\mathrm{q}} = \frac {L _ {\mathrm{q}}}{\lambda (1 - P _ {c + N})}\tag{12}
$$

Again, the total time spent by the request for waiting in the buffer as well as completing the service of downloading the required Web pages is then easily obtained by adding the average queuing time to the average service time. In other words,

$$
W = W _ {\mathrm{q}} + E (s)\tag{13}
$$

This expression for W is used in constraint (1) for solving the optimization Problem P detailed in Section 4.

## 6. Numerical experiments

The goal of the numerical experiments reported in this section is to obtain the solution to the nonlinear optimization Problem P in terms of the total cost of installation of servers and buffers, optimal number of servers and optimal number of buffers. The designer provides known bounds for the blocking probability and average waiting time of a connection. We experiment with two different distributions—Erlang-2 (with coefficient of variation 0.5) and hyperexponential (with coefficient of variation 1.0) to represent the ‘general’ service distribution of the model and for two pairs of values for E(s) and k. Physically, the Web server is a commercially available computer server that can host a Web site and hence we assume the unit cost of server (a) to be US\$3000. The buffer is equivalent to a hard disk that can be used for storage of requests and the unit cost of buffer (b) is assumed to be US\$100.

Since Problem P is a nonlinear optimization problem it could not be solved using any commercially available software. We used an indirect approach for solving this problem. Given a known delay bound and a blocking probability bound we first completely enumerated the combination of c and N values (integers) that satisfy constraints (1) and (2). Next we choose the pair of values that resulted in the minimum value of the objective function as the optimal solution. The program for obtaining the solution was coded using MATLAB 5.3 and was run on a Pentium III 650 MHz personal computer.

An important step in conducting the numerical experiments is to estimate the parameters k and E(s). Estimates of these parameters can be obtained from the log-files associated with a Web site. As noted by Eschenfelder et al. [7], the estimates can be obtained from the access log file that lists the IP address of the user, data and time of the access and user action taken during the access period including the timestamp of the last activity of the user on the Web site. For our numerical experiments, we studied the log-files of several Web sites to obtain realistic values for the parameters k and E(s).

In the first experiment, we assume a heavy traffic load on the server and let k = 170 requests/s and E(s) = 175 s. The service distribution is Erlang-2. The blocking probability is varied from 0.01 to 0.1 and the average waiting time is varied from 300 to 1000 s. No feasible solution to the optimization problem can be found if the blocking probability is less than 0.01 and the average waiting time is less than 300 s. The most expensive scenario for design involves 23 servers and 40 buffers, with a total design cost of US\$73 000. The least cost of design, i.e., US\$3500, is obtained when the blocking probability is 0.1 and the average waiting time varies between 600 and 1000 s. The results of this experiment are shown in Table 1.

In the second experiment, all parameter values are kept unchanged except the service distribution is chosen to be hyperexponential. It is to be noted that the specific distribution function is not used in calculation of the problem parameters. The coefficient of variation of the service distribution is used for computation of D and W. In Table 2, no optimal solution can be obtained for a blocking probability value of 0.01. This is so because there is no feasible solution available that satisfies a loss probability bound of 0.01 as well as a delay bound between 300 and 1000 s. This goes to show that a loss probability bound of 0.01 (i.e., only 1% of the requests are rejected) is extremely stringent and generally cannot be provided by a Web server while providing a delay bound within a tolerable limit. It is also observed from the second experiment that the optimal design turns out to be more expensive in the case of the hyperexponential service distribution than that of the Erlang-2 distribution.

The third set of experiments is conducted for k = 340 requests/s, E(s) = 350 s and for Erlang-2 and hyperexponential distributions and the results are reported in Tables 3 and 4, respectively. From Tables 3 and 4, we see that when the arrival rate is doubled and the service rate is halved it becomes increasingly difficult to obtain an optimal solution to the optimization problem for stricter delay bounds. This is the reason why our solution method is not able to find any solution for an average delay bound < 600 s. Also, as observed in the paragraph above, we again note that the optimal design turns out to be more expensive in the case of the hyperexponential service distribution.

Table 1  
Number of servers, number of buffers and total installation cost (US\$) for various average delay bounds (s) and loss probability bounds for Erlang-2 service distribution with E(s) = 175 s and k = 170/s  
![](/api/attachments/MX7YRFZQ/fulltext/images/a8bc1f56e00697fef8e9d33df7d11388ac38e722ea7ec8f2bed84d029dabe507.jpg)  
z: Total installation cost

<table><tr><td rowspan="2">Loss probability</td><td colspan="8">Delay</td></tr><tr><td>300</td><td>400</td><td>500</td><td>600</td><td>700</td><td>800</td><td>900</td><td>1000</td></tr><tr><td rowspan="2">0.01</td><td>23, 40</td><td>14, 41</td><td>10, 41</td><td>8, 41</td><td>6, 42</td><td>5, 42</td><td>5, 42</td><td>4, 42</td></tr><tr><td>73000</td><td>46100</td><td>34100</td><td>28100</td><td>22200</td><td>19200</td><td>19200</td><td>16200</td></tr><tr><td rowspan="2">0.02</td><td>14, 23</td><td>8, 23</td><td>6, 24</td><td>5, 24</td><td>4, 24</td><td>4, 24</td><td>3, 24</td><td>3, 24</td></tr><tr><td>44300</td><td>26300</td><td>20400</td><td>17400</td><td>14400</td><td>14400</td><td>11400</td><td>11400</td></tr><tr><td rowspan="2">0.03</td><td>4, 39</td><td>6, 16</td><td>5, 16</td><td>4, 17</td><td>3, 17</td><td>3, 17</td><td>2, 17</td><td>2, 27</td></tr><tr><td>15900</td><td>19600</td><td>16600</td><td>13700</td><td>10700</td><td>10700</td><td>7700</td><td>7700</td></tr><tr><td rowspan="2">0.04</td><td>4, 35</td><td>5, 12</td><td>4, 13</td><td>3, 13</td><td>2, 13</td><td>2, 13</td><td>2, 13</td><td>2, 13</td></tr><tr><td>15500</td><td>16200</td><td>13300</td><td>10300</td><td>7300</td><td>7300</td><td>7300</td><td>7300</td></tr><tr><td rowspan="2">0.05</td><td>4, 33</td><td>4, 10</td><td>3, 10</td><td>2, 10</td><td>2, 10</td><td>2, 10</td><td>2, 10</td><td>2, 10</td></tr><tr><td>15300</td><td>13000</td><td>10000</td><td>7000</td><td>7000</td><td>7000</td><td>7000</td><td>7000</td></tr><tr><td rowspan="2">0.06</td><td>3, 31</td><td>3, 8</td><td>3, 8</td><td>2, 9</td><td>2, 9</td><td>2, 9</td><td>2, 9</td><td>1, 9</td></tr><tr><td>12100</td><td>9800</td><td>9800</td><td>6900</td><td>6900</td><td>6900</td><td>6900</td><td>3900</td></tr><tr><td rowspan="2">0.07</td><td>3, 31</td><td>3, 7</td><td>2, 7</td><td>2, 7</td><td>2, 7</td><td>2, 7</td><td>1, 8</td><td>1, 8</td></tr><tr><td>12100</td><td>9700</td><td>6700</td><td>6700</td><td>6700</td><td>6700</td><td>3800</td><td>3800</td></tr><tr><td rowspan="2">0.08</td><td>3, 30</td><td>3, 6</td><td>2, 6</td><td>2, 6</td><td>2, 6</td><td>1, 7</td><td>1, 7</td><td>1, 7</td></tr><tr><td>12000</td><td>9600</td><td>6600</td><td>6600</td><td>6600</td><td>3700</td><td>3700</td><td>3700</td></tr><tr><td rowspan="2">0.09</td><td>3, 5</td><td>3, 5</td><td>2, 6</td><td>2, 6</td><td>1, 6</td><td>1, 6</td><td>1, 6</td><td>1, 6</td></tr><tr><td>9500</td><td>9500</td><td>6600</td><td>6600</td><td>3600</td><td>3600</td><td>3600</td><td>3600</td></tr><tr><td rowspan="2">0.1</td><td>3, 5</td><td>2, 5</td><td>2, 5</td><td>1, 5</td><td>1, 5</td><td>1, 5</td><td>1, 5</td><td>1, 5</td></tr><tr><td>9500</td><td>6500</td><td>6500</td><td>3500</td><td>3500</td><td>3500</td><td>3500</td><td>3500</td></tr></table>

Table 2

Number of servers, number of buffers and total installation cost (US\$) for various average delay bounds (s) and loss probability bounds for hyperexponential service distribution with E(s) = 175 s and k = 170/s

<table><tr><td rowspan="2">Loss probability</td><td colspan="8">Delay</td></tr><tr><td>300</td><td>400</td><td>500</td><td>600</td><td>700</td><td>800</td><td>900</td><td>1000</td></tr><tr><td>0.01</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0.02</td><td>21, 35</td><td>12, 36</td><td>9, 37</td><td>7, 37</td><td>6, 37</td><td>5, 38</td><td>5, 38</td><td>4, 38</td></tr><tr><td></td><td>66500</td><td>39600</td><td>30700</td><td>24700</td><td>21700</td><td>18800</td><td>18800</td><td>15800</td></tr><tr><td>0.03</td><td>5, 46</td><td>9, 25</td><td>7, 25</td><td>5, 26</td><td>4, 26</td><td>4, 26</td><td>3, 26</td><td>3, 26</td></tr><tr><td></td><td>19600</td><td>29500</td><td>23500</td><td>17600</td><td>14600</td><td>14600</td><td>11600</td><td>11600</td></tr><tr><td>0.04</td><td>4, 39</td><td>5, 49</td><td>5, 19</td><td>4, 20</td><td>4, 20</td><td>3, 20</td><td>3, 20</td><td>2, 20</td></tr><tr><td></td><td>15900</td><td>19900</td><td>16900</td><td>14000</td><td>14000</td><td>11000</td><td>11000</td><td>8000</td></tr><tr><td>0.05</td><td>4, 35</td><td>6, 15</td><td>4, 16</td><td>4, 16</td><td>3, 16</td><td>3, 16</td><td>2, 16</td><td>2, 16</td></tr><tr><td></td><td>15500</td><td>19500</td><td>13600</td><td>13600</td><td>10600</td><td>10600</td><td>7600</td><td>7600</td></tr><tr><td>0.06</td><td>4, 33</td><td>5, 12</td><td>4, 13</td><td>3, 13</td><td>3, 13</td><td>2, 13</td><td>2, 13</td><td>2, 13</td></tr><tr><td></td><td>15300</td><td>16200</td><td>13300</td><td>10300</td><td>10300</td><td>7300</td><td>7300</td><td>7300</td></tr><tr><td>0.07</td><td>4, 32</td><td>4, 11</td><td>3, 11</td><td>3, 11</td><td>2, 11</td><td>2, 11</td><td>2, 11</td><td>2, 11</td></tr><tr><td></td><td>15200</td><td>13100</td><td>10100</td><td>10100</td><td>7100</td><td>7100</td><td>7100</td><td>7100</td></tr><tr><td>0.08</td><td>4, 31</td><td>4, 9</td><td>3, 9</td><td>2, 10</td><td>2, 10</td><td>2, 10</td><td>2, 10</td><td>2, 10</td></tr><tr><td></td><td>15100</td><td>12900</td><td>9900</td><td>7000</td><td>7000</td><td>7000</td><td>7000</td><td>7000</td></tr><tr><td>0.09</td><td>4, 31</td><td>3, 8</td><td>3, 8</td><td>2, 9</td><td>2, 9</td><td>2, 9</td><td>2, 9</td><td>1, 9</td></tr><tr><td></td><td>15100</td><td>9800</td><td>9800</td><td>6900</td><td>6900</td><td>6900</td><td>6900</td><td>3900</td></tr><tr><td>0.1</td><td>3, 30</td><td>3, 7</td><td>3, 7</td><td>2, 8</td><td>2, 8</td><td>2, 8</td><td>1, 8</td><td>1, 8</td></tr><tr><td></td><td>12000</td><td>9700</td><td>9700</td><td>6800</td><td>6800</td><td>6800</td><td>3800</td><td>3800</td></tr></table>

These results can be of use to a Web site designer in a number of ways. First, if the designer is operating under a given budget, (s)he can decide how many servers and buffers to procure to provide the best quality of service. For some designers, blocking probability will be of more concern than average delay and (s)he can choose to operate with a stringent bound for blocking probability and loose bound for average delay. Depending on the criterion, (s)he will be able to operate on different cells of Table 1, 2, 3 or 4. Second, an important aspect of these experiments is that even if the designer has no knowledge about the service distribution of the various users, (s)he can still use the results of the hyperexponential and Erlang-2 distributions to solve the problem of Web site design to get an idea about the approximate cost of config-

Number of servers, number of buffers and total installation cost (US\$) for various average delay bounds (s) and loss probability bounds for Erlang-2 service distribution with E(s) = 350 s and k = 340/s

<table><tr><td rowspan="2">Loss probability</td><td colspan="6">Delay</td></tr><tr><td>500</td><td>600</td><td>700</td><td>800</td><td>900</td><td>1000</td></tr><tr><td rowspan="2">0.01</td><td>-</td><td>23, 40</td><td>17, 40</td><td>14, 41</td><td>11, 41</td><td>10, 41</td></tr><tr><td></td><td>73000</td><td>55000</td><td>46100</td><td>37100</td><td>34100</td></tr><tr><td rowspan="2">0.02</td><td>-</td><td>14, 23</td><td>10, 23</td><td>8, 23</td><td>7, 23</td><td>6, 24</td></tr><tr><td></td><td>44300</td><td>32300</td><td>26300</td><td>23300</td><td>20400</td></tr><tr><td rowspan="2">0.03</td><td>-</td><td>10, 16</td><td>7, 16</td><td>6, 16</td><td>5, 16</td><td>5, 16</td></tr><tr><td></td><td>31600</td><td>22600</td><td>19600</td><td>16600</td><td>16600</td></tr><tr><td rowspan="2">0.04</td><td>-</td><td>8, 12</td><td>6, 12</td><td>5, 12</td><td>4, 13</td><td>4, 13</td></tr><tr><td></td><td>25200</td><td>19200</td><td>16200</td><td>13300</td><td>13300</td></tr><tr><td rowspan="2">0.05</td><td>-</td><td>6, 10</td><td>5, 10</td><td>4, 10</td><td>3, 10</td><td>3, 10</td></tr><tr><td></td><td>19000</td><td>16000</td><td>13000</td><td>10000</td><td>10000</td></tr><tr><td rowspan="2">0.06</td><td>-</td><td>5, 8</td><td>4, 8</td><td>3, 8</td><td>3, 8</td><td>3, 8</td></tr><tr><td></td><td>15800</td><td>12800</td><td>9800</td><td>9800</td><td>9800</td></tr><tr><td rowspan="2">0.07</td><td>-</td><td>5, 7</td><td>4, 7</td><td>3, 7</td><td>2, 7</td><td>2, 7</td></tr><tr><td></td><td>15700</td><td>12700</td><td>9700</td><td>6700</td><td>6700</td></tr><tr><td rowspan="2">0.08</td><td>-</td><td>4, 6</td><td>3, 6</td><td>3, 6</td><td>2, 6</td><td>2, 6</td></tr><tr><td></td><td>12600</td><td>9600</td><td>9600</td><td>6600</td><td>6600</td></tr><tr><td rowspan="2">0.09</td><td>-</td><td>3, 5</td><td>3, 5</td><td>3, 5</td><td>2, 6</td><td>2, 6</td></tr><tr><td></td><td>9500</td><td>9500</td><td>9500</td><td>6600</td><td>6600</td></tr><tr><td rowspan="2">0.1</td><td>-</td><td>3, 5</td><td>3, 5</td><td>2, 5</td><td>2, 5</td><td>2, 5</td></tr><tr><td></td><td>9500</td><td>9500</td><td>6500</td><td>6500</td><td>6500</td></tr></table>

Number of servers, number of buffers and total installation cost (US\$) for various average delay bounds (s) and loss probability bounds for hyperexponential service distribution with E(s) = 350 s and k = 340/s

<table><tr><td rowspan="2">Loss probability</td><td colspan="6">Delay</td></tr><tr><td>500</td><td>600</td><td>700</td><td>800</td><td>900</td><td>1000</td></tr><tr><td>0.01</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0.02</td><td>-</td><td>21, 35</td><td>16, 35</td><td>12, 36</td><td>11, 36</td><td>9, 37</td></tr><tr><td></td><td></td><td>66500</td><td>51500</td><td>39600</td><td>36600</td><td>30700</td></tr><tr><td>0.03</td><td>-</td><td>12, 49</td><td>11, 25</td><td>9, 25</td><td>7, 25</td><td>7, 25</td></tr><tr><td></td><td></td><td>40900</td><td>35500</td><td>29500</td><td>23500</td><td>23500</td></tr><tr><td>0.04</td><td>-</td><td>10, 41</td><td>9, 18</td><td>7, 19</td><td>6, 19</td><td>5, 19</td></tr><tr><td></td><td></td><td>34100</td><td>28800</td><td>22900</td><td>19900</td><td>16900</td></tr><tr><td>0.05</td><td>-</td><td>9, 14</td><td>7, 15</td><td>6, 15</td><td>5, 15</td><td>4, 16</td></tr><tr><td></td><td></td><td>28400</td><td>22500</td><td>19500</td><td>16500</td><td>13600</td></tr><tr><td>0.06</td><td>-</td><td>8, 12</td><td>6, 12</td><td>5, 12</td><td>4, 13</td><td>4, 13</td></tr><tr><td></td><td></td><td>25200</td><td>19200</td><td>16200</td><td>13300</td><td>13300</td></tr><tr><td>0.07</td><td>-</td><td>6, 10</td><td>5, 10</td><td>4, 11</td><td>4, 11</td><td>3, 11</td></tr><tr><td></td><td></td><td>19000</td><td>16000</td><td>13100</td><td>13100</td><td>10100</td></tr><tr><td>0.08</td><td>-</td><td>6, 9</td><td>4, 9</td><td>4, 9</td><td>3, 9</td><td>3, 9</td></tr><tr><td></td><td></td><td>18900</td><td>12900</td><td>12900</td><td>9900</td><td>9900</td></tr><tr><td>0.09</td><td>-</td><td>5, 8</td><td>4, 8</td><td>3, 8</td><td>3, 8</td><td>3, 8</td></tr><tr><td></td><td></td><td>15800</td><td>12800</td><td>9800</td><td>9800</td><td>9800</td></tr><tr><td>0.1</td><td>-</td><td>5, 7</td><td>4, 7</td><td>3, 7</td><td>3, 7</td><td>3, 7</td></tr><tr><td></td><td></td><td>15700</td><td>12700</td><td>9700</td><td>9700</td><td>9700</td></tr></table>

uration. Third, these experiments can help designers understand what realistic performance guarantees they can provide to their users (e.g., a delay bound of 300 s will be difficult to provide together with a blocking probability bound of 0.01).

## 7. Conclusion

With the present design of the Web, whenever the client makes a request for accessing a Web site they are often refused connection after waiting for a significant amount of time. This leads to a growing frustration among the users. From an electronic commerce point of view, this is a tremendous loss for sites that are conducting business over the Web because these unsatisfied customers are not likely to return to these sites again. A better way to handle this situation would be to configure the Web site a priori based on knowledge about bounds for average waiting time and blocking probability. In this paper, we provide an optimization-based formulation of the problem of minimizing the cost of Web site design when a given delay bound and blocking probability bound is to be guaranteed to all users. The solution obtained shows that for higher arrival rates and lower service rates it will become increasingly difficult to satisfy stringent delay bounds. Also, when the service distribution is hyperexponential with a higher coefficient of variation, the optimal design turns out to be more expensive under identical operating conditions than that of the Erlang-2 service distribution.

Future research can be conducted by extending this model to the case where the low level implementation details of the HTTP and TCP/IP are accounted for in the model. Another extension can be to model the situation where there are proxy caches in between the requesting client and the server and hence a large number of requests do not reach the server itself but are satisfied by the intermediate caches. In fact, in an extensive study conducted by considering the end-toend traffic between client sites distributed worldwide and 700 servers to which majority of the traffic is targeted, Krishnamurthy and Wills [12] has showed that caching and multi-server content distribution can improve performance of Web servers significantly if done in an effective manner. One effective way to improve performance of proxy caches is to use prefetching. The prefetching technique relies on the ability of the proxy cache server to predict which cached documents a user might reference next, and takes advantage of the idle time between user requests to push or pull the documents to the user. Future extensions should incorporate the idea of prefetching as well as caching in the model of a Web server. In recent literature such as Crovella and Bestavros [6], it has been reported that the Web traffic often tend to be self-similar and bursty and hence the ‘memoryless property of the exponential inter-arrival distribution of a Poisson arrival process may or may not hold at all times. The arrival process in this paper is assumed to be Poisson but the model can be extended to the case where the arrival process is modeled by a heavy-tailed distribution to more accurately model the real-time Web traffic.

## Acknowledgements

The authors would like to thank the two anonymous referees for their various useful and important suggestions that have helped improve the quality of the paper to a great extent.

## References

[1] V.A.F. Almeida, J.M. de Almeida, C.S. Murta, Performance analysis of a web server, Proceedings of the 22nd International Conference for the Resource Management and Performance Evaluation of Enterprise Computing Systems, San Diego, CA, 1996, pp. 829 – 838.

[2] M. Arlitt, C.L. Williamson, Internet web servers: workload characterization and performance implications, IEEE/ACM Transactions on Networking 5 (1997) 631–645.

[3] L.M. Applegate, C.W. Holsapple, R. Kalakota, F.J. Radermacher, A.B. Whinston, Electronic commerce: building blocks of new business opportunity, Journal of Organizational Computing and Electronic Commerce 6 (1996) 1 – 10.

[4] T. Berners-Lee, R. Caillian, A. Luotonen, H.F. Nielsen, A. Secret, The World-Wide Web, Communications of the ACM 37 (1994) 77 – 82.

[5] H.K. Bhargava, S. Sridhar, Design issues in configuring servers on the World Wide Web, Proceedings of the First INFORMS Conference on Information Systems and Technology, Washington, DC, USA, 1996, pp. 204– 208.

[6] M.E. Crovella, A. Bestavros, Self-similarity in World Wide Web traffic: evidence and possible causes, IEEE/ACM Transactions on Networking 5 (1997) 835–846.

[7] K. Eschenfelder, S.K. Wyman, J.C. Bertot, W.E. Moen, C.R. McClure, Using log files to assess web-enabled information systems usage, Proceedings of the Third Americas Conference on Information Systems, Indianapolis, IN, USA, 1997, pp. 869–871.

[8] M.J. Fischer, D.A. Garbin, A. Gharakhanian, Performance modeling of distributed automatic call distribution systems, Telecommunication Systems 9 (1998) 133– 152.

[9] R. Hariharan, P. Reeser, R. Van der Mei, Web server performance modeling, Proceedings of the 4th INFORMS Conference on Telecommunication, Boca Raton, FL, USA, 1998, pp. 43 – 44.

[10] A. Iyengar, E. MacNair, T. Nguyen, An analysis of web server performance, Proceedings of the IEEE Global Telecommunications Conference, Phoenix, AZ, USA, 1997, pp. 1943 – 1947.

[11] T. Kimura, A transform-free approximation for the finite capacity M/G/s queue, Operations Research 44 (1996) 984 – 988.

[12] B. Krishnamurthy, C.E. Wills, Analyzing factors that influence end-to-end Web performance, Computer Networks 33 (2000) 17 – 32.

[13] C. Lu, T.F. Abdelzaher, J.A. Stankovic, S.H. Son, A feedback control approach for guaranteeing relative delays in web servers, Proceedings of the 7th Real-Time Technology and Applications Symposium Taipei, Taiwan, 2001, pp. 51 – 62.

[14] N.J. Lightner, I. Bose, G. Salvendy, What is wrong with the World-Wide-Web?: a diagnosis of some problems and

prescription of some remedies, Ergonomics 39 (1996) 995– 1004.

[15] P.R. Selvidge, B.S. Chaparro, G.T. Bender, The world wide wait: effects of delays on user performance, International Journal of Industrial Ergonomics 29 (2002) 15– 20.

[16] L.P. Slothouber, A model of web server performance. Proceedings of the 5th International World Wide Web Conference, Paris, France.

[17] W. Whitt, Improving service by informing customers about anticipated delays, Management Science 45 (1999) 192 – 207.

Indranil Bose is an Assistant Professor of Decision and Information Sciences at the Warrington College of Business Administration, University of Florida. His degrees include BTech (Electrical Engineering) from Indian Institute of Technology, MS (Electrical and Computer Engineering) from University of Iowa, MS (Industrial Engineering) and PhD (Management Information Systems) from Purdue University. He has research interests in telecommunications design and policy issues, data mining and artificial intelligence, electronic commerce, applied operations research and supply chain management. His teaching interests are in telecommunications, database management, systems analysis and design, and data mining. His publications have appeared in Computers and Operations Research, Decision Support Systems, Ergonomics, European Journal of Operational Research, Information and Management and in the proceedings of numerous international and national conferences.

Kemal Altinkemer received his PhD in Computers and Information Systems from William E. Simon School of Business Administration, University of Rochester, Rochester, NY 14627 in 6/87. He is currently an Associate Professor and the area coordinator for MIS at the Krannert School of Management, Purdue University. His research interests are Infrastructure for E-commerce and pricing of information goods, bidding with intelligent software agents, strategy from Brickandmortar to Clickandmortar business model, design and analysis of local area networks, local access computer networks and backbone networks, infrastucture development such as ATM, LEOS systems such as TELEDESIC, distribution of priorities by using pricing as a tool, and time restricted priority routing. He has published numerous articles in journals such as Management Science, Operations Research, INFORMS Journal on Computing, EJOR and Transactions of the ACM.
