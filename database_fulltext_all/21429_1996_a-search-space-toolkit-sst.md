---
otero_id: 21429
otero_key: "M6CNFTWS"
title: "A search space toolkit: SST"
authors: "Andrew Gelsey; Don Smith; Mark Schwabacher; Khaled Rasheed; Keith Miyake"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)80009-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A search space toolkit: SST

Andrew Gelsey $^{*}$ , Don Smith, Mark Schwabacher, Khaled Rasheed, Keith Miyake

Computer Science Department, Rutgers University, New Brunswick, NJ 08903, USA

Received 27 March 1995; revised 2 August 1995; accepted 27 January 1996

## Abstract

The Search Space Toolkit (SST) is a suite of tools for investigating the properties of the continuous search spaces which arise in designing complex engineering artifacts whose evaluation requires significant computation by a numerical simulator. SST has been developed as part of NDA, a computational environment for (semi-)automated design of jet engine exhaust nozzles for supersonic aircraft which resulted from a collaboration between computer scientists at Rutgers University and design engineers at General Electric and Lockheed. Though the design spaces for this sort of engineering artifact are mainly continuous, they typically include features such as unevaluable points, multiple local optima, and large derivatives which cause difficulties for standard numerical optimization methods. The search spaces which SST explores also differ significantly from the discrete search spaces that typically arise in artificial intelligence research, and properly searching such spaces requires a synergistic combination of numerical methods and AI techniques and is a fundamental AI research area. By promoting the design space to be a first class entity, rather than a “black box” buried in the interface between an (unconstrained) optimizer and a simulator, SST allows a more principled approach to automated design.

Keywords: Continuous search spaces; Complex engineering artifacts design; Numerical simulator

## 1. Introduction

Various researchers have addressed decision making problems with unified approaches which merge optimization techniques with artificial intelligence techniques. Approaches using optimization in conjunction with subfields of AI including case-based reasoning $[12]$ and other machine learning $[22,21]$ constraint satisfaction problems $[13]$ , and rule-based systems $[14]$ have been explored. In the present article we extend the research on unified AI/optimization approaches, focusing on the combination of optimization with ideas from two subfields of AI: search and problem formation.

The Search Space Toolkit (SST) is a suite of tools for investigating the properties of continuous search spaces. The search spaces which SST explores differ significantly from the discrete search spaces that typically arise in artificial intelligence research, and properly searching such spaces is a fundamental AI research area. Our SST research has focused on the problem of designing complex engineering artifacts and the analysis of the associated search spaces. Evaluation of points within these search spaces requires significant computation by a numerical simulator. The knowledge of search space properties which SST extracts can be used as a basis for AI-augmented optimization, in which numerical optimization algorithms are supplemented by AI techniques to improve their ability to find optima in complex, realistic search spaces.

![](/api/attachments/M6CNFTWS/fulltext/images/94d12536c3ebaf2d40178565bd024fcce1ad4acbbf275825f399e00701af4084.jpg)  
Fig. 1. Axisymmetric convergent-divergent exhaust nozzle (flow from left to right).

SST has been primarily developed as part of the Nozzle Design Associate (NDA) project [7]. NDA is a computational environment for (semi-)automated design of jet engine exhaust nozzles for supersonic aircraft. NDA was developed in a collaboration between computer scientists at Rutgers University and design engineers at General Electric and Lockheed. The NDA project has two principal goals: to provide a useful engineering tool for exhaust nozzle design, and to explore fundamental research issues that arise in the application of automated design optimization methods to realistic engineering problems.

Fig. 1 shows the class of nozzles supported by the current NDA, the axisymmetric scheduled convergent-divergent exhaust nozzles often found in supersonic aircraft [15]. In Fig. 1, $r_{10}$ , $r_e$ , and $r_7$ are fixed radii, and $r_8$ and $r_9$ are radii which are mechanically varied during aircraft operation. $r_{10}$ is the outer radius of the engine to which the nozzle is attached, $r_e$ is the radius of the duct leaving the engine, $r_7$ is the radius of the duct at the beginning of the movable convergent section of the nozzle, $r_8$ is the (variable) radius of the nozzle throat, and $r_9$ is the (variable) nozzle exit radius. Mechanically, this nozzle is a four-bar linkage, with three movable links labeled in Fig. 1 by their lengths $l_c$ , $l_d$ , and $l_e$ . During aircraft operation, the linkage is moved to change $r_8$ so that the cross-sectional area at the nozzle throat will produce desired engine performance. Since a four-bar linkage has one degree of freedom, setting $r_8$ also sets $r_9$ . The job of NDA is to choose values for the parameters $l_c$ , $l_d$ , and $l_e$ that give optimal performance for a particular aircraft and flight mission.

Fig. 2 shows what might be called a “naive” approach to design automation: simply combine a standard optimizer with a simulator capable of evaluating candidate designs. Unfortunately, simulators are typically written with the assumption that they will be invoked by experienced human users, and making them robust enough for use in an automated environment like Fig. 2 can be demanding. Even when some software engineering has been done to make the simulator and optimizer capable of working together, optimization results tend to vary widely, as illustrated by the example in Fig. 3, in which an exhaust nozzle simulator is combined with a number of different optimization algorithms from [20] and [11]. In Fig. 3, each optimizer was started at the same point and run until it could find no further design improvement. The vertical axis in Fig. 3 shows the deviation of the design quality of each point found by an optimizer from the best point found by any method, and the horizontal axis shows the number of iterations used to reach each point. In Fig. 3, we sort the optimization methods into groups: those whose deviation was small enough to be “acceptable” for the current design goals, and those with larger, unacceptable deviation.

![](/api/attachments/M6CNFTWS/fulltext/images/67e9f7be59a9fdfde630d8fa5ba24120d1369898cb80dbb0f7bff37a41792076.jpg)  
Fig. 2. Simple simulate/modify loop.

![](/api/attachments/M6CNFTWS/fulltext/images/481bd3c635b6c717966ce50522b3181b9d89df0d7bf2f4ce879bd4d97af2ed31.jpg)  
Fig. 3. Experimental data showing quality of termination points of various optimization methods.

Fig. 4 illustrates an alternative way of looking at the problem of automated design optimization. The viewpoint here is that the simulator implicitly defines a search space, which in turn is searched by the optimizer. The premise of our SST research is that automated design optimization has a much better chance of success if this search space is treated as a distinct entity whose geometry and topology should be investigated by a variety of computational tools, rather than as a “black box” buried in the interface between an optimizer and a simulator.

In the current version of NDA, the design parameters defining the search space are the lengths of the convergent, divergent, and external nozzle flaps ( $l_{c}$ , $l_{d}$ , and $l_{e}$ in Fig. 1). NDA optimizes the nozzle design under the constraint that the aircraft must be able to complete its designated mission, and with the goal that cost should be minimized. NDA currently uses gross takeoff mass as an approximation for cost, as takeoff mass is a rough combination of both acquisition cost (approximated by dry mass) and operating cost (approximated by fuel mass). To compute gross takeoff mass, NDA uses a detailed numerical simulation of the relevant physics [7].

![](/api/attachments/M6CNFTWS/fulltext/images/d5e506a49b0159e7272cd2ad1af56bb94cd4714bb1a5b8cb69b70facbad16cc0.jpg)  
Fig. 4. Optimizer searches space induced by simulator.

Section 3 of this article describes search space properties of interest for design automation, Section 4 describes the tools in SST for investigating search space properties, and Section 5 discusses our experiments in “AI-augmented optimization”, in which knowledge of the design search space acquired by the search space toolkit is used to improve the ability of numerical optimizers to find an optimal design.

## 2. Related work

[13] describes UNIK-OPT, a knowledge-assisted optimization model formulation system. [12] describes UNIK-CASE, which uses case-based methods to provide knowledge for use by UNIK-OPT. [14] describes a framework which unifies an optimization model with a rule-based system.

A great deal of work has been done in the area of numerical optimization algorithms $[8,25,18,16,17]$ though not much has been published about the particular difficulties of attempting to optimize functions defined by large “real-world” numerical simulators. Search has been a key focus of AI research from the field’s beginning $[5]$ , but most of the attention has been on discrete rather than continuous objective functions. A number of research efforts have combined AI techniques with numerical optimization $[24,19,3,2,23,1,27,10,4]$ , but automated identification of search space properties has not been a focus in this work.

Other work in our Rutgers AI/Design research group used machine learning $[26]$ to improve optimization by generating abstractions and decompositions of the search space $[6]$ , by selecting a prototype defining an appropriate search space for a given design goal $[22]$ and by reformulating the search space through the incorporation of constraints into the design modification operators $[21]$ .

## 3. Search space properties

Fig. 5 lists a number of search space properties that are likely to be important in searching the space

• number of local optima

\- convexity

\- "depth" of local optima

\- smoothness; continuity of $n^{\text{th}}$ derivative

\- local properties in piecewise smooth regions

\- evaluability of objective function

• topology/geometry of evaluable region

\- constraints: explicit, implicit

\- ridges; valleys

\- plateaus

Fig. 5. Search space properties.

for an acceptable design. One extremely important property of a search space is the number of local optima. Search techniques that work well on a space with a single local optimum, which is therefore the global optimum, may be ineffective for spaces with multiple local optima. Which search techniques are most appropriate will depend greatly on the number of local optima. If it is possible to show that the objective function is “convex” (Hessian matrix positive-definite everywhere) and that the feasible region is convex (geometric sense) then the function can have at most one local optimum [25]. An associated property is the “depth” of the local optima, i.e., how much worse the objective function gets before leaving the basin of attraction of a local optimum.

Numerical optimization algorithms $[25]$ tend to be quite sensitive to the smoothness of the objective function. SST focuses on problems in which the objective function to be optimized by the search process is computed by a complex numerical simulation of the physics of the artifact being designed. Such an objective function is often not very smooth. Continuity of the objective function itself is important for almost any numerical optimizer, and degree of smoothness (i.e., continuity of the first, second, or even higher derivatives) is important for several optimization methods.

As we will discuss in the following section, SST builds a global picture of a search space by combining information gathered at different local points. For example, if a point is suspected of being a local optimum, information about derivatives of the objective function should be gathered. If the objective function is not smooth at the point under consideration, then the neighborhood about the point should be divided into piecewise smooth regions so derivatives can be computed (numerically) in each region. The gradient (vector of first partial derivatives of the objective function with respect to the design parameters) is an important piece of data, since if it is zero that often indicates that a point is a local optimum. The Hessian (matrix of second partial derivatives of the objective function with respect to pairs of design parameters) is also useful, and if the Hessian is diagonalized, its eigenvalues and eigenvectors may indicate important directions in the search space.

An issue of great practical importance that tends to be ignored by AI work on search and by work in numerical optimization is the evaluability of the objective function. In designing a complex engineering artifact, the objective function is computed by numerical simulation. The numerical simulator is in effect “executing” a model of the physical system being designed, and like any model of physics this model must be based on various approximations and simplifying assumptions. However, it is quite likely that some combinations of values for the design parameters will result in physical configurations that violate the assumptions upon which the model is based, thus making the objective function unevaluable at that point of the search space.

One obvious “fix” for an objective function which is not evaluable everywhere is to extend the simulator to use a more complete model which is consistent with the “bad” set of parameters. However, this effort typically cannot be justified unless it is likely that the unevaluable regions contain good designs. Often the good designs themselves will in fact satisfy the model assumptions. For example, certain sets of parameter values for the exhaust nozzle in Fig. 1 will make it impossible to bring the exhaust to a supersonic velocity under certain flight conditions. In this case, the nozzle will have a very low thrust and thus be a bad design. However, the basic nozzle model depends on the assumption that flow will become supersonic in part of the nozzle, so this set of nozzle parameters will actually not be evaluable by the simulator. The problem is that, while this design is not a good one, it may be encountered by an optimizer as it searches the design space, and since it is unevaluable, the optimizer will have no information to guide it towards better regions of the search space.

Thus the topology and geometry of the evaluable region $^{1}$ of the search space are important properties. A basic topological question is whether the evaluable region is connected. If the evaluable region has several disconnected components, then it is quite unlikely that a search started in one component will ever make its way into a different component. If it turns out that the evaluable region is connected, then a second question is whether it is simply connected, or if there are “holes” – pockets of unevaluable points inside the evaluable region. Geometrical properties may also be important: for example, whether the evaluable region is a convex geometric shape.

Constraints on the allowable set of solutions within the search space are also an important property. Explicit constraints will typically be clear from the problem statement, but as the discussion above indicates, there may also be implicit constraints such as not violating modeling assumptions. By an “implicit constraint”, we mean a constraint which is satisfied at design points where the simulator is able to finish its computation and return a value for the objective function, and which fails to be satisfied at design points where the simulator “crashes” and cannot compute a value for the objective function. Ideally, simulators should never crash, but “real-world” engineering simulators often do, unfortunately.

Ridges, valleys (“negative ridges”), and plateaus are also important search space features. Ridges and valleys are regions in which movement in a particular direction causes the objective function to change very rapidly, potentially masking weaker changes in an orthogonal direction which may nevertheless eventually lead to improvement of the objective function. Plateaus are regions where the objective function changes very slowly – they may trap optimizers.

## 4. Tools

The organization of SST follows a “toolkit” approach rather than an “environment” approach: different capabilities are implemented in different “tools” (programs) which the user runs from an operating system “shell”, rather than from a special SST environment. Some SST tools also internally call other SST tools.

As mentioned in the previous section, the number of local optima is a critical property. Unfortunately, for an objective function defined by a large numerical simulation program, the information we are able to obtain about the number of local optima will generally be statistical in nature, rather than the subject of a mathematical proof. SST uses a Monte-Carlo-like multistart method for estimating the number of local optima: the algorithm repeatedly chooses random combinations of design parameters, uses the resulting design as a starting point for a numerical optimizer, and sorts the termination points of the optimizations into bins. (A byproduct of this process may be the identification of a global optimum, which is the best of the local optima.)

Of the nine numerical optimizers we have tried, the best performance in terms of speed and reliability was produced by CFSQP, a state-of-the-art implementation of the Sequential Quadratic Programming method [11]. Sequential Quadratic Programming is a quasi-Newton method that solves a nonlinear constrained optimization problem by fitting a sequence of quadratic programs $^{2}$ to it, and then solving each of these problems using a quadratic programming method. Fig. 6 shows results of a multistart using CFSQP in the NDA nozzle design search space. For ten optimization runs all with different randomly generated starting points, Fig. 6 shows the takeoff mass (in kilograms) and nozzle flap lengths (in inches) of the best nozzle design found by the optimizer with each starting point. (As described in Section 1, the design goal is to minimize takeoff mass while satisfying mission requirements.) CFSQP terminated when it could find no further local improvement, and Fig. 6 shows how many function evaluations (i.e., mission simulations) occurred during the optimization. Note that the space appears to have two local optima.

<table><tr><td>start point</td><td>takeoff mass</td><td> $l_c$ </td><td> $l_d$ </td><td> $l_c$ </td><td>function evaluations</td><td>local optimum</td></tr><tr><td>1</td><td>306525.8</td><td>4.4</td><td>37.5</td><td>57.4</td><td>299</td><td>A</td></tr><tr><td>2</td><td>306526.9</td><td>4.3</td><td>37.2</td><td>57.0</td><td>387</td><td>A</td></tr><tr><td>3</td><td>306527.2</td><td>4.3</td><td>37.0</td><td>56.8</td><td>231</td><td>A</td></tr><tr><td>4</td><td>306524.7</td><td>4.3</td><td>37.3</td><td>57.1</td><td>351</td><td>A</td></tr><tr><td>5</td><td>306995.1</td><td>2.6</td><td>35.2</td><td>52.7</td><td>371</td><td>B</td></tr><tr><td>6</td><td>306526.6</td><td>4.4</td><td>37.7</td><td>57.7</td><td>355</td><td>A</td></tr><tr><td>7</td><td>306995.1</td><td>2.6</td><td>35.2</td><td>52.7</td><td>475</td><td>B</td></tr><tr><td>8</td><td>306524.9</td><td>4.4</td><td>37.3</td><td>57.2</td><td>261</td><td>A</td></tr><tr><td>9</td><td>306995.1</td><td>2.6</td><td>35.2</td><td>52.7</td><td>517</td><td>B</td></tr><tr><td>10</td><td>306525.0</td><td>4.3</td><td>37.4</td><td>57.3</td><td>305</td><td>A</td></tr></table>

Fig. 6. Multistart using CFSQP to minimize aircraft takeoff mass.

SST currently addresses the issue of objective function evaluability by a fixed grid sampling technique, both on large regions and on selected subregions of a search space. In the NDA exhaust nozzle search space, if SST imposes a grid on a large section of the search space spanning the “reasonable” range of values for the design parameters, sampling the grid points reveals that only about 4% of the grid points are evaluable. These grid points are contiguous, and form a “slab-shaped” evaluable region. Fig. 7 graphically portrays the appearance of this slab using the AVS (Advanced Visualization

System) scientific visualization software. In the current NDA, the space of possible nozzle designs is three dimensional, since we only allow NDA to vary the three parameters $l_{c}$ , $l_{d}$ , and $l_{e}$ , the lengths of the movable nozzle flaps. SST does not detect internal pockets of unevaluable points within this slab, suggesting that the evaluable region in this space is simply connected. The boundaries of this slab are implicit constraints on the acceptable combinations of design parameters for this problem. For the purpose of performing design optimization, when computing partial derivatives the NDA dynamically modifies the derivative step size and direction in order to avoid the unevaluable region, and a software wrapper returns to the optimizer a large “bad” value for unevaluable points that are encountered outside of gradient computation (i.e., a large nonsmooth penalty function is applied at unevaluable points).

Several of the SST tools have led us to the conclusion that the gross structure of the NDA nozzle design space is that of a valley. The SST fixed grid sampling reveals that the slab-like evaluable region has a thin surface running midway between the flat boundaries of the slab which contains designs much better than their neighbors closer to the outside of the slab. The optimizations run by the Monte-Carlo-like multistart techniques tend to stop on this central surface, though many of the stopping points are not true local minima. If the Hessian matrix for a point on this central surface is diagonalized, one eigenvalue is much larger than the others, and its corresponding eigenvector is normal to the central surface. This data gathered by SST strongly suggests that the central surface running through the middle of the slab is a higher dimensional analog of a ridge. The nozzle design objective function is an approximation of cost, which should be minimized, so we refer to this ridge as a “valley” and we refer to the central surface in the slab as the “valley floor”. Optimizers tend to stop soon after finding the valley floor because the gradients driving the optimization towards the valley floor are very strong and tend to mask the much weaker gradients along the valley floor.

![](/api/attachments/M6CNFTWS/fulltext/images/cbd1602557e760282f691862f7dfbaca3c1bfeebcbba90831897b6c170a761df.jpg)  
Fig. 7. The “slab-shaped” evaluable region. (We normally display this in color on a workstation screen, with differing colors indicating differing design quality.)

Fig. 8 shows how the objective function varies about a “typical” optimization stopping point as a function of change in design space parameters ( $l_{c}$ , $l_{d}$ , and $l_{e}$ in Fig. 1), and indicates that the gradient is approximately zero and the second derivatives positive, so that it was “legitimate” for the optimizer to stop here. Fig. 9 shows how the objective function varies about the same optimization stopping point as a function of combinations of parameters in the direction of the eigenvectors of the Hessian at this point. Here we see that there may in fact be a “downhill” direction which is a linear combination of the eigenvectors corresponding to the two smaller eigenvalues, but that the other much larger eigenvalue is “masking” this possibility for improvement.

There is more to a search space than its gross structure. If gross analysis reveals that a search space is a valley, the next natural question is “what is the structure of the valley floor?”. To investigate this issue, SST includes a tool we call “dimension reduction”. The floor of a valley can be considered a search space in its own right, but a search space of dimensionality one less than that of the primary search space. Though the valley floor space has fewer dimensions, it may still have a very complex structure. To ascertain the properties of this subspace without having them masked by the strong gradients in the rest of the primary search space, SST must limit its evaluations to points exactly on the valley floor.

The SST dimension reduction algorithm works by projecting the desired subspace onto a hyperplane tangent to the subspace at some point. (A limitation of our current version of this algorithm is that it works poorly for subspaces with high curvature.)

![](/api/attachments/M6CNFTWS/fulltext/images/bf76e0e7c1a00b52164e0c44e3c7b6331ac2f32a246a441b75ffa036030945fa.jpg)  
Fig. 8. Objective as function of $\Delta l_{c}$ , $\Delta l_{d}$ , and $\Delta l_{e}$ .

a) Large scale

![](/api/attachments/M6CNFTWS/fulltext/images/a8a084e73f81c5f830d9821a884495f4dbb9201a6ab52687bef5e9ca0be9aa5d.jpg)

![](/api/attachments/M6CNFTWS/fulltext/images/a2d775a438d1afc893c9c8a8c21c3bd6e79df914dd1c5e09af5ba678b7ce8fe9.jpg)  
Fig. 9. Objective function variation in directions of Hessian eigenvalues. (a) Large scale, (b) Close-up view.

![](/api/attachments/M6CNFTWS/fulltext/images/556a681968a55aaa1a3ac7a2e4487bd4e7fc4723a0cd80fe205fa9ea1aa192b7.jpg)  
Fig. 10. Valley floor structure for NDA nozzle design space (one dimension less than full nozzle design space).

Linear algebra gives a coordinate system for the hyperplane with one less dimension than the primary space. This coordinate system then serves as a coordinate system for the subspace by identifying each point $P_{s}$ in the subspace with the nearest point $P_{h}$ on the hyperplane (i.e., the line defined by $P_{s}$ and $P_{h}$ is normal to the hyperplane.) Thus each function evaluation in the reduced dimension subspace requires a search in the primary space along the line normal to the corresponding point on the hyperplane in order to find the intersection with the subspace and evaluate the point of intersection. If the subspace is the valley floor in the nozzle search space, then each function evaluation requires solving a one-dimensional minimization problem, because the line normal to the hyperplane (just a plane in this case) will have its minimum value of the objective function where it intersects the valley floor.

The SST dimension reduction algorithm has been applied to the NDA nozzle design search space. By combining the dimension reduction algorithm with our fixed grid sampling technique, we were able to determine the structure of the valley floor for the nozzle design space. Fig. 10 shows the reduced dimension nozzle design space computed by this algorithm. This “valley floor” space has one less dimension than the full 3D nozzle design space. (Fig. 11 shows a contour plot of the same data).

Fig. 12 and Fig. 13 show “closeups” of the valley floor near the global optimum. Here a finer fixed grid sampling of the dimension-reduced space

![](/api/attachments/M6CNFTWS/fulltext/images/ec576971df66c5225415fbdc3dbf74e1204e02d7d65678bdb167ed16e2bc5ace.jpg)  
Fig. 11. Valley floor contour plot.

![](/api/attachments/M6CNFTWS/fulltext/images/ef1c6d803b5e6cab5521c1e941da57015cd7461efdfa4a74501e94f180558d49.jpg)  
Fig. 12. Valley floor structure (closeup view).

has been used. $^{3}$ Note that the range of takeoff masses (vertical axis in Fig. 12) does not range as high as in Fig. 10 and Fig. 11. Also note the apparent presence of two local optima, which is particularly clear in Fig. 12. The locations of these optima are the same (to within grid spacing) as the locations of the two local optima found by the multistart of Fig. 6, providing an internal consistency check between the two methods.

The use of scientific visualization software to display an entire search space is only possible for a three-dimensional search space, as in the visualization shown in Fig. 7. However, extensions of the search space toolkit dimension reduction algorithms may be useful for extracting two- or three-dimensional “slices” of higher dimensional search spaces which can then be displayed using visualization techniques for 3D spaces (as used in Fig. 7) or 2D spaces (as used in Figs. 10–13).

## 5. AI-augmented optimization

The search space properties which SST extracts can be used as a basis for AI-augmented optimization, in which numerical optimization algorithms are supplemented by AI techniques to improve their ability to find optima in complex, realistic search spaces. A particular form of AI-augmented optimization is the use of problem reformulation to improve optimizer performance. Problem reformulation has long been an important area of theoretical AI research – here we demonstrate that problem reformulation can have practical benefits as well.

![](/api/attachments/M6CNFTWS/fulltext/images/e57b65de565b996023c1fab4edddd3dab4423a87e7a9d7aea648fb93c084d08e.jpg)  
Fig. 13. Valley floor contour plot (closeup view).

![](/api/attachments/M6CNFTWS/fulltext/images/e294c96e4bacdc170546b50d3ce92f17078f8146f28ca16b52d0e174fbc55030.jpg)  
Fig. 14. Reformulations of the exhaust nozzle design problem.

Several possible problem reformulations are suggested by the characteristics of the NDA nozzle design search space which SST identifies. Fig. 14 shows some problem reformulations we have investigated. In each case, the reformulated problem involves three design parameters. In Case 0 of Fig. 14, which is the original nozzle design problem described in Section 1, the three parameters are the lengths of the three movable nozzle flaps. The other three cases involve transformed sets of parameters which are described below.

We implement each particular problem reformulation by means of a software mediator which we call a “wrapper”, as shown in Fig. 15. To external agents such as optimizers or the SST, the wrapper “looks” just like the core nozzle simulator – they both accept three design parameters and return a single measure of merit. To the core nozzle simulator inside, the wrapper “looks” just like the external agents that typically invoke it. Thus we can experiment with any reparameterization of the nozzle design problem without having to change any software other than the wrapper itself.

Both the very large-scale information in Fig. 7 and the very small-scale information in Fig. 8 and Fig. 9 indicate the importance of the spatial direction normal to the slab. One natural problem reformulation is Case 1 in Fig. 14, a linear transformation which rotates the coordinates of the search space so that the slab in Fig. 7 is oriented parallel to the coordinate axes. This new orientation has two advantages: multistart can randomly select starting points in a box with much higher density of evaluable points, and numerical differentiation in the directions along the slab will tend to be more accurate since the direction of rapid change normal to the slab will not be mixed into the calculation. Fig. 16 shows the results of a multistart CFSQP in this rotated space: the optimizations reach the same two optima as the earlier CFSQP multistart in Fig. 6, but the average number of function evaluations required dropped by 25% compared with Fig. 6, yielding a corresponding improvement in speed.

![](/api/attachments/M6CNFTWS/fulltext/images/0c4df87b89299ab5b94b220140618a37efdb770afe7ec9cbcc9ef1558d67bcd8.jpg)  
Fig. 15. Wrappers for exhaust nozzle design problem.

Case 2 in Fig. 14 is a more complex sort of problem reformulation. The motivation for this reformulation is to create a more intuitive design space. The original design space of three flap lengths gives very little suggestion of what flap lengths might lead to a good design, and as Fig. 8 and Fig. 9 indicate, the original space has very bad designs which are very “close” to all the good designs. The nonlinear problem reformulation in Case 2 of Fig. 14 keeps the external flap (see Fig. 1) as part of the nozzle design, but instead of specifying the other two flap lengths, the cross-sectional area of the nozzle at its exit is specified in a nondimensional fashion at two points during the aircraft’s mission. The nondimensionalization used is to specify a ratio of the actual exit area to the ideal exit area for a perfect nozzle at the same point in the mission. Thus if these two parameters have the value 1, the nozzle will work perfectly at those two points in the mission. The optimizer still needs to vary these values, since the best overall nozzle design for a mission will typically not be best at any particular point in the mission – it is a compromise. Fig. 17 shows the results of a multistart CFSQP in this transformed space: the optimizations reach the same two optima as the earlier CFSQP multistart in Fig. 6, but the average number of function evaluations required dropped by 20% compared with Fig. 6, yielding a corresponding improvement in speed. Note also that CFSQP typically achieves a slightly better design quality in this transformed space by more accurately computing the global optimum, perhaps because the problem reformulation makes it possible to compute gradients with less roundoff error.

<table><tr><td>start point</td><td>takeoff mass</td><td> $p_1$ </td><td> $p_2$ </td><td> $p_3$ </td><td>function evaluations</td><td>local optimum</td></tr><tr><td>1</td><td>306524.7</td><td>-9.0</td><td>43.4</td><td>51.9</td><td>274</td><td>A</td></tr><tr><td>2</td><td>306524.9</td><td>-9.0</td><td>43.6</td><td>52.2</td><td>203</td><td>A</td></tr><tr><td>3</td><td>306525.0</td><td>-9.0</td><td>43.3</td><td>51.7</td><td>213</td><td>A</td></tr><tr><td>4</td><td>306995.2</td><td>-8.6</td><td>39.1</td><td>49.2</td><td>228</td><td>B</td></tr><tr><td>5</td><td>306995.1</td><td>-8.7</td><td>39.1</td><td>49.2</td><td>233</td><td>B</td></tr><tr><td>6</td><td>306524.9</td><td>-9.0</td><td>43.5</td><td>52.1</td><td>210</td><td>A</td></tr><tr><td>7</td><td>306524.8</td><td>-9.0</td><td>43.4</td><td>51.9</td><td>384</td><td>A</td></tr><tr><td>8</td><td>306524.7</td><td>-9.0</td><td>43.5</td><td>52.0</td><td>214</td><td>A</td></tr><tr><td>9</td><td>306524.9</td><td>-9.0</td><td>43.5</td><td>52.1</td><td>165</td><td>A</td></tr><tr><td>10</td><td>306524.7</td><td>-9.0</td><td>43.4</td><td>51.8</td><td>591</td><td>A</td></tr></table>

Fig. 16. Multistart CFSQP in rotated space.

<table><tr><td>start point</td><td>takeoff mass</td><td> $e_1$ </td><td> $e_2$ </td><td> $l_e$ </td><td>function evaluations</td><td>local optimum</td></tr><tr><td>1</td><td>306524.7</td><td>0.95</td><td>1.00</td><td>57.1</td><td>294</td><td>A</td></tr><tr><td>2</td><td>306524.7</td><td>0.95</td><td>1.00</td><td>57.1</td><td>661</td><td>A</td></tr><tr><td>3</td><td>306995.1</td><td>0.94</td><td>1.04</td><td>52.7</td><td>258</td><td>B</td></tr><tr><td>4</td><td>306524.7</td><td>0.95</td><td>1.00</td><td>57.1</td><td>173</td><td>A</td></tr><tr><td>5</td><td>306524.7</td><td>0.95</td><td>1.00</td><td>57.1</td><td>169</td><td>A</td></tr><tr><td>6</td><td>306524.7</td><td>0.95</td><td>1.00</td><td>57.1</td><td>490</td><td>A</td></tr><tr><td>7</td><td>306524.7</td><td>0.95</td><td>1.00</td><td>57.1</td><td>195</td><td>A</td></tr><tr><td>8</td><td>306524.7</td><td>0.95</td><td>1.00</td><td>57.1</td><td>157</td><td>A</td></tr><tr><td>9</td><td>306524.7</td><td>0.95</td><td>1.00</td><td>57.1</td><td>161</td><td>A</td></tr><tr><td>10</td><td>306524.7</td><td>0.95</td><td>1.00</td><td>57.1</td><td>252</td><td>A</td></tr></table>

Fig. 17. Multistart CFSQP with nonlinear problem reformulation.

Case 3 in Fig. 14 is a compromise between Case 0 and Case 2 – it retains two of the original nozzle flap lengths and only uses one nondimensionalized exit area. Fig. 18 shows optimization results in this space. Here the average number of function evaluations required dropped by 43% compared with Fig. 6, yielding a corresponding improvement in speed. Note that the seventh stopping point in this example (marked as \*\*\*) is not one of the local optima encountered before. In fact, investigation using SST revealed that this stopping point is not a true local optimum at all: at this point the gradient of the objective function points directly into an unevaluable region of the search space, so CFSQP was unable to achieve further local improvements in takeoff mass.

In order to test the generality of the problem reformulations of Fig. 14, we also tested their impact on the performance of genetic algorithms [9] for finding the optimal design for the NDA exhaust nozzle. The algorithm used combined classical methods with new ideas inspired from the search space structure revealed through the use of SST, and gave comparable results to the multistart CFSQP.

<table><tr><td>start point</td><td>takeoff mass</td><td> $e_0$ </td><td> $l_c$ </td><td> $l_e$ </td><td>function evaluations</td><td>local optimum</td></tr><tr><td>1</td><td>306524.7</td><td>0.93</td><td>4.3</td><td>57.0</td><td>202</td><td>A</td></tr><tr><td>2</td><td>306524.7</td><td>0.93</td><td>4.3</td><td>57.1</td><td>188</td><td>A</td></tr><tr><td>3</td><td>306526.9</td><td>0.93</td><td>4.3</td><td>57.0</td><td>147</td><td>A</td></tr><tr><td>4</td><td>306524.7</td><td>0.93</td><td>4.3</td><td>57.1</td><td>114</td><td>A</td></tr><tr><td>5</td><td>306524.7</td><td>0.93</td><td>4.3</td><td>57.1</td><td>255</td><td>A</td></tr><tr><td>6</td><td>306524.7</td><td>0.93</td><td>4.3</td><td>57.1</td><td>238</td><td>A</td></tr><tr><td>7</td><td>308257.9</td><td>0.78</td><td>2.2</td><td>53.4</td><td>245</td><td>***</td></tr><tr><td>8</td><td>306524.7</td><td>0.93</td><td>4.3</td><td>57.1</td><td>217</td><td>A</td></tr><tr><td>9</td><td>306524.8</td><td>0.93</td><td>4.3</td><td>57.0</td><td>214</td><td>A</td></tr><tr><td>10</td><td>306524.7</td><td>0.93</td><td>4.3</td><td>57.0</td><td>185</td><td>A</td></tr></table>

Fig. 18. Multistart CFSQP with Case 3 problem reformulation.

The genetic algorithm (GA) we implemented uses selection, mutation and crossover operators to search for the global optimum. Each run of the GA was more expensive than a single CFSQP run, but the higher cost can be justified by the higher degree of confidence in reaching the global optimum.

An individual in the GA was represented by a sequence of three real numbers representing the flap lengths (or other parameters in the case of reformulation), and the fitness of the individual was based on the takeoff mass of the corresponding aircraft design. A starting population was generated at random to start the algorithm.

Selection by rank, a method in which the population is maintained in sorted order according to fitness and the chance of an individual being selected depends on its order rather than its actual fitness, was used. This strategy was used instead of the classical roulette wheel selection strategy due to the relatively narrow fitness range (takeoff mass spectrum) in this problem. If roulette wheel selection were used, the simple fitness measure, which is inversely proportional to takeoff mass, would lead to near random selection and very slow convergence. On the other hand, using a more complicated fitness measure would make the performance dependent to a large extent on the robustness of the measure used, thus introducing unnecessary complexity.

![](/api/attachments/M6CNFTWS/fulltext/images/8c7cfc60fd9cd3fea8e07dbff3736cbd180eb1c0edcc1cbebdf62686e7bd0d52.jpg)  
Fig. 19. Impact of problem reformulations on design using genetic algorithms.

Mutation was done in two different ways, the classical way, which is to make a small random perturbation in the mutated individual's parameter values, and a new way in which the direction of the small perturbation was selected to maximize the likelihood of fitness improvement, based on information obtained from the structure of all the individuals of the population. This new way of mutation proved to be very useful in improving the accuracy of the final result, making it very close to the exact global optimum.

Crossover was also done in two different ways, the classical way, which is to exchange some of the design parameters between two individuals, and a new way in which each of the two sequences of design parameters was regarded as a point in a vector space and crossover was done by selecting a random point along the line formed by joining these two points and taking it to represent the new born individual. This second way was much more appropriate than the classical way for the original search space, and was still a very powerful tool in the transformed spaces as well.

Fig. 19 shows the impact of our problem reformulations on exhaust nozzle design using genetic algorithms. The figure illustrates the takeoff mass of the best design found after a specific number of iterations, averaged over 20 runs of the GA in each space. Note that the GA search performs considerably better in the reformulated spaces than in the original search space. In particular, Fig. 19 indicates that GA performance with the Case 3 reformulation of Fig. 14 is quite impressive, and for finding the global optimum appears competitive with or perhaps superior to CFSQP, which in this multimodal space must be started from several points to ensure a high probability of finding the global optimum. Part of the reason for the improvement of the GA in the reformulated spaces over the original space is that the classical crossover operator was able to make a much larger contribution in these spaces.

## 6. Conclusion

The Search Space Toolkit (SST) is a suite of tools for investigating the properties of continuous search spaces. SST identifies properties such as number of local optima, local properties in piecewise smooth regions, topology/geometry of the evaluable regions of the objective function, ridges, valleys, and noise. These properties are key characteristics of search spaces which arise in designing complex engineering artifacts whose evaluation requires significant computation by a numerical simulator, and the properties SST investigates can have a major impact on the searchability of design spaces. The search spaces which SST explores differ significantly from the discrete search spaces that typically arise in artificial intelligence research, and properly searching such spaces is a fundamental AI research area. We have extended existing research on unified AI/optimization approaches, focusing on the combination of optimization with ideas from two subfields of AI: search and problem formation.

## Acknowledgements

This research depended critically on our collaboration with Ron Luffy and Steve Scavo of General Electric Aircraft Engines and Gene Bouchard of Lockheed. We thank Gerard Richter and our other colleagues in the AI/Design research group for valuable contributions to the work described in this paper. This research is partially supported by NASA under grant NAG2-817 and is also part of the Rutgers-based HPCD (Hypercomputing and Design) project supported by the Advanced Research Projects Agency of the Department of Defense through contract ARPA-DABT 63-93-C-0064.

## References

[1] A.M. Agogino and A.S. Almgren, Techniques for Integrating Qualitative Reasoning and Symbolic Computing, Engineering Optimization 12 (1987) 117–135.

[2] E.E. Bouchard, Concepts for a Future Aircraft Design Environment, in: Proceedings, 1992 Aerospace Design Conference, Irvine, CA (February 1992) AIAA-92-1188.

[3] E.E. Bouchard, G.H. Kidwell and J.E. Rogan, The Application of Artificial Intelligence Technology to Aeronautical System Design, in: AIAA/AHS/ASEE Aircraft Design Systems and Operations Meeting, Atlanta, Georgia (September 1988) AIAA-88-4426.

[4] G. Cerbone, Machine Learning in Engineering: Techniques to Speed Up Numerical Optimization, Technical Report 92-

30-09, Ph.D. Thesis, Oregon State University Department of Computer Science (1992).

[5] Eugene Charniak and Drew McDermott, Introduction to Artificial Intelligence (Addison-Wesley, Reading, MA, 1987) (reprinted with corrections January, 1987).

[6] T. Ellman and M. Schwabacher, Abstraction and Decomposition in Hillclimbing Design Optimization, Technical Report CAP-TR-14, Department of Computer Science, Rutgers University (January 1993).

[7] Andrew Gelsey and Don Smith, A Computational Environment for Exhaust Nozzle Design, in: Proceedings, Computing in Aerospace 10, San Antonio, TX (March 1995) 531-539, AIAA-95-1016-CP.

[8] Philip E. Gill, Walter Murray and Margaret H. Wright, Practical Optimization (Academic Press, London; New York, 1981).

[9] David E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning (Addison-Wesley, Reading, MA, 1989).

[10] D. Hoeltzel and W. Chieng, Statistical Machine Learning for the Cognitive Selection of Nonlinear Programming Algorithms in Engineering Design Optimization, in: Advances in Design Automation (Boston, MA, 1987).

[11] C. Lawrence, J. Zhou and A. Tits, User's Guide For CFSQP Version 2.3: A C Code for Solving (Large Scale) Constrained Nonlinear (Minimax) Optimization Problems, Generating Iterates Satisfying All Inequality Constraints, Technical Report TR-94-16r1, Institute for Systems Research, University of Maryland (August 1995).

[12] Jae Kyu Lee and Min Yong Kim, Case-Based Learning for Knowledge-Based Optimization Modeling System: UNIK-CASE, Expert Systems with Applications 6 (1993) 87–95.

[13] Jae Kyu Lee and Min Yong Kim, Knowledge-Assisted Optimization Model Formulation: UNIK-OPT, Decision Support Systems 13 (1995) 111–132.

[14] Jae Kyu Lee and Yong Uk Song, UNIK-PMA: A Unifier of Optimization With Rule-Based Systems by the Post-Model Analysis, Annals of Operations Research (1996) (forthcoming).

[15] Jack D. Mattingly, William H. Heiser and Daniel H. Daley, Aircraft Engine Design, AIAA Education Series, American Institute of Aeronautics and Astronautics, New York, NY (1987).

[16] Jorge J. Moré and Stephen J. Wright, Optimization Software Guide (SIAM, Philadelphia, 1993).

[17] P. Papalambros and J. Wilde, Principles of Optimal Design (Cambridge University Press, New York, NY, 1988).

[18] Anthony L. Peressini, Francis E. Sullivan and J.J. Uhl, Jr., The Mathematics of Nonlinear Programming (Springer-Verlag, New York, 1988).

[19] D. Powell, Inter-GEN: A Hybrid Approach to Engineering Design Optimization, Technical Report, Ph.D. Thesis, Rensselaer Polytechnic Institute Department of Computer Science (December 1990).

[20] William H. Press, Saul A. Teukolsky, William T. Vetterling and Brian P. Flannery, Numerical Recipes in C: The Art of Scientific Computing, 2nd edition (Cambridge University Press, Cambridge, [England]; New York), 1992.

[21] M. Schwabacher, T. Ellman and H. Hirsh, Learning When Reformulation Is Appropriate for Iterative Design (to appear at IJCAI-95 Workshop of Machine Learning in Engineering, 1995).

[22] M. Schwabacher, H. Hirsh and T. Ellman, Learning Prototype-Selection Rules for Case-Based Iterative Design, in: Proceedings of the Tenth IEEE Conference on Artificial Intelligence for Applications, San Antonio, Texas (1994).

[23] J. Sobieszczanski-Sobieski, B.B. James and A.R. Dovi, Structural Optimization by Multilevel Decomposition, AIAA Journal 23, No. 11 (November 1985) 1775–1782.

[24] Siu Shing Tong, David Powell and Sanjay Goel, Integration of Artificial Intelligence and Numerical Optimization Techniques for the Design of Complex Aerospace Systems, in: Proceedings, 1992 Aerospace Design Conference, Irvine, CA (February 1992) AIAA.

[25] Garret N. Vanderplaats, Numerical Optimization Techniques for Engineering Design: With Applications (McGraw-Hill, New York, 1984).

[26] Sholom M. Weiss and Casimir A. Kulikowski, Computer Systems That Learn (Morgan Kaufmann, San Mateo, CA, 1991).

[27] Brian C. Williams and Jonathan Cagan, Activity Analysis: The Qualitative Analysis of Stationary Points for Optimal Reasoning, Proceedings, 12th National Conference on Artificial Intelligence, Seattle, Washington (August 1994) 1224–1230.

![](/api/attachments/M6CNFTWS/fulltext/images/96d9025b324af24c3a161d4d74bc5179d7225149cece83ed72b43d5557f306db.jpg)

Andrew Gelsey is an Assistant Professor in the Rutgers University Computer Science Department. He has a B.A. in Physics from Harvard University, a M.S. in Mathematics from the Courant Institute of Mathematical Sciences at New York University, and a Ph.D. in Computer Science from Yale University. Professor Gelsey's research interests include Artificial Intelligence, automated reasoning about physical systems, and the use of AI to improve engineering

design methods. Professor Gelsey is a member of the American Association for Artificial Intelligence, the Association for Computing Machinery, the Institute of Electrical and Electronic Engineers, and the American Institute of Aeronautics and Astronautics.

![](/api/attachments/M6CNFTWS/fulltext/images/acdb7f52557bc5095b28880b3f0e0f2ed162933d0228135bc81157965b184438.jpg)

Don Smith is an Assistant Research Professor in the Rutgers University Computer Science Department. He has a B.S. in Aeronautical Engineering from Brown University, a M.S. in Fluid Mechanics from Brown University, and a Ph.D. in Computer Science from Rutgers University. Professor Smith's research interests include AI-based engineering design methodologies, massively parallel architectures, and VLSI circuit design. Professor Smith is a

member of the Association for Computing Machinery and the Institute of Electrical and Electronic Engineers.

![](/api/attachments/M6CNFTWS/fulltext/images/e99669ad8d64970c6f22eb533669edf9a726974be2b9d7d7b52d1e1b7732aedf.jpg)  
Mark Schwabacher is a Ph.D. student in the Rutgers University Computer Science Department. He has a B.A. in Computer Science, Mathematical Economic Analysis, and Mathematical Sciences from Rice University, and a M.S. in Computer Science from Rutgers University. His research interests include Artificial Intelligence, machine learning, and the use of AI to improve the numerical optimization of engineering designs. He is a member of the American Asso

![](/api/attachments/M6CNFTWS/fulltext/images/283a84e6cc901c84b130da365be261a254e84a1ad5e10747ee480d68af10bf5b.jpg)  
Keith Miyake is a programmer at the Rutgers University Laboratory for Computer Science Research. He has a B.S. from the California Institute of Technology and a M.S. in Computer Science from Purdue University.

ciation for Artificial Intelligence.  
![](/api/attachments/M6CNFTWS/fulltext/images/aecfcfe909246331ae7e75a5f16becc07a4644ec5e00d2f2986c0f3dcecf552e.jpg)

Khaled Rasheed is a Ph.D. student in the Rutgers University Computer Science Department. He has a B.Sc. in Computer Science from Alexandria University (Egypt) and a M.Sc. in Computer Science from Rutgers University. Mr. Rasheed's research interests include genetic algorithms, pattern recognition and machine learning.
