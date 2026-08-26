---
otero_id: 21655
otero_key: "VHGH38GU"
title: "A stochastic study of hidden failures in power system protection"
authors: "Koeunyi Bae; James S Thorp"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00069-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A stochastic study of hidden failures in power system protection

Koeunyi Bae <sup>a,)</sup>, James S. Thorp <sup>b,1</sup>

428 Phillips Hall, School of Electrical Engineering, Cornell UniÕersity, Ithaca, NY 14853, USA

<sup>b</sup> 224 Phillips Hall, School of Electrical Engineering, Cornell UniÕersity, Ithaca, NY 14853, USA

## Abstract

Recent studies have shown that power systems protection mechanisms have played a major role in propagating disturbances. All of the last five major Western Systems Coordinating Council WSCC events the North Ridge earthquake,Ž . Ž December 14, 1994, July 2 and 3, 1996, and August 10, 1996 , involved either false trips of line protection relays or. generator protection equipment. Using an importance sampling based algorithm on the 179-bus WSCC equivalent system, we modeled the sequence of rare events involving generator trips and incorrect zone 3 relay operations. Due to possible loss of generation and load, frequencies were monitored for the necessary of load shedding. The algorithm uses the Newton–Raphson method for accuracy but reverts to DC load flow when the Newton–Raphson algorithm fails to converge within three iterations. The resulting sequence of rare events and its corresponding probability are used to detect weak links in the power system. This information can be beneficial not only in areas such as service and maintenance scheduling and in planning, but also in determining locations where an investment in improving the protection system is warranted. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Power systems relaying; Statistics; Power systems protection; Disturbance propagation; Importance sampling; Rare events; Hidden failures

## 1. Introduction

Recent studies show that power protection system played a significant role not only in possible triggering of the initial event, but in further propagating the disturbances. These types of cascading effects lead to major blackouts. The ability to transfer power reliably through a network is a necessity in order to maintain system security. In a deregulated power system of the future, reliability and security are even more crucial when heavy penalties are attached to failing to maintain a secure network. Hence, there exists a need to study the hidden failures imbedded within the protection system. Hidden failures are the insecure or failed protection system that remains undetected until abnormal operating conditions are reached.

In 1996 alone, the Western Systems Coordinating Council WSCC servicing 59 million people suf-Ž . fered two major blackouts. The WSCC Final Report <sup>w</sup> <sup>x</sup> 10 states that on July 2, parts of the WSCC system were not operating in conditions in compliance with the WSCC Minimum Operating Reliability Criteria. Initiated by a flashover near the Jim Bridger–Kinport 345,000 V line, a protective device operate incorrectly in the Jim Bridger–Goshen 345,000 V line de-energized the line, triggered the remedial action scheme, and led to tripping of two units near the Jim Bridger generating station. Again on July 3, a similar scenario played out. However, the system operators managed to halt the cascading effect. In the WSCC Final Report dated October 1996 9 , the<sup>w</sup> <sup>x</sup> August 10 event, which affected a loss of power to 7.5 million customers, involved a false tripping of the phase imbalance relay on the exciter system and a zone 1 KD relay malfunction. In both the July 2 and August 10, 1996 cases, hidden failures have been blamed for promoting the initial disturbance. The North America Reliability Council report 4<sup>w</sup> <sup>x</sup> supports the assertion that protection systems play a huge role in the sequence of events that lead to power system disturbances.

In spite of its importance, the impact of protection system malfunction on overall system reliability has not been well studied. The existing protection system has multiple overlapping zones of protection. Their bias is toward dependability, even at the cost of global system security. Highly redundant local protection schemes tend to undermine the total system integrity. Siting the 1996 WSCC events as examples once again, virtually all relay misoperations are false trips, which during major system events act to propagate major disturbances.

Simulations to analyze such cascading scenarios can be daunting. The obvious problem arises from the fact that such rare cases are difficult to capture in large but limited databases. Even though thousands of load flows or transient stability cases can be involved in a database, the probability of major disturbances are so small that they cannot reasonably be included by conventional techniques. The North American Electric Reliability Council NERC re- Ž . ports make it obvious that major disturbances typically involve a string of six to seven unlikely events. Since simulation studies which capture a number of low probability events are difficult to perform, and the exact probability of the various unlikely events are not known, only few attempt has been made to model the temporal spreading of the disturbance. Recent studies 3,5–8 use importance sampling to <sup>w</sup> <sup>x</sup> alleviate the difficulty of simulating rare events. The simulations are performed with altered probabilities, which make the unlikely events more likely and processing the simulation results so that the correct answers are obtained. An importance sampling-based algorithm can be used to investigate where in the system changes in the protection mechanism would be most effective, and then evaluate the increase in reliability obtained from monitoring the protection system.

Importance sampling is critical to the success of studying hidden failures imbedded in the power system. In the wake of the summer of 1996 events, reliability of the protection system is an issue. It is our contention that study of hidden failures using importance sampling would determine the place in the bulk power system most sensitive to incorrect operations. Not only will this information be crucial for scheduling of maintenance and service, this information can also be used during the initial planning stages to better optimize the system network.

## 2. Methodology

Two types of hidden failures in the relays will be the focus of the study. The first involves the third zone relays protection of transmission line. After reviewing the WSCC events, a second type of hidden failure was added to the list: voltage-based hidden failures triggered by low voltage conditions.

## 2.1. Line protection hidden failures

In Refs. 5,8 , if any line sharing a bus with a<sup>w</sup> <sup>x</sup> transmission line L trips, then hidden failures in line L are exposed. If one line trips correctly, then all the lines connected to its ends are exposed to the incorrect tripping. The recent WSCC events show that although such incorrect relay operations are rare, they do occur.

Consider a fictitious model with some initial load flow shown in Fig. 1. If line 2 trips legitimately, then it exposes lines 1, 4, 9 and 19. The rest of the lines are not effected since they are not connected to bus A or E. The 16 possible outcomes at this step are as follows:

<sup>Ø</sup> one possible way of zero incorrect operations;

<sup>Ø</sup> four possible ways of a single line incorrect operations;

<sup>Ø</sup> six possible ways of two line incorrect operations;

<sup>Ø</sup> four possible ways for a three line incorrect operations; and

<sup>Ø</sup> one possible way for all four lines to incorrect operations.

For illustration purposes, if the probability of an exposed line tripping is taken as p then probability of it not tripping is $q = 1 - p .$ Hence, there is a probability $p ^ { 4 }$ that all four lines succumb to the hidden failure and trip incorrectly, $4 p q ^ { 3 }$ that a single line trips incorrectly, $6 p ^ { 2 } q ^ { 2 }$ that two lines misoperate, $4 p ^ { 3 } q$ that three lines trip, and $q ^ { 4 }$ that all four relays operate correctly. Reverting back to Fig. 1, line 9 operates incorrectly and exposes lines 1, 10, 11, and 19. Suppose lines 10 and 11 trip, then additional lines 7, 12, 13, and 14 are exposed leaving bus C is isolated.

In a real power system, isolation of a bus such as C could mean loss of generation or load. This causes a mismatch to develop between the generation and the demand section of the power system. It is crucial that frequency decay of the power system is halted before further damage to turbine blades or auxiliary systems can occur. Hence, underfrequency relays are employed to detect the onset of frequency decay and to maintain a balance between load and generation. The frequency monitoring and the associated load shedding techniques are well documented in Ref. 2 .<sup>w</sup> <sup>x</sup>

The bulk power system is usually split into smaller sections. Each one of these regions tracks its own frequency and performs individual load shedding. Though the real WSCC are split into many regions, for our study, the 179-bus equivalent will be only broken into four sections. They are as follows:

<sup>Ø</sup> Canada, Washington, Oregon, Idaho

<sup>Ø</sup> Northern California

<sup>Ø</sup> Southern California

<sup>Ø</sup> Nevada, Utah, Arizona, Wyoming, New Mexico The four regions will monitor frequency separately and shed load accordingly. Loss of 300 MW load for any region is the definition of NERC disturbance used in our experiment.

## 2.2. Voltage-based hidden failures

In the July 2 and 3 and August 10, 1996 events, low voltage conditions led the exciter to believe in the existence of an imbalance in the SCR bridge circuit. The relay operated incorrectly and took action to avoid damage. The generator tripped unnecessarily. Therefore, we include the rare voltage based hidden failures in our study.

Suppose a generator bus voltage violates

$$
\left| V _ {\mathrm{min}} \right| \leq \left| V \right| \leq \left| V _ {\mathrm{max}} \right|\tag{1}
$$

and there exists inadequate VAR support, then the protection system is again exposed to hidden failures. If the relay operates incorrectly at that bus and the generator trips, then all lines connected to that bus would also be exposed to hidden failures.

In Fig. 2, another fictitious model, a legitimate relay operation on line 2, which exposes lines 1, 4, 9, and 19. Line 9 operates incorrectly leaving hidden failures in lines 1, 10, 11, and 19. Suppose line 10 trips and at the same time the generator at bus H trips due to the low voltage plus inadequate VAR combination. This exposes lines 7, 11, 12, 13, and 14. Tripping of lines 13 and 14 exposes lines 7, 11, 12, and 17. The voltage based hidden failure gives another point for an initial disturbance perhaps even accelerating the cascading behavior.

## 3. Importance sampling

Given $\{ x _ { i } \}$ are identically distributed Bernoulli random variables with

$$
P \{x _ {i} = 1 \} = \rho = 1 - P \{x _ {i} = 0 \}\tag{2}
$$

where $P \{ x _ { i } = 1 \}$ is the probability of the event occurring and $P \{ x _ { i } = 0 \}$ is the probability of an event not occurring, we will estimate $\rho$ with at most 20% error with 95% confidence. We want to estimate $\hat { \rho }$

$$
\hat {\rho} = \frac {1}{N} \sum_ {i} ^ {N} x _ {i}\tag{3}
$$

to be such that

$$
P \left\{\mid \rho - \hat {\rho} \mid \leq 0. 2 \rho \right\} \geq 0. 9 5\tag{4}
$$

where N is the number of observations of the random variable $x _ { i }$ . For example, $x _ { i } = 1$ could correspond to a line being in operation while $x _ { i } = 0$ could refer to the line being tripped. In Ref. 9 , the <sup>w</sup> <sup>x</sup> estimate of N is found to be

$$
N = \frac {1 0 0}{\rho}.\tag{5}
$$

Hence if $\rho$ is on the order of $1 0 ^ { - 6 }$ , we would need $1 0 ^ { 8 }$ number of samples to simulate the cascading outages.

![](/api/attachments/VHGH38GU/fulltext/images/f54f72e8ff37e1b0991ca5da2c86b09791d688ef0ef9fc35d5f8a732f9e2e410.jpg)

![](/api/attachments/VHGH38GU/fulltext/images/0d4503420752f497f6b41b7bc1058027174a69cb02e5f2ace54b9ef329fb6f39.jpg)  
Fig. 2

Each simulation requires a random number draw putting the long-term behavior of the random number generator under scrutiny. It is clear that such long term simulation would require an unrealistically large amount of computation time and demands the impossible for the random number generator.

Importance sampling enables the simulation to be run with altered probabilities so that the rare events occur more frequently. Upon re-examining the sequence of events in Fig. 1, after the original flashover of line 2, misoperation at line 9, and another misop eration at lines 10 and 11, bus C becomes isolated. Suppose the loss of this particular bus pushes the system into the blackout situation. This bus then would be recorded by the conventional method as a 1. The number of 1’s in N simulations divided by N is the estimate of the probability of a cascading failure. In importance sampling rather than using the actual probabilities $p$ and $q ,$ the simulations use the altered probabilities $p p$ and qq. Rather than recording the number of $\mathbf { l } ^ { \prime } \mathbf { s } ,$ we record a number t, a ratio of actual probability of the event divided by the probabilities used in the simulation, computed as the simulation progresses. For the event described,

$$
t = \left(\frac {p}{p p}\right) \left(\frac {q}{q q}\right) ^ {3} \left(\frac {p}{p p}\right) ^ {2} \left(\frac {q}{q q}\right) ^ {2}\tag{6}
$$

The actual probability of the event is $p ^ { 3 } q ^ { 4 }$ while the probability that the event occurs in the simulation is ${ \bar { p } } p ^ { 3 } q q ^ { 4 }$ . The following forms the estimate of the probability:

$$
\hat {\rho} = \frac {1}{N} \sum_ {i} ^ {N} t _ {i}\tag{7}
$$

and will have the correct mean even if N is smaller than the $1 0 0 / \rho$ estimate.

More generally, each line will have a different probability of tripping incorrectly as shown in Fig. 3. The model shows the probability of the exposed line tripping incorrectly as a function of impedance seen by the relay. The value of three times the zone impedance setting is chosen. We will calculate the zone three impedance as 250% of the line impedance. Dependence on the current system condition implies that impedance must be calculated after each computation.

![](/api/attachments/VHGH38GU/fulltext/images/223694f65d58f5f9800701838a5ade4b43ea4d268b26f4eb4f0610b34b6cee47.jpg)  
Fig. 3. Probability of exposed line tripping incorrectly.

Fig. 4 shows the probability of incorrect generator tripping as a function of reactive power. When the voltage is maintained within operating range, the probability of false trip is negligible. However, once outside that range, misoperations can occur. For our calculation purposes, we will gauge the misoperation using VAR support. If

$$
| Q _ {\mathrm{min}} | \leq | Q | \leq | Q _ {\mathrm{max}} |\tag{8}
$$

is violated for any generator bus then operating voltage conditions cannot be met. Hence, the generators are exposed to false trips. Again, the voltage must be recomputed at each stage.

## 3.1. Importance sampling Õariation

As explained in Ref. 8 , the following variation<sup>w</sup> <sup>x</sup> on importance sampling was incorporated into the algorithm. The numerator in Eq. 6 is the actualŽ . probability of the sample path of sequences of line outages. Rather than accumulate the weighted probabilities as in Eq. 7 , we can record the distinctŽ . sample paths exposed in the simulation using pp probabilities along with the actual probabilities and then sum the probabilities. If the number of simulations is large enough to produce the significant sample paths, then the sum is a tight lower bound to the actual probability of failure. Although the choice of the simulation probabilities is less critical than the direct importance sampling, some variation in the typical sample paths are observed as the rule for generating the $p p ^ { \prime } \mathbf { s }$ is changed. If all exposed lines are given the same probability say 1 Ž . <sup>r</sup>2 then the resulting sample paths are somewhat different than those obtained when the exposed probabilities are simply scaled so the largest is $1 / 2 .$ . A solution is to randomize the rule for generating the simulation probabilities. If $p _ { j }$ represents the actual probability among the exposed lines, then

![](/api/attachments/VHGH38GU/fulltext/images/ef80e1bfdf9889dcd4d278f9400e1841a32643aad5aacc709acb31ad786dda81.jpg)  
Fig. 4. Probability of generator tripping incorrectly.

$$
p p _ {j} = 0. 5 \left(\frac {p _ {j}}{p _ {\mathrm{max}}}\right) ^ {\mu_ {j}}\tag{9}
$$

where $\mu _ { j } ^ { \mathrm { ~ , ~ } } \mathrm { { s } }$ are uniform random variables in the interval 0 to 1. The value $\mu _ { j } = 1$ corresponds to uniform scaling while a value of 0 corresponds to setting all the values to $1 / 2$ . Since the $\mu _ { j } ^ { \mathrm { ~ , ~ } } \mathrm { { s } }$ are chosen at each step, all combinations are exposed.

## 4. The algorithm

For the following simulations, we use a definition of major disturbance given by NERC to determine the termination of the cascading effect. The loss of 300 MW or more load in any of the four sections of the WSCC equivalent model qualifies the system to be in a state of a blackout.

Initially the simulation begins from a base load flow. A line is selected as the triggering event and the following algorithm is repeated N times.

1. Determine all the lines that tripped in the last iteration.

2. Determine all lines connected to the buses of step 1. These are the exposed lines.

3. Check for violations in VAR constraints and find the probability of generator tripping using Fig. 4.

4. If generator protection operates incorrectly, add all lines connected to the bus to the list of exposed lines.

5. Check the frequency of the regions and shed load to maintain system balance.

6. Compute the load flow using the Newton–Raphson method. If it fails to converge within three iterations, use DC load flow.

7. Recompute the impedance seen by relays for exposed lines.

8. Find the probability of tripping for each exposed line using Fig. 3.

9. For the exposed line record, $t _ { i } = \Pi _ { i } p _ { j } \Pi _ { k } ( 1 -$ $p _ { k } )$ where j are all lines that tripped and k all lines that did not trip.

10. Record all the lines that tripped.

11. Go to step 1 if any lines tripped and each region are within the 300 MW load loss. Continue until no lines are lost or experience a blackout.

12. If the system fails, determine if $t = \prod _ { i } t _ { i }$ is a new number or a new sequence of line outages. If so record it.

## 5. WSCC 179-bus equivalent system

The 179-bus WSCC system has 29 generators and 203 transmission lines. The initial load flow data is based on the December 12, 1994 conditions. We chose this particular system rather than a fictional one i.e., New England 39 bus for the sole purposeŽ . of testing if the algorithm can pinpoint any weaknesses in a real system.

For each simulation, a single transmission line, $l ^ { \mathrm { o } } ,$ acts as the initial triggering event. All exposed lines associated with this event have different probabilities of tripping incorrectly as shown in Fig. 3. Probability of a generator tripping is according to Fig. 4. In both, maximum probability of a hidden failure is set at and is the number of iteration per simulation. Each iteration is terminated when load shedding exceeds 300 MW.

## 5.1. Simulation results

For each initial line out, we obtain a table of sequence of line outages and the probability associated with that sequence. Table 1 shows simulation results for initial triggering event of l <sup>o s</sup> 200, a transmission line between BenLomnd UT and Mid-Ž . Ž . <sup>o</sup> point ID . For any initial event, l , we generate M

Table 1 Sequence of events for initial failure at line 200

<table><tr><td colspan="19">Lines out</td><td>Probability</td></tr><tr><td>1</td><td>4</td><td>154</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td></td></tr><tr><td>1</td><td>4</td><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>202</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>4</td><td>154</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>202</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>4</td><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>155</td><td>156</td><td>157</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>4</td><td>154</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td></td></tr><tr><td>154</td><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>156</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>163</td><td>164</td><td>165</td><td>166</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>155</td><td>156</td><td>157</td><td>158</td><td>160</td><td>161</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>154</td><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>163</td><td>164</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>155</td><td>156</td><td>158</td><td>160</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>163</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>4</td><td>155</td><td>156</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>165</td><td>166</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>156</td><td>157</td><td>158</td><td>159</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>4</td><td>156</td><td>157</td><td>158</td><td>160</td><td>161</td><td>162</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>164</td><td>165</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>164</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>155</td><td>156</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>164</td><td>165</td><td>166</td><td>200</td><td>201</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>156</td><td>157</td><td>158</td><td>159</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>166</td><td>168</td><td>200</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>163</td><td>164</td><td>166</td><td>168</td><td>200</td><td>201</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>162</td><td>164</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>155</td><td>156</td><td>158</td><td>159</td><td>160</td><td>162</td><td>163</td><td>165</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>4</td><td>156</td><td>157</td><td>159</td><td>160</td><td>162</td><td>163</td><td>164</td><td>166</td><td>168</td><td>200</td><td>201</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>156</td><td>158</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>165</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>154</td><td>156</td><td>157</td><td>158</td><td>160</td><td>161</td><td>162</td><td>164</td><td>166</td><td>168</td><td>200</td><td>201</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>154</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>1</td><td>155</td><td>156</td><td>157</td><td>158</td><td>160</td><td>161</td><td>162</td><td>166</td><td>168</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>154</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>165</td><td>166</td><td>200</td><td>201</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>154</td><td>155</td><td>156</td><td>157</td><td>158</td><td>160</td><td>161</td><td>162</td><td>163</td><td>168</td><td>200</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $2.00 \times 10^{-12}$ </td><td></td></tr><tr><td>1</td><td>154</td><td>155</td><td>156</td><td>157</td><td>160</td><td>161</td><td>162</td><td>163</td><td>165</td><td>166</td><td>200</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $3.00 \times 10^{-12}$ </td><td></td></tr><tr><td>1</td><td>154</td><td>156</td><td>157</td><td>158</td><td>160</td><td>161</td><td>162</td><td>163</td><td>168</td><td>200</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $3.00 \times 10^{-12}$ </td><td></td></tr><tr><td>154</td><td>155</td><td>156</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>168</td><td>200</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $5.00 \times 10^{-12}$ </td><td></td></tr><tr><td>1</td><td>156</td><td>157</td><td>160</td><td>161</td><td>162</td><td>163</td><td>166</td><td>168</td><td>200</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $1.40 \times 10^{-11}$ </td><td></td></tr><tr><td>155</td><td>156</td><td>157</td><td>158</td><td>160</td><td>161</td><td>162</td><td>165</td><td>168</td><td>200</td><td>201</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $1.90 \times 10^{-11}$ </td><td></td></tr><tr><td>154</td><td>156</td><td>158</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>168</td><td>200</td><td>201</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $2.80 \times 10^{-11}$ </td><td></td></tr><tr><td>154</td><td>155</td><td>156</td><td>157</td><td>158</td><td>159</td><td>160</td><td>164</td><td>168</td><td>200</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $2.80 \times 10^{-11}$ </td><td></td></tr><tr><td>155</td><td>156</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>164</td><td>168</td><td>200</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $1.67 \times 10^{-10}$ </td><td></td></tr><tr><td>154</td><td>156</td><td>157</td><td>158</td><td>161</td><td>162</td><td>165</td><td>168</td><td>200</td><td>202</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $3.49 \times 10^{-10}$ </td><td></td></tr><tr><td>154</td><td>155</td><td>156</td><td>157</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>200</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $4.30 \times 10^{-10}$ </td><td></td></tr><tr><td>154</td><td>155</td><td>156</td><td>157</td><td>158</td><td>160</td><td>161</td><td>162</td><td>200</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $2.80 \times 10^{-9}$ </td><td></td></tr><tr><td>154</td><td>156</td><td>159</td><td>160</td><td>161</td><td>162</td><td>163</td><td>168</td><td>200</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $3.80 \times 10^{-9}$ </td><td></td></tr></table>

different sequences. In this case, 59 distinct sequences were recorded. Note however, that events involving the same lines but tripping in a different order will have distinct probabilities. Out of these $M = 5 9$ lines, only $\hat { M }$ contribute significantly to the total probability $( \mathrm { i . e . }$ , sum of probability of all se-. quences . For $l ^ { \mathrm { o } } = 2 0 0 .$ , only 13 cases exhibit substantial probabilities. The other $M { - } \hat { M }$ sequences contain one of the $\hat { M }$ sequences as its subset. Therefore, we can justify using only the $\hat { M }$ sequences in evaluating the weaknesses in the system. Note: by the past definition of a major disturbance used in Ref. 1 the isolation of a node during a sequence of<sup>w</sup> <sup>x</sup> Ž relay misoperations , the sequence of lines tend to be. short. Most notably, very few sequences in the $\hat { M }$ set contained the long string of six or seven events. By <sub>using one of the NERC definition of a blackout, M</sub>ˆ shown in Table 1 contains longer strings of events. The event with the largest probability contains nine transmission lines with a probability of occurrence at $\hat { \rho } = 3 . 8 \times 1 0 ^ { - 9 }$ for initial probability of $p = 0 . 0 5$ The longest sequence and one with the lowest probability involves 18 transmission lines.

If total probability of sequence of events for initial line outage of $l ^ { \mathrm { o } }$ is

$$
p ^ {l ^ {\mathrm{o}}} = \sum_ {\forall i} p _ {i} ^ {l ^ {\mathrm{o}}}\tag{10}
$$

where i is the ith sample path of total M, then the probability of line $k ' s$ contribution to the major disturbance for $l ^ { \mathrm { o } }$ is

$$
p ^ {(k | l ^ {\mathrm{o}})} = \sum_ {k \in i} p _ {i} ^ {l ^ {\mathrm{o}}} \approx \sum_ {k \in m} p _ {i} ^ {l ^ {\mathrm{o}}}\tag{11}
$$

where $m \in { \hat { M } }$ is the list of sequences that contribute significantly to the total probability.

When the initial line outage, $l ^ { \mathrm { o } } ,$ is plotted vs. probability of subsequent tripped lines i.e., line Ž k <sup>o</sup> given l ., few lines stand out. If the system has a narrow banded adjacency matrix, then most of the

![](/api/attachments/VHGH38GU/fulltext/images/a8c8615d78e9463bc642e499cbb65ce78df08b9324ebef6573e2ded3b288bacc.jpg)  
Fig. 5. WSCC 179-bus system. The right hand axis denotes the initial line out number. The left-hand axis marks the subsequent tripped lines. The z-axis denotes the corresponding probability.

Table 2  
List of transmission lines with the highest probability of hidden failures

<table><tr><td>Initial line</td><td>Subsequent line</td><td>Bus to</td><td>Bus from</td><td>Probability</td><td>Regions</td></tr><tr><td>94</td><td>94</td><td>Burns</td><td>Burns</td><td>0.0003</td><td>SE Oregon</td></tr><tr><td>94</td><td>198</td><td>Burns</td><td>Burns2</td><td>0.0003</td><td>SE Oregon</td></tr><tr><td>94</td><td>199</td><td>Burns2</td><td>Summer L</td><td>0.0003</td><td>SE Oregon</td></tr><tr><td>94</td><td>80</td><td>Grizzly2</td><td>Summer L</td><td>0.0002</td><td>SE Oregon</td></tr><tr><td>94</td><td>83</td><td>Malin2</td><td>Summer L</td><td>0.0002</td><td>SE Oregon</td></tr><tr><td>13</td><td>13</td><td>Moenkop2</td><td>Westwing</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>13</td><td>17</td><td>Palovrd</td><td>Westwing</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>21</td><td>7</td><td>Navajo2</td><td>Moenkopi</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>21</td><td>11</td><td>Moenkopi</td><td>Moenkop1</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>21</td><td>14</td><td>Moenkopi</td><td>Moenkop3</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>21</td><td>21</td><td>Fourcor2</td><td>Moenkopi</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>107</td><td>104</td><td>Round Mt</td><td>Round1</td><td>0.0002</td><td>California</td></tr><tr><td>107</td><td>107</td><td>Table Mt</td><td>Round2</td><td>0.0002</td><td>California</td></tr><tr><td>107</td><td>173</td><td>Malin4</td><td>Round Mt</td><td>0.0002</td><td>California</td></tr><tr><td>107</td><td>176</td><td>Malin</td><td>Round Mt</td><td>0.0002</td><td>California</td></tr><tr><td>109</td><td>106</td><td>Round2</td><td>Table Mt</td><td>0.0002</td><td>California</td></tr><tr><td>109</td><td>109</td><td>Round3</td><td>Round4</td><td>0.0002</td><td>California</td></tr><tr><td>109</td><td>110</td><td>Table Mt</td><td>Table1</td><td>0.0002</td><td>California</td></tr><tr><td>109</td><td>113</td><td>Table Mt</td><td>Table</td><td>0.0002</td><td>California</td></tr><tr><td>11</td><td>7</td><td>Navajo2</td><td>Moenkopi</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>11</td><td>11</td><td>Moenkopi</td><td>Moenkop1</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>11</td><td>14</td><td>Moenkopi</td><td>Moenkop3</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>11</td><td>21</td><td>Fourcor2</td><td>Moenkopi</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>13</td><td>196</td><td>Palovrd</td><td>Devers</td><td>0.0002</td><td>NE Arizona</td></tr><tr><td>13</td><td>18</td><td>Palovrd</td><td>Westwing</td><td>0.0002</td><td>NE Arizona</td></tr></table>

activity occurs along the diagonal. In a real power system, no matter how clever the labeling, it is highly unlikely that a tightly banded adjacency matrix exist.

For the 179-bus WSCC system in Fig. 5, there are clusters of high peaks around the diagonal with several off diagonal sharp peaks. These are the ‘weak’ lines in the system since they are more prone to contribute to a blackout event. This figure shows that the 179-bus system contains single contingency cases with high probability and lengthy chains of Ž <sup>o</sup> misoperations see l around 1–20, 100, 150, and 200 . Also viewing the graph from the tripped lines . perspective, those same areas show weakness. This implies that certain transmission lines are effected by a large number of initiating events. For those reasons, the WSCC system contains several weak links that tend to propagate the initial disturbance.

Table 2 is a list of the highest likelihood cases and the corresponding transmission line names involved in a blackout event. The transmission line between Burns and Burns1 located in southeastern Oregon has the highest probability of being part of a disaster. Each of the four frequency regions was represented in this high probability list. This implies that this experiment, with 300 MW load loss being the blackout definition and the division of WSCC into only four regions, shows frail links in southeastern Oregon, California, and northeastern Arizona<sup>r</sup> northwestern New Mexico.

## 6. Conclusion

By incorporating an importance sampling based algorithm, this study of cascading protection system failures hopes to illustrate weaknesses in the power system. By monitoring the frequency deviations which enables load shedding and using a NERC definition of a blackout, the study shows that WSCC 179-bus system on December 12, 1994 shows signs of weak links in southeastern Oregon.

## 7. Symbols and units

$p$ Probability of exposed line tripping; actual probability of an exposed line tripping

$q$ Probability of exposed line not tripping; actual probability of an exposed line not tripping

$\rho$ Probability of an event occurring $\hat { \rho }$ Estimate of $\rho$

$p p$ Altered probability of exposed line tripping

$q q$ Altered probability of exposed line not tripping

$V$ Generator bus voltage

$V _ { \mathrm { m i n } }$ Generator bus voltage minimum

$V _ { \mathrm { m a x } }$ Generator bus voltage maximum

$N$ Number of iterations of simulation

$Q$ VAR support

$Q _ { \mathrm { m i n } }$ Minimum VAR support

$Q _ { \mathrm { m a x } }$ Maximum VAR support

$M$ Number of distinct sequences of lines failures

$\hat { M }$ Subset of M containing majority of probability

$l ^ { \mathrm { o } }$ Initiating line trip

$p ^ { l ^ { \mathrm { { o } } } }$ Probability of sequence of events for initial line out of $l ^ { \mathrm { o } }$

$p ^ { ( k | l ^ { \mathrm { o } } ) }$ Probability of line $K \ ' s$ likelihood of being involved in a major disturbance given $l ^ { \mathrm { o } }$

## Acknowledgements

This work was conducted under the NSF grant number ECS-9634823.

## References

<sup>w</sup> <sup>x</sup> 1 K. Bae, J.S. Thorp, An importance sampling application: 179-bus WSCC system under voltage based hidden failures

and relay misoperations, Proceedings of the Thirty-first Hawaii International Conference on System Sciences, Vol. 3, 1998.

<sup>w</sup> <sup>x</sup> 2 S.H. Horowitz, A.G. Phadke, Power System Relaying, Research Studies Press, Somerset, England, 1992.

<sup>w</sup> <sup>x</sup> 3 S.H. Horowitz, A.G. Phadke, J.S. Thorp, The role of adaptive protection in mitigating system blackouts, 1995 CIGRE SC 34 Colloquium, Stockholm, 11–17 June 1995.

4 NERC Disturbance Reports, North American Electric Reliability Council, NJ, 1984–1988.

<sup>w</sup> <sup>x</sup> 5 C. Tamronglak, A.G. Phadke, S.H. Horowitz, J.S. Thorp, Anatomy of power system blackouts: preventive relaying strategies, ’95 WM 032-3-PWRD, IEEE Winter Meeting, Feb. 1995.

<sup>w</sup> <sup>x</sup> 6 C. Tamronglak, S.H. Horowitz, A.G. Phadke, J.S. Thorp, Anatomy of power system blackouts: preventive relaying strategies, IEEE Transactions on Power Delivery 11 2Ž . Ž .1996 708–715.

<sup>w</sup> <sup>x</sup> 7 J.S. Thorp, A.G. Phadke, Expose hidden failures to prevent cascading outages, IEEE Computer Applications in Power 9 Ž . Ž .3 1996 20–23.

<sup>w</sup> <sup>x</sup> 8 J.S. Thorp, A.G. Phadke, S.H. Horowitz, C. Tamronglak, Anatomy of Power System Disturbances: Importance Sampling, PSCC, Dresden, Aug. 1996.

<sup>w</sup> <sup>x</sup> 9 Western Systems Coordinating Council Final Report, 2 and 3 July event, 19 September 1996.

<sup>w</sup> <sup>x</sup> 10 Western Systems Coordinating Council Final Report, 10 August 1996 event, October 1996.

Koeunyi Bae is currently enrolled in the PhD program in Electrical Engineering at Cornell University in Ithaca, NY. She received her BSEE and Master of Engineering EE in 1994 and 1995 from Cornell. Her research interests include power systems protection and nonlinear dynamical systems.

James S. Thorp F, 1989 received the BEE, MS, and PhD degreesŽ . from Cornell University, Ithaca, NY. He joined the faculty of Cornell in 1962, where he is currently a Professor and Director of the School of Electrical Engineering. In 1976, he was the Faculty Intern at the American Electric Power Service. He was an associate editor for the IEEE Transactions on Circuits and Systems from 1985 to 1987. In 1988, he was an Overseas Fellow at the Churchill College, Cambridge, England. He is a member of the IEEE Power Systems Relaying Committee, CIGRE, Eta Kappa Nu, Tau Beta Pi, and Sigma Xi.
