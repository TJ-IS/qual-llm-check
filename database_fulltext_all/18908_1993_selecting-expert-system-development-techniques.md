---
otero_id: 18908
otero_key: "GXWZ88ZY"
title: "Selecting expert system development techniques"
authors: "Youngohc Yoon; Tor Guimaraes"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90017-n"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Selecting expert system development techniques

Youngohc Yoon

Southwest Missouri State University, Springfield, MO 65804, USA

Tor Guimaraes

Tennessee Technological University, Cookeville, TN 38505, USA

The widespread development of Expert System applications with a wide variety of characteristics raises a risk that development techniques and application types are not properly matched. This could lead to ES development and maintenance problems, and unnecessary costs for the organization. Four widely used ES development techniques are discussed in terms of basic characteristics and their strengths and limitations. The appropriate application of each technique is prescribed and the commercially available tools supporting the techniques are presented. IS managers and ES developers can use the information acquired and properly match ES development tools to applications targeted for ES use in their development.

Keywords: ES development techniques; Selecting development techniques; Inductive learning; Artificial neural network; Case-based reasoning; Model-based reasoning.

![](/api/attachments/GXWZ88ZY/fulltext/images/5f302f43f4fbdeb817fa98112ac61cc5515711aba36f8b2bd658d7eb42113d46.jpg)

Youngohc Yoon is an assistant professor in the Department of Computer Information Systems at Southwest Missouri State University. She received her M.S. from the University of Pittsburgh and her Ph.D. from the University of Texas at Arlington. She has recently published articles in the Journal of Neural Network Computing and Expert Systems. Dr. Yoon is a member of the Decision Sciences Institute, International Neural Network Society, American Association for Ar tificial Intelligence, ACM, SIGBDP, and IEEE Computer Society.

## 1. Introduction

Expert Systems (ES) are now widely accepted in business organizations. They have become critical components in many decision making and problem-solving processes $[23,9]$ . Widespread adoption and dependence on ES has, however, resulted in rising user expectations. An important challenge facing ES developers and managers is to improve the development process and enable quick construction of systems that are sophisticated, economical, evolvable, and, above all, satisfy user's demands and expectations. Lu and Guimaraes $[25]$ have addressed the selection of appropriate ES applications and development strategies in broader terms, using more detailed knowledge about the applications and how ES development techniques have performed in practice.

Expert systems using explicit decision rules extracted from domain experts are predominant today. However, the development process and resulting products suffer from serious limitations. First, the construction of a rule based ES has

![](/api/attachments/GXWZ88ZY/fulltext/images/d95ac9f16dd9774bd1a873d91fca854e6ca7cdb9afaaf39fcaa29627d1db52af.jpg)

sponsored by professional organizations including ACM, IEEE, ASM, DPMA, INFOMART, and Sales and Marketing Executives. He has consulted on several IS topics with many leading organizations including TRW, American Greetings, AT&T, IBM and the Department of Defense. He has published over fifty articles in leading journals such as Information Systems Research, Communications of the ACM, MIS Quarterly, Decision Sciences, OMEGA, Computers and Operations Research, Information and Management, and Database.

proved to be difficult in many cases since it requires developers to determine the decision rules of human experts and to represent them in an “if-then” format. In order to extract the decision rules, developers, who are relatively novices in the various domains, often fail to ask relevant questions and experience great difficulty in finding the domain knowledge. Due to the implicit nature of human knowledge [30], domain experts are often unable to articulate information requirements as well as they can use it [27]. This results in a lengthy process: the interviews and development process being time- and labor intensive task. Second, a sophisticated knowledge base must evolve from a simple one by adding new knowledge learned from experience; unfortunately, most conventional expert systems are incapable of learning through experience [10]. Finally, rules in conventional expert systems can have relationships with many other rules; when a rule is modified or a new rule is added, one has to worry about its effect on existing related rules. Thus a large conventional expert system can become unwieldy and difficult to maintain [1].

In order to overcome these limitations, researchers have explored various ES development techniques. The most promising are inductive learning, artificial neural networks, case-based reasoning, and model-based reasoning $[2,5,6,8,13,14,17,26,37]$ . The applications of these methods have demonstrated their potential, not only for resolving the bottleneck of knowledge acquisition but also for enhancing the capabilities of an ES and broadening the scope. Due to their superior performance, it is important that developers and Information Systems managers become familiar with the basic concepts, strengths and limitations of each ES method. No particular approach is consistently more effective. Each may be superior, depending upon the characteristics of the application domain and the available systems development resources. Therefore, understanding the profile of applications best suited to each method becomes very important.

## 2. Expert system application development techniques

Various ES techniques have been developed to cope with a broad range of domains. The four most promising techniques which have been demonstrated for effectively surmounting ES development problems are now discussed.

## 2.1. Inductive learning

Machine learning involves acquiring new knowledge through instruction or practice and organizing it in general, effective representations that improve the system performance. One branch of machine learning is “inductive learning” or “learning by example”; it is concerned with the development of concept descriptions (or classification rules) from examples.

Unlike the development of a conventional expert system, the developers of an inductive ES have to acquire a set of examples that human experts previously solved and then employ an inductive learning system to generate classification rules. The set of classification rules generated from the learning system is then used as the knowledge base of an inductive expert system. Therefore, the process of eliciting explicit classification rules from domain experts through interviews and observations becomes unnecessary. Various inductive learning algorithms exist, such as AQ [28], Version Space [29], ID3 [34], SPROUTER [15], and Thoth [36].

The most widely used inductive method is ID3. Its objective is to develop a decision tree that requires a minimum number of attribute tests for a set of examples [S]. Each example consists of a number of attributes and a predefined classification of the example. In order to minimize a decision tree, ID3 chooses the attribute whose discriminating power is largest among them and splits the examples into two sets, $[S_{1}$ and $S_{2}]$ according to the chosen attribute. A set, $[S_{i}]$ is then classified into two subsets by the attribute that has the largest discriminating power. The process is repeated until all examples are appropriately classified and/or no other attribute is available to be used for classification.

When calculating the discriminating power of each attribute, ID3 employs an information-theoretic approach adapted from communication theory which measures the expected information of a probability distribution P by:

$$
- \sum_ {x} P (x) \log P (x).
$$

![](/api/attachments/GXWZ88ZY/fulltext/images/d3e0ea571349ce2b84adc9078b43576f6a47bd6549979d170c0f2f1252f933cd.jpg)  
Fig. 1. A decision tree structure for partitioning examples.

Suppose a set S of training examples contains two classes, H and L. Let K denote the number of examples in class H in S and G denotes the number of examples in class L in S. An unseen example belongs to class H with probability $K/(K + G)$ and to class L with probability $G/(K + G)$ . When classifying a new example, a decision tree is regarded as the source of a message indicating the class of the example, H or L. According to information theory, the expected information associated with the message is given by:

$$
\begin{array}{c} M (S) = - K / (K + G) \log_ {2} K / (K + G) \\ - G / (K + G) \log_ {2} G / (K + G). \end{array}
$$

For an attribute with the alternative values of $A_{1}, A_{2}, \ldots, A_{n}$ , the attribute test, T, produces a partition $\{S_{1}, S_{2} \ldots S_{n}\}$ (Figure 1). Suppose $S_{i}$ contains $K_{i}$ examples of class H and $G_{i}$ examples of class L. The expected information of a branch $A_{i}, EI(A_{i})$ , is given by:

$$
\begin{array}{r l} E I (A _ {i}) = & - K _ {i} / (K _ {i} + G _ {i}) \log_ {2} K _ {i} / (K _ {i} + G _ {i}) \\ & - G _ {i} / (K _ {i} + G _ {i}) \log_ {2} G _ {i} / (K _ {i} + G _ {i}). \end{array}
$$

The expected information of all branches with T at its root can then be defined as:

$$
E (T) = \sum_ {i} \frac {\left(K _ {i} + G _ {i}\right)}{(K + G)} * E I \left(A _ {i}\right) \quad \text { for } i = 1 \text { to } n.
$$

The ratio $(K_{i} + G_{i})/(K + G)$ represents the proportion of the examples in S that belongs to $S_{i}$ . Thus, the information gained by performing the attribute test is given by $M(S) - E(T)$ . The next attribute to be tested is the one which gives the most information, i.e., the one for which $M(S) - E(T)$ is maximum.

In order to illustrate the inductive approach, consider the development of a risk classification system for capital project analysis. The risk of a project is determined by many factors: size, market, a project type, the national focus, the cost of the project, etc. A prototype ES classifies the risk of a project into one of two classes (High or Low), depending on the project type and the other risk factors. When using a conventional approach, the developer extracts classification rules from domain experts; whereas, in an inductive approach, the developer obtains a set of live examples (see Table 1) and applies an inductive algorithm like ID3 to those examples to generate classification rules. Consider the set of training examples that illustrate the process of generating a decision rule by ID3. The set S contains 11 examples in which 5 are in class H (High) and 6 are in class L (Low) in S, therefore,

$$
\begin{array}{r l} M (S) & = - 5 / 1 1 \log_ {2} 5 / 1 1 - 6 / 1 1 \log_ {2} 6 / 1 1 \\ & = 0. 9 9 4 0. \end{array}
$$

A Set of training examples used to illustrate the concept of ID3.

<table><tr><td>Project type</td><td>Product</td><td>Market</td><td>Focus</td><td>Classes</td></tr><tr><td>Replacement</td><td>Existing</td><td>Existing</td><td>International</td><td>Low</td></tr><tr><td>Replacement</td><td>Existing</td><td>New</td><td>Domestic</td><td>Low</td></tr><tr><td>Replacement</td><td>New</td><td>Existing</td><td>Domestic</td><td>Low</td></tr><tr><td>Replacement</td><td>New</td><td>Existing</td><td>International</td><td>High</td></tr><tr><td>Replacement</td><td>New</td><td>New</td><td>International</td><td>High</td></tr><tr><td>New</td><td>Existing</td><td>Existing</td><td>Domestic</td><td>Low</td></tr><tr><td>New</td><td>Existing</td><td>New</td><td>Domestic</td><td>Low</td></tr><tr><td>New</td><td>New</td><td>Existing</td><td>Domestic</td><td>Low</td></tr><tr><td>New</td><td>New</td><td>Existing</td><td>International</td><td>High</td></tr><tr><td>New</td><td>New</td><td>New</td><td>Domestic</td><td>High</td></tr><tr><td>New</td><td>New</td><td>New</td><td>International</td><td>High</td></tr></table>

![](/api/attachments/GXWZ88ZY/fulltext/images/041de51723b0af2bc5a242a2c404727a04149271a18b5d116d4ba2ba84111458.jpg)  
Fig. 2. A decision tree developed by ID3.

The information gained for the “Replacement” branch of an attribute test “Project Type” is as follows:

$$
\begin{array}{r l} E I \left(" \text {Replacement}"\right) & \\ = - 2 / 5 \log_ {2} 2 / 5 - 3 / 5 \log_ {2} 3 / 5 = 0. 9 7 0 \end{array}
$$

and for the “New” branch:

$$
\begin{array}{r l} E I \left(" \text {New}"\right) & = - 3 / 6 \log_ {2} 3 / 6 - 3 / 6 \log_ {2} 3 / 6 \\ & = 1. 0. \end{array}
$$

Thus the expected information for all branches of the attribute test is

$$
\begin{array}{r l} E (\text { ``Project Type'' }) & = 5 / 1 1 * 0. 9 7 0 + 6 / 1 1 * 1. 0 \\ & = 0. 9 8 6. \end{array}
$$

The information gained by testing the attribute “Project Type” is

$$
0. 9 9 4 0 - 0. 9 8 6 = 0. 0 0 8,
$$

which is negligible. Meanwhile, the information gained by testing the attributes “Product,”

“Market” and “Focus” is 0.4448, 0.0518, and 0.3113, respectively. Thus, the principle of maximizing the expected information gained from an attribute test leads us to select the “Product” as the first attribute to test and thus to form the root of the decision tree. Applying the same concept to the six examples which belong to the “New” branch of the attribute “Product” leads us to choose the “Focus” as the second test attribute and finally “Market” as the third; this yields the decision tree in Figure 2. The attribute “Project Type” is found unnecessary to classify the training examples. The decision tree is finally coded into a knowledge base in an “if-then” form to classify new examples.

## 2.2. Artificial neural network

Artificial Neural Network (ANN) research is based on the belief that human information processing takes place through the interaction of many billions of neurons, each sending excitatory or inhibitory signals to other neurons. A neuron in a human brain contains a nucleus, an axon, and one or more dendrites, as illustrated in Figure 3. The nucleus receives signals from other neurons through ramified dendrites, collects the input signal, and transforms the collected input signal. The single axon then transmits the transformed signal to other neurons, usually by the propagation of an “action potential” or “spike” [4]. The signals that pass through the junction, known as synapses, are either weakened or strengthened depending upon the strength of the synaptic connection. By modifying synaptic strengths, the human brain is able to store knowledge and thus allow certain inputs to result in specific output or behavior.

![](/api/attachments/GXWZ88ZY/fulltext/images/62770894f7f68bb277ecb0d77219916cd37a0be7a2f06f1375166ea6f41811a6.jpg)  
Fig. 3. A classical neuron.

In order to implement such human information processing in an artificial system, the basic ANN model consists of computational units which emulate the functions of a nucleus in a human brain cell $[24]$ . Computational units in an ANN are connected by links with variable weights which represent synapses in the biological model. The unit receives a weighted sum of all its inputs via connections and computes its own output value using its own output function. The output value is then propagated to many other units via the connection between units, as shown in Figure 4. Receiving units repeat the process. In real-world problems, a computational unit represents a parameter, and a connection weight represents the association between parameters, as shown in Figure 5.

Some researchers have recently explored the use of an ANN to resolve the difficulty of generating a knowledge base, and thereby developed a new construct called a connectionist expert system (CES) - an ES developed with an ANN approach [3,35]. Like an inductive approach, in lieu of decision rules elicited from a human expert, the CES approach obtains a set of training examples. This approach applies a learning algorithm to extract the functional relationships between input and output parameters and to encode them in the connection weights.

For example, supervised learning algorithms, like Back Propagation [33], require a set of attributes and a class identification for each training example. They use a gradient descent algorithm by which network connection weights are iteratively modified to reduce the difference between the system's classification and the expected classification over all examples. For the developmental process of a knowledge base, a set of weight is initially assigned at random. A collection of attributes then propagates forward to compute the output values of the output units. These are then compared to measure the error according to:

Fig. 4. The basic components of an artificial neural network model.  
![](/api/attachments/GXWZ88ZY/fulltext/images/8eecd6b9789f595127094e3e42201173700be4f4b42064637a7991561e2ce485.jpg)

$$
E = \frac {1}{2} \sum_ {j = 0} ^ {n} \left(D _ {j} - O _ {j}\right) ^ {2},
$$

where $D_{j}$ is the expected and $O_{j}$ is the actual output value. Finally, the differences are propagated back to the weights in order to reduce the error.

This procedure is repeated for a number of epochs for all training examples; an epoch is completed after the network processes all of the input and output pairs for all examples. When the change in weights becomes negligible, the iterative learning process is terminated. The mapping (from input to output) of what the ANN has learned is encoded in the magnitudes of the weights of the connections. The network whose connection weights accurately represent the processing function becomes a knowledge base for the ES. Thus, the knowledge base of a CES is a multi-layered network, and the pattern of weighted connections, produces implicitly what conventional ES developers must achieve by the specification of explicit decision rules.

The inductive approach and the ANN method are very similar in that both approaches use a set of examples to extract the decision rules. The major difference between these methods is that the final output of an inductive approach is an explicit decision tree in which a path can be traced, whereas the ANN approach produces an implicit network in which a decision path cannot be traced. Additionally, an inductive approach works with qualitative variables or quantitative variables whose values are categorized, while an ANN works with qualitative, discrete, or continuous quantitative variables.

## 2.3. Case-based reasoning

A Case-Based Reasoning (CBR) technique is based on the human information processing model in some problem areas; human experts depend heavily on memory of past experiences when solving new problems, particularly in law, diagnosis, and strategic planning $[31,32]$ . A CBR emulates this information processing model and maintains a historical case base. It retrieves cases relevant to the present problem situation from the case base and decides on the solution to the current problem on the basis of the outcomes from previous cases. In order to facilitate casebased reasoning, a case-based expert system (Figure 6) consists of several components which perform the necessary activities: a case base, a retriever, an adapter, a refiner, an executor, and an evaluator [21].

![](/api/attachments/GXWZ88ZY/fulltext/images/92d527bb998a827d46ca16f014bb2e8758e7041f6dcc9cfb1e41854d26b0e8b7.jpg)  
Fig. 5. The architecture of a connectionist expert system.

A case base functions as a repository of prior cases. The cases are indexed so that they can be quickly recalled when necessary. The knowledge source for a case-based system are previous cases solved by human experts. A case contains the general descriptions of old problems and solutions; whereas, an example in inductive learning is defined in terms of its attributes and its class.

When a new problem is entered into a case-based system, a search is instituted to find the features similar to the stored cases; the search involves indices to aid in retrieval. When relevant prior cases are found, an adapter examines the differences between these cases and the current problem, and then applies rules to modify the old solution to fit the new problem; this adapter employs structural and derivational methods. Structural adaptation applies rules directly to the old solution. Derivational adaptation reapplies rules that generated the old solution, creating a solution for the new situation. The method of derivation adaptation is to store the planning sequence that constructed the original solution along with its solution. When a case is retrieved for analysis and adaptation, the stored solution is therefore not changed directly but re-execution of the original solution process is initiated with the variables of the new problem statement.

A refiner then critiques the adapted solution against prior outcomes. One way to do this is to compare it to similar solutions of prior cases. If a solution exists for a different problem statement, then the system decides whether the solution is derived correctly. Alternatively, if a known failure exists for a derived solution, then the system must decide whether the similarities are sufficient to suspect that the new solution will fail.

Once a solution is critiqued, an executor applies the refined solution to the current problem, and an evaluator then analyzes the results. If they are as expected, no further analysis is made, the case and its solution are stored for use in future problem solving. However, if the results are not as expected, the case-based reasoner explains the failure and repairs it. In some situations, where the failure has been experienced before, the cause of the failure is explained and this guides the repair. In situations where the failure is unexpected, the repair occurs before the failure is formally explained. Repair and adaptation are similar in nature: a solution is modified to fit a problem statement. However, adaptation works with old solutions and new cases, while repair works with a solution, a failure report, possibly an explanation, and modifies the solution. Once a repair is made, a link is stored between the failed solutions and the one that finally worked. A case-based reasoning system can use such a link to determine whether there is anything in common with the original failed solution and the solution of a new problem.

![](/api/attachments/GXWZ88ZY/fulltext/images/296f820965c16fc760e0b411ca925aad7fbb65b32b1d9980565d1c8974f7d667.jpg)  
Fig. 6. The architecture of a case-based reasoning system.

![](/api/attachments/GXWZ88ZY/fulltext/images/4c936a78534395d9e26c9735a34f36d9aca05ecfd6ab5bf9f113dd92cbc3f1c7.jpg)  
Fig. 7. Fundamental idea of model-based reasoning.

Case-based systems must contain all components in order to solve the new problem. However, a developer may build a partial case-based system with only a case base and a retrieval subsystem if a domain is too complicated for development of all components. A partial system may not provide recommendations but can support decisions by providing relevant cases to the user. With a partial system, an end user must evaluate retrieved cases, determine their applicability to a current problem, and modify them to fit the problem.

## 2.4. Model-based reasoning

Manufacturing firms take measurements of processes in order to control product quality and prevent costly breakdowns. Similarly, fast, accurate fault diagnosis are needed for model-based reasoning techniques. A model-based system is a type of ES based on a model of the structure and behavior of the device that the system is designed to simulate [7]. Figure 7 illustrates the fundamental idea: the comparison of observation and prediction.

In model-based reasoning, observed behavior (what the device is actually doing) is compared with predicted behavior (what the device is supposed to do). The difference between them is called a discrepancy, and this indicates that a defect exists in the device. Then a process is initiated to diagnose the nature and location of the defect. Such a technique can be implemented to develop a model-based expert system if a real-world mechanical device exists whose behavior is observable, and a model can be built to simulate the structure and function of the mechanical device, and thus to make predictions about its intended behavior.

![](/api/attachments/GXWZ88ZY/fulltext/images/eb7d6e2101514e02b6eab3bf664468eea61eac7cb5ceb81a02aee08d878b6955.jpg)  
Fig. 8. A multiplier example of model-based reasoning.

To illustrate the concept of model-based reasoning, a device which contains three multipliers and two adders is used as an example (Figure 8). The values at the five inputs are given. The predicted value at output F is 12, but the observed value is 10 (inside brackets). The value at output G is predicted to be 12, and the actual value is 12. The diagnostic task must use knowledge about the structure and behavior of the components to determine which one could have produced the discrepancy at F. When diagnosing this, model-based reasoning techniques employs three steps: hypothesis generation, hypothesis testing, and hypothesis discrimination. The system first generates a set of suspected error points. These hypotheses can be generated in several ways. The simplest and most accurate way would be to suspect every component, but this is impracticable, another way is to consider only those components connected to the discrepancy. For example, only those components “upstream” from the discrepancy are suspect: i.e., MULTI-1, MULTI-2, and ADD-1.

After an hypothesis is generated, the system tests the suspected causes of error to determine which components could have failed, based on available observations of behavior. One of the approaches uses fault-model simulation. The fault model is created from a set of components that can malfunction. A simulation is run assuming that a component may malfunction as specified. If it malfunctions as specified, the hypothesis is retained; otherwise it is discarded. Another approach is based on the idea of fault corroboration, where only those components involved in the generation of incorrect prediction are considered for testing. For example, the correct output value at G is generated, indicating that the component, MULTI-2, functions properly; thus, it is eliminated from testing.

Almost always, more than one hypothesis remains after testing is completed. Therefore, hypothesis discrimination tests are conducted to distinguish between the remaining hypotheses. A probing technique is often used to accomplish this. The simplest form of probing involves starting the probe at the discrepancy and working upstream until a component is discovered producing the bad output from good input. For example, two components MULTI-1 and ADD-1 are probed in sequence to determine if one is a malfunctioning component. A disadvantage of this is the amount of time involved in the search: to improve search time, a binary search can be used. If available, one alternative involves considering the failure probabilities of the components and first consecutively test the components with the highest expected failure rates.

Table 2  
Comparing ES development techniques along selected variables.

<table><tr><td>Variables</td><td>ID3</td><td>ANN</td><td>CBR</td><td>MBR</td></tr><tr><td colspan="5">Input data</td></tr><tr><td>Required data</td><td>Examples</td><td>Examples</td><td>Cases</td><td>Design specifications</td></tr><tr><td rowspan="2">Input variables</td><td>Qualitative</td><td>Qualitative</td><td>Qualitative</td><td>Qualitative</td></tr><tr><td>Quantitative (Categorized only)</td><td>Quantitative</td><td>Quantitative (Categorized only)</td><td>Quantitative (Categorized only)</td></tr><tr><td colspan="5">Capabilities of a system</td></tr><tr><td>Generalization</td><td>Poor</td><td>Good</td><td>Good</td><td>Poor</td></tr><tr><td>Explanation power</td><td>Good</td><td>Poor</td><td>Excellent</td><td>Good</td></tr><tr><td>Development Support of Incremental Development</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Cost</td><td>Low</td><td>Medium</td><td>Medium</td><td>Medium</td></tr><tr><td>Difficulty</td><td>Low</td><td>Medium</td><td>Medium</td><td>Medium</td></tr><tr><td>Domain Problem structure</td><td>Well-defined</td><td>Ill-Defined</td><td>Ill-defined</td><td>Very Well-Defined</td></tr><tr><td>Appropriate domains</td><td>Diagnosis Instruction</td><td>Forecasting Interpretation Diagnosis</td><td>Planning Design Explanation</td><td>Fault Diagnosis Monitoring Control</td></tr></table>

The development of a model-based system involves the analysis of a device and the creation of a model to simulate it. A developer also has to find methods for hypothesis generation, testing, and discrimination.

## 3. Strengths and limitations of each method

Each of the ES development techniques have some advantages and disadvantages, as shown in Table 2. The inductive learning algorithm helps a knowledge engineer to develop a knowledge base from examples instead of eliciting decision rules from experts. The simplicity and efficiency of ID3 makes it a desirable alternative in the case of ES applications characterized by particularly demanding knowledge elicitation. With inductive learning, it becomes unnecessary for a knowledge engineer to study the concepts in the domain before moving on to the specification of decision rules. The time that knowledge engineers and domain experts must spend is significantly reduced by the inductive learning development technique, with a favorable impact on the cost/time associated with the development process. Additionally, the generation of explanations for an inductive expert system is relatively trivial, since its knowledge base employs explicit decision rules extracted from examples, indicating the decision path can be traced to disclose which variables and/or rules trigger a system's conclusion.

However, ID3 is not an incremental approach: new examples cause a decision tree to be discarded and redeveloped to accommodate new information. The method also does not guarantee the simplest decision tree, since the information-theoretical concept for choosing attribute tests is only a heuristic and cannot be optimized [19]. Furthermore, the input variables of ID3 should be qualitative and have a small number of possible values, since the efficiency and effectiveness of the algorithm can be significantly reduced when each possible value of the input variable represents a branch in a decision tree. Additionally, a continuous quantitative variable must be categorized to produce a finite number of branches, and a significant amount of information may be lost by classifying the variable.

Like an inductive learning approach, connectionist expert systems that use ANN learning algorithms are capable of generating a knowledge base from a set of examples. Regardless of the characteristics of input variables, ANN has been shown to be able to learn to generalize functional relationships between input and output, even though the relationships may be fuzzy, incomplete, or unclear [20]: the “learned” function is encoded in the interconnection weights of a multi-layered network and knowledge is distributed over the network, with connection weights representing implicit decision rules. This provides a more direct and effective mechanism to represent knowledge, where the implicit knowledge remains in an implicit form. In a comparison with an inductive learning method, a CES demonstrated slightly higher decision accuracy than ID3, regardless of knowledge domains [11].

A disadvantage of CES is that it cannot easily generate explanations $[18]$ : CES cannot explain decisions based on the underlying knowledge base Conventional ES and inductive systems employ explicit decision rules in an “if-then” format so that the system can be programmed to display the rules being used to reach a given conclusion. Connectionist expert systems use implicit decision rules which make such tracing very difficult. In addition, the CES technique does not support an incremental ES development approach, so new examples and new parameters result in redeveloping a completely new knowledge-based network.

The CBR development technique also facilitates the development of a knowledge base. Unlike a conventional ES, much of the knowledge needed for CBR is in the form of cases that are general descriptions of previous problems and solutions. Therefore, as long as historical cases are available, CBR may be useful for addressing ill-defined problems. A case-based system can easily incorporate new cases, thus facilitating the incremental development of an expert system. A small number of cases can initiate a case-based system, and the system can be gradually expanded as more are incorporated.

Maintaining a case-based system is easier than maintaining conventional expert systems, since case interactions are easier to understand. In a conventional expert system, for any rule change the developer is forced to analyze the interactions among all rules with relationships to the changed rule. Another important advantage of CBR is higher system efficiency. It uses individual or generalized cases to provide an explanation; thus, they are relatively simple to generate and more satisfactory than a conventional expert system. It can also propose solutions to problems quickly, requiring no time to derive answers from scratch $[22]$ . Remembering previous experiences (cases) is particularly useful in warning about potential problems, therefore, a case-based system can alert itself and users to avoid repeating past mistakes.

Although the CBR technique is found to have many advantages, its success depends largely on the quality of the indexing mechanism and consequent search technique. The match algorithm, including a way to deal with partial-matches, is critical. Last, enforcing cross-case consistency is quite difficult in a case-based system, since each case is defined separately and has no explicit relationship with others.

A major advantage of a model-based reasoning technique is its device independence. The process of knowledge acquisition starts from the ES design phase. The task of monitoring and diagnosing can therefore begin immediately, without waiting for human diagnostic expertise. Since its knowledge base is composed of a list of components and their functions, device modification poses no threat to diagnostic ability and the knowledge base is simply modified to reflect the changes $[12]$ . With a conventional expert system, device modification requires a major revision of the knowledge base. The development of a model-based expert system is likely to be less expensive, since it is not necessary to acquire knowledge from human experts. Given a design description for a device, diagnostic work can begin right away, and given a new design description for a different device, one can start to work just as quickly.

Of even greater value is the model-based system's ability to detect uncommon failures. A rule-based system relies on expert experience, which is likely to be focused on common malfunctions; the rare failure is doomed to obscurity and may not be appropriately diagnosed. A model-based system can reason and diagnose even the non-intuitive anomalies, since the system has extensive specifications used to build the device. A major limitation of the model-based reasoning approach is that it requires the complete specification of interaction between components.

## 4. Prescribing the application of each method

Each of the four techniques is applicable to different kinds of problems. The inductive techniques work best for applications where problem-solving knowledge can be represented by explicit rules, but the acquisition of explicit decision rules from human experts is difficult. The technique is applicable when there are many examples that jointly determine which course of action is to be recommended, and where an expert is available to verify the problem-solving process. An inductive technique would be a viable alternative to extract a set of rules from examples of problems. Each example should be defined in terms of attributes as well as its class identification; without a class identification, ID3 cannot create a decision tree.

The ANN approach is useful when the number of data points to be analyzed, or the range of values for each data point, is quite large or the reasoning about the data is fuzzy and ill-defined $[16]$ . A large set of examples must be available for the system to extract the mapping between input and output. CES is useful when examples are complete with no missing data, and the class identifications of examples are consistent.

The ANN approach provides a group of learning algorithms able to fit a broad range of problems. Some algorithms require attributes as well as class identifications; whereas, others require only attributes. Therefore, unlike inductive methods, the ANN approach is still applicable to a business problem where each available example does not have its class identification. Additionally, some ANN algorithms accept either continuous or discrete variables. In a business environment, CES is particularly useful in identifying the underlying pattern to be used for forecasting where the available data is so noisy, complex or highly variable over time that rule-based expert systems are impractical. An example would be the analysis of financial statements using financial ratios whose values are continuous and difficult to categorize without losing important information.

A CBR technique is applicable to solve problems and make decisions when the knowledge needed to solve the problem is so obscure that formulating domain rules is infeasible, but cases are available. CBR can also be used when rules can be formulated, but using them is expensive, because the rule base is large or the average rule chain is long. A case-based system is an effective approach when cases with similar solutions have similar problem statements. Problems dealing with classification, evaluation by comparison, explanation of anomalies, dispute mediation, planning, design, and repair are all good candidate applications for ES development using a case-based reasoning technique. In a business environment, CBR can be quite useful in developing ES which assist managers in strategic planning. Extracting the complete decision specifications for strategic planning is very difficult; however, a case-based reasoning approach enables the ES developer to augment the memory of a planner by providing the outcomes of prior cases relevant to a current plan and by supporting the decision-making processes through suggestions based on prior cases.

Finally, the MBR approach can be most useful in diagnosing problems; however, MBR is applicable only for problems that have a complete and accurate model. For example, a complete and accurate model for a human body cannot be built; thus the MBR technique is not appropriate to develop ES to diagnose human diseases. Also, if the problem constantly changes over time, it is impossible to construct a stable model for MBR.

Table 3  
A list of ES shells that support inductive, CES, CBR, or MBR techniques.

<table><tr><td>ES techniques and shells</td><td>Platforms</td><td>Developers</td><td>Cost</td></tr><tr><td colspan="4">Inductive learning</td></tr><tr><td>1st-Class</td><td>PCs: OS/2, DOSVAX VMS</td><td>AI Corp.</td><td>$995$2500-$45000</td></tr><tr><td>INDUCPRL</td><td>PC: DOS</td><td>OXKO</td><td>$95- $195</td></tr><tr><td>KDS 2 &amp; 3</td><td>PC: DOS</td><td>KDS</td><td>$1495</td></tr><tr><td>Rule Master</td><td>PC: DOS, OS/2VAX: Unix, VMS</td><td>Radian Corp.</td><td>$495- $2495$7500-$28000</td></tr><tr><td>Super Expert</td><td>PC: DOS</td><td>Softsync Inc.</td><td>$199</td></tr><tr><td>TIMM</td><td>PC: DOS</td><td>General Research Corp.</td><td>$1900-$19000</td></tr><tr><td>VP-Expert</td><td>PC: DOS</td><td>Paperback Software</td><td>$249</td></tr><tr><td>Xi Plus</td><td>PC: DOS</td><td>Inference Corp.</td><td>$995</td></tr><tr><td>Xpcrt Rule</td><td>PC: DOS</td><td>ATTAR Software</td><td>$950-$28000</td></tr><tr><td colspan="4">Artificial neural network</td></tr><tr><td>Neural Works</td><td>PC: DOS</td><td>Neural Ware, Inc.</td><td>$1895</td></tr><tr><td>Professional II Plus</td><td>SUN WS</td><td></td><td>$3995</td></tr><tr><td rowspan="2">NDS (Nestor Development System)</td><td>PC: DOS</td><td>Nestor, Inc.</td><td>$25000</td></tr><tr><td>SUN WS</td><td></td><td>$27000</td></tr><tr><td>ExploreNet 3000</td><td>PC: DOS</td><td>HNC</td><td>$1495</td></tr><tr><td>Brain Maker</td><td>PC: DOS</td><td>California Scientific Software</td><td>$795</td></tr><tr><td>Professional</td><td></td><td></td><td></td></tr><tr><td colspan="4">Case-based reasoning</td></tr><tr><td>CABARET</td><td></td><td>U. of Massachusetts at Amherst</td><td></td></tr><tr><td>RE: MIND</td><td>PC: DOSUNIXMacintosh</td><td>Cognitive System</td><td>$3000$5000$3000</td></tr><tr><td>CBR Express</td><td>PC: DOSSUN WS</td><td>Inference Corp.</td><td>$10000$12500-$15000</td></tr><tr><td colspan="4">Model-based reasoning</td></tr><tr><td>IDEA</td><td>PC: DOS</td><td>AI Square</td><td>$25000</td></tr></table>

The use of the MBR technique for device fault diagnosis has played a central role in broadening the scope of ES applications in engineering domains. However, any problem which is sufficiently well defined to enable the development of a causal model can benefit from this approach.

## 5. Conclusions and recommendations to IS managers

Given the widespread effort to develop ES in industry, the limitations of developing explicit decision rule ES, the large number of development tools available, and the wide variety of problems being addressed, there is considerable risk that ES developers will use development techniques inappropriate to their task.

IS managers must accept the need for development tools supporting all four major techniques. These are techniques whose strengths and weaknesses have been observed in practice. Only when experts are easily available and the decisions can be readily articulated is the conventional ES development preferred. The proper matching of development technique to specific applications is likely to produce cost reductions and system effectiveness well beyond the relatively small investment required for obtaining the tools. For a large organization, the cost of experimenting with these tools are insignificant and the potential benefits cannot be ignored. Smaller companies, unable to experiment concurrently with more than one shell, should select application areas most likely to benefit from ES development, and then select an ES shell which properly supports applications.

A number of ES shells are available to facilitate ES development. Depending on the maturity of the technique, the number of supporting commercial off the shelf (COTS) tools vary significantly. Inductive learning techniques have been used since the late 1970s and have enjoyed an abundance of supporting shells; whereas, MBR techniques are relatively in their infancy and have a single commercially available shell. Table 3 presents a list of COTS tools for ES development.

The inductive method employed by 1st-Class, INDUCPRL and Xi Plus is ID3; however, the underlying inductive algorithm employed in VP-Expert is not explicitly stated by the vendor. 1st

Class is one of the most popular inductive shells available. It allows users to create a table of examples and it generates rules from the table. INDUCPRL reads an ASCII table of examples and generates rules in the production-rule language for the LEVEL-5 and LEVEL-5 Object. Xi Plus provides a routine named Xi Rule that derives rules from examples. VP-Expert uses a command named INDUCE to construct rules from examples. Other COTS tools include Rule Master and TIMM which are large inductive tools to develop rules from a large number of examples. Small inductive tools, such as Super Expert, and KDS 2 and 3 are also available. All of these inductive tools are very easy to use and easy to learn; an end-user, who has neither experience in ES development nor an in-depth knowledge can utilize the inductive tools to solve business problems if examples are available.

The CES tools are developed by a large number of software companies; only the four leading products are presented in this paper. ExploreNet 300 supports 21 different learning algorithms and runs under Microsoft Windows. The Nestor Development System (NDS) utilizes the Nestor Learning System (NLS) –a patented ANN learning algorithm. Neural Works Professional II Plus and Brain Maker Professional support various learning algorithms and provide interfaces with ASCII files produced by Lotus 1-2-3, dBase III, Excel, and other products. Again, all of these software products require no programming to operate most applications and are easy to learn and to use. However, unlike inductive systems, the development of a CES requires the in-depth understanding of a chosen ANN learning technique, since the results from the system depend on several parameters, and those parameters should be well tuned in order to obtain an optimal solution. Another resource necessary for constructing a CES is a math coprocessor. Its development usually consumes relatively large amounts of CPU time due to the heavy computations. Math coprocessors are strongly recommended to speed up the development process and operation of a large CES.

Compared to the large number of tools available in inductive and ANN approaches, only a few COTS tools are available for implementing CBR techniques. Inference Corporation recently released Case-Based Reasoning Express which facilitates a case-based expert system. The software allows a developer to construct knowledge bases by entering case histories. It then searches for prior similar cases and applies those solutions to new problems. Other systems, RE: MIND, developed by Cognitive Systems and CABARET from the University of Massachusetts at Amherst, perform similar functions. They are very sophisticated and their users will need extensive training. Last, MBR development techniques are still at an early stage, with only one supporting COTS shell. Most MBR applications have been developed jointly with universities, and LISP or Prolog have usually been used to implement the systems.

## References

[1] T.J.M. Bench-Capon, Knowledge Representation: An Approach to Artificial Intelligence, Academic Press, London, 1990.

[2] J. Berger, “ROENTGEN: A Case-based Approach to Radiation Therapy Planning”, Proceeding of the Second Workshop on Case-based Reasoning, Pensacola Beach, Fl., 1989, pp. 218–222.

[3] D.G. Bound, P.J. Lloyd, B. Mathew, and G. Waddell, “A Multi-layer Perceptron Network for the Diagnosis of Low Back Pain”, Proceedings of the IEEE International Conference on Neural Networks, June 1988, pp. II-481–489.

[4] F. Crick, and C. Asanuman, “Certain Aspects of the Anatomy and Physiology of the Cerebral Cortex”, D.E. Rumelhart and J.L. McClelland (Eds.) Parallel Distributed Processing: Exploration in the Microstructure of Cognition, MIT Press, Cambridge, MA, 1986, pp. 333–371.

[5] F. Daube, and B. Hayes-Roth, “A Case-based Mechanical Redesign System”, Proceedings of the International Joint Conference on Artificial Intelligence, Detroit, 1989, pp. 1402–1407.

[6] R. Davis, “Diagnostic Reasoning based on Structure and Behavior”, Artificial Intelligence, Vol. 24, No. 3, 1984, pp. 347–410.

[7] R. Davis, and W. Hamscher, “Model-based Reasoning: Troubleshooting”, Schrobe, H.E. (Ed.), Exploring Artificial Intelligence: Surveying Talks from the National Conferences on Artificial Intelligence, Morgan Kaufman, San Mateo, CA, 1988.

[8] J. de Kleer, and B.C. Williams, “Diagnosing Multiple Faults”, Artificial Intelligence, Vol. 32, No. 1, 1987, pp. 97–130.

[9] E. Feigenbaum, P. McCorduck, and P. Nii, The Rise of the Expert Company, Time Life, Alexandria, VA, 1988.

[10] M.W. Firebaugh, Artificial Intelligence: Knowledge-based Approach, Boyd and Fraser Publishing Co, Boston, MA, 1988.

[11] D.H. Fisher, and K.B. McKusick, “An Empirical Comparison of ID3 and Back-Propagation”, Proceedings of

the Eighth National Conference on Artificial Intelligence, August 1989, pp. 788–793.

[12] S.L. Fulton, and C.O. Pepe, “An Introduction to Model-based Reasoning”, AI Expert, January 1990, pp. 48–55.

[13] S.I. Gallent, “Connectionist Expert System”, Communication of the ACM, Vol. 31, 1988, pp. 152–169.

[14] M. Goodman, “CBR in Battle Planning”, Proceeding of the Second Workshop on Case-based Reasoning, Pensacola Beach, FL, 1989, pp. 264–269.

[15] F. Hayes-Roth, and J. McDermott, “An Interference matching technique for inducing abstractions”, Communication of the ACM, Vol. 21, No. 5, 1978, pp. 401–410.

[16] D. Hillman, “Integrating neural nets and expert systems”, AI Expert, June 1990, pp. 54–59.

[17] T.R. Hinrichs, “Strategies for Adaptation and Recovery in a Design Problem Solver”, Proceeding of the Second Workshop on Case-based Reasoning, Pensacola Beach, FL, 1989, pp. 115–118.

[18] W.R. Hutchison, and R.S. Kenneth, “Integration of Distributed and Symbolic Knowledge Representation”, Proceedings of the First International Conference of Neural Networks, June 1987, pp. II395–II398.

[19] P.T. Jackson, Introduction to Expert Systems, Addison Wesley Publishing Co., Workingham, 1990.

[20] T. Kohonen, “An Introduction to Neural Computing”, Neural Networks, Vol. 1, No. 1, 1988, pp. 3–16.

[21] J.L. Kolodner, and C. Riesbeck, Tutorial book on Case-based Reasoning in the Eighth National Conference on Artificial Intelligence, Boston, 1990.

[22] P. Koton, “Integrating Case-based and Causal Reasoning”, Proceedings of the Tenth Annual Conference of the Cognitive Science Society, Montreal, 1988, pp. 167–173.

[23] J. Liebowitz, “Introducing Expert Systems into the Firm”, Expert Systems for Business and Management, Liebowitz, J. (Ed), Yourdon Press, Englewood Cliffs, NY, 1990, pp. 1–12.

[24] R.P. Lippmann, “Introduction to Neural Computing”, IEEE ASSP Magazine, April 1987, pp. 4–22.

[25] M. Lu, and T. Guimaraes, “Expert Systems Project Selection and Development Strategies”, Systems Development Management, December 1988. Reprinted in Journal of Information Systems Management, Spring 1989 and Expert Systems, Summer 1989.

[26] W. Mark, “Case-based Reasoning for Autoclave Management”, Proceeding of the Second Workshop on Case-based Reasoning, Pensacola Beach, FL, 1989, pp. 176–180.

[27] R. Michalski, and R. Chilausky, “Knowledge acquisition by encoding expert rules versus computer induction from examples: a case study involving soybean pathology”, International Journal of Man–Machine Studies, Vol. 12, 1980, pp. 63–87.

[28] R. Michalski, and J.B. Larson, “Selection of Most Representative Training Examples and Incremental Generation of VL1 Hypotheses: The Underlying Methodology and the Description of Programs ESEL and AQ11”, Technical Report 867, Computer Science Department, University of Illinois at Urbana-Champaign, 1978.

[29] T.M. Mitchell, “Version Spaces: A Candidate Elimination Approach to Rule Learning”, Proceedings of the Fifth International Joint Conference on Artificial Intelligence, 1977, pp. 305–310.

[30] M. Polanyi, Personal Knowledge, University of Chicago Press, Chicago, 1958.

[31] B.H. Ross, “Remindings in Learning: Objects and Tools”, S. Vosniadou and A. Ortony (Eds.), Similarity and Analogical Reasoning, Cambridge University Press, Cambridge, 1986, pp. 438–469.

[32] B.H. Ross, “Some Psychological Results on Case-based Reasoning”, Proceeding of the Second Workshop on Case-based Reasoning, Pensacola Beach, FL, 1989, pp. 144–147.

[33] D.E. Rumelhart, G.E. Hinton, and R.J. Williams, "Learning Internal Representation by Error Propagation", D.E. Rumelhart and J.L. McClelland (Eds.), Parallel Distributed Processing: Exploration in the Microstructure of Cognition, MIT Press, Cambridge, 1986, pp. 312-362.

[34] J.R. Quinlan, “Learning Efficient Classification Procedures and Their Application to Chess End Games”, R.S. Michaski, J.G. Carbonell, and T.M. Mitchell (Eds.), Machine Learning: An Artificial Intelligence Approach, Tioga Publishing Co., Palo Alto, CA, 1983, pp. 463–482.

[35] K. Saito, and R. Nakano, “Medical Diagnostic Expert System based on PAP Model”, Proceedings of the IEEE International Conference on Neural Networks, June 1988, pp. I225–I262.

[36] S.A. Vere, “Induction of Concepts in the Predicate Calculus”, Proceedings of the Fourth International Joint Conference on Artificial Intelligence, Tbilisi, USSR, 1975, pp. 281–287.

[37] Y. Yoon, R.W. Brobst, P.R. Bergstresser, and L. Peterson, “A Connectionist Expert System for Dermatology Diagnosis”, Expert System, Vol. 1, No. 1, 1990, pp. 22–31.
