---
otero_id: 218
otero_key: "U6PRRDUT"
title: "Genetic programming for prevention of cyberterrorism through dynamic and evolving intrusion detection"
authors: "James V. Hansen; Paul Benjamin Lowry; Rayman D. Meservy; Daniel M. McDonald"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.04.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Genetic programming for prevention of cyberterrorism through dynamic and evolving intrusion detection

James V. Hansen <sup>a,⁎</sup>, Paul Benjamin Lowry <sup>a</sup>, Rayman D. Meservy <sup>a</sup>, Daniel M. McDonald <sup>b</sup>

<sup>a</sup> Information Systems Department, Kevin and Debra Rollins Center for e-Business, Marriott School of Management, Brigham Young University, United States

<sup>b</sup> Artificial Intelligence Lab, Department of Management Information Systems, University of Arizona, United States

Available online 6 June 2006

## Abstract

Because malicious intrusions into critical information infrastructures are essential to the success of cyberterrorists, effective intrusion detection is also essential for defending such infrastructures. Cyberterrorism thrives on the development of new technologies; and, in response, intrusion detection methods must be robust and adaptive, as well as efficient. We hypothesize that genetic programming algorithms can aid in this endeavor. To investigate this proposition, we conducted an experiment using a very large dataset from the 1999 Knowledge Discovery in Database (KDD) Cup data, supplied by the Defense Advanced Research Projects Agency (DARPA) and MIT's Lincoln Laboratories. Using machine-coded linear genomes and a homologous crossover operator in genetic programming, promising results were achieved in detecting malicious intrusions. The resulting programs execute in real time, and high levels of accuracy were realized in identifying both positive and negative instances. © 2006 Elsevier B.V. All rights reserved.

Keywords: Cyberterrorism; Genetic programming; Homologous crossover; Intrusion detection; Pattern recognition; Information security

## 1. Introduction

Electronic business (e-business) and electronic government (e-government) transacted over the Internet are revolutionizing the ways in which business and government are conducted. Using the Internet as a medium for managing transactions enhances accessibility to a wide variety of information and services. Consequently, many organizations are able to leverage critical operations through Internet-based electronic processes. This is evidenced partly by the increasing number of resources that are procured, managed, created, and consumed over the Internet, intranets, and extranets.

At the same time, modern Internet-based computer systems are increasingly vulnerable to malicious intrusions because of the high interconnectivity among systems worldwide [3]. This interconnectivity extends from private to public sectors with no respect to borders, which makes it difficult to assign responsibility and accountability for intrusion prevention [10]. Deficiencies in computer security can allow intrusions that lead to loss of physical assets, digital assets, money, consumer confidence, national security, and even life. Such intrusions can take the form of disruptions of critical service, exploitations (e.g., identity theft, credit card theft, theft of strategic information, misinformation, misuse of control systems that manage physical infrastructure such as air traffic and dams, or creation of terror for coercive purposes), and destruction of information [10].

With the advent of cyberterrorism, systems are now subject to even more daunting threats [10,48]. Cyberterrorism is a form of politically motivated terrorism that uses information, computers, networks, and technical infrastructure to conduct destructive or malicious terrorist activities [45,48]. Because of the importance of these Internetworking components, some experts argue that cyberterrorism is potentially more damaging than traditional terrorism [45]. In particular, cyberterrorists are likely to target financial and commercial infrastructure as well as infrastructure involved with government records, dam control, air traffic control, and medical records.

Because of these and similar threats, computer system security is a growing concern [45] for consumers, system administrators, business owners, and government leaders. The security community has responded by providing a stream of new security methodologies. For example, Internet-related security risks can be mitigated by implementing recent developments that enhance authentication, nonrepudiation, confidentiality, privacy protection, and data integrity [46]. These achievements are due in part to technological advances in areas such as public and private data encryption, trusted third-party digital certificates, firewalls, passwords, confirmation services, software patches, cryptographic algorithms, and biometrics.

Nonetheless, these developments may not sufficiently meet the challenge of establishing necessary security against cyberterrorism threats. Recent studies suggest that traditional approaches to identifying and correcting security flaws are unlikely to succeed because they are grounded in a view of computers as static systems, as opposed to their true dynamic nature [13,21,41]. Specifically, limitations of existing approaches to computer security are reflected in part by an increasing level of human involvement in computer and network maintenance due to security issues. This involvement is inefficient and may be hard to sustain, which motivates a need for computer systems to be self-corrective and selfmaintaining [4].

## 2. Motivation

Although it is true that intrusion detection techniques apply to broader circumstances than cyberterrorism, it is vital that the discussion of prevention of cyberterrorism include intrusion detection as a core remedy. Unpredictable intrusion is a key tool that cyberterrorists can wield to disrupt systems, steal information, destroy or alter information, create false identities, or even alter processes in a way to cause threat to human life (e.g., air traffic control, nuclear power plant control, traffic control).

An ideal defense is a set of foolproof preventative roadblocks that prevent cyberterrorists from breaching security. Although this idea is fundamental, foolproof systems are virtually impossible to design because of the complexities of distinguishing between false-positives and true-positives. Moreover, the underlying cost– benefit calculus is difficult to compute and may vary from one organization to another.

This is not to suggest that preventative mechanisms are not useful; rather, that they must be adjusted for the level of risk that an organization is willing to bear in light of the threat of cyberterrorism. Thus, cyberterrorism prevention may require accepting a higher level of cost associated with investigating false-positives to increase the percentage of identified true positives.

With these issues as a foundation, this paper investigates the potential of genetic programming (GP) as an adaptive method of responding to the complexities of cyberterrorist intrusion detection. We focus on GP because two research studies have indicated its strong potential for intrusion detection in highly complex, dynamic, and distributed environments posed by cyberterrorism: Crosbie and Spafford [9] completed a seminal study investigating GP as intrusion-detection tool in a distributed computing environment. GP was found to be computationally efficient and robust, while yielding immediately deployable programs as output. More recently, Lu and Traore [31] investigate the capability of GP to identify novel intrusion signatures.

Our research differentiates from these studies in its focus on three important needs pertinent to cyberterrorist intrusion detection: First, the potential costs to society underscore the desirability of a high-level of accuracy in identifying true positives. Second, it would be advantageous if this objective can be accomplished without incurring a costly number of false positives. Third, the high performance objectives must be met in an adaptable manner to keep pace with the changing strategies of cyberterrorists. Recent developments in GP, which include increased speed through use of linear genomes constructed of machine code instructions and the development of homologous crossover operators, motivate a study of these issues. In theory, these enhancements should improve the adaptability and robustness of GP algorithms.

The remainder of the paper proceeds as follows: The following section provides a review of related work on cyberterrorism and intrusion detection. We then provide more detail on the our study's inspiration, which is followed by an overview of the GP algorithm and GP crossover operators that are pertinent to this study. This discussion is followed by a description and analysis of a large-scale experiment that examines the use of GP for the detection of multiple intrusion events. We close by offering concluding remarks on the contributions, limitations, and future directions of this research.

## 3. Related work

## 3.1. Cyberterrorism

Although cyberterrorists may use traditional “hacking” techniques, they do not behave like common hackers whose intentions may vary from the benign to the catastrophic. “Like other terrorist acts, cyberterrorist attacks are typically premeditated, politically motivated, perpetrated by small groups rather than governments, and designed to call attention to a cause, spread fear, or otherwise influence the public and decision-makers” [45] p. 2. Cyberterrorism is an increasingly attractive choice for terrorists because it can be accomplished with only modest financial resources, with anonymity, and from a great distance [45]. Moreover, cyberterrorism has its greatest potential for damage in conjunction with coordinated physical attacks: “For example, they might try to block emergency communications or cut off electricity or water in the wake of a conventional bombing or a biological, chemical, or radiation attack” [45] p. 2.

The primary weapons of cyberterrorists are traditional and modified versions of common intrusion techniques. Techniques for cyber warfare are dynamic and difficult to predict, whether they use identity theft, redirection and spoofing, data sniffing and interception, logic bombs, e-mail bombs, viruses, parasites, worms, Trojan horses, false identities, guessing passwords, back doors, denial-of-service attacks, stealing classified files, disseminating false information, etc. [45].

Whereas hackers and abusers of information systems have been security threats for decades, the advent of cyberterrorism and related research is relatively new. Recent overviews of cyberterrorism are included in [1,8,17,27,30,36,40]. Recent notable research projects that focus on cyberterrorism prevention have studied the use of support vector machines for terrorism information extraction [44], the identification of authorship for cybercrimes [51], a collaborative decision-making framework to address homeland security [37], and a terrorism knowledge-discovery project [38]. Yet, research on cyberterrorism prevention is sparse, particularly in the area of intrusion detection [9].

## 3.2. Intrusion detection

Given the motivation, organization, and sophistication of terrorist groups, and the fact that approximately 10% of traditional intrusions are detected [10], institutions need increasingly sophisticated intrusion-detection methods to better detect and prevent cyberterrorism threats.

An intrusion is “any intentional event where an intruder gains access that compromises the confidentiality, integrity, or availability of computers, networks, or the data residing on them” [32] p. 257. Intrusion detection typically

Uses standard computer logs and computer audit trails, gathered as a matter of routine by host computers, and/or information gathered at communication routers and switches, in order to detect and identify intrusions into a computer system. Successful detection of intrusions is based either upon recognition of a known exploitation of a known vulnerability or upon recognition of unusual or anomalous behavior patterns (signatures) or a combination of the two [32] p. 258.

Rather than being a preventative control per se, intrusion detection is a reactive technique used to identify undesired intrusions requiring immediate action, as well as to provide a source of information to help improve preventive controls [9]. Intrusion detection is indispensable because standard security control techniques are known to be fallible [32] and because modern software is often designed with inadequate security controls [15].

Stallings [42] affirms that inevitably the best intrusion prevention system will fail and that the essential second line of defense is intrusion detection. If an intrusion is detected immediately, the intruder can be identified and appropriate action can be taken. Further, if effective intrusion detection is known to exist, it can act as a deterrent to intrusion attempts. Moreover, effective intrusion detection facilitates the collection of information about intrusion techniques that can be helpful in improving intrusion prevention techniques [42].

Difficulties arise because of the nature of intrusiondetection data: It often contains a scarcity of intrusion instances (positive events), which can confound a learning mechanism in its attempt to discover signatures associated with attacks. Further, where there are large numbers of transactions involved, even a small number of false positives [32] or false alarms can steal away precious time and resources because of the result of investigating spurious intrusions. False negatives can also be a concern: Faced with cyberterrorism, anything that improves the detection of actual intrusions (true positives) will be of considerable value. Without argument, the best intrusion-detection mechanisms will accurately identify both positive instances and negative instances.

Attainment of these objectives is complicated by the fact that cyberterrorism attacks may be fluid in the use of new intrusion techniques or variants of existing ones. We argue that dynamic, self-learning intrusion-detection techniques, as found in GP, are requisite to mitigating cyberterrorism attacks. Lu and Traore [31] provide a summary of other learning mechanisms that have been tested in the intrusion detection domain. Their discussion includes identification of the limitations of those methods as compared to GP.

## 4. Genetic programming

## 4.1. Automatic problem solving

Crosbie and Spafford [9] emphasize that an effective intrusion-detection system must include a robust learning mechanism. They argue that GP is a promising candidate because of its robustness in evolving patternrecognition programs that can be immediately deployed. That is, once programs are evolved, developers can integrate them into a real system to run continually and to detect malfeasance in real time.

In other domains, GP has been highly successful as a means of enabling computers to automatically solve problems without having to provide them with explicit instructions on how to do so [25]. Indeed, John Koza [23], one of the pioneers of GP technology, recently reported that GP has been used to automatically recreate twenty-one previously patented inventions as well as two new patentable inventions. GP has also been applied to other difficult problems, such as pattern recognition [47], data mining [50], robotic control [2], design of artificial neural network architectures [20], grammatical evolution [34], bioinformatics [18], artificial ants [25], Web spidering [7], and generating models to fit data and to help with aircraft landing control [19].

Banzhaf et al. [3] emphasize that problem representation—one of the crucial defining characteristics of a machine learning (ML) system—is also important to the selection of GP. That is, most ML paradigms rely on a form of constrained problem representation, such as

Boolean, threshold, decision trees, case-based representations, and others. Adding constraints can make the traversal of the solution space more tractable, so long as the solution space is well tailored to the problem domain. However, since all these methods result in programs that can be run on a computer, GP can, in principle, evolve any solution that can be calculated by any other ML algorithm.

Moreover, the GP search space includes the problem space and the space of the representation of the problem. Therefore, it may be possible that GP can evolve its own problem representations to detect regularities in various environments. The degree to which an agent can model its environment in this way depends on its own computational resources and on what machine class or language is used when making a model [25].

GP is an extension of the seminal, evolutionary computational technique of genetic algorithms (GAs). Since GP is more expressive than GAs, it is now viewed as a generalization of GAs [3]. The difference in expressiveness is found in the representation of solutions: GAs represent solutions as fixed-length binary strings; whereas GP solutions are represented as variable-length computer programs. These programs are comprised of functions and terminals combined with rules for when and how each function or terminal is to be executed.

A high-level description of GP can be divided into a number of sequential steps:

1. Generate an initial population of random compositions of the functions and terminals of the problem (computer programs).

2. Run a tournament, which picks four programs randomly out of the population of programs. It compares them and picks two winners and two losers based on a fitness measure.

3. Apply the search operators crossover and mutation (and possibly others) to the winners to produce offspring in the following way:

a. Copy the two winners

b. With Crossover Frequency, apply crossover to copies of the winners

c. With Mutation Frequency, mutate the programs from (a).

4. Replace the tournament losers with the new offspring. The winners of the tournament are unchanged.

5. Repeat until a predefined termination criterion has been satisfied, or a fixed number of generations have been explored.

6. The solution is the genetic program with the best fitness within all the generations.

Functions and terminals must be assembled into a structure (genome) before they can execute as programs. The three principal program structures used in GP are tree, graph, and linear structures. Tree and graph structures are widely discussed in the literature. Fig. 1 illustrates a generic example of a linear structure. The tree and graph structures, and even some linear structures require interpretation prior to execution. In this study, we use machine-code linear structures that can be executed directly. This representation has been shown to execute as many as two orders of magnitude faster than other methods [25].

GP has typically utilized nonhomologous crossover operators as the principle method of evolving improved programs. Recent developments have introduced homologous crossover operators, which have characteristics that may improve the process of evolving effective programs [35]. A brief background on each operator is provided in the next section on homology.

## 4.2. Homology

Nonhomologous crossover in GP occurs when instruction blocks are exchanged between two evolved programs with no reference to the size and location of the two sets of instruction blocks (see Fig. 2). Conversely, homologous crossover attempts to mimic natural evolution more closely. With homologous crossover, the two evolved programs are juxtaposed and the crossover is accomplished by exchanging sets of continuous instruction blocks between the two evolved programs. The groups of continuous instruction blocks are selected so that the sets from each parent program are the same length and are taken from the same position in both parents' evolved programs (see Fig. 3). Several researchers have developed operators that are designed to achieve homologouslike results [14,24,50].

![](/api/attachments/U6PRRDUT/fulltext/images/05b786c220b9aa3f911396cbc5e02508762860bd9bf2f60773f134b2ca781d0c.jpg)  
Fig. 1. Structure of AIMGP linear genome.

Pertinent to this study, Francone et al. [14] developed a homologous crossover operator called sticky crossover to promote the emergence of positional homology in a population of linear genomes. This operator randomly selects a sequence of code (a block) from one parent program. This sequence of instruction code is then swapped with a sequence of instruction code that has the same position and length in the other parent program (see Fig. 3). Positional homology is thus achieved directly. The authors argue that this operator may also encourage the evolution of functionally similar code at equivalent positions in the parent programs. In particular, these researchers reason that the result will be a homology of at least partially functional code and that this functional code can evolve through normal selection to become useful code. An empirical test on a Gaussian classification problem yielded better accuracy in a validation set by applying higher homologous crossover rates.

In sum, homologous crossover is a method recombination between equal-length program fragments in the same positions in each parent structure. This strategy is designed to reduce the tendency of evolved programs to grow larger with parallel fitness improvements. The study by Francone et al. [14] provides preliminary evidence that homologous crossover can yield salutary effects, including perhaps the emergence of functionally related blocks, improved robustness, and better generalization ability than can be achieved with nonhomologous crossover.

## 5. Experiment

## 5.1. Data profile

The data selected for our study comes from the 1999 Knowledge Discovery in Database (KDD) Cup data, supplied by the Defense Advanced Research Projects Agency (DARPA) and MIT's Lincoln Laboratories [29].

![](/api/attachments/U6PRRDUT/fulltext/images/83527a475238e07941ad70ca7bdcc19871fd95bd36068c2702dbbcb66b4e96d1.jpg)  
Fig. 2. Ordinary GP crossover with linear genome.

The dataset was chosen because it is current and has strong representational integrity of actual intrusion forensic data. The dataset was generated via a simulated U.S. Air Force LAN set up at the Lincoln Laboratories. It was operated similar to a standard Air force network with the exception of planned and recorded attacks.

The original data was composed of nine weeks of raw TCP dump data from the Air Force network. This large database was established based on sequences of TCP packets [43]. Forty-one unique attributes were compiled from each raw TCP packet sequence, including symbolic attributes like “protocol type,” with values

TCP, ICMP, and UDP, along with continuous attributes such as error rates over the closed interval [0,1] and bytes transferred over the half-open interval [0, ∞). Each resulting connection record was then labeled as either normal or malicious. In the complete dataset, there are approximately five million separate connection records, totaling over 720 MB.

Stolfo et al. [43] defined higher-level features that help distinguish normal connections from attacks. The same host feature examines only the connections in the past two seconds that have the same destination host as the current connection. The same service feature examines only the connections in the past two seconds that have the same services as the current connection. These features together are called time-based traffic features on the connection records. Because some PROBING attacks scan the hosts (or ports) using a much larger time interval than two seconds (e.g., once per minute), the connection records were also sorted by destination host, using a window of 100 connections to the same host. Since the R2L and U2R attacks are embedded in the data portion of packets, normally involving only a single connection, sequential patterns were not apparent for these types of attacks.

![](/api/attachments/U6PRRDUT/fulltext/images/ef1f2b471cf3bdb45a7a773597bcbc6305b4fa21c8c0d5ae001c8cc7f77dd372.jpg)  
Fig. 3. Homologous crossover with linear genomes.

The attacks fall into four main categories [33]: (1) denial-of-service (DoS), (2) probing and surveillance, (3) unauthorized access from a remote to a local machine (R2L), and (4) unauthorized access to local superuser/root privileges (U2R). We will now briefly discuss each of these.

DoS is a class of attacks where some computing or memory resource is made too busy to handle requests or too full for legitimate users to access the machine [33]. DoS attacks often involve pinging. When a machine is pinged, an ICMP (Internet Control Message Protocol) echo request packet (including the return IP address) is sent to the destination computer. When the destination computer receives the TCP packet, it replies to confirm the ping request.

The DoS attacks we examined included Smurf, Neptune, and Back. In the case of a Smurf DoS attack, the ping's packet return IP address is replaced with the IP address of the targeted machine. The ping is issued to an entire IP broadcast address. This causes every machine to respond to the bogus ping packets and reply to the targeted machine, which floods the targeted machine. As explained in [46], Neptune exploits a TCP protocol vulnerability, causing a SYN flood (TCP connection requests coming faster than a machine can process them) DoS on one or more ports. Back is a DoS attack against an Apache webserver where a client requests a URL containing too many backslashes, causing webserver problems.

As explained in [33], probing is a class of attacks where a network of computers is scanned to gather information or find known vulnerabilities. The attacker then looks for ways to exploit the network by using this knowledge of the machines and services available. Examples we tested included IPSweep, NMap, Portsweep, and Satan. IPSweep scans a network of computers or a DNS server to find valid IP addresses (determine what machines are on a network), as well as what services these machines are running [6]. NMap also maps the network, but it uses various options, including SYN, FIN (not finishing the three-way handshake that opens a port), and ACK scanning with both TCP and UDP, as well as ICMP (ping) scanning [6]. Portsweep also examines many ports to determine which services are supported (active ports) on a single host. Satan looks for more well-known security vulnerabilities.

R2L and U2R are the two smallest classes, but they represent the most serious attacks. Unauthorized access from a remote to a local machine allows an attacker that does not have an account to exploit some vulnerability to gain local access, exfiltrate files from the machine, or modify data in transit to the machine [28,33]. We examined the buffer overflow where an attacker gains access to a machine by remotely overflowing the IMAP service.

Unauthorized access to local superuser/root privileges refers to attacks where an attacker starts out with normal user account access but is able to exploit some vulnerability to gain root access. The goal of this attack is to exfiltrate special files that the security policy specifies should remain on the victim hosts [28]. The type we examined is WarezClient, which downloads from an FTP server illegal copies of copyrighted software that were placed there anonymously with WarezMaster [6,52].

## 6. Research method

Somayaji et al. [41] emphasize that an effective intrusion-detection system must have the ability to detect attacks that it has never before encountered. Hence, it is important that our experiment test the capability of our model to generalize to unseen cases, both positive and negative.

In this study, we have the advantage of a very large dataset from which to extract sizeable training and test sets. Weiss and Kulikowski [49] and Efron [11] affirm that when training sets contain more than 1000 instances, accuracy statistics from a single train-andtest procedure are reliable. Thus, we have not used cross-validation or bootstrap techniques; instead, we have applied the single train-and-test mechanism to ten different types of intrusion as described in the previous section. Using SQL statements, we selected training sets of 30,000 instances and test sets of 10,000 instances from the DARPA data set. These sets contained the same proportional profiles as the complete dataset. The fields were also ordered for use in the software. Comparative performance was measured by creating two models for each intrusion domain: one each for the ordinary crossover operator and the homologous crossover operator. Experiments were expressed as 0–1 (non-intrusion or intrusion) classification problems.

In a study of patterns of another type, Francone et al. [14] varied the mutation rate over 5%, 20%, 50%, and 80%. Mutation rates above 50% dominated performance at every crossover rate tested. Consequently, in our experiments, we set the mutation rate at a constant value of 80%. Francone et al. [14] also experimented with crossover rates of 0%, 20%, 40%, 59%, 80%, and 95%. Dominant results were achieved using the 95% crossover rate. Based on a series of preliminary tests, we selected a 70% crossover rate as being more robust across problem domains. Following Banzhaf, et al. [3], we set the mutation rate at five percent.

Tests were executed using Disciplus© 3.0 software on a desktop computer with a Pentium© IV processor. Each run was allowed a time limit of ten minutes, seven minutes longer than in the study by Francone et al. [14], whose time limit was justified by the code executing much faster than competing GP systems.

The instruction groups that were used included Addition, Arithmetic, Comparison, Data Transfer, Multiplication, Subtraction, and Trigonometric. The Addition instruction allows addition of two registers. The Arithmetic Group contains instructions for absolute value, change of sign, scaling, and square root. The Comparison Group compares the values in two registers. The Data Transfer Group allows values to be moved without changing the values. The Multiplication Group multiplies two registers, or allows the contents of a register to be multiplied by a constant. The Subtraction Group is similar using subtraction. The Trigonometric

Group evokes two functions: cosine and sine. These groups were selected in an attempt to keep the instruction set small enough to mitigate search time, while retaining capabilities for robust exploration of the solution space, including nonlinear behavior [3].

Other parameter settings controlled by the user include the program size (P), which controls the size of the initial and subsequent programs. Koza et al. [23] recommend $5 0 \le P \le 1 0 , 0 0 0$ , with a common setting of 500—which is what we used. An advanced feature available in some GP software is that of dynamic subset selection (DSS). DSS computes the fitness of evolved programs by using a constantly changing subset of the entire training set. The choice of training subset from the entire set of training examples applies three criteria: age, difficult, and randomness. Age references the time since a specific training example has been used in the training subset. Difficulty is a measure of how difficult the training example is for the algorithm to correctly classify. Randomness is applied in the usual way. The user may set the relative importance of these criteria, and we set age at 50% and difficulty at 50% as suggested in [3].

The resulting models are deployable as programs, which then execute at the same speed as standard code. They can also be deployed as machine language programs, which make them directly executable. In either case, the intrusion detection code executes in real time.

## 7. Results and discussion

Table 1 shows the ratio of intrusions to nonintrusions in these datasets. Testing on each dataset was completed for each of the model types: nonhomogous crossover and homologous crossover.

Table 2 depicts overall accuracy in applying learned GP models to the test sets. The overall accuracy is high for all intrusions tested, with the homologous GP models weakly dominating the nonhomologous crossover GP models (homologous crossover accuracy z nonhomologous crossover accuracy). Yet accuracy on both positive instances and negative instances is important: We wish to identify intrusions accurately while limiting the overhead associated with taking unneeded action. It is evident from Table 1 that in some instances, a naïve model that always predicts negative might yield high overall accuracy but may never identify an actual intrusion.

Table 2  
Overall comparative accuracy on test sets

<table><tr><td>GP model/problem type</td><td>Ordinary crossover</td><td>Homologous crossover</td></tr><tr><td>Smurf</td><td>99.74</td><td>99.88</td></tr><tr><td>Satan</td><td>99.77</td><td>99.77</td></tr><tr><td>IPSweep</td><td>99.91</td><td>99.91</td></tr><tr><td>PortSweep</td><td>99.78</td><td>99.87</td></tr><tr><td>Back</td><td>99.99</td><td>99.99</td></tr><tr><td>Normal</td><td>97.60</td><td>98.85</td></tr><tr><td>Buffer Overflow</td><td>99.8</td><td>100.00</td></tr><tr><td>WarezClient</td><td>99.79</td><td>99.90</td></tr><tr><td>Neptune</td><td>99.30</td><td>99.65</td></tr></table>

Table 1  
Proportions of intrusions in each dataset

<table><tr><td>Set type/problem domain</td><td>Learning(intrusions/total)</td><td>Test(intrusions/total)</td></tr><tr><td>Smurf</td><td>16,854/29,394</td><td>5601/9800</td></tr><tr><td>Satan</td><td>89/29,395</td><td>40/9800</td></tr><tr><td>IPSweep</td><td>90/29,404</td><td>9/9780</td></tr><tr><td>PortSweep</td><td>61/29,390</td><td>22/9794</td></tr><tr><td>Back</td><td>16/29,400</td><td>2/9790</td></tr><tr><td>Normal</td><td>5878/29,394</td><td>1937/9790</td></tr><tr><td>Buffer Overflow</td><td>24/29,413</td><td>3/9797</td></tr><tr><td>WarezClient</td><td>623/30,000</td><td>24/10,110</td></tr></table>

Table 3 shows comparative performance in identifying positive instances. Again, the GP models with homologous crossover weakly dominate GP models with nonhomologous crossover. The accuracy of the homologous model ranges from a high of 100% to a low of 66.7%.

Table 4 depicts comparative performance in identifying negative instances. Nonhomologous crossover yields slightly better accuracy for the Satan domain. Otherwise, the homologous-crossover models continue to weakly dominate. A noteworthy difference is that the base numbers are large, indicating that variances in accuracy reflect larger numbers of misidentified negative instances. The Base-Rate Fallacy, as discussed by

Table 3  
Comparative accuracy in identifying intrusions in test sets

<table><tr><td>GP model/problem type</td><td>Ordinary crossover (%)</td><td>Homologous crossover (%)</td></tr><tr><td>Smurf</td><td>99.82</td><td>99.93</td></tr><tr><td>Satan</td><td>85.83</td><td>100.00</td></tr><tr><td>IPSweep</td><td>68.90</td><td>88.89</td></tr><tr><td>PortSweep</td><td>81.82</td><td>86.36</td></tr><tr><td>Back</td><td>100.00</td><td>100.00</td></tr><tr><td>Normal</td><td>99.07</td><td>100.00</td></tr><tr><td>Buffer Overflow</td><td>100.00</td><td>100.00</td></tr><tr><td>WarezClient</td><td>66.34</td><td>66.67</td></tr><tr><td>Neptune</td><td>99.67</td><td>100.00</td></tr></table>

![](/api/attachments/U6PRRDUT/fulltext/images/afd46e47b83d606eb2285bcb535f0a106733f0b851c6065c9503d7349fec214e.jpg)  
Fig. 4. Validation performance over time—Smurf intrusion.

Stallings [42], requires that the accuracy on negatives be very high to avoid costly activity in responding to false intrusion alarms.

Figs. 4 and 5 provide example validation performance (homologous crossover) over time for Smurf intrusions and Satan intrusions, respectively. In Fig. 4 it can be seen that GPs that accurately identify Smurf intrusions evolve much earlier in the evolutionary process than do programs that accurately identify nonintrusions. Fig. 5 shows similar dynamics, except that it takes longer for both intrusion and non-intrusion performance to achieve high levels of performance. This suggests that patterns in the Satan data may be more difficult to identify.

Table 5 compares the current study results with results from the KDD'99 Classifier Leaning Contest that also used the DARPA data. 24 entries were submitted for the contest. The winning analysis was submitted by Dr. Bernhard Pfahringer of the Austrian Research Institute for Artificial Intelligence; C5 was used as the base-level learning algorithm [35]. Elkan [12] notes that only nine entries scored better than “simply the trusty old 1-nearest neighbor classifier,” of which only six were statistically significantly better. The Homologous Crossover consistently identified the intrusions better than earlier results.

Table 4  
Comparative accuracy in identification of negative instances in test sets

<table><tr><td>GP model/problem type</td><td>Ordinary crossover (%)</td><td>Homologous crossover (%)</td></tr><tr><td>Smurf</td><td>99.95</td><td>99.95</td></tr><tr><td>Satan</td><td>100.00</td><td>99.64</td></tr><tr><td>IPSweep</td><td>99.99</td><td>100.00</td></tr><tr><td>PortSweep</td><td>99.90</td><td>100.00</td></tr><tr><td>Back</td><td>100.00</td><td>100.00</td></tr><tr><td>Normal</td><td>99.15</td><td>100.00</td></tr><tr><td>Buffer Overflow</td><td>99.89</td><td>100.00</td></tr><tr><td>WarezClient</td><td>99.97</td><td>99.97</td></tr><tr><td>Neptune</td><td>99.19</td><td>99.56</td></tr></table>

![](/api/attachments/U6PRRDUT/fulltext/images/417d81a805dd93f8921000150a02c385222f443d61d1592cfc811018e46462ca.jpg)  
Fig. 5. Validation performance of evolved programs over time—Satan intrusion.

Overall, the accuracy results over the types of intrusions tested are very high. Since our evidence is empirical, we cannot claim general proof. We do, however, argue that the dataset we tested is robust across a variety of known and supposed intrusion patterns. It is possible that untested domains exist in which intrusion detection is less effective.

It is important to note that our dataset represents connection-level data, as seen in [26]. It may be useful for future research to apply GP to other levels of analytical units for cyberterrorism prevention. These units could include packet-level [5,39], session/connection-level (our level of analysis), user-level [26], and program-level intrusion detection [16,22].

Table 5  
Comparative accuracy of other methods with homologous crossover

<table><tr><td rowspan="2">Attack category</td><td colspan="3">Accuracy (% correct)</td></tr><tr><td>Simple method—nearest neighbor</td><td>Competition winner</td><td>Homologous crossover</td></tr><tr><td>Normal</td><td>99.6</td><td>99.5</td><td>98.9</td></tr><tr><td>Probe</td><td>75.0</td><td>83.3</td><td>99.9</td></tr><tr><td>Denial of service (DOS)</td><td>97.3</td><td>97.1</td><td>99.8</td></tr><tr><td>User-to-root (U2R)</td><td>3.5</td><td>13.2</td><td>99.9</td></tr><tr><td>Remote-to-local (R2L)</td><td>0.6</td><td>8.4</td><td>100.0</td></tr></table>

## 8. Concluding remarks

The results of this study, together with the work of Crosbie and Spafford [9], and Lu and Traore [31], shows the potential of GP as a tool in devising defenses against cyberterrorism in the form of intrusion-detection programs that are immediately deployable. In a dynamic environment, it may be necessary to produce one of these programs daily, weekly, or each time a new intrusion is identified and its pattern is learned.

Although the focus of our study was not on comparative models, per se, we did include competing crossover operators to help address the intrusiondetection problem. The homologous crossover operator dominated results in overall accuracy, as well as accuracy in identifying positive and negative instances in test sets that were unseen in evolving the respective GP models. These were our objectives in considering the needs of cyberterrorist intrusion detection.

In summary, learning systems are at the foundation of intrusion detection; but the question of which learning system is most effective is not yet established. The answer will surely be a mechanism that is adaptable to the dynamics of intrusion attacks. GP produced unusual accuracy in our experiment, and we anticipate that these results will encourage related studies.

## Acknowledgements

We express appreciation for funding received to help support this project from the Information Systems Department and the Kevin and Debra Rollins Center for e-Business, both at the Marriott School, Brigham Young University.

## References

[1] J. Arquilla, D. Ronfeldt, Networks and Netwars: The Future of Terror, Crime, and Militancy, Rand Corporation, Santa Monica, CA, 2001.

[2] W. Banzhaf, P. Nordin, M. Olmer, Generating adaptive behavior for a real robot using function regression within genetic programming, Proceedings of the Second Annual Conference on Genetic Programming 1997, Stanford University, CA, 1997.

[3] W. Banzhaf, P. Nordin, R.E. Keller, F.D. Francone, Genetic Programming: an Introduction: on the Automatic Evolution Of Computer Programs and its Applications, Morgan Kaufmann, San Francisco, CA, 1998.

[4] M. Burgess, Computer immunology, Proceedings of the Twelfth Systems Administration Conference (Lisa XII). Boston, MA, 1998.

[5] J. Cannady, J. Mahaffey, The application of artificial neural networks to misuse detection: initial results, Proceedings of the 1st International Workshop on Recent Advances in Intrusion Detection (RAID, 1998), Louvain-la-Neuve, Belgium, 1998.

[6] P. Chan, W. Fan, W. Lee, A. Prodromidis, S. Tselepis, JAM Project at Columbia University, vol. 2004, 2004.

[7] H. Chen, Y.-M. Chung, M. Ramsey, A smart itsy bitsy spider for the Web, Journal of the American Society of Information Science 49 (1998) 604–618.

[8] B.C. Collin, The future of cyberterrorism: where the physical and virtual worlds converge, Proceedings of the 11th Annual International Symposium on Criminal Justice Issues, 2001.

[9] M. Crosbie, E. Spafford, Applying genetic programming to intrusion detection, Proceedings of the Working Notes for the AAAI Symposium on Genetic Programming, Cambridge, MA, 1995.

[10] A. de Borchgrave, F.J. Cilluffo, S.L. Cardash, M.M. Ledgerwood, Cyber Threats and Information Security: Meeting the 21st Century Challenge, Center for Strategic and International Studies (CSIS), Washington, DC, May 2001.

[11] B. Efron, Estimating the error rate of a prediction rule, Journal of the American Statistical Association 78 (1983) 316–333.

[12] C. Elkan, Results of the KDD'99 Classifier Learning Contest, vol. 2005, SIGKDD ACM, 1999.

[13] S. Forrest, A. Somayaji, D. Ackley, Building diverse computer systems, Proceedings of the Sixth Workshop on Hot Topics in Operating Systems, Los Alamitos, CA, 1997.

[14] F.D. Francone, W. Banzhaf, M. Conrads, P. Nordin, Homologous crossover in genetic programming, Proceedings of the Genetic and Evolutional Computation Conference (GECCO), Orlando, FL, 1999.

[15] S. Garfinkel, G. Spafford, Practical UNIX Security, O'Reilly, Sebastepol, CA, 1991.

[16] A.K. Ghosh, J. Wanken, F. Charron, Detecting anomalous and unknown intrusions against programs, Proceedings of the 1998 Annual Computer Security Applications Conference (ACSAC'98), Los Alamitos, CA, 1998.

[17] P. Grabosky, M. Stohl, Cyberterrorism, Reform 82 (2003) 8–13.

[18] S. Handley, Predicting whether or not a 60-base DNA sequence contains a centrally-located splice site using genetic programming, Proceedings of the Workshop on Genetic Programming: From Theory to Real-World Applications, Tahoe City, CA, 1995.

[19] J.V. Hansen, Genetic programming experiments with standard and homologous crossover methods, Genetic Programming and Evolvable Machines 4 (2003) 53–66.

[20] J.V. Hansen, R.D. Meservy, Learning experiments with genetic optimization of a generalized regression neural network, Decision Support Systems (DSS) 18 (1996) 317–325.

[21] S.A. Hofmeyr, S. Forrest, Architecture for an artificial immune system, Evolutionary Computing Journal 8 (2000) 443–473.

[22] S.A. Hofmeyr, S. Forrest, A. Somayaji, Intrusion detection using sequences of system calls, Journal of Computer Security 6 (1998) 151–180.

[23] J.R. Koza, M.A. Keane, M.J. Streeter, Evolving inventions, Scientific American 288 (2003) 52–59.

[24] W.B. Langdon, Size fair and homologous tree crossovers, CWI Technical Report, Amsterdam, The Netherlands, 1999.

[25] W.B. Langdon, R. Poli, Foundations of Genetic Programming, Springer-Verlag, Berlin, 2002.

[26] W. Lee, S. Stolfo, A framework for constructing features and models for intrusion detection systems, ACM Transactions on Information and System Security 3 (2000) 227–261.

[27] J.A. Lewis, Assessing the Risks of Cyber Terrorism, Cyber War, and Other Cyber Threats, Center for Strategic and International Studies, Washington, DC, December 2002.

[28] R. Lippmann, J.W. Haines, D.J. Fried, J. Korba, K. Das, The 1999 DARPA off-line intrusion detection evaluation, vol. 2004, Lincoln Laboratory, Massachusetts Institute of Technology, 1999.

[29] R. Lippmann, J.W. Haines, D.J. Fried, J. Korba, K. Das, Analysis and results of the 1999 DARPA off-line intrusion detection evaluation, Proceedings of the Recent Advances in Intrusion Detection (RAID) 2000, Toulouse, France, 2000.

[30] V. Lorenzo, M. Knights, Affecting trust: terrorism, Internet, and offensive information warfare, Terrorism and Political Violence 12 (2000) 15–36.

[31] W. Lu, I. Traore, Detecting new forms of network intrusion using genetic programming, Computational Intelligence 20 (2004) 470–489.

[32] G. Mohay, A. Andeson, B. Collie, O. de Vel, R. McKemmish, Computer and Intrusion Forensics, Artech House, Boston, MA, 2003.

[33] S. Mukkamala, A.H. Sung, Identifying significant features for network forensic analysis using artificial intelligent techniques, International Journal of Digital Evidence 1 (Winter 2003) 1–17.

[34] M. O'Neill, C. Ryan, M. Keijzer, M. Cattolico, Crossover in grammatical evolution, Genetic Programming and Evolvable Machines 4 (2003) 67–93.

[35] B. Pfahringer, Winning the KDD99 classification cup: bagged boosting, SIGKDD Explorations 1 (2000) 65–66.

[36] M.M. Pollit, Cyberterrorism: Fact or fancy? FBI Laboratory Washington, DC, 2002

[37] T.S. Raghu, R. Ramesh, A.B. Whinston, Addressing the homeland security problem: a collaborative decision-making framework, Proceedings of the First Symposium on Intelligence and Security Informatics, ISI 2003, Tucson, AZ, 2003.

[38] E. Reid, W. Chung, J. Xu, Y. Zhou, R. Schumaker, M. Sageman, C. Hsinchun, Terrorism knowledge discovery project: a knowledge discovery approach to addressing the threats of terrorism, Proceedings of the Second Symposium on Intelligence and Security Informatics, Tucson, AZ, 2004.

[39] M. Roesch, Snort: lightweight intrusion detection for networks, Proceedings of the LISA '99: 13th Annual Systems Administration Conference, Seattle, WA, 1999.

[40] L.I. Shelley, Organized crime, terrorism, and cyberterrorism, in: A. Bryden, P. Fluri (Eds.), Security Sector Reform: Institutions, Society, and Good Governance, Nomos Verlagsgesellschaft, Baden-Baden, 2003, pp. 303–312.

[41] A. Somayaji, S. Hofmeyr, S. Forrest, Principles of a computer immune system, Proceedings of the 1997 New Security Paradigms Workshop, Langdale, Cumbria, UK, 1998.

[42] W. Stallings, Cryptography and Network Security, 3rd ed., Prentice Hall, 2003.

[43] S.J. Stolfo, W. Fan, W. Lee, A. Prodromidis, P.K. Chan, Costbased modeling for fraud and intrusion detection: results from the JAM project, Proceedings of the DARPA Information Survivability Conference and Exposition, Hilton Head, SC, 2000.

[44] A. Sun, M.-M. Naing, E.-P. Lim, W. Lam, Using support vector machines for terrorism information extraction, Proceedings of the First Symposium on Intelligence and Security Informatics, ISI 2003, Tucson, AZ, 2003.

[45] Terrorism: Questions and Answers: Cyberterrorism, vol. 2004, Council on foreign relations, 2004.

[46] G. Torkzadeh, G. Dhillon, Measuring factors that influence the success of Internet commerce, Information Systems Research (ISR) 13 (2002) 187–206.

[47] T.W.A., Genetic programming for feature discovery and image discrimination, Proceedings of the Fifth International Conference on Genetic Algorithms, San Mateo, CA, 1993.

[48] W.H. Webster, A. de Borchgrave, P.R. Gallagher, F.J. Cilluffo, B. D. Berkowitz, S. Lanz, Cybercrime…Cyberterrorism…Cyberwarfare...: Averting an Electronic Waterloo, Center for Strategic and International Studies (CSIS), Washington, DC, November 1998.

[49] S. Weiss, C. Kulikowski, Computer Systems That Learn: Classification and Prediction Methods from Statistics, Neura Nets, Machine Learning, and Expert Systems, Morgan Kaufmann, 1991.

[50] M.L. Wong, K.S. Leung, Data Mining Using Grammar Based Genetic Programming and the Applications, Kluwer Academic Publishers, 1999.

[51] R. Zheng, Y. Qin, Z. Huang, H. Chen, Authorship analysis in cybercrime investigation, Proceedings of the First Symposium on Intelligence and Security Informatics, ISI 2003, Tucson, AZ, 2003.

[52] M. Zissman, DARPA intrusion detection evaluation: 1998 training data attack schedule, vol. 2004, Lincoln Laboratory, Massachusetts Institute of Technology, 1998.

![](/api/attachments/U6PRRDUT/fulltext/images/36aeefc5e599c9d99172facbba4d471a62cb42e71b14a5d5c38fb71bb8cf5660.jpg)

James V. Hansen is the J. Owen Cherrington Professor in the Information Systems Department of the Marriott School at Brigham Young University. He also is a faculty researcher at the Rollins Center for e-Business at the Marriott School. He received his Ph.D. from the University of Washington, Seattle. Professor Hansen serves on the editorial boards of IEEE Intelligent Systems, Information Systems Frontiers, and Intelligent Systems in Accounting, Finance and

Management, and is listed in Who’s Who in Science and Engineering. His research interests are in machine learning and agent-based systems. His most recent research has been published in Decision Support Systems (DSS), Information & Management (I&M), European Journal of Operational Research, Electronic Commerce Research (ECR), Communications of the ACM (CACM), Computers & Operations Research, Genetic Programming and Evolvable Machines, IEEE Transactions on Neural Networks, and Journal of Experimental and Theoretical Artificial Intelligence.

![](/api/attachments/U6PRRDUT/fulltext/images/807b6245f5582b149069e8cd5465a2c2ea3a8d970549cd7a4faab91f7db2d7e4.jpg)

Paul Benjamin Lowry is an Assistant Professor of Information Systems at the Marriott School, Brigham Young University and a Rollins Faculty Fellow, affiliated with the Kevin and Debra Rollins Center for e-Business. His interests include Human-Computer Interaction (HCI) (collaboration, communication, entertainment), e-business (electronic markets), and Scientometrics of Information Systems research. He received his Ph.D. in Management Information Sys-

tems (MIS) from the University of Arizona, and a B.S. in Information Management and an MBA, both from the Marriott School at Brigham Young University. He has articles accepted and published in Journal of the Association for Information Systems (JAIS), Communications of the ACM (CACM), Communications of the Association for Information Systems (CAIS), Decision Support Systems (DSS); IEEE Transactions on Systems, Man, and Cybernetics (IEEESMC); IEEE Transactions on Professional Communication (IEEETPC); Information Sciences; Journal of Business Communication (JBC), Journal of Information Systems Education (JISE), and others.

![](/api/attachments/U6PRRDUT/fulltext/images/dcef694b68c4e9131871842bb7f67bc67578b1e288be629a928262a8d8dd6e31.jpg)

Daniel McDonald is a Ph.D. candidate at the University of Arizona in Management Information Systems, where he also received his Master of Science degree. Daniel’s research centers primarily on text mining and natural language processing. Daniel has published in journals such as ACM Transactions on Information Systems (ACMTOIS), Bioinformatics, and Journal of the American Society for Information Science and Technology. Daniel has presented at the Joint

Conference on Digital Libraries (JCDL) and the AAAI Spring Symposium. Prior to returning to school, Daniel worked three years in industry accounting and systems roles. He currently works in the Global Knowledge Management Center at the University of Utah.

![](/api/attachments/U6PRRDUT/fulltext/images/ac9e4bd13d93ddb73bbe0a30a61e0a959dc810367a84a79aadbba552ba52890a.jpg)

Rayman D. Meservy received his Ph.D. at the University of Minnesota in 1985 and then taught at Carnegie-Mellon University. He is currently a professor at Brigham Young University in Accounting and Information Systems. He is past president of the American Accounting Association-Information Systems Section and is currently serving as treasurer of the Association for Information Systems (AIS). He has published extensively in such journals as The Accounting Review,

IEEE Transactions on Knowledge and Data Engineering (IEEETKDE), Auditing: A Journal of Practice and Theory, and Decision Support Systems (DSS).
