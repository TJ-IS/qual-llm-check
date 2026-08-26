---
otero_id: 1598
otero_key: "HRJ44KFB"
title: "Design Principles for Signal Detection in Modern Job Application Systems: Identifying Fabricated Qualifications"
authors: "Nathan W. Twyman; Steven J. Pentland; Lee Spitzley"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2020.1790201"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design Principles for Signal Detection in Modern Job Application Systems: Identifying Fabricated Qualifications

Nathan W. Twyman , Steven J. Pentland & Lee Spitzley

To cite this article: Nathan W. Twyman , Steven J. Pentland & Lee Spitzley (2020) Design Principles for Signal Detection in Modern Job Application Systems: Identifying Fabricated Qualifications, Journal of Management Information Systems, 37:3, 849-874, DOI: 10.1080/07421222.2020.1790201

To link to this article: https://doi.org/10.1080/07421222.2020.1790201

![](/api/attachments/HRJ44KFB/fulltext/images/852d3036ca4291bc095819fef7cc472de867f880d7d5109025ee02f9403865f0.jpg)

© 2020 The Author(s). Published with license by Taylor & Francis Group, LLC.

![](/api/attachments/HRJ44KFB/fulltext/images/e74a015fe57befc5e897d3cb96c0c80330f901404e854636a2971d57233bdcc2.jpg)

Published online: 18 Nov 2020.

View supplementary material

![](/api/attachments/HRJ44KFB/fulltext/images/e177acb59c4b8f7aca022f3468f04cecf3666edd41de8d225433cec6fa4ad0ad.jpg)

Article views: 119

![](/api/attachments/HRJ44KFB/fulltext/images/176ac75cacdc83b98cd60cf5a85da6d327f074301510dc2c3f7f5f451f81e1a2.jpg)

Submit your article to this journal

![](/api/attachments/HRJ44KFB/fulltext/images/021122a63a75601e1962112ca379e9a0e3249a34a9287ccb620ddb101ac1e656.jpg)

![](/api/attachments/HRJ44KFB/fulltext/images/fa6e116b1ecd5f6fbb938bc770e027a50fa84b249009b10bb27d8d4a34dadd15.jpg)

View related articles

![](/api/attachments/HRJ44KFB/fulltext/images/ceaed35e3a2b3826fe99dbecd3d7f3ef27f6b70acfd05bf61557dabe68a784c6.jpg)

View Crossmark data

∂ OPEN ACCESS

Check for updates

# Design Principles for Signal Detection in Modern Job Application Systems: Identifying Fabricated Qualifications

Nathan W. Twyman<sup>a</sup>, Steven J. Pentland<sup>b</sup>, and Lee Spitzley<sup>c</sup>

<sup>a</sup>Department of Information Systems, Marriott School of Business, Brigham Young University, Provo, UT, USA; <sup>b</sup>Information Technology and Supply Chain Management, College of Business and Economics, Boise State University, Boise, ID, USA; <sup>c</sup>Information Security and Digital Forensics, School of Business,University at Albany, State University of New York, Albany, NY, USA

## ABSTRACT

Hiring a new employee is traditionally thought to be an uncertain investment. This uncertainty is lessened by the presence of signals that indicate job fitness. Ideally, job applicants objectively signal their qualifications, and those signals are correctly assessed by the hiring team. In reality, signal manipulation is pervasive in the hiring process, mitigating the reliability of signals used to make hiring decisions. To combat these ineficiencies, we propose and evaluate SIGHT, a theoretical class of systems afording more robust signal evaluation during the job application process. A prototypical implementation of the SIGHT framework was evaluated using a mock-interview paradigm. Results provide initial evidence that SIGHT systems can elicit and capture qualification signals beyond what can be traditionally obtained from a typical application and that SIGHT systems can assess signals more efectively than unaided decision-making. SIGHT principles may extend to domains such as audit and security interviews.

## KEYWORDS

Signaling theory; jobapplication assessment; behavioral assessment; automated interviewing; virtual-agent-based interviewing; deception detection; human-risk assessment; NeuroIS; design science

## Introduction

Information systems (IS) research is trying to bring human behavior analytics to more decision makers in more places. This new generation of decision support systems is especially meaningful in situations where human behaviors cannot be manually examined, or where behavioral deviations are so slight that they require high-precision instruments to measure. IS scholars are increasingly leveraging day-to-day sensing instruments such as human-computer input devices [33] and standard video cameras [58] to capture and analyze human behaviors. The use of ubiquitous sensing instruments allows for remote collection and analysis and is essential in cases involving large volumes of human trafic.

The screening of large numbers of job applicants is an area that may benefit from human behavior analytics. Exaggeration and even overt deception are staples of this domain [44], making accurate candidate assessment dificult and at times even impossible. In the modern process, a large pool of candidates is filtered down to a small subset, consisting of those perceived to be most qualified. This filtering process relies on sending and receiving signals, or communications representing potential fitness. Job candidates demonstrate their competencies by sending signals related to education, work experience, technical knowledge, or many other characteristics believed to communicate fitness. Employers evaluate signals and determine which candidates possess optimal qualifications. This traditional process is prone to error because many applicants present exaggerated or false qualifications that can be dificult to verify. Discovering that a potential employee has unacceptably low competence, social skills, or cultural fit often requires interviews, and manipulation techniques can prevent even interviews from efectively identifying poor applicants [1]. For positions for which dozens or hundreds of applicants apply, interviewing all applicants is not feasible.

This phenomenon can be explained by signaling theory, which is perhaps easiest to understand in the natural systems domain: Biological organisms use shapes, colors, motions, or other features to “signal” (communicate) a particular property, such as danger or fitness. Some organisms take advantage of the system by using false signals to obtain the same benefits won by honest signalers. For instance, the red milk snake displays color patterns similar to that of the venomous coral snake, falsely signaling danger to potential predators. False signalers find success as long as the cost of testing the signal’s veracity remains suficiently high [19]. If deceptive signaling becomes pervasive enough, the signaling system fails because other organisms find they can no longer make efective assessments using that signal.

In some specialized domains, falsifying qualifications exacts too high a cost to job candidates for deception to become pervasive. However, in many domains, job applications have become rife with exaggeration and at times outright fabrication—to the point that efective assessments at the application-review stage are infeasible. Some desirable traits, such as integrity and social skills, are nearly impossible to assess at the application stage.

We therefore propose that in these cases, the typical candidate selection process can be appropriately conceptualized as a broken signaling system. A new, better system should provide an alternative means of evaluating candidate fitness at the application stage. We propose that to evaluate fitness, the new system should have minimal reliance on traditional signals of fitness—such as whether the application explicitly states the candidate possesses the desired skills or traits—and should instead rely on feasible alternative signals or the detection of false signals.

Starting from the application stage of the process, a new signaling system could provide reliable insight into key metrics, such as the competence, social skills, cultural fit, and integrity of a potential employee. The aim of this study is to propose a framework for such a system, implement a proof of concept, and evaluate the concept’s potential through experimentation. The result of this process is a type of signaling system that we term Systems for Identifying Genuine Hidden Talent (SIGHT). Traditional application systems are often undermined by their data-collection methods, with applicants’ traits and skills either self-reported or dificult to collect at all. SIGHT systems measure psychophysiological and behavioral signals that are less manipulable and thus more diagnostic. Although in this study we focus on signal manipulation during the job application process, the proposed SIGHT design principles may extend to many behavior assessment scenarios in which high volumes of applicants must be evaluated, such as policy compliance, visa applications, security screenings, and corporate audits.

## Research approach

The impetus for this research stemmed from an observation of major problems and opportunities in many high-volume hiring practices. Because the research question includes both a conceptualization of the problem and a potential solution, we selected a research approach that reflects what has come to be termed design science research (DSR). Conducting DSR usually involves implementing and evaluating specific solutions, [57] with the goal of identifying generalizable principles. Often this approach involves a program of research as principles are iteratively modified in successive studies—similar to agile development but on a broader scale [54]. The knowledge contribution of DSR typically involves both descriptive and prescriptive knowledge [29] and both practical and theoretical impacts.

To this end, this study begins with a description of an organizational problem. It then describes and prescribes a new type of system for the hiring process, aimed at addressing the problem. Then, the attributes, components, processes, and interrelationships required for the proposed type of system are outlined and justified at a high level. Finally, the construction and evaluation of an example prototype examine the concept’s potential. Accordingly, the knowledge contributions that will be expounded in this paper include the following: 1) a description of the problem, 2) a theoretical solution, and 3) evidence demonstrating the potential of that solution. The next section of this paper describes the problem and the theoretical solution. The succeeding sections describe the implementation and evaluation of the example prototype. The paper concludes with a discussion of the implications of these contributions.

## Signal theory and job candidate selection

The conceptualization of signaling theory has roots in economics [61]. Since signaling theory’s inception, the theory has been extensively applied in natural systems; it has also been applied in many organizational fields of study, such as marketing communication [32], recruiting [13], financial services [20], human resource management [64], and strategic management and entrepreneurship [16]. IS research has applied the theory [22] to software preannouncements [35], knowledge management [23], and e-commerce [75]. This study returns to signaling theory’s classical application: the hiring process.

The classical conceptualization of signaling theory describes the hiring process as involving potential employees signaling their qualifications to recruiters [61]. Applicants can improve the perception of their fitness for a position by altering their signaling—for instance, by obtaining and reporting additional education or experience. For applicants, the ability to honestly signal this additional fitness has traditionally been costly; theoretically, however, that cost prevents less-qualified applicants from sending the same signals [61]. This signaling system theoretically allows recruiters to choose the most qualified candidates. Spence [61] describes this system as a feedback loop in which organizations learn the actual value of signals only after employees have been hired and their productivity observed. Organizations adjust their valuation of specific signals for each subsequent hire, based on the observed productivity of past hires. False signaling was not explicitly considered in the original conceptualization of signaling theory, and a need for investigating this phenomenon in organizational applications has been identified [16]. If false signals follow the same model as honest signals, the false signals should progressively be perceived as unreliable and be devalued in the hiring process. However, in practice, false signalers have a higher probability of receiving job ofers and higher compensation than do honest signalers [30].

Recent research indicates that manipulated signaling has become common among job seekers. In three separate studies, Levashina and Campion [44] found that 79% of job seekers engaged in deceptive signaling, such as constructed, invented, or borrowed skills and experiences. Similarly, in a controlled study, Weiss and Feldman [74] found that 81% of job seekers told at least one lie while being interviewed for a job and that lies were orchestrated to signal conformance to the specific technical requirements of the job description.

False signaling is an increasingly prevalent problem, and it appears to be efectively manipulating the system: Culbertson et al. found that even interviewers with knowledge of deceptive behaviors were unable to recognize falsified signals during interviews [18]. The results of a recent U.S. industry survey indicate that 74% of hiring and HR managers claimed they had made a “bad hire” that year, with “bad hire” defined as an employee who exhibited characteristics of unexpectedly poor performance: poor work quality, negative attitude, poor teamwork, attendance problems, or lower skill than was claimed during the hiring process [11]. This percentage was up from 69% five years earlier [12]. Although signaling in job applications and the hiring process is intended to reduce information asymmetry, false signaling seems to increase the probability of adverse selection (i.e., hiring the less optimal candidate).

Though prevalent enough to allow for many bad hires, false signaling is not yet pervasive enough for organizations to completely discount all signals in the traditional application system. Nevertheless, the signaling system for job candidate selection as originally described in 1973 appears to be experiencing increasing failures. Whenever it is dificult to verify a signal’s veracity, the signaling system is apt to fail if job candidates choose to take advantage of that system’s weakness. This weakness is most obvious at the application stage, during which the cost to applicants for falsely claiming they have a particular qualification has become quite low.

Considering the evidence that costly manipulation pervades the current signaling system, we propose that a new signaling system is needed. The overarching objectives of this system should be (a) to increase the cost to applicants of sending false signals, to a degree that such signals are prevented, and (b) to decrease the cost to hiring personnel of accurately assessing applicant signals. To meet these objectives, the system design must address the process of sending and receiving signals, and improve the analysis of interviewees’ signals. The following subsections define these problems and propose system requirements that may alleviate these problems.

## The Signaling process

For most job seekers, the signaling process begins with an application. Signals on applications include degrees, titles, experience descriptions, skills, and even formatting and presentation. Partly because these signals can often be easily manipulated, interviews are then used to validate signals. Interviews also allow decision makers to obtain additional soft signals not available on an application—signals that indicate less deterministic qualifications such as social skills and organizational fit. These existing procedures can be adapted in several ways that can be described in signaling theory terms.

## Applications can include more signals

Applying for jobs often involves submitting online forms from any location [63]. Even many walk-in application processes involve an initial kiosk-based application. Using webbased, electronic human resource management (eHRM) systems, organizations receive applications, perform assessments, and sometimes even conduct interviews. This digitalization of hiring practices is largely based on the desire of companies to reduce costs and labor demands associated with hiring [56]. Although digitalization has enabled a significant increase in the number of applications for entry-level positions, applications alone provide limited and imperfect signals. The interview stage of the process has largely remained expensive and time consuming, and is still used only for a select few applicants, despite the increased size of the pool. The persistent use of interviews implies that the value of the signals received via interviewing is greater than the costs incurred [17], but this value is only obtained for a small portion of applicants.

We propose that an automated interview completed as part of the application stage could allow early, efective collection of additional and more reliable signals while simultaneously reducing the cost of conducting in-person interviews. The additional signals captured during this process could be included in automatic and manual application reviews, reducing the probability of adverse selection at this stage.

## One-way interviews can be standardized

Personnel selection literature indicates that using structured interviews reduces the bias and subjectivity otherwise associated with the selection process [10] and increases the validity and reliability of selection decisions [36, 45]. Existing automated interviewing research has naturally used structured interviews delivered identically to each interviewee. Carefully selected, structured questioning has been a critical component for detecting hidden knowledge of illicit behaviors in the context of criminal investigations and security screenings [67]. This practice can be adapted to job application-interviews to provide similar consistency. However, automated interviewing research often uses only binary-response questions to further increase the likelihood of internal consistency in the results [67]. For an application-interview, we propose retaining the open-ended questions commonly used in interviews. The brevity of responses to yes-or-no questions may not produce suficient signals to assess commonly desired traits, such as social skills and creativity. Nevertheless, we acknowledge that open-ended responses may increase noise compared to yes-or-no questions. Therefore, the system we propose will need to rely on signals that are robust enough to be suficiently discriminant despite this noise.

## Data collection can use ubiquitous sensors

Application-interviews can leverage ubiquitous sensors. Human perception is the typical sensor in traditional application and interview settings, but an automated approach requires alternative sensors. The interview process for our proposed system is adapted from professional criminal interviewing research, but the technology used in such interviews would be inordinately inconvenient, expensive, and obtrusive for an application-interview context. In criminal interviews, sensors such as heart-rate monitors and electrodermal response sensors efectively measure psychophysiological signals that are relatively dificult to manipulate. Professional examiners use these signals as indicators of interviewees’ truthfulness, or of the their hidden knowledge about a topic or event [51]. Although these types of sensors may be common in criminal investigations, they are uncommon in typical work and home ofices and therefore do not fit the environmental needs for the proposed system. Furthermore, few organizations and applicants would be comfortable using sensors that must be strapped or hooked on to a person.

To be clear, the job application system we propose should be able to leverage new and better signals to gauge all kinds of qualifications, not just truthfulness. However, much of the interview-system research to date has naturally been built on criminal-activity detection, and we draw on that research to make a case for the technological properties of the proposed system. Recognizing wider application of automated interviewing to domains such as visa application and security screening, some research has turned to noninvasive sensors as a means of assessing veracity [67]. Unfortunately, even though sensors such as eye trackers, thermal imagers, and force platforms show promise as noncontact alternatives [8], they have the same availability problem. The devices by which application systems are typically accessed have a camera paired with a microphone.

Recent developments in automated video and audio processing have transformed the potential of standard cameras as behavioral evaluation sensors. Deception detection research has leveraged these developments when using cameras to evaluate facial motion and vocal stress during criminal interviews [e.g., 58]. A typical camera provides access to a wide array of other signal sources as well, such as visual behaviors, voice characteristics, and language usage (via audio transcription). We therefore propose that the new type of application system should use a web-based program designed to conduct automated interviews and collect application material simultaneously, making use of standard enduser web cameras or other ubiquitous sensor inputs in which behavioral signals are embedded.

## Applicant signals can be rapidly assessed

The final hurdles in the signaling process that we seek to address are those of turnaround time and accuracy. Manually reviewing all applications, including recorded applicationinterviews, would normally be cost prohibitive and could also increase the likelihood of biased and faulty signal detection. We therefore propose extracting reliable signals from the data captured during automated interviews and using those signals to automatically estimate applicant qualifications. Machine learning and other forms of analytical models can fit this need, though care must be taken to minimize the potential for bias in these automated assessments.

## The Signals from interviewees

Current job application systems collect signals that employers have predetermined as benchmarks for hireability, such as education and skill with a technology. Modern eHRM systems automatically sift through applications by keywords and other metrics through web-based portals. These systems tend to favor applicants who portray the best signals, not necessarily those who are actually the most qualified. Applicants aware of keyword filtering may pad their applications with additional terms to ensure they make it past the first screening phase. Even non-proctored, web-based skills assessments allow many opportunities for manipulation.

Human-perceived signals that indicate social skills, personality, leadership, and teamwork are less deterministic, but are usually critical for getting hired. Hufcutt et al. [37] found that personality tendencies and social skills were more frequently assessed during the interview process compared to traits such as knowledge, skills, and mental capabilities. Other less-deterministic traits may include handshake firmness, physical appearance, word choice, and loudness of voice. Hiring committee members consciously and subconsciously use these and many other verbal and nonverbal behaviors to make inferences about interviewees. But many applicants will greatly embellish their abilities or significantly modify their natural behaviors to send such signals. To be efective, this interviewing system must collect and analyze signals that represent genuine candidate qualifications.

## Application systems can examine signals that are more dificult to manipulate

A core problem with relying on broad interpersonal signals (such as those used to evaluate nondeterministic qualifications) is that applicants can easily manufacture and manipulate the signals they send. This is well documented in self-presentation literature, which demonstrates that conscious actions are taken to present one’s self in a certain light [43]. There are many examples of how education level, emotional state, and conversational goals can afect an individual’s situational behaviors, and ultimately others’ perceptions of that individual. For example, speech fluency can afect the perceived hireability of a candidate during interviews [34, 49]. Positive facial afect and facial expressivity are consistently found to influence the outcomes of interviews [42, 49], likely because positive and expressive facial behaviors are also associated with sociability, persuasiveness, and competence [9]. Even the loudness of a job candidate’s voice correlates with higher perceptions of social skills, communication skills, and persuasion [46, 52]. Kinesic features (i.e., properties of body or facial movement) reflect felt emotions [25] and neurological reactions to stimuli [3], and there is initial evidence suggesting these signals can reflect general perceptions of hireability [52], as well as some social attributes, such as friendliness [49]. However, this research does not necessarily provide managers with heuristics for selecting the best candidate; rather, it helps candidates learn how to send more convincing signals.

We propose that, instead of commonly used human-perceived signals, a better system would rely on signals that a typical computing device can perceive but are dificult for humans to manipulate. We propose that SIGHT systems use these verbal and nonverbal signals to reflect deterministic qualities such as actual (rather than just perceived) social skills, as well as actual job performance, education, skill level, and integrity. Thus, SIGHT systems focus on efective signal detection rather than impression management. Signaling theory makes no assumption that a social actor must consciously or deliberately portray signals; therefore, we propose that especially costly signals be identified and used in a SIGHT system when evaluating job candidates. Ideally, a SIGHT system would include many signals that are dificult for a person to consciously manipulate, efectively increasing the cost of false signaling.

In certain structured criminal interviews, such as the polygraph, questions relevant to a criminal activity of interest are grouped with similar questions that have more easily verifiable answers [51]. Responses to verifiable questions serve as an individual baseline for comparison. Adapting this process to an interview setting could provide additional control to mitigate the impact of individual diferences in behaviors. For instance, one use of a SIGHT system might be to detect the willingness of candidates to fabricate qualifications. To address this issue, the software skills portion of the applicationinterview could include a question about experience with a nonexistent software package. Responses to this question could be compared to other software skills responses, providing a measure that controls for many interpersonal diferences, such as personal preferences, interests, gender, and culture. Similarly, questions about education and training could include questions about degrees obtained, for which there is publicly available information. The portion of the interview designed to assess communication skills could pair uncommon questions with common questions for which applicants might have practiced answers.

## The Analysis can control for individual diferences

Because candidates with the same qualifications may have diferent personalities, backgrounds, and dispositions, some of these telling signals may also vary between candidates. For instance, some interviewees may naturally experience higher degrees of nervousness. A 3-cm increase in distance from the screen may be a large behavioral variation for one person but in the range of normal behavior for another. To help counter this noise, we can normalize the signals for each question set to which a candidate responds, allowing more individualized identification of anomalous behavior. Normalizing responses within candidates and within question sets allows a system to perceive the individual’s baseline “normal” behavior, even if magnitude levels vary by individuals or topics. Within-subject comparison can create greater objectivity compared to between-subject approaches [55].

## Multiple robust signals can improve reliability

We already mentioned that tracking multiple signals increases an applicant’s cost to manipulate others’ perception of a desired trait. Tracking multiple signals can also decrease adverse selection due to signal noise. While normalizing signals can account for natural variations in signal strength between subjects, it may not account for other sources of unrelated variation in the signals. There is a possibility that, for any given behavioral signal, multiple mechanisms may trigger the same behavior. For instance, pupil dilation may reflect familiarity, but it may also reflect changes in lighting. Question sets and normalization may help minimize—but not eliminate—these unintentional false signals.

SIGHT systems therefore should track multiple distinct signals for robustness in cases where some signals are corrupted. Supporting this idea, related work has suggested that multiple signal modalities have greater predictive accuracy than any single signal [65, 68].

To summarize, the proposed system includes seven properties (Figure 1) encompassing the signaling process, environment, technology, and interviewees. To facilitate large-scale collection of signals, the design relies on an automated, web-based interviewer platform that is accessible from convenient locations and allows for simultaneous use and collection of diverse forms of data. Additionally, the design uses commonly available sensors (e.g., a web camera) to extract behavioral signals from an interviewee. To account for interpersonal diferences, a structured interview paradigm provides consistency and allows for both within- and between-interviewee comparisons. Finally, the analysis of interviewees relies on multiple distinct signals that are dificult to manipulate, to minimize the efects of noise. For each signal, within-interviewee normalization techniques are needed to identify individualized anomalous behaviors.

![](/api/attachments/HRJ44KFB/fulltext/images/8bd45a48326601ec0be9836e0862af9616296278225892504396b0f030dd387e.jpg)  
Figure 1. Summary of proposed properties for SIGHT systems.

## Prototypical implementation

In order to establish proof of concept, we instantiated the proposed design properties in a prototypical SIGHT system. The basic structure of the prototype was based on asynchronous interviewing platforms currently used by companies to prescreen job applicants [4]. The standard implementation of these systems includes a web portal where applicants provide verbal responses to text-based interview questions while being recorded by a webcam. Applicants can participate in interviews at locations and times of convenience using their personal computers or mobile devices. System administrators can adjust the maximum time to consider a response and the maximum time to respond. Similarly, the prototypical SIGHT system displays interview questions sequentially in a text-based form, allowing respondents 30 seconds to consider a response and 60 seconds to respond. Video recording only occurs during a response.

Figure 2A illustrates the prototype’s user interface. The black box is a placeholder for the livestream feed from an applicant’s webcam. During responses, this box is replaced with a view of the applicant as depicted by the webcam. When the large button above the camera view box is pressed, it reveals the next interview question to which the applicant must respond, and initiates a time-to-read countdown timer (displayed at the upper-left corner of the interface). At this point, the applicant reads the question and considers their response prior to the camera recording. Once the countdown timer reaches zero, or when the applicant clicks the green “Start Recording” button, a new 60-second timer is displayed, and the camera begins recording the applicant as he or she responds (see Figure 2B). Once the timer reaches zero, or if the user decides to stop recording early by clicking the red “Next Question” button, the camera will automatically stop recording. The recorded video is uploaded to the webserver, and the process repeats for the next interview question.

![](/api/attachments/HRJ44KFB/fulltext/images/cbe33f589f86e1195bfb5e3a6dc8edeff6e1347f8d4f38e3c7b99489bbe7f585.jpg)  
Figure 2. Question preparation and response in the sample SIGHT implementation.

## Signal collection and processing

In traditional implementations, asynchronous interview platforms save recorded responses on a centralized server where hiring managers manually review videos to assess applicant qualifications beyond the deterministic data appearing on résumés and applications. The SIGHT system allows manual review, but more importantly, it extracts raw data that contain signals. When video recordings are loaded onto the server, a series of behavioral feature-detection algorithms extract fine-grained voice, language, and facial behaviors that can be analyzed for their signal value. Figure 3 outlines the prototypical systems, including the delivery of interview questions, capture of responses, and extraction of behavioral features.

For this stage, we took an approach similar to IS deception detection research, in that we used noninvasive sensors to collect useful behavioral and psychophysiological data. Sensors used in related research have included eye-tracking systems, force platforms, and human-friendly lasers [8, 53]. In interview settings, these sensors have been used to generate raw behavioral data of various types, such as oculometric, kinesic, and even cardiorespiratory measurements, sometimes on a very small scale that would be suitable for recognition of minute signals. Requiring such specialized equipment would prevent most use cases for SIGHT systems. Thus, the prototype incorporated only a common webcam.

![](/api/attachments/HRJ44KFB/fulltext/images/232957ca86f22c253ddff5559d694e574fa79cbea19c86b68c331c7a45db6700.jpg)  
Figure 3. Technological components of the prototypical SIGHT application system.

The prototype used OpenSmile [27] to extract voice measures (e.g., pitch, intensity, jitter) from the recorded audio. Webcam microphones typically sample audio at 44 kHz, necessitating the calculation of summary statistics for each question response. To facilitate linguistic analysis, the system used the IBM Watson speech-to-text service [39], which returns a textual transcript. These transcripts were then processed with Structured Programming for Linguistic Cue Extraction (SPLICE), a program that processes text and returns quantitative summaries of linguistic cues for each question response [47]. The videos were processed using Intraface [76], a facial-point mapping program, which generates raw Cartesian coordinates of various points on the face for each frame of video.

The prototype used this raw data to calculate summary statistics across each interview question response, such as total word count and average position, acceleration, and movement for each point on the face. At this stage, it is necessary to identify which of all these summary features were likely candidates to serve as signals for each qualification of interest.

## Signal selection

SIGHT systems will ideally evaluate signaling for a broad range of desirable traits, including social skills and job performance. At this proof-of-concept stage, it was not feasible to examine signaling for every possible type of applicant qualification. For this evaluation, we elected to focus on an applicant’s truthfulness. We chose this as a starting case because integrity is expected to be a commonly desired qualification, and IS research in the criminal interviewing domain already provides insight into possible mechanisms that could create minute signals for this context.

## Theoretical basis for deception signals

Prior research has revealed behavioral indicators of veracity in a variety of contexts that may possibly serve as signals for this context. In most cases, the theoretical explanation for veracity assessment has relied on the concepts of leakage or strategic behaviors. Leakage theory asserts that lying produces natural human responses that the deceiver typically tries to mask or otherwise control. The theory suggests that such behavioral and psychophysiological responses “leak” out because of an inherent inability to control or mask them all [24]. Some later theories additionally proposed strategic behaviors as an explanation for some indicators. Strategic indicators are abnormal behaviors purposely exhibited by deceivers in an attempt to appear truthful [7]. Whether leaked or strategic, an observed behavior when deceiving is commonly compared to a normal (i.e., truthful) behavior to gauge its potential as a deception indicator [26].

There are many strategic and leaked behaviors in these three modalities that may serve as efective signals. However, we considered only behaviors that can be automatically measured and that may occur on a minute scale. Because the prototype input is limited to signals that can be obtained via webcam, we investigated facial, vocal, and linguistic behaviors in the evaluation.

## Visual signals

Facial movement was one candidate selected to serve as a signal. We expected overall facial movement to decrease during deception, based on prior research identifying facial freeze as an indicator of a deceptive response during short answers [58]. While some research has shown decreases in movement that are noticeable to a trained eye [e.g., 62, 69], this recent IS research identified decreases in facial movement that, because of their small scale, must be detected through analysis of data generated via computer vision. Though small in scale, the freezing efect was reported to be present across all parts of the face. This minute behavioral diference was discovered in the context of one-word answers to structured questioning. While SIGHT systems prescribe a similar question structure, the responses are expected to be considerably longer than one word, creating potential for noise in a signal that previous research reported to be statistically significant but minor in terms of scale [58]. However, the mechanism driving facial freeze appears to be either a natural fight-or-flight response or a natural tendency to try to appear truthful [66]—and both of these mechanisms should be expected to persist throughout a response, regardless of the response duration. We expected the evaluation to help reveal whether the freezing efect is strong enough to be detectable despite the additional noise introduced by extended answers.

An added reason for including facial movement as a potential signal was initial evidence in related work, which showed that a decrease in head and body movement during deception is dificult to consciously manipulate [68, 72]. Related research also suggested that the mechanisms driving decreased movement may similarly produce wooden movement—movement that starts and stops more suddenly as though it is being forced [6, 72]. We thus also included movement acceleration as a potential signal.

Considering that emotional masking may be a relatively easy manipulation, we elected to exclude general emotional facial expressions as signals. However, facial expressions can reflect underlying cognitive states [59], and cognitive activities such as memory retrieval and image control may be at diferent levels during deceptive as compared to truthful responses [14]. We thus included individual expression components, using the evaluation to identify which, if any, might produce a useful signal.

## Audio signals

The vocalic behaviors we selected were pitch, loudness, jitter, and shimmer. Falsifying a response appears to increase larynx muscle tension, which results in a slightly higher vocal pitch compared to truthful responses [68]. We considered that emotional tension may increase the loudness of a falsified response if interviewees naturally compensate for tension by projecting confidence. Jitter and shimmer are measures of perturbation of the fundamental vocal frequency. These are smallest when vocal folds are well controlled and held at a constant level of resistance [5]. We expected that naturally confident responses would reflect a clearer, more consistent vocal signal as compared to falsified responses, which may be accompanied by less confidence. We also included the first derivative of each of these behaviors with respect to time.

We included linguistic behaviors with empirical evidence supporting their association with leakage and strategic behavior theories. When lying is more dificult than telling the truth, false statements contain fewer sensory details, less contextual information, and greater response latency [71]. However, job interviews often contain predictable questions about skills and personality, which interviewees can prepare for to reduce the cognitive demands of lying. When answering expected questions, liars produce more detail than truth tellers [60]. Deceivers also difer in the quality of details, and they include a greater amount of nonverifiable information when describing an event than truth tellers [48].

## Signal fusion and standardization

Neither leakage theory nor strategic explanations guarantee that one will display distinctive behaviors when lying. Presumably, diferent deception indicators may be displayed depending on interpersonal, group, or cultural nuances. For instance, a person who is less worried about self-image may focus more on portraying believable linguistic content in their deception, while an image-conscious deceiver may put more efort into appropriate body language. With theories that provide no specific indicator guarantees, it is little wonder that no “Pinocchio’s nose” or highly reliable indicator of deception has been found. Neither do existing deception detection frameworks suggest any perfect indicator will ever be found. Therefore, we propose that an efective design will necessarily measure and incorporate a breadth of potential deception indicators. A classification model that fuses many indicators should more reliably catch deception because it is not possible to predict which indicators will be present. The relative magnitude of these indicators varies from person to person. For instance, although some individuals may have naturally stoic speech and body movements, others may be naturally dynamic. A small reduction in movement may be a major variation for some but minor for others. Prior research has addressed this issue by requiring withininterviewee standardization prior to classification [66].

## Method

To test the eficacy of the system, we conducted a mock job interview quasi-experiment with undergraduate students at a large university in the United States in the spring of 2017. The experiment employed the prototype as the interviewing mechanism for screening job applicants.

## Experimental procedure

Prior to arriving for the study, participants completed an online questionnaire. The questionnaire mirrored a basic employment application and contained questions about education, work experience, and skills. The skills-related questions asked participants to rate their level of experience with common software packages, including Microsoft Excel, Microsoft Word, Adobe Photoshop, RStudio, and Oracle SQL. Participants also rated their level of experience with StatView, which is an old statistical analysis program originally released for Apple Macintosh in 1985 and last updated in approximately 1998.

When participants arrived for the study, they were told that they would be participating in a mock job interview using a one-way automated interviewing system. They were then given a description of the job for which they would be interviewing. Participants were told that both their online applications and interview responses would be evaluated to determine if they were suitable for the job. All participants were then allowed to “tailor” their stored generic applications to suit the job description, if they so desired. The participants were also told that, if their qualifications matched the requirements in the job description, and if they performed well during their interviews, they would receive \$20. Otherwise, they would receive only \$5. This money was given to motivate participants to take the interview seriously, but was also a slight deception: all participants ultimately received \$20 for participation. Additionally, all participants received extra credit in their course for participating.

The job description listed several required skills, including “Advanced knowledge of Microsoft Excel” and “Proficiency with StatView Software Suite”; however, it did not mention other skills outlined in the online application. The objective was to give participants the choice to fabricate their qualifications for specific skills included in the job description. Thus, there was no a priori assignment to the deception or control condition —each participant naturally self-selected his or her condition. While self-selection is unusual for this type of research, we believe that self-selection bias introduced by this approach should prove more ecologically valid. This is because the deception group probably reflected those who were more comfortable with lying in the job-hiring process. Self-selection preserved naturalness in the interaction and therefore should have elicited behaviors that can more reliably serve as signals for this context.

Following the opportunity to tailor their online applications, participants responded to 15 interview questions using SIGHT. The interview contained nine generic interview questions (e.g., “Tell me about yourself”) and six questions regarding skills from the job description and online application (e.g., “On a scale of 0 to 5, with 0 being none and 5 being a great deal, rate your level of experience with the following: Microsoft Excel. Give a brief example to back your rating”). Questions seeking self-ratings of Microsoft Excel, Microsoft Word, public speaking, business statistics, and StatView were included in the analysis.

The experimental design allowed researchers to track fabrications made to an application to appear qualified for a job. The online application completed prior to viewing the job description was treated as ground truth. After the interview, participants took a posttask survey that measured their perceptions of their experience, including the importance of being selected for the mock position, and whether the mock position reflected a position they would consider applying for in a real-life scenario. Approximately 86% of participants reported that it was moderately important to extremely important to be selected as a top job candidate. Additionally, 82% of participants reported that the job description matched a position they either would or maybe would apply for during a realworld job search $( ^ { \mathrm { c c } } \mathrm { y e s } ^ { \mathrm { y } } = 4 1 \% , ^ { \mathrm { \alpha } } \mathrm { m a y b e } ^ { \mathrm { y } } = 4 1 \% , ^ { \mathrm { \alpha } } \mathrm { n o } ^ { \mathrm { y } } = 8 \% )$ . And when asked, “How much efort did you put into giving good answers during the interview?” 77% responded with “a lot” or “a great deal” $( ^ { \ast } \mathrm { n o n e } ^ { \mathfrak { n } } = 0 \% ,$ , “a littl $e ^ { ^ { \prime \prime } } { = } 1 . 1 4 \%$ , “moderate amoun $" ^ { \infty } = 2 1 . 5 9 \%$ , “a lot” $= 4 5 . 4 5 \%$ , “a great dea $\Gamma ^ { \prime \prime } = 3 1 . 8 2 \% )$ .

## Participants

A total of 89 undergraduate students aged 20 to 31 years old participated in the experiment (male = 35, female = 54). One subject (a female) was removed from the dataset for not completing all procedures. Though college students are commonly used in proof-ofconcept studies because of convenience, they were used in this study also because they represent well a large portion of the applicants for entry-level positions. Entry-level positions, because of relatively lower barriers, often have high volumes of applications, making them ideal use cases for SIGHT systems. In the United States, hiring of recent college graduates has consistently increased since 2010 [50], and over 60% of entry-level jobs have an education requirement somewhere between a high school diploma and a bachelor’s degree [73]. Of the participants who completed the experiment, 26% reported having previously used a similar one-way, video-based interviewing system during employment searches. In research generally, the use of students is often criticized because it impacts generalizability. However, as Compeau et al. [15, p. 1102] notes, “If the students are part of the population of interest … then their inclusion in the sample frame is appropriate because they are part of that population.” Though using students in this proof-of-concept evaluation was appropriate, caution should be exercised when extending results to other demographics.

When given the opportunity to tailor their online applications, 43.8% increased their self-rating for Microsoft Excel, 21.3% increased their self-rating for Microsoft Word, and 31.4% reported having at least some experience with StatView, after previously reporting that they had never used StatView. Eight participants initially reported having experience with StatView. These participants were removed from the analysis because, given the dated, unavailable nature of the software, it seems most likely they were confusing StatView with another software program.

## Condition labeling

A response was labeled as deceptive only if an applicant initially reported zero experience with a skill/software program, but later reported some level of experience after having viewed the job requirements. It is unlikely that applicants were being deceptive when indicating they had zero ability with a particular skill, because reporting a lack of skill in a general application would have no perceived advantage. This is especially true of the StatView question, for which experience among any of the applicants was extremely unlikely. When given the opportunity to tailor an application, an applicant increasing the rating of a skill from zero to something higher is highly likely to be an outright fabrication as opposed to a simple exaggeration of an existing skill.

Self-ratings that remained the same were labeled as truthful. Exaggerations were also labeled as truthful. Exaggerations were defined as ratings that were initially greater than zero that were increased further when applicants were given the opportunity to modify their applications. This method was adopted to maximize certainty of the presence of deception and to minimize the impact of exaggeration. We labeled participants who exaggerated as truthful for two reasons. First, the experience ratings were subjective: A change from 2 to 3 on a Likert scale might reflect a participant rating a skill in relation to the requirements specified by the position. Second, an organization is more likely to experience harm from hiring an applicant with no experience than from hiring someone with at least some experience. From the participants and questions analyzed, 37 (46.25%) were truthful for all questions, 35 (43.75%) were deceptive during one question, seven (8.75%) were deceptive during two questions, and one (1.25%) was deceptive for three questions.

## Analysis and results

The SIGHT system captured video and audio for each question, processed the raw data to generate measures of the selected behaviors for the skill question responses, and standardized the measures within subjects to control for interpersonal diferences. Video, audio, and linguistic measures were separately submitted to principal components analyses, for both component identification and dimension reduction (see Supplemental Online Appendix). The final, rotated components were labeled according to the behavioral trait they appeared to reflect, based on the items that loaded heavily. The labeled components are shown in Table 1.

We identified behaviors to which deception created significant variation by using a multivariate regression model with deception as the predictor variable and the behaviors in Table 1 as outcome variables. Full model results are available in the Supplemental Online Appendix. Figure 4 shows the behaviors that are significant predictors of deception. The units of measurement in Figure 4 are standard deviations, so an interpretation for vocal excitement would be that, on average, interviewees spoke with about half a standard deviation more excitement than normal when fabricating a response in comparison to their own baseline responses.

The results indicate that, compared to the baseline responses, deceptive responses were associated with reduced movement in locations across the face. Additionally, the facial

Table 1. Labeled behavioral components generated by the SIGHT prototype

<table><tr><td colspan="2">Vocal Signals</td><td>Facial Signals</td></tr><tr><td>Vocal Power</td><td>Main Mouth Movement</td><td>Bottom of Nose Acceleration</td></tr><tr><td>Vocal Quality</td><td>Upper Eyelid Movement</td><td>Inner Brow Acceleration</td></tr><tr><td rowspan="3">Vocal Excitement</td><td>Bottom of Nose Movement</td><td>Outer Brow Acceleration</td></tr><tr><td>Nose Bridge Movement</td><td>Lower Eyelid Acceleration</td></tr><tr><td>Outer Brow Movement</td><td>Mouth Corners Acceleration</td></tr><tr><td>Linguistic Signals</td><td>Inner Brow Movement</td><td>Nose to Mouth Corners— Vertical Distance</td></tr><tr><td>Word Complexity</td><td>Lower Eyelid Movement</td><td>Inner Brows to Lower Lids— Vertical Distance</td></tr><tr><td>Syntactic Complexity</td><td>Mouth Corners Movement</td><td>Upper Lips to Lower Lips —Vertical Distance</td></tr><tr><td>Creative Expression</td><td>Main Mouth Acceleration</td><td>Upper Lids to Outer Brows— Vertical Distance</td></tr><tr><td>Active Language</td><td>Upper Eyelids Acceleration</td><td>Right Outer Brow— Vertical Position</td></tr><tr><td>Subjective Language Agreeable Language</td><td></td><td>Left Outer Brow— Vertical Position</td></tr><tr><td>Past- Tense Usage</td><td></td><td>Nostrils— Vertical Position</td></tr><tr><td>Linguistic Negativity</td><td></td><td>Nose Bridge Acceleration</td></tr><tr><td>Adjective Usage</td><td></td><td></td></tr><tr><td>Adverb Usage</td><td></td><td></td></tr></table>

Note: These features are a small subset of features that can be generated via computer vision, natural language processing, and vocalic analysis. These features were selected based on theory indicating the presence of voice, face, and language anomalies during deception.

![](/api/attachments/HRJ44KFB/fulltext/images/2ac379b4a6118f7f716aeda79d0395c712447c7ece317222697f38ebfbcdcdb0.jpg)  
Figure 4. Graphical representation of the coeficient estimates of significant (p < .05) signals during deceptive responses.

movement that did occur accelerated more slowly than in baseline responses. From a vocalic perspective, deceptive responses resulted in a significant drop in what we termed “vocal quality,” which means that the pitch, intensity, and jitter of the voice decreased. Probably relatedly, a deceptive response typically marked a low point in a trend toward increased vocalic excitement in later responses.

Deceptive responses contained significantly more “creative expression” language, having more cognitive complexity, expressivity, and lexical diversity, and fewer words than truthful responses. Prior research has indicated that measures in the “creative expression” category generally decrease as cognitive load increases, presumably because deception is more cognitively demanding than truth telling [31, 71, 78]. However, the participants in this study had a brief period to prepare before responding to the questions, which should have lowered cognitive load overall [60, 70]. Truthful responses to questions regarding skills may require greater levels of cognitive load than lying because a truthful response likely involves recalling specific experiences, tasks, and skills. Liars may use greater expressivity than truth tellers when a task requires persuasion [77]. The number of words used as a predictive cue tends to vary by context [21, 31]. In general, liars tend to use fewer words than truth tellers, likely due to increased cognitive demand [31].

Word complexity, which is a composite of several word length measurements, was lower for deceptive responses. The literature on word complexity generally shows no diference between truth and deception [31, 38]; however, this measurement is generally tested between subjects and not within subjects. In an interview context, adjectives and adverbs may represent claims that an interviewer cannot verify, unlike most nouns and verbs (e.g., “I have extensively worked with advanced spreadsheet functions” versus “I have worked with spreadsheet macros for three years”). Liars showed an increased rate of adverbs, suggesting that candidates rely on pufery when lying about skills or experience.

## Evaluation of predictive capability

The multivariate regression analysis provided evidence that our design can elicit and identify minute behaviors that may serve as signals in a SIGHT interview setting. However, the general presence of such markers is not a guarantee that they can efectively identify deception. The SIGHT system should classify interviewee qualifications using standardized signals as inputs. We employed a series of predictive capability analyses to gauge the design’s potential for identifying deceptive responses. For each of the predictive models, only the behavioral signals listed in Table 1 (and correlating below .70) were included as predictors. This approach difers from the traditional approach of including all possible features and then reducing them through a feature selection process. Selecting features based on theory allows the predictive models to better reflect the theoretical system they represent (SIGHT), as opposed to one specific instance. Thus, our design retains features that are not significant predictors within this particular data set.

Among common predictive techniques, there is not necessarily a theoretical reason to believe ex ante that one type of classification model would perform better than another. Therefore, we evaluated the SIGHT prototype using four diferent classes of supervised classification algorithms: radial support vector machine (SVM), bagged artificial neural networks (ANNs), random forest (RF), and boosted logistic regression (BLR). Comparing algorithm performance or proposing new variations on well-known algorithms is not a goal of this research. Rather, various classification algorithms were used to gain initial insight into how a theoretical SIGHT system might perform, at least in a laboratory setting.

All behavioral indicators from Table 1 were the inputs for the classification models. Two behaviors, the movement of the bottom of the nose and the movement of the main part of the mouth, were correlated at .76. The bottom-of-nose movement was excluded to avoid potential prediction problems that high multicollinearity can sometimes create. All other correlations were at acceptable levels (< .70). To reduce the likelihood that model performance was not a function of training and testing sampling, a 100-fold Monte Carlo cross-validation (MCCV) approach was employed. MCCV uses an iterative split, train, and test process. For each iteration, a new model was trained using 75% of the full dataset. The subsequent model was then tested on the remaining 25% holdout set. During each iteration, the training and testing datasets were randomly drawn from the full dataset. Correct and incorrect classifications were recorded for each iteration. Finally, performance measures were calculated.

Table 2. Classification results

<table><tr><td rowspan="2">Model</td><td rowspan="2">Accuracy</td><td rowspan="2">Precision</td><td rowspan="2">Recall</td><td rowspan="2"> $F_1$ </td><td colspan="3">Confusion matrix</td></tr><tr><td></td><td colspan="2">Actual</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Predicted</td><td>Deception</td><td>Truth</td></tr><tr><td rowspan="2">Radial SVM</td><td rowspan="2">0.8565</td><td rowspan="2">0.8511</td><td rowspan="2">0.8256</td><td rowspan="2">0.8381</td><td>Deception</td><td>743</td><td>130</td></tr><tr><td>Truth</td><td>157</td><td>970</td></tr><tr><td rowspan="2">Random Forest</td><td rowspan="2">0.910</td><td rowspan="2">0.9176</td><td rowspan="2">0.8789</td><td rowspan="2">0.8978</td><td>Deception</td><td>791</td><td>71</td></tr><tr><td>Truth</td><td>109</td><td>1029</td></tr><tr><td rowspan="2">Boosted LR</td><td rowspan="2">0.950</td><td rowspan="2">0.9167</td><td rowspan="2">0.9778</td><td rowspan="2">0.9462</td><td>Deception</td><td>880</td><td>80</td></tr><tr><td>Truth</td><td>20</td><td>1020</td></tr><tr><td rowspan="2">Bagged ANN</td><td rowspan="2">0.957</td><td rowspan="2">0.9367</td><td rowspan="2">0.9700</td><td rowspan="2">0.9531</td><td>Deception</td><td>873</td><td>59</td></tr><tr><td>Truth</td><td>27</td><td>1041</td></tr></table>

Notes: Measures represent cumulative performance over 100 iterations of Monte Carlo Cross-Validation.

Table 2 lists the performance results of the classification models generated. “Accuracy” reflects the algorithm’s ability to correctly classify a response as truthful or deceptive using the signals received; “precision” reflects the algorithm’s ability to avoid labeling truthful responses as deceptive; and “recall” reflects the algorithm’s ability to correctly classify deceptive responses as deceptive. In many scenarios, the harmonic mean of precision and recall $( \mathrm { i . e . , F _ { 1 } ) }$ is a desirable measure of performance because it minimizes the influence of false negatives. In this context, true negatives indicate honest job candidates, and classifying them as such is just as valuable—or perhaps even more valuable—than identifying deceptive responses. Therefore, $\mathrm { F } _ { 1 }$ may be the most telling performance measure here because it represents a balance between organization and interviewee interests. We report all these metrics because each contains unique information.

The classification models produced $\mathrm { F } _ { 1 }$ values ranging between .84 and .95—better than the well-documented human performance rate of 54% [2] and better than the noinformation rate (55%), which is the accuracy rate if all responses are classified as deceptive. In a follow-up analysis that restricted features to those that were both theoretically predicted and found to be statistically significant, $\mathrm { F } _ { 1 }$ values were .85, .92, .87, and .73. Overall, these results demonstrate the exceptional potential of SIGHT to identify honest responses to interview questions.

## Discussion

Hiring organizations must contend with pervasive false signaling in the application process and beyond. To address this issue, we proposed principles for a more robust signaling system to aid the hiring process. Largely following an established DSR methodology [54], this study proposed a theoretical system and provided initial evidence toward proof of concept, by creating one instantiation of the SIGHT process and technology and then experimentally evaluating its potential. The results reflect broad potential for SIGHT signaling systems.

Post-survey data revealed that participants largely had positive reactions to the interviewing technology (“extremely positiv $\ ? ^ { \infty } = 1 2 . 5 \%$ , “somewhat positive $\begin{array} { r } { \ddot { \mathbf { \eta } } ^ { \mathfrak { p } } = 4 5 . 4 5 \% , } \end{array}$ “neither positive nor negative $^ { \ ' } = 1 8 . 1 8 \%$ , “somewhat $\mathrm { n e g a t i v e } ^ { \gg } = 2 1 . 5 9 \%$ , “extremely $\mathrm { n e g a t i v e ^ { \mathfrak { W } } = }$ 2.27%). However, when asked what type of interview they preferred (traditional, one-way, or either), 76.14% chose a more traditional interview, compared to 13.64% who preferred one-way interviewing technology. Those preferring traditional interviews often explained their preference by citing the importance of building rapport with the interviewer and using the interviewers’ body language to judge performance.

The several contributions of this research are best articulated from a DSR perspective. DSR studies commonly produce descriptive and/or prescriptive knowledge [29] by proposing, instantiating, and evaluating new classes of systems [54]. This article first produced descriptive knowledge through presenting a novel articulation of the problem domain: The hiring process was uniquely conceptualized as a broken signaling system, due to skewed cost functions aforded by technology advances. This contribution is important because it provided the theoretical context and boundaries necessary to begin to address the problem in both this study and in future research. Although we claim a new signaling system is needed, we do not mean to imply a fundamental inaccuracy in signaling theory. Rather, the need for a new system stems from technological and social changes that have altered the cost function of both conveying and detecting false signaling. This framework can also be a useful lens to view similar problems, where sociotechnical afordances have decreased the costs of sending false signals while increasing the costs of evaluating signals, to levels that may threaten the stability of the system. Example use cases include identifying misleading or false user-generated content, auditing interviews, assessing news-source credibility, and developing telehealth diagnoses. In some cases, SIGHT may prove a valuable alternative or supplement to form-based responses.

The study further contributes prescriptive knowledge [29] by describing a system-based solution that can be used in a signaling environment to help rectify problems related to the cost function. This novel prescriptive contribution includes a multidisciplinary and theoretically derived system design based on prior research in the areas of communication, deception detection, interviewing, and scalable technologies. The core of this solution involves an automated, structured collection and use of new, less manipulable signals for each attribute of interest by using ubiquitous technology. SIGHT systems increase the cost of false signaling for job applicants and decrease the cost of signal assessment for hiring organizations.

We anticipate some resistance to the idea of a “machine” gauging job fitness. Some individuals may question a machine’s ability to correctly interpret signals, or to at least correctly interpret the individuals’ own signals, which the individuals may see as diferent from normal. These concerns do have validity: The SIGHT system incorrectly interpreted some interviewee responses, and there are still many avenues to explore to ascertain the robustness of the results. However, the results thus far reflect a marked improvement upon the status quo. A SIGHT system’s ability to correctly classify signal veracity appears to far outperform typical human ability, which is notoriously poor [2] and subject to all sorts of biases, such as cultural bias [28]. Bias in an automated signaling system can be more easily detected and corrected. Furthermore, SIGHT leverages carefully structured questioning to generate individual baseline responses and identify signals, thereby greatly diminishing the efects of interpersonal diferences. Thus, there is little theoretical reason to expect systemic bias in SIGHT due to race, culture, age, or gender. Nevertheless, in practice, bias may be possible due to unforeseen variables, measurement error, and noise. Research beyond this proof of concept is needed to explore this potential.

The behavioral indicators of signal manipulation commonly studied in the domains of psychology and communications are often associated with high levels of stress or arousal —for example, in the context of criminal activities. Unlike in criminal investigations, the low-stakes outcomes of deceit during the hiring process may not induce high levels of stress or arousal, potentially resulting in diminished behavioral variations. The low cost and high return of deception seem to make exaggeration and fabrication more easily rationalized. SIGHT systems respond by monitoring multiple behavioral channels during highly structured responses. The variety and granularity of behaviors sensed by SIGHT allow for the recognition of slight anomalies between structured responses.

The SIGHT design specifications are rooted in environmental factors associated with hiring processes and practices, as well as in established theories and methods from varying academic disciplines. Just as DSR draws from existing environmental factors and knowledge bases, the approach also contributes to each. From a knowledge-based perspective, the design and evaluation of SIGHT add to the growing body of literature on machinebased deception detection. Notably, the results of our evaluation provide further evidence of a facial-rigidity efect during deception. This behavioral cue has only recently started receiving attention because of the dificulty of detecting rigidity; nonetheless, facial rigidity seems to be a consistent indicator of deception. Additionally, this study is the first to identify decreased facial acceleration as a potential deception indicator. Though the cause of decreased facial acceleration is unclear, it may be related to the facial freeze associated with the psychophysiological and behavioral mechanisms theorized to accompany deception. This study also found that participants who presented false qualifications used more creative language when discussing false qualifications. The components of the creative language measure normally decrease under greater cognitive load [31]. This unexpected result may indicate that it is easier to express false experience than it is to accurately explain areas in which one is skilled.

The path from conceiving new systems to creating standalone value involves many steps and can require many studies [54]. In developing the general design framework for SIGHT systems and evaluating a limited example prototype, we did not provide evidence that the SIGHT concept has identified and solved all major hurdles and is ready for widespread adoption. Rather, this study has provided evidence toward proof of concept, which includes defining the problem and solution as well as finding evidence that the concept has potential, at least in a limited form. Future research should refine and build on this foundation.

## Limitations and future work

This research has several limitations that provide opportunities for future research. In contrast to related research, this study includes ecological validity in that applicants deliberately deceived rather than portrayed instructed or sanctioned deception. This action introduces self-selection bias, which in this case more closely reflects real-world deception in interviewing. The experimental evaluation used a realistic job description, online application software, and one-way interviewing—tools and processes with which the target population was familiar. However, applicants were in a mock job interview seeking a limited monetary incentive, a situation that does not necessarily reflect the pressure or stakes of a real job interview. Though this study identified no theoretical reasons why such situational diferences might be problematic, the possibility remains that they may somehow diminish or change the signals used. Examining SIGHT principles for real job applications is necessary to evaluate signal robustness. Further, this system was tested with students at a university in the United States. Students are a significant portion of the population of interest. Field testing in diverse environments is necessary to help refine design principles and determine if distinguishing features vary by age, culture, language, education, or socioeconomic background.

The design of SIGHT as a system for signal verification relies on the assumption that certain human behaviors are more dificult to control during deception than are other behaviors. For this reason, features such as facial movement and facial movement accelerations were extracted; we did not extract macro-emotional expressions, which are easier to purposely control and manipulate. However, we did not specifically evaluate the controllability of each signal. Prior research has indicated that macro facial displays are highly controllable [79], whereas voice features are strongly tied to psychophysiological mechanisms [40], making this channel more dificult to control. This past research provided support for including some behavioral features while excluding others. Even so, future research is needed to better understand the extent to which subtle behaviors can be controlled and manipulated.

Further, the system evaluation design mitigated machine learning bias by using observed behaviors (the observed act of deception and observed verbal/nonverbal behaviors during responses) to train classifiers. As the system expands to predict constructs beyond deception, such as interview performance or cultural fit, future research must incorporate methods to alleviate bias (e.g., gender or race discrimination) caused by training data [41]. This bias is the result of “garbage-in, garbage-out” efects; using training data derived from subjective human interpretation naturally includes the inherent biases of humans.

## Conclusion

This paper began by explaining how signaling during the employee selection process has become problematic, with many candidates choosing to manipulate their signaled qualifications. In response, we proposed SIGHT, a rigorously designed new type of information system capable of evaluating signals early in the hiring process. The results of our evaluation demonstrated the eficacy of using such a system to reduce the risk of bad hires. Although employee selection was the primary focus, the design principles outlined in this paper apply to many situations in which human behaviors must be evaluated at scale. These situations include high-volume deception detection (security screenings, auditing, etc.) as well as skill assessment, mental-health examinations, and collegeadmission screenings. This research represents a growing body of work within the IS community that provides decision support solutions using human analytics.

## Funding

This study was funded partially by the Center for Leadership Ethics at the University of Arizona.

## References

1. Barrick, M.R.; Shafer, J.A.; and DeGrassi, S.W. What you see may not be what you get: Relationships among self-presentation tactics and ratings of interview and job performance. Journal of Applied Psychology, 94, 6 (2009), 1394–1411.

2. Bond, C.F.; and DePaulo, B.M. Accuracy of deception judgments. Personality and Social Psychology Review, 10, 3 (2006), 214–234.

3. Bracha, H.S.; Ralston, T.C.; Matsukawa, J.M.; Williams, A.E.; and Bracha, A.S. Does “fight or flight” need updating? Psychosomatics, 45, 5 (September 2004), 448–449.

4. Brenner, F.S.; Ortner, T.M.; and Fay, D. Asynchronous video interviewing as a new technology in personnel selection: The applicant’s point of view. Frontiers in Psychology, 7 (2016), 863.

5. Brockmann, M.; Storck, C.; Carding, P.N.; and Drinnan, M.J. Voice loudness and gender efects on jitter and shimmer in healthy adults. Journal of Speech Language and Hearing Research, 51, 5 (October 2008), 1152.

6. Buller, D.B.; and Aune, R.K. Nonverbal cues to deception among intimates, friends, and strangers. Journal of Nonverbal Behavior, 11(1987), 269–290.

7. Buller, D.B.; and Burgoon, J.K. Interpersonal deception theory. Communication Theory, 6, 3 (1996), 203–242.

8. Burgoon, J.; Nunamaker Jr., J.; and Metaxas, D. Noninvasive measurement of multimodal indicators of deception and credibility. Final Report to the Defense Academy for Credibility Assessment (2010). Tucson: University of Arizona.

9. Burgoon, J.K.; Birk, T.; and Pfau, M. Nonverbal behaviors, persuasion, and credibility. Human Communication Research, 17, 1 (1990), 140–169.

10. Campion, M.A.; Palmer, D.K.; and Campion, J.E. A review of structure in the selection interview. Personnel Psychology, 50, 3 (1997), 655–702.

11. CareerBuilder. Nearly 3 in 4 employers afected by a bad hire, according to a recent CareerBuilder survey, December 7, 2017. Accessed on 22 July, 2020: http://press.career builder.com

12. CareerBuilder.com. Nearly 7 in 10 businesses afected by a bad hire in the past year, according to CareerBuilder survey, December 13, 2012. Accessed on 22 July, 2020: https://www. careerbuilder.com

13. Celani, A.; and Singh, P. Signaling theory and applicant attraction outcomes. Personnel Review, 40, 2 (February 2011), 222–238.

14. Christ, S.E.; Van Essen, D.C.; Watson, J.M.; Brubaker, L.E.; and McDermott, K.B. The contributions of prefrontal cortex and executive control to deception: Evidence from activation likelihood estimate meta-analyses. Cerebral Cortex, 19, 7 (July 2009), 1557–1566.

15. Compeau, D.; Marcolin, B.; Kelley, H.; and Higgins, C. Generalizability of information systems research using student subjects—a reflection on our practices and recommendations for future research. Information Systems Research, 23, 4 (2012), 1093–1109.

16. Connelly, B.L.; Certo, S.T.; Ireland, R.D.; and Reutzel, C.R. Signaling theory: A review and assessment. Journal of Management, 37, 1 (2011), 39–67.

17. Cook, M. Personnel Selection: Adding Value Through People—a Changing Picture. John Wiley & Sons, 2016.

18. Culbertson, S.S.; Weyhrauch, W.S.; and Waples, C.J. Behavioral cues as indicators of deception in structured employment interviews. International Journal of Selection and Assessment, 24, 2 (2016), 119–131.

19. Dawkins, M.S.; and Guilford, T. The corruption of honest signalling. Animal Behaviour, 41, 5 (1991), 865–873.

20. De Franco, G.; and Zhou, Y. The performance of analysts with a CFA designation: The role of human-capital and signaling theories. The Accounting Review, 84, 2 (2009), 383–404.

21. DePaulo, B.M.; Lindsay, J.J.; Malone, B.E.; Muhlenbruck, L.; Charlton, K.; and Cooper, H. Cues to deception. Psychological Bulletin, 129, 1 (2003), 74–118.

22. Dimoka, A.; Hong, Y.; and Pavlou, P.A. On product uncertainty in online markets: Theory and evidence. MIS Quarterly, 36, 2 (2012), 395–426.

23. Durcikova, A.; and Gray, P. How knowledge validation processes afect knowledge contribution. Journal of Management Information Systems, 25, 4 (2009), 81–108.

24. Ekman, P.; and Friesen, W.V. Nonverbal leakage and clues to deception. Psychiatry, 32, 1 (February 1969), 88–106.

25. Ekman, P.; Friesen, W.V.; and Ellsworth, P. Emotion in the Human Face: Guidelines for Research and an Integration of Findings. Pergamon Press, 1972. Elmsford, NY; Toronto, Canada; Oxford, UK; Sydney, Australia; and Braunschweig, Germany.

26. Elkins, A.C.; Derrick, D.C.; and Gariup, M. The voice and eye gaze behavior of an imposter: Automated interviewing and detection for rapid screening at the border. In EACL 2012 Workshop on Computational Approaches to Deception Detection, Avignon, France, 2012, pp. 49–54.

27. Eyben, F.; Weninger, F.; Gross, F.; and Schuller, B. Recent developments in openSMILE, the Munich open-source multimedia feature extractor. In Proceedings of the 21st ACM International Conference on Multimedia, 2013, pp. 835–838.

28. George, J.F.; Gupta, M.; Giordano, G.; Mills, A.M.; Tennant, V.M.; and Lewis, C.C. The efects of communication media and culture on deception detection accuracy. MIS Quarterly, 42, 2 (2018), 551–575.

29. Gregor, S.; and Hevner, A.R. Positioning and presenting design science research for maximum impact. MIS Quarterly, 37, 2 (2013), 337–355.

30. Grifith, R.L.; Chmielowski, T.; and Yoshita, Y. Do applicants fake? An examination of the frequency of applicant faking behavior. Personnel Review, 36, 3 (April 2007), 341–355.

31. Hauch, V.; Blandón-Gitlin, I.; Masip, J.; and Sporer, S.L. Are computers efective lie detectors? A meta-analysis of linguistic cues to deception. Personality and Social Psychology Review, 19, 4 (2015), 307–342.

32. Herbig, P. Market signalling: A review. Management Decision, 34, 1 (February 1996), 35–45.

33. Hibbeln, M.T.; Jenkins, J.L.; Schneider, C.; Valacich, J.; and Weinmann, M. How is your user feeling? Inferring emotion through human-computer interaction devices. MIS Quarterly, 41, 1 (2017), 1–21.

34. Hollandsworth, J.G.; Jr., Kazelskis; R., Stevens; J., and Dressel, M.E. Relative contributions of verbal, articulative, and nonverbal communication to employment decisions in the job interview setting. Personnel Psychology, 32, 2 (1979), 359–367.

35. Hoxmeier, J.A. Software preannouncements and their impact on customers’ perceptions and vendor reputation. Journal of Management Information Systems, 17, 1 (2000), 115–139.

36. Hufcutt, A.I.; and Arthur, W. Hunter and Hunter (1984) revisited: Interview validity for entry-level jobs. Journal of Applied Communication Research, 79, 2 (1994), 184–190.

37. Hufcutt, A.I.; Conway, J.M.; Roth, P.L.; and Stone, N.J. Identification and meta-analytic assessment of psychological constructs measured in employment interviews. Journal of Applied Psychology, 86, 5 (2001), 897–913.

38. Humpherys, S.L.; Mofitt, K.C.; Burns, M.B.; Burgoon, J.K.; and Felix, W.F. Identification of fraudulent financial statements using linguistic credibility analysis. Decision Support Systems, 50, 3 (2011), 585–594.

39. IBM. Watson Speech to Text. International Business Machines (IBM), 2018.

40. Juslin, P.N.; and Scherer, K.R. Vocal expression of afect. In The New Handbook of Methods in Nonverbal Behavior Research, edited by Jinni Harrigan, Robert Rosenthal, and Klaus Scherer. Oxford: Oxford University Press, 2005, pp. 65-135.

41. Khademi, A.; Lee, S.; Foley, D.; and Honavar, V. Fairness in algorithmic decision making: An excursion through the lens of causality. In The World Wide Web Conference, 2019, pp. 2907–2914.

42. Krumhuber, E.; Manstead, A.S.; Cosker, D.; Marshall, D.; and Rosin, P.L. Efects of dynamic attributes of smiles in human and synthetic faces: A simulated job interview setting. Journal of Nonverbal Behavior, 33, 1 (2009), 1–15.

43. Leary, M.R.; and Kowalski, R.M. Impression management: A literature review and two-component model. Psychological Bulletin, 107, 1 (1990), 34.

44. Levashina, J.; and Campion, M.A. Measuring faking in the employment interview: development and validation of an interview faking behavior scale. Journal of Applied Psychology, 92, 6 (2007), 1638-1656.

45. Levashina, J.; Hartwell, C.J.; Morgeson, F.P.; and Campion, M.A. The structured employment interview: Narrative and quantitative review of the research literature. Personnel Psychology, 67, 1 (2014), 241–293.

46. Mehrabian, A.; and Williams, M. Nonverbal concomitants of perceived and intended persuasiveness. Journal of Personality and Social Psychology, 13, 1 (1969), 37–58.

47. Mofitt, K.C.; Giboney, J.S.; Ehrhardt, E.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Structured programming for linguistic cue extraction (SPLICE). In Report of the HICSS-45 Rapid Screening Technologies, Deception Detection, and Credibility Assessment Symposium, 2012.

48. Nahari, G.; Vrij, A.; and Fisher, R.P. Exploiting liars’ verbal strategies by examining the verifiability of details. Legal and Criminological Psychology, 19, 2 (September 2014), 227–239.

49. Naim, I.; Tanveer, M.I.; Gildea, D.; and Hoque, M.E. Automated prediction and analysis of job interview performance: The role of what you say and how you say it. In 11th IEEE International Conference and Workshops on Automatic Face and Gesture Recognition, 2015, pp. 1–6.

50. National Association of Colleges and Employers (NACE). Job Outlook 2019. Bethlehem, PA, 2018.

51. National Research Council. The Polygraph and Lie Detection. Washington, D.C., 2003. The National Academies Press

52. Nguyen, L.S.; and Gatica-Perez, D. I would hire you in a minute: Thin slices of nonverbal behavior in job interviews. In Proceedings of the 2015 ACM on International Conference on Multimodal Interaction, 2015, pp. 51–58.

53. Nunamaker, J.F., Jr.; Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; and Patton, M.W. Embodied conversational agent-based kiosk for automated interviewing. Journal of Management Information Systems, 28, 1 (July 2011), 17–48.

54. Nunamaker, J.F., Jr.; Twyman, N.W.; Giboney, J.S.; and Briggs, R.O. Creating high-value real-world impact through systematic programs of research. MIS Quarterly, 41, 2 (2017), 335–351.

55. Palena, N.; Caso, L.; and Vrij, A. Detecting lies via a theme-selection strategy. Frontiers in Psychology, 9 (2018), 2775.

56. Parry, E.; and Tyson, S. Desired goals and actual outcomes of e-HRM. Human Resource Management Journal, 21, 3 (July 2011), 335–354.

57. Pefers, K.; Tuunanen, T.; Rothenberger, M.A.; and Chatterjee, S. A design science research methodology for information systems research. Journal of Management Information Systems, 24, 3 (2007), 45–77.

58. Pentland, S.J.; Twyman, N.W.; Burgoon, J.K.; Nunamaker, J.F., Jr.; and Diller, C.B. A video-based screening system for automated risk assessment using nuanced facial features. Journal of Management Information Systems, 34, 4 (2017), 970–993.

59. Rozin, P.; and Cohen, A.B. High frequency of facial expressions corresponding to confusion, concentration, and worry in an analysis of naturally occurring facial expressions of Americans. Emotion, 3, 1 (2003), 68–75.

60. Shaw, D.J.; Vrij, A.; Leal, S.; Mann, S.; Hillman, J.; Granhag, P.A.; and Fisher, R.P. Expect the unexpected? Variations in question type elicit cues to deception in joint interviewer contexts. Applied Cognitive Psychology, 27, 3 (2013), 336–343.

61. Spence, M. Job market signaling. The Quarterly Journal of Economics, 87, 3 (August 1973), 355–374.

62. Sporer, S.L.; and Schwandt, B. Moderators of nonverbal indicators of deception: A meta-analytic synthesis. Psychology Public Policy and Law, 13(2007), 1–34.

63. Stone, D.L.; Lukaszewski, K.M.; Stone-Romero, E.F.; and Johnson, T.L. Factors afecting the efectiveness and acceptance of electronic selection systems. Human Resource Management Review, 23, 1 (March 2013), 50–70.

64. Suazo, M.M.; Martínez, P.G.; and Sandoval, R. Creating psychological and legal contracts through human resource practices: A signaling theory perspective. Human Resource Management Review, 19, 2 (June 2009), 154–166.

65. Throckmorton, C.S.; Mayew, W.J.; Venkatachalam, M.; and Collins, L.M. Financial fraud detection using vocal, linguistic, and financial cues. Decision Support Systems, 74 (June 2015), 78–87.

66. Twyman, N.W.; Elkins, A.C.; Burgoon, J.K.; and Nunamaker, J.F., Jr. A rigidity detection system for automated credibility assessment. Journal of Management Information Systems, 31, 1 (2014), 173–202.

67. Twyman, N.W.; Lowry, P.B.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Autonomous scientifically controlled screening systems for detecting information purposely concealed by individuals. Journal of Management Information Systems, 31, 3 (July 2014), 106–137.

68. Twyman, N.W.; Proudfoot, J.G.; Schuetzler, R.M.; Elkins, A.C.; and Derrick, D.C. Robustness of multiple indicators in automated screening systems for deception detection. Journal of Management Information Systems, 32, 4 (2015), 215–245.

69. Vrij, A. Behavioral correlates of deception in a simulated police interview. Journal of Psychology, 129 (January 1995), 15–28.

70. Vrij, A.; Fisher, R.; Mann, S.; and Leal, S. A cognitive load approach to lie detection. Journal of Investigative Psychology and Ofender Profiling, 5, 1–2 (2008), 39–43.

71. Vrij, A.; Mann, S.; Fisher, R.; Leal, S.; Milne, R.; and Bull, R. Increasing cognitive load to facilitate lie detection: The benefit of recalling an event in reverse order. Law and Human Behavior, 32(2008), 253–265.

72. Vrij, A.; Semin, G.R.; and Bull, R. Insight into behavior displayed during deception. Human Communication Research, 22, 4 (1996), 544–562.

73. Watson, A. Employment trends by typical entry-level education requirement. Monthly Labor Review (September 2017), 1–22.

74. Weiss, B.; and Feldman, R.S. Looking good and lying to do it: Deception as an impression management strategy in job interviews. Journal of Applied Social Psychology, 36, 4 (2006), 1070–1086.

75. Wells, J.D.; Valacich, J.S.; and Hess, T.J. What signal are you sending? How website quality influences perceptions of product quality and purchase intentions. MIS Quarterly, 35, 2 (2011), 373–396.

76. Xiong, X.; and De la Torre, F. Supervised descent method and its applications to face alignment. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Portland, OR, 2013, pp. 532–539.

77. Zhou, L.; Burgoon, J.K.; Nunamaker, J.F.; and Twitchell, D.P. Automating linguistics-based cues for detecting deception in text-based asynchronous computer-mediated communications. Group Decision and Negotiation, 13, 1 (2004), 81–106.

78. Zhou, L.; and Zhang, D. Following linguistic footprints: automatic deception detection in online communication. Communications of the ACM, 51, 9 (2008), 119–122.

79. Zuckerman, M.; Larrance, D.T.; Spiegel, N.H.; and Klorman, R. Controlling nonverbal displays: Facial expressions and tone of voice. Journal of Experimental Social Psychology, 17, 5 (1981), 506–524.

## About the Authors

Nathan W. Twyman (nathantwyman@byu.edu; corresponding author) is an Assistant Professor of Information Systems at Brigham Young University. He received his Ph.D. in Management Information Systems from the University of Arizona. His research interests focus on humancomputer interaction, decision support systems and group support systems, virtual communities, credibility assessment systems, and health IS. He has been a principal investigator of and key contributor to research grants from the National Science Foundation, the Department of Homeland Security, and the Department of Defense. Dr. Twyman’s industry experience is in data management, business intelligence, strategic planning, training, and electronics. His work is published in MIS Quarterly, Journal of Management Information Systems, Journal of the Association for Information Systems, Information and Management, and other outlets.

Steven J. Pentland (stevenpentland@boisestate.edu) is an Assistant Professor of Information Technology and Supply Chain Management at Boise State University. He received his Ph.D. in Management Information Systems from the University of Arizona. His research interests include interpersonal deception, afective computing, automated interviewing, and personnel selection. Dr. Pentland has contributed to a variety of projects supported by the National Science Foundation, Department of Homeland Security, and the Army Research Ofice.

Lee A. Spitzley (lspitzley@albany.edu) is an Assistant Professor of Information Security and Digital Forensics at the University at Albany, SUNY. He received his Ph.D. in Management Information Systems from the University of Arizona. His research interests include understanding how language and nonverbal behavior reflect underlying psychological states and traits, linking language measures to psychological constructs, and using these methods to solve real-world problems in the areas of financial fraud, job interviews, and group interactions.
