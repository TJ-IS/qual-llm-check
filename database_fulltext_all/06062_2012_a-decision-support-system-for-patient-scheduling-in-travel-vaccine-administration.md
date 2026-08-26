---
otero_id: 6062
otero_key: "4F9H294R"
title: "A decision support system for patient scheduling in travel vaccine administration"
authors: "Alan S. Abrahams; Cliff T. Ragsdale"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for patient scheduling in travel vaccine administration

Alan S. Abrahams ⁎, Cliff T. Ragsdale

Department of Business Information Technology, Pamplin College of Business, Virginia Tech, Blacksburg, VA 24061, United States

## a r t i c l e i n f o

Article history: Received 12 September 2011 Received in revised form 16 February 2012 Accepted 13 May 2012 Available online 19 May 2012

Keywords: Patient scheduling Optimization Health care

## a b s t r a c t

The administration of travel vaccines presents a number of operations management challenges. The interplay between shared consumption of multi-dose vaccine packages, rapid spoilage upon opening, the high cost of wastage, and the unique vaccination needs of the patients makes for a very interesting and complex scheduling problem that could bene<sup>fi</sup>t from computerized decision support. We compare the performance of a novel binary integer programming model and a genetic algorithm solution technique with conventional scheduling approaches. Computational results show that signi<sup>fi</sup>cant cost savings can be achieved with the DSS while simultaneously considering scheduling preferences of patients and mitigating scheduling inconvenience.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Health care costs are one of the most pressing economic problems of our time. As such, computerized decision support that leverages sound operations research and management science principles has a unique opportunity to assist medical professionals in ensuring the delivery of services in the most ef<sup>fi</sup>cient means possible. This paper considers one such opportunity.

With the rising cost of prescription medicines, reducing waste in the delivery and administration of pharmaceutical products has become of increasing concern [31]. Management of pharmaceutical stock is often regarded simply as an issue of perishable inventory management, a <sup>fi</sup>eld well-studied by management scientists over many decades—for a review, see Ref. [40]. However, while conventional perishable inventory management may apply for many prescription drugs, there is a <sup>fi</sup>eld of medical practice where the inventory management problem is atypical: the <sup>fi</sup>eld of travel vaccine administration.

The United States Centers for Disease Control (CDC) recommends a variety of routine, recommended, and required vaccines for travelers to foreign destinations [7]. For example, when traveling to South Africa, the CDC recommends travelers be brought up-todate on all routine vaccinations (including measles, mumps and rubella; diphtheria, pertussis, and tetanus; polio, and others), and also receive additional immunizations for hepatitis A, hepatitis B, typhoid, and rabies.

Travel vaccine administration presents peculiar challenges to management scientists for numerous reasons. Firstly, many vaccines are packaged in multi-dose vials such that the contents are administered to several patients (shared consumption). Secondly, each patient typically requires a particular combination of vaccines, depending on their planned destination of travel and prior immunization history; therefore, consumer assortment demands are particularly stringent. Thirdly, and most critically, once opened or reconstituted, many vaccines must be used within a very short time-span, or discarded, due to rapid spoilage when exposed to air and room temperatures [2,60]. Finally, vaccines are costly to produce, making wasted doses quite expensive. For instance, YF-Vax® (yellow fever vaccine), is available in multi-dose vials with a shelf-life-onceopened of 60 min [44]. YF-Vax® wholesales for over \$340 per multidose vial [51], with each wasted dose costing the medical practice almost \$70. A single dose formulation is also available, as an alternative to the multi-dose vial, but the per-dose cost is 25% higher for the single dose formulation [51], so clinics should prefer the multidose formulation if no doses will be wasted. Simulation results from [34] indicate the severity of poor vaccine format stocking decisions: incorrect selection of single-dose vs. multi-dose format for the clinic's formulary can cost clinics between \$8000 and \$24,000 per vaccine, per year. For a clinic stocking 5 common vaccines, total costs of poor choice of single vs. multi-dose formats can exceed \$65,000 per clinic, per year.

The interplay between shared consumption of single packages, rapid spoilage once opened, stringent consumer assortment demands, and high cost of wastage creates a dif<sup>fi</sup>cult scheduling problem for the travel clinic administrator. With multiple vials of different vaccines open and deteriorating rapidly, and numerous patients each potentially requiring a different assortment of vaccines, determining the optimal scheduling of patients is non-trivial. In this paper, we show that traditional patient scheduling methods in travel vaccine clinics, such as <sup>fi</sup>rst-in, <sup>fi</sup>rst-out (FIFO), are sub-optimal and can lead to signi<sup>fi</sup>cant vaccine wastage. We propose and compare an integer programming model and a genetic algorithm solution procedure in Excel, that can signi<sup>fi</sup>cantly reduce a clinic's vaccine costs.

It is possible to develop a patient scheduling DSS using a variety of software engines instead of Excel (e.g. MATLAB, LINDO, CPLEX), and some DSS designers will prefer one engine to another. Our objective was to design a decision support tool for clerical staff in a health care clinic using a familiar, affordable, and accessible software platform.

We begin with a discussion of related work in perishable inventory management, job shop scheduling, patient scheduling, and vaccine management and describe how our approach differs from past work. We then provide descriptions and experimental evaluations for the solution procedures we tested. Finally, we conclude with a discussion of recommendations, limitations, and areas for future research.

## 2. Related work

In this section, we brie<sup>fl</sup>y review traditional perishable inventory issuance policies, common parameters to perishable inventory models, standard performance measures for perishable inventory models, and historic application areas for these perishable inventory models. We review earlier work on job shop scheduling. We also look at prior operations research work in health care delivery, particularly pertaining to patient scheduling and vaccine management. Finally, we compare and contrast our work to the past literature.

## 2.1. Perishable inventory management

A substantive body of literature discusses the management of perishable inventory—see, for example Refs. [10,13,32,37–41]. Previous authors have considered both ordering policies for replenishing perishable inventory [27,41,43,50,55,64], and issuance policies for arranging or selling perishable inventory. The most commonly recommended issuance policy for perishable inventory is the agebased FIFO issuance policy, where the oldest unexpired product is issued <sup>fi</sup>rst [48]. For inventory stockpiles with non-uniform deterioration, a quality-based issuance policy, SRSL (Shortest Remaining Shelf Life) is suggested [62]. For health-related perishables, such as blood, where patient needs vary in terms of urgency or inventory freshness, authors have recommended urgency or outsourcing classes [4] (where urgently needed stock is procured at extra expense from a 3rd party vendor, rather than stored in house) or freshness classes [21] to segregate stock and ensure availability of a compatible product for particularly ill or in<sup>fi</sup>rm patients. Inventory assortment decisions for varied perishable stock types have also been investigated [18].

Authors have considered a number of parameters that impact ordering and issuance decisions. Cost parameters include ordering cost, holding cost, outdates (e.g. disposal) cost, shortage costs, <sup>fi</sup>xed and marginal production costs, and order backlogging costs. Typical external input parameters to perishable inventory models include order lead times, replenishment rates, consumption rates (most often regarded as Poisson distributed), shelf life, and stock deterioration rate, though some authors have introduced exotic parameters such as consumer patience [47]. Other controllable parameters have been considered, such as lot size [27], product pricing [13], and production or storage capacity [19].

To evaluate the ef<sup>fi</sup>cacy of different models, authors typically measure pro<sup>fi</sup>t, de<sup>fi</sup>ned as expected sales revenues less all costs (enumerated earlier). Other performance measures include customer wait times or backlogged orders [1]; spoilage rate, lost sales rate, mean time between stock-outs, average inventory level on hand, distribution of age of items [33]; estimated effects on customer's store loyalty [25]; rate of outdatings, rate of high-cost special orders [4]; average age of inventory, probability of shortage, average number of items discarded per time period [6]; and expected quantity of any new order which will outdate [39].

Previous authors also have considered various application areas for perishable inventory management. Blood product management is a popular area of study [6,10,21,48,49], as is fresh food stock management [18,25,38,62], where authors have paid particular attention to seafood, meat, dairy, and bakery products. Some authors have even classed high-tech products with short productive or marketable life as perishables [68].

## 2.2. Job shop scheduling

The well-known job shop scheduling problem [11,61] is reminiscent of the sequencing dif<sup>fi</sup>culties encountered when scheduling patients for travel vaccination. In job shop scheduling, jobs (with machining needs) are assigned to machines. With patient scheduling, patients (with vaccination needs) are assigned to a nurse, or nurses, with limited capacity. In job shop scheduling, setup costs can be reduced and economies of scale can be achieved by grouping similar jobs by family [61]. In the vaccination problem, costs can be reduced by intelligent application of economically attractive multi-dose formulations. Notably, in the vaccination problem, a complication is added by the fact that multi-dose vials have limited shelf-life-once-opened. Further, since CDC injection safety recommendations discourage the sharing of open vials amongst multiple nurses, there is little opportunity to shift materials (drugs) amongst treatment stations (nurses). Finally, to minimize administration errors, a patient must receive all required vaccinations in a single sitting, rather than allowing a job to be split into multiple operations (individual vaccinations) spread over time. Nevertheless, techniques such as integer programming and genetic algorithms which have been shown to be effective in the job shop scheduling prob lem [11] are clearly pertinent to and useful for the travel vaccination problem.

## 2.3. Health care delivery: patient scheduling and vaccine management

Healthcare care delivery has been an important area of application for operations research techniques [5,20,57]. Important contributions have been made, in particular, for patient scheduling, such as surgical priority ranking [56], diagnostic facility scheduling [16,23,45], or inpatient bed assignment [58]. Typically, these approaches involve segmenting patients into urgency classes and giving priority to the more urgent cases. In the area of vaccine management, operations researchers have focused on a number of major issues. Formulary composition—selecting an optimal assortment of vaccines for the clinic's stockroom—has been the subject of much prior research [26,29,30,63]. The scheduling of catch up doses for patients that have missed multiple prior vaccines has also received some attention: for example, [17] implemented optimization technologies and a decision support tool to help healthcare practitioners schedule catch-up doses, taking into account minimum and maximum ages for administration, and time separation between doses. Various authors have employed operations research techniques to tackle the suppression of a single-disease pandemic, such as in<sup>fl</sup>uenza, through the optimal selection or allocation of vaccines [12,52,54,67].

Finally, with the increasing availability of multi-dose vaccine formulations, attention has recently been paid to estimating the total economic impact of multi-dose versus single-dose formulations, by conducting sensitivity analysis assuming a range of multi-dose vial sizes, costs per dose, daily clinic arrival rates, and vaccine vial utilization rates [34]. This economic model informs formulary choice (whether to stock single-dose or multi-dose vaccine formats, and which multi-dose format, for various anticipated patient arrival rates) and vaccine packaging (how many doses per multi-dose vial, for vaccine manufacturing) based on average patient arrival rates, but does not provide suggestions for optimizing patient scheduling for particular clinics, which we attend to in this paper. For example, for the Yellow Fever vaccine, it is recommended [34] that clinics stock only 5-dose vials if they have an average of less than 33 patients per day, or only 50-dose vials, if they expect more than 33 patients per day. In contrast, in this paper, we look at the optimal ordering of patients requiring multiple vaccines, in order to minimize the costly wastage of doses from available multi-dose vials.

## 2.4. Comparison to prior work

Our work differs from past research on perishable inventory management, vaccine management, and patient <sup>fl</sup>ow management in a number of respects. For the area of perishable inventory management, our work deals also with consumer scheduling, not solely producer inventory scheduling as is typical. Further, existing inventory management work typically looks at product shelf life (refrigerated), but not shelf-life-once-opened. Perhaps most importantly, travel vaccine administration is quite different from traditional perishable product stock management as used for blood products or fresh food. The availability of multi-dose vials with rapid spoilage and costly wastage, and the different vaccine assortment requirements of each patient [2,7,60], impose additional constraints not considered by standard perishable inventory management procedures, or by vaccine formulary optimization approaches. For patient <sup>fl</sup>ow management, operations researchers have historically focused on the assignment of limited, shared, and costly physical resources (such as surgical beds, inpatient beds, and diagnostic facilities). Though multi-dose vaccine vials are limited, shared, and costly, multi-dose vaccine vials are unlike beds or diagnostic facilities in that they have the unusual property of needing to be discarded within a short time after their <sup>fi</sup>rst usage, which complicates their management. Unlike surgical or diagnostic clinics, where urgency is determined by the severity of the patient's clinical assessment, in travel clinics the patients are not ill and urgency is determined by the relative expense and volatility of open vaccination vials.

This paper therefore de<sup>fi</sup>nes a new and distinct class of problem— the perishable multi-dose vial administration problem (travel vaccine administration problem)—and its solution using operations research and decision support techniques.

## 3. The integer programming model

We now consider the problem of scheduling patients in need of multiple vaccines for foreign travel purposes. Each patient is to be assigned to one time slot of constant duration (e.g. 15 min) in which they will receive the needed vaccines. We assume throughout that the number of patients to be seen is less than or equal to the number of available time slots. We also assume a single patient queue and a single server (i.e., one nurse).

Vaccines are available in both single-dose and multi-dose formulations. In the multi-dose formulation case, the vaccine vial contains multiple doses which, once opened, can only be used within a certain number of times slots; after which any remaining doses from the vial must be discarded for safety and ef<sup>fi</sup>cacy reasons. The single-dose formulation is used immediately, for a single patient, so no doses are wasted once opened. However, as the single-dose formulation is typically 10% to 30% more expensive per dose than the comparable multi-dose formulation, the multi-dose formulation is preferred if patients can be scheduled in such a way as to minimize wasted (unused expired) doses from a multi-dose vial. It is assumed that using all doses from a multi-dose vial is cheaper than using the same number of single doses, due to economies of scale in packaging cost. Based on our observations from current vaccine pricing practice, we further assume that wasting any number of doses, w, from an n-dose multi-dose vial is always more expensive than using (n–w) single doses, where w≥1. Therefore, a multi-dose vial will only be opened if all the doses it contains will be used (i.e. no doses will be wasted). If opening a multi-dose vial would have led to any doses from that vial being wasted, then single doses vials will be used instead.

Let the binary variable $p _ { i j } = 1$ if patient i is scheduled to be seen during time slot j; and 0 otherwise. Further suppose patient i requires a number of different vaccines indicated by the binary vector a where $a _ { i k } = 1$ if patient i requires vaccine k and is 0 otherwise. Let $Q _ { k m }$ denote the number of doses of vaccine k available per vial in formulation m (i.e., where m indexes a single or multi-dose formulation of vaccine k). Let $I _ { k m }$ denote the number of vials of formulation m of vaccine k available in inventory. Let $T _ { k m }$ denote the number of consecutive time slots in which doses from a speci<sup>fi</sup>c vial of formulation m of vaccine k may be administered once the vial is opened. For example, if we are scheduling in 15-minute time slots and a vial of formulation m of vaccine k contains $Q _ { k m } = 3$ doses that may be administered within an hour of opening the vial, then the 3 available doses from that vial can only be administered within $T _ { k m } = 4$ consecutive possible dosage times slots. So, continuing with this example, if the patient scheduled for time period j requires vaccine k, that requirement could be met by using the <sup>fi</sup>rst possible dosage time slot from a vial opened freshly in time period j (of either a single or multi-dose formulation of the vaccine), or by using the second possible dosage time slot from a multi-dose vial opened in time period j−1, or by using the third possible dosage time slot from a multi-dose vial opened in time period $j - 2$ , or by using the fourth possible dosage time slot from a multi-dose vial opened in time period j−3. Thus, we let the binary variable $d _ { n k m j } = 1$ if the nth possible dosage time slot from a vial containing formulation m of vaccine k is used in time slot j; and 0 otherwise. Notice that the dosage represented by the variable $d _ { n k m j }$ implicitly comes from the vial of formulation m of vaccine k that is opened in time slot $j - n + 1$ . Of course, constraints will ensure that no more than $Q _ { k m }$ doses are used from any vial of formulation m of vaccine k and that the <sup>fi</sup>rst dosage time slot for any vial is used before any subsequent dosage time slots from the same vial are used.

A binary integer programming model for this problem is given as follows. Let $c _ { k m }$ denote the cost of a vial of formulation m of vaccine k. Our objective in Eq. (1) is to schedule patients in such a way as to minimize the total cost (or, if $c _ { k m } = 1$ , the total number) of vials required to complete the necessary vaccinations. (Note that $d _ { 1 k m j } = 1$ whenever the first dose from a previously unopened vial containing formulation m of vaccine k is administered in time slot j.)

$$
M I N \Sigma_ {k} \Sigma_ {m} \Sigma_ {j} c _ {k m} d _ {1 k m j}\tag{1}
$$

Subject to

$$
\sum_ {j} p _ {i j} = 1, \forall i\tag{2}
$$

$$
\sum_ {i} p _ {i j} \leq 1, \forall j\tag{3}
$$

$$
\sum_ {i} a _ {i k} p _ {i j} \leq \sum_ {n} \sum_ {m} d _ {n k m j,} \forall k, j\tag{4}
$$

$$
\sum_ {n = 1} ^ {T _ {k m} - 1} d _ {n + 1, k, m, j + n} \leq (Q _ {k m} - 1) d _ {1 k m j}, \forall k, m, j\tag{5}
$$

$$
\sum_ {j} d _ {1 k m j} \leq I _ {k m}, \forall k, m\tag{6}
$$

$$
\text { All   } p _ {i j} \text {   and   } d _ {n k m j} \text {   are   binary. }\tag{7}
$$

Eqs. (2) and (3) are standard assignment problem constraints requiring, respectively, that each patient be assigned to a single time slot and each time slot be assigned, at most, a single patient. Constraints (4) and (5) together ensure that the cost associated with a given patient schedule is computed appropriately by the objective function (1). Constraint (4) ensures that each vaccine k required by the patient scheduled for time slot j has an appropriate binary dosage variable $d _ { n k m j }$ set equal to one. Constraint (5) imposes several of the necessary conditions for this problem. First, it requires that the <sup>fi</sup>rst dose from a vial containing formulation m of vaccine k (represented by $d _ { 1 k m j } )$ must be used (and accounted for in the objective function (1)) if any other doses from the vial are used. Second, it ensures that no more than $Q _ { k m } - 1$ doses beyond the <sup>fi</sup>rst dose (or $Q _ { k m }$ total doses) are administered from the vial. Finally, it also ensures that all doses administered from a vial are given within the appropriate time-span for the drug in question (that is, within $T _ { k m } - 1$ periods following the time period in which the <sup>fi</sup>rst dose from the vial is used).

Constraint (6) ensures that the number of vials of formulation m of vaccine k opened does not exceed the related number of vials available in inventory. In our computational testing with this model, we assume unlimited inventory of all vaccine formulations as well as unlimited shelf life before opening a vial (otherwise using an about-to-expire multi-dose formulation to treat a single patient is less wasteful than using a recently acquired single dose). We believe the assumption of fresh vaccines always being available is reasonable in the light of the long shelf life of vaccines currently in production, and given vaccine stock ordering and issuance recommendations provided by the CDC. Assuming manufacturer's supply fresh stock to clinics, all popular vaccines have a long shelf life—1 to 18 years [42]—except for the <sup>fl</sup>u vaccine which is valid only for the current <sup>fl</sup>u season (a few months). Further, the CDC requires that primary vaccine coordinators at each clinic rotate stock so that vaccine closest to its expiration date be used <sup>fi</sup>rst, that vaccine inventory be conducted monthly to ensure supply is adequate to meet demand, that the condition and expiration date of all vaccines be checked upon arrival at the clinic, and that all clinics have emergency vaccine supplies available at a backup location such as a local hospital, pharmacy, long term care facility, or the Red Cross [2]. Given the long shelf life of vaccines, and these rigorous vaccine inventory management protocols, the incidence of stock-outs or necessity to use about-to-expire stock should be rare.

## 4. The genetic algorithm (GA) implementation

Genetic algorithms [22], also known as evolutionary algorithms, make use of selection, mutation, and crossover in evolving improved solutions to problems. In a nutshell, GAs work by generating a population of numeric vectors (called chromosomes), each representing a possible solution to a problem. The individual components (numeric values) within a chromosome are called genes. New chromosomes are created by crossover (the probabilistic exchange of values between vectors) or mutation (the random replacement of values in a vector). Mutation provides randomness within the chromosomes to increase coverage of the search space and help prevent premature convergence on a local optimum. Chromosomes are then evaluated according to a <sup>fi</sup>tness (or objective) function, with the <sup>fi</sup>ttest surviving into the next generation. The result is a gene pool that evolves over time to produce better and better solutions to a problem. The GA's search process typically continues until a pre-speci<sup>fi</sup>ed <sup>fi</sup>tness value is reached, a set amount of computing time passes, or until no signi<sup>fi</sup>cant improvement occurs in the population for a given number of iterations. GA's have been shown as a viable alternative to traditional mathematical programming formulations for various classes of dif<sup>fi</sup>cult combinatorial optimization problems [3,11].

In the travel vaccine problem, each GA chromosome is a nonrepeating sequence of patients (permutation of unique patient identi<sup>fi</sup>ers). The <sup>fi</sup>tness function computes the cost of vaccinating the current patient sequence using multi-dose vials wherever economically prudent, in place of the single-dose formulation, to achieve economies of scale.

## 5. Methodology

To evaluate the potential usefulness of our optimization techniques, we generated simulated data for the operation of a clinic that processes 30 patients each day. We assigned each patient to a 15-minute time slot, which is consistent with <sup>fi</sup>ndings in the medical literature as well as the actual scheduling practice at the county health clinic that prompted this study (though time-motion studies show that the time taken to physically administer a single vaccine is on the order of 1.7 to 2.4 min [46], an average patient inoculation visit comprising a review of travel plans and the administration of multiple vaccines consumes approximately 14 min [53]). Further, we assumed that vaccinations were performed by a single healthcare practitioner (nurse) working a 9-hour shift, from 8 am to 5 pm, with two 15-minute breaks and an hour for lunch. Such a shift allows for thirty 15-minute periods in which to see patients; hence 30 patients per day.

Accounting for breaks, lunch and any other non-service providing periods is an integral part of this problem as these time periods have direct implications on the potential expiration and usability of open vials of multi-dose vaccines. Fortunately, such issues are easy to accommodate in our proposed solution techniques by assigning arti<sup>fi</sup>cial patients (requiring no vaccinations) to the time periods where service is unavailable. In this study, we assumed no service would be provided in the periods from 10:00–10:15, 12:00–1:00, and 3:00–3:15 to allow for breaks and lunch for the service provider. However, with our proposed solution techniques it would be easy to modify this assumption to allow for <sup>fl</sup>exibility in when breaks and lunch occur (e.g., we could easily require that an arti<sup>fi</sup>- cial patient be scheduled either from 10:00 to 10:15 or from 10:15 to 10:30).

To evaluate the effectiveness of our solution techniques we randomly generated 30 trials representing 30 independent days of patient treatment. Each trial consisted of 30 randomly generated patients, each requiring from 1 to 7 inoculations out of 20 possible available vaccines (with an average of 3.74 vaccinations per patient). Each vaccine was assumed to be available in two formulations: a single-dose formulation, and a multi-dose formulation. We obtained and used vaccine formulation (multi-dose vs. singledose), shelf-life-once-opened, and pricing data from the United States Centers for Disease Control [2,7,8,51,60] and MMCAP [51], a multi-state pharmaceutical contracting alliance consisting of 44 member states and controlling over \$1 billion of annual pharmaceutical purchases. Per-dose costs varied from \$6 per dose (for A<sup>fl</sup>uria® <sup>fl</sup>u vaccine 10-dose vial) to \$85 per dose (YF-Vax®, single dose). As is to be expected, multi-dose formulations were priced lower per dose than the equivalent single-dose formulation, typically by 10% to 30%, meaning that one or more wasted doses would render the use of a multi-dose formulation insensible. For multi-dose formulations, shelf-life-once-opened in our experiments varied between 45 min (3 service periods) and 75 min (5 service periods). The vaccine formulation and cost data was held constant across each of our 30 replications.

The typical scheduling practice used at travel clinics involves patients calling several days or weeks ahead of time to make an appointment for service on a particular day at a particular time. On a given day, the clinic then processes patients on (more or less) a FIFO basis. Such a system is convenient for the patient but can be quite inef<sup>fi</sup>cient for the clinic from a cost management perspective. For instance, if <sup>fi</sup>ve patients need to receive an expensive vaccination on the same day with two patients arriving early in the day and the other three arriving late in the day, the clinic will likely have to use <sup>fi</sup>ve single-dose vials of vaccine rather than a less costly multi-dose formulation, due to the short shelf-life once opened.

Another approach to clinic scheduling (where our proposed opti mization techniques could be used) would be for patients to call several days or weeks ahead of time and select a day and, optionally, a planning time window during that day when they could be at the clinic to receive inoculations. Each day, the clinic could then look at the next day's workload and determine a schedule that orders that day's patients in a way that makes the best use of multidose formulations of vaccines and minimizes costs. Of course, if a scheduled day <sup>fi</sup>lls up many days in advance, the clinic may optimize that day's workload multiple days in advance. Knowing their schedule many days early may be more convenient for patients, though any subsequent cancellations by other patients may (or may not) require a reshuf<sup>fl</sup>ing of the schedule. Once the schedule is determined, patients could be noti<sup>fi</sup>ed (via phone call, e-mail, or text message) of the speci<sup>fi</sup>c time within their planning time window that has been assigned (and/or asking them to arrive 15 to 20 min before their assigned time to complete paperwork and create a safety buffer of time for the schedule). While such an approach might be somewhat less convenient for the patient, this type of scheduling system is commonly used with surgical patients. Furthermore, if a patient knows well in advance that their appointment will be between, say, 8:00 am and 10:00 am, then the inconvenience of being noti<sup>fi</sup>ed the day before of the exact time within that interval is fairly minimal.

In this study, we consider three different planning time window scenarios de<sup>fi</sup>ned as follows:

1) Four 2-hour windows (8:00–10:00, 10:00–12:00, 1:00–3:00 and 3:00–5:00),

2) Two 4-hour windows (8:00–12:00 and 1:00–5:00), and

3) One 8-hour window (8:00–5:00, omitting the lunch hour).

For example, in the four 2-hour windows scenario, patients would initially self-select into one of the four 2-hour windows (subject to available service capacity within the window) and their scheduled order within that window is optimized. It is important to note that this does not reduce the problem to four individual optimization problems because patients in one time window could potentially be sharing a multi-dose vaccination with patients in an adjacent time window. At the other extreme, in the one 8- hour window scenario, patients would initially select the day they would like to come to the clinic (subject to available service capacity) and are then scheduled optimally into any of the 30 possible 15-minute time slots available that day. The one 8-hour window scenario provides the greatest freedom and potential for optimization and costs savings but also creates the most schedule uncertainty and potential inconvenience for patients; whereas the four 2-hour window scenario provides the least potential for cost savings but the greatest convenience and schedule certainty for the patient.

For the 8-hour window, there are 30! $( = 2 . 6 5 \mathrm { E } + 3 2 )$ total possible patient orderings. For the 4-hour time window setting there are $1 \bar { 5 } ! ^ { 2 } ( = 1 . 7 1 \mathrm { E } + \bar { 2 } 4 )$ total patient orderings. For the 2-hour time window there are $7 ! ^ { 2 } 8 ! ^ { 2 } ~ ( = 4 . 1 3 \mathrm { { E } } + 1 6 )$ total patient orderings. In all cases, brute-force enumeration of all possible patient orderings is time-prohibitive. For the 8-hour window case, at 8200 enumerations evaluated per minute (which we determined to be the capacity of the 2 GHz personal computers used in our experiments) full enumeration would take 6.15E+22 years. Even for the simplest 2-hour time window case, full enumeration would take 9.5 million years.

We began by computing a lower bound for our problem. A lower bound can be computed by <sup>fi</sup>nding the lowest possible total vaccine cost, assuming multi-dose vials with in<sup>fi</sup>nite shelf-life-once-opened could have been used. For example, assume one drug with two formulations: single dose vials or <sup>fi</sup>ve-dose vials. Assume each individual dose in the multi-dose vial is cheaper than a single dose, if all doses are used. If 6 patients require that drug, and the drug has in<sup>fi</sup>nite shelf-life-once-opened, the lower bound involves the opening of one <sup>fi</sup>ve-dose vial and one single-dose vial, as this would be the cheapest possible solution. Mathematically:

$$
\begin{array}{l} \text { Lower   bound } \\ = \sum_ {k} (c _ {k m} \times t r u n c a t e (p _ {k} \div Q _ {k m}) + c _ {k s} \times m o d u l u s (p _ {k}, Q _ {k m})) \end{array}
$$

where:

$c _ { k m }$ is the cost of a Multi-dose vial of drug k, and $c _ { k s }$ is the cost of a Single-dose vial of drug k.

$p _ { k }$ is the total number of patients requiring drug k.

$Q _ { k m }$ is the number of doses in a Multi-dose vial for drug k

truncate() provides the integer portion of a number, and

modulus() returns the remainder after dividing the <sup>fi</sup>rst number by the divisor

This is a lower bound for the 1-window problem. For the 2- window and 4-window problem, if no drug has a shelf-life-onceopened that exceeds the duration of the lunch break, the lower bound can be further tightened by considering before-lunchpatients and after-lunch-patients separately, as open multi-dose vials must be disposed of during the lunch break, and new multidose vials must be opened (if economically feasible) after lunch.

Using the lower bound as the best case—albeit infeasible due to limited shelf-life-once-opened—we compare the effectiveness of the following scheduling procedures using each of our 30 simulated days of patients and each of the 3 planning time window settings (90 total test cases):

1. FIFO: Patients are vaccinated in the (randomly generated) order of their appointments at the clinic. Multi-dose vaccines are used whenever it is advantageous to do so cost-wise.

2. RANDOM: In this approach, used as a ‘straw man’ for comparison, patient sequences are generated at random, and evaluated for cost. We set the RANDOM algorithm to proceed for no longer than 2 h total, and to terminate after 15 min with no improvement. The goal was to rapidly evaluate as many (different) random solutions as possible. Disadvantages to this approach are that the solution space is exceptionally large, so the probability of achieving a solution close to the optimal is tiny. Inef<sup>fi</sup>ciency arises as large numbers of solutions with high cost are evaluated since the random generator proceeds with reckless abandon.

3. SORT: Patients begin in their original (FIFO) order and are sorted within each planned time window using a rapid greedy heuristic. This heuristic <sup>fi</sup>rst <sup>fi</sup>lters the data to identify vaccines required by enough patients in each time window to warrant use of a multi-dose vial. Next, the vaccines are sorted in descending order of their effective cost per dose, multiplied by the number of patients in the time window requiring that dose. Finally, a multi-level sort is performed to group together patients requiring the most expensive vaccines, then the next most expensive vaccine, and so on.

4. CPLEX: Patients are scheduled within their appropriate time window using the model in Eqs. (1)–(7) above, formulated and solved in CPLEX 11.0 [28]. This model requires about 3000 binary variables and approximately 2500 constraints. When using more than one time window, the appropriate $p _ { i j }$ variables are set to zero to prevent patients from being assigned to times slots outside their assigned time windows. We solve the model using the SORT ordering as a starting solution for CPLEX, since the SORT solution is a good solution that can be computed within milliseconds. For all problems, the search was terminated when a solution was proven to be within 0.5% of the theoretical optimum or when 2 h of run time had elapsed (whichever occurred <sup>fi</sup>rst). Non-default CPLEX parameters used in our testing include: Time limit in seconds (CPX\_PARAM\_TILIM) 7200, Mixed integer optimality gap tolerance (CPX\_PARAM\_EPGAP) 0.005, Variable selection strategy (CPX\_PARAM\_VARSEL) 4, Frequency to apply periodic heuristic algorithm (CPX\_PARAM\_HEURFREQ ) 50, Number of cutting plane passes (CPX\_PARAM\_CUTPASS) 1. For problems with one 8-hour window, a lower bound on the required number of vials for each type of vaccine can be computed easily by summing the number of doses required by the patients on a given day and dividing the result by the number of doses in the multidose formulation of the vaccine (and rounding fractional quotients to the next highest integer value). For problems with four 2-hour windows or two 4-hour windows, better bounds on the required number of vials can be computed by summing the number of doses required, respectively, by the patients before and after lunch on a given day and dividing the result by the number of doses in the multi-dose formulation of the vaccine (and rounding fractional quotients to the next highest integer values). (This assumes any multi-does vials opened before lunch would expire by the end of the lunch break, as is the case for the data in our test problems.) Adding such lower bound constraints on the minimum number of vials to be opened for each type of vaccine can sometimes help to tighten the linear programming (LP) relaxation of the formulation in Eqs. (1)–(7) and was done for each data set in this study. See Ref. [59] for further discussion of this issue.

5. GA: To ascertain the usefulness of GAs to the travel vaccine patient scheduling problem, we used Solver's evolutionary optimizer included natively with Excel 2010. No additional software purchase (beyond Excel 2010) would therefore be required for the travel clinic to use this solution approach. However, we did have to write a special purpose, user-de<sup>fi</sup>ned <sup>fi</sup>tness function in Excel VBA, which was tailored for the travel vaccine problem. A pseudo-code description of this <sup>fi</sup>tness function is provided in Appendix 1. The genetic algorithm generates random patient sequences (permutations) and assesses the cost of treating patients in that sequence using multi-dose vials wherever economically feasible. Based on our observations of current vaccine pricing practice, it is economically feasible to open a multi-dose vial if a look-ahead at the current candidate patient schedule shows that all doses of the current vaccine will be administered before the vial expires. It is economically infeasible to open a multidose if a look-ahead at the current patient schedule shows any doses will be wasted: in this case, single doses will be used instead. The SORT ordering (a good solution, which can be computed within milliseconds) is used as a candidate starting solution for the GA, along with random patient orderings. At each generation, the best patient orderings are selected and mutated. The stopping condition used for the GA was as follows: the GA was set to terminate any time no solution improvement was observed for 15 min, or if 2 h had elapsed, whichever occurred <sup>fi</sup>rst. No other changes were made to Solver's default evolutionary parameter settings.

All computations were carried out on a computer with a 2.0 GHz processor and 1.0 GB of RAM running Windows Vista—typical of the affordable, mass market desktop computer found in, or accessible to, a modern travel clinic. The various methods being compared were applied to the same set of test problems, so that each problem was solved four times. For both solution quality and solution time, two-tailed, paired difference Student's t-tests, with a 99% con<sup>fi</sup>dence level, were used to ascertain if the differences between algorithms were statistically signi<sup>fi</sup>cant.

## 6. Computational results

In this section, we compare both solution quality and solution time of all the approaches we tested.

## 6.1. Solution quality

Fig. 1, a box and whisker plot, allows rapid comparison of solution quality for all approaches, across all 30 trial days, and all three time-window settings. To make comparison easier, the y-axis shows the change, in Dollars Per Day, from the FIFO solutions, rather than simply the average daily vaccination cost. The average daily vaccination cost using FIFO was \$4038. A change-from-FIFO of -\$200 therefore represents an approximately 5% saving from FIFO. Within a given time window setting (1 window, 2 windows, 4 windows), an asterisk (\*) alongside an algorithm's name on the x-axis indicates the algorithm's solution quality is signi<sup>fi</sup>cantly better than the algorithm to its left, when measured at the 99% con<sup>fi</sup>dence level. For SORT, which has no explicit algorithm to its left, an asterisk alongside SORT indicates it is statistically signi<sup>fi</sup>cantly better than FIFO (FIFO is used as the baseline).

When using a single time window (allowing for maximum scheduling <sup>fl</sup>exibility) the simple and rapid SORT technique reduced the average daily cost of vaccination (over the FIFO schedule) by just over \$100 (or 2.8%). In comparison, the CPLEX and GA methods reduced the average daily cost signi<sup>fi</sup>cantly more—about 3 times more—to almost \$300 (or 7.2%). The difference between CPLEX and the GA was not statistically signi<sup>fi</sup>cantly different.

As expected, the cost advantage of applying any of the optimization techniques is reduced as the number of potential time windows is increased. This chart illustrates the trade-offs clinics face in terms of minimizing costs (which is facilitated by having a single time window) and accommodating the scheduling preferences of the patients (which is facilitated by offering a greater number of time windows).

Comparing the optimization algorithms to each other, CPLEX's branch-and-bound algorithm and Solver's evolutionary genetic algorithm (GA) were the clear winners by solution quality. Table 1 shows the number of occasions CPLEX produced the winning solution versus the GA. CPLEX <sup>fi</sup>nds a better solution than the GA on 17 of 30 one-window scenarios and 18 of 30 four-window scenarios, but the GA outperforms CPLEX on 16 of 30 two-window scenarios. The two algorithms regularly achieve ties. Notably, on average, the GA and CPLEX approaches produced solutions within 1/20th of 1% of one another. Furthermore CPLEX was statistically signi<sup>fi</sup>cantly better than the GA only on the four-window problems, and even then the average difference between the two algorithms was only \$4. On four-window problems, CPLEX's maximum win margin was \$18, and the GA's maximum win margin was \$5.

For the one-window setting, it is signi<sup>fi</sup>cant to note the worst case performance for both CPLEX and the GA over the 30 trials still produced solutions that were over \$170 better for the day than the FIFO solution. In the best cases, CPLEX and the GA outperformed the FIFO technique by almost \$390 for the day. If the clinic adopted the one time window scheduling technique and optimized with our two best methods, a potential average annual cost savings of approximately \$72,000 per year (with a standard deviation of \$12,178) is achievable, assuming a <sup>fi</sup>ve day work week and the equivalent of 50 operating weeks per year.

Alternatively, when using four time windows (allowing for greater scheduling convenience for patients) the SORT technique reduced the average daily cost of vaccination (over the FIFO schedule) by \$33.71 (or 0.83%) and, in the worst case, increased the cost over the FIFO schedule by \$40.61. However, in the same set of problems the CPLEX and GA techniques reduced the average daily cost by nearly \$150 (or 4%). In the worst case, CPLEX and the GA produced a solution that was \$80 better than the FIFO solution and, in the best case, outperformed the FIFO technique by \$256. If the clinic adopted the four time window scheduling technique and optimized with our two best methods, these results indicate a potential average annual costs savings of approximately \$37,000 per year (with a standard deviation of \$9893), again assuming a <sup>fi</sup>ve day work week and the equivalent of 50 operating weeks per year.

Table 1  
![](/api/attachments/4F9H294R/fulltext/images/e695994061e057e03257d6a386540571066327869f1427d126340abf2b5d6170.jpg)  
Fig. 1. Box-and-whisker plot showing relative solution quality for all methods

Clearly, the RANDOM approach, which we used as a strawman, performs poorly. Let us, for instance, use Scenario 1 as an exemplar for the RANDOM approach. Looking at the one-window case, since it is the most complex to solve, we found that the RANDOM approach to this problem generates solutions with a mean daily cost of \$3914 and standard deviation of \$24. Using this sample mean and standard deviation, the percentage of random solutions, from the full population of random solutions, that are within 1% of the theoretical optimum is 2.86E−36. The percentage of random solutions better than CPLEX is 1.78E−35, and better than SORT is 4.69E−06. Hence, any random solution has a miniscule chance of being better than CPLEX. However, generating a few thousand alternatives per minute on our test workstations, RANDOM has a high probability of beating SORT within a few minutes.

Lastly, it is worthwhile to compare our results to the prior prescriptions of the literature regarding vaccine format utilization. In our experiments, we found that 63%–76% of doses administered come from single-dose vials (i.e. roughly one quarter to one third come from multi-dose vials). Recent research [34] has overlooked the opportunity to stock multiple vaccine formats—single and multi-dose—and has considered only the possibility of stocking just a single format (single or multi dose). Lee et al. [34] advise that this choice between formats be based on the anticipated mean patient arrival rate, for the coming year, for a given vaccine. Firstly, this assumes that the daily mean patient arrival rate over an entire year has low variance, which we have found not to be the case for travel vaccines, like Yellow Fever, were patient arrival rate is highly volatile. Secondly, it is assumed that the patient arrival rate for different vaccines is independent, which is not the case in a travel clinic. Finally, there is no allowance for the reordering of patients in order to take advantage of both single and multi-dose vials, when appropriate, on a given day. Both the exclusive singledose and exclusive multi-dose stocking practices would be more costly than our FIFO results. Our FIFO baseline assumes that multidoses are only opened when all doses will be administered. As all multi-dose vials are fully consumed, there is no wastage of partially-used vials (assuming no last-minute patient cancellations). In contrast, a clinic that stocks only single-dose vials will incur more expense than our FIFO baseline as more economical multi-dose formats are never used when it would have been economical to do so. Similarly, a clinic that stocks only multi-dose vials will incur more expense than our FIFO baseline as many doses from multi-dose vials will be wasted, since single doses are not available in cases where it is economically infeasible to open a new multi-dose.

Number of times each algorithm performs best, over 30 scenarios

<table><tr><td>Time windows</td><td>CPLEX</td><td>GA</td><td>Tied</td></tr><tr><td>1</td><td>17</td><td>13</td><td>-</td></tr><tr><td>2</td><td>8</td><td>16</td><td>6</td></tr><tr><td>4</td><td>18</td><td>2</td><td>10</td></tr></table>

## 6.2. Solution time

Fig. 2, another box and whisker plot, shows the elapsed time to best solution for all approaches used. Within a given time window setting, an asterisk (\*) alongside an algorithm's name on the y-axis indicates the algorithm's time to best solution is signi<sup>fi</sup>cantly different from the algorithm directly below it, when measured at the 99% con<sup>fi</sup>dence level. Fig. 2 shows only the time at which the best solution was found. Total algorithm runtime (shown in Fig. 3) is often lengthier. For the GA and RANDOM algorithms, the algorithm terminates 15 min after the best solution is found. For CPLEX. the algorithm was set to terminate at 2 h or when the best solution is within 0.5% of the theoretical optimum. For SORT, the algorithm terminates as soon as its solution is found.

SORT is the fastest method, taking only a few milliseconds, but, as we saw earlier, producing low quality results. CPLEX works rapidly on two- and four-window scenarios, but takes over an hour to <sup>fi</sup>nd its best solution on the more complex one-window setting. When using CPLEX on one-window problems, all but one of the 30 problems ran for the full 2 h allocated and produced solutions that could be shown to be within 1.57% of the theoretical optimum, on average. When using two or four time windows, CPLEX solved the problem to within 0.5% of optimality in a reasonably short amount of time. In comparison, the GA found low cost solutions of comparable quality to CPLEX generally within 1 to 10 min irrespective of the number of time windows. The GA therefore appears to provide the best time–cost tradeoff, as it consistently produces solutions of equivalent quality to CPLEX (practically speaking), in much less time. An advantage of our proposed GA technique is that a clinic can implement it in Excel 2010 (which is likely to already be available) while acquiring CPLEX might be cost prohibitive. However, it should be noted that several open source optimizers are now freely available (e.g., see opensolver.org and coin-or.org) and are capable of solving this problem as well.

Fig. 3, shows the total run time for all approaches used (in comparison to Fig. 2, which shows the elapsed time to best solution for all approaches). Comparing Fig. 3 (total run time for all approaches)

![](/api/attachments/4F9H294R/fulltext/images/c6301e281cb02aabb2d69e0336a0682e3c5466d9620cbfb6534eafb45d465dad.jpg)  
Fig. 2. Box-and-whisker plot showing time-to-best-solution for all methods

to Fig. 2 (time to best solution for all approaches), we see the following. For the SORT algorithm, total run time and time-to-best solution are the same in all cases. For RANDOM and GA, the total run time is simply 15 min greater than the time-to-best solution (since these algorithms were set to terminate with 15 min of no improvement). So, the only series of interest is CPLEX: for 4-window and 2-window cases (simplest cases) CPLEX terminates about 10 min after <sup>fi</sup>nding the best solution (i.e. rapidly determines that its solution is within 0.5% of the theoretical optimum). For the hardest case (1 time window) CPLEX continues to run, on average, for almost an hour with no improvement, eventually terminating at the 2 hour time limit for all but one of the 30 example scenarios.

## 7. Implications

As these results indicate, the CPLEX and GA techniques signi<sup>fi</sup>cantly improve upon average performance of both the FIFO and SORT solutions, with savings between approximately 4% and 7% depending on patient-scheduling <sup>fl</sup>exibility (one vs. two vs. four time-windows). Further, the GA produces very high-quality solutions within a few minutes on even the most complex (1 window) time slot variation.

Though the average daily savings provided by our DSS may seem moderate, the potential impact of the accumulated savings is quite signi<sup>fi</sup>cant, especially when the savings are applied to a number of clinics and vaccinations over an extended time. Average daily savings of \$287 per day, from the best (GA and CPLEX) methods in our experiments above, translate to annual savings of about \$72,000 per clinic per year, at a busy clinic that operates a full patient load (assumed at 30 patients per day), 250 days per year. Implementation of the DSS at 200 busy clinics, yields \$14.4 million of annual savings; at 2000 busy clinics the saving is \$144 million annually. These estimates should, however, be regarded as optimistic, as our model assumes no appointment cancellations, no stock-outs (forcing the use of a single dose from a multi-dose formulation), and no shelf-life issues (forcing the use of an about-to-expire multi-dose in place of a fresh single dose).

Over 540 million doses of the Yellow Fever (YF) vaccine alone have been administered globally since its invention in 1937 [35], averaging roughly 7 million doses internationally per year. In the United States, the CDC has 5135 authorized civilian centers in its Yellow Fever Vaccination Center Registry (excluding federal and military facilities) [9]. According to the CDC (from a personal e-mail communication, via cdcinfo@cdc.gov, in March 2010):

“In terms of the number of people vaccinated per year in the US, the most recent data we have is from 2006, when there were approx. 200,000 doses of YF vaccine administered to civilians … The average yearly number of doses administered to military personnel during 1998–2002 was 185,400—but that number could have changed since that period.”

Lindsey et al. [35] comment that the estimated 200,000 doses of YF vaccine sold annually to civilian providers in the United States are predominantly sold in single-dose vials, resulting in little or no YF vaccine wastage. However the single-dose formulation costs 25% more, per dose, than the multi-dose formulation [51]. With a current wholesale cost of \$85 per single dose [51], a modest 5% reduction in total vaccination cost, as suggested in our experiments, would give annual system-wide savings amounting to \$1.7 million in the United States (=\$85×400,000 doses×5%), or \$30 million (=\$85×7 million doses×5%) globally, for the Yellow Fever vaccination alone. Moreover, a number of vaccines are available and anticipated in multidose formulations—e.g. Yellow Fever (YF), Inactivated Polio Vaccine (IPV), In<sup>fl</sup>uenza, Typhoid, Anthrax, PPV, HPV, DTaP, Measles (MEA), Bacille Calmette-Guérin (BCG), Hemophilus in<sup>fl</sup>uenza type B (Hib), Pneomococcal Conjugate Virus (PCV), Human Pappilomavirus (HPV), Rotavirus, and DTP-HepB-Hib Pentavalent [34,60,65,66]. Multiplying the single-vaccine savings by multiple vaccines, could potentially yield total annual savings exceeding \$15 million in the US, or \$300 million globally.

![](/api/attachments/4F9H294R/fulltext/images/d110033a42911a84ced7350f87d40217c9f169659766e7a768c72dd7e98b1140.jpg)  
Fig. 3. Box-and-whisker plot showing total run time for all methods

Lee et al. [34] demonstrate that the optimal number of doses per vial to be purchased by the clinic's formulary may vary by vaccine, geographically, and by patient demand. With medical researchers expecting that mass customization of vial dosage purchasing decisions to be on the horizon, a model like the one proposed here would be helpful in ensuring multi-dose formulations in the clinic's formulary are used in the most ef<sup>fi</sup>cient way.

Our results also illustrate that, the greater the <sup>fl</sup>exibility of patients and the greater the number of patients, the more valuable the decision support tool becomes, particularly the GA method, which scales well as patient numbers increase. According to travel industry data, 65% of intercontinental travelers reserve their <sup>fl</sup>ights more than 2 weeks in advance of travel [15]. If some portion of these travelers were available to receive their vaccinations anywhere within a 10 day window, scheduling heuristics that are able to cope with large patient numbers have greater scope to produce larger cost savings.

Aside from the potential <sup>fi</sup>nancial bene<sup>fi</sup>ts of this model, the model also offers some convenience bene<sup>fi</sup>ts to the patient. Under existing FIFO scheduling procedures, patients frequently endure long waits as an open vial of an expensive vaccine leads nurses to urgently vaccinate other waiting patients requiring the open vaccine, to the detriment of scheduled patients. Under our proposed system, patients can be informed in advance of appropriate arrival times that should help reduce wait times. In a recent state-of-theart review of challenges and opportunities in appointment scheduling in health care, Gupta and Denton [24] observe that virtually all operations research models of appointment systems ignore patient scheduling preferences and cite the need for new models that address patient preferences. We have demonstrated how time windows may provide a means for addressing this issue in a way that lowers the cost of service while considering patient scheduling preferences and mitigating much of the scheduling inconvenience that patients encounter.

## 8. Limitations and future work

Fine tuning of various algorithm parameters (e.g. GA mutation rates, optimization engine search strategies, etc.), or running parallel computations on a computing cluster, could perhaps yield results slightly better than those we found here. However, the user of our DSS will have little background in optimization methods and little interest in <sup>fi</sup>ne tuning and con<sup>fi</sup>guration, given the low marginal cost reduction available (law of diminishing marginal returns in DSS usage). A streamlined approach, which sacri<sup>fi</sup>ces some technical improvements in favor of enhanced usability, is therefore preferable.

While our DSS appears to produce signi<sup>fi</sup>cant savings, it does require some work and expense to implement. Firstly, a modest software investment would be required by each clinical practice. In particular, the Excel-based travel vaccine patient scheduling decision support system would need to be integrated with the existing patient appointment system and the vaccine formulary data base (which holds inventory, shelf-life-once-opened, and pricing data). Moreover, once the system is implemented, up to 40 min (though usually less than 10 min) is required to run the GA method. Of course, this process can easily be scheduled overnight or during daytime hours when many clinic computers have idle capacity. Patients would then need to be noti<sup>fi</sup>ed of their <sup>fi</sup>nal scheduled time via phone call, text message, or e-mail.

Obviously, last-minute patient cancellations or changes, after creation of the patient vaccination schedule, would impact the costeffectiveness of the recommended solution. On the other hand, communicating with patients a day or so before their scheduled appointments might reveal cancellations and other last-minute scheduling issues that can be addressed proactively rather than reactively. Such cancellations and changes would impact any patient schedule and should not discourage one from formulating a good operational plan. Indeed, the need to reshuf<sup>fl</sup>e patients due to last minute cancellations implies that algorithms that produce a satisfactory (satis<sup>fi</sup>cing) solution within a timely fashion—soon enough to make last minute schedule modi<sup>fi</sup>cations—may be preferable to those that <sup>fi</sup>nd an optimal solution slowly.

Since excessive cancellations would lead to expensive multi-dose vials being opened and unused, attention to patient cancellation frequencies is important, to determine the patient cancellation rate threshold at which the risk of opening multi-dose vials exceeds the bene<sup>fi</sup>t—see Ref. [34].

The model we describe is contingent on vaccine disposal costs being trivial. This is indeed the case, and we expect it to remain so. In this work, we have assumed that multi-dose vials are only opened if all doses will be administered—it is not economically feasible to open a multi-dose otherwise. This assumption is consistent with our observations of current vaccine pricing practice. Given that all doses in a multi-dose will be used in our model (assuming no last-minute patient cancellations), all waste vials will be empty. Empty waste vials are non-hazardous and can be disposed of in the regular trash, at no cost [14]. In the unusual event of needing to dispose of a nonempty multi-dose vial (e.g. due to a last-minute patient cancellation), these are classi<sup>fi</sup>ed as “RCRA Hazardous” by the United States Resource Conservation and Recovery Act (RCRA) [36]. Disposal costs for this class of waste are \$2–\$4 per pound ( \$5–\$9 per kilogram ) [34,36]. Typical vaccine doses are 0.5 ml (about half a gram) per dose and empty 20-dose vials (the largest vial size currently in regular production [2]) weigh no more than 6 g [34], giving a per dose disposal cost (including packaging) of no more than 6 cents per dose, which is negligible. To summarize, while most of our waste vials will be empty, and can be disposed of at no cost in the regular trash, even in the unusual event of needing to dispose of a non-empty vial, the disposal cost is still currently minimal.

As previously mentioned, our model requires that fresh inventory be available. This assumption is supported by the long shelf life (months or years) of vaccines currently on the market. Our model would need some adaptation should new vaccines be introduced which have a short shelf life (of a few days or weeks).

Possible extensions to this work include modifying the model to accommodate multiple servers/nurses – creating the ability to schedule more than one patient per time slot. It would also be interesting to consider the implications of the model for formulary selection (vaccine stock choice decisions), over an extended period.

Finally, while we considered total vaccination cost, some attention could also be paid to additional objectives such as maximizing schedule robustness. In our experiments, we regularly found several thousand permutations with total costs that were very close to the best solution. A solution that is a few dollars from the best solution but that is less sensitive to modi<sup>fi</sup>cation than the best solution, may be preferable, as it mitigates the patient no-show risk. Furthermore, if the risk of individual patient cancellation can be quanti<sup>fi</sup>ed (e.g. patients that don't respond to their text message reminder with an explicit con<sup>fi</sup>rmation are more likely to cancel unexpectedly), this information could be helpful in selecting more robust schedules.

```python
TotalCost = 0
For k = 1 To number of vaccines
    For i = 1 To number of patients
    If a(i, k) = 1 Then
    'Determine how many patients need a dose of vaccine k within the multi-dose time window'
    Need = 0
    For j = i To Min(i + T_{k2} - 1, number of patients)
    Need = Need + a(j, k)
    Next
```

## 9. Conclusions

Optimal choice of single versus multi-dose vaccine formulations within a travel vaccine clinic is highly complex given the short shelf-life-once-opened of multi-dose formulations and the unique vaccine assortment requirements of each patient. In this paper, we introduced a spreadsheet-based decision support tool for the travel vaccination problem. Our tool incorporated a novel binary integer programming model and a GA. In experiments comparing these approaches to alternative patient scheduling mechanisms (such as vaccinating patients on a FIFO basis, or sorting patients so that those requiring the highest-cost vaccinations are grouped together), we have shown that the integer programming and GA methods produce meaningful cost savings, at mild implementation complexity. Importantly, we were able to implement a GA solution to the travel vaccination problem that produces a rapid solution, of similar quality to the integer programming method, within only a few minutes of runtime.

We have demonstrated that our practical decision support tool presents a useful new operations management mechanism that supplements traditional stock issuance and job scheduling policies and could allow health care managers to signi<sup>fi</sup>cantly lower vaccine administration costs. Gupta and Denton [24] observe that while operations research models have been used successfully to improve ef<sup>fi</sup>ciency in many service industries, the same degree of success has not yet occurred in the health care; and note this as an important challenge for the research community. We believe that the DSS proposed in this paper is one small step in meeting this challenge.

## Acknowledgments

The authors would like to thank the anonymous reviewers for various helpful suggestions which greatly improved the quality of the manuscript.

## Appendix 1

The following pseudo-code provides the logic used in our GA implementation to calculate the total vaccination cost for a given patient ordering represented by the binary matrix a(i, k) where entries of one indicate that the ith patient in the matrix requires vaccine k. Below, $c _ { \mathrm { k 1 } }$ and $c _ { \mathrm { k 2 } }$ represent, respectively, the cost of a single and multidose vial of vaccine k; $Q _ { k 2 }$ denotes the number of doses of vaccine k available per vial in the multi-dose formulation of the product; and $T _ { \mathrm { k } 2 }$ represents the number of consecutive time slots in which doses from a speci<sup>fi</sup>c multi-dose vial vaccine k may be administered once the vial is opened.

```txt
'Compute the number of needed doses that can be given from a multi-dose vial'
    Doses = Min(Need, Qk2)
    'Compare cost of using multi-dose vs single doses'
    If ck2 < Doses * ck1 Then
    'Use a multi-dose vial of vaccine k'
    TotalCost = TotalCost + ck2
    'Adjust i for the number of patients serviced'
    For j = i To Min(i + Tk2 - 1, number of patients)
    If Doses > 0 And a(j, k) = 1 Then
    Doses = Doses - 1
    LastPatient = j
    End If
    Next
    i = LastPatient
    Else
    'Use a single dose of vaccine k'
    TotalCost = TotalCost + ck1
    End If
    End If
Next i
Next k
```

## References

[1] P.L. Abad, Optimal pricing and lot-sizing under conditions of perishability and partial backordering, Management Science 42 (8) (1996) 1093–1104.

[2] W. Atkinson, S. Wolfe, J. Hamborsky, L. McIntyre (Eds.), Epidemiology and prevention of vaccine-preventable diseases 12th edition Centers for Disease Con: trol, Washington, DC, May 2011.

[3] R. Barkhi, E. Rolland, J. Butler, W. Fan, Decision Support System induced guidance for model formulation and solution, Decision Support Systems 40 (2005) 269–281.

[4] S.K. Bar-lev, D. Perry, W. Stadje, Control policies for inventory systems with perishable items: outsourcing and urgency classes, Probability in the Engineering and Informational Sciences 19 (3) (2005) 309–326.

[5] Operations Research and Health Care: A Handbook of Methods and Applications, in: M.L. Brandeau, F. Sainfort, W.P. Pierskalla (Eds.), International Series in Oper ations Research and Management Science, Springer, New York, 2004

[6] E. Brodheim, C. Derman, G. Prastacos, On the evaluation of a class of inventory policies for perishable products such as blood, Management Science 21 (11) (1975) 1320–1325.

[7] G.W. Brunette, P.E. Kozarsky, A.J. Magill, D.R. Shlim (Eds.), CDC Health Information for International Travel 2010, Centers for Disease Control, Washington, DC, 2010.

[8] CDC (Centers for Disease Control), CDC Vaccine Price ListAvailable at: http:// www.cdc.gov/vaccines/programs/vfc/cdc-vac-price-list.htm (Accessed June 17, 2011).

[9] CDC (Centers for Disease Control), Yellow Fever vaccination clinicsAvailable at: http://wwwnc.cdc.gov/travel/yellow-fever-vaccination-clinics/search.htm. (Accessed June 24, 2011).

[10] D. Chazan, S. Gal, A Markovian Model for Perishable Product Inventory, Management Science 23 (5) (1977) 512–521.

[11] R. Cheng, M. Gen, Y. Tsujimura, A tutorial survey of job-shop scheduling problems using genetic algorithms, part II: Hybrid genetic search strategies, Computers and Industrial Engineering 36 (1999) 343–364.

[12] S.E. Chick, H. Mamani, D. Simchi-Levi, Supply chain coordination and in<sup>fl</sup>uenza vaccination, Operations Research 56 (6) (2008) 1493–1506.

[13] Y.H. Chun, Optimal pricing and ordering policies for perishable commodities, European Journal of Operational Research 144 (1) (2003) 68–82.

[14] Colorado Department of Public Health and the Environment, Disposal of Waste/Outdated Vaccine, State of Colorado, December 2010.

[15] CWT Travel Management Institute, CWTVISION, Q2, Air BookingsMade 14+ Days in Advance, Carlson Wagonlit Travel, 2011.

[16] R.W. Day, M.D. Dean, R. Gar<sup>fi</sup>nkel, S. Thompson, Improving patient <sup>fl</sup>ow in a hospital through dynamic allocation of cardiac diagnostic testing time slots, Decision Support Systems 49 (4) (2010) 463–473.

[17] F.G. Engineer, P. Keskinocak, L.K. Pickering, Catch-up scheduling for childhood vaccination Operations Research 57 (6) (2009) 1307–1319

[18] M.L. Entrup, M. Grunow, H.O. Gunther, T. Seiler, P. van Beek, An MILP modeling approach for shelf life integrated planning in yoghurt production, Operations Research Proceedings, Springer, Berlin, Heidelberg, 2004, pp. 67–75.

[19] Y. Fenga, B. Xiaob, Integration of pricing and capacity allocation for perishable products, European Journal of Operational Research 168 (1) (2006) 17–34.

[20] C.D. Flagle, Some origins of operations research in the health services, Operations Research 50 (1) (2002) 52–60

[21] C.-H. Goh, B.S. Greenberg, H. Matsuo, Two-stage perishable inventory models, Management Science 39 (5) (1993) 633–649.

[22] D.E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning, Addison-Wesley, Reading, MA, 1989

[23] L.V. Green, S.V. Savin, B. Wang, Managing patient service in a diagnostic medical facility, Operations Research 54 (1) (2006) 11–25.

[24] D. Gupta, B. Denton, Appointment scheduling in health care: challenges and opportunities, IIE Transactions 40 (9) (2008) 800–819.

[25] M.G. Haby, R.J. Miget, The effect of stocking procedure on consumption of shelf life in refrigerated seafoods displayed in full service departments, Journal of Food Distribution Research 21 (1) (1991) 69–80.

[26] S.N. Hall, S.H. Jacobson, E.C. Sewell, An analysis of pediatric formulary selection problems, Operations Research 56 (6) (2008) 1348–1365.

[27] V.N. Hsu, Dynamic economic lot size model with perishable inventory, Management Science 46 (8) (2000) 1159–1169.

[28] IBM, IBM ILOG CPLEX OptimizerAvailable at: http://www-01.ibm.com/software/ integration/optimization/cplex-optimizer/2010.

[29] S.H. Jacobson, E.C. Sewell, R. Deuson, B.G. Weniger, An integer programming model for vaccine procurement and delivery for childhood immunization: a pilot study, Health Care Management Science 2 (1) (1999) 1–9.

[30] S.H. Jacobson, T. Karnani, E.C. Sewell, Assessing the impact of wastage on pediatric vaccine immunization formulary costs using a vaccine selection algorithm, Vaccine 22 (17–18) (2004) 2307–2315.

[31] J. Jesson, R. Pocock, K. Wilson, Reducing medicines waste in the community, Primary Health Care Research and Development 6 (2) (2005) 117–124.

[32] H. Kaspi, D. Perry, Inventory system of perishable commodities, Advances in Applied Probability 15 (3) (1983) 674–685.

[33] J. Keilson, A. Seidman, Product selection policies for perishable inventory systems, Operations Research Center Working Paper OR 226–90, Massachusetts Institute of Technology, Boston, MA, August 1990, pp. 1–47.

[34] B.Y. Lee, B.A. Norman, T.-M. Assi, S. Chen, R.R. Bailey, J. Rajgopal, S.T. Brown, A.E. Wiringa, D.S. Burke, Single versus multi-dose vaccine vials: an economic compu tational model, Vaccine 28 (32) (2010) 5292–5300.

[35] N.P. Lindsey, B.A. Schroeder, E.R. Miller, M.M. Braun, A.F. Hinckley, N. Marano, B.A. Slade, E.D. Barnett, G.W. Brunette, K. Horan, J.E. Staples, P.E. Kozarsky, E.B. Hayes, Adverse event reports following yellow fever vaccination, Vaccine 26 (48) (2008) 6077–6082.

[36] Managing Pharmaceutical Waste: A Discussion Guide for Health-System Pharmacists. American Society of Health Systems Pharmacists. (October 2007) http://www.ashpadvantage.com/docs/PharmaWaste-Discussion-Guide.pdf Accessed on 23 Jan 2012.

[37] S. Nahmias, Myopic approximations for the perishable inventory problem, Management Science 22 (9) (1976) 1002–1008.

[38] S. Nahmias, On ordering perishable inventory when both demand and lifetime are random, Management Science 24 (1) (1977) 82–90.

[39] S. Nahmias, On ordering perishable inventory under Erlang demand, Naval Research Logistics 22 (3) (2006) 415–425.

[40] S. Nahmias, Perishable inventory systems, International Series in Operations Research and Management Science, Springer, New York, ISBN: 978-1-4419-7998-8, 2011.

[41] S. Nahmias, C.P. Schmidt, (S-1, S) policies for perishable inventory, Management Science 31 (6) (1985) 719–728.

[42] New York City Department of Health and Mental Hygeine, Bureau of Immunization, Vaccine Management: Recommendations for Handling and Storage of Selected BiologicalsAvailable at: http://www.nyc.gov/html/doh/html imm/immhand.shtml (Accessed on: 15 Feb 2012).

[43] G. Padmanabhan, P. Vrat, EOQ models for perishable items under stock dependent selling rate, European Journal of Operational Research 86 (2) (1995) 281–292.

[44] Sano<sup>fi</sup> Pasteur, Yellow Fever Vaccine YF-Vax® package insert, v4, Jan 6 2010.

[45] J. Patrick, M.L. Puterman, M. Queyranne, Dynamic multipriority patient scheduling for a diagnostic resource, Operations Research 56 (6) (2008) 1507–1525.

[46] J.M. Pellissier, P.M. Coplan, L.A. Jackson, J.E. May, The effect of additional shots on the vaccine administration process: results of a time-motion study in 2 settings The American Journal of Managed Care 6 (9) (2000) 1038–1044.

[47] D. Perry, W. Stadje, Perishable inventory systems with impatient demands, Mathematical Methods of Operations Research 50 (1) (1999) 77–90.

[48] W.P. Pierskalla, C.D. Roach, Optimal issuing policies for perishable inventories, Management Science 18 (11) (1972) 603–614.

[49] G.P. Prastacos, Blood inventory management: an overview of theory and practice, Management Science 30 (7) (1984) 777–800.

[50] B. Sivakumar, A perishable inventory system with retrial demands and a <sup>fi</sup>nite population, Journal of Computational and Applied Mathematics 224 (1) (2009) 29–38.

[51] State of Minnesota, Department of Administration, Minnesota Multistate Contracting Alliance for Pharmacy (MMCAP) and Sanofi Pasteur Inc. MMCAP Contract No. MMS27122, Amendment 12, Attachment A, Contract #412365, 1 January 2011 – 30 June 2011, Page 3 of 3.

[52] P. Sun, L. Yang, F. de Vericourt, Sel<sup>fi</sup>sh drug allocation for containing an international in<sup>fl</sup>uenza pandemic at the onset, Operations Research 57 (6) (2009) 1320–1332.

[53] P.G. Szilagyi, M.K. Iwane, S.E. Humiston, S. Schaffer, T. McInerny, L. Shone, J. Jennings, M.L. Washington, B. Schwartz, Time spent by primary care practices on pediatric in-<sup>fl</sup>uenza vaccination visits: implications for universal in<sup>fl</sup>uenza vaccination, Archives of Pediatrics and Adolescent Medicine 157 (2) (2003) 191–195.

[54] M.W. Tanner, L. Ntaimo, IIS branch-and-cut for joint chance-constrained stochastic programs and application to optimal vaccine allocation, European Journal of Operational Research 207 (1) (2010) 290–296.

[55] E. Tekin, Ü. Gürler, E. Berk, Age-based vs. stock level control policies for a perishable inventory system, European Journal of Operational Research 134 (2) (2001) 309–329.

[56] A. Testi, E. Tanfani, R. Valente, M. Fato, I. Porro, A web-based system to manage elective waiting lists: ef<sup>fi</sup>ciency and equity issues, International Journal of Healthcare Technology and Management 10 (4/5) (2009) 277–288.

[57] A. Testi, E. Tanfani, E. Ivaldi, G. Carello, R. Aringhieri, V. Fragnelli (Eds.), Operations research for patient-centered health care delivery, FrancoAngeli, Milano, Italy, 2010.

[58] S. Thompson, M. Nunez, R. Garfinkel, M.D. Dean, Efficient short-term allocation and reallocation of patients to <sup>fl</sup>oors of a hospital during demand surges, Operations Research 57 (2) (2009) 261–273.

[59] M.A. Trick, Formulations and reformulations in integer programming, in: R. Barták, M. Milano (Eds.), Integration of AI and OR techniques in constraint programming for combinatorial optimization problems, Lecture Notes in Computer Science, 3524, Springer, Berlin, 2005, pp. 366–379.

[60] Vaccine Storage and Handling Guide, Department of Health and Human Services, Centers for Disease Control and Prevention, Washington, DC, December 2011.

[61] S. Webster, K.R. Baker, Scheduling groups of jobs on a single machine, Operations Research 43 (4) (1995) 692–703.

[62] J.W. Wells, R.P. Singh, A quality-based inventory issue policy for perishable foods, Journal of Food Processing and Preservation 12 (4) (2007) 271–292.

[63] B.G. Weniger, R.T. Chen, S.H. Jacobson, E.C. Sewell, R. Deuson, J.R. Livengood, W.A. Orenstein. Addressing the challenges to immunization practice with an economic algorithm for vaccine selection, Vaccine 16 (19) (1998) 1885–1897.

[64] C.L. Williams, B.E. Patuwo, A perishable inventory model with positive order lead times, European Journal of Operational Research 116 (2) (1999) 352–373.

[65] World Health Organization (WHO), Vaccine Presentation and Packaging Advisory Group (VPPAG), Vaccine presentation for Pneumococcal vaccines, Available at: http://sites.google.com/site/vppagp/2007. (Accessed on: 24 June 2011).

[66] World Health Organization (WHO), Vaccine Presentation and Packaging Advisory Group (VPPAG), Human Papillomavirus (HPV) vaccine presentation and packaging, Available at: http://sites.google.com/site/vppagp/2008(Accessed on: 24 June 2011).

[67] J.T. Wu, L.M. Wein, A.S. Perelson, Optimization of in<sup>fl</sup>uenza vaccine selection, Operations Research 53 (3) (2005) 456–476.

[68] Y. Xu, B.R. Sarker, Models for a family of products with shelf life, and production and shortage costs in emerging markets. Computers and Operations Research 30 (6) (2003) 925–938.

Alan S. Abrahams is an Assistant Professor in the Department of Business Information Technology, Pamplin College of Business, at Virginia Tech. He received a PhD in Computer Science from the University of Cambridge and holds a BBusSc majoring in Information Systems from the University of Cape Town. He has published in a variety of journals including Expert Systems with Applications, Communications of the AIS, Journal of Computer Information Systems, and Group Decision and Negotiation.

Cliff T. Ragsdale is a Bank of America Professor of Business Information Technology in the Pamplin College of Business at Virginia Tech. He received his PhD in Management Science and Information Technology from the University of Georgia. He also holds an MBA in Finance and a B.A. in Psychology from the University of Central Florida. He has published in a variety of journals including Decision Support Systems, Decision Sciences, Naval Research Logistics, and OMEGA. He is author of the textbook Spreadsheet Modeling and Decision Analysis, 6ed.
