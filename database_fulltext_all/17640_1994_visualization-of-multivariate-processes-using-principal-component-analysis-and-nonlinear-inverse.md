---
otero_id: 17640
otero_key: "V2MPSGED"
title: "Visualization of multivariate processes using principal component analysis and nonlinear inverse modelling"
authors: "Petri A. Jokinen"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90065-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Visualization of multivariate processes using principal component analysis and nonlinear inverse modelling

Petri A. Jokinen

NESTE Engineering, Porvoo, Finland

Interpretation of the state of industrial processes is considered using principal component analysis as a visualization technique. A procedure for using the resulting two dimensional maps in detecting upsets and faults of the process is described. Nonlinear inverse models from the map coordinates back to the original process variables are studied and compared to linear modelling methods. Visualization techniques together with inverse modelling methods are shown to form a useful decision support system for the operating personnel of the plant. The visualization techniques and inverse modelling are studied using a simulated chemical process as an example.

Keywords: Principal component analysis; Fault detection; Fault diagnosis.

## 1. Introduction

Visualization of complex systems that consist of several tens of variables is necessary for persons that must interpret the status of such a system. Operating personnel of industrial processes could benefit greatly from good visualization techniques, because the number of measured variables from the process is constantly increasing. Process automation systems make it easy to collect vast amounts of data efficiently, but at the same time interpretation of variables and their dependencies becomes difficult.

Most visualization techniques are some kind of projection methods from multidimensional vector space to some low dimensional space. Two dimensional presentation of information is perhaps the most commonly used type and also intuitive for humans. Principal component analysis is one such projection method that can be used for visualization of multi-dimensional processes.

A common problem of all projection methods is that inversion from the projection coordinates back to the original variables is not unique. This in turn means that there is a need for a separate inverse model that connects the projection coordinates back to the original process variables. If such inverse model exists and can be estimated then it becomes possible to use the projection to a two dimensional plane as a map of the process state. Current state of the process is shown as a dot on the map and values of the process variables corresponding to the desired process state on the map can be computed using the inverse model.

Visualization techniques have been developed in the field of statistics and artificial intelligence at least. Examples of such methods are Andrews' curves [1] and Chernoff's faces [2] These methods are suitable for problems, in which the alternatives are examined to identify clusters and outliers for example [8]. It is still difficult to find rules for associating “good values of process variables” with “beautiful faces”. Some of these interpretation problems are avoided by using a simple principal component analysis technique. This paper investigates the use of principal component analysis for visualization of the state of a continuous chemical process. The inverse modelling problem from projected coordinates back to the original variables is also studied. For inverse modelling linear and nonlinear modelling methods are used.

This paper is divided as follows. The basic idea of principal component analysis as a visualization technique of multi-dimensional data is explained. Next, a nonlinear dynamically capacity allocating (DCA) network model is briefly discussed. This model is important for inverse modelling, because it can learn arbitrary continuous functions incrementally. The chemical process that is used as an example is then introduced and results showing the utility of this approach for monitoring and control of the process are presented.

## 2. Principal component analysis

Principal component analysis [9] of an m by n matrix X decomposes it into the sum of the products of n pairs of vectors. Each pair consists of a n dimensional loadings vector $p_{i}$ and a m dimensional score vector $t_{i}$ . This means that the original matrix X can be written as

$$
\boldsymbol {X} = \boldsymbol {t} _ {1} \boldsymbol {p} _ {1} ^ {\mathrm{T}} + \boldsymbol {t} _ {2} \boldsymbol {p} _ {2} ^ {\mathrm{T}} + \dots + \boldsymbol {t} _ {n} \boldsymbol {p} _ {n} ^ {\mathrm{T}}.\tag{1}
$$

The matrix of loadings vectors P, forms an orthogonal basis and the column vectors $p_{i}$ are the eigenvectors of the correlation matrix $R = X^{T}X$ . Each of the scores $t_{i}$ is simply the projection of X onto the basis vector $p_{i}$ :

$$
\boldsymbol {t} _ {i} = \boldsymbol {X p} _ {i}.\tag{2}
$$

Principal component analysis can be used for visualization of multivariate processes by computing the eigenvectors using some representative data set and projecting the new input vectors $x_{i}$ onto selected principal components. By selecting two principal components that correspond to the largest eigenvalues for example, we are able to use those as axes of a two dimensional “map”.

Each input vector $x_{i}$ is projected onto the selected vectors and is presented as a dot on the map.

While the map provides a view of the current state of a multivariate process, it is often desirable to be able to determine the values of the input variables based on any point of the map. This means that we should invert the model that was formed as a projection. Unfortunately this is not possible, because that inversion is not unique in general. To be more accurate, model inversion requires inversion of n by n rank one matrix and therefore the resulting inverse is not unique [9].

A separate inverse model can still be identified by using the map coordinates as inputs and process variables as outputs. Accuracy of this model may not be very good, but this problem of constructing inverse model is discussed using an example in section 4. For this purpose, one nonlinear modelling method is next introduced briefly.

## 3. DCA network structure

The dynamically capacity allocating (DCA) network model estimates the functional form as well as the model parameters simultaneously. In particular, these networks can be considered as an extension of kernel estimation methods, where the scalar valued function $f(x)$ is approximated using a linear combination of kernel functions $K(\cdot)$ :

$$
f (\boldsymbol {x}) = \sum_ {i = 1} ^ {k} b _ {i} K (\boldsymbol {x} - \boldsymbol {w} _ {i}).\tag{3}
$$

The DCA networks have a three layer feedforward connection structure. Figure 1 shows a network with 7 inputs, 3 hidden nodes and 2 outputs, that is, the approximated function is now a vector valued function. In this network, all outputs from the input layer are connected to all hidden nodes. If the current input pattern vector is x, the weights of node i are $w_{i}$ and A is a weighting matrix, then the output activation $h_{i}$ of hidden node i is

$$
h _ {i} = e ^ {(- 1 / 2 a) (x - w _ {i}) ^ {T} A (x - w _ {i})},\tag{4}
$$

where a is a positive scalar constant, x and $w_{i}$ are nx1 column vectors and A is a positive definite $n \times n$ square matrix. The outputs of all hidden nodes $h_i$ are used for calculating the $j$ th output of the network $O_j$

![](/api/attachments/V2MPSGED/fulltext/images/0242974c420d871950f822ee682b83625eebca91bf15fa7a4e349be8e9b1d60d.jpg)  
Fig. 1. Connection structure of the proposed DCA network.

$$
O _ {j} = \sum_ {i = 1} ^ {k} b _ {i j} h _ {i}.\tag{5}
$$

In all, this three layer connection structure of DCA networks corresponds to the kernel estimate of equation (3) with multivariate gaussian kernels given by equation (4). Hartman, Keeler et al. [3] have shown that this network structure is able to approximate any continuous function with arbitrary accuracy.

If the weighting matrix A is an identity matrix I then the distance metric in the exponent of $h_{i}$ is simply the Euclidean distance and the output activation function of each hidden node is symmetric with respect to all input pattern vector components. If the weighting matrix A is equal to the inverse of input pattern covariance matrix then it is a special case of the Mahalanobis distance that maximizes the separation between input pattern vectors x [9]. This selection of the distance function between stored and input pattern vectors is not the only possibility. Some other commonly used measures such as Hamming, Minkowski or Canberra metrics [9] could be used instead.

Equations (4) and (5) form a pair that can be written in the following form:

$$
f (\boldsymbol {x}) = \sum_ {i = 1} ^ {k} \boldsymbol {b} _ {i} G \big (| \boldsymbol {x} - \boldsymbol {w} _ {i} | _ {A} \big),\tag{6}
$$

where $G(|\cdot|_{A})$ is a radial Green's function. The Green's function is a solution of a regularized estimation problem, see Poggio and Girosi [10]. In their studies, the number of hidden nodes k have been fixed. The dynamically capacity allocating networks clearly have a close connection to the approximation theory of functions, but in this particular case k is the number of hidden nodes and is changed dynamically during learning to achieve better local interpolation performance. At the same time the structure of the approximating function $f(\cdot)$ changes.

For the dynamic allocation of hidden nodes during learning, each hidden node is defined to respond to a different region in the input pattern vector space. If the gaussian shaped activation function is cut at some height then the borderline of this cut defines an n-dimensional ellipsoid in the input pattern vector space. The equation of this n-dimensional ellipsoid is

$$
\left(\boldsymbol {x} - \boldsymbol {w} _ {i}\right) ^ {T} A \left(\boldsymbol {x} - \boldsymbol {w} _ {i}\right) = c.\tag{7}
$$

If the weight vector $w_{i}$ , weighting matrix A and the positive scalar constant c are defined then the constant a in equation (4) defines the steepness of the activation function response. Figure 2 shows some possible ellipsoid borders in a two-dimensional input pattern vector space. Identification of DCA network models is discussed in detail in a series of previous articles [5,6,7] by the author and therefore it is not repeated here.

![](/api/attachments/V2MPSGED/fulltext/images/c9d297e2b8057a817759eb3841ff98df6e47b7d8db54b3626ac835cefaf34607.jpg)  
Fig. 2. Ellipsoid bounds of 5 hidden nodes in the two dimensional input pattern vector space.

![](/api/attachments/V2MPSGED/fulltext/images/2487a222cd4223ebf4dbf8dfb25f16e3dca4cf3b378e8a0b2394663e59e48c85.jpg)  
Fig. 3. Schematic diagram of the studied chemical process.

## 4. Visualization of process state

Automated fault detection and diagnosis of industrial processes presents a significant challenge in engineering and software design. For a review of process fault detection methods see also Isermann [4]. This paper presents an application of principal component analysis to detection of abnormal and faulty process behavior. Venkatasubramanian et. al. [11] have used a simulated chemical process consisting of a reactor and a distillation column as an example and the same example process is used here. The schematic diagram of the process is shown in Figure 3.

The studied process consists of a jacketed continuously stirred tank reactor (CSTR) where an irreversible, exothermic first-order reaction $A \rightarrow B$ takes place. The reactor is provided with three control loops which control the outlet temperature, the reactor holdup and the outlet concentration. This reactor effluent stream containing a binary mixture of A and B is fed into the distillation column where it is separated into a distillate stream containing 98% A and a bottoms stream with 2% A. The distillation column is provided with controllers for the overhead and bottoms product compositions by manipulating the reflux rate R and the vapor boilup rate $V_{a}$ , respectively.

Table 1 presents the malfunctions that were identified in the plant. Faults $F_{1}-F_{6}$ are global, in the sense that they affect the operation of the entire plant. Faults $F_{7}$ and $F_{8}$ are local to the distillation column.

Table 1  
Identified fault types of the chemical process

<table><tr><td>Fault</td><td>Description</td></tr><tr><td> $F_1$ </td><td>High flowrate at reactor inlet</td></tr><tr><td> $F_2$ </td><td>Low flowrate at reactor inlet</td></tr><tr><td> $F_3$ </td><td>High concentration of A at reactor inlet</td></tr><tr><td> $F_4$ </td><td>Low concentration of A at reactor inlet</td></tr><tr><td> $F_5$ </td><td>High temperature at reactor inlet</td></tr><tr><td> $F_6$ </td><td>Low temperature at reactor inlet</td></tr><tr><td> $F_7$ </td><td>Bottoms composition controller failure</td></tr><tr><td> $F_8$ </td><td>Distillate composition controller failure</td></tr></table>

![](/api/attachments/V2MPSGED/fulltext/images/3f8cbd4776e68a5c357ae264f729e7873edd16cbd426c4da43d82bffc6cc6833.jpg)  
Fig. 4. Projection of the process state corresponding to normal operation and eight different fault conditions.

The state variables characterizing the plant were the concentration of A at reactor inlet C, the reactor effluent temperature T, the reactor holdup V, the reactor outlet flowrate F, the outlet temperature of the cooling water in the reactor jacket $T_{j}$ , the flowrate of the cooling water $F_{j}$ , the reflux rate R, the vapor boilup rate $V_{a}$ , the bottoms flowrate B, the distillate flowrate D, the bottoms product composition $X_{B}$ and the distillate product composition $X_{D}$ . These 12 variables were used for computing the eigenvectors of the data set. This data set consisted of examples that were corresponding to the normal operation of the plant and each of the faults in Table 1. Mean was removed from the observation matrix before computing eigenvectors and the two vectors corresponding to the largest eigenvalues were selected as axes.

![](/api/attachments/V2MPSGED/fulltext/images/fb6aa7e93fa524459b735915944e44d2388a76d594881de9b06306a9bcd67e1e.jpg)  
Fig. 5. Projection of the process state corresponding to normal operation and eight different fault conditions with noisy process measurements.

Figure 4 shows a two dimensional map of 12 dimensional process state. The axes that have been marked with “pc 1” and “pc 2” are the most significant principal component vectors. The dots marked with numbers 1–6 correspond to the process faults $F_{1}-F_{6}$ from Table 1. Dots 7–10 correspond to fault $F_{7}$ , 11–14 to fault $F_{8}$ and 15–20 to the normal operation of the plant. It can be seen that faults $F_{1}-F_{6}$ can be separated quite easily from the normal operating region. Faults $F_{7}$ and $F_{8}$ , in turn, are so similar to the normal operation that such identification can not be done using the map. This can be seen also from Figure 5 that was produced by adding noise to the process variables. Noisy data describes more accurately the situation in the industrial environment. Faults $F_{1}-F_{6}$ can still be identified, but the cloud of dots in the middle contains noisy process states corresponding to normal operation and faults $F_{7}$ and $F_{8}$ . This is a typical situation, it is not possible to detect all possible upsets of the process using a map, but many malfunctions can still be detected.

Percentage of explained variance of each process variable using a DCA network model and a linear model

<table><tr><td>Process variable</td><td>DCA network model</td><td>MLR model</td></tr><tr><td>C</td><td>99.1</td><td>60.6</td></tr><tr><td>T</td><td>65.4</td><td>-</td></tr><tr><td>V</td><td>51.7</td><td>-</td></tr><tr><td>F</td><td>97.2</td><td>90.4</td></tr><tr><td> $T_j$ </td><td>42.3</td><td>-</td></tr><tr><td> $F_j$ </td><td>100.0</td><td>99.7</td></tr><tr><td>R</td><td>98.4</td><td>91.7</td></tr><tr><td> $V_a$ </td><td>99.6</td><td>95.6</td></tr><tr><td> $X_B$ </td><td>45.2</td><td>-</td></tr><tr><td> $X_D$ </td><td>6.9</td><td>-</td></tr><tr><td>B</td><td>98.6</td><td>94.1</td></tr><tr><td>D</td><td>99.1</td><td>97.1</td></tr></table>

A natural question that arises while looking at these maps it what are the values of the process variables that are causing this behavior. It is easy

![](/api/attachments/V2MPSGED/fulltext/images/6c634542f156c1e371ee8adbc9c439a71394f142539cffd8f3e9853a18952a9f.jpg)  
Fig. 6. Prediction of concentration C on the basis of projected variables. Continuous line is true concentration, - - - - - is predicted by a DCA network model and $\cdot -\cdot -\cdot$ is predicted by the best linear model.

![](/api/attachments/V2MPSGED/fulltext/images/cdb3afeed3bde481296dbd5e3a360f633fd72a5061a602edeb892f2385d9058f.jpg)  
Fig. 7. Prediction of reactor effluent temperature T on the basis of projected variables. Continuous line is the true value, ---- is predicted by a DCA network model.

to tell the values of the variables at the current position of the map, but what about the neighborhood, for example. This calls for the inverse model and here a linear modelling method and DCA network model have been compared.

Table 2 shows the fraction of explained vari-

![](/api/attachments/V2MPSGED/fulltext/images/e9fa494803ec79480e44b1b9b3be19cd8d0ac03b4539d1c2d667682c2bb7bbae.jpg)  
Fig. 8. Prediction of reactor holdup V on the basis of projected variables. Continuous line is the true value, ---- is predicted by a DCA network model.

variable F

![](/api/attachments/V2MPSGED/fulltext/images/88e9763ddaeaf1dc878d20bfbdba5a2a7ecad35f6983045cc2c86b5be231d97a.jpg)  
Fig. 9. Prediction of reactor outlet flowrate F on the basis of projected variables. Continuous line is the true value, ---- is predicted by a DCA network model.

ance by each of the studied models. DCA network model is an incrementally learning nonlinear model and MLR is a simple multiple linear regression model. There are gaps in Table 2 that are shown with three dots. This means that the model was not able to explain the variance of the corresponding process variable at all. The DCA network model explained smaller fraction of the variance in case of these same process variables.

![](/api/attachments/V2MPSGED/fulltext/images/9c7280e154ca7e80304a14aa03e3fd0aa903c81fa4ff3a655f2ebc6913f68138.jpg)  
Fig. 10. Prediction of the outlet temperature of the cooling water in the reactor jacket $T_{j}$ on the basis of projected variables. Continuous line is the true value, -- - - - - is predicted by a DCA network model.

![](/api/attachments/V2MPSGED/fulltext/images/298f738f9955c060aa1592584bfc24eb6b9c3d5dbc9bd32d22b82e67acab2f01.jpg)  
Fig. 11. Prediction of the cooling water flowrate $F_{j}$ on the basis of projected variables. Continuous line is the true value, - - - - - is predicted by a DCA network model.

This is attributed to the fact that the variances of the process variables were not scaled to unity. The scaling might sound like a trivial thing, but in

![](/api/attachments/V2MPSGED/fulltext/images/e7de25717e363df77a1301d19a3f0f2e5adde71dd49ce8609d6069972cde37f3.jpg)  
Fig. 12. Prediction of the reflux rate R on the basis of projected variables. Continuous line is the true value, - - - - - is predicted by a DCA network model.

![](/api/attachments/V2MPSGED/fulltext/images/cd7574a3b5c767ab99f24044029dd631f34d429092c37d1312d1f2d916b7d159.jpg)  
Fig. 13. Prediction of the vapor boilup rate $V_{a}$ on the basis of projected variables. Continuous line is the true value, -- -- -- -- is predicted by a DCA network model.

fact it is not. While a data set is collected from the process we are able to calculate sample variance of the data set, but it seems to be that such variance is almost always incorrect due to the fact that within longer time period the variance is constantly increasing. This means that an attempt

![](/api/attachments/V2MPSGED/fulltext/images/f0961d8b1dc1d258cefc8e8ded5864761dc52eeb3953a3185cc170639c9b191d.jpg)  
Fig. 14. Prediction of the bottoms product composition $X_B$ on the basis of projected variables. Continuous line is the true value, -- - - - - is predicted by a DCA network model.

![](/api/attachments/V2MPSGED/fulltext/images/d4492bee57bc5f58a4bdfcfa254a80a61dea791efc06089dbcd1a0e7ab834aab.jpg)  
Fig. 15. Prediction of the distillate product composition $X_{D}$ on the basis of projected variables. Continuous line is the true value, -- - - - - is predicted by a DCA network model.

to make the variances of the process variables equal using sample variances is going to fail. The results of Table 2 therefore describe a fairly good approximation to the real situation and the results can be interpreted to indicate that inverse modelling using simple linear models is not feasible.

Figure 6 shows the true value of the concentration of substance A together with the estimated values using DCA network models and a multiple linear regression model. The DCA network model predicts accurately the changes in concentration C as it should based on the high percentage of explained variance (99.1%). The linear model estimates some of the jumps incorrectly to wrong direction and as a whole is able to estimate only the largest changes correctly. Figures 7–17 show the true process variables using continuous lines and the prediction of DCA network model using dashed lines. Some of the process variables can be estimated amazingly well using only the two coordinates of the map as input, but some are estimated poorly. For example reactor holdup signal V contains so much noise that the DCA network model is capable of predicting only the general trend of this signal, Figure 8. The result seem to be such that variables that contain most of the relevant variation can be estimated with fairly good accuracy and such variables that either contain a lot of noise or carry little information are neglected by the DCA network model.

![](/api/attachments/V2MPSGED/fulltext/images/4caaec5acd76ae9035cfbad22f8ed613b2c53e28331f931bebf5dab11514895d.jpg)  
Fig. 16. Prediction of the bottoms flowrate B on the basis of projected variables. Continuous line is the true value, ---- is predicted by a DCA network model.

variable D  
![](/api/attachments/V2MPSGED/fulltext/images/fed10d85eff8081bcc9ad163938a6d58bf6160d9e389254af6002348db719b53.jpg)  
Fig. 17. Prediction of the distillate flowrate D on the basis of projected variables. Continuous line is the true value, ---- is predicted by a DCA network model.

## 5. Conclusions

Visualization of multivariate industrial processes using principal component analysis has been described. This method provides a simple way to view the changes in the process state using two dimensional maps. These maps can be used to identify abnormal and faulty operation of the plant using visual information that has been extracted from a large number of process variables.

These maps can be used for setting desired operating points for the plant in terms of position on the map, but a separate inverse model is needed for that. The inverse model converts the map coordinates back to the original variables, which in turn can be used as set points for the controllers. This paper compared linear and nonlinear inverse modelling methods and nonlinear models were found to provide better performance.

This study has indicated that visualization of multivariate processes using principal component analysis coupled with nonlinear inverse modelling method can be used as a decision support system for process operators. It is also believed that this method can contribute to better quality control of products by making it possible to detect deviations in the process operation more quickly.

## References

[1] Andrews D., Plots of High Dimensional Data, Biometrics, vol. 28, pp. 125–136, 1972.

[2] Chernoff H., Using Faces to Represent Points in k-Dimensional Space Graphically. Journal of American Statistical Association, vol. 68, pp. 361–368, 1973.

[3] Hartman E., Keeler J.D., and Kowalski J.M., Layered Neural Networks with Gaussian Hidden Units as Universal Approximations. Neural Computation, vol. 2, no. 2, pp. 210–215, 1990.

[4] Isermann R., Process Fault Detection Based on Modelling and Estimation Methods-A Survey, Automatica, vol. 20, no. 4, pp. 387–404, 1984.

[5] Jokinen P.A., Neural Networks with Dynamic Capacity

Allocation and Quadratic Function Neurons, In Proceedings of International Workshop NEURO-Nimes '90, pp. 351–362, Nimes, France, 1990.

[6] Jokinen P.A., Dynamically Capacity Allocating Network Models for Continuous Learning, In Proceedings of International Conference on Artificial Neural Networks, ICANN-91, Helsinki, Finland, pp. 1153–1156, 1991.

[7] Jokinen P.A., A Nonlinear Network Model for Continuous Learning, Neurocomputing, vol. 3, pp. 157–176, 1991.

[8] Korhonen P., Using harmonious houses for visual pairwise comparison of multiple criteria alternatives, Decision Support Systems, vol. 7, no 1, pp. 47–54, 1991.

[9] Mardia K.V., Kent J.T., and Bibby J.M., Multivariate Analysis, Academic Press, London, 1979.

[10] Poggio T., and Girosi F., A Theory of Networks for Approximation and Learning, A.I. Memo No. 1140, MIT Artificial Intelligence Laboratory and Center for Biological Information Processing, July 1989, p. 84.

[11] Venkatasubramanian V., Vaidyanathan R., and Yamamoto Y., Process Fault Detection and Diagnosis Using Neural Networks – I, Steady-State Processes, Computers & Chemical Engineering, vol. 14, no. 7, pp. 699–712, 1990.
