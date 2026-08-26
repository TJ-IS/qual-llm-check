---
otero_id: 18943
otero_key: "HDD93M6J"
title: "Experimentation with a back-propagation neural network"
authors: "Ronald W. Lodewyck; Pi-Sheng Deng"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90042-r"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Experimentation with a back-propagation neural network

An application to planning end user system development

Ronald W. Lodewyck and Pi-Sheng Deng
California State University, Stanislaus, Turlock CA, USA

Neural networks utilize the paradigm of the human brain to acquire knowledge through a training process. The knowledge base is stored in the form of weighted interconnections between layer nodes; this allows the network to generalize. Computational experimentation with a back-propagation algorithm yielded useful information concerning the effect of several key model parameters on network training and performance. These findings are illustrated through the application of a modest sized three layer neural network to the planning of end user involvement in the development of information systems.

Keywords: Back-propagation algorithm; Neural networks; Connectionist models; Unstructured decision making; End user system development; Information system planning

![](/api/attachments/HDD93M6J/fulltext/images/9e49e278cbb38dd9f6683d8af8e754370cac6de0a31ff155decf526cce419daa.jpg)

Ronald W. Lodewyck is Professor and Chair of Computer Information Systems at California State University, Stanislaus. He received his Ph.D. in Industrial Engineering and Management Science from Northwestern University. His current research and consulting interests include information systems planning, procurement information systems, applied artificial intelligence, and applications of information systems technology to assist the severely physically disabled.

Correspondence to: Professor R.W. Lodewyck, School of Business Administration, California State University, 801 West Monte Vista Avenue, Turlock, CA 95380, USA.

## 1. Introduction

The potential benefits and risks associated with end user developed information systems have been well documented $[1,3,10,12,15]$ . However, the incorporation of end user development into the information system planning process is not so well understood. In particular, determining if a proposed project is appropriate for end user development is often an unclear and difficult process. A common approach $[13]$ is to establish guidelines and standards for data access. The guidelines are intended to protect against problems such as inadvertent corruption or unauthorized dissemination of data. Presumably, only projects that adhere to the guidelines would be approved for end user development. The value of such an approach in the planning process is limited by the ability of management to assess the degree of conformance of the proposed project with the established guidelines. Evaluation of the tradeoff between benefits and risks of end user development is not addressed. This difficulty was identified by Henderson and Treacy $[5]$ who called to the research community to “(...) respond by providing the means to carry out evaluation and justification activities". We propose a new approach which takes into consideration both the advantages and disadvantages in determining whether a proposed information system project is an appropriate candidate for end user development.

![](/api/attachments/HDD93M6J/fulltext/images/0cda7158132b3a05aab571e144548050ffd26b474dd0425219ebcc78bc6957d3.jpg)  
gent data base systems, and the decision-theoretic approach to building expert system theory.

The neural network model, also known as the connectionist model, simulates the operation of the human brain. It can handle incomplete or fuzzy information, and is suitable for cases where generalization or inference is required. Neural networks have been successfully applied to many low-level cognitive tasks, such as speech recognition, signal processing, character recognition, and motor control $[4,14,16]$ . However, the potential of this approach has rarely been explored for a high-level cognitive task such as planning and decision support.

We propose a connectionist approach to the unstructured task of planning end user system development. A multilayer network is constructed as a knowledge base in which knowledge is distributed over the network in the form of weighted interconnections, and the back-propagation algorithm is used to modify the knowledge base from a set of given representative cases.

## 2. End-user development tradeoffs

End user development of information systems may yield substantial benefits. Principal among these are:

\- the user/developer has an intimate knowledge of the functional area and probably a better understanding of the need assuming that technology driven change will not occur to the process. This should translate into better specifications as well as a better user interface design;

– reduced development time;

\- reduced overall development cost.

End user developed systems also involve numerous risks to the organization such as:

\- possible corruption of existing data if the system ‘feeds’ an organization database.

\- the integrity of the data may be suspect if the system does not employ satisfactory controls on data entry;

\- the accuracy of output results may be suspect, especially if the system is not thoroughly tested before routine use;

\- the system may become burdensome to maintain if the application was not written from a recorded set of requirements in an organization standard language following structured programming techniques;

\- if the system was designed by and for a specific user, it may not be possible to share it throughout the organization;

– large recovery costs might occur if procedures are not designed and implemented with a reliable backup system;

\- the organization might be exposed to considerable legal costs and financial liability if the system supplies mandated information incorrectly to regulatory agencies or poor ‘expert’ advice to customers;

\- the organization might suffer losses due to fraud, sabotage, or error if the system is not designed with security controls taken into consideration.

The tradeoff between these benefits and risks needs to be analyzed before planning the development of a system by an end user. But how is it possible to perform such an analysis when some, if not all, of the variables involved are ‘fuzzy’ and not easily measured or compared? A connectionist model which is able to translate a set of system attributes into a strategy based on experience appears to have potential.

## 3. Connectionist systems

An artificial neural network is a computational structure modeled on biological processes; it has many names, such as: Connectionist models, parallel distributed processing models, or neuromorphic systems. Unlike the von Neumann computer, which performs a program of instruction sequentially, a neural network explores many competing hypotheses simultaneously, using a massively parallel network composed of many non-linear computational elements connected by links with variable weights. A neural network's knowledge is distributed over the multilayer network in such a way that a pattern of weighted interconnections accomplishes what is usually achieved by specification of explicit decision rules. Neural net models are usually specified in terms of the neuron-node characteristics, net topology, and a learning algorithm. Some of the popular models include: ADALINE, ART, Hamming Net, Hopfield Net, Kohonen Feature Map, and Multilayer Perceptron [2,6,9,11].

Each computational node $(i)$ in a neural net receives a set of inputs, $(x_{1}, x_{2}, \ldots, x_{K})$ , along with a set of corresponding weights, $(w_{1i}, w_{2i}, \ldots, w_{Ki})$ where $w_{ji}$ is the weight from node j to node i. The activation mechanism of the node determines the level of excitation by comparing the sum of these weighted inputs with the threshold value. This value is passed to the transfer mechanism to determine the output from the node. Popular transfer mechanisms include the sigmoid, hard limiter, and threshold logic functions [11].

Topology refers to the pattern of connectivity between nodes across a neural net. Nodes may be only locally connected to neighbors, fully connected to all other nodes, or sparsely connected to a few distant nodes. A neural net may be layered with feedforward connections from lower to higher layers, as in multilayer neural nets, or provided with recurrent feedback connections, as in fully connected networks. A recurrent feedback network may be unstable for certain conditions, while a feedforward network guarantees stability. An unstable network will have outputs that oscillate, or vary chaotically over time, or may even lock up to fixed values.

Our approach is based on a multilayer network topology. A multilayer feedforward network can form an arbitrarily complex decision region $[11]$ , and is capable of arbitrarily accurate approximations to arbitrary mappings $[7]$ . These capabilities render a multilayer neural net useful in dealing with different types of applications, including unstructured decision making.

The driving force of a neural net is its learning algorithm, which varies connection weights over time to improve performance based on current results and thus equips a neural net with adaptability. It is such change that provides a degree of robustness by compensating for minor variabilities in characteristics of the node. A multilayer network generally uses the back propagation learning algorithm, which is an iterative gradient descent algorithm designed to minimize the mean square error between the actual output of a multilayer feedforward net and the desired output.

![](/api/attachments/HDD93M6J/fulltext/images/b17a732088e9f73c1074e991ed3fab8dd7625d275735b61b6c8eecd4a0cdf21c.jpg)  
Fig. 1. Three layer network

## 4. A neural network for planning development

Planning for information systems development may be viewed as a neural network with a three-layer architecture consisting of input, hidden, and output layers, as shown in Figure 1. Though the architecture of multiple hidden layers is also possible, all of its functions can be accomplished by a three-layered network [8].

Each node in one layer is connected in the forward direction to every node in the next layer. Input here is a list of attributes recognized as important in planning end user development; it is denoted by a vector $(x_{1}, x_{2}, \ldots, x_{K})$ , where K is the number of nodes in the input layer. In this model we implement the threshold as a weight $w_{0}$ , for convenience. The continuous and differential sigmoid function is adopted as a node's transfer mechanism; it translates the activation value into an output value. Our system uses the back propagation learning algorithm to modify the weight associated with the connection between nodes. This strategy generates multiple output values: A set of strategies for planning end user development.

We illustrate the approach with a neural network consisting of 11 input nodes, H hidden layer nodes, and 4 output nodes. The input nodes are the attributes we identified as important to this planning task. In this example, we include qualitative attributes represented on a relative strength numerical scale from 0 to 1.

Each of the input attributes is denoted by $x_{i}$ ; they are defined as follows:

$x_{1}$ Potential exposure to fraud, sabotage or the disclosure of confidential information to unauthorized persons. A system which inputs and outputs only data which is public knowledge would have minimum sensitivity, while a system which processes secret military or bank account transaction data would have maximum exposure.

$x_{2}$ Potential liability caused by faulty output from the system. A closed, completely internal system would have minimum potential liability, while a system which generates mandated reports (e.g., taxation data) or advice (e.g., financial, health-related, or highly personal information) would have maximum potential liability.

$x_{3}$ Need for data entry control procedures to ensure correctness and check validity of input. A system which has no data entry input origination (simulations, or download data from a host system) would have a minimum need for such control, while a system which is to become the source for transactional data fed to the organization database would have a maximum need for data entry control procedures.

$x_{4}$ Span of use. A system used by one person would have a minimum span, while a multi-user system, possibly used by two or more departments, would have a maximum span of use.

$x_{5}$ Impact on organizational goals, such as profit or service level. The loss of the system for any reason (departure of the programmer/developer, sabotage, inability to recover application and/or data following system failure, etc.) would have an impact ranging from inconsequential (minimum) to mission critical (maximum).

$x_{6}$ Vulnerability. The degree to which the system can be disrupted, disabled, or compromised deliberately or inadvertently by either external or internal sources ranges from impenetrable (minimum) to vulnerable (maximum).

$x_{7}$ Functional competence. End user knowledge and experience with the application ranges from none (minimum) to expert (maximum).

$x_{8}$ Technical competence. End user knowledge and experience with information system development ranges from none (minimum) to expert (maximum).

$x_{0}$ Time frame. The time available for development of the system ranges from urgent (minimum) to no rush (maximum).

$x_{10}$ Technical sophistication of the system. The application might be very straightforward and easily implemented in a 4GL or other user oriented development language. On the other hand, the application might be quite complex or demanding from a technical perspective. For example, the application might be timing sensitive, require navigation through multiple layers of software, or require operating system commands or function calls. The system technical complexity can therefore range from straightforward (minimum) to extremely complex (maximum).

$x_{11}$ Cost to develop a new system, including all hardware, software, consultants, and employee time. The cost can range from insignificant (minimum) to major investment (maximum).

The output layer includes a set of planning strategies for system development in an end user development environment. We have used the letters A, B, C, and D as symbols to represent four strategies, as follows:

A Development by the end user with no assistance;

B Development by the end user with guidance and/or assistance from either internal or external consultants;

C Development is a joint effort involving both the end user and the MIS staff with overall project management responsibility resting with the MIS group;

D Development by the MIS group as a result of the customary statement of needs from the end user.

Output from the input layer is received by the hidden layer, which allows the hidden layer to develop complex feature detectors or internal representations. The number of nodes in the hidden layer is treated as a parameter of the network in this paper.

We used a set of representative projects, shown in Table 1, to train the system. While the inputs may range from 0–1, we restricted them to a range from 0.1–0.9 in order to increase the likelihood of convergence of the learning algorithm.

The values may be explained as follows: Project 1 would be a good candidate for end-user development since functional and technical competence are very high ( $x_{7}=x_{8}=0.9$ ), but all other factors are very low. Conversely, project 4 would be a good candidate for professional MIS group development since end user competence is very low ( $x_{7}=x_{8}=0.1$ ), and all other factors are very high. Project 2 may be undertaken by the end user who has a moderate level of competence ( $x_{7}=x_{8}=0.7$ ), but ought to receive professional guidance and assistance to ensure conformance with organizational standards. Project 3 is a moderately sophisticated ( $x_{10}=0.5$ ) multi-user system ( $x_{4}=0.9$ ) with some time urgency ( $x_{9}=0.5$ ) which would probably be best undertaken as a joint effort to take advantage of the benefits of heavy end user involvement, but reduce the risks by assigning the MIS group overall project management responsibility.

Table 1
Training cases

<table><tr><td rowspan="2">Inputs</td><td colspan="4">Project</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td> $x_{1}$  exposure</td><td>0.1</td><td>0.2</td><td>0.5</td><td>0.9</td></tr><tr><td> $x_{2}$  liability</td><td>0.1</td><td>0.2</td><td>0.5</td><td>0.9</td></tr><tr><td> $x_{3}$  entry_control</td><td>0.1</td><td>0.2</td><td>0.5</td><td>0.9</td></tr><tr><td> $x_{4}$  span</td><td>0.1</td><td>0.1</td><td>0.9</td><td>0.9</td></tr><tr><td> $x_{5}$  impact</td><td>0.1</td><td>0.2</td><td>0.5</td><td>0.9</td></tr><tr><td> $x_{6}$  vulnerability</td><td>0.1</td><td>0.2</td><td>0.5</td><td>0.9</td></tr><tr><td> $x_{7}$  functional_competence</td><td>0.9</td><td>0.7</td><td>0.5</td><td>0.1</td></tr><tr><td> $x_{8}$  technical_competence</td><td>0.9</td><td>0.7</td><td>0.3</td><td>0.1</td></tr><tr><td> $x_{9}$  time_frame</td><td>0.1</td><td>0.2</td><td>0.5</td><td>0.9</td></tr><tr><td> $x_{10}$  technical_sophistication</td><td>0.1</td><td>0.2</td><td>0.5</td><td>0.9</td></tr><tr><td> $x_{11}$  cost</td><td>0.1</td><td>0.2</td><td>0.5</td><td>0.9</td></tr><tr><td>Desired output strategy</td><td>A</td><td>B</td><td>C</td><td>D</td></tr></table>

## 5. Parameter selection

Experiments were conducted to determine the effect of several key network parameters. Two issues were considered: Training time and performance. The time required to train the network can vary greatly depending on the selection of the learning rate ( $\alpha$ ), training tolerance (Tol), and hidden layer size (H) parameters. Training time is directly related to the number of training set iterations (runs) required until the weighting factors converge to within the specified training tolerance. The number of runs required is preferred to the time required, since it is independent of the speed of the computer used.

![](/api/attachments/HDD93M6J/fulltext/images/b33d6b7c3ba9d7113df47dd9c5e2c33e9258ff9a1cfdc403e090bfe0e7280350.jpg)  
Fig. 2. Runs versus learning rate

At first, the interconnection weights are randomly initialized. Training cases are fed into the system, and the back propagation learning algorithm is applied to iteratively modify the interconnection weights so that the error between the desired and actual outputs can be minimized.

The network was trained for successively increasing learning rates over the range 0.5–4 with the training tolerance fixed at 0.05 and hidden layer size fixed at 8 nodes. The number of runs required appears to be approximately inversely related to the learning rate, as seen in Figure 2. With the learning rate fixed at 1.0 and hidden layer size fixed at 8, the network was trained for successively increasing training tolerances over the range 0.001–0.2. Again, the number of runs appears to be approximately inversely related to the training tolerance, as seen in Figure 3. The network failed to converge if the testing tolerance is less than 0.005; this would imply an infinitely large number of runs. Finally, the learning rate was fixed at 1.0 and the training tolerance at 0.05, while the hidden layer size was varied from 4–50 nodes. As seen in Figure 4, training time is also inversely related to hidden layer size. If training time were the only consideration, the larger the value for learning rate, training tolerance, and hidden layer size, the better.

![](/api/attachments/HDD93M6J/fulltext/images/fb42fb37a3976428fc24ba9e5a3f55f51bace5028326dc70cbb234a2a7651d61.jpg)  
Fig. 3. Runs versus training tolerance

![](/api/attachments/HDD93M6J/fulltext/images/07eb706aa6113c064b26ed02bd2ceb28f53851596853252865e3f094b7d8b066.jpg)  
Fig. 4. Runs versus hidden layer size

The significance of parameter selection on the resulting trained network was also investigated by considering the effect on a measure of performance. A network which is able to perfectly generalize would yield an output with a neuron value of 1 for the 'correct' output node and 0 for all other 'incorrect' output nodes for all test cases presented to it. One measure of performance then would be the sum of the squared deviations from the perfect node values across all test cases.

$$
\mathrm{SSD} = \sum_ {i = 1} ^ {N} \left(1 - V _ {i c}\right) ^ {2} + \sum_ {i = 1} ^ {N} \sum_ {\substack {j = 1 \\ j \neq c}} ^ {M} V _ {i j} ^ {2},
$$

where N is the number of test projects; M is the number of output nodes; $V_{ic}$ is the neuron value of ‘correct’ node c for test project i; $V_{ij}$ is the neuron value of ‘not correct’ node j for test project i.

The SSD was measured for the suite of four test cases listed in Table 2 for each of the networks trained in the first part of the experimentation. Each trained network yielded a matrix of neuron values for each output node. An example outcome based on the trained network with the hidden layer size 8, learning rate 1.0, and training tolerance 0.05, is shown in Table 3. The outcome shows that strategy A is ranked as the most likely one for project 5, B for project 6, C for project 7, and D for project 8. This outcome coincides with our expectation, or recommended ‘correct’ strategy for these four test cases and suggests that the network is capable of generalization to new projects. Figures 5, 6 and 7 are graphs of SSD as a function of learning rate, training tolerance and hidden layer size, respectively. Somewhat surprisingly, learning rate and hidden layer size appear to have no predictable effect on the SSD. However, with the training tolerance varying over discrete values in the range 0.005–0.2, a relation to performance does appear. The graph suggests that the training tolerance should not be too small (the network cannot generalize very well) or too large (the network generalizes too broadly).

Table 2
Test cases

<table><tr><td rowspan="2">Inputs</td><td colspan="4">Project</td></tr><tr><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td> $x_{1}$  exposure</td><td>0.125</td><td>0.25</td><td>0.75</td><td>0.75</td></tr><tr><td> $x_{2}$  liability</td><td>0.125</td><td>0.25</td><td>0.25</td><td>0.75</td></tr><tr><td> $x_{3}$  entry_control</td><td>0.25</td><td>0.25</td><td>0.75</td><td>0.875</td></tr><tr><td> $x_{4}$  span</td><td>0.125</td><td>0.125</td><td>0.875</td><td>0.875</td></tr><tr><td> $x_{5}$  impact</td><td>0.125</td><td>0.25</td><td>0.75</td><td>0.875</td></tr><tr><td> $x_{6}$  vulnerability</td><td>0.125</td><td>0.25</td><td>0.5</td><td>0.5</td></tr><tr><td> $x_{7}$  functional_competence</td><td>0.875</td><td>0.75</td><td>0.875</td><td>0.125</td></tr><tr><td> $x_{8}$  technical_competence</td><td>0.875</td><td>0.75</td><td>0.125</td><td>0.125</td></tr><tr><td> $x_{9}$  time_frame</td><td>0.125</td><td>0.25</td><td>0.5</td><td>0.75</td></tr><tr><td> $x_{10}$  technical_sophistication</td><td>0.125</td><td>0.375</td><td>0.5</td><td>0.875</td></tr><tr><td> $x_{11}$  cost</td><td>0.125</td><td>0.375</td><td>0.5</td><td>0.75</td></tr><tr><td>Recommended ‘correct’ strategy</td><td>A</td><td>B</td><td>C</td><td>D</td></tr></table>

Table 3  
Example outcome

<table><tr><td rowspan="2">Output node</td><td colspan="4">Project</td></tr><tr><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>A</td><td>0.831</td><td>0.010</td><td>0.000</td><td>0.000</td></tr><tr><td>B</td><td>0.190</td><td>0.978</td><td>0.009</td><td>0.030</td></tr><tr><td>C</td><td>0.025</td><td>0.034</td><td>0.959</td><td>0.101</td></tr><tr><td>D</td><td>0.000</td><td>0.002</td><td>0.009</td><td>0.809</td></tr></table>

![](/api/attachments/HDD93M6J/fulltext/images/17dde173c989f4f97beb68abff0fa1c67c776d353c1d2974b04abbdd4362525b.jpg)  
Fig. 5. SSD versus learning rate

![](/api/attachments/HDD93M6J/fulltext/images/9878bd4384bc603e1c4608ce54e2b25fe1a46cb4a7cb178099f90b4a17b48948.jpg)  
Fig. 6. SSD versus training tolerance

![](/api/attachments/HDD93M6J/fulltext/images/12f6f6e2ae862b7e2d74f5c573e57b71e67a26de28a2e5ba0c6b61483fcbcb18.jpg)  
Fig. 7. SSD versus hidden layer size

No attempt was made at developing an optimization algorithm to find the best training tolerance level since it affects both learning time and network performance and the trade-off of these criteria will be application dependent.

## 6. Conclusion

In this paper we propose the application of neural networks to the planning of information system development in an end user environment, a high-level cognitive process. An example is used to illustrate this application. With the connectionist approach, it is possible to generate a knowledge base automatically from a set of historical cases, producing a system to ease the task of planning end user development. Our results show that the connectionist approach has potential as a decision support tool, especially as applied to unstructured decision making.

Since the goal of this paper was to show the potential and the feasibility of the application of neural networks to planning end user development, we simply give an example with a small set of hypothetical data to support our approach rather than use a large set of historical data. As the number of representative training cases increases, the system is expected to generate more reliable results, and its generalization capability is also expected to become more refined and 'educated'. We plan to extend this research by collecting, training, and testing the neural network with more empirical data and investigating the effect of various parameters, such as the learning rate, training tolerance and testing tolerance with respect to various measures of performance.

## References

[1] Alavi, M. and I. Weiss, ‘Managing the Risks Associated with End User Computing’, Journal of Management Information Systems, Winter, 1985.

[2] Carpenter, G.A. and S. Grossberg, 'The ART of Adaptive Pattern Recognition by a Self Organizing Neural Network', Computer, March, 1988, pp. 77–78.

[3] Davis, G.B., 'Caution: User Developed Systems Can Be Dangerous to Your Health', In: N. Ryan ed., End User Computing: Concepts, Issues, and Applications, John Wiley & Sons, New York, 1988.

[4] Gorman, R.P. and T.J. Sejnowski, 'Analysis of Hidden Units in a Layered Network Trained to Classify Sonar Targets', Neural Networks, Vol. 1, No. 1, 1988, pp. 75–89.

[5] Henderson, J.C. and M.E. Treacy, 'Managing End-User Computing for Competitive Advantage', Sloan Management Review, Winter, 1986, pp. 3–14.

[6] Hopfield, J.J., 'Neural Networks and Physical Systems with Emergent Collective Computational Abilities', Proceedings of the National Academy of Science, Vol. 79, 1982, pp. 2554–2558.

[7] Hornik, K., M. Stinchcombe and H. White, 'Universal Approximation of an Unknown Mapping and its Derivatives Using Multilayer Feedforward Networks', Neural Networks, Vol. 3, No. 5, 1990, pp. 551–560.

[8] Knight, K., 'Connectionist Ideas and Algorithms', Communications of the ACM, Vol. 33, No. 11, 1990, pp. 59–74.

[9] K. Kohonen, Self-Organization and Associative Memory, Springer-Verlag, Berlin, 1984.

[10] Laudon, K.C. and J.P. Laudon, Management Information Systems: a Contemporary Perspective, second edition, McMillan Publishing Company, New York; 1991.

[11] Lippman, R.P., ‘An Introduction to Computing with

Neural Nets', IEEE ASSP Magazine, April, 1987, pp. 4–22.

[12] Nolan, R.L. and G. Verdugo, ‘Renovating the DP Applications Portfolio’, reprinted in: Gray et al., eds., Management of Information Systems, Dryden Press, 1989.

[13] Senn, J.A., Analysis and Design of Information Systems, second edition, McGraw-Hill, 1989.

[14] Silverman, R.H. and A.S. Noetzel, 'Image Processing and

Pattern Recognition in Ultrasonograms by Backpropagation', Neural Networks, Vol. 3, No. 5, 1990, pp. 593–603.

[15] Sprague, R.H. and B.C. McNurlin, eds., Information Systems in Practice, Prentice-Hall, 1986.

[16] Stork, D., 'Self-organization, Pattern Recognition, and Adaptive Resonance Networks', Neural Network Computing, Vol. 1, No. 1, 1989, pp. 26–42.
