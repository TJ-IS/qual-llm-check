---
otero_id: 18812
otero_key: "784JJHMD"
title: "Self-improving expert systems"
authors: "Arie Ben-David; Yoh-Han Pao"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90028-e"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Self-improving expert systems An architecture and implementation

Arie Ben-David

The Hebrew University, Mount Scopus, Jerusalem, Israel

Yoh-Han Pao

Case Western Reserve University, Cleveland, OH, USA

Self-improving expert systems that are based upon learning-by-example have drawn much attention in recent years. A methodology is presented which assists in the use of a learning-by-example paradigm for expert systems applications. The architecture is based upon a hybrid of neural networks and rule-based models. Practitioners may use a similar approach to construct self-improving expert systems faster and more efficiently than has been possible with pure rule-based systems. The ideas are illustrated through an actual expert system that assists experts during the planning stage of a chemical product that has given properties and composition. A description of the application and a discussion of some interesting implementation issues are presented.

Keywords: Expert systems, Neural networks, Learning-by-example, Rule-based systems, Process simulation.

![](/api/attachments/784JJHMD/fulltext/images/4b6830aaae5c59363b93e05fb2e44321a521ea3be1b498dd0e9f97e28a54a0ad.jpg)

Arie Ben-David heads the Management Information Systems Department in the School of Business Administration at the Hebrew University of Jerusalem, Israel. He earned his Ph.D. in Computer Science at Case Western Reserve University, Cleveland, OH (1988) and his M.B.A. in MIS at the School of Business Administration, Tel Aviv University, Israel. His research interests include: expert systems, machine learning and decision support systems. He has been a consultant to financial and industrial institutions both in Israel and in the USA.

Correspondence to: A. Ben-David, School of Business Administration, The Hebrew University, Mount Scopus, Jerusalem 91905, Israel. Tel: 02-883235.

## Motivation

Expert, or knowledge-based, systems have become widely accepted in recent years. Expert systems are currently used in a wide variety of domains, including diagnosis, planning, and configuration. There are, currently, thousands of reported expert systems operating in an increasing number of organizations [6].

One of the major differences between expert systems and traditional information management systems is the emphasize of the former on knowledge, rather than on data, processing. The traditional approach to knowledge extraction for building and maintaining expert systems is to use domain expert(s). The expert has to explain explicitly how he/she reaches the right decisions under the many circumstances that may arise. During the early eighties it became evident that such explicit knowledge extraction (sometimes called knowledge acquisition) is inherently slow and expensive even in domains of moderate complexity.

It is known that it is easier for a good expert to make the right decision than to explain exactly

![](/api/attachments/784JJHMD/fulltext/images/59dcbc63638999fe722d8cc85814d163aca8082a6bf94afc4f5448001af43bf7.jpg)

Yoh-Han Pao has been a Professor of Electrical Engineering and Computer Science at Case Western Reserve University (CWRU) since 1967. He has served as chairman of the University's Electrical Engineering Department (1969–77), as Director of the Electrical, Computer and System Engineering Division at NSF (1978–1980), and as founding director of the Center for Automation and Intelligent Systems Research at CWRU. He is the George S. Dively Distinguished

Professor of Engineering at CWRU, is a Fellow of IEEE and of the American Optical Society. He has been a NATO Senior Science Fellow, has visited MIT, Edinburgh University and the Turing Institute as lecturer/researcher, and has been a member of the technical staff at AT&T Bell Laboratories in Murray Hill, NJ. He is co-founder and president of AI Ware Inc., Cleveland, OH.

how the decision has been made. The main reasons for this difficulty stem from the fact that human knowledge is frequently unstructured, ill-defined, and hard to express. Also, many good decisions are made based upon intuition. The more complicated the domain the harder it is to acquire the knowledge required for maKing it into a successful expert system.

The nature of knowledge acquisition has made it a major factor in budget allocation for many expert systems projects. As expert systems have evolved to deal with more complex domains, knowledge acquisition frequently becomes a real barrier. New methods that reduce knowledge acquisition costs must, therefore, be found in order to make expert systems an attractive tool for solving complex problems. An interesting way of achieving this goal is discussed here.

## Expert systems and their deficiencies

An expert system is a program that supports high level tasks such as decision-making, classification, and forecasting, by using specific domain knowledge. Usually, an expert system recommends a decision or an action. It is also capable of explaining how it reached its conclusion. In general, a computerized system can rightfully be called an expert system when it approaches the performance level of a human expert.

Rule-based systems are one of the main mechanisms for building expert systems due to early successful applications which were almost entirely based on rules. Indeed, the terms rule-based and expert system are sometimes used synonymously. A rule-based expert system is typically composed of a collection of rules and inference mechanism, or interpreter, that performs the required computation. We show how an expert system that does not rely entirely upon rules is built by trading rules with other powerful paradigms that more effectively model a process.

Pan and Tenenbaum [9] made a distinction between ‘deep’ and ‘shallow’ approaches to expert systems. A deep knowledge-base forms a model of the process, while a shallow one records some rather important aspects acquired from human experts. “A shallow-level system…”, they wrote, “attempts to help domain experts in formalizing their experience…”. A deep-level approach “explicitly represents the structure of the domain in terms of multiple causal structure”. The need to incorporate process models within expert systems was also reported by Mittal [8] in the context of the design of mechanical mechanisms, and by Fink [2] regarding diagnostics. In most reported expert systems, process models were expressed as rules. Rule-based process models were used, for instance, by Herrod and Richel [3] for glass annealing simulation, and by Kumar and Ernst [7] in the WAX casting monitor.

Rule-based process simulation can be very complicated in terms of knowledge acquisition when no comprehensive theory exists about the process at hand. Knowledge base maintenance is another major consideration in rule-based systems. Consider, for example, a chemical product assembled from 15 components. Applying a rule-based approach to composition design requires explicit expression of all the meaningful states (i.e., different compositions) via rules. This strategy may be very costly, since the possible number of compositions is likely to be very high. Consequently, the required knowledge acquisition and maintenance effort sometimes make the rule-based approach unattractive.

An alternative approach to conventional expert systems architecture is proposed here. Instead of using rules to express the model of the process, we suggest simulation of complex processes with neural networks. These are then augmented with rules to express extra knowledge that cannot be captured in the networks.

## Neural networks and their relevance to expert systems

Neural networks belong to a family of models that are based upon a learning-by-example paradigm, in which, decision-rules or classification formulas are automatically generated according to actual examples with which the model is presented. The application of the decision-rules or classification formulas is possible only after enough examples have been seen, so that the model's predictions are acceptable within a predefined margin of error.

Neural networks are gradually being accepted as useful tools in certain applications. Pattern recognition applications of neural networks are described by Hinton and Kevin [4]; Utilization in signal analysis is presented by Sejnowski and Rosenberg [12]; Hopfield and Tank [5] used neural networks for optimization, and Pao and Sobajic [10] proposed means for incorporating them in adaptive control applications. A comprehensive list of neural network applications is reported by Caudill [1].

![](/api/attachments/784JJHMD/fulltext/images/8efefd36ead1f1e2e854df1dd4d676d19c61a2048395db4caa655cbf53470988.jpg)  
Fig. 1. A simplified neural network.

Neural networks are known by many other terms, such as connectionist and parallel distributed models. Actually, there are now a wide variety of neural network models. Generally, they mimic some basic behavior of our human neural system. Figure 1 schematically shows a typical model of a neural network: it is a collection of nodes, or processing elements, and a set of connections between them. In this three layer example, each node is connected to every node at the lower level (the input side), and to each in the next higher layer (the output). Each connection has a weight which reflects its strength. Each node sums its weighted input and produces an output that is typically a nonlinear function of the (weighted) input. A neural network can be used to approximate a nonlinear function.

The construction of a neural network involves three phases:

(a) Configuration, in which the number of layers, the number of nodes at each layer, and few other parameters are determined. This phase is manual and it is performed by the system designer.

(b) Training, in which the network is presented with actual examples (i.e., pairs of input and output vectors), and the values of the weights are calculated. Training is automatic and requires no human intervention.

(c) Classification, in which the network provides predictions of output vectors, given only their input values. This phase, too, is fully automatic.

A neural network can be trained only after it has been configured. Similarly, classification can only be done via a trained network (i.e., after the completion of the training phase). We discuss now some important aspects of neural networks in greater detail.

Determining a neural network configuration involves the following major decisions: $^{1}$

1. The number of layers in the network.

2. The number of processing units at each layer.

It is important to note that during configuration, these same decisions are made, regardless of the size and nature of the problem at hand. In this respect, the designer's task does not become more complicated as the size and degree of nonlinearity of the domain grow.

In order to use a neural network to properly approximate a function (i.e., within a permissible margin of errors), we first train it. During the training phase, examples are introduced to the network. This assigns values to the weights in such a way that the average error of the predictions over all the examples is minimized. A gradient descent algorithm (for finding the greatest slope up or down a curve and, hence, the maximum or minimum) is the most common way of assigning the proper weights to a neural network. Appendix A shows the formulas for training Rumelhart's [11] powerful feed-forward neural network. The gradient descent algorithm allows incremental additions of observations to further train an (already trained) network. This is essentially an automatic feedback feature that is very important for many applications.

While classifying, new patterns are fed to the network's input and their predicted output values are calculated. These patterns may be used to further train the network in order to improve the classifications.

Neural networks have limitations also. Most importantly, their abstract entity is very remote from the domain with which they are dealing. It is not straightforward (to say the least) for a domain expert to think about his \ her areas of expertise in terms of nodes, connections, and weights. It is, therefore, very difficult to provide the end-user with convincing explanations about how a recommendation has been made. Furthermore, neural networks generally require significant computer resources. These features must also be taken into account while using neural networks in expert systems.

It is emphasized that the configuration phase is the only step during neural network construction that requires active participation of the system designer. Furthermore, his\ her decisions during configuration are relatively simple and are unaffected by the complexity of the domain. Training and classification, on the other hand, are fully automatic. Also, neural networks have an inherent automatic feedback feature.

Given these observations, we propose that, by replacing rules with neural networks in an appropriate manner, expert systems technology can realize a substantial improvement. Some significant advantages may result from a combination of rule-bases and neural networks in a unified expert system framework, notably:

(a) The required knowledge acquisition effort is substantially reduced, since there are fewer rules in the system (compared with the equivalent rule-based system). Consequently, it is easier to maintain the system throughout its life cycle.

(b) The model of the process can be updated automatically without any change in the code. By presenting new examples to the neural network, the predictions are automatically improved.

We have designed an architecture which is a hybrid of neural networks and rule-based approaches. The architecture was tested on a real world expert system that would have been extremely difficult to develop using the rule-based approach alone. The results were very encouraging, suggesting that such a hybrid architecture may increase the number of domains for which solutions using expert systems may provide cost-effective.

## The problem domain

In our application, 15 chemical substances are components that will be mixed and processed in order to produce a product that exhibits certain required properties, such as specific heat, color, and resistance to acids. The designer's goal is to find a composition that meets these properties. However, unfortunately no theoretical model of the process is yet known. Consequently, domain experts rely upon the history of previous compositions, stored in a database, and upon their experience. They typically retrieve the closest neighbor to what is needed from a database, and gradually modify this basic formula to meet the specifications.

Components have conflicting effects on the various properties. Furthermore, the effects are state (or composition) dependent. They vary both in magnitude and in direction, depending on the current composition. As a result, experts prefer to deal with one property at a time. At each iteration, a few ingredients (typically up to three) are modified in order to bring one property closer to its constraint. Each iteration involves substantial cost: The properties of new compositions then have to be measured in a laboratory, which takes a couple of hours. The overall time to arrive at the proper formula for new specifications may involve from a couple of days to several weeks.

The expert system we use as an example was built in order to guide an expert technician through this lengthy process of finding an acceptable formula. The system recommends a basic formula and iteratively advises the user what changes to make in the current composition in order to meet the product specifications faster.

Candidate rule-based approaches towards solving problems of this sort are described by Herrod [3] and Kumar [7] among others. Based upon their description, a rule in a composition-properties rule-base will be verbally expressed as:

IF the percentage of COMPONENT $_{1}$ is between Low-LIMIT $_{1}$ , and High-LIMIT $_{1}$ , and the percentage of COMPONENT $_{2}$ is between ... etc

THEN the value of $PROPERTY_{1}$ is anticipated to be between Low-Property-LIMIT and High-Property-LIMIT, and the value of $PROPERTY_{2}$ is anticipated ... etc.

Within a rule-base, this is usually entered in the form:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
IF ( $(\% \text{ Low-LIMIT}_1 &lt; \% \text{ COMPONENT}_1 &lt; \% \text{ High-LIMIT}_1)$ 
&amp; ( $(\% \text{ Low-LIMIT}_2 &lt; \% \text{ COMPONENT}_2 &lt; \% \text{ High-LIMIT}_2)$ 
&amp;
...
( $(\% \text{ Low-LIMIT}_n &lt; \% \text{ COMPONENT}_n &lt; \% \text{ High-LIMIT}_n)$ 
)
THEN ( $(Low\text{-Prop-LIMIT}_1 &lt; PROPERTY_1 &lt; High\text{-Prop-LIMIT}_1)$ 
&amp;
$(Low\text{-Prop-LIMIT}_2 &lt; PROPERTY_2 &lt; High\text{-Prop-LIMIT}_2)$ 
&amp;
...
$(Low\text{-Prop-LIMIT}_m &lt; PROPERTY_m &lt; High\text{-Prop-LIMIT}_m)$
</div>

These authors have pointed out that a rule-based process simulation is cost-effective as long as the number of rules can be kept at a reasonable number. Due to the fact that fifteen components and at least five relevant properties are involved in our chemical composition problem and that the phenomenon at hand is nonlinear, it was not practical to express the process model via such rules. The domain experts found it very difficult to express such complex rules accurately. A more efficient way therefore had to be found.

## The solution

An appealing direction toward a cost-effective solution is to generate the model process automatically, based on examples of known formulas. We have chosen to express the model via neural networks for reasons to be discussed shortly.

Figure 2 shows the architecture of the system. Two types of neural networks are used for process simulation. The neural network at the top of Figure 2 provides the basic formula. Given five properties as input (i.e., the product specifications), this network predicts a composition which will later be used, if needed, for further improvement. The second, lower, neural network deals with the inverse problem: it predicts properties, given a composition.

![](/api/attachments/784JJHMD/fulltext/images/af0028254d588400f9b7df67ad6ea55a66876484b1cccc344775a46792744df3.jpg)  
Fig. 2. A hybrid of neural networks and rule-base.

The networks are augmented with extra knowledge that cannot be captured within the neural network's framework. The supplementary knowledge is embodied in relatively few simple rules.

Any prediction is naturally susceptible to errors; Field tests must be carried out in order to verify the actual properties before any mass production takes place. When the predictions are accurate within predefined margins, the algorithm terminates successfully. Inappropriate predictions are handled differently.

The results of the laboratory tests (i.e.: the actual properties) are stored for further network training. The degree of accuracy of future predictions automatically improves as more real samples (results) are provided to the neural networks. Meanwhile, although the network has failed to predict the desired current properties accurately (mainly due to lack of sufficient examples) it still continues to support the actual product design.

When a prediction is not accurate, there is no reason to perform sensitivity or response analysis within the immediate neighborhood of the incorrectly predicted point. At this stage of the dialogue, the system invokes another source of knowledge – a rule-based component that iteratively suggests possible modifications to the current formula. The rule-base was derived directly from the personal knowledge of the experts, and it is based upon their experience. We have mentioned previously that domain experts modify one property at a time while trying (as much as possible) not to disturb the other properties. This way they have better control over the refinement procedure. The rules were similarly defined: They deal with one property at a time, and assume minor effects of composition changes on the rest of the properties. A typical composition modification rule states the following:

In order to bring $PROPERTY_{i}$ to its desired value, which is within $DISTANCE_{i}$ in $DIRECTION_{i}$ from its current value, one can: Either change $COMPONENT_{k}$ by $PERCENT_{k}$ in $DIRECTION_{k}$ (increase of decrease), or change $COMPONENT_{l}$ by $PERCENT_{l}$ in $DIRECTION_{l}$ , or ..., etc.

The above rule is presented in the computer in the following equivalent form:

$$
\begin{array}{l l} I F & (P R O P E R T Y _ {i} D I R E C T I O N _ {i} D I S T A N C E _ {i}) \\ T H E N & ((C O M P O N E N T _ {i k} D I R E C T I O N _ {i k} P E R - \\ & C E N T _ {i k}) o r \\ & (C O M P O N E N T _ {i l} D I R E C T I O N _ {i l} P E R - \\ & C E N T _ {i l}) o r \\ & \dots \\ & (C O M P O N E N T _ {i w} D I R E C T I O N _ {i w} P E R - \\ & C E N T _ {i w})) \end{array}
$$

Component modifications are assumed to be linear with the magnitude of the deviation of each property from its target value (i.e., large deviations require large modifications). We have found that most of our experts behave similarly. The marginal increment, PERCENT, is therefore calculated via a simple heuristic linear expressions. For instance:

$$
\begin{array}{r l} \text { PERCENT } _ {i k} & = \text { MIN - INCREMENT } _ {i k} \\ & + \text { CONSTANT } _ {i k} * \text { DISTANCE } _ {i}, \end{array}
$$

where MIN-INCREMENT and CONSTANT are defined for each component with respect to each property.

The rules are also assumed to be symmetric by default. If a rule states that we can generally increase the value of $PROPERTY_{i}$ by decreasing $COMPONENT_{k}$ by $X$ percent, it is assumed that increasing the same component by the same percent will have similar effect in the opposite direction. When the user indicates which property value he \ she wants to improve, the system automatically generates all the candidate plans for formula modification. Plan generation is done by locating the rule which is pertinent to the particular case and calculating the appropriate increments for each relevant plan.

It is important to note that the number of rules in the rule-base is rather small, since it is bounded by the number of relevant properties. The simplified assumptions behind the rules, however, have made them susceptible to erroneous behavior if applied under certain conditions: for some compositions, they produce the opposite of the desired effect. Unfortunately, no expert can specify these exceptions accurately enough within a reasonable time frame. Another method of filtering out bad plans from anticipated good ones is therefore required. In addition, it is essential to prioritize potentially good plans according to their expected effect. A neural network provides these two important facilities.

All the potential plans (derived from the rule-base) are fed into a neural network before a recommendation is given. The network then predicts properties given a composition. Using the second neural network (shown at the middle of Figure 2), it is possible to estimate the effects of each plan before resorting to a costly laboratory test. Priorities among prospective plans are assigned as follows:

(1) A plan is rejected from further consideration if there is a contradiction between the rule-base and the neural network predictions of the anticipated direction of the effect on the selected property.

(2) Among all non-rejected plans, plan X is preferred to plan Y if X is predicted (by the neural networks) to yield a better improvement of the selected property value.

The anticipated values of all the properties for all candidate plans are displayed as well, so that the user can use his \ her own judgement in the final decision making.

Conflicts occasionally occur between the rules and the network prediction. This is not surprising, taking into account the fact that the rules make the simplifying assumption of linearity, as explained previously. We have found that on the average, about 75 percent of the rule-based generated plans passed the filter of step 1 above. The user typically has five to seven alternatives to choose from at each iteration of step 2.

Once the user has selected a plan, a laboratory test is carried out. Bad predictions (i.e., selected formulas with their actual properties) are fed back into the system. The new information is stored and used for further training of the neural networks. At intervals, all the neural networks are trained using this feedback. The rule based component, on the other hand, is static. It can only be modified explicitly. The consultation process repeats iteratively until an acceptable formula is found.

Three major advantages are associated with neural networks for our application:

(a) The process of training is almost automatic and involves very little knowledge acquisition effort.

(b) The required storage size of the network does not depend upon the number of examples (it depends on the network configuration alone).

(c) As more examples are input to the neural networks, their predictions become more accurate. This process is fully automatic.

The neural networks in our problem domain have four layers. Each internal layer has 5 to 10 nodes. The target machine was an IBM AT of 10 MHz. We have found 80286 based machines too slow for training the networks on-line, therefore the training has been done on DEC's VAX 780 using its efficient Fortran compiler. Training each of the neural networks requires about 2 hours, on average, for 200 examples. The resulting trained networks were imported to the AT, where the system is currently running. Training, is, therefore, done off-line, a fact which does not adversely affect the implementation.

The implementation on the AT utilized TI's Personal Consultant, a general purpose expert system shell written in Lisp. This programing tool was used for implementing the man-machine interface and the rule-based component of the system. The neural networks were implemented on the AT using AI-WARE's N-NET, which is a C-based neural network development tool kit. A meaningful demo version was available at the sponsor's facility for beta tests about three-months after the project start date. A full version for one line of products was ready within six months. This timetable would have been impossible had a purely rule-based approach been adopted.

To summarize, the main advantage of the architecture described is that it enables avoidance of the definition of many complicated rules: they are few and simple. We can afford a very simple rule-base since the neural networks capture the nonlinear cross-effects of various inputs on the outputs. In other words, what allows the architecture to function adequately (in spite of simplifying assumptions behind the rules) is the existence of a process model that is embedded in the neural networks. The rule-based component acts only as a 'driver' (or generator) to prospective refinement plans, while the neural networks function as the testing module. The accuracy of the process model automatically improves as more examples are introduced to the system, which actually learns from its mistakes.

## Limitations and conclusions

While neural networks are very useful tools for AI applications, it is also important to understand their limitations. First, they behave as black boxes, making it tough to explain their predictions in terms natural to the user. Secondly, although examples are generally easier to derive than rules, they are not always handy.

The architecture described in this paper provides only partial solution to these difficulties. In term of explanations, one can use the rule-based component as a source of explanations. Also, where examples are scarce, a rule-based component can partially compensate for inaccurate predictions. Consequently, the system may be operational without having to wait for the neural networks to ‘mature’ (i.e., have sufficient examples).

As more examples are introduced, the predictions improve, and the reliance upon the rules eventually decreases.

Despite their limitations, neural networks are currently taking off rapidly from research laboratories to the real world. It has been shown how a hybrid structure of neural networks and rule-bases can be used to construct self-improving expert systems efficiently. It is anticipated that an increasing number of domains will enjoy these new artificial intelligence technologies in future.

## References

[1] Caudill, M. “Neural Networks Primer”, AI Expert, Vol. 2, No. 12 and Vol. 3, No. 2 and 6, 1987–1988.

[2] Fink, P.K. “Control and Integration of Diverse Knowledge in a Diagnostic Expert System”, IJCAI Proceedings, 1985, pp. 426–431.

[3] Herrod, R.A. and Richel, J. "Knowledge Based Simulation of a Glass Annealing Process – An AI Application in the Glass industry", AAAI-86 Proceedings, 1986, pp. 800–804.

[4] Hinton, G.E. and Kevin, J.L. "Shape Recognition and Illusory Conjunctions", IJCAI Proceedings, 1985, pp. 252–259.

[5] Hopfield, J.J. and Tank, D.W. “Neural Computation of Decisions in Optimization Problems”, Biological Cybernetics, Vol. 52, 1985, pp. 141–152.

[6] Jain, H.K. and Chaturvedi, A.R. "Expert Systems Problem Selection: A Domain Characteristics Approach", Information and Management, Vol. 17, 1989, pp. 245-253.

[7] Kumar, G.S. and Ernst, G.W. “An Expert System Architecture for Predictive Monitoring”, Proceedings of the Winter Annual Meeting of the ASME, 1987.

[8] Mittal, S. and Araya, A. “A Knowledge Based Framework for Design”, AAAI Proceedings, 1986, pp. 856–865.

[9] Pan, J.Y. and Tenenbaum, M.J. "P.I.E.S: An Engineer's Do-It-Yourself Knowledge System for Interpretation of Parametric Test Data", AAAI Proceedings, 1986, pp. 836–843.

[10] Pao, Y.H. and Sobajic, D.J. “Connectionist-Net Technology for Intelligent Robotic Control”, Working paper no. TR 87-117, Center for Automation and Intelligent Systems, Case Western Reserve University, Cleveland, OH, 1987.

[11] Rumelhart, D.E. “Learning Internal Representation by Error Propagation”, In: Parallel Distributed Processing, Rumelhart, D.E. and McClelland, J.L., eds., Vol. 1, The MIT Press, Cambridge, MA, 1986.

[12] Sejnowski, T.J. and Rosenberg, C.R. "NETtalk: A Parallel Network that Learns to Read Aloud", Working paper no. TR-JHU/EECS-86/01, EE and CS Department, Johns Hopkins University, Baltimore, MD, 1986.

## Appendix A

Here we consider the feed-forward neural network proposed by Rumelhart [11]. Figure 1 is such a feed-forward network. The output of the Jth node, $O_{j}$ , is typically a sigmodial activation function of the form:

$$
O _ {j} = \frac {1}{1 + e ^ {- (n e t _ {j} + Q _ {j})}},\tag{1}
$$

where $Q_{j}$ is a threshold and $net_{j} = \sum_{i} W_{jj} O_{i}$ over all incoming connections. $W_{ji}$ denotes the weight of the jith connection.

During learning the network is presented with pairs of patterns. Each pair has an input pattern and a corresponding desired output. Weights and thresholds are initially selected at random. Using their initial values, the output value is calculated and compared with the desired output. The error term can be written:

$$
E = 1 / 2 \sum_ {k} \left(T _ {k} - O _ {k}\right) ^ {2},\tag{2}
$$

there $T_{k}$ designates the desired output and $O_{k}$ is the predicted one.

Learning consists of changing the weights and thresholds in a gradient descent manner to minimize the error function. For activation functions of expression (1), the incremental change of a weight may be written as:

$$
\Delta W _ {k j} = \eta \delta_ {k} O _ {j},\tag{3}
$$

where $\eta$ is the learning rate parameter and $\delta_{k}$ is given by:

$$
\delta_ {k} = (T _ {k} - O _ {k}) O _ {k} (1 - O _ {k}) \text {   for   an   output }
$$

node $k$ , and

(4a)

$$
\delta_ {j} = O _ {j} (1 - O) \sum_ {k} \delta_ {k} W _ {k j} \text {   for   the   other   nodes. }\tag{4b}
$$

It has been empirically shown that one way to increase the convergence rate without causing the error function to oscillate is to include a momentum term in (3), therefore

$$
\Delta W _ {k j} (n + 1) = \eta \delta_ {k} O _ {j} + \alpha \Delta W _ {k j} (n),\tag{5}
$$

where n indexes the number of times in which a set of input patterns has been presented to the

network during learning. The parameter $\alpha$ is a constant which determines the effect of past weight changes on the current changes in their values. The thresholds, $Q_{j}$ , are computed by determining values of a weight, $W_{jo}$ , which is associated with a dummy connection between node j and a dummy node at a lower level that has a constant unary output. $Q_{j}$ is then set to $W_{jo}$ .
