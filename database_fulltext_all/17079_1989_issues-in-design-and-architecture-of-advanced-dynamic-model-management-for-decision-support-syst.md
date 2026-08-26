---
otero_id: 17079
otero_key: "74J4C9DF"
title: "Issues in design and architecture of advanced dynamic model management for decision support systems"
authors: "Paolo d'Alessandro; Manuela Dalla Mora; Elena De Santis"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90016-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Issues in Design and Architecture of Advanced Dynamic Model Management for Decision Support Systems

Paolo d'ALESSANDRO,

Manuela DALLA MORA and Elena DE SANTIS
Department of Electrical Engineering, University of L'Aquila,
67100 L'Aquila, Italy

This paper presents some of the research issues that arise when the design of a dynamic model management system oriented to decision support is extended to provide such advanced features as handling of symbolic models, automatic building and manipulation of models, model base management and simultaneous processing of multiple models. In particular it discusses the relationship between system theory and the design of software for model management, with an attempt to individuate research orientations that may foster further progress in the development of decision support systems.

![](/api/attachments/74J4C9DF/fulltext/images/9cab503297c7c0d1b5c157bf8640e6ddec83c902e79b6f4cbfbaf3ebe0307b12.jpg)

Paolo d'Alessandro received his degree of Electronic engineer in 1968 from University of Rome. He is currently Professor of System Theory at the department of Electrical Engineering of the University of L'Aquila (Italy). He has published papers on system theory and related fields in a number of journals including Mathematical System Theory, Siam Journal on Control, International Journal on System Science, Journal of the Franklin Institute, Applied Mathematics and Optimization,

Mathematics and Computers in Simulation, Computer and Mathematics with Applications, RAIRO O.R., System & Control Letters. His current research interests focus on Decision Support Systems with emphasis on specifications, model management, optimization, user interfaces and software engineering.

![](/api/attachments/74J4C9DF/fulltext/images/60ef297348235581f416ffe3641d04dd9ee2e1f9c89f785fc157f52386766bea.jpg)

Manuela Dalla Mora received her degree in Mathematics from the University of Padova (Italy) in 1979. She is currently researcher at the Department of Electrical Engineering of the University of L'Aquila (Italy). She has published papers on system theory and DSS in a number of Conferences and Journals as International Journal of the Franklin Institute, Mathematics and Computers with Applications, RAIRO O.R., Systems & Control Letters. Her current research interests are on Decision Support Systems, with emphasis on specifications, model management, optimization, user interfaces and software engineering.

## 1. Introduction

This paper deals essentially with the relationship between the state space approach to dynamic model management and the design of software systems for decision support, with particular emphasis on symbolic manipulation of systems and its applications to DSS design.

For space reasons we confine our concern to modeling and simulation. These are basic components that any software system should provide. Many other tools should be provided as well, first and foremost optimization and in particular multicriteria optimization. Actually in a DSS environment it may be more important to know “what is best” than to know “what if”, but to deal with optimization adequately a separate treatment is required.

Simulation within the framework of the state space approach has received a good deal of attention (see e.g. [1]). However, the decision support motivation entails profound differences with respect to this stream of research. Actually the design of a decision support system focuses its attention on the user. To begin with, the user should be assumed to have concrete but unstructured problems. This means that the system and not the user is in charge of structuring and formalizing the problem in question. Moreover the user should be assumed to have no expertise (and no willingness

![](/api/attachments/74J4C9DF/fulltext/images/5bcac85c128acfe24a2a5f8003d7b85e26a4cf3471c3f6abc1f588f1fa069f8a.jpg)

management, optimization, user interfaces and software engineering.

to acquire any expertise) concerning the methodologies required to solve his/her problems.

This implies that the system must be able to make such methodologies transparent to the user, unless he/she deliberately decides to be involved with them.

The first important implication of this emphasis on the user is that simulation languages are unacceptable in a DSS environment, because a simulation language requires in addition to the expertise on the underlying methodologies expertise on the language itself.

More in general centering the structure of a DSS on the user requires the elicitation of the user needs and the adoption of suitable design criteria. There is of course some debate on these issues. We give here an example of possible criteria, to the purpose of better illustrating this fundamental point and to place in proper perspective the subsequent discussion.

We make reference to a model management system based on simulation and called SUSI (see [2], [3] and [4]). Such research prototype was designed with an aim at the degree of achievement of the following features:

(1) Transparency of the involved methodologies.

(2) Interactivity.

(3) Integration of tools.

(4) User comfort and productivity.

(5) User creativity.

Feature number 5 was suggested by the excellent work of J.J. Elam and M. Mead [5]. The goal of promoting user creativity is probably the best characterization of the spirit that should underlie the design of a DSS. In [5] a discussion of creativity influencing factors and creativity enhancing design principles and of the interaction of each other is given. The design of SUSI also attempts to adhere to such principles, that are interacting and overlapping to 1–4 above. They are

(a) Depth and tenor of feedback.

(b) Ease of use.

(c) Restart capability.

(d) Range of tools.

(e) Enjoyable fun environment.

In the sequel we introduce and discuss some of the tools that should be included in an advanced model management system. Some of them are planned to be integrated in an enhanced (and translated from Pascal to Modula 2) version of SUSI. Others will be implemented on a experimental basis, because they will require further research to become mature. However in this way we try to shape possible perspective of progress in the development of dynamic model management software for decision support.

Another research area of primary importance regards the integration of other useful methodologies, more or less extraneous to system theory, in a common environment. Examples are combinatorial optimization, linear and non linear mathematical programming, time series analysis etc. The need of such integration lead naturally to the concept of multiparadigm DSS, which is treated in a companion paper.

## 2. Advanced Dynamic Model Management Features

In SUSI, which addresses linear dynamical discrete time systems, the following capabilities were provided:

(1) Definition and modification of a model in state space form.

(2) Simulation of a model.

(3) Handling of libraries of models and of simulation experiments.

(4) Auxiliary services (Printing, graphic, report and help services).

An abstract linear dynamical (finite dimensional) discrete time system is defined by means of the recursive input-state-output equations:

$$
\begin{array}{l} x (t + 1) = A x (t) + B u (t), \\ y (t) = C x (t) + D u (t), \end{array}
$$

where t represents the time variable, x, u and y are vector valued functions of time representing respectively the state, the input and the output of the system and A, B, C and D are linear operators (and hence are represented by matrices). These equations are solved by the simulation module starting from some initial time, which can be conventionally set to be zero, and initial condition $x(0) = \bar{x}$ . A model is an abstract system in which all variables appearing in the above vectors are interpreted as representing quantities related to the real process described by the model itself and hence are also given a name. Often, especially within formal discussion, we refer to systems rather than models, but in this cases it is tacitly understood that the same analysis applies, with the obvious modifications, to models as well. The above description of a system will be referred to as standard iso (i.e. input-state-output) form. We shall most of the times add the specification “numeric” to the words “system” and “model” when it is required to stress the distinction with symbolic systems and models (introduced in the next section).

During simulation the user interface is similar to that of a spreadsheet. This is obtained exploiting the concept of the so-called (in the literature on advanced simulation [1]) experimental frame, which is the matrix of the input, state and output variables each disposed on a row with entries representing the values of the variable in question at various instants of time.

The above capabilities are very basic, but a main point in the development of SUSI were the design criteria which qualify the system as a DSS, especially for what concerns the sophisticated user interface. We will concentrate here on the design of a more advanced system, in which, besides the enhancement of the existing features, the following capabilities will be included:

(1a) Handling of models at both the numerical and the symbolic level.

(2a) Automatic building of models.

(3a) Automatic manipulation of models.

(4a) Data base like management of libraries of models and of simulation experiments.

(5a) Simultaneous processing of multiple data structures (i.e. multiple models, multiple simulations experiments etc.).

These capabilities and their motivations are illustrated in the sequel.

We advice from the outset that a complete implementation of the design that will be presented in this paper is fairly difficult and may require a long time. However the spirit is that of assessing the ideal structure of a model base management system and of envisioning the research orientation required to accomplish such an implementation.

## 3. Symbolic Form for Dynamic Models

A model in symbolic form is essentially a parametrized set of models. For instance one may define a vector of parameters $\vartheta$ and the functions that give the dependency of the coefficient matrices A, B, C and D on $\vartheta$ . In this case the input-state-output equations take the form

$$
\begin{array}{l} x (t + 1) = A (\vartheta) x (t) + B (\vartheta) u (t), \\ y (t) = C (\vartheta) x (t) + D (\vartheta) u (t). \end{array}
$$

It should be stressed that the functions of $\vartheta$ appearing in these equations are often heavily non linear even when the system is linear (as it is the case for the firm model presented in [3]). The parametrization itself is particularly important, since it usually derives from the modeling exercise and hence contains properties inherent to the represented process.

Notice also that there are cases in which the set of models and thus its description are more complex, e.g. when more than one parametrization is required to describe the set of models. Let us give a practical example in which not only the parameters of the model, but also the dimensions of some subvectors of the input, state and output vectors are free. Actually the model is the same as the firm model presented in [3], except for the disaggregation of raw materials and of finite products (and hence also of sales) in vectors of quantities and for the assumption of existence of intermediate products. Thus the production process submodel takes on the new form

$$
\begin{array}{c} M A T (t + 1) = M A T (t) + A M A (t) - A _ {M P} P (t) \\ \qquad - A _ {M I} P I (t), \\ I N (t + 1) = I N (t) - A _ {I P} P (t) + (I - A _ {I I}) P I (t), \\ P F (t + 1) = P F (t) + P (t) - V (t), \end{array}
$$

where MAT is the stock of raw materials vector, IN is the stock of intermediate products vector, PF is the stock of finite products vector, AMA is the purchase of raw materials vector, P is the production of finite products vector, PI is the production of intermediate products vector, and it is assumed that raw materials are not sold, that intermediate products are not purchased nor sold and that final products are not purchased. The above equations are a form of the Leontiev dynamical model in which the coefficients of the matrices $A_{MP}$ , $A_{MI}$ , $A_{IP}$ and $A_{II}$ represent the production process. For the sake of brevity we do not report the modification of the whole model with the substitution of the above production process submodel. We only confine ourselves to observing that of course suitable prices vectors are required to compute the aggregate monetary entities from the vectors of quantities, so that the new version of the model is suitable for taking into account prices variations. Rather the point with this example is that now the dimension of the above vectors should be kept free in view of the fact that each company has a different number of finite products, intermediate products etc., and hence in the complete model the dimensions of some subvectors of the input state and output vectors are free, just as the model parameters are free. This results in a much more complex set of models.

In any case, however, it is possible to describe the symbolic model by means of a suitable set of parametrizations.

In view of the foregoing discussion it appears natural to state the following definitions:

Definition 1. Given a family $\{P_{\alpha} : \alpha \in A\}$ of sets whose points represent parameter values, an abstract symbolic system is a set of functions $\{F_{\alpha} : \in A\}$ with domain $F_{\alpha} = P_{\alpha}$ , whose values are abstract systems.

Definition 2. Given a property P of an abstract system, a symbolic system $\{F_{\alpha}:\alpha\in A\}$ is said to enjoy P if all the elements of $U\{range F_{\alpha}:\alpha\in A\}$ enjoy P. This latter set will be called range of the symbolic system.

Definition 3. Two symbolic systems $\{F_{\alpha}:\alpha\in A\}$ and $\{G_{\beta}:\in B\}$ are range equivalent if $U\{\text{range } F_{\alpha}:\alpha\in A\}=U\{\text{range } G_{\beta}:\beta\in B\}$ .

The relationship between a symbolic system and a symbolic model is similar to the numeric case.

We shall mostly refer to linear symbolic systems defined by a single function, whose domain is a linear (finite dimensional) space.

It is clear desirable that all the operations on models can be performed, whenever appropriate, both at the numeric and symbolic level, and that one can pass easily and interactively from the symbolic level to the numerical one and conversely. For example, in the case of model definition and simulation, the user should be given the possibility to define and modify both a vector of parameters and the functions that express the dependency of model coefficients on the parameter vector, and to see the effects of such definitions and modifications on the corresponding numeric model. Moreover, it should be possible to vary the parameters dynamically during a simulation session, even assigning different values of the parameters at different instants of time. This possibility is particularly useful. It is in fact quite common that the parameters contain informations on the scenario of the process represented by the model, so that varying parameters gives a more direct way to experiment in scenario changes. On the other hand the symbolic definition of models is necessary for modeling purposes, and hence to implement automatic model building, because modeling is usually carried out by first determining the model at symbolic level (by means of the so called process dynamics) and then determining the free parameters by means of an identification technique. To sum up, a software package that is able to handle symbolic models should enjoy the following capabilities:

(1) Definition and modification of symbolic models.

(2) Definition and modification of parameter vectors.

(3) Floating of numerical models.

(4) Simulation with dynamic definition of parameter vectors.

(5) Handling of libraries of symbolic models and of parameter vectors.

Floating a numeric model means defining according to user's directives a symbolic model to whose range the given numeric model belongs.

## 4. Automatic Model Building and Manipulation

The motivation to include the possibility of automatic building of models lies in the fact that, as already explained, in a true DSS the user is not required to have methodological expertise, but only a practical (and unstructured) knowledge of the problem he/she wants to solve. This should not prevent the expert user to access any aspect he/she wishes of the methodologies involved. In other words, it is up to the user to decide if the underlying methodologies should be completely transparent, totally opaque or inbetween the two extremes. At the design level this requires more than doubling the whole user interface. It would make little sense to have a system that is very easy at the level of model use but requires sophisticated methodological expertise at the level of model building. The solution to the problem is computer assisted modeling, in which the user gives a description of the real process he wants to model in its own language and the system (possibly eliciting further information from the user) produces the required model. This process can be seen as a fundamental step in transforming an ill-structured problem in a structured one and hence in providing a first level of the required automatic structuring capabilities of a DSS.

In the sequel we refer to the construction of numeric models. This is achieved by first deriving for the process in question the appropriate symbolic model, and then deriving the right numeric model by means of an identification stage.

The development of an automatic model builder requires to conceptualize and formalize the process of model building, which has been so far the most informal methodology in system engineering, and actually much more an art than a science. There are few attempts in the literature. An example in the spirit of DSS and addressing linear programming models is contained in [6]. The only example we know of for dynamical models [7], even though advanced in the use of artificial intelligence techniques, seems to be difficult to use and is based on a non state space technique.

There are various approaches to automatic model building. They may be used separately or in any combination.

(a) The first and more obvious approach, used in the above references, consists in developing a knowledge base, that contains the rules for writing the models equations, on the basis of user's description of the process. Used in our context this technique requires that the system have the intelligence to classify as inputs, states and outputs the variables appearing in the model equations and to try to put such equations in standard iso form. The system should output the model in this form if and only if this is possible, otherwise it should determine that this is not possible and why. Note however that, even though this might be a difficult task, the foundations of system theory suggests how to write the model equations from the outset in such a way to facilitate this step. In our architecture (see section 7) the algebraic symbolic processor is in charge of this operations.

We propose however some further possibilities, where, by the contrary of approach (a), the starting point is already a model or a set of models in standard iso form.

(b) The system may maintain in its library symbolic models that altogether constitute very large set of models, in the hope that the model sought by the user is contained in the union of the ranges of the symbolic models. In other words the idea is that of defining by means of symbolic models a covering that is the largest possible subset of the set of all models that may arise in a certain context. In this case the task of the automatic model builder is to find a symbolic model that may contain the required model and then identifying the model requested. This technique will be called instancing technique. The symbolic models to be used for instancing are singled out by the model builder from the other models that should not be used for these purposes. Examples of these latter are model defined by some user for experimental or tutorial purposes. To distinguish these special models used for instancing purposes from the other we shall call them template models. A similar comment and definition also applies for other techniques below.

There are then various other techniques that depend on manipulation of numeric or symbolic models. By manipulation we mean a transformation of models, both at symbolic level and a numeric level. More precisely we can state the following

Definition 4. Given a set A of symbolic (numeric) systems, a manipulation on A is a function on a set $B \subset 2^{A}$ whose values are symbolic (respectively numeric) systems.

Later on we shall give a simple formal example of manipulation. Of course the elements of B may well be singletons; in this case the manipulation transforms a system into another system. Note also that manipulations of models may well be context dependent and, in this case, they will have, usually, a more limited domain than abstract manipulations.

With the concept of manipulation of models we initiate capability 3a of our advanced model management system. The model manipulations relevant for model building are outlined below.

(c) Model modification. Even though an accessible model (e.g. by instancing) does not constitute the required solution, it may be possible to modify such a model into a satisfactory one, on the base of information yield or elicited from the user. For example assume that in the above production submodel intermediate products are also sold. This entails an obvious modification of the rhs side of the second equation of the submodel.

(d) Model specialization. This transformation occurs when, under a certain hypothesis, the model takes on a special form derivable, according to certain rules, from the form already available. For instance assume that in the above production submodel the intermediate products are not required to produce intermediate products themselves. This requires that the matrix $A_{II}$ in the submodel equations be put equal to zero.

(e) Model simplification. This transformation occurs when the current hypotheses on the real process to be modeled allow to arrive to the desired model by simplifying an available model. A typical case occurs when it is known that certain variables must not appear in the sought model. For example assume that in the production sub-model there are not intermediate products. It should be stressed that there are two form of simplification. The one we are meaning now is an exact simplification in the sense that it produces a model that is believed to be an exact representation of the real process. This should not be confounded with the concept of approximating a given (assumed exact) model with another model that has the advantage to be more simple and hence more handy. We will return to this latter concept later on.

(f) Aggregation and disaggregation. These two transformations are rather self-explanatory and an example of disaggregation has been given with the foregoing production submodel.

(g) Composition of submodels and decomposition in submodels. The first technique consists in developing larger models by interconnecting various submodels. The second consists in extracting a submodel from a larger model.

As a simple but formal example on manipulation one may consider the cascade of two systems. Given $S_{1}$ described by

$$
\begin{array}{l} x _ {1} (t + 1) = A _ {1} (\vartheta_ {1}) x _ {1} (t) + B _ {1} (\vartheta_ {1}) u _ {1} (t), \\ y _ {1} (t) = C _ {1} (\vartheta_ {1}) x _ {1} (t) + D _ {1} (\vartheta_ {1}) u _ {1} (t), \end{array}
$$

and $S_{2}$ described by

$$
\begin{array}{l} x _ {2} (t + 1) = A _ {2} (\vartheta_ {2}) x _ {2} (t) + B _ {2} (\vartheta_ {2}) u _ {2} (t), \\ y _ {2} (t) = C _ {2} (\vartheta_ {2}) x _ {2} (t) + D _ {2} (\vartheta_ {2}) u _ {2} (t), \end{array}
$$

assuming that vectors $u_{2}$ and $y_{1}$ have the same dimension and letting $u_{2}=y_{1}$ the cascade system is defined by

$$
\begin{array}{c} \binom {x _ {1}} {x _ {2}} (t + 1) = \left( \begin{array}{c c} A _ {1} (\vartheta_ {1}) & 0 \\ B _ {2} (\vartheta_ {2}) C _ {1} (\vartheta_ {1}) & A _ {2} (\vartheta_ {2}) \end{array} \right) \binom {x _ {1}} {x _ {2}} \\ \times (t) + \binom {B _ {1} (\vartheta_ {1})} {B _ {2} (\vartheta_ {2}) D _ {1} (\vartheta_ {1})} u _ {1} (t), \\ y _ {2} (t) = \big (D _ {2} (\vartheta_ {2}) C _ {1} (\vartheta_ {1}) C _ {2} (\vartheta_ {2}) \big) \binom {x _ {1}} {x _ {2}} (t) \\ + D _ {2} (\vartheta_ {2}) D _ {1} (\vartheta_ {1}) u _ {1} (t). \end{array}
$$

The resulting symbolic system has input $u_{1}$ , state $(x_{1})_{x_{2}}$ output $y_{2}$ and parameter vector $(\vartheta_{1})_{\vartheta_{2}}$ .

As said above the actual transformations performed by a model management system may well be in-between or combine the items of the above taxonomy.

Note that one could talk, but in a quite different sense from the one adopted in [1], of bottom up approaches for the techniques (a), and for compositions of models and of top down approach for instantiation, simplification and sub-model extraction. Finally there are some tradeoff between the above techniques. For example if a larger library of “template” symbolic models is available, there are more cases in which one may prefer an instantiation technique to a modification technique.

There are also other very important manipulation techniques. Particularly useful might be approximate model simplification. There is some interest in the literature on this topic (see e.g. [8], [9] and the references therein). Another example of important manipulations that the system must be able to perform are some algebraic manipulations that leave invariant a given abstract system as well its variables (including state variables). An example is the comparison of two models for the purpose of testing the occurrence of some relation between the two models, that might require among the other manipulations that the variable be rearranged. This subject is further discussed in section 6. Manipulation techniques are of utmost importance on their own and not only as tools for model building. Thus an ideal model management program should give the user direct control of model manipulations with the possibility of comparing the given model and the transformed one side by side and in action during a simulation session. Thus more than one model must be resident in memory at a given time, and this is one reason why capability 5a must be included in the design of the advanced dynamic model management system. Because the basic motivation to provide this capability is rather self-evident, especially if one bears in mind the preceding discussion on the design principles, it is not necessary to add further comment on it.

All the manipulations and model building techniques require to establish a knowledge base and a context free inference engine that acts on a model according to such knowledge base. The knowledge base is divided in a context free and in a context dependent part. It is most important to achieve a strong separation of these two parts and that the context free part must be maximized and the context dependent part be minimized. The model management system may then switch from a context to another simply invoking a different context dependent knowledge base.

Further very important components must be provided inside the model builder and manipulator. Just has it happens in an expert system which, whenever required, should be able to explain to the user the argument by which a certain conclusion has been reached, in the same way a model builder and manipulator must be able, upon user's request, to explain the process whereby it has come out with a certain numeric or symbolic model. This module represents a non trivial task to the designer especially in terms of user interface, for the difficulty of representing arguments involving model manipulations, and because the explanation should be given either at technical or at informal level, according to the user's request. In addition it is essential in general, but even more in an ill-structured problem context, to provide a model validation module, as further illustrated in the next section.

Finally it is most important to note that of course a system with model building and manipulation capabilities will ensure adaptiveness in problem solving. It has been remarked that this is an important requirement for a DSS. Actually the system we are outlining will be able to modify the model underlying a certain problem solving procedure, so to reflect the changes that may occur in the evolution of the processes represented by the models themselves. In this way the required flexibility and adaptiveness is achieved.

## 5. Robustness and Validation

While a model manipulation will result in a unique transformed model (either numeric or symbolic), we cannot exclude that a modeling problem has many more or less satisfactory solutions. For example, models at various levels of disaggregation may be considered in an economic analysis problem. For a given symbolic model it may be useful to consider slight variations of parameters with respect to their estimated values (as it happens in sensitivity studies). This will be reflected in the behavior of the model builder, which may well propose in certain cases to the user more then one model along with a motivation and a comparative analysis of the features of each model.

An automatic model builder (manipulator) is said to be consistent if, for all input data, it only produces models in standard iso form (or no model at all).

In our context consistency is always ensured since models can be defined only in such a form. However we also require from a model manipulator that it be robust, that it always gives the solution when it exists, and no solution when the solution does not exist. Actually it may happen that the user attempts a manipulation outside its domain (like cascading two systems with mismatching dimensions of the output of the first system and the input of the second). Even more than that, we not only require that the system be able to recognize that the solution to a certain manipulation problem does not exist, but also that it be able to explain the reason.

Formally a model manipulator is said to be robust if it is consistent and it produces the correct solution when and only when such solution exists for any problem submitted to the system.

Before leaving the concept of consistency, some further comments may be useful. Besides the strong theoretical motivation in favor of the adoption of the state space representation (that will be better illustrated later on), an abstract system (model) in standard iso form is always itself consistent, because it obviously admits a unique solution for each initial instant, initial state and input. Thus a major flaw of non state space model building software is that at the end of the modeling process, which may be fairly complex, there is no guarantee that the model produced is consistent. For example the resulting model may not even admit a solution. In such cases the user cannot be protected from a very unfriendly situation, because to fix an inconsistent model needs a good deal of mathematical expertise.

The concept of robustness for model builders is different from the concept of robustness for model manipulators because the class of modeling problems that admit a solution (that is a satisfactory solution), is not so precisely definable as in the case of a manipulation, and, in addition, when the solution exists, it is not usually unique. Hence to evaluate the model builder we have also to evaluate the validity of the models produced for each of a large class of problems submitted to the system. Thus it is convenient to talk both of robustness and credibility of a model builder. This two properties cannot be neatly separated in a model builder. They result from a number of features that altogether give a measure of them. In this respect it is convenient to distinguish the following cases.

(a) In case of contradictory and/or nonsensical indications given by the user the system should try to disambiguate the user description. In the same spirit underlying the design criteria adopted for SUSI, the system should prevent the possibility of making this kind of description. However if the user is able to impose its erroneous description (e.g. because he/she is deliberately trying to fool the system), then the system should refuse to produce any model and be able to explain why no model should be produced. When the system is tested under these circumstances a system failure is registered if a model is produced or no model is produced with a wrong diagnosis, or even worse with no diagnosis at all.

(b) When an acceptable description of a process is achieved with system assistance, and one or more models are produced by the system, the model builder credibility is evaluated from the credibility of the models produced. Such an evaluation is based on methods of model validation and comparison (see e.g. [10]). It is essential that the system itself offer facilities for model validation and comparison.

(c) If, under the same conditions as in (b), the system, even after the elicitation of informations from the user, produces no model, then to decide whether or not a failure should be imputed to the system, it is necessary to verify if an expert (or a panel of experts) is able with the same information to produce a reasonably valid model. A failure may depend on methodology, and/or on inadequate knowledge base and/or inadequate template model base.

Of course our design will aim at achieving the maximum degree of robustness and credibility for a model builder. To this purpose note that obviously the robustness of the model manipulator module is essential both on its own and because a bad model manipulator would also impair the model builder, since the model building process may require a good deal of model manipulations. To evaluate the above properties a substantial software testing and debugging activity is required, which we shall not try to analyze here.

It cannot be excluded however that, once the system has been successfully developed and debugged, because an automatic model builder is necessarily based on a formalized methodology, in certain cases it may well outperform an expert.

Moreover the outlined approach to model building indicates the possibility of inserting in a natural way some basic learning capabilities in the system, which, in this way, will become self-improving. One form of learning originates from the increase in the amount of template models that the modeling activity itself produces. A more sophisticated learning capability can be obtained by connecting the validation module to the module in charge of maintaining the context dependent knowledge base, so as to take advantage of the outcomes of the validation experiments performed to improve such a knowledge base.

We do not explore here more sophisticated learning schemes for the sake of brevity. On the other hand further enhancements in the design of model management systems will derive from progress in the basic sciences of system theory and system engineering. However this requires a specific orientation of research in these fields to the design of software for decision support. Thus current research trends should be reapraised, starting with clarification of improper developments, individuating the results that, even though interesting on their own, have little relevance in the specific context of dynamic model management for decision support systems, the topics that are relevant, but have received too little attention and finally what is lacking. To this purpose is devoted section 8.

## 6. From Data Base Management to Model Base Management

In SUSI the library management is based on numeric model files and simulation data files. The essential functions of loading and saving files are provided. In the design presented in this paper a richer variety of data structures must be handled by the file system because it should now be able to save and load also symbolic models and parameters vectors.

In addition to that, as already noted in [3], it would be desirable to handle these files in the style of data base management system.

In connection to the design of the software module attending these tasks, the classical data base theory would give only a partial answer to the needs of advanced dynamic model management, because it provides only a first superficial structure for the design of the system. In fact the relational structures in classical data base theory are assumed to exist a priori, or to be relatively easily derivable, for example, to answer an user query. This is not the case for models, for which sometimes we may know a priori a change in relational structure, for example because at generation time we know that we have produced a certain model as a submodel of another model, but in other cases the system itself is in charge of the nontrivial derivation of such a structure. This requires that the system has the intelligence of investigating the occurrence of any relation of interest between two given models, or between any two records each of any kind the system is able to generate.

The peculiarity and complexity of these relations also raises the issues as to whether the classical data base structures are adequate for model base management or more suitable ad hoc structures should be devised to address the specific needs arising in this context.

The kind of relationships that might be of interest stem naturally from the preceding discussion and therefore we confine ourselves to a few significant cases. A first obvious example is the model sub-model relation. In addition, two models may stay in the symbolic-numeric model relation, or have a sub-model in common, or be a variant of each other, or have in common a certain set of variables, or being one a simplification or an instantiation or a disaggregation of the other etc. Similarly one may be interested to know, given a certain model, which is the set of all the simulation data records that apply to that model, or that contain time series that might be useful for the simulation of such a model etc.

## 7. Architecture and User Interface

A simplified architecture of the dynamical model management system outlined in this paper is represented in fig. 1. The structure of the system should be rather self-explanatory in view of the preceding discussion, and therefore it does not require further comments.

Rather we would like to comment briefly on the user interface, which has an outstanding importance in qualifying a true decision support system. One of the philosophical points underlying the development of SUSI was that the user interface should be optimized according to the specific task that the system and the user altogether are performing (without neglecting the advantage of certain uniformities of behavior through the whole interface). Thus a system with extended and more sophisticated capabilities requires a much more complex and sophisticated user interface. For instance we have anticipated more extensive window capabilities in general (this in particular is required by capability 5a) and a natural language interface for certain tools like the automatic model builder.

But there is also another major implication of these design enhancements, that consists in the fact that extended and more sophisticated features of the system challenge the designer to remain faithful to the original design criteria illustrated in the introduction. A typical case in question relates the design criteria adopted for SUSI of never defining error conditions. This in SUSI is often achieved correcting user input while it is in progress. On the other hand the new architecture makes provision for an editor and compiler to allow the user to input the formulas expressing the dependence of the model coefficients on the parameter vector. Thus this editor and compiler again should be designed in such a way to prevent the occurrence of any error condition, again possibly correcting the user input while it is in progress.

![](/api/attachments/74J4C9DF/fulltext/images/ef5ee0441319807cd7161f1dfacb1a3fd2e681621f5caf4b3e23d199cd40e471.jpg)  
Fig. 1.

## 8. System Theory: What is Relevant, What is Irrelevant and What is Lacking?

There are far too many books and journals dealing with system theory (and its numerous branch) to try here to give a complete list. Along with the classical books [11] and [12] we confine ourselves to cite the introductory books [13], [9], [14] and [15].

We advise from the outset that the spirit of this section is to stress some relevant links between system theory and DSS, not to give a complete overview of this subject. Thus significant omissions are possible.

The relationship between system theory, together with related field like simulation, control, identification, validation etc., and the design of software for the decision support is of paramount importance. Ultimately system theory determines to a large extent the very approach to the design of software and constitutes the access door to indispensable methodologies cited above. To give just an initial but significant example of the role of system theory consider the fact that the definition itself of abstract system yields the guidelines to determine the software type “model” in a very precise manner. As a matter of fact there is quite a bit of confusion in the literature outside the stream of the state space approach (see e.g. [16]) regarding the concept of model. Note also that the tendency to adopt a concept of model viewed as a coded algorithm is questionable because a model should be anyway an high level abstraction, and hence should not be confounded with an implementation.

This is not to say that the development of system theory is immune from blemishes. As a matter of facts there is a large literature, both old and recent, on the concept of system conceived as a set of input output relations each corresponding to an initial instant of time (see for example the classical books [11], [17]). This concept of system is referred to as IORO in [1]. One can make easily many strong points against this approach. In the first place there is the wild arbitrariness in the choice of even minimal covering of a relation by functions with the same domain as the relation (such a covering is necessary to associate an abstract state to the system). This point is extensively demonstrated and discussed in [18]. In addition and connected to such a point there is a philosophical point. Models are constructed for simulation, control and similar purposes. Now neither control nor simulation (nor any other use of a model) is possible if the effect (output) corresponding to a stimulus (input) applied to the process represented by a model is undetermined as it happens in a relation, for in this case we would be unable to control the process to achieve our objectives. In other words either it is possible to individuate in the process (and hence reflect in the model) a set of conditions (representing the states), each of which standing, to each input there correspond an unique output, or we are forced to conclude that the process in question does not even fall within the scope of any analysis aiming to the above purposes. All these arguments lead naturally to a function space approach to the foundation of system theory, in which an abstract system appears at each initial instant of time as a set of input-output functions with the same domain. It also suggests that usually the states of a model should have, at least in some initial state space in which the model is derived, a precise interpretation as representative of actual states of the real process modeled.

This whole point seems to be completely overlooked in the literature even by the authors that implicitly adhere to the function space approach, but without a foundational justification. The function space approach to the foundation is extensively explored in a series of paper [19], [20] and [21].

Once this approach is adopted another fundamental problem arises. What does it mean that an abstract system is dynamical and what is the relation between the concept of dynamicity and the popular differential (or difference) state space description of real processes? A formal definition of the property of being dynamic (or having memory) along with other properties (first and foremost causality) is given in the above papers and a major upshot of the ensuing theory is that if a system is dynamic and causal then it admits a description is standard iso form and conversely if a model is described in this form then it is necessarily dynamic and causal.

These theoretical results are also consequential from a practical standpoint. Actually in view of them, it is legitimate to affirm that one should either adopt the state space approach (that is the standard iso form) or exhibit a convincing reason to maintain that the process he is modeling is non dynamic and/or non causal. This possibility however is extremely unlikely (see the above references). Needless to say, this statement would be superfluous if there were not a large and growing literature on non state space modeling.

Central to system theory is the theory of the abstract state space. However here a major issue arises regarding the possibility of applying in the present context the results that lean on the concept of abstract state space.

In fact the user of a DSS based on quantitative analysis can communicate with the system essentially via the model variables, that is in the input, state and output variables, and not via abstract variables. Thus we can perform for example a transformation of the state space leaving the abstract system invariant only if we are able to make this transformation transparent to the user (which should keep seeing the same original state variables that have a practical meaning to him) and of course if we can at the same time take some advantage from this transformation. These limitations leave a narrower space for applications of abstract state space techniques. Similarly other model manipulations, like model simplification, should be examined to verify if they can be made transparent to the user or modified in such a way to exploit exclusively the original input, state and output variables.

For space reasons we do not dwell on this point. The interested and mathematically oriented reader may find a more in depth illustration with examples in a earlier version of this paper.

This is a significant example of how a design criterion for the development of a decision support system may call for new orientation in the system theory research.

Notice, incidentally, that our consideration on the concept of state go in the opposite direction of the ones expressed in [22].

With the above words of caution it is already clear from the preceding discussion what are the areas of system theory, and related methodologies, whose progress could produce advances in the design of software for DSS's. A first way to individuate interesting research problems is to make reference to the model manipulation techniques previously discussed. For example the problems of aggregation and approximate simplification of models are already been studied in the literature (see e.g. [8] and [9]). Another relevant line of research would be to develop a symbolic system theory. Actually the contribution exploring the dependence (or independence) of the properties of an abstract system on the values of its parameters (see e.g. [23]) may be considered as fitting into this new branch of system theory, but a much wider attention is deserved in general by symbolic system theory. We are not aware of contributions in the direction of the transparency of abstract state space, whereas of course a good deal of methodologies, first and foremost optimization, do not usually require the use of abstract state spaces.

Further areas of research that are fundamental to the design of decision support systems are those regarding the problem of model bases management, and the development of methods and software for dynamic models validation. Moreover even when a cost or utility index is not considered, and hence no optimization exercise is performed, quite often the need of a realistic modeling suggests that constraints on the variables should be taken into account. This motivates the development of constrained system theory (of course in close connection with optimization theory but also with a certain degree of independence), that also has so far received too little attention (see [24] and [25] and the reference therein).

Finally a most important research area, that for space reason is not treated here, regards the issues arising in the integration of different and not naturally complementary methodologies in the same decision support environment. Such kind of integration should lead, in a hopefully not so far future, to what we call multiparadigm DSS, that are the subject of [26].

## References

[1] T.I. Oren, B.P. Zeigler, M.S. Elzas, Simulation and Model Based Methodologies: An Integrative View, NATO ASI Series, Springer Verlag, 1984.

[2] P. d'Alessandro, and E. De Santis, An Approach to Simulation Software for Discrete Time Models, Proceedings of Telecon '84 Conference, Gerakini, Greece, August 1984.

[3] P. d'Alessandro, M. Dalla Mora and E. De Santis, Linear Dynamic Firm Models: Analysis and Simulation, Proceedings of the 19th HICSS, January 1986, pp. 695–703.

[4] P. d'Alessandro, M. Dalla MOra and E. De Santis, A User Interface for a Decision Support System, Report No. 24-86, Department of Electrical Engineering, University of L'Aquila, January 1986.

[5] J.J. Elam, Creativity Enhancing Design Principles for Decision Support Systems, Proceedings of the 19th HICSS, January 1986, pp. 609–617.

[6] M. Binbasiouglu and M. Jarke, Domain-Specific DSS Tools for Knowledge Based Model Building, Proceedings of the 19th HICSS, January 1986, pp. 503–514.

[7] M. Uschold, N. Harding, R. Muetzelfeldt and A. Bundy, An Intelligent Front End for Ecological Modeling, ECAI '84, Elsevier Publishers B.V. (North Holland), pp. 761–770.

[8] M.S. Mahmoud and M.G. Singh, Large Scale Systems Modeling, Pergamon Press, Oxford, 1981.

[9] M.S. Mahmoud and M.G. Singh, Discrete Systems: Analysis, Control and Optimization, Springer Verlag, 1984.

[10] Preprints of the International Symposium on Criteria for Evaluating the Reliability of Macro-Economics Models, Pisa, December 16–18, 1980, held at the IBM Scientific Center, Pisa.

[11] L.A. Zadeh and C.A. Desoer, Linear System Theory, McGraw Hill, New York, 1963.

[12] L.A. Zadeh and E. Polak, System Theory, McGraw Hill, New York, 1969.

[13] D.G. Luenberger, Introduction to Dynamic Systems: Theory Models and Applications, John Wiley, 1979.

[14] A.V. Balakrishnan, Applied Functional Analysis, Springer Verlag, 1976.

[15] A. Isidori, Nonlinear Control Systems: An Introduction, Springer Verlag, 1985.

[16] J.P. Fry and C.P. Spiguel, A Model Based Information

System: A Framework and Architecture, Proceedings of the 19th HICSS, January 1986, pp. 416–425.

[17] M.D. Mesarovic and Y. Takahara, General System Theory: Mathematical Foundations, Academic Press, New York, 1975.

[18] P. d'Alessandro, The Concept of State and the Axiom of Choice, Journal of the Franklin Institute, Vol. 304, No. 2/3, August/September 1977, pp. 87–99.

[19] P. d'Alessandro, G. Rinaldi and A. Sassano, A Function Space Approach to the Foundations of System Theory, International Journal of System Science, Vol. 14, No. 7, 1983.

[20] P. d'Alessandro and M. Piccioni, Differential Representation for a General Class of Linear Systems, International Journal of System Science, Vol. 16, No. 3, pp. 361–366, 1985.

[21] P. d'Alessandro and M. Dalla Mora, Systems, Memory, Causality, Evolution and Recursive Equations, Computer & Mathematics with Applications, Vol. 10, No. 1, pp. 61–69, 1984, Pergamon Press.

[22] B.P. Zeigler, Systems theoretic foundations of modeling and simulation, Proceedings of NATO Advanced School on Simulation and Model-Based Methodologies: An Integrative View, Springer Verlag, 1984.

[23] J.L. Willems, Structural controllability and observability, Systems & Controls Letters, 8 (1986) 5–12.

[24] P. d'Alessandro, M. Dalla Mora and E. De Santis, On Consistency of Linear Linearly Constrained Discrete Time Systems, International Journal of the Franklin Institute, vo. 319, No. 4, pp. 423–430, April 1985.

[25] P. d'Alessandro, M. Dalla Mora and E. De Santis, On Discrete Time Linear Systems over Cones, Systems & Control Letters, 6 (1985), pp. 271–275, North Holland.

[26] P. d'Alessandro, M. Dalla Mora and E. De Santis, A Perspective of DSS Evolution: Multiparadigm DSS, Report No. 28/87, October 1987, Department of Electrical Engineering, University of L'Aquila.
