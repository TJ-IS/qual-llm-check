---
otero_id: 14428
otero_key: "89X4XWEF"
title: "Automated dynamic approach for detecting ransomware using finite-state machine"
authors: "Gowtham Ramesh; Anjali Menen"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113400"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Automated dynamic approach for detecting ransomware using finite-state machine

![](/api/attachments/89X4XWEF/fulltext/images/3d4abfba788fc71bdaa4a9dfd41451e111b37e0e974c5fb9609b5d2bb8d4082d.jpg)

Gowtham Ramesh<sup>⁎</sup>, Anjali Menen

Department of Computer Science and Engineering, Amrita School of Engineering, Coimbatore, Amrita Vishwa Vidyapeetham, India.

A R T I C L E I N F O

Keywords: Cybersecurity Intrusion/anomaly detection Malware mitigation Ransomware

## A B S T R A C T

Ransomware is a type of malware that afects the victim data by modifying, deleting, or blocking their access. In recent years, ransomware attacks have resulted in critical data and financial losses to individuals and industries. These disruptions force the need for developing efective anti-ransomware methods in the research community. However, most of the existing techniques are designed to detect a specific ransomware variant instead of providing a generic solution mainly because of the obfuscation techniques used by ransomware or the use of static analysis methods. In this context, this paper proposes a novel ransomware-detection technique that identifies ransomware attacks by evaluating the current state of a computer system with knowledge of a ransomware attack. The finite-state machine model is used to synthesise the knowledge of the ransomware attack with respect to the victim machine. The proposed method monitors the changes happening in the computer system in terms of utilisation, persistence, and lateral movement of its resources to detect ransomware attacks. The experimental results demonstrate that the proposed method can accurately detect attacks from diferent ransomware variants with significantly few false predictions.

## 1. Introduction

Malware refers to malicious software developed by attackers to harm computer users. Attackers remotely inject the malware into the user machine using any of the payload delivery mechanisms such as email attachments or drive-by downloads. Ransomware is a type of malware that is developed with the malicious intent of extorting money from the victims. Ransomware primarily encrypts the user files in the target machine, and as a follow-up action, either creates newly en crypted files while deleting the original files or modifies the existing files in the system. Finally, it locks down the system [1]. After en cryption, the ransomware displays a pop-up message on the user screen demanding the user to pay a ransom in Bitcoins. After payment of the ransom by the victims, a decryption key is given to access the user files.

Ransomware attacks have evolved as a serious cyber threat for common online users, industries, and governments. In early 2011, more than 60,000 ransomware attacks were detected by cybersecurity organisations; as the years passed, this count has increased by fourfold. In 2013, the Cryptolocker ransomware infected more than 250,000 sys tems, which then drastically increased to 500,000 machines during 2014. Variants of this ransomware have been estimated to harvest approximately \$3 million from the global organisation during this period [20].

The cybercrime reports show that 406,887 unique ransomware attacks hosted in the year 2015 cost the world over \$325 million dollars. In 2016, ransomware attacks led to financial losses of approximately one billion dollars. Researchers observed that 40% of spam e-mails contained links to ransomware, which resulted in a 6000% steep increase compared with that in the year 2015. In 2017, the financial losses of global organisations due to this malware attack exceeded five billion dollars with an annual attack growth rate of 350% [16,17]. Global ransomware-protection agencies predicted that the loss due to ransomware attacks will exceed \$20 billion by the year 2021. In addition, they mentioned that the present solutions are not efective in protecting against ransomware attacks and indicated the need for developing active solutions [22].

The focus of ransomware attacks is currently shifted from usercentric to more lucrative targets such as healthcare, schools, district/ state/local governments, law-enforcement agencies, and small and medium business entities [21]. This shift is mainly due to the lack of valuable resources existing in consumer computing devices as well as the higher dependence of enterprises on e-mails for their communication, which is leveraged by most malware to infect the target systems. Enterprise infections have gone up by 12% and accounted for 81% of the total ransomware infections [13]. In 2018, 45% of the infected organisations paid ransom for recovery, which increased to 58% in the year 2019. These facts clearly show that ransomware is one of the fastest growing threats in the cybercrime landscape, and robust tech nological solutions and user education against this attack are needed.

According to its behavioural pattern, ransomware is widely categorised into two types, namely, crypto and locker. Among these variants, the crypto ransomware is considered highly risky because it applies strong encryption algorithms on the user files and makes recovery impossible without paying the ransom. Most of the protection systems against the crypto ransomware are designed based on passive or signature-based analysis. The signatures are commonly generated ofline, based on the code patterns existing in known ransomware and stored in a signature repository. The malicious executables are only identified as ransomware when an explicit signature that matches an entry in the repository exists. However, these techniques fail to detect new variants of ransomware featuring code-obfuscation techniques and those de signed for targeted attacks.

Hence, developing a robust protection method against this critical malware is needed by considering all the aforementioned gaps. The method proposed in this paper deploys a dynamic-analysis based paradigm to detect active ransomware. This method monitors the changes that happen in a computer system with respect to the user files, retention state, lateral movement, and system resources. The variability of the system states due to ransomware as well as benign applications is unambiguously captured and represented using a formal framework finite-state machine (FSM). A set of listeners and decision-making modules is deployed along with the FSM model to detect a ransomware attack.

To summarise, this study makes the following research contribu tions.

• It proposes a novel dynamic-analysis based ransomware detection model, which provides more efective countermeasures against ransomware attacks.

It develops an FSM that represents the polymorphic traits of the ransomware. The state transition of the FSM signifies the changes that occur in the underlying system.

• This generic protection system is designed to detect diferent ransomware variants.

An overview of related works is presented in Section 2. The archi tecture of the overall system is discussed in Section 3. In Section 4, we explain the components involved in the behaviour-analysis module. Section 5 explains the decision-making module and details the FSM model used for ransomware detection. The implementation details, evaluation methodology, and experimental results are discussed in Section 6. Section 7 details the limitations of the proposed method Finally, conclusions are presented in Section 8.

## 2. Related work

This section presents the details of the technological need for the proposed system and highlights related studies towards ransomwaredetection techniques and their limitations. Most of the countermeasures against ransomware attacks focus on providing technological solutions. These solutions are broadly classified into three types, namely static, network-parameter analysis, and dynamic analysis methods.

The static analysis methods are designed to detect malware by inspecting the application binary before it executes in the system. The code patterns or signatures extracted from the application binary are compared against known malicious-code patterns to detect the ransomware. The static methods are largely ineficient in detecting unknown ransomware as well as attacks that employ code obfuscation evasion techniques [18]. In many cases, the true behavioural patterns of ransomware are only revealed during execution because of their nonautonomous functionality.

The network-parameter-analysis methods are designed by observing the common communication and well-known infection patterns of ransomware. These mitigation methods detect ransomware attacks by analysing the network trafic and system logs. Cabaj and Mazurczyk [2] proposed ransomware-mitigation methods to stop malware spread in a local network using software-defined networking (SDN), which defines a set of control rules to block communication from the infected computers to the rest of the network. As part of this work, two SDN-based algorithms were proposed, namely SDN1 and SDN2, which both relied on dynamic blacklisting. The SDN algorithms forward all DNS messages to the controller for inspection. The system discards the response when the domain name in the message matches the entry in the precompiled blacklist and prevents the encryption process. However, these techniques are highly inefective for ransomware that employs the dynamic domain generation algorithms. In addition, the growing number of connected devices and volume of trafic they directly generate afect the responsiveness of the security system that works based on the networkparameter analysis. Most of these methods fall short in detecting unknown ransomware types as well as new variants of known ransomware.

The dynamic analysis methods detect ransomware attacks by evaluating the parameters extracted from the active processes in a computer system. These methods are further categorised into process-, data-, and resource-centric approaches [14,17].

The process-centric approach monitors the activities of the running processes in a system and predicts its intended malicious actions before they actually exhibit. Hampton et al. [6] developed a call-tracer approach that analysed the strains commonly produced by the ransomware in the Windows platform. This method recorded the sequence of Windows application programming interface (API) calls made by each of the processes in the system. A machine-learning algorithm was used to detect ransomware by matching the observed sequence of API calls against known patterns. Al-rimy et al. [14] proposed a three-stage ensemble-based classification model to train and test the samples. In the first stage, a novel incremental-bagging technique was used to divide the corpus into several sub-corpora. The second stage identified and extracted the most informative features from each of the data subsets and constructed feature subspaces using semi-random subspace-selection techniques, which in turn helped the system maintain a high degree of diversity between the sub-datasets without compromising accuracy. Finally, each of the feature subspace was trained on a pool of heterogeneous base classifiers, and the results were combined to achieve maximum detection accuracy. A similar work was presented by Shaila et al. [15] to extract the intrinsic attacking characteristics of ransomware samples using a deep-learning-based semi-supervised technique. The authors experimented with different hidden-laver configurations along with diferent numbers of features. Finally, they concluded that the system designed using 1024 nodes in each layer and trained using 15,972 global features were able to detect ransomware with high accuracy. Most of the process-centric approaches are designed based on the behavioural patterns of ransomware gathered in controlled-analysis environments. These methods fall short in detecting ransomware that executes at specific times or is waiting for users to perform specific actions. Further, these methods cannot detect ransomware that replaces API call names with their corresponding hashed values or other masking techniques.

The data-centric approach monitors how user data are accessed and modified in the underlying system. An appropriate warning is issued when the method detects suspicious changes in the user data due to ransomware activities. Continella et al. [9] developed ShieldFS, which monitored the low-level file I/O activities in a system to dynamically detect ransomware attacks. In addition, this method proposed a selfhealing mechanism to recover the infected files. The authors employed the incremental multi-tier classification method to improve the speed of ransomware detection. The method triggered a classifier based on a fraction of the files accessed by a process or group of processes instead of being based on time. This feature however limits it from detecting ransomware that operates by injecting code in one or more benign host processes that have already accessed a substantial portion of the files in a system. Scaife et al. [3] proposed the CryptoDrop method, which used six indicators, including similarity measurement, entropy measurement, and filetype changes, to detect ransomware attacks. CryptoDrop alerts the user and blocks the process when it identifies suspicious activity. Most data-centric methods fail to distinguish user actions from patterns of ransomware actions, which in-turn lead to high false-positive predictions. In addition, these methods fail in detecting cryptoransomware that encrypts only a portion of a file or leaves lower en cryption traces.

The resource-centric approach evaluates parameters extracted from computational resources in the underlying system. Upon detecting variations in the usage pattern of the resources and when these variations signify a ransomware attack, this method issues an alert. Rhode et al. [11] proposed an early-stage ransomware-prediction method using recurrent neural networks (RNNs). This method observes the changes that happen in the computer using nine system parameters, including CPU usage, packets sent, and packets received. According to these observations, they developed an RNN model that could detect a malware infection in the system at an earlier stage. Further, the authors have empirically proven that the RNN outperformed other conventional machine-learning algorithms. However, they did not explain the ra tionale behind the feature selection and how the selected features contributed to high accuracy and faster detection of the malware. Kolodenker et al. [10] developed PayBreak to protect victims from hybrid crypto-system ransomware without paying the ransom. The authors used hooks to redirect the procedures intended to access the cryptographic functions of the system. Further, security keys and other parameters used in the encryption were extracted from the redirected function call, and they were safely exported to the escrow system. After a successful capture of sensitive credentials, the control returns back to the original cryptographic function to resume normal operation. At any point in time, when the method detects the user machine infected by the ransomware, the security credentials stored in the escrow are retrieved to recover the infected user files. Monitoring the system resources to detect a ransomware attack is a cumbersome process because of the dificulty in detecting the underlying causes. Often, these methods result in false-positive predictions mainly because of the be nign application behavioural resemblance to malicious programs.

Malware that uses fingerprinting capability understands the execution environment and evades the sandbox analysis or security tool by not revealing its true identity. Most of the dynamic analysis-based methods fall short in detecting ransomware that changes its char acteristics based on its execution context. The present paper proposes a dynamic analysis-based ransomware-detection method carefully de signed to overcome the limitations of existing approaches. Table 1 lists the features of the proposed method and compares them with those of the other related works. These features include monitoring anomalies in the usage pattern of the system resources, monitoring illegitimate ac cess of the user files, attempting to gain persistent access in the system, and detecting ransomware variants that adopt any of the packing techniques, use a rootkit to trespass higher protection ring, and operate using the multithreading technique.

## 3. System designs

The proposed method identifies a ransomware attack based on the changes that occur in the computer system. These changes significantly deviate from normal usage patterns of the system and match the distinctive behavioural pattern of the ransomware. To facilitate this identification, we have designed an FSM model in which the states represent the current state of the computer system and the transitions between states are caused by system events that are subject to specified conditions. The proposed method consists of two modules, namely, behaviour-analysis and decision-making modules as shown in Fig. 1. The behaviour-analysis module monitors the utilisation, persistence, lateral movement of files, and system resources using corresponding listeners. The listeners trigger a transition between states in the FSM model when they observe significant changes in the system. The decision-making module deploys the state-change listener to keep track of the changes that occur in the system and issues notification when the FSM transitions indicate a possible ransomware attack. On receiving the notification, the decision-making module alerts the user for necessary action and attempts to stop the liable processes.

## 4. Behaviour analysis

The behaviour-analysis module observes the changes that happen in a computer system using four components. These components trigger the corresponding handlers when the module detects abnormalities in the usage patterns of user files, lateral movement of files, usage of system resources, and retention state of the applications. This section presents in detail the operation of each of the four components along with their corresponding event listeners.

## 4.1. Monitoring user files

The crypto-type ransomware takes advantage of the users and encrypts large numbers of files in the system. The encrypted files are further renamed, deleted, or created as new files depending on the variant of the ransomware that infects the system.

This component monitors the changes that happen in the user files using the file-system watcher object and triggers the handler when the changes are found to be suspicious. The watcher object raises an event when it receives a file-system-change notification. This notification in. dicates that a change occurs either in the files or in the directory. This sequence of events is listened by the filter section of this component, and all properties of the events, such as the name of the file, path, and change type, are recorded. These details are utilized by the module to determine the presence of suspicious activities. The handler section is triggered when the module detects that the number of files deleted, renamed, or created using a similar extension across all drives by a process or set of processes exceeds the threshold limit [4]. Upon detecting a suspicious activity, the handler section forwards a statechange request to the decision-making module as shown in Fig. 2.

Table 1  
Comparison with related studies.

<table><tr><td>Reference</td><td>Resource monitoring</td><td>File access control</td><td>Gaining persistence</td><td>Code obfuscation</td><td>Privilege escalation</td><td>Time-based detection</td></tr><tr><td>Continella et al. [9]</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Scaife et al. [3]</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Cabaj and Mazurczyk [2]</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Kolodenker et al. [10]</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Hampton et al. [6]</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Rhode et al. [11]</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Al-rimy et al. [14]</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Shaila et al. [15]</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Our Work</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

![](/api/attachments/89X4XWEF/fulltext/images/a93c1324123ef909dcb8f7920333c686eda86076a79afe954be42b1f829a4295.jpg)  
Fig. 1. Ransomware detection system.

![](/api/attachments/89X4XWEF/fulltext/images/2eb775df1a41cf5836dc3c30d78af98b88acde5a49e7daec90d73c81fcb8308f.jpg)  
Fig. 2. Monitoring user files - sequence of activities.

## 4.1.1. Threshold measurement

Ransomware reads the user files across all drives and writes them into a corresponding encrypted form. Most of these encrypted files are considered entropically secure because extracting any useful informa tion from the ciphertext is made computationally infeasible. These files usually have high entropy distribution compared with regular user files owing to its evenly distributed content. This ransomware property is exploited to determine its threshold value.

A process or set of processes involved in either read or write file operation will be considered for the evaluation. The entropy $e _ { r e a d }$ is derived from the file-read operations whereas the entropy $e _ { w r i t e }$ is derived from file-write, −rename, or -delete operations [3] as shown in Eq. (1).

$$
e = \sum_ {i = 0} ^ {2 5 5} P _ {x _ {i}} \log_ {2} \left(\frac {1}{P _ {x _ {i}}}\right)\tag{1}
$$

where each file is read as byte array and uncertainty in the probability distribution of the bytes is calculated. Here, $P _ { x i }$ represents probability of each byte over total number of bytes in the file. Also, the read and write entropy is averaged out both process-wide and system-wide for every 500 ms. The module triggers the handler when $A \nu e r a g e ( e _ { w r i t e } )$ exceeds Average(e ) at any point in time.

## 4.2. Lateral-movement tracking

Ransomware usually secretly and stealthily enters into a system to evade the system security. Cybercriminals commonly adopt social engineering tactics to drop the ransomware and other malicious executables into the target machines over e-mails, bots, or drive-by downloads. The downloaded executable files are usually distributed with spoofed icons, which look similar to a familiar file in the system. In addition, they persuade the user to open the file with the intention of infecting the system. For example, the executables are distributed using the name invoice.pdf.exe in which the Windows operating system hides the extension of the file by default and the file appears as invoice.pdf. This behavioural pattern of ransomware is monitored by the lateralmovement-tracking component. The properties of the files that enter the system from foreign sources are recorded, and operations are monitored for a defined period of time. This component forwards the state-change request to the decision-making module when it detects suspicious execution files. Any execution file that is preceded by one or more valid file extensions is considered suspicious. Furthermore, this module attempts to remove such suspicious files from the system.

In this component, we use kernel-mode programming to monitor and control the operations of the suspicious files. The ‘ZwQueryDirectoryFile’ routine is used along with the instance of FileHandle attribute to access the files that exist in a specific directory of the target machine. The FileInformation Classes are used to extract the file meta information, and the details are further used to analyse the suspiciousness of the files. On a successful detection of the malicious files, this component initiates the state-change request and uses the ‘ZwDeleteFile’ routine to remove the specific file.

## 4.3. Monitoring system resources

This component monitors the utilisation of system resources, specifically the system-restore feature and activities performed by the running processes. If any process either attempts to change the system restore settings or stops large numbers of processes, then this module initiates the state-change request and forcibly stops the suspicious process.

The system-restore functionality of Microsoft Windows facilitates reverting the system state to any of the previous stable states, which helps the system recover from malfunctions and other malware attacks. The ransomware usually harms the system by disabling the restore feature to ensure that the system cannot revert to the stable state. This component monitors the restore configuration values stored in the path ‘SOFTWARE\Microsoft\Windows NT\Current Version \SystemRestore of the system registry. If any process attempts to change the config uration values, this component initiates the state-change request.

Similarly, the ransomware stops the active processes in the system to facilitate encrypting the corresponding files. The system raises a state-change request when it detects abnormal termination of large numbers of active processes in the system in a short time interval (500 ms).

## 4.4. Persistence of active program

The ransomware is designed to persist between system reboots to complete the attack cycle. To ensure that the persistence ransomware adds the location of the malicious executable file as a key value in the path of the Windows registry. For instance, ransomware update values in the following path to persist.

## HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\ Random< >

## HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\ Random< >

Some ransomware variants add the path of the malicious executable files in the start-up directory of the AppData folder of the user. This component periodically monitors the entries in the Run registry as well as the Startup file-system directory. Upon finding a new entry either in the Run registry or Startup directory, it issues a state-change request. To achieve this, we use the WqlEventQuerry routine to retrieve the data in the specified registry path. Further, delegate function eventHandler and listener ManagementEventWatcher are used to handle the change events in the registry.

Each of the processes related to this module is supervised by an external dedicated process to prevent tampering by the ransomware or any of the user-mode processes. These processes are developed as a protected process with the help of the Filesystem Minifilter Driver framework. The Minifilter custom driver is attached to the Windows onload and registers itself to the Filter Manager to filter the chosen I/O operations. Each I/O request packet (IRP) is a complex data structure that is used by the OS to communicate with the kernel-mode driver. This data structure primarily contains information about the Process Name, Requestor Mode, Operation Type, Filesystem Path, and many others. Through the Minifilter driver, the proposed method can observe and filter all IRPs generated from the user-mode processes. The dedicated process denies all IRP requests that are generated from the usermode applications that attempt to access the protected processes.

## 5. Decision-making module

This module listens to the events generated by the other modules in the system and determines the possibility of a ransomware attack. The state-change listener and FSM model components are deployed to listen and analyse the events, respectively.

## 5.1. FSM model

The FSM model proposed in this paper represents the behavioural traits consistently exhibited by the ransomware in the underlying computer system. This model was developed based on the literature [5–7] and technical reports and by manually observing the behavioural patterns of the ransomware by executing it in a controlled environment. The current study aims to observe the operations that elicit the special behavioural patterns of the ransomware, which include aspects of the ransomware that regulates its functional and structural changes introduced into the system during interplay and the masquerading techniques used to survive.

FSM is a mathematical model that consists of states and transitions. The state in the FSM model represents the current state of the system, and transitions are made between the states based on the set of actions and responses of the system. The responses show the changes that occur in the system in terms of a possible ransomware attack. A transition to any of the final states in a specific sequence indicates that the system is under a ransomware attack.

The behavioural patterns of the ransomware are represented in an FSM form, as shown in $\mathrm { F i g . } 3 . \mathrm { A }$ completely specified FSM is defined as $M = ( Q , S _ { 0 } , X , Y , \delta , F )$ , where;

• Q is a finite set of states, and $S _ { 0 }$ represents the initial state.

• X is a set of causes that represents the sources of the ransomware attack.

• Y represents a finite set of system responses initiated by the cause.

• δ is a state transition function that maps the state and test-case pairs (∑) to other state $Q \times \Sigma  Q$ . This transition indicates the change in the system state due to malicious activity.

• Frepresents the set of final states, where $F \in Q .$

A system is confirmed to be under a ransomware attack when the FSM model transition reaches any of the final states $\{ S _ { 1 } , S _ { 4 } , S _ { 6 } \}$ from initial state $\mathsf { S } _ { 0 } .$ A state transition occurs for every test case (t), and it is represented as a combination of the cause (X) and its corresponding response (Y) pair〈cause, response〉. The causes are listed in Table 2, which represent the root cause of the ransomware attack that might be a file downloaded from the Web or an infectious active process entering from external sources such as a local network or plug-and-play devices.

The changes that occur in the system due to these causes are represented as response in the transition label, and the list of possible responses is listed in Table 3. These responses are identified using the corresponding modules presented in Section 4.

The combination of these transition labels forms a finite nonempty input alphabet set, namely, $\Sigma ~ = ~ \langle X _ { 1 } , Y _ { 1 } \rangle . . . \langle X _ { m } , Y _ { n } \rangle$ , which in turn characterises the cases of a ransomware attack. For example, if a system is assumed to be in state $S _ { 0 }$ and if it receives a create-file notification from the monitoring user files section, it indicates that an active process $\left( X _ { 2 } \right)$ attempts to create massive numbers of new files $\left( Y _ { 3 } \right)$ . This causeand-response pair of request $\langle X _ { 2 } , Y _ { 3 } \rangle$ initiates state transition from $S _ { 0 }$ to $S _ { 3 }$ in the model, as expressed in Eq. (2).

$$
S _ {1} = \delta_ {1} (S _ {0}, \langle X _ {2}, Y _ {3} \rangle)\tag{2}
$$

The generic form of the FSM mapping function is expressed in $\operatorname { E q . }$ (3)

$$
S _ {n} = \delta_ {n} (\delta_ {n - 1} (S _ {0}, \sum))\tag{3}
$$

![](/api/attachments/89X4XWEF/fulltext/images/be16089f87494ee49c637f2b0905a4591ee37208d10ccdb36c10e4dfcc19f389.jpg)  
Fig. 3. FSM model representing the behavioural patterns of ransomware.

Table 2

<table><tr><td>Causes (X)</td><td>Description</td></tr><tr><td> $X_1$ </td><td>File downloaded through various sources such as e-mail, drive by downloading and chat bot</td></tr><tr><td> $X_2$ </td><td>Active process</td></tr></table>

Table 3  
List of responses.

<table><tr><td>Response (Y)</td><td>Description</td></tr><tr><td> $Y_1$ </td><td>Files with suspicious extensions such as .doc.exe, .pdf.exe, and .txt.exe</td></tr><tr><td> $Y_2$ </td><td>Registry key entry to ensure payload persistence</td></tr><tr><td> $Y_3$ </td><td>Created encrypted documents exceed the threshold limit with a suspicious extension such as .pdf.WNCRY and .mp3.WNCRY</td></tr><tr><td> $Y_4$ </td><td>System and user files deleted as a consequence of  $Y_3$ .</td></tr><tr><td> $Y_5$ </td><td>Active-system processes terminated</td></tr><tr><td> $Y_6$ </td><td>Number of modified files exceeds the threshold limit</td></tr><tr><td> $Y_7$ </td><td>Shadow copies of Windows deleted by disabling the system-restore functionality</td></tr></table>

## 5.2. State transition

The state sequences listed in Table 4 present the distinct beha vioural characteristics of the ransomware in a system.

## 5.3. Stage-change listener

The state-change listener is part of the FSM model. It monitors and records the state transitions in the FSM model. For every transition, it checks whether the current state $( \mathsf { S } _ { \mathrm { n } } )$ of the system matches any of the final states $( S _ { 1 } , S _ { 4 } , S _ { 6 } )$ . Upon detecting a successful transition match, it alerts the user with a message and forcibly terminates all the process by leaving the essential processes in the system.

## 6. Implementation and evaluation

## 6.1. Implementation

The proposed ransomware-detection system was developed as a Windows application in C# using Microsoft Visual Studio 2013 with Windows Driver Kit 10. The behavioural patterns of the ransomware was observed and analysed in an autonomous system using 64-bit Windows 7 guest OS installed in Oracle Virtual Box 5.0.40. We installed. NET Framework 4.5.2 in the guest OS to facilitate execution of the proposed protection system. Because ransomware precisely targets the user data, we manually created folders and pushed documents with .doc, .pdf, .mp3, .ppt, and .txt extensions into the root drive, desktop, and My Document sections of the system. Under these settings, we manually executed the ransomware samples obtained from various repositories specified in Section 6.2.

The ransomware behaviour is logged as follows: 1) executing each of the samples in the automatic fully configured malware-analysis system [19], 2) executing the samples in a bare metal system - only the ransomware samples that operate in the user mode, 3) verifying and cross-checking each sample using VirusTotal, and 4) submitting executables to the ThreatExpert system to investigate the changes that are caused by the threats in the OS. We designed the FSM model according to the observed behavioural patterns of the ransomware.

## 6.2. Description of the dataset

To assess the prediction accuracy of the proposed method, we collected a dataset that consisted of 1975 samples. Specifically, this dataset included 1500 legitimate applications as well as 475 ransomware samples collected from online sources over a period of 12 months. Table 5 lists the family-wise ransomware counts used in the evaluation.

The active ransomware samples were obtained from two diferent data sources, as listed in Table 6. This dataset included a representative of most prevalent ransomware families such as Cerber, CryptLocker, CryptoWall, WannaCry, and Lock Screen.

Table 4  
Ransomware test scenarios.

<table><tr><td>States</td><td>Test cases</td><td>Scenario</td></tr><tr><td> $S_0 \rightarrow S_1$ </td><td> $\langle X_1, Y_1 \rangle$ </td><td>The file is downloaded from the Internet with a suspicious extension. Attackers commonly spoof the file extensions intended to inject malicious executables into the user machine. (This case only confirms the download as a malware.)</td></tr><tr><td> $S_0 \rightarrow S_2 \rightarrow S_3 \rightarrow S_4$ </td><td> $\langle X_2, Y_2 \rangle, \langle X_2, Y_3 \rangle, \langle X_2, Y_4 \rangle$ </td><td>The active process adds the Registry keys to ensure persistence between system restarts. This facilitates malicious processes to create the encrypted version of the user documents and delete the original files across all drives in multiple sessions.</td></tr><tr><td> $S_0 \rightarrow S_2 \rightarrow S_5 \rightarrow S_6$ </td><td> $\langle X_2, Y_2 \rangle, \langle X_2, Y_5 \rangle, \langle X_2, Y_6 \rangle$ </td><td>The active process adds the Registry keys to ensure payload persistence. These processes forcibly terminate the active-system processes to facilitate modification of the related files.</td></tr><tr><td> $S_0 \rightarrow S_7 \rightarrow S_5 \rightarrow S_6$ </td><td> $\langle X_2, Y_7 \rangle, \langle X_2, Y_5 \rangle, \langle X_2, Y_6 \rangle$ </td><td>The active process disables the system-restore functionality of Windows by affecting the shadow copies. Further, it forcibly terminates the active-system processes to facilitate modification of the related files into the encrypted version.</td></tr><tr><td> $S_0 \rightarrow S_5 \rightarrow S_6$ </td><td> $\langle X_2, Y_5 \rangle, \langle X_2, Y_6 \rangle$ </td><td>The active process terminates the active-system processes to facilitate modification of a massive number of existing files into the encrypted version.</td></tr><tr><td> $S_0 \rightarrow S_7 \rightarrow S_6$ </td><td> $\langle X_2, Y_7 \rangle, \langle X_2, Y_6 \rangle$ </td><td>The active process disables the system-restore functionality of Windows by affecting the shadow copies. Further, it modifies the content of the user files into the encrypted content.</td></tr><tr><td> $S_0 \rightarrow S_3 \rightarrow S_4$ </td><td> $\langle X_2, Y_3 \rangle, \langle X_2, Y_4 \rangle$ </td><td>The active process creates a massive number of encrypted user files and deletes the corresponding original files across all drives. This activity of the malicious process hampers recovery of the original files.</td></tr><tr><td> $S_0 \rightarrow S_6$ </td><td> $\langle X_2, Y_6 \rangle$ </td><td>The active process rewrites the content of a massive number of user files into an encrypted content.</td></tr></table>

The legitimate applications were collected from the data sources listed in Table 7. We manually confirmed that all applications in the legitimate dataset are popular and contains no suspicious components using VirusTotal.

## 6.3. Metrics used in the evaluation

The true positive rate (TPR), false negative rate (FNR), and accuracy metrics were used to evaluate the performance of our proposed system.

TPR is computed using Eq. (4). This metric computes the ratio of successfully identified ransomware attacks by the proposed system to all tested ransomware samples.

$$
T P R = \frac {M _ {r \rightarrow r}}{(M _ {r \rightarrow r} + M _ {r \rightarrow l})}\tag{4}
$$

where the notations $M _ { l  l }$ and $M _ { r  r }$ represent the correctly identified samples and notations $M _ { l  r }$ and $M _ { r  l }$ represent the wrongly identified samples by our proposed system.

FNR measures the ratio of ransomware samples not identified by the proposed system or considered as legitimate applications. FNR is computed using Eq. (5).

$$
F N R = 1 - T P R\tag{5}
$$

The false positive rate (FPR) calculates the rate of legitimate applications that are wrongly identified as ransomware samples, as expressed in Eq. (6).

$$
F P R = \frac {M _ {l \rightarrow r}}{M _ {l \rightarrow l} + M _ {l \rightarrow r}}\tag{6}
$$

The true negative rate (TNR) calculates the ratio of successfully identified legitimate applications, as expressed in Eq. (7).

$$
T N R = 1 - F P R\tag{7}
$$

Accuracy calculates the ratio of correctly identified samples, which includes both the ransomware and legitimate applications, to all tested samples, as expressed in Eq. (8).

$$
\mathrm{ACC} = \frac {M _ {l \rightarrow l} + M _ {r \rightarrow r}}{M _ {l \rightarrow l} + M _ {l \rightarrow r} + M _ {r \rightarrow r} + M _ {r \rightarrow l}}\tag{8}
$$

## 6.4. Ransomware analysis

The detection accuracy of the proposed method was evaluated by injecting the ransomware and legitimate applications into the guest OS. We observed warning messages raised by the proposed method between the computer system reboot and computed metrics, which are

## Table 5

Malware samples.

<table><tr><td>Sl. No.</td><td>Ransomware Family</td><td>Count</td><td>Sl. No.</td><td>Ransomware Family</td><td>Count</td><td>Sl. No.</td><td>Ransomware Family</td><td>Count</td></tr><tr><td>1</td><td>73V3N</td><td>4</td><td>23</td><td>Paradise</td><td>2</td><td>45</td><td>Krotten</td><td>2</td></tr><tr><td>2</td><td>Anatova</td><td>12</td><td>24</td><td>Petya</td><td>5</td><td>46</td><td>LockerGoga</td><td>5</td></tr><tr><td>3</td><td>BitStak</td><td>2</td><td>25</td><td>PowerWare</td><td>6</td><td>47</td><td>Locky</td><td>12</td></tr><tr><td>4</td><td>Cerber</td><td>10</td><td>26</td><td>PyLocky</td><td>20</td><td>48</td><td>LooCipher</td><td>3</td></tr><tr><td>5</td><td>Chimera</td><td>3</td><td>27</td><td>Radamant</td><td>7</td><td>49</td><td>Manamecrypt</td><td>3</td></tr><tr><td>6</td><td>Critroni</td><td>2</td><td>28</td><td>Reveton</td><td>3</td><td>50</td><td>Matrix</td><td>4</td></tr><tr><td>7</td><td>CryBola</td><td>3</td><td>29</td><td>Ryuk</td><td>4</td><td>51</td><td>MBRLocker</td><td>1</td></tr><tr><td>8</td><td>CryLocker</td><td>2</td><td>30</td><td>Samsam</td><td>4</td><td>52</td><td>MegaCortex</td><td>5</td></tr><tr><td>9</td><td>CryptoBit</td><td>8</td><td>31</td><td>Saturn</td><td>5</td><td>53</td><td>Nemucod</td><td>2</td></tr><tr><td>10</td><td>CryptoWall</td><td>17</td><td>32</td><td>SkidLocker/Pompus</td><td>3</td><td>54</td><td>Noblis</td><td>4</td></tr><tr><td>11</td><td>CryptXXX</td><td>29</td><td>33</td><td>Sodinokibi</td><td>8</td><td>55</td><td>NoobCrypt</td><td>2</td></tr><tr><td>12</td><td>CrySiS</td><td>4</td><td>34</td><td>Spider</td><td>3</td><td>56</td><td>NotPetya</td><td>5</td></tr><tr><td>13</td><td>CTB-Locker</td><td>16</td><td>35</td><td>Syrk</td><td>5</td><td>57</td><td>NullByte</td><td>2</td></tr><tr><td>14</td><td>DirtyDecrypt</td><td>3</td><td>36</td><td>T1 Happy</td><td>3</td><td>58</td><td>PadCrypt</td><td>3</td></tr><tr><td>15</td><td>eCh0raix</td><td>2</td><td>37</td><td>TeleCrypt</td><td>1</td><td>59</td><td>HiddenTear</td><td>2</td></tr><tr><td>16</td><td>EDA2</td><td>18</td><td>38</td><td>TeslaCrypt</td><td>15</td><td>60</td><td>HydraCrypt</td><td>4</td></tr><tr><td>17</td><td>Fabiansomware</td><td>2</td><td>39</td><td>WannaCry</td><td>13</td><td>61</td><td>IEncrypt</td><td>2</td></tr><tr><td>18</td><td>Fantom</td><td>5</td><td>40</td><td>WinLock</td><td>1</td><td>62</td><td>Globe</td><td>10</td></tr><tr><td>19</td><td>Fluffy</td><td>2</td><td>41</td><td>Jigsaw</td><td>6</td><td>63</td><td>Gpcode</td><td>6</td></tr><tr><td>20</td><td>Forma</td><td>4</td><td>42</td><td>JobCrypter</td><td>11</td><td>64</td><td>Hermes</td><td>13</td></tr><tr><td>21</td><td>GandCrab</td><td>16</td><td>43</td><td>KeRanger</td><td>10</td><td>65</td><td>KillLocker</td><td>3</td></tr><tr><td>22</td><td>KillRabbit</td><td>3</td><td>44</td><td>KrakenXXX</td><td>28</td><td>66</td><td>UNCLASSIFIED</td><td>52</td></tr></table>

Table 6  
Malware-sample data sources.

<table><tr><td>Sl.No</td><td>Source</td><td>No. of samples</td><td>Links</td></tr><tr><td>1</td><td>ytisf/theZoo</td><td>45</td><td>https://github.com/ytisf/theZoo/tree/master/malwares</td></tr><tr><td>2</td><td>Virus Total - Intelligence Search Engine</td><td>430</td><td>https://www.virustotal.com/</td></tr></table>

Table 7  
Legitimate application data sources.

<table><tr><td>Sl. No</td><td>Source</td><td>No. of samples</td><td>Link</td></tr><tr><td>1</td><td>Most popular software for Windows</td><td>300</td><td>http://software.informer.com/software/</td></tr><tr><td>2</td><td>File forum</td><td>390</td><td>https://fileforum.betanews.com/</td></tr><tr><td>3</td><td>Major geeks</td><td>417</td><td>http://www.majorgeeks.com/</td></tr><tr><td>4</td><td>Softpedia</td><td>393</td><td>http://www.softpedia.com/</td></tr></table>

<table><tr><td></td><td>Ransomware Sample</td><td>Legitimate sample</td></tr><tr><td>Classified as Ransomware</td><td>TP=466</td><td>FP=0</td></tr><tr><td>Classified as Legitimate</td><td>FN=9</td><td>TN=1500</td></tr></table>

Fig. 4. Confusion matrix of the experimental results.

presented in details in Section 6.3. This section presents a short description of the various characteristics exhibited by two popular ran somware samples WannaCry and Cerber.

The WannaCry and Cerber ransomware were considered to be the most damaging threats in the year 2018 [8]. These threats are manually injected into the system, and the observations are presented in detail in this section. The changes that occurred while enabling the proposed protection system were also observed.

## 6.4.1. Behavioural analysis of the WannaCrypt0r ransomware

When the WannaCrypt0r ransomware was activated, the following notable changes were observed in the system. The ransomware started creating an encrypted version of the user documents across all drives in the system. New files were created with the extension. WNCRY. For instance, it created a new file named ‘sample.txt.WNCRY’ for existing file ‘sample.txt’. After creating these new files, the ransomware deleted the original files from the system. The mentioned changes happened in all user files that were part of following directories.

/Users/ username /mydocuments, /Users/ username /mydocuments/ folders< > < > < >

/Users/ username /desktop, /Users/ username /desktop/ folders< > < > < >

/Users/ username /pictures, /Users/ username /Appdata/temp< > < >

In addition, this ransomware encrypted all the files detected in the Windows thumbnail cache directory, but the original files were not deleted. From this analysis, the ransomware evidently targeted the user documents, instead of the system, because the ransomware was supposed to have a decrypting tool work in the system to facilitate retrieving the user files. A ransom note was provided by the attackers with the instructions that mentioned the mode and address of payment as well as the method of recovery.

This ransomware created a loader executable named tasksche.exe in the desktop when the malicious dropper file was manually executed. The tasksche executable downloaded the necessary modules from the Internet to facilitate the successful encryption process. To ensure persistence of the loader, it created the following key-value pair entry in the Windows registry:

Key: HKEY\_CURRENT\_USER\Software\Microsoft\Windows\Current Version\Run\ nkromzsbgcqr645.

![](/api/attachments/89X4XWEF/fulltext/images/9d8675f02a5012a9647b2ed1bb182ed69f22c59aec528682c5259925af7d9fe5.jpg)  
Fig. 5. Assessment of the results.

Table 8  
Comparison among ransomware methods.

<table><tr><td>Ransomware-detection method</td><td>No. of legitimate samples</td><td>No. of ransomware samples</td><td>Total</td><td>TPR (%)</td><td>FPR (%)</td><td>FNR (%)</td><td>Accuracy (%)</td></tr><tr><td>Continella et al. [9]</td><td>2245</td><td>305</td><td>2550</td><td>97.70</td><td>1.5</td><td>2.3</td><td>98.43</td></tr><tr><td>Lu et al. [12]</td><td>1000</td><td>1000</td><td>2000</td><td>90</td><td>10</td><td>10</td><td>90</td></tr><tr><td>Hampton et al. [6]</td><td>Nil</td><td>103(13 families)</td><td>103</td><td>-</td><td>-</td><td>-</td><td>95</td></tr><tr><td>Al-rimy et al. [14]</td><td>Nil</td><td>8152(from year 2013 onwards; considered crypto-ransomware samples)</td><td>8152</td><td>98.1</td><td>1.85</td><td>-</td><td>97.89</td></tr><tr><td>Shaila et al. [15]</td><td>Nil</td><td>14 families</td><td>1232</td><td>97.69</td><td>0.66</td><td>2.3</td><td>95.96</td></tr><tr><td>Our method</td><td>1500</td><td>475</td><td>1975</td><td>98.1</td><td>0</td><td>1.9</td><td>99.54</td></tr></table>

Value: C:\Users\anjalee\Desktop\tasksche.exe.

A new copy of guest OS was installed with the specified configurations along with the necessary software to facilitate running our proposed protection system. Further, the WannaCry ransomware was manually activated by triggering the malicious dropper file. The per sistence of the active program module detected the addition of a reg istry key in the specified path and raised an event for the state change from $S _ { 0 }$ to $\mathbf { S } _ { 2 } .$ In addition, the watcher object of the monitoring user file module raised, created, and deleted the file events, which in turn triggered state changes from $S _ { 2 }$ to $S _ { 3 }$ and $S _ { 3 }$ to $\mathsf { S } _ { 4 } .$ This sequence of events confirmed that the system was under a ransomware attack in which a warning message was subsequently issued to the user.

## 6.4.2. Behavioural analysis of the Cerber 5 ransomware

The Cerber ransomware was manually launched by triggering malicious dropper file PDFWriter.EXE. It created a window executable file with a random name in the %AppData% section of the system. The ransomware terminated some of the active processes in the system to facilitate the encryption operation. Further, it replaced the content of existing files into an encrypted content across all drives and renamed the files using random extensions such as. BBxx, where xx represents a numerical value. Unlike WannaCry, the Cerber neither created new files nor deleted the original files from the system. In contrast, the content of the plain text files was not modified by the ransomware. The afected file types and thumbnail images of the original file were recovered manually in the Linux system, but decoding its content failed. A ransom note was provided in every directory to allow the victims to regain access. Cerber also spread from the guest Windows OS to the host Linux OS through the temporarily mounted network drive and afected the files in the host system.

A new copy of the guest OS was installed along with our proposed protection system. Further, the Cerber ransomware was manually activated by triggering the malicious dropper file. The monitoring system resource module detected the termination of the processes and raised an event for the state change from $S _ { 0 }$ to $S _ { 5 } .$ In addition, the monitoring user file module detected modifications in massive numbers of user files across all drives. It also triggered the decision-making module for the state change from $S _ { 5 }$ to $S _ { 6 } .$ This sequence of events confirmed the ransomware attack, and a warning message was issued to the user.

## 6.5. Ransomware detection accuracy

The proposed system correctly detected 466 ransomware samples out of the considered 475 samples. During the evaluation, the system did not raise any false warning on the legitimate applications con sidered for evaluation, as shown in Fig. 4. These results clearly indicate that the proposed method could detect the ransomware with 99.5% accuracy and 0% false positive, as shown in Fig. 5.

The proposed method is compared with other dynamic-analysis based ransomware-detection methods, as listed in Table 8. The samples that we considered for evaluation are live and active samples. The results clearly indicate that our method demonstrates more advantages than the other methods. The results listed in Table 8 were obtained from the respective published papers.

## 7. Discussion

The proposed system was built on the behavioural observation of various ransomware variants. Thus, the system was able to accurately identify most of the ransomware variants but failed to raise alerts for some of the ransomware samples considered in the testing. We observed that due to any of the following reasons, the system misclassified the ransomware samples.

• The method was designed to identify the malware that entered into the system through e-mail attachments but did not recognise payloads that entered through other stealthy techniques.

Nine samples were left undetected by the proposed system, which resulted in 1.9% FNR. The main reason for the FNRs was that the dataset consisted of ransomware that belongs to many diferent fa milies as well as variants. Few ransomware that use more sophisticated code-obfuscation and incremental unpacking techniques are capable of hiding their true identity. For instance, ransomware such as NotPetya operates on a user-level privilege, and because it does not attempt to modify any system resources, detecting it using the proposed monitoring system is dificult.

The proposed system failed to raise alerts when the ransomware infected the system either without afecting the system resources or without encrypting the user files. The ‘Lock Screen’ ransomware primarily held the user interface in the OS as a hostage.

## 8. Conclusion

The proposed method detects ransomware attacks based on the changes that occur in the state of an underlying computer system. This method deploys four components along with the corresponding event listeners to monitor the utilisation, persistence, lateral movement of the system and user resources. Upon detecting suspicious activities, the corresponding component passes the notifications to the decisionmaking module. The FSM model is used in the decision making to analyse the events to detect ransomware attacks. The proposed method was tested using different variants of ransomware. The attention on the generic behavioural pattern of the ransomware achieved detection across a range of ransomware families and variants. The experimental results show that the proposed method eficiently detects ransomware attacks with 99.5% accuracy and 0% FPR.

## Acknowledgments

This work is supported by the Science and Engineering Research Board (SERB), Department of Science and Technology, Government of India. We highly acknowledge SERB for their support through ‘Early Career Research’ award (No. ECR/2018/001709). We sincerely thank all the faculties of CSE and CTS lab for their meticulous support. We also thank Mr.Anand R Nair for his assistance in the project.

## References

[1] A. Ali, Ransomware: a research and a personal case study of dealing with this nasty malware, Issues in Informing Science and Information Technology 14 (2017) 087–099.

[2] K. Cabaj, W. Mazurczyk, Using software-defined networking for ransomware mitigation: the case of cryptowall, IEEE Netw. 30 (6) (2016) 14–20.

[3] N. Scaife, H. Carter, P. Traynor, K.R.B. Butler, CryptoLock (and drop it): Stopping ransomware attacks on user data, 2016 IEEE 36th International Conference on Distributed Computing Systems (ICDCS), 2016, pp. 303–312.

[4] A. Kharraz, W. Robertson, D. Balzarotti, L. Bilge, E. Kirda, Cutting the gordian knot: A look under the hood of ransomware attacks, International Conference on Detection of Intrusions and Malware, and Vulnerability Assessment, Springer, Cham, 2015, pp. 3–24.

[5] D. Nieuwenhuizen, A Behavioural-Based Approach to Ransomware Detection, Whitepaper MWR Labs Whitepaper, 2017, https://labs.f-secure.com/assets/ resourceFiles/mwri-behavioural-ransomware-detection-2017-04-5.pdf

[6] N. Hampton, Z. Baig, S. Zeadally, Ransomware behavioural analysis on windows platforms, Journal of Information Security and Applications 40 (2018) 44–51.

[7] N.K. Popli, A. Girdhar, Behavioural analysis of recent ransomwares and prediction of future attacks by polymorphic and metamorphic ransomware, Computational Intelligence: Theories, Applications and Future Directions-Volume II, Springer, 2019, pp. 65–80.

[8] Y. Lena Connolly, D.S. Wall, The rise of crypto-ransomware in a changing cybercrime landscape: Taxonomising countermeasures, Computers & Security. 87 (2019 Nov 1) 101568.

[9] A. Continella, A. Guagnelli, G. Zingaro, G. De Pasquale, A. Barenghi, S. Zanero, F. Maggi, ShieldFS: A self-healing, ransomware-aware filesystem. Proceedings of the 32nd Annual Conference on Computer Security Applications, ACM, 2016, pp. 336-347.

[10] E. Kolodenker, W. Koch, G. Stringhini, M. Egele, PayBreak: Defense against cryptographic ransomware, Proceedings of the 2017 ACM on Asia Conference on Computer and Communications Security, 2017, pp. 599–611.

[11] M. Rhode, P. Burnap. K. Jones, Early-stage malware prediction using recurrent neural networks, Computers and Security 77 (2018) 578–594

[12] T. Lu, L. Zhang, S. Wang, Q. Gong, Ransomware detection based on v-detector negative selection algorithm, 2017 International Conference on Security, Pattern Analysis, and Cybernetics (SPAC), IEEE, 2017, pp. 531–536.

[13] Symantec, Internet Security Threat Report, vol. 24, (2019) https://www.symantec. com/content/dam/symantec/docs/reports/istr-24-2019-en.pdf (accessed January 9, 2020).

[14] B.A. Al-rimy, M.A. Maarof, S.Z. Shaid, Crypto-ransomware early detection mode using novel incremental bagging with enhanced semi-random subspace selection Futur. Gener. Comput. Syst. 101 (2019 Dec 1) 476–491

[15] Sharmeen Shaila, Y.A. Ahmed, S. Huda, B.Ş. Koçer, M.M. Hassan, Avoiding future digital extortion through robust protection against ransomware threats using deep learning based adaptive approaches, IEEE Access. 8 (2020 Jan 30) 24522–24534.

[16] B.A. Al-rimy, M.A. Maarof, S.Z. Shaid, Ransomware threat success factors, taxonomy, and countermeasures: a survey and research directions, Computers & Security. 74 (2018 May 1) 144–166.

[17] Berrueta Eduardo, D. Morató Osés, E. Magana Lizarrondo, M. Izal Azcarate, A survey on detection techniques for cryptographic ransomware, IEEE Access 7 (144925–144944) (2019).

[18] Damodaran Anusha, F. Di Troia, C.A. Visaggio, T.H. Austin, M. Stamp, A comparison of static, dynamic, and hybrid analysis for malware detection, Journal of Computer Virology and Hacking Techniques. 13 (2017 Feb 1) 1):1–2.

[19] O. Ori Or-Meir, N. Nissim, Y. Elovici, L. Rokach, Dynamic malware analysis in th modern era - a state of the art survey, ACM Computing Surveys (CSUR). 52 (5) (2019 Sep 13) 1–48

[20] C.R. Srinivasan, Hobby hackers to billion-dollar industry: the evolution of ransomware, Computer Fraud & Security. 2017 (11) (2017 Nov 1) 7–9.

[21] Chung Marcus, Why employees matter in the fight against ransomware, Computer Fraud & Security 2019 (8) (2019) 8–11.

[22] Kim DaeYoub. J. Lee, Blacklist vs. whitelist-based ransomware solutions, IEEE Consumer Electronics Magazine. Vol. 9. No. 3. Pp. 22–28. 1. May 2020.

![](/api/attachments/89X4XWEF/fulltext/images/0eb8e692f75fa9f8806a4852639446151ed7a1a0ddc6f9f1335e31c141fdb2e5.jpg)  
R. Gowtham is an Assistant Professor in the Department of Computer Science & Engineering at Amrita Vishwa Vidyapeetham, Coimbatore, India. He has obtained his B.E degree from Periyar University, M.E degree from Anna University and Ph.D under Anna University. His research interests are in the areas of Information security and Semantic Web

![](/api/attachments/89X4XWEF/fulltext/images/7d30fc1751922bc84046e9bf659e5aa4cf30206418de5dd97e263c4e333b6090.jpg)  
Anjali Menen received B.Tech degree in Computer Science and Engineering from Nehru College of Engineering and Research Centre, and M.Tech degree in Computer Science and Engineering from Amrita Vishwa Vidyapeetham, Amrita University, Coimbatore. Her research interests ar Semantic Web, Web Security and Data Analytics
