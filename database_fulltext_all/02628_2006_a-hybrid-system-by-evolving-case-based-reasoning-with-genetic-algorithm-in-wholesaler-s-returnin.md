---
otero_id: 2628
otero_key: "NBRUYUJK"
title: "A hybrid system by evolving case-based reasoning with genetic algorithm in wholesaler's returning book forecasting"
authors: "Pei-Chann Chang; Chien-Yuan Lai; K. Robert Lai"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.02.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hybrid system by evolving case-based reasoning with genetic algorithm in wholesaler's returning book forecasting

Pei-Chann Chang <sup>a,⁎</sup>, Chien-Yuan Lai <sup>a</sup>, K. Robert Lai <sup>b</sup>

<sup>a</sup> Department of Industrial Engineering and Management, Yuan Ze University, Taoyuan 32026, Taiwan, R.O.C. <sup>b</sup> Department of Computer Science and Engineering, Yuan Ze University, Taoyuan 32026, Taiwan, R.O.C.

Received 2 February 2005; received in revised form 30 November 2005; accepted 18 February 2006 Available online 19 April 2006

## Abstract

A hybrid system by evolving a Case-Based Reasoning (CBR) system with a Genetic Algorithm (GA) is developed for wholesaler's returning book forecasting. For a new book, key factors, such as the grade of the author, the grade of publisher, hot or slow season of publication date, sale volumes for the first 3 months and the returning rate, have been identified and applied as the key features to calculate the similarity coefficient of a new release book and to retrieve similar book from the reference cases to justify if the new book is a slow-selling or selling book. The case base of this research is acquired from a book wholesaler in Taiwan, and it is applied by the hybrid system to forecast returning books. The results of the prediction of the hybrid system were compared with the results of a back propagation neural network (BPNN), a conventional CBR, and a multiple-regression analysis method. The experimental results show that the GA/CBR is more accurate and efficient when being applied to the forecast of the returning books than other methods.

Keywords: Case-based reasoning; Genetic algorithms; Back propagation neural network; Multiple regression analysis

## 1. Introduction

Book Wholesales in Taiwan are under an extremely competitive business environment, in order to face the complicated market competition; they are trying their best to make the ultimate policy. The completeness of the information available to the decision-maker is the key factor influencing the quality of the decisions. A book wholesaler could have better controls if sales forecast is conducted for a new book, and simultaneously another forecast for book returning is conducted after its release. In business forecasting, managers often apply the outcomes of past similar cases to predict the result of the current one. The methods to be used for sales forecasting are nothing more than naive prediction, statistical methods, or artificial intelligent methods. Among these methods, artificial intelligent (AI) methods are mostly used in academic studies because of the ability to provide rapid solutions with high accuracy and to deal with diversified cases.

For the book industry in Taiwan, it is very difficult to predict sales and returned volumes because the products have various classifications and different lengths of life cycles, and the environment in this industry is very unique. Average, there are about 3412.6 new books being published every month in Taiwan, and the speed for new released books is really high. The returning rate of books is more than 30% in this industry according to the actual data collected from the wholesaler and from the past studies [7]. The main reason of high book returning rate is caused by the insufficient information of book sales status in the book supply chain which brings up bullwhip effect and forms up the unbalanced situation between supply and demand. Blind returning activities happen so often because retailing bookstores are often space limited, without efficient computerized managing system, and moreover they do not have to bear any forward and reverse logistics cost. High book returning rate is a very heavy burden for all companies in this industry. Hence, a returning forecasting system for slow-selling books is developed in this research to advise the retailers on returning book decision making and to avoid blind returning movements. The system is a hybrid method by integrating a conventional CBR with adjusted factor weights by Genetic Algorithms (GAs) to conduct a high accurate and efficient book-returning forecast to reduce high book returning rate and to increase profits.

The remainder of this paper is organized as follows: Section 2 describes relevant literature review. Section 3 presents the hybrid method that integrates CBR with GAs. Section 4 describes problems. Section 5 depicts experimental design and results. In the final section, the conclusion is presented.

## 2. Literature review

In this section, current forecasting approaches and integrated GAs and CBR are briefly reviewed.

## 2.1. Current forecasting approaches

Forecasting always plays an important role in a decision support system. The first step for business planning is sales forecasting, and enterprises have to understand the changing demands of the products for future markets in order to reserve appropriate resources for future production. Effective forecasting obtained in advance can help the decision maker in planning the production quantity and cutting down the material costs, even determining the selling price. It can result in a lower inventory level and achieve the objective of just in time manufacturing [19]. The barrier of communication for forecast occurred because managers usually ignore the application, test, and control of key information and execute the results of forecast of the model [12].

In the book industry, returning books forecast is equally important to sales forecast. Under the environment of limited space, low computerized level, frequent release of new books and no forward/reverse logistics

![](/api/attachments/NBRUYUJK/fulltext/images/94489977c420c8a644d29fe70408dca35d55fb7d6b8b731b26777111ea91ff0f.jpg)  
Fig. 1. A CBR cycle. (Adopted from Aamodt and Plaza [1]).

![](/api/attachments/NBRUYUJK/fulltext/images/17323a8bfdcf19000000e45b8fd2cd268c2c99564d2899c1f75c1ed10cb16692.jpg)  
Fig. 2. The framework of the hybrid system combining CBR and GAs.

cost for retailers, books are returned to wholesales so often without proper evaluations. Retailers might return selling books and place the order again later. This could affect the profit of wholesales, competitive ability of retailers, and also may lead the publishers to re-print a book without proper market demands. Therefore, it should be very important for Taiwan book industry to value the issue of return book forecast, and provide a proper and accurate list of possible slow-selling books to the retailers for correct book returning activities, and also for publishers to evaluate and introduce promotion strategy for the slow-selling books.

![](/api/attachments/NBRUYUJK/fulltext/images/2a0bd6363bcef3703b2b2ef2025d5b3ffa1e1dd09ef267e7c12385a23a79f427.jpg)  
Fig. 3. An introspective learning of case factor weights [8].

Table 2  
![](/api/attachments/NBRUYUJK/fulltext/images/18baa225fc2d0826ac50e6fcd1333c5e60793199f7550addd428c7a96db4aeda.jpg)  
Fig. 4. Weights with combination of binary numbers.

In the early years, studies regarding forecasting mainly relied on statistical techniques such as exponential smoothing, regression model, autoregressive and moving average (ARMR), etc. in Refs. [3,4,9,10,21]. As time goes by, the internal and external environments for enterprises are becoming more and more complex. Traditional statistical prediction methods are no longer effective enough to deal with the problems. Therefore, more kinds of Artificial Intelligence algorithms were developed to face the change. Algorithms such as Artificial Neural Network (ANNs), Fuzzy method, CBR, Genetic Algorithm (GAs) and data envelopment analysis, etc. have been widely applied to many fields such as bankruptcy prediction [6,13], stock market prediction [2,15,18,23] and all kinds of sales prediction.

Description of notations

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Notation Description
M(T) Objective function of forecasting slow-selling books for set of T training cases
 $O_{I}$  Comparison of predicted result to actual result for case i: If the same  $O_{i}=1$ , different  $O_{i}=0$ $P_{i}$  Predicted result of case i in training cases: If case i is a slow-selling book then  $P_{i}=1$ ; otherwise it is a selling book and  $P_{i}=0$ $A_{i}$  Actual result of case i in training cases: If case i is a slow-selling book then  $A_{i}=1$ ; otherwise it is a selling book then  $A_{i}=0$ 
R Set of reference cases,  $R=\{r_{1}, r_{2}, ..., r_{n}\}$ 
T Set of training cases,  $T=\{t_{1}, t_{2}, ..., t_{k}\}$ $Y(r_{j})$  The result of case j of reference cases that is the most similar to case i of training cases,  $r_{j}=$  slow-selling book then  $Y(r_{j})=1$  otherwise  $Y(r_{j})=0$ $S_{ij}$  Similarity degree between case i of training cases and case j of reference cases
D Sum of distances between each weighted factors of training cases and reference cases
 $f_{jh}$  Value of factor h of case j in reference cases
 $f_{ih}$  Value of factor h of case i in training cases
 $w_{h}$  Weight of factor h in reference cases
</div>

There were so many researchers that have been comparing different prediction methods [16,17,20].

From the literatures reviewed, there is no study focusing on returning books forecast. Therefore, this study would like to focus on the book markets and develop an accurate and practical returning books forecasting model.

## 2.2. Integrated GAs and CBR

CBR is one of the emerging paradigms for designing intelligent systems. It shows significant promise for improving the effectiveness of complex and unstructured decision making. It solves new problems by adopting previously successful solutions to analogous problems. In general, the problem-solving life cycle in a CBR system consists essentially of the following four parts (see Fig. 1):

(1) Retrieving similar previously experienced cases whose problem is judged to be similar.

(2) Reusing the cases by copying or integrating the solutions from the cases retrieved.

(3) Revising or adopting the solution(s) retrieved as an attempt to solve the new problem.

(4) Retaining the new solution once it has been confirmed or validated.

Conventional CBR with the same weight for every factor does not reflect the real world situations, and the

Calculation of fitness values for a set of training cases

<table><tr><td>Training cases</td><td> $A_i$ </td><td> $P_i$ </td><td> $O_i$ </td></tr><tr><td> $BOOK_1$ </td><td>1</td><td>0</td><td>0</td></tr><tr><td> $BOOK_2$ </td><td>0</td><td>0</td><td>1</td></tr><tr><td> $\vdots$ </td><td></td><td></td><td></td></tr><tr><td> $BOOK_k$ </td><td>1</td><td>1</td><td>1</td></tr><tr><td>Total  $M(T)$ </td><td></td><td></td><td> $\sum_{i=1}^{k} O_i$ </td></tr></table>

![](/api/attachments/NBRUYUJK/fulltext/images/522946b7cb3ab46d91f24b76442be860c75f8d9fab6359dda330cb2598c7c8fb.jpg)  
Fig. 5. Groups of different cases for different models.

forecasting ability might be affected as well. Many scholars proposed other methods to adjust and improve the factor weights of CBR and mostly they applied the global search function of GAs to adjust the factor weights with very good results. Ref. [22] presented a machine learning approach using GAs to find an optimal or near optimal weight vector for the attributes of cases in case indexing and retrieving of CBR and was demonstrated by applications to corporate bond rating. They had shown that the approach supports effective retrieval of cases and increases overall classification accuracy rate significantly. Ref. [14] proposed a GAs approach to the maintenance of CBR systems and applied to stock market analysis. This approach automatically determined the representation of cases and indexes relevant attributes to grasp the rapidly changing environment around the system. Experimental results showed that their proposed approach significantly outperforms the conventional CBR model and the conventional ANNs model. Ref. [5] proposed a GA-CBR system to predict customerpurchasing behavior and tested with real cases provided by one worldwide insurance direct marketing company. The GAs based approach to determine the fittest weighting values for improving the case identification accuracy. Compared to the regression model, the GA-CBR method had better learning and testing performance. Ref. [11] introduced Genetic algorithm into traditional Question and Answer (Q&A) system and put forward a new architecture with Q&A engine which used the conception of case based reasoning. They proposed the GAs based CBR approach to determine the fittest weighting values for improving the case identification accuracy, and the experimental results showed that its prediction accuracy and efficiency was greatly improved by their GAbased CBR approach than other models.

Table 3  
Definition of selected factors

<table><tr><td>Factors</td><td>Definitions</td></tr><tr><td>1. Grade of Author</td><td>Based on past publishing records and sales volumes for one particular author, the indexes were divided into five grades A, B, C, D and E from good to bad represented by value 1, 2, 3, 4 and 5 accordingly.</td></tr><tr><td>2. Grade of Publisher</td><td>Based on the sales/return volumes and gross profit rate, etc., for one particular publisher, the indexes were divided into four grades A, B, C, and D from very good to bad represented by value 1, 2, 3, and 4 accordingly.</td></tr><tr><td>3. Hot or Slow Season of Publication Date</td><td>Based on Council for Culture Affairs (2000), Jan., Feb., Mar., Jul., Aug., Sep. and Oct. belong to Grade A (Hot Season), and rest of months belong to Grade B (Slow Season) by values 1 and 2 accordingly.</td></tr><tr><td>4. Sale Volumes for First Three Months</td><td>Average sales volume for the first 3 months.</td></tr><tr><td>5. Returning Rate</td><td>Average returning rate for the first 3 months.</td></tr></table>

![](/api/attachments/NBRUYUJK/fulltext/images/d985b012dd5d667c01517adc7383c5b0c1084a1d1d29d3dbf4bb59c874fd5582.jpg)  
Fig. 6. Illustration for data collecting period.

Table 4  
Standardized data samples

<table><tr><td>Cases</td><td> $f_{1}$ </td><td> $f_{2}$ </td><td> $f_{3}$ </td><td> $f_{4}$ </td><td> $f_{5}$ </td><td> $A_{i}$ </td></tr><tr><td>Book $_{1}$ </td><td>1</td><td>0</td><td>1</td><td>0.029070</td><td>0.36</td><td>0</td></tr><tr><td>Book $_{2}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.003577</td><td>0.61</td><td>1</td></tr><tr><td>Book $_{3}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.001737</td><td>0.70</td><td>1</td></tr><tr><td> $\vdots$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Book $_{k}$ </td><td>1</td><td>1</td><td>1</td><td>0.010246</td><td>0</td><td>0</td></tr></table>

From the literature reviewed in this section, the model by integrating GAs and CBR could increase the forecasting accuracy effectively. Therefore, a hybrid model by evolving CBR with GAs for reverse sales forecast of returning book is developed in this research. The detailed implementation procedure of the hybrid model is described in the following section.

## 3. Methodology

GAs and CBR are used in this research to build up an alarm list of slow-selling books and assisting system for returned book handling. The framework of GA/CBR forecasting model is shown in Fig. 2. The advantages of conveying implicit knowledge, comparing characteristics provided by CBR, and the function of random search by GAs providing different weights of factors could increase the accuracy of forecast. Four models are established in this research: Model A—Hybrid System of GAs and CBR, Model B—Conventional back propagation neural network (BPNN), Model $\mathrm { C } -$ Conventional CBR and Model D—Multiple-regression analysis. These four models are selected into this research for analysis and comparison.

## 3.1. Genetic algorithms

CBR emphasizes on how to describe and retrieve cases, and one of the crucial points is the combination of the weight for each characteristic factor. In this section, we will describe the process of using GAs to find the optimal weight for each factor in CBR (see Fig. 3).

Table 5  
Sample data for reference cases

<table><tr><td>Cases</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $f_4$ </td><td> $f_5$ </td><td> $A_i$ </td></tr><tr><td> $Book_{R1}$ </td><td>0</td><td>1</td><td>1</td><td>0.000208</td><td>0</td><td>1</td></tr><tr><td> $Book_{R2}$ </td><td>0.25</td><td>0.33</td><td>0</td><td>0.000451</td><td>0.07</td><td>0</td></tr><tr><td> $Book_{R3}$ </td><td>0.75</td><td>0</td><td>1</td><td>0.011913</td><td>0.3</td><td>0</td></tr><tr><td> $Book_{R4}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.000208</td><td>0.71</td><td>1</td></tr><tr><td> $Book_{R5}$ </td><td>0</td><td>1</td><td>1</td><td>0.001493</td><td>0.06</td><td>0</td></tr><tr><td> $Book_{R6}$ </td><td>0.5</td><td>0.67</td><td>1</td><td>0.002257</td><td>0.3</td><td>0</td></tr><tr><td> $Book_{R7}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.000069</td><td>0</td><td>1</td></tr><tr><td> $Book_{R8}$ </td><td>0</td><td>0</td><td>1</td><td>0.000695</td><td>0.21</td><td>1</td></tr><tr><td> $Book_{R9}$ </td><td>1</td><td>0.33</td><td>1</td><td>0.096690</td><td>0.02</td><td>0</td></tr><tr><td> $Book_{R10}$ </td><td>0</td><td>0</td><td>0</td><td>0.057201</td><td>0.19</td><td>0</td></tr></table>

The steps of finding the best combination are described as below:

Step 1. Encoding

Table 6  
Sample data for training case

<table><tr><td>Cases</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $f_4$ </td><td> $f_5$ </td><td> $A_i$ </td></tr><tr><td> $Book_{T1}$ </td><td>0</td><td>0</td><td>0</td><td>0.014934</td><td>0.3</td><td>0</td></tr><tr><td> $Book_{T2}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.000069</td><td>0</td><td>1</td></tr><tr><td> $Book_{T3}$ </td><td>1</td><td>1</td><td>1</td><td>0.015177</td><td>0.11</td><td>0</td></tr><tr><td> $Book_{T4}$ </td><td>0</td><td>0.33</td><td>1</td><td>0.005765</td><td>0.42</td><td>1</td></tr><tr><td> $Book_{T5}$ </td><td>0</td><td>0</td><td>0</td><td>0.043622</td><td>0.32</td><td>0</td></tr><tr><td> $Book_{T6}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.013198</td><td>0.52</td><td>1</td></tr><tr><td> $Book_{T7}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.003508</td><td>0.68</td><td>1</td></tr><tr><td> $Book_{T8}$ </td><td>0</td><td>0</td><td>0</td><td>0.043587</td><td>0.28</td><td>0</td></tr><tr><td> $Book_{T9}$ </td><td>1</td><td>0.67</td><td>1</td><td>0.035495</td><td>0.17</td><td>0</td></tr><tr><td> $Book_{T10}$ </td><td>0.25</td><td>0</td><td>0</td><td>0.047060</td><td>0.27</td><td>0</td></tr><tr><td> $Book_{T11}$ </td><td>0.5</td><td>0</td><td>1</td><td>1.006252</td><td>0.08</td><td>0</td></tr><tr><td> $Book_{T12}$ </td><td>0</td><td>0</td><td>0</td><td>0.034696</td><td>0.35</td><td>0</td></tr><tr><td> $Book_{T13}$ </td><td>1</td><td>0</td><td>0</td><td>0.007467</td><td>0.22</td><td>0</td></tr><tr><td> $Book_{T14}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.001702</td><td>0.7</td><td>1</td></tr><tr><td> $Book_{T15}$ </td><td>0</td><td>0</td><td>0</td><td>0.021741</td><td>0.33</td><td>0</td></tr><tr><td> $Book_{T16}$ </td><td>1</td><td>0</td><td>0</td><td>0.114055</td><td>0.22</td><td>0</td></tr><tr><td> $Book_{T17}$ </td><td>0</td><td>1</td><td>1</td><td>0.001389</td><td>0.12</td><td>0</td></tr><tr><td> $Book_{T18}$ </td><td>1</td><td>0.67</td><td>1</td><td>0.080019</td><td>0.59</td><td>0</td></tr><tr><td> $Book_{T19}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.010558</td><td>0.51</td><td>1</td></tr><tr><td> $Book_{T20}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.006356</td><td>0.69</td><td>1</td></tr><tr><td> $Book_{T21}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.002813</td><td>0.45</td><td>1</td></tr><tr><td> $Book_{T22}$ </td><td>0</td><td>0</td><td>1</td><td>0.006946</td><td>0.38</td><td>1</td></tr><tr><td> $Book_{T23}$ </td><td>0</td><td>1</td><td>1</td><td>0.013475</td><td>0.55</td><td>1</td></tr><tr><td> $Book_{T24}$ </td><td>1</td><td>0</td><td>0</td><td>0.013163</td><td>0.29</td><td>0</td></tr><tr><td> $Book_{T25}$ </td><td>0</td><td>1</td><td>1</td><td>0.006147</td><td>0</td><td>1</td></tr><tr><td> $Book_{T26}$ </td><td>0</td><td>1</td><td>0</td><td>0.012399</td><td>0.28</td><td>0</td></tr><tr><td> $Book_{T27}$ </td><td>0</td><td>0</td><td>0</td><td>0.033446</td><td>0.29</td><td>0</td></tr><tr><td> $Book_{T28}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.005071</td><td>0.53</td><td>1</td></tr><tr><td> $Book_{T29}$ </td><td>0</td><td>0</td><td>1</td><td>0.006286</td><td>0.43</td><td>1</td></tr><tr><td> $Book_{T30}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.007398</td><td>0.58</td><td>1</td></tr><tr><td> $Book_{T31}$ </td><td>0</td><td>0</td><td>1</td><td>0.005105</td><td>0.4</td><td>1</td></tr><tr><td> $Book_{T32}$ </td><td>1</td><td>1</td><td>1</td><td>0.001320</td><td>0.25</td><td>0</td></tr><tr><td> $Book_{T33}$ </td><td>0</td><td>1</td><td>1</td><td>0.000208</td><td>0</td><td>1</td></tr><tr><td> $Book_{T34}$ </td><td>1</td><td>1</td><td>1</td><td>0.005835</td><td>0.15</td><td>0</td></tr><tr><td> $Book_{T35}$ </td><td>0.25</td><td>0.67</td><td>0</td><td>0.014448</td><td>0.78</td><td>1</td></tr><tr><td> $Book_{T36}$ </td><td>0.5</td><td>0</td><td>1</td><td>0.100476</td><td>0.3</td><td>0</td></tr><tr><td> $Book_{T37}$ </td><td>0.5</td><td>1</td><td>1</td><td>0.008196</td><td>0.31</td><td>0</td></tr><tr><td> $Book_{T38}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.002223</td><td>0.66</td><td>1</td></tr><tr><td> $Book_{T39}$ </td><td>1</td><td>0.67</td><td>1</td><td>0.004897</td><td>0.39</td><td>1</td></tr><tr><td> $Book_{T40}$ </td><td>1</td><td>0.33</td><td>0</td><td>0.011114</td><td>0.23</td><td>0</td></tr><tr><td> $Book_{T41}$ </td><td>1</td><td>1</td><td>1</td><td>0.004619</td><td>0.27</td><td>1</td></tr><tr><td> $Book_{T42}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.000417</td><td>0.84</td><td>1</td></tr><tr><td> $Book_{T43}$ </td><td>0</td><td>0.33</td><td>1</td><td>0.005592</td><td>0.44</td><td>0</td></tr><tr><td> $Book_{T44}$ </td><td>0.5</td><td>0</td><td>1</td><td>0.059216</td><td>0.58</td><td>0</td></tr><tr><td> $Book_{T45}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.013198</td><td>0.52</td><td>1</td></tr><tr><td> $Book_{T46}$ </td><td>1</td><td>0</td><td>0</td><td>0.074706</td><td>0.09</td><td>0</td></tr><tr><td> $Book_{T47}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.002570</td><td>0.68</td><td>1</td></tr><tr><td> $Book_{T48}$ </td><td>0</td><td>0</td><td>1</td><td>0.005175</td><td>0.37</td><td>1</td></tr><tr><td> $Book_{T49}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.000035</td><td>0</td><td>1</td></tr><tr><td> $Book_{T50}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.003404</td><td>0.63</td><td>1</td></tr></table>

Table 7  
Sample data for testing cases

<table><tr><td>Cases</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $f_4$ </td><td> $f_5$ </td><td> $A_i$ </td></tr><tr><td> $Book_{S1}$ </td><td>0</td><td>0.67</td><td>1</td><td>0.005383</td><td>0.44</td><td>1</td></tr><tr><td> $Book_{S2}$ </td><td>0.25</td><td>0.67</td><td>1</td><td>0.061716</td><td>0.21</td><td>0</td></tr><tr><td> $Book_{S3}$ </td><td>0</td><td>1</td><td>0</td><td>0.002396</td><td>0.41</td><td>1</td></tr><tr><td> $Book_{S4}$ </td><td>0</td><td>0.33</td><td>1</td><td>0.000625</td><td>0</td><td>0</td></tr><tr><td> $Book_{S5}$ </td><td>0.25</td><td>1</td><td>1</td><td>0.008092</td><td>0.32</td><td>0</td></tr><tr><td> $Book_{S6}$ </td><td>0</td><td>0</td><td>0</td><td>0.002257</td><td>0.68</td><td>1</td></tr><tr><td> $Book_{S7}$ </td><td>1</td><td>0.67</td><td>0</td><td>0.069531</td><td>0.35</td><td>0</td></tr><tr><td> $Book_{S8}$ </td><td>0</td><td>0.67</td><td>0</td><td>0.003508</td><td>0.68</td><td>1</td></tr><tr><td> $Book_{S9}$ </td><td>0</td><td>0</td><td>0</td><td>0.024937</td><td>0.23</td><td>0</td></tr><tr><td> $Book_{S10}$ </td><td>1</td><td>0.33</td><td>1</td><td>0.051644</td><td>0.31</td><td>0</td></tr></table>

The most common encoding method for gene is binary number used as the original calculating system by computer. It is very convenient to operate the encoding, crossover and mutation steps of GAs. Each factor influencing book returning is assigned a weight with the combination of eight binary numbers shown in Fig. 4.

## Step 2. Generate the Initial Population

Initial weights are randomly generated between 0 and 1; these initial solutions form the first population. GAs operator will evaluate the weights in the chromosomes later.

## Step 3. Compute the fitness value

The purpose of finding the fitness value is to keep good chromosomes. The fitness value of each chromosome will be compared to the current best one, and if the new chromosome has a better fitness value, then the new one will be kept to produce the next offspring. The description of notations is listed in Table 1.

Table 2 shows a set of books in training cases to be forecasted if they are slow-selling books and the calculation of the fitness value for these set of books.

(1) Objective function:

$$
\max M (T) = \sum_ {i = 1} ^ {k} O _ {i}\tag{1}
$$

s.t.

$$
\begin{array}{l} O _ {i} = 1, \text {   if   } P _ {i} = A _ {i} \\ O _ {i} = 0, \text {   if   } P _ {i} \neq A _ {i} \end{array}
$$

(2) Calculation of $P _ { i }$

Table 8  
e value and average error rate

<table><tr><td>Item</td><td>Testing set</td></tr><tr><td>e</td><td> $k - \sum_{i=1}^{k} O_i = 10-9 = 1$ </td></tr><tr><td>Average error rate</td><td> $\frac{1}{m} \sum_{i=1}^{m} \frac{e_t}{k} = \frac{1}{10} = 0.1$ </td></tr></table>

Table 9  
e value and average error rate

<table><tr><td>Item</td><td>Testing set</td></tr><tr><td>e</td><td> $k - \sum_{i=1}^{k} O_i = 10-9 = 1$ </td></tr><tr><td>Average error rate</td><td> $\frac{1}{m} \sum_{t=1}^{m} \frac{e_t}{k} = \frac{1}{10} = 0.1$ </td></tr></table>

Let Set of reference cases $R = \{ r _ { 1 } , r _ { 2 } , . . . , r _ { n } \} , j = 1 , 2 ,$ …, n

Set of training cases $T = \{ t _ { 1 } , t _ { 2 } , . . . , t _ { k } \} , i = 1 , 2 . . . , k$

$$
P _ {i} = Y (r _ {j}), \text { if } S _ {i j} = \min _ {j} [ D (r _ {j}, t _ {i}) ]
$$

and

$$
D (r _ {j}, t _ {i}) = \sqrt {\sum_ {h = 1} ^ {m} w _ {h} (f _ {j h} - f _ {i h}) ^ {2}}, \qquad h = 1, 2, \dots , m
$$

m is the total number of factors.

Step 4. Compute the fitness value

The original concept of fitness is “the larger the better”, because solutions with larger fitness tend to propagate to the next generation. The objective function for the problem of slow-selling books forecast described in this research is to find the accuracy value which is also “the larger the better.” Therefore the objective function is fitness function for a set of training cases.

$$
\operatorname{fit} (T) = M (T) = \sum_ {i = 1} ^ {k} O _ {i}\tag{2}
$$

## Step 5. Reproduction/Selection

The roulette wheel selection method is applied in this research and the value of the fitness function represents the area proportion of each string on the roulette wheel, also represents the probability of being selected. Therefore, a chromosome with larger fitness function value means it has greater probability of being selected for crossover. The probability p(x) of each chromosome x will be chosen to re-produce as defined below:

Table 10  
e value and average error rate

<table><tr><td>Item</td><td>Testing set</td></tr><tr><td>e</td><td> $k - \sum_{i=1}^{k} O_i = 10-7 = 3$ </td></tr><tr><td>Average error rate</td><td> $\frac{1}{m} \sum_{t=1}^{m} \frac{e_t}{k} = \frac{3}{10} = 0.3$ </td></tr></table>

Table 11  
e value and average error rate

<table><tr><td>Item</td><td>Testing set</td></tr><tr><td>e</td><td> $k - \sum_{i=1}^{k} O_i = 10-8 = 2$ </td></tr><tr><td>Average error rate</td><td> $\frac{1}{m} \sum_{t=1}^{m} \frac{e_t}{k} = \frac{2}{10} = 0.2$ </td></tr></table>

$$
p (x) = \frac {\operatorname{fit} (x)}{\Sigma \operatorname{fit} (x)}.\tag{3}
$$

Step 6. Crossover

After the parameter design, two-point crossover method is applied in the research.

Step 7. Mutation

After the parameter design, one-point mutation method is applied in the research.

Step 8. Elite Strategy

Elite strategy is applied in this research in order to have bigger probability for good chromosomes to propagate excellent next generation. 30% of parent chromosomes and 70% offspring chromosomes are used in this research.

Step 9. Replacement

The new population generated by the previous steps updates the old population.

Step 10. Stopping criteria

If the number of generations equals to the maximum generation number then stop, otherwise go to step 3.

## 3.2. A hybrid system combining GAs and CBR

The working procedures of the hybrid system are listed as follows:

Step 1. Inputs of new case

Table 12  
Signal levels and codes of factors (Model A)

<table><tr><td>Code</td><td>Factor</td><td>Level 1</td><td>Level 2</td><td>Level 3</td><td>Level 4</td></tr><tr><td>A</td><td>Crossover rate</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td>B</td><td>Mutation rate</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td></tr><tr><td>C</td><td>Crossover</td><td>One point</td><td>Two points</td><td>One point</td><td>Two points</td></tr><tr><td>D</td><td>Mutation</td><td>One point</td><td>Two points</td><td>One point</td><td>Two points</td></tr></table>

Table 13  
S/N ratio (Model A)

<table><tr><td>Level</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>1</td><td>21.754</td><td>21.928</td><td>21.620</td><td>21.591</td></tr><tr><td>2</td><td>21.861</td><td>22.078*</td><td>21.959</td><td>21.499</td></tr><tr><td>3</td><td>22.051</td><td>21.923</td><td>22.133</td><td>21.839</td></tr><tr><td>4</td><td>22.310*</td><td>22.048</td><td>22.266*</td><td>23.048*</td></tr></table>

\* The best value selected under each level.

New case to be solved is the input in the CBR system in order to find out the solutions of related problem from the past case-base.

Step 2. Factor analysis of new case

Each new case is composed of many related characteristics, and the factor representing each case would be determined in this state. It is very important to select the related factors since the completeness of a case could influence the computing outcome. Five basic factors include the grade of the author, the grade of the publisher, hot or slow season of the publishing date, sales volume for first three months, and returning rate.

Step 3. Calculated Weight of Factors

Apply GAs approach to find the optimal weight for each factor.

Step 4. Find out the most matching case from reference cases for the new case using similarity rule.

This stage would find out the most matching case from reference cases using similarity rule in order to predict the possible slow-selling book for the new case.

$$
S _ {i j} = \min _ {j} [ D (r _ {j}, t _ {i}) ]\tag{4}
$$

$$
D (r _ {j}, t _ {i}) = \sqrt {\sum_ {h = 1} ^ {m} w _ {h} (f _ {j h} - f _ {i h}) ^ {2}}\tag{5}
$$

Step 5. Case Adaptation

After the steps above, the most matching case from reference cases is selected and it would have the most similarity to the new case. K-Nearest Neighbors are added to gain more matching cases from reference cases. k numbers of best matching cases from reference cases are produced by K-Nearest Neighbors. We set k = 5 in this research, and determine the new case result to be the same as most results of 5 best matching case from reference cases. For example, the new case would be slow-selling book if the 5 most matching case from reference cases are mostly slow-selling books.

Table 14  
Signal levels and codes of factors (Model B)

<table><tr><td>Code</td><td>Factor</td><td>Level 1</td><td>Level 2</td><td>Level 3</td><td>Level 4</td><td>Level 5</td></tr><tr><td>A</td><td>Learning rate</td><td>0.1</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0.9</td></tr><tr><td>B</td><td>Reduced factor of learning  $rate^a$ </td><td>0.1</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0.9</td></tr><tr><td>C</td><td>Momentum</td><td>0.1</td><td>0.3</td><td>0.5</td><td>0.7</td><td>0.9</td></tr><tr><td>D</td><td>1st hidden layer</td><td>1</td><td>3</td><td>5</td><td>7</td><td>9</td></tr><tr><td>E</td><td>2nd hidden layer</td><td>0</td><td>1</td><td>3</td><td>5</td><td>7</td></tr></table>

<sup>a</sup> Learning rate (t)=reduced factor of learning rate × learning rate (t − 1).

Table 15  
S/N ratio (Model B)

<table><tr><td>Level</td><td>A</td><td>B</td><td>C</td><td>D</td><td>D</td></tr><tr><td>1</td><td>17.184</td><td>17.545</td><td>18.645*</td><td>18.079</td><td>17.877</td></tr><tr><td>2</td><td>17.357</td><td>18.013</td><td>18.127</td><td>17.925</td><td>18.679*</td></tr><tr><td>3</td><td>17.524</td><td>18.600</td><td>18.201</td><td>17.972</td><td>18.274</td></tr><tr><td>4</td><td>19.342</td><td>18.604*</td><td>17.893</td><td>18.535*</td><td>18.261</td></tr><tr><td>5</td><td>19.631*</td><td>18.275</td><td>18.173</td><td>18.527</td><td>17.948</td></tr></table>

\* The best value selected under each level.

## Step 6. Verifying the results

The forecasted values are either 0 or 1 (True/False Question), and average error rate is applied as the measurement to verify the forecasted results of training cases and testing cases. That is $e = k ^ { - } \textstyle \sum _ { i = 1 } ^ { k } O _ { i }$ and

$$
\text { Average   error   rate } = \frac {1}{m} \sum_ {t = 1} ^ {m} \frac {e _ {\mathrm{t}}}{k}\tag{6}
$$

k is the total number of cases in the test set for each experiment.

$e _ { \mathrm { t } }$ is the total number of forecasting errors for total k cases in experiment t.

m is the total number of experiments.

Average error rate is applied as the forecasting benchmarks to evaluate the accuracy of these four models in this research.

## 4. Problem description

## 4.1. Data description

In this research, the data were collected from a book wholesaler company in Taiwan. This company is one of the leading book wholesalers in Taiwan, and its distribution channels are widely spread out all around Taiwan. Books to be distributed by this company cover almost all categories in the market. Therefore, data collected in this research are quite representative for this industry.

The data are collected from May 01, 2002 to April 30, 2003, include a total of 904cases: 503cases of selling books and 401cases of slow-selling books. 904cases are randomly divided into reference cases, training cases and testing cases for different models as listed in Fig. 5 below. Reference cases and training cases were used in the GA/CBR returning books forecast system described in this research to find out the best weight for each factor. Testing cases were then used to verify the accuracy of this forecast system.

Data collecting time for each case would be nine months including actual sales volume for the first 3 months to be used as a factor in the forecast system, and the actual total sales volume for the 6 months coming afterward would be used as the base to define a book as a slow-selling book when total sales volume within that period is less then 5books (see Fig. 6). Therefore, total collecting time for actual sales volumes for these 904cases started from May 1, 2002 until January 31, 2004.

## 4.2. Data analysis

According to the opinions of the experts from book related industries, seven factors that could influence book-returning volume were selected. The factors are the grade of the author, sales volumes for first 3 months, returning rate, and classification of books, price, the grade of the publisher, and the season (hot or slow) of the publishing date.

![](/api/attachments/NBRUYUJK/fulltext/images/a966447ab09ac9ca0f80fbd040c06d399ec5e40510a1c6c347ceb37e1565afcc.jpg)  
Fig. 7. Learning times and average error rate.

Table 16  
Average error rate for Model A under different reference cases

<table><tr><td>Reference cases, training cases, testing cases</td><td>200,200,100</td><td>300,200,100</td><td>400,200,100</td><td>500,200,100</td><td>Mean</td></tr><tr><td>Average error ratea</td><td>0.101</td><td>0.054</td><td>0.062</td><td>0.043</td><td>0.065</td></tr></table>

<sup>a</sup> Average error rate is the result of ten calculations.

In order to prevent null factors or nuisance factors, stepwise regression of statistic is applied to choose accurate factors. The statistical software SPSS 10.0 was used for calculation; the most interrelated factor to the slow-selling books, which is grade of author, is introduced into the model. Then the second interrelated factor, grade of publisher, is introduced into the model as well. Two factors are being verified in the model, and the less significant forecasting factor will be rejected. The forecast ability is significant when factor grade of author and factor grade of publisher are added into this model, and both factors are not rejected. Repeat the calculation using stepwise regression and we reduce seven factors into five, and they are: grade of author, grade of publisher, hot or slow season of the publishing date, sales volume for first three months, and returning rate listed in Table 3 below.

## 4.3. Data standardization

The collected data could be qualitative data (including grade of Author, grade of Publisher and Season of Publication date) and quantitative data (including sales volume for first three months and returning rate). Therefore, the collected data has to be transformed into standardized form for further calculation.

(1) For the qualitative data (ordinal data)

The steps of standardizing ordinal data are listed as below:

a. For a feature value j and $j { \in } \{ N _ { 1 } , N _ { 2 } , N _ { 3 } \} , { \mathrm { e . g . } }$ , for a feature value such as grade of publisher and it can be divided as the following: $N _ { 1 } \colon$ very good; $N _ { 2 } { \mathrm { : } }$ good; $N _ { 3 } { \mathrm { : } }$ fair and $N _ { 4 } { \mathrm { : } }$ bad.

b. The feature j of a particular book i is $R _ { i j }$ and $R _ { i j } { \in } \{ 1 , 2 , 3 , . . . , t \} { \mathrm { c a } }$

$$
f _ {i j} = \frac {R _ {i j} - 1}{t - 1}\tag{7}
$$

$f _ { i j }$ is the standardized feature value for book i and t is the total number of grades for feature j.

(2) For the quantitative data

The steps of standardizing quantitative data are listed as below:

$$
F _ {i} = \frac {X _ {i} - \min (X _ {1} , X _ {2} , X _ {3} , \dots X _ {n})}{\max (X _ {1} , X _ {2} , X _ {3} \dots X _ {n}) - \min (X _ {1} , X _ {2} , X _ {3} \dots X _ {n})}\tag{8}
$$

X is actual number for each variable.

$F _ { i }$ is standardized value for book i.

After the standardization of these collected data, values of these five factors are standardized between 0 and 1 as shown in Table 4.

## 4.4. A case example for different forecasting models

A case example with 10reference cases, 50training cases and 10testing cases is applied to demonstrate the working procedure of various models, i.e., Model A, Model B, Model C and Model D. Detailed information of the models for reference cases, training cases and testing cases are listed in Tables 5–7.

(1) Model A (GA/CBR)

a. Weight value for each factor was calculated by GAs using CBR adopting sample data from reference cases in Table 5 and training cases in Table 6 after 500 generations. Weight values for each factor are listed as below: $w _ { 1 } = 0 . 7 2 5 5$ 2 $w _ { 2 } = 0 . 7 4 1 2$ , $w _ { 3 } = 0 . 0 3 9 2$ $w _ { 4 } = 0 . 0 9 4 1 , w _ { 5 } = 0 . 6 9 0 2$

b. Weight values produced above are then inputted to CBR for finding out the five most similar reference cases for each case in testing set as shown in Table 7. Only three most similar reference cases are found out as the forecast decision of GA/CBR for each case because the numbers of reference cases in this example are very few. For example, the three most similar reference cases for $\mathrm { B o o k } _ { \mathrm { S 1 } }$ of testing set are: $\mathrm { B o o k } _ { \mathrm { R 4 } } ,$ , Book and $\mathrm { B o o k } _ { \mathrm { R } 5 }$ with actual values of $^ { \circ } 1 ^ { \circ } , ^ { \circ } 1 ^ { \circ }$ and $" 0 "$ . Then the predicted value $( P _ { 1 } )$ of $\mathrm { B o o k } _ { \mathrm { S 1 } }$ of testing set is $^ { 6 6 } 1 ^ { , 5 }$ . The actual value $\left( A _ { 1 } \right)$ for $\mathrm { B o o k } _ { \mathrm { S 1 } }$ is $^ { 6 6 } 1 ^ { \mathfrak { s } }$ which matches the predicted value $( P _ { 1 } )$ , and then the outcome of the forecasting for this case $( O _ { 1 } ) \mathrm { i s } ^ { \infty } 1 ^ { \infty }$

Average error rates and Standard Deviations under 200training cases and 100testing cases for Model A, B, C and D

<table><tr><td>Item</td><td>Model A</td><td>Model B</td><td>Model C</td><td>Model D</td></tr><tr><td>Average error rate $^a$ </td><td>0.043*</td><td>0.084</td><td>0.112</td><td>0.148</td></tr><tr><td>STD $^b$ </td><td>0.024920</td><td>0.019079</td><td>0.021817</td><td>0.026000</td></tr></table>

Table 18  
Average error rate for Model A under different reference cases

<table><tr><td>Reference cases, training cases, testing cases</td><td>200,200,200</td><td>300,200,200</td><td>400,200,200</td><td>500,200,200</td><td>Mean</td></tr><tr><td>Average error rate $^a$ </td><td>0.084</td><td>0.083</td><td>0.051</td><td>0.060</td><td>0.069</td></tr></table>

<sup>a</sup> Average error rate is the result of ten calculations.

c. Calculation of e value and average error rate for these 10testing cases are shown in Table 8. Since there is only one experiment, m is equal to 1 and k is equal to 10 (10testing cases).

## (2) Model B (BPNN)

a. Predicted values produced by BPNN are continuous values (Y ), and a threshold value, i.e., 0.5, is applied to convert the output $Y _ { i }$ into 0 or 1 value. In other words, if $Y _ { i } \ge 0 . 5 , P _ { i } = 1$ , otherwise $P _ { i } { = } 0$ . For example, the predicted values $Y _ { 1 } { = } 0 . 5 3 4 8$ produced by BPNN for Book of testing set is found, then we determine the $P _ { 1 } = 1$ . The actual value $\left( A _ { 1 } \right)$ for $\mathrm { B o o k } _ { \mathrm { S 1 } }$ is $^ { \mathfrak { s } } 1 ^ { \mathfrak { s } }$ which matches the predicted value $( P _ { 1 } )$ , then the outcome of the forecasting for this case $( O _ { 1 } )$ is $^ { \mathfrak { s } } 1 ^ { \mathfrak { s } }$

b. Calculation of e value and average error rate for these 10testing cases are shown in Table 9. Again, m is equal to 1 and k is equal to 10.

## (3) Model C (Conventional CBR)

a. Weight values for five factors under conventional CBR are all the same. Then input these weight values into CBR to find out the five most similar training cases for each case in testing set as shown in Table 7. Only three most similar reference cases are found out as the

## Table 19

Average error rates and Standard Deviations under 200training cases and 200testing cases for Model $\mathrm { A } , \mathrm { B } , \mathrm { C }$ and D

<table><tr><td>Item</td><td>Model A</td><td>Model B</td><td>Model C</td><td>Model D</td></tr><tr><td>Average error rate $^a$ </td><td>0.051*</td><td>0.089</td><td>0.110</td><td>0.151</td></tr><tr><td>STD $^b$ </td><td>0.010909</td><td>0.016948</td><td>0.014221</td><td>0.026024</td></tr></table>

<sup>⁎</sup>: The smallest average error rate.  
<sup>a</sup> Average error rate is the result of ten calculations.  
<sup>b</sup> Standard Deviation, $\mathrm { S T D } = \surd \Sigma ( x - \bar { x } ) ^ { 2 } / n .$

forecast decision for each case in this example of CBR. For example, the three most similar training cases for $\mathrm { B o o k } _ { \mathrm { S 1 } }$ of testing set are: Book $_ { \cdot \mathrm { T 1 9 } } ,$ Book<sub>T6</sub> and $\mathrm { B o o k } _ { \mathrm { T 4 5 } }$ with actual values of $^ { 6 6 } 1 ^ { 9 } , \quad ^ { 6 6 } 1 ^ { , 9 }$ and $^ { \mathfrak { s } } 1 ^ { \mathfrak { s } }$ . Then the predicted value $( P _ { 1 } )$ of Book of testing set is $^ { \mathfrak { s } } 1 ^ { \mathfrak { s } }$ . The actual value $\left( A _ { 1 } \right)$ for Book is $^ { \mathfrak { s } } 1 ^ { \mathfrak { s } }$ which matches the predicted value $( P _ { 1 } )$ , and then the outcome of the forecasting for this case $( O _ { 1 } ) \mathrm { i s } ^ { \infty } 1 ^ { \infty }$

b. Calculation of e value and average error rate for these 10 testing cases are shown in Table 10.

## (4) Model D (Multiple Regression)

a. Data from training set as shown in Table 6 is applied to calculate the coefficient of each input variable in the multiple regression function listed below:

$$
\begin{array}{r l} Y _ {i} & = 0. 1 6 3 6 - 0. 4 8 8 1 f _ {i 1} + 0. 3 1 8 2 f _ {i 2} \\ & \quad + 0. 2 0 2 4 f _ {i 3} - 0. 2 9 4 5 f _ {i 4} + 0. 6 4 9 8 f _ {i 5} \end{array}
$$

b. Predicted values (Y ) are continuous values. Therefore, calculated values are transformed into 0 or 1 under the following rule: if $Y _ { i } \ge 0 . 5 , P _ { i } { = } 1$ , otherwise $P _ { i } { = } 0$ . For example, the predicted values $Y _ { 1 } { = } 0 . 8 6 3 4 3$ produced by above multiple regression function for Book of testing set is found, and then $P _ { 1 }$ is converted into 1. The actual value $\left( A _ { 1 } \right)$ for Book $_ \mathrm { \cdot T 1 }$ is $^ { 6 6 } 1 ^ { \mathfrak { s } }$ which matches the predicted value $( P _ { 1 } )$ , and the outcome of the forecasting for this case $( O _ { 1 } ) \mathrm { i s } ^ { \infty } 1 ^ { \infty }$

c. Calculation of e value and average error rate for these 10testing cases are shown in Table 11.

## 5. Experimental results and analysis

Major softwares used in this research include Minitab 13, VISUAL BASIC 6.0, Microsoft Access 2003 (Model A, C), Neural Works Professional II V5.20 (Model B) and Microsoft Excel 2003 (Model D).

## 5.1. Related parameters designed for the hybrid system

The processing time for GAs in globally searching for optimal weight of CBR among all these 904cases is far too long; therefore Taguchi experimental design is introduced to reduce the computational times without influencing the justice of the experiment. First of all, after a series of try and error analysis, the evolutional process of GAs is operated with 20 populations and 500 generations. Taguchi experiment design is then applied to decide other parameters, and higher Signalto-Noise (S/N) ratio represents better parameter combination, which is defined as,

Table 20  
Average error rate for Model A under different reference cases

<table><tr><td>Reference cases, training cases, testing cases</td><td>200,300,100</td><td>300,300,100</td><td>400,300,100</td><td>500,300,100</td><td>Mean</td></tr><tr><td>Average error ratea</td><td>0.083</td><td>0.083</td><td>0.064</td><td>0.035</td><td>0.066</td></tr></table>

<sup>a</sup> Average error rate is the result of ten calculations.

$$
\begin{array}{l} S / N = - 1 0 \\ \times \log \left(\frac {1}{n} \times \sum_ {i = 1} ^ {n} y _ {i} ^ {2}\right) \quad (\text { smaller   is   better }) \end{array}\tag{9}
$$

Where, n is the total number of experiment, y is the result of the ith test, $y _ { i } \in ( 0 , 1 ) , \forall _ { i } { = } 1 , 2 , . . . , n .$

The crossover rate, mutation rate, crossover and mutation mode settings are designed in different levels as shown in Table 12.

The experiments will be operated in total of 48times by repeating 16combinations of four factors and four levels in three times, and compute the S/N ratio of each factor in each level as shown in Table 13.

From Table 13, the best parameter combination can be found as A4–B2–C4–D4. These codes represent: crossover rate = 0.9, mutation rate = 0.2, two point's crossover, two point's mutation. In addition, the elitist replacement strategy will be applied in this research for fast convergence.

## 5.2. Related parameters designed for BPNN

In this section, the best parameters are designed for BPNN under Model B. Network structure is listed as below:

a. Input layer: five processing elements

b. Output layer: one processing element

c. Learning rule: Delta rule

d. Transfer function: Sigmoid function.

Taguchi experiment design is then used to select the best parameters for BPNN including learning rate, reduced factor of learning rate, momentum, numbers of hidden layers, and number of neurons under each hidden layer shown in Table 14. The result of higher

Signal-to-Noise (S/N) ratio presents better parameter combination. The experiments will be operated in total of 75times by repeating 25 combinations of five factors and five levels in three times, and compute the S/N ratio of each factor in each level as shown in Table 15.

From the Table 15, the best parameter combination can be found as A5–B4–C1–D4–E2. These codes represent: learning rate = 0.9, reduced factor of learning rate= 0.7, Momentum=0.1, number of neurons under first hidden layer =7 and number of neurons under second hidden layer = 1.

Try-and-error method is used to find out the best learning times, and the system becomes stabilized when learning times exceeds 150,000times with average error rate of 0.08. The learning times is set as 180,000 to make sure that each experiment can reach convergence (see Fig. 7).

5.3. Comparison and analysis of average error rate of each model

As shown in Fig. 5, various groups of training cases and testing cases will be applied in these four different models. Among those 904cases, three different groups of cases, i.e., (200,100), (200,200) and (300,100) representing the numbers of training cases and testing cases are set up for experimental tests. Cases for each group are randomly selected each time from these 904cases and each group of experimental test is repeated for 10times.

(1) Group 1: 200training cases and 100testing cases In Model A, reference cases must be calculated with training cases to find out the weight for each factor. In order to find the best result, the most suitable reference set for Model A must be found before compared with other models. Reference case numbers 200, 300, 400 and 500 are calculated and most suitable reference set for Model A is 500cases, as shown in Table 16. The comparison results of these four different models under 200training cases and 100testing cases are illustrated in Table 17.

Table 21  
Average error rates and Standard Deviations under 300training cases and 100testing cases for Model A, B, C and D

<table><tr><td>Item</td><td>Model A</td><td>Model B</td><td>Model C</td><td>Model D</td></tr><tr><td>Average error ratea</td><td>0.035*</td><td>0.089</td><td>0.106</td><td>0.162</td></tr><tr><td>STDb</td><td>0.012845</td><td>0.020224</td><td>0.025377</td><td>0.036551</td></tr></table>

<sup>⁎</sup>: The smallest average error rate.  
<sup>a</sup> Average error rate is the result of ten calculations.  
<sup>b</sup> Standard Deviation, $\mathrm { S T D } = \surd \Sigma ( x - \bar { x } ) ^ { 2 } / n .$

![](/api/attachments/NBRUYUJK/fulltext/images/8b497dd546c297c3dea0bdf2edba0890a2d40af995e39ee70c8cef9f8b060d1b.jpg)  
Fig. 8. Average error rate of four different models under different testing conditions.

Under this group, the most suitable reference set for Model A is 400cases, as shown in Table 18. The comparison results of these four different models under 200training cases and 200testing cases are illustrated in Table 19.

(3) Group 3: 300training cases and 100testing cases Under this group, the most suitable reference set for Model A is 500cases, as shown in Table 20. The comparison results of these four different models under 300training cases and 100testing cases are illustrated in Table 21.

From these intensive experimental tests, the following conclusions are summarized:

(1) The forecasted value which belongs to a binary value (0 or 1) in this paper indicates a book to be either as a selling book or a slow-selling book. Therefore, when the continuous value generated by Model B (BPNN) and Model D (Multi-Regression) is closer to 1, it means that the book tends to be a slow-selling book; to 0 a selling book. That explains how 0.5 is the threshold value in this paper.

(2) As shown in Tables 17, 19 and 21 and Fig. 8, Model A has the smallest average error rate under different groups of training cases and testing cases, indicating that Model A has better forecasting accuracy than other models. The order of forecasting ability, from high to low, is Model A, Model B, Model C and Model D.

(3) As shown in Tables 16, 18 and 20, the forecasting accuracy of Model A increases when the number of reference cases increases. This phenomenon indicates that Model A is highly sensitive to the number of reference cases. Even though the average error rate of 500reference cases under the group of 200training cases and 200testing cases is slightly larger than that of 400reference cases. The difference of these two average error rates is as small as 0.009 indicating that they are almost the same. This study shows that the number of reference set can influence the forecasting accuracy of Model A. In addition, the average error rate of model A under different testing conditions is within the range of 3.5% up to 5.1%, which is quite robust and reliable.

(4) Factor weights are both adjusted under Model A and Model B. The weights are adjusted by fitness value under GAs in Model A and by bias under Model B. Model A has a better forecasting performance under various training cases and testing cases than Model B because GAs calculates factor weights by global searching.

(5) Model A with adjusted factor weights under GAs presents better forecasting ability than Model C, a conventional CBR system. This phenomenon indicates that adjusted factor weights could have better forecasting accuracy and better represent the real world situations.

(6) Model D has the worst forecasting ability compared to other three models because multiple-regression analysis methods perform better for linear problems. For non-linear problems as discussed in this research, Model D has weaker forecasting ability.

## 6. Conclusion

This research discusses how to integrate the GAs and CBR approaches to construct a hybrid system of returning books forecasting. It can help book wholesalers determine the advising list for returning books for the retailers and also the warning list of slow-selling books for publishers. There are so many new books being released each year in Taiwan, meanwhile so many book-returning problems being created. The advising list of returning books can help the space-limited book retailers to make best returning decision and also let the publishers have time to deal with the slow-selling books and make a win–win solution for all parties in the supply chain.

In summary, the contributions of this research can be concluded as the following:

1. In this study, Taiwan book market and book characteristics are analyzed and comprehended, and five factors influencing returning book volumes have been identified.

2. In this research, actual data instead of simulated data are collected for calculation, and the results of the research are more practical.

3. Models A, B and C have not been applied for slowselling book forecast in the past, and from the experimental tests these models can help book wholesalers to advise the retailers to make speedy and accurate decisions upon what books should be returned. The upstream suppliers can also benefit from the forecasting results by reducing logistic costs.

4. The forecasting accuracy of GA/CBR (Model A) is better than other three models, and the average error rate of model A is very small which is between 0.035 and 0.051 for different testing conditions. The results show that Model A is very robust and reliable for slow-selling book forecasting.

5. The experimental results indicated the forecast ability for slow-selling books would increase under GA/ CBR method when the number of reference cases increased. It also indicated that the number of reference cases would affect the accuracy of forecasting ability of the hybrid system.

## Acknowledgements

The authors are grateful for an anonymous referee for his constructive comments and Shin-Yuan book wholesaler in Taiwan for generously providing the book data for us, which make this research possible.

## References

[1] A. Aamodt, E. Plaza, Case-based reasoning: foundational issues, methodological variations, and system approaches, Artificial Intelligence Communications 7 (1) (1994) 39–59.

[2] N. Baba, M. Kozaki, An Intelligent forecasting system of stock price using Neural Networks, Proceedings of the International Joint Conference on Neural Networks 1 (1992) 371–377.

[3] J.C. Chambers, S.K. Mullick, D.D. Smith, How to choose the right forecasting technique, Harvard Business Review 49 (1971) 45–79.

[4] C.W. Chase, Ways to improve sales forecasts, Journal of Business Forecasting 12 (3) (1993) 15–17.

[5] C. Chiu, A case-based customer classification approach for direct marketing, Expert Systems with Applications 22 (2002) 163–168.

[6] A. Cielen, L. Peeters, K. Vanhoof, Bankruptcy prediction using a data envelopment analysis, European Journal of Operational Research 154 (2004) 526–532.

[7] Council for Culture Affairs, The Research for Book Published Market in R.O.C. Council for Culture Affairs of the Executive Yuan of the Republic of China, 2000.

[8] W. Dubitzky, F. Azuaje, A genetic algorithm and growing cell structure approach to learning case retrieval structures, in: S.K. Pal, T.S. Dillon, D.S. Yeung (Eds.), Soft Computing in Case Based Reasoning, Springer-Verlag, London, 2001, pp. 115–146.

[9] E.B. Fliedner, B. Lawrence, Forecasting system parent group formation: an empirical application of cluster analysis, Journal of Operations Management 12 (1995) 119–130.

[10] M.M. Florance, M.S. Sawicz, Positioning sales forecasting for better results, Journal of Business Forecasting 12 (4) (1993) 27–28.

[11] Y. Fu, R. Shen, GA based CBR approach in Q&A system, Expert Systems with Applications 26 (2004) 167–170.

[12] C.W. Gross, Bridging the communications gap between managers and forecasters, Journal of Business Forecasting 9 (1988) 9–13.

[13] H. Jo, I. Han, Integration of Case-based forecasting, neural network, and discriminate analysis for bankruptcy prediction, Expert Systems with Applications 11 (4) (1996) 415–422.

[14] K.J. Kim, I. Han, Maintaining case-based reasoning systems using a genetic algorithms approach, Expert Systems with Applications 21 (2001) 139–145.

[15] H.M. Krolzig, J. Toro, Multiperiod forecasting in stock markets: a paradox solved, Decision Support Systems 37 (2004) 531–542.

[16] R.J. Kuo, K.C. Xue, A decision support system for sales forecasting through fuzzy neural networks with asymmetric fuzzy weights, Decision Support Systems 24 (1998) 105–126.

[17] R.J. Kuo, P. Wu, C.P. Wang, An intelligent sales forecasting system through integration of artificial neural networks and fuzzy neural networks with fuzzy weight elimination, Neural Networks 15 (2002) 909–925.

[18] W. Leigh, R. Purvis, J.M. Ragusa, Forecasting the NYSE composite index with technical analysis, pattern recognizer, neural network, and genetic algorithm: a case study in romantic decision support, Decision Support Systems 32 (2002) 361–377.

[19] G.S. LeVee, The key to understanding the forecasting process, Journal of Business Forecasting 11 (4) (1992) 12–16.

[20] C. Mair, G. Kadoda, M. Lefley, K. Phalp, C. Schofield, M. Shepperd, S. Webster, An investigation of machine learning based prediction systems, The Journal of Systems and Software 53 (2000) 23–29.

[21] G. Rice, E. Mahmoud, Political risk forecasting by Canadian, International Journal of Business Forecasting 6 (1990) 89–120.

[22] K.S. Shin, I. Han, Case-based reasoning supported by genetic algorithms for corporate bond rating, Expert Systems with Applications 16 (1999) 85–95.

[23] X. Wang, P.K.H. Phua, W. Lin, Stock market prediction using neural networks: does trading volume help in short-term prediction? Proceedings of the International Joint Conference 4 (2003) 2438–2442.

![](/api/attachments/NBRUYUJK/fulltext/images/d650c32cc373538e2efccfe3564b0ce2cd3d281772572f59ced4674347021adb.jpg)  
Dr. P. C. Chang received his MS and PhD degrees from the Department of Industrial Engineering at Lehigh University in 1985 and 1989. He is a professor of Yuan Ze University in Taiwan. His research interests include Production Scheduling, Sales Forecasting, Case Based Reasoning, ERP, Global Logistics, and Applications of Soft Computing. He has published his research works in several SCI journals, such as Decision Support Systems, Expert Systems

![](/api/attachments/NBRUYUJK/fulltext/images/6292ba7367cb7f2322073de94e89e2b6d828c5bda06a918f790a9eed09aa93f8.jpg)  
Mr. C. Y. Lai currently is a PhD student in the Department of Industrial Engineering and Management at Yuan Ze University in Taiwan. He is interested in Production Scheduling, Applications of Artificial Intelligence, Forecasting and Heuristics.

with Applications, European Journal of Operational Research, International Journal of Production Economics, Applied Soft Computing, Journal of Intelligent Manufacturing, Computers and Operations Research, etc.  
![](/api/attachments/NBRUYUJK/fulltext/images/e07a4f5f19ccc9f7250ec53ca678fe818121668a2a36ef0e4eaf0f00079136be.jpg)  
K. Robert Lai received his PhD in computer science from North Carolina State University, Raleigh, NC, USA, in 1992. In 1994, he joined Yuan Ze University, Taiwan, ROC, where he is now an associate professor. His current research interests are in computational intelligence, agent technologies, and mobile computing.
