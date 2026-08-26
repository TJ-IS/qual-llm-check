---
otero_id: 16562
otero_key: "FAQRWEXZ"
title: "Filaments of crime: Informing policing via thresholded ridge estimation"
authors: "Ben Moews; Jaime R. Argueta; Antonia Gieschen"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113518"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Filaments of Crime: Informing Policing via Thresholded Ridge Estimation

Ben Moews <sup>·</sup> Jaime R. Argueta, Jr. <sup>·</sup> Antonia Gieschen

## Abstract

In this study, we investigate the potential for optimizing hot spot patrol routes through density ridge estimation. We explore the application of an extended version of the subspace-constrained mean shift algorithm by using 2018 and 2019 Part I crime data from Chicago. Ultimately, the goal of mapping hot spots is to show concentrations of crime, thus targeting the epicenters only focuses on one problem area. For this reason, we refine patrol optimization to focus on the critical ridges in hot spots. In doing so, we extract density ridges of 2018 to early 2019 Part I crime incidents from Chicago to demonstrate that nonlinear mode-following ridges agree with broader kernel density estimations. We create multi-run confidence intervals and show that our patrol templates cover around 94% o incidents for 0.1-mile envelopes around ridges, and deliver evidence that ridges following crime densities enhances the eficiency of patrols. Our post-hoc tests show the stability of ridges, thus ofering an alternative patrol route option that is efective and eficient.

Keywords Density Ridge Estimation, Patrol Routes, Optimized Patrols, Hot Spots

Mathematics Subject Classification (2010) 62G07 62H11 62P25

## 1 Introduction

Investigations of hot spot policing tactics find that focused eforts on problem areas, such as staying at a block, efectively reduce crime Braga et al (2014); Corsaro et al (2019). Related research finds that 15 minutes of police presence in a given hot spot significantly decrease both calls for service and Part I crimes Koper (1995); Telep et al (2014). These practices suggest that the stability of crime places allows for the optimization of tactics. Specifically, one way to optimize patrol routes is to a focus on the spatial aspects of hot spots, for example targeting streets and assigning prevention resources to them Camacho-Collados and Liberatore (2015).

We explore the optimization of hot spot patrols by identifying density segments as targets for crime prevention. Hot spots have high-density centers depending on the parameters defined by the analyst (pp. 356–357 f. of Eck and Guerette, 2012). Practitioners and police oficers rely on spatial analytics to identify hot spots that dictate their patrols, often over-emphasizing the epicenter’s value. This emphasis potentially over-patrols the core area and under-patrols the surrounding areas Eck et al (2005). Therefore, we propose and investigate an optimized patrol algorithm that identifies crime ridge densities in the surrounding hot spot to allow for a spread of patrol.

Previous scholars explored patrol route optimization through a variety of techniques, including multi-agentbased simulations Fukunaga and Hostetler (1975), machine learning Li et al (2011); Marchant et al (2018), and graph theory and evolutionary computing Chawathe (2007); Al Boni and Gerber (2016). These studies consistently show that route optimization is a feasible task, and account for resources and time. The primary issue among these methods is their limited application, as more complex approaches do not equate to efectiveness. Covering each street and hot spot by spending little time between places may lead to hot spots not meeting the required dosage or frequency of visits Kringen et al (2017). In turn, these patrols may have limited efectiveness or backfire Linning and Eck (2018).

Both practices, hot spot patrols and patrol optimization, tend to focus on the hot spot’s epicenter. Thus, the mismatch between the two bodies creates a gap in eficiency and efectiveness. This mismatch demonstrates three problems. First, patrol algorithms’ implementations fixate on a single spot for hot spot patrols Eck et a (2005). Secondly, common practices of identifying hot spots lack patrol direction Chainey et al (2008a); Ratclife (2010). Thirdly, patrol optimization algorithms propose a comprehensive list of all routes to be covered, thus under-patrolling areas.

In this paper, we suggest a way to bridge this gap. Recently, advances in statistics to perform density ridge estimation have enabled the construction of ridges that follow high-density areas, or modes, of a distribution and allow for higher-dimensional extensions Ozertem and Erdogmus (2011); Chen et al (2015a). In efect, this means the extraction of curvilinear structures, or ‘filaments’, that show high-density pathways reflecting an underlying distribution. As such, density ridges are diferent from mode-finding hot spot approaches, ofering the identification of a connected network while identifying finer-grained structures less prone to oversmoothing risks Genovese et al (2014).

For this reason, the present study is exploratory. We seek to address the previous shortcomings of patrol optimization by applying methods from neighboring disciplines. We focus on and extend the subspace-constrained mean shift (SCMS) algorithm Ozertem and Erdogmus (2011) in order to introduce the concept of density ridges to the field of criminology. The identification of ridges will allow law enforcement to eficiently patrol routes in hot spots and surrounding areas. Thus, we contribute to the greater literature by uniting patrol optimization work and ridge estimation in hot spots to select patrol routes. The introduction of density ridges demonstrates advantages by ofering eficiency as well as more equitable and focused patrols through the inclusion of finer-grained information on the density landscape. We show that these density ridges cover more problem segments in hot spots compared to hot spot policing or placing police personnel at single locations, and thus are an efective tool more suitable for crime prevention patrol.

We make use of Chicago Part I crime incident data from 2018 to develop and illustrate the application of ridge estimation through computational experiments. Additionally, we use data from January to May 2019 to test for predictive accuracy in coverage, as well as for convergence consistency, with multi-run confidence intervals and additional experiments for alternative method comparisons. Chicago ofers an ideal data set that allows for mapping and testing, has a typical urban street network, and provides plentiful crime data. Thus, this paper’s empirical work assesses the potential of patrol optimization in urban cities while going beyond current good policing practices.

## 2 Literature review

## 2.1 Hot spots

Over the past two decades, scholars have confirmed that large numbers of calls for service concentrate within 3–5% of a given city Sherman et al (1989); Sherman and Weisburd (1995); Braga et al (2014). Related research finds that hot spots chronically persist for longer than a decade in 5% of block-long street segments Weisburd et a (2004). Since then, the ‘Law of Crime Concentration’ was coined Weisburd (2015), which refers to the concept where crime concentrates in specific small areas of any city or year. Later works find that hot spots vary in size for diferent types of crimes, for example gun-related crime Braga et al (2010), robberies Braga et al (2012), and other major crimes Haberman (2017).

Findings from these studies enable researchers and practitioners in two ways. The first is testing techniques on stable hot spots and investigating which policing strategies can be the most efective. Patrolling hot spots is reported to not disperse crime to neighboring geographic locations Braga (2007). Instead, deterrent efects are difused to nearby streets, making eforts in patrolling hot spots a successful endeavor Braga et al (2014). Recently, research raises issues with the amount of patrolling in hot spots, pointing out a possible hermetic efect Linning and Eck (2018). The latter work suggests that if a hot spot does not meet a specific dosage of patro presence, there may be an increase in crime. Thus, under-policing or even over-policing areas can backfire and result in increases of criminal activity. Similarly, scholars argue that patrols should focus on fewer visits of longer duration at hot spots rather than hitting them randomly and often Williams and Coupe (2017).

The research mentioned above developed in parallel to methods for estimating hot spots. With about 75% of agencies using the hot spots policing approach, most use kernel density estimations to identify intervention areas Weisburd and Majmundar (2018); Mastrofski and Fridell (2015). While kernel methods show great success, they only focus on singular cells and spaces instead of the surrounding problem areas or opportunities. This lead to the suggestion that there should perhaps be more to just plotting densities of crime areas Eck (1997). To address this, a risk terrain model has been presented Caplan et al (2011), applying forecasting of opportunity structures throughout a geographic space and building on prior kernel density work. This does, however, still include possible pitfalls of an over-reliance on the epicenter of cells to suggest patrol work. Hence, the risk terrain model and kerne density models still apply a static approach for placing police on dots, or epicenters, with little consideration for the full spatial range identified.

In summary, hot spot policing provides a way for police departments to reduce crimes by patrolling problem areas efectively, but there are limitations to the use of kernel methods. Hot spots illustrate varying levels of crime concentration over a geographic landscape. The empirical work described in this paper suggests that the decision of where the line is drawn by analysts to define a hot spot may vary the amount of attention. Thus, hot spot patrols may benefit from a defined route that exhibits optimal routes to target crime prevention resources so they do not focus on just one area.

## 2.2 Patrol optimization

For strategic planning, law enforcement makes use of hot spots to identify problem areas to patrol.The visible presence of patrols in a community is one of the key components in reducing crime, especially in hot spots. For this reason, the identification of routes in hot spots is relevant due to patrols being constrained by street networks Menton (2008). Furthermore, given the scarcity of police resources, the eficient allocation of proactive patrols is crucial, and an optimal dosage of police presence at these hot spots needs to be applied. Police agencies identify hot spots with spatial ellipses, grid mapping, thematic mapping, kernel density methods, Getis-Ord Gi\*, and point processes for spatial analytics Chainey et al (2008a); Ratclife (2010); Xue and Brown (2006). That being said, advanced route planning based on proper hot spot estimations still lags behind most current research.

Scholars have recently turn to algorithms. Patrol optimization deals with identifying optimal routes so that oficers target hot spots eficiently. While these methods are complex, they ofer the potential to dynamically shape patrol routes to service each call, problem area, or assignment. For example, recent work using the ant colony optimization algorithm and Bayesian methods Chen et al (2015); Furtado et al (2009) shows the practica utility of eficiently hitting each hot spot in an optimal manner. In another approach, dynamic modeling is used by assuming that ofenders will predict patrol routes Paruchuri et al (2008), demonstrating the model’s ability to determine optimal paths that balance predictable and unpredictable street network paths. Related research suggests the potential to decrease criminal activity and the public’s fear of crime by modeling patrol routes illustrating the shortest Hamiltonian cycle for visiting each location in a city Chevaleyre (2004).

Additional facets of patrol optimization consider limited patrol resources and take on a variety of approaches. These include the application of patrol optimization using a cost-benefit analysis, maximizing the coverage of hot spots and accounting for the paths between streets and places Chawathe (2007), as well as a multi-agent-based algorithm to design eficient patrol strategies Reis et al (2006). The latter simulation models a city’s road network to find optimal routes to minimize crime in a city. Further work studies changing ofenders’ opportunity structure Furtado et al (2006), while related eforts simulate changing problem places that adapt to patrol routes Melo et al (2005). Finally, similar applications look at how district models can be optimized to adequately distribute calls for service or incidents in a given jurisdictions Liberatore et al (2020); Mitchell (1972); Bodily (1978); Piyadasun et a (2017). The shortcoming of each of these works is that they focus on cost eficiency and formulation of routes. Only few works include the importance of hitting potential problem places, although these studies do not account for the quality of patrols Reis et al (2006); Melo et al (2005).

Table I. Part I crime incident numbers for Chicago during the year 2018. Diferent primary crime types are listed separately, with entries descending by the number of reported incidents.

<table><tr><td>Primary crime type</td><td>Number of data points</td></tr><tr><td>Larceny-theft</td><td>42,423</td></tr><tr><td>Aggravated assault</td><td>13,843</td></tr><tr><td>Burglary</td><td>7,821</td></tr><tr><td>Motor vehicle theft</td><td>6,641</td></tr><tr><td>Robbery</td><td>6,525</td></tr><tr><td>Forcible rape</td><td>1,013</td></tr><tr><td>Criminal homicide</td><td>386</td></tr><tr><td>Arson</td><td>242</td></tr></table>

Even with progress underway, there are still several limitations that patrol optimization studies fail to consider in their analyses. To our knowledge, none of the existing patrol optimization articles and hot spot research meet quality patrol needs while being eficient. Additionally, shortening the scope of patrol optimization to deal with one problem appears to be a feasible approach to managing proper eficiency in crime prevention at hot spots. The modeling of optimal patrol routes and simulated agents to combat problem places and limited resources is still in the early stages. While valuable for researching the impacts of policing strategies, real-world applications of optimal patrol routes are, thus, severely limited.

## 3 Data and methods

## 3.1 Crime incident data

We use the Chicago Data Portal , an open-access data service. The portal features a complete dataset of reported crime incidents from 2001 to the present day, covering over 17 years, with the exception of murders where data exist for each victim. The crime incident data are provided by the Citizen Law Enforcement Analysis and Reporting (CLEAR) system of the Chicago Police Department. CLEAR’s choice ofered an ideal data set that allowed for mapping, testing, and near-current crime events.

After obtaining the dataset, we extract all entries pertaining to 2018, and retain only three variables of interest; the primary crime type and the coordinates of the reported crime’s location. We plot the coordinates using ArcMap 10 and TIGER street centerlines projected to Geographic Coordinate System North American 1983 as spatial reference data. After this step, we omit all entries for which at least one of the retained variables is not present. This omission for missing data leads to the data for 2018 being reduced from 178,659 to 177,669 entries, resulting in a negligible loss of around 0.5% of data points.

In this work, we focus on Part I ofenses as defined by the Uniform Crime Reports<sup>b</sup> (UCR). Our choice of Part I crimes reflects both the high priority placed on this type of crime and its reliability, as well as its prior use in patrol route optimization studies Barnett-Ryan et al (2014); Chen et al (2015, 2017). In this context, aggravated assault, forcible rape, criminal homicide, and robbery are Part I violent crimes, whereas arson, burglary, larceny-theft, and motor vehicle theft are Part I property crimes. We extract these eight primary types from the preprocessed dataset, which leaves us with 78,894 incidents of Part I crimes in Chicago during the year 2018, an overview of which is provided in Tab. I. In order to keep our algorithm’s runtime low, and given that we are interested in keeping the overall density profile of crime incidents, we use uniformly-random sampling to reduce the dataset to 5,000 data points and show, in Section 4, the suficiency of the sample in a predictive case.

## 3.2 Subspace-constrained mean shift

Our approach is an extension of the subspace-constrained mean shift algorithm (SCMS), a density ridge estimation method that has been further extended in application areas described below. Following the examples of other scholars, we further adapt and extend the algorithm for a criminological context. The SCMS algorithm can be applied to crime patterns to extract route templates from high-density areas.

In order to provide readers with the background of the employed method in more depth, a short overview of the mathematical foundations is required. Given a probability density function $p : \mathbb { R } ^ { d } $ <sup>R</sup> of dimensionality d, as well as a corresponding gradient $\nabla p ( x )$ and a Hessian $H ( x )$ , let $v = \{ v _ { 1 } , v _ { 2 } , \ldots , v _ { d } \}$ be the eigenvectors of $H ( x )$ corresponding to eigenvalues $\lambda = \{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { d } \}$ sorted in descending order. Defining $\varLambda ( x )$ as the diagonal matrix with λ along the diagonal, and with the eigendecompostion $\begin{array} { r } { H ( x ) = U ( x ) A ( x ) U ( x ) ^ { \top } } \end{array}$ , we let $v ^ { \prime }$ be the columns of $U ( x )$ associated with the $d - 1$ smallest entries in λ. In addition, let $L ( x ) \propto L ( H ( x ) ) = v ^ { \prime } v ^ { \prime \top }$ be a projection on the linear space of the columns in $v ^ { \prime }$ , then the projected gradient is defined as $\nabla p ( x ) = L ( x ) g ( x )$ . For a map $\xi : \mathbb { R } \to \mathbb { R } ^ { d }$ , the ridge R can be expressed as $R = \{ x : | | G ( x ) | | = 0 , \lambda _ { d + 1 } ( x ) < 0 \}$ Ozertem and Erdogmus (2011); Genovese et al (2014). In other words, a density ridge is a local density maximization in the normal direction given by the Hessian. While the above provides a bare-bones definition, we refer the interested reader to Genovese et al (2014) for a more detailed introduction to non-parametric ridge estimation.

Kernel density estimation, which is also known as the Parzen-Rosenblatt window, is a non-parametric statistical method to estimate probability density functions Rosenblatt (1956); Parzen (1962). The most common choice, and the one used in our approach, is the radial basis function (RBF) kernel, also known as the Gaussian kernel, with $\mathcal { K } ( x ) = ( 1 / \sqrt { 2 \pi } ) \exp ( - 0 . 5 x ^ { 2 } )$ . The SCMS algorithm Ozertem and Erdogmus (2011) is a KDE-based non parametric iterative approach to estimate the ridges of a probability density function in the context of self-consistent smooth curves using $\nabla p ( x )$ and $H ( x )$ . While the literature on applications since its recent introduction is sparse, the algorithm has been applied to neuroscience Bas and Erdogmus (2011) and road networks Miao et al (2014), as well as in astronomy Chen et al (2015b,c,a, 2016, 2017); He et al (2017); Hendel et al (2019); Moews et a (2020). Specifically, the method is extended with thresholding Chen et al (2015b) for the application to cosmic web reconstruction, using a KDE over the dataset to counteract the efect of areas with low probability densities.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 SCMS with thresholding
1: Input: Coordinates $\theta$, bandwidth $\beta$, threshold $\tau$, iterations $N$
2: Output: Density ridge point coordinates $\psi$
3: procedure SCMS($\theta$, $\beta$, $\tau$, $N$)
4:    $\kappa(x) \longleftarrow \text{KDE}_{\text{RBF}}(\theta, \beta)$
5:    $\psi \longleftarrow \psi \sim U((\min(\theta_{*,1}), \max(\theta_{*,1})), (\min(\theta_{*,2}), \max(\theta_{*,2})))_{|\theta|}$
6:    $\psi \longleftarrow \forall y \in \psi : \kappa(y) &gt; \tau$
7:    for $n \longleftarrow 1, 2, \ldots, N$ do
8:    for $i \longleftarrow 1, 2, \ldots, |\psi|$ do
9:    for $j \longleftarrow 1, 2, \ldots, |\theta|$ do
10:    $\mu_j = \frac{\psi_i - \theta_j}{\beta^2}$
11:    $\sigma_j = \mathcal{K}_{\text{RBF}}\left(\frac{\psi_i - \theta_j}{\beta}\right)$
12:    end for
13:    $H(x) = \frac{1}{|\theta|} \sum_{j=1}^{|\theta|} \sigma_j\left(\mu_j \mu_j^\top - \frac{1}{\beta^2} \mathbb{I}\right)$
14:    $v, \lambda \longleftarrow v, \lambda$ from eigendecomposition eig($H(x)$)
15:    $v' \longleftarrow$ entries in $v$ corresponding to $\text{sort}_{\text{asc}}(\lambda)_{1,2,\ldots,d-1}$
16:    $\psi_i \longleftarrow v' v'^{\top} \frac{\sum_{j=1}^{|\psi|} \sigma_j \theta_j}{\sum_{j=1}^{|\psi|} \sigma_j}$
17:    end for
18:    end for
19:    return $\psi$
20: end procedure
</div>

The convergence properties of the SCMS algorithm have been analyzed Ghassabeh et al (2013), showing that the method inherits some properties of the previous mean shift algorithm Fukunaga and Hostetler (1975), most importantly its monotonicity and the convergence of density estimates along the output sequence, together with other properties that ofer theoretical guarantees for stopping criteria. For an up-to-date contextualization of the approach in the broader field of topological data analysis, we refer the reader to suitable overview Wasserman (2018), as well as to a more general analysis of non-parametric density ridge estimation Qiao and Polonik (2016). In addition, a study of, as well as extensive proofs for, ridge estimation from a geometrical perspective have been conducted Genovese et al (2012).

## 3.3 Modifications and extensions

In addition to providing a fast pure-Python implementation of the SCMS algorithm, with thresholding implemented in line 6 of Alg. 1, we introduce multiple modifications of the methodology tailored to geospatial data and applications in criminology.

An optimal bandwidth calculation for crime incident data has been introduced earlier Williamson et al (1999), based on the average distance of each coordinate to its nearest k neighbors, averaged over all coordinates in the dataset Eck et al (2005). For the distance $\mathsf { M } ( \theta _ { i } , \theta _ { j } )$ between two coordinates of a dataset θ, and with the number of nearest neighbors k, the calculation of the optimal bandwidth $\hat { \beta }$ takes the form of the following equation:

$$
\hat {\beta} = \frac {1}{k | \theta |} \sum_ {i = 1} ^ {| \theta |} \sum_ {j = 1} ^ {k} \mathbb {M} (\theta_ {i}, \theta_ {j})\tag{1}
$$

This approach is related to the k-nearest neighbors (k-NN) algorithm, a non-parametric statistical method commonly applied to regression and classification problems Cover and Hart (1967). We make use of this calculation to provide an optimized default bandwidth for our method. Without a bandwidth optimization, the bandwidth would need to be set manually by the user, which would lead to problems in both directions. Either the coverage would be diminished due to a too large bandwidth, resulting in ridges that follow an overly broad density profile, or the ridges would present a too fine-grained net of substructures that would mathematically provide good coverage, but not be practical for patrolling.

While the Euclidean distance is a staple in geometric calculations, its use can lead to distorted measures when applied to geospatial coordinates over suficiently large distances. In this context, the orthodromic distance is the shortest path between two coordinates on a sphere, measured along the sphere’s surface. As such, it provides a suficiently realistic way to calculate distances as geodesics on an approximated shape of the Earth. While police patrolling is, in practice, a regional problem and local topology outweighs the curvature of our planet, a negligible diference in computational costs allows the resulting software to be applicable to other, more large-scale challenges in other fields.

The haversine function of an angle α is a numerically better-conditioned for small geodesic distances than using the spherical law of cosines. The haversine formula Inman (1835) makes use of that function and provides a way to calculate the orthodromic distance suitable for our purposes in that it remains accurate on small-scale local distances and stays applicable on larger scales. Denoting the latitudes and longitudes separately, the haversine distance between points $\theta _ { 1 }$ and $\theta _ { 2 }$ is then:

$$
\mathbb {M} _ {\mathrm{hav}} (\theta_ {1}, \theta_ {2}) = \mathrm{hav} (\theta_ {2, 1} - \theta_ {1, 1} + \cos \theta_ {1, 1} \cos \theta_ {2, 1} \mathrm{hav} (\theta_ {2, 2} - \theta_ {1, 2}))\tag{2}
$$

One interesting point to note is that the applicability of the haversine distance directly translates to projected astronomical observations, although with flipped horizontal axes, as the sky in the latter is viewed as a sphere with the Earth at its center. This is done in an application of our implementation Moews et al (2020), making direct use of our work across fields as a result, and showing the interdisciplinary applicability of methodologica and software developments between fields. In addition to its use for the SCMS algorithm’s iterative updates, we also use this distance for the k-NN approach of calculating an optimal bandwidth, replacing $\mathsf { M } ( \theta _ { i } , \theta _ { j } )$ in Eq. 1 with $\boxtimes _ { \mathrm { h a v } } ( \theta _ { i } , \theta _ { j } )$ from Eq. 2.

Well-approximated density ridges require the SCMS algorithm to run over a suficient number of iterations. Since a trial-and-error approach is not the most time-eficient way of using the algorithm, we implement a convergence check that uses the mean shift update in Alg. 1. Let the update be denoted as $\phi _ { n , i }$ , for iteration n and $j \in \{ 1 , 2 , \dots , | \psi | \}$ for ridge candidate points $\psi ,$ then the calculation takes the following form:

$$
\phi_ {n, i} = v ^ {\prime} v ^ {\prime \top} \frac {\sum_ {j = 1} ^ {| \psi |} \sigma_ {j} \theta_ {j}}{\sum_ {j = 1} ^ {| \psi |} \sigma_ {j}} - \psi_ {i}\tag{3}
$$

We then introduce the convergence criterion, for a convergence threshold $c ,$ as the absolute diference between an iteration’s current update and the last iteration’s update not exceeding the convergence threshold, meaning that $| | \phi _ { n - 1 , i } - \phi _ { n , i } | | \leq c .$ Without this introduced convergence criterion, the number of iterations would, as in the original SCMS algorithm, need to be set manually by the user. This poses the challenge of correctly guessing the number of required iterations to create well-defined ridges, as too small a value would result in fuzzy ‘clouds’ along the ridges, as opposed to ridge lines. The value would thus need to be set rather large in order to avoid this issue, hoping to overshoot the necessary but unknown value, which would, even if successful, increase the computational costs and thus the runtime of the algorithm.

Lastly, practitioners in criminology are often primarily interested in hot spots, focusing their eforts on regions with high probability densities. In order to enable this use of our method, we propose a cut-of functionality to return only ridge estimates in regions with a high number of data points in comparison to the dataset. For a given percentage value $p ,$ the KDE in the SCMS algorithm is used to only retain ridge estimate points above the $( 1 0 0 - p ) ^ { \mathrm { t h } }$ percentile of the dataset’s estimated probability density function. This means that the ridge estimate points ψ are, for a bandwidth $\beta$ and a Gaussian-kernel KDE, reduced to a subset $\psi ^ { \prime } { : }$

$$
\begin{array}{r l} & {\psi^ {\prime} = \hat {\psi} \in \psi : \mathrm{KDE} _ {\mathrm{RBF}} (\hat {\psi}, \beta) \geq \gamma ,} \\ & {\quad \mathrm{with} \gamma = \min \left(\mathrm{sort} _ {\mathrm{desc}} \left(\mathrm{KDE} _ {\mathrm{RBF}} (\psi , \beta)\right) _ {1, 2, \ldots , \lfloor \frac {p}{1 0 0} | \psi | \rfloor}\right)} \end{array}\tag{4}
$$

This approach allows for the exclusive retention of ridge estimates that fall within regions of high probability densities, efectively slicing the density landscape horizontally at the required percentage level and extracting the ridge estimate points that can be found on the remaining landscape. The advantage of this extension is that a top percentage level of crime density can be freely chosen to concentrate hot spot policing eforts on a highest-density subset of areas in line with additional considerations by the respective practitioners.

We introduce a pure-Python software tool for density ridge estimation describing geospatial evidence (DREDGE), written for Python 3. The tool itself is available on, and can be installed via, the $\mathrm { P y }$ thon Package Index $( \mathrm { P y } \mathrm { P I } ) . ^ { \mathrm { c } }$ We also provide the complete code for DREDGE in a public repository<sup>d</sup>, accompanied by documentation, a quickstart tutorial, and a use case featuring example code.

## 4 Results

## 4.1 Primary experiment and visualization

The theoretical work on hot spots and direct patrols has been widely applied and studied within the field of criminology Braga et al (2014). Current applications of patrol routes include patrols that are mainly planned using street network models and KDE Mamalian et al (1999); Ratclife (2004a). Our work seeks to capitalize on that aspect through density ridge estimation. The density ridges obtained through this experiment with Chicago’s 2018 Part I crime incidents are shown in both panels of Fig. 1. In the left panel, we additionally show a sample of 5,000 coordinates of reported crime incidents, the same size as used by the DREDGE run. In the right panel, we overlay the density ridges with a KDE based on the same optimal bandwidth used by our method, demonstrating the center-line compliance of ridges with hot spots identified by traditional approaches. We show how DREDGE results line up with the underlying data as well as KDE outputs to demonstrate how our results follow high-density areas identified with this alternative approach, using the latter as a comparison baseline.

The implementation of our method described in this paper is run with default values, allowing the software to make use of its adaptive behavior. We run this experiment on an Intel Core i7-5600U CPU with 2.60 Ghz, two cores, and four threads, on a machine featuring a suficient 8 GB of RAM and resulting in a runtime of 6 minutes and 26 seconds. The algorithm was not parallelized, running in a single-threaded fashion to gauge the out-of-thebox performance, although low-level parallelization on a CPU can be easily implemented with the ‘multiprocess package.

![](/api/attachments/FAQRWEXZ/fulltext/images/311e11c9dfed1c1926198e522fd57375a0b65b3409170216593df93a765af226.jpg)

![](/api/attachments/FAQRWEXZ/fulltext/images/b0b586018de471a430d2e2adb807e40a4e3cffa3ad268c90ff94f1df07697e80.jpg)  
Figure 1. Full density ridges extracted from reported Part I crime incidents for the City of Chicago during 2018. The left panel adds a sample of underlying coordinates, whereas the right panel adds a kernel density estimation (KDE) for the samples in the left panel.

![](/api/attachments/FAQRWEXZ/fulltext/images/69b68177cd1c91962793bfe2c014a060ebbf11b707d94dd73fba92361556f645.jpg)

![](/api/attachments/FAQRWEXZ/fulltext/images/724f1896a9377370b999db9d7e50db374e901bd4610ce830ff0aefc00bc609c9.jpg)  
Figure 2. Partial density ridges extracted from reported Part I crime incidents for the City of Chicago during 2018. The left panel adds a sample of underlying coordinates, whereas the right panel adds a kernel density estimation (KDE) for the ridge-related hot spots.

The practical application and ease of policing hot spots has allowed police departments to patrol specific areas more readily Weisburd and Lum (2005). Capitalizing on hot spots, we make use of DREDGE’s ability to retrieve density ridges from a specified level of high-density areas, as discussed in Section 3.3. Fig. 2 shows the respective top-percentage ridges retrieved through this experiment. Both panels show partial density ridges, making use of the built-in threshold functionality set to 5% for density ridges covering the region above the $9 5 ^ { \mathrm { t h } }$ percentile of the incident density distribution. As in Fig. 1, the left panel additionally shows a sample of 5,000 coordinates of reported crime incidents, the same size as used by the DREDGE run, to show the relation of ridges to the underlying dataset, whereas the right panel overlays the density ridges with a KDE estimate for the data points relevant to the top 5% ridges as a comparison baseline.

Due to the same underlying analysis, the high-density area highlighted through the KDE visualization in Fig. 1 corresponds to the hot spot singled out in Fig. 2. This location falls within the Near North Side and Loop areas of downtown Chicago, known as tourist and shopping destinations. An obvious interpretation of this high-density accumulation of data points relies on the considerable overrepresentation of larceny-theft in our dataset, as these areas provide ample opportunity for such crimes, combined with scaling efects due to the number of people frequenting them, which we confirmed for over a fifth of the larceny-theft reports occurring in these areas.

## 4.2 Post-hoc analyses and comparisons

To test the predictive accuracy and stability of density ridges over time, we extract another dataset from the Chicago Data Portal. The procedure remains the same as in Section 3.1, but with data for the year 2019 until the end of May. This amounts to 38,205 preprocessed Part I crimes. For this experiment, we use the complete dataset without subsampling, in addition to confidence intervals for multiple runs, to assess the stability of the algorithm’s performance. We employ the ridges extracted from the previous 2018 data to simulate route optimization. We measure the distance to the nearest density ridge and calculate the percentage of incidents falling into this envelope around ridges. In doing so, we quantify the amount of incidents in 2019 that happen near a route template based on 2018 data.

This approach is related to a hit rate, or the percentage of crime incidents occurring within an area of a certain size Chainey et al (2008b). Related work Bowers et al (2004) proposes a search eficiency rate that counts the number of events per square kilometres, although this approach lacks comparability between diferent study areas. Our choice to measure the percentage of overall crime incidents within envelopes around ridges bears the closest resemblance to the prediction accuracy index (PAI) Bowers et al (2004). The PAI computes the percentage of crime incidents within a predicted area, divided by the percentual size of the predicted areas in relation to the respective study area. Notably, accounting for the predicted area size is not a concern in our ridge-specific approach, which predicts curvilinear filaments instead of areas. Instead, our measurement’s equivalent is the envelope width around ridges, which requires the calculation of the crime incident coverage for varying widths in order to accurately represent the ridges’ success.

We compute this experiment for distances in the interval [0.1, 1] in miles, in steps of 0.01 miles, and repeat each experiment for each distance for a total of 10 times to recover confidence intervals. Each of these 10 runs per distance step is based on a random subsample of reports from the year 2018, with a diferent random seed each time, to validate the eficacy of a comparatively small subsample of 5,000 data points. In addition, we measure the number of iterations required each time to test the suitability of the convergence criterion introduced in Section 3.3. We also measure the same distance envelope coverage for the top 5% of crime report densities as shown in Fig. 2, and with the same ridges as depicted there, for which we identify five clusters via the mean shift algorithm and use 5%-thresholded crime report coordinates. Using random within-cluster connections with interpolation, we create random routes per identified hot spot to compare the predictive coverage of our approach to random patrols within hot spots, as well as with the use of solely the hot spot center as a point of reference.

Fig. 3 shows the results of these experiments. The black line in the left-hand plot depicts the share of Part I crime reports in the City of Chicago from 2019 data on the vertical axis, depending on the size of the distance envelope around ridges on the horizontal axis. The shaded area around the curve indicates 95% confidence intervals for 10 runs per distance, demonstrating the low variation in coverage for comparatively small subsamples that enable fast runtimes. We expect a highly concave curve path to reflect a diminished increase in coverage with higher distances, as ridges should closely follow higher-density areas due to the way they are computed. The curve path in the figure clearly shows this behavior, with ridge envelopes covering 94% of incidents at 0.1 miles for the whole city, quickly rising to 97.5% and 98.5% at 0.2 and 0.3 miles, respectively, and reaching 99% coverage at about 0.6 miles.

In the lower right corner of the left-hand plot, we show a box-and-whiskers plot, with the upper and lower boundaries of the boxing indicating values within 1.5 times the interquartile range, the horizontal line intersecting the box denoting the median,and the of-standing ‘whiskers’ indicating the minimum and maximum values McGill et al (1978). The number of iterations remains stable for diferent subsamples, demonstrating consistent convergence for subsampled sets in line with the narrow confidence shown in the primary plot. The right-hand plot of Fig. 3 confirms the viability of density ridges as route templates, outperforming random routing within identified hot spot areas. As routes through a hot spot should ofer more distance-based coverage by virtue of covering a larger area, one can reasonably expect center-only measurements to underperform both approaches as a sanity check, which the right-hand plot demonstrates.

![](/api/attachments/FAQRWEXZ/fulltext/images/fde42fbbb9b18fa33688d652125f56b42a6d7fe315ead0fcf257c6e05cba4d72.jpg)

![](/api/attachments/FAQRWEXZ/fulltext/images/b86768f6e8365943b02029cdfac66a647956edfdcb71e379a889ec002aec5506.jpg)  
Figure 3. Left: Distance-based coverage for Part I crimes in January to May 2019 in the City of Chicago, for ridges calculated with data from 2018 and 95% confidence intervals in lighter shades. The subplot in the lower right corner shows a box-and-whiskers plot for the number of iterations to convergence. Right: The same data as on the left, but results are shown for clustered hot spots in top-5% areas, with ridges placed within them in black, random patrols within the hot spots and including the hot spot center in blue, and hot spot centers exclusively in purple.

## 4.3 Mappability and route waypoints

In order to allow for a translation of ridges to route guidelines, we make use of the R package ‘osmar’ Eugster and Schlesinger (2013), which enables access to OpenStreetMap data. For each ridge point, we calculate the closest registered node on OpenStreetMap to allow us to make use of the underlying maps. From each of these neighbouring nodes, we then identify the nearest node which is located on a highway. These highway nodes can be seen in Fig. 4 for the ridges in the top-5% areas, as well as for a zoom-in of a single ridge segment. Due to OpenStreetMap being compatible with commonly used navigation systems, adding these maps into such systems is a straightforward approach. Patrols can then use these points to guide their routes while remaining flexible regarding their order or share of responsibility of area between the individual police oficers.

## 5 Discussion and limitations

In this exploratory study, we present DREDGE as a way to increase hot spot patrol eficiency and quality. Based on extensions from the field of cosmology, we make use of the SCMS algorithm for hot spot patrol routes. Our experiments show that optimized patrol templates cover about 94% of incidents within 0.1 miles of ridges, reaching to about 99% coverage at 0.6 miles. We implement multiple realizations of our experiments to investigate the stability of crime coverage with ridges based on past data. The corresponding results demonstrate relative stability within narrow confidence intervals across difering subsamples, validating the applicability of our approach for large-scale data.

![](/api/attachments/FAQRWEXZ/fulltext/images/cbcaf9350f8e87cb246707027e17fc5456b5e7cd2a54beeb727ad93363ca3234.jpg)

![](/api/attachments/FAQRWEXZ/fulltext/images/fec79d0d7335bbf8a0b716a4b114b249a3073966c42a959e324e5d970acc8c28.jpg)  
Figure 4. Route points plotted for parts of the top-5% areas. Each green node is one highway location point registered on OpenStreetMap which is identified as being the closest to a ridge point. Left: Large-scale view of the identified route points. Right: Zoomed-in depiction of the left-most route shown in the left plot.

Research on hot spots maintains that crime concentrates within a small geographic area Weisburd (2015). The widespread assumption when modeling hot spots is that the epicenter of the hot spots is where police attention should be focused. For example, the Pittsburgh Police Bureau used ‘putting cops on dots’ for about 15 years Gorr and Lee (2015). Commonly employed density estimation methods can, however, obscure underlying features Eck et al (2005). The epicenter may be interpreted as a place to heavily patrol in lieu of surrounding areas that may deserve equal or more attention. Thus, this study’s objective is to provide an efective alternative, and implies a refutation of previous assumptions about optimal patrol routes within hot spots to reduce crime through deterrent efects.

Empirical analyses that use KDE techniques or similar statistical modeling approaches often serve one function, namely guiding patrol routes. The issue of the epicenter misleading oficers to focus patrols on the central area of a mode is a matter of identifying which places and routes will eficiently deliver deterrence efects. Therefore, in lieu of patrolling one stopping point that is criminogenic and identifiable, these ridges use the space around the problem places that lead to the epicenter, serving a dual function of patrolling the criminogenic locations and targeting high-risk locations across normal hot spots. Prior patrol-routing algorithm and selection work hone in on selecting strict routes that ofer little route flexibility. Thus, in-between duties, this application is not meant to be the primary focus of patrols but rather an addition.

Our results show the coverage and potential eficiency of ridge patrolling. The ridges calculated with data from 2018 and 95% confidence intervals in Fig. 3 depict how ridge patrolling, hot spot patrols, and epicenter patrols work. They demonstrate the ridge patrolling method to be the most eficient, exposing nearly 95% of Chicago’s Part 1 crime incidents to directed patrols. If used solely in the epicenter of hot spots by thresholding the data to the highest 5% of crime report densities, ridges still cover the majority of the crime area while providing patrol presence in the latter. Hence, using ridges is more equitable and responsive to the surrounding crime areas than regular epicenter patrolling. The selective or all-inclusive use of this method has the advantage and potential of being a high-eficiency crime prevention program. Furthermore, we argue that it can be a dynamic and widespread crime prevention measure across a city.

Our study is not without limitations. The methodology applied in this paper does not apply weights to problem places. Therefore, future work could focus on the application of spatial weights. In addition, this work assumes that the organization of patrol routes is implementable solely based on filament optimization, not considering community residents who may want to stop oficers or demand more presence Leigh et al (2017). Given the fixed location of hot spots, the desires of residents, and the possible need to redraw routes due to calls for service or complex routes, such alterations should follow an as-close-as-possible alignment with ridges.

In addition, the program solely makes use of the geographic locations of prior incidents within a year frame. Thus, we do not account for the temporal dimension of the hot spots or incidents. However, an adaptation of this program by filtering and grouping incidents into time windows prior to running the program is feasible, which allows for more in-depth investigations. For follow-up research, we propose to combine such investigations with the separation of crime types to explore temporal changes in overall distributions, and weight shifts in types of incidents. Future work should, therefore, investigate such ‘hot times’ and DREDGE for police work, ofering yet another perspective to research on spatio-temporal crime patterns (see, for example, Ratclife, 2004b; Newton and Felson, 1978; Malleson and Andresen, 1978).

Another limitation of this program is the lack of routing times for when oficers should patrol each ridge, providing both spatial and temporal guidance. Building on the mention of weight shifts above, ridge segments for percentage-cut areas for diferent time windows could be weighted for their interest, allowing for time-dependent changes in route templates as well as a duration relying on expected crime density and types. On a more practical note, minimum durations for ridge segment traversal could be calculated through building a graph from points such as the ones covered in Section 4.3. By using either time estimates for average speed or, more advanced, linking the program into the route time prediction that navigation programs ofer, traversal durations could be estimated for given segments.

While our implementation performs successful density ridge estimation in a matter of minutes, this requires subsampling from larger datasets of coordinates. As a rule of thumb, we recommend to use a minimum of 1,000 and a maximum of 10,000 data points to ensure representativeness and suficiently fast runtimes. This is due to the algorithm’s complexity being $\mathcal { O } ( d \cdot | \theta | ^ { 2 } )$ , meaning that it scales linearly with the number of dimensions, which is fixed to $| \theta | = 2$ in our case of latitude-longitude coordinates, but features a polynomial runtime due to the number of data points fed into the algorithm Ozertem and Erdogmus (2011). While sample sizes are, in practice, influenced by both time constraints and the size of available datasets, details on efective sample sizes in geospatial dataset resampling can be found in the literature Grifith (2005); Li et al (2016).

Bias in data is a general problem spanning many fields, which extends to geospatial coordinates. One prominent example is the phenomenon of over-policing and under-policing based on previous records, diferent socioeconomic status, and additional factors such as personal characteristics Black (1980). Since our analysis is based on reported crime incidents, one important limitation of our work relates to previous research on disparities in crime report ing. This multi-faceted issue spans contextual factors in victim and ofender characteristics influencing reporting Xie and Lauritsen (2012), as well as localized reluctance of reporting crime incidents Slocum et al (2010). For this reason, practical implementations based on such data should always strive to take the risk of biases present in these datasets into account.

## 6 Conclusion

Optimizing police patrols, both city-wide and hot spots, remains an interest for researchers and practitioners alike. For this purpose, we show how recent advances in statistics and astronomy can be used to detect principal curves, or density ridges, in crime incident distributions to extract high-density paths. Current work focuses on the hot spot’s epicenter, which decreases equitable patrol to surrounding areas and eficient hot spot patrols to the surrounding area. Overall, we provide a way to amend these issues through a density-based patrol optimization program.

Our study uses 2018 Part I crimes from the Chicago Police Department to demonstrate the patrol templates. Comparing this output to Part I crimes from early 2019, we observe that the majority of crime reports fall into narrow envelopes around identified structures. Thus, this program allocates resources around a hot spot, covering density regions. We argue that this allocates resources equitably and optimally to prevent crimes and reduce hot spots.The combination of hot spot mapping and DREDGE has the potential of being a high-eficiency crime prevention program providing a more responsive and optimal allocation of police resources than solely targeting epicenters of hot spots. We showcase the viability of our approach with intuitive visualizations, allowing for their combination with knowledge about city-specific trafic routes to plan efective patrols while remaining not overly constrained.

## Acknowledgments

We thank the City of Chicago and the Chicago Police Department for their open access data. We wish to express our gratitude to Nicholas Corsaro, Cory Haberman, and Monsuru Adepeju for helpful suggestions and comments We also want to thank the two reviewers for their helpful comments in improving this paper.

## References

Al Boni M, Gerber MS (2016) Automatic optimization of localized kernel density estimation for hotspot policing. In: 15th IEEE International Conference on Machine Learning and Applications, pp 32–38, DOI 10.1109/ICMLA. 2016.0015

Barnett-Ryan C, Langton L, Planty M (2014) The nation’s two crime measures. Tech. rep., Bureau of Justice Statistics & Federal Bureau of Investigation, program report, U.S. Department of Justice, NCJ 246832

Bas E, Erdogmus D (2011) Principal curves as skeletons of tubular objects. Neuroinformatics 9(2):181–191, DOI 10.1007/s12021-011-9105-2

Black D (1980) The manners and customs of the police. New York: Academic Press

Bodily SE (1978) Police sector design incorporating preferences of interest groups for equality and eficiency. J Manag Sci 24(12):1301–1313, DOI 10.1287/mnsc.24.12.1301

Bowers KJ, Johnson SD, Pease K (2004) Prospective hot-spotting: The future of crime mapping? Br J Criminol 44(5):641–658, DOI 10.1093/bjc/azh036

Braga A, Papachristos A, Hureau D (2012) Hot spots policing efects on crime. Campbell Syst Rev 8(8):1–96, DOI 10.4073/csr.2012.8

Braga AA (2007) Policing crime hot spots. In: Preventing Crime, New York: Springer Publishing, pp 179–192, DOI 10.1007/1-4020-4244-2 12

Braga AA, Papachristos AV, Hureau DM (2010) The concentration and stability of gun violence at micro places in Boston, 1980-2008. J Quant Criminol 26(1):33–53, DOI 10.1007/s10940-009-9082-x

Braga AA, Papachristos AV, Hureau DM (2014) The efects of hot spots policing on crime: An updated systematic review and meta-analysis. Justice Q 31(4):633–663, DOI 10.1080/07418825.2012.673632

Camacho-Collados M, Liberatore F (2015) A decision support system for predictive police patrolling. Decis Support Syst 75:25–37, DOI 10.1016/j.dss.2015.04.012

Caplan JM, Kennedy LW, Miller J (2011) Risk terrain modeling: Brokering criminological theory and GIS methods for crime forecasting. Justice Q 28(2):360–381, DOI 10.1080/07418825.2010.486037

Chainey S, Tompson L, Uhlig S (2008a) The utility of hotspot mapping for predicting spatial patterns of crime. Secur J 21(1-2):4–28, DOI 10.1057/palgrave.sj.8350066

Chainey S, Tompson L, Uhlig S (2008b) The utility of hotspot mapping for predicting spatial patterns of crime. Secur J 21(1):4–28, DOI 10.1057/palgrave.sj.8350066

Chawathe SS (2007) Organizing hot-spot police patrol routes. In: 2007 IEEE International Conference on Intelligence and Security Informatics, pp 79–86, DOI 10.1109/ISI.2007.379538

Chen H, Cheng T, Wise S (2015) Designing daily patrol routes for policing based on ANT colony algorithm. ISPRS Ann Photogrammetry, Remote Sens Spat Inf Sci 2:103–109, DOI 10.5194/isprsannals-II-4-W2-103-2015

Chen H, Cheng T, Wise S (2017) Developing an online cooperative police patrol routing strategy. Comp Env Urban Sys 62:19–29, DOI 10.1016/j.compenvurbsys.2016.10.013

Chen YC, Genovese CR, Wasserman L (2015a) Asymptotic theory for density ridges. Ann Stat 43(5):1896–1928

Chen YC, Ho S, Freeman PE, Genovese CR, Wasserman L (2015b) Cosmic web reconstruction through density ridges: Method and algorithm. Mon Notices Royal Astron Soc 454:1140–1156, DOI 10.1093/mnras/stv1996

Chen YC, Ho S, Tenneti A, Mandelbaum R, Croft R, DiMatteo T, Freeman PE, Genovese CR, Wasserman L (2015c) Investigating galaxy-filament alignments in hydrodynamic simulations using density ridges. Mon Notices Royal Astron Soc 454:3341–3350, DOI 10.1093/mnras/stv2260

Chen YC, Ho S, Brinkmann J, Freeman PEP, Wasserman L (2016) Cosmic web reconstruction through density ridges: Catalogue. Mon Notices Royal Astron Soc 461:3896–3909, DOI 10.1093/mnras/stw1554

Chen YC, Ho S, Mandelbaum R, Bahcall NA, Brownstein JR, Freeman PE, Genovese CR, Schneider DP, Wasserman L (2017) Detecting efects of filaments on galaxy properties in the Sloan Digital Sky Survey III. Mon Notices Royal Astron Soc 466:1880–1893, DOI 10.1093/mnras/stw3127

Chevaleyre Y (2004) Theoretical analysis of the multi-agent patrolling problem. In: 2004 IEEE/WIC/ACM Inter national Conference on Intelligent Agent Technology, pp 302–308, DOI 10.1109/IAT.2004.1342959

Corsaro N, Engel RS, Herold TD, Yildirim M (2019) Implementing gang & gun violence reduction strategies in las vegas, nevada: Hot spots evaluation results

Cover TM, Hart PE (1967) Nearest neighbor pattern classification. IEEE Trans Inf Theory 13(1):21–27, DOI 10.1109/TIT.1967.1053964

Eck JE (1997) What do those dots mean? mapping theories with data. In: Crime mapping and crime prevention, New York: Criminal Justice Press, pp 379–406

Eck JE, Guerette RT (2012) Place-based crime prevention: Theory, evidence, and policy. The Oxford handbook of crime prevention pp 354–383, DOI 10.1093/oxfordhb/9780195398823.013.0018

Eck JE, Chainey S, Cameron JG, Leitner M, Wilson RE (2005) Mapping crime: Understanding hot spots, 1st edn. Washington, D.C.: Ofice of Justice Programs, National Institute of Justice

Eugster MJA, Schlesinger T (2013) osmar: OpenStreetMap and R. The R Journal 5(1):53–63, DOI 10.32614/ RJ-2013-005

Fukunaga K, Hostetler LD (1975) The estimation of the gradient of a density function, with applications in pattern recognition. IEEE Trans Inf Theory 21(1):32–40, DOI 10.1109/TIT.1975.1055330

Furtado V, Melo A, Menezes R, Belchior M (2006) Using self-organization in an agent framework to model criminal activity in response to police patrol routes. In: 2006 Florida Artificial Intelligence Research Society Conference, pp 68–73

Furtado V, Melo A, Coelho ALV, Menezes R, Perrone R (2009) A bio-inspired crime simulation model. Decis Support Syst 48(1):282–292, DOI 10.1016/j.dss.2009.08.008

Genovese CR, Perone-Pacifico M, Verdinelli I, Wasserman L (2012) The geometry of nonparametric filament estimation. J Am Stat Assoc 107(498):788–799, DOI 10.1080/01621459.2012.682527

Genovese CR, Perone-Pacifico M, Verdinelli I, Wasserman L (2014) Nonparametric ridge estimation. Ann Statist 42(4):1511–1545, DOI 10.1214/14-AOS1218

Ghassabeh YA, Linder T, Takahara G (2013) On some convergence properties of the subspace constrained mean shift. Pattern Recognit 46(11):3140–3147, DOI 10.1016/j.patcog.2013.04.014

Gorr WL, Lee Y (2015) Early warning system for temporary crime hot spots. Journal of Quantitative Criminology 31(1):25–47, DOI 10.1007/s10940-014-9223-8

Grifith DA (2005) Efective geographic sample size in the presence of spatial autocorrelation. Ann Am Assoc Geogr 95(4):740–760, DOI 10.1111/j.1467-8306.2005.00484.x

Haberman CP (2017) Overlapping hot spots? Examination of the spatial heterogeneity of hot spots of diferent crime types. Criminol Public Policy 16(2):633–660, DOI 10.1111/1745-9133.12303

He S, Alam S, Ferraro S, Chen YC, Ho S (2017) The detection of the imprint of filaments on cosmic microwave background lensing. Nat Astron 2(5):401–406, DOI 10.1038/s41550-018-0426-z

Hendel D, Johnston KV, Patra RK, Sen B (2019) A machine-vision method for automatic classification of stellar halo substructure. Mon Notices Royal Astron Soc 486(3):3604–3616, DOI 10.1093/mnras/stz1107

Inman JW (1835) Navigation and nautical astronomy for the use of British seamen, 3rd edn. London: W. Woodward, C. & J. Rivington

Koper CS (1995) Just enough police presence: Reducing crime and disorderly behavior by optimizing patrol time in crime hot spots. Justice Q 12(4):649–672, DOI 10.1080/07418829500096231

Kringen JA, Sedelmaier CM, Elink-Schuurman-Laura KD (2017) Assessing the relevance of statistics and crime analysis courses for working crime analysts. J Criminal Justice Education 28(2):155–173, DOI 10.1080/10511253. 2016.1192211

Leigh J, Dunnett S, Jackson L (2017) Predictive police patrolling to target hotspots and cover response demand. Ann Oper Res pp 1–16, DOI 10.1007/s10479-017-2528-x

Li B, Grifith DA, Becker B (2016) Spatially simplified scatterplots for large raster datasets. Geo Spat Inf Sci 19(2):81–93, DOI 10.1080/10095020.2016.1179441

Li L, Jiang Z, Duan N, Dong W, Hu K, Sun W (2011) Police patrol service optimization based on the spatial pattern of hotspots. In: 2011 IEEE International Conference on Service Operations, Logistics and Informatics, pp 45–50, DOI 10.1109/SOLI.2011.5986526

Liberatore F, Camacho-Collados M, Vitoriano B (2020) Police districting problem: Literature review and annotated bibliography. In: Optimal Districting and Territory Design, New York: Springer Publishing, pp 9–29

Linning SJ, Eck JE (2018) Weak intervention backfire and criminal hormesis: Why some otherwise efective crime prevention interventions can fail at low doses. The British Journal of Criminology 58(2):309–331, DOI 10.1093/ bjc/azx019

Malleson N, Andresen MA (1978) Spatio-temporal crime hotspots and the ambient population. Crime Sci 4:10, DOI 10.1186/s40163-015-0025-6

Mamalian CA, La Vigne NG, et al (1999) The use of computerized crime mapping by law enforcement: Survey results. Washington, D.C.: U.S. Dept. of Justice, Ofice of Justice Programs, National Institute of Justice

Marchant R, Lu D, Cripps S (2018) Cox Bayesian optimization for police patrolling. In: 32nd Annual Conference on Neural Information Processing Systems

Mastrofski SD, Fridell L (2015) Police departments’ adoption of innovative practices

McGill R, Tukey JW, Larsen WA (1978) Variations of box plots. Am Stat 32(1):12–16

Melo A, Belchior M, Furtado V (2005) Analyzing police patrol routes by simulating the physical reorganization of agents. In: International Workshop on Multi-Agent Systems and Agent-Based Simulation, pp 99–114, DOI 10.1007/11734680 8

Menton C (2008) Bicycle patrols: An underutilized resource. Policing 31(1):93–108, DOI 10.1108/ 13639510810852594

Miao Z, Wang B, Shi W, Wu H (2014) A method for accurate road centerline extraction from a classified image IEEE J Sel Top Appl Earth Obs Remote Sens 7(12):4762–4771, DOI 10.1109/JSTARS.2014.2309613

Mitchell PS (1972) Optimal selection of police patrol beats. J Crim L Criminology & Police Sci 63:577, DOI 10.2307/1141814

Moews B, Schmitz MA, Lawler AJ, Zuntz J, Malz AI, de Souza RS, Vilalta R, Krone-Martins A, Ishida EEO (2020) Ridges in the Dark Energy Survey for cosmic trough identification. arXiv e-prints arXiv:2005.08583

Newton A, Felson M (1978) Editorial: crime patterns in time and space: the dynamics of crime opportunities in urban areas. Crime Sci 4:11, DOI 10.1186/s40163-015-0025-6

Ozertem U, Erdogmus D (2011) Locally defined principal curves and surfaces. J Mach Learn Res 12:1249–1286

Paruchuri P, Pearce JP, Marecki J, Tambe M, Ordonez F, Kraus S (2008) Playing games for security: An eficient exact algorithm for solving Bayesian Stackelberg games. In: 7th International Joint Conference on Autonomous Agents and Multiagent Systems, Vol. 2, pp 895–902

Parzen E (1962) On estimation of a probability density function and mode. Ann Math Statist 33(3):1065–1076, DOI 10.1214/aoms/1177704472

Piyadasun T, Kalansuriya B, Gangananda M, Malshan M, Bandara HD, Marru S (2017) Rationalizing police patrol beats using heuristic-based clustering. In: 2017 Moratuwa Engineering Research Conference (MERCon), IEEE, pp 431–436, DOI MERCon.2017.7980523

Qiao W, Polonik W (2016) Theoretical analysis of nonparametric filament estimation. Ann Statist 44(3):1269–1297, DOI 10.1214/15-AOS1405

Ratclife J (2010) Crime mapping: Spatial and temporal challenges. In: Handbook of quantitative criminology, New York: Springer Publishing, pp 5–24, DOI 10.1007/978-0-387-77650-7 2

Ratclife JH (2004a) Crime mapping and the training needs of law enforcement. Eur J Crim Policy Res 10(1):65–83, DOI 10.1023/B:CRIM.0000037550.40559.1c

Ratclife JH (2004b) The hotspot matrix: A framework for the spatio-temporal targeting of crime reduction. Police Pract Res 5(1):5–23, DOI 10.1080/1561426042000191305

Reis D, Melo A, Coelho AL, Furtado V (2006) GAPatrol: An evolutionary multiagent approach for the automatic definition of hotspots and patrol routes. In: Advances in Artificial Intelligence - IBERAMIA-SBIA 2006, New York: Springer Publishing, pp 118–127, DOI 10.1007/11874850 16

Rosenblatt M (1956) Remarks on some nonparametric estimates of a density function. Ann Math Statist 27(3):832– 837, DOI 10.1214/aoms/1177728190

Sherman LW, Weisburd D (1995) General deterrent efects of police patrol in crime “hot spots”: A randomized, controlled trial. Justice Q 12(4):625–648, DOI 10.1080/07418829500096221

Sherman LW, Gartin PR, Buerger ME (1989) Hot spots of predatory crime: Routine activities and the criminology of place. Criminology 27(1):27–56, DOI 10.1111/j.1745-9125.1989.tb00862.x

Slocum LA, Taylor TJ, Brick BT, Esbensen FA (2010) Neighborhood structural characteristics, individual-level attitudes, and youths’ crime reporting intentions. Criminology 48(4):1063–1100, DOI 10.1111/j.1745-9125.2010. 00212.x

Telep CW, Mitchell RJ, Weisburd D (2014) How much time should the police spend at crime hot spots? Answers from a police agency directed randomized field trial in Sacramento, California. Justice Q 31(5):905–933, DOI 10.1080/07418825.2012.710645

Wasserman L (2018) Topological data analysis. Annu Rev Stat Appl 5(1):501–532, DOI 10.1146/ annurev-statistics-031017-100045

Weisburd D (2015) The law of crime concentration and the criminology of place. Criminology 53(2):133–157, DOI 10.1111/1745-9125.12070

Weisburd D, Lum C (2005) The difusion of computerized crime mapping in policing: Linking research and practice. Police Pract Res 6(5):419–434, DOI 10.1080/15614260500433004

Weisburd D, Majmundar MK (2018) Proactive policing: Efects on crime and communities. Committee on proactive policing: Efects on crime, communities, and civil liberties. Washington, D.C.: National Academies Press

Weisburd D, Bushway S, Lum C, Yang SM (2004) Trajectories of crime at places: A longitudinal study of street segments in the city of Seattle. Criminology 42(2):283–322, DOI 10.1111/j.1745-9125.2004.tb00521.x

Williams S, Coupe T (2017) Frequency vs. length of hot spots patrols: a randomised controlled trial. Cambridge Journal of Evidence-Based Policing 1(1):5–21, DOI 10.1007/s41887-017-0003-1

Williamson D, McLaferty S, Goldsmith V, Mallenkopf J, McGuire P (1999) A better method to smooth crime incident data. ESRI ArcUser Magazine January–March 1999:1–5

Xie M, Lauritsen JL (2012) Racial context and crime reporting: A test of Black’s stratification hypothesis. J Quant Criminol 28(2):265–293, DOI 10.1007/s10940-011-9140-z

Xue Y, Brown DE (2006) Spatial analysis with preference specification of latent decision makers for criminal event prediction. Decis Support Syst 41(3):560–573, DOI 10.1016/j.dss.2004.06.007
